# Scientific contracts

OpenQEvo separates the scientific input, execution metadata, and compatibility
output into two versioned contracts:

- `PauliHamiltonian` is the canonical input used by native methods, adapters,
  and benchmarks.
- `EvolutionResult` carries the output representation, normalized parameters,
  implementation provenance, costs, seeds, sampled sequences, environment,
  warnings, and limitations.

The corresponding JSON schemas are
`context/schema/hamiltonian.schema.json` and
`context/schema/evolution_result.schema.json`.

## Canonical Pauli Hamiltonians

```python
import openqevo

hamiltonian = openqevo.PauliHamiltonian(
    identifier="example-xz",
    source="example",
    terms=(
        openqevo.PauliTerm(1.0, "X", source="example"),
        openqevo.PauliTerm(1.0, "Z", source="example"),
    ),
)
```

Coefficients are finite, real, and nonzero. Every word is a full-system word
over `I`, `X`, `Y`, and `Z`; all terms use the same qubit count and explicit
tensor-factor order. Duplicate words are rejected so cost and ordering
semantics remain unambiguous. `lambda_norm` is the coefficient one-norm used
by standard qDRIFT.

`hamiltonian.to_dict()` produces the versioned machine-readable payload.
`PauliHamiltonian.from_dict(...)` validates and reconstructs it. Dense matrix
terms remain accepted by every method as a small-system compatibility path.

## Structured execution

```python
result = openqevo.get("trotter_s2").run(
    hamiltonian,
    t=1.0,
    steps=20,
)

unitary = result.unitary
metadata = result.to_metadata()
print(result.costs.formula_level_pauli_operations)
```

`run(...)` is the provenance-aware API. `evolve(...)` still returns the dense
unitary directly for existing callers. Native implementations currently emit
dense validation unitaries; the result contract can also describe state,
circuit, operation-sequence, and channel outputs as those execution modes are
implemented.

For qDRIFT, `run(...)` records the seed and complete sampled term sequence.
`run_ensemble(...)` returns the exact expected channel in dense Liouville form
for small-system analytic controls. It is distinct from a finite empirical
trajectory ensemble and is not a scalable output mode.

## Agentic Software boundary

Serialized canonical Hamiltonians can be embedded in executable recommendation
payloads. Agentic Software may request the structured result without taking
ownership of method execution:

```python
result = openqevo.execute_recommendation(
    {
        "method_name": "qdrift",
        "terms": hamiltonian.to_dict(),
        "t": 1.0,
        "parameters": {"samples": 100, "seed": 7},
    },
    structured=True,
)
```

Retrieval, ranking, clarification, and orchestration remain outside OpenQEvo.
The stable integration boundary is the versioned input schema, method metadata,
recommendation schema, and structured result metadata.
