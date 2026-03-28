"""Adapter wrapping Qiskit's Trotter-Suzuki synthesis.

Requires: pip install qiskit

This adapter is not loaded if qiskit is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("qiskit_trotter")
class QiskitTrotterAdapter(EvolutionMethod):
    """Qiskit-backed Trotter-Suzuki decomposition."""

    description = "Trotter-Suzuki via qiskit.synthesis.SuzukiTrotter"
    source = "qiskit"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        # TODO: Implement when Qiskit integration is ready.
        # This stub defines the interface; the actual implementation
        # will map terms to SparsePauliOp and use SuzukiTrotter.
        raise NotImplementedError(
            "Qiskit adapter is a stub. Contributions welcome — see issue #3."
        )
