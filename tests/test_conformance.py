"""Shared native/Qiskit/PennyLane convention and resource tests."""

import numpy as np
import pytest

import openqevo
from openqevo.conformance import (
    CONFORMANCE_CONVENTIONS,
    canonical_conformance_cases,
    evaluate_trotter_adapter,
    phase_aligned_operator_error,
)


def test_conformance_cases_cover_every_required_convention():
    purposes = " ".join(case.purpose for case in canonical_conformance_cases())

    assert "sign" in purposes
    assert "coefficient" in purposes
    assert "tensor-factor" in purposes
    assert "term order" in purposes
    assert {case.order for case in canonical_conformance_cases()} == {1, 2}
    assert CONFORMANCE_CONVENTIONS["target_unitary"] == "exp(-i * H * t)"


def test_phase_alignment_removes_only_global_phase():
    reference = np.diag([1.0, 1.0j])
    phased = np.exp(0.37j) * reference
    changed = np.diag([1.0, -1.0j])

    assert phase_aligned_operator_error(reference, phased) < 1e-14
    assert phase_aligned_operator_error(reference, changed) > 0.5


def test_qiskit_passes_shared_conformance_suite():
    pytest.importorskip("qiskit")
    result = evaluate_trotter_adapter("qiskit_trotter")

    assert result["status"] == "passed"
    assert len(result["cases"]) == 4
    assert all(case["passed"] for case in result["cases"])


def test_qiskit_circuit_output_reports_lowered_costs_and_wire_map():
    pytest.importorskip("qiskit")
    hamiltonian = canonical_conformance_cases()[2].hamiltonian
    result = openqevo.get("qiskit_trotter").run(
        hamiltonian,
        t=0.3,
        steps=2,
        order=2,
        representation="circuit",
    )

    assert result.representation == "circuit"
    assert result.costs.compiled_one_qubit_gates is not None
    assert result.costs.compiled_two_qubit_gates is not None
    assert result.costs.circuit_depth == result.output.depth()
    assert set(result.output.count_ops()) <= {"h", "s", "sdg", "rz", "cx"}
    assert result.parameters["backend_wire_map"] == {"0": 1, "1": 0}


def test_pennylane_passes_shared_conformance_suite_when_installed():
    pytest.importorskip("pennylane")
    result = evaluate_trotter_adapter("pennylane_trotter")

    assert result["status"] == "passed"
    assert all(case["passed"] for case in result["cases"])
