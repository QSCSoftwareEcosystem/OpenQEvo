# Trotterization Wiki

This wiki summarizes OpenQEvo's current knowledge about Trotter-Suzuki and product-formula quantum evolution methods.

For the broader OpenQEvo method-family scope, see [`../../evolution_strategy_families.md`](../../evolution_strategy_families.md).

## Pages

- [Product formulas](product_formulas.md)
- [Error scaling](error_scaling.md)
- [Hamiltonian partitioning](hamiltonian_partitioning.md)
- [Quantum chemistry cautions](quantum_chemistry_cautions.md)
- [Method selection](method_selection.md)
- [Open questions](open_questions.md)
- [Changelog](changelog.md)

## Evidence model

Wiki pages are synthesized from key points, not directly from papers. Key points link back to raw converted paper markdown.

Current key-point IDs:

- `trotter-error-commutator-scaling`
- `trotter-order-depth-tradeoff`
- `quantum-chemistry-trotter-cautions`
- `trotter-alternatives-and-hybrid-methods`

## Maintenance rule

When new papers are added, update the evidence chain in this order:

1. Add converted markdown to `../raw_data/`.
2. Add or update structured key points in `../key_points/`.
3. Update these wiki pages from the key points.
4. Update `../../selection/rules.json` only when method recommendations change.
