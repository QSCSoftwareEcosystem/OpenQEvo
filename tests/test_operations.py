"""Tests for scalable operation output and deterministic reference costs."""

import json

import jsonschema
import numpy as np
from scipy.linalg import expm

import openqevo
from openqevo.operations import PauliEvolutionOperation


def _xz_hamiltonian():
    return openqevo.PauliHamiltonian(
        identifier="operations-xz",
        terms=(
            openqevo.PauliTerm(0.7, "X"),
            openqevo.PauliTerm(-0.4, "Z"),
        ),
    )


def test_pauli_operation_uses_explicit_rotation_and_qubit_order_conventions():
    operation = PauliEvolutionOperation(
        term_index=0,
        coefficient=-0.25,
        pauli_word="XY",
        qubit_order=(1, 0),
        time=0.8,
    )
    generator = openqevo.PauliTerm(-0.25, "XY", qubit_order=(1, 0)).to_matrix()

    np.testing.assert_allclose(operation.to_matrix(), expm(-1j * generator * 0.8))
    assert operation.rotation_angle == -0.4
    assert operation.active_qubits == (0, 1)


def test_native_trotter_operation_output_matches_dense_compatibility_path():
    hamiltonian = _xz_hamiltonian()
    method = openqevo.get("trotter_s2")
    dense = method.run(hamiltonian, t=0.6, steps=2)
    operations = method.run(
        hamiltonian,
        t=0.6,
        steps=2,
        representation="operations",
    )
    circuit = method.run(
        hamiltonian,
        t=0.6,
        steps=2,
        representation="circuit",
    )

    np.testing.assert_allclose(operations.output.to_unitary(), dense.unitary)
    assert operations.representation == "operations"
    assert len(operations.output.operations) == 5
    assert operations.costs.formula_level_pauli_operations == 8
    assert operations.costs.adjacent_merged_pauli_operations == 5
    assert circuit.representation == "circuit"
    assert circuit.costs.compiled_one_qubit_gates == 11
    assert circuit.costs.compiled_two_qubit_gates == 0
    assert circuit.costs.circuit_depth == 11
    assert circuit.output.sha256 == circuit.output_sha256


def test_qdrift_operation_output_replays_the_sampled_dense_trajectory():
    hamiltonian = _xz_hamiltonian()
    method = openqevo.get("qdrift")
    dense = method.run(hamiltonian, t=0.4, samples=12, seed=19)
    operations = method.run(
        hamiltonian,
        t=0.4,
        samples=12,
        seed=19,
        representation="operations",
    )

    assert operations.sampled_sequence == dense.sampled_sequence
    np.testing.assert_allclose(operations.output.to_unitary(), dense.unitary)
    assert operations.costs.formula_level_pauli_operations == 12
    assert operations.costs.adjacent_merged_pauli_operations == len(
        operations.output.operations
    )


def test_reference_compiler_counts_weight_two_rotation_and_identity_phase():
    hamiltonian = openqevo.PauliHamiltonian(
        identifier="compile",
        terms=(
            openqevo.PauliTerm(0.5, "XX"),
            openqevo.PauliTerm(-0.2, "II"),
        ),
    )
    result = openqevo.get("trotter_s1").run(
        hamiltonian,
        t=0.3,
        steps=1,
        representation="circuit",
    )

    assert result.output.one_qubit_gates == 5
    assert result.output.two_qubit_gates == 2
    assert result.output.depth == 5
    assert np.isclose(result.output.global_phase, 0.06)


def test_structured_operation_metadata_validates_against_result_schema():
    result = openqevo.get("trotter_s1").run(
        _xz_hamiltonian(),
        t=0.2,
        steps=2,
        representation="operations",
    )
    with open("context/schema/evolution_result.schema.json") as stream:
        schema = json.load(stream)

    metadata = result.to_metadata()
    jsonschema.validate(metadata, schema)
    assert metadata["output"]["operations"] == len(result.output.operations)
    assert metadata["output"]["sha256"] == result.output.sha256


def test_scalable_outputs_validate_against_dedicated_schemas():
    operations = (
        openqevo.get("trotter_s2")
        .run(
            _xz_hamiltonian(),
            t=0.3,
            steps=2,
            representation="operations",
        )
        .output
    )
    circuit = operations.compile_reference()

    with open("context/schema/operation_sequence.schema.json") as stream:
        operation_schema = json.load(stream)
    with open("context/schema/reference_circuit.schema.json") as stream:
        circuit_schema = json.load(stream)

    jsonschema.validate(operations.to_dict(), operation_schema)
    jsonschema.validate(circuit.to_dict(), circuit_schema)
