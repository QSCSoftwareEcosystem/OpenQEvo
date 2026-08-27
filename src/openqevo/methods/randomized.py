"""Randomized quantum evolution methods."""

from __future__ import annotations

import operator
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

        rng = np.random.default_rng(params.get("seed"))
        result = np.eye(dim, dtype=complex)
        dt = t / samples

        for term_index in rng.choice(len(terms), size=samples, p=probabilities):
            scaled_dt = dt / probabilities[term_index]
            result = expm(-1j * terms[term_index] * scaled_dt) @ result

        return result


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
