# Quantum Evolution Method Selection

This file defines how OpenQEvo should recommend an evolution method from a user query, application goal, Hamiltonian structure, and backend constraints.

## Evidence chain

Recommendations must use the three-layer context stack:

1. Raw evidence: paper markdown in method-family `raw_data/` directories.
2. Extracted knowledge: compact key points in method-family `key_points/` directories.
3. Method selection: method capability metadata in `../methods/` and rules in `rules.json`.

Selection rules should cite key-point IDs instead of citing papers directly. Key points carry the raw evidence links.

## Input classes

### HamiltonianProfile

Describes the Hamiltonian to be evolved.

Fields:

- `representation`: matrix, Pauli sum, sparse operator, fermionic second quantized, bosonic model, lattice model, or unknown.
- `num_qubits`: known qubit count, if available.
- `num_terms`: number of terms after decomposition, if available.
- `locality`: local, nearest-neighbor, sparse non-local, dense non-local, or unknown.
- `commutation_structure`: commuting groups known, mostly commuting, strongly non-commuting, or unknown.
- `time_dependence`: time independent, time dependent, or unknown.
- `domain`: quantum chemistry, lattice dynamics, benchmarking, algorithm development, or unknown.

### EvolutionTask

Describes the user objective.

Fields:

- `goal`: benchmark, production simulation, ansatz evolution block construction, QPE time evolution, convergence study, annealing schedule evolution, or exploratory.
- `accuracy_target`: exact/reference, high, moderate, low, or unknown.
- `time_horizon`: short, moderate, long, or unknown.
- `backend`: classical simulator, ideal quantum simulator, noisy simulator, hardware, or unknown.
- `depth_budget`: strict, moderate, relaxed, or unknown.
- `property_constraints`: size consistency, orbital invariance, symmetry preservation, noise robustness, or none specified.

### MethodRecommendation

Describes the output.

Fields:

- `method`: OpenQEvo method name, such as `exact`, `trotter_s1`, or `trotter_s2`.
- `confidence`: high, medium, or low.
- `parameters`: suggested parameter values or ranges.
- `rationale`: short reasons linked to key-point IDs.
- `questions`: missing inputs that materially affect the choice.
- `warnings`: known risks or limitations.

Executable recommendations should include this minimal payload:

```json
{
  "method_name": "trotter_s2",
  "executable": true,
  "terms": "<provided by caller>",
  "t": "<provided by caller>",
  "parameters": {
    "steps": 10
  }
}
```

If a recommendation is theoretically suitable but not implemented, set
`executable` to `false` and include `non_executable_reason`. Do not emit a
planned method as an executable call.

## OpenQEvo scope

OpenQEvo recommends and implements quantum state/time-evolution strategies and
primitives. In scope families include product formulas, randomized evolution
such as qDRIFT, interaction-picture or QIT-style evolution, annealing or
adiabatic evolution, and exact reference evolution.

Full variational workflows such as VQE and ADAPT-VQE are external consumers,
not OpenQEvo-owned methods. If a user asks about VQE, interpret the OpenQEvo
task as selecting an evolution primitive or ansatz evolution block, not running
the optimization workflow.

## Decision policy

Use `exact` for small classical reference problems, validation, and convergence studies when the matrix size is tractable. Do not present it as a quantum algorithm.

Use `trotter_s1` for shallow baseline circuits, exploratory runs, local or sparse Hamiltonians, and cases where low depth matters more than high precision.

Use `trotter_s2` when the task needs better accuracy than first order and the backend has enough depth budget for the symmetric formula.

For quantum chemistry tasks involving VQE-UCCSD, QPE full-CI, size consistency, or orbital invariance, do not recommend low-order Trotterization without warnings and benchmarking guidance.

When commutation structure is unknown, recommend profiling the Hamiltonian terms or benchmarking against `exact` for small instances before choosing final Trotter steps.

When the Hamiltonian is time dependent, has a dominant exactly simulable component, or direct Trotter depth is impractical, flag interaction-picture or hybrid methods as literature-supported alternatives even if they are not yet native OpenQEvo methods.

When the user asks for qDRIFT, randomized evolution, QIT, interaction-picture
evolution, or annealing, separate scope suitability from implementation
availability. These families are in OpenQEvo scope, but method metadata should
not claim native support until implementation and tests exist.

When the backend is noisy hardware or a noisy simulator, recommend error
mitigation as an optional wrapper around the selected base evolution method.
`mitiq_zne` is planned metadata for Mitiq-backed zero-noise extrapolation; it
should not be treated as a standalone evolution strategy until a compatible
adapter implementation exists.

## Execution bridge

The context layer selects and explains methods. The software execution bridge
should use `method_name` as the registry key accepted by `openqevo.get(name)`.

For v0.1.0, the executable call shape is:

```python
openqevo.get(method_name).evolve(terms, t, **parameters)
```

Hamiltonian profiles guide selection only. They should not be required by the
execution helper. Backend-specific payloads and serialized circuits should stay
outside the core execution helper until adapters expose a stable contract.

## Minimum questions before a high-confidence recommendation

Ask for missing values only when they materially change the method choice:

- Hamiltonian representation and size.
- Accuracy target or acceptable error.
- Backend and depth/noise constraints.
- Whether the task is benchmarking, QPE, annealing, ansatz-block construction, or production simulation.
- Whether quantum chemistry invariants such as size consistency matter.
