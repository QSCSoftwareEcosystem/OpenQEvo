"""Tests for dense reference implementations of additional strategies."""

import json
from pathlib import Path

import numpy as np
import pytest

import openqevo

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)


def _unitarity_error(unitary):
    return np.linalg.norm(unitary @ unitary.conj().T - np.eye(unitary.shape[0]))


def test_advanced_methods_are_registered_with_context():
    for name in ("krylov", "interaction_picture", "annealing"):
        method = openqevo.get(name)
        assert method.context is not None
        assert method.context["execution"]["implemented"] is True


def test_advanced_methods_execute_through_their_context_contracts():
    configurations = {
        "krylov": {"krylov_dim": 2},
        "interaction_picture": {"steps": 8},
        "annealing": {"steps": 8},
    }
    for name, parameters in configurations.items():
        result = openqevo.execute_recommendation(
            {"method_name": name, "parameters": parameters},
            terms=[SIGMA_X, SIGMA_Z],
            t=0.3,
            structured=True,
        )
        assert result.method_name == name
        assert _unitarity_error(result.unitary) < 1e-10


def test_interaction_picture_recommendation_is_executable():
    path = Path(
        "context/selection/recommendation_examples/interaction_picture_executable.json"
    )
    recommendation = json.loads(path.read_text(encoding="utf-8"))
    result = openqevo.execute_recommendation(
        recommendation,
        terms=[SIGMA_X, SIGMA_Z],
        t=0.3,
        structured=True,
    )
    assert result.method_name == "interaction_picture"
    assert _unitarity_error(result.unitary) < 1e-10


class TestKrylovEvolution:
    def test_full_dimension_krylov_matches_exact_reference(self):
        terms = [SIGMA_X, SIGMA_Z]
        approximation = openqevo.get("krylov").evolve(terms, t=0.7, krylov_dim=2)
        exact = openqevo.get("exact").evolve(terms, t=0.7)
        np.testing.assert_allclose(approximation, exact, atol=1e-12)

    def test_larger_krylov_space_improves_the_dense_reference(self):
        terms = [SIGMA_X, SIGMA_Z]
        exact = openqevo.get("exact").evolve(terms, t=0.7)
        low = openqevo.get("krylov").evolve(terms, t=0.7, krylov_dim=1)
        high = openqevo.get("krylov").evolve(terms, t=0.7, krylov_dim=2)
        assert np.linalg.norm(high - exact) < np.linalg.norm(low - exact)

    def test_run_reports_the_approximation_configuration(self):
        result = openqevo.get("krylov").run([SIGMA_Z], t=0.4, krylov_dim=1)
        assert result.parameters["krylov_dim"] == 1
        assert result.warnings
        assert _unitarity_error(result.unitary) < 1e-12


class TestInteractionPictureEvolution:
    def test_reference_only_hamiltonian_is_exact(self):
        hamiltonian = openqevo.PauliHamiltonian(
            identifier="diagonal-z",
            terms=(openqevo.PauliTerm(1.2, "Z"),),
        )
        approximation = openqevo.get("interaction_picture").evolve(
            hamiltonian, t=0.8, steps=3
        )
        exact = openqevo.get("exact").evolve(hamiltonian, t=0.8)
        np.testing.assert_allclose(approximation, exact, atol=1e-12)

    def test_midpoint_steps_converge_for_a_noncommuting_split(self):
        hamiltonian = openqevo.PauliHamiltonian(
            identifier="xz",
            terms=(
                openqevo.PauliTerm(0.8, "X"),
                openqevo.PauliTerm(1.1, "Z"),
            ),
        )
        exact = openqevo.get("exact").evolve(hamiltonian, t=1.0)
        coarse = openqevo.get("interaction_picture").evolve(hamiltonian, t=1.0, steps=4)
        fine = openqevo.get("interaction_picture").evolve(hamiltonian, t=1.0, steps=64)
        assert np.linalg.norm(fine - exact) < np.linalg.norm(coarse - exact)

    def test_run_reports_the_automatic_diagonal_reference_split(self):
        hamiltonian = openqevo.PauliHamiltonian(
            identifier="xz",
            terms=(
                openqevo.PauliTerm(1.0, "X"),
                openqevo.PauliTerm(1.0, "Z"),
            ),
        )
        result = openqevo.get("interaction_picture").run(hamiltonian, t=0.5, steps=8)
        assert result.parameters["reference_term_labels"] == ["Z"]
        assert _unitarity_error(result.unitary) < 1e-12

    def test_invalid_reference_indices_are_rejected(self):
        with pytest.raises(ValueError, match="out-of-range"):
            openqevo.get("interaction_picture").evolve(
                [SIGMA_X, SIGMA_Z], t=0.5, steps=2, reference_term_indices=[2]
            )


class TestAnnealingEvolution:
    def test_constant_schedule_is_exact(self):
        approximation = openqevo.get("annealing").evolve(
            [SIGMA_Z], t=0.7, steps=6, initial_hamiltonian=[SIGMA_Z]
        )
        exact = openqevo.get("exact").evolve([SIGMA_Z], t=0.7)
        np.testing.assert_allclose(approximation, exact, atol=1e-12)

    def test_more_steps_improve_a_linear_schedule(self):
        method = openqevo.get("annealing")
        reference = method.evolve(
            [SIGMA_Z], t=1.0, steps=1024, initial_hamiltonian=[-SIGMA_X]
        )
        coarse = method.evolve(
            [SIGMA_Z], t=1.0, steps=4, initial_hamiltonian=[-SIGMA_X]
        )
        fine = method.evolve([SIGMA_Z], t=1.0, steps=64, initial_hamiltonian=[-SIGMA_X])
        assert np.linalg.norm(fine - reference) < np.linalg.norm(coarse - reference)

    def test_default_driver_and_result_metadata(self):
        result = openqevo.get("annealing").run([SIGMA_Z], t=0.5, steps=16)
        assert result.parameters["schedule"] == "linear"
        assert result.parameters["initial_hamiltonian"]["kind"] == (
            "default_transverse_field_driver"
        )
        assert _unitarity_error(result.unitary) < 1e-12

    def test_only_linear_schedule_is_supported(self):
        with pytest.raises(ValueError, match="linear"):
            openqevo.get("annealing").evolve(
                [SIGMA_Z], t=0.5, steps=2, schedule="quadratic"
            )
