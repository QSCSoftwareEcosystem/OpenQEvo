# Annealing and Adiabatic Evolution

This collection concerns quantum evolution along Hamiltonian paths, including
adiabatic state preparation and quantum annealing. The principles
`adiabatic-schedule-gap-constraints` and `quantum-annealing-scope` distinguish
schedule/gap conditions from the broader optimization workflow.

## Current OpenQEvo capability

Two registered methods provide **experimental dense classical references**:

| Registry key | Inputs and schedule | Current output |
| --- | --- | --- |
| `annealing` | Target supplied as canonical Pauli or dense `terms`; optional `initial_hamiltonian`, defaulting to a transverse-field driver `-sum_i X_i`; linear schedule only. | Dense unitary with schedule and driver provenance through `run(...)`. |
| `adiabatic_evolution` | Dense final `terms` and required dense `initial_terms`; linear schedule by default or `{"type": "power", "power": p}` with finite positive `p`. | Dense unitary; `run(...)` wraps it in the shared result contract. |

Both require total evolution time `t` and a positive integer `steps`. They
approximate the time-ordered propagator of an interpolated Hamiltonian using
midpoint segments. Neither API selects a favorable schedule automatically.
The two keys have different input contracts and are not interchangeable names.

Engineering evidence:

- [Linear annealing contract](../../methods/annealing.json) and
  [implementation](../../../src/openqevo/methods/advanced.py).
- [Explicit-path adiabatic contract](../../methods/adiabatic_evolution.json)
  and [implementation](../../../src/openqevo/methods/annealing.py).

## Scientific and implementation boundaries

The key point `adiabatic-schedule-gap-constraints` concerns remaining near a
desired instantaneous eigenstate: this depends on initial-state preparation,
the path, schedule regularity, spectral properties, and total evolution time.
The propagation APIs return operators. A small discretization error or a
large step count alone does not establish successful ground-state preparation.

`quantum-annealing-scope` describes quantum fluctuations and analog/adiabatic
strategies in the literature. The present dense references do not implement a
quantum annealing device, hardware control schedules, open-system/noise models,
gap estimation, or a full optimization/measurement workflow. They provide no
circuit or hardware resource estimate. Scientific approval of implementation
claims and method applicability remains pending.

## Evidence and navigation

- `adiabatic-schedule-gap-constraints`:
  [structured concept](../key_points/adiabatic_schedule_gap_constraints.json).
- `quantum-annealing-scope`:
  [structured concept](../key_points/quantum_annealing_scope.json).
- [Source inventory](../source_inventory.md): Farhi foundational paper,
  Albash–Lidar adiabatic-computing review, Das–Chakrabarti annealing review.

The sources support scientific principles; method contracts and source code
support the software-status statements. This synthesis is not reviewer sign-off.
