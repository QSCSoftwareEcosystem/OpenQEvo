Compilation by stochastic Hamiltonian sparsification
Yingkai Ouyang1, David R. White1, and Earl T. Campbell1,2
1DepartmentofPhysicsandAstronomy,UniversityofSheffield,Sheffield,UK
2Riverlane,Cambridge,UK
Simulation of quantum chemistry is ex- plex systems classically intractable. Using quantum
pected to be a principal application of quan- mechanicstosimulatequantumsystems[25]willpro-
tum computing. In quantum simulation, a vide unprecedented detail in the solution to chemical
complicated Hamiltonian describing the dy- problems, enabling us to better understand the dy-
namics of a quantum system is decomposed namics of highly entangled systems, predicting their
into its constituent terms, where the effect of properties and chemical reactions [1, 17]. For exam-
each term during time-evolution is individu- ple,simulationcanbeusedinphaseestimationtoex-
ally computed. For many physical systems, tracttheeigenspectrumofaHamiltonian[22,33,44],
the Hamiltonian has a large number of terms, and by sufficiently understanding its energy spectra
constraining the scalability of established sim- wecanaccuratelypredictchemicalreactionrates[23].
ulation methods. To address this limitation Given a Hamiltonian H expressed as the sum
we introduce a new scheme that approximates of multi-qubit Pauli matrices, solution of the
the actual Hamiltonian with a sparser Hamil- Schrödinger equation requires the calculation of its
tonian containing fewer terms. By stochas- exponentiation. Quantum simulation techniques are
tically sparsifying weaker Hamiltonian terms, distinguished by the way they map the chemical
we benefit from a quadratic suppression of er- Hamiltonian to an effective Hamiltonian on qubits
rors relative to deterministic approaches. Re- [3, 4, 20, 31, 36], and subsequent mapping of the ex-
lying on optimality conditions from convex op- ponentiation of this effective Hamiltonian to a com-
timisation theory, we derive an appropriate putation. One well-established method is to apply
probability distribution for the weaker Hamil- the Trotter-Suzuki formula [38–40] to reduce this
tonian terms, and compare its error bounds larger exponentiation to a product of Pauli exponen-
with other probability ansatzes for some elec- tials. Each Pauli exponential can then be interpreted
tronic structure Hamiltonians. Tuning the as a single quantum gate. To date, many variants
sparsity of our approximate Hamiltonians al- of Trotter-Suzuki methods have been studied in the
lowsourschemetointerpolatebetweentwore- context of quantum simulation of chemical systems
cent random compilers: qDRIFT and random- [2, 21, 37].
ized first order Trotter. Our scheme is thus an Trotterisationisanattractiveapproachtoquantum
algorithm that combines the strengths of ran- simulation because of its simplicity. However, a sig-
domised Trotterisation with the efficiency of nificant limitation of Trotterisation is that the num-
qDRIFT, and for intermediate gate budgets, berofquantumgatesrequiredscaleslinearlywiththe
outperforms both of these prior methods. numberoftermsintheHamiltonian,whichmaygrow
very large [42, 44]. Campbell [12] observed the prob-
lematic scaling of the Trotter-Suzuki decomposition
1 Introduction
and introduces qDRIFT, a stochastic approach that
samples terms from the Hamiltonian, trading accu-
Chemistrysimulationisexpectedtobeaprincipalap-
racy for computational cost; importantly, qDRIFT
plication of quantum computing, revealing the prop-
scales independently of the number of terms. We
erties of chemical bonds and interactions by simulat-
build on Campbell’s approach, introducing an algo-
ing classically intractable systems, with applications
rithm that combines the strengths of standard Trot-
in pharmaceuticals, material science, and industrial
terisation with the efficiency of qDRIFT.
chemical manufacture [1, 29]. For example, efficient
OurapproachapproximatesthetargetHamiltonian
simulation of the chemical cluster FeMoCo [5, 9, 35]
via sparsification, yielding a Hamiltonian with fewer
may allow more efficient nitrogen fixation, improving
terms; the Trotterised computation then requires far
the manufacture of fertilizers. The difficulty of di-
fewer gates per Trotter step. Although sparsification
rectly solving the Schrödinger equation of chemically
introduces a new approximation error, the reduction
interesting problems renders even moderately com-
in gate count means we can apply more Trotter steps
YingkaiOuyang: y.ouyang@sheffield.ac.uk within a fixed budget. Our key insight is that spar-
DavidR.White: d.r.white@sheffield.ac.uk sification can be performed stochastically instead of
EarlT.Campbell: earltcampbell@gmail.com
deterministically,andthatthisleadstoimprovedper-
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 1
0202
beF
62
]hp-tnauq[
2v55260.0191:viXra

formance. By defining our approximate Hamiltonian siderable advantage over Trotterisation methods, and
to be a random variable with an expectation value itislikelythatthisadvantagepersistsoverSparSto.
equal to the actual Hamiltonian, we benefit from a However, the value of this work is two-fold. Firstly,
quadratic suppression of errors relative to determin- we improve the best known Trotter methods. Sec-
istic methods; this behaviour is also seen in other ondly, we have demonstrated the value of randomly
stochastic compilers [11, 12, 15, 16]. We refer to our sparsifying Hamiltonians as a technique that might
combination of first order Trotterisation and stochas- later be incorporated into post-Trotter methods. In-
tically sparsified Hamiltonians as SparSto. deed, Berry’s perspective article [6] also highlighted
In many systems, including electronic structure that potential application of randomization to post-
Hamiltonians, we empirically observe power-law dis- Trotterprotocolsisapromisingfutureresearchdirec-
tributions of term strengths, which is promising for tion.
sparsification since weaker terms are clear candidates
for truncation. In a stochastic compiler, it is nat- 2 Trotterisation
ural to relate the probability of a term being trun-
cated from the Hamiltonian with the magnitude of
Consider a time-independent Hamiltonian that ad-
its strength. One of our main technical results is a
mits a decomposition H =
PL
h P . While P can
rigorousupperboundontheerrorof SparStoforan j=1 j j j
often be considered to be multi-qubit Pauli matrices,
arbitraryprobabilitydistributionwherethetermsare
we make no such assumption, and for us P are ma-
j
sampled independently.
trices with singular value at most 1. Without loss
Toobtainthebestpossibleupper-boundweneedto of generality, the corresponding coefficients h can
j
select the best probability distribution. In our anal- then be positive. Solving the Schrödinger equation
ysis, we place the most important terms, with the |ψ(t)i = e−iHt|ψ(0)i allows us to model the contin-
largest strengths, inside an active set so that they uous evolution of the state |ψ(t)i over time. Over a
always appear in the sparsified Hamiltonian. Ran- shorttimeperiods, thefirstorderTrotter-Suzukide-
dom sparsification is instead applied only to a tail compositionapproximatestheexponentiale−iHt with
of weaker Hamiltonian terms that we label the inac- a product of exponentials given by [38]
tive set. We rely on optimality conditions in convex
optimisation theory in order to derive a probability Y L
e−isHj =e−isH +O(s2), (1)
distribution over the inactive set, which we call the
“linear ansatz”. We numerically optimise and anal- j=1
yse the performance of our error bounds for some where H = h P . We call this the “vanilla Trotteri-
j j j
electronic structure Hamiltonians. For low gate bud- sation” scheme,astherearemanyvariantstothisap-
gets SparSto behaves similarly to qDRIFT, and for proach[14,15,39,40],includingonesthatproposeto
larger gate budgets it exactly reproduces randomized deterministicallycoalesceHamiltonianterms[34,43].
first order Trotter; as such it interpolates between We assume that each e−isHj, which we call a gate,
these approaches. However, for intermediate gate can be efficiently implemented on a target quantum
budgets, which coincide with parameter regimes of computer. To simulate e−itH, we approximate e−isH
practical interest, our new sparsification method out- repeatedly r times, such that t = rs. The number
performs both methods by around an order of mag- of gates G required by a simulation is thus the prin-
nitude. We emphasize numerical optimisation is al- cipal measure of its computational cost. Since each
ways performed at the level of upper bounds and not Trotterisationofe−isH involvesLgates, vanillaTrot-
by considering empirical performance of small simu- terisationrequiresG=rLgates, andcanbecomepo-
latable systems. Though SparSto uses first order tentially computationally expensive when L is large.
Trotter, sparsification of Hamiltonians could also be In particular, it is known that an effective Hamilto-
naturallycombinedwithhigherorderTrotterschemes nianfortheelectronicstructureproblemforasystem
to yield higher order randomized compilers. with N modes typically has L=O(N4) terms [1].
When comparing with other Trotter methods we The vanilla Trotterisation scheme approximates
can just count the number of gates of the form e−itH with a simulation error that is at most (cid:15) (cid:46)
van
e−isHj that are unitaries generated by easily acces- λ2t2/2r = Lλ2t2/2G [38], where λ = khk
1
, h =
sible Hamiltonians H . However, to fairly compare (h ,...,h ). In contrast to Trotterisation, the
j 1 L
against post-Trotter methods [7, 9, 13, 26, 27], we qDRIFT method introduced by Campbell has a com-
would also need to assess the resource cost of ex- putationalcostthatisindependentofL;itsgatecount
tra ancilla and select and prepare gadgets that are isO(λ2t2/(cid:15)). qDRIFTsimulatesanidealunitarypro-
notbuiltusinge−isHj. Thismakesdirectcomparison cessbyaMarkovianevolution,samplingasequenceof
with post-Trotter methods an involved task and sen- Pauli gates from a predetermined distribution; each
sitivetothecostmodel. However,post-Trottermeth- exponentiation in the resulting circuit is given the
ods have better asymptotic scaling and for problems same weight τ such that the distribution alone deter-
of interest they have often been found to have a con- minestheoutcomeofthecalculation. Theprobability
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 2

p
j
ofchoosingagiveneiτHj asthenextgateinacom- by T
s,→
= QL
j=1
esLj. Given no a priori reason
putationisweightedbythecorrespondinginteraction to simulate L in any particular order, it is natural
j
strength: p =h /λ,ensuringthatthestochasticpro- to consider permutations of this operator sequence.
j j
cessofrepeatedsamplingdriftsstochasticallytowards A second order approximation of the Taylor expan-
the target unitary. The number of gates is set at a sion can be made by mixing the above Trotterisation
fixed computational budget G representing the num- T
s,→
with T
s,←
= Q1
j=L
esLj, where the arrows de-
ber of primitive gates, and gives approximation error note the ordering over the term index j. The uni-
(cid:15)(cid:46)4λ2t2/G 1. formly mixed operation 1(T + T ), which is a
2 s,→ s,←
Whilst Trotter-Suzuki decompositions have worse randomised first order Trotterisation scheme that we
computational complexity than qDRIFT in the num- denote as R1oTrott, approximates esL with error
ber of terms, their computational cost scales better that is third order in sL [15, Theorem 1]. More gen-
with respect to t and (cid:15). To exploit this trade-off, we erally,Trotterisationcanbefurtherimprovedbycom-
introduce a new approach SparSto, which interpo- pletely randomising the order in which the gates are
lates between qDRIFT and the higher-order Trotter- performed [15, 42]. To approximate etL for a fixed
Suzuki decompositions whilst also building and im- time t, we approximate esL for a total of r times,
proving on the analysis of randomised simulation in where s=t/r. By taking the number of repeats r to
Ref. [15]. belarge,thesimulationtimescanbecomesmall,and
Like qDRIFT, SparSto approximates a unitary (1) holds to a good approximation.
evolutionwithaprobabilisticensembleofunitaryevo- In SparSto, we stochastically sparsify the Hamil-
lutions instead of direct Trotterisation — although tonian using some term-wise independent probability
higher-order Trotterisation can subsequently be ap- distribution and then apply one step of randomized
plied. Thisstochasticschemeisinthespiritofrelated first order Trotter. For each of the r Trotter steps a
work [8, 14, 15] and its merits lie in the ability to use freshstochasticHamiltonianissampled. Therandom
mixtures of unitary operators to approximate a uni- Hamiltonian Hˆ induces a random Liouville operator
tary operator [11, 16]; intuitively stochastic methods Lˆ in the natural way Lˆ(ρ) = i(Hˆρ−ρHˆ). Similarly,
avoid systematic noise. we have random terms Lˆ such that
j
(
L /p with probability p
3 SparSto Analysis Lˆ j = j j j (2)
0 with probability 1−p
j
SparSto uses a random Hamiltonian Hˆ and crucial Here, Lˆ approximates the ideal Liouville operator
j
to our analysis is that the expectation value is equal L in the sense that E(Lˆ ) = L . Given a sampled
to the system Hamiltonian E(Hˆ) = H. To reduce Hˆ j or Lˆ, we also randomiz j e the o j rder of the gates in
gate counts, we would like Hˆ to have far fewer terms
each Trotter step and so introduce the randomized
than H and to be a good approximation, or at least
operators of forward and reverse Trotter steps
to do this with high probability. Rather than consid-
ering arbitrary probability distributions we consider L
the term-wise independent sampling where Hˆ con- Tˆ = Y esLˆ j (3)
s,→
tains the term h j P j /p j with probability p j and with j=1
p E r ( o Hˆ b ) ab = ili H ty a 1 n − d p th j a t t hi t s he te e r x m pe is ct d e r d op n p u e m d b . e T r h o i f s t e e n rm su s re is s Tˆ s,← = Y 1 esLˆ j. (4)
µ= PL p . j=L
j=1 j
Next, we review Lindblad’s formalism of unitary A single step of SparSto is then described by
maps [24], where such maps are generated by expo-
nentiating Liouville operators. We let L j = h j P j Eˆ = 1(cid:16) Tˆ +Tˆ (cid:17) (5)
so that P is a Liouville operator that maps ρ to s 2 s,→ s,←
j
−i(P ρ − ρP ). Clearly then, L (ρ) = −i(H ρ −
j j j j which has µ gates on average. To approximate etL,
ρH ). For any positive number s, Liouville oper-
j SparStosimulatesEˆ independentlyandsequentially
ators generate unitary evolutions in the sense that s
r times. By fixing the expected number of gates G of
esLj(ρ) = e−iHjsρeiHjs. The ideal evolution opera-
SparStotobeconstant,werequireinthefirstbG/µc
tor can be written in terms of the Liouville opera-
tor L = PL L , because esL(ρ) = e−iHsρeiHs. Us- repeats to have s = µt/G and in the final repeat to
j=1 j have s = t − bG/µc. The total number of repeats
ing a vanilla Trotterisation analogous to that given
is then r = dG/µe. We do not consider completely
in (1), a first order approximation of esL is given
randomising the gate orders in Eˆ because it renders
s
our subsequent analysis overly complicated.
1In[12],thesimulationerrorusedisthediamonddistance,
We quantify the maximum error of SparSto us-
whichdiffersfromthediamondnormofthedifferenceofchan-
nels by a factor of 2. This explains why the bound in [12] is ing the diamond norm [19], which when evaluated on
approximatelyatmost2λ2t2/Ginsteadof4λ2t2/G the difference between quantum channels, quantifies
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 3

their distinguishability. For us, we quantify the dis- We upper bound the difference between tails of Eˆ
s
tinguishability between the average of r repeats of Eˆ and esL, which are O(t4µ3/G3) terms, by essentially
s
and the ideal channel etL with the error using the fundamental theorem of calculus to bound
the tail of a power series from its derivatives. From
kE(Eˆr)−etLk , (6)
s (cid:5) this, weevaluateupperboundsonthediamondnorm
of P sj(E(Aˆ )−B ), and call this our tail bound.
where k·k denotes the diamond norm. j≥4 j j
(cid:5) Toapplythefundamentaltheoremofcalculus,wefirst
OurmainresultisananalyticupperboundonkEˆ−
s take the fourth derivatives of Eˆ and esθL with re-
esLk thatwedenoteas(cid:15),whichisexpressedinterms sθ
(cid:5) specttoθ,evaluateupperboundsonthenormoftheir
of the 1-norm k·k .
1 difference over the unit interval for θ. Second, we in-
Theorem 1. Using SparSto with vector of proba- tegrate this upper bound over an appropriate region,
bilities p=(p ,...,p ), vector of Hamiltonian coeffi- which gives a rescaling factor of 1/4!. Also, by ob-
1 L
cients h = (h 1 ,...,h L ), L ≥ 3, and expected number taining polynomials in the diamond norms of L j and
of gates G, the error of simulating etL with SparSto subsequently using the inequality kL j k (cid:5) ≤2h j , along
is at most (cid:15) where with the triangle inequality on the diamond norm of
the difference between the ideal channel and the ap-
2t2µ 4t3µ2 (cid:18) t4µ3(cid:19)
(cid:15)= kuk + K+O , proximate channel, we can obtain a closed form ex-
G 1 3G2 G3
pression for the tail bounds which we show explicitly
with K = (cid:0) kvk +λkwk +4λ3/3 (cid:1) , λ = khk and in Theorem 5 of Appendix A.
1 1 1
It is important to point out that the upper bound
µ=kpk . Moreover, u,v and w are vectors given by
1
on the simulation error in Theorem 1 depends very
u= (cid:18)(cid:18) 1 −1 (cid:19) h2,..., (cid:18) 1 −1 (cid:19) h2 (cid:19) , much on the choice of the probabilities p 1 ,...,p L .
p 1 1 p L L Eachp j signifiestheprobabilitythattheHamiltonian
(cid:18)(cid:18) 1 (cid:19) (cid:18) 1 (cid:19) (cid:19) term H j contributes to the Trotterisation at each it-
v= −1 h3,..., −1 h3 , eration. The smaller the value of µ = p +···+p ,
p2 1 p2 L 1 L
1 L thesparserourHamiltoniansimulationis. Intuitively,
(cid:18)(cid:18) (cid:19) (cid:18) (cid:19) (cid:19)
w= 3 −1 h2,..., 3 −1 h2 . different choices on the values of the probabilities p j
p
1
1 p
L
L inTheorem1affecttheoverallsimulationerrorofetL.
Whenallprobabilitiesareequaltoone, SparStobe-
Atighterboundwithfulldetailsonthehigherorder
comesidenticaltoR1oTrott. Thesimulationerror,
terms in (cid:15) is supplied in Theorem 5 of Appendix A.
can thereby be obtained as the following corollary of
ToboundthediamonddistancebetweenE(Eˆr)and
s Theorem 1.
etL, we bound the diamond distance between E(Eˆ)
s
andesL. Usingthetriangleinequalityonatelescoping
Corollary 2. When p = ··· = p = 1, the simula-
1 L
sum, the unit diamond norm of all channels, and the
tion error is at most
independence of each random unitary Eˆ, we get the
s
bound  
8t3L2 X L 2λ3 (cid:18) t4L3(cid:19)
(cid:13)
(cid:13)E(Eˆ)r−etL
(cid:13)
(cid:13) ≤r
(cid:13)
(cid:13)E(Eˆ)−esL
(cid:13)
(cid:13) . (7)
(cid:15)=
3G2
λ h2
j
+
3
+O
G3
.
(cid:13) s (cid:13) (cid:5) (cid:13) s (cid:13) (cid:5) j=1
To obtain an upper bound on kE(Eˆ s ) − esLk (cid:5) , we While the bound that we have in Corollary 2 is
perform a series expansion of the operators Eˆ s and tighter than[15, Theorem 1], a carefulanalysis ofthe
esL with respect to the parameter s to get Eˆ s = third order terms in [15, Theorem 1] yields the same
P j≥0 Aˆ j sj and esL = P j≥0 B j sj. Using this nota- expression as that given in Corollary 2.
tion, wecanseethatAˆ andB arebothtriviallythe One might also observe that when all the prob-
0 0
identityoperator1, andE(Aˆ )andB arebothequal abilities in Theorem 1 are set to p = 1, we have
1 1 j
to the Liouvillean L. To obtain the O(t2µ/G) and kuk = kvk = 0 and kwk is minimized, which im-
1 1 1
O(t3µ2/G2) terms in (cid:15), we evaluate upper bounds on plies that (cid:15)/r which is roughly the simulation error
kE(Aˆ )−B k and kE(Aˆ )−B k respectively. To per time segment s, is in fact minimized. This leads
2 2 (cid:5) 3 3 (cid:5)
do this, we rewrite Aˆ as sums over products of Lˆkj, onetowonderwhatadvantagemightbegainedbyset-
2 j
where each sum comprises of terms of the form Lˆ2, tingtheprobabilitiestobeotherwise. Thesolutionto
j this conundrum lies in the penalty we pay in making
Lˆ j Lˆ k , where j and k are distinct indices. Having j such a choice. In this scenario, each Eˆ comprises of
and k distinct allows us to find that E(Lˆ2 j ) = L2 j /p j µ=Lgates,andtheoverallerror(cid:15)for s simulatingetL
and E(Lˆ j Lˆ k ) = L j L k . Using a similar strategy for need not be optimized since rsj ∼tj(µ/G)j−1, which
rewriting Aˆ , we can evaluate its expectation explic- appears as coefficients in Theorem 1, is in fact maxi-
3
itly. Writing B and B in a similar form then allows mizedwhenµ=L. Theresultantalgorithmsimulates
2 3
ustocomputetheleadingordertermsin(cid:15). Wesupply etL,withanexpectedgatecountofGwhens=µt/G
the full details of this argument in Appendix A. for all but the last repeat and r =dG/µe.
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 4

10− 2
10− 3
10− 4
10− 5
10− 6
10− 7
10− 8
15 16 17 18 19
Log(Gates)
dnuoBrorrE
CarbonDioxide
10− 3
10− 5
10− 7
10− 9
16 17 18 19 20 21
Log(Gates)
dnuoBrorrE
Ethane
10− 2
10− 3
10− 4
10− 5
10− 6
10− 7
10− 8
15 16 17 18 19
Log(Gates)
dnuoBrorrE
Propane
SparSto Corollary2 qDRIFT COS2ndOrd
Figure 1: Error Bounds: Rigorous upper bounds on the simulation errors of various molecules in the STO-3G basis set with
L≥100000arecomparedwithrigorousboundsforTrotterisationandqDRIFT.Heret=6000. Inanintermediateregimefor
expectedthenumberofgates,SparStorequiresfewergatesthanbothR1oTrottandqDRIFTforafixedsimulationerror.
For propane and carbon dioxide, the second order Trotter error bounds (COS 2nd Order [15, Theorem 2]) are too large to be
seen on the plots.
One can imagine SparSto to be analogous to an- Algorithm1SparSto(t,G,p1,...,pL,h1,...,hL)
otherqDRIFTwhereµ=1sothattheexpectednum- 1: µ←p1+···+pL
2: forallrep=1tordo
ber of gates per time segment s is equal to one. The
3: dir←fwdorbwdwithprobability1/2
tradeoffinthisscenarioisthatkuk 1 andkvk 1 arepo- 4: ifrep≤(cid:98)G/µ(cid:99)then
5: s←µt/G
tentially very large because the probabilities become
6: else
very small. The key advantage of using Theorem 1 7: s←t−(cid:98)G/µ(cid:99)µt/G
allows us to understand how (cid:15) interpolates between 8: if dir=fwdthen
9: forallj=1toLdo
having all the probabilities to be either 1 or 0. In 10: Choosexuniformlyatrandomfrom[0,1].
what follows, we consider one family of probability 11: ifx≥pjthenimplementexp(s(hj/pj)Pj)
12: else (cid:46) dir=bwd
distributions that we use together with Theorem 1.
13: forallj=Lto1do
For this example, we set p =1 whenever h is above 14: Choosexuniformlyatrandomfrom[0,1].
j j
a set threshold. Otherwise, p < 1. We denote the
15: ifx≥pjthenimplementexp(s(hj/pj)Pj)
j
active set A as the set of indices j for which p = 1,
j
and the inactive set A¯ to be the set of indices for
which p < 1. We choose the values of p according order bounds from Childs et al. [15, Theorem 2] are
j j
the following ansatz. visible, in the upper-right of the second plot.
Weperformalimitedbruteforcenumericaloptimi-
Definition 3 (Linear ansatz). For every j ∈ A, we
sation over all feasible values of µ and |A| for our
set p = 1. For every j ∈ A¯, we set p = ch . We
j P j j ansatzes; we examine |A|/L over the interval [0,1]
correspondingly have µ=|A|+c h .
j∈A¯ j with a step size of 0.1, and consider the same values
Clearly, c has to be sufficiently small so that we for µ0 =(µ−|A|)/(L−|A|) along with 1×10−5,1×
indeedhavep <1forallindicesj intheinactiveset. 10−4, and 1×10−3;weconsiderallpairwisecombina-
j
By minimizing (cid:15) with respect to all possible values of tions of these settings. Intu 1 itively we expect that as
|A| and µ using our linear ansatz, we can determine the gate budget G increases, we ought to interpolate
which probabilities p to use. These probabilities can
betweentheqDRIFTregime[12]andtheR1oTrott
j
be inputted into SparSto, which we describe in the regime, and the size of the active set |A| ought to go
pseudocode Algorithm 1. from 0 to L. We observe from our numerical study
Wenumericallystudytheperformanceof SparSto that this indeed is the case. In general, the optimal
using models of molecules drawn from the Open- activesetsizeincreaseswithG,andtheoptimalvalue
Fermion library [30], including carbon dioxide, for µ0 was usually small, and never more than 0.3.
ethane, and propane in the STO-3G basis set, and The linear ansatz outperforms the uniform ansatz.
depict these results in Fig. 1. We evaluate the error This is expected, as the uniform ansatz is naïve and
boundforSparStogivenbyTheorem5inAppendix thelinearansatzcanbeobtainedastheoptimalsolu-
A. We compare the performance of SparSto with tionoftheconvexprogramwhichminimizesthelead-
the Trotter bounds from [15] (Theorem 2 in their pa- ing order term in the total error for constant µ (see
per, setting k = 1), and by setting all probabilities AppendixB).Ineachofthemolecules,thenumberof
p = 1 we also plot Corollary 2. Only the second Hamiltoniantermsisoverahundredthousand,which
j
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 5

is very large. When t = 6000 and for a range of de- chemistry simulation. Phys. Rev. A, 91:022311,
sirederrorvalues,thereisaconsiderableadvantagein Feb 2015. DOI: 10.1103/PhysRevA.91.022311.
| SparSto |     | R1oTrott |     |     |     |     |     |     |     |     |     |
| ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
using over both and qDRIFT. [3] RyanBabbush,CraigGidney,DominicW.Berry,
Weobservesimilarresultsacrossothervaluesoftand Nathan Wiebe, Jarrod McClean, Alexandru
smaller molecules. Paler, Austin Fowler, and Hartmut Neven. En-
|     |     |     |     |     |     | coding | electronic | spectra |     | in quantum | circuits |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | ------- | --- | ---------- | -------- |
withlinearTcomplexity.Phys.Rev.X,8:041015,
4 Discussion
|     |     |     |     |     |     | Oct 2018.                                  | DOI: | 10.1103/PhysRevX.8.041015. |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | ---- | -------------------------- | --- | --- | --- |
|     |     |     |     |     |     | [4] RyanBabbush,NathanWiebe,JarrodMcClean, |      |                            |     |     |     |
While vanilla Trotterisation can simulate any Hamil- James McClain, Hartmut Neven, and Garnet
tonian with sufficiently many gates, the number of Kin-Lic Chan. Low-depth quantum simulation
|             |            |      |             |       |        | of materials. |     | Phys. Rev. | X,  | 8:011044, | Mar 2018. |
| ----------- | ---------- | ---- | ----------- | ----- | ------ | ------------- | --- | ---------- | --- | --------- | --------- |
| these gates | can become | very | large. This | leads | to the |               |     |            |     |           |           |
need to reduce the gate count of quantum simula- DOI: 10.1103/PhysRevX.8.011044.
tion while keeping the size of simulation error fixed. [5] H. Beinert. Iron-sulfur clusters: Nature’s mod-
Here we present a new approach to chemistry sim- ular, multipurpose structures. Science, 277
ulation on a quantum machine, using the stochastic (5326):653–659, August 1997. DOI: 10.1126/sci-
ence.277.5326.653.
| sparsification | of a target | Hamiltonian |     | to derive | a hy- |     |     |     |     |     |     |
| -------------- | ----------- | ----------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- |
brid approach between canonical Trotterisation and [6] Dominic W Berry. A random approach to quan-
qDRIFT.Ouranalysisprovidesanuppererrorbound tum simulation. Physics, 12:91, 2019. DOI:
for the scheme, and optimisation over the probabili- 10.1103/physics.12.91.
ties used in sparsification allows for reductions in the [7] Dominic W. Berry, Andrew M. Childs, Richard
simulation error over parameter regimes of interest. Cleve, Robin Kothari, and Rolando D. Somma.
Itwouldbeinstructivetoconsiderhowtheideasin Exponential improvement in precision for simu-
|     |     |     |     |     |     | latingsparseHamiltonians. |     |     |     | ForumofMathemat- |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ---------------- | --- |
ourhybridapproachmightextendtoothervariantsof
quantum simulation schemes, such as that of the so- ics, Sigma, 5, 2017. DOI: 10.1017/fms.2017.2.
called “quantum signal processing” (QSP) [26] tech- [8] Dominic W Berry, Andrew M Childs, Yuan Su,
niques, linear combinations of unitaries [7], the use of Xin Wang, and Nathan Wiebe. Time-dependent
quantum walks [9, 13], qubitisation [9, 27] and post- Hamiltonian simulation with L1-norm scaling.
|                           |     |                        |     |     |     | arXiv preprint |     | arXiv:1906.07115, |     |     | 2019. |
| ------------------------- | --- | ---------------------- | --- | --- | --- | -------------- | --- | ----------------- | --- | --- | ----- |
| processingtechniques[18]. |     | Therehasalsobeenrecent |     |     |     |                |     |                   |     |     |       |
interest in the quantum simulation of time depen- [9] Dominic W. Berry, Craig Gidney, Mario Motta,
dent Hamiltonians [8, 28], and applications of quan- Jarrod R. McClean, and Ryan Babbush. Qubiti-
tum simulation in phase estimation [12, 22], which zation of Arbitrary Basis Quantum Chemistry
may also prove amenable to stochastic sparsification. Leveraging Sparsity and Low Rank Factoriza-
| Given that | random | techniques | can prove | advanta- |     |                |     |        |          |     |            |
| ---------- | ------ | ---------- | --------- | -------- | --- | -------------- | --- | ------ | -------- | --- | ---------- |
|            |        |            |           |          |     | tion. Quantum, |     | 3:208, | December |     | 2019. ISSN |
geouswhenappliedtohybridquantum-classicalalgo- 2521-327X. DOI: 10.22331/q-2019-12-02-208.
rithmsfornumericaloptimisation[41],ourtechniques [10] Sergey Bravyi and Jeongwan Haah. Quantum
might also offer some speedups in this area. Further- Self-Correction in the 3D Cubic Code Model.
more, there might exist certain families of Hamilto- Phys. Rev. Lett., 111(20):200501, November
| nians where | the advantage |     | of using | our techniques |     |            |                                 |     |     |     |     |
| ----------- | ------------- | --- | -------- | -------------- | --- | ---------- | ------------------------------- | --- | --- | --- | --- |
|             |               |     |          |                |     | 2013. DOI: | 10.1103/PhysRevLett.111.200501. |     |     |     |     |
over deterministic Trotterisation can be understood [11] EarlCampbell. Shortergatesequencesforquan-
| analytically, | and we | leave this | as a subject | for | future |               |     |           |     |            |               |
| ------------- | ------ | ---------- | ------------ | --- | ------ | ------------- | --- | --------- | --- | ---------- | ------------- |
|               |        |            |              |     |        | tum computing |     | by mixing |     | unitaries. | Phys. Rev.    |
| work.         |        |            |              |     |        | A, 95:042306, |     | Apr 2017. |     | DOI:       | 10.1103/Phys- |
Acknowledgements.- This work was supported by RevA.95.042306.
theEPSRC(grantno. EP/M024261/1), andhasalso [12] Earl Campbell. Random compiler for fast
received research funding from Huawei. We like to Hamiltonian simulation. Phys. Rev. Lett.,
| thank Yuan | Su for | a careful | reading | and comments |     |             |     |           |     |      |               |
| ---------- | ------ | --------- | ------- | ------------ | --- | ----------- | --- | --------- | --- | ---- | ------------- |
|            |        |           |         |              |     | 123:070503, |     | Aug 2019. |     | DOI: | 10.1103/Phys- |
on an earlier version of this manuscript. RevLett.123.070503.
|            |     |     |     |     | [13] | AndrewM.ChildsandDominicW.Berry.Black- |         |            |                     |     |                |
| ---------- | --- | --- | --- | --- | ---- | -------------------------------------- | ------- | ---------- | ------------------- | --- | -------------- |
|            |     |     |     |     |      | box Hamiltonian                        |         | simulation |                     | and | unitary imple- |
| References |     |     |     |     |      | mentation.                             | Quantum |            | Information         |     | and Computa-   |
|            |     |     |     |     |      | tion, 12(1-2),                         |         | 2012. DOI: | 10.26421/qic12.1-2. |     |                |
[1] A. Aspuru-Guzik. Simulated quantum computa- [14] Andrew M. Childs, Dmitri Maslov, Yunseong
tion of molecular energies. Science, 309(5741): Nam, Neil J. Ross, and Yuan Su. Toward the
1704–1707, September 2005. DOI: 10.1126/sci- firstquantumsimulationwithquantumspeedup.
| ence.1113479. |     |     |     |     |     | ProceedingsoftheNationalAcademyofSciences, |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
[2] Ryan Babbush, Jarrod McClean, Dave Wecker, 115(38):9456–9461, 2018. ISSN 0027-8424. DOI:
Alán Aspuru-Guzik, and Nathan Wiebe. Chem- 10.1073/pnas.1801723115.
ical basis of Trotter-Suzuki errors in quantum [15] Andrew M. Childs, Aaron Ostrander, and Yuan
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 6

Su. Faster quantum simulation by randomiza- Hamiltonian simulation by quantum signal pro-
tion. Quantum, 3:182, September 2019. DOI: cessing. PhysicalReviewLetters,118(1),January
10.22331/q-2019-09-02-182. 2017. DOI: 10.1103/physrevlett.118.010501.
[16] MatthewB.Hastings. Turninggatesynthesiser- [27] Guang Hao Low and Isaac L. Chuang. Hamil-
rorsintoincoherenterrors. Quantum Info. Com- tonian simulation by qubitization. Quantum, 3:
put., 17(5-6):488–494, March 2017. ISSN 1533- 163,July2019. DOI:10.22331/q-2019-07-12-163.
7146. DOI: 10.26421/QIC17.5-6. [28] Guang Hao Low and Nathan Wiebe. Hamil-
[17] Cornelius Hempel, Christine Maier, Jonathan tonian simulation in the interaction picture.
Romero, Jarrod McClean, Thomas Monz, Heng arXiv:1805.00675, 2018.
Shen, Petar Jurcevic, Ben P. Lanyon, Pe- [29] Sam McArdle, Suguru Endo, Alan Aspuru-
ter Love, Ryan Babbush, Alán Aspuru-Guzik, Guzik, Simon Benjamin, and Xiao Yuan. Quan-
| Rainer | Blatt, | and Christian |     | F. Roos. | Quantum |     |     |               |     |            |     |       |          |
| ------ | ------ | ------------- | --- | -------- | ------- | --- | --- | ------------- | --- | ---------- | --- | ----- | -------- |
|        |        |               |     |          |         |     | tum | computational |     | chemistry. |     | arXiv | preprint |
chemistrycalculationsonatrapped-ionquantum arXiv:1808.10402, 2018.
simulator. Phys. Rev. X, 8:031022, Jul 2018. [30] Jarrod R McClean, Ian D Kivlichan, Kevin J
DOI: 10.1103/PhysRevX.8.031022. Sung, Damian S Steiger, Yudong Cao, Chengyu
[18] William J. Huggins, Jarrod McClean, Nicholas Dai, E Schuyler Fried, Craig Gidney, Brendan
| Rubin, | Zhang | Jiang, | Nathan | Wiebe, |     | K. Bir- |        |        |     |          |        |              |     |
| ------ | ----- | ------ | ------ | ------ | --- | ------- | ------ | ------ | --- | -------- | ------ | ------------ | --- |
|        |       |        |        |        |     |         | Gimby, | Pranav |     | Gokhale, | et al. | OpenFermion: |     |
gitta Whaley, and Ryan Babbush. Efficient the electronic structure package for quantum
and noise resilient measurements for quantum computers. arXiv preprint arXiv:1710.07629,
| chemistry |     | on near-term |     | quantum | computers. |     | 2017. |     |     |     |     |     |     |
| --------- | --- | ------------ | --- | ------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- |
arXiv:1907.13117, 2019. [31] Jarrod R. McClean, Fabian M. Faulstich, Qinyi
[19] Alexei Yu Kitaev, Alexander Shen, Mikhail N Zhu, Bryan O’Gorman, Yiheng Qiu, Steven R.
Vyalyi, and Mikhail N Vyalyi. Classi- White, Ryan Babbush, and Lin Lin. Discontinu-
| cal | and quantum | computation. |     |     | Number | 47. |     |          |                |     |     |         |         |
| --- | ----------- | ------------ | --- | --- | ------ | --- | --- | -------- | -------------- | --- | --- | ------- | ------- |
|     |             |              |     |     |        |     | ous | Galerkin | discretization |     | for | quantum | simula- |
American Mathematical Soc., 2002. DOI: tion of chemistry. arXiv:1909.00028, 2019.
10.1090/gsm/047. [32] Jorge Nocedal and Stephen Wright. Numerical
[20] Ian D. Kivlichan, Jarrod McClean, Nathan optimization. Springer Science & Business Me-
Wiebe, Craig Gidney, Alán Aspuru-Guzik, Gar- dia, 2006. DOI: 10.1007/b98874.
| net | Kin-Lic | Chan, and | Ryan | Babbush. |     | Quan- |            |              |     |             |     |       |            |
| --- | ------- | --------- | ---- | -------- | --- | ----- | ---------- | ------------ | --- | ----------- | --- | ----- | ---------- |
|     |         |           |      |          |     |       | [33] P. J. | J. O’Malley, |     | R. Babbush, |     | I. D. | Kivlichan, |
tum simulation of electronic structure with lin- J. Romero, J. R. McClean, R. Barends, J. Kelly,
| ear | depth | and connectivity. |     | Phys. | Rev. | Lett., |             |     |     |          |          |     |           |
| --- | ----- | ----------------- | --- | ----- | ---- | ------ | ----------- | --- | --- | -------- | -------- | --- | --------- |
|     |       |                   |     |       |      |        | P. Roushan, |     | A.  | Tranter, | N. Ding, | B.  | Campbell, |
120:110501, Mar 2018. DOI: 10.1103/Phys- Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth,
RevLett.120.110501. A. G. Fowler, E. Jeffrey, E. Lucero, A. Megrant,
[21] Ian D. Kivlichan, Craig Gidney, Dominic W. J. Y. Mutus, M. Neeley, C. Neill, C. Quin-
Berry,NathanWiebe,JarrodMcClean,WeiSun, tana, D. Sank, A. Vainsencher, J. Wenner, T. C.
| Zhang | Jiang, | Nicholas | Rubin, |     | Austin | Fowler, |        |     |             |     |       |       |           |
| ----- | ------ | -------- | ------ | --- | ------ | ------- | ------ | --- | ----------- | --- | ----- | ----- | --------- |
|       |        |          |        |     |        |         | White, | P.  | V. Coveney, |     | P. J. | Love, | H. Neven, |
Alán Aspuru-Guzik, Hartmut Neven, and Ryan A. Aspuru-Guzik, and J. M. Martinis. Scalable
Babbush. Improved fault-tolerant quantum sim- quantumsimulationofmolecularenergies. Phys.
ulation of condensed-phase correlated electrons Rev. X, 6:031007, Jul 2016. DOI: 10.1103/Phys-
| via      | Trotterization. | arXiv:1902.10673, |     |     | 2019.    |     | RevX.6.031007. |         |     |       |           |     |            |
| -------- | --------------- | ----------------- | --- | --- | -------- | --- | -------------- | ------- | --- | ----- | --------- | --- | ---------- |
| [22] Ian | D. Kivlichan,   | Christopher       |     | E.  | Granade, | and |                |         |     |       |           |     |            |
|          |                 |                   |     |     |          |     | [34] David     | Poulin, |     | M. B. | Hastings, |     | D. Wecker, |
Nathan Wiebe. Phase estimation with random- N. Wiebe, Andrew C. Doberty, and M. Troyer.
ized Hamiltonians. arXiv:1907.10070, 2019. TheTrotterstepsizerequiredforaccuratequan-
[23] Zhaokai Li, Xiaomei Liu, Hefeng Wang, Sahel tum simulation of quantum chemistry. Quantum
Ashhab, Jiangyu Cui, Hongwei Chen, Xinhua Information & Computation, 15(5-6):0361–0384,
Peng, and Jiangfeng Du. Quantum simulation 2015. DOI: 10.26421/qic15.5-6.
of resonant transitions for solving the eigenprob- [35] MarkusReiher,NathanWiebe,KrystaM.Svore,
lemofaneffectivewaterHamiltonian.Phys.Rev.
|     |     |     |     |     |     |     | Dave | Wecker, | and | Matthias | Troyer. |     | Elucidat- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --- | -------- | ------- | --- | --------- |
Lett.,122:090504,Mar2019.DOI:10.1103/Phys- ing reaction mechanisms on quantum comput-
RevLett.122.090504. ers. Proceedings of the National Academy of
[24] G Lindblad. On the generators of quantum dy- Sciences, 114(29):7555–7560, July 2017. DOI:
namical semigroups. Communications in Mathe- 10.1073/pnas.1619152114.
maticalPhysics,48(2):119–130,1976.ISSN0010-
|     |     |     |     |     |     |     | [36] Kanav | Setia | and | James | D. Whitfield. |     | Bravyi- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | ----- | ------------- | --- | ------- |
3616. DOI: 10.1007/BF01608499. Kitaev superfast simulation of electronic struc-
[25] S. Lloyd. Universal quantum simulators. Sci- ture on a quantum computer. The Journal of
ence, 273(5278):1073–1078, August 1996. DOI: Chemical Physics, 148(16):164104, April 2018.
| 10.1126/science.273.5278.1073. |     |     |     |     |     |     | DOI: | 10.1063/1.5019371. |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | ---- | ------------------ | --- | --- | --- | --- | --- |
[26] Guang Hao Low and Isaac L. Chuang. Optimal [37] Rolando D. Somma. A Trotter-Suzuki ap-
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 7

proximation for lie groups with applications to Meynard-Piganeau, and Jens Eisert. Stochas-
Hamiltonian simulation. Journal of Mathemat- ticgradientdescentforhybridquantum-classical
ical Physics, 57(6):062202, June 2016. DOI: optimization. arXiv preprint arXiv:1910.01155,
| 10.1063/1.4952761. |     |     |     | 2019. |     |     |     |
| ------------------ | --- | --- | --- | ----- | --- | --- | --- |
[38] MasuoSuzuki.GeneralizedTrotter’sformulaand [42] Dave Wecker, Bela Bauer, Bryan K. Clark,
systematic approximants of exponential opera- Matthew B. Hastings, and Matthias Troyer.
tors and inner derivations with applications to Gate-count estimates for performing quan-
|           |           |             |           | tum chemistry | on small | quantum computers. |     |
| --------- | --------- | ----------- | --------- | ------------- | -------- | ------------------ | --- |
| many-body | problems. | Comm. Math. | Phys., 51 |               |          |                    |     |
(2):183–190, 1976. DOI: 10.1007/bf01609348. Phys. Rev. A, 90:022305, Aug 2014. DOI:
[39] Masuo Suzuki. Fractal decomposition of ex- 10.1103/PhysRevA.90.022305.
ponential operators with applications to many- [43] Dave Wecker, Bela Bauer, Bryan K. Clark,
body theories and Monte Carlo simulations. Matthew B. Hastings, and Matthias Troyer.
|         |                            |      |       | Gate-count | estimates | for performing | quan- |
| ------- | -------------------------- | ---- | ----- | ---------- | --------- | -------------- | ----- |
| Physics | Letters A, 146(6):319–323, | June | 1990. |            |           |                |       |
DOI: 10.1016/0375-9601(90)90962-n. tum chemistry on small quantum computers.
|                   |                               |     |     | Phys. Rev. | A, 90:022305, | Aug 2014. | DOI: |
| ----------------- | ----------------------------- | --- | --- | ---------- | ------------- | --------- | ---- |
| [40] MasuoSuzuki. | Generaltheoryoffractalpathin- |     |     |            |               |           |      |
tegrals with applications to many-body theories 10.1103/PhysRevA.90.022305.
and statistical physics. Journal of Mathemati- [44] James D. Whitfield, Jacob Biamonte, and Alán
|              |                |                |      | Aspuru-Guzik. | Simulationofelectronicstructure |     |     |
| ------------ | -------------- | -------------- | ---- | ------------- | ------------------------------- | --- | --- |
| cal Physics, | 32(2):400–407, | February 1991. | DOI: |               |                                 |     |     |
10.1063/1.529425. Hamiltonians using quantum computers. Molec-
|                  |          |                 |        | ular Physics, | 109(5):735–750, | March 2011. | DOI: |
| ---------------- | -------- | --------------- | ------ | ------------- | --------------- | ----------- | ---- |
| [41] Ryan Sweke, | Frederik | Wilde, Johannes | Meyer, |               |                 |             |      |
Maria Schuld, Paul K Fährmann, Barthélémy 10.1080/00268976.2011.552441.
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 8

| A Upper |     | bounds | on the | simulation |     |     | error |     |     |     |     |
| ------- | --- | ------ | ------ | ---------- | --- | --- | ----- | --- | --- | --- | --- |
In this section, we show that Theorem 1 is a corollary of Theorem 5, which we state in Section A.2. Before
we can state Theorem 1, we define relevant notation in Section A.1. After that, we evaluate the leading order
terms and tail terms of Theorem 5 in Section A.3 and Section A.4 respectively.
| A.1 Sum | over | distinct | indices |     |     |     |     |     |     |     |     |
| ------- | ---- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Given real vectors a = (a ,...,a ),b = (b ,...,b ) and c = (c ,...,c ), we define the sums over distinct
|            |     |     | 1   | n   |     | 1   | n   |     | 1   | n   |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indices to | be  |     |     |     |     |     |     |     |     |     |     |
n
X
|     |     |     |     |     | S(a)= | a   | ≤kak | ,   |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |       |     | j    | 1   |     |     |     |
j=1
X
|     |     |     |     | S(a,b)= |     |     | a   | b ≤kak | kbk , |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | ------ | ----- | --- | --- |
|     |     |     |     |         |     |     | j   | k      | 1 1   |     |     |
1≤j,k≤n
j,k distinct
X
|     |     |     |     | S(a,b,c)= |     |     | a   | b c   | ≤kak kbk | kck . | (8) |
| --- | --- | --- | --- | --------- | --- | --- | --- | ----- | -------- | ----- | --- |
|     |     |     |     |           |     |     |     | j k l | 1        | 1 1   |     |
1≤j,k,l≤n
j,k,l distinct
To perform fast computation of the above sums, we can use the following lemma which vectorises summations
| with distinct | indices. |     |     |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Lemma 4. Let n be a positive integer. Let a=(a ,...,a ) and b=(b ,...,b ) be real column vectors. Then
|     |     |     |     |                |          |     | 1      | n     | 1     | n   |      |
| --- | --- | --- | --- | -------------- | -------- | --- | ------ | ----- | ----- | --- | ---- |
|     |     |     |     |                | S(a,b)=A | 1   | B 1 −C | 1     |       |     | (9)  |
|     |     |     |     | S(a,b,b)=A     |          |     | (B2−B  | )−2C  | B +2C | ,   | (10) |
|     |     |     |     |                |          | 1   | 1      | 2     | 1 1   | 2   |      |
|     |     |     |     | S(a,a,a)=A3−3A |          |     |        | A +2A | ,     |     | (11) |
|     |     |     |     |                |          | 1   | 2      | 1     | 3     |     |      |
where
n
X
|     |     |     |     |     |     | A   | =   | aj, |     |     | (12) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     | j   | u   |     |     |      |
u=1
n
|     |     |     |     |     |     |     | X   | bj, |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | B   | j = |     |     |     | (13) |
u
u=1
n
X
|     |     |     |     |     |     | C   | =   | a bj. |     |     | (14) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- |
|     |     |     |     |     |     |     | j   | u u   |     |     |      |
u=1
Lemma 4 can be proved iteratively by careful consideration of summation indices.
Proof of Lemma 4. The result (9) is straightforward to show. To show (10), note that we can use (9) to write
X
|     |     |     |     |     | a b | b   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | u   | v w |     |     |     |     |     |
1≤u,v,w≤n
u,v,w distinct
|        |            |      | X      | n           | X            |         | X            |     | X            |             |     |
| ------ | ---------- | ---- | ------ | ----------- | ------------ | ------- | ------------ | --- | ------------ | ----------- | --- |
|        |            |      | =      | a u         |              | b v b w | −            | a u | b u b w −    | a u b u b v |     |
|        |            |      | u=1    |             | 1≤v,w≤n      |         | 1≤u,w≤n      |     | 1≤u,v≤n      |             |     |
|        |            |      |        | v,w         | distinct     |         | u,w distinct |     | u,v distinct |             |     |
|        |            |      |        |             |              | n       |              |     | n            |             |     |
|        |            |      |        |             |              | X       |              |     | X            |             |     |
|        |            |      | =A     | (B2−B       | )−2          |         | a b B        | +2  | a b2.        |             |     |
|        |            |      |        | 1 1         | 2            |         | u u          | 1   | u u          |             |     |
|        |            |      |        |             |              | u=1     |              |     | u=1          |             |     |
| We can | specialize | this | to sum | of distinct | combinations |         | of           | a a | a to get     |             |     |
|        |            |      |        |             |              |         |              | u   | v w          |             |     |
|        |            |      |        | X           |              |         | (A2−A        |     |              |             |     |
|        |            |      |        |             | a            | a a =A  |              |     | )−2A A       | +2A ,       |     |
|        |            |      |        |             | u            | v w     | 1            | 1   | 2 2          | 1 3         |     |
1≤u,v,w≤n
u,v,w distinct
| which yields | (11). |     |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 9

| A.2 Complete |     | simulation | error      |          | bound |          |        |            |     |     |
| ------------ | --- | ---------- | ---------- | -------- | ----- | -------- | ------ | ---------- | --- | --- |
| The complete |     | upper      | bound that | we prove | here  | is given | by the | following. |     |     |
Theorem 5. Using SparSto with vector of probabilities p = (p ,...,p ), vector of Hamiltonian coefficients
|     |     |     |     |     |     |     |     | 1   | L   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
h = (h ,...,h ), L ≥ 3, and expected number of gates G where G/(p +···+p ) is an integer, the error of
| 1          |     | L          |                |                   |                     |           |     |     | 1 L |     |
| ---------- | --- | ---------- | -------------- | ----------------- | ------------------- | --------- | --- | --- | --- | --- |
| simulating | etL | is at most | (cid:15) where | (cid:15)=(cid:15) | +(cid:15) +(cid:15) | +(cid:15) | and |     |     |     |
|            |     |            |                |                   | 1 2                 | 3,1       | 3,2 |     |     |     |
2t2µ
|     |     |     |     | (cid:15) 1 = | S(u), |     |     |     |     |     |
| --- | --- | --- | --- | ------------ | ----- | --- | --- | --- | --- | --- |
G
|     |     |     |     |            | 4t3µ2          |     |     | 16t3µ2 |           |     |
| --- | --- | --- | --- | ---------- | -------------- | --- | --- | ------ | --------- | --- |
|     |     |     |     | (cid:15) = | (S(v)+S(w,h))+ |     |     |        | S(h,h,h), |     |
|     |     |     |     | 2          | 3G2            |     |     | 9G2    |           |     |
2t4µ3λ4
|     |     |     | (cid:15) | =   | ,   |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |          | 3,1 | 3G3 |     |     |     |     |     |
2t4µ3
|         |     |               | (cid:15) | =   | (p        | ...p )S(q)4, |       |     |     |     |
| ------- | --- | ------------- | -------- | --- | --------- | ------------ | ----- | --- | --- | --- |
|         |     |               |          | 3,2 | 3G3 1     | L            |       |     |     |     |
| with µ= | PL  | p . Moreover, | u,v,w    |     | and q are | vectors      | given | by  |     |     |
j=1 j
|     |     |     |     |     | (cid:18)(cid:18)   | (cid:19)   | (cid:18) | (cid:19)   | (cid:19) |     |
| --- | --- | --- | --- | --- | ------------------ | ---------- | -------- | ---------- | -------- | --- |
|     |     |     |     |     | 1                  |            |          | 1          |          |     |
|     |     |     |     | u=  |                    | −1 h2,..., |          | −1         | h2 ,     |     |
|     |     |     |     |     | p                  |            | 1        | p          | L        |     |
|     |     |     |     |     | 1                  |            |          | L          |          |     |
|     |     |     |     |     | (cid:18)(cid:18) 1 | (cid:19)   | (cid:18) | 1 (cid:19) | (cid:19) |     |
|     |     |     |     |     |                    | h3,...,    |          |            | h3       |     |
|     |     |     |     | v=  |                    | −1         |          | −1         | ,        |     |
|     |     |     |     |     | p2                 |            | 1        | p2         | L        |     |
|     |     |     |     |     | 1                  |            |          | L          |          |     |
|     |     |     |     |     | (cid:18)(cid:18)   | (cid:19)   | (cid:18) | (cid:19)   | (cid:19) |     |
|     |     |     |     |     | 3                  |            |          | 3          |          |     |
|     |     |     |     | w=  |                    | −1 h2,..., |          | −1         | h2 ,     |     |
|     |     |     |     |     |                    |            | 1        |            | L        |     |
|     |     |     |     |     | p 1                |            |          | p L        |          |     |
|     |     |     |     |     | (cid:18)           | (cid:19)   |          |            |          |     |
|     |     |     |     |     | h 1,...,           | h L        |          |            |          |     |
|     |     |     |     | q=  |                    |            | .        |            |          |     |
|     |     |     |     |     | p                  | p          |          |            |          |     |
|     |     |     |     |     | 1                  | L          |          |            |          |     |
We use S as defined in Section A.1. We will see that by considering explicitly the commutation structure of
the matrices P , we can obtain a tighter bound on (cid:15) in Theorem 5 by substituting S(h,h,h) for D in (45).
|     |     | j   |     |     |     | 2   |     |     |     | 5   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Before we proceed to prove Theorem 5, we prove that Theorem 1 is a straightforward consequence of Theo-
| rem 5.   | Note that |     |                 |     |            |         |          |       |     |     |
| -------- | --------- | --- | --------------- | --- | ---------- | ------- | -------- | ----- | --- | --- |
| Proof of | Theorem   | 1.  | By overcounting |     | (8), it is | easy to | see that |       |     |     |
|          |           |     |                 |     | S(w,h)≤kwk |         | khk      | =λkwk | ,   |     |
|          |           |     |                 |     |            |         | 1 1      |       | 1   |     |
and
=λ3.
|     |     |     |     |     | S(h,h,h)≤khk |     | 1 khk 1 | khk 1 |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | ----- | --- | --- |
Moreover, since u and v are non-negative vectors, we have S(u) = kuk and S(v) = kvk . Furthermore, we
|               |              |     |      |           |            |     |     |     | 1 1 |     |
| ------------- | ------------ | --- | ---- | --------- | ---------- | --- | --- | --- | --- | --- |
| have (cid:15) | =O(t4µ3/G3). |     | This | completes | the proof. |     |     |     |     |     |
3,j
The proof of Theorem 5 then arises from the evaluation of (1) the leading order terms (cid:15) and (cid:15) , and (2)
1 2
the higher order terms (cid:15) and (cid:15) . This will proceed in the next two subsections. We emphasize that in
|     |     |     | 3,1 | 3,2 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
what follows, because of the telescoping argument we mentioned in the main text, it suffices to only analyze
kEˆ −esLk , and the overall simulation error will just be r times of this diamond norm.
| s       | (cid:5) |       |       |          |                 |         |     |     |     |     |
| ------- | ------- | ----- | ----- | -------- | --------------- | ------- | --- | --- | --- | --- |
| A.3 The | leading | order | terms | (cid:15) | and (cid:15) in | Theorem | 5   |     |     |     |
1 2
Here, we show that the leading order terms in the simulation error are as given by (cid:15) and (cid:15) . First recall that
1 2
|         |            |        |            |     | Eˆ P | Aˆ sj | esL | P   | sj. |     |
| ------- | ---------- | ------ | ---------- | --- | ---- | ----- | --- | --- | --- | --- |
| we have | the Taylor | series | expansions |     | s =  | j     | and | =   | B j |     |
|         |            |        |            |     | j≥0  |       |     | j≥0 |     |     |
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 10

| Note | that when | L≥3, | we  | have |            |       |     |      |        |          |     |     |
| ---- | --------- | ---- | --- | ---- | ---------- | ----- | --- | ---- | ------ | -------- | --- | --- |
|      |           |      |     |      | L (cid:18) |       | s2  |      | s3     | (cid:19) |     |     |
|      |           |      |     | Tˆ   | Y          | 1+sLˆ |     | Lˆ 2 | Lˆ 3   |          |     |     |
|      |           |      |     | s,→  | =          |       | j + | j +  | j +... |          |     |     |
|      |           |      |     |      |            |       | 2   |      | 6      |          |     |     |
j=1
|     |     |     |     |     |      | L    | s2  | L      | 2s2     |     |       |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | ------ | ------- | --- | ----- | --- |
|     |     |     |     |     |      | X Lˆ |     | X Lˆ 2 |         | X   | Lˆ Lˆ |     |
|     |     |     |     |     | =1+s |      | +   |        | +       |     |       |     |
|     |     |     |     |     |      |      | j 2 | j      | 2       |     | j k   |     |
|     |     |     |     |     |      | j=1  |     | j=1    | 1≤j<k≤L |     |       |     |
L
|     |     |     |     |     | s3  | X     | s2  | X       | (cid:16) |         | (cid:17) |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------- | -------- | ------- | -------- | --- |
|     |     |     |     |     | +   | Lˆ3+s |     |         | Lˆ2Lˆ    | +Lˆ Lˆ2 |          |     |
|     |     |     |     |     |     |       | j   |         | j        | k j     | k        |     |
|     |     |     |     |     | 6   |       | 2   |         |          |         |          |     |
|     |     |     |     |     |     | j=1   |     | 1≤j<k≤L |          |         |          |     |
X
|     |     |     |     |     | +s3 |     | Lˆ  | Lˆ Lˆ +.... |     |     |     | (15) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     | j k l       |     |     |     |      |
1≤j<k<l≤L
Similarly,
|     |     |     |     |     |      | L   |     | L   |         |     |       |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | --- | ----- | --- |
|     |     |     |     |     |      | X   | s2  | X 2 | 2s2     | X   |       |     |
|     |     |     |     | Tˆ  | =1+s | Lˆ  | +   | Lˆ  | +       |     | Lˆ Lˆ |     |
|     |     |     |     | s,← |      |     | j   | j   |         |     | j k   |     |
|     |     |     |     |     |      |     | 2   |     | 2       |     |       |     |
|     |     |     |     |     |      | j=1 |     | j=1 | 1≤k<j≤L |     |       |     |
L
|     |     |     |     |     | s3  | X     | s2  | X       | (cid:16) |         | (cid:17) |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------- | -------- | ------- | -------- | --- |
|     |     |     |     |     | +   | Lˆ3+s |     |         | Lˆ2Lˆ    | +Lˆ Lˆ2 |          |     |
|     |     |     |     |     |     |       | j   |         | j        | k j     | k        |     |
|     |     |     |     |     | 6   |       | 2   |         |          |         |          |     |
|     |     |     |     |     |     | j=1   |     | 1≤j<k≤L |          |         |          |     |
X
|     |     |     |     |     | +s3 |     | Lˆ  | Lˆ Lˆ +.... |     |     |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     | j k l       |     |     |     |      |
1≤l<k<j≤L
|          | (cid:16) |        | (cid:17) |        |          |       |      |     |     |     |     |     |
| -------- | -------- | ------ | -------- | ------ | -------- | ----- | ---- | --- | --- | --- | --- | --- |
| Since Eˆ | = 1      | Tˆ +Tˆ |          | , (15) | and (16) | imply | that |     |     |     |     |     |
|          | s 2      | s,→    | s,←      |        |          |       |      |     |     |     |     |     |
L
|     |     |     |      | X   | 2    | X    |      |     |     |     |     |      |
| --- | --- | --- | ---- | --- | ---- | ---- | ---- | --- | --- | --- | --- | ---- |
|     |     |     | 2!Aˆ | =   | Lˆ + | Lˆ   | Lˆ , |     |     |     |     | (17) |
|     |     |     |      | 2   | j    |      | j k  |     |     |     |     |      |
|     |     |     |      | j=1 |      | j6=k |      |     |     |     |     |      |
L
|     |     |     |      | X   |      | 6X(cid:16) |       |         | (cid:17) 6 | X   |           |      |
| --- | --- | --- | ---- | --- | ---- | ---------- | ----- | ------- | ---------- | --- | --------- | ---- |
|     |     |     | 3!Aˆ |     | Lˆ3+ |            | Lˆ2Lˆ | +Lˆ Lˆ2 |            |     | Lˆ Lˆ Lˆ. |      |
|     |     |     |      | 3 = | j    |            | j k   | j k     | +          |     | j k l     | (18) |
|     |     |     |      |     |      | 4          |       |         | 2          |     |           |      |
|     |     |     |      | j=1 |      | j6=k       |       |         | 1≤j<k<l≤L  |     |           |      |
1≤l<k<j≤L
| Moreover, | we  | know | that |     |     |     |     |     |     |     |     |     |
| --------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L
|     |     |     | X    |     | X    |     |     |     |     |     |     |      |
| --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     | L2 = | L2+ | L    | L , |     |     |     |     |     | (19) |
|     |     |     |      | j   |      | j k |     |     |     |     |     |      |
|     |     |     | j=1  |     | j6=k |     |     |     |     |     |     |      |
L
|         |            |     | X    |           | X(cid:0) |       |           |      |           |           |         |      |
| ------- | ---------- | --- | ---- | --------- | -------- | ----- | --------- | ---- | --------- | --------- | ------- | ---- |
|         |            |     | L3 = | L3+       |          | L2L   | +L L2     | +L L | L (cid:1) |           |         |      |
|         |            |     |      | j         |          | j k   | j k       | j    | k j       |           |         |      |
|         |            |     | j=1  |           | j6=k     |       |           |      |           |           |         |      |
|         |            |     |      | X         |          |       |           | X    |           | X         |         |      |
|         |            |     | +    |           | L        | L L   | +         | L    | L L       | +         | L L L . | (20) |
|         |            |     |      |           |          | j k l |           |      | j k l     |           | j k l   |      |
|         |            |     |      | 1≤j<k<l≤L |          |       | 1≤k<j<l≤L |      |           | 1≤j<l<k≤L |         |      |
|         |            |     |      | 1≤l<k<j≤L |          |       | 1≤k<l<j≤L |      |           | 1≤l<j<k≤L |         |      |
| Clearly | L−E(Lˆ)=0. |     | Next | note      | that     |       |           |      |           |           |         |      |
L
|     |     |     |           |     |     | X(cid:16)   |           | (cid:17) | X(cid:16) |         | (cid:17) |     |
| --- | --- | --- | --------- | --- | --- | ----------- | --------- | -------- | --------- | ------- | -------- | --- |
|     |     |     | L2−E(2!Aˆ |     | )=  |             | L2−E(Lˆ2) | +        | L         | L −E(Lˆ | Lˆ )     |     |
|     |     |     |           |     | 2   |             | j         | j        |           | j k     | j k      |     |
|     |     |     |           |     |     | j=1         |           |          | j6=k      |         |          |     |
|     |     |     |           |     |     | X(cid:16) L |           | (cid:17) |           |         |          |     |
L2−E(Lˆ2)
|     |     |     |     |     | =   |     |     | .   |     |     |     | (21) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     | j   | j   |     |     |     |      |
j=1
| E(Lˆ2)=p |     | L2  |               |     |          |     |     |         |     |     |     |     |
| -------- | --- | --- | ------------- | --- | -------- | --- | --- | ------- | --- | --- | --- | --- |
| Now      |     | j,  | which implies |     | that for | 0<p | ≤1, | we have |     |     |     |     |
|          | j   | jp2 |               |     |          |     | j   |         |     |     |     |     |
j
|     |     |     |     |     |           |     |     | L (cid:18) | (cid:19) |     |     |      |
| --- | --- | --- | --- | --- | --------- | --- | --- | ---------- | -------- | --- | --- | ---- |
|     |     |     |     |     | L2−E(2!Aˆ |     |     | X          | 1        |     |     |      |
|     |     |     |     |     |           |     | )=  | 1−         |          | L2. |     | (22) |
|     |     |     |     |     |           |     | 2   |            | p        | j   |     |      |
j
j=1
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 11

| Since p ≤1, | we  | have |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j
|     |     |     |     |            |     |     |         | L (cid:18) | (cid:19)  |     |     |      |
| --- | --- | --- | --- | ---------- | --- | --- | ------- | ---------- | --------- | --- | --- | ---- |
|     |     |     |     |            |     |     |         | X 1        |           |     |     |      |
|     |     |     |     | kL2−E(2!Aˆ |     |     | )k ≤    |            | −1 (4h2). |     |     | (23) |
|     |     |     |     |            |     | 2   | (cid:5) |            |           | j   |     |      |
p j
j=1
| Since B =L2/2!, |     | we get | the upper | bound |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|     |     |     |     |         |       |     |               | s2 L | (cid:18) 1 | (cid:19) |     |      |
| --- | --- | --- | --- | ------- | ----- | --- | ------------- | ---- | ---------- | -------- | --- | ---- |
|     |     |     |     | ks2E(Aˆ | )−s2B |     |               | X    |            | h2       |     |      |
|     |     |     |     |         | 2     |     | 2 k (cid:5) = | 4    | −1         |          |     |      |
|     |     |     |     |         |       |     |               | 2!   | p          | j        |     |      |
|     |     |     |     |         |       |     |               | j=1  | j          |          |     |      |
|     |     |     |     |         |       |     |               | L    | (cid:18)   | (cid:19) |     |      |
|     |     |     |     |         |       |     |               | X    | 1          |          |     |      |
|     |     |     |     |         |       |     | =2s2          |      | −1         | h2,      |     | (24) |
|     |     |     |     |         |       |     |               |      | p          | j        |     |      |
j
j=1
| where s=tµ/G. |            | Multiplying | this | by    | r =G/µ | gives | us  | (cid:15) 1 . |     |     |     |     |
| ------------- | ---------- | ----------- | ---- | ----- | ------ | ----- | --- | ------------ | --- | --- | --- | --- |
| To evaluate   | (cid:15) , | we proceed  | to   | write |        |       |     |              |     |     |     |     |
2
L3−E(3!Aˆ
|     |     |     |     |     |     | 3 )=D | 1 +D | 2 +D | 3 +D 4 | +D 5 , |     | (25) |
| --- | --- | --- | --- | --- | --- | ----- | ---- | ---- | ------ | ------ | --- | ---- |
where
L
|     |     |     | X(cid:16) |     | (cid:17) |     |     |     |     |     |     |      |
| --- | --- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | ---- |
|     |     | D = | L3−E(Lˆ3) |     |          | ,   |     |     |     |     |     | (26) |
|     |     | 1   |           | j   | j        |     |     |     |     |     |     |      |
j=1
|     |     |     | X(cid:16) |          |     | (cid:17) |     |     |     |     |     |      |
| --- | --- | --- | --------- | -------- | --- | -------- | --- | --- | --- | --- | --- | ---- |
|     |     | D = | L2L       | −E(Lˆ2Lˆ |     | ) ,      |     |     |     |     |     | (27) |
|     |     | 2   |           | j k      | j   | k        |     |     |     |     |     |      |
j6=k
|     |     |     | X(cid:16) | −E(Lˆ |     | Lˆ2) (cid:17) |     |     |     |     |     |      |
| --- | --- | --- | --------- | ----- | --- | ------------- | --- | --- | --- | --- | --- | ---- |
|     |     | D = | L         | L2    |     | ,             |     |     |     |     |     | (28) |
|     |     | 3   |           | j k   | j   | k             |     |     |     |     |     |      |
j6=k
|     |     |       | X (cid:18) |         | 1   |         |     | (cid:19) |     |     |     |      |
| --- | --- | ----- | ---------- | ------- | --- | ------- | --- | -------- | --- | --- | --- | ---- |
|     |     |       |            |         |     | E(Lˆ2Lˆ | +Lˆ | Lˆ2)     |     |     |     |      |
|     |     | D 4 = | L          | j L k L | j − | j       | k   | j k ,    |     |     |     | (29) |
2
j6=k
|     |     |     | X         |     |     |           | X   |       |           | X   |              |      |
| --- | --- | --- | --------- | --- | --- | --------- | --- | ----- | --------- | --- | ------------ | ---- |
|     |     | D = |           | L   | L L | +         |     | L L L | −2        |     | E(Lˆ Lˆ Lˆ). | (30) |
|     |     | 5   |           |     | j k | l         |     | j k   | l         |     | j k l        |      |
|     |     |     | 1≤k<j<l≤L |     |     | 1≤j<l<k≤L |     |       | 1≤j<k<l≤L |     |              |      |
|     |     |     | 1≤k<l<j≤L |     |     | 1≤l<j<k≤L |     |       | 1≤l<k<j≤L |     |              |      |
L3
We now proceed to simplify D for j =1,...,5. Note that E(Lˆ3)=p j. This implies that
|     |     |     | j   |     |     |     |     |     | j jp3 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
j
|     |     |     |     |     |     |     |     | !   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L
|     |     |     |     |     |     |     | X   | 1   |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | D = | 1−  |     | L3. |     |     | (31) |
|     |     |     |     |     |     | 1   |     | p2  | j   |     |     |      |
j
j=1
Next, multiplicativity of the expectation for independent random variables implies that
|     |     |     |     |     |     |     | (cid:18) | (cid:19) |     |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --- | --- | ---- |
|     |     |     |     |     |     | X   |          | 1        |     |     |     |      |
|     |     |     |     |     | D   | =   | 1−       | L2L      | ,   |     |     | (32) |
|     |     |     |     |     |     | 2   |          | p        | j k |     |     |      |
j
j6=k
|            |       |                |          |     |     |             | (cid:18)     | 1 (cid:19) |          |     |          |      |
| ---------- | ----- | -------------- | -------- | --- | --- | ----------- | ------------ | ---------- | -------- | --- | -------- | ---- |
|            |       |                |          |     |     | X           |              |            | L2.      |     |          |      |
|            |       |                |          |     | D   | 3 =         | 1−           | L          | j        |     |          | (33) |
|            |       |                |          |     |     |             |              | p          | k        |     |          |      |
|            |       |                |          |     |     | j6=k        |              | k          |          |     |          |      |
| Now we can | write |                |          |     |     |             |              |            |          |     |          |      |
|            |       |                |          |     |     |             |              |            | (cid:18) |     | (cid:19) |      |
|            |       |                | 1X       |     |     | 1X          |              | X          | 1        |     |          |      |
|            |       | D              | =        | L   | L L | +           | L L          | L −        | E(Lˆ2Lˆ  | +Lˆ | Lˆ2) .   | (34) |
|            |       |                | 4        | j   | k j |             | k            | j k        |          | j k | j k      |      |
|            |       |                | 2        |     |     | 2           |              |            | 2        |     |          |      |
|            |       |                | j6=k     |     |     | j6=k        |              | j6=k       |          |     |          |      |
|            |       | (cid:16) Lˆ2Lˆ | (cid:17) |     |     | (cid:16) Lˆ | Lˆ2 (cid:17) |            |          |     |          |      |
Clearly, we have E =L2L /p and E =L L2/p . Next by swapping the roles of j and k in the
|            |        | j k |     | j k | j    | j    | k   | j k  | k    |     |     |     |
| ---------- | ------ | --- | --- | --- | ---- | ---- | --- | ---- | ---- | --- | --- | --- |
| summation, | we get |     |     |     |      |      |     |      |      |     |     |     |
|            |        |     |     |     | X    | L2/p |     | X    | L2/p |     |     |     |
|            |        |     |     |     |      | L j  | k = | L k  | j .  |     |     |     |
|            |        |     |     |     |      |      | k   |      | j    |     |     |     |
|            |        |     |     |     | j6=k |      |     | j6=k |      |     |     |     |
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 12

By pairing the first term with the third term and the second term with the fourth term in (34), this implies
that
1X 1X
D = L (L L −L L /p )+ (L L −L L /p )L , (35)
4 2 j k j j k j 2 j k k j k k
j6=k j6=k
where we swap the roles of j and k in the second sum. From the above, we can see that
L !
X 1
kD k ≤ −1 8h3, (36)
1 (cid:5) p2 j
j=1 j
(cid:18) (cid:19)
X 1
kD k ≤ −1 8h2h , (37)
2 (cid:5) p j k
j
j6=k
(cid:18) (cid:19)
X 1
kD k ≤ −1 8h h2, (38)
3 (cid:5) p j k
k
j6=k
(cid:18) (cid:19)
X 1
kD k ≤ 1+ 8h2h . (39)
4 (cid:5) p j k
j
j6=k
From this, we can obtain the first two terms in (cid:15) . To see this, note that
2
L !
1 4X 1
kD k ≤ −1 h3, (40)
3! 1 (cid:5) 3 p2 j
j=1 j
and
4 (cid:18) (cid:19)
1 X 4X 1
kD k ≤ 3 −1 h2h . (41)
3! i (cid:5) 3 p j k
j
i=2 j6=k
Multiplying the right sides of (40) and (41) by r gives the first two terms in (cid:15) .
2
We proceed to simplify D . Note from (30) that
5
X X X
D = L L L + L L L + L L L (42)
5 j k l j k l j k l
1≤k<j<l≤L 1≤k<l<j≤L 1≤j<l<k≤L
X X X
+ L L L −2 L L L −2 L L L .
j k l j k l j k l
1≤l<j<k≤L 1≤j<k<l≤L 1≤l<k<j≤L
Now by ordering all the indices in the same way we get
X X X
D = L L L + L L L + L L L
5 k j l l j k j l k
1≤j<k<l≤L 1≤j<k<l≤L 1≤j<k<l≤L
X X
+ L L L −2 (L L L +L L L ). (43)
k l j j k l l k j
1≤j<k<l≤L 1≤j<k<l≤L
By pairing the first term with the fifth term, and the third term with the fifth term in (43), we get L L L −
k j l
L L L =[L ,L ]L andL L L −L L L =L [L ,L ]. Bypairingthesecondtermwiththesixthterm,andthe
j k l k j l j l k j k l j l k
fourthtermwiththesixthtermin(43),wegetL L L −L L L =L [L ,L ]andL L L −L L L =[L ,L ]L .
l j k l k j l j k k l j l k j k l j
We can thus rewrite (43) as
X
D = ([L ,L ]L +L [L ,L ]+L [L ,L ]+[L ,L ]L ) (44)
5 k j l j l k l j k k l j
1≤j<k<l≤L
Collecting the terms in the above summation in terms of commutators again, we get
X
D = ([L ,[L ,L ]]+[[L ,L ],L ]). (45)
5 l j k k l j
1≤j<k<l≤L
A trivial upper bound on the diamond norm of this is
8
kD k ≤8 S(h,h,h), (46)
5 (cid:5) 6
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 13

where the first factor of 8 arises from going from the diamond norm of the Liovillean L to the operator norm
j
of H , and the numerator 8 in the fraction arises from the total number of summations over non-decreasing
j
indices, and 6 arises from the number of ways to permute the indices j,k and l. From the bounds we have on
| the | diamond | norms | of D | ,D ,D | ,D           | and D | , we     | obtain           |      |                |     |     |      |
| --- | ------- | ----- | ---- | ----- | ------------ | ----- | -------- | ---------------- | ---- | -------------- | --- | --- | ---- |
|     |         |       | 1    | 2     | 3 4          |       | 5        |                  |      |                |     |     |      |
|     |         |       |      |       | 1 (cid:13)   |       | (cid:16) | (cid:17)(cid:13) | 1X 5 |                |     |     |      |
|     |         |       |      |       | (cid:13)L3−E |       | 3!Aˆ     | (cid:13)         |      |                |     |     |      |
|     |         |       |      |       |              |       |          | ≤                |      | kD k =(cid:15) | /r. |     | (47) |
|     |         |       |      |       | 3!(cid:13)   |       | 3        | (cid:13)         | 6    | j (cid:5)      | 2   |     |      |
(cid:5)
j=1
Multiplying this by r gives us the error in (cid:15) that is O(t3µ2/G2). We have thus completed bounding the leading
| order | errors | in Theorem  |            | 5.          |     |                  |              |            |     |          |     |     |     |
| ----- | ------ | ----------- | ---------- | ----------- | --- | ---------------- | ------------ | ---------- | --- | -------- | --- | --- | --- |
| A.4   | Tail   | bounds      | in Theorem |             | 1   |                  |              |            |     |          |     |     |     |
| Here, | we     | explain how | the        | tail bounds |     | (cid:15) 3,1 and | (cid:15) 3,2 | in Theorem |     | 5 arise. |     |     |     |
P
Toevaluatethehigherordertermsin(cid:15), weconsideraconvergentpowerseriesinθ givenbyF = f θk.
θ k≥0 k
Here,f isindependentofθ,andF andf belongtoaBanachalgebra. Define[θj]F =f asthejthcoefficient
|     | k   |     |     |     | θ   | k   |     |     |     |     |     | θ j |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in the power series expansion of F . A useful technique to bound quantities in a Banach algebra relies on the
θ
fundamental theorem of calculus, and has been used for example in Ref [10] and Ref [8]. This for example can
be used to obtain the well-known integral form of the remainder term of the Taylor series of the power series
| F   | where | s>0. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s
P
Lemma 6. Let θ =1,s>0 and F = f sk. For every positive integer t, we have
|     |     | 0   |     |     | s   | k≥0 | k    |     |        |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --- | --- | --- | --- |
|     |     |     |     |     |     |     | Z θ0 |     | Z θt−1 | dt  |     |     |     |
X
|     |     |     |     |     |     | f sk | =   | dθ ··· |     | dθ F | .   |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------ | --- | ---- | --- | --- | --- |
|     |     |     |     |     |     | k    |     | 1      |     | tdθ  | sθt |     |     |
|     |     |     |     |     |     |      | 0   |        | 0   | t    |     |     |     |
k≥t
Proof. The proof of this is well-known but we provide the complete details for completeness. We first note that
dt F = P f (sθ )k−tk , where k =(k)...(k−t+1) denotes the falling factorial.
|     | sθt | k   | t   | t   |     | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dθt |     | k≥t |     |     |     |     |     |     |     |     |     |     |     |
Applying the fundamental theorem of calculus on monomials in θ , we have
t
|     |     |     |     |     | Z    |     |     | Z    |     |       |       |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | ----- | ----- | --- | --- |
|     |     |     |     |     | θt−1 | dt  |     | θt−1 | X   |       |       |     |     |
|     |     |     |     |     |      | dθ  | F = |      | dθ  | f (sθ | )k−tk |     |     |
|     |     |     |     |     |      | tdθ | sθt |      | t   | k t   | t     |     |     |
t
|     |     |     |     |     | 0   |     |     | 0   | k≥t |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X
|     |     |     |     |     |     |     | =   | f   | sk−tθk−t−1k |         | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | k           | t−1 t−1 |     |     |     |
k≥t
| Applying |     | this argument | iteratively |     | gives | the | result. |     |     |     |     |     |     |
| -------- | --- | ------------- | ----------- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
Now let us denote a single timeslice of the ideal channel and SparSto for time sθ as U = esθL and
θ
| Eˆ  | 1(esθLˆ | 1...esθLˆ | +esθLˆ | L...esθLˆ |     |     |     |     |     |     |     |     |     |
| --- | ------- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sθ = L 1) respectively. We proceed to evaluate the fourth derivatives of a single
2
| timeslice |     | of U and | Vˆ , which | are | respectively |     | given | by  |     |     |     |     |     |
| --------- | --- | -------- | ---------- | --- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
|           |     | θ        | θ          |     |              |     |       |     |     |     |     |     |     |
d4
=(sL)4U
|     |     |     |     | U   | θ   | θ   | ,   |     |     |     |     |     | (48) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
dθ4
|     |     |     |     | d4  | s4  |     | (cid:18) | 4      | (cid:19)  |               |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | ------------- | --- | --- | --- |
|     |     |     |     | Eˆ  |     | X   |          |        | Lˆn1esθLˆ | 1...LˆnLesθLˆ |     |     |     |
|     |     |     |     |     | =   |     |          |        |           |               |     | L   |     |
|     |     |     |     | dθ4 | sθ  | 2   | n        | ,...,n |           | 1             | L   |     |     |
|     |     |     |     |     |     |     |          | 1      | L         |               |     |     |     |
n1+···+nL=4
n1,...,nL∈N
|     |     |     |     |     | s4  |     | (cid:18) | 4      | (cid:19)  |               |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | ------------- | --- | --- | ---- |
|     |     |     |     |     |     | X   |          |        | LˆnLesθLˆ | L...Lˆn1esθLˆ |     |     |      |
|     |     |     |     |     | +   |     |          |        |           |               |     | 1,  | (49) |
|     |     |     |     |     |     | 2   | n        | ,...,n |           | L             | 1   |     |      |
|     |     |     |     |     |     |     |          | 1      | L         |               |     |     |      |
n1+···+nL=4
n1,...,nL∈N
|     |     |     |     |     |     |     |     |     |     |     | (cid:0) 4 | (cid:1) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --- |
where in the second equation we used the general Leibniz rule and the =4!/(n 1 !...n L !) denotes the
n1,...,nL
multinomial coefficient. The diamond norm of the tail of U is therefore at most
θ
|     |     |     |     |     |     | s4   |     | s4         |      |                   |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---------- | ---- | ----------------- | --- | --- | --- |
|     |     |     |     |     |     | kL4U | k   | ≤          | kL4k | kU k              |     |     |     |
|     |     |     |     |     |     | 4!   | θ   | (cid:5) 4! |      | (cid:5) θ (cid:5) |     |     |     |
(2s)4
|     |     |     |     |     |     |     |     | ≤   | λ4kU | k   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
θ (cid:5)
4!
(2sλ)4
|     |     |     |     |     |     |     |     | =   | ,   |     |     |     | (50) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
4!
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 14

| where the | last equality |     | arises | because | U   | is a quantum |     | channel. |     |     |     |     |     |
| --------- | ------------- | --- | ------ | ------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
θ
| Now note | that | by the | linearity | of  | the derivative |          | and        | expectation | operator,   |               |     |     |     |
| -------- | ---- | ------ | --------- | --- | -------------- | -------- | ---------- | ----------- | ----------- | ------------- | --- | --- | --- |
|          |      |        |           |     |                | (cid:18) |            | (cid:19)    |             |               |     |     |     |
|          |      |        | d4        |     | s4 X           |          | 4          |             |             |               |     |     |     |
|          |      |        | E(Eˆ      | )=  |                |          |            |             | E(Lˆn1esθLˆ | 1...LˆnLesθLˆ |     | L)  |     |
|          |      |        |           | sθ  |                |          |            |             | 1           |               | L   |     |     |
|          |      | dθ4    |           |     | 2              |          | n 1 ,...,n | L           |             |               |     |     |     |
n1+···+nL=4
n1,...,nL∈N
|     |     |     |     |     |     |     | (cid:18) |        | (cid:19)    |     |               |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --- | ------------- | --- | ---- |
|     |     |     |     |     | s4  | X   |          | 4      |             |     |               |     |      |
|     |     |     |     |     | +   |     |          |        | E(LˆnLesθLˆ |     | L...Lˆn1esθLˆ | 1). | (51) |
|     |     |     |     |     |     |     |          |        | L           |     | 1             |     |      |
|     |     |     |     |     | 2   |     | n 1      | ,...,n | L           |     |               |     |      |
n1+···+nL=4
n1,...,nL∈N
By the independence of every stochastic Trotter step, the expectation is multiplicative so that
|     |     | d4  |      | s4  |     | (cid:18) |          | (cid:19)    |     |                  |     |     |     |
| --- | --- | --- | ---- | --- | --- | -------- | -------- | ----------- | --- | ---------------- | --- | --- | --- |
|     |     |     | E(Eˆ |     | X   |          | 4        | E(Lˆn1esθLˆ |     | 1)...E(LˆnLesθLˆ |     |     |     |
|     |     |     |      | )=  |     |          |          |             |     |                  |     | L)  |     |
|     |     | dθ4 | sθ   | 2   |     |          | n ,...,n |             | 1   |                  | L   |     |     |
|     |     |     |      |     |     |          | 1        | L           |     |                  |     |     |     |
n1+···+nL=4
n1,...,nL∈N
|     |     |     |     |     | s4  |     | (cid:18) | 4   | (cid:19)    |                  |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | ---------------- | --- | --- | ---- |
|     |     |     |     |     |     | X   |          |     | E(LˆnLesθLˆ | L)...E(Lˆn1esθLˆ |     |     |      |
|     |     |     |     | +   |     |     |          |     |             |                  |     | 1). | (52) |
|     |     |     |     |     | 2   |     | n ,...,n |     | L           |                  | 1   |     |      |
|     |     |     |     |     |     |     | 1        | L   |             |                  |     |     |      |
n1+···+nL=4
n1,...,nL∈N
Using the triangle inequality and the submultiplicativity of the diamond norm, the diamond norm of the tail of
Eˆ
sθ is at most
|     |     |     |     |     | s4(cid:0) | 4 (cid:1) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
X
|     |     |     |     |     | n1,...,nL |     | kE(Lˆn1esθLˆ | 1)k | ...kE(LˆnLesθLˆ |     | L)k     | .   | (53) |
| --- | --- | --- | --- | --- | --------- | --- | ------------ | --- | --------------- | --- | ------- | --- | ---- |
|     |     |     |     |     |           |     | 1            |     | (cid:5)         | L   | (cid:5) |     |      |
4!
n1+···+nL=4
n1,...,nL∈N
When n j ≥1, we appeal to the Taylor series expansion for the exponential function, to get
|     |     |     |     |     |     |     |    |     |     |    |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X(sθ)k
|     |     |     |     |     | E(LˆnjesθLˆ | j)=E |     |     | Lˆk+nj |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | ----- | --- | --- | ------- | --- | --- | --- | --- |
|     |     |     |     |     | j           |       |     |     | j       |     |     |     |     |
k!
k≥0
X(sθ)k
|     |     |     |     |     |     |     | =   |     | E(Lˆk+nj) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
j
k!
k≥0
X(sθ)k
Lk+nj/pk+nj−1
=
|     |     |     |     |     |     |     |     | k!  | j   | j   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k≥0
|     |     |     |     |     |     |     | =p (L | /p )njesθLj/pj. |     |     |     |     | (54) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     | j     | j j             |     |     |     |     |      |
It is clear that (54) also holds when n =0. Using (54), we get the upper bound
j
kE(LˆnjesθLˆ
|     |     |     |     |     |     |     | j)k     | ≤p (kL | k /p      | )nj. |     |     | (55) |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | ---- | --- | --- | ---- |
|     |     |     |     |     |     | j   | (cid:5) | j      | j (cid:5) | j    |     |     |      |
Using (55) with the multinomial theorem on (53), the diamond norm of the tail of Eˆ is at most
sθ
|     |     |     |     | s4(p | ...p | )   |           |         |     |           |     |     |      |
| --- | --- | --- | --- | ---- | ---- | --- | --------- | ------- | --- | --------- | --- | --- | ---- |
|     |     |     |     |      | 1    | L   |           |         |     |           | )4. |     |      |
|     |     |     |     |      |      | (kL | k /p      | +···+kL |     | k /p      |     |     | (56) |
|     |     |     |     |      | 4!   |     | 1 (cid:5) | 1       | L   | (cid:5) L |     |     |      |
Eˆ
Applying the identity kL k ≤2h , we find that the diamond norm of the tail of is at most
|     |     |     | j (cid:5) | j   |         |      |      |           |     |        |     | sθ  |      |
| --- | --- | --- | --------- | --- | ------- | ---- | ---- | --------- | --- | ------ | --- | --- | ---- |
|     |     |     |           |     | (2s)4(p | ...p | )    |           |     |        |     |     |      |
|     |     |     |           |     |         | 1    | L (h | /p +···+h |     | /p )4. |     |     | (57) |
|     |     |     |           |     |         |      |      | 1 1       | L   | L      |     |     |      |
4!
By setting θ = 1 and multiplying the results that we obtained from the tail bounds on a single timeslice s by
a factor of r, we thus find that the expected contribution to the simulation error from the tail bounds on r
esL Eˆ
| repeats of | and | s is | at most | (cid:15) 3,1 | and | (cid:15) 3,2 respectively, |     | where |     |     |     |     |     |
| ---------- | --- | ---- | ------- | ------------ | --- | -------------------------- | --- | ----- | --- | --- | --- | --- | --- |
24rs4
|     |     |     |     | (cid:15) | =   | λ4  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 3,1      | 4!  |     |     |     |     |     |     |     |     |
24rs4
|     |     |     |     | (cid:15) | =   | (p  | ...p | )(h /p | +···+h | /p  | )), |     | (58) |
| --- | --- | --- | --- | -------- | --- | --- | ---- | ------ | ------ | --- | --- | --- | ---- |
|     |     |     |     | 3,2      |     | 1   | L    | 1      | 1      | L   | L   |     |      |
4!
| from which | the | result follows. |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 15

| B   | Convex |     | programming |     |     | on leading | order |     | error terms |     |     |
| --- | ------ | --- | ----------- | --- | --- | ---------- | ----- | --- | ----------- | --- | --- |
Here we minimise the leading order term in the simulation error by optimizing over the probabilities p . In
j
particular, by restricting our minimisation to only the leading order term of (cid:15) in (cid:15), we find that the leading
1
rs2PL
| order | simulation |     | error | is  |     | h2/p . |     |     |     |     |     |
| ----- | ---------- | --- | ----- | --- | --- | ------ | --- | --- | --- | --- | --- |
|       |            |     |       |     | j=1 | j j    |     |     |     |     |     |
ThewaywefindtheoptimalprobabilityisbytakingthederivativeofthecorrespondingLagrangianfunction,
and thereby determine its turning points. If the primal and dual solutions are furthermore feasible and satisfy
complementaryslackness,thenweknowfromtheconvexityofourproblemthattheseprimalanddualsolutions
| are | optimal | for | the primal | and | dual | optimisation | problems |     | respectively. |     |     |
| --- | ------- | --- | ---------- | --- | ---- | ------------ | -------- | --- | ------------- | --- | --- |
More formally, in convex optimisation theory, we know that a primal problem and its dual problem are both
optimal if and only if (1) Slater’s constraint qualification holds, and (2) the primal and dual variables satisfy
the so-called Karush-Kuhn-Tucker (KKT) conditions [32]. Of these two conditions (1) easily holds. The notion
oftheactivesetappearsinoneoftheoptimalityconditionsof(2), whichisknownascomplementaryslackness.
Nowweonlyoptimizeoverthep forwhichjbelongstotheinactivesetA¯. Henceweconsidertheoptimisation
j
problem
|     |     |     |     |     |     |     |     |     | X h2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     |     |     |     |     |     | rs2  | j   |     |
minimize
|     |     |     |     |     |     |     |          | ∈A¯ | p    |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --- | --- |
|     |     |     |     |     |     |     | p j >0,j |     | j∈A¯ | j   |     |
X
(59)
|     |     |     |     |     |     |     | subject | to  | p j =µ¯, |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- | --- |
j∈A¯
p ≤1,
j
where µ¯ =µ−|A|. Note that the objective function here is convex in p , and the constraint function is linear
j
in p . By treating µ¯ as a constant, we analytically derive the optimal value of this optimisation problem from
j
the first order KKT conditions [32]. Since Slater’s condition is satisfied, the KKT condition is necessary and
sufficient for optimality. The KKT conditions require (1) the turning points of the Lagrangian to be zero,
(2) primal feasibility, (3) feasibility of the Lagrange dual, (4) and complementary slackness. Complementary
slackness requires the Lagrange multiplier of a constraint to be zero when that constraint is not tight.
Denoting u as the Lagrange multiplier for the equality constraint and v j as Lagrange multipliers for the
| inequality |     | constraints, |     | the Lagrangian |     | of (59) | is  |     |     |     |     |
| ---------- | --- | ------------ | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- |
|            |     |              |     |                |     |         |    |     |    |     |     |
2
|     |     |     |     |     |       | X   | h     | X   |       | X       |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | ------- | --- |
|     |     |     |     |     | L=rs2 |     | j +u | p   | −µ¯+ | (p −1)v |     |
|     |     |     |     |     |       |     |       | j   |       | j j     |     |
p j
|     |     |     |     |     |     | j∈A¯ |     | j∈A¯ |     | j∈A¯ |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- |
|     |     |     |     |     |     |      |     |      | !   |      |     |
rs2h2
|     |     |     |     |     |     | X   | j     |      |        |       |      |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ | ----- | ---- |
|     |     |     |     |     | =   |     | +(u+v | j )p | j −v j | −uµ¯. | (60) |
p
|     |     |     |     |     |     | j∈A¯ | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Note that
|     |     |     |     |     |     |     | ∂L −rs2h2 |     |      |     |      |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---- | --- | ---- |
|     |     |     |     |     |     |     | =         | j   | +u+v | ,   | (61) |
|     |     |     |     |     |     |     |           | p2  |      | j   |      |
∂p j
j
| and | hence | the turning |     | point | of the | Lagrangian | L occurs | when |     |     |     |
| --- | ----- | ----------- | --- | ----- | ------ | ---------- | -------- | ---- | --- | --- | --- |
√
rsh
|     |     |     |     |     |     |     | p = | √   | j . |     | (62) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
j
|     |     |     |     |     |     |     |     | u+v | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Note that we have u∈R and v ≥0. From complementary slackness, we know that if the optimal p <1, then
|     |     |     |     |     | j   |     |     |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
we correspondingly have v j =0. When p j =1, the constraint corresponding to v j is active, and v j >0. Hence
| it  | follows | that whenever |     | p <1, | we  | have |     |     |     |     |     |
| --- | ------- | ------------- | --- | ----- | --- | ---- | --- | --- | --- | --- | --- |
j
|             |     |      |       |     |      |     | √   | √   |         |     |      |
| ----------- | --- | ---- | ----- | --- | ---- | --- | --- | --- | ------- | --- | ---- |
|             |     |      |       |     |      |     | up  | j = | rsh j . |     | (63) |
| Conversely, |     | when | p =1, | we  | have |     |     |     |         |     |      |
j
|     |     |     |     |     |     |     | u+v | =rs2h2. |     |     | (64) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---- |
|     |     |     |     |     |     |     |     | j       | j   |     |      |
Note here that we have not verified that the problem is primal feasible, namely, that we need to check that
P
|     | p   | =µ¯. This | can | be satisfied |     | whenever | we have |     |     |     |     |
| --- | --- | --------- | --- | ------------ | --- | -------- | ------- | --- | --- | --- | --- |
j∈A¯ j
r r
X
|     |     |     |     |     |     |     | µ¯ =s |     | h j . |     | (65) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ---- |
u
j∈A¯
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 16

| Thus our ansatz | for p is |     |     |     |     |
| --------------- | -------- | --- | --- | --- | --- |
j
µ¯h
|     |     |     | p = | j , | (66) |
| --- | --- | --- | --- | --- | ---- |
j P
|                     |                |              | j∈A¯        | h j           |     |
| ------------------- | -------------- | ------------ | ----------- | ------------- | --- |
| with the regularity | condition that | this formula | satisfies p | <1 for j ∈A¯. |     |
j
AcceptedinQuantum2020-02-17,clicktitletoverify. PublishedunderCC-BY4.0. 17
