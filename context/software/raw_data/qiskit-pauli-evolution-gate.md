[Skip to main content](#main-content)

[IBM Quantum Platform](/)

* [Home](/)
* [Instances](/instances)
* [Workloads](/workloads?user=me)
* [Compute resources](/computers)
* [Functions

  Preview](/functions)
* ---
* [Documentation](/docs/guides)
* [Tutorials](/docs/tutorials)
* [API references](/docs/api)
* ---
* [Learning](/learning)
* [Composer](/composer)

* [Documentation](/docs/guides)
* [Tutorials](/docs/tutorials)
* API references

##

# PauliEvolutionGate

*class* `qiskit.circuit.library.PauliEvolutionGate(operator, time=1.0, label=None, synthesis=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/library/pauli_evolution.py#L31-L332 "view source code")

Bases: [`Gate`](/docs/api/qiskit/qiskit.circuit.Gate "qiskit.circuit.gate.Gate")

Time-evolution of an operator consisting of Paulis.

For an Hermitian operator HHH consisting of Pauli terms and (real) evolution time ttt this gate represents the unitary

U(t)=e−itH.U(t) = e^{-itH}.U(t)=e−itH.

The evolution gates are related to the Pauli rotation gates by a factor of 2. For example the time evolution of the Pauli XXX operator is connected to the Pauli XXX rotation RXR\_XRX​ by

U(t)=e−itX=RX(2t).U(t) = e^{-itX} = R\_X(2t).U(t)=e−itX=RX​(2t).

Compilation:

This gate represents the exact evolution U(t)U(t)U(t). Implementing this operation exactly, however, generally requires an exponential number of gates. The compiler therefore typically implements an *approximation* of the unitary U(t)U(t)U(t), e.g. using a product formula such as defined by [`LieTrotter`](/docs/api/qiskit/qiskit.synthesis.LieTrotter "qiskit.synthesis.LieTrotter"). By passing the `synthesis` argument, you can specify which method the compiler should use, see [`qiskit.synthesis`](/docs/api/qiskit/synthesis#module-qiskit.synthesis "qiskit.synthesis") for the available options.

Note that the order in which the approximation and methods like [`control()`](#qiskit.circuit.library.PauliEvolutionGate.control "qiskit.circuit.library.PauliEvolutionGate.control") and [`power()`](#qiskit.circuit.library.PauliEvolutionGate.power "qiskit.circuit.library.PauliEvolutionGate.power") are called matters. Changing the order can lead to different unitaries.

Commutation checks:

Qiskit supports efficient commutation checks of [`PauliEvolutionGate`](#qiskit.circuit.library.PauliEvolutionGate "qiskit.circuit.library.PauliEvolutionGate") instances with other Pauli-based gates, such as [`PauliGate`](/docs/api/qiskit/qiskit.circuit.library.PauliGate "qiskit.circuit.library.PauliGate") or [`PauliProductMeasurement`](/docs/api/qiskit/qiskit.circuit.library.PauliProductMeasurement "qiskit.circuit.library.PauliProductMeasurement"). However, these checks require conversion of the operator into [`SparseObservable`](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable") format, hence we strongly suggest to build operators using this operator class if a large number of commutation checks are expected (e.g. if you have a circuit with a large number of sequential [`PauliEvolutionGate`](#qiskit.circuit.library.PauliEvolutionGate "qiskit.circuit.library.PauliEvolutionGate")s).

Examples:

```
from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import SparsePauliOp

X = SparsePauliOp("X")
Z = SparsePauliOp("Z")
I = SparsePauliOp("I")

# build the evolution gate
operator = (Z ^ Z) - 0.1 * (X ^ I)
evo = PauliEvolutionGate(operator, time=0.2)

# plug it into a circuit
circuit = QuantumCircuit(2)
circuit.append(evo, range(2))
print(circuit.draw())
```

The above will print (note that the `-0.1` coefficient is not printed!):

```
     ┌──────────────────────────┐
q_0: ┤0                         ├
     │  exp(-it (ZZ + XI))(0.2) │
q_1: ┤1                         ├
     └──────────────────────────┘
```

References:

[1] G. Li et al. Paulihedral: A Generalized Block-Wise Compiler Optimization Framework For Quantum Simulation Kernels (2021). [arXiv:2109.03371](https://arxiv.org/abs/2109.03371)

**Parameters**

* **operator** ([*qiskit.quantum\_info.Pauli*](/docs/api/qiskit/qiskit.quantum_info.Pauli "qiskit.quantum_info.Pauli") *|*[*SparsePauliOp*](/docs/api/qiskit/qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") *|*[*SparseObservable*](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable") *|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*qiskit.quantum\_info.Pauli*](/docs/api/qiskit/qiskit.quantum_info.Pauli "qiskit.quantum_info.Pauli") *|*[*SparsePauliOp*](/docs/api/qiskit/qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") *|*[*SparseObservable*](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable")*]*) – The operator to evolve. Can also be provided as list of non-commuting operators where the elements are sums of commuting operators. For example: `[XY + YX, ZZ + ZI + IZ, YY]`.
* **time** (*ParameterValueType*) – The evolution time.
* **label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *| None*) – A label for the gate to display in visualizations. Per default, the label is set to `exp(-it <operators>)` where `<operators>` is the sum of the Paulis. Note that the label does not include any coefficients of the Paulis. See the class docstring for an example.
* **synthesis** ([*EvolutionSynthesis*](/docs/api/qiskit/qiskit.synthesis.EvolutionSynthesis "qiskit.synthesis.EvolutionSynthesis") *| None*) – A synthesis strategy. If None, the default synthesis is the Lie-Trotter product formula with a single repetition.

---

## Attributes

### base\_class

Get the base class of this instruction. This is guaranteed to be in the inheritance tree of `self`.

The “base class” of an instruction is the lowest class in its inheritance tree that the object should be considered entirely compatible with for \_all\_ circuit applications. This typically means that the subclass is defined purely to offer some sort of programmer convenience over the base class, and the base class is the “true” class for a behavioral perspective. In particular, you should *not* override [`base_class`](#qiskit.circuit.library.PauliEvolutionGate.base_class "qiskit.circuit.library.PauliEvolutionGate.base_class") if you are defining a custom version of an instruction that will be implemented differently by hardware, such as an alternative measurement strategy, or a version of a parametrized gate with a particular set of parameters for the purposes of distinguishing it in a [`Target`](/docs/api/qiskit/qiskit.transpiler.Target "qiskit.transpiler.Target") from the full parametrized gate.

This is often exactly equivalent to `type(obj)`, except in the case of singleton instances of standard-library instructions. These singleton instances are special subclasses of their base class, and this property will return that base. For example:

```
>>> isinstance(XGate(), XGate)
True
>>> type(XGate()) is XGate
False
>>> XGate().base_class is XGate
True
```

In general, you should not rely on the precise class of an instruction; within a given circuit, it is expected that `Instruction.name` should be a more suitable discriminator in most situations.

### decompositions

Get the decompositions of the instruction from the SessionEquivalenceLibrary.

### definition

Return definition in terms of other basic gates.

### label

Return instruction label

### mutable

Is this instance is a mutable unique instance or not.

If this attribute is `False` the gate instance is a shared singleton and is not mutable.

### name

Return the name.

### num\_clbits

Return the number of clbits.

### num\_qubits

Return the number of qubits.

### params

The parameters of this `Instruction`. Ideally these will be gate angles.

### time

Return the evolution time as stored in the gate parameters.

**Returns**

The evolution time.

---

## Methods

### add\_decomposition

`add_decomposition(decomposition)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L318-L323 "view source code")

Add a decomposition of the instruction to the SessionEquivalenceLibrary.

### broadcast\_arguments

`broadcast_arguments(qargs, cargs)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/gate.py#L206-L263 "view source code")

Validation and handling of the arguments and its relationship.

For example, `cx([q[0],q[1]], q[2])` means `cx(q[0], q[2]); cx(q[1], q[2])`. This method yields the arguments in the right grouping. In the given example:

```
in: [[q[0],q[1]], q[2]],[]
outs: [q[0], q[2]], []
      [q[1], q[2]], []
```

The general broadcasting rules are:

> * If len(qargs) == 1:
>
>   ```
>   [q[0], q[1]] -> [q[0]],[q[1]]
>   ```
> * If len(qargs) == 2:
>
>   ```
>   [[q[0], q[1]], [r[0], r[1]]] -> [q[0], r[0]], [q[1], r[1]]
>   [[q[0]], [r[0], r[1]]]       -> [q[0], r[0]], [q[0], r[1]]
>   [[q[0], q[1]], [r[0]]]       -> [q[0], r[0]], [q[1], r[0]]
>   ```
> * If len(qargs) >= 3:
>
>   ```
>   [q[0], q[1]], [r[0], r[1]],  ...] -> [q[0], r[0], ...], [q[1], r[1], ...]
>   ```

**Parameters**

* **qargs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – List of quantum bit arguments.
* **cargs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – List of classical bit arguments.

**Returns**

A tuple with single arguments.

**Raises**

[**CircuitError**](/docs/api/qiskit/circuit#qiskit.circuit.CircuitError "qiskit.circuit.CircuitError") – If the input is not valid. For example, the number of arguments does not match the gate expectation.

**Return type**

[*Iterable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list), [list](https://docs.python.org/3/library/stdtypes.html#list)]]

### control

`control(num_ctrl_qubits=1, label=None, ctrl_state=None, annotated=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/library/pauli_evolution.py#L248-L309 "view source code")

Return the controlled version of itself.

The outcome is the specified controlled version of e−itHe^{-itH}e−itH. The returned gate represents e−itHCe^{-it H\_C}e−itHC​, where HCH\_CHC​ is the original operator HHH, tensored with ∣0⟩⟨0∣|0\rangle\langle 0|∣0⟩⟨0∣ and ∣1⟩⟨1∣|1\rangle\langle 1|∣1⟩⟨1∣ projectors (depending on the control state).

The controlled gate is implemented as [`PauliEvolutionGate`](#qiskit.circuit.library.PauliEvolutionGate "qiskit.circuit.library.PauliEvolutionGate"), regardless of the value of `annotated`.

**Parameters**

* **num\_ctrl\_qubits** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of controls to add. Defaults to `1`.
* **label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *| None*) – A label for the resulting Pauli evolution gate, to display in visualizations. Per default, the label is set to `exp(-it <operators>)` where `<operators>` is the sum of the Paulis. Note that the label does not include any coefficients of the Paulis. See the class docstring for an example.
* **ctrl\_state** ([*int*](https://docs.python.org/3/library/functions.html#int) *|*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *| None*) – The control state of the gate, specified either as an integer or a bitstring (e.g. `"110"`). If `None`, defaults to the all-ones state `2**num_ctrl_qubits - 1`.
* **annotated** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *| None*) – Ignored.

**Returns**

A controlled version of this gate.

**Return type**

[*Gate*](/docs/api/qiskit/qiskit.circuit.Gate "qiskit.circuit.gate.Gate")

### copy

`copy(name=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L428-L443 "view source code")

Copy of the instruction.

**Parameters**

**name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name to be given to the copied circuit, if `None` then the name stays the same.

**Returns**

a copy of the current instruction, with the name updated if it was provided

**Return type**

[qiskit.circuit.Instruction](/docs/api/qiskit/qiskit.circuit.Instruction "qiskit.circuit.Instruction")

### inverse

`inverse(annotated=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/library/pauli_evolution.py#L224-L226 "view source code")

Return the inverse, which is obtained by flipping the sign of the evolution time.

**Parameters**

**annotated** ([*bool*](https://docs.python.org/3/library/functions.html#bool))

### is\_parameterized

`is_parameterized()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L283-L288 "view source code")

Return whether the `Instruction` contains [compile-time parameters](/docs/api/qiskit/circuit#circuit-compile-time-parameters).

### power

`power(exponent, annotated=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/library/pauli_evolution.py#L228-L243 "view source code")

Raise this gate to the power of `exponent`.

The outcome represents e−itpHe^{-i tp H}e−itpH where ppp equals `exponent`.

**Parameters**

* **exponent** ([*float*](https://docs.python.org/3/library/functions.html#float)) – The power to raise the gate to.
* **annotated** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Not applicable to this class. Usually, when this is `True` we return an [`AnnotatedOperation`](/docs/api/qiskit/qiskit.circuit.AnnotatedOperation "qiskit.circuit.AnnotatedOperation") with a power modifier set instead of a concrete [`Gate`](/docs/api/qiskit/qiskit.circuit.Gate "qiskit.circuit.Gate"). However, we can efficiently represent powers of Pauli evolutions as [`PauliEvolutionGate`](#qiskit.circuit.library.PauliEvolutionGate "qiskit.circuit.library.PauliEvolutionGate"), which is used here.

**Returns**

An operation implementing `gate^exponent`.

**Return type**

[*Gate*](/docs/api/qiskit/qiskit.circuit.Gate "qiskit.circuit.gate.Gate")

### repeat

`repeat(n)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L491-L521 "view source code")

Creates an instruction with `self` repeated nnn times.

**Parameters**

**n** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of times to repeat the instruction

**Returns**

Containing the definition.

**Return type**

[qiskit.circuit.Instruction](/docs/api/qiskit/qiskit.circuit.Instruction "qiskit.circuit.Instruction")

**Raises**

[**CircuitError**](/docs/api/qiskit/circuit#qiskit.circuit.CircuitError "qiskit.circuit.CircuitError") – If n < 1.

### reverse\_ops

`reverse_ops()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L345-L369 "view source code")

For a composite instruction, reverse the order of sub-instructions.

This is done by recursively reversing all sub-instructions. It does not invert any gate.

**Returns**

**a new instruction with**

sub-instructions reversed.

**Return type**

[qiskit.circuit.Instruction](/docs/api/qiskit/qiskit.circuit.Instruction "qiskit.circuit.Instruction")

### soft\_compare

`soft_compare(other)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L214-L254 "view source code")

Soft comparison between gates. Their names, number of qubits, and classical bit numbers must match. The number of parameters must match. Each parameter is compared. If one is a ParameterExpression then it is not taken into account.

**Parameters**

**other** (*instruction*) – other instruction.

**Returns**

are self and other equal up to parameter expressions.

**Return type**

[bool](https://docs.python.org/3/library/functions.html#bool)

### to\_matrix

`to_matrix()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/library/pauli_evolution.py#L185-L222 "view source code")

Return the matrix e−itHe^{-it H}e−itH as `numpy.ndarray`.

**Returns**

The matrix this gate represents.

**Raises**

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) – If the `time` parameters is not numeric.

**Return type**

[*ndarray*](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)

### to\_mutable

`to_mutable()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/instruction.py#L144-L152 "view source code")

Return a mutable copy of this gate.

This method will return a new mutable copy of this gate instance. If a singleton instance is being used this will be a new unique instance that can be mutated. If the instance is already mutable it will be a deepcopy of that instance.

### validate\_parameter

`validate_parameter(parameter)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/circuit/library/pauli_evolution.py#L315-L320 "view source code")

Gate parameters should be int, float, or ParameterExpression

**Parameters**

**parameter** ([*ParameterExpression*](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit._accelerate.circuit.ParameterExpression") *|*[*float*](https://docs.python.org/3/library/functions.html#float))

**Return type**

[*ParameterExpression*](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit._accelerate.circuit.ParameterExpression") | [float](https://docs.python.org/3/library/functions.html#float)

Was this page helpful?

YesNo

Report a bug, typo, or request content on [GitHub](https://github.com/Qiskit/documentation/issues/new/choose).

On this page

* [PauliEvolutionGate](#paulievolutiongate)
* [Attributes](#attributes)
* [base\_class](#base_class)
* [decompositions](#decompositions)
* [definition](#definition)
* [label](#label)
* [mutable](#mutable)
* [name](#name)
* [num\_clbits](#num_clbits)
* [num\_qubits](#num_qubits)
* [params](#params)
* [time](#time)
* [Methods](#methods)
* [add\_decomposition](#add_decomposition)
* [broadcast\_arguments](#broadcast_arguments)
* [control](#control)
* [copy](#copy)
* [inverse](#inverse)
* [is\_parameterized](#is_parameterized)
* [power](#power)
* [repeat](#repeat)
* [reverse\_ops](#reverse_ops)
* [soft\_compare](#soft_compare)
* [to\_matrix](#to_matrix)
* [to\_mutable](#to_mutable)
* [validate\_parameter](#validate_parameter)

Was this page helpful?

YesNo

Report a bug, typo, or request content on [GitHub](https://github.com/Qiskit/documentation/issues/new/choose).

© IBM Corp., 2017-2026

s

* [Terms](https://www.ibm.com/us-en/legal/terms)
* [Privacy](https://www.ibm.com/us-en/privacy)
* Cookie preferences
* [Support](/docs/guides/support)
* [Accessibility](/docs/accessibility)
* [Security](/docs/guides/secure-data)

English

English

Open menu

Light themeSystem preferenceDark theme

Open search dialog

Search