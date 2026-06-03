[Skip to main content](#main-content)

Back to top

`Ctrl`+`K`

[![Mitiq 1.0.0 documentation - Home](../_static/mitiq-logo.png)
![Mitiq 1.0.0 documentation - Home](../_static/mitiq-logo.png)](../index.html)

* [Users Guide](guide.html)
* [Examples](../examples/examples.html)
* [API-doc](../apidoc.html)
* [Contributing](../toc_contributing.html)
* [Changelog](../changelog.html)
* More
  + [References](../bibliography.html)

Search
`Ctrl`+`K`

* [Source Repository](https://github.com/unitaryfoundation/mitiq "Source Repository")

Search
`Ctrl`+`K`

* [Users Guide](guide.html)
* [Examples](../examples/examples.html)
* [API-doc](../apidoc.html)
* [Contributing](../toc_contributing.html)
* [Changelog](../changelog.html)
* [References](../bibliography.html)

* [Source Repository](https://github.com/unitaryfoundation/mitiq "Source Repository")

Section Navigation

* [Core Concepts](core-concepts.html)
  + [Frontends and Backends](frontends-backends.html)
  + [Executors](executors.html)
  + [Observables](observables.html)
  + [Calibration](calibrators.html)
  + [Benchmarking Circuits](benchmarking-circuits.html)
  + [Resource Requirements](resource-requirements.html)
* Zero-Noise Extrapolation
  + [How do I use ZNE?](zne-1-intro.html)
  + [When should I use ZNE?](zne-2-use-case.html)
  + [What additional options are available when using ZNE?](zne-3-options.html)
  + [What happens when I use ZNE?](zne-4-low-level.html)
  + [What is the theory behind ZNE?](zne-5-theory.html)
* [Probabilistic Error Cancellation](pec.html)
  + [How do I use PEC?](pec-1-intro.html)
  + [When should I use PEC?](pec-2-use-case.html)
  + [What additional options are available in PEC?](pec-3-options.html)
  + [What happens when I use PEC?](pec-4-low-level.html)
  + [What is the theory behind PEC?](pec-5-theory.html)
* [Clifford Data Regression](cdr.html)
  + [How do I use CDR?](cdr-1-intro.html)
  + [When should I use CDR?](cdr-2-use-case.html)
  + [What additional options are available in CDR?](cdr-3-options.html)
  + [What happens when I use CDR?](cdr-4-low-level.html)
  + [What is the theory behind CDR?](cdr-5-theory.html)
* [Digital Dynamical Decoupling](ddd.html)
  + [How do I use DDD?](ddd-1-intro.html)
  + [When should I use DDD?](ddd-2-use-case.html)
  + [What additional options are available when using DDD?](ddd-3-options.html)
  + [What happens when I use DDD?](ddd-4-low-level.html)
  + [What is the theory behind DDD?](ddd-5-theory.html)
* [Layerwise Richardson Extrapolation](lre.html)
  + [How do I use LRE?](lre-1-intro.html)
  + [When should I use LRE?](lre-2-use-case.html)
  + [What additional options are available when using LRE?](lre-3-options.html)
  + [What happens when I use LRE?](lre-4-low-level.html)
  + [What is the theory behind LRE?](lre-5-theory.html)
* [Readout-Error Mitigation](rem.html)
  + [How do I use REM?](rem-1-intro.html)
  + [When should I use REM?](rem-2-use-case.html)
  + [What additional options are available when using REM?](rem-3-options.html)
  + [What happens when I use REM?](rem-4-low-level.html)
  + [What is the theory behind REM?](rem-5-theory.html)
* [Twirled Readout Error eXtinction](trex.html)
  + [How do I use TREX?](trex-1-intro.html)
  + [When should I use TREX?](trex-2-use-case.html)
  + [What additional options are available when using TREX?](trex-3-options.html)
  + [What happens when I use TREX?](trex-4-low-level.html)
  + [What is the theory behind TREX?](trex-5-theory.html)
* [Quantum Subspace Expansion](qse.html)
  + [How do I use QSE?](qse-1-intro.html)
  + [When should I use QSE?](qse-2-use-case.html)
  + [What additional options are available in QSE?](qse-3-options.html)
  + [What happens when I use QSE?](qse-4-low-level.html)
  + [What is the theory behind QSE?](qse-5-theory.html)
* [Pauli Twirling](pt.html)
  + [How do I use PT?](pt-1-intro.html)
  + [When should I use PT?](pt-2-use-case.html)
  + [What additional options are available when using PT?](pt-3-options.html)
  + [What happens when I use PT?](pt-4-low-level.html)
  + [What is the theory behind Pauli Twirling?](pt-5-theory.html)
* [About Error Mitigation](error-mitigation.html)
* [Glossary](glossary.html)

* [Virtual Distillation](vd.html)
  + [What is VD?](vd-1-intro.html)
  + [When should I use VD?](vd-2-use-case.html)
  + [What additional options are available when using VD?](vd-3-options.html)
  + [What happens when I use VD?](vd-4-low-level.html)
  + [What is the theory behind VD?](vd-5-theory.html)
* [Probabilistic Error Amplification](pea.html)
  + [How do I use PEA?](pea-1-intro.html)
  + [When should I use PEA?](pea-2-use-case.html)
  + [What additional options are available in PEA?](pea-3-options.html)
  + [What happens when I use PEA?](pea-4-low-level.html)
  + [What is the theory behind PEA?](pea-5-theory.html)
* [Classical Shadows](shadows.html)
  + [How Do I Use Classical Shadows Estimation?](shadows-1-intro.html)
  + [What is the theory behind Classical Shadow Estimation](shadows-5-theory.html)

* [Users Guide](guide.html)
* Zero-Noise Extrapolation

# Zero-Noise Extrapolation[#](#zero-noise-extrapolation "Link to this heading")

Zero-noise extrapolation (ZNE) is an error mitigation technique in which an expectation
value is computed at different noise levels and, as a second step, the ideal
expectation value is inferred by extrapolating the measured results to the zero-noise
limit (see the section [What is the theory behind ZNE?](zne-5-theory.html)).

[![../_images/zne_workflow2_steps.png](../_images/zne_workflow2_steps.png)](../_images/zne_workflow2_steps.png)

The diagram shows the workflow of the zero noise extrapolation (ZNE) in Mitiq.[#](#figzne-overview "Link to this image")

You can get started with ZNE in Mitiq with the following sections of the user guide:

* [How do I use ZNE?](zne-1-intro.html)
* [When should I use ZNE?](zne-2-use-case.html)
* [What additional options are available when using ZNE?](zne-3-options.html)
* [What happens when I use ZNE?](zne-4-low-level.html)
* [What is the theory behind ZNE?](zne-5-theory.html)

Here are some examples on how to use ZNE in Mitiq:

* [Zero-noise extrapolation with Qiskit on IBMQ backends](../examples/ibmq-backends.html)
* [Zero-noise extrapolation with Pennylane on IBMQ backends](../examples/pennylane-ibmq-backends.html)
* [Zero-noise extrapolation with Braket on the IonQ backend](../examples/zne-braket-ionq.html)
* [Zero-noise extrapolation of the energy landscape of a variational circuit with Cirq on a simulator](../examples/simple-landscape-cirq.html)

You can find many more in the **[Examples](../examples/examples.html)** section of the documentation.

[previous

Resource Requirements](resource-requirements.html "previous page")
[next

How do I use ZNE?](zne-1-intro.html "next page")

### This Page

* [Show Source](../_sources/guide/zne.md.txt)

© Copyright 2020 - 2026 Unitary Foundation.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1.