# Krylov methods: two different computational roles

**Classical propagation.** Projected exponential actions are classical
numerical approximations (`classical-krylov-projection`). OpenQEvo's
`krylov` is an experimental dense reference: it propagates each basis vector,
uses `krylov_dim`/`tolerance`, and assembles a full matrix. Sweep dimension,
compare with `exact`, and inspect unitarity; no sparse or device solver is
provided.

**Quantum diagonalization.** Real-time basis preparation and projected
matrix estimation are ingredients of quantum Krylov algorithms
(`quantum-krylov-measurement-boundary`). No such measurement workflow is
registered here. Noisy overlap problems require conditioning/truncation
analysis (`quantum-subspace-conditioning`). Neither label alone establishes
hardware advantage.

The [inventory](../source_inventory.md) links primary-source evidence notes.
They support these scoped distinctions; full-text/equation-level curation and
scientific review remain pending. This wiki is synthesis, not primary evidence.
