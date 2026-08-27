"""Execution helpers for context-backed recommendations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from numpy.typing import NDArray

import openqevo.registry as registry


def execute_recommendation(
    recommendation: Mapping[str, Any],
    terms: Sequence[NDArray[Any]] | None = None,
    t: float | None = None,
    parameters: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> NDArray[Any]:
    """Execute an implemented recommendation through the OpenQEvo registry."""
    method_name = _recommendation_method_name(recommendation)
    context = registry.get_context(method_name, validate=False)
    execution = _execution_contract(recommendation, context)

    if execution is not None:
        execution_method_name = execution.get("method_name")
        if execution_method_name != method_name:
            raise ValueError(
                "Recommendation method_name does not match execution.method_name."
            )
        if not execution.get("implemented", False):
            reason = execution.get("non_executable_reason", "Method is not executable.")
            raise NotImplementedError(reason)

    if method_name not in registry.list_methods():
        raise KeyError(f"Unknown or non-executable method {method_name!r}.")

    if terms is None:
        terms = recommendation.get("terms")
    if t is None:
        t = recommendation.get("t")

    params = _merge_parameters(recommendation, parameters, overrides)
    _validate_required_arguments(execution, terms, t, params)

    if terms is None:
        raise ValueError("'terms' is required.")
    if t is None:
        raise ValueError("'t' is required.")

    return registry.get(method_name).evolve(list(terms), t, **params)


def _recommendation_method_name(recommendation: Mapping[str, Any]) -> str:
    for key in ("method_name", "method"):
        value = recommendation.get(key)
        if isinstance(value, str):
            return value

    execution = recommendation.get("execution")
    if isinstance(execution, Mapping) and isinstance(execution.get("method_name"), str):
        return execution["method_name"]

    raise ValueError("Recommendation must include 'method_name' or 'method'.")


def _execution_contract(
    recommendation: Mapping[str, Any],
    context: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    execution = recommendation.get("execution")
    if isinstance(execution, Mapping):
        return execution
    if context is None:
        return None
    execution = context.get("execution")
    return execution if isinstance(execution, Mapping) else None


def _merge_parameters(
    recommendation: Mapping[str, Any],
    parameters: Mapping[str, Any] | None,
    overrides: Mapping[str, Any],
) -> dict[str, Any]:
    merged: dict[str, Any] = {}

    recommendation_parameters = recommendation.get("parameters")
    if isinstance(recommendation_parameters, Mapping):
        merged.update(recommendation_parameters)

    if parameters is not None:
        merged.update(parameters)

    merged.update(overrides)
    return merged


def _validate_required_arguments(
    execution: Mapping[str, Any] | None,
    terms: Sequence[NDArray[Any]] | None,
    t: float | None,
    parameters: Mapping[str, Any],
) -> None:
    if execution is None:
        return

    required = execution.get("required_arguments", [])
    if "terms" in required and terms is None:
        raise ValueError("'terms' is required.")
    if "t" in required and t is None:
        raise ValueError("'t' is required.")

    missing_parameters = [
        name
        for name in required
        if name not in {"terms", "t"} and name not in parameters
    ]
    if missing_parameters:
        joined = ", ".join(sorted(missing_parameters))
        raise ValueError(f"Missing required parameter(s): {joined}.")
