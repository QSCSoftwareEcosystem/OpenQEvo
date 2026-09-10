DOI: 10.1002/jcc.27438

# RESEARCH ARTICLE

![](_page_0_Picture_7.jpeg)

# Size-consistency and orbital-invariance issues revealed by VQE-UCCSD calculations with the FMO scheme

Kenji Sugisaki <sup>1,2,3</sup> | Tatsuya Nakano <sup>4</sup> | Yuji Mochizuki <sup>5,6</sup> |

#### Correspondence

Kenji Sugisaki, Graduate School of Science and Technology, Keio University, 7-1 Shinkawasaki Saiwai-ku, Kawasaki, Kanagawa 212-0032, Japan. Email: ksugisaki@keio.jp

#### Present address

Tatsuya Nakano, Department of HPC Support, Research Organization for Information Science and Technology, Kobe, Japan.

#### **Funding information**

Ministry of Education, Culture, Sports, Science and Technology; Japan Society for the Promotion of Science; Japan Science and Technology Agency; Rikkyo SFR

#### **Abstract**

The fragment molecular orbital (FMO) scheme is one of the popular fragmentation-based methods and has the potential advantage of making the circuit shallow for quantum chemical calculations on quantum computers. In this study, we used a GPU-accelerated quantum simulator (cuQuantum) to perform the electron correlation part of the FMO calculation as unitary coupled-cluster singles and doubles (UCCSD) with the variational quantum eigensolver (VQE) for hydrogen-bonded (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O systems with the STO-3G basis set. VQE-UCCSD calculations were performed using both canonical and localized MO sets, and the results were examined from the point of view of size-consistency and orbital-invariance affected by the Trotter error. It was found that the use of localized MO leads to better results, especially for (FH)<sub>2</sub>-H<sub>2</sub>O. The GPU acceleration was substantial for the simulations with larger numbers of qubits, and was about a factor of 6.7–7.7 for 18 qubit systems.

#### KEYWORDS

fragment molecular orbital, GPU, Trotter error, UCC, variational quantum eigensolver

# 1 | INTRODUCTION

Starting with the seminal work of Aspuru-Guzik et al., 1 quantum chemical computation has been actively explored and developed as a promising application area for quantum computers, 2-6 where the potential applicability to huge-scale configuration interactions such as the FeMo-cofactor of nitrogenase 7 is attractive with care for the setting of active orbital space. 8 In practice, however, the development of computational methods and algorithms using quantum simulators is currently more mainstream than the use of actual

devices. For noisy intermediate-scale quantum (NISQ) computers, the unitary coupled-cluster singles and doubles (UCCSD) <sup>9-17</sup> has been used for relatively small molecules in conjunction with the variational quantum eigensolver (VQE), <sup>18-21</sup> and this VQE-UCCSD scheme has been extended to multi-reference cases, for example, References 22-25. In addition, GPU-accelerated simulators e.g., cuQuantum <sup>26</sup> have attracted considerable interest due to its pronounced performance.<sup>27</sup>

In another direction, the so-called problem decomposition approach has been introduced to shallow the circuit depth <sup>28</sup> while avoiding the effects of noise. Note that such an approach is rather

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

© 2024 The Author(s). Journal of Computational Chemistry published by Wiley Periodicals LLC.

![](_page_0_Picture_32.jpeg)

 $<sup>^{1}\</sup>mbox{Graduate}$  School of Science and Technology, Keio University, Kawasaki, Japan

 $<sup>^2\</sup>mbox{Quantum}$  Computing Center, Keio University, Yokohama, Japan

<sup>3</sup>Centre for Quantum Engineering, Research and Education, TCG Centres for Research and Education in Science and Technology, Kolkata, India

<sup>&</sup>lt;sup>4</sup>Division of Medicinal Safety Science, National Institute of Health Sciences, Kawasaki, Japan

<sup>&</sup>lt;sup>5</sup>Department of Chemistry and Research Center for Smart Molecules, Faculty of Science, Rikkyo University, Toshima-ku, Japan

<sup>&</sup>lt;sup>6</sup>Institute of Industrial Science, The University of Tokyo, Meguro-ku, Japan

common for large molecules (like proteins) as the fragmentation-based methods. <sup>29–31</sup> The introduction of problem decomposition to quantum computation was pioneered by Yamazaki et al., <sup>32</sup> who compared three methods of fragment molecular orbital (FMO), <sup>33</sup> divide-and-conquer (DC), <sup>34</sup> and density matrix embedding theory (DMET). <sup>35</sup> Recently, the FMO calculations with VQE-UCCSD for hydrogen clusters have been reported. <sup>36</sup> In addition, the Gagliardi group has promoted the quantum calculations based on the concept of orbital locality, <sup>37–39</sup> and also Tsuchimochi et al. have proposed a many-body expansion of UCCSD energy. <sup>40</sup> It may be worth emphasizing here that FMO also divides the larger problem by a kind of locality assumption.

The present attempt to combine FMO and quantum computation is a touchstone project, and its primary purpose is to investigate whether there are any fundamental problems before application calculations. In the future, it is envisioned that the active site of a metal-containing protein (just like FeMoco <sup>7</sup>) will be handled by a UCCSD system calculation (assuming multi-referencing <sup>25</sup> is necessary) to avoid configuration explosion under the approximation of a multilayer FMO,<sup>41</sup> which will be an example of "realistic hybrid use" of ordinary and quantum computers.

In this study, we applied the VQE-UCCSD scheme 18-21 to compute the electron correlation part of FMO calculations 33,42,43 for a couple of hydrogen-bonded systems, (FH)3 and (FH)2-H2O. For the present execution, the cuQuantum simulator 26 was used as done in the previous study.<sup>27</sup> Effect of Trotterization on the orbital-invariance condition of the UCCSD method was investigated using two symmetrically equivalent FH molecules in the latter system. We also studied relationship between the size-consistency condition and the Trotterized UCCSD ansatz, using square tetrahydrogen (4H) and cuboid octahydrogen (8H) clusters. Acceleration of the VQE-UCCSD simulations using cuQuantum is also discussed. The rest of the paper is organized as follows: In Section 2, we describe the calculation methods of both FMO stage and VQE-UCCSD stages. The results of the FMO correlation energies are shown first, and then the issues surrounding the Trotter error are discussed in Section 3. In Section 4, we summarize our work and discuss possible directions for future work.

# 2 | METHOD OF CALCULATION

# 2.1 | FMO scheme and program

The scheme of the basic two-body FMO calculation <sup>33,42,43</sup> is summarized as follows. The first step is to determine the molecular orbital and electron density of each monomer by the Hartree–Fock (HF) approximation <sup>44</sup> under a given basis function, while self-consistently imposing an electrostatic potential (ESP) on each other. The set of ESPs of the monomers is to be determined until the monomer self-consistent-charge (SCC) condition is satisfied by iterations. This allows the polarization of each monomer to be taken into account. In the next step, the monomer-determined ESP is used to calculate the HF for the dimer; no SCC condition is imposed.

The dimer calculation takes into account the delocalization of electrons between the monomers. From the sum of the HF energies of the monomer and the dimer, the two-body FMO energy of the system of interest is given as in Equation (1)

$$E^{\text{FMO}} = \sum_{I>I} E_{IJ} - (N_f - 2) \sum_{I} E_{I}. \tag{1}$$

Indices of I and J specify the respective monomers, and  $N_f$  is the number of fragments.

Electron correlation calculations, such as second-order Møller-Plesset perturbation (MP2),<sup>44</sup> are performed after the HF calculations for each monomer are complete and after the individual HF calculations for each dimer are complete. The correlation energy correction is done in an additive manner as in Equation (1). The introduction of electron correlations is essential to improve quantitatively by incorporating dispersion stabilization and reducing excess ionicities of the HF description. As described in Reference 44, both size-consistency and orbital-invariance are crucial requirements in the correlated methods. This is obviously true for the FMO scheme based on Equation (1).

Currently, GAMESS-US, <sup>45,46</sup> PAICS, <sup>47,48</sup> and ABINIT-MP <sup>49,50</sup> are the available programs that can perform FMO calculations including electron correlation correction by MP2. Besides the MP2 capability, <sup>51–53</sup> ABINIT-MP is unique in supporting higher-order correlated calculations <sup>44,54</sup> on-the-fly; from the third-order MP (MP3) <sup>55</sup> to coupled-cluster singles and doubles including perturbative triples (CCSD(T)) <sup>56</sup> are supported.

# 2.2 | Preparation of molecular integrals under FMO scheme

The geometries of (FH)<sub>3</sub> (under  $C_s$  symmetry) and (FH)<sub>2</sub>-H<sub>2</sub>O ( $C_{2v}$  symmetry) were optimized by the GAUSSIAN16W program <sup>57</sup> at the level of B3LYP <sup>58</sup> corrected with the empirical dispersion <sup>59</sup> with the 6-31+G(d', p') basis set. <sup>60</sup> The resulting Cartesian coordinates are listed in Table 1 and illustrated in Figure 1.

For  $(FH)_3$  and  $(FH)_2$ - $H_2O$ , the FMO calculations were performed with the STO-3G minimal basis set, <sup>61</sup> where we used a local version of ABINIT-MP, which dumped the integral list of basis functions and the converged canonical MO (CMO) coefficients (at the FMO-HF level) of monomers and dimers as separate files. These data were transformed by a small Fortran program into molecular integrals for the second-quantized Hamiltonian used to run VQE-UCCSD, expressed as

$$H = \sum_{pq} h_{pq} a_p^{\dagger} a_q + \frac{1}{2} \sum_{pqrs} g_{pqrs} a_p^{\dagger} a_q^{\dagger} a_s a_r. \tag{2}$$

Indices of p, q, r and s cover the correlating orbital space, and  $h_{pq}$  and  $g_{pqrs}$  are the transformed one- and two-electron integrals. The 1s-like CMOs of fluorine and oxygen were frozen <sup>62</sup> for  $h_{pq}$  in Equation (2),

**TABLE 1** Optimized Cartesian coordinates in units of Å.

| Seq.                                | Frag. | Elem. | x         | у         | z         |
|-------------------------------------|-------|-------|-----------|-----------|-----------|
| (FH) <sub>3</sub>                   |       |       |           |           |           |
| 1                                   | 1     | F     | 0.779023  | 0.287467  | 0.000000  |
| 2                                   | 1     | Н     | 0.000000  | 0.807300  | 0.000000  |
| 3                                   | 2     | F     | -1.361653 | 1.874668  | 0.000000  |
| 4                                   | 2     | Н     | -1.330503 | 2.801407  | 0.000000  |
| 5                                   | 3     | F     | 0.648089  | -2.399606 | 0.000000  |
| 6                                   | 3     | Н     | 0.741364  | -1.471463 | 0.000000  |
| (FH) <sub>2</sub> -H <sub>2</sub> O |       |       |           |           |           |
| 1                                   | 1     | 0     | 0.000000  | 0.000000  | 1.200039  |
| 2                                   | 1     | Н     | 0.000000  | 0.771251  | 1.779594  |
| 3                                   | 1     | Н     | 0.000000  | -0.771251 | 1.779594  |
| 4                                   | 2     | F     | 0.000000  | 2.034006  | -0.694256 |
| 5                                   | 2     | Н     | 0.000000  | 1.179139  | -0.331451 |
| 6                                   | 3     | F     | 0.000000  | -2.034006 | -0.694256 |
| 7                                   | 3     | Н     | 0.000000  | -1.179139 | -0.331451 |

![](_page_2_Picture_5.jpeg)

**FIGURE 1** Molecular structures of (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O. For the former, the middle, upper, and lower FH molecules correspond to fragments "1", "2", and "3", respectively. For the latter, the H<sub>2</sub>O molecule is assigned to fragment "1"; two FH molecules (fragments "2" (upper) and "3" (lower)) are equivalent due to the  $C_{2v}$  symmetry.

which is a good approximation to save on the number of qubits.<sup>63,64</sup> The number of correlated electrons for dimers was thus 16.

Note that there is some degree of locality of monomer CMOs in dimer orbitals with respect to the occupied space for (FH) $_3$  and also that there is the symmetric delocalization for the FH dimer in (FH) $_2$ -H $_2$ O. To address the issue of size-consistency, the Pipek–Mezey localization $^{65}$  was performed for the valence occupied CMOs and the virtual CMOs, respectively, and these sets of localized MOs (LMOs) were also used for the integral transformation. The lists of molecular orbitals (CMOs and LMOs) for the monomers and dimers of (FH) $_3$  and (FH) $_2$ -H $_2$ O are shown in Figures S1 and S2, respectively, in Supplementary Materials.

Due to a proof-of-concept (PoC) phase of this study, the FMO calculations (at the HF level) by ABINIT-MP were done in a separate step from the quantum calculations described in the next subsection. For comparison with the VQE-UCCSD correlation energies, the usual

FMO-MP2 and FMO-CCSD(T) calculations were also performed by ABINIT-MP. These calculations were completed in less than 1 s on a single core of Intel Xeon processor.

# 2.3 | Set-up of VQE-UCCSD calculation

VQE is a quantum-classical hybrid algorithm and it has been proposed to solve quantum chemistry problems using NISQ devices. <sup>18.19</sup> In VQE, an approximate wave function is generated by using a parameterized quantum circuit (PQC) defined by an "ansatz", and the expectation value of the qubit Hamiltonian obtained by applying the fermion-qubit transformation to the second-quantized Hamiltonian given in Equation (2) is computed statistically, by repeatedly executing the quantum circuit and collecting the measurement results. The classical computer then execute a variational optimization of the parameters in PQC. These steps are iterated until convergence.

Various types of ansatzes have been proposed and studied for quantum chemical calculations.<sup>66</sup> In this work, we adopted the UCCSD ansatz defined in Equations (3) and (4), because it is a chemically motivated ansatz and it can give very accurate correlation energies.

$$|\Psi_{\text{UCCSD}}\rangle = e^{T-T^{\dagger}}|\Psi_{\text{HF}}\rangle.$$
 (3)

$$T = \sum_{ia} t^a_i a^{\dagger}_a a_i + \frac{1}{2} \sum_{iiab} t^{ab}_{ij} a^{\dagger}_a a^{\dagger}_b a_j a_i. \tag{4}$$

Here, we used the indices i and j for the occupied spin orbitals and a and b for the unoccupied orbitals of the HF wave function  $|\Psi_{HF}\rangle$ . To accelerate the VOE simulations, we adopted the following techniques: (1) Using the symmetry conserving Bravyi-Kitaev transformation (SCBKT) <sup>67</sup> to reduce two qubits in the simulation, (2) using the MP3 and the MP2 excitation amplitudes as the initial guess of the  $t_i^a$  and  $t_{ii}^{ab}$ , respectively, 25 and (3) GPU-based numerical simulations. The number of gubits for the VQE-UCCSD simulations was 8 and 18 for monomers and dimers, respectively, in (FH)3, and 10 for monomer "1" and 20 for dimers "21" and "31" in (FH)2-H2O. The VQE-UCCSD simulation program was developed by us, by using Python3 with OpenFermion,<sup>68</sup> Cirq,<sup>69</sup> and cuQuantum <sup>26</sup> libraries. It is desirable to use larger basis sets, such as 6-31G(d), to analyze the FMO correlation energies and Trotter effects on the UCCSD ansatz in more detail. However, the VQE-UCCSD simulations for more than 20 qubits are quite challenging, because the simulation time grows exponentially with the number of qubits. Increasing the variational parameters also makes the VQE optimization difficult. Note that the number of variational parameters is 10 (FH; 8 qubits), 34 (H<sub>2</sub>O; 10 qubits), 132 ((FH)<sub>2</sub> under C<sub>s</sub> point group; 18 qubits), and 306 (H<sub>2</sub>O-FH; 20 qubits). In addition, the SCBKT on OpenFermion uses more than 300 GB of memory for the largest system studied (dimers "21" and "31" of (FH)<sub>2</sub>-H<sub>2</sub>O), and the fermion-qubit transformation becomes another bottleneck for simulating larger systems.

In the implementation of the UCCSD quantum circuit, we adopted the first-order Trotter decomposition given in

**TABLE 2** Correlation energies of (FH)<sub>3</sub><sup>a</sup> in units of Hartree.

|                      |           |           |           | UCCSD:CB                               |                  | UCCSD:PW                               |           |           |
|----------------------|-----------|-----------|-----------|----------------------------------------|------------------|----------------------------------------|-----------|-----------|
|                      |           |           |           | —————————————————————————————————————— |                  | —————————————————————————————————————— |           |           |
| Unit                 | MP2       | CCSD      | CCSD(T)   | CMO <sup>b</sup>                       | LMO <sup>c</sup> | СМО                                    | LMO       | CAS-CI    |
| Monomer              |           |           |           |                                        |                  |                                        |           |           |
| "1"                  | -0.017933 | -0.026945 | -0.026945 | -0.026884                              | -0.026854        | -0.026914                              | -0.026729 | -0.026945 |
| "2"                  | -0.017526 | -0.026216 | -0.026216 | -0.026164                              | -0.026169        | -0.026192                              | -0.026019 | -0.026216 |
| "3"                  | -0.017933 | -0.026929 | -0.026929 | -0.026899                              | -0.026839        | -0.026875                              | -0.026691 | -0.026929 |
| Dimer                |           |           |           |                                        |                  |                                        |           |           |
| "21"                 | -0.035493 | -0.051856 | -0.051933 | -0.049880                              | -0.050429        | -0.050452                              | -0.051322 | -0.051963 |
| "31"                 | -0.035980 | -0.052778 | -0.052850 | -0.051554                              | -0.051632        | -0.051527                              | -0.052169 | -0.052879 |
| "32"                 | -0.035446 | -0.053122 | -0.053123 | -0.051952                              | -0.051317        | -0.053067                              | -0.052692 | -0.053124 |
| Sum.                 | -0.053527 | -0.077666 | -0.077816 | -0.073439                              | -0.073516        | -0.075065                              | -0.076744 | -0.077876 |
| w/o FMO <sup>d</sup> | -0.053497 | -0.077566 | -0.077730 |                                        |                  |                                        |           |           |

<sup>&</sup>lt;sup>a</sup>The HF energies (in units of Hartree) of monomer "1", "2", and "3" are -103.815720, -103.995064, -103.563842, respectively. In contrast, the HF energies of dimer "21", "31", "32" are -228.173251, -227.542281, -218.792929, respectively. The sum of Equation (1) is -363.133835 Hartree. Equation (1) is also used for the sum of correlation energies.

Equation (5) in conjunction with the magnitude ordering  $^{70}$  of the cluster operators.

$$\exp(T - T^{\dagger}) = \exp\left(\sum_{k=1}^{K} i t_k P_k\right) \approx \left[\prod_{k=1}^{K} e^{i t_k P_k / M}\right]^{M}$$
 (5)

Here,  $\sum_{k=1}^K it_k P_k$  is the excitation/de-excitation operators in the Pauli operator expressions obtained by adopting the SCBKT to the operator  $(T-T^\dagger)$  in the second-quantized form.  $P_k$  is a direct product of Pauli operators called as a Pauli string, and  $t_k$  is the corresponding coefficient derived from  $t_i^a$  and  $t_{ij}^{ab}$ . K is the number of Pauli strings, and M is the number of Trotter slices. Unless otherwise specified we used the one Trotter slice (M=1) for the VQE-UCCSD simulations.

For the variational optimization of the excitation amplitudes, we examined COBYLA <sup>71</sup> and Powell <sup>72</sup> algorithms; the corresponding labels are shortly denoted as UCCSD:CB and UCCSD:PW, respectively (see Tables 2 and 3). For comparison, the calculation of the complete active space configuration interaction (CAS-CI) was performed to obtain the exact correlation energy in the orbital space of STO-3G. The numerical simulations for (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O were carried out on the Supercomputer 'Flow' Type-II subsystem at Nagoya University and on the in-house NVIDIA DGX H100 system, respectively.

# 3 | RESULTS AND DISCUSSION

# 3.1 | Energies and timings

The correlation energies for  $(FH)_3$  are summarized in Table 2. The MP2, CCSD, and CCSD(T) correlation energies calculated without

applying the FMO scheme are also listed for comparison. The difference between the correlation energies with and without FMO is a maximum of 0.0001 Hartree (0.063 kcal mol<sup>-1</sup>). Compared to MP2, CCSD has a significantly lower energy, and CCSD(T) gives values close to CAS-CI, as expected. UCCSD:PW gave lower energies than UCCSD:CB, but the number of function evaluations (total energy calculations) required in Powell is about 1.6–2.8 times greater than in COBYLA (see Table S1 in Supplementary Materials for details). The same trend was observed for the LMO-based UCCSD calculations. No significant difference was found in the number of function evaluations between CMO and LMO-based calculations.

As we discuss in the next section, Trotterized UCCSD does not automatically satisfy the size-consistency condition, and using LMOs as the basis is crucial to ensure that Trottterized UCCSD is size-consistent. In fact, the correlation energies of the dimers are improved in the LMO-based UCCSD:PW calculations, and the sum of the correlation energies is 0.001679 Hartree (1.0536 kcal mol<sup>-1</sup>) lower in the LMO-based calculations than in the CMO-based one. The deviation of the sum of UCCSD:PW correlation energy from the CAS-CI one is 0.71 kcal mol<sup>-1</sup>.

Table 3 summarizes the results for the (FH)<sub>2</sub>-H<sub>2</sub>O correlation energies. The number of function evaluations in the VQE-UCCSD optimization is given in Table S2 in Supplementary Materials. A checkpoint here is whether the equivalence symmetries (monomers "2" and "3" / dimers "21" and "31") are satisfied, and the usual MP2, CCSD, CCSD(T), and CAS-CI results all satisfy this requirement. The trend of the correlation energies by these methods is the same as in (FH)<sub>3</sub>. On the other hand, the UCCSD results (of both COBYLA and Powell) unfortunately do not satisfy symmetry, as the difference is seen to five decimal places for monomers and three decimal places (in the order of kcal mol<sup>-1</sup>) for dimers. From a chemical precision point of

<sup>&</sup>lt;sup>b</sup>HF canonical orbitals were used for the calculation.

<sup>&</sup>lt;sup>c</sup>Localized molecular orbitals constructed by using Pipek–Mezey method were used for the calculation.

<sup>&</sup>lt;sup>d</sup>The correlation energy of the whole system calculated without FMO scheme.

**TABLE 3** Correlation energies of (FH)<sub>2</sub>-H<sub>2</sub>O<sup>a</sup> in units of Hartree.

|                      |           |           |           | UCCSD:CB  |                  | UCCSD:PW  |           |           |
|----------------------|-----------|-----------|-----------|-----------|------------------|-----------|-----------|-----------|
| Unit                 | MP2       | CCSD      | CCSD(T)   | CMOb      | LMO <sup>c</sup> | СМО       | LMO       | CAS-CI    |
| Monomer              |           |           |           |           |                  |           |           |           |
| "1"                  | -0.035370 | -0.049321 | -0.049394 | -0.049242 | -0.049214        | -0.049231 | -0.048915 | -0.049445 |
| "2"                  | -0.017810 | -0.026705 | -0.026705 | -0.026608 | -0.026648        | -0.026692 | -0.026538 | -0.026705 |
| "3"                  | -0.017810 | -0.026705 | -0.026705 | -0.026677 | -0.026637        | -0.026659 | -0.026476 | -0.026705 |
| Dimer                |           |           |           |           |                  |           |           |           |
| "21"                 | -0.053486 | -0.075392 | -0.075526 | -0.069313 | -0.071305        | -0.071421 | -0.074429 | -0.075600 |
| "31"                 | -0.053486 | -0.075392 | -0.075526 | -0.071847 | -0.069583        | -0.072544 | -0.074367 | -0.075600 |
| "32"                 | -0.035790 | -0.053549 | -0.053553 | -0.053230 | -0.052161        | -0.053207 | -0.052979 | -0.053549 |
| Sum.                 | -0.071770 | -0.101602 | -0.101801 | -0.091863 | -0.090551        | -0.094590 | -0.099846 | -0.101895 |
| w/o FMO <sup>d</sup> | -0.071757 | -0.101649 | -0.101847 |           |                  |           |           |           |

<sup>&</sup>lt;sup>a</sup>The HF energies in units of Hartree of monomer "1", "2", and "3" are -84.426515, -103.695254, and -103.695254, respectively ("2" and "3" are equivalent). In contrast, the HF energies of dimer "21", "31", "32" are -207.357701, -207.357701, and -220.935631, respectively ("21" and "31" are equivalent). The sum of Equation (1) is -343.834010 Hartree. Equation (1) is also used for the sum of correlation energies.

view, it seems problematic that the effect is seen to three decimal places. Furthermore, this issue of broken equivalence should be kept in mind not only for FMO, but for all approaches of fragmentation-oriented methods.<sup>29–31</sup> This problem of VQE-UCCSD is related to the Trotter error and is discussed in the next section.

The effect of orbital localization on the UCCSD correlation energy is remarkable in the  $(FH)_2$ - $H_2O$  system. In the UCCSD:PW calculations the sum of correlation energies improved about 0.005256 Hartree (3.2982 kcal mol $^{-1}$ ) by the orbital localization, and deviation from the CAS-CI correlation energy is 1.29 kcal mol $^{-1}$ . Note that orbital localization also improves the orbital-invariance condition. By using the LMOs, the difference in correlation energy between "21" and "31" is reduced to 0.039 kcal mol $^{-1}$ . These results exemplify the importance of using LMOs in the combination of FMO and VQE-UCCSD approaches.

The cuQuantum quantum simulator was used in this VQE-UCCSD computation. Table 4 summarizes the timings of the UCCSD jobs of (FH)<sub>3</sub> using LMOs on the 'Flow' Type-II subsystem with and without GPU. The GPU acceleration was about a factor of 1.6-2.2 and 6.7-7.7 for monomers and dimers, respectively. In monomer "1", the time for quantum circuit construction is 0.053 s, and the time for quantum circuit simulation is 0.052 and 0.192 s with and without GPU, respectively, for one VQE iteration. In dimer "21", the time for quantum circuit construction is 2.128 s, and the time for a single quantum circuit simulation run is 3.585 (with GPU) and 40.356 (without GPU) s, respectively. The VQE-UCCSD simulations of the dimers "21" and "31" of (FH)<sub>2</sub>-H<sub>2</sub>O (20 qubit systems) without GPU acceleration are too timeconsuming to do. Here we estimated the acceleration ratio by performing the UCCSD simulations of the dimer "21" of (FH)2-H2O by setting the maximum number of function evaluations in the VQE parameter optimization to be 100 on NVIDIA DGX H100. With the

GPU acceleration, the time required for pre-processing (Fermion-qubit transformation, reference CAS-CI calculation, MP2 and MP3 calculations, etc.) was 4773.9 s and 100 function evaluations in the VQE optimization took 1211.0 s. In contrast, the CPU-only calculation took 4421.2 and 37363.9 s for pre-processing and 100 function calls, respectively. The GPU acceleration of the VQE iteration part is about a factor of 30.85. Since the numbers of function evaluations required for convergence in UCCSD:CB and UCCSD:PW were 4913 and 12.452. respectively, the time for the CPU-only simulations are estimated to be about 21 and 54 days for UCCSD:CB and UCCSD:PW, respectively. GPU acceleration is substantial for larger systems, but the speedup is less significant compared with our previous study.<sup>27</sup> This is because the VQE job needs a lot of time for pre-processing and post-processing, and these parts cannot be accelerated by cuQuantum. Considering that a normal FMO-CCSD(T)/STO-3G calculation takes less than 1 s to complete, there is a speed difference of the order of the fourth power of 10 if the correlation part is due to VQE-UCCSD at this time. Note that the present VQE-UCCSD was run on a classical computer, where computational time grows exponentially with the number of qubits. Anyway, as in the previous report,<sup>27</sup> GPU acceleration with cuQuantum is essential for quantum simulations. Such an exponential increase in computation time may not occur if a real quantum computer is used for the VQE-UCCSD calculations. However, there are other kinds of difficulties to overcome in the hardware execution. For example, increase of Hamiltonian terms to evaluate the expectation value, shot noise on the computed energy, difficulty of variational optimization in the presence of various noises, and so on. The combination of various techniques (just such as locality-utilized approaches 32,36-39) to reduce the computational cost in VQE 73-76 may be essential for the hardware execution of VQE-UCCSD.

<sup>&</sup>lt;sup>b</sup>HF canonical orbitals were used for the calculation.

<sup>&</sup>lt;sup>c</sup>Localized molecular orbitals constructed by using Pipek–Mezey method were used for the calculation.

<sup>&</sup>lt;sup>d</sup>The correlation energy of the whole system calculated without FMO scheme.

**TABLE 4** Timings of UCCSD job (in second) of (FH)<sub>3</sub> using LMOs with/without<sup>a</sup> GPU.

|         | UCCSD:CB |             |              | UCCSD:PW | UCCSD:PW    |              |  |
|---------|----------|-------------|--------------|----------|-------------|--------------|--|
| Unit    | With GPU | Without GPU | Acceleration | With GPU | Without GPU | Acceleration |  |
| Monomer |          |             |              |          |             |              |  |
| "1"     | 17.2     | 27.8        | 1.62         | 27.6     | 48.3        | 1.75         |  |
| "2"     | 15.5     | 33.6        | 2.17         | 28.5     | 55.4        | 1.94         |  |
| "3"     | 16.2     | 26.8        | 1.65         | 26.5     | 49.3        | 1.86         |  |
| Dimer   |          |             |              |          |             |              |  |
| "21"    | 12767.5  | 93205.0     | 7.30         | 34153.3  | 260996.7    | 7.64         |  |
| "31"    | 13947.1  | 94199.7     | 6.75         | 34397.3  | 237695.3    | 6.91         |  |
| "32"    | 8805.9   | 59975.6     | 6.81         | 21129.0  | 156257.2    | 7.40         |  |

<sup>&</sup>lt;sup>a</sup>All the calculations were carried out on 'Flow' Type-II subsystem.

#### 3.2 | Relation with Trotter error

It is interesting to note that the monomers "2" and "3" of (FH)2-H2O are symmetrically equivalent, but VQE-UCCSD yields different correlation energies. The HF canonical orbitals of the monomers "2" and "3" are illustrated in Figure 2. We found that the relative phase from the second to the fifth molecular orbitals is different (or inverted) between monomers "2" and "3", which causes changes in the absolute sign of the some excitation amplitudes  $t_i^a$  and  $t_{ii}^{ab}$ . As a result, the quantum states corresponding to the UCCSD wave function are not identical for monomers "2" and "3", and the Trotter error appears in a different way. This fact is confirmed by performing the UCCSD calculations without Trotterization, using the expm multiply function in the SciPy library, 77 which allows us to compute the action of the matrix exponential of  $(T-T^{\dagger})$  on  $|\Psi_{HF}\rangle$ . In this case, the calculated correlation energies of the monomers "2" and "3" are exactly the same: -0.026687 Hartree. The fact that Trotterized UCCSD can not maintain orbital-invariance indicates that care must be taken to ensure that the relative phases of the molecular orbitals match at all points when calculating potential energy surfaces.

Since the Trotter errors appears in an unexpected way, we further investigated about the relationship between Trotter errors and the sizeconsistency, which is an essential condition in the FMO framework as mentioned earlier. Here we focused on the tetrahydrogen (4H) cluster <sup>78</sup> in a square coordinate with R(H-H) = 1.0583 Å (2.0 Bohr) as the monomer, because the Trotter error becomes more significant when the HF is not a good approximation of the ground-state wave function and the UCCSD wave function has large excitation amplitudes. This system is also suitable because the HF CMOs are completely defined by point-group symmetry. In the dimer (8H) calculations, two 4H clusters were placed to form a cuboid, with the inter-monomer distance being 100 Å. Two types of molecular orbitals are examined in the dimer calculations: Completely delocalized canonical orbitals by HF in D<sub>2h</sub> point group and LMOs on the monomers. In the total energy calculations using UCCSD:PW, we used cuQuantum-based quantum circuit simulations with Trotter decomposition and without Trotter decomposition using the expm multiply function in SciPy. The results are summarized in Table 5.

![](_page_5_Picture_9.jpeg)

**FIGURE 2** Active orbitals of FH molecules (monomers "2" and "3") of (FH) $_2$ -H $_2$ O. Red arrows specify the electron occupancy of the HF wave function.

From Table 5, the UCCSD calculations without Trotter decomposition yield almost the same  $\Delta E$  values for both LMO- and CMO-based calculations, and the  $\Delta E$  values of the dimer are twice those of the monomer; that is, Trotter-free UCCSD satisfies the size-consistency condition. Small differences in the  $\Delta E$  values of the dimer with CMO and LMO are due to rounding errors in the AO  $\rightarrow$  MO transformation. In contrast, when the Trotter decomposition is used to construct the UCCSD quantum circuit, the  $\Delta E$  of the dimer with CMO is significantly larger than the  $2 \times \Delta E(\text{Monomer})$ . Since the  $\Delta E$  value for dimer with LMO is approximately twice the  $\Delta E$  of monomer, we concluded that the size-consistency condition of the VQE-UCCSD can be maintained when the molecular orbitals localized on each monomer are used in the calculations.

In the present study, we used the first-order Trotter decomposition given in Equation (5), with the number of Trotter slices M=1. To further investigate the relationship between Trotter error and the size-consistency, we run the UCCSD:PW simulations with M changed from 1 to 5. We also carried out the UCCSD:PW simulations with the second-order Trotter decomposition given in Equation (6).

**TABLE 5** Deviations of the UCCSD:PW total energy from the CAS-CI value for 4H cluster (monomer) and 8H cluster (dimer).

| Unit        | Trotter decomposition | $\Delta \mathbf{E}/\mathrm{kcal}\mathrm{mol}^{-1}$ |
|-------------|-----------------------|----------------------------------------------------|
| Monomer     | No                    | 0.8118                                             |
| Dimer (LMO) | No                    | 1.6236                                             |
| Dimer (CMO) | No                    | 1.6234                                             |
| Monomer     | Yes                   | 0.8102                                             |
| Dimer (LMO) | Yes                   | 1.6207                                             |
| Dimer (CMO) | Yes                   | 5.0319                                             |

$$\exp(T - T^{\dagger}) = \exp\left(\sum_{k=1}^{K} i t_k P_k\right) \approx \left[\prod_{k=1}^{K} e^{i t_k P_k / 2M} \prod_{k=K}^{1} e^{i t_k P_k / 2M}\right]^{M} \tag{6}$$

The results are summarized in Table S3 in the Supplementary Materials. The simulations ended within one hour when GPU is used. The UCCSD:PW energies of monomer (4H cluster) and dimer (8H cluster) with LMO do not change by using a larger number of Trotter slices or by adopting the second-order Trotter decomposition. For the dimer calculations with CMO, in contrast, the deviation from the CAS-CI energy systematically decreases with increasing M. However, even for M=5, the UCCSD:PW energy does not converge to the Trotter-free UCCSD energy calculated by using expm\_multiply in SciPy. This result also implies the importance of using LMO in the FMO scheme in conjunction with the VQE-UCCSD.

Since size-consistency is pivotal not only for FMO but also for general quantum chemical calculations, it is important to provide methods to estimate the Trotter error-free energy. Here we examined the extrapolation method to infer the Trotter error-free UCCSD energy using the idea of algorithmic error mitigation.<sup>79</sup> To do this, we plotted the UCCSD:PW energies as a function of the inverse of the number of Trotter slices, 1/M, and fitted with a function  $E = \alpha (1/M)^{\beta} + \gamma$ . It should be noted that in the context of Hamiltonian simulations, the error of the first-order Trotter decomposition scales as O(1/M).<sup>80</sup> In VQE, however, different Trotterized versions of the UCCSD correspond to different ansatzes, and thus the optimal variational parameters are different. Therefore, it is not necessary to scale the Trotter error of UCCSD as O(1/M). The calculation results are illustrated in Figure 3. The E(UCCSD:PW) were successfully fitted by the function  $E = 0.005396(1/M)^{3.6466} - 3.876244$ , and the difference between the energies estimated from the extrapolation and the Trotter error-free one calculated with expm multiplyis only 35  $\mu$ Hartree. We expect that the extrapolation method used in this work will help to obtain the VQE-UCCSD energy with the size-consistency condition. It is noteworthy that the batch of different slices for extrapolation is a potential target for concurrent processing with multiprocessors.

It should be noted that the dependence of the Trotter error on the locality of the molecular orbitals was investigated by Babbush and coworkers, <sup>81</sup> and they reported that the Trotter error is larger for localized orbital basis than for canonical orbitals and natural orbitals. The reported study focused only on single molecule (monomer), and

![](_page_6_Figure_9.jpeg)

**FIGURE 3** The plot of the UCCSD:PW energies of 8H cluster with different number of Trotter slices *M* and the result of extrapolation.

our discussions are based on comparing the energies of monomers and a dimer. Our results do not contradict this previous study. Trotterization of the UCCSD ansatz can break not only orbital-invariance and size-consistency conditions but also spin symmetry. The wave function obtained by using the Trotterized UCCSD is not always an eigenfunction of the  $S^2$  operator, and is contaminated by other spin states. We calculated the  $\langle S^2 \rangle$  values of the (FH)<sub>3</sub> system and obtained  $\langle S^2 \rangle$  less than  $10^{-6}$ ,  $5 \times 10^{-3}$ , and  $10^{-4}$  for monomers, dimers (CMO), and dimers (LMO), respectively.

# 4 | SUMMARY

We have performed the VQE-UCCSD calculations 17-21 using the cuQuantum simulator 26 in conjunction with the FMO calculations for the (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O systems. The STO-3G minimal basis set <sup>61</sup> was used and the frozen-core restriction <sup>62</sup> was imposed. By combining with symmetry conserving Bravyi-Kitaev transformation, 67 we can simulate the H<sub>2</sub>O-FH dimer with 20 qubits. Both COBYLA and Powell methods were used for VQE optimization, with the latter usually providing better energies but requires more function calls. When the HF CMOs were used for the UCCSD wave function expansion, the calculated correlation energies were somewhat small in magnitude, possibly due to the breakdown of the size-consistency condition. By using the LMOs, the UCCSD correlation energies improved dramatically, and the differences in the correlation energies between the CAS-CI and the UCCSD in conjunction with the Powell optimizer were calculated to be 0.71 and 1.29 kcal mol<sup>-1</sup> for (FH)<sub>3</sub> and (FH)<sub>2</sub>-H<sub>2</sub>O, respectively. The (FH)<sub>2</sub>-H<sub>2</sub>O system has two symmetrically equivalent FH molecules that should have the same energies, but the Trotterized UCCSD does not satisfy symmetry and yields different energies. The difference in correlation energies between the dimers "21" and "31" is on the order of 1 kcal  $mol^{-1}$  in the canonical orbital basis but it reduced to 0.039 kcal mol<sup>-1</sup> in the localized orbital basis.

Size-consistency of the Trotterized UCCSD is also studied numerically using 4H and 8H model clusters. We found that the size-consistency condition can be broken when the molecular orbitals delocalized to the dimer are used for the calculation, and using molecular orbitals localized to the monomers is essential to satisfy the size-consistency. These findings on the relationship between size-consistency and orbital-invariance <sup>44,54</sup> and the error in the Trotter decomposition are very important not only for FMO-based quantum chemical calculations and other fragmentation-oriented methods <sup>29–31</sup> but also for VQE-UCCSD in general. From the numerical simulations, we also demonstrated that the Trotter error-free UCCSD energy can be estimated by means of extrapolation by computing the UCCSD energies with different numbers of Trotter slices.

The GPU acceleration was found to be 7.30 and 7.64 with COBYLA and Powell algorithms, respectively, for the dimer "21" of (FH)<sub>3</sub> (18 qubit system). For the dimer "21" of (FH)<sub>2</sub>-H<sub>2</sub>O, the estimated GPU acceleration ratio of the VQE quantum circuit simulation to be about 30.85, and the VQE simulations of the dimer "21" with COBYLA and Powell will take about 21 and 54 days, respectively. The usefulness of GPUs has attracted much attention in various fields of quantum computation, <sup>82</sup> and quantum chemistry is an example where the acceleration effect is significant, <sup>83</sup> including in this case; even with GPU acceleration, it still takes orders of magnitude longer than a regular FMO-CCSD(T) calculation. <sup>56</sup> Recently, an example of large-scale quantum computation with adamantanes has been reported using VQE. <sup>84</sup> Following these trends, we will perform larger FMO-UCCSD computations on upcoming GPU environments.

#### **ACKNOWLEDGMENTS**

All VQE-UCCSD computations with cuQuantum on the 'Flow' Type-II subsystem at the Information Technology Center of Nagoya University were performed under the JHPCN Joint Research Projects (jh230001 subject by YM). KS and YM would like to thank Yuichiro Minato (CEO of blueqat Inc.), Profs. Takahiro Katagiri (Nagoya University) and Satoshi Ohshima (Kyushu University) for their encouragement regarding quantum simulations with cuQuantum. YM was also supported by Rikkyo SFR. KS acknowledges the support from Quantum Leap Flagship Program (Grant no. JPMXS0120319794) from MEXT, Japan, Center of Innovations for Sustainable Quantum Al (JPMJPF2221) from JST, Japan, and KAKENHI Transformative Research Area B (23H03819) and Scientific Research C (21K03407) from JSPS, Japan.

#### **CONFLICT OF INTEREST STATEMENT**

There are no conflicts to declare.

# **DATA AVAILABILITY STATEMENT**

The data that support the findings of this study are available from the corresponding author upon reasonable request.

#### ORCID

Kenji Sugisaki https://orcid.org/0000-0002-1950-5725

Tatsuya Nakano https://orcid.org/0000-0001-9928-5269

Yuji Mochizuki https://orcid.org/0000-0002-7310-5183

#### **REFERENCES**

- [1] A. Aspuru-Guzik, A. D. Dutoi, P. J. Love, M. Head-Gordon, *Science* 2005, 309, 1704.
- [2] Y. Cao, J. Romero, J. P. Olson, M. Degroote, P. D. Johnson, M. Kieferová, I. D. Kivlichan, T. Menke, B. Peropadre, N. P. D. Sawaya, S. Sim, L. Veis, A. Aspuru-Guzik, *Chem. Rev.* 2019, 119, 10856.
- [3] S. McArdle, S. Endo, A. Aspuru-Guzik, S. C. Benjamin, X. Yuan, Rev. Mod. Phys. 2020, 92, 015003.
- [4] B. Bauer, S. Bravyi, M. Motta, G. K.-L. Chan, Chem. Rev. 2020, 120, 12685.
- [5] M. Motta, J. E. Rice, WIREs Comput. Mol. Sci. 2022, 12, e1580.
- [6] S. Lee, J. Lee, H. Zhai, Y. Tong, A. M. Dalzell, A. Kumar, P. Helms, J. Gray, Z.-H. Cui, W. Liu, M. Kastoryano, R. Babbush, J. Preskill, D. R. Reichman, E. T. Campbell, E. F. Valeev, L. Lin, G. K.-L. Chan, *Nat. Comm.* 2023, 14, 1952.
- [7] M. Reiher, N. Wiebe, K. M. Svore, D. Wecker, M. Troyer, PNAS 2017, 114, 7555.
- [8] Z. Li, J. Li, N. S. Dattani, C. J. Umrigar, G. K.-L. Chan, J. Chem. Phys. 2019, 150, 024302.
- [9] R. Yaris, J. Chem. Phys. 1964, 41, 2419.
- [10] R. Yaris, J. Chem. Phys. 1965, 42, 3019.
- [11] K. Tanaka, H. Terashima, Chem. Phys. Lett. 1984, 106, 558.
- [12] R. J. Bartlett, S. A. Kucharski, J. Noga, Chem. Phys. Lett. 1989, 155, 133.
- [13] W. Kutzelnigg, Theor. Chim. Acta 1991, 80, 349.
- [14] A. G. Taube, R. J. Bartlett, Int. J. Quantum Chem. 2006, 106, 3393.
- [15] B. Cooper, P. J. Knowles, J. Chem. Phys. 2010, 133, 234102.
- [16] G. Harsha, T. Shiozaki, G. E. Scuseria, J. Chem. Phys. 2018, 148, 044107.
- [17] A. Anand, P. Schleich, S. Alperin-Lea, P. W. K. Jensen, S. Sim, M. Díaz-Tinoco, J. S. Kottmann, M. Degroote, A. F. Izmaylov, A. Aspuru-Guzik, Chem. Soc. Rev. 2022, 51, 1659.
- [18] M.-H. Yung, J. Casanova, A. Mezzacapo, J. McClean, L. Lamata, A. Aspuru-Guzik, E. Solano, Sci. Rep. 2014, 4, 3589.
- [19] A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A. Aspuru-Guzik, J. L. O'Brien, Nat. Comm. 2014, 5, 4213.
- [20] J. Romero, R. Babbush, J. R. McClean, C. Hempel, P. J. Love, A. Aspuru-Guzik, Quantum Sci. Technol. 2018, 4, 014008.
- [21] S. Guo, J. Sun, H. Qian, M. Gong, Y. Zhang, F. Chen, Y. Ye, Y. Wu, S. Cao, K. Liu, C. Zha, C. Ying, Q. Zhu, H.-L. Huang, Y. Zhao, S. Li, S. Wang, J. Yu, D. Fan, D. Wu, H. Su, H. Deng, H. Rong, Y. Li, K. Zhang, T.-H. Chung, F. Liang, J. Lin, Y. Xu, L. Sun, C. Guo, N. Li, Y.-H. Huo, C.-Z. Peng, C.-Y. Lu, X. Yuan, X. Zhu, J.-W. Pan, Experimental quantum computational chemistry with optimised unitary coupled cluster ansatz. arXiv:2212.08006v2 2022.
- [22] J. Lee, W. J. Huggins, M. Head-Gordon, K. B. Whaley, J. Chem. Theory Comput. 2019, 15, 311.
- [23] N. H. Stair, R. Huang, F. A. Evangelista, J. Chem. Theory Comput. 2020, 16, 2236.
- [24] G. Greene-Diniz, D. Muñoz Ramo, Int. J. Quantum Chem. 2021, 121, e26352.
- [25] K. Sugisaki, T. Kato, Y. Minato, K. Okuwaki, Y. Mochizuki, Phys. Chem. Chem. Phys. 2022, 24, 8439.
- [26] H. Bayraktar, A. Charara, D. Clark, S. Cohen, T. Costa, Y.-L. L. Fang, Y. Gao, J. Guan, J. Gunnels, A. Haidar, A. Hehn, M. Hohnerbach, M. Jones, T. Lubowe, D. Lyakh, S. Morino, P. Springer, S. Stanwyck, I. Terentyev, S. Varadhan, J. Wong, T. Yamaguchi, cuQuantum SDK: A high-performance library for accelerating quantum science. arXiv: 2308.01999v1 2023.
- [27] K. Sugisaki, V. S. Prasannaa, S. Ohshima, T. Katagiri, Y. Mochizuki, B. K. Sahoo, B. P. Das, *Electron. Struct.* 2023, 5, 035006.
- [28] K. Dalton, C. K. Long, Y. S. Yordanov, C. G. Smith, C. H. W. Barnes, N. Mertig, D. R. M. Arvidsson-Shukur, Npj Quantum Info. 2024, 10, 18.
- [29] M. S. Gordon, D. G. Fedorov, S. R. Pruitt, L. V. Slipchenko, Chem. Rev. 2012, 112, 632.

![](_page_8_Picture_2.jpeg)

- [30] M. A. Collins, R. P. A. Bettens, Chem. Rev. 2015, 115, 5607.
- [31] K. Raghavachari, A. Saha, Chem. Rev. 2015, 115, 5643.
- [32] T. Yamazaki, S. Matsuura, A. Narimani, A. Saidmuradov, A. Zaribafiyan, Towards the practical application of near-term quantum computers in quantum chemistry simulations: A problem decomposition approach. arXiv:1806.01305v1 2018.
- [33] K. Kitaura, E. Ikeo, T. Asada, T. Nakano, M. Uebayasi, Chem. Phys. Lett. 1999, 313, 701.
- [34] T. Akama, M. Kobayashi, H. Nakai, J. Comput. Chem. 2007, 28, 2003.
- [35] G. Knizia, G. K.-L. Chan, Phys. Rev. Lett. 2012, 109, 186404.
- [36] H. Lim, D. H. Kang, J. Kim, A. Pellow-Jarman, S. McFarthing, R. Pellow-Jarman, H.-N. Jeon, B. Oh, J.-K. K. Rhee, K. T. No, Sci. Rep. 2024, 14, 2422.
- [37] M. Otten, M. R. Hermes, R. Pandharkar, Y. Alexeev, S. K. Gray, L. Gagliardi, J. Chem. Theory Comput. 2022, 18, 7205.
- [38] R. D'Cunha, M. Otten, M. R. Hermes, L. Gagliardi, S. K. Gray, J. Chem. Theory Comput. 2024, 20, 3121.
- [39] A. Mitra, R. D'Cunha, Q. Wang, M. R. Hermes, Y. Alexeev, S. K. Gray, M. Otten, L. Gagliardi, The localized active space method with unitary selective coupled cluster. arXiv:2404.12927v1 2024.
- [40] E. Xu, Y. Shimomoto, S. L. Ten-no, T. Tsuchimochi, J. Phys. Chem. A 2024, 128, 2507.
- [41] D. G. Fedorov, K. Kitaura, J. Chem. Phys. 2005, 122, 054108.
- [42] D. Fedorov, K. Kitaura Eds., The Fragment Molecular Orbital Method: Practical Applications to Large Molecular Systems, CRC Press, Florida 2009.
- [43] Y. Mochizuki, S. Tanaka, K. Fukuzawa Eds., Recent Advances of the Fragment Molecular Orbital Method - Enhanced Performance and Applicability, Springer, Berlin 2021.
- [44] A. Szabo, N. S. Ostlund, Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory, Macmillan Publishing, New York 1982.
- [45] D. G. Fedorov, WIREs Comput. Mol. Sci. 2017, 7, e1322.
- [46] D. G. Fedorov, in Recent Advances of the Fragment Molecular Orbital Method: Enhanced Performance and Applicability (Eds: Y. Mochizuki, S. Tanaka, K. Fukuzawa), Springer, Berlin 2021, p. 31.
- [47] T. Ishikawa, T. Ishikura, K. Kuwata, J. Comput. Chem. 2009, 30, 2594.
- [48] T. Ishikawa, in Recent Advances of the Fragment Molecular Orbital Method: Enhanced Performance and Applicability (Eds: Y. Mochizuki, S. Tanaka, K. Fukuzawa), Springer, Berlin 2021, p. 69.
- [49] S. Tanaka, Y. Mochizuki, Y. Komeiji, Y. Okiyama, K. Fukuzawa, Phys. Chem. Chem. Phys. 2014, 16, 10310.
- [50] Y. Mochizuki, T. Nakano, K. Sakakura, Y. Okiyama, H. Watanabe, K. Kato, Y. Akinaga, S. Sato, J. Yamamoto, K. Yamashita, T. Murase, T. Ishikawa, Y. Komeiji, Y. Kato, N. Watanabe, T. Tsukamoto, H. Mori, K. Okuwaki, S. Tanaka, A. Kato, C. Watanabe, K. Fukuzawa, in Recent Advances of the Fragment Molecular Orbital Method: Enhanced Performance and Applicability (Eds: Y. Mochizuki, S. Tanaka, K. Fukuzawa), Springer, Berlin 2021, p. 53.
- [51] Y. Mochizuki, T. Nakano, S. Koikegami, S. Tanimori, Y. Abe, U. Nagashima, K. Kitaura, *Theor. Chem. Acc.* 2004, 112, 442.
- [52] Y. Mochizuki, S. Koikegami, T. Nakano, S. Amari, K. Kitaura, Chem. Phys. Lett. 2004, 396, 473.
- [53] Y. Mochizuki, K. Yamashita, T. Murase, T. Nakano, K. Fukuzawa, K. Takematsu, H. Watanabe, S. Tanaka, Chem. Phys. Lett. 2008, 457, 396.
- [54] I. Shavitt, R. J. Bartlett, Many-Body Methods in Chemistry and Physics: MBPT and Coupled-Cluster Theory, Cambridge University Press, Cambridge 2009.
- [55] Y. Mochizuki, K. Yamashita, K. Fukuzawa, K. Takematsu, H. Watanabe, N. Taguchi, Y. Okiyama, M. Tsuboi, T. Nakano, S. Tanaka, Chem. Phys. Lett. 2010, 493, 346.
- [56] Y. Mochizuki, K. Yamashita, T. Nakano, Y. Okiyama, K. Fukuzawa, N. Taguchi, S. Tanaka, Theor. Chem. Acc. 2011, 130, 515.

- [57] M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone, G. A. Petersson, H. Nakatsuji, X. Li, M. Caricato, A. V. Marenich, J. Bloino, B. G. Janesko, R. Gomperts, B. Mennucci, H. P. Hratchian, J. V. Ortiz, A. F. Izmaylov, J. L. Sonnenberg, D. Williams-Young, F. Ding, F. Lipparini, F. Egidi, J. Goings, B. Peng, A. Petrone, T. Henderson, D. Ranasinghe, V. G. Zakrzewski, J. Gao, N. Rega, G. Zheng, W. Liang, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, K. Throssell, J. A. Montgomery Jr., J. E. Peralta, F. Ogliaro, M. J. Bearpark, J. J. Heyd, E. N. Brothers, K. N. Kudin, V. N. Staroverov, T. A. Keith, R. Kobayashi, J. Normand, K. Raghavachari, A. P. Rendell, J. C. Burant, S. S. Iyengar, J. Tomasi, M. Cossi, J. M. Millam, M. Klene, C. Adamo, R. Cammi, J. W. Ochterski, R. L. Martin, K. Morokuma, O. Farkas, J. B. Foresman, D. J. Fox, Gaussian 16, Revision B.01, Gaussian Inc, Wallingford CT 2016.
- [58] A. D. Becke, J. Chem. Phys. 1993, 98, 1372.
- [59] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, J. Chem. Phys. 2010, 132, 154104
- [60] G. A. Petersson, M. A. Al-Laham, J. Chem. Phys. 1991, 94, 6081.
- [61] W. J. Hehre, R. F. Stewart, J. A. Pople, J. Chem. Phys. 1969, 51, 2657.
- [62] R. P. Hosteny, T. H. Dunning Jr., R. R. Gilman, A. Pipano, I. Shavitt, J. Chem. Phys. 1975, 62, 4764.
- [63] A. J. McCaskey, Z. P. Parks, J. Jakowski, S. V. Moore, T. D. Morris, T. S. Humble, R. C. Pooser, Npj Quantum Info. 2019, 5, 99.
- [64] Y. Mochizuki, K. Okuwaki, T. Kato, Y. Minato, Reduction of orbital space for molecular orbital calculations with quantum computation simulator for educations. ChemRxiv.9863810.v1 2019.
- [65] J. Pipek, P. G. Mezey, J. Chem. Phys. 1989, 90, 4916.
- [66] J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I. Rungger, G. H. Booth, J. Tennyson, Phys. Rep. 2022, 986, 1.
- [67] S. Bravyi, J. M. Gambetta, A. Mezzacapo, K. Temme, Tapering off qubits to simulate fermionic Hamiltonians. arXiv:1701.08213v1 2017
- [68] J. R. McClean, N. C. Rubin, K. J. Sung, I. D. Kivlichan, X. Bonet-Monroig, Y. Cao, C. Dai, E. S. Fried, C. Gidney, B. Gimby, P. Gokhale, T. Häner, T. Hardikar, V. Havlíček, O. Higgott, C. Huang, J. Izaac, Z. Jiang, X. Liu, S. McArdle, J. Romero, N. P. D. Sawaya, B. Senjean, K. Setia, S. Sim, D. S. Steiger, M. Steudtner, Q. Sun, W. Sun, D. Wang, F. Zhang, R. Babbush, *Quantum Sci. Technol.* 2020, 5, 034014.
- [69] Cirq developers, Cirq (v1.2.0). Zenodo. https://doi.org/10.5281/ zenodo.8161252
- [70] A. Tranter, P. J. Love, F. Mintert, P. V. Coveney, J. Chem. Theory Comput. 2018, 14, 5617.
- [71] M. J. D. Powell, in Advances in Optimization and Numerical Analysis (Eds: S. Gomez, J.-P. Hennart), Springer, Dordrecht 1994, p. 51.
- [72] M. J. D. Powell, Comp. J. 1964, 7, 155.
- [73] H. R. Grimsley, S. E. Economou, E. Barnes, N. J. Mayhall, *Nat. Comm.* 2019, 10, 3007.
- [74] Y. Fun, C. Cao, X. Xu, Z. Li, D. Lv, M.-H. Yung, J. Phys. Chem. Lett. 2023, 14, 9596.
- [75] P. Gokhale, O. Angiuli, Y. Ding, K. Gui, T. Tomesh, M. Suchara, M. Martonosi, F. T. Chong, IEEE Trans. Quantum Eng 2020, 1, 1.
- [76] C. Cao, H. Yano, Y. O. Nakagawa, Phys. Rev. Res. 2024, 6, 013205.
- [77] P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, Í. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, SciPy 1.0 Contributors, Nat. Methods 2020, 17, 261.

- [78] J. Paldus, P. Piecuch, L. Pylypow, B. Jeziorski, Phys. Rev. A 1993, 47, 2738.
- [79] S. Endo, Q. Zhao, Y. Li, S. Benjamin, X. Yuan, Phys. Rev. A 2019, 99, 012334.
- [80] M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information, 10th Anniversary ed., Cambridge University Press, Cambridge 2010
- [81] R. Babbush, J. McClean, D. Wecker, A. Aspuru-Guzik, N. Wiebe, Phys. Rev. A 2015, 91, 022311.
- [82] M. Möller, C. Vuik, Ethics Info. Technol. 2017, 19, 253.
- [83] Y. Ino, M. Yonekawa, H. Yuzawa, Y. Minato, K. Sugisaki, Quantum phase estimations of benzene and its derivatives on GPGPU quantum simulators. arXiv:2312.16375v1 2023.

[84] V. K. Prasad, F. Cheng, U. Fekl, H.-A. Jacobsen, *Phys. Chem. Chem. Phys.* **2024**, *26*, 4071.

#### SUPPORTING INFORMATION

Additional supporting information can be found online in the Supporting Information section at the end of this article.

How to cite this article: K. Sugisaki, T. Nakano, Y. Mochizuki, J. Comput. Chem. 2024, 45(26), 2204. <a href="https://doi.org/10.1002/jcc.27438">https://doi.org/10.1002/jcc.27438</a>