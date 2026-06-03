# Software Execution Stack

This collection is software evidence for adapter and execution behavior. It
complements paper evidence in the method-family collections by documenting the
APIs that OpenQEvo uses to execute or plan recommendations.

## Adapter Evidence

- Qiskit evidence covers `PauliEvolutionGate` and `SparsePauliOp`, which support
  the `qiskit_trotter` context metadata and execution contract
  (`qiskit-pauli-evolution-gate-contract`).
- PennyLane evidence covers `TrotterProduct` and `ApproxTimeEvolution`, which
  support the `pennylane_trotter` adapter context
  (`pennylane-trotter-product-contract`).
- Qrack and PyQrack evidence cover the simulator package used by the
  experimental `qrack_trotter` adapter (`qrack-runtime-requirements`).
- Mitiq evidence covers ZNE concepts and APIs. OpenQEvo currently keeps
  `mitiq_zne` as planned, non-executable metadata because no registered adapter
  wraps Mitiq yet (`mitiq-zne-wrapper-scope`).

## Execution Bridge

`openqevo.execute_recommendation(...)` connects an already-selected executable
recommendation to the OpenQEvo registry. The external AS/RAG layer should own
retrieval, ranking, and recommendation construction. OpenQEvo owns the schema,
method metadata, and execution bridge that validates and calls registered
methods.
This contract is captured by `openqevo-execute-recommendation-contract`.

## Inventory

See [`../source_inventory.md`](../source_inventory.md) for source URLs, local raw
Markdown paths, and conversion notes.
