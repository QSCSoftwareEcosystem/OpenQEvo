"""Adapter wrapping Qiskit's Trotter-Suzuki synthesis.

Requires: pip install qiskit

Converts numpy Hamiltonian terms to SparsePauliOp, applies
PauliEvolutionGate with SuzukiTrotter synthesis, and extracts
the resulting unitary matrix.

This adapter is not loaded if qiskit is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import Operator, SparsePauliOp
from qiskit.synthesis import SuzukiTrotter

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("qiskit_trotter")
class QiskitTrotterAdapter(EvolutionMethod):
    """Qiskit-backed Trotter-Suzuki decomposition."""

    description = "Trotter-Suzuki via qiskit PauliEvolutionGate + SuzukiTrotter"
    source = "qiskit"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate exp(-i H t) using Qiskit's Trotter synthesis.

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

        # Convert each numpy matrix to SparsePauliOp and sum
        pauli_ops = [SparsePauliOp.from_operator(Operator(term)) for term in terms]
        hamiltonian = sum(pauli_ops[1:], pauli_ops[0])

        # Create evolution gate with Suzuki-Trotter synthesis
        synthesis = SuzukiTrotter(order=order, reps=steps)
        gate = PauliEvolutionGate(hamiltonian, time=t, synthesis=synthesis)

        # Build circuit, decompose to apply Trotter splitting, extract unitary
        n_qubits = int(np.log2(terms[0].shape[0]))
        qc = QuantumCircuit(n_qubits)
        qc.append(gate, range(n_qubits))

        # decompose() forces Qiskit to apply the Trotter decomposition
        # into individual Pauli rotation gates. Without this, Operator()
        # would compute the exact unitary of the PauliEvolutionGate directly.
        return Operator(qc.decompose()).data
