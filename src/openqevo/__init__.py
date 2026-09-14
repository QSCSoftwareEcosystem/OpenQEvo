"""openQEvo — Open library for quantum evolution operators."""

__version__ = "0.1.0"

# Auto-register all native methods on import
# Auto-register adapters for any installed external libraries
import openqevo.adapters  # noqa: F401
import openqevo.methods  # noqa: F401
from openqevo.execution import execute_recommendation
from openqevo.hamiltonian import PauliHamiltonian, PauliTerm
from openqevo.operations import (
    GateOperation,
    OperationSequence,
    PauliEvolutionOperation,
    ReferenceCircuit,
)
from openqevo.registry import get, list_methods, list_methods_detail
from openqevo.result import EvolutionCosts, EvolutionResult
from openqevo.workloads import (
    commutator_graph_density,
    controlled_pauli_hamiltonian,
    h2_two_qubit,
    heisenberg_chain,
    transverse_field_ising,
)

__all__ = [
    "EvolutionCosts",
    "EvolutionResult",
    "GateOperation",
    "OperationSequence",
    "PauliHamiltonian",
    "PauliEvolutionOperation",
    "PauliTerm",
    "ReferenceCircuit",
    "commutator_graph_density",
    "controlled_pauli_hamiltonian",
    "execute_recommendation",
    "get",
    "h2_two_qubit",
    "heisenberg_chain",
    "list_methods",
    "list_methods_detail",
    "transverse_field_ising",
]
