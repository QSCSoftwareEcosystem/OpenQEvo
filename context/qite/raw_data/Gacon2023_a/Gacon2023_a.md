# Stochastic Approximation of Variational Quantum Imaginary Time Evolution

Julien Gacon\*†, Christa Zoufal\*, Giuseppe Carleo† and Stefan Woerner\*

\*IBM Quantum, IBM Research Europe – Zurich, CH-8803 Rüschlikon, Switzerland †Institute of Physics, École Polytechnique Fédérale de Lausanne (EPFL), CH-1015 Lausanne, Switzerland

Abstract—The imaginary-time evolution of quantum states is integral to various fields, ranging from natural sciences to classical optimization or machine learning. Since simulating quantum imaginary-time evolution generally requires storing an exponentially large wave function, quantum computers are emerging as a promising platform for this task. However, variational approaches, suitable for near-term quantum computers, struggle with a prohibitive number of measurements and impractical runtimes for relevant system sizes. Here, we suggest a stochastic approach to variational quantum imaginary-time evolution, which allows a significant reduction in runtimes. Our approach allows trading off invested resources and accuracy, which makes it also suitable for ground state preparation, where simulating the exact dynamics is not required. We demonstrate the efficiency of our algorithm in simulations and show a hardware experiment performing the imaginary-time evolution of the transverse field Ising model on 27 qubits.

Index Terms—Quantum computing, Quantum algorithms, Quantum simulation, Optimization

#### I. Introduction

Quantum imaginary-time evolution is a powerful tool which allows to prepare thermal states (or Gibbs states) and ground states of a quantum mechanical system [1]. Thermal states are particularly interesting in physics, for example, as they can be used to calculate thermodynamic observables [2, 3], or in machine learning, where they are used in quantum Boltzmann machines [4]. The preparation of ground states is even more general and finds applications in natural sciences, such as physics and chemistry, but also beyond quantum mechanical fields, such as classical optimization, finance, or machine learning [5].

Performing the imaginary-time evolution of quantum states generally requires storing an exponentially large wave function and quantum computers are emerging as a promising platform to solve this task. In contrast to real-time evolution, a unitary operation, imaginary-time evolution is non-unitary. Therefore, the standard Suzuki-Trotter approximation of the time-evolution operator [6], common in the real-time counterpart, cannot be applied directly to simulate imaginary-time dynamics on a gate-based quantum computer. Though there exist generalizations of Trotterization to imaginary-time evolution [7], these often require complex quantum circuits to be executed. These requirements make Trotterization-based approaches unsuitable for near-term quantum computers, which are characterized by short qubit coherence times, limited connectivity, and noisy operations.

Instead of directly evolving the quantum state, variational approaches to imaginary-time evolution map the time evolution onto parameters in an ansatz circuit. This ansatz circuit can be tailored to match the available device's capabilities which makes variational methods especially prominent in the era of near-term quantum computers. The mapping of state to parameter evolution in variational quantum imaginary-time evolution (VarQITE) can be achieved with a variational principle [1, 8], such as the McLachlan variational principle, which relies on the evaluation of the Quantum Geometric Tensor (QGT) and the energy gradient at the current parameter values

If the ansatz circuit has  $d \in \mathbb{N}$  variational parameters, the calculation of the QGT requires sampling from  $\mathcal{O}(d^2)$  circuits, respectively  $\mathcal{O}(d)$  for the energy gradient [9, 10]. This scaling is not an issue for variational states containing a small number of parameters. Still, it can quickly become a bottleneck on near-term devices for circuits with 100 or more parameters [3]. As the current generation of quantum computers reaches 100 qubits and more, such as the IBM Quantum Eagle [11] or Osprey [12] devices, it is crucial to develop scalable algorithms that are suitable for the growing circuit sizes.

In this paper, we suggest a stochastic approach to variational quantum imaginary-time evolution (SA-QITE), that is based on stochastic approximation of Quantum Natural Gradients (QNG) [9, 10]. Instead of computing the full QGT and gradient in each timestep, we start from an accurate initial estimation and correct the estimators in each iteration using unbiased samples. Unlike the  $\mathcal{O}(d^2)$  scaling of the QGT, the samples rely on a simultaneous perturbation, stochastic approximation (SPSA) [13] method, which requires a constant number of circuits independent of the parameter dimension d [10]. We provide numerical evidence that SA-QITE requires fewer measurements than VarQITE to achieve the same accuracy and show that our algorithm represents a promising, near-term compatible imaginary-time simulation approach by applying it to a 27-qubit Ising model on an IBM Quantum processor.

Other approaches to avoid the evaluation of the QGT, that have recently been proposed rely on solving an optimization problem in each timestep, based on e.g. the fidelity [3, 14] or a purified Suzuki-Trotter step [15]. While these methods may exhibit a favorable scaling, it is challenging to measure the fidelity up to the required accuracy on current devices [3], or to efficiently measure the required state overlap [14]. Our

stochastic approach does not suffer from these problems, as it relies only on relative differences of the state fidelity, and can readily be applied on near-term devices.

The remainder of this paper is structured as follows. Section II starts by introducing VarQITE and then shows how to construct unbiased samples of the QGT and energy gradients and how to improve the estimator accuracy using momenta and exact initialization. In Section III we compare the resource requirements of SA-QITE and VarQITE in numerical simulations for imaginary-time evolution of the transverse field Ising model and, then, use a relaxed version of SA-QITE to solve a Max Cut optimization problem. Next, we demonstrate our algorithm on a near-term quantum computer in Section IV, before concluding in Section V.

# II. STOCHASTIC VARIATIONAL IMAGINARY TIME EVOLUTION

The normalized, imaginary-time evolution of an initial state  $|\Psi_0\rangle$  under a Hamiltonian H at time t is defined as

$$|\Psi(t)\rangle = \frac{e^{-tH}}{\sqrt{\langle\Psi_0|e^{-2tH}|\Psi_0\rangle}}\,|\Psi_0\rangle\,.$$

In contrast to real-time evolution, which evolves under  $\exp(-itH)$ , the imaginary-time evolution operator  $\exp(-tH)$  is not unitary.

Instead of evolving the quantum state directly, the idea of VarQITE is to project the state update to updates of variational parameters  $\boldsymbol{\theta} \in \mathbb{R}^d$  in an ansatz state  $|\phi(\boldsymbol{\theta}(t))\rangle \approx |\Psi(t)\rangle$ . This projection is achieved with a variational principle, such as McLachlan's variational principle, which allows computing the parameter derivative as the solution of the following linear system of equations

$$g(\boldsymbol{\theta})\dot{\boldsymbol{\theta}} = \boldsymbol{b}(\boldsymbol{\theta}),\tag{1}$$

where we introduced the real part of the QGT  $g = \text{Re}(G) \in \mathbb{R}^{d \times d}$  and the evolution gradient  $b \in \mathbb{R}^d$ . The QGT is defined as

$$G_{ij}(\boldsymbol{\theta}) = \left\langle \frac{\partial \phi}{\partial \theta_i} \middle| \frac{\partial \phi}{\partial \theta_j} \right\rangle - \left\langle \frac{\partial \phi}{\partial \theta_i} \middle| \phi \right\rangle \left\langle \phi \middle| \frac{\partial \phi}{\partial \theta_j} \right\rangle, \quad (2)$$

and the evolution gradient is

$$b_i(\boldsymbol{\theta}) = -\text{Re}\left(\left\langle \frac{\partial \phi}{\partial \theta_i} \middle| H \middle| \phi \right\rangle\right) = -\frac{1}{2} \frac{\partial E}{\partial \theta_i},$$
 (3)

where  $E(\theta) = \langle \phi(\theta) | H | \phi(\theta) \rangle$  is the energy of the system. The individual terms of g and b can be evaluated, for example, with a linear combination of unitaries approach (LCU) or parameter-shift rules [16]. These techniques require a constant number of expectation values per tensor element (or vector element) and therefore a total of  $\mathcal{O}(d^2)$  circuits for the QGT, respectively  $\mathcal{O}(d)$  for the evolution gradient.

Other variational formulations include the Dirac-Frenkel or the time-dependent variational principle, which also rely on the QGT and evolution gradient but may yield complex parameters [8], which are not available in our quantum circuit model.

#### A. Sampling the QGT and evolution gradient

To circumvent the significant computational costs to evaluate the QGT in high-dimensional parameter spaces we replace g with a stochastic estimate from which we can draw unbiased samples  $\hat{g}$  at a constant cost [10]. The samples are obtained by first reformulating the QGT as Hessian of the Fubini-Study metric and, then, estimating the Hessian using two nested simultaneous perturbation finite difference approximations, as

$$\hat{g} = -\frac{1}{2} \frac{\delta F}{4\epsilon^2} \frac{\mathbf{\Delta}_1 \mathbf{\Delta}_2^T + \mathbf{\Delta}_2 \mathbf{\Delta}_1^T}{2} \tag{4}$$

where  $\Delta_{1,2} \sim \mathcal{U}(\{1,-1\}^d)$  are uniformly distributed perturbation directions,  $\epsilon > 0$  is the perturbation magnitude, and

$$\begin{split} \delta F = & F(\boldsymbol{\theta}, \boldsymbol{\theta} + \epsilon(\boldsymbol{\Delta}_1 + \boldsymbol{\Delta}_2)) - F(\boldsymbol{\theta}, \boldsymbol{\theta} + \epsilon(\boldsymbol{\Delta}_1 - \boldsymbol{\Delta}_2)) \\ & - F(\boldsymbol{\theta}, \boldsymbol{\theta} + \epsilon(\boldsymbol{\Delta}_2 - \boldsymbol{\Delta}_1)) + F(\boldsymbol{\theta}, \boldsymbol{\theta} - \epsilon(\boldsymbol{\Delta}_1 + \boldsymbol{\Delta}_2)), \end{split}$$

with the fidelity  $F(\boldsymbol{\theta}, \boldsymbol{\omega}) = |\langle \phi(\boldsymbol{\theta}) | \phi(\boldsymbol{\omega}) \rangle|^2$ .

There exist a variety of techniques to compute the fidelity F of two quantum states prepared with quantum circuits  $|\phi(\theta)\rangle$  and  $|\phi(\omega)\rangle$ , such as the Swap Test [17] and variations thereof [18] or randomized measurements [19]. Both these methods are, however, unsuitable for our near-term setting as the swap test requires doubling the circuit width and non-local operations, and the randomized measurements use an exponential number of measurements. Instead, we here use the compute-uncompute method [20], which prepares  $U^{\dagger}(\theta)U(\omega)|0\rangle$  and estimates the probability of measuring  $|0\rangle$ . This doubles the circuit depth but does not add any additional qubits or couplings and is, therefore easier to execute on the near-term superconducting devices we consider.

Analogous to g we can estimate b as a first-order gradient with a single perturbation direction  $\Delta \sim \mathcal{U}(\{1, -1\}^d)$ ,

$$\hat{\boldsymbol{b}} = -\frac{1}{2} \frac{E(\boldsymbol{\theta} + \epsilon \boldsymbol{\Delta}) - E(\boldsymbol{\theta} - \epsilon \boldsymbol{\Delta})}{2\epsilon} \boldsymbol{\Delta}.$$
 (5)

As we perturb all parameter dimensions at once, there is no dependency on the number of parameters d and the calculation of a single sample  $\hat{g}$  requires evaluating four circuits only and two expectation values for  $\hat{b}$ .

# B. Improving estimator accuracy

Since the samples  $\hat{g}$  rely on only two perturbation directions (or one direction for  $\hat{b}$ ) they can have a very low accuracy. This is especially true for the QGT, since a single sample has at most rank 2, whereas the exact matrix can have a rank equal to the number of parameters d. Therefore a single sample is typically replaced by an average over a batch of N individual samples

$$\hat{g}_N = \frac{1}{N} \sum_{i=1}^N \hat{g}_{(i)}$$
 and  $\hat{b}_N = \frac{1}{N} \sum_{i=1}^N \hat{b}_{(i)}$ .

The approximation error for both G and b scales as  $\mathcal{O}(N^{-1/2})$  in the number of samples N, see also Appendix A for a numerical experiment.

The estimate at the current step can be combined with all previous ones to further increase stability. Refs. [10, 13]

suggest combining the samples from each time step into a global average

$$\bar{g}^{(k)} = \frac{k}{k+1} \bar{g}^{(k-1)} + \frac{1}{k+1} \hat{g}_N^{(k)}. \tag{6}$$

For time evolution, however, a global average cannot correctly capture the time dependence of the QGT. Instead, we propose to use momentum terms for both the QGT and the evolution gradient, such that the estimators in timestep k are given by

$$\bar{g}^{(k)} = \tau_1 \bar{g}^{(k-1)} + (1 - \tau_1) \hat{g}_N^{(k)}$$
$$\bar{b}^{(k)} = \tau_2 \bar{b}^{(k-1)} + (1 - \tau_2) \hat{b}_N^{(k)},$$

for momenta  $\tau_1, \tau_2 \in (0, 1)$ .

As averaging by moment introduces a bias, especially at early times of the imaginary-time evolution, it is crucial to initialize the algorithm with accurate initial values of g and b. These could be computed using resources that scale with  $\mathcal{O}(d^2)$  a single time but can, in some cases, also be efficiently simulable classically. For example, if the ansatz consists of Pauli rotations and CX gates and the initial parameters are integer multiples of  $\pi/2$ , every operation in the gradient calculations is a Clifford gate, as is discussed in detail in Appendix B. Two common scenarios where this is the case are classical optimization problems, which prepare an equal superposition state,  $|+\rangle^{\otimes n}$ , and use a QAOA or hardwareefficient ansatz [5, 21], or molecular ground state searches, where the ansatz is constructed from a Hartree-Fock initial state followed by operator evolutions, such as UCCSD, or partial swaps [22–24].

#### C. Solving for the parameter update

Determining the parameter derivative  $\theta$  by directly solving the linear system in Eq. (1) is numerically only stable for the exact QGT and evolution gradient [25]. Here, however, we are dealing with a noisy linear system,

$$\bar{g}^{(k)}\dot{\boldsymbol{\theta}} = \bar{\boldsymbol{b}}^{(k)},\tag{7}$$

due to a finite number of measurements in each circuit evaluation, a finite number of gradient samples N, and hardware noise. These noise sources lead to an ill-conditioned linear system which requires careful regularization.

A simple regularization of the linear system is the addition of a weighted identity matrix to the system matrix, that is

$$(\bar{g}^{(k)} + \delta \mathbb{I})\dot{\boldsymbol{\theta}} = \bar{\boldsymbol{b}}^{(k)}, \tag{8}$$

for a shift  $\delta > 0$  and the identity matrix  $\mathbb{I} \in \mathbb{R}^{d \times d}$ . This is equivalent to adding  $\delta$  to each eigenvalue of the QGT estimate, decreasing the condition number, and improving the stability of the linear system.

Adding a diagonal shift, however, influences the parameter dynamics as the derivative magnitude is additionally restricted by its  $\ell_2$  norm. In the case of optimization, for example, Ref. [10] shows that QNG for large diagonal shifts approaches standard gradient descent.

To minimize the regularization effect on the evolution, we can solve for the update step only in a stable subspace, where the eigenvalues are above some threshold. Since the QGT estimate is real and symmetric, we can write

$$\bar{q}^{(k)}\dot{\boldsymbol{\theta}} = B\Lambda B^T\dot{\boldsymbol{\theta}} = \bar{\boldsymbol{b}}^{(k)}$$

for an orthonormal matrix B and diagonal matrix  $\Lambda = \operatorname{diag}(\lambda_1,\lambda_2,...,\lambda_d)$ , with the eigenvalues  $\{\lambda_i\}_{i=1}^d$  of  $\bar{g}^{(k)}$ . Defining  $\dot{\boldsymbol{\theta}}^B = B^T\dot{\boldsymbol{\theta}}$  and  $\boldsymbol{b}^B = B^T\bar{\boldsymbol{b}}^{(k)}$ , we obtain the diagonal linear system

$$\Lambda \dot{\boldsymbol{\theta}}^B = \boldsymbol{b}^B$$
.

which we solve by only considering well-conditioned components in the solution

$$\dot{\theta}_i^B = \begin{cases} b_i^B / \lambda_i, & \text{if } \lambda_i \ge \delta \\ 0, & \text{otherwise} \end{cases}$$
 (9)

Finally we transform back to the original basis via  $\dot{\theta} = B\dot{\theta}^B$ . This update rule ensures the parameter derivative does not diverge in ill-conditioned subspaces. In Appendix C we show that this approach produces a more stable convergence of SA-QITE.

#### D. Relation to Quantum Natural Gradients

Quantum Natural Gradient Descent (QNG) is a variant of gradient descent to find the minimum of an objective function  $\ell(\theta)$ , where the size of the parameter update step is limited by the amount of change induced to the model, measured by the Fubini-Study metric [9, 26]. The next step of the optimization,  $\theta^{(k+1)}$ , is determined as

$$\boldsymbol{\theta}^{(k+1)} = \operatorname*{argmin}_{\boldsymbol{\theta} \in \mathbb{R}^d} (\boldsymbol{\theta} - \boldsymbol{\theta}^{(k)})^T \nabla \ell(\boldsymbol{\theta}^{(k)}) + \frac{D^2(\boldsymbol{\theta}^{(k)}, \boldsymbol{\theta})}{2\eta},$$

with the learning rate  $\eta > 0$  and the Fubini-Study metric  $D^2(\theta, \omega) = \arccos^2(|\langle \phi(\theta) | \phi(\omega) \rangle|)$ .

By solving the minimization and approximating the Fubini-Study metric with a second-order Taylor expansion, we obtain the following update rule

$$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \eta g^{-1}(\boldsymbol{\theta}^{(k)}) \nabla \ell(\boldsymbol{\theta}^{(k)}),$$

which shows the analogy of QNG and VarQITE: If the QNG's loss function is  $\ell(\theta) = E(\theta)/2$  and we integrate the parameter in VarQITE using a forward Euler method with timestep  $\eta$ , the update rules of QNG and VarQITE coincide.

Therefore, the momentum-based estimations of the QGT and gradient are also suitable for optimization. In contrast to imaginary-time evolution, minimizing a loss function does not require tracking the parameter trajectory as closely as possible. This allows to relax the number of samples N per iteration, which provides a less accurate estimation of g and g, but may decrease the total number of measurements required to converge to the minimum.

#### III. NUMERICAL RESULTS

In this section we investigate how SA-QITE performs for two tasks: the imaginary-time evolution of the transverse-field Ising model, and the ground-state approximation of a diagonal Hamiltonian, typical e.g. in Max Cut problems. All algorithms are implemented and simulated using Oiskit [27].

![](_page_3_Figure_0.jpeg)

Fig. 1: The structure of variational ansatz  $|\phi(\theta)\rangle$  used in the SA-QITE experiments.

# A. Quantum Imaginary Time Evolution

The transverse-field Ising model of n spin-1/2 particles on a chain is given by

$$H = J \sum_{i=1}^{n-1} Z_i Z_{i+1} + h \sum_{i=1}^{n} X_i,$$
 (10)

where we set the interaction to J=1/2, the transverse field strength to h=-1,  $X_i$  and  $Z_i$  are Pauli-X and Z operators, acting on spin i. As the initial state of the system, we consider  $|\Psi_0\rangle = |0\rangle^{\otimes n}$ .

The variational ansatz  $|\phi(\theta)\rangle$  is chosen to reflect the nearest-neighbor connectivity of the Hamiltonian. It consists of L alternating rotation layers, with parameterized Pauli-Y and Pauli-Z rotations, and entangling layers with pairwise CX connections. This circuit, whose structure is shown in Fig. 1, has a CX depth of 2 per entangling layer and a total number of parameters d=2n(L+1).

We compare the total number of measurements required by SA-QITE and VarQITE to achieve an average integrated infidelity of  $\mathcal{I}=0.05$  over a time of T=1.5. Here, we define the infidelity with respect to the exact time-evolved state,  $|\psi(t)\rangle$ , that is

$$\mathcal{I}(T) = \frac{1}{T} \int_0^T \left( 1 - |\langle \phi(\boldsymbol{\theta}(t)) | \psi(t) \rangle|^2 \right) dt.$$
 (11)

In Fig. 2 we show the results for a varying number of qubits from n=4 to 10, where we adjust the depth as  $L=\lceil \ln n \rceil$ . The precise settings for each algorithm to achieve the target accuracy are listed in Appendix D.

We observe that, on average, SA-QITE requires about one order of magnitude less measurements than VarQITE to achieve the target accuracy, while both algorithms exhibit the same asymptotic scaling. Other variational time evolution algorithms based on optimizing a fidelity-based loss function, such as DualQITE [3], are also known to reduce the resources compared to VarQITE. However, since fidelity is difficult to measure to high accuracy on current devices, we here only focus on the stochastic approach.

![](_page_3_Figure_11.jpeg)

Fig. 2: Total number of measurements,  $M_{\rm total}$ , required to achieve the target accuracy for SA-QITE and VarQITE, along with the fraction of both resource counts. SA-QITE requires  $\approx 10\%$  of the number of measurements compared to VarQITE.

### B. Ground state approximation

If the exact imaginary-time trajectory is not required, but we are only interested in approximating ground states of a Hamiltonian, we can relax the number of samples N taken in each step. As an example, we minimize the energy of a Hamiltonian derived from a Max Cut problem with integer weights on a circular graph with n=15 nodes, shown in Fig. 3. The Hamiltonian is given by

$$H_C = w_1 \sum_{i=1}^n Z_i Z_{i+1 \mod n} + w_2 \sum_{i=1}^n Z_i Z_{(i+3) \mod n},$$

with  $w_1 = -w_2 = 20$ .

A widely-used approach to approximating the ground states of Hamiltonians obtained from a combinatorial optimization problem is using the Quantum Approximate Optimization Algorithm (QAOA) [21]. There, the energy is minimized in a variational optimization with a specific ansatz that is motivated by simulated annealing from a mixer Hamiltonian,  $H_M$ , whose ground state is easily prepared, to the target Hamiltonian,  $H_C$ . The ansatz is defined as

$$|\phi(\boldsymbol{\gamma}, \boldsymbol{\beta})\rangle = \left(\prod_{p=r}^{1} e^{-i\beta_{p}H_{M}} e^{-i\gamma_{p}H_{C}}\right) |+\rangle^{\otimes n},$$

with the mixer  $H_M = -\sum_{i=1}^n X_i$ , parameters  $\gamma, \beta \in \mathbb{R}^r$ , and we choose r=2. Since  $H_C$  contains only two-qubit Pauli-Z interactions, each term in the exponent  $\exp(-i\gamma_p H_C)$  can be

![](_page_4_Figure_0.jpeg)

Fig. 3: Solid lines mark interactions with  $w_1=20$ , dashed lines with  $w_2=-20$ . A optimal configuration is shown by filled and hollow circles, which indicate opposite qubit states. In total, there are 6 optimal configurations, which can be derived from the indicated solution by rotating the coloring (2 additional configurations) and inverting the colors (3 additional configurations).

realized with a two-qubit Pauli rotation,  $R_{ZZ}$ , on the interacting qubits. Similarly,  $\exp(-i\beta_p H_M)$  can be implemented with a layer of single-qubit  $R_X$  rotation gates.

The ground state of  $H_M$  is  $|+\rangle^{\otimes n}$ , which is obtained by starting the optimization from zero parameters,  $\beta = \gamma = 0$ . In this case, the ansatz becomes a Clifford circuit and we can efficiently evaluate the QGT and energy gradients classically to initialize the SA-QITE algorithm.

We compare SA-QITE against SPSA, as gradient-based, measurement-efficient optimizer, and QN-SPSA, which this work is based on. SPSA [13] minimizes the energy E using unbiased gradient estimates, as in Eq. (5), and for a learning rate  $\eta > 0$  the update step is given by

$$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - \eta \frac{E(\boldsymbol{\theta} + \epsilon \boldsymbol{\Delta}) - E(\boldsymbol{\theta} - \epsilon \boldsymbol{\Delta})}{2\epsilon} \boldsymbol{\Delta},$$

where, as before,  $\epsilon>0$  is a small perturbation and  $\Delta\sim \mathcal{U}(\{1,-1\}^d)$  is the perturbation direction. As a first-order gradient method, SPSA does not take into account the model sensitivity. QN-SPSA [10] corresponds to SA-QITE without the improvements introduced in this paper, that is, QN-SPSA uses a global averaging of the QGT samples, as in Eq. (6), and the identity as initial value,  $g^{(0)}=\mathbb{I}$ .

To ensure the optimizers converge towards the same minimum and avoid the saddle point at the zero initial point, we start the minimization from a small perturbation,  $\gamma^{(0)} = (10^{-3}, 10^{-3})$  and  $\beta^{(0)} = (10^{-2}, 10^{-2})$ . Each circuit evaluation uses  $8 \cdot 10^3$  measurements and we use a perturbation of  $\epsilon = 10^{-2}$  for the gradient approximations. For SPSA, we select the largest possible learning rate such that the algorithm converges consistently, which is the case for  $\eta = 5 \cdot 10^{-7}$ . Since SA-QITE approximates QNG, the update step is normalized with respect to the induced change in the model and we can

![](_page_4_Figure_8.jpeg)

![](_page_4_Figure_9.jpeg)

Fig. 4: (a) The energies E of the cost Hamiltonian as a function of total number of measurements M for SPSA and the natural gradient adaptations. (b) The probability  $p_{\text{optimal}}$  to sample one of the optimal states as a function of M.

choose a substantially larger learning rate, which translates to a "timestep" of  $\Delta_t = 10^{-3}$ .

As we are interested only in converging to the ground state, we relax the number of QGT and energy gradient samples to  $N_0 = 10$  in the first step, and reduce to  $N_k = \max\{1, \lfloor (0.9)^k N_0 \rfloor\}$  in the k-th iteration. The QGT momentum is set to  $\tau_1 = 0.99$ , but we use no gradient momentum ( $\tau_2 = 0$ ) to avoid bias once the optimization converged. Since we expect more noise in the QGT estimate as in the time-evolution case, we now solve the linear system with the diagonal shift of Eq. (8) with  $\delta = 100$ , which is roughly 0.5% of the magnitude of the largest eigenvalue of the initial QGT.

In Fig. 4(a) we show the energy of the  $H_C$  as a function of the total number of measurements M. In the narrow loss landscape, SPSA, as gradient-based optimizer, is only able to converge slowly, even though it uses less resources per iteration. The natural gradient approximations QN-SPSA and

SA-QITE, on the other hand, take into account the model sensitivity, which allows for a faster convergence. In particular we can see that, due to the accurate initial values of the QGT and energy gradient, SA-QITE initially performs better than QN-SPSA. Towards the minimum the QGT estimates of both these algorithms converge to the same values, which, in this example, leads to similar final energies.

Though the energy of the Hamiltonian is an indicator of solution quality, in a classical optimization problem we are often rather interested in the probability of sampling an optimal bitstring. In Fig. 4(b) we therefore show the probability  $p_{\text{optimal}}$  to sample one of the optimal states, as described in Fig. 3. The initial good performance of SA-QITE allows to amplify the solution probability most efficiently of the compared algorithms. To reach a 1% overlap, starting from the initial overlap of  $\sim 2^{-15}$ , for example, it requires only 64% of the measurements of SPSA or QN-SPSA.

#### IV. HARDWARE EXPERIMENTS

To test the near-term compatibility of SA-QITE, we scale the Ising Hamiltonian up to n=27 spins and execute the imaginary-time evolution on <code>ibm\_auckland</code>, which is one of the IBM Quantum Falcon processors [28]. Instead of spins on a chain, we consider nearest-neighbor interactions matching the topology of the device, shown in Fig. 5. This allows us to choose an ansatz that is both hardware-efficient, as it has low depth when compiled to basic instructions of the quantum processor and problem-inspired, as it reflects the interactions of the Hamiltonian.

The ansatz we use for this problem is similar to the one used in the numerical experiments, with the difference that we use a single entangling layer, L=1, and the pairwise connections exist between all qubit connections in the coupling map. This can be achieved with a CX depth of three. Depending on the device, executing a large number of CX depth in parallel, or executing certain connection pairs at the time, can cause frequency collisions. In these cases, increasing the CX depth beyond the requirement minimum can still be favorable.

The parameters for the Ising Hamiltonian are set to J=0.1, h=-1 and we integrate up to T=2 with a timestep of  $\Delta_t=10^{-2}$ . As before, the initial state is  $|0\rangle^{\otimes n}$ , which can be prepared with the variational ansatz by setting all initial parameter values to 0. We perform SA-QITE with M=1024 shots, N=10 samples per step, and momenta  $\tau_1=0.99$  and  $\tau_2=0$  and use no error mitigation. We use a Taylor expansion of the imaginary-time evolution operator as a classical reference calculation, as detailed in Appendix E.

The results of the imaginary-time evolution are presented in Fig. 6. We see that, without error mitigation, the energies calculated by SA-QITE follow the exact energies up to  $t \approx 0.5$ , but then reach a plateau at a constant offset of the reference calculation. However, if we evaluate the energies with the parameters obtained from the noisy hardware with an ideal statevector simulation instead, the energies are close to the exact solution. This suggests that SA-QITE was able to

![](_page_5_Picture_7.jpeg)

Fig. 5: The coupling map of the 27-qubit quantum processor. The colors of the connections indicate the order in which the CX layers are implemented to achieve a CX depth of three. The arrows are pointing from control to target qubit.

![](_page_5_Figure_9.jpeg)

Fig. 6: The energies for the imaginary-time evolution of the Ising model on 27 spins. While the non-error-mitigated values have an offset from the reference calculation, the exact evaluation of the parameter trajectory has a high accuracy, which is also reached by the error-mitigated points.

find the right parameter trajectory despite the present hardware noise, even though the evaluated energies have some errors.

To test the quality of the noisy parameters, we use error mitigation to evaluate specific energies to a higher accuracy on another 27-qubit chip; ibm\_peekskill [28]. We mitigate readout errors with the matrix-free measurement mitigation (M3) [29] and employ a zero-noise extrapolation (ZNE) [30] to further account for errors during the circuit execution. Since ZNE is prone to coherent noise, we average each energy measurement over a set of twirled circuits, which reduces the noise into stochastic noise and thus improves the extrapolation performance [31]. The workflow is summarized in Fig. 7 and the techniques and specific settings are detailed in Appendix E.

In Fig. 6, we see that error mitigation can improve the energy measurements significantly and approaches the ideal, statevector-based evaluation.

![](_page_6_Figure_0.jpeg)

Fig. 7: Error mitigation strategy for the energy measurements. Each CX gate is twirled using single-qubit Pauli operations before being folded  $\zeta=2m+1$  times for  $m\in\{0,1,2\}$ . The energies of the folded circuits are readout mitigated using a reduced calibration matrix  $\tilde{A}$ . Finally, the energies are extrapolated to obtain the energy estimate  $E(\zeta=0)$ .

# V. CONCLUSION

In this paper, we leverage a constant-cost sampling access to the QGT and energy gradient to implement a stochastic approximation of VarQITE, thereby reducing the prohibitive resource requirements. The proposed SA-QITE algorithm for imaginary-time evolution is a generalization of the existing QN-SPSA [10] optimization algorithm, and uses a momentum-based combination of samples, combined an initialization with accurate initial values of the QGT and energy gradient. These changes are also applicable if SA-QITE is used for optimization instead of time evolution, in which case the number of samples per step could be relaxed.

In our numerical experiments we see that, compared to VarQITE, our SA-QITE algorithm reduces the number of measurements required to achieve a target accuracy by about one order of magnitude. For larger, overparameterized circuit models, where the QGT is costly to evaluate but does not have a complex structure and can be efficiently sampled, we expect the advantage of SA-QITE to further increase. We have employed SA-QITE with a reduced number of samples for the optimization of a Max Cut Hamiltonian, where we showed that it is able to further improve on QN-SPSA, and is able to find optimal solutions at a lower number of measurements compared to other optimizers.

To demonstrate the near-term suitability of our algorithm, we use it to perform an imaginary-time evolution on a 27-qubit Ising model. There we find that even without error mitigation, the algorithm can determine the correct parameter dynamics. By investing additional resources for readout error mitigation and ZNE for individual points, we can retrieve energies close to the exact solution.

An open question for the family of stochastic variational algorithms of SA-QITE and QN-SPSA is how the number of samples could be chosen adaptively. This would allow for increasing the accuracy at times when the parameter dynamics are difficult to capture and using fewer resources if

the samples have only a small impact on the current estimate. Another interesting question is how the method introduced here performs for adaptive circuit models, such as in ADAPT-VQE, where the number of parameters is small compared to other hardware-efficient models.

In conclusion, sampling from the QGT and energy gradients allows to reduce the number of measurements compared to VarQITE significantly, and is a suitable approach to implement imaginary-time evolution on near-term quantum computers. Scalable algorithms for current devices are one integral building block for solving practically relevant problems and pave the way to tackle remaining open questions, such as the construction of suitable variational circuit models.

#### ACKNOWLEDGMENTS

We thank Almudena Carrera Vazquez, Daniel Egger, Caroline Tornow, Max Rossmannek, Paul Nation and Christopher J. Wood for helpful discussions on the error mitigation techniques applied in this paper. We are also grateful for the continuous support in the IBM Quantum stack provided by Jessie Yu, Kevin Tian, Daniel Kaulen, Diego Ristè, Maika Takita, and the whole IBM Quantum team.

We acknowledge the use of IBM Quantum services for this work. The views expressed are those of the authors, and do not reflect the official policy or position of IBM or the IBM Quantum team.

IBM, the IBM logo, and ibm.com are trade marks of International Business Machines Corp., registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. The current list of IBM trademarks is available at https://www.ibm.com/legal/copytrade.

# REFERENCES

- [1] S. McArdle, T. Jones, S. Endo, Y. Li, S. C. Benjamin, and X. Yuan, "Variational ansatz-based quantum simulation of imaginary time evolution," *npj Quantum Information*, vol. 5, no. 1, p. 75, Dec. 2019. [Online]. Available: http://www.nature.com/articles/s41534-019-0187-2
- [2] J. C. Getelina, N. Gomes, T. Iadecola, P. P. Orth, and Y.-X. Yao, "Adaptive variational quantum minimally entangled typical thermal states for finite temperature simulations," arXiv:2301.02592, Jan. 2023. [Online]. Available: http://arxiv.org/abs/2301.02592
- [3] J. Gacon, J. Nys, R. Rossi, S. Woerner, and G. Carleo, "Variational quantum time evolution without the quantum geometric tensor," 2023, arXiv. [Online]. Available: http://arxiv.org/abs/2303.12839
- [4] C. Zoufal, A. Lucchi, and S. Woerner, "Variational quantum Boltzmann machines," *Quantum Machine Intelligence*, vol. 3, no. 1, p. 7, Feb. 2021. [Online]. Available: https://doi.org/10.1007/s42484-020-00033-7
- [5] C. Zoufal, R. V. Mishmash, N. Sharma, N. Kumar, A. Sheshadri, A. Deshmukh, N. Ibrahim, J. Gacon, and S. Woerner, "Variational quantum algorithm for unconstrained black box binary optimization: Application to feature selection," *Quantum*, vol. 7, p. 909, Jan. 2023. [Online]. Available: https://doi.org/10.22331/q-2023-01-26-909
- [6] S. Lloyd, "Universal Quantum Simulators," Science, vol. 273, no. 5278, pp. 1073–1078, Aug. 1996. [Online]. Available: https://www.science.org/doi/10.1126/science.273.5278.1073
- [7] M. Motta, C. Sun, A. T. K. Tan, M. J. O. Rourke, E. Ye, A. J. Minnich, F. G. S. L. Brandao, and G. K.-L. Chan, "Determining eigenstates and thermal states on a quantum computer using quantum imaginary time evolution," *Nature Physics*, vol. 16, no. 2, pp. 205–210, Feb. 2020. [Online]. Available: http://arxiv.org/abs/1901.07653
- [8] X. Yuan, S. Endo, Q. Zhao, Y. Li, and S. C. Benjamin, "Theory of variational quantum simulation," *Quantum*, vol. 3, p. 191, Oct. 2019. [Online]. Available: https://doi.org/10.22331/q-2019-10-07-191

- [9] J. Stokes, J. Izaac, N. Killoran, and G. Carleo, "Quantum natural gradient," *Quantum*, vol. 4, p. 269, May 2020.
- [10] J. Gacon, C. Zoufal, G. Carleo, and S. Woerner, "Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information," *Quantum*, vol. 5, p. 567, Oct. 2021. [Online]. Available: https://doi.org/10.22331/q-2021-10-20-567
- [11] IBM Quantum, "IBM Unveils Breakthrough 127 Qubit Quantum Processor," 2021. [Online]. Available: https://newsroom.ibm.com/2021-11-16-IBM-Unveils-Breakthrough-127-Qubit-Quantum-Processor
- [12] ——, "IBM Unveils 400 Qubit Plus Quantum Processor and Next Generation IBM Quantum System Two," 2022. [Online]. Available: https://newsroom.ibm.com/2022-11-09-IBM-Unveils-400-Qubit-Plus-Quantum-Processor-and-Next-Generation-IBM-Quantum-System-Two
- [13] J. C. Spall, "Accelerated second-order stochastic optimization using only function measurements," in *Proceedings of the 36th IEEE Conference* on *Decision and Control*, vol. 2, Dec. 1997, pp. 1417–1424 vol.2, iSSN: 0191-2216.
- [14] M. Benedetti, M. Fiorentini, and M. Lubasch, "Hardware-efficient variational quantum algorithms for time evolution," *Phys. Rev. Res.*, vol. 3, p. 033083, Jul 2021. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevResearch.3.033083
- [15] S.-H. Lin, R. Dilip, A. G. Green, A. Smith, and F. Pollmann, "Real-and imaginary-time evolution with compressed quantum circuits," PRX Quantum, vol. 2, p. 010342, Mar 2021. [Online]. Available: https://link.aps.org/doi/10.1103/PRXQuantum.2.010342
- [16] M. Schuld, V. Bergholm, C. Gogolin, J. Izaac, and N. Killoran, "Evaluating analytic gradients on quantum hardware," *Phys. Rev. A*, vol. 99, p. 032331, Mar 2019. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevA.99.032331
- [17] H. Buhrman, R. Cleve, J. Watrous, and R. de Wolf, "Quantum finger-printing," Phys. Rev. Lett., vol. 87, no. 16, p. 167902, Sep 2001.
- [18] L. Cincio, Y. Subaşı, A. T. Sornborger, and P. J. Coles, "Learning the quantum algorithm for state overlap," Nov. 2018, arXiv. [Online]. Available: http://arxiv.org/abs/1803.04114
- [19] A. Elben, B. Vermersch, C. F. Roos, and P. Zoller, "Statistical correlations between locally randomized measurements: A toolbox for probing entanglement in many-body quantum states," *Phys. Rev. A*, vol. 99, no. 5, May 2019
- [20] V. Havlíček et al., "Supervised learning with quantum-enhanced feature spaces," *Nature*, vol. 567, no. 7747, pp. 209–212, Mar. 2019.
- [21] E. Farhi, J. Goldstone, and S. Gutmann, "A quantum approximate optimization algorithm," 2014, arXiv. [Online]. Available: http://arxiv.org/abs/1411.4028
- [22] P. J. J. O'Malley, R. Babbush, I. D. Kivlichan, J. Romero, J. R. McClean, R. Barends, J. Kelly, P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, A. G. Fowler, E. Jeffrey, E. Lucero, A. Megrant, J. Y. Mutus, M. Neeley, C. Neill, C. Quintana, D. Sank, A. Vainsencher, J. Wenner, T. C. White, P. V. Coveney, P. J. Love, H. Neven, A. Aspuru-Guzik, and J. M. Martinis, "Scalable quantum simulation of molecular energies," *Phys. Rev. X*, vol. 6, p. 031007, Jul 2016. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevX.6.031007
- [23] P. K. Barkoutsos, J. F. Gonthier, I. Sokolov, N. Moll, G. Salis, A. Fuhrer, M. Ganzhorn, D. J. Egger, M. Troyer, A. Mezzacapo, S. Filipp, and I. Tavernelli, "Quantum algorithms for electronic structure calculations: Particle-hole hamiltonian and optimized wave-function expansions," *Phys. Rev. A*, vol. 98, p. 022322, Aug 2018. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevA.98.022322
- [24] J. Romero, R. Babbush, J. R. McClean, C. Hempel, P. J. Love, and A. Aspuru-Guzik, "Strategies for quantum computing molecular energies using the unitary coupled cluster ansatz," *Quantum Science and Technology*, vol. 4, no. 1, p. 014008, oct 2018. [Online]. Available: https://dx.doi.org/10.1088/2058-9565/aad3e4
- [25] L. Hackl, T. Guaita, T. Shi, J. Haegeman, E. Demler, and J. I. Cirac, "Geometry of variational methods: dynamics of closed quantum systems," *SciPost Phys.*, vol. 9, p. 048, 2020. [Online]. Available: https://scipost.org/10.21468/SciPostPhys.9.4.048
- [26] S.-i. Amari, "Natural Gradient Works Efficiently in Learning," *Neural Computation*, vol. 10, no. 2, pp. 251–276, 1998. [Online]. Available: http://www.mitpressjournals.org/doi/10.1162/089976698300017746
- [27] Qiskit contributors, "Qiskit: An open-source framework for quantum computing," 10.5281/zenodo.2562110, 2023.
- [28] IBM Quantum, 2021, https://quantum-computing.ibm.com/.

- [29] P. D. Nation, H. Kang, N. Sundaresan, and J. M. Gambetta, "Scalable mitigation of measurement errors on quantum computers," PRX Quantum, vol. 2, p. 040326, Nov 2021. [Online]. Available: https://link.aps.org/doi/10.1103/PRXQuantum.2.040326
- [30] T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, and W. J. Zeng, "Digital zero noise extrapolation for quantum error mitigation," in 2020 IEEE International Conference on Quantum Computing and Engineering (OCE), 2020, pp. 306–316.
- [31] Y. Kim, C. J. Wood, T. J. Yoder, S. T. Merkel, J. M. Gambetta, K. Temme, and A. Kandala, "Scalable error mitigation for noisy quantum circuits produces competitive expectation values," *Nature Physics*, Feb. 2023. [Online]. Available: https://doi.org/10.1038/s41567-022-01914-3
- [32] D. Gottesman, "The Heisenberg representation of quantum computers," Group 22: Proceedings of the XXII International Colloquium on Group Theoretical Methods in Physics, 6 1998. [Online]. Available: https://www.osti.gov/biblio/319738
- [33] M. J. D. Powell, A Direct Search Optimization Method That Models the Objective and Constraint Functions by Linear Interpolation. Springer Netherlands, 1994.
- [34] S. Endo, S. C. Benjamin, and Y. Li, "Practical quantum error mitigation for near-future applications," *Phys. Rev. X*, vol. 8, p. 031027, Jul 2018. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevX.8.031027

#### APPENDIX A

# SAMPLING ERROR FOR THE QGT AND EVOLUTION GRADIENT

In this section, we investigate the convergence of the QGT and evolution gradient samples,  $\hat{g}_N$  and  $\hat{b}_N$ , as a function of the number of samples N. We measure the convergence as error in the  $\ell_2$  norm, i.e.,

$$\|\hat{g}_N - g\|_2 = \sqrt{\sum_{i,j=1}^d ((\hat{g}_N)_{ij} - g_{ij})^2},$$

and analogously for  $\hat{\boldsymbol{b}}_N$ .

We calculate the errors for up to  $N=10^5$  samples for the 8-qubit Ising Hamiltonian and variational ansatz used in the numerical experiments in Section III, at the initial point  $\theta=0$ . The errors are presented in Fig. 8, for both a statevector-based evaluation of the circuits and for a shot-based evaluation with sampling statistics. Both lines show the expected Monte Carlo convergence of  $\mathcal{O}(N^{-1/2})$ , however the finite readout accuracy in the shot-based case limits the achievable error. Therefore, increasing the number of samples beyond the shot-noise limit does not further improve the estimator accuracy.

### APPENDIX B

### CLIFFORD SIMULATION OF GRADIENT CIRCUITS

If the ansatz circuit at the initial parameter values,  $|\phi(\theta(0))\rangle$ , is a Clifford circuit, we can efficiently evaluate the its expectation values and gradients on a classical computer [32]. This would allow the efficient evaluation of the initial QGT and evolution gradient, which we use in SA-QITE.

A large class of hardware-efficient circuits, including the ones used in this work, or problem-inspired circuits, such as the excitation-preserving or Trotterization circuits, are based on controlled Pauli gates and single-qubit Pauli rotations. The controlled Paulis CX, CY, and CZ themselves belong to the Clifford group and the rotation gates become Clifford gates

![](_page_8_Figure_0.jpeg)

Fig. 8: The sampling error of  $\hat{g}_N$  and  $\hat{\boldsymbol{b}}_N$  measured in  $\ell_2$  distance to the exact values. The statevector-based evaluations  $(M \to \infty)$  use a perturbation of  $\epsilon = 10^{-2}$  and the measurement-based evaluations (M = 1024) use  $\epsilon = 10^{-1}$ .

for certain rotation angles. For multiples of  $\pi/2$ , they can be expressed in terms of the Clifford gates I, S, X and H:

$$\begin{split} R_X\left(\frac{\pi}{2}\right) &= S^\dagger H S^\dagger \\ R_Y\left(\frac{\pi}{2}\right) &= X H \\ R_Z\left(\frac{\pi}{2}\right) &= H R_X\left(\frac{\pi}{2}\right) H. \end{split}$$

Since  $R_{X,Y,Z}(k\pi/2) = R_{X,Y,Z}^k(\pi/2)$ , for  $k \in \mathbb{Z}$  this shows the general case of any multiple of  $\pi 2$ .

To calculate the gradient

$$\left| \frac{\partial}{\partial \theta_i} \phi(\boldsymbol{\theta}) \right\rangle = \frac{\partial}{\partial \theta_i} \prod_{k=d}^{1} U_k(\theta_k) |0\rangle$$
$$= U_d(\theta_d) \cdots \frac{\partial U_i}{\partial \theta_i} \cdots U_1(\theta_1) |0\rangle$$

we replace the unitary  $U_i(\theta_i)$  with its derivative  $\partial_i U_i(\theta_i)$ . Since, for the Pauli rotations, the derivative remains Clifford, the elements of the QGT and evolution gradient, defined in Eqs. (2) and (3), can be calculated efficiently.

Other options to evaluate the gradients include using a parameter-shift rule with a shift of  $\pi/2$  from the initial point, or the linear-combination of unitaries method [16], which only adds Clifford gates to the circuit.

# APPENDIX C REGULARIZATION COMPARISON

In this section, we compare the different methods to solve the noisy linear system

$$\bar{g}^{(k)}\dot{\boldsymbol{\theta}} = \bar{\boldsymbol{b}}^{(k)}.$$

We perform SA-QITE for the Ising Hamiltonian of Section III for 8 qubits, using either the diagonal shift (Eq. 8) or the stable-subspace (Eq. (9)) method to solve the linear system in each timestep. For a numerically stable solution of the linear system with the diagonal shift, we rewrite the equation as convex, quadratic program, that is

$$\dot{\boldsymbol{\theta}} = \operatorname*{argmin}_{\boldsymbol{x}} \frac{\boldsymbol{x}^T (\bar{g}^{(k)} + \delta \mathbb{I}) \boldsymbol{x}}{2} - \boldsymbol{x}^T \boldsymbol{b},$$

and solve it with the classical optimization routine COBYLA [33].

Figure 9 shows the fidelity F at each timestep t and the integrated infidelity  $\mathcal{I}$  for the two methods for different regularization constants  $\delta$ . The stable-subspace technique provides the best results overall at  $\delta = 10^{-1}$ . In addition, it seems to be the more stable because the integrated infidelity does not suffer from the same sudden increase at a larger regularization constant. We, therefore, use the stable subspace technique for solving the linear systems in this work.

![](_page_8_Figure_16.jpeg)

Fig. 9: Fidelity F compared to the exact time-evolved state at each time t, and integrated infidelity  $\mathcal{I}$  for different linear system solvers and regularizations. In the stable subspace method (green), the regularization determines the eigenvalue cutoff threshold and in the diagonal shift technique (blue) the regularization equals the coefficient of the identity added to the QGT.

# APPENDIX D BENCHMARK SETTINGS

This section includes more details for the resource estimation in Section III. In Fig. 10 we show the achieved accuracies, measured in the integrated infidelity  $\mathcal{I}$ , for SA-QITE and VarQITE for the different numbers of qubits. The algorithm settings were each chosen, such that the accuracy is a close as possible to the threshold of  $\mathcal{I} \leq 0.05$ , and are displayed in Table I.

![](_page_9_Figure_1.jpeg)

Fig. 10: The mean and standard deviation of the integrated infidelity  $\mathcal{I}$  for SA-QITE and VarQITE.

| n  | M                          | $\delta$ | n  | M   | N   | $\tau_1$ | $\tau_2$ | $\delta$ |
|----|----------------------------|----------|----|-----|-----|----------|----------|----------|
| 4  | 128                        | 0.05     | 4  | 128 | 10  | 0.99     | 0.7      | 0.05     |
| 6  | 400                        | 0.05     | 6  | 256 | 20  | 0.99     | 0.9      | 0.05     |
| 8  | 1024                       | 0.01     | 8  | 512 | 75  | 0.99     | 0.7      | 0.05     |
| 10 | 128<br>400<br>1024<br>2048 | 0.05     | 10 | 800 | 250 | 0.99     | 0.7      | 0.05     |

(a) VarQITE settings

(b) SA-QITE settings

TABLE I: Algorithm settings for the resource estimations, including the number of qubits n, the number of measurements per basis M, the number of samples for the QGT and energy gradient N, the momenta  $\tau_1$  and  $\tau_2$ , and the cutoff  $\delta$  in the stable subspace solver.

# APPENDIX E 27-QUBIT EXPERIMENT

# A. Classical reference solution

For 27 qubits, computing the classical reference solution with a simple matrix exponential already requires too much memory to execute on an ordinary computer. Instead, to compute a classical reference solution, we Taylor-expand the imaginary-time evolution operator and normalize the state after each timestep. The update rule for the state  $|\psi(t)\rangle \in \mathbb{C}^{2^n}$ , is, then, given by

$$|\tilde{\psi}(t + \Delta_t)\rangle = (\mathbb{I} - \Delta_t H) |\psi(t)\rangle$$
$$|\psi(t + \Delta_t)\rangle = \frac{|\tilde{\psi}(t + \Delta_t)\rangle}{\||\tilde{\psi}(t + \Delta_t)\rangle\|_2},$$

where  $\mathbb{I}$  is the  $2^n \times 2^n$  dimensional identity matrix. We run the evolution for decreasing timesteps  $\Delta_t$  and consider the reference solution as converged, if a smaller timestep does no longer changes the solution. In the 27-qubit experiment, this was reached for  $\Delta_t = 10^{-3}$ .

#### B. Readout error mitigation

Errors during the readout of qubit states are particularly dominating for shallow quantum circuits, like the circuit with a CX depth of three used in the hardware experiments in this work. To mitigate these errors in a scalable approach, we use the M3 error mitigation [29]. In contrast to standard readout error mitigation approaches, such as a complete or tensored measurement mitigation, M3 corrects the measurements only in the subspace of measured bitstrings.

Assume the measured probability distribution over n qubits and M measurements is p, where the k-th element describes the probability to measure the binary representation of k. Then M3 computes the mitigated quasi-probability distribution q as

$$q = \tilde{A}p,$$
 (12)

with the truncated transfer matrix  $\tilde{A}$ . Note that q represents a quasi-probability distribution and can have negative vector elements, but still sums up to 1. To construct  $\tilde{A}$ , we start from the the  $2^n \times 2^n$ -dimensional tensored transfer matrix  $A = C_n \otimes \cdots \otimes C_1$ , which is built from n individual single-qubit calibration matrices of the form

$$C_{j} = \begin{pmatrix} p_{0 \to 0}^{(j)} & p_{0 \to 1}^{(j)} \\ p_{1 \to 0}^{(j)} & p_{1 \to 1}^{(j)} \end{pmatrix}, \tag{13}$$

where  $p_{a \to b}^{(j)}$  denotes the probability that qubit j is initialized in state  $|a\rangle$  and is measured to be in  $|b\rangle$ . The truncated matrix  $\tilde{A}$  is obtained from A by taking into account only indices, that are present in the noisy measurements p, that is

$$\tilde{A} = (A_{ij})_{i,j \in \{k: \ p_k > 0\}}$$
 (14)

Since the experiments in this paper used M=1000 shots for 27 qubits,  $\tilde{A}$  has at most dimension  $1000\times 1000$ , which is small enough to efficiently solve the linear system for the quasi-probabilities q. For a larger number of shots,  $\tilde{A}$  can be further truncated to include only transfers of bitstrings within a certain Hamming distance.

# C. Zero-noise extrapolation

Zero-noise extrapolation (ZNE) is a generic error mitigation technique, which artificially amplifies noise sources to then extrapolate to the zero-noise limit. In this work, we apply ZNE to mitigate the errors introduced by two-qubit gates, in our case CX gates, as these are the main error sources during the quantum circuit execution. We artifically amplify the CX noise by adding an additional even number of CX operations, which logically implement an identity but increase the error rate. Other amplifications are possible, such as the device-specific microwave pulse stretching, though here we focus on the identity-insertion as it is device agnostic and does not require additional pulse calibrations.

For a set of repetition levels  $m \in \mathbb{N}$ , we replace each single CX in the original circuit by

$$CX \to CX^{2m+1}$$
.

![](_page_10_Figure_0.jpeg)

Fig. 11: Zero-noise extrapolation for the energies at different times t. The figures show 5 independent repetitions of the extrapolation. Each interpolation point  $E(\zeta)$  for  $\zeta \in \{1,3,5\}$  is obtained by averaging over 25 Pauli Twirling instances and with M3 readout error mitigation. The black dashed line shows the ideal, statevector-based energy.

and denote the resulting measured energy as  $E(\zeta)$ , where  $\zeta=2m+1$  is the number of applied CX gates. As we expect the noise to increase exponentially in this gate repetition [34], we then fit the measured energies for different  $\zeta$  with an exponential model

$$E(\zeta; a, b, c) = a + be^{c\zeta},$$

and extrapolate the ZNE estimate at  $\zeta = 0$ .

To reduce coherent errors in the CX applications, which can lead to unphysical extrapolations [31], we combine ZNE with Pauli Twirling. Since on our the device, <code>ibm\_peekskill</code>, the single-qubit gate errors are much lower than the two-qubit gate errors, Pauli Twirling can be implemented by sandwiching each logical CX gate in between single-qubit Pauli operations, that preserve the logical operation.

In Fig. 11 we show the interpolation energies  $\{E(\zeta):\zeta\in\{1,3,5\}\}$  and the extrapolated value at  $\zeta=0$  for states at different times t. Each energy measurement includes M3 readout error mitigation and is averaged over  $N_{\rm twirl}=25$  Pauli Twirling instances, where each individual expectation value is measured with M=1000 shots per basis.