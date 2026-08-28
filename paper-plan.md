# OpenQEvo Publication Plan

Status: working draft
Last updated: 2026-08-27

## 1. Objective

Develop OpenQEvo into a publishable scientific software and methodology
contribution centered on reproducible comparison of deterministic and randomized
quantum time-evolution methods.

Working title:

> OpenQEvo: Reproducible Cross-Framework Benchmarking of Deterministic and
> Randomized Quantum Time Evolution

Central claim:

> OpenQEvo provides a common, provenance-aware implementation and benchmarking
> framework that enables fair comparisons of Trotter-Suzuki product formulas and
> qDRIFT, and characterizes the Hamiltonian and resource regimes in which each
> method is preferable.

The paper must not assume that qDRIFT or Trotter-Suzuki is universally better.
The scientific result is the experimentally supported crossover map and the
reproducible protocol used to obtain it.

## 2. Current Starting Point

OpenQEvo already provides:

- an `EvolutionMethod` interface;
- a registry for method discovery;
- exact, first-order Trotter, and second-order Trotter reference code;
- a registered qDRIFT dense-unitary baseline with deterministic sampling;
- Qiskit and PennyLane adapters;
- schema-validated method context and references;
- convergence, adapter, registry, qDRIFT, execution-contract, and context tests;
- structured method-selection context for use by Agentic Software without
  embedding agent orchestration in OpenQEvo;
- a versioned `H = X + Z` pilot with equal logical-operation budgets, 30 fixed
  qDRIFT seeds, append-only raw records, bootstrap uncertainty, checksums, and a
  generated convergence figure under `experiments/xz_pilot/`.

The following gaps prevent a strong publication:

- the native Trotter and qDRIFT implementations still require Algorithms
  Thrust scientific review;
- the API returns dense unitary matrices and therefore does not define a
  scalable execution boundary;
- the `H = X + Z` pilot is exploratory; the production benchmark grid,
  cross-framework conformance study, and broader archival dataset do not yet
  exist;
- the package is not publicly released and the license is still undecided;
- the current scientific context must be audited against primary sources.

## 3. Intended Contributions

The paper should claim the following concrete contributions:

1. A common method and result contract for quantum time-evolution algorithms,
   preserving method parameters, implementation provenance, random seeds, and
   execution costs.
2. Production-quality implementations of first- and second-order
   Trotter-Suzuki formulas and standard qDRIFT.
3. Cross-framework validation against Qiskit and PennyLane implementations.
4. A reproducible benchmark protocol that compares methods under equal logical
   evolution-operation budgets and, separately, equal compiled gate budgets.
5. An empirical study of how error and resource trade-offs depend on term count,
   coefficient norm, commutator structure, evolution time, and target accuracy.
6. An open benchmark dataset containing configurations, raw results,
   environments, seeds, and plotting scripts.

The registry, adapters, and context schema support these contributions, but are
not sufficient scientific novelty by themselves.

## 4. Research Questions

### RQ1: Accuracy scaling

Do the implementations reproduce the expected convergence behavior of
first-order Trotter, second-order Trotter, and qDRIFT across controlled
Hamiltonian families?

### RQ2: Resource-normalized performance

At equal numbers of Pauli evolution operations, when does qDRIFT obtain lower
simulation error than first- or second-order Trotter, and when does it not?

### RQ3: Hamiltonian structure

How do term count, coefficient distribution, Pauli weight, and commutator
structure affect the crossover between deterministic and randomized methods?

### RQ4: Framework consistency

Do native OpenQEvo, Qiskit, and PennyLane implementations produce equivalent
results after Hamiltonian conventions, term ordering, and cost accounting are
normalized?

### RQ5: Reproducibility

Can an independent user reproduce method selection, sampled qDRIFT sequences,
reported errors, and paper figures from archived configurations and seeds?

## 5. Hypotheses

These hypotheses guide the experiment but must be revised if the evidence does
not support them.

- H1: First-order and second-order Trotter exhibit their expected asymptotic
  convergence rates in the controlled noncommuting cases.
- H2: qDRIFT exhibits approximately inverse-budget convergence for the expected
  channel while retaining nonzero variation among individual trajectories.
- H3: At fixed `lambda * t`, qDRIFT becomes more competitive as term count and
  unfavorable Trotter commutator structure increase.
- H4: Trotter methods remain preferable for sufficiently structured, local, or
  weakly noncommuting Hamiltonians.
- H5: Cross-framework results agree within declared numerical tolerances after
  semantic and compilation differences are normalized.

The study must vary term count and `lambda = sum_j |h_j|` independently. The
standard statement that qDRIFT cost is independent of term count applies only
when other relevant quantities, especially `lambda`, are controlled.

## 6. Publication Scope

### Included

- exact evolution as a small-system reference;
- first-order Trotter-Suzuki;
- second-order symmetric Trotter-Suzuki;
- standard qDRIFT;
- OpenQEvo native implementations;
- Qiskit and PennyLane comparison adapters;
- ideal statevector or matrix validation;
- synthetic, lattice-model, and small chemistry Hamiltonians;
- deterministic benchmark configuration and result capture.

### Explicitly deferred

- Qrack support;
- Krylov, LCU, QSVT, and higher-order product formulas;
- AI method selection;
- QAppsWiki integration;
- hardware-noise and physical-device claims;
- Spack packaging;
- large-scale distributed execution.

Deferred work can become follow-on papers. It must not delay the minimum strong
contribution.

## 7. Required Software Work

### 7.1 Hamiltonian contract

Introduce a validated representation for Pauli-sum Hamiltonians. Each term must
record:

- coefficient, including its sign;
- Pauli word and qubit ordering;
- qubit count;
- source or benchmark identifier;
- optional physical units and mapping metadata.

The first release should support real Pauli coefficients. Existing dense-matrix
inputs may remain as a small-system compatibility path, but the benchmark must
use the same canonical Pauli representation across methods.

### 7.2 Evolution result contract

Replace the assumption that every method returns only a dense unitary with a
structured result that can carry:

- output representation, such as circuit, state, or unitary;
- method name and implementation version;
- normalized parameters;
- number of logical Pauli evolution operations;
- compiled one- and two-qubit gate counts when available;
- circuit depth when available;
- random seed and sampled term sequence for qDRIFT;
- runtime and environment metadata;
- warnings and approximation limitations.

Dense unitaries remain useful for exact small-system validation but cannot be
the only public execution mode.

### 7.3 Production Trotter-Suzuki implementations

- Replace the placeholder status with Algorithms Thrust-reviewed code.
- Define term-ordering semantics explicitly.
- Preserve first-order and symmetric second-order formulas.
- Avoid accidental cancellation or gate merging in logical cost counts.
- Add circuit or operation-sequence output in addition to dense validation.
- Record algorithm references and implementation provenance in context JSON.

### 7.4 Standard qDRIFT implementation

For a Pauli Hamiltonian

`H = sum_j h_j P_j`, with `lambda = sum_j |h_j|`,

the initial implementation should:

1. sample term `j` with probability `|h_j| / lambda`;
2. use `tau = lambda * t / N` for a budget of `N` sampled operations;
3. apply `exp(-i * sign(h_j) * tau * P_j)`;
4. accept an injected `numpy.random.Generator` or explicit seed;
5. preserve the complete sampled sequence in the result;
6. support generation of one trajectory and an ensemble of trajectories;
7. reject invalid coefficients, zero-norm Hamiltonians, and inconsistent Pauli
   dimensions with clear errors.

The API and paper must distinguish:

- error of an individual random trajectory;
- error of the empirical ensemble channel;
- sampling uncertainty from a finite number of trajectories;
- measurement-shot or hardware noise, which is outside the initial study.

### 7.5 Adapter normalization

- Verify sign, time, endianness, qubit-order, and coefficient conventions.
- Ensure adapters consume the canonical Hamiltonian representation.
- Define whether reported counts are before or after framework optimization.
- Pin supported Qiskit and PennyLane versions in benchmark environments.
- Record adapter and dependency versions in every result.

### 7.6 Benchmark runner

Add a command-line benchmark runner driven by versioned YAML or JSON
configurations. A run should emit an append-only structured record containing:

- benchmark and Hamiltonian identifiers;
- method and implementation;
- all parameters and random seeds;
- software and platform versions;
- raw accuracy and resource metrics;
- failure information;
- checksums for inputs and outputs.

Plotting scripts must read these records rather than rerun experiments
implicitly.

## 8. Benchmark Study Design

### 8.1 Fair comparison units

Use two complementary cost models:

1. **Algorithmic cost:** number of Pauli evolution operations. This is the
   primary comparison because it is portable across frameworks.
2. **Compiled cost:** one-qubit gates, entangling gates, and depth after lowering
   to a declared common basis. This captures Pauli weight and compilation
   effects.

Wall-clock time is a secondary implementation metric. It must not replace the
algorithmic cost comparison because framework overheads differ.

For second-order Trotter, adjacent repeated operations may merge. Report both
the formula-level count and the optimized compiled count.

### 8.2 Benchmark families

#### A. Controlled synthetic Pauli Hamiltonians

Generate instances that vary independently where possible:

- qubit count;
- term count;
- `lambda`;
- Pauli-weight distribution;
- coefficient distribution;
- commutator-graph density;
- locality and interaction range.

Include commuting instances as controls and noncommuting instances with known
or measurable commutator structure.

#### B. Physics models

- one-dimensional transverse-field Ising model;
- Heisenberg XXZ or XXX model;
- at least one longer-range or disordered spin model.

Use documented boundary conditions, parameter ranges, initial states, and
observables.

#### C. Quantum chemistry

- H2 as a minimal verification case;
- LiH or another small molecular Hamiltonian as a nontrivial case;
- one larger case for statevector-only scaling if resources permit.

Record geometry, basis, active space, fermion-to-qubit mapping, symmetry
reduction, and coefficient-generation software. Archive the resulting Pauli
Hamiltonians so regenerating chemistry inputs is not required to reproduce the
study.

### 8.3 Parameter factors

The pilot study should determine feasible final ranges for:

- qubits `n`;
- terms `L`;
- evolution time `t`;
- `lambda * t`;
- Pauli evolution budget `N`;
- number of qDRIFT trajectories;
- target error thresholds.

Exact-unitary metrics should be limited to sizes where they are computationally
responsible. Larger cases should use exact state evolution or high-accuracy
classical references for selected initial states.

### 8.4 Accuracy metrics

Report a subset appropriate to each scale:

- normalized operator error for small systems;
- state infidelity for declared initial states;
- trace distance between exact and empirical ensemble output states;
- error in physically meaningful observables;
- cost required to reach declared error thresholds;
- qDRIFT trajectory mean, variance, quantiles, and confidence intervals.

Do not report single-trajectory qDRIFT error as if it were the expected-channel
error. Do not claim diamond-norm performance unless it is actually computed or
rigorously bounded for the reported case.

### 8.5 Statistical protocol

- Predeclare the final benchmark grid after the pilot.
- Use fixed, archived seed lists rather than selecting favorable runs.
- Use enough independent qDRIFT trajectories to stabilize confidence intervals;
  start with at least 30 in the pilot and increase based on variance analysis.
- Report distributions and uncertainty, not only best or mean values.
- Use bootstrap confidence intervals where analytic intervals are unsuitable.
- Keep failed and timed-out runs in the raw dataset with terminal status.
- Separate exploratory plots from confirmatory paper figures.

### 8.6 Confound controls

- Hold `lambda` fixed when testing dependence on term count.
- Hold the logical evolution-operation budget fixed for primary method
  comparisons.
- Define a canonical Trotter term order and run a separate order-sensitivity
  analysis.
- Use the same Hamiltonian, initial state, time, and observable definitions
  across all implementations.
- Disable framework optimizations for formula-level validation, then enable and
  report them separately for compiled-cost analysis.
- Record numerical precision and linear-algebra backend.

## 9. Scientific Validation Gates

### Gate 1: Unit correctness

- Pauli parsing and coefficient normalization tests pass.
- All generated operations are unitary within tolerance.
- Seeded qDRIFT runs reproduce the same sampled sequence.
- Invalid Hamiltonians fail deterministically.

### Gate 2: Analytic controls

- Exact evolution agrees with closed-form one- and two-qubit cases.
- Trotter is exact for selected commuting decompositions.
- First- and second-order convergence slopes match expectations in controlled
  asymptotic regimes.
- qDRIFT empirical ensemble error decreases with operation budget.

### Gate 3: Cross-framework agreement

- Native, Qiskit, and PennyLane results agree for a shared conformance suite.
- Any differences caused by decomposition or gate optimization are documented.

### Gate 4: Benchmark reproducibility

- A clean environment regenerates a representative raw result and figure.
- Two independent runs with the same configuration and seeds agree.
- CI runs a small benchmark smoke suite; full experiments remain an archived
  research workflow.

### Gate 5: Scientific review

- Algorithms Thrust reviewers approve method definitions and tests.
- Statistical design receives review before full production runs.
- All context claims and references are checked against primary sources.

## 10. Planned Results and Visuals

The paper should target the following figures and tables:

1. OpenQEvo architecture and reproducibility boundary.
2. Convergence validation for first-order Trotter, second-order Trotter, and
   qDRIFT.
3. Error versus logical Pauli evolution budget across benchmark families.
4. Cost to target accuracy for each method.
5. Crossover map over `lambda * t`, term count, and commutator structure.
6. qDRIFT trajectory distributions and ensemble convergence.
7. Formula-level versus compiled gate costs.
8. Cross-framework conformance table.
9. Reproducibility and artifact table listing configurations, environments,
   data, and checksums.

Figures must display uncertainty and failed regions, not only successful
method regimes.

## 11. Paper Outline

1. **Introduction** - method-selection problem, reproducibility gap, and paper
   contributions.
2. **Background and related work** - product formulas, qDRIFT, existing SDK
   implementations, and quantum simulation benchmark practice.
3. **OpenQEvo design** - method contract, Hamiltonian representation, result
   provenance, adapters, and reproducibility model.
4. **Implemented methods** - production Trotter-Suzuki and qDRIFT definitions.
5. **Benchmark methodology** - workloads, cost models, metrics, statistical
   protocol, and confound controls.
6. **Validation** - analytic controls and cross-framework conformance.
7. **Results** - scaling, crossover regimes, uncertainty, and compiled costs.
8. **Discussion** - interpretation, practical method-selection guidance, and
   limits of generalization.
9. **Limitations** - ideal simulation, finite problem sizes, backend/compiler
   dependence, and methods not included.
10. **Reproducibility and availability** - release, DOI, data, environments,
    and commands.
11. **Conclusion**.

## 12. Work Packages and Exit Criteria

### WP0: Scientific alignment

Status: pending scientific ownership and review.

- Confirm paper claim and authorship.
- Assign Algorithms Thrust reviewers for Trotter-Suzuki and qDRIFT.
- Audit primary references and remove unsupported claims.

Exit: signed-off method specifications and benchmark questions.

### WP1: Core scientific data model

Status: partial. Method metadata and recommendation execution contracts exist;
the canonical Pauli Hamiltonian and scalable evolution-result contracts remain.

- Implement canonical Pauli Hamiltonian representation.
- Implement structured evolution results and provenance.
- Preserve a compatibility path for existing examples where practical.

Exit: conformance tests pass for native and adapter methods.

### WP2: Production methods

Status: partial. Trotter and seeded qDRIFT baselines and tests exist, but method
review, scalable outputs, and full analytic validation remain open.

- Replace placeholder Trotter implementations.
- Implement seeded standard qDRIFT and trajectory ensembles.
- Add context JSON, documentation, examples, and tests.

Exit: analytic validation gates pass.

### WP3: Benchmark infrastructure

Status: pilot implementation complete. The `experiments/xz_pilot/` workflow is
configuration-driven, writes immutable JSON Lines records, derives summaries
and plots from those records, and emits checksums. General benchmark families
and compiled-cost capture remain open.

- Implement configuration-driven benchmark execution.
- Implement metric, cost, environment, and raw-result capture.
- Add deterministic dataset and plotting workflows.

Exit: one command reproduces a pilot result bundle and figure.

### WP4: Pilot study

Status: in progress. The controlled `H = X + Z` case is complete with 30 seeded
qDRIFT trajectories; spin-model, chemistry, and variance-sizing work remain.

- Run small synthetic, spin-model, and chemistry cases.
- Estimate qDRIFT variance and computational requirements.
- Finalize benchmark grid, tolerances, and seed counts.

Exit: frozen production protocol and documented resource estimate.

### WP5: Production study

- Execute the frozen benchmark grid.
- Validate and archive raw data.
- Generate paper figures without manually editing result values.

Exit: complete, checksummed result archive and reviewed figure set.

### WP6: Paper and release

- Write and internally review the manuscript.
- Select an approved open-source license.
- Add `CITATION.cff`, authorship, changelog, and contribution metadata.
- Publish a tagged OpenQEvo release and package artifacts.
- Archive software, benchmark configurations, raw data, and figures with DOI.

Exit: manuscript and reproducibility artifact are submission-ready.

## 13. Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| The paper appears to be only SDK adapters | Lead with the controlled scientific study and crossover findings. |
| qDRIFT is compared using an inappropriate single-trajectory metric | Report trajectory distributions and empirical ensemble-channel metrics separately. |
| qDRIFT term-count independence is overstated | Control `lambda` independently and state the theoretical conditions explicitly. |
| Dense-unitary outputs prevent meaningful scaling | Add circuit/state result modes and restrict operator metrics to small systems. |
| Frameworks apply different optimizations | Separate formula-level and compiled-cost comparisons and record all settings. |
| Chemistry input generation is not reproducible | Archive canonical Pauli Hamiltonians plus generation metadata. |
| Benchmark choices favor one method | Predeclare the final grid, include commuting and strongly noncommuting controls, and retain all runs. |
| Literature context contains unverified secondary claims | Audit every paper claim against primary sources before submission. |
| Scope expands to unrelated methods and platforms | Keep deferred features outside the submission critical path. |

## 14. Definition of Paper-Ready

The work is ready for submission only when:

- native Trotter-Suzuki code is no longer a placeholder;
- qDRIFT is implemented, registered, documented, and scientifically reviewed;
- the public API supports a scalable result representation;
- the cross-framework conformance suite passes;
- the final benchmark protocol is frozen and fully executed;
- uncertainty and confounds are reported transparently;
- raw data and figure-generation code are archived;
- an approved license, citation metadata, tagged release, and DOI exist;
- every main claim in the manuscript maps to a test, benchmark result, or primary
  reference.

## 15. Immediate Next Actions

1. Review this plan, the Trotter/qDRIFT baselines, and the `H = X + Z` pilot
   with the Algorithms Thrust; identify scientific owners and reviewers.
2. Validate the pilot's equal-budget accounting, trajectory versus empirical
   ensemble metrics, bootstrap procedure, and fixed 30-seed schedule.
3. Write the canonical Pauli Hamiltonian and scalable evolution-result
   contracts while preserving compatibility with the pilot records.
4. Convert the research questions and remaining validation gates into
   repository issues with explicit owners and exit criteria.
5. Extend the controlled synthetic pilot to vary term count, `lambda`, Pauli
   weight, and commutator structure independently.
6. Add native/Qiskit/PennyLane conformance cases before freezing the production
   benchmark grid.
