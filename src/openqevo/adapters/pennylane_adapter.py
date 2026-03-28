"""Adapter wrapping PennyLane's TrotterProduct.

Requires: pip install pennylane

Converts numpy Hamiltonian terms to PennyLane operators via
pauli_decompose, applies TrotterProduct, and extracts the
resulting unitary matrix.

This adapter is not loaded if pennylane is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pennylane as qml
from numpy.typing import NDArray

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("pennylane_trotter")
class PennyLaneTrotterAdapter(EvolutionMethod):
    """PennyLane-backed Trotter product decomposition."""

    description = "Trotter product via pennylane TrotterProduct"
    source = "pennylane"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) using PennyLane's TrotterProduct.

        Parameters
        ----------
        terms : list of ndarray
            Hermitian matrices H_k where H = sum(terms).
        t : float
            Total evolution time.
        **params
            steps : int
                Number of Trotter repetitions (required).
            order : int
                Suzuki-Trotter order (default 2).
        """
        steps = params.get("steps")
        if steps is None:
            raise TypeError("'steps' is a required parameter.")
        if not terms:
            raise ValueError("At least one Hamiltonian term is required.")
        if steps < 1:
            raise ValueError("Number of steps must be at least 1.")

        order = params.get("order", 2)
        n_qubits = int(np.log2(terms[0].shape[0]))

        # Decompose each numpy matrix into PennyLane Pauli operators and sum
        pauli_ops = [
            qml.pauli_decompose(term, wire_order=range(n_qubits)) for term in terms
        ]
        hamiltonian = qml.sum(*pauli_ops) if len(pauli_ops) > 1 else pauli_ops[0]

        # PennyLane computes exp(+iHt), so negate time to get exp(-iHt).
        # TrotterProduct requires >= 2 Hamiltonian terms; for a single
        # term, use qml.exp which is exact.
        if len(terms) == 1:
            op = qml.exp(hamiltonian, coeff=-1j * t)
            return np.array(qml.matrix(op))

        trotter_op = qml.TrotterProduct(hamiltonian, time=-t, order=order, n=steps)
        return np.array(qml.matrix(trotter_op))
