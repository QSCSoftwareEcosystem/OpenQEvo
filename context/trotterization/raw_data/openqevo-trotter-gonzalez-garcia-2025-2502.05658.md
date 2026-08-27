## Dynamical complexity of non-Gaussian many-body systems with dissipation

Guillermo González-García<sup>1,2</sup>, Alexey V. Gorshkov<sup>3,4</sup>, J. Ignacio Cirac<sup>1,2</sup>, and Rahul Trivedi<sup>1,2\*</sup>

<sup>1</sup>Max-Planck-Institut für Quantenoptik, Hans-Kopfermann-Str. 1, 85748 Garching, Germany

<sup>2</sup>Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, D-80799 Munich, Germany

<sup>3</sup>Joint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA.

<sup>4</sup>Joint Center for Quantum Information and Computer Science,

NIST/University of Maryland, College Park, Maryland 20742, USA.

(Dated: October 21, 2025)

We characterize the dynamical state of many-body bosonic and fermionic many-body models with inter-site Gaussian couplings, on-site non-Gaussian interactions and local dissipation comprising incoherent particle loss, particle gain, and dephasing. We first establish that, for fermionic systems, if the dephasing noise is larger than the non-Gaussian interactions, irrespective of the Gaussian coupling strength, the system state is a convex combination of Gaussian states at all times. Furthermore, for bosonic systems, we show that if the particle loss and particle gain rates are larger than the Gaussian inter-site couplings, the system remains in a separable state at all times. Building on this characterization, we establish that at noise rates above a threshold, there exists a classical algorithm that can efficiently sample from the system state of both the fermionic and bosonic models. Finally, we show that, unlike fermionic systems, bosonic systems can evolve into states that are not convex-Gaussian even when the dissipation is much higher than the on-site non-Gaussianity. Similarly, unlike bosonic systems, fermionic systems can generate entanglement even with noise rates much larger than the inter-site couplings.

*Introduction*. Whether many-body quantum systems evolve into classically non-trivial states under decoherence is of fundamental interest to the theory of open quantum systems and also has implications for the quantum advantage in quantum computers and simulators [1– 6. Traditionally, this has been mostly studied for manybody spin models, including extensive recent activity in both the discrete-time setting (i.e. quantum circuits interspersed with noise) and in the continuous-time setting (modeled by a many-body Lindblad master equation [7, 8]). For discrete-time models, early results showed that sufficiently high noise suppresses entanglement thus enabling classical simulation [9]. Recent results have shown classical simulability, even with a small amount of depolarizing noise, for both sampling or computing local observables in both random [10–19] and structured models [20–22]. These results have partly been generalized to the geometrically-local continuous-time setting, which more accurately models analog quantum simulators, to show that the system remains classically simulable when the noise rate is larger than the interaction terms in the Hamiltonian [8].

Quantum simulators based on platforms such as ultracold atoms in optical lattices [23–27], superconducting circuits [28, 29] or nonlinear photonics [30–32], are often described by a family of Hamiltonians that, only in certain regimes, reduce to spin systems. They are modeled by a fermionic or bosonic lattice with two kinds of terms: (i) Gaussian coupling terms which are linear or quadratic in creation/annihilation operators (e.g. particle hopping or pair production); (ii) Non-Gaussian interaction terms that typically act on particles only on one site. Consequently, there are two relevant frequency scales: the strength of the Gaussian couplings, J, and that of the onsite (non-Gaussian) interactions, U. If J=0 or U=0, this model is classically simulable. When J=0, the Hamiltonian is a sum of single-site terms which maps product states to product states which can be classically simulated. When U=0, the dynamics is Gaussian and thus local observables can be efficiently computed and, for fermions, even sampling is efficient [33–36]. However, when both  $J,U\neq 0$  and the system is noiseless, this model is universal for quantum computation [37, 38] and thus worst-case hard to simulate classically. While the presence of dissipation should make the model classically simulable, the amount and type of local dissipation needed remains unclear.

For fermionic systems, the impact of noise on non-Gaussianity was studied in a circuit model with Gaussian gates and non-Gaussian ancillas, which showed that the state remains a convex combination of Gaussian states above a noise-threshold[39–41]. Studies analyzing continuous-time dynamics have focused on the non-Gaussianity introduced via two-body dissipation [7]. For bosonic systems, previous studies have either focused on understanding their complexity as a function of evolution time in the absence of noise [42–44], or for the specific task of boson sampling in the presence of noise [45–49]. However, the classical simulability of the noisy continuous-time model motivated above remains unresolved.

In this Letter, we rigorously address this question—we consider fermionic and bosonic systems with n sites, each containing locally L modes (Fig. 1). The annihilation operators corresponding to the  $\sigma^{\text{th}}$  mode at the  $i^{\text{th}}$  site, where  $\sigma \in \{1, 2 ... L\}$  and  $i \in \{1, 2 ... n\}$ , is given by  $a_{i,\sigma}$ . We will use the Hermitian operators  $c_{i,\sigma}^{\alpha}$ ,

<sup>\*</sup> rahul.trivedi@mpq.mpg.de

with  $\alpha \in \{1, 2\}$ , defined as  $c_{i,\sigma}^1 = (a_{i,\sigma} + a_{i,\sigma}^{\dagger})/\sqrt{2}$ ,  $c_{i,\sigma}^2 = -i(a_{i,\sigma} - a_{i,\sigma}^{\dagger})/\sqrt{2}$ , which represent either Majorana operators (for fermions) or position and momentum quadrature operators (for bosons). The noisy dynamics is described by the Lindblad master equation

$$\frac{d\rho(t)}{dt} = -i[H(t), \rho(t)] + \sum_{i,\sigma} \mathcal{L}_{i,\sigma}\rho(t), \tag{1}$$

were H(t) is a (possibly time-dependent) Hamiltonian describing the system.  $\mathcal{L}_{i,\sigma}$  captures the noise, which is assumed to act locally on every mode  $(i,\sigma)$ , and is modeled by

$$\mathcal{L}_{i,\sigma}(\cdot) = \sum_{l=1}^{3} \kappa_{l} \left( L_{i,\sigma}^{(l)}(\cdot) L_{i,\sigma}^{(l)\dagger} - \frac{1}{2} \{ L_{i,\sigma}^{(l)\dagger} L_{i,\sigma}^{(l)}, (\cdot) \} \right), \quad (2)$$

with jump operators  $L_{i,\sigma}^{(1)}=a_{i,\sigma}, L_{i,\sigma}^{(2)}=a_{i,\sigma}^{\dagger}, L_{i,\sigma}^{(3)}=a_{i,\sigma}^{\dagger}a_{i,\sigma}$  and decay rates  $\kappa_1,\kappa_2,\kappa_3$  respectively. The jump operator  $a_{i,\sigma}$  models particle loss,  $a_{i,\sigma}^{\dagger}$  models incoherent particle gain, and  $a_{i,\sigma}^{\dagger}a_{i,\sigma}$  models dephasing. We remark that our conclusions also hold for other physically relevant dissipators such as  $L_{i,\sigma}^{(1)}=c_{i,\sigma}^1, L_{i,\sigma}^{(2)}=c_{i,\sigma}^2$  which, in the bosonic case, would correspond to white noise fluctuations in the quadratures. We use the same noise Lindbladian for both bosons and fermions—for the bosonic case, we will additionally assume that the particle loss occurs at a rate strictly higher than (both coherent and incoherent) particle gain (see Supplement [50] for the exact assumption) so as to avoid an unbounded growth of the number of particles with t which would be unphysical in an actual experiment.

We will assume that the Hamiltonian can be written as  $H(t) = H_{\rm g}(t) + H_{\rm ng}(t)$ , where  $H_{\rm g}(t)$  contains Gaussian general intersite terms:

$$H_{g}(t) = \sum_{i,j} \sum_{\substack{\alpha,\alpha'\\\sigma,\sigma'}} J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t) c_{i,\sigma}^{\alpha} c_{j,\sigma'}^{\alpha'} + \sum_{i,\alpha,\sigma} \Omega_{i;\sigma}^{\alpha}(t) c_{i,\sigma}^{\alpha},$$
(3a)

and  $H_{ng}(t)$  contains on-site non-Gaussian terms which account for particle-particle repulsion and attraction between different modes at the same site:

$$H_{\rm ng}(t) = \sum_{i,\sigma,\sigma'} U_{i,\sigma;i,\sigma'}(t) n_{i,\sigma} n_{i,\sigma'}.$$
 (3b)

Note that in the fermionic case  $\Omega_{i;\sigma}^{\alpha}(t) = 0$ , since physical Hamiltonians must preserve fermionic parity, while in the bosonic case  $\Omega_{i;\sigma}^{\alpha}(t)$  can be a non-zero real scalar. For fermions, we can assume that  $J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t)$  is purely imaginary and anti-symmetric i.e.

$$J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t) = \left(J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t)\right)^* = -J_{j,\sigma';i,\sigma}^{\alpha',\alpha}(t),\tag{4}$$

![](_page_1_Figure_12.jpeg)

FIG. 1. Sketch of the model, with n sites on a lattice, where each site contains L modes. There are Gaussian couplings between the different sites, while the non-Gaussian interactions are only onsite. Nonlocal couplings are allowed. In the bosonic case, interactions of the form  $n_{i,\sigma}^2$  are also allowed.

while for bosons it can be assumed to be purely real and symmetric:

$$J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t) = J_{j,\sigma';i,\sigma}^{\alpha',\alpha}(t). \tag{5}$$

The non-Gaussian onsite interactions  $U_{i,\sigma;i,\sigma'}(t)$  can be assumed to be real and symmetric for both fermions and bosons.

We also define the parameters  $J, \Omega, U$  as the smallest constants such that for every mode  $(i, \sigma)$  and all times t

$$\sum_{j \neq i, \sigma'} \sum_{\alpha, \alpha'} |J_{i, \sigma; j, \sigma'}^{\alpha, \alpha'}(t)| \leq J, \sum_{\alpha} |\Omega_{i, \sigma}^{\alpha}(t)| \leq \Omega \text{ and}$$

$$\sum_{\sigma'} |U_{i, \sigma; i, \sigma'}(t)| \leq U. \tag{6}$$

The parameter J captures the Gaussian coupling strength between a mode and the modes at all other sites, U captures the on-site non-Gaussian interaction strength, and  $\Omega$  captures the coherent drive at each site. We will also assume that J, U, and  $\Omega$  are O(1) constants, which is true in most physical models. Finally, we remark that we do not need to assume geometrical locality of the model—our results will apply to geometrically local and non-local models.

The initial state  $\rho(0)$  is either a product state (when analyzing entanglement), a Gaussian state (when analyzing non-Gaussianity), or both (e.g., the vacuum state). In the bosonic case, additionally,  $\rho(0)$  will be assumed to satisfy  $\text{Tr}(n_{i,\sigma}^k\rho(0)) \leq C_0^k k^{\alpha_0 k + \beta_0}, \forall (i,\sigma)$ , for  $k \in \{1,2...\}$ , and for some  $C_0,\alpha_0,\beta_0>0$ : this condition guarantees that the probability of finding  $\geq k$  particles in a mode decreases super-polynomially with k, as would be expected in a physically preparable bosonic state [51].

Results: Our results, depicted in Fig. 2, show the simulability of the fermionic and bosonic models as a function of  $J, U, \kappa_i$ . We first establish that when the noise rate is larger than the on-site non-Gaussian interaction strength

![](_page_2_Figure_1.jpeg)

FIG. 2. Phase diagram for both bosonic and fermionic systems in the presence of generic noise. (a) For fermionic system the state remains convex-Gaussian at all times for error rates  $\kappa_3 \geq 2U$ . (b) In bosonic systems the state remains separable at all times for error rates  $\kappa_1, \kappa_2 \geq 2J$ .

U, the fermionic model remains convex-Gaussian at all times, and can therefore be classically efficiently sampled from

**Theorem 1.** For an initial Gaussian state, if  $\kappa_3 \geq 2U$ , then the state of the fermionic model at time t,  $\rho(t)$ , is a convex combination of Gaussian states for all  $t \geq 0$ . Furthermore,  $\rho(t)$  can be classically sampled in the Fock state basis to an  $\epsilon$  total variation error in  $\operatorname{poly}(n,t,1/\epsilon)$  time.

Physically Theorem 1 suggests that when  $\kappa_3 \geq 2U$ , dephasing noise destroys non-Gaussianity faster than  $H_{\rm ng}(t)$  creates it, so that  $\rho(t)$  always remains convex-Gaussian. Since  $H_{\rm g}(t)$  preserves convex-Gaussianity, the noise threshold in Theorem 1 is independent of J. Notably, it is dephasing that results in this convex-Gaussianity. With only incoherent particle loss/gain,  $\rho(t)$  could evolve into a non-Gaussian state at short times even with large dissipation. This arises from the fermionic parity structure—the density matrix of the fermionic model has the form  $\rho(t) = \rho_{+}(t) + \rho_{-}(t)$ , where  $\rho_{+}(t)$  is supported only on even/odd parity states. Due to this structure, convex-Gaussianity in  $\rho(t)$  requires both  $\rho_{\pm}(t)$  to be convex-Gaussian [40].  $H_{\rm ng}(t)$  generates non-Gaussianity individually in both  $\rho_{\pm}(t)$ . However, the loss/gain dissipators, to first order, switch the parity of the state and do not act within the two parity subspaces. Consequently, they cannot immediately counter the non-convex-Gaussianity created by  $H_{ng}(t)$ .

We provide a complete proof of Theorem 1 in the supplement: The starting point is a Trotterization of the Lindbladian in Eq. 1 — in each Trotter step, we express the evolution as (a) a Gaussian unitary corresponding to  $H_{\rm g}(t)$ , particle loss and gain followed by (b) the single-site channels generated by  $H_{\rm ng}(t)$  and dephasing (Fig. 3). Analyzing the single-site channel, we show that for  $\kappa_3 \geq 2U$ , this channel maps an input convex-Gaussian state to a convex-Gaussian state. Furthermore, we explicitly construct the output convex-Gaussian state, which allows us to sample from it [35, 52].

Next, we consider the bosonic model and establish that when the noise rate is larger than the inter-site Gaussian coupling,  $\rho(t)$  remains separable at all times, and can therefore be classically efficiently sampled from in the Fock state basis.

**Theorem 2.** Suppose  $\rho(t)$  is the state obtained after evolving the bosonic model for time t with an initial product state, then for  $\kappa_1, \kappa_2 \geq 2J$  the state  $\rho(t)$  is separable for all  $t \geq 0$ . Furthermore, there is a randomized classical algorithm that can sample  $\rho(t)$  in the Fock state basis to  $\epsilon$  total variation error in poly $(n, t, 1/\epsilon)$  time.

Our result formalizes the intuition that, when noise exceeds the inter-site coupling strength, a buildup of entanglement is prohibited and no classically non-trivial state is generated. Notably, the noise threshold is determined by particle loss and gain noise. This arises from the dephasing dissipator being diagonal in the Fock basis, while evolution under  $H_q(t)$  creates entanglement through off-diagonal elements (i.e., coherences). Thus, to first order, dephasing cannot counter this entanglement generation. Particle gain or loss dissipators, however, are not diagonal in the Fock basis and can prevent it. In the Supplement, we also extend Theorem 2 to quantum spin models with single spin noise and bosonic models with inter-site non-Gaussian couplings [50]. Unlike previous percolation-based arguments limiting entanglement to  $O(\log n)$  qubit clusters for sufficiently strong noise [8, 9], we show that the state is entirely separable, and provide an explicit construction that can be efficiently sampled from.

A detailed proof of Theorem 2 is provided in the Supplement [50]. Similar to Theorem 1, we begin by a firstorder Trotterization of the model but with a different decomposition of the Lindbladian: We express it as a product of (a) single site gates, which contain the unitary generated by  $H_{ng}(t)$ , single-site terms in  $H_{g}(t)$  and the dephasing dissipator and (b) two-site channels which contain the unitary generated by the inter-site terms in  $H_{\rm g}(t)$ paired together with the particle gain and loss dissipators [Fig. 4]. We denote the channel acting between modes  $(i,\sigma)$  and  $(j,\sigma')$  at the Trotter-step  $\tau$  as  $\Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$ , where  $\delta$  is the size of the Trotter-step. Importantly, the Trotterization is performed in such a way that the channel  $\Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$  can be understood as a time evolution of the inter-site Gaussian couplings between modes  $(i, \sigma)$  and  $(j, \sigma')$ , followed by noise on both modes. This effectively redistributes the single-site noise into "gate-based" noise on the inter-site gates. Analyzing  $\Phi^{i,\sigma;j,\sigma'}_{\tau\delta,(\tau-1)\delta}$ , we show that for  $\kappa_1, \kappa_2 \geq 2J$ , it is separability-preserving and thus the state remains separable at all times. Furthermore, we also explicitly construct an  $O(\delta^2)$  approximation to the separable state after each time-step and obtain an explicit algorithm to sample from  $\rho(t)$ .

Tightness of Theorems 1 and 2. We can now ask if a version of Theorem 1 holds for bosonic systems i.e., is there a noise threshold  $\kappa_{\text{th}}(U)$  dependent only on the non-Gaussian strength U and uniform in  $J, \Omega$  that guarantees a convex-Gaussian at all times? For dephasing

![](_page_3_Figure_1.jpeg)

FIG. 3. Schematic depiction of the Trotterization schemes in the proof of Theorem 1 (fermionic systems with weak non-Gaussianity). For simplicity, we only depict a 1D setting, with each site containing 3 modes (L=3). A single Trotter step consists of a Gaussian channel (orange rectangles) that includes the combined effect of  $H_g(t)$  and the particle gain and loss dissipators, followed by non-Gaussian gates (blue rectangles) interspersed with the dephasing dissipator (gray curved rectangles). Crucially, a non-Gaussian gate followed by sufficiently strong dephasing can be written as a convex combination of Gaussian channels.

![](_page_3_Picture_3.jpeg)

FIG. 4. Schematic depiction of the Trotterization schemes in the proof of Theorem 2 (bosonic systems with weak inter-site couplings). For simplicity, we only depict a 1D setting, with each site containing 3 modes (L=3). A single Trotter step consists of a layer of single-site channels which include the Hamiltonian terms acting on that site and the dephasing dissipator, followed by 2-site gates interspersed with particle gain and loss dissipators (in gray circles). Crucially, a 2-site gate followed by sufficiently strong noise can be written as a convex combination of single-site channels

noise, we provide numerical evidence to the contrary: even for  $\kappa_3 \gg U$ , single-mode dynamics can yield states with negative Wigner function, and thus not convex-Gaussian states can be generated at time-scales  $\sim 1/U$  [50, 53]. While negativity of the Wigner function suggests classical simulation hardness [53, 54], we do not rule out the existence of an efficient classical algorithm. When  $\kappa_3 = 0$ , in the Supplement we show that no matter how small U is relative to  $\kappa_1, \kappa_2$ , computing expected local particle numbers is BQP-hard if  $J, \Omega$  can be arbitrarily large but O(1) [50]. This builds upon Refs. [55, 56] which perform a universal gate-set on a single bosonic

mode with an arbitrarily small effective gate-error rate by engineering the displacement and squeezing. We extend this technique to also implement an entangling gate between two oscillators thus yielding a high-fidelity universal multi-mode gate-set. Together with results from Ref. [57], this suggests that when the noise is non-unital (i.e.  $\kappa_1 \neq \kappa_2$ ), by using sufficiently large J and  $\Omega$ , a fault-tolerant quantum computation can be encoded into the model [58–60]. Thus, it is unlikely to be able to classically compute even local observables in this setting unless BQP = BPP.

Finally, we consider if a version of Theorem 2 holds

for fermions i.e., do noise rates larger than the Gaussian inter-site couplings result in separability at all times. We answer this question in the negative: in the Supplement we show by analyzing few-mode fermionic models that, in contrast with bosons, no matter how high  $\kappa_2, \kappa_3$  are, the system does not remain separable at all times and can exhibit entanglement at time-scales  $\sim \min(\kappa_2^{-1}, \kappa_3^{-1})$ . In fact, this short-time non-separability holds not only if we consider separability with respect to all observables [61], but also if we consider a weaker notion of separability with respect to only parity-conserving observables [62]. However, this result does not rule out separability at longer times or other routes to classical simulation.

Conclusion and outlook. We have characterized the classical complexity of simulating the continuous-time evolution of fermionic and bosonic systems as a function of the noise, Gaussian and non-Gaussian interaction strengths. Future theoretical directions include the study extending our results to non-Markovian models of dissipation.

The models considered in this paper can be experimentally realised in several platforms. The bosonic model can be implemented in superconducting systems where the Gaussian Hamiltonian can be controlled by designing capacitive couplings between different qubits and the single-site non-Gaussianity by the nonlinear Josephson potential in the qubit [28, 29]. We can also use cold bosonic atoms in optical lattices where the strength of both the Gaussian and the non-Gaussian Hamiltonians can be controlled by tuning the optical lattice potential [26, 27]. The fermionic model can be implemented either with cold atoms in optical lattices by using a fermionic species of atoms [23–25], or in solid-state systems such Moiré superlattices hosting trions [63–65]. Since all of these systems will have intrinsic particle loss, gain, and dephasing, tuning the parameters in the Gaussian and non-Gaussian Hamiltonians could allow us to access the parameter regimes in Theorems 1 and 2. A major challenge in experimentally verifying the threshold behavior predicted by Theorems 1 and 2 would be verifying the presence (or absence) of entanglement/non-Gaussianity in  $\rho(t)$ . While this could be hard to do for large systems, we remark that the difference in the threshold behavior in fermionic and bosonic models that we described can be understood even with systems with few ( $\leq$  4) fermionic or bosonic modes, which is well within the regime where a full state tomography can already be performed.

#### ACKNOWLEDGMENTS

We thank Ashish Clerk and Liang Jiang for useful discussions and Peter McMahon for discussions that inspired this project. R.T acknowledges support from Center for Integration of Modern Optoelectronic Materials on Demand (IMOD) seed grant (DMR-2019444). This research was supported in part by grant NSF PHY-2309135 to the Kavli Institute for Theoretical Physics (KITP). The research is part of the Munich Quantum Valley, which is supported by the Bavarian State Government with funds from the High tech Agenda Bayern Plus. J.I.C, R.T, G.G.G acknowledge funding from the project FermiQP of the Bildungsministerium für Bildung und Forschung (BMBF). A.V.G. acknowledges support from the U.S. Department of Energy, Office of Science, Accelerated Research in Quantum Computing, Fundamental Algorithmic Research toward Quantum Utility (FAR-Qu). A.V.G. was also supported in part by NSF QLCI (award No. OMA-2120757), DoE ASCR Quantum Testbed Pathfinder program (awards No. DE-SC0019040 and No. DE-SC0024220), NSF STAQ program, AFOSR MURI, DARPA SAVANT ADVENT, and NQVL:QSTD:Pilot:FTL. A.V.G. also acknowledges support from the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Quantum Systems Accelerator.

<sup>[1]</sup> J. Preskill, Quantum 2, 79 (2018).

<sup>[2]</sup> A. J. Daley, I. Bloch, C. Kokail, S. Flannigan, N. Pearson, M. Troyer, and P. Zoller, Nature 607, 667 (2022).

<sup>[3]</sup> S. Ebadi, T. T. Wang, H. Levine, A. Keesling, G. Semeghini, A. Omran, D. Bluvstein, R. Samajdar, H. Pichler, W. W. Ho, et al., Nature 595, 227 (2021).

<sup>[4]</sup> P. Scholl, M. Schuler, H. J. Williams, A. A. Eberharter, D. Barredo, K.-N. Schymik, V. Lienhard, L.-P. Henry, T. C. Lang, T. Lahaye, et al., Nature 595, 233 (2021).

<sup>[5]</sup> D. Wei, A. Rubio-Abadal, B. Ye, F. Machado, J. Kemp, K. Srakaew, S. Hollerith, J. Rui, S. Gopalakrishnan, N. Y. Yao, I. Bloch, and J. Zeiher, Science 376, 716 (2022).

<sup>[6]</sup> G. Semeghini, H. Levine, A. Keesling, S. Ebadi, T. T. Wang, D. Bluvstein, R. Verresen, H. Pichler, M. Kalinowski, R. Samajdar, A. Omran, S. Sachdev, A. Vishwanath, M. Greiner, V. Vuletić, and M. D. Lukin, Science 374, 1242 (2021).

<sup>[7]</sup> O. Shtanko, A. Deshpande, P. S. Julienne, and A. V. Gorshkov, PRX Quantum 2, 030350 (2021).

<sup>[8]</sup> R. Trivedi and J. I. Cirac, Phys. Rev. Lett. 129, 260405 (2022).

<sup>[9]</sup> D. Aharonov, Phys. Rev. A **62**, 062311 (2000).

<sup>[10]</sup> D. Aharonov, X. Gao, Z. Landau, Y. Liu, and U. Vazirani, in *Proceedings of the 55th Annual ACM Symposium on Theory of Computing*, STOC '23 (ACM, 2023).

<sup>[11]</sup> J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels, arXiv preprint arXiv:2306.14887 (2023).

<sup>[12]</sup> K. Kechedzhi, S. Isakov, S. Mandrà, B. Villalonga, X. Mi, S. Boixo, and V. Smelyanskiy, Future Gener. Comput. Syst. 153, 431 (2024).

<sup>[13]</sup> Y. Shao, F. Wei, S. Cheng, and Z. Liu, Phys. Rev. Lett. 133, 120603 (2024).

<sup>[14]</sup> E. Fontana, M. S. Rudolph, R. Duncan, I. Rungger, and C. Cîrstoiu, arXiv preprint arXiv:2306.05400 (2023).

<sup>[15]</sup> M. S. Rudolph, E. Fontana, Z. Holmes, and L. Cincio,

- arXiv preprint arXiv:2308.09109 (2023).
- [16] X. Gao and L. Duan, arXiv preprint arXiv:1810.03176 (2018).
- [17] H.-J. Liao, K. Wang, Z.-S. Zhou, P. Zhang, and T. Xiang, arXiv preprint arXiv:2308.03082 (2023).
- [18] G. González-García, R. Trivedi, and J. I. Cirac, PRX Quantum 3, 040326 (2022).
- [19] T. Schuster, C. Yin, X. Gao, and N. Y. Yao, arXiv preprint arXiv:2407.12768 (2024).
- [20] G. González-García, J. I. Cirac, and R. Trivedi, arXiv preprint arXiv:2407.16068 (2024).
- [21] J. Rajakumar, J. D. Watson, and Y.-K. Liu, in Proceedings of the 2025 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) (SIAM, 2025) pp. 1037–1056.
- [22] S. D. Mishra, M. Frías-Pérez, and R. Trivedi, PRX Quantum 5, 020317 (2024).
- [23] Z. Z. Yan, B. M. Spar, M. L. Prichard, S. Chi, H.-T. Wei, E. Ibarra-García-Padilla, K. R. A. Hazzard, and W. S. Bakr, Phys. Rev. Lett. 129, 123201 (2022).
- [24] B. M. Spar, E. Guardado-Sanchez, S. Chi, Z. Z. Yan, and W. S. Bakr, Phys. Rev. Lett. 128, 223202 (2022).
- [25] M. A. Norcia, A. W. Young, and A. M. Kaufman, Phys. Rev. X 8, 041054 (2018).
- [26] C. Gross and I. Bloch, Science 357, 995 (2017).
- [27] B. Yang, H. Sun, R. Ott, H.-Y. Wang, T. V. Zache, J. C. Halimeh, Z.-S. Yuan, P. Hauke, and J.-W. Pan, Nature 587, 392 (2020).
- [28] X. Zhang, E. Kim, D. K. Mark, S. Choi, and O. Painter, Science 379, 278 (2023).
- [29] Y.-H. Shi, Z.-H. Sun, Y.-Y. Wang, Z.-A. Wang, Y.-R. Zhang, W.-G. Ma, H.-T. Liu, K. Zhao, J.-C. Song, G.-H. Liang, et al., Nat. Commun. 15, 7573 (2024).
- [30] A. Saxena, A. Manna, R. Trivedi, and A. Majumdar, Nat. Commun. 14, 5260 (2023).
- [31] D. E. Chang, V. Vuletić, and M. D. Lukin, Nat. Photonics 8, 685 (2014).
- [32] C. Noh and D. G. Angelakis, Rep. Prog. Phys. 80, 016401 (2016).
- [33] S. Bravyi and R. König, Quantum Info. Comput. 12, 925–943 (2012).
- [34] S. D. Bartlett, B. C. Sanders, S. L. Braunstein, and K. Nemoto, Phys. Rev. Lett. 88, 097904 (2002).
- [35] B. M. Terhal and D. P. DiVincenzo, Phys. Rev. A 65, 032325 (2002).
- [36] L. G. Valiant, in Proceedings of the thirty-third annual ACM symposium on Theory of computing (2001) pp. 114–123.
- [37] S. B. Bravyi and A. Y. Kitaev, Ann. Phys. 298, 210 (2002).
- [38] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82, 1784 (1999).
- [39] F. de Melo, P. Ćwikliński, and B. M. Terhal, New. J. Phys. 15, 013015 (2013).
- [40] M. Oszmaniec, J. Gutt, and M. Kuś, Phys. Rev. A 90, 020302 (2014).
- [41] S. Bravyi, Phys. Rev. A 73, 042313 (2006).
- [42] N. Maskara, A. Deshpande, A. Ehrenberg, M. C. Tran, B. Fefferman, and A. V. Gorshkov, Phys. Rev. Lett. 129, 150604 (2022).
- [43] A. Deshpande, B. Fefferman, M. C. Tran, M. Foss-Feig, and A. V. Gorshkov, Phys. Rev. Lett. 121, 030501 (2018).
- [44] G. Muraleedharan, A. Miyake, and I. H. Deutsch, New.

- J. of Phys. 21, 055003 (2019).
- [45] C. Oh, L. Jiang, and B. Fefferman, arXiv preprint arXiv:2301.11532 (2023).
- [46] H. Qi, D. J. Brod, N. Quesada, and R. García-Patrón, Phys. Rev. Lett. 124, 100502 (2020).
- [47] V. Shchesnovich, Quantum 5, 423 (2021).
- [48] H.-S. Zhong, H. Wang, Y.-H. Deng, M.-C. Chen, L.-C. Peng, Y.-H. Luo, J. Qin, D. Wu, X. Ding, Y. Hu, P. Hu, X.-Y. Yang, W.-J. Zhang, H. Li, Y. Li, X. Jiang, L. Gan, G. Yang, L. You, Z. Wang, L. Li, N.-L. Liu, C.-Y. Lu, and J.-W. Pan, Science 370, 1460 (2020).
- [49] L. S. Madsen, F. Laudenbach, M. F. Askarani, F. Rortais, T. Vincent, J. F. Bulmer, F. M. Miatto, L. Neuhaus, L. G. Helt, M. J. Collins, et al., Nature 606, 75 (2022).
- [50] See supplemental material for a detailed proof of the theorems, which includes Refs. [66-76].
- [51] T. Kuwahara, T. V. Vu, and K. Saito, Nat. Commun. 15, 2520 (2024).
- [52] E. Knill, arXiv preprint quant-ph/0108033 (2001).
- [53] A. Mari and J. Eisert, Phys. Rev. Lett. 109, 230503 (2012).
- [54] C. Cormick, E. F. Galvão, D. Gottesman, J. P. Paz, and A. O. Pittenger, Phys. Rev. A 73, 012301 (2006).
- [55] M. Yuan, A. Seif, A. Lingenfelter, D. I. Schuster, A. A. Clerk, and L. Jiang, arXiv preprint arXiv:2312.15783 (2023).
- [56] A. Eickbusch, V. Sivak, A. Z. Ding, S. S. Elder, S. R. Jha, J. Venkatraman, B. Royer, S. M. Girvin, R. J. Schoelkopf, and M. H. Devoret, Nat. Phys. 18, 1464 (2022).
- [57] M. Ben-Or, D. Gottesman, and A. Hassidim, arXiv preprint arXiv:1301.1995 (2013).
- [58] K. Noh and C. Chamberland, Phys. Rev. A 101, 012316 (2020).
- [59] T. Matsuura, N. C. Menicucci, and H. Yamasaki, arXiv preprint arXiv:2410.12365 (2024).
- [60] D. Aharonov and M. Ben-Or, SIAM J. Comput. 38, 1207 (2008).
- [61] H. Moriya, J. Phys. A-Math. Gen. 39, 3753 (2006).
- [62] M.-C. Bañuls, J. I. Cirac, and M. M. Wolf, Phys. Rev. A 76, 022311 (2007).
- [63] E. Liu, E. Barré, J. van Baren, M. Wilson, T. Taniguchi, K. Watanabe, Y.-T. Cui, N. M. Gabor, T. F. Heinz, Y.-C. Chang, et al., Nature 594, 46 (2021).
- [64] X. Wang, J. Zhu, K. L. Seyler, P. Rivera, H. Zheng, Y. Wang, M. He, T. Taniguchi, K. Watanabe, J. Yan, et al., Nature Nanotechnology 16, 1208 (2021).
- [65] H. Baek, M. Brotons-Gisbert, A. Campbell, V. Vitale, J. Lischner, K. Watanabe, T. Taniguchi, and B. D. Gerardot, Nature Nanotechnology 16, 1237 (2021).
- [66] C. V. Kraus, A quantum information perspective of fermionic quantum many-body systems, Ph.D. thesis, Technische Universität München (2009).
- [67] J. Surace and L. Tagliacozzo, SciPost Phys. Lect. Notes , 54 (2022).
- [68] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, *Introduction to algorithms* (MIT press, 2022).
- [69] M. Fagotti and P. Calabrese, J. Stat. Mech.-Theory E. 2010, P04016 (2010).
- [70] R. Hudson, Rep. Math. Phys 6, 249 (1974).
- [71] M. Walschaers, PRX Quantum 2, 030204 (2021).
- [72] A. Lingenfelter, D. Roberts, and A. A. Clerk, Sci. Adv. 7, eabj1916 (2021).
- [73] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and R. Vrijen, Proceedings of the National Academy of Sci-

- ences 99, 3388 (2002).
- [74] L. J. Schulman and U. V. Vazirani, in Proceedings of the Thirty-First Annual ACM Symposium on Theory of Computing, STOC '99 (Association for Computing Machinery, New York, NY, USA, 1999) p. 322–329.
- [75] Á. M. Alhambra, M. Lostaglio, and C. Perry, Quantum 3, 188 (2019).
- [76] O. Shtanko and K. Sharma, arXiv preprint arXiv:2411.04819 (2024).
- [77] https://github.com/guillegg10/Separability\_ Wigner-negativity, GitHub repository.

# Supplemental material to "Dynamical complexity of non-Gaussian many-body systems with dissipation"

Guillermo González-García<sup>1,2</sup>, Alexey V. Gorshkov<sup>3,4</sup>, J. Ignacio Cirac<sup>1,2</sup>, and Rahul Trivedi<sup>1,2\*</sup>

<sup>1</sup>Max-Planck-Institut für Quantenoptik, Hans-Kopfermann-Str. 1, 85748 Garching, Germany

<sup>2</sup>Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, D-80799 Munich, Germany

<sup>3</sup>Joint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA.

<sup>4</sup>Joint Center for Quantum Information and Computer Science,

NIST/University of Maryland, College Park, Maryland 20742, USA.

(Dated: October 21, 2025)

This Supplemental Material is organized as follows: First, in section I, we provide the necessary notation and background for the rest of the Supplemental Material. In section II, we provide the proof of Theorem 1, showing convex-Gaussianity and simulability for the fermionic model for sufficiently high noise rates. Then, in section III, we prove Theorem 2 for the bosonic model, which implies separability and simulability for sufficiently high noise rates. In section IV, we extend this result to a class of spin models: for 2-local Hamiltonians and sufficiently high noise rates, the system can be shown to be separable at all times. Finally, in section V, we show that an analogue of Theorem 1 cannot exist for bosonic systems, and that an analogue of Theorem 2 cannot exist for fermionic systems.

## I. NOTATION AND PRELIMINARIES

In this section, we provide the necessary notation and background for the rest of the Supplemental Material. This includes the notation regarding operators and norms (subsection IA), a brief summary on several properties of bosonic and fermionic systems (subsection IB), the Trotter formula that will be used throughout the proofs (subsection IC), the asymptotic notation that we will employ (subsection ID), and a detailed presentation of the bosonic and fermionic models that we will analyze (subsection IE).

## A. Operators, superoperators and their norms

For a quantum state  $|\psi\rangle$ ,  $||\psi\rangle||$  will denote its usual norm  $||\psi\rangle||^2 = \langle\psi|\psi\rangle$ . For an operator A, we will use  $||A||_p$  to denote its Schatten-p norm:

$$||A||_p = \left(\sum_i \sigma_i^p(A)\right)^{1/p}$$
, where  $\sigma_1(A) \ge \sigma_2(A) \ge \sigma_3(A) \dots$  are the singular values of  $A$ . (S1)

We will often use  $||A|| = \sigma_1(A) = ||A||_{\infty}$  to denote its operator norm and  $||A||_F = ||A||_2 = [\text{Tr}(A^{\dagger}A)]^{1/2}$  to denote its Frobenius norm. We will often use the Holder's inequality, which states that

$$||AB||_1 \le ||A||_p ||B||_q \text{ where } \frac{1}{p} + \frac{1}{q} = 1.$$
 (S2)

In particular,  $||AB||_1 \le ||A|| ||B||_1$ . It is also convenient to note the Cauchy-Schwarz inequality for operators: Suppose  $\omega$  is a positive semi-definite operator, then

$$\left| \operatorname{Tr}(A^{\dagger}B\omega) \right|^2 \le \operatorname{Tr}(A^{\dagger}A\omega)\operatorname{Tr}(B^{\dagger}B\omega).$$
 (S3)

For super-operators  $\mathcal{A}$ , we will use  $\|\mathcal{A}\|_{\diamond}$  to denote its diamond norm. In our analysis, we will often encounter super-operators of the form

$$\mathcal{A}(\rho) = \sum_{i} A_{i} \rho B_{i},\tag{S4}$$

<sup>\*</sup> rahul.trivedi@mpq.mpg.de

where  $A_i$  and  $B_i$  are some operators. For such super-operators, it is convenient to note that the Holder's inequality implies that

$$\|\mathcal{A}\|_{\diamond} \le \sum_{i} \|A_{i}\| \|B_{i}\|. \tag{S5}$$

For instance, given an operator L, we will often use  $\mathcal{D}_L$  to denote the following superoperator:

$$\mathcal{D}_L = L\rho L^{\dagger} - \frac{1}{2} \{ L^{\dagger} L, \rho \}, \tag{S6}$$

where  $\{\cdot, \cdot\}$  is the anti-commutator between two operators.  $\mathcal{D}_L$  will be called the "dissipator corresponding to L". From Eq. (S5), we then obtain that

$$\|\mathcal{D}_L\|_{\diamond} \le \|L\|^2 + \|L^{\dagger}L\| \le 2\|L\|^2$$
. (S7)

A super-operator  $\mathcal{E}$  is completely positive if and only if it can be expressed as

$$\mathcal{E}(\rho) = \sum_{i} K_i \rho K_i^{\dagger} \tag{S8}$$

for some operators  $K_i$ . It will be called a channel if it is additionally trace preserving which requires  $\sum_i K_i^{\dagger} K_i = I$ . For any completely-positive trace preserving map  $\mathcal{E}$ ,  $\|\mathcal{E}\|_{\diamond} \leq 1$ .

#### B. Fermions and Bosons

The Hilbert space of m fermionic modes is described by the vacuum state  $|\text{vac}\rangle$  and the standard creation  $(a_i^{\dagger})$  and annihilation  $(a_i)$  operators, with  $i \in \{1, 2, \dots m\}$  labeling the fermionic mode. These satisfy the canonical anticommutation relations:

$$\{a_i, a_j\} = 0 \text{ and } \{a_i, a_j^{\dagger}\} = \delta_{i,j}.$$
 (S9)

The Hilbert space of the fermionic model is the finite-dimensional vector space given by span $\{\prod_{k=1}^{m}(a_k^{\dagger})^{\mu_k} | \text{vac} \rangle : \mu_k \in \{0,1\}\}$ . It will be convenient to work with the 2m Majorana fermion operators defined by

$$c_i^1 = \frac{1}{\sqrt{2}} (a_i^{\dagger} + a_i) \text{ and } c_i^2 = \frac{i}{\sqrt{2}} (a_i^{\dagger} - a_i).$$
 (S10)

The Majorana operators are each Hermitian, traceless and satisfy  $\{c_i^{\alpha}, c_{i'}^{\alpha'}\} = \delta_{i,i'}\delta_{\sigma,\sigma'}$ . We define  $\mathcal{C}_{2m}$  as the algebra generated by the 2m Majorana operators: An operator  $X \in \mathcal{C}_{2m}$  can be expressed as a linear combination of monomials of the form  $\prod_{i=1}^{m} \prod_{\alpha=1}^{2} (c_i^{\alpha})^{\mu_i^{\alpha}}$ , where  $\mu_i^{\alpha} \in \{0,1\}$ . The operator X will be even if it is a linear combination of only even degree monomials, and odd if it is a linear combination of odd degree monomials. Furthermore, any Hermitian operator defined on the fermionic Hilbert space is also in  $\mathcal{C}_{2m}$  and, as usual, fermionic quantum states are positive semi-definite Hermitian operators in  $\mathcal{C}_{2m}$ .

Given a fermionic state  $\rho$ , its correlation matrix elements are defined by  $\Gamma_{i,i'}^{\alpha,\alpha'}=i\mathrm{tr}(\rho[c_i^\alpha,c_{i'}^{\alpha'}])/2$ . A fermionic state  $\rho$  is called Gaussian if it can be expressed as  $\exp(-\beta H)/\mathrm{Tr}(\exp(-\beta H))$  for some Hermitian operator H that is quadratic in the Majorana operators and  $\beta\in\mathbb{R}\cup\{-\infty,\infty\}$ . Thus, fermionic Gaussian states are either Gibb's states of Hamiltonians that are quadratic in the Majorana operators, or are projectors on their ground-state subspace. Fermionic Gaussian states are fully characterized by their correlation matrix elements  $\Gamma_{i,i'}^{\alpha,\alpha'}$  [S1, S2]. We will refer to a fermionic state as convex-Gaussian if it can be expressed as a convex combination of Gaussian states.

Similar to fermions, the Hilbert space of m bosonic modes will be described by a vacuum state  $|\text{vac}\rangle$  and the creation  $(a_i^{\dagger})$  and annihilation  $(a_i)$  operators, with  $i \in \{1, 2...m\}$  labeling the bosonic mode. These satisfy the canonical commutation relations:

$$[a_i, a_{i'}] = 0 \text{ and } [a_i, a_{i'}^{\dagger}] = \delta_{i,i'}.$$
 (S11)

The Hilbert space of the bosonic model is the infinite-dimensional vector space given by span $\{\prod_i (a_i^{\dagger})^{\mu_i} | \text{vac} \rangle : \mu_i \in \{0, 1, 2 \dots \}\}$ . It will be convenient to work with the 2m quadrature operators

$$c_i^1 = \frac{1}{\sqrt{2}} (a_i^{\dagger} + a_i) \text{ and } c_i^2 = \frac{i}{\sqrt{2}} (a_i^{\dagger} - a_i).$$
 (S12)

The quadrature operators are Hermitian and satisfy  $[c_i^{\alpha}, c_i^{\alpha'}] = -i\delta_{i,i'}\Omega_{\alpha,\alpha'}$ , where  $\Omega$  is the  $2 \times 2$  symplectic matrix. Similar to a fermionic state, a bosonic state  $\rho$  is Gaussian if it can be expressed as  $\exp(-\beta H)/\operatorname{Tr}(\exp(-\beta H))$  for some Hermitian operator H which is quadratic or linear in the quadrature operators and for some  $\beta \in \mathbb{R} \cup \{-\infty, \infty\}$ . A state will be called convex-Gaussian if it can be expressed as a convex combination of Gaussians. A useful property of Gaussian states that we will use in our analysis is given in the lemma below.

**Lemma 1.** Suppose  $\rho$  is a (fermionic or bosonic) Gaussian state and  $A = \sum_{i,i'} A_{i,i'}^{\alpha,\alpha'} c_i^{\alpha} c_{i'}^{\alpha'}$  is a quadratic operator, then  $\rho' = e^{-A} \rho e^{-A^{\dagger}} / \text{Tr}(e^{-A} \rho e^{-A^{\dagger}})$  is also a Gaussian state.

*Proof.* This follows from the closure of quadratic and linear operators under commutation, i.e.

- (1) For fermions, the commutator of any two operators of the form  $\sum_{i,i'}\sum_{\alpha,\alpha'}x_{i,i'}^{\alpha,\alpha'}c_i^{\alpha}c_{i'}^{\alpha'}$ , where  $x_{i,i'}^{\alpha,\alpha'}\in\mathbb{C}$ , is again of the same form.
- (2) For bosons, the commutator of any two operators of the form  $\sum_{i,i'}\sum_{\alpha,\alpha'}x_{i,i'}^{\alpha,\alpha'}c_i^{\alpha}c_{i'}^{\alpha'}+\sum_{i,\alpha}y_i^{\alpha}c_i^{\alpha}$ , where  $x_{i,i'}^{\alpha,\alpha'},y_i^{\alpha}\in\mathbb{C}$ , is again of the same form.

Since  $\rho$  is a Gaussian state, it is expressible as  $\exp(-\beta H)/\operatorname{Tr}(\exp(-\beta H))$ , where H is a quadratic form in  $c_i^{\alpha}$  with a possible linear term in  $c_i^{\alpha}$  for bosons. Consequently, using the Baker-Campbell-Hausdorff formula, we obtain that  $e^{-A}\rho e^{-A^{\dagger}}$  can be written as a linear combination of A,  $A^{\dagger}$ , H and their nested commutators. Consequently, from 1 and 2 above, we obtain that  $e^{-A}\rho e^{-A^{\dagger}} \propto \exp(-\beta H')$  for some  $\beta$  and H' that is also a quadratic form in  $c_i^{\alpha}$  with a possible linear term for bosons. Furthermore, note that since  $\rho$  is positive-semidefinite, so is  $e^{-A}\rho e^{-A^{\dagger}}$  and thus is a valid quantum state.

#### C. Trotter formula

In our analysis below, we will often use first-order Trotterization for time-dependent models. Given a time-dependent Lindbladian  $\mathcal{L}(t) = \mathcal{L}^{(1)}(t) + \mathcal{L}^{(2)}(t) + \dots \mathcal{L}^{(M)}(t)$ , its first-order Trotterization in the time-interval [0, t], with T Trotter steps each of length  $\delta = t/T$ , will be given by

$$\Phi = \prod_{\tau=T}^{1} \Phi_{\tau\delta,(\tau-1)\delta}^{(1)} \Phi_{\tau\delta,(\tau-1)\delta}^{(2)} \dots \Phi_{\tau\delta,(\tau-1)\delta}^{(M)} \text{ where } \Phi_{\tau\delta,(\tau-1)\delta}^{(j)} = \mathcal{T} \exp\left(\int_{(\tau-1)\delta}^{\tau\delta} \mathcal{L}^{(j)}(s)ds\right). \tag{S13}$$

In Lemma 2 below, we provide an upper bound on the error between the exact evolution  $\mathcal{T}\exp(\int_0^t \mathcal{L}(s)ds)$  and the Trotter formula  $\Phi$  that we will use repeatedly in the following sections.

**Lemma 2** (Trotter error for bounded Lindbladians). Suppose for any  $s \ge 0$  and  $j \in \{1, 2...M\}$ ,  $\|\mathcal{L}^{(j)}(s)\|_{\diamond} \le \ell_j$ , then for any T > 0,

$$\left\| \mathcal{T} \exp\left( \int_0^t \mathcal{L}(s) ds \right) - \Phi \right\|_{\diamond} \le \frac{t^2}{T} \left( \sum_{j=1}^M \ell_j \right)^2. \tag{S14}$$

#### D. Asymptotic notation

Throughout the paper, we employ the following asymptotic notation commonly used in complexity theory [S3]:

| Notation              | Formal definition                                                                 | Informal description                  |
|-----------------------|-----------------------------------------------------------------------------------|---------------------------------------|
| $f(n) = \Omega(g(n))$ | $\exists k > 0, n_0 : \forall n > n_0,  f(n)  \ge kg(n)$                          | f(n) grows at least as fast as $g(n)$ |
| f(n) = O(g(n))        | $\exists k > 0, n_0 : \forall n > n_0,  f(n)  \le kg(n)$                          | f(n) grows no faster than $g(n)$      |
| $f(n) = \Theta(g(n))$ | $\exists k_1 > 0, k_2 > 0, n_0 : \forall n > n_0, k_1 g(n) \le f(n) \le k_2 g(n)$ | f(n) and $g(n)$ grow equally fast     |

TABLE SI. Table of asymptotic notation used in this paper.

#### E. Model

Here, we briefly recap the fermionic and bosonic models introduced in the main text and streamline the notation. We will consider a more general setting than the one described in the main text: specifically, we will allow here for inter-site non-Gaussian interactions. We recall that we consider systems with n sites, with each site containing L bosonic or fermionic modes. We will use m = nL to denote the total number of modes in the system. With the  $\sigma^{\text{th}}$  mode at the  $i^{\text{th}}$  site, where  $\sigma \in \{1, 2 \dots L\}$  and  $i \in \{1, 2 \dots n\}$ , we will associate an annihilation operator  $a_{i,\sigma}$ —it will be notationally convenient for us to group  $i, \sigma$  into a single index  $v = (i, \sigma)$  and denote the corresponding annihilation operator by  $a_v$ . Furthermore, corresponding to a mode index v, we will use  $i_v$  to denote the site the mode is at and  $\sigma_v$  to be the local index of the mode. Associated with the mode at v, we will also define the operators  $n_v, c_v^1, c_v^2$  via

$$n_v = a_v^{\dagger} a_v, c_v^1 = \frac{a_v + a_v^{\dagger}}{\sqrt{2}} \text{ and } c_v^2 = \frac{a_v - a_v^{\dagger}}{\sqrt{2}i}.$$
 (S15)

Here,  $n_v$  is an operator measuring the number of particles in mode v, and  $c_v^1, c_v^2$  are the Majorana operators (for fermions) or the quadrature operators (for bosons).

As in the main text, the Hamiltonian for the fermionic or bosonic problem will be decomposed as

$$H(t) = H_{\rm g}(t) + H_{\rm ng}(t),$$
 (S16)

where  $H_{\rm g}(t)$  is Gaussian given by

$$H_{g}(t) = \sum_{v,v'} \sum_{\alpha,\alpha'} J_{v,v'}^{\alpha,\alpha'}(t) c_v^{\alpha} c_{v'}^{\alpha'} + \sum_{v,\alpha} \Omega_v^{\alpha}(t) c_v^{\alpha}, \tag{S17}$$

with  $\Omega_v^{\alpha}(t) = 0$  for fermions, and  $H_{\rm ng}(t)$  is non-Gaussian given by

$$H_{\rm ng}(t) = \sum_{v,v'} U_{v,v'}(t) n_v n_{v'}.$$
 (S18)

Without loss of generality, we can assume that

For fermions,  $J_{v,v'}^{\alpha,\alpha'}(t)$  is purely imaginary and  $J_{v,v'}^{\alpha,\alpha'}(t) = -J_{v',v}^{\alpha',\alpha}(t)$ ,

For bosons,  $J_{v,v'}^{\alpha,\alpha'}(t)$  is purely real and  $J_{v,v'}^{\alpha,\alpha'}(t) = J_{v',v}^{\alpha',\alpha}(t)$ ,

For both fermions and bosons,  $U_{v,v'}(t)$  is purely real and  $U_{v,v'}(t) = U_{v',v}(t)$ .

As in the main text, we will also define constants  $J_C, J_{os}, U_C, U_{os}, \Omega$ :

(1)  $J_C$  is a measure of the strength of the Gaussian terms coupling modes at different sites: It is the smallest number such that  $\forall t$  and  $v = (i, \sigma)$

$$\sum_{i':i'\neq i,\sigma'} \sum_{\alpha,\alpha'} |J_{i,\sigma;i',\sigma'}^{\alpha,\alpha'}(t)| \le J_C. \tag{S19}$$

(2)  $J_{os}$  is a measure of the strength of the Gaussian terms coupling modes at the same site: It is the smallest number such that  $\forall t$  and  $v = (i, \sigma)$

$$\sum_{\sigma'} \sum_{\alpha,\alpha'} |J_{i,\sigma;i,\sigma'}^{\alpha,\alpha'}(t)| \le J_{\text{os}}.$$
 (S20)

(3)  $U_C$  is a measure of the strength of the non-Gaussian terms coupling modes at different sites: It is the smallest number such that  $\forall t$  and  $v = (i, \sigma)$

$$\sum_{i' \neq i, \sigma'} |U_{i,\sigma;i',\sigma'}(t)| \le U_C. \tag{S21}$$

(4)  $U_{os}$  is a measure of the strength of the non-Gaussian terms coupling modes at the same site: It is the smallest number such that  $\forall t$  and  $v = (i, \sigma)$

$$\sum_{i\sigma'} |U_{i,\sigma;i,\sigma'}(t)| \le U_{\text{os}}.$$
 (S22)

(5)  $\Omega$  is a measure of the on-site displacement: it is the smallest number such that  $\forall t$  and  $v = (i, \sigma)$

$$\sum_{\alpha} |\Omega_{i,\sigma}^{\alpha}(t)| \le \Omega. \tag{S23}$$

Note that  $\Omega \neq 0$  only for the bosonic model—we do not include a displacement term in the fermionic model.

Note that the inter-site non-Gaussian interactions were not included in the main text, and the results quoted in the main text can be obtained by setting  $U_C = 0$ . Finally, it will also be convenient to define the parameter  $\Lambda$  as

$$\Lambda = J_C + U_C + J_{os} + U_{os} + \kappa + \Omega. \tag{S24}$$

While analyzing the bosonic model, it will be more convenient to express  $H_g$  as a sum of particle number conserving and non-conserving terms via

$$H_{g}(t) = \underbrace{\sum_{v,v'} \left( \mathcal{J}_{v,v'}(t) a_{v}^{\dagger} a_{v'} + \text{h.c.} \right)}_{H_{g}^{\text{hop}}(t)} + \underbrace{\sum_{v,v'} \left( \mathcal{G}_{v,v'}(t) a_{v} a_{v'} + \text{h.c.} \right)}_{H_{g}^{\text{sq}}(t)} + \underbrace{\sum_{v} \left( \mathcal{D}_{v}(t) a_{v} + \text{h.c.} \right)}_{H_{g}^{\text{disp}}(t)}, \tag{S25}$$

where, up to a possibly time-dependent energy shift in  $H_{\rm g}(t)$ ,  $\mathcal{J}_{v,v'}=(J_{v,v'}^{1,1}-iJ_{v,v'}^{1,2}-iJ_{v,v'}^{2,1}+J_{v,v'}^{2,2})/2$ ,  $\mathcal{G}_{v,v'}(t)=(J_{v,v'}^{1,1}+iJ_{v,v'}^{1,2}+iJ_{v,v'}^{2,1}-J_{v,v'}^{2,2})/2$  and  $\mathcal{D}_v=(\Omega_{\nu}^1(t)-i\Omega_{\nu}^2(t))/\sqrt{2}$ . Here,  $H_{\rm g}^{\rm hop}(t)$  is a particle hopping term between different bosonic modes and conserves the total particle number  $N=\sum_v n_v$ ,  $H_{\rm g}^{\rm sq}(t)$  can be considered to be a multi-mode squeezing term in the Hamiltonian and  $H_{\rm g}^{\rm disp}(t)$  displaces the individual bosonic modes. Both  $H_{\rm g}^{\rm sq}(t)$  and  $H_{\rm g}^{\rm disp}(t)$  do not conserve the total particle number N. It will also be convenient to define the constant  $\mathcal G$  as the smallest number such that for all t and v

$$\sum_{v'} |\mathcal{G}_{v,v'}(t)| \le \mathcal{G}. \tag{S26}$$

Furthermore, it can be noted that  $|\mathcal{D}_v(t)| \leq \Omega/\sqrt{2}$ .

Finally, the noise in the dynamics of the bosonic and fermionic models will be modeled by the Lindbladian  $\mathcal{L}_n$  given by

$$\mathcal{L}_{\mathbf{n}} = \sum_{l=1}^{3} \sum_{i,\sigma} \kappa_l \mathcal{D}_{L_{i,\sigma}^{(l)}},\tag{S27}$$

where  $\mathcal{D}_L \rho = L \rho L^{\dagger} - \{L^{\dagger} L, \rho\}/2$ ,  $L_{i,\sigma}^{(1)} = a_{i,\sigma}$  (incoherent particle loss),  $L_{i,\sigma}^{(2)} = a_{i,\sigma}^{\dagger}$  (incoherent particle gain), and  $L_{i,\sigma}^{(3)} = a_{i,\sigma}^{\dagger} a_{i,\sigma} = n_{i,\sigma}$  (dephasing). Unless otherwise mentioned, we will assume that all three dissipators act on each mode  $\kappa_1, \kappa_2, \kappa_3 > 0$  and will denote the total dissipation rate by  $\kappa = \kappa_1 + \kappa_2 + \kappa_3$ . We summarize all the parameters of the model in Table SII.

## II. HIGH NOISE SIMULABILITY OF THE FERMIONIC MODEL (THEOREM 1)

In this section, we will present the proof of Theorem 1, which establishes the high-noise simulability of the fermionic model. We will first analyze the Trotterization of the continuous-time model, followed by analyzing each Trotter time-step to establish its convex Gaussianity for high noise and to obtain an explicit algorithm for classically simulating either sampling from or computing local observables in the fermionic state. We begin with a first-order Trotter approximation to  $\rho(t)$  with the following splitting of the Lindbladian  $\mathcal{L}(t)$  into a Gaussian and non-Gaussian Lindbladian:

$$\mathcal{L}(t) = -i[H_{g}(t), \cdot] + \sum_{l \in \{1,2\}} \sum_{i,\sigma} \kappa_{l} \mathcal{D}_{L_{i,\sigma}^{(l)}} -i[H_{ng}(t), \cdot] + \sum_{i,\sigma} \kappa_{3} \mathcal{D}_{L_{i,\sigma}^{(3)}},$$

$$\mathcal{L}_{g}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_{ng}(t) \qquad \mathcal{L}_$$

We next Trotterize the state  $\rho(t)$  into T Trotter steps: The Trotterized state  $\sigma_T$  will be given by

$$\sigma_T = \left( \prod_{\tau=T}^1 \Phi_{\tau\delta,(\tau-1)\delta}^{\text{ng}} \Phi_{\tau\delta,(\tau-1)\delta}^{\text{g}} \right) \rho(0), \tag{S29a}$$

| Parameter                                                                       | Defined in   | Informal description                                     |
|---------------------------------------------------------------------------------|--------------|----------------------------------------------------------|
|                                                                                 |              | Gaussian coupling between two fermionic or bosonic       |
| $J_{v,v'}^{\alpha,\alpha'}(t)$ or $J_{i,\sigma;i',\sigma'}^{\alpha,\alpha'}(t)$ | Eq. (S17)    | modes                                                    |
|                                                                                 |              | Maximum total strength of Gaussian coupling between a    |
| $J_C$                                                                           | Eq. (S19)    | mode and all other modes at different sites              |
|                                                                                 |              | Maximum total strength of Gaussian coupling between a    |
| $J_{\rm os}$                                                                    | Eq. (S20)    | mode and all other modes at the same site                |
|                                                                                 |              | Non-Gaussian interaction between two fermionic or        |
| $U_{v,v'}(t)$ or $U_{i,\sigma;i',\sigma'}(t)$                                   | Eq. (S18)    | bosonic modes                                            |
|                                                                                 |              | Maximum total strength of non-Gaussian interaction be-   |
| $ U_C $                                                                         | Eq. (S21)    | tween a mode and all other modes at different sites      |
|                                                                                 |              | Maximum total strength of non-Gaussian interaction be-   |
| $U_{os}$                                                                        | Eq. (S22)    | tween a mode and all other modes at the same site        |
| Λ                                                                               | Eq. (S24)    | Total coupling strength                                  |
| $\Omega_v(t)$ or $\Omega_{i,\sigma}(t)$                                         | Eq. (S17)    | On-site displacement acting on bosonic modes             |
| $\mathcal{J}_{v,u}(t)$                                                          | Eq. (S25)    | Gaussian hopping between two bosonic modes               |
| $G_{v,u}(t)$                                                                    | Eq. (S25)    | Multi-mode squeezing term between two bosonic modes      |
|                                                                                 |              | Maximum strength of multi-mode squeezing between one     |
| $ \mathcal{G} $                                                                 | Eq. (S26)    | bosonic mode with all other modes                        |
| $\mathcal{D}_v(t)$                                                              | Eq. (S25)    | Single-mode displacement acting on bosonic modes         |
| $\kappa$                                                                        | Eq. (S27)    | Total dissipation rate                                   |
| $\kappa_1$                                                                      | Eq. (S27)    | Dissipation rate for incoherent particle loss            |
| $\kappa_2$                                                                      | Eq. (S27)    | Dissipation rate for incoherent particle gain            |
| $\kappa_3$                                                                      | Eq. (S27)    | Dissipation rate for dephasing                           |
| $\gamma$                                                                        | Assumption 2 | Defined as $\gamma = \kappa_1 - \kappa_2 - 2\mathcal{G}$ |
| n                                                                               |              | Number of sites                                          |
| L                                                                               |              | Number of modes per site                                 |
| $\overline{m}$                                                                  |              | Total number of modes $m = nL$                           |

TABLE SII. Table of all the coefficients and parameters relevant to the bosonic and fermionic models.

where  $\delta = t/T$  and

$$\Phi_{t,t'}^{\text{ng}} = \mathcal{T} \exp\left(\int_{t'}^{t} \mathcal{L}_{\text{ng}}(s) ds\right) \text{ and } \Phi_{t,t'}^{\text{g}} = \mathcal{T} \exp\left(\int_{t'}^{t} \mathcal{L}_{\text{g}}(s) ds\right). \tag{S29b}$$

We first provide a bound on  $\|\sigma_T - \rho(t)\|_1$ .

**Lemma 3** (Trotterization: Fermionic model). For all T > 0,

$$\|\sigma_T - \rho(t)\|_1 \le \frac{4t^2 m^2}{T} \Lambda^2.$$

Proof. Noting that  $\|\mathcal{L}_{ng}(s)\|_{\diamond} \leq 2m(U_C + U_{os} + \kappa_3)$  and  $\|\mathcal{L}_{g}(s)\|_{\diamond} \leq 2m(J_C + J_{os} + \kappa_1 + \kappa_2)$ , we obtain that the parameter  $\ell$  in Lemma 2 can be chosen to be  $2m\Lambda$ . The lemma statement then follows directly from Lemma 2.

**Lemma 4** (Convex-gaussianity condition for 2-fermionic modes). Consider a Lindbladian on two fermionic modes given by

$$\mathcal{L}(t) = -i[h(t), \cdot] + \sum_{i \in \{1, 2\}} \kappa_i(t) \mathcal{D}_{n_i},$$

where  $h(t) = u(t)n_1n_2$  and  $n_i$  is the number operator for the  $i^{th}$  mode. If  $\kappa_i(t) \geq |u(t)|$ , then the channel  $\mathcal{T}\exp(\int_t^{t+\tau} \mathcal{L}(s)ds)$  generated by the Lindbladian in the time interval  $(t,t+\tau)$  maps a convex Gaussian state to another convex Gaussian state.

*Proof.* It will be convenient to define the scalars

$$U = \int_{t}^{t+\tau} u(s)ds, \quad K_{i} = \int_{t}^{t+\tau} \kappa_{i}(s)ds, \quad \text{and } K = K_{1} + K_{2}.$$
 (S30)

We also note that, since both the Hamiltonian and the jump operators are expressible as polynomials of the fermionic number operators  $n_1, n_2$ , they commute with each other. Therefore,

$$\mathcal{T}\exp\left(\int_{t}^{t+\tau} \mathcal{L}(s)ds\right) = \exp\left(-iU[n_{1}n_{2}, \cdot]\right)\exp\left(K_{1}\mathcal{D}_{n_{1}}\right)\exp\left(K_{2}\mathcal{D}_{n_{2}}\right). \tag{S31}$$

We define the channel  $\mathcal{R}_{t+\tau,t}$  via

$$\mathcal{R}_{t+\tau,t}(\rho) = \mathbb{E}_z(R(z)\rho R^{\dagger}(z)) \text{ where } R(z) = \exp\left(\sqrt{U}e^{-i\pi/4}(zn_1 + z^*n_2)\right), \tag{S32}$$

where  $z = (a+ib)/\sqrt{2}$  with a, b being independent standard normal random variables. Note that, due to Lemma 1,  $\mathcal{R}_{t+\tau,t}$  maps an input Gaussian state to a (possibly unnormalized) convex-Gaussian state.

We now explicitly compute  $\mathcal{R}_{t+\tau,t}(\rho)$ . define  $\mathcal{N}_{i,l}$  as the superoperator which left multiplies by  $n_i$  (i.e.  $\mathcal{N}_{i,l}(\rho) = n_i \rho$ ) and  $\mathcal{N}_{i,r}$  as the superoperator which right multiplies by  $n_i$  (i.e.  $\mathcal{N}_{i,r}(\rho) = \rho n_i$ ). Then

$$\mathcal{R}_{t+\tau,t} = \mathbb{E}_{z} \Big( \exp \Big( \sqrt{U} e^{-i\pi/4} (z \mathcal{N}_{1,l} + z^{*} \mathcal{N}_{2,l}) + \sqrt{U}^{*} e^{i\pi/4} (z^{*} \mathcal{N}_{1,r} + z \mathcal{N}_{2,r}) \Big) \Big) \\
= \mathbb{E}_{a} \Big( \exp \Big( \frac{a}{\sqrt{2}} \Big( \sqrt{U} e^{-i\pi/4} (\mathcal{N}_{1,l} + \mathcal{N}_{2,l}) + \sqrt{U}^{*} e^{i\pi/4} (\mathcal{N}_{1,r} + \mathcal{N}_{2,r}) \Big) \Big) \Big) \times \\
\mathbb{E}_{b} \Big( \exp \Big( \frac{ib}{\sqrt{2}} \Big( \sqrt{U} e^{-i\pi/4} (\mathcal{N}_{1,l} - \mathcal{N}_{2,l}) - \sqrt{U}^{*} e^{i\pi/4} (\mathcal{N}_{1,r} - \mathcal{N}_{2,r}) \Big) \Big) \Big) \Big) \\
\stackrel{\text{(1)}}{=} \exp \Big( -i \frac{U}{4} (\mathcal{N}_{1,l} + \mathcal{N}_{2,l})^{2} + i \frac{U}{4} (\mathcal{N}_{1,r} + \mathcal{N}_{2,r})^{2} + \frac{|U|}{2} (\mathcal{N}_{1,l} + \mathcal{N}_{2,l}) (\mathcal{N}_{1,r} + \mathcal{N}_{2,r}) \Big) \times \\
\exp \Big( i \frac{U}{4} (\mathcal{N}_{1,l} - \mathcal{N}_{2,l})^{2} - i \frac{U}{4} (\mathcal{N}_{1,l} - \mathcal{N}_{2,r})^{2} + \frac{|U|}{2} (\mathcal{N}_{1,l} - \mathcal{N}_{2,l}) (\mathcal{N}_{1,r} - \mathcal{N}_{2,r}) \Big) \\
= \exp \Big( -iU(\mathcal{N}_{1,l} \mathcal{N}_{2,l} - \mathcal{N}_{1,r} \mathcal{N}_{2,r}) + |U| (\mathcal{N}_{1,l} \mathcal{N}_{1,r} + \mathcal{N}_{2,l} \mathcal{N}_{2,r}) \Big), \tag{S33}$$

where, in (1), we have used the fact that, for any operator O,  $\mathbb{E}_{x \in \mathcal{N}(0,1)}(e^{xO}) = e^{O^2/2}$ . Identifying  $\mathcal{N}_{1,l}\mathcal{N}_{2,l} - \mathcal{N}_{1,r}\mathcal{N}_{2,r} = [n_1n_2, \cdot]$ , we obtain that

$$\exp(-iU[n_1 n_2, \cdot]) = \exp(-|U|(\mathcal{N}_{1,l} \mathcal{N}_{1,r} + \mathcal{N}_{2,l} \mathcal{N}_{2,r})) \mathcal{R}_{t+\tau,t}.$$
 (S34)

Using Eq. (S34) and Eq. (S31) together with the fact that  $\mathcal{D}_{n_i} = \mathcal{N}_{i,l} \mathcal{N}_{i,r} - (\mathcal{N}_{i,l}^2 + \mathcal{N}_{i,r}^2)/2$ , we obtain that

$$\mathcal{T}\exp\left(\int_{t}^{t+\tau} \mathcal{L}(s)ds\right) = \left(\prod_{i\in\{1,2\}} \underbrace{\exp((K_{i}-|U|)\mathcal{N}_{i,l}\mathcal{N}_{i,r})}_{\mathcal{E}_{i}} \underbrace{\exp(-(\mathcal{N}_{i,l}^{2}+\mathcal{N}_{i,r}^{2})/2)}_{\mathcal{F}_{i}}\right) \mathcal{R}_{t+\tau,t}. \tag{S35}$$

We note that  $\mathcal{R}_{t+\tau,t}$  and  $\mathcal{F}_i$  are completely positive maps that map convex Gaussian states to possibly unnormalized Gaussian states. Furthermore, if  $K_i \geq |U|$ , which is implied by  $\kappa_i(t) \geq |u(t)|$  quoted in the lemma statement, then  $\mathcal{E}_i$  also have this property. Consequently, since  $\mathcal{T} \exp(\int_t^{t+\tau} \mathcal{L}(s)ds)$  is a channel, as long as  $K_i \geq |U|$ , it maps convex Gaussian states to (normalized) convex Gaussian states.

**Theorem 1** (High-noise convex Gaussianity and classical simulation of the fermionic model, reproduced from the main text). For an initial Gaussian state, if  $\kappa_3 \geq 2U$ , then the state of the fermionic model at time t,  $\rho(t)$ , is convex Gaussian for all  $t \geq 0$ . Furthermore,  $\rho(t)$  can be classically sampled in the Fock state basis to an  $\epsilon$  total variation error in  $O(m^7\Lambda^2t^2/\epsilon)$  time.

*Proof.* Consider the Trotterized state  $\sigma_T$  [Eq. (S29)]—note that  $\Phi_{\tau\delta,(\tau-1)\delta}^{\rm g}$  is a Gaussian channel and hence trivially preserves convex Gaussianity. We now obtain the condition under which  $\Phi_{\tau\delta,(\tau-1)\delta}^{\rm ng}$  also preserves convex Gaussianity using Lemma 4. We first perform the decomposition

$$\Phi_{\tau\delta,(\tau-1)\delta}^{\text{ng}} = \prod_{v,u} \mathcal{T} \exp\left(\int_{(\tau-1)\delta}^{\tau\delta} \mathcal{L}_{v,u}(s)ds\right) \text{ where } \mathcal{L}_{v,u} = -i[U_{v,u}(t)n_v n_u, \cdot] + \kappa_3 \left(p_{v,u}(t)\mathcal{D}_{n_v} + q_{v,u}(t)\mathcal{D}_{n_u}\right), \quad (S36)$$

where we choose

$$p_{v,u}(t) = \frac{1}{2} \frac{|U_{v,u}(t)|}{\sum_{u} |U_{v,u}(t)|} \text{ and } q_{v,u}(t) = \frac{1}{2} \frac{|U_{v,u}(t)|}{\sum_{v} |U_{v,u}(t)|}.$$
 (S37)

Next, we apply Lemma 4: For  $\mathcal{L}_{v,u}(t)$  to generate a channel that is convex-Gaussianity preserving, a sufficient condition is that

$$\kappa_3 p_{v,u}(t), \kappa_3 q_{v,u}(t) \ge |U_{v,u}(t)| \text{ or equivalently } \kappa_3 \ge 2 \sum_{k'} |U_{k,k'}(t)| \text{ for } k \in \{v,u\}.$$
(S38)

Since  $\sum_{k'} |U_{k,k'}(t)| \leq U_C + U_{\text{os}}$ , this condition is satisfied if  $\kappa_3 \geq 2(U_C + U_{\text{os}})$ . Assuming this to be true, it then follows from Lemma 4 that  $\Phi_{\tau\delta,(\tau-1)\delta}^{\text{ng}}$  maps an input Gaussian state to a convex-Gaussian state—consequently, the Trotterized state  $\sigma_T$  is a convex-Gaussian state such that  $\|\rho(t) - \sigma_T\|_1 \leq \epsilon$  when  $T = \Theta(t^2 m^2 \Lambda^2 / \epsilon)$ .

Time-complexity of sampling in the Fock state basis. Since  $\sigma_T$  is convex-Gaussian by construction, it can be expressed as  $\sigma_T = \int \rho_\alpha d\mu(\alpha)$ , where  $\rho_\alpha$  is a Gaussian state and  $\mu$  is a probability measure. To sample from  $\sigma_T$ , we can then first sample from  $\mu$  to obtain a Gaussian state and then use the standard algorithm for sampling from fermionic Gaussian states. Consider sampling from  $\mu(\alpha)$ : Suppose the initial state  $\rho(0)$  is a Gaussian state. Lemma 4 provides an explicit characterization of the convex combination of Gaussian states that result when applying  $\mathcal{T} \exp(\int_{(\tau-1)\delta}^{\tau\delta} \mathcal{L}_{v,u}(s)ds)$  on an input Gaussian state. Furthermore, since the covariance matrix of the Gaussian state is a  $2m \times 2m$  matrix, the probabilities of each Gaussian state in the convex combination being computable from the result for covariance matrices of products of Gaussian states [S2, S4] in  $O(m^3)$  time—sampling from this convex combination thus requires  $O(m^3)$  time. At every time-step, this has to be done for every pair of fermionic modes to apply  $\Phi_{\tau\delta,(\tau-1)\delta}^{ng}$ , thus yielding a total time-complexity of  $O(m^5)$ . The application of the Gaussian evolution in each time-step can also be done at the level of covariance matrices in  $O(m^3)$  time. Thus, the total time of sampling from  $\mu$  is given by  $O(m^5 \times T) = O(m^7 \Lambda^2 t^2 / \epsilon)$ . Finally, having sampled a Gaussian state  $\rho_\alpha$  from  $\sigma_T$ , we can draw a sample in the Fock state basis in  $O(m^3)$  time [S5, S6]—the total time complexity of the sampling algorithm thus is dominated by the cost of sampling from  $\mu$  and is given by  $O(m^7 \Lambda^2 t^2 / \epsilon)$ .

#### III. HIGH-NOISE SEPARABILITY OF THE BOSONIC MODEL (THEOREM 2)

In this section, we will present proof of Theorem 2, which considers the high-noise regime of the bosonic model. Since the bosonic model is infinite-dimensional with unbounded terms in the Hamiltonian, its analysis first requires an analysis of the particle number (as well as its moments) in the model. We do so in the first subsection—then, in the proof of Theorem 2, we first approximate the infinite-dimensional bosonic modes with finite-dimensional qudits and quantify the approximation error. Finally, we analyze the resulting finite-dimensional model and establish high-noise separability in the model.

#### A. Analyzing particle number moments

We begin by introducing a physically motivated assumption on the initial state of the model—the initial state will be assumed to be a product state with a "uniform particle moment density" assumption, similar to that used in Ref. [S7].

**Assumption 1** (Uniform particle moment density). The initial state  $\rho(0)$  is a product state and  $\exists C_0, \alpha_0, \beta_0 > 0$  such that  $\forall v \text{ and } k \in \{1, 2, 3 \dots\}$

$$\operatorname{Tr}(n_{v}^{k}\rho(0)) \leq C_{0}^{k}k^{\alpha_{0}k+\beta_{0}}.$$

As shown in Ref. [S7], this assumption is satisfied for a wide variety of physically relevant initial states of the bosonic model, notably for the vacuum state, thermal states, as well as coherent states. Furthermore, it implies a bound on the moments of the total particle number  $N = \sum_{v} n_v$  since

$$\operatorname{Tr}(N^{k}\rho(0)) = \sum_{v_{1}, v_{2} \dots v_{k}} \operatorname{Tr}(n_{v_{1}} n_{v_{2}} \dots n_{v_{k}} \rho(0)) \leq \sum_{v_{1}, v_{2} \dots v_{k}} \prod_{i=1}^{k} \operatorname{Tr}(n_{v_{i}}^{k} \rho(0))^{1/k} \leq (C_{0}m)^{k} k^{\alpha_{0}k + \beta_{0}}, \tag{S39}$$

where we remind the reader that m = nL is the total number of bosonic modes in the model. This particle number moment bound, in turn, implies that the probability of high-particle-number states being occupied is exponentially suppressed, which we make precise in the following lemma.

**Lemma 5** (Probability of high-particle-number states (Ref. [S7])). Suppose  $\rho$  is a state which satisfies  $\text{Tr}(N^k\rho) \leq (Cm)^k k^{\alpha k + \beta}$  and  $\Pi_{\geq d}$  is a projector on the subspace with  $\geq d$  particles, then

$$\operatorname{Tr}(\Pi_{\geq d}\rho) \leq \left(\frac{de^{\alpha/\beta}}{Cme}\right)^{\beta/\alpha} e^{-(d/Cme)^{1/\alpha}}.$$

*Proof.* Note that, for any k > 0,

$$d^{k}\operatorname{Tr}(\Pi_{\geq d}\rho) \leq \operatorname{Tr}(N^{k}\Pi_{\geq d}\rho) \leq \operatorname{Tr}(N^{k}\rho) \leq (Cm)^{k}k^{\alpha k + \beta} \implies \operatorname{Tr}(\Pi_{\geq d}\rho) \leq k^{\beta} \left(\frac{Cmk^{\alpha}}{d}\right)^{k}. \tag{S40}$$

We can now pick k to be the greatest integer smaller than  $(d/Cme)^{1/\alpha}$ —we then have that  $(d/Cme)^{1/\alpha}-1 \le k \le (d/Cme)^{1/\alpha}$  and therefore

$$\operatorname{Tr}(\Pi_{\geq d}\rho) \leq \left(\frac{d}{Cme}\right)^{\beta/\alpha} e^{-k} \leq \left(\frac{de^{\alpha/\beta}}{Cme}\right)^{\beta/\alpha} e^{-(d/Cme)^{1/\alpha}},\tag{S41}$$

which proves the lemma statement.

While we will assume that the uniform particle moment density condition holds for the initial state, the subsequent dynamics of the bosonic model could possibly violate this condition. In the remainder of this section, we show that under the condition that the total rate of particle loss is higher than the total rate of particle gain (which we make precise below in assumption 2), the moments of the total particle number  $\text{Tr}(N^k \rho(t))$  satisfy an inequality similar to Eq. (S39), which by Lemma 5 implies that the probability of higher particle number states being occupied is super-polynomially small in the particle number.

**Assumption 2.** The parameters  $\kappa_1, \kappa_2$  and  $\mathcal{G}$  are such that  $2\gamma = \kappa_1 - \kappa_2 - 2\mathcal{G} > 0$ .

Physically, this assumption restricts the rate of 3 processes in the bosonic model that can change its particle number: In the noise terms, incoherent particle loss can decrease the particle number at a rate  $\sim \kappa_1$  and incoherent particle gain can increase the particle number at a rate  $\sim \kappa_2$ . Furthermore, in the Hamiltonian, the squeezing term  $(H_g^{sq}(t))$  in Eq. (S25) can also increase the number of particles in the system at a rate  $\sim \mathcal{G}$ . Assumption 2 constrains the model to have particle loss higher than particle gain, without which the number of particles can increase arbitrarily with time. We remark that we do not need any assumption on the strength of displacement term  $(H_g^{disp}(t))$  in Eq. (S25))—we will show in Lemma 8 that, as long as assumption 2 is satisfied, no matter how large the displacement term is, the particle number (and its moments) do not grow arbitrarily with time.

We begin with a two technical lemmas that will be useful in our analysis.

**Lemma 6.** Suppose  $x_k(t)$ , for  $k \in \{0, 1, 2...\}$ , are non-negative functions of time which satisfy the differential inequalities

$$\frac{d}{dt}x_k(t) \le -\gamma kx_k(t) + \lambda mk \sum_{q=1}^k 2^q \binom{k}{q} x_{k-q}(t),$$

where  $\gamma, \lambda, m > 0$ . Furthermore, suppose  $x_0(t) = 1 \ \forall t \geq 0 \ and \ \exists C_0, \alpha_0, \beta_0 > 0 : x_k(0) \leq (C_0 m)^k k^{\alpha_0 k + \beta_0}$  for all  $k \in \{1, 2, 3 \dots\}$ . Then

$$x_k(t) \le (Cm)e^{\alpha k + \beta}$$
, where  $C = e^{\lambda/\gamma}(C_0 + 2)$ ,  $\alpha = \max(\alpha_0, 1)$  and  $\beta = \beta_0$ .

*Proof.* The differential inequality can be written as an integral inequality:

$$x_k(t) \le x_k(0)e^{-\gamma kt} + \lambda mk \sum_{q=1}^k 2^q \binom{k}{q} \int_0^t x_{k-q}(s)e^{-\gamma k(t-s)} ds.$$
 (S42)

Recursing Eq. (S42), we obtain

$$x_{k}(t) \leq x_{k}(0)e^{-\gamma kt} + \sum_{p=1}^{k} \sum_{q_{1}=1}^{k} \sum_{q_{2}=1}^{k-q_{1}} \cdots \sum_{q_{p}=1}^{k-\sum_{i=1}^{p-1} q_{i}} \frac{2^{\sum_{i=1}^{p} q_{i}} \lambda^{p} k!}{q_{1}! q_{2}! \dots q_{p}! (k-\sum_{i=1}^{p} q_{i})!} \left( \prod_{i=1}^{p} \left(k-\sum_{j=1}^{i-1} q_{j}\right) \right) x_{k-\sum_{i=1}^{p} q_{i}}(0) I_{q_{1}, q_{2} \dots q_{p}}^{(k)}(t),$$
(S43)

where

$$I_{q_{1},q_{2}...q_{p}}^{(k)}(t) = \int_{0}^{t} \int_{0}^{s_{1}} \cdots \int_{0}^{s_{p-1}} e^{-\gamma k(t-s_{1})} e^{-\gamma(k-q_{1})(s_{1}-s_{2})} e^{-\gamma(k-q_{1}-q_{2})(s_{2}-s_{3})} \dots e^{-\gamma(k-q_{1}-q_{2}...-q_{p})s_{p}} ds_{1} ds_{2} \dots ds_{p}$$

$$= e^{-k\gamma t} \int_{0}^{t} \int_{0}^{s_{1}} \int_{0}^{s_{2}} \cdots \int_{0}^{s_{p-1}} e^{\gamma(q_{1}s_{1}+q_{2}s_{2}+...q_{p}s_{p})} ds_{1} ds_{2} \dots ds_{p}. \tag{S44}$$

We note that  $I_{q_1,q_2...q_p}^{(k)}(t)$  can be upper bounded:

$$I_{q_{1},q_{2}...q_{p}}^{(k)}(t) \leq e^{-k\gamma t} \int_{-\infty}^{t} \int_{-\infty}^{t} \cdots \int_{-\infty}^{t} e^{\gamma(q_{1}s_{1}+q_{2}s_{2}+...q_{p}s_{p})} ds_{1} ds_{2} \dots ds_{p}$$

$$\leq \frac{1}{\gamma^{p} q_{1} q_{2} \dots q_{p}} e^{-(k-q_{1}-q_{2}-...q_{p})\gamma t}$$

$$\leq \frac{1}{\gamma^{p}} e^{-\gamma(t-q_{1}-q_{2}-...q_{p})}.$$
(S45)

In the calculation done below, it will be useful to note that, given any f(n) where  $n \in \{0, 1, 2...\}$ ,

$$\sum_{q_{1}=1}^{k} \sum_{q_{2}=1}^{k-q_{1}} \cdots \sum_{q_{p}=1}^{k-\sum_{i=1}^{p-1} q_{i}} \frac{1}{q_{1}! q_{2}! \dots q_{p}!} f\left(\sum_{i=1}^{p} q_{i}\right) \stackrel{\text{(1)}}{=} \sum_{q=p}^{k} \sum_{q_{1}=1}^{q} \sum_{q_{2}=1}^{q-q_{1}} \cdots \sum_{q_{p}=1}^{q-\sum_{i=1}^{p-q} q_{i}} \frac{1}{q_{1}! q_{2}! \dots q_{p}!} f(q)
\stackrel{\text{(2)}}{=} \sum_{q=p}^{k} f(q) \sum_{\substack{q_{1}, q_{2} \dots q_{p} \geq 1 \\ q_{1}+q_{2}+\dots q_{p}=q}} \frac{1}{q_{1}! q_{2}! \dots q_{p}!}
\stackrel{\text{(3)}}{\leq} \sum_{q=p}^{k} \frac{p^{q} f(q)}{q!}, \tag{S46}$$

where in (1) we have introduced the index  $q=q_1+q_2+\ldots q_p$ , which ranges from p to k, and re-expressed the summation over  $q_1,q_2\ldots q_p$  as first a sum over q, and then a sum over  $q_1,q_2\ldots q_p$  subject to the contraint  $q_1+q_2+\ldots q_p=q$ . In (2), we have simply noted the fact that the summation over  $q_1\in\{1,2\ldots q\},q_2\in\{1,2\ldots q-q_1\}\ldots q_{p-1}\in\{1,2\ldots q-(q_1+q_2+q_{p-1})\}$  is identical to summation over  $q_1,q_2\ldots q_p\in\{1,2\ldots q\}$  with the additional constraint that  $q_1+q_2+\ldots q_p\leq q$ . Finally, (3) is obtained by identifying the summation as a multinomial sum.

Returning to Eq. (S43), we obtain that

$$x_{k}(t) \stackrel{\text{(1)}}{\leq} x_{k}(0)e^{-\gamma kt} + \sum_{p=1}^{k} \sum_{q_{1}=1}^{k} \sum_{q_{2}=1}^{k} \cdots \sum_{q_{p}=1}^{k} \frac{k!2^{q_{1}+q_{2}\dots q_{p}}}{q_{1}!q_{2}!\dots q_{p}!(k-\sum_{i=1}^{p}q_{i})!p!} \left(\frac{\lambda mk}{\gamma}\right)^{p} x_{k-\sum_{i=1}^{p}q_{i}}(0)e^{-\gamma t(k-\sum_{i=1}^{p}q_{i})} \\ \stackrel{\text{(2)}}{\leq} x_{k}(0)e^{-\gamma kt} + \sum_{p=1}^{k} \sum_{q=p}^{k} (2p)^{q} \binom{k}{q} \left(\frac{\lambda mk}{\gamma}\right)^{p} x_{k-q}(0)e^{-\gamma t(k-q)} \\ \stackrel{\text{(2)}}{\leq} (C_{0}m)^{k} k^{\alpha_{0}k+\beta_{0}} e^{-\gamma kt} + \sum_{q=1}^{k} \sum_{p=1}^{q} (2k)^{q} \binom{k}{q} \left(\frac{\lambda mk}{\gamma}\right)^{p} (C_{0}m)^{k-q} (k-q)^{\alpha_{0}(k-q)+\beta_{0}} e^{-\gamma t(k-q)} \\ \stackrel{\text{(2)}}{\leq} (C_{0}m)^{k} k^{\alpha_{0}k+\beta_{0}} e^{-\gamma kt} + m^{k} e^{k\lambda/\gamma} \sum_{q=1}^{k} \binom{k}{q} (2k)^{q} C_{0}^{k-q} k^{\alpha_{0}(k-q)+\beta_{0}} e^{-\gamma t(k-q)} \\ \stackrel{\text{(3)}}{\leq} (e^{\lambda/\gamma}m)^{k} k^{\beta_{0}} \sum_{q=1}^{k} \binom{k}{q} (C_{0}k^{\alpha_{0}} e^{-\gamma t})^{k-q} (2k)^{q} = (e^{\lambda/\gamma}m)^{k} k^{\beta_{0}} (C_{0}k^{\alpha_{0}} e^{-\gamma t} + 2k)^{k}, \tag{S47}$$

where, in (1), we have used Eq. (S45) and in (2) we have used Eq. (S46). Finally, using  $C_0 k^{\alpha_0} e^{-\gamma t} + 2k \le k^{\max(\alpha_0,1)}(C_0+2)$ , the lemma statement follows.

**Lemma 7.** For any k > 0, v,

$$[a_v, N^k] = a_v(N^k - (N-I)^k)$$
 and  $[a_v, N^k] = ((N+I)^k - N^k)a_v$ .

Furthermore, for any k > 0, v,

$$a_v^{\dagger} N^k a_v \leq n_v N^k$$
.

*Proof.* We begin by noting that, for any z, it follows from  $e^{zN}a_ve^{-zN}=e^{-z}a_v$  that

$$[a_v, e^{zN}] = a_v e^{zN} - e^{zN} a_v = a_v (e^{zN} - e^{z(N-I)}) = (e^{z(N+I)} - e^{zN}) a_v.$$
(S48)

We thus obtain that

$$[a_v, N^k] = \frac{d^k}{dz^k} [a_v, e^{zN}] \bigg|_{z=0} = a_v \left( N^k - (N-I)^k \right) = \left( (N+I)^k - N^k \right) a_v.$$
 (S49)

Furthermore, for any state  $|\psi\rangle = \sum_{\vec{n}} \psi_{\vec{n}} |\vec{n}\rangle$ , where  $\psi_{\vec{n}}$  is the amplitude of  $|\psi\rangle$  on the basis state  $|\vec{n}\rangle = |n_1, n_2 \dots n_m\rangle$ ,

$$\langle \psi | a_v^{\dagger} N^k a_v | \psi \rangle = \sum_{\vec{n}} |\psi_{\vec{n}}|^2 n_v (\|\vec{n}\|_1 - 1)^k \le \sum_{\vec{n}} |\psi_{\vec{n}}|^2 n_v \|\vec{n}\|_1^k = \langle \psi | n_v N^k | \psi \rangle, \tag{S50}$$

from which it follows that  $a_v^{\dagger} N^k a_v \leq n_v N^k$ .

In the next lemma, we derive an upper bound on  $\text{Tr}(N^k\rho(t))$ , which will be central to analyzing the Hilbert space truncation and Trotter bounds in the subsequent subsections.

**Lemma 8** (Upper bounding particle number moments). Consider a bosonic model satisfying assumption 2 with the bosonic modes in an initial state  $\rho(0)$  satisfying assumption 1, then,  $\forall t \geq 0$ ,

$$\operatorname{Tr}(N^k \rho(t)) \le (Cm)^k k^{\alpha k + \beta},$$

where  $C = e^{1+4\Omega^2/\gamma^2+2\mathcal{G}/\gamma+4(\kappa_1+\kappa_2)/\gamma}(C_0+2), \alpha = \max(\alpha_0,1)$  and  $\beta = \beta_0$  with  $C_0, \alpha_0, \beta_0$  defined in assumption 2.

*Proof.* We will use the Heisenberg equations of motion for the operator  $N^k$ . Note that  $[N^k, H_{ng}(t)] = 0$ ,  $[N^k, H_g^{hop}(t)] = 0$  and  $\mathcal{D}_{n_v}^{\dagger}(N^k) = 0$  (where  $H_g^{hop}(t)$  is defined in Eq. (S25)). Using notation  $\langle O \rangle_t = \text{Tr}(O\rho(t))$ , we then have that

$$\frac{d}{dt}\langle N^k \rangle_t = \underbrace{\sum_{v} \left( \kappa_1 \langle \mathcal{D}_{a_v}^{\dagger}(N^k) \rangle_t + \kappa_2 \langle \mathcal{D}_{a_v^{\dagger}}^{\dagger}(N^k) \rangle_t \right)}_{\langle \mathcal{L}_n^{\dagger}(N^k) \rangle_t} - i \langle [N^k, H_g^{\text{sq}}(t)] \rangle_t - i \langle [N^k, H_g^{\text{disp}}(t)] \rangle_t. \tag{S51}$$

Consider first  $\mathcal{D}_{a_v}^{\dagger}(N^k), \mathcal{D}_{a_v^{\dagger}}^{\dagger}(N^k)$ —using Lemma 7, we obtain that

$$\sum_{v} \mathcal{D}_{a_{v}}^{\dagger}(N^{k}) = -\sum_{v} a_{v}^{\dagger}[a_{v}, N^{k}] = -N(N^{k} - (N - I)^{k}) = -kN^{k} + \sum_{l \ge 1} (-1)^{l} \binom{k}{l+1} N^{k-l},$$

$$\sum_{v} \mathcal{D}_{a_{v}^{\dagger}}^{\dagger}(N^{k}) = \sum_{v} [a_{v}, N^{k}] a_{v}^{\dagger} = ((N + I)^{k} - N^{k})(N + I) = kN^{k} + \sum_{l \ge 1} \binom{k+1}{l+1} N^{k-l}.$$
(S52)

Therefore,

$$\langle \mathcal{L}_{n}^{\dagger}(N^{k})\rangle_{t} = -(\kappa_{1} - \kappa_{2})k\langle N^{k}\rangle_{t} + \sum_{l=1}^{k} \left(\kappa_{1}(-1)^{l} \binom{k}{l+1} + \kappa_{2} \binom{k+1}{l+1}\right) \langle N^{k-l}\rangle_{t}$$

$$\stackrel{(1)}{\leq} -(\kappa_{1} - \kappa_{2})k\langle N^{k}\rangle_{t} + \sum_{l=1}^{k} \left(\kappa_{1}k + \kappa_{2}(k+1)\right) \binom{k}{l} \langle N^{k-l}\rangle_{t}$$

$$\leq -(\kappa_{1} - \kappa_{2})k\langle N^{k}\rangle_{t} + 2(\kappa_{1} + \kappa_{2})km \sum_{l=1}^{k} 2^{l} \binom{k}{l} \langle N^{k-l}\rangle_{t}, \tag{S53}$$

where we implicitly set  $\binom{k}{l} = 0$  if l < 0 or l > k and in (1) we have used the fact that  $\binom{k}{l+1} \le k \binom{k}{l}, \binom{k+1}{l+1} \le (k+1) \binom{k}{l}$ .

Next, consider  $[N^k, H_g^{sq}(t)] = \sum_{v,u} \mathcal{G}_{v,u}(t)[N^k, a_v a_u] - \text{h.c.}$  we begin by noting that from Lemma 7

$$[N^k, a_v a_u] = -[a_v, N^k] a_u - a_v [a_u, N^k] = -2 \sum_{l>0} {k \choose 2l+1} a_v N^{k-2l-1} a_u,$$
 (S54)

and therefore

$$\begin{split} \left| \langle [N^k, H_{\mathbf{g}}^{\mathrm{sq}}(t)] \rangle_t \right| &\leq 2 \sum_{v,u} |\mathcal{G}_{v,u}(t)| |\langle [N^k, a_v a_u] \rangle_t | \\ &\stackrel{(1)}{\leq} 2 \sum_{v,u} \sum_{l \geq 0} |\mathcal{G}_{v,u}(t)| \begin{pmatrix} k \\ 2l+1 \end{pmatrix} |\langle a_v N^{k-2l-1} a_u \rangle_t | \\ &\stackrel{(2)}{\leq} \sum_{v,u} \sum_{l \geq 0} |\mathcal{G}_{v,u}(t)| \begin{pmatrix} k \\ 2l+1 \end{pmatrix} \left( |\langle a_v N^{k-2l-1} a_v^{\dagger} \rangle_t | + |\langle \mathrm{Tr}(a_u^{\dagger} N^{k-2l-1} a_u \rangle_t | \right) \\ &\leq \mathcal{G} \sum_{u} \sum_{l \geq 0} \begin{pmatrix} k \\ 2l+1 \end{pmatrix} \left( \langle a_u N^{k-2l-1} a_u^{\dagger} \rangle_t + \langle a_u^{\dagger} N^{k-2l-1} a_u \rangle_t \right) \\ &\stackrel{(3)}{\leq} \mathcal{G} \sum_{u} \sum_{l \geq 0} \begin{pmatrix} k \\ 2l+1 \end{pmatrix} \left( \langle (N+I)^{k-2l-1} a_u a_u^{\dagger} \rangle_t + \langle (N-I)^{k-2l-1} a_u^{\dagger} a_u \rangle_t \right) \\ &\leq 2\mathcal{G} \sum_{l,p \geq 0} \begin{pmatrix} k \\ 2l+1 \end{pmatrix} \begin{pmatrix} k-2l-1 \\ 2p \end{pmatrix} \langle N^{k-2l-2p} \rangle_t + 2\mathcal{G}m \sum_{l,p \geq 0} \begin{pmatrix} k \\ 2l+1 \end{pmatrix} \begin{pmatrix} k-2l-1 \\ p \end{pmatrix} \langle N^{k-2l-p-1} \rangle_t. \end{split} \tag{S55}$$

where, in (1), we have used Eq. (S54), in (2) we have used the fact that, for any two operators  $A, B, \langle AB \rangle \leq \sqrt{\langle AA^{\dagger} \rangle \langle B^{\dagger}B \rangle} \leq (\langle AA^{\dagger} \rangle + \langle B^{\dagger}B \rangle)/2$  and in (3) we have used Lemma 7. We can thus conclude that

$$\left| \langle [N^k, H_{\mathbf{g}}^{\mathrm{sq}}(t)] \rangle_t \right| \le 2\mathcal{G}k \langle N^k \rangle_t + 2\mathcal{G} \sum_{q > 1} f_q^{(k)} \langle N^{k-q} \rangle_t, \tag{S56}$$

where

$$f_q^{(k)} = \begin{cases} m \sum_{l \ge 0} {k \choose 2l+1} {k-(2l+1) \choose q-(2l+1)} & \text{if } q \in \{1,3,5\dots\}, \\ m \sum_{l \ge 0} {k \choose 2l+1} {k-(2l+1) \choose q-(2l+1)} + \sum_{l \ge 0} {k \choose 2l+1} {k-(2l+1) \choose q-2l} & \text{if } q \in \{2,4,6\dots\}. \end{cases}$$
(S57)

The expression for  $f_q^{(k)}$  can be further simplified by noting that

$$\sum_{l>0} {k \choose 2l+1} {k-(2l+1) \choose q-(2l+1)} = \sum_{l>0} \frac{k!}{(2l+1)!(k-q)!(q-(2l+1))!} = {k \choose q} \sum_{l>0} {q \choose 2l+1} = 2^{q-1} {k \choose q}, \quad (S58)$$

and

$$\sum_{l>0} \binom{k}{2l+1} \binom{k-(2l+1)}{q-2l} = \sum_{l>0} \frac{k!}{(2l+1)!(k-q-1)!(q-2l)!} = \binom{k}{q+1} \sum_{l>0} \binom{q+1}{2l+1} = 2^q \binom{k}{q+1}.$$
 (S59)

We then obtain that

$$f_q^{(k)} = \begin{cases} 2^{q-1} m \binom{k}{q} & \text{if } q \in \{1, 3, 5 \dots\}, \\ 2^{q-1} m \binom{k}{q} + 2^q \binom{k}{q+1} & \text{if } q \in \{2, 4, 6 \dots\}. \end{cases}$$
(S60)

Again, we note that, since  $\binom{k}{q+1} \le k \binom{k}{q}$ , it follows that  $f_q^{(k)} \le 2^{q-1}(m+2k) \binom{k}{q} \le mk2^q \binom{k}{q}$ , and thus we obtain that

$$\left| \langle [N^k, H_{\mathbf{g}}^{\mathrm{sq}}(t)] \rangle_t \right| \le 2\mathcal{G}k \langle N^k \rangle_t + mk\mathcal{G} \sum_{q > 1} \binom{k}{q} 2^q \langle N^{k-q} \rangle_t. \tag{S61}$$

Finally, we consider  $[N^k, H_{\rm g}^{\rm disp}(t)] = \sum_v \mathcal{D}_v(t)[N^k, a_v] - {\rm h.c.}$ —we begin by noting that, from Lemma 7,

$$[N^k, a_v] = ((N+I)^k - N^k) = \sum_{q>1} {k \choose q} N^{k-q} a_v,$$
 (S62)

and therefore

$$\left| \langle [N^{k}, H_{2}(t)] \rangle_{t} \right| \leq 2\Omega \sum_{v} \sum_{q \geq 1} {k \choose q} \left| \langle N^{k-q} a_{v} \rangle_{t} \right|$$

$$\stackrel{\text{(1)}}{\leq} \sum_{v} \sum_{q \geq 1} {k \choose q} \sqrt{\gamma \langle a_{v}^{\dagger} N^{k-q} a_{v} \rangle_{t} \times \frac{4\Omega^{2}}{\gamma} \langle N^{k-q} \rangle_{t}}$$

$$\leq \sum_{v} \sum_{q \geq 1} {k \choose q} \left( \frac{\gamma}{2} \langle a_{v}^{\dagger} N^{k-q} a_{v} \rangle_{t} + \frac{2\Omega^{2}}{\gamma} \langle N^{k-q} \rangle_{t} \right)$$

$$\stackrel{\text{(2)}}{\leq} \sum_{v} \sum_{q \geq 1} {k \choose q} \left( \frac{\gamma}{2} \langle N^{k-q} n_{v} \rangle_{t} + \frac{2\Omega^{2}}{\gamma} \langle N^{k-q} \rangle_{t} \right)$$

$$\leq \frac{\gamma}{2} k \langle N^{k} \rangle_{t} + \sum_{q \geq 1} \left( \frac{\gamma}{2} {k \choose q+1} + \frac{2m\Omega^{2}}{\gamma} {k \choose q} \right) \langle N^{k-q} \rangle_{t}$$

$$\stackrel{\text{(3)}}{\leq} \frac{\gamma}{2} k \langle N^{k} \rangle_{t} + \sum_{q \geq 1} \left( \frac{\gamma}{2} k + \frac{2m\Omega^{2}}{\gamma} \right) {k \choose q} \langle N^{k-q} \rangle_{t}, \tag{S63}$$

where, in (1), we have again used that  $\langle AB \rangle \leq \sqrt{\langle AA^{\dagger} \rangle \langle B^{\dagger}B \rangle}$  and introduced the parameter  $\gamma = \kappa_1 - \kappa_2 - 2\mathcal{G}$  from assumption 2, in (2) we have used Lemma 7 to obtain that  $\langle a_v^{\dagger} N^{k-q} a_v \rangle \leq \langle N^{k-q} n_v \rangle$ , and in (3) we have used the fact that  $\binom{k}{q+1} \leq k \binom{k}{q}$ . Setting  $k, m \leq km$ , we obtain that

$$\left| \langle [N^k, H_{\mathbf{g}}^{\mathrm{disp}}(t)] \rangle_t \right| \le \frac{\gamma}{2} k \langle N^k \rangle_t + mk \left( \frac{\gamma}{2} + \frac{2\Omega^2}{\gamma} \right) \sum_{q \ge 1} \binom{k}{q} \langle N^{k-q} \rangle_t. \tag{S64}$$

Combining Eq. (S51) with Eqs. (S53, S61, S64), we obtain that

$$\frac{d}{dt}\langle N^k \rangle_t \le -\frac{\gamma}{2} k \langle N^k \rangle_t + \lambda k m \sum_{q>1} \left(\frac{k}{q}\right) \langle N^{k-q} \rangle_t, \tag{S65}$$

where  $\lambda = \gamma/2 + 2\Omega^2/\gamma + \mathcal{G} + 2(\kappa_1 + \kappa_2)$ . Then, solving this inequality using Lemma 6, we obtain the lemma statement.

Combining this lemma with Lemma 5, we straightforwardly obtain the following lemma upper bounding the probability of large number of excitations at any time in the bosonic model.

**Lemma 9.** Suppose  $\Pi_{\geq d}$  is a projector on the subspace with  $\geq d$  particles and the bosonic model satisfies assumptions 1 and 2, then for any  $t \geq 0$ ,

$$\operatorname{Tr}(\Pi_{\geq d}\rho(t)) \leq e\left(\frac{d}{d_0m}\right)^{k_0} \exp\left(-\left(\frac{d}{d_0m}\right)^{1/\alpha}\right),$$

where  $d_0 = eC$ ,  $k_0 = \beta/\alpha$  with  $C, \alpha, \beta$  being defined in Lemma 8.

## B. Proof of Theorem 2 (bosons)

The proof of Theorem 2 has three main parts:

(1) Truncation of the Hilbert space of the bosonic model to a finite-dimensional space and an analysis of the truncation error (Lemma 11).

- (2) First-order Trotterization of the truncated finite-dimensional model (Lemma 12).
- (3) Analysis of each Trotter step to establish high-noise separability (Lemma 13).

Truncation of the bosonic model. Suppose we want to truncate the local Hilbert space of each bosonic mode to d levels—we will denote by  $\mathcal{H}_{\leq d}$  the Hilbert space of the bosonic model with each bosonic mode truncated to at most d particles. For the  $v^{\text{th}}$  bosonic mode, we will define the projectors  $\Pi_{v,d}, \Pi_{v,\leq d}$ , and  $\Pi_{v,>d}$  via

$$\Pi_{v,d} = |d\rangle\langle d|, \Pi_{v,\leq d} = \sum_{j=0}^{d} \Pi_{v,j}, \text{ and } \Pi_{v,>d} = \sum_{j=d+1}^{\infty} \Pi_{v,j}.$$
 (S66)

We will define the projector  $\Pi_{\leq d} = \otimes_v \Pi_{v, \leq d}$ , which will be the projector onto  $\mathcal{H}_{\leq d}$ . The truncated model will be described by a Lindbladian  $\mathcal{L}_{\leq d}(t)$  while

$$\mathcal{L}_{\leq d} = -i[H_{\leq d}, \cdot] + \sum_{l=1}^{3} \sum_{v} \kappa_{l} \mathcal{D}_{L_{v, \leq d}^{(l)}}, \tag{S67a}$$

where

$$\begin{split} H_{\leq d}(t) &= \Pi_{\leq d} H(t) \Pi_{\leq d}, \\ L_{v,\leq d}^{(1)} &= a_{v,\leq d} = \Pi_{v,\leq d} a_v \Pi_{v,\leq d}, \\ L_{v,\leq d}^{(2)} &= a_{v,\leq d}^{\dagger} = \Pi_{v,\leq d} a_v^{\dagger} \Pi_{v,\leq d}, \\ L_{v,\leq d}^{(3)} &= n_{v,\leq d} = \Pi_{v,\leq d} n_v \Pi_{v,\leq d}. \end{split} \tag{S67b}$$

It will be convenient to define super-operators  $\mathcal{P}_{\leq d}$  and  $\mathcal{Q}_{\leq d}$  via

$$\mathcal{P}_{\leq d}(\rho) = \prod_{\leq d} \rho \prod_{\leq d} \text{ and } \mathcal{Q}_{\leq d} = \text{id} - \mathcal{P}_{\leq d}.$$
 (S68)

The super-operator  $\mathcal{P}_{\leq d}$  projects an input density matrix onto  $\mathcal{H}_{\leq d}$ . We first present a lemma that quantifies the error between the state  $\rho(t)$  at time t and the state obtained from the truncated evolution:  $\rho_{\leq d}(t) = \mathcal{T} \exp(\int_0^t \mathcal{L}_{\leq d}(\tau)d\tau)(\mathcal{P}_{\leq d}\rho(0))$ .

**Lemma 10.** For any d > 0, it follows that

$$\begin{split} \left\| \rho(t) - \mathcal{T} \exp\left( \int_0^t \mathcal{L}_{\leq d}(\tau) d\tau \right) (\mathcal{P}_{\leq d} \rho(0)) \right\|_1 \\ &\leq \left\| \mathcal{Q}_{\leq d} \rho(t) \right\|_1 + (d+1) \sum_v \int_0^t \left\| \Pi_{v,d} \rho(s) \right\|_1 ds + \int_0^t \left\| \mathcal{P}_{\leq d} \mathcal{L}(s) \mathcal{Q}_{\leq d} \right\|_{\diamond} \left\| \mathcal{Q}_{\leq d} \rho(s) \right\|_1 ds. \end{split}$$

*Proof.* Using  $\mathcal{P}_{\leq d} + \mathcal{Q}_{\leq d} = \text{id together with the master equation } (d\rho(t)/dt = \mathcal{L}(t)\rho(t))$ , we obtain that

$$\frac{d}{dt}\mathcal{P}_{\leq d}\rho(t) = \mathcal{P}_{\leq d}\mathcal{L}(t)\mathcal{P}_{\leq d}\rho(t) + \mathcal{P}_{\leq d}\mathcal{L}(t)\mathcal{Q}_{\leq d}\rho(t), \tag{S69a}$$

$$\frac{d}{dt}\mathcal{Q}_{\leq d}\rho(t) = \mathcal{Q}_{\leq d}\mathcal{L}(t)\mathcal{P}_{\leq d}\rho(t) + \mathcal{Q}_{\leq d}\mathcal{L}(t)\mathcal{Q}_{\leq d}\rho(t). \tag{S69b}$$

Furthermore, we note that, for any operator X that is supported on the truncated subspace  $\mathcal{H}_d$  (i.e.  $X = \prod_{\leq d} X \prod_{\leq d}$ ), and defining  $H_{\leq d}(t) = \prod_{\leq d} H(t) \prod_{\leq d}$ , we have

$$\mathcal{P}_{\leq d}\mathcal{L}\mathcal{P}_{\leq d}(X) = -i[H_{\leq d}(t), X] + \prod_{\leq d} \mathcal{L}_n \prod_{\leq d} (X), \tag{S70}$$

$$\mathcal{P}_{\leq d} \mathcal{D}_{a_v} \mathcal{P}_{\leq d}(X) = \Pi_{v, \leq d} a_v \Pi_{v, \leq d} X \Pi_{v, \leq d} a_v^{\dagger} \Pi_{v, \leq d} - \frac{1}{2} \left( \Pi_{v, \leq d} n_v \Pi_{v, \leq d} X + X \Pi_{v, \leq d} n_v \Pi_{v, \leq d} \right)$$

$$= a_{v, \leq d} X a_{v, \leq d}^{\dagger} - \frac{1}{2} \left( a_{v, \leq d}^{\dagger} a_{v, \leq d} X + X a_{v, \leq d}^{\dagger} a_{v, \leq d} \right)$$

$$= \mathcal{D}_{a_{v, \leq d}}(X), \tag{S71a}$$

$$\mathcal{P}_{\leq d} \mathcal{D}_{a_v^{\dagger}} \mathcal{P}_{\leq d}(X) = \Pi_{v,\leq d} a_v^{\dagger} \Pi_{v,\leq d} X \Pi_{v,\leq d} a_v \Pi_{v,\leq d} - \frac{1}{2} \left( \Pi_{v,\leq d} a_v a_v^{\dagger} \Pi_{v,\leq d} X + X \Pi_{v,\leq d} a_v a_v^{\dagger} \Pi_{v,\leq d} \right)$$

$$= a_{v,\leq d}^{\dagger} X a_{v,\leq d} - \frac{1}{2} \left( a_{v,\leq d} a_{v,\leq d}^{\dagger} X + X a_{v,\leq d} a_{v,\leq d}^{\dagger} \right) - \frac{d+1}{2} \left( \Pi_{v,d} X + X \Pi_{v,d} \right)$$

$$= \mathcal{D}_{a_v^{\dagger},\leq d}(X) - \frac{d+1}{2} \left( \Pi_{v,d} X + X \Pi_{v,d} \right), \tag{S71b}$$

$$\mathcal{P}_{\leq d} \mathcal{D}_{n_{v}} \mathcal{P}_{\leq d}(X) = \prod_{v, \leq d} n_{v} \prod_{v, \leq d} X \prod_{v, \leq d} n_{v}^{2} \prod_{v, \leq d} - \frac{1}{2} \left( \prod_{v, \leq d} n_{v}^{2} \prod_{v, \leq d} X + X \prod_{v, \leq d} n_{v}^{2} \prod_{v, \leq d} \right)$$

$$= n_{v, \leq d} X n_{v, \leq d} - \frac{1}{2} \left( n_{v, \leq d}^{2} X + X n_{v, \leq d}^{2} \right)$$

$$= \mathcal{D}_{n_{v, \leq d}}(X). \tag{S71c}$$

Defining  $\mathcal{L}_{n,\leq d} = \sum_{v} \left( \kappa_1 \mathcal{D}_{a_{v,\leq d}} + \kappa_2 \mathcal{D}_{a_{v,\leq d}^{\dagger}} + \kappa_3 \mathcal{D}_{n_{v,\leq d}} \right)$ , we then obtain that,  $\forall X \in \mathcal{H}_{\leq d}$ .

$$\mathcal{P}_{\leq d}\mathcal{L}(t)\mathcal{P}_{\leq d}(X) = \mathcal{L}_{\leq d}(t)(X) - \frac{d+1}{2} \sum_{v} \left( \Pi_{v,d} X + X \Pi_{v,d} \right). \tag{S72}$$

Consequently, from Eq. (S69a), we obtain that

$$\frac{d}{dt}\mathcal{P}_{\leq d}\rho(t) = \mathcal{L}_{\leq d}(t)\mathcal{P}_{\leq d}\rho(t) + \mathcal{P}_{\leq d}\mathcal{L}(t)\mathcal{Q}_{\leq d}\rho(t) - \frac{d+1}{2}\sum_{v}\left(\Pi_{v,d}\mathcal{P}_{\leq d}\rho(t) + (\mathcal{P}_{\leq d}\rho(t))\Pi_{v,d}\right),\tag{S73}$$

which can be integrated to obtain

$$\mathcal{P}_{\leq d}\rho(t) = \mathcal{E}_{\leq d}(t,0)\mathcal{P}_{\leq d}\rho(0) + \int_{0}^{t} \mathcal{E}_{\leq d}(t,s) \left(\mathcal{P}_{\leq d}\mathcal{L}(s)\mathcal{Q}_{\leq d}\rho(s) - \frac{d+1}{2}\sum_{v} \left(\Pi_{v,d}\mathcal{P}_{\leq d}\rho(s) + (\mathcal{P}_{\leq d}\rho(s))\Pi_{v,d}\right)\right) ds, \tag{S74}$$

where  $\mathcal{E}_{\leq d}(t,s) = \mathcal{T} \exp(\int_s^t \mathcal{L}_{\leq d}(\tau) d\tau)$ . From here, it immediately follows that

$$\|\mathcal{E}_{\leq d}(t,0)\mathcal{P}_{\leq d}\rho(0) - \rho(t)\|_{1}$$

$$\leq \|\rho_{\leq d}(t) - \mathcal{P}_{\leq d}\rho(t)\|_{1} + \|\mathcal{Q}_{\leq d}\rho(t)\|_{1}$$

$$\leq (d+1)\sum_{v} \int_{0}^{t} \|\Pi_{v,d}\mathcal{P}_{\leq d}\rho(s)\|_{1} ds + \int_{0}^{t} \|\mathcal{P}_{\leq d}\mathcal{L}(s)\mathcal{Q}_{\leq d}\rho(s)\|_{1} ds + \|\mathcal{Q}_{\leq d}\rho(t)\|_{1}$$

$$\stackrel{(1)}{\leq} (d+1)\sum_{v} \int_{0}^{t} \|\Pi_{v,d}\rho(s)\|_{1} ds + \int_{0}^{t} \|\mathcal{P}_{\leq d}\mathcal{L}(s)\mathcal{Q}_{\leq d}\rho(s)\|_{1} ds + \|\mathcal{Q}_{\leq d}\rho(t)\|_{1} .$$
(S76)

where, in (1), we have used the fact that  $\Pi_{v,d}\Pi_{\leq d} = \Pi_{\leq d}\Pi_{v,d}$  to set  $\|\Pi_{v,d}\mathcal{P}_{\leq d}\rho(s)\|_1 = \|\Pi_{\leq d}\Pi_{v,d}\rho(s)\Pi_{\leq d}\|_1 \leq \|\Pi_{\leq d}\|\|\Pi_{v,d}\rho(s)\|_1 \|\Pi_{\leq d}\| = \|\Pi_{v,d}\rho(s)\|_1$ ,

Finally, combining Lemma 10 with Lemmas 5 and 8, we obtain the next lemma quantifying the truncation error as a function of d.

**Lemma 11.** For any  $d \ge 1$ , it follows that

$$\left\| \rho(t) - \mathcal{T} \exp\left( \int_0^t \mathcal{L}_{\leq d}(s) ds \right) \mathcal{P}_{\leq d} \rho(0) \right\|_1 \leq O\left( m^{1 - k_0/2} d^{2 + k_0/2} t (J_C + J_{os} + U_C + U_{os} + \kappa) e^{-\frac{1}{2} (d/d_0 m)^{1/\alpha}} \right),$$

where  $d_0, k_0, \alpha$  are the constants in Lemma 9.

Proof. We bound each term in Lemma 10. We first note that

$$\|\mathcal{Q}_{\leq d}\rho(t)\|_{1} = \|\Pi_{>d}\rho(t) + \Pi_{\leq d}\rho(t)\Pi_{>d}\|_{1} \\ \leq \|\Pi_{>d}\rho(t)\|_{1} + \|\Pi_{\leq d}\rho(t)\Pi_{>d}\|_{1} \\ \leq \sqrt{\text{Tr}(\Pi_{>d}\rho(t))} + \sqrt{\text{Tr}(\Pi_{\leq d}\rho(t))\text{Tr}(\Pi_{>d}\rho(t))} \\ \leq 2\sqrt{\text{Tr}(\Pi_{\geq d}\rho(t))} \leq 2\sqrt{e} \left(\frac{d}{d_{0}m}\right)^{k_{0}/2} \exp\left(-\frac{1}{2}\left(\frac{d}{d_{0}m}\right)^{1/\alpha}\right), \tag{S77}$$

where, in (1), we have used the Holder's inequality to conclude that  $||A\rho(t)B||_1 \leq \sqrt{\text{Tr}(A^{\dagger}A\rho(t))\text{Tr}(B^{\dagger}B\rho(t))}$ . Furthermore,

$$\|\Pi_{v,d}\rho(t)\| \le \sqrt{\text{Tr}(\Pi_{v,d}\rho(t))} \le \sqrt{\text{Tr}(\Pi_{\ge d}\rho(t))} \le \sqrt{e} \left(\frac{d}{d_0 m}\right)^{k_0/2} \exp\left(-\frac{1}{2}\left(\frac{d}{d_0 m}\right)^{1/\alpha}\right). \tag{S78}$$

Finally, we consider upper-bounding  $\|\mathcal{P}_{\leq d}\mathcal{L}(s)\mathcal{Q}_{\leq d}\|_1 \leq \|\mathcal{P}_{\leq d}\mathcal{L}(s)\mathcal{P}_{\leq d}\|_{\diamond} + \|\mathcal{P}_{\leq d}\mathcal{L}(s)\|_{\diamond} \leq 2\|\mathcal{P}_{\leq d}\mathcal{L}(s)\|_{\diamond}$ , where we have used the fact that  $\|\mathcal{P}_{\leq d}\|_{\diamond} \leq 1$ . Next, we note that, for a Hamiltonian H and jump operator L,

$$\|\mathcal{P}_{\leq d}[H, \cdot]\|_{\diamond} \le 2\|\Pi_{\leq d}H\| \text{ and } \|\mathcal{P}_{\leq d}\mathcal{D}_{L}\|_{\diamond} \le \|\Pi_{\leq d}L\|^{2} + \|\Pi_{\leq d}L^{\dagger}L\|.$$
 (S79)

Furthermore, since

$$\|\Pi_{\leq d} a_v\|, \|\Pi_{\leq d} a_v^{\dagger}\| \leq \sqrt{d+1}, \|\Pi_{\leq d} a_v^{\dagger} a_u\| \leq d \text{ and } \|\Pi_{\leq d} a_v a_u\|, \|\Pi_{\leq d} a_v^{\dagger} a_u^{\dagger}\| \leq d+2, \tag{S80}$$

we obtain

$$\|\mathcal{P}_{\leq d}[\cdot, H(t)]\|_{\diamond} \leq 2\|\Pi_{\leq d}H_{g}^{\text{hop}}(t)\|_{\diamond} + 2\|\Pi_{\leq d}H_{g}^{\text{sq}}(t)\|_{\diamond} + 2\|\Pi_{\leq d}H_{g}^{\text{disp}}(t)\|_{\diamond} + 2\|\Pi_{\leq d}H_{g}^{\text{ng}}(t)\|$$

$$\leq 4d\sum_{v,u}|\mathcal{J}_{v,u}| + 4(d+2)\sum_{v,u}|\mathcal{G}_{v,u}| + 4\sqrt{d+1}\sum_{v}|\mathcal{D}_{v,u}(t)| + 4d^{2}\sum_{v,u}|U_{v,u}|$$

$$\leq 4(d+1)m(J_{\text{os}} + J_{C}) + 2\sqrt{2(d+1)}\Omega + 4d^{2}(U_{C} + U_{\text{os}})$$

$$\leq 8m(d(J_{\text{os}} + J_{C}) + \sqrt{d}|\Omega| + d^{2}(U_{C} + U_{\text{os}}). \tag{S81}$$

where we have used the decomposition of  $H_{\rm g}(t)$  in Eq. (S25). Furthermore,

$$\|\mathcal{P}_{\leq d}\mathcal{L}_{\mathbf{n}}\| \leq \sum_{v} \left( \kappa_{1} \|\mathcal{P}_{\leq d}\mathcal{D}_{a_{v}}\|_{\diamond} + \kappa_{2} \|\mathcal{P}_{\leq d}\mathcal{D}_{a_{v}^{\dagger}}\|_{\diamond} + \kappa_{3} \|\mathcal{P}_{\leq d}\mathcal{D}_{a_{v}^{\dagger}a_{v}}\|_{\diamond} \right)$$

$$\leq m \left( \kappa_{1}(2d+1) + \kappa_{2}(2d+2) + \kappa_{3}d^{2} \right)$$

$$\leq 8m \left( (\kappa_{1} + \kappa_{2})d + \kappa_{3}d^{2} \right). \tag{S82}$$

Combining Eqs. (S81) and (S82), we obtain that

$$\|\mathcal{P}_{\leq d}\mathcal{L}(s)\mathcal{Q}_{\leq d}\|_{\diamond} \leq 2\|\mathcal{P}_{\leq d}\mathcal{L}(s)\|_{\diamond} \leq 16m((J_{\text{os}} + J_{C} + (\kappa_{1} + \kappa_{2}))d + \Omega\sqrt{d} + (U_{C} + U_{\text{os}} + \kappa_{3})d^{2})$$

$$\leq 16md^{2}(J_{\text{os}} + J_{C} + \Omega + U_{\text{os}} + U_{C} + \kappa). \tag{S83}$$

Finally, combining Eqs. (S77, S78, S83) together with Lemmas 10 and 9, we obtain the lemma.

Trotterization of the truncated model. We will perform a first-order Trotterization of the state  $\rho_{\leq d}(t) = \mathcal{T} \exp(\int_0^t \mathcal{L}_{\leq d}(s)ds)\mathcal{P}_{\leq d}(\rho(0))$ . We will split the Hamiltonian  $H_{\leq d}(t)$  into a sum of inter-site terms  $H_{\leq d}^{\mathbf{C}}(t)$  and a sum of on-site terms  $H_{\leq d}^{\mathbf{cs}}(t)$ :

$$H_{\leq d}(t) = \underbrace{\sum_{i < j} \sum_{\sigma, \sigma'} h_{i, \sigma; j, \sigma'}^{C}(t)}_{H_{\leq d}^{C}(t)} + \underbrace{\sum_{i} \sum_{\sigma, \sigma'} h_{i; \sigma, \sigma'}^{os}(t)}_{H_{\leq d}^{ss}(t)}, \tag{S84}$$

where, in  $h_{i,\sigma;j,\sigma'}^{C}(t)$  we include all the terms that mediate an interaction between  $(i,\sigma)$  and  $(j,\sigma')$ :

$$h_{i,\sigma;j,\sigma'}^{C}(t) = \prod_{\leq d} \left( U_{i,\sigma;j,\sigma'}(t) n_{i,\sigma} n_{j,\sigma'} + \sum_{\alpha,\alpha'} J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t) c_{i,\sigma}^{\alpha} c_{j,\sigma'}^{\alpha'} \right) \prod_{\leq d} + (i,\sigma) \leftrightarrow (j,\sigma')$$

$$= 2U_{i,\sigma;j,\sigma'}(t) n_{i,\sigma;\leq d} n_{j,\sigma';\leq d} + 2 \sum_{\alpha,\alpha'} J_{i,\sigma;j',\sigma'}(t) c_{i,\sigma;\leq d}^{\alpha} c_{j,\sigma';\leq d}^{\alpha'}, \tag{S85}$$

where  $c_{i,\sigma;\leq d}^1=(a_{i,\sigma;\leq d}+a_{i,\sigma;\leq d}^\dagger)/\sqrt{2},$   $c_{i,\sigma;\leq d}^2=(a_{i,\sigma;\leq d}-a_{i,\sigma;\leq d}^\dagger)/\sqrt{2}i.$  In  $h_{i;\sigma,\sigma'}^{\text{os}}(t)$ , we include all the terms (Gaussian or non-Gaussian) that act between modes  $(i,\sigma)$  and  $(i,\sigma')$ :

$$h_{i;\sigma,\sigma'}^{\text{os}}(t) = \Pi_{\leq d} \left( U_{i,\sigma;i,\sigma'}(t) n_{i,\sigma} n_{i,\sigma'} + \sum_{\alpha,\alpha'} J_{i,\sigma;i,\sigma'}^{\alpha,\alpha'}(t) c_{i,\sigma}^{\alpha} c_{i,\sigma'}^{\alpha'} \right) \Pi_{\leq d}$$

$$= U_{i,\sigma;i,\sigma'}(t) n_{i,\sigma;\leq d} n_{i,\sigma';\leq d} + \sum_{\alpha,\alpha'} J_{i,\sigma;i',\sigma'}^{\alpha,\alpha'}(t) \Pi_{i,\sigma;\leq d} \Pi_{i,\sigma';\leq d} c_{i,\sigma}^{\alpha} c_{i',\sigma'}^{\alpha'} \Pi_{i,\sigma;\leq d} \Pi_{i,\sigma';\leq d}. \tag{S86}$$

Furthermore, we will also decompose the dissipation  $\mathcal{L}_{n,\leq d}$ :

$$\mathcal{L}_{\mathbf{n},\leq d} = \sum_{i < j} \sum_{\sigma,\sigma'} \mathcal{L}_{i,\sigma;j,\sigma'}^{\mathbf{n}}(t) \text{ where } \mathcal{L}_{i,\sigma;j,\sigma'}^{\mathbf{n}}(t) = \sum_{l=1}^{3} \kappa_l \left( p_{i,\sigma;j,\sigma'}^{(l)}(t) \mathcal{D}_{L_{i,\sigma,\leq d}}^{(l)} + q_{i,\sigma;j,\sigma'}^{(l)}(t) \mathcal{D}_{L_{j,\sigma',\leq d}}^{(l)} \right), \tag{S87}$$

where we will choose  $p_{i,\sigma;i',\sigma'}^{(l)}(t), q_{i,\sigma;i',\sigma'}^{(l)}(t) \geq 0$  later. For this decomposition of  $\mathcal{L}_{n,\leq d}$  to be consistent, we must also have

$$\forall k, \sigma : \sum_{k' > k} \sum_{\sigma'} p_{k,\sigma;k',\sigma'}^{(l)}(t) + \sum_{k' < k} \sum_{\sigma'} q_{k',\sigma';k,\sigma}^{(l)}(t) = 1.$$
 (S88)

Now, the state of the truncated model at time t,  $\rho_{\leq d}(t)$ , will be approximated by the state  $\sigma_{T,\leq d}$ , where T is the number of Trotter steps and

$$\sigma_{T,\leq d} = \prod_{\tau=T}^{1} \left( \prod_{i < j} \prod_{\sigma,\sigma'} \Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'} \right) \mathcal{U}_{\tau\delta,(\tau-1)\delta}^{\text{os}} \rho_{\leq d}(0), \tag{S89a}$$

where  $\delta = t/T$ ,

$$\Phi_{t,t'}^{i,\sigma;j,\sigma'} = \mathcal{T} \exp\left(\int_{t'}^{t} \mathcal{L}_{i,\sigma;j,\sigma'}^{C}(s)ds\right) \text{ where } \mathcal{L}_{i,\sigma;j,\sigma'}^{C}(s) = -i[h_{i,\sigma;j,\sigma'}^{C}(s), \cdot] + \mathcal{L}_{i,\sigma;j,\sigma'}^{n}(s),$$
(S89b)

and

$$\mathcal{U}_{\tau\delta,(\tau-1)\delta}^{\text{os}} = U_{\tau\delta,(\tau-1)\delta}^{\text{os}}(\cdot)U_{\tau\delta,(\tau-1)\delta}^{\text{os}\dagger} \text{ where } U_{\tau\delta,(\tau-1)\delta}^{\text{os}} = \mathcal{T}\exp\bigg(-i\int_{(\tau-1)\delta}^{\tau\delta} H^{\text{os}}(s)ds\bigg). \tag{S89c}$$

The next lemma provides an upper bound on the Trotter error  $\|\rho_{\leq d}(t) - \sigma_{T,\leq d}\|_1$ .

**Lemma 12.** For any T > 0 and  $d \ge 1$ :

$$\left\|\sigma_{T,\leq d}-\rho_{\leq d}(t)\right\|_1\leq \frac{16t^2m^2d^4\Lambda^2}{T}.$$

*Proof.* This lemma follows from an application of Lemma 2: We note that

$$\|\mathcal{L}_{i,\sigma;j,\sigma'}^{C}(s)\|_{\diamond} \leq 2\|h_{i,\sigma;j,\sigma'}^{C}(s)\| + 2\sum_{l=1}^{3} \kappa_{l} \left(p_{i,\sigma;j,\sigma'}^{(l)}(s)\|L_{i,\sigma,\leq d}^{(l)}\|^{2} + q_{i,\sigma;j,\sigma'}^{(l)}(s)\|L_{j,\sigma',\leq d}^{(l)}\|^{2}\right)$$

$$\stackrel{\text{(1)}}{\leq} \left(4|U_{i,\sigma;j,\sigma'}(s)| + 8\sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(s)| + 2\sum_{l=1}^{3} \kappa_{l} \left(p_{i,\sigma;j,\sigma'}^{(l)}(s) + q_{i,\sigma;j,\sigma'}^{(l)}(s)\right)\right) d^{2}, \tag{S90}$$

$$\|[\cdot, H^{\text{os}}(t)]\|_{\diamond} \le 2 \sum_{i, j, -l'} \|h_{i; \sigma, \sigma'}^{\text{os}}(t)\|$$

$$\stackrel{\text{(2)}}{\leq} \left( 2 \sum_{i,\sigma,\sigma'} |U_{i,\sigma;i,\sigma'}(s)| + 4 \sum_{i,\sigma,\sigma'} \sum_{\alpha,\alpha'} |J_{i,\sigma;i,\sigma'}^{\alpha,\alpha'}(s)| \right) d^2, \tag{S91}$$

where, in (1) and (2), we have used the fact that, for the truncated bosonic model,  $\|c_{i,\sigma,\leq d}^{\alpha}\| \leq \sqrt{2d} \leq \sqrt{2d}$ ,  $\|n_{i,\sigma,\leq d}\| \leq d$ ,  $\|L_{i,\sigma,\leq d}^{(1)}\|$ ,  $\|L_{i,\sigma,\leq d}^{(2)}\|$ ,  $\|L_{i,\sigma,\leq d}^{(2)}\| \leq d$  and  $\|L_{i,\sigma,\leq d}^{(3)}\| \leq d$ . We can now estimate the parameter  $\ell$  from Lemma 2:  $\ell$  would be an upper bound on

$$\|[\cdot, H^{os}(s)]\|_{\diamond} + \sum_{j,i < j} \sum_{\sigma,\sigma'} \|\mathcal{L}_{i,\sigma;j,\sigma'}^{C}(s)\|_{\diamond}$$

$$\leq \left(4\sum_{i,j} \sum_{\sigma,\sigma'} \left(|U_{i,\sigma;j,\sigma'}(s)| + \sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}|\right) + 2\sum_{i,j:i < j} \sum_{\sigma,\sigma'} \sum_{l=1}^{3} \kappa_{l}(p_{i,\sigma;j,\sigma'}^{(l)}(s) + q_{i,\sigma;j,\sigma'}^{(l)}(s))\right)d^{2}$$

$$\leq \underbrace{4(U_{C} + U_{os} + J_{C} + J_{os} + \kappa)md^{4}}_{\varrho}.$$
(S92)

Thus, from Lemma 2, we obtain that  $\|\sigma_{T,\leq d} - \rho_{\leq d}(t)\|_1 \leq 16t^2m^2d^2(U_C + U_{os} + J_C + J_{os} + \kappa)^2/T$ .

**Lemma 13** (Separability condition for the bosonic model). Consider the following Lindbladian  $\mathcal{L}_{\leq d}(t)$  on two bosonic modes truncated to  $d \geq 1$  particles each:

$$\mathcal{L}_{\leq d}(t) = -i[h_{\mathrm{g},\leq d}(t) + h_{\mathrm{ng},\leq d}(t), \cdot] + \sum_{i \in \{1,2\}} \sum_{l=1}^{3} \kappa_{i}^{(l)}(t) \mathcal{D}_{L_{i,\leq d}^{(l)}},$$

where

$$h_{\mathrm{g},\leq d}(t) = \sum_{\alpha,\beta\in\{1,2\}} g_{\alpha,\beta}(t) c_{1,\leq d}^{\alpha} c_{2,\leq d}^{\beta}, h_{\mathrm{ng},\leq d}(t) = u(t) n_{1,\leq d} n_{2,\leq d}, \ L_i^{(1)} = a_{i,\leq d}, L_i^{(2)} = a_{i,\leq d}^{\dagger} \ \ and \ L_i^{(3)} = n_{i,\leq d}, L_i^{(3)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i^{(4)} = n_{i,\leq d}, L_i$$

where  $c_{i,\leq d}^1 = (a_{\leq d} + a_{\leq d}^{\dagger})/\sqrt{2}$ ,  $c_{i,\leq d}^2 = (a_{\leq d} - a_{\leq d}^{\dagger})/\sqrt{2}i$  and  $g_{\alpha,\beta}(t), u(t)$  are real and  $\kappa_i^{(l)}(t) \geq 0$ . If

(C1)
$$\kappa_i^{(1)}(t), \kappa_i^{(2)}(t) \ge \sum_{\alpha, \beta} |g_{\alpha, \beta}(t)|$$
 and

(C2)
$$\kappa_i^{(3)}(t) \ge |u(t)|,$$

then there is a completely-positive map  $\mathcal{M}_{t+\tau,t}$  which maps separable states to separable states and

$$\left\|\mathcal{M}_{t+\tau,t} - \mathcal{T} \exp\bigg(\int_t^{t+\tau} \mathcal{L}_{\leq d}(s) ds\bigg)\right\|_{\diamond} \leq 8d^4 \bigg(\sum_{\alpha,\beta} \int_t^{t+\tau} |g_{\alpha,\beta}(s)| \, ds + \int_t^{t+\tau} |u(s)| \, ds + \sum_{l=1}^3 \sum_{i \in \{1,2\}} \int_t^{t+\tau} \kappa_i^{(l)}(s) ds\bigg)^2.$$

*Proof.* It will be notationally convenient to define the scalars

$$G_{\alpha,\beta} = \int_{t}^{t+\tau} g_{\alpha,\beta}(s)ds, K_{i}^{(l)} = \int_{t}^{t+\tau} \kappa_{i}^{(l)}(s)ds, U = \int_{t}^{t+\tau} u(s)ds \text{ and}$$

$$G_{0} = \sum_{\alpha,\beta} \int_{t}^{t+\tau} |g_{\alpha,\beta}(s)| ds, U_{0} = \int_{t}^{t+\tau} |u(s)| ds, K_{i} = \sum_{l=1}^{3} K_{i}^{(l)}, K^{(l)} = \sum_{i \in \{1,2\}} K_{i}^{(l)}, K = \sum_{l=1}^{3} K^{(l)}. \tag{S93}$$

We will define the completely positive map  $\mathcal{R}_{t+\tau,t}$  via

$$\mathcal{R}_{t+\tau,t}(\rho) = \mathbb{E}_z \left[ R_1(z) R_2(z) \rho R_2^{\dagger}(z) R_1^{\dagger}(z) \right], \tag{S94a}$$

with

$$R_1(z) = Q_1 + e^{-i\pi/4} \sum_{\alpha,\beta} z_{\alpha,\beta} \sqrt{G_{\alpha,\beta}} c_{1,\leq d}^{\alpha}, R_2(z) = Q_2 + e^{-i\pi/4} \sum_{\alpha,\beta} z_{\alpha,\beta}^* \sqrt{G_{\alpha,\beta}} c_{2,\leq d}^{\beta},$$
 (S94b)

where  $z_{\alpha,\beta}$  are drawn independently and uniformly at random from the set  $\{\pm 1, \pm i\}$  and  $Q_i = \exp(-(K_i^{(1)} a_{i,\leq d}^{\dagger} a_{i,\leq d} + K_i^{(2)} a_{i,\leq d} a_{i,\leq d}^{\dagger})/2)$ . It can be noted that, by construction,  $\mathcal{R}_{t+\tau,t}$  maps a separable input state to a separable (but

possibly unnormalized) output state. Explicitly evaluating the expectation value in Eq. (S94), we obtain that

$$\mathcal{R}_{t+\tau,t}(\rho) = Q_{1}Q_{2}\rho Q_{2}^{\dagger}Q_{1}^{\dagger} - i\sum_{\alpha,\beta} G_{\alpha,\beta} \left( c_{1,\leq d}^{\alpha} c_{2,\leq d}^{\beta} \rho Q_{2}^{\dagger}Q_{1}^{\dagger} - Q_{1}Q_{2}\rho c_{1,\leq d}^{\alpha} c_{2,\leq d}^{\beta} \right) + \\
\sum_{\alpha,\beta} |G_{\alpha,\beta}| \left( c_{1,\leq d}^{\alpha} Q_{2}\rho Q_{2}^{\dagger} c_{1,\leq d}^{\alpha} + Q_{1}c_{2,\leq d}^{\beta} \rho c_{2,\leq d}^{\beta} Q_{1}^{\dagger} \right) + \\
\sum_{\alpha,\alpha',\beta,\beta'} \left( G_{\alpha,\beta} G_{\alpha',\beta'} c_{1,\leq d}^{\alpha} c_{2,\leq d}^{\beta} \rho c_{2,\leq d}^{\beta'} c_{1,\leq d}^{\alpha'} + |G_{\alpha,\beta}| |G_{\alpha',\beta'}| c_{1,\leq d}^{\alpha} c_{2,\leq d}^{\beta'} \rho c_{2,\leq d}^{\alpha'} c_{1,\leq d}^{\alpha'} \right) \\
= \rho - i \left[ \int_{t}^{t+\delta} h_{g,\leq d}(s) ds, \rho \right] + \sum_{\alpha,\beta} |G_{\alpha,\beta}| \left( c_{1,\leq d}^{\alpha} \rho c_{1,\leq d}^{\alpha} + c_{2,\leq d}^{\beta} \rho c_{2,\leq d}^{\beta} \right) - \\
\frac{1}{2} \sum_{i\in\{1,2\}} \left\{ K_{i}^{(1)} a_{i,\leq d}^{\dagger} a_{i,\leq d} + K_{i}^{(2)} a_{i,\leq d} a_{i,\leq d}^{\dagger}, \rho \right\} + \Delta_{t+\tau,t}(\rho), \tag{S95}$$

where, using the fact that

$$||Q_i|| \leq 1,$$

$$\|Q_{i} - I\| \leq \frac{1}{2} (K_{i}^{(1)} \|a_{1, \leq d}\|^{2} + K_{i}^{(2)} \|a_{2, \leq d}\|^{2}) \leq \frac{d}{2} (K_{i}^{(1)} + K_{i}^{(2)}),$$

$$\|Q_{i} - \left(I - \frac{1}{2} (K_{i}^{(1)} a_{i, \leq d}^{\dagger} a_{i, \leq d} + K_{i}^{(2)} a_{i, \leq d} a_{i, \leq d}^{\dagger})\right)\| \leq \frac{1}{8} (K_{i}^{(1)} \|a_{i, \leq d}\|^{2} + K_{i}^{(2)} \|a_{i, \leq d}\|^{2})^{2} \leq \frac{d^{2}}{8} (K_{i}^{(1)} + K_{i}^{(2)})^{2},$$

$$\|c_{i, \leq d}^{\alpha}\| \leq \sqrt{2} \|a_{i, \leq d}\| \leq \sqrt{2d},$$
(S96)

it follows that

$$\|\Delta_{t+\tau,t}\|_{\diamond} \le \frac{d^2}{2} (K^{(1)} + K^{(2)})^2 + 4d^2 G(K^{(1)} + K^{(2)}) + 8d^2 G^2.$$
 (S97)

Similarly, we also define the completely positive map  $\tilde{\mathcal{R}}_{t+\tau,t}$ :

$$\tilde{\mathcal{R}}_{t+\tau,t}(\rho) = \mathbb{E}_y \left[ \tilde{R}_1(y) \tilde{R}_2(y) \rho \tilde{R}_2^{\dagger}(y) \tilde{R}_1^{\dagger}(y) \right], \tag{S98a}$$

with

$$\tilde{R}_1(y) = \tilde{Q}_1 + ye^{-i\pi/4}\sqrt{U}n_{1, \leq d} \text{ and } \tilde{R}_2(y) = \tilde{Q}_2 + y^*e^{-i\pi/4}\sqrt{U}n_{2, \leq d},$$
 (S98b)

where y is drawn randomly from  $\{-1, 1, i, -i\}$  and  $\tilde{Q}_i = \exp(-\frac{K_i^{(3)}}{2}n_{i, \leq d}^2)$ . Similar to  $\mathcal{R}_{t+\tau,t}$ ,  $\tilde{\mathcal{R}}_{t+\tau,t}$  also maps a separable input state to a separable but possibly unnormalized output state. By explicitly evaluating the expectation in Eq. (S98), we find that

$$\begin{split} \tilde{\mathcal{R}}_{t+\tau,t}(\rho) &= \tilde{Q}_{1} \tilde{Q}_{2} \rho \tilde{Q}_{2}^{\dagger} \tilde{Q}_{1}^{\dagger} - i U(n_{1,\leq d} n_{2,\leq d} \rho \tilde{Q}_{1}^{\dagger} \tilde{Q}_{2}^{\dagger} - \tilde{Q}_{1} \tilde{Q}_{2} \rho n_{1,\leq d} n_{2,\leq d}) + \\ & |U| \left( n_{1,\leq d} \tilde{Q}_{2} \rho \tilde{Q}_{2}^{\dagger} n_{1,\leq d} + \tilde{Q}_{1} n_{2,\leq d} \rho n_{2,\leq d} \tilde{Q}_{1}^{\dagger} \right) + |U|^{2} n_{1,\leq d} n_{2,\leq d} \rho n_{2,\leq d} n_{1,\leq d} \\ &= \rho - i \left[ \int_{t}^{t+\delta} h_{\mathrm{ng},\leq d}(s) ds, \rho \right] + |U| \left( n_{1,\leq d} \rho n_{1,\leq d} + n_{2,\leq d} \rho n_{2,\leq d} \right) - \frac{1}{2} K_{3} \{ n_{1,\leq d} + n_{2,\leq d}, \rho \} + \tilde{\Delta}_{t+\tau,t}(\rho), \end{split}$$
(S99)

where, using the fact that  $\|\tilde{Q}_i\| \leq 1$ ,  $\|\tilde{Q}_i - I\| \leq K_i^{(3)} \|n_{i,\leq d}\|^2/2 \leq K_i^{(3)} d^2/2$ ,  $\|\tilde{Q}_i - (I - \frac{K_i^{(3)}}{2} n_i^2)\| \leq (K_i^{(3)} \|n_{i,\leq d}\|^2)^2/8 \leq (K_i^{(3)})^2 d^4/8$  and  $\|n_{i,\leq d}\| \leq d$ , it follows that

$$\|\tilde{\Delta}_{t+\tau,t}\|_{\diamond} \le \frac{1}{2} (K^{(3)})^2 d^4 + U_0^2 d^4 + 2U_0 K^{(3)} d^4.$$
 (S100)

Finally, we consider the channel generated by the fermionic Lindbladian in the time interval  $(t, t + \tau)$ : Performing a first-order Taylor expansion, we obtain that

$$\mathcal{T}\exp\left(\int_{t}^{t+\tau} \mathcal{L}(s)ds\right)\rho = \rho + \int_{t}^{t+\tau} \mathcal{L}(s)\rho ds + \Delta_{t+\tau,t}^{\mathcal{E}}(\rho),\tag{S101}$$

where  $\|\Delta_{t+\tau,t}^{\mathcal{E}}\|_{\diamond} \leq 8d^4(G+U+K)^2$ . From Eqs. (S95, S99, S101), we then obtain that

$$\mathcal{T}\exp\left(\int_{t}^{t+\tau} \mathcal{L}(s)ds\right) = \mathcal{M}_{t+\tau,t} + E_{t+\tau,t},\tag{S102}$$

where

$$\mathcal{M}_{t+\tau,t} = \mathcal{R}_{t+\tau,t} + \tilde{\mathcal{R}}_{t+\tau,t} + \underbrace{\sum_{i \in \{1,2\}} \left( K_i^{(1)} a_{i,\leq d} \cdot a_{i,\leq d}^{\dagger} + K_i^{(2)} a_{i,\leq d}^{\dagger} \cdot a_{i,\leq d} \right) - \sum_{\alpha,\beta} |G_{\alpha,\beta}| \left( c_{1,\leq d}^{\alpha} \cdot c_{1,\leq d}^{\alpha} + c_{2,\leq d}^{\beta} \cdot c_{2,\leq d}^{\beta} \right) + \underbrace{\sum_{i \in \{1,2\}} \left( K_i^{(3)} - |U| \right) n_{i,\leq d} \rho n_{i,\leq d}}_{\tilde{\mathcal{V}}_{t+\tau,t}}$$
(S103)

$$E_{t+\tau,t} = \Delta_{t+\tau,t}^{\mathcal{E}} - \Delta_{t+\tau,t} - \tilde{\Delta}_{t+\tau,t}. \tag{S104}$$

We note that  $\mathcal{M}_{t+\tau,t}$  is a channel that preserves separability as long as  $\mathcal{V}_{t+\tau,t}$  and  $\tilde{\mathcal{V}}_{t+\tau,t}$  are completely positive. The complete positivity of  $\tilde{\mathcal{V}}_{t+\tau,t}$  is ensured by requiring  $K_i^{(3)} \geq |U|$  which is implied by the condition C2 quoted in the lemma statement. To ensure that  $\mathcal{V}_{t+\tau,t}$  is completely positive, we note that it can be re-written as

$$\mathcal{V}_{t+\tau,t} = \sum_{i \in \{1,2\}} \left( F_{0,0}^{(i)} a_{i,\leq d} \cdot a_{i,\leq d}^{\dagger} + F_{0,1}^{(i)} a_{i,\leq d} \cdot a_{i,\leq d} + F_{1,0}^{(i)} a_{i,\leq d}^{\dagger} \cdot a_{i,\leq d} + F_{1,1}^{(i)} a_{i,\leq d}^{\dagger} \cdot a_{i,\leq d}^{\dagger} \right), \tag{S105}$$

where

$$F^{(1)} = \begin{bmatrix} K_1^{(1)} - \frac{1}{2}G & \frac{1}{2}\sum_{\beta} \left( |G_{2,\beta}| - |G_{1,\beta}| \right) \\ \frac{1}{2}\sum_{\beta} \left( |G_{2,\beta}| - |G_{1,\beta}| \right) & K_1^{(2)} - \frac{1}{2}G \end{bmatrix}, F^{(2)} = \begin{bmatrix} K_2^{(1)} - \frac{1}{2}G & \frac{1}{2}\sum_{\alpha} \left( |G_{\alpha,2}| - |G_{\alpha,1}| \right) \\ \frac{1}{2}\sum_{\beta} \left( |G_{\alpha,2}| - |G_{\alpha,1}| \right) & K_2^{(2)} - \frac{1}{2}G \end{bmatrix}.$$
(S106)

As long as  $F^{(1)}$ ,  $F^{(2)}$  are positive-semidefinite, it would follow that  $\mathcal{V}_{t+\tau,t}$  is completely positive. Now, it is easy to see that a sufficient condition for  $F^{(i)} \succeq 0$  is that  $K_i^{(1)}$ ,  $K_i^{(2)} \succeq G$ , which is implied by the condition C1 quoted in the lemma statement. Finally, the error term  $E_{t+\tau,t}$  can be bounded by

$$||E_{t+\tau,t}||_{\diamond} \le ||\Delta_{t+\tau,t}^{\mathcal{E}}||_{\diamond} + ||\Delta_{t+\tau,t}||_{\diamond} + ||\tilde{\Delta}_{t+\tau,t}||_{\diamond} \le 8d^{4}(G + U_{0} + K)^{2},$$
(S107)

which establishes the error bound in the lemma statement.

**Theorem 2** (High-noise seperability and classical simulation of bosonic model; reproduced from the main text). Suppose  $\rho(t)$  is the state obtained after evolving the bosonic system for time t with an initial product state, then for  $\min(\kappa_1, \kappa_2) \geq 2J$  the state  $\rho(t)$  is separable. Furthermore, there is a randomized classical algorithm that can sample within  $\epsilon$  total variation error of  $\rho(t)$  in  $O(\Lambda^2 t^2 m^{4L+8} \epsilon^{-1} \text{polylog}(m\Lambda t/\epsilon))$  time.

*Proof.* To prove Theorem 2, we will start with truncated first-order Trotter approximation of  $\rho(t)$ , i.e. with  $\sigma_{T,\leq d}$  given in Eq. (S89). From Lemmas 11 and 12, we obtain that

$$\|\rho(t) - \sigma_{T, \le d}\|_{1} \le O\left(\frac{\Lambda^{2} t^{2} m^{2} d^{2}}{T}\right) + O\left(\Lambda t m^{1 - k_{0}/2} d^{2 + k_{0}/2} e^{-\frac{1}{2}(d/d_{0} m)^{1/\alpha}}\right), \tag{S108}$$

where  $\Lambda = U_C + U_{os} + J_C + J_{os} + \kappa$ . Next, we use Lemma 13 to further approximate  $\sigma_{T,\leq d}$  with a separable state  $\phi_T$ . However, the noise rates at each step in the Trotterization need to be sufficiently high to meet the necessary conditions for separability [(C1) and (C2) provided in Lemma 13]—to ensure this, we make a choice of the parameters  $p_{i,\sigma;i,\sigma'}^{(l)}(t), q_{i,\sigma;i,\sigma'}^{(l)}(t)$  in Eq. (S87) that we so far left unspecified:

$$p_{i,\sigma;j,\sigma'}^{(1)}(t) = p_{i,\sigma;j,\sigma'}^{(2)}(t) = \frac{\sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t)|}{\sum_{k\neq i} \sum_{\nu} \sum_{\alpha,\alpha'} |J_{i,\sigma;k,\nu}^{\alpha,\alpha'}(t)|}, p_{i,\sigma;j,\sigma'}^{(3)}(t) = \frac{|U_{i,\sigma;j,\sigma'}(t)|}{\sum_{k\neq i} \sum_{\nu} |U_{i,\sigma;k,\nu}(t)|}, q_{i,\sigma;j,\sigma'}^{(3)}(t) = \frac{\sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t)|}{\sum_{k\neq i} \sum_{\nu} \sum_{\alpha,\alpha'} |J_{i,\sigma;k,\nu}^{\alpha,\alpha'}(t)|}, q_{i,\sigma;j,\sigma'}^{(3)}(t) = \frac{|U_{i,\sigma;j,\sigma'}(t)|}{\sum_{k\neq i} \sum_{\nu} |U_{i,\sigma';k,\nu}(t)|}, (S109a)$$

and it can be checked that they satisfy the normalization condition in Eq. (S88). Considering now the channels  $\Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$  from Eq. (S89) in Trotterized state  $\sigma_{T,\leq d}$ —to apply Lemma 13 to these channels, we need

(1) Imposing condition C1: For  $l \in \{1, 2\}$

$$\kappa_l p_{i,\sigma;j,\sigma'}^{(l)}(t), \kappa_l q_{i,\sigma;j,\sigma'}^{(l)}(t) \ge 2 \sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(t)| \text{ or equivalently}$$
(S109b)

$$\kappa_l \ge 2 \sum_{k' \ne k} \sum_{\nu'} \sum_{\alpha,\alpha'} |J_{k,\nu;k',\nu'}^{\alpha,\alpha'}(t)| \text{ for } (k,\nu) \in \{(i,\sigma),(j,\sigma')\}.$$
(S109c)

This condition can clearly be satisfied if  $\kappa_1, \kappa_2 \geq 2J_C$  since  $\sum_{k' \neq k} \sum_{\nu'} \sum_{\alpha, \alpha'} |J_{k,\nu;k',\nu'}^{\alpha,\alpha'}(t)| \leq J_C$ .

(2) Imposing condition C2:

$$\kappa_3 p_{i,\sigma;j,\sigma'}^{(3)}(t), \kappa_3 q_{i,\sigma;j,\sigma'}^{(3)}(t) \ge 2|U_{i,\sigma;j,\sigma'}(t)|$$
 or equivalently (S109d)

$$\kappa_3 \ge 2 \sum_{k' \ne k} \sum_{\nu'} |U_{k,\nu;k',\nu'}(t)| \text{ for } (k,\nu) \in \{(i,\sigma),(j,\sigma')\}.$$
(S109e)

This condition can clearly be satisfied if  $\kappa_3 \geq 2U_C$  since  $\sum_{k'\neq k} \sum_{\nu'} |U_{k,\nu;k',\nu'}(t)| \leq U_C$ .

Now, assuming  $\kappa_1, \kappa_2 \geq 2J_C$  and  $\kappa_3 \geq 2U_C$ , we can then approximate  $\sigma_{T,\leq d}$  by  $\phi_T$  given by

$$\phi_T = \prod_{\tau=N}^{1} \left( \prod_{i < j} \prod_{\sigma,\sigma'} \mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'} \right) \mathcal{U}_{\tau\delta,(\tau-1)\delta}^{\text{os}} \rho(0), \tag{S109f}$$

where  $\mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$  is the separability preserving completely-positive map corresponding to  $\Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$  from Lemma 13, which also satisfies

$$\|\Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'} - \mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}\|_{\diamond} \le \varepsilon_{\tau}^{i,\sigma;j,\sigma'},\tag{S109g}$$

where

$$\varepsilon_{\tau}^{i,\sigma;j,\sigma'} = 8d^4 \left( \int_{(\tau-1)\delta}^{\tau\delta} \left( \sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(s)| ds + |U_{i,\sigma;j,\sigma'}(s)| ds + \sum_{l=1}^{3} \kappa_l \left( p_{i,\sigma;j,\sigma'}^{(l)}(s) + q_{i,\sigma;j,\sigma'}^{(l)}(s) \right) \right) ds \right)^2. \tag{S109h}$$

We note that  $\varepsilon$  is defined by

$$\varepsilon = \sum_{\tau=1}^{T} \sum_{i,j:i < j} \sum_{\sigma,\sigma'} \varepsilon_{\tau}^{i,\sigma;j,\sigma'} \\
\leq 8d^{4} \sum_{\tau=1}^{T} \left( \int_{(\tau-1)\delta}^{\tau\delta} \sum_{i,j;i < j} \left( \sum_{\alpha,\alpha'} |J_{i,\sigma;j,\sigma'}^{\alpha,\alpha'}(s)| ds + |U_{i,\sigma;j,\sigma'}(s)| ds + \sum_{l=1}^{3} \kappa_{l} \left( p_{i,\sigma;j,\sigma'}^{(l)}(s) + q_{i,\sigma;j,\sigma'}^{(l)}(s) \right) \right) ds \right)^{2} \\
\leq 8d^{4} \left( J_{C} + U_{C} + 2\kappa \right)^{2} \frac{t^{2}m^{2}}{T} \leq 32d^{4} \frac{\Lambda^{2}t^{2}m^{2}}{T}. \tag{S110}$$

Furthermore, we also note from the triangle inequality that

$$\|\mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}\|_{\diamond} \leq \|\Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}\|_{\diamond} + \|\mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'} - \Phi_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}\|_{\diamond} \leq 1 + \varepsilon_{\tau}^{i,\sigma;j,\sigma'} \leq \exp(\varepsilon_{\tau}^{i,\sigma;j,\sigma'}). \tag{S111}$$

We can now bound the error between  $\phi_T$  and  $\sigma_{T,\leq d}$  using telescoping to obtain

$$\|\phi_T - \sigma_{T, \le d}\|_1 \le e^{\varepsilon} \varepsilon \le e^{O(\Lambda^2 t^2 m^2 d^4 / T^2)} O\left(\frac{\Lambda^2 t^2 m^2 d^4}{T}\right). \tag{S112}$$

Finally, using Eq. (S108), we obtain that

$$\|\rho(t) - \phi_T\|_1 \le e^{O(\Lambda^2 t^2 m^2 d^4/T)} O\left(\frac{\Lambda^2 t^2 m^2 d^4}{T}\right) + O\left(\frac{\Lambda^2 t^2 m^2 d^4}{T}\right) + O\left(\Lambda t m^{1 - k_0/2} d^{2 + k_0/2} e^{-\frac{1}{2}(d/d_0 m)^{1/\alpha}}\right).$$
(S113)

Thus, choosing

$$d = \Theta\left(m \text{ polylog}\left(\frac{m\Lambda t}{\epsilon}\right)\right), T = \Theta\left(\frac{\Lambda^2 t^2 m^6}{\epsilon} \text{polylog}\left(\frac{m\Lambda t}{\epsilon}\right)\right)$$
 (S114)

ensures that  $\|\rho(t) - \phi_T\|_1 \le \epsilon$ . Finally, we note that  $\phi_N$  by itself is guaranteed to be positive semi-definite but not normalized. We will instead consider  $\tilde{\phi}_T = \phi_T/\text{Tr}(\phi_T)$ —note that, if  $\|\phi_T - \rho(t)\|_1 \le \epsilon < 1$ ,

$$\|\tilde{\phi}_{T} - \rho(t)\|_{1} \le \frac{1}{\text{Tr}(\phi_{N})} \|\phi_{T} - \rho(t)\|_{1} + \left| \frac{\text{Tr}(\phi_{T}) - 1}{\text{Tr}(\phi_{T})} \right| \|\rho(t)\|_{1} \le \frac{2\epsilon}{1 - \epsilon} \le O(\epsilon), \tag{S115}$$

where in (1) we have used that  $|\operatorname{Tr}(\phi_T) - 1| = |\operatorname{Tr}(\phi_T) - \operatorname{Tr}(\rho(t))| \le ||\phi_T - \rho(t)||_1 \le \epsilon$ .

Time-complexity of sampling in the Fock state basis. We now consider the cost of sampling from the state  $\tilde{\phi}_T$ . By construction,  $\tilde{\phi}_T$  is a separable state and hence can be expressed as

$$\tilde{\phi}_T = \sum_{\alpha} p_{\alpha} \bigg( \bigotimes_{i} \rho_i^{(\alpha)} \bigg), \tag{S116}$$

where  $p_{\alpha}$  is a probability distribution over  $\alpha$  and  $\rho_i^{(\alpha)}$  is a state supported on the modes at the  $i^{\text{th}}$  site. To either sample from or compute a local observable in  $\tilde{\phi}_T$ , we first sample from  $p_{\alpha}$  and obtain a product state  $\otimes_i \rho_i^{(\alpha)}$  from the mixed state ensemble  $\tilde{\phi}_T$ . Given the initial state  $\rho_{\leq d}(0)$  as a product state, we sequentially apply  $\mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$ , normalize the result and sample from the resulting separable state to obtain another product state—since the input state is a product state, each application of  $\mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$ , normalization and the subsequent sampling involves only the 2L truncated bosonic modes at sites i and j and can be classically done in  $O(d^{4L}) \leq O(m^{4L} \text{polylog}(m\Lambda t/\varepsilon))$  time. Additionally, the application of the on-site unitaries  $(\mathcal{U}_{\tau\delta,(\tau-1)\delta}^{os})$  will map a product state between the different sites to another product state, and it can be applied classically in  $O(md^{3L}) \leq O(m^{3L+1} \text{polylog}(m\Lambda t/\varepsilon))$  time. Counting the time needed to apply, in this manner, all  $\mathcal{M}_{\tau\delta,(\tau-1)\delta}^{i,\sigma;j,\sigma'}$  and  $\mathcal{U}_{\tau\delta,(\tau-1)\delta}^{os}$ , the total classical run-time for drawing one product state from  $\tilde{\phi}_T$  is thus  $O(Tm^2 \times m^{4L} \text{polylog}(m\Lambda t/\varepsilon)) \leq O(\Lambda^2 t^2 m^{4L+8} \epsilon^{-1} \text{polylog}(m\Lambda t/\varepsilon))$ . Having drawn a product state  $\otimes_i \rho_i^{(\alpha)}$  from the separable state  $\tilde{\phi}_T$ , we can now consider the task of drawing a sample in the Fock state basis: Given each  $\rho_i^{(\alpha)}$  as a  $d^L \times d^L$  matrix, drawing a sample from  $\otimes_i \rho_i^{(\alpha)}$  on the Fock state basis requires computational time  $O(nd^L) \leq O(m^{L+1} \text{polylog}(m\Lambda t/\epsilon))$ . Thus, the total time complexity of drawing a single sample from  $\tilde{\phi}_T$  is dominated by the cost of sampling from  $p_\alpha$  and is  $O(\Lambda^2 t^2 m^{4L+8} \epsilon^{-1} \text{polylog}(m\Lambda t/\epsilon))$ .

#### IV. HIGH-NOISE SEPARABILITY IN SPIN MODELS

In this section, we analyze a spin model evolving under a 2-local Hamiltonian in the presence of noise, which closely follows the analysis of the bosonic model in the previous section. We only provide a derivation of the counterpart of Lemma 13 for the spin model, which outlines a sufficient condition for separability preservation for two qudits. Combining this lemma with standard first-order Trotterization can allow us to show that even in the many-body regime, a sufficiently high noise maps a separable state to another separable state.

Lemma 14 (Separability condition for spin models). Consider a Lindbladian on two d-level qudits given by

$$\mathcal{L}(t) = -i[h(t), \cdot] + \kappa(t) \sum_{i \in \{1, 2\}} \sum_{k} \mathcal{D}_{L_{i,k}},$$

where  $\kappa(t) \geq 0$ . Here h(t) is a two-qudit Hamiltonian which we express as

$$h(t) = \sum_{\alpha} s_{\alpha}(t) O_{1,\alpha} \otimes O_{2,\alpha},$$

where we can assume  $s_{\alpha}(t) \geq 0$ ,  $O_{i,\alpha}$  are Hermitian operators on the  $i^{th}$  qudit with  $\|O_{i,\alpha}\|_F \leq 1$ . Furthermore, for each  $i \in \{1,2\}$ , the jump operators  $L_{i,k}$  satisfy  $\sum_k \|L_{i,k}\|^2 \leq 1$  and have a full Kraus rank and  $\exists \lambda_0 > 0$  such that for any single qudit operator A

$$\sum_{k} |\operatorname{Tr}(L_{i,k}^{\dagger} A)|^2 \ge \lambda_0 \|A\|_F^2.$$

Then if  $\kappa(t) \geq \sum_{\alpha} s_{\alpha}(t)/\lambda_0$ , there is a completely positive map  $\mathcal{M}_{t+\tau,t}$  which maps separable states to separable states

$$\left\| \mathcal{M}_{t+\tau,t} - \mathcal{T} \exp\left( \int_t^{t+\tau} \mathcal{L}(s) ds \right) \right\|_{\diamond} \le 4 \left( \int_t^{t+\tau} \kappa(t') dt' + \sum_{\alpha} \int_t^{t+\tau} s_{\alpha}(t') dt' \right)^2.$$

*Proof.* It will be convenient to introduce the scalars

$$S_{\alpha} = \int_{t}^{t+\tau} s_{\alpha}(t')dt', S = \sum_{\alpha} S_{\alpha} \text{ and } K = \int_{t}^{t+\tau} \kappa(t')dt'.$$
 (S117)

We will also define

$$q_i^{\text{eff}}(t) = \frac{\kappa(t)}{2} \sum_k L_{i,k}^{\dagger} L_{i,k}, \quad q^{\text{eff}} = q_1^{\text{eff}}(t) \otimes I + I \otimes q_2^{\text{eff}}(t) \text{ and } Q_i = \exp\left(-\int_t^{t+\tau} q_i^{\text{eff}}(t') dt'\right). \tag{S118}$$

Consider the following completely positive map

$$\mathcal{R}_{t+\tau,t}\rho = \mathbb{E}_z((R_1(z) \otimes R_2(z))\rho(R_1^{\dagger}(z) \otimes R_2^{\dagger}(z))), \tag{S119a}$$

where

$$R_1(z) = Q_1 + e^{-i\pi/4} \sum_{\alpha} z_{\alpha} \sqrt{S_{\alpha}} O_{1,\alpha} \text{ and } R_2(z) = Q_2 + e^{-i\pi/4} \sum_{\alpha} z_{\alpha}^* \sqrt{S_{\alpha}} O_{2,\alpha},$$
 (S119b)

where  $z_{\alpha}$  are drawn uniformly and independently from the set  $\{\pm 1, \pm i\}$ . We note that  $\mathcal{R}_{t+\tau,t}$  is separability preserving i.e. maps a separable state to another separable state. Explicitly evaluating the expectation value in Eq. (S119), we obtain

$$\mathcal{R}_{t+\tau,t}(\rho) = (Q_1 \otimes Q_2)\rho(Q_1^{\dagger} \otimes Q_2^{\dagger}) - i\sum_{\alpha} S_{\alpha} \left( (O_{1,\alpha} \otimes O_{2,\alpha})\rho(Q_1^{\dagger} \otimes Q_2^{\dagger}) - (Q_1 \otimes Q_2)\rho(O_{1,\alpha} \otimes O_{2,\alpha}) \right) +$$

$$\sum_{\alpha} S_{\alpha} \left( (O_{1,\alpha} \otimes Q_2)\rho(O_{1,\alpha} \otimes Q_2^{\dagger}) + (Q_1 \otimes O_{2,\alpha})\rho(Q_1^{\dagger} \otimes O_{2,\alpha}) \right) +$$

$$\sum_{\alpha} S_{\alpha} S_{\alpha'} \left( (O_{1,\alpha} \otimes O_{2,\alpha})\rho(O_{1,\alpha'} \otimes O_{2,\alpha'}) + (O_{1,\alpha} \otimes O_{2,\alpha'})\rho(O_{1,\alpha} \otimes O_{2,\alpha'}) \right), \tag{S120}$$

where using  $||Q_i|| \le 1, ||Q_i - I|| \le K/2, ||Q_i - (I - q_i^{\text{eff}})|| \le K^2/8$ , we obtain that

$$\mathcal{R}_{t+\tau,t}(\rho) = \rho - i \int_{t}^{t+\tau} [h(t'), \rho] dt' - \int_{t}^{t+\tau} \{q^{\text{eff}}(t'), \rho\} dt' + \sum_{\alpha} S_{\alpha}(O_{1,\alpha} \otimes I) \rho(O_{1,\alpha} \otimes I) + (I \otimes O_{2,\alpha}) \rho(I \otimes O_{2,\alpha})) + \Delta_{t+\tau,t}(\rho)$$

$$= \rho + \int_{t}^{t+\tau} \mathcal{L}(t') \rho dt' - \mathcal{G}_{t+\tau,t} \rho + \Delta_{t+\tau,t}^{(R)}(\rho), \tag{S121}$$

where  $\mathcal{G}_{t+\tau,t}$  is a superoperator given by

$$\mathcal{G}_{t+\tau,t} = \mathcal{G}_{t+\tau,t}^{(1)} \otimes \operatorname{id} + \operatorname{id} \otimes \mathcal{G}_{t+\tau,t}^{(2)}, \text{ where}$$

$$\mathcal{G}_{t+\tau,t}^{(i)}(\rho) = K \sum_{k} L_{i,k} \rho L_{i,k}^{\dagger} - \sum_{\alpha} S_{\alpha} O_{i,\alpha} \rho O_{i,\alpha},$$
(S122)

and  $\Delta_{t+\tau,t}$  is a super-operator with

$$\|\Delta_{t+\tau,t}^{(R)}\|_{\diamond} \le 2K^2 + 4SK + 2S^2 = 2(S+K)^2.$$
(S123)

Furthermore, the channel generated by the Lindbladian can be expanded to the first order to obtain

$$\mathcal{T}\exp\left(\int_{t}^{t+\tau} \mathcal{L}(s)ds\right) = \rho + \int_{t}^{t+\tau} \mathcal{L}(t')\rho dt' + \Delta_{t+\tau,t}^{(L)},\tag{S124}$$

where, since  $\|\mathcal{L}(t)\|_{\diamond} \leq 2(\sum_{\alpha} s_{\alpha}(t) + \kappa(t)), \, \Delta_{t+\tau,t}^{(L)}$  is a superoperator with

$$\|\Delta_{t+\tau,t}^{(L)}\|_{\diamond} \le 2(S+K)^2. \tag{S125}$$

Consequently, we have that

$$\left\| \mathcal{T} \exp\left( \int_0^t \mathcal{L}(s) ds \right) - \left( \mathcal{R}_{t+\tau,t} + \mathcal{G}_{t+\tau,t} \right) \right\|_{\diamond} \le 4(S+K)^2.$$
 (S126)

We note that  $\mathcal{R}_{t+\tau,t}$  is separability preserving by construction. Furthermore,  $\mathcal{G}_{t+\tau,t}$  is a sum of super-operators acting individually on the two qudits—consequently,  $\mathcal{G}_{t+\tau,t}$  will be separability preserving as long as it is completely positive. To find a sufficient condition for complete positivity of  $\mathcal{G}_{t+\tau,t}^{(i)}$ , we will impose that its Choi state,  $\Phi_{\mathcal{G}^{(i)}}$ , is positive semi-definite. From Eq. (S122), we obtain that

$$\Phi_{\mathcal{G}^{(i)}} = \sum_{i,j'=1}^{d} \left( K \sum_{k} L_{i,k} |j\rangle\langle j'| L_{i,k}^{\dagger} - \sum_{\alpha} S_{\alpha} O_{i,\alpha} |j\rangle\langle j'| O_{i,\alpha} \right) \otimes |j\rangle\langle j'|. \tag{S127}$$

Now, suppose  $|\psi\rangle = \sum_{j,j'} \psi_{j,j'} |j,j'\rangle \in \mathbb{C}^d \otimes \mathbb{C}^d$  is a two-qudit state and  $\Psi = \sum_{j,j'} \psi_{j,j'} |j\rangle\langle j'|$  is its corresponding matrix, then

$$\langle \psi | \Phi_{\mathcal{G}^{(i)}} | \psi \rangle = K \sum_{k} |\text{Tr}(L_{i,k}^{\dagger} \Psi)|^{2} - \sum_{\alpha} S_{\alpha} |\text{Tr}(O_{i,\alpha} \Psi)|^{2}$$

$$\stackrel{\text{(1)}}{\geq} K \lambda_{0} \|\Psi\|_{F}^{2} - \sum_{\alpha} S_{\alpha} \|O_{i,\alpha}\|_{F}^{2} \|\Psi\|_{F}^{2}$$

$$= (K \lambda_{0} - S) \||\psi\rangle\|^{2}, \tag{S128}$$

where in (1) we have used the fact that  $\operatorname{Tr}(A^{\dagger}B)^2 \leq \operatorname{Tr}(A^{\dagger}A)\operatorname{Tr}(B^{\dagger}B)$  and also the condition  $\sum_k |\operatorname{Tr}(L_{i,k}^{\dagger}\Psi)|^2 \geq \lambda_0 \|\Psi\|_F^2$  from the lemma statement. Therefore, if  $K \geq S/\lambda_0$ , which is implied by the condition  $\kappa(t) \geq \sum_{\alpha} s_{\alpha}(t)/\lambda_0$ , then  $\mathcal{G}^{(i)}$  are completely positive. This in turn implies that the super-operator  $\mathcal{M}_{t+\tau,t} = \mathcal{R}_{t+\tau,t} + \mathcal{G}_{t+\tau,t}$  is both completely positive and separability preserving, which proves the lemma.

Similar to the case of the fermionic and bosonic models, this lemma can be combined with first-order Trotterization in the many-body setting to show high-noise separability for a broad class of noise models. In particular, we could consider noisy dynamics described by the master equation

$$\frac{d}{dt}\rho(t) = -i[H, \rho(t)] + \kappa \sum_{i,k} \mathcal{D}_{L_{i,k}}$$
(S129)

with  $L_{i,k}$  satisfying the conditions in Lemma 14 and

$$H(t) = \sum_{i} h_i(t) + \sum_{i < j} \sum_{\alpha} s_{\alpha}^{i,j}(t) (O_{i,\alpha} \otimes O_{j,\alpha}), \tag{S130}$$

where  $O_{i,\alpha}$  would be a Hermitian operator acting on the  $i^{\text{th}}$  qudit chosen to be normalized such that  $||O_{i,\alpha}||_F = 1$ . Introducing the "inter-site interaction-strength" parameter J as the smallest number satisfying

$$\sum_{j>i} |s_{\alpha}^{i,j}(t)| + \sum_{j\le i} |s_{\alpha}^{j,i}(t)| \le J \text{ for all } i, t \ge 0,$$
(S131)

we can then establish using Lemma 14 that if  $\kappa \geq J/\lambda_0$ , then an initial separable state of the spins always evolves into a separable state.

#### V. COUNTER-EXAMPLES

In this section, we consider the question of whether a counterpart of Theorem 1 can be obtained for the bosonic model, and if a counterpart for Theorem 2 can be established for the fermionic model.

![](_page_31_Figure_1.jpeg)

FIG. S1. Representation of the Wigner function for the state  $\rho(t)$  obtained by evolving Eq. (S133) with initial state  $\rho(0) = |\alpha\rangle\langle\alpha|$ , with parameters U=0.05 and t=0.5. (a) The Wigner function W(x,p) is represented in phase space for  $\alpha=5$  and error rate  $\kappa=0.1U$  (left) and  $\kappa=2U$  (right). (b) Representation of the minimum value of the Wigner function  $W_{\min}=\min_{x,p}W(x,p)$ . One can clearly observe that, for a fixed value of  $\kappa/U$ , the Wigner function becomes more negative by increasing  $\alpha$ , which suggest that the Gaussian resources can effectively boost the non-Gaussianity of the system. Hence, even for large values of  $\kappa$ , a negative Wigner state might be reached, by increasing  $\alpha$ .

## A. High-noise regime for the bosonic model is not convex-Gaussian at all times

We will provide evidence that there is no counterpart of Theorem 1 for bosonic systems. That is, even with noise rates larger than the non-Gaussianity ( $\kappa \gg U$ ), one can still obtain states which are not convex-Gaussian. In section V A 1, we provide numerical evidence that, with a single bosonic mode and dephasing noise greater than the non-Gaussianity ( $\kappa_3 \geq U$ ), states with negative Wigner function can be reached, which automatically implies lack of convex Gaussianity. In section V A 2, we provide a stronger argument in the absence of dephasing noise: for noise models containing only incoherent particle loss and gain ( $\kappa_3 = 0$ ), one can perform high-fidelity arbitrary gates even if the non-Gaussianity is much smaller than the noise rate,  $U \ll \kappa$ , provided that the Gaussian couplings  $J, \Omega$  can be made sufficiently large, enabling the implementation of gates with effective error rates below the fault tolerance threshold [S8–S10]. As a consequence, not only is the state not guaranteed to remain convex-Gaussian, but the classical simulation of local observables is provably BQP-hard.

## 1. High dephasing noise regime

Here, we provide a simple example with a single bosonic mode, where dephasing noise, no-matter how high, is unable to make the state convex Gaussian. Our analysis is centered on the Wigner function, which, for a single bosonic mode state  $\rho$ , is defined as

$$W(x,p) = \frac{1}{\pi} \int_{-\infty}^{\infty} \langle x - y | \rho | x + y \rangle e^{2ipy} dy.$$
 (S132)

Since quantum states with positive Wigner functions can be efficiently simulated [S11], the negativity of the Wigner function is regarded as a necessary resource for quantum advantage. Furthermore, a negative Wigner function rules out convex-Gaussianity, since all pure Gaussian states have nonnegative Wigner functions [S12, S13], and as a consequence convex Gaussian states do as well.

Specifically, we consider an initial state  $\rho(0) = |\alpha\rangle\langle\alpha|$ , where  $|\alpha\rangle$  represents the single-mode coherent state  $|\alpha\rangle = e^{\alpha(a^{\dagger} - a)} |\text{vac}\rangle$ , with  $\alpha$  a real number. Then, the state is evolved under the Hamiltonian  $H = Un^2$  and dephasing noise of rate  $\kappa_3 = \kappa$ , which yields the master equation

$$\frac{d}{dt}\rho(t) = \mathcal{L}\rho(t) = -iU[n^2, \rho(t)] + \kappa \left(n\rho(t)n - \frac{1}{2}\{n^2, \rho(t)\}\right). \tag{S133}$$

In this setting, we numerically compute the minimum value of the Wigner function,  $W_{\min} = \min_{x,p} W(x,p)$ , and represent it in Fig. S1. One can appreciate that, even when  $\kappa \geq U$ , using a sufficiently large  $\alpha$  results in a state with a negative Wigner function. Consequently, we do not expect an analogue of Theorem 1 to hold for bosons: even for a high dephasing noise rate, with a sufficiently large Gaussian displacement, an initially Gaussian state can evolve into Wigner negative (not convex-Gaussian) states at short times. The time-scale at which the state becomes Wigner negative is determined by both the value of U, as well as the displacement. For the one-mode problem considered

![](_page_32_Figure_1.jpeg)

FIG. S2. The relative Wigner negativity, quantified by  $-W_{\min}/W_{\max} = -\min_{x,p} W(x,p)/\max_{x,p} W(x,p)$ , for a single bosonic mode evolving under the Hamiltonian  $H = Un^2$  as well as dephasing noise at rate  $\kappa$ . The initial state of the bosonic mode is the coherent state  $|\alpha\rangle$ . As expected, the relative Wigner negativity decreases as U decreases, and at a fixed  $\alpha$ , the maximum Wigner negativity is attained at time-scales of 1/U.

above, Fig. S2 shows the relative wigner-negativity  $-W_{\min}/W_{\max} = -\min_{x,p} W(x,p)/\max_{x,p} W(x,p)$  as a function of time. We find that while the state eventually becomes Wigner non-negative, even in the regime  $\kappa_3 \gg U$ , there is an intermediate temporal region that depends on U and  $\alpha$  where the state is Wigner negative. For a fixed  $\alpha$ , the time  $t^*$  at which the state is maximally Wigner negative scales as 1/U, consistent with the fact that U determines the strength of the process generating the non-Gaussianity or Wigner negativity in the dynamics.

We remark that this does not necessarily imply simulation hardness: the question of whether there is a threshold error  $\kappa_{\text{th}}(U)$  depending on U but not on  $J, \Omega$  above which the classical simulation becomes tractable remains open.

## 2. High incoherent particle loss and gain regime

Here we analyze the complexity of classically simulating the bosonic system in the absence of dephasing noise  $(\kappa_3 = 0)$  and find that the problem does not become easy above a noise threshold depending exclusively on the non-Gaussian interaction strength, thus showing that no counterpart of Theorem 1 can exist for bosons in the absence of dephasing noise. Specifically, we show that, even when the non-Gaussian interaction strength is much smaller than the noise strength,  $U \ll \kappa$ , one can perform arbitrarily fast gates. Due to the threshold theorem, this allows for the implementation of fault-tolerant schemes [S8, S10]. To show this, it is enough to consider systems with only one bosonic mode per site (L = 1) and only onsite non-Gaussianity  $(U_C = 0)$ .

We will start with a technical lemma: we will show that, for a system with m modes evolving under the noise model in Eq. (S27), the error induced by the noise can be upper bounded by  $O(m\kappa t)$ .

**Lemma 15** (Error bound between noisy and noiseless evolution). Consider a bosonic system with m modes evolving under the master equation

$$\frac{d}{dt}\rho(t) = \mathcal{L}\rho(t) = -i[H(t), \rho(t)] + \sum_{l=1}^{2} \sum_{v=1}^{m} \kappa_l \mathcal{D}_{L_v^{(l)}},$$

where  $\mathcal{D}_L \rho = L \rho L^{\dagger} - \{L^{\dagger} L, \rho\}/2$ ,  $L_v^{(1)} = a_v, L_v^{(2)} = a_v^{\dagger}$ , and  $\kappa_1 + \kappa_2 = 1$ . Assume that, for some integer d,  $\rho(0)$  lies in the subspace  $\mathcal{H}_{\leq d}$  of the Hilbert space spanned by the first d+1 levels  $\{|0\rangle, \ldots, |d\rangle\}$ , and that the Hamiltonian H(t) contains no couplings between the state  $|d\rangle$  and any state  $|k\rangle$  with k>d. Then, denoting by  $\mathcal{U}(\cdot) = \mathcal{T} \exp\left(-i \int_0^t [H(s), \cdot] ds\right)$  the time-evolution in the noiseless case  $(\kappa=0)$ , the error induced by the dissipation can be bounded as

$$\left\| \mathcal{T} \exp \left( \int_0^t \mathcal{L}(s) ds \right) \rho(0) - \mathcal{U} \rho(0) \right\|_1 \le 2m \kappa t (d+1).$$

*Proof.* Let us consider the following effective Hamiltonian:

$$H_{\text{eff}} = H - i \frac{1}{2} \sum_{v=1}^{m} \left( \kappa_1 a_v^{\dagger} a_v + \kappa_2 a_v a_v^{\dagger} \right). \tag{S134}$$

Then, the time evolution may be written as

$$\rho(t) = \mathcal{T} \exp\left(\int_0^t \mathcal{L}(s)ds\right)\rho(0) = \underbrace{\mathcal{T} \exp\left(-i\int_0^t [H_{\text{eff}}(s), \cdot]ds\right)\rho(0)}_{\sigma} + \mathcal{N}(\rho(0)) = \sigma + \mathcal{N}(\rho(0)), \tag{S135}$$

where  $\sigma$  is the (unnormalized) state obtained by evolving under the effective Hamiltonian, and  $\mathcal{N}(\rho)$  is a completely positive channel that is not trace preserving. Naturally,  $\operatorname{tr}(\sigma) + \operatorname{tr}(\mathcal{N}(\rho)) = 1$ . The state  $\sigma$  can be understood as the output when no errors occur, while  $\mathcal{N}(\rho)$  captures the output with one or more errors.

For the  $v^{\text{th}}$  bosonic mode, we define the projector that truncates to at most d particles as  $\Pi_{v,\leq d} = \sum_{j=0}^{d} |j\rangle \langle j|$ . Then,  $\Pi_{\leq d} = \otimes_v \Pi_{v,\leq d}$  is the projector onto  $\mathcal{H}_{\leq d}$ . Note that, since H does not contain couplings to higher levels, neither does  $H_{\text{eff}}$ . As a consequence, the dynamics of  $\sigma$  are constrained to the first d+1 levels, and can be truncated.

Let us denote the truncated Hamiltonians by  $\tilde{H} = \Pi_d H \Pi_d$ ,  $\tilde{H}_{\rm dis} = \Pi_d H_{\rm dis} \Pi_d$ . Using the definition of  $\tilde{H}_{\rm dis}$  in Eq. (S134), the operator norm of the truncated effective Hamiltonian  $\tilde{H}_{\rm dis}$  can then be bounded as

$$\|\tilde{H}_{\text{dis}}\| \le \frac{m}{2} \left(\kappa_1 d + \kappa_2 (d+1)\right) \le \frac{m}{2} \left(\kappa_1 + \kappa_2\right) d \le \frac{m\kappa}{2} (d+1).$$
 (S136)

Let us now write  $\sigma$  in a more convenient form as  $\sigma = \lim_{N\to\infty} (O_N \rho(0) O_N^{\dagger})$ , where

$$O_N = \prod_{k=1}^N \left( e^{-i\tilde{H}(kt/N)t/N} e^{-i\tilde{H}_{\text{dis}}t/N} \right). \tag{S137}$$

This expression can be derived, for example, from standard Trotterization techniques. We would now like to bound  $\text{tr}(\sigma)$ , which can be understood as the probability of no errors occurring during the computation. Naturally, the unitary parts of the evolution in Eq. (S137) are trace preserving, and we only need to bound the imaginary time evolution induced by the Hamiltonian  $\tilde{H}_{\text{dis}}$ . Note also that, using Eq. (S136), the minimum singular value in each step can be bounded as

$$\sigma_{\min}(e^{-\tilde{H}_{\mathrm{dis}}t/N}) \ge \exp\left(-\frac{m\kappa}{2}\frac{t}{N}\left(\kappa_1(d+1) + \kappa_2(d+1)\right)\right) \ge \exp\left(-\frac{m\kappa}{2}\frac{t}{N}(d+1)\right). \tag{S138}$$

As a consequence, using Eq. (S137) and Eq. (S138), it can be easily checked that

$$\sigma_{\min}(O_N^{\dagger}O_N) \ge \left[\sigma_{\min}(e^{-\tilde{H}_{\mathrm{dis}}t/N})\right]^{2N} \ge \exp\left[-m\kappa t(d+1)\right]. \tag{S139}$$

This allows us to bound the trace as

$$\operatorname{tr}(\sigma) = \lim_{N \to \infty} \operatorname{tr}(O_N^{\dagger} O_N \rho(0)) \ge \lim_{N \to \infty} \sigma_{\min}(O_N^{\dagger} O_N) \operatorname{tr}(\rho(0)) \ge \exp\left[-m\kappa t(d+1)\right]. \tag{S140}$$

As a consequence, since the total evolution of the system must be trace preserving, it immediately follows that  $\operatorname{tr}(\mathcal{N}(\rho(0)) \le 1 - e^{-m\kappa t d^2})$ .

Now, let us bound the distance between  $\sigma$  and the state obtained under ideal (noiseless) evolution,  $\|\sigma - \mathcal{U}\rho(0)\|_1$ . We use the fact that

$$\frac{\partial}{\partial \kappa} e^{-\tilde{H}_{\text{dis}} \frac{t}{N}} = -\frac{t}{N} \frac{\tilde{H}_{\text{dis}}}{\kappa} e^{-\tilde{H}_{\text{dis}} \frac{t}{N}} \quad \text{and} \quad \|e^{-\tilde{H}_{\text{dis}} \frac{t}{N}}\|, \|e^{-i\tilde{H}(\kappa t/N) \frac{t}{N}}\| \le 1. \tag{S141}$$

Using Eq. (S136), one can bound

$$\left\| \frac{\partial}{\partial \kappa} e^{-\tilde{H}_{\text{dis}} \frac{t}{N}} \right\| = \left\| \frac{t}{N} \frac{\tilde{H}_{\text{dis}}}{\kappa} e^{-\tilde{H}_{\text{dis}} \frac{t}{N}} \right\| \le \frac{t}{N\kappa} \|\tilde{H}_{\text{dis}}\| \le \frac{mt(d+1)}{2N}. \tag{S142}$$

Furthermore, using the definition of  $O_N$  in Eq. (S137), the norm bound in Eq. (S142), and the fact that  $\|e^{-\tilde{H}_{\text{dis}}\frac{t}{N}}\|, \|e^{-i\tilde{H}(\kappa t/N)\frac{t}{N}}\| \le 1$ , one can bound

$$\left\| \frac{\partial}{\partial \kappa} \sigma \right\| \le 2 \left\| \frac{\partial}{\partial \kappa} O_N \right\| \le \frac{2t}{\kappa} \|\tilde{H}_{\text{dis}}\| \le mt(d+1). \tag{S143}$$

This directly yields a bound on the desired distance:

$$\|\sigma - \mathcal{U}\rho(0)\|_{1} = \left\| \int_{0}^{\kappa} \frac{\partial}{\partial \kappa} \sigma d\kappa \right\|_{1} \le \int_{0}^{k} \left\| \frac{\partial}{\partial \kappa} \sigma \right\|_{1} d\kappa \le m\kappa t (d+1). \tag{S144}$$

Finally, this, together with Eqs. (S135, S144), implies that

$$\left\| \mathcal{T} \exp \left( \int_0^t \mathcal{L}(s) ds \right) \rho(0) - \mathcal{U} \rho(0) \right\|_1 \le \|\rho(t) - \sigma\|_1 + \|\mathcal{N}(\rho(0))\|_1 \le m\kappa t(d+1) + 1 - e^{-m\kappa t(d+1)} \le 2m\kappa t(d+1), \tag{S145}$$

which proves the lemma.

We will now show how one can use a single bosonic mode Hamiltonian to apply arbitrary single qubit gates with high fidelity, even when the nonlinearity is much smaller than the noise strength. We note that a similar result is already shown in Refs. [S14, S15]. To do this, we will consider a single bosonic mode with  $\kappa \gg U$ , where both the error rate and non-Gaussianity U are fixed, and study the effective error rate in the asymptotic limit of large Gaussian strength.

Lemma 16 (Single-qubit gates, from Ref. [S14]). Consider a single bosonic mode under the master equation

$$\frac{d}{dt}\rho = \mathcal{L}\rho = -i[H(t), \rho] + \sum_{l=1}^{2} \kappa_{l}\mathcal{D}_{L^{(l)}}\rho,$$

with Hamiltonian

$$H(t) = U(t)a^{\dagger 2}a^2 + \left(\Lambda_1(t)a^{\dagger} + \Lambda_2(t)a^{\dagger 2} + \text{h.c.}\right) + \Delta(t)a^{\dagger}a,$$

where  $\mathcal{D}_L \rho = L \rho L^{\dagger} - \{L^{\dagger} L, \rho\}/2$ ,  $L^{(1)} = a, L^{(2)} = a^{\dagger}$  and  $L^{(3)} = a^{\dagger} a = n$ , and  $\kappa_1 + \kappa_2 = \kappa$ , and the strength of the Gaussian terms is bounded by P,  $|\Lambda_1(t)|, |\Lambda_2(t)|, |\Delta(t)| \leq P$ . Then, for any single-qubit quantum unitary operation  $\mathcal{U}$  (i.e.  $\mathcal{U}(\cdot) = U(\cdot)U^{\dagger}$  for some single-qubit gate U), the Lindbladian  $\mathcal{L}(t)$  can approximate  $\mathcal{U}$ ,  $\|(\mathcal{T}e^{\int_0^t \mathcal{L}(s)ds} - \mathcal{U})\rho_0\|_1 \leq \tilde{O}(\kappa(U^2P)^{-1/3})$ , in time  $t = O((U^2P)^{-1/3})$ , with  $\rho_0$  a single-qubit state.

Proof. We will show that, by tuning the parameters in the Hamiltonian H(t), one can generate T, S, and  $\sqrt{X}$  gates, which is sufficient for arbitrary single-qubit rotations. For implementing a T gate or an S gate, one simply has to set  $\Omega(t) = 0$  and  $\Delta(t) = P$ . This yields the Hamiltonian  $H = U(a^{\dagger 2}a^2)/2 + Pa^{\dagger}a$ . Since there are no couplings between the states  $|0\rangle$ ,  $|1\rangle$  and the rest, we can restrict ourselves to the subspace spanned by  $\{|0\rangle, |1\rangle\}$ . Denoting the projector onto this subspace  $\Pi_1 = |0\rangle \langle 0| + |1\rangle \langle 1|$ , the projection of  $H_{\alpha}$  on the blockaded subspace yields  $\Pi_1 H \Pi_1 = P |1\rangle \langle 1|$ . Then, evolving under the Hamiltonian for time  $t = 3\pi/(2P)$  yields an S gate, while evolving for time  $t = 3\pi/(4P)$  yields a T gate. Therefore, applying the error bound in Lemma 15, T gates and S gates can be implemented with precision  $O(\kappa/P)$  in time t = O(1/P).

Now, let us consider the problem of applying a  $\sqrt{X}$  gate. This can be done by using the construction from Refs. [S14, S16], by going to a displaced frame. We will first show that, considering the Hamiltonian in a displaced frame, one can implement a fast  $\sqrt{X}$  gate. Then, we will show that one can go to the displaced frame by applying fast pulses at the beginning and end of the computation, hence enabling the application of a high-fidelity fast  $\sqrt{X}$  gate in the laboratory frame, even in the presence of errors.

First, let us consider the Hamiltonian in a frame displaced by  $\alpha(t)$ ,  $a \to a + \alpha(t)$ . We write the Hamiltonian in the displaced frame as  $H_{\alpha(t)}$  and the noise as  $\mathcal{D}_{L^{(l)};\alpha(t)}$ . Note that the noise in the displaced frame can be written as

$$\sum_{l=1}^{2} \kappa_{l} \mathcal{D}_{L^{(l)},\alpha(t)}(\cdot) = \sum_{l=1}^{2} \kappa_{l} \mathcal{D}_{L^{(l)}} + \frac{i}{2} (\kappa_{1} - \kappa_{2}) \left[ i(\alpha(t)a^{\dagger} - \alpha^{*}(t)a), (\cdot) \right]. \tag{S146}$$

Furthermore, the displaced Hamiltonian  $H_{\alpha(t)}$  may be written as

$$H_{\alpha(t)} = U(t)a^{\dagger 2}a^2 + \tilde{\Delta}(t)a^{\dagger}a + (\tilde{\Lambda}_1(t)a^{\dagger} + \tilde{\Lambda}_2(t)a^{\dagger 2} + \tilde{\Lambda}_3(t)a^{\dagger 2}a + \text{h.c.}), \tag{S147}$$

where

$$\tilde{\Delta}(t) = \Delta(t) + 4U(t)|\alpha(t)|^2,$$

$$\tilde{\Lambda}_2(t) = \Lambda_2(t) + 2U(t)\alpha(t)^2,$$

$$\tilde{\Lambda}_1(t) = \Lambda_1(t) + \alpha\Delta(t) + 2\alpha(t)^*\Lambda_2(t) + 2U(t)|\alpha(t)|^2\alpha(t) - \frac{1}{2}i\alpha(t)(\kappa_1 - \kappa_2),$$

$$\tilde{\Lambda}_3(t) = 2U(t)\alpha(t).$$
(S148)

where the noise term from Eq (S146) has already been absorbed into the Hamiltonian. The master equation in the displaced frame is then

$$\frac{d}{dt}\rho_{\alpha(t)} = \mathcal{L}_{\alpha(t)}\rho_{\alpha(t)} = -i[H_{\alpha(t)}, \rho_{\alpha(t)}] + \sum_{l=1}^{2} \kappa_l \mathcal{D}_{L^{(l)}}.$$
 (S149)

By suitably choosing the parameters so that  $\tilde{\Delta}(t) = \tilde{\Lambda}_1(t) = \tilde{\Lambda}_2(t) = 0$ , the Hamiltonian becomes  $H_{\alpha(t)} = 2U(t)\alpha(t)a^{\dagger}(n-1) + \text{h.c.}$ .

Crucially, one can notice that the Hamiltonian  $H_{\alpha(t)}$  is blockaded, since it does not contain couplings to state  $|2\rangle$ . Therefore, in the noiseless case, the dynamics will be restricted to the qubit subspace spanned by  $\{|0\rangle, |1\rangle\}$ . Denoting the projector onto this subspace by  $\Pi_1 = |0\rangle \langle 0| + |1\rangle \langle 1|$ , the projection of  $H_{\alpha(t)}$  onto the blockaded subspace yields  $\Pi_1 H_{\alpha(t)} \Pi_1 = -2U\alpha(t)X$ . Let us pick a constant  $\alpha(t) = \alpha_F$ . It is then clear that evolving under the Hamiltonian  $H_{\alpha F}$  for a time  $t = \pi/(8U\alpha_F)$  produces a  $\sqrt{X}$  gate.

We will pick the displacement to be  $\alpha_F = \Theta((P/U)^{1/3})$ , since it is the largest displacement that can simultaneously fulfill Eq. (S148) and the restriction that  $|\Lambda_1(t)|, |\Lambda_2(t)|, |\Delta(t)| \leq P$ .

Naturally, one is interested in performing operations in the laboratory frame, which means that at the beginning (t=0) and end  $(t=t_F)$  of the computation the displacement is  $\alpha(0)=\alpha(t_F)=0$ . This can be achieved by simply applying a displacement term in the beginning and end of the computation. Hence, the computation can be performed in three steps. First, a displacement term is applied for a time  $t_{\rm dis}$  to go from  $\alpha(0)=0$  to  $\alpha(t_{\rm dis})=\alpha_F$ . Then, the gate is performed in the frame displaced by  $\alpha_F$ , which takes time  $t_{\rm gate}=\pi/(8U\alpha_F)$ . Finally, the displacement is taken to 0 again, which takes time  $t_{\rm dis}$ . Therefore, the total computation time for a  $\sqrt{X}$  gate is  $t_{\sqrt{X}}=2t_{\rm dis}+t_{\rm gate}$ . In order to achieve the desired displacement  $\alpha_F$ , one can apply the Hamiltonian

$$H(t) = i(P - \alpha_F \kappa/2)(a^{\dagger} - a) + \frac{i}{2}(P - \alpha_F)t(\kappa_1 - \kappa_2)(a^{\dagger} - a), \tag{S150}$$

where the first term takes the system to the frame displaced by  $\alpha(t) = (P - \alpha_F \kappa/2)$ , and the second term corrects the contributions of the noise. The choice of parameters ensures that  $|\Lambda_1| \leq P$  at all times. Specifically, in the displaced frame, the system evolves under the master equation

$$\frac{d}{dt}\rho_{\alpha(t)} = \sum_{l=1}^{3} \kappa_l \mathcal{D}_{L^{(l)}} \quad \text{for} \quad t \le t_{\text{dis}}, \tag{S151}$$

with  $\alpha(0)=0$  and  $\alpha(t_{\rm dis})=\alpha_F$ , and  $t_{\rm dis}=\alpha_F/(P-\alpha_F)=O(\alpha_F/P)=O((P^2U)^{-1/3})$ . Let us denote the total evolution time by  $t_{\sqrt{X}}=2t_{\rm dis}+t_{\rm gate}$ . Note that  $t_{\rm gate}=O((U\alpha_F)^{-1})=O((PU^2)^{-1/3})$ , while  $t_{\rm dis}=O(\alpha_F/P)=O((P^2U)^{-1/3})$ . In the large P limit, it is clear that  $t_{\rm dis}\ll t_{\rm gate}$ , and the total time scales as  $t_{\sqrt{X}}=t_{\rm gate}+2t_{\rm dis}=O(t_{\rm gate})=O((PU^2)^{-1/3})$ . From the Solovay-Kitaev theorem, it follows that any single-qubit rotation can be approximated to precision  $\varepsilon$  in time  $t=O(t_{\sqrt{X}}\log^c(1/\varepsilon))$  for some constant c<2. We can now bound the total contribution of the error: straightforward application of Lemma 15 shows that the error after time  $t=\tilde{O}(t_{\sqrt{X}})=\tilde{O}((U^2P)^{-1/3})$  is

$$\|(\mathcal{T}e^{\int_0^t \mathcal{L}(s)ds} - \mathcal{U})\rho_0\|_1 \le \tilde{O}\left(\frac{\kappa}{(U^2P)^{1/3}}\right),\tag{S152}$$

where  $\tilde{O}$  hides polylogarithmic factors. This proves the lemma.

So far we have shown that one can make arbitrary single-qubit gates with high fidelity even if the noise is much larger than the non-Gaussianity,  $\kappa \gg U$ , as long as one can increment the strength of the Gaussian terms,  $P \gg \kappa^3/U^2$ . We will now show how to implement entangling gates, which is enough to obtain a universal gate-set.

Lemma 17 (Two-qubit gates). Consider two bosonic modes evolving under the master equation

$$\frac{d}{dt}\rho(t) = -i[H(t), \rho(t)] + \sum_{l=1}^{2} \sum_{v=1}^{2} \kappa_l \mathcal{D}_{L_v^{(l)}},$$
 (S153)

where H(t) is the Hamiltonian  $H(t) = H_1(t) + H_2(t) + ig(t)[a_1a_2^{\dagger} - a_1^{\dagger}a_2]$ , with

$$H_i(t) = U_i(t)a_i^{\dagger 2}a_i^2 + \left(\Lambda_{i,1}(t)a_i^{\dagger} + \Lambda_{i,2}(t)a_i^{\dagger 2} + \text{h.c.}\right) + \Delta_i(t)a_i^{\dagger}a_i, \tag{S154}$$

and  $\mathcal{D}_L \rho = L \rho L^{\dagger} - \{L^{\dagger} L, \rho\}/2$ ,  $L_v^{(1)} = a_v$ ,  $L_v^{(2)} = a_v^{\dagger}$ , and  $\kappa_1 + \kappa_2 = \kappa$ . Assume that the strength of the Gaussian terms is bounded by  $P(|\Lambda_{i,1}(t)|, |\Lambda_{i,2}(t)|, |\Delta_i(t)|, |g(t)| \leq P)$ .

Then, for any two-qubit quantum unitary operation  $\mathcal{U}$  (i.e.  $\mathcal{U}(\cdot) = U(\cdot)U^{\dagger}$  for some single-qubit gate U), the Lindbladian  $\mathcal{L}(t)$  can implement a time evolution that approximates  $\mathcal{U}$ ,  $\|(\mathcal{T}e^{\int_0^t \mathcal{L}(s)ds} - \mathcal{U})\rho_0\|_1 \leq \tilde{O}(\kappa(U^2P)^{-1/3})$ , for a time  $t = O((U^2P)^{-1/3})$ , with  $\rho_0$  a two-qubit state.

*Proof.* In Lemma 16 it is shown how to use H(t) to generate arbitrary single-qubit gates on either of the modes with arbitrarily high fidelity. Hence, it is only necessary to show how to apply an entangling two-qubit gate in order to have a universal gate-set.

To do this, let us consider the collective modes  $b_1 = (a_1 + a_2)/\sqrt{2}$  and  $b_2 = (a_1 - a_2)/\sqrt{2}$ . We will denote by  $|j,k\rangle_{a_1,a_2} = (j!\,k!)^{-1/2}(a_1^{\dagger})^j(a_2^{\dagger})^k\,|0,0\rangle$  the Fock states in the original basis, and  $|j,k\rangle_{n_1,n_2} = (j!\,k!)^{-1/2}(b_1^{\dagger})^j(b_2^{\dagger})^k\,|0,0\rangle$ . One obtains that

$$\begin{split} |0,0\rangle_{a_{1},a_{2}} &= |0,0\rangle_{b_{1},b_{2}}\,,\\ |0,1\rangle_{a_{1},a_{2}} &= \frac{1}{\sqrt{2}}\left(|1,0\rangle_{b_{1},b_{2}} - |0,1\rangle_{b_{1},b_{2}}\right),\\ |1,0\rangle_{a_{1},a_{2}} &= \frac{1}{\sqrt{2}}\left(|1,0\rangle_{b_{1},b_{2}} + |0,1\rangle_{b_{1},b_{2}}\right),\\ |1,1\rangle_{a_{1},a_{2}} &= \frac{1}{2}\left(|2,0\rangle_{b_{1},b_{2}} - |0,2\rangle_{b_{1},b_{2}}\right). \end{split} \tag{S155}$$

Let us now denote by U the single-mode unitary that maps  $U|0\rangle_{b_1}=|0\rangle_{b_1},\ U|1\rangle_{b_1}=i|1\rangle_{b_1},\ U|2\rangle_{b_1}=|2\rangle_{b_1}$ . Using Eq. (S155), it can be seen that U will act in the  $a_1,a_2$  basis as

$$\begin{split} &U\left|0,0\right\rangle_{a_{1},a_{2}}=\left|0,0\right\rangle_{a_{1},a_{2}},\\ &U\left|0,1\right\rangle_{a_{1},a_{2}}=\frac{1}{2}\left(\left(1+i\right)\left|0,1\right\rangle_{a_{1},a_{2}}-\left(1-i\right)\left|1,0\right\rangle_{a_{1},a_{2}}\right),\\ &U\left|1,0\right\rangle_{a_{1},a_{2}}=\frac{1}{2}\left(-\left(1-i\right)\left|0,1\right\rangle_{a_{1},a_{2}}+\left(1+i\right)\left|1,0\right\rangle_{a_{1},a_{2}}\right),\\ &U\left|1,1\right\rangle_{a_{1},a_{2}}=\left|1,1\right\rangle_{a_{1},a_{2}}. \end{split} \tag{S156}$$

Hence, U is clearly an entangling gate between modes  $a_1$  and  $a_2$ . Furthermore, U can be implemented in a fast manner using the same technique as in Lemma 16. Let us detail the procedure. First, one can evolve the system under the term  $P(a_1^{\dagger}a_2 + \text{h.c})$ , which induces the mixing of the modes  $a_1 \to b_1$  and  $a_2 \to b_2$  in time t = O(1/P). The Hamiltonian in the new basis,  $H_b(t)$ , may be written us

$$H_b(t) = U_1 b_1^{\dagger 2} b_1^2 + (\Lambda_{1,1} b_1^{\dagger} + \Lambda_{1,2} b_1^{\dagger 2} + \text{h.c.}) + \Delta_1 b_1^{\dagger} b_1, \tag{S157}$$

where we have chosen  $\Delta_2 = \Lambda_{2,1} = \Lambda_{2,2} = U_2 = 0$ . One can note that the technique in Lemma 16 can be readily applied to the Hamiltonian  $H_b$  in Eq. (S157). That is, one can go to a frame in which  $b_1$  is displaced by  $\alpha(t)$ ,  $b_1 \to b_1 + \alpha(t)$ . As shown in the proof of Lemma 16, a suitable choice of the parameters leads to the displaced Hamiltonian  $H_{b,\alpha(t)} = U_1(t)(b_1^{\dagger})^2b_1^2 + 2U_1[\alpha(t)b_1^{\dagger}(b_1^{\dagger}b_1 - 2) + \text{h.c.}]$ . Note that this Hamiltonian contains no couplings between  $|2\rangle_{b_1}$  and  $|3\rangle_{b_1}$ , and hence the subspace spanned by  $\{|0\rangle_{b_1}, |1\rangle_{b_1}, |2\rangle_{b_1}\}$  is blockaded. Furthermore, one can rewrite

$$H_{b,\alpha(t)} = U_1(t)(b_1^{\dagger})^2 b_1^2 + 2U_1(t) \operatorname{Re}(\alpha(t)) H_{\alpha,R} + 2U_1(t) \operatorname{Im}(\alpha(t)) H_{\alpha,I},$$
 (S158)

with  $H_{\alpha(t),R} = b_1^{\dagger}(b_1^{\dagger}b_1 - 2) + (b_1^{\dagger}b_1 - 2)b_1$  and  $H_{\alpha(t),I} = i(b_1^{\dagger}(b_1^{\dagger}b_1 - 2) - (b_1^{\dagger}b_1 - 2)b_1)$ . One can compute the commutator  $[H_{\alpha(t),R}, H_{\alpha(t),I}] = 2i(3b_1^{\dagger^2}b_1^2 - 6b_1^{\dagger}b_1 + 4)$ , which is diagonal, and can clearly implement the gate U, which consists

only of a phase rotation of the state  $|1\rangle_{b_1}$ . In fact, the analysis in Ref. [S14] shows that one can generate arbitrary unitaries in the subspace spanned by  $\{|0\rangle_{b_1}, |1\rangle_{b_1}, |2\rangle_{b_1}\}$ .

Following the analysis in Lemma 16, the gate U can then be implemented in time  $t_U = O((U^2P)^{-1/3})$ . This is also the dominant source of error, since applying the displacement takes time  $t_{\text{dis}} = O((P^2U)^{-1/3})$ , and going to the collective mode  $b_1$  takes time  $t_b = O(1/P)$ , and therefore  $t_U \gg t_{\text{dis}}, t_b$ . Hence, the total error will be  $O(\kappa t_U) = O(\kappa (U^2P)^{1/3})$ .

Therefore, we have shown how to implement an entangling gate. Together with the implementation of arbitrary single-qubit gates and the Solovay-Kitaev theorem (which introduces and additional polylogarithmic factor), this proves that any 2-qubit gate  $\mathcal{U}$  can be implemented by evolving the Lindbladian  $\mathcal{L}(t)$  up to precision

$$\|(\mathcal{T}e^{\int_0^t \mathcal{L}(s)ds} - \mathcal{U})\rho_0\|_1 \le \tilde{O}\left(\frac{\kappa}{(U^2P)^{1/3}}\right),\tag{S159}$$

where  $\rho_0$  is a two-qubit state, and the error bound follows directly from Lemma 15.

So far, we have shown how the bosonic Hamiltonian can be used to generate high-fidelity universal gates. Specifically, we have seen that 2-qubit gates can be implemented in time  $t = \tilde{O}((PU^2)^{-1/3})$ , where U is the non-Gaussian strength, and P refers to the maximum absolute value allowed for the Gaussian terms of the Hamiltonian. Let us now consider a system with nL bosonic modes as described in section IE and study the asymptotic scaling with n. In this case,  $|J_{i,j}^{\alpha,\alpha'}(t)|, |\Omega_i^{\alpha}(t)| \leq P$ . Let us assume that  $J,\Omega = \Theta(P)$  (this is the case, for example, for geometrically local Hamiltonians). Then, provided that the Gaussian couplings  $J,\Omega = O(1)$  can be arbitrarily large constants, it follows from Lemma 17 that any gate can be implemented to an arbitrarily small (but independent of n) precision. Since this allows for the implementation of gates with an effective gate error below that of the threshold theorem [S8–S10], this implies that fault-tolerant circuits can be implemented. We remark that, in addition to high-fidelity gates, fault-tolerant constructions usually require the ability to implement RESTART operations to provide fresh qubits [S9]. For spin systems in the presence of non-unital noise, cooling algorithms [S17–S19] in conjunction with the noise channel can be leveraged to implement such an operation [S20–S22]. In our case, a similar scheme would be needed; however, we leave a careful analysis of the construction for future work.

## B. High-noise regime of the fermionic model is not separable at all times

For the bosonic model, Theorem 2 establishes that, in the presence of a sufficiently incoherent high particle loss or incoherent particle gain, the state of the bosonic model is separable at all times. In this subsection, we show that such a result cannot be true for the fermionic model. We show this for two notions of separability for fermions [S23, S24]—the first notion holds for all observables, and the second weaker notion holds for parity-conserving, or even, observables.

Throughout this section, it will be enough for us to consider separability in the bi-partite setting. We will consider m fermionic modes which are divided into two subgroups of modes, A with modes  $\{1, 2, \ldots, m_A\}$  and B with modes  $\{m_A+1, m_A+2, \ldots, m\}$ . Recall that an operator on the fermionic Hilbert space is an element of the algebra generated by  $\{c_v^1, c_v^2\}_{v \in \{1, 2, \ldots m\}}$  or alternatively by  $\{a_v, a_v^{\dagger}\}_{v \in \{1, 2, \ldots m\}}$ . An operator acting on sub-system A will be an element of the algebra generated by  $\{a_v, a_v^{\dagger}\}_{v \in \{1, 2, \ldots m_A\}}$  and, similarly, an operator acting on the sub-system B will be an element of the algebra generated by  $\{a_v, a_v^{\dagger}\}_{v \in \{m_A+1, m_A+2, \ldots m_B\}}$ . The parity operator of a set  $S \subseteq \{1, 2, \ldots m\}$  of fermionic modes is  $P_A = \exp(i\pi \sum_{i \in S} a_i^{\dagger} a_i)$ . Operators that conserve the parity operator are called *even operators*. Physically relevant states of the fermionic modes are restricted to be even operators—note, however, that a physical operator that is even on all the fermionic modes is not necessarily even on a subset of these fermionic modes.

**Definition 1.** A state  $\rho$  of m fermionic modes will be called a **product state with respect to all observables** on the bi-partition A|B if there exist states  $\rho_A$  for the modes in A and  $\rho_B$  for the modes in B such that, for all operators  $O_A$  supported on A and  $O_B$  supported on B,

$$\operatorname{Tr}(O_A O_B \rho) = \operatorname{Tr}(O_A \rho_A) \operatorname{Tr}(O_B \rho_B).$$

A state  $\rho$  of the m fermionic modes will be called a **separable state** with respect to all observables on the bi-partition A|B if it can be expressed as a convex-combination of such product states.

We remark that it was shown in Ref. [S24] that if  $\rho$  is an even operator, which is also a product state as per definition 1, then  $\rho_A$  and  $\rho_B$  are also both even operators.

**Definition 2.** A state  $\rho$  of m fermionic modes will be called a **product state with respect to even observables** on the bi-partition A|B if there exist states  $\rho_A$  for the modes in A and  $\rho_B$  forthe modes in B such that, for all even operators  $O_A^{(+)}$  supported on A and  $O_B^{(+)}$  supported on B,

$$\operatorname{Tr}(O_A^{(+)}O_B^{(+)}\rho) = \operatorname{Tr}(O_A^{(+)}\rho_A)\operatorname{Tr}(O_B^{(+)}\rho_B).$$

A state  $\rho$  of the m fermionic modes will be called a **separable state with respect to even observables** on the bi-partition A|B if it can be expressed as a convex-combination of such product states.

As discussed in Ref. [S23], while separability with respect to all observables implies separability with respect to even observables, the converse is not necessarily true. This can be seen explicitly in a simple 2-mode example—consider the state  $|\psi\rangle=(a_1^\dagger+a_2^\dagger)|\mathrm{vac}\rangle/\sqrt{2}$ . This state is not separable as per definition 1—to see this, one can use the 2-mode separability criteria from Refs. [S23, S24], which we also provide in Lemma 18. However, this state is separable as per definition 2—to see this, we note that, for any even observable  $O_1^{(+)}$  on the first fermionic mode and  $O_2^{(+)}$  on the second fermionic mode,

$$\langle \psi | O_1^{(+)} O_2^{(+)} | \psi \rangle = \frac{1}{2} \left( \langle \phi_1 | O_1^{(+)} | \phi_1 \rangle \langle \phi_2 | O_2^{(+)} | \phi_2 \rangle + \langle \theta_1 | O_1^{(+)} | \theta_1 \rangle \langle \theta_2 | O_2^{(+)} | \theta_2 \rangle \right), \tag{S160}$$

where  $|\phi_1\rangle = a_1^{\dagger} |\text{vac}\rangle, |\phi_2\rangle = |\text{vac}\rangle, |\theta_1\rangle = |\text{vac}\rangle \text{ and } |\theta_2\rangle = a_2^{\dagger} |\text{vac}\rangle.$

## 1. Non-separability for any observable

Here, we provide a simple 2-mode example which shows that, unlike the bosonic model, no matter how high the rate of particle loss and incoherent particle gain is in the fermionic model, the dynamics of the fermionic model is not separability preserving with respect to all observables (definition 1). To establish this result, we first review the 2-mode separability criteria from Refs. [S23, S24].

**Lemma 18** (2-mode separability, Refs. [S23, S24]). A 2-mode density matrix  $\rho$  is separable with respect to all observables (definition 1) if and only if it is diagonal in the computational basis.

**Proposition 1.** Consider a system with m=2 fermionic modes, with the sub-system A with mode 1 and sub-system B with mode 2 whose density matrix  $\rho(t)$  satisfies the Lindblad master equation

$$\frac{d}{dt}\rho(t) = -i[J(a_1^{\dagger}a_2 + a_2^{\dagger}a_1), \rho(t)] + \sum_{i=1}^{4} \left(\kappa_1 \mathcal{D}_{a_j} + \kappa_2 \mathcal{D}_{a_j^{\dagger}}\right) \rho(t),$$

Then,  $\forall \kappa_1, \kappa_2 > 0$ ,  $\exists \rho(0)$  which is separable with respect to all observables (Definition 2) such that  $\rho(t)$  cannot be separable for all  $t \geq 0$ .

*Proof.* Throughout this proof, "separability" refers to separability with respect to all observables (Definition 1). Consider the initial state  $\rho(0) = a_1^{\dagger} |\text{vac}\rangle\langle\text{vac}| a_1$ . Note that  $\rho(0)$  is trivially separable—we now establish that, for a small time t,  $\rho(t) = e^{\mathcal{L}t}(\rho(0))$  is not separable to  $O(t^2)$  for any  $\kappa$ , which is enough to contradict separability of  $\rho(t)$  at all times t. Now,

$$\rho(t) = \rho(0) + t\mathcal{L}\rho(0) + O(\varepsilon^2), \tag{S161}$$

which, in the computational basis (i.e.  $|0,0\rangle = |\mathrm{vac}\rangle$ ,  $|1,0\rangle = a_1^\dagger |\mathrm{vac}\rangle$ ,  $|0,1\rangle = a_2^\dagger |\mathrm{vac}\rangle$ ,  $|1,1\rangle = a_1^\dagger a_2^\dagger |\mathrm{vac}\rangle$ ), satisfies  $|\langle 1,0|\,\rho(\varepsilon)\,|0,1\rangle| = Jt + O(t^2)$ . From the separability criteria in Lemma 18, it then follows that there cannot exist a separable state  $\sigma(t)$  such that  $\|\rho(t) - \sigma(t)\|_1 \leq O(t^2)$ , no matter what the rate  $\kappa$  is.

While the analysis above indicates that there would be times when the state  $\rho(t)$  would be entangled, we can also analyze the time-scale at which this entanglement is developed. In Fig. S3, we simulate the two-fermionic-mode model from Proposition 1 for  $\kappa_1 = \kappa_2 = \kappa$  and numerically compute the entanglement measure  $E(\rho) = \sum_{b,b':b\neq b'} |\rho_{b,b'}|$  (i.e., the 1-norm of a vector formed with the off-diagonal elements of  $\rho$ ) as a function of t. Note that from Lemma 18, this measure quantified how non-separable the two-mode state is when considering all observables. We observe that this measure becomes 0 at long times, however it is largest at time  $t^* \sim 1/\kappa$  — thus consistent with the analysis of Proposition 1, even at large  $\kappa$ , the fermionic state becomes entangled at short times and, unlike the bosonic model, does not exhibit a threshold behavior of transitioning to an always separable state at sufficiently large  $\kappa$ .

![](_page_39_Figure_1.jpeg)

FIG. S3. Numerical simulation of the two-fermionic-mode model considered in Proposition 1 with both particle loss rate  $\kappa_1$  and particle gain rate  $\kappa_2$  set to  $\kappa$  and  $\rho(0) = a_1^{\dagger} |\text{vac}\rangle\langle\text{vac}| a_1$ . (a) Time evolution of the entanglement measure computed by adding all off-diagonal elements of the two-mode density matrix of the model. As per Lemma 18, this quantifies non-separability with respect to all observables for 2-mode fermionic systems. (b) The time  $t^*$  at which the entanglement measure computed in (a) is maximum as a function of  $\kappa$ . We see that entanglement is developed at time-scales  $t^* \sim 1/\kappa$  no matter how large  $\kappa$  is.

#### 2. Non-separability for even observables

We will use the following lemma, which reduces the problem of checking the non-separability of a 4-mode fermionic state with respect to even observables to an effective problem with 2 qubits.

**Lemma 19.** Suppose  $\rho$  is a state of m=4 fermionic modes, with sub-system A with modes 1 and 2 and sub-system B with modes 3 and 4, and suppose the 2-qubit state  $\sigma = (Q_{A,e}Q_{B,o})\rho(Q_{A,e}^{\dagger}Q_{B,o}^{\dagger})$ , where

$$Q_{A,e} = |0_A\rangle\langle \text{vac}| + |1_A\rangle\langle \text{vac}| a_1 a_2, Q_{B,o} = |0_B\rangle\langle \text{vac}| a_3 + |1_B\rangle\langle \text{vac}| a_4,$$

is entangled, then  $\rho$  is not separable with respect to even observables.

*Proof.* This lemma follows by contradiction—let us assume that  $\rho$  is separable with respect to even observables. Now, for any two operators  $O_A, O_B \in \mathbb{C}^{2\times 2}$ , consider the even observables

$$O_A^{(+)} = Q_{A,e}^{\dagger} O_A Q_{A,e} \text{ and } O_B^{(+)} = Q_{B,o}^{\dagger} O_B Q_{B,o}.$$
 (S162)

Note that  $O_A^{(+)}$  acts on the fermionic modes in A and  $O_B^{(+)}$  acts on the fermionic modes in B. We note also that

$$\text{Tr}(O_A^{(+)}O_B^{(+)}\rho) = \text{Tr}(O_A O_B \sigma).$$
 (S163)

Now, since  $\rho$  is separable with respect to even observables by assumption, it follows that  $\exists \rho_{A,x}, \rho_{B,x}$  and a probability measure  $\mu$  such that

$$Tr(O_A^{(+)}O_B^{(+)}\rho) = \int Tr(O_A^{(+)}\rho_{A,x})Tr(O_B^{(+)}\rho_{B,x})d\mu(x),$$
 (S164)

and consequently, using Eq. (S162), we find that

$$Tr(O_A O_B \sigma) = \int Tr(O_A \sigma_{A,x}) Tr(O_B \sigma_{B,x}) d\mu(x), \tag{S165}$$

where  $\sigma_{A,x}=Q_{A,e}\rho_{A,x}Q_{A,e}^{\dagger}$  and  $\sigma_{B,x}=Q_{B,o}\rho_{B,x}Q_{B,o}^{\dagger}$ . This would imply that  $\sigma$  is separable and therefore, by contradiction, we conclude that  $\rho$  cannot be separable even with respect to even observables.

**Proposition 2.** Consider a system with m=4 fermionic modes, with the sub-system A with modes 1 and 2 and sub-system B with modes 3 and 4, whose density matrix  $\rho(t)$  satisfies the Lindblad master equation

$$\frac{d}{dt}\rho(t) = -i[J(a_2a_3 + a_3^{\dagger}a_2^{\dagger}), \rho(t)] + \sum_{i=1}^{4} \left(\kappa_1 \mathcal{D}_{a_i} + \kappa_2 \mathcal{D}_{a_j^{\dagger}}\right)\rho(t).$$

Then,  $\forall \kappa_1, \kappa_2 > 0$ ,  $\exists \rho(0)$  which is separable with respect to even observables (Definition 2) such that  $\rho(t)$  cannot be separable for all  $t \geq 0$ .

*Proof.* Throughout this proof, "separability" refers to separability with respect to even observables (Definition 2). We choose  $\rho(0) = |\psi(0)\rangle\langle\psi(0)|$ , where

$$|\psi(0)\rangle = \frac{1}{\sqrt{2}} \left( a_1^{\dagger} |\text{vac}\rangle + a_4^{\dagger} |\text{vac}\rangle \right).$$
 (S166)

It can be noted that  $\rho(0)$  is separable with respect to even observables since, for any even observables  $O_A^{(+)}$  on A and  $O_B^{(+)}$  on B,

$$\operatorname{Tr}(\rho(0)O_{A}^{(+)}O_{B}^{(+)}) = \frac{1}{2} \left\langle \psi_{A}^{(1)} | O_{A}^{(+)} | \psi_{A}^{(1)} \right\rangle \left\langle \psi_{B}^{(1)} | O_{B}^{(+)} | \psi_{B}^{(1)} \right\rangle + \frac{1}{2} \left\langle \psi_{A}^{(2)} | O_{A}^{(+)} | \psi_{A}^{(2)} \right\rangle \left\langle \psi_{B}^{(2)} | O_{B}^{(+)} | \psi_{B}^{(2)} \right\rangle, \tag{S167}$$

where  $|\psi_A^{(1)}\rangle = a_1^\dagger |\operatorname{vac}\rangle$ ,  $|\psi_B^{(1)}\rangle = |\operatorname{vac}\rangle$ ,  $|\psi_A^{(2)}\rangle = |\operatorname{vac}\rangle$ , and  $|\psi_B^{(2)}\rangle = a_4^\dagger |\operatorname{vac}\rangle$ . Again, to show that  $\rho(t)$  is not separable for all t>0, it is enough to show that there isn't a separable state  $\sigma(t)$  such that  $\|\rho(t)-\sigma(t)\|_1 \leq O(t^2)$  as  $t\to 0$ . To show this, we consider a first-order expansion of  $\rho(t)$ :

$$\rho(t) = \rho(0) + t\mathcal{L}\rho(0) + O(t^2)$$

$$= |\psi(t)\rangle\langle\psi(t)| + t\sum_{j=1}^{4} \left(\kappa_1 \mathcal{D}_{a_j}(|\psi(0)\rangle\langle\psi(0)|) + \kappa_2 \mathcal{D}_{a_j^{\dagger}}(|\psi(0)\rangle\langle\psi(0)|)\right) + O(t^2), \tag{S168}$$

where  $|\psi(t)\rangle = (a_1^\dagger + a_4^\dagger - ita_3^\dagger a_2^\dagger a_1^\dagger - ita_3^\dagger a_2^\dagger a_4^\dagger) |\operatorname{vac}\rangle / \sqrt{2}$ . We can now compute the state  $\sigma(t) = (Q_{A,e}Q_{B,o})\rho(t)(Q_{B,o}^\dagger Q_{A,e}^\dagger)$  defined in Lemma 19, which effectively amounts to projecting  $\rho(t)$  on the subspace spanned by  $\{a_3^\dagger |\operatorname{vac}\rangle, a_4^\dagger |\operatorname{vac}\rangle, a_3^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle, a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4^\dagger a_2^\dagger a_1^\dagger |\operatorname{vac}\rangle + a_4$

$$\sigma = ((1 - (\kappa_1 + \kappa_2)t) | 0_A, 1_B \rangle - it | 1_A, 0_B \rangle)((1 - (\kappa_1 + \kappa_2)t) \langle 0_A, 1_B | + it \langle 1_A, 0_B |) + O(t^2), \tag{S169}$$

It is easy to see that  $\forall \kappa_1, \kappa_2 > 0$ ,  $\sigma(t)$  (as a 2-qubit state), does not admit an  $O(t^2)$  separable approximation for sufficiently small t. Consequently, from Lemma 19, we find that  $\rho(t)$  (as a 4-mode fermionic state) does not admit an  $O(t^2)$  separable approximation, thus proving the lemma.

To analyze the timescales at which the state  $\rho(t)$  becomes non-separable relative to even observables, in Fig. S4, we numerically simulate the four-fermionic-mode model from Proposition 2 with  $\kappa_1 = \kappa_2 = \kappa$  and compute  $\rho(t)$ . To quantify the extent to which  $\rho(t)$  is non-separable, we first construct the effective two-qubit state  $\sigma(t) = Q_{A,e}Q_{B,o}\rho(t)Q_{B,o}^{\dagger}Q_{A,e}^{\dagger}$  from  $\rho(t)$  defined in Lemma 19 and then compute the minimum eigenvalue of its partial transpose. The negative of this minimum eigenvalue is the entanglement measure shown in Fig. S4(a). We find that, while at long times  $\sigma$  has a non-negative partial transpose and is thus separable, at short times  $\sigma$  is entangled irrespective of how large  $\kappa$  is. Furthermore, the minimum eigenvalue of the partial transpose of  $\sigma$  is attained at  $t^* \sim 1/\kappa$  [Fig. S4(b)], which sets the time-scale at which non-separability with respect to even observables in this system is developed.

<sup>[</sup>S1] C. V. Kraus, A quantum information perspective of fermionic quantum many-body systems, Ph.D. thesis, Technische Universität München (2009).

<sup>[</sup>S2] J. Surace and L. Tagliacozzo, SciPost Phys. Lect. Notes, 54 (2022).

<sup>[</sup>S3] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to algorithms (MIT press, 2022).

<sup>[</sup>S4] M. Fagotti and P. Calabrese, J. Stat. Mech.-Theory E. 2010, P04016 (2010).

<sup>[</sup>S5] B. M. Terhal and D. P. DiVincenzo, Phys. Rev. A 65, 032325 (2002).

<sup>[</sup>S6] E. Knill, arXiv preprint quant-ph/0108033 (2001).

<sup>[</sup>S7] T. Kuwahara, T. V. Vu, and K. Saito, Nat. Commun. 15, 2520 (2024).

<sup>[</sup>S8] K. Noh and C. Chamberland, Phys. Rev. A 101, 012316 (2020).

<sup>[</sup>S9] D. Aharonov and M. Ben-Or, SIAM J. Comput. 38, 1207 (2008).

<sup>[</sup>S10] T. Matsuura, N. C. Menicucci, and H. Yamasaki, arXiv preprint arXiv:2410.12365 (2024).

<sup>[</sup>S11] A. Mari and J. Eisert, Phys. Rev. Lett. 109, 230503 (2012).

<sup>[</sup>S12] R. Hudson, Rep. Math. Phys 6, 249 (1974).

<sup>[</sup>S13] M. Walschaers, PRX Quantum 2, 030204 (2021).

<sup>[</sup>S14] M. Yuan, A. Seif, A. Lingenfelter, D. I. Schuster, A. A. Clerk, and L. Jiang, arXiv preprint arXiv:2312.15783 (2023).

![](_page_41_Figure_1.jpeg)

FIG. S4. Numerical simulation of the four-mode fermionic model considered in Proposition 2 with both particle loss rate  $\kappa_1$  and particle gain rate  $\kappa_2$  set to  $\kappa$  and  $|\psi(0)\rangle = (a_1^{\dagger} + a_4^{\dagger})|\text{vac}\rangle$ . (a) Time evolution of the entanglement measure computed by first computing the two-qubit state  $\sigma(t)$  corresponding to the 4-mode fermionic state  $\rho(t)$  from Lemma 19 and then computing (the negative) of the minimum eigenvalue of its partial transpose. As per Lemma 19, this quantifies non-separability with respect to all observables for 2-mode fermionic systems. (b) The time  $t^*$  at which the entanglement measure computed in (a) is maximum as a function of  $\kappa$ — we see that entanglement is developed at time-scales  $t^* \sim 1/\kappa$  no matter how large  $\kappa$  is.

- [S15] A. Eickbusch, V. Sivak, A. Z. Ding, S. S. Elder, S. R. Jha, J. Venkatraman, B. Royer, S. M. Girvin, R. J. Schoelkopf, and M. H. Devoret, Nat. Phys. 18, 1464 (2022).
- [S16] A. Lingenfelter, D. Roberts, and A. A. Clerk, Sci. Adv. 7, eabj1916 (2021).
- [S17] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and R. Vrijen, Proceedings of the National Academy of Sciences 99, 3388 (2002).
- [S18] L. J. Schulman and U. V. Vazirani, in Proceedings of the Thirty-First Annual ACM Symposium on Theory of Computing, STOC '99 (Association for Computing Machinery, New York, NY, USA, 1999) p. 322–329.
- [S19] Á. M. Alhambra, M. Lostaglio, and C. Perry, Quantum 3, 188 (2019).
- [S20] M. Ben-Or, D. Gottesman, and A. Hassidim, arXiv preprint arXiv:1301.1995 (2013).
- [S21] R. Trivedi and J. I. Cirac, Phys. Rev. Lett. 129, 260405 (2022).
- [S22] O. Shtanko and K. Sharma, arXiv preprint arXiv:2411.04819 (2024).
- [S23] M.-C. Bañuls, J. I. Cirac, and M. M. Wolf, Phys. Rev. A 76, 022311 (2007).
- [S24] H. Moriya, J. Phys. A-Math. Gen. **39**, 3753 (2006).