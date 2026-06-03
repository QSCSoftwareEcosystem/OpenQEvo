# Hamiltonian Partitioning

Hamiltonian partitioning affects both circuit cost and Trotter error. The same Hamiltonian can lead to different practical performance depending on term grouping, ordering, and available structure.

## Useful structure

- Locality or nearest-neighbor structure.
- Sparse term decompositions.
- Known commuting groups.
- Dominant terms that can be handled separately.
- Symmetries that reduce the effective circuit.

## OpenQEvo implication

Current native method metadata supports `exact`, `trotter_s1`, and `trotter_s2`. If direct Trotterization becomes too deep, the selection layer should mark alternatives as literature-supported but not yet native unless implementation support exists.

## Key points

- `trotter-error-commutator-scaling`
- `trotter-alternatives-and-hybrid-methods`
