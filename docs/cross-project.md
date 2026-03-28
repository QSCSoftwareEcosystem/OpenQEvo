# Cross-project workflow

openQEvo is a collaboration across all five Software Thrust projects and
the Algorithms Thrust. This document describes how the pieces fit together.

## Workflow

```mermaid
flowchart LR
    subgraph ALGO ["Algorithms Thrust"]
        SRC["Scientific scripts\n(raw research code)"]
    end

    subgraph SW ["Software Thrust"]
        HW["HW — Hybrid Workflows\nContext files, how-to\nguides, test examples"]
        DS["DS — Data Schema\nJSON schema for\nmethod context"]
        AS["AS — Agentic Software\nAI orchestration\nlayer (MCP/RAG)"]
        SE["SE — Software Engineering\nPackaging, CI/CD\ndocs, testing"]
    end

    subgraph OUT ["openQEvo"]
        LIB["Packaged library\nwith structured context"]
    end

    SRC -->|"raw code"| HW
    DS -->|"schema"| HW
    HW -->|"methods +\ncontext JSON"| LIB
    SE -->|"CI/CD +\npackaging"| LIB
    AS -->|"AI tooling"| LIB

    click HW "https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4"
    click DS "https://github.com/QSCSoftwareThrust/OpenQEvo/issues/2"
    click AS "https://github.com/QSCSoftwareThrust/OpenQEvo/issues/3"
    click SE "https://github.com/QSCSoftwareThrust/OpenQEvo/issues/1"

    style ALGO fill:#4a90d9,color:#fff
    style SW fill:#f5f5f5,color:#333
    style OUT fill:#2ecc71,color:#fff
```

## Responsibilities

### HW — Hybrid Workflows ([Issue #4](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/4))

**What they deliver:**
- One JSON context file per evolution method (metadata, limitations,
  applicable Hamiltonians, complexity, references)
- How-to guides: when to use each strategy and on what types of Hamiltonians
- Test examples for each method
- Integration of the actual Algorithms Thrust code into `methods/`

**Key personnel:** Zack Windom (context and examples), Daniel Claudino (QC)

### DS — Data Schema ([Issue #2](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/2))

**What they deliver:**
- JSON schema defining the structure of method context files
- Validation tooling for context files
- Alignment with the broader openQSE data schema

**Key personnel:** Thomas Naughton, Samuel Stein

**Related:** [DataSchema RFC #5 — trotterization schema requirements](https://github.com/QSCSoftwareThrust/DataSchema/issues/5)

### AS — Agentic Software ([Issue #3](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/3))

**What they deliver:**
- Design for AI-assisted method selection using the structured context
- MCP or RAG integration so AI agents can discover and recommend methods
- Orchestration layer connecting openQEvo to hybrid workflows

**Key personnel:** Tirthankar Ghosal

**Dependency:** Needs the JSON schema (DS, issue #2) to be defined first.

### SE — Software Engineering ([Issue #1](https://github.com/QSCSoftwareThrust/OpenQEvo/issues/1))

**What they deliver:**
- Python package structure (`src/` layout, `pyproject.toml`) — done
- CI/CD workflows (GitHub Actions: lint, test, docs build)
- Documentation infrastructure (Sphinx or MkDocs)
- Branch protection rules and PR review setup
- Spack recipe for HPC deployment (Phase 3)

**Key personnel:** Seth Johnson

## Dependency chain

```mermaid
flowchart TD
    SE1["SE: Package structure"] -->|done| DS1["DS: JSON schema design"]
    SE1 --> HW1["HW: Context files + examples"]
    DS1 --> HW1
    DS1 --> AS1["AS: AI orchestration design"]
    HW1 --> AS1
    HW1 --> ALGT["Algorithms Thrust:\ncode integration"]
    ALGT --> PHASE2["Phase 2: Adapters"]
    AS1 --> PHASE3["Phase 3: MCP/RAG"]

    style SE1 fill:#2ecc71,color:#fff
    style DS1 fill:#f39c12,color:#fff
    style HW1 fill:#f39c12,color:#fff
    style AS1 fill:#e74c3c,color:#fff
    style ALGT fill:#e74c3c,color:#fff
    style PHASE2 fill:#95a5a6,color:#fff
    style PHASE3 fill:#95a5a6,color:#fff
```

Legend: green = done, orange = in progress, red = blocked/waiting, gray = future
