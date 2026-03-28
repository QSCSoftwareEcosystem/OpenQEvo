"""Adapter wrapping PennyLane's TrotterProduct.

Requires: pip install pennylane

This adapter is not loaded if pennylane is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

import pennylane as qml

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("pennylane_trotter")
class PennyLaneTrotterAdapter(EvolutionMethod):
    """PennyLane-backed Trotter product decomposition."""

    description = "Trotter product via qml.TrotterProduct"
    source = "pennylane"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        # TODO: Implement when PennyLane integration is ready.
        # This stub defines the interface; the actual implementation
        # will map terms to qml.Hamiltonian and use qml.TrotterProduct.
        raise NotImplementedError(
            "PennyLane adapter is a stub. Contributions welcome — see issue #3."
        )
