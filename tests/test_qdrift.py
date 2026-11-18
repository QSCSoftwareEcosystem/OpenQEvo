"""Tests for qDRIFT randomized evolution."""

import numpy as np
import pytest
from scipy.linalg import expm

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

    def test_sample_sequence_can_be_archived_and_replayed(self):
        terms = [SIGMA_X, SIGMA_Z]
        sequence = self.method.sample_sequence(terms, samples=8, seed=7)

        sampled = self.method.evolve(terms, t=0.5, samples=8, seed=7)
        replayed = self.method.evolve(
            terms,
            t=0.5,
            samples=8,
            sampled_sequence=sequence,
        )

        assert len(sequence) == 8
        assert set(sequence) <= {0, 1}
        np.testing.assert_allclose(sampled, replayed, atol=1e-12)

    def test_external_rng_advances_an_ensemble_stream(self):
        terms = [SIGMA_X, SIGMA_Z]
        first_rng = np.random.default_rng(12)
        second_rng = np.random.default_rng(12)

        first = self.method.sample_sequence(terms, samples=8, rng=first_rng)
        second = self.method.sample_sequence(terms, samples=8, rng=first_rng)

        assert first == self.method.sample_sequence(terms, samples=8, rng=second_rng)
        assert second == self.method.sample_sequence(terms, samples=8, rng=second_rng)

    def test_sample_sequence_validation(self):
        terms = [SIGMA_X, SIGMA_Z]

        with pytest.raises(ValueError, match="mutually exclusive"):
            self.method.sample_sequence(
                terms,
                samples=2,
                seed=1,
                rng=np.random.default_rng(1),
            )

        with pytest.raises(ValueError, match="length"):
            self.method.evolve(
                terms,
                t=0.5,
                samples=2,
                sampled_sequence=[0],
            )

        with pytest.raises(ValueError, match="out-of-range"):
            self.method.evolve(
                terms,
                t=0.5,
                samples=2,
                sampled_sequence=[0, 2],
            )

        with pytest.raises(ValueError, match="does not match"):
            self.method.evolve(
                terms,
                t=0.5,
                samples=2,
                seed=7,
                sampled_sequence=[0, 0],
            )

    def test_result_is_unitary(self):
        result = self.method.evolve([SIGMA_X, SIGMA_Z], t=0.5, samples=8, seed=3)
        identity = result @ result.conj().T
        np.testing.assert_allclose(identity, np.eye(2), atol=1e-12)

    def test_steps_alias_for_samples(self):
        result = self.method.evolve([SIGMA_Z], t=0.5, steps=4, seed=123)
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.5)
        np.testing.assert_allclose(result, exact, atol=1e-12)

    def test_term_weights_control_sampling(self):
        result = self.method.run(
            [SIGMA_X, SIGMA_Z],
            t=0.5,
            samples=4,
            seed=123,
            term_weights=[1.0, 3.0],
        )
        probabilities = [0.25, 0.75]
        expected = np.eye(2, dtype=complex)
        for index in result.sampled_sequence:
            term = [SIGMA_X, SIGMA_Z][index]
            expected = expm(-1j * term * (0.5 / 4 / probabilities[index])) @ expected

        assert set(result.sampled_sequence) == {0, 1}
        assert result.parameters["sampling_probabilities"] == probabilities
        np.testing.assert_allclose(result.unitary, expected, atol=1e-12)

    @pytest.mark.parametrize(
        "entrypoint",
        ["evolve", "run", "sample_sequence", "ensemble_channel", "run_ensemble"],
    )
    @pytest.mark.parametrize(
        ("terms", "weights"),
        [
            ([SIGMA_X, SIGMA_Z], [0.0, 1.0]),
            ([SIGMA_X, SIGMA_Z], [1.0, 0.0]),
            ([1e-200 * SIGMA_X, SIGMA_Z], [0.0, 1.0]),
        ],
        ids=["first-term", "second-term", "tiny-nonzero-term"],
    )
    def test_nonzero_terms_require_sampling_support(self, entrypoint, terms, weights):
        params = {"samples": 2, "term_weights": weights}
        if entrypoint != "sample_sequence":
            params["t"] = 0.5
        with pytest.raises(ValueError, match="positive sampling probability"):
            getattr(self.method, entrypoint)(terms, **params)

    def test_replay_cannot_omit_a_nonzero_term_from_sampling_support(self):
        with pytest.raises(ValueError, match="positive sampling probability"):
            self.method.evolve(
                [SIGMA_X, SIGMA_Z],
                t=0.5,
                samples=2,
                term_weights=[0.0, 1.0],
                sampled_sequence=[1, 1],
            )

    @pytest.mark.parametrize(
        "entrypoint",
        ["evolve", "run", "sample_sequence", "ensemble_channel", "run_ensemble"],
    )
    @pytest.mark.parametrize("weights", [None, [0.0, 1.0]])
    def test_zero_matrix_terms_may_have_zero_weight(self, entrypoint, weights):
        params = {"samples": 2, "term_weights": weights}
        if entrypoint != "sample_sequence":
            params["t"] = 0.5
        result = getattr(self.method, entrypoint)(
            [np.zeros_like(SIGMA_X), SIGMA_Z], **params
        )
        if entrypoint == "sample_sequence":
            assert result == (1, 1)
            return

        expected = expm(-1j * SIGMA_Z * 0.5)
        if entrypoint in {"ensemble_channel", "run_ensemble"}:
            expected = np.kron(expected.conj(), expected)
        if entrypoint in {"run", "run_ensemble"}:
            result = result.output
        np.testing.assert_allclose(result, expected, atol=1e-12)

    @pytest.mark.parametrize(
        ("weights", "error"),
        [
            ([1e-300, 1e300], "positive sampling probability"),
            ([1e308, 1e308], "sum.*finite"),
        ],
        ids=["probability-underflow", "weight-sum-overflow"],
    )
    def test_invalid_normalization_cannot_silently_drop_terms(self, weights, error):
        with pytest.raises(ValueError, match=error):
            self.method.ensemble_channel(
                [SIGMA_X, SIGMA_Z], t=0.5, samples=2, term_weights=weights
            )

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

    def test_canonical_coefficients_control_sampling_and_sign(self):
        hamiltonian = openqevo.PauliHamiltonian(
            identifier="negative-z",
            terms=(openqevo.PauliTerm(-2.0, "Z"),),
        )
        result = self.method.run(hamiltonian, t=0.5, samples=4, seed=7)
        exact = openqevo.get("exact").evolve(hamiltonian, t=0.5)

        np.testing.assert_allclose(result.unitary, exact, atol=1e-12)
        assert result.parameters["term_weights"] == [2.0]
        assert result.parameters["sampling_probabilities"] == [1.0]
        assert result.sampled_sequence == (0, 0, 0, 0)

    def test_canonical_weights_cannot_be_overridden(self):
        hamiltonian = openqevo.PauliHamiltonian(
            identifier="xz",
            terms=(
                openqevo.PauliTerm(1.0, "X"),
                openqevo.PauliTerm(2.0, "Z"),
            ),
        )

        with pytest.raises(ValueError, match="cannot override"):
            self.method.evolve(
                hamiltonian,
                t=0.5,
                samples=4,
                seed=3,
                term_weights=[1.0, 1.0],
            )

    def test_expected_ensemble_channel_converges_with_budget(self):
        hamiltonian = openqevo.PauliHamiltonian(
            identifier="xz",
            terms=(
                openqevo.PauliTerm(1.0, "X"),
                openqevo.PauliTerm(1.0, "Z"),
            ),
        )
        exact_unitary = openqevo.get("exact").evolve(hamiltonian, t=1.0)
        exact_channel = np.kron(exact_unitary.conj(), exact_unitary)

        low_budget = self.method.run_ensemble(hamiltonian, t=1.0, samples=8)
        high_budget = self.method.run_ensemble(hamiltonian, t=1.0, samples=128)
        low_error = np.linalg.norm(low_budget.output - exact_channel, ord=2)
        high_error = np.linalg.norm(high_budget.output - exact_channel, ord=2)

        assert low_budget.representation == "channel"
        assert high_error < low_error
