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

# SparsePauliOp

*class* `qiskit.quantum_info.SparsePauliOp(data, coeffs=None, *, ignore_pauli_phase=False, copy=True)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L51-L1255 "view source code")

Bases: `LinearOp`

Sparse N-qubit operator in a Pauli basis representation.

This is a sparse representation of an N-qubit matrix [`Operator`](/docs/api/qiskit/qiskit.quantum_info.Operator "qiskit.quantum_info.Operator") in terms of N-qubit [`PauliList`](/docs/api/qiskit/qiskit.quantum_info.PauliList "qiskit.quantum_info.PauliList") and complex coefficients.

It can be used for performing operator arithmetic for hundreds of qubits if the number of non-zero Pauli basis terms is sufficiently small.

The Pauli basis components are stored as a [`PauliList`](/docs/api/qiskit/qiskit.quantum_info.PauliList "qiskit.quantum_info.PauliList") object and can be accessed using the [`paulis`](#qiskit.quantum_info.SparsePauliOp.paulis "qiskit.quantum_info.SparsePauliOp.paulis") attribute. The coefficients are stored as a complex Numpy array vector and can be accessed using the [`coeffs`](#qiskit.quantum_info.SparsePauliOp.coeffs "qiskit.quantum_info.SparsePauliOp.coeffs") attribute.

**Data type of coefficients**

The default `dtype` of the internal `coeffs` Numpy array is `complex128`. Users can configure this by passing `np.ndarray` with a different dtype. For example, a parameterized [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") can be made as follows:

```
>>> import numpy as np
>>> from qiskit.circuit import ParameterVector
>>> from qiskit.quantum_info import SparsePauliOp
```

```
>>> SparsePauliOp(["II", "XZ"], np.array(ParameterVector("a", 2)))
SparsePauliOp(['II', 'XZ'],
      coeffs=[ParameterExpression(1.0*a[0]), ParameterExpression(1.0*a[1])])
```

Note

Parameterized [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") does not support the following methods:

* `to_matrix(sparse=True)` since `scipy.sparse` cannot have objects as elements.
* `to_operator()` since [`Operator`](/docs/api/qiskit/qiskit.quantum_info.Operator "qiskit.quantum_info.Operator") does not support objects.
* `sort`, `argsort` since [`ParameterExpression`](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit.circuit.ParameterExpression") does not support comparison.
* `equiv` since [`ParameterExpression`](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit.circuit.ParameterExpression") cannot be converted into complex.
* `chop` since [`ParameterExpression`](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit.circuit.ParameterExpression") does not support absolute value.

Initialize an operator object.

**Parameters**

* **data** ([*PauliList*](/docs/api/qiskit/qiskit.quantum_info.PauliList "qiskit.quantum_info.PauliList") *or*[*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") *or*[*Pauli*](/docs/api/qiskit/qiskit.quantum_info.Pauli "qiskit.quantum_info.Pauli") *or*[*list*](https://docs.python.org/3/library/stdtypes.html#list) *or*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Pauli list of terms. A list of Pauli strings or a Pauli string is also allowed.
* **coeffs** (*np.ndarray*) –

  complex coefficients for Pauli terms.

  Note

  If `data` is a [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") and `coeffs` is not `None`, the value of the `SparsePauliOp.coeffs` will be ignored, and only the passed keyword argument `coeffs` will be used.
* **ignore\_pauli\_phase** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, any `phase` component of a given [`PauliList`](/docs/api/qiskit/qiskit.quantum_info.PauliList "qiskit.quantum_info.PauliList") will be assumed to be zero. This is more efficient in cases where a [`PauliList`](/docs/api/qiskit/qiskit.quantum_info.PauliList "qiskit.quantum_info.PauliList") has been constructed purely for this object, and it is already known that the phases in the ZX-convention are zero. It only makes sense to pass this option when giving [`PauliList`](/docs/api/qiskit/qiskit.quantum_info.PauliList "qiskit.quantum_info.PauliList") data. (Default: False)
* **copy** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – copy the input data if True, otherwise assign it directly, if possible. (Default: True)

**Raises**

[**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – If the input data or coeffs are invalid.

---

## Attributes

### atol

Default value: `1e-08`

### coeffs

Return the Pauli coefficients.

### dim

Return tuple (input\_shape, output\_shape).

### num\_qubits

Return the number of qubits if a N-qubit operator or None otherwise.

### parameters

Return the free `Parameter`s in the coefficients.

### paulis

Return the PauliList.

### qargs

Return the qargs for the operator.

### rtol

Default value: `1e-05`

### settings

Return settings.

### size

The number of Pauli of Pauli terms in the operator.

---

## Methods

### adjoint

`adjoint()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L323-L328 "view source code")

Return the adjoint of the Operator.

### apply\_layout

`apply_layout(layout, num_qubits=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1210-L1255 "view source code")

Apply a transpiler layout to this [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

**Parameters**

* **layout** ([*TranspileLayout*](/docs/api/qiskit/qiskit.transpiler.TranspileLayout "qiskit.transpiler.TranspileLayout") *|*[*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*] | None*) – Either a [`TranspileLayout`](/docs/api/qiskit/qiskit.transpiler.TranspileLayout "qiskit.transpiler.TranspileLayout"), a list of integers or None. If both layout and num\_qubits are none, a copy of the operator is returned.
* **num\_qubits** ([*int*](https://docs.python.org/3/library/functions.html#int) *| None*) – The number of qubits to expand the operator to. If not provided then if `layout` is a [`TranspileLayout`](/docs/api/qiskit/qiskit.transpiler.TranspileLayout "qiskit.transpiler.TranspileLayout") the number of the transpiler output circuit qubits will be used by default. If `layout` is a list of integers the permutation specified will be applied without any expansion. If layout is None, the operator will be expanded to the given number of qubits.

**Returns**

A new [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") with the provided layout applied

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

### argsort

`argsort(weight=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L534-L602 "view source code")

Return indices for sorting the rows of the table.

Returns the composition of permutations in the order of sorting by coefficient and sorting by Pauli. By using the weight kwarg the output can additionally be sorted by the number of non-identity terms in the Pauli, where the set of all Pauli’s of a given weight are still ordered lexicographically.

**Example**

Here is an example of how to use SparsePauliOp argsort.

```
import numpy as np
from qiskit.quantum_info import SparsePauliOp

# 2-qubit labels
labels = ["XX", "XX", "XX", "YI", "II", "XZ", "XY", "XI"]
# coeffs
coeffs = [2.+1.j, 2.+2.j, 3.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j, 7.+0.j]

# init
spo = SparsePauliOp(labels, coeffs)
print('Initial Ordering')
print(spo)

# Lexicographic Ordering
srt = spo.argsort()
print('Lexicographically sorted')
print(srt)

# Lexicographic Ordering
srt = spo.argsort(weight=False)
print('Lexicographically sorted')
print(srt)

# Weight Ordering
srt = spo.argsort(weight=True)
print('Weight sorted')
print(srt)
```

```
Initial Ordering
SparsePauliOp(['XX', 'XX', 'XX', 'YI', 'II', 'XZ', 'XY', 'XI'],
              coeffs=[2.+1.j, 2.+2.j, 3.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j, 7.+0.j])
Lexicographically sorted
[4 7 0 1 2 6 5 3]
Lexicographically sorted
[4 7 0 1 2 6 5 3]
Weight sorted
[4 7 3 0 1 2 6 5]
```

**Parameters**

* **weight** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optionally sort by weight if True (Default: False).
* **sorted** (*By using the weight kwarg the output can additionally be*)
* **Pauli.** (*by the number of non-identity terms in the*)

**Returns**

the indices for sorting the table.

**Return type**

[array](/docs/api/qiskit/qiskit.primitives.BitArray#array "qiskit.primitives.BitArray.array")

### assign\_parameters

`assign_parameters(parameters, inplace=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1156-L1208 "view source code")

Bind the free `Parameter`s in the coefficients to provided values.

Note

If all the parameters in the circuit are bound to numeric values, the coefficients array will be returned with a [`complex`](https://docs.python.org/3/library/functions.html#complex) dtype.

**Parameters**

* **parameters** ([*Mapping*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)*[*[*Parameter*](/docs/api/qiskit/qiskit.circuit.Parameter "qiskit._accelerate.circuit.Parameter")*,* [*complex*](https://docs.python.org/3/library/functions.html#complex) *|*[*ParameterExpression*](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit._accelerate.circuit.ParameterExpression")*] |* [*Sequence*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)*[*[*complex*](https://docs.python.org/3/library/functions.html#complex) *|*[*ParameterExpression*](/docs/api/qiskit/qiskit.circuit.ParameterExpression "qiskit._accelerate.circuit.ParameterExpression")*]*) – The values to bind the parameters to.
* **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If `False`, a copy of the operator with the bound parameters is returned. If `True` the operator itself is modified.

**Returns**

A copy of the operator with bound parameters, if `inplace` is `False`, otherwise `None`.

**Return type**

[*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.operators.symplectic.sparse_pauli_op.SparsePauliOp") | None

### chop

`chop(tol=1e-14)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L676-L714 "view source code")

Set real and imaginary parts of the coefficients to 0 if `< tol` in magnitude.

For example, the operator representing `1+1e-17j X + 1e-17 Y` with a tolerance larger than `1e-17` will be reduced to `1 X` whereas [`SparsePauliOp.simplify()`](#qiskit.quantum_info.SparsePauliOp.simplify "qiskit.quantum_info.SparsePauliOp.simplify") would return `1+1e-17j X`.

If both the real and imaginary part of a coefficient is 0 after chopping, the corresponding Pauli is removed from the operator.

**Parameters**

**tol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – The absolute tolerance to check whether a real or imaginary part should be set to 0.

**Returns**

This operator with chopped coefficients.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

### compose

`compose(other, qargs=None, front=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L330-L381 "view source code")

Return the operator composition with another SparsePauliOp.

**Parameters**

* **other** ([*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")) – a SparsePauliOp object.
* **qargs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *or None*) – a list of subsystem positions to apply other on. If None apply on all subsystems (default: None).
* **front** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If True compose using right operator multiplication, instead of left multiplication [default: False].

**Returns**

The composed SparsePauliOp.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

**Raises**

[**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if other cannot be converted to an operator, or has incompatible dimensions for specified subsystems.

Note

Composition (`&`) by default is defined as left matrix multiplication for matrix operators, while `@` (equivalent to [`dot()`](#qiskit.quantum_info.SparsePauliOp.dot "qiskit.quantum_info.SparsePauliOp.dot")) is defined as right matrix multiplication. That is that `A & B == A.compose(B)` is equivalent to `B @ A == B.dot(A)` when `A` and `B` are of the same type.

Setting the `front=True` kwarg changes this to right matrix multiplication and is equivalent to the [`dot()`](#qiskit.quantum_info.SparsePauliOp.dot "qiskit.quantum_info.SparsePauliOp.dot") method `A.dot(B) == A.compose(B, front=True)`.

### conjugate

`conjugate()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L305-L312 "view source code")

Return the conjugate of the SparsePauliOp.

### copy

`copy()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/base_operator.py#L143-L145 "view source code")

Make a deep copy of current operator.

### dot

`dot(other, qargs=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/mixins/group.py#L136-L152 "view source code")

Return the right multiplied operator self \* other.

**Parameters**

* **other** ([*Operator*](/docs/api/qiskit/qiskit.quantum_info.Operator "qiskit.quantum_info.Operator")) – an operator object.
* **qargs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list) *or None*) – a list of subsystem positions to apply other on. If None apply on all subsystems (default: None).

**Returns**

The right matrix multiplied Operator.

**Return type**

[Operator](/docs/api/qiskit/qiskit.quantum_info.Operator "qiskit.quantum_info.Operator")

Note

The dot product can be obtained using the `@` binary operator. Hence `a.dot(b)` is equivalent to `a @ b`.

### equiv

`equiv(other, atol=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L220-L234 "view source code")

Check if two SparsePauliOp operators are equivalent.

**Parameters**

* **other** ([*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")) – an operator object.
* **atol** ([*float*](https://docs.python.org/3/library/functions.html#float) *| None*) – Absolute numerical tolerance for checking equivalence.

**Returns**

True if the operator is equivalent to `self`.

**Return type**

[bool](https://docs.python.org/3/library/functions.html#bool)

### expand

`expand(other)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L388-L391 "view source code")

Return the reverse-order tensor product with another SparsePauliOp.

**Parameters**

**other** ([*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")) – a SparsePauliOp object.

**Returns**

**the tensor product b⊗ab \otimes ab⊗a, where aaa**

is the current SparsePauliOp, and bbb is the other SparsePauliOp.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

### from\_list

*static* `from_list(obj, dtype=None, *, num_qubits=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L799-L869 "view source code")

Construct from a list of Pauli strings and coefficients.

For example, the 5-qubit Hamiltonian

H=Z1X4+2Y0Y3H = Z\_1 X\_4 + 2 Y\_0 Y\_3H=Z1​X4​+2Y0​Y3​

can be constructed as

```
from qiskit.quantum_info import SparsePauliOp

# via tuples and the full Pauli string
op = SparsePauliOp.from_list([("XIIZI", 1), ("IYIIY", 2)])
```

**Parameters**

* **obj** (*Iterable[Tuple[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*complex*](https://docs.python.org/3/library/functions.html#complex)*]]*) – The list of 2-tuples specifying the Pauli terms.
* **dtype** ([*type*](/docs/api/qiskit/qiskit.dagcircuit.DAGDepNode#type "qiskit.dagcircuit.DAGDepNode.type") *| None*) – Data type for the coefficients. If `None` (default), the dtype is automatically inferred.
* **num\_qubits** ([*int*](https://docs.python.org/3/library/functions.html#int)) – The number of qubits of the operator (Default: None).

**Returns**

The SparsePauliOp representation of the Pauli terms.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

**Raises**

* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – If an empty list is passed and num\_qubits is None.
* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – If num\_qubits and the objects in the input list do not match.

### from\_operator

*static* `from_operator(obj, atol=None, rtol=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L752-L797 "view source code")

Construct from an Operator object.

Note that the cost of this construction is exponential in general because the number of possible Pauli terms in the decomposition is exponential in the number of qubits.

Internally this uses an implementation of the “tensorized Pauli decomposition” presented in [Hantzko, Binkowski and Gupta (2023)](https://arxiv.org/abs/2310.13421).

**Parameters**

* **obj** ([*Operator*](/docs/api/qiskit/qiskit.quantum_info.Operator "qiskit.quantum_info.Operator")) – an N-qubit operator.
* **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Optional. Absolute tolerance for checking if coefficients are zero (Default: 1e-8). Since the comparison is to zero, in effect the tolerance used is the maximum of `atol` and `rtol`.
* **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Optional. relative tolerance for checking if coefficients are zero (Default: 1e-5). Since the comparison is to zero, in effect the tolerance used is the maximum of `atol` and `rtol`.

**Returns**

the SparsePauliOp representation of the operator.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

**Raises**

[**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if the input operator is not an N-qubit operator.

### from\_sparse\_list

*static* `from_sparse_list(obj, num_qubits, do_checks=True, dtype=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L871-L950 "view source code")

Construct from a list of local Pauli strings and coefficients.

Each list element is a 3-tuple of a local Pauli string, indices where to apply it, and a coefficient.

For example, the 5-qubit Hamiltonian

H=Z1X4+2Y0Y3H = Z\_1 X\_4 + 2 Y\_0 Y\_3H=Z1​X4​+2Y0​Y3​

can be constructed as

```
from qiskit.quantum_info import SparsePauliOp

# via triples and local Paulis with indices
op = SparsePauliOp.from_sparse_list([("ZX", [1, 4], 1), ("YY", [0, 3], 2)], num_qubits=5)

# equals the following construction from "dense" Paulis
op = SparsePauliOp.from_list([("XIIZI", 1), ("IYIIY", 2)])
```

**Parameters**

* **obj** (*Iterable[*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*],* [*complex*](https://docs.python.org/3/library/functions.html#complex)*]]*) – The list 3-tuples specifying the Paulis.
* **num\_qubits** ([*int*](https://docs.python.org/3/library/functions.html#int)) – The number of qubits of the operator.
* **do\_checks** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Whether to perform validity checks on the input indices.
* **dtype** ([*type*](/docs/api/qiskit/qiskit.dagcircuit.DAGDepNode#type "qiskit.dagcircuit.DAGDepNode.type") *| None*) – Data type for the coefficients. If `None` (default), the dtype is automatically inferred.

**Returns**

The SparsePauliOp representation of the Pauli terms.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

**Raises**

* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – If the number of qubits is incompatible with the indices of the Pauli terms.
* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – If the designated qubit is already assigned.

### from\_sparse\_observable

*static* `from_sparse_observable(obs)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L952-L971 "view source code")

Initialize from a [`SparseObservable`](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable").

Warning

A [`SparseObservable`](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable") can efficiently represent eigenstate projectors (such as ∣0⟨⟩0∣|0\langle\rangle 0|∣0⟨⟩0∣), but a [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") **cannot**. If the input `obs` has nnn single-qubit projectors, the resulting [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") will use 2n2^n2n terms, which is an exponentially expensive representation that can quickly run out of memory.

**Parameters**

**obs** ([*SparseObservable*](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable")) – The [`SparseObservable`](/docs/api/qiskit/qiskit.quantum_info.SparseObservable "qiskit.quantum_info.SparseObservable") to convert.

**Returns**

A [`SparsePauliOp`](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp") version of the observable.

**Return type**

[*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.operators.symplectic.sparse_pauli_op.SparsePauliOp")

### group\_commuting

`group_commuting(qubit_wise=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1119-L1145 "view source code")

Partition a SparsePauliOp into sets of commuting Pauli strings.

**Parameters**

**qubit\_wise** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) –

whether the commutation rule is applied to the whole operator, or on a per-qubit basis. For example:

```
>>> from qiskit.quantum_info import SparsePauliOp
>>> op = SparsePauliOp.from_list([("XX", 2), ("YY", 1), ("IZ",2j), ("ZZ",1j)])
>>> op.group_commuting()
[SparsePauliOp(["IZ", "ZZ"], coeffs=[0.+2.j, 0.+1j]),
 SparsePauliOp(["XX", "YY"], coeffs=[2.+0.j, 1.+0.j])]
>>> op.group_commuting(qubit_wise=True)
[SparsePauliOp(['XX'], coeffs=[2.+0.j]),
 SparsePauliOp(['YY'], coeffs=[1.+0.j]),
 SparsePauliOp(['IZ', 'ZZ'], coeffs=[0.+2.j, 0.+1.j])]
```

**Returns**

**List of SparsePauliOp where each SparsePauliOp contains**

commuting Pauli operators.

**Return type**

[list](https://docs.python.org/3/library/stdtypes.html#list)[[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")]

### input\_dims

`input_dims(qargs=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/base_operator.py#L135-L137 "view source code")

Return tuple of input dimension for specified subsystems.

### is\_unitary

`is_unitary(atol=None, rtol=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L433-L463 "view source code")

Return True if operator is a unitary matrix.

This method checks whether the operator composed with its adjoint equals the identity, up to the provided tolerance. The tolerance is used when simplifying the composed operator and checking if the result is the identity.

**Parameters**

* **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Optional. Absolute tolerance for checking if coefficients are zero (Default: 1e-8).
* **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Optional. Relative tolerance for checking if coefficients are zero (Default: 1e-5).

**Returns**

True if the operator is unitary, False otherwise.

**Return type**

[bool](https://docs.python.org/3/library/functions.html#bool)

### label\_iter

`label_iter()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1048-L1070 "view source code")

Return a label representation iterator.

This is a lazy iterator that converts each term in the SparsePauliOp into a tuple (label, coeff). To convert the entire table to labels use the `to_labels()` method.

**Returns**

label iterator object for the SparsePauliOp.

**Return type**

LabelIterator

### matrix\_iter

`matrix_iter(sparse=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1072-L1099 "view source code")

Return a matrix representation iterator.

This is a lazy iterator that converts each term in the SparsePauliOp into a matrix as it is used. To convert to a single matrix use the [`to_matrix()`](#qiskit.quantum_info.SparsePauliOp.to_matrix "qiskit.quantum_info.SparsePauliOp.to_matrix") method.

**Parameters**

**sparse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optionally return sparse CSR matrices if True, otherwise return Numpy array matrices (Default: False)

**Returns**

matrix iterator object for the PauliList.

**Return type**

MatrixIterator

### noncommutation\_graph

`noncommutation_graph(qubit_wise)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1101-L1117 "view source code")

Create the non-commutation graph of this SparsePauliOp.

This transforms the measurement operator grouping problem into graph coloring problem. The constructed graph contains one node for each Pauli. The nodes will be connecting for any two Pauli terms that do \_not\_ commute.

**Parameters**

**qubit\_wise** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – whether the commutation rule is applied to the whole operator, or on a per-qubit basis.

**Returns**

**the non-commutation graph with nodes for each Pauli and edges**

indicating a non-commutation relation. Each node will hold the index of the Pauli term it corresponds to in its data. The edges of the graph hold no data.

**Return type**

[rustworkx.PyGraph](https://www.rustworkx.org/apiref/rustworkx.PyGraph.html#rustworkx.PyGraph)

### output\_dims

`output_dims(qargs=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/base_operator.py#L139-L141 "view source code")

Return tuple of output dimension for specified subsystems.

### power

`power(n)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/mixins/group.py#L154-L174 "view source code")

Return the composition of an operator with itself n times.

**Parameters**

**n** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the number of times to compose with self (n>0).

**Returns**

the n-times composed operator.

**Return type**

[Clifford](/docs/api/qiskit/qiskit.quantum_info.Clifford "qiskit.quantum_info.Clifford")

**Raises**

[**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if the input and output dimensions of the operator are not equal, or the power is not a positive integer.

### reshape

`reshape(input_dims=None, output_dims=None, num_qubits=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/base_operator.py#L106-L133 "view source code")

Return a shallow copy with reshaped input and output subsystem dimensions.

**Parameters**

* **input\_dims** (*None or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – new subsystem input dimensions. If None the original input dims will be preserved [Default: None].
* **output\_dims** (*None or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – new subsystem output dimensions. If None the original output dims will be preserved [Default: None].
* **num\_qubits** (*None or* [*int*](https://docs.python.org/3/library/functions.html#int)) – reshape to an N-qubit operator [Default: None].

**Returns**

returns self with reshaped input and output dimensions.

**Return type**

BaseOperator

**Raises**

[**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if combined size of all subsystem input dimension or subsystem output dimensions is not constant.

### simplify

`simplify(atol=None, rtol=None)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L465-L532 "view source code")

Simplify PauliList by combining duplicates and removing zeros.

**Parameters**

* **atol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Optional. Absolute tolerance for checking if coefficients are zero (Default: 1e-8).
* **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float)) – Optional. relative tolerance for checking if coefficients are zero (Default: 1e-5).

**Returns**

the simplified SparsePauliOp operator.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

### sort

`sort(weight=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L604-L674 "view source code")

Sort the rows of the table.

After sorting the coefficients using numpy’s argsort, sort by Pauli. Pauli sort takes precedence. If Pauli is the same, it will be sorted by coefficient. By using the weight kwarg the output can additionally be sorted by the number of non-identity terms in the Pauli, where the set of all Pauli’s of a given weight are still ordered lexicographically.

**Example**

Here is an example of how to use SparsePauliOp sort.

```
import numpy as np
from qiskit.quantum_info import SparsePauliOp

# 2-qubit labels
labels = ["XX", "XX", "XX", "YI", "II", "XZ", "XY", "XI"]
# coeffs
coeffs = [2.+1.j, 2.+2.j, 3.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j, 7.+0.j]

# init
spo = SparsePauliOp(labels, coeffs)
print('Initial Ordering')
print(spo)

# Lexicographic Ordering
srt = spo.sort()
print('Lexicographically sorted')
print(srt)

# Lexicographic Ordering
srt = spo.sort(weight=False)
print('Lexicographically sorted')
print(srt)

# Weight Ordering
srt = spo.sort(weight=True)
print('Weight sorted')
print(srt)
```

```
Initial Ordering
SparsePauliOp(['XX', 'XX', 'XX', 'YI', 'II', 'XZ', 'XY', 'XI'],
              coeffs=[2.+1.j, 2.+2.j, 3.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j, 7.+0.j])
Lexicographically sorted
SparsePauliOp(['II', 'XI', 'XX', 'XX', 'XX', 'XY', 'XZ', 'YI'],
              coeffs=[4.+0.j, 7.+0.j, 2.+1.j, 2.+2.j, 3.+0.j, 6.+0.j, 5.+0.j, 3.+0.j])
Lexicographically sorted
SparsePauliOp(['II', 'XI', 'XX', 'XX', 'XX', 'XY', 'XZ', 'YI'],
              coeffs=[4.+0.j, 7.+0.j, 2.+1.j, 2.+2.j, 3.+0.j, 6.+0.j, 5.+0.j, 3.+0.j])
Weight sorted
SparsePauliOp(['II', 'XI', 'YI', 'XX', 'XX', 'XX', 'XY', 'XZ'],
              coeffs=[4.+0.j, 7.+0.j, 3.+0.j, 2.+1.j, 2.+2.j, 3.+0.j, 6.+0.j, 5.+0.j])
```

**Parameters**

* **weight** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optionally sort by weight if True (Default: False).
* **sorted** (*By using the weight kwarg the output can additionally be*)
* **Pauli.** (*by the number of non-identity terms in the*)

**Returns**

a sorted copy of the original table.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

### sum

*static* `sum(ops)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L716-L746 "view source code")

Sum of SparsePauliOps.

This is a specialized version of the builtin `sum` function for SparsePauliOp with smaller overhead.

**Parameters**

**ops** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")*]*) – a list of SparsePauliOps.

**Returns**

the SparsePauliOp representing the sum of the input list.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

**Raises**

* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if the input list is empty.
* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if the input list includes an object that is not SparsePauliOp.
* [**QiskitError**](/docs/api/qiskit/exceptions#qiskit.exceptions.QiskitError "qiskit.exceptions.QiskitError") – if the numbers of qubits of the objects in the input list do not match.

### tensor

`tensor(other)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L383-L386 "view source code")

Return the tensor product with another SparsePauliOp.

**Parameters**

**other** ([*SparsePauliOp*](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")) – a SparsePauliOp object.

**Returns**

**the tensor product a⊗ba \otimes ba⊗b, where aaa**

is the current SparsePauliOp, and bbb is the other SparsePauliOp.

**Return type**

[SparsePauliOp](#qiskit.quantum_info.SparsePauliOp "qiskit.quantum_info.SparsePauliOp")

Note

The tensor product can be obtained using the `^` binary operator. Hence `a.tensor(b)` is equivalent to `a ^ b`.

### to\_list

`to_list(array=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L973-L996 "view source code")

Convert to a list Pauli string labels and coefficients.

For operators with a lot of terms converting using the `array=True` kwarg will be more efficient since it allocates memory for the full Numpy array of labels in advance.

**Parameters**

**array** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – return a Numpy array if True, otherwise return a list (Default: False).

**Returns**

List of pairs (label, coeff) for rows of the PauliList.

**Return type**

[list](https://docs.python.org/3/library/stdtypes.html#list) or [array](/docs/api/qiskit/qiskit.primitives.BitArray#array "qiskit.primitives.BitArray.array")

### to\_matrix

`to_matrix(sparse=False, force_serial=False)`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1006-L1038 "view source code")

Convert to a dense or sparse matrix.

**Parameters**

* **sparse** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if `True` return a sparse CSR matrix, otherwise return dense Numpy array (the default).
* **force\_serial** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if `True`, use an unthreaded implementation, regardless of the state of the [Qiskit threading-control environment variables](/docs/guides/configure-qiskit-local#environment-variables). By default, this will use threaded parallelism over the available CPUs.

**Returns**

A dense matrix if sparse=False. csr\_matrix: A sparse matrix in CSR format if sparse=True.

**Return type**

[array](/docs/api/qiskit/qiskit.primitives.BitArray#array "qiskit.primitives.BitArray.array")

### to\_operator

`to_operator()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L1040-L1042 "view source code")

Convert to a matrix Operator object

**Return type**

[*Operator*](/docs/api/qiskit/qiskit.quantum_info.Operator "qiskit.quantum_info.operators.operator.Operator")

### to\_sparse\_list

`to_sparse_list()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L998-L1004 "view source code")

Convert to a sparse Pauli list format with elements (pauli, qubits, coefficient).

### transpose

`transpose()`

[GitHub](https://github.com/Qiskit/qiskit/tree/stable/2.4/qiskit/quantum_info/operators/symplectic/sparse_pauli_op.py#L314-L321 "view source code")

Return the transpose of the SparsePauliOp.

Was this page helpful?

YesNo

Report a bug, typo, or request content on [GitHub](https://github.com/Qiskit/documentation/issues/new/choose).

On this page

* [SparsePauliOp](#sparsepauliop)
* [Attributes](#attributes)
* [atol](#atol)
* [coeffs](#coeffs)
* [dim](#dim)
* [num\_qubits](#num_qubits)
* [parameters](#parameters)
* [paulis](#paulis)
* [qargs](#qargs)
* [rtol](#rtol)
* [settings](#settings)
* [size](#size)
* [Methods](#methods)
* [adjoint](#adjoint)
* [apply\_layout](#apply_layout)
* [argsort](#argsort)
* [assign\_parameters](#assign_parameters)
* [chop](#chop)
* [compose](#compose)
* [conjugate](#conjugate)
* [copy](#copy)
* [dot](#dot)
* [equiv](#equiv)
* [expand](#expand)
* [from\_list](#from_list)
* [from\_operator](#from_operator)
* [from\_sparse\_list](#from_sparse_list)
* [from\_sparse\_observable](#from_sparse_observable)
* [group\_commuting](#group_commuting)
* [input\_dims](#input_dims)
* [is\_unitary](#is_unitary)
* [label\_iter](#label_iter)
* [matrix\_iter](#matrix_iter)
* [noncommutation\_graph](#noncommutation_graph)
* [output\_dims](#output_dims)
* [power](#power)
* [reshape](#reshape)
* [simplify](#simplify)
* [sort](#sort)
* [sum](#sum)
* [tensor](#tensor)
* [to\_list](#to_list)
* [to\_matrix](#to_matrix)
* [to\_operator](#to_operator)
* [to\_sparse\_list](#to_sparse_list)
* [transpose](#transpose)

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