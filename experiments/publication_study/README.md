# Software-frozen publication study

This directory expands the exploratory `X + Z` pilot into controlled Pauli,
spin-model, and fixed mapped H₂ workloads. The checked-in protocol freezes the
method set, workload parameters, equal logical-operation budgets, seeds,
tolerances, uncertainty rule, and failure-retention policy.

“Software-frozen” does not mean scientifically approved. Algorithms Thrust and
statistics reviewers remain unassigned, so the protocol and its results are a
publication candidate rather than final evidence.

Run into a new, empty bundle directory:

```bash
python -m openqevo.study \
  --protocol experiments/publication_study/protocol.json \
  --output-dir experiments/publication_study/results-2026-09-01
```

The command refuses to overwrite a nonempty bundle. It archives the protocol,
canonical workloads, pre-run resource estimate, raw JSONL records, derived
summary, overview figure, and SHA-256 manifest. Each qDRIFT record includes its
seed and complete sampled sequence; failed attempts remain in the raw stream.

The H₂ input is a fixed two-qubit operator archived in IBM Quantum tutorial
material. It is used as a mapped chemistry workload; OpenQEvo does not claim to
regenerate its electronic-structure transformation.
