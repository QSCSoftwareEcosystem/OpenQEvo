![](_page_0_Picture_4.jpeg)

# Is the Trotterized UCCSD Ansatz Chemically Well-Defined?

Harper R. Grimsley,<sup>†</sup> Daniel Claudino,<sup>†©</sup> Sophia E. Economou,<sup>‡</sup> Edwin Barnes,<sup>‡</sup> and Nicholas J. Mayhall\*,<sup>†©</sup>

Supporting Information

ABSTRACT: The variational quantum eigensolver (VQE) has emerged as one of the most promising near-term quantum algorithms that can be used to simulate many-body systems such as molecular electronic structures. Serving as an attractive ansatz in the VQE algorithm, unitary coupled cluster (UCC) theory has seen a renewed interest in recent literature. However, unlike the original classical UCC theory, implementation on a quantum computer requires a finite-order Suzuki-Trotter decomposition to separate the exponentials of the large sum of Pauli operators. While previous literature has recognized the nonuniqueness of different orderings of the operators in the Trotterized form of UCC methods, the question of whether or not different orderings matter at the *chemical scale* has not been

![](_page_0_Picture_11.jpeg)

addressed. In this Letter, we explore the effect of operator ordering on the Trotterized UCCSD ansatz, as well as the much more compact k-UpCCGSD ansatz recently proposed by Lee et al. [J. Chem. Theory Comput., 2019, 15, 311. arXiv, 2019, quant-ph:1909.09114. https://arxiv.org/abs/1909.09114]. We observe a significant, system-dependent variation in the energies of Trotterizations with different operator orderings. The energy variations occur on a chemical scale, sometimes on the order of hundreds of kcal/mol. This Letter establishes the need to define not only the operators present in the ansatz but also the order in which they appear. This is necessary for adhering to the quantum chemical notion of a "model chemistry", in addition to the general importance of scientific reproducibility. As a final note, we suggest a useful strategy to select out of the combinatorial number of possibilities, a single well-defined and effective ordering of the operators.

The ability to accurately simulate chemistry at the subatomic level can provide deeper scientific insights and further reaching predictions than through experiment alone. Although exact simulation requires computational resources which increase exponentially with system size, many stable molecules can be accurately modeled using polynomially scaling techniques, providing accurate and interpretable results. Examples of such approximations include density-functional theory, perturbation theory, or coupled-cluster theory. To study more complicated systems with many strongly correlated electrons such as those involved in numerous catalytic systems or materials applications, more general modeling solutions are needed.

Quantum simulation, which has recently seen a dramatic increase in activity due to rapid developments in both hardware and algorithms, provides an exciting possibility for performing approximation-free simulations without the exponential computational cost plaguing classical simulations. Because the Hilbert space of a single spin—orbital can be mapped to the Hilbert space of a single qubit, the exponential growth of the molecular Hamiltonian is matched by the exponential growth of a quantum computer's Hilbert space. Consequently, a quantum computer with only tens of logical qubits could potentially demonstrate a quantum advantage. 1–3 While full error-correction is not

expected to be realized in the near future, so-called Noisy Intermediate Scaled Quantum (NISQ) devices<sup>4</sup> have interesting properties that might still offer important computational advantages.

While the first quantum algorithm proposed for simulating many-body systems, the Phase Estimation Algorithm (PEA), 1,5,6 provides a path for achieving arbitrarily accurate simulations, it does so at the cost of incredibly deep circuits. Because device noise and errors limit the number of gates that can be applied in sequence, PEA is not viable on NISQ devices. In 2014, Peruzzo and co-workers proposed and demonstrated an alternative algorithm termed the Variational Quantum Eigensolver (VQE) which offers unique advantages for NISQ devices. Unlike PEA, VQE limits the depth of the circuit, which makes it possible to implement on current and near-term devices. However, this comes at the cost of an increased number of measurements and the introduction of a wave function ansatz that can limit the accuracy of the simulation (although our recent approach, ADAPT-VQE, can remove the ansatz error).8 The initial demonstration of VQE was followed by several theoretical

Received: October 29, 2019 Published: December 16, 2019

<sup>&</sup>lt;sup>†</sup>Department of Chemistry, Virginia Tech, Blacksburg, Virginia 24061, United States

<sup>&</sup>lt;sup>‡</sup>Department of Physics, Virginia Tech, Blacksburg, Virginia 24061, United States

studies  $^{9-15}$  and demonstrations on other hardware such as superconducting qubits  $^{10,14,16}$  and trapped ions.  $^{17,18}$ 

A key ingredient in VQE is the ansatz, which is implemented as a quantum circuit which constructs trial wave functions that are measured and then updated in a classical optimization loop. The quality of the ansatz ultimately determines the accuracy of the simulated ground state energy and properties. In the original proposal, the unitary variant of coupled-cluster theory was chosen as an ansatz due to several attractive features:

- Accurate: Coupled-cluster theory is among the most accurate classical methods for many-body simulation.
- Well studied: The unitary variant of coupled-cluster singles and doubles (UCCSD) has been analyzed in detail in the context of classical simulations.<sup>19–22</sup>
- Unitary: Because a quantum circuit implements unitary operations, the unitary nature of UCCSD makes the approach natural in a VQE context.

The UCCSD ansatz is obtained by replacing the traditional Hermitian cluster operator terms in coupled cluster theory with anti-Hermitian operators

$$\begin{split} |\Psi_{\text{UCCSD}}\rangle &= e^{\hat{\mathcal{T}}_1 + \hat{\mathcal{T}}_2} |0\rangle \\ \hat{\mathcal{T}}_1 &= \sum_{ia} \theta_{ia} (a_a^{\dagger} a_i - a_i^{\dagger} a_a) \\ \hat{\mathcal{T}}_2 &= \sum_{ijab} \theta_{ijab} (a_a^{\dagger} a_b^{\dagger} a_i a_j - a_j^{\dagger} a_i^{\dagger} a_b a_a) \end{split} \tag{1}$$

where  $|0\rangle$  is the uncorrelated reference state, usually Hartree–Fock,  $a_p^{\dagger}(a_p)$  is a creation (annihilation) operator for the orbital indexed by p, and  $\{\theta_{ia},\theta_{ijab}\}$  are the parameters to be variationally optimized.

Although the unitarity of UCCSD implies an ease of implementation on quantum hardware, gate-based quantum computing requires a decomposition of operations into one- and two-qubit gates, such as single-qubit rotations and CNOT gates. In contrast, complicating direct implementation, the  $\hat{T}_n$  operators simultaneously act on N qubits. In principle, any unitary operation can be decomposed into one- and two-qubit gates. However, the number of gates produced from such a decomposition grows rapidly with the number of qubits acted on by the unitary, making it desirable to use an approximation scheme such as Suzuki-Trotter<sup>24</sup> when implementing N-qubit unitary operators.

The first-order Suzuki-Trotter approximation is given by eq 2.

$$e^{\hat{A}+\hat{B}} \approx e^{\hat{A}}e^{\hat{B}} \tag{2}$$

This becomes exact in infinite order:

$$e^{\hat{A}+\hat{B}} = \lim_{n \to \infty} \left( e^{\frac{\hat{A}}{n}} e^{\frac{\hat{B}}{n}} \right)^n \tag{3}$$

To approximate UCCSD accurately using a product form, large Trotter numbers, n, could in principle be used. This would, of course, create extremely deep circuits, making quantum simulation intractable. Alternatively, one could choose an aggressive truncation such as that in eq 2. In general, this would provide a very poor approximation to the UCCSD wave function but would provide a relatively shallow circuit that is better for NISQ realization. Note the stark difference between the effect of "Trotterizing" the ansatz in VQE and Trotterizing the time-evolution operator for algorithms like PEA. In

Trotterizing the evolution operator, the goal is to reproduce the dynamics of the original Hamiltonian. Any Trotter error destroys the dynamics, and thus convergence with respect to Trotter error is sought.<sup>25–27</sup> In contrast, when Trotterizing the ansatz in VQE it is generally accepted that the variational optimization can, in practice, absorb most of the energy difference between the conventional UCCSD and the Trotterized form. <sup>12,13,28</sup>

At this point we want to clarify some of the language used above. Despite having used the Suzuki-Trotter approximation as a motivation for separating out the ansatz into a product form, it is no longer appropriate to call this a Trotter approximation. The reason is that the Trotterization occurs before parameter optimization. Thus, one is actually variationally optimizing the parameters of the product form, and it no longer relates to the conventional UCCSD (in ref 29 Evangelista et al. refer to this as the disentangled form of UCCSD, opting to avoid the Trotterization language altogether). In fact, if one were to use the optimized parameters from the product form and insert them into the conventional UCCSD ansatz, the result would necessarily be higher in energy. Therefore, it is important to note that the term "Trotterized form" referred to throughout this Letter is not an approximation to the conventional UCCSD ansatz. It is instead a different ansatz altogether, a point easily made by recognizing that the Trotterized form can sometimes yield a lower energy than the conventional, yet variational, UCCSD.

Unfortunately, a problem of definition arises during Trotterization. Reordering the product approximation in eq 2 does not generally give the same result, except in the trivial case where the operators commute. With the number of operator orderings being a path enumeration problem, the number of possible ansatzes produced during Trotterization (and potentially reported in the literature) is exponentially large. This, of course, is not an issue in UCCSD, as a sum of operators has no dependence on the order in which they are summed.

The objective of this Letter is to determine if the term "Trotterized UCCSD" is sufficiently well-defined, such that the range of energies coming from different operator orderings falls within some notion of chemical accuracy (e.g., 1 kcal/mol), a term referred to in the title as chemically well-defined. If that were the case, then the term "Trotterized UCCSD" would be welldefined, as an arbitrary operator ordering would produce practically similar results. However, if changing the operator ordering significantly changes the accuracy on a chemical scale, then it proves necessary to provide more information to fully define an ansatz and to provide reproducible results. To answer this question, we perform classical simulations with randomly shuffled operators using a custom code built with Open-Fermion<sup>30</sup> and Psi4,<sup>31</sup> which uses the gradient algorithm we developed, which is outlined in the Appendix of ref 8. The results using various operator orderings are compared to both UCCSD and Full CI (FCI).

## NUMERICAL EXAMPLES

We consider four molecules in the context of the UCCSD ansatz, LiH,  $H_6$ , BeH<sub>2</sub>, and  $N_2$  with its 1s and 2s orbitals frozen. All molecules are arranged in uniform, linear geometries with varying interatomic distances. For each system, we classically simulate the calculation of a potential energy curve using a large number of random operator orderings.

For each system, the minimal STO-3G basis is used to minimize computational cost (the implementations use the full

Journal of Chemical Theory and Computation

![](_page_2_Figure_2.jpeg)

Figure 1. Potential energy curves relative to the FCI dissociation limit of each system for, from left to right,  $H_6$ , LiH, BeH<sub>2</sub>, and  $N_2$  (top) and errors from FCI (bottom) for the UCCSD ansatz.

Hilbert space of the orbitals), and the restricted Hartree-Fock (RHF) singlet state is chosen as the reference state. The oneand two-electron integrals are computed with the Psi4 quantum chemical package.<sup>31</sup> The Hamiltonian, anti-Hermitian operators in the UCCSD ansatz, and reference state are formed in the qubit basis using the Jordan-Wigner transform in Open-Fermion.<sup>30</sup> At this point, the various orderings of ansatzes are constructed, and their parameters  $\{\theta_{ia},\theta_{iiab}\}$  are optimized by the SciPy implementation of BFGS. 32 The potential energy curves are displayed in Figure 1 along with standard deviation plots and range plots. We additionally compare the random Trotter orderings to a "sequential gradient ordering" (SGO), a quasideterministic method where one operator with the largest gradient is added at a time, according to the prescription followed by the ADAPT-VQE ansatz construction. However, in contrast to the ADAPT-VQE, the SGO approach refrains from allowing inclusion of more than one instance of the same operator so that a direct comparison to the original UCCSD results can be made.

A cursory evaluation of the data suggests that the variance among different ansatzes increases with static correlation of the chemical system. Because these tend to be the systems of greatest chemical interest for VQE since they represent classically hard problems, the ability to choose good Trotter orderings is critical.

The UCCSD results for the first molecular PES, H<sub>6</sub>, are characterized by an accurate description near the equilibrium region, a quick increase in error upon bond breaking, and then a similarly rapid decrease in error as the bond is further stretched to dissociation. With five "bonds" being broken simultaneously, it is expected that UCCSD should fail to accurately describe this system. One interesting observation from this plot is that the *ordering variance* (the statistical variance of the energies computed with randomly shuffled operators) increases as the UCCSD error increases. In contrast to H<sub>6</sub>, LiH is a relatively simple system, and we observe negligible ordering variance.

Regardless of Trotter ordering, the curves are all extremely good approximations.

Similar to  $H_6$ , Be $H_2$  exhibits a simultaneous quick rise in the ordering variance and UCCSD energy error. However, unlike  $H_6$ , the ordering variance decreases again after bond breaking, along with the UCCSD energy error. The range of values obtained from different orderings is of the same order of magnitude as the actual absolute error of the UCCSD energy.

Unlike both  $H_6$  and  $BeH_2$ , the UCCSD curve for  $N_2$  does not decrease in error after bond breaking but rather flattens out to a nearly constant error of around 10 kcal/mol. The ordering variance increases alongside the UCCSD error and also levels out, despite a significant jump occurring around 3.5 Å in the range of energy values obtained from the Trotterized ansatzes. This is due to at least one of the operator orderings getting stuck in a local minimum (the variational parameters are initialized to 0), which is a consequence of the highly nonlinear nature of the optimization.

Overall, we find that when static correlation appears, the energy differences between orderings increase. This can be understood from the fact that the differences between operator orderings depend on the commutators of the operators, and these in turn depend on the optimal parameter values, which tend to be larger when the electron correlation is stronger. (A system with no electron correlation would have an optimal solution with all parameters equal to zero.) As such it makes sense that for more strongly correlated systems, the differences between operator orderings increase. While uniquely well-defined (up to orderings of operators with degenerate gradients), the sequential gradient ordering scheme does not appear to be reliably better or worse than other orderings.

Alternative Ways To Reorder Operators. In Figure 1, a comparison is made between the un-Trotterized ansatz and a series of randomly shuffled Trotterizations. However, one could group the operators by excitation rank before Trotterization. This would result in a significantly reduced sampling space and

potentially provide more consistently accurate results. To address this possibility, we have computed the performance of multiple different orderings, such as grouping singles first and doubles second or doubles first and singles second. From these results, we find that it is generally favorable to apply double excitations to the reference first, followed by singles. This data is provided in the Supporting Information.

**k-UpCCGSD.** From the results in Figure 1, we notice that the ordering variance increases with error in the associated unTrotterized ansatz. It seems then that when UCCSD is accurate, there may be an excess of operators, such that the extra operators (while not necessary for accurate energy estimates) are useful in minimizing the differences between different Trotterization orderings. To test this hypothesis, we have additionally considered the more compact k-UpCCGSD ansatz by Lee et al., which has far fewer parameters (for small k) than UCCSD, where k controls the number of variational parameters by considering k products of the ansatz with all generalized paired doubles and orbital rotations:

$$|\Psi_{k\text{-UpCCGSD}}\rangle = \prod_{i=1}^{k} \left(e^{\hat{T}^{(i)} - \hat{T}^{(i)\dagger}}\right)|0\rangle \tag{4}$$

The k-UpCCGSD ansatz is a more economical parametrization where only the operators which are expected to be most important are included. This translates into having fewer excess parameters, such that higher accuracy can be reached with a comparable circuit depth by increasing k. Based on our results above, we would anticipate a higher ordering variance for small values of k (larger than UCCSD), but that by increasing k, one can make the energy error (and thus the ordering variance) arbitrarily small. On the other hand, it is worth mentioning that the improvement attained by increasing k is accompanied by placing a heavier burden on the classical optimizer, as it tends to exacerbate the highly nonlinear character of the underlying optimization, making it difficult to locate the global minimum. Moreover, the minima found by the optimizer show strong dependence on the initialization of the variational parameters. One way this can be circumvented in the cases involving the un-Trotterized version of the k-UpCCGSD, as presented in eq 4, is to perform many simulations with the variational parameters  $\theta$ initialized at random, as suggested in ref 15 and carried out here by repeating the simulations at each bond length 100 times and taking the lowest energy value as the global minimum for each geometry. This leads to potential energy curves for k = 1, 2 that are smooth in the energy scale relevant in the current context. The variational parameters are initialized at 0 for all Trotterized ansatzes constructed based on eq 4, in line with what is detailed for the UCCSD ansatz and whose results are displayed in Figure

Figure 2 shows simulation results for  $H_6$  with k=1, 2 for 100 randomly sampled operator groupings. Several features of the performance of the different Trotterized versions of 1- and 2-UpCCGSD agree with the results for the Trotterized versions of the UCCSD ansatz. For short bond distances (<1.1 Å), there is an evident insensitivity of the energy with respect to a specific sampling of the operators. Despite being already fairly small in this regime with k=1, this distinction is largely quenched when k=2, rendering the results with differently sampled ansatzes visually identical on the scale of the plots.

The most remarkable divergences among the operator groupings and the size of the generator, that is, k = 1 vs k = 2, are observed when moving toward the limit of  $H_6$  dissociating

![](_page_3_Figure_8.jpeg)

**Figure 2.** Potential energy curves relative to the FCI dissociation limit of  $H_6$  into six hydrogen atoms (top) and errors from FCI (bottom) for the 1-UpCCGSD (left) and 2-UpCCGSD (right) ansatzes.

into six noninteracting hydrogen atoms. These results are consistent with the observations found in ref 33, which noticed that for k = 1 there were large differences in energy depending on whether one grouped or split the singles and doubles excitations. Ansatzes with different operator groupings start to deviate in the vicinity of the Coulson-Fischer point. In this region, none of the orderings that were sampled for the 1-UpCCGSD operators approach the corresponding un-Trotterized and FCI energies. Some of the ansatzes are able to get back on track in closely approaching the FCI dissociation limit, along with the un-Trotterized 1-UpCCGSD energies. These ansatzes happen to be largely comprised of double excitation operators flocked closer to the reference determinant, which is in line with the findings from the simulations with the SD orderings, provided in the Supporting Information. The 1-UpCCGSD ansatz tracks well the FCI results, being able to provide the correct qualitative behavior along the PES. However, this ansatz is quite compact, and its limited number of parameters impairs its ability to variationally achieve results that are quantitatively comparable to FCI. The operator ordering originated from the SGO construction closely follows the lowest energies from random operator samplings. It is worth pointing out that it is able to overcome the deficiencies around the Coulson-Fischer point and asymptotically recover the exact (FCI) dissociation limit, whereas the corresponding un-Trotterized ansatz cannot account for all the missing correlation as the H-H bonds are stretched. Because in the SGO ansatz the operators are added according to the magnitude of their gradient component, an ansatz with identical operators, such as k-UpCCGSD with k > 1cannot be unambiguously defined and that is why we do not report such results in Figure 2.

The disparities among operator groupings are largely removed all throughout the potential energy curves by doubling the number of variational parameters, accomplished by setting k=2. We preserve the same orderings studied for k=1, that is, we have a product of two Trotterized exponential generators wherein operators are not shuffled across the two instances of  $e^{\hat{T}^{(i)}-\hat{T}^{(i)\dagger}}$ . Except for a slight spread surrounding the Coulson-Fischer point which is the region most strongly correlated in the

potential energy curve, all of the different ansatzes behave in a strikingly similar fashion. The errors are largest in this region, and keeping in mind the different scales in the plots when changing k, they are significantly mitigated in comparison with k=1, with all orderings approaching the FCI energy in the dissociation limit. The advantage due to a larger set of variational parameters is also reflected in the un-Trotterized version of the ansatz, 2-UpCCGSD, whose dissociation curve practically overlays with the FCI results. The significant improvement in the results with k=2, accompanied by a virtually absent spread in the computed energies, is in agreement with the findings of Lee et al., <sup>15</sup> which implies that these ansatzes are relatively insensitive to the ordering of the operators.

## CONCLUSIONS

In this Letter, we sought to determine if the operator ordering in Trotterized UCCSD impacts the results in a "chemically meaningful" way, such that the differences between unique operator orderings produce results which differ on a chemical scale, i.e., greater than 1 kcal/mol. Our numerical simulations clearly demonstrate that the operator ordering has a significant effect (large energy differences between orderings) only when there is a significant amount of electron correlation. However, the renewed interest in UCCSD (and the relevance of the Trotterized form) is due to the use of the UCCSD ansatz in VQE simulations on quantum computers. Strongly correlated molecules are the primary target of quantum simulations, and so this makes the issue of operator ordering even more important. Consequently, the results in this paper emphasize that to ensure scientific reproducibility, it is necessary for authors to report the specific orderings used in simulations involving Trotterized ansatzes. These results strongly advocate for the use of a dynamic ansatz which uniquely determines the operator ordering, such as ADAPT-VQE,8 or adopting an ansatz which does not require trotterization (such as the Jastrow-based approach in ref 33). Our findings also suggest that there are systematic patterns to which Trotter orderings will give the lowest energy, offering a useful route to defining useful and unique operator orderings.

## ASSOCIATED CONTENT

## **S** Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.jctc.9b01083.

Plots for simulations with operators shuffled only within excitation rank sets and details on how to access code used to obtain results (PDF)

Specific operator orderings and corresponding energy values for data used in Figure 2 (XLSX)

#### AUTHOR INFORMATION

#### **Corresponding Author**

\*E-mail: nmayhall@vt.edu.

## ORCID ®

Daniel Claudino: 0000-0002-8860-0689 Nicholas J. Mayhall: 0000-0002-1312-9781

#### Notes

The authors declare no competing financial interest.

### ACKNOWLEDGMENTS

This research was supported by the U.S. Department of Energy (Award No. DE-SC0019199) and the National Science Foundation (Award No. 1839136). S.E.E. also acknowledges support from Award No. DE-SC0019318 from the U.S. Department of Energy.

## REFERENCES

- (1) Aspuru-Guzik, A.; Dutoi, A. D.; Love, P. J.; Head-Gordon, M. Simulated Quantum Computation of Molecular Energies. *Science* **2005**, 309, 1704–1707.
- (2) McArdle, S.; Endo, S.; Aspuru-Guzik, A.; Benjamin, S.; Yuan, X. Quantum computational chemistry. 2018, arXiv:1808.10402. https://arxiv.org/abs/1808.10402 (accessed Dec 17, 2019).
- (3) Cao, Y.; Romero, J.; Olson, J. P.; Degroote, M.; Johnson, P. D.; Kieferová, M.; Kivlichan, I. D.; Menke, T.; Peropadre, B.; Sawaya, N. P. D.; Sim, S.; Veis, L.; Aspuru-Guzik, A. Quantum Chemistry in the Age of Quantum Computing. *Chem. Rev* **2019**, *119*, 10856–10915.
- (4) Preskill, J. Quantum Computing in the NISQ era and beyond. *Quantum* **2018**, 2, 79.
- (5) Kitaev, A. Y. Quantum measurements and the Abelian Stabilizer Problem. 1995. quant-ph/9511026. arXiv e-prints. https://arxiv.org/abs/quant-ph/9511026 (accessed Dec 17, 2019).
- (6) Lloyd, S. Universal Quantum Simulators. Science 1996, 273, 1073-1078.
- (7) Peruzzo, A.; McClean, J.; Shadbolt, P.; Yung, M.-H.; Zhou, X.-Q.; Love, P. J.; Aspuru-Guzik, A.; O'Brien, J. L. A variational eigenvalue solver on a photonic quantum processor. *Nat. Commun.* **2014**, *5*, 4213.
- (8) Grimsley, H. R.; Economou, S. E.; Barnes, E.; Mayhall, N. J. An adaptive variational algorithm for exact molecular simulations on a quantum computer. *Nat. Commun.* **2019**, *10*, 3007.
- (9) McClean, J. R.; Romero, J.; Babbush, R.; Aspuru-Guzik, A. The theory of variational hybrid quantum-classical algorithms. *New J. Phys.* **2016**, *18*, 023023.
- (10) O'Malley, P.; et al. Scalable Quantum Simulation of Molecular Energies. *Phys. Rev. X* **2016**, *6*, 031007.
- (11) McClean, J. R.; Kimchi-Schwartz, M. E.; Carter, J.; de Jong, W. A. Hybrid quantum-classical hierarchy for mitigation of decoherence and determination of excited states. *Phys. Rev. A: At., Mol., Opt. Phys.* **2017**, 95, 042308.
- (12) Barkoutsos, P. K.; Gonthier, J. F.; Sokolov, I.; Moll, N.; Salis, G.; Fuhrer, A.; Ganzhorn, M.; Egger, D. J.; Troyer, M.; Mezzacapo, A.; Filipp, S.; Tavernelli, I. Quantum algorithms for electronic structure calculations: Particle-hole Hamiltonian and optimized wave-function expansions. *Phys. Rev. A: At., Mol., Opt. Phys.* **2018**, *98*, 022322.
- (13) Romero, J.; Babbush, R.; McClean, J. R.; Hempel, C.; Love, P. J.; Aspuru-Guzik, A. Strategies for quantum computing molecular energies using the unitary coupled cluster ansatz. *Quantum Sci. Technol.* **2019**, *4*, 014008.
- (14) Colless, J. I.; Ramasesh, V. V.; Dahlen, D.; Blok, M. S.; Kimchi-Schwartz, M. E.; McClean, J. R.; Carter, J.; de Jong, W. A.; Siddiqi, I. Computation of Molecular Spectra on a Quantum Processor with an Error-Resilient Algorithm. *Phys. Rev. X* **2018**, *8*, 011021.
- (15) Lee, J.; Huggins, W. J.; Head-Gordon, M.; Whaley, K. B. Generalized Unitary Coupled Cluster Wave functions for Quantum Computation. *J. Chem. Theory Comput.* **2019**, *15*, 311–324.
- (16) Kandala, A.; Mezzacapo, A.; Temme, K.; Takita, M.; Brink, M.; Chow, J. M.; Gambetta, J. M. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. *Nature* **2017**, 549, 242–246.
- (17) Shen, Y.; Zhang, X.; Zhang, S.; Zhang, J.-N.; Yung, M.-H.; Kim, K. Quantum implementation of the unitary coupled cluster for simulating molecular electronic structure. *Phys. Rev. A: At., Mol., Opt. Phys.* **2017**, 95, 020501.
- (18) Hempel, C.; Maier, C.; Romero, J.; McClean, J.; Monz, T.; Shen, H.; Jurcevic, P.; Lanyon, B. P.; Love, P.; Babbush, R.; Aspuru-Guzik, A.; Blatt, R.; Roos, C. F. Quantum Chemistry Calculations on a Trapped-Ion Quantum Simulator. *Phys. Rev. X* **2018**, *8*, 031022.

- (19) Bartlett, R. J.; Kucharski, S. A.; Noga, J. Alternative coupled-cluster ansätze II. The unitary coupled-cluster method. *Chem. Phys. Lett.* **1989**, *155*, 133–140.
- (20) Kutzelnigg, W. Error analysis and improvements of coupled-cluster theory. *Theoret. Chim. Acta* **1991**, *80*, 349–386.
- (21) Taube, A. G.; Bartlett, R. J. New perspectives on unitary coupled-cluster theory. *Int. J. Quantum Chem.* **2006**, *106*, 3393–3401.
- (22) Harsha, G.; Shiozaki, T.; Scuseria, G. E. On the difference between variational and unitary coupled cluster theories. *J. Chem. Phys.* **2018**, *148*, 044107.
- (23) Nielsen, M. A.; Chuang, I. L. Quantum Computation and Quantum Information, 10th Anniversary ed.; Cambridge University Press: 2010.
- (24) Hatano, N.; Suzuki, M. Finding Exponential Product Formulas of Higher Orders. In *Quantum Annealing and Other Optimization Methods*; Springer: Berlin, Heidelberg, 2005; pp 37–68, DOI: 10.1007/11526216 2.
- (25) Babbush, R.; McClean, J.; Wecker, D.; Aspuru-Guzik, A.; Wiebe, N. Chemical Basis of Trotter-Suzuki Errors in Quantum Chemistry Simulation. *Phys. Rev. A: At., Mol., Opt. Phys.* **2015**, *91*, 022311.
- (26) Heyl, M.; Hauke, P.; Zoller, P. Quantum Localization Bounds Trotter Errors in Digital Quantum Simulation. *Science Advances* **2019**, 5, No. eaau8342.
- (27) Sieberer, L. M.; Olsacher, T.; Elben, A.; Heyl, M.; Hauke, P.; Haake, F.; Zoller, P. Digital Quantum Simulation, Trotter Errors, and Quantum Chaos of the Kicked Top. *npj Quantum Information* **2019**, *5*, 78.
- (28) Rubin, N. C. A Hybrid Classical/Quantum Approach for Large-Scale Studies of Quantum Systems with Density Matrix Embedding Theory. 2016. arXiv:1610.06910 [cond-mat, physics:quant-ph]. arXiv: 1610.06910. https://arxiv.org/abs/1610.06910 (accessed Dec 17, 2019).
- (29) Evangelista, F. A.; Chan, G. K.-L.; Scuseria, G. E. Exact Parameterization of Fermionic Wave Functions via Unitary Coupled Cluster Theory. 2019. arXiv:1910.10130 [cond-mat, physics:physics, physics:quant-ph]. https://arxiv.org/abs/1910.10130 (accessed Dec 17, 2019).
- (30) McClean, J. R. et al. OpenFermion: The Electronic Structure Package for Quantum Computers. 2017, arXiv:1710.07629 [physics, physics:quant-ph]. arXiv: 1710.07629. https://arxiv.org/abs/1710.07629 (accessed Dec 17, 2019).
- (31) Parrish, R. M.; et al. Psi4 1.1: An Open-Source Electronic Structure Program Emphasizing Automation, Advanced Libraries, and Interoperability. *J. Chem. Theory Comput.* **2017**, *13*, 3185–3197.
- (32) Fletcher, R. Practical Methods of Optimization, 2nd ed.; Wiley-Interscience: New York, NY, USA, 1987; DOI: 10.1002/9781118723203.
- (33) A Jastrow-Type Decomposition in Quantum Chemistry for Low-Depth Quantum Circuits. [1909.12410v1]. https://arxiv.org/abs/1909.12410v1 (accessed Dec 17, 2019).