# Error Scaling

Trotter error is not only a function of simulation time, step count, and number of Hamiltonian terms. It is strongly affected by the commutator structure of the decomposed Hamiltonian.

When Hamiltonian terms commute or nearly commute, practical error can be much smaller than conservative worst-case bounds. When terms are dense and strongly non-commuting, shallow product formulas can require many steps.

## Practical checks

- Identify whether terms form commuting groups.
- Use exact evolution on small instances when possible.
- Sweep Trotter step counts before making final accuracy claims.
- Treat worst-case asymptotic bounds as guidance, not as a substitute for calibration.

## Method implication

Unknown commutator structure should lower recommendation confidence. A robust recommendation should ask for Hamiltonian representation, number of terms, locality, and target accuracy.

## Key points

- `trotter-error-commutator-scaling`
- `trotter-order-depth-tradeoff`
