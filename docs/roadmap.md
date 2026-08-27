# OpenQEvo roadmap

_Last reviewed: 2026-08-25_

> [!IMPORTANT]
> The original June 2026 release target was not completed. The package contains
> `0.1.0` version metadata, but OpenQEvo is still a source-installable,
> pre-alpha prototype. This roadmap uses verified release gates instead of
> presenting the historical target as a current commitment.

## Current baseline

| Area | Verified repository state |
| --- | --- |
| Package foundation | `src/` layout, `pyproject.toml`, registry, method contract, tests, and CI are present. |
| Native methods | Exact evolution, first-/second-order Trotter references, and a qDRIFT randomized baseline are available; the approximation methods still need Algorithms Thrust review. |
| Context | Schema-validated metadata exists for native and adapter methods, with selection rules and executable recommendation examples. Research notes alone are not registered package methods. |
| Qiskit | Adapter and 9 dependency-conditional tests are implemented. |
| PennyLane | Adapter and 9 dependency-conditional tests are implemented. |
| Qrack | Experimental optional adapter and 7 fake-runtime tests are implemented; GPU/OpenCL validation remains host-dependent. |
| Distribution | Editable source installation works; no PyPI release or Spack recipe is claimed. |
| Release stewardship | License, citation metadata, approved acknowledgment, and stable-support policy remain open. |

## First release objective

Deliver a licensed, source-traceable OpenQEvo release whose scientific methods,
software behavior, and limitations have been reviewed and can be reproduced
from a clean environment.

### Scientific gates

- Replace or formally approve the reference Trotter and qDRIFT implementations
  with Algorithms Thrust-reviewed code.
- Define Hamiltonian term ordering, sign, time, qubit-order, and coefficient
  conventions explicitly.
- Audit registered context claims and references against primary sources.
- Validate native, Qiskit, PennyLane, and Qrack results with one shared
  conformance suite.
- Archive one representative benchmark configuration, raw result, environment,
  and generated figure.

### Software and release gates

- Select a license and add `LICENSE` plus matching `pyproject.toml` metadata.
- Add `CITATION.cff` and approved QSC funding acknowledgment language.
- Decide which public API elements receive compatibility guarantees.
- Exercise every supported optional adapter explicitly in continuous
  integration rather than relying on dependency skips.
- Test the documented source installation and quick start in a clean
  environment.
- Publish versioned documentation and a tagged release.
- Decide whether the first release is published to PyPI and whether a Spack
  recipe is ready or deferred.

## Planned phases

### Phase 1 — establish the release boundary

The immediate phase is about trust, not method count:

1. close the scientific-review and license blockers;
2. normalize method and adapter semantics;
3. publish one reproducible validation artifact;
4. make supported adapters visible in CI;
5. issue the first tagged, documented release.

### Phase 2 — expand the scientific method set

qDRIFT now provides an executable randomized baseline but still needs the same
scientific review and conformance evidence as the product formulas. Candidate
expansion includes Krylov-subspace approaches, interaction-picture methods,
annealing, and additional product formulas. A method becomes a supported
package capability only after it has:

- a reviewed implementation;
- a registered context record;
- unit, analytic-control, and regression tests;
- a reproducible example;
- documented applicability and limitations.

Research notes under `context/` do not by themselves indicate an implemented
or supported method.

### Phase 3 — scale the execution and integration model

Longer-term work may include:

- structured result objects that carry method parameters, provenance, costs,
  seeds, warnings, and environment metadata;
- circuit or state outputs in addition to dense unitaries;
- validated GPU/OpenCL execution through Qrack and other accelerated adapters;
- Spack and quantum-HPC deployment support;
- QSC workflow, catalog, and agent integrations;
- controlled benchmark datasets and archival releases.

These are directional goals, not current package capabilities.

## Cross-project contributions

| Group | Release contribution |
| --- | --- |
| Algorithms Thrust | Review scientific definitions, implementations, and validation cases |
| HW — Hybrid Workflows | Provide representative examples, context guidance, and integration use cases |
| DS — Data Schema | Refine context and future result/provenance contracts |
| AS — Agentic Software | Define future machine-readable discovery and orchestration needs |
| SE — Software Engineering | Own packaging, tests, CI, documentation, release, and sustainability practices |

## Historical planning context

The initial roadmap targeted a `0.1.0` release on 2026-06-15 with Qiskit and
PennyLane adapters, context JSON, documentation, PyPI distribution, and Spack
packaging. The foundation and adapter implementations remain useful outputs of
that plan, but PyPI/Spack publication, Algorithms Thrust scientific review,
Qrack GPU/OpenCL validation, licensing, and release stewardship were not
completed.

Future dates should be added only after owners accept the release gates and
dependencies above.
