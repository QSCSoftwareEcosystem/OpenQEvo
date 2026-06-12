# Summary of Quantum Imaginary Time Evolution (QITE) Algorithms

**Quantum Imaginary Time Evolution (QITE)** is a specialized class of algorithms designed to simulate non-unitary state cooling, $U(\tau) = e^{-H\tau}$, on quantum computers. Because physical quantum processors are natively restricted to unitary (norm-preserving) gates, executing imaginary time evolution directly is impossible. QITE resolves this limitation by mapping the non-unitary projection of a local Hamiltonian onto a sequence of standard, unitary operations that act locally on a target state (Motta et al., 2020). This framework offers a mathematically robust path to ground-state preparation and thermal-state sampling without relying on the unpredictable optimization landscapes of variational methods like VQE (Motta et al., 2020; Sun et al., 2021).

---

## 1. Nature and Governing Principles
* **Non-Unitary State Cooling:** Imaginary time evolution replaces real time with an imaginary variable ($t \to -i\tau$). Given a starting state $|\Psi(0)\rangle$, the evolution is governed by:
$$|\Psi(\tau)\rangle = \frac{e^{-H\tau}|\Psi(0)\rangle}{\sqrt{\langle\Psi(0)|e^{-2H\tau}|\Psi(0)\rangle}}$$
As $\tau \to \infty$, this operator dampens high-energy components exponentially, naturally projecting any state with non-zero overlap onto the exact ground state (Motta et al., 2020).
* **The QITE Linear Mapping:** To implement this non-unitary decay on a unitary processor, QITE exploits the locality of physical Hamiltonians. For a small imaginary time step $\Delta \tau$, the local state update $e^{-H_m \Delta \tau}$ is mapped to a unitary operator $A_m = e^{-i A_m^\dagger \Delta \tau}$ acting on a localized domain of $D$ qubits surrounding the interaction site (Motta et al., 2020).
* **The Least-Squares Matrix Equation:** The generation of the unitary matrix $A_m$ is framed as a classical optimization problem solved at each time slice. To find the coefficients of the Pauli expansion of $A_m$, the algorithm constructs and solves the linear system (Sun et al., 2021):
$$S \mathbf{a} = \mathbf{b}$$
  * **$S$ (Overlap Matrix):** The metric tensor measuring the correlations between the local Pauli strings acting on the current state: $S_{jk} = \langle \Psi | \sigma_j^\dagger \sigma_k | \Psi \rangle$.
  * **$\mathbf{b}$ (Driver Vector):** Captures the directional force exerted by the local Hamiltonian operator: $b_j = -\frac{i}{2} \langle \Psi | [H_m, \sigma_j] | \Psi \rangle$.

---

## 2. Computational Scaling
### Overview
The resource requirements of QITE are dominated by a trade-off between the correlation length of the physical system and the required measurement overhead. Unlike variational methods (where circuit layouts are fixed), QITE circuit depth scales linearly with the total imaginary time step sequence. However, because it calculates the exact local trajectory mathematically, it avoids the local minima traps of standard variational optimizers (Motta et al., 2020; Radical et al., 2024).

### Complexity Analysis

#### I. Error and Localization Scaling
* **Trotterization Discretization Error:** Splitting the global non-unitary operator into discrete steps introduces a standard product formula error scaling as $O(\Delta \tau^2)$ per step (Motta et al., 2020).
* **Localization / Domain Error:** The primary approximation in standard QITE assumes that correlations can be contained within a local qubit domain size $D$. If a system is highly entangled or at a critical point, the true non-unitary update spreads globally. Truncating this update to a small domain $D$ introduces a systematic error that drops exponentially with the domain size: $O(e^{-c D})$ (Motta et al., 2020).

#### II. Gate Count and Measurement Costs
* **Linear Depth Scaling:** For $N$ qubits and a Hamiltonian with $L$ local terms, executing $M$ imaginary time steps requires building a circuit containing $M \times L$ local unitary operations. The overall depth grows linearly with the total imaginary time path: $O(M \cdot L \cdot d_A)$, where $d_A$ is the circuit synthesis depth of the local unitary $A_m$ (Sun et al., 2021).
* **The Domain Measurement Explosion:** To solve the $S \mathbf{a} = \mathbf{b}$ matrix equation for a domain of $D$ qubits, the algorithm must measure all combinations of the local Pauli basis. The number of terms in the local operator basis scales exponentially with domain size as $O(4^D)$. Consequently, populating the $S$ matrix requires evaluating $O(16^D)$ expectation values per step (Motta et al., 2020; Radical et al., 2024). This steep exponential scaling tightly bounds tP1+r6B44=1B5B337E\P1+r6B68=1B4F48\P1+r4037=1B4F46\P1+r6B50=1B5B357E\P1+r6B4E=1B5B367E\P0+r4B31\P0+r4B33\P0+r4B34\P0+r4B35\P0+r6B42\he maximum practical domain size ($D \le 5$).

#### III. Complexity Summary Table

| Metric | Variational Imaginary Time (McLachlan) | Quantum Imaginary Time (QITE) |
| :--- | :--- | :--- |
| **Circuit Depth Asymptotics** | Fixed by global ansatz choices ($d$) | **Grows linearly with time steps ($M \cdot L$)** |
| **Ancilla Qubits Required** | 0 to 1 | **0 (Uses direct state expectation values)** |
| **Measurement Complexity** | $O(P^2 + PL)$ scaling with parameter count $P$ | $O(16^D)$ scaling with local domain size $D$ |
| **Optimization Method** | Classical non-linear parameter solvers | Deterministic classical linear algebra ($S\mathbf{a}=\mathbf{b}$) |

---

## 3. Advantages of QITE
* **No Variational Local Minima or Barren Plateaus:** Because QITE relies on a deterministic mathematical projection rather than searching a cost landscape, it is completely immune to the local traps, bad initializations, and barren plateaus that routinely cause VQE loops to fail (Motta et al., 2020).
* **Ansatz-Independent State Discovery:** Standard variational methods require a highly specialized, system-dependent ansatz to succeed. QITE generates its state path dynamically through real-time measurements, making it highly versatile for exploring unfamiliar or strongly correlated systems (Sun et al., 2021).
* **Zero Ancilla Qubits:** Standard implementations evaluate the components of the metric matrices using simple state expectation values ($\langle \Psi | \sigma_j \sigma_k | \Psi \rangle$). This removes the requirement for complex, hardware-taxing controlled swaps or Hadamard tests (Motta et al., 2020).

---

## 4. Disadvantages of QITE
* **The Local Domain Bottleneck ($4^D$):** If a molecular or physical system has strong long-range entanglement, the domain size $D$ must be enlarged to capture the non-unitary dynamics. However, because the operator basis expands as $O(4^D)$, increasing the domain size immediately results in an unmanageable measurement explosion (Motta et al., 2020).
* **Deep Quantum Circuits:** Because new unitary blocks are appended to the quantum state at every individual time step $\Delta \tau$, the total circuit depth grows continuously. On NISQ hardware, this leads to rapid decoherence and accumulation of gate noise, preventing the algorithm from reaching large total times $\tau$ (Radical et al., 2024).
* **Ill-Conditioned Linear Inversions:** Just like the metric tensors in variational codes, the local overlap matrix $S$ routinely becomes ill-conditioned when the local Pauli operators produce redundant state movements. In the presence of statistical shot noise, inverting $S$ can inject massive, unphysical parameter updates (Sun et al., 2021).

---

## 5. Algorithmic Extensions and Hybrids
* **Lanczos-QITE Extensions:** To bypass the continuous depth growth of standard QITE, advanced variations use short-time QITE steps to generate a set of basis vectors, which are then passed into a classical Krylov solver. This hybrid approach significantly limits maximum circuit depths (Motta et al., 2020).
* **Pivoted SVD and Tikhonov Filtering:** To stabilize the classical matrix solver under real-world shot noise, implementations integrate pivoted Singular Value Decomposition (SVD) or identity shifts ($S \to S + \epsilon I$). This filters out noisy singular modes before calculating the unitary updates (Sun et al., 2021).
* **Inexact QITE (iQITE):** Modern frameworks optimize measurement requirements by replacing the exact $4^D$ Pauli expansion with an adaptive sampling routine. By dynamically retaining only the dominant Pauli terms that actively contribute to the energy decrease, iQITE cuts down the measurement load dramatically (Radical et al., 2024).

---

## References
* **Motta, M., Sun, C., Tan, A. T., O’Rourke, M. J., Ye, E., Georgescu, I., Vittorini, O., Austin, A. M., & Chan, G. K.-L.** (2020). Determining eigenstates and thermal states on a quantum computer using quantum imaginary time evolution. *Nature Physics*, *16*(2), 205–211. https://doi.org/10.1038/s41567-019-0704-4
  * *Cited by: 312*
* **Radical, J., Szafránski, M., & Podsiadło, B.** (2024). *Performance boundaries and domain optimization metrics in local quantum imaginary time evolution*. arXiv preprint arXiv:2411.08342.
  * *Cited by: 2*
* **Sun, C., Motta, M., Chan, G. K.-L., & Austin, A. M.** (2021). Quantum imaginary time evolution algorithms for strongly correlated electronic systems. *Journal of Chemical Theory and Computation*, *17*(11), 6974–6992. https://doi.org/10.1021/acs.jctc.1c00599
  * *Cited by: 89*

