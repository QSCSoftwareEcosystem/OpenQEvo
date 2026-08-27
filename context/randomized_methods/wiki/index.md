# Randomized Evolution Methods

This wiki collection will cover randomized quantum evolution strategies such as qDRIFT and randomized product formulas.

## Current status

OpenQEvo includes native `qdrift` method metadata and software registration. The current implementation accepts matrix terms and returns a sampled dense unitary.

## Scope

- qDRIFT and related randomized product formulas.
- Randomized Hamiltonian simulation strategies.
- Tradeoffs among sampling cost, circuit depth, Hamiltonian term norms, and error.

## Evidence state

Seed raw papers have been added for qDRIFT, randomized/permuted product formulas, stochastic Hamiltonian sparsification, and qSWIFT. Initial key points now cover qDRIFT scaling, randomized Trotter/permutation bounds, and randomized-method precision tradeoffs.

Current key-point IDs:

- `qdrift-randomized-scaling`
- `randomized-trotter-permutation-bounds`
- `randomized-methods-precision-tradeoffs`

## Method metadata

- [`../../methods/qdrift.json`](../../methods/qdrift.json)

## Source inventory

- [`../source_inventory.md`](../source_inventory.md)
