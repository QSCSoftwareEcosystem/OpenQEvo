"""Tests for dense interaction-picture evolution."""

import json

import numpy as np
import pytest

import openqevo

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
ZERO_2 = np.zeros((2, 2), dtype=complex)


class TestInteractionPicture:
    def setup_method(self):
        self.method = openqevo.get("interaction_picture")

    def test_registered(self):
        assert "interaction_picture" in openqevo.list_methods()
        assert self.method.source == "openqevo"

    def test_implicit_reference_matches_single_term_exact(self):
        result = self.method.evolve([SIGMA_X], t=0.5, steps=1)
        exact = openqevo.get("exact").evolve([SIGMA_X], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_zero_interaction_matches_dominant_exact(self):
        result = self.method.evolve(
            [ZERO_2],
            t=0.5,
            dominant_terms=[SIGMA_Z],
            steps=4,
        )
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_zero_dominant_matches_residual_exact_for_single_term(self):
        result = self.method.evolve(
            [SIGMA_X],
            t=0.5,
            dominant_terms=[ZERO_2],
            steps=4,
        )
        exact = openqevo.get("exact").evolve([SIGMA_X], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_commuting_split_matches_exact(self):
        result = self.method.evolve(
            [0.25 * SIGMA_Z],
            t=0.5,
            dominant_terms=[SIGMA_Z],
            steps=4,
        )
        exact = openqevo.get("exact").evolve([SIGMA_Z, 0.25 * SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_converges_with_more_steps(self):
        terms = [SIGMA_X]
        dominant_terms = [0.75 * SIGMA_Z]
        exact = openqevo.get("exact").evolve([*dominant_terms, *terms], t=1.0)

        error_5 = np.linalg.norm(
            self.method.evolve(
                terms,
                t=1.0,
                dominant_terms=dominant_terms,
                steps=5,
            )
            - exact
        )
        error_50 = np.linalg.norm(
            self.method.evolve(
                terms,
                t=1.0,
                dominant_terms=dominant_terms,
                steps=50,
            )
            - exact
        )
        assert error_50 < error_5

    def test_result_is_unitary(self):
        result = self.method.evolve(
            [SIGMA_X, SIGMA_Y],
            t=0.5,
            dominant_terms=[SIGMA_Z],
            steps=8,
        )
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-12)

    def test_explicit_reference_provenance_is_serializable_and_distinct(self):
        result = self.method.run([SIGMA_X], t=0.5, dominant_terms=[SIGMA_Z], steps=16)
        different_reference = self.method.run(
            [SIGMA_X], t=0.5, dominant_terms=[2.0 * SIGMA_Z], steps=16
        )
        metadata = json.loads(json.dumps(result.to_metadata(), allow_nan=False))
        assert metadata["parameters"]["evolution_hamiltonian"] == "H0 + V"
        assert metadata["parameters"]["reference_split"] == "dominant_terms"
        assert metadata["parameters"]["dominant_terms"]["representation"] == (
            "dense_matrix_terms"
        )
        assert result.hamiltonian == different_reference.hamiltonian
        assert (
            result.parameters["dominant_terms"]["sha256"]
            != (different_reference.parameters["dominant_terms"]["sha256"])
        )
        assert np.linalg.norm(result.unitary - different_reference.unitary) > 0.1

    def test_invalid_inputs_raise(self):
        with pytest.raises(TypeError, match="steps"):
            self.method.evolve([SIGMA_X], t=0.5, dominant_terms=[SIGMA_Z])

        with pytest.raises(ValueError, match="at least 1"):
            self.method.evolve([SIGMA_X], t=0.5, dominant_terms=[SIGMA_Z], steps=0)

        with pytest.raises(TypeError, match="integer"):
            self.method.evolve([SIGMA_X], t=0.5, dominant_terms=[SIGMA_Z], steps=1.5)

        with pytest.raises(ValueError, match="square matrices"):
            self.method.evolve(
                [np.array(1.0, dtype=complex)],
                t=0.5,
                dominant_terms=[SIGMA_Z],
                steps=1,
            )

        with pytest.raises(ValueError, match="same dimension"):
            self.method.evolve(
                [SIGMA_X],
                t=0.5,
                dominant_terms=[np.eye(4, dtype=complex)],
                steps=1,
            )

        with pytest.raises(ValueError, match="Hermitian"):
            self.method.evolve(
                [np.array([[0, 1], [0, 0]], dtype=complex)],
                t=0.5,
                dominant_terms=[SIGMA_Z],
                steps=1,
            )

    @pytest.mark.parametrize("order", [1, 1.5, "1", 3])
    def test_unsupported_product_formula_order_is_rejected(self, order):
        with pytest.raises((TypeError, ValueError), match="order"):
            self.method.evolve(
                [SIGMA_X],
                t=0.5,
                dominant_terms=[SIGMA_Z],
                steps=1,
                order=order,
            )

    def test_explicit_and_index_reference_splits_are_mutually_exclusive(self):
        with pytest.raises(ValueError, match="mutually exclusive"):
            self.method.evolve(
                [SIGMA_X],
                t=0.5,
                dominant_terms=[SIGMA_Z],
                reference_term_indices=[0],
                steps=1,
            )
