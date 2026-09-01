"""Tests for controlled and domain-motivated publication workloads."""

import math

import numpy as np
import pytest

from openqevo.workloads import (
    commutator_graph_density,
    controlled_pauli_hamiltonian,
    h2_two_qubit,
    heisenberg_chain,
    pauli_words_commute,
    transverse_field_ising,
)


def test_pauli_commutation_uses_parity():
    assert pauli_words_commute("XX", "YY")
    assert not pauli_words_commute("XI", "ZI")
    with pytest.raises(ValueError, match="same length"):
        pauli_words_commute("X", "XX")


@pytest.mark.parametrize("structure", ["commuting", "mixed", "dense"])
def test_controlled_workloads_are_reproducible_and_normalized(structure):
    kwargs = {
        "n_qubits": 3,
        "term_count": 3,
        "lambda_norm": 2.5,
        "pauli_weight": 1,
        "commutator_structure": structure,
        "coefficient_distribution": "skewed",
        "seed": 17,
    }
    first = controlled_pauli_hamiltonian(**kwargs)
    second = controlled_pauli_hamiltonian(**kwargs)

    assert first.to_dict() == second.to_dict()
    assert math.isclose(first.lambda_norm, 2.5)
    assert all(term.weight == 1 for term in first.terms)
    assert first.mapping_metadata["commutator_graph_density"] == pytest.approx(
        commutator_graph_density(first)
    )
    if structure == "commuting":
        assert commutator_graph_density(first) == 0


def test_spin_models_have_expected_terms_and_are_hermitian():
    tfim = transverse_field_ising(3)
    heisenberg = heisenberg_chain(3)

    assert len(tfim.terms) == 5
    assert len(heisenberg.terms) == 9
    assert np.allclose(tfim.to_matrix(), tfim.to_matrix().conj().T)
    assert np.allclose(heisenberg.to_matrix(), heisenberg.to_matrix().conj().T)


def test_h2_archived_operator_has_transparent_provenance():
    hamiltonian = h2_two_qubit()

    assert hamiltonian.units == "hartree"
    assert len(hamiltonian.terms) == 5
    assert hamiltonian.mapping_metadata["molecule"] == "H2"
    assert "does not claim" in hamiltonian.mapping_metadata["scope_note"]
