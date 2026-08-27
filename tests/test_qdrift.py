"""Tests for qDRIFT randomized evolution."""

import numpy as np
import pytest

import openqevo

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


class TestQDrift:
    def setup_method(self):
        self.method = openqevo.get("qdrift")

    def test_registered(self):
        assert "qdrift" in openqevo.list_methods()
        assert self.method.source == "algorithms-thrust"

    def test_single_term_is_exact(self):
        result = self.method.evolve([SIGMA_Z], t=0.5, samples=4, seed=123)
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_seed_reproducible(self):
        terms = [SIGMA_X, SIGMA_Z]

        first = self.method.evolve(terms, t=0.5, samples=8, seed=7)
        second = self.method.evolve(terms, t=0.5, samples=8, seed=7)

        np.testing.assert_allclose(first, second, atol=1e-12)

    def test_result_is_unitary(self):
        result = self.method.evolve([SIGMA_X, SIGMA_Z], t=0.5, samples=8, seed=3)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-12)

    def test_steps_alias_for_samples(self):
        result = self.method.evolve([SIGMA_Z], t=0.5, steps=4, seed=123)
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_term_weights_control_sampling(self):
        result = self.method.evolve(
            [SIGMA_X, SIGMA_Z],
            t=0.5,
            samples=4,
            seed=123,
            term_weights=[0.0, 1.0],
        )
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_invalid_inputs_raise(self):
        with pytest.raises(TypeError, match="samples"):
            self.method.evolve([SIGMA_Z], t=0.5)

        with pytest.raises(ValueError, match="at least 1"):
            self.method.evolve([SIGMA_Z], t=0.5, samples=0)

        with pytest.raises(TypeError, match="integer"):
            self.method.evolve([SIGMA_Z], t=0.5, samples=1.5)

        with pytest.raises(ValueError, match="term_weights"):
            self.method.evolve([SIGMA_Z], t=0.5, samples=1, term_weights=[1.0, 2.0])

        with pytest.raises(ValueError, match="non-negative"):
            self.method.evolve([SIGMA_Z], t=0.5, samples=1, term_weights=[-1.0])
