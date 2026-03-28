"""Example: Trotter-Suzuki convergence for a two-term Hamiltonian.

Demonstrates how first- and second-order Trotter errors decrease
as the number of steps increases. Uses the registry to fetch methods
by name — the same interface an AI agent would use.
"""

import numpy as np

import openqevo

# Hamiltonian: H = X + Z (two non-commuting Pauli terms)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)

terms = [SIGMA_X, SIGMA_Z]
t = 1.0

# Get methods from the registry
s1 = openqevo.get("trotter_s1")
s2 = openqevo.get("trotter_s2")
exact = openqevo.get("exact")

exact_result = exact.evolve(terms, t)

print(f"Available methods: {openqevo.list_methods()}")
print()
print(f"Trotter-Suzuki convergence for H = X + Z, t = {t}")
print(f"{'Steps':>8}  {'1st order error':>16}  {'2nd order error':>16}")
print("-" * 44)

for steps in [1, 2, 5, 10, 20, 50, 100, 200]:
    err1 = np.linalg.norm(s1.evolve(terms, t, steps=steps) - exact_result)
    err2 = np.linalg.norm(s2.evolve(terms, t, steps=steps) - exact_result)
    print(f"{steps:>8}  {err1:>16.2e}  {err2:>16.2e}")
