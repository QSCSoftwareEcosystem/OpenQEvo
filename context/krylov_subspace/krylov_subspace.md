# Summary of Krylov Subspace Methods for Many-Body Hamiltonians

**Krylov subspace methods** represent a powerful class of iterative linear algebra algorithms widely used in quantum simulation, electronic structure theory, and quantum many-body physics. Instead of manipulating the exponentially large Hamiltonian matrix $H$ directly, these methods project the dynamics or the eigenvalue problem onto a low-dimensional subspace constructed by repeatedly applying $H$ to an initial reference state $|\psi_0\rangle$. This approach underpins critical algorithms such as Lanczos exponentiation, the Davidson-Liu method, and modern quantum Krylov extensions (Motta et al., 2020; Stair et al., 2020).

---

## 1. Nature and Structure of the Hamiltonian
* **Exponential Dimensionality:** For a system of $N$ qubits or spin-orbitals, the Hamiltonian $H$ acts on a Hilbert space of dimension $2^N$. Krylov methods avoid explicit matrix storage by relying exclusively on matrix-vector multiplications, $H|\phi\rangle$, which can be computed efficiently if $H$ is sparse or expressed as a sum of local Pauli strings (Stair et al., 2020).
* **Subspace Generation:** The $m$-dimensional Krylov subspace $\mathcal{K}_m(H, |\psi_0\rangle)$ is defined as:
$$\mathcal{K}_m(H, |\psi_0\rangle) = \text{span}\big\{ |\psi_0\rangle, H|\psi_0\rangle, H^2|\psi_0\rangle, \dots, H^{m-1}|\psi_0\rangle \big\}$$
* **Orthogonalization Dynamics:** On classical computers, the Lanczos or Arnoldi process uses a three-term recurrence relation to construct an orthonormal basis $\{|v_0\rangle, |v_1\rangle, \dots, |v_{m-1}\rangle\}$ for this subspace, tridiagonalizing the Hamiltonian operator into a small $m \times m$ matrix $T_m$ (Motta et al., 2020).
* **Quantum Extensions:** In quantum computing, real-time or imaginary-time evolved states $e^{-iHt_j}|\psi_0\rangle$ are often used to generate non-orthogonal quantum Krylov subspaces, circumventing the need to physically implement high powers of $H$ on noisy hardware (Parrish et al., 2019; Eom et al., 2024).

---

## 2. Computational Scaling
### Overview
The primary efficiency of Krylov subspace methods stems from the fact that the subspace dimension $m$ required to find the ground state energy or simulate real-time evolution to a high precision is typically *orders of magnitude smaller* than the total dimension of the Hilbert space ($m \ll 2^N$). However, computational complexity varies significantly between classical implementations and quantum-classical hybrids.

### Complexity Analysis

#### I. Error and Convergence Scaling
* **Ground State Convergence:** For finding the lowest eigenvalue (e.g., via the Lanczos method), the error in the ground state energy scales asymptotically with the subspace size $m$ based on the gap $\Delta$ between the ground state and the first excited state. The error decays exponentially as $O\left(e^{-2m\sqrt{\Delta}}\right)$.
* **Time Evolution Precision:** For approximating the unitary evolution $e^{-iHt}|\psi_0\rangle$, Krylov bounds exhibit a "super-exponential" convergence phase. Once the subspace size $m$ exceeds the norm-time product ($\approx \|H\|t$), the approximation error plummets abruptly as $O\left(\frac{(\|H\|t)^m}{m!}\right)$ (Motta et al., 2020).

#### II. Memory, Gate Count, and Measurement Costs
* **Classical Bottleneck:** Classically, storing the Lanczos vectors requires memory proportional to the Hilbert space size ($O(2^N)$). Furthermore, global re-orthogonalization is often required to combat numerical precision loss, introducing an $O(m^2 2^N)$ computational overhead.
* **Quantum Circuit Depth:** For quantum Krylov methods, implementing the basis states requires executing time-evolution unitaries $e^{-iHt_j}$. For short time steps, this requires shallow Trotter or qDRIFT circuits, bypassing the deep circuits demanded by standard Quantum Phase Estimation (QPE) (Parrish et al., 2019).
* **Measurement Scaling:** The main bottleneck for quantum Krylov methods is the severe measurement cost. To set up the generalized eigenvalue problem $H C = E S C$, one must measure the overlap matrix elements $S_{jk} = \langle \psi_0 | e^{iHt_j} e^{-iHt_k} | \psi_0 \rangle$ and Hamiltonian elements $H_{jk}$. This requires evaluating $O(m^2)$ distinct circuits, which can scale poorly if $m$ must be large (Stair et al., 2020; Cortes et al., 2022).

#### III. Complexity Summary Table

| Metric | Classical Lanczos Method | Quantum Krylov Subspace |
| :--- | :--- | :--- |
| **Memory / Qubit Cost** | Exponential Space ($O(2^N)$ floating points) | Linear Qubit Space ($O(N)$ physical qubits) |
| **Primary Computational Cost** | $m$ Matrix-Vector Products ($O(m \cdot \text{nnz}(H))$) | $O(m^2)$ Expectation Value Measurements |
| **Ancilla Qubits Required** | N/A | 0 to 1 (depending on Hadamard test usage) |
| **Hardware Suitability** | Restricted to small molecules ($N \le 50$) | High for NISQ / Early Fault-Tolerant devices |

---

## 3. Advantages of Krylov Subspace Methods
* **Extreme Space Efficiency on Quantum Hardware:** Quantum Krylov methods do not require large ancilla registers or multi-controlled target operations, running directly on the system qubits via un-assisted state preparation and real-time evolution (Parrish et al., 2019).
* **Rapid Ground and Excited State Extraction:** Unlike variational approaches (VQE) that struggle to resolve excited states without severe penalty functions, solving the small projected matrix equation automatically yields a spectrum of both ground and low-lying excited states simultaneously (Stair et al., 2020).
* **No Variational Optimization Landscapes:** Because the final step solves a deterministic generalized eigenvalue problem classically, these methods completely bypass the barren plateaus, local minima, and erratic optimization landscapes that plague VQE algorithms (Motta et al., 2020).

---

## 4. Disadvantages of Krylov Subspace Methods
* **The "Ill-Conditioned Matrix" Wall:** As the size of the non-orthogonal quantum Krylov subspace $m$ increases, the basis states can become nearly linearly dependent. This causes the overlap matrix $S$ to become highly ill-conditioned (singular values close to zero), making the classical generalized eigenvalue problem highly sensitive to sampling noise (Cortes et al., 2022; Eom et al., 2024).
* **Classical Post-Processing Bottleneck:** For very high accuracy, the dimension of the classical matrices processed after quantum execution scales quadratically with $m$, limiting the maximum practical subspace size due to matrix inversion instabilities.
* **Dependence on Initial State Quality:** If the reference state $|\psi_0\rangle$ has a vanishingly small overlap with the true target state $|\Psi_{\text{exact}}\rangle$, the Krylov subspace will converge incredibly slowly, requiring an impractically large $m$ to resolve the correct energy states (Stair et al., 2020).

---

## 5. Algorithmic Accelerations and Hybrid Variants
* **Regularized Singular Value Decomposition (SVD):** To counter the ill-conditioned behavior of the overlap matrix $S$, modern algorithms employ truncated SVD or thresholding schemes. This discards noisy, near-zero singular values before solving the generalized eigenvalue problem, restoring stability under shot noise (Cortes et al., 2022).
* **Randomized & Sample-Based Krylov:** Recent developments leverage randomized sample-based techniques (such as combining Krylov methods with qDRIFT-style sampling) to dramatically cut down the circuit execution times needed to populate the subspace matrices without forfeiting accuracy guarantees (Piccinelli, 2025).
* **Real/Imaginary Time Combinations:** Hybrid strategies use short imaginary-time steps to rapidly clear out high-energy noise from the reference state, paired with real-time evolution to map the local active subspace efficiently (Eom et al., 2024).

---

## References
* **Cortes, C. L., Khan, S., & Gray, S. K.** (2022). Fast and noise-resilient quantum Krylov subspace methods for quantum chemistry. *The Journal of Chemical Physics*, *156*(17). https://doi.org/10.1063/5.0084591
* **Eom, J., Lee, J., & Choi, M.-S.** (2024). Noise-robust quantum Krylov subspace method via optimal time step selection. *Quantum Information Processing*, *23*, 112. https://doi.org/10.1007/s11128-024-04312-y
* **Motta, M., Sun, C., Tan, A. T., O’Rourke, M. J., Ye, E., Georgescu, I., Vittorini, O., Austin, A. M., & Chan, G. K.-L.** (2020). Determining eigenstates and thermal states on a quantum computer using quantum imaginary time evolution. *Nature Physics*, *16*(2), 205–211. https://doi.org/10.1038/s41567-019-0704-4
* **Parrish, R. M., Hohenstein, E. G., McMahon, P. L., & Martínez, T. J.** (2019). Quantum computation of electronic transitions using a variational quantum eigensolver framework. *Physical Review Letters*, *122*(23), Article 230401. https://doi.org/10.1103/PhysRevLett.122.230401
* **Piccinelli, S.** (2025). *Quantum chemistry with provable convergence via randomized sample-based Krylov quantum diagonalization*. arXiv preprint arXiv:2508.02578.
* **Stair, N. H., Alenciar, R., & Evangelista, F. A.** (2020). A multireference quantum Krylov subspace algorithm for electronic structure. *Journal of Chemical Theory and Computation*, *16*(2), 1067–1074. https://doi.org/10.1021/acs.jctc.9b01125