# Interaction-Picture Evolution

This wiki collection will cover interaction-picture and QIT-style quantum evolution strategies.

## Current status

No native interaction-picture evolution method is implemented in OpenQEvo yet. Existing trotterization context already flags these methods as literature-supported alternatives when direct Trotter depth is impractical.

## Scope

- Interaction-picture Hamiltonian simulation.
- Splitting dominant exactly simulable terms from residual interactions.
- Hybrid strategies that combine product formulas, qDRIFT, or oracle-based methods.

## Evidence state

A seed raw paper has been added for interaction-picture Hamiltonian simulation. Related evidence also lives in `../trotterization/key_points/trotter_alternatives_and_hybrid_methods.json`.

Current key-point IDs:

- `interaction-picture-split-hamiltonian`

## Source inventory

- [`../source_inventory.md`](../source_inventory.md)
