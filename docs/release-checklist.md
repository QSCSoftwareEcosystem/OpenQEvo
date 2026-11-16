---
orphan: true
---

# OpenQEvo release checklist

_Prepared 2026-11-16 from the development checkout and repository configuration._

This checklist records the evidence needed to approve a release. It does not
certify today's working tree or repeat the historical test counts in older
status notes. Keep work on `dev` until the project owner accepts the MPV and
its validation evidence; publish from an identified, reviewed revision.

## Review and authorization

| Gate | Current evidence | Required completion and owner |
| --- | --- | --- |
| Native scientific methods | Trotter and qDRIFT implementations, analytic controls, shared convention cases, and context metadata exist. | Algorithms Thrust reviewers record approval or required corrections for ordering, sign, coefficients, qDRIFT sampling/angles, expected-channel claims, and formula-level cost accounting. Project owner incorporates corrections. |
| Experimental method scope | Dense Krylov, interaction-picture, and annealing references exist. | Project owner identifies supported public method names, parameters, and output modes, and preserves experimental limitations. Scientific reviewers assess any promoted claims. |
| Benchmark interpretation | [Protocol](../experiments/publication_study/protocol.json) says `scientific_review_status: pending`; the [bundle](https://github.com/QSCSoftwareEcosystem/OpenQEvo/tree/dev/experiments/publication_study) is software-frozen. | Scientific/statistical reviewers assess workloads, metrics, the selected initial state, 30-seed summaries, bootstrap intervals, and trajectory sizing. Archive integrity does not close this gate. |
| License and copyright | `pyproject.toml` still says `TBD`; no release license is established. | Project lead obtains DOE authorization and the applicable license/copyright decision. Add the authorized `LICENSE` and matching package metadata. Do not select legal wording by inference. |
| Citation and acknowledgment | Citation and approved funding wording remain unresolved. | Project owner confirms contributors and authors, adds `CITATION.cff`, and incorporates approved institutional/funding acknowledgment text. Add a DOI only when an actual archive record exists. |
| Compatibility and support | Versioned contracts exist; support commitments remain open. | Project owner declares the stable API, experimental surface, supported Python/framework/runtime versions, deprecation policy, and issue/support route. |

## Revision and artifact provenance

- [ ] Review all intended source, context, documentation, and packaging changes
  in the current working tree. Keep generated Graphify changes distinguishable
  from executable source and frozen scientific artifacts during review.
- [ ] Record the exact candidate Git SHA and environment. Run validation against
  that revision, rather than borrowing results from September's status notes.
- [ ] Preserve the original frozen study bundle. Its manifest hashes the
  protocol and files but does not identify the exact execution-source revision.
  Local commit `b33502b326ce9f5fbf180aa2e22bd9c79a006447` adds the runner and
  bundle; it is evidence of a source snapshot, not proof of the execution state.
  Recover the execution provenance or produce a separately versioned run from
  an identified source revision. Do not rewrite the old manifest to imply proof.
- [ ] Ensure the chosen source revision, protocol, environment, raw data,
  summaries, and figure-generation instructions are accessible to the intended
  release audience. Record which claims the approved artifact supports.

## Validation evidence

The [CI workflow](../.github/workflows/ci.yml) configures lint, Python
3.10–3.12 tests, dedicated Qiskit/PennyLane conformance jobs, real PyQrack CPU
checks, installed-package validation, bundle integrity verification, and a
strict Sphinx build. Check the completed runs for the release revision and
review unexpected skips. GPU/OpenCL Qrack claims still require their own
actual-runtime evidence; CPU and fake-runtime tests do not establish them.

From the repository root, record the command, source SHA, environment, and
result for the relevant checks:

```bash
python -m pytest -q
ruff check .
ruff format --check .
sphinx-build -W -b html docs docs/_build/html
python -m openqevo.study --verify-bundle experiments/publication_study/results-2026-09-01
```

For distribution checks, build an sdist and wheel, install the wheel, then run
the installed-package check from outside the checkout:

```bash
python -m pip install build
python -m build
python -m pip install dist/*.whl
cd /tmp
python /path/to/OpenQEvo/packaging/check_installed.py
```

The check requires imports to resolve to the installed package, validates its
bundled collection manifest and schemas, resolves local primary-source
evidence links, and executes the quick start and executable recommendation
examples. Source/editable installs continue using the live `context/` knowledge
base. Wheels preserve runtime metadata and its local evidence dependencies
under `openqevo/_context`; the original source knowledge base stays in place.
The packaged textual subset also includes source inventories, their linked
legacy Markdown papers, and two cited CSV discovery surveys. It excludes
PDF/image companions and conversion scratch under `raw_data/tmp/`; inventory
links to those recovery-only files resolve in the source checkout. Rendered
paper images and other acquisition material remain in the source corpus.
A discovery survey is a retrieval lead and does
not become scientific evidence because it is distributed with the package.

Local development evidence on 2026-11-16 includes a strict Sphinx build with
zero warnings and ten passing targeted Qrack adapter/runtime tests. An sdist
was rebuilt into a wheel, installed into a separate target, and checked from
`/tmp` while reusing the local scientific dependencies: all seven collection
records, 32 local key-point evidence links, method contexts, the quick start,
and executable recommendation examples passed. The packaged subset contained
123 text/JSON/CSV files (4,300,028 uncompressed bytes). These checks describe
the working development checkout; repeat or confirm them for the final
committed candidate and record hosted CI results before release.

- [ ] Resolve failures against the candidate, including registry/context
  alignment and recommendation execution. Report dependency skips by name.
- [ ] Run each supported adapter in an environment containing its declared
  dependency. Preserve native/framework sign, qubit-order, coefficient, time,
  and term-order conformance evidence.
- [ ] Record Qrack CPU validation independently from GPU/OpenCL support.
  If GPU/OpenCL evidence is unavailable, preserve the experimental limitation
  and avoid altering a contributor's GPU setup to meet the release checklist.
- [ ] Build an sdist and wheel from the candidate. Install the wheel outside
  the source checkout in a clean environment and execute the documented quick
  start, registry/context discovery, and one structured recommendation.
  Confirm packaged schemas/context are available wherever the API expects them.
- [ ] Check the built package metadata, dependency extras, README links,
  documentation, and examples against the accepted release scope.

## Distribution decisions

| Channel | Existing setup | Required decision/evidence |
| --- | --- | --- |
| Source and docs | Development repository, Sphinx docs, and CI configuration exist. | Project owner approves the release revision, merge to `main`, immutable tag/version, release notes, documentation hosting/version, and branch policy. |
| PyPI | Source installation and package metadata exist; no public package release is claimed. | Choose publish now or defer. If publishing, configure the selected credentials/trusted-publishing path, validate built artifacts, and publish the approved version only after authorization gates close. |
| Spack | [Local recipe](../spack/packages/py-openqevo/package.py) is a development `@main` recipe; it does not pin this `dev` checkout. | Choose submit or defer. For submission, add immutable release version/checksum, match the authorized license, validate supported HPC environments, and follow the destination repository's contribution process. Project owner coordinates this work; historical [Issue #1](https://github.com/QSCSoftwareEcosystem/OpenQEvo/issues/1) is closed and supplies no pending handoff. |
| Archival record | Frozen study files and their checksums exist locally. | Choose an archive destination, retain the accepted source/data/environment versions, obtain its real persistent identifier, and then update citation and availability metadata. |

## AS review and manuscript coordination

[Issue #7](https://github.com/QSCSoftwareEcosystem/OpenQEvo/issues/7) asks AS
reviewers to resolve optional query, Hamiltonian-feature, backend-constraint,
ranking, and provenance fields. OpenQEvo already owns context and selected
method execution, while the external orchestrator owns retrieval/ranking and
execution decisions. The project owner incorporates the agreed contract and
keeps examples aligned. [Issue #3](https://github.com/QSCSoftwareEcosystem/OpenQEvo/issues/3)
tracks the broader AS design. External orchestration is not a prerequisite for
the agreed software MPV.

The manuscript has its own private repository. Scientific/statistical review,
software provenance, licensing, citation, and approved acknowledgment decisions
must be reflected there before submission. Author and venue decisions remain
with the project owner and contributors.
