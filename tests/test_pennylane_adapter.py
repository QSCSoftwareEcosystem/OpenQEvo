"""Tests for the PennyLane Trotter adapter."""

import numpy as np
import pytest

pennylane = pytest.importorskip("pennylane")

import openqevo  # noqa: E402

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


class TestPennyLaneAdapter:
    def setup_method(self):
        self.method = openqevo.get("pennylane_trotter")

    def test_registered(self):
        assert "pennylane_trotter" in openqevo.list_methods()

    def test_single_term_is_exact(self):
        terms = [SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)
        approx = self.method.evolve(terms, t=1.0, steps=1)
        np.testing.assert_allclose(approx, exact, atol=1e-10)

    def test_converges_with_more_steps(self):
        terms = [SIGMA_X, SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)

        error_1 = np.linalg.norm(self.method.evolve(terms, t=1.0, steps=1) - exact)
        error_50 = np.linalg.norm(self.method.evolve(terms, t=1.0, steps=50) - exact)
        assert error_50 < error_1

    def test_result_is_unitary(self):
        terms = [SIGMA_X, SIGMA_Y, SIGMA_Z]
        result = self.method.evolve(terms, t=0.5, steps=10)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-10)

    def test_order_parameter(self):
        terms = [SIGMA_X, SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)
        steps = 2

        error_order1 = np.linalg.norm(
            self.method.evolve(terms, t=1.0, steps=steps, order=1) - exact
        )
        error_order2 = np.linalg.norm(
            self.method.evolve(terms, t=1.0, steps=steps, order=2) - exact
        )
        assert error_order2 < error_order1

    def test_two_qubit_hamiltonian(self):
        xi = np.kron(SIGMA_X, np.eye(2))
        zz = np.kron(SIGMA_Z, SIGMA_Z)
        terms = [xi, zz]

        result = self.method.evolve(terms, t=0.5, steps=20)
        assert result.shape == (4, 4)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(4), atol=1e-10)

    def test_empty_terms_raises(self):
        with pytest.raises(ValueError, match="At least one"):
            self.method.evolve([], t=1.0, steps=1)

    def test_missing_steps_raises(self):
        with pytest.raises(TypeError, match="steps"):
            self.method.evolve([SIGMA_Z], t=1.0)

    def test_zero_steps_raises(self):
        with pytest.raises(ValueError, match="at least 1"):
            self.method.evolve([SIGMA_Z], t=1.0, steps=0)
