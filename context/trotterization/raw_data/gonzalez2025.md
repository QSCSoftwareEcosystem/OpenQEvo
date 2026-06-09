Dynamical complexity of non-Gaussian many-body systems with dissipation

$$1,2 3,4 1,2 1,2 ∗$$

Guillermo Gonz´alez-Garc´ıa , Alexey V. Gorshkov , J. Ignacio Cirac , and Rahul Trivedi Max-Planck-Institut fu¨r Quantenoptik, Hans-Kopfermann-Str. 1, 85748 Garching, Germany Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, D-80799 Munich, Germany Joint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA. Joint Center for Quantum Information and Computer Science, NIST/University of Maryland, College Park, Maryland 20742, USA. (Dated: October 21, 2025) Wecharacterizethedynamicalstateofmany-bodybosonicandfermionicmany-bodymodelswith inter-site Gaussian couplings, on-site non-Gaussian interactions and local dissipation comprising incoherent particle loss, particle gain, and dephasing. We ﬁrst establish that, for fermionic systems, if the dephasing noise is larger than the non-Gaussian interactions, irrespective of the Gaussian coupling strength, the system state is a convex combination of Gaussian states at all times. Furthermore, for bosonic systems, we show that if the particle loss and particle gain rates are larger than the Gaussian inter-site couplings, the system remains in a separable state at all times. Building on this characterization, we establish that at noise rates above a threshold, there exists a classical algorithm that can eﬃciently sample from the system state of both the fermionic and bosonic mod-

els. Finally, we show that, unlike fermionic systems, bosonic systems can evolve into states that are not convex-Gaussian even when the dissipation is much higher than the on-site non-Gaussianity. Similarly, unlike bosonic systems, fermionic systems can generate entanglement even with noise rates much larger than the inter-site couplings.

Introduction. Whether many-body quantum systems sequently, there are two relevant frequency scales: the h evolve into classically non-trivial states under decoherstrength of the Gaussian couplings, J, and that of the onp ence is of fundamental interest to the theory of open site (non-Gaussian) interactions, U. If $J=0$ or $U=0$, t quantum systems and also has implications for the quanthis model is classically simulable. When $J=0$, the n tumadvantageinquantumcomputersandsimulators[1– Hamiltonian is a sum of single-site terms which maps 6]. Traditionally, this has been mostly studied for manyproduct states to product states which can be classically body spin models, including extensive recent activity in simulated. When $U=0$, the dynamics is Gaussian and [ both the discrete-time setting (i.e. quantum circuits inthus local observables can be eﬃciently computed and,

terspersed with noise) and in the continuous-time setfor fermions, even sampling is eﬃcient [33–36]. How2 ting(modeledbyamany-bodyLindbladmasterequation ever, when both J,$U=0$ and the system is noiseless, [7, 8]). For discrete-time models, early results showed this model is universal for quantum computation [37, 38] that suﬃciently high noise suppresses entanglement thus and thus worst-case hard to simulate classically. While 6 enabling classical simulation [9]. Recent results have the presence of dissipation should make the model classi5 shown classical simulability, even with a small amount of cally simulable, the amount and type of local dissipation 0 depolarizing noise, for both sampling or computing local needed remains unclear. 2 observables in both random [10–19] and structured modFor fermionic systems, the impact of noise on non0 els [20–22]. These results have partly been generalized Gaussianity was studied in a circuit model with Gaus5 to the geometrically-local continuous-time setting, which sian gates and non-Gaussian ancillas, which showed that 2 more accurately models analog quantum simulators, to the state remains a convex combination of Gaussian v show that the system remains classically simulable when states above a noise-threshold[39–41]. Studies analyzi the noise rate is larger than the interaction terms in the ing continuous-time dynamics have focused on the nonX Hamiltonian [8]. Gaussianity introduced via two-body dissipation [7]. For Quantum simulators based on platforms such as ultrabosonic systems, previous studies have either focused on cold atoms in optical lattices [23–27], superconducting understanding their complexity as a function of evolucircuits [28, 29] or nonlinear photonics [30–32], are often tion time in the absence of noise [42–44], or for the described by a family of Hamiltonians that, only in cerspeciﬁc task of boson sampling in the presence of noise tain regimes, reduce to spin systems. They are modeled [45–49]. However, the classical simulability of the noisy by a fermionic or bosonic lattice with two kinds of terms: continuous-time model motivated above remains unre(i) Gaussian coupling terms which are linear or quadratic solved. in creation/annihilation operators (e.g. particle hopping In this Letter, we rigorously address this question— or pair production); (ii) Non-Gaussian interaction terms we consider fermionic and bosonic systems with n sites, that typically act on particles only on one site. Coneach containing locally L modes (Fig. 1). The annihilation operators corresponding to the $\sigma$ mode at the i site, where $\sigma$ 1,2...L and i 1,2...n , is

$$∈ \{\}∈ \{\}^{\alpha}$$

given by ai,$\sigma$. We will use the Hermitian operators ci,$\sigma$, rahul.trivedi@mpq.mpg.de

$$1 †_{\sqrt}2$$

$$wi th \alpha 1,2,de ﬁ ne da sc_{i}_{,}_{\sigma}=(a_{i}_{,}_{\sigma}+a_{i}_{,}_{\sigma})/2,c_{i}_{,}_{\sigma}=$$

$$∈ \{_{†}\}$$

i(ai,$\sigma$ ai,$\sigma$)/$\sqrt 2$, which represent either Majorana operators(forfermions)orpositionandmomentumquadrature operators (for bosons). The noisy dynamics is described by the Lindblad master equation

$$d \rho(t)$$

$$=i[H(t),\rho(t)]+_{i}_{,}_{\sigma}\rho(t),(1)$$

dt − L

$$Xi,\sigma$$

were H(t) is a (possibly time-dependent) Hamiltonian describing the system. i,$\sigma$ captures the noise, which is assumed to act locally on every mode (i,$\sigma$), and is modeled by FIG. 1. Sketch of the model, with n sites on a lattice, where each site contains L modes. There are Gaussian couplings (l) (l)† 1 (l)† (l) between the diﬀerent sites, while the non-Gaussian interac-

$$_{i}_{,}_{\sigma}()=\kappa_{l}L_{i}_{,}_{\sigma}()L_{i}_{,}_{\sigma}L_{i}_{,}_{\sigma}L_{i}_{,}_{\sigma},(),(2)$$

(cid:18) $\cdot − 2${ $\cdot$ }(cid:19) tions are only onsite. Nonlocal couplings are allowed. In the

$$Xl=1 2$$

bosonic case, interactions of the form ni,$\sigma$ are also allowed.

$$(1)(2)†(3)$$

$$wi th ju mp op er at or sL_{i}_{,}_{\sigma}=a_{i}_{,}_{\sigma},L_{i}_{,}_{\sigma}=a_{i}_{,}_{\sigma},L_{i}_{,}_{\sigma}=$$

ai,$\sigma^{a}i$,$\sigma$ anddecayrate$s \kappa_{1}$,$\kappa 2$,$\kappa 3$ respectively. The jump while for bosons it can be assumed to be purely real and operator ai,$\sigma$ models particle loss, a†i,$\sigma$ models incoherent symmetric: particle gain, and ai,$\sigma^{a}i$,$\sigma$ models dephasing. We remark $\alpha$,$_{\alpha}^{′}_{\alpha}^{′}$,$\alpha$

$$J_{i}_{,}_{\sigma}_{j}_{,}_{\sigma}^{′}(t)=J_{j}_{,}_{\sigma}^{′}_{i}_{,}_{\sigma}(t).(5)$$

that our conclusions also hold for other physically relevant dissipators such as Li,$_{\sigma}=ci$,$\sigma$, Li,$_{\sigma}=ci$,$\sigma$ which, in The non-Gaussian onsite interactions Ui,$\sigma$;i,$\sigma ′$(t) can be the bosonic case, would correspond to white noise ﬂuctuassumed to be real and symmetric for both fermions and ations in the quadratures. We use the same noise Lindbosons. bladian for both bosons and fermions—for the bosonic We also deﬁne the parameters J,Ω,U as the smallest case, we will additionally assume that the particle loss constants such that for every mode (i,$\sigma$) and all times t occurs at a rate strictly higher than (both coherent and incoherent) particle gain (see Supplement [50] for the ex$_{J}^{\alpha}$,$\alpha$ (t) J, $_{Ω}^{\alpha}$ (t) Ω and

$$i,\sigma;j,\sigma^{′}i;\sigma$$

act assumption) so as to avoid an unbounded growth of X′X′| | $\le$ X| | $\le$

$$j ̸=i,\sigma \alpha,\alpha \alpha$$

thenumberofparticleswithtwhichwouldbeunphysical in an actual experiment. Ui,$\sigma$;i,$\sigma ′$(t) U.

$$_{′}|| \le$$

We will assume that the Hamiltonian can be written as H(t) $=H$g(t)+Hng(t), where Hg(t) contains Gaussian The parameter J captures the Gaussian coupling general intersite terms: strengthbetweenamodeand themodesatall othersites, $\alpha$,$\alpha^{′}\alpha \alpha^{′}\alpha \alpha$ U capturestheon-sitenon-Gaussianinteractionstrength,

$$H_{g}(t)=J_{i}_{,}_{\sigma}^{′}(t)c_{i}_{,}_{\sigma}c_{j}_{,}_{\sigma}^{′}+Ω_{i}_{;}_{\sigma}(t)c_{i}_{,}_{\sigma},$$

;j,$\sigma$ and Ω captures the coherent drive at each site. We will

$$Xi,j \alpha X,\alpha^{′}iX,\alpha,\sigma$$

alsoassumethatJ, U, andΩareO(1)constants, whichis

$$\sigma,\sigma$$

true in most physical models. Finally, we remark that we donotneedtoassumegeometricallocalityofthemodel— our results will apply to geometrically local and non-local and Hng(t) contains on-site non-Gaussian terms which models. account for particle-particle repulsion and attraction beThe initial state $\rho$(0) is either a product state (when tween diﬀerent modes at the same site: analyzingentanglement), aGaussianstate(whenanalyzH (t) $=$ U ′(t)n n ′. (3b) ing non-Gaussianity), or both (e.g., the vacuum state).

$$ng i,\sigma;i,\sigma i,\sigma i,\sigma$$

In the bosonic case, additionally, $\rho$(0) will be assumed

$$i,\sigma,\sigma$$

$$kk \alpha^{0}k+\beta^{0}$$

$$to sa ti sf yT r(n_{i}_{,}_{\sigma}\rho(0))C_{0}k,(i,\sigma),fo rk$$

$$_{\alpha} \le ∀ ∈$$

Note that in the fermionic case Ωi;$\sigma$(t) $=0$, since phys1,2... , andforsomeC0,$\alpha 0$,$\beta_{0}>0$: thisconditionguarical Hamiltonians must preserve fermionic parity, while antees that the probability of ﬁnding k particles in a

$$\alpha \ge$$

in the bosonic case Ω (t) can be a non-zero real scalar. mode decreases super-polynomially with k, as would be

$$i;\sigma$$

$\alpha$,$\alpha$ expected in a physically preparable bosonic state [51]. For fermions, we can assume that Ji,$\sigma j$,$\sigma ′$(t) is purely Results: Our results, depicted in Fig. 2, show the simuimaginary and anti-symmetric i.e. lability of the fermionic and bosonic models as a function ′ ′ ′ $\alpha$,$\alpha \alpha$,$\alpha ∗ \alpha$ ,$\alpha$ of J,U,$\kappa i$. We ﬁrst establish that when the noise rate is

$$J_{i}_{,}_{\sigma}_{j}_{,}_{\sigma}^{′}(t)=J_{i}_{,}_{\sigma}_{j}_{,}_{\sigma}^{′}(t)=J_{j}_{,}_{\sigma}^{′}_{i}_{,}_{\sigma}(t),(4)$$

larger than the on-site non-Gaussian interaction strength

$$(cid:0)(cid:1)$$

coupling, $\rho$(t) remains separable at all times, and can therefore be classically eﬃciently sampled from in the Fock state basis. Theorem 2. Suppose $\rho$(t) is the state obtained after evolving the bosonic model for time t with an initial product state, then for $\kappa 1$,$\kappa 2$ 2J the state $\rho$(t) is separable $\ge$ for all t 0. Furthermore, there is a randomized classi$\ge$ cal algorithm that can sample $\rho$(t) in the Fock state basis to $\epsilon$ total variation error in poly(n,t,1/$\epsilon$) time. FIG. 2. Phase diagram for both bosonic and fermionic systemsinthepresenceofgenericnoise. (a)Forfermionicsystem Our result formalizes the intuition that, when noise exthe state remains convex-Gaussian at all times for error rates ceeds the inter-site coupling strength, a buildup of en$\kappa^{3} \ge 2$U. (b) In bosonic systems the state remains separable tanglement is prohibited and no classically non-trivial at all times for error rates $\kappa 1$,$\kappa^{2} \ge 2$J. state is generated. Notably, the noise threshold is determined by particle loss and gain noise. This arises from the dephasing dissipator being diagonal in the Fock U, the fermionic model remains convex-Gaussian at all basis, while evolution under Hg(t) creates entanglement times, and can therefore be classically eﬃciently sampled through oﬀ-diagonal elements (i.e., coherences). Thus, to from. ﬁrst order, dephasing cannot counter this entanglement Theorem 1. For an initial Gaussian state, if $\kappa$ 2U, generation. Particle gain or loss dissipators, however, then the state of the fermionic model at time t, $_{\rho}^{ \ge }$(t), is are not diagonal in the Fock basis and can prevent it. In a convex combination of Gaussian states for all t 0. the Supplement, we also extend Theorem 2 to quantum Furthermore, $\rho$(t) can be classically sampled in the $^{ \ge }_{F}$ock spin models with single spin noise and bosonic models state basis to an $\epsilon$ total variation error in poly(n,t,1/$\epsilon$) with inter-site non-Gaussian couplings [50]. Unlike pretime. viouspercolation-basedargumentslimitingentanglement to O(logn) qubit clusters for suﬃciently strong noise Physically Theorem 1 suggests that when $\kappa 3$ 2U, [8, 9], we show that the state is entirely separable, and $\ge$ dephasing noise destroys non-Gaussianity faster than provide an explicit construction that can be eﬃciently Hng(t) creates it, so that $\rho$(t) always remains convexsampled from. Gaussian. Since Hg(t) preserves convex-Gaussianity, A detailed proof of Theorem 2 is provided in the Supthe noise threshold in Theorem 1 is independent of J. plement [50]. Similar to Theorem 1, we begin by a ﬁrstNotably, it is dephasing that results in this convexorder Trotterization of the model but with a diﬀerent Gaussianity. With only incoherent particle loss/gain, decomposition of the Lindbladian: We express it as a $\rho$(t) could evolve into a non-Gaussian state at short product of (a) single site gates, which contain the unitary times even with large dissipation. This arises from the generated by Hng(t), single-site terms in Hg(t) and the fermionic parity structure—the density matrix of the dephasingdissipatorand(b)two-sitechannelswhichconfermionic model has the form $\rho$(t) $=\rho$+(t) + $\rho −$(t), tain the unitary generated by the inter-site terms in Hg(t) wher$e \rho_{\pm}$(t) is supported only on even/odd parity states. paired together with the particle gain and loss dissipators Due to this structure, convex-Gaussianity i$n \rho$(t) requires [Fig. 4]. We denote the channel acting between modes both $\rho \pm$(t) to be convex-Gaussian [40]. Hng(t) generates ′ i,$\sigma$;j,$\sigma$ (i,$\sigma$) and (j,$\sigma$ ) at the Trotter-ste$p \tau$ a$s \Phi$ , where

$$\tau \delta,(\tau − 1)\delta$$

non-Gaussianity individually in both $\rho \pm$(t). However, $\delta$ is the size of the Trotter-step. Importantly, the Trotthe loss/gain dissipators, to ﬁrst order, switch the parity terization is performed in such a way that the channel of the state and do not act within the two parity subi,$\sigma$;j,$_{\sigma}^{′}$ can be understood as a time evolution of the spaces. Consequently, they cannot immediately counter $\tau \delta$,($\tau − 1$)$\delta$ the non-convex-Gaussianity created by H (t). inter-site Gaussian couplings between modes (i,$\sigma$) and We provide a complete proof of Theorem 1 in the (j,$\sigma$ ), followed by noise on both modes. This eﬀectively supplement: The starting point is a Trotterization of redistributes the single-site noise into “gate-based” noise

$$i,\sigma;j,\sigma$$

the Lindbladian in Eq. 1 — in each Trotter step, we on the inter-site gates. Analyzing $\Phi$ , we show

$$\tau \delta,(\tau − 1)\delta$$

express the evolution as (a) a Gaussian unitary correthatfo$r \kappa_{1}$,$\kappa 2$ 2J, itisseparability-preservingandthus sponding to Hg(t), particle loss and gain followed by (b) the state rema$i^{ \ge }n$s separable at all times. Furthermore, we the single-site channels generated by Hng(t) and dephasalso explicitly construct an O($\delta 2$) approximation to the ing (Fig. 3). Analyzing the single-site channel, we show separable state after each time-step and obtain an exthat for $\kappa 3$ 2U, this channel maps an input convexplicit algorithm to sample from $\rho$(t). $\ge$ Gaussianstatetoaconvex-Gaussianstate. Furthermore, Tightness of Theorems 1 and 2. We can now ask if weexplicitlyconstructtheoutputconvex-Gaussianstate, a version of Theorem 1 holds for bosonic systems i.e., which allows us to sample from it [35, 52]. is there a noise threshold $\kappa t$h(U) dependent only on the Next, weconsiderthebosonicmodelandestablishthat non-Gaussian strength U and uniform in J,Ω that guarwhen the noise rate is larger than the inter-site Gaussian antees a convex-Gaussian at all times? For dephasing

FIG. 3. Schematic depiction of the Trotterization schemes in the proof of Theorem 1 (fermionic systems with weak nonGaussianity). For simplicity, we only depict a 1D setting, with each site containing 3 modes ($L=3$). A single Trotter step consists of a Gaussian channel (orange rectangles) that includes the combined eﬀect of Hg(t) and the particle gain and loss dissipators, followedbynon-Gaussiangates(bluerectangles)interspersedwiththedephasingdissipator(graycurvedrectangles). Crucially, a non-Gaussian gate followed by suﬃciently strong dephasing can be written as a convex combination of Gaussian channels. FIG. 4. Schematic depiction of the Trotterization schemes in the proof of Theorem 2 (bosonic systems with weak inter-site couplings). For simplicity, we only depict a 1D setting, with each site containing 3 modes ($L=3$). A single Trotter step consists of a layer of single-site channels which include the Hamiltonian terms acting on that site and the dephasing dissipator, followed by 2-site gates interspersed with particle gain and loss dissipators (in gray circles). Crucially, a 2-site gate followed by suﬃciently strong noise can be written as a convex combination of single-site channels noise, we provide numerical evidence to the contrary: mode with an arbitrarily small eﬀective gate-error rate even for $\kappa 3$ U, single-mode dynamics can yield states by engineering the displacement and squeezing. We exwith negative Wigner function, and thus not convextend this technique to also implement an entangling gate Gaussian states can be generated at time-scales 1/U between two oscillators thus yielding a high-ﬁdelity uni[50,53]. WhilenegativityoftheWignerfunctionsuggests versal multi-mode gate-set. Together with results from classical simulation hardness [53, 54], we do not rule out Ref. [57], this suggests that when the noise is non-unital the existence of an eﬃcient classical algorithm. When (i.e. $\kappa_{1}=\kappa_{2}$), by using suﬃciently large J and Ω, a $\kappa_{3}=0$, in the Supplement we show that no matter how fault-tolerant quantum computation can be encoded into small U is relative to $\kappa 1$,$\kappa 2$, computing expected local the model [58–60]. Thus, it is unlikely to be able to particle numbers is BQP-hard if J,Ω can be arbitrarclassically compute even local observables in this setting ily large but O(1) [50]. This builds upon Refs. [55, 56] unless BQP $=$ BPP. which perform a universal gate-set on a single bosonic Finally, we consider if a version of Theorem 2 holds

for fermions i.e., do noise rates larger than the Gaussian lenge in experimentally verifying the threshold behavior inter-site couplings result in separability at all times. We predicted by Theorems 1 and 2 would be verifying the answer this question in the negative: in the Supplement presence (or absence) of entanglement/non-Gaussianity we show by analyzing few-mode fermionic models that, i$n \rho$(t). While this could be hard to do for large systems, in contrast with bosons, no matter how high $\kappa 2$,$\kappa 3$ are, we remark that the diﬀerence in the threshold behavior thesystemdoesnotremainseparableatalltimesandcan in fermionic and bosonic models that we described can be

$$− 1 − 1$$

exhibit entanglement at time-scales min($^{\kappa}_{2}$ ,$^{\kappa}_{3}$ ). In understood even with systems with few ( 4) fermionic

$$\sim \le$$

fact, this short-time non-separability holds not only if or bosonic modes, which is well within the regime where we consider separability with respect to all observables a full state tomography can already be performed. [61], but also if we consider a weaker notion of separability with respect to only parity-conserving observables [62]. However, this result does not rule out separability ACKNOWLEDGMENTS at longer times or other routes to classical simulation. Conclusion and outlook. We have characterized the We thank Ashish Clerk and Liang Jiang for useful classical complexity of simulating the continuous-time discussions and Peter McMahon for discussions that inevolution of fermionic and bosonic systems as a funcspired this project. R.T acknowledges support from Cention of the noise, Gaussian and non-Gaussian interaction ter for Integration of Modern Optoelectronic Materials strengths. Future theoretical directions include the study on Demand (IMOD) seed grant (DMR-2019444). This extending our results to non-Markovian models of dissiresearch was supported in part by grant NSF PHYpation. 2309135 to the Kavli Institute for Theoretical Physics The models considered in this paper can be experimen(KITP). The research is part of the Munich Quantum tally realised in several platforms. The bosonic model Valley, which is supported by the Bavarian State Govcan be implemented in superconducting systems where ernment with funds from the High tech Agenda Baythe Gaussian Hamiltonian can be controlled by designern Plus. J.I.C, R.T, G.G.G acknowledge funding from ing capacitive couplings between diﬀerent qubits and the the project FermiQP of the Bildungsministerium fu¨r single-site non-Gaussianity by the nonlinear Josephson Bildung und Forschung (BMBF). A.V.G. acknowledges potential in the qubit [28, 29]. We can also use cold support from the U.S. Department of Energy, Oﬃce bosonic atoms in optical lattices where the strength of of Science, Accelerated Research in Quantum Computboth the Gaussian and the non-Gaussian Hamiltonians ing, Fundamental Algorithmic Research toward Quancan be controlled by tuning the optical lattice potential tum Utility (FAR-Qu). A.V.G. was also supported in [26, 27]. The fermionic model can be implemented either part by NSF QLCI (award No. OMA-2120757), DoE with cold atoms in optical lattices by using a fermionic ASCR Quantum Testbed Pathﬁnder program (awards species of atoms [23–25], or in solid-state systems such No.DE-SC0019040andNo.DE-SC0024220), NSFSTAQ Moir´e superlattices hosting trions [63–65]. Since all of program, AFOSR MURI, DARPA SAVaNT ADVENT, these systems will have intrinsic particle loss, gain, and and NQVL:QSTD:Pilot:FTL. A.V.G. also acknowledges dephasing, tuning the parameters in the Gaussian and support from the U.S. Department of Energy, Oﬃce non-Gaussian Hamiltonians could allow us to access the of Science, National Quantum Information Science Reparameter regimes in Theorems 1 and 2. A major chalsearch Centers, Quantum Systems Accelerator.

- [1] J. Preskill, Quantum 2, 79 (2018).
- [7] O. Shtanko, A. Deshpande, P. S. Julienne, and A. V.
- [2] A.J.Daley,I.Bloch,C.Kokail,S.Flannigan,N.Pearson, Gorshkov, PRX Quantum 2, 030350 (2021). M. Troyer, and P. Zoller, Nature 607, 667 (2022).
- [8] R. Trivedi and J. I. Cirac, Phys. Rev. Lett. 129, 260405
- [3] S. Ebadi, T. T. Wang, H. Levine, A. Keesling, G. Semeghini, A. Omran, D. Bluvstein, R. Samajdar, H. Pich
- [9] D. Aharonov, Phys. Rev. A 62, 062311 (2000). ler, W. W. Ho, et al., Nature 595, 227 (2021).
- [10] D. Aharonov, X. Gao, Z. Landau, Y. Liu, and U. Vazi
- [4] P. Scholl, M. Schuler, H. J. Williams, A. A. Eberharter, rani, in Proceedings of the 55th Annual ACM Symposium D. Barredo, K.-N. Schymik, V. Lienhard, L.-P. Henry, on Theory of Computing, STOC ’23 (ACM, 2023). T. C. Lang, T. Lahaye, et al., Nature 595, 233 (2021).
- [11] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels,
- [5] D. Wei, A. Rubio-Abadal, B. Ye, F. Machado, J. Kemp, arXiv preprint arXiv:2306.14887 (2023). K. Srakaew, S. Hollerith, J. Rui, S. Gopalakrishnan,
- [12] K.Kechedzhi,S.Isakov,S.Mandra`,B.Villalonga,X.Mi, N. Y. Yao, I. Bloch, and J. Zeiher, Science 376, 716 S. Boixo, and V. Smelyanskiy, Future Gener. Comput. Syst. 153, 431 (2024).
- [6] G. Semeghini, H. Levine, A. Keesling, S. Ebadi, T. T.
- [13] Y. Shao, F. Wei, S. Cheng, and Z. Liu, Phys. Rev. Lett. Wang, D. Bluvstein, R. Verresen, H. Pichler, M. Kalinowski, R. Samajdar, A. Omran, S. Sachdev, A. Vish
- [14] E. Fontana, M. S. Rudolph, R. Duncan, I. Rungger, and wanath, M. Greiner, V. Vuleti´c, and M. D. Lukin, SciC. Cˆırstoiu, arXiv preprint arXiv:2306.05400 (2023). ence 374, 1242 (2021).
- [15] M. S. Rudolph, E. Fontana, Z. Holmes, and L. Cincio, arXiv preprint arXiv:2308.09109 (2023). J. of Phys. 21, 055003 (2019).
- [16] X. Gao and L. Duan, arXiv preprint arXiv:1810.03176
- [45] C. Oh, L. Jiang, and B. Feﬀerman, arXiv preprint arXiv:2301.11532 (2023).
- [17] H.-J.Liao,K.Wang,Z.-S.Zhou,P.Zhang, andT.Xiang,
- [46] H. Qi, D. J. Brod, N. Quesada, and R. Garc´ıa-Patro´n, arXiv preprint arXiv:2308.03082 (2023). Phys. Rev. Lett. 124, 100502 (2020).
- [18] G. Gonza´lez-Garc´ıa, R. Trivedi, and J. I. Cirac, PRX
- [47] V. Shchesnovich, Quantum 5, 423 (2021). Quantum 3, 040326 (2022).
- [48] H.-S. Zhong, H. Wang, Y.-H. Deng, M.-C. Chen, L.-C.
- [19] T. Schuster, C. Yin, X. Gao, and N. Y. Yao, arXiv Peng, Y.-H. Luo, J. Qin, D. Wu, X. Ding, Y. Hu, P. Hu, preprint arXiv:2407.12768 (2024). X.-Y. Yang, W.-J. Zhang, H. Li, Y. Li, X. Jiang, L. Gan,
- [20] G. Gonza´lez-Garc´ıa, J. I. Cirac, and R. Trivedi, arXiv G. Yang, L. You, Z. Wang, L. Li, N.-L. Liu, C.-Y. Lu, preprint arXiv:2407.16068 (2024). and J.-W. Pan, Science 370, 1460 (2020).
- [21] J. Rajakumar, J. D. Watson, and Y.-K. Liu, in Proceed
- [49] L.S.Madsen,F.Laudenbach,M.F.Askarani,F.Rortais, ings of the 2025 Annual ACM-SIAM Symposium on DisT. Vincent, J. F. Bulmer, F. M. Miatto, L. Neuhaus, crete Algorithms (SODA) (SIAM, 2025) pp. 1037–1056. L. G. Helt, M. J. Collins, et al., Nature 606, 75 (2022).
- [22] S. D. Mishra, M. Fr´ıas-P´erez, and R. Trivedi, PRX
- [50] See supplemental material for a detailed proof of the theQuantum 5, 020317 (2024). orems, which includes Refs. [66-76].
- [23] Z.Z.Yan, B.M.Spar, M.L.Prichard, S.Chi, H.-T.Wei,
- [51] T. Kuwahara, T. V. Vu, and K. Saito, Nat. Commun. E. Ibarra-Garc´ıa-Padilla, K. R. A. Hazzard, and W. S. Bakr, Phys. Rev. Lett. 129, 123201 (2022).
- [52] E. Knill, arXiv preprint quant-ph/0108033 (2001).
- [24] B. M. Spar, E. Guardado-Sanchez, S. Chi, Z. Z. Yan,
- [53] A. Mari and J. Eisert, Phys. Rev. Lett. 109, 230503 and W. S. Bakr, Phys. Rev. Lett. 128, 223202 (2022).
- [25] M. A. Norcia, A. W. Young, and A. M. Kaufman, Phys.
- [54] C. Cormick, E. F. Galva˜o, D. Gottesman, J. P. Paz, and Rev. X 8, 041054 (2018). A. O. Pittenger, Phys. Rev. A 73, 012301 (2006).
- [26] C. Gross and I. Bloch, Science 357, 995 (2017).
- [55] M. Yuan, A. Seif, A. Lingenfelter, D. I. Schuster, A. A.
- [27] B. Yang, H. Sun, R. Ott, H.-Y. Wang, T. V. Zache, J. C. Clerk, and L. Jiang, arXiv preprint arXiv:2312.15783 Halimeh, Z.-S. Yuan, P. Hauke, and J.-W. Pan, Nature
- [56] A.Eickbusch,V.Sivak,A.Z.Ding,S.S.Elder,S.R.Jha,
- [28] X. Zhang, E. Kim, D. K. Mark, S. Choi, and O. Painter, J.Venkatraman,B.Royer,S.M.Girvin,R.J.Schoelkopf, Science 379, 278 (2023). and M. H. Devoret, Nat. Phys. 18, 1464 (2022).
- [29] Y.-H. Shi, Z.-H. Sun, Y.-Y. Wang, Z.-A. Wang, Y.-R.
- [57] M. Ben-Or, D. Gottesman, and A. Hassidim, arXiv Zhang, W.-G. Ma, H.-T. Liu, K. Zhao, J.-C. Song, G.-H. preprint arXiv:1301.1995 (2013). Liang, et al., Nat. Commun. 15, 7573 (2024).
- [58] K. Noh and C. Chamberland, Phys. Rev. A 101, 012316
- [30] A. Saxena, A. Manna, R. Trivedi, and A. Majumdar, Nat. Commun. 14, 5260 (2023).
- [59] T. Matsuura, N. C. Menicucci, and H. Yamasaki, arXiv
- [31] D. E. Chang, V. Vuleti´c, and M. D. Lukin, Nat. Phopreprint arXiv:2410.12365 (2024). tonics 8, 685 (2014).
- [60] D.AharonovandM.Ben-Or,SIAMJ.Comput.38,1207
- [32] C.NohandD.G.Angelakis,Rep.Prog.Phys.80,016401
- [61] H. Moriya, J. Phys. A-Math. Gen. 39, 3753 (2006).
- [33] S. Bravyi and R. Ko¨nig, Quantum Info. Comput. 12,
- [62] M.-C. Ban˜uls, J. I. Cirac, and M. M. Wolf, Phys. Rev. 925–943 (2012). A 76, 022311 (2007).
- [34] S. D. Bartlett, B. C. Sanders, S. L. Braunstein, and
- [63] E. Liu, E. Barr´e, J. van Baren, M. Wilson, T. Taniguchi, K. Nemoto, Phys. Rev. Lett. 88, 097904 (2002). K. Watanabe, Y.-T. Cui, N. M. Gabor, T. F. Heinz, Y.
- [35] B. M. Terhal and D. P. DiVincenzo, Phys. Rev. A 65, C. Chang, et al., Nature 594, 46 (2021).
- [64] X. Wang, J. Zhu, K. L. Seyler, P. Rivera, H. Zheng,
- [36] L. G. Valiant, in Proceedings of the thirty-third annual Y. Wang, M. He, T. Taniguchi, K. Watanabe, J. Yan, ACM symposium on Theory of computing (2001) pp. et al., Nature Nanotechnology 16, 1208 (2021). 114–123.
- [65] H. Baek, M. Brotons-Gisbert, A. Campbell, V. Vitale,
- [37] S. B. Bravyi and A. Y. Kitaev, Ann. Phys. 298, 210 J. Lischner, K. Watanabe, T. Taniguchi, and B. D. Gerardot, Nature Nanotechnology 16, 1237 (2021).
- [38] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82, 1784
- [66] C. V. Kraus, A quantum information perspective of fermionic quantum many-body systems, Ph.D. thesis,
- [39] F. de Melo, P. C´wiklin´ski, and B. M. Terhal, New. J. Technische Universita¨t Mu¨nchen (2009). Phys. 15, 013015 (2013).
- [67] J. Surace and L. Tagliacozzo, SciPost Phys. Lect. Notes
- [40] M. Oszmaniec, J. Gutt, and M. Ku´s, Phys. Rev. A 90,
- [68] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and
- [41] S. Bravyi, Phys. Rev. A 73, 042313 (2006). C. Stein, Introduction to algorithms (MIT press, 2022).
- [42] N. Maskara, A. Deshpande, A. Ehrenberg, M. C. Tran,
- [69] M. Fagotti and P. Calabrese, J. Stat. Mech.-Theory E. B.Feﬀerman, andA.V.Gorshkov,Phys.Rev.Lett.129,
- [70] R. Hudson, Rep. Math. Phys 6, 249 (1974).
- [43] A. Deshpande, B. Feﬀerman, M. C. Tran, M. Foss
- [71] M. Walschaers, PRX Quantum 2, 030204 (2021). Feig, and A. V. Gorshkov, Phys. Rev. Lett. 121, 030501
- [72] A. Lingenfelter, D. Roberts, and A. A. Clerk, Sci. Adv. 7, eabj1916 (2021).
- [44] G. Muraleedharan, A. Miyake, and I. H. Deutsch, New.
- [73] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and R. Vrijen, Proceedings of the National Academy of Sci- ences 99, 3388 (2002).
- [75] A´. M. Alhambra, M. Lostaglio, and C. Perry, Quantum
- [74] L. J. Schulman and U. V. Vazirani, in Proceedings of the Thirty-First Annual ACM Symposium on Theory of
- [76] O. Shtanko and K. Sharma, arXiv preprint Computing, STOC ’99 (Association for Computing MaarXiv:2411.04819 (2024). chinery, New York, NY, USA, 1999) p. 322–329. [77] https://github.com/guillegg10/Separabilit$y_$ Wigner-negativity, GitHub repository.

Supplemental material to “Dynamical complexity of non-Gaussian many-body systems with dissipation” Guillermo Gonz´alez-Garc´ıa , Alexey V. Gorshkov , J. Ignacio Cirac , and Rahul Trivedi ∗ Max-Planck-Institut fu¨r Quantenoptik, Hans-Kopfermann-Str. 1, 85748 Garching, Germany Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, D-80799 Munich, Germany Joint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA. Joint Center for Quantum Information and Computer Science, NIST/University of Maryland, College Park, Maryland 20742, USA. (Dated: October 21, 2025) This Supplemental Material is organized as follows: First, in section I, we provide the necessary notation and background for the rest of the Supplemental Material. In section II, we provide the proof of Theorem 1, showing convex-Gaussianity and simulability for the fermionic model for suﬃciently high noise rates. Then, in section III, we prove Theorem 2 for the bosonic model, which implies separability and simulability for suﬃciently high noise rates. In section IV, we extend this result to a class of spin models: for 2-local Hamiltonians and suﬃciently high noise rates, the system can be shown to be separable at all times. Finally, in section V, we show that an analogue of Theorem 1 cannot exist for bosonic systems, and that an analogue of Theorem 2 cannot exist for fermionic systems. I. NOTATIONANDPRELIMINARIES In this section, we provide the necessary notation and background for the rest of the Supplemental Material. This

includes the notation regarding operators and norms (subsection IA), a brief

summary on several properties of bosonic and fermionic systems (subsection IB), the Trotter formula that will be used throughout the proofs (subsection IC), the asymptotic notation that we will employ (subsection ID), and a detailed presentation of the bosonic and fermionic models that we will analyze (subsection IE). A. Operators, superoperators and their norms For a quantum state $\psi$ , $\psi$ will denote its usual norm $\psi=\psi \psi$ . For an operator A, we will use A to

$$|\rangle ∥|\rangle ∥ ∥|\rangle ∥ \langle|\rangle ∥ ∥$$

denote its Schatten-p norm: A $=\sigma$ (A) , where $\sigma 1$(A) $\sigma 2$(A) $\sigma 3$(A)... are the singular values of A.

$$∥ ∥ \ge \ge$$

$$(cid:18)^{i}(cid:19)$$

We will often use $A=\sigma_{1}$(A) $=A$ to denote its operator norm and A $=A$ $=$ [Tr(A†A)] to denote its

$$∥ ∥ ∥ ∥^{\infty}∥ ∥ ∥ ∥$$

Frobenius norm. We will often use the Holder’s inequality, which states that

$$AB wh er e+=1 .$$

$$∥ ∥ \le ∥ ∥ ∥ ∥ pq$$

In particular, AB A B . It is also convenient to note the Cauchy-Schwarz inequality for operators: Suppose

$$∥ ∥ \le ∥ ∥ ∥ ∥$$

$\omega$ is a positive semi-deﬁnite operator, then

$$Tr(A^{†}B \omega)Tr(A^{†}A \omega)Tr(B^{†}B \omega).(S 3)$$

$\le$ For super-operators , we will use (cid:12) to deno(cid:12)te its diamond norm. In our analysis, we will often encounter

$$∥ A^{(cid:12)}∥^{⋄}^{(cid:12)}$$

super-operators of the form

$$(\rho)=A_{i}\rho B_{i},(S 4)$$

rahul.trivedi@mpq.mpg.de

where Ai and Bi are some operators. For such super-operators, it is convenient to note that the Holder’s inequality implies that

$$A_{i}B_{i}.(S 5)$$

$$∥ A ∥^{⋄} \le ∥ ∥ ∥ ∥$$

For instance, given an operator L, we will often use L to denote the following superoperator:

$$_{L}=L \rho L^{†}L^{†}L,\rho,(S 6)$$

$$D − 2 \{\}$$

where , is the anti-commutator between two operators. L will be called the “dissipator corresponding to L”.

$$\{\cdot \cdot \}D$$

From Eq. (S5), we then obtain that

$$_{L}L+L^{†}L 2 L .(S 7)$$

$$∥ D ∥^{⋄} \le ∥ ∥ \le ∥ ∥$$

A super-operator is completely positive if and only if it c(cid:13)an b(cid:13)e expressed as

$$(cid:13)(cid:13)$$

$$(\rho)=K_{i}\rho K^{†}(S 8)$$

for some operators Ki. It will be called a channel if it is additionally trace preserving which requires K†$K_{i}=I$. For any completely-positive trace preserving map ,

$$E ∥ E ∥^{⋄} \le P$$

B. Fermions and Bosons The Hilbert space of m fermionic modes is described by the vacuum state vac and the standard creation (a†) and annihilation (ai) operators, with i 1,2, m labeling the fermionic mode. These satisfy the canonical

$$∈ \{\cdot \cdot \cdot \}$$

anticommutation relations:

$$a_{i},a_{j}=0 an da_{i},a^{†}=\delta_{i}_{,}_{j}.$$

$$\{\}\{\}$$

$$m µ_{k}$$

The Hilbert space of the fermionic model is the ﬁnite-dimensional vector space given by span (a†) vac : µk

$$k=1 k$$

$$\{|\rangle ∈$$

0,1 . It will be convenient to work with the 2m Majorana fermion operators deﬁned by

$$\{\}\}Q$$

$$c_{i}=a^{†}+a_{i}an dc_{i}=a^{†}a_{i}.$$

$$\sqrt 2 \sqrt 2 −$$

(cid:0) (cid:1) (cid:0) ′ (cid:1) The Majorana operators are each Hermitian, traceless and satisfy ci ,$c_{i}^{′}=\delta i$,$i^{′}\delta \sigma$,$\sigma ′$. We deﬁne 2m as the algebra

$$\{\}C$$

generatedbythe2mMajoranaoperators: AnoperatorX 2m canbeexpressedasalinearcombinationofmonomials

$$m 2 \alpha µ^{\alpha}\alpha ∈ C$$

of the form (ci ) i , where µi 0,1 . The operator X will be even if it is a linear combination of only

$$i=1 \alpha=1$$

$$∈ \{\}$$

even degree monomials, and odd if it is a linear combination of odd degree monomials. Furthermore, any Hermitian operator deﬁQned oQn the fermionic Hilbert space is also in 2m and, as usual, fermionic quantum states are positive semi-deﬁnite Hermitian operators in 2m.

$$C ′ ′$$

$$\alpha,\alpha \alpha \alpha$$

Given a fermionic state $\rho$, its correlation matrix elements are deﬁned by $\Gamma_{′}=i$tr($\rho$[ci ,ci′ ])/2. A fermionic

$$i,i$$

state $\rho$ is called Gaussian if it can be expressed as exp( $\beta H$)/Tr(exp( $\beta H$)) for some Hermitian operator H that

$$_{R}− −$$

is quadratic in the Majorana operators and $\beta$ , . Thus, fermionic Gaussian states are either Gibb’s

$$∈ ∪ \{− \infty \infty \}$$

states of Hamiltonians that are quadratic in the Majorana operators, or are projectors on their ground-state subspace.

$$\alpha,\alpha$$

Fermionic Gaussian states are fully characterized by their correlation matrix elements $\Gamma^{′}$ [S1, S2]. We will refer to i,i a fermionic state as convex-Gaussian if it can be expressed as a convex combination of Gaussian states. Similar to fermions, the Hilbert space of m bosonic modes will be described by a vacuum state vac and the creation (a†) and annihilation (ai) operators, with i 1,2...m labeling the bosonic mode. These satisfy the

$$∈ \{\}$$

canonical commutation relations:

$$[a_{i},a_{i}^{′}]=0 an d[a_{i},a^{†}_{′}]=\delta_{i}_{,}_{i}^{′}.$$

The Hilbert space of the bosonic model is the inﬁnite-dimensional vector space given by span (a†) vac : µi

$$\{|\rangle ∈$$

0,1,2... . It will be convenient to work with the 2m quadrature operators

$$\{\}\}Q$$

$$c_{i}=a^{†}+a_{i}an dc_{i}=a^{†}a_{i}.$$

$$\sqrt 2 \sqrt 2 −$$

(cid:0) (cid:1) (cid:0) (cid:1)

The quadrature operators are Hermitian and satisfy [ci ,ci ] $=i \delta_{i}$,$i^{′}Ω \alpha$,$\alpha ′$, where Ω is the 2 2 symplectic matrix. Similar to a fermionic state, a bosonic stat$e \rho i$s Gaussian if it can be expressed as exp( $\beta H$)/Tr(exp( $\beta H$)) for some − R− Hermitian operator H which is quadratic or linear in the quadrature operators and for some $\beta$ , . A

$$∈ ∪ \{− \infty \infty \}$$

state will be called convex-Gaussian if it can be expressed as a convex combination of Gaussians. A useful property of Gaussian states that we will use in our analysis is given in the lemma below.

$$\alpha,\alpha \alpha \alpha$$

Lemma 1. Suppose $\rho$ is a (fermionic or bosonic) Gaussian state and $A=_{′}A$ ′ ci ci′ is a quadratic operator,

$$i,ii,i$$

A A A A then $\rho_{′}=e_{−}\rho e_{−}$ /Tr($e_{−}\rho e_{−}$ ) is also a Gaussian state. Proof. This follows from the closure of quadratic and linear operators under commutation, i.e. ′ ′ ′

$$\alpha,\alpha \alpha \alpha \alpha,\alpha_{C}$$

(1) For fermions, the commutator of any two operators of the form ′ ′ x ′ ci ci′ , where x ′ , is again i,i $\alpha$,$\alpha$ i,i i,i of the same form.

$$\alpha,\alpha \alpha \alpha \alpha \alpha$$

(2) For bosons, the commutator of any two operators of the form ′ ′ x ′ ci ci′ + yi ci , where

$$i,i \alpha,\alpha i,ii,\alpha$$

$$\alpha,\alpha \alpha_{C}$$

x ′ ,yi , is again of the same form.

$$i,iP PP$$

Since $\rho$ is a Gaussian state, it is expressible as exp( $\beta H$)/Tr(exp( $\beta H$)), where H is a quadratic form in ci with

$$^{\alpha}− −$$

a possible linear term in ci for bosons. Consequently, using the Baker-Campbell-Hausdorﬀ formula, we obtain that $e_{−}\rho e_{−}$ can be written as a linear combination of A,A†,H and their nested commutators. Consequently, from 1

$$AA \alpha$$

and 2 above, we obtain that $e_{−}\rho e_{−}$ exp( $\beta H_{′}$) for some $\beta$ and H′ that is also a quadratic form in ci with a

$$\propto −^{†}$$

possible linear term for bosons. Furthermore, note that since $\rho$ is positive-semideﬁnite, so is $e_{−}\rho e_{−}$ and thus is a valid quantum state. C. Trotter formula Inouranalysisbelow, wewilloftenuseﬁrst-orderTrotterizationfortime-dependentmodels. Givenatime-dependent Lindbladian (t) $=$ (t)+ (t)+... (t), its ﬁrst-order Trotterization in the time-interval [0,t], with T Trotter L L L L steps each of length $\delta=t$/T, will be given by

$$\Phi=\Phi \Phi . . . \Phi wh er e \Phi=ex p(s)ds .$$

$$\tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta$$

$$− − − −^{T}(\tau 1)\delta^{L}$$

$$\tau=T(cid:18)Z_{−}(cid:19)$$

In Lemma 2 below, we provide an upper bound on the error between the exact evolution exp( (s)ds) and the Trotter formula $\Phi$ that we will use repeatedly in the following sections. Lemma 2 (Trotter error for bounded Lindbladians). Suppose for any s 0 and j 1,2...M , (j)(s) ℓj,

$$\ge ∈ \{\}∥ L ∥^{⋄} \le$$

then for any $T>0$,

$$ex p(s)ds \Phi ℓ_{j}.$$

$$T_{0}L − \le T$$

(cid:13) (cid:18)Z (cid:19) (cid:13)⋄ (cid:18)$j=1$ (cid:19)

$$(cid:13)(cid:13)$$

$$(cid:13)(cid:13)$$

$$(cid:13)(cid:13)$$

D. Asymptotic notation Throughout the paper, we employ the following asymptotic notation commonly used in complexity theory [S3]: TABLE SI. Table of asymptotic notation used in this paper.

| Notation     | Formal definition                         | Informal description                |
| ------------ | ----------------------------------------- | ----------------------------------- |
| f(n)=Ω(g(n)) | ∃k>0,n0 :∀n>n0,|f(n)|≥kg(n)               | f(n) grows at least as fast as g(n) |
| f(n)=O(g(n)) | ∃k>0,n0 :∀n>n0,|f(n)|≤kg(n)               | f(n) grows no faster than g(n)      |
| f(n)=Θ(g(n)) | ∃k1 >0,k2 >0,n0 :∀n>n0,k1g(n)≤f(n)≤k2g(n) | f(n) and g(n) grow equally fast     |

E. Model Here, we brieﬂy recap the fermionic and bosonic models introduced in the main text and streamline the notation. We will consider a more general setting than the one described in the main text: speciﬁcally, we will allow here for inter-site non-Gaussian interactions. We recall that we consider systems with n sites, with each site containing L bosonic or fermionic modes. We will use $m=nL$ to denote the total number of modes in the system. With the $\sigma$ mode at the i site, where $\sigma$ 1,2...L and i 1,2...n , we will associate an annihilation operator ai,$\sigma$—it will

$$∈ \{\}∈ \{\}$$

be notationally convenient for us to group i,$\sigma$ into a single index $v=$ (i,$\sigma$) and denote the corresponding annihilation operator by av. Furthermore, corresponding to a mode index v, we will use iv to denote the site the mode is at and $\sigma v$ to be the local index of the mode. Associated with the mode at v, we will also deﬁne the operators nv,cv,cv via

$$1^{a}v^{+}^{a}† v 2^{a}v^{a}† v$$

$$n_{v}=a^{†}_{v}a_{v},c_{v}=an dc_{v}=− .$$

$$\sqrt 2 \sqrt 2 i$$

Here, nv is an operator measuring the number of particles in mode v, and cv,cv are the Majorana operators (for fermions) or the quadrature operators (for bosons). As in the main text, the Hamiltonian for the fermionic or bosonic problem will be decomposed as

$$H(t)=H_{g}(t)+H_{n}_{g}(t),$$

where Hg(t) is Gaussian given by

$$\alpha,\alpha \alpha \alpha \alpha \alpha$$

$$H_{g}(t)=J_{′}(t)c_{v}c_{v}^{′}+Ω_{v}(t)c_{v},$$

$$v,v$$

$$v,v^{′}\alpha,\alpha^{′}v,\alpha$$

$$XX X$$

with Ωv(t) $=0$ for fermions, and Hng(t) is non-Gaussian given by

$$H_{n}_{g}(t)=U_{v}_{,}_{v}^{′}(t)n_{v}n_{v}^{′}.$$

$$v,v^{′}$$

Without loss of generality, we can assume that

$$′ ′ ′$$

$$\alpha,\alpha \alpha,\alpha \alpha,\alpha$$

For fermions, J ′ (t) is purely imaginary and J ′ (t) $=$ J ′ (t),

$$v,vv,vv,v$$

$$′ ′ ′$$

$$\alpha,\alpha \alpha,\alpha \alpha,\alpha$$

For bosons, J ′ (t) is purely real and J ′ (t) $=J_{′}$ (t),

$$v,vv,vv,v$$

For both fermions and bosons, Uv,v′(t) is purely real and Uv,v′(t) $=U_{v}^{′}$,v(t). As in the main text, we will also deﬁne constants JC,Jos,UC,Uos,Ω: (1) JC is a measure of the strength of the Gaussian terms coupling modes at diﬀerent sites: It is the smallest number

$$su ch th at ta nd v=(i,\sigma)$$

$$\alpha,\alpha$$

$$J_{′}_{′}(t)J_{C}.(S 1 9)$$

$$i,\sigma;i,\sigma$$

$$|| \le$$

$$i^{′}:i^{′}=i,\sigma^{′}\alpha,\alpha^{′}$$

$$X^{̸}X$$

(2) Jos is a measure of the strength of the Gaussian terms coupling modes at the same site: It is the smallest number

$$su ch th at ta nd v=(i,\sigma)$$

$$\alpha,\alpha$$

$$J_{′}(t)J_{o}_{s}.$$

$$i,\sigma;i,\sigma$$

$$|| \le$$

$$\sigma^{′}\alpha,\alpha^{′}$$

(3) UC is a measure of the strength of the non-Gaussian terms coupling modes at diﬀerent sites: It is the smallest number such that t and $v=$ (i,$\sigma$)

$$U_{i}_{,}_{\sigma}_{;}_{i}^{′}_{,}_{\sigma}^{′}(t)U_{C}.(S 2 1)$$

$$|| \le$$

$$i^{′}=i,\sigma^{′}$$

(4) Uos is a measure of the strength of the non-Gaussian terms coupling modes at the same site: It is the smallest number such that t and $v=$ (i,$\sigma$)

$$^{U}i,\sigma;i,\sigma^{′}^{(}^{t}^{)}^{U}os^{.}$$

$$|| \le$$

$$i \sigma^{′}$$

(5) Ω is a measure of the on-site displacement: it is the smallest number such that t and $v=$ (i,$\sigma$)

$$Ω_{i}_{,}_{\sigma}(t)Ω .(S 2 3)$$

$$|| \le$$

Note that $Ω=0$ only for the bosonic model—we do not include a displacement term in the fermionic model. Note that the inter-site non-Gaussian interactions were not included in the main text, and the results quoted in the main text can be obtained by setting $U_{C}=0$. Finally, it will also be convenient to deﬁne the parameter $\Lambda$ as

$$\Lambda=J_{C}+U_{C}+J_{o}_{s}+U_{o}_{s}+\kappa+Ω .$$

While analyzing the bosonic model, it will be more convenient to express Hg as a sum of particle number conserving and non-conserving terms via

$$H_{g}(t)=_{v}_{,}_{v}^{′}(t)a^{†}_{v}a_{v}^{′}+h . c .+_{v}_{,}_{v}^{′}(t)a_{v}a_{v}^{′}+h . c .+_{v}(t)a_{v}+h . c .,$$

$$JG D$$

$$v,v^{′}v,v^{′}v$$

X(cid:0) (cid:1) X(cid:0) (cid:1) X(cid:0) (cid:1) hop sq disp

$$H(t)H_{g}(t)H^{g}(t)$$

$$|\{z \}|\{z 1,\}1^{|}1,2^{\{}^{z}2,1^{\}}2,2$$

where, up to a possibly time-dependent energy shift in Hg(t), v,$_{v}^{′}=$ (J ′ iJ ′ iJ ′ + J ′)/2, v,v′(t) $=$ v,v v,v v,v v,v

$$ho p^{−}$$

(J ′ +iJ ′ +iJ ′ J ′)/2 and $v=$ ($^{Ω}_{\nu}$(t) i$^{Ω}_{\nu}$(t))/$\sqrt 2$. Here, Hg (t) is a particle hopping term between v,v v,v v,v v,v

$$− D −_{s}_{q}$$

diﬀerent bosonic modes and conserves the total particle number $N=$ nv, Hg (t) can be considered to be a disp multi-mode squeezing term in the Hamiltonian and Hg (t) displaces the individual bosonic modes. Both Hg (t) disp and Hg (t) do not conserve the total particle number N. It will also be convenient to deﬁne the constant as the smallest number such that for all t and v

$$_{v}_{,}_{v}^{′}(t).(S 2 6)$$

$$|G| \le G$$

Furthermore, it can be noted that v(t) Ω/$\sqrt 2$.

$$|D| \le$$

Finally, the noise in the dynamics of the bosonic and fermionic models will be modeled by the Lindbladian n given

$$_{n}=\kappa_{l}^{(}^{l}^{)},(S 2 7)$$

$$D^{L}i,\sigma$$

$$l=1 i,\sigma$$

where $_{L}\rho=L \rho L_{†}L_{†}L$,$\rho$ /2, L $=a_{i}$,$\sigma$ (incoherent particle loss), L $=a^{†}$ (incoherent particle gain), and

$$i,\sigma i,\sigma i,\sigma$$

$$D − \{\}$$

L $=a^{†}a_{i}$,$\sigma=ni$,$\sigma$ (dephasing). Unless otherwise mentioned, we will assume that all three dissipators act on each

$$i,\sigma i,\sigma$$

mode $\kappa 1$,$\kappa 2$,$\kappa_{3}>0$ and will denote the total dissipation rate by $\kappa=\kappa_{1}$+$\kappa 2$+$\kappa 3$. We summarize all the parameters of the model in Table SII. II. HIGHNOISESIMULABILITYOFTHEFERMIONICMODEL(THEOREM1) In this section, we will present the proof of Theorem 1, which establishes the high-noise simulability of the fermionic model. We will ﬁrst analyze the Trotterization of the continuous-time model, followed by analyzing each Trotter timestep to establish its convex Gaussianity for high noise and to obtain an explicit algorithm for classically simulating either sampling from or computing local observables in the fermionic state. We begin with a ﬁrst-order Trotter approximation to $\rho$(t) with the following splitting of the Lindbladian (t) into a Gaussian and non-Gaussian Lindbladian:

$$(t)=i[H_{g}(t),]+\kappa_{l}^{(}^{l}^{)}i[H_{n}_{g}(t),]+\kappa_{3}^{(}^{3}^{)},$$

$$D^{L}i,\sigma − \cdot D^{L}i,\sigma$$

$$l 1,2 i,\sigma i,\sigma$$

$$∈ X \{\}XX$$

$$_{g}(t)^{n}^{g}(t)$$

We next Trotterize the state $\rho$(|t) into T Trotte{rzsteps: The Tro}t|terized state{$\sigma^{z}_{T}$ will be giv}en by ng g

$$\sigma_{T}=\Phi \Phi \rho(0),(S 2 9 a)$$

$$\tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta$$

$$(cid:18)\tau=T(cid:19)$$

TABLE SII. Table of all the coeﬃcients and parameters relevant to the bosonic and fermionic models.

$$wh er e \delta=t/Ta nd$$

ng g

$$\Phi_{′}=ex p_{n}_{g}(s)ds an d \Phi_{′}=ex p_{g}(s)ds .$$

$$t,tt,t$$

$$T_{t}^{′}LT_{t}^{′}L$$

(cid:18)Z (cid:19) (cid:18)Z (cid:19) We ﬁrst provide a bound on $\sigma_{T}\rho$(t) .

$$∥ − ∥$$

Lemma 3 (Trotterization: Fermionic model). For all $T>0$,

$$\sigma_{T}\rho(t)\Lambda .$$

$$∥ − ∥ \le T$$

Proof. Noting that ng(s) 2m(UC + Uos + $\kappa 3$) and g(s) 2m(JC + Jos + $\kappa 1$ + $\kappa 2$), we obtain that the

$$∥ L ∥_{⋄} \le ∥ L ∥_{⋄} \le$$

parameter ℓ in Lemma 2 can be chosen to be 2$m \Lambda$. The lemma statement then follows directly from Lemma 2. Lemma 4 (Convex-gaussianity condition for 2-fermionic modes). Consider a Lindbladian on two fermionic modes given by

$$(t)=i[h(t),]+\kappa_{i}(t)_{n},$$

$$L − \cdot D$$

$$∈ X \{\}$$

where h(t) $=u$(t)n1n2 and ni is the number operator for the i mode. If $\kappa i$(t) u(t) , then the channel

$$t+\tau \ge ||$$

exp( (s)ds) generated by the Lindbladian in the time interval (t,t + $\tau$) maps a convex Gaussian state to another convex Gaussian state. Proof. It will be convenient to deﬁne the scalars

$$t+\tau t+\tau$$

$$U=u(s)ds,K_{i}=\kappa_{i}(s)ds,an dK=K_{1}+K_{2}.$$

| Parameter                             | Defined in   | Informal description                                                                                 |
| ------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| Jα,α′ Jα,α′ (t) or (t) v,v′ i,σ;i′,σ′ | Eq. (S17)    | Gaussian coupling between two fermionic or bosonic modes                                             |
| JC                                    | Eq. (S19)    | MaximumtotalstrengthofGaussiancouplingbetweena mode and all other modes at different sites           |
| Jos                                   | Eq. (S20)    | MaximumtotalstrengthofGaussiancouplingbetweena mode and all other modes at the same site             |
| U v,v′(t) or U i,σ;i′,σ′(t)           | Eq. (S18)    | Non-Gaussian interaction between two fermionic or bosonic modes                                      |
| UC                                    | Eq. (S21)    | Maximumtotalstrengthofnon-Gaussianinteractionbe- tween a mode and all other modes at different sites |
| Uos                                   | Eq. (S22)    | Maximumtotalstrengthofnon-Gaussianinteractionbe- tween a mode and all other modes at the same site   |
| Λ                                     | Eq. (S24)    | Total coupling strength                                                                              |
| Ωv(t) or Ωi,σ(t)                      | Eq. (S17)    | On-site displacement acting on bosonic modes                                                         |
| Jv,u(t)                               | Eq. (S25)    | Gaussian hopping between two bosonic modes                                                           |
| Gv,u(t)                               | Eq. (S25)    | Multi-mode squeezing term between two bosonic modes                                                  |
| G                                     | Eq. (S26)    | Maximumstrengthofmulti-modesqueezingbetweenone bosonic mode with all other modes                     |
| Dv(t)                                 | Eq. (S25)    | Single-mode displacement acting on bosonic modes                                                     |
| κ                                     | Eq. (S27)    | Total dissipation rate                                                                               |
| κ1                                    | Eq. (S27)    | Dissipation rate for incoherent particle loss                                                        |
| κ2                                    | Eq. (S27)    | Dissipation rate for incoherent particle gain                                                        |
| κ3                                    | Eq. (S27)    | Dissipation rate for dephasing                                                                       |
| γ                                     | Assumption 2 | Defined as γ =κ1−κ2−2G                                                                               |
| n                                     | —            | Number of sites                                                                                      |
| L                                     | —            | Number of modes per site                                                                             |
| m                                     | —            | Total number of modes m=nL                                                                           |

We also note that, since both the Hamiltonian and the jump operators are expressible as polynomials of the fermionic number operators n1,n2, they commute with each other. Therefore,

$$t+\tau$$

exp (s)ds $=e$xp iU[n1n2, ] exp K1 n exp K2 n .

$$T_{t}L − \cdot DD$$

$$(cid:18)Z(cid:19)$$

(cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1) We deﬁne the channel t+$\tau$,t via

$$E_{\sqrt}i \pi/4$$

$$_{t}_{+}_{\tau}_{,}_{t}(\rho)=_{z}R(z)\rho R^{†}(z)wh er eR(z)=ex pU e^{−}(zn_{1}+z^{∗}n_{2}),$$

where $z=$ (a+ib)/$\sqrt 2$ with a,b bein(cid:0)g independen(cid:1)t standard normal (cid:0)random variables. Note(cid:1)that, due to Lemma 1, t+$\tau$,t maps an input Gaussian state to a (possibly unnormalized) convex-Gaussian state. Wenowexplicitlycompute t+$\tau$,t($\rho$). deﬁne i,l as the superoperator which left multiplies by ni (i.e. i,l($\rho$) $=n_{i}\rho$)

$$RN N$$

and i,r as the superoperator which right multiplies by ni (i.e. i,r($\rho$) $=\rho n_{i}$). Then

$$E_{\sqrt}i \pi/4_{\sqrt}_{∗}i \pi/4$$

$$t+\tau,t^{=}z^{e}^{x}^{p}^{U}^{e}−^{(}^{z}1,l^{+}^{z}∗ 2,l^{)}^{+}^{U}^{e}^{(}^{z}∗ 1,r^{+}^{z}2,r^{)}$$

$$RN NN N$$

E (cid:0) (cid:0) a $_{\sqrt}i \pi$/4 $\sqrt ∗ i \pi$/4 (cid:1)(cid:1)

$$^{=}a^{e}^{x}^{p}^{U}^{e}−^{(}1,l^{+}2,l^{+}^{U}^{e}^{(}1,r^{+}2,r$$

$$\sqrt 2 NN NN \times$$

(cid:18) (cid:18) (cid:19)(cid:19) (cid:0) ib (cid:1) (cid:1)(cid:1)

$$E_{\sqrt}i \pi/4_{\sqrt}_{∗}i \pi/4$$

b exp Ue− ( 1,l 2,l U e ( 1,r 2,r

$$\sqrt 2 N − N − N − N$$

(cid:18) (cid:18) (cid:19)(cid:19) (cid:0) U (cid:1) U (cid:1)(cid:1)

$$^{=}^{e}^{x}^{p}^{i}^{(}1,l^{+}2,l^{)}^{+}^{i}^{(}1,r^{+}2,r^{)}^{+}^{|}^{|}^{(}1,l^{+}2,l^{)}^{(}1,r^{+}2,r^{)}$$

$$− 4 NN 4 NN 2 NN NN \times$$

$$(cid:18)(cid:19)$$

$$^{e}^{x}^{p}^{i}^{(}1,l 2,l^{)}^{i}1,l 2,r^{+}^{|}^{|}^{(}1,l 2,l^{)}^{(}1,r 2,r$$

$$4 N − N − 4 N − N 2 N − NN − N$$

$$(cid:18)(cid:19)$$

$=e$xp iU( 1,l 2,l 1,r 2,r) + (cid:0)U ( 1,l 1,r(cid:1)+ 2,l 2,r) , (cid:1)

$$− NN − NN||NN NN$$

$$(cid:0)Ex OO^{2}(cid:1)/2$$

where, in(1), wehaveusedthefactthat, foranyoperatorO, x (0,1)(e ) $=e$ . Identifying 1,l 2,l 1,r 2,$r=$ ∈N N N −N N [n1n2, ], we obtain that

$$ex p(iU[n_{1}n_{2},])=ex p(U(_{1}_{,}_{l}_{1}_{,}_{r}+_{2}_{,}_{l}_{2}_{,}_{r}))_{t}_{+}_{\tau}_{,}_{t}.$$

$$− \cdot −||NN NN R$$

Using Eq. (S34) and Eq. (S31) together with the fact that $n=$ i,l i,r ( + i,r)/2, we obtain that

$$^{i}i,l$$

$$DN N − NN$$

$$t+\tau$$

$$ex p(s)ds=ex p((K_{i}U)_{i}_{,}_{l}_{i}_{,}_{r})ex p((_{i}_{,}_{l}+_{i}_{,}_{r})/2)_{t}_{+}_{\tau}_{,}_{t}.$$

$$T_{t}L −||NN − NN R$$

(cid:18)Z (cid:19) (cid:18)i 1,2 (cid:19)

$$∈ Y \{\}^{i}_{i}$$

We note that t+$\tau$,t and i are completely posit|ive maps t{hzat map con}v|ex Gaussi{azn states to} possibly unnormalized Gaussian states. Furthermore, if Ki U , which is implied by $\kappa i$(t) u(t) quoted in the lemma statement, then

$$\ge ||^{t}^{+}^{\tau} \ge ||$$

i also have this property. Consequently, since exp( (s)ds) is a channel, as long as Ki U , it maps convex

$$ET L \ge ||$$

Gaussian states to (normalized) convex Gaussian states. Theorem 1 (High-noise convex Gaussianity and classical simulation of the fermionic model, reproduced from the main text). For an initial Gaussian state, if $\kappa 3$ 2U, then the state of the fermionic model at time t, $\rho$(t), is convex $\ge$ Gaussian for all t 0. Furthermore, $\rho$(t) can be classically sampled in the Fock state basis to an $\epsilon$ total variation

$$7 2 2^{ \ge }$$

$$er ro ri nO(m \Lambda t/\epsilon)ti me .$$

Proof. Consider the Trotterized state $\sigma T$ [Eq. (S29)]—note that $\Phi$ is a Gaussian channel and hence trivially

$$− ng$$

preserves convex Gaussianity. We now obtain the condition under which $\Phi$ also preserves convex Gaussianity using Lemma 4. We ﬁrst perform the decomposition

$$=ex p_{v}_{,}_{u}(s)ds wh er e_{v}_{,}_{u}=i[U_{v}_{,}_{u}(t)n_{v}n_{u},]+\kappa_{3}p_{v}_{,}_{u}(t)_{n}+q_{v}_{,}_{u}(t)_{n},(S 3 6)$$

$$\tau \delta,(\tau 1)\delta^{v}^{u}$$

$$_{−}T_{(}_{\tau}_{1}_{)}_{\delta}LL − \cdot DD$$

$$v,u(cid:18)Z_{−}(cid:19)$$

$$(cid:0)(cid:1)$$

where we choose

$$1 U_{v}_{,}_{u}(t)1 U_{v}_{,}_{u}(t)$$

$$p_{v}_{,}_{u}(t)=||an dq_{v}_{,}_{u}(t)=|$$

$$2 U_{v}_{,}_{u}(t)2 U_{v}_{,}_{u}(t)$$

$$||||$$

Next, we apply Lemma 4: For v,u(t) to generate a channel that is convex-Gaussianity preserving, a suﬃcient condition is that

$$\kappa_{3}p_{v}_{,}_{u}(t),\kappa_{3}q_{v}_{,}_{u}(t)U_{v}_{,}_{u}(t)or eq ui va le nt ly \kappa_{3}2 U_{k}_{,}_{k}^{′}(t)fo rk v,u .$$

$$\ge || \ge ||∈ \{\}$$

Since ′ Uk,k′(t) UC + Uos, this condition is satisﬁed if $\kappa 3$ 2(UC + Uos). Assuming this to be true, it then

$$|| \le^{n}^{g} \ge$$

follows from Lemma 4 that $\Phi$ maps an input Gaussian state to a convex-Gaussian state—consequently, the

$$^{P}^{−}2 2 2$$

Trotterized state $\sigma T$ is a convex-Gaussian state such that $\rho$(t) $\sigma_{T}\epsilon$ when $T=\Theta$(t m $\Lambda$ /$\epsilon$).

$$∥ − ∥ \le$$

Time-complexity of sampling in the Fock state basis. Since $\sigma T$ is convex-Gaussian by construction, it can be expressed as $\sigma_{T}=\rho_{\alpha}d µ$($\alpha$), where $\rho \alpha$ is a Gaussian state and µ is a probability measure. To sample from $\sigma T$, we can then ﬁrst sample from µ to obtain a Gaussian state and then use the standard algorithm for sampling from fermionic Gaussian states. Consider sampling from µ($\alpha$): Suppose the initial state $\rho$(0) is a Gaussian state. Lemma4providesanexplicitcharacterizationoftheconvexcombinationofGaussianstatesthatresultwhenapplying exp( v,u(s)ds) on an input Gaussian state. Furthermore, since the covariance matrix of the Gaussian state T − L is a 2m 2m matrix, the probabilities of each Gaussian state in the convex combination being computable from

$$R \times^{3}$$

the result for covariance matrices of products of Gaussian states [S2, S4] in O(m ) time—sampling from this convex combination thus requires O(m ) time. At every time-step, this has to be done for every pair of fermionic modes to apply $\Phi$ , thus yielding a total time-complexity of O(m ). The application of the Gaussian evolution in each time-step can also be done at the level of covariance matrices in O(m ) time. Thus, the total time of sampling from µ is given by O(m T) $=O$(m $\Lambda$ t /$\epsilon$). Finally, having sampled a Gaussian state $\rho \alpha$ from $\sigma T$, we can draw a sample in the Fock state basis in O(m ) time [S5, S6]—the total time complexity of the sampling algorithm thus is dominated by the cost of sampling from µ and is given by O(m $\Lambda$ t /$\epsilon$). III. HIGH-NOISESEPARABILITYOFTHEBOSONICMODEL(THEOREM2) In this section, we will present proof of Theorem 2, which considers the high-noise regime of the bosonic model. Since the bosonic model is inﬁnite-dimensional with unbounded terms in the Hamiltonian, its analysis ﬁrst requires an analysis of the particle number (as well as its moments) in the model. We do so in the ﬁrst subsection—then, in the proof of Theorem 2, we ﬁrst approximate the inﬁnite-dimensional bosonic modes with ﬁnite-dimensional qudits and quantify the approximation error. Finally, we analyze the resulting ﬁnite-dimensional model and establish high-noise separability in the model. A. Analyzing particle number moments We begin by introducing a physically motivated assumption on the initial state of the model—the initial state will be assumed to be a product state with a “uniform particle moment density” assumption, similar to that used in Ref. [S7]. Assumption 1 (Uniform particle moment density). The initial state $\rho$(0) is a product state and C0,$\alpha 0$,$\beta_{0}>0$ such that v and k 1,2,3...

$$∀ ∈ \{\}$$

$$kk \alpha^{0}k+\beta^{0}$$

$$Tr(n_{v}\rho(0))C_{0}k .$$

$\le$ As shown in Ref. [S7], this assumption is satisﬁed for a wide variety of physically relevant initial states of the bosonic model, notably for the vacuum state, thermal states, as well as coherent states. Furthermore, it implies a bound on the moments of the total particle number $N=$ nv since

$$kk 1/kk \alpha^{0}k+\beta^{0}$$

$$Tr(N \rho(0))=Tr(n_{v}n_{v}. . . n_{v}\rho(0))Tr(n_{v}\rho(0))(C_{0}m)k,(S 3 9)$$

$$\le \le$$

$$v^{1},v^{2}. . . v_{k}v^{1},v^{2}. . . v_{k}i=1$$

$$XX Y$$

where we remind the reader that $m=nL$ is the total number of bosonic modes in the model. This particle number moment bound, in turn, implies that the probability of high-particle-number states being occupied is exponentially suppressed, which we make precise in the following lemma.

Lemma 5 (Probability of high-particle-number states (Ref. [S7])). Suppose $\rho$ is a state which satisﬁes Tr($N^{k}\rho$)

$$k \alpha k+\beta^{ \le }$$

(Cm) k and $\Pi$ d is a projector on the subspace with d particles, then

$$\ge \ge$$

$$\alpha/\beta \beta/\alpha$$

$$de 1/\alpha$$

$$(d/Cm e)$$

$$Tr(\Pi_{d}\rho)e^{−}.$$

$$^{ \ge } \le Cm e$$

$$(cid:18)(cid:19)$$

Proof. Note that, for any $k>0$,

$$k \alpha k+\beta \beta^{C}^{m}^{k}$$

$$dT r(\Pi_{d}\rho)Tr(N \Pi_{d}\rho)Tr(N \rho)(Cm)k=Tr(\Pi_{d}\rho)k .(S 4 0)$$

$$^{ \ge } \le^{ \ge } \le \le \Rightarrow^{ \ge } \le d$$

$$(cid:18)(cid:19)$$

$$1/\alpha 1/\alpha$$

We can now pick k to be the greatest integer smaller than (d/Cme) —we then have that (d/Cme) 1 k

$$1/\alpha − \le \le$$

(d/Cme) and therefore

$$\beta/\alpha_{\alpha}_{/}_{\beta}\beta/\alpha$$

$$dd e^{1}^{/}^{\alpha}$$

$$(d/Cm e)$$

$$Tr(\Pi_{d}\rho)e^{−}e^{−},(S 4 1)$$

$$^{ \ge } \le Cm e \le Cm e$$

(cid:18) (cid:19) (cid:18) (cid:19) which proves the lemma statement. While we will assume that the uniform particle moment density condition holds for the initial state, the subsequent dynamics of the bosonic model could possibly violate this condition. In the remainder of this section, we show that under the condition that the total rate of particle loss is higher than the total rate of particle gain (which we make precise below in assumption 2), the moments of the total particle number Tr($N \rho$(t)) satisfy an inequality similar to Eq. (S39), which by Lemma 5 implies that the probability of higher particle number states being occupied is super-polynomially small in the particle number. Assumption 2. The parameters $\kappa 1$,$\kappa 2$ and are such that $2 \gamma=\kappa_{1}\kappa_{2}$ 2 $>0$.

$$G − − G$$

Physically, this assumption restricts the rate of 3 processes in the bosonic model that can change its particle number: In the noise terms, incoherent particle loss can decrease the particle number at a rate $\kappa 1$ and incoherent particle

$$^{ \sim }sq$$

gain can increase the particle number at a rate $\kappa 2$. Furthermore, in the Hamiltonian, the squeezing term (Hg (t) in Eq. (S25)) can also increase the number of particles in the system at a rate . Assumption 2 constrains the model to have particle loss higher than particle gain, without which the number of particles can increase arbitrarily with time. disp We remark that we do not need any assumption on the strength of displacement term (Hg (t) in Eq. (S25))—we will show in Lemma 8 that, as long as assumption 2 is satisﬁed, no matter how large the displacement term is, the particle number (and its moments) do not grow arbitrarily with time. We begin with a two technical lemmas that will be useful in our analysis. Lemma 6. Suppose xk(t), for k 0,1,2... , are non-negative functions of time which satisfy the diﬀerential

$$∈ \{\}$$

inequalities

$$d_{q}k$$

$$x_{k}(t)\gamma kx_{k}(t)+\lambda mk 2 x_{k}_{q}(t),$$

$$dt \le − q^{−}$$

$$q=1(cid:18)(cid:19)$$

$$k \alpha^{0}k+\beta^{0}$$

where $\gamma$,$\lambda$,$m>0$. Furthermore, suppose x0(t) $=1$ t 0 and C0,$\alpha 0$,$\beta_{0}>0$ : xk(0) (C0m) k for all

$$∀ \ge ∃ \le$$

k 1,2,3... . Then

$$∈ \{\}$$

$$\alpha k+\beta \lambda/\gamma$$

$$x_{k}(t)(Cm)e,wh er eC=e(C_{0}+2),\alpha=ma x(\alpha_{0},1)an d \beta=\beta_{0}.$$

$\le$ Proof. The diﬀerential inequality can be written as an integral inequality:

$$\gamma kt q^{k}\gamma k(ts)$$

$$x_{k}(t)x_{k}(0)e^{−}+\lambda mk 2 x_{k}_{q}(s)e^{−}^{−}ds .(S 4 2)$$

$$\le q_{0}−$$

$$q=1(cid:18)(cid:19)Z$$

Recursing Eq. (S42), we obtain

$$p − 1$$

$$kk kq^{1}kP^{i}^{=}^{1}q^{i}^{p}_{q}_{p}pi 1$$

$$− − 2^{P}^{i}^{=}^{1}^{i}\lambda k ! −$$

$$\gamma kt(k)$$

$$x_{k}(t)x_{k}(0)e^{−}+_{p}kq_{j}x_{k}^{p}_{q}(0)I_{q}_{,}_{q}_{.}_{.}_{.}_{q}(t),$$

$$Pi=1 i 1 2 p$$

$$\le \cdot \cdot \cdot q_{1}! q_{2}! . . . q_{p}!(kq_{i})! −^{−}$$

$p=1$q$_{1}=1$q$_{2}=1$ $q_{p}=1_{−}^{i}^{=}^{1}$ (cid:18)$i=1$(cid:18) $j=1$ (cid:19)(cid:19) XXX

where t s1 sp−1

$$(k)\gamma k(ts^{1})\gamma(kq^{1})(s^{1}s^{2})\gamma(kq^{1}q^{2})(s^{2}s^{3})\gamma(kq^{1}q^{2}q^{p})s^{p}$$

$$^{I}_{q}_{,}_{q}_{.}_{.}_{.}_{q}^{(}^{t}^{)}^{=}^{e}− −^{e}− − −^{e}− − − −^{.}^{.}^{.}^{e}− − − \cdot \cdot \cdot −^{d}^{s}1^{d}^{s}2^{.}^{.}^{.}^{d}^{s}p$$

$$0 0 \cdot \cdot \cdot 0$$

Z Z Z

$$ts 1 s 2 sp − 1$$

$$k \gamma t \gamma(q^{1}s^{1}+q^{2}s^{2}+. . . q^{p}s^{p})$$

$$=e^{−}ed s_{1}ds_{2}. . . ds_{p}.$$

$$0 0 0^{\cdot}^{\cdot}^{\cdot}0$$

Z Z Z Z

$$(k)$$

We note that Iq1,q2...qp(t) can be upper bounded:

$$tt t$$

$$(k)k \gamma t \gamma(q^{1}s^{1}+q^{2}s^{2}+. . . q^{p}s^{p})$$

Iq ,q ...q (t) e− e ds1ds2 ...dsp

$$\le \cdot \cdot \cdot$$

$$Z − \infty Z − \infty Z − \infty$$

$$^{1}(kq^{1}q^{2}. . . q^{p})\gamma t$$

$$^{e}− − − −$$

$$\le \gamma^{p}q_{1}q_{2}. . . q_{p}$$

$$^{1}\gamma(tq^{1}q^{2}. . . q^{p})$$

$$e^{−}^{−}^{−}^{−}.(S 4 5)$$

$$\le \gamma^{p}$$

In the calculation done below, it will be useful to note that, given any f(n) where n 0,1,2... ,

$$∈ \{\}$$

$$p − 1 p − q$$

$$kk q^{1}kP_{i}_{=}_{1}q^{i}pk qq q^{1}qP_{i}_{=}_{1}q^{i}$$

$$− − 1 − − 1$$

$$fq_{i}=f(q)$$

$$\cdot \cdot \cdot q_{1}! q_{2}! . . . q_{p}! \cdot \cdot \cdot q_{1}! q_{2}! . . . q_{p}!$$

$$q^{1}=1 q^{2}=1 q^{p}=1(cid:18)i=1(cid:19)q=pq^{1}=1 q^{2}=1 q^{p}=1$$

XXX

$$=f(q)$$

q1!q2!...qp!

$$q=pq^{1},q^{2}. . . q^{p}1$$

$$^{X}q^{1}+q^{2}^{X}+. . . q^{ \ge }^{p}=q$$

$$\le q !$$

$$q=p$$

wherein(1)wehaveintroducedtheindex$q=q$1+q2+...qp, whichrangesfromptok, andre-expressedthesummation over q1,q2...qp as ﬁrst a sum over q, and then a sum over q1,q2...qp subject to the contraint q1 + q2 + ...$q_{p}=q$. In (2), we have simply noted the fact that the summation over q1 1,2...q ,q2 1,2...q q1 ...qp 1

$$∈ \{\}∈ \{− \}^{−}∈$$

1,2...q (q1 + q2 + qp 1) is identical to summation over q1,q2...qp 1,2...q with the additional constraint

$$\{−^{−}\}∈ \{\}$$

that q1 +q2 +...qp q. Finally, (3) is obtained by identifying the summation as a multinomial sum. $\le$ Returning to Eq. (S43), we obtain that

$$_{(}_{1}_{)}^{k}^{k}^{k}^{k}q^{1}+q^{2}. . . q^{p}^{p}$$

$$_{\gamma}_{k}_{t}k ! 2 \lambda mk_{(}^{p}_{)}$$

$\gamma tk P$ qi

$$x_{k}(t)x_{k}(0)e^{−}+_{p}x_{k}^{p}_{q}(0)e^{−}^{−}^{i}^{=}^{1}$$

$$\le \cdot \cdot \cdot q_{1}! q_{2}! . . . q_{p}!(kq_{i})! p ! \gamma^{−}^{P}^{i}^{=}^{1}^{i}$$

$$p=1 q_{1}=1 q_{2}=1 q_{p}=1_{−}^{i}^{=}^{1}(cid:18)(cid:19)$$

XXX X

$$kk pP$$

$$\gamma kt q \gamma tk q)$$

$$x_{k}(0)e^{−}+(2 p)x_{k}_{q}(0)e^{−}^{−}$$

$$\le q \gamma^{−}$$

$p=1 q=p$ (cid:18) (cid:19)(cid:18) (cid:19)

$$kq p$$

$$k \alpha^{0}k+\beta^{0}\gamma kt q^{k}^{\lambda}^{m}^{k}kq \alpha^{0}(kq)+\beta^{0}\gamma t(kq)$$

$$(C_{0}m)ke^{−}+(2 k)(C_{0}m)^{−}(kq)^{−}e^{−}^{−}$$

$$\le q \gamma −$$

$q=1 p=1$ (cid:18) (cid:19)(cid:18) (cid:19)

$$k \alpha^{0}k+\beta^{0}\gamma kt kk \lambda/\gamma^{k}qk q \alpha^{0}(kq)+\beta^{0}\gamma t(kq)$$

$$(C_{0}m)ke^{−}+me(2 k)C_{0}^{−}k^{−}e^{−}^{−}$$

$$\le q$$

$$q=1(cid:18)(cid:19)$$

$$\lambda/\gamma k \beta^{0}^{k}\alpha^{0}\gamma tk qq \lambda/\gamma k \beta^{0}\alpha^{0}\gamma tk$$

$$(em)k(C_{0}ke^{−})^{−}(2 k)=(em)k(C_{0}ke^{−}+2 k),(S 4 7)$$

$$\le q$$

$$q=1(cid:18)(cid:19)$$

$$\alpha^{0}\gamma t$$

where, in (1), we have used Eq. (S45) and in (2) we have used Eq. (S46). Finally, using C0k e− + 2k

$$ma x(\alpha_{0},1)^{ \le }$$

(C0 +2), the lemma statement follows. Lemma 7. For any $k>0$,v,

$$kk kk kk$$

$$[a_{v},N]=a_{v}(N(NI))an d[a_{v},N]=((N+I)N)a_{v}.$$

$$− − −$$

Furthermore, for any $k>0$,v, a†vN av nvN .

$$zN zN z$$

Proof. We begin by noting that, for any z, it follows from e $a_{v}e_{−}=e_{−}a_{v}$ that

$$zN zN zN zN z(NI)z(N+I)zN$$

$$[a_{v},e]=a_{v}ee a_{v}=a_{v}(ee^{−})=(ee)a_{v}.$$

$$− − −$$

We thus obtain that

$$k^{d}zN kk kk$$

$$[a_{v},N]=[a_{v},e]=a_{v}N(NI)=(N+I)N)a_{v}.(S 4 9)$$

dzk

$$_{(cid:12)}z=0$$

(cid:12) (cid:0) (cid:1) (cid:0)

$$(cid:12)$$

Furthermore, for any state $\psi=\psi_{⃗}_{n}⃗ n$ , w(cid:12)here $^{\psi}⃗ n$ is the amplitude of $\psi$ on the basis state $⃗ n=n$1,n2 ...nm ,

$$|\rangle|\rangle|\rangle|\rangle|\rangle$$

$$kP 2 k 2 kk$$

$$\psi a^{†}_{v}Na_{v}\psi=\psi_{⃗}_{n}n_{v}(⃗ n 1)\psi_{⃗}_{n}n_{v}⃗ n=\psi n_{v}N \psi,$$

$$\langle||\rangle||∥ ∥ − \le ||∥ ∥ \langle||\rangle$$

$$⃗ n ⃗ n$$

from which it follows that a†vN av nvN . In the next lemma, we derive an upper bound on Tr($N \rho$(t)), which will be central to analyzing the Hilbert space truncation and Trotter bounds in the subsequent subsections. Lemma 8 (Upper bounding particle number moments). Consider a bosonic model satisfying assumption 2 with the bosonic modes in an initial state $\rho$(0) satisfying assumption 1, then, t 0,

$$∀ \ge$$

$$kk \alpha k+\beta$$

$$Tr(N \rho(t))(Cm)k,$$

$\le$

$$1+4 Ω/\gamma+2/\gamma+4(\kappa_{1}+\kappa_{2})/\gamma$$

where $C=e$ G (C0 +2),$\alpha=m$ax($\alpha 0$,1) and $\beta=\beta_{0}$ with C0,$\alpha 0$,$\beta 0$ deﬁned in assumption 2. Proof. We will use the Heisenberg equations of motion for the operator N . Note that [N ,Hng(t)] $=$ k hop k hop 0,[N ,Hg (t)] $=0$ and n† (N ) $=0$ (where Hg (t) is deﬁned in Eq. (S25)). Using notation $O_{t}=T$r($O \rho$(t)), we

$$D \langle \rangle$$

then have that k sq k disp

$$N_{t}=\kappa_{1}_{a}^{†}(N)_{t}+\kappa_{2}^{†}_{†}(N)_{t}i[N,H_{g}(t)]_{t}i[N,H_{g}(t)]_{t}.(S 5 1)$$

$$dt \langle \rangle \langle D^{v}\rangle \langle D^{a}^{v}\rangle − \langle \rangle − \langle$$

$$X(cid:0)(cid:1)$$

$$_{n}(N)^{t}$$

$$\langle L \rangle$$

$$|\{z \}$$

Consider ﬁrst a† (N ), ††(N )—using Lemma 7, we obtain that D v Dav

$$kk kk kl^{k}kl$$

$$_{a}^{†}(N)=a^{†}_{v}[a_{v},N]=NN(NI)=kN+(1)N^{−},$$

$$D − − − − − − l+1$$

$$l 1(cid:18)(cid:19)$$

$$(cid:0)(cid:1)X^{ \ge }$$

$$kk kk k^{k}^{+}^{1}kl$$

$$^{†}_{†}(N)=[a_{v},N]a^{†}_{v}=(N+I)N(N+I)=kN+N^{−}.(S 5 2)$$

Dav

$$l 1(cid:18)(cid:19)$$

$$(cid:0)(cid:1)X^{ \ge }$$

Therefore,

$$kk l^{k}^{k}^{+}^{1}kl$$

$$^{†}_{n}(N)_{t}=(\kappa_{1}\kappa_{2})kN_{t}+\kappa_{1}(1)+\kappa_{2}N^{−}_{t}$$

$$\langle L \rangle − − \langle \rangle − l+1 l+1 \langle \rangle$$

$l=1$ (cid:18) (cid:18) (cid:19) (cid:18) (cid:19)(cid:19)

$$kk l$$

$$(\kappa_{1}\kappa_{2})kN_{t}+\kappa_{1}k+\kappa_{2}(k+1)N^{−}_{t}$$

$$\le − − \langle \rangle l \langle \rangle$$

$$l=1(cid:18)(cid:19)$$

$$X(cid:0)(cid:1)$$

$$kl^{k}kl$$

$$(\kappa_{1}\kappa_{2})kN_{t}+2(\kappa_{1}+\kappa_{2})km 2 N^{−}_{t},(S 5 3)$$

$$\le − − \langle \rangle l \langle \rangle$$

$$l=1(cid:18)(cid:19)$$

$$kk kk+1 k$$

where we implicitly set $=0$ if $l<0$ or $l>k$ and in (1) we have used the fact that

$$ll+1 ll+1 l$$

$$\le \le$$

(cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1)

$$ks qk$$

Next, consider [N ,Hg (t)] $=$ v,u(t)[N ,avau] h.c. — we begin by noting that from Lemma 7

$$v,u$$

$$kk kk 2 l 1$$

$$[N,a_{v}a_{u}]=[a_{v},N]a_{u}a_{v}[a_{u},N]=2 a_{v}N^{−}^{−}a_{u},$$

$$− − − 2 l+1$$

$$l 0(cid:18)(cid:19)$$

$$X \ge$$

and therefore k sq k

$$[N,H_{g}(t)]_{t}2_{v}_{,}_{u}(t)[N,a_{v}a_{u}]_{t}$$

$$\langle \rangle \le |G||\langle \rangle|$$

v,u

$$(cid:12)(cid:12)X$$

$$(cid:12)(cid:12)(1)$$

v,u(t) avN − − au t

$$\le |G|2 l+1|\langle \rangle|$$

$$(cid:18)(cid:19)$$

$$XX^{ \ge }$$

$$v,u^{(}^{t}^{)}^{a}v^{N}− −^{a}†_{v}t^{+}^{T}^{r}^{(}^{a}†_{u}^{N}− −^{a}ut$$

$$\le |G|2 l+1|\langle \rangle||\langle \rangle|$$

$$(cid:18)(cid:19)$$

$$XX^{ \ge }(cid:0)(cid:1)$$

$$^{k}k 2 l 1 k 2 l 1$$

$$^{a}u^{N}− −^{a}†_{u}t^{+}^{a}†_{u}^{N}− −^{a}ut$$

$$\le G 2 l+1 \langle \rangle \langle \rangle$$

$$ul 0(cid:18)(cid:19)$$

$$XX^{ \ge }(cid:0)(cid:1)$$

$$(N+I)^{−}^{−}a_{u}a^{†}_{u}_{t}+(NI)^{−}^{−}a^{†}_{u}a_{u}_{t}$$

$$\le G 2 l+1 \langle \rangle \langle − \rangle$$

$$ul 0(cid:18)(cid:19)$$

$$XX^{ \ge }(cid:0)(cid:1)$$

$$^{k}^{k}^{2}^{l}^{1}_{k}_{2}_{l}_{2}_{p}^{k}^{k}^{2}^{l}^{1}_{k}_{2}_{l}_{p}_{1}$$

$$2 − − N^{−}^{−}_{t}+2 m − − N^{−}^{−}^{−}_{t}.$$

$$\le G 2 l+1 2 p \langle \rangle G 2 l+1 p \langle \rangle$$

l,p 0(cid:18) (cid:19)(cid:18) (cid:19) l,p 0(cid:18) (cid:19)(cid:18) (cid:19)

$$X \ge X \ge$$

where, in (1), we have used Eq. (S54), in (2) we have used the fact that, for any two operators A,B, AB

$$\langle \rangle \le$$

AA† B†B ( AA† + B†B )/2 and in (3) we have used Lemma 7. We can thus conclude that

$$\langle \rangle \langle \rangle \le \langle \rangle \langle \rangle$$

$$^{p}ks qk(k)kq$$

$$[N,H_{g}(t)]_{t}2 kN_{t}+2 f_{q}N^{−}_{t},(S 5 6)$$

$$\langle \rangle \le G \langle \rangle G \langle \rangle$$

$$(cid:12)(cid:12)X^{ \ge }$$

$$(cid:12)(cid:12)$$

where

$$m^{−}if q 1,3,5 . . .,$$

$$(k)l 0 2 l+1 q(2 l+1)$$

$$f_{q}=^{ \ge }^{−}_{(}_{2}_{+}_{1}_{)}∈ \{\}(S 5 7)$$

$$kk lk k(2 l+1)$$

$$_{(}m^{−}+^{−}if q 2,4,6 . . . .$$

Pl 0(cid:0)2l+1(cid:1)(cid:0)q (2l+1)(cid:1) l 0 2l+1 q 2l

$$\ge − \ge −^{∈}^{\{}^{\}}$$

(k) P (cid:0) (cid:1)(cid:0) (cid:1) P (cid:0) (cid:1)(cid:0) (cid:1) The expression for fq can be further simpliﬁed by noting that

$$kk(2 l+1)k ! kq_{q}_{1}k$$

$$−=2^{−},(S 5 8)$$

$$2 l+1 q(2 l+1)(2 l+1)!(kq)!(q(2 l+1))! q 2 l+1 q$$

l 0(cid:18) (cid:19)(cid:18) − (cid:19) l 0 − − (cid:18) (cid:19)l 0(cid:18) (cid:19) (cid:18) (cid:19)

$$X \ge X \ge X \ge$$

and

$$kk(2 l+1)k ! kq+1_{q}k$$

$$−=2 .(S 5 9)$$

$$2 l+1 q 2 l(2 l+1)!(kq 1)!(q 2 l)! q+1 2 l+1 q+1$$

l 0(cid:18) (cid:19)(cid:18) − (cid:19) l 0 − − − (cid:18) (cid:19)l 0(cid:18) (cid:19) (cid:18) (cid:19)

$$X \ge X \ge X \ge$$

We then obtain that

$$2_{−}mi fq 1,3,5 . . .,$$

$$(k)q$$

$$f_{q}=_{k}_{k}∈ \{\}(S 6 0)$$

$$_{(}2_{−}m+2 if q 2,4,6 . . . .$$

$$(cid:0)q(cid:1)q+1$$

$$∈ \{\}$$

(cid:0) (cid:1) (cid:0)(k) (cid:1)

$$kk q 1 kq k$$

Again, we note that, since k , it follows that fq 2 − (m+2k) mk2 , and thus we obtain that

$$\le \le \le$$

(cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1) (cid:0) (cid:1)

$$ks qk^{k}qk q$$

$$[N,H_{g}(t)]_{t}2 kN_{t}+mk 2 N^{−}_{t}.(S 6 1)$$

$$\langle \rangle \le G \langle \rangle Gq \langle \rangle$$

$$q 1(cid:18)(cid:19)$$

$$(cid:12)(cid:12)X^{ \ge }$$

$$(cid:12)(cid:12)$$

k disp Finally, we consider [N ,Hg (t)] $=$ v(t)[N ,av] h.c.—we begin by noting that, from Lemma 7,

$$kk kk q$$

$$[N,a_{v}]=((N+I)N)=N^{−}a_{v},(S 6 2)$$

$$q 1(cid:18)(cid:19)$$

$$X \ge$$

and therefore

$$k^{k}kq$$

$$[N,H_{2}(t)]_{t}2 Ω N^{−}a_{v}_{t}$$

$$\langle \rangle \le q \langle \rangle$$

$$vq 1(cid:18)(cid:19)$$

(cid:12) (cid:12) $XX^{ \ge }$ (cid:12) (cid:12) (cid:12) (cid:12) (cid:12) (cid:12)

$$^{(}^{1}^{)}k 4 Ω 2$$

$$\gamma a †_{v}N^{k}^{q}a_{v}_{t}N^{k}^{q}_{t}$$

$$\le qs \langle \rangle \times \gamma \langle \rangle$$

$$vq 1(cid:18)(cid:19)$$

$$XX^{ \ge }$$

$$^{k}^{\gamma}_{k}_{q}^{2}^{Ω}_{k}_{q}$$

$$^{a}†_{v}^{N}−^{a}vt^{+}^{N}− t$$

$$\le q 2 \langle \rangle \gamma \langle \rangle$$

v q 1(cid:18) (cid:19)(cid:18) (cid:19)

$$XX^{ \ge }$$

$$^{(}^{2}^{)}k \gamma 2 Ω^{2}$$

$$kq kq$$

$$^{N}−^{n}vt^{+}^{N}− t$$

$$\le q 2 \langle \rangle \gamma \langle \rangle$$

v q 1(cid:18) (cid:19)(cid:18) (cid:19)

$$XX^{ \ge }$$

$$\gamma_{k}\gamma k 2 m Ω k_{k}_{q}$$

$$kN_{t}++N^{−}_{t}$$

$$\le 2 \langle \rangle 2 q+1 \gamma q \langle \rangle$$

q 1(cid:18) (cid:18) (cid:19) (cid:18) (cid:19)(cid:19)

$$X \ge$$

$$^{(}^{3}^{)}\gamma \gamma 2 m Ω^{2}k_{k}_{q}$$

$$kN_{t}+k+N^{−}_{t},(S 6 3)$$

$$\le 2 \langle \rangle 2 \gamma q \langle \rangle$$

q 1(cid:18) (cid:19)(cid:18) (cid:19)

$$X \ge$$

where, in (1), we have again used that AB AA† B†B and introduced the parameter $\gamma=\kappa_{1}\kappa_{2}$ 2 from

$$\langle \rangle \le \langle \rangle \langle \rangle^{k}^{q}^{k}^{q}− − G$$

assumption 2, in (2) we have used Lemma 7 to obtain that a†vN − av N − nv , and in (3) we have used the fact

$$_{k}_{k}p \langle \rangle \le \langle \rangle$$

that k . Setting k,m km, we obtain that

$$\le \le$$

(cid:0) (cid:1) (cid:0) (cid:1)

$$kd is p^{\gamma}k^{\gamma}^{2}^{Ω}^{k}kq$$

$$[N,H_{g}(t)]_{t}kN_{t}+mk+N^{−}_{t}.(S 6 4)$$

$$\langle \rangle \le 2 \langle \rangle 2 \gamma q \langle \rangle$$

(cid:18) (cid:19)q 1(cid:18) (cid:19)

$$(cid:12)(cid:12)X^{ \ge }$$

$$(cid:12)(cid:12)$$

Combining Eq. (S51) with Eqs. (S53, S61, S64), we obtain that

$$^{d}k^{\gamma}k^{k}kq$$

$$N_{t}kN_{t}+\lambda km N^{−}_{t},(S 6 5)$$

$$dt \langle \rangle \le − 2 \langle \rangle q \langle \rangle$$

$$q 1(cid:18)(cid:19)$$

$$X \ge$$

where $\lambda=\gamma$/2 + 2Ω /$\gamma$ + +2($\kappa 1$ + $\kappa 2$). Then, solving this inequality using Lemma 6, we obtain the lemma statement. CombiningthislemmawithLemma5,westraightforwardlyobtainthefollowinglemmaupperboundingtheprobability of large number of excitations at any time in the bosonic model. Lemma 9. Suppose $\Pi$ d is a projector on the subspace with d particles and the bosonic model satisﬁes assumptions

$$\ge \ge$$

1 and 2, then for any t 0, $\ge$

$$k^{0}1/\alpha$$

$$Tr(\Pi_{d}\rho(t))ee xp$$

$$^{ \ge } \le d_{0}m − d_{0}m$$

(cid:18) (cid:19) (cid:18) (cid:18) (cid:19) (cid:19) where d0 $=eC$, k0 $=\beta$/$\alpha$ with C,$\alpha$,$\beta$ being deﬁned in Lemma 8. B. Proof of Theorem 2 (bosons) The proof of Theorem 2 has three main parts: (1) Truncation of the Hilbert space of the bosonic model to a ﬁnite-dimensional space and an analysis of the truncation error (Lemma 11).

(2) First-order Trotterization of the truncated ﬁnite-dimensional model (Lemma 12). (3) Analysis of each Trotter step to establish high-noise separability (Lemma 13). Truncation of the bosonic model. Suppose we want to truncate the local Hilbert space of each bosonic mode to d levels—we will denote by d the Hilbert space of the bosonic model with each bosonic mode truncated to at most

$$th H \le$$

d particles. For the v bosonic mode, we will deﬁne the projectors $\Pi v$,d,$\Pi v$, d, and $\Pi v$,$>d$ via $\le$

$$\Pi v,d=dd,\Pi v,d=\Pi v,j,an d \Pi v,>d=\Pi v,j .$$

$$|\rangle \langle|^{ \le }$$

$$j=0 j=d+1$$

We will deﬁne the projector $\Pi$ $d^{=}v^{\Pi}v$, d, which will be the projector onto d. The truncated model will be

$$\le ⊗ \le H \le$$

described by a Lindbladian d(t) while

$$L \le$$

$$_{d}=i[H_{d},]+\kappa_{l}^{(}^{l}^{)},(S 6 7 a)$$

$$L \le − \le \cdot D^{L}^{v}^{,}^{ \le }^{d}$$

$$l=1 v$$

where

$$H_{d}(t)=\Pi_{d}H(t)\Pi_{d},$$

$$\le \le \le$$

$$^{L}_{v}_{,}_{d}^{=}^{a}v,d^{=}^{\Pi}v,d^{a}v^{\Pi}v,d^{,}$$

$$_{ \le } \le \le \le$$

$$L=a †=\Pi v,da †_{v}\Pi v,d,$$

$$v,dv,d$$

$$\le \le \le \le$$

$$^{L}^{=}^{n}v,d^{=}^{\Pi}v,d^{n}v^{\Pi}v,d^{.}$$

$$v,d$$

$$_{ \le } \le \le \le$$

It will be convenient to deﬁne super-operators d and d via

$$P \le Q \le$$

$$_{d}(\rho)=\Pi_{d}\rho \Pi_{d}an d_{d}=id_{d}.$$

$$P \le \le \le Q \le − P \le$$

The super-operator d projects an input density matrix onto d. We ﬁrst present a lemma that quanti-

$$P \le H \le$$

ﬁes the error between the state $\rho$(t) at time t and the state obtained from the truncated evolution: $\rho d$(t) $=$

$$t \le$$

$$ex p(_{d}(\tau)d \tau)(_{d}\rho(0)).$$

$$TL^{ \le }P^{ \le }$$

LemmRa 10. For any $d>0$, it follows that

$$\rho(t)ex p_{d}(\tau)d \tau(_{d}\rho(0))$$

$$− T_{0}L^{ \le }P^{ \le }$$

(cid:13) (cid:18)Z (cid:19) (cid:13)1

$$(cid:13)^{t}(cid:13)$$

$$(cid:13)(cid:13)$$

$$(cid:13)_{d}\rho(t)+(d+1)(cid:13)\Pi_{v}_{,}_{d}\rho(s)ds+_{d}(s)_{d}_{d}\rho(s)ds .$$

$$\le ∥ Q^{ \le }∥_{0}∥ ∥_{0}∥ P^{ \le }LQ^{ \le }∥_{⋄}∥ Q^{ \le }∥$$

$$^{v}ZZ$$

Proof. Using d+ $_{d}=i$d together with the master equation ($d \rho$(t)/$dt=$ (t)$\rho$(t)), we obtain that

$$P^{ \le }Q^{ \le }L$$

$$_{d}\rho(t)=_{d}(t)_{d}\rho(t)+_{d}(t)_{d}\rho(t),(S 6 9 a)$$

$$dt P^{ \le }P^{ \le }LP^{ \le }P^{ \le }LQ^{ \le }$$

$$_{d}\rho(t)=_{d}(t)_{d}\rho(t)+_{d}(t)_{d}\rho(t).(S 6 9 b)$$

$$dt Q^{ \le }Q^{ \le }LP^{ \le }Q^{ \le }LQ^{ \le }$$

Furthermore, we note that, for any operator X that is supported on the truncated subspace d (i.e. $X=\Pi$ $_{d}X \Pi$ d),

$$H \le \le$$

and deﬁning H d(t) $=\Pi$ dH(t)$\Pi$ d, we have

$$\le \le \le$$

$$_{d}_{d}(X)=i[H_{d}(t),X]+\Pi_{d}_{n}\Pi_{d}(X),(S 7 0)$$

$$P \le LP \le − \le \le L \le$$

$$da^{v}d^{(}^{X}^{)}^{=}^{\Pi}v,d^{a}v^{\Pi}v,d^{X}^{\Pi}v,d^{a}† v^{\Pi}v,d^{\Pi}v,d^{n}v^{\Pi}v,d^{X}^{+}^{X}^{\Pi}v,d^{n}v^{\Pi}v,d$$

$$P \le DP \le \le \le \le \le − 2 \le \le \le \le$$

$$(cid:0)(cid:1)$$

$$=av,dX a † a † av,dX+Xa † av,d$$

$$v,dv,dv,d$$

$$\le_{ \le }− 2_{ \le } \le_{ \le } \le$$

$$=_{a}(X),(cid:0)(cid:1)$$

$$v, \le d$$

$$d_{a}^{†}d^{(}^{X}^{)}^{=}^{\Pi}v,d^{a}† v^{\Pi}v,d^{X}^{\Pi}v,d^{a}v^{\Pi}v,d^{\Pi}v,d^{a}v^{a}† v^{\Pi}v,d^{X}^{+}^{X}^{\Pi}v,d^{a}v^{a}† v^{\Pi}v,d$$

$$P \le D^{v}P \le \le \le \le \le − 2 \le \le \le \le$$

$$(cid:0)d+1(cid:1)$$

$$=a † Xa_{v}_{,}_{d}a_{v}_{,}_{d}a † X+Xa_{v}_{,}_{d}a † \Pi v,dX+X \Pi v,d$$

$$v,dv,dv,d$$

$$\le \le − 2 \le \le \le \le − 2$$

d+(cid:0)1 (cid:1) (cid:0) (cid:1)

$$=^{†}(X)\Pi_{v}_{,}_{d}X+X \Pi_{v}_{,}_{d},(S 7 1 b)$$

$$Dv, \le d − 2$$

$$(cid:0)_{2}1(cid:1)_{2}$$

d nv d(X) $=\Pi_{v}$, $d^{n}v^{\Pi}v$, $dX \Pi v$, $d^{n}v^{\Pi}v$, d $\Pi v$, $d^{n}v^{\Pi}v$, dX+$X \Pi_{v}$, $d^{n}v^{\Pi}v$, d

$$P \le DP \le \le \le \le \le − 2 \le \le \le \le$$

$$^{2}(cid:0)(cid:1)$$

$$^{=}^{n}v,d^{X}^{n}v,d^{n}v,d^{X}^{+}^{X}^{n}v,d$$

$$\le \le − 2 \le \le$$

$$=_{n}(X).(cid:0)(cid:1)$$

$$v, \le d$$

Deﬁning n, $d=\kappa 1$ a +$\kappa 2^{†}$ +$\kappa 3$ n , we then obtain that, X d,

$$vv, \le da v, \le d$$

$$L^{ \le }DD^{v}^{,}^{ \le }^{d}D ∀ ∈ H^{ \le }$$

$$P(cid:0)(cid:1)$$

$$_{d}(t)_{d}(X)=_{d}(t)(X)\Pi_{v}_{,}_{d}X+X \Pi_{v}_{,}_{d}.(S 7 2)$$

$$P^{ \le }LP^{ \le }L^{ \le }− 2$$

$$X(cid:0)(cid:1)$$

Consequently, from Eq. (S69a), we obtain that

$$_{d}\rho(t)=_{d}(t)_{d}\rho(t)+_{d}(t)_{d}\rho(t)\Pi_{v}_{,}_{d}_{d}\rho(t)+(_{d}\rho(t))\Pi_{v}_{,}_{d},(S 7 3)$$

$$dt P^{ \le }L^{ \le }P^{ \le }P^{ \le }LQ^{ \le }− 2 P^{ \le }P^{ \le }$$

$$^{v}(cid:18)(cid:19)$$

which can be integrated to obtain

$$_{d}\rho(t)=_{d}(t,0)_{d}\rho(0)+_{d}(t,s)_{d}(s)_{d}\rho(s)\Pi_{v}_{,}_{d}_{d}\rho(s)+(_{d}\rho(s))\Pi_{v}_{,}_{d}ds,$$

$$P^{ \le }E^{ \le }P^{ \le }_{0}E^{ \le }P^{ \le }LQ^{ \le }− 2 P^{ \le }P^{ \le }$$

$$(cid:18)^{v}(cid:19)$$

$$^{X}^{(cid:0)}^{(cid:1)}(S 7 4)$$

where d(t,s) $=$ exp( d($\tau$)$d \tau$). From here, it immediately follows that

$$E^{ \le }TL^{ \le }$$

$$_{d}(t,0^{R})_{d}\rho(0)\rho(t)(S 7 5)$$

$$∥ E^{ \le }P^{ \le }− ∥$$

$$\rho_{d}(t)_{d}\rho(t)+_{d}\rho(t)$$

$$\le ∥^{ \le }− P^{ \le }∥ ∥ Q^{ \le }∥$$

$$(d+1)\Pi_{v}_{,}_{d}_{d}\rho(s)ds+_{d}(s)_{d}\rho(s)ds+_{d}\rho(t)$$

$$\le_{0}∥ P^{ \le }∥_{0}∥ P^{ \le }LQ^{ \le }∥ ∥ Q^{ \le }∥$$

$$^{v}ZZ$$

$$(d+1)\Pi_{v}_{,}_{d}\rho(s)ds+_{d}(s)_{d}\rho(s)ds+_{d}\rho(t).(S 7 6)$$

$$\le_{0}∥ ∥_{0}∥ P^{ \le }LQ^{ \le }∥ ∥ Q^{ \le }∥$$

$$^{v}ZZ$$

where, in (1), we have used the fact that $\Pi v$,$d \Pi$ $d=\Pi d \Pi v$,d to set $\Pi v$,d $d \rho$(s) $=\Pi_{d}\Pi_{v}$,$d \rho$(s)$\Pi$ d

$$^{ \le }^{ \le }∥ P^{ \le }∥ ∥^{ \le }^{ \le }∥ \le$$

$$\Pi_{d}\Pi_{v}_{,}_{d}\rho(s)\Pi_{d}=\Pi_{v}_{,}_{d}\rho(s),$$

$$∥^{ \le }∥ ∥ ∥ ∥^{ \le }∥ ∥ ∥$$

Finally, combining Lemma 10 with Lemmas 5 and 8, we obtain the next lemma quantifying the truncation error as a function of d. Lemma 11. For any d 1, it follows that $\ge$

$$1 1/\alpha$$

$$1 k^{0}/2 2+k^{0}/2(d/d^{0}m)$$

$$\rho(t)ex p_{d}(s)ds_{d}\rho(0)Om^{−}dt(J_{C}+J_{o}_{s}+U_{C}+U_{o}_{s}+\kappa)e^{−}^{2}$$

$$− T_{0}L^{ \le }P^{ \le } \le$$

(cid:13) (cid:18)Z (cid:19) (cid:13)1 (cid:13) (cid:13) (cid:0) (cid:1) where(cid:13)(cid:13)d0,k0,$\alpha$ are the constants in Lemma 9(cid:13)(cid:13).

Proof. We bound each term in Lemma 10. We ﬁrst note that

$$_{d}\rho(t)=\Pi_{>}_{d}\rho(t)+\Pi_{d}\rho(t)\Pi_{>}_{d}$$

$$∥ Q^{ \le }∥ ∥^{ \le }∥$$

$$\Pi_{>}_{d}\rho(t)+\Pi_{d}\rho(t)\Pi_{>}_{d}$$

$$\le ∥ ∥ ∥^{ \le }∥$$

$$Tr(\Pi_{>}_{d}\rho(t))+Tr(\Pi_{d}\rho(t))Tr(\Pi_{>}_{d}\rho(t))$$

$$\le \le$$

$$_{p}qk^{0}/2 1/\alpha$$

$$2 Tr(\Pi_{d}\rho(t))2 \sqrt ee xp$$

$$\le^{ \ge } \le d_{0}m − 2 d_{0}m$$

(cid:18) (cid:19) (cid:18) (cid:18) (cid:19) (cid:19) where, in (1), we have used the Holder’s inequality to conclude that $A \rho$(t)B Tr($A_{†}A \rho$(t))Tr($B_{†}B \rho$(t)). Fur-

$$∥ ∥ \le$$

thermore,

$$k^{0}/2 1/\alpha$$

$$\Pi_{v}_{,}_{d}\rho(t)Tr(\Pi_{v}_{,}_{d}\rho(t))Tr(\Pi_{d}\rho(t))\sqrt ee xp$$

$$∥ ∥ \le \le^{ \ge } \le d_{0}m − 2 d_{0}m$$

(cid:18) (cid:19) (cid:18) (cid:18) (cid:19) (cid:19) Finally, we consider upper-bounding d (s) d 1 d (s) d + d (s) 2 d (s) , where we

$$∥ P^{ \le }LQ^{ \le }∥ \le ∥ P^{ \le }LP^{ \le }∥^{⋄}∥ P^{ \le }L ∥^{⋄} \le ∥ P^{ \le }L ∥_{⋄}$$

have used the fact that d 1. Next, we note that, for a Hamiltonian H and jump operator L,

$$∥ P^{ \le }∥_{⋄} \le$$

$$_{d}[H,]2 \Pi_{d}Ha nd_{d}_{L}\Pi_{d}L+\Pi_{d}L^{†}L .$$

$$∥ P^{ \le }\cdot ∥_{⋄} \le ∥^{ \le }∥ ∥ P^{ \le }D ∥_{⋄} \le ∥^{ \le }∥ ∥^{ \le }∥$$

Furthermore, since $\Pi$ dav , $\Pi$ $da †_{v}^{\sqrt}d$+1, $\Pi$ da†vau d and $\Pi$ davau , $\Pi$ da†va†u d+2,

$$∥^{ \le }∥ ∥^{ \le }∥ \le ∥^{ \le }∥ \le ∥^{ \le }∥ ∥^{ \le }∥ \le$$

we obtain hop sq disp d[ ,H(t)] 2 $\Pi$ dHg (t) +2 $\Pi$ dHg (t) +2 $\Pi$ dHg (t) +2 $\Pi$ dHg (t)

$$∥ P^{ \le }\cdot ∥^{⋄} \le ∥^{ \le }∥^{⋄}∥^{ \le }∥^{⋄}∥^{ \le }∥^{⋄}∥^{ \le }∥$$

$$4 d_{v}_{,}_{u}+4(d+2)_{v}_{,}_{u}+4 \sqrt d+1_{v}_{,}_{u}(t)+4 d^{2}U_{v}_{,}_{u}$$

$$\le |J||G||D|||$$

$$v,uv,uv v,u$$

$$XX XX$$

$$4(d+1)m(J_{o}_{s}+J_{C})+2 2(d+1)Ω+4 d(U_{C}+U_{o}_{s})$$

$\le$

$$8 md(J_{o}_{s}+J_{C})+^{\sqrt}d Ω p+d^{2}(U_{C}+U_{o}_{s}.$$

$$\le ||$$

where we have used the decomposit(cid:0)ion of Hg(t) in Eq. (S25). Furthermo(cid:1)re,

$$dn^{\kappa}1 da_{v}^{+}^{\kappa}2 d_{a}^{†}^{+}^{\kappa}3 d_{a}^{†}_{a}$$

$$∥ P^{ \le }L ∥ \le ∥ P^{ \le }D ∥^{⋄}∥ P^{ \le }D^{v}∥^{⋄}∥ P^{ \le }D^{v}^{v}∥^{⋄}$$

$$^{v}(cid:18)(cid:19)$$

$$m \kappa_{1}(2 d+1)+\kappa_{2}(2 d+2)+\kappa_{3}d$$

$\le$

$$8 m_{(cid:0)}(\kappa_{1}+\kappa_{2})d+\kappa_{3}d ._{(cid:1)}$$

$\le$ Combining Eqs. (S81) and (S82), we obt(cid:0)ain that (cid:1)

$$_{d}(s)_{d}2_{d}(s)1 6 m(J_{o}_{s}+J_{C}+(\kappa_{1}+\kappa_{2}))d+Ω^{\sqrt}d+(U_{C}+U_{o}_{s}+\kappa_{3})d^{2}$$

$$∥ P^{ \le }LQ^{ \le }∥^{⋄} \le ∥ P^{ \le }L ∥^{⋄} \le$$

16m(cid:0)d Jos+JC +Ω+Uos+UC +$\kappa$ . (cid:1) (S83) $\le$ Finally, combining Eqs. (S77, S78, S83) together with(cid:0)Lemmas 10 and 9, we obtain(cid:1)the lemma. Trotterization of the truncated model. We will perform a ﬁrst-order Trotterization of the state $\rho d$(t) $=$

$$t \le$$

exp( d(s)ds) d($\rho$(0)). We will split the Hamiltonian H d(t) into a sum of inter-site terms H (t) and a

$$TL \le P \le \le \le$$

sum of on-site terms H (t):

$$R \le$$

C os

$$H_{d}(t)=h_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(t)+h_{i}_{;}_{\sigma}_{,}_{\sigma}^{′}(t),(S 8 4)$$

$\le$

$$i<j \sigma,\sigma^{′}i \sigma,\sigma^{′}$$

$$XX XX$$

$$H^{C}(t)H^{o}^{s}(t)$$

$$\le d \le d$$

$$|\{z \}|\{z \}$$

where, in hi,$\sigma$;j,$\sigma ′$(t) we include all the terms that mediate an interaction between (i,$\sigma$) and (j,$\sigma ′$):

$$C \alpha,\alpha \alpha \alpha$$

$$h_{i}_{,}_{\sigma}_{;}_{j}^{′}(t)=\Pi_{d}U_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(t)n_{i}_{,}_{\sigma}n_{j}_{,}_{\sigma}^{′}+J^{′}(t)c_{i}_{,}_{\sigma}c_{j}_{,}_{\sigma}^{′}\Pi_{d}+(i,\sigma)(j,\sigma ′)$$

$$,\sigma i,\sigma;j,\sigma$$

$$\le \le \le ftrightarrow$$

$$(cid:18)\alpha,\alpha^{′}(cid:19)$$

$$^{=}^{2}^{U}i,\sigma;j,\sigma^{′}^{(}^{t}^{)}^{n}i,\sigma;d^{n}j,\sigma^{′};d^{+}^{2}^{J}i,\sigma;j^{′},\sigma^{′}^{(}^{t}^{)}^{c}^{c}^{′}^{,}$$

$$i,\sigma;dj,\sigma;d$$

$$\le \le \le \le$$

$$\alpha,\alpha^{′}$$

$$1_{\sqrt}2_{\sqrt}os$$

wherec $=$ (ai,$\sigma$; d+a† )/ 2, c $=$ (ai,$\sigma$; d a† )/ 2i. In hi;$\sigma$,$\sigma ′$(t), weincludealltheterms(Gaussian

$$i,\sigma;di,\sigma;di,\sigma;di,\sigma;d$$

$$\le \le \le \le \le − \le$$

or non-Gaussian) that act between modes (i,$\sigma$) and (i,$\sigma ′$):

$$os \alpha,\alpha \alpha \alpha$$

$$h_{;}^{′}(t)=\Pi_{d}U_{i}_{,}_{\sigma}_{;}_{i}_{,}_{\sigma}^{′}(t)n_{i}_{,}_{\sigma}n_{i}_{,}_{\sigma}^{′}+J^{′}(t)cc^{′}\Pi_{d}$$

$$i \sigma,\sigma i,\sigma;i,\sigma i,\sigma i,\sigma$$

$$\le \le$$

$$(cid:18)\alpha,\alpha^{′}(cid:19)$$

$$\alpha,\alpha \alpha \alpha$$

$$^{=}^{U}i,\sigma;i,\sigma^{′}^{(}^{t}^{)}^{n}i,\sigma;d^{n}i,\sigma^{′};d^{+}^{J}i,\sigma;i^{′},\sigma^{′}^{(}^{t}^{)}^{\Pi}i,\sigma;d^{\Pi}i,\sigma^{′};d^{c}i,\sigma^{c}i^{′},\sigma^{′}^{\Pi}i,\sigma;d^{\Pi}i,\sigma^{′};d^{.}$$

$$\le \le \le \le \le \le$$

$$\alpha,\alpha^{′}$$

Furthermore, we will also decompose the dissipation n, d:

$$L \le$$

$$nn(l)(l)$$

$$_{n}_{,}_{d}=_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(t)wh er e_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(t)=\kappa_{l}p_{′}(t)^{(}^{l}^{)}+q_{′}(t)^{(}^{l}^{)},(S 8 7)$$

$$i,\sigma;j,\sigma Li,\sigma;j,\sigma L$$

$$L \le LL Di,\sigma, \le dD j,\sigma ′, \le d$$

$$i<j \sigma,\sigma^{′}l=1$$

$$X(cid:0)(cid:1)$$

$$(l)(l)$$

where we will choose p ′ ′(t),q ′ ′(t) 0 later. For this decomposition of n, d to be consistent, we must also

$$i,\sigma;i,\sigma i,\sigma;i,\sigma$$

$$\ge L^{ \le }$$

have

$$(l)(l)$$

$$k,\sigma:p_{′}_{′}(t)+q_{′}_{′}(t)=1 .(S 8 8)$$

$$k,\sigma;k,\sigma k,\sigma;k,\sigma$$

$$k^{′}>k \sigma^{′}k^{′}<k \sigma^{′}$$

$$XX XX$$

Now, the state of the truncated model at time t, $\rho d$(t), will be approximated by the state $\sigma T$, d, where T is the

$$\le \le$$

number of Trotter steps and

$$i,\sigma;j,\sigma os$$

$$\sigma_{T}_{,}_{d}=\Phi_{\tau}_{\delta}_{,}_{(}_{\tau}_{1}_{)}_{\delta}\rho_{d}(0),(S 8 9 a)$$

$$\le_{−}U − \le$$

$$\tau=T(cid:18)i<j \sigma,\sigma^{′}(cid:19)$$

$$YY Y$$

$$wh er e \delta=t/T,$$

$$i,\sigma;j,\sigma CC Cn$$

$$^{\Phi}^{′}^{=}^{e}^{x}^{p}_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}^{(}^{s}^{)}^{d}^{s}^{w}^{h}^{e}^{r}^{e}_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}^{(}^{s}^{)}^{=}^{i}^{[}^{h}_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}^{(}^{s}^{)}^{,}^{]}^{+}_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}^{(}^{s}^{)}^{,}$$

t,t

$$T_{t}^{′}LL − \cdot L$$

$$(cid:18)Z(cid:19)$$

and os os os os os

$$\tau \delta,(\tau 1)\delta^{=}^{U}\tau \delta,(\tau 1)\delta^{(}^{)}^{U}†^{w}^{h}^{e}^{r}^{e}^{U}\tau \delta,(\tau 1)\delta^{=}^{e}^{x}^{p}^{i}^{H}^{(}^{s}^{)}^{d}^{s}^{.}$$

$$U − − \cdot − − T −(\tau 1)\delta$$

$$(cid:18)Z^{−}(cid:19)$$

The next lemma provides an upper bound on the Trotter error $\rho d$(t) $\sigma T$, d .

$$∥^{ \le }−^{ \le }∥$$

Lemma 12. For any $T>0$ and d 1: $\ge$

$$\sigma_{T}_{,}_{d}\rho_{d}(t).$$

$$∥^{ \le }−^{ \le }∥ \le T$$

Proof. This lemma follows from an application of Lemma 2: We note that

$$CC(l)(l)2(l)(l)2$$

$$_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)2 h_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)+2 \kappa_{l}p_{′}(s)L+q_{′}(s)L_{′}$$

$$i,\sigma;j,\sigma i,\sigma,di,\sigma;j,\sigma j,\sigma,d$$

$$∥ L ∥^{⋄} \le ∥ ∥ ∥^{ \le }∥ ∥^{ \le }∥$$

$$l=1$$

$$X(cid:0)(cid:1)$$

$$(1)′$$

$$\alpha,\alpha(l)(l)2$$

$$4 U_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)+8 J_{′}(s)+2 \kappa_{l}(p_{′}(s)+q_{′}(s))d,(S 9 0)$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$\le ||||$$

$$(cid:18)\alpha,\alpha^{′}l=1(cid:19)$$

os os

$$[,H(t)]2 h_{i}_{;}_{\sigma}_{,}_{\sigma}^{′}(t)$$

$$∥ \cdot ∥^{⋄} \le ∥ ∥$$

$$i,\sigma,\sigma^{′}$$

$$(2)′$$

$$\alpha,\alpha 2$$

$$2 U_{i}_{,}_{\sigma}_{;}_{i}_{,}_{\sigma}^{′}(s)+4 J_{′}(s)d,(S 9 1)$$

$$i,\sigma;i,\sigma$$

$$\le ||||$$

$$(cid:18)i,\sigma,\sigma^{′}i,\sigma,\sigma^{′}\alpha,\alpha^{′}(cid:19)$$

$$XX X$$

where, in (1) and (2), we have used the fact that, for the truncated bosonic model, $c^{\alpha}\sqrt 2$d $\sqrt 2$d, ni,$\sigma$, d

$$i,\sigma,d$$

$$∥^{ \le }∥ \le \le ∥^{ \le }∥ \le$$

d, L , L $\sqrt d$ d and L d. We can now estimate the parameter ℓ from Lemma 2: ℓ would

$$i,\sigma,di,\sigma,di,\sigma,d$$

$$∥^{ \le }∥ ∥^{ \le }∥ \le \le ∥^{ \le }∥ \le$$

be an upper bound on os C

$$[,H(s)]+_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)$$

$∥ \cdot ∥^{⋄}∥ L ∥^{⋄}$

$$j,i<j \sigma,\sigma^{′}$$

$$\alpha,\alpha(l)(l)2$$

$$4 U_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)+J_{′}+2 \kappa_{l}(p_{′}(s)+q_{′}(s))d$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$\le ||||$$

(cid:18) i,$j \sigma$,$\sigma ′$(cid:18) $\alpha$,$\alpha ′$ (cid:19) i,j:$i<j \sigma$,$\sigma^{′}l=1$ (cid:19) XXX

$$4(U_{C}+U_{o}_{s}+J_{C}+J_{o}_{s}+\kappa)md .$$

$\le$ Thus, from Lemm|a 2, we obtain{tzhat $\sigma T$, d $\rho$} d(t) 16t2m2d2(UC +Uos +JC +Jos +$\kappa$)2/T.

$$∥^{ \le }−^{ \le }∥ \le$$

Lemma 13 (Separabilityconditionforthebosonicmodel). Consider the following Lindbladian d(t) on two bosonic

$$L \le$$

modes truncated to d 1 particles each: $\ge$

$$(l)$$

$$_{d}(t)=i[h_{g}_{,}_{d}(t)+h_{n}_{g}_{,}_{d}(t),]+\kappa(t)^{(}^{l}^{)},$$

$$L \le − \le \le \cdot D^{i}^{,}^{ \le }^{d}$$

$$i 1,2 l=1$$

$$∈ X \{\}X$$

where

$$\alpha \beta(1)(2)(3)$$

$$h_{g}_{,}_{d}(t)=g_{\alpha}_{,}_{\beta}(t)c_{1}_{,}_{d}c,h_{n}_{g}_{,}_{d}(t)=u(t)n_{1}_{,}_{d}n_{2}_{,}_{d},L=a_{i}_{,}_{d},L=a^{†}an dL=n_{i}_{,}_{d},$$

$$2,di ii,di$$

$$\le \le_{ \le } \le \le \le \le_{ \le } \le$$

$$\alpha,\beta 1,2$$

$$X ∈ \{\}$$

where c $=$ (a d +a† )/$\sqrt 2$, c $=$ (a d a† )/$\sqrt 2$i and $g \alpha$,$\beta$(t),u(t) are real and $\kappa$ (t) 0. If

$$i,dd i,dd i$$

$$\le \le \le \le \le − \le \ge$$

$$(C 1)\kappa(t),\kappa(t)g_{\alpha}_{,}_{\beta}(t)an d$$

$$ii \alpha,\beta$$

$$\ge ||$$

$$(C 2)\kappa(t)u(t),$$

$$\ge ||$$

then there is a completely-positive map t+$\tau$,t which maps separable states to separable states and

$$t+\tau t+\tau t+\tau 3 t+\tau 2$$

$$_{t}_{+}_{\tau}_{,}_{t}ex p_{d}(s)ds 8 dg_{\alpha}_{,}_{\beta}(s)ds+u(s)ds+\kappa(s)ds .$$

$$M − T_{t}L^{ \le } \le_{t}||_{t}||_{t}$$

(cid:13) (cid:18)Z (cid:19)(cid:13)⋄ (cid:18) $\alpha$,$\beta Z$ Z $l=1$ i 1,2 Z (cid:19)

$$(cid:13)(cid:13)XX^{∈}X^{\{}^{\}}$$

$$(cid:13)(cid:13)$$

P(cid:13)roof. It will be notationally conveni(cid:13)ent to deﬁne the scalars

$$t+\tau t+\tau t+\tau$$

$$(l)(l)$$

$$G_{\alpha}_{,}_{\beta}=g_{\alpha}_{,}_{\beta}(s)ds,K=\kappa(s)ds,U=u(s)ds an d$$

$$tt t$$

$$ZZ Z$$

$$(l)(l)(l)(l)$$

$$G_{0}=g_{\alpha}_{,}_{\beta}(s)ds,U_{0}=u(s)ds,K_{i}=K,K=K,K=K .(S 9 3)$$

$$_{t}||_{t}||$$

$$\alpha,\beta ZZ l=1 i 1,2 l=1$$

$$XX^{∈}X^{\{}^{\}}X$$

We will deﬁne the completely positive map t+$\tau$,t via

$$_{t}_{+}_{\tau}_{,}_{t}(\rho)=^{E}_{z}R_{1}(z)R_{2}(z)\rho R_{2}^{†}(z)R_{1}^{†}(z),(S 9 4 a)$$

$$wi th^{(cid:2)}^{(cid:3)}$$

$$i \pi/4 \alpha i \pi/4 \beta$$

$$R_{1}(z)=Q_{1}+e^{−}z_{\alpha}_{,}_{\beta}G_{\alpha}_{,}_{\beta}c_{1}_{,}_{d},R_{2}(z)=Q_{2}+e^{−}z_{\alpha}^{∗}_{,}_{\beta}G_{\alpha}_{,}_{\beta}c,(S 9 4 b)$$

$$\le \le$$

$$\alpha,\beta \alpha,\beta$$

$$Xp Xp$$

where $z \alpha$,$\beta$ aredrawnindependentlyanduniformlyatrandomfromtheset 1, i and $Q_{i}=e$xp( (K a† ai, d+ i i, d

$$\{\pm \pm \}−^{ \le }^{ \le }$$

K ai, da† )/2). It can be noted that, by construction, t+$\tau$,t maps a separable input state to a separable (but i i, d

$$\le_{ \le }R$$

possibly unnormalized) output state. Explicitly evaluating the expectation value in Eq. (S94), we obtain that

$$\alpha \beta \alpha \beta$$

$$_{t}_{+}_{\tau}_{,}_{t}(\rho)=Q_{1}Q_{2}\rho Q † Q † iG_{\alpha}_{,}_{\beta}c_{1}_{,}_{d}c \rho Q † Q † Q_{1}Q_{2}\rho c_{1}_{,}_{d}c+$$

$$R − \le \le − \le \le$$

$$\alpha,\beta$$

$$X(cid:0)(cid:1)$$

$$\alpha \alpha \beta \beta$$

$$G_{\alpha}_{,}_{\beta}c_{1}_{,}_{d}Q_{2}\rho Q † c_{1}_{,}_{d}+Q_{1}c \rho cQ †+$$

$$|| \le \le \le \le$$

$$\alpha,\beta$$

$$(cid:0)(cid:1)$$

$$′ ′ ′ ′$$

$$\alpha \beta \beta \alpha \alpha \beta \beta \alpha$$

$$G_{\alpha}_{,}_{\beta}G_{\alpha}^{′}_{,}_{\beta}^{′}cc \rho cc+G_{\alpha}_{,}_{\beta}G_{\alpha}^{′}_{,}_{\beta}^{′}cc \rho cc$$

$$1,d 2,d 2,d 1,d 1,d 2,d 2,d 1,d$$

$$\le \le \le \le |||| \le \le \le \le$$

$$\alpha,\alpha^{′},\beta,\beta^{′}(cid:18)(cid:19)$$

$$t+\delta$$

$$\alpha \alpha \beta \beta$$

$$=\rho ih_{g}_{,}_{d}(s)ds,\rho+G_{\alpha}_{,}_{\beta}c_{1}_{,}_{d}\rho c_{1}_{,}_{d}+c \rho c$$

$$− \le || \le \le_{ \le }_{ \le }−$$

$$(cid:20)Z(cid:21)\alpha,\beta$$

$$(cid:0)(cid:1)$$

$$Ka^{†}a_{i}_{,}_{d}+Ka_{i}_{,}_{d}a^{†},\rho+∆_{t}_{+}_{\tau}_{,}_{t}(\rho),(S 9 5)$$

$$ii,di i,d$$

$$2 \{_{ \le } \le \le_{ \le }\}$$

$$∈ X \{\}$$

where, using the fact that

$$∥ ∥ \le$$

$$Q_{i}I(Ka_{1}_{,}_{d}+Ka_{2}_{,}_{d})(K+K),$$

$$ii ii$$

$$∥ − ∥ \le 2 ∥^{ \le }∥ ∥^{ \le }∥ \le 2$$

$$^{1}(1)(2)^{1}(1)2(2)2 2^{d}(1)(2)2$$

$$Q_{i}I(Ka^{†}a_{i}_{,}_{d}+Ka_{i}_{,}_{d}a^{†})(Ka_{i}_{,}_{d}+Ka_{i}_{,}_{d})(K+K),$$

$$ii,di i,di ii i$$

$$− − 2^{ \le }^{ \le }^{ \le }^{ \le } \le 8 ∥^{ \le }∥ ∥^{ \le }∥ \le 8$$

(cid:13) (cid:18) (cid:19)(cid:13) (cid:13)(cid:13)$c^{\alpha}_{i}$, d $\sqrt 2$ ai, d $\sqrt 2$d, (cid:13)(cid:13)

$$(cid:13)^{ \le } \le ∥^{ \le }∥ \le (cid:13)$$

it fol(cid:13)lows t(cid:13)hat

$$(cid:13)(cid:13)$$

$$∆_{t}_{+}_{\tau}_{,}_{t}(K+K)+4 dG(K+K)+8 dG .(S 9 7)$$

$$∥ ∥_{⋄} \le 2$$

Similarly, we also deﬁne the completely positive map ˜t+$\tau$,t:

$$^{˜}_{t}_{+}_{\tau}_{,}_{t}(\rho)=^{E}_{y}R^{˜}_{1}(y)R^{˜}_{2}(y)\rho R^{˜}_{2}^{†}(y)R^{˜}_{1}^{†}(y),(S 9 8 a)$$

$$wi th(cid:2)(cid:3)$$

$$˜ ˜ i \pi/4_{\sqrt}˜ ˜ i \pi/4_{\sqrt}$$

$$R_{1}(y)=Q_{1}+ye^{−}Un_{1}_{,}_{d}an dR_{2}(y)=Q_{2}+y^{∗}e^{−}Un_{2}_{,}_{d},$$

$$\le \le$$

$$˜^{K}^{i}2 ˜$$

where y is drawn randomly from 1,1,i, i and $Q_{i}=$ exp( n ). Similar to t+$\tau$,t, t+$\tau$,t also maps a

$$\{− − \}−^{ \le }RR$$

separable input state to a separable but possibly unnormalized output state. By explicitly evaluating the expectation in Eq. (S98), we ﬁnd that

$$^{˜}_{t}_{+}_{\tau}_{,}_{t}(\rho)=Q^{˜}_{1}Q^{˜}_{2}\rho Q^{˜}^{†}_{2}Q^{˜}^{†}_{1}iU(n_{1}_{,}_{d}n_{2}_{,}_{d}\rho Q^{˜}^{†}_{1}Q^{˜}^{†}_{2}Q^{˜}_{1}Q^{˜}_{2}\rho n_{1}_{,}_{d}n_{2}_{,}_{d})+$$

$$R − \le \le − \le \le$$

$$^{U}^{n}1,d^{Q}^{˜}2^{\rho}^{Q}^{˜}† 2^{n}1,d^{+}^{Q}^{˜}1^{n}2,d^{\rho}^{n}2,d^{Q}^{˜}† 1^{+}^{U}^{2}^{n}1,d^{n}2,d^{\rho}^{n}2,d^{n}1,d$$

$$|| \le \le \le \le || \le \le \le \le$$

$$t+\delta$$

$$(cid:0)(cid:1)$$

$$=\rho ih_{n}_{g}_{,}_{d}(s)ds,\rho+Un_{1}_{,}_{d}\rho n_{1}_{,}_{d}+n_{2}_{,}_{d}\rho n_{2}_{,}_{d}K_{3}n_{1}_{,}_{d}+n_{2}_{,}_{d},\rho+∆_{t}_{+}_{\tau}_{,}_{t}(\rho),$$

$$−_{t} \le || \le \le \le \le − 2 \{ \le \le \}$$

$$(cid:20)Z(cid:21)$$

$$(cid:0)(cid:1)$$

$$_{˜}_{˜}(3)2(3)_{2}_{˜}K_{2}$$

where, using the fact that Qi 1, Qi I K ni, d /2 K d /2, Qi (I i ni)

$$_{(}_{3}_{)}_{(}_{3}_{)}∥ ∥ \le ∥ − ∥ \le ∥^{ \le }∥ \le ∥ − − ∥ \le$$

(K ni, d ) /8 (K ) d /8 and ni, d d, it follows that

$$∥^{ \le }∥ \le ∥^{ \le }∥ \le$$

$$˜^{1}(3)2 4 2 4(3)4$$

$$∆_{t}_{+}_{\tau}_{,}_{t}(K)d+U_{0}d+2 U_{0}Kd .(S 1 0 0)$$

$$∥ ∥^{⋄} \le 2$$

Finally, we consider the channel generated by the fermionic Lindbladian in the time interval (t,t+$\tau$): Performing a ﬁrst-order Taylor expansion, we obtain that

$$t+\tau t+\tau$$

$$ex p(s)ds \rho=\rho+(s)\rho ds+∆^{E}_{t}_{+}_{\tau}_{,}_{t}(\rho),$$

$$T_{t}L_{t}L$$

$$(cid:18)Z(cid:19)$$

where ∆Et+$\tau$,t 8d (G+U +K) . From Eqs. (S95, S99, S101), we then obtain that

$$∥ ∥^{⋄} \le$$

$$t+\tau$$

$$ex p(s)ds=_{t}_{+}_{\tau}_{,}_{t}+E_{t}_{+}_{\tau}_{,}_{t},$$

$$T_{t}LM$$

$$(cid:18)Z(cid:19)$$

where

$$t+\tau,t^{=}t+\tau,t^{+}^{˜}t+\tau,t^{+}$$

M R R

$$(1)(2)\alpha \alpha \beta \beta$$

$$Ka i,da †+Ka † ai,dG \alpha,\beta c_{1}_{,}_{d}c_{1}_{,}_{d}+cc+$$

$$ii,di i,d 2,d 2,d$$

$$\le \cdot_{ \le }_{ \le }\cdot \le −|| \le \cdot \le_{ \le }\cdot_{ \le }$$

$$i 1,2 \alpha,\beta$$

∈X{ }(cid:0) (cid:1) X (cid:0) (cid:1)

$$t+\tau,t$$

$$|(KU)n_{i}_{,}_{d}\rho n_{i}_{,}_{d},\{z \}(S 1 0 3)$$

$$−||^{ \le }^{ \le }$$

$$∈ X \{\}$$

$$t+\tau,t$$

$$^{E}t+\tau,t^{=}^{∆}Et^{|}+\tau,t^{∆}t+\tau,t^{\{}^{z}^{∆}^{˜}t+\tau,t^{.}^{\}}^{(}^{S}^{1}^{0}^{4}^{)}$$

We note that t+$\tau$,t is a channel that preserves separability as long as t+$\tau$,t and ˜t+$\tau$,t are completely positive. The complete positivity of ˜t+$\tau$,t is ensured by requiring K U which is implied by the condition C2 quoted in the

$$V \ge ||$$

lemma statement. To ensure that t+$\tau$,t is completely positive, we note that it can be re-written as

$$(i)(i)(i)(i)$$

$$_{t}_{+}_{\tau}_{,}_{t}=F_{0}_{0}a_{i}_{,}_{d}a †+Fa_{i}_{,}_{d}a_{i}_{,}_{d}+Fa † a_{i}_{,}_{d}+Fa † a †,(S 1 0 5)$$

$$,i,d 0,1 1,0 i,d 1,1 i,di,d$$

$$V \le \cdot_{ \le } \le \cdot \le_{ \le }\cdot \le_{ \le }\cdot_{ \le }$$

$$i 1,2(cid:18)(cid:19)$$

$$∈ X \{\}$$

where

$$(1)^{K}1_{2}^{G}_{2}\beta^{G}2,\beta^{G}1,\beta(2)^{K}2_{2}^{G}_{2}\alpha^{G}\alpha,2^{G}\alpha,1$$

$$F=−|_{(}_{2}_{)}|−||,F=−|_{(}_{2}_{)}|−||.$$

$$"_{2}_{\beta}^{G}2,\beta^{G}1,\beta_{(cid:0)}^{K}1_{2}^{G}_{(cid:1)}\# "_{2}\beta^{G}\alpha,2^{G}\alpha,1^{K}2_{2}^{G}\#$$

$$||−||^{P}−||−||P^{(cid:0)}−^{(cid:1)}$$

P (cid:0) (cid:1) P (cid:0) (cid:1) As long as F ,F are positive-semideﬁnite, it would follow that t+$\tau$,t is completely positive. Now, it is easy to see that a suﬃcient condition for F 0 is that K ,K G, which is implied by the condition C1 quoted in the

$$⪰ \ge$$

lemma statement. Finally, the error term Et+$\tau$,t can be bounded by ˜ 4 2

$$Et+\tau,t ∆ E_{t}_{+}_{\tau}_{,}_{t}+∆ t+\tau,t+∆ t+\tau,t 8 d(G+U 0+K),(S 1 0 7)$$

$$∥ ∥^{⋄} \le ∥ ∥^{⋄}∥ ∥^{⋄}∥ ∥^{⋄} \le$$

which establishes the error bound in the lemma statement. Theorem 2 (High-noise seperability and classical simulation of bosonic model; reproduced from the main text). Suppose $\rho$(t) is the state obtained after evolving the bosonic system for time t with an initial product state, then for min($\kappa 1$,$\kappa 2$) 2J the state $\rho$(t) is separable. Furthermore, there is a randomized classical algorithm that can sample

$$^{ \ge }2 2 4 L+8 1$$

within $\epsilon$ total variation error of $\rho$(t) in O($\Lambda$ t m $\epsilon −$ polylog $m \Lambda t$/$\epsilon$)) time. Proof. To prove Theorem 2, we will start with truncated ﬁrst-o(cid:0)rder Trotter approximation of $\rho$(t), i.e. with $\sigma T$, d $\le$ given in Eq. (S89). From Lemmas 11 and 12, we obtain that

$$\Lambda tm d^{1}^{1}^{/}^{\alpha}$$

$$1 k^{0}/2 2+k^{0}/2(d/d^{0}m)$$

$$\rho(t)\sigma_{T}_{,}_{d}O+O \Lambda tm^{−}de^{−}^{2},(S 1 0 8)$$

$$∥ −^{ \le }∥ \le T$$

$$(cid:18)(cid:19)$$

$$(cid:0)(cid:1)$$

where $\Lambda=U_{C}$ +Uos+JC +Jos+$\kappa$. Next, we use Lemma 13 to further approximate $\sigma T$, d with a separable state $\le$ $\phi T$. However, the noise rates at each step in the Trotterization need to be suﬃciently high to meet the necessary conditions for separability [(C1) and (C2) provided in Lemma 13]—to ensure this, we make a choice of the parameters

$$(l)(l)$$

p ′(t),q ′(t) in Eq. (S87) that we so far left unspeciﬁed:

$$i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$\alpha,\alpha$$

$$(1)(2)\alpha,\alpha^{′}^{J}i,\sigma;j,\sigma^{′}^{(}^{t}^{)}(3)^{U}i,\sigma;j,\sigma^{′}^{(}^{t}^{)}$$

$$p_{′}(t)=p_{′}(t)=|_{′}|,p_{′}(t)=||,$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma \alpha,\alpha i,\sigma;j,\sigma$$

$$_{P}^{′}J(t)k=i \nu^{U}i,\sigma;k,\nu^{(}^{t}^{)}$$

$$k=i \nu \alpha,\alpha i,\sigma;k,\nu_{|}_{|}$$

$$_{̸}||̸$$

$$\alpha,\alpha$$

$$^{P}^{P}\alpha,\alpha^{P}^{′}^{J}i,\sigma;j,\sigma^{′}^{(}^{t}^{)}(3)^{P}^{P}^{U}i,\sigma;j,\sigma^{′}^{(}^{t}^{)}$$

$$q_{′}(t)=q_{′}(t)=|_{′}|,q_{′}(t)=||,(S 1 0 9 a)$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma \alpha,\alpha i,\sigma;j,\sigma$$

$$_{P}^{′}J^{′}(t)k=i \nu^{U}j,\sigma^{′};k,\nu^{(}^{t}^{)}$$

$$k=i \nu \alpha,\alpha j,\sigma;k,\nu_{|}_{|}$$

$$_{̸}||̸$$

$$PP PP P$$

and it can be checked that they satisfy the normalization condition in Eq. (S88). Considering now the channels

$$i,\sigma;j,\sigma$$

from Eq. (S89) in Trotterized state $\sigma T$, d—to apply Lemma 13 to these channels, we need

$$− \le$$

(1) Imposing condition C1: For l 1,2

$$∈ \{\}$$

$$(l)(l)\alpha,\alpha$$

$$\kappa_{l}p_{′}(t),\kappa_{l}q_{′}(t)2 J_{′}(t)or eq ui va le nt ly$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$\ge ||$$

$$\alpha,\alpha^{′}$$

$$\alpha,\alpha$$

$$\kappa_{l}2 J_{′}_{′}(t)fo r(k,\nu)(i,\sigma),(j,\sigma^{′}).$$

$$k,\nu;k,\nu$$

$$\ge ||∈ \{\}$$

$$k^{′}=k \nu^{′}\alpha,\alpha^{′}$$

$$X^{̸}XX$$

$$\alpha,\alpha$$

This condition can clearly be satisﬁed if $\kappa 1$,$\kappa 2$ 2JC since ′ ′ ′ J ′ ′(t) JC.

$$k=k \nu \alpha,\alpha k,\nu;k,\nu$$

$$\ge^{̸}|| \le$$

(2) Imposing condition C2: P P P

$$\kappa_{3}p_{′}(t),\kappa_{3}q_{′}(t)2 U_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(t)or eq ui va le nt ly$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$\ge ||$$

$$\kappa_{3}2 U_{k}_{,}_{\nu}_{;}_{k}^{′}_{,}_{\nu}^{′}(t)fo r(k,\nu)(i,\sigma),(j,\sigma^{′}).$$

$$\ge ||∈ \{\}$$

$$k^{′}=k \nu^{′}$$

$$X^{̸}X$$

This condition can clearly be satisﬁed if $\kappa 3$ 2UC since ′ ′ Uk,$\nu$;k′,$\nu ′$(t) UC.

$$k=k \nu$$

$$\ge^{̸}|| \le$$

Now, assuming $\kappa 1$,$\kappa 2$ 2JC and $\kappa 3$ 2UC, we can then approPximate$P \sigma^{T}$, d by $\phi T$ given by

$$\ge \ge^{ \le }$$

$$i,\sigma;j,\sigma os$$

$$\phi_{T}=_{\tau}_{\delta}_{,}_{(}_{\tau}_{1}_{)}_{\delta}\rho(0),(S 1 0 9 f)$$

$$M − U −$$

$$\tau=N(cid:18)i<j \sigma,\sigma^{′}(cid:19)$$

$$YY Y$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma$$

where is the separability preserving completely-positive map corresponding to $\Phi$ from Lemma 13,

$$\tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta$$

$$^{M}− −$$

which also satisﬁes

$$′ ′ ′$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$\Phi \epsilon_{\tau},(S 1 0 9 g)$$

$$\tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta$$

$$∥_{−}− M_{−}∥^{⋄} \le$$

where

$$i,\sigma;j,\sigma^{′}4 \alpha,\alpha^{′}(l)(l)$$

$$\epsilon_{\tau}=8 dJ_{′}(s)ds+U_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)ds+\kappa_{l}p_{′}(s)+q_{′}(s)ds .(S 1 0 9 h)$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$(\tau 1)\delta^{′}^{|}^{|}^{|}^{|}$$

(cid:18)Z − (cid:18)$\alpha$,$\alpha l=1$ (cid:19) (cid:19)

$$X(cid:0)(cid:1)$$

We note that $\epsilon$ is deﬁned by

$$i,\sigma;j,\sigma$$

$$\epsilon=\epsilon_{\tau}$$

$$\tau=1 i,j:i<j \sigma,\sigma^{′}$$

XXX

$$4 \alpha,\alpha(l)(l)$$

$$8 dJ_{′}(s)ds+U_{i}_{,}_{\sigma}_{;}_{j}_{,}_{\sigma}^{′}(s)ds+\kappa_{l}p_{′}(s)+q_{′}(s)ds$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$^{ \le }(\tau 1)\delta^{′}^{|}^{|}^{|}^{|}$$

$\tau=1$(cid:18)Z − i,j;$i<j$(cid:18)$\alpha$,$\alpha l=1$ (cid:19) (cid:19)

$$X(cid:0)(cid:1)$$

4 2t m $_{4}^{\Lambda}$ t m

$$8 dJ_{C}+U_{C}+2 \kappa 3 2 d .(S 1 1 0)$$

$$\le T \le T$$

$$(cid:0)(cid:1)$$

Furthermore, we also note from the triangle inequality that

$$′ ′ ′ ′ ′ ′$$

$$i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma i,\sigma;j,\sigma$$

$$1+\epsilon_{\tau}ex p(\epsilon_{\tau}).$$

$$\tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta$$

$$∥ M_{−}∥^{⋄} \le ∥_{−}∥^{⋄}∥ M_{−}−_{−}∥^{⋄} \le \le$$

We can now bound the error between $\phi T$ and $\sigma T$, d using telescoping to obtain $\le$

$$\epsilon O(\Lambda tm d/T)$$

$$\phi_{T}\sigma_{T}_{,}_{d}e \epsilon eO .(S 1 1 2)$$

$$∥ −^{ \le }∥ \le \le T$$

$$(cid:18)(cid:19)$$

Finally, using Eq. (S108), we obtain that

$$^{2}^{2}^{2}^{4}\Lambda tm d \Lambda tm d^{1}^{1}^{/}^{\alpha}$$

$$O(\Lambda tm d/T)1 k^{0}/2 2+k^{0}/2(d/d^{0}m)$$

$$\rho(t)\phi_{T}eO+O+O \Lambda tm^{−}de^{−}^{2}.(S 1 1 3)$$

$$∥ − ∥ \le TT$$

(cid:18) (cid:19) (cid:18) (cid:19)

$$(cid:0)(cid:1)$$

Thus, choosing

$$m \Lambda t \Lambda tm m \Lambda t$$

$$d=\Theta mp ol yl og,T=\Theta po ly lo g$$

$$\epsilon \epsilon \epsilon$$

(cid:18) (cid:18) (cid:19)(cid:19) (cid:18) (cid:18) (cid:19)(cid:19) ensures that $\rho$(t) $\phi_{T}\epsilon$. Finally, we note that $\phi N$ by itself is guaranteed to be positive semi-deﬁnite but not

$$∥ − ∥ \le$$

normalized. We will instead consider $\phi$˜$T=\phi T$/Tr($\phi T$)—note that, if $\phi_{T}\rho$(t) $\epsilon<1$,

$$∥ − ∥ \le$$

$$1 Tr(\phi_{T})1^{(}^{1}^{)}2 \epsilon$$

$$\phi^{˜}_{T}\rho(t)_{1}\phi_{T}\rho(t)_{1}+− \rho(t)O(\epsilon),(S 1 1 5)$$

$$∥ − ∥ \le Tr(\phi_{N})∥ − ∥ Tr(\phi_{T})∥ ∥ \le 1 \epsilon \le$$

$$(cid:12)(cid:12)$$

$$(cid:12)(cid:12)$$

where in (1) we have used that Tr($\phi T$) 1 $=$ Tr($\phi T$) Tr(cid:12)($\rho$(t)) $\phi T$(cid:12) $\rho$(t) $\epsilon$.

$$−||−^{(cid:12)}| \le ∥^{(cid:12)}− ∥^{1} \le$$

Time-complexity of sampling in the Fock state basis. We now consider the cost of sampling from the state $\phi$˜T. By construction, $\phi$˜T is a separable state and hence can be expressed as

$$_{˜}(\alpha)$$

$$\phi_{T}=p_{\alpha}\rho,(S 1 1 6)$$

$$\alpha(cid:18)i(cid:19)$$

$$(\alpha)_{t}_{h}$$

where $p \alpha$ is a probability distribution over $\alpha$ and $\rho$ is a state supported on the modes at the i site. To either

$$_{˜}(\alpha)$$

sample from or compute a local observable in $\phi T$, we ﬁrst sample from $p \alpha$ and obtain a product state $i \rho$ from

$$˜ i,\sigma;j,\sigma$$

the mixed state ensemble $\phi T$. Given the initial state $\rho d$(0) as a product state, we sequentially apply

$$\le M_{−}$$

normalize the result and sample from the resulting separable state to obtain another product state—since the input

$$i,\sigma;j,\sigma$$

state is a product state, each application of , normalization and the subsequent sampling involves only the 2L truncated bosonic modes at sites i and j and can be classically done in O(d ) O(m polylog($m \Lambda t$/$\epsilon$)) time.

$$os^{ \le }$$

Additionally, the application of the on-site unitaries ( ) will map a product state between the diﬀerent sites to another product state, and it can be applied classically in O(md ) O(m polylog($m \Lambda t$/$\epsilon$)) time. Counting

$$^{′} \le$$

$$i,\sigma;j,\sigma os$$

the time needed to apply, in this manner, all and , the total classical run-time for drawing one

$$\tau \delta,(\tau 1)\delta \tau \delta,(\tau 1)\delta$$

$$M − U −$$

˜ 2 4L 2 2 4L+8 1 product state from $\phi T$ is thus O(Tm m polylog($m \Lambda t$/$\epsilon$)) O($\Lambda$ t m $\epsilon −$ polylog($m \Lambda t$/$\epsilon$)). Having drawn a

$$(\alpha)^{\times}_{˜}^{ \le }$$

product state $i \rho$ from the separable state $\phi T$, we can now consider the task of drawing a sample in the Fock

$$^{⊗}(\alpha)_{L}_{L}(\alpha)$$

state basis: Given each $\rho$ as a d d matrix, drawing a sample from $i \rho$ on the Fock state basis requires

$$LL+^{\times}1^{⊗}$$

computational time O(nd ) O(m polylog($m \Lambda t$/$\epsilon$)). Thus, the total time complexity of drawing a single sample

$$˜^{ \le }2 2 4 L+8 1$$

from $\phi T$ is dominated by the cost of sampling from $p \alpha$ and is O($\Lambda$ t m $\epsilon −$ polylog $m \Lambda t$/$\epsilon$)).

$$(cid:0)$$

IV. HIGH-NOISESEPARABILITYINSPINMODELS In this section, we analyze a spin model evolving under a 2-local Hamiltonian in the presence of noise, which closely follows the analysis of the bosonic model in the previous section. We only provide a derivation of the counterpart of Lemma 13 for the spin model, which outlines a suﬃcient condition for separability preservation for two qudits. Combining this lemma with standard ﬁrst-order Trotterization can allow us to show that even in the many-body regime, a suﬃciently high noise maps a separable state to another separable state. Lemma 14 (Separability condition for spin models). Consider a Lindbladian on two d level qudits given by

$$(t)=i[h(t),]+\kappa(t)_{L},$$

$$i,k$$

$$L − \cdot D$$

$$∈ X \{\}X$$

where $\kappa$(t) 0. Here h(t) is a two-qudit Hamiltonian which we express as $\ge$

$$h(t)=s_{\alpha}(t)O_{1}_{,}_{\alpha}O_{2}_{,}_{\alpha},$$

where we can assume $s \alpha$(t) 0, Oi,$\alpha$ are Hermitian operators on the i qudit with Oi,$\alpha$ 1. Furthermore, for

$$\ge_{2}∥ ∥ \le$$

each i 1,2 , the jump operators Li,k satisfy Li,k 1 and have a full Kraus rank and $\lambda_{0}>0$ such that for

$$∈ \{\}∥ ∥ \le ∃$$

any single qudit operator A

$$Tr(L^{†}A)\lambda_{0}A .$$

$$i,kF$$

$$|| \ge ∥ ∥$$

Then if $\kappa$(t) $s \alpha$(t)/$\lambda 0$, there is a completely positive map t+$\tau$,t which maps separable states to separable states

$$\ge M$$

and

$$t+\tau t+\tau t+\tau 2$$

$$_{t}_{+}_{\tau}_{,}_{t}ex p(s)ds 4 \kappa(t^{′})dt^{′}+s_{\alpha}(t^{′})dt^{′}.$$

$$M − T_{t}L \le_{t}_{t}$$

(cid:13) (cid:18)Z (cid:19)(cid:13)⋄ (cid:18)Z $\alpha Z$ (cid:19)

$$(cid:13)(cid:13)$$

$$(cid:13)(cid:13)$$

Proof. It will be co(cid:13)nvenient to introduce the scalars (cid:13)

$$t+\tau t+\tau$$

$$S_{\alpha}=s_{\alpha}(t^{′})dt^{′},S=S_{\alpha}an dK=\kappa(t^{′})dt^{′}.$$

$$t_{\alpha}t$$

We will also deﬁne

$$t+\tau$$

$$e ﬀ^{\kappa}^{(}^{t}^{)}e ﬀ e ﬀ e ﬀ e ﬀ$$

$$q_{i}(t)=L^{†}L_{i}_{,}_{k},q=q_{1}(t)I+Iq_{2}(t)an dQ_{i}=ex pq_{i}(t^{′})dt^{′}.$$

i,k

$$2 ⊗ ⊗ −_{t}$$

$$(cid:18)Z(cid:19)$$

Consider the following completely positive map

$$_{t}_{+}_{\tau}_{,}_{t}\rho=^{E}_{z}(R_{1}(z)R_{2}(z))\rho(R_{1}^{†}(z)R_{2}^{†}(z)),(S 1 1 9 a)$$

$$R ⊗ ⊗$$

$$wh er e(cid:0)(cid:1)$$

$$R_{1}(z)=Q_{1}+e^{−}z_{\alpha}S_{\alpha}O_{1}_{,}_{\alpha}an dR_{2}(z)=Q_{2}+e^{−}z_{\alpha}^{∗}S_{\alpha}O_{2}_{,}_{\alpha},$$

$$Xp Xp$$

where $z \alpha$ aredrawnuniformlyandindependentlyfromtheset 1, i . Wenotethat t+$\tau$,t is separability preserving

$$\{\pm \pm \}R$$

i.e. maps a separable state to another separable state. Explicitly evaluating the expectation value in Eq. (S119), we obtain

$$_{t}_{+}_{\tau}_{,}_{t}(\rho)=(Q_{1}Q_{2})\rho(Q^{†}_{1}Q^{†}_{2})iS_{\alpha}(O_{1}_{,}_{\alpha}O_{2}_{,}_{\alpha})\rho(Q^{†}_{1}Q^{†}_{2})(Q_{1}Q_{2})\rho(O_{1}_{,}_{\alpha}O_{2}_{,}_{\alpha})+$$

$$R ⊗ ⊗ − ⊗ ⊗ − ⊗ ⊗$$

$$X(cid:0)(cid:1)$$

$$S_{\alpha}(O_{1}_{,}_{\alpha}Q_{2})\rho(O_{1}_{,}_{\alpha}Q^{†}_{2})+(Q_{1}O_{2}_{,}_{\alpha})\rho(Q^{†}_{1}O_{2}_{,}_{\alpha})+$$

$$⊗ ⊗ ⊗ ⊗$$

$$X(cid:0)(cid:1)$$

$$S_{\alpha}S_{\alpha}^{′}(O_{1}_{,}_{\alpha}O_{2}_{,}_{\alpha})\rho(O_{1}_{,}_{\alpha}^{′}O_{2}_{,}_{\alpha}^{′})+(O_{1}_{,}_{\alpha}O_{2}_{,}_{\alpha}^{′})\rho(O_{1}_{,}_{\alpha}O_{2}_{,}_{\alpha}^{′}),(S 1 2 0)$$

$$⊗ ⊗ ⊗ ⊗$$

$$\alpha,\alpha^{′}$$

$$(cid:0)(cid:1)$$

eﬀ 2 where using Qi 1, Qi I K/2, Qi (I qi ) K /8, we obtain that

$$∥ ∥ \le ∥ − ∥ \le ∥ − − ∥ \le$$

$$t+\tau t+\tau$$

$$_{t}_{+}_{\tau}_{,}_{t}(\rho)=\rho i[h(t^{′}),\rho]dt^{′}q(t^{′}),\rho dt^{′}+$$

$$R −_{t}−_{t}\{\}$$

$$S_{\alpha}(O_{1}_{,}_{\alpha}I)\rho(O_{1}_{,}_{\alpha}I)+(IO_{2}_{,}_{\alpha})\rho(IO_{2}_{,}_{\alpha}))+∆_{t}_{+}_{\tau}_{,}_{t}(\rho)$$

$$⊗ ⊗ ⊗ ⊗$$

$$t+\tau$$

$$(R)$$

$$=\rho+(t^{′})\rho dt^{′}_{t}_{+}_{\tau}_{,}_{t}\rho+∆_{t}_{+}_{\tau}_{,}_{t}(\rho),(S 1 2 1)$$

$$_{t}L − G$$

where t+$\tau$,t is a superoperator given by

$$t+\tau,t^{=}t+\tau,t^{i}^{d}^{+}^{i}^{d}t+\tau,t^{,}^{w}^{h}^{e}^{r}^{e}$$

$$GG ⊗ ⊗ G$$

$$(i)$$

$$_{t}_{+}_{\tau}_{,}_{t}(\rho)=KL_{i}_{,}_{k}\rho L^{†}S_{\alpha}O_{i}_{,}_{\alpha}\rho O_{i}_{,}_{\alpha},(S 1 2 2)$$

$$i,k$$

and ∆t+$\tau$,t is a super-operator with

$$∆_{t}_{+}_{\tau}_{,}_{t}2 K+4 SK+2 S=2(S+K).(S 1 2 3)$$

$$∥ ∥^{⋄} \le$$

Furthermore, the channel generated by the Lindbladian can be expanded to the ﬁrst order to obtain

$$t+\tau t+\tau$$

$$(L)$$

$$ex p(s)ds=\rho+(t^{′})\rho dt^{′}+∆_{t}_{+}_{\tau}_{,}_{t},$$

$$T_{t}L_{t}L$$

$$(cid:18)Z(cid:19)$$

$$(L)$$

where, since (t) 2( $s \alpha$(t) +$\kappa$(t)), ∆t+$\tau$,t is a superoperator with

$$∥ L ∥^{⋄} \le$$

$$∆_{t}_{+}_{\tau}_{,}_{t}2 S+K .(S 1 2 5)$$

$$∥ ∥^{⋄} \le$$

Consequently, we have that (cid:0) (cid:1)

$$^{e}^{x}^{p}^{(}^{s}^{)}^{d}^{s}t+\tau,t^{+}t+\tau,t$$

$$T_{0}L − RG \le$$

(cid:13) (cid:18)Z (cid:19) (cid:13)⋄ (cid:13) (cid:0) (cid:1)(cid:13) We note that t+$\tau$,t is separab(cid:13)(cid:13)ility preserving by construction. Furtherm(cid:13)(cid:13)ore, t+$\tau$,t is a sum of super-operators acting individually on the two qudits—consequently, t+$\tau$,t will be separability preserving as long as it is completely positive.

$$^{G}(i)$$

To ﬁnd a suﬃcient condition for complete positivity of t+$\tau$,t, we will impose that its Choi state, $\Phi$ (i), is positive semi-deﬁnite. From Eq. (S122), we obtain that

$$\Phi^{(}^{i}^{)}=KL_{i}_{,}_{k}jj^{′}L^{†}S_{\alpha}O_{i}_{,}_{\alpha}jj^{′}O_{i}_{,}_{\alpha}jj^{′}.(S 1 2 7)$$

$$i,k$$

$$^{G}|\rangle \langle|−|\rangle \langle|⊗|\rangle \langle|$$

$$j,j^{′}=1(cid:18)k \alpha(cid:19)$$

$$XX X$$

Now, suppose $\psi=_{′}\psi_{j}$,j′ j,j′ Cd Cd is a two-qudit state and $\Psi=_{′}\psi_{j}$,j′ j j′ is its corresponding

$$j,jj,j$$

$$|\rangle|\rangle ∈ ⊗|\rangle \langle|$$

matrix, then

$$\psi \Phi^{(}^{i}^{)}\psi=KT r(L^{†}\Psi)S_{\alpha}Tr(O_{i}_{,}_{\alpha}\Psi)$$

$$i,k$$

$$\langle|^{G}|\rangle||−||$$

$$K \lambda_{0}\Psi S_{\alpha}O_{i}_{,}_{\alpha}\Psi$$

$$FF F$$

$$\ge ∥ ∥ − ∥ ∥ ∥ ∥$$

$$=(K \lambda_{0}S)\psi,(S 1 2 8)$$

$$− ∥|\rangle ∥$$

where in (1) we have used the fact that Tr(A†B) Tr(A†A)Tr(B†B) and also the condition Tr($L^{†}\Psi$) k i,k

$$\le || \ge$$

$\lambda_{0}\Psi$ from the lemma statement. Therefore, if K S/$\lambda 0$, which is implied by the condition $\kappa$(t) $s \alpha$(t)/$\lambda 0$,

$$FP \alpha$$

$$∥ ∥_{(}_{i}_{)} \ge \ge$$

then are completely positive. This in turn implies that the super-operator t+$\tau$,$t=$ t+$\tau$,t + t+$\tau$,t is both

$$GM RG P$$

completely positive and separability preserving, which proves the lemma. Similar to the case of the fermionic and bosonic models, this lemma can be combined with ﬁrst-order Trotterization in the many-body setting to show high-noise separability for a broad class of noise models. In particular, we could consider noisy dynamics described by the master equation

$$\rho(t)=i[H,\rho(t)]+\kappa_{L}(S 1 2 9)$$

$$i,k$$

$$dt − D$$

$$i,k$$

with Li,k satisfying the conditions in Lemma 14 and

$$i,j$$

$$H(t)=h_{i}(t)+s_{\alpha}(t)(O_{i}_{,}_{\alpha}O_{j}_{,}_{\alpha}),(S 1 3 0)$$

$$ii<j \alpha$$

$$XX X$$

where Oi,$\alpha$ would be a Hermitian operator acting on the i qudit chosen to be normalized such that Oi,$_{\alpha}=1$. Introducing the “inter-site interaction-strength” parameter J as the smallest number satisfying

$$i,jj,i$$

$$s_{\alpha}(t)+s_{\alpha}(t)Jf or al li,t 0,$$

$$|||| \le \ge$$

$$j>ij<i$$

we can then establish using Lemma 14 that if $\kappa$ J/$\lambda 0$, then an initial separable state of the spins always evolves $\ge$ into a separable state. V. COUNTER-EXAMPLES In this section, we consider the question of whether a counterpart of Theorem 1 can be obtained for the bosonic model, and if a counterpart for Theorem 2 can be established for the fermionic model.

FIG. S1. Representation of the Wigner function for the state $\rho$(t) obtained by evolving Eq. (S133) with initial state $\rho$(0) $=$ |$\alpha \rangle \langle \alpha$|, with parameters $U=0$.05 and $t=0$.5. (a) The Wigner function W(x,p) is represented in phase space for $\alpha=5$ and error rate $\kappa=0$.1U (left) and $\kappa=2$U (right). (b) Representation of the minimum value of the Wigner function Wmin $=$ minx,pW(x,p). One can clearly observe that, for a ﬁxed value o$f \kappa$/U, the Wigner function becomes more negative by increasing $\alpha$, which suggest that the Gaussian resources can eﬀectively boost the non-Gaussianity of the system. Hence, even for large values of $\kappa$, a negative Wigner state might be reached, by increasing $\alpha$. A. High-noise regime for the bosonic model is not convex-Gaussian at all times We will provide evidence that there is no counterpart of Theorem 1 for bosonic systems. That is, even with noise rates larger than the non-Gaussianity ($\kappa$ U), one can still obtain states which are not convex-Gaussian. In section VA1, we provide numerical evidence that, with a single bosonic mode and dephasing noise greater than the nonGaussianity ($\kappa 3$ U), states with negative Wigner function can be reached, which automatically implies lack of $\ge$ convex Gaussianity. In section VA2, we provide a stronger argument in the absence of dephasing noise: for noise models containing only incoherent particle loss and gain ($\kappa_{3}=0$), one can perform high-ﬁdelity arbitrary gates even if the non-Gaussianity is much smaller than the noise rate, U $\kappa$, provided that the Gaussian couplings J,Ω can be made suﬃciently large, enabling the implementation of gates with eﬀective error rates below the fault tolerance threshold [S8–S10]. As a consequence, not only is the state not guaranteed to remain convex-Gaussian, but the classical simulation of local observables is provably BQP-hard. 1. High dephasing noise regime Here, we provide a simple example with a single bosonic mode, where dephasing noise, no-matter how high, is unable to make the state convex Gaussian. Our analysis is centered on the Wigner function, which, for a single bosonic mode state $\rho$, is deﬁned as 2ipy

$$W(x,p)=xy \rho x+ye dy .(S 1 3 2)$$

$$\pi \langle −||\rangle$$

$$Z − \infty$$

Since quantum states with positive Wigner functions can be eﬃciently simulated [S11], the negativity of the Wigner functionisregardedasanecessaryresourceforquantumadvantage. Furthermore, anegativeWignerfunctionrulesout convex-Gaussianity, sinceallpureGaussianstateshavenonnegativeWignerfunctions[S12, S13], andasaconsequence convex Gaussian states do as well. Speciﬁcally, we consider an initial state $\rho$(0) $=\alpha \alpha$ , where $\alpha$ represents the single-mode coherent state $\alpha=$

$$^{†}|\rangle \langle||\rangle|\rangle$$

$$\alpha(aa)2$$

e − vac , wit$h \alpha a$ real number. Then, the state is evolved under the Hamiltonian $H=Un$ and dephasing noise of rate $\kappa_{3}=\kappa$, which yields the master equation

$$\rho(t)=\rho(t)=iU[n,\rho(t)]+\kappa n \rho(t)nn,\rho(t).(S 1 3 3)$$

$$dt L − − 2 \{\}$$

$$(cid:18)(cid:19)$$

In this setting, we numerically compute the minimum value of the Wigner function, Wmin $=$ minx,pW(x,p), and represent it in Fig. S1. One can appreciate that, even when $\kappa$ U, using a suﬃciently large $\alpha$ results in a state with $\ge$ a negative Wigner function. Consequently, we do not expect an analogue of Theorem 1 to hold for bosons: even for a high dephasing noise rate, with a suﬃciently large Gaussian displacement, an initially Gaussian state can evolve into Wigner negative (not convex-Gaussian) states at short times. The time-scale at which the state becomes Wigner negative is determined by both the value of U, as well as the displacement. For the one-mode problem considered

$$0 0 0 0 2 5 Æ=3_{.}0 Æ=3_{.}0 Æ=3_{.}0$$

$$Æ=3_{.}5 0 . 0 0 8 Æ=3_{.}5 Æ=3_{.}5$$

$$^{a}^{0}.^{0}^{0}^{0}^{2}^{0}Æ=4_{.}0^{a}Æ=4_{.}0 Æ=4_{.}0$$

$$W Æ=4_{.}5^{0}.^{0}^{0}^{6}Æ=4_{.}5 Æ=4_{.}5$$

$$^{/}Æ=5_{.}0 Æ=5_{.}0 Æ=5_{.}0$$

n n n

$$° 0_{.}0 0 0 0 5 °^{0}.^{0}^{0}^{2}°^{0}^{.}^{0}^{1}$$

0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30

$$Ti me \sum_{t}Ti me \sum_{t}Ti me \sum_{t}$$

FIG. S2. The relative Wigner negativity, quantiﬁed by −Wmin/Wmax $=− m$inx,pW(x,p)/maxx,pW(x,p), for a single bosonic mode evolving under the Hamiltonian $H=Un$ as well as dephasing noise at rate $\kappa$. The initial state of the bosonic mode is the coherent state |$\alpha \rangle$. As expected, the relative Wigner negativity decreases as U decreases, and at a ﬁxed $\alpha$, the maximum Wigner negativity is attained at time-scales of 1/U. above, Fig. S2 shows the relative wigner-negativity Wmin/Wmax $=$ minx,pW(x,p)/maxx,pW(x,p) as a function of time. We ﬁnd that while the state eventually becomes Wigner non-negative, even in the regime $\kappa 3$ U, there is an intermediate temporal region that depends on U and $\alpha$ where the state is Wigner negative. For a ﬁxed $\alpha$, the time t∗ at which the state is maximally Wigner negative scales as 1/U, consistent with the fact that U determines the strength of the process generating the non-Gaussianity or Wigner negativity in the dynamics. We remark that this does not necessarily imply simulation hardness: the question of whether there is a threshold error $\kappa t$h(U) depending on U but not on J,Ω above which the classical simulation becomes tractable remains open. 2. High incoherent particle loss and gain regime Here we analyze the complexity of classically simulating the bosonic system in the absence of dephasing noise ($\kappa_{3}=0$) and ﬁnd that the problem does not become easy above a noise threshold depending exclusively on the non-Gaussian interaction strength, thus showing that no counterpart of Theorem 1 can exist for bosons in the absence of dephasing noise. Speciﬁcally, we show that, even when the non-Gaussian interaction strength is much smaller than the noise strength, U $\kappa$, one can perform arbitrarily fast gates. Due to the threshold theorem, this allows for the implementation of fault-tolerant schemes [S8, S10]. To show this, it is enough to consider systems with only one bosonic mode per site ($L=1$) and only onsite non-Gaussianity ($U_{C}=0$). We will start with a technical lemma: we will show that, for a system with m modes evolving under the noise model in Eq. (S27), the error induced by the noise can be upper bounded by O($m \kappa t$). Lemma 15 (Error bound between noisy and noiseless evolution). Consider a bosonic system with m modes evolving under the master equation

$$\rho(t)=\rho(t)=i[H(t),\rho(t)]+\kappa_{l}^{(}^{l}^{)},$$

DLv

$$l=1 v=1$$

where $_{L}\rho=L \rho L_{†}L_{†}L$,$\rho$ /2, Lv $=a_{v}$,Lv $=a †_{v}$, and $\kappa 1$ + $\kappa_{2}=1$. Assume that, for some integer d,

$$D − \{\}$$

$\rho$(0) lies in the subspace d of the Hilbert space spanned by the ﬁrst d + 1 levels 0 ,..., d , and that the

$$H^{ \le }\{|\rangle|\rangle \}$$

Hamiltonian H(t) contains no couplings between the state d and any state k with $k>d$. Then, denoting by

$$_{t}|\rangle|\rangle$$

( ) $=$ exp i [H(s), ]ds the time-evolution in the noiseless case ($\kappa=0$), the error induced by the dissipation

$$U \cdot T − \cdot$$

can be bounde(cid:16)d as (cid:17)

$$ex p(s)ds \rho(0)\rho(0)2 m \kappa t(d+1).$$

$$T_{0}L − U \le$$

(cid:13) (cid:18)Z (cid:19) (cid:13)1

$$(cid:13)(cid:13)$$

Proof. Let us consider the follow(cid:13)ing eﬀective Hamiltonian: (cid:13)

$$(cid:13)(cid:13)$$

$$H_{e}_{ﬀ}=Hi \kappa_{1}a^{†}_{v}a_{v}+\kappa_{2}a_{v}a^{†}_{v}.$$

$$v=1$$

$$X(cid:0)(cid:1)$$

Then, the time evolution may be written as

$$\rho(t)=ex p(s)ds \rho(0)=ex pi[H_{e}_{ﬀ}(s),]ds \rho(0)+(\rho(0))=\sigma+(\rho(0)),$$

$$T_{0}LT −_{0}\cdot NN$$

(cid:18)Z (cid:19) (cid:18) Z (cid:19) where $\sigma$ is the (unnormalized) state obtain|ed by evolving{uznder the eﬀecti}ve Hamiltonian, and ($\rho$) is a completely positive channel that is not trace preserving. Naturally, tr($\sigma$) + tr( ($\rho$)) $=1$. The state $\sigma$ can be understood as the output when no errors occur, while ($\rho$) captures the output with one or more errors.

$$th^{N}d$$

For the v bosonic mode, we deﬁne the projector that truncates to at most d particles as $\Pi v$, $d=$ j j .

$$j=0$$

$$^{ \le }|\rangle \langle|$$

Then, $\Pi$ $d^{=}v^{\Pi}v$, d is the projector onto d. Note that, since H does not contain couplings to higher levels,

$$\le ⊗ \le H \le P$$

neither does Heﬀ. As a consequence, the dynamics of $\sigma$ are constrained to the ﬁrst d+1 levels, and can be truncated. Let us denote the truncated Hamiltonians by H˜ $=\Pi_{d}H \Pi_{d}$,H˜dis $=\Pi_{d}H$di$s^{\Pi}d$. Using the deﬁnition of H˜dis in Eq. (S134), the operator norm of the truncated eﬀective Hamiltonian H˜dis can then be bounded as

$$mm m \kappa$$

$$H^{˜}_{d}_{i}_{s}(\kappa_{1}d+\kappa_{2}(d+1))(\kappa_{1}+\kappa_{2})d$$

$$∥ ∥ \le 2 \le 2 \le 2$$

Let us now write $\sigma$ in a more convenient form as $\sigma=l$imN ($O_{N}\rho$(0)O† ), where

$$iH^{˜}(kt/N)t/Ni H^{˜}_{d}_{i}_{s}t/N$$

$$O_{N}=e^{−}e^{−}.(S 1 3 7)$$

$$k=1$$

$$Y(cid:16)(cid:17)$$

This expression can be derived, for example, from standard Trotterization techniques. We would now like to bound tr($\sigma$), which can be understood as the probability of no errors occurring during the computation. Naturally, the unitary parts of the evolution in Eq. (S137) are trace preserving, and we only need to bound the imaginary time evolution induced by the Hamiltonian H˜dis. Note also that, using Eq. (S136), the minimum singular value in each step can be bounded as

$$_{H}^{˜}_{t}_{/}_{N}m \kappa tm \kappa t$$

$\sigma m$in(e− dis ) exp ($\kappa 1$(d+1)+$\kappa 2$(d+1)) exp

$$\ge − 2 N \ge − 2 N$$

(cid:18) (cid:19) (cid:18) (cid:19) As a consequence, using Eq. (S137) and Eq. (S138), it can be easily checked that

$$H^{˜}_{d}_{i}_{s}t/N$$

$$\sigma_{m}_{i}_{n}(O^{†}O_{N})\sigma_{m}_{i}_{n}(e^{−})ex p[m \kappa t(d+1)].$$

$$\ge \ge −$$

This allows us to bound the trace as tr($\sigma$) $=$ lim tr($O^{†}O_{N}\rho$ $O_{N}\rho$(0)) lim $\sigma m$in(O† ON)tr($\rho$(0)) exp[ $m \kappa t$(d + 1)].

$$^{N} \ge^{N} \ge −$$

$$\to \infty \to \infty$$

As a consequence, since the total evolution of the system must be trace preserving, it immediately follows that

$$m \kappa td$$

tr( ($\rho$(0)) 1 e− .

$$N \le −$$

Now, let us bound the distance between $\sigma$ and the state obtained under ideal (noiseless) evolution, $\sigma \rho$(0) 1. ∥ −U ∥ We use the fact that

$$^{\partial}H ˜^{t}^{t}^{H}^{˜}di sH ˜^{t}H ˜^{t}iH ˜(\kappa t/N)^{t}$$

e− dis$^{N}=e −$ disN and e− disN , e−

$$\partial \kappa − N \kappa ∥ ∥ ∥ ∥ \le$$

Using Eq. (S136), one can bound

$$^{\partial}_{H}˜^{t}^{t}^{H}^{˜}di s_{H}˜^{t}$$

$$e_{−}^{d}^{i}^{s}^{N}=e_{−}^{d}^{i}^{s}^{N}H^{˜}_{d}_{i}_{s}$$

$$\partial \kappa_{(cid:13)}N \kappa_{(cid:13)} \le N \kappa ∥ ∥ \le 2 N$$

(cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) Furthermore, using the d(cid:13)eﬁnition of (cid:13)ON (cid:13)in Eq. (S137),(cid:13)the norm bound in Eq. (S142), and the fact that

$$H^{˜}_{d}_{i}_{s}^{t}iH^{˜}(\kappa t/N)^{t}$$

e− N , e− N 1, one can bound

$$∥ ∥ ∥ ∥ \le$$

$$\partial \partial 2 t$$

$$H^{˜}_{d}_{i}_{s}mt(d+1).$$

$$\partial \kappa \le \partial \kappa \le \kappa ∥ ∥ \le$$

(cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13)

This directly yields a bound on the desired distance:

$$\partial \partial$$

$$\sigma \rho(0)_{1}=\sigma d \kappa \sigma d \kappa m \kappa t(d+1).(S 1 4 4)$$

$$∥ − U ∥_{0}\partial \kappa \le_{0}\partial \kappa \le$$

(cid:13)Z (cid:13)1 Z (cid:13) (cid:13)1 (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) Finally, this, together with Eqs. (S135, S14(cid:13)4), implies t(cid:13)hat (cid:13) (cid:13)

$$m \kappa t(d+1)$$

$$ex p(s)ds \rho(0)\rho(0)\rho(t)\sigma_{1}+(\rho(0))_{1}m \kappa t(d+1)+1 e^{−}2 m \kappa t(d+1),$$

$$T_{0}L − U \le ∥ − ∥ ∥ N ∥ \le − \le$$

(cid:13) (cid:18)Z (cid:19) (cid:13)1

$$(cid:13)(cid:13)$$

$$(cid:13)(cid:13)$$

$$(cid:13)(cid:13)$$

which proves the lemma. We will now show how one can use a single bosonic mode Hamiltonian to apply arbitrary single qubit gates with high ﬁdelity, even when the nonlinearity is much smaller than the noise strength. We note that a similar result is already shown in Refs. [S14, S15]. To do this, we will consider a single bosonic mode with $\kappa$ U, where both the error rate and non-Gaussianity U are ﬁxed, and study the eﬀective error rate in the asymptotic limit of large Gaussian strength. Lemma 16 (Single-qubit gates, from Ref. [S14]). Consider a single bosonic mode under the master equation

$$\rho=\rho=i[H(t),\rho]+\kappa_{l}_{L}^{(}^{l}^{)}\rho,$$

$$dt L − D$$

$$l=1$$

with Hamiltonian

$$H(t)=U(t)a^{†}a+\Lambda_{1}(t)a^{†}+\Lambda_{2}(t)a^{†}+h . c .+∆(t)a^{†}a,$$

$$(2)(cid:0)(3)(cid:1)$$

where $_{L}\rho=L \rho L_{†}L_{†}L$,$\rho$ /2, L $=a$,L $=a_{†}$ and L $=a_{†}a=n$, and $\kappa 1$ +$\kappa_{2}=\kappa$, and the strength of the

$$D − \{\}$$

Gaussian terms is bounded by P, $\Lambda 1$(t) , $\Lambda 2$(t) , ∆(t) P. Then, for any single-qubit quantum unitary operation

$$|||||| \le^{t}_{(}_{s}_{)}_{d}_{s}U$$

(i.e. ( ) $=U$( )U† for some single-qubit gate U), the Lindbladian (t) can approximate , ( e 0 L

$$_{˜}U_{2}\cdot_{1}_{/}_{3}\cdot_{2}_{1}_{/}_{3}LU ∥ T − U ∥ \le$$

O($\kappa$(U P)− ), in time $t=O$((U P)− ), with $\rho 0$ a single-qubit state. Proof. We will show that, by tuning the parameters in the Hamiltonian H(t), one can generate T, S, and $\sqrt X$ gates, which is suﬃcient for arbitrary single-qubit rotations. For implementing a T gate or an S gate, one simply has to set Ω(t) $=0$ and ∆(t) $=P$. This yields the Hamiltonian $H=U$(a† a )/2+Pa†a. Since there are no couplings between the states 0 , 1 and the rest, we can restrict ourselves to the subspace spanned by 0 , 1 . Denoting the projector

$$|\rangle|\rangle \{|\rangle|\rangle \}$$

onto this subspace $\Pi_{1}=0$ 0 + 1 1 , the projection of $H \alpha$ on the blockaded subspace yields $\Pi_{1}H \Pi_{1}=P$ 1 1 .

$$|\rangle \langle||\rangle \langle||\rangle \langle|$$

Then, evolving under the Hamiltonian for time $t=3 \pi$/(2P) yields an S gate, while evolving for time $t=3 \pi$/(4P) yields a T gate. Therefore, applying the error bound in Lemma 15, T gates and S gates can be implemented with

$$pr ec is io nO(\kappa/P)in ti me t=O(1/P).$$

Now, let us consider the problem of applying a $\sqrt X$ gate. This can be done by using the construction from Refs. [S14, S16], by going to a displaced frame. We will ﬁrst show that, considering the Hamiltonian in a displaced frame, one can implement a fast $\sqrt X$ gate. Then, we will show that one can go to the displaced frame by applying fast pulses at the beginning and end of the computation, hence enabling the application of a high-ﬁdelity fast $\sqrt X$ gate in the laboratory frame, even in the presence of errors. First, let us consider the Hamiltonian in a frame displaced by $\alpha$(t), a a+$\alpha$(t). We write the Hamiltonian in the displaced frame as $H \alpha$(t) and the noise as L(l);$\alpha$(t). Note that the noise in the displaced frame can be written as

$$\kappa_{l}_{L}^{(}^{l}^{)}_{,}_{\alpha}_{(}_{t}_{)}()=\kappa_{l}_{L}^{(}^{l}^{)}+(\kappa_{1}\kappa_{2})i(\alpha(t)a^{†}\alpha^{∗}(t)a),().(S 1 4 6)$$

$$D \cdot D 2 − − \cdot$$

$$l=1 l=1$$

$$(cid:2)(cid:3)$$

Furthermore, the displaced Hamiltonian $H \alpha$(t) may be written as

$$H_{\alpha}_{(}_{t}_{)}=U(t)a^{†}^{2}a^{2}+∆^{˜}(t)a^{†}a+(\Lambda^{˜}_{1}(t)a^{†}+\Lambda^{˜}_{2}(t)a^{†}^{2}+\Lambda^{˜}_{3}(t)a^{†}^{2}a+h . c .),(S 1 4 7)$$

where

$$∆^{˜}(t)=∆(t)+4 U(t)\alpha(t)^{2},$$

$$\Lambda^{˜}_{2}(t)=\Lambda_{2}(t)+2 U(t)\alpha(t)^{2},$$

$$\Lambda^{˜}_{1}(t)=\Lambda_{1}(t)+\alpha ∆(t)+2 \alpha(t)^{∗}\Lambda_{2}(t)+2 U(t)\alpha(t)^{2}\alpha(t)^{1}i \alpha(t)(\kappa_{1}\kappa_{2}),$$

$$||− 2 −$$

$$\Lambda^{˜}_{3}(t)=2 U(t)\alpha(t).(S 1 4 8)$$

where the noise term from Eq (S146) has already been absorbed into the Hamiltonian. The master equation in the displaced frame is then

$$^{\rho}\alpha(t)^{=}\alpha(t)^{\rho}\alpha(t)^{=}^{i}^{[}^{H}\alpha(t)^{,}^{\rho}\alpha(t)^{]}^{+}^{\kappa}lL^{(}^{l}^{)}^{.}^{(}^{S}^{1}^{4}^{9}^{)}$$

$$dt L − D$$

$$l=1$$

By suitably choosing the parameters so that ∆˜(t) $=\Lambda$˜1(t) $=\Lambda$˜2(t) $=0$, the Hamiltonian becomes $H \alpha$(t) $=$

$$2 U(t)\alpha(t)a_{†}(n 1)+h . c . .$$

Crucially, one can notice that the Hamiltonian $H \alpha$(t) is blockaded, since it does not contain couplings to state 2 . Therefore, in the noiseless case, the dynamics will be restricted to the qubit subspace spanned by 0 , 1 . Denoting

$$\{|\rangle|\rangle \}$$

the projector onto this subspace by $\Pi_{1}=0$ 0 + 1 1 , the projection of $H \alpha$(t) onto the blockaded subspace yields

$$|\rangle \langle||\rangle \langle|$$

$\Pi 1 H \alpha$(t)$\Pi_{1}=$ 2$U \alpha$(t)X. Let us pick a constant $\alpha$(t) $=\alpha_{F}$. It is then clear that evolving under the Hamiltonian $H \alpha$ for a time $t=\pi$/(8$U \alpha_{F}$) produces a $\sqrt X$ gate. We will pick the displacement to b$e \alpha_{F}=\Theta$((P/U) ), since it is the largest displacement that can simultaneously fulﬁll Eq. (S148) and the restriction that $\Lambda 1$(t) , $\Lambda 2$(t) , ∆(t) P.

$$|||||| \le$$

Naturally, one is interested in performing operations in the laboratory frame, which means that at the beginning ($t=0$) and end ($t=t_{F}$) of the computation the displacement is $\alpha$(0) $=\alpha$(tF) $=0$. This can be achieved by simply applyingadisplacementterminthebeginningandendofthecomputation. Hence, thecomputationcanbeperformed in three steps. First, a displacement term is applied for a time tdis to go from $\alpha$(0) $=0$ to $\alpha$(tdis) $=\alpha_{F}$. Then, the gate is performed in the frame displaced by $\alpha F$, which takes time tgate $=\pi$/(8$U \alpha_{F}$). Finally, the displacement is taken to 0 again, which takes time tdis. Therefore, the total computation time for a $\sqrt X$ gate is $t_{\sqrt}=2$tdis + tgate. In order to achieve the desired displacement $\alpha F$, one can apply the Hamiltonian

$$H(t)=i(P \alpha_{F}\kappa/2)(a^{†}a)+(P \alpha_{F})t(\kappa_{1}\kappa_{2})(a^{†}a),(S 1 5 0)$$

$$− − 2 − − −$$

where the ﬁrst term takes the system to the frame displaced b$y \alpha$(t) $=$ (P $\alpha_{F}\kappa$/2), and the second term corrects the contributions of the noise. The choice of parameters ensures that $\Lambda 1$ P at all times. Speciﬁcally, in the displaced

$$|| \le$$

frame, the system evolves under the master equation

$$^{\rho}\alpha(t)^{=}^{\kappa}lL^{(}^{l}^{)}^{f}^{o}^{r}^{t}^{t}di s^{,}$$

$$dt D \le$$

$$l=1$$

with $\alpha$(0) $=0$ and $\alpha$(tdis) $=\alpha_{F}$, and tdis $=\alpha_{F}$/(P $\alpha F$) $=O$($\alpha F$/P) $=O$((P U)− ). Let us denote the total

$$^{−}1 2 1/3$$

evolution time by $t_{\sqrt}=2$tdis + tgate. Note that tgate $=O$(($U \alpha_{F}$)− ) $=O$((PU )− ), while tdis $=O$($\alpha F$/P) $=$ O((P U)− ). In the large P limit, it is clear that tdis tgate, and the total time scales as $t_{\sqrt}=t$gate + 2tdis $=O$(tgate) $=O$((PU )− ). From the Solovay-Kitaev theorem, it follows that any single-qubit rotation can be approximated to precision $\epsilon$ in time $t=O$($t \sqrt$ log (1/$\epsilon$)) for some constant $c<2$. We can now bound the total contribution of the error: straightforward application of Lemma 15 shows that the error after time $t=O$˜($t \sqrt$ ) $=$ ˜ 2 1/3

$$O((UP)_{−})is$$

$$R(s)ds ˜$$

$$(e^{0}^{L})\rho_{0}_{1}O,(S 1 5 2)$$

$$∥ T − U ∥ \le (U^{2}P)^{1}^{/}^{3}$$

$$(cid:18)(cid:19)$$

where O˜ hides polylogarithmic factors. This proves the lemma. So far we have shown that one can make arbitrary single-qubit gates with high ﬁdelity even if the noise is much largerthanthenon-Gaussianity, $\kappa$ U, as long as one can increment the strength of the Gaussian terms, P $\kappa$ /U . We will now show how to implement entangling gates, which is enough to obtain a universal gate-set.

Lemma 17 (Two-qubit gates). Consider two bosonic modes evolving under the master equation

$$\rho(t)=i[H(t),\rho(t)]+\kappa_{l}^{(}^{l}^{)},(S 1 5 3)$$

DLv

$$l=1 v=1$$

where H(t) is the Hamiltonian H(t) $=H$1(t) + H2(t) + ig(t)[a1a†2 a†1a2], with

$$H_{i}(t)=U_{i}(t)a^{†}a_{i}+\Lambda_{i}_{,}_{1}(t)a^{†}+\Lambda_{i}_{,}_{2}(t)a^{†}+h . c .+∆_{i}(t)a^{†}a_{i},(S 1 5 4)$$

$$ii ii$$

$$(cid:16)(cid:17)$$

and $_{L}\rho=L \rho L_{†}L_{†}L$,$\rho$ /2, Lv $=a_{v}$,Lv $=a †_{v}$, and $\kappa 1$ + $\kappa_{2}=\kappa$. Assume that the strength of the Gaussian

$$D − \{\}$$

$$te rm si sb ou nd ed by P(\Lambda_{i}_{,}_{1}(t),\Lambda_{i}_{,}_{2}(t),∆_{i}(t),g(t)P).$$

$$|||||||| \le$$

Then, for any two-qubit quantum unitary operation (i.e. ( ) $=U$( )U† for some single-qubit gate U), the

$$UU \cdot \cdot^{t}_{(}_{s}_{)}$$

R ds ˜ 2 1/3 Lindbladian (t) can implement a time evolution that approximates , ( e 0 L )$\rho 0$ 1 O($\kappa$(U P)− ), for

$$L^{2}^{1}^{/}^{3}U ∥ T − U ∥ \le$$

a time $t=O$((U P)− ), with $\rho 0$ a two-qubit state. Proof. In Lemma 16 it is shown how to use H(t) to generate arbitrary single-qubit gates on either of the modes with arbitrarily high ﬁdelity. Hence, it is only necessary to show how to apply an entangling two-qubit gate in order to have a universal gate-set. To do this, let us consider the collective modes b1 $=$ (a1 + a2)/$\sqrt 2$ and b2 $=$ (a1 a2)/$\sqrt 2$. We will denote by

$$1/2 jk^{−}1/2 jk$$

j,k $=$ (j!k!)− (a†1) (a†2) 0,0 the Fock states in the original basis, and j,k $=$ (j!k!)− (b†1) (b†2) 0,0 .

$$|\rangle|\rangle|\rangle|\rangle$$

One obtains that

$$0,0=0,0,$$

$$|\rangle|\rangle$$

$$0,1=1,0 0,1,$$

$$a^{1},a^{2}b^{1},b^{2}b^{1},b^{2}$$

$$|\rangle \sqrt 2|\rangle −|\rangle$$

$$(cid:16)(cid:17)$$

$$1,0=1,0+0,1,$$

$$a^{1},a^{2}b^{1},b^{2}b^{1},b^{2}$$

$$|\rangle \sqrt 2|\rangle|\rangle$$

$$(cid:16)(cid:17)$$

1,1 $=$ 2,0 0,2 . (S155)

$$a^{1},a^{2}b^{1},b^{2}b^{1},b^{2}$$

$$|\rangle 2|\rangle −|\rangle$$

$$(cid:16)(cid:17)$$

Let us now denote by U the single-mode unitary that maps U 0 $=0$ , U 1 $=i$ 1 , U 2 $=2$ . Using b1 b1 b1 b1 b1 b1

$$|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle$$

Eq. (S155), it can be seen that U will act in the a1,a2 basis as

$$U 0,0=0,0,$$

$$|\rangle|\rangle$$

$$U 0,1=(1+i)0,1(1 i)1,0,$$

$$a^{1},a^{2}a^{1},a^{2}a^{1},a^{2}$$

$$|\rangle 2|\rangle − −|\rangle$$

$$1(cid:16)(cid:17)$$

$$U 1,0=(1 i)0,1+(1+i)1,0,$$

$$a^{1},a^{2}a^{1},a^{2}a^{1},a^{2}$$

$$|\rangle 2 − −|\rangle|\rangle$$

$$U 1,1=1,^{(cid:16)}1 .^{(cid:17)}$$

$$|\rangle|\rangle$$

Hence, U is clearly an entangling gate between modes a1 and a2. Furthermore, U can be implemented in a fast manner using the same technique as in Lemma 16. Let us detail the procedure. First, one can evolve the system under the term P(a†1a2+h.c), which induces the mixing of the modes a1 b1 and a2 b2 in time $t=O$(1/P). The Hamiltonian in the new basis, Hb(t), may be written us

$$H_{b}(t)=U_{1}b^{†}_{1}b_{1}+(\Lambda_{1}_{,}_{1}b^{†}_{1}+\Lambda_{1}_{,}_{2}b^{†}_{1}+h . c .)+∆_{1}b^{†}_{1}b_{1},(S 1 5 7)$$

where we have chosen ∆2 $=\Lambda_{2}$,1 $=\Lambda_{2}$,2 $=U$2 $=0$. One can note that the technique in Lemma 16 can be readily applied to the Hamiltonian Hb in Eq. (S157). That is, one can go to a frame in which b1 is displaced by $\alpha$(t), b1 b1 + $\alpha$(t). As shown in the proof of Lemma 16, a suitable choice of the parameters leads to the displaced

$$^{ \to }2 2$$

Hamiltonian Hb,$\alpha$(t) $=U$1(t)(b†1) b1 + 2U1[$\alpha$(t)b†1(b†1b1 2)+h.c.]. Note that this Hamiltonian contains no couplings between 2 and 3 , and hence the subspace spanned by 0 , 1 , 2 is blockaded. Furthermore, one can

$$b 1 b 1 b 1 b 1 b 1$$

$$|\rangle|\rangle \{|\rangle|\rangle|\rangle \}$$

rewrite

$$H_{b}_{,}_{\alpha}_{(}_{t}_{)}=U_{1}(t)(b^{†}_{1})b_{1}+2 U_{1}(t)Re(\alpha(t))H_{\alpha}_{,}_{R}+2 U_{1}(t)Im(\alpha(t))H_{\alpha}_{,}_{I},(S 1 5 8)$$

with $H \alpha$(t),$_{R}=b †_{1}$(b†1b1 2)+(b†1b1 2)b1 and $H \alpha$(t),$_{I}=i$(b†1(b†1b1 2) (b†1b1 2)b1). One can compute the commutator

$$−_{2}− − − −$$

[$H \alpha$(t),R,$H \alpha$(t),I] $=2$i(3b†1 b1 6b†1b1 + 4), which is diagonal, and can clearly implement the gate U, which consists

only of a phase rotation of the state 1 . In fact, the analysis in Ref. [S14] shows that one can generate arbitrary unitaries in the subspace spanned by 0 , 1 , 2 .

$$\{|\rangle|\rangle|\rangle \}$$

Following the analysis in Lemma 16, the gate U can then be implemented in time $t_{U}=O$((U P)− ). This is also the dominant source of error, since applying the displacement takes time tdis $=O$((P U)− ), and going to the collective mode b1 takes time $t_{b}=O$(1/P), and therefore tU tdis,tb. Hence, the total error will be

$$2 1/3^{≫}$$

$$O(\kappa t_{U})=O(\kappa(UP)).$$

Therefore, we have shown how to implement an entangling gate. Together with the implementation of arbitrary single-qubit gates and the Solovay-Kitaev theorem (which introduces and additional polylogarithmic factor), this proves that any 2-qubit gate can be implemented by evolving the Lindbladian (t) up to precision

$$R(s)ds ˜$$

$$(e^{0}^{L})\rho_{0}_{1}O,(S 1 5 9)$$

$$∥ T − U ∥ \le (U^{2}P)^{1}^{/}^{3}$$

$$(cid:18)(cid:19)$$

where $\rho 0$ is a two-qubit state, and the error bound follows directly from Lemma 15. Sofar, wehaveshownhowthebosonicHamiltoniancanbeusedtogeneratehigh-ﬁdelityuniversalgates. Speciﬁcally,

$$˜ 2 1/3$$

we have seen that 2-qubit gates can be implemented in time $t=O$((PU )− ), where U is the non-Gaussian strength, and P refers to the maximum absolute value allowed for the Gaussian terms of the Hamiltonian. Let us now consider a system with nL bosonic modes as described in section IE and study the asymptotic scaling with n. In this case,

$$\alpha,\alpha \alpha$$

J (t) , Ωi (t) P. Let us assume that J,Ω $=\Theta$(P) (this is the case, for example, for geometrically local i,j

$$|||| \le$$

Hamiltonians). Then, provided that the Gaussian couplings J,$Ω=O$(1) can be arbitrarily large constants, it follows from Lemma 17 that any gate can be implemented to an arbitrarily small (but independent of n) precision. Since this allows for the implementation of gates with an eﬀective gate error below that of the threshold theorem [S8–S10], this implies that fault-tolerant circuits can be implemented. We remark that, in addition to high-ﬁdelity gates, faulttolerant constructions usually require the ability to implement RESTART operations to provide fresh qubits [S9]. For spin systems in the presence of non-unital noise, cooling algorithms [S17–S19] in conjunction with the noise channel can be leveraged to implement such an operation [S20–S22]. In our case, a similar scheme would be needed; however, we leave a careful analysis of the construction for future work. B. High-noise regime of the fermionic model is not separable at all times For the bosonic model, Theorem 2 establishes that, in the presence of a suﬃciently incoherent high particle loss or incoherent particle gain, the state of the bosonic model is separable at all times. In this subsection, we show that such a result cannot be true for the fermionic model. We show this for two notions of separability for fermions [S23, S24]—the ﬁrst notion holds for all observables, and the second weaker notion holds for parity-conserving, or even, observables. Throughout this section, it will be enough for us to consider separability in the bi-partite setting. We will consider m fermionic modes which are divided into two subgroups of modes, A with modes 1,2,...,mA and B with modes mA+1,mA+2,...,m . Recall that an operator on the fermionic Hilbert space is an element of the algebra generated

$$\{1 2 \}$$

by cv,cv v 1,2...m or alternatively by av,a†v v 1,2...m . An operator acting on sub-system A will be an element

$$\{\}∈ \{\}\{\}∈ \{\}$$

of the algebra generated by av,a†v v 1,2...m and, similarly, an operator acting on the sub-system B will be an

$$\{\}∈ \{\}$$

element of the algebra generated by av,a†v v m +1,m +2...m . The parity operator of a set S 1,2...m of

$$AA B$$

$$\{\}^{∈}^{\{}^{\}}⊆ \{\}$$

fermionic modes is $P_{A}=$ exp($i \pi a^{†}a_{i}$). Operators that conserve the parity operator are called even operators.

$$iS i$$

Physically relevant states of the fermionic modes are restricted to be even operators—note, however, that a physical operator that is even on all the fePrmionic modes is not necessarily even on a subset of these fermionic modes. Deﬁnition 1. A state $\rho$ of m fermionic modes will be called a product state with respect to all observables on the bi-partition A B if there exist states $\rho A$ for the modes in A and $\rho B$ for the modes in B such that, for all operators OA supported on A and OB supported on B,

$$Tr(O_{A}O_{B}\rho)=Tr(O_{A}\rho_{A})Tr(O_{B}\rho_{B}).$$

A state $\rho$ of the m fermionic modes will be called a separable state with respect to all observables on the bi-partition A B if it can be expressed as a convex-combination of such product states. We remark that it was shown in Ref. [S24] that i$f \rho i$s an even operator, which is also a product state as per deﬁnition 1, then $\rho A$ and $\rho B$ are also both even operators.

Deﬁnition 2. A state $\rho$ of m fermionic modes will be called a product state with respect to even observables on the bi-partition A B if there exist states $\rho A$ for the modes in A and $\rho B$ forthe modes in B such that, for all even (+) | (+) operators O supported on A and O supported on B,

$$(+)(+)(+)(+)$$

$$Tr(OO \rho)=Tr(O \rho_{A})Tr(O \rho_{B}).$$

$$AB AB$$

A state $\rho$ of the m fermionic modes will be called a separable state with respect to even observables on the bi-partition A B if it can be expressed as a convex-combination of such product states. As discussed in Ref. [S23] , while separability with respect to all observables implies separability with respect to even observables, the converse is not necessarily true. This can be seen explicitly in a simple 2-mode example—consider the state $\psi=$ (a†1+a†2) vac /$\sqrt 2$. This state is not separable as per deﬁnition 1—to see this, one can use the 2-mode

$$|\rangle|\rangle$$

separability criteria from Refs. [S23, S24] , which we also provide in Lemma 18. However, this state is separable as (+) (+) per deﬁnition 2—to see this, we note that, for any even observable O1 on the ﬁrst fermionic mode and O2 on the second fermionic mode,

$$\psi O_{1}O_{2}\psi=\phi_{1}O_{1}\phi_{1}\phi_{2}O_{2}\phi_{2}+\theta_{1}O_{1}\theta_{1}\theta_{2}O_{2}\theta_{2},(S 1 6 0)$$

$$\langle||\rangle 2 \langle||\rangle \langle||\rangle \langle||\rangle \langle||\rangle$$

$$(cid:0)(cid:1)$$

where $\phi_{1}=a †_{1}$ vac , $\phi_{2}=$ vac , $\theta_{1}=$ vac and $\theta_{2}=a †_{2}$ vac .

$$|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle$$

1. Non-separability for any observable Here, we provide a simple 2-mode example which shows that, unlike the bosonic model, no matter how high the rate of particle loss and incoherent particle gain is in the fermionic model, the dynamics of the fermionic model is not separability preserving with respect to all observables (deﬁnition 1). To establish this result, we ﬁrst review the 2-mode seperability criteria from Refs. [S23, S24]. Lemma 18 (2-mode separability, Refs. [S23, S24]). A 2-mode density matrix $\rho$ is separable with respect to all observables (deﬁnition 1) if and only if it is diagonal in the computational basis. Proposition 1. Consider a system with $m=2$ fermionic modes, with the sub-system A with mode 1 and sub-system B with mode 2 whose density matrix $\rho$(t) satisﬁes the Lindblad master equation

$$\rho(t)=i[J(a^{†}_{1}a_{2}+a^{†}_{2}a_{1}),\rho(t)]+\kappa_{1}_{a}+\kappa_{2}^{†}\rho(t),$$

$$dt − DD^{j}$$

$$j=1$$

$$X(cid:0)(cid:1)$$

Then, $\kappa 1$,$\kappa_{2}>0$, $\rho$(0) which is separable with respect to all observables (Deﬁnition 2) such that $\rho$(t) cannot be separable for all t 0. $\ge$ Proof. Throughout this proof, “separability” refers to separability with respect to all observables (Deﬁnition 1). Consider the initial state $\rho$(0) $=a †_{1}$ vac vac a1. Note that $\rho$(0) is trivially separable—we now establish that, for a

$$^{t}|\rangle \langle|^{2}$$

small time t, $\rho$(t) $=e_{L}$ ($\rho$(0)) is not seperable to O(t ) for any $\kappa$, which is enough to contradict separability of $\rho$(t) at all times t. Now,

$$\rho(t)=\rho(0)+t \rho(0)+O(\epsilon),(S 1 6 1)$$

which, in the computational basis (i.e. 0,0 $=$ vac , 1,0 $=a †_{1}$ vac , 0,1 $=a †_{2}$ vac , 1,1 $=a †_{1}a †_{2}$ vac ), satisﬁes

$$^{2}|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle$$

1,0 $\rho$($\epsilon$) 0,1 $=Jt$+O(t ). From the separability criteria in Lemma 18, it then follows that there cannot exist a

$$|\langle||\rangle|^{2}$$

separable state $\sigma$(t) such that $\rho$(t) $\sigma$(t) O(t ), no matter what the rate $\kappa$ is.

$$∥ − ∥ \le$$

While the analysis above indicates that there would be times when the state $\rho$(t) would be entangled, we can also analyze the time-scale at which this entanglement is developed. In Fig. S3, we simulate the two-fermionic-mode model from Proposition 1 for $\kappa_{1}=\kappa_{2}=\kappa$ and numerically compute the entanglement measure E($\rho$) $^{=}^{′}^{′}^{\rho}b$,b′ (i.e.,

$$b,b:b=b$$

$$^{̸}||$$

the 1-norm of a vector formed with the oﬀ-diagonal elements of $\rho$) as a function of t. Note that from Lemma 18, this measure quantiﬁed how non-separable the two-mode state is when considering all observables. We observe that this measure becomes 0 at long times, however it is largest at time t∗ 1/$\kappa$ — thus consistent with the analysis of Proposition 1, even at large $\kappa$, the fermionic state becomes entangled at short times and, unlike the bosonic model, does not exhibit a threshold behavior of transitioning to an always separable state at suﬃciently large $\kappa$.

$\sum=J$ . Simulation

$$^{s}\sum=2 J^{t}_{\sum}° 1$$

Fit with

$$\sum=5 J$$

$$_{t}\sum=1 0 J$$

0 1 2 3 4 5 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0

$$^{T}^{i}^{m}^{e}^{J}^{t}De ca yr at e^{\sum}/J$$

FIG. S3. Numerical simulation of the two-fermionic-mode model considered in Proposition 1 with both particle loss rat$e \kappa^{1}$ and particle gain rate $\kappa 2$ set to $\kappa$ and $\rho$(0) $=a$1|va$c \rangle \langle v$ac|a1. (a) Time evolution of the entanglement measure computed by adding all oﬀ-diagonal elements of the two-mode density matrix of the model. As per Lemma 18, this quantiﬁes non-separability with respect to all observables for 2-mode fermionic systems. (b) The time t at which the entanglement measure computed in (a) is maximum as a function of $\kappa$. We see that entanglement is developed at time-scales $t \sim 1$/$\kappa$ no matter how large $\kappa$ is. 2. Non-separability for even observables We will use the following lemma, which reduces the problem of checking the non-separability of a 4-mode fermionic state with respect to even observables to an eﬀective problem with 2 qubits. Lemma 19. Suppose $\rho$ is a state of $m=4$ fermionic modes, with sub-system A with modes 1 and 2 and sub-system B with modes 3 and 4, and suppose the 2-qubit state $\sigma=$ (QA,eQB,o)$\rho$(Q† Q† ), where

$$A,eB,o$$

QA,$_{e}=0$A vac + 1A vac a1a2,QB,$_{o}=0$B vac a3+ 1B vac a4,

$$|\rangle \langle||\rangle \langle||\rangle \langle||\rangle \langle|$$

is entangled, then $\rho$ is not separable with respect to even observables. Proof. This lemma follows by contradiction—let us assume tha$t \rho i$s separable with respect to even observables. Now, for any two operators OA,OB $\times$ , consider the even observables

$$(+)(+)$$

$$O=Q^{†}O_{A}Q_{A}_{,}_{e}an dO=Q^{†}O_{B}Q_{B}_{,}_{o}.$$

$$AA,eB B,o$$

$$(+)(+)$$

Note that O acts on the fermionic modes in A and O acts on the fermionic modes in B. We note also that

$$(+)(+)$$

$$Tr(OO \rho)=Tr(O_{A}O_{B}\sigma).$$

Now, sinc$e \rho i$s separable with respect to even observables by assumption, it follows that $\rho A$,x,$\rho B$,x and a probability measure µ such that

$$(+)(+)(+)(+)$$

$$Tr(OO \rho)=Tr(O \rho_{A}_{,}_{x})Tr(O \rho_{B}_{,}_{x})d µ(x),(S 1 6 4)$$

$$AB AB$$

and consequently, using Eq. (S162), we ﬁnd that

$$Tr(O_{A}O_{B}\sigma)=Tr(O_{A}\sigma_{A}_{,}_{x})Tr(O_{B}\sigma_{B}_{,}_{x})d µ(x),$$

where $\sigma A$,$x=QA$,$e^{\rho}A$,xQ† and $\sigma B$,$x=QB$,$o^{\rho}B$,xQ† . This would imply that $\sigma$ is separable and therefore, by

$$A,eB,o$$

contradiction, we conclude that $\rho$ cannot be separable even with respect to even observables. Proposition 2. Consider a system with $m=4$ fermionic modes, with the sub-system A with modes 1 and 2 and sub-system B with modes 3 and 4, whose density matrix $\rho$(t) satisﬁes the Lindblad master equation

$$\rho(t)=i[J(a_{2}a_{3}+a^{†}_{3}a^{†}_{2}),\rho(t)]+\kappa_{1}_{a}+\kappa_{2}^{†}\rho(t).$$

$$dt − DD^{j}$$

$$j=1$$

$$X(cid:0)(cid:1)$$

Then, $\kappa 1$,$\kappa_{2}>0$, $\rho$(0) which is separable with respect to even observables (Deﬁnition 2) such that $\rho$(t) cannot be separable for all t 0. $\ge$

Proof. Throughout this proof, “separability” refers to separability with respect to even observables (Deﬁnition 2). We choose $\rho$(0) $=\psi$(0) $\psi$(0) , where

$$|\rangle \langle|$$

$$\psi(0)=a^{†}_{1}va c+a^{†}_{4}va c .$$

$$|\rangle \sqrt 2|\rangle|\rangle$$

$$(cid:0)(cid:1)$$

(+) It can be noted that $\rho$(0) is separable with respect to even observables since, for any even observables O on A and (+) O on B,

$$(+)(+)^{1}(1)(+)(1)(1)(+)(1)^{1}(2)(+)(2)(2)(+)(2)$$

$$Tr(\rho(0)OO)=\psi O \psi \psi O \psi+\psi O \psi \psi O \psi,(S 1 6 7)$$

$$AB AA AB BB AA AB BB$$

$$2 \langle||\rangle \langle||\rangle 2 \langle||\rangle \langle||\rangle$$

where $\psi=a^{†}_{1}$ vac , $\psi=$ vac , $\psi=$ vac , and $\psi=a^{†}_{4}$ vac . Again, to show that $\rho$(t) is not separable

$$AB AB$$

$$|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle|\rangle^{2}$$

for all $t>0$, it is enough to show that there isn’t a separable state $\sigma$(t) such that $\rho$(t) $\sigma$(t) O(t ) as t 0.

$$∥ − ∥ \le \to$$

To show this, we consider a ﬁrst-order expansion of $\rho$(t):

$$\rho(t)=\rho(0)+t \rho(0)+O(t)$$

$$=\psi(t)\psi(t)+t \kappa_{1}_{a}(\psi(0)\psi(0))+\kappa_{2}^{†}(\psi(0)\psi(0))+O(t),(S 1 6 8)$$

$$|\rangle \langle|D|\rangle \langle|D^{j}|\rangle \langle|$$

$$j=1$$

$$X(cid:0)(cid:1)$$

where $\psi$(t) $=$ (a†1 + a†4 ita†3a†2a†1 ita†3a†2a†4) vac /$\sqrt 2$. We can now compute the state $\sigma$(t) $=$

$$|\rangle − −|\rangle$$

(QA,eQB,o)$\rho$(t)(Q† Q† ) deﬁned in Lemma 19, which eﬀectively amounts to projecting $\rho$(t) on the subB,o A,e space spanned by a†3 vac ,a†4 vac ,a†3a†2a†1 vac ,a†4a†2a†1 vac and identifying a†3 vac 0A,0B ,a†4 vac

$$\{|\rangle|\rangle|\rangle|\rangle \}|\rangle \to |\rangle|\rangle \to$$

0A,1B ,a†3a†2a†1 vac 1A,0B ,a†4a†2a†1 vac 1A,1B :

$$|\rangle|\rangle \to |\rangle|\rangle \to |\rangle$$

$$\sigma=((1(\kappa_{1}+\kappa_{2})t)0_{A},1_{B}it 1_{A},0_{B})((1(\kappa_{1}+\kappa_{2})t)0_{A},1_{B}+it 1_{A},0_{B})+O(t),(S 1 6 9)$$

$$−|\rangle −|\rangle − \langle|\langle|$$

It is easy to see that $\kappa 1$,$\kappa_{2}>0$, $\sigma$(t) (as a 2-qubit state), does not admit an O(t ) separable approximation for suﬃciently small t. Consequently, from Lemma 19, we ﬁnd that $\rho$(t) (as a 4-mode fermionic state) does not admit an O(t ) separable approximation, thus proving the lemma. To analyze the timescales at which the stat$e \rho$(t) becomes non-separable relative to even observables, in Fig. S4, we numerically simulate the four-fermionic-mode model from Proposition 2 wit$h \kappa_{1}=\kappa_{2}=\kappa a$ndcomput$e \rho$(t). To quantify the extent to whic$h \rho$(t) is non-separable, we ﬁrst construct the eﬀective two-qubit stat$e \sigma$(t) $=Q_{A}$,eQB,$o \rho$(t)Q† Q† B,o A,e from $\rho$(t) deﬁned in Lemma 19 and then compute the minimum eigenvalue of its partial transpose. The negative of this minimum eigenvalue is the entanglement measure shown in in Fig. S4(a). We ﬁnd that, while at long times $\sigma$ has a non-negative partial transpose and is thus separable, at short times $\sigma$ is entangled irrespective of how large $\kappa$ is. Furthermore, the minimum eigenvalue of the partial transpose of $\sigma$ is attained at t∗ 1/$\kappa$ [Fig. S4(b)], which sets the time-scale at which non-separability with respect to even observables in this system is developed. [S1] C. V. Kraus, A quantum information perspective of fermionic quantum many-body systems, Ph.D. thesis, Technische Universita¨t Mu¨nchen (2009). [S2] J. Surace and L. Tagliacozzo, SciPost Phys. Lect. Notes , 54 (2022). [S3] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to algorithms (MIT press, 2022). [S4] M. Fagotti and P. Calabrese, J. Stat. Mech.-Theory E. 2010, P04016 (2010). [S5] B. M. Terhal and D. P. DiVincenzo, Phys. Rev. A 65, 032325 (2002). [S6] E. Knill, arXiv preprint quant-ph/0108033 (2001). [S7] T. Kuwahara, T. V. Vu, and K. Saito, Nat. Commun. 15, 2520 (2024). [S8] K. Noh and C. Chamberland, Phys. Rev. A 101, 012316 (2020). [S9] D. Aharonov and M. Ben-Or, SIAM J. Comput. 38, 1207 (2008). [S10] T. Matsuura, N. C. Menicucci, and H. Yamasaki, arXiv preprint arXiv:2410.12365 (2024). [S11] A. Mari and J. Eisert, Phys. Rev. Lett. 109, 230503 (2012). [S12] R. Hudson, Rep. Math. Phys 6, 249 (1974). [S13] M. Walschaers, PRX Quantum 2, 030204 (2021). [S14] M. Yuan, A. Seif, A. Lingenfelter, D. I. Schuster, A. A. Clerk, and L. Jiang, arXiv preprint arXiv:2312.15783 (2023).

$$^{e}\sum=0 . 1 J^{.}$$

Simulation

$$^{s}\sum=0 . 2 J^{t}_{\sum}° 1$$

Fit with

$$^{e}\sum=0 . 4 J_{e}$$

$$^{t}\sum=0 . 8 J_{i}$$

$$\sum=1 . 6 J^{.}$$

$$_{a}° 0 . 1_{a}$$

E°0.2 0 2 4 6 8 10 0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00

$$^{T}^{i}^{m}^{e}^{J}^{t}De ca yr at e^{\sum}/J$$

FIG. S4. Numerical simulation of the four-mode fermionic model considered in Proposition 2 with both particle loss rate $\kappa 1$ and particle gain rate $\kappa 2$ set to $\kappa$ and |$\psi$(0)$\rangle=$ (a1 +a4)|va$c \rangle$. (a) Time evolution of the entanglement measure computed by ﬁrst computing the two-qubit state $\sigma$(t) corresponding to the 4-mode fermionic state $\rho$(t) from Lemma 19 and then computing (the negative) of the minimum eigenvalue of its partial transpose. As per Lemma 19, this quantiﬁes non-separability with respect to all observables for 2-mode fermionic systems. (b) The time t at which the entanglement measure computed in (a) is maximum as a function of $\kappa$ — we see that entanglement is developed at time-scales $t \sim 1$/$\kappa$ no matter how large $\kappa$ is. [S15] A. Eickbusch, V. Sivak, A. Z. Ding, S. S. Elder, S. R. Jha, J. Venkatraman, B. Royer, S. M. Girvin, R. J. Schoelkopf, and M. H. Devoret, Nat. Phys. 18, 1464 (2022). [S16] A. Lingenfelter, D. Roberts, and A. A. Clerk, Sci. Adv. 7, eabj1916 (2021). [S17] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and R. Vrijen, Proceedings of the National Academy of Sciences 99, [S18] L. J. Schulman and U. V. Vazirani, in Proceedings of the Thirty-First Annual ACM Symposium on Theory of Computing, STOC ’99 (Association for Computing Machinery, New York, NY, USA, 1999) p. 322–329. [S19] A´. M. Alhambra, M. Lostaglio, and C. Perry, Quantum 3, 188 (2019). [S20] M. Ben-Or, D. Gottesman, and A. Hassidim, arXiv preprint arXiv:1301.1995 (2013). [S21] R. Trivedi and J. I. Cirac, Phys. Rev. Lett. 129, 260405 (2022). [S22] O. Shtanko and K. Sharma, arXiv preprint arXiv:2411.04819 (2024). [S23] M.-C. Ban˜uls, J. I. Cirac, and M. M. Wolf, Phys. Rev. A 76, 022311 (2007). [S24] H. Moriya, J. Phys. A-Math. Gen. 39, 3753 (2006).