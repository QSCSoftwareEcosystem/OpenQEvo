"""Trotter-Suzuki product formulas for computing ``exp(-i H t)``.

The formulas are executable reference implementations with analytic controls,
operation-sequence output, and deterministic logical compilation.  Formal
Algorithms Thrust sign-off is tracked separately from software verification.
"""

from __future__ import annotations

import operator
from typing import Any

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

from openqevo.base import EvolutionMethod
from openqevo.hamiltonian import (
    HamiltonianInput,
    PauliHamiltonian,
    dense_terms,
    hamiltonian_provenance,
    term_labels,
)
from openqevo.operations import trotter_operation_sequence
from openqevo.registry import register
from openqevo.result import (
    EvolutionCosts,
    EvolutionResult,
    implementation_provenance,
    runtime_environment,
)


@register("trotter_s1")
class TrotterFirstOrder(EvolutionMethod):
    """First-order Trotter-Suzuki decomposition."""

    description = "First-order product formula: [prod_k exp(-i H_k dt)]^n"
    source = "algorithms-thrust"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) using first-order Trotter.

        Parameters
        ----------
        terms : list of ndarray
            Hermitian matrices H_k where H = sum(terms).
        t : float
            Total evolution time.
        **params
            steps : int
                Number of Trotter steps (required).
        """
        steps = _step_count(params)
        matrix_terms = dense_terms(terms)

        dt = t / steps
        dim = matrix_terms[0].shape[0]
        result = np.eye(dim, dtype=complex)

        step_unitary = np.eye(dim, dtype=complex)
        for h_k in matrix_terms:
            step_unitary = expm(-1j * h_k * dt) @ step_unitary

        for _ in range(steps):
            result = step_unitary @ result

        return result

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        representation = _result_representation(params)
        steps = _step_count(params)
        labels = term_labels(terms)
        operations = steps * len(labels)
        costs = EvolutionCosts(
            formula_level_pauli_operations=operations,
            adjacent_merged_pauli_operations=operations,
        )
        if isinstance(terms, PauliHamiltonian):
            raw_sequence = trotter_operation_sequence(terms, t, steps=steps, order=1)
            sequence = raw_sequence.compact_adjacent()
            circuit = sequence.compile_reference()
            costs = EvolutionCosts(
                formula_level_pauli_operations=len(raw_sequence.operations),
                adjacent_merged_pauli_operations=len(sequence.operations),
                compiled_one_qubit_gates=circuit.one_qubit_gates,
                compiled_two_qubit_gates=circuit.two_qubit_gates,
                circuit_depth=circuit.depth,
            )
            output = _select_output(
                representation=representation,
                unitary_factory=lambda: self.evolve(terms, t, steps=steps),
                sequence=sequence,
                circuit=circuit,
            )
        else:
            _require_dense_unitary_output(representation)
            output = self.evolve(terms, t, steps=steps)
        return _trotter_result(
            method=self,
            terms=terms,
            t=t,
            steps=steps,
            labels=labels,
            output=output,
            representation=representation,
            costs=costs,
        )


@register("trotter_s2")
class TrotterSecondOrder(EvolutionMethod):
    """Second-order (symmetric) Trotter-Suzuki decomposition."""

    description = (
        "Symmetric product formula: "
        "[prod_k exp(-i H_k dt/2) * prod_k(rev) exp(-i H_k dt/2)]^n"
    )
    source = "algorithms-thrust"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) using second-order Trotter.

        Parameters
        ----------
        terms : list of ndarray
            Hermitian matrices H_k where H = sum(terms).
        t : float
            Total evolution time.
        **params
            steps : int
                Number of Trotter steps (required).
        """
        steps = _step_count(params)
        matrix_terms = dense_terms(terms)

        dt = t / steps
        dim = matrix_terms[0].shape[0]
        result = np.eye(dim, dtype=complex)

        forward = np.eye(dim, dtype=complex)
        for h_k in matrix_terms:
            forward = expm(-1j * h_k * dt / 2) @ forward

        backward = np.eye(dim, dtype=complex)
        for h_k in reversed(matrix_terms):
            backward = expm(-1j * h_k * dt / 2) @ backward

        step_unitary = backward @ forward

        for _ in range(steps):
            result = step_unitary @ result

        return result

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        representation = _result_representation(params)
        steps = _step_count(params)
        labels = term_labels(terms)
        formula_operations = 2 * steps * len(labels)
        merged_operations = 2 * steps * (len(labels) - 1) + 1
        costs = EvolutionCosts(
            formula_level_pauli_operations=formula_operations,
            adjacent_merged_pauli_operations=merged_operations,
        )
        if isinstance(terms, PauliHamiltonian):
            raw_sequence = trotter_operation_sequence(terms, t, steps=steps, order=2)
            sequence = raw_sequence.compact_adjacent()
            circuit = sequence.compile_reference()
            costs = EvolutionCosts(
                formula_level_pauli_operations=len(raw_sequence.operations),
                adjacent_merged_pauli_operations=len(sequence.operations),
                compiled_one_qubit_gates=circuit.one_qubit_gates,
                compiled_two_qubit_gates=circuit.two_qubit_gates,
                circuit_depth=circuit.depth,
            )
            output = _select_output(
                representation=representation,
                unitary_factory=lambda: self.evolve(terms, t, steps=steps),
                sequence=sequence,
                circuit=circuit,
            )
        else:
            _require_dense_unitary_output(representation)
            output = self.evolve(terms, t, steps=steps)
        return _trotter_result(
            method=self,
            terms=terms,
            t=t,
            steps=steps,
            labels=labels,
            output=output,
            representation=representation,
            costs=costs,
        )


@register("exact")
class ExactEvolution(EvolutionMethod):
    """Exact time evolution via direct matrix exponentiation.

    Useful as a reference for benchmarking approximation methods.
    """

    description = "Exact exp(-i H t) via scipy.linalg.expm (reference only)"
    source = "openqevo"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        matrix_terms = dense_terms(terms)
        h_total = np.sum(np.stack(matrix_terms), axis=0)
        return expm(-1j * h_total * t)

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        representation = _result_representation(params)
        if representation != "unitary":
            raise ValueError("Exact evolution supports only unitary result output.")
        output = self.evolve(terms, t, **params)
        return EvolutionResult(
            output=output,
            representation="unitary",
            method_name=self.name,
            implementation=implementation_provenance(self.source),
            parameters={"evolution_time": float(t)},
            costs=EvolutionCosts(
                formula_level_pauli_operations=0,
                adjacent_merged_pauli_operations=0,
            ),
            hamiltonian=hamiltonian_provenance(terms),
            environment=runtime_environment(),
            limitations=self._limitations(),
        )


def _step_count(params: dict[str, Any]) -> int:
    steps = params.get("steps")
    if steps is None:
        raise TypeError("'steps' is a required parameter.")
    try:
        count = operator.index(steps)
    except TypeError as exc:
        raise TypeError("'steps' must be an integer.") from exc
    if count < 1:
        raise ValueError("Number of steps must be at least 1.")
    return count


def _trotter_result(
    *,
    method: EvolutionMethod,
    terms: HamiltonianInput,
    t: float,
    steps: int,
    labels: tuple[str, ...],
    output: Any,
    representation: str,
    costs: EvolutionCosts,
) -> EvolutionResult:
    return EvolutionResult(
        output=output,
        representation=representation,
        method_name=method.name,
        implementation=implementation_provenance(method.source),
        parameters={
            "evolution_time": float(t),
            "steps": steps,
            "term_order": list(labels),
        },
        costs=costs,
        hamiltonian=hamiltonian_provenance(terms),
        environment=runtime_environment(),
        limitations=method._limitations(),
    )


def _result_representation(params: dict[str, Any]) -> str:
    representation = params.pop("representation", "unitary")
    if representation not in {"unitary", "operations", "circuit"}:
        raise ValueError(
            "'representation' must be 'unitary', 'operations', or 'circuit'."
        )
    return str(representation)


def _select_output(
    *,
    representation: str,
    unitary_factory: Any,
    sequence: Any,
    circuit: Any,
) -> Any:
    if representation == "unitary":
        return unitary_factory()
    if representation == "operations":
        return sequence
    return circuit


def _require_dense_unitary_output(representation: str) -> None:
    if representation != "unitary":
        raise TypeError(
            "Scalable operation and circuit outputs require PauliHamiltonian input."
        )
