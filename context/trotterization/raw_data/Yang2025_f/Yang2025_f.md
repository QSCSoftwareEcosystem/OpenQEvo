# Quantum simulation of many-body dynamics with noise-robust Trotter decomposition based on symmetric structures

Bo Yang<sup>1, 2, a)</sup> and Naoki Negishi<sup>3, 4, 5, a)</sup>

<sup>1)</sup>LIP6, Sorbonne Université, CNRS, 4 place Jussieu, 75005 Paris, France

<sup>2)</sup>Graduate School of Information Science and Technology, The University of Tokyo, Bunkyo-ku, Tokyo 113-8656, Japan

<sup>3)</sup>Graduate School of Arts and Sciences, The University of Tokyo, Meguro-ku, Tokyo, 153-8902, Japan

<sup>4)</sup>Dipartimento di Fisica, Università di Roma Tor Vergata, Via della Ricerca Scientifica 1, 00133 Rome, Italy

<sup>5)</sup>INFN, Sezione di Roma Tor Vergata, Via della Ricerca Scientifica 1, 00133 Rome, Italy

(\*Electronic mail: negishi@roma2.infn.it) (\*Electronic mail: Bo.Yang@lip6.fr)

(Dated: 16 December 2025)

The Suzuki-Trotter decomposition, which digitalizes quantum time evolution, provides a promising framework for simulating quantum dynamics on quantum hardware and exploring quantum advantage over classical computation. However, conventional Trotter circuits require a large number of non-local gates, lowering their faithfulness to the ideal dynamics when implemented on current noisy quantum hardware. While most previous studies have focused on circuit optimization, we instead propose a new Trotter decomposition that is intrinsically circuit-efficient for simulating quantum dynamics on near-term devices. Our method substantially reduces both the residual error by Trotter decomposition and the number of CNOT operations compared to conventional Trotter decompositions by exploiting the symmetry of the target model to construct an effective Hamiltonian with fewer two-qubit gates. We demonstrate the noise robustness of the proposed approach through numerical simulations of a nine-site Heisenberg model under realistic noise, and further validate its experimental practicality on the IBM superconducting device, achieving a state fidelity exceeding 0.98 when combined with quantum error mitigation in the three-site case. The proposed circuit design is also compatible with existing circuit optimization techniques. Our results establish a practical route toward noise-resilient quantum simulation in many-body dynamics.

# I. INTRODUCTION

Through the rapid advance of quantum hardware, quantum simulation has gained emerging attention to simulate physical and chemical models that become practically intractable by classical computational resources<sup>1,2</sup>. Its prominent and versatile applicability lies in non-equilibrium quantum manybody dynamics, where the digital simulation based on Suzuki-Trotter decomposition enables tractable and scalable approximation of real-time evolution<sup>3–5</sup>. Simulating Trotter iterations with quantum computers frees from classical simulation with exponential computational resources, requiring only linear overhead to system size, which is thus seen as one of the applications with potential near-term quantum advantage.

However, the non-negligible noise level and hardware restrictions of current quantum hardware still pose a significant obstacle to the practical realization of such Trotter-based simulations. In particular, superconducting quantum devices<sup>6</sup>, which are among the most extensively developed and commercially accessible platforms, suffer from noisy non-local gates and limited coherence times<sup>7,8</sup>. Therefore, it is essential to design quantum circuits with reduced depth and fewer non-local gates, such as CNOT gates, to alleviate noise accumulation and improve the fidelity of simulations.

While substantial efforts have focused on optimizing given Trotter circuits under hardware constraints<sup>9–14</sup>, the underlying Trotter decomposition itself sets the fundamental limits of such optimization. In this work, we design a new alternative Trotter decomposition strategy that substantially reduces both the residual error by Trotter decomposition and the number of CNOT gates in use. To achieve this, we exploit the symmetric structure of the given Hamiltonian, particularly, of the *XXX* Heisenberg model. In particular, we transform the three-site Heisenberg Hamiltonian into a more concise two-site effective Hamiltonian through an encoding and decoding procedure. This transformation enables a faster convergence rate of the Trotter iterations compared with using the conventional Trotter decomposition, thereby requiring fewer Trotter iterations to achieve the same level of residual error.

This new decomposition with the effective Hamiltonian reduces the average number of CNOT gates in each Trotter step to 1.75 per qubit, whereas the conventional Trotter circuit requires 3. The proposed method highlights the potential of reducing the circuit overhead with a more efficient approach for Trotter decomposition rather than merely performing circuit optimization on existing Trotter circuits. The schematic illustration of the proposed method can be found in Fig. 1.

We demonstrate the noise-robustness of our proposed method through numerical simulation. Our method outperforms the conventional Trotter decomposition in simulating the time evolution of the nine-site *XXX* Heisenberg model in both setups without noise and with depolarizing noise.

<sup>&</sup>lt;sup>a)</sup>The authors contributed equally.

![](_page_1_Picture_2.jpeg)

FIG. 1. The schematic illustration of the proposed framework. In simulating the time evolution of a given Hamiltonian, we exploit its symmetric structure to construct Trotter blocks with a faster convergence rate and fewer CNOT gates based on the effective Hamiltonian

We also simulate the time evolution of a three-site *XXX* Heisenberg model on the superconducting quantum device ibmq\_jakarta provided by the IBM Quantum Platform<sup>6</sup>. Using quantum error mitigation (QEM)<sup>15–22</sup>, we achieve the target state fidelity over 0.98 on ibmq\_jakarta. In implementing the proposed Trotter circuits, our method finds further compatibility with circuit optimization with the Qiskit package<sup>23</sup>. The overall experiments demonstrate that our method offers not only a novel, efficient Trotter decomposition scheme but also a practical and feasible solution for simulating physical models on current quantum hardware.

### II. SUZUKI-TROTTER DECOMPOSITION

We consider *N*-site J=1 *XXX* Heisenberg Hamiltonian with N=2M+1,  $M\in\mathbb{Z}_{\geq 0}$ , and open boundary condition formalized as

$$\hat{H} = \sum_{i=1}^{N-1} \vec{\sigma}^{(i)} \cdot \vec{\sigma}^{(i+1)}, \tag{1}$$

where denotes the inner product of three components of the Pauli operators of *i*-th site,  $\hat{\sigma}_x^{(i)} := \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \hat{\sigma}_y^{(i)} := \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ ,

and 
$$\hat{\sigma}_z^{(i)} := \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
, defined as

$$\vec{\sigma}^{(i)} \cdot \vec{\sigma}^{(j)} := \sum_{\mu \in \{x, y, z\}} \hat{\sigma}_{\mu}^{(i)} \otimes \hat{\sigma}_{\mu}^{(j)} \quad \text{for} \quad i \neq j.$$
 (2)

Given a Heisenberg Hamiltonian  $\hat{H} = \hat{O}_1 + \hat{O}_2$  that consists of two non-commutative operators  $\hat{O}_1$  and  $\hat{O}_2$ , i.e.  $[\hat{O}_1, \hat{O}_2] \neq 0$ , the conventional Trotter decomposition with n steps<sup>3–5</sup> approximates the evolution of this Hamiltonian with

$$\hat{U}(t) = \left(\exp\left(-\mathrm{i}\hat{O}_{2}\Delta t\right)\exp\left(-\mathrm{i}\hat{O}_{1}\Delta t\right)\right)^{n} + \mathcal{O}\left(\hat{\varepsilon}_{1}n^{-1}\right),\tag{3}$$

where  $\Delta t = t/n$  denotes the evolution time for a step, and  $\hat{O}_1$  and  $\hat{O}_2$  are chosen to be

$$\hat{O}_1 = \sum_{i=1}^{M} \vec{\sigma}^{(2i-1)} \cdot \vec{\sigma}^{(2i)}, \tag{4}$$

$$\hat{O}_2 = \sum_{i=1}^{M} \vec{\sigma}^{(2i)} \cdot \vec{\sigma}^{(2i+1)}, \tag{5}$$

and  $\hat{\epsilon}_1$  is the operator in the error term as follows:

$$\hat{\varepsilon}_{1} = [\hat{O}_{1}, \hat{O}_{2}]$$

$$= \sum_{i=2}^{N-1} (-1)^{i} [\vec{\sigma}^{(i-1)} \cdot \vec{\sigma}^{(i)}, \vec{\sigma}^{(i)} \cdot \vec{\sigma}^{(i+1)}].$$
(6)

The quantum circuit for the decomposition Eq. (3) can be constructed in the following way. First, let  $\hat{u}^{(i)}(\Delta t)$  be the unitary operator of evolution time  $\Delta t$  for i-th and i+1-th qubit defined as

$$\hat{u}^{(i)}(\Delta t) = \exp\left(-i\vec{\sigma}^{(i)} \cdot \vec{\sigma}^{(i+1)} \Delta t\right). \tag{7}$$

Since any two-qubit unitary operation can be realized by three CNOT gates<sup>24–26</sup>, Fig. 2 provides a quantum circuit to implement  $\hat{u}^{(i)}(t)$ .

$$\hat{u}(\Delta t) = \begin{pmatrix} R_z(2\Delta t - \pi/2) & R_z(\pi/2) \\ R_z(-\pi/2) & R_y(\pi/2 - 2\Delta t) \end{pmatrix} \begin{pmatrix} R_z(\pi/2) & R_z(\pi/2) \\ R_z(\pi/2) & R_z(\pi/2) \end{pmatrix}$$

FIG. 2. The quantum circuit of the unitary operator in Eq. (7).

Using this circuit block, the Trotter decomposition in Eq. (3) is then constructed by the quantum circuit in Fig. 3. Since each time step has two layers of operator  $\hat{u}^{(i)}(t)$ , the averaged number of CNOT gates applied over each qubit is three, which represents the most efficient circuit construction regarding the CNOT overhead known to date<sup>27</sup>.

![](_page_1_Figure_24.jpeg)

FIG. 3. The quantum circuit of the time evolution operator using the Trotter decomposition in Eq. (3) for the 5-site system. The operation corresponding to the propagation of each single time step  $\Delta t$  is enclosed by a dashed box.

#### III. PROPOSED DECOMPOSITION

![](_page_2_Picture_3.jpeg)

![](_page_2_Picture_4.jpeg)

FIG. 4. (a) The schematic illustration of the conventional Trotter decomposition that takes non-commutative Trotter blocks with propagator  $\hat{u}(\Delta t)$  according to the native edge structure of the given Hamiltonian. (b) The schematic illustration of the proposed Trotter decomposition that takes non-commutative Trotter blocks with propagator  $\hat{U}_{\rm enc}^{\dagger} \exp\left(-i\hat{H}_{\rm eff}\Delta t'\right)\hat{U}_{\rm enc}$  according to the hyper-edge of the set with three neighboring vertices in the given Hamiltonian.

In order to reduce the number of CNOT gates in each single time step, we propose a new Trotter decomposition. First, we partition the Heisenberg Hamiltonian into  $\hat{H} = \hat{A}_1 + \hat{B}_1$  with the operators

$$\hat{A}_1 = \sum_{i=1}^{M'} \vec{\sigma}^{(4i-3)} \cdot \vec{\sigma}^{(4i-2)} + \vec{\sigma}^{(4i-2)} \cdot \vec{\sigma}^{(4i-1)}, \tag{8}$$

$$\hat{B}_1 = \sum_{i=1}^{M''} \vec{\sigma}^{(4i-1)} \cdot \vec{\sigma}^{(4i)} + \vec{\sigma}^{(4i)} \cdot \vec{\sigma}^{(4i+1)}, \tag{9}$$

where M' = M'' = M/2 for  $M \in 2\mathbb{Z}$  and M' = M'' + 1 = (M+1)/2 for  $M \notin 2\mathbb{Z}$ . Likewise, we also propose another decomposition  $\hat{H} = \hat{A}_2 + \hat{B}_2$  with the operators

$$\hat{A}_{2} = \delta_{M,2N'+1} \vec{\sigma}^{(2M)} \cdot \vec{\sigma}^{(2M+1)}$$

$$+ \sum_{i=1}^{N'} \vec{\sigma}^{(4i-2)} \cdot \vec{\sigma}^{(4i-1)} + \vec{\sigma}^{(4i-1)} \cdot \vec{\sigma}^{(4i)}, \qquad (10)$$

$$\hat{B}_{2} = \vec{\sigma}^{(1)} \cdot \vec{\sigma}^{(2)} + \delta_{M,2N'} \vec{\sigma}^{(2M)} \cdot \vec{\sigma}^{(2M+1)}$$

$$+ \sum_{i=1}^{N''-1} \vec{\sigma}^{(4i)} \cdot \vec{\sigma}^{(4i+1)} + \vec{\sigma}^{(4i+1)} \cdot \vec{\sigma}^{(4i+2)}, \qquad (11)$$

where N' = N'' = M/2 for  $M \in 2\mathbb{Z}$  and N' = N'' - 1 = (M - 1)/2 for  $M \notin 2\mathbb{Z}$ .

Using  $\hat{A}_k$  and  $\hat{B}_k$ , we define a single Trotter iteration as a sequence of propagators

$$\exp\left(-\mathrm{i}\hat{B}_{2}\Delta t'\right)\exp\left(-\mathrm{i}\hat{A}_{2}\Delta t'\right)\exp\left(-\mathrm{i}\hat{B}_{1}\Delta t'\right)\exp\left(-\mathrm{i}\hat{A}_{1}\Delta t'\right). \tag{12}$$

Then, the unitary operation that evolves the system for the time t using m proposed Trotter iterations with  $\Delta t' = t/(2m)$ 

![](_page_2_Picture_15.jpeg)

FIG. 5. The quantum circuit to realize the encoder  $\hat{U}_{enc}$ .

is described as

$$\hat{U}(t) = \left(\exp\left(-i\hat{B}_{2}\Delta t'\right)\exp\left(-i\hat{A}_{2}\Delta t'\right)\right)$$

$$\exp\left(-i\hat{B}_{1}\Delta t'\right)\exp\left(-i\hat{A}_{1}\Delta t'\right)\right)^{m}$$

$$+\mathcal{O}\left(\hat{\epsilon}_{2}m^{-1}\right),$$
(13)

with an operator  $\hat{\epsilon}_2$  defined as

$$\hat{\varepsilon}_{2} = \frac{1}{4} [\hat{A}_{1}, \hat{B}_{1}] + \frac{1}{4} [\hat{A}_{2}, \hat{B}_{2}] 
= \frac{1}{4} \sum_{j=1}^{M} (-1)^{j} [\vec{\sigma}^{(2j-1)} \cdot \vec{\sigma}^{(2j)}, \vec{\sigma}^{(2j)} \cdot \vec{\sigma}^{(2j+1)}] 
+ \frac{1}{4} \sum_{j=1}^{M-1} (-1)^{j} [\vec{\sigma}^{(2j)} \cdot \vec{\sigma}^{(2j+1)}, \vec{\sigma}^{(2j+1)} \cdot \vec{\sigma}^{(2j+2)}], \quad (14)$$

Remarkably, the number of required Trotter iterations m in Eq. (13) is smaller than n in Eq. (3) to achieve the same level of residual error by Trotter decomposition. This arises from the fact that, as shown in Fig. 4, the proposed Trotter iteration has sparser decomposition interval than the conventional one, which yields fewer combinations of non-commutative operators that contributes to the residual error. In particular, the residual error of Eqs. (13) and (14) is reduced to one-quarters of that of the conventional Trotter decomposition for m = n. This implies that using m = n/4 iterations of the proposed Trotter blocks achieves the same level of residual error as the conventional Trotter blocks.

Next, we aim at designing efficient quantum circuits of the time evolution operator  $\exp\left(-i\hat{A}_k\Delta t'\right)$  and  $\exp\left(-i\hat{B}_k\Delta t'\right)$ , where  $\hat{A}_k$  and  $\hat{B}_k$  take the form of a three-site XXX Heisenberg Hamiltonian  $\hat{H}_3 = \vec{\sigma}^{(1)} \cdot \vec{\sigma}^{(2)} + \vec{\sigma}^{(2)} \cdot \vec{\sigma}^{(3)}$ . To construct an efficient quantum circuit of  $\exp\left(-i\hat{H}_3t\right)$ , we compress it to a smaller subsystem by deriving an effective Hamiltonian  $H_{\rm eff}$  focusing on the SU(2) symmetry that  $\hat{H}_3$  is equipped with. We use the fact that the three-site Hamiltonian  $\hat{H}_3$  commutes with the operator defined as  $\hat{s}_\mu := -\hat{\sigma}_\mu^{(1)} \otimes \hat{\sigma}_\mu^{(2)} \otimes \hat{\sigma}_\mu^{(3)}$ , i.e.  $[\hat{H}_3, \hat{s}_\mu] = 0$  and that SU(2) group is spanned by  $\{\hat{s}_\mu\}_{\mu=x,y,z}$ . This symmetry structure yields simultaneous eigenstates as follows:

$$\hat{H}_3 |E\rangle \otimes |P\rangle = E |E\rangle \otimes |P\rangle, \tag{15}$$

$$\hat{s}_{7}|E\rangle\otimes|P\rangle=P|E\rangle\otimes|P\rangle,\tag{16}$$

where  $|E\rangle$  and  $|P\rangle$  denote the eigenstate of the energy E and the eigenvalue  $P \in \{-1,1\}$  of  $\hat{s}_z$ , respectively. This implies

that the eigenstates are doubly degenerated regarding the energy E.

This double degeneracy stemming from SU(2) symmetry is essential to compress  $\hat{H}_3$  into a lower dimensional effective Hamiltonian  $\hat{H}_{\rm eff}$ . Thanks to this degeneracy, one can encode the three-site state into the composition of a single-qubit system specifying the eigenvalue P and the remaining two-qubit system specifying the state within the subspace corresponding to P. This encoding is represented by a unitary  $\hat{U}_{\rm enc}$  that transforms the basis  $|E\rangle \otimes |P\rangle$  into another separable state,

$$\hat{U}_{\text{enc}}|E\rangle\otimes|1\rangle=|0\rangle\otimes|\Psi_{E}\rangle,\tag{17}$$

$$\hat{U}_{\text{enc}} |E\rangle \otimes |-1\rangle = |1\rangle \otimes |\Psi_E\rangle, \qquad (18)$$

where  $\{|0\rangle, |1\rangle\}$  denotes the state in the single-qubit system and  $|\Psi_E\rangle$  denotes the state in the two-qubit system. This encoder  $\hat{U}_{enc}$  can be constructed with three CNOT gates, as shown in Fig. 5.

$$e^{-i\hat{H}_{\text{eff}}\Delta t'} = \frac{R_y(-\pi/4) R_z(\sqrt{2}\Delta t') R_z(-2\Delta t')}{R_y(-\pi/4) R_z(\sqrt{2}\Delta t') R_z(\sqrt{2}\Delta t')} R_z(\sqrt{2}\Delta t') R_z(\pi/4) R_z(\sqrt{2}\Delta t') R_z(\pi/4) R_z(\pi/4)$$

FIG. 6. The quantum circuit of the time evolution operator  $\exp(-i\hat{H}_{\rm eff}\Delta t')$  given by Eq. (21).

The encoder  $\hat{U}_{enc}$  then transforms  $\hat{H}_3$  to a two-qubit effective Hamiltonian  $\hat{H}_{eff}$ ,

$$\hat{H}_{\text{eff}} = \hat{U}_{\text{enc}} \hat{H}_{3} \hat{U}_{\text{enc}}^{\dagger} = \sqrt{2} (\hat{h}^{(1)} + \hat{h}^{(2)}) - (\hat{\sigma}_{z}^{(1)} \otimes \hat{\sigma}_{x}^{(2)} + \hat{\sigma}_{x}^{(1)} \otimes \hat{\sigma}_{z}^{(2)}).$$
(19)

where  $\hat{h}^{(i)} = (\hat{\sigma}_x^{(i)} + \hat{\sigma}_z^{(i)})/\sqrt{2}$  is the Hadamard operator. This yields the following equivalence between the time evolution operators:

$$\exp\left(-i\hat{H}_{3}\Delta t'\right) = \hat{U}_{\text{enc}}^{\dagger} \exp\left(-i\hat{H}_{\text{eff}}\Delta t'\right) \hat{U}_{\text{enc}}.$$
 (20)

This suggests that the time evolution under  $\hat{H}_3$  can be realized as the composition of the encoder  $\hat{U}_{\rm enc}$ , the time evolution under  $\hat{H}_{\rm eff}$ , and the decoding unitary  $\hat{U}_{\rm enc}^{\dagger}$ .

To design an efficient circuit implementation of  $\exp(-i\hat{H}_{eff}\Delta t')$ , we further expand  $\exp(-i\hat{H}_{eff}\Delta t')$  in the following form

$$\begin{split} \exp\left(-\mathrm{i}\hat{H}_{\mathrm{eff}}\Delta t'\right) &= \exp\left(-\mathrm{i}(\hat{h}^{(1)} + \hat{h}^{(2)})\Delta t'/\sqrt{2}\right) \\ &\times \exp\left(\mathrm{i}(\hat{\sigma}_{z}^{(1)} \otimes \hat{\sigma}_{x}^{(2)} + \hat{\sigma}_{x}^{(1)} \otimes \hat{\sigma}_{z}^{(2)})\Delta t'\right) \\ &\times \exp\left(-\mathrm{i}(\hat{h}^{(1)} + \hat{h}^{(2)})\Delta t'/\sqrt{2}\right) \\ &+ \mathscr{O}(m^{-3}), \end{split} \tag{21}$$

where the third order error  $\mathcal{O}(m^{-3})$  is with a higher than that of the conventional Trotter decomposition, derived from the known decomposition

$$\exp\left(\frac{\hat{X}+\hat{Y}}{m}\right) = \exp\left(\frac{\hat{X}}{2m}\right) \exp\left(\frac{\hat{Y}}{m}\right) \exp\left(\frac{\hat{X}}{2m}\right) + \mathcal{O}(m^{-3}). \tag{22}$$

![](_page_3_Picture_18.jpeg)

FIG. 7. The quantum circuit of the single Trotter block for the 9-site system, denoting  $\Delta t'$  time evolution. The two-qubit unitary gate  $\hat{u}$  stays the same as the conventional one shwon in Fig. 2. The red dashed rectangles denote the pair of CNOT gates offsetting with each other. The areas of each Trotter gate  $\exp\left(-i\hat{A}_k\Delta t'\right)$  and  $\exp\left(-i\hat{B}_k\Delta t'\right)$  are separated by the dash-dot lines and highlighted by the characters at the bottom of the figure.

Thus, the proposed construction does not crucially affect on the numerical error for the time propagation by applying sufficient number of Trotter iterations m. This provides a quantum circuit of the time evolution  $\exp\left(-i\hat{H}_{\rm eff}\Delta t'\right)$ , represented in Fig. 6. The number of required CNOT gates amounts up to eight for implementing  $\exp\left(-i\hat{H}_{\rm eff}\Delta t'\right)$  as a quantum circuit.

Using the circuit implementation of  $\exp(-i\hat{A}_k\Delta t')$  and  $\exp(-i\hat{B}_k\Delta t')$ , the whole quantum circuit of the proposed Trotter block for  $\Delta t'$  in Eq. (13) is then described by Fig. 7. The single Trotter block requires  $8 \times 4 = 32$  CNOT gates per four qubits. Moreover, by considering the offsets between the two CNOT gates in the red-dashed rectangles in Fig.7, we can finally reduce CNOT gates to 28 in each four-qubit Trotter block. Thus, our circuit construction consumes on average seven CNOT gates per qubit in a single Trotter block with evolution time  $2\Delta t'$ . Moreover, taking the ratio between  $\Delta t$ and  $\Delta t'$  into account, our circuit construction requires only 7m = 1.75n CNOT gates to perform  $t = n\Delta t$  time evolution for. Since the conventional Trotter circuit requires an average of 3n CNOT gates per qubit up to time t, yielding a reduction rate of 1.75n/3n = 0.583 compared to the original Trotter blocks. This reduction of CNOT gates significantly contributes to the noise resilience of our proposed Trotter decomposition.

# IV. EXPERIMENTS

To demonstrate the practicality of the proposed Trotter decomposition, we simulate the time evolution of the XXX Heisenberg model and calculate the fidelity  $F(\tilde{\rho}, \rho_{\text{ideal}}) =$ 

Tr 
$$\left[\left(\rho_{\text{ideal}}^{1/2}\tilde{\rho}\rho_{\text{ideal}}^{1/2}\right)^{1/2}\right]^2$$
 of the resulting state  $\tilde{\rho}$  to the ideally evolved state  $\rho_{\text{ideal}}$ .

We also compare the process fidelity to the accurate time evolution from t=0 to  $t=\pi$  between the conventional Trotter unitary operation and the proposed Trotter unitary operation. Note that the process fidelity  $^{28}$  is defined as the state fidelity

![](_page_4_Figure_2.jpeg)

![](_page_4_Figure_3.jpeg)

FIG. 8. The process infidelity to the theoretically predicted time evolution without noise. Plots of the conventional Trotter decomposition (Fig. 2) are colored red and those of the proposed decomposition (Fig. 7) are colored blue. (a) The process infidelity of the evolved state to the ideally evolved state without noise, scaling with the number of Trotter iterations. The x-axis k denotes the k-th iteration of  $n \in \{40,60,80,\ldots,400\}$  for the conventional method and  $m \in \{20,30,40,\ldots,200\}$  for the proposed method to make the time intervals  $\Delta t$  and  $\Delta t'$  consistent between each method, i.e.  $\Delta t = \Delta t'$ . (b) The process infidelity of the evolved state to the ideally evolved state without noise, scaling with the number of CNOT gates.

between Choi matrices of the two completely positive tracepreserving (CPTP) maps of interest. In the following experiments, we use the noisy and noise-free density matrix simulator, real-device emulator fake\_jakarta, and real quantum device ibmq\_jakarta provided by IBM Quantum Platform.

### A. Noise-free process fidelity

We first examine the advantage in the convergence rate of approximation error of the proposed Trotter decompositions over the conventional one without the initial state dependency. To see this, we compare the process fidelity of the conventional and of the proposed approaches to the theoretically predicted time evolution without noise. Here, we use nine-site XXX Heisenberg model up to a fixed evolution time  $t = \pi$ . For the conventional Trotter circuit (Fig. 2) we perform 19 different Trotter iterations among  $n \in \{40, 60, 80, \dots, 400\}$ , and for the proposed Trotter circuit (Fig. 7), among  $m \in \{20, 30, 40, \dots, 200\}$ .

The results are shown in Fig. 8, where we plot the process *infidelity* of the conventional method and the proposed method. Figure 8(a) compares the process infidelity with different Trotter iterations where both methods use the same time intervals  $\Delta t = \Delta t'$ . Figure 8(b) compares the process infidelity on the same basis of the number of the total CNOT gates in the Trotter circuit. We observe that the process infidelity of the proposed method seems to be halved from that of the conventional one in Fig. 8(a), which is consistent with theoretical prediction under the setup of  $\Delta t = \Delta t'$  and m = n/2. Besides, Fig. 8(b) implies that the proposed method is more

noise-robust in the sense that it uses fewer CNOT gates which are considered to be the main source of noise on the current quantum hardware.

#### B. State fidelity under depolarizing noise

We next perform the noisy numerical simulation of the nine-site XXX Heisenberg model up to a fixed evolution time  $t = \pi$ .

We introduce depolarizing noise in both single-qubit gates and two-qubit gates with depolarizing probabilities  $p_1 = 1.0 \times 10^{-6}$  and  $p_2 = 10p_1 = 1.0 \times 10^{-5}$ , respectively, which reflect the noise levels of the current and near-future quantum hardware<sup>29,30</sup>. Starting from the Néel state  $|101010101\rangle$ , we compare the state fidelity between the conventional approach for 25 different Trotter iterations among  $n \in \{4, 12, 20, ..., 196\}$  and the proposed approach for 25 different Trotter iterations among  $m \in \{2, 6, 10, ..., 98\}$ .

The simulated results between the conventional Trotter decomposition and the proposed decomposition are plotted in Fig. 9. We observe that there exists an optimal number of Trotter iterations that balances the simulation accuracy and the noise effect induced when increasing the Trotter iterations. From Fig. 9(a), we see that the optimal state infidelity by the proposed method achieves lower state infidelity than the conventional approach.

Note that the cross of the plots between the conventional method and the proposed method when k = 12 in Fig. 9(a) results from the condition to make  $\Delta t = \Delta t'$  in the x-axis, where the extent of the residual error by the proposed method is de-

![](_page_5_Figure_2.jpeg)

![](_page_5_Figure_3.jpeg)

FIG. 9. The state infidelity of noisy time evolution starting from the Néel state  $|1010101010\rangle$  to the ideally evolved state. Plots of the conventional Trotter decomposition (Fig. 2) are colored red and those of the proposed decomposition (Fig. 7) are colored blue. (a) The state infidelity of the evolved state under the depolarizing noise with  $p_1 = 1.0 \times 10^{-6}$  to the ideally evolved state, scaling with the number of Trotter iterations. The x-axis k denotes the k-th iteration of  $n \in \{4, 12, 20, \dots, 196\}$  for the conventional method and  $m \in \{2, 6, 10, \dots, 98\}$  for the proposed method to make the time intervals  $\Delta t$  and  $\Delta t'$  consistent between each method, i.e.  $\Delta t = \Delta t'$ . (b) The state infidelity of the evolved state under the depolarizing noise with  $p_1 = 1.0 \times 10^{-6}$  to the ideally evolved state, scaling with the number of CNOT gates.

![](_page_5_Figure_5.jpeg)

FIG. 10. The minimum state infidelity of the evolved state under the noise with the conventional and proposed approaches to the ideally evolved state without noise, scaling with different depolarizing probabilities  $p_1 \in \{1.0 \times 10^{-7}, 3.0 \times 10^{-7}, 1.0 \times 10^{-6}, 3.0 \times 10^{-6}, 1.0 \times 10^{-5}\}$  and  $p_2 = 10p_1$ .

signed to be the half of the residual error by the conventional method. This means that the proposed method uses correspondingly deeper circuits with more CNOT gates to achieve such a better residual error. Under the noisy execution, this appears as the cross of the plots. When adjusting the x-axis relative to the number of CNOT gates in Fig. 9(b), we then see that the performance of the proposed method is better than the conventional one for larger Trotter iterations. This im-

plies that our proposed decomposition is more noise-robust to achieve a higher state infidelity under the noisy execution. We here also remark that the conventional method outperforms the proposed method for smaller Trotter iterations, which can be explained by insufficient precision to approximate  $\exp\left(-i\hat{H}_{\rm eff}\Delta t'\right)$  in Eq. (21).

Focusing on the infidelity with the optimal number of Trotter iterations when simulating time evolution starting from the Néel state, Fig. 10 visualizes the advantage of our proposed method over the conventional method in terms of lower infidelity under different noise levels ranging among  $p_1 \in \{1.0 \times 10^{-7}, 3.0 \times 10^{-7}, 1.0 \times 10^{-6}, 3.0 \times 10^{-6}, 1.0 \times 10^{-5}\}$  and  $p_2 = 10p_1$ . Note that the latest quantum devices have already reach the regime where the single-qubit and two-qubit gate error probability take  $10^{-5}$  and  $10^{-4}$ , respectively<sup>29,30</sup>. Observing from Fig. 10, the advantage of the proposed method becomes clearer when the error rates become smaller. This means that our approach would further outperform the conventional approach in the near-future quantum devices with smaller noise levels.

#### C. Real-device experiments with error suppression

In implementing the proposed Trotter decomposition on real quantum hardware <code>ibmq\_jakarta</code> and its noise-calibrated simulator <code>fake\_jakarta</code>, we simulate the time evolution of the three-site XXX Heisenberg model from t=0 to  $t=\pi$ . This real device experiments with N=3 corresponds to using only the propagator  $\exp\left(-\mathrm{i}\hat{A}_1\Delta t'\right)$  in Eq. (14), which can be seen as the simplest case of the proposed method.

![](_page_6_Figure_2.jpeg)

FIG. 11. (a) The state infidelity of the evolved state to the expected noise-free state, simulated by the two encoding-decoding strategies among different Trotter iterations m. (b) The state infidelity of the evolved state to the expected noise-free state, for different QEM levels among different Trotter iterations m.

![](_page_6_Figure_4.jpeg)

FIG. 12. The error map of ibmq\_jakarta on April 16, 2022. The numbers on the figure represent the indices of physical qubits. We use the physical qubits 5, 3, and 1 with the virtual qubit indices 0, 1, and 2 on quantum circuits. The device noise is subject to temporal fluctuations.

Since ibmq\_jakarta has constrained qubit connectivity shown in Fig. 12, we further reduce the circuit depth and the number of CNOT gates by adopting the "shallow" encoding and "specific" decoding methods, in which the encoding and decoding processes are simplified regarding the subspace that the chosen initial state belongs to. For example, the encoding operation  $\hat{U}_{enc}$  transforms the initial state  $|110\rangle$  into  $|010\rangle$ , which can be equivalently realized by applying  $\hat{\sigma}_x^{(1)} \otimes \hat{\mathbf{1}}^{(2)} \otimes \hat{\mathbf{1}}^{(3)}$  to the initial state  $|110\rangle$ . Besides, given an initial state within the subspace of P=1, which is the case

for  $|110\rangle$ , the evolved state at any evolution time t would ideally stay in the same subspace. This allows us to further reduce the CNOT operations in the decoding process: acting CNOT(2 $\rightarrow$ 1) and CNOT(3 $\rightarrow$ 2) on the obtained final state sequentially. This optimized encoding-decoding process makes the proposed decomposition more compatible with near-term superconducting devices, without changing the targeted physical evolution.

Based on the above, we compute the infidelity of the resulting state at the evolution time  $t=\pi$  evolved from a given initial state  $|110\rangle$  at t=0. We add quantum error mitigation  $(\text{QEM})^{15-22}$  to reduce the noise effect through classical post-processing. Particularly, we use quantum readout error mitigation  $(\text{QREM})^{19}$  and zero-noise extrapolation  $(\text{ZNE})^{16,18}$ . We use the digital ZNE method  $^{18}$  with the linear fitting method and the scale factors 1.0, 2.0 and 3.0, provided by Mitiq $^{31}$ . Furthermore, the Pauli twirling technique $^{32-34}$  is also combined with ZNE, referring to the implementation by Berthusen et al. $^{35}$ . Each quantum circuit is executed with 8192 shots, and the infidelity is averaged over 8 samples.

First, we examine the performance among Trotter iterations  $\{4,5,6,7,8,9,10,20,30,40\}$  on the noisy simulator fake\_jakarta, comparing the two encoding-decoding methodologies: the general encoder  $\hat{U}_{enc}$  and general decoder  $\hat{U}_{enc}^{\dagger}$  (general-general), and the aforementioned shallow encoding and specific encoding (shallow-specific). Here, we apply only QREM to noisy results before computing the infidelity. The result is shown in Fig. 11(a), where both encoding-decoding methods achieve the infidelity below 0.2 with more than 10 Trotter iterations and the shallow-specific method further achieves the infidelity smaller than 0.1.

The effect of QEM methods is also investigated under fake\_jakarta. Here, we set the configuration to shallow encoding and specific decoding. We observe from Fig. 11(b)

that both QREM and ZNE contribute to reducing the infidelity. The instability of ZNE can be improved by adding Pauli twirling that tailors the noise to a stochastic Pauli channel. We also see that combining Pauli twirling further enhances the accuracy gains achieved by finer Trotter decomposition.

| Settings            | fake_jakarta        | ibmq_jakarta        |
|---------------------|---------------------|---------------------|
| General-general     |                     |                     |
| Without QEM         | $0.7856 \pm 0.0015$ | $0.8039 \pm 0.0048$ |
| QREM                | $0.8448 \pm 0.0015$ | $0.9032 \pm 0.0054$ |
| QREM, ZNE           | $0.9393 \pm 0.0053$ | $0.9866 \pm 0.0017$ |
| QREM, ZNE, Twirling | $0.9801 \pm 0.0031$ | -                   |
| Shallow-specific    |                     |                     |
| Without QEM         | $0.8631 \pm 0.0017$ | $0.8637 \pm 0.0041$ |
| QREM                | $0.9234 \pm 0.0016$ | $0.9728 \pm 0.0040$ |
| QREM, ZNE           | $0.9840 \pm 0.0024$ | $0.9857 \pm 0.0043$ |
| QREM, ZNE, Twirling | $0.9714 \pm 0.0048$ | $0.9624 \pm 0.0167$ |

TABLE I. The fidelity of the simulated state from IBM Quantum Jakarta and its fake simulator under different QREM levels and encoding-decoding strategies. "General-general" represents the use of the general encoder and the general decoder, and "Shallow-specific" represents the use of the shallow encoder and the specific decoder.

Finally, we examine the time evolution from t=0 to  $t=\pi$  on the real quantum device ibmq\_jakarta. We execute 100 Trotter iterations with and without QEM under the two encoding-decoding methods. The state fidelity is then calculated by reconstructing the density matrix through state tomography  $^{36-38}$ .

The results are listed in Table I, where the fidelities obtained by fake\_jakarta and ibmq\_jakarta are compared. All the fidelities exceed 0.80 on ibmq\_jakarta, and all the fidelities even exceed 0.90 with QREM only. Remarkably, we achieve a fidelity over 0.98 with ZNE with the general-general method, which ensures the generality of our method in simulating the dynamics from an arbitrary initial state. All the experimental results on the noisy simulator and the real device support the practicality of our proposed Trotter decomposition.

# V. CONCLUSION

In this work, we propose a novel, noise-resilient Trotter decomposition focusing on the symmetry of the given Heisenberg Hamiltonian to notably reduce the number of CNOT gates in its circuit implementation without sacrificing the accuracy of the Trotter decomposition. The noise-robustness of the proposed method is demonstrated through the numerical simulation under noise. Our experiments also record high fidelities in simulating the three-site Heisenberg model on the real quantum device. The proposed method thus establishes a direct link between physical insight into the model's symmetry and quantum circuit design regarding efficient Trotter decomposition, offering both a fresh theoretical perspective and practical benefits for performing noise-resilient quantum dynamics simulation.

This work opens up several promising directions. First, owing to the generality of the proposed approach, it can be extended to a broader class of physical and chemical models. In particular, our framework applies to models that share the same underlying symmetric structure as the Heisenberg model after an equivalent mapping, such as the Jordan-Wigner transformation<sup>39,40</sup>, which maps fermionic creation and annihilation operators to Pauli operators. Through such transformations, electronic quantum states would be able be simulated within our present framework. A systematic characterization of the classes of physical systems that can be equivalently mapped onto this symmetric form is left as a significant direction for future work.

Next, integrating more recent QEM techniques based on ZNE<sup>41,42</sup> would further suppress both coherent and algorithmic errors in Trotterized circuits. Moreover, resource-efficient implementations using subspace expansion methods<sup>20,43</sup> can also be adapted to our framework to mitigate both coherent and stochastic errors. In combination with quantum–classical divide-and-conquer approaches<sup>44–47</sup>, these techniques would further enhance the practical feasibility of our method on near-term quantum devices.

#### **ACKNOWLEDGMENTS**

The result of real-device experiments is obtained as a solution to the IBM Quantum Awards: Open Science Prize 2021, for which the initial manuscript has been publicly available at<sup>48</sup> since April 2022. B.Y. and N.N. sincerely thank all those who made this contest possible.

# **AUTHOR DECLARATIONS**

#### Conflict of Interest

The authors have no conflicts to disclose.

#### **Author Contributions**

**Bo Yang:** Conceptualization (equal); Data curation (lead); Formal analysis (supporting); Funding acquisition (equal); Investigation (lead); Methodology (supporting); Project administration (equal); Resources (equal); Software (lead); Supervision (equal); Validation (equal); Visualization (equal); Writing - original draft (equal); Writing - review & editing (equal).

Naoki Negishi: Conceptualization (equal); Data curation (supporting); Formal analysis (lead); Funding acquisition (equal); Investigation (supporting); Methodology (lead); Project administration (equal); Resources (equal); Software (supporting); Supervision (equal); Validation (equal); Visualization (equal); Writing - original draft (equal); Writing - review & editing (equal).

#### DATA AVAILABILITY STATEMENT

The code and data used in the experiments in this work are publicly available on the GitHub page: https://github.com/BOBO1997/osp\_solutions<sup>48</sup>.

- <sup>1</sup>O. Lanes, M. Beji, A. D. Corcoles, C. Dalyac, J. M. Gambetta, L. Henriet, A. Javadi-Abhari, A. Kandala, A. Mezzacapo, C. Porter, S. Sheldon, J. Watrous, C. Zoufal, A. Dauphin, and B. Peropadre, "A framework for quantum advantage," (2025).
- <sup>2</sup>H.-Y. Huang, S. Choi, J. R. McClean, and J. Preskill, "The vast world of quantum advantage," (2025).
- <sup>3</sup>H. F. Trotter, "On the product of semi-groups of operators," Proceedings of the American Mathematical Society **10**, 545–551 (1959).
- <sup>4</sup>M. Suzuki, "Generalized trotter's formula and systematic approximants of exponential operators and inner derivations with applications to many-body problems," Communications in Mathematical Physics 51, 183–190 (1976).
- <sup>5</sup>N. Hatano and M. Suzuki, "Finding exponential product formulas of higher orders," in *Quantum Annealing and Other Optimization Methods* (Springer Berlin Heidelberg, 2005) p. 37–68.
- 6"IBM Quantum. https://quantum.cloud.ibm.com/," (2022).
- <sup>7</sup>G. J. Mooney, G. A. L. White, C. D. Hill, and L. C. L. Hollenberg, "Generation and verification of 27-qubit greenberger-horne-zeilinger states in a superconducting quantum computer," Journal of Physics Communications 5, 095004 (2021).
- <sup>8</sup>B. Yang, R. Raymond, H. Imai, H. Chang, and H. Hiraishi, "Testing scalable bell inequalities for quantum graph states on IBM quantum devices," IEEE Journal on Emerging and Selected Topics in Circuits and Systems 12, 638–647 (2022).
- <sup>9</sup>E. Lötstedt, L. Wang, R. Yoshida, Y. Zhang, and K. Yamanouchi, "Error-mitigated quantum computing of heisenberg spin chain dynamics," Physica Scripta 98, 035111 (2023).
- <sup>10</sup>T. A. Chowdhury, K. Yu, M. A. Shamim, M. L. Kabir, and R. S. Sufian, "Enhancing quantum utility: Simulating large-scale quantum spin chains on superconducting quantum computers," Physical Review Research 6 (2024), 10.1103/physrevresearch.6.033107.
- <sup>11</sup>S. Choi, T. A. Chowdhury, and K. Yu, "Quantum utility-scale error mitigation for quantum quench dynamics in heisenberg spin chains," (2025).
- <sup>12</sup>X. Yang, X. Nie, Y. Ji, T. Xin, D. Lu, and J. Li, "Improved quantum computing with higher-order trotter decomposition," Phys. Rev. A **106**, 042401 (2022).
- <sup>13</sup>H. Zhao, M. Bukov, M. Heyl, and R. Moessner, "Making trotterization adaptive and energy-self-correcting for nisq devices and beyond," PRX Quantum 4, 030319 (2023).
- <sup>14</sup>B. D. M. Jones, D. R. White, G. O. O'Brien, J. A. Clark, and E. T. Campbell, "Optimising trotter-suzuki decompositions for quantum simulation using evolutionary strategies," in *Proceedings of the Genetic and Evolutionary Computation Conference*, GECCO '19 (Association for Computing Machinery, New York, NY, USA, 2019) p. 1223–1231.
- <sup>15</sup>Y. Li and S. C. Benjamin, "Efficient variational quantum simulator incorporating active error minimization," Phys. Rev. X 7, 021050 (2017).
- <sup>16</sup>K. Temme, S. Bravyi, and J. M. Gambetta, "Error mitigation for short-depth quantum circuits," Phys. Rev. Lett. 119, 180509 (2017).
- <sup>17</sup>S. Endo, S. C. Benjamin, and Y. Li, "Practical quantum error mitigation for near-future applications," Phys. Rev. X 8, 031027 (2018).
- <sup>18</sup>T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, and W. J. Zeng, "Digital zero noise extrapolation for quantum error mitigation," in 2020 IEEE International Conference on Quantum Computing and Engineering (QCE) (IEEE, 2020).
- <sup>19</sup>B. Yang, R. Raymond, and S. Uno, "Efficient quantum readout-error mitigation for sparse measurement outcomes of near-term quantum devices," Phys. Rev. A 106, 012423 (2022).
- <sup>20</sup>B. Yang, N. Yoshioka, H. Harada, S. Hakkaku, Y. Tokunaga, H. Hakoshima, K. Yamamoto, and S. Endo, "Dual-gse: Resource-efficient generalized quantum subspace expansion," (2023).
- <sup>21</sup>Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. Mc-Clean, and T. E. O'Brien, "Quantum error mitigation," Reviews of Modern Physics 95, 045005 (2023).

- <sup>22</sup>S. Endo, Z. Cai, S. C. Benjamin, and X. Yuan, "Hybrid quantum-classical algorithms and quantum error mitigation," Journal of the Physical Society of Japan 90, 032001 (2021).
- <sup>23</sup> A. Javadi-Abhari, M. Treinish, K. Krsulich, C. J. Wood, J. Lishman, J. Gacon, S. Martiel, P. D. Nation, L. S. Bishop, A. W. Cross, B. R. Johnson, and J. M. Gambetta, "Quantum computing with Qiskit," (2024), arXiv:2405.08810 [quant-ph].
- <sup>24</sup>F. Vatan and C. Williams, "Optimal quantum circuits for general two-qubit gates," Phys. Rev. A 69, 032315 (2004).
- <sup>25</sup>G. Vidal and C. M. Dawson, "Universal quantum circuit for two-qubit transformations with three controlled-not gates," Phys. Rev. A 69, 010301 (2004).
- <sup>26</sup>V. Shende, S. Bullock, and I. Markov, "Synthesis of quantum-logic circuits," IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 25, 1000–1010 (2006).
- <sup>27</sup>T. A. Chowdhury, K. Yu, M. A. Shamim, M. L. Kabir, and R. S. Sufian, "Enhancing quantum utility: Simulating large-scale quantum spin chains on superconducting quantum computers," Phys. Rev. Res. 6, 033107 (2024).
- <sup>28</sup>M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000).
- <sup>29</sup> A. C. Hughes, R. Srinivas, C. M. Löschnauer, H. M. Knaack, R. Matt, C. J. Ballance, M. Malinowski, T. P. Harty, and R. T. Sutherland, "Trappedion two-qubit gates with >99.99% fidelity without ground-state cooling," (2025).
- <sup>30</sup>A. Ransford, M. S. Allman, J. Arkinstall, J. P. Campora, S. F. Cooper, R. D. Delaney, J. M. Dreiling, B. Estey, C. Figgatt, A. Hall, A. A. Husain, A. Isanaka, C. J. Kennedy, N. Kotibhaskar, I. S. Madjarov, K. Mayer, A. R. Milne, A. J. Park, A. P. Reed, R. Ancona, M. P. Andersen, P. Andres-Martinez, W. Angenent, L. Argueta, B. Arkin, L. Ascarrunz, W. Baker, C. Barnes, J. Bartolotta, J. Berg, R. Besand, B. Bjork, M. Blain, P. Blanchard, R. Blume-Kohout, M. Bohn, A. Borgna, D. Y. Botamanenko, R. Boutelle, N. Brown, G. T. Buckingham, N. Q. Burdick, W. C. Burton, V. Carey, C. J. Carron, J. Chambers, J. Children, V. E. Colussi, S. Crepinsek, A. Cureton, J. Davies, D. Davis, M. DeCross, D. Deen, C. Delaney, D. DelVento, B. J. DeSalvo, J. Dominy, R. Duncan, V. Eccles, A. Edgington, N. Erickson, S. Erickson, C. T. Ertsgaard, B. Evans, T. Evans, M. I. Fabrikant, A. Fischer, C. Foltz, M. Foss-Feig, D. Francois, B. Freyberg, C. Gao, R. Garay, J. Garvin, D. M. Gaudiosi, C. N. Gilbreth, J. Giles, E. Glynn, J. Graves, A. Hansen, D. Hayes, L. Heidemann, B. Higashi, T. Hilbun, J. Hines, A. Hlavaty, K. Hoffman, I. M. Hoffman, C. Holliman, I. Hooper, B. Horning, J. Hostetter, D. Hothem, J. Houlton, J. Hout, R. Hutson, R. T. Jacobs, T. Jacobs, M. Johannsen, J. Johansen, L. Jones, S. Julian, R. Jung, A. Keay, T. Klein, M. Koch, R. Kondo, C. Kong, A. Kosto, A. Lawrence, D. Liefer, M. Lollie, D. Lucchetti, N. K. Lysne, C. Lytle, C. MacPherson, A. Malm, S. Mather, B. Mathewson, D. Maxwell, L. Mc-Caffrey, H. McDougall, R. Mendoza, M. Mills, R. Morrison, L. Narmour, N. Nguyen, L. Nugent, S. Olson, D. Ouellette, J. Parks, Z. Peters, J. Petricka, J. M. Pino, F. Polito, M. Preidl, G. Price, T. Proctor, M. Pugh, N. Ratcliff, D. Raymondson, P. Rhodes, C. Roman, C. Roy, C. Ryan-Anderson, F. B. Sanchez, G. Sangiolo, T. Sawadski, A. Schaffer, P. Schow, J. Sedlacek, H. Semenenko, P. Shevchuk, S. Shore, P. Siegfried, K. Singhal, S. Sivarajah, T. Skripka, L. Sletten, B. Spaun, R. T. Sprenkle, P. Stoufer, M. Tader, S. F. Taylor, T. H. Thompson, R. Tobey, A. Tran, T. Tran, G. Vittorini, C. Volin, J. Walker, S. White, D. Wilson, Q. Wolf, C. Wringe, K. Young, J. Zheng, K. Zuraski, C. H. Baldwin, A. Chernoguzov, J. P. Gaebler, S. J. Sanders, B. Neyenhuis, R. Stutz, and J. G. Bohnet, "Helios: A 98-qubit trapped-ion quantum computer," (2025).
- <sup>31</sup>R. LaRose, A. Mari, S. Kaiser, P. J. Karalekas, A. A. Alves, P. Czarnik, M. E. Mandouh, M. H. Gordon, Y. Hindy, A. Robertson, P. Thakre, M. Wahl, D. Samuel, R. Mistri, M. Tremblay, N. Gardner, N. T. Stemen, N. Shammah, and W. J. Zeng, "Mitiq: A software package for error mitigation on noisy quantum computers." Ouantum 6, 774 (2022).
- <sup>32</sup>C. H. Bennett, G. Brassard, S. Popescu, B. Schumacher, J. A. Smolin, and W. K. Wootters, "Purification of noisy entanglement and faithful teleportation via noisy channels," Phys. Rev. Lett. 76, 722–725 (1996).
- <sup>33</sup>E. Knill, "Fault-tolerant postselected quantum computation: Threshold analysis," (2004).
- <sup>34</sup>J. J. Wallman and J. Emerson, "Noise tailoring for scalable quantum computation via randomized compiling," Phys. Rev. A 94, 052325 (2016).

- <sup>35</sup>N. F. Berthusen, T. V. Trevisan, T. Iadecola, and P. P. Orth, "Quantum dynamics simulations beyond the coherence time on nisq hardware by variational trotter compression," (2021).
- <sup>36</sup>M. G. Raymer, M. Beck, and D. McAlister, "Complex wave-field reconstruction using phase-space tomography," Phys. Rev. Lett. **72**, 1137–1140 (1994).
- <sup>37</sup>U. Leonhardt, "Quantum-state tomography and discrete wigner function," Phys. Rev. Lett. **74**, 4101–4105 (1995).
- <sup>38</sup>D. Leibfried, D. M. Meekhof, B. E. King, C. Monroe, W. M. Itano, and D. J. Wineland, "Experimental determination of the motional quantum state of a trapped atom," Phys. Rev. Lett. 77, 4281–4285 (1996).
- <sup>39</sup>G. Ortiz, J. Gubernatis, E. Knill, and R. Laflamme, "Simulating fermions on a quantum computer," Computer Physics Communications **146**, 302– 316 (2002), quantum Computing for Physical Modeling.
- <sup>40</sup>R. Somma, G. Ortiz, J. E. Gubernatis, E. Knill, and R. Laflamme, "Simulating physical phenomena by quantum networks," Phys. Rev. A 65, 042323 (2002).

- <sup>41</sup>S. Endo, Q. Zhao, Y. Li, S. Benjamin, and X. Yuan, "Mitigating algorithmic errors in a hamiltonian simulation," Phys. Rev. A 99, 012334 (2019).
- <sup>42</sup>S. Hakkaku, Y. Suzuki, Y. Tokunaga, and S. Endo, "Data-efficient error mitigation for physical and algorithmic errors in a hamiltonian simulation," (2025).
- <sup>43</sup>N. Yoshioka, H. Hakoshima, Y. Matsuzaki, Y. Tokunaga, Y. Suzuki, and S. Endo, "Generalized quantum subspace expansion," Phys. Rev. Lett. 129, 020502 (2022).
- <sup>44</sup>J. Sun, S. Endo, H. Lin, P. Hayden, V. Vedral, and X. Yuan, "Perturbative quantum simulation," Phys. Rev. Lett. **129**, 120505 (2022).
- <sup>45</sup>A. Eddins, M. Motta, T. P. Gujarati, S. Bravyi, A. Mezzacapo, C. Hadfield, and S. Sheldon, "Doubling the size of quantum simulators by entanglement forging," PRX Quantum 3, 010309 (2022).
- <sup>46</sup>X. Yuan, J. Sun, J. Liu, Q. Zhao, and Y. Zhou, "Quantum simulation with hybrid tensor networks," Phys. Rev. Lett. **127**, 040501 (2021).
- <sup>47</sup>H. Harada, Y. Suzuki, B. Yang, Y. Tokunaga, and S. Endo, "Density matrix representation of hybrid tensor networks for noisy quantum devices," Quantum 9, 1823 (2025).
- <sup>48</sup>B. Yang and N. Negishi, "Solution to IBM Quantum Open Science Prize 2021," https://github.com/B0B01997/osp\_solutions (2022).