"""Adapter wrapping Qiskit's Trotter-Suzuki synthesis.

Requires: pip install qiskit

Converts numpy Hamiltonian terms to SparsePauliOp, applies
PauliEvolutionGate with SuzukiTrotter synthesis, and extracts
the resulting unitary matrix.

This adapter is not loaded if qiskit is not installed.
"""

from __future__ import annotations

import operator
from typing import Any

import numpy as np
from numpy.typing import NDArray
from qiskit import transpile
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import Operator, SparsePauliOp
from qiskit.synthesis import LieTrotter, SuzukiTrotter

from openqevo.base import EvolutionMethod
from openqevo.hamiltonian import HamiltonianInput, PauliHamiltonian, dense_terms
from openqevo.registry import register
from openqevo.result import (
    EvolutionCosts,
    EvolutionResult,
    implementation_provenance,
    installed_versions,
    runtime_environment,
)

DEFAULT_BASIS_GATES = ("h", "s", "sdg", "rz", "cx")


@register("qiskit_trotter")
class QiskitTrotterAdapter(EvolutionMethod):
    """Qiskit-backed Trotter-Suzuki decomposition."""

    description = "Trotter-Suzuki via qiskit PauliEvolutionGate + SuzukiTrotter"
    source = "qiskit"
    backend_packages = ("qiskit",)

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) using Qiskit's Trotter synthesis.

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
        circuit = self.build_circuit(terms, t, **params)
        return Operator(circuit).data

    def build_circuit(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> QuantumCircuit:
        """Return the synthesized product-formula circuit before basis lowering."""
        steps = _step_count(params.pop("steps", None))
        order = _formula_order(params.pop("order", 2))
        if params:
            names = ", ".join(sorted(params))
            raise TypeError(f"Unexpected Qiskit adapter parameters: {names}.")
        matrix_terms = dense_terms(terms)

        # Converting each input term independently preserves the canonical term
        # order.  For canonical input, Qiskit's wire n-1-q represents OpenQEvo
        # qubit q so that both libraries expose the same q0-most-significant
        # output matrix convention.
        pauli_ops = [
            SparsePauliOp.from_operator(Operator(term)) for term in matrix_terms
        ]
        hamiltonian = sum(pauli_ops[1:], pauli_ops[0])
        synthesis = (
            LieTrotter(reps=steps)
            if order == 1
            else SuzukiTrotter(order=order, reps=steps)
        )
        gate = PauliEvolutionGate(hamiltonian, time=float(t), synthesis=synthesis)
        n_qubits = int(np.log2(matrix_terms[0].shape[0]))
        circuit = QuantumCircuit(n_qubits)
        circuit.append(gate, range(n_qubits))

        # Force synthesis here. Operator(PauliEvolutionGate) would otherwise
        # materialize the exact exponential instead of the requested formula.
        return circuit.decompose()

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        """Return a dense unitary or compiled Qiskit circuit with resources."""
        representation = params.pop("representation", "unitary")
        if representation not in {"unitary", "circuit"}:
            raise ValueError("Qiskit output must be 'unitary' or 'circuit'.")
        steps = _step_count(params.pop("steps", None))
        order = _formula_order(params.pop("order", 2))
        basis_gates = tuple(params.pop("basis_gates", DEFAULT_BASIS_GATES))
        optimization_level = params.pop("optimization_level", 0)
        if params:
            names = ", ".join(sorted(params))
            raise TypeError(f"Unexpected Qiskit adapter parameters: {names}.")
        if not basis_gates or any(not isinstance(name, str) for name in basis_gates):
            raise TypeError("'basis_gates' must be a non-empty sequence of names.")
        if optimization_level not in {0, 1, 2, 3}:
            raise ValueError("'optimization_level' must be 0, 1, 2, or 3.")

        circuit = self.build_circuit(terms, t, steps=steps, order=order)
        compiled = transpile(
            circuit,
            basis_gates=list(basis_gates),
            optimization_level=optimization_level,
        )
        one_qubit, two_qubit = _gate_counts(compiled)
        term_count = len(dense_terms(terms))
        formula_operations, merged_operations = _formula_costs(
            term_count=term_count,
            steps=steps,
            order=order,
        )
        output = compiled if representation == "circuit" else Operator(circuit).data
        n_qubits = int(np.log2(dense_terms(terms)[0].shape[0]))
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
                "backend_wire_map": {
                    str(qubit): n_qubits - 1 - qubit for qubit in range(n_qubits)
                },
                "compiled_basis_gates": list(basis_gates),
                "optimization_level": optimization_level,
            },
            costs=EvolutionCosts(
                formula_level_pauli_operations=formula_operations,
                adjacent_merged_pauli_operations=merged_operations,
                compiled_one_qubit_gates=one_qubit,
                compiled_two_qubit_gates=two_qubit,
                circuit_depth=int(compiled.depth()),
            ),
            hamiltonian=(
                {
                    "representation": "pauli_sum",
                    "id": terms.identifier,
                    "sha256": terms.sha256,
                    "qubits": terms.n_qubits,
                    "terms": len(terms.terms),
                    "lambda": terms.lambda_norm,
                    "qubit_order": list(terms.qubit_order),
                }
                if isinstance(terms, PauliHamiltonian)
                else self._dense_provenance(terms)
            ),
            environment=runtime_environment(),
            limitations=self._limitations(),
        )

    @staticmethod
    def _dense_provenance(terms: HamiltonianInput) -> dict[str, Any]:
        from openqevo.hamiltonian import hamiltonian_provenance

        return hamiltonian_provenance(terms)


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


def _gate_counts(circuit: QuantumCircuit) -> tuple[int, int]:
    one_qubit = 0
    two_qubit = 0
    for instruction in circuit.data:
        size = instruction.operation.num_qubits
        if size == 1:
            one_qubit += 1
        elif size == 2:
            two_qubit += 1
    return one_qubit, two_qubit


def _formula_costs(*, term_count: int, steps: int, order: int) -> tuple[int, int]:
    if order == 1:
        formula = term_count * steps
        merged = formula if term_count > 1 else 1
        return formula, merged
    if order == 2:
        formula = 2 * term_count * steps
        return formula, 2 * steps * (term_count - 1) + 1
    formula = 2 * (5 ** (order // 2 - 1)) * term_count * steps
    # Cross-block simplification for higher orders is backend-dependent; keep
    # the unsimplified formula count and rely on compiled fields for realization.
    return formula, formula
