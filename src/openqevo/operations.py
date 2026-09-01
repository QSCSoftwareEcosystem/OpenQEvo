"""Scalable Pauli-evolution operations and a deterministic reference compiler.

The dense matrix API remains useful for small-system validation.  This module
provides the representation used when materializing a full unitary would be
inappropriate: an ordered sequence of Pauli rotations with an explicit
``exp(-i * coefficient * time * P)`` convention.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from numbers import Integral, Real
from typing import Any

import numpy as np
from numpy.typing import NDArray

from openqevo.hamiltonian import PauliHamiltonian, PauliTerm

OPERATION_SEQUENCE_SCHEMA_VERSION = "openqevo-operation-sequence/v1"
REFERENCE_CIRCUIT_SCHEMA_VERSION = "openqevo-reference-circuit/v1"


@dataclass(frozen=True, slots=True)
class PauliEvolutionOperation:
    """One operation with unitary ``exp(-i * coefficient * time * P)``.

    ``rotation_angle`` follows the common Pauli-rotation convention
    ``R_P(theta) = exp(-i * theta * P / 2)`` and therefore equals
    ``2 * coefficient * time``.
    """

    term_index: int
    coefficient: float
    pauli_word: str
    qubit_order: tuple[int, ...] | Sequence[int]
    time: float

    def __post_init__(self) -> None:
        if isinstance(self.term_index, bool) or not isinstance(
            self.term_index, Integral
        ):
            raise TypeError("'term_index' must be an integer.")
        if self.term_index < 0:
            raise ValueError("'term_index' must be non-negative.")
        if isinstance(self.coefficient, bool) or not isinstance(self.coefficient, Real):
            raise TypeError("'coefficient' must be a real number.")
        coefficient = float(self.coefficient)
        if not math.isfinite(coefficient) or coefficient == 0:
            raise ValueError("'coefficient' must be finite and non-zero.")
        if isinstance(self.time, bool) or not isinstance(self.time, Real):
            raise TypeError("'time' must be a real number.")
        time = float(self.time)
        if not math.isfinite(time):
            raise ValueError("'time' must be finite.")

        # Reuse the canonical term validation for Pauli labels and ordering.
        validated = PauliTerm(
            coefficient=coefficient,
            pauli_word=self.pauli_word,
            qubit_order=tuple(self.qubit_order),
        )
        object.__setattr__(self, "term_index", int(self.term_index))
        object.__setattr__(self, "coefficient", coefficient)
        object.__setattr__(self, "qubit_order", validated.qubit_order or ())
        object.__setattr__(self, "time", time)

    @property
    def n_qubits(self) -> int:
        return len(self.pauli_word)

    @property
    def rotation_angle(self) -> float:
        """Angle in ``R_P(theta) = exp(-i theta P / 2)`` convention."""
        return 2.0 * self.coefficient * self.time

    @property
    def active_qubits(self) -> tuple[int, ...]:
        labels = dict(zip(self.qubit_order, self.pauli_word))
        return tuple(qubit for qubit in range(self.n_qubits) if labels[qubit] != "I")

    def to_matrix(self) -> NDArray[np.complex128]:
        """Materialize the operation for small-system validation only."""
        pauli = PauliTerm(
            coefficient=1.0,
            pauli_word=self.pauli_word,
            qubit_order=self.qubit_order,
        ).to_matrix()
        angle = self.coefficient * self.time
        identity = np.eye(2**self.n_qubits, dtype=complex)
        return np.asarray(
            math.cos(angle) * identity - 1j * math.sin(angle) * pauli,
            dtype=complex,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "term_index": self.term_index,
            "coefficient": self.coefficient,
            "pauli_word": self.pauli_word,
            "qubit_order": list(self.qubit_order),
            "time": self.time,
            "rotation_angle": self.rotation_angle,
        }


@dataclass(frozen=True, slots=True)
class GateOperation:
    """One gate in the backend-independent reference circuit."""

    name: str
    qubits: tuple[int, ...] | Sequence[int]
    angle: float | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Gate 'name' must be a non-empty string.")
        qubits = tuple(self.qubits)
        if not qubits:
            raise ValueError("A gate must act on at least one qubit.")
        if any(
            isinstance(qubit, bool) or not isinstance(qubit, Integral)
            for qubit in qubits
        ):
            raise TypeError("Gate qubits must be integers.")
        qubits = tuple(int(qubit) for qubit in qubits)
        if any(qubit < 0 for qubit in qubits) or len(set(qubits)) != len(qubits):
            raise ValueError("Gate qubits must be unique and non-negative.")
        angle = self.angle
        if angle is not None:
            angle = float(angle)
            if not math.isfinite(angle):
                raise ValueError("Gate angle must be finite.")
        object.__setattr__(self, "qubits", qubits)
        object.__setattr__(self, "angle", angle)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"name": self.name, "qubits": list(self.qubits)}
        if self.angle is not None:
            payload["angle"] = self.angle
        return payload


@dataclass(frozen=True, slots=True)
class ReferenceCircuit:
    """Circuit compiled to the fixed ``H/S/Sdg/RZ/CX`` logical basis."""

    n_qubits: int
    gates: tuple[GateOperation, ...] | Sequence[GateOperation]
    global_phase: float = 0.0
    basis: tuple[str, ...] = ("h", "s", "sdg", "rz", "cx")

    def __post_init__(self) -> None:
        if isinstance(self.n_qubits, bool) or not isinstance(self.n_qubits, Integral):
            raise TypeError("'n_qubits' must be an integer.")
        if self.n_qubits < 1:
            raise ValueError("'n_qubits' must be at least 1.")
        gates = tuple(self.gates)
        if any(not isinstance(gate, GateOperation) for gate in gates):
            raise TypeError("'gates' must contain GateOperation values.")
        if any(max(gate.qubits) >= self.n_qubits for gate in gates):
            raise ValueError("A gate references a qubit outside the circuit.")
        phase = float(self.global_phase)
        if not math.isfinite(phase):
            raise ValueError("'global_phase' must be finite.")
        object.__setattr__(self, "n_qubits", int(self.n_qubits))
        object.__setattr__(self, "gates", gates)
        object.__setattr__(self, "global_phase", phase)

    @property
    def one_qubit_gates(self) -> int:
        return sum(len(gate.qubits) == 1 for gate in self.gates)

    @property
    def two_qubit_gates(self) -> int:
        return sum(len(gate.qubits) == 2 for gate in self.gates)

    @property
    def depth(self) -> int:
        """ASAP depth under gate-order and shared-qubit dependencies."""
        last_layer = [0] * self.n_qubits
        maximum = 0
        for gate in self.gates:
            layer = 1 + max(last_layer[qubit] for qubit in gate.qubits)
            for qubit in gate.qubits:
                last_layer[qubit] = layer
            maximum = max(maximum, layer)
        return maximum

    @property
    def sha256(self) -> str:
        return _json_sha256(self.to_dict())

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": REFERENCE_CIRCUIT_SCHEMA_VERSION,
            "n_qubits": self.n_qubits,
            "basis": list(self.basis),
            "global_phase": self.global_phase,
            "gates": [gate.to_dict() for gate in self.gates],
            "resources": {
                "one_qubit_gates": self.one_qubit_gates,
                "two_qubit_gates": self.two_qubit_gates,
                "depth": self.depth,
            },
        }


@dataclass(frozen=True, slots=True)
class OperationSequence:
    """Ordered, serializable Pauli-evolution operations."""

    n_qubits: int
    operations: tuple[PauliEvolutionOperation, ...] | Sequence[PauliEvolutionOperation]
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if isinstance(self.n_qubits, bool) or not isinstance(self.n_qubits, Integral):
            raise TypeError("'n_qubits' must be an integer.")
        if self.n_qubits < 1:
            raise ValueError("'n_qubits' must be at least 1.")
        operations = tuple(self.operations)
        if any(
            not isinstance(operation, PauliEvolutionOperation)
            for operation in operations
        ):
            raise TypeError("'operations' must contain PauliEvolutionOperation values.")
        if any(operation.n_qubits != self.n_qubits for operation in operations):
            raise ValueError("Every operation must use the sequence qubit count.")
        if not isinstance(self.metadata, Mapping):
            raise TypeError("'metadata' must be a mapping.")
        metadata = _json_compatible(dict(self.metadata))
        object.__setattr__(self, "n_qubits", int(self.n_qubits))
        object.__setattr__(self, "operations", operations)
        object.__setattr__(self, "metadata", metadata)

    @property
    def sha256(self) -> str:
        return _json_sha256(self.to_dict())

    def compact_adjacent(self, *, atol: float = 1e-15) -> OperationSequence:
        """Merge adjacent rotations generated by the same Hamiltonian term."""
        compacted: list[PauliEvolutionOperation] = []
        for operation in self.operations:
            if compacted and _same_generator(compacted[-1], operation):
                previous = compacted.pop()
                combined_time = previous.time + operation.time
                if not math.isclose(combined_time, 0.0, abs_tol=atol):
                    compacted.append(
                        PauliEvolutionOperation(
                            term_index=previous.term_index,
                            coefficient=previous.coefficient,
                            pauli_word=previous.pauli_word,
                            qubit_order=previous.qubit_order,
                            time=combined_time,
                        )
                    )
            elif not math.isclose(operation.time, 0.0, abs_tol=atol):
                compacted.append(operation)
        metadata = dict(self.metadata)
        metadata["compaction"] = "adjacent-identical-generators"
        metadata["uncompacted_operations"] = len(self.operations)
        return OperationSequence(self.n_qubits, tuple(compacted), metadata)

    def compile_reference(self) -> ReferenceCircuit:
        """Compile Pauli rotations to the documented all-to-all logical basis."""
        gates: list[GateOperation] = []
        global_phase = 0.0
        for operation in self.operations:
            labels = dict(zip(operation.qubit_order, operation.pauli_word))
            active = operation.active_qubits
            if not active:
                global_phase -= operation.coefficient * operation.time
                continue

            for qubit in active:
                label = labels[qubit]
                if label == "X":
                    gates.append(GateOperation("h", (qubit,)))
                elif label == "Y":
                    gates.append(GateOperation("sdg", (qubit,)))
                    gates.append(GateOperation("h", (qubit,)))

            for control, target in zip(active, active[1:]):
                gates.append(GateOperation("cx", (control, target)))
            gates.append(
                GateOperation("rz", (active[-1],), angle=operation.rotation_angle)
            )
            for control, target in reversed(tuple(zip(active, active[1:]))):
                gates.append(GateOperation("cx", (control, target)))

            for qubit in active:
                label = labels[qubit]
                if label == "X":
                    gates.append(GateOperation("h", (qubit,)))
                elif label == "Y":
                    gates.append(GateOperation("h", (qubit,)))
                    gates.append(GateOperation("s", (qubit,)))

        return ReferenceCircuit(
            n_qubits=self.n_qubits,
            gates=tuple(gates),
            global_phase=global_phase,
        )

    def to_unitary(self) -> NDArray[np.complex128]:
        """Materialize the sequence for validation; not a scalable execution path."""
        result = np.eye(2**self.n_qubits, dtype=complex)
        for operation in self.operations:
            result = operation.to_matrix() @ result
        return np.asarray(result, dtype=complex)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": OPERATION_SEQUENCE_SCHEMA_VERSION,
            "n_qubits": self.n_qubits,
            "operations": [operation.to_dict() for operation in self.operations],
            "metadata": dict(self.metadata),
        }


def trotter_operation_sequence(
    hamiltonian: PauliHamiltonian,
    t: float,
    *,
    steps: int,
    order: int,
) -> OperationSequence:
    """Build the exact ordered Pauli rotations for first/second-order formulas."""
    if not isinstance(hamiltonian, PauliHamiltonian):
        raise TypeError("Operation output requires a canonical PauliHamiltonian.")
    if isinstance(steps, bool) or not isinstance(steps, Integral):
        raise TypeError("'steps' must be an integer.")
    if steps < 1:
        raise ValueError("'steps' must be at least 1.")
    if order not in {1, 2}:
        raise ValueError("Native operation output supports Trotter order 1 or 2.")

    dt = float(t) / int(steps)
    schedule: list[tuple[int, float]] = []
    for _ in range(int(steps)):
        if order == 1:
            schedule.extend((index, dt) for index in range(len(hamiltonian.terms)))
        else:
            half = dt / 2.0
            schedule.extend((index, half) for index in range(len(hamiltonian.terms)))
            schedule.extend(
                (index, half) for index in reversed(range(len(hamiltonian.terms)))
            )

    operations = tuple(
        _operation_from_term(hamiltonian, term_index, operation_time)
        for term_index, operation_time in schedule
    )
    return OperationSequence(
        n_qubits=hamiltonian.n_qubits,
        operations=operations,
        metadata={
            "method_family": "trotter-suzuki",
            "order": order,
            "steps": int(steps),
            "evolution_time": float(t),
            "hamiltonian_sha256": hamiltonian.sha256,
        },
    )


def sampled_operation_sequence(
    hamiltonian: PauliHamiltonian,
    t: float,
    *,
    sampled_sequence: Sequence[int],
) -> OperationSequence:
    """Build qDRIFT rotations for an already sampled term-index sequence."""
    if not isinstance(hamiltonian, PauliHamiltonian):
        raise TypeError("Operation output requires a canonical PauliHamiltonian.")
    sequence = tuple(int(index) for index in sampled_sequence)
    if not sequence:
        raise ValueError("'sampled_sequence' must contain at least one term index.")
    if any(index < 0 or index >= len(hamiltonian.terms) for index in sequence):
        raise ValueError("'sampled_sequence' contains an out-of-range term index.")

    probabilities = np.array(
        [abs(term.coefficient) for term in hamiltonian.terms], dtype=float
    )
    probabilities /= probabilities.sum()
    dt = float(t) / len(sequence)
    operations = tuple(
        _operation_from_term(
            hamiltonian,
            index,
            dt / float(probabilities[index]),
        )
        for index in sequence
    )
    return OperationSequence(
        n_qubits=hamiltonian.n_qubits,
        operations=operations,
        metadata={
            "method_family": "qdrift",
            "samples": len(sequence),
            "evolution_time": float(t),
            "hamiltonian_sha256": hamiltonian.sha256,
        },
    )


def _operation_from_term(
    hamiltonian: PauliHamiltonian,
    term_index: int,
    operation_time: float,
) -> PauliEvolutionOperation:
    term = hamiltonian.terms[term_index]
    return PauliEvolutionOperation(
        term_index=term_index,
        coefficient=term.coefficient,
        pauli_word=term.pauli_word,
        qubit_order=term.qubit_order or (),
        time=operation_time,
    )


def _same_generator(
    left: PauliEvolutionOperation,
    right: PauliEvolutionOperation,
) -> bool:
    return (
        left.term_index == right.term_index
        and left.pauli_word == right.pauli_word
        and left.qubit_order == right.qubit_order
        and left.coefficient == right.coefficient
    )


def _json_sha256(payload: Mapping[str, Any]) -> str:
    encoded = (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _json_compatible(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_compatible(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_json_compatible(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError(f"Value of type {type(value).__name__!r} is not JSON-compatible.")
