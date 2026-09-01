"""Base protocol for quantum evolution methods.

Every evolution method in openQEvo — whether a native implementation from
the Algorithms Thrust or an adapter wrapping Qiskit/PennyLane — conforms
to this protocol.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import numpy as np
from numpy.typing import NDArray

from openqevo.hamiltonian import HamiltonianInput, hamiltonian_provenance
from openqevo.result import (
    EvolutionCosts,
    EvolutionResult,
    implementation_provenance,
    installed_versions,
    runtime_environment,
)


class EvolutionMethod(ABC):
    """Abstract base class for a time-evolution strategy.

    Subclasses must implement :meth:`evolve`. They may optionally provide
    a ``context`` dict loaded from a JSON file in ``context/methods/``.
    """

    name: str = ""
    description: str = ""
    source: str = ""  # e.g. "algorithms-thrust", "qiskit", "pennylane"
    backend_packages: tuple[str, ...] = ()

    @abstractmethod
    def evolve(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Compute the time-evolution operator exp(-i H t).

        Parameters
        ----------
        terms : list of ndarray
            Hermitian matrices representing the terms H_k in the Hamiltonian
            H = sum(terms).
        t : float
            Total evolution time.
        **params
            Method-specific parameters (e.g. ``steps`` for Trotter).

        Returns
        -------
        ndarray
            Unitary matrix approximating exp(-i H t).
        """

    def run(
        self,
        terms: HamiltonianInput,
        t: float,
        **params: Any,
    ) -> EvolutionResult:
        """Execute a method and return the structured provenance contract.

        ``evolve`` remains the dense-unitary compatibility API. Native methods
        override this method when they can report exact formula costs or sampled
        randomized trajectories.
        """
        output = self.evolve(terms, t, **params)
        metadata_parameters = {
            "evolution_time": float(t),
            **{
                name: value
                for name, value in params.items()
                if name not in {"rng", "sampled_sequence"}
            },
        }
        return EvolutionResult(
            output=output,
            representation="unitary",
            method_name=self.name,
            implementation=implementation_provenance(
                self.source,
                backend_versions=installed_versions(self.backend_packages),
            ),
            parameters=metadata_parameters,
            costs=EvolutionCosts(),
            hamiltonian=hamiltonian_provenance(terms),
            seed=params.get("seed"),
            sampled_sequence=params.get("sampled_sequence"),
            environment=runtime_environment(),
            limitations=self._limitations(),
        )

    def _limitations(self) -> tuple[str, ...]:
        context = self.context
        if context is None:
            return ()
        return tuple(str(item) for item in context.get("limitations", ()))

    @property
    def context(self) -> dict[str, Any] | None:
        """Structured metadata for this method, loaded from context/methods/ JSON.

        Returns None if no context file has been registered.
        """
        from openqevo.registry import get_context

        return get_context(self.name)
