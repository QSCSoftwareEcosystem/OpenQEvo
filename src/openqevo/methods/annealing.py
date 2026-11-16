"""Dense reference adiabatic and annealing evolution."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm

from openqevo.base import EvolutionMethod
from openqevo.methods._dense import (
    finite_time,
    integer_param,
    sum_terms,
    validate_compatible_terms,
    validate_terms,
)
from openqevo.registry import register


@register("adiabatic_evolution")
class AdiabaticEvolution(EvolutionMethod):
    """Dense reference adiabatic evolution over a Hamiltonian path."""

    description = (
        "Dense adiabatic/annealing reference evolution for H(s) = (1 - s) H0 + s H1"
    )
    source = "algorithms-thrust"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        """Approximate time-ordered evolution under a scheduled path."""
        t = finite_time(t)
        steps = integer_param(params, "steps")
        schedule = _schedule(params.get("schedule", {"type": "linear"}))

        initial_terms = params.get("initial_terms")
        if initial_terms is None:
            raise TypeError("'initial_terms' is a required parameter.")
        initial_terms = list(initial_terms)

        dim = validate_terms(terms, "Final terms")
        validate_compatible_terms(initial_terms, dim, "Initial terms")

        h0 = sum_terms(initial_terms)
        h1 = sum_terms(terms)
        dt = t / steps
        result = np.eye(dim, dtype=complex)

        for step_index in range(steps):
            midpoint = (step_index + 0.5) / steps
            s_value = schedule(midpoint)
            h_mid = (1 - s_value) * h0 + s_value * h1
            result = expm(-1j * h_mid * dt) @ result

        return result


def _schedule(spec: Any):
    if spec == "linear":
        return lambda s: s

    if isinstance(spec, Mapping):
        schedule_type = spec.get("type", "linear")
        if schedule_type == "linear":
            return lambda s: s
        if schedule_type == "power":
            power = float(spec.get("power", 1.0))
            if not np.isfinite(power) or power <= 0:
                raise ValueError("Schedule power must be finite and positive.")
            return lambda s: s**power

    raise ValueError("'schedule' must be 'linear' or a supported schedule object.")
