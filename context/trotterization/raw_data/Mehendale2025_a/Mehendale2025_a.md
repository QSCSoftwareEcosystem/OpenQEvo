# Estimating Trotter Approximation Errors to Optimize Hamiltonian Partitioning for Lower Eigenvalue Errors

Shashank G. Mehendale\*, 1,2 Luis A. Martínez-Martínez\*, 1,2

Prathami Divakar Kamath\*, 3 and Artur F. Izmaylov 1,2

1 Chemical Physics Theory Group, Department of Chemistry,

University of Toronto, Toronto, Ontario M5S 3H6, Canada

2 Department of Physical and Environmental Sciences,

University of Toronto Scarborough, Toronto, Ontario M1C 1A4, Canada

3 Department of Metallurgical Engineering and Materials Science,

Indian Institute of Technology Bombay, Maharashtra, 400076, India

## Abstract

Trotter approximation in conjunction with Quantum Phase Estimation can be used to extract eigen-energies of a many-body Hamiltonian on a quantum computer. There were several ways proposed to assess the quality of this approximation based on estimating the norm of the difference between the exact and approximate evolution operators. Here, we explore how different error estimators correlate with the true error in the ground state energy due to Trotter approximation. For a set of small molecules we calculate these exact error in ground-state electronic energies due to the second-order Trotter approximation. Comparison of these errors with previously used upper bounds show correlation less than 0.4 across various Hamiltonian partitionings. On the other hand, building the Trotter approximation error estimation based on perturbation theory up to a second order in the time-step for eigenvalues provides estimates with very good correlations with the exact Trotter approximation errors. These findings highlight the non-faithful character of norm-based estimations for prediction of a Trotter-based eigenvalue estimation performance and the need of alternative estimators. The developed perturbative estimates can be used for practical time-step and Hamiltonian partitioning selection protocols, which are needed for an accurate assessment of quantum resources.

<sup>\*</sup> These authors contributed equally to this work

## I. INTRODUCTION

Solving the electronic structure problem is one of the anticipated uses of quantum computing. As an eigenvalue problem with a Hamiltonian operator that can be expressed compactly, this problem is convenient for quantum computing because classical-quantum data transfer is usually a bottleneck.[1] Obtaining electronic wavefunctions and energies is one of the key procedures in first principles modeling of molecular physics since molecular energy scale is dominated by the electronic part. Yet, solving this problem scales exponentially with the size unless some approximations are made.

Fault-tolerant quantum computers offer potential advantages for efficient estimation of energy eigenvalues through exponential speedup with respect to classical methods, by means of the Quantum Phase Estimation (QPE) algorithm [2]. The QPE framework contains three main parts: 1) initial state preparation, 2) procedure for an evolution or a walker operator that involves the Hamiltonian encoding, and 3) the eigenvalue extraction. Here, we focus on the second part, two main approaches for the Hamiltonian encoding are representing the Hamiltonian exponential function via the Trotter approximation and embedding the Hamiltonian as a block of a larger unitary via decomposing the Hamiltonian as a Linear Combination of Unitaries (LCU).

Within the Trotter approximation, the target Hamiltonian is decomposed into easy-to-simulate (or fast-forwardable) Hamiltonian fragments:

$$\hat{H} = \sum_{m=1}^{M} \hat{H}_m \tag{1}$$

and the exact unitary evolution operator for an arbitrary simulation time  $\tau$  is approximated using the time evolution of the fragments  $\hat{H}_m$ . The second-order Trotter approximation is given by

$$\hat{U}(\tau) = e^{-i\tau\hat{H}} \approx \left(\prod_{m=1}^{M} e^{-i\hat{H}_{m}\tau/(2n)} \prod_{m=M}^{1} e^{-i\hat{H}_{m}\tau/(2n)}\right)^{n} = \left(\hat{U}_{T}^{(2)}(\tau/n)\right)^{n}$$
(2)

where the approximation is exact up to second order in  $\tau$ . This approximate representation of the exact time evolution operator introduces a deviation in the spectrum of the simulated time evolution unitary with respect to the exact one. For estimation of energy eigenvalues through QPE under a fixed target error, it is therefore crucial to rationalize the scaling of

this deviation with the time scale used for discretization of the total simulation time as well as its dependence with different Hamiltonian partitioning schemes.

In spite of less favorable time scaling of the Trotter approach compared to the LCU based techniques, it has benefits of a lower ancilla qubit overhead and possibility for using commutation relation between terms of the Hamiltonian for formulating fast-forwardable fragments. Yet, one difficulty for practical use of the Trotter approximation is estimation of its error. This estimation is needed for choosing the evolution time-step and the overall error estimation. Another use of the Trotter approximation error is choosing the Hamiltonian partitioning that minimizes error and thus the number of steps required.

Recently, upper bounds were formulated for the norm of the difference between propagators,

$$||\hat{U}(\tau) - \hat{U}_{T}^{(2)}(\tau/n)^{n}|| \leq \frac{\alpha \tau^{3}}{n^{2}},$$

$$\alpha = \frac{1}{12} \sum_{m_{1}=1}^{M} \left\| \left[ \sum_{m_{3}=m_{1}+1}^{M} H_{m_{3}}, \left[ \sum_{m_{2}=m_{1}+1}^{M} H_{m_{2}}, H_{m_{1}} \right] \right] \right\|$$

$$+ \frac{1}{24} \sum_{m_{1}=1}^{M} \left\| \left[ H_{m_{1}}, \left[ H_{m_{1}}, \sum_{m_{2}=m_{1}+1}^{M} H_{m_{2}} \right] \right] \right\|.$$

$$(4)$$

which allowed one to estimate the effect of the Trotter approximation on the accuracy of dynamics [3]. These estimates can be used to derive upper bounds for the energy error in QPE [4]. In what follows, for brevity, we will refer to the time step as  $t = \tau/n$ . However, it is known in general that the Trotter upper bounds are relatively loose and using them could lead to underestimation of appropriate time-step [5]. Considering that with some simplifications  $\alpha$  values can be evaluated and used to differentiate various Hamiltonian partitionings [6], it is interesting to examine how accurate  $\alpha$ -based trends are compared to those using the exact Trotter approximation error in eigenvalues.

Here, we investigate using the exact error calculation for small systems whether the Trotter approximation error upper bounds can be used to differentiate Hamiltonian partitionings. We also explore alternative estimates of the Trotter approximation error for eigenvalues based on time-independent perturbation theory. Such theory can be built by representing the Trotter propagator as

$$\hat{U}_T^{(2)}(t) = e^{-it\hat{H}_{\text{eff}}(t)} \tag{5}$$

and performing perturbative analysis of the  $\hat{H}_{\rm eff}(t)$  spectrum. Even though perturbative estimates are not upper bounds, they can be used for differentiating between various Hamiltonian partitioning schemes. As for predicting the Trotter step, one can use perturbative estimates as a first step in the iterative procedure suggested recently.[7]

# II. PERTURBATIVE ERROR ESTIMATES

Time-independent perturbation theory is built by considering Baker-Campbell–Hausdorff expansion of the second order Trotter evolution operator in Eq. (5)

$$\hat{H}_{\text{eff}}(t) = \hat{H} + \sum_{k} \hat{V}_{k} t^{k}. \tag{6}$$

By construction [see Eq. (2)],  $\hat{U}_{T}^{(2)}(t)\hat{U}_{T}^{(2)}(-t) = 1$ , implying  $\hat{H}_{\text{eff}}(t) = \hat{H}_{\text{eff}}(-t)$ . Therefore, only even order  $\hat{V}_{k}$ 's survive in Eq. (6). The leading term is then given by [see Appendix A 5]

$$\hat{V}_2 = -\frac{1}{24} \sum_{v'=v}^{2M} \sum_{v=\mu+1}^{2M} \sum_{\mu=1}^{2M-1} \left(1 - \frac{\delta_{v',v}}{2}\right) [\hat{H}_{v'}, [\hat{H}_v, \hat{H}_{\mu}]], \tag{7}$$

where  $H_{M+i} = H_{M+1-i}$  for i = 1 to M. Note that in spite of t dependence of  $\hat{H}_{\text{eff}}$ , we do not need time-dependent perturbation theory since we are interested in eigenvalues of  $\hat{H}_{\text{eff}}$  as a function of t. Eigenvalues of  $\hat{H}_{\text{eff}}$  can be obtained as perturbative series starting from those of  $\hat{H}$ . Focusing on the ground state energy  $E_0$ , the correction from first-order perturbation theory can be written as

$$E_{\rm GS}^{(1)} = \langle \phi_0 | \hat{V}_2 | \phi_0 \rangle t^2,$$

where  $|\phi_0\rangle$  is the electronic ground state. Note that next correction to energy will be fourth order in time. This implies, the ground state energy of  $H_{\text{eff}}$  is  $E_0^{(T)} = E_0 + \varepsilon_2 t^2 + \mathcal{O}(t^4)$ , where

$$\varepsilon_2 = \langle \phi_0 | \hat{V}_2 | \phi_0 \rangle. \tag{8}$$

Calculating  $\varepsilon_2$  requires knowledge of the ground state of  $\hat{H}$ . Since it is not accessible for a general Hamiltonian, we approximate  $\varepsilon_2$  using approximate eigenstate  $|\psi_0\rangle$  obtained via cost efficient classical methods. We can then define an approximation to  $\varepsilon_2$  given by

$$\varepsilon_{\text{app}} = \langle \psi_0 | \hat{V}_2 | \psi_0 \rangle . iv \tag{9}$$

The difference  $|\varepsilon_2 - \varepsilon_{app}|$  is expected to become smaller with larger overlap  $|\langle \phi_0 | \psi_0 \rangle|$ .

#### III. RESULTS AND DISCUSSION

Here, we assess correlations between the exact Trotter approximation errors and estimates based on  $\alpha$  [Eq. (4)] and perturbative expression  $\varepsilon_{\rm app}$  [Eqs. (9)]. The Trotter approximation errors are obtained for electronic Hamiltonians of small molecules (H<sub>2</sub>, LiH, BeH<sub>2</sub>, H<sub>2</sub>O, and NH<sub>3</sub>) and various Hamiltonian partitioning schemes described in Appendix A. The approximate ground state  $|\psi_0\rangle$  is obtained from CISD calculations. For H<sub>2</sub>, LiH, and BeH<sub>2</sub>, the bond length is chosen to be 1 . For H<sub>2</sub>O and NH<sub>3</sub>, the bond length is chosen to be 1.9 . The overlap  $|\langle \phi_0 | \psi_0 \rangle|^2$  equals 93% for H<sub>2</sub>O and 83% for NH<sub>3</sub>. The exact Trotter approximation errors  $|\Delta E_T| = |E_0^{(T)} - E_0|$  are computed by numerical diagonalization of  $\hat{H}$  and  $\hat{H}_{\rm eff}$  [Eq. (5)] as described in Appendix A 4.

## A. Exact Trotter approximation errors

We define  $\varepsilon = \Delta E_T/t^2$  to represent the exact Trotter approximation error and examine the correlations between  $\varepsilon$  and the error estimators. Comparing true errors with predictions based on  $\alpha$  upper bound in Fig. 1 (a) (red marker) shows poor correlation. Thus, it is not possible to determine the Hamiltonian partitioning performance in terms of the Trotter approximation error based on  $\alpha$  values. Upper bounds based on  $\alpha$ 's are usually very loose, so we have considered an  $\alpha$ -like estimator

$$\alpha_e = ||\hat{U}(t) - \hat{U}_T^{(2)}(t)||/t^3. \tag{10}$$

 $\alpha_e$  captures the exact error in the time propagator introduced by the Trotter approximation. However, the correlation plot of Fig. 1 (a) (blue marker) shows that  $\alpha_e$  is also poorly correlated with  $\varepsilon$ . This discrepancy can be understood as a consequence of  $\alpha$  and  $\alpha_e$  being worst-case scenario metrics for the deviation (with respect to exact unitary propagation) that ensue from the Trotter approximation rather than a measure of deviation with respect to the eigenspectrum of the target simulated Hamiltonian.

![](_page_5_Figure_0.jpeg)

FIG. 1: Correlation between exact Trotter error and the error estimators. Each point on the plot corresponds to a unique pair of molecule and fragmentation technique. The straight lines are plotted using the Pearson correlation coefficient, given in the legend. All axes are normalized to one. (a)  $\varepsilon$  vs  $\alpha$  correlation is denoted in red, while  $\varepsilon$  vs  $\alpha_e$  is denoted in blue. (b)  $\varepsilon$  vs  $\varepsilon_2$  correlation is denoted in red, while  $\varepsilon$  vs  $\varepsilon_{app}$  in blue. The corresponding numerical data is presented in appendix A 6.

On the other hand, since  $|\Delta E_T| = \varepsilon_2 t^2 + \mathcal{O}(t^4)$ , for small enough t,  $\varepsilon_2$  should exactly capture  $\varepsilon$ . We can observe this in Fig. 1 (b), where we plot the correlation between  $\varepsilon$  and  $\varepsilon_2$  in red. The correlation coefficient, as expected, is one. In the same subplot, we also show the correlation between  $\varepsilon$  and  $\varepsilon_{app}$ . We can see a strong correlation between the two quantities, with a correlation coefficient of 0.99. This suggests that despite having approximate wavefunctions with a fidelity as low as 0.83, one can still predict the best and worst partitioning techniques.

#### B. Resource efficiency

Table I summarizes upper bound estimations of the T-gate count required for QPE under a target accuracy based on the exact scaling of Trotter approximation errors  $\varepsilon$ , alongside cruder estimations based on the  $\alpha$  upper bounds. Even though upper bound estimations on T-gate count based on the  $\alpha$  mostly predict best performance of qubit decompositions, they tend to consistently overrate the FC SI and QWC SI methods.  $\alpha$  based T gate count overestimates T gates by more than an order of magnitude for H<sub>2</sub>O and NH<sub>3</sub>. The overes-

|                  |                              | $\varepsilon$ -based         |                                | $\alpha$ -based              |                                |                                |  |  |
|------------------|------------------------------|------------------------------|--------------------------------|------------------------------|--------------------------------|--------------------------------|--|--|
| Molecule         | $1^{\text{st}}$ best $(N_T)$ | $2^{\text{nd}}$ best $(N_T)$ | $3^{\mathrm{nd}}$ best $(N_T)$ | $1^{\rm st}$ best $(N_T)$    | $2^{\mathrm{nd}}$ best $(N_T)$ | $3^{\mathrm{nd}}$ best $(N_T)$ |  |  |
| $H_2$            | QWC LF $(6.2 \times 10^6)$   | QWC SI $(6.2 \times 10^6)$   | FC LF $(6.2 \times 10^6)$      | QWC SI $(1.4 \times 10^7)$   | FC SI $(1.4 \times 10^7)$      | QWC LF $(1.5 \times 10^7)$     |  |  |
| LiH              | QWC SI $(2.5 \times 10^8)$   | FC SI $(2.7 \times 10^8)$    | FC LF $(3.0 \times 10^8)$      | FC SI $(2.9 \times 10^9)$    | QWC SI $(2.9 \times 10^9)$     | FC LF $(4.7 \times 10^9)$      |  |  |
| $\mathrm{BeH}_2$ | FC SI $(5.5 \times 10^8)$    | QWC SI $(6.2 \times 10^8)$   | QWC LF $(7.0 \times 10^8)$     | FC SI $(6.3 \times 10^9)$    | QWC SI $(6.4 \times 10^9)$     | QWC LF $(1.3 \times 10^{10})$  |  |  |
| $_{\rm H_2O}$    | FC SI $(5.1 \times 10^8)$    | QWC SI $(6.7\times10^8)$     | QWC LF $(7.7 \times 10^8)$     | FC SI $(5.9 \times 10^{10})$ | QWC SI $(6.0 \times 10^{10})$  | QWC LF $(1.0 \times 10^{11})$  |  |  |
| $\mathrm{NH}_3$  | QWC SI $(9.8 \times 10^8)$   | QWC LF $(1.0 \times 10^9)$   | FC SI $(1.2 \times 10^9)$      | FC SI $(4.4 \times 10^{10})$ | QWC SI $(4.5 \times 10^{10})$  | QWC LF $(8.1 \times 10^{10})$  |  |  |

TABLE I: Best resource-efficient Hamiltonian decomposition methods for eigenvalue estimation within chemical accuracy with a Trotterized QPE algorithm. T-gate count  $N_T$  is given in parenthesis.

|                  |                            | $\varepsilon_{\mathrm{app}}$ -based |                                |  |  |  |  |  |  |  |  |
|------------------|----------------------------|-------------------------------------|--------------------------------|--|--|--|--|--|--|--|--|
| Molecule         | $1^{\rm st}$ best $(N_T)$  | $2^{\mathrm{nd}}$ best $(N_T)$      | $3^{\mathrm{nd}}$ best $(N_T)$ |  |  |  |  |  |  |  |  |
| $H_2$            | QWC LF $(6.2 \times 10^6)$ | QWC SI $(6.2 \times 10^6)$          | FC LF $(6.2 \times 10^6)$      |  |  |  |  |  |  |  |  |
| LiH              | QWC SI $(2.5 \times 10^8)$ | FC SI $(2.7 \times 10^8)$           | FC LF $(3.0 \times 10^8)$      |  |  |  |  |  |  |  |  |
| $\mathrm{BeH}_2$ | FC SI $(5.6 \times 10^8)$  | QWC SI $(6.2 \times 10^8)$          | QWC LF $(7.0 \times 10^8)$     |  |  |  |  |  |  |  |  |
| H <sub>2</sub> O | FC SI $(7.6 \times 10^8)$  | QWC SI $(8.8 \times 10^8)$          | QWC LF $(9.7 \times 10^8)$     |  |  |  |  |  |  |  |  |
| $NH_3$           | FC SI $(1.0 \times 10^9)$  | QWC LF $(1.1 \times 10^9)$          | QWC SI $(1.2 \times 10^9)$     |  |  |  |  |  |  |  |  |

TABLE II: Best resource-efficient Hamiltonian decomposition methods for eigenvalue estimation within chemical accuracy with a Trotterized QPE algorithm. T-gate count  $N_T$  is given in parenthesis.

timation is expected to grow as the sizes of molecules or the basis sets increase, since this leads to larger norm of the Hamiltonian and its fragments, and hence the error operators in Eq. (4). Thus, using  $\alpha$ 's leads to drastic overestimations of resources needed to obtain energies using the Trotter approximation and QPE.

For  $\varepsilon$  analysis based on perturbation theory expressions we cannot establish the same trends as those found for  $\alpha$ 's in Ref. [6]. Finally, in Table II we explore the faithfulness of  $\varepsilon_{\rm app}$  in the discrimination of the best resource-efficient methods, from which we note that  $\varepsilon_{\rm app}$ -based estimator accurately captures the right order of magnitude of the T-gate numbers as obtained by the  $\varepsilon$ . Also, the  $\varepsilon_{\rm app}$ -based estimator correctly suggests qubit partition methods as the most accurate compared to their fermionic counterparts. Due to similarity of

T-gate numbers for various qubit partitionings, the ranking based on  $\varepsilon_{app}$  and  $\varepsilon$  are different, in spite of the high degree of  $\varepsilon_{app} - \varepsilon$  correlation (Fig.1). Since all the best Hamiltonian partitioning methods have very similar resource estimations and their particular order is of little importance,  $\varepsilon_{app}$  can be a good substitute for  $\varepsilon$ . Thus, estimators of Trotter error based on perturbative expression [Eq. (8)] and a classically-accessible approximation to the electronic ground state, provide better correlation than commutator-norm-based counterparts, even for the strongly correlated molecular configurations.

## IV. CONCLUSIONS

We have calculated exact errors associated with the second order Trotter approximation for small molecules and different Hamiltonian partitionings. Previously derived commutator norm based upper bound,  $\alpha$ , was shown to have low correlation with the induced exact error in energy due to Trotter approximation. This confirmed the loose character of the  $\alpha$  based upper bounds for energies, which makes these upper bounds inadequate in determining the true resources needed to achieve target accuracy in energy. The alternative estimate of the Trotter approximation error,  $\varepsilon_{\rm app}$ , based on perturbative analysis of the effective Hamiltonian eigen-spectrum performed much better. The T gate upper bound estimates based on  $\alpha$  were orders of magnitude higher than those predicted by the exact Trotter error. However, estimates based on  $\varepsilon_{\rm app}$  produced correct order of T gate estimates.

Substituting the exact ground eigenstate with a classically easy to obtain counterpart in calculating perturbation corrections gave accurate approximations, even in the case of strongly correlated molecular configurations. Specifically, the method produced accurate results in the case of H<sub>2</sub>O and NH<sub>3</sub>, where the CISD ground states have overlaps 93% and 83% with respect to the exact ground state, respectively. For electronic systems with a higher degree of multiconfigurational character, one can find approximations to the global ground state using more sophisticated polynomial-in-time scaling methods, and hence make use of the tools developed here. These estimations of the Trotter approximation error raise two questions for future research: 1) how to optimize efficiently the Hamiltonian partitioning and ordering of its fragments based on the obtained error estimates; and 2) how to obtain upper bounds instead of approximations for the error estimates based on the eigen-spectrum

analysis of  $H_{\text{eff}}$ . Answering the second question will allow one to set an optimal Trotter time step for resource efficient simulation under a target energy eigenvalue estimation accuracy.

## DATA AVAILABILITY

The code to generate the Hamiltonian fragments and calculate the exact and approximate Trotter errors can be found at https://github.com/Shashank-G-M/Perturbative\_Trotter\_Error. The same has been archived on Zenodo with DOI: https://zenodo.org/records/15327942.

#### ACKNOWLEDGMENTS

The authors would like to thank Nathan Wiebe for useful discussions. L.A.M.M. is grateful to the Center for Quantum Information and Quantum Control (CQIQC) for a postdoctoral fellowship. P.D.K. is grateful to Mitacs for the Globalink research award. A.F.I. acknowledges financial support from the Natural Sciences and Engineering Council of Canada (NSERC). This research was partly enabled by the support of Compute Ontario (computeontario.ca) and the Digital Research Alliance of Canada (alliancecan.ca). Part of the computations were performed on the Niagara supercomputer at the SciNet HPC Consortium. SciNet is funded by Innovation, Science, and Economic Development Canada, the Digital Research Alliance of Canada, the Ontario Research Fund: Research Excellence, and the University of Toronto.

<sup>[1]</sup> Torsten Hoefler, Thomas Haener, and Matthias Troyer. "Disentangling hype from practicality:
On realistically achieving quantum advantage" (2023). arXiv:2307.00523.

<sup>[2]</sup> Lindsay Bassman Oftelie, Miroslav Urbanek, Mekena Metcalf, Jonathan Carter, Alexander F. Kemper, and Wibe A. de Jong. "Simulating quantum materials with digital quantum computers". Quantum Sci. Technol. 6, 043002 (2021).

<sup>[3]</sup> Andrew M. Childs, Yuan Su, Minh C. Tran, Nathan Wiebe, and Shuchen Zhu. "Theory of trotter error with commutator scaling". Phys. Rev. X 11, 011020 (2021).

- [4] Markus Reiher, Nathan Wiebe, Krysta M. Svore, Dave Wecker, and Matthias Troyer. "Elucidating reaction mechanisms on quantum computers". Proc. Natl. Acad. Sci. U.S.A. 114, 7555–7560 (2017).
- [5] David Poulin, Matthew B. Hastings, Dave Wecker, Nathan Wiebe, Andrew C. Doherty, and Matthias Troyer. "Trotter step size required for accurate quantum simulation of quantum chemistry" (2014). arXiv:1406.4920.
- [6] Luis A. Martínez-Martínez, Tzu-Ching Yen, and Artur F. Izmaylov. "Assessment of various Hamiltonian partitionings for the electronic structure problem on a quantum computer using the Trotter approximation". Quantum 7, 1086 (2023).
- [7] Gumaro Rendon, Jacob Watkins, and Nathan Wiebe. "Improved error scaling for trotter simulations through extrapolation" (2022). arXiv:1406.4920.
- [8] Trygve Helgaker, Poul Jørgensen, and Jeppe Olsen. "Molecular electronic structure theory". John Wiley & Sons, LTD. Chichester (2000).
- [9] Tzu-Ching Yen and Artur F. Izmaylov. "Cartan subalgebra approach to efficient measurements of quantum observables". PRX Quantum 2, 040320 (2021).
- [10] Mario Motta, Erika Ye, Jarrod R. McClean, Zhendong Li, Austin J. Minnich, Ryan Babbush, and Garnet Kin-Lic Chan. "Low rank representations for quantum simulation of electronic structure". npj Quantum Inf. 7, 83 (2021).
- [11] Joonho Lee, Dominic W. Berry, Craig Gidney, William J. Huggins, Jarrod R. McClean, Nathan Wiebe, and Ryan Babbush. "Even more efficient quantum computations of chemistry through tensor hypercontraction". PRX Quantum 2, 030305 (2021).
- [12] Zachary Pierce Bansingh, Tzu-Ching Yen, Peter D Johnson, and Artur F Izmaylov. "Fidelity overhead for nonlocal measurements in variational quantum algorithms". J. Phys. Chem. A 126, 7007–7012 (2022).
- [13] Ewout Van Den Berg and Kristan Temme. "Circuit optimization of hamiltonian simulation by simultaneous diagonalization of pauli clusters". Quantum 4, 322 (2020).
- [14] Tzu-Ching Yen, Vladyslav Verteletskyi, and Artur F Izmaylov. "Measuring all compatible operators in one series of single-qubit measurements using unitary transformations". J. Chem. Theory Comput. 16, 2400–2409 (2020).
- [15] Vladyslav Verteletskyi, Tzu-Ching Yen, and Artur F. Izmaylov. "Measurement optimization in the variational quantum eigensolver using a minimum clique cover". J. Chem. Phys. 152,

- 124114 (2020).
- [16] Jarrod R McClean, Nicholas C Rubin, Kevin J Sung, Ian D Kivlichan, Xavier Bonet-Monroig, Yudong Cao, Chengyu Dai, E Schuyler Fried, Craig Gidney, Brendan Gimby, et al. "Openfermion: the electronic structure package for quantum computers". Quantum Sci. Technol. 5, 034014 (2020).
- [17] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. "SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python". Nat. Methods 17, 261–272 (2020).
- [18] Sergey Bravyi, Jay M. Gambetta, Antonio Mezzacapo, and Kristan Temme. "Tapering off qubits to simulate fermionic hamiltonians" (2017). arXiv:1701.08213.
- [19] Marcelo Ponce, Ramses van Zon, Scott Northrup, Daniel Gruner, Joseph Chen, Fatih Ertinaz, Alexey Fedoseev, Leslie Groer, Fei Mao, Bruno C. Mundim, Mike Nolta, Jaime Pinto, Marco Saldarriaga, Vladimir Slavnic, Erik Spence, Ching-Hsing Yu, and W. Richard Peltier. "Deploying a top-100 supercomputer for large parallel workloads: the niagara supercomputer". In Practice and Experience in Advanced Research Computing 2019: Rise of the Machines (Learning). PEARC '19New York, NY, USA (2019). Association for Computing Machinery.
- [20] Andrew Tranter, Peter J. Love, Florian Mintert, Nathan Wiebe, and Peter V. Coveney. "Ordering of trotterization: Impact on errors in quantum simulation of electronic structure". Entropy 21, 1218 (2019).
- [21] Dominic W. Berry, Dominic W. Berry, Brendon Higgins, Stephen D. Bartlett, Morgan W. Mitchell, Geoff J. Pryde, and Howard M. Wiseman. "How to perform the most accurate possible phase measurements". Phys. Rev. A 80, 052114 (2009).
- [22] Ian D. Kivlichan, Craig Gidney, Dominic W. Berry, Nathan Wiebe, Jarrod McClean, Wei Sun, Zhang Jiang, Nicholas Rubin, Austin Fowler, Alán Aspuru-Guzik, Hartmut Neven, and Ryan Babbush. "Improved Fault-Tolerant Quantum Simulation of Condensed-Phase Correlated Electrons via Trotterization". Quantum 4, 296 (2020).

# Appendix A: Fermionic and Qubit-based Hamiltonian Decomposition methods

Here, we discuss the methods we used to decompose electronic Hamiltonians into fast-forwardable fragments using fermionic- and qubit-based methods. The second quantized representation of the molecular electronic Hamiltonian with N single particle spin-orbitals under this representation is

$$\hat{H} = \sum_{pq=1}^{N} h_{pq} \hat{a}_{p}^{\dagger} \hat{a}_{q} + \sum_{pqrs=1}^{N} g_{pqrs} \hat{a}_{p}^{\dagger} \hat{a}_{q} \hat{a}_{r}^{\dagger} \hat{a}_{s}$$
(A1)

where  $a_p^{\dagger}$  ( $a_q$ ) is the creation (annihilation) fermionic operator for the  $p^{th}$  spin-orbital,  $h_{pq}$  and  $g_{pqrs}$  are one- and two-electron integrals.[8]

## 1. Fermionic partitioning methods

These partitioning methods are built upon the solvability of one-electron Hamiltonians using orbital rotations, according to

$$\hat{H}_{1e} = \sum_{pq} h_{pq} \hat{a}_p^{\dagger} \hat{a}_q = \hat{U}_1^{\dagger} \left( \sum_p \tilde{h}_p \hat{n}_p \right) \hat{U}_1, \tag{A2}$$

$$\hat{U}_1 = \prod_{p>q} e^{\theta_{pq}(\hat{a}_p^{\dagger} \hat{a}_q - \hat{a}_q^{\dagger} \hat{a}_p)} \tag{A3}$$

where  $\hat{n}_p = \hat{a}_p^{\dagger} \hat{a}_q$  occupation number operators,  $\tilde{h}_p$  are real constants, and  $\hat{U}_1$  is an orbital rotation parameterized by the amplitudes  $\theta_{pq}$ . Orbital rotations can also be employed to solve two-electron Hamiltonians that are squares of one-electron Hamiltonians as follows:

$$\hat{H}^{(LR)} = \left(\sum_{pq} h_{pq} \hat{a}_p^{\dagger} \hat{a}_q\right)^2 = \hat{U}^{\dagger} \left(\sum_{p} \tilde{h}_p \hat{n}_p\right)^2 \hat{U} \tag{A4}$$

$$= \hat{U}^{\dagger} \left( \sum_{pq} \tilde{h}_p \tilde{h}_q \hat{n}_p \hat{n}_q \right) \hat{U}. \tag{A5}$$

The matrix with entries  $\lambda_{pq} = \tilde{h}_p \tilde{h}_q$  is a rank-deficient one. The form of two-electron solvable Hamiltonians by means of orbital rotations in (A4) can be straightforwardly generalized by lifting the rank-deficient character of  $\lambda$  matrix and regarding it as a full-rank hermitian matrix:

$$\hat{H}^{(FR)} = \hat{U}^{\dagger} \left( \sum_{pq} \lambda_{pq} \hat{n}_p \hat{n}_q \right) \hat{U}. \tag{A6}$$

The fermionic methods that follow are classified according to whether the Hamiltonian decomposition yields fast-forwardable fragments with low- or full-rank character.

Greedy Full Rank Optimization (GFRO): The approach uses orbital rotations to diagonalize the one-electron part and approximate the two-body interaction terms featured in Eq. (A1) as a sum of full-rank Hamiltonian fragments of the form (A6) [9]

$$\hat{H} = \hat{H}_{1e} + \sum_{m=2}^{M} \hat{H}_{m}^{(FR)}.$$
(A7)

The decomposition is carried out in a greedy fashion to select an optimal Hamiltonian fragment  $\hat{H}_{i+1}^{(FR)}$  [Eq. (A6)] that minimizes the  $L_1$  norm of the  $\tilde{G}^{(i+1)}$  tensor at the  $i^{th}$  iteration:

$$\sum_{pqrs=1}^{N} \tilde{G}_{pqrs}^{(i+1)} \hat{a}_{p}^{\dagger} \hat{a}_{q} \hat{a}_{s}^{\dagger} a_{s} = \sum_{pqrs}^{N} \tilde{G}_{pqrs}^{(i)} \hat{a}_{p}^{\dagger} \hat{a}_{q} \hat{a}_{r}^{\dagger} \hat{a}_{s} - \hat{H}_{i+1}^{(FR)}$$
(A8)

for  $i \geq 1$  and  $\tilde{G}_{pqrs}^{(1)} = g_{pqrs}$ , as a function of parameters  $\{\lambda_{pq}^{(m)}\}$  and  $\{\theta^{(m)}\}$ .

Low-rank (LR) decomposition: This partitioning method is based on regarding the two-electron integral tensor  $g_{pqrs}$  in Eq. (A1) as a square matrix with composite indices along each dimension. It has been shown [10] that rank-deficient Hamiltonian fragments can be efficiently found by means of nested factorizations on this matrix, such that

$$\hat{H} = \hat{H}_{1e} + \sum_{m=2}^{M} \hat{H}_{m}^{(LR)},\tag{A9}$$

where

$$\hat{H}_{m}^{(LR)} = \hat{U}_{m}^{\dagger} \left( \sum_{p,q} \tilde{h}_{p}^{(m)} \tilde{h}_{q}^{(m)} \hat{n}_{p} \hat{n}_{q} \right) \hat{U}_{m}$$
(A10)

**Pre- and post-processing of Hamiltonian fragments:** So far, the one-body electronic terms of the Hamiltonian in Eq. (A1) have been relegated given their straightforward orbital-rotation solvability. However, the one-electron Hamiltonian in (A1) can be partitioned in the same footing as the discussed methods by merging the former in the two-body electronic

terms as follows

$$\hat{H} = \hat{U}_1^{\dagger} \left( \sum_p \varepsilon_p \hat{a}_p^{\dagger} \hat{a}_p \right) \hat{U}_1 + \sum_{pqrs} g_{pqrs} \hat{a}_p^{\dagger} \hat{a}_q \hat{a}_r^{\dagger} \hat{a}_s \tag{A11}$$

$$= \hat{U}_{1}^{\dagger} \left( \sum_{pq,rs} \left[ \tilde{g}_{pq,rs} + \varepsilon_{p} \delta_{pq} \delta_{pr} \delta_{ps} \right] \hat{a}_{p}^{\dagger} \hat{a}_{q} \hat{a}_{r}^{\dagger} \hat{a}_{s} \right) \hat{U}_{1}$$
(A12)

$$= \sum_{p'q,r's'} \bar{g}_{p'q',r's'} \hat{a}_p^{\dagger} \hat{a}_q \hat{a}_r^{\dagger} \hat{a}_s, \tag{A13}$$

the decomposition of the ensuing two-electron Hamiltonian can be carried out with the fermionic techniques discussed above. For computational ease, in this work we consider the decomposition of the Hamiltonian (A13) with the GFRO approach, and refer to our combined scheme as SD GFRO, where SD stands for "singles and doubles" in analogy to the terminology used in the electronic structure literature for single and double fermionic excitation operators. In addition to the pre-processing discussed above, we consider a post-processing technique that usually lowers the Trotter approximation error estimator  $\alpha$  and relies on the removal of the one-body electron contributions encoded within each of the two-body Hamiltonian fragments and grouping the former in a single one-body electronic sub-Hamiltonian. This is accomplished by employing the approach based in [11], where two-body interaction terms are written as a Linear Combination of Unitaries (LCU), with a concomitant adjustment of the one-body Hamiltonian contributions: [6]

$$\hat{H} = \sum_{pq=1}^{N} \left( h_{pq} + \sum_{l} g_{pq,ll} \right) \hat{a}_{p}^{\dagger} \hat{a}_{q} + \sum_{l=2} \hat{U}_{l}^{\dagger} \left( \sum_{i,j}^{N} \frac{\lambda_{ij}^{(l)}}{4} \hat{r}_{i} \hat{r}_{i} \right) \hat{U}_{l}$$
 (A14)

$$-\frac{1}{4}\sum_{p,q}g_{pp,qq}.\tag{A15}$$

## 2. Qubit-based partitioning methods

When the Hamiltonian (A1) is mapped to N interacting two-level systems through encodings such as Jordan-Wigner or Bravyi-Kitaev, the Hamiltonian thus obtained is of the form,

$$\hat{H}_q = \sum_n c_n \hat{P}_n$$
 where  $\hat{P}_n = \bigotimes_{k=1}^N \hat{\sigma}_k^{(n)}$ 

where,  $c_n$  are numerical coefficients and  $\hat{P}_n$  are tensor products of single-qubit Pauli operators and the identity,  $\hat{\sigma}_k^{(n)} = \hat{x}_k, \hat{y}_k, \hat{z}_k, \hat{I}_k$ , acting on the  $k^{th}$  qubit. The Fully Commuting (FC)

grouping partitions  $\hat{H}_q$  into  $\hat{H}_n^{(FC)}$  fragments containing commuting Pauli products:

if 
$$\hat{P}_i, \hat{P}_j \in \hat{H}_n^{(FC)}$$
 then  $[\hat{P}_i, \hat{P}_j] = 0$ .

This FC condition ensures that  $\hat{H}_n^{(FC)}$  can be transformed, through a series of Clifford group transformations, into sums of only products of Pauli  $\hat{z}_k$  operators.[12, 13] We also consider a grouping with a more strict condition known as qubit-wise commutativity (QWC), where each single-qubit Pauli operator in one product commutes with its counterpart in the other product. For example,  $\hat{x}_1\hat{y}_2\hat{I}_3$  and  $\hat{x}_1\hat{I}_2\hat{z}_3$  have QWC as  $[\hat{x}_1,\hat{x}_1]=0$ ,  $[\hat{y}_2,\hat{I}_2]=0$ ,  $[\hat{I}_3,\hat{z}_3]=0$ . Hence, both terms must also fully commute. The converse does not always hold true. For example,  $\hat{x}_1\hat{x}_2$  and  $\hat{y}_1\hat{y}_2$  are fully commuting but not qubit-wise commuting.[14]

For the FC and QWC partitioning techniques, we work with the largest-first (LF) heuristic and the Sorted Insertion (SI) algorithm. The SI algorithm is based on a greedy partitioning of the Hamiltonian, which results in concentrated coefficients  $c_n$  in the first found Hamiltonian fragments. The LF algorithm, in contrast, yields a homogeneous distribution in the magnitudes of the  $c_n$  coefficients across Hamiltonian fragments, which usually results in a smaller number of fragments compared to the SI version [14, 15].

## 3. Details of the Hamiltonians and Wavefunctions

The Hamiltonians were generated using the STO-3G basis and the Jordan-Wigner transformations for qubit encodings as implemented in the OpenFermion package [16]. The nuclear geometries for the molecules are given by R(H-H)=1 Å (H<sub>2</sub>), R(Li-H)=1 Å (LiH) and R(Be-H)=1 Å with collinear atomic arrangement (BeH<sub>2</sub>), R(OH)= 1.9 Å and  $\angle HOH$ =104.5° (H<sub>2</sub>O); and R(N-H)=1.9 Å with  $\angle HNH$ =107° (NH<sub>3</sub>). The ground state CISD wavefunction is generated using the OpenFermion package.

## 4. Computation of errors for the second order Trotter approximation

From Eq. (5) of the main text,  $\hat{H}_{\text{eff}}$  is computed through

$$\hat{H}_{\text{eff}} = it^{-1} \ln \left( \hat{U}_T^{(2)}(t) \right),$$
 (A16)

where  $t = \mathcal{O}(||\hat{H}||^{-1})$ .  $\varepsilon$ 's are obtained according to  $\varepsilon = t^{-2}|E_0^{(T)} - E_0|$ , where  $E_0^{(T)}$  ( $E_0$ ) is the ground state energy of  $\hat{H}_{\text{eff}}$  ( $\hat{H}$ ). All these calculations were performed using the python

Scipy library [17]. To reduce computational overhead in our calculations, we take advantage of the fact that the initial state  $|\psi\rangle$  belongs to a particular irreducible representation of the molecular symmetries: the number of electrons,  $\hat{N}_e$ , the electron spin,  $\hat{S}^2$ , and its projection,  $\hat{S}_z$ . Selecting symmetry adapted states for the neutral singlet molecular forms allowed to reduce the Hamiltonian sub-spaces by almost two orders of magnitude. Similarly, for qubit-based partitioning methods, we use qubit tapering to reduce the system size of NH<sub>3</sub> from a 16-qubit system to a 14-qubit system [18]. Since the number qubit fragments and their sizes are usually large for BeH<sub>2</sub>, H<sub>2</sub>O and NH<sub>3</sub>, instead of exponentiating each fragment exactly, we approximate the exponential using Taylor series up to 11<sup>th</sup> order in time. We make use of the Niagara compute cluster hosted by SciNet [19] for memory intensive calculations. The Trotter approximation error depends on the order in which individual unitaries  $e^{-it\hat{H}_n}$  are applied [20]. The code to generate Hamiltonian fragments and calculate the Trotter error can be accessed at https://doi.org/10.5281/zenodo.15327942.

# 5. Effective Hamiltonian derivation based on BCH expansion.

In this section we generalize the BCH formula, usually defined for two Hamiltonian fragments, to an arbitrary number of fragments N. We will use mathematical induction with a starting point:

$$e^{-iH_2t}e^{-iH_1t} = \exp\left(-iH_{\text{eff}}^{(2)}t\right),$$
 (A17)

where

$$H_{\text{eff}}^{(2)} = H_2 + H_1 + \frac{(-i)}{2}t[H_2, H_1] + \frac{(-i)^2}{12}t^2[H_2, [H_2, H_1]] - \frac{(-i)^2}{12}t^2[H_1, [H_2, H_1]] + \mathcal{O}(t^3).$$

To obtain the form of the effective Hamiltonian for N fragments,  $H_{\text{eff}}^{(N)}$  we extend Eq. (A17) to the three-fragment case:

$$e^{-iH_3t}e^{-iH_2t}e^{-iH_1t} = e^{-iH_3t}e^{-iH_{\text{eff}}^{(2)}t} = \exp\left(-iH_3t - iH_{\text{eff}}^{(2,1)}t + \frac{(-i)^2}{2}t^2[H_3, H_{\text{eff}}^{(2,1)}]\right)$$
$$+ \frac{(-i)^3}{12}t^3[H_3, [H_3, H_{\text{eff}}^{(2,1)}]] - \frac{(-i)^3}{12}t^3[H_{\text{eff}}^{(2,1)}, [H_3, H_{\text{eff}}^{(2,1)}]] + \mathcal{O}(t^4)$$
$$= \exp\left(\hat{A}\right)$$

where  $\hat{A}$  becomes

$$\begin{split} \hat{A} &= -iH_3t - iH_2t - iH_1t + \frac{(-i)^2}{2}t^2[H_2, H_1] + \frac{(-i)^2}{2}t^2[H_3, H_1] + \frac{(-i)^2}{2}t^2[H_3, H_2] \\ &+ \frac{(-i)^3}{12}t^3[H_2, [H_2, H_1]] - \frac{(-i)^3}{12}t^3[H_1, [H_2, H_1]] + \frac{(-i)^3}{4}t^3[H_3, [H_2, H_1]] \\ &+ \frac{(-i)^3}{12}t^3[H_3, [H_3, H_2]] + \frac{(-i)^3}{12}t^3[H_3, [H_3, H_1]] - \frac{(-i)^3}{12}t^3[H_1, [H_3, H_1]] \\ &- \frac{(-i)^3}{12}t^3[H_2, [H_3, H_1]] - \frac{(-i)^3}{12}t^3[H_1, [H_3, H_2]] - \frac{(-i)^3}{12}t^3[H_2, [H_3, H_2]] + \mathcal{O}(t^4) \\ &= -iH_3t - iH_2t - iH_1t + \frac{(-i)^2}{2}t^2\sum_{v>\mu}^3[H_v, H_\mu] + \frac{(-i)^3}{4}t^3\sum_{v'>v>\mu}^3[H_{v'}, [H_v, H_\mu]] \\ &+ \frac{(-i)^3}{12}t^3\sum_{v>\mu}^3[H_v, [H_v, H_\mu]] - \frac{(-i)^3}{12}t^3\sum_{v>\mu}^3[H_{v'}, [H_v, H_\mu]] + \mathcal{O}(t^4). \end{split}$$

We note that  $\hat{A}$  can be written in the form

$$\hat{A} = -it \left( H^{(3)} + \frac{t}{2} \hat{v}_1^{(3)} + \frac{t^2}{3} \hat{v}_2^{(3)} + i \frac{t^2}{12} [H^{(3)}, \hat{v}_1^{(3)}] + \mathcal{O}(t^3) \right), \tag{A18}$$

where

$$H^{(n)} = \sum_{j=1}^{n} H_j,$$

$$\hat{v}_1^{(n)} = -i \sum_{v=\mu+1}^{n} \sum_{\mu=1}^{n-1} [H_v, H_\mu],$$

$$\hat{v}_2^{(n)} = -\sum_{v'=v}^{n} \sum_{v=\mu+1}^{n} \sum_{\mu=1}^{n-1} \left(1 - \frac{\delta_{v',v}}{2}\right) [H_{v'}, [H_v, H_\mu]].$$

Finally, to show that the form (A18) can be generalized for an arbitrary number of Hamiltonian fragments, we use induction:

$$e^{-iH_{n+1}t}e^{-iH_{\text{eff}}^{(n)}t} = \exp\left(-iH_{\text{eff}}^{(n)}t - iH_{n+1}t + \frac{(-i)^2}{2}t^2[H_{n+1}, H_{\text{eff}}^{(n)}] + \frac{(-i)^3}{12}t^3[H_{n+1}, [H_{n+1}, H_{\text{eff}}^{(n)}]] - \frac{(-i)^3}{12}t^3[H_{\text{eff}}^{(n)}, [H_{n+1}, H_{\text{eff}}^{(n)}]] + \mathcal{O}(t^4)\right)$$

$$= \exp\left(\hat{B}\right),$$

where

$$\hat{B} = -iH_{n+1}t - iH^{(n)}t - i\frac{t^2}{2}\hat{v}_1^{(n)} - i\frac{t^3}{3}\hat{v}_2^{(n)} + \frac{t^3}{12}[\hat{H}^{(n)}, \hat{v}_1^{(n)}]$$

$$+ \frac{(-i)^2}{2}t^2[H_{n+1}, H^{(n)} + \frac{t}{2}\hat{v}_1^{(n)}] + \frac{(-i)^3}{12}t^3[H_{n+1}, [H_{n+1}, H^{(n)}]]$$

$$- \frac{(-i)^3}{12}t^3[H^{(n)}, [H_{n+1}, H^{(n)}]] + \mathcal{O}(t^4)$$

$$= -i\left(H_{n+1} + H^{(n)}\right)t - i\frac{t^2}{2}\left(\hat{v}_1^{(n)} - i[H_{n+1}, H^{(n)}]\right)$$

$$- i\frac{t^3}{3}\left(\hat{v}_2^{(n)} - \frac{1}{2}[H_{n+1}, [H_{n+1}, H^{(n)}]] - i[H_{n+1}, \hat{v}_1^{(n)}]\right)$$

$$+ \frac{t^3}{12}\left([H^{(n)}, \hat{v}_1^{(n)}] - i[H^{(n)}, [H_{n+1}, H^{(n)}]] + [H_{n+1}, \hat{v}_1^{(n)}]\right)$$

$$- i[H_{n+1}, [H_{n+1}, H^{(n)}]] \right).$$

By using

$$H^{(n+1)} = H^{(n)} + H_{n+1}$$

$$\hat{v}_1^{(n+1)} = \hat{v}_1^{(n)} - i[\hat{H}_{n+1}, \hat{H}^{(n)}]$$

$$\hat{v}_2^{(n+1)} = \hat{v}_2^{(n)} - \frac{1}{2}[H_{n+1}, [H_{n+1}, H^{(n)}]] - i[H_{n+1}, \hat{v}_1^{(n)}]$$

$$[\hat{H}^{(n+1)}, \hat{v}_1^{(n+1)}] = [H^{(n)}, \hat{v}_1^{(n)}] - i[H^{(n)}, [H_{n+1}, H^{(n)}]]$$

$$+ [H_{n+1}, \hat{v}_1^{(n)}] - i[H_{n+1}, [H_{n+1}, H^{(n)}]]$$

we have

$$H_{\text{eff}}^{(n+1)} = H^{(n+1)} + \frac{t}{2}\hat{v}_1^{(n+1)} + \frac{t^2}{3}\hat{v}_2^{(n+1)} + i\frac{t^2}{12}[H^{(n+1)}, \hat{v}_1^{(n+1)}] + \mathcal{O}(t^3).$$

Therefore, for Hamiltonian H decomposed into N Hamiltonian fragments, the effective Hamiltonian  $H_{\text{eff}}$  is

$$H_{\text{eff}} = H^{(N)} + \frac{\tau}{2} \hat{v}_{1}^{(N)} + \frac{\tau^{2}}{3} \hat{v}_{2}^{(N)} + i \frac{\tau^{2}}{12} [H^{(N)}, \hat{v}_{1}^{(N)}] + \mathcal{O}(\tau^{3})$$

$$= H + \frac{\tau}{2} \hat{v}_{1} + \frac{\tau^{2}}{3} \hat{v}_{2} + i \frac{\tau^{2}}{12} [H, \hat{v}_{1}] + \mathcal{O}(\tau^{3})$$

$$= H + \hat{V}_{1}\tau + \hat{V}_{2}\tau^{2} + \mathcal{O}(\tau^{3}),$$
(A19)

where

$$\hat{V}_{1} = \frac{\hat{v}_{1}}{2} = -\frac{i}{2} \sum_{v=\mu+1}^{N} \sum_{\mu=1}^{N-1} [H_{v}, H_{\mu}],$$

$$\hat{V}_{2} = \frac{1}{3} \hat{v}_{2} + \frac{i}{12} [H, \hat{v}_{1}]$$

$$= -\frac{1}{3} \sum_{v'=v}^{N} \sum_{v=\mu+1}^{N} \sum_{\mu=1}^{N-1} \left(1 - \frac{\delta_{v',v}}{2}\right) [H_{v'}, [H_{v}, H_{\mu}]] + \frac{i}{6} [H, \hat{V}_{1}].$$
(A20)

To get the special case of second order Trotter, use N = 2M, where M is the number of Hamiltonian fragments, and  $H_{M+i} = H_{M+1-i}$  for i = 1 to M. Also, each of the fragment will have to be rescaled by a factor of half, as we repeat each fragment twice in the second order Tortter formula [see Eq. (2)]. With this constraint, for every commutator  $[H_{\mu}, H_{\nu}]$  in the expression of  $\hat{V}_1$ , there exists a commutator  $[H_{\nu}, H_{\mu}]$  with the same coefficient. Thus,  $\hat{V}_1$  equals zero. Using the same constraint in the expression of  $\hat{V}_2$ , we recover Eq. (7).

# 6. Compendium of different Trotter approximation error upper bounds

Tables III-V compile Trotter approximation error estimates based on  $\varepsilon$ ,  $\alpha$ , and  $\alpha_e$  quantities. Tables VI and VII summarize  $\varepsilon_{app}$  and  $\varepsilon_2$  values. These results are obtained by considering the Trotterized unitary:

$$\hat{U}_T^{(2)}(t) = \prod_{m=1}^M e^{-i\hat{H}_m t/2} \prod_{m=M}^1 e^{-i\hat{H}_m t/2}.$$

where the ordering of Hamiltonian fragments was taken as found by the different partition methods with no further post-processing.

# 7. T-gate count upper bound estimations

Upper-bound for T-gate counts for a fixed target error  $\varepsilon_{Tot}$  in energy eigenvalue estimation in a Trotterized Quantum Phase Estimation algorithm can be formulated in light of previous works [21, 22]. The total T-gate count  $N_T$  [4, 22] is given by

$$N_T = N_R N_{HT} N_{PE} \tag{A21}$$

where  $N_R$  is the number of single-qubit rotations needed for the implementation of a single Trotter step in a quantum computer.  $N_{HT}$  refers to the number of T gates needed to compile

| Molecule         | QWC                  | QWC                  | FC                   | FC                   | LR                 | GFRO                 | LR                   | GFRO                 | SD                   |
|------------------|----------------------|----------------------|----------------------|----------------------|--------------------|----------------------|----------------------|----------------------|----------------------|
|                  | LF                   | SI                   | LF                   | SI                   | LCU                | LCU                  |                      |                      | GFRO                 |
| $H_2$            | $3.3\times10^{-3}$   | $3.3\times10^{-3}$   | $3.3\times10^{-3}$   | $3.3\times10^{-3}$   | $3.3\times10^{-3}$ | $3.3\times10^{-3}$   | $2.8\times10^{-3}$   | $2.8 \times 10^{-3}$ | $3.1\times10^{-3}$   |
| LiH              | $3.2\times10^{-3}$   | $2.2 \times 10^{-3}$ | $3.0\times10^{-3}$   | $2.4 \times 10^{-3}$ | $3.3\times10^{-3}$ | $3.4 \times 10^{-3}$ | $4.7 \times 10^{-2}$ | $5.0 \times 10^{-2}$ | $1.8 \times 10^{-2}$ |
| BeH <sub>2</sub> | $1.4 \times 10^{-2}$ | $1.1 \times 10^{-2}$ | $2.3 \times 10^{-2}$ | $8.8 \times 10^{-3}$ | $9.3\times10^{-3}$ | $9.6 \times 10^{-3}$ | $2.9\times10^{-2}$   | $3.3 \times 10^{-2}$ | $2.0 \times 10^{-2}$ |
| H <sub>2</sub> O | $6.2\times10^{-3}$   | $4.8 \times 10^{-3}$ | $2.4 \times 10^{-2}$ | $2.9\times10^{-3}$   | $2.4\times10^{-2}$ | $2.5\times10^{-2}$   | $1.4\times10^{-1}$   | $1.3 \times 10^{-1}$ | $2.6\times10^{-2}$   |
| $\rm NH_3$       | $1.1 \times 10^{-2}$ | $1.0 \times 10^{-2}$ | $9.0 \times 10^{-2}$ | $1.5 \times 10^{-2}$ | $2.0\times10^{-2}$ | $2.0\times10^{-2}$   | $1.7\times10^{-1}$   | $1.4 \times 10^{-1}$ | $2.9 \times 10^{-2}$ |

TABLE III:  $\varepsilon$  values obtained from true Trotter approximation error scaling for different fermionic and qubit-based partitioning methods and molecules

| Molecule         | QWC   | QWC   | FC     | FC    | LR    | GFRO  | LR    | GFRO  | SD    |
|------------------|-------|-------|--------|-------|-------|-------|-------|-------|-------|
|                  | LF    | SI    | LF     | SI    | LCU   | LCU   |       |       | GFRO  |
| $H_2$            | 0.02  | 0.02  | 0.02   | 0.02  | 0.02  | 0.02  | 0.02  | 0.02  | 0.02  |
| LiH              | 1.07  | 0.26  | 0.63   | 0.26  | 0.13  | 0.12  | 0.52  | 0.46  | 0.23  |
| $\mathrm{BeH}_2$ | 4.22  | 1.02  | 4.96   | 0.99  | 0.58  | 0.55  | 2.36  | 2.03  | 1.13  |
| H <sub>2</sub> O | 79.41 | 28.73 | 181.56 | 27.86 | 15.30 | 15.06 | 52.37 | 48.27 | 27.88 |
| $NH_3$           | 51.66 | 16.36 | 65.99  | 16.02 | 7.81  | 7.64  | 28.43 | 25.79 | 14.51 |

TABLE IV: Values of Trotter approximation error upper bound  $\alpha$  as defined in Eq. (4).

one single qubit rotation (for a fixed target error  $\varepsilon_{HT}$ ) and  $N_{PE}$  is the number of Trotter steps required to resolve the target energy eigenvalue under a target uncertainty  $\varepsilon_{PE}$ , the latter scaling as  $t^{-1}$ , t being the total simulation time. Using our results that describe the energy deviation in the estimated ground-state energy eigenvalue due to the Trotter approximation, according to the relation  $\varepsilon \Delta t^2 = \Delta E_T$ , we find the Trotter step  $\Delta t$  according to a target error  $\varepsilon_{TS}$ , given by  $\Delta t = \sqrt{\frac{\varepsilon_{TS}}{\varepsilon}}$ . The number of Trotter steps needed for a target uncertainty in phase estimation under adaptive phase estimation techniques is given by

$$N_{PE} \approx \frac{0.76\pi}{\varepsilon_{PE}\Delta t} = \frac{0.76\pi\sqrt{\varepsilon}}{\varepsilon_{PE}\sqrt{\varepsilon_{TS}}}$$
 (A22)

Finally, the number of T gates needed to compile one single qubit rotation for a fixed target error  $\varepsilon_{HT}$  is  $N_{HT} = 1.15 \log_2 \left( \frac{N_R}{\varepsilon_{HT} \Delta t} \right) + 9.2 = 1.15 \log_2 \left( \frac{N_R \sqrt{\varepsilon}}{\varepsilon_{HT} \sqrt{\varepsilon_{TS}}} \right) + 9.2$ . Putting everything

| Molecule         | QWC   | QWC   | FC    | FC    | LR   | GFRO  | LR    | GFRO  | SD    |
|------------------|-------|-------|-------|-------|------|-------|-------|-------|-------|
|                  | LF    | SI    | LF    | SI    | LCU  | LCU   |       |       | GFRO  |
| $H_2$            | 0.02  | 0.01  | 0.02  | 0.01  | 0.01 | 0.01  | 0.01  | 0.01  | 0.01  |
| LiH              | 0.22  | 0.18  | 0.25  | 0.18  | 0.10 | 0.10  | 0.07  | 0.08  | 0.06  |
| $\mathrm{BeH}_2$ | 0.67  | 0.75  | 0.81  | 0.76  | 0.42 | 0.43  | 0.29  | 0.35  | 0.36  |
| H <sub>2</sub> O | 23.25 | 23.42 | 46.45 | 23.45 | 1.85 | 11.86 | 15.67 | 14.88 | 12.87 |
| NH <sub>3</sub>  | 11.23 | 11.23 | 15.86 | 11.21 | 6.55 | 6.56  | 7.25  | 7.05  | 6.03  |

TABLE V: Values of 
$$\alpha_e = \left\| \hat{U}_T(t) - \hat{U}_T^{(2)}(t) \right\| / t^3$$
.

| Molecule         | QWC-LF                | QWC-SI                | FC-LF               | FC-SI               | LR LCU                | GFRO LCU              | LR                    | GFRO                  | SD-GFRO               |
|------------------|-----------------------|-----------------------|---------------------|---------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| $H_2$            | $3.24 \times 10^{-3}$ | $3.24\times10^{-3}$   | $3.24\times10^{-3}$ | $3.24\times10^{-3}$ | $3.24\times10^{-3}$   | $3.24 \times 10^{-3}$ | $2.77\times10^{-3}$   | $2.78 \times 10^{-3}$ | $3.00\times10^{-3}$   |
| LiH              | $3.26 \times 10^{-3}$ | $2.18\times10^{-3}$   | $3.02\times10^{-3}$ | $2.46\times10^{-3}$ | $3.30\times10^{-3}$   | $3.39 \times 10^{-3}$ | $4.72 \times 10^{-2}$ | $4.99 \times 10^{-2}$ | $1.82 \times 10^{-2}$ |
| $\mathrm{BeH}_2$ | $1.38\times10^{-2}$   | $1.12 \times 10^{-2}$ | $2.25\times10^{-2}$ | $8.93\times10^{-3}$ | $9.49 \times 10^{-3}$ | $9.83 \times 10^{-3}$ | $2.89\times10^{-2}$   | $3.36 \times 10^{-2}$ | $1.98 \times 10^{-2}$ |
| H <sub>2</sub> O | $9.78 \times 10^{-3}$ | $8.04 \times 10^{-3}$ | $1.99\times10^{-2}$ | $6.03\times10^{-3}$ | $3.22\times10^{-2}$   | $3.52 \times 10^{-2}$ | $1.78\times10^{-1}$   | $1.67 \times 10^{-1}$ | $3.48 \times 10^{-2}$ |
| $NH_3$           | $1.31 \times 10^{-2}$ | $1.57 \times 10^{-2}$ | $7.79\times10^{-2}$ | $1.05\times10^{-2}$ | $3.33\times10^{-2}$   | $3.44 \times 10^{-2}$ | $2.34\times10^{-1}$   | $2.09 \times 10^{-1}$ | $4.75 \times 10^{-2}$ |

TABLE VI:  $\varepsilon_{\rm app} = \langle \psi_0 | \hat{V}_2 | \psi_0 \rangle$  for different Hamiltonian decomposition methods and molecules.

together we arrive at

$$N_T \approx \frac{0.76\pi N_R \sqrt{\varepsilon}}{\sqrt{\varepsilon_{TS}} \varepsilon_{PE}} \left[ 1.15 \log_2 \left( \frac{N_R \sqrt{\varepsilon}}{\varepsilon_{HT} \sqrt{\varepsilon_{TS}}} \right) + 9.2 \right]$$
 (A23)

In the worst case, the errors due to the three sources discussed above, add linearly [22] and to guarantee that the total error is at most  $\varepsilon_{Tot}$  we assume

$$\varepsilon_{Tot} = \varepsilon_{TS} + \varepsilon_{PE} + \varepsilon_{HT}. \tag{A24}$$

| Molecule           | QWC-LF                | QWC-SI              | FC-LF               | FC-SI               | LR LCU              | GFRO LCU              | LR                          | GFRO                  | SD-GFRO               |
|--------------------|-----------------------|---------------------|---------------------|---------------------|---------------------|-----------------------|-----------------------------|-----------------------|-----------------------|
| $H_2$              | $3.24\times10^{-3}$   | $3.24\times10^{-3}$ | $3.24\times10^{-3}$ | $3.24\times10^{-3}$ | $3.24\times10^{-3}$ | $3.24 \times 10^{-3}$ | $2.77\times 10^{-3}$        | $2.78\times10^{-3}$   | $3.00\times10^{-3}$   |
| LiH                | $3.25 \times 10^{-3}$ | $2.16\times10^{-3}$ | $3.01\times10^{-3}$ | $2.45\times10^{-3}$ | $3.30\times10^{-3}$ | $3.39 \times 10^{-3}$ | $4.72 \times 10^{-2}$       | $4.99 \times 10^{-2}$ | $1.82 \times 10^{-2}$ |
| $\mathrm{BeH}_2$   | $1.37 \times 10^{-2}$ | $1.10\times10^{-2}$ | $2.27\times10^{-2}$ | $8.76\times10^{-3}$ | $9.30\times10^{-3}$ | $9.63 \times 10^{-3}$ | $2.87\times10^{-2}$         | $3.34 \times 10^{-2}$ | $1.96 \times 10^{-2}$ |
| $_{\mathrm{H_2O}}$ | $6.22 \times 10^{-3}$ | $4.76\times10^{-3}$ | $2.36\times10^{-2}$ | $2.85\times10^{-3}$ | $2.37\times10^{-2}$ | $2.51 \times 10^{-2}$ | $\boxed{1.42\times10^{-1}}$ | $1.28 \times 10^{-1}$ | $2.58 \times 10^{-2}$ |
| $NH_3$             | $1.15\times10^{-2}$   | $9.98\times10^{-3}$ | $8.95\times10^{-2}$ | $1.52\times10^{-2}$ | $2.00\times10^{-2}$ | $1.98\times10^{-2}$   | $1.65\times10^{-1}$         | $1.38\times10^{-1}$   | $2.94 \times 10^{-2}$ |

TABLE VII:  $\varepsilon_2 = \langle \phi_0 | \hat{V}_2 | \phi_0 \rangle$  for different Hamiltonian decomposition methods and molecules.

Thus, we can minimize the number of T-gates  $N_T$  over the target errors in Eq. (A23) subject to the constraint (A24), for an estimation of T-gate under a target error  $\varepsilon_{Tot}$ . In this work, we have taken  $\varepsilon_{Tot} = 1.6 \times 10^{-3}$  Hartree, the chemical accuracy.