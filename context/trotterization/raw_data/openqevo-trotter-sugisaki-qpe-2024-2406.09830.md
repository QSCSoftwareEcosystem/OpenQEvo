

<!-- page-01 -->

## Does the full configuration interaction method based on quantum phase estimation with Trotter decomposition satisfy the size consistency condition?

Kenji Sugisaki<sup>1, 2, 3</sup>

<sup>1)</sup>Graduate School of Science and Technology, Keio University, 7-1 Shinkawasaki, Saiwai-ku, Kawasaki, Kanagawa 212-0032, Japan

<sup>2)</sup>Quantum Computing Center, Keio University, 3-14-1 Hiyoshi, Kohoku-ku, Yokohama, Kanagawa 223-8522, Japan

<sup>3)</sup>Centre for Quantum Engineering, Research and Education, TCG Centres for Research and Education in Science and Technology, Sector V, Salt Lake, Kolkata 700091, India

(\*Electronic mail: ksugisaki@keio.jp)

(Dated: 9 August 2024)

Electronic structure calculations of atoms and molecules are considered to be a promising application for quantum computers. Two key algorithms, the quantum phase estimation (QPE) and the variational quantum eigensolver (VQE), have been extensively studied. The condition that the energy of a dimer consisting of two monomers separated by a large distance should be equal to twice the energy of a monomer, known as size consistency, is essential in quantum chemical calculations. Recently, we reported that the size consistency condition can be violated by Trotterization in the unitary coupled cluster singles and doubles (UCCSD) ansatz in VQE when employing molecular orbitals delocalized to the dimer (K. Sugisaki *et al.*, *J. Comput. Chem.*, published online; DOI:10.1002/jcc.27438). It is well known that the full configuration interaction (full-CI) energy is invariant to arbitrary rotations of molecular orbitals, and therefore the QPE-based full-CI should theoretically satisfy the size consistency. However, Trotterization of the time evolution operator can break the size consistency conditions. In this work, we investigated whether size consistency can be maintained with Trotterization of the time evolution operator in QPE-based full-CI calculations. Our numerical simulations revealed that size consistency in QPE-based full-CI is not automatically violated by using molecular orbitals delocalized to the dimer, but employing an appropriate Trotter decomposition condition is crucial to maintain size consistency. We also report on the acceleration of QPE simulations through the sequential addition of ancillary qubits.

## I. INTRODUCTION

Solving the Schrödinger equation for atoms and molecules as accurately as possible is a fundamental goal of quantum chemistry. The full configuration interaction (full-CI) method provides the best variational wave functions and energies within the Hilbert space spanned by the chosen basis set. However, the computational cost of the full-CI method grows exponentially with the number of basis functions and electrons, making it impractical except for small molecules with simple basis sets. The method of solving the full-CI on a quantum computer using the quantum phase estimation (QPE) algorithm was proposed in 2005. Since then, a number of theoretical studies on QPE-based quantum chemical calculations<sup>2–13</sup> and extensions of the QPE algorithm<sup>14–18</sup> have been reported. Experimentally, iterative QPE-based full-CI/STO-3G calculations of the H<sub>2</sub> molecule were reported in 2010 with photonic<sup>19</sup> and NMR<sup>20</sup> quantum processors, using one qubit for wave function encoding. The same system was investigated with two qubits for wave function storage with superconducting qubits in 2016<sup>21</sup>, and on an ion-trap quantum processor in conjunction with a Bayesian QPE framework with quantum error detection.<sup>22</sup> The experimental demonstration of the full-CI/STO-3G of the HeH+ molecule was also reported using the NV center of the diamond system.<sup>23</sup> Recently, statistical QPE with up to six-qubit Hamiltonian on a superconducting quantum processor was reported.<sup>24</sup>

In 2014, the quantum-classical hybrid approach known as

a variational quantum eigensolver (VQE) was proposed for quantum chemical calculations using noisy intermediate-scale quantum devices. <sup>25,26</sup> In VQE, an approximate wave function is generated on a quantum computer using a parameterized quantum circuit defined by an "ansatz", and the energy expectation value is computed by statistically sampling the measurement results of the quantum circuit The unitary coupled cluster (UCC) ansatz<sup>27</sup> is often used as a physically motivated ansatz, and is defined as

$$|\Psi_{\rm UCC}\rangle = e^{(T-T^{\dagger})}|\Psi_{\rm HF}\rangle,$$
 (1)

where  $|\Psi_{\rm HF}\rangle$  is the Hartree–Fock (HF) wave function, and T and  $T^{\dagger}$  are the excitation and de-excitation operators, respectively, applied to the HF wave function. The UCC ansatz, when considering single and double excitation operators as T, is known as the UCCSD ansatz and typically provides accurate correlation energies for closed shell molecules.

In quantum chemical calculations, the energy of a dimer consisting of two monomers separated by a large distance should be twice the energy of a monomer. This condition, known as size consistency, <sup>28</sup> is crucial, especially in the calculation of large molecules. Truncated configuration interaction expansions, such as CISD and CISDT, do not satisfy the size consistency, while truncated coupled cluster methods like CCSD and CCSDT do. The UCCSD ansatz, used in the VQE framework, is based on the cluster expansion and it generally assumed to be size consistent. However, in VQE, the UCCSD ansatz is usually implemented using the Trotter

<!-- page-02 -->

decomposition to construct the parameterized quantum circuit. Recently, we have numerically demonstrated that the Trotterized UCCSD ansatz does not automatically satisfy the size consistency condition.<sup>29</sup> Size consistency of the UCCSD ansatz can be maintained when molecular orbitals localized to each monomer are used, but it can be broken when molecular orbitals delocalized over the dimer are employed in the UCCSD ansatz.

Since OPE-based full-CI is often implemented using the Trotter decomposition of the time evolution operator, it is important to verify whether QPE-based full-CI with Trotter decomposition automatically satisfies the size consistency condition. While it is known that full-CI energy is invariant with respect to the choice of reference molecular orbitals, it is unclear how the robustness of QPE-based full-CI energy is affected by Trotter errors based on the choice of molecular orbitals. It is important to note that Trotter decomposition impacts size consistency differently in VQE-UCCSD and QPE. In VQE-UCCSD, the total energy is calculated as the expectation value of the Hamiltonian, and the contamination of wave function from other electronic states due to Trotter decomposition affects size consistency. In contrast, QPE calculates the total energy based on the phase shift induced by time evolution. In this case, changes in the amount of phase shift due to Trotter error can lead to a breakdown in size consistency.

In this work, we performed numerical quantum circuit simulations of QPE-based full-CI using both localized and delocalized molecular orbitals with various Trotter decomposition conditions, focusing on the size consistency condition. The paper is organized as follows: Section II introduces the QPE-based full-CI method. Section III describes the target molecular systems in this work and outlines the numerical simulation conditions. We also discuss accelerating the numerical simulation of the QPE quantum circuit based on the sequential addition of ancillary qubits. Section IV presents the results of the numerical simulations. A summary of this work is given in Section V.

## II. THEORY

The QPE is a quantum algorithm designed to find the eigenvalues and corresponding eigenvectors of a unitary matrix U in polynomial time. <sup>30,31</sup> In quantum chemical calculations, the QPE is performed using the time evolution operator as the unitary operator,

$$U = e^{-iHt}. (2)$$

The Born–Oppenheimer approximation<sup>32</sup> is usually adopted, and the electronic Hamiltonian is used as H. In the second quantized formula, the electronic Hamiltonian H is expressed as

$$H = \sum_{pq} h_{pq} a_p^{\dagger} a_q + \frac{1}{2} \sum_{pqrs} g_{pqrs} a_p^{\dagger} a_q^{\dagger} a_s a_r. \tag{3}$$

Here,  $h_{pq}$  and  $g_{pqrs}$  are the one- and two-electron integrals, respectively, and the indices p, q, r, and s run over spin orbitals in the active space.

![](_page_0_Figure_10.jpeg)

FIG. 1. The quantum circuit of the textbook implementation of QPE.  $x_1, x_2, \dots, x_N$  represent the measurement outcomes of ancillary qubits.

The textbook implementation of the quantum circuit for QPE<sup>33</sup> is shown in FIG. 1. This quantum circuit contains L qubits for wave function storage and N ancillary qubits for eigenphase readout. The QPE-based full-CI consists of five steps: (1) preparation of the approximate wave function of the target electronic state using a Prep circuit, (2) generation of quantum superposition states using Hadamard (H) gates, (3) controlled-time evolution operation, (4) inverse quantum Fourier transform, and (5) measurement of ancillary qubits. The bit string obtained from the measurement in step (5) corresponds to the fractional binary representation of the eigenphase  $\phi = 0.x_1x_2 \cdots x_N$  in

$$e^{-iHt}|\Psi\rangle = e^{-iEt}|\Psi\rangle = e^{i2\pi\phi}|\Psi\rangle,$$
 (4)

which corresponds to one of the eigenstates. The probability of obtaining a particular eigenvalue is proportional to the overlap between the input and full-CI wave functions.

In the quantum circuit implementation, the second quantized Hamiltonian in eq. (3) is transformed into a qubit Hamiltonian  $H_q$ ,

$$H_q = \sum_{i=1}^J w_j P_j,\tag{5}$$

using the fermion–qubit transformation techniques such as the Jordan–Wigner transformation  $(JWT)^{34}$  and the Bravyi–Kitaev transformation  $(BKT)^{35}$ . Here,  $P_j$  represents a tensor product of Pauli operators, known as Pauli strings, J is the number of Pauli strings, and  $w_j$  is the coefficient computed from  $h_{pq}$  and  $g_{pqrs}$ . The time evolution operator in eq. (2) is then implemented using the Trotter decomposition. The first-order and second-order Trotter decompositions are given by

$$e^{-iH_qt} = \left[\Pi_{j=1}^J e^{-iw_j P_j t/M}\right]^M \tag{6}$$

and

$$e^{-iH_qt} = \left[ \left( \Pi_{j=1}^J e^{-iw_j P_j t/2M} \right) \left( \Pi_{j=J}^1 e^{-iw_j P_j t/2M} \right) \right]^M,$$
 (7)

respectively. Here, M is the number of Trotter slices. Besides the Trotter decomposition-based implementation, approaches based on the truncated Taylor series<sup>36,37</sup> and qubitization<sup>38</sup> have also been proposed. The technique based on qubitization

<!-- page-03 -->

![](_page_0_Picture_1.jpeg)

FIG. 2. Schematic illustrations of the molecular orbitals for the 4H and 8H clusters. The intermonomer spacing is reduced for clarity. The lowest two and four orbitals for the monomer and the dimers, respectively, are doubly occupied in the HF wave function.

shows better computational cost scaling compared to Trotterization, but it requires additional ancillary qubits.<sup>39</sup> In this work, we focus on the Trotter decomposition-based approach.

It is well known that the full-CI energy is invariant under arbitrary unitary rotations of the molecular orbitals. For convenience, we focus on the HF canonical molecular orbitals (CMO) and the localized molecular orbitals (LMO) as the two reference orbitals. By defining a unitary matrix *V* that transforms the two different orbitals, the Hamiltonian matrices in the LMO and CMO bases are written as

$$H_{\rm LMO} = V^{\dagger} H_{\rm CMO} V. \tag{8}$$

Similarly, the time evolution operators can be expressed as

$$U_{\rm LMO} = V^{\dagger} U_{\rm CMO} V. \tag{9}$$

However, in the full-CI calculations using QPE with Trotter decomposition, the Trotterized time evolution operator  $U^{\text{Trotter}}$  does not necessarily satisfy the equality in eq. (9);

$$U_{\rm LMO}^{\rm Trotter} \neq V^{\dagger} U_{\rm CMO}^{\rm Trotter} V,$$
 (10)

because the order of the Pauli strings in the Trotterized time evolution operator can depend on the molecular orbitals. We expect that the Pauli strings must be ordered appropriately so that the Trotter error affects both the monomer and the dimer in the same way to satisfy the size consistency condition.

## III. COMPUTATIONAL CONDITIONS

In this work we mainly focus on a tetrahydrogen (4H) cluster in a square geometry with R(H-H) = 1.0583 Å (2.0 Bohr) as the monomer, which is well known as a strongly correlated system.<sup>40</sup> The octahydrogen (8H) cluster, representing

the dimer, is constructed by placing two 4H clusters to form a cuboid, with an intermonomer distance of 100 Å. This system is also used in our previous work.<sup>29</sup> We employed the STO-3G basis set, and the active space includes all the molecular orbitals. The size of the active space is (4e, 4o) and (8e, 8o) for 4H and 8H clusters, respectively. Here, (ke, lo) indicates that the active space contains k electrons and l molecular orbitals

In the present study, we used two different sets of molecular orbitals for the dimer calculations: the CMOs, delocalized to the dimer under the  $D_{2h}$  point group, and the LMOs under the  $C_{2v}$  point group. Schematic illustrations of the CMO and LMO of 4H and 8H clusters are given in FIG. 2. These molecular orbitals are generated using the GAMESS-US software<sup>41</sup>.

Conventional fermion–qubit transformations such as JWT and BKT require 2l qubits to encode the wave function. In this work, we used the symmetry-conserving Bravyi–Kitaev transformation (SCBKT),<sup>42</sup> which reduces the qubit count by two by specifying the number of spin- $\alpha$  and spin- $\beta$  electrons. Thus, the number of qubits for wave function encoding (L in FIG. 1) is 6 and 14 for 4H and 8H clusters, respectively.

In addition to the 4H/8H clusters, we also studied 2H/4H clusters to examine the system size dependence, and the acetylene (HC≡CH) molecule under triple bond dissociation as the representative system of covalent bond cleavage. For the 2H/4H clusters calculations, the intra- and inter-molecular H−H distances are set to 1.0583 Å and 100 Å, respectively. The STO-3G basis set is used, with the active space being (2e, 2o) and (4e, 4o) for the monomer and dimer, respectively. In the case of acetylene, the monomer is the lowest spin-quartet state of the C−H fragment, with a bond length set to the experimental value of acetylene (1.1199 Å). Using the STO-3G basis set and freezing the 1s core orbital of the C atoms, we constructed (5e, 5o) and (10e, 10o) active spaces for the monomer and dimer, respectively.

In the QPE simulations, we set the time length of the time evolution operator in eq. (2) to t = 1.0. We used 10 ancillary qubits to read out the eigenphase for 4H/8H and 2H/4H clusters, and 8 ancillary qubits for the triple bond dissociation of acetylene. As input wave functions for the QPE, we examined both the full-CI and HF wave functions to assess the state dependence of the Trotter error. For the implementation of the controlled-time evolution operator, we utilized both the first-order and second-order Trotter decompositions with M = 1, 2, 5, and 10. The Trotter error depends on the order of the Pauli strings. Unless otherwise stated, we employed magnitude ordering, where the Pauli strings are applied in descending order of the absolute value of the corresponding coefficient,  $|w_i|^{43}$  All simulations were conducted using our custom Python3 code, developed with the OpenFermion,44 Cirq, 45 and cuQuantum 46 libraries. For reference, the Trotterfree time evolution was implemented using the expm function in the SciPy library.<sup>47</sup>

The computational cost of quantum circuit simulations for QPE-based full-CI is substantial, making acceleration crucial for studying larger systems. In QPE with N ancillary qubits, we need to perform the controlled-U operation  $2^N - 1$  times, which is the most time-consuming process. In this study, we

<!-- page-04 -->

![](_page_0_Figure_1.jpeg)

FIG. 3. Schematic illustration of the numerical simulations for the QPE-based full-CI with four ancillary qubits. Each step of the numerical simulation is indicated by a dotted square.

![](_page_0_Figure_3.jpeg)

FIG. 4. Plot of phase value versus measurement probability from the QPE simulation of 4H/8H clusters using the full-CI wave function as the input. Magnitude ordering is used for the Trotter decomposition.

![](_page_0_Figure_5.jpeg)

![](_page_0_Figure_6.jpeg)

FIG. 5. Plot of phase value versus measurement probability from the QPE simulation of 4H/8H clusters using the HF wave function as the input. Magnitude ordering is used for the Trotter decomposition.

## IV. RESULTS

## A. 4H and 8H clusters

Plots of phase value versus measurement probability from the QPE-based full-CI of the 4H and 8H clusters, as a function of the number of Trotter slices M, are shown in FIG. 4 and 5, using full-CI and HF wave functions, respectively, as the inputs. For small M, the peak obtained from the Trotterized time evolution operator is shifted from the peak calculated by the Trotter-free simulations, but it converges to the Trotter-free result as M increases. Notably, both CMO- and LMO-based QPE simulations yield peaks at nearly the same position. The peak height is reduced when using the HF wave function as the input due to the decreased overlap between the input and full-CI wave functions, although the peak position remains consistent between the full-CI and HF inputs. It is important to note that some peaks exhibit larger variance due

<!-- page-05 -->

![](_page_0_Figure_1.jpeg)

FIG. 6. Plot of phase value versus measurement probability from the QPE simulation of 4H/8H clusters with the full-CI wave function as the input. Lexicographic ordering is used for the Trotter decomposition.

to the well-known "leakage problem" in the textbook implementation of QPE. 48

To assess the impact of operator ordering on the Trotterized time evolution operator, we examined lexicographic ordering in the Trotter decomposition. The results are shown in FIG. 6. As anticipated, the trend of the Trotter error varied with different strategies for operator ordering. In the dimer CMO calculations using the first-order Trotter decomposition, the computed peak is already quite close to the Trotter-free value even for M = 1, likely due to a fortuitous cancellation of errors (see FIG. 6(c)). However, in the first-order Trotter simulations for M = 1 in the dimer CMO, an additional small peak is observed around  $\phi = 0.492$ , despite using the full-CI wave function as the input. This is because the Trotterized time evolution operator differs from the original time evolution operator, and the full-CI wave function is no longer an eigenfunction of the Trotterized time evolution operator. The presence of additional peaks indicates a significant deviation of  $U^{\text{Trotter}}$  from U, suggesting that a more refined approach to Trotter decomposition is necessary. It should be noted that the peak positions are insensitive to the order of the Trotter decomposition for monomer and dimer with LMO. However, this is not always the case. In fact, as we discuss in the following subsections, we observed clear differences in size consistency breakdown between first-order and second-order Trotter decompositions.

The eigenphase value is determined by fitting the measurement probability plot with a Gaussian function. The ratio of the dimer and monomer eigenenergies,  $E_{\rm Dimer}/E_{\rm Monomer}$ , is computed and plotted in FIG. 7(a) and (b) for magnitude and lexicographic orderings, respectively, as a function of 1/M. Ideally, when size consistency is perfectly maintained, this ratio should be equal to two. However, in our numeri-

![](_page_0_Figure_6.jpeg)

FIG. 7. Ratio of the total energies of the 8H cluster (dimer) to the 4H cluster (monomer) calculated using (a) magnitude ordering and (b) lexicographic ordering. The ratio values normalized by the Trotter-free simulation results are plotted in (c) and (d).

cal simulations, the ratio deviates slightly from two even in the Trotter-free implementation, likely due to rounding and leakage errors. To assess the deviation of  $E_{\text{Dimer}}/E_{\text{Monomer}}$ values from Trotter decomposition-based simulation (denoted as "Trotter" in the superscript) compare to Trotter-free simulations (denoted as "w/o Trotter" in the superscript), we plot  $E_{\text{Dimer}}^{\text{Trotter}}/E_{\text{Monomer}}^{\text{Trotter}}$  normalized by  $E_{\text{Dimer}}^{\text{w/o Trotter}}/E_{\text{Monomer}}^{\text{w/o Trotter}}$ in FIG. 7(c) and (d) for magnitude and lexicographic orderings, respectively. In this case, using M = 1 for the Trotter decomposition (where  $\Delta t$ , the time length of a single Trotter slice, is 1.0) is insufficient to meet the size consistency condition, irrespective of the operator ordering method and the molecular orbitals employed for the wave function expansion. Increasing the number of Trotter slices to M = 2 nearly satisfies the size consistency condition, except for the CMO with first-order Trotter decomposition using lexicographic ordering. Even in this case, size consistency condition is systematically recovered with a higher number of Trotter slices. Our numerical simulations indicate that size consistency is not inherently violated using LMOs for wave function expansion. However, the convergence behavior towards Trotter-free results with respect to the number of Trotter slices underscores the importance of selecting appropriate Trotter decomposition conditions, such as reference molecular orbitals, the order of Trotter decomposition, and operator ordering, to ensure size consistency in QPE-based full-CI calculations.

## B. 2H and 4H clusters

Next, we investigate the system size dependency of the breakdown of size consistency in the QPE with Trotterized time evolution operators. We performed the QPE simulations using 2H and 4H clusters as a monomer and a dimer, respectively. The ratio of the total energies of the dimer to the

<!-- page-06 -->

![](_page_0_Figure_1.jpeg)

FIG. 8. Ratio of the total energies of the 4H cluster (dimer) to the 2H cluster (monomer) normalized by the Trotter-free simulation results. (a) Magnitude ordering. (b) Lexicographic ordering

monomer, normalized by the Trotter-free simulation results, is plotted in FIG. 8. Note that the scale of the vertical axis of FIG. 8 is a half of that of FIG. 7(c) and (d). Although the deviation from size consistency is smaller in 2H/4H clusters compared to 4H/8H clusters, lexicographic ordering in conjunction with CMO is likely to break size consistency when the number of Trotter slices is small, whereas LMO nearly maintains size consistency with lexicographic ordering for M = 1.

## C. Triple bond dissociation in acetylene

To examine the size consistency condition under bond breaking, we conducted OPE simulations of acetylene undergoing triple bond dissociation, using the C≡H fragment as the monomer. The results are summarized in FIG. 9. Due to the large total energies of the acetylene system, we plotted the ratio of the eigenenergies of the qubit Hamiltonian without constant terms (frozen core energy and the constant term obtained in the SCBKT). Note that the constant term of the dimer is exactly twice that of the monomer. We observed clear difference in the behavior of size consistency breakdown between CMO and LMO. Size consistency is nearly preserved when LMO is used for wave function expansion, even with lexicographic ordering and M = 1 in the Trotter decomposition. In contrast, the CMO-based calculation shows a breakdown in size consistency for small M. It is important to note that size consistency does not always guarantee accurate total energy. Specifically,  $E_{\rm Monomer}^{\rm w/oTrotter} - E_{\rm Monomer}^{\rm Trotter}$  and  $E_{\rm Dimer;LMO}^{\rm w/oTrotter} - E_{\rm Dimer;LMO}^{\rm Trotter}$  values with lexicographic ordering and M=1 are calculated as 0.0020 and 0.0040 Hartree, respectively.

## D. Comparison between LMO and CMO

As we observed from the numerical simulations, the extent of size consistency violation is smaller for LMO compared to CMO. This observation is consistent with expectations from a chemical perspective.

Consider a dimer composed of spatially well-separated monomers A and B. In the LMO basis, in the limit of weak inter-monomer interaction, the Hamiltonian of the dimer,

![](_page_0_Figure_9.jpeg)

FIG. 9. Ratio of the total energies of the dimer to the monomer normalized by the Trotter-free simulation results in triple bond dissociation of acetylene. (a) Magnitude ordering. (b) Lexicographic ordering

H(A + B), can be expressed as a linear combination of monomer Hamiltonians H(A) and H(B),

$$H(A+B) = H(A) + H(B) \tag{11}$$

with

$$[H(A), H(B)] = 0.$$
 (12)

Using the commutation relation in eq. (12), the Trotterized time evolution operator for the dimer can be rewritten as the product of the Trotterized time evolution operators for monomers A and B, with the Trotterized terms arranged accordingly. For instance, in the first-order Trotter decomposition, we have

$$e^{-iH(A+B)_{q}t} = \left[\Pi_{j}e^{-iw_{j}P_{j}t/M}\right]^{M}$$
$$= \left[\Pi_{k\in A}e^{-iw_{k}P_{k}t/M}\Pi_{l\in B}e^{-iw_{l}P_{l}t/M}\right]^{M}. \quad (13)$$

If the orderings of the Pauli strings  $P_{k \in A}$  and  $P_{l \in B}$  in eq. (13) are the same as those in the Trotterized time evolution operators for monomers A and B, respectively, then size consistency can be preserved.

In contrast, when CMOs are used for wave function expansion, decomposing the dimer Hamiltonian H(A+B) into H(A) and H(B) is not straightforward. Consequently, it is not possible to rearrange the terms in the Trotterized time evolution operator for the dimer to express it as a product of the Trotterized time evolution operators for the monomers.

## V. SUMMARY

A recent theoretical study on VQE-UCCSD highlighted that size consistency can be violated by Trotter decomposition, when the molecular orbitals delocalized over the dimer are used.<sup>29</sup> In this study, we investigated the impact of Trotter decomposition of the time evolution operator in QPE-based full-CI calculations, focusing on the size consistency condition. Our numerical simulations of the 4H/8H clusters, 2H/4H clusters, and triple bond dissociation in acetylene, using both

<!-- page-07 -->

CMOs and LMOs, revealed that the eigenphase values obtained from QPE are less sensitive to the choice of molecular orbitals when magnitude ordering is employed, and size consistency is nearly maintained when the evolution time length of a single Trotter slice is set to 0.2 or shorter. In contrast, with lexicographic ordering, size consistency is not satisfied when CMO is used in conjunction with small number of Trotter slices. However, size consistency can be systematically recovered by increasing the number of Trotter slices. The fact that QPE-based full-CI can satisfy the size consistency condition under appropriate Trotter decomposition conditions is promising for quantum chemical calculations on quantum computers. This becomes particularly relevant as large-scale quantum chemical calculations that are intractable on classical computers become feasible. The integration of QPE with fragmentation-based methods where size consistency is crucial, such as divide-and-conquer (DC),49 density matrix embedding theory (DMET),<sup>50</sup> and fragment molecular orbital (FMO)<sup>51</sup> methods, appears to be a promising direction, which will be discussed in a forthcoming paper.

#### **ACKNOWLEDGMENTS**

The computation was carried out using the JHPCN Joint Research Projects (jh240001) on supercomputer 'Flow' at Information Technology Center, Nagoya University. K. Sugisaki acknowledges Naoki Yamamoto, Takashi Abe, Yu-ya Ohnishi, Shu Kanno, and Yudai Suzuki for useful discussions. This work was supported by Quantum-LEAP Flagship Program (JPMXS0120319794) from Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan; Center of Innovations for Sustainable Quantum AI (JPMJPF2221) from Japan Science and Technology Agency (JST), Japan; and Grants-in-Aid for Scientific Research C (21K03407) and for Transformative Research Area B (23H03819) from Japan Society for the Promotion of Science (JSPS), Japan.

# **AUTHOR DECLARATIONS**

# Conflict of Interest

The author has no conflicts to disclose.

## **Author Contributions**

**Kenji Sugisaki**: Conceptualization (Lead); Software (Lead); Investigation (Lead); Validation (Lead); Writing – original draft (Lead); Writing – review and editing (Lead)

# DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

### **REFERENCES**

- <sup>1</sup>A. Aspuru-Guzik, A. D. Dutoi, P. J. Love, and M. Head-Gordon, "Simulated quantum computation of molecular energies," Science **309**, 1704–1707 (2005).
- Veis and J. Pittner, "Quantum computing applied to calculations of molecular energies: CH<sub>2</sub> benchmark," J. Chem. Phys. 133, 194106 (2010).
  M. Reiher, N. Wiebe, K. M. Svore, D. Wecker, and M. Troyer, "Elucidating reaction mechanisms on quantum computers," PNAS 114, 7555–7560 (2017).
- <sup>4</sup>C. G. R. Babbush, D. W. Berry, N. Wiebe, J. McClean, A. Paler, A. Fowler, and H. Neven, "Encoding electronic spectra in quantum circuits with linear T complexity," Phys. Rev. X 8, 041015 (2018).
- <sup>5</sup>J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean, N. Wiebe, and R. Babbush, "Even more efficient quantum computations of chemistry through tensor hypercontraction," PRX Quantum **2**, 030305 (2021).
- <sup>6</sup>N. P. Bauman, H. Liu, E. J. Bylaska, S. Krishnamoorthy, G. H. Low, C. E. Granade, N. Wiebe, A. Baker, B. Peng, M. Roetteler, and M. T. nd K. Kowalski, "Toward quantum computing for high-energy excited states in molecular systems: quantum phase estimations of core-level states," J. Chem. Theory Comput. 17, 201–210 (2021).
- <sup>7</sup>I. H. Kim, Y.-H. Liu, S. Pallister, W. Pol, S. Roberts, and E. Lee, "Fault-tolerant resource estimate for quantum chemical simulations: case study on Li-ion battery electrolyte molecules," Phys. Rev. Res. **4**, 023019 (2022).
- <sup>8</sup>R. Izsak, C. Riplinger, N. S. Blunt, B. de Souza, N. Holzmann, O. Crawford, J. Camps, F. Neese, and P. Schopf, "Quantum computing in pharma: a multilayer embedding approach for near future applications," J. Comput. Chem. 44, 406–421 (2023).
- <sup>9</sup>C. Kang, N. P. Bauman, S. Krishnamoorthy, and K. Kowalski, "Optimized quantum phase estimation for simulating electronic states in various energy regimes," J. Chem. Theory Comput. 18, 6567–6576 (2022).
- <sup>10</sup>D. Hadler, V. S. Prasannaa, V. Agarawal, and R. Maitra, "Iterative quantum phase estimation with variationally prepared reference state," Int. J. Quantum Chem. **123**, e27021 (2022).
- <sup>11</sup>P. A. M. Casares, R. Campos, and M. A. Martin-Delgado, "TFermion: a non-Clifford gate cost assessment library of quantum phase estimation algorithms for quantum chemistry," Qauntum 6, 768 (2022).
- <sup>12</sup>Y. Ino, M. Yonekawa, H. Yuzawa, Y. Minato, and K. Sugisaki, "Quantum phase estimations of benzene and its derivatives on GPGPU quantum simulators," arXiv:2312.16375 (2023).
- <sup>13</sup>M. Otten, B. Kang, D. Fedorov, A. Benali, S. Habib, Y. Alexeev, and S. K. Gray, "QREChem: quantum resource estimation software for chemistry applications," arXiv:2404.16351 (2024).
- <sup>14</sup>A. Roggero and J. Carlson, "Dynamical linear response quantum algorithm," Phys. Rev. C 100, 034610 (2019).
- <sup>15</sup> K. Sugisaki, C. Sakai, K. Toyota, K. Sato, D. Shiomi, and T. Takui, "Bayesian phase difference estimation: a general quantum algorithm for the direct calculation of energy gaps," Phys. Chem. Chem. Phys. 23, 20152– 20162 (2021).
- <sup>16</sup>K. Sugisaki, "Projective measurement-based quantum phase difference estimation algorithm for the direct computation of eigenenergy differences on a quantum computer," J. Chem. Theory Comput. 19, 7617–7625 (2023).
- <sup>17</sup>K. Kowalski, N. P. Bauman, G. H. Low, M. Roetteler, J. J. Rehr, and F. D. Vila, "Capturing many-body correlation effects with quantum and classical computing," arXiv:2402.11418 (2024).
- <sup>18</sup>R. Sakuma, S. Kanno, K. Sugisaki, T. Abe, and N. Yamamoto, "Entanglement-assisted phase estimation algorithm for calculating dynamical response functions," arXiv:2404.19554 (2024).
- <sup>19</sup>B. P. Lanyon, J. D. Whitfield, G. G. Gillett, M. E. Goggin, M. P. Almeida, I. Kassal, J. D. Biamonte, M. Mohseni, B. J. Powell, M. Barbieri, A. Aspuru-Guzik, and A. G. White, "Towards quantum chemistry on a quantum computer," Nat. Chem. 2, 106–111 (2010).
- <sup>20</sup>J. Du, N. Xu, X. Peng, P. wang, S. Wu, and D. Lu, "NMR implementation of a molecular hydrogen quantum simulation with adiabatic state preparation," Phys. Rev. Lett. **104**, 030502 (2010).
- <sup>21</sup>P. J. J. O'Malley, R. Babbush, I. D. Kivlichan, J. Romero, J. R. Mc-Clean, R. Barends, J. Kelly, P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, A. G. Fowler, E. Jeffery, E. Lucero, A. Megrant, J. Y. Mutus, M. Neeley, C. Neill, C. Quintana,

<!-- page-08 -->

- D. Sank, A. Vainsencher, J. Wenner, T. C. White, P. V. Coveney, P. J. Love, H. Neven, A. Aspuru-Guzik, and J. M. Martinis, "Scalable quantum simulation of molecular energies," Phys. Rev. X 6, 031007 (2016).
- <sup>22</sup>K. Yamamoto, S. Duffield, Y. Kikuchi, and D. Munoz Ramo, "Demonstrating Bayesian quantum phase estimation with quantum error detection," Phys. Rev. Res. 6, 013221 (2024).
- <sup>23</sup>Y. Wang, F. Dolde, J. Biamonte, R. Babbush, V. Bergholm, S. Yang, I. Jakobi, P. Neumann, A. Aspuru-Guzik, J. D. Whitfield, and J. Wrachtrup, "Quantum simulation of helium hydride cation in a sild-state spin register," ACS Nano 9, 7769–7774 (2015).
- <sup>24</sup>N. S. Blunt, L. Caune, R. Izsák, E. T. Campbell, and N. Holzmann, "Statistical phase estimation and error mitigation on a superconducting quantum processor," PRX Quantum 4, 040341 (2023).
- <sup>25</sup> A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A. Aspuru-Guzik, and J. L. O'Brien, "A variational eigenvalue solver on a photonic quantum processor," Nat. Comm. 5, 4213 (2014).
- <sup>26</sup>J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I. Rungger, G. H. Booth, and J. Tennyson, "The variational quantum eigensolver: a review of methods and best practices," Phys. Rep. 986, 1–128 (2022).
- <sup>27</sup> A. Anand, P. Schleich, S. Alperin-Lea, P. W. K. Jensen, S. Sim, M. Diaz-Tinoco, J. S. Kottmann, M. Degroote, A. F. Izmaylov, and A. Aspuru-Guzik, "A quantum computing view on unitary coupled cluster theory," Chem. Soc. Rev. 51, 1659–1684 (2022).
- <sup>28</sup>A. Szabo and N. S. Ostlund, Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory (Dover Publication Inc., Minoela, NY, 1996).
- <sup>29</sup>K. Sugisaki, T. Nakano, and Y. Mochizuki, "Size-consistency and orbital-invariance issues revealed by VQE-UCCSD calculations with the FMO scheme," J. Comput. Chem. (2024), 10.1002/jcc.27438, published online.
- <sup>30</sup> A. Y. Kitaev, "Quantum measurements and the Abelian stabilizer problem," arXiv:quant-ph/9511026 (1995).
- <sup>31</sup>D. S. Abrams and S. Lloyd, "Quantum algorithm providing exponential speed increase for finding eigenvalues and eigenvectors," Phys. Rev. Lett. 83, 5162–5165 (1999).
- <sup>32</sup>M. Born and R. Oppenheimer, "Zur quantentheorie der molekeln," Ann. Phys. 389, 457–484 (1927).
- <sup>33</sup>M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information: 10th Anniversary Edition* (Cambridge University Press, Cambridge, UK, 2010).
- <sup>34</sup>P. Jordan and E. Wigner, "Über das paulische äquivalenzverbot," Z. Phys. 47, 631–651 (1928).
- <sup>35</sup>J. T. Seeley, M. J. Richard, and P. J. Love, "The Bravyi–Kitaev transformation for quantum computation of electronic structure," J. Chem. Phys. 137, 224109 (2012).
- <sup>36</sup>D. W. Berry, A. M. Childs, R. Cleve, R. Kothari, and R. S. Somma, "Simulating Hamiltonian dynamics with a truncated Taylor series," Phys. Rev. Lett. 114, 090502 (2015).
- <sup>37</sup> A. Daskin and S. Kais, "A generalized circuit for the Hamiltonian dynamics through the truncated series," Quantum Info. Proc. 17, 328 (2018).
- <sup>38</sup>G. H. Low and I. L. Chuang, "Hamiltonian simulation by qubitization," Ouantum 3, 163 (2019).
- <sup>39</sup>D. W. Berry, C. Gidney, M. Motta, J. R. McClean, and R. Babbush, "Qubitization of arbitrary basis quantum chemistry leveraging sparsity and

- low rank factorization," Quantum 3, 208 (2019).
- <sup>40</sup>J. Paldus, P. Piecuch, L. Pylypow, and B. Jeziorski, "Application of Hilbert-space coupled-cluster theory to simple (H<sub>2</sub>)<sub>2</sub> model systems: Planar models," Phys. Rev. A 47, 2738–2782 (1993).
- <sup>41</sup>G. M. J. Barca, C. Bertoni, L. Carrington, D. Datta, N. De Silva, J. Emiliano Deustua, D. G. Fedorov, J. R. Gour, A. O. Gunina, E. Guidez, T. Harville, S. Irle, J. Ivanic, K. Kowalski, S. S. Leang, H. Li, W. Li, J. J. Lutz, I. Magoulas, J. Mato, V. Mironov, H. Nakata, B. Q. Pham, P. Piecuch, D. Poole, S. R. Pruitt, A. P. Rendell, L. B. Roskop, K. Ruedenberg, T. Sattasathuchana, M. W. Schmidt, J. Shen, L. Slipchenko, M. Sosonkina, V. Sundriyal, A. Tiwari, J. L. Galvez Vallejo, B. Westheimer, M. Wloch, P. Xu, F. Zahariev, and M. S. Gordon, "Recent developments in the general atomic and molecular electronic structure system," J. Chem. Phys. 152, 154102 (2020).
- <sup>42</sup>S. Bravyi, J. M. Gambetta, A. Mezzacapo, and K. Temme, "Tapering off qubits to simulate fermionic Hamiltonians," arXiv:1701.08213 (2017).
- <sup>43</sup>A. Tranter, P. J. Love, F. Mintert, and P. V. Coveney, "A comparison of the Bravyi-Kitaev and Jordan-Wigner transformations for the quantum simulation of quantum chemistry," J. Chem. Theory Comput. **14**, 5617–5630 (2018).
- <sup>44</sup>J. R. McClean, N. C. Rubin, K. J. Sung, I. D. Kivlichan, X. Bonet-Monroig, Y. Cao, C. Dai, E. Schuyler Fried, C. Gidney, B. Gimby, P. Gokhale, T. Häner, T. Hardikar, V. Havliček, O. Higgott, C. Huang, J. Izaac, Z. Jiang, X. Liu, S. McArdle, M. Neeley, T. O'Brien, B. O'Gorman, I. Ozfidan, M. D. Radin, J. Romero, N. P. D. Sawaya, B. Senjean, K. Setia, S. Sim, D. S. Steiger, M. Steudtner, Q. Sun, W. Sun, D. Wang, F. Zhang, and R. Babbush, "OpenFermion: the electronic structure package for quantum computers," Quantum Sci. Technol. 5, 034014 (2020).
- <sup>45</sup>Cirq Developers, "Cirq (v1.2.0)," Zenodo (2022).
- <sup>46</sup>H. Bayraktar, A. Charara, D. Clark, S. Cohen, T. Costa, Y.-L. L. Fang, Y. Gao, J. Guan, J. Gunnels, A. Haidar, A. Hehn, M. Hohnerbach, M. Jones, T. Lubowe, D. Lyakh, S. Morino, P. Springer, S. Stanwyck, I. Terentyev, S. Varadhan, J. Wong, and T. Yamaguchi, "cuQuantum SDK: A high-performance library for accelerating quantum science," arXiv:2308.01999 (2023)
- <sup>47</sup>P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, Í. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, and SciPy 1.0 Contributors, "SciPy 1.0: fundamental algorithms for scientific computing in Python," Nat. Methods 17, 261–272 (2020).
- <sup>48</sup>Y. Xiong, S. X. Ng, G.-L. Long, and L. Hanzo, "Dual-frequency quantum phase estimation mitigates the spectral leakage of quantum algorithms," IEEE Signal Proc. Lett. 22, 1222–1226 (2022).
- <sup>49</sup>W. Yang and T.-S. Lee, "A density-matrix divide-and-conquer approach for electronic structure calculations of large molecules," J. Chem. Phys. **103**, 5674–5678 (1995).
- <sup>50</sup>G. Knizia and G. K.-L. Chan, "Density matrix embedding: a simple alternative to dynamical mean-field theory," Phys. Rev. Lett. **109**, 186404 (2012).
- <sup>51</sup>K. Kitaura, E. Ikeo, T. Asada, T. Nakano, and M. Uebayasi, "Fragment molecular orbital method: an approximate computational method for large molecules," Chem. Phys. Lett. 313, 701–706 (1999).