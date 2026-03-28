"""Trotter-Suzuki product formulas for computing exp(-iHt).

PLACEHOLDER IMPLEMENTATION — This module contains a reference implementation
of first- and second-order Trotter-Suzuki decompositions used to validate
the package structure, tests, and CI/CD pipeline. It will be replaced by
the production implementation from the QSC Algorithms Thrust.

See: https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("trotter_s1")
class TrotterFirstOrder(EvolutionMethod):
    """First-order Trotter-Suzuki decomposition."""

    description = "First-order product formula: [prod_k exp(-i H_k dt)]^n"
    source = "algorithms-thrust"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
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
        steps = params.get("steps")
        if steps is None:
            raise TypeError("'steps' is a required parameter.")
        if not terms:
            raise ValueError("At least one Hamiltonian term is required.")
        if steps < 1:
            raise ValueError("Number of steps must be at least 1.")

        dt = t / steps
        dim = terms[0].shape[0]
        result = np.eye(dim, dtype=complex)

        step_unitary = np.eye(dim, dtype=complex)
        for h_k in terms:
            step_unitary = expm(-1j * h_k * dt) @ step_unitary

        for _ in range(steps):
            result = step_unitary @ result

        return result


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
        terms: list[NDArray[np.complexfloating]],
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
        steps = params.get("steps")
        if steps is None:
            raise TypeError("'steps' is a required parameter.")
        if not terms:
            raise ValueError("At least one Hamiltonian term is required.")
        if steps < 1:
            raise ValueError("Number of steps must be at least 1.")

        dt = t / steps
        dim = terms[0].shape[0]
        result = np.eye(dim, dtype=complex)

        forward = np.eye(dim, dtype=complex)
        for h_k in terms:
            forward = expm(-1j * h_k * dt / 2) @ forward

        backward = np.eye(dim, dtype=complex)
        for h_k in reversed(terms):
            backward = expm(-1j * h_k * dt / 2) @ backward

        step_unitary = backward @ forward

        for _ in range(steps):
            result = step_unitary @ result

        return result


@register("exact")
class ExactEvolution(EvolutionMethod):
    """Exact time evolution via direct matrix exponentiation.

    Useful as a reference for benchmarking approximation methods.
    """

    description = "Exact exp(-i H t) via scipy.linalg.expm (reference only)"
    source = "openqevo"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        if not terms:
            raise ValueError("At least one Hamiltonian term is required.")

        h_total = sum(terms)
        return expm(-1j * h_total * t)
