# Quantum Chemistry Cautions

Quantum chemistry applications can expose failures that are not visible from generic product-formula scaling alone.

Low-order or poorly controlled Trotterization can affect chemical properties such as size consistency and orbital invariance. This is especially relevant for VQE-UCCSD and QPE full-CI workflows.

## Recommendation policy

For quantum chemistry tasks, do not recommend low-order Trotterization without checking:

- whether size consistency matters;
- whether orbital localization or orbital invariance matters;
- the molecular orbital convention;
- target accuracy;
- whether small-system exact benchmarking is feasible.

## Mitigation ideas

- Benchmark small fragments with `exact`.
- Sweep Trotter steps.
- Test decomposition and ordering choices.
- Record property constraints in the method recommendation.

## Key points

- `quantum-chemistry-trotter-cautions`
- `trotter-error-commutator-scaling`
