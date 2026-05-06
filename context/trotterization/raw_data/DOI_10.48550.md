Dynamical complexity of non-Gaussian many-body systems with dissipation

Guillermo Gonz´alez-Garc´ıa1,2, Alexey V. Gorshkov3,4, J. Ignacio Cirac1,2, and Rahul Trivedi1,2∗
1Max-Planck-Institut f¨ur Quantenoptik, Hans-Kopfermann-Str. 1, 85748 Garching, Germany
2Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, D-80799 Munich, Germany
3Joint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA.
4Joint Center for Quantum Information and Computer Science,
NIST/University of Maryland, College Park, Maryland 20742, USA.
(Dated: October 21, 2025)

We characterize the dynamical state of many-body bosonic and fermionic many-body models with
inter-site Gaussian couplings, on-site non-Gaussian interactions and local dissipation comprising in-
coherent particle loss, particle gain, and dephasing. We ﬁrst establish that, for fermionic systems,
if the dephasing noise is larger than the non-Gaussian interactions, irrespective of the Gaussian
coupling strength, the system state is a convex combination of Gaussian states at all times. Fur-
thermore, for bosonic systems, we show that if the particle loss and particle gain rates are larger
than the Gaussian inter-site couplings, the system remains in a separable state at all times. Building
on this characterization, we establish that at noise rates above a threshold, there exists a classical
algorithm that can eﬃciently sample from the system state of both the fermionic and bosonic mod-
els. Finally, we show that, unlike fermionic systems, bosonic systems can evolve into states that are
not convex-Gaussian even when the dissipation is much higher than the on-site non-Gaussianity.
Similarly, unlike bosonic systems, fermionic systems can generate entanglement even with noise rates
much larger than the inter-site couplings.

Introduction. Whether many-body quantum systems
evolve into classically non-trivial states under decoher-
ence is of fundamental interest to the theory of open
quantum systems and also has implications for the quan-
tum advantage in quantum computers and simulators [1–
6]. Traditionally, this has been mostly studied for many-
body spin models, including extensive recent activity in
both the discrete-time setting (i.e. quantum circuits in-
terspersed with noise) and in the continuous-time set-
ting (modeled by a many-body Lindblad master equation
[7, 8]). For discrete-time models, early results showed
that suﬃciently high noise suppresses entanglement thus
enabling classical simulation [9]. Recent results have
shown classical simulability, even with a small amount of
depolarizing noise, for both sampling or computing local
observables in both random [10–19] and structured mod-
els [20–22]. These results have partly been generalized
to the geometrically-local continuous-time setting, which
more accurately models analog quantum simulators, to
show that the system remains classically simulable when
the noise rate is larger than the interaction terms in the
Hamiltonian [8].

Quantum simulators based on platforms such as ultra-
cold atoms in optical lattices [23–27], superconducting
circuits [28, 29] or nonlinear photonics [30–32], are often
described by a family of Hamiltonians that, only in cer-
tain regimes, reduce to spin systems. They are modeled
by a fermionic or bosonic lattice with two kinds of terms:
(i) Gaussian coupling terms which are linear or quadratic
in creation/annihilation operators (e.g. particle hopping
or pair production); (ii) Non-Gaussian interaction terms
that typically act on particles only on one site. Con-

∗ rahul.trivedi@mpq.mpg.de

sequently, there are two relevant frequency scales: the
strength of the Gaussian couplings, J, and that of the on-
site (non-Gaussian) interactions, U . If J = 0 or U = 0,
this model is classically simulable. When J = 0, the
Hamiltonian is a sum of single-site terms which maps
product states to product states which can be classically
simulated. When U = 0, the dynamics is Gaussian and
thus local observables can be eﬃciently computed and,
for fermions, even sampling is eﬃcient [33–36]. How-
ever, when both J, U
= 0 and the system is noiseless,
this model is universal for quantum computation [37, 38]
and thus worst-case hard to simulate classically. While
the presence of dissipation should make the model classi-
cally simulable, the amount and type of local dissipation
needed remains unclear.

For fermionic systems, the impact of noise on non-
Gaussianity was studied in a circuit model with Gaus-
sian gates and non-Gaussian ancillas, which showed that
the state remains a convex combination of Gaussian
states above a noise-threshold[39–41]. Studies analyz-
ing continuous-time dynamics have focused on the non-
Gaussianity introduced via two-body dissipation [7]. For
bosonic systems, previous studies have either focused on
understanding their complexity as a function of evolu-
tion time in the absence of noise [42–44], or for the
speciﬁc task of boson sampling in the presence of noise
[45–49]. However, the classical simulability of the noisy
continuous-time model motivated above remains unre-
solved.

In this Letter, we rigorously address this question—
we consider fermionic and bosonic systems with n sites,
each containing locally L modes (Fig. 1). The annihi-
lation operators corresponding to the σth mode at the
ith site, where σ
, is
1, 2 . . . L
}
given by ai,σ. We will use the Hermitian operators cα
i,σ,

1, 2 . . . n

and i

∈ {

∈ {

}

5
2
0
2

t
c
O
7
1

]
h
p
-
t
n
a
u
q
[

2
v
8
5
6
5
0
.
2
0
5
2
:
v
i
X
r
a

̸

i,σ = (ai,σ + a†

with α
i(ai,σ

, deﬁned as c1
i,σ =
1, 2
∈ {
}
a†
i,σ)/√2, which represent either Majorana op-
−
−
erators (for fermions) or position and momentum quadra-
ture operators (for bosons). The noisy dynamics is de-
scribed by the Lindblad master equation

i,σ)/√2, c2

dρ(t)
dt

=

−

i[H(t), ρ(t)] +

L

Xi,σ

i,σρ(t),

(1)

were H(t) is a (possibly time-dependent) Hamiltonian
describing the system.
i,σ captures the noise, which
is assumed to act locally on every mode (i, σ), and is
modeled by

L

i,σ(

·

L

) =

3

Xl=1

κl

L(l)
i,σ(

)L(l)†

i,σ −

·

(cid:18)

1
2 {

i,σ L(l)
L(l)†

i,σ, (

,

)

·

}(cid:19)

(2)

i,σ, L(3)

i,σ = a†

i,σ = ai,σ, L(2)

with jump operators L(1)
i,σ =
a†
i,σai,σ and decay rates κ1, κ2, κ3 respectively. The jump
operator ai,σ models particle loss, a†
i,σ models incoherent
particle gain, and a†
i,σai,σ models dephasing. We remark
that our conclusions also hold for other physically rele-
vant dissipators such as L(1)
i,σ = c1
i,σ which, in
the bosonic case, would correspond to white noise ﬂuctu-
ations in the quadratures. We use the same noise Lind-
bladian for both bosons and fermions—for the bosonic
case, we will additionally assume that the particle loss
occurs at a rate strictly higher than (both coherent and
incoherent) particle gain (see Supplement [50] for the ex-
act assumption) so as to avoid an unbounded growth of
the number of particles with t which would be unphysical
in an actual experiment.

i,σ, L(2)

i,σ = c2

We will assume that the Hamiltonian can be written
as H(t) = Hg(t)+Hng(t), where Hg(t) contains Gaussian
general intersite terms:

Hg(t) =

Xi,j Xα,α′
σ,σ′

J α,α′
i,σ;j,σ′ (t)cα

i,σcα′

j,σ′ +

Xi,α,σ

Ωα

i;σ(t)cα

i,σ,

(3a)

and Hng(t) contains on-site non-Gaussian terms which
account for particle-particle repulsion and attraction be-
tween diﬀerent modes at the same site:

Hng(t) =

Ui,σ;i,σ′ (t)ni,σni,σ′ .

(3b)

Xi,σ,σ′

Note that in the fermionic case Ωα
i;σ(t) = 0, since phys-
ical Hamiltonians must preserve fermionic parity, while
in the bosonic case Ωα
i;σ(t) can be a non-zero real scalar.
For fermions, we can assume that J α,α′
i,σ;j,σ′ (t) is purely
imaginary and anti-symmetric i.e.

J α,α′
i,σ;j,σ′ (t) =

J α,α′
i,σ;j,σ′ (t)

∗

=

(cid:0)

(cid:1)

J α′,α
j,σ′;i,σ(t),

−

(4)

2

FIG. 1. Sketch of the model, with n sites on a lattice, where
each site contains L modes. There are Gaussian couplings
between the diﬀerent sites, while the non-Gaussian interac-
tions are only onsite. Nonlocal couplings are allowed. In the
bosonic case, interactions of the form n2

i,σ are also allowed.

while for bosons it can be assumed to be purely real and
symmetric:

i,σ;j,σ′ (t) = J α′,α
J α,α′

j,σ′;i,σ(t).

(5)

The non-Gaussian onsite interactions Ui,σ;i,σ′ (t) can be
assumed to be real and symmetric for both fermions and
bosons.

We also deﬁne the parameters J, Ω, U as the smallest
constants such that for every mode (i, σ) and all times t

Xj̸=i,σ′ Xα,α′ |

J α,α′
i,σ;j,σ′ (t)

J,

| ≤

Xα |

Ωα

i;σ(t)

| ≤

Ω and

Ui,σ;i,σ′ (t)

U.

| ≤

|

Xσ′

(6)

the Gaussian coupling
The parameter J captures
strength between a mode and the modes at all other sites,
U captures the on-site non-Gaussian interaction strength,
and Ω captures the coherent drive at each site. We will
also assume that J, U , and Ω are O(1) constants, which is
true in most physical models. Finally, we remark that we
do not need to assume geometrical locality of the model—
our results will apply to geometrically local and non-local
models.

The initial state ρ(0) is either a product state (when
analyzing entanglement), a Gaussian state (when analyz-
ing non-Gaussianity), or both (e.g., the vacuum state).
In the bosonic case, additionally, ρ(0) will be assumed
C k
to satisfy Tr(nk
∈
, and for some C0, α0, β0 > 0: this condition guar-
1, 2...
}
{
antees that the probability of ﬁnding
k particles in a
mode decreases super-polynomially with k, as would be
expected in a physically preparable bosonic state [51].

0 kα0k+β0 ,

i,σρ(0))

(i, σ),

for k

≤

≥

∀

Results: Our results, depicted in Fig. 2, show the simu-
lability of the fermionic and bosonic models as a function
of J, U, κi. We ﬁrst establish that when the noise rate is
larger than the on-site non-Gaussian interaction strength

3

coupling, ρ(t) remains separable at all times, and can
therefore be classically eﬃciently sampled from in the
Fock state basis.

Theorem 2. Suppose ρ(t) is the state obtained after
evolving the bosonic model for time t with an initial prod-
2J the state ρ(t) is separable
uct state, then for κ1, κ2 ≥
0. Furthermore, there is a randomized classi-
for all t
cal algorithm that can sample ρ(t) in the Fock state basis
to ϵ total variation error in poly(n, t, 1/ϵ) time.

≥

Our result formalizes the intuition that, when noise ex-
ceeds the inter-site coupling strength, a buildup of en-
tanglement is prohibited and no classically non-trivial
state is generated. Notably, the noise threshold is de-
termined by particle loss and gain noise. This arises
from the dephasing dissipator being diagonal in the Fock
basis, while evolution under Hg(t) creates entanglement
through oﬀ-diagonal elements (i.e., coherences). Thus, to
ﬁrst order, dephasing cannot counter this entanglement
generation. Particle gain or loss dissipators, however,
are not diagonal in the Fock basis and can prevent it. In
the Supplement, we also extend Theorem 2 to quantum
spin models with single spin noise and bosonic models
with inter-site non-Gaussian couplings [50]. Unlike pre-
vious percolation-based arguments limiting entanglement
to O(log n) qubit clusters for suﬃciently strong noise
[8, 9], we show that the state is entirely separable, and
provide an explicit construction that can be eﬃciently
sampled from.

A detailed proof of Theorem 2 is provided in the Sup-
plement [50]. Similar to Theorem 1, we begin by a ﬁrst-
order Trotterization of the model but with a diﬀerent
decomposition of the Lindbladian: We express it as a
product of (a) single site gates, which contain the unitary
generated by Hng(t), single-site terms in Hg(t) and the
dephasing dissipator and (b) two-site channels which con-
tain the unitary generated by the inter-site terms in Hg(t)
paired together with the particle gain and loss dissipators
[Fig. 4]. We denote the channel acting between modes
(i, σ) and (j, σ′) at the Trotter-step τ as Φi,σ;j,σ′
τ δ,(τ −1)δ, where
δ is the size of the Trotter-step. Importantly, the Trot-
terization is performed in such a way that the channel
Φi,σ;j,σ′
τ δ,(τ −1)δ can be understood as a time evolution of the
inter-site Gaussian couplings between modes (i, σ) and
(j, σ′), followed by noise on both modes. This eﬀectively
redistributes the single-site noise into “gate-based” noise
on the inter-site gates. Analyzing Φi,σ;j,σ′
τ δ,(τ −1)δ, we show
2J, it is separability-preserving and thus
that for κ1, κ2 ≥
the state remains separable at all times. Furthermore, we
also explicitly construct an O(δ2) approximation to the
separable state after each time-step and obtain an ex-
plicit algorithm to sample from ρ(t).

Tightness of Theorems 1 and 2. We can now ask if
a version of Theorem 1 holds for bosonic systems i.e.,
is there a noise threshold κth(U ) dependent only on the
non-Gaussian strength U and uniform in J, Ω that guar-
antees a convex-Gaussian at all times? For dephasing

FIG. 2. Phase diagram for both bosonic and fermionic sys-
tems in the presence of generic noise. (a) For fermionic system
the state remains convex-Gaussian at all times for error rates
κ3 ≥ 2U . (b) In bosonic systems the state remains separable
at all times for error rates κ1, κ2 ≥ 2J.

U , the fermionic model remains convex-Gaussian at all
times, and can therefore be classically eﬃciently sampled
from.
Theorem 1. For an initial Gaussian state, if κ3 ≥
2U ,
then the state of the fermionic model at time t, ρ(t), is
a convex combination of Gaussian states for all t
0.
Furthermore, ρ(t) can be classically sampled in the Fock
state basis to an ϵ total variation error in poly(n, t, 1/ϵ)
time.

≥

2U ,
Physically Theorem 1 suggests that when κ3 ≥
dephasing noise destroys non-Gaussianity faster than
Hng(t) creates it, so that ρ(t) always remains convex-
Gaussian.
Since Hg(t) preserves convex-Gaussianity,
the noise threshold in Theorem 1 is independent of J.
Notably,
it is dephasing that results in this convex-
Gaussianity. With only incoherent particle loss/gain,
ρ(t) could evolve into a non-Gaussian state at short
times even with large dissipation. This arises from the
fermionic parity structure—the density matrix of the
fermionic model has the form ρ(t) = ρ+(t) + ρ−(t),
where ρ±(t) is supported only on even/odd parity states.
Due to this structure, convex-Gaussianity in ρ(t) requires
both ρ±(t) to be convex-Gaussian [40]. Hng(t) generates
non-Gaussianity individually in both ρ±(t). However,
the loss/gain dissipators, to ﬁrst order, switch the parity
of the state and do not act within the two parity sub-
spaces. Consequently, they cannot immediately counter
the non-convex-Gaussianity created by Hng(t).

We provide a complete proof of Theorem 1 in the
supplement: The starting point is a Trotterization of
the Lindbladian in Eq. 1 — in each Trotter step, we
express the evolution as (a) a Gaussian unitary corre-
sponding to Hg(t), particle loss and gain followed by (b)
the single-site channels generated by Hng(t) and dephas-
ing (Fig. 3). Analyzing the single-site channel, we show
2U , this channel maps an input convex-
that for κ3 ≥
Gaussian state to a convex-Gaussian state. Furthermore,
we explicitly construct the output convex-Gaussian state,
which allows us to sample from it [35, 52].

Next, we consider the bosonic model and establish that
when the noise rate is larger than the inter-site Gaussian

4

FIG. 3. Schematic depiction of the Trotterization schemes in the proof of Theorem 1 (fermionic systems with weak non-
Gaussianity). For simplicity, we only depict a 1D setting, with each site containing 3 modes (L = 3). A single Trotter step
consists of a Gaussian channel (orange rectangles) that includes the combined eﬀect of Hg(t) and the particle gain and loss
dissipators, followed by non-Gaussian gates (blue rectangles) interspersed with the dephasing dissipator (gray curved rectangles).
Crucially, a non-Gaussian gate followed by suﬃciently strong dephasing can be written as a convex combination of Gaussian
channels.

FIG. 4. Schematic depiction of the Trotterization schemes in the proof of Theorem 2 (bosonic systems with weak inter-site
couplings). For simplicity, we only depict a 1D setting, with each site containing 3 modes (L = 3). A single Trotter step
consists of a layer of single-site channels which include the Hamiltonian terms acting on that site and the dephasing dissipator,
followed by 2-site gates interspersed with particle gain and loss dissipators (in gray circles). Crucially, a 2-site gate followed by
suﬃciently strong noise can be written as a convex combination of single-site channels

noise, we provide numerical evidence to the contrary:
U , single-mode dynamics can yield states
even for κ3 ≫
with negative Wigner function, and thus not convex-
Gaussian states can be generated at time-scales
1/U
[50, 53]. While negativity of the Wigner function suggests
classical simulation hardness [53, 54], we do not rule out
the existence of an eﬃcient classical algorithm. When
κ3 = 0, in the Supplement we show that no matter how
small U is relative to κ1, κ2, computing expected local
particle numbers is BQP-hard if J, Ω can be arbitrar-
ily large but O(1) [50]. This builds upon Refs. [55, 56]
which perform a universal gate-set on a single bosonic

∼

mode with an arbitrarily small eﬀective gate-error rate
by engineering the displacement and squeezing. We ex-
tend this technique to also implement an entangling gate
between two oscillators thus yielding a high-ﬁdelity uni-
versal multi-mode gate-set. Together with results from
Ref. [57], this suggests that when the noise is non-unital
= κ2), by using suﬃciently large J and Ω, a
(i.e. κ1 ̸
fault-tolerant quantum computation can be encoded into
the model [58–60]. Thus, it is unlikely to be able to
classically compute even local observables in this setting
unless BQP = BPP.

Finally, we consider if a version of Theorem 2 holds

for fermions i.e., do noise rates larger than the Gaussian
inter-site couplings result in separability at all times. We
answer this question in the negative: in the Supplement
we show by analyzing few-mode fermionic models that,
in contrast with bosons, no matter how high κ2, κ3 are,
the system does not remain separable at all times and can
3 ). In
exhibit entanglement at time-scales
fact, this short-time non-separability holds not only if
we consider separability with respect to all observables
[61], but also if we consider a weaker notion of separa-
bility with respect to only parity-conserving observables
[62]. However, this result does not rule out separability
at longer times or other routes to classical simulation.

min(κ−1

2 , κ−1

∼

5

lenge in experimentally verifying the threshold behavior
predicted by Theorems 1 and 2 would be verifying the
presence (or absence) of entanglement/non-Gaussianity
in ρ(t). While this could be hard to do for large systems,
we remark that the diﬀerence in the threshold behavior
in fermionic and bosonic models that we described can be
4) fermionic
understood even with systems with few (
or bosonic modes, which is well within the regime where
a full state tomography can already be performed.

≤

ACKNOWLEDGMENTS

Conclusion and outlook. We have characterized the
classical complexity of simulating the continuous-time
evolution of fermionic and bosonic systems as a func-
tion of the noise, Gaussian and non-Gaussian interaction
strengths. Future theoretical directions include the study
extending our results to non-Markovian models of dissi-
pation.

The models considered in this paper can be experimen-
tally realised in several platforms. The bosonic model
can be implemented in superconducting systems where
the Gaussian Hamiltonian can be controlled by design-
ing capacitive couplings between diﬀerent qubits and the
single-site non-Gaussianity by the nonlinear Josephson
potential in the qubit [28, 29]. We can also use cold
bosonic atoms in optical lattices where the strength of
both the Gaussian and the non-Gaussian Hamiltonians
can be controlled by tuning the optical lattice potential
[26, 27]. The fermionic model can be implemented either
with cold atoms in optical lattices by using a fermionic
species of atoms [23–25], or in solid-state systems such
Moir´e superlattices hosting trions [63–65]. Since all of
these systems will have intrinsic particle loss, gain, and
dephasing, tuning the parameters in the Gaussian and
non-Gaussian Hamiltonians could allow us to access the
parameter regimes in Theorems 1 and 2. A major chal-

We thank Ashish Clerk and Liang Jiang for useful
discussions and Peter McMahon for discussions that in-
spired this project. R.T acknowledges support from Cen-
ter for Integration of Modern Optoelectronic Materials
on Demand (IMOD) seed grant (DMR-2019444). This
research was supported in part by grant NSF PHY-
2309135 to the Kavli Institute for Theoretical Physics
(KITP). The research is part of the Munich Quantum
Valley, which is supported by the Bavarian State Gov-
ernment with funds from the High tech Agenda Bay-
ern Plus. J.I.C, R.T, G.G.G acknowledge funding from
the project FermiQP of the Bildungsministerium f¨ur
Bildung und Forschung (BMBF). A.V.G. acknowledges
support from the U.S. Department of Energy, Oﬃce
of Science, Accelerated Research in Quantum Comput-
ing, Fundamental Algorithmic Research toward Quan-
tum Utility (FAR-Qu). A.V.G. was also supported in
part by NSF QLCI (award No. OMA-2120757), DoE
ASCR Quantum Testbed Pathﬁnder program (awards
No. DE-SC0019040 and No. DE-SC0024220), NSF STAQ
program, AFOSR MURI, DARPA SAVaNT ADVENT,
and NQVL:QSTD:Pilot:FTL. A.V.G. also acknowledges
support from the U.S. Department of Energy, Oﬃce
of Science, National Quantum Information Science Re-
search Centers, Quantum Systems Accelerator.

[1] J. Preskill, Quantum 2, 79 (2018).
[2] A. J. Daley, I. Bloch, C. Kokail, S. Flannigan, N. Pearson,
M. Troyer, and P. Zoller, Nature 607, 667 (2022).
[3] S. Ebadi, T. T. Wang, H. Levine, A. Keesling, G. Se-
meghini, A. Omran, D. Bluvstein, R. Samajdar, H. Pich-
ler, W. W. Ho, et al., Nature 595, 227 (2021).

[4] P. Scholl, M. Schuler, H. J. Williams, A. A. Eberharter,
D. Barredo, K.-N. Schymik, V. Lienhard, L.-P. Henry,
T. C. Lang, T. Lahaye, et al., Nature 595, 233 (2021).
[5] D. Wei, A. Rubio-Abadal, B. Ye, F. Machado, J. Kemp,
K. Srakaew, S. Hollerith, J. Rui, S. Gopalakrishnan,
N. Y. Yao, I. Bloch, and J. Zeiher, Science 376, 716
(2022).

[6] G. Semeghini, H. Levine, A. Keesling, S. Ebadi, T. T.
Wang, D. Bluvstein, R. Verresen, H. Pichler, M. Kali-
nowski, R. Samajdar, A. Omran, S. Sachdev, A. Vish-
wanath, M. Greiner, V. Vuleti´c, and M. D. Lukin, Sci-
ence 374, 1242 (2021).

[7] O. Shtanko, A. Deshpande, P. S. Julienne, and A. V.

Gorshkov, PRX Quantum 2, 030350 (2021).

[8] R. Trivedi and J. I. Cirac, Phys. Rev. Lett. 129, 260405

(2022).

[9] D. Aharonov, Phys. Rev. A 62, 062311 (2000).
[10] D. Aharonov, X. Gao, Z. Landau, Y. Liu, and U. Vazi-
rani, in Proceedings of the 55th Annual ACM Symposium
on Theory of Computing, STOC ’23 (ACM, 2023).
[11] J. Tindall, M. Fishman, M. Stoudenmire, and D. Sels,

arXiv preprint arXiv:2306.14887 (2023).

[12] K. Kechedzhi, S. Isakov, S. Mandr`a, B. Villalonga, X. Mi,
S. Boixo, and V. Smelyanskiy, Future Gener. Comput.
Syst. 153, 431 (2024).

[13] Y. Shao, F. Wei, S. Cheng, and Z. Liu, Phys. Rev. Lett.

133, 120603 (2024).

[14] E. Fontana, M. S. Rudolph, R. Duncan, I. Rungger, and
C. Cˆırstoiu, arXiv preprint arXiv:2306.05400 (2023).
[15] M. S. Rudolph, E. Fontana, Z. Holmes, and L. Cincio,

arXiv preprint arXiv:2308.09109 (2023).

J. of Phys. 21, 055003 (2019).

[16] X. Gao and L. Duan, arXiv preprint arXiv:1810.03176

[45] C. Oh, L. Jiang,

and B. Feﬀerman, arXiv preprint

6

(2018).

[17] H.-J. Liao, K. Wang, Z.-S. Zhou, P. Zhang, and T. Xiang,

arXiv preprint arXiv:2308.03082 (2023).

[18] G. Gonz´alez-Garc´ıa, R. Trivedi, and J. I. Cirac, PRX

Quantum 3, 040326 (2022).
[19] T. Schuster, C. Yin, X. Gao,

and N. Y. Yao, arXiv

preprint arXiv:2407.12768 (2024).

[20] G. Gonz´alez-Garc´ıa, J. I. Cirac, and R. Trivedi, arXiv

preprint arXiv:2407.16068 (2024).

[21] J. Rajakumar, J. D. Watson, and Y.-K. Liu, in Proceed-
ings of the 2025 Annual ACM-SIAM Symposium on Dis-
crete Algorithms (SODA) (SIAM, 2025) pp. 1037–1056.
and R. Trivedi, PRX

[22] S. D. Mishra, M. Fr´ıas-P´erez,
Quantum 5, 020317 (2024).

[23] Z. Z. Yan, B. M. Spar, M. L. Prichard, S. Chi, H.-T. Wei,
E. Ibarra-Garc´ıa-Padilla, K. R. A. Hazzard, and W. S.
Bakr, Phys. Rev. Lett. 129, 123201 (2022).

[24] B. M. Spar, E. Guardado-Sanchez, S. Chi, Z. Z. Yan,
and W. S. Bakr, Phys. Rev. Lett. 128, 223202 (2022).
[25] M. A. Norcia, A. W. Young, and A. M. Kaufman, Phys.

Rev. X 8, 041054 (2018).

[26] C. Gross and I. Bloch, Science 357, 995 (2017).
[27] B. Yang, H. Sun, R. Ott, H.-Y. Wang, T. V. Zache, J. C.
Halimeh, Z.-S. Yuan, P. Hauke, and J.-W. Pan, Nature
587, 392 (2020).

[28] X. Zhang, E. Kim, D. K. Mark, S. Choi, and O. Painter,

Science 379, 278 (2023).

[29] Y.-H. Shi, Z.-H. Sun, Y.-Y. Wang, Z.-A. Wang, Y.-R.
Zhang, W.-G. Ma, H.-T. Liu, K. Zhao, J.-C. Song, G.-H.
Liang, et al., Nat. Commun. 15, 7573 (2024).

[30] A. Saxena, A. Manna, R. Trivedi, and A. Majumdar,

Nat. Commun. 14, 5260 (2023).

[31] D. E. Chang, V. Vuleti´c, and M. D. Lukin, Nat. Pho-

tonics 8, 685 (2014).

[32] C. Noh and D. G. Angelakis, Rep. Prog. Phys. 80, 016401

(2016).

[33] S. Bravyi and R. K¨onig, Quantum Info. Comput. 12,

925–943 (2012).

[34] S. D. Bartlett, B. C. Sanders, S. L. Braunstein, and

K. Nemoto, Phys. Rev. Lett. 88, 097904 (2002).

[35] B. M. Terhal and D. P. DiVincenzo, Phys. Rev. A 65,

032325 (2002).

[36] L. G. Valiant, in Proceedings of the thirty-third annual
ACM symposium on Theory of computing (2001) pp.
114–123.

[37] S. B. Bravyi and A. Y. Kitaev, Ann. Phys. 298, 210

(2002).

[38] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82, 1784

(1999).

[39] F. de Melo, P. ´Cwikli´nski, and B. M. Terhal, New. J.

Phys. 15, 013015 (2013).

[40] M. Oszmaniec, J. Gutt, and M. Ku´s, Phys. Rev. A 90,

020302 (2014).

[41] S. Bravyi, Phys. Rev. A 73, 042313 (2006).
[42] N. Maskara, A. Deshpande, A. Ehrenberg, M. C. Tran,
B. Feﬀerman, and A. V. Gorshkov, Phys. Rev. Lett. 129,
150604 (2022).

[43] A. Deshpande, B. Feﬀerman, M. C. Tran, M. Foss-
Feig, and A. V. Gorshkov, Phys. Rev. Lett. 121, 030501
(2018).

[44] G. Muraleedharan, A. Miyake, and I. H. Deutsch, New.

arXiv:2301.11532 (2023).

[46] H. Qi, D. J. Brod, N. Quesada, and R. Garc´ıa-Patr´on,

Phys. Rev. Lett. 124, 100502 (2020).
[47] V. Shchesnovich, Quantum 5, 423 (2021).
[48] H.-S. Zhong, H. Wang, Y.-H. Deng, M.-C. Chen, L.-C.
Peng, Y.-H. Luo, J. Qin, D. Wu, X. Ding, Y. Hu, P. Hu,
X.-Y. Yang, W.-J. Zhang, H. Li, Y. Li, X. Jiang, L. Gan,
G. Yang, L. You, Z. Wang, L. Li, N.-L. Liu, C.-Y. Lu,
and J.-W. Pan, Science 370, 1460 (2020).

[49] L. S. Madsen, F. Laudenbach, M. F. Askarani, F. Rortais,
T. Vincent, J. F. Bulmer, F. M. Miatto, L. Neuhaus,
L. G. Helt, M. J. Collins, et al., Nature 606, 75 (2022).
[50] See supplemental material for a detailed proof of the the-

orems, which includes Refs. [66-76].

[51] T. Kuwahara, T. V. Vu, and K. Saito, Nat. Commun.

15, 2520 (2024).

[52] E. Knill, arXiv preprint quant-ph/0108033 (2001).
[53] A. Mari and J. Eisert, Phys. Rev. Lett. 109, 230503

(2012).

[54] C. Cormick, E. F. Galv˜ao, D. Gottesman, J. P. Paz, and
A. O. Pittenger, Phys. Rev. A 73, 012301 (2006).
[55] M. Yuan, A. Seif, A. Lingenfelter, D. I. Schuster, A. A.
Clerk, and L. Jiang, arXiv preprint arXiv:2312.15783
(2023).

[56] A. Eickbusch, V. Sivak, A. Z. Ding, S. S. Elder, S. R. Jha,
J. Venkatraman, B. Royer, S. M. Girvin, R. J. Schoelkopf,
and M. H. Devoret, Nat. Phys. 18, 1464 (2022).

[57] M. Ben-Or, D. Gottesman,

and A. Hassidim, arXiv

preprint arXiv:1301.1995 (2013).

[58] K. Noh and C. Chamberland, Phys. Rev. A 101, 012316

(2020).

[59] T. Matsuura, N. C. Menicucci, and H. Yamasaki, arXiv

preprint arXiv:2410.12365 (2024).

[60] D. Aharonov and M. Ben-Or, SIAM J. Comput. 38, 1207

(2008).

[61] H. Moriya, J. Phys. A-Math. Gen. 39, 3753 (2006).
[62] M.-C. Ba˜nuls, J. I. Cirac, and M. M. Wolf, Phys. Rev.

A 76, 022311 (2007).

[63] E. Liu, E. Barr´e, J. van Baren, M. Wilson, T. Taniguchi,
K. Watanabe, Y.-T. Cui, N. M. Gabor, T. F. Heinz, Y.-
C. Chang, et al., Nature 594, 46 (2021).

[64] X. Wang, J. Zhu, K. L. Seyler, P. Rivera, H. Zheng,
Y. Wang, M. He, T. Taniguchi, K. Watanabe, J. Yan,
et al., Nature Nanotechnology 16, 1208 (2021).

[65] H. Baek, M. Brotons-Gisbert, A. Campbell, V. Vitale,
J. Lischner, K. Watanabe, T. Taniguchi, and B. D. Ger-
ardot, Nature Nanotechnology 16, 1237 (2021).

[66] C. V. Kraus, A quantum information perspective of
fermionic quantum many-body systems, Ph.D. thesis,
Technische Universit¨at M¨unchen (2009).

[67] J. Surace and L. Tagliacozzo, SciPost Phys. Lect. Notes

, 54 (2022).

[68] T. H. Cormen, C. E. Leiserson, R. L. Rivest,

and
C. Stein, Introduction to algorithms (MIT press, 2022).
[69] M. Fagotti and P. Calabrese, J. Stat. Mech.-Theory E.

2010, P04016 (2010).

[70] R. Hudson, Rep. Math. Phys 6, 249 (1974).
[71] M. Walschaers, PRX Quantum 2, 030204 (2021).
[72] A. Lingenfelter, D. Roberts, and A. A. Clerk, Sci. Adv.

7, eabj1916 (2021).

[73] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and
R. Vrijen, Proceedings of the National Academy of Sci-

ences 99, 3388 (2002).

[74] L. J. Schulman and U. V. Vazirani, in Proceedings of
the Thirty-First Annual ACM Symposium on Theory of
Computing, STOC ’99 (Association for Computing Ma-
chinery, New York, NY, USA, 1999) p. 322–329.

[75] ´A. M. Alhambra, M. Lostaglio, and C. Perry, Quantum

[76] O.

3, 188 (2019).
Shtanko

and K.
arXiv:2411.04819 (2024).

Sharma,

arXiv

preprint

[77] https://github.com/guillegg10/Separability_

Wigner-negativity, GitHub repository.

7

Supplemental material to
“Dynamical complexity of non-Gaussian many-body systems with dissipation”

Guillermo Gonz´alez-Garc´ıa1,2, Alexey V. Gorshkov3,4, J. Ignacio Cirac1,2, and Rahul Trivedi1,2
1Max-Planck-Institut f¨ur Quantenoptik, Hans-Kopfermann-Str. 1, 85748 Garching, Germany
2Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, D-80799 Munich, Germany
3Joint Quantum Institute, NIST/University of Maryland, College Park, Maryland 20742, USA.
4Joint Center for Quantum Information and Computer Science,
NIST/University of Maryland, College Park, Maryland 20742, USA.
(Dated: October 21, 2025)

∗

This Supplemental Material is organized as follows: First, in section I, we provide the necessary notation and
background for the rest of the Supplemental Material. In section II, we provide the proof of Theorem 1, showing
convex-Gaussianity and simulability for the fermionic model for suﬃciently high noise rates. Then, in section III, we
prove Theorem 2 for the bosonic model, which implies separability and simulability for suﬃciently high noise rates. In
section IV, we extend this result to a class of spin models: for 2-local Hamiltonians and suﬃciently high noise rates,
the system can be shown to be separable at all times. Finally, in section V, we show that an analogue of Theorem 1
cannot exist for bosonic systems, and that an analogue of Theorem 2 cannot exist for fermionic systems.

I. NOTATION AND PRELIMINARIES

In this section, we provide the necessary notation and background for the rest of the Supplemental Material. This
includes the notation regarding operators and norms (subsection I A), a brief summary on several properties of bosonic
and fermionic systems (subsection I B), the Trotter formula that will be used throughout the proofs (subsection I C),
the asymptotic notation that we will employ (subsection I D), and a detailed presentation of the bosonic and fermionic
models that we will analyze (subsection I E).

A. Operators, superoperators and their norms

∥p =
A
∥

i

(cid:18) X
= σ1(A) =

For a quantum state

,
denote its Schatten-p norm:

ψ

⟩

|

ψ

∥|

⟩∥

σp
i (A)

will denote its usual norm

2 =

ψ

∥|

⟩∥

ψ

ψ

|

⟨

⟩

. For an operator A, we will use

A
∥

∥p to

1/p

(cid:19)

, where σ1(A)

σ2(A)

≥

≥

σ3(A) . . . are the singular values of A.

(S1)

We will often use
A
∥∞
Frobenius norm. We will often use the Holder’s inequality, which states that

to denote its operator norm and

A
∥
∥

A

∥

∥

∥F =

A

∥2 = [Tr(A†A)]1/2 to denote its

∥

AB
∥

A

∥1 ≤ ∥

∥p ∥

B

∥q where

1
p

+

1
q

= 1.

(S2)

In particular,
∥1 ≤ ∥
ω is a positive semi-deﬁnite operator, then

AB

∥ ∥

B

A

∥

∥1. It is also convenient to note the Cauchy-Schwarz inequality for operators: Suppose

For super-operators
super-operators of the form

A

, we will use

Tr(A†Bω)

2

≤

Tr(A†Aω)Tr(B†Bω).

(S3)

(cid:12)
(cid:12)
∥A∥⋄

to denote its diamond norm.

(cid:12)
(cid:12)

In our analysis, we will often encounter

A

(ρ) =

AiρBi,

i
X

(S4)

∗ rahul.trivedi@mpq.mpg.de

where Ai and Bi are some operators. For such super-operators, it is convenient to note that the Holder’s inequality
implies that

2

Ai∥ ∥

Bi∥

∥

.

∥A∥⋄ ≤

i
X

For instance, given an operator L, we will often use

DL to denote the following superoperator:

DL = LρL†

−

1
2 {

L†L, ρ
}

,

(S5)

(S6)

where
From Eq. (S5), we then obtain that

· }

{ ·

,

is the anti-commutator between two operators.

DL will be called the “dissipator corresponding to L”.

A super-operator

E

∥DL∥⋄ ≤ ∥

L

2 +
∥

L†L

2

L

2 .
∥

∥

≤

is completely positive if and only if it can be expressed as

(cid:13)
(cid:13)

(cid:13)
(cid:13)
KiρK †i

(ρ) =

E

i
X

for some operators Ki. It will be called a channel if it is additionally trace preserving which requires
,
For any completely-positive trace preserving map

1.

E

∥E∥⋄ ≤

B. Fermions and Bosons

(S7)

(S8)

i K †i Ki = I.

P

The Hilbert space of m fermionic modes is described by the vacuum state

and the standard creation (a†i )
labeling the fermionic mode. These satisfy the canonical

vac

⟩

|

and annihilation (ai) operators, with i
anticommutation relations:

1, 2,

∈ {

m

}

· · ·

ai, aj}
{
The Hilbert space of the fermionic model is the ﬁnite-dimensional vector space given by span

ai, a†j}

= 0 and

= δi,j.

{

0, 1
{

}}

. It will be convenient to work with the 2m Majorana fermion operators deﬁned by

(S9)

m
k=1(a†k)µk

vac

: µk ∈

⟩

|

{
Q

(S10)

c1
i =

1
√2

a†i + ai

and c2

i =

(cid:0)

(cid:1)

i
√2

a†i −
(cid:0)
i , cα′
cα
i′
{

ai

.

(cid:1)

}

Q

m
i=1

i ∈ {

0, 1
}

2
α=1(cα

i , where µα

Given a fermionic state ρ, its correlation matrix elements are deﬁned by Γα,α′

C2m as the algebra
= δi,i′ δσ,σ′ . We deﬁne
The Majorana operators are each Hermitian, traceless and satisfy
generated by the 2m Majorana operators: An operator X
∈ C2m can be expressed as a linear combination of monomials
i )µα
of the form
. The operator X will be even if it is a linear combination of only
even degree monomials, and odd if it is a linear combination of odd degree monomials. Furthermore, any Hermitian
Q
operator deﬁned on the fermionic Hilbert space is also in
C2m and, as usual, fermionic quantum states are positive
semi-deﬁnite Hermitian operators in
i , cα′
i,i′ = itr(ρ[cα
i′ ])/2. A fermionic
βH)) for some Hermitian operator H that
state ρ is called Gaussian if it can be expressed as exp(
is quadratic in the Majorana operators and β
. Thus, fermionic Gaussian states are either Gibb’s
states of Hamiltonians that are quadratic in the Majorana operators, or are projectors on their ground-state subspace.
Fermionic Gaussian states are fully characterized by their correlation matrix elements Γα,α′
[S1, S2]. We will refer to
i,i′
a fermionic state as convex-Gaussian if it can be expressed as a convex combination of Gaussian states.
Similar to fermions, the Hilbert space of m bosonic modes will be described by a vacuum state

βH)/Tr(exp(
,

−
∪ {−∞

C2m.

∞}

vac

−

R

∈

and the
labeling the bosonic mode. These satisfy the

⟩

|

creation (a†i ) and annihilation (ai) operators, with i
canonical commutation relations:

∈ {

1, 2 . . . m

}

The Hilbert space of the bosonic model is the inﬁnite-dimensional vector space given by span
0, 1, 2 . . .
{

. It will be convenient to work with the 2m quadrature operators

}}

[ai, ai′ ] = 0 and [ai, a†i′ ] = δi,i′ .

c1
i =

1
√2

a†i + ai

and c2

i =

(cid:0)

(cid:1)

i
√2

a†i −

ai

.

(cid:0)

(cid:1)

(S11)

i(a†i )µi

vac

: µi ∈

⟩

|

{
Q

(S12)

The quadrature operators are Hermitian and satisfy [cα
2 symplectic matrix.
Similar to a fermionic state, a bosonic state ρ is Gaussian if it can be expressed as exp(
βH)) for some
. A
Hermitian operator H which is quadratic or linear in the quadrature operators and for some β
,
state will be called convex-Gaussian if it can be expressed as a convex combination of Gaussians. A useful property
of Gaussian states that we will use in our analysis is given in the lemma below.

×
βH)/Tr(exp(
R

iδi,i′ Ωα,α′ , where Ω is the 2

−
∪ {−∞

i ] =

∞}

−

−

∈

i , cα′

Lemma 1. Suppose ρ is a (fermionic or bosonic) Gaussian state and A =

then ρ′ = e−

Aρe−

A†

/Tr(e−

Aρe−

A†

) is also a Gaussian state.

P

i,i′ Aα,α′

i,i′ cα

i cα′
i′

is a quadratic operator,

Proof. This follows from the closure of quadratic and linear operators under commutation, i.e.

3

(1) For fermions, the commutator of any two operators of the form

of the same form.

P
(2) For bosons, the commutator of any two operators of the form

xα,α′
i,i′

, yα

i ∈

C, is again of the same form.

α,α′ xα,α′

i,i′ cα

i cα′

i′ , where xα,α′

i,i′

i,i′

C, is again

∈

P

i,i′

P

P

α,α′ xα,α′

i,i′ cα

i cα′

i′ +

i,α yα

i cα

i , where

P

A†

Aρe−

Since ρ is a Gaussian state, it is expressible as exp(
a possible linear term in cα
i
e−
and 2 above, we obtain that e−
−
possible linear term for bosons. Furthermore, note that since ρ is positive-semideﬁnite, so is e−
valid quantum state.

i with
for bosons. Consequently, using the Baker-Campbell-Hausdorﬀ formula, we obtain that
can be written as a linear combination of A, A†, H and their nested commutators. Consequently, from 1
i with a
and thus is a

βH ′) for some β and H ′ that is also a quadratic form in cα

βH)), where H is a quadratic form in cα

βH)/Tr(exp(

Aρe−

Aρe−

exp(

A†

A†

∝

−

−

C. Trotter formula

In our analysis below, we will often use ﬁrst-order Trotterization for time-dependent models. Given a time-dependent
(M )(t), its ﬁrst-order Trotterization in the time-interval [0, t], with T Trotter

(2)(t)+. . .

(1)(t)+

Lindbladian
steps each of length δ = t/T , will be given by

(t) =

L

L

L

L

Φ =

1

Yτ =T

Φ(1)

τ δ,(τ

−

1)δΦ(2)

τ δ,(τ

−

1)δ . . . Φ(M )

τ δ,(τ

−

1)δ where Φ(j)

τ δ,(τ

1)δ =

−

T

exp

τ δ

(τ

(cid:18) Z

−

1)δ L

(j)(s)ds

.

(cid:19)

(S13)

In Lemma 2 below, we provide an upper bound on the error between the exact evolution
Trotter formula Φ that we will use repeatedly in the following sections.

T

Lemma 2 (Trotter error for bounded Lindbladians). Suppose for any s
then for any T > 0,

≥

0 and j

1, 2 . . . M

∈ {

t

exp

0 L

(cid:18) Z

(s)ds

Φ

−

(cid:19)

t2
T

≤

M

2

.

ℓj

(cid:18)

j=1
X

(cid:19)

⋄

(cid:13)
(cid:13)
(cid:13)
(cid:13)

T

(cid:13)
(cid:13)
(cid:13)
(cid:13)

D. Asymptotic notation

exp(

t
0 L

(s)ds) and the

R
,

}

(j)(s)

∥L

∥⋄ ≤

ℓj,

(S14)

Throughout the paper, we employ the following asymptotic notation commonly used in complexity theory [S3]:

Notation
f (n) = Ω(g(n))
f (n) = O(g(n))
f (n) = Θ(g(n)) ∃k1 > 0, k2 > 0, n0 : ∀n > n0, k1g(n) ≤ f (n) ≤ k2g(n)

Formal deﬁnition
∃k > 0, n0 : ∀n > n0, |f (n)| ≥ kg(n)
∃k > 0, n0 : ∀n > n0, |f (n)| ≤ kg(n)

Informal description
f (n) grows at least as fast as g(n)
f (n) grows no faster than g(n)
f (n) and g(n) grow equally fast

TABLE SI. Table of asymptotic notation used in this paper.

E. Model

4

Here, we brieﬂy recap the fermionic and bosonic models introduced in the main text and streamline the notation.
We will consider a more general setting than the one described in the main text: speciﬁcally, we will allow here for
inter-site non-Gaussian interactions. We recall that we consider systems with n sites, with each site containing L
bosonic or fermionic modes. We will use m = nL to denote the total number of modes in the system. With the σth
mode at the ith site, where σ
, we will associate an annihilation operator ai,σ—it will
be notationally convenient for us to group i, σ into a single index v = (i, σ) and denote the corresponding annihilation
operator by av. Furthermore, corresponding to a mode index v, we will use iv to denote the site the mode is at and
σv to be the local index of the mode. Associated with the mode at v, we will also deﬁne the operators nv, c1
v via

1, 2 . . . L

1, 2 . . . n

v, c2

and i

∈ {

∈ {

}

}

nv = a†vav, c1

v =

av + a†v
√2

and c2

v =

a†v

av −
√2i

.

(S15)

Here, nv is an operator measuring the number of particles in mode v, and c1
fermions) or the quadrature operators (for bosons).

v, c2

v are the Majorana operators (for

As in the main text, the Hamiltonian for the fermionic or bosonic problem will be decomposed as

where Hg(t) is Gaussian given by

H(t) = Hg(t) + Hng(t),

Hg(t) =

Xv,v′

Xα,α′

J α,α′
v,v′ (t)cα

v cα′

v′ +

Ωα

v (t)cα
v ,

v,α
X

with Ωα

v (t) = 0 for fermions, and Hng(t) is non-Gaussian given by

Without loss of generality, we can assume that

Hng(t) =

Uv,v′ (t)nvnv′ .

Xv,v′

(S16)

(S17)

(S18)

For fermions, J α,α′
For bosons, J α,α′
For both fermions and bosons, Uv,v′ (t) is purely real and Uv,v′ (t) = Uv′,v(t).

v,v′ (t) is purely imaginary and J α,α′
v,v′ (t) is purely real and J α,α′

v,v′ (t) = J α′,α

J α′,α
v′,v (t),

v,v′ (t) =

v′,v (t),

−

As in the main text, we will also deﬁne constants JC, Jos, UC, Uos, Ω:

(1) JC is a measure of the strength of the Gaussian terms coupling modes at diﬀerent sites: It is the smallest number

such that

∀

t and v = (i, σ)

J α,α′
i,σ;i′,σ′ (t)

JC.

| ≤

=i,σ′

Xi′:i′

Xα,α′ |

(S19)

(2) Jos is a measure of the strength of the Gaussian terms coupling modes at the same site: It is the smallest number

such that

∀

t and v = (i, σ)

J α,α′
i,σ;i,σ′ (t)

Jos.

| ≤

Xα,α′ |

Xσ′

(S20)

(3) UC is a measure of the strength of the non-Gaussian terms coupling modes at diﬀerent sites: It is the smallest

number such that

t and v = (i, σ)

∀

Ui,σ;i′,σ′ (t)

UC.

| ≤

=i,σ′ |
Xi′

(S21)

(4) Uos is a measure of the strength of the non-Gaussian terms coupling modes at the same site: It is the smallest

number such that

t and v = (i, σ)

∀

Ui,σ;i,σ′ (t)

Uos.

| ≤

Xiσ′ |

(S22)

̸
̸
(5) Ω is a measure of the on-site displacement: it is the smallest number such that

t and v = (i, σ)

∀

Ωα

i,σ(t)

Ω.

| ≤

|

α
X

5

(S23)

Note that Ω

= 0 only for the bosonic model—we do not include a displacement term in the fermionic model.

Note that the inter-site non-Gaussian interactions were not included in the main text, and the results quoted in the
main text can be obtained by setting UC = 0. Finally, it will also be convenient to deﬁne the parameter Λ as

While analyzing the bosonic model, it will be more convenient to express Hg as a sum of particle number conserving

and non-conserving terms via

Λ = JC + UC + Jos + Uos + κ + Ω.

(S24)

Hg(t) =

Xv,v′

(cid:0)

Jv,v′ (t)a†vav′ + h.c.

+

(cid:1)

H hop
g

(t)

Xv,v′

(cid:0)

Gv,v′ (t)avav′ + h.c.

+

H sq

g (t)

(cid:1)

v
X

(cid:0)

Dv(t)av + h.c.

,

(cid:1)

H disp
g

(t)

(S25)

|

}

v,v′ + iJ 1,2

v,v′ + iJ 2,1
v,v′

where, up to a possibly time-dependent energy shift in Hg(t),
(J 1,1
J 2,2
v,v′ )/2 and
diﬀerent bosonic modes and conserves the total particle number N =
multi-mode squeezing term in the Hamiltonian and H disp
and H disp
smallest number such that for all t and v

ν(t)

iΩ2

−

−

g

g

{z
Dv = (Ω1

}
{z
Jv,v′ = (J 1,1
v,v′
ν(t))/√2. Here, H hop

g

P

|

−

iJ 1,2
v,v′

{z
iJ 2,1

}
v,v′ )/2,

|
v,v′ + J 2,2
Gv,v′ (t) =
−
(t) is a particle hopping term between
g (t) can be considered to be a
g (t)
as the

v nv, H sq

(t) do not conserve the total particle number N . It will also be convenient to deﬁne the constant

(t) displaces the individual bosonic modes. Both H sq

Furthermore, it can be noted that

|Dv(t)

| ≤

Finally, the noise in the dynamics of the bosonic and fermionic models will be modeled by the Lindbladian

|Gv,v′ (t)

| ≤ G

.

Xv′

Ω/√2.

by

3

Ln =

κlDL(l)

i,σ

,

i,σ
Xl=1 X
i,σ = ai,σ (incoherent particle loss), L(2)

DLρ = LρL†

where
i,σ = a†i,σ (incoherent particle gain), and
L(3)
i,σ = a†i,σai,σ = ni,σ (dephasing). Unless otherwise mentioned, we will assume that all three dissipators act on each
mode κ1, κ2, κ3 > 0 and will denote the total dissipation rate by κ = κ1 + κ2 + κ3. We summarize all the parameters
of the model in Table SII.

− {

/2, L(1)
L†L, ρ
}

G

(S26)

Ln given

(S27)

II. HIGH NOISE SIMULABILITY OF THE FERMIONIC MODEL (THEOREM 1)

In this section, we will present the proof of Theorem 1, which establishes the high-noise simulability of the fermionic
model. We will ﬁrst analyze the Trotterization of the continuous-time model, followed by analyzing each Trotter time-
step to establish its convex Gaussianity for high noise and to obtain an explicit algorithm for classically simulating
either sampling from or computing local observables in the fermionic state. We begin with a ﬁrst-order Trotter approx-
imation to ρ(t) with the following splitting of the Lindbladian

(t) into a Gaussian and non-Gaussian Lindbladian:

(t) =

i[Hg(t),

] +

L

−

·

i[Hng(t),

] +

·

κ3DL(3)

i,σ

,

(S28)

1,2
Xl
∈{
Lg(t)
{z
We next Trotterize the state ρ(t) into T Trotter steps: The Trotterized state σT will be given by

Lng(t)
{z

|

|

}

}

i,σ
} X

i,σ
X

L
κlDL(l)

i,σ

−

σT =

1

(cid:18)

Yτ =T

Φng

τ δ,(τ

−

1)δΦg

τ δ,(τ

ρ(0),

1)δ

−

(cid:19)

(S29a)

̸
Parameter

J α,α′
v,v′ (t) or J α,α′

i,σ;i′,σ′ (t)

JC

Jos

Deﬁned in

Eq. (S17)

Eq. (S19)

Eq. (S20)

Uv,v′ (t) or Ui,σ;i′,σ′ (t)

Eq. (S18)

UC

Uos
Λ
Ωv(t) or Ωi,σ(t)
Jv,u(t)
Gv,u(t)

G
Dv(t)
κ
κ1
κ2
κ3
γ
n
L
m

Eq. (S21)

Eq. (S22)
Eq. (S24)
Eq. (S17)
Eq. (S25)
Eq. (S25)

Eq. (S26)
Eq. (S25)
Eq. (S27)
Eq. (S27)
Eq. (S27)
Eq. (S27)
Assumption 2
—
—
—

6

Informal description
Gaussian coupling between two fermionic or bosonic
modes
Maximum total strength of Gaussian coupling between a
mode and all other modes at diﬀerent sites
Maximum total strength of Gaussian coupling between a
mode and all other modes at the same site
Non-Gaussian interaction between two fermionic or
bosonic modes
Maximum total strength of non-Gaussian interaction be-
tween a mode and all other modes at diﬀerent sites
Maximum total strength of non-Gaussian interaction be-
tween a mode and all other modes at the same site
Total coupling strength
On-site displacement acting on bosonic modes
Gaussian hopping between two bosonic modes
Multi-mode squeezing term between two bosonic modes
Maximum strength of multi-mode squeezing between one
bosonic mode with all other modes
Single-mode displacement acting on bosonic modes
Total dissipation rate
Dissipation rate for incoherent particle loss
Dissipation rate for incoherent particle gain
Dissipation rate for dephasing
Deﬁned as γ = κ1 − κ2 − 2G
Number of sites
Number of modes per site
Total number of modes m = nL

TABLE SII. Table of all the coeﬃcients and parameters relevant to the bosonic and fermionic models.

where δ = t/T and

Φng

t,t′ =

T

exp

(cid:18) Z
∥1.

We ﬁrst provide a bound on

σT −
∥
Lemma 3 (Trotterization: Fermionic model). For all T > 0,

ρ(t)

t

t′ Lng(s)ds

(cid:19)

and Φg

t,t′ =

t

exp

T

t′ Lg(s)ds

.

(cid:19)

(cid:18) Z

(S29b)

Proof. Noting that
parameter ℓ in Lemma 2 can be chosen to be 2mΛ. The lemma statement then follows directly from Lemma 2.

2m(JC + Jos + κ1 + κ2), we obtain that the

2m(UC + Uos + κ3) and

∥Lng(s)

∥⋄ ≤

∥⋄ ≤

σT −
∥

ρ(t)

∥1 ≤

Λ2.

4t2m2
T
∥Lg(s)

Lemma 4 (Convex-gaussianity condition for 2-fermionic modes). Consider a Lindbladian on two fermionic modes
given by

(t) =

L

−

i[h(t),

] +

·

κi(t)

Dni ,

1,2
Xi
∈{

}

where h(t) = u(t)n1n2 and ni is the number operator for the ith mode.

, then the channel
(s)ds) generated by the Lindbladian in the time interval (t, t + τ ) maps a convex Gaussian state to

If κi(t)

exp(

u(t)

≥ |

|

T
another convex Gaussian state.

L

t+τ
t

R

Proof. It will be convenient to deﬁne the scalars

t+τ

t+τ

U =

u(s)ds, Ki =

κi(s)ds,

and K = K1 + K2.

(S30)

t

Z

t

Z

We also note that, since both the Hamiltonian and the jump operators are expressible as polynomials of the fermionic
number operators n1, n2, they commute with each other. Therefore,

7

We deﬁne the channel

L

t+τ

exp

T

t

(cid:18) Z
Rt+τ,t via
Rt+τ,t(ρ) = Ez

(s)ds

= exp

(cid:19)

−

(cid:0)

iU [n1n2,

]

exp

·

K1Dn1

exp

K2Dn2

.

(cid:1)

(cid:0)

(cid:1)

(cid:0)

(cid:1)

R(z)ρR†(z)

where R(z) = exp

√U e−

iπ/4(zn1 + z∗n2)

,

(S31)

(S32)

(cid:0)

(cid:1)

We now explicitly compute

where z = (a + ib)/√2 with a, b being independent standard normal random variables. Note that, due to Lemma 1,
Rt+τ,t maps an input Gaussian state to a (possibly unnormalized) convex-Gaussian state.
and

Ni,r as the superoperator which right multiplies by ni (i.e.
√U e−
a
√2

Ni,l as the superoperator which left multiplies by ni (i.e.
Ni,r(ρ) = ρni). Then
N2,r)
N1,r + z
N1,r +

N2,l) + √U ∗eiπ/4(z∗
+ √U ∗eiπ/4(

Rt+τ,t = Ez
= Ea

Rt+τ,t(ρ). deﬁne

N1,l + z∗
iπ/4(

Ni,l(ρ) = niρ)

N1,l +

√U e−

iπ/4(z

N2,r

(cid:0)
exp

N2,l

exp

(cid:1)(cid:1)

×

(cid:0)

(cid:0)

(cid:1)

(cid:18)

(cid:18)

(cid:0)
exp

Eb

ib
√2

√U e−

iπ/4(

(cid:1)
N1,l − N2,l

√U ∗eiπ/4(

(cid:19)(cid:19)

(cid:1)(cid:1)
N1,r − N2,r

(1)= exp

(cid:18)

−

= exp

−

i

(

(

U
4

(cid:18)
U
4

(cid:18)
N1,l +
U
4

(cid:0)
N2,l)2 + i
N1,r +
U
N1,l − N2,l)2
4
(cid:18)
N1,lN2,l − N1,rN2,r) +
iU (

−

(

i

i

exp

N1,l − N2,r
(cid:0)
U
|

(cid:1)
N1,lN1,r +

(

|

−
(cid:1)
N2,r)2 + |

U
2

2

|

+ |

(

N1,l +
U
2
N2,lN2,r)

(

|

,

(cid:19)(cid:19)
(cid:1)(cid:1)
N1,r +

N2,r)

N2,l)(

×

(cid:19)

N1,l − N2,l)(

N1,r − N2,r

(cid:19)

(cid:1)

(S33)

where, in (1), we have used the fact that, for any operator O, Ex
[n1n2,

], we obtain that

(cid:0)

·

(cid:1)
(0,1)(exO) = eO2/2. Identifying

∈N

N1,lN2,l−N1,rN2,r =

Using Eq. (S34) and Eq. (S31) together with the fact that

exp(

−

iU [n1n2,

·

]) = exp(

U

− |

(

N1,lN1,r +
|
Dni =

Rt+τ,t.

N2,lN2,r))
2
i,l +
(

Ni,lNi,r −

N

2
i,r)/2, we obtain that

N

U

exp((Ki − |
Ei
{z

R

exp

T

t

(cid:18) Z

t+τ

L

(s)ds

=

(cid:19)

(cid:18) Yi

∈{

1,2

}

)

Ni,lNi,r)

|

exp(

2
i,l +

(

−

N

N

2
i,r)/2)

Rt+τ,t.

(cid:19)

Fi
{z

We note that
Rt+τ,t and
, which is implied by κi(t)
Gaussian states. Furthermore, if Ki ≥ |
t+τ
Ei also have this property. Consequently, since
t
Gaussian states to (normalized) convex Gaussian states.

}
|
Fi are completely positive maps that map convex Gaussian states to possibly unnormalized
quoted in the lemma statement, then
≥ |
, it maps convex
U

|
(s)ds) is a channel, as long as Ki ≥ |

exp(

u(t)

L

U

T

|

}

|

|

Theorem 1 (High-noise convex Gaussianity and classical simulation of the fermionic model, reproduced from the
main text). For an initial Gaussian state, if κ3 ≥
2U , then the state of the fermionic model at time t, ρ(t), is convex
Gaussian for all t
0. Furthermore, ρ(t) can be classically sampled in the Fock state basis to an ϵ total variation
error in O(m7Λ2t2/ϵ) time.
Proof. Consider the Trotterized state σT [Eq. (S29)]—note that Φg
preserves convex Gaussianity. We now obtain the condition under which Φng
using Lemma 4. We ﬁrst perform the decomposition

1)δ is a Gaussian channel and hence trivially
1)δ also preserves convex Gaussianity

τ δ,(τ

τ δ,(τ

≥

−

−

Φng

τ δ,(τ

1)δ =

−

v,u
Y
where we choose

τ δ

exp

T

1)δ Lv,u(s)ds

(cid:19)

(τ

(cid:18) Z

−

where

Lv,u =

−

i[Uv,u(t)nvnu,

] + κ3

pv,u(t)

Dnv + qv,u(t)

Dnu

, (S36)

·

(cid:0)

(cid:1)

pv,u(t) =

1
2

Uv,u(t)

|

Uv,u(t)

|
u |

and qv,u(t) =

1
2

|

Uv,u(t)

|

Uv,u(t)

|
v |

.

|

(S37)

P

P

(S34)

(S35)

Next, we apply Lemma 4: For
condition is that

Lv,u(t) to generate a channel that is convex-Gaussianity preserving, a suﬃcient

κ3pv,u(t), κ3qv,u(t)

Uv,u(t)

or equivalently κ3 ≥

2

|

≥ |

Uk,k′ (t)

for k

v, u

∈ {

.
}

|

(S38)

|

Xk′

8

|

−

R

k′

−

P

τ δ,(τ

| ≤

Uk,k′ (t)
Since
follows from Lemma 4 that Φng
Trotterized state σT is a convex-Gaussian state such that

UC + Uos, this condition is satisﬁed if κ3 ≥

2(UC + Uos). Assuming this to be true, it then
1)δ maps an input Gaussian state to a convex-Gaussian state—consequently, the

ϵ when T = Θ(t2m2Λ2/ϵ).

ρ(t)
σT ∥1 ≤
∥
Time-complexity of sampling in the Fock state basis. Since σT is convex-Gaussian by construction, it can be
expressed as σT =
ραdµ(α), where ρα is a Gaussian state and µ is a probability measure. To sample from σT ,
we can then ﬁrst sample from µ to obtain a Gaussian state and then use the standard algorithm for sampling
from fermionic Gaussian states. Consider sampling from µ(α): Suppose the initial state ρ(0) is a Gaussian state.
Lemma 4 provides an explicit characterization of the convex combination of Gaussian states that result when applying
exp(
1)δ Lv,u(s)ds) on an input Gaussian state. Furthermore, since the covariance matrix of the Gaussian state
T
2m matrix, the probabilities of each Gaussian state in the convex combination being computable from
is a 2m
R
the result for covariance matrices of products of Gaussian states [S2, S4] in O(m3) time—sampling from this convex
combination thus requires O(m3) time. At every time-step, this has to be done for every pair of fermionic modes
to apply Φng
1)δ, thus yielding a total time-complexity of O(m5). The application of the Gaussian evolution in
each time-step can also be done at the level of covariance matrices in O(m3) time. Thus, the total time of sampling
from µ is given by O(m5
T ) = O(m7Λ2t2/ϵ). Finally, having sampled a Gaussian state ρα from σT , we can draw a
sample in the Fock state basis in O(m3) time [S5, S6]—the total time complexity of the sampling algorithm thus is
dominated by the cost of sampling from µ and is given by O(m7Λ2t2/ϵ).

−
×

τ δ
(τ

τ δ,(τ

×

−

III. HIGH-NOISE SEPARABILITY OF THE BOSONIC MODEL (THEOREM 2)

In this section, we will present proof of Theorem 2, which considers the high-noise regime of the bosonic model.
Since the bosonic model is inﬁnite-dimensional with unbounded terms in the Hamiltonian, its analysis ﬁrst requires an
analysis of the particle number (as well as its moments) in the model. We do so in the ﬁrst subsection—then, in the
proof of Theorem 2, we ﬁrst approximate the inﬁnite-dimensional bosonic modes with ﬁnite-dimensional qudits and
quantify the approximation error. Finally, we analyze the resulting ﬁnite-dimensional model and establish high-noise
separability in the model.

A. Analyzing particle number moments

We begin by introducing a physically motivated assumption on the initial state of the model—the initial state will
be assumed to be a product state with a “uniform particle moment density” assumption, similar to that used in
Ref. [S7].

Assumption 1 (Uniform particle moment density). The initial state ρ(0) is a product state and
that

1, 2, 3 . . .

v and k

∀

∈ {

}

C0, α0, β0 > 0 such

∃

≤
As shown in Ref. [S7], this assumption is satisﬁed for a wide variety of physically relevant initial states of the bosonic
model, notably for the vacuum state, thermal states, as well as coherent states. Furthermore, it implies a bound on
the moments of the total particle number N =

v nv since

Tr(nk

vρ(0))

C k

0 kα0k+β0 .

P

k

Tr(N kρ(0)) =

Tr(nv1 nv2 . . . nvk ρ(0))

v1,v2...vk
X

≤

v1,v2...vk
X

i=1
Y

Tr(nk

vi ρ(0))1/k

≤

(C0m)kkα0k+β0 ,

(S39)

where we remind the reader that m = nL is the total number of bosonic modes in the model. This particle number
moment bound, in turn, implies that the probability of high-particle-number states being occupied is exponentially
suppressed, which we make precise in the following lemma.

Lemma 5 (Probability of high-particle-number states (Ref. [S7])). Suppose ρ is a state which satisﬁes Tr(N kρ)
(Cm)kkαk+β and Π

d is a projector on the subspace with

d particles, then

≥

Proof. Note that, for any k > 0,

Tr(Π

≥

dρ)

≤

(cid:18)

≥
deα/β
Cme

(cid:19)

β/α

e−

(d/Cme)1/α

.

9

≤

dkTr(Π

≥

dρ)

≤

Tr(N kΠ

dρ)

≥

≤

Tr(N kρ)

≤

(Cm)kkαk+β =

⇒

Tr(Π

≥

dρ)

≤

kβ

Cmkα
d

k

.

(cid:19)

(cid:18)

(S40)

We can now pick k to be the greatest integer smaller than (d/Cme)1/α—we then have that (d/Cme)1/α
(d/Cme)1/α and therefore

1

−

≤

k

≤

Tr(Π

≥

dρ)

d
Cme

(cid:19)

≤

(cid:18)

β/α

k

e−

β/α

deα/β
Cme

(cid:19)

≤

(cid:18)

e−

(d/Cme)1/α

,

(S41)

which proves the lemma statement.

While we will assume that the uniform particle moment density condition holds for the initial state, the subsequent
dynamics of the bosonic model could possibly violate this condition. In the remainder of this section, we show that
under the condition that the total rate of particle loss is higher than the total rate of particle gain (which we make
precise below in assumption 2), the moments of the total particle number Tr(N kρ(t)) satisfy an inequality similar
to Eq. (S39), which by Lemma 5 implies that the probability of higher particle number states being occupied is
super-polynomially small in the particle number.

G

Assumption 2. The parameters κ1, κ2 and

are such that 2γ = κ1 −
Physically, this assumption restricts the rate of 3 processes in the bosonic model that can change its particle number:
κ1 and incoherent particle
In the noise terms, incoherent particle loss can decrease the particle number at a rate
gain can increase the particle number at a rate
g (t) in
Eq. (S25)) can also increase the number of particles in the system at a rate
. Assumption 2 constrains the model to
have particle loss higher than particle gain, without which the number of particles can increase arbitrarily with time.
We remark that we do not need any assumption on the strength of displacement term (H disp
(t) in Eq. (S25))—we
will show in Lemma 8 that, as long as assumption 2 is satisﬁed, no matter how large the displacement term is, the
particle number (and its moments) do not grow arbitrarily with time.

κ2. Furthermore, in the Hamiltonian, the squeezing term (H sq

κ2 −

> 0.

∼ G

∼

∼

G

2

g

We begin with a two technical lemmas that will be useful in our analysis.

Lemma 6. Suppose xk(t), for k
inequalities

∈ {

0, 1, 2 . . .

}

, are non-negative functions of time which satisfy the diﬀerential

d
dt

xk(t)

≤ −

k

γkxk(t) + λmk

2q

k
q

(cid:18)

(cid:19)

xk

−

q(t),

C0, α0, β0 > 0 : xk(0)

∃

≤

(C0m)kkα0k+β0 for all

q=1
X
0 and

t

∀

≥

where γ, λ, m > 0. Furthermore, suppose x0(t) = 1
k

1, 2, 3 . . .

. Then

∈ {

}

xk(t)

≤

(Cm)eαk+β, where C = eλ/γ(C0 + 2), α = max(α0, 1) and β = β0.

Proof. The diﬀerential inequality can be written as an integral inequality:

xk(t)

≤

xk(0)e−

γkt + λmk

k

q=1
X

2q

k
q

(cid:18)

0

(cid:19) Z

t

xk

−

q(s)e−

γk(t

s)ds.

−

(S42)

Recursing Eq. (S42), we obtain

xk(t)

≤

xk(0)e−

γkt +

k

k

q1

k

−

P

p−1
i=1 qi

k

−

2P

p

i=1 qi λpk!

p

p=1
X

q1=1
X

q2=1
X

· · ·

qp=1
X

q1!q2! . . . qp!(k

p
i=1 qi)!

(cid:18)

i=1 (cid:18)
Y

−

P

k

−

qj

1

i

−

j=1
X

xk

P

−

(cid:19)(cid:19)

p

i=1 qi (0)I (k)

q1,q2...qp (t),

(S43)

e−

γk(t

s1)e−

−

γ(k

q1)(s1−

s2)e−

−

γ(k

q1−

q2)(s2−

s3) . . . e−

−

γ(k

q1−

q2···−

qp)sp ds1ds2 . . . dsp

−

10

eγ(q1s1+q2s2+...qpsp)ds1ds2 . . . dsp.

(S44)

where

I (k)
q1,q2...qp (t) =

Z

t

s1

sp−1

· · ·
t

0
Z
s1

0

0 Z
kγt

= e−

s2

sp−1

0 Z

0 Z

Z

0

· · ·

0

Z

We note that I (k)

q1,q2...qp (t) can be upper bounded:

t

t

t

I (k)
q1,q2...qp (t)

≤

≤

≤

kγt

e−

−∞ Z

Z
1
γpq1q2 . . . qp
1
γp e−

q1−

γ(t

−

eγ(q1s1+q2s2+...qpsp)ds1ds2 . . . dsp

−∞

Z
q1−

q2−

...qp)γt

· · ·

−∞
e−

(k

−

q2−

...qp).

(S45)

In the calculation done below, it will be useful to note that, given any f (n) where n

0, 1, 2 . . .

∈ {

,
}

k

q1

k

−

P

p−1
i=1 qi

k

−

· · ·

q1=1
X

q2=1
X

qp=1
X

1
q1!q2! . . . qp!

f

k

q

q1

q

−

P

p−q
i=1 qi

q

−

· · ·

q1=1
X

q2=1
X

qp=1
X

1
q1!q2! . . . qp!

f (q)

p

qi

(1)=

(cid:18)

i=1
X

(cid:19)

q=p
X
k

q=p
X

k

q=p
X

(2)=

(3)

≤

f (q)

Xq1,q2...qp≥
q1+q2+...qp=q

1

1
q1!q2! . . . qp!

pqf (q)
q!

,

(S46)

where in (1) we have introduced the index q = q1+q2+. . . qp, which ranges from p to k, and re-expressed the summation
over q1, q2 . . . qp as ﬁrst a sum over q, and then a sum over q1, q2 . . . qp subject to the contraint q1 + q2 + . . . qp = q.
In (2), we have simply noted the fact that the summation over q1 ∈ {
1 ∈
−
with the additional constraint
is identical to summation over q1, q2 . . . qp ∈ {
1, 2 . . . q
{
−
that q1 + q2 + . . . qp ≤

q. Finally, (3) is obtained by identifying the summation as a multinomial sum.

, q2 ∈ {
}
1, 2 . . . q
}

(q1 + q2 + qp

1, 2 . . . q

1, 2 . . . q

q1}

. . . qp

1)

}

−

−

Returning to Eq. (S43), we obtain that

xk(t)

(1)

≤

(2)

≤

≤

≤

≤

k

k

k

k

xk(0)e−

γkt +

p=1
X
k

q1=1
X
k

q2=1
X

xk(0)e−

γkt +

(2p)q

p=1
X

q=p
X

(cid:18)
k

· · ·

qp=1
X

k
q

(cid:19)(cid:18)
q

(C0m)kkα0k+β0 e−

γkt +

(2k)q

q=1
X

p=1
X

k

(C0m)kkα0k+β0 e−

γkt + mkekλ/γ

(eλ/γm)kkβ0

k

q=1 (cid:18)
X

k
q

(cid:19)

k!2q1+q2...qp
p
i=1 qi)!p!

q1!q2! . . . qp!(k

−

λmk
γ

p

(cid:19)

(cid:18)

xk

−

p

i=1 qi (0)e−

P

γt(k

−

P

p
i=1 qi)

λmk
γ

P
γt(k

q)

−

xk

−

q(0)e−

p

(cid:19)

k
q

(cid:18)

(cid:19)(cid:18)

λmk
γ

p

(cid:19)

(C0m)k

q(k

−

−

q)α0(k

q)+β0 e−

−

γt(k

q)

−

(2k)qC k
0

q

−

kα0(k

q)+β0 e−

−

γt(k

q)

−

k
q

(cid:19)

q=1 (cid:18)
X

(C0kα0 e−

γt)k

q(2k)q = (eλ/γm)kkβ0 (C0kα0 e−

γt + 2k)k,

−

(S47)

in (1), we have used Eq. (S45) and in (2) we have used Eq. (S46). Finally, using C0kα0 e−

where,
kmax(α0,1)(C0 + 2), the lemma statement follows.

γt + 2k

≤

Lemma 7. For any k > 0, v,

[av, N k] = av(N k

(N

−

−

I)k) and [av, N k] = ((N + I)k

N k)av.

−

11

(S48)

(S49)

|

,

n1, n2 . . . nm⟩
(S50)

Furthermore, for any k > 0, v,

Proof. We begin by noting that, for any z, it follows from ezN ave−

zN = e−

zav that

[av, ezN ] = avezN

ezN av = av(ezN

−

−

ez(N

I)) = (ez(N +I)

−

ezN )av.

−

a†vN kav ⪯

nvN k.

We thus obtain that

[av, N k] =

dk
dzk [av, ezN ]

Furthermore, for any state

ψ

=

, where ψ⃗n is the amplitude of

on the basis state

=

⃗n
|

⟩

= av

N k

(N

−

−

I)k

=

(N + I)k

N k)av.

−

z=0

(cid:12)
(cid:12)
(cid:12)
(cid:12)

(cid:0)

2 nv(

⃗n
∥

∥1 −

1)k

≤

ψ⃗n|

|

X⃗n

k
1 =
∥

ψ

|

⟨

nvN k

,

ψ

|

⟩

(cid:1)

(cid:0)
ψ

|
⟩
2 nv ∥
⃗n

|
⟩
a†vN kav |

ψ

ψ

|

⟨

⃗n
⃗n ψ⃗n |
P
=
⟩

|

⟩
ψ⃗n|

X⃗n
nvN k.

from which it follows that a†vN kav ⪯
In the next lemma, we derive an upper bound on Tr(N kρ(t)), which will be central to analyzing the Hilbert space
truncation and Trotter bounds in the subsequent subsections.

Lemma 8 (Upper bounding particle number moments). Consider a bosonic model satisfying assumption 2 with the
bosonic modes in an initial state ρ(0) satisfying assumption 1, then,

0,

t

Tr(N kρ(t))

≤

≥
(Cm)kkαk+β,

∀

where C = e1+4Ω2/γ2+2

/γ+4(κ1+κ2)/γ(C0 + 2), α = max(α0, 1) and β = β0 with C0, α0, β0 deﬁned in assumption 2.

G

Proof. We will use the Heisenberg equations of motion for the operator N k.
0, [N k, H hop
then have that

†nv (N k) = 0 (where H hop

(t)] = 0 and

(t) is deﬁned in Eq. (S25)). Using notation

Note that [N k, Hng(t)] =
⟩t = Tr(Oρ(t)), we

D

O

⟨

g

g

d
dt ⟨

N k

⟩t =

v
X

(cid:0)

κ1⟨D

†av (N k)

⟩t + κ2⟨D

†
a†
v

(N k)

⟩t

i

⟨

−

[N k, H sq

g (t)]

⟩t −

i

⟨

[N k, H disp

g

(t)]

⟩t.

(S51)

†
n(N k)

⟩t

⟨L

(cid:1)

Consider ﬁrst

†av (N k),

D

D

|
(N k)—using Lemma 7, we obtain that
†
a†
v

{z

}

†av (N k) =

−

D

v
X

a†v[av, N k] =

N

N k

−

(N

−

−

I)k

=

−

kN k +

(

1
Xl
≥

(cid:1)

v
X
[av, N k]a†v =

(cid:0)

(N + I)k

−

(cid:0)

(cid:1)

N k

(N + I) = kN k +

k
l + 1

(cid:19)

N k

l,

−

N k

l.

−

(S52)

1)l

−

(cid:18)
k + 1
l + 1

1 (cid:18)

Xl
≥

(cid:19)

(N k) =

†
a†
v

D

v
X

Therefore,

v
X

1)l

κ1(

−

k
l + 1

(cid:18)

+ κ2

(cid:19)

(cid:18)

k + 1
l + 1

⟨

(cid:19)(cid:19)

N k

−

l

⟩t

†n(N k)

⟨L

⟩t =

(κ1 −

−

κ2)k

(1)

≤ −

(κ1 −

κ2)k

(κ1 −

≤ −

κ2)k

⟨

⟨

⟨

k

Xl=1 (cid:18)

k

N k

⟩t +

N k

⟩t +

κ1k + κ2(k + 1)

Xl=1

(cid:0)
⟩t + 2(κ1 + κ2)km

N k

(cid:18)

(cid:1)
k
l

(cid:18)

k

2l

Xl=1

k
l

⟨

(cid:19)

N k

−

l

⟩t

N k

−

l

⟩t,

⟨

(cid:19)

(S53)

where we implicitly set

k
l

(cid:0)

(cid:1)

= 0 if l < 0 or l > k and in (1) we have used the fact that

k
l+1

≤

k

k
l

,

k+1
l+1

≤

(k + 1)

(cid:0)

(cid:1)

(cid:0)

(cid:1)

(cid:0)

(cid:1)

k
l

.

(cid:0)

(cid:1)

Next, consider [N k, H sq

g (t)] =

v,u Gv,u(t)[N k, avau]

−

h.c. — we begin by noting that from Lemma 7

P
[N k, avau] =

[av, N k]au −

−

av[au, N k] =

2

−

k
2l + 1

(cid:19)

0 (cid:18)

Xl
≥

avN k

2l

1au,

−

−

(S54)

12

and therefore

[N k, H sq

g (t)]

⟨

(cid:12)
(cid:12)

⟩t

(cid:12)
(cid:12)

≤

(1)

≤

(2)

≤

2

2

v,u
X

v,u
X

0
Xl
≥

v,u
X

0
Xl
≥

|Gv,u(t)

||⟨

[N k, avau]

⟩t|

|Gv,u(t)

|

k
2l + 1

(cid:18)

|⟨

(cid:19)

avN k

−

2l

−

1au⟩t|

|Gv,u(t)

|

(cid:18)

k
2l + 1

(cid:19)

(cid:0)
auN k

−

≤ G

(3)

≤ G

u
X

0 (cid:18)

Xl
≥

u
X

0 (cid:18)

Xl
≥

k
2l + 1

k
2l + 1

⟨

⟨

(cid:19)

(cid:0)

(cid:19)

(cid:0)
k

avN k

−

2l

−

1a†v⟩t|

+

|⟨

|⟨

Tr(a†uN k

−

2l

−

1au⟩t|

2l

−

1a†u⟩t +

⟨

a†uN k

−

2l

−

1au⟩t

(cid:1)

(N + I)k

−

2l

−

1aua†u⟩t +

⟨

(N

−

I)k

−

2l

(cid:1)

(cid:1)
k

−

1a†uau⟩t
k
2l + 1

(cid:19)(cid:18)

2

G

≤

0 (cid:18)

Xl,p
≥

k
2l + 1

(cid:19)(cid:18)

−

2l
2p

−

1

⟨

(cid:19)

N k

−

2l

−

2p

⟩t + 2

G

m

0 (cid:18)

Xl,p
≥

−

1

−

2l
p

⟨

(cid:19)

N k

−

2l

−

p

−

1

⟩t.
(S55)

where, in (1), we have used Eq. (S54), in (2) we have used the fact that, for any two operators A, B,

AA†⟩⟨

⟨

B†B

⟩ ≤

(

⟨

AA†

+

⟨

⟩

B†B

⟩

)/2 and in (3) we have used Lemma 7. We can thus conclude that

p

where

[N k, H sq

g (t)]

⟩t

k

2
G

⟨

≤

N k

⟩t + 2

G

(cid:12)
(cid:12)

⟨

(cid:12)
(cid:12)

N k

−

q

f (k)
q

⟨

⟩t,

1
Xq
≥

f (k)
q =

m

m

(

l

≥

P

l

≥

k
2l+1
k
2l+1

(cid:0)

0

0

(cid:1)(cid:0)

k
q
k
q

−
−
−
−

(2l+1)
(2l+1)
(2l+1)
(2l+1)

+

(cid:1)

k
2l+1

k

(2l+1)
−
2l
q

−

0

l

≥

if q

if q

1, 3, 5 . . .

2, 4, 6 . . .

∈ {

∈ {

,
}
.
}

The expression for f (k)

q

P

(cid:0)

(cid:1)(cid:0)

(cid:1)

P

(cid:0)

(cid:1)(cid:0)

(cid:1)

can be further simpliﬁed by noting that

k
2l + 1

(2l + 1)
(2l + 1)

k
q

−
−

(cid:19)(cid:18)

=

(cid:19)

0
Xl
≥

0 (cid:18)

Xl
≥

(2l + 1)!(k

k!
q)!(q

−

−

(2l + 1))!

=

k
q

(cid:18)

and

q
2l + 1

(cid:19)

= 2q

−

1

k
q

,

(cid:19)

(cid:18)

(cid:19) Xl

≥

0 (cid:18)

AB

⟨

⟩ ≤

(S56)

(S57)

(S58)

k
2l + 1

k

−
q

(2l + 1)
2l

−

(cid:19)

=

(cid:19)(cid:18)

0 (cid:18)

Xl
≥

(2l + 1)!(k

0
Xl
≥

k!
q

−

−

1)!(q

2l)!

−

k
q + 1

=

(cid:18)

We then obtain that

(cid:19) Xl

≥

0 (cid:18)

q + 1
2l + 1

(cid:19)

= 2q

k
q + 1

.

(cid:19)

(cid:18)

(S59)

Again, we note that, since

k
q+1

k

k
q

≤

f (k)
q =

2q
2q

−

1m
1m

k
q
k
q

+ 2q

k
q+1

(

−

(cid:0)
(cid:0)
, it follows that f (k)

(cid:1)
(cid:1)

(cid:0)
q

if q
if q

1, 3, 5 . . .
2, 4, 6 . . .

∈ {
∈ {

,
}
.
}

(S60)

(cid:1)
≤

2q

−

1(m + 2k)

k
q

≤

mk2q

k
q

, and thus we obtain that

(cid:0)

(cid:1)
(cid:0)
(cid:1)
[N k, H sq
g (t)]

⟨

⟩t

2

k

⟨

G

≤

N k

⟩t + mk

G

(cid:12)
(cid:12)

(cid:12)
(cid:12)

(cid:0)

(cid:1)

(cid:0)
2q

(cid:1)
N k

⟨

q

−

⟩t.

k
q

(cid:19)

1 (cid:18)

Xq
≥

(S61)

Finally, we consider [N k, H disp

g

(t)] =

v Dv(t)[N k, av]

−

h.c.—we begin by noting that, from Lemma 7,

P

[N k, av] = ((N + I)k

N k) =

−

k
q

(cid:19)

1 (cid:18)

Xq
≥

N k

−

qav,

13

(S62)

and therefore

⟨

(cid:12)
(cid:12)

[N k, H2(t)]

2Ω

⟩t

≤

k
q

(cid:19)

⟨

(cid:12)
(cid:12)

⟨

(cid:19)s
γ
2 ⟨

(cid:19)(cid:18)

N k

−

qav⟩t

γ

a†vN k

−

(cid:12)
(cid:12)
qav⟩t ×

a†vN k

−

qav⟩t +

γ
2 ⟨

N k

(cid:19)(cid:18)

−

⟩t +

1 (cid:18)

Xq
≥

qnv⟩t +
k
q + 1

+

(cid:18)

k +

(cid:19)
2mΩ2
γ

γ
2

γ
2

v
X

1 (cid:18)

Xq
≥
k
q

v
X

1 (cid:18)

Xq
≥

k
q

k
q

v
X

1 (cid:18)

Xq
≥

1 (cid:18)

Xq
≥
N k

v
X
γ
2

k

⟨

γ
2

k

N k

⟨

⟩t +

(cid:12)
(cid:12)

(1)

≤

≤

(2)

≤

≤

(3)

≤

4Ω2

γ ⟨

N k

q

−

⟩t

2Ω2
γ ⟨

N k

−

q

⟩t

(cid:19)

2Ω2
γ ⟨

N k

−

q

⟩t

(cid:19)

2mΩ2
γ

k
q

(cid:18)

⟨

(cid:19)(cid:19)

N k

−

q

⟩t

Xq
≥
where, in (1), we have again used that
AA†⟩⟨
assumption 2, in (2) we have used Lemma 7 to obtain that
that

km, we obtain that

. Setting k, m

⟨
p

AB

⟩ ≤

k

⟨

1 (cid:18)

k
q+1

≤

k
q

≤

(cid:0)

(cid:1)

(cid:0)

(cid:1)

[N k, H disp

g

(t)]

⟨

γ
2

k

⟨

N k

⟩t + mk

⟩t

≤

Combining Eq. (S51) with Eqs. (S53, S61, S64), we obtain that

(cid:12)
(cid:12)

(cid:12)
(cid:12)

k
q

⟨

(cid:19)

(cid:19)(cid:18)

N k

−

q

⟩t,

(S63)

B†B

⟩
a†vN k

and introduced the parameter γ = κ1 −
qnv⟩

from
, and in (3) we have used the fact

qav⟩ ≤ ⟨

κ2 −

2
G

N k

−

−

⟨

γ
2

+

2Ω2
γ

(cid:18)

k
q

⟨

(cid:19)

N k

−

q

⟩t.

(cid:19) Xq

≥

1 (cid:18)

(S64)

(S65)

d
dt ⟨

N k

⟩t ≤ −

γ
2

k

⟨

N k

⟩t + λkm

k
q

⟨

(cid:19)

N k

−

q

⟩t,

1 (cid:18)

Xq
≥

where λ = γ/2 + 2Ω2/γ +
statement.

G

+ 2(κ1 + κ2). Then, solving this inequality using Lemma 6, we obtain the lemma

Combining this lemma with Lemma 5, we straightforwardly obtain the following lemma upper bounding the probability
of large number of excitations at any time in the bosonic model.

Lemma 9. Suppose Π
≥
1 and 2, then for any t
≥

0,

d is a projector on the subspace with

d particles and the bosonic model satisﬁes assumptions

≥

Tr(Π

≥

dρ(t))

e

≤

k0

exp

d
d0m

(cid:19)

(cid:18)

d
d0m

(cid:19)

−

(cid:18)

(cid:18)

1/α

,

(cid:19)

where d0 = eC, k0 = β/α with C, α, β being deﬁned in Lemma 8.

B. Proof of Theorem 2 (bosons)

The proof of Theorem 2 has three main parts:

(1) Truncation of the Hilbert space of the bosonic model to a ﬁnite-dimensional space and an analysis of the

truncation error (Lemma 11).

(2) First-order Trotterization of the truncated ﬁnite-dimensional model (Lemma 12).

(3) Analysis of each Trotter step to establish high-noise separability (Lemma 13).

14

Truncation of the bosonic model. Suppose we want to truncate the local Hilbert space of each bosonic mode to d
d the Hilbert space of the bosonic model with each bosonic mode truncated to at most

levels—we will denote by
d particles. For the vth bosonic mode, we will deﬁne the projectors Πv,d, Πv,

H≤

d, and Πv,>d via

≤

Πv,d =

d

d

|

⟩⟨

|

, Πv,

≤

d

d =

Πv,j, and Πv,>d =

∞

Πv,j.

(S66)

j=0
X

Xj=d+1
d, which will be the projector onto

H≤

d. The truncated model will be

(S67a)

We will deﬁne the projector Π
described by a Lindbladian

d =

⊗vΠv,

≤

≤
d(t) while

L≤

where

d =

i[H

d,

≤

−

·

L≤

] +

3

v
Xl=1 X

κlDL(l)

v,≤d

,

H
≤
L(1)
v,
≤
L(2)
v,
≤
L(3)
v,
≤
It will be convenient to deﬁne super-operators

d(t) = Π

dH(t)Π

≤
d = Πv,

d,

≤
davΠv,

≤

d = Πv,

≤

d = Πv,

≤

≤

da†vΠv,

≤
dnvΠv,

≤

≤

d,

d,

d = av,

≤

d = a†v,

≤
d = nv,

d.

(S67b)

d and

d via

P≤
d(ρ) = Π

dρΠ

Q≤
d and

Q≤
d projects an input density matrix onto

P≤

≤

≤

The super-operator
ﬁes the error between the state ρ(t) at time t and the state obtained from the truncated evolution: ρ

H≤

P≤

d = id

d.

− P≤
d. We ﬁrst present a lemma that quanti-
d(t) =

≤

(S68)

t
0 L≤

exp(

d(τ )dτ )(

dρ(0)).

P≤
T
Lemma 10. For any d > 0, it follows that

R

t

ρ(t)

− T

exp

0 L≤

(cid:18) Z

d(τ )dτ

(

(cid:19)

P≤

dρ(0))

≤ ∥Q≤

dρ(t)

∥1 + (d + 1)

v Z

X

1

t

(cid:13)
(cid:13)
(cid:13)
Πv,dρ(s)
(cid:13)
0 ∥

t

∥1 ds +

Z

0 ∥P≤

dL

(s)

Q≤

d∥⋄ ∥Q≤

dρ(s)

∥1 ds.

(cid:13)
(cid:13)
(cid:13)
(cid:13)

Proof. Using

d +

P≤

Q≤

d = id together with the master equation (dρ(t)/dt =

(t)ρ(t)), we obtain that

L

d
dt P≤
d
dt Q≤

dρ(t) =

(t)

P≤

dL

P≤

dρ(t) +

(t)

P≤

dL

Q≤

dρ(t),

dρ(t) =

Q≤

dL

(t)

P≤

dρ(t) +

(t)

Q≤

dL

Q≤

dρ(t).

Furthermore, we note that, for any operator X that is supported on the truncated subspace
and deﬁning H

d, we have

d(t) = Π

dH(t)Π

≤

≤

≤

(S69a)

(S69b)

Hd (i.e. X = Π

≤

dXΠ

≤

d),

P≤

dLP≤

d(X) =

i[H

≤

−

d(t), X] + Π

dLnΠ

≤

≤

d(X),

(S70)

(cid:1)

(cid:1)

(S71b)

(S71c)

(cid:1)

P≤

dDav P≤

d(X) = Πv,

davΠv,

dXΠv,

da†vΠv,

≤

d −

≤

≤

≤

1
2

Πv,

≤

dnvΠv,

≤

dX + XΠv,

dnvΠv,

d

≤

≤

15

a†v,

dav,

≤

≤

(cid:0)

dX + Xa†v,

dav,

d

≤

≤

d −

1
2

(cid:0)

(cid:1)

(cid:1)

(S71a)

P≤

dDa†

v P≤

d(X) = Πv,

= av,

=

≤

≤

dXa†v,
Dav,≤d (X),
da†vΠv,

≤

= a†v,

dXav,

≤

≤

d −

=

Da†

v,≤d

(X)

−

1
2
d + 1
(cid:0)
2

dXΠv,

≤

≤

davΠv,

d −

≤

1
2

Πv,

≤

dava†vΠv,

≤

dX + XΠv,

dava†vΠv,

d

≤

≤

av,

(cid:0)

dX + Xav,

da†v,

≤

≤

da†v,

≤

d

≤

−

d + 1
2

Πv,dX + XΠv,d

Πv,dX + XΠv,d

,

(cid:1)

(cid:0)

P≤

dDnv P≤

d(X) = Πv,

dnvΠv,

≤

(cid:0)
dXΠv,
≤

≤

dn2

(cid:1)
Πv,

≤

dn2

vΠv,

≤

dX + XΠv,

dn2

vΠv,

d

≤

≤

≤

≤

=

= nv,

dXnv,
Dnv,≤d (X).
κ1Dav,≤d + κ2Da†

v,≤d

d −

n2
v,

≤

1
2

(cid:0)

+ κ3Dnv,≤d

(cid:1)

Deﬁning

d =

Ln,

≤

v

P

(cid:0)

(cid:1)

, we then obtain that,

X

∀

d,

∈ H≤

vΠv,

1
d −
2
≤
dX + Xn2
v,

(cid:0)
d
≤

(t)

P≤

dL

P≤

d(X) =

L≤

d(t)(X)

Consequently, from Eq. (S69a), we obtain that

d + 1
2

−

v
X

(cid:0)

Πv,dX + XΠv,d

.

(S72)

(cid:1)

d
dt P≤

dρ(t) =

d(t)

L≤

P≤

dρ(t) +

(t)

P≤

dL

Q≤

dρ(t)

−

d + 1
2

v (cid:18)

X

Πv,dP≤

dρ(t) + (

P≤

dρ(t))Πv,d

,

(S73)

(cid:19)

which can be integrated to obtain

dρ(t) =

d(t, 0)

E≤

P≤

dρ(0) +

P≤

t

0 E≤

Z

d(t, s)

(cid:18)

(s)

P≤

dL

Q≤

dρ(s)

−

d + 1
2

Πv,dP≤

dρ(s) + (

P≤

dρ(s))Πv,d

ds,

(cid:19)

(cid:1)

(S74)

v
X

(cid:0)

where

d(t, s) =

E≤

exp(

T

t
s L≤

d(τ )dτ ). From here, it immediately follows that

∥E≤

R
d(t, 0)
ρ

≤ ∥

dρ(0)

P≤

d(t)

≤

−
− P≤

(d + 1)

(d + 1)

≤

(1)

≤

v Z

X

v Z

X

ρ(t)
∥1
∥1 +
dρ(t)
t
Πv,dP≤

0 ∥
t

∥Q≤

dρ(s)

dρ(t)

∥1
∥1 ds +

t

t

0 ∥P≤

dL

Z

(s)

dρ(s)

∥1 ds +

Q≤

∥Q≤

dρ(t)

∥1

Πv,dρ(s)

0 ∥

∥1 ds +

0 ∥P≤

dL

Z

(s)

dρ(s)

∥1 ds +

dρ(t)

∥1 .

∥Q≤

Q≤

(S75)

(S76)

≤

d∥ ∥

Πv,dρ(s)

where, in (1), we have used the fact that Πv,dΠ
Π
d∥
∥
Finally, combining Lemma 10 with Lemmas 5 and 8, we obtain the next lemma quantifying the truncation error as a
function of d.

Πv,dρ(s)
∥

Πv,dP≤
∥

dΠv,d to set

dΠv,dρ(s)Π

∥1 =

d∥1 ≤

d = Π

dρ(s)

Π
∥

∥1,

∥1 ∥

=

Π

≤

≤

≤

≤

≤

Lemma 11. For any d

1, it follows that

≥
t

ρ(t)

exp

− T

d(s)ds

dρ(0)

P≤

0 L≤

(cid:13)
(cid:13)
(cid:13)
where d0, k0, α are the constants in Lemma 9.
(cid:13)

(cid:13)
(cid:13)
(cid:13)
(cid:13)

(cid:18) Z

(cid:19)

1 ≤

O

m1

−

k0/2d2+k0/2t(JC + Jos + UC + Uos + κ)e−

1

2 (d/d0m)1/α

(cid:0)

,

(cid:1)

Proof. We bound each term in Lemma 10. We ﬁrst note that

dρ(t)

∥Q≤

Π>dρ(t) + Π
∥1 =
∥
∥1 +
Π>dρ(t)
≤ ∥
(1)
Tr(Π>dρ(t)) +

dρ(t)Π>d∥1
Π
∥

dρ(t)Π>d∥1
Tr(Π

≤

≤

dρ(t))Tr(Π>dρ(t))

≤

Tr(Π

dρ(t))

q

2√e

≤

≥

d
d0m

(cid:19)

(cid:18)

k0/2

exp

d
d0m

1
2

(cid:18)

(cid:19)

−

(cid:18)

1/α

,

(cid:19)

≤

≤

p
2

q

16

(S77)

where, in (1), we have used the Holder’s inequality to conclude that
thermore,

Aρ(t)B
∥

∥1 ≤

Tr(A†Aρ(t))Tr(B†Bρ(t)). Fur-

p

Πv,dρ(t)

∥

∥ ≤

Tr(Πv,dρ(t))

q

≤

q
(s)

Tr(Π

dρ(t))

√e

≤

d
d0m

(cid:19)

(cid:18)

k0/2

exp

d
d0m

1
2

(cid:18)

(cid:19)

−

(cid:18)

1/α

.

(cid:19)

≥

Finally, we consider upper-bounding
have used the fact that

dL
1. Next, we note that, for a Hamiltonian H and jump operator L,

d∥1 ≤ ∥P≤

∥⋄ ≤

d∥⋄

∥P≤

∥P≤

∥P≤

dL

dL

dL

Q≤

P≤

(s)

+

(s)

2

(s)

d∥⋄ ≤
d[H,

∥P≤

∥P≤

]

∥⋄ ≤

2

Π
∥

≤

dH

∥

and

∥P≤

·

dDL∥⋄ ≤ ∥

Π

dL

2 +
∥

Π
∥

≤

dL†L

.
∥

≤

Furthermore, since

Π

,
dav∥

Π
∥

≤

da†v∥ ≤

≤

∥

√d + 1,

Π
∥

≤

da†vau∥ ≤

d and

Π

≤

,
davau∥

Π
∥

≤

da†va†u∥ ≤

∥

d + 2,

we obtain

d[

·

∥P≤

, H(t)]

∥⋄ ≤

≤

≤

≤

2
∥
4d

Π

dH hop
g

(t)

+ 2

Π
∥

≤

∥⋄

dH sq

g (t)

≤

+ 4(d + 2)

|Jv,u|

v,u
X

v,u
X

|Gv,u|

+ 2

Π
∥⋄
∥
≤
+ 4√d + 1

dH disp
g

(t)
∥⋄
|Dv,u(t)

|

+ 2

Π
∥
≤
+ 4d2

dH ng

g (t)
∥
Uv,u|

|

v
X

v,u
X

4(d + 1)m(Jos + JC) + 2
d(Jos + JC) + √d

8m

Ω

2(d + 1)Ω + 4d2(UC + Uos)
+ d2(UC + Uos
p
|

.

|

where we have used the decomposition of Hg(t) in Eq. (S25). Furthermore,

(cid:1)

(cid:0)

∥P≤

dLn∥ ≤

≤

≤

v (cid:18)

X
m

κ1∥P≤

+ κ2∥P≤

dDav ∥⋄

dDa†
v ∥⋄
κ1(2d + 1) + κ2(2d + 2) + κ3d2
(κ1 + κ2)d + κ3d2

.

8m
(cid:0)

(cid:1)

+ κ3∥P≤

dDa†

vav ∥⋄

(cid:19)

Combining Eqs. (S81) and (S82), we obtain that

(cid:0)

(cid:1)

(S78)

, where we

∥⋄

(S79)

(S80)

(S81)

(S82)

∥P≤

dL

(s)

Q≤

d∥⋄ ≤

2
∥P≤

dL

(s)

∥⋄ ≤

≤

16m
16md2
(cid:0)

(Jos + JC + (κ1 + κ2))d + Ω√d + (UC + Uos + κ3)d2

Jos + JC + Ω + Uos + UC + κ

.

(cid:1)

(S83)

Finally, combining Eqs. (S77, S78, S83) together with Lemmas 10 and 9, we obtain the lemma.

(cid:0)

(cid:1)

Trotterization of the truncated model. We will perform a ﬁrst-order Trotterization of the state ρ
exp(

d(ρ(0)). We will split the Hamiltonian H

d(s)ds)

d(t) into a sum of inter-site terms H C
≤

t
0 L≤

P≤

≤

d(t) =
d(t) and a

≤

T
sum of on-site terms H os
≤

R

d(t):

d(t) =

H

≤

hC
i,σ;j,σ′ (t)

+

hos
i;σ,σ′ (t)

,

i<j
X

Xσ,σ′
H C

≤d(t)

i
X

Xσ,σ′
H os

≤d(t)

|

{z

}

|

{z

}

(S84)

17

(S85)

where, in hC

i,σ;j,σ′ (t) we include all the terms that mediate an interaction between (i, σ) and (j, σ′):

hC
i,σ;j,σ′ (t) = Π

≤

(cid:18)

d

Ui,σ;j,σ′ (t)ni,σnj,σ′ +

J α,α′
i,σ;j,σ′ (t)cα

i,σcα′
j,σ′

Xα,α′
d + 2

Ji,σ;j′,σ′ (t)cα

i,σ;

d + (i, σ)

(j, σ′)

↔

Π

≤

(cid:19)
dcα′

≤

j,σ′;

d,

≤

= 2Ui,σ;j,σ′ (t)ni,σ;

dnj,σ′;

≤

≤

where c1
≤
or non-Gaussian) that act between modes (i, σ) and (i, σ′):

d)/√2, c2

d = (ai,σ;

d = (ai,σ;

d+a†i,σ;

d−

i,σ;

i,σ;

≤

≤

≤

≤

d)/√2i. In hos

i;σ,σ′ (t), we include all the terms (Gaussian

hos
i;σ,σ′ (t) = Π

≤

(cid:18)

d

Ui,σ;i,σ′ (t)ni,σni,σ′ +

J α,α′
i,σ;i,σ′ (t)cα

i,σcα′
i,σ′

Π

d

≤

(cid:19)

= Ui,σ;i,σ′ (t)ni,σ;

dni,σ′;

d +

≤

≤

dΠi,σ′;

≤

≤

dcα

i,σcα′

i′,σ′ Πi,σ;

dΠi,σ′;

d.

≤

≤

(S86)

Furthermore, we will also decompose the dissipation

Xα,α′
a†i,σ;

≤

Xα,α′

J α,α′
i,σ;i′,σ′ (t)Πi,σ;

Xα,α′
Ln,

d:

≤

3

d =

Ln,

≤

i<j
X
where we will choose p(l)
have

Xσ,σ′ L
i,σ;i′,σ′ (t), q(l)

n
i,σ;j,σ′ (t) where

n
i,σ;j,σ′ (t) =

L

κl

p(l)
i,σ;j,σ′ (t)

Xl=1

(cid:0)

DL(l)

i,σ,≤d

+ q(l)

i,σ;j,σ′ (t)

DL(l)

j,σ′ ,≤d

(S87)

,

(cid:1)

i,σ;i′,σ′ (t)

0 later. For this decomposition of

d to be consistent, we must also

Ln,

≤

≥

k, σ :

∀

p(l)
k,σ;k′,σ′ (t) +

q(l)
k′,σ′;k,σ(t) = 1.

Xk′>k Xσ′

Xk′<k Xσ′

(S88)

Now, the state of the truncated model at time t, ρ
number of Trotter steps and

≤

d(t), will be approximated by the state σT,

d, where T is the

≤

1

σT,

≤

d =

Yτ =T (cid:18) Y

i<j

Yσ,σ′

where δ = t/T ,

Φi,σ;j,σ′

τ δ,(τ

1)δ

−

os
τ δ,(τ

1)δρ

≤

−

d(0),

U

(cid:19)

(S89a)

Φi,σ;j,σ′
t,t′

=

exp

T

t

t′ L

(cid:18) Z

C
i,σ;j,σ′ (s)ds

where

(cid:19)

C
i,σ;j,σ′ (s) =

L

−

i[hC

i,σ;j,σ′ (s),

] +

·

L

n
i,σ;j,σ′ (s),

(S89b)

and

os
τ δ,(τ

U

−

1)δ = U os

τ δ,(τ

1)δ(

·

−

)U os

†τ δ,(τ

−

1)δ where U os

τ δ,(τ

1)δ =

−

T

exp

τ δ

1)δ

(τ

−

i

−
Z
d∥1.

H os(s)ds

.

(S89c)

(cid:19)

(cid:18)
σT,

≤

d(t)

ρ

≤

∥

−

The next lemma provides an upper bound on the Trotter error

Lemma 12. For any T > 0 and d

1:

≥

σT,
∥

d −

≤

ρ

≤

d(t)

∥1 ≤

16t2m2d4Λ2
T

.

Proof. This lemma follows from an application of Lemma 2: We note that

C
i,σ;j,σ′ (s)

∥⋄ ≤

2
∥

∥L

hC
i,σ;j,σ′ (s)

+ 2

∥

3

Xl=1

(1)

≤

, H os(t)]

[
∥

·

∥⋄ ≤

(cid:18)

2

Ui,σ;j,σ′ (s)

4
|

+ 8

|

hos
i;σ,σ′ (t)

∥

Xi,σ,σ′ ∥

Xα,α′ |

κl

p(l)
i,σ;j,σ′ (s)

L(l)
i,σ,
∥

d∥

≤

2 + q(l)

i,σ;j,σ′ (s)

L(l)
∥

j,σ′,

2
d∥

≤

(cid:0)
J α,α′
i,σ;j,σ′ (s)

+ 2

|

3

Xl=1

κl(p(l)

i,σ;j,σ′ (s) + q(l)

(cid:1)
i,σ;j,σ′ (s))

(cid:19)

(2)

≤

2

(cid:18)

Xi,σ,σ′ |

Ui,σ;i,σ′ (s)

+ 4

|

J α,α′
i,σ;i,σ′ (s)

d2,

|

(cid:19)

Xi,σ,σ′

Xα,α′ |

d2,

(S90)

(S91)

where, in (1) and (2), we have used the fact that, for the truncated bosonic model,
L(3)
i,σ,

cα
d∥ ≤
i,σ,
d. We can now estimate the parameter ℓ from Lemma 2: ℓ would

ni,σ,
∥

L(1)
i,σ,

d and

d∥ ≤

√2d,

√2d

√d

≤

∥

≤

≤

≤

∥

d∥ ≤

≤

d,
,
d∥
be an upper bound on

L(2)
i,σ,
∥

d∥ ≤

∥

≤

≤

18

[
∥

·

, H os(s)]

+

∥⋄

C
i,σ;j,σ′ (s)

∥⋄

j,i<j
X

Xσ,σ′ ∥L
Ui,σ;j,σ′ (s)

4

≤

≤

|

Xα,α′ |
(cid:18)
4(UC + Uos + JC + Jos + κ)md4

Xσ,σ′ (cid:18)

i,j
X

|

.

+

J α,α′
i,σ;j,σ′

3

+ 2

|

(cid:19)

i,j:i<j
X

Xσ,σ′

Xl=1

κl(p(l)

i,σ;j,σ′ (s) + q(l)

i,σ;j,σ′ (s))

d2

(cid:19)

(S92)

|
Thus, from Lemma 2, we obtain that

{z

σT,

∥

d −

≤

}
ρ
≤

d(t)

∥1 ≤

16t2m2d2(UC + Uos + JC + Jos + κ)2/T .

ℓ

Lemma 13 (Separability condition for the bosonic model). Consider the following Lindbladian
modes truncated to d

1 particles each:

≥

d(t) on two bosonic

L≤

d(t) =

i[hg,

≤

−

L≤

d(t) + hng,

d(t),

≤

] +

·

3

1,2
Xi
∈{

}

Xl=1

κ(l)
i (t)

,

DL(l)

i,≤d

where

hg,

≤

d(t) =

Xα,β
∈{

1,2

}

gα,β(t)cα
1,

dcβ

2,

≤

d, hng,

≤

≤

d(t) = u(t)n1,

dn2,

≤

≤

d, L(1)

i = ai,

d, L(2)

i = a†i,

≤

≤

d and L(3)

i = ni,

d,

≤

d + a†
≤

d)/√2, c2
i,

d = (a

d −

≤

a†
≤

≤

d)/√2i and gα,β(t), u(t) are real and κ(l)

i (t)

0. If

≥

where c1
i,

d = (a

≤
≤
(t), κ(2)
(C1) κ(1)

(t)

i

i

i

≥

α,β |

gα,β(t)

and

|

(C2) κ(3)

(t)

u(t)

,

P

|
then there is a completely-positive map

≥ |

Mt+τ,t − T

t+τ

exp

d(s)ds

t

L≤

8d4

≤

(cid:13)
(cid:13)
(cid:13)
(cid:13)
Proof. It will be notationally convenient to deﬁne the scalars

(cid:18) Xα,β Z

(cid:19)(cid:13)
(cid:13)
(cid:13)
(cid:13)

(cid:18) Z

⋄

Mt+τ,t which maps separable states to separable states and

t+τ

t+τ

3

t+τ

gα,β(s)

t

|

ds +

|

t

Z

u(s)

|

|

ds +

Xl=1 Xi
1,2
∈{

} Z

t

κ(l)
i (s)ds

2

.

(cid:19)

Gα,β =

t

Z

G0 =

t

Xα,β Z

t+τ

gα,β(s)ds, K (l)

i =

t+τ

t+τ

κ(l)
i (s)ds, U =

t+τ

t

Z

u(s)ds and

t+τ

t

Z

3

gα,β(s)

|

|

ds, U0 =

t

Z

u(s)

|

|

ds, Ki =

K (l)
i

, K (l) =

K (l)
i

, K =

Xl=1

1,2
Xi
∈{

}

K (l).

(S93)

3

Xl=1

We will deﬁne the completely positive map

with

(cid:2)

Rt+τ,t via
Rt+τ,t(ρ) = Ez

R1(z)R2(z)ρR†2(z)R†1(z)

,

(cid:3)

R1(z) = Q1 + e−

iπ/4

zα,β

Gα,βcα
1,

Xα,β

p

≤

d, R2(z) = Q2 + e−

iπ/4

z∗α,β

Xα,β

p

Gα,βcβ
2,

d,

≤

(S94a)

(S94b)

where zα,β are drawn independently and uniformly at random from the set
K (2)
d)/2). It can be noted that, by construction,

d +
Rt+τ,t maps a separable input state to a separable (but

and Qi = exp(

i a†i,

i ai,

dai,

da†i,

{±

1,

±

−

}

≤

≤

≤

i

≤

(K (1)

19

(S95)

)2,

(S96)

(S97)

(S98a)

(S98b)

possibly unnormalized) output state. Explicitly evaluating the expectation value in Eq. (S94), we obtain that

Rt+τ,t(ρ) = Q1Q2ρQ†2Q†1 −

i

Gα,β

cα
1,

dcβ

2,

≤

dρQ†2Q†1 −

≤

Q1Q2ρcα
1,

dcβ

2,

≤

d

≤

+

Xα,β
(cid:0)
dQ2ρQ†2cα
1,

d + Q1cβ

2,

dρcβ

2,

≤

≤

≤

dQ†1

+

(cid:1)

Gα,β|

|

cα
1,

≤

Xα,β

Xα,α′,β,β′ (cid:18)

t+δ

= ρ

i

−

t

(cid:20) Z

hg,

≤

(cid:0)
Gα,βGα′,β′ cα
1,

dcβ

2,

≤

≤

dρcβ′

2,

≤

dcα′

1,

≤

(cid:1)
Gα,β| |

|

d +

Gα′,β′

cα
1,

|

≤

dcβ′

2,

≤

dρcβ

2,

≤

dcα′

1,

≤

d

(cid:19)

+

d(s)ds, ρ
(cid:21)
Xα,β
d + K (2)
i ai,

dai,

|

≤

K (1)
{

i a†i,

≤

Gα,β|

cα
1,

≤

dρcα
1,

≤

d + cβ

2,

≤

dρcβ

2,

d

≤

−

(cid:0)
da†i,

≤

d, ρ
}

≤

+ ∆t+τ,t(ρ),

(cid:1)

1
2

1,2
Xi
∈{

}

where, using the fact that

1,

Qi∥ ≤
∥
I
Qi −
∥

∥ ≤

I

(cid:18)

Qi −
cα
i,

d

≤
it follows that

≤

(cid:13)
(cid:13)

(cid:13)
(cid:13)
(cid:13)
(cid:13)
(cid:13)
(cid:13)

1
2
1
2
−
√2

(K (1)
i

a1,
∥
(K (1)

i a†i,

d∥

≤

i

2 + K (2)

a2,
∥
d + K (2)

i ai,

≤

dai,

≤
√2d,

ai,
∥

d∥ ≤

≤

2)

d∥

≤

≤

d
2

≤

da†i,

d)

≤

(cid:19)(cid:13)
(cid:13)
(cid:13)
(cid:13)

),

(K (1)

i

i + K (2)
1
8

(K (1)
i

≤

2 + K (2)

i

d∥

≤

ai,
∥

≤

2)2

d∥

≤

d2
8

(K (1)

i + K (2)

i

ai,
∥

∆t+τ,t∥⋄ ≤
∥
Similarly, we also deﬁne the completely positive map ˜

d2
2

(K (1) + K (2))2 + 4d2G(K (1) + K (2)) + 8d2G2.

˜
Rt+τ,t(ρ) = Ey

Rt+τ,t:
˜R1(y) ˜R2(y)ρ ˜R†2(y) ˜R†1(y)

,

(cid:3)

with

˜R1(y) = ˜Q1 + ye−

iπ/4√U n1,

(cid:2)

≤

d and ˜R2(y) = ˜Q2 + y∗e−

iπ/4√U n2,

d,

≤

1, 1, i,

Rt+τ,t also maps a
where y is drawn randomly from
separable input state to a separable but possibly unnormalized output state. By explicitly evaluating the expectation
in Eq. (S98), we ﬁnd that
Rt+τ,t(ρ) = ˜Q1 ˜Q2ρ ˜Q†2
˜
n1,

dρ ˜Q†1
dn2,
≤
≤
d + ˜Q1n2,

˜Q†1 −
iU (n1,
d ˜Q2ρ ˜Q†2n1,

˜Q1 ˜Q2ρn1,
≤
d ˜Q†1
U
+

d). Similar to

˜Q†2 −
dρn2,

dn2,
≤
2 n1,

dρn2,

dn1,

dn2,

d)+

{−

−

−

U

}

≤

i,

i

d

and ˜Qi = exp(

Rt+τ,t, ˜

≤

≤

≤

|

|

≤

≤

≤

≤

K(3)
2 n2
i

hng,

≤

d(s)ds, ρ
(cid:21)

+

U

|

|

n1,

≤

dρn1,

(cid:1)
d + n2,
≤

≤

dρn2,

(cid:0)

1
2

d

≤

−

(cid:1)

n1,

K3{

≤

d + n2,

d, ρ
}

≤

+ ˜∆t+τ,t(ρ),

(S99)

|

|

≤
t+δ

= ρ

(cid:0)

i

t

(cid:20) Z

−

where, using the fact that
(K (3)
2)2/8
i

(K (3)
i

ni,
∥

d∥

≤

≤

1,

˜Qi −
˜Qi∥ ≤
∥
∥
)2d4/8 and
ni,
d∥ ≤
∥
˜∆t+τ,t∥⋄ ≤
∥

1
2

≤

I

K (3)
i

ni,
∥
d, it follows that

∥ ≤

2 /2

d∥

≤

≤

K (3)

i d2/2,

˜Qi −
∥

(I

−

K(3)
2 n2
i )
i

∥ ≤

(K (3))2d4 + U 2

0 d4 + 2U0K (3)d4.

(S100)

Finally, we consider the channel generated by the fermionic Lindbladian in the time interval (t, t + τ ): Performing a
ﬁrst-order Taylor expansion, we obtain that

t+τ

L

exp

T

t

(cid:18) Z

(s)ds

ρ = ρ +

(cid:19)

t+τ

L

t

Z

(s)ρds + ∆Et+τ,t(ρ),

(S101)

where

∆Et+τ,t∥⋄ ≤
∥

8d4(G + U + K)2. From Eqs. (S95, S99, S101), we then obtain that

exp

T

t

(cid:18) Z

t+τ

L

(s)ds

=

(cid:19)

Mt+τ,t + Et+τ,t,

20

(S102)

where

Mt+τ,t =

Rt+τ,t + ˜

Rt+τ,t+
K (1)
i ai,

1,2
Xi
∈{

} (cid:0)

d ·

a†i,

≤

d + K (2)

i a†i,

ai,

d

≤

d ·

≤

−

≤

(K (3)

i − |

)ni,

U

|

≤

dρni,

,

d

≤

|
1,2
Xi
∈{

}

Et+τ,t = ∆Et+τ,t −

|

˜
Vt+τ,t
{z
∆t+τ,t −

˜∆t+τ,t.

}

(cid:1)
Vt+τ,t
{z

Xα,β

Gα,β|

|

cα
1,

cα
1,

≤

d + cβ

2,

d ·

≤

cβ
2,

d

≤

d ·

≤

+

(cid:0)

(cid:1)

}

(S103)

(S104)

We note that
complete positivity of ˜
lemma statement. To ensure that

Mt+τ,t is a channel that preserves separability as long as
Vt+τ,t is ensured by requiring K (3)

i ≥ |

U

|

Vt+τ,t and ˜

Vt+τ,t are completely positive. The
which is implied by the condition C2 quoted in the

Vt+τ,t is completely positive, we note that it can be re-written as
d + F (i)
a†i,

d + F (i)

d + F (i)

1,1a†i,

1,0a†i,

0,1ai,

a†i,

ai,

ai,

F (i)
0,0ai,

d ·

≤

≤

d ·

≤

≤

d ·

≤

≤

d ·

≤

,

d

(cid:19)

(S105)

≤

Vt+τ,t =

1,2
Xi
∈{

}

(cid:18)

where

F (1) =

1
2

"

β

K (1)
1
2 G
1 −
G2,β| − |

|

G1,β|

1
2

β

P

G2,β| − |
|
K (2)
1
2 G
(cid:0)
1 −

G1,β|

#

(cid:1)

, F (2) =

1
2

"

β

K (1)
1
2 G
2 −
Gα,2| − |

|

Gα,1|

1
2

α

P

Gα,2| − |
|
K (2)
1
2 G
2 −
(cid:0)

Gα,1|

.

(cid:1)

#
(S106)

P

(cid:0)

(cid:1)

As long as F (1), F (2) are positive-semideﬁnite, it would follow that
see that a suﬃcient condition for F (i)
lemma statement. Finally, the error term Et+τ,t can be bounded by

0 is that K (1)

, K (2)

i ≥

⪰

i

(cid:0)

P
Vt+τ,t is completely positive. Now, it is easy to
G, which is implied by the condition C1 quoted in the

(cid:1)

∆t+τ,t∥⋄
Et+τ,t∥⋄ ≤ ∥
∥
∥
which establishes the error bound in the lemma statement.

∆Et+τ,t∥⋄

+

+

˜∆t+τ,t∥⋄ ≤
∥

8d4(G + U0 + K)2,

(S107)

Theorem 2 (High-noise seperability and classical simulation of bosonic model; reproduced from the main text).
Suppose ρ(t) is the state obtained after evolving the bosonic system for time t with an initial product state, then for
min(κ1, κ2)
2J the state ρ(t) is separable. Furthermore, there is a randomized classical algorithm that can sample
within ϵ total variation error of ρ(t) in O(Λ2t2m4L+8ϵ−

mΛt/ϵ)) time.

1polylog

≥

Proof. To prove Theorem 2, we will start with truncated ﬁrst-order Trotter approximation of ρ(t), i.e. with σT,
given in Eq. (S89). From Lemmas 11 and 12, we obtain that

(cid:0)

d

≤

ρ(t)
∥

−

σT,

d∥1 ≤

≤

O

Λ2t2m2d2
T

(cid:18)

(cid:19)

+ O

Λtm1

k0/2d2+k0/2e−

−

1

2 (d/d0m)1/α

,

(S108)

(cid:1)
where Λ = UC + Uos + JC + Jos + κ. Next, we use Lemma 13 to further approximate σT,
d with a separable state
ϕT . However, the noise rates at each step in the Trotterization need to be suﬃciently high to meet the necessary
conditions for separability [(C1) and (C2) provided in Lemma 13]—to ensure this, we make a choice of the parameters
p(l)
i,σ;j,σ′ (t), q(l)

i,σ;j,σ′ (t) in Eq. (S87) that we so far left unspeciﬁed:

(cid:0)

≤

p(1)
i,σ;j,σ′ (t) = p(2)

i,σ;j,σ′ (t) =

α,α′ |
ν

=i

P

k

q(1)
i,σ;j,σ′ (t) = q(2)

i,σ;j,σ′ (t) =

P

P

α,α′

P
|

=i

P

k

ν

J α,α′
i,σ;j,σ′ (t)
|
J α,α′
i,σ;k,ν(t)

α,α′
|
J α,α′
i,σ;j,σ′ (t)
|
J α,α′
j,σ′;k,ν(t)

α,α′

|

|

, p(3)

i,σ;j,σ′ (t) =

|
=i

Ui,σ;j,σ′ (t)

|
Ui,σ;k,ν(t)

,

|

ν |

k

P

, q(3)

i,σ;j,σ′ (t) =

|

P
Ui,σ;j,σ′ (t)
|
=i

|
Uj,σ′;k,ν(t)

ν |

,

|

(S109a)

k

P

P

P

P

P

̸
̸
̸
̸
(S109b)

(S109c)

(S109d)

(S109e)

(S109f)

and it can be checked that they satisfy the normalization condition in Eq. (S88). Considering now the channels
Φi,σ;j,σ′

d—to apply Lemma 13 to these channels, we need

1)δ from Eq. (S89) in Trotterized state σT,

τ δ,(τ

≤

−

21

(1) Imposing condition C1: For l

1, 2

∈ {

}

κlp(l)

i,σ;j,σ′ (t), κlq(l)

i,σ;j,σ′ (t)

2

≥

J α,α′
i,σ;j,σ′ (t)

|

or equivalently

Xα,α′ |

J α,α′
k,ν;k′,ν′ (t)

for (k, ν)

|

(i, σ), (j, σ′)

∈ {

.

}

κl ≥

2

Xk′

=k Xν′

Xα,α′ |

This condition can clearly be satisﬁed if κ1, κ2 ≥

2JC since

(2) Imposing condition C2:

k′

=k

ν′

α,α′ |

P

P

P

J α,α′
k,ν;k′,ν′ (t)

JC.

| ≤

i,σ;j,σ′ (t), κ3q(3)

κ3p(3)
κ3 ≥

2

i,σ;j,σ′ (t)

≥
Uk,ν;k′,ν′ (t)

Ui,σ;j,σ′ (t)

2
|
for (k, ν)

or equivalently

|

(i, σ), (j, σ′)

∈ {

.

}

|

|

Xk′

=k Xν′

This condition can clearly be satisﬁed if κ3 ≥

2UC since

k′

=k

ν′

|

Uk,ν;k′,ν′ (t)

UC.

| ≤

Now, assuming κ1, κ2 ≥

2JC and κ3 ≥

2UC, we can then approximate σT,

P

P

d by ϕT given by

≤

1

ϕT =

i,σ;j,σ′
τ δ,(τ

1)δ

os
τ δ,(τ

1)δρ(0),

Yσ,σ′ M
1)δ is the separability preserving completely-positive map corresponding to Φi,σ;j,σ′

Yτ =N (cid:18) Y

τ δ,(τ

i<j

(cid:19)

U

−

−

1)δ from Lemma 13,

−

i,σ;j,σ′
τ δ,(τ

where
which also satisﬁes

M

−

Φi,σ;j,σ′
∥

τ δ,(τ

−

1)δ − M

i,σ;j,σ′
τ δ,(τ

1)δ∥⋄ ≤

−

εi,σ;j,σ′
τ

,

(S109g)

where

εi,σ;j,σ′
τ

= 8d4

τ δ

(τ

(cid:18) Z

−

1)δ (cid:18) Xα,α′ |

We note that ε is deﬁned by

J α,α′
i,σ;j,σ′ (s)

ds +

|

|

Ui,σ;j,σ′ (s)

ds +

|

3

κl

p(l)
i,σ;j,σ′ (s) + q(l)

i,σ;j,σ′ (s)

ds

2

.

(S109h)

Xl=1

(cid:0)

(cid:19)

(cid:1)

(cid:19)

T

τ =1
X

8d4

8d4

ε =

≤

≤

εi,σ;j,σ′
τ

i,j:i<j
X
T

Xσ,σ′

τ δ

τ =1 (cid:18) Z
X

1)δ

(τ

−

JC + UC + 2κ

i,j;i<j (cid:18) Xα,α′ |
2 t2m2

X

T ≤

ds +

J α,α′
i,σ;j,σ′ (s)

|
32d4 Λ2t2m2

.

T

Ui,σ;j,σ′ (s)

ds +

|

|

3

κl

p(l)
i,σ;j,σ′ (s) + q(l)

i,σ;j,σ′ (s)

ds

2

Xl=1

(cid:0)

(cid:19)

(cid:1)

(cid:19)

(S110)

(cid:1)
Furthermore, we also note from the triangle inequality that

(cid:0)

i,σ;j,σ′
τ δ,(τ

Φi,σ;j,σ′

+

∥M
We can now bound the error between ϕT and σT,

∥M

1)δ∥⋄ ≤ ∥

1)δ∥⋄

τ δ,(τ

−

−

i,σ;j,σ′
τ δ,(τ

1)δ −

−

Φi,σ;j,σ′

τ δ,(τ

1)δ∥⋄ ≤

−

1 + εi,σ;j,σ′
τ

≤

exp(εi,σ;j,σ′
τ

).

(S111)

d using telescoping to obtain

≤

ϕT −

∥

σT,

d∥1 ≤

≤

eεε

≤

eO(Λ2t2m2d4/T 2)O

Λ2t2m2d4
T

.

(cid:19)

(cid:18)

Finally, using Eq. (S108), we obtain that

ρ(t)
∥

ϕT ∥1 ≤

−

eO(Λ2t2m2d4/T )O

Λ2t2m2d4
T

(cid:18)

+ O

(cid:19)

(cid:18)

Λ2t2m2d4
T

+ O

Λtm1

k0/2d2+k0/2e−

−

1

2 (d/d0m)1/α

(cid:19)

(cid:0)

(S112)

(S113)

.

(cid:1)

̸
̸
̸
̸
Thus, choosing

d = Θ

m polylog

(cid:18)

(cid:18)

mΛt
ϵ

, T = Θ

(cid:19)(cid:19)

(cid:18)

Λ2t2m6
ϵ

polylog

(cid:18)

mΛt
ϵ

(cid:19)(cid:19)

22

(S114)

ρ(t)

ensures that
normalized. We will instead consider ˜ϕT = ϕT /Tr(ϕT )—note that, if

ϵ. Finally, we note that ϕN by itself is guaranteed to be positive semi-deﬁnite but not
ϕT −
∥
1

ϕT ∥1 ≤

ϵ < 1,

∥1 ≤

ρ(t)

2ϵ

−

∥

(1)

Tr(ϕT )

where in (1) we have used that

(cid:12)
(cid:12)
(cid:12)
(cid:12)
Time-complexity of sampling in the Fock state basis. We now consider the cost of sampling from the state ˜ϕT . By

(cid:12)
(cid:12)
(cid:12)
ϕT −
(cid:12)

Tr(ρ(t))

Tr(ϕT )

Tr(ϕT )

∥1 ≤

| ≤ ∥

−
ϵ.

ρ(t)

1
|

=

−

−

|

|

ϕT −

ρ(t)

∥1 +

−
Tr(ϕT )

ρ(t)
∥

∥1

≤

1

ϵ ≤

O(ϵ),

(S115)

˜ϕT −
∥

ρ(t)

∥1 ≤

1
Tr(ϕN ) ∥

construction, ˜ϕT is a separable state and hence can be expressed as

˜ϕT =

pα

ρ(α)
i

,

(S116)

(cid:19)

i

(cid:18) O

≤

α
X
where pα is a probability distribution over α and ρ(α)
is a state supported on the modes at the ith site. To either
i
sample from or compute a local observable in ˜ϕT , we ﬁrst sample from pα and obtain a product state
from
the mixed state ensemble ˜ϕT . Given the initial state ρ
1)δ,
d(0) as a product state, we sequentially apply
normalize the result and sample from the resulting separable state to obtain another product state—since the input
1)δ, normalization and the subsequent sampling involves only the
state is a product state, each application of
O(m4Lpolylog(mΛt/ε)) time.
2L truncated bosonic modes at sites i and j and can be classically done in O(d4L)
Additionally, the application of the on-site unitaries (
1)δ) will map a product state between the diﬀerent sites
O(m3L+1polylog(mΛt/ε)) time. Counting
to another product state, and it can be applied classically in O(md3L)
the time needed to apply, in this manner, all
1)δ, the total classical run-time for drawing one
product state from ˜ϕT is thus O(T m2
1polylog(mΛt/ε)). Having drawn a
⊗iρ(α)
from the separable state ˜ϕT , we can now consider the task of drawing a sample in the Fock
product state
state basis: Given each ρ(α)
as a dL
on the Fock state basis requires
i
×
O(mL+1polylog(mΛt/ϵ)). Thus, the total time complexity of drawing a single sample
computational time O(ndL)
from ˜ϕT is dominated by the cost of sampling from pα and is O(Λ2t2m4L+8ϵ−

i,σ;j,σ′
1)δ and
τ δ,(τ
m4Lpolylog(mΛt/ε))

dL matrix, drawing a sample from

⊗iρ(α)
1polylog

O(Λ2t2m4L+8ϵ−

⊗iρ(α)

i
i,σ;j,σ′
τ δ,(τ

i,σ;j,σ′
τ δ,(τ

mΛt/ϵ)).

os
τ δ,(τ

os
τ δ,(τ

M

M

M

≤

≤

≤

×

≤

U

U

−

−

−

−

−

i

i

IV. HIGH-NOISE SEPARABILITY IN SPIN MODELS

(cid:0)

In this section, we analyze a spin model evolving under a 2-local Hamiltonian in the presence of noise, which closely
follows the analysis of the bosonic model in the previous section. We only provide a derivation of the counterpart
of Lemma 13 for the spin model, which outlines a suﬃcient condition for separability preservation for two qudits.
Combining this lemma with standard ﬁrst-order Trotterization can allow us to show that even in the many-body
regime, a suﬃciently high noise maps a separable state to another separable state.

Lemma 14 (Separability condition for spin models). Consider a Lindbladian on two d

level qudits given by

−

where κ(t)

≥

0. Here h(t) is a two-qudit Hamiltonian which we express as

(t) =

L

−

i[h(t),

·

] + κ(t)

DLi,k ,

1,2
Xi
∈{

} Xk

where we can assume sα(t)
each i
1, 2
}
any single qudit operator A

∈ {

, the jump operators Li,k satisfy

≥

0, Oi,α are Hermitian operators on the ith qudit with
2

Oi,α∥F ≤
∥
1 and have a full Kraus rank and
∃

Li,k∥

≤

1. Furthermore, for
λ0 > 0 such that for

h(t) =

sα(t)O1,α ⊗

O2,α,

α
X

k ∥

P

Tr(L†i,kA)

2

|

≥

A
λ0 ∥
∥

2
F .

|

Xk

α sα(t)/λ0, there is a completely positive map

Mt+τ,t which maps separable states to separable states

23

Then if κ(t)
and

≥

P

Proof. It will be convenient to introduce the scalars

Mt+τ,t − T

exp

t

(cid:18) Z

t+τ

(s)ds

L

(cid:13)
(cid:13)
(cid:13)
(cid:13)

t+τ

4
(cid:18) Z

t

≤

⋄

t+τ

t+τ

κ(t′)dt′ +

sα(t′)dt′

t

α Z
X

t+τ

2

.

(cid:19)

(cid:19)(cid:13)
(cid:13)
(cid:13)
(cid:13)

Sα =

sα(t′)dt′, S =

Sα and K =

κ(t′)dt′.

(S117)

t

Z

α
X

t

Z

We will also deﬁne

qeﬀ
i (t) =

κ(t)
2

L†i,kLi,k, qeﬀ = qeﬀ

1 (t)

Xk
Consider the following completely positive map
Rt+τ,tρ = Ez

I + I

⊗

⊗

qeﬀ
2 (t) and Qi = exp

t+τ

−

t

Z

(cid:18)

qeﬀ
i (t′)dt′

.

(cid:19)

(R1(z)

⊗

R2(z))ρ(R†1(z)

R†2(z))

,

⊗

(S118)

(S119a)

where

(cid:0)

(cid:1)

R1(z) = Q1 + e−

iπ/4

zα

SαO1,α and R2(z) = Q2 + e−

iπ/4

z∗α

SαO2,α,

(S119b)

Rt+τ,t is separability preserving
where zα are drawn uniformly and independently from the set
i.e. maps a separable state to another separable state. Explicitly evaluating the expectation value in Eq. (S119), we
obtain

{±

±

1,

i

α
X

p

α
X
. We note that
}

p

Rt+τ,t(ρ) = (Q1 ⊗

Q2)ρ(Q†1 ⊗

Q†2)

−

i

Sα

(O1,α ⊗

O2,α)ρ(Q†1 ⊗

Q†2)

(Q1 ⊗

Q2)ρ(O1,α ⊗

−

O2,α)

+

Sα

(O1,α ⊗

α
X
(cid:0)
Q2)ρ(O1,α ⊗

Q†2) + (Q1 ⊗

O2,α)ρ(Q†1 ⊗

O2,α)

+

(cid:1)

α
X

(cid:0)
SαSα′

(O1,α ⊗

O2,α)ρ(O1,α′

O2,α′ ) + (O1,α ⊗

⊗

(cid:1)
O2,α′ )ρ(O1,α ⊗

O2,α′ )

,

(S120)

where using

Qi∥ ≤

∥

1,

∥

Xα,α′
I
Qi −

∥ ≤

(cid:0)
K/2,

t+τ

Qi −
∥

(I

−

qeﬀ
i )

∥ ≤
t+τ

K 2/8, we obtain that

(cid:1)

Rt+τ,t(ρ) = ρ

−

i

t

Z

α
X
t+τ

= ρ +

t

Z

[h(t′), ρ]dt′

Sα(O1,α ⊗

t

qeﬀ(t′), ρ
dt′+
−
{
}
Z
I)ρ(O1,α ⊗

I) + (I

⊗

O2,α)ρ(I

O2,α)) + ∆t+τ,t(ρ)

⊗

(t′)ρdt′

L

− Gt+τ,tρ + ∆(R)

t+τ,t(ρ),

where

Gt+τ,t is a superoperator given by

(1)
t+τ,t ⊗

Gt+τ,t =
(i)
t+τ,t(ρ) = K
G

G

id + id
⊗ G
Li,kρL†i,k −

(2)
t+τ,t, where

SαOi,αρOi,α,

α
X

Xk

and ∆t+τ,t is a super-operator with

Furthermore, the channel generated by the Lindbladian can be expanded to the ﬁrst order to obtain

∆(R)
∥

t+τ,t∥⋄ ≤

2K 2 + 4SK + 2S2 = 2(S + K)2.

t+τ

L

exp

T

t

(cid:18) Z

(s)ds

= ρ +

(cid:19)

t+τ

L

t

Z

(t′)ρdt′ + ∆(L)

t+τ,t,

(S121)

(S122)

(S123)

(S124)

24

(S125)

(S126)

where, since

(t)

∥L

∥⋄ ≤

2(

α sα(t) + κ(t)), ∆(L)

t+τ,t is a superoperator with

P

Consequently, we have that

∆(L)
∥

t+τ,t∥⋄ ≤

2

S + K

2

.

(cid:0)

(cid:1)

t

exp

T

0 L

(cid:18) Z

(s)ds

−

(cid:19)

(cid:0)

(cid:13)
(cid:13)
(cid:13)
(cid:13)

Rt+τ,t +

Gt+τ,t

4(S + K)2.

≤

⋄

(cid:1)

(cid:13)
(cid:13)
(cid:13)
(cid:13)

Rt+τ,t is separability preserving by construction. Furthermore,

We note that
individually on the two qudits—consequently,
To ﬁnd a suﬃcient condition for complete positivity of
semi-deﬁnite. From Eq. (S122), we obtain that

Gt+τ,t is a sum of super-operators acting
Gt+τ,t will be separability preserving as long as it is completely positive.
(i)
t+τ,t, we will impose that its Choi state, Φ
(i) , is positive

G

G

d

K

(i) =

Φ

G

Xj,j′=1 (cid:18)
j, j′

|

⟩ ∈

Xk
Cd

⊗

Li,k |

j

j′

L†i,k −

|

⟩⟨

SαOi,α |

j

⟩⟨

|

j′

Oi,α

α
X
Cd is a two-qudit state and Ψ =

j

j′

.

|

⟩⟨

⊗ |

(cid:19)

(S127)

j,j′ ψj,j′

j′

j

|

⟩⟨

|

is its corresponding

Now, suppose
matrix, then

=

ψ

|

⟩

P

j,j′ ψj,j′

Φ

ψ

|

⟨

G

(i)

ψ

|

⟩

= K

Tr(L†i,kΨ)

|

2

|

−

Xk
Ψ
Kλ0 ∥

(1)

≥

2
F −
∥

Sα ∥
2 ,

α
X
ψ

P

Tr(Oi,αΨ)

2

|

Sα|

α
X
Oi,α∥

2
F ∥

Ψ

2
F
∥

= (Kλ0 −
where in (1) we have used the fact that Tr(A†B)2
2
λ0 ∥
F from the lemma statement. Therefore, if K
∥
(i) are completely positive. This in turn implies that the super-operator
then
G
completely positive and separability preserving, which proves the lemma.

Tr(A†A)Tr(B†B) and also the condition
k |
S/λ0, which is implied by the condition κ(t)
P
≥
Rt+τ,t +

Mt+τ,t =

≤
≥

S)

⟩∥

Ψ

∥|

(S128)

2

Tr(L†i,kΨ)

≥
|
α sα(t)/λ0,
Gt+τ,t is both
P

Similar to the case of the fermionic and bosonic models, this lemma can be combined with ﬁrst-order Trotterization
in the many-body setting to show high-noise separability for a broad class of noise models. In particular, we could
consider noisy dynamics described by the master equation

with Li,k satisfying the conditions in Lemma 14 and

d
dt

ρ(t) =

−

i[H, ρ(t)] + κ

DLi,k

Xi,k

H(t) =

hi(t) +

i
X

i<j
X

α
X

si,j
α (t)(Oi,α ⊗

Oj,α),

(S129)

(S130)

where Oi,α would be a Hermitian operator acting on the ith qudit chosen to be normalized such that
Introducing the “inter-site interaction-strength” parameter J as the smallest number satisfying

Oi,α∥F = 1.
∥

si,j
α (t)

+

|

|

j>i
X

j<i
X

sj,i
α (t)

|

| ≤

J for all i, t

0,

≥

(S131)

we can then establish using Lemma 14 that if κ
into a separable state.

≥

J/λ0, then an initial separable state of the spins always evolves

V. COUNTER-EXAMPLES

In this section, we consider the question of whether a counterpart of Theorem 1 can be obtained for the bosonic

model, and if a counterpart for Theorem 2 can be established for the fermionic model.

25

FIG. S1. Representation of the Wigner function for the state ρ(t) obtained by evolving Eq. (S133) with initial state ρ(0) =
|α⟩ ⟨α|, with parameters U = 0.05 and t = 0.5. (a) The Wigner function W (x, p) is represented in phase space for α = 5
and error rate κ = 0.1U (left) and κ = 2U (right). (b) Representation of the minimum value of the Wigner function Wmin =
minx,p W (x, p). One can clearly observe that, for a ﬁxed value of κ/U , the Wigner function becomes more negative by increasing
α, which suggest that the Gaussian resources can eﬀectively boost the non-Gaussianity of the system. Hence, even for large
values of κ, a negative Wigner state might be reached, by increasing α.

A. High-noise regime for the bosonic model is not convex-Gaussian at all times

≫

We will provide evidence that there is no counterpart of Theorem 1 for bosonic systems. That is, even with noise
rates larger than the non-Gaussianity (κ
U ), one can still obtain states which are not convex-Gaussian. In section
V A 1, we provide numerical evidence that, with a single bosonic mode and dephasing noise greater than the non-
U ), states with negative Wigner function can be reached, which automatically implies lack of
Gaussianity (κ3 ≥
convex Gaussianity. In section V A 2, we provide a stronger argument in the absence of dephasing noise: for noise
models containing only incoherent particle loss and gain (κ3 = 0), one can perform high-ﬁdelity arbitrary gates even
if the non-Gaussianity is much smaller than the noise rate, U
κ, provided that the Gaussian couplings J, Ω can
be made suﬃciently large, enabling the implementation of gates with eﬀective error rates below the fault tolerance
threshold [S8–S10]. As a consequence, not only is the state not guaranteed to remain convex-Gaussian, but the
classical simulation of local observables is provably BQP-hard.

≪

1. High dephasing noise regime

Here, we provide a simple example with a single bosonic mode, where dephasing noise, no-matter how high, is
unable to make the state convex Gaussian. Our analysis is centered on the Wigner function, which, for a single
bosonic mode state ρ, is deﬁned as

W (x, p) =

1
π

∞

Z

−∞

x

⟨

−

ρ

y

|

|

x + y

⟩

e2ipydy.

(S132)

Since quantum states with positive Wigner functions can be eﬃciently simulated [S11], the negativity of the Wigner
function is regarded as a necessary resource for quantum advantage. Furthermore, a negative Wigner function rules out
convex-Gaussianity, since all pure Gaussian states have nonnegative Wigner functions [S12, S13], and as a consequence
convex Gaussian states do as well.

Speciﬁcally, we consider an initial state ρ(0) =

=
α
|
, with α a real number. Then, the state is evolved under the Hamiltonian H = U n2 and dephasing noise

represents the single-mode coherent state

, where

vac

⟩ ⟨

α

α

α

⟩

⟩

|

|

|

a)

eα(a†
of rate κ3 = κ, which yields the master equation

−

⟩

|

d
dt

ρ(t) =

ρ(t) =

L

−

iU [n2, ρ(t)] + κ

nρ(t)n

(cid:18)

1
2 {

n2, ρ(t)

−

.

}
(cid:19)

(S133)

In this setting, we numerically compute the minimum value of the Wigner function, Wmin = minx,p W (x, p), and
represent it in Fig. S1. One can appreciate that, even when κ
U , using a suﬃciently large α results in a state with
a negative Wigner function. Consequently, we do not expect an analogue of Theorem 1 to hold for bosons: even for
a high dephasing noise rate, with a suﬃciently large Gaussian displacement, an initially Gaussian state can evolve
into Wigner negative (not convex-Gaussian) states at short times. The time-scale at which the state becomes Wigner
negative is determined by both the value of U , as well as the displacement. For the one-mode problem considered

≥

Æ = 3.0
Æ = 3.5
Æ = 4.0
Æ = 4.5
Æ = 5.0

x
a
m
W
/
n
m
W
°

i

0.00025

0.00020

0.00015

0.00010

0.00005

0.00000

x
a
m

0.008

0.006

i

n
m

0.004

°

0.002

0.000

Æ = 3.0
Æ = 3.5
Æ = 4.0
Æ = 4.5
Æ = 5.0

0.04

0.03

0.02

i

n
m

0.01

°

0.00

26

Æ = 3.0
Æ = 3.5
Æ = 4.0
Æ = 4.5
Æ = 5.0

0

5

10
15
Time ∑t

20

25

30

0

5

10

15
Time ∑t

20

25

30

0

5

10

15
Time ∑t

20

25

30

FIG. S2. The relative Wigner negativity, quantiﬁed by −Wmin/Wmax = − minx,p W (x, p)/ maxx,p W (x, p), for a single bosonic
mode evolving under the Hamiltonian H = U n2 as well as dephasing noise at rate κ. The initial state of the bosonic mode is
the coherent state |α⟩. As expected, the relative Wigner negativity decreases as U decreases, and at a ﬁxed α, the maximum
Wigner negativity is attained at time-scales of 1/U .

above, Fig. S2 shows the relative wigner-negativity
minx,p W (x, p)/ maxx,p W (x, p) as a function
−
U , there is
of time. We ﬁnd that while the state eventually becomes Wigner non-negative, even in the regime κ3 ≫
an intermediate temporal region that depends on U and α where the state is Wigner negative. For a ﬁxed α, the
time t∗ at which the state is maximally Wigner negative scales as 1/U , consistent with the fact that U determines
the strength of the process generating the non-Gaussianity or Wigner negativity in the dynamics.

Wmin/Wmax =

−

We remark that this does not necessarily imply simulation hardness: the question of whether there is a threshold
error κth(U ) depending on U but not on J, Ω above which the classical simulation becomes tractable remains open.

2. High incoherent particle loss and gain regime

Here we analyze the complexity of classically simulating the bosonic system in the absence of dephasing noise
(κ3 = 0) and ﬁnd that the problem does not become easy above a noise threshold depending exclusively on the
non-Gaussian interaction strength, thus showing that no counterpart of Theorem 1 can exist for bosons in the absence
of dephasing noise. Speciﬁcally, we show that, even when the non-Gaussian interaction strength is much smaller than
the noise strength, U
κ, one can perform arbitrarily fast gates. Due to the threshold theorem, this allows for
the implementation of fault-tolerant schemes [S8, S10]. To show this, it is enough to consider systems with only one
bosonic mode per site (L = 1) and only onsite non-Gaussianity (UC = 0).

≪

We will start with a technical lemma: we will show that, for a system with m modes evolving under the noise model

in Eq. (S27), the error induced by the noise can be upper bounded by O(mκt).

Lemma 15 (Error bound between noisy and noiseless evolution). Consider a bosonic system with m modes evolving
under the master equation

d
dt

ρ(t) =

ρ(t) =

L

−

i[H(t), ρ(t)] +

2

m

Xl=1

v=1
X

κlDL(l)

v

,

DLρ = LρL†
where
− {
ρ(0) lies in the subspace
Hamiltonian H(t) contains no couplings between the state

v = a†v, and κ1 + κ2 = 1. Assume that, for some integer d,
, and that the
d
⟩}
with k > d. Then, denoting by

d of the Hilbert space spanned by the ﬁrst d + 1 levels

and any state

, . . . ,

0
⟩

H≤

{|

k

d

|

/2, L(1)
L†L, ρ
}

v = av, L(2)

the time-evolution in the noiseless case (κ = 0), the error induced by the dissipation

|

⟩

|

⟩

·

(

) =

exp

i
U
T
can be bounded as
R

−

(cid:16)

t
0 [H(s),

]ds

·

(cid:17)

Proof. Let us consider the following eﬀective Hamiltonian:

t

exp

T

0 L

(cid:18)Z

(s)ds

ρ(0)

(cid:19)

ρ(0)

− U

(cid:13)
(cid:13)
(cid:13)
(cid:13)

2mκt(d + 1).

1 ≤

(cid:13)
(cid:13)
(cid:13)
(cid:13)

Heﬀ = H

i

1
2

−

m

v=1
X

(cid:0)

κ1a†vav + κ2ava†v

.

(cid:1)

(S134)

Then, the time evolution may be written as

ρ(t) =

exp

T

t

0 L

(cid:18)Z

t

(s)ds

ρ(0) =

(cid:19)

exp

T

i

−

(cid:18)

0

Z

[Heﬀ (s),

·

]ds

ρ(0)

+

(cid:19)

(ρ(0)) = σ +

(ρ(0)),

N

N

(S135)

σ

27

|

{z

where σ is the (unnormalized) state obtained by evolving under the eﬀective Hamiltonian, and
positive channel that is not trace preserving. Naturally, tr(σ) + tr(
output when no errors occur, while

(ρ) captures the output with one or more errors.

(ρ) is a completely
(ρ)) = 1. The state σ can be understood as the

N

N

For the vth bosonic mode, we deﬁne the projector that truncates to at most d particles as Πv,

.
|
d. Note that, since H does not contain couplings to higher levels,
Then, Π
neither does Heﬀ . As a consequence, the dynamics of σ are constrained to the ﬁrst d + 1 levels, and can be truncated.
Let us denote the truncated Hamiltonians by ˜H = ΠdHΠd, ˜Hdis = ΠdHdisΠd. Using the deﬁnition of ˜Hdis in

d is the projector onto

⊗vΠv,

d =

d =

H≤

P

⟩ ⟨

≤

≤

≤

j

j

Eq. (S134), the operator norm of the truncated eﬀective Hamiltonian ˜Hdis can then be bounded as

d
j=0 |

N

}

˜Hdis∥ ≤
∥

m
2

(κ1d + κ2(d + 1))

m
2

≤

(κ1 + κ2) d

mκ
2

≤

(d + 1).

Let us now write σ in a more convenient form as σ = limN

(ON ρ(0)O†N ), where

→∞

N

ON =

Yk=1 (cid:16)

i ˜H(kt/N )t/N e−

e−

i ˜Hdist/N

.

(cid:17)

(S136)

(S137)

This expression can be derived, for example, from standard Trotterization techniques. We would now like to bound
tr(σ), which can be understood as the probability of no errors occurring during the computation. Naturally, the
unitary parts of the evolution in Eq. (S137) are trace preserving, and we only need to bound the imaginary time
evolution induced by the Hamiltonian ˜Hdis. Note also that, using Eq. (S136), the minimum singular value in each
step can be bounded as

σmin(e−

˜Hdist/N )

exp

≥

mκ
2

t
N

−

(κ1(d + 1) + κ2(d + 1))

(cid:18)
As a consequence, using Eq. (S137) and Eq. (S138), it can be easily checked that

(cid:19)

(cid:18)

exp

≥

mκ
2

t
N

−

(d + 1)

.

(S138)

(cid:19)

σmin(O†N ON )

This allows us to bound the trace as

σmin(e−

˜Hdist/N )

≥

h

2N

i

exp [

−

≥

mκt(d + 1)] .

tr(σ) = lim
→∞

N

tr(O†N ON ρ(0))

lim
N
→∞

≥

σmin(O†N ON )tr(ρ(0))

exp [

−

≥

mκt(d + 1)] .

(S139)

(S140)

As a consequence, since the total evolution of the system must be trace preserving, it immediately follows that
tr(

N
Now, let us bound the distance between σ and the state obtained under ideal (noiseless) evolution,

(ρ(0))

mκtd2

e−

−

≤

1

.

We use the fact that

∂
∂κ

˜Hdis

t
N =

e−

t
N

˜Hdis
κ

−

˜Hdis

t
N

e−

and

˜Hdis

t
N

e−
∥

,
∥

e−
∥

i ˜H(κt/N ) t
N

1.

∥ ≤

Using Eq. (S136), one can bound

t
N

˜Hdis
κ

˜Hdis

t
N

e−

t
N κ ∥

˜Hdis∥ ≤

mt(d + 1)
2N

.

≤

∂
∂κ

˜Hdis

t
N

e−

=

(cid:13)
(cid:13)
(cid:13)
(cid:13)

(cid:13)
(cid:13)
(cid:13)
(cid:13)
(cid:13)
1, one can bound

(cid:13)
(cid:13)
(cid:13)
(cid:13)

(cid:13)
(cid:13)
(cid:13)
(cid:13)
(cid:13)

Furthermore, using the deﬁnition of ON in Eq. (S137), the norm bound in Eq. (S142), and the fact that
e−
∥

i ˜H(κt/N ) t
N

e−
∥

∥ ≤

˜Hdis

,
∥

t
N

σ

∥

ρ(0)

∥1.

− U

(S141)

(S142)

∂
∂κ

ON

∂
∂κ

σ

(cid:13)
(cid:13)
(cid:13)
(cid:13)

2

≤

(cid:13)
(cid:13)
(cid:13)
(cid:13)

(cid:13)
(cid:13)
(cid:13)
(cid:13)

(cid:13)
(cid:13)
(cid:13)
(cid:13)

2t
κ ∥

˜Hdis∥ ≤

≤

mt(d + 1).

(S143)

This directly yields a bound on the desired distance:

Finally, this, together with Eqs. (S135, S144), implies that

σ

∥

ρ(0)

∥1 =

− U

κ

∂
∂κ

0

Z

σdκ

(cid:13)
(cid:13)
(cid:13)
(cid:13)

1 ≤

(cid:13)
(cid:13)
(cid:13)
(cid:13)

28

(S144)

∂
∂κ

σ

k

Z

0 (cid:13)
(cid:13)
(cid:13)
(cid:13)

1

(cid:13)
(cid:13)
(cid:13)
(cid:13)

dκ

≤

mκt(d + 1).

t

exp

T

0 L

(cid:18)Z

(s)ds

ρ(0)

(cid:19)

ρ(0)

− U

(cid:13)
(cid:13)
(cid:13)
(cid:13)

which proves the lemma.

ρ(t)

1 ≤ ∥

σ

∥1 +

−

∥N

(ρ(0))

∥1 ≤

mκt(d + 1) + 1

mκt(d+1)

e−

−

≤

2mκt(d + 1),

(S145)

(cid:13)
(cid:13)
(cid:13)
(cid:13)

We will now show how one can use a single bosonic mode Hamiltonian to apply arbitrary single qubit gates with
high ﬁdelity, even when the nonlinearity is much smaller than the noise strength. We note that a similar result is
already shown in Refs. [S14, S15]. To do this, we will consider a single bosonic mode with κ
U , where both the
error rate and non-Gaussianity U are ﬁxed, and study the eﬀective error rate in the asymptotic limit of large Gaussian
strength.

≫

Lemma 16 (Single-qubit gates, from Ref. [S14]). Consider a single bosonic mode under the master equation

d
dt

ρ =

ρ =

L

−

i[H(t), ρ] +

2

Xl=1

κlDL(l) ρ,

with Hamiltonian

H(t) = U (t)a†

2a2 +

Λ1(t)a† + Λ2(t)a†

2 + h.c.

+ ∆(t)a†a,

DLρ = LρL†
where
Gaussian terms is bounded by P ,
(i.e.
) = U (
(
U
˜O(κ(U 2P )−

− {

1/3), in time t = O((U 2P )−

·

|

·

,
|
|
)U † for some single-qubit gate U ), the Lindbladian

Λ1(t)

Λ2(t)

| ≤

|

|

1/3), with ρ0 a single-qubit state.

L

/2, L(1) = a, L(2) = a† and L(3) = a†a = n, and κ1 + κ2 = κ, and the strength of the
L†L, ρ
}

P . Then, for any single-qubit quantum unitary operation

∆(t)

,

,

(

∥

T

U

eR t

0 L

(s)ds

− U

U
)ρ0∥1 ≤

(t) can approximate

(cid:0)

(cid:1)

Proof. We will show that, by tuning the parameters in the Hamiltonian H(t), one can generate T , S, and √X gates,
which is suﬃcient for arbitrary single-qubit rotations. For implementing a T gate or an S gate, one simply has to set
2a2)/2 + P a†a. Since there are no couplings between
Ω(t) = 0 and ∆(t) = P . This yields the Hamiltonian H = U (a†
. Denoting the projector
1
0
the states
⟩}
⟩
onto this subspace Π1 =
.
1
|
Then, evolving under the Hamiltonian for time t = 3π/(2P ) yields an S gate, while evolving for time t = 3π/(4P )
yields a T gate. Therefore, applying the error bound in Lemma 15, T gates and S gates can be implemented with
precision O(κ/P ) in time t = O(1/P ).

, the projection of Hα on the blockaded subspace yields Π1HΠ1 = P

and the rest, we can restrict ourselves to the subspace spanned by

1
⟩ ⟨

0
⟩

1
⟩

1
|

0
|

⟩ ⟨

⟩ ⟨

+

{|

0

1

|

|

|

,

|

|

,

|

Now, let us consider the problem of applying a √X gate. This can be done by using the construction from
Refs. [S14, S16], by going to a displaced frame. We will ﬁrst show that, considering the Hamiltonian in a displaced
frame, one can implement a fast √X gate. Then, we will show that one can go to the displaced frame by applying
fast pulses at the beginning and end of the computation, hence enabling the application of a high-ﬁdelity fast √X
gate in the laboratory frame, even in the presence of errors.

First, let us consider the Hamiltonian in a frame displaced by α(t), a

a + α(t). We write the Hamiltonian in the

displaced frame as Hα(t) and the noise as

DL(l);α(t). Note that the noise in the displaced frame can be written as

→

2

Xl=1

κlDL(l),α(t)(

·

) =

2

Xl=1

κlDL(l) +

i
2

(κ1 −

κ2)

i(α(t)a†

α∗(t)a), (

−

(cid:2)

.

)

·

(cid:3)

(S146)

Furthermore, the displaced Hamiltonian Hα(t) may be written as

Hα(t) = U (t)a†

2a2 + ˜∆(t)a†a + (˜Λ1(t)a† + ˜Λ2(t)a†

2 + ˜Λ3(t)a†

2a + h.c.),

(S147)

where

˜∆(t) = ∆(t) + 4U (t)
2,
˜Λ2(t) = Λ2(t) + 2U (t)α(t)2,

α(t)

|

|

˜Λ1(t) = Λ1(t) + α∆(t) + 2α(t)∗Λ2(t) + 2U (t)

2α(t)

α(t)

|

|

1
2

−

iα(t)(κ1 −

κ2),

˜Λ3(t) = 2U (t)α(t).

29

(S148)

where the noise term from Eq (S146) has already been absorbed into the Hamiltonian. The master equation in the
displaced frame is then

d
dt

ρα(t) =

Lα(t)ρα(t) =

−

i[Hα(t), ρα(t)] +

2

Xl=1

κlDL(l) .

(S149)

−

By suitably choosing the parameters so that ˜∆(t) = ˜Λ1(t) = ˜Λ2(t) = 0, the Hamiltonian becomes Hα(t) =
2U (t)α(t)a†(n

1) + h.c..

|

|

1

−

+

⟩ ⟨

0
|

1
|

0
⟩ ⟨

Crucially, one can notice that the Hamiltonian Hα(t) is blockaded, since it does not contain couplings to state

.
2
⟩
. Denoting
, the projection of Hα(t) onto the blockaded subspace yields
2U α(t)X. Let us pick a constant α(t) = αF . It is then clear that evolving under the Hamiltonian

Therefore, in the noiseless case, the dynamics will be restricted to the qubit subspace spanned by
the projector onto this subspace by Π1 =
Π1Hα(t)Π1 =
HαF for a time t = π/(8U αF ) produces a √X gate.

fulﬁll Eq. (S148) and the restriction that

We will pick the displacement to be αF = Θ((P/U )1/3), since it is the largest displacement that can simultaneously
∆(t)
Naturally, one is interested in performing operations in the laboratory frame, which means that at the beginning
(t = 0) and end (t = tF ) of the computation the displacement is α(0) = α(tF ) = 0. This can be achieved by simply
applying a displacement term in the beginning and end of the computation. Hence, the computation can be performed
in three steps. First, a displacement term is applied for a time tdis to go from α(0) = 0 to α(tdis) = αF . Then, the
gate is performed in the frame displaced by αF , which takes time tgate = π/(8U αF ). Finally, the displacement is
taken to 0 again, which takes time tdis. Therefore, the total computation time for a √X gate is t√X = 2tdis + tgate.

Λ2(t)

Λ1(t)

0
⟩

| ≤

P .

⟩}

{|

1

|

|

|

|

,

|

,

|

|

,

In order to achieve the desired displacement αF , one can apply the Hamiltonian

H(t) = i(P

αF κ/2)(a†

−

a) +

−

i
2

(P

αF )t(κ1 −

−

κ2)(a†

a),

−

(S150)

where the ﬁrst term takes the system to the frame displaced by α(t) = (P
contributions of the noise. The choice of parameters ensures that
Λ1| ≤
frame, the system evolves under the master equation

|

αF κ/2), and the second term corrects the
−
P at all times. Speciﬁcally, in the displaced

3

ρα(t) =

d
dt

κlDL(l)

≤

for

t

tdis,

(S151)

Xl=1
1/3). Let us denote the total
with α(0) = 0 and α(tdis) = αF , and tdis = αF /(P
1/3), while tdis = O(αF /P ) =
evolution time by t√X = 2tdis + tgate. Note that tgate = O((U αF )−
O((P 2U )−
tgate, and the total time scales as t√X = tgate +
1/3). From the Solovay-Kitaev theorem, it follows that any single-qubit rotation can
2tdis = O(tgate) = O((P U 2)−
be approximated to precision ε in time t = O(t√X logc(1/ε)) for some constant c < 2. We can now bound the total
contribution of the error: straightforward application of Lemma 15 shows that the error after time t = ˜O(t√X ) =
˜O((U 2P )−

In the large P limit, it is clear that tdis ≪

αF ) = O(αF /P ) = O((P 2U )−
1) = O((P U 2)−

1/3) is

1/3).

−

where ˜O hides polylogarithmic factors. This proves the lemma.

eR t

0 L

(s)ds

(
∥

T

)ρ0∥1 ≤

− U

˜O

κ
(U 2P )1/3

,

(cid:19)

(cid:18)

(S152)

So far we have shown that one can make arbitrary single-qubit gates with high ﬁdelity even if the noise is much
κ3/U 2.

larger than the non-Gaussianity, κ
We will now show how to implement entangling gates, which is enough to obtain a universal gate-set.

U , as long as one can increment the strength of the Gaussian terms, P

≫

≫

30

(S153)

(S154)

Lemma 17 (Two-qubit gates). Consider two bosonic modes evolving under the master equation

d
dt

ρ(t) =

−

2

2

i[H(t), ρ(t)] +

Xl=1
where H(t) is the Hamiltonian H(t) = H1(t) + H2(t) + ig(t)[a1a†2 −
Λi,1(t)a†i + Λi,2(t)a†
Hi(t) = Ui(t)a†

2
i a2

i +

and
DLρ = LρL†
terms is bounded by P (

/2, L(1)
L†L, ρ
}
,
Λi,1(t)
| ≤
Then, for any two-qubit quantum unitary operation

(cid:16)
v = av, L(2)
∆i(t)
,
Λi,2(t)

g(t)

− {

|

|

|

|

|

,

|

|

P ).

(
·
(t) can implement a time evolution that approximates

(i.e.

U

U

Lindbladian
a time t = O((U 2P )−

L

1/3), with ρ0 a two-qubit state.

κlDL(l)

v

,

v=1
X
a†1a2], with

2
i + h.c.

+ ∆i(t)a†i ai,

(cid:17)

v = a†v, and κ1 + κ2 = κ. Assume that the strength of the Gaussian

) = U (
(
∥

U

T

,

)U † for some single-qubit gate U ), the
·
eR t
1/3), for

˜O(κ(U 2P )−

(s)ds

0 L

)ρ0∥1 ≤

− U

Proof. In Lemma 16 it is shown how to use H(t) to generate arbitrary single-qubit gates on either of the modes with
arbitrarily high ﬁdelity. Hence, it is only necessary to show how to apply an entangling two-qubit gate in order to
have a universal gate-set.

To do this, let us consider the collective modes b1 = (a1 + a2)/√2 and b2 = (a1 −
j, k
⟩n1,n2
⟩a1,a2
|
One obtains that

the Fock states in the original basis, and

1/2(a†1)j(a†2)k

= (j! k!)−

0, 0
⟩

j, k

|

|

a2)/√2. We will denote by
.
= (j! k!)−

1/2(b†1)j(b†2)k

0, 0
⟩

|

0, 0

⟩a1,a2

0, 1

⟩a1,a2

1, 0

⟩a1,a2

1, 1

⟩a1,a2

|

|

|

|

=

=

=

=

,

⟩b1,b2
1, 0

(cid:16)

|

|

(cid:16)
2, 0

|

0, 0
1
√2
1
√2
1
2

|

(cid:16)

⟩b1,b2 − |

0, 1

⟩b1,b2

1, 0

⟩b1,b2

+

|

0, 1

⟩b1,b2

0, 2

⟩b1,b2 − |

⟩b1,b2

,

,

(cid:17)

(cid:17)
.

Let us now denote by U the single-mode unitary that maps U
Eq. (S155), it can be seen that U will act in the a1, a2 basis as

0

|

⟩b1

=

|

(S155)

1

|

⟩b1

= i

, U

1
⟩b1

|

2

|

⟩b1

=

2
⟩b1

|

. Using

(cid:17)
0
⟩b1

, U

U

U

U

U

0, 0

⟩a1,a2

0, 1

⟩a1,a2

1, 0

⟩a1,a2

1, 1

⟩a1,a2

|

|

|

|

=

=

=

=

0, 0
|
1
2
1
2
(cid:16)
1, 1

(cid:16)

|

⟩a1,a2
(1 + i)

⟩a1,a2

,

.

0, 1

⟩a1,a2 −

|

(1

i)

|

−

1, 0

⟩a1,a2

(1

i)

|

−

0, 1

⟩a1,a2

+ (1 + i)

1, 0

|

−

(cid:17)
⟩a1,a2

,

,

(cid:17)

(S156)

Hence, U is clearly an entangling gate between modes a1 and a2. Furthermore, U can be implemented in a fast
manner using the same technique as in Lemma 16. Let us detail the procedure. First, one can evolve the system
b2 in time t = O(1/P ). The
under the term P (a†1a2 + h.c), which induces the mixing of the modes a1 →
Hamiltonian in the new basis, Hb(t), may be written us

b1 and a2 →

Hb(t) = U1b†

2
1 b2

1 + (Λ1,1b†1 + Λ1,2b†

2
1 + h.c.) + ∆1b†1b1,

(S157)

where we have chosen ∆2 = Λ2,1 = Λ2,2 = U2 = 0. One can note that the technique in Lemma 16 can be readily
applied to the Hamiltonian Hb in Eq. (S157). That is, one can go to a frame in which b1 is displaced by α(t),
b1 + α(t). As shown in the proof of Lemma 16, a suitable choice of the parameters leads to the displaced
b1 →
Hamiltonian Hb,α(t) = U1(t)(b†1)2b2
2) + h.c.]. Note that this Hamiltonian contains no couplings
is blockaded. Furthermore, one can
and
between
rewrite

, and hence the subspace spanned by

1 + 2U1[α(t)b†1(b†1b1 −

2
⟩b1 }

3
⟩b1

⟩b1

⟩b1

⟩b1

{|

2

1

0

|

|

|

|

,

,

Hb,α(t) = U1(t)(b†1)2b2

1 + 2U1(t)Re(α(t))Hα,R + 2U1(t)Im(α(t))Hα,I ,

(S158)

with Hα(t),R = b†1(b†1b1 −
[Hα(t),R, Hα(t),I ] = 2i(3b†

2)+(b†1b1 −
2
1 b2
1 −

2)b1 and Hα(t),I = i(b†1(b†1b1 −

2)b1). One can compute the commutator
(b†1b1 −
6b†1b1 + 4), which is diagonal, and can clearly implement the gate U , which consists

2)

−

31

. In fact, the analysis in Ref. [S14] shows that one can generate arbitrary

only of a phase rotation of the state
unitaries in the subspace spanned by

1
⟩b1
0
⟩b1

|
{|

2
⟩b1 }
Following the analysis in Lemma 16, the gate U can then be implemented in time tU = O((U 2P )−

⟩b1

1

,

|

,

|

.

is also the dominant source of error, since applying the displacement takes time tdis = O((P 2U )−
to the collective mode b1 takes time tb = O(1/P ), and therefore tU ≫
O(κtU ) = O(κ(U 2P )1/3).

1/3). This
1/3), and going
tdis, tb. Hence, the total error will be

Therefore, we have shown how to implement an entangling gate. Together with the implementation of arbitrary
single-qubit gates and the Solovay-Kitaev theorem (which introduces and additional polylogarithmic factor), this
proves that any 2-qubit gate

can be implemented by evolving the Lindbladian

(t) up to precision

U

L

where ρ0 is a two-qubit state, and the error bound follows directly from Lemma 15.

eR t

0 L

(s)ds

(
∥

T

)ρ0∥1 ≤

− U

˜O

κ
(U 2P )1/3

,

(cid:19)

(cid:18)

(S159)

|

,

|

i,j

(t)

Ωα

| ≤

i (t)

So far, we have shown how the bosonic Hamiltonian can be used to generate high-ﬁdelity universal gates. Speciﬁcally,
we have seen that 2-qubit gates can be implemented in time t = ˜O((P U 2)−
1/3), where U is the non-Gaussian strength,
and P refers to the maximum absolute value allowed for the Gaussian terms of the Hamiltonian. Let us now consider
a system with nL bosonic modes as described in section I E and study the asymptotic scaling with n. In this case,
J α,α′
P . Let us assume that J, Ω = Θ(P ) (this is the case, for example, for geometrically local
|
Hamiltonians). Then, provided that the Gaussian couplings J, Ω = O(1) can be arbitrarily large constants, it follows
from Lemma 17 that any gate can be implemented to an arbitrarily small (but independent of n) precision. Since
this allows for the implementation of gates with an eﬀective gate error below that of the threshold theorem [S8–S10],
this implies that fault-tolerant circuits can be implemented. We remark that, in addition to high-ﬁdelity gates, fault-
tolerant constructions usually require the ability to implement RESTART operations to provide fresh qubits [S9]. For
spin systems in the presence of non-unital noise, cooling algorithms [S17–S19] in conjunction with the noise channel
can be leveraged to implement such an operation [S20–S22]. In our case, a similar scheme would be needed; however,
we leave a careful analysis of the construction for future work.

B. High-noise regime of the fermionic model is not separable at all times

For the bosonic model, Theorem 2 establishes that, in the presence of a suﬃciently incoherent high particle loss
or incoherent particle gain, the state of the bosonic model is separable at all times.
In this subsection, we show
that such a result cannot be true for the fermionic model. We show this for two notions of separability for fermions
[S23, S24]—the ﬁrst notion holds for all observables, and the second weaker notion holds for parity-conserving, or
even, observables.

}

1,2...m

v}v

v, c2
c1
{

Throughout this section, it will be enough for us to consider separability in the bi-partite setting. We will consider
and B with modes
m fermionic modes which are divided into two subgroups of modes, A with modes
. Recall that an operator on the fermionic Hilbert space is an element of the algebra generated
mA +1, mA +2, . . . , m
{
. An operator acting on sub-system A will be an element
av, a†v}v
by
{
∈{
of the algebra generated by
av, a†v}v
and, similarly, an operator acting on the sub-system B will be an
1,2...mA}
{
∈{
of
. The parity operator of a set S
element of the algebra generated by
av, a†v}v
{
fermionic modes is PA = exp(iπ
S a†i ai). Operators that conserve the parity operator are called even operators.
Physically relevant states of the fermionic modes are restricted to be even operators—note, however, that a physical
operator that is even on all the fermionic modes is not necessarily even on a subset of these fermionic modes.

1, 2, . . . , mA}

mA+1,mA+2...mB }

or alternatively by

1, 2 . . . m
}

1,2...m

⊆ {

P

∈{

∈{

{

∈

}

}

i

Deﬁnition 1. A state ρ of m fermionic modes will be called a product state with respect to all observables on
the bi-partition A
B if there exist states ρA for the modes in A and ρB for the modes in B such that, for all operators
OA supported on A and OB supported on B,

|

Tr(OAOBρ) = Tr(OAρA)Tr(OBρB).

A state ρ of the m fermionic modes will be called a separable state with respect to all observables on the
bi-partition A
|

B if it can be expressed as a convex-combination of such product states.

We remark that it was shown in Ref. [S24] that if ρ is an even operator, which is also a product state as per deﬁnition
1, then ρA and ρB are also both even operators.

Deﬁnition 2. A state ρ of m fermionic modes will be called a product state with respect to even observables
on the bi-partition A
B if there exist states ρA for the modes in A and ρB forthe modes in B such that, for all even
|
operators O(+)

A supported on A and O(+)

B supported on B,

32

Tr(O(+)

A O(+)

B ρ) = Tr(O(+)

A ρA)Tr(O(+)

B ρB).

A state ρ of the m fermionic modes will be called a separable state with respect to even observables on the
bi-partition A
|

B if it can be expressed as a convex-combination of such product states.

As discussed in Ref. [S23] , while separability with respect to all observables implies separability with respect to even
observables, the converse is not necessarily true. This can be seen explicitly in a simple 2-mode example—consider
/√2. This state is not separable as per deﬁnition 1—to see this, one can use the 2-mode
the state
separability criteria from Refs. [S23, S24] , which we also provide in Lemma 18. However, this state is separable as
per deﬁnition 2—to see this, we note that, for any even observable O(+)
on the
second fermionic mode,

on the ﬁrst fermionic mode and O(+)

= (a†1 + a†2)

vac

ψ

⟩

⟩

1

2

|

|

O(+)

1 O(+)

2

ψ

|

⟨

=

ψ

|

⟩

1
2

O(+)
1

ϕ1|

⟨

ϕ1⟩ ⟨

ϕ2|

|

O(+)
2

ϕ2⟩

|

+

θ1|

⟨

O(+)
1

θ1⟩ ⟨

θ2|

|

O(+)
2

θ2⟩

|

,

(S160)

where

ϕ1⟩

|

= a†1 |

vac

,

ϕ2⟩

|

⟩

=

vac

,

⟩

θ1⟩

|

|

(cid:0)
=

vac

|

⟩

and

θ2⟩

|

= a†2 |

vac

.

⟩

(cid:1)

1. Non-separability for any observable

Here, we provide a simple 2-mode example which shows that, unlike the bosonic model, no matter how high the
rate of particle loss and incoherent particle gain is in the fermionic model, the dynamics of the fermionic model is
not separability preserving with respect to all observables (deﬁnition 1). To establish this result, we ﬁrst review the
2-mode seperability criteria from Refs. [S23, S24].

Lemma 18 (2-mode separability, Refs. [S23, S24]). A 2-mode density matrix ρ is separable with respect to all observ-
ables (deﬁnition 1) if and only if it is diagonal in the computational basis.

Proposition 1. Consider a system with m = 2 fermionic modes, with the sub-system A with mode 1 and sub-system
B with mode 2 whose density matrix ρ(t) satisﬁes the Lindblad master equation

d
dt

ρ(t) =

−

i[J(a†1a2 + a†2a1), ρ(t)] +

4

j=1
X

(cid:0)

κ1Daj + κ2Da†

j

ρ(t),

(cid:1)

ρ(0) which is separable with respect to all observables (Deﬁnition 2) such that ρ(t) cannot be

∃
0.

Then,
separable for all t

κ1, κ2 > 0,

∀

≥

Proof. Throughout this proof, “separability” refers to separability with respect to all observables (Deﬁnition 1).
a1. Note that ρ(0) is trivially separable—we now establish that, for a
Consider the initial state ρ(0) = a†1 |
t(ρ(0)) is not seperable to O(t2) for any κ, which is enough to contradict separability of ρ(t) at
small time t, ρ(t) = eL
all times t. Now,

vac

vac

⟩⟨

|

ρ(t) = ρ(0) + t

ρ(0) + O(ε2),

L

(S161)

which, in the computational basis (i.e.

ρ(ε)

0, 1

1, 0
|

|⟨
⟩|
separable state σ(t) such that

|

vac
= a†2 |
), satisﬁes
|
= Jt + O(t2). From the separability criteria in Lemma 18, it then follows that there cannot exist a
O(t2), no matter what the rate κ is.

= a†1a†2 |

= a†1 |

1, 0
⟩

0, 0
⟩

0, 1
⟩

1, 1
⟩

σ(t)

vac

vac

vac

=

⟩

⟩

⟩

⟩

|

|

|

|

,

,

,

ρ(t)
∥

−

∥1 ≤

While the analysis above indicates that there would be times when the state ρ(t) would be entangled, we can also
analyze the time-scale at which this entanglement is developed. In Fig. S3, we simulate the two-fermionic-mode model
(i.e.,
from Proposition 1 for κ1 = κ2 = κ and numerically compute the entanglement measure E(ρ) =
the 1-norm of a vector formed with the oﬀ-diagonal elements of ρ) as a function of t. Note that from Lemma 18,
this measure quantiﬁed how non-separable the two-mode state is when considering all observables. We observe that
this measure becomes 0 at long times, however it is largest at time t∗
1/κ — thus consistent with the analysis of
Proposition 1, even at large κ, the fermionic state becomes entangled at short times and, unlike the bosonic model,
does not exhibit a threshold behavior of transitioning to an always separable state at suﬃciently large κ.

ρb,b′

b,b′:b

P

=b′

∼

|

|

̸
(a)

e
r
u
s
a
e
m

t
n
e
m
e
l
g
n
a
t
n
E

0.30

0.25

0.20

0.15

0.10

0.05

0.00

∑ = J
∑ = 2J
∑ = 5J
∑ = 10J

(b)

0.25

§

t
J

0.20

e
m

i
t

.
t
n
e

x
a
M

0.15

0.10

0.05

33

Simulation
Fit with ∑°1

0

1

2
3
Time Jt

4

5

2.5

5.0

10.0 12.5 15.0 17.5 20.0

7.5
Decay rate ∑/J

FIG. S3. Numerical simulation of the two-fermionic-mode model considered in Proposition 1 with both particle loss rate κ1 and
particle gain rate κ2 set to κ and ρ(0) = a†
1 |vac⟩⟨vac| a1. (a) Time evolution of the entanglement measure computed by adding
all oﬀ-diagonal elements of the two-mode density matrix of the model. As per Lemma 18, this quantiﬁes non-separability with
respect to all observables for 2-mode fermionic systems. (b) The time t∗ at which the entanglement measure computed in (a)
is maximum as a function of κ. We see that entanglement is developed at time-scales t∗ ∼ 1/κ no matter how large κ is.

2. Non-separability for even observables

We will use the following lemma, which reduces the problem of checking the non-separability of a 4-mode fermionic
state with respect to even observables to an eﬀective problem with 2 qubits.

Lemma 19. Suppose ρ is a state of m = 4 fermionic modes, with sub-system A with modes 1 and 2 and sub-system
B with modes 3 and 4, and suppose the 2-qubit state σ = (QA,eQB,o)ρ(Q†A,eQ†B,o), where
1A⟩⟨

0A⟩⟨
is entangled, then ρ is not separable with respect to even observables.

a1a2, QB,o =

0B⟩⟨

1B⟩⟨

QA,e =

a3 +

vac

vac

vac

vac

a4,

+

|

|

|

|

|

|

|

|

Proof. This lemma follows by contradiction—let us assume that ρ is separable with respect to even observables. Now,
for any two operators OA, OB ∈

2, consider the even observables

C2

×

O(+)

A = Q†A,eOAQA,e and O(+)

B = Q†B,oOBQB,o.

(S162)

Note that O(+)

A acts on the fermionic modes in A and O(+)

B acts on the fermionic modes in B. We note also that

Tr(O(+)

A O(+)

B ρ) = Tr(OAOBσ).

(S163)

Now, since ρ is separable with respect to even observables by assumption, it follows that
measure µ such that

∃

ρA,x, ρB,x and a probability

Tr(O(+)

A O(+)

B ρ) =

Tr(O(+)

A ρA,x)Tr(O(+)

B ρB,x)dµ(x),

and consequently, using Eq. (S162), we ﬁnd that

Z

Tr(OAOBσ) =

Tr(OAσA,x)Tr(OBσB,x)dµ(x),

Z

(S164)

(S165)

where σA,x = QA,eρA,xQ†A,e and σB,x = QB,oρB,xQ†B,o. This would imply that σ is separable and therefore, by
contradiction, we conclude that ρ cannot be separable even with respect to even observables.

Proposition 2. Consider a system with m = 4 fermionic modes, with the sub-system A with modes 1 and 2 and
sub-system B with modes 3 and 4, whose density matrix ρ(t) satisﬁes the Lindblad master equation

d
dt

ρ(t) =

−

i[J(a2a3 + a†3a†2), ρ(t)] +

κ1Daj + κ2Da†

j

ρ(t).

4

j=1
X

(cid:0)
ρ(0) which is separable with respect to even observables (Deﬁnition 2) such that ρ(t) cannot be
∃
0.

(cid:1)

Then,
separable for all t

κ1, κ2 > 0,

∀

≥

Proof. Throughout this proof, “separability” refers to separability with respect to even observables (Deﬁnition 2). We
choose ρ(0) =

, where

ψ(0)

ψ(0)

|

⟩⟨

|

ψ(0)

=

⟩

|

1
√2

vac

a†1 |

+ a†4 |

⟩

vac

⟩

.

(S166)

34

It can be noted that ρ(0) is separable with respect to even observables since, for any even observables O(+)
O(+)

A on A and

B on B,

(cid:0)

(cid:1)

Tr(ρ(0)O(+)

A O(+)

B ) =

1
2 ⟨

ψ(1)
A |

O(+)
A |

ψ(1)

A ⟩ ⟨

ψ(1)
B |

O(+)
B |

ψ(1)
B ⟩

+

1
2 ⟨

ψ(2)
A |

O(+)
A |

ψ(2)

A ⟩ ⟨

ψ(2)
B |

O(+)
B |

ψ(2)
B ⟩

,

(S167)

ψ(1)
A ⟩

ψ(2)
ψ(1)
where
B ⟩
A ⟩
for all t > 0, it is enough to show that there isn’t a separable state σ(t) such that
To show this, we consider a ﬁrst-order expansion of ρ(t):

ψ(2)
B ⟩

= a†4 |

= a†1 |

, and

vac

vac

vac

vac

=

=

⟩

⟩

⟩

⟩

|

|

|

,

,

|

|

|

. Again, to show that ρ(t) is not separable
0.

O(t2) as t

σ(t)

ρ(t)

∥

−

∥1 ≤

→

ρ(t) = ρ(0) + t

L

ρ(0) + O(t2)

4

+ t

ψ(t)

=

|

⟩⟨

ψ(t)

|

κ1Daj (

|

ψ(0)

⟩⟨

ψ(0)

) + κ2Da†

j

|

(

|

ψ(0)

⟩⟨

ψ(0)

)

|

+ O(t2),

(S168)

|

⟩

ψ(t)

= (a†1 + a†4 −

(cid:1)
/√2. We can now compute the state σ(t) =
where
vac
(QA,eQB,o)ρ(t)(Q†B,oQ†A,e) deﬁned in Lemma 19, which eﬀectively amounts to projecting ρ(t) on the sub-
space spanned by
, a†3a†2a†1 |
0A, 1B⟩

and identifying a†3 |

vac
⟩
, a†4a†2a†1 |

a†3 |
{
vac
⟩ → |

, a†3a†2a†1 |
vac

0A, 0B⟩

ita†3a†2a†4)

, a†4 |

⟩ → |

⟩ →

vac

vac

vac

vac

⟩}

⟩

|

|

j=1
X
(cid:0)
ita†3a†2a†1 −

σ = ((1

−

0A, 1B⟩ −

|

(κ1 + κ2)t)

0A, 1B|

⟨

+ it

1A, 0B|

⟨

) + O(t2),

(S169)

−

, a†4a†2a†1 |
⟩
:
1A, 1B⟩
⟩ → |
)((1
it

1A, 0B⟩

|

, a†4 |
vac
⟩
1A, 0B⟩
(κ1 + κ2)t)

κ1, κ2 > 0, σ(t) (as a 2-qubit state), does not admit an O(t2) separable approximation for
It is easy to see that
suﬃciently small t. Consequently, from Lemma 19, we ﬁnd that ρ(t) (as a 4-mode fermionic state) does not admit an
O(t2) separable approximation, thus proving the lemma.

∀

To analyze the timescales at which the state ρ(t) becomes non-separable relative to even observables, in Fig. S4, we nu-
merically simulate the four-fermionic-mode model from Proposition 2 with κ1 = κ2 = κ and compute ρ(t). To quantify
the extent to which ρ(t) is non-separable, we ﬁrst construct the eﬀective two-qubit state σ(t) = QA,eQB,oρ(t)Q†B,oQ†A,e
from ρ(t) deﬁned in Lemma 19 and then compute the minimum eigenvalue of its partial transpose. The negative of
this minimum eigenvalue is the entanglement measure shown in in Fig. S4(a). We ﬁnd that, while at long times σ
has a non-negative partial transpose and is thus separable, at short times σ is entangled irrespective of how large κ
is. Furthermore, the minimum eigenvalue of the partial transpose of σ is attained at t∗
1/κ [Fig. S4(b)], which sets
the time-scale at which non-separability with respect to even observables in this system is developed.

∼

[S1] C. V. Kraus, A quantum information perspective of fermionic quantum many-body systems, Ph.D. thesis, Technische

Universit¨at M¨unchen (2009).

[S2] J. Surace and L. Tagliacozzo, SciPost Phys. Lect. Notes , 54 (2022).
[S3] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to algorithms (MIT press, 2022).
[S4] M. Fagotti and P. Calabrese, J. Stat. Mech.-Theory E. 2010, P04016 (2010).
[S5] B. M. Terhal and D. P. DiVincenzo, Phys. Rev. A 65, 032325 (2002).
[S6] E. Knill, arXiv preprint quant-ph/0108033 (2001).
[S7] T. Kuwahara, T. V. Vu, and K. Saito, Nat. Commun. 15, 2520 (2024).
[S8] K. Noh and C. Chamberland, Phys. Rev. A 101, 012316 (2020).
[S9] D. Aharonov and M. Ben-Or, SIAM J. Comput. 38, 1207 (2008).

[S10] T. Matsuura, N. C. Menicucci, and H. Yamasaki, arXiv preprint arXiv:2410.12365 (2024).
[S11] A. Mari and J. Eisert, Phys. Rev. Lett. 109, 230503 (2012).
[S12] R. Hudson, Rep. Math. Phys 6, 249 (1974).
[S13] M. Walschaers, PRX Quantum 2, 030204 (2021).
[S14] M. Yuan, A. Seif, A. Lingenfelter, D. I. Schuster, A. A. Clerk, and L. Jiang, arXiv preprint arXiv:2312.15783 (2023).

(a)

e
r
u
s
a
e
m

t
n
e
m
e
l
g
n
a
t
n
E

0.5

0.4

0.3

0.2

0.1

0.0

°0.1

°0.2

∑ = 0.1J
∑ = 0.2J
∑ = 0.4J
∑ = 0.8J
∑ = 1.6J

(b)

§

t
J

e
m

i
t

.
t
n
e

x
a
M

0.5

0.4

0.3

0.2

0.1

35

Simulation
Fit with ∑°1

0

2

4
6
Time Jt

8

10

0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00
Decay rate ∑/J

FIG. S4. Numerical simulation of the four-mode fermionic model considered in Proposition 2 with both particle loss rate κ1
and particle gain rate κ2 set to κ and |ψ(0)⟩ = (a†
4) |vac⟩. (a) Time evolution of the entanglement measure computed by
ﬁrst computing the two-qubit state σ(t) corresponding to the 4-mode fermionic state ρ(t) from Lemma 19 and then computing
(the negative) of the minimum eigenvalue of its partial transpose. As per Lemma 19, this quantiﬁes non-separability with
respect to all observables for 2-mode fermionic systems. (b) The time t∗ at which the entanglement measure computed in (a)
is maximum as a function of κ — we see that entanglement is developed at time-scales t∗ ∼ 1/κ no matter how large κ is.

1 + a†

[S15] A. Eickbusch, V. Sivak, A. Z. Ding, S. S. Elder, S. R. Jha, J. Venkatraman, B. Royer, S. M. Girvin, R. J. Schoelkopf,

and M. H. Devoret, Nat. Phys. 18, 1464 (2022).

[S16] A. Lingenfelter, D. Roberts, and A. A. Clerk, Sci. Adv. 7, eabj1916 (2021).
[S17] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and R. Vrijen, Proceedings of the National Academy of Sciences 99,

3388 (2002).

[S18] L. J. Schulman and U. V. Vazirani, in Proceedings of the Thirty-First Annual ACM Symposium on Theory of Computing,

STOC ’99 (Association for Computing Machinery, New York, NY, USA, 1999) p. 322–329.

[S19] ´A. M. Alhambra, M. Lostaglio, and C. Perry, Quantum 3, 188 (2019).
[S20] M. Ben-Or, D. Gottesman, and A. Hassidim, arXiv preprint arXiv:1301.1995 (2013).
[S21] R. Trivedi and J. I. Cirac, Phys. Rev. Lett. 129, 260405 (2022).
[S22] O. Shtanko and K. Sharma, arXiv preprint arXiv:2411.04819 (2024).
[S23] M.-C. Ba˜nuls, J. I. Cirac, and M. M. Wolf, Phys. Rev. A 76, 022311 (2007).
[S24] H. Moriya, J. Phys. A-Math. Gen. 39, 3753 (2006).

