"""Example: Trotter-Suzuki convergence for a two-term Hamiltonian.

Demonstrates how first- and second-order Trotter errors decrease as the number
of steps increases. Use ``--plot PATH`` to save the convergence figure used in
the project README.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

import openqevo

# Hamiltonian: H = X + Z (two non-commuting Pauli terms)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)

STEPS = (1, 2, 5, 10, 20, 50, 100, 200)


def convergence_data() -> list[tuple[int, float, float]]:
    """Return first- and second-order errors for the bundled example."""
    terms = [SIGMA_X, SIGMA_Z]
    evolution_time = 1.0
    first_order = openqevo.get("trotter_s1")
    second_order = openqevo.get("trotter_s2")
    exact_result = openqevo.get("exact").evolve(terms, evolution_time)

    rows = []
    for steps in STEPS:
        first_error = np.linalg.norm(
            first_order.evolve(terms, evolution_time, steps=steps) - exact_result
        )
        second_error = np.linalg.norm(
            second_order.evolve(terms, evolution_time, steps=steps) - exact_result
        )
        rows.append((steps, float(first_error), float(second_error)))
    return rows


def print_table(rows: list[tuple[int, float, float]]) -> None:
    """Print the convergence data in a compact terminal table."""
    print(f"Available methods: {openqevo.list_methods()}")
    print()
    print("Trotter-Suzuki convergence for H = X + Z, t = 1.0")
    print(f"{'Steps':>8}  {'1st order error':>16}  {'2nd order error':>16}")
    print("-" * 44)
    for steps, first_error, second_error in rows:
        print(f"{steps:>8}  {first_error:>16.2e}  {second_error:>16.2e}")


def save_plot(rows: list[tuple[int, float, float]], output: Path) -> None:
    """Render the convergence evidence as an accessible repository-owned SVG."""
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover - depends on optional extra
        raise SystemExit(
            'Plotting requires: pip install -e ".[visualization]"'
        ) from exc

    steps = [row[0] for row in rows]
    first_errors = [row[1] for row in rows]
    second_errors = [row[2] for row in rows]

    figure, axis = plt.subplots(figsize=(10.8, 5.8), constrained_layout=True)
    figure.patch.set_facecolor("#f4f1e9")
    axis.set_facecolor("#fffdf8")
    axis.loglog(
        steps,
        first_errors,
        "o-",
        color="#306a91",
        linewidth=2.4,
        markersize=6,
        label="First-order Trotter",
    )
    axis.loglog(
        steps,
        second_errors,
        "o-",
        color="#ae1935",
        linewidth=2.4,
        markersize=6,
        label="Second-order Trotter",
    )
    axis.set_title(
        "Trotter-Suzuki convergence",
        color="#101d2d",
        fontsize=18,
        fontweight="bold",
        loc="left",
        pad=16,
    )
    axis.text(
        0,
        1.01,
        "H = X + Z, t = 1.0 · matrix-norm error against exact evolution",
        color="#526273",
        fontsize=10,
        transform=axis.transAxes,
        va="bottom",
    )
    axis.set_xlabel("Trotter steps", color="#101d2d", fontweight="bold")
    axis.set_ylabel("Approximation error", color="#101d2d", fontweight="bold")
    axis.grid(True, which="both", color="#101d2d", alpha=0.12, linewidth=0.8)
    axis.legend(frameon=False, loc="lower left")
    axis.tick_params(colors="#253548")
    for spine in axis.spines.values():
        spine.set_color("#9aa5ae")

    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(
        output,
        format=output.suffix.lstrip(".") or "svg",
        facecolor=figure.get_facecolor(),
        metadata={
            "Title": "openQEvo Trotter-Suzuki convergence",
            "Creator": "examples/trotter_convergence.py",
            "Date": None,
        },
    )
    plt.close(figure)

    if output.suffix.lower() == ".svg":
        svg = output.read_text(encoding="utf-8")
        normalized = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
        output.write_text(normalized, encoding="utf-8")

    print(f"Saved plot: {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--plot",
        type=Path,
        metavar="PATH",
        help="save the convergence figure (SVG recommended)",
    )
    args = parser.parse_args()

    rows = convergence_data()
    print_table(rows)
    if args.plot:
        save_plot(rows, args.plot)


if __name__ == "__main__":
    main()
