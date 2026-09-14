# OpenQEvo `execute_recommendation` Raw Execution Note

Source file: `src/openqevo/execution.py`

Generated from local source inspection on 2026-06-03 and updated against the
canonical execution contracts on 2026-09-01.

## Module

`openqevo.execution` provides execution helpers for context-backed
recommendations.

## Function Signature

```python
execute_recommendation(
    recommendation,
    terms=None,
    t=None,
    parameters=None,
    *,
    structured=False,
    **overrides,
)
```

Returns the compatibility output from `evolve(...)` by default. With
`structured=True`, returns the method's versioned `EvolutionResult` containing
the output, normalized parameters, provenance, costs, seeds, environment,
warnings, and limitations.

## Behavior

- Reads `method_name` from `recommendation["method_name"]`,
  `recommendation["method"]`, or `recommendation["execution"]["method_name"]`.
- Loads method context with `openqevo.registry.get_context(method_name,
  validate=False)`.
- Uses `recommendation["execution"]` when present; otherwise falls back to the
  method context `execution` block.
- Rejects recommendations whose `execution.method_name` does not match the
  top-level selected method.
- Rejects `execution.implemented == false` with `NotImplementedError`.
- Rejects unknown or non-registered methods with `KeyError`.
- Uses explicit `terms` and `t` arguments when supplied; otherwise reads
  `recommendation["terms"]` and `recommendation["t"]`.
- Accepts a `PauliHamiltonian`, legacy dense matrix terms, or a serialized
  `openqevo-pauli-hamiltonian/v1` mapping.
- Merges parameters in this precedence order:
  recommendation `parameters`, explicit `parameters`, then keyword overrides.
- Validates `execution.required_arguments`, including `terms`, `t`, and any
  method-specific required parameters.
- Calls `openqevo.get(method_name).run(terms, t, **params)` for structured
  execution and `evolve(terms, t, **params)` for compatibility execution.

## AS/RAG Relevance

An executable LLM recommendation must select a registered method and either
provide a canonical Hamiltonian, `t`, and required parameters directly or
arrange for the caller to pass them into `execute_recommendation`. AS can use
the declared input and result schema versions without owning method execution.
Non-executable planned methods such as `mitiq_zne` should be recommended only as
future/planned wrappers unless an adapter is registered and its context
`execution.implemented` flag is changed to `true`.
