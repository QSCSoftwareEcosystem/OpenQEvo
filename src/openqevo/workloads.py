"""Controlled Hamiltonian families for conformance and publication studies."""

from __future__ import annotations

import itertools
import math
from collections.abc import Sequence

import numpy as np

from openqevo.hamiltonian import PauliHamiltonian, PauliTerm


def pauli_words_commute(left: str, right: str) -> bool:
    """Return whether two full-system Pauli words commute."""
    if len(left) != len(right):
        raise ValueError("Pauli words must have the same length.")
    if any(label not in "IXYZ" for label in left + right):
        raise ValueError("Pauli words may contain only I, X, Y, and Z.")
    anticommuting_positions = sum(
        a != "I" and b != "I" and a != b for a, b in zip(left, right)
    )
    return anticommuting_positions % 2 == 0


def commutator_graph_density(hamiltonian: PauliHamiltonian) -> float:
    """Fraction of unordered term pairs whose Pauli words anticommute."""
    words = [term.pauli_word for term in hamiltonian.terms]
    pairs = list(itertools.combinations(words, 2))
    if not pairs:
        return 0.0
    edges = sum(not pauli_words_commute(left, right) for left, right in pairs)
    return float(edges / len(pairs))


def controlled_pauli_hamiltonian(
    *,
    n_qubits: int,
    term_count: int,
    lambda_norm: float,
    pauli_weight: int,
    commutator_structure: str,
    coefficient_distribution: str,
    seed: int,
    identifier: str | None = None,
) -> PauliHamiltonian:
    """Generate a deterministic Pauli workload with independently set controls.

    ``commutator_structure`` accepts ``commuting``, ``mixed``, or ``dense``.
    The latter two are greedy selections whose realized graph density is stored
    in metadata rather than silently promising an unattainable exact density.
    """
    if isinstance(n_qubits, bool) or not isinstance(n_qubits, int) or n_qubits < 1:
        raise ValueError("'n_qubits' must be a positive integer.")
    if (
        isinstance(pauli_weight, bool)
        or not isinstance(pauli_weight, int)
        or not 1 <= pauli_weight <= n_qubits
    ):
        raise ValueError("'pauli_weight' must be between 1 and n_qubits.")
    if (
        isinstance(term_count, bool)
        or not isinstance(term_count, int)
        or term_count < 1
    ):
        raise ValueError("'term_count' must be a positive integer.")
    if not math.isfinite(lambda_norm) or lambda_norm <= 0:
        raise ValueError("'lambda_norm' must be positive and finite.")
    if commutator_structure not in {"commuting", "mixed", "dense"}:
        raise ValueError(
            "'commutator_structure' must be 'commuting', 'mixed', or 'dense'."
        )
    if coefficient_distribution not in {"uniform", "skewed"}:
        raise ValueError("'coefficient_distribution' must be 'uniform' or 'skewed'.")
    if isinstance(seed, bool) or not isinstance(seed, int) or seed < 0:
        raise ValueError("'seed' must be a non-negative integer.")

    rng = np.random.default_rng(seed)
    candidates = _words_of_weight(n_qubits, pauli_weight)
    if commutator_structure == "commuting":
        candidates = [word for word in candidates if set(word) <= {"I", "Z"}]
        rng.shuffle(candidates)
        selected = candidates[:term_count]
    else:
        rng.shuffle(candidates)
        selected = _select_by_density(
            candidates,
            term_count=term_count,
            target=1.0 if commutator_structure == "dense" else 0.5,
        )
    if len(selected) != term_count:
        available = (
            len(selected) if commutator_structure == "commuting" else len(candidates)
        )
        raise ValueError(
            f"Requested {term_count} terms, but only {available} satisfy the controls."
        )

    if coefficient_distribution == "uniform":
        magnitudes = np.ones(term_count, dtype=float)
    else:
        magnitudes = np.geomspace(1.0, 0.1, term_count, dtype=float)
    magnitudes *= float(lambda_norm) / float(np.sum(magnitudes))
    signs = np.where(np.arange(term_count) % 2 == 0, 1.0, -1.0)
    coefficients = magnitudes * signs
    workload_id = identifier or (
        f"controlled-q{n_qubits}-l{term_count}-w{pauli_weight}-"
        f"{commutator_structure}-{coefficient_distribution}-s{seed}"
    )
    hamiltonian = PauliHamiltonian(
        identifier=workload_id,
        source="openqevo-controlled-generator/v1",
        terms=tuple(
            PauliTerm(coefficient=float(coefficient), pauli_word=word)
            for coefficient, word in zip(coefficients, selected)
        ),
        mapping_metadata={
            "family": "controlled_pauli",
            "generator_version": "v1",
            "seed": seed,
            "requested_commutator_structure": commutator_structure,
            "coefficient_distribution": coefficient_distribution,
            "pauli_weight": pauli_weight,
        },
    )
    metadata = dict(hamiltonian.mapping_metadata)
    metadata["commutator_graph_density"] = commutator_graph_density(hamiltonian)
    return PauliHamiltonian(
        terms=hamiltonian.terms,
        identifier=hamiltonian.identifier,
        source=hamiltonian.source,
        mapping_metadata=metadata,
    )


def transverse_field_ising(
    n_qubits: int,
    *,
    coupling: float = 1.0,
    field: float = 0.7,
    periodic: bool = False,
) -> PauliHamiltonian:
    """Return an open or periodic transverse-field Ising chain."""
    _validate_chain(n_qubits, coupling, field)
    edges = _chain_edges(n_qubits, periodic)
    terms = [PauliTerm(coupling, _two_site_word(n_qubits, edge, "Z")) for edge in edges]
    terms.extend(
        PauliTerm(field, _one_site_word(n_qubits, qubit, "X"))
        for qubit in range(n_qubits)
    )
    return _spin_hamiltonian(
        terms,
        identifier=f"tfim-q{n_qubits}-{'periodic' if periodic else 'open'}",
        family="transverse_field_ising",
        parameters={
            "coupling": float(coupling),
            "field": float(field),
            "periodic": periodic,
        },
    )


def heisenberg_chain(
    n_qubits: int,
    *,
    coupling: float = 1.0,
    field: float = 0.3,
    periodic: bool = False,
) -> PauliHamiltonian:
    """Return an isotropic Heisenberg chain with a longitudinal field."""
    _validate_chain(n_qubits, coupling, field)
    terms = [
        PauliTerm(coupling, _two_site_word(n_qubits, edge, label))
        for edge in _chain_edges(n_qubits, periodic)
        for label in "XYZ"
    ]
    if field != 0:
        terms.extend(
            PauliTerm(field, _one_site_word(n_qubits, qubit, "Z"))
            for qubit in range(n_qubits)
        )
    return _spin_hamiltonian(
        terms,
        identifier=f"heisenberg-q{n_qubits}-{'periodic' if periodic else 'open'}",
        family="heisenberg",
        parameters={
            "coupling": float(coupling),
            "field": float(field),
            "periodic": periodic,
        },
    )


def h2_two_qubit() -> PauliHamiltonian:
    """Return the archived two-qubit H2 operator used in IBM tutorials.

    This is a fixed mapped workload, not an ab-initio chemistry calculation.
    Its provenance intentionally does not infer geometry or mapping choices not
    stated alongside the archived coefficients.
    """
    coefficients = (
        (-1.052373245772859, "II"),
        (0.39793742484318045, "IZ"),
        (-0.39793742484318045, "ZI"),
        (-0.01128010425623538, "ZZ"),
        (0.18093119978423156, "XX"),
    )
    return PauliHamiltonian(
        identifier="h2-ibm-tutorial-two-qubit",
        source="IBM Quantum tutorial archived two-qubit H2 operator",
        units="hartree",
        terms=tuple(
            PauliTerm(value, word, units="hartree") for value, word in coefficients
        ),
        mapping_metadata={
            "family": "chemistry_archived_operator",
            "molecule": "H2",
            "provenance_url": (
                "https://qiskit.qotlabs.org/learning/courses/"
                "variational-algorithm-design/examples-and-applications"
            ),
            "scope_note": (
                "Fixed tutorial coefficients; OpenQEvo does not claim to regenerate "
                "the electronic-structure mapping."
            ),
        },
    )


def _words_of_weight(n_qubits: int, weight: int) -> list[str]:
    words = []
    for active in itertools.combinations(range(n_qubits), weight):
        for labels in itertools.product("XYZ", repeat=weight):
            word = ["I"] * n_qubits
            for qubit, label in zip(active, labels):
                word[qubit] = label
            words.append("".join(word))
    return words


def _select_by_density(
    candidates: Sequence[str], *, term_count: int, target: float
) -> list[str]:
    selected: list[str] = []
    remaining = list(candidates)
    while remaining and len(selected) < term_count:
        if not selected:
            selected.append(remaining.pop())
            continue
        best_index = min(
            range(len(remaining)),
            key=lambda index: (
                abs(_density_after(selected, remaining[index]) - target),
                remaining[index],
            ),
        )
        selected.append(remaining.pop(best_index))
    return selected


def _density_after(selected: Sequence[str], candidate: str) -> float:
    words = [*selected, candidate]
    pairs = list(itertools.combinations(words, 2))
    return sum(not pauli_words_commute(*pair) for pair in pairs) / len(pairs)


def _validate_chain(n_qubits: int, coupling: float, field: float) -> None:
    if isinstance(n_qubits, bool) or not isinstance(n_qubits, int) or n_qubits < 2:
        raise ValueError("A spin chain requires at least two qubits.")
    if not all(math.isfinite(float(value)) for value in (coupling, field)):
        raise ValueError("Spin-model coefficients must be finite.")
    if coupling == 0:
        raise ValueError("'coupling' must be non-zero.")


def _chain_edges(n_qubits: int, periodic: bool) -> list[tuple[int, int]]:
    edges = [(qubit, qubit + 1) for qubit in range(n_qubits - 1)]
    if periodic and n_qubits > 2:
        edges.append((n_qubits - 1, 0))
    return edges


def _one_site_word(n_qubits: int, qubit: int, label: str) -> str:
    word = ["I"] * n_qubits
    word[qubit] = label
    return "".join(word)


def _two_site_word(n_qubits: int, edge: tuple[int, int], label: str) -> str:
    word = ["I"] * n_qubits
    for qubit in edge:
        word[qubit] = label
    return "".join(word)


def _spin_hamiltonian(
    terms: Sequence[PauliTerm],
    *,
    identifier: str,
    family: str,
    parameters: dict[str, float | bool],
) -> PauliHamiltonian:
    hamiltonian = PauliHamiltonian(
        terms=tuple(terms),
        identifier=identifier,
        source="openqevo-spin-model/v1",
        mapping_metadata={"family": family, "parameters": parameters},
    )
    metadata = dict(hamiltonian.mapping_metadata)
    metadata["commutator_graph_density"] = commutator_graph_density(hamiltonian)
    return PauliHamiltonian(
        terms=hamiltonian.terms,
        identifier=hamiltonian.identifier,
        source=hamiltonian.source,
        mapping_metadata=metadata,
    )
