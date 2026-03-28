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


class EvolutionMethod(ABC):
    """Abstract base class for a time-evolution strategy.

    Subclasses must implement :meth:`evolve`. They may optionally provide
    a ``context`` dict loaded from a JSON file in ``context/``.
    """

    name: str = ""
    description: str = ""
    source: str = ""  # e.g. "algorithms-thrust", "qiskit", "pennylane"

    @abstractmethod
    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
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

    @property
    def context(self) -> dict[str, Any] | None:
        """Structured metadata for this method, loaded from context/ JSON.

        Returns None if no context file has been registered.
        """
        from openqevo.registry import get_context

        return get_context(self.name)
