# Architecture

openQEvo uses a **Strategy + Registry + Adapter** pattern to keep the
codebase modular. Every evolution method — whether native code from the
Algorithms Thrust or a wrapper around an external library — implements the
same `EvolutionMethod` interface and self-registers with the registry.

## Overview

```mermaid
flowchart TB
    subgraph INPUT ["Algorithms Thrust (Source)"]
        A1["Research script\n(e.g. trotterization.py)"]
        A2["Future methods\n(QDrift, LCU, QSVT, ...)"]
    end

    subgraph OPENQEVO ["openQEvo (Software Thrust)"]
        direction TB

        subgraph CORE ["Core Architecture"]
            B0["hamiltonian.py\nPauliTerm / PauliHamiltonian\ncanonical input + dense bridge"]
            B1["base.py\nEvolutionMethod protocol"]
            B2["registry.py\n@register decorator\nget() / list_methods()"]
            B3["result.py\nEvolutionResult\nprovenance + costs"]
            B4["operations.py\noperation sequences\nreference compiler"]
        end

        subgraph METHODS ["methods/"]
            M1["trotter.py\nTrotterFirstOrder\nTrotterSecondOrder\nExactEvolution"]
            M2["future_method.py\n(same pattern)"]
        end

        subgraph ADAPTERS ["adapters/"]
            AD1["qiskit_adapter.py"]
            AD2["pennylane_adapter.py"]
            AD3["qrack_adapter.py"]
        end

        subgraph CONTEXT ["context/"]
            C1["methods/\ntrotter_s1.json\ntrotter_s2.json"]
            C2["trotterization/key_points/\nselection/rules.json"]
        end

        subgraph QUALITY ["SE Layer"]
            Q1["pyproject.toml"]
            Q2["tests/"]
            Q3["CI/CD"]
            Q4["docs/"]
        end
    end

    subgraph CONSUMERS ["Consumers"]
        U1["Researchers\npip install openqevo"]
        U2["HPC Users\nspack install openqevo"]
        U3["AI Agents\nMCP / RAG"]
        U4["Other Thrusts\nApplications, Validation"]
    end

    A1 -->|"Integrate &\nengineer"| M1
    A2 -.->|"Future"| M2
    B0 --- B1
    B1 --- B2
    B1 --- B3
    B1 --- B4
    B2 --- M1
    B2 --- M2
    B2 --- AD1
    B2 --- AD2
    B2 --- AD3
    M1 --- C1
    C1 --- C2
    OPENQEVO --> U1
    OPENQEVO --> U2
    OPENQEVO --> U3
    OPENQEVO --> U4

    style INPUT fill:#4a90d9,color:#fff
    style OPENQEVO fill:#f5f5f5,color:#333
    style CONSUMERS fill:#2ecc71,color:#fff
    style CORE fill:#fff3cd,color:#333
    style METHODS fill:#d4edda,color:#333
    style ADAPTERS fill:#d1ecf1,color:#333
    style CONTEXT fill:#f8d7da,color:#333
    style QUALITY fill:#e2e3e5,color:#333
```

## Class diagram

```mermaid
classDiagram
    class EvolutionMethod {
        <<abstract>>
        +name: str
        +description: str
        +source: str
        +evolve(hamiltonian, t, **params) NDArray
        +run(hamiltonian, t, **params) EvolutionResult
        +context: dict | None
    }

    class PauliTerm {
        +coefficient: float
        +pauli_word: str
        +qubit_order: tuple
        +to_matrix() NDArray
        +to_dict() dict
    }

    class PauliHamiltonian {
        +identifier: str
        +terms: tuple~PauliTerm~
        +lambda_norm: float
        +sha256: str
        +dense_terms() tuple
        +to_dict() dict
    }

    class EvolutionResult {
        +representation: str
        +method_name: str
        +parameters: dict
        +costs: EvolutionCosts
        +sampled_sequence: tuple
        +to_metadata() dict
    }

    class OperationSequence {
        +operations: tuple
        +compact_adjacent() OperationSequence
        +compile_reference() ReferenceCircuit
        +to_unitary() NDArray
    }

    class ReferenceCircuit {
        +gates: tuple
        +one_qubit_gates: int
        +two_qubit_gates: int
        +depth: int
    }

    class Registry {
        +register(name) decorator
        +get(name) EvolutionMethod
        +list_methods() list~str~
        +list_methods_detail() list~dict~
        +get_context(name) dict | None
    }

    class TrotterFirstOrder {
        +source = "algorithms-thrust"
        +evolve(terms, t, steps)
    }

    class TrotterSecondOrder {
        +source = "algorithms-thrust"
        +evolve(terms, t, steps)
    }

    class ExactEvolution {
        +source = "openqevo"
        +evolve(terms, t)
    }

    class QiskitTrotterAdapter {
        +source = "qiskit"
        +evolve(terms, t, **params)
    }

    class PennyLaneTrotterAdapter {
        +source = "pennylane"
        +evolve(terms, t, **params)
    }

    class QrackTrotterAdapter {
        +source = "qrack"
        +evolve(terms, t, **params)
    }

    class FutureMethod {
        <<planned>>
        +source = "algorithms-thrust"
        +evolve(terms, t, **params)
    }

    EvolutionMethod <|-- TrotterFirstOrder
    EvolutionMethod <|-- TrotterSecondOrder
    EvolutionMethod <|-- ExactEvolution
    EvolutionMethod <|-- QiskitTrotterAdapter
    EvolutionMethod <|-- PennyLaneTrotterAdapter
    EvolutionMethod <|-- QrackTrotterAdapter
    EvolutionMethod <|-- FutureMethod
    PauliHamiltonian *-- PauliTerm
    EvolutionMethod --> PauliHamiltonian : consumes
    EvolutionMethod --> EvolutionResult : produces
    EvolutionResult --> OperationSequence : scalable output
    OperationSequence --> ReferenceCircuit : compiles
    Registry --> EvolutionMethod : manages
```

## Project structure

```
src/openqevo/
├── __init__.py              # Auto-registers methods, exports registry API
├── base.py                  # EvolutionMethod ABC
├── hamiltonian.py           # Canonical Pauli input + dense compatibility
├── operations.py            # Scalable Pauli operations + logical compiler
├── result.py                # Structured results, costs, and provenance
├── conformance.py           # Native/Qiskit/PennyLane convention suite
├── workloads.py             # Controlled, spin, and mapped chemistry inputs
├── study.py                 # Frozen study runner and immutable archive
├── registry.py              # @register, get(), list_methods(), context loader
├── methods/
│   ├── __init__.py          # Auto-imports all native methods
│   └── trotter.py           # Trotter-Suzuki 1st/2nd order + exact references
└── adapters/
    ├── __init__.py          # Optional imports (skip if lib not installed)
    ├── qiskit_adapter.py    # Qiskit wrapper (working)
    ├── pennylane_adapter.py # PennyLane wrapper (working)
    └── qrack_adapter.py     # Qrack-backed Trotter adapter (experimental)
```

The canonical `PauliHamiltonian` is the benchmark and adapter input boundary.
Legacy sequences of dense Hermitian terms are validated and retained for
small-system compatibility. `EvolutionMethod.run(...)` returns structured
metadata and output, while `evolve(...)` remains the direct dense-unitary API.
Canonical Pauli inputs can instead return operation sequences or reference
circuits without materializing exponentially large unitaries.

The Qrack adapter is implemented and validated in CPU mode with real
`pyqrack`. GPU acceleration depends on a working host OpenCL/NVIDIA runtime;
the adapter remains marked experimental until GPU validation is complete.

## How to add a new method

Adding a new evolution method requires **one file** and **one import line**:

### 1. Create the method file

```python
# src/openqevo/methods/qdrift.py
from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("qdrift")
class QDrift(EvolutionMethod):
    description = "Randomized product formula"
    source = "algorithms-thrust"

    def evolve(self, terms, t, **params): ...
```

### 2. Register it

Add one import to `src/openqevo/methods/__init__.py`:

```python
from openqevo.methods import qdrift  # noqa: F401
```

That's it. The method is now available via `openqevo.get("qdrift")` and
appears in `openqevo.list_methods()`.

### 3. (Optional) Add context metadata

Create `context/methods/qdrift.json` following the schema in
`context/schema/method.schema.json`.
The method's `.context` property will automatically load and validate it.

```json
{
  "method_name": "qdrift",
  "description": "...",
  "source": "algorithms-thrust",
  "parameters": {
    "steps": { "type": "int", "description": "...", "required": true }
  }
}
```

Use `pytest --no-context-validation` while the file is still incomplete.

## How to add an adapter

Same pattern, but in `adapters/` and with a `try/except` import:

### 1. Create the adapter file

```python
# src/openqevo/adapters/new_lib_adapter.py
from new_lib import SomeEvolver

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("new_lib_evolver")
class NewLibAdapter(EvolutionMethod):
    description = "Evolution via new_lib"
    source = "new_lib"

    def evolve(self, terms, t, **params):
        # Translate terms to new_lib format and call
        ...
```

### 2. Register it

Add to `src/openqevo/adapters/__init__.py`:

```python
try:
    from openqevo.adapters import new_lib_adapter  # noqa: F401
except ImportError:
    pass
```

The `try/except` ensures openQEvo works without `new_lib` installed.

## Context validation

Every `context/methods/*.json` file is validated against
`context/schema/method.schema.json` (JSON Schema draft 2020-12) both at
**runtime** (when `.context` is accessed) and in **tests**
(`test_context_validates_against_schema`).

### Runtime behaviour

`registry.get_context()` validates by default. Pass `validate=False` to skip
for a specific call:

```python
ctx = openqevo.registry.get_context("qdrift", validate=False)
```

The global default is controlled by `registry._settings["context_validation"]`
(always `True` in normal use). This will become `openqevo.configure()` in a
future release.

### Disabling validation during development

When writing a new context file that is not yet complete, pass
`--no-context-validation` to pytest to skip the schema test for the whole
session:

```bash
pytest --no-context-validation
```

Remove the flag once the file satisfies the schema; CI always runs without it.

### Currently required fields

| Field | Type | Description |
|-------|------|-------------|
| `method_name` | string | Registry key matching `@register("name")` |
| `description` | string | Human-readable summary of the method |
| `source` | string (enum) | Origin: `algorithms-thrust`, `openqevo`, `qiskit`, `pennylane`, `qrack` |
| `parameters` | object | Per-parameter metadata (type, description, required, range) |

All other fields (`applicable_hamiltonians`, `limitations`, `complexity`,
`references`, `example_path`) are optional but encouraged — see
`context/methods/trotter_s1.json` for a complete example.

### Promoting a field to required

1. Add the field name to `"required"` in `context/schema/method.schema.json`
2. Add the field to every existing `context/methods/*.json` file
3. Run `pytest` — the schema test enforces it automatically with no test code changes
