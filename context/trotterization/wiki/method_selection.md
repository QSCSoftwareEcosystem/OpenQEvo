# Method Selection

This page summarizes how the selection layer should use trotterization knowledge.

The authoritative selection policy is `../../selection/quantum_evolution_method_selection.md`. Machine-readable rules are in `../../selection/rules.json`.

## Executable recommendation shape

Executable recommendations must use a `method_name` accepted by `openqevo.get(name)`.

```json
{
  "method_name": "trotter_s2",
  "executable": true,
  "parameters": {
    "steps": 10
  }
}
```

The caller supplies `terms` and `t` at execution time. Planned methods should use `executable: false` and include a reason.

## Current recommendations

Use `exact` when the goal is classical benchmarking, reference evolution, or convergence checking and the full matrix is tractable.

Use `trotter_s1` when the user needs a shallow baseline, the Hamiltonian is local or sparse, and accuracy requirements are low to moderate.

Use `trotter_s2` when first-order error is unacceptable and the backend has enough depth budget.

Use low confidence for quantum chemistry recommendations involving size consistency, orbital invariance, VQE-UCCSD, or QPE full-CI until the task constraints and benchmarking plan are clear.

Flag interaction-picture or hybrid methods when direct Trotterization appears impractical, but separate literature suitability from current OpenQEvo native support.

For noisy hardware or noisy simulator execution, consider an error-mitigation wrapper such as planned `mitiq_zne` after selecting the base evolution method. Mitigation should not be used as a substitute for validating product-formula or decomposition error.

## Key points

- `trotter-error-commutator-scaling`
- `trotter-order-depth-tradeoff`
- `quantum-chemistry-trotter-cautions`
- `trotter-alternatives-and-hybrid-methods`
- `noisy-hardware-error-mitigation`
