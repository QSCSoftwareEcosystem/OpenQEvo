"""Adapters wrapping external libraries behind the EvolutionMethod protocol.

Each adapter is an optional integration. Import errors are caught so that
openQEvo works without the external library installed.
"""

try:
    from openqevo.adapters import qiskit_adapter  # noqa: F401
except ImportError:
    pass

try:
    from openqevo.adapters import pennylane_adapter  # noqa: F401
except ImportError:
    pass

try:
    from openqevo.adapters import qrack_adapter  # noqa: F401
except ImportError:
    pass
