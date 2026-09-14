"""Dense reference implementations for additional evolution strategies.

These methods deliberately target small systems.  They provide reproducible,
well-tested baselines and metadata for method selection, not hardware-ready
circuits or scalable production solvers.
"""

from __future__ import annotations

import math
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
from openqevo.registry import register
from openqevo.result import (
    EvolutionCosts,
    EvolutionResult,
    implementation_provenance,
    runtime_environment,
)


@register("krylov")
class KrylovEvolution(EvolutionMethod):
    """Lanczos-Krylov reference propagation for Hermitian Hamiltonians."""

    description = "Dense Lanczos-Krylov approximation of exp(-i H t)"
    source = "openqevo"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate a dense propagator by Krylov propagation of each column."""
        matrix_terms = dense_terms(terms)
        hamiltonian = np.sum(np.stack(matrix_terms), axis=0)
        dimension = hamiltonian.shape[0]
        time = _finite_time(t)
        krylov_dim = _krylov_dimension(params, dimension)
        tolerance = _tolerance(params)
        columns = [
            _lanczos_action(
                hamiltonian,
                np.eye(dimension, dtype=complex)[:, index],
                time,
                krylov_dim,
                tolerance,
            )
            for index in range(dimension)
        ]
        return np.column_stack(columns)

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        configured = dict(params)
        _require_unitary_representation(configured)
        dimension = dense_terms(terms)[0].shape[0]
        krylov_dim = _krylov_dimension(configured, dimension)
        tolerance = _tolerance(configured)
        output = self.evolve(terms, t, **configured)
        return _dense_reference_result(
            method=self,
            terms=terms,
            t=t,
            output=output,
            parameters={
                "krylov_dim": krylov_dim,
                "tolerance": tolerance,
                "propagator_construction": "independent_basis_state_actions",
            },
            warnings=(
                "The dense propagator is assembled from independent Lanczos "
                "actions; assess approximation error and unitarity for the "
                "chosen Krylov dimension.",
            ),
        )


@register("interaction_picture")
class InteractionPictureEvolution(EvolutionMethod):
    """Midpoint interaction-picture integrator for a selected Hamiltonian split."""

    description = "Midpoint interaction-picture evolution with a reference split"
    source = "openqevo"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Propagate ``H = H0 + V`` in the interaction picture of ``H0``."""
        steps = _step_count(params)
        reference, perturbation, _, _ = _interaction_partition(terms, params)
        time = _finite_time(t)
        dt = time / steps
        dimension = reference.shape[0]
        interaction_unitary = np.eye(dimension, dtype=complex)

        for step in range(steps):
            midpoint = (step + 0.5) * dt
            reference_frame = expm(1j * reference * midpoint)
            interaction_hamiltonian = (
                reference_frame @ perturbation @ reference_frame.conj().T
            )
            interaction_unitary = (
                expm(-1j * interaction_hamiltonian * dt) @ interaction_unitary
            )

        return expm(-1j * reference * time) @ interaction_unitary

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        configured = dict(params)
        _require_unitary_representation(configured)
        steps = _step_count(configured)
        _, _, reference_indices, perturbation_indices = _interaction_partition(
            terms, configured
        )
        labels = term_labels(terms)
        output = self.evolve(terms, t, **configured)
        return _dense_reference_result(
            method=self,
            terms=terms,
            t=t,
            output=output,
            parameters={
                "steps": steps,
                "reference_term_indices": list(reference_indices),
                "reference_term_labels": [labels[index] for index in reference_indices],
                "perturbation_term_indices": list(perturbation_indices),
            },
            warnings=(
                "This is a dense midpoint interaction-picture reference; "
                "it does not provide a hardware circuit or asymptotic resource "
                "estimate.",
            ),
        )


@register("annealing")
class AnnealingEvolution(EvolutionMethod):
    """Linear-schedule quantum-annealing reference evolution."""

    description = (
        "Dense linear-schedule annealing from a driver to a target Hamiltonian"
    )
    source = "openqevo"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Evolve under ``H(s) = (1-s) H_initial + s H_target``."""
        steps = _step_count(params)
        _require_linear_schedule(params)
        target = np.sum(np.stack(dense_terms(terms)), axis=0)
        initial, _ = _annealing_initial_hamiltonian(
            params.get("initial_hamiltonian"), target.shape[0]
        )
        time = _finite_time(t)
        dt = time / steps
        result = np.eye(target.shape[0], dtype=complex)

        for step in range(steps):
            progress = (step + 0.5) / steps
            instantaneous = (1.0 - progress) * initial + progress * target
            result = expm(-1j * instantaneous * dt) @ result
        return result

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        configured = dict(params)
        _require_unitary_representation(configured)
        steps = _step_count(configured)
        _require_linear_schedule(configured)
        target_dimension = dense_terms(terms)[0].shape[0]
        _, initial_provenance = _annealing_initial_hamiltonian(
            configured.get("initial_hamiltonian"), target_dimension
        )
        output = self.evolve(terms, t, **configured)
        return _dense_reference_result(
            method=self,
            terms=terms,
            t=t,
            output=output,
            parameters={
                "steps": steps,
                "schedule": "linear",
                "initial_hamiltonian": initial_provenance,
            },
            warnings=(
                "This method uses a first-order piecewise-constant midpoint "
                "discretization of a linear schedule; increase steps until the "
                "result is converged for the observable of interest.",
            ),
        )


def _dense_reference_result(
    *,
    method: EvolutionMethod,
    terms: HamiltonianInput,
    t: float,
    output: NDArray[np.complexfloating],
    parameters: dict[str, Any],
    warnings: tuple[str, ...],
) -> EvolutionResult:
    return EvolutionResult(
        output=output,
        representation="unitary",
        method_name=method.name,
        implementation=implementation_provenance(method.source),
        parameters={"evolution_time": _finite_time(t), **parameters},
        costs=EvolutionCosts(),
        hamiltonian=hamiltonian_provenance(terms),
        environment=runtime_environment(),
        warnings=warnings,
        limitations=method._limitations(),
    )


def _finite_time(value: float) -> float:
    time = float(value)
    if not math.isfinite(time):
        raise ValueError("Evolution time must be finite.")
    return time


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


def _krylov_dimension(params: dict[str, Any], dimension: int) -> int:
    requested = params.get("krylov_dim", min(12, dimension))
    try:
        count = operator.index(requested)
    except TypeError as exc:
        raise TypeError("'krylov_dim' must be an integer.") from exc
    if count < 1:
        raise ValueError("'krylov_dim' must be at least 1.")
    return min(count, dimension)


def _tolerance(params: dict[str, Any]) -> float:
    tolerance = float(params.get("tolerance", 1e-12))
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("'tolerance' must be positive and finite.")
    return tolerance


def _lanczos_action(
    hamiltonian: NDArray[np.complex128],
    state: NDArray[np.complex128],
    time: float,
    krylov_dim: int,
    tolerance: float,
) -> NDArray[np.complex128]:
    """Apply a Hermitian Lanczos approximation of the exponential to one state."""
    norm = float(np.linalg.norm(state))
    if norm <= tolerance:
        return np.zeros_like(state, dtype=complex)

    basis = np.zeros((hamiltonian.shape[0], krylov_dim), dtype=complex)
    diagonal: list[float] = []
    off_diagonal: list[float] = []
    previous = np.zeros_like(state, dtype=complex)
    current = np.asarray(state, dtype=complex) / norm

    for column in range(krylov_dim):
        basis[:, column] = current
        residual = hamiltonian @ current
        if column:
            residual -= off_diagonal[-1] * previous
        alpha = float(np.real(np.vdot(current, residual)))
        diagonal.append(alpha)
        residual -= alpha * current
        if column:
            prior_basis = basis[:, :column]
            residual -= prior_basis @ (prior_basis.conj().T @ residual)
        beta = float(np.linalg.norm(residual))
        if beta <= tolerance or column + 1 == krylov_dim:
            break
        off_diagonal.append(beta)
        previous = current
        current = residual / beta

    size = len(diagonal)
    projected = np.diag(np.asarray(diagonal, dtype=float)).astype(complex)
    for index, beta in enumerate(off_diagonal):
        projected[index, index + 1] = beta
        projected[index + 1, index] = beta
    coefficients = norm * expm(-1j * projected * time)[:, 0]
    return basis[:, :size] @ coefficients


def _interaction_partition(
    terms: HamiltonianInput,
    params: dict[str, Any],
) -> tuple[
    NDArray[np.complex128], NDArray[np.complex128], tuple[int, ...], tuple[int, ...]
]:
    matrix_terms = dense_terms(terms)
    indices = _reference_indices(terms, params, len(matrix_terms))
    reference = np.sum(np.stack([matrix_terms[index] for index in indices]), axis=0)
    perturbation_indices = tuple(
        index for index in range(len(matrix_terms)) if index not in indices
    )
    if perturbation_indices:
        perturbation = np.sum(
            np.stack([matrix_terms[index] for index in perturbation_indices]), axis=0
        )
    else:
        perturbation = np.zeros_like(reference)
    return reference, perturbation, indices, perturbation_indices


def _reference_indices(
    terms: HamiltonianInput,
    params: dict[str, Any],
    term_count: int,
) -> tuple[int, ...]:
    raw_indices = params.get("reference_term_indices")
    if raw_indices is None:
        if isinstance(terms, PauliHamiltonian):
            diagonal_indices = tuple(
                index
                for index, term in enumerate(terms.terms)
                if set(term.pauli_word) <= {"I", "Z"}
            )
            return diagonal_indices or (0,)
        return (0,)
    if isinstance(raw_indices, (str, bytes)):
        raise TypeError("'reference_term_indices' must be a sequence of integers.")
    try:
        indices = tuple(operator.index(index) for index in raw_indices)
    except TypeError as exc:
        raise TypeError(
            "'reference_term_indices' must be a sequence of integers."
        ) from exc
    if not indices:
        raise ValueError("'reference_term_indices' must not be empty.")
    if len(set(indices)) != len(indices):
        raise ValueError("'reference_term_indices' must not contain duplicates.")
    if any(index < 0 or index >= term_count for index in indices):
        raise ValueError("'reference_term_indices' contains an out-of-range index.")
    return indices


def _annealing_initial_hamiltonian(
    initial_hamiltonian: HamiltonianInput | None,
    target_dimension: int,
) -> tuple[NDArray[np.complex128], dict[str, Any]]:
    if initial_hamiltonian is None:
        qubits = int(round(math.log2(target_dimension)))
        return _transverse_field_driver(qubits), {
            "kind": "default_transverse_field_driver",
            "qubits": qubits,
            "coefficient": -1.0,
        }
    initial_terms = dense_terms(initial_hamiltonian)
    initial = np.sum(np.stack(initial_terms), axis=0)
    if initial.shape != (target_dimension, target_dimension):
        raise ValueError("'initial_hamiltonian' must have the target dimension.")
    return initial, hamiltonian_provenance(initial_hamiltonian)


def _transverse_field_driver(qubits: int) -> NDArray[np.complex128]:
    identity = np.eye(2, dtype=complex)
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    driver = np.zeros((2**qubits, 2**qubits), dtype=complex)
    for qubit in range(qubits):
        factors = [pauli_x if index == qubit else identity for index in range(qubits)]
        term = factors[0]
        for factor in factors[1:]:
            term = np.kron(term, factor)
        driver -= term
    return driver


def _require_unitary_representation(params: dict[str, Any]) -> None:
    representation = params.pop("representation", "unitary")
    if representation != "unitary":
        raise ValueError("This dense reference method supports only unitary output.")


def _require_linear_schedule(params: dict[str, Any]) -> None:
    schedule = params.get("schedule", "linear")
    if schedule != "linear":
        raise ValueError("Only the 'linear' annealing schedule is currently supported.")
