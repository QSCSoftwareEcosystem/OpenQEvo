Received:15March2024 Revised:8May2024 Accepted:9May2024
DOI:10.1002/jcc.27438
RESEARCH ARTICLE
Size-consistency and orbital-invariance issues revealed
by VQE-UCCSD calculations with the FMO scheme
Kenji Sugisaki1,2,3 | Tatsuya Nakano4 | Yuji Mochizuki5,6
1GraduateSchoolofScienceandTechnology,KeioUniversity,Kawasaki,Japan
2QuantumComputingCenter,KeioUniversity,Yokohama,Japan
3CentreforQuantumEngineering,ResearchandEducation,TCGCentresforResearchandEducationinScienceandTechnology,Kolkata,India
4DivisionofMedicinalSafetyScience,NationalInstituteofHealthSciences,Kawasaki,Japan
5DepartmentofChemistryandResearchCenterforSmartMolecules,FacultyofScience,RikkyoUniversity,Toshima-ku,Japan
6InstituteofIndustrialScience,TheUniversityofTokyo,Meguro-ku,Japan
Correspondence
KenjiSugisaki,GraduateSchoolofScience Abstract
andTechnology,KeioUniversity,7-1 Thefragmentmolecularorbital(FMO)schemeisoneofthepopularfragmentation-based
ShinkawasakiSaiwai-ku,Kawasaki,
Kanagawa212-0032,Japan. methods and has the potential advantage of making the circuit shallow for quantum
Email:ksugisaki@keio.jp chemicalcalculationsonquantumcomputers.Inthisstudy,weusedaGPU-accelerated
Presentaddress quantum simulator (cuQuantum) to perform the electron correlation part of the FMO
TatsuyaNakano,DepartmentofHPCSupport, calculation as unitary coupled-cluster singles and doubles (UCCSD) with the variational
ResearchOrganizationforInformationScience
andTechnology,Kobe,Japan. quantum eigensolver (VQE) for hydrogen-bonded (FH) 3 and (FH) 2 -H 2 O systems with
theSTO-3Gbasisset. VQE-UCCSDcalculationswereperformedusingbothcanoni-
Fundinginformation
MinistryofEducation,Culture,Sports,Science caland localized MOsets, and theresults wereexamined from the pointof view of
andTechnology;JapanSocietyforthe size-consistency and orbital-invariance affected by the Trotter error. It was found
PromotionofScience;JapanScienceand
TechnologyAgency;RikkyoSFR that the use of localized MO leads to better results, especially for (FH) 2 -H 2 O. The
GPU acceleration was substantial for the simulations with larger numbers of qubits,
andwasaboutafactorof6.7–7.7for18qubitsystems.
KEYWORDS
fragmentmolecularorbital,GPU,Trottererror,UCC,variationalquantumeigensolver
1 | INTRODUCTION devices. For noisy intermediate-scale quantum (NISQ) computers,
theunitarycoupled-clustersinglesanddoubles(UCCSD)9–17hasbeen
Starting with the seminal work of Aspuru-Guzik et al.,1 quantum used for relatively small molecules in conjunction with the variational
chemicalcomputationhasbeenactivelyexploredanddevelopedas quantumeigensolver(VQE),18–21andthisVQE-UCCSDschemehasbeen
apromisingapplicationareaforquantumcomputers,2–6wherethe extended to multi-reference cases, for example, References 22–25. In
potentialapplicabilitytohuge-scaleconfigurationinteractionssuch addition,GPU-acceleratedsimulatorse.g.,cuQuantum26haveattracted
as the FeMo-cofactor of nitrogenase 7 is attractive with care for considerableinterestduetoitspronouncedperformance.27
thesettingofactiveorbitalspace.8Inpractice,however,thedevel- In another direction, the so-called problem decomposition
opment of computational methods and algorithms using quantum approach has been introduced to shallow the circuit depth 28 while
simulators is currently more mainstream than the use of actual avoiding the effects of noise. Note that such an approach is rather
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttributionLicense,whichpermitsuse,distributionandreproductioninanymedium,
providedtheoriginalworkisproperlycited.
©2024TheAuthor(s).JournalofComputationalChemistrypublishedbyWileyPeriodicalsLLC.
2204 wileyonlinelibrary.com/journal/jcc JComputChem.2024;45:2204–2213.

 1096987x, 2024, 26, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438 by Oak Ridge National Laboratory Ut Battelle, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
SUGISAKIETAL. 2205
commonforlargemolecules(likeproteins)asthefragmentation-based The dimer calculation takes into account the delocalization of elec-
methods.29–31 The introduction of problem decomposition to trons between the monomers. From the sum of the HF energies of
al.,32
quantum computation was pioneered by Yamazaki et who themonomerandthedimer,thetwo-bodyFMOenergyofthesystem
compared three methods of fragment molecular orbital (FMO),33 ofinterestisgivenasinEquation(1)
| divide-and-conquer | (DC),34 | and | density matrix embedding | theory |     |     |     |     |
| ------------------ | ------- | --- | ------------------------ | ------ | --- | --- | --- | --- |
|                    |         |     |                          |        |     | X   | X   |     |
(DMET).35 Recently, the FMO calculations with VQE-UCCSD for EFMO¼ E (cid:2)ðN (cid:2)2Þ E : ð1Þ
|     |     |     |     |     |     |     | IJ f | I   |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- |
hydrogen clusters have been reported.36 In addition, the Gagliardi I>J I
| group has | promoted | the quantum | calculations | based on the |     |     |     |     |
| --------- | -------- | ----------- | ------------ | ------------ | --- | --- | --- | --- |
concept of orbital locality,37–39 and also Tsuchimochi et al. have IndicesofIandJspecifytherespectivemonomers,andN isthenum-
f
| proposed | a many-body | expansion | of UCCSD energy.40 | It may be | beroffragments. |     |     |     |
| -------- | ----------- | --------- | ------------------ | --------- | --------------- | --- | --- | --- |
worth emphasizing here that FMO alsodividesthe larger problem Electron correlation calculations, such as second-order
byakindoflocalityassumption. Møller–Plesset perturbation (MP2),44 are performed after the HF
ThepresentattempttocombineFMOandquantumcomputation calculationsforeachmonomerarecompleteandaftertheindivid-
is a touchstone project, and its primary purpose is to investigate ual HF calculations for each dimer are complete. The correlation
whether there are any fundamental problems before application energycorrectionisdoneinanadditivemannerasinEquation(1).
calculations. In the future, it is envisioned that the active site of a The introduction of electron correlations is essential to improve
metal-containing protein (just like FeMoco 7) will be handled by a quantitatively by incorporating dispersion stabilization and
25
UCCSD system calculation (assuming multi-referencing is neces- reducing excess ionicities of the HF description. As described in
sary) to avoid configuration explosion under the approximation of a Reference 44, both size-consistency and orbital-invariance are
multilayerFMO,41whichwillbeanexampleof“realistichybriduse” crucial requirements in the correlated methods. This is obviously
ofordinaryandquantumcomputers. truefortheFMOschemebasedonEquation(1).
Inthisstudy,weappliedtheVQE-UCCSDscheme18–21tocom- Currently, GAMESS-US,45,46 PAICS,47,48 and ABINIT-MP 49,50
33,42,43
pute the electron correlation part of FMO calculations for a are the available programs that can perform FMO calculations
couple of hydrogen-bonded systems, (FH) and (FH) -H O. For the includingelectroncorrelationcorrectionbyMP2.BesidestheMP2
|     |     |     | 3   | 2 2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
capability,51–53
presentexecution,thecuQuantumsimulator26wasusedasdonein ABINIT-MP is unique in supporting higher-order
thepreviousstudy.27EffectofTrotterizationontheorbital-invariance correlated calculations 44,54 on-the-fly; from the third-order MP
conditionoftheUCCSDmethodwasinvestigatedusingtwosymmet- (MP3)55tocoupled-clustersinglesanddoublesincludingperturba-
tivetriples(CCSD(T))56aresupported.
ricallyequivalentFHmoleculesinthelattersystem.Wealsostudied
relationshipbetweenthesize-consistencyconditionandtheTrotter-
izedUCCSDansatz,usingsquaretetrahydrogen(4H)andcuboidocta-
hydrogen(8H)clusters.AccelerationoftheVQE-UCCSDsimulations 2.2 | Preparationofmolecularintegralsunder
| usingcuQuantumisalsodiscussed.Therestofthepaperisorganized |     |     |     |     | FMOscheme |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- |
asfollows:InSection2,wedescribethecalculationmethodsofboth
FMOstageandVQE-UCCSDstages.TheresultsoftheFMOcorrela- The geometries of (FH) (under C symmetry) and (FH) -H O (C
|     |     |     |     |     |     | 3   | s   | 2 2 2v |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
tion energies are shown first, and then the issues surrounding the symmetry)wereoptimizedbytheGAUSSIAN16Wprogram57atthe
TrottererrorarediscussedinSection3.InSection4,wesummarize level of B3LYP 58 corrected with the empirical dispersion 59 with
ourworkanddiscusspossibledirectionsforfuturework. the6-31+G(d',p')basisset.60TheresultingCartesiancoordinatesare
listedinTable1andillustratedinFigure1.
|     |     |     |     |     | For(FH) | and(FH) -H | O,theFMOcalculationswereperformed |     |
| --- | --- | --- | --- | --- | ------- | ---------- | --------------------------------- | --- |
3 2 2
2 | METHOD OF CALCULATION withtheSTO-3Gminimalbasisset,61whereweusedalocalversion
|     |     |     |     |     | of ABINIT-MP, | which dumped | the integral | list of basis functions |
| --- | --- | --- | --- | --- | ------------- | ------------ | ------------ | ----------------------- |
2.1 | FMOschemeandprogram andtheconvergedcanonicalMO(CMO)coefficients(attheFMO-HF
|     |     |     |     |     | level) of monomers | and dimers | as separate | files. These data were |
| --- | --- | --- | --- | --- | ------------------ | ---------- | ----------- | ---------------------- |
Theschemeofthebasictwo-bodyFMOcalculation33,42,43issumma- transformed by a small Fortran program into molecular integrals
rized as follows. The first step is to determine the molecular orbital for the second-quantized Hamiltonian used to run VQE-UCCSD,
| and electron       | density | of each | monomer by the        | Hartree–Fock | expressedas |     |     |     |
| ------------------ | ------- | ------- | --------------------- | ------------ | ----------- | --- | --- | --- |
| (HF) approximation | 44      | under a | given basis function, | while self-  |             |     |     |     |
|                    |         |         |                       |              |             | X   | X   |     |
1
consistently imposing an electrostatic potential (ESP) on each other. H¼ h a†a þ g a†a†aa: ð2Þ
|     |     |     |     |     |     | pq  | p q 2 pqrs p | q s r |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- |
ThesetofESPsofthemonomersistobedetermineduntilthemono- pq pqrs
| mer self-consistent-charge |     | (SCC) | condition is satisfied | by iterations. |     |     |     |     |
| -------------------------- | --- | ----- | ---------------------- | -------------- | --- | --- | --- | --- |
This allows the polarization of each monomer to be taken into Indicesofp,q,randscoverthecorrelatingorbitalspace,andh and
pq
account. In the next step, the monomer-determined ESP is used to g arethetransformedone-andtwo-electronintegrals.The1s-like
pqrs
CMOsoffluorineandoxygenwerefrozen62forh
calculate the HF for the dimer; no SCC condition is imposed. pq inEquation(2),

 1096987x, 2024, 26, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438 by Oak Ridge National Laboratory Ut Battelle, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2206 |     |     |     |     |     |     | SUGISAKIETAL. |     |
| ---- | --- | --- | --- | --- | --- | --- | ------------- | --- |
TABLE 1 OptimizedCartesiancoordinatesinunitsofÅ. FMO-MP2 and FMO-CCSD(T) calculations were also performed by
ABINIT-MP.Thesecalculationswerecompletedinlessthan1sona
| Seq. | Frag. Elem. x | y   | z   |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
singlecoreofIntelXeonprocessor.
(FH)3
| 1   | 1 F 0.779023 | 0.287467 | 0.000000 |     |     |     |     |     |
| --- | ------------ | -------- | -------- | --- | --- | --- | --- | --- |
| 2   | 1 H 0.000000 | 0.807300 | 0.000000 |     |     |     |     |     |
2.3 | Set-upofVQE-UCCSDcalculation
| 3   | 2 F (cid:2)1.361653 | 1.874668 | 0.000000 |     |     |     |     |     |
| --- | ------------------- | -------- | -------- | --- | --- | --- | --- | --- |
4 2 H (cid:2)1.330503 2.801407 0.000000 VQEisaquantum–classicalhybridalgorithmandithasbeenproposed
(cid:2)2.399606
5 3 F 0.648089 0.000000 to solve quantum chemistry problems using NISQ devices.18,19 In
(cid:2)1.471463
6 3 H 0.741364 0.000000 VQE,anapproximatewavefunctionisgeneratedbyusingaparame-
(FH) -H O terizedquantumcircuit(PQC)definedbyan“ansatz”,andtheexpec-
2 2
1 1 O 0.000000 0.000000 1.200039 tation value of the qubit Hamiltonian obtained by applying the
fermion–qubit
2 1 H 0.000000 0.771251 1.779594 transformation to the second-quantized Hamiltonian
giveninEquation(2)iscomputedstatistically,byrepeatedlyexecuting
| 3   | 1 H 0.000000 | (cid:2)0.771251 | 1.779594        |                                                              |     |     |     |     |
| --- | ------------ | --------------- | --------------- | ------------------------------------------------------------ | --- | --- | --- | --- |
|     |              |                 | (cid:2)0.694256 | thequantumcircuitandcollectingthemeasurementresults.Theclas- |     |     |     |     |
| 4   | 2 F 0.000000 | 2.034006        |                 |                                                              |     |     |     |     |
sicalcomputerthenexecuteavariationaloptimizationoftheparame-
| 5   | 2 H 0.000000 | 1.179139 | (cid:2)0.331451 |     |     |     |     |     |
| --- | ------------ | -------- | --------------- | --- | --- | --- | --- | --- |
tersinPQC.Thesestepsareiterateduntilconvergence.
| 6   | 3 F 0.000000 | (cid:2)2.034006 | (cid:2)0.694256 |         |                   |           |                      |     |
| --- | ------------ | --------------- | --------------- | ------- | ----------------- | --------- | -------------------- | --- |
|     |              |                 |                 | Various | types of ansatzes | have been | proposed and studied | for |
| 7   | 3 H 0.000000 | (cid:2)1.179139 | (cid:2)0.331451 |         |                   |           |                      |     |
quantumchemicalcalculations.66Inthiswork,weadoptedtheUCCSD
ansatzdefinedinEquations(3)and(4),becauseitisachemicallymoti-
vatedansatzanditcangiveveryaccuratecorrelationenergies.
|     |     |     |     |     | jΨ     | i¼eT(cid:2)T†jΨ | i:  | ð3Þ |
| --- | --- | --- | --- | --- | ------ | --------------- | --- | --- |
|     |     |     |     |     | UCCSD  |                 | HF  |     |
|     |     |     |     |     | X      | X               |     |     |
|     |     |     |     |     | taa†aþ | 1 taba†a†aa:    |     |     |
|     |     |     |     |     | T¼     | i               | j i | ð4Þ |
i a 2 ij a b
|     |     |     |     |     | ia  | ijab |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
Here,weusedtheindicesiandjfortheoccupiedspinorbitalsanda
|     |     |     |     | andbfortheunoccupiedorbitalsoftheHFwavefunctionjΨ |     |     |     | i.To |
| --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | ---- |
HF
acceleratetheVQEsimulations,weadoptedthefollowingtechniques:
|        |                             |         |             | (1) Using | the symmetry conserving | Bravyi–Kitaev | transformation |     |
| ------ | --------------------------- | ------- | ----------- | --------- | ----------------------- | ------------- | -------------- | --- |
| FIGURE | 1 Molecularstructuresof(FH) | and(FH) | -H O.Forthe |           |                         |               |                |     |
|        |                             | 3       | 2 2         |           |                         |               |                |     |
(SCBKT)67toreducetwoqubitsinthesimulation,(2)usingtheMP3
former,themiddle,upper,andlowerFHmoleculescorrespondto
andtheMP2excitationamplitudesastheinitialguessoftheta
fragments“1”,“2”,and“3”,respectively.Forthelatter,theH 2 O and
i
moleculeisassignedtofragment“1”;twoFHmolecules(fragments tab, respectively,25 and (3) GPU-based numerical simulations. The
ij
| “2”(upper)and“3”(lower))areequivalentduetotheC |     |     | symmetry. |                                                      |     |     |                     |     |
| ---------------------------------------------- | --- | --- | --------- | ---------------------------------------------------- | --- | --- | ------------------- | --- |
|                                                |     |     | 2v        | numberofqubitsfortheVQE-UCCSDsimulationswas8and18for |     |     |                     |     |
|                                                |     |     |           | monomersanddimers,respectively,in(FH)                |     |     | ,and10formonomer“1” |     |
3
|     |     |     |     | and20fordimers“21”and“31”in(FH) |     | -H  | O.TheVQE-UCCSDsim- |     |
| --- | --- | --- | --- | ------------------------------- | --- | --- | ------------------ | --- |
2 2
whichisagoodapproximationtosaveonthenumberofqubits.63,64
|     |     |     |     | ulation program | was developed | by us, | by using Python3 | with |
| --- | --- | --- | --- | --------------- | ------------- | ------ | ---------------- | ---- |
Thenumberofcorrelatedelectronsfordimerswasthus16. OpenFermion,68Cirq,69andcuQuantum26libraries.Itisdesirableto
Note that there is some degree of locality of monomer CMOs uselargerbasissets,suchas6-31G(d),toanalyzetheFMOcorrelation
indimerorbitalswithrespecttotheoccupiedspacefor(FH) andalso energies and Trotter effects on the UCCSD ansatz in more detail.
3
thatthereisthesymmetricdelocalizationfortheFHdimerin(FH) - However,the VQE-UCCSDsimulations for more than 20 qubits are
2
Pipek–Mezey
H 2 O. To address the issue of size-consistency, the quite challenging, because the simulation time grows exponentially
localization65wasperformedforthevalenceoccupiedCMOsandthe withthenumberofqubits.Increasingthevariationalparametersalso
virtual CMOs, respectively, and these sets of localized MOs (LMOs) makestheVQEoptimizationdifficult.Notethatthenumberofvaria-
werealsousedfortheintegraltransformation.Thelistsofmolecular tionalparametersis10(FH;8qubits),34(H O;10qubits),132((FH)
|     |     |     |     |     |     |     | 2   | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
orbitals(CMOsandLMOs)forthemonomersanddimersof(FH) and under C point group; 18 qubits), and 306 (H O-FH; 20 qubits). In
|     |     |     | 3   | s   |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(FH) 2 -H 2 O are shown in Figures S1 and S2, respectively, in Supple- addition, the SCBKT on OpenFermion uses more than 300 GB of
mentaryMaterials. memory for the largest system studied (dimers “21” and “31” of
Due to a proof-of-concept (PoC) phase of this study, the FMO (FH) -H O), and the fermion–qubit transformation becomes another
2 2
calculations(attheHFlevel)byABINIT-MPweredoneinaseparate bottleneckforsimulatinglargersystems.
stepfromthequantumcalculationsdescribedinthenextsubsection. In the implementation of the UCCSD quantum circuit, we
ForcomparisonwiththeVQE-UCCSDcorrelationenergies,theusual adopted the first-order Trotter decomposition given in

 1096987x, 2024, 26, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438 by Oak Ridge National Laboratory Ut Battelle, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| SUGISAKIETAL. |                             |                    |     |     |     |     |     |     |     | 2207 |
| ------------- | --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | ---- |
| TABLE         | 2 Correlationenergiesof(FH) | ainunitsofHartree. |     |     |     |     |     |     |     |      |
3
|      |     |      |         | UCCSD:CB |      |     | UCCSD:PW |     |     |        |
| ---- | --- | ---- | ------- | -------- | ---- | --- | -------- | --- | --- | ------ |
| Unit | MP2 | CCSD | CCSD(T) | CMOb     | LMOc |     | CMO      |     | LMO | CAS-CI |
Monomer
“1” (cid:2)0.017933 (cid:2)0.026945 (cid:2)0.026945 (cid:2)0.026884 (cid:2)0.026854 (cid:2)0.026914 (cid:2)0.026729 (cid:2)0.026945
“2” (cid:2)0.017526 (cid:2)0.026216 (cid:2)0.026216 (cid:2)0.026164 (cid:2)0.026169 (cid:2)0.026192 (cid:2)0.026019 (cid:2)0.026216
“3” (cid:2)0.017933 (cid:2)0.026929 (cid:2)0.026929 (cid:2)0.026899 (cid:2)0.026839 (cid:2)0.026875 (cid:2)0.026691 (cid:2)0.026929
Dimer
“21” (cid:2)0.035493 (cid:2)0.051856 (cid:2)0.051933 (cid:2)0.049880 (cid:2)0.050429 (cid:2)0.050452 (cid:2)0.051322 (cid:2)0.051963
“31” (cid:2)0.035980 (cid:2)0.052778 (cid:2)0.052850 (cid:2)0.051554 (cid:2)0.051632 (cid:2)0.051527 (cid:2)0.052169 (cid:2)0.052879
“32” (cid:2)0.035446 (cid:2)0.053122 (cid:2)0.053123 (cid:2)0.051952 (cid:2)0.051317 (cid:2)0.053067 (cid:2)0.052692 (cid:2)0.053124
(cid:2)0.053527 (cid:2)0.077666 (cid:2)0.077816 (cid:2)0.073439 (cid:2)0.073516 (cid:2)0.075065 (cid:2)0.076744 (cid:2)0.077876
Sum.
| w/oFMOd | (cid:2)0.053497 | (cid:2)0.077566 | (cid:2)0.077730 |     |     |     |     |     |     |     |
| ------- | --------------- | --------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
aTheHFenergies(inunitsofHartree)ofmonomer“1”,“2”,and“3”are(cid:2)103.815720,(cid:2)103.995064,(cid:2)103.563842,respectively.Incontrast,theHF
energiesofdimer“21”,“31”,“32”are(cid:2)228.173251,(cid:2)227.542281,(cid:2)218.792929,respectively.ThesumofEquation(1)is(cid:2)363.133835Hartree.
Equation(1)isalsousedforthesumofcorrelationenergies.
bHFcanonicalorbitalswereusedforthecalculation.
cLocalizedmolecularorbitalsconstructedbyusingPipek–Mezeymethodwereusedforthecalculation.
dThecorrelationenergyofthewholesystemcalculatedwithoutFMOscheme.
Equation(5)inconjunctionwiththemagnitudeordering70ofthe
applyingtheFMOschemearealsolistedforcomparison.Thediffer-
clusteroperators. ence between the correlation energies with and without FMO is a
mol(cid:2)1).
|     |     |       |     |     | maximum | of 0.0001 | Hartree | (0.063 kcal | Compared | to MP2, |
| --- | --- | ----- | --- | --- | ------- | --------- | ------- | ----------- | -------- | ------- |
|     |     |   ! " | #   |     |         |           |         |             |          |         |
(cid:2) (cid:3) XK YK M CCSDhasasignificantlylowerenergy,andCCSD(T)givesvaluesclose
|     | exp T(cid:2)T† ¼exp | it P ≈ | eitkPk =M | ð5Þ |     |     |     |     |     |     |
| --- | ------------------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
k k to CAS-CI, as expected. UCCSD:PW gave lower energies than
k¼1 k¼1
|     |     |     |     |     | UCCSD:CB, | but the | number | of function | evaluations | (total energy |
| --- | --- | --- | --- | --- | --------- | ------- | ------ | ----------- | ----------- | ------------- |
calculations)requiredinPowellisabout1.6–2.8timesgreaterthanin
P
Here, K it P istheexcitation/de-excitationoperatorsinthePauli COBYLA (see Table S1 in Supplementary Materials for details).
|     | k¼1 k k |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
operatorexpressionsobtainedbyadoptingtheSCBKTtotheoperator The same trend was observed for the LMO-based UCCSD calcula-
ðT(cid:2)T†Þinthesecond-quantizedform.P isadirectproductofPauli tions.Nosignificantdifferencewasfoundinthenumberoffunction
k
operatorscalledasa Paulistring,andt k isthecorrespondingcoeffi- evaluationsbetweenCMOandLMO-basedcalculations.
cientderivedfromtaandtab.KisthenumberofPaulistrings,andMis As we discussin the next section, Trotterized UCCSD does not
|     | i ij |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thenumberofTrotterslices.Unlessotherwisespecifiedweusedthe automaticallysatisfythesize-consistencycondition,andusingLMOs
oneTrotterslice(M¼1)fortheVQE-UCCSDsimulations. as the basis is crucial to ensure that Trottterized UCCSD is size-
For the variational optimization of the excitation amplitudes, we consistent.Infact,thecorrelationenergiesofthedimersareimproved
|     | 71  | 72  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
examined COBYLA and Powell algorithms; the corresponding intheLMO-basedUCCSD:PWcalculations,andthesumofthecorre-
labelsareshortlydenotedasUCCSD:CBandUCCSD:PW,respectively lationenergiesis0.001679Hartree(1.0536kcalmol(cid:2)1)lowerinthe
(seeTables2and3).For comparison,thecalculationofthecomplete LMO-based calculations than in the CMO-based one. The deviation
activespaceconfigurationinteraction(CAS-CI)wasperformedtoobtain ofthesumofUCCSD:PWcorrelationenergyfromtheCAS-CIoneis
| theexactcorrelationenergyintheorbitalspaceofSTO-3G.Thenumer- |     |     |     |     | 0.71kcalmol(cid:2)1. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
ical simulations for (FH) 3 and (FH) 2 -H 2 O were carried out on the Table 3 summarizes the results for the (FH) 2 -H 2 O correlation
Supercomputer ‘Flow’ Type-II subsystem at Nagoya University and energies. The number of function evaluations in the VQE-UCCSD
onthein-houseNVIDIADGXH100system,respectively. optimizationisgiveninTableS2inSupplementaryMaterials.Acheck-
pointhereiswhethertheequivalencesymmetries(monomers“2”and
“3”/dimers“21”and“31”)aresatisfied,andtheusualMP2,CCSD,
| 3 | | RESULTS AND | DISCUSSION |     |     |     |     |     |     |     |     |
| --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
CCSD(T),andCAS-CIresultsallsatisfythisrequirement.Thetrendof
|     |     |     |     |     | thecorrelationenergiesbythesemethodsisthesameasin(FH) |     |     |     |     | .On |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
3
3.1 | Energiesandtimings the other hand, the UCCSD results (of both COBYLA and Powell)
|     |     |     |     |     | unfortunately | do not | satisfy | symmetry, | as the difference | is seen to |
| --- | --- | --- | --- | --- | ------------- | ------ | ------- | --------- | ----------------- | ---------- |
The correlation energies for (FH) are summarized in Table 2. The five decimal places for monomers and three decimal places (in the
3
mol(cid:2)1)
MP2, CCSD, and CCSD(T) correlation energies calculated without order of kcal for dimers. From a chemical precision point of

2208 SUGISAKIETAL.
TABLE 3 Correlationenergiesof(FH) -H OainunitsofHartree.
2 2
UCCSD:CB UCCSD:PW
Unit MP2 CCSD CCSD(T) CMOb LMOc CMO LMO CAS-CI
Monomer
“1” (cid:2)0.035370 (cid:2)0.049321 (cid:2)0.049394 (cid:2)0.049242 (cid:2)0.049214 (cid:2)0.049231 (cid:2)0.048915 (cid:2)0.049445
“2” (cid:2)0.017810 (cid:2)0.026705 (cid:2)0.026705 (cid:2)0.026608 (cid:2)0.026648 (cid:2)0.026692 (cid:2)0.026538 (cid:2)0.026705
“3” (cid:2)0.017810 (cid:2)0.026705 (cid:2)0.026705 (cid:2)0.026677 (cid:2)0.026637 (cid:2)0.026659 (cid:2)0.026476 (cid:2)0.026705
Dimer
“21” (cid:2)0.053486 (cid:2)0.075392 (cid:2)0.075526 (cid:2)0.069313 (cid:2)0.071305 (cid:2)0.071421 (cid:2)0.074429 (cid:2)0.075600
“31” (cid:2)0.053486 (cid:2)0.075392 (cid:2)0.075526 (cid:2)0.071847 (cid:2)0.069583 (cid:2)0.072544 (cid:2)0.074367 (cid:2)0.075600
“32” (cid:2)0.035790 (cid:2)0.053549 (cid:2)0.053553 (cid:2)0.053230 (cid:2)0.052161 (cid:2)0.053207 (cid:2)0.052979 (cid:2)0.053549
Sum. (cid:2)0.071770 (cid:2)0.101602 (cid:2)0.101801 (cid:2)0.091863 (cid:2)0.090551 (cid:2)0.094590 (cid:2)0.099846 (cid:2)0.101895
w/oFMOd (cid:2)0.071757 (cid:2)0.101649 (cid:2)0.101847
aTheHFenergiesinunitsofHartreeofmonomer“1”,“2”,and“3”are(cid:2)84.426515,(cid:2)103.695254,and(cid:2)103.695254,respectively(“2”and“3”are
equivalent).Incontrast,theHFenergiesofdimer“21”,“31”,“32”are(cid:2)207.357701,(cid:2)207.357701,and(cid:2)220.935631,respectively(“21”and“31”are
equivalent).ThesumofEquation(1)is(cid:2)343.834010Hartree.Equation(1)isalsousedforthesumofcorrelationenergies.
bHFcanonicalorbitalswereusedforthecalculation.
cLocalizedmolecularorbitalsconstructedbyusingPipek–Mezeymethodwereusedforthecalculation.
dThecorrelationenergyofthewholesystemcalculatedwithoutFMOscheme.
view, it seems problematic that the effect is seen to three decimal GPUacceleration,thetimerequiredforpre-processing(Fermion–qubit
places.Furthermore,thisissueofbrokenequivalenceshouldbekept transformation, reference CAS-CI calculation, MP2 and MP3 calcula-
in mind not only for FMO, but for all approaches of fragmentation- tions, etc.) was 4773.9 s and 100 function evaluations in the VQE
orientedmethods.29–31ThisproblemofVQE-UCCSDisrelatedtothe optimizationtook1211.0s.Incontrast,theCPU-onlycalculationtook
Trottererrorandisdiscussedinthenextsection. 4421.2 and 37363.9 s for pre-processing and 100 function calls,
TheeffectoforbitallocalizationontheUCCSDcorrelationenergy respectively.TheGPUaccelerationoftheVQEiterationpartisabouta
isremarkableinthe(FH) -H Osystem.IntheUCCSD:PWcalculations factorof30.85.Sincethenumbersoffunctionevaluationsrequiredfor
2 2
the sum of correlation energies improved about 0.005256 Hartree convergence in UCCSD:CB and UCCSD:PW were 4913 and 12,452,
(3.2982kcalmol(cid:2)1)bytheorbitallocalization,anddeviationfromthe respectively, the time for the CPU-only simulations are estimated to
CAS-CIcorrelationenergyis1.29kcalmol(cid:2)1.Notethatorbitallocali- beabout21and54daysforUCCSD:CBandUCCSD:PW,respectively.
zation also improves the orbital-invariance condition. By using the GPU acceleration is substantial for larger systems, but the
LMOs,thedifferenceincorrelationenergybetween“21”and“31”is speedup is less significant compared with our previous study.27
reducedto0.039kcalmol(cid:2)1.Theseresultsexemplifytheimportance ThisisbecausetheVQEjobneedsalotoftimeforpre-processing
of using LMOs in the combination of FMO and VQE-UCCSD and post-processing, and these parts cannot be accelerated by
approaches. cuQuantum. Considering that a normal FMO-CCSD(T)/STO-3G
The cuQuantum quantum simulator was used in this VQE-UCCSD calculationtakeslessthan1stocomplete,thereisaspeeddiffer-
computation.Table4summarizesthetimingsoftheUCCSDjobsof(FH) ence of the order of the fourth power of 10 if the correlation
3
usingLMOsonthe‘Flow’Type-IIsubsystemwithandwithoutGPU. part is due to VQE-UCCSD at this time. Note that the present
TheGPUaccelerationwasaboutafactorof1.6–2.2and6.7–7.7for VQE-UCCSDwasrunonaclassicalcomputer,wherecomputational
monomers and dimers, respectively. In monomer “1”, the time for time grows exponentially with the number of qubits. Anyway, as
quantum circuit construction is 0.053 s, and the time for quantum in the previous report,27 GPU acceleration with cuQuantum is
circuitsimulationis0.052and0.192swithandwithoutGPU,respec- essentialforquantumsimulations.Suchanexponentialincreasein
tively, for one VQE iteration. In dimer “21”, the time for quantum computationtimemaynotoccurifarealquantumcomputerisused
circuitconstructionis2.128s,andthetimeforasinglequantumcircuit for the VQE-UCCSD calculations. However, there are other kinds
simulationrunis3.585(withGPU)and40.356(withoutGPU)s,respec- ofdifficultiestoovercomeinthehardwareexecution.Forexample,
tively. The VQE-UCCSD simulations of the dimers “21” and “31” of increase of Hamiltonian terms to evaluate the expectation value,
(FH) -H O(20qubitsystems)withoutGPUaccelerationaretootime- shotnoiseonthecomputedenergy,difficultyofvariationaloptimiza- 2 2
consuming to do. Here we estimated the acceleration ratio by tioninthepresenceofvariousnoises,andsoon.Thecombinationof
performing the UCCSD simulations of the dimer “21” of (FH) -H O varioustechniques(justsuchaslocality-utilizedapproaches32,36–39)
2 2
bysettingthemaximumnumberoffunctionevaluationsintheVQE toreducethecomputationalcostinVQE73–76maybeessentialfor
parameter optimizationto be 100 on NVIDIA DGX H100. With the thehardwareexecutionofVQE-UCCSD.
1096987x,
2024,
26,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438
by
Oak
Ridge
National
Laboratory
Ut
Battelle,
Wiley
Online
Library
on
[06/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 1096987x, 2024, 26, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438 by Oak Ridge National Laboratory Ut Battelle, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| SUGISAKIETAL. |                                   |     |     |     |                            |     |     |     |     | 2209 |
| ------------- | --------------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | ---- |
| TABLE 4       | TimingsofUCCSDjob(insecond)of(FH) |     |     |     | usingLMOswith/withoutaGPU. |     |     |     |     |      |
3
|     | UCCSD:CB |     |     |     |     |     |     | UCCSD:PW |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
Unit WithGPU WithoutGPU Acceleration WithGPU WithoutGPU Acceleration
Monomer
| “1” | 17.2 |     | 27.8 |     |     | 1.62 |     | 27.6 | 48.3 | 1.75 |
| --- | ---- | --- | ---- | --- | --- | ---- | --- | ---- | ---- | ---- |
| “2” | 15.5 |     | 33.6 |     |     | 2.17 |     | 28.5 | 55.4 | 1.94 |
| “3” | 16.2 |     | 26.8 |     |     | 1.65 |     | 26.5 | 49.3 | 1.86 |
Dimer
| “21” | 12767.5 |     | 93205.0 |     |     | 7.30 |     | 34153.3 | 260996.7 | 7.64 |
| ---- | ------- | --- | ------- | --- | --- | ---- | --- | ------- | -------- | ---- |
| “31” | 13947.1 |     | 94199.7 |     |     | 6.75 |     | 34397.3 | 237695.3 | 6.91 |
| “32” | 8805.9  |     | 59975.6 |     |     | 6.81 |     | 21129.0 | 156257.2 | 7.40 |
aAllthecalculationswerecarriedouton‘Flow’Type-IIsubsystem.
3.2 | RelationwithTrottererror
| Itisinterestingtonotethatthemonomers“2”and“3”of(FH) |     |     |     |     |     | -H O |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
2 2
aresymmetricallyequivalent,butVQE-UCCSDyieldsdifferentcorre-
| lation energies. | The HF | canonical | orbitals of | the monomers |     | “2” and |     |     |     |     |
| ---------------- | ------ | --------- | ----------- | ------------ | --- | ------- | --- | --- | --- | --- |
“3”areillustratedinFigure2.Wefoundthattherelativephasefrom
| the second | to the fifth | molecular | orbitals | is different | (or | inverted) |     |     |     |     |
| ---------- | ------------ | --------- | -------- | ------------ | --- | --------- | --- | --- | --- | --- |
betweenmonomers“2”and“3”,whichcauseschangesintheabso-
lutesignofthesomeexcitationamplitudestaandtab.Asaresult,the
|     |     |     |     | i ij |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
quantumstatescorrespondingtotheUCCSDwavefunctionarenot
identicalformonomers“2”and“3”,andtheTrottererrorappearsina
differentway.ThisfactisconfirmedbyperformingtheUCCSDcalcu-
lationswithoutTrotterization,usingtheexpm_multiplyfunctionin
| the SciPy          | library,77 which | allows       | us to compute | the        | action         | of the |            |                                                    |     |     |
| ------------------ | ---------------- | ------------ | ------------- | ---------- | -------------- | ------ | ---------- | -------------------------------------------------- | --- | --- |
| matrix exponential | of ðT(cid:2)T†Þ  | on           | jΨ i. In      | this case, | the calculated |        |            |                                                    |     |     |
|                    |                  |              | HF            |            |                |        | FIGURE     | 2 ActiveorbitalsofFHmolecules(monomers“2”and       |     |     |
| correlation        | energies of      | the monomers | “2”           | and “3”    | are exactly    | the    | “3”)of(FH) |                                                    |     |     |
|                    |                  |              |               |            |                |        |            | 2 -H 2 O.Redarrowsspecifytheelectronoccupancyofthe |     |     |
same:(cid:2)0:026687Hartree.ThefactthatTrotterizedUCCSDcannot
HFwavefunction.
| maintain | orbital-invariance | indicates | that | care must | be  | taken to |     |     |     |     |
| -------- | ------------------ | --------- | ---- | --------- | --- | -------- | --- | --- | --- | --- |
ensurethattherelativephasesofthemolecularorbitalsmatchatall FromTable5,theUCCSDcalculationswithoutTrotterdecomposi-
pointswhencalculatingpotentialenergysurfaces. tionyieldalmostthesameΔEvaluesforbothLMO-andCMO-based
Since the Trotter errors appears in an unexpected way, we further calculations, and the ΔE values of the dimer are twice those of the
investigated about the relationship between Trotter errors and the size- monomer; that is, Trotter-free UCCSD satisfies the size-consistency
consistency,whichisanessentialconditionintheFMOframeworkasmen- condition.SmalldifferencesintheΔEvaluesofthedimerwithCMO
tionedearlier.Herewefocusedonthetetrahydrogen(4H)cluster78ina andLMOareduetoroundingerrorsintheAO!MOtransformation.
squarecoordinatewithR(H–H)=1.0583Å(2.0Bohr)asthemonomer, Incontrast,whentheTrotterdecompositionisusedtoconstructthe
becausetheTrottererrorbecomesmoresignificantwhentheHFisnota UCCSD quantum circuit, the ΔE of the dimer with CMO is signifi-
cantlylargerthanthe2(cid:3)ΔEðMonomerÞ.SincetheΔEvaluefordimer
| good approximation | of the | ground-state | wave | function | and the | UCCSD |     |     |     |     |
| ------------------ | ------ | ------------ | ---- | -------- | ------- | ----- | --- | --- | --- | --- |
wavefunctionhaslargeexcitationamplitudes.Thissystemisalsosuitable withLMOisapproximatelytwicetheΔEofmonomer,weconcluded
becausetheHFCMOsarecompletelydefinedbypoint-groupsymmetry. that the size-consistency condition of the VQE-UCCSD can be
In the dimer (8H) calculations, two 4H clusters were placed to form a maintained when the molecular orbitals localized on each monomer
cuboid, with the inter-monomer distance being 100 Å. Two types of areusedinthecalculations.
molecular orbitals are examined in the dimer calculations: Completely Inthepresentstudy,weusedthefirst-orderTrotterdecomposi-
delocalizedcanonicalorbitalsbyHFinD pointgroupandLMOsonthe tiongiveninEquation(5),withthenumberofTrotterslicesM¼1.To
2h
monomers.InthetotalenergycalculationsusingUCCSD:PW,weused further investigate the relationship between Trotter error and the
cuQuantum-basedquantumcircuitsimulationswithTrotterdecomposi- size-consistency,weruntheUCCSD:PWsimulationswithMchanged
tion and without Trotter decomposition using the expm_multiply from1to5.WealsocarriedouttheUCCSD:PWsimulationswiththe
functioninSciPy.TheresultsaresummarizedinTable5. second-orderTrotterdecompositiongiveninEquation(6).

 1096987x, 2024, 26, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438 by Oak Ridge National Laboratory Ut Battelle, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2210    |                                           |     |     |     |     |     |     | SUGISAKIETAL. |
| ------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- |
| TABLE 5 | DeviationsoftheUCCSD:PWtotalenergyfromthe |     |     |     |     |     |     |               |
CAS-CIvaluefor4Hcluster(monomer)and8Hcluster(dimer).
| Unit           |         | Trotterdecomposition |              | ΔE=kcalmol(cid:2)1 |     |     |     |     |
| -------------- | ------- | -------------------- | ------------ | ------------------ | --- | --- | --- | --- |
| Monomer        |         | No                   |              | 0.8118             |     |     |     |     |
| Dimer(LMO)     |         | No                   |              | 1.6236             |     |     |     |     |
| Dimer(CMO)     |         | No                   |              | 1.6234             |     |     |     |     |
| Monomer        |         | Yes                  |              | 0.8102             |     |     |     |     |
| Dimer(LMO)     |         | Yes                  |              | 1.6207             |     |     |     |     |
| Dimer(CMO)     |         | Yes                  |              | 5.0319             |     |     |     |     |
|                |         |                      | ! "          | #                  |     |     |     |     |
|                |         | XK                   | YK           | Y1                 | M   |     |     |     |
| (cid:2)        | (cid:3) |                      |              |                    |     |     |     |     |
| exp T(cid:2)T† | ¼exp    | it P                 | ≈ eitkPk =2M | eitkPk =2M         | ð6Þ |     |     |     |
k k
|     |     | k¼1 | k¼1 | k¼K |        |                                           |     |     |
| --- | --- | --- | --- | --- | ------ | ----------------------------------------- | --- | --- |
|     |     |     |     |     | FIGURE | 3 TheplotoftheUCCSD:PWenergiesof8Hcluster |     |     |
TheresultsaresummarizedinTableS3intheSupplementaryMate- withdifferentnumberofTrotterslicesMandtheresultof
extrapolation.
rials.ThesimulationsendedwithinonehourwhenGPUisused.The
UCCSD:PWenergiesofmonomer(4Hcluster)anddimer(8Hcluster)
withLMOdonotchangebyusingalargernumberofTrotterslicesor
by adopting the second-order Trotter decomposition. For the dimer our discussions are based on comparing the energies of monomers
calculations with CMO, in contrast, the deviation from the CAS-CI andadimer.Ourresultsdonotcontradictthispreviousstudy.Trot-
energysystematicallydecreaseswithincreasingM.However,evenfor terizationoftheUCCSDansatzcanbreaknotonlyorbital-invariance
M¼5,theUCCSD:PWenergydoesnotconvergetotheTrotter-free
|     |     |     |     |     | and size-consistency | conditions | but also spin symmetry. | The wave |
| --- | --- | --- | --- | --- | -------------------- | ---------- | ----------------------- | -------- |
UCCSD energy calculated by using expm_multiply in SciPy. This functionobtained by using the Trotterized UCCSD is not always an
resultalsoimpliestheimportanceofusingLMOintheFMOscheme eigenfunctionof theS2 operator, andis contaminated by otherspin
inconjunctionwiththeVQE-UCCSD. states. We calculated the hS2i values of the (FH) system and
3
Since size-consistency is pivotal not only for FMO but also for obtained hS2i less than 10(cid:2)6, 5(cid:3)10(cid:2)3, and 10(cid:2)4 for monomers,
general quantum chemical calculations, it is important to provide dimers(CMO),anddimers(LMO),respectively.
methodstoestimatetheTrottererror-freeenergy.Hereweexamined
| the extrapolation | method | to infer | the Trotter | error-free | UCCSD |     |     |     |
| ----------------- | ------ | -------- | ----------- | ---------- | ----- | --- | --- | --- |
energy using the idea of algorithmic error mitigation.79 To do this, 4 | SUMMARY
| we plotted | the UCCSD:PW | energies | as a function | of the inverse | of  |     |     |       |
| ---------- | ------------ | -------- | ------------- | -------------- | --- | --- | --- | ----- |
|            |              |          | 1=M,          |                |     |     |     | 17–21 |
the number of Trotter slices, and fitted with a function We have performed the VQE-UCCSD calculations using the
E¼αð1=MÞβþγ.ItshouldbenotedthatinthecontextofHamiltonian cuQuantumsimulator26inconjunctionwiththeFMOcalculationsfor
simulations,theerrorofthefirst-orderTrotterdecompositionscales the(FH) and (FH) -H O systems.TheSTO-3Gminimalbasisset 61
3 2 2
asOð1=MÞ.80 InVQE,however,differentTrotterizedversionsofthe wasusedandthefrozen-corerestriction62wasimposed.Bycombin-
UCCSDcorrespondtodifferentansatzes,andthustheoptimalvaria- ing with symmetry conserving Bravyi–Kitaev transformation,67 we
tionalparametersaredifferent.Therefore,itisnotnecessarytoscale can simulate the H 2 O-FH dimer with 20 qubits. Both COBYLA and
the Trotter error of UCCSD as Oð1=MÞ. The calculation results are PowellmethodswereusedforVQEoptimization,withthelatterusu-
illustratedinFigure3.TheE(UCCSD:PW)weresuccessfullyfittedby allyprovidingbetterenergiesbutrequiresmorefunctioncalls.When
thefunctionE¼0:005396ð1=MÞ3:6466(cid:2)3:876244,andthedifference the HF CMOs were used for the UCCSD wave function expansion,
between the energies estimated from the extrapolation and the calculated correlation energies were somewhat small in magni-
theTrottererror-freeonecalculatedwithexpm_multiplyisonly35
|     |     |     |     |     | tude, possibly | due to the breakdown | of the size-consistency | condi- |
| --- | --- | --- | --- | --- | -------------- | -------------------- | ----------------------- | ------ |
μHartree.Weexpectthattheextrapolationmethodusedinthiswork tion. By using the LMOs, the UCCSD correlation energies improved
willhelptoobtaintheVQE-UCCSDenergywiththesize-consistency dramatically,andthedifferencesinthecorrelationenergiesbetween
condition. It is noteworthy that the batch of different slices for theCAS-CIandtheUCCSDinconjunctionwiththePowelloptimizer
extrapolation is a potential target for concurrent processing with werecalculatedtobe0.71and1.29kcalmol(cid:2)1 for(FH) and(FH) -
3 2
multiprocessors. H 2 O, respectively. The (FH) 2 -H 2 O system has two symmetrically
It should be noted that the dependence of the Trotter error on equivalentFHmoleculesthatshouldhavethesameenergies,butthe
thelocalityofthemolecularorbitalswasinvestigatedbyBabbushand Trotterized UCCSD does not satisfy symmetry and yields different
coworkers,81 and they reported that the Trotter error is larger for energies. The difference in correlation energies between the dimers
localizedorbitalbasisthanforcanonicalorbitalsandnaturalorbitals. “21”and“31”isontheorderof1kcalmol(cid:2)1 inthecanonicalorbital
basisbutitreducedto0.039kcalmol(cid:2)1
Thereportedstudyfocusedonlyonsinglemolecule(monomer),and inthelocalizedorbitalbasis.

 1096987x, 2024, 26, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438 by Oak Ridge National Laboratory Ut Battelle, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| SUGISAKIETAL.                                                 |     |     |     |     |     |     |     |            |     |     |     |     |     |     | 2211 |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | ---- |
| Size-consistencyoftheTrotterizedUCCSDisalsostudiednumerically |     |     |     |     |     |     |     | REFERENCES |     |     |     |     |     |     |      |
using4Hand8Hmodelclusters.Wefoundthatthesize-consistency [1] A. Aspuru-Guzik, A. D. Dutoi, P. J. Love, M. Head-Gordon, Science
2005,309,1704.
| condition | can be broken | when    | the          | molecular | orbitals  | delocalized | to       |             |            |     |              |              |     |             |     |
| --------- | ------------- | ------- | ------------ | --------- | --------- | ----------- | -------- | ----------- | ---------- | --- | ------------ | ------------ | --- | ----------- | --- |
|           |               |         |              |           |           |             |          | [2] Y. Cao, | J. Romero, |     | J. P. Olson, | M. Degroote, | P.  | D. Johnson, | M.  |
| the dimer | are used      | for the | calculation, | and using | molecular |             | orbitals |             |            |     |              |              |     |             |     |
Kieferová,I.D.Kivlichan,T.Menke,B.Peropadre,N.P.D.Sawaya,S.
localizedtothemonomersisessentialtosatisfythesize-consistency.
Sim,L.Veis,A.Aspuru-Guzik,Chem.Rev.2019,119,10856.
| These findings | on  | the relationship |     | between | size-consistency |     | and |                                                              |     |     |     |     |     |     |     |
| -------------- | --- | ---------------- | --- | ------- | ---------------- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                |     |                  |     |         |                  |     |     | [3] S.McArdle,S.Endo,A.Aspuru-Guzik,S.C.Benjamin,X.Yuan,Rev. |     |     |     |     |     |     |     |
orbital-invariance44,54andtheerrorintheTrotterdecompositionare Mod.Phys.2020,92,015003.
|                |     |          |           |         |          |     |          | [4] B.Bauer,S.Bravyi,M.Motta,G.K.-L.Chan,Chem.Rev.2020,120, |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --------- | ------- | -------- | --- | -------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| very important | not | only for | FMO-based | quantum | chemical |     | calcula- |                                                             |     |     |     |     |     |     |     |
12685.
| tions and | other fragmentation-oriented |     |     | methods | 29–31 | but | also for |                                                         |     |     |     |     |     |     |     |
| --------- | ---------------------------- | --- | --- | ------- | ----- | --- | -------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |                              |     |     |         |       |     |          | [5] M.Motta,J.E.Rice,WIREsComput.Mol.Sci.2022,12,e1580. |     |     |     |     |     |     |     |
VQE-UCCSD in general. From the numerical simulations, we also [6] S.Lee,J.Lee,H.Zhai,Y.Tong,A.M.Dalzell,A.Kumar,P.Helms,J.
demonstrated that the Trotter error-free UCCSD energy can be Gray,Z.-H.Cui,W.Liu,M.Kastoryano,R.Babbush,J.Preskill,D.R.
|           |          |                  |     |              |     |     |       | Reichman, | E.  | T. Campbell, | E. F. | Valeev, L. | Lin, G. | K.-L. Chan, | Nat. |
| --------- | -------- | ---------------- | --- | ------------ | --- | --- | ----- | --------- | --- | ------------ | ----- | ---------- | ------- | ----------- | ---- |
| estimated | by means | of extrapolation |     | by computing |     | the | UCCSD |           |     |              |       |            |         |             |      |
Comm.2023,14,1952.
energieswithdifferentnumbersofTrotterslices.
|     |                  |     |           |       |      |          |      | [7] M.Reiher,N.Wiebe,K.M.Svore,D.Wecker,M.Troyer,PNAS2017, |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --------- | ----- | ---- | -------- | ---- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| The | GPU acceleration |     | was found | to be | 7.30 | and 7.64 | with |                                                            |     |     |     |     |     |     |     |
114,7555.
COBYLA and Powell algorithms, respectively, for the dimer “21” of [8] Z.Li,J.Li,N.S.Dattani,C.J.Umrigar,G.K.-L.Chan,J.Chem.Phys.
(FH) (18 qubit system). For the dimer “21” of (FH) -H O, the esti- 2019,150,024302.
| 3   |     |     |     |     | 2   | 2   |     |                                       |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | [9] R.Yaris,J.Chem.Phys.1964,41,2419. |     |     |     |     |     |     |     |
matedGPUaccelerationratiooftheVQEquantumcircuitsimulation
|     |     |     |     |     |     |     |     | [10] R.Yaris,J.Chem.Phys.1965,42,3019. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
andtheVQEsimulationsofthedimer“21”with
tobeabout30.85, [11] K.Tanaka,H.Terashima,Chem.Phys.Lett.1984,106,558.
COBYLAandPowellwilltakeabout21and54days,respectively.The [12] R. J. Bartlett, S. A. Kucharski, J. Noga, Chem. Phys. Lett. 1989,
155,133.
usefulnessofGPUshasattractedmuchattentioninvariousfieldsof
|     |     |     |     |     |     |     |     | [13] W.Kutzelnigg,Theor.Chim.Acta1991,80,349. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
quantumcomputation,82andquantumchemistryisanexamplewhere
|     |     |     |     |     |     |     |     | [14] A.G.Taube,R.J.Bartlett,Int.J.QuantumChem.2006,106,3393. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
theaccelerationeffectissignificant,83includinginthiscase;evenwith
|     |     |     |     |     |     |     |     | [15] B.Cooper,P.J.Knowles,J.Chem.Phys.2010,133,234102. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
GPUacceleration,itstilltakesordersofmagnitudelongerthanaregu- [16] G. Harsha, T. Shiozaki, G. E. Scuseria, J. Chem. Phys. 2018, 148,
| lar FMO-CCSD(T) |             | calculation.56 | Recently,   | an  | example | of large-scale |       | 044107.        |     |           |                 |       |            |     |         |
| --------------- | ----------- | -------------- | ----------- | --- | ------- | -------------- | ----- | -------------- | --- | --------- | --------------- | ----- | ---------- | --- | ------- |
|                 |             |                |             |     |         |                |       | [17] A. Anand, | P.  | Schleich, | S. Alperin-Lea, | P. W. | K. Jensen, | S.  | Sim, M. |
| quantum         | computation | with           | adamantanes | has | been    | reported       | using |                |     |           |                 |       |            |     |         |
Díaz-Tinoco,J.S.Kottmann,M.Degroote,A.F.Izmaylov,A.Aspuru-
VQE.84 Followingthesetrends,wewillperformlargerFMO-UCCSD
Guzik,Chem.Soc.Rev.2022,51,1659.
computationsonupcomingGPUenvironments. [18] M.-H. Yung, J. Casanova, A. Mezzacapo, J. McClean, L. Lamata, A.
Aspuru-Guzik,E.Solano,Sci.Rep.2014,4,3589.
|     |     |     |     |     |     |     |     | [19] A.Peruzzo,J.McClean,P.Shadbolt,M.-H.Yung,X.-Q.Zhou,P.J. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
ACKNOWLEDGMENTS
Love,A.Aspuru-Guzik,J.L.O'Brien,Nat.Comm.2014,5,4213.
| All VQE-UCCSD | computations |     | with | cuQuantum | on the | ‘Flow’ | Type-II |                 |     |          |                |     |         |       |          |
| ------------- | ------------ | --- | ---- | --------- | ------ | ------ | ------- | --------------- | --- | -------- | -------------- | --- | ------- | ----- | -------- |
|               |              |     |      |           |        |        |         | [20] J. Romero, | R.  | Babbush, | J. R. McClean, | C.  | Hempel, | P. J. | Love, A. |
subsystemattheInformationTechnologyCenterofNagoyaUniversity
Aspuru-Guzik,QuantumSci.Technol.2018,4,014008.
were performed under the JHPCN Joint Research Projects (jh230001 [21] S.Guo,J.Sun,H.Qian,M.Gong,Y.Zhang,F.Chen,Y.Ye,Y.Wu,S.
|     |     |     |     |     |     |     |     | Cao, | K. Liu, C. | Zha, | C. Ying, Q. | Zhu, H.-L. | Huang, Y. | Zhao, | S. Li, S. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ---- | ----------- | ---------- | --------- | ----- | --------- |
subjectbyYM).KSandYMwouldliketothankYuichiroMinato(CEOof
Wang,J.Yu,D.Fan,D.Wu,H.Su,H.Deng,H.Rong,Y.Li,K.Zhang,
| blueqat Inc.), | Profs. | Takahiro | Katagiri | (Nagoya | University) | and | Satoshi |     |     |     |     |     |     |     |     |
| -------------- | ------ | -------- | -------- | ------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
T.-H.Chung,F.Liang,J.Lin,Y.Xu,L.Sun,C.Guo,N.Li,Y.-H.Huo,
Ohshima(KyushuUniversity)fortheirencouragementregardingquantum C.-Z.Peng,C.-Y.Lu,X.Yuan,X.Zhu,J.-W.Pan,Experimentalquan-
simulationswithcuQuantum.YMwasalsosupportedbyRikkyoSFR.KS tumcomputationalchemistrywithoptimisedunitarycoupledcluster
ansatz.arXiv:2212.08006v22022.
acknowledgesthesupportfromQuantumLeapFlagshipProgram(Grant
|                      |     |      |       |               |     |             |     | [22] J.Lee,W.J.Huggins,M.Head-Gordon,K.B.Whaley,J.Chem.Theory |     |     |     |     |     |     |     |
| -------------------- | --- | ---- | ----- | ------------- | --- | ----------- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| no. JPMXS0120319794) |     | from | MEXT, | Japan, Center | of  | Innovations | for |                                                               |     |     |     |     |     |     |     |
Comput.2019,15,311.
SustainableQuantumAI(JPMJPF2221)fromJST,Japan,andKAKENHI
|     |     |     |     |     |     |     |     | [23] N. H. | Stair, | R. Huang, | F. A. Evangelista, |     | J. Chem. | Theory | Comput. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --------- | ------------------ | --- | -------- | ------ | ------- |
TransformativeResearchAreaB(23H03819)andScientificResearchC 2020,16,2236.
(21K03407)fromJSPS,Japan. [24] G.Greene-Diniz,D.MuñozRamo,Int.J.QuantumChem.2021,121,
e26352.
|                             |     |     |     |     |     |     |     | [25] K.Sugisaki,T.Kato,Y.Minato,K.Okuwaki,Y.Mochizuki,Phys.Chem. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| CONFLICTOFINTERESTSTATEMENT |     |     |     |     |     |     |     | Chem.Phys.2022,24,8439.                                          |     |     |     |     |     |     |     |
Therearenoconflictstodeclare. [26] H.Bayraktar,A.Charara,D.Clark,S.Cohen,T.Costa,Y.-L.L.Fang,Y.
|     |     |     |     |     |     |     |     | Gao, | J. Guan, | J. Gunnels, | A. Haidar, | A. Hehn, | M.  | Hohnerbach, | M.  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ----------- | ---------- | -------- | --- | ----------- | --- |
DATAAVAILABILITYSTATEMENT Jones, T. Lubowe, D. Lyakh, S. Morino, P. Springer, S. Stanwyck, I.
Terentyev,S.Varadhan,J.Wong,T.Yamaguchi,cuQuantumSDK:A
Thedatathatsupportthefindingsofthisstudyareavailablefromthe
|                                           |     |     |     |     |     |     |     | high-performance  |     | library       | for accelerating |          | quantum      | science.      | arXiv: |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------- | ---------------- | -------- | ------------ | ------------- | ------ |
| correspondingauthoruponreasonablerequest. |     |     |     |     |     |     |     | 2308.01999v12023. |     |               |                  |          |              |               |        |
|                                           |     |     |     |     |     |     |     | [27] K. Sugisaki, | V.  | S. Prasannaa, | S.               | Ohshima, | T. Katagiri, | Y. Mochizuki, |        |
B.K.Sahoo,B.P.Das,Electron.Struct.2023,5,035006.
ORCID
|               |                                       |     |     |     |     |     |     | [28] K.Dalton,C.K.Long,Y.S.Yordanov,C.G.Smith,C.H.W.Barnes,N. |     |     |     |     |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| KenjiSugisaki | https://orcid.org/0000-0002-1950-5725 |     |     |     |     |     |     |                                                               |     |     |     |     |     |     |     |
Mertig,D.R.M.Arvidsson-Shukur,NpjQuantumInfo.2024,10,18.
TatsuyaNakano https://orcid.org/0000-0001-9928-5269 [29] M.S.Gordon,D.G.Fedorov,S.R.Pruitt,L.V.Slipchenko,Chem.Rev.
2012,112,632.
| YujiMochizuki | https://orcid.org/0000-0002-7310-5183 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

2212 SUGISAKIETAL.
[30] M.A.Collins,R.P.A.Bettens,Chem.Rev.2015,115,5607. [57] M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A.
[31] K.Raghavachari,A.Saha,Chem.Rev.2015,115,5643. Robb,J.R.Cheeseman,G.Scalmani,V.Barone,G.A.Petersson,H.
[32] T. Yamazaki, S. Matsuura, A. Narimani, A. Saidmuradov, A. Nakatsuji, X. Li, M. Caricato, A. V. Marenich, J. Bloino, B. G.
Zaribafiyan,Towardsthepracticalapplicationofnear-termquantum Janesko, R. Gomperts, B. Mennucci, H. P. Hratchian, J. V. Ortiz,
computersinquantumchemistrysimulations:Aproblemdecomposi- A. F. Izmaylov, J. L. Sonnenberg, D. Williams-Young, F. Ding, F.
tionapproach.arXiv:1806.01305v12018. Lipparini,F.Egidi,J.Goings,B.Peng,A.Petrone,T.Henderson,D.
[33] K. Kitaura, E. Ikeo, T. Asada, T. Nakano, M. Uebayasi, Chem. Phys. Ranasinghe,V.G.Zakrzewski,J.Gao,N.Rega,G.Zheng,W.Liang,
Lett.1999,313,701. M.Hada,M.Ehara,K.Toyota,R.Fukuda,J.Hasegawa,M.Ishida,
[34] T.Akama,M.Kobayashi,H.Nakai,J.Comput.Chem.2007,28,2003. T.Nakajima,Y.Honda,O.Kitao,H.Nakai,T.Vreven,K.Throssell,
[35] G.Knizia,G.K.-L.Chan,Phys.Rev.Lett.2012,109,186404. J.A.MontgomeryJr.,J.E.Peralta,F.Ogliaro,M.J.Bearpark,J.J.
[36] H. Lim, D. H. Kang, J. Kim, A. Pellow-Jarman, S. McFarthing, R. Heyd,E.N.Brothers,K.N.Kudin,V.N.Staroverov,T.A.Keith,R.
Pellow-Jarman, H.-N. Jeon, B. Oh,J.-K. K.Rhee, K.T.No, Sci. Rep. Kobayashi, J. Normand, K. Raghavachari, A. P. Rendell, J. C.
2024,14,2422. Burant,S.S.Iyengar,J.Tomasi,M.Cossi,J.M.Millam,M.Klene,
[37] M. Otten, M. R. Hermes, R. Pandharkar, Y. Alexeev, S. K. Gray, L. C.Adamo,R.Cammi,J.W.Ochterski,R.L.Martin,K.Morokuma,
Gagliardi,J.Chem.TheoryComput.2022,18,7205. O. Farkas, J. B. Foresman, D. J. Fox, Gaussian 16, Revision B.01,
[38] R.D'Cunha,M.Otten,M.R.Hermes,L.Gagliardi,S.K.Gray,J.Chem. GaussianInc,WallingfordCT2016.
TheoryComput.2024,20,3121. [58] A.D.Becke,J.Chem.Phys.1993,98,1372.
[39] A.Mitra,R.D'Cunha,Q.Wang,M.R.Hermes,Y.Alexeev,S.K.Gray, [59] S.Grimme,J.Antony,S.Ehrlich,H.Krieg,J.Chem.Phys.2010,132,
M.Otten,L.Gagliardi,Thelocalizedactivespacemethodwithunitary 154104.
selectivecoupledcluster.arXiv:2404.12927v12024. [60] G.A.Petersson,M.A.Al-Laham,J.Chem.Phys.1991,94,6081.
[40] E.Xu,Y.Shimomoto,S.L.Ten-no,T.Tsuchimochi,J.Phys.Chem.A [61] W.J.Hehre,R.F.Stewart,J.A.Pople,J.Chem.Phys.1969,51,2657.
2024,128,2507. [62] R.P.Hosteny,T.H.DunningJr.,R.R.Gilman,A.Pipano,I.Shavitt,
[41] D.G.Fedorov,K.Kitaura,J.Chem.Phys.2005,122,054108. J.Chem.Phys.1975,62,4764.
[42] D.Fedorov,K.KitauraEds.,TheFragmentMolecularOrbitalMethod: [63] A.J.McCaskey,Z.P.Parks,J.Jakowski,S. V.Moore, T.D. Morris,
Practical Applications to Large Molecular Systems, CRC Press, T.S.Humble,R.C.Pooser,NpjQuantumInfo.2019,5,99.
Florida2009. [64] Y. Mochizuki, K. Okuwaki, T. Kato, Y. Minato, Reduction of orbital
[43] Y. Mochizuki, S. Tanaka, K. Fukuzawa Eds., Recent Advances of space for molecular orbital calculations with quantum computation
the Fragment Molecular Orbital Method - Enhanced Performance and simulatorforeducations.ChemRxiv.9863810.v12019.
Applicability,Springer,Berlin2021. [65] J.Pipek,P.G.Mezey,J.Chem.Phys.1989,90,4916.
[44] A.Szabo,N.S.Ostlund,ModernQuantumChemistry:Introductionto [66] J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L.
AdvancedElectronicStructureTheory,MacmillanPublishing,NewYork Wossnig, I. Rungger, G. H. Booth, J. Tennyson, Phys. Rep. 2022,
1982. 986,1.
[45] D.G.Fedorov,WIREsComput.Mol.Sci.2017,7,e1322. [67] S. Bravyi, J. M. Gambetta, A. Mezzacapo, K. Temme, Tapering off
[46] D.G.Fedorov,inRecentAdvancesoftheFragmentMolecularOrbital qubits to simulate fermionic Hamiltonians. arXiv:1701.08213v1
Method:EnhancedPerformanceandApplicability(Eds:Y.Mochizuki,S. 2017.
Tanaka,K.Fukuzawa),Springer,Berlin2021,p.31. [68] J. R. McClean, N. C. Rubin, K. J. Sung, I. D. Kivlichan, X. Bonet-
[47] T. Ishikawa, T. Ishikura, K. Kuwata, J. Comput. Chem. 2009, Monroig, Y. Cao, C. Dai, E. S. Fried, C. Gidney, B. Gimby, P.
30,2594. Gokhale,T.Häner,T.Hardikar,V.Havlícˇek,O.Higgott,C.Huang,
[48] T. Ishikawa, in Recent Advances of the Fragment Molecular Orbital J.Izaac,Z.Jiang,X.Liu,S.McArdle,J.Romero,N.P.D.Sawaya,B.
Method:EnhancedPerformanceandApplicability(Eds:Y.Mochizuki,S. Senjean, K. Setia, S.Sim, D. S. Steiger, M.Steudtner, Q.Sun, W.
Tanaka,K.Fukuzawa),Springer,Berlin2021,p.69. Sun,D.Wang,F.Zhang,R.Babbush,QuantumSci.Technol.2020,
[49] S.Tanaka,Y.Mochizuki,Y.Komeiji,Y.Okiyama,K.Fukuzawa,Phys. 5,034014.
Chem.Chem.Phys.2014,16,10310. [69] Cirq developers, Cirq (v1.2.0). Zenodo. https://doi.org/10.5281/
[50] Y.Mochizuki,T.Nakano,K.Sakakura,Y.Okiyama,H.Watanabe,K. zenodo.8161252
Kato,Y.Akinaga,S.Sato,J.Yamamoto,K.Yamashita,T.Murase,T. [70] A.Tranter,P.J.Love,F.Mintert,P.V.Coveney,J.Chem.TheoryCom-
Ishikawa,Y.Komeiji,Y.Kato,N.Watanabe,T.Tsukamoto,H.Mori,K. put.2018,14,5617.
Okuwaki, S. Tanaka, A. Kato, C. Watanabe, K. Fukuzawa, in Recent [71] M. J. D. Powell, in Advances in Optimization and Numerical Analysis
AdvancesoftheFragmentMolecularOrbitalMethod:EnhancedPerfor- (Eds:S.Gomez,J.-P.Hennart),Springer,Dordrecht1994,p.51.
manceandApplicability(Eds:Y.Mochizuki,S.Tanaka,K.Fukuzawa), [72] M.J.D.Powell,Comp.J.1964,7,155.
Springer,Berlin2021,p.53. [73] H.R.Grimsley,S.E.Economou,E.Barnes,N.J.Mayhall,Nat.Comm.
[51] Y. Mochizuki, T. Nakano, S. Koikegami, S. Tanimori, Y. Abe, 2019,10,3007.
U.Nagashima,K.Kitaura,Theor.Chem.Acc.2004,112,442. [74] Y. Fun,C.Cao,X.Xu,Z. Li, D. Lv,M.-H.Yung,J. Phys. Chem.Lett.
[52] Y. Mochizuki, S. Koikegami, T. Nakano, S. Amari, K. Kitaura, Chem. 2023,14,9596.
Phys.Lett.2004,396,473. [75] P. Gokhale, O. Angiuli, Y. Ding, K. Gui, T. Tomesh, M. Suchara, M.
[53] Y. Mochizuki, K. Yamashita, T. Murase, T. Nakano, K. Fukuzawa, Martonosi,F.T.Chong,IEEETrans.QuantumEng2020,1,1.
K.Takematsu,H.Watanabe,S.Tanaka,Chem.Phys.Lett.2008,457,396. [76] C.Cao,H.Yano,Y.O.Nakagawa,Phys.Rev.Res.2024,6,013205.
[54] I.Shavitt,R.J.Bartlett,Many-BodyMethodsinChemistryandPhysics: [77] P.Virtanen,R.Gommers,T.E.Oliphant,M.Haberland,T.Reddy,D.
MBPT and Coupled-Cluster Theory, Cambridge University Press, Cournapeau,E.Burovski,P.Peterson,W.Weckesser,J.Bright,S.J.
Cambridge2009. vanderWalt,M.Brett,J.Wilson,K.J.Millman,N.Mayorov,A.R.J.
[55] Y. Mochizuki, K. Yamashita, K. Fukuzawa, K. Takematsu, H. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, Í. Polat, Y. Feng,
Watanabe,N.Taguchi,Y.Okiyama,M.Tsuboi,T.Nakano,S.Tanaka, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I.
Chem.Phys.Lett.2010,493,346. Henriksen,E.A.Quintero,C.R.Harris,A.M.Archibald,A.H.Ribeiro,
[56] Y.Mochizuki,K.Yamashita,T.Nakano,Y.Okiyama,K.Fukuzawa,N. F.Pedregosa,P.vanMulbregt,SciPy1.0Contributors,Nat.Methods
Taguchi,S.Tanaka,Theor.Chem.Acc.2011,130,515. 2020,17,261.
1096987x,
2024,
26,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438
by
Oak
Ridge
National
Laboratory
Ut
Battelle,
Wiley
Online
Library
on
[06/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SUGISAKIETAL. 2213
[78] J.Paldus,P.Piecuch,L.Pylypow,B.Jeziorski,Phys.Rev.A1993,47, [84] V. K. Prasad, F. Cheng, U. Fekl, H.-A. Jacobsen, Phys. Chem. Chem.
2738. Phys.2024,26,4071.
[79] S. Endo, Q. Zhao, Y. Li, S. Benjamin, X. Yuan, Phys. Rev. A 2019,
99,012334.
[80] M.A.Nielsen,I.L.Chuang,QuantumComputationandQuantumInfor- SUPPORTINGINFORMATION
mation,10thAnniversaryed.,CambridgeUniversityPress,Cambridge AdditionalsupportinginformationcanbefoundonlineintheSupport-
2010.
ingInformationsectionattheendofthisarticle.
[81] R.Babbush,J.McClean,D.Wecker,A.Aspuru-Guzik,N.Wiebe,Phys.
Rev.A2015,91,022311.
[82] M.Möller,C.Vuik,EthicsInfo.Technol.2017,19,253.
Howtocitethisarticle:K.Sugisaki,T.Nakano,Y.Mochizuki,
[83] Y. Ino, M. Yonekawa, H. Yuzawa, Y. Minato, K. Sugisaki, Quantum
phase estimations of benzene and its derivatives on GPGPU J.Comput.Chem.2024,45(26),2204.https://doi.org/10.
quantumsimulators.arXiv:2312.16375v12023. 1002/jcc.27438
1096987x,
2024,
26,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/jcc.27438
by
Oak
Ridge
National
Laboratory
Ut
Battelle,
Wiley
Online
Library
on
[06/05/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License