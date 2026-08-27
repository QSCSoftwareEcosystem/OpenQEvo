# Evolution Strategy Families

OpenQEvo is organized around quantum state and time-evolution strategies.

## Implemented or partially implemented

| Family | Context collection | Current method metadata |
| :--- | :--- | :--- |
| Product formulas / Trotter-Suzuki | `trotterization/` | `methods/trotter_s1.json`, `methods/trotter_s2.json` |
| Randomized evolution | `randomized_methods/` | `methods/qdrift.json` |
| Exact reference evolution | `methods/` | `methods/exact.json` |
| Error mitigation wrappers | `methods/` | `methods/mitiq_zne.json` planned metadata; not a standalone evolution strategy |

## Planned families

| Family | Context collection | Notes |
| :--- | :--- | :--- |
| Interaction-picture / QIT-style evolution | `interaction_picture/` | Evolution strategies that separate dominant or exactly simulable Hamiltonian components. |
| Annealing / adiabatic evolution | `annealing/` | Schedule-based Hamiltonian evolution primitives. |

## Out of core scope

Full variational workflows are not OpenQEvo methods:

- VQE
- ADAPT-VQE
- optimizer loops
- ansatz growth workflows
- measurement and gradient orchestration

Those workflows may call OpenQEvo primitives, but OpenQEvo owns the evolution
strategy, not the full algorithm workflow.
