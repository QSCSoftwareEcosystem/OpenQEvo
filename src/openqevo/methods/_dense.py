"""Shared dense-matrix helpers for native reference methods."""

from __future__ import annotations

import operator
from typing import Any

import numpy as np
from numpy.typing import NDArray


def validate_terms(
    terms: list[NDArray[np.complexfloating]],
    label: str = "Hamiltonian terms",
) -> int:
    """Validate a non-empty list of same-shape Hermitian dense matrices."""
    if not terms:
        raise ValueError(f"{label} must contain at least one term.")

    for term in terms:
        if term.ndim != 2:
            raise ValueError(f"{label} must be square matrices of same shape.")

    dim = terms[0].shape[0]
    for term in terms:
        if term.shape != (dim, dim):
            raise ValueError(f"{label} must be square matrices of same shape.")
        if not np.all(np.isfinite(term)):
            raise ValueError(f"{label} must contain only finite values.")
        if not np.allclose(term, term.conj().T):
            raise ValueError(f"{label} must be Hermitian.")

    return dim


def validate_compatible_terms(
    terms: list[NDArray[np.complexfloating]],
    dim: int,
    label: str,
) -> None:
    """Validate Hermitian dense matrices against an expected dimension."""
    if not terms:
        raise ValueError(f"{label} must contain at least one term.")

    for term in terms:
        if term.ndim != 2 or term.shape != (dim, dim):
            raise ValueError(f"{label} must be square matrices of same shape.")
        if not np.all(np.isfinite(term)):
            raise ValueError(f"{label} must contain only finite values.")
        if not np.allclose(term, term.conj().T):
            raise ValueError(f"{label} must be Hermitian.")


def integer_param(params: dict[str, Any], name: str) -> int:
    """Read a required integer parameter with a minimum value of 1."""
    value = params.get(name)
    if value is None:
        raise TypeError(f"'{name}' is a required parameter.")

    try:
        count = operator.index(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(f"'{name}' must be an integer.") from exc

    if count < 1:
        raise ValueError(f"'{name}' must be at least 1.")

    return count


def finite_time(value: float) -> float:
    """Return a finite real evolution time."""
    try:
        time = float(value)
    except (TypeError, ValueError) as exc:
        raise TypeError("Evolution time must be a finite real number.") from exc

    if not np.isfinite(time):
        raise ValueError("Evolution time must be finite.")

    return time


def sum_terms(terms: list[NDArray[np.complexfloating]]) -> NDArray[np.complexfloating]:
    """Sum dense Hamiltonian terms without relying on Python's scalar zero."""
    total = np.zeros_like(terms[0], dtype=complex)
    for term in terms:
        total = total + term
    return total
