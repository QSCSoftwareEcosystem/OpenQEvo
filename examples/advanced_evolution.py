"""Compare the experimental dense evolution references on a one-qubit model.

The methods in this example are numerical references for small systems.  They
return dense unitaries and do not synthesize hardware circuits.
"""

from __future__ import annotations

import numpy as np

import openqevo

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
TERMS = [SIGMA_Z, 0.4 * SIGMA_X]
EVOLUTION_TIME = 0.8


def unitary_error(unitary: np.ndarray, reference: np.ndarray) -> float:
    """Return the Frobenius-norm difference between dense propagators."""
    return float(np.linalg.norm(unitary - reference))


def main() -> None:
    """Run one representative configuration of each experimental method."""
    exact = openqevo.get("exact").evolve(TERMS, EVOLUTION_TIME)
    annealing_reference = openqevo.get("annealing").evolve(
        TERMS, EVOLUTION_TIME, steps=2048
    )
    configurations = {
        "krylov": ({"krylov_dim": 2}, exact, "static exact"),
        "interaction_picture": (
            {"steps": 32, "reference_term_indices": [0]},
            exact,
            "static exact",
        ),
        "annealing": ({"steps": 32}, annealing_reference, "2048-step anneal"),
    }

    print("Experimental dense evolution references")
    print(f"{'Method':<22} {'Numerical error':>16}  Reference")
    print("-" * 72)
    for method_name, (parameters, reference, label) in configurations.items():
        result = openqevo.get(method_name).run(TERMS, EVOLUTION_TIME, **parameters)
        print(
            f"{method_name:<22} "
            f"{unitary_error(result.output, reference):>16.2e}  {label}"
        )


if __name__ == "__main__":
    main()
