"""Frozen, configuration-driven publication study and archival bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray

from openqevo.hamiltonian import PauliHamiltonian
from openqevo.registry import get
from openqevo.result import EvolutionResult
from openqevo.workloads import (
    commutator_graph_density,
    controlled_pauli_hamiltonian,
    h2_two_qubit,
    heisenberg_chain,
    transverse_field_ising,
)

PROTOCOL_SCHEMA_VERSION = "openqevo-publication-study/v1"
RECORD_SCHEMA_VERSION = "openqevo-publication-record/v1"
SUMMARY_SCHEMA_VERSION = "openqevo-publication-summary/v1"
MANIFEST_SCHEMA_VERSION = "openqevo-publication-manifest/v1"

METHOD_ORDER = {"trotter_s1": 0, "trotter_s2": 1, "qdrift": 2}
METHOD_LABELS = {
    "trotter_s1": "First-order Trotter",
    "trotter_s2": "Second-order Trotter",
    "qdrift": "qDRIFT",
}


def load_protocol(path: Path) -> dict[str, Any]:
    """Load and validate a publication protocol."""
    with path.open(encoding="utf-8") as stream:
        protocol = json.load(stream)
    if not isinstance(protocol, dict):
        raise ValueError("Publication protocol must be a JSON object.")
    validate_protocol(protocol)
    return protocol


def validate_protocol(protocol: Mapping[str, Any]) -> None:
    """Validate every field that can change the frozen experiment."""
    if protocol.get("schema_version") != PROTOCOL_SCHEMA_VERSION:
        raise ValueError(f"'schema_version' must be {PROTOCOL_SCHEMA_VERSION!r}.")
    for name in ("protocol_id", "protocol_status", "scientific_review_status"):
        if not isinstance(protocol.get(name), str) or not protocol[name]:
            raise ValueError(f"'{name}' must be a non-empty string.")
    if protocol["protocol_status"] != "software-frozen":
        raise ValueError("'protocol_status' must be 'software-frozen'.")

    _positive_finite(protocol.get("evolution_time"), "evolution_time")
    multipliers = protocol.get("logical_budget_multipliers")
    if not isinstance(multipliers, list) or not multipliers:
        raise ValueError("'logical_budget_multipliers' must be a non-empty list.")
    if any(not _is_positive_integer(value) for value in multipliers):
        raise ValueError("Every logical budget multiplier must be positive.")
    if multipliers != sorted(set(multipliers)):
        raise ValueError("Logical budget multipliers must be sorted and unique.")

    seeds = protocol.get("qdrift_seeds")
    if not isinstance(seeds, list) or not seeds:
        raise ValueError("'qdrift_seeds' must be a non-empty list.")
    if any(not _is_nonnegative_integer(seed) for seed in seeds):
        raise ValueError("Every qDRIFT seed must be a non-negative integer.")
    if len(seeds) != len(set(seeds)):
        raise ValueError("qDRIFT seeds must be unique.")

    _positive_finite(
        protocol.get("target_mean_ci_half_width"), "target_mean_ci_half_width"
    )
    _positive_finite(
        protocol.get("target_expected_channel_error"),
        "target_expected_channel_error",
    )
    _positive_finite(protocol.get("confidence_z"), "confidence_z")
    if not _is_positive_integer(protocol.get("bootstrap_resamples")):
        raise ValueError("'bootstrap_resamples' must be a positive integer.")
    if not _is_nonnegative_integer(protocol.get("bootstrap_seed")):
        raise ValueError("'bootstrap_seed' must be a non-negative integer.")

    tolerances = protocol.get("tolerances")
    if not isinstance(tolerances, Mapping) or not tolerances:
        raise ValueError("'tolerances' must be a non-empty object.")
    for name, value in tolerances.items():
        _positive_finite(value, f"tolerances.{name}")

    workload_specs = protocol.get("workloads")
    if not isinstance(workload_specs, list) or not workload_specs:
        raise ValueError("'workloads' must be a non-empty list.")
    workload_ids = []
    for index, spec in enumerate(workload_specs):
        if not isinstance(spec, Mapping):
            raise ValueError(f"Workload {index} must be an object.")
        if not isinstance(spec.get("id"), str) or not spec["id"]:
            raise ValueError(f"Workload {index} must have a non-empty 'id'.")
        if spec.get("kind") not in {"controlled", "tfim", "heisenberg", "h2"}:
            raise ValueError(f"Workload {spec['id']!r} has an unsupported 'kind'.")
        workload_ids.append(spec["id"])
    if len(workload_ids) != len(set(workload_ids)):
        raise ValueError("Workload ids must be unique.")


def build_workloads(protocol: Mapping[str, Any]) -> list[PauliHamiltonian]:
    """Construct every workload declared by a validated protocol."""
    validate_protocol(protocol)
    workloads = []
    for spec in protocol["workloads"]:
        identifier = str(spec["id"])
        kind = spec["kind"]
        parameters = dict(spec.get("parameters", {}))
        if kind == "controlled":
            workload = controlled_pauli_hamiltonian(**parameters, identifier=identifier)
        elif kind == "tfim":
            workload = _with_identifier(
                transverse_field_ising(**parameters), identifier
            )
        elif kind == "heisenberg":
            workload = _with_identifier(heisenberg_chain(**parameters), identifier)
        else:
            if parameters:
                raise ValueError("The fixed H2 workload accepts no parameters.")
            workload = _with_identifier(h2_two_qubit(), identifier)
        workloads.append(workload)
    return workloads


def estimate_resources(
    protocol: Mapping[str, Any], workloads: Sequence[PauliHamiltonian]
) -> dict[str, Any]:
    """Estimate deterministic record and logical-operation counts before a run."""
    validate_protocol(protocol)
    seeds = len(protocol["qdrift_seeds"])
    multipliers = protocol["logical_budget_multipliers"]
    workload_estimates = []
    total_records = 0
    total_formula_operations = 0
    for hamiltonian in workloads:
        term_count = len(hamiltonian.terms)
        budgets = [2 * term_count * multiplier for multiplier in multipliers]
        records = 1 + len(budgets) * (2 + seeds)
        operations = sum(budgets) * (2 + seeds)
        total_records += records
        total_formula_operations += operations
        workload_estimates.append(
            {
                "workload_id": hamiltonian.identifier,
                "qubits": hamiltonian.n_qubits,
                "dense_dimension": 2**hamiltonian.n_qubits,
                "terms": term_count,
                "logical_budgets": budgets,
                "records": records,
                "formula_level_pauli_operations": operations,
            }
        )
    return {
        "schema_version": "openqevo-publication-resource-estimate/v1",
        "total_workloads": len(workloads),
        "total_records": total_records,
        "total_formula_level_pauli_operations": total_formula_operations,
        "qdrift_trajectories_per_budget": seeds,
        "workloads": workload_estimates,
    }


def run_study(protocol: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Execute the frozen native-method study while retaining failures."""
    validate_protocol(protocol)
    protocol_hash = _json_sha256(protocol)
    run_id = f"{protocol['protocol_id']}:{protocol_hash[:16]}"
    evolution_time = float(protocol["evolution_time"])
    records: list[dict[str, Any]] = []
    for hamiltonian in build_workloads(protocol):
        initial_state = np.zeros(2**hamiltonian.n_qubits, dtype=complex)
        initial_state[0] = 1.0
        try:
            exact_result = get("exact").run(hamiltonian, evolution_time)
        except Exception as exc:  # study contract retains unexpected failures
            records.append(
                _failure_record(
                    run_id,
                    protocol,
                    protocol_hash,
                    hamiltonian,
                    method="exact",
                    logical_budget=None,
                    parameters={"evolution_time": evolution_time},
                    exc=exc,
                )
            )
            continue

        exact_unitary = exact_result.unitary
        exact_state = exact_unitary @ initial_state
        records.append(
            _success_record(
                run_id,
                protocol,
                protocol_hash,
                hamiltonian,
                logical_budget=None,
                result=exact_result,
                exact_unitary=exact_unitary,
                exact_state=exact_state,
                initial_state=initial_state,
            )
        )
        term_count = len(hamiltonian.terms)
        for multiplier in protocol["logical_budget_multipliers"]:
            budget = 2 * term_count * int(multiplier)
            requests = [
                ("trotter_s1", {"steps": budget // term_count}),
                ("trotter_s2", {"steps": budget // (2 * term_count)}),
            ]
            requests.extend(
                ("qdrift", {"samples": budget, "seed": int(seed)})
                for seed in protocol["qdrift_seeds"]
            )
            for method_name, parameters in requests:
                try:
                    result = get(method_name).run(
                        hamiltonian, evolution_time, **parameters
                    )
                    records.append(
                        _success_record(
                            run_id,
                            protocol,
                            protocol_hash,
                            hamiltonian,
                            logical_budget=budget,
                            result=result,
                            exact_unitary=exact_unitary,
                            exact_state=exact_state,
                            initial_state=initial_state,
                        )
                    )
                except Exception as exc:  # preserve instead of dropping a run
                    records.append(
                        _failure_record(
                            run_id,
                            protocol,
                            protocol_hash,
                            hamiltonian,
                            method=method_name,
                            logical_budget=budget,
                            parameters=parameters,
                            exc=exc,
                        )
                    )
    return records


def summarize_records(
    records: Sequence[Mapping[str, Any]], protocol: Mapping[str, Any]
) -> dict[str, Any]:
    """Derive deterministic group statistics and qDRIFT ensemble sizing."""
    validate_protocol(protocol)
    if not records:
        raise ValueError("At least one study record is required.")
    exact_states = {
        str(record["workload_id"]): _decode_state(record["output_state"])
        for record in records
        if record.get("status") == "success" and record.get("method") == "exact"
    }
    groups: dict[tuple[str, str, int], list[Mapping[str, Any]]] = defaultdict(list)
    failures = []
    for record in records:
        if record.get("status") != "success":
            failures.append(record)
        elif record.get("method") != "exact":
            groups[
                (
                    str(record["workload_id"]),
                    str(record["method"]),
                    int(record["logical_budget"]),
                )
            ].append(record)

    group_summaries = []
    for (workload_id, method, budget), group in sorted(
        groups.items(),
        key=lambda item: (
            item[0][0],
            item[0][2],
            METHOD_ORDER[item[0][1]],
        ),
    ):
        operator_errors = [
            float(record["metrics"]["phase_aligned_operator_error"]) for record in group
        ]
        state_distances = [
            float(record["metrics"]["state_trace_distance"]) for record in group
        ]
        seed_offset = int(hashlib.sha256(workload_id.encode()).hexdigest()[:8], 16)
        seed_offset += budget + 100_000 * METHOD_ORDER[method]
        operator_summary = _distribution_summary(
            operator_errors,
            resamples=int(protocol["bootstrap_resamples"]),
            seed=int(protocol["bootstrap_seed"]) + seed_offset,
        )
        state_summary = _distribution_summary(
            state_distances,
            resamples=int(protocol["bootstrap_resamples"]),
            seed=int(protocol["bootstrap_seed"]) + seed_offset + 50_000,
        )
        summary: dict[str, Any] = {
            "workload_id": workload_id,
            "method": method,
            "method_label": METHOD_LABELS[method],
            "logical_budget": budget,
            "trajectories": len(group),
            "phase_aligned_operator_error": operator_summary,
            "state_trace_distance": state_summary,
            "costs": _cost_summary(group),
        }
        if method == "qdrift":
            exact_state = exact_states[workload_id]
            states = [_decode_state(record["output_state"]) for record in group]
            ensemble = sum(np.outer(state, state.conj()) for state in states) / len(
                states
            )
            exact_density = np.outer(exact_state, exact_state.conj())
            standard_deviation = float(state_summary["standard_deviation"])
            half_width = float(protocol["target_mean_ci_half_width"])
            z_value = float(protocol["confidence_z"])
            required = max(
                1, math.ceil((z_value * standard_deviation / half_width) ** 2)
            )
            summary["empirical_ensemble_state_trace_distance"] = (
                _density_trace_distance(ensemble, exact_density)
            )
            summary["qdrift_ensemble_sizing"] = {
                "statistic": "mean individual-trajectory state trace distance",
                "target_ci_half_width": half_width,
                "confidence_z": z_value,
                "pilot_standard_deviation": standard_deviation,
                "estimated_trajectories": required,
                "estimator": "normal approximation; review required before inference",
            }

        group_summaries.append(summary)

    workload_summaries = []
    for exact in (
        record
        for record in records
        if record.get("status") == "success" and record.get("method") == "exact"
    ):
        hamiltonian = exact["hamiltonian"]
        target = float(protocol["target_expected_channel_error"])
        theory_samples = math.ceil(
            2
            * float(hamiltonian["lambda"]) ** 2
            * float(protocol["evolution_time"]) ** 2
            / target
        )
        workload_summaries.append(
            {
                "workload_id": exact["workload_id"],
                "input_sha256": exact["input_sha256"],
                "qubits": hamiltonian["qubits"],
                "terms": len(hamiltonian["terms"]),
                "lambda": hamiltonian["lambda"],
                "commutator_graph_density": exact["workload_features"][
                    "commutator_graph_density"
                ],
                "qdrift_small_step_sample_estimate": {
                    "target_expected_channel_error": target,
                    "samples": theory_samples,
                    "formula": "ceil(2 * lambda^2 * t^2 / epsilon)",
                    "scope": "small-step expected-channel approximation",
                },
            }
        )

    first = records[0]
    return {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "run_id": first["run_id"],
        "protocol_id": first["protocol_id"],
        "protocol_sha256": first["protocol_sha256"],
        "protocol_status": protocol["protocol_status"],
        "scientific_review_status": protocol["scientific_review_status"],
        "comparison_basis": "equal formula-level Pauli-evolution operations",
        "initial_state": "computational |0...0>",
        "workloads": workload_summaries,
        "groups": group_summaries,
        "failures": {
            "count": len(failures),
            "records": [
                {
                    "workload_id": record["workload_id"],
                    "method": record["method"],
                    "logical_budget": record["logical_budget"],
                    "failure": record["failure"],
                }
                for record in failures
            ],
        },
    }


def generate_bundle(
    protocol_path: Path, output_dir: Path, *, create_plot: bool = True
) -> dict[str, Path]:
    """Create a write-once study bundle with checksums for every artifact."""
    protocol = load_protocol(protocol_path)
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(
            "Refusing to modify an existing study bundle; choose a new directory."
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "protocol": output_dir / "protocol.json",
        "workloads": output_dir / "workloads.json",
        "resources": output_dir / "resource_estimate.json",
        "records": output_dir / "study_records.jsonl",
        "summary": output_dir / "study_summary.json",
        "figure": output_dir / "study_overview.svg",
        "manifest": output_dir / "manifest.json",
    }
    workloads = build_workloads(protocol)
    _write_json(paths["protocol"], protocol)
    _write_json(paths["workloads"], [workload.to_dict() for workload in workloads])
    _write_json(paths["resources"], estimate_resources(protocol, workloads))
    records = run_study(protocol)
    _write_jsonl(paths["records"], records)
    summary = summarize_records(_read_jsonl(paths["records"]), protocol)
    _write_json(paths["summary"], summary)
    if create_plot:
        plot_summary(summary, paths["figure"])

    archived = [
        path for key, path in paths.items() if key != "manifest" and path.exists()
    ]
    manifest = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "run_id": summary["run_id"],
        "scientific_review_status": protocol["scientific_review_status"],
        "files": {
            path.name: {"bytes": path.stat().st_size, "sha256": _file_sha256(path)}
            for path in archived
        },
    }
    _write_json(paths["manifest"], manifest)
    return {key: path for key, path in paths.items() if path.exists()}


def verify_bundle(bundle_dir: Path) -> dict[str, Any]:
    """Verify an archived study bundle without modifying it.

    Verification covers the byte manifest and the cross-file invariants needed
    to use a bundle as publication evidence.  It deliberately does not confer
    scientific approval.
    """
    if not bundle_dir.is_dir():
        raise ValueError(f"Study bundle does not exist: {bundle_dir}")

    manifest = _read_json_object(bundle_dir / "manifest.json", "manifest")
    if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        raise ValueError(
            f"Manifest 'schema_version' must be {MANIFEST_SCHEMA_VERSION!r}."
        )
    files = manifest.get("files")
    if not isinstance(files, Mapping) or not files:
        raise ValueError("Manifest 'files' must be a non-empty object.")

    integrity_errors: list[str] = []
    expected_names: set[str] = set()
    for name, metadata in files.items():
        if not isinstance(name, str) or Path(name).name != name:
            integrity_errors.append(f"unsafe manifest path {name!r}")
            continue
        expected_names.add(name)
        if not isinstance(metadata, Mapping):
            integrity_errors.append(f"invalid metadata for {name!r}")
            continue
        path = bundle_dir / name
        if not path.is_file():
            integrity_errors.append(f"missing file {name!r}")
            continue
        if metadata.get("bytes") != path.stat().st_size:
            integrity_errors.append(f"byte-count mismatch for {name!r}")
        if metadata.get("sha256") != _file_sha256(path):
            integrity_errors.append(f"SHA-256 mismatch for {name!r}")

    actual_names = {
        path.name
        for path in bundle_dir.iterdir()
        if path.is_file() and path.name != "manifest.json"
    }
    for name in sorted(actual_names - expected_names):
        integrity_errors.append(f"unmanifested file {name!r}")
    if integrity_errors:
        raise ValueError(
            "Bundle byte-integrity verification failed: "
            + "; ".join(integrity_errors)
        )

    required = {
        "protocol.json",
        "resource_estimate.json",
        "study_records.jsonl",
        "study_summary.json",
        "workloads.json",
    }
    missing_required = sorted(required - expected_names)
    if missing_required:
        raise ValueError(
            "Bundle manifest is missing required artifacts: "
            + ", ".join(missing_required)
        )

    protocol = load_protocol(bundle_dir / "protocol.json")
    resources = _read_json_object(
        bundle_dir / "resource_estimate.json", "resource estimate"
    )
    summary = _read_json_object(bundle_dir / "study_summary.json", "study summary")
    workloads = _read_json_list(bundle_dir / "workloads.json", "workloads")
    records = _read_jsonl(bundle_dir / "study_records.jsonl")

    consistency_errors: list[str] = []
    run_id = summary.get("run_id")
    protocol_hash = _json_sha256(protocol)
    statuses = {
        manifest.get("scientific_review_status"),
        protocol.get("scientific_review_status"),
        summary.get("scientific_review_status"),
    }
    if len(statuses) != 1:
        consistency_errors.append("scientific-review statuses differ")
    if manifest.get("run_id") != run_id:
        consistency_errors.append("manifest and summary run ids differ")
    if summary.get("protocol_id") != protocol.get("protocol_id"):
        consistency_errors.append("protocol ids differ")
    if summary.get("protocol_sha256") != protocol_hash:
        consistency_errors.append("summary protocol hash is incorrect")
    if resources.get("total_records") != len(records):
        consistency_errors.append("resource-estimate record count is incorrect")
    if resources.get("total_workloads") != len(workloads):
        consistency_errors.append("resource-estimate workload count is incorrect")

    workload_ids = {
        workload.get("id")
        for workload in workloads
        if isinstance(workload, Mapping)
    }
    protocol_workload_ids = {spec["id"] for spec in protocol["workloads"]}
    if workload_ids != protocol_workload_ids:
        consistency_errors.append("archived workloads differ from the protocol")

    failure_count = sum(record.get("status") != "success" for record in records)
    if summary.get("failures", {}).get("count") != failure_count:
        consistency_errors.append("summary failure count is incorrect")

    budget_violations = 0
    qdrift_seeds: dict[tuple[str, int], set[int]] = defaultdict(set)
    exact_counts: dict[str, int] = defaultdict(int)
    for record in records:
        if record.get("run_id") != run_id:
            consistency_errors.append("a record has an inconsistent run id")
            break
        if record.get("protocol_sha256") != protocol_hash:
            consistency_errors.append("a record has an inconsistent protocol hash")
            break
        workload_id = str(record.get("workload_id"))
        if workload_id not in protocol_workload_ids:
            consistency_errors.append("a record references an unknown workload")
            break
        method = record.get("method")
        if method == "exact":
            exact_counts[workload_id] += 1
            continue
        budget = record.get("logical_budget")
        if record.get("status") == "success" and (
            not isinstance(budget, int)
            or record.get("costs", {}).get("formula_level_pauli_operations") != budget
        ):
            budget_violations += 1
        if method == "qdrift" and isinstance(budget, int):
            seed = record.get("parameters", {}).get("seed")
            if isinstance(seed, int):
                qdrift_seeds[(workload_id, budget)].add(seed)

    if budget_violations:
        consistency_errors.append(
            f"{budget_violations} successful records violate equal logical budgets"
        )
    if exact_counts != {workload_id: 1 for workload_id in protocol_workload_ids}:
        consistency_errors.append("each workload must have exactly one exact record")

    expected_seeds = set(protocol["qdrift_seeds"])
    expected_qdrift_groups = len(protocol_workload_ids) * len(
        protocol["logical_budget_multipliers"]
    )
    if len(qdrift_seeds) != expected_qdrift_groups or any(
        seeds != expected_seeds for seeds in qdrift_seeds.values()
    ):
        consistency_errors.append("qDRIFT groups do not contain every frozen seed")

    expected_groups = expected_qdrift_groups * len(METHOD_ORDER)
    if len(summary.get("groups", [])) != expected_groups:
        consistency_errors.append("summary method-group count is incorrect")
    if consistency_errors:
        raise ValueError(
            "Bundle cross-file verification failed: "
            + "; ".join(consistency_errors)
        )

    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "status": "passed",
        "bundle": str(bundle_dir),
        "run_id": run_id,
        "scientific_review_status": protocol["scientific_review_status"],
        "files": len(expected_names),
        "workloads": len(workloads),
        "records": len(records),
        "groups": len(summary["groups"]),
        "failures": failure_count,
        "equal_budget_violations": budget_violations,
        "qdrift_trajectories_per_group": len(expected_seeds),
    }


def plot_summary(summary: Mapping[str, Any], output_path: Path) -> None:
    """Plot cross-workload accuracy and compiled two-qubit gate costs."""
    try:
        import matplotlib
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            'Plotting requires: python -m pip install -e ".[visualization]"'
        ) from exc

    matplotlib.rcParams["svg.hashsalt"] = str(summary["run_id"])
    colors = {"trotter_s1": "#306A91", "trotter_s2": "#AE1935", "qdrift": "#D9782D"}
    by_method_budget: dict[tuple[str, int], list[Mapping[str, Any]]] = defaultdict(list)
    for group in summary["groups"]:
        by_method_budget[(group["method"], group["logical_budget"])].append(group)

    figure, axes = plt.subplots(1, 2, figsize=(13.2, 5.6), constrained_layout=True)
    figure.patch.set_facecolor("#F4F1E9")
    for axis in axes:
        axis.set_facecolor("#FFFDF8")
        axis.grid(True, which="both", color="#101D2D", alpha=0.12, linewidth=0.8)
    for method in METHOD_ORDER:
        grouped = sorted(
            (
                (budget, groups)
                for (name, budget), groups in by_method_budget.items()
                if name == method
            ),
            key=lambda item: item[0],
        )
        budgets = [budget for budget, _ in grouped]
        errors = [
            float(np.median([g["state_trace_distance"]["mean"] for g in groups]))
            for _, groups in grouped
        ]
        gates = [
            float(np.median([g["costs"]["compiled_two_qubit_gates"] for g in groups]))
            for _, groups in grouped
        ]
        axes[0].loglog(
            budgets, errors, "o-", color=colors[method], label=METHOD_LABELS[method]
        )
        axes[1].loglog(
            budgets,
            np.maximum(gates, 0.5),
            "o-",
            color=colors[method],
            label=METHOD_LABELS[method],
        )
    axes[0].set_title(
        "Median state error across workloads", loc="left", fontweight="bold"
    )
    axes[0].set_ylabel("Mean trajectory trace distance")
    axes[1].set_title("Median compiled logical cost", loc="left", fontweight="bold")
    axes[1].set_ylabel("Two-qubit gates (0 displayed at 0.5)")
    for axis in axes:
        axis.set_xlabel("Formula-level Pauli operations")
        axis.legend(frameon=False)
    figure.suptitle(
        "OpenQEvo software-frozen publication study",
        x=0.02,
        ha="left",
        fontsize=17,
        fontweight="bold",
        color="#101D2D",
    )
    figure.savefig(
        output_path,
        format="svg",
        facecolor=figure.get_facecolor(),
        metadata={
            "Title": "OpenQEvo publication study",
            "Creator": "openqevo.study",
            "Date": None,
        },
    )
    plt.close(figure)
    normalized = "\n".join(
        line.rstrip() for line in output_path.read_text(encoding="utf-8").splitlines()
    )
    output_path.write_text(normalized + "\n", encoding="utf-8")


def _success_record(
    run_id: str,
    protocol: Mapping[str, Any],
    protocol_hash: str,
    hamiltonian: PauliHamiltonian,
    *,
    logical_budget: int | None,
    result: EvolutionResult,
    exact_unitary: NDArray[np.complexfloating],
    exact_state: NDArray[np.complexfloating],
    initial_state: NDArray[np.complexfloating],
) -> dict[str, Any]:
    state = result.unitary @ initial_state
    return {
        **_record_base(run_id, protocol, protocol_hash, hamiltonian),
        "status": "success",
        "method": result.method_name,
        "logical_budget": logical_budget,
        "result_schema_version": result.to_metadata()["schema_version"],
        "implementation": result.implementation.to_dict(),
        "environment": dict(result.environment),
        "parameters": dict(result.parameters),
        "costs": result.costs.to_dict(),
        "sampled_sequence": (
            list(result.sampled_sequence)
            if result.sampled_sequence is not None
            else None
        ),
        "metrics": _accuracy_metrics(result.unitary, state, exact_unitary, exact_state),
        "output_state": _encode_state(state),
        "output_sha256": result.output_sha256,
        "warnings": list(result.warnings),
        "limitations": list(result.limitations),
        "failure": None,
    }


def _failure_record(
    run_id: str,
    protocol: Mapping[str, Any],
    protocol_hash: str,
    hamiltonian: PauliHamiltonian,
    *,
    method: str,
    logical_budget: int | None,
    parameters: Mapping[str, Any],
    exc: Exception,
) -> dict[str, Any]:
    return {
        **_record_base(run_id, protocol, protocol_hash, hamiltonian),
        "status": "failure",
        "method": method,
        "logical_budget": logical_budget,
        "parameters": dict(parameters),
        "costs": None,
        "sampled_sequence": None,
        "metrics": None,
        "output_state": None,
        "output_sha256": None,
        "failure": {"type": type(exc).__name__, "message": str(exc)},
    }


def _record_base(
    run_id: str,
    protocol: Mapping[str, Any],
    protocol_hash: str,
    hamiltonian: PauliHamiltonian,
) -> dict[str, Any]:
    return {
        "schema_version": RECORD_SCHEMA_VERSION,
        "run_id": run_id,
        "protocol_id": protocol["protocol_id"],
        "protocol_sha256": protocol_hash,
        "workload_id": hamiltonian.identifier,
        "input_sha256": hamiltonian.sha256,
        "hamiltonian": hamiltonian.to_dict(),
        "workload_features": {
            "family": hamiltonian.mapping_metadata.get("family", "unspecified"),
            "commutator_graph_density": commutator_graph_density(hamiltonian),
        },
    }


def _accuracy_metrics(
    unitary: NDArray[np.complexfloating],
    state: NDArray[np.complexfloating],
    exact_unitary: NDArray[np.complexfloating],
    exact_state: NDArray[np.complexfloating],
) -> dict[str, float]:
    overlap = np.trace(exact_unitary.conj().T @ unitary)
    phase = 1.0 + 0.0j if abs(overlap) < 1e-15 else overlap.conjugate() / abs(overlap)
    operator_error = np.linalg.norm(phase * unitary - exact_unitary, ord=2)
    denominator = np.linalg.norm(exact_unitary, ord=2)
    fidelity = float(abs(np.vdot(exact_state, state)) ** 2)
    infidelity = float(np.clip(1.0 - fidelity, 0.0, 1.0))
    return {
        "phase_aligned_operator_error": float(operator_error / denominator),
        "state_infidelity": infidelity,
        "state_trace_distance": float(math.sqrt(infidelity)),
    }


def _distribution_summary(
    values: Sequence[float], *, resamples: int, seed: int
) -> dict[str, float | int]:
    array = np.asarray(values, dtype=float)
    mean = float(np.mean(array))
    if array.size == 1:
        standard_deviation = 0.0
        low = high = mean
    else:
        standard_deviation = float(np.std(array, ddof=1))
        rng = np.random.default_rng(seed)
        indices = rng.integers(0, array.size, size=(resamples, array.size))
        low, high = (
            float(value)
            for value in np.quantile(np.mean(array[indices], axis=1), [0.025, 0.975])
        )
    return {
        "count": int(array.size),
        "mean": mean,
        "standard_deviation": standard_deviation,
        "minimum": float(np.min(array)),
        "median": float(np.median(array)),
        "maximum": float(np.max(array)),
        "mean_ci95_low": low,
        "mean_ci95_high": high,
    }


def _cost_summary(group: Sequence[Mapping[str, Any]]) -> dict[str, float]:
    names = (
        "formula_level_pauli_operations",
        "adjacent_merged_pauli_operations",
        "compiled_one_qubit_gates",
        "compiled_two_qubit_gates",
        "circuit_depth",
    )
    return {
        name: float(np.mean([record["costs"][name] for record in group]))
        for name in names
    }


def _density_trace_distance(
    density: NDArray[np.complexfloating], exact_density: NDArray[np.complexfloating]
) -> float:
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(density - exact_density))))


def _encode_state(state: NDArray[np.complexfloating]) -> dict[str, list[float]]:
    return {
        "real": [float(value) for value in np.real(state)],
        "imag": [float(value) for value in np.imag(state)],
    }


def _decode_state(encoded: Mapping[str, Sequence[float]]) -> NDArray[np.complex128]:
    return np.asarray(encoded["real"], dtype=float) + 1j * np.asarray(
        encoded["imag"], dtype=float
    )


def _with_identifier(
    hamiltonian: PauliHamiltonian, identifier: str
) -> PauliHamiltonian:
    return PauliHamiltonian(
        terms=hamiltonian.terms,
        identifier=identifier,
        source=hamiltonian.source,
        units=hamiltonian.units,
        mapping_metadata=hamiltonian.mapping_metadata,
    )


def _positive_finite(value: Any, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"'{name}' must be a positive finite number.")
    if not math.isfinite(float(value)) or value <= 0:
        raise ValueError(f"'{name}' must be a positive finite number.")


def _is_positive_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _is_nonnegative_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _canonical_json(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def _json_sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _write_jsonl(path: Path, records: Sequence[Mapping[str, Any]]) -> None:
    with path.open("x", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            stream.write("\n")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"Archived {label} must be a JSON object.")
    return value


def _read_json_list(path: Path, label: str) -> list[Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, list):
        raise ValueError(f"Archived {label} must be a JSON array.")
    return value


def main(argv: Sequence[str] | None = None) -> None:
    """Execute a frozen study into a new immutable bundle directory."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--verify-bundle", type=Path)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args(argv)
    if args.verify_bundle is not None:
        if args.protocol is not None or args.output_dir is not None or args.no_plot:
            parser.error("--verify-bundle cannot be combined with generation options")
        try:
            report = verify_bundle(args.verify_bundle)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            parser.error(str(exc))
        print(json.dumps(report, indent=2, sort_keys=True))
        return
    if args.protocol is None or args.output_dir is None:
        parser.error(
            "--protocol and --output-dir are required when generating a bundle"
        )
    try:
        paths = generate_bundle(
            args.protocol, args.output_dir, create_plot=not args.no_plot
        )
    except FileExistsError as exc:
        parser.error(str(exc))
    print(f"Study bundle: {args.output_dir}")
    for name, path in paths.items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main()
