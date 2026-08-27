"""Adapter wrapping Qrack's quantum simulation.

Requires: pip install pyqrack

Converts dense numpy Hamiltonian terms to Pauli-string coefficients,
applies Trotterized Pauli exponentials with QrackSimulator, and extracts
the resulting unitary matrix by evolving each computational basis vector.

This adapter is not loaded if pyqrack is not installed.
"""

from __future__ import annotations

import ctypes
from typing import Any

import numpy as np
from numpy.typing import NDArray
from pyqrack import QrackSimulator
from pyqrack.pauli import Pauli

from openqevo.base import EvolutionMethod
from openqevo.registry import register

_PAULI_MATRICES: dict[str, NDArray[np.complexfloating]] = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}

_QRACK_PAULI = {
    "I": int(Pauli.PauliI),
    "X": int(Pauli.PauliX),
    "Y": int(Pauli.PauliY),
    "Z": int(Pauli.PauliZ),
}


def _validate_terms(
    terms: list[NDArray[np.complexfloating]],
) -> tuple[int, int]:
    if not terms:
        raise ValueError("At least one Hamiltonian term is required.")

    dim = terms[0].shape[0]
    if terms[0].ndim != 2 or terms[0].shape != (dim, dim):
        raise ValueError("Hamiltonian terms must be square matrices.")

    n_qubits = int(np.log2(dim))
    if 2**n_qubits != dim:
        raise ValueError("Hamiltonian dimension must be a power of 2.")

    for term in terms:
        if term.ndim != 2 or term.shape != (dim, dim):
            raise ValueError("All Hamiltonian terms must have the same square shape.")
        if not np.allclose(term, term.conj().T):
            raise ValueError("Hamiltonian terms must be Hermitian.")

    return dim, n_qubits


def _pauli_matrix(labels_by_qubit: tuple[str, ...]) -> NDArray[np.complexfloating]:
    matrix = np.array([[1]], dtype=complex)
    for label in reversed(labels_by_qubit):
        matrix = np.kron(matrix, _PAULI_MATRICES[label])
    return matrix


def _pauli_decompose(
    term: NDArray[np.complexfloating],
    n_qubits: int,
    *,
    atol: float,
) -> list[tuple[tuple[str, ...], float]]:
    dim = term.shape[0]
    components: list[tuple[tuple[str, ...], float]] = []

    def visit(prefix: tuple[str, ...]) -> None:
        if len(prefix) == n_qubits:
            pauli = _pauli_matrix(prefix)
            coeff = np.trace(pauli.conj().T @ term) / dim
            if abs(coeff) > atol:
                if abs(coeff.imag) > atol:
                    raise ValueError(
                        "Hamiltonian term has a non-real Pauli coefficient; "
                        "Qrack adapter expects Hermitian terms."
                    )
                components.append((prefix, float(coeff.real)))
            return

        for label in ("I", "X", "Y", "Z"):
            visit((*prefix, label))

    visit(())
    return components


def _basis_vector(index: int, dim: int) -> list[complex]:
    state = np.zeros(dim, dtype=complex)
    state[index] = 1.0
    return state.tolist()


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
        """Approximate exp(-i H t) using Qrack Pauli exponentials.

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
                Suzuki-Trotter order. Supported values are 1 and 2.
            is_gpu : bool
                Passed to QrackSimulator. Defaults to False so CPU-only
                environments can exercise the adapter.
        """
        steps = params.get("steps")
        if steps is None:
            raise TypeError("'steps' is a required parameter.")
        if steps < 1:
            raise ValueError("Number of steps must be at least 1.")

        order = params.get("order", 2)
        if order not in (1, 2):
            raise ValueError("Qrack adapter currently supports order 1 or 2.")

        atol = params.get("atol", 1e-12)
        dim, n_qubits = _validate_terms(terms)
        decomposed = [
            _pauli_decompose(np.asarray(term, dtype=complex), n_qubits, atol=atol)
            for term in terms
        ]

        dt = t / steps
        unitary = np.empty((dim, dim), dtype=complex)

        for basis_index in range(dim):
            sim = QrackSimulator(
                qubit_count=n_qubits,
                is_gpu=params.get("is_gpu", False),
            )
            sim.in_ket(_basis_vector(basis_index, dim))
            phase = 1.0 + 0.0j

            for _ in range(steps):
                if order == 1:
                    phase *= self._apply_terms(sim, decomposed, dt)
                else:
                    phase *= self._apply_terms(sim, decomposed, dt / 2)
                    phase *= self._apply_terms(sim, reversed(decomposed), dt / 2)

            unitary[:, basis_index] = phase * np.asarray(sim.out_ket(), dtype=complex)

        return unitary

    @staticmethod
    def _apply_terms(
        sim: QrackSimulator,
        decomposed_terms: Any,
        dt: float,
    ) -> complex:
        phase = 1.0 + 0.0j
        for components in decomposed_terms:
            for labels, coeff in components:
                active = [
                    (qubit, label) for qubit, label in enumerate(labels) if label != "I"
                ]
                angle = -coeff * dt
                if not active:
                    phase *= np.exp(1j * angle)
                    continue

                _apply_qrack_pauli_exp(sim, active, angle)

        return phase


def _apply_qrack_pauli_exp(
    sim: QrackSimulator,
    active: list[tuple[int, str]],
    angle: float,
) -> None:
    qubits = [qubit for qubit, _ in active]
    bases = [_QRACK_PAULI[label] for _, label in active]

    if not hasattr(sim, "sid"):
        sim.exp(bases, angle, qubits)
        return

    if len(active) == 1:
        _apply_qrack_native_exp(sim, bases, angle, qubits)
        return

    _change_to_z_basis(sim, active)

    target = qubits[-1]
    controls = qubits[:-1]
    for control in controls:
        sim.mcx([control], target)

    _apply_qrack_native_exp(sim, [_QRACK_PAULI["Z"]], angle, [target])

    for control in reversed(controls):
        sim.mcx([control], target)

    _restore_from_z_basis(sim, reversed(active))


def _apply_qrack_native_exp(
    sim: QrackSimulator,
    bases: list[int],
    angle: float,
    qubits: list[int],
) -> None:
    from pyqrack.qrack_system import Qrack

    basis_array = (ctypes.c_int * len(bases))(*bases)
    qubit_array = (ctypes.c_ulonglong * len(qubits))(*qubits)
    Qrack.qrack_lib.Exp(
        sim.sid,
        len(bases),
        basis_array,
        ctypes.c_double(angle),
        qubit_array,
    )
    sim._throw_if_error()


def _change_to_z_basis(
    sim: QrackSimulator,
    active: list[tuple[int, str]],
) -> None:
    for qubit, label in active:
        if label == "X":
            sim.h(qubit)
        elif label == "Y":
            sim.adjs(qubit)
            sim.h(qubit)


def _restore_from_z_basis(
    sim: QrackSimulator,
    active: Any,
) -> None:
    for qubit, label in active:
        if label == "X":
            sim.h(qubit)
        elif label == "Y":
            sim.h(qubit)
            sim.s(qubit)
