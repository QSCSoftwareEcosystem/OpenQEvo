# OpenQEvo Context Stack

OpenQEvo context is organized into three abstraction layers plus a persistent
wiki surface. The maintenance contract is defined in `wiki_manifest.json`.

## Layer 0: Raw evidence

Raw source material lives under domain-specific `raw_data/` directories, for example:

- `trotterization/raw_data/`
- `randomized_methods/raw_data/`
- `interaction_picture/raw_data/`
- `annealing/raw_data/`

This layer contains converted paper markdown and provenance notes. It should preserve source content with minimal interpretation.
Converted paper markdown may retain PDF extraction artifacts such as two-column ordering, broken equations, and spacing noise. That is acceptable for Layer 0 when the core claims, terminology, tables, and provenance remain searchable. Human-readable synthesis belongs in Layer 1 key points and the wiki surface, not in `raw_data/`.

## Layer 1: Extracted knowledge

Key extracted concepts live under domain-specific `key_points/` directories, for example:

- `trotterization/key_points/`
- `randomized_methods/key_points/`
- `interaction_picture/key_points/`
- `annealing/key_points/`

This layer turns raw papers into compact, structured claims: concepts, applicability conditions, limitations, implications, related methods, and evidence links back to Layer 0.

## Wiki surface

Human-readable synthesized wiki pages live under domain-specific `wiki/`
directories, for example:

- `trotterization/wiki/`
- `randomized_methods/wiki/`
- `interaction_picture/wiki/`
- `annealing/wiki/`

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
