"""Adapter wrapping PennyLane's TrotterProduct.

Requires: pip install pennylane

Converts numpy Hamiltonian terms to PennyLane operators via
pauli_decompose, applies TrotterProduct, and extracts the
resulting unitary matrix.

This adapter is not loaded if pennylane is not installed.
"""

from __future__ import annotations

import operator
from typing import Any

import numpy as np
import pennylane as qml
from numpy.typing import NDArray

from openqevo.base import EvolutionMethod
from openqevo.hamiltonian import (
    HamiltonianInput,
    PauliHamiltonian,
    dense_terms,
    hamiltonian_provenance,
)
from openqevo.operations import trotter_operation_sequence
from openqevo.registry import register
from openqevo.result import (
    EvolutionCosts,
    EvolutionResult,
    implementation_provenance,
    installed_versions,
    runtime_environment,
)


@register("pennylane_trotter")
class PennyLaneTrotterAdapter(EvolutionMethod):
    """PennyLane-backed Trotter product decomposition."""

    description = "Trotter product via pennylane TrotterProduct"
    source = "pennylane"
    backend_packages = ("pennylane",)

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) using PennyLane's TrotterProduct.

        Parameters
        ----------
        terms : list of ndarray
            Hermitian matrices H_k where H = sum(terms).
        t : float
            Total evolution time.
        **params
            steps : int
                Number of Trotter repetitions (required).
            order : int
                Suzuki-Trotter order (default 2).
        """
        operation = self.build_operator(terms, t, **params)
        n_qubits = int(np.log2(dense_terms(terms)[0].shape[0]))
        return np.array(qml.matrix(operation, wire_order=range(n_qubits)))

    def build_operator(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> Any:
        """Return the PennyLane operation representing the requested formula."""
        steps = _step_count(params.pop("steps", None))
        order = _formula_order(params.pop("order", 2))
        if params:
            names = ", ".join(sorted(params))
            raise TypeError(f"Unexpected PennyLane adapter parameters: {names}.")
        matrix_terms = dense_terms(terms)
        n_qubits = int(np.log2(matrix_terms[0].shape[0]))
        pauli_ops = [
            qml.pauli_decompose(term, wire_order=range(n_qubits))
            for term in matrix_terms
        ]
        # PennyLane emits first-order operand decompositions in reverse list
        # order. Reverse its input only for order 1 so the temporal sequence
        # matches OpenQEvo/Qiskit listed-term semantics. Symmetric formulas are
        # palindromic and already match without this adjustment.
        ordered_ops = list(reversed(pauli_ops)) if order == 1 else pauli_ops
        hamiltonian = qml.sum(*ordered_ops) if len(ordered_ops) > 1 else ordered_ops[0]

        # PennyLane defines TrotterProduct for exp(+i H t); OpenQEvo's public
        # convention is exp(-i H t), hence the explicit negative time.
        if len(matrix_terms) == 1:
            return qml.exp(hamiltonian, coeff=-1j * float(t))
        return qml.TrotterProduct(
            hamiltonian,
            time=-float(t),
            order=order,
            n=steps,
        )

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        """Return a dense unitary or reusable PennyLane circuit operation."""
        representation = params.pop("representation", "unitary")
        if representation not in {"unitary", "circuit"}:
            raise ValueError("PennyLane output must be 'unitary' or 'circuit'.")
        steps = _step_count(params.pop("steps", None))
        order = _formula_order(params.pop("order", 2))
        if params:
            names = ", ".join(sorted(params))
            raise TypeError(f"Unexpected PennyLane adapter parameters: {names}.")

        operation = self.build_operator(terms, t, steps=steps, order=order)
        n_qubits = int(np.log2(dense_terms(terms)[0].shape[0]))
        output = (
            operation
            if representation == "circuit"
            else np.array(qml.matrix(operation, wire_order=range(n_qubits)))
        )
        term_count = len(dense_terms(terms))
        formula_operations, merged_operations = _formula_costs(
            term_count=term_count,
            steps=steps,
            order=order,
        )
        compiled_one = None
        compiled_two = None
        circuit_depth = None
        cost_model = "backend-unavailable-for-dense-input"
        if isinstance(terms, PauliHamiltonian) and order in {1, 2}:
            sequence = trotter_operation_sequence(
                terms,
                t,
                steps=steps,
                order=order,
            ).compact_adjacent()
            reference = sequence.compile_reference()
            compiled_one = reference.one_qubit_gates
            compiled_two = reference.two_qubit_gates
            circuit_depth = reference.depth
            cost_model = "openqevo-reference-h-s-sdg-rz-cx"

        return EvolutionResult(
            output=output,
            representation=str(representation),
            method_name=self.name,
            implementation=implementation_provenance(
                self.source,
                backend_versions=installed_versions(self.backend_packages),
            ),
            parameters={
                "evolution_time": float(t),
                "steps": steps,
                "order": order,
                "term_order": "input-order",
                "matrix_qubit_order": "q0-most-significant",
                "pennylane_time_sign": -1,
                "compiled_cost_model": cost_model,
            },
            costs=EvolutionCosts(
                formula_level_pauli_operations=formula_operations,
                adjacent_merged_pauli_operations=merged_operations,
                compiled_one_qubit_gates=compiled_one,
                compiled_two_qubit_gates=compiled_two,
                circuit_depth=circuit_depth,
            ),
            hamiltonian=hamiltonian_provenance(terms),
            environment=runtime_environment(),
            limitations=self._limitations(),
        )


def _step_count(value: Any) -> int:
    if value is None:
        raise TypeError("'steps' is a required parameter.")
    try:
        steps = operator.index(value)
    except TypeError as exc:
        raise TypeError("'steps' must be an integer.") from exc
    if steps < 1:
        raise ValueError("Number of steps must be at least 1.")
    return steps


def _formula_order(value: Any) -> int:
    try:
        order = operator.index(value)
    except TypeError as exc:
        raise TypeError("'order' must be an integer.") from exc
    if order != 1 and (order < 2 or order % 2):
        raise ValueError("'order' must be 1 or a positive even integer.")
    return order


def _formula_costs(*, term_count: int, steps: int, order: int) -> tuple[int, int]:
    if order == 1:
        formula = term_count * steps
        return formula, formula if term_count > 1 else 1
    if order == 2:
        formula = 2 * term_count * steps
        return formula, 2 * steps * (term_count - 1) + 1
    formula = 2 * (5 ** (order // 2 - 1)) * term_count * steps
    return formula, formula
