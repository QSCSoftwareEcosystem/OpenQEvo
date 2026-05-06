0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

ViewOnlineExportCitationRESEARCH ARTICLE| SEPTEMBER 13 2024Does the full configuration interaction method based onquantum phase estimation with Trotter decompositionsatisfy the size consistency condition?Kenji Sugisaki AIP Advances 14, 095021 (2024)https://doi.org/10.1063/5.0223661 CHORUSArticles You May Be Interested InQuantum simulation of many-body dynamics with noise-robust Trotter decomposition based on symmetricstructuresAVS Quantum Sci. (February 2026)Simulating spin biology using a digital quantum computer: Prospects on a near-term quantum hardwareemulatorHigh‐order correction to the Trotter expansion for use in computer simulationJ. Chem. Phys. (May 1987)

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

Does the full configuration interaction method
based on quantum phase estimation with Trotter
decomposition satisfy the size consistency
condition?

Cite as: AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661
Submitted: 27 July 2024 • Accepted: 21 August 2024 •
Published Online: 13 September 2024

Kenji Sugisakia)

AFFILIATIONS

Graduate School of Science and Technology, Keio University, 7-1 Shinkawasaki, Saiwai-ku, Kawasaki, Kanagawa 212-0032, Japan;
Quantum Computing Center, Keio University, 3-14-1 Hiyoshi, Kohoku-ku, Yokohama, Kanagawa 223-8522, Japan; and Centre for
Quantum Engineering, Research and Education, TCG Centres for Research and Education in Science and Technology, Sector V,
Salt Lake, Kolkata 700091, India

a)Author to whom correspondence should be addressed: ksugisaki@keio.jp

ABSTRACT

Electronic structure calculations of atoms and molecules are considered to be a promising application for quantum computers. Two key algo-
rithms, the quantum phase estimation (QPE) and the variational quantum eigensolver (VQE), have been extensively studied. The condition
that the energy of a dimer consisting of two monomers separated by a large distance should be equal to twice the energy of a monomer, known
as size consistency, is essential in quantum chemical calculations. Recently, we reported that the size consistency condition can be violated
by Trotterization in the unitary coupled cluster singles and doubles ansatz in the VQE when employing molecular orbitals delocalized to the
dimer [Sugisaki et al., J. Comput. Chem. 45, 2204 (2024)]. It is well known that the full configuration interaction (full-CI) energy is invariant
to arbitrary rotations of molecular orbitals, and therefore, the QPE-based full-CI should theoretically satisfy the size consistency. However,
Trotterization of the time evolution operator can break the size consistency conditions. In this work, we investigated whether size consis-
tency can be maintained with Trotterization of the time evolution operator in QPE-based full-CI calculations. Our numerical simulations
revealed that size consistency in the QPE-based full-CI is not automatically violated by using molecular orbitals delocalized to the dimer, but
employing an appropriate Trotter decomposition condition is crucial to maintain size consistency. We also report on the acceleration of QPE
simulations through the sequential addition of ancillary qubits.

© 2024 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license
(https://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/5.0223661

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

I. INTRODUCTION

Solving the Schrödinger equation for atoms and molecules as
accurately as possible is a fundamental goal of quantum chem-
istry. The full configuration interaction (full-CI) method provides
the best variational wave functions and energies within the Hilbert
space spanned by the chosen basis set. However, the computational
cost of the full-CI method grows exponentially with the num-
ber of basis functions and electrons, making it impractical except
for small molecules with simple basis sets. The method of solv-
ing the full-CI on a quantum computer using the quantum phase
estimation (QPE) algorithm was proposed in 2005.1 Since then,

a number of theoretical studies on QPE-based quantum chemi-
cal calculations2–13 and extensions of the QPE algorithm14–18 have
been reported. Experimentally, iterative QPE-based full-CI/STO-3G
of the H2 molecule, where STO-3G approximates each Slater-type
orbital by three Gaussian functions, were reported in 2010 with
photonic19 and nuclear magnetic resonance (NMR)20 quantum pro-
cessors, using one qubit for wave function encoding. The same
system was investigated with two qubits for wave function stor-
age with superconducting qubits in 201621 and using an ion-trap
quantum processor in conjunction with a Bayesian QPE framework
with quantum error detection.22 The experimental demonstration
of the full-CI/STO-3G of the HeH+ molecule was also reported

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-1

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

using the nitrogen-vacancy (NV) center of the diamond system.23
Recently, statistical QPE with up to a six-qubit Hamiltonian on a
superconducting quantum processor was reported.24

In 2014, the quantum–classical hybrid approach known as a
variational quantum eigensolver (VQE) was proposed for quan-
tum chemical calculations using noisy intermediate-scale quantum
devices.25,26 In the VQE, an approximate wave function is gener-
ated on a quantum computer using a parameterized quantum circuit
defined by an “ansatz,” and the energy expectation value is computed
by statistically sampling the measurement results of the quantum
circuit. The unitary coupled cluster (UCC) ansatz27 is often used as
a physically motivated ansatz and is defined as

∣ΨUCC⟩ = e

(T−T

†)∣ΨHF⟩,

(1)

where ∣ΨHF⟩ is the Hartree–Fock (HF) wave function, and T and T
are the excitation and de-excitation operators, respectively, applied
to the HF wave function. The UCC ansatz, when considering sin-
gle and double excitation operators as T, is known as the unitary
coupled cluster singles and doubles (UCCSD) ansatz and typically
provides accurate correlation energies for closed shell molecules.

†

In quantum chemical calculations, the energy of a dimer con-
sisting of two monomers separated by a large distance should be
twice the energy of a monomer. This condition, known as size con-
sistency,28 is crucial, especially in the calculation of large molecules.
Truncated configuration interaction expansions, such as configu-
ration interaction singles and doubles (CISD) and configuration
interaction singles, doubles, and triples (CISDT), do not satisfy the
size consistency, while truncated coupled cluster methods such as
coupled cluster singles and doubles (CCSD) and coupled cluster sin-
gles, doubles, and triples (CCSDT) do. The UCCSD ansatz, used in
the VQE framework, is based on the cluster expansion, and it is
generally assumed to be size consistent. However, in the VQE, the
UCCSD ansatz is usually implemented using the Trotter decompo-
sition to construct the parameterized quantum circuit. Recently, we
have numerically demonstrated that the Trotterized UCCSD ansatz
does not automatically satisfy the size consistency condition.29 Size
consistency of the UCCSD ansatz can be maintained when molecu-
lar orbitals localized to each monomer are used, but it can be broken
when molecular orbitals delocalized over the dimer are employed in
the UCCSD ansatz.

Since the QPE-based full-CI is often implemented using the
Trotter decomposition of the time evolution operator, it is important
to verify whether the QPE-based full-CI with Trotter decomposi-
tion automatically satisfies the size consistency condition. While it
is known that full-CI energy is invariant with respect to the choice
of reference molecular orbitals, it is unclear how the robustness of
QPE-based full-CI energy is affected by Trotter errors based on the
choice of molecular orbitals. It is important to note that Trotter
decomposition impacts size consistency differently in the VQE-
UCCSD and QPE. In the VQE-UCCSD, the total energy is calculated
as the expectation value of the Hamiltonian, and the contamina-
tion of the wave function from other electronic states due to Trotter
decomposition affects size consistency. In contrast, the QPE cal-
culates the total energy based on the phase shift induced by time
evolution. In this case, changes in the amount of phase shift due to
Trotter error can lead to a breakdown in size consistency.

In this work, we performed numerical quantum circuit simula-
tions of the QPE-based full-CI using both localized and delocalized
molecular orbitals with various Trotter decomposition conditions,
focusing on the size consistency condition. The paper is organized as
follows: Sec. II introduces the QPE-based full-CI method. Section III
describes the target molecular systems in this work and outlines
the numerical simulation conditions. We also discuss accelerating
the numerical simulation of the QPE quantum circuit based on
the sequential addition of ancillary qubits. Section IV presents the
results of the numerical simulations. A summary of this work is
given in Sec. V.

II. THEORY

The QPE is a quantum algorithm designed to find the eigen-
values and corresponding eigenvectors of a unitary matrix U in
polynomial time.30,31 In quantum chemical calculations, the QPE is
performed using the time evolution operator as the unitary operator,

U = e

−iHt.

(2)

The Born–Oppenheimer approximation32 is usually adopted, and
the electronic Hamiltonian H is used. In the second quantized
formula, the electronic Hamiltonian H is expressed as

H = ∑
pq

hpqa

†
paq +

1
2

∑
pqrs

gpqrsa

†
pa

†
qasar.

(3)

Here, hpq and gpqrs are the one- and two-electron integrals, respec-
tively, and the indices p, q, r, and s run over spin orbitals in the active
space.

The textbook implementation of the quantum circuit for the
QPE33 is shown in Fig. 1. This quantum circuit contains L qubits
for wave function storage and N ancillary qubits for eigenphase
readout. The QPE-based full-CI consists of five steps: (1) prepara-
tion of the approximate wave function of the target electronic state
using a Prep circuit, (2) generation of quantum superposition states
using Hadamard (H) gates, (3) controlled-time evolution operation,
(4) inverse quantum Fourier transform, and (5) measurement of
ancillary qubits. The bit string obtained from the measurement in
step (5) corresponds to the fractional binary representation of the
eigenphase ϕ = 0. x1x2 ⋅ ⋅ ⋅ xN as

−iHt∣Ψ⟩ = e

−iEt∣Ψ⟩ = ei2πϕ∣Ψ⟩,

e

(4)

which corresponds to one of the eigenstates. The probability of
obtaining a particular eigenvalue is proportional to the overlap
between the input and full-CI wave functions.

In the quantum circuit implementation, the second quantized
Hamiltonian in Eq. (3) is transformed into a qubit Hamiltonian Hq,

Hq =

J
∑
j=1

wjPj,

(5)

using the fermion–qubit transformation techniques such as the
Jordan–Wigner transformation (JWT)34 and the Bravyi–Kitaev
transformation (BKT).35 Here, Pj represents a tensor product of
Pauli operators, known as Pauli strings, J is the number of Pauli
strings, and wj is the coefficient computed from hpq and gpqrs. The

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-2

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

FIG. 1. The quantum circuit of the textbook implementation of QPE. x1, x2, . . . , xN
represent the measurement outcomes of ancillary qubits.

time evolution operator in Eq. (2) is then implemented using the
Trotter decomposition. The first-order and second-order Trotter
decompositions are given by

−iHqt = [ΠJ

j=1e

e

−iwj Pj t/M]

M

and

−iHqt = [(ΠJ

j=1e

e

−iwj Pj t/2M)(Π1

j=Je

−iwj Pj t/2M)]

M

,

(6)

(7)

respectively. Here, M is the number of Trotter slices. Besides the
Trotter decomposition-based implementation, approaches based on
the truncated Taylor series36,37 and qubitization38 have also been
proposed. The technique based on qubitization shows better com-
putational cost scaling than Trotterization, but it requires addi-
tional ancillary qubits.39 In this work, we focus on the Trotter
decomposition-based approach.

It is well known that the full-CI energy is invariant under arbi-
trary unitary rotations of the molecular orbitals. For convenience,
we focus on the HF canonical molecular orbitals (CMOs) and the
localized molecular orbitals (LMOs) as the two reference orbitals.
By defining a unitary matrix V that transforms the two different
orbitals, the Hamiltonian matrices in the LMO and CMO bases are
written as

HLMO = V

†

HCMOV.

Similarly, the time evolution operators can be expressed as

ULMO = V

†

UCMOV.

(8)

(9)

However, in the full-CI calculations using the QPE with Trotter
decomposition, the Trotterized time evolution operator UTrotter does
not necessarily satisfy the equality in Eq. (9),

UTrotter

LMO ≠ V

†

UTrotter

CMO V,

(10)

because the order of the Pauli strings in the Trotterized time evolu-
tion operator can depend on the molecular orbitals. We expect that
the Pauli strings must be ordered appropriately so that the Trotter
error affects both the monomer and the dimer in the same way to
satisfy the size consistency condition.

III. COMPUTATIONAL CONDITIONS

In this work, we mainly focus on a tetrahydrogen (4H) clus-
ter in a square geometry with R(H–H) = 1.0583 Å (2.0 bohrs)
as the monomer, which is well known as a strongly correlated

system.40 The octahydrogen (8H) cluster, representing the dimer, is
constructed by placing two 4H clusters to form a cuboid, with an
intermonomer distance of 100 Å. This system is also used in our
previous work.29 We employed the STO-3G basis set, and the active
space includes all the molecular orbitals. The size of the active space
is (4e, 4o) and (8e, 8o) for 4H and 8H clusters, respectively. Here,
(ke, lo) indicates that the active space contains k electrons and l
molecular orbitals.

In the present study, we used two different sets of molecular
orbitals for the dimer calculations: the CMOs, delocalized to the
dimer under the D2h point group, and the LMOs under the C2v
point group. Schematic illustrations of the CMO and LMO of 4H
and 8H clusters are given in Fig. 2. These molecular orbitals are gen-
erated using the General Atomic and Molecular Electronic Structure
System (GAMESS-US) software.41

Conventional fermion–qubit transformations such as JWT and
BKT require 2l qubits to encode the wave function. In this work,
we used the symmetry-conserving Bravyi–Kitaev transformation
(SCBKT),42 which reduces the qubit count by two by specifying the
number of spin-α and spin-β electrons. Thus, the number of qubits
for wave function encoding (L in Fig. 1) is 6 and 14 for 4H and 8H
clusters, respectively.

In addition to the 4H/8H clusters, we also studied 2H/4H
clusters to examine the system size dependence and the acetylene
(HC≡CH) molecule under triple bond dissociation as the repre-
sentative system of covalent bond cleavage. For the 2H/4H cluster
calculations, the intra- and inter-molecular H–H distances are set to
1.0583 and 100 Å, respectively. The STO-3G basis set is used, with
the active space being (2e, 2o) and (4e, 4o) for the monomer and
dimer, respectively. In the case of acetylene, the monomer is the low-
est spin-quartet state of the C–H fragment, with the bond length set
to the experimental value of acetylene (1.1199 Å). Using the STO-3G
basis set and freezing the 1s core orbital of the C atoms, we con-
structed (5e, 5o) and (10e, 10o) active spaces for the monomer and
dimer, respectively.

In the QPE simulations, we set the time length of the time evo-
lution operator shown in Eq. (2) to t = 1.0. We used ten ancillary
qubits to read out the eigenphase for 4H/8H and 2H/4H clusters,
and we used eight ancillary qubits for the triple bond dissociation of
acetylene. As input wave functions for the QPE, we examined both
the full-CI and HF wave functions to assess the state dependence
of the Trotter error. For the implementation of the controlled-time
evolution operator, we utilized both the first-order and second-
order Trotter decompositions with M = 1, 2, 5, and 10. The Trotter
error depends on the order of the Pauli strings. Unless otherwise
stated, we employed magnitude ordering, where the Pauli strings are
applied in descending order of the absolute value of the correspond-
ing coefficient, ∣wj∣.43 All simulations were conducted using our
custom Python3 code, developed with the OpenFermion,44 Cirq,45
and cuQuantum46 libraries. For reference, the Trotter-free time
evolution was implemented using the expm function in the SciPy
library.47

The computational cost of quantum circuit simulations for the
QPE-based full-CI is substantial, making acceleration crucial for
studying larger systems. In the QPE with N ancillary qubits, we
need to perform the controlled-U operation 2N − 1 times, which
is the most time-consuming process. In this study, we reduce the
simulation cost by sequentially adding ancillary qubits one by one.

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-3

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

FIG. 2. Schematic illustrations of the molecular orbitals for the 4H and 8H clusters. The intermonomer spacing is reduced for clarity. The lowest two and four orbitals for the
monomer and the dimers, respectively, are doubly occupied in the HF wave function.

The schematic representation of our QPE quantum circuit simula-
tion is shown in Fig. 3. In this strategy, the most time-consuming
controlled-U2N−1
is simulated with L + 1 qubits in the first step (the
leftmost dotted square in Fig. 3). Next, we add an ancillary qubit
to simulate the controlled-U2N−2
with L + 2 qubits in the second
step (shown in the second dotted square from the left in Fig. 3). In
this approach, the simulation time for the second step is approxi-
mately the same as that for the first step. This occurs because the
depth of the quantum circuit in the second step is about half of
that in the first step, while the number of qubits increases by one.
The reduction in simulation time due to the decreased circuit depth
is offset by the increased qubit count, leading to nearly equal sim-
ulation times for both steps. The QPE simulations are based on
the implementation shown in Fig. 3, resulting in an exponential

speed up of the numerical simulations from naive implementation
shown in Fig. 1.

IV. RESULTS

A. 4H and 8H clusters

Plots of phase value vs measurement probability from the
QPE-based full-CI of the 4H and 8H clusters, as a function of the
number of Trotter slices M, are shown in Figs. 4 and 5, using
full-CI and HF wave functions, respectively, as the inputs. For
small M, the peak obtained from the Trotterized time evolution
operator is shifted from the peak calculated by the Trotter-free sim-
ulations, but it converges to the Trotter-free result as M increases.
Notably, both CMO- and LMO-based QPE simulations yield peaks

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

FIG. 3. Schematic illustration of the numerical simulations for the QPE-based full-CI. Each step of the numerical simulation is indicated by a dotted square.

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-4

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

FIG. 4. Plot of phase value vs measurement probability from the QPE simulation of 4H/8H clusters using the full-CI wave function as the input. Magnitude ordering is used
for the Trotter decomposition. (a) Monomer, first order Trotter. (b) Monomer, second order Trotter. (c) Dimer CMO, first order Trotter. (d) Dimer CMO, second order Trotter.
(e) Dimer LMO, first order Trotter. (f) Dimer LMO, second order Trotter.

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

FIG. 5. Plot of phase value vs measurement probability from the QPE simulation of 4H/8H clusters using the HF wave function as the input. Magnitude ordering is used for
the Trotter decomposition. (a) Monomer, first order Trotter. (b) Monomer, second order Trotter. (c) Dimer CMO, first order Trotter. (d) Dimer CMO, second order Trotter. (e)
Dimer LMO, first order Trotter. (f) Dimer LMO, second order Trotter.

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-5

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

FIG. 6. Plot of phase value vs measurement probability from the QPE simulation of 4H/8H clusters with the full-CI wave function as the input. Lexicographic ordering is used
for the Trotter decomposition. (a) Monomer, first order Trotter. (b) Monomer, second order Trotter. (c) Dimer CMO, first order Trotter. (d) Dimer CMO, second order Trotter.
(e) Dimer LMO, first order Trotter. (f) Dimer LMO, second order Trotter.

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

at nearly the same position. The peak height is reduced when using
the HF wave function as the input due to the decreased overlap
between the input and full-CI wave functions, although the peak
position remains consistent between the full-CI and HF inputs. It
is important to note that some peaks exhibit larger variance due to
the well-known “leakage problem” in the textbook implementation
of QPE.48

To assess the impact of operator ordering on the Trotterized
time evolution operator, we examined lexicographic ordering in the
Trotter decomposition. The results are shown in Fig. 6. As antici-
pated, the trend of the Trotter error varied with different strategies
for operator ordering. In the dimer CMO calculations using the first-
order Trotter decomposition, the computed peak is already quite
close to the Trotter-free value even for M = 1, likely due to a fortu-
itous cancellation of errors [see Fig. 6(c)]. However, in the first-order
Trotter simulations for M = 1 in the dimer CMO, an additional small
peak is observed around ϕ = 0.492, despite using the full-CI wave
function as the input. This is because the Trotterized time evolu-
tion operator differs from the original time evolution operator, and
the full-CI wave function is no longer an eigenfunction of the Trot-
terized time evolution operator. The presence of additional peaks
indicates a significant deviation of UTrotter from U, suggesting that
a more refined approach to Trotter decomposition is necessary. It
should be noted that the peak positions are insensitive to the order of

the Trotter decomposition for the monomer and dimer with LMOs.
However, this is not always the case. In fact, as we discuss in the
following subsections, we observed clear differences in size con-
sistency breakdown between first-order and second-order Trotter
decompositions.

The eigenphase value is determined by fitting the measure-
ment probability plot with a Gaussian function. The ratio of the
dimer and monomer eigenenergies, EDimer/EMonomer, is computed
and plotted in Figs. 7(a) and 7(b) for magnitude and lexicographic
orderings, respectively, as a function of 1/M. Ideally, when size
consistency is perfectly maintained, this ratio should be equal
to two. However, in our numerical simulations, the ratio devi-
ates slightly from two even in the Trotter-free implementation,
likely due to rounding and leakage errors. To assess the devia-
tion of EDimer/EMonomer values from Trotter decomposition-based
simulation (denoted as “Trotter” in the superscript) compare to
Trotter-free simulations (denoted as “w/o Trotter” in the super-
/Ew/o Trotter
script), we plot ETrotter
Monomer
in Figs. 7(c) and 7(d) for magnitude and lexicographic orderings,
respectively. In this case, using M = 1 for the Trotter decomposi-
tion (where Δt, the time length of a single Trotter slice, is 1.0) is
insufficient to meet the size consistency condition, irrespective of
the operator ordering method and the molecular orbitals employed
for the wave function expansion. Increasing the number of Trotter

Monomer normalized by Ew/o Trotter

Dimer /ETrotter

Dimer

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-6

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

FIG. 7. Ratio of the total energies of the 8H cluster (dimer) to the 4H cluster (monomer) calculated using (a) magnitude ordering and (b) lexicographic ordering. The ratio
values normalized by the Trotter-free simulation results are plotted in (c) and (d).

slices to M = 2 nearly satisfies the size consistency condition, except
for the CMO with first-order Trotter decomposition using lexico-
graphic ordering. Even in this case, the size consistency condition is
systematically recovered with a higher number of Trotter slices. Our
numerical simulations indicate that size consistency is not inher-
ently violated using LMOs for wave function expansion. However,
the convergence behavior toward Trotter-free results with respect
to the number of Trotter slices underscores the importance of
selecting appropriate Trotter decomposition conditions, such as ref-
erence molecular orbitals, the order of Trotter decomposition, and
operator ordering, to ensure size consistency in QPE-based full-CI
calculations.

B. 2H and 4H clusters

Next, we investigate the system size dependency of the break-
down of size consistency in the QPE with Trotterized time evo-
lution operators. We performed the QPE simulations using 2H
and 4H clusters as a monomer and a dimer, respectively. The
ratio of the total energies of the dimer to the monomer, normal-
ized by the Trotter-free simulation results, is plotted in Fig. 8.
Note that the scale of the vertical axis of Fig. 8 is half of that
of Figs. 7(c) and 7(d). Although the deviation from size consis-
tency is smaller in 2H/4H clusters than 4H/8H clusters, lexico-
graphic ordering in conjunction with CMOs is likely to break size
consistency when the number of Trotter slices is small, whereas
LMO nearly maintains size consistency with lexicographic ordering
for M = 1.

C. Triple bond dissociation in acetylene

To examine the size consistency condition under bond break-
ing, we conducted QPE simulations of acetylene undergoing triple
bond dissociation, using the C≡H fragment as the monomer. The
results are summarized in Fig. 9. Due to the large total ener-
gies of the acetylene system, we plotted the ratio of the eigenen-
ergies of the qubit Hamiltonian without constant terms (frozen
core energy and the constant term obtained in the SCBKT).
Note that the constant term of the dimer is exactly twice that
of the monomer. We observed a clear difference in the behav-
ior of size consistency breakdown between the CMO and LMO.
Size consistency is nearly preserved when the LMO is used for
wave function expansion, even with lexicographic ordering and
M = 1 in the Trotter decomposition. In contrast, the CMO-
based calculation shows a breakdown in size consistency for
small M. It
to note that size consistency does
not always guarantee accurate total energy. Specifically, Ew/o Trotter
Monomer
− ETrotter
Dimer;LMO values with lexicographic
ordering and M = 1 are calculated as 0.0020 and 0.0040 hartree,
respectively.

Monomer and Ew/o Trotter

Dimer;LMO − ETrotter

is important

D. Comparison between the LMO and CMO

As we observed from the numerical simulations, the extent of
size consistency violation is smaller for the LMO than the CMO.
This observation is consistent with expectations from a chemical
perspective.

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-7

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

FIG. 8. Ratio of the total energies of the 4H cluster (dimer) to the 2H cluster (monomer) normalized by the Trotter-free simulation results. (a) Magnitude ordering. (b)
Lexicographic ordering.

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

FIG. 9. Ratio of the total energies of the dimer to the monomer normalized by the Trotter-free simulation results in triple bond dissociation of acetylene. (a) Magnitude ordering.
(b) Lexicographic ordering.

Consider a dimer composed of

spatially well-separated
monomers A and B. In the LMO basis, in the limit of weak inter-
monomer interaction, the Hamiltonian of the dimer, H(A + B), can
be expressed as a linear combination of monomer Hamiltonians
H(A) and H(B),

with

H(A + B) = H(A) + H(B),

[H(A), H(B)] = 0.

(11)

(12)

Using the commutation relation in Eq. (12), the Trotterized time
evolution operator for the dimer can be rewritten as the product
of the Trotterized time evolution operators for monomers A and B,
with the Trotterized terms arranged accordingly. For instance, in the
first-order Trotter decomposition, we have

−iH(A+B)qt = [Πje

e

−iwj Pj t/M]

M

= [Πk∈Ae

−iwkPkt/MΠl∈Be

−iwlPlt/M]

M

.

(13)

If the orderings of the Pauli strings Pk∈ A and Pl∈ B in Eq. (13)
are the same as those in the Trotterized time evolution operators
for monomers A and B, respectively, then size consistency can be
preserved.

In contrast, when CMOs are used for wave function expan-
sion, decomposing the dimer Hamiltonian H(A + B) into H(A) and
H(B) is not straightforward. Consequently, it is not possible to rear-
range the terms in the Trotterized time evolution operator for the
dimer to express it as a product of the Trotterized time evolution
operators for the monomers.

V. SUMMARY

A recent theoretical study on VQE-UCCSD highlighted that
size consistency can be violated by Trotter decomposition, when
the molecular orbitals delocalized over the dimer are used.29 In this
study, we investigated the impact of Trotter decomposition of the
time evolution operator in QPE-based full-CI calculations, focus-
ing on the size consistency condition. Our numerical simulations
of the 4H/8H clusters, 2H/4H clusters, and triple bond dissociation

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-8

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

in acetylene, using both CMOs and LMOs, revealed that the eigen-
phase values obtained from the QPE are less sensitive to the choice of
molecular orbitals when magnitude ordering is employed, and size
consistency is nearly maintained when the evolution time length of
a single Trotter slice is set to 0.2 or shorter. In contrast, with lexi-
cographic ordering, size consistency is not satisfied when the CMO
is used in conjunction with a small number of Trotter slices. How-
ever, size consistency can be systematically recovered by increasing
the number of Trotter slices. The fact that the QPE-based full-CI
can satisfy the size consistency condition under appropriate Trotter
decomposition conditions is promising for quantum chemical calcu-
lations on quantum computers. This becomes particularly relevant
as large-scale quantum chemical calculations that are intractable on
classical computers become feasible. The integration of the QPE
with fragmentation-based methods where size consistency is crucial,
such as divide-and-conquer (DC),49 density matrix embedding the-
ory (DMET),50 and fragment molecular orbital (FMO)51 methods,
appears to be a promising direction, which will be discussed in a
forthcoming paper.

ACKNOWLEDGMENTS

The computation was carried out using the JHPCN Joint
jh240001) on the supercomputer
Research Projects (Grant No.
“Flow” at the Information Technology Center, Nagoya Univer-
sity. K. Sugisaki acknowledges Naoki Yamamoto, Takashi Abe,
Yu-ya Ohnishi, Shu Kanno, and Yudai Suzuki for useful discus-
sions. This work was supported by the Quantum-LEAP Flagship
Program (Grant No. JPMXS0120319794) from the Ministry of Edu-
cation, Culture, Sports, Science and Technology (MEXT), Japan;
the Center of Innovations for Sustainable Quantum AI (Grant
No. JPMJPF2221) from the Japan Science and Technology Agency
(JST), Japan; and Grants-in-Aid for Scientific Research C (Grant
No. 21K03407) and for Transformative Research Area B (Grant No.
23H03819) from the Japan Society for the Promotion of Science
(JSPS), Japan.

AUTHOR DECLARATIONS

Conflict of Interest

The author has no conflicts to disclose.

Author Contributions

Kenji Sugisaki: Conceptualization (lead); Investigation (lead); Soft-
ware (lead); Validation (lead); Writing – original draft (lead);
Writing – review & editing (lead).

DATA AVAILABILITY

The data that support the findings of this study are available

from the corresponding author upon reasonable request.

REFERENCES

1A. Aspuru-Guzik, A. D. Dutoi, P. J. Love, and M. Head-Gordon, “Simulated
quantum computation of molecular energies,” Science 309, 1704–1707 (2005).

2L. Veis and J. Pittner, “Quantum computing applied to calculations of molecular
energies: CH2 benchmark,” J. Chem. Phys. 133, 194106 (2010).
3M. Reiher, N. Wiebe, K. M. Svore, D. Wecker, and M. Troyer, “Elucidating reac-
tion mechanisms on quantum computers,” Proc. Natl. Acad. Sci. U. S. A. 114,
7555–7560 (2017).
4R. Babbush, C. Gidney, D. W. Berry, N. Wiebe, J. McClean, A. Paler, A. Fowler,
and H. Neven, “Encoding electronic spectra in quantum circuits with linear T
complexity,” Phys. Rev. X 8, 041015 (2018).
5J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean, N. Wiebe, and
R. Babbush, “Even more efficient quantum computations of chemistry through
tensor hypercontraction,” PRX Quantum 2, 030305 (2021).
6N. P. Bauman, H. Liu, E. J. Bylaska, S. Krishnamoorthy, G. H. Low, C. E. Granade,
N. Wiebe, N. A. Baker, B. Peng, M. Roetteler, M. Troyer, and K. Kowalski,
“Toward quantum computing for high-energy excited states in molecular systems:
Quantum phase estimations of core-level states,” J. Chem. Theory Comput. 17,
201–210 (2021).
7I. H. Kim, Y.-H. Liu, S. Pallister, W. Pol, S. Roberts, and E. Lee, “Fault-tolerant
resource estimate for quantum chemical simulations: Case study on Li-ion battery
electrolyte molecules,” Phys. Rev. Res. 4, 023019 (2022).
8R. Izsak, C. Riplinger, N. S. Blunt, B. de Souza, N. Holzmann, O. Crawford, J.
Camps, F. Neese, and P. Schopf, “Quantum computing in pharma: A multilayer
embedding approach for near future applications,” J. Comput. Chem. 44, 406–421
(2023).
9C. Kang, N. P. Bauman, S. Krishnamoorthy, and K. Kowalski, “Optimized quan-
tum phase estimation for simulating electronic states in various energy regimes,”
J. Chem. Theory Comput. 18, 6567–6576 (2022).
10D. Halder, V. S. Prasannaa, V. Agarawal, and R. Maitra, “Iterative quantum
phase estimation with variationally prepared reference state,” Int. J. Quantum
Chem. 123, e27021 (2022).
11P. A. M. Casares, R. Campos, and M. A. Martin-Delgado, “TFermion: A non-
Clifford gate cost assessment library of quantum phase estimation algorithms for
quantum chemistry,” Quantum 6, 768 (2022).
12Y. Ino, M. Yonekawa, H. Yuzawa, Y. Minato, and K. Sugisaki, “Quantum
phase estimations of benzene and its derivatives on GPGPU quantum simulators,”
arXiv:2312.16375 (2023).
13M. Otten, B. Kang, D. Fedorov, J.-H. Lee, A. Benali, S. Habib, S. K. Gray, and
Y. Alexeev, “QREChem: Quantum resource estimation software for chemistry
applications,” Front. Quantum Sci. Technol. 2, 1232624 (2023).
14A. Roggero and J. Carlson, “Dynamic linear response quantum algorithm,”
Phys. Rev. C 100, 034610 (2019).
15K. Sugisaki, C. Sakai, K. Toyota, K. Sato, D. Shiomi, and T. Takui,
“Bayesian phase difference estimation: A general quantum algorithm for the
direct calculation of energy gaps,” Phys. Chem. Chem. Phys. 23, 20152–20162
(2021).
16K. Sugisaki, “Projective measurement-based quantum phase difference esti-
mation algorithm for the direct computation of eigenenergy differences on a
quantum computer,” J. Chem. Theory Comput. 19, 7617–7625 (2023).
17K. Kowalski, N. P. Bauman, G. H. Low, M. Roetteler, J. J. Rehr, and F.
D. Vila, “Capturing many-body correlation effects with quantum and classical
computing,” arXiv:2402.11418 (2024).
18R. Sakuma, S. Kanno, K. Sugisaki, T. Abe, and N. Yamamoto, “Entanglement-
assisted phase estimation algorithm for calculating dynamical
response
functions,” Phys. Rev. A 110, 022618 (2024).
19B. P. Lanyon, J. D. Whitfield, G. G. Gillett, M. E. Goggin, M. P. Almeida, I.
Kassal, J. D. Biamonte, M. Mohseni, B. J. Powell, M. Barbieri, A. Aspuru-Guzik,
and A. G. White, “Towards quantum chemistry on a quantum computer,” Nat.
Chem. 2, 106–111 (2010).
20J. Du, N. Xu, X. Peng, P. wang, S. Wu, and D. Lu, “NMR implementation of a
molecular hydrogen quantum simulation with adiabatic state preparation,” Phys.
Rev. Lett. 104, 030502 (2010).
21P. J. J. O’Malley, R. Babbush, I. D. Kivlichan, J. Romero, J. R. McClean, R.
Barends, J. Kelly, P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen, Z. Chen,
B. Chiaro, A. Dunsworth, A. G. Fowler, E. Jeffrey, E. Lucero, A. Megrant, J. Y.
Mutus, M. Neeley, C. Neill, C. Quintana, D. Sank, A. Vainsencher, J. Wenner,
T. C. White, P. V. Coveney, P. J. Love, H. Neven, A. Aspuru-Guzik, and J. M.

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-9

AIP Advances

ARTICLE

pubs.aip.org/aip/adv

Martinis, “Scalable quantum simulation of molecular energies,” Phys. Rev. X 6,
031007 (2016).
22K. Yamamoto, S. Duffield, Y. Kikuchi, and D. Munõz Ramo, “Demonstrating
Bayesian quantum phase estimation with quantum error detection,” Phys. Rev.
Res. 6, 013221 (2024).
23Y. Wang, F. Dolde, J. Biamonte, R. Babbush, V. Bergholm, S. Yang, I. Jakobi,
P. Neumann, A. Aspuru-Guzik, J. D. Whitfield, and J. Wrachtrup, “Quantum
simulation of helium hydride cation in a solid-state spin register,” ACS Nano 9,
7769–7774 (2015).
24N. S. Blunt, L. Caune, R. Izsák, E. T. Campbell, and N. Holzmann, “Statistical
phase estimation and error mitigation on a superconducting quantum processor,”
PRX Quantum 4, 040341 (2023).
25A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A.
Aspuru-Guzik, and J. L. O’Brien, “A variational eigenvalue solver on a photonic
quantum processor,” Nat. Commun. 5, 4213 (2014).
26J. Tilly, H. Chen, S. Cao, D. Picozzi, K. Setia, Y. Li, E. Grant, L. Wossnig, I.
Rungger, G. H. Booth, and J. Tennyson, “The variational quantum eigensolver: A
review of methods and best practices,” Phys. Rep. 986, 1–128 (2022).
27A. Anand, P. Schleich, S. Alperin-Lea, P. W. K. Jensen, S. Sim, M. Diaz-Tinoco,
J. S. Kottmann, M. Degroote, A. F. Izmaylov, and A. Aspuru-Guzik, “A quan-
tum computing view on unitary coupled cluster theory,” Chem. Soc. Rev. 51,
1659–1684 (2022).
28A. Szabo and N. S. Ostlund, Modern Quantum Chemistry: Introduction to
Advanced Electronic Structure Theory (Dover Publication, Inc., Minoela, NY,
1996).
29K. Sugisaki, T. Nakano, and Y. Mochizuki, “Size-consistency and orbital-
invariance issues revealed by VQE-UCCSD calculations with the FMO scheme,”
J. Comput. Chem. 45, 2204 (2024).
30A. Y. Kitaev, “Quantum measurements and the Abelian stabilizer problem,”
arXiv:quant-ph/9511026 (1995).
31D. S. Abrams and S. Lloyd, “Quantum algorithm providing exponential speed
increase for finding eigenvalues and eigenvectors,” Phys. Rev. Lett. 83, 5162–5165
(1999).
32M. Born and R. Oppenheimer, “Zur quantentheorie der molekeln,” Ann. Phys.
389, 457–484 (1927).
33M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Infor-
mation, 10th anniversary ed. (Cambridge University Press, Cambridge, UK,
2010).
34P. Jordan and E. Wigner, “Über das paulische äquivalenzverbot,” Z. Phys. 47,
631–651 (1928).
35J. T. Seeley, M. J. Richard, and P. J. Love, “The Bravyi–Kitaev transformation for
quantum computation of electronic structure,” J. Chem. Phys. 137, 224109 (2012).
36D. W. Berry, A. M. Childs, R. Cleve, R. Kothari, and R. D. Somma, “Simulating
Hamiltonian dynamics with a truncated Taylor series,” Phys. Rev. Lett. 114,
090502 (2015).
37A. Daskin and S. Kais, “A generalized circuit for the Hamiltonian dynamics
through the truncated series,” Quantum Inf. Process. 17, 328 (2018).
38G. H. Low and I. L. Chuang, “Hamiltonian simulation by qubitization,”
Quantum 3, 163 (2019).
39D. W. Berry, C. Gidney, M. Motta,
J. R. McClean, and R. Babbush,
“Qubitization of arbitrary basis quantum chemistry leveraging sparsity and low
rank factorization,” Quantum 3, 208 (2019).

40J. Paldus, P. Piecuch, L. Pylypow, and B. Jeziorski, “Application of Hilbert-space
coupled-cluster theory to simple (H2)2 model systems: Planar models,” Phys. Rev.
A 47, 2738–2782 (1993).
41G. M. J. Barca, C. Bertoni, L. Carrington, D. Datta, N. De Silva, J. E. Deustua, D.
G. Fedorov, J. R. Gour, A. O. Gunina, E. Guidez, T. Harville, S. Irle, J. Ivanic, K.
Kowalski, S. S. Leang, H. Li, W. Li, J. J. Lutz, I. Magoulas, J. Mato, V. Mironov, H.
Nakata, B. Q. Pham, P. Piecuch, D. Poole, S. R. Pruitt, A. P. Rendell, L. B. Roskop,
K. Ruedenberg, T. Sattasathuchana, M. W. Schmidt, J. Shen, L. Slipchenko, M.
Sosonkina, V. Sundriyal, A. Tiwari, J. L. Galvez Vallejo, B. Westheimer, M. Wloch,
P. Xu, F. Zahariev, and M. S. Gordon, “Recent developments in the general
atomic and molecular electronic structure system,” J. Chem. Phys. 152, 154102
(2020).
42S. Bravyi, J. M. Gambetta, A. Mezzacapo, and K. Temme, “Tapering off qubits
to simulate fermionic Hamiltonians,” arXiv:1701.08213 (2017).
43A. Tranter, P. J. Love, F. Mintert, and P. V. Coveney, “A comparison of
the Bravyi–Kitaev and Jordan–Wigner transformations for the quantum sim-
ulation of quantum chemistry,” J. Chem. Theory Comput. 14, 5617–5630
(2018).
44J. R. McClean, N. C. Rubin, K. J. Sung, I. D. Kivlichan, X. Bonet-Monroig, Y.
Cao, C. Dai, E. S. Fried, C. Gidney, B. Gimby, P. Gokhale, T. Häner, T. Hardikar,
V. Havlìˇcek, O. Higgott, C. Huang, J. Izaac, Z. Jiang, X. Liu, S. McArdle, M. Neeley,
T. O’Brien, B. O’Gorman, I. Ozfidan, M. D. Radin, J. Romero, N. P. D. Sawaya, B.
Senjean, K. Setia, S. Sim, D. S. Steiger, M. Steudtner, Q. Sun, W. Sun, D. Wang,
F. Zhang, and R. Babbush, “OpenFermion: The electronic structure package for
quantum computers,” Quantum Sci. Technol. 5, 034014 (2020).
45Cirq Developers (2022). “Cirq (v1.2.0),” Zenodo. https://doi.org/10.5281/
zenodo.8161252
46H. Bayraktar, A. Charara, D. Clark, S. Cohen, T. Costa, Y.-L. L. Fang, Y. Gao,
J. Guan, J. Gunnels, A. Haidar, A. Hehn, M. Hohnerbach, M. Jones, T. Lubowe,
D. Lyakh, S. Morino, P. Springer, S. Stanwyck, I. Terentyev, S. Varadhan, J.
Wong, and T. Yamaguchi, “cuQuantum SDK: A high-performance library for
accelerating quantum science,” IEEE Int. Conf. Quant. Comput. Enginer. 1, 1050
(2023).
47P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cour-
napeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M.
Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern,
E. Larson, C. J. Carey, Í. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J.
Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald,
A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, and SciPy 1.0 Contributors, “SciPy
1.0: Fundamental algorithms for scientific computing in Python,” Nat. Methods
17, 261–272 (2020).
48Y. Xiong, S. X. Ng, G.-L. Long, and L. Hanzo, “Dual-frequency quantum phase
estimation mitigates the spectral leakage of quantum algorithms,” IEEE Signal
Process. Lett. 29, 1222–1226 (2022).
49W. Yang and T.-S. Lee, “A density-matrix divide-and-conquer approach
for electronic structure calculations of large molecules,” J. Chem. Phys. 103,
5674–5678 (1995).
50G. Knizia and G. K.-L. Chan, “Density matrix embedding: A simple
alternative to dynamical mean-field theory,” Phys. Rev. Lett. 109, 186404
(2012).
51K. Kitaura, E. Ikeo, T. Asada, T. Nakano, and M. Uebayasi, “Fragment molecu-
lar orbital method: An approximate computational method for large molecules,”
Chem. Phys. Lett. 313, 701–706 (1999).

0
6

M
a
y

2
0
2
6

2
0
:
2
2
:
5
3

AIP Advances 14, 095021 (2024); doi: 10.1063/5.0223661

© Author(s) 2024

14, 095021-10

