"""Executable cross-framework conformance cases for product formulas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from openqevo.hamiltonian import PauliHamiltonian, PauliTerm
from openqevo.registry import get, list_methods

CONFORMANCE_SCHEMA_VERSION = "openqevo-conformance/v1"
CONFORMANCE_CONVENTIONS = {
    "target_unitary": "exp(-i * H * t)",
    "pauli_rotation": "R_P(theta) = exp(-i * theta * P / 2)",
    "matrix_basis_order": "q0-most-significant",
    "pauli_word": "pauli_word[index] acts on qubit_order[index]",
    "term_order": "listed Hamiltonian order",
    "qiskit_wire_map": "backend_wire = n_qubits - 1 - openqevo_qubit",
    "pennylane_time_map": "pennylane_time = -openqevo_time",
}


@dataclass(frozen=True, slots=True)
class ConformanceCase:
    """One convention-sensitive product-formula comparison."""

    identifier: str
    hamiltonian: PauliHamiltonian
    evolution_time: float
    steps: int
    order: int
    purpose: str
    tolerance: float = 5e-10

    @property
    def reference_method(self) -> str:
        return "trotter_s1" if self.order == 1 else "trotter_s2"


def canonical_conformance_cases() -> tuple[ConformanceCase, ...]:
    """Return the shared sign, ordering, coefficient, and formula cases."""
    asymmetric = PauliHamiltonian(
        identifier="conformance-asymmetric-two-qubit",
        source="openqevo-conformance/v1",
        terms=(
            PauliTerm(0.7, "XI", source="openqevo-conformance/v1"),
            PauliTerm(-0.4, "ZZ", source="openqevo-conformance/v1"),
            PauliTerm(0.2, "IY", source="openqevo-conformance/v1"),
        ),
        mapping_metadata={"matrix_basis_order": "q0-most-significant"},
    )
    return (
        ConformanceCase(
            identifier="negative-coefficient-sign",
            hamiltonian=PauliHamiltonian(
                identifier="conformance-negative-z",
                source="openqevo-conformance/v1",
                terms=(PauliTerm(-0.75, "Z"),),
            ),
            evolution_time=0.4,
            steps=3,
            order=1,
            purpose="evolution sign, coefficient sign, and factor-of-two rotation",
        ),
        ConformanceCase(
            identifier="explicit-qubit-order",
            hamiltonian=PauliHamiltonian(
                identifier="conformance-reordered-x",
                source="openqevo-conformance/v1",
                terms=(PauliTerm(0.6, "XI", qubit_order=(1, 0)),),
            ),
            evolution_time=0.3,
            steps=2,
            order=2,
            purpose="explicit tensor-factor and backend-wire ordering",
        ),
        ConformanceCase(
            identifier="ordered-first-order-noncommuting",
            hamiltonian=asymmetric,
            evolution_time=0.7,
            steps=3,
            order=1,
            purpose="listed term order with asymmetric noncommuting coefficients",
        ),
        ConformanceCase(
            identifier="ordered-second-order-noncommuting",
            hamiltonian=asymmetric,
            evolution_time=0.7,
            steps=3,
            order=2,
            purpose="symmetric second-order schedule and term order",
        ),
    )


def phase_aligned_operator_error(
    reference: np.ndarray[Any, Any],
    candidate: np.ndarray[Any, Any],
) -> float:
    """Return normalized spectral error after removing one global phase."""
    reference_array = np.asarray(reference, dtype=complex)
    candidate_array = np.asarray(candidate, dtype=complex)
    if reference_array.shape != candidate_array.shape:
        return float("inf")
    overlap = np.vdot(reference_array.reshape(-1), candidate_array.reshape(-1))
    if abs(overlap) > 0:
        candidate_array = candidate_array * np.conj(overlap / abs(overlap))
    denominator = max(float(np.linalg.norm(reference_array, ord=2)), 1.0)
    return float(np.linalg.norm(candidate_array - reference_array, ord=2) / denominator)


def evaluate_trotter_adapter(
    method_name: str,
    *,
    cases: tuple[ConformanceCase, ...] | None = None,
) -> dict[str, Any]:
    """Evaluate one registered adapter against native formula references."""
    available = set(list_methods())
    if method_name not in available:
        return {
            "schema_version": CONFORMANCE_SCHEMA_VERSION,
            "adapter": method_name,
            "status": "unavailable",
            "conventions": dict(CONFORMANCE_CONVENTIONS),
            "cases": [],
        }

    records = []
    for case in cases or canonical_conformance_cases():
        reference = get(case.reference_method).evolve(
            case.hamiltonian,
            t=case.evolution_time,
            steps=case.steps,
        )
        candidate = get(method_name).evolve(
            case.hamiltonian,
            t=case.evolution_time,
            steps=case.steps,
            order=case.order,
        )
        phase_aligned_error = phase_aligned_operator_error(reference, candidate)
        raw_error = float(
            np.linalg.norm(np.asarray(candidate) - np.asarray(reference), ord=2)
            / max(float(np.linalg.norm(reference, ord=2)), 1.0)
        )
        records.append(
            {
                "case": case.identifier,
                "purpose": case.purpose,
                "hamiltonian_sha256": case.hamiltonian.sha256,
                "order": case.order,
                "steps": case.steps,
                "evolution_time": case.evolution_time,
                "raw_normalized_operator_error": raw_error,
                "phase_aligned_normalized_operator_error": phase_aligned_error,
                "tolerance": case.tolerance,
                "passed": phase_aligned_error <= case.tolerance,
            }
        )
    return {
        "schema_version": CONFORMANCE_SCHEMA_VERSION,
        "adapter": method_name,
        "status": "passed" if all(item["passed"] for item in records) else "failed",
        "conventions": dict(CONFORMANCE_CONVENTIONS),
        "cases": records,
    }


def run_conformance_suite(
    adapters: tuple[str, ...] = ("qiskit_trotter", "pennylane_trotter"),
) -> dict[str, Any]:
    """Run every requested adapter and return a serializable suite record."""
    results = [evaluate_trotter_adapter(adapter) for adapter in adapters]
    available = [result for result in results if result["status"] != "unavailable"]
    status = (
        "passed"
        if available and all(r["status"] == "passed" for r in available)
        else "failed"
    )
    if not available:
        status = "unavailable"
    return {
        "schema_version": CONFORMANCE_SCHEMA_VERSION,
        "status": status,
        "conventions": dict(CONFORMANCE_CONVENTIONS),
        "adapters": results,
    }
