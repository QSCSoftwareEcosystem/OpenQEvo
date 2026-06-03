"""Tests for the Qrack Trotter adapter using a small fake pyqrack module."""

from __future__ import annotations

import importlib
import sys
import types

import numpy as np
import pytest
from scipy.linalg import expm

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI_BY_ID = {
    0: np.eye(2, dtype=complex),
    1: SIGMA_X,
    2: SIGMA_Z,
    3: SIGMA_Y,
}


class FakePauli:
    PauliI = 0
    PauliX = 1
    PauliZ = 2
    PauliY = 3


class FakeQrackSimulator:
    def __init__(self, qubit_count, is_gpu=False):
        self.qubit_count = qubit_count
        self.is_gpu = is_gpu
        self.state = np.zeros(2**qubit_count, dtype=complex)
        self.state[0] = 1.0

    def in_ket(self, state):
        self.state = np.asarray(state, dtype=complex)

    def out_ket(self):
        return self.state.tolist()

    def exp(self, bases, angle, qubits):
        labels = [FakePauli.PauliI] * self.qubit_count
        for basis, qubit in zip(bases, qubits):
            labels[qubit] = basis

        pauli = np.array([[1]], dtype=complex)
        for label in reversed(labels):
            pauli = np.kron(pauli, PAULI_BY_ID[label])

        operator = np.cos(angle) * np.eye(2**self.qubit_count) + (
            1j * np.sin(angle) * pauli
        )
        self.state = operator @ self.state


@pytest.fixture
def qrack_module(monkeypatch):
    pyqrack = types.ModuleType("pyqrack")
    pyqrack.QrackSimulator = FakeQrackSimulator

    pauli = types.ModuleType("pyqrack.pauli")
    pauli.Pauli = FakePauli

    monkeypatch.setitem(sys.modules, "pyqrack", pyqrack)
    monkeypatch.setitem(sys.modules, "pyqrack.pauli", pauli)
    sys.modules.pop("openqevo.adapters.qrack_adapter", None)

    return importlib.import_module("openqevo.adapters.qrack_adapter")


class TestQrackAdapter:
    def test_single_term_is_exact(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        result = method.evolve([SIGMA_Z], t=1.0, steps=1)
        expected = np.array(
            [[np.exp(-1j), 0], [0, np.exp(1j)]],
            dtype=complex,
        )
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_converges_with_more_steps(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        exact = expm(-1j * (SIGMA_X + SIGMA_Z) * 1.0)

        error_1 = np.linalg.norm(
            method.evolve([SIGMA_X, SIGMA_Z], t=1.0, steps=1, order=1) - exact
        )
        error_20 = np.linalg.norm(
            method.evolve([SIGMA_X, SIGMA_Z], t=1.0, steps=20, order=1) - exact
        )
        assert error_20 < error_1

    def test_second_order_is_more_accurate(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        exact = expm(-1j * (SIGMA_X + SIGMA_Z) * 1.0)

        error_order1 = np.linalg.norm(
            method.evolve([SIGMA_X, SIGMA_Z], t=1.0, steps=2, order=1) - exact
        )
        error_order2 = np.linalg.norm(
            method.evolve([SIGMA_X, SIGMA_Z], t=1.0, steps=2, order=2) - exact
        )
        assert error_order2 < error_order1

    def test_two_qubit_hamiltonian(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        xi = np.kron(SIGMA_X, np.eye(2))
        zz = np.kron(SIGMA_Z, SIGMA_Z)

        result = method.evolve([xi, zz], t=0.5, steps=20)

        assert result.shape == (4, 4)
        np.testing.assert_allclose(
            result @ result.conj().T,
            np.eye(4),
            atol=1e-12,
        )

    def test_empty_terms_raises(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        with pytest.raises(ValueError, match="At least one"):
            method.evolve([], t=1.0, steps=1)

    def test_missing_steps_raises(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        with pytest.raises(TypeError, match="steps"):
            method.evolve([SIGMA_Z], t=1.0)

    def test_unsupported_order_raises(self, qrack_module):
        method = qrack_module.QrackTrotterAdapter()
        with pytest.raises(ValueError, match="order 1 or 2"):
            method.evolve([SIGMA_Z], t=1.0, steps=1, order=4)
