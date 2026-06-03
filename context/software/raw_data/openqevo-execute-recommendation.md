# OpenQEvo `execute_recommendation` Raw Execution Note

Source file: `src/openqevo/execution.py`

Generated from local source inspection and `conda run -p ./.conda python -m pydoc openqevo.execution` on 2026-06-03.

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
    **overrides,
)
```

Returns a NumPy array representing the evolved unitary returned by the selected
registered OpenQEvo method.

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
- Merges parameters in this precedence order:
  recommendation `parameters`, explicit `parameters`, then keyword overrides.
- Validates `execution.required_arguments`, including `terms`, `t`, and any
  method-specific required parameters.
- Calls `openqevo.get(method_name).evolve(list(terms), t, **params)`.

## AS/RAG Relevance

An executable LLM recommendation must select a registered method and either
provide `terms`, `t`, and required parameters directly or arrange for the caller
to pass them into `execute_recommendation`. Non-executable planned methods such
as `mitiq_zne` should be recommended only as future/planned wrappers unless an
adapter is registered and its context `execution.implemented` flag is changed to
`true`.
