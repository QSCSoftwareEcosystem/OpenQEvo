"""Adapter wrapping Mitiq's error mitigation around any evolution method.

Requires: pip install mitiq

Mitiq is a Unitary Foundation toolkit for quantum error mitigation. Unlike
other adapters, this one doesn't compute evolution directly — it wraps an
existing openQEvo method and applies error mitigation (e.g., zero-noise
extrapolation) to improve the result.

This adapter is not loaded if mitiq is not installed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import NDArray

from openqevo.base import EvolutionMethod
from openqevo.registry import register


@register("mitiq_zne")
class MitiqZNEAdapter(EvolutionMethod):
    """Error-mitigated evolution via Mitiq's zero-noise extrapolation.

    Wraps another openQEvo method and applies ZNE to mitigate
    Trotter errors by extrapolating from multiple step counts.
    """

    description = (
        "Error-mitigated evolution via zero-noise extrapolation "
        "(Unitary Foundation / Mitiq)"
    )
    source = "mitiq"

    def evolve(
        self,
        terms: list[NDArray[np.complexfloating]],
        t: float,
        **params: Any,
    ) -> NDArray[np.complexfloating]:
        # TODO: Implement when Mitiq integration is ready.
        # This stub defines the interface; the actual implementation
        # will take a base_method param, run it at multiple Trotter
        # step counts, and use Mitiq's ZNE to extrapolate.
        #
        # Expected params:
        #   base_method: str — name of the underlying method (e.g. "trotter_s1")
        #   steps: int — base step count
        #   scale_factors: list[float] — noise scale factors for ZNE
        raise NotImplementedError(
            "Mitiq adapter is a stub. Contributions welcome — see issue #3."
        )
