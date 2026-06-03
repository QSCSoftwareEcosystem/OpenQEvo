[Skip to main content](#main-content)

Back to top

`Ctrl`+`K`

[![Mitiq 1.0.0 documentation - Home](_static/mitiq-logo.png)
![Mitiq 1.0.0 documentation - Home](_static/mitiq-logo.png)](index.html)

* [Users Guide](guide/guide.html)
* [Examples](examples/examples.html)
* API-doc
* [Contributing](toc_contributing.html)
* [Changelog](changelog.html)
* More
  + [References](bibliography.html)

Search
`Ctrl`+`K`

* [Source Repository](https://github.com/unitaryfoundation/mitiq "Source Repository")

Search
`Ctrl`+`K`

* [Users Guide](guide/guide.html)
* [Examples](examples/examples.html)
* API-doc
* [Contributing](toc_contributing.html)
* [Changelog](changelog.html)
* [References](bibliography.html)

* [Source Repository](https://github.com/unitaryfoundation/mitiq "Source Repository")

* API-doc

# API-doc[#](#module-mitiq "Link to this heading")

## Error-Mitigation Techniques[#](#error-mitigation-techniques "Link to this heading")

### Clifford Data Regression[#](#clifford-data-regression "Link to this heading")

#### Clifford Data Regression (High-Level Tools)[#](#module-mitiq.cdr.cdr "Link to this heading")

API for using Clifford Data Regression (CDR) error mitigation.

mitiq.cdr.cdr.cdr\_decorator(*observable=None*, *\**, *simulator*, *num\_training\_circuits=10*, *fraction\_non\_clifford=0.1*, *fit\_function=<function linear\_fit\_function>*, *num\_fit\_parameters=None*, *scale\_factors=(1*, *)*, *scale\_noise=<function fold\_gates\_at\_random>*, *\*\*kwargs*)[[source]](_modules/mitiq/cdr/cdr.html#cdr_decorator)[#](#mitiq.cdr.cdr.cdr_decorator "Link to this definition")
:   Decorator which adds clifford data regression (CDR) mitigation
    to an executor function, i.e., a function which executes a quantum circuit
    with an arbitrary backend and returns the CDR estimate of the ideal
    expectation value associated to the input circuit.

    Parameters:
    :   * **executor** – Executes a circuit and returns a QuantumResult.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of.
          If None, the executor must return an expectation value. Otherwise
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **simulator** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit without noise and returns a
          QuantumResult. For CDR to be efficient, the simulator must
          be able to efficiently simulate near-Clifford circuits.
        * **num\_training\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of training circuits to be used in the
          mitigation.
        * **fraction\_non\_clifford** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The fraction of non-Clifford gates to be
          substituted in the training circuits.
        * **fit\_function** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The function to map noisy to exact data. Takes array of
          noisy and data and parameters returning a float. See
          `cdr.linear_fit_function` for an example.
        * **num\_fit\_parameters** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of parameters the fit\_function takes.
        * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function for scaling the noise of a quantum circuit.
        * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) –

          Factors by which to scale the noise.

          + When 1.0 is the only scale factor, the method is known as CDR.
          + Note: When scale factors larger than 1.0 are provided, the method
            is known as “variable-noise CDR.”
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")) –

          Available keyword arguments are:

          + method\_select (string): Specifies the method used to select the
            non-Clifford gates to replace when constructing the near-Clifford
            training circuits. Can be ‘uniform’ or ‘gaussian’.
          + method\_replace (string): Specifies the method used to replace the
            selected non-Clifford gates with a Clifford when constructing the
            near-Clifford training circuits. Can be ‘uniform’, ‘gaussian’, or
            ‘closest’.
          + sigma\_select (float): Width of the Gaussian distribution used for
            `method_select='gaussian'`.
          + sigma\_replace (float): Width of the Gaussian distribution used
            for `method_replace='gaussian'`.
          + random\_state (int): Seed for sampling.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`, [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`, [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

mitiq.cdr.cdr.execute\_with\_cdr(*circuit*, *executor*, *observable=None*, *\**, *simulator*, *num\_training\_circuits=10*, *fraction\_non\_clifford=0.1*, *fit\_function=<function linear\_fit\_function>*, *num\_fit\_parameters=None*, *scale\_factors=(1*, *)*, *scale\_noise=<function fold\_gates\_at\_random>*, *\*\*kwargs*)[[source]](_modules/mitiq/cdr/cdr.html#execute_with_cdr)[#](#mitiq.cdr.cdr.execute_with_cdr "Link to this definition")
:   Function for the calculation of an observable from some circuit of
    interest to be mitigated with CDR (or vnCDR) based on
    Ref. [[19](bibliography.html#id17 "Piotr Czarnik, Andrew Arrasmith, Patrick J. Coles, and Lukasz Cincio. Error mitigation with Clifford quantum-circuit data. Quantum, 5:592, (2021). URL: http://dx.doi.org/10.22331/q-2021-11-26-592, doi:10.22331/q-2021-11-26-592.")] and Ref. [[6](bibliography.html#id41 "Angus Lowe, Max Hunter Gordon, Piotr Czarnik, Andrew Arrasmith, Patrick J. Coles, and Lukasz Cincio. Unified approach to data-driven quantum error mitigation. Phys. Rev. Research, 3:033098, (2021). URL: https://link.aps.org/doi/10.1103/PhysRevResearch.3.033098, doi:10.1103/PhysRevResearch.3.033098.")].

    The circuit of interest must be compiled in the native basis of the IBM
    quantum computers, that is {Rz, sqrt(X), CNOT}, or such that all the
    non-Clifford gates are contained in the Rz rotations.

    The observable/s to be calculated should be input as an array or a list of
    arrays representing the diagonal of the observables to be measured. Note
    these observables MUST be diagonal in z-basis measurements corresponding to
    the circuit of interest.

    Returns mitigated observables list of raw observables (at noise scale
    factors).

    This function returns the mitigated observable/s.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Quantum program to execute with error mitigation.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit and returns a QuantumResult.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of.
          If None, the executor must return an expectation value. Otherwise
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **simulator** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit without noise and returns a
          QuantumResult. For CDR to be efficient, the simulator must
          be able to efficiently simulate near-Clifford circuits.
        * **num\_training\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of training circuits to be used in the
          mitigation.
        * **fraction\_non\_clifford** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The fraction of non-Clifford gates to be
          substituted in the training circuits.
        * **fit\_function** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The function to map noisy to exact data. Takes array of
          noisy and data and parameters returning a float. See
          `cdr.linear_fit_function` for an example.
        * **num\_fit\_parameters** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of parameters the fit\_function takes.
        * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function for scaling the noise of a quantum circuit.
        * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) –

          Factors by which to scale the noise.

          + When 1.0 is the only scale factor, the method is known as CDR.
          + Note: When scale factors larger than 1.0 are provided, the method
            is known as “variable-noise CDR.”
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")) –

          Available keyword arguments are:

          + method\_select (string): Specifies the method used to select the
            non-Clifford gates to replace when constructing the near-Clifford
            training circuits. Can be ‘uniform’ or ‘gaussian’.
          + method\_replace (string): Specifies the method used to replace the
            selected non-Clifford gates with a Clifford when constructing the
            near-Clifford training circuits. Can be ‘uniform’, ‘gaussian’, or
            ‘closest’.
          + sigma\_select (float): Width of the Gaussian distribution used for
            `method_select='gaussian'`.
          + sigma\_replace (float): Width of the Gaussian distribution used
            for `method_replace='gaussian'`.
          + random\_state (int): Seed for sampling.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

mitiq.cdr.cdr.mitigate\_executor(*executor*, *observable=None*, *\**, *simulator*, *num\_training\_circuits=10*, *fraction\_non\_clifford=0.1*, *fit\_function=<function linear\_fit\_function>*, *num\_fit\_parameters=None*, *scale\_factors=(1*, *)*, *scale\_noise=<function fold\_gates\_at\_random>*, *\*\*kwargs*)[[source]](_modules/mitiq/cdr/cdr.html#mitigate_executor)[#](#mitiq.cdr.cdr.mitigate_executor "Link to this definition")
:   Returns a clifford data regression (CDR) mitigated version of
    the input ‘executor’.

    The input executor executes a circuit with an arbitrary backend and
    produces an expectation value (without any error mitigation). The returned
    executor executes the circuit with the same backend but uses clifford
    data regression to produce the CDR estimate of the ideal expectation
    value associated to the input circuit.

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit and returns a QuantumResult.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of.
          If None, the executor must return an expectation value. Otherwise
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **simulator** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit without noise and returns a
          QuantumResult. For CDR to be efficient, the simulator must
          be able to efficiently simulate near-Clifford circuits.
        * **num\_training\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of training circuits to be used in the
          mitigation.
        * **fraction\_non\_clifford** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The fraction of non-Clifford gates to be
          substituted in the training circuits.
        * **fit\_function** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The function to map noisy to exact data. Takes array of
          noisy and data and parameters returning a float. See
          `cdr.linear_fit_function` for an example.
        * **num\_fit\_parameters** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of parameters the fit\_function takes.
        * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function for scaling the noise of a quantum circuit.
        * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) –

          Factors by which to scale the noise.

          + When 1.0 is the only scale factor, the method is known as CDR.
          + Note: When scale factors larger than 1.0 are provided, the method
            is known as “variable-noise CDR.”
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")) –

          Available keyword arguments are:

          + method\_select (string): Specifies the method used to select the
            non-Clifford gates to replace when constructing the near-Clifford
            training circuits. Can be ‘uniform’ or ‘gaussian’.
          + method\_replace (string): Specifies the method used to replace
            the selected non-Clifford gates with a Clifford when constructing
            the near-Clifford training circuits. Can be ‘uniform’, ‘gaussian’
            , or ‘closest’.
          + sigma\_select (float): Width of the Gaussian distribution used for
            `method_select='gaussian'`.
          + sigma\_replace (float): Width of the Gaussian distribution used
            for `method_replace='gaussian'`.
          + random\_state (int): Seed for sampling.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

#### Clifford Training Data[#](#module-mitiq.cdr.clifford_training_data "Link to this heading")

Functions for mapping circuits to (near) Clifford circuits.

mitiq.cdr.clifford\_training\_data.generate\_training\_circuits(*circuit*, *num\_training\_circuits*, *fraction\_non\_clifford*, *method\_select='uniform'*, *method\_replace='closest'*, *random\_state=None*, *\*\*kwargs*)[[source]](_modules/mitiq/cdr/clifford_training_data.html#generate_training_circuits)[#](#mitiq.cdr.clifford_training_data.generate_training_circuits "Link to this definition")
:   Returns a list of (near) Clifford circuits obtained by replacing (some)
    non-Clifford gates in the input circuit by Clifford gates.
    The way in which non-Clifford gates are selected to be replaced is
    determined by `method_select` and `method_replace`.
    In the Clifford Data Regression (CDR) method
    [[19](bibliography.html#id17 "Piotr Czarnik, Andrew Arrasmith, Patrick J. Coles, and Lukasz Cincio. Error mitigation with Clifford quantum-circuit data. Quantum, 5:592, (2021). URL: http://dx.doi.org/10.22331/q-2021-11-26-592, doi:10.22331/q-2021-11-26-592.")], data generated from these circuits is used
    as a training set to learn the effect of noise.

    Parameters:
    :   * **circuit** (`Circuit`) – A circuit of interest assumed to be compiled into the gate
          set {Rz, sqrt(X), CNOT}, or such that all the non-Clifford gates
          are contained in the Rz rotations.
        * **num\_training\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of circuits in the returned training set.
        * **fraction\_non\_clifford** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (approximate) fraction of non-Clifford
          gates in each returned circuit.
        * **method\_select** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – Method by which non-Clifford gates are selected to be
          replaced by Clifford gates. Options are ‘uniform’ or ‘gaussian’.
        * **method\_replace** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – Method by which selected non-Clifford gates are
          replaced by Clifford gates. Options are ‘uniform’, ‘gaussian’ or
          ‘closest’.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling.
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")) –

          Available keyword arguments are:

          + sigma\_select (float): Width of the Gaussian distribution used for
            `method_select='gaussian'`.
          + sigma\_replace (float): Width of the Gaussian distribution used
            for `method_replace='gaussian'`.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Circuit`]

#### Data Regression[#](#module-mitiq.cdr.data_regression "Link to this heading")

The data regression portion of Clifford data regression.

mitiq.cdr.data\_regression.linear\_fit\_function(*x\_data*, *params*)[[source]](_modules/mitiq/cdr/data_regression.html#linear_fit_function)[#](#mitiq.cdr.data_regression.linear_fit_function "Link to this definition")
:   Returns \(y(x) = a\_1 x\_1 + \cdots + a\_n x\_n + b\).

    Parameters:
    :   * **x\_data** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – The independent variables $x\_1, …, x\_n$. In CDR, these are
          nominally the noisy expectation values to perform regression on.
        * **params** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Parameters $a\_1, …, a\_n, b$ of the linear fit. Note the $b$
          parameter is the intercept of the fit.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

mitiq.cdr.data\_regression.linear\_fit\_function\_no\_intercept(*x\_data*, *params*)[[source]](_modules/mitiq/cdr/data_regression.html#linear_fit_function_no_intercept)[#](#mitiq.cdr.data_regression.linear_fit_function_no_intercept "Link to this definition")
:   Returns \(y(x) = a\_1 x\_1 + \cdots + a\_n x\_n\).

    Parameters:
    :   * **x\_data** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – The independent variables $x\_1, …, x\_n$. In CDR, these are
          nominally the noisy expectation values to perform regression on.
        * **params** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Parameters $a\_1, …, a\_n$ of the linear fit.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

See Ref. [[19](bibliography.html#id17 "Piotr Czarnik, Andrew Arrasmith, Patrick J. Coles, and Lukasz Cincio. Error mitigation with Clifford quantum-circuit data. Quantum, 5:592, (2021). URL: http://dx.doi.org/10.22331/q-2021-11-26-592, doi:10.22331/q-2021-11-26-592.")] for more details on these methods.

### Digital Dynamical Decoupling[#](#digital-dynamical-decoupling "Link to this heading")

#### Digital Dynamical Decoupling (High-Level Tools)[#](#module-mitiq.ddd.ddd "Link to this heading")

High-level digital dynamical decoupling (DDD) tools.

mitiq.ddd.ddd.combine\_results(*results*)[[source]](_modules/mitiq/ddd/ddd.html#combine_results)[#](#mitiq.ddd.ddd.combine_results "Link to this definition")
:   Averages over the DDD results to get the expectation value from using
    DDD.

    Parameters:
    :   **results** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Results as obtained from running circuits.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value estimated with DDD.

mitiq.ddd.ddd.construct\_circuits(*circuit*, *rule*, *rule\_args=None*, *num\_trials=1*)[[source]](_modules/mitiq/ddd/ddd.html#construct_circuits)[#](#mitiq.ddd.ddd.construct_circuits "Link to this definition")
:   Generates a list of circuits with DDD sequences inserted.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The quantum circuit to be modified with DD.
        * **rule** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – A function that takes as main argument a slack length (i.e. the
          number of idle moments) of a slack window (i.e. a single-qubit idle
          window in a circuit) and returns the DDD sequence of gates to be
          applied in that window.
        * **rule\_args** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – An optional dictionary of keyword arguments for `rule`.
        * **num\_trials** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of circuits to generate with DDD insertions.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   A list of circuits with DDD inserted.

mitiq.ddd.ddd.ddd\_decorator(*observable=None*, *\**, *rule*, *rule\_args=None*, *num\_trials=1*, *full\_output=False*)[[source]](_modules/mitiq/ddd/ddd.html#ddd_decorator)[#](#mitiq.ddd.ddd.ddd_decorator "Link to this definition")
:   Decorator which adds an error-mitigation layer based on digital
    dynamical decoupling (DDD) to an executor function, i.e., a function which
    executes a quantum circuit with an arbitrary backend and returns a
    `QuantumResult` (e.g. an expectation value).

    Parameters:
    :   * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor must return an expectation value. Otherwise,
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **rule** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – A function that takes as main argument a slack length (i.e. the
          number of idle moments) of a slack window (i.e. a single-qubit idle
          window in a circuit) and returns the DDD sequence of gates to be
          applied in that window. Mitiq provides standard built-in rules
          that can be directly imported from mitiq.ddd.rules.
        * **rule\_args** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – An optional dictionary of keyword arguments for rule.
        * **num\_trials** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of independent experiments to average over.
          A number larger than 1 can be useful to average over multiple
          applications of a rule returning non-deterministic DDD sequences.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False only the mitigated expectation value is returned.
          If True a dictionary containing all DDD data is returned too.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]]]

    Returns:
    :   The error-mitigating decorator to be applied to an executor function.

mitiq.ddd.ddd.execute\_with\_ddd(*circuit*, *executor*, *observable=None*, *\**, *rule*, *rule\_args=None*, *num\_trials=1*, *full\_output=False*)[[source]](_modules/mitiq/ddd/ddd.html#execute_with_ddd)[#](#mitiq.ddd.ddd.execute_with_ddd "Link to this definition")
:   Estimates the error-mitigated expectation value associated to the
    input circuit, via the application of digital dynamical decoupling (DDD).

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit to execute with DDD.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `QuantumResult` (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the `executor` must return an expectation value. Otherwise,
          the `QuantumResult` returned by `executor` is used to compute
          the expectation of the observable.
        * **rule** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – A function that takes as main argument a slack length (i.e. the
          number of idle moments) of a slack window (i.e. a single-qubit idle
          window in a circuit) and returns the DDD sequence of gates to be
          applied in that window. Mitiq provides standard built-in rules
          that can be directly imported from `mitiq.ddd.rules`.
        * **rule\_args** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – An optional dictionary of keyword arguments for `rule`.
        * **num\_trials** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of independent experiments to average over.
          A number larger than 1 can be useful to average over multiple
          applications of a rule returning non-deterministic DDD sequences.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If `False` only the mitigated expectation value is
          returned. If `True` a dictionary containing all DDD data is
          returned too.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   The tuple `(ddd_value, ddd_data)` where `ddd_value` is the
        expectation value estimated with DDD and `ddd_data` is a dictionary
        containing all the raw data involved in the DDD process (e.g. the
        circuit filled with DDD sequences). If `full_output` is false,
        only `ddd_value` is returned.

mitiq.ddd.ddd.mitigate\_executor(*executor*, *observable=None*, *\**, *rule*, *rule\_args=None*, *num\_trials=1*, *full\_output=False*)[[source]](_modules/mitiq/ddd/ddd.html#mitigate_executor)[#](#mitiq.ddd.ddd.mitigate_executor "Link to this definition")
:   Returns a modified version of the input ‘executor’ which is
    error-mitigated with digital dynamical decoupling (DDD).

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A function that executes a circuit and returns the
          unmitigated QuantumResult (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor must return an expectation value. Otherwise,
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **rule** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – A function that takes as main argument a slack length (i.e. the
          number of idle moments) of a slack window (i.e. a single-qubit idle
          window in a circuit) and returns the DDD sequence of gates to be
          applied in that window. Mitiq provides standard built-in rules
          that can be directly imported from mitiq.ddd.rules.
        * **rule\_args** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – An optional dictionary of keyword arguments for rule.
        * **num\_trials** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of independent experiments to average over.
          A number larger than 1 can be useful to average over multiple
          applications of a rule returning non-deterministic DDD sequences.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False only the mitigated expectation value is returned.
          If True a dictionary containing all DDD data is returned too.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]]

    Returns:
    :   The error-mitigated version of the input executor.

#### Insertion[#](#module-mitiq.ddd.insertion "Link to this heading")

Tools to determine slack windows in circuits and to insert DDD sequences.

mitiq.ddd.insertion.get\_slack\_matrix\_from\_circuit\_mask(*mask*)[[source]](_modules/mitiq/ddd/insertion.html#get_slack_matrix_from_circuit_mask)[#](#mitiq.ddd.insertion.get_slack_matrix_from_circuit_mask "Link to this definition")
:   Given a circuit mask matrix \(A\), e.g., the output of
    `_get_circuit_mask()`, returns a slack matrix \(B\),
    where \(B\_{i,j} = t\) if the position \(A\_{i,j}\) is the
    initial element of a sequence of \(t\) zeros (from left to right).

    Parameters:
    :   **mask** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`int64`]]) – The mask matrix of a quantum circuit.

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`int64`]]

    Returns:
    :   The matrix of slack lengths.

mitiq.ddd.insertion.insert\_ddd\_sequences(*circuit*, *rule*)[[source]](_modules/mitiq/ddd/insertion.html#insert_ddd_sequences)[#](#mitiq.ddd.insertion.insert_ddd_sequences "Link to this definition")
:   Returns the circuit with DDD sequences applied according to the input
    rule.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The QPROGRAM circuit to be modified with DDD sequences.
        * **rule** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], `Circuit`]) – The rule determining what DDD sequences should be applied.
          A set of built-in DDD rules can be imported from
          `mitiq.ddd.rules`.

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

    Returns:
    :   The circuit with DDD sequences added.

#### Rules[#](#module-mitiq.ddd.rules.rules "Link to this heading")

Built-in rules determining what DDD sequence should be applied in a given
slack window.

mitiq.ddd.rules.rules.general\_rule(*slack\_length*, *gates*, *spacing=-1*)[[source]](_modules/mitiq/ddd/rules/rules.html#general_rule)[#](#mitiq.ddd.rules.rules.general_rule "Link to this definition")
:   Returns a digital dynamical decoupling sequence, based on inputs.

    Parameters:
    :   * **slack\_length** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Length of idle window to fill.
        * **spacing** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – How many identity spacing gates to apply between dynamical
          decoupling gates, as a non-negative int. Negative int corresponds
          to default. Defaults to maximal spacing that fits a single sequence
          in the given slack window.
        * **gates** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Gate`]) – A list of single qubit Cirq gates to build the rule. E.g. [X, X]
          is the xx sequence, [X, Y, X, Y] is the xyxy sequence.
          - Note: To repeat the sequence, specify a repeated gateset.

    Return type:
    :   `Circuit`

    Returns:
    :   A digital dynamical decoupling sequence, as a Cirq circuit.

    Example

    When `slack_length = 8` and `gates = [X, X]` the spacing defaults
    to 2 and the rule returns the sequence:

    ```
    ──I──I──X──I──I──X──I──I──
    ```

    When `slack_length = 9` and `gates [X, Y, X, Y]` the spacing
    defaults to 1 and the rule returns the sequence:

    ```
    ──I──X──I──Y──I──X──I──Y──I──
    ```

mitiq.ddd.rules.rules.repeated\_rule(*slack\_length*, *gates*)[[source]](_modules/mitiq/ddd/rules/rules.html#repeated_rule)[#](#mitiq.ddd.rules.rules.repeated_rule "Link to this definition")
:   Returns a general digital dynamical decoupling sequence that repeats
    until the slack is filled without spacing, up to a complete repetition.

    Parameters:
    :   * **slack\_length** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Length of idle window to fill.
        * **gates** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Gate`]) – A list of single qubit Cirq gates to build the rule. E.g. [X, X]
          is the xx sequence, [X, Y, X, Y] is the xyxy sequence.

    Return type:
    :   `Circuit`

    Returns:
    :   A repeated digital dynamical decoupling sequence, as a Cirq circuit.

    Warning

    Where [`general_rule()`](#mitiq.ddd.rules.rules.general_rule "mitiq.ddd.rules.rules.general_rule") fills a slack window with a single
    sequence, this rule attempts to fill every moment with sequence
    repetitions (up to a complete repetition of the gate set).
    E.g. given `slack_length = 8` and `gates = [X, Y, X, Y]`, this
    rule returns the sequence:

    ```
    ──X──Y──X──Y──X──Y──X──Y──
    ```

mitiq.ddd.rules.rules.xx(*slack\_length*, *spacing=-1*)[[source]](_modules/mitiq/ddd/rules/rules.html#xx)[#](#mitiq.ddd.rules.rules.xx "Link to this definition")
:   Returns an XX digital dynamical decoupling sequence, based on inputs.

    Parameters:
    :   * **slack\_length** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Length of idle window to fill.
        * **spacing** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – How many identity spacing gates to apply between dynamical
          decoupling gates, as a non-negative int. Negative int corresponds
          to default. Defaults to maximal spacing that fits a single sequence
          in the given slack window.
          E.g. given slack\_length = 8 the spacing defaults to 2 and this
          rule returns the sequence:
          ──I──I──X──I──I──X──I──I──.

    Return type:
    :   `Circuit`

    Returns:
    :   An XX digital dynamical decoupling sequence, as a Cirq circuit.

mitiq.ddd.rules.rules.xyxy(*slack\_length*, *spacing=-1*)[[source]](_modules/mitiq/ddd/rules/rules.html#xyxy)[#](#mitiq.ddd.rules.rules.xyxy "Link to this definition")
:   Returns an XYXY digital dynamical decoupling sequence, based on inputs.

    Parameters:
    :   * **slack\_length** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Length of idle window to fill.
        * **spacing** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – How many identity spacing gates to apply between dynamical
          decoupling gates, as a non-negative int. Negative int corresponds
          to default. Defaults to maximal spacing that fits a single sequence
          in the given slack window.
          E.g. given slack\_length = 9 the spacing defaults to 1 and this
          rule returns the sequence:
          ──I──X──I──Y──I──X──I──Y──I──.

    Return type:
    :   `Circuit`

    Returns:
    :   An XYXY digital dynamical decoupling sequence, as a Cirq circuit.

mitiq.ddd.rules.rules.yy(*slack\_length*, *spacing=-1*)[[source]](_modules/mitiq/ddd/rules/rules.html#yy)[#](#mitiq.ddd.rules.rules.yy "Link to this definition")
:   Returns a YY digital dynamical decoupling sequence, based on inputs.

    Parameters:
    :   * **slack\_length** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Length of idle window to fill.
        * **spacing** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – How many identity spacing gates to apply between dynamical
          decoupling gates, as a non-negative int. Negative int corresponds
          to default. Defaults to maximal spacing that fits a single sequence
          in the given slack window.
          E.g. given slack\_length = 8 the spacing defaults to 2 and
          this rule returns the sequence:
          ──I──I──Y──I──I──Y──I──I──.

    Return type:
    :   `Circuit`

    Returns:
    :   An YY digital dynamical decoupling sequence, as a Cirq circuit.

### Layerwise Richardson Extrapolation[#](#module-mitiq.lre.lre "Link to this heading")

Extrapolation methods for Layerwise Richardson Extrapolation (LRE)

mitiq.lre.lre.combine\_results(*results*, *circuit*, *degree*, *fold\_multiplier*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/lre.html#combine_results)[#](#mitiq.lre.lre.combine_results "Link to this definition")
:   Computes the error-mitigated expectation value associated to the
    input results from executing the scaled circuits and using the multivariate
    richardson coeffecients, via the application of Layerwise Richardson
    Extrapolation (LRE).

    Parameters:
    :   * **results** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – An array storing the results of running the scaled circuits.
        * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Circuit to be scaled.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap value required for unitary folding which
          is used to generate the scale factor vectors.
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value estimated with LRE.

mitiq.lre.lre.construct\_circuits(*circuit*, *degree*, *fold\_multiplier*, *folding\_method=<function fold\_gates\_at\_random>*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/lre.html#construct_circuits)[#](#mitiq.lre.lre.construct_circuits "Link to this definition")
:   Given a circuit, degree, fold\_multiplier, folding\_method, and
    :   num\_chunks, outputs a list of circuits that will be used in LRE.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Circuit to be scaled.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap value required for unitary folding which
          is used to generate the scale factor vectors.
        * **folding\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Unitary folding method. Default is
          [`mitiq.zne.scaling.folding.fold_gates_at_random()`](#mitiq.zne.scaling.folding.fold_gates_at_random "mitiq.zne.scaling.folding.fold_gates_at_random").
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   The scaled circuits using the
        [`mitiq.lre.multivariate_scaling.layerwise_folding.multivariate_layer_scaling()`](#mitiq.lre.multivariate_scaling.layerwise_folding.multivariate_layer_scaling "mitiq.lre.multivariate_scaling.layerwise_folding.multivariate_layer_scaling").

mitiq.lre.lre.execute\_with\_lre(*circuit*, *executor*, *degree*, *fold\_multiplier*, *observable=None*, *folding\_method=<function fold\_gates\_at\_random>*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/lre.html#execute_with_lre)[#](#mitiq.lre.lre.execute_with_lre "Link to this definition")
:   Defines the executor required for Layerwise Richardson
    Extrapolation as defined in [[30](bibliography.html#id59 "Vincent Russo and Andrea Mari. Quantum error mitigation by layerwise richardson extrapolation. (2024). arXiv:2402.04000.")].

    Note that this method only works for the multivariate extrapolation
    methods. It does not allows a user to choose which layers in the input
    circuit will be scaled.

    See also

    If you would prefer to choose the layers for unitary
    folding, use [`mitiq.zne.scaling.layer_scaling.get_layer_folding()`](#mitiq.zne.scaling.layer_scaling.get_layer_folding "mitiq.zne.scaling.layer_scaling.get_layer_folding")
    instead.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Circuit to be scaled.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit and returns a float
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap value required for unitary folding which
          is used to generate the scale factor vectors.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
          `None`, the `executor` must return an expectation value.
          Otherwise, the `DensityMatrix` or `Bitstrings` returned by
          `executor` is used to compute the expectation of the observable.
        * **folding\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Unitary folding method. Default is
          [`mitiq.zne.scaling.folding.fold_gates_at_random()`](#mitiq.zne.scaling.folding.fold_gates_at_random "mitiq.zne.scaling.folding.fold_gates_at_random").
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   Error-mitigated expectation value

mitiq.lre.lre.lre\_decorator(*degree*, *fold\_multiplier*, *observable=None*, *folding\_method=<function fold\_gates\_at\_random>*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/lre.html#lre_decorator)[#](#mitiq.lre.lre.lre_decorator "Link to this definition")
:   Decorator which adds an error-mitigation layer based on
    layerwise richardson extrapolation (LRE).

    Parameters:
    :   * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **which** (*fold\_multiplier Scaling gap value required for unitary folding*) – is used to generate the scale factor vectors.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
          `None`, the `executor` must return an expectation value.
          Otherwise, the `DensityMatrix` or `Bitstrings` returned by
          `executor` is used to compute the expectation of the observable.
        * **folding\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Unitary folding method. Default is
          [`mitiq.zne.scaling.folding.fold_gates_at_random()`](#mitiq.zne.scaling.folding.fold_gates_at_random "mitiq.zne.scaling.folding.fold_gates_at_random").
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"))

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

    Returns:
    :   Error-mitigated decorator.

mitiq.lre.lre.mitigate\_executor(*executor*, *degree*, *fold\_multiplier*, *observable=None*, *folding\_method=<function fold\_gates\_at\_random>*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/lre.html#mitigate_executor)[#](#mitiq.lre.lre.mitigate_executor "Link to this definition")
:   Returns a modified version of the input executor which is
    error-mitigated with layerwise richardson extrapolation (LRE).

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit and returns a float.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **which** (*fold\_multiplier Scaling gap value required for unitary folding*) – is used to generate the scale factor vectors.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
          `None`, the `executor` must return an expectation value.
          Otherwise, the `DensityMatrix` or `Bitstrings` returned by
          `executor` is used to compute the expectation of the observable.
        * **folding\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]) – Unitary folding method. Default is
          [`mitiq.zne.scaling.folding.fold_gates_at_random()`](#mitiq.zne.scaling.folding.fold_gates_at_random "mitiq.zne.scaling.folding.fold_gates_at_random").
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"))

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   Error-mitigated version of the circuit executor.

Functions for layerwise folding of input circuits to allow for multivariate
extrapolation as defined in [[30](bibliography.html#id59 "Vincent Russo and Andrea Mari. Quantum error mitigation by layerwise richardson extrapolation. (2024). arXiv:2402.04000.")].

mitiq.lre.multivariate\_scaling.layerwise\_folding.get\_scale\_factor\_vectors(*input\_circuit*, *degree*, *fold\_multiplier*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/multivariate_scaling/layerwise_folding.html#get_scale_factor_vectors)[#](#mitiq.lre.multivariate_scaling.layerwise_folding.get_scale_factor_vectors "Link to this definition")
:   Returns the patterned scale factor vectors required for multivariate
    extrapolation.

    Parameters:
    :   * **input\_circuit** (`Circuit`) – Quantum circuit to be scaled.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap required by unitary folding.
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of
          circuit layers (default, each layer is a separate chunk).

    Returns:
    :   A vector of scale factors where each
        :   component in the vector corresponds to the layer in the input
            circuit.

    Return type:
    :   scale\_factor\_vectors

mitiq.lre.multivariate\_scaling.layerwise\_folding.multivariate\_layer\_scaling(*input\_circuit*, *degree*, *fold\_multiplier*, *num\_chunks=None*, *folding\_method=<function fold\_gates\_at\_random>*)[#](#mitiq.lre.multivariate_scaling.layerwise_folding.multivariate_layer_scaling "Link to this definition")
:   Defines the noise scaling function required for Layerwise Richardson
    Extrapolation as defined in [[30](bibliography.html#id59 "Vincent Russo and Andrea Mari. Quantum error mitigation by layerwise richardson extrapolation. (2024). arXiv:2402.04000.")].

    Note that this method only works for the multivariate extrapolation
    methods. It does not allows a user to choose which layers in the input
    circuit will be scaled.

    See also

    If you would prefer to choose the layers for unitary
    folding, use [`mitiq.zne.scaling.layer_scaling.get_layer_folding()`](#mitiq.zne.scaling.layer_scaling.get_layer_folding "mitiq.zne.scaling.layer_scaling.get_layer_folding")
    instead.

    Parameters:
    :   * **input\_circuit** (`Circuit`) – Circuit to be scaled.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap required by unitary folding.
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).
        * **folding\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Unitary folding method. Default is
          `fold_gates_at_random()`.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Circuit`]

    Returns:
    :   Multiple folded variations of the input circuit.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – When the degree for the multinomial is not greater than or
        equal to 1; when the fold multiplier to scale the circuit is
        greater than/equal to 1; when the number of chunks for a
        large circuit is 0 or when the number of chunks in a circuit is
        greater than the number of layers in the input circuit.

Functions for multivariate richardson extrapolation as defined in
[[30](bibliography.html#id59 "Vincent Russo and Andrea Mari. Quantum error mitigation by layerwise richardson extrapolation. (2024). arXiv:2402.04000.")].

mitiq.lre.inference.multivariate\_richardson.multivariate\_richardson\_coefficients(*input\_circuit*, *degree*, *fold\_multiplier*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/inference/multivariate_richardson.html#multivariate_richardson_coefficients)[#](#mitiq.lre.inference.multivariate_richardson.multivariate_richardson_coefficients "Link to this definition")
:   Defines the function to find the linear combination coefficients from the
    sample matrix as required for multivariate extrapolation (defined in
    [[30](bibliography.html#id59 "Vincent Russo and Andrea Mari. Quantum error mitigation by layerwise richardson extrapolation. (2024). arXiv:2402.04000.")]).

    We use the sample matrix to find the constants of linear combination
    $c = (c\_1, c\_2, …, c\_M)$ associated with a known vector of noisy
    expectation values \(z = (\langle O(λ\_1)\rangle,
    \langle O(λ\_2)\rangle, ..., \langle O(λ\_M)\rangle)^T\).

    The coefficients are found through the ratio of the determinants of $M\_i$
    and the sample matrix. The new matrix $M\_i$ is defined by replacing the ith
    row of the sample matrix with $e\_1 = (1, 0, 0,…, 0)$.

    Parameters:
    :   * **input\_circuit** (`Circuit`) – Circuit to be scaled.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap required by unitary folding.
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the number of circuit
          layers (default, each layer is a separate chunk).

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   List of the evaluated monomial basis terms using the scale factor
        :   vectors.

mitiq.lre.inference.multivariate\_richardson.sample\_matrix(*input\_circuit*, *degree*, *fold\_multiplier*, *num\_chunks=None*)[[source]](_modules/mitiq/lre/inference/multivariate_richardson.html#sample_matrix)[#](#mitiq.lre.inference.multivariate_richardson.sample_matrix "Link to this definition")
:   Defines the square sample matrix required for multivariate extrapolation as
    defined in [[30](bibliography.html#id59 "Vincent Russo and Andrea Mari. Quantum error mitigation by layerwise richardson extrapolation. (2024). arXiv:2402.04000.")].

    The number of monomial terms should be equal to the
    number of scale factor vectors such that the monomial terms define the rows
    and the scale factor vectors define the columns.

    Parameters:
    :   * **input\_circuit** (`Circuit`) – Quantum circuit to be scaled.
        * **degree** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Degree of the multivariate polynomial.
        * **fold\_multiplier** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Scaling gap required by unitary folding.
        * **num\_chunks** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of equally-sized circuit chunks. Noise
          scaling is applied to each chunk independently. Ranges from 1
          (all gates in one chunk, similar to ZNE) to the
          number of circuit layers (default, each layer is a separate chunk).

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   Matrix of the evaluated monomial basis terms from the scale factor
        :   vectors.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – When the degree for the multinomial is not greater than or
        equal to 1; when the fold multiplier to scale the circuit is
        greater than/equal to 1; when the number of chunks for a
        large circuit is 0 or when the number of chunks in a circuit is
        greater than the number of layers in the input circuit.

### Pauli Twirling[#](#module-mitiq.pt.pt "Link to this heading")

mitiq.pt.pt.add\_noise\_to\_two\_qubit\_gates(*circuit*, *noise\_name*, *\*\*kwargs*)[[source]](_modules/mitiq/pt/pt.html#add_noise_to_two_qubit_gates)[#](#mitiq.pt.pt.add_noise_to_two_qubit_gates "Link to this definition")
:   Add noise to CNOT and CZ gates on pre-twirled circuits.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Pre-twirled circuit
        * **noise\_name** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – name of noise operator to apply after CNOT and CZ gates
        * **kwargs** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

mitiq.pt.pt.generate\_pauli\_twirl\_variants(*circuit*, *num\_circuits=10*, *noise\_name=None*, *\*\*kwargs*)[[source]](_modules/mitiq/pt/pt.html#generate_pauli_twirl_variants)[#](#mitiq.pt.pt.generate_pauli_twirl_variants "Link to this definition")
:   Return the Pauli twirled versions of the input circuit.

    Only the CNOT and CZ gates in an input circuit are Pauli twirled
    as specified in [[39](bibliography.html#id61 "Abdullah Ash Saki, Amara Katabarwa, Salonik Resch, and George Umbrarescu. Hypothesis testing for error mitigation: how to evaluate error mitigation. (2023). arXiv:2301.02690.")].

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit on which twirling is applied.
        * **num\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of twirled variants of the circuits.
        * **noise\_name** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Name of the noisy operator acting on CNOT and CZ gates.
          This is useful if the user requires a noisy circuit after twirling.
          Values allowed: [“bit-flip”, “depolarize”]
        * **kwargs** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   A list of num\_circuits twirled versions of circuit

mitiq.pt.pt.twirl\_CNOT\_gates(*circuit*, *num\_circuits*)[[source]](_modules/mitiq/pt/pt.html#twirl_CNOT_gates)[#](#mitiq.pt.pt.twirl_CNOT_gates "Link to this definition")
:   Generate a list of circuits using Pauli twirling on CNOT gates.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The circuit to generate twirled versions of
        * **num\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of sampled circuits to return

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

mitiq.pt.pt.twirl\_CZ\_gates(*circuit*, *num\_circuits*)[[source]](_modules/mitiq/pt/pt.html#twirl_CZ_gates)[#](#mitiq.pt.pt.twirl_CZ_gates "Link to this definition")
:   Generate a list of circuits using Pauli twirling on CZ gates.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The circuit to generate twirled versions of
        * **num\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of sampled circuits to return

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

### Probabilistic Error Cancellation[#](#probabilistic-error-cancellation "Link to this heading")

#### Probabilistic Error Cancellation (High-Level Tools)[#](#module-mitiq.pec.pec "Link to this heading")

High-level probabilistic error cancellation tools.

*exception* mitiq.pec.pec.LargeSampleWarning[[source]](_modules/mitiq/pec/pec.html#LargeSampleWarning)[#](#mitiq.pec.pec.LargeSampleWarning "Link to this definition")
:   Warning is raised when PEC sample size is greater than 10 \*\* 5

mitiq.pec.pec.combine\_results(*results*, *norm*, *signs*)[[source]](_modules/mitiq/pec/pec.html#combine_results)[#](#mitiq.pec.pec.combine_results "Link to this definition")
:   Combine expectation values coming from probabilistically sampled
    circuits.

    Warning

    The `results` must be in the same order as the circuits were
    generated.

    Parameters:
    :   * **results** ([`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Results as obtained from running circuits.
        * **norm** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The one-norm of the circuit representation.
        * **signs** ([`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]) – The signs corresponding to the positivity of the sampled
          circuits.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The PEC estimate of the expectation value.

mitiq.pec.pec.construct\_circuits(*circuit*, *representations*, *precision=0.03*, *num\_samples=None*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/pec/pec.html#construct_circuits)[#](#mitiq.pec.pec.construct_circuits "Link to this definition")
:   Generates a list of sampled circuits based on the given
    quasi-probability representations.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The quantum circuit to be sampled.
        * **representations** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]) – The quasi-probability representations of the circuit
          operations.
        * **precision** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The desired precision for the sampling process.
          Default is 0.03.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of samples to generate. If None, the number of
          samples is deduced based on the precision. Default is None.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The random state or seed for reproducibility.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, returns the signs and the norm along with the
          sampled circuits. Default is False.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]] | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   A list of sampled circuits. If `full_output` is True, also returns a
        list of signs, the norm.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If the precision is not within the interval (0, 1].

mitiq.pec.pec.execute\_with\_pec(*circuit*, *executor*, *observable=None*, *\**, *representations*, *precision=0.03*, *num\_samples=None*, *force\_run\_all=True*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/pec/pec.html#execute_with_pec)[#](#mitiq.pec.pec.execute_with_pec "Link to this definition")
:   Estimates the error-mitigated expectation value associated to the
    input circuit, via the application of probabilistic error cancellation
    (PEC). [[9](bibliography.html#id70 "Kristan Temme, Sergey Bravyi, and Jay M. Gambetta. Error mitigation for short-depth quantum circuits. Physical Review Letters, (2017). URL: https://doi.org/10.1103/PhysRevLett.119.180509, doi:10.1103/physrevlett.119.180509.")] [[48](bibliography.html#id20 "Suguru Endo, Simon C. Benjamin, and Ying Li. Practical quantum error mitigation for near-future applications. Phys. Rev. X, 8:031027, (2018). URL: https://link.aps.org/doi/10.1103/PhysRevX.8.031027, doi:10.1103/PhysRevX.8.031027.")].

    This function implements PEC by:

    1. Sampling different implementable circuits from the quasi-probability
       representation of the input circuit;
    2. Evaluating the noisy expectation values associated to the sampled
       circuits (through the “executor” function provided by the user);
    3. Estimating the ideal expectation value from a suitable linear
       combination of the noisy ones.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit to execute with error-mitigation.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `QuantumResult` (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor must return an expectation value. Otherwise,
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **representations** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]) – Representations (basis expansions) of each operation
          in the input circuit.
        * **precision** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The desired estimation precision (assuming the observable
          is bounded by 1). The number of samples is deduced according
          to the formula (one\_norm / precision) \*\* 2, where ‘one\_norm’
          is related to the negativity of the quasi-probability
          representation [[9](bibliography.html#id70 "Kristan Temme, Sergey Bravyi, and Jay M. Gambetta. Error mitigation for short-depth quantum circuits. Physical Review Letters, (2017). URL: https://doi.org/10.1103/PhysRevLett.119.180509, doi:10.1103/physrevlett.119.180509.")]. If ‘num\_samples’ is
          explicitly set by the user, ‘precision’ is ignored and has no
          effect.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of noisy circuits to be sampled for PEC.
          If not given, this is deduced from the argument ‘precision’.
        * **force\_run\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, all sampled circuits are executed regardless of
          uniqueness, else a minimal unique set is executed.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling circuits.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False only the average PEC value is returned.
          If True a dictionary containing all PEC data is returned too.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   The tuple `(pec_value, pec_data)` where `pec_value` is the
        expectation value estimated with PEC and `pec_data` is a dictionary
        which contains all the raw data involved in the PEC process (including
        the PEC estimation error).
        The error is estimated as `pec_std / sqrt(num_samples)`, where
        `pec_std` is the standard deviation of the PEC samples, i.e., the
        square root of the mean squared deviation of the sampled values from
        `pec_value`. If `full_output` is `False`, only `pec_value` is
        returned.

mitiq.pec.pec.mitigate\_executor(*executor*, *observable=None*, *\**, *representations*, *precision=0.03*, *num\_samples=None*, *force\_run\_all=True*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/pec/pec.html#mitigate_executor)[#](#mitiq.pec.pec.mitigate_executor "Link to this definition")
:   Returns a modified version of the input ‘executor’ which is
    error-mitigated with probabilistic error cancellation (PEC).

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A function that executes a circuit and returns the
          unmitigated QuantumResult (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor must return an expectation value. Otherwise,
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **representations** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]) – Representations (basis expansions) of each operation
          in the input circuit.
        * **precision** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The desired estimation precision (assuming the observable
          is bounded by 1). The number of samples is deduced according
          to the formula (one\_norm / precision) \*\* 2, where ‘one\_norm’
          is related to the negativity of the quasi-probability
          representation [[9](bibliography.html#id70 "Kristan Temme, Sergey Bravyi, and Jay M. Gambetta. Error mitigation for short-depth quantum circuits. Physical Review Letters, (2017). URL: https://doi.org/10.1103/PhysRevLett.119.180509, doi:10.1103/physrevlett.119.180509.")]. If ‘num\_samples’ is
          explicitly set, ‘precision’ is ignored and has no effect.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of noisy circuits to be sampled for PEC.
          If not given, this is deduced from the argument ‘precision’.
        * **force\_run\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, all sampled circuits are executed regardless of
          uniqueness, else a minimal unique set is executed.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling circuits.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False only the average PEC value is returned.
          If True a dictionary containing all PEC data is returned too.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]]

    Returns:
    :   The error-mitigated version of the input executor.

mitiq.pec.pec.pec\_decorator(*observable=None*, *\**, *representations*, *precision=0.03*, *num\_samples=None*, *force\_run\_all=True*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/pec/pec.html#pec_decorator)[#](#mitiq.pec.pec.pec_decorator "Link to this definition")
:   Decorator which adds an error-mitigation layer based on probabilistic
    error cancellation (PEC) to an executor function, i.e., a function which
    executes a quantum circuit with an arbitrary backend and returns a
    `QuantumResult` (e.g. an expectation value).

    Parameters:
    :   * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor function being decorated must return an expectation
          value. Otherwise, the QuantumResult returned by this executor
          is used to compute the expectation of the observable.
        * **representations** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]) – Representations (basis expansions) of each operation
          in the input circuit.
        * **precision** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The desired estimation precision (assuming the observable
          is bounded by 1). The number of samples is deduced according
          to the formula (one\_norm / precision) \*\* 2, where ‘one\_norm’
          is related to the negativity of the quasi-probability
          representation [[9](bibliography.html#id70 "Kristan Temme, Sergey Bravyi, and Jay M. Gambetta. Error mitigation for short-depth quantum circuits. Physical Review Letters, (2017). URL: https://doi.org/10.1103/PhysRevLett.119.180509, doi:10.1103/physrevlett.119.180509.")]. If ‘num\_samples’ is
          explicitly set by the user, ‘precision’ is ignored and has no
          effect.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of noisy circuits to be sampled for PEC.
          If not given, this is deduced from the argument ‘precision’.
        * **force\_run\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, all sampled circuits are executed regardless of
          uniqueness, else a minimal unique set is executed.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling circuits.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False only the average PEC value is returned.
          If True a dictionary containing all PEC data is returned too.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]]]

    Returns:
    :   The error-mitigating decorator to be applied to an executor function.

#### Quasi-Probability Representations[#](#module-mitiq.pec.representations.optimal "Link to this heading")

Functions for finding optimal representations given a noisy basis.

mitiq.pec.representations.optimal.find\_optimal\_representation(*ideal\_operation*, *noisy\_operations*, *tol=1e-08*, *initial\_guess=None*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/pec/representations/optimal.html#find_optimal_representation)[#](#mitiq.pec.representations.optimal.find_optimal_representation "Link to this definition")
:   Returns the `OperationRepresentation` of the input ideal operation
    which minimizes the one-norm of the associated quasi-probability
    distribution.

    More precisely, it solve the following optimization problem:

    \[\min\_{\eta\_\alpha} \left\{\sum\_\alpha |\eta\_\alpha| \, : \,
    \mathcal G = \sum\_\alpha \eta\_\alpha \mathcal O\_\alpha \right\}\]

    where \(\{\mathcal O\_j\}\) is the input basis of noisy operations,
    and \(\mathcal{G}\) is the ideal operation to be represented.

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation to represent.
        * **noisy\_operations** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`NoisyOperation`](#mitiq.pec.types.types.NoisyOperation "mitiq.pec.types.types.NoisyOperation")]) – The basis in which the `ideal_operation`
          should be represented. Must be a list of `NoisyOperation` objects
          which are initialized with a numerical superoperator matrix.
        * **tol** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The error tolerance for each matrix element
          of the represented operation.
        * **initial\_guess** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional initial guess for the coefficients
          \(\{ \eta\_\alpha \}\).
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation corresponds to the
          operation on the specific qubits defined in ideal\_operation.
          If False, the representation is valid for the same gate even if
          acting on different qubits from those specified in
          ideal\_operation.

    Return type:
    :   [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")

    Returns: The optimal OperationRepresentation.

mitiq.pec.representations.optimal.minimize\_one\_norm(*ideal\_matrix*, *basis\_matrices*, *tol=1e-08*, *initial\_guess=None*)[[source]](_modules/mitiq/pec/representations/optimal.html#minimize_one_norm)[#](#mitiq.pec.representations.optimal.minimize_one_norm "Link to this definition")
:   Returns the list of real coefficients \([x\_0, x\_1, \dots]\),
    which minimizes \(\sum\_j |x\_j|\) with the contraint that
    the following representation of the input `ideal_matrix` holds:

    \[\text{ideal\_matrix} = x\_0 A\_0 + x\_1 A\_1 + \cdots\]

    where \(\{A\_j\}\) are the basis matrices, i.e., the elements of
    the input `basis_matrices`.

    This function can be used to compute the optimal representation
    of an ideal superoperator (or Choi state) as a linear
    combination of real noisy superoperators (or Choi states).

    Parameters:
    :   * **ideal\_matrix** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – The ideal matrix to represent.
        * **basis\_matrices** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]]) – The list of basis matrices.
        * **tol** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The error tolerance for each matrix element
          of the represented matrix.
        * **initial\_guess** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional initial guess for the coefficients
          \([x\_0, x\_1, \dots]\).

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]

    Returns:
    :   The list of optimal coefficients \([x\_0, x\_1, \dots]\).

Functions related to representations with amplitude damping noise.

mitiq.pec.representations.damping.amplitude\_damping\_kraus(*noise\_level*, *num\_qubits*)[[source]](_modules/mitiq/pec/representations/damping.html#amplitude_damping_kraus)[#](#mitiq.pec.representations.damping.amplitude_damping_kraus "Link to this definition")
:   Returns the Kraus operators of the tensor product of local
    depolarizing channels acting on each qubit.

    Parameters:
    :   * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))
        * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"))

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]]

Functions related to representations with depolarizing noise.

mitiq.pec.representations.depolarizing.global\_depolarizing\_kraus(*noise\_level*, *num\_qubits*)[[source]](_modules/mitiq/pec/representations/depolarizing.html#global_depolarizing_kraus)[#](#mitiq.pec.representations.depolarizing.global_depolarizing_kraus "Link to this definition")
:   Returns the kraus operators of a global depolarizing channel at a
    given noise level.

    Parameters:
    :   * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))
        * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"))

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]]

mitiq.pec.representations.depolarizing.local\_depolarizing\_kraus(*noise\_level*, *num\_qubits*)[[source]](_modules/mitiq/pec/representations/depolarizing.html#local_depolarizing_kraus)[#](#mitiq.pec.representations.depolarizing.local_depolarizing_kraus "Link to this definition")
:   Returns the kraus operators of the tensor product of local
    depolarizing channels acting on each qubit.

    Parameters:
    :   * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))
        * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"))

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]]

mitiq.pec.representations.depolarizing.represent\_operation\_with\_global\_depolarizing\_noise(*ideal\_operation*, *noise\_level*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/pec/representations/depolarizing.html#represent_operation_with_global_depolarizing_noise)[#](#mitiq.pec.representations.depolarizing.represent_operation_with_global_depolarizing_noise "Link to this definition")
:   As described in [[9](bibliography.html#id70 "Kristan Temme, Sergey Bravyi, and Jay M. Gambetta. Error mitigation for short-depth quantum circuits. Physical Review Letters, (2017). URL: https://doi.org/10.1103/PhysRevLett.119.180509, doi:10.1103/physrevlett.119.180509.")], this function maps an
    `ideal_operation` \(\mathcal{U}\) into its quasi-probability
    representation, which is a linear combination of noisy implementable
    operations \(\sum\_\alpha \eta\_{\alpha} \mathcal{O}\_{\alpha}\).

    This function assumes a depolarizing noise model and, more precicely,
    that the following noisy operations are implementable
    \(\mathcal{O}\_{\alpha} = \mathcal{D} \circ \mathcal P\_\alpha
    \circ \mathcal{U}\), where \(\mathcal{U}\) is the unitary associated
    to the input `ideal_operation` acting on \(k\) qubits,
    \(\mathcal{P}\_\alpha\) is a Pauli operation and
    \(\mathcal{D}(\rho) = (1 - \epsilon) \rho + \epsilon I/2^k\) is a
    depolarizing channel (\(\epsilon\) is a simple function of
    `noise_level`).

    For a single-qubit `ideal_operation`, the representation is as
    follows:

    \[\mathcal{U}\_{\beta} = \eta\_1 \mathcal{O}\_1 + \eta\_2 \mathcal{O}\_2 +
    \eta\_3 \mathcal{O}\_3 + \eta\_4 \mathcal{O}\_4\]

    \[ \begin{align}\begin{aligned}\eta\_1 =1 + \frac{3}{4} \frac{\epsilon}{1- \epsilon},
    \qquad \mathcal{O}\_1 = \mathcal{D} \circ \mathcal{I} \circ \mathcal{U}\\\eta\_2 =- \frac{1}{4}\frac{\epsilon}{1- \epsilon} , \qquad
    \mathcal{O}\_2 = \mathcal{D} \circ \mathcal{X} \circ \mathcal{U}\\\eta\_3 =- \frac{1}{4}\frac{\epsilon}{1- \epsilon} , \qquad
    \mathcal{O}\_3 = \mathcal{D} \circ \mathcal{Y} \circ \mathcal{U}\\\eta\_4 =- \frac{1}{4}\frac{\epsilon}{1- \epsilon} , \qquad
    \mathcal{O}\_4 = \mathcal{D} \circ \mathcal{Z} \circ \mathcal{U}\end{aligned}\end{align} \]

    It was proven in [[15](bibliography.html#id69 "Ryuji Takagi. Optimal resource cost for error mitigation. Physical Review Research, (2021). URL: http://dx.doi.org/10.1103/PhysRevResearch.3.033178, doi:10.1103/physrevresearch.3.033178.")] that, under suitable assumptions,
    this representation is optimal (minimum 1-norm).

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation (as a QPROGRAM) to represent.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The noise level (as a float) of the depolarizing channel.
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation corresponds to the
          operation on the specific qubits defined in ideal\_operation.
          If False, the representation is valid for the same gate even if
          acting on different qubits from those specified in
          ideal\_operation.

    Return type:
    :   [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")

    Returns:
    :   The quasi-probability representation of the `ideal_operation`.

    Note

    This representation is based on the ideal assumption that one
    can append Pauli gates to a noisy operation without introducing
    additional noise. For a backend which violates this assumption,
    it remains a good approximation for small values of `noise_level`.

    Note

    The input `ideal_operation` is typically a QPROGRAM with a single
    gate but could also correspond to a sequence of more gates.
    This is possible as long as the unitary associated to the input
    QPROGRAM, followed by a single final depolarizing channel, is
    physically implementable.

mitiq.pec.representations.depolarizing.represent\_operation\_with\_local\_depolarizing\_noise(*ideal\_operation*, *noise\_level*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/pec/representations/depolarizing.html#represent_operation_with_local_depolarizing_noise)[#](#mitiq.pec.representations.depolarizing.represent_operation_with_local_depolarizing_noise "Link to this definition")
:   As described in [[9](bibliography.html#id70 "Kristan Temme, Sergey Bravyi, and Jay M. Gambetta. Error mitigation for short-depth quantum circuits. Physical Review Letters, (2017). URL: https://doi.org/10.1103/PhysRevLett.119.180509, doi:10.1103/physrevlett.119.180509.")], this function maps an
    `ideal_operation` \(\mathcal{U}\) into its quasi-probability
    representation, which is a linear combination of noisy implementable
    operations \(\sum\_\alpha \eta\_{\alpha} \mathcal{O}\_{\alpha}\).

    This function assumes a (local) single-qubit depolarizing noise model even
    for multi-qubit operations. More precicely, it assumes that the following
    noisy operations are implementable \(\mathcal{O}\_{\alpha} =
    \mathcal{D}^{\otimes k} \circ \mathcal P\_\alpha \circ \mathcal{U}\),
    where \(\mathcal{U}\) is the unitary associated
    to the input `ideal_operation` acting on \(k\) qubits,
    \(\mathcal{P}\_\alpha\) is a Pauli operation and
    \(\mathcal{D}(\rho) = (1 - \epsilon) \rho + \epsilon I/2\) is a
    single-qubit depolarizing channel (\(\epsilon\) is a simple function
    of `noise_level`).

    More information about the quasi-probability representation for a
    depolarizing noise channel can be found in:
    [`represent_operation_with_global_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operation_with_global_depolarizing_noise "mitiq.pec.representations.depolarizing.represent_operation_with_global_depolarizing_noise").

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation (as a QPROGRAM) to represent.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The noise level of each depolarizing channel.
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation corresponds to the
          operation on the specific qubits defined in ideal\_operation.
          If False, the representation is valid for the same gate even
          if acting on different qubits from those specified in
          ideal\_operation.

    Return type:
    :   [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")

    Returns:
    :   The quasi-probability representation of the `ideal_operation`.

    Note

    The input `ideal_operation` is typically a QPROGRAM with a single
    gate but could also correspond to a sequence of more gates.
    This is possible as long as the unitary associated to the input
    QPROGRAM, followed by a single final depolarizing channel, is
    physically implementable.

mitiq.pec.representations.depolarizing.represent\_operations\_in\_circuit\_with\_global\_depolarizing\_noise(*ideal\_circuit*, *noise\_level*)[[source]](_modules/mitiq/pec/representations/depolarizing.html#represent_operations_in_circuit_with_global_depolarizing_noise)[#](#mitiq.pec.representations.depolarizing.represent_operations_in_circuit_with_global_depolarizing_noise "Link to this definition")
:   Iterates over all unique operations of the input `ideal_circuit` and,
    for each of them, generates the corresponding quasi-probability
    representation (linear combination of implementable noisy operations).

    This function assumes that the same depolarizing noise channel of strength
    `noise_level` affects each implemented operation.

    This function internally calls
    [`represent_operation_with_global_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operation_with_global_depolarizing_noise "mitiq.pec.representations.depolarizing.represent_operation_with_global_depolarizing_noise") (more details
    about the quasi-probability representation can be found in its docstring).

    Parameters:
    :   * **ideal\_circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal circuit, whose ideal operations should be
          represented.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (gate-independent) depolarizing noise level.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]

    Returns:
    :   The list of quasi-probability representations associated to
        the operations of the input `ideal_circuit`.

    Note

    Measurement gates are ignored (not represented).

    Note

    The returned representations are always defined in terms of
    Cirq circuits, even if the input is not a `cirq.Circuit`.

mitiq.pec.representations.depolarizing.represent\_operations\_in\_circuit\_with\_local\_depolarizing\_noise(*ideal\_circuit*, *noise\_level*)[[source]](_modules/mitiq/pec/representations/depolarizing.html#represent_operations_in_circuit_with_local_depolarizing_noise)[#](#mitiq.pec.representations.depolarizing.represent_operations_in_circuit_with_local_depolarizing_noise "Link to this definition")
:   Iterates over all unique operations of the input `ideal_circuit` and,
    for each of them, generates the corresponding quasi-probability
    representation (linear combination of implementable noisy operations).

    This function assumes that the tensor product of `k` single-qubit
    depolarizing channels affects each implemented operation, where
    `k` is the number of qubits associated to the operation.

    This function internally calls
    [`represent_operation_with_local_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operation_with_local_depolarizing_noise "mitiq.pec.representations.depolarizing.represent_operation_with_local_depolarizing_noise") (more details
    about the quasi-probability representation can be found in its docstring).

    Parameters:
    :   * **ideal\_circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal circuit, whose ideal operations should be
          represented.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (gate-independent) depolarizing noise level.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]

    Returns:
    :   The list of quasi-probability representations associated to
        the operations of the input `ideal_circuit`.

    Note

    Measurement gates are ignored (not represented).

    Note

    The returned representations are always defined in terms of
    Cirq circuits, even if the input is not a `cirq.Circuit`.

#### Learning-based PEC[#](#module-mitiq.pec.representations.biased_noise "Link to this heading")

Function to generate representations with biased noise.

mitiq.pec.representations.biased\_noise.represent\_operation\_with\_local\_biased\_noise(*ideal\_operation*, *epsilon*, *eta*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/pec/representations/biased_noise.html#represent_operation_with_local_biased_noise)[#](#mitiq.pec.representations.biased_noise.represent_operation_with_local_biased_noise "Link to this definition")
:   This function maps an
    `ideal_operation` \(\mathcal{U}\) into its quasi-probability
    representation, which is a linear combination of noisy implementable
    operations \(\sum\_\alpha \eta\_{\alpha} \mathcal{O}\_{\alpha}\).

    This function assumes a combined depolarizing and dephasing noise model
    with a bias factor \(\eta\) (see [[16](bibliography.html#id66 "Armands Strikis, Dayue Qin, Yanzhu Chen, Simon C. Benjamin, and Ying Li. Learning-based quantum error mitigation. PRX Quantum, (2021). URL: http://dx.doi.org/10.1103/PRXQuantum.2.040330, doi:10.1103/prxquantum.2.040330.")])
    and that the following noisy operations are implementable
    \(\mathcal{O}\_{\alpha} = \mathcal{D} \circ \mathcal P\_\alpha\)
    where \(\mathcal{U}\) is the unitary associated
    to the input `ideal_operation`,
    \(\mathcal{P}\_\alpha\) is a Pauli operation and

    \[\mathcal{D}(\epsilon) = (1 - \epsilon)[\mathbb{1}] +
    \epsilon(\frac{\eta}{\eta + 1} \mathcal{Z}
    + \frac{1}{3}\frac{1}{\eta + 1}(\mathcal{X} + \mathcal{Y}
    + \mathcal{Z}))\]

    is the combined (biased) dephasing and depolarizing channel acting on a
    single qubit. For multi-qubit operations, we use a noise channel that is
    the tensor product of the local single-qubit channels.

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation (as a QPROGRAM) to represent.
        * **epsilon** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The local noise severity (as a float) of the combined channel.
        * **eta** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The noise bias between combined dephasing and depolarizing
          channels with \(\eta = 0\) describing a fully depolarizing
          channel and \(\eta = \infty\) describing a fully dephasing
          channel.
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation corresponds to the
          operation on the specific qubits defined in ideal\_operation.
          If False, the representation is valid for the same gate even if
          acting on different qubits from those specified in
          ideal\_operation.

    Return type:
    :   [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")

    Returns:
    :   The quasi-probability representation of the `ideal_operation`.

    Note

    This representation is based on the ideal assumption that one
    can append Pauli gates to a noisy operation without introducing
    additional noise. For a backend which violates this assumption,
    it remains a good approximation for small values of `epsilon`.

    Note

    The input `ideal_operation` is typically a QPROGRAM with a single
    gate but could also correspond to a sequence of more gates.
    This is possible as long as the unitary associated to the input
    QPROGRAM, followed by a single final biased noise channel, is
    physically implementable.

Functions to calculate parameters for depolarizing noise and biased noise
models via a learning-based technique.

mitiq.pec.representations.learning.biased\_noise\_loss\_function(*params*, *operations\_to\_mitigate*, *training\_circuits*, *ideal\_values*, *noisy\_executor*, *pec\_kwargs*, *pec\_data=None*, *observable=None*)[[source]](_modules/mitiq/pec/representations/learning.html#biased_noise_loss_function)[#](#mitiq.pec.representations.learning.biased_noise_loss_function "Link to this definition")
:   Loss function for optimizing quasi-probability representations
    assuming a biased noise model depending on two real parameters.

    Parameters:
    :   * **params** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – Array of optimization parameters epsilon
          (local noise strength) and eta (noise bias between reduced
          dephasing and depolarizing channels).
        * **operations\_to\_mitigate** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – List of ideal operations to be represented by
          a combination of noisy operations.
        * **training\_circuits** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – List of training circuits for generating the
          error-mitigated expectation values.
        * **ideal\_values** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – Expectation values obtained by noiseless simulations.
        * **noisy\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Executes the circuit with noise and returns a
          QuantumResult.
        * **pec\_kwargs** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]) – Options to pass to execute\_w\_pec for the error-mitigated
          expectation value obtained from executing the training circuits.
        * **pec\_data** (*optional*) – 3-D array of error-mitigated expection values for
          model training.
        * **observable** (*optional*) – Observable to compute the expectation value of.
          If None, the `executor` must return an expectation value.
          Otherwise the `QuantumResult` returned by `executor` is used to
          compute the expectation of the observable.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns: Mean squared error between the error-mitigated values and
    :   the ideal values, over the training set.

mitiq.pec.representations.learning.depolarizing\_noise\_loss\_function(*epsilon*, *operations\_to\_mitigate*, *training\_circuits*, *ideal\_values*, *noisy\_executor*, *pec\_kwargs*, *pec\_data=None*, *observable=None*)[[source]](_modules/mitiq/pec/representations/learning.html#depolarizing_noise_loss_function)[#](#mitiq.pec.representations.learning.depolarizing_noise_loss_function "Link to this definition")
:   Loss function for optimizing quasi-probability representations
    assuming a depolarizing noise model depending on one real parameter.

    Parameters:
    :   * **epsilon** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – Array of optimization parameters epsilon
          (local noise strength) and eta (noise bias between reduced
          dephasing and depolarizing channels).
        * **operations\_to\_mitigate** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – List of ideal operations to be represented by
          a combination of noisy operations.
        * **training\_circuits** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – List of training circuits for generating the
          error-mitigated expectation values.
        * **ideal\_values** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – Expectation values obtained by noiseless simulations.
        * **noisy\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Executes the circuit with noise and returns a
          QuantumResult.
        * **pec\_kwargs** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]) – Options to pass to execute\_w\_pec for the error-mitigated
          expectation value obtained from executing the training circuits.
        * **pec\_data** (*optional*) – 2-D array of error-mitigated expection values for
          model training.
        * **observable** (*optional*) – Observable to compute the expectation value of.
          If None, the `executor` must return an expectation value.
          Otherwise the `QuantumResult` returned by `executor` is used to
          compute the expectation of the observable.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns: Mean squared error between the error-mitigated values and
    :   the ideal values, over the training set.

mitiq.pec.representations.learning.learn\_biased\_noise\_parameters(*operations\_to\_learn*, *circuit*, *ideal\_executor*, *noisy\_executor*, *pec\_kwargs=None*, *num\_training\_circuits=5*, *fraction\_non\_clifford=0.2*, *training\_random\_state=None*, *epsilon0=0.05*, *eta0=1*, *observable=None*, *\*\*learning\_kwargs*)[[source]](_modules/mitiq/pec/representations/learning.html#learn_biased_noise_parameters)[#](#mitiq.pec.representations.learning.learn_biased_noise_parameters "Link to this definition")
:   This function learns the biased noise parameters epsilon and eta
    associated to a set of input operations. The learning process is based on
    the execution of a set of training circuits on a noisy backend and on a
    classical simulator. The training circuits are near-Clifford approximations
    of the input circuit. A biased noise model characterization is assumed.

    Parameters:
    :   * **operations\_to\_learn** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – The ideal operations to learn the noise model of.
        * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The full quantum program as defined by the user.
        * **ideal\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Simulates a circuit and returns
          a noiseless `QuantumResult`.
        * **noisy\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Executes a circuit on a noisy backend
          and returns a `QuantumResult`.
        * **pec\_kwargs** (*optional*) – Options to pass to `execute_w_pec` for the
          error-mitigated expectation value obtained from executing
          the training circuits.
        * **num\_training\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of near-Clifford circuits to be
          generated for training.
        * **fraction\_non\_clifford** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (approximate) fraction of non-Clifford
          gates in each training circuit.
        * **training\_random\_state** ([`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling the training circuits.
        * **epsilon0** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Initial guess for noise strength.
        * **eta0** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Initial guess for noise bias.
        * **observable** (*optional*) – Observable to compute the expectation value of.
          If None, the `executor` must return an expectation value.
          Otherwise the QuantumResult returned by executor is used to
          compute the expectation of the observable.
        * **learning\_kwargs** (*optional*) – Additional data and options including
          `method` an optimization method supported by
          `scipy.optimize.minimize` and settings for the chosen
          optimization method.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   A 3-tuple containing a flag indicating whether or not the optimizer
        exited successfully, the optimized noise strength epsilon, and the
        optimized noise bias, eta.

    Note

    Using this function may require some tuning. One of the main
    challenges is setting a good value of `num_samples` in the PEC
    options `pec_kwargs`. Setting a small value of `num_samples` is
    typically necessary to obtain a reasonable execution time. On the other
    hand, using a number of PEC samples that is too small can result in a
    large statistical error, ultimately causing the optimization process to
    fail.

mitiq.pec.representations.learning.learn\_depolarizing\_noise\_parameter(*operations\_to\_learn*, *circuit*, *ideal\_executor*, *noisy\_executor*, *pec\_kwargs=None*, *num\_training\_circuits=5*, *fraction\_non\_clifford=0.2*, *training\_random\_state=None*, *epsilon0=0.05*, *observable=None*, *\*\*learning\_kwargs*)[[source]](_modules/mitiq/pec/representations/learning.html#learn_depolarizing_noise_parameter)[#](#mitiq.pec.representations.learning.learn_depolarizing_noise_parameter "Link to this definition")
:   This function learns the depolarizing noise parameter (epsilon)
    associated to a set of input operations. The learning process is based on
    the execution of a set of training circuits on a noisy backend and on a
    classical simulator. The training circuits are near-Clifford approximations
    of the input circuit. A depolarizing noise model characterization is
    assumed.

    Parameters:
    :   * **operations\_to\_learn** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – The ideal operations to learn the noise model of.
        * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The full quantum program as defined by the user.
        * **ideal\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Simulates a circuit and returns
          a noiseless `QuantumResult`.
        * **noisy\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Executes a circuit on a noisy backend
          and returns a `QuantumResult`.
        * **pec\_kwargs** (*optional*) – Options to pass to `execute_w_pec` for the
          error-mitigated expectation value obtained from executing
          the training circuits.
        * **num\_training\_circuits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of near-Clifford circuits to be
          generated for training.
        * **fraction\_non\_clifford** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (approximate) fraction of non-Clifford
          gates in each training circuit.
        * **training\_random\_state** ([`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling the training circuits.
        * **epsilon0** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Initial guess for noise strength.
        * **observable** (*optional*) – Observable to compute the expectation value of.
          If None, the `executor` must return an expectation value.
          Otherwise the QuantumResult returned by executor is used to
          compute the expectation of the observable.
        * **learning\_kwargs** (*optional*) – Additional data and options including
          `method` an optimization method supported by
          `scipy.optimize.minimize` and settings for the chosen
          optimization method.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   A 2-tuple containing flag indicating whether or not the optimizer
        exited successfully and the optimized noise strength epsilon.

    Note

    Using this function may require some tuning. One of the main
    challenges is setting a good value of `num_samples` in the PEC
    options `pec_kwargs`. Setting a small value of `num_samples` is
    typically necessary to obtain a reasonable execution time. On the other
    hand, using a number of PEC samples that is too small can result in a
    large statistical error, ultimately causing the optimization process to
    fail.

#### Sampling from a Noisy Decomposition of an Ideal Operation[#](#module-mitiq.pec.sampling "Link to this heading")

Tools for sampling from the noisy representations of ideal operations.

mitiq.pec.sampling.sample\_circuit(*ideal\_circuit*, *representations*, *random\_state=None*, *num\_samples=1*)[[source]](_modules/mitiq/pec/sampling.html#sample_circuit)[#](#mitiq.pec.sampling.sample_circuit "Link to this definition")
:   Samples a list of implementable circuits from the quasi-probability
    representation of the input ideal circuit.
    Returns the list of circuits, the corresponding list of signs and the
    one-norm of the quasi-probability representation (of the full circuit).

    Parameters:
    :   * **ideal\_circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal circuit from which an implementable circuit
          is sampled.
        * **representations** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]) – List of representations of every operation in the
          input circuit. If a representation cannot be found for an operation
          in the circuit, a ValueError is raised.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of samples.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   The tuple (`sampled_circuits`, `signs`, `norm`) where
        `sampled_circuits` are the sampled implementable circuits,
        `signs` are the signs associated to sampled\_circuits and
        `norm` is the one-norm of the circuit representation.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If a representation is not found for an operation in the circuit.

mitiq.pec.sampling.sample\_sequence(*ideal\_operation*, *representations*, *random\_state=None*, *num\_samples=1*)[[source]](_modules/mitiq/pec/sampling.html#sample_sequence)[#](#mitiq.pec.sampling.sample_sequence "Link to this definition")
:   Samples a list of implementable sequences from the quasi-probability
    representation of the input ideal operation.
    Returns the list of sequences, the corresponding list of signs and the
    one-norm of the quasi-probability representation (of the input operation).

    For example, if the ideal operation is U with representation U = a A + b B,
    then this function returns A with probability \(|a| / (|a| + |b|)\) and
    B with probability \(|b| / (|a| + |b|)\). Also returns sign(a)
    (sign(b)) and \(|a| + |b|\) if A (B) is sampled.

    Note that the ideal operation can be a sequence of operations (circuit),
    for instance U = V W, as long as a representation is known. Similarly, A
    and B can be sequences of operations (circuits) or just single operations.

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation from which an implementable
          sequence is sampled.
        * **representations** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]) – A list of representations of ideal operations in a
          noisy basis. If no representation is found for ideal\_operation,
          a ValueError is raised.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for sampling.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of samples.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   The tuple (`sequences`, `signs`, `norm`) where
        `sequences` are the sampled sequences,
        `signs` are the signs associated to the sampled `sequences` and
        `norm` is the one-norm of the quasi-probability distribution.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If no representation is found for ideal\_operation.

#### Probabilistic Error Cancellation Types[#](#module-mitiq.pec.types.types "Link to this heading")

Types used in probabilistic error cancellation.

*class* mitiq.pec.types.types.NoisyBasis(*\*args*, *\*\*kwargs*)[[source]](_modules/mitiq/pec/types/types.html#NoisyBasis)[#](#mitiq.pec.types.types.NoisyBasis "Link to this definition")
:   A set of noisy operations which a quantum computer can actually
    implement, assumed to form a basis of n-qubit unitary matrices.

    This class has been removed since Mitiq v0.24.0.

    Parameters:
    :   * **args** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))

*class* mitiq.pec.types.types.NoisyOperation(*circuit*, *channel\_matrix=None*)[[source]](_modules/mitiq/pec/types/types.html#NoisyOperation)[#](#mitiq.pec.types.types.NoisyOperation "Link to this definition")
:   An operation (or sequence of operations) which a noisy quantum computer
    can actually implement.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – A short circuit which, when executed on a given noisy
          quantum computer, generates a noisy channel. It typically
          contains a single-gate or a short sequence of gates.
        * **channel\_matrix** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Superoperator representation of the noisy channel
          which is generated when executing the input `circuit` on the
          noisy quantum computer.

    Raises:
    :   [**TypeError**](https://docs.python.org/3.11/library/exceptions.html#TypeError "(in Python v3.11)") – If `ideal` is not a `QPROGRAM`.

    *property* circuit*: Circuit*[#](#mitiq.pec.types.types.NoisyOperation.circuit "Link to this definition")
    :   Returns the circuit of the NoisyOperation as a Cirq circuit.

    *property* native\_circuit*: Circuit | [pyquil.Program](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)") | [QuantumCircuit](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)") | Circuit | [QuantumTape](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)") | [Circuit](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)") | QasmStringType*[#](#mitiq.pec.types.types.NoisyOperation.native_circuit "Link to this definition")
    :   Returns the circuit used to initialize the NoisyOperation.

*class* mitiq.pec.types.types.OperationRepresentation(*ideal*, *noisy\_operations*, *coeffs*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/pec/types/types.html#OperationRepresentation)[#](#mitiq.pec.types.types.OperationRepresentation "Link to this definition")
:   A decomposition (basis expansion) of an operation or sequence of
    operations in a basis of noisy, implementable operations.

    Parameters:
    :   * **ideal** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation desired to be implemented.
        * **basis\_expansion** – Representation of the ideal operation in a basis
          of `NoisyOperation` objects.
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation
          corresponds to the operation on the specific qubits defined in
          `ideal`. If False, the representation is valid for the same
          gate even if acting on different qubits from those specified in
          `ideal`.
        * **noisy\_operations** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`NoisyOperation`](#mitiq.pec.types.types.NoisyOperation "mitiq.pec.types.types.NoisyOperation")])
        * **coeffs** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")])

    Raises:
    :   [**TypeError**](https://docs.python.org/3.11/library/exceptions.html#TypeError "(in Python v3.11)") – If all keys of `basis_expansion` are not instances of
        `NoisyOperation` objects.

    *property* coeffs*: [list](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[float](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]*[#](#mitiq.pec.types.types.OperationRepresentation.coeffs "Link to this definition")
    :   Returns the coefficients of the quasi-probability distribution.

    *property* distribution*: [list](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[float](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]*[#](#mitiq.pec.types.types.OperationRepresentation.distribution "Link to this definition")
    :   Returns the probability distribution obtained from taking
        the absolute value and normalizing the quasi-probability distribution.

    *property* norm*: [float](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")*[#](#mitiq.pec.types.types.OperationRepresentation.norm "Link to this definition")
    :   Returns the 1-norm of the quasi-probability distribution.

    sample(*random\_state=None*)[[source]](_modules/mitiq/pec/types/types.html#OperationRepresentation.sample)[#](#mitiq.pec.types.types.OperationRepresentation.sample "Link to this definition")
    :   Returns a randomly sampled NoisyOperation from the basis expansion.

        Parameters:
        :   **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Defines the seed for sampling if provided.

        Return type:
        :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`NoisyOperation`](#mitiq.pec.types.types.NoisyOperation "mitiq.pec.types.types.NoisyOperation"), [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

#### Utilities for Quantum Channels[#](#module-mitiq.pec.channels "Link to this heading")

Utilities for manipulating matrix representations of quantum channels.

mitiq.pec.channels.choi\_to\_super(*choi\_state*)[[source]](_modules/mitiq/pec/channels.html#choi_to_super)[#](#mitiq.pec.channels.choi_to_super "Link to this definition")
:   Returns the superoperator matrix corresponding to
    the channel defined by the input (normalized) Choi state.

    Up to normalization, this is just a tensor transposition.

    Parameters:
    :   **choi\_state** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]])

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

mitiq.pec.channels.kraus\_to\_choi(*kraus\_ops*)[[source]](_modules/mitiq/pec/channels.html#kraus_to_choi)[#](#mitiq.pec.channels.kraus_to_choi "Link to this definition")
:   Returns the normalized choi state corresponding to
    the channel defined by the input kraus operators.

    Parameters:
    :   **kraus\_ops** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]])

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

mitiq.pec.channels.kraus\_to\_super(*kraus\_ops*)[[source]](_modules/mitiq/pec/channels.html#kraus_to_super)[#](#mitiq.pec.channels.kraus_to_super "Link to this definition")
:   Maps a set of Kraus operators into a single superoperator
    matrix acting by matrix multiplication on vectorized
    density matrices.

    The returned matrix \(S\) is obtained with the formula:

    \[S = \sum\_j K\_j \otimes K\_j^\*,\]

    where \(\{K\_j\}\) are the Kraus operators.
    The mapping is based on the following isomorphism:

    \[A|i \rangle\langle j|B <=> (A \otimes B^T) |i\rangle|j\rangle.\]

    Parameters:
    :   **kraus\_ops** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]])

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

mitiq.pec.channels.super\_to\_choi(*super\_operator*)[[source]](_modules/mitiq/pec/channels.html#super_to_choi)[#](#mitiq.pec.channels.super_to_choi "Link to this definition")
:   Returns the normalized choi state corresponding to
    the channel defined by the input superoperator.

    Up to normalization, this is just a tensor transposition.

    Parameters:
    :   **super\_operator** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]])

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

### Quantum Subspace Expansion[#](#module-mitiq.qse.qse "Link to this heading")

High-level Quantum Susbapce Expansion tools.

mitiq.qse.qse.execute\_with\_qse(*circuit*, *executor*, *check\_operators*, *code\_hamiltonian*, *observable*, *pauli\_string\_to\_expectation\_cache=None*)[[source]](_modules/mitiq/qse/qse.html#execute_with_qse)[#](#mitiq.qse.qse.execute_with_qse "Link to this definition")
:   Function for the calculation of an observable from some circuit of
    interest to be mitigated with quantum subspace expansion (QSE).

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Quantum program to execute with error mitigation.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit and returns a QuantumResult.
        * **check\_operators** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")]) – List of check operators that define the
          stabilizer code space.
        * **code\_hamiltonian** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Hamiltonian of the code space.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the mitigated expectation value of.
        * **pauli\_string\_to\_expectation\_cache** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString"), [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Cache for expectation values of
          Pauli strings used to compute the projector and the observable.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value estimated with QSE.

mitiq.qse.qse.mitigate\_executor(*executor*, *check\_operators*, *code\_hamiltonian*, *observable*, *pauli\_string\_to\_expectation\_cache=None*)[[source]](_modules/mitiq/qse/qse.html#mitigate_executor)[#](#mitiq.qse.qse.mitigate_executor "Link to this definition")
:   Returns a modified version of the input ‘executor’ which is
    error-mitigated with quantum subspace expansion (QSE).

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – Executes a circuit and returns a QuantumResult.
        * **check\_operators** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")]) – List of check operators that define the
          stabilizer code space.
        * **code\_hamiltonian** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Hamiltonian of the code space.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the mitigated expectation value for.
        * **pauli\_string\_to\_expectation\_cache** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString"), [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Cache for expectation values of
          Pauli strings used to compute the projector and the observable.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   The error-mitigated version of the input executor.

mitiq.qse.qse.qse\_decorator(*check\_operators*, *code\_hamiltonian*, *observable*, *pauli\_string\_to\_expectation\_cache=None*)[[source]](_modules/mitiq/qse/qse.html#qse_decorator)[#](#mitiq.qse.qse.qse_decorator "Link to this definition")
:   Decorator which adds an error-mitigation layer based on quantum
    subspace expansion (QSE) to an executor function, i.e., a function which
    executes a quantum circuit with an arbitrary backend and returns a
    `QuantumResult`.

    Parameters:
    :   * **check\_operators** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")]) – List of check operators that define the
          stabilizer code space.
        * **code\_hamiltonian** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Hamiltonian of the code space.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the mitigated expectation value of.
        * **pauli\_string\_to\_expectation\_cache** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString"), [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Cache for expectation values of
          Pauli strings used to compute the projector and the observable.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

    Returns:
    :   The error-mitigating decorator to be applied to an executor function.

### Readout-Error Mitigation[#](#readout-error-mitigation "Link to this heading")

#### Postselection[#](#module-mitiq.rem.post_select "Link to this heading")

mitiq.rem.post\_select.post\_select(*result*, *selector*, *inverted=False*)[[source]](_modules/mitiq/rem/post_select.html#post_select)[#](#mitiq.rem.post_select.post_select "Link to this definition")
:   Returns only the bitstrings which satisfy the predicate in `selector`.

    Parameters:
    :   * **result** ([`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")) – List of bitstrings.
        * **selector** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]], [`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")]) –

          Predicate for which bitstrings to select. Examples:

          + `selector = lambda bitstring: sum(bitstring) == k`
            - Select all bitstrings of Hamming weight `k`.
          + `selector = lambda bitstring: sum(bitstring) <= k`
            - Select all bitstrings of Hamming weight at most `k`.
          + `selector = lambda bitstring: bitstring[0] == 1`
            - Select all bitstrings such that the first bit is 1.
        * **inverted** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – Invert the selector predicate so that bitstrings which obey
          `selector(bitstring) == False` are selected and returned.

    Return type:
    :   [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")

#### REM Technique[#](#module-mitiq.rem.rem "Link to this heading")

Readout Confusion Inversion.

mitiq.rem.rem.execute\_with\_rem(*circuit*, *executor*, *observable*, *\**, *inverse\_confusion\_matrix*)[[source]](_modules/mitiq/rem/rem.html#execute_with_rem)[#](#mitiq.rem.rem.execute_with_rem "Link to this definition")
:   Returns the readout error mitigated expectation value utilizing an
    inverse confusion matrix.

    Parameters:
    :   * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `MeasurementResult`.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the expectation value of (required).
        * **inverse\_confusion\_matrix** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – The inverse confusion matrix to apply to the
          probability vector estimated with noisy measurement results.
        * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`])

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value estimated with REM.

mitiq.rem.rem.mitigate\_executor(*executor*, *\**, *inverse\_confusion\_matrix*)[[source]](_modules/mitiq/rem/rem.html#mitigate_executor)[#](#mitiq.rem.rem.mitigate_executor "Link to this definition")
:   Returns a modified version of the input ‘executor’ which is
    error-mitigated with readout confusion inversion (RCI).
    The type of the output executor will be equal to the type of
    the input executor: an [`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") object or a Python callable.

    Parameters:
    :   * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `MeasurementResult`.
        * **inverse\_confusion\_matrix** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – The inverse confusion matrix to apply to the
          probability vector estimated with noisy measurement results.

    Return type:
    :   [`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]

    Returns:
    :   The error-mitigated version of the input executor.

mitiq.rem.rem.rem\_decorator(*\**, *inverse\_confusion\_matrix*)[[source]](_modules/mitiq/rem/rem.html#rem_decorator)[#](#mitiq.rem.rem.rem_decorator "Link to this definition")
:   Decorator which adds an error-mitigation layer based on readout
    confusion inversion (RCI) to an executor function, i.e., a function
    which executes a quantum circuit with an arbitrary backend and returns
    a `MeasurementResult`.

    Parameters:
    :   **inverse\_confusion\_matrix** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]) – The inverse confusion matrix to apply to the
        probability vector estimated with noisy measurement results
        (required).

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]]

    Returns:
    :   The error-mitigating decorator to be applied to an executor function.

### Zero Noise Extrapolation[#](#zero-noise-extrapolation "Link to this heading")

#### Zero Noise Extrapolation (High-Level Tools)[#](#module-mitiq.zne.zne "Link to this heading")

High-level zero-noise extrapolation tools.

mitiq.zne.zne.combine\_results(*scale\_factors*, *results*, *extrapolation\_method*)[[source]](_modules/mitiq/zne/zne.html#combine_results)[#](#mitiq.zne.zne.combine_results "Link to this definition")
:   Computes the error-mitigated expectation value associated to the
    input results from executing the scaled circuits, via the application
    of zero-noise extrapolation (ZNE).

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – An array of noise scale factors.
        * **results** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – An array storing the results of running the scaled circuits.
        * **extrapolation\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The method of extrapolation to use when fitting
          the measured results. A list of built-in functions can be found
          in `mitiq.zne.inference`.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value estimated with ZNE.

mitiq.zne.zne.construct\_circuits(*circuit*, *scale\_factors*, *scale\_method=<function fold\_gates\_at\_random>*)[[source]](_modules/mitiq/zne/zne.html#construct_circuits)[#](#mitiq.zne.zne.construct_circuits "Link to this definition")
:   Given a circuit, scale\_factors and a scale\_method, outputs a list
    :   of circuits that will be used in ZNE.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit to execute with ZNE.
        * **scale\_factors** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – An array of noise scale factors.
        * **scale\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – The function for scaling the noise of a quantum circuit.
          A list of built-in functions can be found in `mitiq.zne.scaling`.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   The scaled circuits using the scale\_method.

mitiq.zne.zne.execute\_with\_zne(*circuit*, *executor*, *observable=None*, *\**, *factory=None*, *scale\_noise=<function fold\_gates\_at\_random>*, *num\_to\_average=1*)[[source]](_modules/mitiq/zne/zne.html#execute_with_zne)[#](#mitiq.zne.zne.execute_with_zne "Link to this definition")
:   Estimates the error-mitigated expectation value associated to the
    input circuit, via the application of zero-noise extrapolation (ZNE).

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit to execute with ZNE.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `QuantumResult` (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
          `None`, the `executor` must return an expectation value.
          Otherwise, the `QuantumResult` returned by `executor` is used
          to compute the expectation of the observable.
        * **factory** ([`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – `Factory` object that determines the zero-noise
          extrapolation method.
        * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – The function for scaling the noise of a quantum circuit.
          A list of built-in functions can be found in `mitiq.zne.scaling`.
        * **num\_to\_average** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of times expectation values are computed by
          the executor after each call to `scale_noise`, then averaged.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value estimated with ZNE.

mitiq.zne.zne.mitigate\_executor(*executor*, *observable=None*, *\**, *factory=None*, *scale\_noise=<function fold\_gates\_at\_random>*, *num\_to\_average=1*)[[source]](_modules/mitiq/zne/zne.html#mitigate_executor)[#](#mitiq.zne.zne.mitigate_executor "Link to this definition")
:   Returns a modified version of the input ‘executor’ which is
    error-mitigated with zero-noise extrapolation (ZNE).

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A function that executes a circuit and returns the
          unmitigated QuantumResult (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor must return an expectation value. Otherwise,
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **factory** ([`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Factory object determining the zero-noise extrapolation
          method.
        * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function for scaling the noise of a quantum circuit.
        * **num\_to\_average** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of times expectation values are computed by
          the executor after each call to scale\_noise, then averaged.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   The error-mitigated version of the input executor.

mitiq.zne.zne.zne\_decorator(*observable=None*, *\**, *factory=None*, *scale\_noise=<function fold\_gates\_at\_random>*, *num\_to\_average=1*)[[source]](_modules/mitiq/zne/zne.html#zne_decorator)[#](#mitiq.zne.zne.zne_decorator "Link to this definition")
:   Decorator which adds an error-mitigation layer based on zero-noise
    extrapolation (ZNE) to an executor function, i.e., a function which
    executes a quantum circuit with an arbitrary backend and returns a
    `QuantumResult` (e.g. an expectation value).

    Parameters:
    :   * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor being decorated must return an expectation value.
          Otherwise, the QuantumResult returned by the executor is used
          to compute the expectation of the observable.
        * **factory** ([`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Factory object determining the zero-noise extrapolation
          method.
        * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function for scaling the noise of a quantum circuit.
        * **num\_to\_average** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of times expectation values are computed by
          the executor after each call to scale\_noise, then averaged.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

    Returns:
    :   The error-mitigating decorator to be applied to an executor function.

#### Inference and Extrapolation: Factories[#](#module-mitiq.zne.inference "Link to this heading")

Classes corresponding to different zero-noise extrapolation methods.

*class* mitiq.zne.inference.AdaExpFactory(*steps*, *scale\_factor=2.0*, *asymptote=None*, *avoid\_log=False*, *max\_scale\_factor=6.0*)[[source]](_modules/mitiq/zne/inference.html#AdaExpFactory)[#](#mitiq.zne.inference.AdaExpFactory "Link to this definition")
:   Factory object implementing an adaptive zero-noise extrapolation
    algorithm assuming an exponential ansatz y(x) = a + b \* exp(-c \* x),
    with c > 0.

    The noise scale factors are are chosen adaptively at each step,
    depending on the history of collected results.

    If y(x->inf) is unknown, the ansatz y(x) is fitted with a non-linear
    optimization.

    If y(x->inf) is given and avoid\_log=False, the exponential
    model is mapped into a linear model by logarithmic transformation.

    Parameters:
    :   * **steps** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of optimization steps. At least 3 are necessary.
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The second noise scale factor (the first is always 1.0).
          Further scale factors are adaptively determined.
        * **asymptote** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The infinite-noise limit y(x->inf) (optional argument).
        * **avoid\_log** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If set to True, the exponential model is not linearized
          with a logarithm and a non-linear fit is applied even if asymptote
          is not None. The default value is False.
        * **max\_scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Maximum noise scale factor. Default is 6.0.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    *static* extrapolate(*scale\_factors*, *exp\_values*, *asymptote=None*, *avoid\_log=False*, *eps=1e-06*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#AdaExpFactory.extrapolate)[#](#mitiq.zne.inference.AdaExpFactory.extrapolate "Link to this definition")
    :   Static method which evaluates the extrapolation to the zero-noise
        limit assuming an exponential ansatz y(x) = a + b \* exp(-c \* x),
        with c > 0.

        If y(x->inf) is unknown, the ansatz y(x) is fitted with a non-linear
        optimization.

        If y(x->inf) is given and avoid\_log=False, the exponential
        model is mapped into a linear model by a logarithmic transformation.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
            * **asymptote** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The infinite-noise limit y(x->inf) (optional argument).
            * **avoid\_log** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If set to True, the exponential model is not linearized
              with a logarithm and a non-linear fit is applied even if
              asymptote is not None. The default value is False.
            * **eps** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Epsilon to regularize log(sign(scale\_factors - asymptote))
              when the argument is to close to zero or negative.
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False (default), only the zero-noise limit is
              returned. If True, additional results are returned too.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

        Returns:
        :   The extrapolated zero-noise limit. If full\_output is True, also
            returns
            \* standard deviation of the extrapolated zero-noise limit,
            \* optimal parameters of the best-fit model,
            \* parameter covariance matrix of best-fit model,
            \* best-fit model as a Callable[[float], float] function.

        Raises:
        :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If the arguments are not consistent with the
              extrapolation model.
            * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
            * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

        Note

        This static method computes the zero-noise limit from input
        parameters. To compute the zero-noise limit from the Factory
        parameters, use the `reduce` method.

    is\_converged()[[source]](_modules/mitiq/zne/inference.html#AdaExpFactory.is_converged)[#](#mitiq.zne.inference.AdaExpFactory.is_converged "Link to this definition")
    :   Returns True if all the needed expectation values have been
        computed, else False.

        Return type:
        :   [`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")

    next()[[source]](_modules/mitiq/zne/inference.html#AdaExpFactory.next)[#](#mitiq.zne.inference.AdaExpFactory.next "Link to this definition")
    :   Returns a dictionary of parameters to execute a circuit at.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    reduce()[[source]](_modules/mitiq/zne/inference.html#AdaExpFactory.reduce)[#](#mitiq.zne.inference.AdaExpFactory.reduce "Link to this definition")
    :   Returns the zero-noise limit found by fitting an exponential
        model to the internal data stored in the factory.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

        Returns:
        :   The zero-noise limit.

*class* mitiq.zne.inference.AdaptiveFactory[[source]](_modules/mitiq/zne/inference.html#AdaptiveFactory)[#](#mitiq.zne.inference.AdaptiveFactory "Link to this definition")
:   Abstract class designed to adaptively produce a new noise scaling
    parameter based on a historical stack of previous noise scale parameters
    (“self.\_instack”) and previously estimated expectation values
    (“self.\_outstack”).

    Specific zero-noise extrapolation algorithms which are adaptive are derived
    from this class.

    *abstract* is\_converged()[[source]](_modules/mitiq/zne/inference.html#AdaptiveFactory.is_converged)[#](#mitiq.zne.inference.AdaptiveFactory.is_converged "Link to this definition")
    :   Returns True if all needed expectation values have been computed,
        else False.

        Return type:
        :   [`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")

    *abstract* next()[[source]](_modules/mitiq/zne/inference.html#AdaptiveFactory.next)[#](#mitiq.zne.inference.AdaptiveFactory.next "Link to this definition")
    :   Returns a dictionary of parameters to execute a circuit at.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    *abstract* reduce()[[source]](_modules/mitiq/zne/inference.html#AdaptiveFactory.reduce)[#](#mitiq.zne.inference.AdaptiveFactory.reduce "Link to this definition")
    :   Returns the extrapolation to the zero-noise limit.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    run(*qp*, *executor*, *observable=None*, *scale\_noise=<function fold\_gates\_at\_random>*, *num\_to\_average=1*, *max\_iterations=100*)[[source]](_modules/mitiq/zne/inference.html#AdaptiveFactory.run)[#](#mitiq.zne.inference.AdaptiveFactory.run "Link to this definition")
    :   Evaluates a sequence of expectation values by executing quantum
        circuits until enough data is collected (or iterations reach
        “max\_iterations”).

        Parameters:
        :   * **qp** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Circuit to mitigate.
            * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A `mitiq.Executor` or a function which inputs a (list
              of) quantum circuits and outputs a (list of)
              `mitiq.QuantumResult` s.
            * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
              None, the executor must return an expectation value.
              Otherwise, the QuantumResult returned by executor is used
              to compute the expectation of the observable.
            * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function that scales the noise level of a quantum
              circuit.
            * **num\_to\_average** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of times expectation values are computed by
              the executor after each call to scale\_noise, then averaged.
            * **max\_iterations** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Maximum number of iterations (optional).

        Return type:
        :   [`AdaptiveFactory`](#mitiq.zne.inference.AdaptiveFactory "mitiq.zne.inference.AdaptiveFactory")

    run\_classical(*scale\_factor\_to\_expectation\_value*, *max\_iterations=100*)[[source]](_modules/mitiq/zne/inference.html#AdaptiveFactory.run_classical)[#](#mitiq.zne.inference.AdaptiveFactory.run_classical "Link to this definition")
    :   Evaluates a sequence of expectation values until enough
        data is collected (or iterations reach “max\_iterations”).

        Parameters:
        :   * **scale\_factor\_to\_expectation\_value** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Function mapping a noise scale
              factor to an expectation value. If shot\_list is not None,
              “shots” must be an argument of this function.
            * **max\_iterations** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Maximum number of iterations (optional).
              Default: 100.

        Raises:
        :   [**ConvergenceWarning**](#mitiq.zne.inference.ConvergenceWarning "mitiq.zne.inference.ConvergenceWarning") – If iteration loop stops before convergence.

        Return type:
        :   [`AdaptiveFactory`](#mitiq.zne.inference.AdaptiveFactory "mitiq.zne.inference.AdaptiveFactory")

*class* mitiq.zne.inference.BatchedFactory(*scale\_factors*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#BatchedFactory)[#](#mitiq.zne.inference.BatchedFactory "Link to this definition")
:   Abstract class of a non-adaptive Factory initialized with a
    pre-determined set of scale factors.

    Specific (non-adaptive) extrapolation algorithms are derived from this
    class by defining the reduce method.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which expectation
          values should be measured.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the
          number of samples taken for each expectation value. If this
          argument is explicitly passed to the factory, it must have the
          same length of scale\_factors and the executor function must
          accept “shots” as a valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If the number of scale factors is less than 2.
        * [**TypeError**](https://docs.python.org/3.11/library/exceptions.html#TypeError "(in Python v3.11)") – If shot\_list is provided and has any non-integer values.

    *abstract static* extrapolate(*\*args*, *\*\*kwargs*)[[source]](_modules/mitiq/zne/inference.html#BatchedFactory.extrapolate)[#](#mitiq.zne.inference.BatchedFactory.extrapolate "Link to this definition")
    :   Returns the extrapolation to the zero-noise limit.

        Parameters:
        :   * **args** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))
            * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

    reduce()[[source]](_modules/mitiq/zne/inference.html#BatchedFactory.reduce)[#](#mitiq.zne.inference.BatchedFactory.reduce "Link to this definition")
    :   Evaluates the zero-noise limit found by fitting according to
        the factory’s extrapolation method.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

        Returns:
        :   The zero-noise limit.

    run(*qp*, *executor*, *observable=None*, *scale\_noise=<function fold\_gates\_at\_random>*, *num\_to\_average=1*)[[source]](_modules/mitiq/zne/inference.html#BatchedFactory.run)[#](#mitiq.zne.inference.BatchedFactory.run "Link to this definition")
    :   Computes the expectation values at each scale factor and stores them
        in the factory. If the executor returns a single expectation value, the
        circuits are run sequentially. If the executor is batched and returns
        a list of expectation values (one for each circuit), then the circuits
        are sent to the backend as a single job. To detect if an executor is
        batched, it must be annotated with a return type that is one of the
        following:

        > * Iterable[float]
        > * List[float]
        > * Sequence[float]
        > * Tuple[float]
        > * numpy.ndarray

        Parameters:
        :   * **qp** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Quantum circuit to run.
            * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A `mitiq.Executor` or a function which inputs a (list
              of) quantum circuits and outputs a (list of)
              `mitiq.QuantumResult` s.
            * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
              None, the executor must return an expectation value.
              Otherwise, the QuantumResult returned by executor is used
              to compute the expectation of the observable.
            * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Noise scaling function.
            * **num\_to\_average** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of circuits executed for each noise
              scale factor. This parameter can be used to increase the
              precision of the “executor” or to average the effect of a
              non-deterministic “scale\_noise” function.

        Return type:
        :   [`BatchedFactory`](#mitiq.zne.inference.BatchedFactory "mitiq.zne.inference.BatchedFactory")

    run\_classical(*scale\_factor\_to\_expectation\_value*)[[source]](_modules/mitiq/zne/inference.html#BatchedFactory.run_classical)[#](#mitiq.zne.inference.BatchedFactory.run_classical "Link to this definition")
    :   Computes expectation values by calling the input function at each
        scale factor.

        Parameters:
        :   **scale\_factor\_to\_expectation\_value** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Function mapping a noise scale
            factor to an expectation value. If shot\_list is not None,
            “shots” must be an argument of this function.

        Return type:
        :   [`BatchedFactory`](#mitiq.zne.inference.BatchedFactory "mitiq.zne.inference.BatchedFactory")

*exception* mitiq.zne.inference.ConvergenceWarning[[source]](_modules/mitiq/zne/inference.html#ConvergenceWarning)[#](#mitiq.zne.inference.ConvergenceWarning "Link to this definition")
:   Warning raised by [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory") objects when
    their run\_classical method fails to converge.

*class* mitiq.zne.inference.ExpFactory(*scale\_factors*, *asymptote=None*, *avoid\_log=False*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#ExpFactory)[#](#mitiq.zne.inference.ExpFactory "Link to this definition")
:   Factory object implementing a zero-noise extrapolation algorithm assuming
    an exponential ansatz y(x) = a + b \* exp(-c \* x), with c > 0.

    If y(x->inf) is unknown, the ansatz y(x) is fitted with a non-linear
    optimization.

    If y(x->inf) is given and avoid\_log=False, the exponential
    model is mapped into a linear model by a logarithmic transformation.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which expectation
          values should be measured.
        * **asymptote** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Infinite-noise limit (optional argument).
        * **avoid\_log** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If set to True, the exponential model is not linearized
          with a logarithm and a non-linear fit is applied even if asymptote
          is not None. The default value is False.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the number
          of samples taken for each expectation value. If this argument is
          explicitly passed to the factory, it must have the same length of
          scale\_factors and the executor function must accept “shots” as a
          valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    *static* extrapolate(*scale\_factors*, *exp\_values*, *asymptote=None*, *avoid\_log=False*, *eps=1e-06*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#ExpFactory.extrapolate)[#](#mitiq.zne.inference.ExpFactory.extrapolate "Link to this definition")
    :   Static method which evaluates the extrapolation to the zero-noise
        limit assuming an exponential ansatz y(x) = a + b \* exp(-c \* x),
        with c > 0.

        If y(x->inf) is unknown, the ansatz y(x) is fitted with a non-linear
        optimization.

        If y(x->inf) is given and avoid\_log=False, the exponential
        model is mapped into a linear model by a logarithmic transformation.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
            * **asymptote** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The infinite-noise limit y(x->inf) (optional argument).
            * **avoid\_log** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If set to True, the exponential model is not linearized
              with a logarithm and a non-linear fit is applied even if
              asymptote is not None. The default value is False.
            * **eps** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Epsilon to regularize log(sign(scale\_factors - asymptote))
              when the argument is to close to zero or negative.
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False (default), only the zero-noise limit is
              returned. If True, additional information about the
              extrapolated limit is returned too.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

        Returns:
        :   The extrapolated zero-noise limit. If full\_output is True, also
            returns
            \* standard deviation of the extrapolated zero-noise limit,
            \* optimal parameters of the best-fit model,
            \* parameter covariance matrix of best-fit model,
            \* best-fit model as a Callable[[float], float] function.

        Raises:
        :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If the arguments are not consistent with the
              extrapolation model.
            * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
            * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

        Note

        This static method computes the zero-noise limit from input
        parameters. To compute the zero-noise limit from the Factory
        parameters, use the `reduce` method.

*exception* mitiq.zne.inference.ExtrapolationError[[source]](_modules/mitiq/zne/inference.html#ExtrapolationError)[#](#mitiq.zne.inference.ExtrapolationError "Link to this definition")
:   Error raised by [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory") objects when
    the extrapolation fit fails.

*exception* mitiq.zne.inference.ExtrapolationWarning[[source]](_modules/mitiq/zne/inference.html#ExtrapolationWarning)[#](#mitiq.zne.inference.ExtrapolationWarning "Link to this definition")
:   Warning raised by [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory") objects when
    the extrapolation fit is ill-conditioned.

*class* mitiq.zne.inference.Factory[[source]](_modules/mitiq/zne/inference.html#Factory)[#](#mitiq.zne.inference.Factory "Link to this definition")
:   Abstract base class which performs the classical parts of zero-noise
    extrapolation. This minimally includes:

    > * scaling circuits,
    > * sending jobs to execute,
    > * collecting the results,
    > * fitting the collected data,
    > * Extrapolating to the zero-noise limit.

    If all scale factors are set a priori, the jobs can be batched. This is
    handled by a BatchedFactory.

    If the next scale factor depends on the previous history of results,
    jobs are run sequentially. This is handled by an AdaptiveFactory.

    get\_expectation\_values()[[source]](_modules/mitiq/zne/inference.html#Factory.get_expectation_values)[#](#mitiq.zne.inference.Factory.get_expectation_values "Link to this definition")
    :   Returns the expectation values computed by the factory.

        Return type:
        :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    get\_extrapolation\_curve()[[source]](_modules/mitiq/zne/inference.html#Factory.get_extrapolation_curve)[#](#mitiq.zne.inference.Factory.get_extrapolation_curve "Link to this definition")
    :   Returns the extrapolation curve, i.e., a function which
        inputs a noise scale factor and outputs the associated expectation
        value. This function is the solution of the regression problem
        used to evaluate the zero-noise extrapolation.

        Return type:
        :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    get\_optimal\_parameters()[[source]](_modules/mitiq/zne/inference.html#Factory.get_optimal_parameters)[#](#mitiq.zne.inference.Factory.get_optimal_parameters "Link to this definition")
    :   Returns the optimal model parameters produced by the extrapolation
        fit.

        Return type:
        :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    get\_parameters\_covariance()[[source]](_modules/mitiq/zne/inference.html#Factory.get_parameters_covariance)[#](#mitiq.zne.inference.Factory.get_parameters_covariance "Link to this definition")
    :   Returns the covariance matrix of the model parameters produced by
        the extrapolation fit.

        Return type:
        :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]

    get\_scale\_factors()[[source]](_modules/mitiq/zne/inference.html#Factory.get_scale_factors)[#](#mitiq.zne.inference.Factory.get_scale_factors "Link to this definition")
    :   Returns the scale factors that were either passed in to the factory
        or at which the factory has computed expectation values.

        Return type:
        :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    get\_zero\_noise\_limit()[[source]](_modules/mitiq/zne/inference.html#Factory.get_zero_noise_limit)[#](#mitiq.zne.inference.Factory.get_zero_noise_limit "Link to this definition")
    :   Returns the last evaluation of the zero-noise limit
        computed by the factory. To re-evaluate
        its value, the method ‘reduce’ should be called first.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    get\_zero\_noise\_limit\_error()[[source]](_modules/mitiq/zne/inference.html#Factory.get_zero_noise_limit_error)[#](#mitiq.zne.inference.Factory.get_zero_noise_limit_error "Link to this definition")
    :   Returns the extrapolation error representing the uncertainty
        affecting the zero-noise limit. It is deduced by error propagation
        from the covariance matrix associated to the fit parameters.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

        Note: this quantity is only related to the ability of the model
        :   to fit the measured data. Therefore, it may underestimate the
            actual error existing between the zero-noise limit and the
            true ideal expectation value.

    plot\_data()[[source]](_modules/mitiq/zne/inference.html#Factory.plot_data)[#](#mitiq.zne.inference.Factory.plot_data "Link to this definition")
    :   Returns a figure which is a scatter plot of (x, y) data where x are
        scale factors at which expectation values have been computed, and y are
        the associated expectation values.

        Returns:
        :   A 2D scatter plot described above.

        Return type:
        :   fig

    plot\_fit()[[source]](_modules/mitiq/zne/inference.html#Factory.plot_fit)[#](#mitiq.zne.inference.Factory.plot_fit "Link to this definition")
    :   Returns a figure which plots the experimental data as well as the
        best fit curve.

        Returns:
        :   A figure which plots the best fit curve as well as the data.

        Return type:
        :   fig

    push(*instack\_val*, *outstack\_val*)[[source]](_modules/mitiq/zne/inference.html#Factory.push)[#](#mitiq.zne.inference.Factory.push "Link to this definition")
    :   Appends “instack\_val” to “self.\_instack” and “outstack\_val” to
        “self.\_outstack”. Each time a new expectation value is computed this
        method should be used to update the internal state of the Factory.

        Parameters:
        :   * **instack\_val** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")])
            * **outstack\_val** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))

        Return type:
        :   [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory")

    reset()[[source]](_modules/mitiq/zne/inference.html#Factory.reset)[#](#mitiq.zne.inference.Factory.reset "Link to this definition")
    :   Resets the internal state of the Factory.

        Return type:
        :   [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory")

    *abstract* run(*qp*, *executor*, *observable=None*, *scale\_noise=<function fold\_gates\_at\_random>*, *num\_to\_average=1*)[[source]](_modules/mitiq/zne/inference.html#Factory.run)[#](#mitiq.zne.inference.Factory.run "Link to this definition")
    :   Calls the executor function on noise-scaled quantum circuit and
        stores the results.

        Parameters:
        :   * **qp** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – Quantum circuit to scale noise in.
            * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A `mitiq.Executor` or a function which inputs a (list
              of) quantum circuits and outputs a (list of)
              `mitiq.QuantumResult` s.
            * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
              None, the executor must return an expectation value.
              Otherwise, the QuantumResult returned by executor is used
              to compute the expectation of the observable.
            * **scale\_noise** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]) – Function which inputs a quantum circuit and outputs
              a noise-scaled quantum circuit.
            * **num\_to\_average** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of times the executor function is called
              on each noise-scaled quantum circuit.

        Return type:
        :   [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory")

    *abstract* run\_classical(*scale\_factor\_to\_expectation\_value*)[[source]](_modules/mitiq/zne/inference.html#Factory.run_classical)[#](#mitiq.zne.inference.Factory.run_classical "Link to this definition")
    :   Calls the function scale\_factor\_to\_expectation\_value at each scale
        factor of the factory, and stores the results.

        Parameters:
        :   **scale\_factor\_to\_expectation\_value** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – A function which inputs a scale
            factor and outputs an expectation value. This does not have to
            involve a quantum processor making this a “classical analogue”
            of the run method.

        Return type:
        :   [`Factory`](#mitiq.zne.inference.Factory "mitiq.zne.inference.Factory")

*class* mitiq.zne.inference.FakeNodesFactory(*scale\_factors*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#FakeNodesFactory)[#](#mitiq.zne.inference.FakeNodesFactory "Link to this definition")
:   Factory object implementing a modified version [[De2020polynomial]](#de2020polynomial) of
    Richardson extrapolation. In this version the original set of scale factors
    is mapped to a new set of fake nodes, known as Chebyshev-Lobatto points.
    This method may give a better interpolation for particular types of curves
    and if the number of scale factors is large (> 10). One should be aware
    that, in many other cases, the fake nodes extrapolation method is usually
    not superior to standard Richardson extrapolation.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which
          expectation values should be measured.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the number
          of samples taken for each expectation value. If this
          argument is explicitly passed to the factory, it must have
          the same length of scale\_factors and the executor function
          must accept “shots” as a valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    [De2020polynomial]

    : S.De Marchia. F. Marchetti, E.Perracchionea
    and D.Poggialia,
    “Polynomial interpolation via mapped bases without resampling,”
    *Journ of Comp. and App. Math.* **364**, 112347 (2020),
    (<https://www.sciencedirect.com/science/article/abs/pii/S0377042719303449>).

    *static* extrapolate(*scale\_factors*, *exp\_values*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#FakeNodesFactory.extrapolate)[#](#mitiq.zne.inference.FakeNodesFactory.extrapolate "Link to this definition")
    :   Returns the extrapolation to the zero-noise limit.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")])
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")])
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)"))

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

*class* mitiq.zne.inference.LinearFactory(*scale\_factors*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#LinearFactory)[#](#mitiq.zne.inference.LinearFactory "Link to this definition")
:   Factory object implementing zero-noise extrapolation based
    on a linear fit.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which
          expectation values should be measured.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the number
          of samples taken for each expectation value. If this
          argument is explicitly passed to the factory, it must have
          the same length of scale\_factors and the executor function
          must accept “shots” as a valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    *static* extrapolate(*scale\_factors*, *exp\_values*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#LinearFactory.extrapolate)[#](#mitiq.zne.inference.LinearFactory.extrapolate "Link to this definition")
    :   Static method which evaluates the linear extrapolation to the
        zero-noise limit.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False (default), only the zero-noise limit is
              returned. If True, additional results are returned too.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

        Returns:
        :   The extrapolated zero-noise limit. If full\_output is True, also
            returns
            \* standard deviation of the extrapolated zero-noise limit,
            \* optimal parameters of the best-fit model,
            \* parameter covariance matrix of best-fit model,
            \* best-fit model as a Callable[[float], float] function.

        Raises:
        :   [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

        Note

        This static method computes the zero-noise limit from input
        parameters. To compute the zero-noise limit from the Factory
        parameters, use the `reduce` method.

*class* mitiq.zne.inference.PolyExpFactory(*scale\_factors*, *order*, *asymptote=None*, *avoid\_log=False*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#PolyExpFactory)[#](#mitiq.zne.inference.PolyExpFactory "Link to this definition")
:   Factory object implementing a zero-noise extrapolation algorithm assuming
    an (almost) exponential ansatz with a non linear exponent
    y(x) = a + sign \* exp(z(x)), where z(x) is a polynomial of a given order.

    The parameter “sign” is a sign variable which can be either 1 or -1,
    corresponding to decreasing and increasing exponentials, respectively.
    The parameter “sign” is automatically deduced from the data.

    If y(x->inf) is unknown, the ansatz y(x) is fitted with a non-linear
    optimization.

    If y(x->inf) is given and avoid\_log=False, the exponential
    model is mapped into a polynomial model by logarithmic transformation.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which
          expectation values should be measured.
        * **order** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Extrapolation order (degree of the polynomial z(x)).
          It cannot exceed len(scale\_factors) - 1.
          If asymptote is None, order cannot exceed
          len(scale\_factors) - 2.
        * **asymptote** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The infinite-noise limit y(x->inf) (optional argument).
        * **avoid\_log** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If set to True, the exponential model is not linearized
          with a logarithm and a non-linear fit is applied even
          if asymptote is not None. The default value is False.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the number
          of samples taken for each expectation value. If this
          argument is explicitly passed to the factory, it must have
          the same length of scale\_factors and the executor function
          must accept “shots” as a valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    *static* extrapolate(*scale\_factors*, *exp\_values*, *order*, *asymptote=None*, *avoid\_log=False*, *eps=1e-06*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#PolyExpFactory.extrapolate)[#](#mitiq.zne.inference.PolyExpFactory.extrapolate "Link to this definition")
    :   Static method which evaluates the extrapolation to the
        zero-noise limit with an exponential ansatz (whose exponent
        is a polynomial of degree “order”).

        The exponential ansatz is y(x) = a + sign \* exp(z(x)) where z(x) is a
        polynomial and “sign” is either +1 or -1 corresponding to decreasing
        and increasing exponentials, respectively. The parameter “sign” is
        automatically deduced from the data.

        It is also assumed that z(x–>inf) = -inf, such that y(x–>inf) –> a.

        If asymptote is None, the ansatz y(x) is fitted with a non-linear
        optimization.

        If asymptote is given and avoid\_log=False, a linear fit with respect to
        z(x) := log[sign \* (y(x) - asymptote)] is performed.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
            * **asymptote** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The infinite-noise limit y(x->inf) (optional argument).
            * **order** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The degree of the polynomial z(x).
            * **avoid\_log** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If set to True, the exponential model is not linearized
              with a logarithm and a non-linear fit is applied even if
              asymptote is not None. The default value is False.
            * **eps** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Epsilon to regularize log(sign(scale\_factors - asymptote))
              when the argument is to close to zero or negative.
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False (default), only the zero-noise limit is
              returned. If True, additional information about the
              extrapolated limit is returned too.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

        Returns:
        :   The extrapolated zero-noise limit. If full\_output is True, also
            returns
            \* standard deviation of the extrapolated zero-noise limit,
            \* optimal parameters of the best-fit model,
            \* parameter covariance matrix of best-fit model,
            \* best-fit model as a Callable[[float], float] function.

        Raises:
        :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If the arguments are not consistent with the
              extrapolation model.
            * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
            * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

        Note

        This static method computes the zero-noise limit from input
        parameters. To compute the zero-noise limit from the Factory
        parameters, use the `reduce` method.

*class* mitiq.zne.inference.PolyFactory(*scale\_factors*, *order*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#PolyFactory)[#](#mitiq.zne.inference.PolyFactory "Link to this definition")
:   Factory object implementing a zero-noise extrapolation algorithm based
    on a polynomial fit.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which
          expectation values should be measured.
        * **order** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Extrapolation order (degree of the polynomial fit).
          It cannot exceed len(scale\_factors) - 1.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the number
          of samples taken for each expectation value. If this
          argument is explicitly passed to the factory, it must have
          the same length of scale\_factors and the executor function
          must accept “shots” as a valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    Note

    RichardsonFactory and LinearFactory are special cases of PolyFactory.

    *static* extrapolate(*scale\_factors*, *exp\_values*, *order*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#PolyFactory.extrapolate)[#](#mitiq.zne.inference.PolyFactory.extrapolate "Link to this definition")
    :   Static method which evaluates a polynomial extrapolation to the
        zero-noise limit.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
            * **order** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The extrapolation order (degree of the polynomial fit).
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False (default), only the zero-noise limit is
              returned. If True, additional information about the
              extrapolated limit is returned too.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

        Returns:
        :   The extrapolated zero-noise limit. If full\_output is True, also
            returns
            \* standard deviation of the extrapolated zero-noise limit,
            \* optimal parameters of the best-fit model,
            \* parameter covariance matrix of best-fit model,
            \* best-fit model as a Callable[[float], float] function.

        Raises:
        :   [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

        Note

        This static method computes the zero-noise limit from input
        parameters. To compute the zero-noise limit from the Factory
        parameters, use the `reduce` method.

*class* mitiq.zne.inference.RichardsonFactory(*scale\_factors*, *shot\_list=None*)[[source]](_modules/mitiq/zne/inference.html#RichardsonFactory)[#](#mitiq.zne.inference.RichardsonFactory "Link to this definition")
:   Factory object implementing Richardson extrapolation.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Sequence of noise scale factors at which
          expectation values should be measured.
        * **shot\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional sequence of integers corresponding to the number
          of samples taken for each expectation value. If this
          argument is explicitly passed to the factory, it must have
          the same length of scale\_factors and the executor function
          must accept “shots” as a valid keyword argument.

    Raises:
    :   * [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If data is not consistent with the extrapolation model.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

    *static* extrapolate(*scale\_factors*, *exp\_values*, *full\_output=False*)[[source]](_modules/mitiq/zne/inference.html#RichardsonFactory.extrapolate)[#](#mitiq.zne.inference.RichardsonFactory.extrapolate "Link to this definition")
    :   Static method which evaluates the Richardson extrapolation to the
        :   zero-noise limit.

        Parameters:
        :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
            * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
            * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False (default), only the zero-noise limit is
              returned. If True, additional results are returned too.

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

        Returns:
        :   The extrapolated zero-noise limit. If full\_output is True, also
            returns
            \* standard deviation of the extrapolated zero-noise limit,
            \* optimal parameters of the best-fit model,
            \* parameter covariance matrix of best-fit model,
            \* best-fit model as a Callable[[float], float] function.

        Raises:
        :   [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

        Note

        This static method computes the zero-noise limit from input
        parameters. To compute the zero-noise limit from the Factory
        parameters, use the `reduce` method.

mitiq.zne.inference.mitiq\_curve\_fit(*ansatz*, *scale\_factors*, *exp\_values*, *init\_params=None*)[[source]](_modules/mitiq/zne/inference.html#mitiq_curve_fit)[#](#mitiq.zne.inference.mitiq_curve_fit "Link to this definition")
:   Fits the ansatz to the (scale factor, expectation value) data using
    `scipy.optimize.curve_fit`, returning the optimal parameters and
    covariance matrix of the parameters.

    Parameters:
    :   * **ansatz** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The model function used for zero-noise extrapolation. The first
          argument is the noise scale variable, the remaining arguments are
          the parameters to fit.
        * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
        * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
        * **init\_params** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Initial guess for the parameters. If None, the initial
          values are set to 1.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]]

    Returns:
    :   The array of optimal parameters and the covariance matrix of the
        parameters. If the fit is ill-conditioned, the covariance matrix may
        contain np.inf elements.

    Raises:
    :   * [**ExtrapolationError**](#mitiq.zne.inference.ExtrapolationError "mitiq.zne.inference.ExtrapolationError") – If the extrapolation fit fails.
        * [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

mitiq.zne.inference.mitiq\_polyfit(*scale\_factors*, *exp\_values*, *deg*, *weights=None*)[[source]](_modules/mitiq/zne/inference.html#mitiq_polyfit)[#](#mitiq.zne.inference.mitiq_polyfit "Link to this definition")
:   Fits the ansatz to the (scale factor, expectation value) data using
    `numpy.polyfit`, returning the optimal parameters and covariance matrix
    of the parameters.

    Parameters:
    :   * **scale\_factors** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of noise scale factors.
        * **exp\_values** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The array of expectation values.
        * **deg** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The degree of the polynomial fit.
        * **weights** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Buffer`, `_SupportsArray`[[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]], `_NestedSequence`[`_SupportsArray`[[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]], [`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`bytes`](https://docs.python.org/3.11/library/stdtypes.html#bytes "(in Python v3.11)"), `_NestedSequence`[[`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)") | [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)") | [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`bytes`](https://docs.python.org/3.11/library/stdtypes.html#bytes "(in Python v3.11)")], [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")]) – Optional array of weights for each sampled point.
          This is used to make a weighted least squares fit.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")]

    Returns:
    :   The optimal parameters and covariance matrix of the parameters.
        If there is not enough data to estimate the covariance matrix, it is
        returned as None.

    Raises:
    :   [**ExtrapolationWarning**](#mitiq.zne.inference.ExtrapolationWarning "mitiq.zne.inference.ExtrapolationWarning") – If the extrapolation fit is ill-conditioned.

#### Noise Scaling: Unitary Folding[#](#module-mitiq.zne.scaling.folding "Link to this heading")

Functions for local and global unitary folding on supported circuits.

*exception* mitiq.zne.scaling.folding.UnfoldableCircuitError[[source]](_modules/mitiq/zne/scaling/folding.html#UnfoldableCircuitError)[#](#mitiq.zne.scaling.folding.UnfoldableCircuitError "Link to this definition")

mitiq.zne.scaling.folding.fold\_all(*circuit*, *scale\_factor*, *exclude=frozenset({})*)[[source]](_modules/mitiq/zne/scaling/folding.html#fold_all)[#](#mitiq.zne.scaling.folding.fold_all "Link to this definition")
:   Returns a circuit with all gates folded locally.

    Parameters:
    :   * **circuit** (`Circuit`) – Circuit to fold.
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) –

          Approximate factor by which noise is scaled in the
          circuit. Each gate is folded round((scale\_factor - 1.0) / 2.0)
          times. For example:

          ```
          scale_factor | num_folds
          ------------------------
          1.0          | 0
          3.0          | 1
          5.0          | 2
          ```
        * **exclude** ([`frozenset`](https://docs.python.org/3.11/library/stdtypes.html#frozenset "(in Python v3.11)")[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]) –

          Do not fold these gates. Supported gate keys are listed in
          the following table.:

          ```
          Gate key    | Gate
          -------------------------
          "H"         | Hadamard
          "X"         | Pauli X
          "Y"         | Pauli Y
          "Z"         | Pauli Z
          "I"         | Identity
          "S"         | Phase gate
          "T"         | T gate
          "rx"        | X-rotation
          "ry"        | Y-rotation
          "rz"        | Z-rotation
          "CNOT"      | CNOT
          "CZ"        | CZ gate
          "SWAP"      | Swap
          "ISWAP"     | Imaginary swap
          "CSWAP"     | CSWAP
          "TOFFOLI"   | Toffoli gate
          "single"    | All single qubit gates
          "double"    | All two-qubit gates
          "triple"    | All three-qubit gates
          ```

    Return type:
    :   `Circuit`

mitiq.zne.scaling.folding.fold\_gates\_at\_random(*circuit*, *scale\_factor*, *seed=None*, *\*\*kwargs*)[[source]](_modules/mitiq/zne/scaling/folding.html#fold_gates_at_random)[#](#mitiq.zne.scaling.folding.fold_gates_at_random "Link to this definition")
:   Returns a new folded circuit by applying the map G -> G G^dag G to a
    subset of gates of the input circuit, different indices randomly sampled
    without replacement.

    The folded circuit has a number of gates approximately equal to
    scale\_factor \* n where n is the number of gates in the input circuit.

    For equal gate fidelities, this function reproduces the local unitary
    folding method defined in equation (5) of
    [[11](bibliography.html#id28 "Tudor Giurgica-Tiron, Yousef Hindy, Ryan LaRose, Andrea Mari, and William J. Zeng. Digital zero noise extrapolation for quantum error mitigation. (2020). arXiv:2005.10921.")].

    Parameters:
    :   * **circuit** (`Circuit`) – Circuit to fold.
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Factor to scale the circuit by. Any real number >= 1.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for random number generator.
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))

    Keyword Arguments:
    :   * **fidelities** (*Dict**[*[*str*](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")*,* [*float*](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")*]*) –

          Dictionary of gate fidelities. Each key
          is a string which specifies the gate and each value is the
          fidelity of that gate. When this argument is provided, folded
          gates contribute an amount proportional to their infidelity
          (1 - fidelity) to the total noise scaling. Fidelity values must be
          in the interval (0, 1]. Gates not specified have a default
          fidelity of 0.99\*\*n where n is the number of qubits the gates act
          on.

          Supported gate keys are listed in the following table.:

          ```
          Gate key    | Gate
          -------------------------
          "H"         | Hadamard
          "X"         | Pauli X
          "Y"         | Pauli Y
          "Z"         | Pauli Z
          "I"         | Identity
          "S"         | Phase gate
          "T"         | T gate
          "rx"        | X-rotation
          "ry"        | Y-rotation
          "rz"        | Z-rotation
          "CNOT"      | CNOT
          "CZ"        | CZ gate
          "SWAP"      | Swap
          "ISWAP"     | Imaginary swap
          "CSWAP"     | CSWAP
          "TOFFOLI"   | Toffoli gate
          "single"    | All single qubit gates
          "double"    | All two-qubit gates
          "triple"    | All three-qubit gates
          ```

          Keys for specific gates override values set by “single”, “double”,
          and “triple”.

          For example, fidelities = {“single”: 1.0, “H”, 0.99} sets all
          single-qubit gates except Hadamard to have fidelity one.
        * **squash\_moments** ([*bool*](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, all gates (including folded gates) are
          placed as early as possible in the circuit. If False, new moments
          are created for folded gates. This option only applies to QPROGRAM
          types which have a “moment” or “time” structure. Default is True.
        * **return\_mitiq** ([*bool*](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, returns a Mitiq circuit instead of
          the input circuit type (if different). Default is False.

    Returns:
    :   The folded quantum circuit as a QPROGRAM.

    Return type:
    :   folded

mitiq.zne.scaling.folding.fold\_global(*circuit*, *scale\_factor*, *\*\*kwargs*)[[source]](_modules/mitiq/zne/scaling/folding.html#fold_global)[#](#mitiq.zne.scaling.folding.fold_global "Link to this definition")
:   Returns a new circuit obtained by folding the global unitary of the
    input circuit.

    The returned folded circuit has a number of gates approximately equal to
    scale\_factor \* len(circuit).

    Parameters:
    :   * **circuit** (`Circuit`) – Circuit to fold.
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Factor to scale the circuit by.
        * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))

    Keyword Arguments:
    :   **return\_mitiq** ([*bool*](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, returns a Mitiq circuit instead of
        the input circuit type (if different). Default is False.

    Returns:
    :   the folded quantum circuit as a QPROGRAM.

    Return type:
    :   folded

#### Noise Scaling: Identity Insertion Scaling[#](#module-mitiq.zne.scaling.identity_insertion "Link to this heading")

Functions for scaling supported circuits by inserting layers of identity
gates.

*exception* mitiq.zne.scaling.identity\_insertion.UnscalableCircuitError[[source]](_modules/mitiq/zne/scaling/identity_insertion.html#UnscalableCircuitError)[#](#mitiq.zne.scaling.identity_insertion.UnscalableCircuitError "Link to this definition")

mitiq.zne.scaling.identity\_insertion.insert\_id\_layers(*input\_circuit*, *scale\_factor*)[[source]](_modules/mitiq/zne/scaling/identity_insertion.html#insert_id_layers)[#](#mitiq.zne.scaling.identity_insertion.insert_id_layers "Link to this definition")
:   Returns a scaled version of the input circuit by inserting layers of
    identities.

    Parameters:
    :   * **input\_circuit** (`Circuit`) – Cirq Circuit to be scaled
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Noise scaling factor as a float

    Returns:
    :   Scaled quantum circuit via identity layer insertions

    Return type:
    :   scaled\_circuit

#### Noise Scaling: Layerwise Folding[#](#module-mitiq.zne.scaling.layer_scaling "Link to this heading")

Functions for layer-wise unitary folding on supported circuits.

mitiq.zne.scaling.layer\_scaling.get\_layer\_folding(*layer\_index*)[[source]](_modules/mitiq/zne/scaling/layer_scaling.html#get_layer_folding)[#](#mitiq.zne.scaling.layer_scaling.get_layer_folding "Link to this definition")
:   Return function to perform folding. The function return can be used as
    an argument to define the noise scaling within the execute\_with\_zne
    function.

    Parameters:
    :   **layer\_index** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The layer of the circuit to apply folding to.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   The function for folding the ith layer.

mitiq.zne.scaling.layer\_scaling.layer\_folding(*circuit*, *layers\_to\_fold*)[[source]](_modules/mitiq/zne/scaling/layer_scaling.html#layer_folding)[#](#mitiq.zne.scaling.layer_scaling.layer_folding "Link to this definition")
:   Applies a variable amount of folding to select layers of a circuit.

    Note that this method only works for the univariate extrapolation methods.
    It allows a user to choose which layers in the input circuit will be
    scaled.

    See also

    If you would prefer to
    use a multivariate extrapolation method for unitary
    folding, use
    [`mitiq.lre.multivariate_scaling.layerwise_folding()`](#module-mitiq.lre.multivariate_scaling.layerwise_folding "mitiq.lre.multivariate_scaling.layerwise_folding") instead.

    The layerwise folding required for multivariate extrapolation is
    different as the layers in the input circuit have to be scaled in
    a specific pattern. The required specific pattern for multivariate
    extrapolation does not allow a user to provide a choice of which
    layers to fold.

    Parameters:
    :   * **circuit** (`Circuit`) – The input circuit.
        * **layers\_to\_fold** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]) – A list with the index referring to the layer number,
          and the element filled by an integer representing the
          number of times the layer is folded.

    Return type:
    :   `Circuit`

    Returns:
    :   The folded circuit.

#### Noise Scaling: Parameter Calibration[#](#module-mitiq.zne.scaling.parameter "Link to this heading")

*exception* mitiq.zne.scaling.parameter.CircuitMismatchException[[source]](_modules/mitiq/zne/scaling/parameter.html#CircuitMismatchException)[#](#mitiq.zne.scaling.parameter.CircuitMismatchException "Link to this definition")

*exception* mitiq.zne.scaling.parameter.GateTypeException[[source]](_modules/mitiq/zne/scaling/parameter.html#GateTypeException)[#](#mitiq.zne.scaling.parameter.GateTypeException "Link to this definition")

mitiq.zne.scaling.parameter.compute\_parameter\_variance(*executor*, *gate*, *qubit*, *depth=100*)[[source]](_modules/mitiq/zne/scaling/parameter.html#compute_parameter_variance)[#](#mitiq.zne.scaling.parameter.compute_parameter_variance "Link to this definition")
:   Given an executor and a gate, determines the effective variance in the
    control parameter that can be used as the `base_variance` argument in
    `mitiq.zne.scaling.scale_parameters`.

    Note: Only works for one qubit gates for now.

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – A function that takes in a quantum circuit and returns
          an expectation value.
        * **gate** (`EigenGate`) – The quantum gate that you wish to profile.
        * **qubit** (`Qid`) – The index of the qubit you wish to profile.
        * **depth** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of operations you would like to use to profile
          your gate.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The estimated variance of the control parameter.

mitiq.zne.scaling.parameter.scale\_parameters(*circuit*, *scale\_factor*, *base\_variance*, *seed=None*)[[source]](_modules/mitiq/zne/scaling/parameter.html#scale_parameters)[#](#mitiq.zne.scaling.parameter.scale_parameters "Link to this definition")
:   Applies parameter-noise scaling to the input circuit,
    assuming that each gate has the same base level of noise.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The circuit to scale as a QPROGRAM. All measurements
          should be in the last moment of the circuit.
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The amount to scale the base noise level by.
        * **base\_variance** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The base level (variance) of parameter noise,
          assumed to be the same for each gate of the circuit.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional seed for random number generator.

    Return type:
    :   `Circuit`

    Returns:
    :   The parameter noise scaled circuit.

## Experimental Techniques[#](#experimental-techniques "Link to this heading")

The following techniques have unstable APIs and are not covered by mitiq’s semantic versioning
guarantees. Access them via `mitiq.experimental`.

### Classical Shadows[#](#classical-shadows "Link to this heading")

#### Classical Shadows (High-Level Tools)[#](#module-mitiq.experimental.shadows.shadows "Link to this heading")

Classical shadow estimation for quantum circuits.

mitiq.experimental.shadows.shadows.classical\_post\_processing(*shadow\_outcomes*, *calibration\_results=None*, *observables=None*, *k\_shadows=None*, *state\_reconstruction=False*)[[source]](_modules/mitiq/experimental/shadows/shadows.html#classical_post_processing)[#](#mitiq.experimental.shadows.shadows.classical_post_processing "Link to this definition")
:   Executes a circuit with classical shadows. This function can be used for
    state reconstruction or expectation value estimation of observables.

    Parameters:
    :   * **shadow\_outcomes** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]) – The output of function
          [`shadow_quantum_processing()`](#mitiq.experimental.shadows.shadows.shadow_quantum_processing "mitiq.experimental.shadows.shadows.shadow_quantum_processing").
        * **calibration\_results** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The output of function
          [`pauli_twirling_calibrate()`](#mitiq.experimental.shadows.shadows.pauli_twirling_calibrate "mitiq.experimental.shadows.shadows.pauli_twirling_calibrate").
        * **observables** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The set of observables to measure.
        * **k\_shadows** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Number of groups of “median of means” used for shadow
          estimation of expectation values.
        * **state\_reconstruction** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – Whether to reconstruct the state or estimate
          the expectation value of the observables.

    Returns:
    :   * If `state_reconstruction` is `True`: `{"reconstructed_state":
          ndarray}` where the array is the reconstructed density matrix.
        * If `observables` is provided: a mapping from each observable’s
          string representation to its estimated expectation value.

    Return type:
    :   A dictionary with one of two forms depending on the arguments

mitiq.experimental.shadows.shadows.pauli\_twirling\_calibrate(*k\_calibration=1*, *locality=None*, *zero\_state\_shadow\_outcomes=None*, *qubits=None*, *executor=None*, *num\_total\_measurements\_calibration=20000*)[[source]](_modules/mitiq/experimental/shadows/shadows.html#pauli_twirling_calibrate)[#](#mitiq.experimental.shadows.shadows.pauli_twirling_calibrate "Link to this definition")
:   This function returns the dictionary of the median of means estimation
    of Pauli fidelities: \(\{\)“b”: \(f\_{b}\}\_{b\in\{0,1\}^n}\).
    The number of \(f\_b\) is \(2^n\), or \(\sum\_{i=1}^d C\_n^i\) if
    the locality \(d\) is given.

    In the notation of [[61](bibliography.html#id83 "Senrui Chen, Wenjun Yu, Pei Zeng, and Steven T Flammia. Robust shadow estimation. PRX Quantum, 2(3):030348, (2021).")], this function estimates
    the coefficient \(f\_b\), which are expansion coefficients of the
    twirled channel \(\mathcal{M}=\sum\_b f\_b\Pi\_b\).

    In practice, the output of this function can be used as calibration data
    for performing the classical shadows protocol in a way which is more
    robust to noise.

    Parameters:
    :   * **k\_calibration** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of groups of “median of means” used to solve for
          Pauli fidelity.
        * **locality** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The locality of the operator, whose expectation value is
          going to be estimated by the classical shadow. e.g. if operator is
          Ising model Hamiltonian with nearest neighbor interaction, then
          locality = 2.
        * **zero\_state\_shadow\_outcomes** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The output of function
          [`shadow_quantum_processing()`](#mitiq.experimental.shadows.shadows.shadow_quantum_processing "mitiq.experimental.shadows.shadows.shadow_quantum_processing") of zero calibrate state.
        * **qubits** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Qid`] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The qubits to measure, needs to specify when the
          `zero_state_shadow_outcomes` is None.
        * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`Circuit`], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The function to use to do quantum measurement, must be same
          as executor in [`shadow_quantum_processing()`](#mitiq.experimental.shadows.shadows.shadow_quantum_processing "mitiq.experimental.shadows.shadows.shadow_quantum_processing"). Needs to specify
          when the `zero_state_shadow_outcomes` is None.
        * **num\_total\_measurements\_calibration** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Number of shots per group of
          “median of means” used for calibration. Needs to specify when
          the `zero_state_shadow_outcomes` is None.

    Return type:
    :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")]

    Returns:
    :   A dictionary containing the calibration outcomes.

mitiq.experimental.shadows.shadows.shadow\_quantum\_processing(*circuit*, *executor*, *num\_total\_measurements\_shadow*, *random\_seed=None*, *qubits=None*)[[source]](_modules/mitiq/experimental/shadows/shadows.html#shadow_quantum_processing)[#](#mitiq.experimental.shadows.shadows.shadow_quantum_processing "Link to this definition")
:   This function returns the bitstrings and Pauli strings corresponding to
    the executor measurement outcomes for a given circuit, rotated by unitaries
    randomly sampled from a fixed unitary ensemble \(\mathcal{U}\).

    In the current implementation, the unitaries are sampled from the local
    Clifford group for \(n\) qubits, i.e.,
    \(\mathcal{U} = \mathcal{C}\_1^{\otimes n}\).

    In practice, the output of this function provides the raw experimental
    data necessary to perform the classical shadows protocol.

    Parameters:
    :   * **circuit** (`Circuit`) – The circuit to execute.
        * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`Circuit`], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – The function to use to do quantum measurement,
          must be same as executor in [`pauli_twirling_calibrate()`](#mitiq.experimental.shadows.shadows.pauli_twirling_calibrate "mitiq.experimental.shadows.shadows.pauli_twirling_calibrate").
        * **num\_total\_measurements\_shadow** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Total number of shots for shadow
          estimation.
        * **random\_seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The random seed to use for the shadow measurements.
        * **qubits** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Qid`] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The qubits to measure.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]

    Returns:
    :   A tuple of two lists of strings, each of length
        `num_total_measurements_shadow`. The first list contains bitstrings
        of computational basis measurement outcomes (e.g. `"01"`); the
        second contains the corresponding Pauli bases (e.g. `"XY"`).

#### Quantum Processing[#](#module-mitiq.experimental.shadows.quantum_processing "Link to this heading")

Quantum processing functions for classical shadows.

mitiq.experimental.shadows.quantum\_processing.get\_rotated\_circuits(*circuit*, *pauli\_strings*, *qubits=None*)[[source]](_modules/mitiq/experimental/shadows/quantum_processing.html#get_rotated_circuits)[#](#mitiq.experimental.shadows.quantum_processing.get_rotated_circuits "Link to this definition")
:   Returns a list of circuits measured in bases corresponding to
    `pauli_strings`.

    Parameters:
    :   * **circuit** (`Circuit`) – The circuit of interest.
        * **pauli\_strings** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]) – The Pauli strings to measure.
        * **qubits** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[`Qid`] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The qubits to measure. If None, all qubits in the circuit.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Circuit`]

    Returns: The list of circuits with rotation and measurement gates appended.

mitiq.experimental.shadows.quantum\_processing.random\_pauli\_measurement(*circuit*, *num\_measurements*, *executor*, *qubits=None*)[[source]](_modules/mitiq/experimental/shadows/quantum_processing.html#random_pauli_measurement)[#](#mitiq.experimental.shadows.quantum_processing.random_pauli_measurement "Link to this definition")
:   This function performs random Pauli measurements on a given circuit and
    returns the outcomes. These outcomes are represented as a tuple of two
    lists of strings.

    Parameters:
    :   * **circuit** (`Circuit`) – A Cirq circuit.
        * **num\_measurements** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of snapshots.
        * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`Circuit`], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – A callable that runs a circuit and returns a single
          bitstring.
        * **qubits** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[`Qid`] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The qubits in the circuit to be measured. If None,
          all qubits in the circuit will be measured.

    Warning

    The `executor` must return a `MeasurementResult` for a single shot,
    i.e., a single bitstring.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]

    Returns:
    :   Tuple containing two lists of strings, each of length equal to
        `num_measurements`. Strings in the first list are sequences of
        0’s and 1’s, which represent qubit measurements outcomes in the
        computational basis (e.g. “01001”). Strings in the second list are
        sequences of Pauli-measurement performed on each qubit (e.g. “XZZYY”).

mitiq.experimental.shadows.quantum\_processing.sample\_random\_pauli\_bases(*num\_qubits*, *num\_strings*)[[source]](_modules/mitiq/experimental/shadows/quantum_processing.html#sample_random_pauli_bases)[#](#mitiq.experimental.shadows.quantum_processing.sample_random_pauli_bases "Link to this definition")
:   Generate a list of random Pauli strings.

    Parameters:
    :   * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the Pauli strings.
        * **num\_strings** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of Pauli strings to generate.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]

    Returns:
    :   A list of random Pauli strings.

#### Classical Post-Processing[#](#module-mitiq.experimental.shadows.classical_postprocessing "Link to this heading")

Classical post-processing process of classical shadows.

mitiq.experimental.shadows.classical\_postprocessing.classical\_snapshot(*bitstring*, *paulistring*, *fidelities=None*)[[source]](_modules/mitiq/experimental/shadows/classical_postprocessing.html#classical_snapshot)[#](#mitiq.experimental.shadows.classical_postprocessing.classical_snapshot "Link to this definition")
:   Implement a single snapshot state reconstruction
    with calibration of the noisy quantum channel.

    Parameters:
    :   * **bitstring** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – The bitstring corresponding to the measurement outcome.
        * **paulistring** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – String of the applied Pauli measurement on each qubit.
        * **fidelities** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The estimated Pauli fidelities to use for calibration if
          available.

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   Reconstructed classical snapshot in terms of nparray.

mitiq.experimental.shadows.classical\_postprocessing.expectation\_estimation\_shadow(*measurement\_outcomes*, *pauli*, *num\_batches*, *fidelities=None*)[[source]](_modules/mitiq/experimental/shadows/classical_postprocessing.html#expectation_estimation_shadow)[#](#mitiq.experimental.shadows.classical_postprocessing.expectation_estimation_shadow "Link to this definition")
:   Calculate the expectation value of an observable from classical shadows.
    Use median of means to ameliorate the effects of outliers.

    Parameters:
    :   * **measurement\_outcomes** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]) – A shadow tuple obtained from
          random\_pauli\_measurement.
        * **pauli** ([`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")) – Single mitiq observable consisting of Pauli operators.
        * **num\_batches** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of batches to process measurement outcomes in.
        * **fidelities** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The estimated Pauli fidelities to use for calibration if
          available.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   Float corresponding to the estimate of the observable expectation
        value.

mitiq.experimental.shadows.classical\_postprocessing.get\_pauli\_fidelities(*calibration\_outcomes*, *num\_batches*, *locality=None*)[[source]](_modules/mitiq/experimental/shadows/classical_postprocessing.html#get_pauli_fidelities)[#](#mitiq.experimental.shadows.classical_postprocessing.get_pauli_fidelities "Link to this definition")
:   Calculate Pauli fidelities for the calibration circuit. In the notation of
    arXiv:2011.09636, this function estimates the coefficients
    \(f\_b\), which characterize the (noisy) classical shadow channel
    \(\mathcal{M}=\sum\_b f\_b \Pi\_b\).

    Parameters:
    :   * **calibration\_outcomes** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]) – The random\_pauli\_measurement outcomes for
          the state \(|0^n\rangle\).
        * **num\_batches** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of batches in the median of means estimator.
        * **locality** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The locality of the operator, whose expectation value is
          going to be estimated by the classical shadow. E.g., if the
          operator is the Ising model Hamiltonian with nearest neighbor
          interactions, then locality = 2.

    Return type:
    :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")]

    Returns:
    :   A \(2^n\)-dimensional dictionary of Pauli fidelities
        \(f\_b\) for \(b = \{0,1\}^{n}\)

mitiq.experimental.shadows.classical\_postprocessing.get\_single\_shot\_pauli\_fidelity(*bitstring*, *paulistring*, *locality=None*)[[source]](_modules/mitiq/experimental/shadows/classical_postprocessing.html#get_single_shot_pauli_fidelity)[#](#mitiq.experimental.shadows.classical_postprocessing.get_single_shot_pauli_fidelity "Link to this definition")
:   Calculate Pauli fidelity \(f\_b\) for a single shot measurement of the
    calibration circuit for b= bit\_string.

    In the notation of arXiv:2011.09636, this function estimates the
    coefficient \(f\_b\), which characterizes the (noisy) classical
    shadow channel.

    The locality is realized on the assumption that the noisy
    channel \(\Lambda\) is local
    \(\Lambda \equiv \bigotimes\_i^n\Lambda\_i\).

    Parameters:
    :   * **bitstring** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – The bitstring corresponding to a computational basis state.
          E.g., ‘01…0’\(:=|0\rangle|1\rangle...|0\rangle\).
        * **paulistring** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – The local Pauli measurement performed on each qubit.
          e.g.’XY…Z’ means perform local X-basis measurement on the
          1st qubit, local Y-basis measurement the 2nd qubit, local Z-basis
          measurement the last qubit in the circuit.
        * **locality** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The locality of the operator, whose expectation value is
          going to be estimated by the classical shadow. E.g., if the
          operator is the Ising model Hamiltonian with nearest neighbor
          interactions, then locality = 2.

    Returns:
    :   \(\{{f}\_b\}\).
        If the locality is \(w < n\), then derive the output’s keys from
        the bit\_string. Ensure that the number of 1s in the keys is less
        than or equal to w. The corresponding Pauli fidelity is the product of
        local Pauli fidelity where the associated locus in the keys are ‘1’.

    Return type:
    :   A dictionary of Pauli fidelity bit\_string

mitiq.experimental.shadows.classical\_postprocessing.shadow\_state\_reconstruction(*shadow\_measurement\_outcomes*, *fidelities=None*)[[source]](_modules/mitiq/experimental/shadows/classical_postprocessing.html#shadow_state_reconstruction)[#](#mitiq.experimental.shadows.classical_postprocessing.shadow_state_reconstruction "Link to this definition")
:   Reconstruct a state approximation as an average over all snapshots.

    Parameters:
    :   * **shadow\_measurement\_outcomes** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]) – Measurement result and the basis
          performing the measurement obtained from random\_pauli\_measurement
          for classical shadow protocol.
        * **fidelities** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The estimated Pauli fidelities to use for calibration if
          available.

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[[`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   The state reconstructed from classical shadow protocol

#### Utility Functions[#](#module-mitiq.experimental.shadows.shadows_utils "Link to this heading")

Defines utility functions for classical shadows protocol.

mitiq.experimental.shadows.shadows\_utils.batch\_calibration\_data(*data*, *num\_batches*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#batch_calibration_data)[#](#mitiq.experimental.shadows.shadows_utils.batch_calibration_data "Link to this definition")
:   Split calibration data into `num_batches` equal-sized chunks.

    Parameters:
    :   * **data** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]]) – The random Pauli measurement outcomes.
        * **num\_batches** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of batches to split the data into.

    Yields:
    :   Tuples of bit strings and pauli strings.

    Return type:
    :   [`Generator`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Generator "(in Python v3.11)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]], [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")]

mitiq.experimental.shadows.shadows\_utils.create\_string(*str\_len*, *loc\_list*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#create_string)[#](#mitiq.experimental.shadows.shadows_utils.create_string "Link to this definition")
:   This function returns a string of length `str_len` with 1s at the
    locations specified by `loc_list` and 0s elsewhere.

    Parameters:
    :   * **str\_len** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The length of the string.
        * **loc\_list** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]) – A list of integers indices specifying the locations of 1s in
          the string.

    Return type:
    :   [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")

    Returns:
    :   A bitstring constructed as above.

    Example

    A basic example:

    ```
    create_string(5, [1, 3])
    >>> "01010"
    ```

mitiq.experimental.shadows.shadows\_utils.fidelity(*sigma*, *rho*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#fidelity)[#](#mitiq.experimental.shadows.shadows_utils.fidelity "Link to this definition")
:   Calculate the fidelity between two states.

    Parameters:
    :   * **sigma** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – A state in terms of square matrix or vector.
        * **rho** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – A state in terms square matrix or vector.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   Scalar corresponding to the fidelity.

mitiq.experimental.shadows.shadows\_utils.local\_clifford\_shadow\_norm(*obs*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#local_clifford_shadow_norm)[#](#mitiq.experimental.shadows.shadows_utils.local_clifford_shadow_norm "Link to this definition")
:   Calculate shadow norm of an operator with random unitary sampled from local
    Clifford group.

    Parameters:
    :   **obs** ([`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")) – A self-adjoint operator, i.e. mitiq.PauliString with real
        coefficient.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   Shadow norm when unitary ensemble is local Clifford group.

mitiq.experimental.shadows.shadows\_utils.n\_measurements\_opts\_expectation\_bound(*error*, *observables*, *failure\_rate*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#n_measurements_opts_expectation_bound)[#](#mitiq.experimental.shadows.shadows_utils.n_measurements_opts_expectation_bound "Link to this definition")
:   This function returns the minimum number of classical shadows required and
    the number of groups “k” into which we need to split the shadows for
    achieving the desired accuracy and failure rate in operator expectation
    value estimation.

    Parameters:
    :   * **error** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The error on the estimator.
        * **observables** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")]) – List of mitiq.PauliString corresponding to the
          observables we intend to measure.
        * **failure\_rate** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Rate of failure for the bound to hold.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]

    Returns:
    :   Integers quantifying the number of snapshots required to satisfy
        the shadow bound and the chunk size required to attain the specified
        failure rate.

mitiq.experimental.shadows.shadows\_utils.n\_measurements\_tomography\_bound(*epsilon*, *num\_qubits*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#n_measurements_tomography_bound)[#](#mitiq.experimental.shadows.shadows_utils.n_measurements_tomography_bound "Link to this definition")
:   This function returns the minimum number of classical shadows required
    for state reconstruction for achieving the desired accuracy.

    Parameters:
    :   * **epsilon** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The error on the estimator.
        * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the system.

    Return type:
    :   [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")

    Returns:
    :   An integer that gives the number of snapshots required to satisfy the
        shadow bound.

mitiq.experimental.shadows.shadows\_utils.valid\_bitstrings(*num\_qubits*, *max\_hamming\_weight=None*)[[source]](_modules/mitiq/experimental/shadows/shadows_utils.html#valid_bitstrings)[#](#mitiq.experimental.shadows.shadows_utils.valid_bitstrings "Link to this definition")
:   Return all bitstrings on `num_qubits` bits up to a Hamming weight.

    Parameters:
    :   * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of bits in each bitstring.
        * **max\_hamming\_weight** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – If provided, only bitstrings whose Hamming weight
          (number of 1s) is at most this value are returned. Must be >= 1.

    Return type:
    :   [`set`](https://docs.python.org/3.11/library/stdtypes.html#set "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")]

    Returns:
    :   The set of all valid bitstrings on `num_qubits` bits, optionally
        filtered to a maximum Hamming weight.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If `max_hamming_weight` is provided and less than 1.

### Probabilistic Error Amplification[#](#probabilistic-error-amplification "Link to this heading")

#### Probabilistic Error Amplification (High-Level Tools)[#](#module-mitiq.experimental.pea.pea "Link to this heading")

High-level probabilistic error amplification tools.

mitiq.experimental.pea.pea.combine\_results(*scale\_factors*, *scaled\_results*, *scaled\_norms*, *scaled\_signs*, *extrapolation\_method*)[[source]](_modules/mitiq/experimental/pea/pea.html#combine_results)[#](#mitiq.experimental.pea.pea.combine_results "Link to this definition")
:   Combine expectation values coming from probabilistically sampled
    circuits at each of the input noise scale\_factors and extrapolate
    the resulting expectation values to the zero noise limit to obtain the
    error-mitigated expectation value.

    Warning

    The `scaled_results` must be in the same order as the circuits were
    generated.

    Parameters:
    :   * **scale\_factors** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – A list of (positive) numbers by which the baseline
          noise level is to be amplified.
        * **scaled\_results** ([`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]) – Results as obtained from running circuits at each scale
          factor.
        * **scaled\_norms** ([`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The one-norm of the circuit representations at each scale
          factor.
        * **scaled\_signs** ([`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`Iterable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Iterable "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]]) – The signs corresponding to the positivity of the sampled
          circuits at each scale factor.
        * **extrapolation\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The method of extrapolation to use when fitting
          the measured results. A list of built-in functions can be found
          in `mitiq.zne.inference`.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The PEA estimate of the expectation value.

mitiq.experimental.pea.pea.construct\_circuits(*circuit*, *scale\_factors*, *noise\_model*, *epsilon*, *random\_state=None*, *precision=0.1*, *num\_samples=None*)[[source]](_modules/mitiq/experimental/pea/pea.html#construct_circuits)[#](#mitiq.experimental.pea.pea.construct_circuits "Link to this definition")
:   Samples lists of implementable circuits from the noise-amplified
    representation of the input ideal circuit at each input noise scale
    factor.

    Note that the ideal operation can be a sequence of operations (circuit),
    for instance U = V W, as long as a representation is known. Similarly, A
    and B can be sequences of operations (circuits) or just single operations.

    Parameters:
    :   * **circuit** (`Circuit`) – The ideal circuit from which an implementable
          sequence is sampled.
        * **scale\_factors** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – A list of (positive) numbers by which the baseline
          noise level is to be amplified.
        * **noise\_model** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – A string describing the noise model to be used for the
          noise-scaled representations, e.g. “local\_depolarizing” or
          “global\_depolarizing”.
        * **epsilon** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Baseline noise level.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The random state or seed for reproducibility.
        * **precision** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The desired precision for the sampling process.
          Default is 0.1.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of noisy circuits to be sampled for PEA.
          If not given, this is deduced from the ‘precision’.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]]

    Returns:
    :   The scaled circuits, their signs and norms at each scale factor.

    Raises:
    :   [**ValueError**](https://docs.python.org/3.11/library/exceptions.html#ValueError "(in Python v3.11)") – If the precision is not within the interval (0, 1].

mitiq.experimental.pea.pea.execute\_with\_pea(*circuit*, *executor*, *scale\_factors*, *noise\_model*, *epsilon*, *extrapolation\_method*, *observable=None*, *random\_state=None*, *precision=0.1*, *num\_samples=None*, *full\_output=False*, *force\_run\_all=False*)[[source]](_modules/mitiq/experimental/pea/pea.html#execute_with_pea)[#](#mitiq.experimental.pea.pea.execute_with_pea "Link to this definition")
:   Estimates the error-mitigated expectation value associated to the
    input circuit, via the application of probabilistic error amplification
    (PEA). [[59](bibliography.html#id37 "Youngseok Kim, Andrew Eddins, Sajant Anand, Ken Xuan Wei, Ewout van den Berg, Sami Rosenblatt, Hasan Nayfeh, Yantao Wu, Michael Zaletel, Kristan Temme, and Abhinav Kandala. Evidence for the utility of quantum computing before fault tolerance. Nature, 618(7965):500–505, (2023). URL: https://doi.org/10.1038/s41586-023-06096-3, doi:10.1038/s41586-023-06096-3.")].

    This function implements PEA by:

    1. Sampling different implementable circuits from the quasi-probability
       representation of the input circuit at each of the input noise
       scale\_factors;
    2. Evaluating the noisy expectation values associated to the sampled
       circuits (through the “executor” function provided by the user);
    3. Estimating the ideal expectation value from a suitable linear
       combination of the noisy ones at each noise scale factor;
    4. Extrapolating the expectation values obtained at each noise
       scale factor to the zero noise limit.

    Parameters:
    :   * **circuit** (`Circuit`) – The input circuit to execute with error-mitigation.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `QuantumResult` (e.g. an expectation value).
        * **scale\_factors** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – A list of (positive) numbers by which the baseline
          noise level is to be amplified.
        * **noise\_model** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – A string describing the noise model to be used for the
          noise-scaled representations, e.g. “local\_depolarizing” or
          “global\_depolarizing”.
        * **epsilon** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Baseline noise level.
        * **extrapolation\_method** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")], [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The method of extrapolation to use when fitting
          the measured results. A list of built-in functions can be found
          in `mitiq.zne.inference`.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If None,
          the executor must return an expectation value. Otherwise,
          the QuantumResult returned by executor is used to compute the
          expectation of the observable.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The random state or seed for reproducibility.
        * **precision** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The desired precision for the sampling process.
          Default is 0.1.
        * **num\_samples** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The number of noisy circuits to be sampled for PEA.
          If not given, this is deduced from the argument ‘precision’.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If False only the average PEA value is returned.
          If True a dictionary containing all PEA data is returned too.
        * **force\_run\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, all sampled circuits are executed regardless of
          uniqueness, else a minimal unique set is executed.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   The tuple `(pea_value, pea_data)` where `pea_value` is the
        expectation value estimated with PEA and `pea_data` is a dictionary
        which contains all the raw data involved in the PEA process. If
        `full_output` is `False`, only `pea_value` is
        returned.

#### Noise Amplification Utilities[#](#module-mitiq.experimental.pea.scale_amplifications "Link to this heading")

Tools for constructing the noise-amplified representations of ideal
operations.

mitiq.experimental.pea.scale\_amplifications.scale\_circuit\_amplifications(*ideal\_circuit*, *scale\_factor*, *noise\_model*, *epsilon*)[[source]](_modules/mitiq/experimental/pea/scale_amplifications.html#scale_circuit_amplifications)[#](#mitiq.experimental.pea.scale_amplifications.scale_circuit_amplifications "Link to this definition")
:   Generates a list of implementable sequences from the noise-amplified
    representation of the input ideal circuit based on the input noise model
    and baseline noise level.

    Parameters:
    :   * **ideal\_circuit** (`Circuit`) – The ideal circuit from which an implementable
          sequence is sampled.
        * **scale\_factor** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – A (positive) number by which the baseline noise
          level is to be amplified.
        * **noise\_model** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – A string describing the noise model to be used for the
          noise-scaled representations, e.g. “local\_depolarizing” or
          “global\_depolarizing”.
        * **epsilon** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Baseline noise level.

    Return type:
    :   [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]

    Returns:
    :   A list of noise-amplified circuits, corresponding to each scale
        factor multiplied by the baseline noise level.

#### Depolarizing Amplifications[#](#module-mitiq.experimental.pea.amplifications.amplify_depolarizing "Link to this heading")

Functions related to amplifications with depolarizing noise.

mitiq.experimental.pea.amplifications.amplify\_depolarizing.amplify\_noisy\_op\_with\_global\_depolarizing\_noise(*ideal\_operation*, *noise\_level*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/experimental/pea/amplifications/amplify_depolarizing.html#amplify_noisy_op_with_global_depolarizing_noise)[#](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_op_with_global_depolarizing_noise "Link to this definition")
:   As described in [[59](bibliography.html#id37 "Youngseok Kim, Andrew Eddins, Sajant Anand, Ken Xuan Wei, Ewout van den Berg, Sami Rosenblatt, Hasan Nayfeh, Yantao Wu, Michael Zaletel, Kristan Temme, and Abhinav Kandala. Evidence for the utility of quantum computing before fault tolerance. Nature, 618(7965):500–505, (2023). URL: https://doi.org/10.1038/s41586-023-06096-3, doi:10.1038/s41586-023-06096-3.")], this function maps an
    `ideal_operation` \(\mathcal{U}\) into its noise-amplified
    representation, which is a linear combination of noisy implementable
    operations \(\sum\_\alpha \eta\_{\alpha} \mathcal{O}\_{\alpha}\).

    This function assumes a depolarizing noise model and, more precisely,
    that the following noisy operations are implementable
    \(\mathcal{O}\_{\alpha} = \mathcal{D} \circ \mathcal P\_\alpha
    \circ \mathcal{U}\), where \(\mathcal{U}\) is the unitary associated
    to the input `ideal_operation` acting on \(k\) qubits,
    \(\mathcal{P}\_\alpha\) is a Pauli operation and
    \(\mathcal{D}(\rho) = (1 - \epsilon) \rho + \epsilon I/2^k\) is a
    depolarizing channel (\(\epsilon\) is a simple function of
    `noise_level`).

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation (as a QPROGRAM) to represent.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The noise level (as a float) of the depolarizing channel.
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation corresponds to the
          operation on the specific qubits defined in ideal\_operation.
          If False, the representation is valid for the same gate even if
          acting on different qubits from those specified in
          ideal\_operation.

    Return type:
    :   [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")

    Returns:
    :   The noise-amplified representation of the `ideal_operation`.

mitiq.experimental.pea.amplifications.amplify\_depolarizing.amplify\_noisy\_op\_with\_local\_depolarizing\_noise(*ideal\_operation*, *noise\_level*, *is\_qubit\_dependent=True*)[[source]](_modules/mitiq/experimental/pea/amplifications/amplify_depolarizing.html#amplify_noisy_op_with_local_depolarizing_noise)[#](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_op_with_local_depolarizing_noise "Link to this definition")
:   As described in [[59](bibliography.html#id37 "Youngseok Kim, Andrew Eddins, Sajant Anand, Ken Xuan Wei, Ewout van den Berg, Sami Rosenblatt, Hasan Nayfeh, Yantao Wu, Michael Zaletel, Kristan Temme, and Abhinav Kandala. Evidence for the utility of quantum computing before fault tolerance. Nature, 618(7965):500–505, (2023). URL: https://doi.org/10.1038/s41586-023-06096-3, doi:10.1038/s41586-023-06096-3.")], this function maps an
    `ideal_operation` \(\mathcal{U}\) into its noise-amplified
    representation, which is a linear combination of noisy implementable
    operations \(\sum\_\alpha \eta\_{\alpha} \mathcal{O}\_{\alpha}\).

    This function assumes a (local) single-qubit depolarizing noise model even
    for multi-qubit operations. More precisely, it assumes that the following
    noisy operations are implementable \(\mathcal{O}\_{\alpha} =
    \mathcal{D}^{\otimes k} \circ \mathcal P\_\alpha \circ \mathcal{U}\),
    where \(\mathcal{U}\) is the unitary associated
    to the input `ideal_operation` acting on \(k\) qubits,
    \(\mathcal{P}\_\alpha\) is a Pauli operation and
    \(\mathcal{D}(\rho) = (1 - \epsilon) \rho + \epsilon I/2\) is a
    single-qubit depolarizing channel (\(\epsilon\) is a simple function
    of `noise_level`).

    More information about the noise-amplified representation for a
    depolarizing noise channel can be found in:
    `amplify_operation_with_global_depolarizing_noise()`.

    Parameters:
    :   * **ideal\_operation** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal operation (as a QPROGRAM) to represent.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The noise level of each depolarizing channel.
        * **is\_qubit\_dependent** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, the representation corresponds to the
          operation on the specific qubits defined in ideal\_operation.
          If False, the representation is valid for the same gate even
          if acting on different qubits from those specified in
          ideal\_operation.

    Return type:
    :   [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")

    Returns:
    :   The noise-amplified representation of the `ideal_operation`.

    Note

    The input `ideal_operation` is typically a QPROGRAM with a single
    gate but could also correspond to a sequence of more gates.
    This is possible as long as the unitary associated to the input
    QPROGRAM, followed by a single final depolarizing channel, is
    physically implementable.

mitiq.experimental.pea.amplifications.amplify\_depolarizing.amplify\_noisy\_ops\_in\_circuit\_with\_global\_depolarizing\_noise(*ideal\_circuit*, *noise\_level*)[[source]](_modules/mitiq/experimental/pea/amplifications/amplify_depolarizing.html#amplify_noisy_ops_in_circuit_with_global_depolarizing_noise)[#](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_ops_in_circuit_with_global_depolarizing_noise "Link to this definition")
:   Iterates over all unique operations of the input `ideal_circuit` and,
    for each of them, generates the corresponding noise-amplified
    representation (linear combination of implementable noisy operations).

    This function assumes that the same depolarizing noise channel of strength
    `noise_level` affects each implemented operation.

    Parameters:
    :   * **ideal\_circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal circuit, whose ideal operations should be
          represented.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (gate-independent) depolarizing noise level.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]

    Returns:
    :   The list of quasi-probability amplifications associated to
        the operations of the input `ideal_circuit`.

    Note

    Measurement gates are ignored.

    Note

    The returned amplifications are always defined in terms of
    Cirq circuits, even if the input is not a `cirq.Circuit`.

mitiq.experimental.pea.amplifications.amplify\_depolarizing.amplify\_noisy\_ops\_in\_circuit\_with\_local\_depolarizing\_noise(*ideal\_circuit*, *noise\_level*)[[source]](_modules/mitiq/experimental/pea/amplifications/amplify_depolarizing.html#amplify_noisy_ops_in_circuit_with_local_depolarizing_noise)[#](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_ops_in_circuit_with_local_depolarizing_noise "Link to this definition")
:   Iterates over all unique operations of the input `ideal_circuit` and,
    for each of them, generates the corresponding quasi-probability
    amplification (linear combination of implementable noisy operations).

    This function assumes that the tensor product of `k` single-qubit
    depolarizing channels affects each implemented operation, where
    `k` is the number of qubits associated to the operation.

    Parameters:
    :   * **ideal\_circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The ideal circuit, whose ideal operations should be
          represented.
        * **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The (gate-independent) depolarizing noise level.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation "mitiq.pec.types.types.OperationRepresentation")]

    Returns:
    :   The list of quasi-probability amplifications associated to
        the operations of the input `ideal_circuit`.

    Note

    Measurement gates are ignored.

    Warning

    The returned amplifications are always defined in terms of
    Cirq circuits, even if the input is not a `cirq.Circuit`.

### Twirled Readout Error eXtinction[#](#twirled-readout-error-extinction "Link to this heading")

#### TREX (High-Level Tools)[#](#module-mitiq.experimental.trex.trex "Link to this heading")

High-level Twirled Readout Error eXtinction (TREX) tools.

TREX is a model-free readout error mitigation technique that applies
random X gates before measurement and classically undoes the flips,
effectively twirling the readout error channel into a diagonal form.
Calibration circuits estimate the readout error eigenvalues, and the
true expectation value is recovered by dividing by these eigenvalues.

See [[35](bibliography.html#id72 "Ewout van den Berg, Zlatko K. Minev, and Kristan Temme. Model-free readout-error mitigation for quantum expectation values. Nature Physics, 18:1116–1121, (2022). arXiv:2012.09738, doi:10.1038/s41567-022-01742-5.")] for more details.

mitiq.experimental.trex.trex.combine\_results(*twirled\_results*, *calibration\_results*, *randomization\_strings*, *observable*)[[source]](_modules/mitiq/experimental/trex/trex.html#combine_results)[#](#mitiq.experimental.trex.trex.combine_results "Link to this definition")
:   Compute the TREX-corrected expectation value.

    For each Pauli string in the observable, the noisy expectation value
    from twirled measurements is divided by the calibration factor
    (readout error eigenvalue) estimated from calibration data, and then
    averaged across randomizations.

    Parameters:
    :   * **twirled\_results** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – Measurement results from twirled circuits.
          Ordered as [group0\_rand0, group0\_rand1, …, group1\_rand0, …].
        * **calibration\_results** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – Measurement results from calibration circuits
          (one per randomization).
        * **randomization\_strings** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`int64`]]] | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`int64`]]) – Random bitstrings used for twirling.
          Can be a list of 1D arrays or a 2D array of shape
          `(num_randomizations, n_qubits)`.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – The observable being estimated.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The TREX-corrected expectation value.

mitiq.experimental.trex.trex.construct\_circuits(*circuit*, *observable*, *num\_randomizations=32*, *random\_state=None*)[[source]](_modules/mitiq/experimental/trex/trex.html#construct_circuits)[#](#mitiq.experimental.trex.trex.construct_circuits "Link to this definition")
:   Generate twirled measurement circuits and calibration circuits for TREX.

    For each randomization pattern and each commuting group in the
    observable, a twirled measurement circuit is created by inserting
    random X gates before measurement. A corresponding set of calibration
    circuits (identity circuit with the same twirling) is also created.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The quantum circuit to mitigate readout errors for.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable defining the measurement basis.
        * **num\_randomizations** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of random twirling patterns.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed or `np.random.RandomState` for reproducibility.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`int64`]]]

    Returns:
    :   A tuple `(twirled_circuits, calibration_circuits,
        randomization_strings)` where:

        * `twirled_circuits`: List of circuits (in the same format as the
          input `circuit`) with readout twirling applied. Ordered as
          [group0\_rand0, group0\_rand1, …, group1\_rand0, …].
        * `calibration_circuits`: List of calibration circuits in the same
          format as the input (one per randomization, shared across groups).
        * `randomization_strings`: 2D array of shape
          `(num_randomizations, n_qubits)` with random bitstrings used
          for twirling.

mitiq.experimental.trex.trex.execute\_with\_trex(*circuit*, *executor*, *observable*, *\**, *num\_randomizations=32*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/experimental/trex/trex.html#execute_with_trex)[#](#mitiq.experimental.trex.trex.execute_with_trex "Link to this definition")
:   Estimates the error-mitigated expectation value of an observable
    using Twirled Readout Error eXtinction (TREX).

    TREX mitigates readout errors by randomly applying X gates before
    measurement (readout twirling) and using calibration data to correct
    the resulting expectation values. See [[35](bibliography.html#id72 "Ewout van den Berg, Zlatko K. Minev, and Kristan Temme. Model-free readout-error mitigation for quantum expectation values. Nature Physics, 18:1116–1121, (2022). arXiv:2012.09738, doi:10.1038/s41567-022-01742-5.")].

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit to execute with TREX.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – A Mitiq executor that executes a circuit and returns
          a `MeasurementResult` (raw bitstrings).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the expectation value of.
        * **num\_randomizations** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of random readout twirling
          patterns to average over. More randomizations give better
          accuracy at the cost of more circuit executions.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed or `np.random.RandomState` for reproducibility.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If `False` only the mitigated expectation value is
          returned. If `True` a dictionary containing all TREX data
          is returned too.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]

    Returns:
    :   The expectation value estimated with TREX. If `full_output` is
        `True`, returns a tuple `(trex_value, trex_data)` where
        `trex_data` is a dictionary of intermediate results.

mitiq.experimental.trex.trex.mitigate\_executor(*executor*, *observable*, *\**, *num\_randomizations=32*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/experimental/trex/trex.html#mitigate_executor)[#](#mitiq.experimental.trex.trex.mitigate_executor "Link to this definition")
:   Returns a modified version of the input `executor` which is
    error-mitigated with TREX.

    Parameters:
    :   * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – A Mitiq executor that executes a circuit and returns
          a `MeasurementResult`.
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the expectation value of.
        * **num\_randomizations** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of random twirling patterns.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed or `np.random.RandomState` for reproducibility.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If `False` only the mitigated expectation value is
          returned. If `True` a dictionary containing all TREX data
          is returned too.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]]

    Returns:
    :   The error-mitigated version of the input executor.

mitiq.experimental.trex.trex.trex\_decorator(*observable*, *\**, *num\_randomizations=32*, *random\_state=None*, *full\_output=False*)[[source]](_modules/mitiq/experimental/trex/trex.html#trex_decorator)[#](#mitiq.experimental.trex.trex.trex_decorator "Link to this definition")
:   Decorator which adds TREX error mitigation to an executor function.

    Parameters:
    :   * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – Observable to compute the expectation value of.
        * **num\_randomizations** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of random twirling patterns.
        * **random\_state** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed or `np.random.RandomState` for reproducibility.
        * **full\_output** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If `False` only the mitigated expectation value is
          returned. If `True` a dictionary containing all TREX data
          is returned too.

    Return type:
    :   [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]], [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]]]

    Returns:
    :   The error-mitigating decorator to be applied to an executor function.

### Virtual Distillation[#](#module-mitiq.experimental.vd.vd "Link to this heading")

mitiq.experimental.vd.vd.combine\_results(*measurements*)[[source]](_modules/mitiq/experimental/vd/vd.html#combine_results)[#](#mitiq.experimental.vd.vd.combine_results "Link to this definition")
:   Process measurement results according to the virtual distillation
    protocol.

    Parameters:
    :   **measurements** ([`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")) – Measurement results from circuit execution

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float64`]]

    Returns:
    :   Array of error-mitigated expectation values for
        \(\langle Z\_i\rangle\) observables.

mitiq.experimental.vd.vd.construct\_circuits(*circuit*)[[source]](_modules/mitiq/experimental/vd/vd.html#construct_circuits)[#](#mitiq.experimental.vd.vd.construct_circuits "Link to this definition")
:   Constructs a circuit which contains two copies of the input circuit,
    with an entangled gate applied between them.

    Parameters:
    :   **circuit** (`Circuit`) – The input circuit to copy.

    Return type:
    :   `Circuit`

mitiq.experimental.vd.vd.execute\_with\_vd(*circuit*, *executor*)[[source]](_modules/mitiq/experimental/vd/vd.html#execute_with_vd)[#](#mitiq.experimental.vd.vd.execute_with_vd "Link to this definition")
:   Given a circuit that acts on N qubits, this function returns the
    expectation values of a given observable for each qubit i.
    The expectation values are corrected using the virtual distillation
    algorithm.

    Parameters:
    :   * **circuit** (`Circuit`) – The input circuit of N qubits to execute with VD.
        * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`Circuit`], [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")]) – An executor that executes a circuit and returns either a
          density matrix, or a measurement result (bitstring).

    Note

    Use an odd number of shots when using this technique. This prevents an
    (unlikely) scenario where the normalization constant can be zero.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    Returns:
    :   A list of VD-estimated expectation values for
        \(\langle Z\_i\rangle\).

## Tools For Error Mitigation[#](#tools-for-error-mitigation "Link to this heading")

### Benchmarks[#](#benchmarks "Link to this heading")

#### GHZ Circuits[#](#module-mitiq.benchmarks.ghz_circuits "Link to this heading")

Functions for creating GHZ circuits for benchmarking purposes.

mitiq.benchmarks.ghz\_circuits.generate\_ghz\_circuit(*n\_qubits*, *return\_type=None*)[[source]](_modules/mitiq/benchmarks/ghz_circuits.html#generate_ghz_circuit)[#](#mitiq.benchmarks.ghz_circuits.generate_ghz_circuit "Link to this definition")
:   Returns a GHZ circuit ie a circuit that prepares an `n_qubits`
    GHZ state.

    Parameters:
    :   * **n\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the circuit.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the returned
          circuits. See the keys of `mitiq.SUPPORTED_PROGRAM_TYPES`
          for options. If `None`, the returned circuits have type
          `cirq.Circuit`.

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

    Returns:
    :   A GHZ circuit acting on `n_qubits` qubits.

#### Mirror Circuits[#](#module-mitiq.benchmarks.mirror_circuits "Link to this heading")

Functions for creating mirror circuits as defined in
[[1](bibliography.html#id57 "Timothy Proctor, Kenneth Rudinger, Kevin Young, Erik Nielsen, and Robin Blume-Kohout. Measuring the capabilities of quantum computers. Nature Physics, 18(1):75–79, (2021). URL: https://doi.org/10.1038%2Fs41567-021-01409-7, doi:10.1038/s41567-021-01409-7.")] for benchmarking quantum computers
(with error mitigation).

mitiq.benchmarks.mirror\_circuits.edge\_grab(*two\_qubit\_gate\_prob*, *connectivity\_graph*, *random\_state*)[[source]](_modules/mitiq/benchmarks/mirror_circuits.html#edge_grab)[#](#mitiq.benchmarks.mirror_circuits.edge_grab "Link to this definition")
:   Parameters:
    :   * **two\_qubit\_gate\_prob** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Probability of an edge being chosen
          from the set of candidate edges.
        * **connectivity\_graph** (`Graph`) – The connectivity graph for the backend
          on which the circuit will be run.
        * **random\_state** ([`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)")) – Random state to select edges (uniformly at random).

    Return type:
    :   `Graph`

    Returns:
    :   Returns a set of edges for which two qubit gates are to be
        applied given a two qubit gate density and the connectivity graph
        that must be satisfied.

mitiq.benchmarks.mirror\_circuits.generate\_mirror\_circuit(*nlayers*, *two\_qubit\_gate\_prob*, *connectivity\_graph*, *two\_qubit\_gate\_name='CNOT'*, *seed=None*, *return\_type=None*)[[source]](_modules/mitiq/benchmarks/mirror_circuits.html#generate_mirror_circuit)[#](#mitiq.benchmarks.mirror_circuits.generate_mirror_circuit "Link to this definition")
:   Parameters:
    :   * **nlayers** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of random Clifford layers to be generated.
        * **two\_qubit\_gate\_prob** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – Probability of a two-qubit gate being applied.
        * **connectivity\_graph** (`Graph`) – The connectivity graph of the backend
          on which the mirror circuit will be run. This is used
          to make sure 2-qubit gates are only applied to connected qubits.
        * **two\_qubit\_gate\_name** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – Name of two-qubit gate to use. Options are “CNOT”
          and “CZ”.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for generating randomized mirror circuit.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the
          returned circuit. See the keys of `mitiq.SUPPORTED_PROGRAM_TYPES`
          for options. If `None`, the returned circuit is a
          `cirq.Circuit`.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]]

    Returns:
    :   A randomized mirror circuit and the bitstring corresponding
        to a noise free result.

mitiq.benchmarks.mirror\_circuits.random\_cliffords(*connectivity\_graph*, *random\_state*, *two\_qubit\_gate=cirq.CNOT*)[[source]](_modules/mitiq/benchmarks/mirror_circuits.html#random_cliffords)[#](#mitiq.benchmarks.mirror_circuits.random_cliffords "Link to this definition")
:   Parameters:
    :   * **connectivity\_graph** (`Graph`) – A graph with the edges for which the
          two-qubit Clifford gate is to be applied.
        * **random\_state** ([`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)")) – Random state to choose Cliffords (uniformly at random).
        * **two\_qubit\_gate** (`Gate`) – Two-qubit gate to use.

    Return type:
    :   `Circuit`

    Returns:
    :   A circuit with a two-qubit Clifford gate applied to each edge in
        edges, and a random single-qubit Clifford gate applied to every
        other qubit.

mitiq.benchmarks.mirror\_circuits.random\_paulis(*connectivity\_graph*, *random\_state*)[[source]](_modules/mitiq/benchmarks/mirror_circuits.html#random_paulis)[#](#mitiq.benchmarks.mirror_circuits.random_paulis "Link to this definition")
:   Returns a circuit with randomly selected Pauli gates on each qubit.

    Parameters:
    :   * **connectivity\_graph** (`Graph`) – Connectivity graph of device to run circuit on.
        * **random\_state** ([`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)")) – Random state to select Paulis I, X, Y, Z uniformly at
          random.

    Return type:
    :   `Circuit`

mitiq.benchmarks.mirror\_circuits.random\_single\_cliffords(*connectivity\_graph*, *random\_state*)[[source]](_modules/mitiq/benchmarks/mirror_circuits.html#random_single_cliffords)[#](#mitiq.benchmarks.mirror_circuits.random_single_cliffords "Link to this definition")
:   Parameters:
    :   * **connectivity\_graph** (`Graph`) – A graph with each node representing a qubit for
          which a random single-qubit Clifford gate is to be applied.
        * **random\_state** ([`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.4)")) – Random state to choose Cliffords (uniformly at random).

    Return type:
    :   `Circuit`

    Returns:
    :   A circuit with a random single-qubit Clifford gate applied on each
        given qubit.

#### Mirror Quantum Volume Circuits[#](#module-mitiq.benchmarks.mirror_qv_circuits "Link to this heading")

Functions to create a Mirror Quantum Volume Benchmarking circuit
as defined in <https://arxiv.org/abs/2303.02108>.

mitiq.benchmarks.mirror\_qv\_circuits.generate\_mirror\_qv\_circuit(*num\_qubits*, *depth*, *decompose=False*, *seed=None*, *return\_type=None*)[[source]](_modules/mitiq/benchmarks/mirror_qv_circuits.html#generate_mirror_qv_circuit)[#](#mitiq.benchmarks.mirror_qv_circuits.generate_mirror_qv_circuit "Link to this definition")
:   Generate a mirror quantum volume circuit with the given number of qubits
    and depth as defined in [[3](bibliography.html#id2 "Mirko Amico, Helena Zhang, Petar Jurcevic, Lev S. Bishop, Paul Nation, Andrew Wack, and David C. McKay. Defining Standard Strategies for Quantum Benchmarks. (2023). arXiv:2303.02108.")].

    The generated circuit consists of a quantum volume circuit up to depth/2
    layers followed by an inverse of the quantum volume portion up to depth/2
    when depth is an even number.

    When depth is odd, the layers will be changed to depth+1.

    The ideal output bit-string is a string of zeroes.

    Parameters:
    :   * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the generated circuit.
        * **depth** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of layers in the generated circuit.
        * **decompose** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – Recursively decomposes the randomly sampled (numerical)
          unitary matrix gates into simpler gates.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for generating random circuit.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the returned
          circuits. See the keys of `mitiq.SUPPORTED_PROGRAM_TYPES`
          for options. If `None`, the returned circuits have type
          `cirq.Circuit`.

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

    Returns:
    :   A quantum volume circuit acting on `num_qubits` qubits.

#### Quantum Phase Estimation Circuits[#](#module-mitiq.benchmarks.qpe_circuits "Link to this heading")

Functions to create a QPE circuit.

mitiq.benchmarks.qpe\_circuits.generate\_qpe\_circuit(*evalue\_reg*, *input\_gate=cirq.T*, *return\_type=None*)[[source]](_modules/mitiq/benchmarks/qpe_circuits.html#generate_qpe_circuit)[#](#mitiq.benchmarks.qpe_circuits.generate_qpe_circuit "Link to this definition")
:   Returns a circuit to create a quantum phase estimation (QPE) circuit as
    defined in <https://en.wikipedia.org/wiki/Quantum_phase_estimation_algorithm>

    The unitary to estimate the phase of corresponds to a
    single-qubit gate (`input_gate`).

    The IQFT circuit defined in this method is taken from taken from Sec 7.7.4
    of [[85](bibliography.html#id78 "Thomas G. Wong. Introduction to Classical and Quantum Computing. Rooted Grove, (2022). ISBN 9798985593105.")]. The notation for eigenvalue register and eigenstate
    register used to define this function also follows from [[85](bibliography.html#id78 "Thomas G. Wong. Introduction to Classical and Quantum Computing. Rooted Grove, (2022). ISBN 9798985593105.")].

    Parameters:
    :   * **evalue\_reg** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of qubits in the eigenvalue register. The qubits
          in this variable are used to estimate the phase.
        * **input\_gate** (`Gate`) – The unitary to estimate the phase of as a single-qubit
          Cirq gate. Default gate used here is cirq.T.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Return type of the output circuit.

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

    Returns:
    :   A Quantum Phase Estimation circuit.

#### Quantum Volume Circuits[#](#module-mitiq.benchmarks.quantum_volume_circuits "Link to this heading")

Functions for creating circuits of the form used in quantum
volume experiments as defined in <https://arxiv.org/abs/1811.12926>.

Useful overview of quantum volume experiments:
<https://pennylane.ai/qml/demos/quantum_volume>

Cirq implementation of quantum volume circuits:
cirq-core/cirq/contrib/quantum\_volume/quantum\_volume.py

mitiq.benchmarks.quantum\_volume\_circuits.compute\_heavy\_bitstrings(*circuit*, *num\_qubits*)[[source]](_modules/mitiq/benchmarks/quantum_volume_circuits.html#compute_heavy_bitstrings)[#](#mitiq.benchmarks.quantum_volume_circuits.compute_heavy_bitstrings "Link to this definition")
:   Classically compute the heavy bitstrings of the provided circuit.

    The heavy bitstrings are defined as the output bit-strings that have a
    greater than median probability of being generated.

    Parameters:
    :   * **circuit** (`Circuit`) – The circuit to classically simulate.
        * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"))

    Return type:
    :   [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]]

    Returns:
    :   A list containing the heavy bitstrings.

mitiq.benchmarks.quantum\_volume\_circuits.generate\_quantum\_volume\_circuit(*num\_qubits*, *depth*, *decompose=False*, *seed=None*, *return\_type=None*)[[source]](_modules/mitiq/benchmarks/quantum_volume_circuits.html#generate_quantum_volume_circuit)[#](#mitiq.benchmarks.quantum_volume_circuits.generate_quantum_volume_circuit "Link to this definition")
:   Generate a quantum volume circuit with the given number of qubits and
    depth.

    The generated circuit consists of depth layers of random qubit
    permutations followed by random two-qubit gates that are sampled from the
    Haar measure on SU(4).

    Parameters:
    :   * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the generated circuit.
        * **depth** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of layers in the generated circuit.
        * **decompose** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – Recursively decomposes the randomly sampled (numerical)
          unitary matrix gates into simpler gates.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for generating random circuit.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the returned
          circuits. See the keys of `mitiq.SUPPORTED_PROGRAM_TYPES`
          for options. If `None`, the returned circuits have type
          `cirq.Circuit`.

    Return type:
    :   [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`], [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]]]

    Returns:
    :   A quantum volume circuit acting on `num_qubits` qubits.
        A list of the heavy bitstrings for the returned circuit.

#### Randomized Benchmarking Circuits[#](#module-mitiq.benchmarks.randomized_benchmarking "Link to this heading")

Functions for generating randomized benchmarking circuits.

mitiq.benchmarks.randomized\_benchmarking.generate\_rb\_circuits(*n\_qubits*, *num\_cliffords*, *trials=1*, *return\_type=None*, *seed=None*)[[source]](_modules/mitiq/benchmarks/randomized_benchmarking.html#generate_rb_circuits)[#](#mitiq.benchmarks.randomized_benchmarking.generate_rb_circuits "Link to this definition")
:   Returns a list of randomized benchmarking circuits, i.e. circuits that
    are equivalent to the identity.

    Parameters:
    :   * **n\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits. Can be either 1 or 2.
        * **num\_cliffords** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of Clifford group elements in the
          random circuits. This is proportional to the depth per circuit.
        * **trials** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of random circuits at each num\_cfd.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the
          returned circuits. See the keys of
          `mitiq.SUPPORTED_PROGRAM_TYPES` for options. If `None`, the
          returned circuits have type `cirq.Circuit`.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – A seed for generating randomized benchmarking circuits.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   A list of randomized benchmarking circuits.

#### Rotated Randomized Benchmarking Circuits[#](#module-mitiq.benchmarks.rotated_randomized_benchmarking "Link to this heading")

Functions for generating rotated randomized benchmarking circuits.

mitiq.benchmarks.rotated\_randomized\_benchmarking.generate\_rotated\_rb\_circuits(*n\_qubits*, *num\_cliffords*, *theta=None*, *trials=1*, *return\_type=None*, *seed=None*)[[source]](_modules/mitiq/benchmarks/rotated_randomized_benchmarking.html#generate_rotated_rb_circuits)[#](#mitiq.benchmarks.rotated_randomized_benchmarking.generate_rotated_rb_circuits "Link to this definition")
:   Generates a list of “rotated” randomized benchmarking circuits.
    This benchmarking method enables testing QEM techniques in more general
    scenarios, closer to real-world applications in which expectation values
    can take arbitrary values.

    Rotated randomized bencmarking circuits are randomized benchmarking
    circuits with an \(R\_z(\theta)\) rotation inserted in the middle, such
    that:

    \[C(\theta) = G\_n \dots G\_{n/2 +1} R\_z(\theta)G\_{n/2} \dots G\_2 G\_1\]

    where \(G\_j\) are Clifford elements or Clifford gates.

    For most values of the seed, the probability of the zero state is a
    sinusoidal function of \(\theta\). For some values of the seed
    the probability of the zero state is 1 for all \(\theta\).

    Since (up to factors of 2) we have
    \(R\_z(\theta) =cos(\theta) I + i \ sin(\theta) Z\), the rotated
    Clifford circuit \(C(\theta)\) can be written as a linear combination
    of just two Clifford circuits, and therefore it is still easy to
    classically simulate.

    Parameters:
    :   * **n\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits. Can be either 1 or 2.
        * **num\_cliffords** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of Clifford group elements in the
          random circuits. This is proportional to the depth per circuit.
        * **theta** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The rotation angle about the \(Z\) axis.
        * **trials** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of random circuits to return.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the
          returned circuits. See the keys of
          `mitiq.SUPPORTED_PROGRAM_TYPES` for options. If `None`, the
          returned circuits have type `cirq.Circuit`.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – A seed for generating radomzed benchmarking circuits.

    Return type:
    :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

    Returns:
    :   A list of rotated randomized benchmarking circuits.

#### Randomized Clifford+T Circuits[#](#module-mitiq.benchmarks.randomized_clifford_t_circuit "Link to this heading")

mitiq.benchmarks.randomized\_clifford\_t\_circuit.generate\_random\_clifford\_t\_circuit(*num\_qubits*, *num\_oneq\_cliffords*, *num\_twoq\_cliffords*, *num\_t\_gates*, *return\_type=None*, *seed=None*)[[source]](_modules/mitiq/benchmarks/randomized_clifford_t_circuit.html#generate_random_clifford_t_circuit)[#](#mitiq.benchmarks.randomized_clifford_t_circuit.generate_random_clifford_t_circuit "Link to this definition")
:   Generate a random quantum circuit with the given number of qubits,
    number of one-qubit Cliffords, number of two-qubit Cliffords and number
    of T gates.

    Parameters:
    :   * **num\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the generated circuit.
        * **num\_oneq\_cliffords** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of one-qubit Cliffords to be used.
        * **num\_twoq\_cliffords** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of two-qubit Cliffords to be used.
        * **num\_t\_gates** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of T gates to be used.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Seed for generating random circuit.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – String which specifies the type of the returned
          circuits. See the keys of `mitiq.SUPPORTED_PROGRAM_TYPES`
          for options. If `None`, the returned circuits have type
          `cirq.Circuit`.

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

    Returns:
    :   A quantum circuit acting on `num_qubits` qubits.

#### W State Circuits[#](#module-mitiq.benchmarks.w_state_circuits "Link to this heading")

Functions for creating a linear complexity W-state benchmarking circuit
as defined in [[4](bibliography.html#id16 "Diogo Cruz, Romain Fournier, Fabien Gremion, Alix Jeannerot, Kenichi Komagata, Tara Tosic, Jarla Thiesbrummel, Chun Lam Chan, Nicolas Macris, Marc-André Dupertuis, and Clément Javerzac-Galy. Efficient quantum algorithms for ghz and w states, and implementation on the ibm quantum computer. Advanced Quantum Technologies, 2(5-6):1900015, (2019). URL: https://arxiv.org/abs/1807.05572, doi:https://doi.org/10.48550/arXiv.1807.05572.")].

mitiq.benchmarks.w\_state\_circuits.generate\_w\_circuit(*n\_qubits*, *return\_type=None*)[[source]](_modules/mitiq/benchmarks/w_state_circuits.html#generate_w_circuit)[#](#mitiq.benchmarks.w_state_circuits.generate_w_circuit "Link to this definition")
:   Returns a circuit to create a `n_qubits` qubit Werner-state with
    linear complexity as defined in [[4](bibliography.html#id16 "Diogo Cruz, Romain Fournier, Fabien Gremion, Alix Jeannerot, Kenichi Komagata, Tara Tosic, Jarla Thiesbrummel, Chun Lam Chan, Nicolas Macris, Marc-André Dupertuis, and Clément Javerzac-Galy. Efficient quantum algorithms for ghz and w states, and implementation on the ibm quantum computer. Advanced Quantum Technologies, 2(5-6):1900015, (2019). URL: https://arxiv.org/abs/1807.05572, doi:https://doi.org/10.48550/arXiv.1807.05572.")].

    Parameters:
    :   * **n\_qubits** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of qubits in the circuit.
        * **return\_type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Return type of the output circuit.

    Return type:
    :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

    Returns:
    :   A W-state circuit of linear complexity acting on `n_qubits` qubits.

### Calibration[#](#module-mitiq.calibration.calibrator "Link to this heading")

*class* mitiq.calibration.calibrator.Calibrator(*executor*, *\**, *frontend*, *settings=<mitiq.calibration.settings.Settings object>*, *ideal\_executor=None*)[[source]](_modules/mitiq/calibration/calibrator.html#Calibrator)[#](#mitiq.calibration.calibrator.Calibrator "Link to this definition")
:   An object used to orchestrate experiments for calibrating optimal error
    mitigation strategies.

    Parameters:
    :   * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – An unmitigated executor returning a
          [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult").
        * **settings** ([`Settings`](#mitiq.calibration.settings.Settings "mitiq.calibration.settings.Settings")) – A `Settings` object which specifies the type and amount of
          circuits/error mitigation methods to run.
        * **frontend** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – The executor frontend as a string. For a list of supported
          frontends see `mitiq.SUPPORTED_PROGRAM_TYPES.keys()`,
        * **ideal\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – An optional simulated executor returning the ideal
          [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") without noise. Required when using
          custom benchmark circuits without a pre-set ideal distribution.

    best\_strategy()[[source]](_modules/mitiq/calibration/calibrator.html#Calibrator.best_strategy)[#](#mitiq.calibration.calibrator.Calibrator.best_strategy "Link to this definition")
    :   Finds the best strategy by using the parameters that had the
        smallest error.

        Parameters:
        :   **results** – Calibration experiment results. Obtained by first running
            [`run()`](#mitiq.calibration.calibrator.Calibrator.run "mitiq.calibration.calibrator.Calibrator.run").

        Return type:
        :   [`Strategy`](#mitiq.calibration.settings.Strategy "mitiq.calibration.settings.Strategy")

        Returns:
        :   A single `Strategy` object specifying the technique and
            parameters that performed best.

    *property* cirq\_executor*: [Executor](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")*[#](#mitiq.calibration.calibrator.Calibrator.cirq_executor "Link to this definition")
    :   Returns an executor which is able to run Cirq circuits
        by converting them and calling self.executor.

        Parameters:
        :   **executor** – Executor which takes as input QPROGRAM circuits.

        Returns:
        :   Executor which takes as input a Cirq circuits.

    execute\_with\_mitigation(*circuit*, *expval\_executor*, *observable=None*)[[source]](_modules/mitiq/calibration/calibrator.html#Calibrator.execute_with_mitigation)[#](#mitiq.calibration.calibrator.Calibrator.execute_with_mitigation "Link to this definition")
    :   See [`execute_with_mitigation()`](#mitiq.calibration.calibrator.execute_with_mitigation "mitiq.calibration.calibrator.execute_with_mitigation") for signature and details.

        Parameters:
        :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`])
            * **expval\_executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")])
            * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"))

        Return type:
        :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    get\_cost()[[source]](_modules/mitiq/calibration/calibrator.html#Calibrator.get_cost)[#](#mitiq.calibration.calibrator.Calibrator.get_cost "Link to this definition")
    :   Returns the expected number of noisy and ideal expectation values
        required for calibration.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]

        Returns:
        :   A summary of the number of circuits to be run.

    *property* ideal\_cirq\_executor*: [Executor](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [None](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")*[#](#mitiq.calibration.calibrator.Calibrator.ideal_cirq_executor "Link to this definition")
    :   Executor running ideal circuits if provided.

    run(*log=None*)[[source]](_modules/mitiq/calibration/calibrator.html#Calibrator.run)[#](#mitiq.calibration.calibrator.Calibrator.run "Link to this definition")
    :   Runs all the circuits required for calibration.

        Parameters:
        :   **log** ([`OutputForm`](#mitiq.calibration.calibrator.OutputForm "mitiq.calibration.calibrator.OutputForm") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – If set, detailed results of each experiment run by the
            calibrator are printed. The value corresponds to the format of
            the information and can be set to “flat” or “cartesian”.

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

*class* mitiq.calibration.calibrator.ExperimentResults(*strategies*, *problems*)[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults)[#](#mitiq.calibration.calibrator.ExperimentResults "Link to this definition")
:   Class to store calibration experiment data, and provide helper methods
    for computing results based on it.

    Parameters:
    :   * **strategies** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Strategy`](#mitiq.calibration.settings.Strategy "mitiq.calibration.settings.Strategy")])
        * **problems** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`BenchmarkProblem`](#mitiq.calibration.settings.BenchmarkProblem "mitiq.calibration.settings.BenchmarkProblem")])

    add\_result(*strategy*, *problem*, *\**, *ideal\_val*, *noisy\_val*, *mitigated\_val*)[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.add_result)[#](#mitiq.calibration.calibrator.ExperimentResults.add_result "Link to this definition")
    :   Add a single result from a (Strategy, BenchmarkProblem) pair and
        store the results.

        Parameters:
        :   * **strategy** ([`Strategy`](#mitiq.calibration.settings.Strategy "mitiq.calibration.settings.Strategy"))
            * **problem** ([`BenchmarkProblem`](#mitiq.calibration.settings.BenchmarkProblem "mitiq.calibration.settings.BenchmarkProblem"))
            * **ideal\_val** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))
            * **noisy\_val** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))
            * **mitigated\_val** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)"))

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    best\_strategy\_id()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.best_strategy_id)[#](#mitiq.calibration.calibrator.ExperimentResults.best_strategy_id "Link to this definition")
    :   Returns the strategy id that corresponds to the strategy that
        maintained the smallest error across all `BenchmarkProblem`
        instances.

        Return type:
        :   [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")

    ensure\_full()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.ensure_full)[#](#mitiq.calibration.calibrator.ExperimentResults.ensure_full "Link to this definition")
    :   Check to ensure all expected data is collected. All mitigated, noisy
        and ideal values must be nonempty for this to pass and return True.

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    is\_missing\_data()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.is_missing_data)[#](#mitiq.calibration.calibrator.ExperimentResults.is_missing_data "Link to this definition")
    :   Method to check if there is any missing data that was expected from
        the calibration experiments.

        Return type:
        :   [`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")

    log\_results\_cartesian()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.log_results_cartesian)[#](#mitiq.calibration.calibrator.ExperimentResults.log_results_cartesian "Link to this definition")
    :   Prints the results of the calibrator in cartesian form:

        ```
        ┌──────────────────────────────┬────────────────────────────┬────────────────────────────┐
        │ strategy\benchmark           │ Type: rb                   │ Type: ghz                  │
        │                              │ Num qubits: 2              │ Num qubits: 2              │
        │                              │ Circuit depth: 337         │ Circuit depth: 2           │
        │                              │ Two qubit gate count: 80   │ Two qubit gate count: 1    │
        ├──────────────────────────────┼────────────────────────────┼────────────────────────────┤
        │ Technique: ZNE               │ ✔                          │ ✘                          │
        │ Factory: Richardson          │ Noisy error: 0.1128        │ Noisy error: 0.0117        │
        │ Scale factors: 1.0, 2.0, 3.0 │ Mitigated error: 0.0501    │ Mitigated error: 0.0439    │
        │ Scale method: fold_global    │ Improvement factor: 2.2515 │ Improvement factor: 0.2665 │
        ├──────────────────────────────┼────────────────────────────┼────────────────────────────┤
        │ Technique: ZNE               │ ✔                          │ ✘                          │
        │ Factory: Richardson          │ Noisy error: 0.1128        │ Noisy error: 0.0117        │
        │ Scale factors: 1.0, 3.0, 5.0 │ Mitigated error: 0.0408    │ Mitigated error: 0.0171    │
        │ Scale method: fold_global    │ Improvement factor: 2.7672 │ Improvement factor: 0.6852 │
        └──────────────────────────────┴────────────────────────────┴────────────────────────────┘
        ```

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    log\_results\_flat()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.log_results_flat)[#](#mitiq.calibration.calibrator.ExperimentResults.log_results_flat "Link to this definition")
    :   Prints the results of the calibrator in flat form:

        ```
        ┌──────────────────────────┬──────────────────────────────┬────────────────────────────┐
        │ benchmark                │ strategy                     │ performance                │
        ├──────────────────────────┼──────────────────────────────┼────────────────────────────┤
        │ Type: rb                 │ Technique: ZNE               │ ✔                          │
        │ Num qubits: 2            │ Factory: Richardson          │ Noisy error: 0.101         │
        │ Circuit depth: 323       │ Scale factors: 1.0, 3.0, 5.0 │ Mitigated error: 0.0294    │
        │ Two qubit gate count: 77 │ Scale method: fold_global    │ Improvement factor: 3.4398 │
        ├──────────────────────────┼──────────────────────────────┼────────────────────────────┤
        │ Type: rb                 │ Technique: ZNE               │ ✔                          │
        │ Num qubits: 2            │ Factory: Richardson          │ Noisy error: 0.101         │
        │ Circuit depth: 323       │ Scale factors: 1.0, 2.0, 3.0 │ Mitigated error: 0.0501    │
        │ Two qubit gate count: 77 │ Scale method: fold_global    │ Improvement factor: 2.016  │
        ├──────────────────────────┼──────────────────────────────┼────────────────────────────┤
        │ Type: ghz                │ Technique: ZNE               │ ✔                          │
        │ Num qubits: 2            │ Factory: Richardson          │ Noisy error: 0.0128        │
        │ Circuit depth: 2         │ Scale factors: 1.0, 2.0, 3.0 │ Mitigated error: 0.0082    │
        │ Two qubit gate count: 1  │ Scale method: fold_global    │ Improvement factor: 1.561  │
        ├──────────────────────────┼──────────────────────────────┼────────────────────────────┤
        │ Type: ghz                │ Technique: ZNE               │ ✘                          │
        │ Num qubits: 2            │ Factory: Richardson          │ Noisy error: 0.0128        │
        │ Circuit depth: 2         │ Scale factors: 1.0, 3.0, 5.0 │ Mitigated error: 0.0137    │
        │ Two qubit gate count: 1  │ Scale method: fold_global    │ Improvement factor: 0.9369 │
        └──────────────────────────┴──────────────────────────────┴────────────────────────────┘
        ```

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    reset\_data()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.reset_data)[#](#mitiq.calibration.calibrator.ExperimentResults.reset_data "Link to this definition")
    :   Reset all experiment result data using NaN values.

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    squared\_errors()[[source]](_modules/mitiq/calibration/calibrator.html#ExperimentResults.squared_errors)[#](#mitiq.calibration.calibrator.ExperimentResults.squared_errors "Link to this definition")
    :   Returns an array of squared errors, one for each (strategy, problem)
        pair.

        Return type:
        :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`float32`]]

*exception* mitiq.calibration.calibrator.MissingResultsError[[source]](_modules/mitiq/calibration/calibrator.html#MissingResultsError)[#](#mitiq.calibration.calibrator.MissingResultsError "Link to this definition")

*class* mitiq.calibration.calibrator.OutputForm(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](_modules/mitiq/calibration/calibrator.html#OutputForm)[#](#mitiq.calibration.calibrator.OutputForm "Link to this definition")

mitiq.calibration.calibrator.convert\_to\_expval\_executor(*executor*, *bitstring*)[[source]](_modules/mitiq/calibration/calibrator.html#convert_to_expval_executor)[#](#mitiq.calibration.calibrator.convert_to_expval_executor "Link to this definition")
:   Constructs a new executor returning an expectation value given by the
    probability that the circuit outputs the most likely state according to the
    ideal distribution.

    Parameters:
    :   * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")) – Executor which returns a [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")
          (bitstrings).
        * **bitstring** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – The bitstring to measure the probability of. Defaults to
          ground state bitstring “00…0”.

    Return type:
    :   [`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor")

    Returns:
    :   A tuple containing an executor returning expectation values and,
        the most likely bitstring, according to the passed `distribution`

mitiq.calibration.calibrator.execute\_with\_mitigation(*circuit*, *executor*, *observable=None*, *\**, *calibrator*)[[source]](_modules/mitiq/calibration/calibrator.html#execute_with_mitigation)[#](#mitiq.calibration.calibrator.execute_with_mitigation "Link to this definition")
:   Estimates the error-mitigated expectation value associated to the
    input circuit, via the application of the best mitigation strategy, as
    determined by calibration.

    Parameters:
    :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The input circuit to execute.
        * **executor** ([`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") | [`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A Mitiq executor that executes a circuit and returns the
          unmitigated `QuantumResult` (e.g. an expectation value).
        * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable to compute the expectation value of. If
          `None`, the `executor` must return an expectation value.
          Otherwise, the `QuantumResult` returned by `executor` is used
          to compute the expectation of the observable.
        * **calibrator** ([`Calibrator`](#mitiq.calibration.calibrator.Calibrator "mitiq.calibration.calibrator.Calibrator")) – `Calibrator` object with which to determine the error
          mitigation strategy to execute the circuit.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

    Returns:
    :   The error mitigated expectation value.

*class* mitiq.calibration.settings.BenchmarkProblem(*id*, *circuit*, *type*, *ideal\_distribution*)[[source]](_modules/mitiq/calibration/settings.html#BenchmarkProblem)[#](#mitiq.calibration.settings.BenchmarkProblem "Link to this definition")
:   A dataclass containing information for instances of problems that will
    be run during the calibrations process.

    Parameters:
    :   * **id** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – A unique numerical id.
        * **circuit** (`Circuit`) – The circuit to be run.
        * **type** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – The type of the circuit (often the name of the algorithm)
        * **ideal\_distribution** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – The ideal probability distribution after applying
          `circuit`.

    converted\_circuit(*circuit\_type*)[[source]](_modules/mitiq/calibration/settings.html#BenchmarkProblem.converted_circuit)[#](#mitiq.calibration.settings.BenchmarkProblem.converted_circuit "Link to this definition")
    :   Adds measurements to all qubits and convert
        to the input frontend type.

        Parameters:
        :   **circuit\_type** (`SUPPORTED_PROGRAM_TYPES`) – The circuit type as a string.
            For supported circuit types see mitiq.SUPPORTED\_PROGRAM\_TYPES.

        Return type:
        :   [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]

        Returns:
        :   The converted circuit with final measurements.

    to\_dict()[[source]](_modules/mitiq/calibration/settings.html#BenchmarkProblem.to_dict)[#](#mitiq.calibration.settings.BenchmarkProblem.to_dict "Link to this definition")
    :   Produces a summary of the `BenchmarkProblem`, to be used in
        recording the results when running calibration experiments.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]

        Returns:
        :   Dictionary summarizing important attributes of the problem’s
            circuit.

*class* mitiq.calibration.settings.MitigationTechnique(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](_modules/mitiq/calibration/settings.html#MitigationTechnique)[#](#mitiq.calibration.settings.MitigationTechnique "Link to this definition")
:   Simple enum type for handling validation, and providing helper functions
    when accessing mitigation techniques.

*class* mitiq.calibration.settings.Settings(*benchmarks*, *strategies*)[[source]](_modules/mitiq/calibration/settings.html#Settings)[#](#mitiq.calibration.settings.Settings "Link to this definition")
:   A class to store the configuration settings of a [`Calibrator`](#mitiq.calibration.calibrator.Calibrator "mitiq.calibration.calibrator.Calibrator").

    Parameters:
    :   * **benchmarks** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]) –

          A list where each element is a dictionary of parameters for
          generating circuits to be used in calibration experiments. The
          dictionary keys include `circuit_type`, `num_qubits`,
          `circuit_depth`, and in the case of mirror circuits, a random
          seed `circuit_seed`. An example of input to `benchmarks` is:

          ```
          [
              {
                  "circuit_type": "rb",
                  "num_qubits": 2,
                  "circuit_depth": 7,
              },
              {
                  "circuit_type": "mirror",
                  "num_qubits": 2,
                  "circuit_depth": 7,
                  "circuit_seed": 1,
              }
          ]
          ```
        * **strategies** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]]) – A specification of the methods/parameters to be used in
          calibration experiments.

    make\_problems()[[source]](_modules/mitiq/calibration/settings.html#Settings.make_problems)[#](#mitiq.calibration.settings.Settings.make_problems "Link to this definition")
    :   Generate the benchmark problems for the calibration experiment.
        :rtype: [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`BenchmarkProblem`](#mitiq.calibration.settings.BenchmarkProblem "mitiq.calibration.settings.BenchmarkProblem")]
        :returns: A list of [`BenchmarkProblem`](#mitiq.calibration.settings.BenchmarkProblem "mitiq.calibration.settings.BenchmarkProblem") objects

    make\_strategies()[[source]](_modules/mitiq/calibration/settings.html#Settings.make_strategies)[#](#mitiq.calibration.settings.Settings.make_strategies "Link to this definition")
    :   Generates a list of [`Strategy`](#mitiq.calibration.settings.Strategy "mitiq.calibration.settings.Strategy") objects using the specified
        configurations.

        Return type:
        :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Strategy`](#mitiq.calibration.settings.Strategy "mitiq.calibration.settings.Strategy")]

        Returns:
        :   A list of [`Strategy`](#mitiq.calibration.settings.Strategy "mitiq.calibration.settings.Strategy") objects.

*class* mitiq.calibration.settings.Strategy(*id*, *technique*, *technique\_params*)[[source]](_modules/mitiq/calibration/settings.html#Strategy)[#](#mitiq.calibration.settings.Strategy "Link to this definition")
:   A dataclass which describes precisely an error mitigation approach by
    specifying a technique and the associated options.

    Parameters:
    :   * **id** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – A unique numerical id.
        * **technique** ([`MitigationTechnique`](#mitiq.calibration.settings.MitigationTechnique "mitiq.calibration.settings.MitigationTechnique")) – One of Mitiq’s support error mitigation strategies,
          specified as a [`MitigationTechnique`](#mitiq.calibration.settings.MitigationTechnique "mitiq.calibration.settings.MitigationTechnique").
        * **technique\_params** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]) – A dictionary of options to pass to the mitigation
          method specified in technique.

    to\_dict()[[source]](_modules/mitiq/calibration/settings.html#Strategy.to_dict)[#](#mitiq.calibration.settings.Strategy.to_dict "Link to this definition")
    :   A summary of the strategies parameters, without the technique added.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]

        Returns:
        :   A dictionary describing the strategies parameters.

### Executors[#](#module-mitiq.executor.executor "Link to this heading")

Defines utilities for efficiently running collections of circuits generated
by error mitigation techniques to compute expectation values.

*class* mitiq.executor.executor.Executor(*executor*, *max\_batch\_size=75*)[[source]](_modules/mitiq/executor/executor.html#Executor)[#](#mitiq.executor.executor.Executor "Link to this definition")
:   Tool for efficiently scheduling/executing quantum programs and storing
    the results.

    Parameters:
    :   * **executor** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`, [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]]], [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]) – A function which inputs a program and outputs a
          `mitiq.QuantumResult`, or inputs a sequence of programs and
          outputs a sequence of `mitiq.QuantumResult` s.
        * **max\_batch\_size** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Maximum number of programs that can be sent in a
          single batch (if the executor is batched).

    *property* can\_batch*: [bool](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")*[#](#mitiq.executor.executor.Executor.can_batch "Link to this definition")
    :   Returns True if the executor is recognized as a “batched executor”,
        else False.

        The executor is detected as “batched” if and only if it is annotated
        with a return type that is a subclass of `Iterable`. Common examples
        include:

        * `Iterable[QuantumResult]`
        * `List[QuantumResult]`/`list[QuantumResult]`
        * `Sequence[QuantumResult]`
        * `Tuple[QuantumResult]`/`tuple[QuantumResult]`

        Otherwise, it is considered “serial”.

        Batched executors can *run several quantum programs in a single call*.

        Returns:
        :   True if the executor is detected as batched, else False.

    evaluate(*circuits*, *observable=None*, *force\_run\_all=True*, *\*\*kwargs*)[[source]](_modules/mitiq/executor/executor.html#Executor.evaluate)[#](#mitiq.executor.executor.Executor.evaluate "Link to this definition")
    :   Returns the expectation value Tr[ρ O] for each circuit in
        `circuits` where O is the observable provided or implicitly defined
        by the `executor`. (The observable is implicitly defined when the
        `executor` returns float(s).)

        All executed circuits are stored in `self.executed_circuits`, and all
        quantum results are stored in `self.quantum_results`.

        Parameters:
        :   * **circuits** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`, [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]]) – A single circuit or list of circuits.
            * **observable** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Observable O in the expression Tr[ρ O]. If None,
              the `executor` must return a float (which corresponds to
              Tr[ρ O] for a specific, fixed observable O).
            * **force\_run\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, force every circuit in the input sequence
              to be executed (if some are identical). Else, detects identical
              circuits and runs a minimal set.
            * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))

        Return type:
        :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

        Returns:
        :   List of real valued expectation values.

    run(*circuits*, *force\_run\_all=True*, *\*\*kwargs*)[[source]](_modules/mitiq/executor/executor.html#Executor.run)[#](#mitiq.executor.executor.Executor.run "Link to this definition")
    :   Runs all input circuits using the least number of possible calls to
        the executor.

        Parameters:
        :   * **circuits** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`, [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]]) – Circuit or sequence thereof to execute with the executor.
            * **force\_run\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, force every circuit in the input sequence
              to be executed (if some are identical). Else, detects identical
              circuits and runs a minimal set.
            * **kwargs** ([`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)"))

        Return type:
        :   [`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]

### Observables[#](#observables "Link to this heading")

#### Observable[#](#module-mitiq.observable.observable "Link to this heading")

*class* mitiq.observable.observable.Observable(*\*paulis*)[[source]](_modules/mitiq/observable/observable.html#Observable)[#](#mitiq.observable.observable.Observable "Link to this definition")
:   A quantum observable typically used to compute its mitigated expectation
    value.

    Parameters:
    :   **paulis** ([`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")) – PauliStrings used to define the observable.

    expectation(*circuit*, *execute*)[[source]](_modules/mitiq/observable/observable.html#Observable.expectation)[#](#mitiq.observable.observable.Observable.expectation "Link to this definition")
    :   Computes the expectation value of the observable.

        This method executes the given quantum circuit and estimates the
        expectation value of the observable based on the measurement results.

        Parameters:
        :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The quantum circuit to be executed.
            * **execute** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]], [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")]) – A function that takes a quantum circuit as input and
            * **outcomes.** (*returns a QuantumResult containing measurement*)

        Return type:
        :   [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")

        Returns:
        :   The expectation value of the observable.

    *static* from\_pauli\_string\_collections(*\*pauli\_string\_collections*)[[source]](_modules/mitiq/observable/observable.html#Observable.from_pauli_string_collections)[#](#mitiq.observable.observable.Observable.from_pauli_string_collections "Link to this definition")
    :   Creates an `Observable` from one or more `PauliStringCollection`
        :   instances.

        Parameters:
        :   **pauli\_string\_collections** ([`PauliStringCollection`](#mitiq.observable.pauli.PauliStringCollection "mitiq.observable.pauli.PauliStringCollection")) – One or more collections of Pauli strings
            used to define the observable.

        Return type:
        :   [`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")

        Returns:
        :   An `Observable` containing the given Pauli string collections.

    matrix(*qubit\_indices=None*)[[source]](_modules/mitiq/observable/observable.html#Observable.matrix)[#](#mitiq.observable.observable.Observable.matrix "Link to this definition")
    :   Returns the (potentially very large) matrix of the `Observable`.

        Parameters:
        :   * **qubit\_indices** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional list of qubit indices specifying the order
            * **None** (*of qubits in the matrix representation. If*)
            * **default** (*the*)
            * **used.** (*ordering from self.qubit\_indices is*)

        Return type:
        :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

        Returns:
        :   A `NumPy` array representing the matrix form of the observable.

    measure\_in(*circuit*)[[source]](_modules/mitiq/observable/observable.html#Observable.measure_in)[#](#mitiq.observable.observable.Observable.measure_in "Link to this definition")
    :   Given a quantum circuit, this method returns a list of circuits
        where each circuit corresponds to a different group of commuting Pauli
        strings, which allows measurement in the appropriate basis.

        Parameters:
        :   * **circuit** ([`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]) – The quantum circuit in which the observable should be
            * **measured.**

        Return type:
        :   [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[`Circuit`, [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)"), [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)"), `Circuit`, [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)"), [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)"), `QasmStringType`]]

        Returns:
        :   A list of quantum circuits with the appropriate measurement
            settings for each group of Pauli strings.

    partition(*seed=None*)[[source]](_modules/mitiq/observable/observable.html#Observable.partition)[#](#mitiq.observable.observable.Observable.partition "Link to this definition")
    :   Partitions the observable’s Pauli strings into commuting groups.

        This method groups the `PauliStringCollection` instances such that
        each group consists of mutually commuting operators, which can be
        measured together in a quantum circuit.

        Note

        This method randomizes the way in which the list of
        paulis is partitioned.

        Parameters:
        :   **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – An optional seed for shuffling to ensure deterministic
            behavior when partitioning.

        Return type:
        :   [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")

#### Pauli Observable[#](#module-mitiq.observable.pauli "Link to this heading")

*class* mitiq.observable.pauli.PauliString(*spec=''*, *coeff=1.0*, *support=None*)[[source]](_modules/mitiq/observable/pauli.html#PauliString)[#](#mitiq.observable.pauli.PauliString "Link to this definition")
:   A `PauliString` is a (tensor) product of single-qubit Pauli gates
    \(I, X, Y\), and \(Z\), with a leading (real or complex)
    coefficient. `PauliString` objects can be measured in any
    `mitiq.QPROGRAM`.

    Parameters:
    :   * **spec** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – String specifier of the PauliString. Should only contain
          characters ‘I’, ‘X’, ‘Y’, and ‘Z’.
        * **coeff** ([`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")) – Coefficient of the PauliString.
        * **support** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Qubits the `spec` acts on, if provided.

    Examples

    ```
    >>> PauliString(spec="IXY")  # X(1)*Y(2)
    >>> PauliString(spec="ZZ", coeff=-0.5)  # -0.5*Z(0)*Z(1)
    >>> PauliString(spec="XZ", support=(10, 17))  # X(10)*Z(17)
    ```

    can\_be\_measured\_with(*other*)[[source]](_modules/mitiq/observable/pauli.html#PauliString.can_be_measured_with)[#](#mitiq.observable.pauli.PauliString.can_be_measured_with "Link to this definition")
    :   Returns True if the expectation value of the PauliString can be
        simultaneously estimated with other via single-qubit measurements.

        Parameters:
        :   **other** ([`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")) – The PauliString to check simultaneous measurement with.

        Return type:
        :   [`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")

    matrix(*qubit\_indices\_to\_include=None*)[[source]](_modules/mitiq/observable/pauli.html#PauliString.matrix)[#](#mitiq.observable.pauli.PauliString.matrix "Link to this definition")
    :   Returns the (potentially very large) matrix of the PauliString.

        Parameters:
        :   **qubit\_indices\_to\_include** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"))

        Return type:
        :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

    *property* spec*: [str](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")*[#](#mitiq.observable.pauli.PauliString.spec "Link to this definition")
    :   Returns a string representation of the Pauli gates in
        the PauliString.

    weight()[[source]](_modules/mitiq/observable/pauli.html#PauliString.weight)[#](#mitiq.observable.pauli.PauliString.weight "Link to this definition")
    :   Returns the weight of the PauliString, i.e., the number of
        non-identity terms in the PauliString.

        Return type:
        :   [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")

*class* mitiq.observable.pauli.PauliStringCollection(*\*paulis*, *check\_precondition=True*)[[source]](_modules/mitiq/observable/pauli.html#PauliStringCollection)[#](#mitiq.observable.pauli.PauliStringCollection "Link to this definition")
:   A collection of PauliStrings that qubit-wise commute and so can be
    measured with a single circuit.

    Parameters:
    :   * **paulis** ([`PauliString`](#mitiq.observable.pauli.PauliString "mitiq.observable.pauli.PauliString")) – PauliStrings to add to the collection.
        * **check\_precondition** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, raises an error if some of the
          `PauliString` objects do not qubit-wise commute.

    Example

    ```
    >>> pcol = PauliStringCollection(
    >>>     PauliString(spec="X"),
    >>>     PauliString(spec="IZ", coeff=-2.2)
    >>> )
    >>> print(pcol)  # X(0) + (-2.2+0j)*Z(1)
    >>> print(pcol.support())  # {0, 1}
    >>>
    >>> # XZ qubit-wise commutes with X(0) and Z(1), so can be added.
    >>> print(pcol.can_add(PauliString(spec="XZ")))  # True.
    >>> pcol.add(PauliString(spec="XZ"))
    >>> print(pcol)  # X(0) + (-2.2+0j)*Z(1) + X(0)*Z(1)
    >>>
    >>> # Z(0) doesn't qubit-wise commute with X(0), so can't be added.
    >>> print(pcol.can_add(PauliString(spec="Z")))  # False.
    ```

### Raw[#](#raw "Link to this heading")

#### Run experiments without error mitigation (raw results)[#](#module-mitiq.raw.raw "Link to this heading")

Run experiments without error mitigation.

## Core Utilities[#](#core-utilities "Link to this heading")

### Circuit types and result types[#](#circuit-types-and-result-types "Link to this heading")

mitiq.typing.QPROGRAM[#](#mitiq.typing.QPROGRAM "Link to this definition")
:   alias of `Circuit` | [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)") | [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)") | `Circuit` | [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)") | [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)") | `QasmStringType`

mitiq.typing.QuantumResult[#](#mitiq.typing.QuantumResult "Link to this definition")
:   alias of [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)") | [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult") | [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")

mitiq.typing.Bitstring[#](#mitiq.typing.Bitstring "Link to this definition")
:   alias of [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]

*class* mitiq.typing.MeasurementResult(*result*, *qubit\_indices=None*)[[source]](_modules/mitiq/typing.html#MeasurementResult)[#](#mitiq.typing.MeasurementResult "Link to this definition")
:   Mitiq object for collecting the bitstrings sampled from a quantum
    computer when executing a circuit. This is one of the possible types
    (see [`QuantumResult`](#mitiq.typing.QuantumResult "mitiq.typing.QuantumResult")) that an
    [`Executor`](#mitiq.executor.executor.Executor "mitiq.executor.executor.Executor") can return.

    Parameters:
    :   * **result** ([`Sequence`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Sequence "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)") | [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]]) – The sequence of measured bitstrings.
        * **qubit\_indices** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – The qubit indices associated to each
          bit in a bitstring (from left to right).
          If not given, Mitiq assumes the default ordering
          `tuple(range(self.nqubits))`, where `self.nqubits`
          is the bitstring length deduced from `result`.

    Example

    ```
    >>> mr = MeasurementResult(["001", "010", "001"])
    >>> mr.get_counts()
    {'001': 2, '010': 1}
    ```

    Warning

    Use caution when selecting the default option for `qubit_indices`,
    especially when estimating an [`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")
    acting on a subset of qubits. In this case Mitiq
    only applies measurement gates to the specific qubits and, therefore,
    it is essential to specify the corresponding `qubit_indices`.

    filter\_qubits(*qubit\_indices*)[[source]](_modules/mitiq/typing.html#MeasurementResult.filter_qubits)[#](#mitiq.typing.MeasurementResult.filter_qubits "Link to this definition")
    :   Returns the bitstrings associated to a subset of qubits.

        Parameters:
        :   **qubit\_indices** ([`list`](https://docs.python.org/3.11/library/stdtypes.html#list "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")])

        Return type:
        :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`int64`]]

    *classmethod* from\_counts(*counts*, *qubit\_indices=None*)[[source]](_modules/mitiq/typing.html#MeasurementResult.from_counts)[#](#mitiq.typing.MeasurementResult.from_counts "Link to this definition")
    :   Initializes a `MeasurementResult` from a dictionary of counts.

        **Example**:

        ```
        MeasurementResult.from_counts({"00": 175, "11": 177})
        ```

        Parameters:
        :   * **counts** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")])
            * **qubit\_indices** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"))

        Return type:
        :   [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")

    *classmethod* from\_dict(*data*)[[source]](_modules/mitiq/typing.html#MeasurementResult.from_dict)[#](#mitiq.typing.MeasurementResult.from_dict "Link to this definition")
    :   Loads a `MeasurementResult` from a Python dictionary.

        Note: Only `data["counts"]` and `data["qubit_indices"]` are used
        by this method. Total shots and number of qubits are deduced.

        Parameters:
        :   **data** ([`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")])

        Return type:
        :   [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")

    get\_counts()[[source]](_modules/mitiq/typing.html#MeasurementResult.get_counts)[#](#mitiq.typing.MeasurementResult.get_counts "Link to this definition")
    :   Returns a Python dictionary whose keys are the measured
        bitstrings and whose values are the counts.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")]

    prob\_distribution()[[source]](_modules/mitiq/typing.html#MeasurementResult.prob_distribution)[#](#mitiq.typing.MeasurementResult.prob_distribution "Link to this definition")
    :   Returns a Python dictionary whose keys are the measured
        bitstrings and whose values are their empirical frequencies.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]

    to\_dict()[[source]](_modules/mitiq/typing.html#MeasurementResult.to_dict)[#](#mitiq.typing.MeasurementResult.to_dict "Link to this definition")
    :   Exports data to a Python dictionary.

        Note: Information about the order measurements is not preserved.

        Return type:
        :   [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "(in Python v3.11)")[[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)"), [`Any`](https://docs.python.org/3.11/library/typing.html#typing.Any "(in Python v3.11)")]

### Mitiq Interface[#](#mitiq-interface "Link to this heading")

#### Braket Conversions[#](#module-mitiq.interface.mitiq_braket.conversions "Link to this heading")

mitiq.interface.mitiq\_braket.conversions.from\_braket(*circuit*)[[source]](_modules/mitiq/interface/mitiq_braket/conversions.html#from_braket)[#](#mitiq.interface.mitiq_braket.conversions.from_braket "Link to this definition")
:   Returns a Cirq circuit equivalent to the input Braket circuit.

    Note: The returned Cirq circuit acts on cirq.LineQubit’s with indices equal
    to the qubit indices of the Braket circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Braket circuit to convert to a Cirq circuit.

    Return type:
    :   `Circuit`

mitiq.interface.mitiq\_braket.conversions.to\_braket(*circuit*)[[source]](_modules/mitiq/interface/mitiq_braket/conversions.html#to_braket)[#](#mitiq.interface.mitiq_braket.conversions.to_braket "Link to this definition")
:   Returns a Braket circuit equivalent to the input Cirq circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Cirq circuit to convert to a Braket circuit.

    Return type:
    :   `Circuit`

#### Cirq Utils[#](#module-mitiq.interface.mitiq_cirq.cirq_utils "Link to this heading")

Cirq utility functions.

mitiq.interface.mitiq\_cirq.cirq\_utils.compute\_density\_matrix(*circuit*, *noise\_model\_function=<function amplitude\_damp>*, *noise\_level=(0.01*, *)*)[[source]](_modules/mitiq/interface/mitiq_cirq/cirq_utils.html#compute_density_matrix)[#](#mitiq.interface.mitiq_cirq.cirq_utils.compute_density_matrix "Link to this definition")
:   Returns the density matrix of the quantum state after the
    (noisy) execution of the input circuit.

    Parameters:
    :   * **circuit** (`Circuit`) – The input Cirq circuit.
        * **noise\_model** – Input Cirq noise model. Default is amplitude damping.
        * **noise\_level** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Noise rate as a tuple of floats.
        * **noise\_model\_function** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[[`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), `NoiseModel`, `Gate`]])

    Return type:
    :   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]

    Returns:
    :   The final density matrix as a NumPy array.

mitiq.interface.mitiq\_cirq.cirq\_utils.execute\_with\_depolarizing\_noise(*circuit*, *obs*, *noise*)[[source]](_modules/mitiq/interface/mitiq_cirq/cirq_utils.html#execute_with_depolarizing_noise)[#](#mitiq.interface.mitiq_cirq.cirq_utils.execute_with_depolarizing_noise "Link to this definition")
:   Simulates a circuit with depolarizing noise
    and returns the expectation value of the input observable.
    The expectation value is deterministically computed from
    the final density matrix and, therefore, shot noise is absent.

    Parameters:
    :   * **circuit** (`Circuit`) – The input Cirq circuit.
        * **obs** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – The observable to measure as a NumPy array.
        * **noise** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The depolarizing noise as a float, i.e. 0.001 is 0.1% noise.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value of obs as a float.

mitiq.interface.mitiq\_cirq.cirq\_utils.sample\_bitstrings(*circuit*, *noise\_model\_function=<function amplitude\_damp>*, *noise\_level=(0.01*, *)*, *sampler=<cirq.sim.density\_matrix\_simulator.DensityMatrixSimulator object>*, *shots=8192*)[[source]](_modules/mitiq/interface/mitiq_cirq/cirq_utils.html#sample_bitstrings)[#](#mitiq.interface.mitiq_cirq.cirq_utils.sample_bitstrings "Link to this definition")
:   Adds noise to the input circuit. The noise is added based on a
    particular noise model and some value for the error rate.

    Parameters:
    :   * **circuit** (`Circuit`) – The input Cirq circuit with measurements applied.
        * **noise\_model** – Input Cirq noise model. Default is amplitude damping.
        * **noise\_level** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")]) – Noise rate as a tuple of floats.
        * **sampler** (`Sampler`) – Cirq simulator from which the result will be sampled from.
        * **shots** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – Number of measurements.
        * **noise\_model\_function** ([`Callable`](https://docs.python.org/3.11/library/collections.abc.html#collections.abc.Callable "(in Python v3.11)")[[`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)"), [`Union`](https://docs.python.org/3.11/library/typing.html#typing.Union "(in Python v3.11)")[[`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)"), `NoiseModel`, `Gate`]])

    Return type:
    :   [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")

    Returns:
    :   Sampled outcome from a measurement.

#### Pennylane Conversions[#](#module-mitiq.interface.mitiq_pennylane.conversions "Link to this heading")

Functions to convert between Mitiq’s internal circuit representation and
Pennylane’s circuit representation.

*exception* mitiq.interface.mitiq\_pennylane.conversions.UnsupportedQuantumTapeError[[source]](_modules/mitiq/interface/mitiq_pennylane/conversions.html#UnsupportedQuantumTapeError)[#](#mitiq.interface.mitiq_pennylane.conversions.UnsupportedQuantumTapeError "Link to this definition")

mitiq.interface.mitiq\_pennylane.conversions.from\_pennylane(*tape*)[[source]](_modules/mitiq/interface/mitiq_pennylane/conversions.html#from_pennylane)[#](#mitiq.interface.mitiq_pennylane.conversions.from_pennylane "Link to this definition")
:   Returns a Mitiq circuit equivalent to the input QuantumTape.

    Parameters:
    :   **tape** ([`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)")) – Pennylane QuantumTape to convert to a Mitiq circuit.

    Return type:
    :   `Circuit`

    Returns:
    :   Mitiq circuit representation equivalent to the input QuantumTape.

mitiq.interface.mitiq\_pennylane.conversions.to\_pennylane(*circuit*)[[source]](_modules/mitiq/interface/mitiq_pennylane/conversions.html#to_pennylane)[#](#mitiq.interface.mitiq_pennylane.conversions.to_pennylane "Link to this definition")
:   Returns a QuantumTape equivalent to the input Mitiq circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Mitiq circuit to convert to a Pennylane QuantumTape.

    Return type:
    :   [`QuantumTape`](https://docs.pennylane.ai/en/stable/code/api/pennylane.tape.QuantumTape.html#pennylane.tape.QuantumTape "(in PennyLane v0.44)")

    Returns:
    :   QuantumTape object equivalent to the input Mitiq circuit.

#### PyQuil Conversions[#](#module-mitiq.interface.mitiq_pyquil.conversions "Link to this heading")

Functions to convert between Mitiq’s internal circuit representation and
pyQuil’s circuit representation (Quil programs).

mitiq.interface.mitiq\_pyquil.conversions.from\_pyquil(*program*)[[source]](_modules/mitiq/interface/mitiq_pyquil/conversions.html#from_pyquil)[#](#mitiq.interface.mitiq_pyquil.conversions.from_pyquil "Link to this definition")
:   Returns a Mitiq circuit equivalent to the input pyQuil Program.

    Parameters:
    :   **program** ([`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)")) – PyQuil Program to convert to a Mitiq circuit.

    Return type:
    :   `Circuit`

    Returns:
    :   Mitiq circuit representation equivalent to the input pyQuil Program.

mitiq.interface.mitiq\_pyquil.conversions.from\_quil(*quil*)[[source]](_modules/mitiq/interface/mitiq_pyquil/conversions.html#from_quil)[#](#mitiq.interface.mitiq_pyquil.conversions.from_quil "Link to this definition")
:   Returns a Mitiq circuit equivalent to the input Quil string.

    Parameters:
    :   **quil** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – Quil string to convert to a Mitiq circuit.

    Return type:
    :   `Circuit`

    Returns:
    :   Mitiq circuit representation equivalent to the input Quil string.

mitiq.interface.mitiq\_pyquil.conversions.to\_pyquil(*circuit*)[[source]](_modules/mitiq/interface/mitiq_pyquil/conversions.html#to_pyquil)[#](#mitiq.interface.mitiq_pyquil.conversions.to_pyquil "Link to this definition")
:   Returns a pyQuil Program equivalent to the input Mitiq circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Mitiq circuit to convert to a pyQuil Program.

    Return type:
    :   [`Program`](https://pyquil-docs.rigetti.com/en/stable/apidocs/pyquil.html#pyquil.Program "(in pyQuil v4.17.0)")

    Returns:
    :   pyquil.Program object equivalent to the input Mitiq circuit.

mitiq.interface.mitiq\_pyquil.conversions.to\_quil(*circuit*)[[source]](_modules/mitiq/interface/mitiq_pyquil/conversions.html#to_quil)[#](#mitiq.interface.mitiq_pyquil.conversions.to_quil "Link to this definition")
:   Returns a Quil string representing the input Mitiq circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Mitiq circuit to convert to a Quil string.

    Returns:
    :   Quil string equivalent to the input Mitiq circuit.

    Return type:
    :   QuilType

#### Qibo Conversions[#](#qibo-conversions "Link to this heading")

mitiq.interface.mitiq\_qibo.conversions.from\_qibo(*qibo\_circuit*)[[source]](_modules/mitiq/interface/mitiq_qibo/conversions.html#from_qibo)[#](#mitiq.interface.mitiq_qibo.conversions.from_qibo "Link to this definition")
:   Returns a Cirq circuit equivalent to the input QiboCircuit.

    Parameters:
    :   **qibo\_circuit** ([`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)")) – QiboCircuit to convert to a Cirq circuit.

    Return type:
    :   `Circuit`

    Returns:
    :   Cirq circuit representation equivalent to the input QiboCircuit.

mitiq.interface.mitiq\_qibo.conversions.to\_qibo(*circuit*)[[source]](_modules/mitiq/interface/mitiq_qibo/conversions.html#to_qibo)[#](#mitiq.interface.mitiq_qibo.conversions.to_qibo "Link to this definition")
:   Returns a QiboCircuit equivalent to the input Cirq circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Cirq circuit to convert to a QiboCircuit.

    Return type:
    :   [`Circuit`](https://qibo.science/qibo/stable/api-reference/qibo.html#qibo.models.circuit.Circuit "(in qibo)")

    Returns:
    :   QiboCircuit object equivalent to the input Mitiq circuit.

#### Qiskit Conversions[#](#module-mitiq.interface.mitiq_qiskit.conversions "Link to this heading")

Functions to convert between Mitiq’s internal circuit representation and
Qiskit’s circuit representation.

mitiq.interface.mitiq\_qiskit.conversions.from\_qasm(*qasm*)[[source]](_modules/mitiq/interface/mitiq_qiskit/conversions.html#from_qasm)[#](#mitiq.interface.mitiq_qiskit.conversions.from_qasm "Link to this definition")
:   Returns a Mitiq circuit equivalent to the input QASM string.

    Parameters:
    :   **qasm** ([`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")) – QASM string to convert to a Mitiq circuit.

    Return type:
    :   `Circuit`

    Returns:
    :   Mitiq circuit representation equivalent to the input QASM string.

mitiq.interface.mitiq\_qiskit.conversions.from\_qiskit(*circuit*)[[source]](_modules/mitiq/interface/mitiq_qiskit/conversions.html#from_qiskit)[#](#mitiq.interface.mitiq_qiskit.conversions.from_qiskit "Link to this definition")
:   Returns a Mitiq circuit equivalent to the input Qiskit circuit.

    Parameters:
    :   **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – Qiskit circuit to convert to a Mitiq circuit.

    Return type:
    :   `Circuit`

    Returns:
    :   Mitiq circuit representation equivalent to the input Qiskit circuit.

mitiq.interface.mitiq\_qiskit.conversions.to\_qasm(*circuit*)[[source]](_modules/mitiq/interface/mitiq_qiskit/conversions.html#to_qasm)[#](#mitiq.interface.mitiq_qiskit.conversions.to_qasm "Link to this definition")
:   Returns a QASM string representing the input Mitiq circuit.

    Parameters:
    :   **circuit** (`Circuit`) – Mitiq circuit to convert to a QASM string.

    Returns:
    :   QASM string equivalent to the input Mitiq circuit.

    Return type:
    :   QASMType

mitiq.interface.mitiq\_qiskit.conversions.to\_qiskit(*circuit*)[[source]](_modules/mitiq/interface/mitiq_qiskit/conversions.html#to_qiskit)[#](#mitiq.interface.mitiq_qiskit.conversions.to_qiskit "Link to this definition")
:   Returns a Qiskit circuit equivalent to the input Mitiq circuit. Note
    that the output circuit registers may not match the input circuit
    registers.

    Parameters:
    :   **circuit** (`Circuit`) – Mitiq circuit to convert to a Qiskit circuit.

    Return type:
    :   [`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")

    Returns:
    :   Qiskit.QuantumCircuit object equivalent to the input Mitiq circuit.

#### Qiskit Utils[#](#module-mitiq.interface.mitiq_qiskit.qiskit_utils "Link to this heading")

Qiskit utility functions.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.compute\_expectation\_value\_on\_noisy\_backend(*circuit*, *obs*, *backend=None*, *noise\_model=None*, *shots=10000*, *measure\_all=False*, *qubit\_indices=None*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#compute_expectation_value_on_noisy_backend)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.compute_expectation_value_on_noisy_backend "Link to this definition")
:   Returns the noisy expectation value of the input Mitiq observable
    obtained from executing the input circuit on a Qiskit backend.

    Parameters:
    :   * **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – The input Qiskit circuit.
        * **obs** ([`Observable`](#mitiq.observable.observable.Observable "mitiq.observable.observable.Observable")) – The Mitiq observable to compute the expectation value of.
        * **backend** ([`Backend`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.providers.Backend "(in Qiskit v2.3)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – A real or fake Qiskit backend. The input circuit
          should be transpiled into a compatible gate set.
        * **noise\_model** (`NoiseModel` | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – A valid Qiskit `NoiseModel` object. This option is used
          if and only if `backend` is `None`. In this case a default
          density matrix simulator is used with `optimization_level=0`.
        * **shots** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of measurements.
        * **measure\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, measurement gates are applied to all qubits.
        * **qubit\_indices** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional qubit indices associated to bitstrings.

    Return type:
    :   [`complex`](https://docs.python.org/3.11/library/functions.html#complex "(in Python v3.11)")

    Returns:
    :   The noisy expectation value.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.execute(*circuit*, *obs*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#execute)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute "Link to this definition")
:   Simulates a noiseless evolution and returns the
    expectation value of some observable.

    Parameters:
    :   * **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – The input Qiskit circuit.
        * **obs** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – The observable to measure as a NumPy array.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value of obs as a float.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.execute\_with\_noise(*circuit*, *obs*, *noise\_model*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#execute_with_noise)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute_with_noise "Link to this definition")
:   Simulates the evolution of the noisy circuit and returns
    the exact expectation value of the observable.

    Parameters:
    :   * **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – The input Qiskit circuit.
        * **obs** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – The observable to measure as a NumPy array.
        * **noise\_model** (`NoiseModel`) – The input Qiskit noise model.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value of obs as a float.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.execute\_with\_shots(*circuit*, *obs*, *shots*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#execute_with_shots)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute_with_shots "Link to this definition")
:   Simulates the evolution of the circuit and returns
    the expectation value of the observable.

    Parameters:
    :   * **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – The input Qiskit circuit.
        * **obs** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – The observable to measure as a NumPy array.
        * **shots** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of measurements.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value of obs as a float.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.execute\_with\_shots\_and\_noise(*circuit*, *obs*, *noise\_model*, *shots*, *seed=None*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#execute_with_shots_and_noise)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute_with_shots_and_noise "Link to this definition")
:   Simulates the evolution of the noisy circuit and returns
    the statistical estimate of the expectation value of the observable.

    Parameters:
    :   * **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – The input Qiskit circuit.
        * **obs** ([`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)")[[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)"), [`...`](https://docs.python.org/3.11/library/constants.html#Ellipsis "(in Python v3.11)")], [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "(in NumPy v2.4)")[`complex64`]]) – The observable to measure as a NumPy array.
        * **noise\_model** (`NoiseModel`) – The input Qiskit noise model.
        * **shots** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of measurements.
        * **seed** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional seed for qiskit simulator.

    Return type:
    :   [`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")

    Returns:
    :   The expectation value of obs as a float.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.initialized\_depolarizing\_noise(*noise\_level*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#initialized_depolarizing_noise)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.initialized_depolarizing_noise "Link to this definition")
:   Initializes a depolarizing noise Qiskit NoiseModel.

    Parameters:
    :   **noise\_level** ([`float`](https://docs.python.org/3.11/library/functions.html#float "(in Python v3.11)")) – The noise strength as a float, e.g., 0.01 is 1%.

    Return type:
    :   `NoiseModel`

    Returns:
    :   A Qiskit depolarizing NoiseModel.

mitiq.interface.mitiq\_qiskit.qiskit\_utils.sample\_bitstrings(*circuit*, *backend=None*, *noise\_model=None*, *shots=10000*, *measure\_all=False*, *qubit\_indices=None*)[[source]](_modules/mitiq/interface/mitiq_qiskit/qiskit_utils.html#sample_bitstrings)[#](#mitiq.interface.mitiq_qiskit.qiskit_utils.sample_bitstrings "Link to this definition")
:   Returns measurement bitstrings obtained from executing the input circuit
    on a Qiskit backend (passed as an argument).
    Note that the input circuit must contain measurement gates
    (unless `measure_all` is `True`).

    Parameters:
    :   * **circuit** ([`QuantumCircuit`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.circuit.QuantumCircuit "(in Qiskit v2.3)")) – The input Qiskit circuit.
        * **backend** ([`Backend`](https://quantum.cloud.ibm.com/docs/api/qiskit/qiskit.providers.Backend "(in Qiskit v2.3)") | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – A real or fake Qiskit backend. The input circuit
          should be transpiled into a compatible gate set.
          It may be necessary to set `optimization_level=0` when
          transpiling.
        * **noise\_model** (`NoiseModel` | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – A valid Qiskit `NoiseModel` object. This option is used
          if and only if `backend` is `None`. In this case a default
          density matrix simulator is used with `optimization_level=0`.
        * **shots** ([`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")) – The number of measurements.
        * **measure\_all** ([`bool`](https://docs.python.org/3.11/library/functions.html#bool "(in Python v3.11)")) – If True, measurement gates are applied to all qubits.
        * **qubit\_indices** ([`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "(in Python v3.11)")[[`int`](https://docs.python.org/3.11/library/functions.html#int "(in Python v3.11)")] | [`None`](https://docs.python.org/3.11/library/constants.html#None "(in Python v3.11)")) – Optional qubit indices associated to bitstrings.

    Return type:
    :   [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")

    Returns:
    :   The measured bitstrings casted as a Mitiq [`MeasurementResult`](#mitiq.typing.MeasurementResult "mitiq.typing.MeasurementResult")
        object.

#### OpenQASM Conversions[#](#module-mitiq.interface.mitiq_openqasm.conversions "Link to this heading")

Functions to convert between Mitiq’s internal circuit representation and
OpenQASM’s circuit representation.

mitiq.interface.mitiq\_openqasm.conversions.from\_openqasm(*circuit*)[[source]](_modules/mitiq/interface/mitiq_openqasm/conversions.html#from_openqasm)[#](#mitiq.interface.mitiq_openqasm.conversions.from_openqasm "Link to this definition")
:   Convert a OpenQASM program to a cirq Circuit.
    :type circuit: [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")
    :param circuit: The OpenQASM program to convert.
    :type circuit: str

    Returns:
    :   The converted cirq Circuit.

    Return type:
    :   Circuit

mitiq.interface.mitiq\_openqasm.conversions.to\_openqasm(*circuit*)[[source]](_modules/mitiq/interface/mitiq_openqasm/conversions.html#to_openqasm)[#](#mitiq.interface.mitiq_openqasm.conversions.to_openqasm "Link to this definition")
:   Convert a cirq Circuit to OpenQASM program.
    :type circuit: `Circuit`
    :param circuit: The cirq Circuit to convert.
    :type circuit: Circuit

    Returns:
    :   The converted OpenQASM program.

    Return type:
    :   [str](https://docs.python.org/3.11/library/stdtypes.html#str "(in Python v3.11)")

[previous

Mitiq paper codeblocks](examples/mitiq-paper/mitiq-paper-codeblocks.html "previous page")
[next

Contributing](toc_contributing.html "next page")

On this page

* [Error-Mitigation Techniques](#error-mitigation-techniques)
  + [Clifford Data Regression](#clifford-data-regression)
    - [Clifford Data Regression (High-Level Tools)](#module-mitiq.cdr.cdr)
      * [`cdr_decorator()`](#mitiq.cdr.cdr.cdr_decorator)
      * [`execute_with_cdr()`](#mitiq.cdr.cdr.execute_with_cdr)
      * [`mitigate_executor()`](#mitiq.cdr.cdr.mitigate_executor)
    - [Clifford Training Data](#module-mitiq.cdr.clifford_training_data)
      * [`generate_training_circuits()`](#mitiq.cdr.clifford_training_data.generate_training_circuits)
    - [Data Regression](#module-mitiq.cdr.data_regression)
      * [`linear_fit_function()`](#mitiq.cdr.data_regression.linear_fit_function)
      * [`linear_fit_function_no_intercept()`](#mitiq.cdr.data_regression.linear_fit_function_no_intercept)
  + [Digital Dynamical Decoupling](#digital-dynamical-decoupling)
    - [Digital Dynamical Decoupling (High-Level Tools)](#module-mitiq.ddd.ddd)
      * [`combine_results()`](#mitiq.ddd.ddd.combine_results)
      * [`construct_circuits()`](#mitiq.ddd.ddd.construct_circuits)
      * [`ddd_decorator()`](#mitiq.ddd.ddd.ddd_decorator)
      * [`execute_with_ddd()`](#mitiq.ddd.ddd.execute_with_ddd)
      * [`mitigate_executor()`](#mitiq.ddd.ddd.mitigate_executor)
    - [Insertion](#module-mitiq.ddd.insertion)
      * [`get_slack_matrix_from_circuit_mask()`](#mitiq.ddd.insertion.get_slack_matrix_from_circuit_mask)
      * [`insert_ddd_sequences()`](#mitiq.ddd.insertion.insert_ddd_sequences)
    - [Rules](#module-mitiq.ddd.rules.rules)
      * [`general_rule()`](#mitiq.ddd.rules.rules.general_rule)
      * [`repeated_rule()`](#mitiq.ddd.rules.rules.repeated_rule)
      * [`xx()`](#mitiq.ddd.rules.rules.xx)
      * [`xyxy()`](#mitiq.ddd.rules.rules.xyxy)
      * [`yy()`](#mitiq.ddd.rules.rules.yy)
  + [Layerwise Richardson Extrapolation](#module-mitiq.lre.lre)
    - [`combine_results()`](#mitiq.lre.lre.combine_results)
    - [`construct_circuits()`](#mitiq.lre.lre.construct_circuits)
    - [`execute_with_lre()`](#mitiq.lre.lre.execute_with_lre)
    - [`lre_decorator()`](#mitiq.lre.lre.lre_decorator)
    - [`mitigate_executor()`](#mitiq.lre.lre.mitigate_executor)
    - [`get_scale_factor_vectors()`](#mitiq.lre.multivariate_scaling.layerwise_folding.get_scale_factor_vectors)
    - [`multivariate_layer_scaling()`](#mitiq.lre.multivariate_scaling.layerwise_folding.multivariate_layer_scaling)
    - [`multivariate_richardson_coefficients()`](#mitiq.lre.inference.multivariate_richardson.multivariate_richardson_coefficients)
    - [`sample_matrix()`](#mitiq.lre.inference.multivariate_richardson.sample_matrix)
  + [Pauli Twirling](#module-mitiq.pt.pt)
    - [`add_noise_to_two_qubit_gates()`](#mitiq.pt.pt.add_noise_to_two_qubit_gates)
    - [`generate_pauli_twirl_variants()`](#mitiq.pt.pt.generate_pauli_twirl_variants)
    - [`twirl_CNOT_gates()`](#mitiq.pt.pt.twirl_CNOT_gates)
    - [`twirl_CZ_gates()`](#mitiq.pt.pt.twirl_CZ_gates)
  + [Probabilistic Error Cancellation](#probabilistic-error-cancellation)
    - [Probabilistic Error Cancellation (High-Level Tools)](#module-mitiq.pec.pec)
      * [`LargeSampleWarning`](#mitiq.pec.pec.LargeSampleWarning)
      * [`combine_results()`](#mitiq.pec.pec.combine_results)
      * [`construct_circuits()`](#mitiq.pec.pec.construct_circuits)
      * [`execute_with_pec()`](#mitiq.pec.pec.execute_with_pec)
      * [`mitigate_executor()`](#mitiq.pec.pec.mitigate_executor)
      * [`pec_decorator()`](#mitiq.pec.pec.pec_decorator)
    - [Quasi-Probability Representations](#module-mitiq.pec.representations.optimal)
      * [`find_optimal_representation()`](#mitiq.pec.representations.optimal.find_optimal_representation)
      * [`minimize_one_norm()`](#mitiq.pec.representations.optimal.minimize_one_norm)
      * [`amplitude_damping_kraus()`](#mitiq.pec.representations.damping.amplitude_damping_kraus)
      * [`global_depolarizing_kraus()`](#mitiq.pec.representations.depolarizing.global_depolarizing_kraus)
      * [`local_depolarizing_kraus()`](#mitiq.pec.representations.depolarizing.local_depolarizing_kraus)
      * [`represent_operation_with_global_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operation_with_global_depolarizing_noise)
      * [`represent_operation_with_local_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operation_with_local_depolarizing_noise)
      * [`represent_operations_in_circuit_with_global_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operations_in_circuit_with_global_depolarizing_noise)
      * [`represent_operations_in_circuit_with_local_depolarizing_noise()`](#mitiq.pec.representations.depolarizing.represent_operations_in_circuit_with_local_depolarizing_noise)
    - [Learning-based PEC](#module-mitiq.pec.representations.biased_noise)
      * [`represent_operation_with_local_biased_noise()`](#mitiq.pec.representations.biased_noise.represent_operation_with_local_biased_noise)
      * [`biased_noise_loss_function()`](#mitiq.pec.representations.learning.biased_noise_loss_function)
      * [`depolarizing_noise_loss_function()`](#mitiq.pec.representations.learning.depolarizing_noise_loss_function)
      * [`learn_biased_noise_parameters()`](#mitiq.pec.representations.learning.learn_biased_noise_parameters)
      * [`learn_depolarizing_noise_parameter()`](#mitiq.pec.representations.learning.learn_depolarizing_noise_parameter)
    - [Sampling from a Noisy Decomposition of an Ideal Operation](#module-mitiq.pec.sampling)
      * [`sample_circuit()`](#mitiq.pec.sampling.sample_circuit)
      * [`sample_sequence()`](#mitiq.pec.sampling.sample_sequence)
    - [Probabilistic Error Cancellation Types](#module-mitiq.pec.types.types)
      * [`NoisyBasis`](#mitiq.pec.types.types.NoisyBasis)
      * [`NoisyOperation`](#mitiq.pec.types.types.NoisyOperation)
        + [`NoisyOperation.circuit`](#mitiq.pec.types.types.NoisyOperation.circuit)
        + [`NoisyOperation.native_circuit`](#mitiq.pec.types.types.NoisyOperation.native_circuit)
      * [`OperationRepresentation`](#mitiq.pec.types.types.OperationRepresentation)
        + [`OperationRepresentation.coeffs`](#mitiq.pec.types.types.OperationRepresentation.coeffs)
        + [`OperationRepresentation.distribution`](#mitiq.pec.types.types.OperationRepresentation.distribution)
        + [`OperationRepresentation.norm`](#mitiq.pec.types.types.OperationRepresentation.norm)
        + [`OperationRepresentation.sample()`](#mitiq.pec.types.types.OperationRepresentation.sample)
    - [Utilities for Quantum Channels](#module-mitiq.pec.channels)
      * [`choi_to_super()`](#mitiq.pec.channels.choi_to_super)
      * [`kraus_to_choi()`](#mitiq.pec.channels.kraus_to_choi)
      * [`kraus_to_super()`](#mitiq.pec.channels.kraus_to_super)
      * [`super_to_choi()`](#mitiq.pec.channels.super_to_choi)
  + [Quantum Subspace Expansion](#module-mitiq.qse.qse)
    - [`execute_with_qse()`](#mitiq.qse.qse.execute_with_qse)
    - [`mitigate_executor()`](#mitiq.qse.qse.mitigate_executor)
    - [`qse_decorator()`](#mitiq.qse.qse.qse_decorator)
  + [Readout-Error Mitigation](#readout-error-mitigation)
    - [Postselection](#module-mitiq.rem.post_select)
      * [`post_select()`](#mitiq.rem.post_select.post_select)
    - [REM Technique](#module-mitiq.rem.rem)
      * [`execute_with_rem()`](#mitiq.rem.rem.execute_with_rem)
      * [`mitigate_executor()`](#mitiq.rem.rem.mitigate_executor)
      * [`rem_decorator()`](#mitiq.rem.rem.rem_decorator)
  + [Zero Noise Extrapolation](#zero-noise-extrapolation)
    - [Zero Noise Extrapolation (High-Level Tools)](#module-mitiq.zne.zne)
      * [`combine_results()`](#mitiq.zne.zne.combine_results)
      * [`construct_circuits()`](#mitiq.zne.zne.construct_circuits)
      * [`execute_with_zne()`](#mitiq.zne.zne.execute_with_zne)
      * [`mitigate_executor()`](#mitiq.zne.zne.mitigate_executor)
      * [`zne_decorator()`](#mitiq.zne.zne.zne_decorator)
    - [Inference and Extrapolation: Factories](#module-mitiq.zne.inference)
      * [`AdaExpFactory`](#mitiq.zne.inference.AdaExpFactory)
        + [`AdaExpFactory.extrapolate()`](#mitiq.zne.inference.AdaExpFactory.extrapolate)
        + [`AdaExpFactory.is_converged()`](#mitiq.zne.inference.AdaExpFactory.is_converged)
        + [`AdaExpFactory.next()`](#mitiq.zne.inference.AdaExpFactory.next)
        + [`AdaExpFactory.reduce()`](#mitiq.zne.inference.AdaExpFactory.reduce)
      * [`AdaptiveFactory`](#mitiq.zne.inference.AdaptiveFactory)
        + [`AdaptiveFactory.is_converged()`](#mitiq.zne.inference.AdaptiveFactory.is_converged)
        + [`AdaptiveFactory.next()`](#mitiq.zne.inference.AdaptiveFactory.next)
        + [`AdaptiveFactory.reduce()`](#mitiq.zne.inference.AdaptiveFactory.reduce)
        + [`AdaptiveFactory.run()`](#mitiq.zne.inference.AdaptiveFactory.run)
        + [`AdaptiveFactory.run_classical()`](#mitiq.zne.inference.AdaptiveFactory.run_classical)
      * [`BatchedFactory`](#mitiq.zne.inference.BatchedFactory)
        + [`BatchedFactory.extrapolate()`](#mitiq.zne.inference.BatchedFactory.extrapolate)
        + [`BatchedFactory.reduce()`](#mitiq.zne.inference.BatchedFactory.reduce)
        + [`BatchedFactory.run()`](#mitiq.zne.inference.BatchedFactory.run)
        + [`BatchedFactory.run_classical()`](#mitiq.zne.inference.BatchedFactory.run_classical)
      * [`ConvergenceWarning`](#mitiq.zne.inference.ConvergenceWarning)
      * [`ExpFactory`](#mitiq.zne.inference.ExpFactory)
        + [`ExpFactory.extrapolate()`](#mitiq.zne.inference.ExpFactory.extrapolate)
      * [`ExtrapolationError`](#mitiq.zne.inference.ExtrapolationError)
      * [`ExtrapolationWarning`](#mitiq.zne.inference.ExtrapolationWarning)
      * [`Factory`](#mitiq.zne.inference.Factory)
        + [`Factory.get_expectation_values()`](#mitiq.zne.inference.Factory.get_expectation_values)
        + [`Factory.get_extrapolation_curve()`](#mitiq.zne.inference.Factory.get_extrapolation_curve)
        + [`Factory.get_optimal_parameters()`](#mitiq.zne.inference.Factory.get_optimal_parameters)
        + [`Factory.get_parameters_covariance()`](#mitiq.zne.inference.Factory.get_parameters_covariance)
        + [`Factory.get_scale_factors()`](#mitiq.zne.inference.Factory.get_scale_factors)
        + [`Factory.get_zero_noise_limit()`](#mitiq.zne.inference.Factory.get_zero_noise_limit)
        + [`Factory.get_zero_noise_limit_error()`](#mitiq.zne.inference.Factory.get_zero_noise_limit_error)
        + [`Factory.plot_data()`](#mitiq.zne.inference.Factory.plot_data)
        + [`Factory.plot_fit()`](#mitiq.zne.inference.Factory.plot_fit)
        + [`Factory.push()`](#mitiq.zne.inference.Factory.push)
        + [`Factory.reset()`](#mitiq.zne.inference.Factory.reset)
        + [`Factory.run()`](#mitiq.zne.inference.Factory.run)
        + [`Factory.run_classical()`](#mitiq.zne.inference.Factory.run_classical)
      * [`FakeNodesFactory`](#mitiq.zne.inference.FakeNodesFactory)
        + [`FakeNodesFactory.extrapolate()`](#mitiq.zne.inference.FakeNodesFactory.extrapolate)
      * [`LinearFactory`](#mitiq.zne.inference.LinearFactory)
        + [`LinearFactory.extrapolate()`](#mitiq.zne.inference.LinearFactory.extrapolate)
      * [`PolyExpFactory`](#mitiq.zne.inference.PolyExpFactory)
        + [`PolyExpFactory.extrapolate()`](#mitiq.zne.inference.PolyExpFactory.extrapolate)
      * [`PolyFactory`](#mitiq.zne.inference.PolyFactory)
        + [`PolyFactory.extrapolate()`](#mitiq.zne.inference.PolyFactory.extrapolate)
      * [`RichardsonFactory`](#mitiq.zne.inference.RichardsonFactory)
        + [`RichardsonFactory.extrapolate()`](#mitiq.zne.inference.RichardsonFactory.extrapolate)
      * [`mitiq_curve_fit()`](#mitiq.zne.inference.mitiq_curve_fit)
      * [`mitiq_polyfit()`](#mitiq.zne.inference.mitiq_polyfit)
    - [Noise Scaling: Unitary Folding](#module-mitiq.zne.scaling.folding)
      * [`UnfoldableCircuitError`](#mitiq.zne.scaling.folding.UnfoldableCircuitError)
      * [`fold_all()`](#mitiq.zne.scaling.folding.fold_all)
      * [`fold_gates_at_random()`](#mitiq.zne.scaling.folding.fold_gates_at_random)
      * [`fold_global()`](#mitiq.zne.scaling.folding.fold_global)
    - [Noise Scaling: Identity Insertion Scaling](#module-mitiq.zne.scaling.identity_insertion)
      * [`UnscalableCircuitError`](#mitiq.zne.scaling.identity_insertion.UnscalableCircuitError)
      * [`insert_id_layers()`](#mitiq.zne.scaling.identity_insertion.insert_id_layers)
    - [Noise Scaling: Layerwise Folding](#module-mitiq.zne.scaling.layer_scaling)
      * [`get_layer_folding()`](#mitiq.zne.scaling.layer_scaling.get_layer_folding)
      * [`layer_folding()`](#mitiq.zne.scaling.layer_scaling.layer_folding)
    - [Noise Scaling: Parameter Calibration](#module-mitiq.zne.scaling.parameter)
      * [`CircuitMismatchException`](#mitiq.zne.scaling.parameter.CircuitMismatchException)
      * [`GateTypeException`](#mitiq.zne.scaling.parameter.GateTypeException)
      * [`compute_parameter_variance()`](#mitiq.zne.scaling.parameter.compute_parameter_variance)
      * [`scale_parameters()`](#mitiq.zne.scaling.parameter.scale_parameters)
* [Experimental Techniques](#experimental-techniques)
  + [Classical Shadows](#classical-shadows)
    - [Classical Shadows (High-Level Tools)](#module-mitiq.experimental.shadows.shadows)
      * [`classical_post_processing()`](#mitiq.experimental.shadows.shadows.classical_post_processing)
      * [`pauli_twirling_calibrate()`](#mitiq.experimental.shadows.shadows.pauli_twirling_calibrate)
      * [`shadow_quantum_processing()`](#mitiq.experimental.shadows.shadows.shadow_quantum_processing)
    - [Quantum Processing](#module-mitiq.experimental.shadows.quantum_processing)
      * [`get_rotated_circuits()`](#mitiq.experimental.shadows.quantum_processing.get_rotated_circuits)
      * [`random_pauli_measurement()`](#mitiq.experimental.shadows.quantum_processing.random_pauli_measurement)
      * [`sample_random_pauli_bases()`](#mitiq.experimental.shadows.quantum_processing.sample_random_pauli_bases)
    - [Classical Post-Processing](#module-mitiq.experimental.shadows.classical_postprocessing)
      * [`classical_snapshot()`](#mitiq.experimental.shadows.classical_postprocessing.classical_snapshot)
      * [`expectation_estimation_shadow()`](#mitiq.experimental.shadows.classical_postprocessing.expectation_estimation_shadow)
      * [`get_pauli_fidelities()`](#mitiq.experimental.shadows.classical_postprocessing.get_pauli_fidelities)
      * [`get_single_shot_pauli_fidelity()`](#mitiq.experimental.shadows.classical_postprocessing.get_single_shot_pauli_fidelity)
      * [`shadow_state_reconstruction()`](#mitiq.experimental.shadows.classical_postprocessing.shadow_state_reconstruction)
    - [Utility Functions](#module-mitiq.experimental.shadows.shadows_utils)
      * [`batch_calibration_data()`](#mitiq.experimental.shadows.shadows_utils.batch_calibration_data)
      * [`create_string()`](#mitiq.experimental.shadows.shadows_utils.create_string)
      * [`fidelity()`](#mitiq.experimental.shadows.shadows_utils.fidelity)
      * [`local_clifford_shadow_norm()`](#mitiq.experimental.shadows.shadows_utils.local_clifford_shadow_norm)
      * [`n_measurements_opts_expectation_bound()`](#mitiq.experimental.shadows.shadows_utils.n_measurements_opts_expectation_bound)
      * [`n_measurements_tomography_bound()`](#mitiq.experimental.shadows.shadows_utils.n_measurements_tomography_bound)
      * [`valid_bitstrings()`](#mitiq.experimental.shadows.shadows_utils.valid_bitstrings)
  + [Probabilistic Error Amplification](#probabilistic-error-amplification)
    - [Probabilistic Error Amplification (High-Level Tools)](#module-mitiq.experimental.pea.pea)
      * [`combine_results()`](#mitiq.experimental.pea.pea.combine_results)
      * [`construct_circuits()`](#mitiq.experimental.pea.pea.construct_circuits)
      * [`execute_with_pea()`](#mitiq.experimental.pea.pea.execute_with_pea)
    - [Noise Amplification Utilities](#module-mitiq.experimental.pea.scale_amplifications)
      * [`scale_circuit_amplifications()`](#mitiq.experimental.pea.scale_amplifications.scale_circuit_amplifications)
    - [Depolarizing Amplifications](#module-mitiq.experimental.pea.amplifications.amplify_depolarizing)
      * [`amplify_noisy_op_with_global_depolarizing_noise()`](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_op_with_global_depolarizing_noise)
      * [`amplify_noisy_op_with_local_depolarizing_noise()`](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_op_with_local_depolarizing_noise)
      * [`amplify_noisy_ops_in_circuit_with_global_depolarizing_noise()`](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_ops_in_circuit_with_global_depolarizing_noise)
      * [`amplify_noisy_ops_in_circuit_with_local_depolarizing_noise()`](#mitiq.experimental.pea.amplifications.amplify_depolarizing.amplify_noisy_ops_in_circuit_with_local_depolarizing_noise)
  + [Twirled Readout Error eXtinction](#twirled-readout-error-extinction)
    - [TREX (High-Level Tools)](#module-mitiq.experimental.trex.trex)
      * [`combine_results()`](#mitiq.experimental.trex.trex.combine_results)
      * [`construct_circuits()`](#mitiq.experimental.trex.trex.construct_circuits)
      * [`execute_with_trex()`](#mitiq.experimental.trex.trex.execute_with_trex)
      * [`mitigate_executor()`](#mitiq.experimental.trex.trex.mitigate_executor)
      * [`trex_decorator()`](#mitiq.experimental.trex.trex.trex_decorator)
  + [Virtual Distillation](#module-mitiq.experimental.vd.vd)
    - [`combine_results()`](#mitiq.experimental.vd.vd.combine_results)
    - [`construct_circuits()`](#mitiq.experimental.vd.vd.construct_circuits)
    - [`execute_with_vd()`](#mitiq.experimental.vd.vd.execute_with_vd)
* [Tools For Error Mitigation](#tools-for-error-mitigation)
  + [Benchmarks](#benchmarks)
    - [GHZ Circuits](#module-mitiq.benchmarks.ghz_circuits)
      * [`generate_ghz_circuit()`](#mitiq.benchmarks.ghz_circuits.generate_ghz_circuit)
    - [Mirror Circuits](#module-mitiq.benchmarks.mirror_circuits)
      * [`edge_grab()`](#mitiq.benchmarks.mirror_circuits.edge_grab)
      * [`generate_mirror_circuit()`](#mitiq.benchmarks.mirror_circuits.generate_mirror_circuit)
      * [`random_cliffords()`](#mitiq.benchmarks.mirror_circuits.random_cliffords)
      * [`random_paulis()`](#mitiq.benchmarks.mirror_circuits.random_paulis)
      * [`random_single_cliffords()`](#mitiq.benchmarks.mirror_circuits.random_single_cliffords)
    - [Mirror Quantum Volume Circuits](#module-mitiq.benchmarks.mirror_qv_circuits)
      * [`generate_mirror_qv_circuit()`](#mitiq.benchmarks.mirror_qv_circuits.generate_mirror_qv_circuit)
    - [Quantum Phase Estimation Circuits](#module-mitiq.benchmarks.qpe_circuits)
      * [`generate_qpe_circuit()`](#mitiq.benchmarks.qpe_circuits.generate_qpe_circuit)
    - [Quantum Volume Circuits](#module-mitiq.benchmarks.quantum_volume_circuits)
      * [`compute_heavy_bitstrings()`](#mitiq.benchmarks.quantum_volume_circuits.compute_heavy_bitstrings)
      * [`generate_quantum_volume_circuit()`](#mitiq.benchmarks.quantum_volume_circuits.generate_quantum_volume_circuit)
    - [Randomized Benchmarking Circuits](#module-mitiq.benchmarks.randomized_benchmarking)
      * [`generate_rb_circuits()`](#mitiq.benchmarks.randomized_benchmarking.generate_rb_circuits)
    - [Rotated Randomized Benchmarking Circuits](#module-mitiq.benchmarks.rotated_randomized_benchmarking)
      * [`generate_rotated_rb_circuits()`](#mitiq.benchmarks.rotated_randomized_benchmarking.generate_rotated_rb_circuits)
    - [Randomized Clifford+T Circuits](#module-mitiq.benchmarks.randomized_clifford_t_circuit)
      * [`generate_random_clifford_t_circuit()`](#mitiq.benchmarks.randomized_clifford_t_circuit.generate_random_clifford_t_circuit)
    - [W State Circuits](#module-mitiq.benchmarks.w_state_circuits)
      * [`generate_w_circuit()`](#mitiq.benchmarks.w_state_circuits.generate_w_circuit)
  + [Calibration](#module-mitiq.calibration.calibrator)
    - [`Calibrator`](#mitiq.calibration.calibrator.Calibrator)
      * [`Calibrator.best_strategy()`](#mitiq.calibration.calibrator.Calibrator.best_strategy)
      * [`Calibrator.cirq_executor`](#mitiq.calibration.calibrator.Calibrator.cirq_executor)
      * [`Calibrator.execute_with_mitigation()`](#mitiq.calibration.calibrator.Calibrator.execute_with_mitigation)
      * [`Calibrator.get_cost()`](#mitiq.calibration.calibrator.Calibrator.get_cost)
      * [`Calibrator.ideal_cirq_executor`](#mitiq.calibration.calibrator.Calibrator.ideal_cirq_executor)
      * [`Calibrator.run()`](#mitiq.calibration.calibrator.Calibrator.run)
    - [`ExperimentResults`](#mitiq.calibration.calibrator.ExperimentResults)
      * [`ExperimentResults.add_result()`](#mitiq.calibration.calibrator.ExperimentResults.add_result)
      * [`ExperimentResults.best_strategy_id()`](#mitiq.calibration.calibrator.ExperimentResults.best_strategy_id)
      * [`ExperimentResults.ensure_full()`](#mitiq.calibration.calibrator.ExperimentResults.ensure_full)
      * [`ExperimentResults.is_missing_data()`](#mitiq.calibration.calibrator.ExperimentResults.is_missing_data)
      * [`ExperimentResults.log_results_cartesian()`](#mitiq.calibration.calibrator.ExperimentResults.log_results_cartesian)
      * [`ExperimentResults.log_results_flat()`](#mitiq.calibration.calibrator.ExperimentResults.log_results_flat)
      * [`ExperimentResults.reset_data()`](#mitiq.calibration.calibrator.ExperimentResults.reset_data)
      * [`ExperimentResults.squared_errors()`](#mitiq.calibration.calibrator.ExperimentResults.squared_errors)
    - [`MissingResultsError`](#mitiq.calibration.calibrator.MissingResultsError)
    - [`OutputForm`](#mitiq.calibration.calibrator.OutputForm)
    - [`convert_to_expval_executor()`](#mitiq.calibration.calibrator.convert_to_expval_executor)
    - [`execute_with_mitigation()`](#mitiq.calibration.calibrator.execute_with_mitigation)
    - [`BenchmarkProblem`](#mitiq.calibration.settings.BenchmarkProblem)
      * [`BenchmarkProblem.converted_circuit()`](#mitiq.calibration.settings.BenchmarkProblem.converted_circuit)
      * [`BenchmarkProblem.to_dict()`](#mitiq.calibration.settings.BenchmarkProblem.to_dict)
    - [`MitigationTechnique`](#mitiq.calibration.settings.MitigationTechnique)
    - [`Settings`](#mitiq.calibration.settings.Settings)
      * [`Settings.make_problems()`](#mitiq.calibration.settings.Settings.make_problems)
      * [`Settings.make_strategies()`](#mitiq.calibration.settings.Settings.make_strategies)
    - [`Strategy`](#mitiq.calibration.settings.Strategy)
      * [`Strategy.to_dict()`](#mitiq.calibration.settings.Strategy.to_dict)
  + [Executors](#module-mitiq.executor.executor)
    - [`Executor`](#mitiq.executor.executor.Executor)
      * [`Executor.can_batch`](#mitiq.executor.executor.Executor.can_batch)
      * [`Executor.evaluate()`](#mitiq.executor.executor.Executor.evaluate)
      * [`Executor.run()`](#mitiq.executor.executor.Executor.run)
  + [Observables](#observables)
    - [Observable](#module-mitiq.observable.observable)
      * [`Observable`](#mitiq.observable.observable.Observable)
        + [`Observable.expectation()`](#mitiq.observable.observable.Observable.expectation)
        + [`Observable.from_pauli_string_collections()`](#mitiq.observable.observable.Observable.from_pauli_string_collections)
        + [`Observable.matrix()`](#mitiq.observable.observable.Observable.matrix)
        + [`Observable.measure_in()`](#mitiq.observable.observable.Observable.measure_in)
        + [`Observable.partition()`](#mitiq.observable.observable.Observable.partition)
    - [Pauli Observable](#module-mitiq.observable.pauli)
      * [`PauliString`](#mitiq.observable.pauli.PauliString)
        + [`PauliString.can_be_measured_with()`](#mitiq.observable.pauli.PauliString.can_be_measured_with)
        + [`PauliString.matrix()`](#mitiq.observable.pauli.PauliString.matrix)
        + [`PauliString.spec`](#mitiq.observable.pauli.PauliString.spec)
        + [`PauliString.weight()`](#mitiq.observable.pauli.PauliString.weight)
      * [`PauliStringCollection`](#mitiq.observable.pauli.PauliStringCollection)
  + [Raw](#raw)
    - [Run experiments without error mitigation (raw results)](#module-mitiq.raw.raw)
* [Core Utilities](#core-utilities)
  + [Circuit types and result types](#circuit-types-and-result-types)
    - [`QPROGRAM`](#mitiq.typing.QPROGRAM)
    - [`QuantumResult`](#mitiq.typing.QuantumResult)
    - [`Bitstring`](#mitiq.typing.Bitstring)
    - [`MeasurementResult`](#mitiq.typing.MeasurementResult)
      * [`MeasurementResult.filter_qubits()`](#mitiq.typing.MeasurementResult.filter_qubits)
      * [`MeasurementResult.from_counts()`](#mitiq.typing.MeasurementResult.from_counts)
      * [`MeasurementResult.from_dict()`](#mitiq.typing.MeasurementResult.from_dict)
      * [`MeasurementResult.get_counts()`](#mitiq.typing.MeasurementResult.get_counts)
      * [`MeasurementResult.prob_distribution()`](#mitiq.typing.MeasurementResult.prob_distribution)
      * [`MeasurementResult.to_dict()`](#mitiq.typing.MeasurementResult.to_dict)
  + [Mitiq Interface](#mitiq-interface)
    - [Braket Conversions](#module-mitiq.interface.mitiq_braket.conversions)
      * [`from_braket()`](#mitiq.interface.mitiq_braket.conversions.from_braket)
      * [`to_braket()`](#mitiq.interface.mitiq_braket.conversions.to_braket)
    - [Cirq Utils](#module-mitiq.interface.mitiq_cirq.cirq_utils)
      * [`compute_density_matrix()`](#mitiq.interface.mitiq_cirq.cirq_utils.compute_density_matrix)
      * [`execute_with_depolarizing_noise()`](#mitiq.interface.mitiq_cirq.cirq_utils.execute_with_depolarizing_noise)
      * [`sample_bitstrings()`](#mitiq.interface.mitiq_cirq.cirq_utils.sample_bitstrings)
    - [Pennylane Conversions](#module-mitiq.interface.mitiq_pennylane.conversions)
      * [`UnsupportedQuantumTapeError`](#mitiq.interface.mitiq_pennylane.conversions.UnsupportedQuantumTapeError)
      * [`from_pennylane()`](#mitiq.interface.mitiq_pennylane.conversions.from_pennylane)
      * [`to_pennylane()`](#mitiq.interface.mitiq_pennylane.conversions.to_pennylane)
    - [PyQuil Conversions](#module-mitiq.interface.mitiq_pyquil.conversions)
      * [`from_pyquil()`](#mitiq.interface.mitiq_pyquil.conversions.from_pyquil)
      * [`from_quil()`](#mitiq.interface.mitiq_pyquil.conversions.from_quil)
      * [`to_pyquil()`](#mitiq.interface.mitiq_pyquil.conversions.to_pyquil)
      * [`to_quil()`](#mitiq.interface.mitiq_pyquil.conversions.to_quil)
    - [Qibo Conversions](#qibo-conversions)
      * [`from_qibo()`](#mitiq.interface.mitiq_qibo.conversions.from_qibo)
      * [`to_qibo()`](#mitiq.interface.mitiq_qibo.conversions.to_qibo)
    - [Qiskit Conversions](#module-mitiq.interface.mitiq_qiskit.conversions)
      * [`from_qasm()`](#mitiq.interface.mitiq_qiskit.conversions.from_qasm)
      * [`from_qiskit()`](#mitiq.interface.mitiq_qiskit.conversions.from_qiskit)
      * [`to_qasm()`](#mitiq.interface.mitiq_qiskit.conversions.to_qasm)
      * [`to_qiskit()`](#mitiq.interface.mitiq_qiskit.conversions.to_qiskit)
    - [Qiskit Utils](#module-mitiq.interface.mitiq_qiskit.qiskit_utils)
      * [`compute_expectation_value_on_noisy_backend()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.compute_expectation_value_on_noisy_backend)
      * [`execute()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute)
      * [`execute_with_noise()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute_with_noise)
      * [`execute_with_shots()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute_with_shots)
      * [`execute_with_shots_and_noise()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.execute_with_shots_and_noise)
      * [`initialized_depolarizing_noise()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.initialized_depolarizing_noise)
      * [`sample_bitstrings()`](#mitiq.interface.mitiq_qiskit.qiskit_utils.sample_bitstrings)
    - [OpenQASM Conversions](#module-mitiq.interface.mitiq_openqasm.conversions)
      * [`from_openqasm()`](#mitiq.interface.mitiq_openqasm.conversions.from_openqasm)
      * [`to_openqasm()`](#mitiq.interface.mitiq_openqasm.conversions.to_openqasm)

### This Page

* [Show Source](_sources/apidoc.md.txt)

© Copyright 2020 - 2026 Unitary Foundation.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1.