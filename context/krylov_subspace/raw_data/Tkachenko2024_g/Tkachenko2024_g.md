![](_page_0_Picture_1.jpeg)

![](_page_0_Picture_2.jpeg)

# **PAPER • OPEN ACCESS**

# Quantum Davidson algorithm for excited states

To cite this article: Nikolay V Tkachenko et al 2024 Quantum Sci. Technol. 9 035012

View the <u>article online</u> for updates and enhancements.

# You may also like

- <u>Sequence of penalties method to study</u> <u>excited states using VQE</u> R Carobene, S Barison and A Giachero
- Quantum simulation of excited states from parallel contracted quantum eigensolvers
   Carlos L Benavides-Riveros, Yuchen
   Wang, Samuel Warren et al.
- Challenging excited states from adaptive quantum eigensolvers: subspace expansions vs. state-averaged strategies Harper R Grimsley and Francesco A Evangelista

# Quantum Science and Technology

![](_page_1_Picture_4.jpeg)

#### **OPEN ACCESS**

#### RECEIVED

5 September 2023

#### REVISED

23 January 2024

### ACCEPTED FOR PUBLICATION

4 April 2024

#### PURIISHED

22 April 2024

Original Content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence

Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

![](_page_1_Picture_16.jpeg)

#### **PAPER**

# Quantum Davidson algorithm for excited states

Nikolay V Tkachenko<sup>1,3,4</sup>, Lukasz Cincio¹, Alexander I Boldyrev³, Sergei Tretiak¹, Pavel A Dub², and Yu Zhang<sup>1,\*</sup>

- Theoretical Division, Los Alamos National Laboratory, Los Alamos, NM 87545, United States of America
- Chemistry Division, Los Alamos National Laboratory, Los Alamos, NM 87545, United States of America
- Department of Chemistry and Biochemistry, Utah State University, Logan, UT 84322, United States of America
- Now at College of Chemistry, University of California, Berkeley.
- Now at Schrödinger, Inc.
- Author to whom any correspondence should be addressed.

E-mail: zhy@lanl.gov and pavel.dub@schrodinger.com

Keywords: quantum computation, quantum chemistry, excited state, quantum Krylov subspace, Davidson algorithm Supplementary material for this article is available online

#### Abstract

Excited state properties play a pivotal role in various chemical and physical phenomena, such as charge separation and light emission. However, the primary focus of most existing quantum algorithms has been the ground state, as seen in quantum phase estimation and the variational quantum eigensolver (VQE). Although VQE-type methods have been extended to explore excited states, these methods grapple with optimization challenges. In contrast, the quantum Krylov subspace (QKS) method has been introduced to address both ground and excited states, positioning itself as a cost-effective alternative to quantum phase estimation. However, conventional QKS methodologies depend on a pre-generated subspace through real or imaginary-time evolutions. This subspace is inherently expansive and can be plagued with issues like slow convergence or numerical instabilities, often leading to relatively deep circuits. Our research presents an economic QKS algorithm, which we term the quantum Davidson (QDavidson) algorithm. This innovation hinges on the iterative expansion of the Krylov subspace and the incorporation of a pre-conditioner within the Davidson framework. By using the residues of eigenstates to expand the Krylov subspace, we manage to formulate a compact subspace that aligns closely with the exact solutions. This iterative subspace expansion paves the way for a more rapid convergence in comparison to other QKS techniques, such as the quantum Lanczos. Using quantum simulators, we employ the novel QDavidson algorithm to delve into the excited state properties of various systems, spanning from the Heisenberg spin model to real molecules. Compared to the existing QKS methods, the QDavidson algorithm not only converges swiftly but also demands a significantly shallower circuit. This efficiency establishes the QDavidson method as a pragmatic tool for elucidating both ground and excited state properties on quantum computing platforms.

### 1. Introduction

Computing the ground and excited state properties of intricate many-body systems is a cornerstone of quantum physics and chemistry. Despite the importance, this endeavor demands substantial computational power due to the factorial growth of the full many-body wavefunction's solution space as the system size (represented by the number of electrons and basis functions) [1–3]. As a result, classical quantum chemistry techniques such as Hartree–Fock (HF), density functional theory [4, 5], tensor network methods [6, 7] that optimize the wavefunction in the form of a matrix product states, selected configuration interaction (CI) [8, 9] that iteratively expands the CI spaces, and coupled-cluster theory truncated at finite orders [10] have been conceived to bypass the direct formulation of full many-body wavefunctions. However, these techniques invariably employ truncations or approximations and are limited to a certain size.

Since the 1980s, quantum computers (QCs) that leverage the power of quantum entanglement have been proposed as the ideal platforms for simulating quantum mechanics [11, 12]. Advancing into the noisy intermediate-scale quantum (NISQ) era [13], quantum computing has shown its potential with the demonstration of quantum advantages in well-defined tasks [14]. Electronic structure problems, crucial to various scientific disciplines, emerge as one of the most promising and immediate applications of QCs [1–3, 15]. Numerous quantum algorithms have been proposed for calculating the ground state of quantum many-body systems on QC since the advent of quantum phase estimation [16, 17]. However, the inherently noisy nature of NISQ devices necessitates hybrid quantum—classical algorithms with shallower circuits. To this end, the variational quantum eigensolver (VQE) that leverages the power of variational principle and classical optimization was conceived accordingly [18]. The VQE scheme deploys the parameterized wavefunction(or ansatz) and the corresponding energy measurement on QCs and then uses classical algorithms for variational energy minimization. VQE algorithm has been performed on various quantum architectures such as photons [18], superconducting qubits [19, 20], and trapped ions [21]. Since then, many algorithms have been proposed to improve the performance further or reduce the quantum resource requirements of VQE [22–34].

Despite the extensive development of quantum algorithms for electronic structure problems, the majority pivots on ground state properties. However, many photophysical and photochemical critical processes, including energy transfer [35], bond dissociation [36], light emission and nonadiabatic dynamics [37, 38], revolve around electronically excited states. Which necessitates the development of quantum algorithms for excited states. One straightforward way is to extend VQE for excited states by introducing certain constraints [39–45]. Despite the success and impact of VQE algorithms, they suffer from optimization problems. The optimization process in VQE is challenging due to the high nonlinearity of the energy and stochastic errors [46] and is compounded by the inclusion of multiple excited states.

Alternatively, the other emerging direction for calculating excited states on QC is based on the quantum subspace, showcased by quantum subspace expansion [43, 47–50], non-orthogonal VQE [51], equation of motions [52, 53], and the quantum Krylov subspace (QKS) framework inspired by its classical analogs [54–58]. Current QKS methods utilize either real or imaginary time [55, 56] evolutions to generate the Krylov subspace, which then is used to sample the low-lying spectrum of the Hamiltonian  $\hat{H}$ . In particular, the quantum Lanczos (QLanczos) algorithm [56] that engages a basis of correlated states generated from the imaginary-time propagation [59, 60] has been proposed. Even though the QKS methods remove the optimization problems of the VQE algorithms, the current QKS usually requires a relatively deep circuit due to the trotter expansion of the real/imaginary time evolution and a larger number of iterations for convergence. Moreover, the pre-generated Krylov subspace from the time evolution is not necessarily compact.

This research introduces the Quantum Davidson (QDavidson) algorithm, an economic QKS method that efficiently crafts a compact Krylov subspace. By harnessing the Residue and a pre-conditioner, Davidson's algorithm restricts the subspace search near the exact state, guaranteeing brisk convergence [61]. Compared to its classical counterpart, our strategy offloads subspace expansion to the QC, eliminating the explicit construction of full many-body wavefunctions on classical computers, leading to the speedup in the subspace projection. Compared to the existing QKS method, QDavidson's rapid convergence results in a much shallower circuit, making it potentially more noise resilient.

# 2. Theory

# 2.1. Krylov subspace and classical Davidson algorithm

In linear algebra, an order-r Krylov subspace generated by a matrix H and a reference vector b is the linear subspace spanned by the images of b under the first r powers of H [62]. This subspace is denoted as  $\mathcal{K}_r(H,b) \equiv \{b,Hb,H^2b,\cdots,H^{r-1}b\}$ . The Krylov subspace has been extensively utilized in numerical algorithms for finding solutions to high-dimensional matrices, such as the generalized minimal residual method, Davidson, and quasi-minimal residual algorithms [61].

In quantum chemistry, the iterative Krylov subspace  $\mathcal{K}_r(\hat{H},|\psi\rangle)$  is especially valuable for identifying low-lying states in electronic structure theory since the number of such states is typically much smaller than the size of the solution space. Various versions of the Davidson algorithm have been developed to enhance convergence by designing efficient pre-conditioners [63–65]. Furthermore, the Davidson algorithm has been generalized to use non-orthogonal Krylov spaces [66]. The flowchart of a standard classical Davidson algorithm is presented in algorithm S1 of the supplementary information (SI). Despite its computational

efficiency, the generation of the subspace  $\hat{H}^r|\psi\rangle$  remains a significant bottleneck in the Davidson algorithm and becomes computationally intensive on classical computers as the dimension of  $\hat{H}$  grows.

#### 2.2. QDavidson algorithm

In this study, we introduce a quantum counterpart of the Davidson algorithm, termed QDavidson, that harnesses QCs to mitigate the scaling challenges of generating the Krylov subspace. Compared to the traditional Krylov method, the QKS scheme encodes arbitrarily complex states on quantum circuits, where the matrix's projection into the subspace is measured. The benefits of QKS methods over VQE-based techniques for computing low-lying excited states include (1) an independent ansatz for each reference state with a streamlined quantum circuit and (2) the elimination of the intricate optimization process. In [56], quantum imaginary time evolution (QITE) is conducted using the Trotter decomposition of the evolution operator  $e^{-\hat{H}t}$  and mapping each Trotter step into a unitary. Subsequently, the QLanczos algorithm is introduced in the Krylov space derived from QITE snapshots. However, the QKS arising from sequential time evolution lacks compactness. Here, we develop the QDavidson algorithm to create a compact QKS set, yielding a more efficient and numerically stable realization of the QKS approach.

Instead of pre-generating the subspace through real or imaginary-time evolution, the QDavidson framework adaptively expands the QKS, keeping the subspace growth closely with the true eigenspace. Initially, orthogonal states serve as the reference. HF  $|\phi_0\rangle$ , single-excitation configurations  $|\phi_i^a\rangle = a_a^\dagger a_i |\phi_0\rangle$ , and CI single (CIS) states  $\{\sum_{ia} C_{ia} |\phi_i^a\rangle\}$ , which are efficiently computed on classical computers, are natural choices for initial reference states. The set of these initial reference states is denoted as  $\{|\psi_k\rangle\}$ . Within the QKS framework, each basis (subsequently called a Krylov vector) within the Krylov subspace of the jth Davidson iteration assumes the following ansatz,

$$|\psi_{\rm K}\rangle = \hat{U}_{\rm K}^j \sum_{\rm I} C_{\rm KI} |\phi_{\rm I}\rangle \equiv \hat{U}_{\rm K}^j |\Phi_{\rm K}\rangle.$$
 (1)

Here, multiple reference states (i.e. a linear combination of HF/CIS states) are utilized where  $|\phi_I\rangle$  denote a single determinant. The entanglers  $\hat{U}_K^i$  arise from the Krylov space expansion and introduce correlations that extend beyond the initial states. In the case of QDavidson, the entanglers take the form  $\hat{U}_K^i = \mathrm{e}^{-\mathrm{i}\hat{A}_K^i\delta\tau}$ , where the operator  $\hat{A}_K^j$  is determined by mapping the non-unitary operator  $\mathrm{e}^{-(\hat{H}-E_K^i)\delta\tau}$  into a unitary form. The further details of  $\hat{U}_K^i$  will be elaborated later, with  $\hat{U}_K^1 = 1$  for the initial iteration.

The general ground and excited states, denoted  $|\Psi_I\rangle$ , can be expressed as linear combinations of the Krylov vectors,

$$|\Psi_{\rm I}\rangle = \sum_{\rm K} V_{\rm KI} |\psi_{\rm K}\rangle. \tag{2}$$

Therefore, the challenge of finding the ground state and low-lying excited states, represented by the equation  $\hat{H}|\Psi\rangle=E|\Psi\rangle$ , can be recast as the generalized eigenvalue problem HV=ESV within the Krylov subspace. Here, H denotes the Hamiltonian matrix within the Krylov subspace, as described by equation (1),

$$H_{KL} = \langle \psi_K | \hat{H} | \psi_L \rangle = \langle \Phi_K | \hat{U}_V^{\dagger} \hat{H} \hat{U}_L | \Phi_L \rangle. \tag{3}$$

Additionally, S represents the overlap matrix among Krylov vectors, with individual elements given by,

$$S_{KL} = \langle \psi_K | \psi_L \rangle = \langle \Phi_K | \hat{U}_K^{\dagger} \hat{U}_L | \Phi_L \rangle. \tag{4}$$

Considering each Krylov vector may contain distinct entanglers and reference states, the matrix elements of both H and S are measured on QCs using an ancillary qubit and the Hadamard test [51, 55], as illustrated in figure 1. Once the elements of H and S are measured, the generalized eigenvalue problem HV = ESV can be trivially solved on classical computers due to the small dimensionality of the Krylov subspace.

After solving for the approximate excited states in the current subspace, the residues of these approximate states can be computed as

$$|R_{\rm I}\rangle = \hat{H}|\Psi_{\rm I}\rangle - E_{\rm I}|\Psi_{\rm I}\rangle = (\hat{H} - E_{\rm I})\sum_{\rm K} V_{\rm KI}|\psi_{\rm K}\rangle.$$
 (5)

The norm of the residue can be measured on QCs similarly to the  $H_{KL}$  measurement,

![](_page_4_Figure_3.jpeg)

**Figure 1.** Schematic diagram of modified Hadamard test for measuring off-diagonal elements of H and S matrices. The expectation value of  $2\sigma_+ = X + iY$  operator is measured. For the overlap matrix the unitary entanglers are of the form  $\hat{U}_{\alpha} = \mathrm{e}^{-\mathrm{i}\hat{\lambda}_{\alpha}\delta\tau}$  and  $\hat{U}_{\beta} = \mathrm{e}^{-\mathrm{i}\hat{\lambda}_{\beta}\delta\tau}$ , while for Hamiltonian matrix  $\hat{H} = \sum_i C_i \hat{P}_i$  the  $\hat{P}_i$  should be included into one of the unitary entangler.

$$||R_{\rm I}\rangle| = \langle \Psi_{\rm I}| \left(\hat{H} - E_{\rm I}\right)^2 |\Psi_{\rm I}\rangle$$

$$= \sum_{\rm KI} V_{\rm KI}^* V_{\rm LI} \langle \psi_{\rm K}| \left(\hat{H} - E_{\rm I}\right)^2 |\psi_{\rm L}\rangle. \tag{6}$$

Hence, the measurement of  $||R_I\rangle|$  is akin to the  $H_{KL}$  measurement but with the Hamiltonian  $\hat{H}$  in equation (3) replaced by  $(\hat{H} - E_I^2)^2$ . The norm indicates the convergence of each eigenstate. If  $||R_I\rangle|$  exceeds  $\epsilon$  (where  $\epsilon$  denotes the convergence criterion), a new Krylov vector, based on the normalized counterpart of  $|R_I\rangle$ , should be incorporated into the Davidson algorithm, provided it is linearly independent within the existing Krylov subspace.

The classical Davidson employs the Krylov subspace  $\mathcal{K}_r((\hat{H}-E),|\Phi_{\rm I}\rangle)$  to solve the eigenvalue problem. However, it is non-trivial to create the  $\hat{H}|\Psi_{\rm I}\rangle$  state on quantum circuits with the non-unitary  $\hat{H}$ . As an alternative, within the QDavidson algorithm, a correction vector defined by

$$|\delta_{\rm I}\rangle = e^{-\Delta\tau \left(\hat{H} - E_{\rm I}\right)} |\Psi_{\rm I}\rangle \tag{7}$$

is employed to expand the Krylov subspace. In other words, the QDavidson algorithm uses the subspace of  $\mathcal{K}_r(e^{-\Delta \tau(\hat{H}-E)},|\Phi_I\rangle)$  to derive the eigenstates. Because  $|\delta_I\rangle=[1-\Delta \tau(\hat{H}-E)]|\Phi_I\rangle+\mathcal{O}(\Delta \tau)$ , it can be verified that  $\mathcal{K}_r(e^{-\delta \tau(\hat{H}-E)},|\Phi_I\rangle)$  is equivalent to  $\mathcal{K}_r((\hat{H}-E),|\Phi_I\rangle)$  when  $\Delta \tau \to 0$ . The evolution detailed in equation (7) is subsequently mapped to unitary operators  $e^{-i\hat{A}}$  as proposed in [56],

$$|\delta_{\rm I}\rangle \simeq n_{\rm I} e^{-{\rm i}\hat{A}} |\Phi_{\rm I}\rangle$$
 (8)

where  $n_{\rm I}$  is the normalization factor and  $\hat{A}=\sum_{\alpha}a_{\alpha}\hat{P}_{\alpha}$ . The coefficients  $a_{\alpha}$  are obtained by solving a system of linear algebra equations associated with the mapping (more details can be found in appendix A). An alternative method involves directly mapping the preconditioned residue  $\frac{1}{\bar{H}-E_i}(\hat{H}-E)$  into  ${\rm e}^{-{\rm i}\hat{A}}$ , represented by  $|\delta_{\rm I}\rangle=\frac{1}{\bar{H}-E_i}(\hat{H}-E)|\Phi_{\rm I}\rangle\approx C{\rm e}^{-{\rm i}\hat{A}}|\Phi_{\rm I}\rangle$  where  $\bar{H}$  is the diagonal part of the Hamiltonian matrix in the Krylov subspace. We note that the investigation of the effects of different preconditioners on QDavidson's performance is beyond the scope of the current paper.

After mapping the residue operator to unitaries, the QDavidson algorithm determines if the new Krylov vectors (or the correction vector) are linearly dependent within the current subspace by introducing  $|\delta'_{K'}\rangle$ 

$$|\delta_{\rm I}'\rangle \equiv |\delta_{\rm I}\rangle - \sum_{\rm KJ} |\Psi_{\rm K}\rangle \left(S^{-1}\right)_{\rm KJ} \langle \Psi_{\rm J} | \delta_{\rm I}\rangle$$

$$\equiv |\delta_{\rm I}\rangle - \sum_{\rm KJ} \left(S^{-1}\right)_{\rm KJ} d_{\rm IJ} |\delta_{\rm I}\rangle. \tag{9}$$

Here,  $d_{\rm KJ} = \langle \Psi_J | \delta_I \rangle$  and the norm  $||\delta_I' \rangle|$  is measured is measured on QCs. If the ratio  $\frac{||\delta_I' \rangle|}{||\delta_I \rangle|} > \epsilon$ , it implies that the new Krylov vector  $|\delta_I \rangle$  is linearly independent within the current subspace, and hence, it should be incorporated into the subspace. As the inclusion of a new Krylov vector into the Krylov space introduces additional correlations, the next iteration will draw the results nearer to the exact solutions. The flowchart of the QDavidson algorithm is summarized in figure 2.

Since the size of the Krylov subspace  $N_{\rm K}$  is small, computing the generalized eigenvalue problems on classical computers is cheap. The primary complexity of the QDavidson algorithm stems from mapping the residue vectors into unitaries. Hence, its main bottleneck is the formation of S, b, and the resolution of the linear system to obtain unitary  $\hat{A}$ . Earlier research has shown that mapping non-unitary exponential operators into unitaries scales exponentially with correlation domain D [56]. But, a local approximation can be applied to eliminate the exponential dependence on D [56], leading to polynomial complexity, which is also utilized in the QDavidson method.

![](_page_5_Figure_3.jpeg)

**Figure 2.** Flowchart of the QDavidson algorithm. The orange (blue) box represents the part of the algorithm that is performed on QPU (CPU).

# 3. Numerical experiments

In this section, we present numerical results for the proposed algorithm. To demonstrate the performance of the QDavidson algorithm, we conducted exact quantum simulations of various systems, such as one-dimensional (1D) Heisenberg models and molecular systems, using a noiseless state-vector simulator.

## 3.1. 1D Heisenberg models

Both long-range (LR) and short-range (SR) 1D Heisenberg models, analogous to the models described in [56], were tested in this work. The SR models account only for nearest-neighbor interactions between spins, characterized by  $C_{ij}(\hat{X}_i\hat{X}_j+\hat{Y}_i\hat{Y}_j+\hat{Z}_i\hat{Z}_j)$  terms. In contrast, the LR models consider pairwise interactions among all spins, encompassing a larger number of terms in a qubit Hamiltonian. Explicitly, the LR and SR Hamiltonians are given by

$$\hat{H}_{SR} = -\sum_{i=1}^{N} \hat{S}_{i} \hat{S}_{i+1}, \tag{10}$$

and

$$\hat{H}_{LR} = -\sum_{j>i}^{N} \frac{1}{D_{ij}} \hat{S}_{i} \hat{S}_{j}, \tag{11}$$

where  $D_{ij} = \min(1 + |j-i|, 1 + N - |j-i|)$ . N denotes the number of spins in the system. For the SR Hamiltonians, the index i is cyclic; thus, when it reaches N+1, it reverts to 1. The QDavidson algorithm is state-dependent, necessitating the definition of initial reference states. We initiated the algorithm with the anti-ferromagnetic product state, which corresponds to the alternating  $|01...\rangle$  state in a computational basis. In order to benchmark the QDavidson algorithm against other QKS methods, a QLanczos algorithm with identical initial parameters was also implemented.

The results of the QDavidson and QLanczos algorithms for the 1D-Heisenberg models are shown in figure 3. For the initial four low-lying solutions, the QDavidson algorithm achieved convergence within 4 and 7 iterations for four-spin and six-spin systems, respectively (figures 3(E)–(H)). This performance

![](_page_6_Figure_3.jpeg)

**Figure 3.** Energy differences of the 1D Heisenberg models as a function of algorithm iteration. The energy difference is defined as  $E_{\text{algorithm}} - E_{\text{exact}}$ . Results for different states are represented by different colors: black for the ground state, blue for the first excited state, green for the second excited state, and red for the third excited state. Graphs (a)–(d) present the results of the QLanczos algorithm, while graphs (e)–(h) depict the results of the QDavidson algorithm obtained with the same QITE expansion parameters. Graphical representations of each system are provided in the bottom-left corner of each graph. The small circles with numbers symbolize spins, and the lines connecting these circles denote  $C_k \hat{S}_i \hat{S}_j$  terms. Different  $C_k$  coefficients are illustrated by lines of varying colors and widths.

surpasses the recently proposed QLanczos [56] algorithm (figures 3(A)–(D)), which not only converges slower but also displays numerical instability as the resultant states quickly become linearly dependent. By implementing root convergence criteria and a linear dependency check, the QDavidson algorithm exhibits enhanced numerical stability. The full results for the QLanczos algorithm are provided in the SI (figure S3). This algorithm was executed until an iteration produced a linearly dependent state. Notably, while the QLanczos managed to compute exact energy values for all four-spin models within six iterations (figures S3(A) and (B)), it did not converge for six-spin systems, and the final energy estimations showed a considerable deviation (figures S3(C) and (D)).

As each iteration appends a new entangler after mapping the imaginary time evolution operator into unitaries, the circuit depth increases monotonically with iterations within the QITE, QLanczos, and QDavidson frameworks. Hence, faster convergence translates to more compact circuits. Compared to QITE algorithms, QLanczos converges faster in finding the ground state [56]. Our QDavidson algorithm substantially improves convergence by employing the residue operator to narrow the subspace search near the exact state, resulting in a significantly reduced circuit depth. Although this improvement may not be evident for smaller systems, it becomes remarkably advantageous for larger systems. To elucidate this, we examined how the lowest-state energy's accuracy varies with the resulting circuits' maximum depth for both QLanczos and QDavidson. The results are shown in figure 4. QDavidson reproduces the exact solution for six-spin systems when the subspace comprises circuits with maximum gate depths of approximately 400 and 900 for the SR and LR models, respectively. In contrast, QLanczos results are less accurate, and deeper circuits are required to perform the algorithm. For instance, the accuracy attained by QLanczos after eight iterations (gate depth of 480) for the six-spin SR model can be achieved by QDavidson using circuits with a peak gate depth of just 120. Given the iterative expansion of the subspace, each QDavidson algorithm iteration contains states characterized by circuits of various depths. Consequently, tracking solely the longest circuit within the subspace is sufficient. The circuit depth was analyzed based on the Pauli words present in the operator  $\hat{A}$  in the  $e^{-\Delta \tau(\hat{H}-E)}|\Psi_I\rangle \to e^{-i\hat{A}}|\Psi_I\rangle$  expansion. Recognizing the elements of  $\hat{A}=\sum_i \theta_i \hat{\sigma}_i$ , a standard unitary evolution circuit could be constructed for  $e^{-i\hat{A}}$  (assuming one Trotter step).

### 3.2. $\pi$ -conjugated hydrocarbons

In addition to the 1D Heisenberg models, we also examined our algorithm on chemical systems. As expected, molecular Hamiltonians are notably more complex than the 1D Heisenberg models due to the intricate entanglement between numerous orbitals. To highlight the advantage of the QDavidson algorithm for molecular systems, we studied three molecular systems: ethylene, cyclopropene cation, and benzene. The

![](_page_7_Figure_3.jpeg)

**Figure 4.** Energy differences of the lowest states for six-spin 1D Heisenberg models as a function of a maximum circuit depth (A) SR model; (B) LR model.

Cartesian coordinates of the investigated molecular systems are provided in the SI (see table S1). An active space representing the  $\pi$ -conjugated system was selected for all the systems. The detailed active orbitals can be found in the SI (see figure S1). Therefore, the (2e, 2o) active space was considered for the  $C_2H_4$  molecule, (2e, 3o) for  $C_3H_3^+$ , and (6e, 6o) for  $C_6H_6$ . The Jordan–Wigner transformation [67] was utilized to map the second-quantized Hamiltonian into the qubit Hamiltonian. Consequently, the largest system examined in this study is the benzene molecule, comprising six electrons and 12 spin-orbitals in the active space (which corresponds to a 12 qubit Hamiltonian with 407 terms).

Taking into account that the electronic structure problems in molecular systems maintain particle-preserving and total spin-preserving symmetries, it is beneficial to establish a symmetric pool of Pauli terms for the correction vector  $|\delta_I\rangle$  mapping. Therefore, a set of all possible spin projection-preserving single and double excitation operators was selected and then transformed into qubit operators employing the Jordan–Wigner (JW) scheme [67]. All unique Pauli terms with an odd number of  $\hat{Y}$  operators were selected into the pool. This results in 12, 40, and 828 unique Pauli terms for the ethylene, cyclopropene cation, and benzene, respectively.

The performance of the QDavidson algorithm depends on the defined initial state. Multiple simulations were conducted using varying initial configurations ( $|\phi_0\rangle, |\phi_i^a\rangle = a_a^\dagger a_i |\phi_0\rangle$ ). In particular, the HF, the first excited singlet, and the first triplet product states were taken into consideration. The QDavidson algorithm converges to exact energy values for the smallest molecular systems within several iterations. For  $C_2H_4$ , starting from the HF product state, the QDavidson algorithm obtained the exact ground state energy (-77.115 18 Hartree) and the exact second excited singlet state energy (-76.375 41 Hartree) after just one iteration. Similar results were acquired for the  $C_3H_3^+$  system, where the exact ground state (-113.649 29 Hartree) and the first three singlet excited states were determined. Table 1 presents results for other initial states. Intriguingly, the eigenstates identified for the  $C_3H_3^+$  system maintain particle preservation and do not coincide with a neutral state solution with three electrons instead of two, even though they are lower in energy.

For the more extensive  $C_6H_6$  system, the QDavidson algorithm also accurately located the energies of several low-lying states (within chemical accuracy). However, as depicted in figures 5(A)–(C), many more iterations were needed. This is presumably due to the limited operator pool chosen, which only includes Pauli words from JW-mapped single and double excitation operators. Consequently, multi-electron systems (with electron count exceeding 2) might lack sufficient flexibility in the  $e^{-\Delta \tau (\hat{H}-E)}$  operator mapping. Regardless, the algorithm yielded meaningful results even with this restricted operator pool. For the benzene molecule, the algorithm found the first excited singlet and triplet states within  $10^{-2}$  Hartree after approximately 30 iterations (see figures 5(B) and (C)). For comparison, the QLanczos algorithm tends to get trapped in linearly dependent solutions after approximately 30 iterations, and the precision of the energies obtained is inferior to that in the QDavidson case. Consequently, when initiating the algorithm with the  $|HF\rangle$  state, the energy error for the ground state was found to be  $5 \times 10^{-3}$  Hartree, while the first excited singlet and triplet states could not be accurately reproduced, as illustrated in figure S2. With initialization with the excited state determinant, the algorithm successfully reproduced the energy of the first excited triplet within  $10^{-1}$  Hartree. However, this accuracy is an order of magnitude lower than that achieved with QDavidson.

For larger systems, it becomes evident that initiating the algorithm from a singular initial state is not the optimal strategy to capture the first few low-lying excited states, as illustrated in figures 5(A)–(C). Even though the algorithm can locate states of interest, the accuracy is far from the desired precision of  $10^{-3}$ 

**Table 1.** Results of QDavidson algorithm for  $C_2H_4$  and  $C_3H_3^+$  molecules. The initial state and number of iterations for the algorithm convergence are given. Different eigenstates are denoted in parenthesis as the following:  $S_0$ —ground singlet state,  $T_1$ —the lowest triplet state,  $S_i$ —ith excited singlet state,  $T_i$ —ith excited triplet state. The  $S_z$  denotes the spin projection of the obtained state.

| Molecule                      | Initial<br>state | Number of iterations | Energies                                                                                                            |
|-------------------------------|------------------|----------------------|---------------------------------------------------------------------------------------------------------------------|
| C <sub>2</sub> H <sub>4</sub> | 0011⟩            | 1                    | $-77.11518(S_0), S_z = 0$<br>$-76.37541(S_2), S_z = 0$                                                              |
|                               | $ 1001\rangle$   | 1                    | $-76.922 18 (T_1), S_z = 0$ $-76.582 76 (S_1), S_z = 0$                                                             |
|                               | $ 0101\rangle$   | $0^a$                | $-76.92218(T_1), S_z = 1$                                                                                           |
| $C_3H_3^+$                    | 000011⟩          | 2                    | $-113.649 29 (S_0), S_z = 0$ $-113.198 54 (S_1), S_z = 0$ $-112.759 64 (S_2), S_z = 0$ $-112.681 41 (S_3), S_z = 0$ |
|                               | $ 001001\rangle$ | 2                    | $-113.352 09 (T_1), S_z = 0$ $-113.198 54 (S_1), S_z = 0$ $-112.968 18 (T_2), S_z = 0$ $-112.759 64 (S_2), S_z = 0$ |
|                               | $ 000101\rangle$ | $0^a$                | $-113.352 09 (T_1), S_z = 1$                                                                                        |

<sup>&</sup>lt;sup>a</sup> The initial product state is already an exact solution.

![](_page_8_Figure_6.jpeg)

**Figure 5.** Energies and errors of the first four low-lying states  $(S_0, T_1, S_1, T_2)$  of  $C_6H_6$  molecule obtained from the QDavidson procedure as a function of algorithm iteration. Results for different states are given in different colors. The algorithm was initialized with different product states:  $|00000111111\rangle$  (A) and (E);  $|000010011111\rangle$  (B) and (F);  $|000001011111\rangle$  (C) and (G); a combination of three product states mentioned above (D) and (H). Black dashed horizontal lines show the exact energies obtained from a direct diagonalization of the corresponding Hamiltonian. The geometry of the molecule is shown in the inset of (E).

Hartree. Even initiating the algorithm with the first excited singlet (figure 5(F)) or triplet (figure 5(G)) determinants leads to quicker convergence compared to using the HF initial state. However, the energy convergence remains slow and often diverges from the exact values. Additionally, the initialization of the QDavidson with the entangled triplet CIS state was performed. Although the initial rapid convergence toward the exact excited energy was observed as illustrated in figure S3 (the accuracy of  $10^{-2}$  Hartree was achieved already at the third iteration), the convergence slows down and the desired accuracy of  $10^{-3}$  Hartree was not achieved even after 30 iterations. In turn, the generalization of the algorithm with multiple initial states results in faster convergence and higher accuracy (see figure 5(H), highlighting the significance of multireference states. Notably, chemically accurate energies for  $S_0$ ,  $T_1$ , and  $T_2$  states could be obtained after just 11 iterations. Therefore, to efficiently find the low-lying excited states of a large molecular system, it is advised to begin with multiple initial states to expedite energy convergence. Nevertheless, it is anticipated that the convergence will be affected by different initial states, and we expect a more significant overlap between the initial states and true ground state will accelerate the convergence as is in classical Davidson algorithms.

#### 3.3. Effects of statistical shot-noise

Owing to the finite number of quantum measurements (shots), exact measurements of the Hamiltonian matrix and overlap matrix elements within the Krylov subspace are unattainable. A limited shot count may introduce numerical instabilities into the QDavidson procedure. In general, to estimate the expectation value of a Hamiltonian with respect to a single state  $|\psi\rangle$  with precision p, it is required to perform  $O(|h_{\text{max}}|^2 M p^{-2})$ measurements, where  $h_{\max}$  is the largest coefficient in the Hamiltonian decomposition  $\hat{H} = \sum_i h_i \hat{P}_i$ , and M denotes the number of Hamiltonian terms [18]. Similar conclusions apply when evaluating Hamiltonian matrix elements within the Krylov subspace. Since  $\langle \Psi_{\rm I}|\hat{H}|\Psi_{\rm J}\rangle=\sum_i h_i \langle \Psi_{\rm I}|\hat{P}_i|\Psi_{\rm J}\rangle=\sum_i \sum_{\rm KL} V_{\rm KI}^* V_{\rm LJ}$  $\langle \psi_K | \hat{P}_i | \psi_L \rangle$  and each element  $\langle \psi_K | \hat{P}_i | \psi_L \rangle$  can be evaluated according to figure 1, the cost of evaluating the Hamiltonian matrix element is  $O(|h_{\text{max}}|^2 M p^{-2} N_K^2)$  where  $N_K$  is a size of the Krylov subspace. Although this measurement process can be complex, in practice, only a small subspace is typically spanned, and the growth of the subspace is linear with respect to the number of iterations, making the  $N_K^2$  factor relatively insignificant compared to  $|h_{\text{max}}|^2 M p^{-2}$ . Likewise, the overlap matrix's measurement incurs a cost of  $O(p^{-2}N_K^2)$  shots. The procedure for mapping residual vectors to unitaries also requires quantum measurements. The required shot count here depends on the size of the operator pool (P) chosen for the mapping and is in order of max[ $O(|h_{\text{max}}|^2Mp^{-2}N_K^2P)$ ,  $O(p^{-2}N_K^2P^2)$ ]. Another procedure necessitating quantum measurements involves checking for root convergence and assessing linear dependency. The root convergence check, as introduced in equation (6), incurs a cost of  $O(|h_{\text{max}}|^4 M^2 p^{-2} N_{\text{K}}^2)$  measurements. This is considered affordable since size of Krylov subspace  $N_{\rm K}$  is small and M grows polynomially with the system size. For linear dependency, if it is realized through the ratio  $\frac{||\delta_1'\rangle|}{||\delta_1\rangle|} > \epsilon$  the number of measurements required would be  $O(p^{-2}(N_K+1)^2)$ . Alternatively, linear dependency can be assessed by computing the determinant of the new overlap matrix (checking  $\det(S) < \epsilon$ ) obtained by including  $|\delta_1'\rangle$  in the Krylov subspace, with the same number of measurements. It is noteworthy that QLanczos formally requires fewer measurements per iteration as it does not involve checking for root convergence and linear dependency. However, its performance is significantly hampered by numerical instability, which might be deteriorated with the presence of shot noise. Besides, according to our numerical comparison, the QLancocs require more iterations to converge, eventually leading to more measurements. Additionally, it is noteworthy that the shots needed for QDavidson to converge are fewer than for the VQE procedure since the latter's ansatz optimization involves a substantial number of energy evaluations.

To illustrate the number of shots required to perform the algorithm on a real-world example, we incorporated the shot-noise into the calculations for the  $C_2H_4$  molecule. The desired precision p was determined after examining the algorithm's noise robustness by introducing the random error to each element of Hamiltonian matrix, (off-diagonal) overlap matrix element,  $S_{\alpha\beta}$  and  $b_{\alpha}$  (appendix A). It was found that an evaluation precision of  $10^{-4}$  is sufficient to guarantee the algorithm's numerical stability. With this level of precision, energy values of  $-77.115 \pm 0.001(S_0)$  and  $-76.375 \pm 0.001(S_2)$  were replicated. The algorithm, when initiated with a HF reference state, converged after one iteration. The estimated shot count per circuit evaluation was set to  $10^8$ , and the total number of shots was found to be  $\sim 10^{10}$ . This experiment underscores the QDavidson algorithm's capability to reproduce the low-lying spectra of the evaluated Hamiltonian even in the presence of statistical shot noise.

# 4. Summary

In this study, we developed an efficient QKS algorithm, QDavidson, to compute ground states and low-lying excited states by harnessing the Krylov subspace's power and the Davidson algorithm's rapid convergence. Unlike other QKS methodologies that employ real or imaginary time to pre-generate a subspace, QDavidson uses residues from previously approximated states to expand the subspace and capitalizes on the pre-conditioner to narrow the subspace search near the exact state, ensuring rapid convergence. Our numerical simulations confirm that the QDavidson algorithm surpasses other QKS methods like QLanczos in terms of convergence speed. Since the circuit depth increases with iterations, QDavidson's rapid convergence results in less complex quantum circuits, enhancing its resilience against noise. Future research could delve into advanced pre-conditioners for the QDavidson method [63, 65], potentially further trimming the iterative steps and circuit depth. Moreover, simulation accuracy is bound by the chosen basis set. While a large basis set is essential for achieving chemical accuracy, increasing the basis set size in quantum algorithms is not NISQ friendly, which requires a significantly larger number of qubits and deeper circuits [68]. However, by employing a trans-correlated Hamiltonian, one can attain accuracy at the cc-pVTZ basis even with a minimal basis set [68].

# Data availability statement

The data cannot be made publicly available upon publication due to legal restrictions preventing unrestricted public distribution. The data that support the findings of this study are available upon reasonable request from the authors.

# Acknowledgments

The research presented in this article was supported by the Laboratory Directed Research and Development program of Los Alamos National Laboratory (LANL) under Project Number 20200056DR. We thank the LANL Institutional Computing program for access to HPC resources. S T acknowledges the support from the Center of Integrated Nanotechnologies, a US Department of Energy and Office of Basic Energy Sciences User Facility. LANL is operated by Triad National Security, LLC, for the National Nuclear Security Administration of the US Department of Energy (Contract No. 89233218CNA000001). AIB and NVT acknowledge funding from the subcontract with LANL (Award ID: 203369-00001). AIB acknowledges financial support from the R Gaurth Hansen Professorship Fund.

### ORCID iDs

Alexander I Boldyrev https://orcid.org/0000-0002-8277-3669 Yu Zhang https://orcid.org/0000-0001-8938-1927

#### References

- [1] Cao Y et al 2019 Chem. Rev. 119 10856
- [2] McArdle S, Endo S, Aspuru-Guzik A, Benjamin S C and Yuan X 2020 Rev. Mod. Phys. 92 015003
- [3] Bauer B, Bravyi S, Motta M and Chan G K-L 2020 Chem. Rev. 120 12685
- [4] Cohen A J, Mori-Sánchez P and Yang W 2012 Chem. Rev. 112 289
- [5] Schuch N and Verstraete F 2009 Nat. Phys. 5 732
- [6] Chan G K-L and Sharma S 2011 Annu. Rev. Phys. Chem. 62 465
- [7] Schollwöck U 2011 Ann. Phys., NY 326 96
- [8] Tubman N M, Freeman C D, Levine D S, Hait D, Head-Gordon M and Whaley K B 2020 J. Chem. Theory Comput. 16 2139
- [9] Dash M, Feldt J, Moroni S, Scemama A and Filippi C 2019 J. Chem. Theory Comput. 15 4896
- [10] Lyakh D I, Musiał M, Lotrich V F and Bartlett R J 2012 Chem. Rev. 112 182
- [11] Feynman R P 1982 Int. J. Theor. Phys. 21 467
- [12] Manin Y I 1980 Sovetskoe Radio p 128
- [13] Preskill J 2018 Quantum 2 79
- [14] Arute F et al 2019 Nature 574 505
- [15] Alexeev Y et al 2021 PRX Quantum 2 017001
- [16] Abrams D S and Lloyd S 1999 Phys. Rev. Lett. 83 5162
- [17] Kitaev A, Shen A, Vyalyi M and Vyalyi M 2002 Classical and Quantum Computation (Graduate Studies in Mathematics) (American Mathematical Society)
- [18] Peruzzo A, McClean J, Shadbolt P, Yung M H, Zhou X Q, Love P J, Aspuru-Guzik A and O'Brien J L 2014 Nat. Commun. 5 4213
- [19] Kandala A, Temme K, Córcoles A D, Mezzacapo A, Chow J M and Gambetta J M 2019 Nature 567 491
- [20] Kandala A, Mezzacapo A, Temme K, Takita M, Brink M, Chow J M and Gambetta J M 2017 Nature 549 242
- [21] Nam Y et al 2020 npj Quantum Inf. 6 33
- [22] Tkachenko N V, Sud J, Zhang Y, Tretiak S, Anisimov P M, Arrasmith A T, Coles P J, Cincio L and Dub P A 2021 PRX Quantum
- [23] Ryabinkin I G, Lang R A, Genin S N and Izmaylov A F 2020 J. Chem. Theory Comput. 16 1055
- [24] Grimsley H R, Economou S E, Barnes E and Mayhall N J 2019 Nat. Commun. 10 3007
- [25] Zhang Y, Cincio L, Negre C F A, Czarnik P, Coles P J, Anisimov P M, Mniszewski S M, Tretiak S and Dub P A 2022 npj Quantum Inf. 8 96
- [26] Tang H L, Shkolnikov V, Barron G S, Grimsley H R, Mayhall N J, Barnes E and Economou S E 2021 PRX Quantum 2 020310
- [27] Ryabinkin I G, Izmaylov A F and Genin S N 2021 Quantum Sci. Technol. 6 024012
- [28] Lang R A, Ryabinkin I G and Izmaylov A F 2021 J. Chem. Theory Comput. 17 66
- [29] Zhang Z-J, Kyaw T H, Kottmann J, Degroote M and Aspuru-Guzik A 2021 Quantum Sci. Tech. 6 035001
- [30] Yordanov Y S, Armaos V, Barnes C H W and Arvidsson-Shukur D R M 2020 Iterative qubit-excitation based variational quantum eigensolver (arXiv:2011.10540)
- [31] Yuan X, Sun J, Liu J, Zhao Q and Zhou Y 2021 arXiv:2007.00958
- [32] Gu A, Lowe A, Dub P A, Coles P J and Arrasmith A 2021 arXiv:2108.10434
- [33] Cerezo M et al 2021 Nat. Rev. Phys. 3 625
- [34] Bharti K et al 2021 Noisy intermediate-scale quantum (NISQ) algorithms (arXiv:2101.08448)
- [35] Nelson T R, Ondarse-Alvarez D, Oldani N, Rodriguez-Hernandez B, Alfonso-Hernandez L, Galindo J F, Kleiman V D, Fernandez-Alberti S, Roitberg A E and Tretiak S 2018 Nat. Commun. 9 2316
- [36] Zhang Y, Li L, Tretiak S and Nelson T 2020 J. Chem. Theory Comput. 16 2053
- [37] Nelson T R, White A J, Bjorgaard J A, Sifain A E, Zhang Y, Nebgen B, Fernandez-Alberti S, Mozyrsky D, Roitberg A E and Tretiak S 2020 Chem. Rev. 120 2215
- [38] Weight B M, Li X and Zhang Y 2023 Phys. Chem. Chem. Phys. 25 31554

- [39] Nakanishi K M, Mitarai K and Fujii K 2019 Phys. Rev. Res. 1 033062
- [40] Higgott O, Wang D C and Brierley S 2019 Quantum 3 1
- [41] Parrish R M, Hohenstein E G, McMahon P L and Martínez T J 2019 Phys. Rev. Lett. 122 230401
- [42] Shen Y, Zhang X, Zhang S, Zhang J-N, Yung M-H and Kim K 2017 Phys. Rev. A 95 020501
- [43] McClean J R, Kimchi-Schwartz M E, Carter J and de Jong W A 2017 Phys. Rev. A 95 042308
- [44] Kawai H and Nakagawa Y O 2020 Mach. Learn. Sci. Technol. 1 045027
- [45] Greene-Diniz G and Muñoz Ramo D 2021 Int. J. Quantum Chem. 121 e26352
- [46] Stilck Françediia D and García-Patrón R 2021 Nat. Phys. 17 1221
- [47] Colless J I, Ramasesh V V, Dahlen D, Blok M S, Kimchi-Schwartz M E, McClean J R, Carter J, de Jong W A and Siddiqi I 2018 Phys. Rev. X 8 011021
- [48] Takeshita T, Rubin N C, Jiang Z, Lee E, Babbush R and McClean J R 2020 Phys. Rev. X 10 011004
- [49] Parrish R M and McMahon P L 2021 arXiv:1909.08925
- [50] Ollitrault P J, Kandala A, Chen C-F, Barkoutsos P K, Mezzacapo A, Pistoia M, Sheldon S, Woerner S, Gambetta J M and Tavernelli I 2020 Phys. Rev. Res. 2 043140
- [51] Huggins W J, Lee J, Baek U, O'Gorman B and Whaley K B 2020 New J. Phys. 22 073009
- [52] Asthana A et al 2023 Chem. Sci. 14 2405
- [53] Kumar A, Asthana A, Abraham V, Crawford T D, Mayhall N J, Zhang Y, Cincio L, Tretiak S and Dub P A 2023 J. Chem. Theory Comput. 19 9136
- [54] Cortes C L and Gray S K 2022 Phys. Rev. A 105 022417
- [55] Stair N H, Huang R and Evangelista F A 2020 J. Chem. Theory Comput. 16 2236
- [56] Motta M, Sun C, Tan A T K, O'Rourke M J, Ye E, Minnich A J, Brandão F G S L and Chan G K-L 2020 Nat. Phys. 16 205
- [57] Yeter-Aydeniz K, Gard B T, Jakowski J, Majumder S, Barron G S, Siopsis G, Humble T and Pooser R C 2021 arXiv:2102.05511
- [58] Epperly E N, Lin L and Nakatsukasa Y 2021 arXiv:2110.07492
- [59] McArdle S, Jones T, Endo S, Li Y, Benjamin S C and Yuan X 2019 npj Quantum Inf. 5 75
- [60] Yeter-Aydeniz K, Pooser R C and Siopsis G 2020 npj Quantum Inf. 6 63
- [61] Saad Y 2003 Iterative Methods for Sparse Linear Systems (Other Titles in Applied Mathematics 2nd edn (SIAM)
- [62] Lanczos C 1950 J. Res. Natl. Bur. Stand. B 45 255
- [63] Parrish R M, Hohenstein E G and Martínez T J 2016 J. Chem. Theory Comput. 12 3003
- [64] Tretiak S, Isborn C M, Niklasson A M N and Challacombe M 2009 J. Chem. Phys. 130 054111
- [65] Zhou Z and Parker S M 2021 J. Chem. Phys. 155 204111
- [66] Furche F, Krull B T, Nguyen B D and Kwon J 2016 J. Chem. Phys. 144 174105
- [67] Jordan P and Wigner E 1928 Z. Phy. 47 631
- [68] Kumar A, Asthana A, Masteran C, Valeev E F, Zhang Y, Cincio L, Tretiak S and Dub P A 2022 J. Chem. Theory Comput. 18 5312