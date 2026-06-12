![](_page_0_Picture_1.jpeg)

# ARTICLE OPEN

![](_page_0_Picture_3.jpeg)

# Practical quantum computation of chemical and nuclear energy levels using quantum imaginary time evolution and Lanczos algorithms

Kübra Yeter-Aydeniz notati Raphael C. Pooser and George Siopsis notati

Various methods have been developed for the quantum computation of the ground and excited states of physical and chemical systems, but many of them require either large numbers of ancilla qubits or high-dimensional optimization in the presence of noise. The quantum imaginary-time evolution (QITE) and quantum Lanczos (QLanczos) methods proposed in Motta et al. (2020) eschew the aforementioned issues. In this study, we demonstrate the practical application of these algorithms to challenging quantum computations of relevance for chemistry and nuclear physics, using the deuteron-binding energy and molecular hydrogen binding and excited state energies as examples. With the correct choice of initial and final states, we show that the number of timesteps in QITE and QLanczos can be reduced significantly, which commensurately simplifies the required quantum circuit and improves compatibility with NISQ devices. We have performed these calculations on cloud-accessible IBM Q quantum computers. With the application of readout-error mitigation and Richardson error extrapolation, we have obtained ground and excited state energies that agree well with exact results obtained from diagonalization.

npj Quantum Information (2020)6:63; https://doi.org/10.1038/s41534-020-00290-1

## INTRODUCTION

Noisy intermediate scale quantum (NISQ) computers have recently become workhorse platforms for the study of codesign and the design of near-term quantum algorithms<sup>1</sup>. Thus far, the variational quantum eigensolver has proved to be one of the most useful applications for these devices. Variational methods have been used to solve problems in chemistry, nuclear physics, quantum field theory, high-energy physics, and others<sup>2–8</sup>. While these smallscale applications show promise for using NISQ devices to sample from distributions and calculate expectation values, short coherence times make calculations involving time evolution exceedingly difficult on NISQ devices. Time evolution calculations hold promise for calculating scattering amplitudes<sup>9</sup> and, excited 10,11, and non-equilibrium states 12. One approach to the problem of short coherence times is quantum imaginary time evolution (QITE)<sup>13</sup>, in which non-unitary evolution can be calculated variationally. Combining QITE with the Lanczos optimization method (referred to as QLanczos in the context of quantum computing), one can obtain time-evolved phenomena of various many-body systems'.

Here, we demonstrate the practical application of QITE and QLanczos on current cloud-based NISQ hardware in order to calculate ground and excited states in different fields of study. We use the method to obtain the ground state of the deuteron nucleus in one instance, and we calculate both the ground and excited states of the  $\rm H_2$  molecule in another. The quantum computations were done on several cloud-accessible IBM Q Experience devices, i.e. 20-qubit Johannesburg, 20-qubit Poughkeepsie, 53-qubit Rochester, and 5-qubit Yorktown hardware. The results obtained from the quantum computations were compared with the classical calculations obtained from exact diagonalization. Despite the fact that we used a simplified version of the deuteron

Hamiltonian, we were able to obtain the ground state energy of deuteron without the need for any non-linear optimization or ancillae. We also obtained the energy spectrum of  $\rm H_2$  molecule very close and even within chemical accuracy ( $\rm 1.6\times10^{-3}$  Hartree). These demonstrations show great promise for scaling up time evolution as a solution method on near-term quantum hardware, and they illustrate that the approaches have practical, near-term applicability to an array of fields from high energy physics to chemistry.

Quantum imaginary time evolution addresses the problem of exponentially increasing resource requirements for computation as a function of the number of interacting particles. It replaces the real time in the time-dependent Schrödinger equation with imaginary time ( $t \rightarrow -i\beta$ ). The solution to this equation involves an imaginary-time evolution operator,  $\mathcal{U} = \mathrm{e}^{-\beta H}$ . This operator leads to the decay of all states except for the ground state provided that the initial state has non-zero overlap with the ground state,  $|\Omega\rangle$ , (i.e.,  $\langle \Psi(0)|\Omega\rangle \neq 0$ ). Therefore, the normalized imaginary-time evolution of a state can be expressed as

$$|\Psi(\beta)\rangle = \frac{e^{-\beta H}|\Psi(0)\rangle}{||e^{-\beta H}|\Psi(0)\rangle||}, \tag{1}$$

where  $\beta$  is the imaginary time<sup>14</sup>,  $|\Psi(0)\rangle$  is the initial state, and  $||\cdot|| \equiv \sqrt{\langle\cdot|\cdot\rangle}$  is the state norm.

Quantum computation of the ground state energy of many-body systems using the imaginary-time evolution can be thought of as a natural alternative as quantum computers provide exponential speed ups. The basic idea behind QITE<sup>13</sup> is to approximate the non-unitary imaginary-time evolution in small steps with unitary updates on a set of qubits, including data qubits and ancilla qubits. The non-unitary evolution is provided by variationally changing the parameters of the *Ansatz* circuit, which

<sup>&</sup>lt;sup>1</sup>Physics Division, Oak Ridge National Laboratory, Oak Ridge, TN 37831, USA. <sup>2</sup>Computational Sciences and Engineering Division, Oak Ridge National Laboratory, Oak Ridge, TN 37831, USA. <sup>3</sup>Department of Physics and Astronomy, The University of Tennessee, Knoxville, TN 37996-1200, USA. <sup>™</sup>email: yeteraydenik@ornl.gov; pooserrc@ornl.gov; siopsis@tennessee.edu

![](_page_0_Picture_17.jpeg)

allows us to approximate imaginary time evolution and calculate the decay to the ground state via (1). However, the algorithm of Motta et al. eliminates ancillae as a requirement by using a special type of Ansatz,  $e^{-iA[s]\Delta\tau}$ , considerably simplifying the algorithm. On a quantum computer, the unitary evolution utilizes Trotterization. Current quantum computers are incapable of simulating long time evolution, or a large number of Trotter steps, due to short coherence times and excessive gate noise that further reduces coherence time. However, since QITE seeks to approximate non-unitary evolution with a unitary operator, we can reduce the number of Trotter steps by calculating a specific unitary that corresponds to the largest possible steps in imaginary time that yield a given desired accuracy. This amounts to solving a linear system of equations that provide coefficients of expansion, in terms of Pauli operators, for the unitary evolution operators. In the case of the deuteron, we found that solving this system of equations for the largest timesteps provided a unitary evolution operator that corresponded to the familiar unitary coupled cluster (UCC) Ansatz<sup>15</sup>

While this was a large simplification of the QITE algorithm, a key advantage over variational methods is the ability to use the method in a QLanczos algorithm to calculate excited states. The basic idea behind the QLanczos algorithm is to fill the Krylov space with vectors in powers of  $e^{-2\Delta \tau H}$ , which is done using QITE, and then these vectors are used to calculate Hamiltonian matrix elements, which leads to a generalized eigenvalue equation, yielding a computation of ground and excited states. Using the single-step method in QITE, we reduced the depth of the quantum circuit, which makes these algorithms more compatible with NISQ<sup>16</sup> devices. This method also economizes QITE calculations that might be useful beyond the NISQ regime.

# **RESULTS**

Here, we present the experimental results from IBM Q hardware for QITE and QLanczos algorithms. Information on the experiments and the hardware used can be found in Table 5 of the "Methods" section.

# OITE results

Using the QITE algorithm we were able to calculate the ground state energy of deuteron for both N=2 and N=3 cases. Figure 1 depicts the convergence to the ground state energy for N=2 and N=3 deuteron Hamiltonian.

Data in Figs 1 and 2 were obtained after 10 runs each with 8192 shot on IBM Q Johannesburg hardware. Figure 2 shows the application of the Richardson extrapolation for N=3 case at  $\beta = 0.30$ . In this figure, the expectation value of the ground state energy and the operators are plotted as a function of the number of CNOT gates corresponding to each CNOT gate in the original quantum circuit. As a result of our QITE computation the ground state energy for N=2 (N=3) case is calculated as  $E_2=-1.762\pm$ 0.2 ( $E_3 = -2.033 \pm 0.1$ ) MeV which is off by 0.76% (0.64%) from its value obtained from exact diagonalization, i.e.,  $E_{2,exact} = -1.749$ MeV ( $E_{3,\text{exact}} = -2.046 \text{ MeV}$ ). To produce our energy estimates in Fig. 1a we sampled several collections of qubits on the chip and used results containing the least hardware noise from each set. For example, at points  $\beta = 0.10$ , 0.15, and 0.25 we used the data obtained from qubit layout  $[q_0, q_1] = [0, 5]$ , where  $q_i$  denotes qubit i on quantum hardware. The data obtained from qubit layout  $[q_0]$  $q_1$ ] = [0, 1] had greater standard deviation. Since each data set was obtained with the same number of samples, we attribute the extra noise in layout [0, 1] to quantum hardware errors. The comparison of the data collected for these two-qubit layouts can be found in Table 4 (see "Methods" section). Readout error mitigation (ROEM) suffices for  $\beta = 0$  data points in both N = 2 and N=3 cases, since they do not involve any CNOT gates. To obtain

![](_page_1_Figure_10.jpeg)

![](_page_1_Figure_11.jpeg)

Fig. 1 Energy expectation values of deuteron as a function of imaginary time. a The hardware simulations for N=2 with  $|\Psi_0\rangle=|10\rangle$  were run on IBM Q 20-qubit Johannesburg on qubit layouts  $[q_0,q_1]=[0,1]$  (points  $\beta=0$ , 0.05, 0.20, 0.30) and  $[q_0,q_1]=[0,5]$  (points  $\beta=0.10$ , 0.15, 0.25). b The hardware simulations for N=3 with  $|\Psi_0\rangle=|100\rangle$  were run on IBM Q 20-qubit Johannesburg. The error bars represent  $\pm\sigma$  ( $\sigma=$  standard deviation).

![](_page_1_Figure_13.jpeg)

Fig. 2 Richardson extrapolation of the expectation values of the Pauli operators (on the right axis) and Hamiltonian operator (on the left axis) from their plots as a function of the CNOT gates corresponding to each CNOT gate. The quantum circuit used is in Fig. 5b (see "Methods" section) for N=3 qubit Hamiltonian at  $\beta=0.30$ . This simulation was run on IBM Q 20-qubit Johannesburg hardware using the qubit layout  $[q_0,q_1,q_2]=[8,7,9]$ . The error bars represent  $\pm \sigma$ .

the energy measurements in Fig. 1a, only ROEM was conducted, except for  $\beta = 0.30$ , where both ROEM and extrapolation were used. Each experimental point in Fig. 1b is the result of post-processing with ROEM and Richardson extrapolation.

Although in ref. <sup>1</sup> the QITE algorithm is used for calculating the ground-state energy of a system, we were able to calculate the ground- as well as excited-state energies by changing the initial state. A choice that is orthogonal to the ground state leads to the

![](_page_2_Figure_3.jpeg)

![](_page_2_Figure_4.jpeg)

Fig. 3 Energy expectation values of two-qubit molecular Hydrogen as a function of bond length, *R*. We compared the values from exact diagonalization with the values obtained from hardware. The inset shows the relative errors of the quantum computed energy values compared to chemical accuracy. a The ground state energy (GSE) calculations (with  $|\Psi_0\rangle=|00\rangle$ ) were done on IBM Q 5 Yorktown and the first excited state energy (1st ESE) calculations (with  $|\Psi_0\rangle=|10\rangle$ ) were done on IBM Q Poughkeepsie hardware using the QITE algorithm. ROEM and Richardson extrapolation were applied. b The GSE and third excited-state energy (3rd ESE) calculations (with  $|\Psi_0\rangle=|00\rangle$ ) were done on IBM Q Rochester and the first and second excited-state energy (2nd ESE) calculations (with  $|\Psi_0\rangle=|01\rangle$ ) were done on IBM Q Poughkeepsie hardware using the QLanczos algorithm. The values with and without ROEM are presented. The error bars represent  $\pm \sigma$ .

first-excited state. If, additionally, the initial state is chosen to be orthogonal to the (known) first-excited state, then the algorithm leads to the second excited state, etc.<sup>17,18</sup>. Orthogonality can often be ensured by the symmetry properties of the system Hamiltonian.

In our case, the molecular Hydrogen Hamiltonian (7) is invariant under exchange of the two qubits, owing to the symmetry of the molecule under interchange of the two nuclei (protons). Let X be the swap operator for the two qubits. Since  $X^2=\mathbb{I}$ , its eigenvalues are  $\pm 1$ . The ground state has eigenvalue +1, whereas the first excited state has eigenvalue -1. To produce the ground state using QITE, we used the symmetric initial state  $|\Psi_0\rangle=|00\rangle$ . We obtained the ground state  $|\phi_0\rangle=-0.993|00\rangle+0.115|11\rangle$ . For the first excited state, there is a unique choice that has eigenvalue X=-1, namely the state  $|\phi_1\rangle=\frac{1}{\sqrt{2}}|10\rangle-|01\rangle$ . In our quantum computations, for the first excited state we used the initial state  $|\Psi_0\rangle=|10\rangle$  which is orthogonal to the ground state  $|\phi_0\rangle$ , and confirmed the result from the symmetry argument. Higher-level states were derived using the QLanczos algorithm with input provided by QITE.

In Fig. 3a we plotted the ground- and first-excited-state energies as functions of bond length, *R*, that we obtained by implementing QITE on quantum hardware, and compared with

the values obtained from exact diagonalization. Because of the availability of devices, we used two separate processors for calculation of the ground-state (on IBM Q 5 Yorktown) and first-excited-state (on IBM Q Poughkeepsie) energies. In the case of chemical systems we would like to calculate energy values within chemical accuracy which is  $1.6\times10^{-3}$  Hartree. Here, the terminology "chemical accuracy" refers to the difference between the exact results and our heuristic calculations. Therefore, in the inset of Fig. 3a we show the relative error in energy ( $\Delta E(R)$ ) as a function of bond length compared with chemical accuracy. QITE was able to obtain chemical accuracy for one or two steps depending on the trial state.

As explained above, it is a challenge to access the whole energy spectrum of the system using the QITE algorithm. The calculation of excited-state energies using a variational imaginary-time algorithm was first studied in ref. <sup>19</sup> where all energy levels could be calculated by first targeting the ground state with imaginary time evolution and then successive excited states could be reached by penalizing the ground state and other lower-level states with the use of the shallow swap test. In this work, to access higher-level states, we used the QITE algorithm as a subroutine that provided sufficient input to the QLanczos algorithm to produce the entire spectrum of the system Hamiltonian, as discussed below. Unlike the method in ref. <sup>19</sup>, our QITE/QLanczos implementation does not make use of ancilla qubits and has no need of an additional variational optimization step.

## QLanczos results

QLanczos algorithm can also be used for quantum computation of both the ground- and excited-state energies. The choice of the initial state,  $|\Psi_0\rangle$ , is the one that determines which energies are being calculated. Here, we present our quantum computation of the ground (for deuteron and molecular Hydrogen) and excited-state energies (for molecular Hydrogen only—note that the deuteron does not have a bound excited state) using QLanczos.

Quantum computation of the ground- and excited-state energies using QLanczos might require stabilization of the algorithm as the generalized eigenvalue equation (see Eq. (22) in "Methods" section) might be numerically ill-conditioned. In our particular deuteron problem, due to the linear dependence of the vectors,  $|\Phi_I\rangle$ , in Krylov subspace, we had to perform the stabilization process explained in the Supplementary Information of ref. <sup>1</sup>.

We ran QLanczos on two different devices: IBM Q 20-qubit Poughkeepsie (for N=2 deuteron and first and second excited-state energies of molecular Hydrogen) and IBM Q 53-qubit Rochester (for N=3 deuteron and ground and third excited-state energies molecular Hydrogen). The statistical error is calculated for  $N_{\rm runs}=5$  for deuteron and  $N_{\rm runs}=3$  for molecular Hydrogen, each run having 8192 shots. Results of our quantum computation of the ground state energies for N=2 and N=3 deuteron Hamiltonian are summarized in Table 1.

In Table 1 and Fig. 3b we present the results for QLanczos with and without readout error mitigation (indicated as ROEM) for the deuteron and molecular Hydrogen, repsectively. The results obtained using (24) (given in "Methods" section) are in good agreement with the values obtained from exact diagonalization, while energies obtained from the stabilized generalized eigenvalue equation do not agree well with the exact values due to stability issues in the case of molecular Hydrogen. Choosing a smaller regularization parameter would make these values closer to the exact values with a cost of adding more vectors to the Krylov subspace. In our example, a Krylov subspace with two vectors out of  $\{|\Phi_0\rangle, |\Phi_2\rangle, |\Phi_4\rangle\}$  subspace were sufficient to obtain the ground- and excited-state energies for the deuteron and molecular Hydrogen examples. For molecular Hydrogen, we used two different initial states  $(|\Psi_0\rangle = |00\rangle)$  and  $|\Psi_0\rangle = |10\rangle)$  which

**ROFM** 

 $-2.022 \pm 0.02$ 

![](_page_3_Picture_2.jpeg)

N=2

Raw

 $-1.726 \pm 0.02$ 

**Table 1.** N=2 and N=3 ground state energies (in MeV) calculated using the QLanczos algorithm. E from exact diagonalization N = 2N = 3-1.749 -2.046QLanczos E from eigenvalues of Eq. (22) N = 2Raw **ROEM** Raw **ROFM**  $-1.024 \pm 0.1$  $-1.631 \pm 0.1$  $2.347 \pm 0.4$ -1.402 ± 0.5 QLanczos E from Eq. (24)

We ran the simulations on IBM Q 20-qubit Poughkeepsie (N=2) and 53-qubit Rochester (N=3) hardware. We chose the initial state  $|\Psi_0\rangle=|10\rangle$  ( $|\Psi_0\rangle=|100\rangle$ ) for N=2 (N=3). Please see "Methods" section for (22) and (24).

**ROFM** 

 $-1.728 \pm 0.02$ 

N = 3

Raw

 $-2.025 \pm 0.02$ 

**Table 2.** Lüscher's extrapolation of the deuteron bound state energies (in MeV) to the infinite basis.

|          | N | E <sub>N</sub> | $\mathcal{O}(e^{-2\textit{kl}})$ | $\mathcal{O}(\textit{kLe}^{-4\textit{kl}})$ | $\mathcal{O}(\mathrm{e}^{-4kl})$ |
|----------|---|----------------|----------------------------------|---------------------------------------------|----------------------------------|
| Exact    | 2 | -1.749         | -2.394                           | -2.194                                      |                                  |
|          | 3 | -2.046         | -2.336                           | -2.199                                      | -2.209                           |
| QITE     | 2 | -1.762         | -2.410                           | -2.208                                      |                                  |
|          | 3 | -2.033         | -2.334                           | -2.198                                      | -2.174                           |
| QLanczos | 2 | -1.728         | -2.369                           | -2.171                                      |                                  |
|          | 3 | -2.022         | -2.311                           | -2.175                                      | -2.185                           |

helped us to calculate the energy spectrum as a function of the bond length. *R*.

We found that using (24) gives very close values to exact diagonalization with or without ROEM, meaning that QLanczos is potentially noise resilient. Combined with fast convergence the algorithm has a few advantages that make it useful for quantum computation of the ground and excited-state energies of manybody systems. Since our QLanczos results are in good agreement with the exact values from diagonalization, we did not perform Richardson extrapolation. This would require three more measurements at every QITE step to build the Krylov space.

Although the computational limits of the quantum computers require us to truncate the harmonic oscillator (HO) basis, different schemes were proposed for extrapolating the bound state energies to infinite basis. We will follow the scheme that is based on the Lüscher's formula<sup>20</sup> that was used in ref. <sup>5</sup>. The extrapolation of the bound state energy values to the infinite basis is listed in Table 2. For more information on the extrapolation of the ground state energy to the infinite HO basis please see the "Methods" section.

# **DISCUSSION**

In this study, we presented a practical alternative for calculation of the ground- and excited-state energies of the many-body systems by using *single-step* version of the QITE and QLanczos algorithms presented in ref. <sup>1</sup> using deuteron and molecular Hydrogen as specific examples. This approach may be a good low-depth circuit alternative to other contemporary methods. Depending on the

parameters of the system, the convergence to the ground state or excited states may require too many steps for a small  $\Delta \tau$  value. In this case, one may limit the algorithm to two-step, three-step, etc., processes which will still reduce the circuit depth but provide better imaginary-time evolution. As the system size increases, the required computational resources increase. In this case, the *inexact* QITE proposed in ref. <sup>1</sup> can be used. Although we were able to reduce the circuit depth for less error in hardware by employing a single-step process, the QITE algorithm still requires measurement and calculation of the next unitary operator at every time step.

We also demonstrated how QITE can be used to calculate the excited-state energy whose eigenvector is non-orthogonal to the initial state  $|\Psi_0\rangle$ . We also presented examples of the applications of ROEM and Richardson extrapolation with these algorithms. On the other hand, QLanczos gave results that are good agreement with the exact diagonalization calculations; therefore, it did not require additional error mitigation procedures.

We obtained the bound state energy of the deuteron at the next-to-leading order with a 0.5% (0.9%) error for N=2 (N=3) using QITE and with a 2.2% (1.6%) error for N=2 (N=3) case using QLanczos, compared to its experimental value of -2.22 MeV. We also showed the ground- and excited-state energies of the two-qubit molecular Hydrogen can be calculated within chemical accuracy using the QLanczos algorithm for a few bond lengths.

In future work, we will extend our implementation of the QITE/QLanczos algorithm to study the scattering problem for heavier nuclei and molecules as well as the Ising model.

## **METHODS**

The model

We will apply QITE and QLanczos algorithms into two nontrivial systems, i.e., deuteron and Hydrogen molecule, respectively.

For deuteron system, we follow the refs <sup>5,21</sup>, in which the pion-less effective field theory (EFT) is implemented through a discrete variable representation in the HO basis based on refs <sup>22,23</sup>. Then the pion-less EFT Hamiltonian of the deuteron in the discrete variable representation using the HO basis can be expressed as

$$H_{N} = \sum_{n,n'=0}^{N-1} \langle n' | (T+V) | n \rangle a_{n'}^{\dagger} a_{n} , \qquad (2)$$

where N is the maximum number of oscillator quanta included in the HO basis and  $a_n$  and  $a_n^{\dagger}$  are, respectively, the annihilation and creation operators for n=0,1,...,N-1 and they obey fermionic anti-commutation relations

$$\{a_n, a_{n'}\} = \{a_n^{\dagger}, a_{n'}^{\dagger}\} = 0,$$

$$\{a_n, a_{n'}^{\dagger}\} = a_n a_{n'}^{\dagger} + a_{n'}^{\dagger} a_n = \delta_{n,n'}.$$

$$(3)$$

The kinetic and potential energy terms in this Hamiltonian can be written as

$$\langle n'|T|n\rangle = \frac{\hbar\omega}{2} \left[ (2n+3/2)\delta_n^{n'} - \sqrt{n(n+1/2)}\delta_n^{n'+1} - \sqrt{(n+1)(n+3/2)}\delta_n^{n'-1} \right], \tag{4}$$

$$\langle n'|V|n\rangle = V_0\delta_n^0\delta_n^{n'}.$$

We choose the HO energy spacing as  $\hbar\omega\approx7$  MeV, the potential coefficient as  $V_0\approx-5.686$  MeV and the ultraviolet cutoff for the potential as  $\Lambda\approx152$  MeV .

The simulation of the physical systems on quantum computers is made possible by mapping the creation and annihilation operators onto Pauli matrices. This process is done using the Jordan–Wigner transformation<sup>24</sup> and for N=2 and 3 we obtain

$$H_2 = 5.907I + 0.2183Z_0 - 6.125Z_1 - 2.143(X_0X_1 + Y_0Y_1)$$

$$H_3 = H_2 + 9.625(I - Z_2) - 3.913(X_1X_2 + Y_1Y_2).$$
(5)

with the Pauli matrices defined as

$$\sigma_j = I \otimes \cdots \otimes \sigma \otimes \cdots \otimes I, \tag{6}$$

where  $\sigma \in \{X, Y, Z\}$  is in the *j*th position with  $j = 0, ..., N - 1, \otimes$  indicates tensor product and *l* is the identity matrix.

We will use the two-qubit molecular Hydrogen Hamiltonian<sup>2</sup>

$$H(R) = h_0(R)I + h_1(R)Z_0 + h_2(R)Z_1 + h_3(R)Z_0Z_1 + h_4(R)X_0X_1 + h_5(R)Y_0Y_1.$$
(7)

where coefficients  $h_i(R)$  for  $i \in \{0, 1, ..., 5\}$  are real-valued functions of the bond length, R, of the molecule. We have  $h_1 = h_2$ , so that the Hamiltonian is invariant under interchange of the two qubits (interchange of labels:  $0 \leftrightarrow 1$ ), which is due to the symmetry of the Hydrogen molecule. For calculation of the binding and excited state energies of the Hydrogen molecule we will use the coefficients calculated in STO-3G basis given in Table I of Supplementary Information of ref. <sup>7</sup>.

# Algorithms

Here, we present a brief review of the QITE and QLanczos algorithms that were proposed in ref. <sup>1</sup>.

To be able to simulate the dynamics of many-body systems we need to break down the Hamiltonian of these systems into local components such that  $H = \sum_{m=1}^{M} h_m$  where  $h_m$  are non-commuting local terms of the system<sup>25</sup>. For many-body systems, the number of terms in the Hamiltonian scales polynomially with the number of particles in the system. For example, the N=2 deuteron Hamiltonian in (5) can be decomposed into

$$h_1 = 5.906709I + 0.218291Z_0 - 6.125Z_1,$$
  

$$h_2 = -2.143304(X_0X_1 + Y_0Y_1).$$
(8)

Because of the non-commuting terms in the Hamiltonian the decomposition of the evolution into small time steps and decomposing these steps into local gates can be done using the first order Lie–Trotter–Suzuki decomposition formula<sup>26</sup> which gives

$$\mathcal{U} = \left(\prod_{m=1}^{M} e^{-\Delta \tau h_m}\right)^n + \mathcal{O}(\Delta \tau), \tag{9}$$

where  $n = \frac{\beta}{\Lambda \tau}$  is the number of steps in the evolution.

For two non-commuting operators the matrix exponential can be written as

$$e^{-A\Delta\tau}e^{-B\Delta\tau}=e^{-(A+B)\Delta\tau-\frac{1}{2}[A,B](\Delta\tau)^2+\dots}\ . \tag{10}$$

following the Baker-Campbell-Hausdorff lemma.

This formula is given for two operators only, but it can be generalized to n operators. In our calculations assuming that  $\Delta \tau$  is small we can approximate the imaginary-time evolution up to an order of  $\mathcal{O}(\Delta \tau)$  as follows:

$$|\Psi(\beta)\rangle \approx c_n (e^{-(h_1+h_2+\cdots+h_M)\Delta\tau})^n |\Psi(0)\rangle,$$
 (11)

where

$$c_{n} = \frac{1}{\sqrt{\langle \Psi(0) | (e^{-(h_{1} + h_{2} + \dots + h_{M})\Delta r})^{2n} | \Psi(0) \rangle}}$$
(12)

is the normalization constant.

The sth step of the imaginary-time evolution can be written as

$$|\Psi_{s}\rangle=c_{s}e^{-(h_{1}+h_{2}+\cdots+h_{M})\Delta\tau}|\Psi_{s-1}\rangle, \tag{13}$$

where  $s=1,2,\ldots,n$ . The purpose of the QITE algorithm is to approximate (13) with unitary updates such that

$$|\Psi_{s}\rangle\approx e^{-i\Delta\tau A_{s}}|\Psi_{s-1}\rangle. \tag{14}$$

where  $A_s$  can be written in terms of Pauli operators (defined in (6)) up to D+1 qubits and can be expressed as

$$A_{s} = \sum_{i_{0}i_{1}...i_{D}} a[s]_{i_{0}i_{1}...i_{D}} \sigma_{i_{0}}\sigma_{i_{1}}...\sigma_{i_{D}}.$$
(15)

For our two (three)-qubit systems we used D=1 (D=2). To be able to approximate the imaginary-time evolution with these unitary updates we need to calculate the coefficients a[s]. For small  $\Delta \tau$ , up to an order of  $\mathcal{O}(\Delta \tau)$ , the coefficients are found by solving a linear system of equations  $\mathcal{S}a[s] = \mathbf{b}$  at every step of the imaginary-time evolution, where

$$S_{\mathcal{I},\mathcal{I}'}[s] = \langle \Psi_s | \sigma_{i_0}^{\dagger} \sigma_{i_1}^{\dagger} \dots \sigma_{i_D}^{\dagger} \sigma_{i'_0} \sigma_{i'_1} \dots \sigma_{i'_D} | \Psi_s \rangle, \tag{16}$$

$$b_{\mathcal{I}}[s] = -ic_{s}^{-1/2} \langle \Psi_{s} | \sigma_{i_{0}}^{\dagger} \sigma_{i_{1}}^{\dagger} \dots \sigma_{i_{n}}^{\dagger} h_{m} | \Psi_{s} \rangle \tag{17}$$

with  $\mathcal{I}=i_0,i_1,\ldots,i_D$ . The solution to this equation minimizes the operator norm  $||c_s^{-1/2}|\Psi_s\rangle-(1-i\Delta\tau A_s)|\Psi_{s-1}\rangle||$ . More detailed discussion on the calculation of the coefficients a[m] can be found in the Supplementary Information of ref. <sup>1</sup>.

The calculation of the unitary updates for our deuteron and molecular Hydrogen examples gave us interesting results. For N=2 case the unitary updates have the form of  $A_s=a[s](X_0Y_1-X_1Y_0)$  and N=3 the unitary updates have the form of  $A_s=a_1[s](X_0Y_1-X_1Y_0)+a_2[s](X_0Z_1Y_2-X_2Z_1Y_0)$  which are in the same form as UCC (unitary coupled cluster) Ansätze that were proposed for molecular Hydrogen in ref.  $^2$  and for deuteron in ref.  $^5$ . This means that the unitary updates recover the UCC Ansatz.

Using QITE it is possible to obtain the excited state energies since the system does not necessarily converge to the ground state, but rather depends on the initial state,  $|\Psi_0\rangle$ , choice. In general, the system converges to the eigenvalue of the Hamiltonian whose eigenvector is non-orthogonal to the initial state,  $|\Psi_0\rangle$ .

The QLanczos algorithm is based on the QITE algorithm, but provides the advantage of faster convergence, and it can be used to calculate excited state energies. The basic idea behind the QLanczos algorithm is to fill in the Krylov subspace with vectors in powers of  $\mathrm{e}^{-2\Delta\tau H}$  at each Lanczos iteration such that  $\mathcal{K}:\{|\Phi\rangle,\mathrm{e}^{-2\Delta\tau H}|\Phi\rangle,\mathrm{e}^{-4\Delta\tau H}|\Phi\rangle,\dots\}$ . The vectors in the Krylov subspace are obtained using the QITE algorithm as

$$|\Phi_{l}\rangle = c_{l}e^{-l\Delta\tau H}|\Psi_{t}\rangle \tag{18}$$

for  $0 \leq I < L_{\max}$  assuming I is an even number. Here,  $|\Psi_t\rangle = c_t (\prod_{s=1}^t e^{-i\Delta \tau A_s}) |\Psi_0\rangle = |\Phi_0\rangle$  is the initial QLanczos state which is obtained from QITE subroutine. After building the Krylov subspace we need to calculate the overlap matrix elements  $(\mathcal{T}_{I,I'})$  and Hamiltonian matrix elements  $(\mathcal{H}_{I,I'})$  in terms of the expectation values since they are the only experimentally accessible values. The calculations give overlap and Hamiltonian matrix elements as

$$\mathcal{T}_{l,l'} = \langle \Phi_l | \Phi_{l'} \rangle = \frac{c_l c_{l'}}{c_r^2} \,, \tag{19}$$

$$\mathcal{H}_{l,l'} = \langle \Phi_l | H | \Phi_{l'} \rangle = \mathcal{T}_{l,l'} \langle \Phi_r | H | \Phi_r \rangle , \qquad (20)$$

where  $r = \frac{l+1}{2}$ . The normalization constants can be recursively calculated in terms of expectation values using

$$\frac{1}{c_{r+1}^2} = \frac{\langle \Phi_r | e^{-2\Delta \tau H} | \Phi_r \rangle}{c_r^2} \ . \tag{21}$$

The next step of the QLanczos algorithm is to utilize the calculated overlap and Hamiltonian matrix elements and solve the generalized eigenvalue equation

$$\mathcal{H}x = ETx$$
. (22)

The ground and excited states can then be found from the eigenvectors of the generalized eigenvalue equation. For example, the normalized ground (g) (excited (e)) state approximation is

$$\left| \Phi_{g(e)} \right\rangle = \frac{\sum_{l=0,2,...}^{L_{\text{max}}} x_{lg(e)} |\Phi_{l}\rangle}{\left| \left| \sum_{l=0,2,...}^{L_{\text{max}}} x_{lg(e)} |\Phi_{l}\rangle \right| \right|}, \tag{23}$$

where the coefficients  $x_{I_{g(e)}}$  are obtained from the eigenvector that corresponds to the ground (excited) state energy such that  $(x_{0g(e)}x_{2g(e)}...x_{L_{maxg(e)}})^T$ . Then the energy expectation values are calculated from

$$E_{q(e)} = \langle \Phi_{q(e)} | H | \Phi_{q(e)} \rangle, \tag{24}$$

which then leads to calculation of the ground and excited state energies using QLanczos algorithm. In the exact calculations the energy values obtained from the eigenvalues of the generalized eigenvalue equation (22) match with the values obtained from (24). Our quantum computation shows that using (24) is numerically more stable and gives much better results than using the eigenvalues of (22) as seen in Table 1.

The QLanczos method converges much faster than the QITE algorithm but one needs to do measurements at each imaginary-time projection of the Krylov subspace vectors to obtain the corresponding overlap and Hamiltonian matrix elements from the expectation values. The more vectors in the Krylov subspace the more QITE measurements with an increasing quantum circuit depth are required. At this point, the *single-step* method we proposed that is explained in next section plays an important

![](_page_5_Figure_3.jpeg)

Fig. 4 Two-qubit QITE quantum circuit with initial state  $|\Psi_0\rangle=|10\rangle$ . The quantum circuit in the box is repeated at each QITE step after the second step of the algorithm for convergence.

![](_page_5_Figure_5.jpeg)

Fig. 5 Two- and three-qubit single-step QITE quantum circuit. The initial state is a  $|\Psi_0\rangle=|10\rangle$  and b  $|\Psi_0\rangle=|100\rangle$ , respectively. The angle parameters are calculated for the same circuit until the convergence is reached.

role in terms of reducing the circuit depth and possible noise that will arise due to the gates in the circuit.

# Quantum program

As mentioned earlier, the imaginary-time evolution in QITE algorithm is provided by unitary updates of the form  $\mathcal{U}_s = \mathrm{e}^{-\mathrm{i}\Delta\tau\sigma[s](X_0Y_1-X_1Y_0)}$  for our two-qubit examples. One way to obtain the ground state energy using QITE is to start with an initial product state, say  $|\Psi_0\rangle=|10\rangle$  and apply the unitary updates while calculating the coefficients a[s] that give the state  $|\Psi_s\rangle$  at every step of the imaginary-time evolution. At the end of the nth step of the imaginary-time evolution one expects to reach the ground state energy. This version of QITE would require a quantum circuit as seen in Fig. 4, which only shows the first two steps of the imaginary-time evolution; the depth of the quantum circuit increases as the number of steps increases. At every step of the imaginary-time evolution, the quantum circuit in the shaded area is repeated such that  $\theta_s=2\Delta\tau a[s]$ . Naturally, large depth circuits are very noisy, and not necessarily amenable to error mitigation techniques.

To reduce the circuit depth we reduce the number of time steps. In the single-step version, instead of building the quantum circuit that combines each unitary update which gives  $|\Psi_s\rangle\approx e^{-i\Delta\tau A[s]}|\Psi_{s-1}\rangle$  we build the quantum circuit based on the calculated coefficient A' that gives  $|\Psi_s\rangle\approx e^{-i\Delta\tau sA'}|\Psi_0\rangle$ . In this case, the quantum circuit is given in Fig. 5a which only includes one CNOT gate for a specific initial state of  $|\Psi_0\rangle=|10\rangle$ . The rotation angle is now defined as  $\theta_{s'}=2s\Delta\tau a'[s]$  such that  $\beta'=s\Delta\tau$  is the imaginary-time corresponding to a specific expectation value, and at  $\beta=n\Delta\tau$  the energy converges to the ground (or excited) state energy. We run the same quantum circuit with different calculated a'[s] coefficients until the energy expectation value converges to the ground (or excited) state energy.

Applying the same strategy to our three-qubit deuteron example with an initial state of  $|\Psi_0\rangle=|100\rangle$  gives the unitary updates of the form

$$\mathcal{U}_{s'} \approx e^{-i\Delta \tau s \alpha'_1[s](X_0 Y_1 - X_1 Y_0)} e^{-i\Delta \tau s \alpha'_2[s](X_0 Z_1 Y_2 - X_2 Z_1 Y_0)} . \tag{25}$$

with  $\theta_{s'}=2s\Delta\tau a'[s]$  for  $i=1,\ 2$  which can be approximated with the quantum circuit in Fig. 5b.

In addition to our *single-step* QITE approach we also applied the error mitigation strategies to improve results. In our quantum computations, we applied these error mitigation strategies to obtain the energy expectation values.

# Error mitigation

The noise due to the nature of the quantum simulators requires the application of the error mitigation strategies. Although there are various error mitigation strategies proposed in the literature, for our purposes, we used ROEM and Richardson extrapolation techniques to reduce the noise involved in our calculations.

Out of the different sources of errors in a quantum circuit the readout errors are the errors associated with the final measurements in the quantum circuit. Therefore, we start by mitigating these errors in our

quantum computation. To this end, we use the ROEM scheme proposed in ref. <sup>27</sup>. In that scheme, the expectation values of the operators in the Hamiltonian are calculated using the following formula:

$$\langle \sigma_i \dots \sigma_j \rangle = \sum_{\substack{x \in \text{possible outcomes}}} p(x) \times \frac{(-1)^{x_j} - p_j^-}{1 - p_j^+} \times \dots \times \frac{(-1)^{x_j} - p_j^-}{1 - p_j^+} , \qquad (26)$$

where p(x) is the probability of each qubit outcome and it takes  $2^N$  values. For example, for N = 2,  $x \in \{00, 01, 10, 11\}$ . The symmetric and antisymmetric combinations of the probability of ith qubit flipping from 0 to 1  $(p_i(0|1))$  or from 1 to 0  $(p_i(1|0))$  is defined as

$$p_i^{\pm} = p_i(0|1) \pm p_i(1|0)$$
 (27)

Although  $p_i(0|1)$  and  $p_j(1|0)$  values are provided by IBM's Qiskit library, to get the most up-to-date values we obtained the readout error probabilities by preparing each qubit in computational basis 0 and 1 and then performing a measurement on each qubit in each case which gives us

$$p(1|0) = \frac{\text{\# of states prepared in } |1\rangle \text{ measured in } |0\rangle}{\text{\# of shots}}$$
(28)

or vice versa for p(0|1). We ran the simulations using 8192 number of shots. To propagate the error due to the statistical error in the readout errors for N=2 deuteron case we did the readout error measurements 10 times and propagated the statistical error in measurements and statistical error in readout measurements in our results. As a result of our experimental measurements the statistical error in measurements is not different than the statistical error in readout error measurements therefore, we calculated the statistical error only for our N=3 deuteron and molecular Hydrogen calculations.

Although we were able to reduce the depth of the quantum circuit using the single-step method, the decoherence effects became apparent in the expectation value measurements. Therefore, in addition to the ROEM we also used the Richardson extrapolation  $^{15,28}$  technique for the short-depth quantum circuits $^{29}$  to mitigate the errors associated with the noise produced by the gates used in the quantum circuit. The basic idea in this technique is to increase the error rate deliberately by a constant factor of r which is followed by an extrapolation to obtain the noise free expectation value. In this particular study, we increase the error rate by adding pairs of CNOT gates. The process of adding CNOT pairs is not expected to change the result of measurements since it corresponds to an identity matrix but it will contribute to the noise produced by CNOT gates. Our results showed that for two-qubit systems the expectation values of the observables scale linearly as

$$\langle \mathcal{O}(r) \rangle = Ar + \langle \mathcal{O}(0) \rangle$$
 (29)

and for N=3 deuteron system they scale quadratically as

$$\langle \mathcal{O}(r) \rangle = Ar^2 + Br + \langle \mathcal{O}(0) \rangle,$$
 (30)

where the coefficients A, B, and the extrapolated noiseless expectation value  $\langle \mathcal{O}(0) \rangle$  are found from the linear and quadratic fit to the data points of the expectation values of the operators for each case. We did not apply Richardson extrapolation technique to the QLanczos measurements since the results obtained using the QLanczos algorithm were in good agreement with the exact diagonalization results.

# Extrapolation to the infinite HO basis

The finite-size corrections to the infinite size HO basis based on the Lüscher's method can be stated as

$$E_N - E_\infty = \mathcal{A}e^{-2k_\infty L} + \mathcal{B}k_\infty L e^{-4k_\infty L} + \mathcal{C}e^{-4k_\infty L}, \qquad (31)$$

where

$$\mathcal{A} = \frac{h^2 k_{\infty} y^2}{m}, \quad \mathcal{B} = \frac{2h^2 \gamma^4}{m},$$

$$\mathcal{C} = \frac{h^2 k_{\infty} y^2}{\mu} \left( 1 - \frac{y^2}{k_{\infty}} - \frac{y^4}{4k^2} + 2w_2 k_{\infty} \gamma^4 \right).$$
(32)

The values and definitions of the variables in (31) are given in Table 3. The terms in right-hand side of (31) refer to leading order (LO), next-to-leading order (NLO), and N2LO, respectively. Curve fitting the LO and NLO terms gives the binding momentum,  $k_{\infty}$  and the asymptotic normalization coefficient,  $\gamma$ , for each order by using  $E_1$  and  $E_2$ . Fitting to N2LO term adding  $E_3$  data helps calculating an effective range parameter,  $w_2$ .

| Table 3. The values and definitions of the variables in (31). |                                                |                        |  |  |  |
|---------------------------------------------------------------|------------------------------------------------|------------------------|--|--|--|
| Variable                                                      | Symbol, Equation                               | Value                  |  |  |  |
| Finite-basis energy                                           | E <sub>N</sub>                                 |                        |  |  |  |
| Infinite-basis energy                                         | $E_{\infty}=-\frac{\hbar^2k_{\infty}^2}{2\mu}$ |                        |  |  |  |
| Binding momentum                                              | <i>k</i> ∞                                     |                        |  |  |  |
| Reduced mass                                                  | $\mu=\frac{m_{p}+m_{n}}{4}$                    | 469.45925 MeV $c^{-2}$ |  |  |  |
| Proton mass                                                   | $m_{p}$                                        | 938.272 MeV $c^{-2}$   |  |  |  |
| Neutron mass                                                  | $m_{n}$                                        | 939.565 MeV $c^{-2}$   |  |  |  |
| Effective hard-wall radius                                    | L(N)                                           | L(1) = 9.14  fm        |  |  |  |
|                                                               |                                                | L(2) = 11.45  fm       |  |  |  |
|                                                               |                                                | L(3) = 13.38  fm       |  |  |  |
| Conversion constant                                           | ћс                                             | 197.326 MeV fm         |  |  |  |
| Energy spacing                                                | ħω                                             | 7 MeV                  |  |  |  |

**Table 4.** The exact and ROEM energy expectation values calculated using qubit layouts  $[q_0, q_1] = [0, 1]$  and  $[q_0, q_1] = [0, 5]$  on IBM Q Johannesburg hardware are compared.

|                | Exact (MeV)   | ROEM (MeV)            |                       |  |
|----------------|---------------|-----------------------|-----------------------|--|
|                |               | $[q_0, q_1] = [0, 1]$ | $[q_0, q_1] = [0, 5]$ |  |
| $\beta = 0.10$ | -1.743        | $-1.516 \pm 0.2$      | $-1.679 \pm 0.06$     |  |
| $\beta = 0.15$ | -1.749        | $-1.645 \pm 0.2$      | $-1.643 \pm 0.06$     |  |
| $\beta = 0.25$ | <b>−1.749</b> | $-1.441 \pm 0.4$      | $-1.729 \pm 0.05$     |  |

To plot Fig. 1a we used the values from layout  $[q_0, q_1] = [0, 5]$  at points  $\beta = 0.10, 0.15, 0.25$  as they revealed less deviation and less error out of 10 runs.

| Table 5.         Information about the experimental runs on hardware. |            |           |                            |  |  |
|-----------------------------------------------------------------------|------------|-----------|----------------------------|--|--|
| Figure/Table                                                          | # of shots | # of runs | IBM Q hardware             |  |  |
| Figure 1a                                                             | 8192       | 10        | Johannesburg (v1.1.5)      |  |  |
| Figure 1b                                                             | 8192       | 10        | Johannesburg (v1.1.5)      |  |  |
| Figure 2                                                              | 8192       | 10        | Johannesburg (v1.1.5)      |  |  |
| Table 1 ( <i>N</i> = 2)                                               | 8192       | 5         | Poughkeepsie (v1.2.6)      |  |  |
| Table 1 ( <i>N</i> = 3)                                               | 8912       | 5         | Rochester (v1.1.1)         |  |  |
| Figure 3a                                                             | 8192       | 3         | 5 Yorktown (v2.0.1)        |  |  |
| Figure 3b                                                             | 8192       | 3         | Poughkeepsie and Rochester |  |  |

Information on experimental runs on IBM Q hardware

In Table 4 exact and ROEM energy expectation values are given for the  $\beta=0.10,~0.15,~0.25$  points in Fig. 1a for qubit layouts  $[q_0,~q_1]=[0,~1]$  and  $[q_0,~q_1]=[0,~5]$  on IBM Q Johannesburg hardware.

Table 5 demonstrates the hardware used, the number of runs, and the number of shots in each run to obtain each figure and table in this study.

# **DATA AVAILABILITY**

The data that support the findings of this study are available from the authors upon reasonable request.

# **CODE AVAILABILITY**

The code that is used to produce the data presented in this study is available from the authors upon reasonable request.

Received: 30 December 2019; Accepted: 5 June 2020;

Published online: 17 July 2020

#### REFERENCES

- Motta, M. et al. Determining eigenstates and thermal states on a quantum computer using quantum imaginary time evolution. Nat. Phys. 16, 205–210 (2020).
- O'Malley, P. J. J. et al. Scalable quantum simulation of molecular energies. Phys. Rev. X 6. 031007 (2016).
- Linke, N. M. et al. Experimental comparison of two quantum computing architectures. Proc. Natl Acad. Sci. USA 114, 3305–3310 (2017).
- Kandala, A. et al. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. *Nature* 549, 242–246 (2017).
- Dumitrescu, E. F. et al. Cloud quantum computing of an atomic nucleus. Phys. Rev. Lett. 120, 210501 (2018).
- Klco, N. et al. Quantum-classical computation of Schwinger model dynamics using quantum computers. Phys. Rev. A 98, 032331 (2018).
- Colless, J. I. et al. Computation of molecular spectra on a quantum processor with an error-resilient Algorihm. Phys. Rev. X 8, 011021 (2018).
- 8. McCaskey, A. J. et al. Quantum chemistry as a benchmark for near-term quantum computers. *npj Quant. Inf.* **5**, 98 (2019).
- Jordan, S. P., Lee, K.S. & Preskill, J. Quantum algorithms for fermionic quantum field theories. Preprint at https://arxiv.org/abs/1404.7115 (2014).
- McClean, J. R., Kimchi-Schwartz, M. E., Carter, J. & de Jong, W. A. Hybrid quantumclassical hierarchy for mitigation of decoherence and determination of excited states. *Phys. Rev. A* 95, 042308 (2017).
- Higgott, O., Wang, D. & Brierley, S. Variational quantum computation of excited states. Quantum 3, 156 (2019).
- Lamm, H. & Lawrence, S. Simulation of nonequilibrium dynamics on a quantum computer. *Phys. Rev. Lett.* 121, 170501 (2018).
- McArdle, S. et al. Variational ansatz-based quantum simulation of imaginary time evolution. npj Quant. Inf. 5, 75 (2019).
- Magnus, W. On the exponential solution of differential equations for a linear operator. Commun. Pure Appl. Math. 7, 649–673 (1954).
- Li, Y. & Benjamin, S. C. Efficient variational quantum simulator incorporating active error minimization. *Phys. Rev. X* 7, 021050 (2017).
- Preskill, J. Quantum computing in the NISQ era and beyond. Quantum 2, 79 (2018).
- Ma, F., Zhang, S. & Krakauer, H. Excited state calculations in solids by auxiliaryfield quantum Monte Carlo. New J. Phys. 15, 093017 (2013).
- Drummond, N. D. & Needs, R. J. Diffusion quantum Monte Carlo calculation of the quasiparticle effective mass of the two-dimensional homogeneous electron gas. *Phys. Rev. B* 87, 045131 (2013).
- 19. Jones, T., Endo, S., McArdle, S., Yuan, X. & Benjamin, S. C. Variational quantum algorithms for discovering Hamiltonian spectra. *Phys. Rev. A* **99**, 062304 (2019).
- Furnstahl, R. J., More, S. N. & Papenbrock, T. Systematic expansion for infrared oscillator basis extrapolations. *Phys. Rev. C* 89, 044301 (2014).
- Shehab, O. et al. Toward convergence of effective field theory simulations on digital quantum computers. Phys. Rev. A 100, 062319 (2019).
- Binder, S., Ekström, A., Hagen, G., Papenbrock, T. & Wendt, K. A. Effective field theory in the harmonic oscillator basis. *Phys. Rev. C* 93, 044332 (2016).
- Bansal, A. et al. Pion-less effective field theory for atomic nuclei and lattice nuclei. Phys. Rev. C 98, 054301 (2018).
- Jordan, P. & Wigner, E. P. In Wightman A. S. (ed.) The Collected Works of Eugene Paul Wigner. 109–129 (Springer, 1993).
- Jones, B. D. M., O'Brien, G. O., White, D. R., Campbell, E. T. & Clark J. A. Optimising Trotter-Suzuki decompositions for quantum simulation using evolutionary strategies. GECCO'19: Proceedings of the Genetic and Evolutionary Computation Conference, Association for Computing Machinery, New York, NY, USA (2019).
- Trotter, H. F. On the Product of Semi-Groups of Operators. Vol. 10, 545 (Proceedings of the American Mathematical Society, 1959).
- Yeter-Aydeniz, K. et al. Scalar quantum field theories as a benchmark for nearterm quantum computers. Phys. Rev. A 99, 032306 (2019).
- Kandala, A. et al. (2018). Error mitigation extends the computational reach of a noisy quantum processor. Nature 567, 491–495 (2019).
- Temme, K., Bravyi, S. & Gambetta, J. M. Error mitigation for short-depth quantum circuits. Phys. Rev. Lett. 119, 180509 (2017).
- Eastin, B. & Flammia, S. T. Q-circuit tutorial. Preprint at https://arxiv.org/abs/ quant-ph/0406003 (2004).

# **ACKNOWLEDGEMENTS**

This manuscript has been authored by UT-Battelle, LLC, under Contract No. DE-AC0500OR22725 with the U.S. Department of Energy. We acknowledge useful discussions with C. W. Johnson, T. Morris, and E. Dumitrescu. The quantum circuits were drawn using Q-circuit package<sup>30</sup>. This work was supported by the Quantum

![](_page_7_Picture_2.jpeg)

Information Science Enabled Discovery (QuantiSED) for High Energy Physics program at ORNL under FWP number ERKAP61 and used resources of Oak Ridge Leadership Computing Facility located at ORNL, which is supported by the Office of Science of the Department of Energy under contract No. DE-AC05-00OR22725. The authors acknowledge use of the IBM Q for this work. The views expressed are those of the authors and do not reflect the official policy or position of IBM or the IBM Q team.

## **AUTHOR CONTRIBUTIONS**

K.Y.-A. designed the study, collected data, and produced figures. R.C.P. and G.S. supervised the research. All authors discussed the results and contributed to the final paper.

## **COMPETING INTERESTS**

The authors declare no competing interests.

## **ADDITIONAL INFORMATION**

**Correspondence** and requests for materials should be addressed to K.Y.-A.,R. C.P.or G.S.

Reprints and permission information is available at http://www.nature.com/reprints

**Publisher's note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly

article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit <a href="http://creativecommons.org/licenses/by/4.0/">http://creativecommons.org/licenses/by/4.0/</a>.

© The Author(s) 2020