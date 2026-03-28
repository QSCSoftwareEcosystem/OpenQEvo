"""Tests for Trotter-Suzuki decompositions via the registry."""

import numpy as np
import pytest

import openqevo

# Pauli matrices
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


class TestRegistry:
    def test_methods_registered(self):
        methods = openqevo.list_methods()
        assert "trotter_s1" in methods
        assert "trotter_s2" in methods
        assert "exact" in methods

    def test_list_methods_detail(self):
        details = openqevo.list_methods_detail()
        names = [d["name"] for d in details]
        assert "trotter_s1" in names
        sources = {d["name"]: d["source"] for d in details}
        assert sources["trotter_s1"] == "algorithms-thrust"
        assert sources["exact"] == "openqevo"

    def test_unknown_method_raises(self):
        with pytest.raises(KeyError, match="Unknown method"):
            openqevo.get("nonexistent")


class TestFirstOrder:
    def setup_method(self):
        self.method = openqevo.get("trotter_s1")

    def test_single_term_is_exact(self):
        terms = [SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)
        approx = self.method.evolve(terms, t=1.0, steps=1)
        np.testing.assert_allclose(approx, exact, atol=1e-12)

    def test_converges_with_more_steps(self):
        terms = [SIGMA_X, SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)

        error_10 = np.linalg.norm(
            self.method.evolve(terms, t=1.0, steps=10) - exact
        )
        error_100 = np.linalg.norm(
            self.method.evolve(terms, t=1.0, steps=100) - exact
        )
        assert error_100 < error_10

    def test_result_is_unitary(self):
        terms = [SIGMA_X, SIGMA_Y, SIGMA_Z]
        result = self.method.evolve(terms, t=0.5, steps=10)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-12)

    def test_empty_terms_raises(self):
        with pytest.raises(ValueError, match="At least one"):
            self.method.evolve([], t=1.0, steps=1)

    def test_missing_steps_raises(self):
        with pytest.raises(TypeError, match="steps"):
            self.method.evolve([SIGMA_Z], t=1.0)

    def test_zero_steps_raises(self):
        with pytest.raises(ValueError, match="at least 1"):
            self.method.evolve([SIGMA_Z], t=1.0, steps=0)


class TestSecondOrder:
    def setup_method(self):
        self.method = openqevo.get("trotter_s2")

    def test_single_term_is_exact(self):
        terms = [SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)
        approx = self.method.evolve(terms, t=1.0, steps=1)
        np.testing.assert_allclose(approx, exact, atol=1e-12)

    def test_more_accurate_than_first_order(self):
        terms = [SIGMA_X, SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=1.0)
        steps = 10

        s1 = openqevo.get("trotter_s1")
        error_s1 = np.linalg.norm(s1.evolve(terms, t=1.0, steps=steps) - exact)
        error_s2 = np.linalg.norm(
            self.method.evolve(terms, t=1.0, steps=steps) - exact
        )
        assert error_s2 < error_s1

    def test_result_is_unitary(self):
        terms = [SIGMA_X, SIGMA_Y, SIGMA_Z]
        result = self.method.evolve(terms, t=0.5, steps=10)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-12)


class TestExactEvolution:
    def setup_method(self):
        self.method = openqevo.get("exact")

    def test_known_result(self):
        t = np.pi / 4
        result = self.method.evolve([SIGMA_Z], t)
        expected = np.array(
            [[np.exp(-1j * t), 0], [0, np.exp(1j * t)]], dtype=complex
        )
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_identity_at_zero_time(self):
        result = self.method.evolve([SIGMA_X, SIGMA_Z], t=0.0)
        np.testing.assert_allclose(result, np.eye(2), atol=1e-12)
