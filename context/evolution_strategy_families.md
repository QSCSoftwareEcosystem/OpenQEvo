# Evolution Strategy Families

OpenQEvo's specialist knowledge base covers quantum state and time-evolution
strategies. Literature coverage, executable software, output representation,
and scientific approval are separate properties. Classical references provide
numerical controls for studying quantum algorithms.

## Current knowledge and software boundaries

| Family | Context collection | Available software and limits |
| :--- | :--- | :--- |
| Product formulas / Trotter–Suzuki | `trotterization/` | `methods/trotter_s1.json`, `methods/trotter_s2.json`: dense references, logical operations, and reference circuits; scientific approval pending. |
| Randomized evolution | `randomized_methods/` | `methods/qdrift.json`: seeded dense trajectories, logical operations/reference circuits, and small-system channel controls; scientific approval pending. Other randomized strategies remain literature-supported candidates. |
| Exact reference evolution | `methods/` | `methods/exact.json`: classical dense matrix exponentiation for validation. |
| Krylov subspace strategies | `krylov_subspace/` | `methods/krylov.json`: experimental classical dense Lanczos propagation. Quantum Krylov state preparation and measurement workflows in the literature are distinct capabilities. |
| Interaction-picture evolution | `interaction_picture/` | `methods/interaction_picture.json`: experimental dense midpoint reference; supports reference-term indices or a separately supplied dominant Hamiltonian. No interaction-picture circuit/oracle/resource model. |
| Annealing / adiabatic evolution | `annealing/` | `methods/annealing.json`: experimental dense linear-schedule reference with optional driver; `methods/adiabatic_evolution.json`: dense explicit-initial-terms reference with linear/power schedules. Neither supplies an analog device, optimized schedule, or ground-state-preparation guarantee. |
| Error mitigation wrappers | `software/`, `methods/` | `methods/mitiq_zne.json`: planned non-executable wrapper metadata, rather than an independent evolution strategy. |

The [annealing wiki](annealing/wiki/index.md) explains the two schedule APIs;
the [interaction-picture wiki](interaction_picture/wiki/index.md) describes
split semantics. Metadata and source implementations establish software
availability. Scientific sources and reviewer decisions establish which claims
about quantum algorithms and applicability can be justified. Neither
availability nor a metadata `source` label constitutes scientific approval.

## Candidate extensions

Hardware-aware compilation, interaction-picture circuits, LCU/qubitization,
sparse/distributed Krylov solvers, quantum Krylov measurement workflows,
advanced schedules, and resource models require their own reviewed evidence
and contracts. Discussing one of these in the corpus does not register a
method or demonstrate quantum hardware execution.

## Out of core scope

Full variational/optimization workflows remain external consumers:

- VQE and ADAPT-VQE optimizer loops;
- ansatz growth and gradient orchestration;
- full annealing optimization, measurement, and readout workflows.

Those workflows may consume OpenQEvo evolution primitives. The knowledge base
can discuss their evolution requirements without claiming ownership of the
entire workflow.
