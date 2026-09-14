"""Tests for canonical Hamiltonian and structured result contracts."""

import json

import jsonschema
import numpy as np
import pytest

import openqevo
from openqevo.hamiltonian import HAMILTONIAN_SCHEMA_VERSION, dense_terms
from openqevo.result import EVOLUTION_RESULT_SCHEMA_VERSION, EvolutionResult


def xz_hamiltonian():
    return openqevo.PauliHamiltonian(
        identifier="test-xz",
        source="tests",
        terms=(
            openqevo.PauliTerm(1.0, "X", source="tests"),
            openqevo.PauliTerm(-0.5, "Z", source="tests"),
        ),
        mapping_metadata={"mapping": "direct"},
    )


def test_pauli_hamiltonian_dense_conversion_and_round_trip():
    hamiltonian = xz_hamiltonian()
    payload = hamiltonian.to_dict()
    restored = openqevo.PauliHamiltonian.from_dict(payload)

    expected = np.array([[-0.5, 1.0], [1.0, 0.5]], dtype=complex)
    np.testing.assert_allclose(hamiltonian.to_matrix(), expected)
    np.testing.assert_allclose(restored.to_matrix(), expected)
    assert payload["schema_version"] == HAMILTONIAN_SCHEMA_VERSION
    assert payload["qubit_order"] == [0]
    assert payload["lambda"] == 1.5
    assert restored.sha256 == hamiltonian.sha256


def test_pauli_hamiltonian_contract_validates_against_schema():
    with open("context/schema/hamiltonian.schema.json") as stream:
        schema = json.load(stream)

    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.validate(instance=xz_hamiltonian().to_dict(), schema=schema)


@pytest.mark.parametrize(
    ("args", "error"),
    [
        ((0.0, "X"), ValueError),
        ((float("nan"), "X"), ValueError),
        ((1.0, "A"), ValueError),
        ((1.0 + 1.0j, "X"), TypeError),
    ],
)
def test_pauli_term_rejects_invalid_coefficients_and_words(args, error):
    with pytest.raises(error):
        openqevo.PauliTerm(*args)


def test_pauli_hamiltonian_rejects_inconsistent_or_duplicate_terms():
    with pytest.raises(ValueError, match="duplicate"):
        openqevo.PauliHamiltonian(
            identifier="duplicate",
            terms=(
                openqevo.PauliTerm(1.0, "X"),
                openqevo.PauliTerm(2.0, "X"),
            ),
        )

    with pytest.raises(ValueError, match="qubit count"):
        openqevo.PauliHamiltonian(
            identifier="dimension-mismatch",
            terms=(
                openqevo.PauliTerm(1.0, "X"),
                openqevo.PauliTerm(1.0, "ZZ"),
            ),
        )


def test_pauli_term_respects_explicit_qubit_order_in_dense_form():
    reordered = openqevo.PauliTerm(1.0, "XZ", qubit_order=(1, 0))
    expected = np.kron(
        np.array([[1, 0], [0, -1]], dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
    )

    np.testing.assert_allclose(reordered.to_matrix(), expected)


def test_dense_matrix_compatibility_is_preserved():
    matrices = dense_terms(xz_hamiltonian())
    exact_from_contract = openqevo.get("exact").evolve(xz_hamiltonian(), t=0.25)
    exact_from_dense = openqevo.get("exact").evolve(matrices, t=0.25)

    np.testing.assert_allclose(exact_from_contract, exact_from_dense)


def test_structured_result_carries_costs_and_provenance():
    result = openqevo.get("trotter_s1").run(xz_hamiltonian(), t=0.5, steps=4)
    metadata = result.to_metadata()

    assert isinstance(result, EvolutionResult)
    assert result.representation == "unitary"
    assert result.unitary.shape == (2, 2)
    assert result.costs.formula_level_pauli_operations == 8
    assert result.hamiltonian["representation"] == "pauli_sum"
    assert metadata["schema_version"] == EVOLUTION_RESULT_SCHEMA_VERSION
    assert metadata["output"]["sha256"] == result.output_sha256
    assert metadata["parameters"]["term_order"] == ["X", "Z"]


def test_structured_result_contract_validates_against_schema():
    with open("context/schema/evolution_result.schema.json") as stream:
        schema = json.load(stream)

    jsonschema.Draft202012Validator.check_schema(schema)
    result = openqevo.get("trotter_s2").run(xz_hamiltonian(), t=0.5, steps=4)
    jsonschema.validate(instance=result.to_metadata(), schema=schema)


def test_recommendation_accepts_serialized_hamiltonian_and_structured_result():
    result = openqevo.execute_recommendation(
        {
            "method_name": "trotter_s1",
            "parameters": {"steps": 2},
            "terms": xz_hamiltonian().to_dict(),
            "t": 0.25,
        },
        structured=True,
    )

    assert isinstance(result, EvolutionResult)
    assert result.method_name == "trotter_s1"
    assert result.hamiltonian["id"] == "test-xz"
