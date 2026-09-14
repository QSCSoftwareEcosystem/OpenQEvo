# Evolution Strategy Families

OpenQEvo is organized around quantum state and time-evolution strategies.

## Implemented or partially implemented

| Family | Context collection | Current method metadata |
| :--- | :--- | :--- |
| Product formulas / Trotter-Suzuki | `trotterization/` | `methods/trotter_s1.json`, `methods/trotter_s2.json` |
| Randomized evolution | `randomized_methods/` | `methods/qdrift.json` |
| Exact reference evolution | `methods/` | `methods/exact.json` |
| Krylov subspace evolution | `krylov_subspace/` | `methods/krylov.json`; experimental dense Lanczos reference |
| Interaction-picture evolution | `interaction_picture/` | `methods/interaction_picture.json`; experimental dense midpoint reference |
| Annealing / adiabatic evolution | `annealing/` | `methods/annealing.json`; experimental linear-schedule dense reference |
| Error mitigation wrappers | `methods/` | `methods/mitiq_zne.json` planned metadata; not a standalone evolution strategy |

## Planned families

| Family | Context collection | Notes |
| :--- | :--- | :--- |
| Hardware-aware and scalable variants | `interaction_picture/`, `annealing/`, `krylov_subspace/` | Circuit synthesis, sparse/distributed solvers, advanced schedules, and resource models remain separate work. |

## Out of core scope

Full variational workflows are not OpenQEvo methods:

- VQE
- ADAPT-VQE
- optimizer loops
- ansatz growth workflows
- measurement and gradient orchestration

Those workflows may call OpenQEvo primitives, but OpenQEvo owns the evolution
strategy, not the full algorithm workflow.
