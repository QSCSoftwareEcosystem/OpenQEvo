"""Adapter wrapping Qrack's GPU-accelerated quantum simulation.

Requires: pip install pyqrack

NOT YET IMPLEMENTED. Qrack operates at the gate level rather than the
Hamiltonian level, so this adapter requires manual Pauli decomposition
and Trotter circuit construction using QrackSimulator gate operations.
This will be implemented in a future release.

This adapter is not loaded if pyqrack is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray
from pyqrack import QrackSimulator  # noqa: F401

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
        raise NotImplementedError(
            "Qrack adapter requires gate-level circuit construction "
            "(Pauli decomposition + Trotter gate sequence). "
            "Planned for a future release."
        )
