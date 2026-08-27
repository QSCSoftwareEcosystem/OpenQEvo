# Size-consistency and orbital-invariance issues revealed by VQE-UCCSD calculations with the FMO scheme

Kenji Sugisaki $^{a,b,c,\dagger}$ , Tatsuya Nakano $^d$ , Yuji Mochizuki $^{e,f,\ddagger}$

- <sup>a</sup> Graduate School of Science and Technology, Keio University, 7-1 Shinkawasaki, Saiwai-ku, Kawasaki, Kanagawa 212-0032, Japan
  - <sup>b</sup> Quantum Computing Center, Keio University, 3-14-1 Hiyoshi, Kohoku-ku Yokohama, Kanagawa 223-8522. Japan
- <sup>c</sup> Centre for Quantum Engineering, Research and Education, TCG Centres for Research and Education in Science and Technology, Sector V, Salt Lake, Kolkata 700091, India
  - <sup>d</sup>Division of Medicinal Safety Science, National Institute of Health Sciences, 1-18-1 Kamiyoga, Setaqaya-ku, Tokyo 158-8501, Japan
  - <sup>e</sup>Department of Chemistry and Research Center for Smart Molecules, Faculty of Science, Rikkyo University, 3-34-1 Nishi-ikebukuro, Toshima-ku, Tokyo 171-8501, Japan
- f Institute of Industrial Science, The University of Tokyo, 4-6-1 Komaba, Meguro-ku, Tokyo 153-8505,

  Japan

 $^\dagger \mbox{Corresponding author: ksugisaki@keio.jp, $^\sharp fullmoon@rikkyo.ac.jp}$

2nd version for arXiv, 2024/3/13, JST

## Abstract

The fragment molecular orbital (FMO) scheme is one of the popular fragmentation-based methods and has the potential advantage of making the circuit flat in quantum chemical calculations on quantum computers. In this study, we used a GPU-accelerated quantum simulator (cuQuantum) to perform the electron correlation part of the FMO calculation as unitary coupled-cluster singles and doubles (UCCSD) with the variational quantum eigensolver (VQE) for hydrogen-bonded (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O systems with the STO-3G basis set. VQE-UCCD calculations were performed using both canonical and localized MO sets, and the results were examined from the point of view of size-consistency and orbital-invariance affected by the Trotter error. It was found that the use of localized MO leads to better results, especially for (FH)<sub>2</sub>-H<sub>2</sub>O. The GPU acceleration was substantial for the simulations with larger numbers of qubits, and was about a factor of 6.7–7.7 for 18 qubit systems.

## **Keywords**

FMO, UCC, GPU, VQE, Trotter Error

## 1. Introduction

Starting with the seminal work of Aspuru-Guzik et al. [1], quantum chemical computation has been actively explored and developed as a promising application area for quantum computers [2–6], where the potential applicability to huge-scale configuration interactions such as the FeMo-cofactor of nitrogenase [7] is attractive with care for the setting of active orbital space [8]. In practice, however, the development of computational methods and algorithms using quantum simulators is currently more mainstream than the use of actual devices. For noisy intermediate-scale quantum (NISQ) computers, the unitary coupled-cluster singles and doubles (UCCSD) [9–16] has been used for relatively small molecules in conjunction with the variational quantum eigensolver (VQE) [17–20], and this VQE-UCCSD scheme has been extended to multi-reference cases, e.g., Refs. [21–24]. In addition, GPU-accelerated simulators e.g., cuQuantum [25] have attracted considerable interest due to its pronounced performance [26].

In another direction, the so-called problem decomposition approach has been introduced to shallow the circuit depth [27] while avoiding the effects of noise. Note that such an approach is rather common for large molecules (like proteins) as the fragmentation-based methods [28–30]. The introduction of problem decomposition to quantum computation was pioneered by Yamazaki et al. [31], who compared three methods of fragment molecular orbital (FMO) [32], divide-and-conquer (DC) [33], and density matrix embedding theory (DMET) [34]. Recently, the FMO calculations with VQE-UCCSD for hydrogen clusters have been reported [35]. Note that the  $(H_2)_2$ , trans-butadiene, and  $[Cr_2(OH)_3(NH_3)_6]^{3+}$  systems were treated by UCCSD based on the concept of orbital locality [36].

In this study, we applied the VQE-UCCSD scheme [17–20] to compute the electron correlation part of FMO calculations [32, 37, 38] for a couple of hydrogen-bonded systems, (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O. For execution, the cuQuantum simulator [25] was used as done in the previous study [26]. Effect of Trotterization on the orbital-invariance condition of the UCCSD method was investigated using two symmetrically equivalent FH molecules in the latter system. We also studied relationship between the size-consistency condition and the Trotterized UCCSD ansatz, using square tetrahydrogen (4H) and cuboid octahydrogen (8H) clusters. Acceleration of the VQE-UCCSD simulations using cuQuantum is also discussed. The rest of the paper is organized as follows: In Section 2, we describe the calculation methods of both FMO stage and VQE-UCCSD stages. The results of the FMO correlation energies are shown first, and then

the issues surrounding the Trotter error are discussed in Section 3. In Section 4, we summarize our work and discuss possible directions for future work.

### 2. Method of calculation

#### 2.1. FMO scheme and program

The scheme of the basic two-body FMO calculation [32, 37, 38] is summarized as follows. The first step is to determine the molecular orbital and electron density of each monomer by the Hartree–Fock (HF) approximation [39] under a given basis function, while self-consistently imposing an electrostatic potential (ESP) on each other. The set of ESPs of the monomers is to be determined until the monomer self-consistent-charge (SCC) condition is satisfied by iterations. This allows the polarization of each monomer to be taken into account. In the next step, the monomer-determined ESP is used to calculate the HF for the dimer; no SCC condition is imposed. The dimer calculation takes into account the delocalization of electrons between the monomers. From the sum of the HF energies of the monomer and the dimer, the two-body FMO energy of the system of interest is given as in Eq. (1)

$$E^{\text{FMO}} = \sum_{I>J} E_{IJ} - (N_f - 2) \sum_{I} E_{I}. \tag{1}$$

Indices of I and J specify the respective monomers, and  $N_f$  is the number of fragments.

Electron correlation calculations, such as second-order Møller-Plesset perturbation (MP2) [39], are performed after the HF calculations for each monomer are complete and after the individual HF calculations for each dimer are complete. The correlation energy correction is done in an additive manner as in Eq. (1). The introduction of electron correlations is essential to improve quantitatively by incorporating dispersion stabilization and reducing excess ionicities of the HF description. As described in Ref. [39], both size-consistency and orbital-invariance are crucial requirements in the correlated methods. This is obviously true for the FMO scheme based on Eq. (1).

Currently, GAMESS-US [40, 41], PAICS [42, 43], and ABINIT-MP [44, 45] are the available programs that can perform FMO calculations including electron correlation correction by MP2. Besides the MP2 capability [46–48], ABINIT-MP is unique in supporting higher-order correlated calculations [39, 49] on-the-fly; from the third-order MP (MP3) [50] to coupled-cluster singles and doubles including perturbative triples (CCSD(T)) [51] are supported.

![](_page_4_Picture_0.jpeg)

FIG. 1. Molecular structures of (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O. For the former, the middle, upper, and lower FH molecules correspond to fragments "1", "2", and "3", respectively. For the latter, the H<sub>2</sub>O molecule is assigned to fragment "1"; two FH molecules (fragments "2" (upper) and "3" (lower)) are equivalent due to the C<sub>2v</sub> symmetry.

TABLE I. Optimized Cartesian coordinates in units of Å.

| Seq.              | Frag. | Elem.        | X         | У         | $\mathbf{z}$ |
|-------------------|-------|--------------|-----------|-----------|--------------|
| $(FH)_3$          |       |              |           |           |              |
| 1                 | 1     | $\mathbf{F}$ | 0.779023  | 0.287467  | 0.000000     |
| 2                 | 1     | Η            | 0.000000  | 0.807300  | 0.000000     |
| 3                 | 2     | $\mathbf{F}$ | -1.361653 | 1.874668  | 0.000000     |
| 4                 | 2     | Η            | -1.330503 | 2.801407  | 0.000000     |
| 5                 | 3     | $\mathbf{F}$ | 0.648089  | -2.399606 | 0.000000     |
| 6                 | 3     | Η            | 0.741364  | -1.471463 | 0.000000     |
| $(FH)_2$ - $H_2O$ |       |              |           |           |              |
| 1                 | 1     | O            | 0.000000  | 0.000000  | 1.200039     |
| 2                 | 1     | Η            | 0.000000  | 0.771251  | 1.779594     |
| 3                 | 1     | Η            | 0.000000  | -0.771251 | 1.779594     |
| 4                 | 2     | $\mathbf{F}$ | 0.000000  | 2.034006  | -0.694256    |
| 5                 | 2     | Η            | 0.000000  | 1.179139  | -0.331451    |
| 6                 | 3     | $\mathbf{F}$ | 0.000000  | -2.034006 | -0.694256    |
| 7                 | 3     | Η            | 0.000000  | -1.179139 | -0.331451    |

#### 2.2. Preparation of molecular integrals under FMO scheme

The geometries of (FH)<sub>3</sub> (under  $C_s$  symmetry) and (FH)<sub>2</sub>-H<sub>2</sub>O ( $C_{2v}$  symmetry) were optimized by the GAUSSIAN16W program [52] at the level of B3LYP [53] corrected with the empirical dispersion [54] with the 6-31+G(d',p') basis set [55]. The resulting Cartesian coordinates are listed in TABLE I and illustrated in FIG. 1.

For (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O, the FMO calculations were performed with the STO-3G minimal basis set [56], where we used a local version of ABINIT-MP, which dumped the integral list of basis functions

and the converged canonical MO (CMO) coefficients (at the FMO-HF level) of monomers and dimers as separate files. These data were transformed by a small Fortran program into molecular integrals for the second-quantized Hamiltonian used to run VQE-UCCSD, expressed as

$$H = \sum_{pq} h_{pq} a_p^{\dagger} a_q + \frac{1}{2} \sum_{pqrs} g_{pqrs} a_p^{\dagger} a_q^{\dagger} a_s a_r.$$
 (2)

Indices of p, q, r and s cover the correlating orbital space, and  $h_{pq}$  and  $g_{pqrs}$  are the transformed oneand two-electron integrals. The 1s-like CMOs of fluorine and oxygen were frozen [57] for  $h_{pq}$  in Eq. (2), which is a good approximation to save on the number of qubits [58, 59]. The number of correlated electrons for dimers was thus 16.

Note that there is some degree of locality of monomer CMOs in dimer orbitals with respect to the occupied space for (FH)<sub>3</sub> and also that there is the symmetric delocalization for the FH dimer in (FH)<sub>2</sub>-H<sub>2</sub>O. To address the issue of size-consistency, the Pipek–Mezey localization[60] was performed for the valence occupied CMOs and the virtual CMOs, respectively, and these sets of localized MOs (LMOs) were also used for the integral transformation. The lists of molecular orbitals (CMOs and LMOs) of for the monomers and dimers of (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O are shown in FIG. S1 and S2, respectively, in Supplementary Materials.

Due to a proof-of-concept (PoC) phase of this study, the FMO calculations (at the HF level) by ABINIT-MP were done in a separate step from the quantum calculations described in the next subsection. For comparison with the VQE-UCCSD correlation energies, the usual FMO-MP2 and FMO-CCSD(T) calculations were also performed by ABINIT-MP. These calculations were completed in less than 1 second on a single core of Intel Xeon processor.

#### 2.3. Set-up of VQE-UCCSD calculation

VQE is a quantum–classical hybrid algorithm and it has been proposed to solve quantum chemistry problems using NISQ devices [17, 18]. In VQE, an approximate wave function is generated by using a parameterized quantum circuit (PQC) defined by an "ansatz", and the expectation value of the qubit Hamiltonian obtained by applying the fermion–qubit transformation to the second-quantized Hamiltonian given in Eq. (2) is computed statistically, by repeatedly executing the quantum circuit and collecting the measurement results. The classical computer then execute a variational optimization of the parameters

in PQC. These steps are iterated until convergence.

Various types of ansatzes have been proposed and studied for quantum chemical calculations [61]. In this work, we adopted the UCCSD ansatz defined in Eqs. (3) and (4), because it is a chemically motivated ansatz and it can give very accurate correlation energies.

$$|\Psi_{\text{UCCSD}}\rangle = e^{T - T^{\dagger}} |\Psi_{\text{HF}}\rangle.$$
 (3)

$$T = \sum_{ia} t_i^a a_a^{\dagger} a_i + \frac{1}{2} \sum_{ijab} t_{ij}^{ab} a_a^{\dagger} a_b^{\dagger} a_j a_i.$$
 (4)

Here, we used the indices i and j for the occupied spin orbitals and a and b for the unoccupied orbitals of the HF wave function  $|\Psi_{\rm HF}\rangle$ . To accelerate the VQE simulations, we adopted the following techniques: (1) Using the symmetry conserving Bravyi–Kitaev transformation (SCBKT) [62] to reduce two qubits in the simulation, (2) using the MP3 and the MP2 excitation amplitudes as the initial guess of the  $t_i^a$  and  $t_{ij}^{ab}$ , respectively [24], and (3) GPU-based numerical simulations. The number of qubits for the VQE-UCCSD simulations was 8 and 18 for monomers and dimers, respectively, in (FH)<sub>3</sub>, and 10 for monomer "1" and 20 for dimers "21" and "31" in (FH)<sub>2</sub>-H<sub>2</sub>O. The VQE-UCCSD simulation program was developed by us, by using Python3 with OpenFermion [63], Cirq [64], and cuQuantum [25] libraries.

In the implementation of the UCCSD quantum circuit, we adopted the first-order Trotter decomposition given in Eq. (5) in conjunction with the magnitude ordering [65] of the cluster operators.

$$\exp\left(T - T^{\dagger}\right) = \exp\left(\sum_{k=1}^{K} i t_k P_k\right) \approx \left[\prod_{k=1}^{K} e^{i t_k P_k / M}\right]^M \tag{5}$$

Here,  $\sum_{k=1}^{K} it_k P_k$  is the excitation/de-excitation operators in the Pauli operator expressions obtained by adopting the SCBKT to the operator  $(T - T^{\dagger})$  in the second-quantized form.  $P_k$  is a direct product of Pauli operators called as a Pauli string, and  $t_k$  is the corresponding coefficient derived from  $t_i^a$  and  $t_{ij}^{ab}$ . K is the number of Pauli strings, and M is the number of Trotter slices. Unless otherwise specified we used the one Trotter slice (M = 1) for the VQE-UCCSD simulations.

For the variational optimization of the excitation amplitudes, we examined COBYLA [66] and Powell [67] algorithms; the corresponding labels are shortly denoted as UCCSD:CB and UCCSD:PW, respectively (see TABLE II and III). For comparison, the calculation of the complete active space configuration

interaction (CAS-CI) was performed to obtain the exact correlation energy in the orbital space of STO-3G. The numerical simulations for (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O were carried out on the Supercomputer 'Flow' Type-II subsystem at Nagoya University and on the in-house NVIDIA DGX H100 system, respectively.

## 3. Results and discussion

#### 3.1. Energies and timings

The correlation energies for (FH)<sub>3</sub> are summarized in TABLE II. Compared to MP2, CCSD has a significantly lower energy, and CCSD(T) gives values close to CAS-CI, as expected. UCCSD:PW gave lower energies than UCCSD:CB, but the number of function evaluations (total energy calculations) required in Powell is about 1.6–2.8 times greater than in COBYLA (see TABLE S1 in Supplementary Materials for details). The same trend was observed for the LMO-based UCCSD calculations. No significant difference was found in the number of function evaluations between CMO and LMO-based calculations.

As we discuss in the next section, Trotterized UCCSD does not automatically satisfy the size-consistency condition, and using LMOs as the basis is crucial to ensure that Trottterized UCCSD is size-consistent. In fact, the correlation energies of the dimers are improved in the LMO-based UCCSD:PW calculations, and the sum of the correlation energies is 0.001679 Hartree (1.0536 kcal mol<sup>-1</sup>) lower in the LMO-based calculations than in the CMO-based one. The deviation of the sum of UCCSD:PW correlation energy from the CAS-CI one is 0.71 kcal mol<sup>-1</sup>.

TABLE III summarizes the results for the (FH)<sub>2</sub>-H<sub>2</sub>O correlation energies. The number of function evaluations in the VQE-UCCSD optimization is given in TABLE S2 in Supplementary Materials. A checkpoint here is whether the equivalence symmetries (monomers "2" and "3" / dimers "21" and "31") are satisfied, and the usual MP2, CCSD, CCSD(T), and CAS-CI results all satisfy this requirement. The trend of the correlation energies by these methods is the same as in (FH)<sub>3</sub>. On the other hand, the UCCSD results (of both COBYLA and Powell) unfortunately do not satisfy symmetry, as the difference is seen to five decimal places for monomers and three decimal places (in the order of kcal mol<sup>-1</sup>) for dimers. From a chemical precision point of view, it seems problematic that the effect is seen to three decimal places. Furthermore, this issue of broken equivalence should be kept in mind not only for FMO, but for

TABLE II. Correlation energies of (FH)<sub>3</sub><sup>a</sup> in units of Hartree.

| Unit    | MP2       | CCSD      | CCSD(T)   | UCCS               | SD:CB     | UCCS      | D:PW         | CAS-CI    |
|---------|-----------|-----------|-----------|--------------------|-----------|-----------|--------------|-----------|
|         |           |           |           | $\mathrm{CMO^{b}}$ | $LMO^{c}$ | CMO       | $_{\rm LMO}$ |           |
| Monomer |           |           |           |                    |           |           |              |           |
| "1"     | -0.017933 | -0.026945 | -0.026945 | -0.026884          | -0.026854 | -0.026914 | -0.026729    | -0.026945 |
| "2"     | -0.017526 | -0.026216 | -0.026216 | -0.026164          | -0.026169 | -0.026192 | -0.026019    | -0.026216 |
| "3"     | -0.017933 | -0.026929 | -0.026929 | -0.026899          | -0.026839 | -0.026875 | -0.026691    | -0.026929 |
| Dimer   |           |           |           |                    |           |           |              |           |
| "21"    | -0.035493 | -0.051856 | -0.051933 | -0.049880          | -0.050429 | -0.050452 | -0.051322    | -0.051963 |
| "31"    | -0.035980 | -0.052778 | -0.052850 | -0.051554          | -0.051632 | -0.051527 | -0.052169    | -0.052879 |
| "32"    | -0.035446 | -0.053122 | -0.053123 | -0.051952          | -0.051317 | -0.053067 | -0.052692    | -0.053124 |
|         |           |           |           |                    |           |           |              |           |
| Sum.    | -0.053527 | -0.077666 | -0.077816 | -0.073439          | -0.073516 | -0.075065 | -0.076744    | -0.077876 |

<sup>&</sup>lt;sup>a</sup> The HF energies (in units of Hartree) of monomer "1", "2", and "3" are -103.815720, -103.995064, -103.563842, respectively. In contrast, the HF energies of dimer "21", "31", "32" are -228.173251, -227.542281, -218.792929, respectively. The sum of Eq. (1) is -363.133835 Hartree. Eq. (1) is also used for the sum of correlation energies.

all approaches of fragmentation-oriented methods [28–30]. This problem of VQE-UCCSD is related to the Trotter error and is discussed in the next section.

The effect of orbital localization on the UCCSD correlation energy is remarkable in the (FH)<sub>2</sub>-H<sub>2</sub>O system. In the UCCSD:PW calculations the sum of correlation energies improved about 0.005256 Hartree (3.2982 kcal mol<sup>-1</sup>) by the orbital localization, and deviation from the CAS-CI correlation energy is 1.29 kcal mol<sup>-1</sup>. Note that orbital localization also improves the orbital-invariance condition. By using the LMOs, the difference in correlation energy between "21" and "31" is reduced to 0.039 kcal mol<sup>-1</sup>. These results exemplify the importance of using LMOs in the combination of FMO and VQE-UCCSD approaches.

The cuQuantum quantum simulator was used in this VQE-UCCSD computation. TABLE IV summarizes the timings of the UCCSD jobs of (FH)<sub>3</sub> using LMOs on the 'Flow' Type-II subsystem with and without GPU. The GPU acceleration was about a factor of 1.6–2.2 and 6.7–7.7 for monomers and dimers, respectively. The VQE-UCCSD simulations of the dimers "21" and "31" of (FH)<sub>2</sub>-H<sub>2</sub>O (20 qubit systems) without GPU acceleration are too time-consuming to do. Here we estimated the acceleration ratio by performing the UCCSD simulations of the dimer "21" of (FH)<sub>2</sub>-H<sub>2</sub>O by setting the maximum number of function evaluations in the VQE parameter optimization to be 100 on NVIDIA DGX H100. With the GPU acceleration, the time required for pre-processing (Fermion–qubit transformation, reference CAS-CI

<sup>&</sup>lt;sup>b</sup> HF canonical orbitals were used for the calculation.

<sup>&</sup>lt;sup>c</sup> Localied molecular orbitals constructed by using Pipek–Mezey method were used for the calculation.

TABLE III. Correlation energies of (FH)<sub>2</sub>-H<sub>2</sub>O<sup>a</sup> in units of Hartree.

| Unit    | MP2       | CCSD      | CCSD(T)   | UCCS             | D:CB      | UCCS      | D:PW         | CAS-CI    |
|---------|-----------|-----------|-----------|------------------|-----------|-----------|--------------|-----------|
|         |           |           |           | $\mathrm{CMO^b}$ | $LMO^{c}$ | CMO       | $_{\rm LMO}$ |           |
| Monomer |           |           |           |                  |           |           |              |           |
| "1"     | -0.035370 | -0.049321 | -0.049394 | -0.049242        | -0.049214 | -0.049231 | -0.048915    | -0.049445 |
| "2"     | -0.017810 | -0.026705 | -0.026705 | -0.026608        | -0.026648 | -0.026692 | -0.026538    | -0.026705 |
| "3"     | -0.017810 | -0.026705 | -0.026705 | -0.026677        | -0.026637 | -0.026659 | -0.026476    | -0.026705 |
| Dimer   |           |           |           |                  |           |           |              |           |
| "21"    | -0.053486 | -0.075392 | -0.075526 | -0.069313        | -0.071305 | -0.071421 | -0.074429    | -0.075600 |
| "31"    | -0.053486 | -0.075392 | -0.075526 | -0.071847        | -0.069583 | -0.072544 | -0.074367    | -0.075600 |
| "32"    | -0.035790 | -0.053549 | -0.053553 | -0.053230        | -0.052161 | -0.053207 | -0.052979    | -0.053549 |
|         |           |           |           |                  |           |           |              |           |
| Sum.    | -0.071770 | -0.101602 | -0.101801 | -0.091863        | -0.090551 | -0.094590 | -0.099846    | -0.101895 |

a The HF energies in units of Hartree of monomer "1", "2", and "3" are -84.426515, -103.695254, and -103.695254, respectively ("2" and "3" are equivalent). In contrast, the HF energies of dimer "21", "31", "32" are -207.357701, -207.357701, and -220.935631, respectively ("21" and "31" are equivalent). The sum of Eq. (1) is -343.834010 Hartree. Eq. (1) is also used for the sum of correlation energies.

calculation, MP2 and MP3 calculations, etc.) was 4773.9 seconds and 100 function evaluations in the VQE optimization took 1211.0 seconds. In contrast, the CPU-only calculation took 4421.2 and 37363.9 seconds for pre-processing and 100 function calls, respectively. The GPU acceleration of the VQE iteration part is about a factor of 30.85. Since the numbers of function evaluations required for convergence in UCCSD:CB and UCCSD:PW were 4913 and 12452, respectively, the time for the CPU-only simulations are estimated to be about 21 and 54 days for UCCSD:CB and UCCSD:PW, respectively. GPU acceleration is substantial for larger systems, but the speedup is less significant compared with our previous study [26]. This is because the VQE job needs a lot of time for pre-processing and post-processing, and these parts cannot be accelerated by cuQuantum. Considering that a normal FMO-CCSD(T)/STO-3G calculation takes less than 1 second to complete, there is a speed difference of the order of the fourth power of 10 if the correlation part is due to VQE-UCCSD at this time. Note that the present VQE-UCCSD was run on a classical computer, where computational time grows exponentially with the number of qubits. Anyway, as in the previous report [26], GPU acceleration with cuQuantum is essential for quantum simulations.

#### 3.2. Relation with Trotter error

It is interesting to note that the monomers "2" and "3" of (FH)<sub>2</sub>-H<sub>2</sub>O are symmetrically equivalent, but VQE-UCCSD yields different correlation energies. The HF canonical orbitals of the monomers "2"

<sup>&</sup>lt;sup>b</sup> HF canonical orbitals were used for the calculation.

<sup>&</sup>lt;sup>c</sup> Localied molecular orbitals constructed by using Pipek–Mezey method were used for the calculation.

TABLE IV. Timings of UCCSD job (in second) of (FH)<sub>3</sub> using LMOs with/without GPU.<sup>a</sup>

| Unit    |          | UCCSD:CB    |              | UCCSD:PW |             |              |  |
|---------|----------|-------------|--------------|----------|-------------|--------------|--|
|         | with GPU | without GPU | Acceleration | with GPU | without GPU | Acceleration |  |
| Monomer |          |             |              |          |             |              |  |
| "1"     | 17.2     | 27.8        | 1.62         | 27.6     | 48.3        | 1.75         |  |
| "2"     | 15.5     | 33.6        | 2.17         | 28.5     | 55.4        | 1.94         |  |
| "3"     | 16.2     | 26.8        | 1.65         | 26.5     | 49.3        | 1.86         |  |
| Dimer   |          |             |              |          |             |              |  |
| "21"    | 12767.5  | 93205.0     | 7.30         | 34153.3  | 260996.7    | 7.64         |  |
| "31"    | 13947.1  | 94199.7     | 6.75         | 34397.3  | 237695.3    | 6.91         |  |
| "32"    | 8805.9   | 59975.6     | 6.81         | 21129.0  | 156257.2    | 7.40         |  |

<sup>&</sup>lt;sup>a</sup> All the calculations were carried out on 'Flow' Type-II subsystem.

![](_page_10_Picture_3.jpeg)

FIG. 2. Active orbitals of FH molecules (monomers "2" and "3") of  $(FH)_2$ -H<sub>2</sub>O. Red arrows specify the electron occupancy of the HF wave function.

and "3" are illustrated in FIG. 2. We found that the relative phase from the second to the fifth molecular orbitals is different (or inverted) between monomers "2" and "3", which causes changes in the absolute sign of the some excitation amplitudes  $t_i^a$  and  $t_{ij}^{ab}$ . As a result, the quantum states corresponding to the UCCSD wave function are not identical for monomers "2" and "3", and the Trotter error appears in a different way. This fact is confirmed by performing the UCCSD calculations without Trotterization, using the expm\_multiply function in the SciPy library [68], which allows us to compute the action of the matrix exponential of  $(T - T^{\dagger})$  on  $|\Psi_{\rm HF}\rangle$ . In this case, the calculated correlation energies of the monomers "2" and "3" are exactly the same: -0.026687 Hartree. The fact that Trotterized UCCSD can

TABLE V. Deviations of the UCCSD:PW total energy from the CAS-CI value for 4H cluster (monomer) and 8H cluster (dimer).

| TT                    | m 1                   | A E /1 1 1-1                       |
|-----------------------|-----------------------|------------------------------------|
| $\operatorname{Unit}$ | Trotter decomposition | $\Delta E/\mathrm{kcal\ mol^{-1}}$ |
| Monomer               | No                    | 0.8118                             |
| Dimer (LMO)           | No                    | 1.6236                             |
| Dimer (CMO)           | No                    | 1.6234                             |
| Monomer               | Yes                   | 0.8102                             |
| Dimer (LMO)           | Yes                   | 1.6207                             |
| Dimer (CMO)           | Yes                   | 5.0319                             |

not maintain orbital-invariance indicates that care must be taken to ensure that the relative phases of the molecular orbitals match at all points when calculating potential energy surfaces.

Since the Trotter errors appears in an unexpected way, we further investigated about the relationship between Trotter errors and the size-consistency, which is an essential condition in the FMO framework as mentioned earlier. Here we focused on the tetrahydrogen (4H) cluster [69] in a square coordinate with R(H-H) = 1.0583 Å (2.0 Bohr) as the monomer, because the Trotter error becomes more significant when the HF is not a good approximation of the ground-state wave function and the UCCSD wave function has large excitation amplitudes. This system is also suitable because the HF CMOs are completely defined by point-group symmetry. In the dimer (8H) calculations, two 4H clusters were placed to form a cuboid, with the inter-monomer distance being 100 Å. Two types of molecular orbitals are examined in the dimer calculations: Completely delocalized canonical orbitals by HF in  $D_{2h}$  point group and LMOs on the monomers. In the total energy calculations using UCCSD:PW, we used cuQuantum-based quantum circuit simulations with Trotter decomposition and without Trotter decomposition using the expm\_multiply function in SciPy. The results are summarized in TABLE V.

From TABLE V, the UCCSD calculations without Trotter decomposition yield almost the same  $\Delta E$  values for both LMO- and CMO-based calculations, and the  $\Delta E$  values of the dimer are twice those of the monomer; i.e., Trotter-free UCCSD satisfies the size-consistency condition. Small differences in the  $\Delta E$  values of the dimer with CMO and LMO are due to rounding errors in the AO  $\rightarrow$  MO transformation. In contrast, when the Trotter decomposition is used to construct the UCCSD quantum circuit, the  $\Delta E$  of the dimer with CMO is significantly larger than the  $2 \times \Delta E$  (Monomer). Since the  $\Delta E$  value for dimer with LMO is approximately twice the  $\Delta E$  of monomer, we concluded that the size-consistency condition

of the VQE-UCCSD can be maintained when the molecular orbitals localized on each monomer are used in the calculations.

In the present study, we used the first-order Trotter decomposition given in Eq. (5), with the number of Trotter slices M=1. To further investigate the relationship between Trotter error and the size-consistency, we run the UCCSD:PW simulations with M changed from 1 to 5. We also carried out the UCCSD:PW simulations with the second-order Trotter decomposition given in Eq. (6).

$$\exp\left(T - T^{\dagger}\right) = \exp\left(\sum_{j=1}^{J} i t_j P_j\right) \approx \left[\prod_{j=1}^{J} e^{i t_j P_j / 2M} \prod_{j=J}^{1} e^{i t_j P_j / 2M}\right]^M \tag{6}$$

The results are summarized in TABLE S3 in the Supplementary Materials. The simulations ended within one hour when GPU is used. The UCCSD:PW energies of monomer (4H cluster) and dimer (8H cluster) with LMO do not change by using a larger number of Trotter slices or by adopting the second-order Trotter decomposition. For the dimer calculations with CMO, in contrast, the deviation from the CAS-CI energy systematically decreases with increasing M. However, even for M=5, the UCCSD:PW energy does not converge to the Trotter-free UCCSD energy calculated by using expm\_multiply in SciPy. This result also implies the importance of using LMO in the FMO scheme in conjunction with the VQE-UCCSD.

Since size-consistency is pivotal not only for FMO but also for general quantum chemical calculations, it is important to provide methods to estimate the Trotter error-free energy. Here we examined the extrapolation method to infer the Trotter error-free UCCSD energy using the idea of algorithmic error mitigation [70]. To do this, we plotted the UCCSD:PW energies as a function of the inverse of the number of Trotter slices, 1/M, and fitted with a function  $E = \alpha(1/M)^{\beta} + \gamma$ . It should be noted that in the context of Hamiltonian simulations, the error of the first-order Trotter decomposition scales as O(1/M) [71]. In VQE, however, different Trotterized versions of the UCCSD correspond to different ansatzes, and thus the optimal variational parameters are different. Therefore, it is not necessary to scale the Trotter error of UCCSD as O(1/M). The calculation results are illustrated in FIG. 3. The E(UCCSD:PW) were successfully fitted by the function  $E = 0.005396(1/M)^{3.6466} - 3.876244$ , and the difference between the energies estimated from the extrapolation and the Trotter error-free one calculated with expm\_multiply is only 35  $\mu$ Hartree. We expect that the extrapolation method used in this work will help to obtain the VQE-UCCSD energy with the size-consistency condition.

![](_page_13_Figure_0.jpeg)

FIG. 3. The plot of the UCCSD:PW energies of 8H cluster with different number of Trotter slices M and the result of extrapolation.

It should be noted that the dependence of the Trotter error on the locality of the molecular orbitals was investigated by Babbush and coworkers [72], and they reported that the Trotter error is larger for localized orbital basis than for canonical orbitals and natural orbitals. The reported study focused only on single molecule (monomer), and our discussions are based on comparing the energies of monomers and a dimer. Our results do not contradict this previous study.

# 4. Summary

We have performed the VQE-UCCSD calculations [16–20] using the cuQuantum simulator [25] in conjunction with the FMO calculations for the (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O systems. The STO-3G minimal basis set [56] was used and the frozen-core restriction [57] was imposed. By combining with symmetry conserving Bravyi–Kitaev transformation [62], we can simulate the HF···H<sub>2</sub>O dimer with 20 qubits. Both COBYLA and Powell methods were used for VQE optimization, with the latter usually providing better energies but requires more function calls. When the HF CMOs were used for the UCCSD wave function expansion, the calculated correlation energies were somewhat small in magnitude, possibly due to the breakdown of the size-consistency condition. By using the LMOs, the UCCSD correlation energies improved dramatically, and the differences in the correlation energies between the CAS-CI and the UCCSD

in conjunction with the Powell optimizer were calculated to be 0.71 and 1.29 kcal mol<sup>-1</sup> for (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O, respectively. The (FH)<sub>2</sub>-H<sub>2</sub>O system has two symmetrically equivalent FH molecules that should have the same energies, but the Trotterized UCCSD does not satisfy symmetry and yields different energies. The difference in correlation energies between the dimers "21" and "31" is on the order of 1 kcal mol<sup>-1</sup> in the canonical orbital basis but it reduced to 0.039 kcal mol<sup>-1</sup> in the localized orbital basis. Size-consistency of the Trotterized UCCSD is also studied numerically using 4H and 8H model clusters. We found that the size-consistency condition can be broken when the molecular orbitals delocalized to the dimer are used for the calculation, and using molecular orbitals localized to the monomers is essential to satisfy the size-consistency. These findings on the relationship between size-consistency and orbital-invariance [39, 49] and the error in the Trotter decomposition are very important not only for FMO-based quantum chemical calculations and other fragmentation-oriented methods [28–30] but also for VQE-UCCSD in general. From the numerical simulations, we also demonstrated that the Trotter error-free UCCSD energy can be estimated by means of extrapolation by computing the UCCSD energies with different numbers of Trotter slices.

The GPU acceleration was found to be 7.30 and 7.64 with COBYLA and Powell algorithms, respectively, for the dimer "21" of (FH)<sub>3</sub> (18 qubit system). For the dimer "21" of (FH)<sub>2</sub>-H<sub>2</sub>O, the estimated GPU acceleration ratio of the VQE quantum circuit simulation to be about 30.85, and the VQE simulations of the dimer "21" with COBYLA and Powell will take about 21 and 54 days, respectively. The usefulness of GPUs has attracted much attention in various fields of quantum computation [73], and quantum chemistry is an example where the acceleration effect is significant [74], including in this case; even with GPU acceleration, it still takes orders of magnitude longer than a regular FMO-CCSD(T) calculation [51]. Recently, an example of large-scale quantum computation with adamantanes has been reported using VQE [75]. Following these trends, we will perform larger FMO-UCCSD computations on upcoming GPU environments.

# 5. Acknowledgement

All VQE-UCCSD computations with cuQuantum on the 'Flow' Type-II subsystem at the Information Technology Center of Nagoya University were performed under the JHPCN Joint Research Projects (jh230001 subject by YM). KS and YM would like to thank Profs. Takahiro Katagiri (Nagoya University) and Satoshi Ohshima (Kyushu University) for their encouragement. YM was also supported by Rikkyo SFR. KS acknowledges the support from Quantum Leap Flagship Program (Grant No. JP-MXS0120319794) from MEXT, Japan, Center of Innovations for Sustainable Quantum AI (JPMJPF2221) from JST, Japan, and KAKENHI Transformative Research Area B (23H03819) and Scientific Research C (21K03407) from JSPS, Japan.

- [1] A. Aspuru-Guzik, A. D. Dutoi, P. J. Love, and M. Head-Gordon. Simulated quantum computation of molecular energies. *Science*, 309:1704–1707, 2005.
- [2] Y. Cao, J. Romero, J. P. Olson, M. Degroote, P. D. Johnson, M. Kieferová, I. D. Kivlichan, T. Menke, B. Peropadre, N. P. D. Sawaya, S. Sim, L. Veis, and A. Aspuru-Guzik. Quantum chemistry in the age of quantum computing. *Chem. Rev.*, 119:10856–10915, 2019.
- [3] S. McArdle, S. Endo, A. Aspuru-Guzik, S. C. Benjamin, and X. Yuan. Quantum computational chemistry. Rev. Mod. Phys., 92:015003, 2020.
- [4] B. Bauer, S. Bravyi, M. Motta, and G. K.-L. Chan. Quantum algorithms for quantum chemistry and quantum materials science. *Chem. Rev.*, 120:12685–12717, 2020.
- [5] M. Motta and J. E. Rice. Emerging quantum computing algorithms for quantum chemistry. WIREs Comput. Mol. Sci., 12:e1580, 2022.
- [6] S. Lee, J. Lee, H. Zhai, Y. Tong, A. M. Dalzell, A. Kumar, P. Helms, J. Gray, Z.-H. Cui, W. Liu, M. Kastoryano, R. Babbush, J. Preskill, D. R. Reichman, E. T. Campbell, E. F. Valeev, L. Lin, and G. K.-L. Chan. Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry. *Nat. Comm.*, 14:1952, 2023.
- [7] M. Reiher, N. Wiebe, K. M. Svore, D. Wecker, and M. Troyer. Elucidating reaction mechanisms on quantum computers. PNAS, 114:7555-7560, 2017.
- [8] Z. Li, J. Li, N. S. Dattani, C. J. Umrigar, and G. K.-L. Chan. The electronic complexity of the ground-state of the femo cofactor of nitrogenase as relevant to quantum simulations. *J. Chem. Phys.*, 150:024302, 2019.
- [9] R. Yaris. Linked-cluster theorem and unitarity. J. Chem. Phys., 41:2419-2421, 1964.
- [10] R. Yaris. Cluster expansions and the unitary group. J. Chem. Phys., 42:3019–3024, 1965.
- [11] K. Tanaka and H. Terashima. A cluster expansion theory with multireference functions using the unitary ansatz. Chem. Phys. Lett., 106:558–562, 1984.
- [12] R. J. Bartlett, S. A. Kucharski, and Jozef Noga. Alternative coupled-cluster ansätze ii. the unitary coupled-cluster method. Chem. Phys. Lett., 155:133–140, 1989.
- [13] W. Kutzelnigg. Error analysis and improvements of coupled-cluster theory. Theor. Chim. Acta, 80:349–386, 1991.
- [14] A. G. Taube and R. J. Bartlett. New perspectives on unitary coupled-cluster theory. Int. J. Quantum Chem., 106:3393–3401, 2006.
- [15] G. Harsha, T. Shiozaki, and G. E. Scuseria. On the difference between variational and unitary coupled cluster theories. J. Chem. Phys., 148:044107, 2018.
- [16] A. Anand, P. Schleich, S. Alperin-Lea, P. W. K. Jensen, S. Sim, M. Díaz-Tinoco, J. S. Kottmann, M. Degroote, A. F. Izmaylov, and A. Aspuru-Guzik. A quantum computing view on unitary coupled cluster theory. *Chem. Soc. Rev.*, 51:1659–1684, 2022.
- [17] M.-H. Yung, J. Casanova, A. Mezzacapo, J. McClean, L. Lamata, A. Aspuru-Guzik, and E. Solano. From transistor to trapped-ion computers for quantum chemistry. Sci. Rep., 4:3589, 2014.
- [18] A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A. Aspuru-Guzik, and J. L. O'Brien. A variational eigenvalue solver on a photonic quantum processor. *Nat. Comm.*, 5:4213, 2014.
- [19] J. Romero, R. Babbush, J. R. McClean, C. Hempel, P. J. Love, and A. Aspuru-Guzik. Strategies for quantum computing molecular energies using the unitary coupled cluster ansatz. *Quantum Sci. Technol.*, 4:014008, 2018.
- [20] S. Guo, J. Sun, H. Qian, M. Gong, Y. Zhang, F. Chen, Y. Ye, Y. Wu, S. Cao, K. Liu, C. Zha, C. Ying, Q. Zhu, H.-L. Huang, Y. Zhao, S. Li, S. Wang, J. Yu, D. Fan, D. Wu, H. Su, H. Deng, H. Rong, Y. Li, K. Zhang, T.-H. Chung, F. Liang, J. Lin, Y. Xu, L. Sun, C. Guo, N. Li, Y.-H. Huo, C.-Z. Peng, C.-Y. Lu, X. Yuan, X. Zhu, and J.-W. Pan. Experimental quantum computational chemistry with optimised unitary coupled cluster ansatz. arXiv:2212.08006v2, 2022.
- [21] J. Lee, W. J. Huggins, M. Head-Gordon, and K. B. Whaley. Generalized unitary coupled cluster wave functions for quantum computation. J. Chem. Theory Comput., 15:311–324, 2019.
- [22] N. H. Stair, R. Huang, and F. A. Evangelista. A multireference quantum Krylov algorithm for strongly correlated electrons. J. Chem. Theory Comput., 16:2236–2245, 2020.
- [23] G. Greene-Diniz and D. M. Ramo. Generalized unitary coupled cluster excitations for multireference molecular states optimized by the variational quantum eigensolver. *Int. J. Quantum Chem.*, 121:e26352, 2021.
- [24] K. Sugisaki, T. Kato, Y. Minato, K. Okuwaki, and Y. Mochizuki. Variational quantum eigensolver simulations with the multireference unitary coupled cluster ansatz: a case study of the C<sub>2v</sub> quasi-reaction pathway of

- beryllium insertion into a H<sub>2</sub> molecule. Phys. Chem. Chem. Phys., 24:8439–8452, 2022.
- [25] H. Bayraktar, A. Charara, D. Clark, S. Cohen, T. Costa, Y.-L. L. Fang, Y. Gao, J. Guan, J. Gunnels, A. Haidar, A. Hehn, M. Hohnerbach, M. Jones, T. Lubowe, D. Lyakh, S. Morino, P. Springer, S. Stanwyck, I. Terentyev, S. Varadhan, J. Wong, and T. Yamaguchi. cuQuantum SDK: A high-performance library for accelerating quantum science. arXiv:2308.01999v1, 2023.
- [26] K. Sugisaki, V. S. Prasannaa, S. Ohshima, T. Katagiri, Y. Mochizuki, B. K. Sahoo, and B. P. Das. Bayesian phase difference estimation algorithm for direct calculation of fine structure splitting: accelerated simulation of relativistic and quantum many-body effects. *Electron. Struct.*, 5:035006, 2023.
- [27] K. Dalton, C. K. Long, Y. S. Yordanov, C. G. Smith, C. H. W. Barnes, N. Mertig, and D. R. M. Arvidsson-Shukur. Quantifying the effect of gate errors on variational quantum eigensolvers for quantum chemistry. npj Quantum Info., 10:18, 2024.
- [28] M. S. Gordon, D. G. Fedorov, S. R. Pruitt, and L. V. Slipchenko. Fragmentation methods: A route to accurate calculations on large systems. *Chem. Rev.*, 112:632–672, 2012.
- [29] M. A. Collins and R. P. A. Bettens. Energy-based molecular fragmentation methods. Chem. Rev., 115:5607–5642, 2015.
- [30] K. Raghavachari and A. Saha. Accurate composite and fragment-based quantum chemical models for large molecules. Chem. Rev., 115:5643–5677, 2015.
- [31] T. Yamazaki, S. Matsuura, A. Narimani, A. Saidmuradov, and A. Zaribafiyan. Towards the practical application of near-term quantum computers in quantum chemistry simulations: A problem decomposition approach. arXiv:1806.01305v1, 2018.
- [32] K. Kitaura, E. Ikeo, T. Asada, T. Nakano, and M. Uebayasi. Fragment molecular orbital method: an approximate computational method for large molecules. Chem. Phys. Lett., 313:701–706, 1999.
- [33] T. Akama, M. Kobayashi, and H. Nakai. Implementation of divide-and-conquer method including Hartree-Fock exchange interaction. J. Comput. Chem., 28:2003–2012, 2007.
- [34] G. Knizia and G. K.-L. Chan. Density matrix embedding: A simple alternative to dynamical mean-field theory. Phys. Rev. Lett., 109:186404, 2012.
- [35] H. Lim, D. H. Kang, J. Kim, A. Pellow-Jarman, S. McFarthing, R. Pellow-Jarman, H.-N. Jeon, B. Oh, J.-K. K. Rhee, and K. T. No. Fragment molecular orbital-based variational quantum eigensolver for quantum chemistry in the age of quantum computing. Sci. Rep., 14:2422, 2024.
- [36] M. Otten, M. R. Hermes, R. Pandharkar, Y. Alexeev, S. K. Gray, and L. Gagliardi. Localized quantum chemistry on quantum computers. J. Chem. Theory Comput., 18:7205-7217, 2022.
- [37] D. Fedorov and K. Kitaura, editors. The Fragment Molecular Orbital Method: Practical Applications to Large Molecular Systems. CRC Press, Florida, 2009.
- [38] Y. Mochizuki, S. Tanaka, and K. Fukuzawa, editors. Recent Advances of the Fragment Molecular Orbital Method - Enhanced Performance and Applicability. Springer, Berlin, 2021.
- [39] A. Szabo and N. S. Ostlund. Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory. Macmillan Publishing, New York, 1982.
- [40] D. G. Fedorov. The fragment molecular orbital method: theoretical development, implementation in GAMESS, and applications. WIREs Comput. Mol. Sci., 7:e1322, 2017.
- [41] D. G. Fedorov. Recent development of the fragment molecular orbital method in GAMESS. In Y. Mochizuki, S. Tanaka, and K. Fukuzawa, editors, Recent Advances of the Fragment Molecular Orbital Method: Enhanced Performance and Applicability, pages 31–51. Springer, Berlin, 2021.
- [42] T. Ishikawa, T. Ishikura, and K. Kuwata. Theoretical study of the prion protein based on the fragment molecular orbital method. J. Comput. Chem., 30:2594–2601, 2009.
- [43] T. Ishikawa. PAICS: Development of an open-source software of fragment molecular orbital method for biomolecule. In Y. Mochizuki, S. Tanaka, and K. Fukuzawa, editors, Recent Advances of the Fragment Molecular Orbital Method: Enhanced Performance and Applicability, pages 69-76. Springer, Berlin, 2021.
- [44] S. Tanaka, Y. Mochizuki, Y. Komeiji, Y. Okiyama, and K. Fukuzawa. Electron-correlated fragment-molecular-orbital calculations for biomolecular and nano systems. Phys. Chem. Chem. Phys., 16:10310–10344, 2014.
- [45] Y. Mochizuki, T. Nakano, K. Sakakura, Y. Okiyama, H. Watanabe, K. Kato, Y. Akinaga, S. Sato, J. Yamamoto, K. Yamashita, T. Murase, T. Ishikawa, Y. Komeiji, Y. Kato, N. Watanabe, T. Tsukamoto, H. Mori, K. Okuwaki, S. Tanaka, A. Kato, C. Watanabe, and K. Fukuzawa. The ABINIT-MP program. In Y. Mochizuki, S. Tanaka, and K. Fukuzawa, editors, Recent Advances of the Fragment Molecular Orbital Method: Enhanced Performance and Applicability, pages 53–67. Springer, Berlin, 2021.
- [46] Y. Mochizuki, T. Nakano, S. Koikegami, S. Tanimori, Y. Abe, U. Nagashima, and K. Kitaura. A parallelized integral-direct second-order Møller–Plesset perturbation theory method with a fragment molecular orbital

- scheme. Theor. Chem. Acc., 112:442–452, 2004.
- [47] Y. Mochizuki, S. Koikegami, T. Nakano, S. Amari, and K. Kitaura. Large scale MP2 calculations with fragment molecular orbital scheme. Chem. Phys. Lett., 396:473–479, 2004.
- [48] Y. Mochizuki, K. Yamashita, T. Murase, T. Nakano, K. Fukuzawa, K. Takematsu, H. Watanabe, and S. Tanaka. Large scale FMO-MP2 calculations on a massively parallel-vector computer. *Chem. Phys. Lett.*, 457:396–403, 2008.
- [49] I. Shavitt and R. J. Bartlett. Many-Body Methods in Chemistry and Physics: MBPT and Coupled-Cluster Theory. Cambridge University Press, Cambridge, 2009.
- [50] Y. Mochizuki, K. Yamashita, K. Fukuzawa, K. Takematsu, H. Watanabe, N. Taguchi, Y. Okiyama, M. Tsuboi, T. Nakano, and S. Tanaka. Large-scale FMO-MP3 calculations on the surface proteins of influenza virus, hemagglutinin (HA) and neuraminidase (NA). Chem. Phys. Lett., 493:346–352, 2010.
- [51] Y. Mochizuki, K. Yamashita, T. Nakano, Y. Okiyama, K. Fukuzawa, N. Taguchi, and S. Tanaka. Higher-order correlated calculations based on fragment molecular orbital scheme. *Theor. Chem. Acc.*, 130:515–530, 2011
- [52] M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone, G. A. Petersson, H. Nakatsuji, X. Li, M. Caricato, A. V. Marenich, J. Bloino, B. G. Janesko, R. Gomperts, B. Mennucci, H. P. Hratchian, J. V. Ortiz, A. F. Izmaylov, J. L. Sonnenberg, D. Williams-Young, F. Ding, F. Lipparini, F. Egidi, J. Goings, B. Peng, A. Petrone, T. Henderson, D. Ranasinghe, V. G. Zakrzewski, J. Gao, N. Rega, G. Zheng, W. Liang, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, K. Throssell, J. A. Montgomery, Jr., J. E. Peralta, F. Ogliaro, M. J. Bearpark, J. J. Heyd, E. N. Brothers, K. N. Kudin, V. N. Staroverov, T. A. Keith, R. Kobayashi, J. Normand, K. Raghavachari, A. P. Rendell, J. C. Burant, S. S. Iyengar, J. Tomasi, M. Cossi, J. M. Millam, M. Klene, C. Adamo, R. Cammi, J. W. Ochterski, R. L. Martin, K. Morokuma, O. Farkas, J. B. Foresman, and D. J. Fox. Gaussian 16, Revision B.01, 2016. Gaussian Inc. Wallingford CT.
- [53] A. D. Becke. A new mixing of Hartree–Fock and local density-functional theories. J. Chem. Phys., 98:1372– 1377, 1993.
- [54] S. Grimme, J. Antony, S. Ehrlich, and H. Krieg. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. J. Chem. Phys., 132:154104, 2010
- [55] G. A. Petersson and M. A. Al-Laham. A complete basis set model chemistry. II. Open-shell systems and the total energies of the first-row atoms. J. Chem. Phys., 94:6081–6090, 1991.
- [56] W. J. Hehre, R. F. Stewart, and J. A. Pople. Self-consistent molecular-orbital methods. I. Use of Gaussian expansions of Slater-type atomic orbitals. J. Chem. Phys., 51:2657–2664, 1969.
- [57] R. P. Hosteny, T. H. Dunning Jr., R. R. Gilman, A. Pipano, and I. Shavitt. Ab initio study of the π-electron states of trans-butadiene. J. Chem. Phys., 62:4764–4779, 1975.
- [58] A. J. McCaskey, Z. P. Parks, J. Jakowski, S. V. Moore, T. D. Morris, T. S. Humble, and R. C. Pooser. Quantum chemistry as a benchmark for near-term quantum computers. npj Quantum Info., 5:99, 2019.
- [59] Y. Mochizuki, K. Okuwaki, T. Kato, and Y. Minato. Reduction of orbital space for molecular orbital calculations with quantum computation simulator for educations. ChemRxiv.9863810.v1, 2019.
- [60] J. Pipek and P. G. Mezey. A fast intrinsic localization procedure applicable for ab-initio and semiempirical linear combination of atomic orbital wave functions. J. Chem. Phys., 90:4916–4926, 1989.
- [61] J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I. Rungger, G. H. Booth, and J. Tennyson. The variational quantum eigensolver: A review of methods and best practices. *Phys. Rep.*, 986:1–128, 2022.
- [62] S. Bravyi, J. M. Gambetta, A. Mezzacapo, and K. Temme. Tapering off qubits to simulate fermionic Hamiltonians. arXiv:1701.08213v1, 2017.
- [63] J. R. McClean, N. C. Rubin, K. J. Sung, I. D. Kivlichan, X. Bonet-Monroig, Y. Cao, C. Dai, E. S. Fried, C. Gidney, B. Gimby, P. Gokhale, T. Häner, T. Hardikar, V. Havlíček, O. Higgott, C. Huang, J. Izaac, Z. Jiang, X. Liu, S. McArdle, J. Romero, N. P. D. Sawaya, B. Senjean, K. Setia, S. Sim, D. S. Steiger, M. Steudtner, Q. Sun, W. Sun, D. Wang, F. Zhang, and R. Babbush. OpenFermion: the electronic structure package for quantum computers. Quantum Sci. Technol., 5:034014, 2020.
- [64] Cirq developers. Cirq (v1.2.0). Zenodo. https://doi.org/10.5281/zenodo.8161252.
- [65] A. Tranter, P. J. Love, F. Mintert, and P. V. Coveney. A comparison of the Bravyi-Kitaev and Jordan-Wigner transformations for the quantum simulation of quantum chemistry. J. Chem. Theory Comput., 14:5617–5630, 2018.
- [66] M. J. D. Powell. A direct search optimization method that models the objective and constraint functions

- by linear interpolation. In S. Gomez and J.-P. Hennart, editors, Advances in Optimization and Numerical Analysis, pages 51–67. Springer, Dordrecht, 1994.
- [67] M. J. D. Powell. An efficient method for finding the minimum of a function of several variables without calculating derivatives. Comp. J., 7:155–162, 1964.
- [68] P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, Í. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, and SciPy 1.0 Contributors. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nat. Methods, 17:261–272, 2020.
- [69] J. Paldus, P. Piecuch, L. Pylypow, and B. Jeziorski. Application of Hilbert-space coupled-cluster theory to simple (H<sub>2</sub>)<sub>2</sub> model systems: Planar models. *Phys. Rev. A*, 47:2738–2782, 1993.
- [70] S. Endo, Q. Zhao, Y. Li, S. Benjamin, and X. Yuan. Mitigating algorithmic errors in a Hamiltonian simulation. Phys. Rev. A, 99:012334, 2019.
- [71] M. A. Nielsen and I. L. Chuang. Quantum Computation and Quantum Information: 10th Anniversary Edition. Cambridge University Press, Cambridge, 2010.
- [72] R. Babbush, J. McClean, D. Wecker, A. Aspuru-Guzik, and N. Wiebe. Chemical basis of Trotter-Suzuki errors in quantum chemistry simulation. *Phys. Rev. A*, 91:022311, 2015.
- [73] M. Möller and C. Vuik. On the impact of quantum computing technology on future developments in high-performance scientific computing. Ethics Info. Technol., 19:253–269, 2017.
- [74] Y. Ino, M. Yonekawa, H. Yuzawa, Y. Minato, and K. Sugisaki. Quantum phase estimations of benzene and its derivatives on GPGPU quantum simulators. arXiv:2312.16375v1, 2023.
- [75] V. K. Prasad, F. Cheng, U. Fekl, and H.-A. Jacobsen. Applications of noisy quantum computing and quantum error mitigation to "adamantaneland": a benchmarking study for quantum chemistry. *Phys. Chem. Chem. Phys.*, 26:4071–4082, 2024.

# Supplementary Materials

TABLE S1. The number of function evaluations in the VQE-UCCSD parameter optimization of  $(FH)_3$ .

| Unit    | CMO    | O      | LMO    |        |  |
|---------|--------|--------|--------|--------|--|
|         | COBYLA | Powell | COBYLA | Powell |  |
| Monomer |        |        |        |        |  |
| "1"     | 115    | 225    | 133    | 256    |  |
| "2"     | 130    | 257    | 113    | 257    |  |
| "3"     | 119    | 193    | 125    | 241    |  |
| Dimer   |        |        |        |        |  |
| "21"    | 1762   | 4783   | 1924   | 5264   |  |
| "31"    | 1963   | 4765   | 2085   | 5188   |  |
| "32"    | 1910   | 5408   | 1546   | 5188   |  |

TABLE S2. The number of function evaluations in the VQE-UCCSD parameter optimization of (FH)<sub>2</sub>-H<sub>2</sub>O.

| Unit    | CMO    | O      | LMO    |        |  |
|---------|--------|--------|--------|--------|--|
|         | COBYLA | Powell | COBYLA | Powell |  |
| Monomer |        |        |        |        |  |
| "1"     | 262    | 401    | 474    | 791    |  |
| "2"     | 114    | 238    | 142    | 246    |  |
| "3"     | 121    | 215    | 129    | 207    |  |
| Dimer   |        |        |        |        |  |
| "21"    | 3278   | 12448  | 4913   | 12452  |  |
| "31"    | 3511   | 11966  | 4568   | 12764  |  |
| "32"    | 1348   | 2544   | 1342   | 3882   |  |

TABLE S3. The difference of the UCCSD:PW energies from the CAS-CI values of 4H cluster (monomer) and 8H cluster (dimer) calculated with different Trotter decomposition conditions, in units of kcal  $\mathrm{mol}^{-1}$

| Unit        | First-order Trotter  |        |        |        | Second-order Trotter | expm_multiply <sup>a</sup> |        |
|-------------|----------------------|--------|--------|--------|----------------------|----------------------------|--------|
|             | $M = 1^{\mathrm{b}}$ | M = 2  | M = 3  | M = 4  | M = 5                | M = 1                      |        |
| Monomer     | 0.8102               | 0.8101 | 0.8099 | 0.8100 | 0.8100               | 0.8101                     | 0.8118 |
| Dimer (LMO) | 1.6207               | 1.6200 | 1.6203 | 1.6204 | 1.6205               | 1.6206                     | 1.6236 |
| Dimer (CMO) | 5.0319               | 1.9139 | 1.7141 | 1.6681 | 1.6496               | 2.0172                     | 1.6234 |

 $<sup>^{\</sup>rm a}$  Trotter-free implementation using  ${\tt expm\_multiply}$  in SciPy library.

 $<sup>^{\</sup>rm b}$  M represents the number of Trotter slices.

![](_page_21_Figure_0.jpeg)

FIG. S1. Active orbitals of monomers and dimers of  $(FH)_3$ . CMO and LMO stand for the HF canonical molecular orbitals and the localized molecular orbitals constructed by using Pipek–Mezey method, respectively. Red arrows specify the electron occupancy of the HF wave function.

![](_page_22_Figure_0.jpeg)

FIG. S2. Active orbitals of monomers and dimers of  $(FH)_2$ - $H_2O$ . CMO and LMO stand for the HF canonical molecular orbitals and the localized molecular orbitals constructed by using Pipek–Mezey method, respectively. Red arrows specify the electron occupancy of the HF wave function.