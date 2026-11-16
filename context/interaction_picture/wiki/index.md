# Interaction-Picture Evolution

This collection covers quantum Hamiltonian-simulation strategies that split
`H = H0 + V` and work in the interaction picture of `H0`. Its scientific
principles are captured by `interaction-picture-split-hamiltonian`: useful
quantum resource trade-offs require an appropriate split and a cheaply
implementable reference evolution. The source literature also considers
hybrid and time-dependent simulation machinery.

## Current OpenQEvo capability

`interaction_picture` is an implemented **experimental dense classical
reference** for a time-independent input Hamiltonian. It uses midpoint
integration of the residual in the interaction frame, then transforms back.
It returns a dense unitary; `run(...)` adds structured result metadata.

The current API offers two split conventions:

- With `terms` containing the full Hamiltonian, provide
  `reference_term_indices` to select `H0`. By default canonical Pauli input
  uses all diagonal I/Z terms, falling back to the first term if none exist;
  dense input defaults to its first term.
- With separately supplied `dominant_terms` representing `H0`, `terms`
  represents `V`. This convention evolves their sum. It cannot be combined
  with `reference_term_indices`. The structured result records both input
  and reference provenance, identifying the `H0 + V` interpretation.

Both conventions require `steps` and evolution time `t`; increase steps to
assess convergence. A product-formula `order` argument is unsupported. The
automatic split is a numerical convenience whose suitability must be checked.

See the [method contract](../../methods/interaction_picture.json) and
[current implementation](../../../src/openqevo/methods/advanced.py). These
are engineering evidence for availability; scientific sources below support
the algorithmic principles.

## Scientific and implementation boundaries

The dense reference does not supply an interaction-picture circuit, LCU/oracle
implementation, hardware execution, or an asymptotic resource estimate.
Time dependence induced by the interaction frame does not make the input API
an arbitrary time-dependent Hamiltonian solver. Quantum algorithmic advantages
in the literature do not transfer automatically to this dense implementation.
Scientific review and claim-level applicability checks remain pending.

This collection uses “interaction picture” for the split-Hamiltonian strategy.
Quantum imaginary-time state preparation is a different subject; the earlier
undefined “QIT-style” label is not an executable capability claim.

## Evidence and navigation

- Key point: `interaction-picture-split-hamiltonian`,
  [structured concept](../key_points/interaction_picture_split_hamiltonian.json).
- [Source inventory](../source_inventory.md): Low–Wiebe seed source and the
  related Rajput hybrid-method source in the Trotter collection.
- Related concept: `trotter-alternatives-and-hybrid-methods`,
  [structured concept](../../trotterization/key_points/trotter_alternatives_and_hybrid_methods.json).

The raw papers are primary evidence; this wiki is synthesis and current
implementation guidance, with no recorded expert scientific approval.
