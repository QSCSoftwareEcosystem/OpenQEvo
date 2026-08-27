# Product Formulas

Product formulas approximate time evolution under a decomposed Hamiltonian by applying simpler term evolutions in sequence.

For a Hamiltonian split into terms, first-order Trotterization gives the shallowest product formula currently represented in OpenQEvo. Second-order symmetric Trotterization increases per-step depth but cancels lower-order error terms.

## OpenQEvo methods

- `trotter_s1`: first-order product formula.
- `trotter_s2`: second-order symmetric product formula.
- `exact`: classical reference evolution, not a scalable quantum algorithm.

## Practical implication

Use first-order formulas for shallow baselines or exploratory runs. Use second-order formulas when first-order error is too large and the depth budget allows more gates per step.

## Key points

- `trotter-order-depth-tradeoff`
- `trotter-error-commutator-scaling`
