# X + Z paper pilot

This exploratory benchmark implements the smallest controlled study in the
OpenQEvo publication plan. It compares exact evolution, first-order Trotter,
second-order Trotter, and 30 independently seeded qDRIFT trajectories for the
noncommuting one-qubit Hamiltonian

`H = X + Z`, with `t = 1`.

Every approximation receives the same formula-level Pauli evolution-operation
budget. Trotter errors are deterministic. qDRIFT reports the distribution of
individual trajectory errors and the trace distance of the empirical ensemble
output state from the exact output for the declared initial state `|0>`.

Generate the complete bundle with:

```bash
python -m pip install -e ".[visualization]"
python -m openqevo.benchmark \
  --config experiments/xz_pilot/config.json \
  --output-dir experiments/xz_pilot/results \
  --replace
```

The runner writes each raw result once to a JSON Lines stream. The summary and
figure are then derived by reading that stream; plotting never reruns the
experiment. The manifest records byte counts and SHA-256 checksums for the
configuration, raw records, summary, and figure.

This is a validation pilot, not the frozen production study. It does not yet
cover larger systems, independent control of Hamiltonian term count and
`lambda`, compiled gate costs, framework conformance, or chemistry workloads.
