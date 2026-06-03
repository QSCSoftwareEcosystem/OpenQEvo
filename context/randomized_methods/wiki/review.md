# Randomized Methods Review

## Review status

Initial codexA review finds the current randomized-method seed evidence sufficient for the present OpenQEvo recommendation scope:

- `qdrift-randomized-scaling` supports recommending executable `qdrift` as a randomized baseline for weighted, many-term Hamiltonians.
- `randomized-trotter-permutation-bounds` supports treating randomized/permuted product formulas as a literature-backed future method family.
- `randomized-methods-precision-tradeoffs` supports treating qSWIFT and stochastic sparsification as non-executable future-method evidence rather than executable recommendations.

## Source sufficiency

The current source set is enough for:

- qDRIFT selection as the only executable randomized method.
- Identifying randomized/permuted product formulas as a distinct future method family.
- Warning that sample count, stochastic variance, total Hamiltonian weight, and precision targets must be validated.
- Keeping qSWIFT and stochastic sparsification out of executable recommendation output until method metadata and software registration exist.

More raw sources may still be useful before claiming broad randomized-product-formula coverage across many Hamiltonian classes, but the collection now has direct first-party raw evidence for randomized/permuted product formulas.

## Review decision

For v0.1-style context, no additional source is required to keep qDRIFT as an executable randomized baseline. Randomized/permuted product formulas, qSWIFT, and stochastic sparsification now have seed raw evidence, but they should remain non-executable until OpenQEvo defines method metadata, parameter contracts, and software registration for each distinct method.
