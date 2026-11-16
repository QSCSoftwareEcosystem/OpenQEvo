# OpenQEvo Context Stack

OpenQEvo context is organized into three abstraction layers plus a persistent
wiki surface. The maintenance contract is defined in `wiki_manifest.json`.

## Layer 0: Raw evidence

Raw source material lives under domain-specific `raw_data/` directories, for example:

- `trotterization/raw_data/`
- `randomized_methods/raw_data/`
- `interaction_picture/raw_data/`
- `annealing/raw_data/`
- `software/raw_data/`

This layer contains converted paper markdown and provenance notes. It should preserve source content with minimal interpretation.
Converted paper markdown may retain PDF extraction artifacts such as two-column ordering, broken equations, and spacing noise. That is acceptable for Layer 0 when the core claims, terminology, tables, and provenance remain searchable. Human-readable synthesis belongs in Layer 1 key points and the wiki surface, not in `raw_data/`.

Software raw data stores converted or source-derived documentation for adapter
APIs and the OpenQEvo execution bridge. This lets AS/RAG tooling cite software
contracts directly instead of relying only on papers.

## Layer 1: Extracted knowledge

Key extracted concepts live under domain-specific `key_points/` directories, for example:

- `trotterization/key_points/`
- `randomized_methods/key_points/`
- `interaction_picture/key_points/`
- `annealing/key_points/`
- `software/key_points/`

This layer turns raw papers into compact, structured claims: concepts, applicability conditions, limitations, implications, related methods, and evidence links back to Layer 0.
Software key points turn raw API documentation into compact adapter and
execution-contract claims.

## Wiki surface

Human-readable synthesized wiki pages live under domain-specific `wiki/`
directories, for example:

- `trotterization/wiki/`
- `randomized_methods/wiki/`
- `interaction_picture/wiki/`
- `annealing/wiki/`
- `software/wiki/`

Wiki pages should cite Layer 1 key-point IDs as their evidence hooks. They
should not be treated as primary evidence.

## Layer 2: Method and selection logic

Method metadata lives in:

- `methods/`

Selection policy and recommendation rules live in:

- `selection/`

This layer uses method capability metadata and Layer 1 key points to decide which quantum evolution method to recommend for an application, Hamiltonian, backend, and user query.

Method metadata can include an `execution` block. For implemented methods,
`execution.method_name` is the registry key accepted by `openqevo.get(name)`.
For planned methods, `execution.implemented` must be `false` and the metadata
must include a `non_executable_reason`.

## Project boundary

OpenQEvo owns quantum state and time-evolution strategies: product formulas,
randomized evolution, interaction-picture evolution, annealing or adiabatic
evolution, and exact reference evolution.

OpenQEvo does not own full variational algorithm workflows such as VQE or
ADAPT-VQE. Those workflows may consume OpenQEvo evolution primitives, but
optimizer loops, ansatz growth, gradient measurement, and experiment
orchestration belong outside this project.

## Schemas

Schemas live in:

- `schema/method.schema.json`
- `schema/key_point.schema.json`
- `schema/selection_rule.schema.json`
- `schema/wiki_manifest.schema.json`

Method JSON files are loaded by the OpenQEvo registry from `methods/`.

## Collection discovery and evidence identity

[`wiki_manifest.json`](wiki_manifest.json) is the single collection registry.
Consumers discover available `raw_data`, `source_inventory`, `key_points`,
`wiki`, `summary`, and `selection_rules` paths from each entry rather than
hardcoding family names. `status: maintained` has the full structured chain;
`status: legacy_alias` delegates maintained claims to `canonical_collection`
and may omit key-point/wiki layers. The legacy `qdrift` directory routes to
`randomized_methods`; software contracts and `krylov_subspace` are registered
collections too. A collection is not necessarily an executable algorithm.

Each inventory labels local source identities, preferred conversion aliases,
known version differences, and unverified provenance. Multiple conversions
are preserved and must not be treated as independent scientific support.
`qdrift/raw_data` citation surveys are discovery indexes, not acquired papers.
Trotter `raw_data/tmp` is conversion scratch. New Krylov raw files are short
original primary-source evidence notes, explicitly naming the inspected
abstract/metadata surface; full-text acquisition is not claimed. Missing
acquisition dates, exact source versions, or expert review stay unknown.

The scope distinguishes classical dense references (`exact`, `krylov`, dense
interaction-picture/annealing propagation) from quantum circuits or quantum
subspace algorithms. Quantum Krylov basis preparation and projected-matrix
measurement are research context rather than registered `krylov` behavior.
LCU/qubitization, QSP, general time-dependent/open-system simulation, and
quantum imaginary-time algorithms lack equivalent curated evidence chains and
must not receive unsupported executable recommendations. The legacy term
"QIT-style" has no unique algorithm definition here: clarify whether the user
means imaginary time, interaction picture, or another task before selecting.

## Source knowledge base and installed subset

This source directory is the complete maintained knowledge base plus labeled
legacy/discovery material. The packaging build selects runtime metadata and
its local evidence dependencies into `openqevo/_context`; that selection does
not replace the source corpus or imply a right to redistribute every third-party
conversion. Existing license/release decisions cover redistribution review.
A passing JSON/path check proves structural consistency, not scientific
correctness, citation entailment, expert review, or ranking calibration.
