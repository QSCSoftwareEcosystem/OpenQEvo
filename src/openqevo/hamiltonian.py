"""Canonical Hamiltonian contracts and dense compatibility helpers."""

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

HAMILTONIAN_SCHEMA_VERSION = "openqevo-pauli-hamiltonian/v1"

_PAULI_MATRICES: dict[str, NDArray[np.complex128]] = {
    "I": np.eye(2, dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


@dataclass(frozen=True, slots=True)
class PauliTerm:
    """One real-weighted Pauli word with explicit tensor-factor ordering.

    ``pauli_word[index]`` acts on ``qubit_order[index]``. The word is a full
    system word, including identities, so its length is the qubit count.
    """

    coefficient: float
    pauli_word: str
    qubit_order: tuple[int, ...] | None = None
    source: str | None = None
    units: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if isinstance(self.coefficient, bool) or not isinstance(self.coefficient, Real):
            raise TypeError("Pauli coefficients must be real numbers.")
        coefficient = float(self.coefficient)
        if not math.isfinite(coefficient):
            raise ValueError("Pauli coefficients must be finite.")
        if coefficient == 0:
            raise ValueError("Canonical Pauli terms must have non-zero coefficients.")

        if not isinstance(self.pauli_word, str) or not self.pauli_word:
            raise ValueError("'pauli_word' must be a non-empty string.")
        if any(label not in _PAULI_MATRICES for label in self.pauli_word):
            raise ValueError("'pauli_word' may contain only I, X, Y, and Z.")

        if self.qubit_order is None:
            qubit_order = tuple(range(len(self.pauli_word)))
        else:
            qubit_order = tuple(self.qubit_order)
        if len(qubit_order) != len(self.pauli_word):
            raise ValueError("'qubit_order' length must match 'pauli_word'.")
        if any(
            isinstance(qubit, bool) or not isinstance(qubit, Integral)
            for qubit in qubit_order
        ):
            raise TypeError("'qubit_order' must contain integer qubit indices.")
        qubit_order = tuple(int(qubit) for qubit in qubit_order)
        if sorted(qubit_order) != list(range(len(self.pauli_word))):
            raise ValueError(
                "'qubit_order' must be a permutation of all system qubits."
            )

        for field_name, value in (("source", self.source), ("units", self.units)):
            if value is not None and (not isinstance(value, str) or not value.strip()):
                raise ValueError(f"'{field_name}' must be a non-empty string.")
        if not isinstance(self.metadata, Mapping):
            raise TypeError("'metadata' must be a mapping.")
        metadata = dict(self.metadata)
        _validate_json_metadata(metadata, "metadata")

        object.__setattr__(self, "coefficient", coefficient)
        object.__setattr__(self, "qubit_order", qubit_order)
        object.__setattr__(self, "metadata", metadata)

    @property
    def n_qubits(self) -> int:
        """Number of qubits represented by the full Pauli word."""
        return len(self.pauli_word)

    @property
    def weight(self) -> int:
        """Number of non-identity factors in the Pauli word."""
        return sum(label != "I" for label in self.pauli_word)

    def to_matrix(self) -> NDArray[np.complex128]:
        """Return the dense matrix in ascending computational-qubit order."""
        labels_by_qubit = dict(zip(self.qubit_order or (), self.pauli_word))
        matrix = np.array([[1]], dtype=complex)
        for qubit in range(self.n_qubits):
            matrix = np.kron(matrix, _PAULI_MATRICES[labels_by_qubit[qubit]])
        return np.asarray(self.coefficient * matrix, dtype=complex)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible canonical representation."""
        payload: dict[str, Any] = {
            "coefficient": self.coefficient,
            "pauli_word": self.pauli_word,
            "qubit_order": list(self.qubit_order or ()),
        }
        if self.source is not None:
            payload["source"] = self.source
        if self.units is not None:
            payload["units"] = self.units
        if self.metadata:
            payload["metadata"] = dict(self.metadata)
        return payload

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> PauliTerm:
        """Construct a validated term from its JSON-compatible form."""
        return cls(
            coefficient=payload["coefficient"],
            pauli_word=payload["pauli_word"],
            qubit_order=tuple(payload.get("qubit_order", ())) or None,
            source=payload.get("source"),
            units=payload.get("units"),
            metadata=payload.get("metadata", {}),
        )


@dataclass(frozen=True, slots=True)
class PauliHamiltonian:
    """Validated, ordered Pauli-sum Hamiltonian used across OpenQEvo methods."""

    terms: tuple[PauliTerm, ...] | Sequence[PauliTerm]
    identifier: str
    source: str | None = None
    units: str | None = None
    mapping_metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        terms = tuple(self.terms)
        if not terms:
            raise ValueError("At least one Pauli term is required.")
        if any(not isinstance(term, PauliTerm) for term in terms):
            raise TypeError("'terms' must contain only PauliTerm objects.")
        if not isinstance(self.identifier, str) or not self.identifier.strip():
            raise ValueError("'identifier' must be a non-empty string.")
        if self.source is not None and (
            not isinstance(self.source, str) or not self.source.strip()
        ):
            raise ValueError("'source' must be a non-empty string.")
        if self.units is not None and (
            not isinstance(self.units, str) or not self.units.strip()
        ):
            raise ValueError("'units' must be a non-empty string.")
        if not isinstance(self.mapping_metadata, Mapping):
            raise TypeError("'mapping_metadata' must be a mapping.")
        mapping_metadata = dict(self.mapping_metadata)
        _validate_json_metadata(mapping_metadata, "mapping_metadata")

        first = terms[0]
        seen_words: set[str] = set()
        for term in terms:
            if term.n_qubits != first.n_qubits:
                raise ValueError("All Pauli terms must use the same qubit count.")
            if term.qubit_order != first.qubit_order:
                raise ValueError("All Pauli terms must use the same qubit ordering.")
            if term.pauli_word in seen_words:
                raise ValueError(
                    "Canonical Pauli Hamiltonians cannot contain duplicate words."
                )
            seen_words.add(term.pauli_word)
            if self.units is not None and term.units not in (None, self.units):
                raise ValueError("Term units must match the Hamiltonian units.")

        object.__setattr__(self, "terms", terms)
        object.__setattr__(self, "mapping_metadata", mapping_metadata)

    @property
    def n_qubits(self) -> int:
        """Number of qubits in every full-system Pauli word."""
        return self.terms[0].n_qubits

    @property
    def qubit_order(self) -> tuple[int, ...]:
        """Declared tensor-factor ordering shared by every term."""
        return self.terms[0].qubit_order or ()

    @property
    def lambda_norm(self) -> float:
        """Coefficient one-norm used by standard qDRIFT."""
        return float(sum(abs(term.coefficient) for term in self.terms))

    @property
    def sha256(self) -> str:
        """Stable hash of the canonical JSON representation."""
        encoded = (
            json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":")) + "\n"
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def dense_terms(self) -> tuple[NDArray[np.complex128], ...]:
        """Return coefficient-weighted dense terms for small-system validation."""
        return tuple(term.to_matrix() for term in self.terms)

    def to_matrix(self) -> NDArray[np.complex128]:
        """Return the complete dense Hamiltonian for reference calculations."""
        return np.sum(np.stack(self.dense_terms()), axis=0)

    def to_dict(self) -> dict[str, Any]:
        """Return the versioned JSON-compatible Hamiltonian contract."""
        payload: dict[str, Any] = {
            "schema_version": HAMILTONIAN_SCHEMA_VERSION,
            "id": self.identifier,
            "qubits": self.n_qubits,
            "qubit_order": list(self.qubit_order),
            "terms": [term.to_dict() for term in self.terms],
            "lambda": self.lambda_norm,
        }
        if self.source is not None:
            payload["source"] = self.source
        if self.units is not None:
            payload["units"] = self.units
        if self.mapping_metadata:
            payload["mapping_metadata"] = dict(self.mapping_metadata)
        return payload

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> PauliHamiltonian:
        """Construct a validated Hamiltonian from the versioned contract."""
        schema_version = payload.get("schema_version")
        if schema_version != HAMILTONIAN_SCHEMA_VERSION:
            raise ValueError(
                f"'schema_version' must be {HAMILTONIAN_SCHEMA_VERSION!r}."
            )
        terms = tuple(PauliTerm.from_dict(term) for term in payload["terms"])
        hamiltonian = cls(
            terms=terms,
            identifier=payload["id"],
            source=payload.get("source"),
            units=payload.get("units"),
            mapping_metadata=payload.get("mapping_metadata", {}),
        )
        if payload.get("qubits") != hamiltonian.n_qubits:
            raise ValueError("Declared 'qubits' does not match the Pauli terms.")
        if tuple(payload.get("qubit_order", ())) != hamiltonian.qubit_order:
            raise ValueError("Declared 'qubit_order' does not match the Pauli terms.")
        declared_lambda = payload.get("lambda")
        if declared_lambda is not None and not math.isclose(
            float(declared_lambda), hamiltonian.lambda_norm, rel_tol=0, abs_tol=1e-12
        ):
            raise ValueError("Declared 'lambda' does not match the coefficients.")
        return hamiltonian


HamiltonianInput = PauliHamiltonian | Sequence[NDArray[Any]]


def dense_terms(hamiltonian: HamiltonianInput) -> tuple[NDArray[np.complex128], ...]:
    """Normalize canonical or legacy dense input into validated dense terms."""
    if isinstance(hamiltonian, PauliHamiltonian):
        return hamiltonian.dense_terms()
    if isinstance(hamiltonian, (str, bytes)):
        raise TypeError("Hamiltonian input must be PauliHamiltonian or matrix terms.")

    terms = tuple(np.asarray(term, dtype=complex) for term in hamiltonian)
    if not terms:
        raise ValueError("At least one Hamiltonian term is required.")

    first = terms[0]
    if first.ndim != 2 or first.shape[0] != first.shape[1]:
        raise ValueError("Hamiltonian terms must be square matrices of same shape.")
    dimension = first.shape[0]
    n_qubits = int(np.log2(dimension)) if dimension else -1
    if dimension < 2 or 2**n_qubits != dimension:
        raise ValueError("Hamiltonian dimension must be a positive power of 2.")

    for term in terms:
        if term.ndim != 2 or term.shape != (dimension, dimension):
            raise ValueError("Hamiltonian terms must be square matrices of same shape.")
        if not np.all(np.isfinite(term)):
            raise ValueError("Hamiltonian terms must contain only finite values.")
        if not np.allclose(term, term.conj().T):
            raise ValueError("Hamiltonian terms must be Hermitian.")
    return terms


def term_labels(hamiltonian: HamiltonianInput) -> tuple[str, ...]:
    """Return stable labels for ordered Hamiltonian terms."""
    if isinstance(hamiltonian, PauliHamiltonian):
        return tuple(term.pauli_word for term in hamiltonian.terms)
    return tuple(str(index) for index, _ in enumerate(dense_terms(hamiltonian)))


def hamiltonian_provenance(hamiltonian: HamiltonianInput) -> dict[str, Any]:
    """Return JSON-compatible input provenance without embedding dense matrices."""
    if isinstance(hamiltonian, PauliHamiltonian):
        return {
            "representation": "pauli_sum",
            "id": hamiltonian.identifier,
            "sha256": hamiltonian.sha256,
            "qubits": hamiltonian.n_qubits,
            "terms": len(hamiltonian.terms),
            "lambda": hamiltonian.lambda_norm,
            "qubit_order": list(hamiltonian.qubit_order),
        }

    terms = dense_terms(hamiltonian)
    digest = hashlib.sha256()
    digest.update(len(terms).to_bytes(8, byteorder="little", signed=False))
    digest.update(terms[0].shape[0].to_bytes(8, byteorder="little", signed=False))
    for term in terms:
        digest.update(np.ascontiguousarray(term, dtype="<c16").tobytes())
    return {
        "representation": "dense_matrix_terms",
        "sha256": digest.hexdigest(),
        "qubits": int(np.log2(terms[0].shape[0])),
        "terms": len(terms),
    }


def _validate_json_metadata(value: Mapping[str, Any], field_name: str) -> None:
    try:
        json.dumps(value, sort_keys=True, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise TypeError(f"'{field_name}' must contain JSON-compatible values.") from exc
