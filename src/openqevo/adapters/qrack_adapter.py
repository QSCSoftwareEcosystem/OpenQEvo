"""Adapter wrapping Qrack's GPU-accelerated quantum simulation.

Requires: pip install pyqrack

Qrack is a Unitary Foundation project providing GPU-accelerated circuit
simulation. This adapter maps Hamiltonian terms to Trotter circuits and
executes them on Qrack's simulator to compute exp(-iHt).

This adapter is not loaded if pyqrack is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

from pyqrack import QrackSimulator

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("qrack_trotter")
class QrackTrotterAdapter(EvolutionMethod):
    """Qrack-backed GPU-accelerated Trotter-Suzuki decomposition."""

    description = "GPU-accelerated Trotter-Suzuki via Qrack (Unitary Foundation)"
    source = "qrack"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        # TODO: Implement when Qrack integration is ready.
        # This stub defines the interface; the actual implementation
        # will map terms to Trotter gate sequences and execute on
        # QrackSimulator with GPU acceleration.
        raise NotImplementedError(
            "Qrack adapter is a stub. Contributions welcome — see issue #3."
        )
