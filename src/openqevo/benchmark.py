"""Configuration-driven benchmark support for the OpenQEvo paper pilot.

The first benchmark is deliberately small: a one-qubit ``H = X + Z`` control
that compares exact evolution, first- and second-order Trotter formulas, and a
seeded qDRIFT ensemble under equal formula-level Pauli-operation budgets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from collections import defaultdict
from collections.abc import Mapping, Sequence
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

import numpy as np
import scipy
from numpy.typing import NDArray

from openqevo.registry import get

CONFIG_SCHEMA_VERSION = "openqevo-xz-pilot-config/v1"
RECORD_SCHEMA_VERSION = "openqevo-benchmark-record/v1"
SUMMARY_SCHEMA_VERSION = "openqevo-benchmark-summary/v1"
MANIFEST_SCHEMA_VERSION = "openqevo-benchmark-manifest/v1"

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
INITIAL_STATE = np.array([1, 0], dtype=complex)

METHOD_ORDER = {"trotter_s1": 0, "trotter_s2": 1, "qdrift": 2}
METHOD_LABELS = {
    "trotter_s1": "First-order Trotter",
    "trotter_s2": "Second-order Trotter",
    "qdrift": "qDRIFT",
}


def load_config(path: Path) -> dict[str, Any]:
    """Load and validate a pilot configuration from JSON."""
    with path.open(encoding="utf-8") as stream:
        config = json.load(stream)
    if not isinstance(config, dict):
        raise ValueError("Pilot configuration must be a JSON object.")
    validate_config(config)
    return config


def validate_config(config: Mapping[str, Any]) -> None:
    """Validate the fields needed by the fixed ``X + Z`` pilot."""
    if config.get("schema_version") != CONFIG_SCHEMA_VERSION:
        raise ValueError(f"'schema_version' must be {CONFIG_SCHEMA_VERSION!r}.")
    if not isinstance(config.get("benchmark_id"), str) or not config["benchmark_id"]:
        raise ValueError("'benchmark_id' must be a non-empty string.")

    evolution_time = config.get("evolution_time")
    if not isinstance(evolution_time, (int, float)) or isinstance(evolution_time, bool):
        raise ValueError("'evolution_time' must be a finite number.")
    if not np.isfinite(evolution_time) or evolution_time <= 0:
        raise ValueError("'evolution_time' must be positive and finite.")

    budgets = config.get("logical_budgets")
    if not isinstance(budgets, list) or not budgets:
        raise ValueError("'logical_budgets' must be a non-empty list.")
    if any(not _is_integer(value) or value < 4 or value % 4 for value in budgets):
        raise ValueError("Each logical budget must be a positive multiple of 4.")
    if budgets != sorted(set(budgets)):
        raise ValueError("'logical_budgets' must be sorted and unique.")

    seeds = config.get("qdrift_seeds")
    if not isinstance(seeds, list) or not seeds:
        raise ValueError("'qdrift_seeds' must be a non-empty list.")
    if any(not _is_integer(seed) or seed < 0 for seed in seeds):
        raise ValueError("Each qDRIFT seed must be a non-negative integer.")
    if len(seeds) != len(set(seeds)):
        raise ValueError("'qdrift_seeds' must be unique.")

    bootstrap_resamples = config.get("bootstrap_resamples")
    bootstrap_seed = config.get("bootstrap_seed")
    if not _is_integer(bootstrap_resamples) or bootstrap_resamples < 1:
        raise ValueError("'bootstrap_resamples' must be a positive integer.")
    if not _is_integer(bootstrap_seed) or bootstrap_seed < 0:
        raise ValueError("'bootstrap_seed' must be a non-negative integer.")


def run_pilot(config: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Run the deterministic methods and qDRIFT ensemble for ``H = X + Z``."""
    validate_config(config)
    config_hash = _json_sha256(config)
    run_id = f"{config['benchmark_id']}:{config_hash[:16]}"
    environment = _environment()
    hamiltonian = {
        "id": "pauli-x-plus-z",
        "qubits": 1,
        "terms": [
            {"coefficient": 1.0, "pauli_word": "X"},
            {"coefficient": 1.0, "pauli_word": "Z"},
        ],
        "lambda": 2.0,
    }
    input_hash = _json_sha256(hamiltonian)
    terms = [SIGMA_X, SIGMA_Z]
    evolution_time = float(config["evolution_time"])

    exact_method = get("exact")
    exact_unitary = exact_method.evolve(terms, evolution_time)
    exact_state = exact_unitary @ INITIAL_STATE
    records = [
        _record(
            run_id=run_id,
            benchmark_id=str(config["benchmark_id"]),
            config_hash=config_hash,
            input_hash=input_hash,
            environment=environment,
            method_name="exact",
            method_source=exact_method.source,
            logical_budget=None,
            parameters={"evolution_time": evolution_time},
            sampled_sequence=None,
            formula_operations=0,
            merged_operations=0,
            unitary=exact_unitary,
            exact_unitary=exact_unitary,
            exact_state=exact_state,
        )
    ]

    first_order = get("trotter_s1")
    second_order = get("trotter_s2")
    qdrift = get("qdrift")

    for logical_budget in config["logical_budgets"]:
        first_steps = logical_budget // len(terms)
        first_unitary = first_order.evolve(terms, evolution_time, steps=first_steps)
        records.append(
            _record(
                run_id=run_id,
                benchmark_id=str(config["benchmark_id"]),
                config_hash=config_hash,
                input_hash=input_hash,
                environment=environment,
                method_name="trotter_s1",
                method_source=first_order.source,
                logical_budget=logical_budget,
                parameters={
                    "evolution_time": evolution_time,
                    "steps": first_steps,
                    "term_order": ["X", "Z"],
                },
                sampled_sequence=None,
                formula_operations=logical_budget,
                merged_operations=logical_budget,
                unitary=first_unitary,
                exact_unitary=exact_unitary,
                exact_state=exact_state,
            )
        )

        second_steps = logical_budget // (2 * len(terms))
        second_unitary = second_order.evolve(terms, evolution_time, steps=second_steps)
        records.append(
            _record(
                run_id=run_id,
                benchmark_id=str(config["benchmark_id"]),
                config_hash=config_hash,
                input_hash=input_hash,
                environment=environment,
                method_name="trotter_s2",
                method_source=second_order.source,
                logical_budget=logical_budget,
                parameters={
                    "evolution_time": evolution_time,
                    "steps": second_steps,
                    "term_order": ["X", "Z"],
                },
                sampled_sequence=None,
                formula_operations=logical_budget,
                merged_operations=2 * second_steps * (len(terms) - 1) + 1,
                unitary=second_unitary,
                exact_unitary=exact_unitary,
                exact_state=exact_state,
            )
        )

        for seed in config["qdrift_seeds"]:
            sequence = qdrift.sample_sequence(
                terms,
                samples=logical_budget,
                seed=seed,
            )
            qdrift_unitary = qdrift.evolve(
                terms,
                evolution_time,
                samples=logical_budget,
                sampled_sequence=sequence,
            )
            records.append(
                _record(
                    run_id=run_id,
                    benchmark_id=str(config["benchmark_id"]),
                    config_hash=config_hash,
                    input_hash=input_hash,
                    environment=environment,
                    method_name="qdrift",
                    method_source=qdrift.source,
                    logical_budget=logical_budget,
                    parameters={
                        "evolution_time": evolution_time,
                        "samples": logical_budget,
                        "seed": seed,
                        "term_weights": [1.0, 1.0],
                    },
                    sampled_sequence=sequence,
                    formula_operations=logical_budget,
                    merged_operations=_adjacent_merged_count(sequence),
                    unitary=qdrift_unitary,
                    exact_unitary=exact_unitary,
                    exact_state=exact_state,
                )
            )

    return records


def summarize_records(
    records: Sequence[Mapping[str, Any]],
    config: Mapping[str, Any],
) -> dict[str, Any]:
    """Aggregate raw records without rerunning any evolution method."""
    validate_config(config)
    if not records:
        raise ValueError("At least one benchmark record is required.")

    exact_records = [record for record in records if record.get("method") == "exact"]
    if len(exact_records) != 1:
        raise ValueError("Exactly one exact reference record is required.")
    exact_state = _decode_state(exact_records[0]["output_state"])

    groups: dict[tuple[str, int], list[Mapping[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("status") != "success" or record.get("method") == "exact":
            continue
        groups[(str(record["method"]), int(record["logical_budget"]))].append(record)

    summaries = []
    bootstrap_seed = int(config["bootstrap_seed"])
    bootstrap_resamples = int(config["bootstrap_resamples"])
    for (method_name, logical_budget), group in sorted(
        groups.items(), key=lambda item: (item[0][1], METHOD_ORDER[item[0][0]])
    ):
        operator_errors = [
            float(record["metrics"]["normalized_operator_error"]) for record in group
        ]
        state_distances = [
            float(record["metrics"]["state_trace_distance"]) for record in group
        ]
        states = [_decode_state(record["output_state"]) for record in group]
        ensemble_state = sum(np.outer(state, state.conj()) for state in states) / len(
            states
        )
        exact_density = np.outer(exact_state, exact_state.conj())

        seed_offset = 100_000 * METHOD_ORDER[method_name] + logical_budget
        summaries.append(
            {
                "method": method_name,
                "method_label": METHOD_LABELS[method_name],
                "logical_budget": logical_budget,
                "trajectories": len(group),
                "normalized_operator_error": _distribution_summary(
                    operator_errors,
                    bootstrap_resamples=bootstrap_resamples,
                    bootstrap_seed=bootstrap_seed + seed_offset,
                ),
                "state_trace_distance": _distribution_summary(
                    state_distances,
                    bootstrap_resamples=bootstrap_resamples,
                    bootstrap_seed=bootstrap_seed + seed_offset + 50_000,
                ),
                "empirical_ensemble_state_trace_distance": _density_trace_distance(
                    ensemble_state, exact_density
                ),
            }
        )

    first = records[0]
    return {
        "schema_version": SUMMARY_SCHEMA_VERSION,
        "run_id": first["run_id"],
        "benchmark_id": first["benchmark_id"],
        "config_sha256": first["config_sha256"],
        "environment": first["environment"],
        "initial_state": "|0>",
        "comparison_basis": "equal formula-level Pauli evolution operations",
        "groups": summaries,
    }


def write_records(path: Path, records: Sequence[Mapping[str, Any]]) -> None:
    """Create an immutable JSON Lines record stream for one benchmark run."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            stream.write("\n")


def read_records(path: Path) -> list[dict[str, Any]]:
    """Read a benchmark JSON Lines stream."""
    records = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError(f"Record on line {line_number} is not a JSON object.")
            records.append(record)
    return records


def generate_bundle(
    config_path: Path,
    output_dir: Path,
    *,
    replace: bool = False,
    create_plot: bool = True,
) -> dict[str, Path]:
    """Generate raw records, a derived summary, a figure, and file checksums."""
    config = load_config(config_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "config": output_dir / "config.json",
        "records": output_dir / "pilot_records.jsonl",
        "summary": output_dir / "pilot_summary.json",
        "figure": output_dir / "pilot_convergence.svg",
        "manifest": output_dir / "manifest.json",
    }
    existing = [path for path in paths.values() if path.exists()]
    if existing and not replace:
        names = ", ".join(path.name for path in existing)
        raise FileExistsError(
            f"Refusing to modify an existing pilot bundle ({names}); use --replace."
        )
    if replace:
        for path in existing:
            path.unlink()

    _write_json(paths["config"], config)
    records = run_pilot(config)
    write_records(paths["records"], records)
    summary = summarize_records(read_records(paths["records"]), config)
    _write_json(paths["summary"], summary)
    if create_plot:
        plot_summary(summary, paths["figure"])

    archived_paths = [paths["config"], paths["records"], paths["summary"]]
    if create_plot:
        archived_paths.append(paths["figure"])
    manifest = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "run_id": summary["run_id"],
        "files": {
            path.name: {
                "bytes": path.stat().st_size,
                "sha256": _file_sha256(path),
            }
            for path in archived_paths
        },
    }
    _write_json(paths["manifest"], manifest)
    return {key: path for key, path in paths.items() if path.exists()}


def plot_summary(summary: Mapping[str, Any], output_path: Path) -> None:
    """Render the convergence figure exclusively from an aggregated summary."""
    try:
        import matplotlib
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover - depends on optional extra
        raise RuntimeError(
            'Plotting requires: python -m pip install -e ".[visualization]"'
        ) from exc

    matplotlib.rcParams["svg.hashsalt"] = str(summary["run_id"])
    colors = {
        "trotter_s1": "#306A91",
        "trotter_s2": "#AE1935",
        "qdrift": "#D9782D",
    }
    groups_by_method: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for group in summary["groups"]:
        groups_by_method[str(group["method"])].append(group)

    figure, axes = plt.subplots(1, 2, figsize=(13.2, 5.6), constrained_layout=True)
    figure.patch.set_facecolor("#F4F1E9")
    for axis in axes:
        axis.set_facecolor("#FFFDF8")
        axis.grid(True, which="both", color="#101D2D", alpha=0.12, linewidth=0.8)
        axis.tick_params(colors="#253548")
        for spine in axis.spines.values():
            spine.set_color("#9AA5AE")

    for method_name in ("trotter_s1", "trotter_s2", "qdrift"):
        groups = sorted(
            groups_by_method[method_name], key=lambda group: group["logical_budget"]
        )
        budgets = np.array([group["logical_budget"] for group in groups])
        operator_stats = [group["normalized_operator_error"] for group in groups]
        operator_means = np.array([stats["mean"] for stats in operator_stats])
        axes[0].loglog(
            budgets,
            operator_means,
            "o-",
            color=colors[method_name],
            linewidth=2.2,
            markersize=5,
            label=METHOD_LABELS[method_name],
        )
        if method_name == "qdrift":
            axes[0].fill_between(
                budgets,
                [stats["mean_ci95_low"] for stats in operator_stats],
                [stats["mean_ci95_high"] for stats in operator_stats],
                color=colors[method_name],
                alpha=0.2,
                linewidth=0,
                label="qDRIFT 95% bootstrap CI",
            )

        state_stats = [group["state_trace_distance"] for group in groups]
        state_means = np.array([stats["mean"] for stats in state_stats])
        axes[1].loglog(
            budgets,
            state_means,
            "o-",
            color=colors[method_name],
            linewidth=2.2,
            markersize=5,
            label=(
                f"{METHOD_LABELS[method_name]} trajectory mean"
                if method_name == "qdrift"
                else METHOD_LABELS[method_name]
            ),
        )
        if method_name == "qdrift":
            axes[1].fill_between(
                budgets,
                [stats["mean_ci95_low"] for stats in state_stats],
                [stats["mean_ci95_high"] for stats in state_stats],
                color=colors[method_name],
                alpha=0.2,
                linewidth=0,
            )
            axes[1].loglog(
                budgets,
                [group["empirical_ensemble_state_trace_distance"] for group in groups],
                "s--",
                color="#6E3B87",
                linewidth=2.0,
                markersize=4.5,
                label="qDRIFT empirical ensemble",
            )

    axes[0].set_title("Trajectory operator error", loc="left", fontweight="bold")
    axes[0].set_ylabel("Normalized spectral-norm error")
    axes[1].set_title("State error for |0⟩", loc="left", fontweight="bold")
    axes[1].set_ylabel("Trace distance")
    for axis in axes:
        axis.set_xlabel("Formula-level Pauli evolution operations")
        axis.legend(frameon=False, fontsize=8)

    figure.suptitle(
        "OpenQEvo pilot · H = X + Z · t = 1",
        x=0.02,
        ha="left",
        fontsize=17,
        fontweight="bold",
        color="#101D2D",
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(
        output_path,
        format="svg",
        facecolor=figure.get_facecolor(),
        metadata={
            "Title": "OpenQEvo X plus Z paper pilot",
            "Creator": "openqevo.benchmark",
            "Date": None,
        },
    )
    plt.close(figure)

    svg = output_path.read_text(encoding="utf-8")
    normalized = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    output_path.write_text(normalized, encoding="utf-8")


def _record(
    *,
    run_id: str,
    benchmark_id: str,
    config_hash: str,
    input_hash: str,
    environment: Mapping[str, str],
    method_name: str,
    method_source: str,
    logical_budget: int | None,
    parameters: Mapping[str, Any],
    sampled_sequence: Sequence[int] | None,
    formula_operations: int,
    merged_operations: int,
    unitary: NDArray[np.complexfloating],
    exact_unitary: NDArray[np.complexfloating],
    exact_state: NDArray[np.complexfloating],
) -> dict[str, Any]:
    state = unitary @ INITIAL_STATE
    metrics = _accuracy_metrics(unitary, state, exact_unitary, exact_state)
    return {
        "schema_version": RECORD_SCHEMA_VERSION,
        "run_id": run_id,
        "benchmark_id": benchmark_id,
        "config_sha256": config_hash,
        "input_sha256": input_hash,
        "status": "success",
        "method": method_name,
        "implementation": {
            "package": "openqevo",
            "version": _openqevo_version(),
            "source": method_source,
        },
        "environment": dict(environment),
        "logical_budget": logical_budget,
        "parameters": dict(parameters),
        "costs": {
            "formula_level_pauli_operations": formula_operations,
            "adjacent_merged_pauli_operations": merged_operations,
            "compiled_gate_counts": None,
        },
        "sampled_sequence": (
            list(sampled_sequence) if sampled_sequence is not None else None
        ),
        "metrics": metrics,
        "output_state": _encode_state(state),
        "output_sha256": _array_sha256(unitary),
        "failure": None,
    }


def _accuracy_metrics(
    unitary: NDArray[np.complexfloating],
    state: NDArray[np.complexfloating],
    exact_unitary: NDArray[np.complexfloating],
    exact_state: NDArray[np.complexfloating],
) -> dict[str, float]:
    denominator = float(np.linalg.norm(exact_unitary, ord=2))
    operator_error = float(np.linalg.norm(unitary - exact_unitary, ord=2) / denominator)
    fidelity = float(abs(np.vdot(exact_state, state)) ** 2)
    state_infidelity = float(np.clip(1.0 - fidelity, 0.0, 1.0))
    return {
        "normalized_operator_error": operator_error,
        "state_infidelity": state_infidelity,
        "state_trace_distance": float(np.sqrt(state_infidelity)),
    }


def _distribution_summary(
    values: Sequence[float],
    *,
    bootstrap_resamples: int,
    bootstrap_seed: int,
) -> dict[str, float | int]:
    array = np.asarray(values, dtype=float)
    if array.size == 0:
        raise ValueError("Cannot summarize an empty distribution.")
    mean = float(np.mean(array))
    if array.size == 1:
        low = high = mean
        standard_deviation = 0.0
    else:
        rng = np.random.default_rng(bootstrap_seed)
        indices = rng.integers(0, array.size, size=(bootstrap_resamples, array.size))
        means = np.mean(array[indices], axis=1)
        low, high = (float(value) for value in np.quantile(means, [0.025, 0.975]))
        standard_deviation = float(np.std(array, ddof=1))
    return {
        "count": int(array.size),
        "mean": mean,
        "standard_deviation": standard_deviation,
        "minimum": float(np.min(array)),
        "q25": float(np.quantile(array, 0.25)),
        "median": float(np.median(array)),
        "q75": float(np.quantile(array, 0.75)),
        "maximum": float(np.max(array)),
        "mean_ci95_low": low,
        "mean_ci95_high": high,
    }


def _density_trace_distance(
    state: NDArray[np.complexfloating],
    exact_state: NDArray[np.complexfloating],
) -> float:
    difference = state - exact_state
    eigenvalues = np.linalg.eigvalsh(difference)
    return float(0.5 * np.sum(np.abs(eigenvalues)))


def _encode_state(state: NDArray[np.complexfloating]) -> dict[str, list[float]]:
    return {
        "real": [float(value) for value in np.real(state)],
        "imag": [float(value) for value in np.imag(state)],
    }


def _decode_state(encoded: Mapping[str, Sequence[float]]) -> NDArray[np.complex128]:
    return np.asarray(encoded["real"], dtype=float) + 1j * np.asarray(
        encoded["imag"], dtype=float
    )


def _adjacent_merged_count(sequence: Sequence[int]) -> int:
    if not sequence:
        return 0
    return 1 + sum(left != right for left, right in zip(sequence, sequence[1:]))


def _environment() -> dict[str, str]:
    return {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "openqevo": _openqevo_version(),
    }


def _openqevo_version() -> str:
    try:
        return version("openqevo")
    except PackageNotFoundError:  # pragma: no cover - source import without install
        return "0.1.0+source"


def _is_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _canonical_json(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def _json_sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _array_sha256(value: NDArray[np.complexfloating]) -> str:
    array = np.ascontiguousarray(value, dtype="<c16")
    return hashlib.sha256(array.tobytes()).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main(argv: Sequence[str] | None = None) -> None:
    """Run the paper pilot and create its reproducibility bundle."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--replace",
        action="store_true",
        help="replace an existing bundle instead of refusing to modify it",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="skip the optional Matplotlib figure",
    )
    args = parser.parse_args(argv)

    try:
        paths = generate_bundle(
            args.config,
            args.output_dir,
            replace=args.replace,
            create_plot=not args.no_plot,
        )
    except FileExistsError as exc:
        parser.error(str(exc))

    print(f"Pilot bundle: {args.output_dir}")
    for name, path in paths.items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main()
