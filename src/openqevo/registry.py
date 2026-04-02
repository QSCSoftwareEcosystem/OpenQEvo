"""Registry for discovering and accessing evolution methods.

Methods self-register using the ``@register`` decorator. Users and AI agents
can list available methods and retrieve them by name.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema

from openqevo.base import EvolutionMethod

_METHODS: dict[str, type[EvolutionMethod]] = {}

CONTEXT_DIR = Path(__file__).resolve().parent.parent.parent / "context"

_settings: dict = {
    "context_validation": True,
}


def register(name: str):
    """Class decorator that registers an evolution method.

    Usage::

        @register("trotter_s1")
        class TrotterFirstOrder(EvolutionMethod):
            ...
    """

    def decorator(cls: type[EvolutionMethod]) -> type[EvolutionMethod]:
        cls.name = name
        _METHODS[name] = cls
        return cls

    return decorator


def get(name: str, **kwargs: Any) -> EvolutionMethod:
    """Get an instance of a registered method by name.

    Parameters
    ----------
    name : str
        Registered method name (e.g. ``"trotter_s1"``).
    **kwargs
        Passed to the method constructor.

    Raises
    ------
    KeyError
        If the method name is not registered.
    """
    if name not in _METHODS:
        available = ", ".join(sorted(_METHODS)) or "(none)"
        raise KeyError(f"Unknown method {name!r}. Available methods: {available}")
    return _METHODS[name](**kwargs)


def list_methods() -> list[str]:
    """Return a sorted list of registered method names."""
    return sorted(_METHODS)


def list_methods_detail() -> list[dict[str, str]]:
    """Return details for all registered methods."""
    return [
        {
            "name": name,
            "description": cls.description,
            "source": cls.source,
        }
        for name, cls in sorted(_METHODS.items())
    ]


def _validate_context(ctx: dict) -> None:
    """Validate a context dict against context/schema.json."""
    schema_path = CONTEXT_DIR / "schema.json"
    with open(schema_path) as f:
        schema = json.load(f)
    jsonschema.validate(instance=ctx, schema=schema)


def get_context(name: str, validate: bool | None = None) -> dict[str, Any] | None:
    """Load context JSON for a method, if it exists.

    Looks for ``context/{name}.json``.

    Parameters
    ----------
    name : str
        Registered method name.
    validate : bool or None
        Whether to validate against schema.json. If None, uses the global
        ``_settings["context_validation"]`` value (default True).
    """
    path = CONTEXT_DIR / f"{name}.json"
    if not path.exists():
        return None
    with open(path) as f:
        ctx = json.load(f)
    should_validate = validate if validate is not None else _settings["context_validation"]
    if should_validate:
        _validate_context(ctx)
    return ctx
