# Roadmap

## Timeline

```mermaid
gantt
    title openQEvo development plan
    dateFormat YYYY-MM
    axisFormat %b %Y

    section Foundation
        Package structure & CI/CD (SE)        :done, se1, 2026-03, 2026-04
        Trotter placeholder implementation    :done, hw0, 2026-03, 2026-04

    section Phase 1 — Trotterization
        JSON schema design (DS)               :active, ds1, 2026-04, 2026-05
        Context files & how-to guides (HW)    :hw1, 2026-04, 2026-06
        Algorithms Thrust code integration    :alg1, 2026-04, 2026-06
        AI orchestration design (AS)          :as1, 2026-05, 2026-07

    section Phase 2 — Adapters
        Qiskit adapter                        :qk1, 2026-06, 2026-08
        PennyLane adapter                     :pl1, 2026-06, 2026-08
        Qrack adapter (Unitary Foundation)    :qr1, 2026-06, 2026-08
        Mitiq ZNE adapter (Unitary Foundation):mt1, 2026-07, 2026-09

    section Phase 3 — Scale
        Second method from Algorithms Thrust  :alg2, 2026-07, 2026-09
        Spack recipe (SE)                     :se2, 2026-08, 2026-09
        MCP/RAG integration (AS)              :as2, 2026-08, 2026-10

    section Phase 4 — openQSE v1.0
        Integration into openQSE release      :rel1, 2026-10, 2027-01
```

## Phases

### Phase 1 — Trotterization (current)

The first method integration, establishing the pattern for all future work.

| Task | Owner | Status |
|------|-------|--------|
| Package structure (`pyproject.toml`, `src/` layout) | SE | Done |
| Trotter placeholder implementation | openQEvo | Done |
| JSON schema for method context files | DS | [In progress (#2)](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/2) |
| Context files, how-to guides, test examples | HW | [Open (#4)](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4) |
| Replace placeholder with Algorithms Thrust code | HW + Algorithms | Pending |
| AI orchestration design (MCP/RAG) | AS | [Open (#3)](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/3) |
| CI/CD workflows | SE | [Open (#1)](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/1) |

### Phase 2 — Adapters

Wrap external libraries behind the same `EvolutionMethod` interface so
users can compare methods from different ecosystems.

| Adapter | Library | Type |
|---------|---------|------|
| `qiskit_trotter` | Qiskit | Direct evolution |
| `pennylane_trotter` | PennyLane | Direct evolution |
| `qrack_trotter` | Qrack (Unitary Foundation) | GPU-accelerated evolution |
| `mitiq_zne` | Mitiq (Unitary Foundation) | Error-mitigated wrapper |

### Phase 3 — Scale

Prove the model by integrating a second method from the Algorithms Thrust
(e.g., QDrift, LCU, or QSVT). If the architecture handles this cleanly,
the pattern is validated.

Also: Spack recipe for HPC deployment, and MCP/RAG integration for
AI-assisted method selection.

### Phase 4 — openQSE v1.0

Bundle openQEvo into the first openQSE release alongside outputs from the
other Software Thrust projects (Data Schema, Compilation Tools, etc.).

## Long-term vision

openQEvo is one component of a larger pattern. If the model succeeds:

```mermaid
flowchart TB
    ALG["Algorithms Thrust\n(scientific code)"]

    subgraph OPENQSE ["openQSE Ecosystem"]
        OQEVO["openQEvo\n(evolution operators)"]
        FUTURE1["openQ___\n(next algorithm family)"]
        FUTURE2["openQ___\n(another family)"]
    end

    ALG --> OQEVO
    ALG -.-> FUTURE1
    ALG -.-> FUTURE2

    style ALG fill:#4a90d9,color:#fff
    style OPENQSE fill:#f5f5f5,color:#333
```

Each `openQ___` library follows the same architecture: Strategy + Registry +
Adapters + Context JSON. The Software Thrust provides the engineering; the
Algorithms Thrust provides the science.
