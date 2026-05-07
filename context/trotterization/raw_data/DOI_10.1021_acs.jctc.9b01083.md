Letter
|     |     |     |     |     |     |     | CiteThis:J.Chem.TheoryComput.2020,16,1−6 |     |     |     |     |     |     |     | pubs.acs.org/JCTC |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- |
fi
|     | Is the | Trotterized |     |     | UCCSD |     | Ansatz |     | Chemically |     | Well-De |     | ned? |     |     |
| --- | ------ | ----------- | --- | --- | ----- | --- | ------ | --- | ---------- | --- | ------- | --- | ---- | --- | --- |
Harper R. Grimsley,† Daniel Claudino,† Sophia E. Economou,‡ Edwin Barnes,‡
Mayhall*,†
|     | and Nicholas |     | J.  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
†
|     | Department | of  | Chemistry, | Virginia | Tech, | Blacksburg, |     | Virginia | 24061, | United | States |     |     |     |     |
| --- | ---------- | --- | ---------- | -------- | ----- | ----------- | --- | -------- | ------ | ------ | ------ | --- | --- | --- | --- |
‡
|     | Department | of  | Physics, | Virginia | Tech, | Blacksburg, |     | Virginia | 24061, | United States |     |     |     |     |     |
| --- | ---------- | --- | -------- | -------- | ----- | ----------- | --- | -------- | ------ | ------------- | --- | --- | --- | --- | --- |
*
|     | Supporting |     | Information |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S
|     | ABSTRACT: |     | Thevariationalquantumeigensolver(VQE)has |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
.selcitra dehsilbup erahs yletamitigel ot woh no snoitpo rof senilediuggnirahs/gro.sca.sbup//:sptth eeS
|                                                                            | emerged    | as one       | of             | the most | promising   |         | near-term    | quantum       |     |     |     |     |     |     |     |
| -------------------------------------------------------------------------- | ---------- | ------------ | -------------- | -------- | ----------- | ------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
| .)CTU( 80:42:02 ta 6202 ,6 yaM no YROTAROBAL LTAN EGDIR KAO aiv dedaolnwoD | algorithms | that         | can            | be used  | to simulate |         | many-body    | systems       |     |     |     |     |     |     |     |
|                                                                            | such as    | molecular    | electronic     |          | structures. | Serving | as           | an attractive |     |     |     |     |     |     |     |
|                                                                            | ansatz     | in the       | VQE algorithm, |          | unitary     | coupled | cluster      | (UCC)         |     |     |     |     |     |     |     |
|                                                                            | theory     | has seen     | a              | renewed  | interest    | in      | recent       | literature.   |     |     |     |     |     |     |     |
|                                                                            | However,   | unlike       | the            | original | classical   | UCC     | theory,      | implemen-     |     |     |     |     |     |     |     |
|                                                                            | tation     | on a quantum |                | computer | requires    | a       | finite-order | Suzuki-       |     |     |     |     |     |     |     |
Trotterdecompositiontoseparatetheexponentialsofthelarge
sumofPaulioperators.Whilepreviousliteraturehasrecognized
thenonuniquenessofdifferentorderingsoftheoperatorsinthe
|     | Trotterized | form | of UCC | methods,thequestion |     |     |     | of whether | or  |     |     |     |     |     |     |
| --- | ----------- | ---- | ------ | ------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
notdifferentorderingsmatteratthechemicalscalehasnotbeen
addressed.InthisLetter,weexploretheeffectofoperatororderingontheTrotterizedUCCSDansatz,aswellasthemuchmore
compact k-UpCCGSD ansatz recently proposed by Lee et al. [J. Chem. Theory Comput., 2019, 15, 311. arXiv, 2019, quant-
significant,
ph:1909.09114. https://arxiv.org/abs/1909.09114]. We observe a system-dependent variation in the energies of
different
Trotterizations with operator orderings. The energy variations occur on a chemical scale, sometimes on the order of
hundredsofkcal/mol.ThisLetterestablishestheneedtodefinenotonlytheoperatorspresentintheansatzbutalsotheorder
inwhichtheyappear.Thisisnecessaryforadheringtothequantumchemicalnotionofa“modelchemistry”,inadditiontothe
general importance of scientific reproducibility. As a final note, we suggest a useful strategy to select out of the combinatorial
|     |        |                   |     |          | well-defined |     |     | effective |          |                   |     |     |     |     |     |
| --- | ------ | ----------------- | --- | -------- | ------------ | --- | --- | --------- | -------- | ----------------- | --- | --- | --- | --- | --- |
|     | number | of possibilities, |     | a single |              |     | and |           | ordering | of the operators. |     |     |     |     |     |
T
heabilitytoaccuratelysimulatechemistryatthesubatomic expected to be realized in the near future, so-called Noisy
scientific
level can provide deeper insights and further IntermediateScaledQuantum(NISQ)devices4haveinteresting
reachingpredictionsthanthroughexperimentalone.Although properties that might still offer important computational
|     | exact simulation |     | requires | computational |     |     | resources | which |     |     |     |     |     |     |     |
| --- | ---------------- | --- | -------- | ------------- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
advantages.
first
increaseexponentiallywithsystemsize,manystablemolecules While the quantum algorithm proposed for simulating
can be accurately modeled using polynomially scaling many-bodysystems,thePhaseEstimationAlgorithm(PEA),1,5,6
techniques, providing accurate and interpretable results. providesapathforachievingarbitrarilyaccuratesimulations,it
|     | Examples | of such | approximations |     | include | density-functional |     |     |     |            |                        |     |      |           |                |
| --- | -------- | ------- | -------------- | --- | ------- | ------------------ | --- | --- | --- | ---------- | ---------------------- | --- | ---- | --------- | -------------- |
|     |          |         |                |     |         |                    |     |     |     | does so at | the cost of incredibly |     | deep | circuits. | Because device |
theory,perturbationtheory,orcoupled-clustertheory.Tostudy
noiseanderrorslimitthenumberofgatesthatcanbeappliedin
more complicated systems with many strongly correlated sequence,PEAisnotviableonNISQdevices.In2014,Peruzzo
electronssuchasthoseinvolvedinnumerouscatalyticsystems
|     |     |     |     |     |     |     |     |     |     | and co-workers | proposed | and | demonstrated |     | an alternative |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ------------ | --- | -------------- |
or materials applications, more general modeling solutions are algorithmtermedtheVariationalQuantumEigensolver(VQE)7
needed.
whichoffersuniqueadvantagesforNISQdevices.UnlikePEA,
|     | Quantum | simulation, |     | which | has recently |     | seen | a dramatic |     |     |     |     |     |     |     |
| --- | ------- | ----------- | --- | ----- | ------------ | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
VQElimitsthedepthofthecircuit,whichmakesitpossibleto
increaseinactivityduetorapiddevelopmentsinbothhardware
|     |                 |     |          |             |             |     |                |     |     | implement | on current | and near-term |     | devices. | However, this |
| --- | --------------- | --- | -------- | ----------- | ----------- | --- | -------------- | --- | --- | --------- | ---------- | ------------- | --- | -------- | ------------- |
|     | and algorithms, |     | provides | an exciting | possibility |     | for performing |     |     |           |            |               |     |          |               |
comesatthecostofanincreasednumberofmeasurementsand
approximation-freesimulationswithouttheexponentialcompu-
|     |     |     |     |     |     |     |     |     |     | the introduction | of a wave | function | ansatz | that | can limit the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | -------- | ------ | ---- | ------------- |
tationalcostplaguingclassicalsimulations.BecausetheHilbert
space of a single spin−orbital can be mapped to the Hilbert accuracy of the simulation (although our recent approach,
|     |     |     |     |     |     |     |     |     |     | ADAPT-VQE, | can remove | the | ansatz | error).8 | The initial |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------ | -------- | ----------- |
spaceofasinglequbit,theexponentialgrowthofthemolecular
|     |     |     |     |     |     |     |     |     |     | demonstration | of VQE7 | was | followed | by several | theoretical |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | -------- | ---------- | ----------- |
Hamiltonianismatchedbytheexponentialgrowthofaquantum
|     | computer’sHilbert |     | space.Consequently, |     |     | aquantum |     | computer |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ------------------- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
withonlytensoflogicalqubitscouldpotentiallydemonstratea Received: October29,2019
advantage.1−3
quantum While full error-correction is not Published: December16,2019
|     |     |     |     | ©2019AmericanChemicalSociety |     |     |     |     | 1   |     |     |     |     | DOI:10.1021/acs.jctc.9b01083 |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- |
J.Chem.TheoryComput.2020,16,1−6

| JournalofChemicalTheoryandComputation |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Letter |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
studies9−15
and demonstrations on other hardware such as Trotterizing the evolution operator, the goal is to reproduce
superconductingqubits10,14,16andtrappedions.17,18
|     |     |     |     |     |     |     |     | the dynamics | of  | the original | Hamiltonian. |     | Any | Trotter | error |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | ------------ | --- | --- | ------- | ----- |
AkeyingredientinVQEistheansatz,whichisimplemented destroys the dynamics, and thus convergence with respect to
asaquantumcircuitwhichconstructstrialwavefunctionsthat Trottererrorissought.25−27Incontrast,whenTrotterizingthe
aremeasuredandthenupdatedinaclassicaloptimizationloop. ansatz in VQE it is generally accepted that the variational
Thequalityoftheansatzultimatelydeterminestheaccuracyof optimization can, in practice, absorb most of the energy
difference
thesimulatedgroundstateenergyandproperties.Intheoriginal between the conventional UCCSD and the
proposal, the unitary variant of coupled-cluster theory was Trotterizedform.12,13,28
chosenasanansatzduetoseveralattractivefeatures: At this point we want to clarify some of the language used
above.DespitehavingusedtheSuzuki-Trotterapproximationas
| •   | Accurate: | Coupled-cluster |     |     | theory is among | the | most |     |     |     |     |     |     |     |     |
| --- | --------- | --------------- | --- | --- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
accurateclassicalmethodsformany-bodysimulation. amotivationforseparatingouttheansatzintoaproductform,it
| •   |      |          |     |         |            |                 |     | isnolongerappropriatetocallthisaTrotterapproximation.The |         |                    |     |        |        |     |           |
| --- | ---- | -------- | --- | ------- | ---------- | --------------- | --- | -------------------------------------------------------- | ------- | ------------------ | --- | ------ | ------ | --- | --------- |
|     | Well | studied: | The | unitary | variant of | coupled-cluster |     |                                                          |         |                    |     |        |        |     |           |
|     |      |          |     |         |            |                 |     | reason                                                   | is that | the Trotterization |     | occurs | before |     | parameter |
singlesanddoubles(UCCSD)hasbeenanalyzedindetail
optimization.Thus,oneisactuallyvariationallyoptimizingthe
inthecontextofclassicalsimulations.19−22
parametersoftheproductform,anditnolongerrelatestothe
•
|     | Unitary: | Because | a   | quantum | circuit implements |     | unitary |     |     |     |     |     |     |     |     |
| --- | -------- | ------- | --- | ------- | ------------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
conventionalUCCSD(inref29Evangelistaetal.refertothisas
|     | operations, |     | the unitary | nature | of UCCSD | makes | the |                  |     |      |           |     |        |          |     |
| --- | ----------- | --- | ----------- | ------ | -------- | ----- | --- | ---------------- | --- | ---- | --------- | --- | ------ | -------- | --- |
|     |             |     |             |        |          |       |     | the disentangled |     | form | of UCCSD, |     | opting | to avoid | the |
approachnaturalinaVQEcontext.
|     |     |     |     |     |     |     |     | Trotterization | language | altogether). |     | In  | fact, if | one were | to use |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ------------ | --- | --- | -------- | -------- | ------ |
The UCCSD ansatz is obtained by replacing the traditional the optimized parameters from the product form and insert
Hermitianclusteroperatortermsincoupledclustertheorywith them into the conventional UCCSD ansatz, the result would
anti-Hermitianoperators necessarilybehigherinenergy.Therefore,itisimportanttonote
|     |     |           |              |     |     |     |     |          |      | “Trotterized | form” |          |     |            |      |
| --- | --- | --------- | ------------ | --- | --- | --- | --- | -------- | ---- | ------------ | ----- | -------- | --- | ---------- | ---- |
|     |     |           |              |     |     |     |     | that the | term |              |       | referred | to  | throughout | this |
|     |     | e(cid:59) | ̂+(cid:59) ̂ |     |     |     |     |          |      |              |       |          |     |            |      |
|Ψ ⟩ = 1 2 |0⟩ Letter is not an approximation to the conventional UCCSD
UCCSD
|     |     |      |     |     |     |     |     | ansatz. It | is instead | a different | ansatz | altogether, |     | a point | easily |
| --- | --- | ---- | --- | --- | --- | --- | --- | ---------- | ---------- | ----------- | ------ | ----------- | --- | ------- | ------ |
|     |     | ̂ ∑θ | †a  | †a  |     |     |     |            |            |             |        |             |     |         |        |
(cid:59) = (a − a ) madebyrecognizing thattheTrotterized form cansometimes
|     |     | 1   | ia a | i i a |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ia yield a lower energy than the conventional, yet variational,
|     | (cid:59)̂ | ∑θ  | (a†a†aa |     | a†a†a |     |     | UCCSD. |     |     |     |     |     |     |     |
| --- | --------- | --- | ------- | --- | ----- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |           | =   |         | −   | a)    |     |     |        |     |     |     |     |     |     |     |
2 ijab a b i j j i b a Unfortunately, a problem of definition arises during
(1)
ijab Trotterization. Reordering the product approximation in eq 2
where|0⟩istheuncorrelatedreferencestate,usuallyHartree− doesnotgenerallygivethesameresult,exceptinthetrivialcase
†
Fock,a (a )isacreation(annihilation)operatorfortheorbital where the operators commute. With the number of operator
|     | p p |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
indexedbyp,and{θ ,θ }aretheparameterstobevariationally orderings being a path enumeration problem, the number of
|     |     |     | ia ijab |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimized. possible ansatzes produced during Trotterization (and poten-
|          |     |     |           |          |         |     |         | tially reported |     | in the literature) |     | is exponentially |     | large. | This, of |
| -------- | --- | --- | --------- | -------- | ------- | --- | ------- | --------------- | --- | ------------------ | --- | ---------------- | --- | ------ | -------- |
| Although |     | the | unitarity | of UCCSD | implies | an  | ease of |                 |     |                    |     |                  |     |        |          |
course,isnotanissueinUCCSD,asasumofoperatorshasno
| implementation |     | on  | quantum | hardware, | gate-based | quantum |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | ------- | --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
computingrequiresadecompositionofoperationsintoone-and dependenceontheorderinwhichtheyaresummed.
two-qubitgates,suchassingle-qubitrotationsandCNOTgates. The objective of this Letter is to determine if the term
|              |     |              |     |        |                 |     | (cid:59)̂ | “TrotterizedUCCSD”issufficientlywell-defined,suchthatthe |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ------ | --------------- | --- | --------- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| In contrast, |     | complicating |     | direct | implementation, |     | the       |                                                          |     |     |     |     |     |     |     |
n rangeofenergiescomingfromdifferentoperatororderingsfalls
| operators | simultaneously |     |     | act on | N qubits. In | principle, | any |             |        |             |     |          |        |              |     |
| --------- | -------------- | --- | --- | ------ | ------------ | ---------- | --- | ----------- | ------ | ----------- | --- | -------- | ------ | ------------ | --- |
|           |                |     |     |        |              |            |     | within some | notion | of chemical |     | accuracy | (e.g., | 1 kcal/mol), | a   |
unitaryoperationcanbedecomposedintoone-andtwo-qubit
gates.23 termreferredtointhetitleaschemicallywell-defined.Ifthatwere
However, the number of gates produced from such a “Trotterized UCCSD”
|     |     |     |     |     |     |     |     | the case, | then | the term |     |     |     | would | be well- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------- | --- | --- | --- | ----- | -------- |
decompositiongrowsrapidlywiththenumberofqubitsactedon
|        |          |                     |     |           |                   |               |         | defined,    | as an   | arbitrary | operator | ordering |          | would | produce  |
| ------ | -------- | ------------------- | --- | --------- | ----------------- | ------------- | ------- | ----------- | ------- | --------- | -------- | -------- | -------- | ----- | -------- |
| by the | unitary, | making              | it  | desirable | to use an         | approximation |         |             |         |           |          |          |          |       |          |
|        |          |                     |     |           |                   |               |         | practically | similar | results.  | However, | if       | changing | the   | operator |
| scheme | such     | as Suzuki-Trotter24 |     |           | when implementing |               | N-qubit |             |         |           |          |          |          |       |          |
orderingsignificantlychangestheaccuracyonachemicalscale,
unitaryoperators.
Thefirst-orderSuzuki-Trotterapproximationisgivenbyeq2. then it proves necessary to provide more information to fully
defineanansatzandtoprovidereproducibleresults.Toanswer
eÂ+B̂ eÂ eB̂ this question, we perform classical simulations with randomly
|     | ≈   |     |     |     |     |     | (2) |          |           |       |          |      |       |      |       |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | -------- | ---- | ----- | ---- | ----- |
|     |     |     |     |     |     |     |     | shuffled | operators | using | a custom | code | built | with | Open- |
Thisbecomesexactininfiniteorder:
|     |     |     |     |     |     |     |     | Fermion30 | and | Psi4,31 which | uses | the | gradient | algorithm | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | ---- | --- | -------- | --------- | --- |
̂ ̂ n d e v e lo p e d , w h ic h i s o u t li n e d i n t h e A p p e n d ix o f r ef 8 . T h e re su l ts
| eÂ+B̂ |     |     | A B |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
= lim e n e n u s i n g v a ri o u s o p er a t o r o r d e ri n g s a r e c o m p a re d t o b o t h U C C S D
|                |             | n→∞        |                                         |            |       |           | (3)   | a■ndFullCI(FCI).  |     |     |     |     |     |     |     |
| -------------- | ----------- | ---------- | --------------------------------------- | ---------- | ----- | --------- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| To             | approximate |            | UCCSD                                   | accurately | using | a product | form, |                   |     |     |     |     |     |     |     |
|                |             | i          | y                                       |            |       |           |       | NUMERICALEXAMPLES |     |     |     |     |     |     |     |
| largeTrotternu |             | jjj mbers, | zzz n,couldinprinciplebeused.Thiswould, |            |       |           |       |                   |     |     |     |     |     |     |     |
of course, creakte ext{remely deep circuits, making quantum We consider four molecules in the context of the UCCSD
simulation intractable. Alternatively, one could choose an ansatz,LiH,H ,BeH ,andN withits1sand2sorbitalsfrozen.
|     |     |     |     |     |     |     |     |     | 6   | 2   | 2   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aggressive truncation such as that in eq 2. In general, this All molecules are arranged in uniform, linear geometries with
wouldprovideaverypoorapproximationtotheUCCSDwave varying interatomic distances. For each system, we classically
function but would provide a relatively shallow circuit that is simulatethecalculationofapotentialenergycurveusingalarge
betterforNISQrealization.Notethestarkdifference between numberofrandomoperatororderings.
theeffectof“Trotterizing”theansatzinVQEandTrotterizing For each system, the minimal STO-3G basis is used to
the time-evolution operator for algorithms like PEA. In minimizecomputationalcost(theimplementationsusethefull
|     |     |     |     |     |     |     |     | 2   |     |     |     |     | DOI:10.1021/acs.jctc.9b01083 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
J.Chem.TheoryComput.2020,16,1−6

JournalofChemicalTheoryandComputation Letter
Figure1.PotentialenergycurvesrelativetotheFCIdissociationlimitofeachsystemfor,fromlefttoright,H,LiH,BeH,andN (top)anderrors
6 2 2
fromFCI(bottom)fortheUCCSDansatz.
Hilbertspaceoftheorbitals),andtherestrictedHartree−Fock RegardlessofTrotterordering,thecurvesareallextremelygood
(RHF) singlet state is chosen as the reference state. The one- approximations.
andtwo-electronintegralsarecomputedwiththePsi4quantum SimilartoH ,BeH exhibitsasimultaneousquickriseinthe
6 2
chemicalpackage.31TheHamiltonian,anti-Hermitianoperators ordering variance and UCCSD energy error. However, unlike
in the UCCSD ansatz, and reference state are formed in the H , the ordering variance decreases again after bond breaking,
6
qubit basis using the Jordan-Wigner transform in Open- along with the UCCSD energy error. The range of values
Fermion.30 At this point, the various orderings of ansatzes are obtained from different orderings is of the same order of
constructed,andtheirparameters{θ ,θ }areoptimizedbythe magnitudeastheactualabsoluteerroroftheUCCSDenergy.
ia ijab
SciPyimplementationofBFGS.32 Thepotentialenergycurves UnlikebothH andBeH ,theUCCSDcurveforN doesnot
6 2 2
aredisplayedinFigure1alongwithstandarddeviationplotsand decreaseinerrorafterbondbreakingbutratherflattensouttoa
range plots. We additionally compare the random Trotter nearly constant error of around 10 kcal/mol. The ordering
orderings to a “sequential gradient ordering” (SGO), a quasi- variance increases alongside the UCCSD error and also levels
deterministic method where one operator with the largest out, despite a significant jump occurring around 3.5 Å in the
gradient is added at a time, according to the prescription rangeofenergyvaluesobtainedfromtheTrotterizedansatzes.
followedbytheADAPT-VQEansatzconstruction.However,in Thisisduetoatleastoneoftheoperatororderingsgettingstuck
contrasttotheADAPT-VQE,theSGOapproachrefrainsfrom inalocalminimum(thevariationalparametersareinitializedto
allowing inclusion of more than one instance of the same 0),whichisaconsequenceofthehighlynonlinearnatureofthe
operator so that a direct comparison to the original UCCSD optimization.
resultscanbemade. Overall, we find that when static correlation appears, the
A cursory evaluation of the data suggests that the variance energy differences between orderings increase. This can be
amongdifferentansatzesincreaseswithstaticcorrelationofthe understoodfromthefactthatthedifferencesbetweenoperator
chemical system. Because these tend to be the systems of orderings depend on the commutators of the operators, and
greatest chemical interest for VQE since they represent these in turn depend on the optimal parameter values, which
classically hard problems, the ability to choose good Trotter tend to be larger when the electron correlation is stronger. (A
orderingsiscritical. system with no electron correlation would have an optimal
The UCCSD results for the first molecular PES, H , are solution with all parameters equal to zero.) As such it makes
6
characterized by an accurate description near the equilibrium sensethatformorestronglycorrelatedsystems,thedifferences
region,aquickincreaseinerroruponbondbreaking,andthena between operator orderings increase. While uniquely well-
similarlyrapiddecreaseinerrorasthebondisfurtherstretched defined (up to orderings of operators with degenerate
todissociation.Withfive“bonds”beingbrokensimultaneously, gradients), the sequential gradient ordering scheme does not
itisexpectedthatUCCSDshouldfailtoaccuratelydescribethis appeartobereliablybetterorworsethanotherorderings.
system. One interesting observation from this plot is that the AlternativeWaysTo Reorder Operators.InFigure1, a
ordering variance (the statistical variance of the energies comparison is made between the un-Trotterized ansatz and a
computed with randomly shuffled operators) increases as the seriesofrandomlyshuffledTrotterizations.However,onecould
UCCSD error increases. In contrast to H , LiH is a relatively group the operators by excitation rank before Trotterization.
6
simple system, and we observe negligible ordering variance. Thiswouldresultinasignificantlyreducedsamplingspaceand
3 DOI:10.1021/acs.jctc.9b01083
J.Chem.TheoryComput.2020,16,1−6

| JournalofChemicalTheoryandComputation |         |      |              |     |          |          |     |     |     |     |     |     |     |     | Letter |
| ------------------------------------- | ------- | ---- | ------------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
| potentially                           | provide | more | consistently |     | accurate | results. | To  |     |     |     |     |     |     |     |        |
addressthispossibility,wehavecomputedtheperformanceof
| multiple | different | orderings, | such | as grouping |     | singles | first and |     |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | ---- | ----------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
doublessecondordoublesfirstandsinglessecond.Fromthese
| results, we | find | that it | is generally | favorable |     | to apply | double |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------- | ------------ | --------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
excitationstothereferencefirst,followedbysingles.Thisdatais
providedintheSupportingInformation.
k-UpCCGSD.FromtheresultsinFigure1,wenoticethatthe
| ordering | variance | increases | with | error | in the | associated | un- |     |     |     |     |     |     |     |     |
| -------- | -------- | --------- | ---- | ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Trotterizedansatz.ItseemsthenthatwhenUCCSDisaccurate,
theremaybeanexcessofoperators,suchthattheextraoperators
(whilenotnecessaryforaccurateenergyestimates)areusefulin
| minimizing | the      | differences | between     |           | different | Trotterization |           |     |     |     |     |     |     |     |     |
| ---------- | -------- | ----------- | ----------- | --------- | --------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| orderings. | To       | test this   | hypothesis, |           | we have   | additionally   |           |     |     |     |     |     |     |     |     |
| considered | the more | compact     |             | k-UpCCGSD |           | ansatz         | by Lee et |     |     |     |     |     |     |     |     |
al.,15whichhasfarfewerparameters(forsmallk)thanUCCSD,
| where k | controls | the | number | of variational |     | parameters | by  |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | ------ | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
consideringkproductsoftheansatzwithallgeneralizedpaired
doublesandorbitalrotations:
Figure2.PotentialenergycurvesrelativetotheFCIdissociationlimit
k
∏ (eT̂(i)−T̂(i)† o f H 6 in to s ix h y dr o g e n a t o m s ( to p ) a nd err o r s fr o m F C I ( b ottom)for
| |Ψ  | ⟩   | =   |     | )|0⟩ |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k‐UpCCGSD th e 1 -U p C C G S D ( l e ft ) a n d 2 - U p C C G SD ( r ig h t ) an sa tz e s .
(4)
i=1
| The k-UpCCGSD |     |     | ansatz | is a more | economical |     | para- |          |                |     |          |        |       |         |     |
| ------------- | --- | --- | ------ | --------- | ---------- | --- | ----- | -------- | -------------- | --- | -------- | ------ | ----- | ------- | --- |
|               |     |     |        |           |            |     |       | into six | noninteracting |     | hydrogen | atoms. | These | results | are |
metrizationwhereonlytheoperatorswhichareexpectedtobe
consistentwiththeobservationsfoundinref33,whichnoticed
mostimportantareincluded.Thistranslatesintohavingfewer
thatfork=1therewerelargedifferencesinenergydependingon
excessparameters,suchthathigheraccuracycanbereachedwith
whetheronegroupedorsplitthesinglesanddoublesexcitations.
acomparablecircuitdepthbyincreasingk.Basedonourresults Ansatzeswithdifferentoperatorgroupingsstarttodeviateinthe
above,wewouldanticipateahigherorderingvarianceforsmall
vicinityoftheCoulson-Fischerpoint.Inthisregion,noneofthe
valuesofk(largerthanUCCSD),butthatbyincreasingk,one
|          |            |       |      |      |              |     |           | orderings | that were         | sampled | for            | the 1-UpCCGSD |     | operators |           |
| -------- | ---------- | ----- | ---- | ---- | ------------ | --- | --------- | --------- | ----------------- | ------- | -------------- | ------------- | --- | --------- | --------- |
| can make | the energy | error | (and | thus | the ordering |     | variance) |           |                   |         |                |               |     |           |           |
|          |            |       |      |      |              |     |           | approach  | the corresponding |         | un-Trotterized |               | and | FCI       | energies. |
arbitrarilysmall.Ontheotherhand,itisworthmentioningthat
|                 |     |          |               |     |      |             |     | Some of     | the ansatzes | are              | able | to get back | on    | track in | closely |
| --------------- | --- | -------- | ------------- | --- | ---- | ----------- | --- | ----------- | ------------ | ---------------- | ---- | ----------- | ----- | -------- | ------- |
| the improvement |     | attained | by increasing |     | k is | accompanied | by  |             |              |                  |      |             |       |          |         |
|                 |     |          |               |     |      |             |     | approaching | the          | FCI dissociation |      | limit,      | along | with     | the un- |
placingaheavierburdenontheclassicaloptimizer,asittendsto
Trotterized1-UpCCGSDenergies.Theseansatzeshappentobe
| exacerbate | the | highly nonlinear |     | character | of  | the underlying |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
largelycomprisedofdoubleexcitationoperatorsflockedcloser
optimization,makingitdifficulttolocatetheglobalminimum.
tothereferencedeterminant,whichisinlinewiththefindings
| Moreover,  | the minima |                    | found | by the | optimizer   | show        | strong |            |              |      |               |               |        |          |        |
| ---------- | ---------- | ------------------ | ----- | ------ | ----------- | ----------- | ------ | ---------- | ------------ | ---- | ------------- | ------------- | ------ | -------- | ------ |
|            |            |                    |       |        |             |             |        | from the   | simulations  | with | the           | SD orderings, |        | provided | in the |
| dependence | on         | the initialization |       | of the | variational | parameters. |        |            |              |      |               |               |        |          |        |
|            |            |                    |       |        |             |             |        | Supporting | Information. |      | The 1-UpCCGSD |               | ansatz | tracks   | well   |
Onewaythiscanbecircumventedinthecasesinvolvingtheun-
|     |     |     |     |     |     |     |     | the FCI | results, | being able | to  | provide | the correct | qualitative |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | --- | ------- | ----------- | ----------- | --- |
Trotterizedversionofthek-UpCCGSD,aspresentedineq4,is
toperformmanysimulationswiththevariationalparametersθ⃗ behavioralongthePES.However,thisansatzisquitecompact,
|     |     |     |     |     |     |     |     | and its | limited | number | of parameters |     | impairs | its ability | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ------------- | --- | ------- | ----------- | --- |
initializedatrandom,assuggestedinref15andcarriedouthere
|     |     |     |     |     |     |     |     | variationally | achieve | results | that | are quantitatively |     | comparable |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------- | ---- | ------------------ | --- | ---------- | --- |
byrepeatingthesimulationsateachbondlength100timesand
|     |     |     |     |     |     |     |     | to FCI. | The operator |     | ordering | originated |     | from the | SGO |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | -------- | ---------- | --- | -------- | --- |
takingthelowestenergyvalueastheglobalminimumforeach
|     |     |     |     |     |     |     |     | construction | closely | follows | the | lowest | energies | from | random |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | --- | ------ | -------- | ---- | ------ |
geometry.Thisleadstopotentialenergycurvesfork=1,2that
|     |     |     |     |     |     |     |     | operator | samplings. | It is | worth | pointing | out | that it is | able to |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----- | ----- | -------- | --- | ---------- | ------- |
aresmoothintheenergyscalerelevantinthecurrentcontext.
|     |     |     |     |     |     |     |     | overcome | the deficiencies |     | around | the | Coulson-Fischer |     | point |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------ | --- | --------------- | --- | ----- |
Thevariationalparametersareinitializedat0forallTrotterized
|     |     |     |     |     |     |     |     | and asymptotically |     | recover | the | exact (FCI) | dissociation |     | limit, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | --- | ----------- | ------------ | --- | ------ |
ansatzesconstructedbasedoneq4,inlinewithwhatisdetailed
|                                                      |     |     |     |     |     |     |     | whereas | the corresponding |         |             | un-Trotterized |        | ansatz | cannot |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | ------- | ----------- | -------------- | ------ | ------ | ------ |
| fortheUCCSDansatzandwhoseresultsaredisplayedinFigure |     |     |     |     |     |     |     |         |                   |         |             |                |        | H−H    |        |
|                                                      |     |     |     |     |     |     |     | account | for all the       | missing | correlation |                | as the | bonds  | are    |
1.
|                                   |         |          |            |     |                 |          |        | stretched. | Because | in the    | SGO | ansatz the     | operators | are        | added |
| --------------------------------- | ------- | -------- | ---------- | --- | --------------- | -------- | ------ | ---------- | ------- | --------- | --- | -------------- | --------- | ---------- | ----- |
| Figure2showssimulationresultsforH |         |          |            |     | withk=1,2for100 |          |        |            |         |           |     |                |           |            |       |
|                                   |         |          |            |     | 6               |          |        | according  | to the  | magnitude | of  | their gradient |           | component, | an    |
| randomly                          | sampled | operator | groupings. |     | Several         | features | of the |            |         |           |     |                |           |            |       |
ansatzwithidenticaloperators,suchask-UpCCGSDwithk>1
different
| performance | of  | the | Trotterized |     | versions | of  | 1- and 2- |           |               |     | defined |     |         |        |        |
| ----------- | --- | --- | ----------- | --- | -------- | --- | --------- | --------- | ------------- | --- | ------- | --- | ------- | ------ | ------ |
|             |     |     |             |     |          |     |           | cannot be | unambiguously |     |         | and | that is | why we | do not |
UpCCGSDagreewiththeresultsfortheTrotterizedversionsof
reportsuchresultsinFigure2.
theUCCSDansatz.Forshortbonddistances(<1.1Å),thereis
Thedisparitiesamongoperatorgroupingsarelargelyremoved
| anevidentinsensitivityof |     |     | theenergywithrespect |     |     | toaspecific |     |                |     |               |        |        |     |          |     |
| ------------------------ | --- | --- | -------------------- | --- | --- | ----------- | --- | -------------- | --- | ------------- | ------ | ------ | --- | -------- | --- |
|                          |     |     |                      |     |     |             |     | all throughout |     | the potential | energy | curves | by  | doubling | the |
samplingoftheoperators.Despitebeingalreadyfairlysmallin
numberofvariationalparameters,accomplishedbysettingk=2.
thisregimewithk=1,thisdistinctionislargelyquenchedwhenk
differently Wepreservethesameorderingsstudiedfork=1,thatis,wehave
| = 2, rendering |     | the results | with |     | sampled |     | ansatzes |           |        |             |     |             |            |     |         |
| -------------- | --- | ----------- | ---- | --- | ------- | --- | -------- | --------- | ------ | ----------- | --- | ----------- | ---------- | --- | ------- |
|                |     |             |      |     |         |     |          | a product | of two | Trotterized |     | exponential | generators |     | wherein |
visuallyidenticalonthescaleoftheplots.
operatorsarenotshuffledacrossthetwoinstancesofeT̂(i)−T̂(i)†
| The most | remarkable |     | divergences |     | among | the | operator |     |     |     |     |     |     |     | .   |
| -------- | ---------- | --- | ----------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
groupingsandthesizeofthegenerator,thatis,k=1vsk=2, Except for a slight spread surrounding the Coulson-Fischer
areobservedwhenmovingtowardthelimitof H dissociating point which is the region most strongly correlated in the
6
|     |     |     |     |     |     |     |     | 4   |     |     |     |     | DOI:10.1021/acs.jctc.9b01083 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
J.Chem.TheoryComput.2020,16,1−6

| JournalofChemicalTheoryandComputation |     |     |     |     |     |     |     | ■   |     |     |     |     |     |     | Letter |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
potentialenergycurve,allofthedifferentansatzesbehaveina
ACKNOWLEDGMENTS
| strikingly | similar | fashion. | The | errors are | largest | in this | region, |     |     |     |     |     |     |     |     |
| ---------- | ------- | -------- | --- | ---------- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ThisresearchwassupportedbytheU.S.DepartmentofEnergy
| and keeping | in  | mind | the different | scales | in  | the plots | when |        |                   |     |     |     |              |         |     |
| ----------- | --- | ---- | ------------- | ------ | --- | --------- | ---- | ------ | ----------------- | --- | --- | --- | ------------ | ------- | --- |
|             |     |      |               |        |     |           |      | (Award | No. DE-SC0019199) |     |     | and | the National | Science |     |
changingk,theyaresignificantlymitigatedincomparisonwithk
|           |               |     |             |     |         |        |        | Foundation | (Award     | No. | 1839136).        | S.E.E. | also | acknowledges |      |
| --------- | ------------- | --- | ----------- | --- | ------- | ------ | ------ | ---------- | ---------- | --- | ---------------- | ------ | ---- | ------------ | ---- |
| = 1, with | all orderings |     | approaching |     | the FCI | energy | in the |            |            |     |                  |        |      |              |      |
|           |               |     |             |     |         |        |        | support    | from Award |     | No. DE-SC0019318 |        |      | from the     | U.S. |
dissociationlimit.Theadvantageduetoalargersetofvariational D■epartmentofEnergy.
parametersisalsoreflectedintheun-Trotterizedversionofthe
| ansatz, | 2-UpCCGSD, |     | whose | dissociation | curve | practically |     |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ----- | ------------ | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| overlays | with the | FCI | results. | The significant | improvement |     | in  |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | -------- | --------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theresultswithk=2,accompaniedbyavirtuallyabsentspread (1) Aspuru-Guzik, A.; Dutoi, A. D.; Love, P. J.; Head-Gordon, M.
energies,isinagreementwiththefindingsof SimulatedQuantumComputationofMolecularEnergies.Science2005,
| inthecomputed |     |     |     |     |     |     |     | 309,1704−1707. |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
al.,15
| Lee et | which | implies |     | that these | ansatzes | are relatively |     |     |     |     |     |     |     |     |     |
| ------ | ----- | ------- | --- | ---------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(2)McArdle,S.;Endo,S.;Aspuru-Guzik,A.;Benjamin,S.;Yuan,X.
insensitivetotheorderingoftheoperators.
■ Quantumcomputationalchemistry.2018,arXiv:1808.10402.https://
arxiv.org/abs/1808.10402(accessedDec17,2019).
CONCLUSIONS (3)Cao,Y.;Romero,J.;Olson,J.P.;Degroote,M.;Johnson,P.D.;
Kieferova,́
M.;Kivlichan,I.D.;Menke,T.;Peropadre,B.;Sawaya,N.P.
InthisLetter,wesoughttodetermineiftheoperatororderingin
D.;Sim,S.;Veis,L.;Aspuru-Guzik,A.QuantumChemistryintheAge
Trotterized UCCSD impacts the results in a “chemically ofQuantumComputing.Chem.Rev2019,119,10856−10915.
| meaningful” | way, | such | that | the differences | between |     | unique |               |            |     |           |        |      |         |         |
| ----------- | ---- | ---- | ---- | --------------- | ------- | --- | ------ | ------------- | ---------- | --- | --------- | ------ | ---- | ------- | ------- |
|             |      |      |      |                 |         |     |        | (4) Preskill, | J. Quantum |     | Computing | in the | NISQ | era and | beyond. |
differ
| operator | orderings | produce | results | which |     | on a chemical |     | Quantum2018,2,79. |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ------- | ----- | --- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
scale, i.e., greater than 1 kcal/mol. Our numerical simulations (5)Kitaev,A.Y.QuantummeasurementsandtheAbelianStabilizer
clearlydemonstratethattheoperatororderinghasasignificant Problem. 1995. quant-ph/9511026. arXiv e-prints. https://arxiv.org/
effect (large energy differences between orderings) only when abs/quant-ph/9511026(accessedDec17,2019).
there is a significant amountof electron correlation. However, (6) Lloyd, S. Universal Quantum Simulators. Science 1996, 273,
1073−1078.
| the renewed | interest |     | in UCCSD | (and | the relevance |     | of the |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | -------- | ---- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
(7)Peruzzo,A.;McClean,J.;Shadbolt,P.;Yung,M.-H.;Zhou,X.-Q.;
Trotterized form) is due to the use of the UCCSD ansatz in O’Brien,
|                 |     |            |     |            |          |            |     | Love, P. | J.; Aspuru-Guzik, |     | A.; | J. L. | A variational | eigenvalue |     |
| --------------- | --- | ---------- | --- | ---------- | -------- | ---------- | --- | -------- | ----------------- | --- | --- | ----- | ------------- | ---------- | --- |
| VQE simulations |     | on quantum |     | computers. | Strongly | correlated |     |          |                   |     |     |       |               |            |     |
solveronaphotonicquantumprocessor.Nat.Commun.2014,5,4213.
moleculesaretheprimarytargetofquantumsimulations,andso
(8)Grimsley,H.R.;Economou,S.E.;Barnes,E.;Mayhall,N.J.An
thismakestheissueofoperatororderingevenmoreimportant.
|     |     |     |     |     |     |     |     | adaptive | variational | algorithm | for exact | molecular |     | simulations | on a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --------- | --------- | --------- | --- | ----------- | ---- |
Consequently,theresultsinthispaperemphasizethattoensure quantumcomputer.Nat.Commun.2019,10,3007.
scientificreproducibility,itisnecessaryforauthorstoreportthe
(9)McClean,J.R.;Romero,J.;Babbush,R.;Aspuru-Guzik,A.The
specific orderings used in simulations involving Trotterized theoryofvariationalhybridquantum-classicalalgorithms.NewJ.Phys.
| ansatzes. | These | results | strongly | advocate | for | the use | of a | 2016,18,023023. |     |     |     |     |     |     |     |
| --------- | ----- | ------- | -------- | -------- | --- | ------- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- |
(10)O’Malley,P.;etal.ScalableQuantumSimulationofMolecular
| dynamic   | ansatz  | which       | uniquely | determines  |     | the operator |       |                                   |     |     |     |     |     |     |     |
| --------- | ------- | ----------- | -------- | ----------- | --- | ------------ | ----- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |         | ADAPT-VQE,8 |          |             |     |              |       | Energies.Phys.Rev.X2016,6,031007. |     |     |     |     |     |     |     |
| ordering, | such as |             |          | or adopting | an  | ansatz       | which |                                   |     |     |     |     |     |     |     |
(11)McClean,J.R.;Kimchi-Schwartz,M.E.;Carter,J.;deJong,W.A.
| does not | require | trotterization |     | (such | as the | Jastrow-based |     |     |     |     |     |     |     |     |     |
| -------- | ------- | -------------- | --- | ----- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hybridquantum-classicalhierarchyformitigationofdecoherenceand
| approach | in ref | 33). Our | findings | also | suggest | that there | are |     |     |     |     |     |     |     |     |
| -------- | ------ | -------- | -------- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
determinationofexcitedstates.Phys.Rev.A:At.,Mol.,Opt.Phys.2017,
| systematic | patterns | to  | which | Trotter | orderings | will give | the |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | ------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
95,042308.
| lowest energy, |     | offering | a useful | route | to defining | useful | and |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | -------- | ----- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(12)Barkoutsos,P.K.;Gonthier,J.F.;Sokolov,I.;Moll,N.;Salis,G.;
uniqueoperatororderings. ■ Fuhrer, A.; Ganzhorn, M.; Egger, D. J.; Troyer, M.; Mezzacapo, A.;
|     |     |     |     |     |     |     |     | Filipp, S.; | Tavernelli, | I. Quantum | algorithms |     | for electronic | structure |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---------- | ---------- | --- | -------------- | --------- | --- |
ASSOCIATEDCONTENT calculations: Particle-hole Hamiltonian and optimized wave-function
expansions.Phys.Rev.A:At.,Mol.,Opt.Phys.2018,98,022322.
*
S SupportingInformation (13)Romero,J.;Babbush,R.;McClean,J.R.;Hempel,C.;Love,P.J.;
The Supporting Information is available free of charge at Aspuru-Guzik,A.Strategiesforquantumcomputingmolecularenergies
usingtheunitarycoupledclusteransatz.QuantumSci.Technol.2019,4,
https://pubs.acs.org/doi/10.1021/acs.jctc.9b01083.
014008.
Plotsforsimulationswithoperatorsshuffledonlywithin (14)Colless,J.I.;Ramasesh,V.V.;Dahlen,D.;Blok,M.S.;Kimchi-
excitationranksetsanddetailsonhowtoaccesscodeused Schwartz,M.E.;McClean,J.R.;Carter,J.;deJong,W.A.;Siddiqi,I.
toobtainresults(PDF) ComputationofMolecularSpectraonaQuantumProcessorwithan
Error-ResilientAlgorithm.Phys.Rev.X2018,8,011021.
Specific operator orderings and corresponding energy (15) Lee, J.; Huggins, W. J.; Head-Gordon, M.; Whaley, K. B.
valuesfordatausedinFigure2(XLSX) Generalized Unitary Coupled Cluster Wave functions for Quantum
Computation.J.Chem.TheoryComput.2019,15,311−324.
■
(16)Kandala,A.;Mezzacapo,A.;Temme,K.;Takita,M.;Brink,M.;
AUTHORINFORMATION Chow,J.M.;Gambetta,J.M.Hardware-efficientvariationalquantum
eigensolverforsmallmoleculesandquantummagnets.Nature2017,
549,242−246.
CorrespondingAuthor
*E-mail:nmayhall@vt.edu. (17)Shen,Y.;Zhang,X.;Zhang,S.;Zhang,J.-N.;Yung,M.-H.;Kim,
|     |     |     |     |     |     |     |     | K. Quantum | implementation |     | of  | the unitary | coupled | cluster | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | --- | ----------- | ------- | ------- | --- |
ORCID
simulatingmolecularelectronicstructure.Phys.Rev.A:At.,Mol.,Opt.
DanielClaudino:0000-0002-8860-0689
Phys.2017,95,020501.
NicholasJ.Mayhall:0000-0002-1312-9781 (18)Hempel,C.;Maier,C.;Romero,J.;McClean,J.;Monz,T.;Shen,
H.;Jurcevic,P.;Lanyon,B.P.;Love,P.;Babbush,R.;Aspuru-Guzik,A.;
Notes
Blatt,R.;Roos,C.F.QuantumChemistryCalculationsonaTrapped-
Theauthorsdeclarenocompetingfinancialinterest.
IonQuantumSimulator.Phys.Rev.X2018,8,031022.
|     |     |     |     |     |     |     |     | 5   |     |     |     |     | DOI:10.1021/acs.jctc.9b01083 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
J.Chem.TheoryComput.2020,16,1−6

JournalofChemicalTheoryandComputation Letter
(19) Bartlett, R. J.; Kucharski, S. A.; Noga, J. Alternative coupled-
clusteransaẗzeII.Theunitarycoupled-clustermethod.Chem.Phys.Lett.
1989,155,133−140.
(20) Kutzelnigg, W. Error analysis and improvements of coupled-
clustertheory.Theoret.Chim.Acta1991,80,349−386.
(21)Taube,A.G.;Bartlett,R.J.Newperspectivesonunitarycoupled-
clustertheory.Int.J.QuantumChem.2006,106,3393−3401.
(22) Harsha, G.; Shiozaki, T.; Scuseria, G. E. On the difference
betweenvariationalandunitarycoupledclustertheories.J.Chem.Phys.
2018,148,044107.
(23) Nielsen, M. A.; Chuang, I. L. Quantum Computation and
Quantum Information, 10th Anniversary ed.; Cambridge University
Press:2010.
(24)Hatano,N.;Suzuki,M.FindingExponentialProductFormulasof
HigherOrders.InQuantumAnnealingandOtherOptimizationMethods;
Springer: Berlin, Heidelberg, 2005; pp 37−68, DOI: 10.1007/
11526216_2.
(25)Babbush,R.;McClean,J.;Wecker,D.;Aspuru-Guzik,A.;Wiebe,
N. Chemical Basis of Trotter-Suzuki Errors in Quantum Chemistry
Simulation.Phys.Rev.A:At.,Mol.,Opt.Phys.2015,91,022311.
(26)Heyl,M.;Hauke,P.;Zoller,P.QuantumLocalizationBounds
TrotterErrorsinDigitalQuantumSimulation.ScienceAdvances2019,
5,No.eaau8342.
(27) Sieberer, L. M.; Olsacher, T.; Elben, A.; Heyl, M.; Hauke, P.;
Haake,F.;Zoller,P.DigitalQuantumSimulation,TrotterErrors,and
QuantumChaosoftheKickedTop.npjQuantumInformation2019,5,
78.
(28)Rubin,N.C.AHybridClassical/QuantumApproachforLarge-
Scale Studies of Quantum Systems with Density Matrix Embedding
Theory.2016.arXiv:1610.06910[cond-mat,physics:quant-ph].arXiv:
1610.06910. https://arxiv.org/abs/1610.06910 (accessed Dec 17,
2019).
(29) Evangelista, F. A.; Chan, G. K.-L.; Scuseria, G. E. Exact
Parameterization of Fermionic Wave Functions via Unitary Coupled
Cluster Theory. 2019. arXiv:1910.10130 [cond-mat, physics:physics,
physics:quant-ph]. https://arxiv.org/abs/1910.10130 (accessed Dec
17,2019).
(30) McClean, J. R. et al. OpenFermion: The Electronic Structure
Package for Quantum Computers. 2017, arXiv:1710.07629 [physics,
physics:quant-ph]. arXiv: 1710.07629. https://arxiv.org/abs/1710.
07629(accessedDec17,2019).
(31) Parrish, R. M.; et al. Psi4 1.1: An Open-Source Electronic
StructureProgramEmphasizingAutomation,AdvancedLibraries,and
Interoperability.J.Chem.TheoryComput.2017,13,3185−3197.
(32)Fletcher,R.PracticalMethodsof Optimization,2nded.;Wiley-
Interscience: New York, NY, USA, 1987; DOI: 10.1002/
9781118723203.
(33)AJastrow-TypeDecompositioninQuantumChemistryforLow-
Depth Quantum Circuits. [1909.12410v1]. https://arxiv.org/abs/
1909.12410v1(accessedDec17,2019).
6 DOI:10.1021/acs.jctc.9b01083
J.Chem.TheoryComput.2020,16,1−6