"""Randomized quantum evolution methods."""

from __future__ import annotations

import operator
from collections.abc import Sequence
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
)
from openqevo.registry import register
from openqevo.result import (
    EvolutionCosts,
    EvolutionResult,
    implementation_provenance,
    runtime_environment,
)


@register("qdrift")
class QDriftEvolution(EvolutionMethod):
    """qDRIFT-style randomized product formula."""

    description = "Randomized Hamiltonian evolution via qDRIFT sampling"
    source = "algorithms-thrust"

    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) with a sampled product formula."""
        matrix_terms, _, probabilities, sequence = _trajectory_inputs(terms, params)
        return _apply_trajectory(matrix_terms, probabilities, sequence, t)

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        """Return one qDRIFT trajectory with its complete sampled sequence."""
        samples = _sample_count(params)
        matrix_terms, weights, probabilities, sequence = _trajectory_inputs(
            terms, params
        )
        output = _apply_trajectory(matrix_terms, probabilities, sequence, t)
        seed = params.get("seed")
        metadata_parameters: dict[str, Any] = {
            "evolution_time": float(t),
            "samples": samples,
            "term_weights": [float(value) for value in weights],
            "sampling_probabilities": [float(value) for value in probabilities],
        }
        if seed is not None:
            metadata_parameters["seed"] = int(seed)
        if params.get("rng") is not None:
            metadata_parameters["rng"] = "external-generator"

        return EvolutionResult(
            output=output,
            representation="unitary",
            method_name=self.name,
            implementation=implementation_provenance(self.source),
            parameters=metadata_parameters,
            costs=EvolutionCosts(
                formula_level_pauli_operations=samples,
                adjacent_merged_pauli_operations=_adjacent_merged_count(sequence),
            ),
            hamiltonian=hamiltonian_provenance(terms),
            seed=seed,
            sampled_sequence=sequence,
            environment=runtime_environment(),
            limitations=self._limitations(),
        )

    def sample_sequence(
        self,
        terms: HamiltonianInput,
        *,
        samples: int,
        seed: int | None = None,
        term_weights: Any = None,
        rng: np.random.Generator | None = None,
    ) -> tuple[int, ...]:
        """Return the sampled term indices for a reproducible qDRIFT trajectory.

        The returned sequence can be archived and passed back to :meth:`evolve`
        through ``sampled_sequence``. Supplying an existing ``rng`` allows a
        caller to manage an ensemble stream explicitly; ``seed`` and ``rng``
        are mutually exclusive.
        """
        count = _sample_count({"samples": samples})
        matrix_terms = dense_terms(terms)
        weights = _term_weights(terms, matrix_terms, term_weights)
        probabilities = weights / np.sum(weights)
        return _draw_sequence(probabilities, count, seed=seed, rng=rng)

    def ensemble_channel(
        self,
        terms: HamiltonianInput,
        t: float,
        *,
        samples: int,
        term_weights: Any = None,
    ) -> NDArray[np.complexfloating]:
        """Return the exact expected qDRIFT channel in Liouville form.

        This dense validation mode averages the one-sample unitary channel and
        raises it to ``samples``. It is intended for analytic small-system
        controls, not scalable production execution.
        """
        count = _sample_count({"samples": samples})
        matrix_terms = dense_terms(terms)
        weights = _term_weights(terms, matrix_terms, term_weights)
        probabilities = weights / np.sum(weights)
        step_channel = np.zeros(
            (matrix_terms[0].size, matrix_terms[0].size), dtype=complex
        )
        dt = t / count
        for probability, term in zip(probabilities, matrix_terms):
            if probability <= 0:
                continue
            unitary = expm(-1j * term * (dt / probability))
            step_channel += probability * np.kron(unitary.conj(), unitary)
        return np.linalg.matrix_power(step_channel, count)

    def run_ensemble(
        self,
        terms: HamiltonianInput,
        t: float,
        *,
        samples: int,
        term_weights: Any = None,
    ) -> EvolutionResult:
        """Return the expected qDRIFT channel with structured provenance."""
        count = _sample_count({"samples": samples})
        matrix_terms = dense_terms(terms)
        weights = _term_weights(terms, matrix_terms, term_weights)
        probabilities = weights / np.sum(weights)
        output = self.ensemble_channel(
            terms, t, samples=count, term_weights=term_weights
        )
        return EvolutionResult(
            output=output,
            representation="channel",
            method_name=self.name,
            implementation=implementation_provenance(self.source),
            parameters={
                "evolution_time": float(t),
                "samples": count,
                "term_weights": [float(value) for value in weights],
                "sampling_probabilities": [float(value) for value in probabilities],
                "ensemble": "expected-channel",
            },
            costs=EvolutionCosts(formula_level_pauli_operations=count),
            hamiltonian=hamiltonian_provenance(terms),
            environment=runtime_environment(),
            limitations=(
                *self._limitations(),
                "Expected-channel construction is a dense validation mode.",
            ),
        )


def _sample_count(params: dict[str, Any]) -> int:
    samples = params.get("samples", params.get("steps"))
    if samples is None:
        raise TypeError("'samples' is a required parameter.")

    try:
        count = operator.index(samples)
    except TypeError as exc:
        raise TypeError("'samples' must be an integer.") from exc

    if count < 1:
        raise ValueError("Number of samples must be at least 1.")

    return count


def _term_weights(
    hamiltonian: HamiltonianInput,
    matrix_terms: tuple[NDArray[np.complex128], ...],
    weights: Any,
) -> NDArray[np.float64]:
    if isinstance(hamiltonian, PauliHamiltonian):
        canonical = np.array(
            [abs(term.coefficient) for term in hamiltonian.terms], dtype=float
        )
        if weights is not None:
            supplied = np.asarray(weights, dtype=float)
            if supplied.shape != canonical.shape or not np.allclose(
                supplied, canonical
            ):
                raise ValueError(
                    "'term_weights' cannot override canonical Pauli coefficients."
                )
        values = canonical
    elif weights is None:
        values = np.array(
            [np.linalg.norm(term, ord=2) for term in matrix_terms], dtype=float
        )
    else:
        values = np.asarray(weights, dtype=float)
        if values.shape != (len(matrix_terms),):
            raise ValueError("'term_weights' must match the number of terms.")

    if not np.all(np.isfinite(values)):
        raise ValueError("'term_weights' must be finite.")
    if np.any(values < 0):
        raise ValueError("'term_weights' must be non-negative.")
    if np.sum(values) <= 0:
        raise ValueError("At least one qDRIFT term weight must be positive.")

    return values


def _trajectory_inputs(
    terms: HamiltonianInput,
    params: dict[str, Any],
) -> tuple[
    tuple[NDArray[np.complex128], ...],
    NDArray[np.float64],
    NDArray[np.float64],
    tuple[int, ...],
]:
    samples = _sample_count(params)
    matrix_terms = dense_terms(terms)
    weights = _term_weights(terms, matrix_terms, params.get("term_weights"))
    probabilities = weights / np.sum(weights)
    sequence = params.get("sampled_sequence")
    if sequence is None:
        sequence = _draw_sequence(
            probabilities,
            samples,
            seed=params.get("seed"),
            rng=params.get("rng"),
        )
    else:
        sequence = _validate_sampled_sequence(
            sequence,
            samples=samples,
            probabilities=probabilities,
        )
        if params.get("rng") is not None:
            raise ValueError("'rng' cannot be combined with 'sampled_sequence'.")
        seed = params.get("seed")
        if seed is not None:
            seeded_sequence = _draw_sequence(
                probabilities,
                samples,
                seed=seed,
                rng=None,
            )
            if sequence != seeded_sequence:
                raise ValueError(
                    "'sampled_sequence' does not match the declared 'seed'."
                )
    return matrix_terms, weights, probabilities, sequence


def _apply_trajectory(
    terms: tuple[NDArray[np.complex128], ...],
    probabilities: NDArray[np.float64],
    sequence: tuple[int, ...],
    t: float,
) -> NDArray[np.complex128]:
    result = np.eye(terms[0].shape[0], dtype=complex)
    dt = t / len(sequence)
    for term_index in sequence:
        scaled_dt = dt / probabilities[term_index]
        result = expm(-1j * terms[term_index] * scaled_dt) @ result
    return result


def _adjacent_merged_count(sequence: Sequence[int]) -> int:
    if not sequence:
        return 0
    return 1 + sum(left != right for left, right in zip(sequence, sequence[1:]))


def _draw_sequence(
    probabilities: NDArray[np.float64],
    samples: int,
    *,
    seed: int | None,
    rng: np.random.Generator | None,
) -> tuple[int, ...]:
    if rng is not None and seed is not None:
        raise ValueError("'seed' and 'rng' are mutually exclusive.")
    if rng is not None and not isinstance(rng, np.random.Generator):
        raise TypeError("'rng' must be a numpy.random.Generator.")

    generator = rng if rng is not None else np.random.default_rng(seed)
    sampled = generator.choice(len(probabilities), size=samples, p=probabilities)
    return tuple(int(index) for index in sampled)


def _validate_sampled_sequence(
    sequence: Any,
    *,
    samples: int,
    probabilities: NDArray[np.float64],
) -> tuple[int, ...]:
    if isinstance(sequence, (str, bytes)) or not isinstance(sequence, Sequence):
        raise TypeError("'sampled_sequence' must be a sequence of term indices.")

    try:
        indices = tuple(operator.index(index) for index in sequence)
    except TypeError as exc:
        raise TypeError(
            "'sampled_sequence' must contain only integer term indices."
        ) from exc

    if len(indices) != samples:
        raise ValueError("'sampled_sequence' length must equal 'samples'.")
    if any(index < 0 or index >= len(probabilities) for index in indices):
        raise ValueError("'sampled_sequence' contains an out-of-range term index.")
    if any(probabilities[index] <= 0 for index in indices):
        raise ValueError("'sampled_sequence' selects a zero-probability term.")

    return indices
