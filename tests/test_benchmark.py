"""Tests for the configuration-driven paper pilot."""

import json
from pathlib import Path

import pytest

from openqevo.benchmark import (
    CONFIG_SCHEMA_VERSION,
    generate_bundle,
    load_config,
    read_records,
    run_pilot,
    summarize_records,
    validate_config,
)

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def small_config():
    return {
        "schema_version": CONFIG_SCHEMA_VERSION,
        "benchmark_id": "test-xz-pilot",
        "evolution_time": 1.0,
        "logical_budgets": [4, 8],
        "qdrift_seeds": [11, 12, 13],
        "bootstrap_resamples": 50,
        "bootstrap_seed": 99,
    }


def test_equal_budget_records_and_qdrift_provenance(small_config):
    records = run_pilot(small_config)

    assert len(records) == 11
    assert records[0]["method"] == "exact"
    for record in records[1:]:
        assert (
            record["costs"]["formula_level_pauli_operations"]
            == record["logical_budget"]
        )
        assert record["status"] == "success"
        if record["method"] == "qdrift":
            assert len(record["sampled_sequence"]) == record["logical_budget"]
            assert record["parameters"]["seed"] in small_config["qdrift_seeds"]


def test_pilot_is_numerically_reproducible(small_config):
    assert run_pilot(small_config) == run_pilot(small_config)


def test_summary_distinguishes_trajectories_from_ensemble(small_config):
    records = run_pilot(small_config)
    summary = summarize_records(records, small_config)
    qdrift_groups = [
        group for group in summary["groups"] if group["method"] == "qdrift"
    ]

    assert len(qdrift_groups) == 2
    assert all(group["trajectories"] == 3 for group in qdrift_groups)
    assert all(
        group["normalized_operator_error"]["count"] == 3 for group in qdrift_groups
    )
    assert all(
        group["empirical_ensemble_state_trace_distance"] >= 0 for group in qdrift_groups
    )


def test_bundle_is_immutable_without_explicit_replace(tmp_path, small_config):
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(small_config), encoding="utf-8")
    output_dir = tmp_path / "bundle"

    paths = generate_bundle(config_path, output_dir, create_plot=False)
    records = read_records(paths["records"])

    assert len(records) == 11
    assert paths["manifest"].exists()
    with pytest.raises(FileExistsError, match="--replace"):
        generate_bundle(config_path, output_dir, create_plot=False)


def test_config_rejects_unfair_budget(small_config):
    small_config["logical_budgets"] = [6]

    with pytest.raises(ValueError, match="multiple of 4"):
        validate_config(small_config)


def test_archived_pilot_uses_at_least_thirty_fixed_seeds():
    config = load_config(ROOT / "experiments" / "xz_pilot" / "config.json")

    assert len(config["qdrift_seeds"]) >= 30
    assert len(config["qdrift_seeds"]) == len(set(config["qdrift_seeds"]))
