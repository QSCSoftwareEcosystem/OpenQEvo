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
unitary directly for existing callers. Canonical Pauli inputs accept
`representation="unitary"`, `"operations"`, or `"circuit"` for native Trotter
and qDRIFT runs. Operation sequences preserve the explicit
`exp(-i * coefficient * time * P)` convention. Reference circuits use the
fixed logical `H/S/Sdg/RZ/CX` basis and report compiled one-qubit gates,
two-qubit gates, and ASAP depth. They assume all-to-all logical connectivity;
hardware routing is deliberately outside this cost contract.

```python
operations = openqevo.get("trotter_s2").run(
    hamiltonian, t=1.0, steps=20, representation="operations"
)
circuit = openqevo.get("trotter_s2").run(
    hamiltonian, t=1.0, steps=20, representation="circuit"
)

print(operations.output.to_dict())
print(circuit.costs.compiled_two_qubit_gates)
```

For qDRIFT, `run(...)` records the seed and complete sampled term sequence.
`run_ensemble(...)` returns the exact expected channel in dense Liouville form
for small-system analytic controls. It is distinct from a finite empirical
trajectory ensemble and is not a scalable output mode.

## Cross-framework convention contract

OpenQEvo's target is `U(t) = exp(-i H t)`, with Pauli rotation angle
`2 * coefficient * time`. Pauli word position zero denotes logical qubit zero,
which is the most-significant tensor factor in dense matrices. Serialized terms
execute in their declared order.

The Qiskit adapter maps logical wires to preserve this dense convention and
forces product-formula synthesis before unitary extraction. PennyLane's
`TrotterProduct` uses `exp(+i H t)`, so the adapter negates time; its
first-order term input is reversed to preserve OpenQEvo's execution order.
`openqevo.conformance` stores the complete machine-readable convention and
analytic cases used by the shared suite.

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
