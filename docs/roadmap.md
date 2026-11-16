---
orphan: true
---

# OpenQEvo roadmap

_Last reviewed: 2026-11-16, against the local development checkout._

OpenQEvo remains a source-installable, pre-alpha prototype. The package's
`0.1.0` metadata does not establish a published release. Current work is on
`dev`; the project owner accepts the MPV scope and its evidence before merging
it into `main`. The [release checklist](release-checklist.md) gives the
remaining gates and the evidence required to close them.

## Current baseline

| Area | Repository evidence and remaining boundary |
| --- | --- |
| Package foundation | Registry, shared method interface, structured results, context schemas, tests, documentation, and CI are present. |
| Native methods | Exact evolution, first- and second-order Trotter, and qDRIFT are implemented. Algorithms Thrust approval of the approximation methods remains pending. |
| Additional methods | Krylov, interaction-picture, and annealing have experimental dense reference implementations. They do not establish scalable solvers or hardware execution. |
| Scientific contracts | Canonical Pauli Hamiltonians, sign and qubit ordering, result provenance, logical operations, and reference circuits are implemented and documented in [contracts](contracts.md). Dense references remain necessary for the archived small-system accuracy study. |
| Context and recommendations | The specialized quantum-evolution knowledge base preserves primary sources, extracted key points, curated wiki pages, selection rules, method contracts, and recommendation examples. Installed distributions carry the runtime records and their local evidence dependencies. AS contract review is open; retrieval and ranking belong to an external orchestrator. |
| Qiskit and PennyLane | Dedicated CI jobs install each adapter's dependencies and run its tests plus shared conformance cases. This is configured coverage; release evidence must come from the chosen revision's completed jobs. |
| Qrack | Adapter logic has fake-runtime coverage, and the local targeted suite passes ten tests including isolated real PyQrack CPU checks. A dedicated CPU CI job is configured; its hosted result remains pending. GPU/OpenCL validation remains open. |
| Benchmark artifact | The expanded software-frozen study archives controlled Pauli, spin-model, and mapped H₂ inputs, raw records, summaries, figure, and checksums. CI is configured to verify integrity. Scientific/statistical approval and exact execution-source provenance remain open. |
| Distribution | Wheel/sdist packaging includes method schemas and evidence-linked runtime context, with an installed-package smoke check in CI. A local Spack development recipe tracks upstream `main`, rather than the current `dev` checkout. An immutable version/checksum, authorized license, supported HPC validation, and submission are needed for upstream publication. No PyPI release is claimed. |
| Release stewardship | License/DOE authorization, citation metadata, acknowledgment wording, support policy, and distribution decisions remain open. |

## Next milestone: accept the software and its release boundary

The project owner coordinates the following work:

1. Review and integrate the current `dev` changes; run the required checks on
   the exact candidate revision and record their results.
2. Obtain scientific review of native Trotter and qDRIFT definitions, logical
   cost accounting, context claims, and the benchmark protocol. Document which
   experimental methods are included in the first release and their limits.
3. Record authorized license and acknowledgment decisions, citation metadata,
   public API compatibility commitments, and supported adapter/runtime versions.
4. Validate installation and the quick start from the built distribution in a
   clean environment; verify that installed method/context discovery works.
5. Publish documentation and a tagged release after the gates close. Choose
   PyPI and upstream Spack publication or explicitly defer either channel.

These steps close release gates. Method expansion is follow-on work and should
not substitute for completing review and packaging of the existing capability.

## Integration work with AS

[Issue #7](https://github.com/QSCSoftwareEcosystem/OpenQEvo/issues/7) remains
open for recommendation-schema and contract review, and
[Issue #3](https://github.com/QSCSoftwareEcosystem/OpenQEvo/issues/3) covers the
broader agentic design. The existing boundary assigns schemas, evidence,
metadata, and execution to OpenQEvo; retrieval, ranking, clarification, and
execution decisions belong to external AS/MCP/RAG. Record any changes to that
boundary before adding internal orchestration.

The {ref}`delivery ownership note <delivery-ownership>` assigns
implementation, context, validation, packaging, and release coordination to
the project owner. Historical HW, DS, and SE issue labels do not create new
external delivery dependencies. Algorithms Thrust scientific approval and
DOE license authorization still require the appropriate reviewers.

## Further scientific and execution work

Candidates after the release boundary is accepted include scalable Krylov
propagation, interaction-picture circuits, advanced annealing schedules,
hardware routing, GPU/OpenCL execution, and additional randomized methods.
Promote a method only with reviewed source, an explicit contract, matching
metadata, meaningful validation, and a reproducible example. Structured
results, logical circuit outputs, the development Spack recipe, and controlled
benchmark datasets already exist and are not future implementation promises.

## Manuscript and historical planning

The manuscript is developed separately in the private
[OpenQEvo-Manuscript repository](https://github.com/vicenley/OpenQEvo-Manuscript).
Authorship, venue, and submission review belong to that workstream. Software
release decisions and benchmark provenance still supply evidence it needs.

The original June 2026 release target was not completed. Future release dates
should be set only after owners accept the gates and their dependencies.
