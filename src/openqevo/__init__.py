"""openQEvo — Open library for quantum evolution operators."""

__version__ = "0.1.0"

# Auto-register all native methods on import
# Auto-register adapters for any installed external libraries
import openqevo.adapters  # noqa: F401
import openqevo.methods  # noqa: F401
from openqevo.execution import execute_recommendation
from openqevo.hamiltonian import PauliHamiltonian, PauliTerm
from openqevo.registry import get, list_methods, list_methods_detail
from openqevo.result import EvolutionCosts, EvolutionResult

__all__ = [
    "EvolutionCosts",
    "EvolutionResult",
    "PauliHamiltonian",
    "PauliTerm",
    "execute_recommendation",
    "get",
    "list_methods",
    "list_methods_detail",
]
