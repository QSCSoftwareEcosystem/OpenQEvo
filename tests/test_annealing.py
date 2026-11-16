"""Tests for dense adiabatic/annealing evolution."""

import numpy as np
import pytest

import openqevo

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


class TestAdiabaticEvolution:
    def setup_method(self):
        self.method = openqevo.get("adiabatic_evolution")

    def test_registered(self):
        assert "adiabatic_evolution" in openqevo.list_methods()
        assert self.method.source == "algorithms-thrust"

    def test_identical_initial_and_final_matches_exact(self):
        result = self.method.evolve(
            [SIGMA_Z],
            t=0.5,
            initial_terms=[SIGMA_Z],
            steps=4,
        )
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_zero_time_returns_identity(self):
        result = self.method.evolve(
            [SIGMA_Z],
            t=0.0,
            initial_terms=[SIGMA_X],
            steps=4,
        )
        np.testing.assert_allclose(result, np.eye(2), atol=1e-12)

    def test_commuting_linear_path_matches_integrated_exact(self):
        result = self.method.evolve(
            [2.0 * SIGMA_Z],
            t=0.5,
            initial_terms=[SIGMA_Z],
            steps=4,
        )
        exact = openqevo.get("exact").evolve([1.5 * SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_converges_with_more_steps(self):
        final_terms = [SIGMA_Z]
        initial_terms = [SIGMA_X]
        reference = self.method.evolve(
            final_terms,
            t=1.0,
            initial_terms=initial_terms,
            steps=400,
        )

        error_5 = np.linalg.norm(
            self.method.evolve(
                final_terms,
                t=1.0,
                initial_terms=initial_terms,
                steps=5,
            )
            - reference
        )
        error_50 = np.linalg.norm(
            self.method.evolve(
                final_terms,
                t=1.0,
                initial_terms=initial_terms,
                steps=50,
            )
            - reference
        )
        assert error_50 < error_5

    def test_power_schedule(self):
        result = self.method.evolve(
            [SIGMA_Z],
            t=0.5,
            initial_terms=[SIGMA_Z],
            steps=4,
            schedule={"type": "power", "power": 2.0},
        )
        assert result.shape == (2, 2)

    def test_result_is_unitary(self):
        result = self.method.evolve(
            [SIGMA_Z],
            t=0.5,
            initial_terms=[SIGMA_X, SIGMA_Y],
            steps=8,
        )
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-12)

    def test_invalid_inputs_raise(self):
        with pytest.raises(TypeError, match="initial_terms"):
            self.method.evolve([SIGMA_Z], t=0.5, steps=1)

        with pytest.raises(TypeError, match="steps"):
            self.method.evolve([SIGMA_Z], t=0.5, initial_terms=[SIGMA_X])

        with pytest.raises(ValueError, match="at least 1"):
            self.method.evolve([SIGMA_Z], t=0.5, initial_terms=[SIGMA_X], steps=0)

        with pytest.raises(TypeError, match="integer"):
            self.method.evolve([SIGMA_Z], t=0.5, initial_terms=[SIGMA_X], steps=1.5)

        with pytest.raises(ValueError, match="square matrices"):
            self.method.evolve(
                [np.array(1.0, dtype=complex)],
                t=0.5,
                initial_terms=[SIGMA_X],
                steps=1,
            )

        with pytest.raises(ValueError, match="same shape"):
            self.method.evolve(
                [SIGMA_Z],
                t=0.5,
                initial_terms=[np.eye(3, dtype=complex)],
                steps=1,
            )

        with pytest.raises(ValueError, match="Hermitian"):
            self.method.evolve(
                [np.array([[0, 1], [0, 0]], dtype=complex)],
                t=0.5,
                initial_terms=[SIGMA_X],
                steps=1,
            )

        with pytest.raises(ValueError, match="schedule"):
            self.method.evolve(
                [SIGMA_Z],
                t=0.5,
                initial_terms=[SIGMA_X],
                steps=1,
                schedule={"type": "unsupported"},
            )

        with pytest.raises(ValueError, match="finite"):
            self.method.evolve(
                [SIGMA_Z],
                t=0.5,
                initial_terms=[SIGMA_X],
                steps=1,
                schedule={"type": "power", "power": float("nan")},
            )

        with pytest.raises(ValueError, match="finite"):
            self.method.evolve(
                [SIGMA_Z],
                t=0.5,
                initial_terms=[SIGMA_X],
                steps=1,
                schedule={"type": "power", "power": float("inf")},
            )
