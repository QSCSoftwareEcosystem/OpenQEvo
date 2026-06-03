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
        GitHub Actions CI (lint + test)        :done, ci1, 2026-03-28, 2026-03-28
        Draft JSON schema + context files      :done, ds0, 2026-03-28, 2026-03-28

    section Adapters (done)
        Qiskit adapter                         :done, qk1, 2026-03-28, 2026-03-28
        PennyLane adapter                      :done, pl1, 2026-03-28, 2026-03-28

    section Core (Apr–May)
        Refine JSON schema with DS             :active, ds1, 2026-04-01, 2026-04-18
        Context files & how-to guides (HW)     :ctx1, 2026-04-07, 2026-05-02
        Algorithms Thrust code integration     :alg1, 2026-04-07, 2026-05-16
        AI orchestration design (AS)           :as1, 2026-05-01, 2026-05-22

    section Release (May–Jun)
        Qrack adapter (Unitary Foundation)     :done, qr1, 2026-05-01, 2026-05-22
        Spack recipe                           :se2, 2026-05-15, 2026-05-29
        Documentation & examples               :doc1, 2026-05-22, 2026-06-12

    section Release
        v0.1.0 release                         :milestone, rel1, 2026-06-15, 0d
```

## Task tracker

### Foundation — done

| Task | Status |
|------|--------|
| Package structure (`src/` layout, `pyproject.toml`) | Done |
| Strategy + Registry + Adapter architecture | Done |
| Trotter placeholder (1st, 2nd order, exact) | Done |
| GitHub Actions CI (lint + test, Python 3.10-3.12) | Done |
| Draft JSON schema for context files | Done |
| Context JSON for trotter_s1, trotter_s2, exact | Done |
| 19 core tests passing | Done |
| README, CONTRIBUTING.md, docs/ | Done |

### Adapters — done

| Adapter | Library | Status | Tests |
|---------|---------|--------|-------|
| `qiskit_trotter` | Qiskit | **Working** | 9 passing |
| `pennylane_trotter` | PennyLane | **Working** | 9 passing |
| `qrack_trotter` | Qrack (Unitary Foundation) | **Experimental** | 7 passing + real PyQrack CPU validation |

### Core — April/May 2026

| Task | Owner | Status | Issue |
|------|-------|--------|-------|
| Refine JSON schema with DS feedback | DS (Thomas) | In progress | [#2](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/2) |
| Context JSON refinement + how-to guides | HW (Zack) | Open | [#4](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4) |
| Replace placeholder with Algorithms Thrust code | HW + Algorithms | Pending | — |
| AI orchestration design (MCP/RAG) | AS (Tirthankar) | Open | [#3](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/3) |

### Release — May/June 2026

| Task | Owner | Status |
|------|-------|--------|
| Qrack adapter implementation | Unitary Foundation collab | Implemented; GPU/OpenCL validation pending host runtime |
| Spack recipe | SE | Pending |
| Documentation & examples | All | Ongoing |

### Release — June 15, 2026

| Deliverable | Description |
|-------------|-------------|
| `openqevo` v0.1.0 on PyPI | Pip-installable package |
| Spack recipe in `spack-packages/` | HPC-installable |
| 2 working adapters (Qiskit, PennyLane) + experimental Qrack | External library integration |
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
