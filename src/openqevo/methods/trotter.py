"""Trotter-Suzuki product formulas for computing exp(-iHt).

PLACEHOLDER IMPLEMENTATION — This module contains a reference implementation
of first- and second-order Trotter-Suzuki decompositions used to validate
the package structure, tests, and CI/CD pipeline. It will be replaced by
the production implementation from the QSC Algorithms Thrust.

See: https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4
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
    dense_terms,
    hamiltonian_provenance,
    term_labels,
)
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
        steps = _step_count(params)
        labels = term_labels(terms)
        output = self.evolve(terms, t, steps=steps)
        operations = steps * len(labels)
        return _trotter_result(
            method=self,
            terms=terms,
            t=t,
            steps=steps,
            labels=labels,
            output=output,
            costs=EvolutionCosts(
                formula_level_pauli_operations=operations,
                adjacent_merged_pauli_operations=operations,
            ),
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
        steps = _step_count(params)
        labels = term_labels(terms)
        output = self.evolve(terms, t, steps=steps)
        formula_operations = 2 * steps * len(labels)
        merged_operations = 2 * steps * (len(labels) - 1) + 1
        return _trotter_result(
            method=self,
            terms=terms,
            t=t,
            steps=steps,
            labels=labels,
            output=output,
            costs=EvolutionCosts(
                formula_level_pauli_operations=formula_operations,
                adjacent_merged_pauli_operations=merged_operations,
            ),
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
    output: NDArray[np.complexfloating],
    costs: EvolutionCosts,
) -> EvolutionResult:
    return EvolutionResult(
        output=output,
        representation="unitary",
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
