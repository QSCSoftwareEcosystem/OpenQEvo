"""Tests for the frozen publication study contract."""

import json
from pathlib import Path

import pytest

from openqevo.study import (
    PROTOCOL_SCHEMA_VERSION,
    build_workloads,
    estimate_resources,
    generate_bundle,
    load_protocol,
    run_study,
    summarize_records,
    validate_protocol,
    verify_bundle,
)

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def small_protocol():
    return {
        "schema_version": PROTOCOL_SCHEMA_VERSION,
        "protocol_id": "test-publication-study",
        "protocol_status": "software-frozen",
        "scientific_review_status": "pending",
        "evolution_time": 0.5,
        "logical_budget_multipliers": [1, 2],
        "qdrift_seeds": [11, 12, 13],
        "bootstrap_resamples": 50,
        "bootstrap_seed": 31,
        "target_mean_ci_half_width": 0.05,
        "target_expected_channel_error": 0.1,
        "confidence_z": 1.96,
        "tolerances": {"conformance_operator_norm": 1e-10},
        "workloads": [
            {
                "id": "controlled-test",
                "kind": "controlled",
                "parameters": {
                    "n_qubits": 2,
                    "term_count": 2,
                    "lambda_norm": 1.0,
                    "pauli_weight": 1,
                    "commutator_structure": "dense",
                    "coefficient_distribution": "uniform",
                    "seed": 7,
                },
            }
        ],
    }


def test_study_uses_equal_formula_level_budgets(small_protocol):
    records = run_study(small_protocol)

    assert len(records) == 11
    assert records[0]["method"] == "exact"
    for record in records[1:]:
        assert record["status"] == "success"
        assert (
            record["costs"]["formula_level_pauli_operations"]
            == record["logical_budget"]
        )
        assert record["costs"]["compiled_one_qubit_gates"] is not None
        assert record["costs"]["compiled_two_qubit_gates"] is not None
        assert record["costs"]["circuit_depth"] is not None


def test_summary_sizes_qdrift_ensembles_and_estimates_resources(small_protocol):
    workloads = build_workloads(small_protocol)
    estimate = estimate_resources(small_protocol, workloads)
    records = run_study(small_protocol)
    summary = summarize_records(records, small_protocol)
    qdrift = [group for group in summary["groups"] if group["method"] == "qdrift"]

    assert estimate["total_records"] == len(records)
    assert summary["failures"]["count"] == 0
    assert len(qdrift) == 2
    assert all(
        group["qdrift_ensemble_sizing"]["estimated_trajectories"] >= 1
        for group in qdrift
    )
    assert summary["workloads"][0]["qdrift_small_step_sample_estimate"]["samples"] >= 1


def test_bundle_is_write_once_and_byte_reproducible(tmp_path, small_protocol):
    protocol_path = tmp_path / "protocol.json"
    protocol_path.write_text(json.dumps(small_protocol), encoding="utf-8")
    first = generate_bundle(protocol_path, tmp_path / "first", create_plot=False)
    second = generate_bundle(protocol_path, tmp_path / "second", create_plot=False)

    for artifact in (
        "protocol",
        "workloads",
        "resources",
        "records",
        "summary",
        "manifest",
    ):
        assert first[artifact].read_bytes() == second[artifact].read_bytes()
    report = verify_bundle(tmp_path / "first")
    assert report["status"] == "passed"
    assert report["records"] == 11
    assert report["groups"] == 6
    assert report["equal_budget_violations"] == 0
    with pytest.raises(FileExistsError, match="new directory"):
        generate_bundle(protocol_path, tmp_path / "first", create_plot=False)


def test_bundle_verifier_detects_tampering(tmp_path, small_protocol):
    protocol_path = tmp_path / "protocol.json"
    protocol_path.write_text(json.dumps(small_protocol), encoding="utf-8")
    paths = generate_bundle(protocol_path, tmp_path / "bundle", create_plot=False)
    paths["records"].write_text("tampered\n", encoding="utf-8")

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        verify_bundle(tmp_path / "bundle")


def test_protocol_rejects_unfrozen_or_duplicate_seed(small_protocol):
    small_protocol["protocol_status"] = "draft"
    with pytest.raises(ValueError, match="software-frozen"):
        validate_protocol(small_protocol)
    small_protocol["protocol_status"] = "software-frozen"
    small_protocol["qdrift_seeds"] = [1, 1]
    with pytest.raises(ValueError, match="unique"):
        validate_protocol(small_protocol)


def test_archived_protocol_is_frozen_with_thirty_trajectories():
    protocol = load_protocol(
        ROOT / "experiments" / "publication_study" / "protocol.json"
    )

    assert protocol["protocol_status"] == "software-frozen"
    assert protocol["scientific_review_status"] == "pending"
    assert len(protocol["qdrift_seeds"]) >= 30
