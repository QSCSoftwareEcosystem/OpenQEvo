Hybridized Methods for Quantum
Simulation in the Interaction Picture
Abhishek Rajput1, Alessandro Roggero2,3, and Nathan Wiebe1,4,5
1DepartmentofPhysics,UniversityofWashington,Seattle,WA98195,USA
2InQubatorforQuantumSimulation(IQuS),DepartmentofPhysics,UniversityofWashington,Seattle,WA98195,USA
3DipartimentodiFisica,UniversityofTrento,viaSommarive14,I–38123,Povo,Trento,Italy
4DepartmentofComputerScience,UniversityofToronto,Toronto,ONM5S2E4,Canada
5PacificNorthwestNationalLaboratory,Richland,WA99354,USA
Conventional methods of quantum simulation involve trade-offs that limit their ap-
plicability to specific contexts where their use is optimal. In particular, the interaction
picture simulation has been found to provide substantial asymptotic advantages for
some Hamiltonians but incurs prohibitive constant factors and is incompatible with
methods like qubitization. We provide a framework that allows different simulation
methods to be hybridized and thereby improve performance for interaction picture
simulations over known algorithms. These approaches show asymptotic improvements
over the individual methods that comprise them and further make interaction pic-
ture simulation methods practical in the near term. Physical applications of these
hybridized methods yield a gate complexity scaling as log2Λ in the electric cutoff Λ
fortheSchwingerModelandindependentoftheelectrondensityforcollectiveneutrino
oscillations,outperformingthescalingforallcurrentalgorithmswiththeseparameters.
For the general problem of Hamiltonian simulation subject to dynamical constraints,
these methods yield a query complexity independent of the penalty parameter λ used
to impose an energy cost on time-evolution into an unphysical subspace.
1 Introduction
SinceFeynman’sseminalworkonthesimulationofquantumdynamicswithquantumcomputers[1],
considerable research has been undertaken on the problem of quantum simulation as it is a major
areawherequantumcomputersareexpectedtooutperformclassicalsupercomputers[2,3,4,5,6].
Theproblemofsimulationisineffectacompilationproblem. Thetaskinsimulationistogenerate,
for a given Hermitian matrix H, evolution time t, and error tolerance (cid:15) a sequence of quantum
gatesU(t)suchthatkU(t)−e−iHtk≤(cid:15),foranappropriatenormk·k,andthecostofthesequence
of gate operations that comprise U(t) is minimal. This problem is distinct from ordinary unitary
synthesis problems because here we do not explicitly know the matrix elements of e−iHt and need
to construct this unitary only using information about the Hamiltonian H.
A variety of simulation methods have been developed to approximate the ideal time-evolution
channel. The first, and most space efficient, algorithms are the Trotter-Suzuki formulas and their
time-ordered generalizations [2, 7, 8, 9, 10], but recent years have seen several additions to the
repertoireofquantumsimulationtechniques. Themethodofqubitization[11,12,13,14,15,16,17]
involves the implementation of a walk operator whose eigenvalues are an efficiently computable
function of those of H and achieves linear scaling in the simulation time t, logarithmic scaling in
theinverseerrortolerance, andscalingindependentofthenumberoftermsintheHamiltonian. A
majordrawbackofqubitizationisthatthemethoddoesnotapplytotime-dependentHamiltonians.
Linearcombinationsofunitariesprovidessimulationmethods[18,19,20,21]thataddressthisshort
comingandallowsimulationswithintheinteractionpictureatcoststhatcanbeexponentiallylower
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 1
2202
guA
01
]hp-tnauq[
3v80330.9012:viXra

thanallotherknownmethods[21];however,theseapproachesrequirecomplicatedquantumcontrol
logic which can lead to undesirable constant factors [22].
The quantum stochastic drift protocol [23], or qDRIFT, is spiritually related to linear combi-
nation of unitaries but uses classically controlled evolutions rather than quantum controlled ones.
This approach drifts towards the correct unitary time-evolution with high precision and with a
gate complexity independent on the number of terms in the Hamiltonian. qDRIFT was later gen-
eralized to the continuous qDRIFT protocol for time-dependent Hamiltonians with an L1-norm
scaling in the gate complexity [24]. The principal disadvantages of this approach are that it has
a larger scaling in the simulation time t compared to other algorithms and does not exploit any
commutator structure between the terms of a Hamiltonian.
We develop hybrid algorithms in this paper that combine the various conventional approaches
forquantumsimulationaftermovingintotheinteractionpicture(I.P.). Thisissignificantbecause
while the interaction picture simulation method provides the best asymptotic scaling known for
many problems, the constant factors involved can make it impractical for many applications [22].
We address this by combining algorithms such as qDRIFT and qubitization at different stages
of the overall simulation procedure within the interaction picture. Since the interaction picture
transformation involves conjugation of Hamiltonian summands P
k6=j
H
k
via eitHj, the unitary
invariance of the L1-norm scaling from qDRIFT essentially eliminates the contribution of H to
j
the query complexity of the hybrid protocols. A direct application of these methods to physical
systems such as the Schwinger Model and collective neutrino oscillations yield improved scaling
over current algorithms with respect to certain parameters of interest. The general problem of
Hamiltonian simulation constrained to a physical subspace can likewise be efficiently simulated
using these algorithms, with a scaling independent of the penalty parameter used to impose an
energy cost on projections onto the unphysical subspace.
We summarize the scaling of the newly introduced hybrid schemes and compare them to stan-
dardapproachesinTable1. Theseareexpressedintermsoftheoraclecomplexityforapproximat-
ing the time-evolution under a Hamiltonian H =
PL
H . For the Trotter/qDRIFT based I.P.
i=1 i
methods, we show the asymptotic scaling in terms of queries to oracles {W }L implementing
k k=1
W
k
(t) = e−iHkt for any choice of summand H
k
. For the hybrid qubitization I.P. based methods,
the queries are instead to the SELECT/PREPARE oracles (see Section 2.2 for details) and the
oracle W
l
(t)=e−itHl. The latter is specifically used to implement the time evolution of the term
H toentertheinteractionpicture, whiletheoracles{W }L aboveareusedtoimplementallthe
l k k=1
time-evolutions. The constant λ and λ are obtained by first writing H as a linear combination of
α
P P P
unitaries H = ω U with real ω >0. Then we have λ= ω and λ = ω =λ−ω .
k k k l k k α k6=l k l
As anticipated above, the hybrid I.P. schemes introduced here can become advantageous when
λ (cid:28) λ or kH −H k (cid:28) kHk , that is, when the Hamiltonian term H has a large norm (here
α l ∞ ∞ l
and in the rest of the paper, kHk denotes the Schatten p-norm of a matrix. See Appendix B for
p
further details).
Section 2 contains a review of some standard methods of quantum simulation and of the inter-
action picture. More specifically, in Section 2.1 we summarize the continuous qDRIFT protocol
and the relevant theorems on its query complexity. Section 2.2 delves into qubitization and singu-
lar value transformations. Section 2.3 contains an overview of Trotterization and a generalization
of the first order Trotter-Suzuki formula to time-dependent Hamiltonians. Section 2.4 reviews
the interaction picture, the key component of our hybrid protocols. Section 3 and Section 4 con-
tain the main results on our hybrid protocols with Section 5, Section 6, and Section 7 presenting
applications of them to the Schwinger Model, collective neutrino oscillations, and constrained
Hamiltonian dynamics respectively. The reader can find additional background on the diamond
norminAppendixAandonsomeofthenormnotationusedthroughoutthepaperinAppendixB.
2 Standard Methods of Quantum Simulation
This section contains brief overviews of interaction picture of quantum mechanics and relevant
results from standard methods of quantum simulation such as continuous qDRIFT, qubitization,
and Trotterization. Those readers already familiar with these topics can skip to Section 3.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 2

Algorithm Number of oracle calls to W
k
or PREPARE/SELECT and W
l
(cid:16) (cid:17)
Trotter [10] O α˜1/pt1+1/p
(cid:15)1/p
(cid:18) h i2 (cid:19)
qDRIFT [23] O t2 PL kH k
(cid:15) k=1 k ∞
(cid:16) (cid:17)
Qubitization [11, 12] O λt+ log(1/(cid:15))
log(log(1/(cid:15)))
(cid:16) h (cid:13)h i(cid:13) i(cid:17)
Trotter + qDRIFT + I.P. [Cor. 3.3] O t2 PL kH k2 +(cid:13) H , PL H (cid:13)
(cid:15) k6=l k ∞ (cid:13) k q>k,q6=l q (cid:13)
qDRIFT + Qubitization + I.P. [Th. 4.2] O (cid:16) λ α t+ (cid:16) kH−H (cid:15) lk2 ∞ t2(cid:17) lo l g o l g o ( g k ( H kH − − H H lk l ∞ k∞ t/ t (cid:15) / ) (cid:15)) (cid:17) ∞
Table 1: Query complexities for standard qDRIFT, Trotter, qubitization, and the hybrid schemes from Corol-
lary 3.3 and Theorem 4.2 where H =
PL
H with L the number of summands in the Hamiltonian H, t
i=1 i
the simulation time, and (cid:15) the simulation error. In the Trotter formula, p is the order of the Trotter formula
and α˜ involves sums of commutators nested p times. The query complexity for qDRIFT and Trotter-based
algorithms are given in terms of upper bounds for queries to each of the W oracles that implement time-
k
evolutionunderasummandH . Thequerycomplexityforthequbitizationmethodsaregiveninqueriestothe
k
oracles W implementing time-evolution for the interaction picture transformation, SELECT, and PREPARE.
l
P
Forthelattermethods,H isdecomposedasalinearcombinationofunitariesH = ω U withrealω >0.
P k k k l
Then λ = ω and λ = λ−ω. The hybrid I.P. schemes can become advantageous when λ (cid:28) λ or
k k α l α
kH−Hk (cid:28)kHk .
l ∞ ∞
2.1 Continuous qDRIFT
In this subsection, we outline the continuous qDRIFT protocol used to simulate time-dependent
Hamiltonians with a scaling depending only on the L1-norm of the Hamiltonian. At its heart is
a classical sampling protocol which randomly samples a simulation time τ ∈ [0,t] according to a
probability distribution and evolves a given state under the time-independent Hamiltonian H(τ).
The probability distribution is chosen such that it is biased towards τ with large ||H(τ)|| . The
∞
result is a simulation protocol that stochastically drifts towards the ideal unitary time evolution
with small error in the diamond norm.
We present relevant results from [24] used throughout this paper without proof. Let H(τ) be
a time dependent Hamiltonian defined for 0 ≤ τ ≤ t. Unless otherwise specified, we make the
following assumptions of H(τ):
1. It is non-zero and continuously differentiable on [0,t]
2. It is finite dimensional, i.e. H :[0,t]→CM×M
3. There exists an oracle W: R2 7→ CM×M such that for any τ ∈ [0,t] and ∆ ∈ R, W(τ,∆) =
e−iH(τ)∆
ThespecificimplementationofW dependsonthesimulationprotocolinquestion. Forinstance,
a concrete realization involves “qubitization oracles” to be discussed later in the paper. For our
present purposes, it suffices to assume the existence of such an oracle and analyze the query
complexity of algorithms invoking it as a black box.
Rt
The ideal evolution of H(τ) for time t is given by E(t,0) = exp (−i dτH(τ)) and the
T 0
quantum channel corresponding to this is
(cid:18) Z t (cid:19) (cid:18) Z t (cid:19)
E(t,0)=E(t,0)ρE†(t,0)=exp −i dτH(τ) ρexp† −i dτH(τ) , (1)
T T
0 0
where the subscript T in exp denotes the time-ordered exponential. Generalizations of these
T
channelstonon-zeroinitialtimescanbeaccomplishedsimplybychangingthelimitsofintegration.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 3

Sinceitisdifficultinpracticetoimplementtheidealchannelduetothepresenceoftime-ordered
exponentials, we can instead approximate it by a mixed unitary channel defined by
Z t
|     |     |     |     |            |     |     | p(τ)e−iH | ( τ )  | ρeiH ( τ ) |     |
| --- | --- | --- | --- | ---------- | --- | --- | -------- | ------ | ---------- | --- |
|     |     |     |     | U(t,0)(ρ)= |     | dτ  |          | p( τ ) | p( τ ) ,   | (2) |
0
where
||H(τ)||
∞
p(τ):=
||H||
∞,1
| is a | probability | density | function | defined |     | for 0≤τ | ≤t  | and |     |     |
| ---- | ----------- | ------- | -------- | ------- | --- | ------- | --- | --- | --- | --- |
Z
t
|     |     |     |     |     | ||H|| | :=  | dτkHk |     | .   |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- |
|     |     |     |     |     |       | ∞,1 |       | ∞   |     |     |
0
(i.e. the outermost subscript indicates an L1 norm while the innermost subscript indicates a
Schatten infinity norm). This channel can be implemented via a classical sampling protocol and
| has | the following |           | features: |       |          |      |                |     |     |     |
| --- | ------------- | --------- | --------- | ----- | -------- | ---- | -------------- | --- | --- | --- |
| (a) | p(τ)          | is biased | towards   | those | τ ∈[0,t] | with | large ||H(τ)|| |     |     |     |
∞
(b) p(τ) decreases with the evolution time t since ||H(τ)|| involves an integral over [0,t]
∞,1
(c) Withatimeτ ∈[0,t]obtainedfromsamplingp(τ), wecanquerytheoracleW citedaboveby
i
inputting W(τ ,p(τ )−1) to obtain an implementation of the unitary time-evolution operator
|     |     |     | i i |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e−iH(τi)/p(τi)
This classical sampling protocol and the unitary channel (2) implemented by it is denoted
by “continuous qDRIFT”. We assume the spectral norm ||H|| or an upper bound is already
∞
known and that we can efficiently sample from p(τ). We then have the following theorem when
| the | simulation | time | t is assumed |     | to be sufficiently |     | small: |     |     |     |
| --- | ---------- | ---- | ------------ | --- | ------------------ | --- | ------ | --- | --- | --- |
(L1-norm
Theorem 2.1 error bound for continuous qDRIFT, short-time version). Let H(τ) be a
time-dependent Hamiltonian defined for 0≤τ ≤t and satisfying conditions 1 and 2 above. Define
| E(t,0) |     | U(t,0)(ρ) |     |                   |     |         |               |     |      |     |
| ------ | --- | --------- | --- | ----------------- | --- | ------- | ------------- | --- | ---- | --- |
|        | and |           | as  | in equations      | (1) | and (2) | respectively. |     | Then |     |
|        |     |           |     | ||E(t,0)−U(t,0)|| |     |         | ≤4||H||2      |     | .    | (3) |
|        |     |           |     |                   |     |         | (cid:5)       |     | ∞,1  |     |
(See Appendix A for information about the diamond norm for quantum channels). When the
simulation time t is large, we will need to divide the simulation interval [0,t] into sub-intervals
[t j ,t j+1 ] where 0=t 0 <t 1 <···<t r =t and apply the continuous qDRIFT protocol within each
to control the simulation error. In these cases, we have a “long-time” version of Theorem 2.1:
(L1-normerrorboundforcontinuousqDRIFTforlongsimulationtime)
| Theorem |     | 2.2. |     |     |     |     |     |     | LetH(τ) |     |
| ------- | --- | ---- | --- | --- | --- | --- | --- | --- | ------- | --- |
be a time-dependent Hamiltonian defined for 0 ≤ τ ≤ t and satisfying conditions 1 and 2 above.
Define E(t,0) and U(t,0)(ρ) as in (1) and (2) respectively. For any positive integer r, there exists
| a division |        | 0=t 0          | <t 1 <···<t | r =t             |         |              |               |           |       |     |
| ---------- | ------ | -------------- | ----------- | ---------------- | ------- | ------------ | ------------- | --------- | ----- | --- |
|            |        |                |             | (cid:13)         |         |              | (cid:13)      |           |       |     |
|            |        |                |             | (cid:13)         | r −1    |              | (cid:13)      |           | kHk 2 |     |
|            |        |                |             | (cid:13) E(t,0)− | Y       | U(t          | (cid:13)      |           | ∞,1   |     |
|            |        |                |             | (cid:13)         |         |              | ,t ) (cid:13) | ≤4        | .     | (4) |
|            |        |                |             | (cid:13)         |         | j+1          | j (cid:13)    |           | r     |     |
|            |        |                |             | (cid:13)         |         |              | (cid:13)      |           |       |     |
|            |        |                |             |                  | j=0     |              |               | (cid:5)   |       |     |
| To         | ensure | the simulation |             | error is         | at most | (cid:15), it | suffices      | to choose |       |     |
|            |        |                |             |                  |         | &            |               | ’         |       |     |
kHk2
|     |     |     |     |     | r   | ≥4  | ∞,1 | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:15)
ThevalueofrabovecanalsobeinterpretedasthequerycomplexityofthecontinuousqDRIFT
protocol, i.e. the number of queries to the oracle W needed to implemented channel (2) and
| satisfy | (4) | with error | less | than (cid:15). |     |     |     |     |     |     |
| ------- | --- | ---------- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
Foradditionalinformationonthediamondnormandnotationusedintheseresults, thereader
| may | consult | Appendix | A   | and Appendix |     | B.  |     |     |     |     |
| --- | ------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 4

| 2.2 Qubitization |     | and | Singular | Value | Transformations |     |     |     |
| ---------------- | --- | --- | -------- | ----- | --------------- | --- | --- | --- |
Having considered continuous qDRIFT, we now briefly review the basics of the qubitization simu-
lation protocol which we seek to combine with the former. We will also frame qubitization as an
example of the general notion of the block-encoding of non-unitary matrices within larger unitary
ones.
QubitizationisamethodofHamiltoniansimulationinvolvingthesynthesisofthetime-evolution
operator eiHt, where H is a time-independent Hamiltonian, via the implementation of a walk
W(H)
operator whose eigenvalues are an efficiently computable function of those of H. Assuming
thatwehavedecomposedH asalinearcombinationofunitarymatrices,thedesiredwalkoperator
can implemented with the so-called SELECT and PREPARE qubitization oracles. The spectrum
canthenbetransformedefficientlyusingtechniquesinvolvingsingularvaluetransformationswhich
transform the singular values of an operator by a polynomial function [11, 12].
Block-encoding refers to the embedding of a non-unitary matrix H into a larger unitary U,
typically as the upper-left block of U. Once a block-encoding is achieved, a quantum circuit
can be expressed in terms of U. This greatly broadens the applicability of quantum computers,
particularly in the domain of the simulation of unitary quantum dynamics. We largely follow the
| treatments | in [17,   | 25]. |     |      |     |     |     |     |
| ---------- | --------- | ---- | --- | ---- | --- | --- | --- | --- |
|            | ∈End(CN), |      |     | =2n, |     |     |     |     |
Let H where N be a Hermitian operator. Suppose there exists an (m+n)-
| qubit unitary | matrix | U   | ∈End(CMN), |     | where M =2m, | such | that |     |
| ------------- | ------ | --- | ---------- | --- | ------------ | ---- | ---- | --- |
H
|     |     |     |     |     | (cid:18) | (cid:19) |     |     |
| --- | --- | --- | --- | --- | -------- | -------- | --- | --- |
|     |     |     |     |     | H/α      | ·        |     |     |
|     |     |     |     |     | U =      | ,        |     |     |
H
|     |     |     |     |     | ·   | ·   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
where α>0 is a known normalization constant. We may then get access to H/α by
|     |     |     |     | H =(h0|m⊗I | )U  | (|0im⊗I | ).  |     |
| --- | --- | --- | --- | ---------- | --- | ------- | --- | --- |
|     |     |     |     |            | n H |         | n   |     |
To quantify how “close” the block encoded matrix is to the original one, we introduce the
following general definition. This definition can also be extended to the case of block-encodings
within superoperators, which we will need to consider for the proofs of some later theorems:
Definition 2.3 (Block Encoding). Suppose that A is an n-qubit operator, α,ε∈R , and m∈N.
+
We then say that the (m+n)-qubit unitary U H is a (α,m,ε)-block-encoding of A if
|           |       |         | kA−α(hS|⊗I |     | n )U H (|Si⊗I | n   | )k ∞ ≤ε. |     |
| --------- | ----- | ------- | ---------- | --- | ------------- | --- | -------- | --- |
| where |Si | is an | m-qubit | state.     |     |               |     |          |     |
Similarly, we say that a quantum channel Λ is a (α,m,ε)-block-encoding of A if
|     |     | maxkAρA†−α(hT|⊗I |     |     | )Λ(|TihT|⊗ρ)(|Ti⊗I |     | )k ≤(cid:15), |     |
| --- | --- | ---------------- | --- | --- | ------------------ | --- | ------------- | --- |
|     |     |                  |     |     | n                  |     | n ∞           |     |
ρ
where the maximization is over density matrices ρ and |Ti is an m-qubit state.
Here |Si or |Ti are referred to as the “signal state”. The previous example involving H is a
| (1,m,0)-encoding |     | where | |Si=|0im. |     |     |     |     |     |
| ---------------- | --- | ----- | --------- | --- | --- | --- | --- | --- |
Now suppose we are given a time-independent H. H can be decomposed into a linear combi-
| nation of | unitary | operators |     |     |     |     |     |     |
| --------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
L−1
X
|     |     |     | H   | =   | w H , w ∈R+, |     | H2 =I . | (5) |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | --- |
|     |     |     |     |     | l l l        | 0   | l       |     |
l=0
Here we assume that any complex phases are absorbed into U l . The two oracles used are a
| preparation | oracle | whose | action | on |0ilogL | is defined | as follows: |     |     |
| ----------- | ------ | ----- | ------ | ---------- | ---------- | ----------- | --- | --- |
L−1r
|     |     |     |                |     | X   | w   |           |     |
| --- | --- | --- | -------------- | --- | --- | --- | --------- | --- |
|     |     |     | PREPARE|0ilogL |     | =   |     | l|li=|Li, | (6) |
λ
l=0
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 5

where
X
|     |     |     |     |     |     | λ=  | w , |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l
l
and a selection oracle whose action on an ancilla register |li and system register |Ψi is as follows:
L−1
X
|     |     |     |     | SELECT= |     |     | |lihl|⊗H | ,   |     | (7) |
| --- | --- | --- | --- | ------- | --- | --- | -------- | --- | --- | --- |
l
l=0
|     |     |     |     | SELECT|li|Ψi7→|liH |     |     |     | |Ψi. |     | (8) |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | ---- | --- | --- |
l
Inotherwords,theSELECToracle“selects”aunitaryH conditionedonthestateoftheancilla
l
register |li. Using (7) and (8), it can be shown that SELECT squares to the identity operator and
can therefore be considered as a “reflection” operator. Note that we also have the following result
| for the | action of | SELECT | on                      | |Li: |     |     |     |       |     |     |
| ------- | --------- | ------ | ----------------------- | ---- | --- | --- | --- | ----- | --- | --- |
|         |           |        |                         |      |     |     | 1   | X H   |     |     |
|         |           |        | (hL|⊗I)(SELECT)(|Li⊗I)= |      |     |     |     | w H = | .   | (9) |
|         |           |        |                         |      |     |     | λ   | l l   | λ   |     |
l
Thepreviousequationisaconditionforqubitizationandoraclesthatsatisfythisconditionare
| referred | to as “qubitization |     | oracles” | [12]. | If  | we define |     |     |     |     |
| -------- | ------------------- | --- | -------- | ----- | --- | --------- | --- | --- | --- | --- |
=(PREPARE†⊗I)(SELECT)(PREPARE⊗I),
U
H
P
it follows from (9) that U is a (kwk ,logL,0)-block encoding of H, where kwk = |w |.
|     |     |     | H   |     | 1   |     |     |     | 1 l | l   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The desired walk operator, also known as the “iterate”, can now be defined as follows:
|     |     |     | W=R |          |     | R   | =(2|LihL|⊗I−I). |     |     |      |
| --- | --- | --- | --- | -------- | --- | --- | --------------- | --- | --- | ---- |
|     |     |     |     | ·SELECT, |     |     |                 |     |     | (10) |
|     |     |     |     | L        |     | L   |                 |     |     |      |
WisoftheformofaSzegedywalkoperatorsinceitisthecompositionoftworeflections. From
a lemma by C. Jordan on the common invariant subspaces of two reflections [26], it follows that
the Hilbert space of the system decomposes under the action of W into a direct sum of 1 and
wherethelatterisspannedby|Li|kiandanorthogonalstate
2-dimensionalirreduciblesubspaces,
|φ i. Here, |ki is an eigenstate of H with eigenvalue E and |φ i is the component of W|Li|ki
| k          |            |                                |      |      |        |           | k   | k   |            |     |
| ---------- | ---------- | ------------------------------ | ---- | ---- | ------ | --------- | --- | --- | ---------- | --- |
| orthogonal | to |Li|ki. | Using                          | (9), | this | can be | expressed | as  |     |            |     |
|            |            | (I−|LihL|⊗|kihk|)·SELECT|Li|ki |      |      |        |           |     |     | EkI)|Li|ki |     |
(SELECT−
|     | |φ i= |                                    |     |     |     |     |     | =   | λ . | (11) |
| --- | ----- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     | k     | ||(I−|LihL|⊗|kihk|)·SELECT|Li|ki|| |     |     |     |     |     | q   |     |      |
1−(Ek)2
λ
Inthe2-dimensionalsubspaces,Wactsasarotationwhereasonthe1-dimensionalsubspaces,it
ThematrixelementsofWwithinatwo-dimensionalsubspacecanbecomputed
has±1eigenvalues.
| using the | above | relations. | Using | (9), | the top-left | entry | is  |     |     |     |
| --------- | ----- | ---------- | ----- | ---- | ------------ | ----- | --- | --- | --- | --- |
E
|     |     |     |     |     | hk|hL|W|Li|ki= |     | k   | ,   |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
λ
| and the | upper-right | entry | using | (11) | is  |     |     |     |     |     |
| ------- | ----------- | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- |
s
|     |     |     |     |     |     |     | (cid:18) | (cid:19)2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | --- |
E
|     |     |     |     | hk|hL|W|φ |     | i=  | 1−  | k . |     |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
k
λ
The other elements can be computed in an analogous way and we obtain for the form of the
| 2-dimensional | blocks | of  | W   |     |     |          |                   |     |     |      |
| ------------- | ------ | --- | --- | --- | --- | -------- | ----------------- | --- | --- | ---- |
|               |        |     |    |     | s   |          |                  |     |     |      |
|               |        |     |     |     |     | (cid:18) | (cid:19)2         |     |     |      |
|               |        |     |     | E   |     | E        |                   |     |     |      |
|               |        |     |    | k   |     | 1−       | k                |     |     |      |
|               |        |     |    | λ   |     |          | λ                |     |     |      |
|               |        |     |     |     |     |          | =eiarccos(Ek/λ)Y |     | .   | (12) |
 s
|     |     |     |    | (cid:18) | (cid:19)2 |     |    |     |     |     |
| --- | --- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- |
|     |     |     | −  | Ek       |           | Ek  |    |     |     |     |
1−
|     |     |     |     | λ   |     | λ   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 6

The controlled walk operator can be implemented using the circuit in Figure 1 [25]. It is
W
clear from this that requires one query to SELECT and at most two queries to PREPARE to
implement. The controlled-SELECT operation can be approximated as requiring the same gate
| complexity | to implement |     | as the | SELECT | operation. |        |     |     |     |
| ---------- | ------------ | --- | ------ | ------ | ---------- | ------ | --- | --- | --- |
|            |              |     | •      |        |            | •      | •   |     |     |
|            |              | |αi | /      | =      | |αi        | /      |     | =   |     |
|            |              |     | W      |        |            | SELECT | R   |     |     |
L
|     |     | |ψi   | /   |     | |ψi      | /   |         |     |     |
| --- | --- | ----- | --- | --- | -------- | --- | ------- | --- | --- |
|     |     |       |     | •   |          | Z   |         |     |     |
|     |     | |αi / |     |     | PREPARE† |     | PREPARE |     |     |
SELECT
|     |        | |ψi /              |     |          |          |        |            |         |         |
| --- | ------ | ------------------ | --- | -------- | -------- | ------ | ---------- | ------- | ------- |
|     | Figure | 1: Controlled-walk |     | operator | in terms | of the | SELECT and | PREPARE | oracles |
NotethatiftheconditionthatH2
=I in(5)doesnothold,wenolongerhavetheinterpretation
l
of SELECT acting like a reflection operator. It then follows that W cannot be interpreted as a
Szegedy walk operator and we can no longer apply Jordan’s lemma to it. However, we can still
W
define as in (10) and the subsequent computations involving the calculation of matrix elements
ofWwhenrestrictedtothetwo-dimensionalsubspacespannedbytheorthogonalstates|Li|kiand
|φ k i remain unaffected. It can still be shown that the Hilbert space decomposes as a direct sum of
such 2 dimensional irreducible subspaces as W does not take vectors within the subspace outside
of it.
Thearccosin(12)canbeefficientlyinvertedtorecovertheoriginalspectrumofH viatechniques
involving singular value transformations and quantum signal processing. The impetus for the
development of the general formalism of singular value transformations was the Quantum Signal
Processing techniques introduced by Low et al. [27]. They considered the following problem: if
| one applies | a gate | sequence | of the                               | form |     |     |     |     |     |
| ----------- | ------ | -------- | ------------------------------------ | ---- | --- | --- | --- | --- | --- |
|             |        |          | eiφ0σzeiθσxeiφ1σzeiθσx···eiθσxeiφkσz |      |     |     | ,   |     |     |
eiθσx
for unknown θ, where is the “signal unitary” and where we have control over the angles
φ ,··· ,φ , what unitary operators can be constructed in this manner? This problem lies at the
| 0        | k        |        |              |     |     |     |     |     |     |
| -------- | -------- | ------ | ------------ | --- | --- | --- | --- | --- | --- |
| heart of | “Quantum | Signal | Processing”. |     |     |     |     |     |     |
The answer to this problem is given in Theorem 3 of [13] and involves polynomial transfor-
mations of the entries of the signal unitary. This idea behind Quantum Signal Processing can
be generalized to situations where we apply an arbitrary unitary U between phase operators. It
can be shown that this induces polynomial transformations to the singular values of a particular
block of the unitary U. In the application to qubitization we are concerned with, Quantum Signal
Processing can be applied to the two-dimensional invariant subspaces of the walk operator W.
As we saw in Section 2.2, qubitization exploits a lemma by C. Jordan’s on the invariant sub-
spaces of two reflection operations and the decomposition of the entire vector space into a direct
sum of those subspaces. One of the reflections in the lemma can be replaced by a phase gate
in the context of quantum search algorithms [27]. In [13], the other reflection is replaced by an
arbitrary unitary U and the invariant subspaces in question are those arising from the singular
valuedecompositionofablockoftheunitarymatrix. Forourpurposes,weonlyneedthefollowing
results.
|     |     |     |     |     | H   |     |     |     | U,Π,Π˜ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Definition 2.4 (Theorem 17 of [13]). Let be a finite-dimensional Hilbert space and ∈
U
End(H ) be linear operators on H such that U is unitary and Π,Π˜ are orthogonal projectors.
| U   |     |     |     | U   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Φ∈Rn.
| Let | Then | we define   | the | phased                                 | alternating | sequence | U Φ as | follows |          |
| --- | ---- | ----------- | --- | -------------------------------------- | ----------- | -------- | ------ | ------- | -------- |
|     |      | (           |     | Q(n−1)/2(eiφ2j(2Π−I)U†eiφ2j+1(2Π˜−I)U) |             |          |        |         |          |
|     |      | eiφ1(2Π−I)U |     |                                        |             |          |        | if      | n is odd |
|     | U := |             |     | j=1                                    |             |          |        |         | .        |
Φ Qn/2(eiφ2j−1(2Π−I)U†eiφ2j(2Π˜−I)U)
if n is even
j=1
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 7

Figure 2 shows the circuit implementation of the alternating phase modulation sequence for
even n.
U eiφn(2Π˜−I) U† eiφn−1(2Π−I) ··· U eiφ2(2Π˜−I) U† eiφ1(2Π−I)
|     |     | Figure 2: Circuit | for U when | n is even |
| --- | --- | ----------------- | ---------- | --------- |
Φ
LetH
Theorem 2.5 (QuantumSingularValueTransformation: Theorem17of[13]). U beafinite-
U,Π,Π˜
dimensional Hilbert space and let ∈ End(H ) be linear operators on H such that U is
U U
unitary, and Π,Π˜ are orthogonal projectors. Let P ∈C[x] and Φ∈Rn. Then
(
Π˜U
|     |     | P(SV)(Π˜UΠ)= | Φ Π | if n is odd |
| --- | --- | ------------ | --- | ----------- |
,
|     |     |     | ΠU Φ Π | if n is even |
| --- | --- | --- | ------ | ------------ |
where P(SV) is a polynomial of degree at most n that performs a singular value transformation on
| the operator | to which it | is applied. |     |     |
| ------------ | ----------- | ----------- | --- | --- |
The polynomials in the above theorem are required to satisfy the conditions listed in Corollary
8 of [13]:
| (a) P has             | parity n mod        | 2             |     |     |
| --------------------- | ------------------- | ------------- | --- | --- |
| (b) ∀x∈[−1,1]:        | |P(x)|≤1            |               |     |     |
| (c) ∀x∈(−∞,−1]∪[1,∞): |                     | |P(x)|≥1      |     |     |
| (d) If n              | is even, then ∀x∈R: | P(ix)P∗(ix)≥1 |     |     |
Qubitizationworksbyinvertingthearccosine. Whilethisboilsdowntotheproblemofapplying
acosinetransformationtotheinputinprinciple,inpracticeaFourier-Chebyshevexpansionisused
via the Jacobi-Anger expansion that requires both the odd and even terms to closely approximate
the desired function and guarantee that the function is within [−1,1] for the entire domain to use
the bounds provided in the work. This process is described in detail in [27] as well as in Section 5
of [13].
Applying the preceding theorems to U =CTRL(W) and Π=Π˜ =|0iLh0|L⊗I, where L is the
numberofqubitsintheregister|αiinFigure1, willenableustoinvertthearccosinthespectrum
of the walk-operator. A circuit for the unitary operator ei2φj(2Π−I) is given in Figure 3.
Note that we are merely concerned with the existence of a transformation of the spectrum of
the walk-operator by a polynomial via the preceding theorem rather than the finding of the phase
factors needed to effect a given polynomial transformation. Constructive algorithms for finding
| these phase | factors are | outlined in [16, 17, | 28, 29]. |     |
| ----------- | ----------- | -------------------- | -------- | --- |
Theoverallquerycomplexityforqubitizationandthesingularvaluetransformationisgivenby
| the following | result as | expressed in the language | of block | encodings. |
| ------------- | --------- | ------------------------- | -------- | ---------- |

|0i⊗L 

|     |     |     | .       | .   |
| --- | --- | --- | ------- | --- |
|     |     |     | .       | .   |
|     |     |     | .       | .   |
|     |     | |0i | R (2φ ) |     |
Z i
Figure 3: Circuit for fractional reflection gadget, ei2φj(2Π−I), used in quantum singular value transformations.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 8

Theorem 2.6 (Corollary 60 of [13]). Let (cid:15) ∈ (0,1), t ∈ R and α ∈ R+. Let U be an (α,a,0)-
2
block encoding of the unknown Hamiltonian H. In order to implement an (cid:15)-precise Hamiltonian
simulation unitary V which is an (1,a+2,(cid:15))-block encoding of eitH, it is necessary and sufficient
| to use U | a total number |     | of times |          |     |          |     |          |     |      |
| -------- | -------------- | --- | -------- | -------- | --- | -------- | --- | -------- | --- | ---- |
|          |                |     |          | (cid:18) |     | log(1/ε) |     | (cid:19) |     |      |
|          |                |     |          | Θ α|t|+  |     |          |     |          | .   | (13) |
log(e+log(1/ε)/(α|t|))
Letting α=λ in our notation and assuming that ε is small, we can simplify (13) as
|     |     |     |     |     | (cid:18) |     | (cid:19) |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- |
log(1/ε)
|     |     |     |     |     | Θ λt+ |     |     | .   |     | (14) |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ---- |
loglog(1/ε)
The linear term comes from the qubitization portion of the procedure while the logarithmic
term stems from the transformation of the singular values via the procedure outlined above. This
result can be equivalently interpreted as the query complexity for qubitization in terms of the
number of queries (modulo irrelevant constants) needed to the PREPARE and SELECT oracles,
=CTRL(W)
| since U |     | is  | related | to PREPARE |     | and SELECT |     | via Figure | 1.  |     |
| ------- | --- | --- | ------- | ---------- | --- | ---------- | --- | ---------- | --- | --- |
2.3 Trotterization
We briefly outline the basics of Trotterization, the oldest method of quantum simulation based on
productformulas, andpresenttherelevantresultsonTrotterizationerrorsusedinthispaper. Our
ultimategoalistosynthesizethismethodofsimulationwiththeinteractionpictureandcontinuous
qDRIFT, and compare it with a hybrid continuous qDRIFT and qubitization protocol. This will
| be followed | by an | application |     | of both | methods | to several | physical |     | models. |     |
| ----------- | ----- | ----------- | --- | ------- | ------- | ---------- | -------- | --- | ------- | --- |
PΓ
Let H = H i be a time-independent Hamiltonian expressed as a sum of Γ terms. The
|     | i=1 |     |     |     |     |           | PΓ  |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |     |     |     |     |     | istheneit |     | Hi. |     |     |
unitarytime-evolutionoperatorgeneratedbyH Thereareavarietyofproduct
i=1
formulasthatcanbeusedtodecomposethetime-evolutionoperatorintoaproductofexponentials
involving the individual terms H . The most basic is the first-order Lie-Trotter formula
i
S (t):=eitHΓ···eitH1
|        |                       |     |           |          | 1          |              |            | .           |          |     |
| ------ | --------------------- | --- | --------- | -------- | ---------- | ------------ | ---------- | ----------- | -------- | --- |
| Higher | order generalizations |     |           | are      | the Suzuki | formulas     | defined    | recursively | as       |     |
|        |                       |     | S (t):=ei | tH1···ei |            | tHΓ−1eitHΓei | tHΓ−1···ei |             | tH1 ,    |     |
|        |                       |     | 2         | 2        |            | 2            | 2          |             | 2        |     |
|        |                       | S   | (t):=S    |          | (u t)2S    | ((1−4u       |            | )t)S        | (u t)2 , |     |
|        |                       |     | 2k        | 2k−2     | k          | 2k−2         | k          | 2k−2        | k        |     |
where u =(4−4−(2k−1))−1. There is an extensive literature devoted to investigating the utility
k
and performance of various product-formulas for a variety of physical systems and applications [4,
5,10]. Whiletherearemultiplestrategiesforaddressingthetime-orderingoftheoperatorsforthe
time-ordered operator exponentials that emerge when simulating time-dependent Hamiltonians,
| we broadly | follow | the analysis |     | outlined | in  | [9]. |     |     |     |     |
| ---------- | ------ | ------------ | --- | -------- | --- | ---- | --- | --- | --- | --- |
P
Let H(t) = H (t) be a time-dependent Hamiltonian acting on N particles, where S ⊂
|     |     | S S |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{1,...,N}, and each term has bounded norm and acts on at most k particles with k a constant
independentofN. Thetime-evolutionoperatorE(t,0)governingtheevolutionofthesystemfrom
| time 0 | to t is determined |     | by the | Schrodinger |     | equation |     |     |     |     |
| ------ | ------------------ | --- | ------ | ----------- | --- | -------- | --- | --- | --- | --- |
d
E(t,0)=−iH(t)E(t,0),
dt
| which admits | a solution |     | in terms | of         | a time-ordered | exponential |        |          |     |     |
| ------------ | ---------- | --- | -------- | ---------- | -------------- | ----------- | ------ | -------- | --- | --- |
|              |            |     |          |            |                | (cid:26) Z  | t      | (cid:27) |     |     |
|              |            |     |          | E(t,0)=exp |                | T −i        | H(s)ds | .        |     |     |
0
ItturnsoutthattheTrotter-Suzukiformulasgivenabovecanbegeneralizedtotime-dependent
scenarios,eveninsituationswheretheHamiltonianexperiencesfluctuationsontime-scalesshorter
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 9

than the time step ∆t [9]. Suppose we wish to simulate the time-evolution of our system up to
time t +∆t = T from t = 0. The exact time-evolution operator can be broken up into shorter
|          | r   |          | 0   |     |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| segments | of  | the form |     |     |     |     |     |     |     |     |     |     |
r
Y
|     |     |     |     |     | E(T,0)= |     | E(t +∆t,t |     | ),  |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |         |     | i         | i   |     |     |     |     |
i=0
where
|     |     |     |     |     |     | (cid:18) | Z tj+∆t |     |     | (cid:19) |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --- | -------- | --- | --- |
X
|     |     |     | E(t | +∆t,t | )=exp | T   | −i  | ds  | H (s) | .   |     | (15) |
| --- | --- | --- | --- | ----- | ----- | --- | --- | --- | ----- | --- | --- | ---- |
|     |     |     |     | i     | i     |     |     |     | S     |     |     |      |
tj
S
In the case where the sum over S involves only two terms, H and H , the generalized Trotter-
|           |           |          |            |        |          |         |         |          | 1         | 2       |          |      |
| --------- | --------- | -------- | ---------- | ------ | -------- | ------- | ------- | -------- | --------- | ------- | -------- | ---- |
| Suzuki    | expansion | is       | of the     | form   |          |         |         |          |           |         |          |      |
|           |           |          |            |        | (cid:18) | Z tj+∆t |         | (cid:19) | (cid:18)  | Z tj+∆t | (cid:19) |      |
|           | ETS(t     | +∆t,t    |            | )=exp  | −i       |         | dsH (s) | exp      | −i        |         | dsH (s)  |      |
|           |           | j        | j          |        | T        |         | 1       |          | T         |         | 2        |      |
|           |           |          |            |        |          | tj      |         |          |           | tj      |          |      |
|           |           |          |            | =ETS(t |          | )ETS(t  |         |          |           |         |          |      |
|           |           |          |            |        | j +∆t,t  | j       | j +∆t,t | j        | ),        |         |          | (16) |
|           |           |          |            |        | 1        |         | 2       |          |           |         |          |      |
| and gives | rise      | to a     | simulation | error  | of       |         |         |          |           |         |          |      |
|           |           |          | kE(t       | +∆t,t  | )−ETS(t  |         | +∆t,t   | )k       | ≤c (∆t2), |         |          | (17) |
|           |           |          |            | j      | j        |         | j       | j ∞      | 12        |         |          |      |
| where     | c is      | given by |            |        |          |         |         |          |           |         |          |      |
12
|     |     | 1   | Z tj+∆t |     | Z v |     |     | 1   |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c 12 = dv duk[H 1 (u),H 2 (v)]k ∞ ≤ max(k[H 1 (u),H 2 (v)]k ∞ ) . (18)
|     |                 | (∆t)2 |         |     |     |     |     | 2   | u,v |     |     |     |
| --- | --------------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |                 |       | tj      |     | tj  |     |     |     |     |     |     |     |
| 2.4 | The Interaction |       | Picture |     |     |     |     |     |     |     |     |     |
The interaction picture or Dirac picture of quantum mechanics is one of the three representations
of operators and states in quantum mechanics [30]. It is intermediate to the Schrodinger and
Heisenberg pictures of quantum mechanics where the former is characterized by state vectors
that evolve in time but with operators constant in time, and vice versa for the latter. Within
the interaction picture however, both operators and states have time dependence but the latter
evolves according to the interaction Hamiltonian consisting of the left-over terms in the original
Hamiltonian. This picture is particularly useful with dealing with terms in a Hamiltonian that
can be treated as small perturbations to a main term such as in time-dependent perturbation
theory, where it is used in deriving transition rates via Fermi’s golden rule and the Dyson series
perturbative expansion of the time-evolution operator. It also finds widespread application in
| interacting | quantum |     | field | theories. | [31]. |     |     |     |     |     |     |     |
| ----------- | ------- | --- | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
We follow the derivation in [30]. Consider a time-independent Hamiltonian H = P H . Sup-
i i
| pose the | energy | eigenvalues |     | and | eigenstates | of H | j for some | j   | are known. |     |     |     |
| -------- | ------ | ----------- | --- | --- | ----------- | ---- | ---------- | --- | ---------- | --- | --- | --- |
At t=t 0 , let the state of the physical system be given by |αi. At a later time t, we denote the
| state in | the | Schrodinger | picture |     | by |α,t | ;ti . Now | define |     |     |     |     |     |
| -------- | --- | ----------- | ------- | --- | ------- | --------- | ------ | --- | --- | --- | --- | --- |
0 S
|     |     |     |     |     | |α,t | ;ti :=eiHjt|α,t |     | ;ti | ,   |     |     | (19) |
| --- | --- | --- | --- | --- | ---- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | 0    | I               |     | 0 S |     |     |     |      |
(cid:126)
where we have implicitly set = 1 and where the subscript I indicates the same situation as
| represented |      | in the so-called   |     | “interaction |                 | picture” | (I.P.). |     |     |     |     |      |
| ----------- | ---- | ------------------ | --- | ------------ | --------------- | -------- | ------- | --- | --- | --- | --- | ---- |
| We          | also | define observables |     | in           | the interaction |          | picture | as  |     |     |     |      |
|             |      |                    |     |              | (t):=eiHjtA     |          | e−iHjt  |     |     |     |     |      |
|             |      |                    |     |              | A I             |          | S       |     | .   |     |     | (20) |
The physical implication of this definition is that we pick any term in the Hamiltonian and
move into its “interaction frame” via conjugation by eiHjt. The major difference between this
definition and the analogous one in the Heisenberg picture is the appearance of H in the former
j
| as opposed | to  | the full | H in | the | latter. |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 10

| We  | now take | the    | time derivative |     | of equation |     | (19):   |     |     |     |     |     |
| --- | -------- | ------ | --------------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
|     |          | ∂      |                 | ∂   | (cid:0)     |     | (cid:1) |     |     |     |     |     |
|     |          | i |α,t | ;ti             | =i  | eiHjt|α,t   | ;ti |         |     |     |     |     |     |
|     |          |        | 0               | I   |             | 0   | S       |     |     |     |     |     |
|     |          | ∂t     |                 | ∂t  |             |     |         |     |     |     |     |     |
X
|     |     |     |     |     | eiHjt|α,t |       | +eiHjt(H |     |     |           |         |     |
| --- | --- | --- | --- | --- | --------- | ----- | -------- | --- | --- | --------- | ------- | --- |
|     |     |     |     | =−H | j         | 0 ;ti | S        |     | j + | H i )|α,t | 0 ;ti S |     |
i6=j
X
|     |     |     |     | =eiHjt |     | H e−iHjteiHjt|α,t |     | ;ti | =H  | (t)|α,t | ;ti , | (21) |
| --- | --- | --- | --- | ------ | --- | ----------------- | --- | --- | --- | ------- | ----- | ---- |
|     |     |     |     |        |     | i                 |     | 0   | S   | I       | 0 I   |      |
i6=j
where we used the Schrodinger equation in the second equality. Thus we have
∂
i(cid:126)
|     |     |     |     |     | |α,t | 0 ;ti I | =H I (t)|α,t | 0   | ;ti I , |     |     | (22) |
| --- | --- | --- | --- | --- | ---- | ------- | ------------ | --- | ------- | --- | --- | ---- |
∂t
with
|     |     |     |     |             |     | (cid:18) | (cid:19) |     |      |     |     |      |
| --- | --- | --- | --- | ----------- | --- | -------- | -------- | --- | ---- | --- | --- | ---- |
|     |     |     |     |             |     | X        |          |     | X    |     |     |      |
|     |     |     |     | H (t)=eiHjt |     |          | H e−iHjt | =   | HI,  |     |     | (23) |
|     |     |     |     | I           |     |          | i        |     |      | i   |     |      |
|     |     |     |     |             |     | i6=j     |          |     | i6=j |     |     |      |
where
|     |     |     |     |     | HI  | =eiHjtH | e−iHjt | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     | i   |         | i      |     |     |     |     |     |
This is a Schrodinger-like equation for the time-evolution of the interaction picture state but with
| the Hamiltonian |     | H replaced |     | by H | I . |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
It is important to note the distinction between how observables in the interaction picture are
represented in (20) versus the interaction Hamiltonian above. Naively, we would expect the full
Hamiltonian to be what is conjugated within the big parentheses in (23) by analogy with (20).
This“discrepancy”merelyarisesfromthefactthatweneededtodefineH I asabovetoobtainthe
| Schrodinger-like |     | equation | (22). |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We can apply the interaction picture to the continuous qDRIFT protocol outlined before and
| obtain | the following |     | simple | lemma. |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 2.7. (L1-norm error bound for IP continuous qDRIFT for long simulation time) Let
H (τ) be an interaction picture Hamiltonian as in (23). Suppose it is defined for 0 ≤ τ ≤ t and
I
|     |     |     |     |     |     |     | E(t,0) |     | U(t,0) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- |
satisfies conditions 1 and 2 in Section 2.1. Define and as in (1) and (2) respectively
but with H (τ). Then for any positive integer r, there exists a division 0=t <t <···<t =t
|     | I   |     |     |     |     |     |     |     |     |     | 0 1 | r   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
such that
|     |     |     | (cid:13)         |     |      |     | (cid:13)        |     |      |     |     |      |
| --- | --- | --- | ---------------- | --- | ---- | --- | --------------- | --- | ---- | --- | --- | ---- |
|     |     |     | (cid:13)         |     | r −1 |     | (cid:13)        | k   | P H  | k2  |     |      |
|     |     |     | (cid:13)         |     | Y    |     | (cid:13)        |     | i6=j | i ∞ |     |      |
|     |     |     | (cid:13) E(t,0)− |     | U(t  | ,t  | ) (cid:13) ≤4t2 |     |      |     | .   | (24) |
|     |     |     | (cid:13)         |     |      | j+1 | j (cid:13)      |     | r    |     |     |      |
|     |     |     | (cid:13)         |     | j=0  |     | (cid:13)        |     |      |     |     |      |
(cid:5)
| To ensure | the | simulation | error | is  | at most | (cid:15), it | therefore | suffices | to  | choose |     |     |
| --------- | --- | ---------- | ----- | --- | ------- | ------------ | --------- | -------- | --- | ------ | --- | --- |
|           |     |            |       |     |         | &            |           | ’        |     |        |     |     |
|           |     |            |       |     |         | t2k          | P H       | k2       |     |        |     |     |
i ∞
|     |     |     |     |     | r ≥4 |     | i6=j |     | .   |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
(cid:15)
Proof. Wecansubstitute(23)directlyintoequation(4)andtheexpressionforr. Notehoweverthe
spectral norm of an operator (and the Schatten norms more generally) is invariant under unitary
| transformations |     | of that | operator. |       | We then | obtain | the  | simplification |           |     |     |     |
| --------------- | --- | ------- | --------- | ----- | ------- | ------ | ---- | -------------- | --------- | --- | --- | --- |
|                 |     |         |           |       | Z       |        |      | (cid:13)       | (cid:13)  |     |     |     |
|                 |     |         |           |       |         | t      |      | (cid:13)X      | (cid:13)  |     |     |     |
|                 |     |         | ||H       | ||    | =       | dτkH   | (τ)k | =(cid:13)      | H         | t,  |     |     |
|                 |     |         |           | I ∞,1 |         |        | I ∞  |                | i(cid:13) |     |     |     |
|                 |     |         |           |       |         |        |      | (cid:13)       | (cid:13)  |     |     |     |
|                 |     |         |           |       | 0       |        |      |                | i6=j      | ∞   |     |     |
so that
P
|     |     |     | (cid:13) |           |     | (cid:13)       | (k  |      | H k )2t2 |     |     |      |
| --- | --- | --- | -------- | --------- | --- | -------------- | --- | ---- | -------- | --- | --- | ---- |
|     |     |     | (cid:13) | E (t,0)−U |     | (cid:13)       |     | i6=j | i ∞      |     |     |      |
|     |     |     | (cid:13) | I         | I   | (t,0) (cid:13) | ≤4  |      |          | ,   |     | (25) |
|     |     |     | (cid:13) |           |     | (cid:13)       |     |      | r        |     |     |      |
(cid:5)
and
|     |     |     |     |     |      | & P |        |      | ’   |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------ | ---- | --- | --- | --- | --- |
|     |     |     |     |     |      | (k  | H k    | )2t2 |     |     |     |     |
|     |     |     |     |     |      |     | i6=j i | ∞    |     |     |     |     |
|     |     |     |     |     | r ≥4 |     |        |      | ,   |     |     |     |
(cid:15)
| to ensure | our | simulation | error | is  | less than | some | desired | (cid:15). |     |     |     |     |
| --------- | --- | ---------- | ----- | --- | --------- | ---- | ------- | --------- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 11

As before, r can also be interpreted as the number of queries to the oracle W defined in
Section 2.1. Each resulting time-independent piece will need to be simulated using techniques like
Trotterization or Qubitization and the main goal of the paper is to quantify the overall query and
gate complexity of “hybrid” protocols combining these with the IP continuous qDRIFT technique
outlined here.
Comparing this result to Theorem 2.2, we see that moving into the interaction frame of a fixed
termH oftheoverallHamiltonianeffectively“eliminates”itscontributiontotheerror. Moreover,
j
duetothepropertiesofthespectralnormandtheinteractionHamiltonian,L1-normdependenceof
theresultsinTheorem2.2reducetothosereminiscentofthetime-independentcase. Thisbehavior
recurs in subsequent results and is particularly useful when dealing with terms with unbounded
behavior or large ∞-norm, such as the electric term in the Schwinger Model considered later in
the paper.
| 3   | Hybrid | Trotterization |     | and | qDRIFT | Protocol |     |     |     |     |
| --- | ------ | -------------- | --- | --- | ------ | -------- | --- | --- | --- | --- |
We now present an analysis of our first hybrid simulation protocol where a generalization of the
time-dependent Trotter-Suzuki formula given in (16) proved below is combined with continuous
| qDRIFT. | Let H(t)= |     | PL H | (t). | The procedure | is as | follows: |     |     |     |
| ------- | --------- | --- | ---- | ---- | ------------- | ----- | -------- | --- | --- | --- |
k
k=1
1. Use Trotterization technique below to approximate the time-ordered exponential of H(t) as
|     | a product | of L | time-ordered | exponentials. |     |     |     |     |     |     |
| --- | --------- | ---- | ------------ | ------------- | --- | --- | --- | --- | --- | --- |
2. Use continuous qDRIFT to approximate each time-ordered exponential by the channel (2).
Implementing this channel involves sampling from a probability distribution and yields a
productofrtime-independent termsoftheformexp(−iH I (τ k )/p(τ k )),whereristhenumber
|     | of sub-intervals |     | of the whole | simulation |     | interval. |     |     |     |     |
| --- | ---------------- | --- | ------------ | ---------- | --- | --------- | --- | --- | --- | --- |
Before proving the error bounds for these processes, we first show the following simple lemma
| with | time arguments |     | suppressed | for | notational | convenience: |     |     |     |     |
| ---- | -------------- | --- | ---------- | --- | ---------- | ------------ | --- | --- | --- | --- |
Lemma 3.1. Let ETS denote the superoperator representing the Trotter-Suzuki decomposition of
E
the time-ordered exponential in (16) and let be as in (1). If D 2n is the set of density operators
| in the | domain | of E, then |     |      |               |     |           |     |     |      |
| ------ | ------ | ---------- | --- | ---- | ------------- | --- | --------- | --- | --- | ---- |
|        |        | kE−ETSk    |     |      | kE(ρ)−ETS(ρ)k |     | ≤2kE−ETSk |     |     |      |
|        |        |            |     | ∞ := | sup           |     | ∞         | ∞ . |     | (26) |
ρ∈D2n
| Proof. | From the | triangle | inequality |               | we have | that  |                     |     |     |     |
| ------ | -------- | -------- | ---------- | ------------- | ------- | ----- | ------------------- | --- | --- | --- |
|        | kE−ETSk  |          |            | kEρE†−ETSρE†k |         |       | kETSρE†−ETSρ(ETS)†k |     |     |     |
|        |          |          | ≤ sup      |               |         | +     | sup                 |     |     |     |
|        |          | ∞        |            |               |         | ∞     |                     |     | ∞   |     |
|        |          |          | ρ∈D2n      |               |         |       | ρ∈D2n               |     |     |     |
|        |          |          |            | k(Eρ−ETSρ)E†k |         |       | kETS(ρE†−ρ(ETS)†)k  |     |     |     |
|        |          |          | = sup      |               |         | ∞ +   | sup                 |     | ∞   |     |
|        |          |          | ρ∈D2n      |               |         |       | ρ∈D2n               |     |     |     |
|        |          |          | = sup      | k(E−ETS)ρk    |         | + sup | k(E−ETS)ρk          |     |     |     |
|        |          |          |            |               |         | ∞     | ∞                   |     |     |     |
|        |          |          | ρ∈D2n      |               |         | ρ∈D2n |                     |     |     |     |
|        |          |          | ≤2kE−ETSk  |               | .       |       |                     |     |     |     |
∞
In the third line, we used the unitary invariance of the infinity norm and that kAk =kA†k
|     |     |     |     |     |     |     |     |     | ∞   | ∞   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for any bounded square operator A. The latter follows from √ the fact that the Schatten infinity
norm is the spectral norm, which is the largest eigenvalue of AA† and coincides with the largest
eigenvalue of A†A. In the fourth line, we used the sub-multiplicativity of the infinity norm and
| the fact | that kρk | ≤1  | for all | density | operators. |     |     |     |     |     |
| -------- | -------- | --- | ------- | ------- | ---------- | --- | --- | --- | --- | --- |
∞
We now have the following results for quantum simulation with this hybrid protocol:
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 12

Theorem 3.2 (Hybrid Trotterization and qDRIFT Simulation). Let {H (t) : k = 1,...,L} be
k
a set of time-dependent Hermitian operators satisfying conditions 1 and 2 in Section 2.1. Let
U denote the superoperator representing the continuous qDRIFT channel for the time-dependent
k
summand H (t) as in (2). Then given a decomposition of [0,t] into r sub-intervals of length
k
∆t=t/r,
(cid:13) (cid:13) (cid:13) (cid:13) E(t,0)− Y r Y L U k (t j +∆t,t j ) (cid:13) (cid:13) (cid:13) (cid:13) ≤ L2c r maxt2+4r X L kH k k2 ∞,1 . (27)
j=1k=1 ∞ k=1
Herec isdefinedasc = 1 max PLk[H (u), PL H (v)]k andthe1-norminkH k2
max max L2 u,v p p q>p q ∞ k ∞,1
denotes an integral over an interval of size ∆t.
Proof. We first generalize (16) to the case where H(t) is the sum of L time-dependent terms.
SupposewebreakupH(t)asH(t)=H (t)+
PL
H (t). Treatingthesumasour“second”term
1 k>1 k
and considering a specific time-step [t ,t +∆t], we can substitute these into the expression for c
l l 12
above. Our proof of the error bound from recursively applying the bound in (16) is inductive. Let
us consider the base case. Using (18) we have that
(cid:13) (cid:13) Z tj+∆t X L !
(cid:13)exp −i H (t)+ H (t)dt
(cid:13) T 1 k
(cid:13) tj k=2
Z tj+∆t ! Z tj+∆t X L !(cid:13) (cid:13)
−exp −i H (t)dt exp −i H (t)dt (cid:13)
T 1 T k (cid:13)
tj tj k=2 (cid:13) ∞
1 (cid:13) (cid:13) " X L #(cid:13) (cid:13)
≤ max(cid:13) H (u), H (v) (cid:13) ∆t2 (28)
2 u,v (cid:13) (cid:13) 1 q (cid:13) (cid:13)
q>1 ∞
Next assume that for some p≥1 we have that
(cid:13) (cid:13) Z tj+∆t X L !
(cid:13)exp −i H (t)+ H (t)dt
(cid:13) T 1 k
(cid:13) tj k=2
Y p Z tj+∆t !  Z tj+∆t X L (cid:13) (cid:13)
− exp
T
−i H
q
(t)dt exp T−i H
k
(t)dt (cid:13)
(cid:13)
q=1 tj tj k=p+1 (cid:13) ∞
(cid:13) (cid:13)
p (cid:13) L (cid:13)
≤ 1 2 X m u a ,v x (cid:13) (cid:13) (cid:13) H ‘ (u), X H q (v) (cid:13) (cid:13) (cid:13) ∆t2 . (29)
‘=1 (cid:13) q>‘ (cid:13)
∞
We then have from the triangle inequality and the unitary invariance of Schatten norms that for
p+1
(cid:13) (cid:13) Z tj+∆t X L !
(cid:13)exp −i H (t)+ H (t)dt
(cid:13) T 1 k
(cid:13) tj k=2
p Y +1 Z tj+∆t !  Z tj+∆t X L (cid:13) (cid:13)
− exp
T
−i H
q
(t)dt exp T−i H
k
(t)dt (cid:13)
(cid:13)
q=1 tj tj k=p+2 (cid:13) ∞
≤ 1 2 X ‘= p 1 m u a ,v x (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13)  H ‘ (u), X q> L ‘ H q (v)   (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) ∆t2+ (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) exp T  −i Z tj tj+∆t k= X L p+1 H k (t)dt  
Z tj+∆t !  Z tj+∆t X L (cid:13) (cid:13)
−exp
T
−i H
p+1
(t)dt exp T−i H
k
(t)dt (cid:13)
(cid:13)
tj tj k=p+2 (cid:13) ∞
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 13

≤ 1 2 X ‘= p 1 m u a ,v x (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13)  H ‘ (u), X q> L ‘ H q (v)   (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) ∞ ∆t2+ 2 1 m u a ,v x (cid:13) (cid:13) (cid:13) (cid:13) (cid:13) " H p+1 (u), q> X L p+1 H q (v) #(cid:13) (cid:13) (cid:13) (cid:13) (cid:13) ∞ ∆t2
(cid:13) (cid:13)
p+1 (cid:13) L (cid:13)
= 2 1X m u a ,v x (cid:13) (cid:13) (cid:13) H ‘ (u), X H q (v) (cid:13) (cid:13) (cid:13) ∆t2 . (30)
‘=1 (cid:13) q>‘ (cid:13)
∞
This demonstrates the induction step and combined with the base case in (28) shows the error
bound we need inductively.
Since this analysis was for the time interval [t +∆t,t ] and since there are r such intervals
j j
sub-dividingoursimulationinterval,wecanmultiplyourpreviousresultbyr usingBox4.1in[32].
Since ∆t=t/r, we then have
L2c
kE(t,0)−ETS(t,0)k ≤ maxt2 . (31)
∞ 2r
Now note that from (3) that if we denote the time evolution under H to be given by the unitary
k
superoperator E (t +∆t,t ), then
k j j
kE (t +∆t,t )−U (t +∆t,t )k ≤kE (t +∆t,t )−U (t +∆t,t )k ≤4kH k2 . (32)
k j j k j j ∞ k j j k j j (cid:5) k ∞,1
Using the sub-multiplicativity and triangle inequality for the induced infinity norm for superoper-
ators, we get
(cid:13) L L (cid:13) L
(cid:13) (cid:13) (cid:13) Y E k (t j +∆t,t j )− Y U k (t j +∆t,t j ) (cid:13) (cid:13) (cid:13) ≤4 X kH k k2 ∞,1 , (33)
k=1 k=1 ∞ k=1
where the 1-norm in the subscript on the RHS denotes an integral over an interval of size ∆t from
t to t +∆t. Note that this notation causes the duration of the integral over time to be implicitly
j j
rather than explicitly defined. Despite this drawback, we use this notation in places throughout
the manuscript for brevity.
AstraightforwardgeneralizationoftheargumentinBox4.1in[32]usingthesub-multiplicativity
and triangle inequality for the diamond norm, and the fact quantum channels have diamond norm
at most 1 yields
(cid:13) r L r L (cid:13) L
(cid:13) (cid:13) (cid:13) Y Y E k (t j +∆t,t j )− Y Y U k (t j +∆t,t j ) (cid:13) (cid:13) (cid:13) ≤4r X kH k k2 ∞,1 . (34)
j=1k=1 j=1k=1 ∞ k=1
From the above inequality, Lemma 2.7, and Lemma 3.1 we obtain that the bound of the induced
∞-norm of the difference between the super-operator and the hybridized channel is
(cid:13) r L (cid:13)
(cid:13) (cid:13) E(t,0)− Y Y U k (t j +∆t,t j ) (cid:13) (cid:13) ≤
(cid:13) (cid:13)
j=1k=1 ∞
(cid:13) r L (cid:13) (cid:13) r L r L (cid:13)
(cid:13) (cid:13) E(t,0)− Y Y E k (t j +∆t,t j ) (cid:13) (cid:13) + (cid:13) (cid:13) Y Y E k (t j +∆t,t j )− Y Y U k (t j +∆t,t j ) (cid:13) (cid:13)
(cid:13) (cid:13) (cid:13) (cid:13)
j=1k=1 ∞ j=1k=1 j=1k=1 ∞
≤ L2c maxt2+4r X L kH k2 . (35)
r k ∞,1
k=1
Note that since the 1-norm in kH k2 denotes an integral over a time-interval of size ∆t,
k ∞,1
this term scales with t2/r. If we implement each qDRIFT channel U with some error (cid:15), an easy
k
application of the triangle inequality will add an additional subdominant term of rL(cid:15) to (27).
It should also be noted that the result of Theorem 3.2 applies for both the case of time-
dependent as well as time-independent Hamiltonian evolution. This is relevant because it shows
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 14

that the lowest-order Trotter-Suzuki formula can be combined with qDRIFT profitably wherein
small terms in the Hamiltonian can be reallocated between the Trotter and the qDRIFT portions
oftheHamiltoniantoreducethesimulationcost. Thiscanbeseenasanextensionofthecoalescing
| strategy | of [33]. |     |     |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
If we compare this result with that given in Theorem 7’ of [24], we find that the error in the
latter approach using solely continuous qDRIFT scales with kH k2 , where the last 1 in the
k ∞,1,1
subscript denotes a sum over k, and we square after performing the integral and sum. While the
result in (27) adds a term which scales at worst quadratically in the number of terms L in the
Hamiltonian, we will find that for systems like those considered later in this paper, we can exploit
thecommutationrelationsbetweenthetermsintheHamiltoniantogiveboundsthatscalelinearly
with L.
Corollary 3.3 (Hybrid Trotterization and qDRIFT Simulation in Interaction Picture). Let H =
PL
H k be a time-independent Hamiltonian where each summand satisfies conditions 1 and 2 in
k=1
Section 2.1. Then given a decomposition of [0,t] into r sub-intervals of size ∆t, we can perform
the Hamiltonian simulation of H in the interaction frame of H as in (23) such that
l
|     |     | (cid:13)         |     | r       | L    |         | (cid:13) t     | 2(cid:18) | L   | (cid:19) |      |
| --- | --- | ---------------- | --- | ------- | ---- | ------- | -------------- | --------- | --- | -------- | ---- |
|     |     | (cid:13) E(t,0)− |     | Y Y     | U    |         | (cid:13)       |           | X   | k2       |      |
|     |     | (cid:13)         |     |         | k (t | j +∆t,t | j ) (cid:13) ≤ | c I +4    | kH  | k ,      | (36) |
|     |     | (cid:13)         |     |         |      |         | (cid:13)       | r         |     | ∞        |      |
|     |     |                  |     | j=1k6=l |      |         | ∞              |           |     |          |      |
k6=l
|     | PL  |     | PL  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
where c I = k[H p , H q ]k ∞ . To ensure the simulation error in the infinity-norm is less
|                |              | p6=l     | q>p |           |     |            |     |          |     |     |     |
| -------------- | ------------ | -------- | --- | --------- | --- | ---------- | --- | -------- | --- | --- | --- |
| than (cid:15), | it therefore | suffices |     | to choose |     |            |     |          |     |     |     |
|                |              |          |     |           |     | t2(cid:18) | L   | (cid:19) |     |     |     |
X
|     |     |     |     |     | r ≥ | c   | +4 kH | k2 . |     |     | (37) |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | ---- |
|     |     |     |     |     |     | I   | k     | ∞    |     |     |      |
(cid:15)
k6=l
Proof. When moving into the interaction frame of a particular term H in H as in (23), we have
l
[H I,H I]=H IH I −H IH I =eiHltH H e−iHlt−eiHltH H e−iHlt =[H ,H ]I .
|           | p        | q    | p q          | q   | p          |        | p q          |      | q p | p q |     |
| --------- | -------- | ---- | ------------ | --- | ---------- | ------ | ------------ | ---- | --- | --- | --- |
| Since the | infinity | norm | is unitarily |     | invariant, |        | we then have | that |     |     |     |
|           |          |      |              |     | k[H        | ,H ]Ik | =k[H ,H      | ]k   | .   |     |     |
|           |          |      |              |     | p          | q      | ∞ p          | q ∞  |     |     |     |
Asthetime-dependencecameonlyfromtheeiHlt
|     |     |     |     |     |     |     | terms, | wecandropthemaximizationovertimes |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------------------------- | --- | --- | --- |
in c . The sums in c will be over those indices p,q 6=l and we define this simplified quantity
| max |     |     | max |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as c as above.
I
The 1-norm in kH k2 denotes an integral over an interval of measure ∆t, so it again follows
k ∞,1
|     |     |     |     |     |     |     |     | k2  | =(∆t)2kH | k2  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
from the unitary invariance of the infinity-norm that kH . Substituting ∆t=
|          |      |             |     |         |             |     |     | k ∞,1 |     | k ∞ |     |
| -------- | ---- | ----------- | --- | ------- | ----------- | --- | --- | ----- | --- | --- | --- |
| t/r into | (27) | then yields | the | desired | expression. |     |     |       |     |     |     |
We can frame the complexity of the preceding process in terms of oracles defined as follows:
|     |     |     |     | P   |     |     |     | HamiltonianinCM×M. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
Definition 3.4. LetH = H k beatime-independent Wedefineoracles
k
{W }L such that for each k, W :R7→CM×M with the action W (∆)=e−iHk∆.
| k k=1 |     |     |     |     | k   |     |     |     | k   |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
These oracles can be used to implement the interaction frame transformation and the time
evolutionunderspecificsummandsofH atvariousfixedtimes. Equation(37)thengivesanupper
bound on the number of queries to the oracles W needed to ensure the simulation protocol is
k
| within   | error (cid:15). |            |     |        |     |     |              |     |          |     |     |
| -------- | --------------- | ---------- | --- | ------ | --- | --- | ------------ | --- | -------- | --- | --- |
| 4 Hybrid |                 | Continuous |     | qDRIFT |     | and | Qubitization |     | Protocol |     |     |
We would also like to consider the scenario where we simulate a time-independent Hamiltonian H
| with the | following | procedure: |     |     |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 15

1. Move into the interaction frame of a term H in H to turn the simulation problem into one
j
| involving |     | a time-dependent |     | interaction |     | Hamiltonian |     | H (τ) | as in | (23). |     |     |
| --------- | --- | ---------------- | --- | ----------- | --- | ----------- | --- | ----- | ----- | ----- | --- | --- |
I
2. Use continuous qDRIFT to approximate the ideal time-evolution by the channel (2). Imple-
menting this channel involves sampling from a probability distribution and yields a product
of r time-independent terms of the form exp(−iH I (τ k )/p(τ k )), where r is the number of
| sub-intervals |     | of  | the whole | simulation |     | interval. |     |     |     |     |     |     |
| ------------- | --- | --- | --------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
3. Usequbitizationtosimulateeachtime-independenttermaboveandperformasingularvalue
transformation to transform the spectrum in (12) and recover the original spectrum of H.
| We  | first make | the | following | definition: |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition 4.1. Let H = P w H be a time-independent Hamiltonian in CM×M. We define an
|          |        |      |          | k k | k    |            |     |            |     |     |     |     |
| -------- | ------ | ---- | -------- | --- | ---- | ---------- | --- | ---------- | --- | --- | --- | --- |
|          |        |      | :R7→CM×M |     |      |            |     | (∆)=e−iHj∆ |     |     |     |     |
| oracle W | j such | that | W j      |     | with | the action | W   | j          |     |     |     |     |
We use this oracle to transform to the interaction frame of a particular summand H in the
j
| Hamiltonian |     | H in the | following | theorem: |     |     |     |     |     |     |     |     |
| ----------- | --- | -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
∈C2n×2n
Theorem 4.2 (HybridqDRIFTandQubitizationI.P.Simulation). LetH =H j +H α be
a time-independent Hamiltonian such that H has an LCU decomposition H = PL w H , where
|     |     |     |     |     |     | α   |     |     |     | α   | l6=j l | l   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
w ∈ R+, and each w and H are obtained by oracles PREPARE and SELECT in (6) and (7)
| l   |     |     | l   | l   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
respectively.
Thereexistsaquantumalgorithmsuchthatforany(cid:15),t>0,itimplementsaquantumchannelΛ
thatisa(1,O(logL),(cid:15))block-encodingofe−iHt usinganumberofqueriestoPREPARE,SELECT,
| and W | (t) in |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
|     |     |     |     | (cid:18) | (cid:18) | k2 t2(cid:19)      |        |                   | (cid:19)    |     |     |      |
| --- | --- | --- | --- | -------- | -------- | ------------------ | ------ | ----------------- | ----------- | --- | --- | ---- |
|     |     |     |     |          | kH       | α                  | log(kH | α k ∞ t/(cid:15)) |             |     |     |      |
|     |     |     | O   | λ t+     |          | ∞                  |        |                   |             | ,   |     | (38) |
|     |     |     |     | α        |          | (cid:15) loglog(kH |        | k                 | t/(cid:15)) |     |     |      |
α ∞
P
| where λ | α = | |w  | l |. |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l6=j
Proof. From Theorem 2.2, we have that for any positive integer r, there exists a division of [0,t]
|     |     |     |     |     |     |     |     |     |     | E(t,0) | U(t |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
where 0=t 0 <t 1 <···<t k <···<t r =t such that (4) holds, where and each k ,t k+1 )
| are understood |     | as involving |     | the interaction |     | Hamiltonian |     | H (τ) | of (23). |     |     |     |
| -------------- | --- | ------------ | --- | --------------- | --- | ----------- | --- | ----- | -------- | --- | --- | --- |
I
| By  | equation | (4) |     |                  |      |     |               |     |     |     |     |     |
| --- | -------- | --- | --- | ---------------- | ---- | --- | ------------- | --- | --- | --- | --- | --- |
|     |          |     |     | (cid:13)         |      |     | (cid:13)      |     |     |     |     |     |
|     |          |     |     | (cid:13)         | r −1 |     | (cid:13)      | kH  | k2  |     |     |     |
|     |          |     |     | (cid:13) E(t,0)− | Y    | U(t | (cid:13)      | I   | ∞,1 |     |     |     |
|     |          |     |     | (cid:13)         |      | ,t  | ) (cid:13) ≤4 |     | .   |     |     |     |
|     |          |     |     | (cid:13)         |      | j+1 | j (cid:13)    | r   |     |     |     |     |
|     |          |     |     | (cid:13)         | j=0  |     | (cid:13)      |     |     |     |     |     |
(cid:5)
From the relationship of the trace norm to the diamond norm in (105) and the monotonicity
kHIk2
of the Schatten p-norm, we get after choosing r ≥ 8 ∞,1 and defining D 2n to be the set of all
(cid:15)
| density | operators        | in            | C2n×2n     |       |               |                         |          |                    |     |         |               |     |
| ------- | ---------------- | ------------- | ---------- | ----- | ------------- | ----------------------- | -------- | ------------------ | --- | ------- | ------------- | --- |
|         | (cid:13)         |               |            |       | (cid:13)      | (cid:13)                |          |                   |     |        | (cid:13)      |     |
|         | (cid:13)         |               | r−1        |       | (cid:13)      | (cid:13)                |          |                    | r−1 |         | (cid:13)      |     |
|         | (cid:13)         |               | Y          |       | (cid:13)      | (cid:13)                |          |                    | Y   |         | (cid:13)      |     |
|         | (cid:13) E(t,0)− |               | U(t        | ,t    | ) (cid:13) := | max (cid:13) E(t,0)◦ρ− |          |                    | U(t | ,t )◦ρ | (cid:13)      |     |
|         | (cid:13)         |               |            | j+1 j | (cid:13)      | ρ∈D2n(cid:13)           |          |                    |     | j+1 j   | (cid:13)      |     |
|         | (cid:13)         |               | j=0        |       | (cid:13)      | (cid:13)                |          |                    | j=0 |         | (cid:13)      |     |
|         |                  |               |            |       | ∞             |                         |          |                    |     |         | ∞             |     |
|         |                  | (cid:13)      |            |      |               |                        | (cid:13) | (cid:13)           |     |         | (cid:13)      |     |
|         |                  | (cid:13)      |            |       | r−1           |                         | (cid:13) | (cid:13)           |     | r−1     | (cid:13)      |     |
|         |                  | (cid:13)      |            |       | Y             |                         | (cid:13) | (cid:13)           |     | Y       | (cid:13)      |     |
|         | ≤                | max (cid:13)  | E(t,0)◦ρ− |       | U(t           | ,t )◦ρ                 | (cid:13) | = (cid:13) E(t,0)− |     | U(t     | ,t ) (cid:13) |     |
|         |                  |               |            |       |               | j+1 j                   |          |                    |     | j+1     | j             |     |
|         |                  | ρ∈D2n(cid:13) |            |       |               |                         | (cid:13) | (cid:13)           |     |         | (cid:13)      |     |
|         |                  | (cid:13)      |            |       | j=0           |                         | (cid:13) | (cid:13)           |     | j=0     | (cid:13)      |     |
|         |                  |               |            |       |               |                         | 1        |                    |     |         | (cid:5)       |     |
k2
|     |     | kH I |       | (cid:15) |     |     |     |     |     |     |     |      |
| --- | --- | ---- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     | ≤4  |      | ∞,1 ≤ | .        |     |     |     |     |     |     |     | (39) |
|     |     | r    |       | 2        |     |     |     |     |     |     |     |      |
Next, let Q(t ,t ) denote a channel which implements the three-step procedure outlined in the
k+1 k
| beginning | of  | the section | and | let |     |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r−1
Y
|     |     |     |     |     | Λ=  | Q(t | ,t ), |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | j+1 j |     |     |     |     |     |
j=0
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 16

We claim Λ is the desired channel. To show this, note that from Definition 2.3, we have upon
fixing a signal state |Ti = |0im and setting α = 1 (which can be done since we’re implementing
qubitization) that
(cid:13)   (cid:13)
(cid:13) r−1 (cid:13)
ρ m ∈D a 2 x n kE(t,0)(ρ)−(h0|m⊗I n )(Λ(|0ih0|m⊗ρ))(|0im⊗I n )k ∞ ≤ ρ m ∈D a 2 x n (cid:13) (cid:13) (cid:13) (cid:13) E(t,0)(ρ)− j Y =0 U(t j+1 ,t j )(ρ) (cid:13) (cid:13) (cid:13) (cid:13)
∞
(cid:13)  (cid:13)
(cid:13) r−1 (cid:13)
+ max (cid:13) (cid:13) Y U(t j+1 ,t j )(ρ)−(h0|m⊗I n )(Λ(|0ih0|m⊗ρ))(|0im⊗I n ) (cid:13) (cid:13)
ρ∈D2n(cid:13)
(cid:13) j=0
(cid:13)
(cid:13)
∞
(cid:15)
≤ +rmax max kU(t ,t )(ρ)−(h0|m⊗I )(Q(t ,t )(|0ih0|m⊗ρ))(|0im⊗I )k . (40)
2 j ρ∈D2n j+1 j n j+1 j n ∞
Recall that sampling from U(t ,t ) yields a time-independent term exp(−iH (τ )/p(τ ))
k k+1 I k k
where τ ∈ [t ,t ] ⊂ [0,t] is a specific time in some sub-interval [t ,t ] at which H (τ) is
k k k+1 k k+1 I
being evaluated. The latter term above can thus be interpreted as the maximum spectral norm of
thedifferencebetweenanidealimplementationofthetime-evolutionoperatorfort∈[t ,t ]and
k k+1
an implementation involving qubitization, maximized over all sub-intervals. This can be made as
small as desired via singular value transformation techniques discussed previously. Choosing
(cid:15)
max max kU(t ,t )(ρ)−(h0|m⊗I )(Q(t ,t )(|0ih0|m⊗ρ))(|0im⊗I )k ≤ ,
j ρ∈D2n j+1 j n j+1 j n ∞ 2r
we then have
(cid:15) (cid:15)
max kE(t,0)(ρ)−(h0|m⊗I )(Λ(|0ih0|m⊗ρ))(|0im⊗I )k ≤ +r =(cid:15).
ρ∈D2n n n ∞ 2 2r
We now define
H˜ (τ)=H (τ)/p(τ),
i i
for i6=j. Using the following identity which holds for all invertible matrices U
UeAU† =exp(UAU†), (41)
we have
(cid:18) (cid:18) (cid:19) (cid:19)
exp(−iH (τ)/p(τ))=exp eiHjτ −i X H˜ e−iHjτ
I i
i6=j
(42)
(cid:18) (cid:18) (cid:19)(cid:19)
=eiHjτ exp X −iH˜ e−iHjτ .
i
i6=j
Eachexp(−iH (τ )/p(τ ))termobtainedfromsamplingU(t ,t )canbeexpandedasin(42).
I k k k+1 k
Using the unitary invariance of the spectral norm, we have the simplification
p(τ )= kH I (τ k )k ∞ = keiHjτk( P i6=j H i )e−iHjτkk ∞
k kH I (τ)k ∞,1 R t t k k+1dtkeiHjτk( P i6=j H i )e−iHjτkk ∞
P
= k i6=j H i k ∞ = 1 .
k P i6=j H i k ∞ R t t k k+1dt t k+1 −t k
Thus, we obtain a product of terms of the form
(cid:18) (cid:19)
X
exp(−iH
I
(τ
k
)(t
k+1
−t
k
))=eiHjτkexp −i(t
k+1
−t
k
) H
i
e−iHjτk .
i6=j
We then obtain the overall query complexity by summing (14) as applied to each sub-interval
[t ,t ] from 0 to r−1 with error in the QSP transformation at most δ:
k k+1
(cid:18)r−1(cid:18) (cid:19)(cid:19) (cid:18) (cid:19)
X log(1/δ) log(1/δ)
O λ (t −t )+ =O λ t+r . (43)
α k+1 k loglog(1/δ) α loglog(1/δ)
k=0
Letting δ =O((cid:15)/r) for our choice of r in the above completes the proof.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 17

Lastly, we consider a hybrid Trotter, qDRIFT, and qubitization I.P. protocol which extends
the results of Theorem 3.3 to include a qubitization step at the end to simulate all the resulting
time-independent exponentials. This procedure is largely similar to that outlined in the beginning
| of the | section | but with | an  | additional | Trotter | step: |     |     |     |     |     |     |
| ------ | ------- | -------- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
1. Move into the interaction frame of a term H in H to turn the simulation problem into one
j
| involving |     | a time-dependent |     |     | interaction | Hamiltonian |     | H (τ) as | in (23). |     |     |     |
| --------- | --- | ---------------- | --- | --- | ----------- | ----------- | --- | -------- | -------- | --- | --- | --- |
I
2. Use the Trotterization technique outlined in Section 2.3 to split the resulting time-ordered
exponential into a product of L time-ordered exponentials, one for each summand in the
Hamiltonian.
3. Use continuous qDRIFT to approximate each of the L time-ordered exponentials by the
channel (2). Implementing this channel involves sampling from a probability distribution
that yields a product of r time-independent terms of the form exp(−iH (τ )/p(τ )) for each
|     |       |              |     |               |     |     |     |     |     | I   | k   | k   |
| --- | ----- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of  | the L | time-ordered |     | exponentials. |     |     |     |     |     |     |     |     |
4. Use qubitization to simulate the rL time-independent pieces and perform a singular value
transformation to transform the spectrum in (12) and recover the original spectrum of H.
| This | yields | the following |     | theorem: |     |     |     |     |     |     |     |     |
| ---- | ------ | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorem 4.3 (Hybrid Trotter, qDRIFT, and Qubitization I.P. Simulation). Let the assumptions
of the previous theorem hold. There exists a quantum algorithm such that for any (cid:15),t > 0, it
implements a quantum channel Γ that is a (1,O(logL),(cid:15)) block-encoding of e−iHt using a number
| of queries | to  | PREPARE, | SELECT, |     | and | W (t) in |     |     |     |     |     |     |
| ---------- | --- | -------- | ------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
j
|     |     |     |     |     | (cid:18) |     |     | (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- |
log(rL/(cid:15))
|     |     |     |     |     | O λ | t+rL                  |     | ,   |     |     |     | (44) |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | α loglog(rL/(cid:15)) |     |     |     |     |     |      |
P
| where | λ = | |w   | | and | r is as | in (37). |     |     |     |     |     |     |     |
| ----- | --- | ---- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
|       | α   | l6=j | l     |         |          |     |     |     |     |     |     |     |
Proof. Let Γ denote a channel which implements the four-step procedure outlined above. Using
| the notation |     | from the | proof | of the | preceding | theorem, | we  | can express | Γ   | as  |     |     |
| ------------ | --- | -------- | ----- | ------ | --------- | -------- | --- | ----------- | --- | --- | --- | --- |
|              |     |          |       |        |           | r L      |     |             |     |     |     |     |
Y Y
|     |     |     |     |     | Γ=  | Q   | (t    | ,t ) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | k j+1 | j    |     |     |     |     |
j=1k=1
where the subscript k denotes the quantum channel performing steps 3-4 above for a specific
| Hamiltonian |     | term H | .   |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k
| Replicating |     | the arguments |     | of  | the preceding | theorem, |     | we can pick |     |     |     |     |
| ----------- | --- | ------------- | --- | --- | ------------- | -------- | --- | ----------- | --- | --- | --- | --- |
(cid:15)
maxmax max kU (t ,t )(ρ)−(h0|m⊗I )(Q (t ,t )(|0ih0|m⊗ρ))(|0im⊗I )k ≤ .
|     |         |     | k j+1 | j   |     | n k | j+1 | j   |     |     | n ∞ | 2rL |
| --- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| k   | j ρ∈D2n |     |       |     |     |     |     |     |     |     |     |     |
(45)
|     |     |     |     |     |     | (cid:18) |     |     | (cid:19) |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- | --- | --- | --- |
|     |     |     |     |     |     | 2t2      | PL  | k2  |          |     |     |     |
From Corollary 3.3, we can pick r ≥ c I +4 kH k . Then from the triangle in-
|           |                    |      |     |                        |     | (cid:15) |     | k6=l ∞ |     |     |     |     |
| --------- | ------------------ | ---- | --- | ---------------------- | --- | -------- | --- | ------ | --- | --- | --- | --- |
| equality, | we                 | have |     |                        |     |          |     |        |     |     |     |     |
|           | kE(t,0)(ρ)−(h0|m⊗I |      |     | )(Γ(|0ih0|m⊗ρ))(|0im⊗I |     |          |     |        |     |     |     |     |
| max       |                    |      |     |                        |     |          |     | )k     |     |     |     |     |
|           |                    |      |     | n                      |     |          |     | n ∞    |     |     |     |     |
ρ∈D2n
|               | (cid:13)    |     |    |        |     |  (cid:13) |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
|               | (cid:13)    |     |     | r L    |     | (cid:13)   |     |     |     |     |     |     |
|               | (cid:13)    |     |     | Y Y    |     | (cid:13)   |     |     |     |     |     |     |
| ≤ max         | E(t,0)(ρ)− |     |     |        | U(t | ,t )(ρ)   |     |     |     |     |     |     |
|               | (cid:13)    |     |     |        | j+1 | j (cid:13) |     |     |     |     |     |     |
| ρ∈D2n(cid:13) |             |     |     |        |     | (cid:13)   |     |     |     |     |     |     |
|               | (cid:13)    |     |     | j=1k=1 |     | (cid:13)   |     |     |     |     |     |     |
∞
|     | (cid:13) |     |     |    |     |     |     |     |     |     | (cid:13) |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
|     | (cid:13)  | r L |     |     |     |     |     |     |     |     | (cid:13) |     |
Y Y
+ max (cid:13) U(t ,t )(ρ)−(h0|m⊗I )(Γ(|0ih0|m⊗ρ))(|0im⊗I ) (cid:13)
|               | (cid:13) |        | j+1 | j   |     | n   |     |     |     | n   | (cid:13) |     |
| ------------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
| ρ∈D2n(cid:13) |           |        |     |     |     |     |     |     |     |     | (cid:13) |     |
|               | (cid:13)  | j=1k=1 |     |     |     |     |     |     |     |     | (cid:13) |     |
∞
(cid:15)
|          |           |            |       | kU(t | )(ρ)−(h0|m⊗I |     |         |        | )(|0ih0|m⊗ρ))(|0im⊗I |     |     |      |
| -------- | --------- | ---------- | ----- | ---- | ------------ | --- | ------- | ------ | -------------------- | --- | --- | ---- |
| ≤        | +rLmaxmax |            | max   |      | j+1 ,t j     |     | n )(Q(t | j+1 ,t | j                    |     |     | n )k |
| 2        |           | k j        | ρ∈D2n |      |              |     |         |        |                      |     |     | ∞    |
| (cid:15) |           | (cid:15)   |       |      |              |     |         |        |                      |     |     |      |
| ≤        | +rL       | =(cid:15). |       |      |              |     |         |        |                      |     |     | (46) |
| 2        | 2rL       |            |       |      |              |     |         |        |                      |     |     |      |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 18

Theoverallquerycomplexityisobtainedbysumming(14)asappliedtoeachoftheδ =t/rsized
sub-intervals and summing over the magnitude of the coefficients in the interaction Hamiltonian.
| We then | have, | after | choosing | δ = | (cid:15) | that |     |     |     |     |     |
| ------- | ----- | ----- | -------- | --- | -------- | ---- | --- | --- | --- | --- | --- |
2rL
|     |     | (cid:18) | L (cid:18) |       |             |     | (cid:19)(cid:19) | (cid:18) |                     | (cid:19) |      |
| --- | --- | -------- | ---------- | ----- | ----------- | --- | ---------------- | -------- | ------------------- | -------- | ---- |
|     |     |          | X          |       | log(1/δ)    |     |                  |          | log(rL/(cid:15))    |          |      |
|     |     | O r      |            | λ ∆t+ |             |     | =O               | λ t+rL   |                     | .        | (47) |
|     |     |          |            | i     | loglog(1/δ) |     |                  | α        | loglog(rL/(cid:15)) |          |      |
k=1
Note that the above methods can also be used to hybridize these simulation methods in the
time-independent case. Unlike the Trotter-methods, the scaling of the query complexity is not
substantially improved. Instead, any potential cost improvements to the simulation come from
| simplifications |     | to PREPARE |     | and | SELECT. |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Finally,wenotethatonecanchooseothercombinationsthananouterqDRIFTorTrotterloop
and an inner qubitization loop. The first step in each of these hybrid procedures is to exploit the
L1-norm invariance of continuous qDRIFT by begining with a time-independent Hamiltonian and
transformingintotheinteractionframeofaparticularsummand. Thisresultsinatime-dependent
Hamiltonian, which cannot be simulated via qubitization and constrains us to use either Trotter
or qDRIFT first. This still leaves open the possibility of whether trading an inner qDRIFT loop
for another Trotterization procedure that decomposes the time-ordered exponentials to ordinary
exponentials or randomly interleaving qDRIFT or Trotter procedures can result in additional
| speedups,     | and | we leave | such       | investigations |     | for        | future work. |       |     |     |     |
| ------------- | --- | -------- | ---------- | -------------- | --- | ---------- | ------------ | ----- | --- | --- | --- |
| 5 Hamiltonian |     |          | Simulation |                | of  | Schwinger  |              | Model |     |     |     |
| 5.1 Schwinger |     | Model    |            | and Query      |     | Complexity | Bounds       |       |     |     |     |
WeapplytheseideasinsimulatingtheSchwingerModel,quantumelectrodynamicsin1+1dimen-
sions on a lattice [34, 35]. This model has been extensively used as an important stepping stone
in simulations of lattice field theories using both tensor networks (see e.g. [36, 37]) and quantum
| devices | (see e.g. | [38, | 39, 40]). |     |     |     |     |     |     |     |     |
| ------- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Using the Hamiltonian formulation of lattice gauge theory in the U(1) compact case [41, 42],
the Hamiltonian of the model with N −1 links and N/2 spatial sites (half of which are electronic
| and half | are positronic), |     | is  | given | by  |      |       |     |     |     |      |
| -------- | ---------------- | --- | --- | ----- | --- | ---- | ----- | --- | --- | --- | ---- |
|          |                  |     |     |       |     | H =H | +H +H |     |     |     | (48) |
|          |                  |     |     |       |     | E    | h     | M   |     |     |      |
with
g2aX
|     |     |     |     | H   | =   | E2  |     |     |     |     | (49) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | E   |     | r   |     |     |     |      |
2
r
|     |     |     |     |     |      | 1 X |         |         |     |     |      |
| --- | --- | --- | --- | --- | ---- | --- | ------- | ------- | --- | --- | ---- |
|     |     |     |     | H   | =    | U   | ψ†ψ     | −U†ψ ψ† |     |     | (50) |
|     |     |     |     |     | h 2a |     | r r r+1 | r r     | r+1 |     |      |
r
X
|     |     |     |     | H   | =m  | (−1)rψ†ψ | ,   |     |     |     | (51) |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | M   |          | r r |     |     |     |      |
r
where a is the lattice spacing, m the fermion mass, and g is the coupling constant. H can be
E
interpretedastheelectricenergygivenintermsofE , theinteger-valuedelectricfieldsresidingon
r
ψ†
the links. The remaining terms are expressed in terms of the fermionic operators ψ r and living
r
oneachsiter, andtheunitarylinkoperatorsU =eiaAr expressedintermsofthegauge-potential
r
A = (0,A ) in the temporal-gauge. H is a lattice analog of the minimal coupling of the Dirac
| µ   | 1   |     |     |     |     | h   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fermionic field to the gauge field and H is the mass energy of the Dirac fermions, which are
M
| staggered | based | on the | (−1)r | factor. |     |     |     |     |     |     |     |
| --------- | ----- | ------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
We also have the following commutation relations between the link operators E and U
|     |     |     |     |     |        |      |               |     |      | r   | r    |
| --- | --- | --- | --- | --- | ------ | ---- | ------------- | --- | ---- | --- | ---- |
|     |     |     |     | [E  | ,U ]=U | δ    | ⇒[E ,U†]=−U†δ |     | ,    |     | (52) |
|     |     |     |     |     | r s    | r rs | r             | s   | r rs |     |      |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 19

| and between | the fermionic |     | creation | and annihilation |     | operators |     |     |     |
| ----------- | ------------- | --- | -------- | ---------------- | --- | --------- | --- | --- | --- |
}={ψ†,ψ†}=0
|     |     |     |     | {ψ ,ψ |     |        |     |     | (53) |
| --- | --- | --- | --- | ----- | --- | ------ | --- | --- | ---- |
|     |     |     |     | r s   |     | r s    |     |     |      |
|     |     |     |     |       | {ψ  | ,ψ†}=δ | .   |     | (54) |
|     |     |     |     |       |     | r s    | rs  |     |      |
We can map the fermionic creation and annihilation operators in equations (50) and (51)
onto a corresponding set of operators acting on spin degrees of freedom via the Jordan-Wigner
transformation
|     |     |     |     |     | (X −iY | ) r−1 |       |     |      |
| --- | --- | --- | --- | --- | ------ | ----- | ----- | --- | ---- |
|     |     |     |     | ψ†  | r      | r Y   |       |     |      |
|     |     |     |     | =   |        |       | Z j . |     | (55) |
|     |     |     |     | r   | 2      |       |       |     |      |
j=1
| Substituting | the | above into | (50) | and (51) | and | simplifying | yields |     |     |
| ------------ | --- | ---------- | ---- | -------- | --- | ----------- | ------ | --- | --- |
N−1
1 X
|     |     |     | H = |     | [U σ−σ+ | +U†σ+σ− |     | ]   |     |
| --- | --- | --- | --- | --- | ------- | ------- | --- | --- | --- |
|     |     |     | h   |     | r r     | r+1     | r r | r+1 |     |
2a
r=1
1 N−1
|     | X   | +U†)(X |     |     |     |     | −U†)(X |     |     |
| --- | --- | ------ | --- | --- | --- | --- | ------ | --- | --- |
= [(U r r X r+1 +Y r Y r+1 )+i(U r r X r+1 −Y r Y r+1 )] (56)
|     | 8a  |     | r   |     |     |     |     | r   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r=1
and
N
mX
|     |     |     |     | H = |     | (−1)r+1Z | .   |     | (57) |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- |
|     |     |     |     | M   |     |          | r   |     |      |
2
r=1
NotethatafactorofI/2wasdroppedintheaboveequationsincetermsproportionaltotheidentity
inaHamiltonianmerelyshiftthespectrumbyaconstant. Thederivationabovealsoassumesopen
boundary conditions, but generalizations to periodic boundary conditions are straightforward. In
that case the total number of links becomes N instead of N −1 and the asymptotic results we
| derive below | for simulating |     | the Schwinger |     | Model | remain | unchanged. |     |     |
| ------------ | -------------- | --- | ------------- | --- | ----- | ------ | ---------- | --- | --- |
It is customary to use the electric eigenbasis |(cid:15)i for the infinite-dimensional Hilbert space of
r
| each link. | In this basis, | the | E operator | takes | the | diagonal | form |     |     |
| ---------- | -------------- | --- | ---------- | ----- | --- | -------- | ---- | --- | --- |
r
X
|     |     |     |     | E   | =   | (cid:15)|(cid:15)i h(cid:15)| |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- |
|     |     |     |     | r   |     | r                             | r   |     |     |
(cid:15)
| and U | takes the form |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
r
X
|     |     |     |     | U   | =   | |(cid:15)+1ih(cid:15)|, |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
r
(cid:15)
i.e. of a raising operator. Note that in order to map these degrees onto a quantum computer, it is
customary to truncate the link Hilbert space by wrapping the electric field at a chosen cutoff Λ.
This requires modifying the commutation relations in (52) but this issue is not directly relevant
| for our | present work. |     |     |     |     |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Since H and H are manifestly a sum of unitary operators, we can use the PREPARE and
h M
SELECT oracles from the qubitization simulation technique outlined previously. The overarching
strategy is to move into the interaction frame of the H term, employ our hybrid protocols as
E
outlined in the previous sections, and determine the query complexity in terms of the qubitization
querymodel. ThephysicalreasonsforselectingtheH termfortheinteractionpictureisthatthe
E
spectral norm of E is either large for a large cutoff Λ or unbounded in the strong coupling regime
r
where g →∞. Choosing this term “removes” it from consideration in the interaction Hamiltonian
as per equation (23). Additionally, since the E operators are diagonal in its eigenbasis and the
r
matrix elements are computable in polynomial time, the cost of simulating H E in isolation is in
O(poly(nlog(1/(cid:15))) [7]. This efficiency justifies the choice to consider such simulations as oracles
in the prior discussion. As H commutes with the H term and is also 1-sparse, we may also opt
|     |     |     | M   |     |     | E   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to move into the combined interaction frame of the H and H terms. In this case, it will suffice
|     |     |     |     |     |     | E   | M   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to simulate only the H term via qubitization, and the simulation of this term will be the biggest
h
| asymptotic | driver of | the query | complexity. |     |     |     |     |     |     |
| ---------- | --------- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 20

Recall that the PREPARE oracle acts on an empty ancilla register of O(logL) qubits, if L is
thenumberoftermsinthedecompositionoftheHamiltonianintounitaryoperators,andprepares
| the superposition | state |     |     |     |     |     |
| ----------------- | ----- | --- | --- | --- | --- | --- |
L r
X w
|     |     | PREPARE≡ | l|lih0|, |     |     |     |
| --- | --- | -------- | -------- | --- | --- | --- |
λ
l=1
P
where w denotes the coefficients of the terms in the decomposition of H and λ = |w | is the
| l   |     |     |     |     | h   | l l |
| --- | --- | --- | --- | --- | --- | --- |
sum of the absolute value of the coefficients in the H term. Note that this oracle does not get
h
altered when moving into the interaction frame since the coefficients w l remain the same. Since
there are 8(N −1) terms in the LCU decomposition of H , we may set L = 8(N −1). There is
h
only one type of coefficient in H in terms of magnitude, so w /λ = 1/L and we obtain for our
|     |     | h   |     | l   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
situation
1 L
X
|     |     | PREPARE≡ | √   | |lih0|. |     | (58) |
| --- | --- | -------- | --- | ------- | --- | ---- |
L
l=1
Asaresult,wecanscaleeveryterminourHamiltonianbyafactorof8aandscalethesimulation
| time by a factor | of 1/(8a). |     |     |     |     |     |
| ---------------- | ---------- | --- | --- | --- | --- | --- |
On the other hand, a modification of the traditional select oracle is used to incorporate the
| interaction picture: |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- |
X
|     | SELECT0 ≡ | |lihl|⊗ei(HE+HM)tH0e−i(HE+HM)t |     |     |     |     |
| --- | --------- | ------------------------------ | --- | --- | --- | --- |
l
l
|     | =(I⊗ei(HE+HM)t)( |     | X |lihl|⊗H0)(I⊗e−i(HE+HM)t). |     |     |     |
| --- | ---------------- | --- | ---------------------------- | --- | --- | --- |
(59)
l
l
ThisismerelythecustomarySELECToraclebutconjugatedbytheunitaryoperatoreiHEteiHMt
on the data qubits since H and H commute. It thus suffices to give circuit implementations of
|                  | E       | M   |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- | --- |
| the usual SELECT | oracle. |     |     |     |     |     |
Tosummarize,sincetheconditionsofTheorem4.2aresatisfied,wehavethefollowingcorollary:
Corollary 5.1 (Hybrid qDRIFT and Qubitization I.P Simulation for the Schwinger Model). Let
H =H +H +H be the Schwinger model Hamiltonian as given in (49), (50), and (51). Then
| E M | h   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
we can perform the Hamiltonian simulation of H with the method of Theorem 4.2 using a total
| number of queries | to PREPARE, | SELECT,    | and W HM+HE          | (t) in   |     |      |
| ----------------- | ----------- | ---------- | -------------------- | -------- | --- | ---- |
|                   |             | (cid:18)   |                      | (cid:19) |     |      |
|                   |             | N2t2       | log(Nt/a(cid:15))    |          |     |      |
|                   |             | O          |                      | .        |     | (60) |
|                   |             | a2(cid:15) | loglog(Nt/a(cid:15)) |          |     |      |
Here, N is the number of sites in the system, a is the lattice spacing, t≥0 is the simulation time,
and (cid:15) is the error quantifying the distance in 1-norm from the ideal time-evolution channel.
Proof. Note that H h is manifestly a linear combination of unitary operators and that H M and
H are diagonal, and therefore 1-sparse, and commute with each other. Thus, the conditions of
E
Theorem 4.2 are satisfied and we may move into the interaction frame of both the H and H
M E
terms.
Tocomputetheexplicitformofλ0, notethatH consistsofasumover8(N−1)unitaryterms
h
each with a coefficient of absolute value 1/(8a). We therefore have (N −1)/a for the overall sum.
Thus
N −1
λ0
|     |     |     | = . |     |     | (61) |
| --- | --- | --- | --- | --- | --- | ---- |
a
Now note that kUk =1 for any unitary operator U. Then we have kH k ≤λ0 by using the
|     | ∞   |     |     |     | h ∞ |     |
| --- | --- | --- | --- | --- | --- | --- |
triangle-inequality and the sub-multiplicativity of the Schatten infinity norm. Substituting these
relationships into (38) and retaining the dominant terms gives the claimed query complexity.
Corollary 5.2 (Hybrid Trotter, qDRIFT, and qubitization I.P Simulation for Schwinger Model).
LetH =H E +H M +H h betheSchwingermodelHamiltonianasgivenin (49),(50),and (51). Then
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 21

wecanperformtheHamiltoniansimulationoftheSchwingermodelwiththemethodofTheorem4.3
using a number of queries to PREPARE, SELECT, and W (t) in
HE+HM
(cid:18) Nt2 log(Nt2/(a2(cid:15)2)) (cid:19)
O . (62)
a2(cid:15) loglog(Nt2/(a2(cid:15)2))
Proof. We directly apply Corollary 3.3 to the situation where we move into the interaction frame
of H and H , leaving only the H term of the Schwinger model remaining. For the terms
E M h
in H , we use the notation U σiσj , where i = 1 or 2 so that σ1 = X and σ2 = Y . Since
h r r r+1 r r r r
[U ,U ] = 0 for all r,s and [U ,U†] = 0 since U is unitary (and therefore normal), we need only
r s r r r
focus on the commutators between the Pauli matrices in computing c . But since Pauli operators
I
acting on different sites commute, we can further specialize to considering those terms that yield
[X ,Y ] = iZ . Therefore, given a term U σiσj , it fails to commute with only U σk σl
r r r r r r+1 r−1 r−1 r
and U σm σn , with analogous statements holding for U†σiσj . In other words, the terms
r+1 r+1 r+2 r r r+1
involving a particular site r fail to commute with only those involving adjacent sites. Terms such
as [U X X ,U Y Y ] do not contribute since
r r r+1 r r r+1
[U X X ,U Y Y ]=U2X Y X Y −U2Y X Y X =0,
r r r+1 r r r+1 r r r r+1 r+1 r r r r+1 r+1
where we’ve used in the anti-commutation relation twice {X ,Y }=0 to obtain the last equality.
k k
Therefore, we can decompose H into “even” and “odd” pieces as follows:
h
(N−1)/2
1 X
Heven = [(U +U† )(X X +Y Y )+i(U −U† )(X X −Y Y )]
h 8a 2r 2r 2r 2r+1 2r 2r+1 2r 2r 2r 2r+1 2r 2r+1
r=1
(N−1)/2
1 X
Hodd = [(U +U† )(X X +Y Y )+i(U −U† )(X X −Y Y )].
h 8a 2r−1 2r−1 2r−1 2r 2r−1 2r 2r−1 2r−1 2r−1 2r 2r−1 2r
r=1
Fromtheprecedingdiscussion, givenaparticularterminthe“odd”sum, thereareexactlytwo
terms in the even sum that fail to commute with it. In particular, there is exactly one term in
Heven with higher site index that fails to commute with it. Then by the definition of c ,
I I
(N −1) 1 N −1
c =k[Heven,Hodd]k= = .
I p q 2 64a2 128a2
Similarly, since each term in H has norm 1, we have
h
N−1
X 32(N −1)
4 kH k2 ≤
h ∞ 64a2.
r=1
Substituting these into (37) gives
65(N −1)t2
r ≥ . (63)
128a2(cid:15)
Substituting this and L=2 into (44) and retaining the dominant terms gives
(cid:18) Nt2 log(Nt2/(a2(cid:15)2)) (cid:19)
O (64)
a2(cid:15) loglog(Nt2/(a2(cid:15)2))
as claimed. Note that these choices for the errors ensure that the total error for approximation of
the ideal time-evolution channel via this entire procedure is (cid:15)/2+(2r)((cid:15)/4r)=(cid:15)/2+(cid:15)/2=(cid:15).
Comparing the results of the preceeding corollaries, we see that Trotterizing first before apply-
ing qDRIFT can result in improvements in the query complexity in situations where the Hamilto-
nian has additional commutator structure that can be exploited. For unstructured problems, the
additional Trotterization step is not generally useful.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 22

|     | 5.2 Construction |     | of  | Prepare | and | Select | Oracles |     |     |     |     |     |
| --- | ---------------- | --- | --- | ------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
We now give high-level circuit implementations of the aforementioned SELECT and PREPARE
|     | oracles | for the | H term | of the | Schwinger | model. |     |     |     |     |     |     |
| --- | ------- | ------- | ------ | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- |
h
We opt to employ a unary encoding of the control qubits |c i needed for the prepare and
i
select oracles, i.e. |ii = |0...1...0i, where the 1 occurs on the i-th spot in the ket. Though this
encoding requires a number of qubits linear in the number of terms in the LCU decomposition
rather than logarithmic for the implementation of the oracles, it greatly simplifies the control
|     | structures | required | within | the | circuits. |     |     |     |     |     |     |     |
| --- | ---------- | -------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ToimplementtheselectoracleforH h , weexploitcertainpatternswithinthecoefficientsofthe
terms in H . Note that there are terms with U† and U , phases of ±i, and X and Y . We can
|     |     | h   |     |     |     |     | r   | r   |     |     | r   | r   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
switchbetweenX andY viatheidentitySXS† =Y. Fromtechniquesinvolvingtwo’scomplement
numbers,thereexistsaunitaryoperatorQthatcanflipU toU† [43]. Lastly,thefactors±icanbe
|     |     |     |     |     |     |     |     | r   | r   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inserted via suitable insertions of controlled-Z gate and controlled-S gate operations. The circuit
|     | that accomplishes |     | this | is given | in Figure | 4.  |     |     |     |     |     |     |
| --- | ----------------- | --- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     | |c1i              |     | •    |          |           |     |     |     | •   |     |     |     |
|     | |c2i              |     |      |          | •         |     |     |     |     | •   |     |     |
.
.
.
| |cN−1i |      |     |      |     |      |     | •   |     |     |     | •   |     |
| ------ | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|        | |l1i | Q†  | U1 Q |     |      |     |     |     |     |     |     |     |
|        | |l2i |     |      | Q†  | U2 Q |     |     |     |     |     |     |     |
.
.
.
| |lN−1i |       |     |        |     |        | Q†      | UN−1    | Q         |           |       |     |     |
| ------ | ----- | --- | ------ | --- | ------ | ------- | ------- | --------- | --------- | ----- | --- | --- |
|        | |q1i  |     |        |     |        |         |         | S†        | X1        |       |     | S   |
|        | |q2i  |     |        |     |        |         |         | S†        | X2        | X2    |     | S   |
|        | |q3i  |     |        |     |        |         |         | S†        |           | X3    |     | S   |
|        | .     |     |        |     |        |         |         | .         |           | ...   |     | .   |
|        | .     |     |        |     |        |         |         | .         |           |       |     | .   |
|        | .     |     |        |     |        |         |         | .         |           |       |     | .   |
| |qN−1i |       |     |        |     |        |         |         | S†        |           | XN−1  |     | S   |
|        | |qNi  |     |        |     |        |         |         | S†        |           |       | XN  | S   |
|        | |0i H | •   | •      | •   |        | • •     |         | •         |           |       |     | • • |
|        | |0i H |     |        |     |        |         |         | •         |           |       |     | • • |
|        | |0i H | S   |        |     |        |         |         |           |           |       |     | Z   |
|        |       |     | Figure | 4:  | SELECT | circuit | for the | H term in | Schwinger | Model |     |     |
h
Here, |c i represent the control qubits used to implement the controlled operations, |l i the
|     |     | r   |     |     |     |     |     |     |     |     |     | r   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
qubits corresponding to the links of the system, and |q i the qubits corresponding to the sites.
r
Note how the control gate structure in this unary encoding is much more simple than what would
have been required with a binary encoding. Though the latter encoding would have required only
log(N −1) control qubits instead of N −1 as above, the advantage there is mitigated by the fact
|     | that numerous |     | multi-controlled |     | gates | would | have | been required. |     |     |     |     |
| --- | ------------- | --- | ---------------- | --- | ----- | ----- | ---- | -------------- | --- | --- | --- | --- |
Since the terms in H for a given r only differ by coefficients of ±1 or ±i, these can be
h
implemented via the insertion of a Z or S gate through the above constructions that exploit the
aforementioned patterns in H . Note that the number of qubits needed to specify the state of link
h
|l r i will depend on the cut off for the electric energy term chosen. If our cutoff is Λ, then |l r i will
|     | be a logΛ-qubit |     | state | and U | a logΛ-qubit |     | operator. |     |     |     |     |     |
| --- | --------------- | --- | ----- | ----- | ------------ | --- | --------- | --- | --- | --- | --- | --- |
r
The circuit implementation of the PREPARE oracle reduces to preparing a uniform superpo-
sition state in binary, as per (58), and then converting the encoding to a unary one. The overall
circuit with the general pattern is depicted in Figure 5 with k = log(8(N −1)) ancilla control
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 23

qubits. Note that since in the unary encoding an integer k is expressed as a state with a 1 in
the k-th spot and 0’s elsewhere, the X gate on |0i and the subsequent swaps have the effect of
1
permuting the 1 to the appropriate position.
|b 1 i H
. .
.
...
|b k−1 i H • •
|b k i H • •
|ci 1 X × ×
|ci × ×
2
|ci ×
3
|ci ×
4 . . . . ···
. .
|ci
N−1
Figure 5: PREPARE circuit for the H term in Schwinger Model
h
The control structure on the bits b encoding the binary integers for the controlled-swap gates
j
isgivenpreciselybythebinaryrepresentationofthatindex. Forexample, sincethebinaryinteger
|00...1i gets mapped to |01...0i in our unary encoding, we have to do a swap on the |0i and
1
|0i qubits controlled on the first k−1 b qubits being 0 and b being 1.
2 k
5.3 Gate Complexity Analysis
We now analyze the gate complexity per query to CTRL(W) of our simulation protocol and do
so by analyzing the circuits given in Figure 4 and Figure 5. It suffices to express the complexity
in terms of Toffoli gates since they dominate the computational complexity compared to Clifford
operations.
Our analysis proceeds as follows:
1. FirstconsiderthePREPARE† andPREPAREoperationsinFigure1. Wemaketheapprox-
imation that they have roughly the same gate complexity and that it therefore suffices to
determine the gate complexity of just the PREPARE circuit.
From Figure 5, note that we have N −1 multiply-controlled swap gates since we needed to
perform a binary-to-unary conversion to the N −1 qubits we have. Each can be converted
to standard Ck(SWAP) by inserting X gates on either side of the 0 controls. Since we
are assuming Pauli operations are approximately cost-free, it suffices to determine the gate
complexity of these N − 1 Ck(SWAP) gates. Standard circuit arguments show that the
following identities hold:

• • • • •
k  • . • • • . . • .
. . . .
. = . = . .
 • • • • •
• • •
× • •
× • • • •
Thus, each Ck(SWAP) gate can be decomposed into a Ck+1(NOT) gate and 2 CNOT gates.
FromCorollary1in[44],wegetthatCk+1(NOT)gatecanbedecomposedinto8(k+2)−24=
8k−8Toffoligatesusingonlyasingleauxiliaryqubitthatcanbereused. Thisgivesroughly
2(N−1)(8k−8)ToffoligatesthatareneededforboththePREPAREandPREPARE† parts
of Figure 1. Overall we have a gate complexity of
O(NlogN)
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 24

| with | 1 ancilla | qubit needed. |     |     |     |     |     |
| ---- | --------- | ------------- | --- | --- | --- | --- | --- |
The methods in [45] can be used to perform PREPARE circuit with NlogN controlled
swap gates, each of which can be decomposed into at most four non-Clifford operations
using [46]. This results in a smaller gate cost but ultimately does not affect the asymptotic
| gate | complexity | shown | above. |     |     |     |     |
| ---- | ---------- | ----- | ------ | --- | --- | --- | --- |
2. The multiply-controlled Z gate in Figure 1 is controlled only on the N −1 control qubits
that make up the unary encoding portion of Figure 5. Applying the above corollary again,
| we  | get a gate | complexity | of  |     |     |     |     |
| --- | ---------- | ---------- | --- | --- | --- | --- | --- |
O(N)
| with | 1 ancilla | qubit needed. |     |     |     |     |     |
| ---- | --------- | ------------- | --- | --- | --- | --- | --- |
3. To analyze the gate complexity of the controlled-SELECT operation in Figure 1, we first
examinetheoperationsthatdon’tinvolveU r andQ. Theexternalcontroldistributesamong
the operations involving the 2(N −1) controlled-S and controlled-S† gates, 2(N −2)+2
controlled-X gates, and the final 3 CNOT operations. Adding these together yields a total
r
| of 4N | −1  | Toffoli gates, | giving | a gate complexity | of  |     |     |
| ----- | --- | -------------- | ------ | ----------------- | --- | --- | --- |
O(N)
| with | no ancilla | qubits | needed. |     |     |     |     |
| ---- | ---------- | ------ | ------- | --- | --- | --- | --- |
4. For the U gates, note that its action on states is that of an incrementer. This can be
r
implementedbyutilizingthequantumripple-carryaddercircuitgivenbyCuccaro[47]. Since
weincrementlogΛ-qubitnumbers,thegatecomplexityisgiveninthepapertobe2logΛ−1
| Toffoli | gates, | 5logΛ−3 | CNOTs, | and 2logΛ−4 | negations. |     |     |
| ------- | ------ | ------- | ------ | ----------- | ---------- | --- | --- |
Since we must perform a controlled-U operation for the walk operator, we get (5logΛ−3)
r
Toffoli gates, and (2logΛ−1) C3(NOT) gates. Again from Corollary 1 in [44], the latter is
equivalent to 8(2logΛ−1) Toffoli gates with 1 extra qubit needed. Since we must perform
N −1 of these U r operations, we have altogether (N −1)(21logΛ−11) Toffoli gates, giving
| a gate | complexity | of  |     |     |     |     |     |
| ------ | ---------- | --- | --- | --- | --- | --- | --- |
O(NlogΛ)
| with | 1 ancilla | qubit needed. |     |     |     |     |     |
| ---- | --------- | ------------- | --- | --- | --- | --- | --- |
5. The Q and Q† operations can be implemented with O(log(Λ)) Toffoli gates each (see [43]),
with the extra controls giving only constant pre-factors to the cost. Since there are 2(N−1)
| of these | operations | performed, |     | we have | a gate complexity | of  |     |
| -------- | ---------- | ---------- | --- | ------- | ----------------- | --- | --- |
O(NlogΛ)
O(Nlog2(Λ))
6. Finally, the cost of performing the diagonal Hamiltonian simulation is as the
computation of the diagonal elements of the Hamiltonian involves squaring the input value,
| which | can            | be performed | in  | time O(log2(Λ)) | (see Lemma   | 2 of [48]). |     |
| ----- | -------------- | ------------ | --- | --------------- | ------------ | ----------- | --- |
| These | considerations | give         | us  | the following   | corollaries: |             |     |
Corollary5.3(GateComplexityforHybridqDRIFTandQubitizationI.P.SimulationofSchwinger
Model). Let H = H h +H M +H E be the Schwinger model Hamiltonian as given in (49), (50),
and (51). Then the Hamiltonian simulation of H can be performed using the method of Theo-
| rem 4.2 with | a   | gate complexity | in  |                                 |          |          |      |
| ------------ | --- | --------------- | --- | ------------------------------- | -------- | -------- | ---- |
|              |     |                 |     | (cid:18)                        |          | (cid:19) |      |
|              |     |                 |     | N3t2 log(Nt/a(cid:15))          |          |          |      |
|              |     |                 | O   |                                 | log2(NΛ) | ,        | (65) |
|              |     |                 |     | a2(cid:15) loglog(Nt/a(cid:15)) |          |          |      |
with an ancilla qubit overhead of O(1). In O˜ notation, the gate complexity is
|     |     |     |     | (cid:18) N3t2 | (cid:19) |     |      |
| --- | --- | --- | --- | ------------- | -------- | --- | ---- |
|     |     |     |     | O˜            | log2Λ    |     |      |
|     |     |     |     |               | .        |     | (66) |
a2(cid:15)
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 25

Proof. Summing up the scaling results from steps 1-6 as outlined above, we get a per-query gate
| complexity | of  |                                   |     |     |     |     |     |     |      |
| ---------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|            |     | O(Nlog2(Λ)+Nlog(N))⊆O(Nlog2(NΛ)). |     |     |     |     |     |     | (67) |
Multiplying these by (60) and retaining the dominant terms yields the stated results.
Corollary 5.4 (Gate Complexity for Hybrid Trotter, qDRIFT, Qubitization I.P. Simulation
of Schwinger Model). Let H = H +H +H be the Schwinger model Hamiltonian as given
|     |     |     | h   | M E |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in (49), (50), and (51). Then the Hamiltonian simulation of H can be performed using the method
| of Theorem | 4.3 with | a gate | complexity    | in                        |     |         |          |     |      |
| ---------- | -------- | ------ | ------------- | ------------------------- | --- | ------- | -------- | --- | ---- |
|            |          |        | (cid:18) N2t2 | log(Nt2/(a2(cid:15)2))    |     |         | (cid:19) |     |      |
|            |          |        | O             |                           |     | log2(Λ) | ,        |     | (68) |
|            |          |        | a2(cid:15)    | loglog(Nt2/(a2(cid:15)2)) |     |         |          |     |      |
O˜
with an ancilla qubit overhead of O(1). In notation, the gate complexity is
|     |     |     |     | (cid:18) N2t2 |     | (cid:19) |     |     |      |
| --- | --- | --- | --- | ------------- | --- | -------- | --- | --- | ---- |
|     |     |     |     | O˜ log2(Λ)    |     |          |     |     |      |
|     |     |     |     |               |     | .        |     |     | (69) |
a2(cid:15)
Proof. Multiplying(62)byNlog(NΛ)givesthebig-Ocost. Droppingallsub-dominantlogarithmic
O˜
| factors gives  | the scaling. |                |     |     |     |     |     |     |     |
| -------------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
| 5.4 Comparison | with         | Trotterization |     |     |     |     |     |     |     |
Theresultsof (66)and(69)canbedirectlycomparedwiththeresultgiveninCorollary11of[48]for
using a second-order Trotter-Suzuki formula to perform the quantum simulation of the Schwinger
model. Wewillfirstconsidertheregimeinwhichsimulationsarecarriedatconstant1/(ga)=O(1)
and for fixed m/g = O(1). For this condition, we can use the result in Corollary 9 of [48] which
after rescaling the time variable T → ag2t/2 to align with our normalization conventions for the
| Schwinger | Model Hamiltonian, |     | gives a                          | total T-gate | cost                           | of  |     |     |     |
| --------- | ------------------ | --- | -------------------------------- | ------------ | ------------------------------ | --- | --- | --- | --- |
|           |                    |     | (cid:18) N3/2t3/2Λa1/2g2(cid:19) |              | (cid:18) N3/2t3/2Λg3/2(cid:19) |     |     |     |     |
|           |                    | O˜  |                                  | =O˜          |                                |     |     |     |     |
.
|        |              |     | (cid:15)1/2    |              |            | (cid:15)1/2 |          |     |     |
| ------ | ------------ | --- | -------------- | ------------ | ---------- | ----------- | -------- | --- | --- |
| In the | same regime, | the | result of (69) | gives a gate | complexity |             | in       |     |     |
|        |              |     | (cid:18)       | (cid:19)     | (cid:18)   |             | (cid:19) |     |     |
|        |              |     | N2t2           |              | N2t2g2     |             |          |     |     |
|        |              |     | O˜ log2(Λ)     | =O˜          |            | log2(Λ)     | .        |     |     |
a2(cid:15)
(cid:15)
We then see that the hybrid I.P. scheme provides a quasi-exponential speedup with respect to the
electric cutoff Λ over the second-order Trotter-Suzuki approach, at the expense of a slightly worse
| scaling in | all the other | parameters | (N,t,g,(cid:15)). |     |     |     |     |     |     |
| ---------- | ------------- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- |
In order to extract physical observables however, it is important to consider that the number
of sites N and the the lattice spacing cannot be chosen independently as the product L = Na
gives the physical size of the system. In past numerical simulations it was found that choosing
Nga = O(10) is appropriate for a large number of configurations (see e.g. [36]). In order to keep
our derivation general, we will then introduce the dimensionless parameter l = Nga. In addition
to the thermodynamic limit Na → ∞, one also has to work with ga → 0 in order to recover the
continuum limit of the theory. The resulting gate complexity of the hybrid I.P. algorithm from
| Corollary | 5.4 is found | to be |     |          |     |          |     |     |     |
| --------- | ------------ | ----- | --- | -------- | --- | -------- | --- | --- | --- |
|           |              |       |     | (cid:18) |     | (cid:19) |     |     |     |
l2t2
|     |     |     |     | O˜ log2(Λ) |     | ,   |     |     |     |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
g2a4(cid:15)
while for the second order Trotter-Suzuki scheme we have to consider two distinct regimes
| • large | cutoff limit | Λga>1, | in which | case the           | T-gate | count    | is bounded | by  |     |
| ------- | ------------ | ------ | -------- | ------------------ | ------ | -------- | ---------- | --- | --- |
|         |              |        |          | (cid:18) l3/2t3/2Λ |        | (cid:19) |            |     |     |
O˜
,
a3/2(cid:15)1/2
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 26

• small lattice spacing limit Λga < 1, in which case the result of Corollary 9 of [48] does not
holdanymore. TheT-gatecountcanbefoundinsteadbyusingthemore generalresultfrom
| Corollary | 11 there, | resulting |     | in the | Λ-independent |          | scaling  |     |
| --------- | --------- | --------- | --- | ------ | ------------- | -------- | -------- | --- |
|           |           |           |     |        | (cid:18)      | l3/2t3/2 | (cid:19) |     |
|           |           |           |     |        | O˜            |          | .        |     |
g3/2a3(cid:15)1/2
These results show that for fixed error (cid:15) and lattice extent l, the hybrid I.P. approach can be
especially beneficial in the first regime thanks to the poly-logarithmic dependence on the cutoff Λ.
Inthesmalllatticespacingregimerelevantforthecontinuumlimit,thesecondorderTrotter-Suzuki
scheme developed in [48] has instead a better scaling with respect to all the parameters.
Finally,forthecontinuumlimititmightbepossibletoimprovethethegatecomplexityinsome
regimes by choosing to perform the I.P. simulation in the rotating frame given by the the interac-
tion Hamiltonian H instead. Using the hybrid Trotter and qDRIFT scheme from Corollary 3.3,
h
together with the implementation via qubitization of the time evolution operator for H derived
h
| in Section | 5.2, this scheme |     | has gate | cost | in       |                          |          |     |
| ---------- | ---------------- | --- | -------- | ---- | -------- | ------------------------ | -------- | --- |
|            |                  |     | (cid:18) | N2t  | N2t2     |                          | (cid:19) |     |
|            |                  |     | O˜       |      |          | (cid:0) m2+g4a2Λ4(cid:1) |          |     |
|            |                  |     |          | +    |          |                          | .        |     |
|            |                  |     |          | a    | (cid:15) |                          |          |     |
For m/g =O(1) and introducing the dimensional lattice size l=Nga, this becomes
|     |     |     |     | (cid:18) l2t | l2t2       | l2t2     | (cid:19) |     |
| --- | --- | --- | --- | ------------ | ---------- | -------- | -------- | --- |
|     |     |     |     | O˜           |            |          | g2Λ4     |     |
|     |     |     |     |              | +          | +        | .        |     |
|     |     |     |     | g2a3         | a2(cid:15) | (cid:15) |          |     |
ThisisclearlyworsethaneithertheHybridapproachesdiscussedaboveorthesecondorderTrotter-
Suzukischemefrom[48]inthelargecutofflimitΛga>1,butcanbecomecompetitiveinthesmall
| lattice spacing | limit | Λga<1 | for some | choices | of  | ((cid:15),l,Λ). |     |     |
| --------------- | ----- | ----- | -------- | ------- | --- | --------------- | --- | --- |
A detailed comparison of these different schemes to extract continuum quantities of physical
interestintheSchwingermodelwithsometargetprecisionδwouldrequireamorecarefulanalysisof
thescalingofthelatticesizelandtheelectricfieldcutoffΛ,aswellasamorecarefulconsideration
of the logarithmic factors hidden by the O˜ notation. We leave this interesting extension of the
| present work | to future | studies. |              |     |     |     |     |     |
| ------------ | --------- | -------- | ------------ | --- | --- | --- | --- | --- |
| 6 Collective | Neutrino  |          | Oscillations |     |     |     |     |     |
Inextremeastrophysicalenvironments,suchassupernovaexplosions,neutrinosarepresentinsuch
large densities that neutrino-neutrino interactions can become important to describe flavor evolu-
tion [49, 50]. These interactions are responsible for the appearance of collective modes in flavor
oscillations and have traditionally been studied with the help of a mean-field approximation (see
e.g. [51, 52] for reviews). Due to the presence of interactions, many-body effects and quantum
correlations could be important in understanding these phenomena and a number of studies is un-
derwaywithavarietyoftechniques: fromexactdiagonalization[53]toBethe-ansatzsolutions[54],
from tensor networks [55, 56] to digital quantum simulations [57, 58]. Quantum computing might
offer a promising route to study these phenomena in situations where the entanglement entropy
grows too fast with system size for tensor network simulations to remain feasible.
An important obstacle towards describing collective oscillations in realistic regimes is the fact
that besides interactions with other neutrinos, scattering with external leptons (especially the
abundant electrons) is an important effect near the proto-neutron star. The matter interaction
terms can become the dominant contributions in this regime, requiring very small time-steps for
an accurate simulation of the flavor dynamics. On the quantum computing side, this requirement
translates into a large number of gates required for the simulation and it is therefore important to
designsimulationalgorithmswithagentlecomputationalscalingwiththeexternalmatterdensity.
The Hamiltonian we are interested in can be written as follows (see e.g. [59] for a derivation)
|     |     |     | N   |     |     | N   | N          |      |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- |
|     |     |     | Xω  | iB~ | λX  |     | µ X        |      |
|     |     | H   | =   | ·~σ | +   | Z + | J ~σ ·~σ . | (70) |
|     |     |     |     | 2   | i 2 | i   | 2N ij i j  |      |
|     |     |     | i=1 |     | i=1 |     | i<j        |      |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 27

Here~σ isthevectorofPaulimatricesactingonthei-thqubitandthesingleparticleenergiesω are
i i
positiveforneutrinosandnegativeforanti-neutrinos. ThecouplingmatrixJ takesvaluesin[0,2]
ij
andthenormalizedvectorB~ containsthevacuummixingangleasB~ =(sin(2θ),0,−cos(2θ)). The
√ √
constants are given by λ= 2G n and µ= 2G n , with G Fermi’s constant and n and n
F e F ν F e ν
theelectronandneutrinodensitiesrespectively. Intypicalsituationstheelectroncontributionλis
thedominantterm. Astandardapproachtodealwiththisproblemistomovetotherotatingframe
defined by the unitary U (t) = exp(−itλ PN Z ) and define the Hamiltonian in the interaction
e 2 i=1 i
picture as
∂
H(t)=U†(t)HU (t)−iU†(t) U (t)
e e e ∂t e
N N N
=sin(2θ) Xω i (cos(λt)X −sin(λt)Y )−cos(2θ) Xω iZ + µ X J ~σ ·~σ (71)
2 i i 2 i 2N ij i j
i=1 i=1 i<j
P P
=eiλ
i
ZitH
ν
e−iλ
i
Zit,
where
N N
H = Xω iB~ ·~σ + µ X J ~σ ·~σ . (72)
ν 2 i 2N ij i j
i=1 i<j
Typically only the leading order contribution in the Magnus expansion is retained, giving the
time-independent Hamiltonian
N N
H =−cos(2θ) Xω iZ + µ X J ~σ ·~σ . (73)
0 2 i 2N ij i j
i=1 i<j
In this limit, flavor states will not experience oscillations and typically this is solved by defin-
ing the flavor axis to be rotated by a small phenomenological amount away from the Z axis. It
would be desirable however to be able to exercise more control in this approximation. Expan-
sions to high orders in the Magnus expansion quickly produce higher order interactions which
will complicate the implementation of the corresponding time-independent evolution. Here we use
the time-dependent algorithm described above to work directly in the interaction picture without
introducing uncontrollable errors.
6.1 Trotter Suzuki Approximations in Interaction Frame
As a first step, let us consider simulating the Hamiltonian in the interaction frame using a kth-
order Trotter-Suzuki formula such as those in [8]. To do this, we need to introduce a notion of the
typical energy scale of the time-dependent Hamiltonian with respect to the Trotter decomposition
of the interaction frame Hamiltonian. If we use a conventional Trotter decomposition, as opposed
to (18), we find that the error incurred from using a first-order Trotter formula for an ordered
operator exponential U (t) formed by evaluating the Hamiltonian at t = 0 and then Trotterizing
1
the resultant ordinary operator exponential is
(cid:13) (cid:18) Z (cid:19) (cid:13)
(cid:13) (cid:13) (cid:13) exp τ −i H(t)dt −U 1 (t) (cid:13) (cid:13) (cid:13) ∈O((m t axkH0(t)k ∞ + X m t axk[H p (t),H q (t)]k ∞ )t2), (74)
∞ p,q
where the specific constants can be found using the techniques in [33]. The derivative of the
Hamiltonian in the interaction frame is in
kH0(t)k ∈O(θNλ). (75)
∞
The commutator sum similarly obeys
k X maxk[H (t0),H (t)]k ∈O (cid:0) Nωθ+µNθ+ωNµ+Nµ2(cid:1)
p q ∞
t,t0
p,q
=O(N(θ(ω+µ)+µ(ω+µ)))
⊆O (cid:0) Nµ2) (cid:1) , (76)
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 28

| where ω | =max | |ω | | and in | the last | term | we take µ(cid:29)ω. |     |     |     |
| ------- | ---- | ---- | ------ | -------- | ---- | ------------------- | --- | --- | --- |
i i
| The overall |     | error | in the | simulation | is  | therefore                  |     |     |      |
| ----------- | --- | ----- | ------ | ---------- | --- | -------------------------- | --- | --- | ---- |
|             |     |       |        |            |     | (cid:0) (Nµ2+θNλ)t2(cid:1) |     |     |      |
|             |     |       |        |            | O   |                            | .   |     | (77) |
If we break the overall evolution into r time slices, then it follows that the error in the simulation
| can be made | at  | most | (cid:15) by choosing |     |     |     |     |     |     |
| ----------- | --- | ---- | -------------------- | --- | --- | --- | --- | --- | --- |
(cid:18) N(µ2+θλ)t2(cid:19)
|     |     |     |     |     | r ∈O |     |     | .   | (78) |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
(cid:15)
AsthereareO(N2)operatorexponentialspertimestep,thetotalnumberofoperatorexponentials
| needed to | perform | the | simulation |     | is  |     |     |     |     |
| --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(cid:18) N3(µ2+θλ)t2(cid:19)
|     |     |     |     |     | N ∈O |          |     | .   | (79) |
| --- | --- | --- | --- | --- | ---- | -------- | --- | --- | ---- |
|     |     |     |     |     | exp  | (cid:15) |     |     |      |
Since each operator exponential requires O(1) gates from the H,R z ,CNOT gate library, the gate
complexity is also proportional to this [7]. Interestingly, using the swap-network protocol from
Ref. [57] (and inspired from their fermionic variant [60]), this cost is not affected by limited con-
nectivity in the device despite the interaction being all-to-all. This cost also coincides with the
optimal scaling with λ permitted by the no-fast forwarding theorem [27], despite being a low-
order formula that has inferior scaling with respect to the other parameters relative to alternative
| simulation | methods. |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Higher-ordertime-dependent Trotterformulasforthesimulationcanbeused,buttheadvantage
gleaned by using them with respect to the λ scaling is less clear. Such algorithms scale with the
| parameter | [8] |     |         |                           |     |     |     |            |      |
| --------- | --- | --- | ------- | ------------------------- | --- | --- | --- | ---------- | ---- |
|           |     |     | Λk+1/rk | =max(k∂jH(t)k1/j+1)k+1/rk |     |     |     | ∈O(λk/rk), | (80) |
|           |     |     | k       |                           |     | t ∞ |     |            |      |
j≤k
where k represents the orderof the Trotter formula. It thenfollows that these formulasultimately
lead to the same linear scaling in the gate complexity with λ (assuming that θ ∈ Θ(1)). By
contrast, if we did not use the interaction picture algorithm, the cost of simulation using the kth-
O(λ1+1/2k)
order Trotter time-independent formula would scale as [7, 8]. This illustrates that for
problems with an imbalance in the scales of the operators, switching to an interaction frame can
| be beneficial | at  | virtually | no  | cost overhead. |     |     |     |     |     |
| ------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
6.2 Simulating Neutrino Oscillations using Hybrid Trotter-qDRIFT
Now we will apply Corollary 3.3 to compare this cost to that required by the hybrid Trotter and
continuous qDRIFT algorithm. Specifically, the error in an r-segment simulation is of the form
| (under the | assumption |     | that | µ(cid:29)ω) |     |            |                        |     |     |
| ---------- | ---------- | --- | ---- | ----------- | --- | ---------- | ---------------------- | --- | --- |
|            |            |     |      | t2(cid:18)  |     | L (cid:19) | (cid:18) Nµ2t2(cid:19) |     |     |
X
|     |     |     |     | c   | +4  | kH k2 ∈O |     | .   | (81) |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- |
|     |     |     |     | r   | I   | k ∞      |     | r   |      |
k6=l
As each segment of qubitization requires application of a first order Trotter formula, the cost per
O(N2).
segment in terms of operator exponentials scales as Thus if we demand that the error is
| at most (cid:15), | the | cost is |     |     |     |          |                |     |     |
| ----------------- | --- | ------- | --- | --- | --- | -------- | -------------- | --- | --- |
|                   |     |         |     |     |     | (cid:18) | N3µ2t2(cid:19) |     |     |
∈O(N2r)⊆O
|     |     |     |     | N   | exp |     |     | ,   | (82) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
(cid:15)
whereineachoperatorexponentialrequiresO(1)applicationsofH,R andCNOT.Thisshowsthat
z
the above asymptotic scaling applies in the gate complexity as well as the number of exponentials.
Interestingly, in the limit where λ (cid:29) 1, this result provides better scaling than even the gate
complexityofthetruncatedDysonseries[20,21]whichscalesintheinteractionframeaslog(λ). In
our case, the quantum computational complexity is completely independent of λ. Of course, poly-
logarithmic costs with these algorithms need to be incurred at the classical side to compute the
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 29

rotation angles that go into the single qubit rotations but such costs are assumed to be negligible
in our cost model. This implies that for such cases where the cost of the simulation is gated
by the cost of preparing and controlling from the time-register, switching to a method that only
requiresclassicalcontrolscanallowustooutperformsuchmethodsandmakethegatecount(rather
than just the query complexity [21]) independent of the magnitude of the norm of the interaction
Hamiltonian.
As a final note, similar scaling can also be attained by using the approach of [9] to time-order
the operator exponentials that we use in the interaction frame. The performance of this method
is summarized in (18) and gives an alternative to the hybrid approach considered here and yields
| comparable |             | scaling | with        | λ.  |          |     |     |     |     |     |     |     |
| ---------- | ----------- | ------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 7          | Constrained |         | Hamiltonian |     | Dynamics |     |     |     |     |     |     |     |
As a final application of these techniques, let us consider the application of quantum simulation
to dynamics subject to dynamical constraints. Specifically, we will consider a Hamiltonian of the
form
|     |     |     |     |     |     | H =H | +λP | ,   |     |     |     | (83) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |      | f c |     |     |     |     |      |
where H ∈ C2n×2n is the free Hamiltonian and P ∈ C2n×2n is a projector onto an infeasible
|     | f   |     |     |     |     |     | c   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
region. The idea behind our approach to simulating constrained quantum dynamics is that if we
choose λ (cid:29) kH k and an initial state |ψi = (1−P )|ψi, then the dynamics of the quantum
|     |     | f   | ∞   |     |     |     | c   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
system will, up to small errors, be confined to within the dynamically feasible region specified by
thenull-spaceofP . Notethatthisresultisreminiscentofothersintheliteraturesuchas[61,62];
c
however, this result is specialized to time evolution and is simpler to employ in this context.
∈C2n×2n
Lemma7.1. LetH beafreeHamiltonianforasystemandletλbeavariabledescribing
f
thestrengthoftheconstraintsuchthatkH k (cid:28)λ. Wethenhavethatforany|ψiinthenull-space
f ∞
of P ,
|     | c   |     |                   |     |     |                     |     | (cid:18) |      | (cid:19) |     |     |
| --- | --- | --- | ----------------- | --- | --- | ------------------- | --- | -------- | ---- | -------- | --- | --- |
|     |     |     |                   |     |     |                     |     | kH       | k2 t |          |     |     |
|     |     |     | ke−i(Hf−λPc)t|ψi− |     | l   | im e−i(Hf−λPc)t|ψik |     | ∈O       | f ∞  |          |     |     |
2
|       |     |        |        |        | λ →     | ∞   |     |     | λ   |     |     |     |
| ----- | --- | ------ | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
| where | k·k | refers | to the | vector | 2-norm. |     |     |     |     |     |     |     |
2
Proof. In order to show the deviation in each eigenvector of the Hamiltonian that arises from
| adding | the small | Hamiltonian |     | H   | to the | constraint | term, | we will introduce |     |     |     |     |
| ------ | --------- | ----------- | --- | --- | ------ | ---------- | ----- | ----------------- | --- | --- | --- | --- |
f
|     |     |     |     |     | H   | (x):=H | x+λP | ,   |     |     |     | (84) |
| --- | --- | --- | --- | --- | --- | ------ | ---- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | f      | f    | c   |     |     |     |      |
wherex∈[0,1]. Forx=0,H (0)=λP hasadegeneratenull-spacedenotedP0. Let|v (x)idenote
|     |     |     |     | f   | c   |     |     |     |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the eigenvectors of H (x) with corresponding eigenvalues E (x). We then have from perturbation
|        |      |                | f   |       |         |     |     | j   |     |     |     |     |
| ------ | ---- | -------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
| theory | that | the derivative |     | of |v | (x)i is |     |     |     |     |     |     |     |
j
|     |     |     |     | ∂|v | (x)i | X   | hv (x)|H | |v (x)i |     |     |     |      |
| --- | --- | --- | --- | --- | ---- | --- | -------- | ------- | --- | --- | --- | ---- |
|     |     |     |     |     | j =  | |v  | (x)i k   | f j     |     |     |     | (85) |
k
|     |     |     |     |     | ∂x  |     | E j (x)−E | k (x) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- |
k6=j
Assuming that the eigenvalue gaps are non-zero, we further have that the second derivative is
| finite.  | From | the definition |       | of a Riemann |     | integral, | we get        |                |     |                |     |     |
| -------- | ---- | -------------- | ----- | ------------ | --- | --------- | ------------- | -------------- | --- | -------------- | --- | --- |
|          | Z    |                |       |              |     | r         |               |                |     |                |     |     |
|          |      | 1 ∂|v (x)i     |       |              |     | X X       |               | hv ((p−1)/r)|H |     | |v ((p−1)/r)i1 |     |     |
| |v (1)i= |      | j              | dx=|v | (0)i+        | lim |           | |v ((p−1)/r)i | k              |     | f j            |     | .   |
| j        |      |                |       | j            |     |           | k             |                |     |                |     |     |
|          |      | ∂x             |       |              | r→∞ |           |               | E ((p−1)/r)−E  |     | ((p−1)/r)      |     | r   |
|          | 0    |                |       |              |     | p=2k6=j   |               | j              |     | k              |     |     |
(86)
This expression allows us to relate the shift in the eigenvectors recursively. First let us consider
the initial time step. As H (x) is degenerate at x = 0, we can choose the eigenvectors such
f
that the matrix with components hv (0)|H |v (0)i is a diagonal matrix for all |v (0)i,|v (0)i ∈
|     |     |     |     |     | j   | f   | k   |     |     | j   | k   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P0⊥
P0 or |v (0)i,|v (0)i ∈ . In the former case we have that (1 − P )|v (0)i = |v (0)i, so
|     | j   | k   |     |     |     |     |     |     | c   | j   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hv (0)|H |v (0)i = hv (0)|(1−P )H (1−P )|v (0)i. Thus we can achieve the diagonal crite-
| j   | f k |     | j   |     | c f | c   | k    |      |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | (1−P | (1−P |     |     |     |     |
ria by choosing each |v (0)i to be an eigenvector of )H ). Similarly, we can achieve
|     |     |     | j   |     |     |     |     | c f | c   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 30

the diagonal criteria for each vector in
P0⊥
by choosing each |v i to be an eigenvector of P H P .
j c f c
We then have that for any |v (0)i in P0,
j
|v (1/r)i=|v (0)i+
1X
|v (0)i
hv
k
(0)|H
f
|v
j
(0)i
j j r k E (0)−E (0)
j k
k6=j
=|v (0)i− X |v (0)i hv k (0)|H f |v j (0)i . (87)
j k λr
k:|vk(0)i6=P0
In turn
k|v (0)i−|v (1/r)ik ∈O(kH k /λr). (88)
j j 2 f ∞
Furthermorefrom[63], wehavethatforallk, |E (x)−E (0)|≤xkH k . Nowletusassumethat
k k f ∞
for some integer q ≥0
k|v (0)i−|v (q/r)ik ∈O(qkH k /λr). (89)
j j 2 f ∞
We then have
|v ((q+1)/r)i=|v (q/r)i+
1X
|v (q/r)i
hv
k
(q/r)|H
f
|v
j
(q/r)i
(90)
j j r k E (q/r)−E (q/r)
j k
k6=j
and therefore
(cid:18) (cid:19) (cid:18) (cid:19)
kH k kH k
k|v ((q+1)/r)i−|v (q/r)ik ∈O f ∞ =O f ∞ . (91)
j j 2 (λ−2kH k )r λr
f ∞
Thus we have
k|v ((q+1)/r)i−|v (0)ik ≤k|v ((q+1)/r)i−|v (q/r)ik +k|v (0)i−|v (q/r)ik
j j 2 j j 2 j j 2
(cid:18) (cid:19)
(q+1)kH k
∈O f ∞ . (92)
λr
This in turn shows us that
(cid:18) (cid:19)
kH k
k|v (1)i−|v (0)ik ∈O f ∞ . (93)
j j 2 λ
Next by examining the differential equation for the eigenvalues, we have that the corresponding
eigenvalue E (1) obeys
j
Z 1 ∂E (x) Z 1 ∂E (x)
E (1)=E (0)+ j dx= j dx
j j ∂x ∂x
0 0
Z 1 (cid:18) kH k2 (cid:19)
= hv (x)|H |v (x)idx=hv (0)|H |v (0)i+O f ∞ . (94)
j f j j f j λ
0
Similarly for any |v (0)i ∈
P0⊥
, E (1) = λ+hv (0)|H |v (0)i+O
(cid:16) kHfk2
∞
(cid:17)
. We therefore have
j j j f j λ
from the triangle inequality that
X
kH(1)− (λδ +hv (0)|H |v (0)i|v (0)ihv (0)|)k
|vki∈P0⊥ k f k k k ∞
k
(cid:18) kH k2 (cid:19)
∈O f ∞ . (95)
λ
We therefore have from the fact that ke−iHt−e−iH0tk ≤kH−H0k t for all Hermitian matrices
∞ ∞
H and H0 of equal dimension that
(cid:16) (cid:17)
ke−iH(1)t−e
−i P
k
λδ |vki∈P0⊥+hvk(0)|Hf|vk(0)i|vk(0)ihvk(0)| t
k ∈O
(cid:18) kH
f
k2
∞
t (cid:19)
. (96)
∞ λ
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 31

| Therefore | for any |ψi∈P0 | we            | have that |                  |     |          |             |      |
| --------- | -------------- | ------------- | --------- | ---------------- | --- | -------- | ----------- | ---- |
|           |                |               |           |                  |     | (cid:18) | k2 (cid:19) |      |
|           |                |               |           |                  |     | kH       | f t         |      |
|           |                | ke−iH(1)t|ψi− |           | lim e−iH(1)t|ψik |     | ∈O       | ∞ .         | (97) |
|           |                |               |           |                  |     | 2        | λ           |      |
λ→∞
This shows that we can simulate constrained dynamics for time t within error (cid:15) by choosing
λ ≥ kH k2 t/(cid:15). This in turn leads to a substantial degradation of the scaling of most simulation
| f   | ∞   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
algorithms if [H ,P ] 6= 0, because the Hamiltonian’s norm scales with both the evolution time
f c
and the uncertainty desired in the simulation. This makes such constrained dynamics impractical
| for many | applications. |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
This drawback can, however, be mitigated through the use of an interaction frame transforma-
tion. Bytransformingtotheinteractionframeoftheconstraint, wecanperform thesimulationat
costthatis(insomecases)independentofthechoiceofλ. Thecostofsuchsimulationsusingahy-
brid qubitization and qDRIFT algorithm is given below. We cite the complexity of this algorithm
rather than truncated Dyson methods because such methods explicitly have a cost that scales
logarithmically with λ; whereas in some cases the quantum gate complexity will be independent
of λ.
Theorem 7.2. Let the assumptions of Theorem 4.2 hold. Then there exists a quantum algorithm
thatimplements, foranyt>0and(cid:15)>0, aquantumchannelthatisa(1,O(log(L)),(cid:15))blockencod-
e−i(Hf+λPc)t.
ing of Further this implementation requires a total number of queries to PREPARE,
| SELECT | and W | in  |     |     |     |     |     |     |
| ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Pc
|     |     | (cid:18) | (cid:18) | kH k2 t2(cid:19) | log(kH    | k t/(cid:15)) | (cid:19)    |     |
| --- | --- | -------- | -------- | ---------------- | --------- | ------------- | ----------- | --- |
|     |     |          |          | f ∞              |           | f ∞           |             |     |
|     |     | O        | βt+      |                  |           |               | .           |     |
|     |     |          |          | (cid:15)         | loglog(kH | k             | t/(cid:15)) |     |
f ∞
Proof. The proof follows directly from previous results. Specifically we have that
|     | kV|ψi− | lim e−i(Hf+λPc)tk |     |     |     |     |     |     |
| --- | ------ | ----------------- | --- | --- | --- | --- | --- | --- |
2
λ→∞
≤kV|ψi−e−i(Hf+λPc)t|ψik +ke−i(Hf+λPc)t|ψi− lim e−i(Hf+λPc)t|ψik . (98)
|     |     |     |     | 2   |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
λ→∞
From Theorem 4.2, we have that the number of queries to PREPARE, SELECT and W needed
Pc
| to implement | a (1,O(log(L)),(cid:15)/2) |          | block    | encoding   | is        | in            |             |     |
| ------------ | -------------------------- | -------- | -------- | ---------- | --------- | ------------- | ----------- | --- |
|              |                            | (cid:18) | (cid:18) | t2(cid:19) |           |               | (cid:19)    |     |
|              |                            |          |          | kH k2      | log(kH    | k t/(cid:15)) |             |     |
|              |                            | O        | βt+      | f ∞        |           | f ∞           | .           |     |
|              |                            |          |          | (cid:15)   | loglog(kH | f k ∞         | t/(cid:15)) |     |
Next, from Theorem 7.1 we have that there exists a value of λ ∈ O(kH k2 t/(cid:15)) such that
f ∞
ke−i(Hf+λPc)t|ψi−lim e−i(Hf+λPc)t|ψik ≤ (cid:15)/2. The result then follows from the triangle
|     |     | λ→∞ |     | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
inequality.
These results show that query efficient methods exist for simulating Hamiltonian dynamics;
however,theexistenceofaqueryefficientalgorithmforsimulatingdynamicssubjecttoaparticular
constraint does not imply the existence of a gate efficient algorithm. For example, let us consider
the case where P |xi=|xi if and only if E(x)≤δ for some δ >0 and E(x) is the energy function
c
for an arbitrary Ising model. Since this problem is NP-hard [64], a gate efficient version of this
constraint is only possible if NP ⊆ BQP, which is strongly believed to be false. For this reason,
we provide below a sufficient, but not a necessary, condition for the W Pc to be simulatable in
| O(polylog(2nλt/(cid:15))) |     | gate operations. |     |     |     |     |     |     |
| ------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
∈C2n×2n
Proposition 7.3. Let P be a projector matrix. Suppose there exist functions such that
c
for any x,y ∈Z , g(x,y)=hx|P |yi and f(x,i) yields the column index of the ith non-zero matrix
|            | 2n               |     | c                 |     |        |     |     |     |
| ---------- | ---------------- | --- | ----------------- | --- | ------ | --- | --- | --- |
| element of | P as represented | in  | the computational |     | basis. | If  |     |     |
c
1. P has at most 1 non-zero matrix elements in each row when expressed in the computational
c
basis.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 32

2. f is computable using a number of quantum gates that are in O(poly(n)) and g within error
| 2−m using | O(poly(nm)) | quantum | operations |     |     |     |
| --------- | ----------- | ------- | ---------- | --- | --- | --- |
then for any λ≥0 and t≥0, a unitary U˜ can be constructed such that kU˜ −U (λ;t)k ≤(cid:15) using
I ∞
| O(polylog(2nλt/(cid:15))) | quantum | operations. |     |     |     |     |
| ------------------------- | ------- | ----------- | --- | --- | --- | --- |
Proof. The proof follows straight forwardly. If we assume that g(x,y) can be implemented within
e−iλPct
zero error with m bits of precision, we have from [65] that can be implemented with zero
error using O(1) applications of f and g as well as O(poly(nm)) auxillary quantum operations.
Now let us assume that g(x,y) cannot be computed within zero error using m < ∞ bits of
precision. If we denote g˜(x,y) to be the approximate version of g, we have from the fact that P c
| is one-sparse                       | that |     |                          |     |     |     |
| ----------------------------------- | ---- | --- | ------------------------ | --- | --- | --- |
| P                                   |      |     | P                        |     |     |     |
| ke−iλt g(x,f(x,1))|xihf(x,1)|−e−iλt |      |     | g˜(x,f(x,1))|xihf(x,1)|k |     |     |     |
| x                                   |      |     | x                        |     |     |     |
∞

ke−iλtg(x,f(x,1))(|xihf(x,1)|+|f(x,1)ihx|)−e−iλtg˜(x,f(x,1))(|xihf(x,1)|+|f(x,1)ihx|)k
| =max | max |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- |
∞
x:x6=f(x,1)
!
ke−iλtg(x,f(x,1))|xihx|−e−iλtg˜(x,f(x,1))|xihx|)k
|     | ,   | max |     |     |     | ∞   |
| --- | --- | --- | --- | --- | --- | --- |
x:x=f(x,1)
≤λtmax|g(x,f(x,1))−g˜(x,f(x,1))|≤λt2−m
. (99)
x
Thus to achieve an error of (cid:15), we need to take m ∈ O(log(λt/(cid:15))). The result immediately follows
| from the assumptions |     | on the cost | of f and | g.  |     |     |
| -------------------- | --- | ----------- | -------- | --- | --- | --- |
There are a number of applications of this approach to solve constrained versions of quantum
dynamics. One such application involves the simulation of quantum field theories within a partic-
ular gauge, which describes a choice of a dynamically unobservable feature of the system that is
needed to unambiguously determine the dynamics. For example, the Lorenz gauge involves choos-
ing the vector potential such that ∂ Aµ =0. Rather than fixing the gauge by a clever choice of an
µ
equationofmotion, thisapproachallowsustoimposesuchgaugesbypenalizingallconfigurations
| that violate this. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- |
AnotherapplicationinvolvesGauss’lawinquantumelectrodynamics[38,66]. ForD-dimensional
quantum electrodynamics, Gauss’ law reads ∇·Eˆ(s)−ρˆ(s) = 0, where Eˆ(s) is the electric field
operatoratpositionsandρˆ(s)isthechargedensitythere. Onalattice,thiscanbefurthersimpli-
fiedtoG(s):= PD (Eˆ(s)−Eˆ(s−e ))− P e n (s), wheren (s)isthenumberofelectrons(or
|     | i=1 |     | i   | s,σ σ σ | σ   |     |
| --- | --- | --- | --- | ------- | --- | --- |
positrons)atasiteande is±1dependingonthesite. Fromthis,theconstraintprojectorP canbe
σ c
expressed using the properties of discrete Fourier transforms as P =1− 1 PN e−i2πG(s)/N [66].
|     |     |     |     |     | c   | i=1 |
| --- | --- | --- | --- | --- | --- | --- |
N
ThisisrelevantbecauseGauss’lawisonlyapproximatelyheldformethodssuchasTrotter-Suzuki
simulationsandsotheapplicationofthisconstraintoraclecanbeusedtofilterouttheunphysical
P0
components of simulation error. Specifically, consider a constraint on |ψi ∈ given by the pro-
P
jector P that commutes with the Hamiltonian. In other words, [P , H ] = 0; however there
| c   |     |     |     |     | c   | j j |
| --- | --- | --- | --- | --- | --- | --- |
may exist k0 such that [H ,P ]6=0. This creates problems for the Trotter-Suzuki expansion, but
|     |     | k0 c |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- |
we can address this by transforming into the interaction frame as discussed below
 
| PM  |     | PM  |     |     | Z t X |     |
| --- | --- | --- | --- | --- | ----- | --- |
e −i Hjt |ψi=e −i( Hj+λPc)t |ψi=e−iλPctexp eiλPcs H e−iλPcsds|ψi. (100)
| j=1 |     | j=1 |     |     | τ  | j   |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 0   | j   |
We can then implement the time-ordered operator exponential in (100) using one of our previous
methods, such as a hybridized Trotter-qDRIFT method or that used in the previous section. This
allows us to impose a constraint, such as Gauss’ law, on the integration formula at low cost. By
contrast, if we were to try to do so using a high-order Trotter formula, we would have remainder
terms in the Trotter-Suzuki expansion that are in O(poly(λt)). From Theorem 7.1, this is in
O(poly(kH k2 t2/(cid:15))) and thus cannot be implemented at low cost in the limit where (cid:15)(cid:28)1, unlike
f ∞
| in the interaction | picture | approach. |     |     |     |     |
| ------------------ | ------- | --------- | --- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 33

AsimilarsimpleexampleofthisissolvingtheSchrodingerequationforaparticleconstrainedto
agivensurface. Asanexample,considersolvingtheSchrodingerequationforaparticleconstrained
tobeonthesurfaceofaFigure-8immersionofaKleinbottle,whichisanon-orientablesurfacewith
noboundary. Suchasurfaceisgiven,forsomefixedvalueofr >2,bythefollowingparameterized
surface over the angles θ,v ∈[0,2π)
x=(r+cos(θ/2)sin(v)−sin(θ/2)sin(2v))cos(θ)
y =(r+cos(θ/2)sin(v)−sin(θ/2)sin(2v))sin(θ)
z =sin(θ/2)sin(v)+cos(θ/2)sin(2v), (101)
where in Cartesian coordinates θ = arctan(y/x) and v is found implicitly through the above
expressions. As all these coordinate functions are Lipshitz continuous, a least square solution can
be found using gradient descent after dividing up the surface in (θ,v) coordinates into a finite
number of regions and then performing gradient descent of k~x−~x(r,θ,v)k. Thus by following this
procedure,wecandecidewithin(cid:15)errorwhetheragiven(x,y,z)liesonthesurfaceofKleinbottle.
In turn, P can be constructed by using reversible logic to evaluate this in time O(poly(log(1/(cid:15)))).
c
Thus, complicated quantum dynamics on unusual manifolds can be simulated through the use of
our approach to constraints, even in cases like the figure-8 immersion of the Klein bottle where
no simple coordinate system is available that makes the computation of the Laplacian operator in
(r,v,θ) coordinates trivial. This is because the gradient fails to be defined there, as the normal
vector cannot be defined at the intersection in the figure-8. Instead, we can rely on the constraint
operator to force the dynamics to lie on the surface of the bottle and use the standard Laplacian
in Cartesian coordinates.
As a final point of discussion, let us consider applying these ideas to simulate a universal
Hamiltonian with a quantum circuit. A universal Hamiltonian is a Hamiltonian such that the
groundstate of the Hamiltonian encodes a quantum superposition of the history of a quantum
computer via a clockstate of the form √1 P |ti|ψ(t)i where |ψ(t)i is the state of the quantum
T t
computer after t gates have been applied to it [67, 68, 69, 70]. In order to minimize the locality
neededbytheseconstructions,techniquessuchas“perturbativegadgets”areemployedwhichallow
restricted interactions such as 2-local ones to simulate the action of a Hamiltonian of greater k-
locality. It is tempting therefore to ask whether our techniques could be used to accelerate the
simulation of these constrained Hamiltonians.
As an example, the work of [70] shows that a translationally invariant 1D Hamiltonian of the
following form for parameters T, ∆ is universal
H = X ∆h(3)+T X h(2), (102)
ij i
hi,ji i
whereeachh(3) isatwo-bodytranslationallyinvariantHamiltonianandeachh isatranslationally
ij i
invariant one-body Hamiltonian. At first glance, the latter term appears to be fast forwardable.
Thisissignificant,becausethevalueT correspondstothenumberofgatesemployedinthecircuit.
Thus we would be able to fast forward an arbitrary calculation if this were, by itself, true.
However, the value of ∆ needed to provide a close approximation to the dynamics generically
dominates the remaining term in [70]. In particular if we demand a simulation error on the order
of (cid:15), then it suffices to take ∆ ∈ O(T4/(cid:15)) (for all other simulation parameters fixed). Thus the
translationally invariant 2-body term dominates asymptotically and even if were possible to fast-
forward the simulation of this Hamiltonian, the best case scenario would lead to a method that
hasscalingO(T log(1/(cid:15)))fromtheone-bodyterm. However, thisconstructionisnotself-evidently
fast-forwardable and so a polynomial improvement is expected at best from transitioning to the
interaction frame of the two-body operator.
8 Conclusions
We have developed novel simulation protocols that combine the standard simulation protocols of
Trotterization, continuous qDRIFT, and qubitization in the interaction picture to simulate time-
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 34

independentHamiltonians. Byexploitingtheinteractionpicture, wecanenterintotheinteraction
frame of a fast-forwardable term with large or unbounded norm. Continuous qDRIFT is used
to split the resulting time-ordered exponential into a product of time-independent exponentials
with bounds proven for the number of time steps needed to achieve a desired error (cid:15). In the
case of Hamiltonians with underlying commutator structure, Trotterizing first can reduce the
query complexity further. Qubitization is then used for implementing the final time-independent
exponentials, though other simulation techniques can be used.
ThehybridprotocolusingTrotterizationbeforecontinuousqDRIFTintheinteractionframeof
a fast-forwardable term in the Hamiltonian has a query complexity of O(t2(c + PL kH k2 )/(cid:15)),
I k6=l k ∞
where c depends on the sum of norms of commutators. For Hamiltonian simulation problems
I
with commutator structure, this is a drastic improvement over the complexity O(kH k2 /(cid:15))
k ∞,1,1
obtained from directly employing conventional qDRIFT methods to a linear combination query
model. The qubitization and continuous qDRIFT hybrid I.P. protocol has a query complexity
bounded by O˜(λ t+kH k2 t2/(cid:15)), where the quantities λ and H only involve the terms in the
α α ∞ α α
interaction Hamiltonian. If the term selected for the interaction frame is unbounded or of large
operatornorm,thisagainyieldsanimprovementinthescalingwiththe‘1-normofH comparedto
qubitization. Ourapproach doesnot require a complicatedclock constructioneither, which makes
it more practical than truncated Dyson series methods [21].
DirectapplicationofthesetechniquestotheSchwingerModelyieldalogarithmicscalinginthe
electric field cutoff Λ for the query complexity. For the Hamiltonian model of collective neutrino
√
oscillations, the query complexity is independent of the typically large constant λ = 2G n
f e
representingtheelectrondensity,withthesamescalingwithrespecttootherparameterscompared
to conventional Trotter-Suzuki methods. The scaling with these parameters outperforms those
achieved by current simulation methods.
Further applications of these methods appear in simulating constrained dynamics. We show
that the magnitude of the constraint term in the Hamiltonian needs to be prohibitively large to
applysuchaconstraintusingtraditionalsimulationmethods,suchasqubitization. However,using
our approaches we can simulate the dynamics using a number of gate operations that (for certain
constraints)isindependentofthemagnitudeoftheconstraint. Thisallowsapproximationmethods
similar to Trotter-Suzuki simulations to be employed while guaranteeing that the simulation does
not break important symmetries present in the underlying dynamics (such as Gauss’ law).
Another interesting fact to note is that even when Trotter formulas are used for the entire
simulation, transforming to the interaction picture can have an advantage over performing the
simulation in the laboratory frame. This is because Trotter formulas have costs that scale with
fractionalpowersofthederivativesandleadtocoststhatarelinearinthestrengthoftheinteraction
term,ratherthanasuper-linearfunctionaswouldbeexpectedfromasimulationinthelaboratory
frame[8,10]. AlthoughhybridmethodsthatprovideL1-normscalingareshowntobeadvantageous
in this regard, this advantage can be useful and may lead to improved methods to reduce the cost
of simulation purely within the Trotter-Suzuki formalism wherein the structure of commutators
can be more easily exploited.
These hybrid techniques are primarily useful in contexts where there are not only terms of
large operator norm in a Hamiltonian but when those terms are diagonalizable, one-sparse, or
more generally fast-forwardable. However, situations often arise in quantum simulation where it
might be desirable to enter the interaction frame of terms that are not fast-forwardable, such as
the hopping term H of the Schwinger model in the continuum limit. As a na¨ıve application of
h
the present methods would involve doubling the number of times the non fast-forwardable term
wouldbeneedtobesimulated(seeequation(42)),additionalworkisneededtodevelopinteraction
picture algorithms, hybrid or otherwise, that are more optimized with respect to parameters that
define certain physical regimes of interest.
Acknowledgements
We thank Martin Savage for useful discussions. This work was supported in part by the U.S. De-
partmentofEnergy,OfficeofScience,OfficeofNuclearPhysics,InqubatorforQuantumSimulation
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 35

(IQuS) under Award Number DOE (NP) Award DE-SC0020970. It was further supported by a
grant from Google research award, and NW’s theoretical work on this project was supported by
theU.S.DepartmentofEnergy,OfficeofScience,NationalQuantumInformationScienceResearch
Centers, Co-Design Center for Quantum Advantage under contract number DE-SC0012704.
References
[1] RichardP.Feynman. Simulatingphysicswithcomputers. InternationalJournalofTheoretical
Physics, 21(6):467–488, 1982. ISSN 1572-9575. doi:10.1007/BF02650179.
[2] Seth Lloyd. Universal quantum simulators. Science, 273(5278):1073–1078, 1996.
doi:10.1126/science.273.5278.1073.
[3] Al´an Aspuru-Guzik, Anthony D Dutoi, Peter J Love, and Martin Head-Gordon. Sim-
ulated quantum computation of molecular energies. Science, 309(5741):1704–1707, 2005.
doi:10.1126/science.1113479.
[4] Markus Reiher, Nathan Wiebe, Krysta M Svore, Dave Wecker, and Matthias Troyer. Eluci-
dating reaction mechanisms on quantum computers. Proceedings of the National Academy of
Sciences, 114(29):7555–7560, 2017. doi:10.1073/pnas.1619152114.
[5] Stephen P Jordan, Keith SM Lee, and John Preskill. Quantum algorithms for quantum field
theories. Science, 336(6085):1130–1133, 2012. doi:10.1126/science.1217069.
[6] Alessandro Roggero, Andy C. Y. Li, Joseph Carlson, Rajan Gupta, and Gabriel N. Perdue.
Quantum computing for neutrino-nucleus scattering. Phys. Rev. D, 101:074038, Apr 2020.
doi:10.1103/PhysRevD.101.074038.
[7] Dominic W Berry, Graeme Ahokas, Richard Cleve, and Barry C Sanders. Efficient quantum
algorithmsforsimulatingsparsehamiltonians. Communications in Mathematical Physics,270
(2):359–371, 2007. doi:https://doi.org/10.1007/s00220-006-0150-x.
[8] Nathan Wiebe, Dominic Berry, Peter Høyer, and Barry C Sanders. Higher order decomposi-
tions of ordered operator exponentials. Journal of Physics A: Mathematical and Theoretical,
43(6):065203, 2010. doi:10.1088/1751-8113/43/6/065203.
[9] David Poulin, Angie Qarry, Rolando Somma, and Frank Verstraete. Quantum simulation of
time-dependent hamiltonians and the convenient illusion of hilbert space. Physical Review
Letters, 106(17), Apr 2011. ISSN 1079-7114. doi:10.1103/physrevlett.106.170501.
[10] Andrew M Childs, Yuan Su, Minh C Tran, Nathan Wiebe, and Shuchen Zhu. The-
ory of trotter error with commutator scaling. Physical Review X, 11(1):011020, 2021.
doi:10.1103/PhysRevX.11.011020.
[11] Guang Hao Low and Isaac L. Chuang. Optimal hamiltonian simulation by quantum signal
processing. Phys. Rev. Lett., 118:010501, Jan 2017. doi:10.1103/PhysRevLett.118.010501.
[12] Guang Hao Low and Isaac L. Chuang. Hamiltonian simulation by qubitization. Quantum, 3:
163, Jul 2019. ISSN 2521-327X. doi:10.22331/q-2019-07-12-163.
[13] Andr´as Gily´en, Yuan Su, Guang Hao Low, and Nathan Wiebe. Quantum singular value
transformation and beyond: exponential improvements for quantum matrix arithmetics. In
Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pages
193–204, 2019. doi:10.1145/3313276.3316366.
[14] DominicWBerry,M´ariaKieferov´a,ArturScherer,YuvalRSanders,GuangHaoLow,Nathan
Wiebe, Craig Gidney, and Ryan Babbush. Improved techniques for preparing eigenstates of
fermionic hamiltonians. npj Quantum Information, 4(1):1–7, 2018. doi:10.1038/s41534-018-
0071-5.
[15] David Poulin, Alexei Kitaev, Damian S Steiger, Matthew B Hastings, and Matthias Troyer.
Quantumalgorithmforspectralmeasurementwithalowergatecount. Physicalreviewletters,
121(1):010501, 2018. doi:10.1103/PhysRevLett.121.010501.
[16] John M. Martyn, Zane M. Rossi, Andrew K. Tan, and Isaac L. Chuang. Grand unification of
quantum algorithms. PRX Quantum, 2(4), dec 2021. doi:10.1103/prxquantum.2.040203.
[17] Yulong Dong, Xiang Meng, K Birgitta Whaley, and Lin Lin. Efficient phase-factor
evaluation in quantum signal processing. Physical Review A, 103(4):042419, 2021.
doi:10.1103/PhysRevA.103.042419.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 36

[18] Andrew M Childs and Nathan Wiebe. Hamiltonian simulation using linear combinations
of unitary operations. Quantum Information & Computation, 12(11-12):901–924, 2012.
doi:10.26421/qic12.11-12.
[19] Dominic W Berry, Andrew M Childs, Richard Cleve, Robin Kothari, and Rolando D Somma.
Exponential improvement in precision for simulating sparse hamiltonians. In Proceedings
of the forty-sixth annual ACM symposium on Theory of computing, pages 283–292, 2014.
doi:10.1145/2591796.2591854.
[20] Ma´ria Kieferov´a, Artur Scherer, and Dominic W Berry. Simulating the dynamics of time-
dependent hamiltonians with a truncated dyson series. Physical Review A, 99(4):042314,
2019. doi:10.1103/PhysRevA.99.042314.
[21] GuangHaoLowandNathanWiebe. Hamiltoniansimulationintheinteractionpicture. arXiv
preprint arXiv:1805.00675, 2018. doi:10.48550/ARXIV.1805.00675.
[22] Yuan Su, Dominic W Berry, Nathan Wiebe, Nicholas Rubin, and Ryan Babbush.
Fault-tolerant quantum simulations of chemistry in first quantization. arXiv preprint
arXiv:2105.12767, 2021. URL https://doi.org/10.48550/arXiv.2105.12767.
[23] Earl Campbell. Random compiler for fast hamiltonian simulation. Physical Review Letters,
123(7), Aug 2019. ISSN 1079-7114. doi:10.1103/physrevlett.123.070503. URL http://dx.
doi.org/10.1103/PhysRevLett.123.070503.
[24] Dominic W Berry, Andrew M Childs, Yuan Su, Xin Wang, and Nathan Wiebe.
Time-dependent hamiltonian simulation with l1-norm scaling. Quantum, 4:254, 2020.
doi:10.22331/q-2020-04-20-254.
[25] Ryan Babbush, Craig Gidney, Dominic W. Berry, Nathan Wiebe, Jarrod McClean, Alexan-
dru Paler, Austin Fowler, and Hartmut Neven. Encoding electronic spectra in quantum
circuits with linear t complexity. Physical Review X, 8(4), Oct 2018. ISSN 2160-3308.
doi:10.1103/physrevx.8.041015. URL http://dx.doi.org/10.1103/PhysRevX.8.041015.
[26] Camille Jordan. Essai sur la g´eom´etrie `a n dimensions. Bulletin de la Soci´et´e Math´ematique
de France, 3:103–174, 1875. URL http://eudml.org/doc/85325.
[27] Guang Hao Low, Theodore J. Yoder, and Isaac L. Chuang. Methodology of resonant equian-
gular composite quantum gates. Physical Review X, 6(4), Dec 2016. ISSN 2160-3308.
doi:10.1103/physrevx.6.041067. URL http://dx.doi.org/10.1103/PhysRevX.6.041067.
[28] RuiChao, DaweiDing, AndrasGilyen, CupjinHuang, andMarioSzegedy. Findinganglesfor
quantum signal processing with machine precision. arXiv preprint arXiv:2003.02831, 2020.
URL https://doi.org/10.48550/arXiv.2003.02831.
[29] Jeongwan Haah. Product decomposition of periodic functions in quantum signal processing.
Quantum, 3:190, 2019. doi:10.22331/q-2019-10-07-190.
[30] J.J.SakuraiandJimNapolitano. Modern Quantum Mechanics. CambridgeUniversityPress,
2 edition, 2017. doi:10.1017/9781108499996.
[31] Steven Weinberg. The Quantum Theory of Fields, volume 1. Cambridge University Press,
1995. doi:10.1017/CBO9781139644167.
[32] Michael A. Nielsen and Isaac L. Chuang. Quantum Computation and Quantum Information:
10th Anniversary Edition. Cambridge University Press, USA, 10th edition, 2011. ISBN
1107002176.
[33] Dave Wecker, Matthew B Hastings, Nathan Wiebe, Bryan K Clark, Chetan Nayak, and
MatthiasTroyer.Solvingstronglycorrelatedelectronmodelsonaquantumcomputer.Physical
Review A, 92(6):062318, 2015. doi:10.1103/PhysRevA.92.062318.
[34] Julian Schwinger. Gauge invariance and mass. ii. Phys. Rev., 128:2425–2429, Dec 1962.
doi:10.1103/PhysRev.128.2425.
[35] Sidney Coleman, R Jackiw, and Leonard Susskind. Charge shielding and quark confinement
in the massive schwinger model. Annals of Physics, 93(1):267–275, 1975. ISSN 0003-4916.
doi:https://doi.org/10.1016/0003-4916(75)90212-2.
[36] M.C.Ban˜uls, K.Cichy, J.I.Cirac, andK.Jansen. Themassspectrumoftheschwingermodel
withmatrixproductstates. Journal of High Energy Physics, 2013(11), Nov2013. ISSN1029-
8479. doi:10.1007/jhep11(2013)158. URL http://dx.doi.org/10.1007/JHEP11(2013)158.
[37] T. Pichler, M. Dalmonte, E. Rico, P. Zoller, and S. Montangero. Real-time dynamics
in u(1) lattice gauge theories with tensor networks. Phys. Rev. X, 6:011023, Mar 2016.
doi:10.1103/PhysRevX.6.011023.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 37

[38] P. Hauke, D. Marcos, M. Dalmonte, and P. Zoller. Quantum simulation of a lat-
tice schwinger model in a chain of trapped ions. Phys. Rev. X, 3:041018, Nov 2013.
doi:10.1103/PhysRevX.3.041018.
[39] Esteban A. Martinez, Christine A. Muschik, Philipp Schindler, Daniel Nigg, Alexander Er-
hard, Markus Heyl, Philipp Hauke, Marcello Dalmonte, Thomas Monz, Peter Zoller, and
et al. Real-time dynamics of lattice gauge theories with a few-qubit quantum computer.
Nature, 534(7608):516–519, Jun 2016. ISSN 1476-4687. doi:10.1038/nature18318. URL
http://dx.doi.org/10.1038/nature18318.
[40] N. Klco, E. F. Dumitrescu, A. J. McCaskey, T. D. Morris, R. C. Pooser, M. Sanz,
E. Solano, P. Lougovski, and M. J. Savage. Quantum-classical computation of schwinger
model dynamics using quantum computers. Phys. Rev. A, 98:032331, Sep 2018.
doi:10.1103/PhysRevA.98.032331.
[41] JohnKogutandLeonardSusskind. Hamiltonianformulationofwilson’slatticegaugetheories.
Phys. Rev. D, 11:395–408, Jan 1975. doi:10.1103/PhysRevD.11.395.
[42] T. Banks, Leonard Susskind, and John Kogut. Strong-coupling calculations of lattice
gauge theories: (1 + 1)-dimensional exercises. Phys. Rev. D, 13:1043–1053, Feb 1976.
doi:10.1103/PhysRevD.13.1043.
[43] Yuval R. Sanders, Dominic W. Berry, Pedro C.S. Costa, Louis W. Tessler, Nathan Wiebe,
Craig Gidney, Hartmut Neven, and Ryan Babbush. Compilation of fault-tolerant quan-
tum heuristics for combinatorial optimization. PRX Quantum, 1(2), Nov 2020. ISSN 2691-
3399. doi:10.1103/prxquantum.1.020312. URL http://dx.doi.org/10.1103/PRXQuantum.
1.020312.
[44] Yong He, Mingxing Luo, E. Zhang, Hong-Ke Wang, and Xiao-Feng Wang. Decompositions
of n-qubit toffoli gates with linear circuit complexity. International Journal of Theoretical
Physics, 56, 07 2017. doi:10.1007/s10773-017-3389-4.
[45] Johannes Bausch. Fast black-box quantum state preparation, 2020. URL https://arxiv.
org/abs/2009.10709.
[46] Cody Jones. Low-overhead constructions for the fault-tolerant toffoli gate. Physical Review
A, 87(2):022328, 2013. doi:10.1103/PhysRevA.87.022328.
[47] Steven A Cuccaro, Thomas G Draper, Samuel A Kutin, and David Petrie Moulton. A new
quantum ripple-carry addition circuit. arXiv preprint quant-ph/0410184, 2004. URL https:
//doi.org/10.48550/arXiv.quant-ph/0410184.
[48] Alexander F. Shaw, Pavel Lougovski, Jesse R. Stryker, and Nathan Wiebe. Quan-
tum algorithms for simulating the lattice schwinger model. Quantum, 4:306, Aug 2020.
ISSN 2521-327X. doi:10.22331/q-2020-08-10-306. URL http://dx.doi.org/10.22331/
q-2020-08-10-306.
[49] James Pantaleone. Neutrino oscillations at high densities. Physics Letters B, 287(1):128 –
132, 1992. ISSN 0370-2693. doi:https://doi.org/10.1016/0370-2693(92)91887-F.
[50] Huaiyu Duan, George M. Fuller, J. Carlson, and Yong-Zhong Qian. Coherent development
of neutrino flavor in the supernova environment. Phys. Rev. Lett., 97:241101, Dec 2006.
doi:10.1103/PhysRevLett.97.241101.
[51] Huaiyu Duan, George M. Fuller, and Yong-Zhong Qian. Collective neutrino os-
cillations. Annual Review of Nuclear and Particle Science, 60(1):569–594, 2010.
doi:10.1146/annurev.nucl.012809.104524. URL https://doi.org/10.1146/annurev.nucl.
012809.104524.
[52] Sovan Chakraborty, Rasmus Hansen, Ignacio Izaguirre, and Georg Raffelt. Collective neu-
trino flavor conversion: Recent developments. Nuclear Physics B, 908:366 – 381, 2016. ISSN
0550-3213. doi:https://doi.org/10.1016/j.nuclphysb.2016.02.012. Neutrino Oscillations: Cele-
brating the Nobel Prize in Physics 2015.
[53] Ermal Rrapaj. Exact solution of multiangle quantum many-body collective neutrino-flavor
oscillations. Phys. Rev. C, 101:065805, Jun 2020. doi:10.1103/PhysRevC.101.065805.
[54] MichaelJ.Cervia,AmolV.Patwardhan,A.B.Balantekin,S.N.Coppersmith,andCalvinW.
Johnson. Entanglement and collective flavor oscillations in a dense neutrino gas. Phys. Rev.
D, 100:083001, Oct 2019. doi:10.1103/PhysRevD.100.083001.
[55] Alessandro Roggero. Entanglement and many-body effects in collective neutrino oscillations.
Phys. Rev. D, 104:103016, Nov 2021. doi:10.1103/PhysRevD.104.103016.
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 38

[56] AlessandroRoggero. Dynamicalphasetransitionsinmodelsofcollectiveneutrinooscillations.
| Phys. | Rev. D, 104:123023, | Dec 2021. doi:10.1103/PhysRevD.104.123023. |     |     |
| ----- | ------------------- | ------------------------------------------ | --- | --- |
[57] Benjamin Hall, Alessandro Roggero, Alessandro Baroni, and Joseph Carlson. Simulation of
collective neutrino oscillations on a quantum computer. Phys. Rev. D, 104:063009, Sep 2021.
doi:10.1103/PhysRevD.104.063009.
[58] Ku¨bra Yeter-Aydeniz, Shikha Bangar, George Siopsis, and Raphael C. Pooser. Collective
neutrino oscillations on a quantum computer. Quantum Information Processing, 2021. URL
https://doi.org/10.1007/s11128-021-03348-x.
[59] Y.Pehlivan,A.B.Balantekin,ToshitakaKajino,andTakashiYoshida. Invariantsofcollective
neutrino oscillations. Phys. Rev. D, 84:065008, Sep 2011. doi:10.1103/PhysRevD.84.065008.
[60] Ian D. Kivlichan, Jarrod McClean, Nathan Wiebe, Craig Gidney, Al´an Aspuru-Guzik,
Garnet Kin-Lic Chan, and Ryan Babbush. Quantum simulation of electronic struc-
ture with linear depth and connectivity. Phys. Rev. Lett., 120:110501, Mar 2018.
doi:10.1103/PhysRevLett.120.110501.
[61] Roberto Oliveira and Barbara M. Terhal. The complexity of quantum spin systems on a
two-dimensional square lattice, 2005. URL https://doi.org/10.48550/ARXIV.QUANT-PH/
0504050.
[62] Yudong Cao and Sabre Kais. Efficient optimization of perturbative gadgets, 2017. URL
https://doi.org/10.48550/arXiv.1709.02705.
[63] Roger A Horn and Charles R Johnson. Matrix analysis. Cambridge university press, 2012.
[64] Francisco Barahona. On the computational complexity of ising spin glass models. Journal of
Physics A: Mathematical and General, 15(10):3241, 1982. doi:10.1088/0305-4470/15/10/028.
[65] Andrew M Childs, Richard Cleve, Enrico Deotto, Edward Farhi, Sam Gutmann, and
Daniel A Spielman. Exponential algorithmic speedup by a quantum walk. In Proceed-
ings of the thirty-fifth annual ACM symposium on Theory of computing, pages 59–68, 2003.
doi:10.1145/780542.780552.
[66] Jesse R Stryker. Oracles for gauss’s law on digital quantum computers. Physical Review A,
| 99(4):042301, | 2019. doi:10.1103/PhysRevA.99.042301. |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- |
[67] Julia Kempe and Oded Regev. 3-local hamiltonian is qma-complete. arXiv preprint quant-
ph/0302079, 2003. URL https://doi.org/10.48550/arXiv.quant-ph/0302079.
[68] Dorit Aharonov, Wim Van Dam, Julia Kempe, Zeph Landau, Seth Lloyd, and Oded Regev.
Adiabatic quantum computation is equivalent to standard quantum computation. SIAM
| review, | 50(4):755–787, | 2008. doi:10.1137/080734479. |     |     |
| ------- | -------------- | ---------------------------- | --- | --- |
[69] Tobias J Osborne. Hamiltonian complexity. Reports on progress in physics, 75(2):022001,
| 2012. | doi:10.1088/0034-4885/75/2/022001. |     |     |     |
| ----- | ---------------------------------- | --- | --- | --- |
[70] Tamara Kohler, Stephen Piddock, Johannes Bausch, and Toby Cubitt. Translationally in-
variant universal quantum hamiltonians in 1d. In Annales Henri Poincar´e, volume 23, pages
| 223–254.  | Springer, 2022. | doi:10.1007/s00023-021-01111-7. |     |     |
| --------- | --------------- | ------------------------------- | --- | --- |
| A Diamond | Norm            |                                 |     |     |
The diamond distance is often used as a measure of error between two quantum channels. It is
| defined as | follows: |     |     |     |
| ---------- | -------- | --- | --- | --- |
(E,N)= 1 ||E−N||
|               |                | d       | ,         | (103) |
| ------------- | -------------- | ------- | --------- | ----- |
|               |                | (cid:5) | 2 (cid:5) |       |
| where ||...|| | is the diamond | norm    |           |       |
(cid:5)
|     |     | ||P|| :=sup        | ||(P⊗I)(ρ)|| | (104) |
| --- | --- | ------------------ | ------------ | ----- |
|     |     | (cid:5) ρ;||ρ||1=1 | 1            |       |
and E and N are two quantum channels or superoperators. Note that I acts on the same size
P
Hilbert space as and ρ is a density matrix. All operators here are expressed as square matrices
and ρ can represent states entangled with qubits that are not operated on. We then need an
identity matrix to “pad out” the missing dimensions so that P⊗I can act sensibly upon ρ.
The diamond norm is simply the trace distance but maximized over all possible input states
| and satisfies | two key properties: |     |     |     |
| ------------- | ------------------- | --- | --- | --- |
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 39

| (1) Triangle              | inequality: |     | ||A+B|| |         | ≤||A|| | +||B||          |         |     |     |     |     |     |
| ------------------------- | ----------- | --- | ------- | ------- | ------ | --------------- | ------- | --- | --- | --- | --- | --- |
|                           |             |     |         | (cid:5) |        | (cid:5)         | (cid:5) |     |     |     |     |     |
| (2) Sub-multiplicativity: |             |     | ||AB||  | ≤||A||  |        | ||B||           |         |     |     |     |     |     |
|                           |             |     |         | (cid:5) |        | (cid:5) (cid:5) |         |     |     |     |     |     |
It follows from the definition of the diamond norm that if we apply the channel E and N to the
| quantum | state | σ, we | have |     |     |     |     |     |     |     |     |     |
| ------- | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |      | (E(σ),N(σ))= |     | ||E(σ)−N(σ)|| |     |     | (E,N).     |     |     |       |
| --- | --- | --- | ---- | ------------ | --- | ------------- | --- | --- | ---------- | --- | --- | ----- |
|     |     |     | d tr |              |     |               |     | 1   | ≤d (cid:5) |     |     | (105) |
2
The trace norm distance is important since it bounds the error in expectation values. To see
this, consider the expression |Tr(ME(σ))−Tr(MN(σ))|. The expectation value of an operator M
withrespecttoastateρcanbefoundbytakingthetraceoftheirproduct,i.eTr(Mρ). Thus,inthe
above expression, we first send a state σ through our two channels. Then we find the expectation
value of M with respect to their outputs and take the absolute value of the difference to find the
| error in | expectation                                      |      | values. |                |     |        |     |               |              |     |             |     |
| -------- | ------------------------------------------------ | ---- | ------- | -------------- | --- | ------ | --- | ------------- | ------------ | --- | ----------- | --- |
| We       | can bound                                        | this | error   | in expectation |     | values | by  | the following | inequalities |     |             |     |
|          | |Tr(ME(σ))−Tr(MN(σ))|=|Tr[M(E(σ)−N(σ))]|≤2||M||d |      |         |                |     |        |     |               |              |     | (E(σ),N(σ)) |     |
tr
(E,N).
|     |     |     |     |     | ≤2||M||d |     |     |     |     |     |     | (106) |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | ----- |
(cid:5)
| In the | first | inequality, | the | von-Neumann |     | trace | inequality |     |     |     |     |     |
| ------ | ----- | ----------- | --- | ----------- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
n
X
|     |     |     |     |     | |Tr(AB)|≤ |     |     | α β |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
i i
i=1
wasusedwhereα i ,β i arethesingularvaluesoftheoperatorsAandB respectively. Thisinequality
can be further bounded by recognizing that α ≤α for all i, where α is the largest singular
|          |        |         |          |       |     | i              | max |       |     | max |     |     |
| -------- | ------ | ------- | -------- | ----- | --- | -------------- | --- | ----- | --- | --- | --- | --- |
| value of | A. The | largest | singular | value | of  | A is precisely |     | ||A|| | so  |     |     |     |
∞
|     |     |     |           |     | n   |     | n   |          |     |         |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | -------- | --- | ------- | --- | --- |
|     |     |     |           |     | X   |     | X   |          |     |         |     |     |
|     |     |     | |Tr(AB)|≤ |     | α   | β ≤ | α   | β =||A|| |     | ||B|| . |     |     |
|     |     |     |           |     |     | i i | max | i        | ∞   | 1       |     |     |
|     |     |     |           |     | i=1 |     | i=1 |          |     |         |     |     |
Thesecondinequalityintheaboveexpressionfollowsdirectlyfromthedefinitionofthediamond
norm.
P†P
Now note that if we have a projection operator P, = P since projection operators are
Hermitian and square to themselves. Their eigenvalues are 1 and 0 so it immediately follows that
||P|| =1. So if M is a projection operator and we have ε error in the diamond distance, then
∞
|Tr(ME(σ))−Tr(MN(σ))|≤2ε.
This justifies the statement that measurement statistics are correct up to a factor of 2ε with
| an ε error | in diamond |     | distance. |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B Notation |            | for | qDRIFT    |     |     |     |     |     |     |     |     |     |
We establish the following notational conventions from [24] for describing the time-dependent
α∈CL
qDRIFT scaling. Let be a vector. The notation ||α|| represents the l norm of α and we
|          |           |     |          |     |     |     |     |     | p   |     | p   |     |
| -------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| define a | few cases | as  | follows: |     |     |     |     |     |     |     |     |     |
v
u
|     |     |         | L     |      |         | L   |          |       |      |               |         |     |
| --- | --- | ------- | ----- | ---- | ------- | --- | -------- | ----- | ---- | ------------- | ------- | --- |
|     |     |         | X     |      |         | uX  |          |       |      |               |         |     |
|     |     | ||α|| 1 | := |α | j |, | ||α|| 2 | :=t | |α j |2, | ||α|| | ∞ := | max           | |α j |. |     |
|     |     |         | j=1   |      |         | j=1 |          |       |      | j∈{1,2,...,L} |         |     |
If A is a matrix, ||A|| denotes the Schatten-p norm of A. A few important examples are:
p
|     |       |       | √   |       |       | q   |          |     |                     |     |     |     |
| --- | ----- | ----- | --- | ----- | ----- | --- | -------- | --- | ------------------- | --- | --- | --- |
|     | ||A|| | :=Tr( |     | A†A), | ||A|| | :=  | Tr(A†A), |     | ||A|| :=max||A|ψi|| |     | .   |     |
|     |       | 1     |     |       |       | 2   |          |     | ∞                   |     | 2   |     |
|ψi
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 40

If f :[0,t]→C is a continuous function, ||f|| denotes the Lp norm of the function. Thus,
p
s
|     |       | Z t |           |       |     | Z t |            |       |         |         |
| --- | ----- | --- | --------- | ----- | --- | --- | ---------- | ----- | ------- | ------- |
|     | ||f|| | :=  | dτ|f(τ)|, | ||f|| | :=  |     | dτ|f(τ)|2, | ||f|| | := max  | |f(τ)|. |
|     | 1     |     |           |       | 2   |     |            | ∞     |         |         |
|     |       | 0   |           |       |     | 0   |            |       | τ∈[0,t] |         |
These norms can be combined to obtain vector and operator-valued functions. Suppose α :
CL
[0,t] → is a continuous vector-valued function with components at time τ denoted by α (τ).
j
||α|| denotes taking the l norm ||α(τ)|| for all τ and computing the Lq norm of the resulting
| p,q              |      |     | p   |     | p   |     |     |     |     |     |
| ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scalar function, | e.g. |     |     |     |     |     |     |     |     |     |
|                  |      |     |     |     |     | Z t | L   |     |     |     |
X
|     |     |     |     | ||α|| |     | =   | dτ |α | |.  |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     |       | 1,1 |     |       | j   |     |     |
0
j=1
SimilarreasoningapplieswhendealingwiththeSchattenp-normofatime-dependentoperator
and then applying an Lq norm to the resulting scalar function, i.e. ||A|| . For example,
p,q
s
|     |     |     |     |       |     | Z t | √       |         |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ------- | ------- | --- | --- |
|     |     |     |     |       |     |     | (cid:0) | (cid:1) |     |     |
|     |     |     |     | ||A|| | =   | dτ  | (Tr A†A | )2 .    |     |     |
1,2
0
Note that this notation, while compact, is not well suited for describing evolution within a sub-
interval of the entire evolution. In the event that a shorter evolution needs to be described, we
| explicitly | use the | integral | expression | over | the | domain | in question. |     |     |     |
| ---------- | ------- | -------- | ---------- | ---- | --- | ------ | ------------ | --- | --- | --- |
PL
For time-dependent linear combinations A(τ)= A l (τ), the notation ||A|| p,q,r means tak-
l=1
ing the Schatten p-norm ||A (τ)|| of each term in the sum and applying the l and Lr norms to
|               |               |     | t          | p   |      |     |     |     |     | q   |
| ------------- | ------------- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
| the resulting | vector-valued |     | functions, |     | e.g. |     |     |     |     |     |
|               |               |     |            |     |      |     | X L |     |     |     |
:=
|     |     |     |     | kAk 1,1,∞ |     | max | kA l | (τ)k 1 . |     |     |
| --- | --- | --- | --- | --------- | --- | --- | ---- | -------- | --- | --- |
τ∈[0,t]
l=1
AcceptedinQuantum2022-07-22,clicktitletoverify. PublishedunderCC-BY4.0. 41