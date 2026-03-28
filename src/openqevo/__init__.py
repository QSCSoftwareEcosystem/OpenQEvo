"""openQEvo — Open library for quantum evolution operators."""

__version__ = "0.1.0"

# Auto-register all native methods on import
import openqevo.methods  # noqa: F401

from openqevo.registry import get, list_methods, list_methods_detail

__all__ = ["get", "list_methods", "list_methods_detail"]
