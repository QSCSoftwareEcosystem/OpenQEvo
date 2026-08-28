"""Randomized quantum evolution methods."""

from __future__ import annotations

import operator
from collections.abc import Sequence
from typing import Any

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("qdrift")
class QDriftEvolution(EvolutionMethod):
    """qDRIFT-style randomized product formula."""

    description = "Randomized Hamiltonian evolution via qDRIFT sampling"
    source = "algorithms-thrust"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) with a sampled product formula."""
        samples = _sample_count(params)

        dim = _validate_terms(terms)
        weights = _term_weights(terms, params.get("term_weights"))
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

        result = np.eye(dim, dtype=complex)
        dt = t / samples

        for term_index in sequence:
            scaled_dt = dt / probabilities[term_index]
            result = expm(-1j * terms[term_index] * scaled_dt) @ result

        return result

    def sample_sequence(
        self,
        terms: list[NDArray[np.complexfloating]],
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
        _validate_terms(terms)
        weights = _term_weights(terms, term_weights)
        probabilities = weights / np.sum(weights)
        return _draw_sequence(probabilities, count, seed=seed, rng=rng)


def _validate_terms(terms: list[NDArray[np.complexfloating]]) -> int:
    if not terms:
        raise ValueError("At least one Hamiltonian term is required.")

    dim = terms[0].shape[0]
    for term in terms:
        if term.ndim != 2 or term.shape != (dim, dim):
            raise ValueError("Hamiltonian terms must be square matrices of same shape.")
        if not np.allclose(term, term.conj().T):
            raise ValueError("Hamiltonian terms must be Hermitian.")

    return dim


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
    terms: list[NDArray[np.complexfloating]],
    weights: Any,
) -> NDArray[np.float64]:
    if weights is None:
        values = np.array([np.linalg.norm(term, ord=2) for term in terms], dtype=float)
    else:
        values = np.asarray(weights, dtype=float)
        if values.shape != (len(terms),):
            raise ValueError("'term_weights' must match the number of terms.")

    if not np.all(np.isfinite(values)):
        raise ValueError("'term_weights' must be finite.")
    if np.any(values < 0):
        raise ValueError("'term_weights' must be non-negative.")
    if np.sum(values) <= 0:
        raise ValueError("At least one qDRIFT term weight must be positive.")

    return values


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
