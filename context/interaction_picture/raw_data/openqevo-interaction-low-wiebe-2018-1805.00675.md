# Hamiltonian Simulation in the Interaction Picture

Guang Hao Low and Nathan Wiebe Quantum Architectures and Computation, Microsoft Research, Redmond, Washington, USA (Dated: June 7, 2019)

We present a low-space overhead simulation algorithm based on the truncated Dyson series for time-dependent quantum dynamics. This algorithm is applied to simulating time-independent Hamiltonians by transitioning to the interaction picture, where some portions are made time-dependent. This can provide a favorable complexity trade-off as the algorithm scales exponentially better with derivatives of the time-dependent component than the original Hamiltonian. We show that this leads to an exponential improvement in gate complexity for simulating some classes of diagonally dominant Hamiltonian. Additionally we show that this can reduce the gate-complexity scaling for simulating N-site Hubbard models for time t with arbitrary long-range interactions as well as reduce the cost of quantum chemistry simulations within a similar-sized plane-wave basis to  $\widetilde{\mathcal{O}}(N^2t)$  from  $\widetilde{\mathcal{O}}(N^{11/3}t)$ . We also show a quadratic improvement in query complexity for simulating sparse time-dependent Hamiltonians, which may be of independent interest.

### I. INTRODUCTION

Simulating quantum dynamics has become in recent years an an increasingly sophisticated field whose growth has been buoyed up by a host of recent successes in both general purpose simulation methods [1–12] as well as in chemistry and material simulation [13–15]. The majority of the advances that we have seen in the field have not come from identifying ways to exploit the structure of the Hamiltonian; rather, most have arisen from either better analysis of the simulation methods or from designing more efficient ways to implement the propagators. In this work, we show a method that can explicitly take advantage of structures within the Hamiltonian to further reduce the complexity of simulations.

The central intuition behind our work stems from the interaction picture. Quantum computation is often discussed in the Schrödinger picture wherein the time dynamics of the quantum state is given by

$$\partial_t |\psi(t)\rangle = -iH(t)|\psi(t)\rangle,$$
 (1)

for the general case where the Hamiltonian H(t) is time-dependent. The quantum state carries the entirety of the dynamics here. Alternatively, one can work in the Heisenberg picture where the time evolution is absorbed into the operators that are being measured.

The interaction picture can be viewed as a compromise between the Heisenberg and the Schrödinger pictures. In the interaction picture, some of the dynamics are carried by the operators and others by the state. This view allows one to focus on effects of the interaction, and is particularly fruitful in manual calculations when interactions are perturbative corrections to the free-theory. For instance, if the Hamiltonian is H = A + B then an analytic evaluation of the time-ordered propagator of the interaction picture Hamiltonian  $H_I(t) = e^{iAt}Be^{-iAt}$  is possible by perturbative expansions based on Green's functions and Feynman diagrams. Without assuming any kind of perturbative limit, this division in our case is precisely what allows us to gain an advantage for certain quantum simulation problems.

Simulation of a Hamiltonian that is time-independent in the Schrödinger picture can be much more challenging to simulate in the interaction picture. There, evolution by a time-independent Hamiltonian H is transformed in the rotating frame  $|\psi_I(t)\rangle = e^{iAt}|\psi(t)\rangle$  to evolution by a time-dependent Hamiltonian  $H_I(t) = e^{iAt}Be^{-iAt}$ . This follows from an elementary manipulation of the Schrödinger equation:

$$i\partial_t |\psi(t)\rangle = (A+B)|\psi(t)\rangle \longrightarrow i\partial_t |\psi_I(t)\rangle = e^{iAt}Be^{-iAt}|\psi_I(t)\rangle.$$
 (2)

Implementing the time-ordered propagator  $\mathcal{T}[\exp(-i\int_0^t H(s)\mathrm{d}s)]$  that solves Eq. (2) on a quantum computer requires time-dependent simulation algorithms. These are generally more complicated than time-independent algorithms, and exhibit different cost trade-offs that do not appear favorable. For instance, an order-k time-dependent Trotter-Suzuki product formula [3] has cost that scales with the rate of change of H(t) like  $\mathcal{O}(e^{\mathcal{O}(k)}(t\Lambda)^{1+1/(2k)})^1$ , where  $\Lambda = \max_s \|\dot{H}(s)\|^{1/2} \in \mathcal{O}(\|[A,B]\|^{1/2})$ . More advanced techniques based on compressed fractional queries [6] appear

<sup>&</sup>lt;sup>1</sup> The standard big- $\mathcal{O}$  notation defines  $f(n) \in \mathcal{O}(g(n))$  for positive functions f(n), g(n) > 0 as the existence of absolute constants a > 0, b > 0 such that for any n > a,  $f(n) \le bg(n)$ . We also use  $f(n) = \tilde{\mathcal{O}}(g(n))$  when  $f(n) \le bg(n)$  polylog(g(n)), and  $f(n) = \Omega(g(n))$  when  $f(n) \ge bg(n)$ , and  $f(n) = \Theta(g(n))$  when both  $f(n) \in \mathcal{O}(g(n))$  and  $f(n) = \Omega(g(n))$  are true.

to scale better like  $\sim t \|B\| \frac{\log{(\Lambda t/\epsilon)}}{\log{\log{(\Lambda t/\epsilon)}}}$  but in terms of queries to a unitary oracle that obscures the gate complexity as it expresses Hamiltonian matrix elements at different times in binary, and may be difficult to implement in practice. One proposed technique [8] directly implements a truncated Dyson series of a the time-ordered propagator and argues, though without proof, a similar scaling in terms of queries to a different type of oracle.

We show that simulation in the interaction picture can substantially improve the efficiency of time-independent simulation. In Section III, we complete the general time-dependent simulation algorithm by a truncated Dyson series proposed by [8] by providing a rigorous analysis of the approximation and explicit circuit constructions, with improvements in gate and space complexity over previously expected costs. In Section IV, we identify situations where the gate complexity of implementing these queries scale with the interaction strength  $\mathcal{O}(\|B\|)$ , and not the larger uninteresting component  $\mathcal{O}(\|A\|)$ . Such are the cases where simulation in the interaction picture is advantageous. In Section V, we showcase the potential of interaction-picture simulation by an electronic structure application in the plane-wave basis. We rigorously bound the cost of simulating the time-evolution of N spin-orbitals subject to long-range electron-electron interactions to  $\tilde{\mathcal{O}}(N^2t)$  gates, which is close to a quadratic improvement over prior art of  $\tilde{\mathcal{O}}(N^{11/3}t)$  [14]. In Section VI, we present a complexity theoretic perspective of our work by considering the abstract problem of simulating time-dependent sparse Hamiltonians in the standard query model. We obtain a quadratic improvement in sparsity scaling [6], and find optimized algorithms for simulating diagonally dominant Hamiltonians.

#### II. OUTLINE OF PAPER

A detailed summary of main results in each section follows.

## Section III - Time-dependent Hamiltonian simulation by a truncated Dyson series

We present our main algorithmic contribution: a general time-dependent simulation algorithm, described in Theorem 3 with a rigorous analysis of its performance and explicit circuit constructions, that is based on synthesizing an approximate Dyson series for general time-dependent Hamiltonians H(t) characterized by spectral-norm  $\alpha \geq \max_t \|H(t)\|$  and average rate-of-change  $\langle \|\dot{H}\| \rangle$ . Bounds on the approximation error of truncating and discretizing the Dyson series are proven in Appendix A, which is used to obtain the cost of simulating the time-ordered evolution operator. In Appendix B, this cost is determined to be  $\mathcal{O}(\alpha t \frac{\log{(\alpha t/\epsilon)}}{\log{\log{(\alpha t/\epsilon)}}})$  queries. Compared to the original proposal by [8], worked out in Appendix C, our approach has a gate complexity that scales with  $\mathcal{O}(\log{(\langle \|\dot{H}\|\rangle)})$ , instead of the worst case  $\mathcal{O}(\log{(\max_t \|\dot{H}(t)\|)})$ . The qubit overhead is also reduced by a multiplicative factor of  $\mathcal{O}(\log{(\frac{t}{\epsilon}\langle \|\dot{H}\|\rangle)})$ . The trick we use is of independent interest as it also reduces the space overhead of the time-independent truncated Taylor series algorithm [8], discussed in Appendix D for completeness.

# Section IV – Interaction picture simulation

We apply this truncated Dyson series algorithm to simulate time-evolution by a time-independent Hamiltonian H = A + B in the interaction picture. In Section IV A, we evaluate the gate complexity of constructing the query HAM-T for an interaction picture Hamiltonian  $H_I(t) = e^{iAt}Be^{-iAt}$ . This leads to a simulation, described in Theorem 7, of  $e^{-i(A+B)t}$  using

$$\mathcal{O}\left(\alpha_B t \operatorname{polylog}((\alpha_A + \alpha_B)t/\epsilon)\right) \tag{3}$$

queries to a unitary oracle  $O_B$  such that  $(\langle 0|_a \otimes \mathbb{1}_s)O_B(|0\rangle_a \otimes \mathbb{1}_s) = \frac{B}{\alpha_B}$ , queries to unitary time-evolution  $e^{iA\tau}$  by A alone for time  $\tau = \mathcal{O}(\alpha_B^{-1})$ , and additional primitive quantum gates. The parameter  $\alpha_A \geq ||A||$  is also any upper bound on the spectral norm of A. This may be compared to state-of-art Schrödinger picture simulation algorithms for time-independent Hamiltonians, which require

$$\mathcal{O}\left((\alpha_B + \alpha_A)t \operatorname{polylog}((\alpha_A + \alpha_B)t/\epsilon)\right) \tag{4}$$

queries to  $O_B$ , queries an analogous oracle for  $O_A$ , and additional primitive quantum gates. Our result Eq. (3) is then advantageous in cases where roughly  $||A|| \gg ||B||$  and the gate complexity of  $e^{iA\tau}$  is of the same order as  $O_B$ . In other words, the dominant scaling in gate complexity is the interaction strength ||B||, and not the larger uninteresting component ||A||.

### Section V – Application to the Hubbard model with long-ranged interactions

We demonstrate the advantage of Hamiltonian simulation in the interaction picture over time-independent simulation algorithms with the example of a general second-quantized Hubbard model on N lattice sites in an arbitrary number of dimensions.

The model we consider allows for arbitrary single-site disorder, in addition to arbitrary periodic translationally invariant kinetic hopping terms and long-ranged density-density interactions. Provided that the energy of the kinetic term is extensive, our interaction-picture algorithm has gate complexity  $\tilde{\mathcal{O}}\left(N^2t\right)$ . Most remarkably, the potential energy only needs to be polynomial in N, which is an extremely lax constraint. In particular, this model generalizes electronic structure simulations in the plane-wave basis [14] (which has potential energy  $\mathcal{O}(N^2)$ ), considered in Section V A. In this case, our result achieves almost a quadratic improvement over the prior art of  $\tilde{\mathcal{O}}\left(N^{11/3}t\right)$  gates. This is complementary to recent work by [16] which achieves  $\tilde{\mathcal{O}}(Nt)$  scaling, but under the much stronger assumption of short-range exponentially decaying interactions.

## Section VI – Application to sparse Hamiltonian simulation

We consider a complexity-theoretic generalization of the technology we develop for time-dependent simulation and simulation in the interaction picture. This is through the standard query model for black-box d-sparse Hamiltonian simulation, which assumes access to a unitary oracle that provides the positions and values of non-zero entries of the Hamiltonian. Each each row has at most d non-zero entries, and the maximum absolute value of any entry is  $\|H\|_{\max}$ . This information is also provided as a function of a time index for time-dependent Hamiltonians. In Section VI A, we consider this time-dependent case and describe in Theorem 9 how the time-ordered evolution operator may be simulated using  $\mathcal{O}(td\|H\|_{\max}/\epsilon)$  queries. Though linear scaling with respect to d is well-known in the time-independent case [5], this is a quadratic improvement in sparsity scaling over prior art for the time-dependent case [6]. An analogous treatment for simulating sparse time-independent Hamiltonian in the interaction picture in Section VI B, Theorem 10 has an identical query complexity, except that  $\|H\|_{\max}$  is replaced by the maximum absolute value of any off-diagonal entry. This improvement is particularly advantageous for the simulation of diagonally dominant Hamiltonians which arise in many physical systems expressed within an appropriate basis.

### III. TIME-DEPENDENT HAMILTONIAN SIMULATION BY A TRUNCATED DYSON SERIES

In the Schrödinger picture, the dynamics of a quantum state is given by  $i\partial_t |\psi(t)\rangle = H(t)|\psi(t)\rangle$  – given the initial state  $|\psi(0)\rangle$  at time t=0, the time-evolved state is  $|\psi(t)\rangle = U(t)|\psi(0)\rangle$ . If H(t) is time-independent U(t) can always be written as  $e^{-iHt}$ . In the time-dependent case the time evolution operator no longer is  $e^{-iHt}$  and indeed it does not in general have a closed-form expression. The following notation is customarily used to represent the time-evolution operator,  $U(t):|\psi(0)\rangle \mapsto |\psi(t)\rangle$ , in the case where  $H:\mathbb{R}\mapsto \mathbb{C}^{N\times N}$  is a piecewise continuous function:

$$U(t) = \lim_{r \to \infty} \prod_{j=1}^{r} e^{-iH(t(j-1)/r)t/r} := \mathcal{T}e^{-i\int_{0}^{t} H(s)ds},$$
 (5)

where  $\mathcal{T}$  is known as the time-ordering operator.

The fact that time-dependent dynamics lacks a closed form makes simulating its dynamics slightly more challenging than the time-independent case. This arises because approximations, such as Taylor series, fail to give a simple series expansion for U(t) unless [H(t), H(t')] = 0. Fortunately, there exists a more general expansion known as the Dyson series that fills the exact same role that the Taylor series fills for the time-independent case. For any t > 0 and bounded ||H(t)||, the Dyson series gives the following absolutely convergent expansion for U(t)

$$U(t) = \mathbb{1} - i \int_0^t H(t_1) dt_1 - \int_{t_2}^t \int_0^{t_2} H(t_2) H(t_1) dt_1 dt_2 + i \int_{t_2}^t \int_{t_2}^{t_3} \int_0^{t_2} H(t_3) H(t_2) H(t_1) dt_1 dt_2 dt_3 + \cdots$$
 (6)

This may be compactly represented using the time-ordering operator  $\mathcal{T}$  which sorts any sequence of k operators according to the times  $t_j$  of their evaluation, that is,  $\mathcal{T}[H(t_k)\cdots H(t_2)H(t_1)]=H(t_{\sigma(k)})\cdots H(t_{\sigma(2)})H(t_{\sigma(1)})$ , where  $\sigma$  is a permutation such that  $t_{\sigma(1)} \leq t_{\sigma(2)} \leq \cdots \leq t_{\sigma(k)}$ . For instance,  $\mathcal{T}[H(t_2)H(t_1)]=\theta(t_2-t_1)H(t_2)H(t_1)+\theta(t_1-t_2)H(t_1)H(t_2)$  using the Heaviside step function  $\theta$ . With this notation, the propagator is formally expressed as a time-ordered evolution operator  $U(t)=\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right]$  defined as

$$\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right] = \sum_{k=0}^\infty (-i)^k D_k, \quad D_k = \frac{1}{k!} \int_0^t \cdots \int_0^t \mathcal{T}\left[H(t_k)\cdots H(t_1)\right] \mathrm{d}^k t. \tag{7}$$

The aim of our work is to approximate U(t) within error  $\epsilon$  (as measured by the spectral-norm  $\|\cdot\|$  of the difference between the approximation and the true dynamics) for any  $t \geq 0$ . We achieve this by constructing the Dyson series expansion  $U(t) \approx \sum_{k=0}^{K} (-i)^k D_k$  and truncate it at finite order K to control the error. This idea was suggested earlier by [8], though without proof.

![](_page_3_Picture_1.jpeg)

FIG. 1. Quantum circuit representation of (left) an oracle HAM from Definition 1 encoding a time-independent Hamiltonian, (center) an oracle HAM-T from Definition 2 encoding a time-dependent Hamiltonian, and (right) an example implementation of HAM from with a linear-combination of unitaries from Eq. (9). Bold horizontal lines with a backslash '\' depict registers that in general comprise of multiple qubits. Vertical lines connecting boxes depict unitaries that act jointly on all registers covered by the boxes. A small square box marked by 'T' indicates control by a time index.

#### A. Input model

The cost of our algorithm is expressed in terms of unitary oracles HAM and HAM-T that encode Hamiltonians in a so-called standard-form [10, 12]. When H is time-independent, we assume access to the following oracle.

**Definition 1** (Time-independent matrix encoding). Given a matrix  $H \in \mathbb{C}^{2^{n_s} \times 2^{n_s}}$ , and a promise  $||H|| \leq \alpha$  assume there exists a unitary oracle  $HAM \in \mathbb{C}^{2^{n_a+n_s} \times 2^{n_a+n_s}}$  such that

$$HAM = \begin{pmatrix} H/\alpha & \cdot \\ \cdot & \cdot \end{pmatrix} \quad \Rightarrow \quad (\langle 0|_a \otimes \mathbb{I}_s) \, HAM(|0\rangle_a \otimes \mathbb{I}_s) = \frac{H}{\alpha}. \tag{8}$$

Use of this is justified as it generalizes a variety of different input models [10]. As an example,  $H = \sum_{j=1}^{2^{n_a}} a_j U_j$  [4] could be a linear combination of  $l = 2^{n_a}$  unitaries. Then the circuit depicted in Fig. 1 implements HAM with normalization constant  $\alpha = \sum_{j=1}^{l} a_j$  using the unitary oracles

$$HAM = (PREP^{\dagger} \otimes \mathbb{1}_{s}) \cdot SEL \cdot (PREP \otimes \mathbb{1}_{s}), \quad PREP |0\rangle_{a} = \sum_{j=1}^{l} \sqrt{\frac{a_{j}}{\alpha}} |j\rangle_{a}, \quad SEL = \sum_{j=1}^{l} |j\rangle\langle j|_{a} \otimes U_{j}.$$
 (9)

These unitaries each cost  $\mathcal{O}(l)$  gates – PREP is implemented by an a algorithm for preparing arbitrary l-dimensional quantum states [17], and SEL is implemented by binary-tree control logic [18].

A direct time-dependent generalization of Definition 1 is the unitary oracle HAM-T that encodes the Hamiltonian H(s) defined over time  $s \in [0, t]$ , with t > 0. The continuous parameter s is discretized into an integer number of M > 0 time bins which we index by  $m \in \{0, 1, \dots, M-1\}$ .

**Definition 2** (Time-dependent matrix encoding). Given a matrix  $H(s):[0,t]\to\mathbb{C}^{2^{n_s}\times 2^{n_s}}$ , integer M>0, and a promise  $\|H\|\leq \alpha$ , assume there exists a unitary oracle HAM-T  $\in \mathbb{C}^{M2^{n_a+n_s}\times M2^{n_a+n_s}}$  such that

$$\operatorname{HAM-T} = \begin{pmatrix} H/\alpha \\ \cdot \\ \cdot \end{pmatrix}, \quad H = \operatorname{Diagonal}[H(0), H(t/M), \cdots, H((M-1)t/M)],$$

$$\Rightarrow (\langle 0|_a \otimes \mathbb{1}_s) \operatorname{HAM-T}(|0\rangle_a \otimes \mathbb{1}_s) = \sum_{m=0}^{M-1} |m\rangle\langle m| \otimes \frac{H(mt/M)}{\alpha}.$$

$$(10)$$

In later sections where the time-dependent simulation algorithm is applied to the interaction picture, we 'open up' this oracle and discuss the gate complexity of its implementation. We assume that the query complexity to a controlled-unitary black-box is the same as that to the original black-box. In general, this will not affect the gate complexity. Though there are often cleverer ways to implement an arbitrary controlled-unitary, in the worst-case, all quantum gates may be replaced by their controlled versions with a constant multiplicative overhead.

## B. Truncated Dyson series algorithm

We now state our main algorithm for general time-dependent simulation.

**Theorem 3** (Hamiltonian simulation by a truncated Dyson series). Let  $H(s):[0,t]\to\mathbb{C}^{2^{n_s}\times 2^{n_s}}$ , let it be promised that  $\max_s\|H(s)\|\leq \alpha$  and  $\langle\|\dot{H}\|\rangle=\frac{1}{t}\int_0^t\left\|\frac{\mathrm{d}H(s)}{\mathrm{d}s}\right\|$  ds and assume  $M\in\mathcal{O}\left(\frac{t^2}{\epsilon}\left(\langle\|\dot{H}\|\rangle+\max_s\|H(s)\|^2\right)\right)$  in Definition 2. For all  $t\in[0,\frac{1}{2\alpha}]$  and  $\epsilon>0$ , an operation W can be implemented such that  $\left\|W-\mathcal{T}\left[e^{-i\int_0^tH(s)\mathrm{d}s}\right]\right\|\leq\epsilon$  with failure probability  $\mathcal{O}(\epsilon)$  with the following costs.

- 1. Queries to HAM-T:  $\mathcal{O}\left(\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$ ,
- 2. Qubits:  $n_s + \mathcal{O}\left(n_a + \log\left(\frac{t^2}{\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right)$ ,
- 3. Primitive gates:  $\mathcal{O}\left(\left(n_a + \log\left(\frac{t^2}{\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right) \frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$ .

The proof and circuit construction of Theorem 3 is given in Appendix B. This algorithm simulates time-evolution for short durations  $|\tau| \leq \frac{1}{2\alpha}$ , which we call a segment. Thus simulation for longer durations  $|t| > \frac{1}{2\alpha}$  require multiple segments that each query a different oracle HAM-T<sub>j</sub> encoding H(s) over a different time domain. The complexity of this multi-segment approach is as follows.

Corollary 4 (Multi-segment Hamiltonian simulation by a truncated Dyson series). Let  $H(s):[0,t]\to\mathbb{C}^{2^{n_s}\times 2^{n_s}}$ , and let it be promised that  $\max_s\|H(s)\|\leq \alpha$ , and  $\langle\|\dot{H}\|\rangle=\frac{1}{t}\int_0^t\left\|\frac{\mathrm{d}H(s)}{\mathrm{d}s}\right\|\mathrm{d}s$ . Let  $\tau=t/\lceil 2\alpha t\rceil$  and assume  $H_j(s)=H((j-1)\tau+s):s\in[0,\tau]$  is accessed by an oracle HAM-T<sub>j</sub> of the form specified in Definition 2 with  $M\in\mathcal{O}\left(\frac{t}{\alpha\epsilon}\left(\langle\|\dot{H}\|\rangle+\max_s\|H(s)\|^2\right)\right)$ . For all  $|t|\geq 0$  and  $\epsilon>0$ , an operation W can be implemented with failure probability at most  $\mathcal{O}(\epsilon)$  such that  $\left\|W-\mathcal{T}\left[e^{-i\int_0^tH(s)\mathrm{d}s}\right]\right\|\leq\epsilon$  with the following cost.

- 1. Queries to all HAM-T<sub>j</sub>:  $\mathcal{O}\left(\alpha t \frac{\log{(\alpha t/\epsilon)}}{\log{\log{(\alpha t/\epsilon)}}}\right)$
- 2. Qubits:  $n_s + \mathcal{O}\left(n_a + \log\left(\frac{t}{\alpha\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right)$
- 3. Primitive gates:  $\mathcal{O}\left(\alpha t \left(n_a + \log\left(\frac{t}{\alpha \epsilon} \left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right) \frac{\log(\alpha t/\epsilon)}{\log\log(\alpha t/\epsilon)}\right)$ .

Proof. The time-ordered evolution operator  $\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right] = \prod_{j=1}^L \mathcal{T}\left[e^{-i\int_{t_{j-1}}^{t_j} H(s)\mathrm{d}s}\right]$  may be broken into  $L = \mathcal{O}(\alpha t)$  segments, where  $[0,t] = \bigcup_{j=1}^L [t_{j-1},t_j]$  and  $0=t_0 < t_1 < \cdots < t_L = t$  and  $t_j - t_{j-1} \in \mathcal{O}(1/\alpha)$ . Each segment is then simulated using Theorem 3 to error  $\delta$ . From the proof of Theorem 3 in Appendix B, each segment is a unitary quantum circuit  $V_j$  such that the (near-unitary) operations  $W_j = (\langle 0| \otimes \mathbb{1}_s)V_j(|0\rangle \otimes \mathbb{1}_s)$  where

$$\left\| (\langle 0 | \otimes \mathbb{1}_s) V_j(|0\rangle \otimes \mathbb{1}_s) - \mathcal{T} \left[ e^{-i \int_{t_{j-1}}^{t_j} H(s) ds} \right] \right\| \le \delta.$$
 (11)

To obtain the error of applying these  $W_j$  in sequence, note that in general if  $A_j$  and  $B_j$  are a sequence of arbitrary bounded operators and  $\|\cdot\|$  is a sub-multiplicative norm then it is straightforward to show using an inductive argument and a triangle inequality that for all positive integer L,

$$\left\| \prod_{j=1}^{L} A_j - \prod_{j=1}^{L} B_j \right\| \le \sum_{k=1}^{L} \left( \prod_{j=1}^{k-1} \|A_j\| \right) \|A_k - B_k\| \left( \prod_{j=k+1}^{L} \|B_j\| \right). \tag{12}$$

Let us simply notation by setting  $A_j = W_j$  and  $B_j = \mathcal{T}[e^{-i\int_{t_{j-1}}^{t_j} H(s)ds}]$ . Using the fact that  $||W_j|| \le 1$  and  $||U_j|| = 1$ , Eq. (12) yields

$$\left\| \prod_{j}^{L} W_{j} - \mathcal{T} \left[ e^{-i \int_{0}^{t} H(s) ds} \right] \right\| \le L\delta.$$
 (13)

As  $W_j$  is obtained by applying  $V_j$  on the  $|0\rangle$  state in the ancilla register followed by a projection back onto  $\langle 0|$  state, let  $\Pi = (\mathbb{1}. - |0\rangle\langle 0|.) \otimes \mathbb{1}_s$  be this projector. Then

$$\|(\mathbb{1} - \Pi)V_j(|0\rangle \otimes \mathbb{1}_s)\| \le \sqrt{1 - (1 - \delta)^2} = \sqrt{2\delta - \delta^2} \le \sqrt{2\delta}.$$
 (14)

Thus the failure probability of projecting onto  $\langle 0 | \text{ is } \leq 2\delta$ . With L repetitions, this failure probability is  $\leq 1 - (1 - \delta)^L \in \mathcal{O}(L\delta)$ . Thus we identify  $W = W_L \cdots W_1$  and choose choose  $\delta = \epsilon/L$  to ensure that error of W and the failure probability of its application is at most  $\mathcal{O}(\epsilon)$ . The result then follows from the fact that  $L \in \Theta(\alpha t)$ .

#### C. Discretization and truncation error

Note that Theorem 3 and Corollary 4 all make a particular choice of M, which controls the number of points at which H(s) is evaluated in the oracle of Definition 2. This is determined precisely by the error incurred in truncating the Dyson series at some finite order  $k = K \ge 0$ , and evaluating  $H(t_j)$  at some finite number of M time-steps of size  $\Delta = t/M$ . Thus we have the approximation

$$\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right] \approx \sum_{k=0}^K (-i)^k D_k \approx \sum_{k=0}^\infty \frac{(-it)^k}{k!M^k} \tilde{B}_k, \quad \tilde{B}_k = \sum_{m_1, \dots, m_k=0}^{M-1} \mathcal{T}\left[H\left(m_k\Delta\right) \dots H\left(m_1\Delta\right)\right], \tag{15}$$

which converges to U(t) in the limit  $K, M \to \infty$  if H(t) is Riemann integrable. The time-ordering operator in  $\tilde{B}_k$  may be removed with a slightly different approximation

$$\tilde{B}_k = k! B_k + C_k, \quad B_k = \sum_{0 \le m_1 < \dots < m_k < M} H(m_k \Delta) \cdots H(m_1 \Delta), \tag{16}$$

where  $C_k$  captures terms where at least one pair of indices  $m_j = m_k$  collide for  $j \neq k$ . Given a target error  $\epsilon$  and failure probability  $\mathcal{O}(\epsilon)$ , the required K and M are given by the following.

**Lemma 5** (Error from truncating and discretizing the Dyson series). Let  $H(s):[0,t]\mapsto\mathbb{C}^{N\times N}$  be differentiable and  $\langle \|\dot{H}\|\rangle:=\frac{1}{t}\int_0^t \left\|\frac{\mathrm{d}H(s)}{\mathrm{d}s}\right\| \mathrm{d}s$ . For any  $\epsilon\in(0,2^{1-e}]$ , an approximation to the time ordered operator exponential of -iH(s) can be constructed such that

$$\left\| \mathcal{T}\left[ e^{-i\int_0^t H(s)\mathrm{d}s} \right] - \sum_{k=0}^K \left( -it/M \right)^k B_k \right\| \le \epsilon, \quad B_k = \sum_{0 \le m_1 < \dots < m_k < M} H\left( m_k t/M \right) \cdots H\left( m_1 t/M \right),$$

if we take all the following are true.

1.  $\max_{s} ||H(s)|| t < \ln 2$ .

2.
$$K = \left[ -1 + \frac{2\ln(2/\epsilon)}{\ln\ln(2/\epsilon) + 1} \right]$$
.

3.
$$M \ge \max \left\{ \frac{16t^2}{\epsilon} \left( \langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2 \right), K^2 \right\}$$
.

A detailed proof is presented in Appendix A. On a quantum computer, it is possible to compute the  $B_k$  exactly and efficiently even if they sum over exponentially many points M. In contrast, computing these Riemann sums on classical computer would be prohibitive, even by approximate Monte-Carlo sampling, which is exacerbated by the sign problem. However, this efficient quantum computation crucially assumes that information describing the Hamiltonian at different times are made accessible in a certain coherent manner – in our case, this is information accessed through black-box unitary oracles described by Definition 2.

### IV. INTERACTION PICTURE SIMULATION

Time-independent Hamiltonians H become time-dependent  $H_I(t)$  in the interaction picture. Simulating this requires the use of time-dependent Hamiltonian simulation algorithms, which scale with parameters of  $H_I(t)$  that differ from those for the time-independent case. For certain broad classes of Hamiltonian identified in Section IV A, these different dependencies allow us to improve the gate complexity of approximating the time-evolution operator  $e^{-iHt}$  by instead performing simulation in the interaction picture using the truncated Dyson series algorithm Theorem 3.

The interaction picture can be viewed as an intermediate between the Schrödinger and Heisenberg pictures wherein some of the dynamics is absorbed into the state and the remainder is absorbed into the dynamics of the operators. If the Hamiltonian in the Schrödinger picture H = A + B generates time-evolution like  $|\psi(t)\rangle = e^{-iHt}|\psi(0)\rangle$ , then the

Hamiltonian in the interaction picture is  $H_I(t) = e^{iAt}Be^{-iAt}$  and  $i\partial_t |\psi_I(t)\rangle = H_I(t)|\psi_I(t)\rangle$  with  $|\psi_I(t)\rangle = e^{iAt}|\psi(t)\rangle$  for all t. These relations can easily be seen by substituting into the Schrödinger equation:

$$i\partial_t |\psi_I(t)\rangle = i\partial_t \left( e^{iAt} |\psi(t)\rangle \right) = e^{iAt} (-A + H) |\psi(t)\rangle = e^{iAt} B e^{-iAt} e^{iAt} |\psi(t)\rangle$$
$$= H_I(t) |\psi_I(t)\rangle. \tag{17}$$

Note that if we started with time-dependent B(t), that is H(t) = A + B(t), the interaction picture Hamiltonian is  $H_I(t) = e^{iAt}B(t)e^{-iAt}$ . Our following results generalize easily to this situation, and so we consider time-independent B for simplicity.

The advantage of this representation is a Hamiltonian with a smaller norm  $||H_I(t)|| = ||B|| \le ||A|| + ||B||$ , but at the price of introducing time-dependence. The following notation is commonly used to express this time-evolution operator  $\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right] = \lim_{r\to\infty} \prod_{j=1}^r e^{-iH(jt/r)t/r}$  where this product is implicitly defined to be time ordered. Given an initial state  $|\psi(0)\rangle$ , the state after evolution for t>0 in the Schrödinger picture may thus be written as

$$|\psi(t)\rangle = e^{-iAt}|\psi_I(t)\rangle = e^{-iAt}\mathcal{T}\left[e^{-i\int_0^t H_I(s)ds}\right]|\psi_I(0)\rangle = e^{-iAt}\mathcal{T}\left[e^{-i\int_0^t H_I(s)ds}\right]|\psi(0)\rangle = e^{-i(A+B)t}|\psi(0)\rangle. \tag{18}$$

As this is true for any t, evolution by the full duration is identical to evolution by L shorter segments of duration  $\tau = t/L$ , such as

$$|\psi(t)\rangle = (e^{-i(A+B)\tau})^L |\psi(0)\rangle = \left(e^{-iA\tau} \mathcal{T} \left[e^{-i\int_0^\tau H_I(s)ds}\right]\right)^L |\psi(0)\rangle. \tag{19}$$

Using the simulation algorithm Theorem 3 to simulate each segment in Eq. (19) leads to the following result.

**Lemma 6** (Query complexity of Hamiltonian simulation in the interaction picture). Let  $A \in \mathbb{C}^{2^{n_s} \times 2^{n_s}}$ ,  $B \in \mathbb{C}^{2^{n_s} \times 2^{n_s}}$ , let  $\alpha_A$  and  $\alpha_B$  be known constants such that  $||A|| \leq \alpha_A$  and  $||B|| \leq \alpha_B$ . Assume the existence of a unitary oracle that implements the Hamiltonian within the interaction picture, denoted HAM-T  $\in \mathbb{C}^{2^{n_s+n_a} \times 2^{n_s+n_a}}$  which implicitly depends on the time-step size  $\tau \in \mathcal{O}(\alpha_B^{-1})$  and number of time-steps  $M \in \mathcal{O}\left(\frac{t}{\epsilon}(\alpha_A + \alpha_B)\right)$ , such that

$$(\langle 0|_a \otimes \mathcal{I}_s) \text{ HAM-T}(|0\rangle_a \otimes \mathcal{I}_s) = \sum_{m=0}^{M-1} |m\rangle\langle m| \otimes \frac{e^{iA\tau m/M} B e^{-iA\tau m/M}}{\alpha_B}, \tag{20}$$

For all  $t \geq 2\alpha_B \tau$ , the time-evolution operator  $e^{-i(A+B)t}$  may be approximated to error  $\epsilon$  with the following cost.

- 1. Simulations of  $e^{-iA\tau}$ :  $\mathcal{O}(\alpha_B t)$ .
- 2. Queries to HAM-T:  $\mathcal{O}\left(\alpha_B t \frac{\log(\alpha_B t/\epsilon)}{\log\log(\alpha_B t/\epsilon)}\right)$ ,
- 3. Qubits:  $n_s + \mathcal{O}\left(n_a + \log\left(\frac{t}{\epsilon}\left(\alpha_A + \alpha_B\right)\right)\right)$ ,
- 4. Primitive gates:  $\mathcal{O}\left(\alpha_B t \left(n_a + \log\left(\frac{t}{\epsilon}\left(\alpha_A + \alpha_B\right)\right)\right) \frac{\log\left(\alpha_B t/\epsilon\right)}{\log\log\left(\alpha_B t/\epsilon\right)}\right)$ .

Proof. According to Corollary 4, the maximum time duration of simulation  $\tau$  in each segment of Eq. (19) is limited to  $\tau \in \mathcal{O}(\alpha_B^{-1})$ . Thus there are  $L \in \mathcal{O}(\alpha_B t)$  segments. Each segment also requires one application of  $e^{-iA\tau}$ , thus the query complexity to  $e^{-iA\tau}$  is L. Note that for all  $t \leq \frac{1}{2\alpha_B}$ , only one application of  $e^{-iAt}$  is required. Each segment also requires one application of  $\mathcal{T}\left[e^{-i\int_0^\tau H_I(s)\mathrm{d}s}\right]$ , which we approximate with TDS from Theorem 3. By a triangle inequality, it suffices to simulate each segment with error  $\delta = \mathcal{O}(\epsilon/L)$  in order to obtain a total error  $\epsilon$ . Simulating each segment makes  $\mathcal{O}\left(\frac{\log{(\alpha_B t/\epsilon)}}{\log{\log{(\alpha_B t/\epsilon)}}}\right)$  queries to HAM-T. Thus simulation for the full duration makes  $\mathcal{O}\left(\alpha_B t \frac{\log{(\alpha_B t/\epsilon)}}{\log{\log{(\alpha_B t/\epsilon)}}}\right)$  queries to HAM-T.

The number of qubits, primitive gates, and discretization points M required are obtained directly from the conditions of Corollary 4. We obtain the stated M by substituting the facts  $\max_s ||H_I(s)|| \le ||B||$ ,  $\langle ||\dot{H}|| \rangle = ||[A, B]|| \le 2||A||||B||$ , and  $\tau \in \mathcal{O}(\alpha_B^{-1})$ . Thus it suffices to choose

$$M \in \mathcal{O}\left(\frac{\alpha_B t \tau^2}{\epsilon} \left( \langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2 \right) \right) \subseteq \mathcal{O}\left(\frac{t}{\epsilon} \left(\frac{\|A\| \|B\|}{\alpha_B} + \alpha_B\right)\right) \subseteq \mathcal{O}\left(\frac{t}{\epsilon} \left(\alpha_A + \alpha_B\right)\right). \tag{21}$$

## A. Comparison with simulation of time-independent Hamiltonians in the Schrödinger picture

We now compare the cost of simulation in the interaction picture using the truncated Dyson series, with state-of-art simulation in the Schrödinger picture with time-independent Hamiltonians using the truncated Taylor series approach [8] outlined in Appendix D. Up to logarithmic factors, this comparison is valid as the truncated Taylor series algorithm cost differs from optimal algorithms [10, 11] by only logarithmic factors. For any Hamiltonian H = A + B, let us assume access to the oracles

$$(\langle 0|_a \otimes \mathbb{1}_s) O_A(|0\rangle_a \otimes \mathbb{1}_s) = \frac{A}{\alpha_A}, \quad (\langle 0|_a \otimes \mathbb{1}_s) O_B(|0\rangle_a \otimes \mathbb{1}_s) = \frac{B}{\alpha_B}, \tag{22}$$

which have gate complexity  $C_A, C_B$  respectively, and encode A, B using  $n_a$  additional qubits. Note that in every case where  $O_A$  and  $O_B$  act non-trivially on  $|0\rangle_a$ , the cost  $C_A, C_B \geq n_a$ . The gate complexity of time-independent simulation  $e^{-i(A+B)t}$  by prior art is then

$$C_{\text{TTS}} \in \mathcal{O}\left( (C_A + C_B)(\alpha_A + \alpha_B) t \frac{\log\left((\alpha_A + \alpha_B)t/\epsilon\right)}{\log\log\left((\alpha_A + \alpha_B)t/\epsilon\right)} \right) \tag{23}$$

In contrast, we prove the following theorem for simulation in the interaction picture.

**Theorem 7** (Gate complexity of Hamiltonian simulation in the interaction picture). Let  $A \in \mathbb{C}^{2^{n_s} \times 2^{n_s}}$ ,  $B \in \mathbb{C}^{2^{n_s} \times 2^{n_s}}$  be time-independent Hamiltonians that are promised to obey  $||A|| \leq \alpha_B$ , such that

- 1. B is encoded in an oracle  $(\langle 0|_a \otimes \mathbb{1}_s)O_B(|0\rangle_a \otimes \mathbb{1}_s) = \frac{B}{\alpha_B}$  using  $n_a$  additional qubits and  $C_B \geq n_a$  gates.
- 2.  $e^{-iAs}$  is approximated to error  $\epsilon$  using  $C_{e^{-iAs}}[\epsilon] \in \mathcal{O}\left(|s|\log^{\gamma}(s/\epsilon)\right)$  gates for some  $\gamma > 0$  and any  $|s| \geq 0$ .

For all t>0, the time-evolution operator  $e^{-i(A+B)t}$  may be approximated to error  $\epsilon$  with gate complexity

$$C_{TDS} \in \mathcal{O}\left(\alpha_B t \left(C_B + C_{e^{-iA/\alpha_B}} \left[\frac{\epsilon}{\alpha_B t \log(\alpha_B)}\right] \log\left(\frac{t(\alpha_A + \alpha_B)}{\epsilon}\right)\right) \frac{\log(\alpha_B t/\epsilon)}{\log\log(\alpha_B t/\epsilon)}\right)$$

$$= \mathcal{O}\left(\alpha_B t \left(C_B + C_{e^{-iA/\alpha_B}} \left[\epsilon\right]\right) \operatorname{polylog}(t(\alpha_A + \alpha_B)/\epsilon)\right). \tag{24}$$

*Proof.* Expressing Lemma 6 solely in terms of gate complexity requires an expression  $C_{\text{HAM-T}}[\delta]$  for the cost of approximating the oracle HAM-T to error  $\delta$ . One possible construction is

$$\text{HAM-T} = \left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{iA\tau m/M}\right) \cdot \left(\mathbb{1}_d \otimes O_B\right) \cdot \left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{-iA\tau m/M}\right), \quad \tau \in \mathcal{O}(\alpha_B^{-1}). \quad (25)$$

Note that the controlled-Hamiltonian evolution operator  $\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes e^{iA\tau m/M}$  may be implemented by  $\lceil \log_2{(M)} \rceil$  controlled- $e^{iA\tau/M}$ ,  $e^{iA2\tau/M}$ ,  $e^{iA4\tau/M}$ ,  $\cdots$ ,  $e^{iA2^{\lceil \log_2{(M)} \rceil}\tau/M}$ . By approximating each controlled- $e^{iAj\tau/M}$  with error  $\mathcal{O}(\delta/\log{(M)})$ , the overall error will be bounded by  $\mathcal{O}(\delta)$ . As we assume that  $C_{e^{-iAt}}[\delta/\log{(M)}] \in \mathcal{O}(|t|\log^{\gamma}{(t\log{(M)/\delta)}})$ , each controlled- $e^{iAj\tau/M}$  costs at most  $\mathcal{O}(\tau\log^{\gamma}{(\tau\log{(M)/\delta)}})$  gates. Thus the cost of all controlled- $e^{iAj\tau/M}$  sums to  $\mathcal{O}(\tau\log{(M)/\delta}) = \mathcal{O}(\tau\log{(M)/\delta}) = \mathcal{O}(\tau\log{(M)/\delta})$ . By adding the cost of  $O_B$ ,

$$C_{\text{HAM-T}}[\delta] \in \mathcal{O}\left(C_B + \tau \log\left(M\right) \log^{\gamma}\left(\tau/\delta\right)\right) = \mathcal{O}\left(C_B + \frac{1}{\alpha_B} \log\left(M\right) \log^{\gamma}\left(\frac{1}{\alpha_B \delta}\right)\right). \tag{26}$$

From Lemma 6, approximating  $e^{-iHt}$  to error  $\mathcal{O}(\epsilon)$  requires  $\mathcal{O}\left(\alpha_B t \frac{\log{(\alpha_B t/\epsilon)}}{\log{\log{(\alpha_B t/\epsilon)}}}\right)$  queries to HAM-T. We obtain this overall error by approximating each HAM-T query with error  $\delta \in \mathcal{O}\left(\epsilon \frac{\log{\log{(\alpha_B t/\epsilon)}}}{\alpha_B t \log{(\alpha_B t/\epsilon)}}\right)$ . Thus

$$C_{\text{HAM-T}}[\delta] \in \mathcal{O}\left(C_B + \frac{1}{\alpha_B}\log\left(M\right)\log^{\gamma}\left(\frac{1}{\epsilon}\frac{t\log\left(\alpha_B t/\epsilon\right)}{\log\log\left(\alpha_B t/\epsilon\right)}\right)\right) = \mathcal{O}\left(C_B + \frac{1}{\alpha_B}\log\left(M\right)\log^{\gamma}\left(\frac{t\log\left(\alpha_B\right)}{\epsilon}\right)\right). \tag{27}$$

From Lemma 6, we also require  $\mathcal{O}(\alpha_B t)$  queries to  $e^{-iA\tau}$ , and  $\mathcal{O}\left((n_a + \log{(M)})\alpha_B t \frac{\log{(\alpha_B t/\epsilon)}}{\log{\log{(\alpha_B t/\epsilon)}}}\right)$  primitive gates. It suffices to approximate each  $e^{-iA\tau}$  to error  $\mathcal{O}(\epsilon/(\alpha_B t))$ . By adding all these contributions, the total gate complexity

of simulation in the interaction picture is

$$\mathcal{O}\left(\alpha_{B}t\left(\left(C_{\text{HAM-T}}[\delta] + \left(n_{a} + \log\left(M\right)\right)\right) \frac{\log\left(\alpha_{B}t/\epsilon\right)}{\log\log\left(\alpha_{B}t/\epsilon\right)} + C_{e^{-iA\tau}}[\epsilon/(\alpha_{B}t)]\right)\right) \\
= \mathcal{O}\left(\alpha_{B}t\left(\left(C_{B} + \frac{1}{\alpha_{B}}\log\left(M\right)\log^{\gamma}\left(\frac{t\log\left(\alpha_{B}\right)}{\epsilon}\right) + \left(n_{a} + \log\left(M\right)\right)\right) \frac{\log\left(\alpha_{B}t/\epsilon\right)}{\log\log\left(\alpha_{B}t/\epsilon\right)} + \frac{1}{\alpha_{B}}\log^{\gamma}\left(\frac{t}{\epsilon}\right)\right)\right) \\
= \mathcal{O}\left(\alpha_{B}t\left(C_{B} + n_{a} + \frac{1}{\alpha_{B}}\log^{\gamma}\left(\frac{t\log\left(\alpha_{B}\right)}{\epsilon}\right)\log\left(M\right)\right) \frac{\log\left(\alpha_{B}t/\epsilon\right)}{\log\log\left(\alpha_{B}t/\epsilon\right)}\right) \\
= \mathcal{O}\left(\alpha_{B}t\left(C_{B} + C_{e^{-iA/\alpha_{B}}}\left[\frac{\epsilon}{\alpha_{B}t\log\left(\alpha_{B}\right)}\right]\log\left(\frac{t(\alpha_{A} + \alpha_{B})}{\epsilon}\right)\right) \frac{\log\left(\alpha_{B}t/\epsilon\right)}{\log\log\left(\alpha_{B}t/\epsilon\right)}.\right).$$

From comparing Eqs. (23) and (24), we may immediately state sufficient criteria for when simulation in the interaction picture is advantageous over simulation in the Schrödinger picture.

- 1. The upper bound on the spectral norms  $\alpha_A \geq ||A||$ ,  $\alpha_B \geq ||B||$  of the encoding in Eq. (22) satisfy  $\alpha_A \gg \alpha_B$ . Generally speaking, this is correlated with term A representing fast dynamics  $||A|| \gg ||B||$ .
- 2. The gate complexity of time-evolution by A alone for time  $\tau \in \mathcal{O}(\alpha_B^{-1})$  is comparable to that of synthesizing the oracle  $O_B$ , that is  $C_{\sigma^{iA}\alpha_B^{-1}} \in \mathcal{O}(C_B)$ .

Note that satisfying condition (2) depends strongly on the structure of A, B. For instance, a simulation of A for time  $\tau \in \mathcal{O}(\alpha_B^{-1})$  using generic time-independent techniques has gate complexity  $\tilde{\mathcal{O}}\left(C_A\alpha_A/\alpha_B\right)$ . As we are interested in the case  $\|A\|/\|B\| \gg 1$ , this quantity could be large and scale poorly with the problem size. One very strong sufficient assumption is that  $e^{-iAt}$  is cheap and can be fast-forwarded, such that the gate complexity  $C_{e^{-iAt}}[\epsilon] \in \mathcal{O}(\text{polylog}(t/\epsilon))$  is constant up to logarithmic factor. This turns out to be a reasonable assumption in the application we next consider.

#### V. APPLICATION TO THE HUBBARD MODEL WITH LONG-RANGED INTERACTIONS

We now apply the technology developed in Section III and Section IV for Hamiltonian simulation in the interaction picture to physical problems of practical interest. We focus on the periodic Hubbard model in d-dimensions with N lattice sites subject to local disorder and translational-invariant two-body couplings that may be long-ranged in general. We perform a gate complexity comparison with simulation by time-independent techniques, and later in Section VA, we specialize this model to that of quantum chemistry simulations in the plane-wave and dual basis [14].

The periodic Hubbard Hamiltonian we consider has the form H = T + U + V, where T is the kinetic energy hopping operator, U is the local single-site potential, and V is a symmetric translationally-invariant two-body density coupling term between opposite spins. In the dual basis, H is expressed in terms of single-site Fermionic creation and annihilation operators  $\{a_{\vec{x}\sigma}, a_{\vec{y}\sigma'}^{\phantom{\dagger}}\} = \{a_{\vec{x}\sigma}^{\dagger}, a_{\vec{y}\sigma'}^{\phantom{\dagger}}\} = 0$ ,  $\{a_{\vec{x}\sigma}, a_{\vec{y}\sigma'}^{\phantom{\dagger}}\} = \delta_{\vec{x}\vec{y}}\delta_{\sigma\sigma'}$ , and the number operator  $n_{\vec{x}\sigma} = a_{\vec{x}\sigma}^{\dagger}a_{\vec{x}\sigma}$ . The subscript  $\vec{x} \in [-N^{1/d}, N^{1/d}]^d$  indexes one of N lattice sites in d dimensions, and  $\sigma \in \{-1, 1\}$  is a spin- $\frac{1}{2}$  index. Explicitly,

$$H = \sum_{\vec{x}, \vec{y}, \sigma} T(\vec{x} - \vec{y}) a_{\vec{x}\sigma}^{\dagger} a_{\vec{y}\sigma} + \sum_{\vec{x}, \sigma} U(\vec{x}, \sigma) n_{\vec{x}\sigma} + \sum_{(\vec{x}, \sigma) \neq (\vec{y}, \sigma')} V(\vec{x} - \vec{y}) n_{\vec{x}\sigma} n_{\vec{y}\sigma'}, \tag{29}$$

where the coefficients  $T(\vec{s}), U(\vec{s}, \sigma), V(\vec{s})$  are real functions of the  $\vec{s} \in [-N^{1/d}, N^{1/d}]^d$ .

Further simplification of Eq. (29) is possible as the kinetic energy operator is diagonal in the plane-wave basis. This basis related to the dual basis by a unitary rotation FFFT, an acronym for 'Fast-Fermionic-Fourier-Transform' [14] that implements a Fourier transform over the lattice site indices, resulting in Fermionic creation and annihilation operators  $c_{\vec{p}\sigma}^{\dagger}$ ,  $c_{\vec{p}\sigma}$ .

$$c_{\vec{p}\sigma} = \frac{1}{\sqrt{N}} \sum_{\vec{r}} a_{\vec{x}\sigma} \ e^{i2\pi \vec{p} \cdot \vec{x}/N^{1/d}} = \text{FFFT}^{\dagger} \ a_{\vec{p}\sigma} \ \text{FFFT}, \quad c_{\vec{p}\sigma}^{\dagger} = \frac{1}{\sqrt{N}} \sum_{\vec{r}} a_{\vec{x}\sigma}^{\dagger} \ e^{-i2\pi \vec{p} \cdot \vec{x}/N^{1/d}} = \text{FFFT}^{\dagger} \ a_{\vec{p}\sigma}^{\dagger} \ \text{FFFT}, \quad (30)$$

By substituting the Fourier transform of the kinetic term  $T(\vec{s}) = \frac{1}{N} \sum_{\vec{p}} \tilde{T}(\vec{p}) \ e^{-i2\pi \vec{p} \cdot \vec{s}/N^{1/d}}$ , an equivalent expression for the Hubbard Hamiltonian is

$$H = \text{FFFT}^{\dagger} \cdot \left( \sum_{\vec{x},\sigma} \tilde{T}(\vec{x}) n_{\vec{x}\sigma} \right) \cdot \text{FFFT} + \sum_{\vec{x},\sigma} U(\vec{x},\sigma) n_{\vec{x}\sigma} + \sum_{(\vec{x},\sigma) \neq (\vec{y},\sigma')} V(\vec{x} - \vec{y}) n_{\vec{x}\sigma} n_{\vec{y}\sigma'}, \tag{31}$$

where each term is now diagonal in their respective bases.

A simulation of this Hamiltonian on a qubit quantum computer requires a map from its Fermionic operators to spin operators. One possibility is the Jordan-Wigner transformation, which requires some map from Fermionic indices to spin indices, such as  $f(\vec{x}, \sigma) = N \frac{1-\sigma}{2} + \left(\sum_{j=0}^{d-1} \vec{x}_j N^{j/d}\right)$ . Subsequently, we replace

$$a_{\vec{x}\sigma}^{\dagger} \to \frac{1}{2} (X_{f(\vec{x},\sigma)} - iY_{f(\vec{x},\sigma)}) \bigotimes_{j=0}^{f(\vec{x},\sigma)-1} Z_j, \quad a_{\vec{x}\sigma} \to \frac{1}{2} (X_{f(\vec{x},\sigma)} + iY_{f(\vec{x},\sigma)}) \bigotimes_{j=0}^{f(\vec{x},\sigma)-1} Z_j.$$

$$(32)$$

Note the very useful property where number operators map to single-site spin operators  $n_{\vec{x}\sigma} \to \frac{1}{2}(I - Z_{f(\vec{x},\sigma)})$  under this encoding. Moreover, FFFT can be implemented using  $\mathcal{O}(N \log(N))$  primitive quantum gates [19] in the Jordan-Wigner representation.

Let us evaluate the worst-case gate-complexity for time-evolution by H in the Schrödinger picture. As an example of state-of-art using the truncated Taylor series approach in Appendix D,  $e^{-i(T+U+V)t}$  may be simulated using  $\mathcal{O}((\alpha_T + \alpha_U + \alpha_V)t \log(t(\alpha_T + \alpha_U + \alpha_V)/\epsilon))$  queries to oracles that encode T, U, and V as follows.

$$(\langle 0|_{\mathbf{a}} \otimes \mathbb{1}_{\mathbf{s}}) O_T(|0\rangle_{\mathbf{a}} \otimes \mathbb{1}_{\mathbf{s}}) = \frac{T}{\alpha_T}, \quad (\langle 0|_{\mathbf{a}} \otimes \mathbb{1}_{\mathbf{s}}) O_U(|0\rangle_{\mathbf{a}} \otimes \mathbb{1}_{\mathbf{s}}) = \frac{U}{\alpha_U}, \quad (\langle 0|_{\mathbf{a}} \otimes \mathbb{1}_{\mathbf{s}}) O_V(|0\rangle_{\mathbf{a}} \otimes \mathbb{1}_{\mathbf{s}}) = \frac{V}{\alpha_V}. \tag{33}$$

The cost of simulation depends strongly on the coefficients  $\tilde{T}(\vec{p}), U(\vec{x}), V(\vec{x})$ . The most straightforward approach synthesizes these oracles using the linear-combination of unitaries outline in Eq. (9). For instance,  $O_T = (PREP_T^{\dagger} \otimes FFFT^{\dagger}) \cdot SEL_T \cdot (PREP_T \otimes FFFT)$ , where

$$PREP_{T} |0\rangle_{a} = \sum_{\vec{p},\sigma} \sqrt{\frac{\tilde{T}(\vec{p})}{\alpha_{T}}} |\vec{p},\sigma\rangle_{a}, \quad SEL_{T} = \sum_{\vec{p},\sigma} |\vec{p},\sigma\rangle\langle\vec{p},\sigma|_{a} \otimes n_{\vec{p}\sigma}, \quad \alpha_{T} = \sum_{\vec{p},\sigma} |\tilde{T}(\vec{p})|.$$
 (34)

and similarly for U and V. As there are  $\mathcal{O}(N)$  distinct coefficients in the worst-case, each of  $\mathrm{PREP}_{T,U,V}$  costs  $\mathcal{O}(N)$ . As V has  $\mathcal{O}(N^2)$  terms,  $\mathrm{SEL}_V$  has the largest cost of  $\mathcal{O}(N^2)$ . Thus overall gate complexity is  $\mathcal{O}(N^2(\alpha_T + \alpha_U + \alpha_V)t\log(t(\alpha_T + \alpha_U + \alpha_V)/\epsilon))$ . As there are  $\mathcal{O}(N^2)$  coefficients,  $\max\{\alpha_T, \alpha_U, \alpha_V\} \in \mathcal{O}(\alpha_T + N^2)$ , and so the cost of simulation is

$$\mathcal{O}\left(N^2(\alpha_T + N^2)t\log\left(\frac{t(\alpha_T + N^2)}{\epsilon}\right)\right). \tag{35}$$

The worst-case gate-complexity may be substantially improved by instead simulating H in the interaction picture using the truncated Dyson series algorithm in Section III. The key idea is to simulate in the rotating frame of the interactions  $e^{-i(U+V)t}$ , where the Hamiltonian becomes time-dependent like  $H_I(t) = e^{i(U+V)t}Te^{-i(U+V)t}$ . Using the same oracle  $O_T$  in Eq. (33) for the kinetic term, the cost of time-evolution  $e^{-i(T+U+V)t}$  by this technique is given by Eq. (24):

$$C_{\text{TDS}} \in \mathcal{O}\left(\left(N + C_{e^{-i(U+V)/\alpha_T}} \left[\frac{\epsilon}{\alpha_T t \log(\alpha_T)}\right] \log\left(\frac{t(\|U+V\| + \alpha_T)}{\epsilon}\right)\right) \alpha_T t \frac{\log(\alpha_T t/\epsilon)}{\log\log(\alpha_T t/\epsilon)}\right)$$

$$\in \mathcal{O}\left(\left(N + C_{e^{i(U+V)/\alpha_T}}[\epsilon]\right) \alpha_T t \operatorname{polylog}\left((\|U+V\| + \alpha_T)t/\epsilon\right)\right).$$
(36)

All that remains is to bound the cost of time-evolution by the term  $C_{e^{i(U+V)/\alpha_T}}[\epsilon]$ . Using the fact that this is diagonal in the Pauli Z basis, the Hamiltonian may be fast-forwarded and so has cost that is independent of the evolution time and error. Thus the most straightforward approach decomposes

$$e^{i(U+V)t} = \left(\prod_{\vec{x},\sigma} e^{-iU(\vec{x},\sigma)n_{\vec{x}\sigma}t}\right) \left(\prod_{(\vec{x},\sigma)\neq(\vec{y},\sigma')} e^{-iV(\vec{x}-\vec{y})n_{\vec{x}\sigma}n_{\vec{y}\sigma'}t}\right). \tag{37}$$

There are  $\mathcal{O}(N^2)$  exponentials, and so  $C_{e^{i(U+V)t}}[\epsilon] \in \mathcal{O}(N^2)$ , which is independent of  $\epsilon$  in the primitive gate set of arbitrary two-qubit rotations, hence  $C_{\text{TDS}} \in \mathcal{O}\left(N^2\alpha_T t \log\left(\frac{t(\|U+V\|+\alpha_T)}{\epsilon}\right) \frac{\log\left(\alpha_T t/\epsilon\right)}{\log\log\left(\alpha_T t/\epsilon\right)}\right)$ . Compared to Eq. (35), we already a factor  $\mathcal{O}(N)$  improvement in cases where the kinetic energy is extensive, meaning that  $\alpha_T \in \mathcal{O}(N)$ .

A further improvement to

$$C_{\text{TDS}} \in \mathcal{O}(N\alpha_T t \operatorname{polylog}(N(\|U + V\| + \alpha_T)t/\epsilon))$$
 (38)

is possible through a more creative evaluation to reduce the gate complexity of  $e^{i(U+V)t}$  from  $\mathcal{O}(N^2)$  to  $\mathcal{O}(N\log(N))$ . Clearly,  $C_{e^{iUt}} \in \mathcal{O}(N)$  with N commuting terms poses no problem. The difficulty lies in constructing time-evolution by the two-body term  $e^{iVt}$  such that  $C_{e^{iVt}} \in \mathcal{O}(N\log N)$ . As V is a sum of  $\mathcal{O}(N^2)$  commuting terms, a gate cost  $\mathcal{O}(N^2)$  appear unavoidable. However, this may be reduced by exploiting the translation symmetry of its coefficients with a discrete Fourier transform. Assuming  $V(\vec{x}) = V(-\vec{x})$  is real and symmetric, its discrete Fourier transform  $\tilde{V}(\vec{k}) = \sum_{\vec{x}} V(\vec{x}) e^{i2\pi\vec{x}\cdot\vec{k}/N^{1/d}}$  only has real coefficients. Let we re-write V from Eq. (29) as

$$V = \sum_{(\vec{x},\sigma)\neq(\vec{y},\sigma')} V(\vec{x}-\vec{y}) n_{\vec{x}\sigma} n_{\vec{y}\sigma'} = \sum_{(\vec{x},\sigma)\neq(\vec{y},\sigma')} \frac{1}{N} \sum_{\vec{k}} \tilde{V}(\vec{k}) e^{-i2\pi(\vec{x}-\vec{y})\cdot\vec{k}/N} n_{\vec{x}\sigma} n_{\vec{y}\sigma'}$$

$$= \sum_{\vec{k}} \frac{\tilde{V}(\vec{k})}{N} \left( \sum_{(\vec{x},\sigma),(\vec{y},\sigma')} e^{-i2\pi(\vec{x}-\vec{y})\cdot\vec{k}/N} n_{\vec{x},\sigma} n_{\vec{y},\sigma'} - \sum_{\vec{x},\sigma} n_{\vec{x},\sigma} \right)$$

$$= \sum_{\vec{k}} \tilde{V}(\vec{k}) \underbrace{\left( \frac{1}{\sqrt{N}} \sum_{\vec{x}} e^{-i2\pi\vec{x}\cdot\vec{k}/N} \sum_{\sigma} n_{\vec{x},\sigma} \right)}_{\tilde{\chi}_{k}} \underbrace{\left( \frac{1}{\sqrt{N}} \sum_{\vec{y}} e^{i2\pi\vec{y}\cdot\vec{k}/N} \sum_{\sigma'} n_{\vec{y},\sigma'} \right)}_{\tilde{\chi}_{k}^{\dagger}} - \sum_{\vec{p},\sigma} \left( \sum_{\vec{k}} \tilde{V}(\vec{k}) \right) n_{\vec{p},\sigma}.$$

$$(39)$$

Our strategy for implementing  $e^{-iVt}$  is based on the following observation: Suppose we had a unitary oracle  $O_{\vec{A}}|j\rangle|0\rangle_o|0\rangle_{\rm garb} = |j\rangle|A_j\rangle_o|g(j)\rangle_{\rm garbage}$  that on input  $|j\rangle \in \mathbb{C}^{\dim[\vec{A}]}$ , outputs on the l-qubit o register, the value of the  $j^{\rm th}$  element of some complex vector  $\vec{A}$ , together with some garbage state  $|g(j)\rangle_{\rm garb}$  of lesser interest required to make the operation reversible. One may then perform a phase rotation that depends on  $A_j$  as follows:

$$|j\rangle|0\rangle_{o}|0\rangle_{\rm garb}|0\rangle\underset{O_{\vec{A}}}{\rightarrow}|j\rangle|A_{j}\rangle_{o}|g(j)\rangle_{\rm garb}|0\rangle\underset{\rm PHASE}{\rightarrow}e^{-iA_{j}t}|j\rangle|A_{j}\rangle_{o}|g(j)\rangle_{\rm garb}|0\rangle\underset{O_{\vec{A}}^{\dagger}}{\rightarrow}e^{-iA_{j}t}|j\rangle|0\rangle_{o}|0\rangle_{\rm garb}|0\rangle. \tag{40}$$

If  $A_j$  were represented in binary, say,  $A_j = \sum_{k=0}^{l-1} q_k 2^{-k}$ , PHASE could be implemented using  $\mathcal{O}(l)$  controlled-phase  $|0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes e^{-it2^{-k}Z}$  rotations.

Thus, we construct a unitary  $O_{V,\text{binary}}$  with the property that

$$O_{V,\text{binary}}\left(\bigotimes_{\vec{x},\sigma}|n_{\vec{x},\sigma}\rangle\right)|0\rangle|0\rangle_{\text{garb}} = \left(\bigotimes_{\vec{x},\sigma}|n_{\vec{x},\sigma}\rangle\right)|f(\vec{n})\rangle|g(\vec{n})\rangle_{\text{garb}},$$

$$f(\vec{n}) = \sum_{(\vec{x},\sigma)\neq(\vec{y},\sigma')}V(\vec{x}-\vec{y})n_{\vec{p},\sigma}n_{\vec{q},\sigma'},$$

$$(41)$$

where the value  $f(\vec{n})$  is encoded in  $l \in \mathcal{O}(\log(1/\epsilon))$  bits. This is implemented by the following sequence, where we have omitted the garbage register for clarity.

$$\left(\bigotimes_{\vec{x},\sigma}|n_{\vec{x}\sigma}\rangle\right)|0\rangle\underset{\text{ADD}}{\longrightarrow}\bigotimes_{\vec{x}}|\sum_{\sigma}n_{\vec{x}\sigma}\rangle\underset{\text{FFT}}{\longrightarrow}\bigotimes_{\vec{k}}|\tilde{\chi}_{\vec{k}}\rangle\underset{|\cdot|^{2}}{\longrightarrow}\bigotimes_{\vec{k}}||\tilde{\chi}_{\vec{k}}|^{2}\rangle\underset{\text{V}}{\longrightarrow}\bigotimes_{\vec{k}}|V(\vec{k})|\tilde{\chi}_{\vec{k}}|^{2}\rangle,\tag{42}$$

The cost of  $O_{V,\text{binary}}$  may be expressed in term of the four standard reversible arithmetical operations, addition, subtraction, division, and multiplication, which each cost  $\mathcal{O}(\text{poly}(l))$  primitive gates. The first steps ADD adds  $\mathcal{O}(N)$  pairs of two bits  $n_{\vec{x},\sigma=1}+n_{\vec{x},\sigma=-1}$  and costs  $\mathcal{O}(N)$  arithmetic operations. The second step FFT is a d-dimensional Fast-Fourier-Transform on  $\mathcal{O}(N)$  binary numbers and requires  $\mathcal{O}(N\log(N))$  arithmetic operations. The third step computes the absolute-value-squared of  $\mathcal{O}(N)$  binary numbers, and uses  $\mathcal{O}(N)$  arithmetic operations. The last step multiplies each  $|\tilde{\chi}_k|^2$  with the corresponding  $V_k$ , and costs  $\mathcal{O}(N)$  arithmetic operations. This last step may actually be avoided by rescaling the time parameter  $e^{-iA_jt} \to e^{-iA_jV_kt}$  in Eq. (40). Thus the total cost of  $O_{V,\text{binary}}$  is  $\mathcal{O}(N\log(N)\operatorname{poly}(l)) = \mathcal{O}(N\log(N)\operatorname{polylog}(1/\epsilon))$ . Using one query to  $O_{V,\text{binary}}$ ,  $O_{V,\text{binary}}^{\dagger}$ , and  $\mathcal{O}(N\log(N)\operatorname{polylog}(1/\epsilon))$  primitive quantum gates, we may thus apply  $e^{-iVt}$  with a phase error  $\mathcal{O}(\epsilon)$  for a fixed value of t.

## A. Application to quantum chemistry in the plane-wave basis

The Hamiltonian that generates time-evolution for a state  $|\psi(t)\rangle$  of interacting electrons in d=3 dimension consists of three operators: the electron kinetic energy T, the electron-nuclei potential energy U, and the electron-electron

potential energy V. It was demonstrated by [14] that this electronic structure Hamiltonian is a special case of the general Hubbard Hamiltonian of Eq. (31). In the plane-wave basis,

$$i\partial_{t}|\psi(t)\rangle = H|\psi(t)\rangle$$

$$H_{P} = \frac{1}{2} \sum_{\vec{p},\sigma} |\vec{k}_{\vec{p}}|^{2} c_{\vec{p},\sigma}^{\dagger} c_{\vec{p},\sigma} + \frac{4\pi}{\Omega} \sum_{\vec{p} \neq \vec{q} \atop j,\sigma} \left( -\zeta_{j} \frac{e^{i\vec{k}_{\vec{q}-\vec{p}} \cdot \vec{R}_{j}}}{|\vec{k}_{\vec{p}-\vec{q}}|^{2}} \right) c_{\vec{p},\sigma}^{\dagger} c_{\vec{q},\sigma} + \frac{2\pi}{\Omega} \sum_{\substack{(\vec{p},\sigma) \neq (\vec{q},\sigma') \\ \vec{p} \neq 0}} \frac{c_{\vec{p},\sigma}^{\dagger} c_{\vec{q},\sigma'}^{\dagger} c_{\vec{q}+\vec{\nu},\sigma'} c_{\vec{p}-\vec{\nu},\sigma}}{|\vec{k}_{\vec{\nu}}|^{2}},$$

$$(43)$$

where  $k_{\vec{p}} = 2\pi \vec{p}/\Omega^{1/3}$ ,  $\vec{p} \in [-N^{1/3}, N^{1/3}]^3$ ,  $r_{\vec{p}} = \vec{p}(\Omega/N)^{1/3}$ ,  $\Omega$  represents the volume of the simulation, and  $\eta_j$  is the nuclear charge of the  $j^{\text{th}}$  nucleus. Whereas T is diagonal here, one may find an alternate basis where U and V are diagonal. This is the dual basis, defined through the unitary transform FFFT of Eq. (30). In this basis, let us define the state  $|\psi_D(t)\rangle = \text{FFFT}^{\dagger} |\psi(t)\rangle$ , which evolves under the Hamiltonian H, which is of exactly that of Eq. (31), with coefficients

$$\tilde{T}(\vec{p}) = \frac{1}{2} |\vec{k}_{\vec{p}}|^2 \quad U(\vec{p}) = -\frac{4\pi}{\Omega} \sum_{\vec{\nu} \neq 0,} \frac{\zeta_j \cos\left[\vec{k}_{\vec{\nu}} \cdot \left(\vec{R}_{\vec{j}} - \vec{r}_{\vec{p}}\right)\right]}{|\vec{k}_{\vec{\nu}}|^2}, \quad V(\vec{s}) = \frac{2\pi}{\Omega} \sum_{\vec{\nu} \neq 0} \frac{\cos\left[\vec{k}_{\vec{\nu}} \cdot \vec{r}_{\vec{s}}\right]}{|\vec{k}_{\vec{\nu}}|^2}. \tag{44}$$

Thus the cost of time-evolution by the electronic structure Hamiltonian  $e^{-iHt}$  using the interaction picture is given by Eq. (38). The only dominant parameter that depends on the problem is the normalization factor

$$\alpha_T = \sum_{\vec{p},\sigma} \frac{|\vec{k}_{\vec{p}}|^2}{2} \in \mathcal{O}\left(\int_0^{N^{1/3}} \frac{p^2}{\Omega^{2/3}} (4\pi p^2) dp\right) = \mathcal{O}\left(\frac{N^{5/3}}{\Omega^{2/3}}\right). \tag{45}$$

The spectral norms of the potential terms are bounded by  $||U+V|| \in \mathcal{O}\left(\frac{||\zeta||_1 N^{5/3}}{\Omega^{1/3}} + \frac{N^{7/3}}{\Omega^{1/3}}\right)$ , where  $||\zeta||_1 = \sum_j |\zeta_j|$  [14] – the exact scaling is unimportant, so long as it is polynomial. Thus the total gate complexity of time-evolution under the assumption of constant density (i.e.  $N/\Omega \in O(1)$ ) is

$$C_{\text{TDS}} \in \mathcal{O}\left(\frac{N^{8/3}}{\Omega^{2/3}}t \operatorname{polylog}\left(\frac{(\|\zeta\|_1 + N)Nt}{\epsilon}\right)\right) = \mathcal{O}\left(N^2t \operatorname{polylog}\left(\|\zeta\|_1 Nt\epsilon\right)\right). \tag{46}$$

In contrast, the cost of simulation in the plane-wave dual basis [14] applies the 'Qubitization' technique [10] and has gate complexity that scales like  $\tilde{\mathcal{O}}((\|\zeta\|_1 + N)N^{8/3}t)$ , and also has a polynomial dependence on the nuclear charges  $\zeta_j$ . Our method outperforms this, and notably depends only poly-logarithmically on the sum of the nuclear charges. This means that the cost of the simulation method is largely insensitive to the nuclear charges present in the simulation, unlike Trotter-Suzuki simulation methods which sensitively depend on the nuclear charges [20].

### VI. APPLICATION TO SPARSE HAMILTONIAN SIMULATION

In this section, we present a complexity-theoretic perspective of the improvements that are enabled by simulation with the truncated Dyson series, and simulation in the interaction picture. We do so by evaluating the query complexity for the simulation of sparse Hamiltonians H. Such Hamiltonians of dimension N are called d-sparse if there are at most  $d \in \mathcal{O}(\operatorname{polylog}(N))$  non-zero entries in every row, and the position and values of these entries may be efficiently output, in say a binary representation, by some classical circuit of size  $\mathcal{O}(\operatorname{polylog}(N))$ . This abstract model is useful in quantum complexity theory as a natural generalization these classical circuits leads to unitary quantum oracles that can be queried to access the same information, but now in superposition. With this model, we achieve in Section VIA time-dependent simulation with a square-root improvement with respect to the sparsity parameter, and gate complexity scaling with the average instead of worst-case rate-of-change  $\|\dot{H}\|$ . By moving to the interaction picture in Section VIB, we find more efficient time-independent simulation algorithms for diagonally-dominant Hamiltonians.

This model assumes that the Hamiltonian is input to the simulation routine through two oracles:  $O_f$  and  $O_H$ .  $O_H$  is straight forward; it provides the values of the matrix elements of the Hamiltonian given a time index  $|t\rangle$  and indices  $|x\rangle$ ,  $|y\rangle$  to for the row and column of H as follows

$$O_H|t, x, y, 0\rangle = |t, x, y, H_{xy}(t)\rangle. \tag{47}$$

 $O_f$  provides the locations of the non-zero matrix elements in any given row or column of H. Specifically, let f(x,j) give the column index of the j<sup>th</sup> non-zero matrix element in row x if it exists and an appropriately chosen zero element if it does not. In particular, let  $r_{t,j}$  be the list of column indices of these non-zero matrix elements in row j. We then define, with a time-index t,

$$O_f|t, x, j\rangle = |t, x, f_t(x, j)\rangle. \tag{48}$$

### A. Simulation of sparse time-dependent Hamiltonians

Applying the truncated Dyson series simulation algorithm to sparse Hamiltonians requires us to synthesize HAM-T in Definition 2 from these oracles  $O_H$ ,  $O_F$ . This is possible by a straightforward construction.

**Lemma 8** (Synthesis of HAM-T from sparse Hamiltonian oracles). Let a time-dependent d-sparse Hamiltonian  $H(s):[0,t]\to\mathbb{C}^{N\times N}$  be be encoded in the oracles  $O_H$  and  $O_f$  from Eqs. (47) and (48) to  $n_p$  bits of precision. Then the unitary HAM-T such that for  $\|H\|_{\max}:=\max_s\|H(s)\|_{\max}$

$$(\langle 0|_a \otimes \mathbb{1}_s) \text{ HAM-T}(|0\rangle_a \otimes \mathbb{1}_s) = \sum_t |t\rangle\langle t|_d \otimes \frac{H(t)}{d||H||_{\text{max}}}, \tag{49}$$

can be implemented with O(1) queries to  $O_f$  and  $O_H$ , and  $O(\operatorname{poly}(n_p) + \log(N))$  primitive gates.

*Proof.* The proof closely mimics the discussion by [12], but we formally restate the result here to make it manifestly applicable to the time-dependent case. Let  $U_{\text{col}}$ ,  $U_{\text{row}}$  be the following unitary transformations

$$U_{\text{col}}|t\rangle_{d}|k\rangle_{s}|0\rangle_{a} := |t\rangle_{d}|\chi_{k}(t)\rangle = \frac{1}{\sqrt{d}} \sum_{p \in r_{k}} |t\rangle_{d}|k\rangle_{s}|p\rangle_{a_{1}} \left(\sqrt{\frac{H_{p,k}(t)}{\|H\|_{\text{max}}}}|0\rangle_{a_{2}} + \sqrt{1 - \frac{|H_{k,p}(t)|}{\|H(t)\|_{\text{max}}}}|1\rangle_{a_{2}}\right), \tag{50}$$

$$\langle 0|_{a}\langle j|_{s}\langle t|_{d}U_{\text{row}}^{\dagger} := \langle \bar{\chi}_{j}(t)|\langle t|_{d} = \frac{1}{\sqrt{d}} \sum_{q \in r_{j}} \left(\sqrt{\frac{H_{j,q}(t)}{\|H\|_{\text{max}}}}\langle 0|_{a_{2}} + \sqrt{1 - \frac{|H_{q,j}(t)|}{\|H\|_{\text{max}}}}\langle 2|_{a_{2}}\right) \langle j|_{a_{1}}\langle q|_{s}\langle t|_{d},$$

$$\langle \bar{\chi}_{j}(t)|\chi_{k}(t)\rangle = \frac{H_{j,k}}{d\|H\|_{\text{max}}}.$$

Let  $|\psi\rangle = \sum_{t,k} a_{t,k} |t\rangle_d |k\rangle_s$ . We then have that

$$[|0\rangle\langle 0|_{a} \otimes \mathbb{1}]U_{\text{row}}^{\dagger} \cdot U_{\text{col}}|t\rangle_{d}|\psi\rangle|0\rangle_{a} = |0\rangle\langle 0|_{a} \otimes \sum_{t',j} (|t'\rangle\langle t'|_{d} \otimes |j\rangle\langle j|_{s}) \sum_{t,k} a_{t,k} U_{\text{row}}^{\dagger} \cdot U_{\text{col}}|t\rangle_{d}|k\rangle_{s}|0\rangle_{a}.$$

$$= |0\rangle_{a} \sum_{t',j} |t'\rangle_{d}|j\rangle_{s} \sum_{t,k} a_{t,k} (\langle \bar{\chi}_{j}(t')|\langle t'|_{d})(|t\rangle_{d}|\chi_{k}(t)\rangle)$$

$$= \sum_{j,k} a_{t,k}|0\rangle_{a}|t\rangle_{d}|j\rangle_{s} \frac{H_{j,k}(t)}{d|H|_{\text{max}}} = \frac{|0\rangle_{s}H(t)|\psi\rangle}{d|H|_{\text{max}}}.$$

$$(51)$$

As this result holds for any input state  $|\psi\rangle$ , the choice HAM-T =  $U_{\text{row}}^{\dagger} \cdot U_{\text{col}}$  satisfies Eq. (49).

The query cost then follows from the fact that  $U_{\text{col}}$  and  $U_{\text{row}}^{\dagger}$  can be implemented using O(1) calls to  $O_f$ . In

particular,  $U_{\rm col}$  can be prepared in the following steps:

$$|t\rangle|k\rangle|0\rangle \mapsto |t\rangle|k\rangle \frac{1}{\sqrt{d}} \sum_{\ell=1}^{d} |\ell\rangle|0\rangle$$

$$\stackrel{\leftrightarrow}{O_f} |t\rangle|k\rangle \frac{1}{\sqrt{d}} \sum_{p\in r_k} |p\rangle|0\rangle$$

$$\stackrel{\leftrightarrow}{O_H} |t\rangle|k\rangle \frac{1}{\sqrt{d}} \sum_{p\in r_k} |p\rangle|H_{k,p}(t)\rangle|0\rangle$$

$$\mapsto |t\rangle|k\rangle \frac{1}{\sqrt{d}} \sum_{p\in r_k} |p\rangle|H_{k,p}(t)\rangle \left(\sqrt{\frac{H_{k,p}^*(t)}{\|H\|_{\max}}}|0\rangle + \sqrt{1 - \frac{|H_{k,p}(t)|}{\|H\|_{\max}}}|1\rangle\right)$$

$$\stackrel{\leftrightarrow}{O_H^{-1}} |t\rangle|k\rangle \frac{1}{\sqrt{d}} \sum_{p\in r_k} |p\rangle \left(\sqrt{\frac{H_{p,k}(t)}{\|H\|_{\max}}}|0\rangle + \sqrt{1 - \frac{|H_{p,k}(t)|}{\|H\|_{\max}}}|1\rangle\right)|0\rangle = U_{\text{col}}|t\rangle|k\rangle|0\rangle. \tag{52}$$

Therefore accessing  $U_{\text{col}}$  unitaries requires O(1) queries to the fundamental oracles as claimed, along with a arithmetic circuit, of size polynomial in the number of bits used to represent  $|H_{k,p}(t)\rangle$ , for computing trigonometric functions of the magnitudes of the complex-valued matrix elements as well as their arguments. The argument that  $U_{\text{row}}^{\dagger}$  requires O(1) queries follows in exactly the same manner, but with an additional final step that swaps the s and  $a_1$  registers.  $\square$

Once HAM-T, is obtained, the complexity of simulation follows directly from previous results.

**Theorem 9** (Simulation of sparse time-dependent Hamiltonians). Let a time-dependent d-sparse Hamiltonian H(s):  $[0,t] \to \mathbb{C}^{N\times N}$  have average rate-of-change  $\langle \|\dot{H}\| \rangle = \frac{1}{t} \int_0^t \left\| \frac{\mathrm{d}H(s)}{\mathrm{d}s} \right\| \mathrm{d}s$ , and be encoded in the oracles  $O_H$  and  $O_f$  from Eqs. (47) and (48) to  $n_p$  bits of precision. Then the time-ordered evolution operator  $\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right]$  may be approximated with error  $\epsilon$  and probability of failure  $\mathcal{O}(\epsilon)$  using

- 1. Queries to  $O_H$  and  $O_f : \mathcal{O}\left(d\|H\|_{\max}t\frac{\log\left(d\|H\|_{\max}t/\epsilon\right)}{\log\log\left(d\|H\|_{\max}t/\epsilon\right)}\right)$ .
- 2. Qubits:  $\mathcal{O}\left(n_p + \log\left(\frac{Nt}{d\|H\|_{\max}\epsilon}\left(\langle \|\dot{H}\| \rangle + [d\|H\|_{\max}]^2\right)\right)\right)$
- 3. Primitive gates:  $\mathcal{O}\left(d\|H\|_{\max}t\left(\operatorname{poly}(n_p) + \log\left(\frac{Nt}{d\|H\|_{\max}\epsilon}\left(\langle \|\dot{H}\|\rangle + [d\|H\|_{\max}]^2\right)\right)\frac{\log\left(d\|H\|_{\max}t/\epsilon\right)}{\log\log\left(d\|H\|_{\max}t/\epsilon\right)}\right)\right)$ .

Proof. From Theorem 3, the number of qubits required is  $\mathcal{O}(n_s + n_a + n_d + \log\log(1/\epsilon))$ . Values for these parameters are obtained from the construction of HAM-T in Lemma 8, which also requires an additional  $n_p$  qubits for the bits of precision to which H is encoded. In this construction,  $n_a \in \mathcal{O}(n_s) \in \mathcal{O}(\log(N))$ .  $n_d$  is obtained from the number of time-discretization points required by Theorem 3. Simulation for time t is implemented by simulating segments of duration  $\Theta(\alpha^{-1})$ . As there are  $\Theta(t\alpha)$  segments, we rescale  $\epsilon \to \Theta(\epsilon/(t\alpha))$ .

Compared to prior art [6], this is a quadratic improvement in sparsity d. Furthermore, instead of scaling with the worst-case  $\mathcal{O}\left(\log\left(\max_{s}\|\dot{H}(s)\|\right)\right)$ , we obtain scaling with average rate-of-change  $\langle\|\dot{H}\|\rangle$ . If we further assume that the computed matrix elements  $H_{j,k}$  are not exact, the number of bit of precision scales like  $n_p \in \mathcal{O}\left(\log\left(\|H\|t/\epsilon\right)\right)$  [7]. Note several generic improvements to Theorem 9 are possible, but will not be pursued further as they are straightforward. For instance, if  $\|H(t)\|_{\max}$  as a function of time is known, we may use step sizes of varying size by encoding each segment  $t \in [t_j, t_{j+1}]$  with the largest  $\max_{t \in [t_j, t_{j+1}]} \|H(t)\|_{\max}$ , rather than the worst-case  $\max_{t} \|H(t)\|_{\max}$ .

### B. Simulation of sparse time-independent Hamiltonians in the interaction picture

We now turn our attention to time-independent d-sparse Hamiltonians H = A + B where A is diagonal and  $B_{k,k} = 0$  for all k. In particular, we consider the case of diagonally dominant Hamiltonians, where  $||A|| \ge d||B||_{\max}$ . Given norms for each of these terms ||A|| and  $||B||_{\max}$ , it is straightforward to simulate time-evolution  $e^{-iHt}$  in the Schrödinger picture. For instance, using the truncated Taylor series approach in Eq. (23), one obtains a query complexity of  $\mathcal{O}(t(d||B||_{\max} + ||A||) \operatorname{polylog}(t, d, ||A||, ||B||_{\max}, \epsilon))$ . By instead simulating  $H_I(t) = e^{iAt}Be^{-iAt}$  in the

interaction picture, the dependence on ||A|| can be removed, which is particularly useful in cases of strong diagonal dominance  $||A|| \ge d||B||_{\text{max}}$ , of which the Hubbard model with long-ranged interactions in Section V is an example. Similar to our results for time-dependent sparse Hamiltonian simulation in Section VIA, this is easily proven by mapping the input oracles  $O_H$  and  $O_f$  for matrix values and positions to the oracles of Theorem 7 for the more general result.

**Theorem 10** (Simulation of sparse diagonally dominant Hamiltonians). Let a time-independent d-sparse Hamiltonian  $H = A + B \in \mathbb{C}^{N \times N}$  be encoded in the oracles  $O_H$  and  $O_f$  from Eqs. (47) and (48) to  $n_p$  bits of precision, and be characterized by spectral norm spectral norm ||A|| for the diagonal component and max-norm  $||B||_{\max}$  for the off-diagonal component. Let  $\alpha_B = d||B||_{\max}$ . Then the time-evolution operator  $e^{-iHt}$  may be approximated with error  $\epsilon$  using

- 1. Queries to  $O_H$  and  $O_f$ :  $\mathcal{O}\left(\alpha_B t \frac{\log{(\alpha_B t/\epsilon)}}{\log{\log{(\alpha_B t/\epsilon)}}}\right)$ .
- 2. Qubits:  $\mathcal{O}\left(n_p + \log\left(N\right) + \log\left(\frac{t}{\epsilon}\left(\|A\| + \alpha_B\right)\right)\right)$ .
- 3. Primitive gates:  $\mathcal{O}\left(\alpha_B t \left(\log\left(N\right) + \operatorname{poly}(n_p) \log\left(\frac{t}{\epsilon} \left(\|A\| + \alpha_B\right)\right)\right) \frac{\log\left(\alpha_B t/\epsilon\right)}{\log\log\left(\alpha_B t/\epsilon\right)}\right)$ .

*Proof.* This follows immediately by combining the query complexity of Lemma 6 to  $e^{-iAt}$  and HAM-T that encodes the Hamiltonian  $H_I(t) = e^{iAt}Be^{-iAt}$  in the rotating frame, with the query complexity of the approach in Theorem 7 for synthesizing these oracles using the input oracles  $O_H$  and  $O_f$ . One possible decomposition of HAM-T is

$$\text{HAM-T} = \left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{iA\tau m/M}\right) \left(\mathbb{1}_d \otimes O_B\right) \left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{-iA\tau m/M}\right), \quad (53)$$

$$(\langle 0|_a \otimes \mathbb{1}_s)O_B(|0\rangle_a \otimes \mathbb{1}_s) = \frac{B}{\alpha_B},$$

where  $\alpha_B = d\|B\|_{\max}$ ,  $\tau \in \mathcal{O}(\alpha_B^{-1})$  and  $M \in \mathcal{O}\left(\frac{t}{\epsilon}(\|A\| + \alpha_B)\right)$ . Note that with this construction,  $(\langle 0|_a \otimes \mathbb{1}_s) \text{ HAM-T}(|0\rangle_a \otimes \mathbb{1}_s) = \sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \frac{H_I(\tau m/M)}{d\|B\|_{\max}}$ . First, let us synthesize  $\left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{iA\tau m/M}\right)$  using  $\mathcal{O}(1)$  queries to the input oracles  $O_H$ , and

First, let us synthesize  $\left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{iA\tau m/M}\right)$  using  $\mathcal{O}(1)$  queries to the input oracles  $O_H$ , and  $\mathcal{O}(\log(N) + n_p \log(M))$  primitive gates. Since A is diagonal,  $e^{-iAt}$  can be simulated for any t > 0 using only two queries. This is implemented by the following steps:

$$|k\rangle|0\rangle|0\rangle|0\rangle \mapsto |k\rangle|k\rangle|0\rangle|0\rangle \tag{54}$$

$$\mapsto |k\rangle|k\rangle|H_{k,k}\rangle|0\rangle$$

$$\mapsto |k\rangle|k\rangle|H_{k,k}\rangle e^{-iH_{k,k}Zt}|0\rangle = e^{-iH_{k,k}t}|k\rangle|k\rangle|H_{k,k}\rangle|0\rangle$$

$$\mapsto e^{-iH_{k,k}t}|k\rangle|k\rangle|0\rangle|0\rangle$$

$$\to e^{-iH_{k,k}t}|k\rangle|0\rangle|0\rangle.$$

Step one uses  $n_s \in \mathcal{O}(\log(N))$  CNOT gates to copy the computational basis state  $|k\rangle$ . Step three applies  $\mathcal{O}(n_p)$  phase rotation with angle controlled by the bits of  $|H_{k,k}\rangle$ , and the value of t, which is given beforehand. Subsequently,  $\left(\sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes \mathbb{1}_a \otimes e^{iA\tau m/M}\right)$  may be implemented by a sequence of rotations with angles increasing in a geometric series, and each controlled by a different qubit in the d register, e.g. controlled- $e^{iA\tau 2^{-1}/M}$ ,  $e^{iA\tau 2^{-2}/M}$ ,  $e^{iA\tau 2^{-n+p}/M}$ . Naively, this requires  $\mathcal{O}(\log(M))$  queries. However, it is only necessary to compute  $|H_{k,k}\rangle$  once as the entire sequence of controlled-phases may be applied after step three. Similarly, it is only necessary to copy the computational basis state  $\mathcal{O}(1)$  times.

Second, let us synthesize  $O_B$  using  $\mathcal{O}(1)$  queries to the input oracles  $O_H$  and  $O_f$ . How this is done should be clear from Lemma 8, by omitting the time-index, and preparing the state in Eq. (50) when the input indices k = p. This has gate complexity  $\mathcal{O}(\text{poly}(n_p) + \log(N))$ . Thus  $e^{-iA\tau}$  and HAM-T combined have query complexity  $\mathcal{O}(1)$  to  $O_H$  and  $O_f$ , and gate complexity  $\mathcal{O}(\text{poly}(n_p)\log(M) + \log(N))$ . By substituting into Lemma 6, we obtain the stated results.

This provides a formal proof that the query complexity of simulating a Hamiltonian, within the interaction picture, is independent of the magnitude of the diagonal elements of the Hamiltonian, up to logarithmic factors.

#### VII. CONCLUSION

We demonstrate in this work that simulating quantum dynamics within the interaction picture rather than the Schrödinger picture can be advantageous. This requires a good time-dependent simulation algorithm – our formulation of the truncated Dyson series simulation algorithm is rigorous and achieves space savings over the original proposal [8]. When applied to simulating Hubbard models with long-ranged interactions as well as quantum chemistry within a plane-wave basis, we find that the gate complexity scales with time t as  $\tilde{\mathcal{O}}(N^2t)$  for systems with N sites, assuming that kinetic energy is an extensive property. In the black-box model of time-dependent sparse Hamiltonians, we find that simulation in the truncated Dyson series framework generally reduces the query complexity from  $\tilde{\mathcal{O}}(d^2)$  to  $\tilde{\mathcal{O}}(d)$ . Combined with the interaction picture, this also reduces the scaling with respect to the magnitude of diagonal components from linear to logarithmic, which is particularly relevant to the common case of diagonally dominant Hamiltonians.

Some straightforward extensions of our work on time-dependent simulation are possible. For instance, the step-size of our algorithm may be adaptively chosen to scale with the worst-case norm of the Hamiltonian in each segment rather than with worst-case across all segments. Furthermore, the query complexity  $\tilde{\mathcal{O}}(d\|H\|_{\text{max}})$  of our time-dependent sparse Hamiltonian simulation algorithm may be easily improved in combination with [12] to scale like  $\tilde{\mathcal{O}}\left(\sqrt{d\|H\|_{\text{max}}\|H\|_1}\right)$  if the induced one-norm  $\|H\|_1$  of the Hamiltonian is also known beforehand. Our technique of interaction picture simulation is also applicable to many other quantum systems, particularly quantum field theories. Identifying other such physical systems would be of great interest.

More generally, the complexity of time-independent quantum simulation for generic Hamiltonians, given minimal information, appears to be nearly resolved [11]. Thus future advancements, such as this work, will likely focus on exploiting the detailed structure of Hamiltonians of interest. The promise of results in similar directions is exemplified by recent work that exploit the geometric locality of interactions [16], or the sizes of different terms in a Hamiltonian [21]. The challenge will be finding characterizations of Hamiltonians that are sufficiently specific so as to enable a speedup, yet sufficiently general so as to include problems of practical and scientific value.

#### VIII. ACKNOWLEDGMENTS

We thank Isaac Chuang, Jeongwan Haah, Robin Kothari, and Matthias Troyer for insightful discussions. We further thank Dominic Berry for pointing out important typographic errors in a previous version of the manuscript.

<sup>[1]</sup> Dorit Aharonov and Amnon Ta-Shma, "Adiabatic Quantum State Generation and Statistical Zero Knowledge," in *Proceedings of the Thirty-fifth Annual ACM Symposium on Theory of Computing*, STOC '03 (ACM, New York, NY, USA, 2003) pp. 20–29.

<sup>[2]</sup> Dominic W Berry, Graeme Ahokas, Richard Cleve, and Barry C Sanders, "Efficient Quantum Algorithms for Simulating Sparse Hamiltonians," Commun. Math. Phys. 270, 359–371 (2007).

<sup>[3]</sup> Nathan Wiebe, Dominic Berry, Peter Høyer, and Barry C Sanders, "Higher order decompositions of ordered operator exponentials," Journal of Physics A: Mathematical and Theoretical 43, 65203 (2010).

<sup>[4]</sup> Andrew M Childs and Nathan Wiebe, "Hamiltonian Simulation Using Linear Combinations of Unitary Operations," Quantum Information & Computation 12, 901–924 (2012).

<sup>[5]</sup> Dominic W Berry and Andrew M Childs, "Black-box Hamiltonian Simulation and Unitary Implementation," Quantum Info. Comput. 12, 29–62 (2012).

<sup>[6]</sup> Dominic W Berry, Andrew Μ Childs, Richard Cleve, Robin Kothari, and Rolando D simulating Somma, "Exponential improvement inprecision for Hamiltonians," sparse Proceedings of the 46th Annual ACM Symposium on Theory of Computing - STOC '14, STOC '14 (ACM Press, New York, New York, USA, 2014) pp. 283-292.

<sup>[7]</sup> Dominic W Berry, Andrew M Childs, and Robin Kothari, "Hamiltonian Simulation with Nearly Optimal Dependence on all Parameters," in 2015 IEEE 56th Annual Symposium on Foundations of Computer Science, FOCS '15 (IEEE, Washington, DC, USA, 2015) pp. 792–809.

<sup>[8]</sup> Dominic W Berry, Andrew M Childs, Richard Cleve, Robin Kothari, and Rolando D Somma, "Simulating Hamiltonian Dynamics with a Truncated Taylor Series," Phys. Rev. Lett. 114, 90502 (2015).

<sup>[9]</sup> Leonardo Novo and Dominic W Berry, "Improved Hamiltonian simulation via a truncated Taylor series and corrections," Quantum Info. Comput. 17, 623 (2017).

<sup>[10]</sup> Guang Hao Low and Isaac L Chuang, "Hamiltonian Simulation by Qubitization," arXiv preprint arXiv:1610.06546 (2016), arXiv:1610.06546.

- [11] Guang Hao Low and Isaac L. Chuang, "Optimal Hamiltonian Simulation by Quantum Signal Processing," Physical Review Letters 118, 10501 (2017), arXiv:1606.02685.
- [12] Guang Hao Low and Isaac L Chuang, "Hamiltonian Simulation by Uniform Spectral Amplification," arXiv preprint arXiv:1707.05391 (2017), arXiv:1707.05391.
- [13] James D Whitfield, Jacob Biamonte, and Alán Aspuru-Guzik, "Simulation of electronic structure Hamiltonians using quantum computers," Molecular Physics 109, 735–750 (2011).
- [14] Ryan Babbush, Nathan Wiebe, Jarrod McClean, James McClain, Hartmut Neven, and Garnet Kin-Lic Chan, "Low-depth quantum simulation of materials," Phys. Rev. X 8, 011044 (2018).
- [15] Bela Bauer, Dave Wecker, Andrew J. Millis, Matthew B. Hastings, and Matthias Troyer, "Hybrid quantum-classical approach to correlated materials," Phys. Rev. X 6, 031045 (2016).
- Matthew В [16] Jeongwan Haah, Hastings, Robin Kothari, and Guang "Quantum Algorithm for Simulating Real Time Evolution of Lattice Hamiltonians," 2018 IEEE 59th Annual Symposium on Foundations of Computer Science (FOCS) FOCS '18, 350–360 (2018).
- [17] Vivek V Shende, Stephen S Bullock, and Igor L Markov, "Synthesis of quantum-logic circuits," IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 25, 1000–1010 (2006), quant-ph/0406176.
- [18] Andrew M Childs, Dmitri Maslov, Yunseong Nam, Neil J Ross, and Yuan Su, "Toward the first quantum simulation with quantum speedup," Proceedings of the National Academy of Sciences 115, 9456–9461 (2018).
- [19] Andrew J Ferris, "Fourier Transform for Fermionic Systems and the Spectral Tensor Network," Phys. Rev. Lett. 113, 10401 (2014).
- [20] Ryan Babbush, Jarrod McClean, Dave Wecker, Alán Aspuru-Guzik, and Nathan Wiebe, "Chemical basis of Trotter-Suzuki errors in quantum chemistry simulation," Physical Review A 91, 022311 (2015).
- [21] Stuart Hadfield and Anargyros Papageorgiou, "Divide and conquer approach to quantum Hamiltonian simulation," New Journal of Physics (2018).
- [22] Steven A Cuccaro, Thomas G Draper, Samuel A Kutin, and David Petrie Moulton, "A new quantum ripple-carry addition circuit," arXiv preprint quant-ph/0410184 (2004), arXiv:0410184.
- [23] Dominic W. Berry, Mária Kieferová, Artur Scherer, Yuval R. Sanders, Guang Hao Low, Nathan Wiebe, Craig Gidney, and Ryan Babbush, "Improved techniques for preparing eigenstates of fermionic Hamiltonians," npj Quantum Information 4, 22 (2018).

### Appendix A: Error Estimates for Truncated Dyson series

In this section, we complete the proof of Lemma 5 for the error from truncating the Dyson series at order K, and the error from approximating its terms, which are time-ordered integrals, with Riemann sums. These results provide a rigorous upper bound on the error of time-dependent Hamiltonian simulation. Let  $D_k$  be the  $k^{\text{th}}$  term in the Dyson expansion, and let  $B_k$  be the Riemann sum of  $D_k$  with each dimension discretized into  $M = t/\Delta$  segments.

$$\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right] = \sum_{k=0}^\infty (-i)^k D_k = \lim_{M \to \infty} \sum_{k=0}^\infty \frac{(-it)^k}{M^k} B_k,$$

$$D_k := \frac{1}{k!} \int_0^t \cdots \int_0^t \mathcal{T}\left[H(t_1)\cdots H(t_k)\right] \mathrm{d}^k t,$$

$$B_k := \sum_{0 \le m_k \le \cdots \le m_1 \le M} H\left(m_k \Delta\right) \cdots H\left(m_1 \Delta\right).$$
(A1)

We now prove bounds on the error  $\epsilon_1$  due to truncating the Dyson series at order K.

**Lemma 11.** Let  $H(s): \mathbb{R} \to \mathbb{C}^{N \times N}$  be differentiable on the domain [0,t]. For any  $\epsilon_1 \in [0,2^{-e}]$ , an approximation to the time ordered operator exponential of -iH(s) can be constructed such that

$$\left\| \mathcal{T} \left[ e^{-i \int_0^t H(s) ds} \right] - \sum_{k=0}^K (-i)^k D_k \right\| \le \epsilon_1,$$

if we take

1.
$$K \ge \left[ -1 + \frac{2\ln(1/\epsilon_1)}{\ln\ln(1/\epsilon_1) + 1} \right]$$

2.
$$\max_{s} ||H(s)||t < \ln 2$$

*Proof.* We start by bounding  $||D_k||$ .

$$||D_k|| = \frac{1}{k!} \left| \left| \int_0^t \cdots \int_0^t \mathcal{T}[H(t_1) \cdots H(t_k)] d^k t \right| \le \frac{1}{k!} \left| \left| \int_0^t \cdots \int_0^t \prod_{j=1}^k ||H(t_j)|| d^k t \right| \right| \le \frac{(t \max_s ||H(s)||)^k}{k!}.$$
 (A2)

At this point, the proof is identical to the time-independent case as  $\max_s ||H(s)||$  is independent of time. Thus using Stirling's approximation and assuming  $K \ge 2 \max_s ||H(s)|| |t|$ ,

$$\epsilon_{1} = \left\| \mathcal{T} \left[ e^{-i \int_{0}^{t} H(s) ds} \right] - \sum_{k=0}^{K} (-i)^{k} D_{k} \right\| \leq \sum_{k=K+1}^{\infty} \|D_{k}\| \leq \sum_{k=K+1}^{\infty} \frac{(t \max_{s} \|H(s)\|)^{k}}{k!} \\
\leq \frac{(t \max_{s} \|H(s)\|)^{K+1}}{(K+1)!} \sum_{k=K+2}^{\infty} (1/2)^{k-K-1} = \frac{(t \max_{s} \|H(s)\|)^{K+1}}{(K+1)!} \\
\leq \left( \frac{te \max_{s} \|H(s)\|}{K+1} \right)^{K+1} \tag{A3}$$

Now we find that this in turn is less than  $\epsilon_1$  if  $\max_s ||H(s)|| te < \min\{\ln(1/\epsilon_1), e \ln 2\} \le 1$  given that  $\epsilon_1 \le 2^{-e}$  and

$$K \ge \max\left\{-1 + \frac{\ln(1/\epsilon_1)}{W\left(\frac{\ln(1/\epsilon_1)}{\max_s \|H(s)\|te}\right)}, 2\max_s \|H(s)\||t|\right\},\tag{A4}$$

where W is the Lambert-W function. Using the fact that for  $x \ge 1$ ,  $W(x) \ge (\ln(x) + 1)/2$  and  $\ln(e \ln 2) < 1$  we obtain the simpler bound

$$K = \left[ -1 + \frac{2\ln(1/\epsilon_1)}{\ln\ln(1/\epsilon_1) + 1} \right] \in \mathcal{O}\left(\frac{\ln(1/\epsilon_1)}{\ln\ln(1/\epsilon_1)}\right). \tag{A5}$$

We now prove bounds on the error  $\epsilon_2$  from approximating the Dyson series with its Riemann sum.

**Lemma 12.** Let  $H(s): \mathbb{R} \mapsto \mathbb{C}^{N \times N}$  be differentiable on the domain [0,t]. Let us also define the quantities  $\langle \|\dot{H}\| \rangle := \frac{1}{t} \int_0^t \left\| \frac{\mathrm{d} H(s)}{\mathrm{d} s} \right\| \mathrm{d} s$ . For integer  $K \geq 0$  and  $\epsilon_2 > 0$ ,

$$\left\| \sum_{k=0}^{K} (-i)^k D_k - \sum_{k=0}^{K} \left( -i \frac{t}{M} \right)^k B_k \right\| \le \epsilon_2,$$

by choosing any M such that

1.
$$M \ge \frac{t^2}{\epsilon_2} 4e^{\max_s \|H(s)\|t} \left( \langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2 \right),$$

2.
$$M \ge K^2$$
.

*Proof.* We first expand the time-ordered evolution operator using the Dyson series. We then examine the error incurred in evaluating a given order of the Dyson series for a small hypercubic region of side-length  $\Delta = t/M$ . We then upper bound the maximum number of such hypercubes within the allowed volume and use the triangle inequality to argue that the error is the product of the number of such hypercubes and the maximum error per hypercube.

Since H(s) is a differentiable function it holds from Taylor's theorem that for any  $\delta \ll 1$  and computational basis states  $|x\rangle, |y\rangle$ ,

$$\langle x|H(s+\delta)|y\rangle = \langle x|H(s)|y\rangle + \delta\langle x|\dot{H}(s)|y\rangle + o(\max_{s} ||\dot{H}(s)||_{\max}\delta). \tag{A6}$$

Since computational basis states form a complete orthonormal basis it follows through norm inequalities that

$$H(s+\delta) = H(s) + \delta \dot{H}(s) + o(\|\dot{H}(s)\|_{\text{max}} N^2 \delta).$$
 (A7)

We then have from Taylor's theorem and the triangle inequality that

$$||H(s+\delta) - H(s)|| = \left\| \sum_{j=1}^{r} [H(s+j\delta/r) - H(s+[j-1]\delta/r)] \right\|$$

$$\leq \left\| \sum_{j=1}^{r} \dot{H}(s+[j-1]\delta/r)\delta/r \right\| + r \left[ o(\max_{s} ||\dot{H}(s)||_{\max} N^{2}\delta/r) \right]$$

$$\leq \int_{0}^{\delta} ||\dot{H}(s)||_{ds} + r \left[ o(\max_{s} ||\dot{H}(s)||_{\max} N^{2}\delta/r) \right]. \tag{A8}$$

Since this equation holds for all r, it also holds in the limit as r approaches infinity. Therefore

$$||H(s+\delta) - H(s)|| \le \int_0^\delta ||\dot{H}(s)|| ds.$$
 (A9)

Next, let us consider the error in approximating the integral over a hypercube to lowest order and let us define the hypercube to be C with  $x_1, \ldots, x_q$  being the corner of the hypercube with smallest norm. First note that in general if  $A_j$  and  $B_j$  are a sequence of bounded operators and  $\|\cdot\|$  is a sub-multiplicative norm then it is straight forward to show using an inductive argument that for all positive integer q.

$$\left\| \prod_{j=1}^{q} A_j - \prod_{j=1}^{q} B_j \right\| \le \sum_{k=1}^{q} \left( \prod_{j=1}^{k-1} \|A_j\| \right) \|A_k - B_k\| \left( \prod_{j=k+1}^{q} \|B_j\| \right). \tag{A10}$$

By applying this in combination with Eq. (A9) to region C, the error induced is

$$\left\| \int_{C} H(x_{1} + y_{1}) \cdots H(x_{q} + y_{q}) d^{q}y - \Delta^{q} \prod_{j=1}^{q} H(x_{j}) \right\| \leq \int_{C} \left\| \prod_{j=1}^{q} H(x_{j} + y_{j}) - \prod_{j=1}^{q} H(x_{j}) \right\| dy^{q},$$

$$\leq \sum_{k=1}^{q} \left( \prod_{j=1}^{k-1} \int_{0}^{\Delta} \|H(x_{j} + s)\| ds \right) \left( \int_{0}^{\Delta} \int_{0}^{s} \|\dot{H}(x_{k} + y)\| dy ds \right) \left( \prod_{j=k+1}^{q} \int_{0}^{\Delta} \|H(x_{j})\| ds \right)$$

$$\leq \sum_{k=1}^{q} \left( \prod_{j=1}^{k-1} \int_{0}^{\Delta} \|H(x_{j} + s)\| ds \right) \left( \int_{0}^{\Delta} \int_{0}^{s} \|\dot{H}(x_{k} + y)\| dy ds \right) \left( \prod_{j=k+1}^{q} \int_{0}^{\Delta} \alpha ds \right)$$

$$\leq (\alpha)^{q-1} \Delta \sum_{k=1}^{q} \left( \prod_{j\neq k}^{q} \int_{0}^{\Delta} ds \right) \left( \int_{0}^{\Delta} \|\dot{H}(x_{k} + s)\| ds \right)$$
(A11)

where  $\alpha := \max_{s} ||H(s)||$ .

There are two regions in the problem. The first region, which we call the bulk, is the region that satisfies all the constraints of the problem namely bulk :=  $\{(t_1, \ldots, t_q) : \lfloor t_1/\Delta \rfloor > \cdots > \lfloor t_q/\Delta \rfloor \}$ . Thus for any index  $x_1, \cdots, x_q$  to a hypercube in the bulk, the ordering of terms  $H(x_1 + t_1) \cdots H(x_q + t_q)$  in the integrand of Eq. (A11) is fixed. The second region is called the boundary which is the region in which the hypercubes used in the Riemann sum would stretch outside the allowed region for the integral. Since we approximate the integral to be zero on all hypercubes that intersect the boundary, the maximum error in the approximation is the maximum error that the discrete approximation to the integrand can take within the region scaled to the volume of the corresponding region.

Finally we have from Eq. (A11) that the contribution to the error from integration over the bulk of the simplex is

$$\sum_{\substack{\vec{x} \in \{0, \Delta, \dots, (M-1)\Delta\}^q \\ x_1 < x_2 < \dots < x_q}} \left\| \int_C H(x_1 + t_1) \dots H(x_q + t_q) d^q t - \Delta^q \prod_{j=1}^q H(x_j) \right\| \\
\leq \sum_{\substack{\vec{x} \in \{0, \Delta, \dots, (M-1)\Delta\}^q \\ x_1 < x_2 < \dots < x_q}} (\alpha)^{q-1} \Delta \sum_{k=1}^q \left( \prod_{j \neq k} \int_0^\Delta ds \right) \left( \int_0^\Delta \|\dot{H}(x_k + s)\| ds \right)$$

In order to understand how the error scales let us examine the partial sum over  $x_1$  for fixed k > 1 is

$$\sum_{x_{2},...,x_{q}} \sum_{x_{1}=0}^{x_{2}-1} \int_{0}^{\Delta} \|\dot{H}(x_{1}+s)\| ds \left[ (\alpha)^{q-1} \Delta \left( \prod_{j\neq k}^{q} \int_{0}^{\Delta} ds \right) \left( \int_{0}^{\Delta} \|\dot{H}(x_{k}+s)\| ds \right) \right] \\
\leq \sum_{x_{2},...,x_{q}} \int_{0}^{x_{2}\Delta} \|\dot{H}(s)\| ds \left[ (\alpha)^{q-1} \Delta \left( \prod_{j\neq k}^{q} \int_{0}^{\Delta} \|H(x_{j}+s)\| ds \right) \left( \int_{0}^{\Delta} \|\dot{H}(x_{k}+s)\| ds \right) \right]. \tag{A13}$$

The integral then takes exactly the same form as the original integral and so by repeating the argument q-1 times it is easy to see, even in the case where k=1, that

$$\sum_{\substack{\vec{x} \in \{0, \Delta, \dots, (M-1)\Delta\}^q \\ x_1 < x_2 < \dots < x_q}} (\alpha)^{q-1} \Delta \sum_{k=1}^q \left( \prod_{j \neq k}^q \int_0^\Delta ds \right) \left( \int_0^\Delta \|\dot{H}(x_k + s)\| ds \right) \\
\leq (\alpha)^{q-1} \Delta \sum_{k=1}^q \left( \prod_{j \neq k}^q \int_0^{x_{j+1}\Delta} ds \right) \left( \int_0^{x_{k+1}\Delta} \|\dot{H}(s)\| ds \right) \leq \frac{(\alpha t)^{q-1}}{[q-1]!} \Delta \int_0^t \|\dot{H}(s)\| ds, \tag{A14}$$

where we have used the definition that  $x_{q+1} := M = t/\Delta$  and the fact that  $\int_0^x \|\dot{H}(s)\| ds$  is a monotonically increasing function of x. Thus the contribution to the error from the boundary is at most

$$\sum_{q=1}^{K} \frac{(\alpha t)^{q-1}}{[q-1]!} \Delta \int_{0}^{t} \|\dot{H}\|(s) ds \leq \sum_{q=1}^{\infty} \frac{(\alpha)^{q-1}}{[q-1]!} \Delta \int_{0}^{t} \|\dot{H}(s)\| ds = e^{\alpha t} \Delta \int_{0}^{t} \|\dot{H}(s)\| ds. \tag{A15}$$

Next we need to estimate the volume of the boundary. If a point is on the boundary then by definition there exists at least one  $t_j$  such that  $\lfloor t_j/\Delta \rfloor = \lfloor t_{j+1}/\Delta \rfloor$  taking  $t_0 = t$ . All other values are consistent with points within the bulk. It is then straight forward to see that (after relabeling the indexes for the summation) that the volume can be expressed as the sum over all possible choices of such sums with at least one matched index. If we further assume that  $q^2 \Delta \max_s \|H(s)\|/[\alpha t] \le \ln(2)$  then we have the following upper bound on boundary contribution to the error in the Dyson series:

$$\int \prod_{j=1}^{q} \|H(t_q)\| \delta_{t \in \text{bdy}} dt^q \leq \sum_{p=1}^{q} \Delta^q \max_s \|H(s)\|^p \alpha^{q-p} \binom{q}{p} \sum_{j_1=1}^{t/\Delta} \sum_{j_2=1}^{j_1-1} \cdots \sum_{j_{q-p}=1}^{j_{q-p}-1-1} 1$$

$$= \Delta^q \alpha^q \sum_{p=1}^{q} \max_s \|H(s)\|^p \alpha^{-p} \binom{q}{p} \binom{t/\Delta}{q-p}.$$

$$\leq \Delta^q \alpha^q \sum_{p=1}^{q} \max_s \|H(s)\|^p \alpha^{-p} \frac{(t/\Delta)^q}{q!p!} \binom{q^2 \Delta}{t}^p$$

$$= \frac{t^q \alpha^q}{q!} \sum_{p=1}^{q} \frac{1}{p!} \left( \frac{q^2 \Delta \max_s \|H(s)\|}{\alpha t} \right)^p$$

$$\leq \frac{t^q \alpha^q}{q!} \left( \frac{q^2 \Delta \max_s \|H(s)\|}{\alpha t} \right) \sum_{p=0}^{\infty} \frac{1}{p!} \left( \frac{q^2 \Delta \max_s \|H(s)\|}{\alpha t} \right)^p$$

$$\leq \frac{2q(t\alpha)^{q-1}}{(q-1)!} \left( \Delta \max_s \|H(s)\| \right)$$
(A16)

Note that when q=1, there is no boundary contribution. Using the fact that  $q/(q-1) \le 2$ ,  $\forall q \ge 2$ , this upper bound

$$\int \prod_{i=1}^{q} \|H(t_q)\| \delta_{t \in \text{bdy}} dt^q \le \frac{4\Delta \max_{s} \|H(s)\| (\alpha t)^{q-1}}{(q-2)!}$$
(A17)

It then follows from summing Eq. (A17) that the error is

$$\delta_{\text{bdy}} \le \sum_{q=1}^{K} \int \prod_{j=1}^{q} \|H(t_q)\| \delta_{t \in \text{bdy}} dt^q \le \sum_{q=2}^{\infty} \frac{4\Delta \max_{s} \|H(s)\| (\alpha t)^{q-1}}{(q-2)!} \le 4\Delta \alpha t \max_{s} \|H(s)\| e^{\alpha t}. \tag{A18}$$

By adding this result to that of Eq. (A15)

$$\sum_{q=1}^{K} \|D_q - \Delta^q B_q\| \le \delta_{\text{bulk}} + \delta_{\text{bdy}} \le 4\Delta t e^{\max_s \|H(s)\|t} (\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2)$$
(A19)

It follows from elementary algebra that this total error is at most  $\epsilon_2$  if

$$\Delta \le \frac{\epsilon_2}{4te^{\max_s \|H(s)\|t} [\langle \|\dot{H}\|\rangle + \max_s \|H(s)\|^2]}.$$
(A20)

Expressed in terms of the number of points  $M = \frac{t}{\Delta}$ , the total error is at most  $\epsilon_2$  if choose any M such that

$$M \ge \frac{t^2}{\epsilon_2} 4e^{\max_s \|H(s)\|^t} [\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2]$$
(A21)

The final bound on M quoted immediately follows from  $\frac{q^2\Delta}{\alpha t} \max_s \|H(s)\| \le \ln(2) \Rightarrow K \le \sqrt{\ln(2)M} \le \sqrt{M}$ .

Now that we have proved the necessary results regarding the error in the truncated Dyson series simulation, we are now ready to prove Lemma 5, which we restate for convenience.

**Lemma 5** (Error from truncating and discretizing the Dyson series). Let  $H(s):[0,t]\mapsto\mathbb{C}^{N\times N}$  be differentiable and  $\langle \|\dot{H}\|\rangle:=\frac{1}{t}\int_0^t \left\|\frac{\mathrm{d}H(s)}{\mathrm{d}s}\right\|\mathrm{d}s$ . For any  $\epsilon\in(0,2^{1-e}]$ , an approximation to the time ordered operator exponential of -iH(s) can be constructed such that

$$\left\| \mathcal{T} \left[ e^{-i \int_0^t H(s) ds} \right] - \sum_{k=0}^K \left( -it/M \right)^k B_k \right\| \le \epsilon, \quad B_k = \sum_{0 \le m_1 < \dots < m_k < M} H\left( m_k t/M \right) \cdots H\left( m_1 t/M \right),$$

if we take all the following are true.

1.  $\max_{s} ||H(s)|| t \leq \ln 2$ .

2.
$$K = \left[ -1 + \frac{2\ln(2/\epsilon)}{\ln\ln(2/\epsilon) + 1} \right]$$

3.
$$M \ge \max \left\{ \frac{16t^2}{\epsilon} \left( \langle ||\dot{H}|| \rangle + \max_s ||H(s)||^2 \right), K^2 \right\}$$
.

*Proof.* This is proven by combining two intermediate results using a triangle inequality. The approximation error is upper-bounded by

$$\left\| \mathcal{T} \left[ e^{-i \int_{0}^{t} H(s) ds} \right] - \sum_{k=0}^{K} \left( -i \frac{t}{M} \right)^{k} B_{k} \right\| = \left\| \mathcal{T} \left[ e^{-i \int_{0}^{t} H(s) ds} \right] - \sum_{k=0}^{K} (-i)^{k} D_{k} + \sum_{k=0}^{K} (-i)^{k} D_{k} - \sum_{k=0}^{K} \left( -i \frac{t}{M} \right)^{k} B_{k} \right\|$$

$$\leq \underbrace{\left\| \mathcal{T} \left[ e^{-i \int_{0}^{t} H(s) ds} \right] - \sum_{k=0}^{K} (-i)^{k} D_{k} \right\|}_{E_{1}} + \underbrace{\left\| \sum_{k=0}^{K} (-i)^{k} D_{k} - \sum_{k=0}^{K} \left( -i \frac{t}{M} \right)^{k} B_{k} \right\|}_{E_{2}} \leq \epsilon.$$
(A22)

We choose the errors in both cases to obey  $\epsilon_1 = \epsilon/2$  and  $\epsilon_2 = \epsilon/2$ . The result then follows by taking the most restrictive of the assumptions of Lemma 11 and Lemma 12.

## Appendix B: Truncated Dyson series algorithm with low space overhead

The quantum algorithm described by Theorem 3 applies an  $\epsilon$ -approximation  $\tilde{U} = \sum_{k=0}^K \frac{(-it)^k}{M^k} B_k$  of the time-ordered evolution operator  $\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right]$ , where the truncation order K and the number of discretization points M are given by Lemma 5.

The simulation algorithm then proceeds in three steps. First, we construct a sequence of K unitary operators  $U_1, U_2, \dots, U_K$ , that encode some matrix  $H_k$  such that  $H_k \dots H_2 H_1 \propto B_k$  implements the  $k^{\text{th}}$  term of the Dyson series. We call DYS<sub>K</sub> the unitary that applies this sequence of unitaries  $U_1 \dots U_k$  controlled on an index state  $|k\rangle_b$ . A naive implementation of this idea, as worked out in Appendix C, requires the K-fold duplication of registers a and d of the oracle HAM-T. We present a compression gadget described by Lemma 13 avoids this overhead. Second, we take a linear combination of  $B_k$  to apply  $\tilde{U}$  with some success probability on any input state to the s register. As  $B_K$  contains products of K Hamiltonians, this step requires K queries to HAM-T. Third, since  $\tilde{U}$  is  $\epsilon$ -close to unitary, we apply oblivious amplitude amplification [8] to boost this probability to  $1 - \mathcal{O}(\epsilon)$ .

We now prove the compression gadget, which is followed by a proof Theorem 3.

**Lemma 13** (Compression gadget). Let  $\{U_k : k \in [K]\}$  be a set of K unitaries that encode matrices  $H_k \in \mathbb{C}^{2^{n_s} \times 2^{n_s}}$  such that

$$(\langle 0|_a \otimes \mathbb{1}_s) U_k(|0\rangle_a \otimes \mathbb{1}_s) = H_k, \quad ||H_k|| \le 1, \quad |0\rangle_a \in \mathbb{C}^{2^{n_a}}. \tag{B1}$$

Then there exists a quantum circuit V such that on input states spanned by  $\{|k\rangle_b : k \in \{0, \dots, K\}\}$ ,

$$(\langle 0|_{ac} \otimes \mathbb{1}_s)V(|0\rangle_{ac} \otimes \mathbb{1}_s) = |0\rangle\langle 0|_b \otimes \mathbb{1}_s + \sum_{k=1}^K |k\rangle\langle k|_b \otimes \left(\prod_{j=1}^k H_j\right), \quad |0\rangle_a \in \mathbb{C}^{2^{n_a}}, \quad |k\rangle_b \in \mathbb{C}^{2^{n_b}}, \quad |0\rangle_c \in \mathbb{C}^{2^{n_c}},$$
(B2)

where the number of qubits  $n_b \in \mathcal{O}(n_c) = \mathcal{O}(\log(K))$ . The cost of V is one query each to controlled-controlled- $U_k$ , and  $\mathcal{O}(K(n_a + \log(K)))$  additional primitive quantum gates.

*Proof.* Though binary control logic for this sequence is trivial when  $H_k$  is unitary, the complication here is that  $H_k$  is in general non-unitary and so the probability of successfully measuring  $|0\rangle_a$  is less than one. Any other measurement outcome corresponds failure as it applies on register a an operator that is not  $H_k$ . This complication is overcome by introducing two more registers b, c of size  $\mathcal{O}(\log(K))$  qubits that coherently count the number of successful measurements, and then applying  $U_k$  conditional on there being no failures.

Let the counter register b represent an  $n_b$ -bit integer  $l_b = \sum_{r=0}^{n_b-1} 2^r q_r$  in the number state  $|l_b\rangle_b := |q_0q_1\cdots q_{n_b,c-1}\rangle_b$ , where  $q_r \in \{0,1\}$ , and similarly for the counter register c. The size of these integers are determined by  $n_b = n_c + 1 = \lceil \log_2(K+1) \rceil + 1$ . The unitaries  $U_j$  will be applied conditional on both the leading bits  $q_{n_c-1} = 0$  and  $q_{n_b-1} = 0$ , that is

$$CC-U_k := I^{\otimes n_b + n_c - 2} \otimes \left( |0\rangle \langle 0|_{b_{n_b - 1}} \otimes |0\rangle \langle 0|_{c_{n_c - 1}} \otimes U_k + \cdots \right).$$
(B3)

Consider the circuit in Fig. 2. There, we apply CC- $U_k$ , then increment k by one, decrement  $l_c$  by one conditional on the a register not being in the  $|0\rangle_a$  state, and decrement  $l_b$  by one conditional on the a register being in the  $|0\rangle_a$  state. This is accomplished by multiply-controlled modular addition

$$ADD_{ca} = ADD_{b}^{\dagger} \otimes \mathbb{1}_{c} \otimes |0\rangle\langle 0|_{a} + \mathbb{1}_{b} \otimes ADD_{c}^{\dagger} \otimes \sum_{l=1}^{2^{n_{a}}-1} |l\rangle\langle l|_{a},$$

$$ADD_{b} = \sum_{l=0}^{2^{n_{b}}-1} |l+1 \mod 2^{n_{b}}\rangle\langle l|_{b}, \quad ADD_{c} = \sum_{l=0}^{2^{n_{c}}-1} |l+1 \mod 2^{n_{c}}\rangle\langle l|_{c}.$$
(B4)

As we add integers of size  $\mathcal{O}(K)$ , each application of modular addition costs  $\mathcal{O}(\log(K))$  primitive gates and requires  $\mathcal{O}(\log(K))$  qubits [22]. Implementing the multiple controls costs  $\mathcal{O}(n_a)$  primitive gates and up to  $n_a$  extra qubits. Restricted to input states  $|0\rangle_a|l_b\rangle_b|0\rangle_c$ , where  $l_b \in \{2^{n_b}-1,0,1,2,3,\cdots,K-1\}$ , this implements V. For example,

![](_page_22_Figure_1.jpeg)

FIG. 2. Quantum circuit representations of the gadget V for probabilistically applying a sequence of operators  $H_k \cdots H_2 H_1$ , encoded in  $(\langle 0|_a \otimes \mathbb{1}_s) U_k(|0\rangle_a \otimes \mathbb{1}_s) = H_k$ , controlled on number state  $|k\rangle_b$ ,  $k \in \{0, 1, \dots, K\}$ . Horizontal lines without a backslash depict single-qubit registers. Filled circles depict a unitary controlled by the  $|0\rangle \cdots |0\rangle$  state.

consider the evolution of an input state  $|0\rangle_a|1\rangle_b|0\rangle_c|\psi\rangle_s$  for K=3.

$$|0\rangle_{a}|1\rangle_{b}|0\rangle_{c}|\psi\rangle_{s} \underset{CC^{-}U_{1}}{\longrightarrow} |0\rangle_{a}|1\rangle_{b}|0\rangle_{c}H_{1}|\psi\rangle_{s} + |0^{\perp,1}\rangle_{a}|2\rangle_{b}|0\rangle_{c} \cdots$$

$$\underset{ADD_{ca}}{\longrightarrow} |0\rangle_{a}|0\rangle_{b}|0\rangle_{c}H_{1}|\psi\rangle_{s} + |0^{\perp,1}\rangle_{a}|2\rangle_{b}|2^{n_{c}} - 1\rangle_{c} \cdots$$

$$\underset{CC^{-}U_{2}}{\longrightarrow} |0\rangle_{a}|0\rangle_{b}|0\rangle_{c}H_{2}H_{1}|\psi\rangle_{s} + |0^{\perp,2}\rangle_{a}|1\rangle_{b}|0\rangle_{c} \cdots + |0^{\perp,1}\rangle_{a}|2\rangle_{b}|2^{n_{c}} - 1\rangle_{c} \cdots$$

$$\underset{ADD_{ca}}{\longrightarrow} |0\rangle_{a}|2^{n_{b}} - 1\rangle_{b}|0\rangle_{c}H_{2}H_{1}|\psi\rangle_{s} + |0^{\perp,2}\rangle_{a}|1\rangle_{b}|2^{n_{c}} - 1\rangle_{c} \cdots + |0^{\perp,1}\rangle_{a}|2\rangle_{b}|2^{n_{c}} - 2\rangle_{c} \cdots$$

$$\underset{ADD_{ca}}{\longrightarrow} |0\rangle_{a}|2^{n_{b}} - 1\rangle_{b}|0\rangle_{c}H_{2}H_{1}|\psi\rangle_{s} + |0^{\perp,2}\rangle_{a}|1\rangle_{b}|2^{n_{c}} - 1\rangle_{c} \cdots + |0^{\perp,1}\rangle_{a}|2\rangle_{b}|2^{n_{c}} - 2\rangle_{c} \cdots$$

$$\underset{ADD_{ca}}{\longrightarrow} |0\rangle_{a}|2^{n_{b}} - 2\rangle_{b}|0\rangle_{c}H_{2}H_{1}|\psi\rangle_{s} + |0^{\perp,2}\rangle_{a}|1\rangle_{b}|2^{n_{c}} - 2\rangle_{c} \cdots + |0^{\perp,1}\rangle_{a}|2\rangle_{b}|2^{n_{c}} - 3\rangle_{c} \cdots$$

$$\underset{ADD^{K}}{\longrightarrow} |0\rangle_{a}|1\rangle_{b}|0\rangle_{c}H_{2}H_{1}|\psi\rangle_{s} + \cdots .$$

In the above, subtracting from 0 results in the largest possible integer, hence the leading bit becomes  $q_{n_b-1}=1$ , and similarly for  $q_{n_c-1}=1$ . As a result, the controls in Eq. (B3) do not apply  $U_k$ . By choosing the largest integer representable by the b register to be at least two times of K, we also ensure that this leading bit is set to 1, it will remain in the same state after the at most K subtractions. Note that Eq. (B2) applies  $H_k \cdots H_1$  controlled on  $|k\rangle_b$ , whereas Eq. (B5) applies  $H_{l_b} \cdots H_1$  controlled on  $|l_b-1\rangle_b$  – we simply relabel  $k=l_b-1 \mod 2^{n_b}$ .

Before proceeding to the proof of Theorem 3 we need to use a well-known result called 'robust oblivious amplitude amplification', restated below for convenience.

**Lemma 14** (Robust oblivious amplitude amplification [8]). Let V, U be unitary and let  $\tilde{U}$  be an arbitrary matrix such that  $||U - \tilde{U}|| \in \mathcal{O}(\epsilon)$ , and  $(\langle 0|_a \otimes \mathcal{I}_s)V(|0\rangle_a \otimes \mathcal{I}_s) = \frac{\tilde{U}}{2}$ . Let  $W = -V \cdot (\text{REF} \otimes \mathcal{I}_s) \cdot V^{\dagger} \cdot (\text{REF} \otimes \mathcal{I}_s) \cdot V$ , where  $\text{REF} = \mathcal{I}_a - 2|0\rangle\langle 0|_a$ . Then  $||(\langle 0|_a \otimes \mathcal{I}_s)W(|0\rangle_a \otimes \mathcal{I}_s) - U|| \in \mathcal{O}(\epsilon)$ .

The proof of Theorem 3 follows.

**Theorem 3** (Hamiltonian simulation by a truncated Dyson series). Let  $H(s):[0,t]\to\mathbb{C}^{2^{n_s}\times 2^{n_s}}$ , let it be promised that  $\max_s\|H(s)\|\leq \alpha$  and  $\langle\|\dot{H}\|\rangle=\frac{1}{t}\int_0^t\left\|\frac{\mathrm{d}H(s)}{\mathrm{d}s}\right\|$  ds and assume  $M\in\mathcal{O}\left(\frac{t^2}{\epsilon}\left(\langle\|\dot{H}\|\rangle+\max_s\|H(s)\|^2\right)\right)$  in Definition 2. For all  $t\in[0,\frac{1}{2\alpha}]$  and  $\epsilon>0$ , an operation W can be implemented such that  $\left\|W-\mathcal{T}\left[e^{-i\int_0^tH(s)\mathrm{d}s}\right]\right\|\leq\epsilon$  with failure probability  $\mathcal{O}(\epsilon)$  with the following costs.

- 1. Queries to HAM-T:  $\mathcal{O}\left(\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$
- 2. Qubits:  $n_s + \mathcal{O}\left(n_a + \log\left(\frac{t^2}{\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right)$ ,
- 3. Primitive gates:  $\mathcal{O}\left(\left(n_a + \log\left(\frac{t^2}{\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right) \frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$ .

*Proof of Theorem 3.* The unitary DYS<sub>K</sub>, as defined in Eq. (B6), may be implemented through Lemma 13 provided that we find a sequence  $\{U_k\}$  such that  $H_k \cdots H_2 H_1 \propto B_k$ . – in other words,

$$(\langle 0|_{ac,\text{others}} \otimes \mathbb{1}_{bs}) \operatorname{DYS}_K(|0\rangle_{ac,\text{others}} \otimes \mathbb{1}_{bs}) = \sum_{k=0}^K |k\rangle\langle k|_b \otimes \gamma_k B_k,$$
(B6)

where 'others' represent registers with size independent of K, and  $\gamma_k$  is a scaling factor depends on the choice of  $U_k$ . This sequence is obtained by combining three matrices. First, a unitary matrix U that prepares a uniform superposition  $U|0\rangle_d = \sum_{m=0}^{M-1} \frac{1}{\sqrt{M}} |m\rangle_d$ . Second, the block-diagonal matrix

$$D = \sum_{m=0}^{M-1} |m\rangle\langle m|_d \otimes H(\Delta m), \quad \Delta = t/M,$$
(B7)

implemented by HAM-T. Third, a strictly upper-triangular matrix  $G \in \mathbb{R}^{M \times M}$  with elements

$$G_{ij} = \begin{cases} \frac{1}{M}, & i < j, \\ 0, & \text{otherwise,} \end{cases} G = \frac{1}{M} \sum_{i=0}^{M-1} \sum_{j=i+1}^{M-1} |i\rangle\langle j|_d.$$
 (B8)

The non-unitary triangular operator G is implemented by using an integer comparator COMP acting on registers d, e, f consisting of  $n_d = n_e \in \mathcal{O}(\log(M))$  and  $n_f = 1$  qubits, and thus costs  $\mathcal{O}(\log(M))$  primitive gates. For any input number state index  $|j\rangle_d$ , let us compare j with a uniform superposition state  $\sum_{i=0}^{M-1} \frac{1}{\sqrt{M}} |i\rangle_e$ . Conditional on  $i \geq j$ , the comparator perform a NOT gate on register f. We then swap registers d, e, and unprepare the uniform superposition. On input  $|j\rangle_d |0\rangle_e |0\rangle_f$ , this implements the sequence

$$|j\rangle_{d}|0\rangle_{e}|0\rangle_{f} \xrightarrow[U \text{ on } e]{} \frac{|j\rangle_{d}}{\sqrt{M}} \sum_{i=0}^{M-1} |i\rangle_{e}|0\rangle_{f} \xrightarrow[COMP]{} \frac{|j\rangle_{d}}{\sqrt{M}} \sum_{i=0}^{M-1} |i\rangle_{e}|i \geq j\rangle_{f} \xrightarrow[SWAP_{de}]{} \frac{|j\rangle_{e}}{\sqrt{M}} \sum_{i=0}^{M-1} |i\rangle_{d}|i \geq j\rangle_{f}$$

$$\xrightarrow[U^{\dagger} \text{ on } e]{} \frac{1}{M} \sum_{i=0}^{M-1} |i\rangle_{d}|0\rangle_{e}|i \geq j\rangle_{f} + \cdots,$$
(B9)

where  $|i \geq j\rangle_f = |1\rangle_f$  if  $i \geq j$  and is  $|0\rangle_f$  if i < j. This defines the following circuit LT that encodes G using  $\mathcal{O}(\log(M))$  primitive gates.

$$\operatorname{LT} = (\mathbb{1}_{f} \otimes U^{\dagger} \otimes \mathbb{1}_{d}) \cdot (\mathbb{1}_{f} \otimes \operatorname{SWAP}_{de}) \cdot \operatorname{COMP} \cdot (\mathbb{1}_{f} \otimes U \otimes \mathbb{1}_{d}),$$

$$\Rightarrow (\langle 0|_{ef} \otimes \mathbb{1}_{d}) \operatorname{LT}(|0\rangle_{ef} \otimes \mathbb{1}_{d}) = \frac{1}{M} \sum_{i=0}^{M-1} \sum_{j=i+1}^{M-1} |i\rangle\langle j|_{d} = G.$$
(B10)

One may then verify that the terms  $B_k$  are generated by the following sequence

$$\langle 0|_{d}U^{\dagger} \cdot D \cdot U|0\rangle_{d} = \frac{B_{1}}{M} = \frac{1}{M} \sum_{m_{1}=0}^{M-1} H(\Delta m),$$

$$\langle 0|_{d}U^{\dagger} \cdot (D \cdot G) \cdot D \cdot U|0\rangle_{d} = \frac{B_{2}}{M^{2}} = \frac{1}{M^{2}} \sum_{0 \leq m_{1} < m_{2} < M} H(\Delta m_{2}) H(\Delta m_{1}),$$
(B11)

:

$$\langle 0|_d U^{\dagger} \cdot (D \cdot G)^{k-1} \cdot D \cdot U|0\rangle_d = \frac{B_k}{M^k} = \frac{1}{M^k} \sum_{0 \le m_1 < m_2 < \cdots m_j < M} H(\Delta m_j) \cdots H(\Delta m_2) \cdots H(\Delta m_1).$$

Thus we make the choice

$$U_{k} := \begin{cases} (U^{\dagger} \otimes \mathbb{1}_{aefs}) \cdot (\text{HAM-T} \otimes \mathbb{1}_{ef}) \cdot (U \otimes \mathbb{1}_{aefs}), & k = 1, \\ (U^{\dagger} \otimes \mathbb{1}_{aefs}) \cdot (\text{HAM-T} \otimes \mathbb{1}_{ef}) \cdot (\text{LT} \otimes \mathbb{1}_{as}) \cdot (U \otimes \mathbb{1}_{aefs}), & k > 1. \end{cases}$$
(B12)

Combined with Lemma 13, this leads to the circuit of Fig. 3 which implements DYS<sub>K</sub> in Eq. (B6) by identifying 'others' with the d, e and f registers, and recognizing from Eq. (B11) that the scaling factor  $\gamma_k = \frac{1}{M^k}$ . In other words,

$$(\langle 0|_{acdef} \otimes \mathbb{1}_{bs}) \operatorname{DYS}_{K}(|0\rangle_{acdef} \otimes \mathbb{1}_{bs}) = \sum_{k=0}^{K} |k\rangle\langle k|_{b} \otimes \frac{B_{k}}{M^{k}},$$
(B13)

![](_page_24_Figure_1.jpeg)

FIG. 3. Quantum circuit representation of (top) DYS<sub>K</sub> in Eq. (B6), implemented using the compression gadget Lemma 13 depicted in Fig. 2; (bottom, left) a single step of time-evolution by the truncated Dyson series algorithm from Eq. (B15) before oblivious amplitude amplification; (bottom, right) a single step of time-evolution by the truncated Dyson series algorithm from Eq. (B16). Note that when  $\beta = 2$ , a single-round of oblivious amplitude amplification is used.

According to Lemma 13, the number of primitive gates required by DYS<sub>K</sub>, excluding that for the  $U_k$ , is  $\mathcal{O}(K(n_a + n_d + n_e + n_f + \log(K))) = \mathcal{O}(K(n_a + \log(M) + \log(K)))$ .

We then select the desired linear combination of different orders in the Dyson series with the state preparation unitary

$$COEF |0\rangle_b = \frac{1}{\sqrt{\beta}} \sum_{k=0}^K \sqrt{(-it)^k} |k\rangle_b, \quad COEF' |0\rangle_b = \frac{1}{\sqrt{\beta}} \sum_{k=0}^K \sqrt{t^k} |k\rangle_b, \quad \beta = \sum_{j=0}^K t^k \le \sum_{k=0}^\infty t^k = \frac{1}{1-t}, \quad (B14)$$

which can be implemented using  $\mathcal{O}(K)$  primitive gates [17]. In summing the  $t^k$ , we assume that t < 1 for convergence. The resulting unitary  $TDS_{\beta}$ , is defined as follows.

$$TDS_{\beta} := (COEF'^{\dagger} \otimes \mathbb{1}_{acdefs}) \cdot DYS_{K} \cdot (COEF \otimes \mathbb{1}_{acdefs})$$

$$\Rightarrow (\langle 0 | abcdef \otimes \mathbb{1}_{s}) TDS_{\beta} (|0\rangle_{abcdef} \otimes \mathbb{1}_{s}) = \frac{\sum_{k=0}^{K} (-it)^{k} B_{k}}{M^{k} \beta} \approx \frac{\mathcal{T}e^{-i\int_{0}^{t} H(s) ds}}{\beta}.$$
(B15)

Using the provided parameters for  $K \in \mathcal{O}\left(\frac{\log{(1/\epsilon)}}{\log{\log{(1/\epsilon)}}}\right)$  and  $M = \frac{t^2}{\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)$ , the numerator, by Lemma 5, approximates a unitary operation to error  $\mathcal{O}(\epsilon)$ .

The probability of applying this operation can be boosted from  $|\frac{1+\Theta(\epsilon)}{\beta}|^2$  to  $1-\mathcal{O}(\epsilon)$ . If we choose  $t=\Theta(1)\approx 1/2$  to be sufficiently small such that  $\beta=2$ , then a single round of robust oblivious amplitude amplification, outlined in Lemma 14, suffices. This implements a single time-step of the truncated Dyson series algorithm TDS in Fig. 3 as follows.

$$TDS = -TDS_{2} \cdot (REF \otimes \mathbb{1}_{s}) \cdot TDS_{2}^{\dagger} \cdot (REF \otimes \mathbb{1}_{s}) \cdot TDS_{2},$$

$$\Rightarrow \|(\langle 0|_{abcdef} \otimes \mathbb{1}_{s}) TDS(|0\rangle_{abcdef} \otimes \mathbb{1}_{s}) - \mathcal{T}[e^{-i\int_{0}^{t} H(s)ds}]\| \in \mathcal{O}(\epsilon).$$
(B16)

Note that each reflection REF =  $\mathbb{1}_{abcdef} - 2|0\rangle\langle 0|_{abcdef}$  acts on  $n_a + \mathcal{O}(\log(K) + \log(M))$  qubits and therefore costs  $\mathcal{O}(n_a + \log(K) + \log(M))$  gates. If we wish to simulate time-evolution for any  $t \leq \frac{1}{2}$ , this will lead to  $\beta \leq 2$ . In this situation, there are a variety of methods to boost  $\beta$  back to 2. Unlike oblivious amplitude amplification, this

corresponds to decreasing the success probability and is easy to accomplish. For instance, introducing an additional qubit together with a 1 single-qubit rotation may be used as described by [8] to artificially decrease the overlap.

We now tally the query, gate, and qubit complexity. From Fig. 3, the number of HAM-T queries is  $3K \in \mathcal{O}\left(\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$ . The gate complexity is that of REF, COEF, K times of LT, and K times of the multiply-controlled modular addition circuits ADD. This is dominated by the addition circuits, with gate complexity  $\mathcal{O}(K(n_a + \log(M) + \log(K))) = \mathcal{O}(n_a + \log(M) \frac{\log(1/\epsilon)}{\log\log(1/\epsilon)})$  as M has the dominant  $\epsilon$  scaling. The number of qubits in each register is  $n_b = n_c \in \mathcal{O}(\log(K))$ ,  $n_d = n_e \in \mathcal{O}(\log(M))$ , and  $n_f = 1$ . Thus  $n_s + n_a + n_b + n_c + n_d + n_e + n_f = n_s + n_a + \mathcal{O}(\log(K) + \log(M)) = n_s + n_a + \mathcal{O}(\log(M))$ . However, the control logic for multiply-controlled unitaries can require up to a single duplication of the control registers. Thus the qubit complexity is  $n_s + \mathcal{O}(n_a + \log(M))$ . Note that we leave  $n_s$  out of the big- $\mathcal{O}$  set as this register is never duplicated.

## Appendix C: Truncated Dyson series algorithm by duplicating control registers

In this section, we present a quantum algorithm that applies the  $\epsilon$ -approximation  $\tilde{U} = \sum_{k=0}^{\infty} \frac{(-it)^k}{M^k} B_k$  to the time-ordered evolution operator  $\mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right]$ , where the truncation order K and the number of discretization points M are given by Lemma 5. This version is based on the original proposal by [8], and applies the same operator as Theorem 3 with the same query and gate complexity, but has worse space complexity. Our contributions here are rigorous bounds on K and M, and the implementation of a key step not discussed previously – the efficient preparation of a particular quantum state that correctly selects a desired linear combination of time-ordered products of Hamiltonians. This step is non-obvious as the state has  $\mathcal{O}(M!)$  different amplitudes, and in the worst-case would take  $\mathcal{O}(M!)$  gates to create by arbitrary state preparation techniques. The cost of this implementation is captured by the following theorem.

**Theorem 15** (Hamiltonian simulation by a truncated Dyson series with duplicated registers). Let  $H(s): [0,t] \to \mathbb{C}^{2^{n_s} \times 2^{n_s}}$ , let it be promised that  $\max_s \|H(s)\| \le \alpha$  and  $\langle \|\dot{H}\| \rangle = \frac{1}{t} \int_0^t \left\| \frac{\mathrm{d}H(s)}{\mathrm{d}s} \right\| \mathrm{d}s$  and assume that the number of discretization points obeys  $M \in \mathcal{O}\left(\frac{t^2}{\epsilon}\left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)$  in Definition 2. For all  $t \in [0, \frac{1}{2\alpha}]$  and  $\epsilon > 0$ , an operation W can be implemented such that  $\|W - \mathcal{T}\left[e^{-i\int_0^t H(s)\mathrm{d}s}\right]\| \le \epsilon$  with failure probability  $\mathcal{O}(\epsilon)$  with the following costs.

- 1. Queries to HAM-T:  $\mathcal{O}\left(\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$ .
- 2. Qubits:  $n_s + \mathcal{O}\left(\left(n_a + \log \frac{t^2}{\epsilon} \left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right)\right)$ .
- 3. Primitive gates:  $\mathcal{O}\left(\left(n_a + \log \frac{t^2}{\epsilon} \left(\langle \|\dot{H}\| \rangle + \max_s \|H(s)\|^2\right)\right) \frac{\log \left(1/\epsilon\right)}{\log \log \left(1/\epsilon\right)}\right)$ .

*Proof.* Let HAM-T<sub>K</sub> be a unitary that acts jointly on registers  $s, \vec{a}, \vec{b}, c, \vec{d}$ . This unitary is defined to apply products of Hamiltonians

$$(\langle 0|_{\vec{a}} \otimes \mathbb{1}_{s}) \operatorname{HAM-T}_{K}(|0\rangle_{\vec{a}} \otimes \mathbb{1}_{s})$$

$$:= \left( \sum_{k=0}^{K} |k\rangle\langle k|_{\vec{b}} \otimes \left( \sum_{\vec{m} \in [M]^{k}} |\vec{m}\rangle\langle \vec{m}|_{d_{1}\cdots d_{k}} \otimes \mathbb{1}_{d_{k+1}\cdots d_{K}} \otimes \left( \prod_{j=1}^{k} H(m_{j}\Delta) \right) \right) + \cdots \right) \otimes \operatorname{SWAP}_{c}, \quad (C1)$$

where SWAP<sub>c</sub> swaps the two qubits of register c, and a possible implementation is depicted in Fig. 4. Note that we only define the action of HAM-T<sub>K</sub> for input states to register  $\vec{b}$  that are spanned by basis states of the unary encoding  $|k\rangle_{\vec{b}} = |0\rangle^{\otimes k}|1\rangle^{\otimes K-k}$ , which determines the number of terms in the product. As seen in the figure, HAM-T<sub>K</sub> makes K queries to HAM-T and copies the a, b, and d registers K times.

$$|s_k\rangle_{\vec{d}} := \sqrt{\frac{k!(M-k)!}{M!}} \left( \sum_{0 \le m_1 < m_2 < \dots < m_k < M} |\vec{m}\rangle_{d_1 \dots d_k} \right) |0\rangle_{d_{k+1} \dots d_K}. \tag{C2}$$

![](_page_26_Figure_1.jpeg)

FIG. 4. Quantum circuit representation of (top, left)  $\text{HAM}_L$  in Eq. (C1); (top, right)  $\text{DYS}_K$  in Eq. (C4); (bottom, left) a single step of time-evolution by the truncated Dyson series algorithm from Eq. (C6) before oblivious amplitude amplification; (bottom, right) a single step of time-evolution by the truncated Dyson series algorithm with duplicated ancilla registers. Note that when  $\beta = 2$ , a single-round of oblivious amplitude amplification is used.

This state is easy to prepare when k = 1 – there, it is simply a uniform superposition over M number states, and costs  $\mathcal{O}(\log M)$  gates. Otherwise, naive methods based on rejection sampling have some success probability  $|\gamma_k|^2$  that decreases exponentially with large k. Let  $\text{PREP}_K$  be one such unitary that prepares  $|s_k\rangle_{\vec{d}}$  on measurement outcome  $|00\rangle_c$ .

$$PREP_K |k\rangle_{\vec{b}} |0\rangle_{c\vec{d}} := |k\rangle_{\vec{b}} \left(\gamma_k |00\rangle_c |s_k\rangle_{\vec{d}} + \sqrt{1 - |\gamma_k|^2} |01\rangle_c \cdots \right).$$
 (C3)

For each order k, the Riemann sum  $B_k$  may be implemented by  $\mathrm{DYS}_K := (\mathrm{PREP}_K^\dagger \otimes \mathbb{1}_{as}) \cdot \mathrm{HAM} \cdot \mathrm{T}_K \cdot (\mathrm{PREP}_K \otimes \mathbb{1}_{as})$ , as depicted in Fig. 4. The unitary  $\mathrm{DYS}_K$  encodes precisely terms  $B_k$  of the Dyson series as follows

$$(\langle 0|_{\vec{a}c\vec{d}} \otimes \mathbb{1}_{\vec{b}s}) \operatorname{DYS}_{K}(|0\rangle_{\vec{a}c\vec{d}} \otimes \mathbb{1}_{\vec{b}s}) = \sum_{k=0}^{K} |k\rangle\langle k|_{\vec{b}} \otimes \frac{|\gamma_{k}|^{2} k! (M-k)!}{M!} B_{k}.$$
(C4)

Now, a linear combination of Dyson series terms is implemented by preparing a state with the appropriate amplitudes in the basis  $|k\rangle_{\vec{k}}$ . The required state preparation operators are

$$\begin{aligned}
\text{COEF} & |0\rangle_{\vec{b}} := \frac{1}{\sqrt{\beta}} \sum_{k=0}^{K} \sqrt{\frac{M!(-it)^{k}}{M^{k}|\gamma_{k}|^{2}k!(M-k)!}} |k\rangle_{\vec{b}}, \quad \beta = \sum_{k=0}^{K} \frac{M!t^{k}}{M^{k}|\gamma_{k}|^{2}k!(M-k)!}, \\
\text{COEF}' & |0\rangle_{\vec{b}} := \frac{1}{\sqrt{\beta}} \sum_{k=0}^{K} \sqrt{\frac{M!t^{k}}{M^{k}|\gamma_{k}|^{2}k!(M-k)!}} |k\rangle_{\vec{b}},
\end{aligned} (C5)$$

and may be implemented using  $\mathcal{O}(K)$  primitive gates. Up to a proportionality factor  $\beta$ , we obtain the desired linear combination for simulating time-evolution.

$$TDS_{\beta} := (COEF'^{\dagger} \otimes \mathbb{1}_{\vec{a}\vec{c}\vec{d}s}) \cdot DYS_{K} \cdot (COEF \otimes \mathbb{1}_{\vec{a}\vec{c}\vec{d}s})$$

$$(\langle 0|_{\vec{a}\vec{b}\vec{c}\vec{d}} \otimes \mathbb{1}_{s}) TDS_{\beta}(|0\rangle_{\vec{a}\vec{b}\vec{c}\vec{d}} \otimes \mathbb{1}_{s}) = \frac{\sum_{k=0}^{K} (-it)^{k} B_{k}}{M^{k}\beta} \approx \frac{\mathcal{T}e^{-i\int_{0}^{t} H(s)ds}}{\beta}.$$
(C6)

Using the provided parameters for K and M, the numerator, by Lemma 5, approximates a unitary operation to error  $\mathcal{O}(\epsilon)$ . The probability of applying this operation can be boosted from  $|\frac{1+\Theta(\epsilon)}{\beta}|^2$  to  $1-\mathcal{O}(\epsilon)$  using oblivious amplitude

amplification [6]. If we choose t to be sufficiently small such that  $\beta=2$ , then a single round of oblivious amplitude amplification suffices, and we obtain a single time-step of the truncated Dyson series algorithm TDS in Fig. 4, where each reflection REF acts on  $K(n_a+n_d+1)+2$  qubits and therefore costs  $K(n_a+n_d+1)+2$  gates. All that remains is to find an implementation of PREP<sub>K</sub> that prepares  $|s_k\rangle_{\vec{d}}$  with an amplitude that  $|\gamma_k|$  that is sufficiently large so that  $t=\Theta(1)$ .

The state  $|s_k\rangle_{\vec{b}c\vec{d}}$  can be prepared in a number of ways. The most straightforward approach creates a uniform superposition of states over the dimension-k hypercube using  $n_d \times k$  Hadamard gates HAD, then uses k reversible adders to flag states  $|\vec{m}\rangle_{d_1\cdots d_k}$  with the correct ordering. This circuit  $\text{PREP}_{|s_k\rangle}$  produces  $|s_k\rangle_{\vec{d}}$  with amplitude  $\gamma_k = \sqrt{\frac{M!}{M^k k!(M-k)!}}$ .  $\text{PREP}_K$  is then obtained by controlling  $\text{PREP}_{|s_k\rangle}$  on input state  $|k\rangle_{\vec{b}}$ . Thus

$$\beta = \sum_{k=0}^{K} t^k \le \sum_{k=0}^{\infty} t^k = \frac{1}{1-t}.$$
 (C7)

Thus by choosing  $t = \Theta(1) \approx 1/2$ , we obtain the desired  $\beta = 2$ . Notably, even though the success probability of naive state preparation  $|\gamma_k|^2$  decays rapidly, this only amounts to a constant factor slowdown compared to more sophisticated techniques that effectively prepare  $|s_k\rangle_{\vec{d}}$  with success probability  $\approx 1$ . For example, rather than rejection sampling, one may perform a reversible sort on on uniform superposition of states  $\frac{1}{\sqrt{M^k}} \sum_{\vec{m}} |\vec{m}\rangle_{d_1 \cdots d_k} |0\rangle_{\text{garbage}} \rightarrow \frac{1}{\sqrt{M^k}} \sum_{\vec{m}} |\mathcal{T}[m_{d_1} \cdots m_{d_k}]\rangle_{d_1 \cdots d_k} |\vec{m}\rangle_{\text{garbage}}$ , such as with the quantum bitonic sorting network [23]. This effectively increases  $\gamma_k^2$  by a factor of k!, and uses significantly more ancilla qubits, but ultimately allows us to implement time steps  $t \approx \ln 2 \approx 0.693$  larger by a constant factor.

If we wish to simulate time-evolution for any  $t \leq \frac{1}{2}$ , this will lead to  $\beta \leq 2$ . In this situation,  $\beta$  may be increased to 2 using single-qubit rotations, as described by [8], to artificially worsen the success probability.

## Appendix D: Truncated Taylor series algorithm

The truncated Taylor series simulation algorithm was a major advance in quantum simulation for its conceptual simplicity and computational efficiency. The original algorithm [8] is motivated by truncating the Taylor expansion of the time-evolution operator at degree K.

$$e^{-iHt} = 1 - iHt + \frac{(-iHt)^2}{2!} + \frac{(-iHt)^3}{3!} \dots = \underbrace{\sum_{k=0}^K \frac{(-iHt)^k}{k!}}_{\bar{R}_K} + \underbrace{\sum_{k=K+1}^\infty \frac{(-iHt)^k}{k!}}_{R_K}.$$
 (D1)

Assuming that t > 0 and that the truncation order  $K \ge 2||H||t$ , the norms of  $\bar{R}_K$  and the remainder term  $R_K$  are bounded by

$$\|\bar{R}_K\| = \|e^{-iHt} - R_K\| \le 1 + \|R_K\|,$$

$$\|R_K\| \le \sum_{k=K+1}^{\infty} \frac{(\|H\|t)^k}{k!} \le \frac{(\|H\|t)^{K+1}}{(K+1)!} \sum_{k=K+2}^{\infty} (1/2)^{k-K-1} = \frac{2(\|H\|t)^{K+1}}{(K+1)!}.$$
(D2)

Thus any unitary quantum circuit TTS that acts jointly on registers a, b, s and applies the non-unitary operator  $(\langle 00|_{ab} \otimes \mathbb{1}_s) \operatorname{TTS}(|00\rangle_{ab} \otimes \mathbb{1}_s) \approx \bar{R}_K$  approximates the time-evolution operator with error  $\delta$  and failure probability p given by

$$\delta = \|e^{-iHt} - \bar{R}_K\| = \|R_K\| \le \frac{2(\|H\|t)^{K+1}}{(K+1)!},$$

$$p \le 1 - \min_{|\psi\rangle_s} \left| \frac{\bar{R}_K |\psi\rangle_s}{1 + \|R_K\|} \right|^2 = 1 - \min_{|\psi\rangle_s} \left| \frac{(e^{-iHt} - R_K)|\psi\rangle_s}{1 + \|R_K\|} \right|^2 \le 1 - \left| \frac{1 - \|R_K\|}{1 + \|R_K\|} \right|^2 = 4\|R_K\| = 4\delta.$$
(D3)

Solving Eq. (D3) for  $||H||t \in \mathcal{O}(1)$  gives the required truncation order  $K \in \mathcal{O}\left(\frac{\log(1/\delta)}{\log\log(1/\delta)}\right)$ .

The simulation algorithm TTS in Fig. 5 is obtained by constructing two oracles.  $HAM_K$ , which applies positive integer powers of  $(-iH)^k$  up to k=K, and COEF, which prepares a quantum state that selects these terms with the

right coefficients.  $HAM_K$  will require additional ancilla registers, which we index with  $\vec{a}$  and  $\vec{b}$ . Note that the gate and space complexity in the truncated Taylor series algorithm is dominated by that of  $HAM_K$ .

$$(\langle 0|_{\vec{a}} \otimes \mathbb{1}_{s\vec{b}}) \operatorname{HAM}_{K}(|0\rangle_{\vec{a}} \otimes \mathbb{1}_{s\vec{b}}) := \sum_{k=0}^{K} |k\rangle \langle k|_{\vec{b}} \otimes (-iH)^{k},$$

$$\operatorname{COEF} |0\rangle_{\vec{b}} := \frac{1}{\sqrt{\beta}} \sum_{k=0}^{K} \sqrt{\frac{t^{k}}{k!}} |k\rangle_{\vec{b}}, \quad \beta = \sum_{k=0}^{K} \frac{t^{k}}{k!} \leq e^{t}.$$

$$(D4)$$

![](_page_28_Figure_3.jpeg)

FIG. 5. Quantum circuit representation of (top, left) an example implementation of HAM<sub>K</sub> from Eq. (D4) using K queries to controlled-HAM; (top, right) an example implementation of HAM<sub>K</sub> with fewer ancilla qubits using the compression gadget of Lemma 13; (bottom, left) a single step of the truncated Taylor series algorithm before oblivious amplitude amplification; (bottom, right) a single step of time-evolution by the truncated Taylor series algorithm from Eq. (D7). Note that  $\beta = 2$  as a single-round of oblivious amplitude amplification is used.

The original algorithm [8] implements  $HAM_K$  using K queries to controlled-HAM

$$C-HAM := |1\rangle\langle 1|_b \otimes \mathbb{1}_{as} + |0\rangle\langle 0|_b \otimes (-i HAM)$$
(D5)

with K copies of registers a and b. The state  $|k\rangle_{\vec{b}} = |0\rangle^{\otimes k}|1\rangle^{\otimes K-k}$  that selects desired powers of H is encoded in unary, and so COEF may be implemented using  $\mathcal{O}(K)$  primitive gates. Up to a proportionality factor  $\beta$ , the unitaries of Eq. (D4) allow us to implement the desired linear combination  $\bar{R}_K$  for simulating time-evolution.

$$TTS_{\beta} := (COEF^{\dagger} \otimes \mathbb{1}_{\vec{a}s}) HAM_{K}(COEF \otimes \mathbb{1}_{\vec{a}s})$$

$$(\langle 0|_{\vec{a}b} \otimes \mathbb{1}_{s}) TTS_{\beta}(|0\rangle_{\vec{a}b} \otimes \mathbb{1}_{s}) = \frac{\bar{R}_{K}}{\beta} \approx \frac{e^{-iHt}}{\beta}.$$
(D6)

As  $\bar{R}_k$  is close to unitary, the success probability  $\approx 1/\beta^2$  may be boosted using oblivious amplitude amplification [6]. When  $\beta=2$ , a single round of oblivious amplitude amplification suffices to boost the success probability to  $1-\mathcal{O}(\delta)$ . Thus we chose  $\ln 2 \le t \in \mathcal{O}(1)$  such that  $\beta=2$ . If we desire  $|t| < \ln 2$ ,  $\beta$  may be decreased by appending a single-qubit ancilla and noting that  $|\langle 0|e^{i\theta X}|0\rangle|=|\cos\theta|\le 1$ . Thus simulation is accomplished with the circuit

$$TTS = TTS_{\beta=2} \cdot (REF \otimes \mathbb{1}_s) \cdot TTS_{\beta=2}^{\dagger} \cdot (REF \otimes \mathbb{1}_s) \cdot TTS_{\beta=2},$$

$$REF = \mathbb{1}_{\vec{a}\vec{b}} - 2|0\rangle\langle 0|_{\vec{a}\vec{b}}.$$
(D7)

This approximates time-evolution by  $e^{-iHt}$  with error  $\|(\langle 0|_{\vec{a}b} \otimes \mathbb{1}_s) \operatorname{TTS}(|0\rangle_{\vec{a}b} \otimes \mathbb{1}_s) - e^{-iHt}\| \in \mathcal{O}(\delta)$ . In order to simulate evolution  $e^{-iHT}$  by longer times T > t, we apply  $\operatorname{TTS}^{T/t}$  – here  $t = \Theta(1)$  is chosen such that T/t is an integer. The overall error

$$\epsilon = \left\| [TTS^{T/t} - \mathbb{1}_{\vec{a}\vec{b}} \otimes e^{-iHT}] (|0\rangle_{\vec{a}\vec{b}} \otimes \mathbb{1}_s) \right\| \in \mathcal{O}(T\delta), \tag{D8}$$

and success probability  $1 - \mathcal{O}(\epsilon)$  may thus be controlled by choosing the error of each segment to be  $\delta \in \mathcal{O}\left(\frac{\epsilon}{T}\right)$ . This requires a truncation order of  $K \in \mathcal{O}\left(\frac{\log{(\alpha T/\epsilon)}}{\log{\log{(\alpha T/\epsilon)}}}\right)$ . We may drop the implicit assumption that  $||H|| \leq 1$ , by

rescaling  $H \to H/\alpha$ , for some normalization constant  $\alpha \ge \|H\|$ . Thus simulation of  $e^{-iHt}$  requires  $\mathcal{O}\left(\alpha T \frac{\log{(\alpha T/\epsilon)}}{\log{\log{(\alpha T/\epsilon)}}}\right)$  queries to C-HAM. Note that the gate cost of all queries to COEF at  $\mathcal{O}\left(\alpha T \frac{\log{(\alpha T/\epsilon)}}{\log{\log{(\alpha T/\epsilon)}}}\right)$  and that of REF at  $\mathcal{O}\left(n_a \alpha T \frac{\log{(\alpha T/\epsilon)}}{\log{\log{(\alpha T/\epsilon)}}}\right)$ , is typically dominated by the gate cost of all applications of C-HAM.

The ancilla overhead of the truncated Taylor series algorithm, at  $n_s + \mathcal{O}(n_a \frac{\log(1/\epsilon)}{\log\log(1/\epsilon)})$  qubits, may be significantly improved by choosing the sequence of unitaries in the compression gadget Lemma 13 of Appendix B to be  $U_j = -i$  HAM. This straightforwardly furnishes the following result.

Corollary 16 (Hamiltonian simulation by a compressed truncated Taylor series). Let a time-independent Hamiltonian H be encoded in standard-form with normalization  $\alpha$  and  $n_s + n_a$  qubits, as per Definition 1. Then the truncated Taylor series algorithm approximates the time-evolution operator  $e^{-iHt}$  for any  $|\alpha t| \leq \ln 2$  to error  $\epsilon$  using

- 1. Queries to HAM:  $\mathcal{O}\left(\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}\right)$ .
- 2. Qubits:  $n_s + \mathcal{O}(n_a + \log \log (1/\epsilon))$ .
- 3. Primitive gates:  $\mathcal{O}\left((n_a + \log\log(1/\epsilon))\frac{\log(1/\epsilon)}{\log\log\log(1/\epsilon)}\right)$ .

For longer-time simulations  $e^{-iHT}$  of duration T > t, Corollary 16 is applied  $\alpha T/\ln(2)$  times, each with error  $\mathcal{O}(\frac{\epsilon}{\alpha T})$ . This leads a query complexity  $\mathcal{O}(\alpha T \frac{\log{(\alpha T/\epsilon)}}{\log{\log{(\alpha T/\epsilon)}}})$ . Though the compressed algorithm is still worse than the quantum signal processing approach, which uses  $n_s + \mathcal{O}(n_a)$  qubits, the technique is applicable to simulating time-dependent Hamiltonians, as demonstrated in Section III.