"""Tests for the Qiskit Trotter-Suzuki adapter."""

import numpy as np
import pytest

qiskit = pytest.importorskip("qiskit")

import openqevo  # noqa: E402

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


class TestQiskitAdapter:
    def setup_method(self):
        self.method = openqevo.get("qiskit_trotter")

    def test_registered(self):
        assert "qiskit_trotter" in openqevo.list_methods()

    def test_single_term_is_exact(self):
        terms = [SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)
        approx = self.method.evolve(terms, t=1.0, steps=1)
        np.testing.assert_allclose(approx, exact, atol=1e-10)

    def test_converges_with_more_steps(self):
        """Use 2-qubit non-commuting terms to see Trotter error."""
        # XI and ZZ do not commute
        xi = np.kron(SIGMA_X, np.eye(2))
        zz = np.kron(SIGMA_Z, SIGMA_Z)
        terms = [xi, zz]
        exact = openqevo.get("exact").evolve(terms, t=2.0)

        error_1 = np.linalg.norm(
            self.method.evolve(terms, t=2.0, steps=1, order=1) - exact
        )
        error_20 = np.linalg.norm(
            self.method.evolve(terms, t=2.0, steps=20, order=1) - exact
        )
        assert error_20 < error_1

    def test_result_is_unitary(self):
        terms = [SIGMA_X, SIGMA_Y, SIGMA_Z]
        result = self.method.evolve(terms, t=0.5, steps=10)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-10)

    def test_order_parameter(self):
        """Higher order should give better accuracy at same step count."""
        xi = np.kron(SIGMA_X, np.eye(2))
        zz = np.kron(SIGMA_Z, SIGMA_Z)
        terms = [xi, zz]
        exact = openqevo.get("exact").evolve(terms, t=2.0)
        steps = 2

        error_order1 = np.linalg.norm(
            self.method.evolve(terms, t=2.0, steps=steps, order=1) - exact
        )
        error_order2 = np.linalg.norm(
            self.method.evolve(terms, t=2.0, steps=steps, order=2) - exact
        )
        assert error_order2 < error_order1

    def test_two_qubit_hamiltonian(self):
        """Test with a 4x4 Hamiltonian (2-qubit system)."""
        # XX interaction
        xx = np.kron(SIGMA_X, SIGMA_X)
        # ZZ interaction
        zz = np.kron(SIGMA_Z, SIGMA_Z)
        terms = [xx, zz]

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
