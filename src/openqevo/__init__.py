"""openQEvo — Open library for quantum evolution operators."""

__version__ = "0.1.0"

# Auto-register all native methods on import
# Auto-register adapters for any installed external libraries
import openqevo.adapters  # noqa: F401
import openqevo.methods  # noqa: F401
from openqevo.execution import execute_recommendation
from openqevo.registry import get, list_methods, list_methods_detail

__all__ = ["execute_recommendation", "get", "list_methods", "list_methods_detail"]
