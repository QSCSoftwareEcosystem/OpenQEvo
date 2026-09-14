| Faster      |     | quantum         |          |                 | simulation  |     | by           | randomization |     |
| ----------- | --- | --------------- | -------- | --------------- | ----------- | --- | ------------ | ------------- | --- |
| Andrew      |     | M. Childs1,2,3, | Aaron    | Ostrander2,3,4, |             | and | Yuan Su1,2,3 |               |     |
| 1Department |     | of Computer     | Science, | University      | of Maryland |     |              |               |     |
2Institute
|     |     | for Advanced | Computer | Studies, | University | of Maryland |     |     |     |
| --- | --- | ------------ | -------- | -------- | ---------- | ----------- | --- | --- | --- |
3Joint
|             | Center | for Quantum | Information |     | and Computer | Science, | University | of Maryland |     |
| ----------- | ------ | ----------- | ----------- | --- | ------------ | -------- | ---------- | ----------- | --- |
| 4Department |        | of Physics, | University  | of  | Maryland     |          |            |             |     |
9102 guA 82  ]hp-tnauq[  2v58380.5081:viXra ProductformulascanbeusedtosimulateHamiltoniandynamicsonaquan-
tum computer by approximating the exponential of a sum of operators by a
product of exponentials of the individual summands. This approach is both
straightforward and surprisingly efficient. We show that by simply random-
izing how the summands are ordered, one can prove stronger bounds on the
quality of approximation for product formulas of any given order, and thereby
give more efficient simulations. Indeed, we show that these bounds can be
asymptotically better than previous bounds that exploit commutation between
the summands, despite using much less information about the structure of the
Hamiltonian. Numerical evidence suggests that the randomized approach has
|     | better | empirical | performance |     | as well. |     |     |     |     |
| --- | ------ | --------- | ----------- | --- | -------- | --- | --- | --- | --- |
1 Introduction
Simulating quantum dynamics is one of the major potential applications of quantum com-
puters. The apparent intractability of simulating quantum dynamics with a classical com-
puter led Feynman [19] and others to propose the idea of quantum computation. Lloyd
gave the first explicit quantum algorithm for simulating the dynamics of local Hamiltoni-
ans [25], and later work showed that the more general class of sparse Hamiltonians can
also be simulated efficiently [1]. Quantum simulation can be applied to understand the
behavior of various physical systems—including many-body physics [31], quantum chem-
istry [2, 30, 36], and quantum field theory [23]—and designing new quantum algorithms
| [9, | 11, | 16, 18, 21]. |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
The main ingredient in Lloyd’s algorithm is the Lie product formula, which provides a
first-order approximation to the exponential of a sum as a product of exponentials of the
summands. Given Hermitian operators H 1 ,...,H (which we refer to as the summands
L
of the Hamiltonian H = PL H ) and a complex number λ, the Lie product formula
|     |     |     |     | j=1 | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L
Y
|     |     |     |     |     | S (λ) := | exp(λH | ),  |     | (1) |
| --- | --- | --- | --- | --- | -------- | ------ | --- | --- | --- |
|     |     |     |     |     | 1        |        | j   |     |     |
j=1
| approximates |     | the | exponentiation |     |     |          |            |     |     |
| ------------ | --- | --- | -------------- | --- | --- | -------- | ---------- | --- | --- |
|              |     |     |                |     |     | (cid:18) | L (cid:19) |     |     |
X
|     |     |     |     |     | V(λ) := | exp λ | H   |     | (2) |
| --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- |
j
j=1
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 1

in the sense that V(λ) ≈ S (λ/r)r for large r. Suzuki systematically extended this formula
1
| to give | a (2k)th-order | approximation | S , defined | recursively |     | by  |     |
| ------- | -------------- | ------------- | ----------- | ----------- | --- | --- | --- |
2k
|     |     |          | L                  | 1      |                    |        |     |
| --- | --- | -------- | ------------------ | ------ | ------------------ | ------ | --- |
|     |     |          | (cid:18)λ (cid:19) |        | (cid:18)λ (cid:19) |        |     |
|     |     | :=       | Y                  | Y      |                    |        |     |
|     |     | S 2 (λ)  | exp H j            | exp    | H j                |        |     |
|     |     |          | 2                  |        | 2                  |        | (3) |
|     |     |          | j=1                | j=L    |                    |        |     |
|     |     | S (λ) := | S (p λ)2S          | ((1−4p | )λ)S               | (p λ)2 |     |
|     |     | 2k       | 2k−2 k 2k−2        |        | k 2k−2             | k      |     |
with p := 1/(4 − 41/(2k−1)) [33]. Again we have V(λ) ≈ S (λ/r)r for large r, and
|     | k   |     |     |     |     | 2k  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
the approximation obtained with a given value of r improves as k increases (albeit with a
prefactorthatgrowsexponentiallyink). Werefertoallsuchformulasasproduct formulas.
When they are used for quantum simulation, H is chosen to be the Hamiltonian and
λ = −it, where t is the evolution time. Although other approaches to quantum simulation
have better proven asymptotic performance as a function of various parameters [4, 6–8, 20,
26, 27], product formulas perform well in practice [17] and are widely used in experimental
implementations [3, 12, 24] due to their simplicity and the fact that they do not require
| any ancilla | qubits. |     |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- | --- |
The main challenge in applying product formulas to quantum simulation is to choose
the number of segments r to ensure the simulation error is at most some allowed threshold
PL
(cid:15). To simulate H = H for time t, rigorous error analysis shows that
j=1 j
(cid:18)(tΛL)2(cid:19)
|          |           |               | r =                          | O               |             |     | (4) |
| -------- | --------- | ------------- | ---------------------------- | --------------- | ----------- | --- | --- |
|          |           |               | 1,det                        | (cid:15)        |             |     |     |
| suffices | to ensure | error at most | (cid:15) for the first-order |                 | formula and |     |     |
|          |           |               |                              | (cid:18)(tΛL)1+ | 1 (cid:19)  |     |     |
2 k
|     |     |     | r = O |     |     |     | (5) |
| --- | --- | --- | ----- | --- | --- | --- | --- |
2k,det
(cid:15)2k 1
suffices for (2k)th order [5], where Λ := max kH k is a spectral-norm upper bound on
j j
the summands and det indicates that these formulas are constructed deterministically.
However, numerical simulations suggest that the product formula algorithm can perform
significantlybetterinpracticethanthebestprovenerrorboundsdemonstrate[2,17,31,32].
Indeed,recentworksuggeststhatitcanevenasymptoticallyoutperformmoresophisticated
simulation algorithms with better proven running times [17]. This dramatic gap between
theprovableandtheactualbehaviorofproductformulasimulationsuggeststhatitmaybe
possible to significantly improve their analysis, and thereby give more efficient algorithms
| for quantum | simulation. |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- | --- | --- |
It is sometimes possible to improve the analysis of product formulas using further in-
formation about the form of the Hamiltonian. In particular, the cost of simulation can
be reduced when many pairs of summands commute [2, 17, 25]. However, this approach
canonlybeappliedforstructuredHamiltoniansthatcontainmanycommutingsummands.
Furthermore, the best known bounds of this type give only modest improvement, remain-
ing orders of magnitude away from the empirical performance even in cases where many
| summands | commute | [17]. |     |     |     |     |     |
| -------- | ------- | ----- | --- | --- | --- | --- | --- |
Randomizationcanbeapowerfultoolforimprovingtheperformanceofquantumsimu-
lation algorithms. For example, Poulin et al. gave improved simulations of time-dependent
Hamiltonians by sampling the Hamiltonian at random times [29]. Closer in spirit to the
present paper, Zhang studied the effect of randomizing the ordering and/or duration of
evolutions in a product formula, showing in particular that randomly ordering the sum-
mands in the first-order formula in either forward or reverse order can give an improved
| algorithm | [37]. |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 2

In this paper, we explore a closely related approach for higher-order product formulas,
whichcanachievesignificantlybetterasymptoticperformance. Specifically, weanalyzethe
effect of randomly permuting the summands. The resulting algorithm is not much more
complicated than a deterministic product formula, but the savings in the simulation cost
are substantial. For any permutation σ ∈ Sym(L) of the L summands, let
|     |     |     |       | L   | (cid:18)λ | (cid:19) | 1   | (cid:18)λ | (cid:19) |     |     |     |
| --- | --- | --- | ----- | --- | --------- | -------- | --- | --------- | -------- | --- | --- | --- |
|     |     |     | Sσ(λ) | Y   |           |          | Y   |           |          |     |     |     |
|     |     |     |       | :=  | exp H     |          | exp | H         |          |     |     |     |
|     |     |     | 2     |     | 2         | σ(j)     |     | 2         | σ(j)     |     |     |     |
(6)
|     |           |     |              | j=1    |            |                   | j=L      |               |         |       |                  |     |
| --- | --------- | --- | ------------ | ------ | ---------- | ----------------- | -------- | ------------- | ------- | ----- | ---------------- | --- |
|     |           |     | Sσ (λ)       | := [Sσ | (p λ)]2Sσ  |                   | ((1−4p   | )λ)[Sσ        |         | (p    | λ)]2.            |     |
|     |           |     | 2k           | 2k−2   | k          | 2k−2              |          | k             | 2k−2    | k     |                  |     |
| We  | show that | the | (2k)th-order |        | randomized | simulation        |          | has           | error   |       |                  |     |
|     | (cid:13)  |     |              |        |            |                   | (cid:13) |               |         |       |                  |     |
|     | (cid:13)  |     |              |        |            | (cid:19)r(cid:13) |          |               |         |       |                  |     |
|     |           |     | (cid:18) 1   | X      |            |                   |          | (cid:18)(Λ tL | ) 4k +2 | (Λt)2 | k + 1L2k(cid:19) |     |
(cid:13) V(−it)− S σ (cid:0) −it/r (cid:1) (cid:13) = O + . (7)
|     | (cid:13) |     |          |     | 2 k |     | (cid:13) |     |        |     |       |     |
| --- | -------- | --- | -------- | --- | --- | --- | -------- | --- | ------ | --- | ----- | --- |
|     | (cid:13) |     | L !      |     |     |     | (cid:13) | r   | 4k + 1 |     | r 2 k |     |
|     | (cid:13) |     | σ∈Sym(L) |     |     |     | (cid:13) |     |        |     |       |     |
(cid:5)
where V(−it) and Sσ (−it/r) are quantum channels describing the unitary transformation
2k
V(−it) and the random unitary Sσ (−it/r), respectively, and k·k is the diamond norm
|          |     |         |     |     | 2k  |     |     |     |     | (cid:5) |     |     |
| -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
| (defined | in  | Section | 2). |     |     |     |     |     |     |         |     |     |
Our analysis uses a mixing lemma of Campbell and Hastings [13, 22] to bound the
diamond norm distance from the ideal evolution. (Even for the first-order case, this im-
proves over the analysis of Zhang, which uses similar methods but only bounds the trace
distance from the ideal final state [37], a metric that does not account for entanglement
with a reference system.) Informally, the lemma of [13, 22] states that if we can approxi-
mate a desired operation as the average over some set of operations, then the overall error
depends linearly on the error in the average operation but only quadratically on the error
in any individual operation. Standard error bounds for product formulas do not depend
on how the summands are ordered, but we show that randomizing the ordering gives a
more accurate average evolution. We motivate this approach in Section 2, where we con-
sider the effect of randomizing how the summands are ordered in the simple case of the
first-order formula. Assuming Λ := max kH k is constant, the randomized first-order al-
|     |     |     |     |     |     | j                                   | j   |     |     |     |         |         |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ------- | ------- |
|     |     |     |     |     |     | (cid:0) t1.5L2.5/(cid:15)0.5(cid:1) |     |     |     |     | (cid:0) | (cid:1) |
gorithm has gate complexity grand = O , improving over gdet = O t2L3/(cid:15) in
|     |               |     |       |     | 1   |     |     |     |     |     | 1   |     |
| --- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the | deterministic |     | case. |     |     |     |     |     |     |     |     |     |
Analyzing the effect of randomization on higher-order formulas is more challenging.
For terms of order at most L in the Taylor expansion of a product formula, the majority
of the error comes from terms in which no summands are repeated. We call such contri-
butions nondegenerate terms. In Section 3, we give a combinatorial argument to compute
nondegenerate terms of the average evolution 1 P Sσ (λ) in closed form. (In fact,
|     |     |     |     |     |     |     | L!  | σ∈Sym(L) | 2k  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
we prove a more general result that applies to the average evolution as a special case.) As
a corollary, we show that the nondegenerate terms completely cancel in the randomized
| product | formula. |     |     |     |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Section 4 presents our main technical result, an upper bound on the error in a ran-
domized higher-order product formula simulation. This bound follows by using the mixing
lemmatocombineanerrorboundfortheaverageevolutionoperatorwithstandardproduct
formula error bounds for the error of the individual terms. Section 5 discusses the overall
performanceoftheresultingalgorithmandcomparesitwithdeterministicapproaches. For
:=
the (2k)th-order product formula, assuming Λ max j kH j k is constant, our randomized
| Hamiltonian |     | simulation |       | algorithm | has               | complexity         |       |                   |                   |                  |     |     |
| ----------- | --- | ---------- | ----- | --------- | ----------------- | ------------------ | ----- | ----------------- | ----------------- | ---------------- | --- | --- |
|             |     |            |       |           |                   |                    | 1     |                   |                   | 1                |     |     |
|             |     |            |       |           | (cid:26) (cid:18) | (cid:18)tL(cid:19) |       | (cid:19) (cid:18) | (cid:18)t(cid:19) | (cid:19)(cid:27) |     |     |
|             |     |            | grand |           | tL2               |                    | 4k +1 | tL2               |                   | 2 k              |     |     |
|             |     |            |       | = max     | O                 |                    |       | ,O                |                   |                  | ,   | (8) |
|             |     |            | 2k    |           |                   | (cid:15)           |       |                   | (cid:15)          |                  |     |     |
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 3

|     |     | d et | (cid:0) tL2(tL/(cid:15))2 |     | 1 (cid:1) |     |     |     |     |     |     |
| --- | --- | ---- | ------------------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
compared to g = O k in the deterministic case. Thus our algorithm always
2 k
improves the dependence on L and sometimes achieves better dependence on t and (cid:15) as
well.
We also show in Section 5 that our bound can outperform a previous bound that takes
advantage of the structure of the Hamiltonian. Specifically, we compare our randomized
productformulaalgorithmwiththedeterministicalgorithmusingthecommutatorboundof
[17] for a one-dimensional Heisenberg model in a random magnetic field. We find that over
asignificantrangeofparameters,therandomizedalgorithmhasbetterprovenperformance,
| despite using | less | information |     | about | the | form of | the Hamiltonian. |     |     |     |     |
| ------------- | ---- | ----------- | --- | ----- | --- | ------- | ---------------- | --- | --- | --- | --- |
Inlightofthelargegapbetweenprovenandempiricalperformanceofproductformulas,
it is natural to ask whether randomized product formulas still offer an improvement under
thebestpossibleerrorbounds. Toaddressthisquestion,wepresentnumericalcomparisons
of the deterministic and randomized product formulas in Section 6. In particular, we show
that the randomized approach can sometimes outperform the deterministic approach even
| with respect | to  | their | empirical | performance. |     |     |     |     |     |     |     |
| ------------ | --- | ----- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Finally, we conclude in Section 7 with a brief discussion of the results and some open
questions.
| 2 The | power | of  | randomization |     |     |     |     |     |     |     |     |
| ----- | ----- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
To see how randomness can improve a product formula simulation, consider a simple
Hamiltonian expressed as a sum of two operators, H = H +H . The Taylor expansion of
|                 |     |         |      |          |     |          |     | 1   | 2   |     |     |
| --------------- | --- | ------- | ---- | -------- | --- | -------- | --- | --- | --- | --- | --- |
| the first-order |     | formula | as a | function | of  | λ ∈ C is |     |     |     |     |     |
λ2
|         |            |         |     |     |                 |     |     | (H2+2H |     | +H2)+O(λ3), |     |
| ------- | ---------- | ------- | --- | --- | --------------- | --- | --- | ------ | --- | ----------- | --- |
| S (λ) = | exp(λH     | )exp(λH |     | ) = | I +λ(H          | +H  | )+  |        | H   |             | (9) |
| 1       |            | 1       |     | 2   |                 | 1   | 2 2 | 1      | 1   | 2 2         |     |
| whereas | the Taylor | series  | of  | the | ideal evolution |     | is  |        |     |             |     |
λ2
V(λ) = exp((H +H )λ) = I+λ(H +H )+ (H2+H H +H H +H2)+O(λ3). (10)
|     |     | 1   | 2   |     | 1   | 2   | 1   | 1 2 | 2   | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
Using the triangle inequality, we can bound the spectral-norm error as
|λ|2
+O((Λ|λ|)3),
|     |     |     | kV(λ)−S | 1   | (λ)k ≤ | k[H 1 ,H | 2 ]k |     |     |     | (11) |
| --- | --- | --- | ------- | --- | ------ | -------- | ---- | --- | --- | --- | ---- |
2
where Λ := max{kH k,kH k}. Since H and H need not commute, S (λ) approximates
|         |             |     | 1     | 2         |     | 1   | 2   |     |     | 1   |     |
| ------- | ----------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
| V(λ) to | first order | in  | λ, as | expected. |     |     |     |     |     |     |     |
It is clearly impossible to approximate V(λ) to second order using a product of only
two exponentials of H and H : any such product can have only one of the products H H
|     |     |     | 1   | 2   |     |     |     |     |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and H H in its Taylor expansion, whereas V(λ) contains both of these products in its
| 2   | 1   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
second-order term. However, we can obtain both products by taking a uniform mixture of
S (λ) and
1
|           |         |             |                | Srev(λ) | :=      | exp(λH | )exp(λH         | ).                     |     |     | (12) |
| --------- | ------- | ----------- | -------------- | ------- | ------- | ------ | --------------- | ---------------------- | --- | --- | ---- |
|           |         |             |                | 1       |         |        | 2               | 1                      |     |     |      |
| Indeed, a | simple  | calculation |                | shows   | that    |        |                 |                        |     |     |      |
|           |         |             | (cid:13)       |         | 1       |        | (cid:13)        |                        |     |     |      |
|           |         |             | (cid:13)       |         | (cid:0) | rev(λ) | (cid:1)(cid:13) | (cid:0) (Λ|λ|)3(cid:1) |     |     |      |
|           |         |             | (cid:13) V(λ)− |         | S (λ)+S |        | (cid:13) =      | O                      | .   |     | (13) |
|           |         |             | (cid:13)       |         | 2 1     | 1      | (cid:13)        |                        |     |     |      |
|           | (cid:0) |             |                | (cid:1) |         |        |                 |                        |     |     |      |
However, S (−it) + Srev(−it) /2 is not a unitary operation in general. We could in
|     | 1   |     | 1   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
principle implement a linear combination of unitaries using the techniques of [6], but such
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 4

an approach would use ancillas and could have high cost, especially when the Hamiltonian
contains many summands. A simpler approach is to apply one of the two operations
S (−it) and Srev(−it) chosen uniformly at random (as in Algorithm 2 of [37]), thereby
| 1   |     | 1   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
implementingaquantumchannelthatgivesagoodapproximationtothedesiredevolution.
We now introduce some notation that is useful to analyze the performance of random-
ized product formulas. Let X be a matrix acting on a finite-dimensional Hilbert space
H. We write kXk for its spectral norm (the largest singular value) and kXk for its trace
1
norm (the sum of its singular values, i.e., its Schatten 1-norm). Let E: X 7→ E(X) be a
linear map on the space of matrices on H. The diamond norm of E is
|     |     |     | kEk | :=  | max{k(E | ⊗1  | )(Y)k | : kYk ≤ | 1}, |     | (14) |
| --- | --- | --- | --- | --- | ------- | --- | ----- | ------- | --- | --- | ---- |
H
|     |     |     |     | (cid:5) |     |     |     | 1 1 |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
where the maximization is taken over all matrices Y on H⊗H satisfying kYk ≤ 1.
1
The following mixing lemma bounds how well we can approximate a unitary operation
usingarandomunitarychannel. Specifically, theerrorislinearinthedistancebetweenthe
target unitary and the average of the random unitaries, and only quadratic in the distance
| between | the | target | unitary | and | each individual |     | random | unitary. |     |     |     |
| ------- | --- | ------ | ------- | --- | --------------- | --- | ------ | -------- | --- | --- | --- |
Lemma 1 (Mixing lemma [13, 22]). Let V and {U j } be unitary matrices, with associated
|     |     |     |     | VρV† |     |     |     | ρU†, |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- |
quantum channels V: ρ 7→ and U j : ρ 7→ U j and let {p j } be a collection of
j
| positive | numbers | satisfying |       | P         | p = 1. | Suppose | that |     |     |     |     |
| -------- | ------- | ---------- | ----- | --------- | ------ | ------- | ---- | --- | --- | --- | --- |
|          |         |            |       | j         | j      |         |      |     |     |     |     |
| (i) kU   | −Vk     | ≤          | a for | all j and |        |         |      |     |     |     |     |
j
| (ii) (cid:13) (cid:13)(P | p   | U )−V | (cid:13) ≤ | b.  |     |     |     |     |     |     |     |
| ------------------------ | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                          | j   | j j   | (cid:13)   |     |     |     |     |     |     |     |     |
P
Then the average evolution E := p U satisfies kE −Vk ≤ a2+2b.
|     |     |     |     |     | j   | j j |     | (cid:5) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
To simulate the Hamiltonian H = H +H for time t, we divide the evolution into r
|     |     |     |     |     |     | 1   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
segments of duration t/r and implement each segment via the random unitary operation
1
|     |     |     |     |     | (cid:0) (−it/r)+Srev(−it/r) |     |     | (cid:1) |     |     |      |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------- | --- | --- | ---- |
|     |     |     |     |     | S                           |     |     |         |     |     | (15) |
|     |     |     |     |     | 2 1                         |     | 1   |         |     |     |      |
Srev
using one bit of randomness per segment, where S 1 and are the quantum channels
1
associated with S and Srev. Invoking the mixing lemma with a = O (cid:0) (Λt)2/r2(cid:1) and
|     |     | 1   |     | 1   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0) (Λt)3/r3(cid:1)
| b = O |     | , we     | find | that |         |     |     |                 |                       |     |     |
| ----- | --- | -------- | ---- | ---- | ------- | --- | --- | --------------- | --------------------- | --- | --- |
|       |     | (cid:13) |      |      |         |     |     | (cid:13)        | (cid:18)(Λt)3(cid:19) |     |     |
|       |     | (cid:13) |      | 1    | (cid:0) |     |     | (cid:1)(cid:13) |                       |     |     |
(cid:13) V(−it/r)− S (−it/r)+S rev(−it/r) (cid:13) = O . (16)
|     |     |          |     | 2   | 1   |     | 1   |                  | r3  |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
|     |     | (cid:13) |     |     |     |     |     | (cid:13) (cid:5) |     |     |     |
Since the diamond norm distance between quantum channels is subadditive under compo-
| sition [35, | p.  | 178],            | the error | of      | the entire  | simulation |            | is               |                       |     |      |
| ----------- | --- | ---------------- | --------- | ------- | ----------- | ---------- | ---------- | ---------------- | --------------------- | --- | ---- |
|             |     | (cid:13)         |           | 1       |             |            |            | (cid:13)         | (cid:18)(Λt)3(cid:19) |     |      |
|             |     | (cid:13)         |           | (cid:0) |             |            | rev(−it/r) | (cid:1)r(cid:13) |                       |     |      |
|             |     | (cid:13) V(−it)− |           |         | S (−it/r)+S |            |            | (cid:13) = O     |                       | .   | (17) |
|             |     | (cid:13)         |           | 2r      | 1           |            | 1          | (cid:13)         | r2                    |     |      |
(cid:5)
Thus the randomized first-order formula is effectively a second-order formula.
This approach easily extends to a sum of L operators, again effectively making the
first-order formula accurate to second order (cf. [37], which shows the same result with
respect to trace distance of the output state). Keeping track of all the prefactors, we find
| the following |     | error | bound | for the | randomized |     | first-order | formula. |     |     |     |
| ------------- | --- | ----- | ----- | ------- | ---------- | --- | ----------- | -------- | --- | --- | --- |
Theorem 1 (Randomized first-order error bound). Let {H }L be Hermitian matrices.
j j=1
Let
|     |     |     |     |     |     |     | (cid:18) | L (cid:19) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- | --- |
X
|     |     |     |     |     | V(−it) | := exp | −it | H   |     |     | (18) |
| --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | ---- |
j
j=1
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 5

be the evolution induced by the Hamiltonian H = PL H for time t ∈ R. Define
|     |     |     |     |        |     |         |         | j=1 | j      |      |     |      |
| --- | --- | --- | --- | ------ | --- | ------- | ------- | --- | ------ | ---- | --- | ---- |
|     |     |     |     | L      |     |         |         |     | 1      |      |     |      |
|     |     |     | :=  | Y      |     |         | Srev(λ) | :=  | Y      |      |     |      |
|     |     | S 1 | (λ) | exp(λH |     | j ) and |         |     | exp(λH | j ). |     | (19) |
1
|         |     |            |         | j=1 |       |       |      |      | j=L |     |     |     |
| ------- | --- | ---------- | ------- | --- | ----- | ----- | ---- | ---- | --- | --- | --- | --- |
|         | N   |            |         |     |       | :=    |      |      |     |     |     |     |
| Let r ∈ | be  | a positive | integer |     | and Λ | maxkH | j k. | Then |     |     |     |     |
(cid:13) 1 (cid:13) (Λ|t|L)4 (cid:18) Λ|t|L(cid:19) 2(Λ|t|L)3 (cid:18)Λ|t|L(cid:19)
| (cid:13)         |     | (cid:0)     |     | rev(−it/r) |     | (cid:1)r(cid:13) |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
| (cid:13) V(−it)− |     | S (−it/r)+S |     |            |     | (cid:13)         | ≤   | exp | 2   | +   | exp |     |
| (cid:13)         | 2r  | 1           |     | 1          |     | (cid:13)         | r3  |     | r   | 3r2 |     | r   |
(cid:5)
(20)
where, for λ = −it, we associate channels V(λ), S (λ), and Srev(λ) with the unitaries
|         |      |              |     |               |     |     |     | 1   |     | 1   |     |     |
| ------- | ---- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| V(λ), S | (λ), | and Srev(λ), |     | respectively. |     |     |     |     |     |     |     |     |
|         | 1    |              | 1   |               |     |     |     |     |     |     |     |     |
Toguaranteethatthesimulationerrorisatmost(cid:15), weupperboundtheright-handside
of (20) by (cid:15) and solve for r. Assuming Λ := max kH k is constant, we find that it suffices
|     |     |     |     |     |     |     | j   | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0) (tL)1.5/(cid:15)0.5(cid:1)
to choose rrand = O , giving a simulation algorithm with gate complexity
1
| grand | (cid:0) t1.5L2.5/(cid:15)0.5(cid:1) |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
= O . In comparison, the gate complexity in the deterministic case
1
| gdet | (cid:0) | t2L3/(cid:15) | (cid:1) |     |     |     |     |     |     |     |     |     |
| ---- | ------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is = O . Therefore, the randomized first-order product formula algorithm
1
improves over the deterministic algorithm with respect to all parameters of interest.
It is natural to ask whether a similar randomization strategy can improve higher-order
product formulas (as defined in (3)). While it turns out that randomization does not
improve the order of the formula, it does result in a significant reduction of the error, and
in particular, lowers the dependence on the number of summands in the Hamiltonian. The
more complicated structure of higher-order formulas makes this analysis more involved
than in the first-order case (in particular, we randomly permute the L summands instead
ofsimplychoosingwhetherornottoreversethem, soweuseΘ(LlogL)bitsofrandomness
per segment instead of only a single bit). As discussed at the end of Section 1, our proof
is based on a randomization lemma (established in the next section) that evaluates the
dominant contribution to the Taylor series of the randomized product formula in closed
form.
| 3 Randomization |     |     | lemma |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In this section, we study the Taylor expansion of the average evolution operator obtained
by randomizing how the summands of a Hamiltonian are ordered. We consider a formula
of the form
|     |     |     | exp(q | λH      | )exp(q | λH  | )···exp(q |     | λH      | )   |     |     |
| --- | --- | --- | ----- | ------- | ------ | --- | --------- | --- | ------- | --- | --- | --- |
|     |     |     |       | 1 π1(1) |        | 1   | π1(2)     |     | 1 π1(L) |     |     |     |
|     |     |     | exp(q | λH      | )exp(q | λH  | )···exp(q |     | λH      | )   |     |     |
|     |     |     |       | 2 π2(1) |        | 2   | π2(2)     |     | 2 π2(L) |     |     |     |
(21)
···
|     |     |     | exp(q | κ λH | )exp(q | κ   | λH )···exp(q |     | κ λH  | )   |     |     |
| --- | --- | --- | ----- | ---- | ------ | --- | ------------ | --- | ----- | --- | --- | --- |
|     |     |     |       |      | πκ(1)  |     | πκ(2)        |     | πκ(L) |     |     |     |
|     |     |     |       | R,   |        |     |              | C,  |       |     |     |     |
for real numbers q 1 ,...,q κ ∈ a complex number λ ∈ Hermitian matrices H 1 ,...,H L ,
and permutations π ,...,π ∈ Sym(L). By choosing appropriate values of q ,...,q ∈
|     |     |     | 1   | κ   |     |     |     |     |     |     | 1   | κ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R and ordering H ,...,H in both forward and backward directions, we can write any
|         |         | 1    |        | L    |       |     |     |     |     |     |     |     |
| ------- | ------- | ---- | ------ | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
| product | formula | S 2k | (λ) in | this | form. |     |     |     |     |     |     |     |
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 6

We now permute the summands to get the average evolution
1 X
exp(q λH )exp(q λH )···exp(q λH )
L! 1 σ(π1(1)) 1 σ(π1(2)) 1 σ(π1(L))
σ∈Sym(L)
exp(q λH )exp(q λH )···exp(q λH ) (22)
2 σ(π2(1)) 2 σ(π2(2)) 2 σ(π2(L))
···
exp(q λH )exp(q λH )···exp(q λH ).
κ σ(πκ(1)) κ σ(πκ(2)) κ σ(πκ(L))
In its Taylor expansion, we call the sum of the form
X α λsH ···H , (23)
m1...ms m1 ms
m1,...,ms
pairwisedifferent
with coefficients α ∈ C, the sth-order nondegenerate term. This term contributes
m1...ms
Θ(Ls) to the sth-order error, whereas the remaining (degenerate) terms only contribute
O(Ls−1).
The following lemma shows how to compute the sth-order nondegenerate term for an
arbitrary average evolution.
Lemma 2 (Randomization lemma). Define an average evolution operator as in (22) and
let s ≤ L be a positive integer. The sth-order nondegenerate term of this operator is
[(q 1 +···+q κ )λ]s X
H ···H . (24)
s!
m1 ms
m1,...,ms
pairwise different
Proof. WetakeallpossibleproductsofstermsfromtheTaylorexpansionof(22). Observe
that the exponentials in (22) are organized in an array with κ rows and L columns.
We use κ ,...,κ and l ,...,l to label the row and column indices, respectively, of the
1 s 1 s
exponentials from which the terms are chosen. To avoid double counting, we take terms
with smaller row indices first (i.e., κ ≤ ··· ≤ κ ). Within each row, we take terms with
1 s
smaller column indices first. To get the sth-order nondegenerate term, we require that
π (l ),...,π (l ) are pairwise different. The sth-order nondegenerate term of (22) can
κ1 1 κs s
then be expressed as
1 X X X
(q λH )···(q λH ). (25)
L! κ1 σ(πκ1 (l1)) κs σ(πκs (ls))
σ∈Sym(L)κ1≤···≤κsπκ1 (l1),...,πκs (ls)
pairwisedifferent
A direct calculation shows that
1 X X X
(q λH )···(q λH )
L! κ1 σ(πκ1 (l1)) κs σ(πκs (ls))
σ∈Sym(L) κ1≤···≤κs πκ1 (l1),...,πκs (ls)
pairwisedifferent
1 X X X X
= (q λH )···(q λH )
L!
κ1 m1 κs ms
σ∈Sym(L) κ1≤···≤κs πκ1 (l1),...,πκs (ls) m1=σ(πκ1 (l1)),...,
pairwisedifferent ms=σ(πκs (ls))
1 X X X X
= (q λH )···(q λH )
L!
κ1 m1 κs ms
pair
m
wi
1
s
,
e
..
d
.,
i
m
ffe
s
rent
κ1≤···≤κs πκ1 (l1),...,πκs (ls) σ∈Sym(L):
pairwisedifferent σ(πκ1 (l1))=m1,...,
σ(πκs (ls))=ms
(L−s)! X (cid:20) X X (cid:21)
= (q λ)···(q λ) H ···H .
L!
κ1 κs m1 ms
pair
m
wi
1
s
,
e
..
d
.,
i
m
ffe
s
rent
κ1≤···≤κs πκ1 (l1),...,πκs (ls)
pairwisedifferent
(26)
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 7

Now observe that the summand (q λ)···(q λ) depends only on the row indices. Letting
|     |     |     |     | κ1  |     | κs  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r ,...,r denote the number of terms picked from row 1,...,κ, respectively, we can re-
1 κ
express this summand as (q λ)r1···(q λ)rκ. We determine the coefficient of this term as
|     |     |     |     | 1   | κ   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
follows. The number of ways of choosing l 1 ,...,l s pairwise different is L(L−1)···(L−s+
1). However, when we apply permutations π ,...,π , we may double count some terms.
|     |     |     |     |     |     | κ1  |     | κs  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In particular, if κ = κ , we are to pick terms from the same row κ and we must have
|     |     | i   | i+1 |     |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
l < l . This implies that the ordering of π (l ) and π (l ) is uniquely determined.
| i i+1 |     |     |     |     |     | κi  | i   | κi+1 i+1 |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
Altogether, we see that we have overcounted by a factor of (r !)···(r !). Therefore, we
|     |     |     |     |     |     |     |     | 1   | κ   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
have
L(L−1)···(L−s+1)
| X          |          | X             |               |     |      | X             |      |            |        | λ)r1···(q | λ)rκ |
| ---------- | -------- | ------------- | ------------- | --- | ---- | ------------- | ---- | ---------- | ------ | --------- | ---- |
|            |          |               | (q κ1 λ)···(q | κs  | λ) = |               |      |            |        | (q 1      | κ    |
|            |          |               |               |     |      |               |      | (r !)···(r | !)     |           |      |
|            |          |               |               |     |      | r1 , . . .,r  | :    | 1          | κ      |           |      |
| κ1≤···≤κsπ | κ ( l1   | ) , .. ., π κ | s ( l s )     |     |      |               | κ    |            |        |           |      |
|            | 1        |               |               |     |      | r1+ · · · + r | κ =s |            |        |           |      |
|            | p a ir w | i s e d i ff  | e r e n t     |     |      |               |      |            |        |           |      |
|            |          |               |               |     |      |               |      | [(q        | +···+q | )λ]s      |      |
1 κ
|     |     |     |     |     | =   | L(L−1)···(L−s+1) |     |     |     |     | ,   |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
s!
(27)
| where        | the last | equality | follows   | by the    | multinomial |            | theorem. |     |     |     |     |
| ------------ | -------- | -------- | --------- | --------- | ----------- | ---------- | -------- | --- | --- | --- | --- |
| Substituting |          | (27)     | into (26) | completes |             | the proof. |          |     |     |     |     |
Asanimmediatecorollary,wecomputethesth-ordernondegeneratetermoftheaverage
| evolution | operator |     | 1 P         | Sσ  | (λ). |     |     |     |     |     |     |
| --------- | -------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- |
|           |          |     | L! σ∈Sym(L) | 2k  |      |     |     |     |     |     |     |
Corollary 1. Let {H }L be Hermitian operators; let λ ∈ C, k,s ∈ N, and s ≤ L.
j j=1
Then the sth-order nondegenerate term of the average evolution 1 P Sσ (λ), with
|     |     |     |     |     |     |     |     |     | σ∈Sym(L) | 2k  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
L!
| Sσ (λ) | defined | in (6), | is  |     |     |     |     |     |     |     |     |
| ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2k
λs
X
|     |     |     |     |     |     |     | H ···H | .   |     |     | (28) |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- |
|     |     |     |     | s!  |     |     | m1     | ms  |     |     |      |
m1,...,ms
|     |     |     |     | pairwise | different |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
Sσ
Proof. The fact that (λ) is at least first-order accurate implies that q 1 +···+q κ = 1
2k
in (24).
|     |     |     |     |     |     |     |     | (cid:0) | λPL | (cid:1) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- |
Observethatthesth-ordernondegeneratetermofV(λ) = exp H isalsogiven
j=1 j
by (28). Therefore, the sth-order nondegenerate term completely cancels in
1 X
|     |     |     |     | V(λ)− |     |     | Sσ  | (λ). |     |     | (29) |
| --- | --- | --- | --- | ----- | --- | --- | --- | ---- | --- | --- | ---- |
2k
L!
σ∈Sym(L)
| 4 Error | bounds |     |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In this section we establish our main result, an upper bound on the error of a randomized
product formula simulation. To apply the mixing lemma, we need to bound the error of
the average evolution. We now present an error bound for an arbitrary fixed-order term
| in the | Taylor | expansion | of  | the average | evolution |     | operator. |     |     |     |     |
| ------ | ------ | --------- | --- | ----------- | --------- | --- | --------- | --- | --- | --- | --- |
|        |        |           | }L  |             |           |     |           | C   | N.  |     |     |
Lemma 3. Let {H j be Hermitian operators; let λ ∈ and k,s ∈ Define the target
j=1
evolution V(λ) as in (2), and define the permuted (2k)th-order formula Sσ (λ) as in (6).
2k
| Then the | sth-order |     | error of | the approximation |     |     |     |     |     |     |     |
| -------- | --------- | --- | -------- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |     |     |       |     | X   | Sσ  |     |     |     |      |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | V(λ)− |     |     |     | (λ) |     |     | (30) |
|     |     |     |     |       | L!  |     |     | 2k  |     |     |      |
σ∈Sym(L)
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 8

is at most

|     |     |     | 0  |     |     | 0 ≤ s | ≤ 2k, |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
(31)
|     |     |     | (2·5k−1Λ|λ|)s |     | Ls−1 | s > 2k, |     |     |     |
| --- | --- | --- | ------------- | --- | ---- | ------- | --- | --- | --- |

(s−2)!
| where Λ | := maxkH | k.  |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
j
The proof of this error bound uses the following estimate of a fixed-order degenerate
| term in | the average | evolution | operator. |     |     |     |     |     |     |
| ------- | ----------- | --------- | --------- | --- | --- | --- | --- | --- | --- |
|         |             | }L        |           |     |     |     |     |     | R   |
Lemma 4. Let {H j be Hermitian operators with Λ := max j kH j k; let q 1 ,...,q κ ∈
j=1
with max |q | ≤ 1; and let s ≤ L be a positive integer. Then the norm of the sth-order
k k
degenerate term of the ideal evolution operator V(λ) as in (2) is at most
(Λ|λ|)s
|     |     |     | (cid:2)             |     |     |     |     | (cid:3) |      |
| --- | --- | --- | ------------------- | --- | --- | --- | --- | ------- | ---- |
|     |     |     | Ls−L(L−1)···(L−s+1) |     |     |     |     |         | (32) |
s!
and the norm of the sth-order degenerate term of the average evolution operator as in (22)
is at most
(κΛ|λ|)s
|     |     |     | (cid:2) Ls−L(L−1)···(L−s+1) |     |     |     |     | (cid:3) |      |
| --- | --- | --- | --------------------------- | --- | --- | --- | --- | ------- | ---- |
|     |     |     |                             |     |     |     |     | .       | (33) |
s!
| Proof. The | sth-order | term    | of V(λ) | is       |      |     |      |     |      |
| ---------- | --------- | ------- | ------- | -------- | ---- | --- | ---- | --- | ---- |
|            |           | (cid:0) | λPL     | (cid:1)s |      |     |      |     |      |
|            |           |         | H       |          | λs X |     |      |     |      |
|            |           |         | j=1     | j =      |      | H   | ···H |     | (34) |
|            |           |         |         |          |      | m1  | ms   |     |      |
|            |           |         | s!      |          | s!   |     |      |     |      |
m1,...,ms
| and its nondegenerate |     | term | is  |     |     |     |     |     |     |
| --------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
λs
X
|     |     |     |     |     | H   | m1 ···H | ms . |     | (35) |
| --- | --- | --- | --- | --- | --- | ------- | ---- | --- | ---- |
s!
m1,...,ms
pairwisedifferent
We use the following strategy to bound the norms of these terms: (i) bound the norm of
a sum of terms by summing the norms of each term; (ii) bound the norm of a product
of terms by multiplying the norms of each term; (iii) bound the norm of each summand
by Λ; and (iv) replace λ by |λ|. Applying this strategy, we find that the norm of the
(LΛ|λ|)s/s!,
sth-order term is at most where the nondegenerate term contributes precisely
L(L−1)···(L−s+1)(Λ|λ|)s/s!. Taking the difference gives the desired bound (32).
According to Lemma 2, the sth-order nondegenerate term of the average evolution is
)λ]s
|     |     | [(q 1 | +···+q | κ   | X   |     |      |     |      |
| --- | --- | ----- | ------ | --- | --- | --- | ---- | --- | ---- |
|     |     |       |        |     |     | H   | ···H | .   | (36) |
|     |     |       |        |     |     |     | m1   | ms  |      |
s!
m1,...,ms
pairwisedifferent
Following the same strategy as for V(λ) and also upper bounding the norm of each q by
k
| 1 as part | of step (iv), | we find | that | the norm | of this | term | is at | most |     |
| --------- | ------------- | ------- | ---- | -------- | ------- | ---- | ----- | ---- | --- |
(κΛ|λ|)s
|     |     |     |     | L(L−1)···(L−s+1). |     |     |     |     | (37) |
| --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | ---- |
s!
Itremainstofindanupperboundfortheentiresth-ordertermoftheaverageevolution.
To this end, we start with the average evolution (22) and apply the following strategy:
(i0) replace each summand of the Hamiltonian by Λ; (ii0) replace each q by 1 and each λ
k
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 9

by |λ|; and (iii0) expand all exponentials into their Taylor series and extract the sth-order
term. In other words, we extract the sth-order term of P exp(κLΛ|λ|)/L! to get
σ∈Sym(L)
(κLΛ|λ|)s
|     |     |     |     |     |     | .   |     |     |     |     | (38) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
s!
Theequivalenceofstrategies(i)–(iv)and(i0)–(iii0)canbeseenfrom[17, Eq.(57)]. Finally,
taking the difference between (38) and (37) gives the desired bound (33).
Proof of Lemma 3. We first prove a stronger bound, namely that the sth-order error is at
most

|     |     | 0   |     |     |     |     |     | 0 ≤ | s ≤ | 2k, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     | 2(2·5k−1Λ|λ|)s | [Ls−L(L−1)···(L−s+1)] |     |     |     |     |     |       |     |      |
| --- | --- | -------------- | --------------------- | --- | --- | --- | --- | --- | ----- | --- | ---- |
|     |     |                |                       |     |     |     |     | 2k  | < s ≤ | L,  | (39) |
s!
2(2·5k−1Λ|λ|)s
|     |     |     | Ls  |     |     |     |     | s > | L.  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s!
The first and third cases in this expression are straightforward. The formula Sσ is exact
2k
for terms with order 0 ≤ s ≤ 2k (this is what it means for the formula to have order 2k),
so the error is zero in this case. When s > L, the randomization lemma is not applicable
| and the error | can | be bounded |     | as in | [17, Proof | of Proposition |     | F.3]. |     |     |     |
| ------------- | --- | ---------- | --- | ----- | ---------- | -------------- | --- | ----- | --- | --- | --- |
2·5k−1.
To handle the remaining case 2k < s ≤ L, we apply Lemma 4 with κ = This
choice of κ follows from the definition of the (2k)th-order formula (3). The norm of the
| sth-order | degenerate | terms | can | be upper | bounded       | by  |     |     |     |     |     |
| --------- | ---------- | ----- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
| (Λ|λ|)s   |            |       |     |          | (2·5k−1Λ|λ|)s |     |     |     |     |     |     |
(cid:2) Ls−L(L−1)···(L−s+1) (cid:3) (cid:2) Ls−L(L−1)···(L−s+1) (cid:3)
|     |     |     |     |     | +   |     |     |     |     |     | . (40) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
| s!  |     |     |     |     |     | s!  |     |     |     |     |        |
According to Corollary 1, the sth-order nondegenerate term of (30) cancels, which proves
| (39) for 2k | < s ≤ | L.  |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To finish the proof, we need a unified error expression for order s > 2k. When 2k <
| s ≤ L, we | have |     |     |     |     |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ls−L(L−1)···(L−s+1)
|     | =   | # (cid:8) (l | ,...,l | ) ∈ [L]s(cid:9) | −#  | (cid:8) (l ,...,l | ) ∈ | [L]s : ∀i,j, | l   | 6= l (cid:9) |     |
| --- | --- | ------------ | ------ | --------------- | --- | ----------------- | --- | ------------ | --- | ------------ | --- |
|     |     | 1            | s      |                 |     | 1                 | s   |              |     | i j          |     |
|     |     | (cid:8)      |        | [L]s(cid:9)     |     | \(cid:8)          |     |              |     | (cid:9)      |     |
|     | =   | # (l         | ,...,l | ) ∈             | −#  | (l ,...,l         |     | ) ∈ [L]s     | : l | 6= l         |     |
|     |     | 1            | s      |                 |     | 1                 | s   |              | i   | j            |     |
i<j
(41)
|     |     | [(cid:8) |           |     | [L]s | (cid:9) |     |     |     |     |     |
| --- | --- | -------- | --------- | --- | ---- | ------- | --- | --- | --- | --- | --- |
|     | =   | #        | (l ,...,l | )   | ∈ :  | l = l   |     |     |     |     |     |
|     |     |          | 1         | s   |      | i j     |     |     |     |     |     |
i<j
  !
s
|     | ≤   | Ls−1, |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
with #{·} denoting the size of a set and [L] := {1,...,L}, where the inequality follows
| from the union | bound. |                       | Therefore, | we  | have |     |               |     |            |     |     |
| -------------- | ------ | --------------------- | ---------- | --- | ---- | --- | ------------- | --- | ---------- | --- | --- |
| (2·5k−1Λ|λ|)s  |        |                       |            |     |      |     | (2·5k−1Λ|λ|)s |     |            |     |     |
| 2              |        | [Ls−L(L−1)···(L−s+1)] |            |     |      | ≤   |               |     | s(s−1)Ls−1 |     |     |
|                | s!     |                       |            |     |      |     |               | s!  |            |     |     |
(42)
(2·5k−1Λ|λ|)s
|     |     |     |     |     |     | =   |     |     | Ls−1. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
(s−2)!
N,
| If s >         | L ∈ | we have | s(s−1)        | ≥   | (L+1)L | ≥ 2L          | and |       |     |     |      |
| -------------- | --- | ------- | ------------- | --- | ------ | ------------- | --- | ----- | --- | --- | ---- |
|                |     |         | (2·5k−1Λ|λ|)s |     |        | (2·5k−1Λ|λ|)s |     |       |     |     |      |
|                |     |         | 2             |     | Ls     | ≤             |     | Ls−1. |     |     | (43) |
|                |     |         |               | s!  |        | (s−2)!        |     |       |     |     |      |
| This completes | the | proof.  |               |     |        |               |     |       |     |     |      |
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 10

We also use the following standard tail bound on the exponential function [17, Lemma
F.2].
|       |     |     |       | C     | N,         |            |           |     |     |     |     |      |
| ----- | --- | --- | ----- | ----- | ---------- | ---------- | --------- | --- | --- | --- | --- | ---- |
| Lemma | 5.  | For | any x | ∈ and | κ ∈        | we         | have      |     |     |     |     |      |
|       |     |     |       |       | (cid:12) ∞ | xs(cid:12) | |x|κ      |     |     |     |     |      |
|       |     |     |       |       | (cid:12)X  | (cid:12)   |           |     |     |     |     |      |
|       |     |     |       |       | (cid:12)   | (cid:12) ≤ | exp(|x|). |     |     |     |     | (44) |
|       |     |     |       |       | (cid:12)   | s!(cid:12) | κ!        |     |     |     |     |      |
s=κ
We now establish the main theorem, which upper bounds the error of a higher-order
| randomized |     | product | formula. |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Theorem 2 (Randomizedhigher-ordererrorbound). Let {H }L be Hermitian matrices.
|     |     |     |     |     |     |     |     |     | j j=1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
Let
|     |     |     |     |     |     |     | (cid:18) | L (cid:19) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --- | --- | --- |
X
|     |     |     |     |     | V(−it) | := exp | −it | H   |     |     |     | (45) |
| --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | ---- |
j
j=1
PL
be the evolution induced by the Hamiltonian H = H j for time t. For any permutation
j=1
σ ∈ Sym(L), define the permuted (2k)th-order formula recursively by
|     |     |     |       |     | L (cid:18)λ |      | (cid:19) 1 | (cid:18)λ | (cid:19) |     |     |     |
| --- | --- | --- | ----- | --- | ----------- | ---- | ---------- | --------- | -------- | --- | --- | --- |
|     |     |     |       | Y   |             |      | Y          |           |          |     |     |     |
|     |     |     | Sσ(λ) | :=  | exp         | H    | exp        | H         |          |     |     |     |
|     |     |     | 2     |     | 2           | σ(j) |            | 2         | σ(j)     |     |     |     |
(46)
|     |     |     |     | j=1 |        |      | j=L    |        |      |       |     |     |
| --- | --- | --- | --- | --- | ------ | ---- | ------ | ------ | ---- | ----- | --- | --- |
|     |     |     | Sσ  | [Sσ | λ)]2Sσ |      |        | )λ)[Sσ |      | λ)]2, |     |     |
|     |     |     | (λ) | :=  | (p     |      | ((1−4p |        |      | (p    |     |     |
|     |     |     | 2k  |     | 2k−2 k | 2k−2 |        | k      | 2k−2 | k     |     |     |
N
with p := 1/(4−41/(2k−1)) for k > 1. Let r ∈ and Λ := maxkH k. Then
|                 | k   |            |     |         |                   |          |     |     |     | j   |     |     |
| --------------- | --- | ---------- | --- | ------- | ----------------- | -------- | --- | --- | --- | --- | --- | --- |
| (cid:13)        |     |            |     |         | (cid:19)r(cid:13) |          |     |     |     |     |     |     |
| (cid:13)        |     | (cid:18) 1 |     |         |                   | (cid:13) |     |     |     |     |     |     |
|                 |     |            | X   | Sσ      |                   |          |     |     |     |     |     |     |
| (cid:13)V(−it)− |     |            |     | (−it/r) |                   | (cid:13) |     |     |     |     |     |     |
| (cid:13)        |     | L!         |     | 2k      |                   | (cid:13) |     |     |     |     |     |     |
| (cid:13)        |     |            |     |         |                   | (cid:13) |     |     |     |     |     |     |
|                 |     | σ∈Sym(L)   |     |         |                   | (cid:5)  |     |     |     |     |     |     |
(2·5k−1Λ|t|L)4k+2 (cid:18) Λ|t|L(cid:19) (2·5k−1Λ|t|)2k+1L2k (cid:18) Λ|t|L(cid:19)
| ≤   | 4       |     |          | exp | 4·5k−1 |     | +2  |            |     |     | exp 2·5k−1 |     |
| --- | ------- | --- | -------- | --- | ------ | --- | --- | ---------- | --- | --- | ---------- | --- |
|     | (cid:0) |     | (cid:1)2 |     |        |     |     | (2k−1)!r2k |     |     |            |     |
|     | (2k+1)! |     | r4k+1    |     |        | r   |     |            |     |     |            | r   |
(47)
where, for λ = −it, we associate quantum channels V(λ) and Sσ (λ) with the unitaries
2k
| V(λ) | and Sσ | (λ), | respectively. |     |     |     |     |     |     |     |     |     |
| ---- | ------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2k
| Proof.   | We  | first prove | that |          |     |     |     |     |     |     |     |     |
| -------- | --- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| (cid:13) |     |             |      | (cid:13) |     |     |     |     |     |     |     |     |
| (cid:13) |     |             |      | (cid:13) |     |     |     |     |     |     |     |     |
1 X
| (cid:13) V(λ)− |                   |          | S        | σ (λ) (cid:13) |                     |     |                     |         |     |     |                     |         |
| -------------- | ----------------- | -------- | -------- | -------------- | ------------------- | --- | ------------------- | ------- | --- | --- | ------------------- | ------- |
| (cid:13)       |                   |          |          | 2 k (cid:13)   |                     |     |                     |         |     |     |                     |         |
| (cid:13)       | L                 | !        |          | (cid:13)       |                     |     |                     |         |     |     |                     |         |
| (cid:13)       |                   |          |          | (cid:13)       |                     |     |                     |         |     |     |                     |         |
|                |                   | σ∈Sym(L) |          |                | (cid:5)             |     |                     |         |     |     |                     |         |
|                | (2·5k−1Λ|λ|L)4k+2 |          |          |                |                     |     | (2·5k−1Λ|λ|)2k+1L2k |         |     |     |                     |         |
|                |                   |          |          |                | (cid:0) 4·5k−1Λ|λ|L |     | (cid:1)             |         |     |     | (cid:0) 2·5k−1Λ|λ|L | (cid:1) |
| ≤              | 4                 |          |          | exp            |                     |     | +2                  |         |     |     | exp                 | .       |
|                |                   | (cid:0)  | (cid:1)2 |                |                     |     |                     | (2k−1)! |     |     |                     |         |
(2k+1)!
(48)
To this end, note that the sth-order error of V(λ)−Sσ (λ) is at most
2k

|     |     |     |     |     | 0  |     | 0   | ≤ s ≤ 2k, |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
(49)
2(2·5k−1Λ|λ|)s
|     |     |     |     |     |     |     | Ls s | > 2k |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |    | s!  |      |      |     |     |     |     |
(as before, this follows as in [17, Proof of Proposition F.3]). Thus Lemma 5 gives
(2·5k−1Λ|λ|L)2k+1
|     |     | kV(λ)−Sσ |     |      |     |         |     |     | (cid:0) 2·5k−1Λ|λ|L |     | (cid:1) |      |
| --- | --- | -------- | --- | ---- | --- | ------- | --- | --- | ------------------- | --- | ------- | ---- |
|     |     |          |     | (λ)k | ≤ 2 |         |     | exp |                     |     | .       | (50) |
|     |     |          |     | 2k   |     | (2k+1)! |     |     |                     |     |         |      |
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 11

Ontheotherhand,Lemma3impliesthatthesth-ordererrorofV(λ)− 1 P Sσ (λ)
L! σ∈Sym(L) 2k
is at most

0 0 ≤ s ≤ 2k,
(51)
 (2·5k−1Λ|λ|)s Ls−1 s > 2k,
(s−2)!
so again Lemma 5 gives
(cid:13) (cid:13)
(cid:13) (cid:13) (cid:13) (cid:13) V(λ)− L 1 ! X S 2 σ k (λ) (cid:13) (cid:13) (cid:13) (cid:13) ≤ (2·5k− (2 1 k Λ| − λ| 1 )2 ) k ! +1L2k exp (cid:0) 2·5k−1Λ|λ|L (cid:1) . (52)
(cid:13) σ∈Sym(L) (cid:13)
Equation (48) now follows from Lemma 1 by setting
(2·5k−1Λ|λ|L)2k+1
a = 2 exp (cid:0) 2·5k−1Λ|λ|L (cid:1) ,
(2k+1)!
(53)
(2·5k−1Λ|λ|)2k+1L2k
b = exp (cid:0) 2·5k−1Λ|λ|L (cid:1) .
(2k−1)!
To simulate the evolution for time t, we divide it into r segments. The error within
each segment is obtained from (48) by setting λ = −it/r. Then subadditivity of the
diamond norm distance gives
(cid:13) (cid:13) (cid:13) (cid:13)
(cid:13) (cid:13) (cid:13) (cid:13) V(−it)− (cid:18) L 1 ! X S 2 σ k (cid:0) −it/r (cid:1) (cid:19)r(cid:13) (cid:13) (cid:13) (cid:13) ≤ r (cid:13) (cid:13) (cid:13) (cid:13) V(−it/r)− L 1 ! X S 2 σ k (cid:0) −it/r (cid:1) (cid:13) (cid:13) (cid:13) (cid:13) ,
(cid:13) σ∈Sym(L) (cid:13) (cid:13) σ∈Sym(L) (cid:13)
(cid:5) (cid:5)
(54)
which completes the proof.
5 Algorithm performance and comparisons
We now analyze the complexity of our randomized product formula algorithm. Assume
that k ∈ N is fixed, Λ = O(1) is constant, and r > tL. By Theorem 2, the asymptotic
error of the (2k)th-order randomized product formula is
(cid:13) (cid:13)
(cid:13) (cid:13) (cid:13) (cid:13) V(−it)− (cid:18) L 1 ! X S 2 σ k (cid:0) −it/r (cid:1) (cid:19)r(cid:13) (cid:13) (cid:13) (cid:13) ≤ O (cid:18)(t r L 4 ) k 4 + k 1 +2 + t2k+ r2 1 k L2k(cid:19) . (55)
(cid:13) σ∈Sym(L) (cid:13)
(cid:5)
To guarantee that the simulation error is at most (cid:15), we upper bound the right-hand side
of (55) by (cid:15) and solve for r. We find that it suffices to use
rrand = max
(cid:26)
O
(cid:18)(tL) 4
4
k
k
+
+
2
1
(cid:19)
,O
(cid:18)t 2k
2
+
k
1 L(cid:19)(cid:27)
2k 1 1
(cid:15)4k+1 (cid:15)2k
(56)
(cid:26) (cid:18) (cid:18)tL(cid:19)
4k
1
+1
(cid:19) (cid:18) (cid:18)t(cid:19)
2
1
k
(cid:19)(cid:27)
= max O tL ,O tL
(cid:15) (cid:15)
segments, giving a simulation algorithm with
(cid:26) (cid:18) (cid:18)tL(cid:19)
4k
1
+1
(cid:19) (cid:18) (cid:18)t(cid:19)
2
1
k
(cid:19)(cid:27)
grand = O(Lrrand) = max O tL2 ,O tL2 (57)
2k 2k (cid:15) (cid:15)
elementary gates.
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 12

For comparison, the error in the (2k)th-order deterministic formula algorithm is at
most [17, Proposition F.4]
(cid:18)(tL)2k+1(cid:19)
|     | (cid:13)        |     | (cid:2) |         | (cid:3)r(cid:13) (cid:13) |     |     |     |      |
| --- | --------------- | --- | ------- | ------- | ------------------------- | --- | --- | --- | ---- |
|     | (cid:13)V(−it)− |     | S       | (−it/r) |                           | ≤ O |     | .   | (58) |
|     | (cid:13)        |     | 2k      |         | (cid:13)                  |     | r2k |     |      |
While this bound quantifies the simulation error in terms of the spectral-norm distance, it
can easily be adapted to the diamond-norm distance using either Lemma 1 or [8, Lemma
7]. This translation introduces only constant-factor overhead, so we have
(cid:18)(tL)2k+1(cid:19)
|     | (cid:13)        |     |           |         | (cid:3)r(cid:13) (cid:13) |     |     |     |      |
| --- | --------------- | --- | --------- | ------- | ------------------------- | --- | --- | --- | ---- |
|     | (cid:13)V(−it)− |     | (cid:2) S | (−it/r) |                           | ≤ O |     | .   | (59) |
|     | (cid:13)        |     | 2k        |         | (cid:13)                  |     |     |     |      |
|     |                 |     |           |         | (cid:5)                   |     | r2k |     |      |
Therefore, the number of segments that suffice to ensure error at most (cid:15) satisfies
|     |     |     |     | (cid:18) | (cid:18)tL(cid:19) | 1 (cid:19) |     |     |     |
| --- | --- | --- | --- | -------- | ------------------ | ---------- | --- | --- | --- |
2 k
|     |     |     | rdet = | O   | tL  |     | ,   |     | (60) |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---- |
2k
(cid:15)
giving an algorithm with
1
|     |     |      |            |     | (cid:18) | (cid:18)tL(cid:19) | 2 k (cid:19) |     |      |
| --- | --- | ---- | ---------- | --- | -------- | ------------------ | ------------ | --- | ---- |
|     |     | gdet | = O(Lrdet) |     | = O      | tL2                |              |     | (61) |
|     |     | 2k   |            | 2k  |          |                    |              |     |      |
(cid:15)
elementary gates. Comparing to (57), we see that the randomized product formula strictly
improvesthecomplexityasafunctionofL. Indeed, the(2k)th-orderrandomizedapproach
either provides an improvement with respect to all parameters of interest over the (2k)th
order deterministic approach (if the first term of (57) obtains the maximum), or has better
dependence on the number of terms in the Hamiltonian than any deterministic formula (if
the second term dominates).
We can also compare our result to the commutator bound of [17], which depends on
the specific structure of the Hamiltonian. For concreteness, we consider a one-dimensional
nearest-neighborHeisenbergmodelwitharandommagneticfield,asstudiedin[17]. Specif-
ically, let
n
|     |     |     | X   |       |         | σz)  |     |     |      |
| --- | --- | --- | --- | ----- | ------- | ---- | --- | --- | ---- |
|     |     |     | H = | (~σ j | ·~σ j+1 | +h j |     |     | (62) |
j
j=1
with periodic boundary conditions (i.e., ~σ =~σ ), and h ∈ [−h,h] chosen uniformly at
|     |     |     |     | n+1 |     | 1   | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(σx,σy,σz)
random, where ~σ = denotes a vector of Pauli x, y, and z matrices on qubit
| j   | j   | j j |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
j. The (2k)th-order deterministic formula with the commutator bound has error at most
[17, Eq. (146)]
|          |     |     |     |          |     | (cid:18)(tL)2k+2 |     | t2k+1L2k(cid:19) |     |
| -------- | --- | --- | --- | -------- | --- | ---------------- | --- | ---------------- | --- |
| (cid:13) |     |     |     | (cid:13) |     |                  |     |                  |     |
(cid:13)V(−it)− (cid:2) S (cid:0) −it/r (cid:1)(cid:3)r(cid:13) ≤ O + , (63)
| (cid:13) |     | 2k  |     | (cid:13) |     |       |     |     |     |
| -------- | --- | --- | --- | -------- | --- | ----- | --- | --- | --- |
|          |     |     |     | (cid:5)  |     | r2k+1 |     | r2k |     |
where we have again used Lemma 1 (or [8, Lemma 7]) to relate the spectral-norm distance
to the diamond-norm distance. To guarantee that the simulation error is at most (cid:15), it
suffices to choose
|     |       |       |                       |              | 2 k + 2  |           | 2k + 1            |     |     |
| --- | ----- | ----- | --------------------- | ------------ | -------- | --------- | ----------------- | --- | --- |
|     |       |       | (cid:26) (cid:18)(tL) |              | (cid:19) | (cid:18)t | L(cid:19)(cid:27) |     |     |
|     | rcomm |       |                       |              | 2 k + 1  |           | 2 k               |     |     |
|     |       | = max | O                     |              |          | ,O        |                   |     |     |
|     | 2k    |       |                       |              | 1        |           | 1                 |     |     |
|     |       |       |                       | (cid:15)2k+1 |          |           | (cid:15)2k        |     |     |
(64)
|     |     |       |                   |                    |          | 1        |                            | 1                |     |
| --- | --- | ----- | ----------------- | ------------------ | -------- | -------- | -------------------------- | ---------------- | --- |
|     |     |       | (cid:26) (cid:18) | (cid:18)tL(cid:19) |          | (cid:19) | (cid:18) (cid:18)t(cid:19) | (cid:19)(cid:27) |     |
|     |     |       |                   |                    | 2k       | +1       |                            | 2 k              |     |
|     |     | = max | O                 | tL                 |          | ,O       | tL                         |                  |     |
|     |     |       |                   |                    | (cid:15) |          | (cid:15)                   |                  |     |
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 13

| segments, | giving | an  | algorithm | with |       |                   |                    |       |                   |                   |                  |      |
| --------- | ------ | --- | --------- | ---- | ----- | ----------------- | ------------------ | ----- | ----------------- | ----------------- | ---------------- | ---- |
|           |        |     |           |      |       |                   |                    | 1     |                   |                   | 1                |      |
|           |        |     |           |      |       | (cid:26) (cid:18) | (cid:18)tL(cid:19) |       | (cid:19) (cid:18) | (cid:18)t(cid:19) | (cid:19)(cid:27) |      |
|           | gcomm  |     | O(Lrcomm) |      |       |                   | tL2                | 2k +1 |                   | tL2               | 2 k              |      |
|           |        | =   |           |      | = max | O                 |                    |       | ,O                |                   |                  | (65) |
|           | 2k     |     |           | 2k   |       |                   | (cid:15)           |       |                   | (cid:15)          |                  |      |
elementary gates. Comparing to the corresponding bound (57) for randomized product
formulas,weseethattheonlydifferenceisthattheexponent1/(2k+1)forthecommutator
bound becomes 1/(4k +1) in the randomized case. Thus the randomized approach can
provide a slightly faster algorithm despite using less information about the structure of the
Hamiltonian. More specifically, the relationship between t and L determines whether the
randomized approach offers an improvement. If t = Ω(L2k), then the second term of (65)
1
achieves the maximum, and both approaches have asymptotic complexity O (cid:0) tL2(cid:0)t(cid:1) 2 k (cid:1) .
(cid:15)
However, if t = o(L2k), then the randomized formula is advantageous.
| 6 Empirical |     | performance |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
While randomization provides a useful theoretical handle for establishing better provable
bounds, those bounds may still be far from tight. As described in Section 1, our original
motivationforconsideringrandomizationwastheobservationthatproductformulasappear
to perform dramatically better in practice than the best available proven bounds would
suggest. Toinvestigatetheempiricalbehaviorofproductformulas,wenumericallyevaluate
their performance for simulations of the Heisenberg model (62) with t = n and h = 1,
targeting error (cid:15) = 10−3, as previously considered in [17]. We collect data for the first-,
fourth-, and sixth-order formulas as the latter two orders have the best performance in
practice for small n and the first-order formula offers a qualitatively better theoretical
improvement.
For the deterministic formula, we order the operators of the Hamiltonian in the same
| way as [17], | namely |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
σxσx,...,σx σx,σxσx, σyσy,...,σy σy,σyσy, σzσz,...,σz σz,σzσz, σz,...,σz.
| 1 2 | n−1 | n   | n 1 | 1 2 | n−1 | n   | n 1 | 1 2 |     | n−1 n | n 1 1 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- |
(66)
Wecomputetheerrorintermsofthespectral-normdistanceandconvertittothediamond-
norm distance using Lemma 7 of [8] (i.e., we multiply by 2). To analyze the randomized
formula, we would like to numerically evaluate the diamond-norm distances
|     |     |     | (cid:13)         |     | 1       |             |     |            |                  | (cid:13) |     |      |
| --- | --- | --- | ---------------- | --- | ------- | ----------- | --- | ---------- | ---------------- | -------- | --- | ---- |
|     |     |     | (cid:13)         |     | (cid:0) |             |     | rev(−it/r) | (cid:1)r(cid:13) |          |     |      |
|     |     |     | (cid:13) V(−it)− |     | S       | 1 (−it/r)+S |     |            |                  | (cid:13) |     | (67) |
|     |     |     | (cid:13)         |     | 2r      |             |     | 1          |                  | (cid:13) |     |      |
(cid:5)
and
|     |     |     | (cid:13) |     |          |          |     |               | (cid:13)          |     |     |      |
| --- | --- | --- | -------- | --- | -------- | -------- | --- | ------------- | ----------------- | --- | --- | ---- |
|     |     |     | (cid:13) |     | (cid:18) |          |     |               | (cid:19)r(cid:13) |     |     |      |
|     |     |     | (cid:13) |     | 1        | X        |     |               | (cid:13)          |     |     |      |
|     |     |     | V(−it)−  |     |          |          | S σ | (cid:0) −it/r | (cid:1)           | .   |     | (68) |
|     |     |     | (cid:13) |     |          |          | 2 k |               | (cid:13)          |     |     |      |
|     |     |     | (cid:13) |     | L !      |          |     |               | (cid:13)          |     |     |      |
|     |     |     | (cid:13) |     |          | σ∈Sym(L) |     |               | (cid:13)          |     |     |      |
(cid:5)
While the diamond norm can be computed using a semidefinite program [34], direct com-
putation is prohibitive as the channel contains (L!)r Kraus operators. Instead, we use
Lemma 1 to estimate the error. We randomly choose the ordering of the summands in
each of the r segments, exponentiate each individual operator, and construct a unitary
operator by concatenating the exponentials according to the given product formula. We
follow this procedure to obtain a Monte Carlo estimate of the average error
|     |     |     | (cid:13)        |     | M   |             |         |             |       | (cid:13)         |     |      |
| --- | --- | --- | --------------- | --- | --- | ----------- | ------- | ----------- | ----- | ---------------- | --- | ---- |
|     |     |     | (cid:13)        | 1   | X   | σm,r(cid:0) | (cid:1) | σm,1(cid:0) |       | (cid:1) (cid:13) |     |      |
|     |     |     | (cid:13)V(−it)− |     | S   |             | −it/r   | ···S        | −it/r | (cid:13)         |     | (69) |
|     |     |     | (cid:13)        |     |     | 2k          |         | 2k          |       | (cid:13)         |     |      |
|     |     |     | (cid:13)        | M   |     |             |         |             |       | (cid:13)         |     |      |
m=1
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 14

| 106 |     |     |     |     | 103 |     |     |     | 102 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
105
| r   |     |     |     |     | r 102 |     |     | r   |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
104
|     |     |     | Firstorder    |     |     |     | Fourthorder   |     |     | Sixthorder    |     |
| --- | --- | --- | ------------- | --- | --- | --- | ------------- | --- | --- | ------------- | --- |
|     |     |     | Deterministic |     |     |     | Deterministic |     |     | Deterministic |     |
|     |     |     | Randomized    |     |     |     | Randomized    |     |     | Randomized    |     |
| 103 |     |     |               |     | 101 |     |               |     | 101 |               |     |
|     |     | 6 7 | 8 9           | 10  |     | 6   | 7 8 9 10      |     | 6   | 7 8 9         | 10  |
|     |     |     | n             |     |     |     | n             |     |     | n             |     |
Figure 1: Comparison of the values of r between deterministic and randomized product formulas.
Error bars are omitted when they are negligibly small on the plot. Straight lines show power-law
| fits | to the | data. |     |     |     |     |     |     |     |     |     |
| ---- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for the (2k)th-order formula and similarly for the first-order case. Here, M is the number
of samples in the Monte Carlo estimation, which can be increased to get more accurate
estimate. In practice, we find that it suffices to take only three samples, as the standard
deviations are already negligibly small (about 10−5). We then invoke Lemma 1 to bound
the diamond-norm error in (68). To the extent that the bound of Lemma 1 is loose, we
| expect | the | empirical | performance |     | to  | be better | in practice. |     |     |     |     |
| ------ | --- | --------- | ----------- | --- | --- | --------- | ------------ | --- | --- | --- | --- |
Using five randomly generated instances for each value of n, we apply binary search
10−3.
to determine the smallest number of segments r that suffices to give error at most
Figure 1 shows the resulting data for the first-, fourth-, and sixth-order formulas, which
are well-approximated by power laws. Fitting the data, we estimate that
|     | rremp |     | 300.0n1.806 |     | rremp |     | 5.458n1.439 | rremp | 2.804n1.152 |     |      |
| --- | ----- | --- | ----------- | --- | ----- | --- | ----------- | ----- | ----------- | --- | ---- |
|     |       | =   |             |     |       | =   |             |       | =           |     | (70) |
|     | 1     |     |             |     |       | 4   |             | 6     |             |     |      |
segments should suffice to give error at most 10−3. We thus observe that the empiri-
cal complexity of the randomized algorithm is still significantly better than the provable
performance
|     |     | rrand | = O(n3) |     |     | rrand = | O(n2.25) |     | rrand = O(n2.17). |     | (71) |
| --- | --- | ----- | ------- | --- | --- | ------- | -------- | --- | ----------------- | --- | ---- |
|     |     | 1     |         |     |     | 4       |          |     | 6                 |     |      |
For comparison, analogous empirical fits for deterministic formulas give the comparable
values
|     | rdemp |     | 4143n2.066 |     | rdemp |     | 5.821n1.471 | rdemp | 2.719n1.160, |     |      |
| --- | ----- | --- | ---------- | --- | ----- | --- | ----------- | ----- | ------------ | --- | ---- |
|     |       | =   |            |     |       | =   |             |       | =            |     | (72) |
|     | 1     |     |            |     | 4     |     |             | 6     |              |     |      |
(cf.[17, Eq.(147)], butnotethatwehavegeneratednewdatausing[8, Lemma7]tobound
the diamond-norm distance in terms of the spectral-norm distance), whereas the rigorous
| commutator |     | bound | gives   | the | larger | exponents | [17]      |     |                   |     |      |
| ---------- | --- | ----- | ------- | --- | ------ | --------- | --------- | --- | ----------------- | --- | ---- |
|            |     | rcomm | = O(n3) |     |        | rcomm     | = O(n2.4) |     | rcomm = O(n2.28). |     | (73) |
|            |     | 1     |         |     |        | 4         |           |     | 6                 |     |      |
We see that the randomized bound offers significantly better empirical performance
at first order, consistent with the observation that randomization improves the order of
approximation in this case. The fourth-order formula slightly improves both the exponent
and the constant factor. While this improvement is small, it is nevertheless notable since
it involves only a minor change to the algorithm. At sixth order we see negligible im-
provement. Since the proven bounds give less improvement with each successive order, it
is perhaps not surprising to see that the empirical performance shows similar behavior.
Toillustratetheeffectofusingdifferentformulasanddifferenterrorboundstosimulate
larger systems, Figure 2 compares the cost of simulating our model system for sizes up to
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 15

1013
1012
1011
1010
109
108
107
106
105
10 20 30 40 50 60 70 80 90 100
n
slaitnenopxeforebmun
DeterministicPF4(min)
DeterministicPF4(com)
RandomizedPF4(min)
DeterministicPF4(emp)
RandomizedPF4(emp)
DeterministicPF6(min)
RandomizedPF6(min)
DeterministicPF6(emp)
RandomizedPF6(emp)
Figure 2: Comparison of the total number of elementary exponentials for product formula simu-
lations of the Heisenberg model using deterministic and randomized product formulas of fourth
and sixth order with both rigorous and empirical error bounds. Note that since the empirical
performanceofdeterministicandrandomizedsixth-orderproductformulasisalmostthesame,the
latter data points are obscured by the former.
n = 100 with deterministic and randomized formulas of orders 4 and 6, using both proven
error bounds and the above empirical estimates. (We omit the first-order formula since
it is not competitive even at such small sizes.) We give rigorous bounds for deterministic
formulas using the minimized bound of [17], and for fourth order we also show the result of
using the commutator bound. We see that randomization gives a significant improvement
overthedeterministicformulausingtheminimizedbound,althoughthecommutatorbound
outperforms the randomized bound at the system sizes shown here. For sufficiently large
n, the randomized bound gives lower complexity, but this requires a fairly large n since the
difference in exponents is small and the commutator bound achieves a favorable constant
prefactor. Empirical estimates of the error improve the performance by several orders of
magnitude, with randomization giving a small advantage for the fourth-order formula as
indicated above. However, for systems of size larger than about n = 25, the sixth-order
bound prevails, and in this case randomization no longer offers a significant advantage.
7 Discussion
We have shown that randomization can be used to establish better performance for quan-
tum simulation algorithms based on product formulas. By simply randomizing how the
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 16

summands in the Hamiltonian are ordered, we introduce terms in the average evolution
that could not appear in any deterministic product formula approximation of the same or-
der, and thereby give a more efficient algorithm. Indeed, this approach can outperform the
commutatorboundeventhoughthatmethodusesmoreinformationaboutthestructureof
the Hamiltonian. A randomized product formula simulation algorithm is not much more
complicated than the corresponding deterministic formula, using only O(LlogL) bits of
randomness per segment and no ancilla qubits. Furthermore, we showed that randomiza-
tion can even offer improved empirical performance in some cases.
While randomization has allowed us to make some progress on the challenge of proving
betterboundsontheperformanceofproductformulas,ourstrengthenedboundsremainfar
from the apparent empirical performance. We expect that other ideas will be required to
improve the product-formula approach [15, 28]. Although our bounds have better asymp-
totic n-dependence than the previous commutator bound, they only offer an improvement
if the system is sufficiently large. It could be fruitful to establish bounds for randomized
product formulas that take advantage of the structure of the Hamiltonian, perhaps offer-
ing better performance both asymptotically and for small system sizes. More generally, it
may be of interest to investigate other scenarios in which random choices can be used to
improve the analysis of quantum simulation [10, 14] and other quantum algorithms.
Acknowledgments
We thank Guoming Wang for helpful discussions during the initial stages of this work and
anonymous referees for their helpful comments on our manuscript.
This work was supported in part by the Army Research Office (MURI award W911NF-
16-1-0349), the Canadian Institute for Advanced Research, the Department of Energy
(grant 17-020469), and the National Science Foundation (grant 1526380).
References
[1] DoritAharonovandAmnonTa-Shma. Adiabaticquantumstategenerationandstatis-
tical zero knowledge. In Proceedings of the 35th ACM Symposium on Theory of Com-
puting, pages 20–29, 2003. DOI: 10.1145/780542.780546. arXiv:quant-ph/0301023.
[2] Ryan Babbush, Jarrod McClean, Dave Wecker, Alán Aspuru-Guzik, and Nathan
Wiebe. Chemical basis of Trotter-Suzuki errors in quantum chemistry simula-
tion. Physical Review A, 91:022311, 2015. DOI: 10.1103/PhysRevA.91.022311.
arXiv:1410.8159.
[3] R. Barends, L. Lamata, J. Kelly, L. García-Álvarez, A. G. Fowler, A Megrant, E Jef-
frey, T. C. White, D. Sank, J. Y. Mutus, B. Campbell, Yu Chen, Z. Chen, B. Chiaro,
A. Dunsworth, I.-C. Hoi, C. Neill, P. J. J. O’Malley, C. Quintana, P. Roushan,
A. Vainsencher, J. Wenner, E. Solano, and John M. Martinis. Digital quantum sim-
ulation of fermionic models with a superconducting circuit. Nature Communications,
6:7654, 2015. DOI: 10.1038/ncomms8654. arXiv:1501.07703.
[4] DominicW.BerryandAndrewM.Childs. Black-boxHamiltoniansimulationanduni-
tary implementation. Quantum Information and Computation, 12(1-2):29–62, 2012.
arXiv:0910.4157.
[5] Dominic W. Berry, Graeme Ahokas, Richard Cleve, and Barry C. Sanders. Efficient
quantum algorithms for simulating sparse Hamiltonians. Communications in Mathe-
matical Physics,270(2):359–371,2007. DOI:10.1007/s00220-006-0150-x. arXiv:quant-
ph/0508139.
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 17

[6] DominicW.Berry, AndrewM.Childs, RichardCleve, RobinKothari, andRolandoD.
Somma. Exponential improvement in precision for simulating sparse Hamiltonians.
In Proceedings of the 46th ACM Symposium on Theory of Computing, pages 283–292,
2014. DOI: 10.1145/2591796.2591854. arXiv:1312.1414.
[7] DominicW.Berry, AndrewM.Childs, RichardCleve, RobinKothari, andRolandoD.
Somma. Simulating Hamiltonian dynamics with a truncated Taylor series. Phys-
ical Review Letters, 114(9):090502, 2015. DOI: 10.1103/PhysRevLett.114.090502.
arXiv:1412.4687.
[8] Dominic W. Berry, Andrew M. Childs, and Robin Kothari. Hamiltonian simula-
tion with nearly optimal dependence on all parameters. In Proceedings of the 56th
IEEE Symposium on Foundations of Computer Science, pages 792–809, 2015. DOI:
10.1109/FOCS.2015.54. arXiv:1501.01715.
[9] Dominic W. Berry, Andrew M. Childs, Aaron Ostrander, and Guoming Wang. Quan-
tum algorithm for linear differential equations with exponentially improved depen-
dence on precision. Communications in Mathematical Physics, 356:1057–1081, 2017.
DOI: 10.1007/s00220-017-3002-y. arXiv:1701.03684.
[10] DominicW.Berry,AndrewM.Childs,YuanSu,XinWang,andNathanWiebe. Time-
dependent Hamiltonian simulation with L1-norm scaling, 2019. arXiv:1906.07115.
[11] Fernando G. S. L. Brandao and Krysta M. Svore. Quantum speed-ups for solv-
ing semidefinite programs. In Proceedings of the 58th IEEE Symposium on Foun-
dations of Computer Science, pages 415–426, 2017. DOI: 10.1109/FOCS.2017.45.
arXiv:1609.05537.
[12] Kenneth R. Brown, Robert J. Clark, and Isaac L. Chuang. Limitations of quan-
tum simulation examined by simulating a pairing Hamiltonian using nuclear mag-
netic resonance. Physical Review Letters, 97:050504, 2006. DOI: 10.1103/Phys-
RevLett.97.050504. arXiv:quant-ph/0601021.
[13] Earl Campbell. Shorter gate sequences for quantum computing by mixing uni-
taries. Physical Review A, 95:042306, Apr 2017. DOI: 10.1103/PhysRevA.95.042306.
arXiv:1612.02689.
[14] Earl Campbell. Random compiler for fast Hamiltonian simulation. Physical
Review Letters, 123:070503, Aug 2019. DOI: 10.1103/PhysRevLett.123.070503.
arXiv:1811.08017.
[15] Andrew M. Childs and Yuan Su. Nearly optimal lattice simulation by product
formulas. Physical Review Letters, 123:050503, Aug 2019. DOI: 10.1103/Phys-
RevLett.123.050503. arXiv:1901.00564.
[16] Andrew M. Childs, Richard Cleve, Enrico Deotto, Edward Farhi, Sam Gutmann,
and Daniel A. Spielman. Exponential algorithmic speedup by quantum walk. In
Proceedings of the 35th ACM Symposium on Theory of Computing, pages59–68, 2003.
DOI: 10.1145/780542.780552. arXiv:quant-ph/0209131.
[17] Andrew M. Childs, Dmitri Maslov, Yunseong Nam, Neil J. Ross, and Yuan Su. To-
ward the first quantum simulation with quantum speedup. Proceedings of the Na-
tional Academy of Sciences,115(38):9456–9461,2018. DOI:10.1073/pnas.1801723115.
arXiv:1711.10980.
[18] Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. A quantum algorithm for
the Hamiltonian NAND tree. Theory of Computing, 4(1):169–190, 2008. DOI:
10.4086/toc.2008.v004a008.
[19] Richard P. Feynman. Simulating physics with computers. International Journal of
Theoretical Physics, 21(6-7):467–488, 1982. DOI: 10.1007/BF02650179.
[20] JeongwanHaah,MatthewB.Hastings,RobinKothari,andGuangHaoLow.Quantum
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 18

algorithm for simulating real time evolution of lattice Hamiltonians. In 2018 IEEE
59thAnnualSymposiumonFoundationsofComputerScience(FOCS),pages350–360,
Oct 2018. DOI: 10.1109/FOCS.2018.00041. arXiv:1801.03922.
[21] Aram W. Harrow, Avinatan Hassidim, and Seth Lloyd. Quantum algorithm for
linear systems of equations. Physical Review Letters, 103(15):150502, 2009. DOI:
10.1103/PhysRevLett.103.150502. arXiv:0811.3171.
[22] Matthew B. Hastings. Turning gate synthesis errors into incoherent errors. Quantum
Information and Computation, 17(5-6):488–494, 2017. arXiv:1612.01011.
[23] StephenP.Jordan, KeithS.M.Lee, andJohnPreskill. Quantumalgorithmsforquan-
tumfieldtheories.Science,336(6085):1130–1133,2012.DOI:10.1126/science.1217069.
arXiv:1111.3633.
[24] B. P. Lanyon, C. Hempel, D. Nigg, M. Müller, R. Gerritsma, F. Zähringer,
P. Schindler, J. T. Barreiro, M. Rambach, G. Kirchmair, M. Hennrich, P. Zoller,
R. Blatt, and C. F. Roos. Universal digital quantum simulation with trapped ions.
Science, 334(6052):57–61, 2011. DOI: 10.1126/science.1208001. arXiv:1109.1512.
[25] SethLloyd. Universalquantumsimulators. Science, 273(5278):1073–1078, 1996. DOI:
10.1126/science.273.5278.1073.
[26] Guang Hao Low and Isaac L. Chuang. Optimal Hamiltonian simulation by quantum
signal processing. Physical Review Letters, 118:010501, 2017. DOI: 10.1103/Phys-
RevLett.118.010501. arXiv:1606.02685.
[27] Guang Hao Low and Isaac L. Chuang. Hamiltonian Simulation by Qubitization.
Quantum, 3:163, July 2019. DOI: 10.22331/q-2019-07-12-163. arXiv:1610.06546.
[28] Guang Hao Low, Vadym Kliuchnikov, and Nathan Wiebe. Well-conditioned multi-
product Hamiltonian simulation, 2019. arXiv:1907.11679.
[29] David Poulin, Angie Qarry, Rolando D. Somma, and Frank Verstraete. Quan-
tum simulation of time-dependent Hamiltonians and the convenient illusion of
Hilbert space. Physical Review Letters, 106(17):170501, 2011. DOI: 10.1103/Phys-
RevLett.106.170501. arXiv:1102.1360.
[30] David Poulin, Matthew B. Hastings, Dave Wecker, Nathan Wiebe, Andrew C. Do-
herty, and Matthias Troyer. The Trotter step size required for accurate quantum
simulation of quantum chemistry. Quantum Information and Computation, 15(5-6):
361–384, 2015. arXiv:1406.4920.
[31] Sadegh Raeisi, Nathan Wiebe, and Barry C. Sanders. Quantum-circuit design for
efficient simulations of many-body quantum dynamics. New Journal of Physics, 14:
103017, 2012. DOI: 10.1088/1367-2630/14/10/103017. arXiv:1108.4318.
[32] Markus Reiher, Nathan Wiebe, Krysta M. Svore, Dave Wecker, and Matthias Troyer.
Elucidating reaction mechanisms on quantum computers. Proceedings of the Na-
tional Academy of Sciences,114(29):7555–7560,2017. DOI:10.1073/pnas.1619152114.
arXiv:1605.03590.
[33] Masuo Suzuki. General theory of fractal path integrals with applications to many-
bodytheoriesandstatisticalphysics. Journal of Mathematical Physics,32(2):400–407,
1991. DOI: 10.1063/1.529425.
[34] JohnWatrous. Simplersemidefiniteprogramsforcompletelyboundednorms. Chicago
Journal of Theoretical Computer Science, 2013(8), 2013. DOI:10.4086/cjtcs.2013.008.
[35] John Watrous. The Theory of Quantum Information. Cambridge University Press,
2018. DOI: 10.1017/9781316848142.
[36] Dave Wecker, Bela Bauer, Bryan K. Clark, Matthew B. Hastings, and Matthias
Troyer. Gate count estimates for performing quantum chemistry on small quantum
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 19

computers. Physical Review A, 90:022305, 2014. DOI: 10.1103/PhysRevA.90.022305.
arXiv:1312.1695.
[37] Chi Zhang. Randomized algorithms for Hamiltonian simulation. In Leszek Plaskota
and Henryk Woźniakowski, editors, Monte Carlo and Quasi-Monte Carlo Methods
2010, pages 709–719, Berlin, Heidelberg, 2012. Springer Berlin Heidelberg. ISBN
978-3-642-27440-4. DOI: 10.1007/978-3-642-27440-4_42.
Accepted in Quantum 2019-08-26, click title to verify. Published under CC-BY 4.0. 20
