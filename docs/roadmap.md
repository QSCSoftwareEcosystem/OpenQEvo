# Roadmap

**Deadline: June 2026**

All phases run in parallel. openQSE is a community specification; openQEvo
is the first concrete software deliverable from the Software Thrust.

## Timeline

```mermaid
gantt
    title openQEvo — compressed roadmap (deadline: June 2026)
    dateFormat YYYY-MM-DD
    axisFormat %b %Y

    section Foundation (done)
        Package structure & pyproject.toml     :done, se1, 2026-03-17, 2026-03-28
        Strategy + Registry + Adapter arch     :done, ar1, 2026-03-28, 2026-03-28
        Trotter placeholder + tests (14)       :done, hw0, 2026-03-28, 2026-03-28

    section Core (Apr)
        Draft JSON schema for context (DS)     :active, ds1, 2026-03-28, 2026-04-11
        Context JSON files for Trotter (HW)    :ctx1, 2026-04-07, 2026-04-18
        GitHub Actions CI (lint + test)        :ci1, 2026-03-28, 2026-04-04
        Algorithms Thrust code integration     :alg1, 2026-04-07, 2026-04-30

    section Adapters (Apr–May)
        Qiskit adapter                         :qk1, 2026-04-14, 2026-04-30
        PennyLane adapter                      :pl1, 2026-04-14, 2026-04-30
        Qrack adapter (Unitary Foundation)     :qr1, 2026-04-21, 2026-05-08
        Mitiq ZNE adapter (Unitary Foundation) :mt1, 2026-04-21, 2026-05-08

    section Integration (May–Jun)
        AI orchestration design (AS)           :as1, 2026-05-01, 2026-05-22
        MCP/RAG integration                    :as2, 2026-05-15, 2026-06-05
        Spack recipe                           :se2, 2026-05-15, 2026-05-29
        Documentation & examples               :doc1, 2026-05-22, 2026-06-12

    section Release
        v0.1.0 release                         :milestone, rel1, 2026-06-15, 0d
```

## Task tracker

### Foundation (done)

| Task | Status |
|------|--------|
| Package structure (`src/` layout, `pyproject.toml`) | Done |
| Strategy + Registry + Adapter architecture | Done |
| Trotter placeholder (1st, 2nd order, exact) | Done |
| 14 tests passing | Done |
| Adapter stubs (Qiskit, PennyLane, Qrack, Mitiq) | Done |
| README, CONTRIBUTING.md, docs/ | Done |

### Core — April 2026

| Task | Owner | Status | Issue |
|------|-------|--------|-------|
| Draft JSON schema for context files | DS (Thomas) | In progress | [#2](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/2) |
| Context JSON for Trotter methods | HW (Zack) | Open | [#4](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4) |
| GitHub Actions CI (lint, test, docs) | SE (Seth) | Open | [#1](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/1) |
| Replace placeholder with Algorithms Thrust code | HW + Algorithms | Pending | — |

### Adapters — April/May 2026

| Adapter | Library | Type | Status |
|---------|---------|------|--------|
| `qiskit_trotter` | Qiskit | Direct evolution | Stub |
| `pennylane_trotter` | PennyLane | Direct evolution | Stub |
| `qrack_trotter` | Qrack (Unitary Foundation) | GPU-accelerated | Stub |
| `mitiq_zne` | Mitiq (Unitary Foundation) | Error-mitigated wrapper | Stub |

### Integration — May/June 2026

| Task | Owner | Status | Issue |
|------|-------|--------|-------|
| AI orchestration design (MCP/RAG) | AS (Tirthankar) | Open | [#3](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/3) |
| MCP/RAG integration | AS | Pending | — |
| Spack recipe | SE | Pending | — |
| Documentation & examples | All | Ongoing | — |

### Release — June 15, 2026

| Deliverable | Description |
|-------------|-------------|
| `openqevo` v0.1.0 on PyPI | Pip-installable package |
| Spack recipe in `spack-packages/` | HPC-installable |
| At least 1 working adapter | External library integration |
| Context JSON for all methods | AI-ready metadata |
| CI/CD green | Lint + test + docs build |

## Long-term vision

openQEvo is the first library built using this model. If the pattern works,
future algorithm families from the Algorithms Thrust follow the same
architecture:

```mermaid
flowchart TB
    ALG["Algorithms Thrust\n(scientific code)"]

    subgraph SW ["Software Thrust Libraries"]
        OQEVO["openQEvo\n(evolution operators)"]
        FUTURE1["next library\n(next algorithm family)"]
        FUTURE2["another library\n(another family)"]
    end

    ALG --> OQEVO
    ALG -.-> FUTURE1
    ALG -.-> FUTURE2

    style ALG fill:#4a90d9,color:#fff
    style SW fill:#f5f5f5,color:#333
```

Each library follows the same architecture: Strategy + Registry + Adapters +
Context JSON. The Software Thrust provides the engineering; the Algorithms
Thrust provides the science.
