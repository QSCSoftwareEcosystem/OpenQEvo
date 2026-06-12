# Hybridized Methods for Quantum Simulation in the Interaction Picture

Abhishek Rajput<sup>1</sup>, Alessandro Roggero<sup>2,3</sup>, and Nathan Wiebe<sup>1,4,5</sup>

Conventional methods of quantum simulation involve trade-offs that limit their applicability to specific contexts where their use is optimal. In particular, the interaction picture simulation has been found to provide substantial asymptotic advantages for some Hamiltonians but incurs prohibitive constant factors and is incompatible with methods like qubitization. We provide a framework that allows different simulation methods to be hybridized and thereby improve performance for interaction picture simulations over known algorithms. These approaches show asymptotic improvements over the individual methods that comprise them and further make interaction picture simulation methods practical in the near term. Physical applications of these hybridized methods yield a gate complexity scaling as  $\log^2 \Lambda$  in the electric cutoff  $\Lambda$  for the Schwinger Model and independent of the electron density for collective neutrino oscillations, outperforming the scaling for all current algorithms with these parameters. For the general problem of Hamiltonian simulation subject to dynamical constraints, these methods yield a query complexity independent of the penalty parameter  $\lambda$  used to impose an energy cost on time-evolution into an unphysical subspace.

## 1 Introduction

Since Feynman's seminal work on the simulation of quantum dynamics with quantum computers [1], considerable research has been undertaken on the problem of quantum simulation as it is a major area where quantum computers are expected to outperform classical supercomputers [2, 3, 4, 5, 6]. The problem of simulation is in effect a compilation problem. The task in simulation is to generate, for a given Hermitian matrix H, evolution time t, and error tolerance  $\epsilon$  a sequence of quantum gates U(t) such that  $||U(t) - e^{-iHt}|| \le \epsilon$ , for an appropriate norm  $||\cdot||$ , and the cost of the sequence of gate operations that comprise U(t) is minimal. This problem is distinct from ordinary unitary synthesis problems because here we do not explicitly know the matrix elements of  $e^{-iHt}$  and need to construct this unitary only using information about the Hamiltonian H.

A variety of simulation methods have been developed to approximate the ideal time-evolution channel. The first, and most space efficient, algorithms are the Trotter-Suzuki formulas and their time-ordered generalizations [2, 7, 8, 9, 10], but recent years have seen several additions to the repertoire of quantum simulation techniques. The method of qubitization [11, 12, 13, 14, 15, 16, 17] involves the implementation of a walk operator whose eigenvalues are an efficiently computable function of those of H and achieves linear scaling in the simulation time t, logarithmic scaling in the inverse error tolerance, and scaling independent of the number of terms in the Hamiltonian. A major drawback of qubitization is that the method does not apply to time-dependent Hamiltonians. Linear combinations of unitaries provides simulation methods [18, 19, 20, 21] that address this short coming and allow simulations within the interaction picture at costs that can be exponentially lower

<sup>&</sup>lt;sup>1</sup>Department of Physics, University of Washington, Seattle, WA 98195, USA

<sup>&</sup>lt;sup>2</sup>InQubator for Quantum Simulation (IQuS), Department of Physics, University of Washington, Seattle, WA 98195, USA

<sup>&</sup>lt;sup>3</sup>Dipartimento di Fisica, University of Trento, via Sommarive 14, I–38123, Povo, Trento, Italy

<sup>&</sup>lt;sup>4</sup>Department of Computer Science, University of Toronto, Toronto, ON M5S 2E4, Canada

<sup>&</sup>lt;sup>5</sup>Pacific Northwest National Laboratory, Richland, WA 99354, USA

than all other known methods [21]; however, these approaches require complicated quantum control logic which can lead to undesirable constant factors [22].

The quantum stochastic drift protocol [23], or qDRIFT, is spiritually related to linear combination of unitaries but uses classically controlled evolutions rather than quantum controlled ones. This approach drifts towards the correct unitary time-evolution with high precision and with a gate complexity independent on the number of terms in the Hamiltonian. qDRIFT was later generalized to the continuous qDRIFT protocol for time-dependent Hamiltonians with an  $L^1$ -norm scaling in the gate complexity [24]. The principal disadvantages of this approach are that it has a larger scaling in the simulation time t compared to other algorithms and does not exploit any commutator structure between the terms of a Hamiltonian.

We develop hybrid algorithms in this paper that combine the various conventional approaches for quantum simulation after moving into the interaction picture (I.P.). This is significant because while the interaction picture simulation method provides the best asymptotic scaling known for many problems, the constant factors involved can make it impractical for many applications [22]. We address this by combining algorithms such as qDRIFT and qubitization at different stages of the overall simulation procedure within the interaction picture. Since the interaction picture transformation involves conjugation of Hamiltonian summands  $\sum_{k\neq j} H_k$  via  $e^{itH_j}$ , the unitary invariance of the  $L^1$ -norm scaling from qDRIFT essentially eliminates the contribution of  $H_j$  to the query complexity of the hybrid protocols. A direct application of these methods to physical systems such as the Schwinger Model and collective neutrino oscillations yield improved scaling over current algorithms with respect to certain parameters of interest. The general problem of Hamiltonian simulation constrained to a physical subspace can likewise be efficiently simulated using these algorithms, with a scaling independent of the penalty parameter used to impose an energy cost on projections onto the unphysical subspace.

We summarize the scaling of the newly introduced hybrid schemes and compare them to standard approaches in Table 1. These are expressed in terms of the oracle complexity for approximating the time-evolution under a Hamiltonian  $H = \sum_{i=1}^L H_i$ . For the Trotter/qDRIFT based I.P. methods, we show the asymptotic scaling in terms of queries to oracles  $\{W_k\}_{k=1}^L$  implementing  $W_k(t) = e^{-iH_kt}$  for any choice of summand  $H_k$ . For the hybrid qubitization I.P. based methods, the queries are instead to the SELECT/PREPARE oracles (see Section 2.2 for details) and the oracle  $W_l(t) = e^{-itH_l}$ . The latter is specifically used to implement the time evolution of the term  $H_l$  to enter the interaction picture, while the oracles  $\{W_k\}_{k=1}^L$  above are used to implement all the time-evolutions. The constant  $\lambda$  and  $\lambda_\alpha$  are obtained by first writing H as a linear combination of unitaries  $H = \sum_k \omega_k U_k$  with real  $\omega_l > 0$ . Then we have  $\lambda = \sum_k \omega_k$  and  $\lambda_\alpha = \sum_{k \neq l} \omega_k = \lambda - \omega_l$ . As anticipated above, the hybrid I.P. schemes introduced here can become advantageous when  $\lambda_\alpha \ll \lambda$  or  $\|H - H_l\|_\infty \ll \|H\|_\infty$ , that is, when the Hamiltonian term  $H_l$  has a large norm (here and in the rest of the paper,  $\|H\|_p$  denotes the Schatten p-norm of a matrix. See Appendix B for further details).

Section 2 contains a review of some standard methods of quantum simulation and of the interaction picture. More specifically, in Section 2.1 we summarize the continuous qDRIFT protocol and the relevant theorems on its query complexity. Section 2.2 delves into qubitization and singular value transformations. Section 2.3 contains an overview of Trotterization and a generalization of the first order Trotter-Suzuki formula to time-dependent Hamiltonians. Section 2.4 reviews the interaction picture, the key component of our hybrid protocols. Section 3 and Section 4 contain the main results on our hybrid protocols with Section 5, Section 6, and Section 7 presenting applications of them to the Schwinger Model, collective neutrino oscillations, and constrained Hamiltonian dynamics respectively. The reader can find additional background on the diamond norm in Appendix A and on some of the norm notation used throughout the paper in Appendix B.

## 2 Standard Methods of Quantum Simulation

This section contains brief overviews of interaction picture of quantum mechanics and relevant results from standard methods of quantum simulation such as continuous qDRIFT, qubitization, and Trotterization. Those readers already familiar with these topics can skip to Section 3.

| Algorithm                              | Number of oracle calls to $W_k$ or PREPARE/SELECT and $W_l$                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trotter [10]                           | $O\left(\frac{\tilde{\alpha}^{1/p}t^{1+1/p}}{\epsilon^{1/p}}\right)$                                                                                                                                                                                                                                                                                                                                               |
| qDRIFT [23]                            | $O\left(\frac{t^2}{\epsilon} \left[ \sum_{k=1}^{L} \ H_k\ _{\infty} \right]^2 \right)$ $O\left(\lambda t + \frac{\log(1/\epsilon)}{\log(\log(1/\epsilon))}\right)$                                                                                                                                                                                                                                                 |
| Qubitization [11, 12]                  | $O\left(\lambda t + \frac{\log(1/\epsilon)}{\log(\log(1/\epsilon))}\right)$                                                                                                                                                                                                                                                                                                                                        |
|                                        |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Trotter $+$ qDRIFT $+$ I.P. [Cor. 3.3] | $O\left(\frac{t^2}{\epsilon} \sum_{k \neq l}^{L} \left[ \ H_k\ _{\infty}^2 + \left\  \left[ H_k, \sum_{q > k, q \neq l}^{L} H_q \right] \right\ _{\infty} \right] \right)$                                                                                                                                                                                                                                         |
| qDRIFT + Qubitization + I.P. [Th. 4.2] | $ \left  \begin{array}{c} O\left(\frac{t^2}{\epsilon} \sum_{k \neq l}^{L} \left[ \ H_k\ _{\infty}^2 + \left\  \left[ H_k, \sum_{q > k, q \neq l}^{L} H_q \right] \right\ _{\infty} \right] \right) \\ O\left(\lambda_{\alpha} t + \left( \frac{\ H - H_l\ _{\infty}^2 t^2}{\epsilon} \right) \frac{\log(\ H - H_l\ _{\infty} t/\epsilon)}{\log\log(\ H - H_l\ _{\infty} t/\epsilon)} \right) \end{array} \right  $ |

Table 1: Query complexities for standard qDRIFT, Trotter, qubitization, and the hybrid schemes from Corollary 3.3 and Theorem 4.2 where  $H = \sum_{i=1}^L H_i$  with L the number of summands in the Hamiltonian H,t the simulation time, and  $\epsilon$  the simulation error. In the Trotter formula, p is the order of the Trotter formula and  $\tilde{\alpha}$  involves sums of commutators nested p times. The query complexity for qDRIFT and Trotter-based algorithms are given in terms of upper bounds for queries to each of the  $W_k$  oracles that implement time-evolution under a summand  $H_k$ . The query complexity for the qubitization methods are given in queries to the oracles  $W_l$  implementing time-evolution for the interaction picture transformation, SELECT, and PREPARE. For the latter methods, H is decomposed as a linear combination of unitaries  $H = \sum_k \omega_k U_k$  with real  $\omega_l > 0$ . Then  $\lambda = \sum_k \omega_k$  and  $\lambda_\alpha = \lambda - \omega_l$ . The hybrid I.P. schemes can become advantageous when  $\lambda_\alpha \ll \lambda$  or  $\|H - H_l\|_\infty \ll \|H\|_\infty$ .

#### 2.1 Continuous qDRIFT

In this subsection, we outline the continuous qDRIFT protocol used to simulate time-dependent Hamiltonians with a scaling depending only on the  $L^1$ -norm of the Hamiltonian. At its heart is a classical sampling protocol which randomly samples a simulation time  $\tau \in [0,t]$  according to a probability distribution and evolves a given state under the time-independent Hamiltonian  $H(\tau)$ . The probability distribution is chosen such that it is biased towards  $\tau$  with large  $||H(\tau)||_{\infty}$ . The result is a simulation protocol that stochastically drifts towards the ideal unitary time evolution with small error in the diamond norm.

We present relevant results from [24] used throughout this paper without proof. Let  $H(\tau)$  be a time dependent Hamiltonian defined for  $0 \le \tau \le t$ . Unless otherwise specified, we make the following assumptions of  $H(\tau)$ :

- 1. It is non-zero and continuously differentiable on [0,t]
- 2. It is finite dimensional, i.e.  $H:[0,t]\to\mathbb{C}^{M\times M}$
- 3. There exists an oracle  $W \colon \mathbb{R}^2 \mapsto \mathbb{C}^{M \times M}$  such that for any  $\tau \in [0,t]$  and  $\Delta \in \mathbb{R}$ ,  $W(\tau,\Delta) = e^{-iH(\tau)\Delta}$

The specific implementation of W depends on the simulation protocol in question. For instance, a concrete realization involves "qubitization oracles" to be discussed later in the paper. For our present purposes, it suffices to assume the existence of such an oracle and analyze the query complexity of algorithms invoking it as a black box.

The ideal evolution of  $H(\tau)$  for time t is given by  $E(t,0) = \exp_{\mathcal{T}}(-i\int_0^t d\tau H(\tau))$  and the quantum channel corresponding to this is

$$\mathcal{E}(t,0) = E(t,0)\rho E^{\dagger}(t,0) = \exp_{\mathfrak{T}}\left(-i\int_{0}^{t}d\tau H(\tau)\right)\rho \exp_{\mathfrak{T}}^{\dagger}\left(-i\int_{0}^{t}d\tau H(\tau)\right),\tag{1}$$

where the subscript  $\mathcal{T}$  in  $\exp_{\mathcal{T}}$  denotes the time-ordered exponential. Generalizations of these channels to non-zero initial times can be accomplished simply by changing the limits of integration.

Since it is difficult in practice to implement the ideal channel due to the presence of time-ordered exponentials, we can instead approximate it by a mixed unitary channel defined by

$$U(t,0)(\rho) = \int_0^t d\tau \ p(\tau)e^{-i\frac{H(\tau)}{p(\tau)}}\rho e^{i\frac{H(\tau)}{p(\tau)}}, \qquad (2)$$

where

$$p(\tau) \coloneqq \frac{||H(\tau)||_{\infty}}{||H||_{\infty,1}}$$

is a probability density function defined for  $0 \le \tau \le t$  and

$$||H||_{\infty,1} \coloneqq \int_0^t d\tau ||H||_{\infty}.$$

(i.e. the outermost subscript indicates an  $L^1$  norm while the innermost subscript indicates a Schatten infinity norm). This channel can be implemented via a classical sampling protocol and has the following features:

- (a)  $p(\tau)$  is biased towards those  $\tau \in [0, t]$  with large  $||H(\tau)||_{\infty}$
- (b)  $p(\tau)$  decreases with the evolution time t since  $||H(\tau)||_{\infty,1}$  involves an integral over [0,t]
- (c) With a time  $\tau_i \in [0, t]$  obtained from sampling  $p(\tau)$ , we can query the oracle W cited above by inputting  $W(\tau_i, p(\tau_i)^{-1})$  to obtain an implementation of the unitary time-evolution operator  $e^{-iH(\tau_i)/p(\tau_i)}$

This classical sampling protocol and the unitary channel (2) implemented by it is denoted by "continuous qDRIFT". We assume the spectral norm  $||H||_{\infty}$  or an upper bound is already known and that we can efficiently sample from  $p(\tau)$ . We then have the following theorem when the simulation time t is assumed to be sufficiently small:

**Theorem 2.1** ( $L^1$ -norm error bound for continuous qDRIFT, short-time version). Let  $H(\tau)$  be a time-dependent Hamiltonian defined for  $0 \le \tau \le t$  and satisfying conditions 1 and 2 above. Define  $\mathcal{E}(t,0)$  and  $\mathcal{U}(t,0)(\rho)$  as in equations (1) and (2) respectively. Then

$$||\mathcal{E}(t,0) - \mathcal{U}(t,0)||_{\diamond} \le 4||H||_{\infty,1}^2$$
 (3)

(See Appendix A for information about the diamond norm for quantum channels). When the simulation time t is large, we will need to divide the simulation interval [0,t] into sub-intervals  $[t_j,t_{j+1}]$  where  $0=t_0< t_1< \cdots < t_r=t$  and apply the continuous qDRIFT protocol within each to control the simulation error. In these cases, we have a "long-time" version of Theorem 2.1:

**Theorem 2.2.** ( $L^1$ -norm error bound for continuous qDRIFT for long simulation time) Let  $H(\tau)$  be a time-dependent Hamiltonian defined for  $0 \le \tau \le t$  and satisfying conditions 1 and 2 above. Define  $\mathcal{E}(t,0)$  and  $\mathcal{U}(t,0)(\rho)$  as in (1) and (2) respectively. For any positive integer r, there exists a division  $0 = t_0 < t_1 < \cdots < t_r = t$ 

$$\left\| \mathcal{E}(t,0) - \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_j) \right\|_{\diamond} \le 4 \frac{\|H\|_{\infty,1}^2}{r} . \tag{4}$$

To ensure the simulation error is at most  $\epsilon$ , it suffices to choose

$$r \ge 4 \left\lceil \frac{\|H\|_{\infty,1}^2}{\epsilon} \right\rceil .$$

The value of r above can also be interpreted as the query complexity of the continuous qDRIFT protocol, i.e. the number of queries to the oracle W needed to implemented channel (2) and satisfy (4) with error less than  $\epsilon$ .

For additional information on the diamond norm and notation used in these results, the reader may consult Appendix A and Appendix B.

#### 2.2 Qubitization and Singular Value Transformations

Having considered continuous qDRIFT, we now briefly review the basics of the qubitization simulation protocol which we seek to combine with the former. We will also frame qubitization as an example of the general notion of the block-encoding of non-unitary matrices within larger unitary ones.

Qubitization is a method of Hamiltonian simulation involving the synthesis of the time-evolution operator  $e^{iHt}$ , where H is a time-independent Hamiltonian, via the implementation of a walk operator W(H) whose eigenvalues are an efficiently computable function of those of H. Assuming that we have decomposed H as a linear combination of unitary matrices, the desired walk operator can implemented with the so-called SELECT and PREPARE qubitization oracles. The spectrum can then be transformed efficiently using techniques involving singular value transformations which transform the singular values of an operator by a polynomial function [11, 12].

Block-encoding refers to the embedding of a non-unitary matrix H into a larger unitary U, typically as the upper-left block of U. Once a block-encoding is achieved, a quantum circuit can be expressed in terms of U. This greatly broadens the applicability of quantum computers, particularly in the domain of the simulation of unitary quantum dynamics. We largely follow the treatments in [17, 25].

Let  $H \in \text{End}(\mathbb{C}^N)$ , where  $N = 2^n$ , be a Hermitian operator. Suppose there exists an (m+n)-qubit unitary matrix  $U_H \in \text{End}(\mathbb{C}^{MN})$ , where  $M = 2^m$ , such that

$$U_H = \begin{pmatrix} H/\alpha & \cdot \\ \cdot & \cdot \end{pmatrix} ,$$

where  $\alpha > 0$  is a known normalization constant. We may then get access to  $H/\alpha$  by

$$H = (\langle 0|^m \otimes I_n) U_H(|0\rangle^m \otimes I_n) .$$

To quantify how "close" the block encoded matrix is to the original one, we introduce the following general definition. This definition can also be extended to the case of block-encodings within superoperators, which we will need to consider for the proofs of some later theorems:

**Definition 2.3** (Block Encoding). Suppose that A is an n-qubit operator,  $\alpha, \varepsilon \in \mathbb{R}_+$ , and  $m \in \mathbb{N}$ . We then say that the (m+n)-qubit unitary  $U_H$  is a  $(\alpha, m, \varepsilon)$ -block-encoding of A if

$$||A - \alpha(\langle S| \otimes I_n)U_H(|S\rangle \otimes I_n)||_{\infty} < \varepsilon$$
.

where  $|S\rangle$  is an *m*-qubit state.

Similarly, we say that a quantum channel  $\Lambda$  is a  $(\alpha, m, \varepsilon)$ -block-encoding of A if

$$\max_{\rho} \|A\rho A^{\dagger} - \alpha(\langle T| \otimes I_n) \Lambda(|T\rangle\langle T| \otimes \rho)(|T\rangle \otimes I_n)\|_{\infty} \leq \epsilon,$$

where the maximization is over density matrices  $\rho$  and  $|T\rangle$  is an m-qubit state.

Here  $|S\rangle$  or  $|T\rangle$  are referred to as the "signal state". The previous example involving H is a (1, m, 0)-encoding where  $|S\rangle = |0\rangle^m$ .

Now suppose we are given a time-independent H. H can be decomposed into a linear combination of unitary operators

$$H = \sum_{l=0}^{L-1} w_l H_l, \quad w_l \in \mathbb{R}_0^+, \quad H_l^2 = I .$$
 (5)

Here we assume that any complex phases are absorbed into  $U_l$ . The two oracles used are a preparation oracle whose action on  $|0\rangle^{\log L}$  is defined as follows:

PREPARE 
$$|0\rangle^{\log L} = \sum_{l=0}^{L-1} \sqrt{\frac{w_l}{\lambda}} |l\rangle = |\mathcal{L}\rangle$$
, (6)

where

$$\lambda = \sum_{l} w_{l} ,$$

and a selection oracle whose action on an ancilla register  $|l\rangle$  and system register  $|\Psi\rangle$  is as follows:

$$SELECT = \sum_{l=0}^{L-1} |l\rangle\langle l| \otimes H_l , \qquad (7)$$

SELECT 
$$|l\rangle|\Psi\rangle \mapsto |l\rangle H_l|\Psi\rangle$$
. (8)

In other words, the SELECT oracle "selects" a unitary  $H_l$  conditioned on the state of the ancilla register  $|l\rangle$ . Using (7) and (8), it can be shown that SELECT squares to the identity operator and can therefore be considered as a "reflection" operator. Note that we also have the following result for the action of SELECT on  $|\mathcal{L}\rangle$ :

$$(\langle \mathcal{L} | \otimes I)(\text{SELECT})(|\mathcal{L}\rangle \otimes I) = \frac{1}{\lambda} \sum_{l} w_{l} H_{l} = \frac{H}{\lambda} . \tag{9}$$

The previous equation is a condition for qubitization and oracles that satisfy this condition are referred to as "qubitization oracles" [12]. If we define

$$U_H = (PREPARE^{\dagger} \otimes I)(SELECT)(PREPARE \otimes I)$$
,

it follows from (9) that  $U_H$  is a  $(\|w\|_1, \log L, 0)$ -block encoding of H, where  $\|w\|_1 = \sum_l |w_l|$ .

The desired walk operator, also known as the "iterate", can now be defined as follows:

$$W = \mathcal{R}_L \cdot \text{SELECT}, \quad \mathcal{R}_L = (2|\mathcal{L}\rangle\langle\mathcal{L}| \otimes I - I) .$$
 (10)

 $\mathcal{W}$  is of the form of a Szegedy walk operator since it is the composition of two reflections. From a lemma by C. Jordan on the common invariant subspaces of two reflections [26], it follows that the Hilbert space of the system decomposes under the action of  $\mathcal{W}$  into a direct sum of 1 and 2-dimensional irreducible subspaces, where the latter is spanned by  $|\mathcal{L}\rangle|k\rangle$  and an orthogonal state  $|\phi_k\rangle$ . Here,  $|k\rangle$  is an eigenstate of H with eigenvalue  $E_k$  and  $|\phi_k\rangle$  is the component of  $\mathcal{W}|\mathcal{L}\rangle|k\rangle$  orthogonal to  $|\mathcal{L}\rangle|k\rangle$ . Using (9), this can be expressed as

$$|\phi_k\rangle = \frac{(I - |\mathcal{L}\rangle\langle\mathcal{L}| \otimes |k\rangle\langle k|) \cdot \text{SELECT}|\mathcal{L}\rangle|k\rangle}{||(I - |\mathcal{L}\rangle\langle\mathcal{L}| \otimes |k\rangle\langle k|) \cdot \text{SELECT}|\mathcal{L}\rangle|k\rangle||} = \frac{(\text{SELECT} - \frac{E_k}{\lambda}I)|\mathcal{L}\rangle|k\rangle}{\sqrt{1 - (\frac{E_k}{\lambda})^2}} . \tag{11}$$

In the 2-dimensional subspaces, W acts as a rotation whereas on the 1-dimensional subspaces, it has  $\pm 1$  eigenvalues. The matrix elements of W within a two-dimensional subspace can be computed using the above relations. Using (9), the top-left entry is

$$\langle k | \langle \mathcal{L} | \mathcal{W} | \mathcal{L} \rangle | k \rangle = \frac{E_k}{\lambda} ,$$

and the upper-right entry using (11) is

$$\langle k | \langle \mathcal{L} | \mathcal{W} | \phi_k \rangle = \sqrt{1 - \left(\frac{E_k}{\lambda}\right)^2} \,.$$

The other elements can be computed in an analogous way and we obtain for the form of the 2-dimensional blocks of  $\mathcal W$ 

$$\begin{bmatrix} \frac{E_k}{\lambda} & \sqrt{1 - \left(\frac{E_k}{\lambda}\right)^2} \\ -\sqrt{1 - \left(\frac{E_k}{\lambda}\right)^2} & \frac{E_k}{\lambda} \end{bmatrix} = e^{i \arccos(E_k/\lambda)Y} . \tag{12}$$

The controlled walk operator can be implemented using the circuit in Figure 1 [25]. It is clear from this that W requires one query to SELECT and at most two queries to PREPARE to implement. The controlled-SELECT operation can be approximated as requiring the same gate complexity to implement as the SELECT operation.

![](_page_6_Figure_1.jpeg)

Figure 1: Controlled-walk operator in terms of the SELECT and PREPARE oracles

Note that if the condition that  $H_l^2 = I$  in (5) does not hold, we no longer have the interpretation of SELECT acting like a reflection operator. It then follows that  $\mathcal W$  cannot be interpreted as a Szegedy walk operator and we can no longer apply Jordan's lemma to it. However, we can still define  $\mathcal W$  as in (10) and the subsequent computations involving the calculation of matrix elements of  $\mathcal W$  when restricted to the two-dimensional subspace spanned by the orthogonal states  $|\mathcal L\rangle|k\rangle$  and  $|\phi_k\rangle$  remain unaffected. It can still be shown that the Hilbert space decomposes as a direct sum of such 2 dimensional irreducible subspaces as  $\mathcal W$  does not take vectors within the subspace outside of it.

The arccos in (12) can be efficiently inverted to recover the original spectrum of H via techniques involving singular value transformations and quantum signal processing. The impetus for the development of the general formalism of singular value transformations was the Quantum Signal Processing techniques introduced by Low et al. [27]. They considered the following problem: if one applies a gate sequence of the form

$$e^{i\phi_0\sigma_z}e^{i\theta\sigma_x}e^{i\phi_1\sigma_z}e^{i\theta\sigma_x}\cdots e^{i\theta\sigma_x}e^{i\phi_k\sigma_z}$$
,

for unknown  $\theta$ , where  $e^{i\theta\sigma_x}$  is the "signal unitary" and where we have control over the angles  $\phi_0, \dots, \phi_k$ , what unitary operators can be constructed in this manner? This problem lies at the heart of "Quantum Signal Processing".

The answer to this problem is given in Theorem 3 of [13] and involves polynomial transformations of the entries of the signal unitary. This idea behind Quantum Signal Processing can be generalized to situations where we apply an arbitrary unitary U between phase operators. It can be shown that this induces polynomial transformations to the singular values of a particular block of the unitary U. In the application to qubitization we are concerned with, Quantum Signal Processing can be applied to the two-dimensional invariant subspaces of the walk operator W.

As we saw in Section 2.2, qubitization exploits a lemma by C. Jordan's on the invariant subspaces of two reflection operations and the decomposition of the entire vector space into a direct sum of those subspaces. One of the reflections in the lemma can be replaced by a phase gate in the context of quantum search algorithms [27]. In [13], the other reflection is replaced by an arbitrary unitary U and the invariant subspaces in question are those arising from the singular value decomposition of a block of the unitary matrix. For our purposes, we only need the following results.

**Definition 2.4** (Theorem 17 of [13]). Let  $\mathcal{H}_U$  be a finite-dimensional Hilbert space and  $U, \Pi, \tilde{\Pi} \in \operatorname{End}(\mathcal{H}_U)$  be linear operators on  $\mathcal{H}_U$  such that U is unitary and  $\Pi, \tilde{\Pi}$  are orthogonal projectors. Let  $\Phi \in \mathbb{R}^n$ . Then we define the phased alternating sequence  $U_{\Phi}$  as follows

$$U_{\Phi} \coloneqq \begin{cases} e^{i\phi_1(2\Pi - I)} U \prod_{j=1}^{(n-1)/2} (e^{i\phi_{2j}(2\Pi - I)} U^{\dagger} e^{i\phi_{2j+1}(2\tilde{\Pi} - I)} U) & \text{if n is odd} \\ \prod_{j=1}^{n/2} (e^{i\phi_{2j-1}(2\Pi - I)} U^{\dagger} e^{i\phi_{2j}(2\tilde{\Pi} - I)} U) & \text{if n is even} \end{cases}.$$

Figure 2 shows the circuit implementation of the alternating phase modulation sequence for even n.

![](_page_7_Figure_1.jpeg)

Figure 2: Circuit for  $U_{\Phi}$  when n is even

**Theorem 2.5** (Quantum Singular Value Transformation: Theorem 17 of [13]). Let  $\mathcal{H}_U$  be a finite-dimensional Hilbert space and let  $U, \Pi, \tilde{\Pi} \in \operatorname{End}(\mathcal{H}_U)$  be linear operators on  $\mathcal{H}_U$  such that U is unitary, and  $\Pi, \tilde{\Pi}$  are orthogonal projectors. Let  $P \in \mathbb{C}[x]$  and  $\Phi \in \mathbb{R}^n$ . Then

$$P^{(SV)}(\tilde{\Pi}U\Pi) = \begin{cases} \tilde{\Pi}U_{\Phi}\Pi & \textit{if $n$ is odd} \\ \Pi U_{\Phi}\Pi & \textit{if $n$ is even} \end{cases},$$

where  $P^{(SV)}$  is a polynomial of degree at most n that performs a singular value transformation on the operator to which it is applied.

The polynomials in the above theorem are required to satisfy the conditions listed in Corollary 8 of [13]:

- (a) P has parity  $n \mod 2$
- (b)  $\forall x \in [-1, 1] : |P(x)| \le 1$
- (c)  $\forall x \in (-\infty, -1] \cup [1, \infty) : |P(x)| \ge 1$
- (d) If n is even, then  $\forall x \in \mathbb{R} : P(ix)P^*(ix) > 1$

Qubitization works by inverting the arccosine. While this boils down to the problem of applying a cosine transformation to the input in principle, in practice a Fourier-Chebyshev expansion is used via the Jacobi-Anger expansion that requires both the odd and even terms to closely approximate the desired function and guarantee that the function is within [-1, 1] for the entire domain to use the bounds provided in the work. This process is described in detail in [27] as well as in Section 5 of [13].

Applying the preceding theorems to U = CTRL(W) and  $\Pi = \tilde{\Pi} = |0\rangle^L \langle 0|^L \otimes I$ , where L is the number of qubits in the register  $|\alpha\rangle$  in Figure 1, will enable us to invert the arccos in the spectrum of the walk-operator. A circuit for the unitary operator  $e^{i2\phi_j(2\Pi-I)}$  is given in Figure 3.

Note that we are merely concerned with the existence of a transformation of the spectrum of the walk-operator by a polynomial via the preceding theorem rather than the finding of the phase factors needed to effect a given polynomial transformation. Constructive algorithms for finding these phase factors are outlined in [16, 17, 28, 29].

The overall query complexity for qubitization and the singular value transformation is given by the following result as expressed in the language of block encodings.

![](_page_7_Figure_15.jpeg)

Figure 3: Circuit for fractional reflection gadget,  $e^{i2\phi_j(2\Pi-I)}$ , used in quantum singular value transformations.

**Theorem 2.6** (Corollary 60 of [13]). Let  $\epsilon \in (0, \frac{1}{2})$ ,  $t \in \mathbb{R}$  and  $\alpha \in \mathbb{R}^+$ . Let U be an  $(\alpha, a, 0)$ -block encoding of the unknown Hamiltonian H. In order to implement an  $\epsilon$ -precise Hamiltonian simulation unitary V which is an  $(1, a+2, \epsilon)$ -block encoding of  $e^{itH}$ , it is necessary and sufficient to use U a total number of times

$$\Theta\left(\alpha|t| + \frac{\log(1/\varepsilon)}{\log(e + \log(1/\varepsilon)/(\alpha|t|))}\right). \tag{13}$$

Letting  $\alpha = \lambda$  in our notation and assuming that  $\varepsilon$  is small, we can simplify (13) as

$$\Theta\left(\lambda t + \frac{\log(1/\varepsilon)}{\log\log(1/\varepsilon)}\right). \tag{14}$$

The linear term comes from the qubitization portion of the procedure while the logarithmic term stems from the transformation of the singular values via the procedure outlined above. This result can be equivalently interpreted as the query complexity for qubitization in terms of the number of queries (modulo irrelevant constants) needed to the PREPARE and SELECT oracles, since U = CTRL(W) is related to PREPARE and SELECT via Figure 1.

#### 2.3 Trotterization

We briefly outline the basics of Trotterization, the oldest method of quantum simulation based on product formulas, and present the relevant results on Trotterization errors used in this paper. Our ultimate goal is to synthesize this method of simulation with the interaction picture and continuous qDRIFT, and compare it with a hybrid continuous qDRIFT and qubitization protocol. This will be followed by an application of both methods to several physical models.

Let  $H = \sum_{i=1}^{\Gamma} H_i$  be a time-independent Hamiltonian expressed as a sum of  $\Gamma$  terms. The unitary time-evolution operator generated by H is then  $e^{it\sum_{i=1}^{\Gamma} H_i}$ . There are a variety of product formulas that can be used to decompose the time-evolution operator into a product of exponentials involving the individual terms  $H_i$ . The most basic is the first-order Lie-Trotter formula

$$\mathscr{S}_1(t) \coloneqq e^{itH_{\Gamma}} \cdots e^{itH_1}$$
.

Higher order generalizations are the Suzuki formulas defined recursively as

$$\mathscr{S}_2(t) := e^{i\frac{t}{2}H_1} \cdots e^{i\frac{t}{2}H_{\Gamma-1}} e^{itH_{\Gamma}} e^{i\frac{t}{2}H_{\Gamma-1}} \cdots e^{i\frac{t}{2}H_1} ,$$

$$\mathscr{S}_{2k}(t) \coloneqq \mathscr{S}_{2k-2}(u_k t)^2 \mathscr{S}_{2k-2}((1-4u_k)t) \mathscr{S}_{2k-2}(u_k t)^2 \;,$$

where  $u_k = (4 - 4^{-(2k-1)})^{-1}$ . There is an extensive literature devoted to investigating the utility and performance of various product-formulas for a variety of physical systems and applications [4, 5, 10]. While there are multiple strategies for addressing the time-ordering of the operators for the time-ordered operator exponentials that emerge when simulating time-dependent Hamiltonians, we broadly follow the analysis outlined in [9].

Let  $H(t) = \sum_{S} H_S(t)$  be a time-dependent Hamiltonian acting on N particles, where  $S \subset \{1, \ldots, N\}$ , and each term has bounded norm and acts on at most k particles with k a constant independent of N. The time-evolution operator E(t,0) governing the evolution of the system from time 0 to t is determined by the Schrödinger equation

$$\frac{d}{dt}E(t,0) = -iH(t)E(t,0) ,$$

which admits a solution in terms of a time-ordered exponential

$$E(t,0) = \exp_{\mathcal{T}} \left\{ -i \int_0^t H(s) ds \right\}.$$

It turns out that the Trotter-Suzuki formulas given above can be generalized to time-dependent scenarios, even in situations where the Hamiltonian experiences fluctuations on time-scales shorter

than the time step  $\Delta t$  [9]. Suppose we wish to simulate the time-evolution of our system up to time  $t_r + \Delta t = T$  from  $t_0 = 0$ . The exact time-evolution operator can be broken up into shorter segments of the form

$$E(T,0) = \prod_{i=0}^{r} E(t_i + \Delta t, t_i) ,$$

where

$$E(t_i + \Delta t, t_i) = \exp_{\mathcal{T}} \left( -i \int_{t_j}^{t_j + \Delta t} ds \sum_{S} H_S(s) \right). \tag{15}$$

In the case where the sum over S involves only two terms,  $H_1$  and  $H_2$ , the generalized Trotter-Suzuki expansion is of the form

$$E^{TS}(t_j + \Delta t, t_j) = \exp_{\mathcal{T}} \left( -i \int_{t_j}^{t_j + \Delta t} ds H_1(s) \right) \exp_{\mathcal{T}} \left( -i \int_{t_j}^{t_j + \Delta t} ds H_2(s) \right)$$
$$= E_1^{TS}(t_j + \Delta t, t_j) E_2^{TS}(t_j + \Delta t, t_j) , \qquad (16)$$

and gives rise to a simulation error of

$$||E(t_i + \Delta t, t_i) - E^{TS}(t_i + \Delta t, t_i)||_{\infty} \le c_{12}(\Delta t^2),$$
 (17)

where  $c_{12}$  is given by

$$c_{12} = \frac{1}{(\Delta t)^2} \int_{t_i}^{t_j + \Delta t} dv \int_{t_i}^{v} du \| [H_1(u), H_2(v)] \|_{\infty} \le \frac{1}{2} \max_{u, v} (\| [H_1(u), H_2(v)] \|_{\infty}) . \tag{18}$$

#### 2.4 The Interaction Picture

The interaction picture or Dirac picture of quantum mechanics is one of the three representations of operators and states in quantum mechanics [30]. It is intermediate to the Schrodinger and Heisenberg pictures of quantum mechanics where the former is characterized by state vectors that evolve in time but with operators constant in time, and vice versa for the latter. Within the interaction picture however, both operators and states have time dependence but the latter evolves according to the interaction Hamiltonian consisting of the left-over terms in the original Hamiltonian. This picture is particularly useful with dealing with terms in a Hamiltonian that can be treated as small perturbations to a main term such as in time-dependent perturbation theory, where it is used in deriving transition rates via Fermi's golden rule and the Dyson series perturbative expansion of the time-evolution operator. It also finds widespread application in interacting quantum field theories. [31].

We follow the derivation in [30]. Consider a time-independent Hamiltonian  $H = \sum_i H_i$ . Suppose the energy eigenvalues and eigenstates of  $H_j$  for some j are known.

At  $t = t_0$ , let the state of the physical system be given by  $|\alpha\rangle$ . At a later time t, we denote the state in the Schrodinger picture by  $|\alpha, t_0; t\rangle_S$ . Now define

$$|\alpha, t_0; t\rangle_I := e^{iH_j t} |\alpha, t_0; t\rangle_S , \qquad (19)$$

where we have implicitly set  $\hbar=1$  and where the subscript I indicates the same situation as represented in the so-called "interaction picture" (I.P.).

We also define observables in the interaction picture as

$$A_I(t) := e^{iH_j t} A_S e^{-iH_j t} . (20)$$

The physical implication of this definition is that we pick any term in the Hamiltonian and move into its "interaction frame" via conjugation by  $e^{iH_jt}$ . The major difference between this definition and the analogous one in the Heisenberg picture is the appearance of  $H_j$  in the former as opposed to the full H in the latter.

We now take the time derivative of equation (19):

$$i\frac{\partial}{\partial t}|\alpha, t_0; t\rangle_I = i\frac{\partial}{\partial t} \left( e^{iH_j t} |\alpha, t_0; t\rangle_S \right)$$

$$= -H_j e^{iH_j t} |\alpha, t_0; t\rangle_S + e^{iH_j t} (H_j + \sum_{i \neq j} H_i) |\alpha, t_0; t\rangle_S$$

$$= e^{iH_j t} \sum_{i \neq j} H_i e^{-iH_j t} e^{iH_j t} |\alpha, t_0; t\rangle_S = H_I(t) |\alpha, t_0; t\rangle_I , \qquad (21)$$

where we used the Schrodinger equation in the second equality. Thus we have

$$i\hbar \frac{\partial}{\partial t} |\alpha, t_0; t\rangle_I = H_I(t) |\alpha, t_0; t\rangle_I ,$$
 (22)

with

$$H_I(t) = e^{iH_j t} \left(\sum_{i \neq j} H_i\right) e^{-iH_j t} = \sum_{i \neq j} H_i^I, \tag{23}$$

where

$$H_i^I = e^{iH_jt}H_ie^{-iH_jt} .$$

This is a Schrodinger-like equation for the time-evolution of the interaction picture state but with the Hamiltonian H replaced by  $H_I$ .

It is important to note the distinction between how observables in the interaction picture are represented in (20) versus the interaction Hamiltonian above. Naively, we would expect the full Hamiltonian to be what is conjugated within the big parentheses in (23) by analogy with (20). This "discrepancy" merely arises from the fact that we needed to define  $H_I$  as above to obtain the Schrodinger-like equation (22).

We can apply the interaction picture to the continuous qDRIFT protocol outlined before and obtain the following simple lemma.

**Lemma 2.7.** (L<sup>1</sup>-norm error bound for IP continuous qDRIFT for long simulation time) Let  $H_I(\tau)$  be an interaction picture Hamiltonian as in (23). Suppose it is defined for  $0 \le \tau \le t$  and satisfies conditions 1 and 2 in Section 2.1. Define  $\mathcal{E}(t,0)$  and  $\mathcal{U}(t,0)$  as in (1) and (2) respectively but with  $H_I(\tau)$ . Then for any positive integer r, there exists a division  $0 = t_0 < t_1 < \cdots < t_r = t$  such that

$$\left\| \mathcal{E}(t,0) - \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_j) \right\|_{2} \le 4t^2 \frac{\| \sum_{i \neq j} H_i \|_{\infty}^2}{r} . \tag{24}$$

To ensure the simulation error is at most  $\epsilon$ , it therefore suffices to choose

$$r \ge 4 \left\lceil \frac{t^2 \|\sum_{i \ne j} H_i\|_{\infty}^2}{\epsilon} \right\rceil.$$

*Proof.* We can substitute (23) directly into equation (4) and the expression for r. Note however the spectral norm of an operator (and the Schatten norms more generally) is invariant under unitary transformations of that operator. We then obtain the simplification

$$||H_I||_{\infty,1} = \int_0^t d\tau ||H_I(\tau)||_{\infty} = \left\| \sum_{i \neq j} H_i \right\|_{\infty} t$$

so that

$$\left\| \mathcal{E}_{I}(t,0) - \mathcal{U}_{I}(t,0) \right\|_{\diamond} \leq 4 \frac{\left( \| \sum_{i \neq j} H_{i} \|_{\infty} \right)^{2} t^{2}}{r} , \qquad (25)$$

and

$$r \geq 4 \left\lceil \frac{(\|\sum_{i \neq j} H_i\|_{\infty})^2 t^2}{\epsilon} \right\rceil \,,$$

to ensure our simulation error is less than some desired  $\epsilon$ .

As before, r can also be interpreted as the number of queries to the oracle W defined in Section 2.1. Each resulting time-independent piece will need to be simulated using techniques like Trotterization or Qubitization and the main goal of the paper is to quantify the overall query and gate complexity of "hybrid" protocols combining these with the IP continuous qDRIFT technique outlined here.

Comparing this result to Theorem 2.2, we see that moving into the interaction frame of a fixed term  $H_j$  of the overall Hamiltonian effectively "eliminates" its contribution to the error. Moreover, due to the properties of the spectral norm and the interaction Hamiltonian,  $L^1$ -norm dependence of the results in Theorem 2.2 reduce to those reminiscent of the time-independent case. This behavior recurs in subsequent results and is particularly useful when dealing with terms with unbounded behavior or large  $\infty$ -norm, such as the electric term in the Schwinger Model considered later in the paper.

# 3 Hybrid Trotterization and qDRIFT Protocol

We now present an analysis of our first hybrid simulation protocol where a generalization of the time-dependent Trotter-Suzuki formula given in (16) proved below is combined with continuous qDRIFT. Let  $H(t) = \sum_{k=1}^{L} H_k(t)$ . The procedure is as follows:

- 1. Use Trotterization technique below to approximate the time-ordered exponential of H(t) as a product of L time-ordered exponentials.
- 2. Use continuous qDRIFT to approximate each time-ordered exponential by the channel (2). Implementing this channel involves sampling from a probability distribution and yields a product of r time-independent terms of the form  $\exp(-iH_I(\tau_k)/p(\tau_k))$ , where r is the number of sub-intervals of the whole simulation interval.

Before proving the error bounds for these processes, we first show the following simple lemma with time arguments suppressed for notational convenience:

**Lemma 3.1.** Let  $\mathcal{E}^{TS}$  denote the superoperator representing the Trotter-Suzuki decomposition of the time-ordered exponential in (16) and let  $\mathcal{E}$  be as in (1). If  $D_{2^n}$  is the set of density operators in the domain of  $\mathcal{E}$ , then

$$\|\mathcal{E} - \mathcal{E}^{TS}\|_{\infty} := \sup_{\rho \in D_{2^n}} \|\mathcal{E}(\rho) - \mathcal{E}^{TS}(\rho)\|_{\infty} \le 2\|E - E^{TS}\|_{\infty}.$$
 (26)

*Proof.* From the triangle inequality we have that

$$\begin{split} \|\mathcal{E} - \mathcal{E}^{\mathrm{TS}}\|_{\infty} &\leq \sup_{\rho \in D_{2^{n}}} \|E\rho E^{\dagger} - E^{\mathrm{TS}}\rho E^{\dagger}\|_{\infty} + \sup_{\rho \in D_{2^{n}}} \|E^{\mathrm{TS}}\rho E^{\dagger} - E^{\mathrm{TS}}\rho (E^{\mathrm{TS}})^{\dagger}\|_{\infty} \\ &= \sup_{\rho \in D_{2^{n}}} \|(E\rho - E^{\mathrm{TS}}\rho)E^{\dagger}\|_{\infty} + \sup_{\rho \in D_{2^{n}}} \|E^{\mathrm{TS}}(\rho E^{\dagger} - \rho (E^{\mathrm{TS}})^{\dagger})\|_{\infty} \\ &= \sup_{\rho \in D_{2^{n}}} \|(E - E^{\mathrm{TS}})\rho\|_{\infty} + \sup_{\rho \in D_{2^{n}}} \|(E - E^{\mathrm{TS}})\rho\|_{\infty} \\ &\leq 2\|E - E^{\mathrm{TS}}\|_{\infty} \,. \end{split}$$

In the third line, we used the unitary invariance of the infinity norm and that  $||A||_{\infty} = ||A^{\dagger}||_{\infty}$  for any bounded square operator A. The latter follows from the fact that the Schatten infinity norm is the spectral norm, which is the largest eigenvalue of  $\sqrt{AA^{\dagger}}$  and coincides with the largest eigenvalue of  $A^{\dagger}A$ . In the fourth line, we used the sub-multiplicativity of the infinity norm and the fact that  $||\rho||_{\infty} \leq 1$  for all density operators.

We now have the following results for quantum simulation with this hybrid protocol:

**Theorem 3.2** (Hybrid Trotterization and qDRIFT Simulation). Let  $\{H_k(t): k=1,\ldots,L\}$  be a set of time-dependent Hermitian operators satisfying conditions 1 and 2 in Section 2.1. Let  $\mathcal{U}_k$  denote the superoperator representing the continuous qDRIFT channel for the time-dependent summand  $H_k(t)$  as in (2). Then given a decomposition of [0,t] into r sub-intervals of length  $\Delta t = t/r$ ,

$$\left\| \mathcal{E}(t,0) - \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{U}_k(t_j + \Delta t, t_j) \right\|_{\infty} \le \frac{L^2 c_{\text{max}}}{r} t^2 + 4r \sum_{k=1}^{L} \|H_k\|_{\infty,1}^2 . \tag{27}$$

Here  $c_{\max}$  is defined as  $c_{\max} = \frac{1}{L^2} \max_{u,v} \sum_{p}^{L} \|[H_p(u), \sum_{q>p}^{L} H_q(v)]\|_{\infty}$  and the 1-norm in  $\|H_k\|_{\infty,1}^2$  denotes an integral over an interval of size  $\Delta t$ .

*Proof.* We first generalize (16) to the case where H(t) is the sum of L time-dependent terms. Suppose we break up H(t) as  $H(t) = H_1(t) + \sum_{k>1}^{L} H_k(t)$ . Treating the sum as our "second" term and considering a specific time-step  $[t_l, t_l + \Delta t]$ , we can substitute these into the expression for  $c_{12}$  above. Our proof of the error bound from recursively applying the bound in (16) is inductive. Let us consider the base case. Using (18) we have that

$$\left\| \exp_{\mathcal{T}} \left( -i \int_{t_{j}}^{t_{j} + \Delta t} H_{1}(t) + \sum_{k=2}^{L} H_{k}(t) dt \right) - \exp_{\mathcal{T}} \left( -i \int_{t_{j}}^{t_{j} + \Delta t} H_{1}(t) dt \right) \exp_{\mathcal{T}} \left( -i \int_{t_{j}}^{t_{j} + \Delta t} \sum_{k=2}^{L} H_{k}(t) dt \right) \right\|_{\infty}$$

$$\leq \frac{1}{2} \max_{u,v} \left\| \left[ H_{1}(u), \sum_{q>1}^{L} H_{q}(v) \right] \right\|_{\infty} \Delta t^{2}$$
(28)

Next assume that for some  $p \geq 1$  we have that

$$\left\| \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} H_{1}(t) + \sum_{k=2}^{L} H_{k}(t) dt \right) - \prod_{q=1}^{p} \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} H_{q}(t) dt \right) \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} \sum_{k=p+1}^{L} H_{k}(t) dt \right) \right\|_{\infty}$$

$$\leq \frac{1}{2} \sum_{\ell=1}^{p} \max_{u,v} \left\| \left[ H_{\ell}(u), \sum_{q>\ell}^{L} H_{q}(v) \right] \right\|_{\infty} \Delta t^{2}. \tag{29}$$

We then have from the triangle inequality and the unitary invariance of Schatten norms that for p+1

$$\left\| \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} H_{1}(t) + \sum_{k=2}^{L} H_{k}(t) dt \right) - \prod_{q=1}^{p+1} \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} H_{q}(t) dt \right) \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} \sum_{k=p+2}^{L} H_{k}(t) dt \right) \right\|_{\infty}$$

$$\leq \frac{1}{2} \sum_{\ell=1}^{p} \max_{u,v} \left\| \left[ H_{\ell}(u), \sum_{q>\ell}^{L} H_{q}(v) \right] \right\| \Delta t^{2} + \left\| \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} \sum_{k=p+1}^{L} H_{k}(t) dt \right) - \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} H_{p+1}(t) dt \right) \exp_{\mathfrak{T}} \left( -i \int_{t_{j}}^{t_{j}+\Delta t} \sum_{k=p+2}^{L} H_{k}(t) dt \right) \right\|_{\infty}$$

$$\leq \frac{1}{2} \sum_{\ell=1}^{p} \max_{u,v} \left\| \left[ H_{\ell}(u), \sum_{q>\ell}^{L} H_{q}(v) \right] \right\|_{\infty} \Delta t^{2} + \frac{1}{2} \max_{u,v} \left\| \left[ H_{p+1}(u), \sum_{q>p+1}^{L} H_{q}(v) \right] \right\|_{\infty} \Delta t^{2} \\
= \frac{1}{2} \sum_{\ell=1}^{p+1} \max_{u,v} \left\| \left[ H_{\ell}(u), \sum_{q>\ell}^{L} H_{q}(v) \right] \right\|_{\infty} \Delta t^{2} .$$
(30)

This demonstrates the induction step and combined with the base case in (28) shows the error bound we need inductively.

Since this analysis was for the time interval  $[t_j + \Delta t, t_j]$  and since there are r such intervals sub-dividing our simulation interval, we can multiply our previous result by r using Box 4.1 in [32]. Since  $\Delta t = t/r$ , we then have

$$||E(t,0) - E^{TS}(t,0)||_{\infty} \le \frac{L^2 c_{\text{max}}}{2r} t^2$$
 (31)

Now note that from (3) that if we denote the time evolution under  $H_k$  to be given by the unitary superoperator  $\mathcal{E}_k(t_j + \Delta t, t_j)$ , then

$$\|\mathcal{E}_k(t_i + \Delta t, t_i) - \mathcal{U}_k(t_i + \Delta t, t_i)\|_{\infty} \le \|\mathcal{E}_k(t_i + \Delta t, t_i) - \mathcal{U}_k(t_i + \Delta t, t_i)\|_{\diamond} \le 4\|H_k\|_{\infty, 1}^2. \tag{32}$$

Using the sub-multiplicativity and triangle inequality for the induced infinity norm for superoperators, we get

$$\left\| \prod_{k=1}^{L} \mathcal{E}_{k}(t_{j} + \Delta t, t_{j}) - \prod_{k=1}^{L} \mathcal{U}_{k}(t_{j} + \Delta t, t_{j}) \right\|_{\infty} \le 4 \sum_{k=1}^{L} \|H_{k}\|_{\infty, 1}^{2} ,$$
 (33)

where the 1-norm in the subscript on the RHS denotes an integral over an interval of size  $\Delta t$  from  $t_j$  to  $t_j + \Delta t$ . Note that this notation causes the duration of the integral over time to be implicitly rather than explicitly defined. Despite this drawback, we use this notation in places throughout the manuscript for brevity.

A straightforward generalization of the argument in Box 4.1 in [32] using the sub-multiplicativity and triangle inequality for the diamond norm, and the fact quantum channels have diamond norm at most 1 yields

$$\left\| \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{E}_{k}(t_{j} + \Delta t, t_{j}) - \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{U}_{k}(t_{j} + \Delta t, t_{j}) \right\|_{\infty} \le 4r \sum_{k=1}^{L} \|H_{k}\|_{\infty, 1}^{2}.$$
 (34)

From the above inequality, Lemma 2.7, and Lemma 3.1 we obtain that the bound of the induced  $\infty$ -norm of the difference between the super-operator and the hybridized channel is

$$\left\| \mathcal{E}(t,0) - \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{U}_{k}(t_{j} + \Delta t, t_{j}) \right\|_{\infty} \leq \left\| \mathcal{E}(t,0) - \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{E}_{k}(t_{j} + \Delta t, t_{j}) \right\|_{\infty} + \left\| \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{E}_{k}(t_{j} + \Delta t, t_{j}) - \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{U}_{k}(t_{j} + \Delta t, t_{j}) \right\|_{\infty} \leq \frac{L^{2} c_{\max}}{r} t^{2} + 4r \sum_{k=1}^{L} \|H_{k}\|_{\infty,1}^{2} .$$
(35)

Note that since the 1-norm in  $||H_k||_{\infty,1}^2$  denotes an integral over a time-interval of size  $\Delta t$ , this term scales with  $t^2/r$ . If we implement each qDRIFT channel  $\mathcal{U}_k$  with some error  $\epsilon$ , an easy application of the triangle inequality will add an additional subdominant term of  $rL\epsilon$  to (27).

It should also be noted that the result of Theorem 3.2 applies for both the case of time-dependent as well as time-independent Hamiltonian evolution. This is relevant because it shows

that the lowest-order Trotter-Suzuki formula can be combined with qDRIFT profitably wherein small terms in the Hamiltonian can be reallocated between the Trotter and the qDRIFT portions of the Hamiltonian to reduce the simulation cost. This can be seen as an extension of the coalescing strategy of [33].

If we compare this result with that given in Theorem 7' of [24], we find that the error in the latter approach using solely continuous qDRIFT scales with  $||H_k||_{\infty,1,1}^2$ , where the last 1 in the subscript denotes a sum over k, and we square after performing the integral and sum. While the result in (27) adds a term which scales at worst quadratically in the number of terms L in the Hamiltonian, we will find that for systems like those considered later in this paper, we can exploit the commutation relations between the terms in the Hamiltonian to give bounds that scale linearly with L.

Corollary 3.3 (Hybrid Trotterization and qDRIFT Simulation in Interaction Picture). Let  $H = \sum_{k=1}^{L} H_k$  be a time-independent Hamiltonian where each summand satisfies conditions 1 and 2 in Section 2.1. Then given a decomposition of [0,t] into r sub-intervals of size  $\Delta t$ , we can perform the Hamiltonian simulation of H in the interaction frame of  $H_l$  as in (23) such that

$$\left\| \mathcal{E}(t,0) - \prod_{j=1}^{r} \prod_{k \neq l}^{L} \mathcal{U}_k(t_j + \Delta t, t_j) \right\|_{\infty} \le \frac{t^2}{r} \left( c_I + 4 \sum_{k \neq l}^{L} \|H_k\|_{\infty}^2 \right), \tag{36}$$

where  $c_I = \sum_{p \neq l}^L ||[H_p, \sum_{q>p}^L H_q]||_{\infty}$ . To ensure the simulation error in the infinity-norm is less than  $\epsilon$ , it therefore suffices to choose

$$r \ge \frac{t^2}{\epsilon} \left( c_I + 4 \sum_{k \ne l}^L \|H_k\|_{\infty}^2 \right).$$
 (37)

*Proof.* When moving into the interaction frame of a particular term  $H_l$  in H as in (23), we have

$$[H_p^I, H_q^I] = H_p^I H_q^I - H_q^I H_p^I = e^{iH_l t} H_p H_q e^{-iH_l t} - e^{iH_l t} H_q H_p e^{-iH_l t} = [H_p, H_q]^I \ .$$

Since the infinity norm is unitarily invariant, we then have that

$$||[H_p, H_q]^I||_{\infty} = ||[H_p, H_q]||_{\infty}.$$

As the time-dependence came only from the  $e^{iH_lt}$  terms, we can drop the maximization over times in  $c_{\text{max}}$ . The sums in  $c_{\text{max}}$  will be over those indices  $p, q \neq l$  and we define this simplified quantity as  $c_I$  as above.

The 1-norm in  $||H_k||_{\infty,1}^2$  denotes an integral over an interval of measure  $\Delta t$ , so it again follows from the unitary invariance of the infinity-norm that  $||H_k||_{\infty,1}^2 = (\Delta t)^2 ||H_k||_{\infty}^2$ . Substituting  $\Delta t = t/r$  into (27) then yields the desired expression.

We can frame the complexity of the preceding process in terms of oracles defined as follows:

**Definition 3.4.** Let  $H = \sum_k H_k$  be a *time-independent* Hamiltonian in  $\mathbb{C}^{M \times M}$ . We define oracles  $\{W_k\}_{k=1}^L$  such that for each  $k, W_k : \mathbb{R} \mapsto \mathbb{C}^{M \times M}$  with the action  $W_k(\Delta) = e^{-iH_k\Delta}$ .

These oracles can be used to implement the interaction frame transformation and the time evolution under specific summands of H at various fixed times. Equation (37) then gives an upper bound on the number of queries to the oracles  $W_k$  needed to ensure the simulation protocol is within error  $\epsilon$ .

# 4 Hybrid Continuous qDRIFT and Qubitization Protocol

We would also like to consider the scenario where we simulate a time-independent Hamiltonian H with the following procedure:

- 1. Move into the interaction frame of a term  $H_j$  in H to turn the simulation problem into one involving a time-dependent interaction Hamiltonian  $H_I(\tau)$  as in (23).
- 2. Use continuous qDRIFT to approximate the ideal time-evolution by the channel (2). Implementing this channel involves sampling from a probability distribution and yields a product of r time-independent terms of the form  $\exp(-iH_I(\tau_k)/p(\tau_k))$ , where r is the number of sub-intervals of the whole simulation interval.
- 3. Use qubitization to simulate each time-independent term above and perform a singular value transformation to transform the spectrum in (12) and recover the original spectrum of H.

We first make the following definition:

**Definition 4.1.** Let  $H = \sum_k w_k H_k$  be a time-independent Hamiltonian in  $\mathbb{C}^{M \times M}$ . We define an oracle  $W_j$  such that  $W_j : \mathbb{R} \mapsto \mathbb{C}^{M \times M}$  with the action  $W_j(\Delta) = e^{-iH_j\Delta}$ 

We use this oracle to transform to the interaction frame of a particular summand  $H_j$  in the Hamiltonian H in the following theorem:

**Theorem 4.2** (Hybrid qDRIFT and Qubitization I.P. Simulation). Let  $H = H_j + H_\alpha \in \mathbb{C}^{2^n \times 2^n}$  be a time-independent Hamiltonian such that  $H_\alpha$  has an LCU decomposition  $H_\alpha = \sum_{l \neq j}^L w_l H_l$ , where  $w_l \in \mathbb{R}^+$ , and each  $w_l$  and  $H_l$  are obtained by oracles PREPARE and SELECT in (6) and (7) respectively.

There exists a quantum algorithm such that for any  $\epsilon, t > 0$ , it implements a quantum channel  $\Lambda$  that is a  $(1, O(\log L), \epsilon)$  block-encoding of  $e^{-iHt}$  using a number of queries to PREPARE, SELECT, and  $W_j(t)$  in

$$O\left(\lambda_{\alpha}t + \left(\frac{\|H_{\alpha}\|_{\infty}^{2}t^{2}}{\epsilon}\right) \frac{\log(\|H_{\alpha}\|_{\infty}t/\epsilon)}{\log\log(\|H_{\alpha}\|_{\infty}t/\epsilon)}\right),\tag{38}$$

where  $\lambda_{\alpha} = \sum_{l \neq j} |w_l|$ .

*Proof.* From Theorem 2.2, we have that for any positive integer r, there exists a division of [0,t] where  $0 = t_0 < t_1 < \cdots < t_k < \cdots < t_r = t$  such that (4) holds, where  $\mathcal{E}(t,0)$  and each  $\mathcal{U}(t_k,t_{k+1})$  are understood as involving the interaction Hamiltonian  $H_I(\tau)$  of (23).

By equation (4)

$$\left\| \mathcal{E}(t,0) - \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_j) \right\|_{2} \le 4 \frac{\|H_I\|_{\infty,1}^2}{r} .$$

From the relationship of the trace norm to the diamond norm in (105) and the monotonicity of the Schatten *p*-norm, we get after choosing  $r \geq 8 \frac{\|H_I\|_{\infty,1}^2}{\epsilon}$  and defining  $D_{2^n}$  to be the set of all density operators in  $\mathbb{C}^{2^n \times 2^n}$ 

$$\left\| \mathcal{E}(t,0) - \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_{j}) \right\|_{\infty} := \max_{\rho \in D_{2^{n}}} \left\| \mathcal{E}(t,0) \circ \rho - \left( \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_{j}) \right) \circ \rho \right\|_{\infty}$$

$$\leq \max_{\rho \in D_{2^{n}}} \left\| \mathcal{E}(t,0) \circ \rho - \left( \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_{j}) \right) \circ \rho \right\|_{1} = \left\| \mathcal{E}(t,0) - \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1}, t_{j}) \right\|_{\diamond}$$

$$\leq 4 \frac{\|H_{I}\|_{\infty,1}^{2}}{r} \leq \frac{\epsilon}{2} . \tag{39}$$

Next, let  $Q(t_{k+1}, t_k)$  denote a channel which implements the three-step procedure outlined in the beginning of the section and let

$$\Lambda = \prod_{j=0}^{r-1} Q(t_{j+1}, t_j) ,$$

We claim  $\Lambda$  is the desired channel. To show this, note that from Definition 2.3, we have upon fixing a signal state  $|T\rangle = |0\rangle^m$  and setting  $\alpha = 1$  (which can be done since we're implementing qubitization) that

$$\max_{\rho \in D_{2^n}} \|\mathcal{E}(t,0)(\rho) - (\langle 0|^m \otimes I_n)(\Lambda(|0\rangle\langle 0|^m \otimes \rho))(|0\rangle^m \otimes I_n)\|_{\infty} \leq \max_{\rho \in D_{2^n}} \left\| \mathcal{E}(t,0)(\rho) - \left( \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1},t_j) \right)(\rho) \right\|_{\infty} + \max_{\rho \in D_{2^n}} \left\| \left( \prod_{j=0}^{r-1} \mathcal{U}(t_{j+1},t_j) \right)(\rho) - (\langle 0|^m \otimes I_n)(\Lambda(|0\rangle\langle 0|^m \otimes \rho))(|0\rangle^m \otimes I_n) \right\|_{\infty} \\
\leq \frac{\epsilon}{2} + r \max_{j} \max_{\rho \in D_{2^n}} \|\mathcal{U}(t_{j+1},t_j)(\rho) - (\langle 0|^m \otimes I_n)(Q(t_{j+1},t_j)(|0\rangle\langle 0|^m \otimes \rho))(|0\rangle^m \otimes I_n)\|_{\infty} . \tag{40}$$

Recall that sampling from  $U(t_k, t_{k+1})$  yields a time-independent term  $\exp(-iH_I(\tau_k)/p(\tau_k))$  where  $\tau_k \in [t_k, t_{k+1}] \subset [0, t]$  is a specific time in some sub-interval  $[t_k, t_{k+1}]$  at which  $H_I(\tau)$  is being evaluated. The latter term above can thus be interpreted as the maximum spectral norm of the difference between an ideal implementation of the time-evolution operator for  $t \in [t_k, t_{k+1}]$  and an implementation involving qubitization, maximized over all sub-intervals. This can be made as small as desired via singular value transformation techniques discussed previously. Choosing

$$\max_{j} \max_{\rho \in D_{2^n}} \| \mathfrak{U}(t_{j+1}, t_j)(\rho) - (\langle 0 |^m \otimes I_n)(Q(t_{j+1}, t_j)(|0\rangle \langle 0 |^m \otimes \rho))(|0\rangle^m \otimes I_n) \|_{\infty} \leq \frac{\epsilon}{2r} ,$$

we then have

$$\max_{\rho \in D_{2^n}} \|\mathcal{E}(t,0)(\rho) - (\langle 0|^m \otimes I_n)(\Lambda(|0\rangle\langle 0|^m \otimes \rho))(|0\rangle^m \otimes I_n)\|_{\infty} \leq \frac{\epsilon}{2} + r\frac{\epsilon}{2r} = \epsilon.$$

We now define

$$\tilde{H}_i(\tau) = H_i(\tau)/p(\tau)$$
,

for  $i \neq j$ . Using the following identity which holds for all invertible matrices U

$$Ue^A U^{\dagger} = \exp(UAU^{\dagger}) \,, \tag{41}$$

we have

$$\exp(-iH_I(\tau)/p(\tau)) = \exp\left(e^{iH_j\tau}\left(-i\sum_{i\neq j}\tilde{H}_i\right)e^{-iH_j\tau}\right)$$

$$= e^{iH_j\tau}\left(\exp\left(\sum_{i\neq j}-i\tilde{H}_i\right)\right)e^{-iH_j\tau}.$$
(42)

Each exp  $(-iH_I(\tau_k)/p(\tau_k))$  term obtained from sampling  $\mathcal{U}(t_{k+1}, t_k)$  can be expanded as in (42). Using the unitary invariance of the spectral norm, we have the simplification

$$p(\tau_k) = \frac{\|H_I(\tau_k)\|_{\infty}}{\|H_I(\tau)\|_{\infty,1}} = \frac{\|e^{iH_j\tau_k}(\sum_{i\neq j} H_i)e^{-iH_j\tau_k}\|_{\infty}}{\int_{t_k}^{t_{k+1}} dt \|e^{iH_j\tau_k}(\sum_{i\neq j} H_i)e^{-iH_j\tau_k}\|_{\infty}}$$
$$= \frac{\|\sum_{i\neq j} H_i\|_{\infty}}{\|\sum_{i\neq j} H_i\|_{\infty} \int_{t_k}^{t_{k+1}} dt} = \frac{1}{t_{k+1} - t_k}.$$

Thus, we obtain a product of terms of the form

$$\exp(-iH_I(\tau_k)(t_{k+1} - t_k)) = e^{iH_j\tau_k} \exp\left(-i(t_{k+1} - t_k) \sum_{i \neq j} H_i\right) e^{-iH_j\tau_k}.$$

We then obtain the overall query complexity by summing (14) as applied to each sub-interval  $[t_k, t_{k+1}]$  from 0 to r-1 with error in the QSP transformation at most  $\delta$ :

$$O\left(\sum_{k=0}^{r-1} \left(\lambda_{\alpha}(t_{k+1} - t_k) + \frac{\log(1/\delta)}{\log\log(1/\delta)}\right)\right) = O\left(\lambda_{\alpha}t + r\frac{\log(1/\delta)}{\log\log(1/\delta)}\right). \tag{43}$$

Letting  $\delta = O(\epsilon/r)$  for our choice of r in the above completes the proof.

Lastly, we consider a hybrid Trotter, qDRIFT, and qubitization I.P. protocol which extends the results of Theorem 3.3 to include a qubitization step at the end to simulate all the resulting time-independent exponentials. This procedure is largely similar to that outlined in the beginning of the section but with an additional Trotter step:

- 1. Move into the interaction frame of a term  $H_j$  in H to turn the simulation problem into one involving a time-dependent interaction Hamiltonian  $H_I(\tau)$  as in (23).
- 2. Use the Trotterization technique outlined in Section 2.3 to split the resulting time-ordered exponential into a product of L time-ordered exponentials, one for each summand in the Hamiltonian.
- 3. Use continuous qDRIFT to approximate each of the L time-ordered exponentials by the channel (2). Implementing this channel involves sampling from a probability distribution that yields a product of r time-independent terms of the form  $\exp(-iH_I(\tau_k)/p(\tau_k))$  for each of the L time-ordered exponentials.
- 4. Use qubitization to simulate the rL time-independent pieces and perform a singular value transformation to transform the spectrum in (12) and recover the original spectrum of H.

This yields the following theorem:

**Theorem 4.3** (Hybrid Trotter, qDRIFT, and Qubitization I.P. Simulation). Let the assumptions of the previous theorem hold. There exists a quantum algorithm such that for any  $\epsilon, t > 0$ , it implements a quantum channel  $\Gamma$  that is a  $(1, O(\log L), \epsilon)$  block-encoding of  $e^{-iHt}$  using a number of queries to PREPARE, SELECT, and  $W_j(t)$  in

$$O\left(\lambda_{\alpha}t + rL\frac{\log(rL/\epsilon)}{\log\log(rL/\epsilon)}\right),$$
 (44)

where  $\lambda_{\alpha} = \sum_{l \neq j} |w_l|$  and r is as in (37).

*Proof.* Let  $\Gamma$  denote a channel which implements the four-step procedure outlined above. Using the notation from the proof of the preceding theorem, we can express  $\Gamma$  as

$$\Gamma = \prod_{j=1}^{r} \prod_{k=1}^{L} Q_k(t_{j+1}, t_j)$$

where the subscript k denotes the quantum channel performing steps 3-4 above for a specific Hamiltonian term  $H_k$ .

Replicating the arguments of the preceding theorem, we can pick

$$\max_{k} \max_{j} \max_{\rho \in D_{2^n}} \| \mathfrak{U}_k(t_{j+1}, t_j)(\rho) - (\langle 0 |^m \otimes I_n)(Q_k(t_{j+1}, t_j)(|0\rangle\langle 0 |^m \otimes \rho))(|0\rangle^m \otimes I_n) \|_{\infty} \leq \frac{\epsilon}{2rL}.$$

$$(45)$$

From Corollary 3.3, we can pick  $r \geq \frac{2t^2}{\epsilon} \left( c_I + 4 \sum_{k \neq l}^L ||H_k||_{\infty}^2 \right)$ . Then from the triangle inequality, we have

$$\max_{\rho \in D_{2^n}} \|\mathcal{E}(t,0)(\rho) - (\langle 0|^m \otimes I_n)(\Gamma(|0\rangle\langle 0|^m \otimes \rho))(|0\rangle^m \otimes I_n)\|_{\infty}$$

$$\leq \max_{\rho \in D_{2^{n}}} \left\| \mathcal{E}(t,0)(\rho) - \left( \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{U}(t_{j+1},t_{j}) \right) (\rho) \right\|_{\infty}$$

$$+ \max_{\rho \in D_{2^{n}}} \left\| \left( \prod_{j=1}^{r} \prod_{k=1}^{L} \mathcal{U}(t_{j+1},t_{j}) \right) (\rho) - (\langle 0|^{m} \otimes I_{n}) (\Gamma(|0\rangle\langle 0|^{m} \otimes \rho)) (|0\rangle^{m} \otimes I_{n}) \right\|_{\infty}$$

$$\leq \frac{\epsilon}{2} + rL \max_{k} \max_{j} \max_{\rho \in D_{2^{n}}} \left\| \mathcal{U}(t_{j+1},t_{j})(\rho) - (\langle 0|^{m} \otimes I_{n}) (Q(t_{j+1},t_{j})(|0\rangle\langle 0|^{m} \otimes \rho)) (|0\rangle^{m} \otimes I_{n}) \right\|_{\infty}$$

$$\leq \frac{\epsilon}{2} + rL \frac{\epsilon}{2} = \epsilon. \tag{46}$$

The overall query complexity is obtained by summing (14) as applied to each of the  $\delta = t/r$  sized sub-intervals and summing over the magnitude of the coefficients in the interaction Hamiltonian. We then have, after choosing  $\delta = \frac{\epsilon}{2rL}$  that

$$O\left(r\sum_{k=1}^{L} \left(\lambda_i \Delta t + \frac{\log(1/\delta)}{\log\log(1/\delta)}\right)\right) = O\left(\lambda_\alpha t + rL \frac{\log(rL/\epsilon)}{\log\log(rL/\epsilon)}\right). \tag{47}$$

Note that the above methods can also be used to hybridize these simulation methods in the time-independent case. Unlike the Trotter-methods, the scaling of the query complexity is not substantially improved. Instead, any potential cost improvements to the simulation come from simplifications to PREPARE and SELECT.

Finally, we note that one can choose other combinations than an outer qDRIFT or Trotter loop and an inner qubitization loop. The first step in each of these hybrid procedures is to exploit the  $L^1$ -norm invariance of continuous qDRIFT by begining with a time-independent Hamiltonian and transforming into the interaction frame of a particular summand. This results in a time-dependent Hamiltonian, which cannot be simulated via qubitization and constrains us to use either Trotter or qDRIFT first. This still leaves open the possibility of whether trading an inner qDRIFT loop for another Trotterization procedure that decomposes the time-ordered exponentials to ordinary exponentials or randomly interleaving qDRIFT or Trotter procedures can result in additional speedups, and we leave such investigations for future work.

# 5 Hamiltonian Simulation of Schwinger Model

#### 5.1 Schwinger Model and Query Complexity Bounds

We apply these ideas in simulating the Schwinger Model, quantum electrodynamics in 1+1 dimensions on a lattice [34, 35]. This model has been extensively used as an important stepping stone in simulations of lattice field theories using both tensor networks (see e.g. [36, 37]) and quantum devices (see e.g. [38, 39, 40]).

Using the Hamiltonian formulation of lattice gauge theory in the U(1) compact case [41, 42], the Hamiltonian of the model with N-1 links and N/2 spatial sites (half of which are electronic and half are positronic), is given by

$$H = H_E + H_h + H_M \tag{48}$$

with

$$H_E = \frac{g^2 a}{2} \sum_r E_r^2$$
 (49)

$$H_h = \frac{1}{2a} \sum_{r} U_r \psi_r^{\dagger} \psi_{r+1} - U_r^{\dagger} \psi_r \psi_{r+1}^{\dagger}$$
 (50)

$$H_M = m \sum_r (-1)^r \psi_r^{\dagger} \psi_r, \tag{51}$$

where a is the lattice spacing, m the fermion mass, and g is the coupling constant.  $H_E$  can be interpreted as the electric energy given in terms of  $E_r$ , the integer-valued electric fields residing on the links. The remaining terms are expressed in terms of the fermionic operators  $\psi_r$  and  $\psi_r^{\dagger}$  living on each site r, and the unitary link operators  $U_r = e^{iaA_r}$  expressed in terms of the gauge-potential  $A_{\mu} = (0, A_1)$  in the temporal-gauge.  $H_h$  is a lattice analog of the minimal coupling of the Dirac fermionic field to the gauge field and  $H_M$  is the mass energy of the Dirac fermions, which are staggered based on the  $(-1)^r$  factor.

We also have the following commutation relations between the link operators  $E_r$  and  $U_r$ 

$$[E_r, U_s] = U_r \delta_{rs} \Rightarrow [E_r, U_s^{\dagger}] = -U_r^{\dagger} \delta_{rs}, \tag{52}$$

and between the fermionic creation and annihilation operators

$$\{\psi_r, \psi_s\} = \{\psi_r^{\dagger}, \psi_s^{\dagger}\} = 0$$
 (53)

$$\{\psi_r, \psi_s^{\dagger}\} = \delta_{rs}. \tag{54}$$

We can map the fermionic creation and annihilation operators in equations (50) and (51) onto a corresponding set of operators acting on spin degrees of freedom via the Jordan-Wigner transformation

$$\psi_r^{\dagger} = \frac{(X_r - iY_r)}{2} \prod_{j=1}^{r-1} Z_j. \tag{55}$$

Substituting the above into (50) and (51) and simplifying yields

$$H_h = \frac{1}{2a} \sum_{r=1}^{N-1} [U_r \sigma_r^- \sigma_{r+1}^+ + U_r^\dagger \sigma_r^+ \sigma_{r+1}^-]$$

$$= \frac{1}{8a} \sum_{r=1}^{N-1} \left[ (U_r + U_r^{\dagger})(X_r X_{r+1} + Y_r Y_{r+1}) + i(U_r - U_r^{\dagger})(X_r X_{r+1} - Y_r Y_{r+1}) \right]$$
 (56)

and

$$H_M = \frac{m}{2} \sum_{r=1}^{N} (-1)^{r+1} Z_r. \tag{57}$$

Note that a factor of I/2 was dropped in the above equation since terms proportional to the identity in a Hamiltonian merely shift the spectrum by a constant. The derivation above also assumes open boundary conditions, but generalizations to periodic boundary conditions are straightforward. In that case the total number of links becomes N instead of N-1 and the asymptotic results we derive below for simulating the Schwinger Model remain unchanged.

It is customary to use the electric eigenbasis  $|\epsilon\rangle_r$  for the infinite-dimensional Hilbert space of each link. In this basis, the  $E_r$  operator takes the diagonal form

$$E_r = \sum_{\epsilon} \epsilon |\epsilon\rangle_r \langle \epsilon|_r$$

and  $U_r$  takes the form

$$U_r = \sum_{\epsilon} |\epsilon + 1\rangle\langle\epsilon|,$$

i.e. of a raising operator. Note that in order to map these degrees onto a quantum computer, it is customary to truncate the link Hilbert space by wrapping the electric field at a chosen cutoff  $\Lambda$ . This requires modifying the commutation relations in (52) but this issue is not directly relevant for our present work.

Since  $H_h$  and  $H_M$  are manifestly a sum of unitary operators, we can use the PREPARE and SELECT oracles from the qubitization simulation technique outlined previously. The overarching strategy is to move into the interaction frame of the  $H_E$  term, employ our hybrid protocols as outlined in the previous sections, and determine the query complexity in terms of the qubitization query model. The physical reasons for selecting the  $H_E$  term for the interaction picture is that the spectral norm of  $E_r$  is either large for a large cutoff  $\Lambda$  or unbounded in the strong coupling regime where  $g \to \infty$ . Choosing this term "removes" it from consideration in the interaction Hamiltonian as per equation (23). Additionally, since the  $E_r$  operators are diagonal in its eigenbasis and the matrix elements are computable in polynomial time, the cost of simulating  $H_E$  in isolation is in  $O(\text{poly}(n \log(1/\epsilon))$  [7]. This efficiency justifies the choice to consider such simulations as oracles in the prior discussion. As  $H_M$  commutes with the  $H_E$  term and is also 1-sparse, we may also opt to move into the combined interaction frame of the  $H_E$  and  $H_M$  terms. In this case, it will suffice to simulate only the  $H_h$  term via qubitization, and the simulation of this term will be the biggest asymptotic driver of the query complexity.

Recall that the PREPARE oracle acts on an empty ancilla register of  $O(\log L)$  qubits, if L is the number of terms in the decomposition of the Hamiltonian into unitary operators, and prepares the superposition state

$$PREPARE \equiv \sum_{l=1}^{L} \sqrt{\frac{w_l}{\lambda}} |l\rangle\langle 0|,$$

where  $w_l$  denotes the coefficients of the terms in the decomposition of  $H_h$  and  $\lambda = \sum_l |w_l|$  is the sum of the absolute value of the coefficients in the  $H_h$  term. Note that this oracle does not get altered when moving into the interaction frame since the coefficients  $w_l$  remain the same. Since there are 8(N-1) terms in the LCU decomposition of  $H_h$ , we may set L=8(N-1). There is only one type of coefficient in  $H_h$  in terms of magnitude, so  $w_l/\lambda=1/L$  and we obtain for our situation

PREPARE 
$$\equiv \frac{1}{\sqrt{L}} \sum_{l=1}^{L} |l\rangle\langle 0|.$$
 (58)

As a result, we can scale every term in our Hamiltonian by a factor of 8a and scale the simulation time by a factor of 1/(8a).

On the other hand, a modification of the traditional select oracle is used to incorporate the interaction picture:

SELECT' 
$$\equiv \sum_{l} |l\rangle\langle l| \otimes e^{i(H_E + H_M)t} H'_l e^{-i(H_E + H_M)t}$$
  
 $= (I \otimes e^{i(H_E + H_M)t}) (\sum_{l} |l\rangle\langle l| \otimes H'_l) (I \otimes e^{-i(H_E + H_M)t}).$  (59)

This is merely the customary SELECT oracle but conjugated by the unitary operator  $e^{iH_Et}e^{iH_Mt}$  on the data qubits since  $H_E$  and  $H_M$  commute. It thus suffices to give circuit implementations of the usual SELECT oracle.

To summarize, since the conditions of Theorem 4.2 are satisfied, we have the following corollary:

Corollary 5.1 (Hybrid qDRIFT and Qubitization I.P Simulation for the Schwinger Model). Let  $H = H_E + H_M + H_h$  be the Schwinger model Hamiltonian as given in (49), (50), and (51). Then we can perform the Hamiltonian simulation of H with the method of Theorem 4.2 using a total number of queries to PREPARE, SELECT, and  $W_{H_M+H_E}(t)$  in

$$O\left(\frac{N^2 t^2}{a^2 \epsilon} \frac{\log(Nt/a\epsilon)}{\log\log(Nt/a\epsilon)}\right). \tag{60}$$

Here, N is the number of sites in the system, a is the lattice spacing,  $t \ge 0$  is the simulation time, and  $\epsilon$  is the error quantifying the distance in 1-norm from the ideal time-evolution channel.

*Proof.* Note that  $H_h$  is manifestly a linear combination of unitary operators and that  $H_M$  and  $H_E$  are diagonal, and therefore 1-sparse, and commute with each other. Thus, the conditions of Theorem 4.2 are satisfied and we may move into the interaction frame of both the  $H_M$  and  $H_E$  terms.

To compute the explicit form of  $\lambda'$ , note that  $H_h$  consists of a sum over 8(N-1) unitary terms each with a coefficient of absolute value 1/(8a). We therefore have (N-1)/a for the overall sum. Thus

$$\lambda' = \frac{N-1}{a}. (61)$$

Now note that  $||U||_{\infty} = 1$  for any unitary operator U. Then we have  $||H_h||_{\infty} \leq \lambda'$  by using the triangle-inequality and the sub-multiplicativity of the Schatten infinity norm. Substituting these relationships into (38) and retaining the dominant terms gives the claimed query complexity.  $\square$ 

Corollary 5.2 (Hybrid Trotter, qDRIFT, and qubitization I.P Simulation for Schwinger Model). Let  $H = H_E + H_M + H_h$  be the Schwinger model Hamiltonian as given in (49), (50), and (51). Then

we can perform the Hamiltonian simulation of the Schwinger model with the method of Theorem 4.3 using a number of queries to PREPARE, SELECT, and  $W_{H_E+H_M}(t)$  in

$$O\left(\frac{Nt^2}{a^2\epsilon} \frac{\log(Nt^2/(a^2\epsilon^2))}{\log\log(Nt^2/(a^2\epsilon^2))}\right).$$
(62)

Proof. We directly apply Corollary 3.3 to the situation where we move into the interaction frame of  $H_E$  and  $H_M$ , leaving only the  $H_h$  term of the Schwinger model remaining. For the terms in  $H_h$ , we use the notation  $U_r\sigma_r^i\sigma_{r+1}^j$ , where i=1 or 2 so that  $\sigma_r^1=X_r$  and  $\sigma_r^2=Y_r$ . Since  $[U_r,U_s]=0$  for all r,s and  $[U_r,U_r^\dagger]=0$  since  $U_r$  is unitary (and therefore normal), we need only focus on the commutators between the Pauli matrices in computing  $c_I$ . But since Pauli operators acting on different sites commute, we can further specialize to considering those terms that yield  $[X_r,Y_r]=iZ_r$ . Therefore, given a term  $U_r\sigma_r^i\sigma_{r+1}^j$ , it fails to commute with only  $U_{r-1}\sigma_{r-1}^k\sigma_r^l$  and  $U_{r+1}\sigma_{r+1}^m\sigma_{r+2}^n$ , with analogous statements holding for  $U_r^\dagger\sigma_r^i\sigma_{r+1}^j$ . In other words, the terms involving a particular site r fail to commute with only those involving adjacent sites. Terms such as  $[U_rX_rX_{r+1}, U_rY_rY_{r+1}]$  do not contribute since

$$[U_r X_r X_{r+1}, U_r Y_r Y_{r+1}] = U_r^2 X_r Y_r X_{r+1} Y_{r+1} - U_r^2 Y_r X_r Y_{r+1} X_{r+1} = 0,$$

where we've used in the anti-commutation relation twice  $\{X_k, Y_k\} = 0$  to obtain the last equality. Therefore, we can decompose  $H_h$  into "even" and "odd" pieces as follows:

$$\begin{split} H_h^{\text{even}} &= \frac{1}{8a} \sum_{r=1}^{(N-1)/2} [(U_{2r} + U_{2r}^{\dagger})(X_{2r}X_{2r+1} + Y_{2r}Y_{2r+1}) + i(U_{2r} - U_{2r}^{\dagger})(X_{2r}X_{2r+1} - Y_{2r}Y_{2r+1})] \\ H_h^{\text{odd}} &= \frac{1}{8a} \sum_{r=1}^{(N-1)/2} [(U_{2r-1} + U_{2r-1}^{\dagger})(X_{2r-1}X_{2r} + Y_{2r-1}Y_{2r}) + i(U_{2r-1} - U_{2r-1}^{\dagger})(X_{2r-1}X_{2r} - Y_{2r-1}Y_{2r})]. \end{split}$$

From the preceding discussion, given a particular term in the "odd" sum, there are exactly two terms in the even sum that fail to commute with it. In particular, there is exactly one term in  $H_I^{\text{even}}$  with higher site index that fails to commute with it. Then by the definition of  $c_I$ ,

$$c_I = \|[H_p^{\text{even}}, H_q^{\text{odd}}]\| = \frac{(N-1)}{2} \frac{1}{64a^2} = \frac{N-1}{128a^2}.$$

Similarly, since each term in  $H_h$  has norm 1, we have

$$4\sum_{r=1}^{N-1} \|H_h\|_{\infty}^2 \le \frac{32(N-1)}{64a^2}.$$

Substituting these into (37) gives

$$r \ge \frac{65(N-1)t^2}{128a^2\epsilon}. (63)$$

Substituting this and L=2 into (44) and retaining the dominant terms gives

$$O\left(\frac{Nt^2}{a^2\epsilon} \frac{\log(Nt^2/(a^2\epsilon^2))}{\log\log(Nt^2/(a^2\epsilon^2))}\right)$$
(64)

as claimed. Note that these choices for the errors ensure that the total error for approximation of the ideal time-evolution channel via this entire procedure is  $\epsilon/2 + (2r)(\epsilon/4r) = \epsilon/2 + \epsilon/2 = \epsilon$ .

Comparing the results of the preceding corollaries, we see that Trotterizing first before applying qDRIFT can result in improvements in the query complexity in situations where the Hamiltonian has additional commutator structure that can be exploited. For unstructured problems, the additional Trotterization step is not generally useful.

#### 5.2 Construction of Prepare and Select Oracles

We now give high-level circuit implementations of the aforementioned SELECT and PREPARE oracles for the  $H_h$  term of the Schwinger model.

We opt to employ a unary encoding of the control qubits  $|c_i\rangle$  needed for the prepare and select oracles, i.e.  $|i\rangle = |0...1...0\rangle$ , where the 1 occurs on the *i*-th spot in the ket. Though this encoding requires a number of qubits linear in the number of terms in the LCU decomposition rather than logarithmic for the implementation of the oracles, it greatly simplifies the control structures required within the circuits.

To implement the select oracle for  $H_h$ , we exploit certain patterns within the coefficients of the terms in  $H_h$ . Note that there are terms with  $U_r^{\dagger}$  and  $U_r$ , phases of  $\pm i$ , and  $X_r$  and  $Y_r$ . We can switch between X and Y via the identity  $SXS^{\dagger} = Y$ . From techniques involving two's complement numbers, there exists a unitary operator Q that can flip  $U_r$  to  $U_r^{\dagger}$  [43]. Lastly, the factors  $\pm i$  can be inserted via suitable insertions of controlled-Z gate and controlled-Z gate operations. The circuit that accomplishes this is given in Figure 4.

![](_page_22_Figure_4.jpeg)

Figure 4: SELECT circuit for the  $\mathcal{H}_h$  term in Schwinger Model

Here,  $|c_r\rangle$  represent the control qubits used to implement the controlled operations,  $|l_r\rangle$  the qubits corresponding to the links of the system, and  $|q_r\rangle$  the qubits corresponding to the sites. Note how the control gate structure in this unary encoding is much more simple than what would have been required with a binary encoding. Though the latter encoding would have required only  $\log(N-1)$  control qubits instead of N-1 as above, the advantage there is mitigated by the fact that numerous multi-controlled gates would have been required.

Since the terms in  $H_h$  for a given r only differ by coefficients of  $\pm 1$  or  $\pm i$ , these can be implemented via the insertion of a Z or S gate through the above constructions that exploit the aforementioned patterns in  $H_h$ . Note that the number of qubits needed to specify the state of link  $|l_r\rangle$  will depend on the cut off for the electric energy term chosen. If our cutoff is  $\Lambda$ , then  $|l_r\rangle$  will be a log  $\Lambda$ -qubit state and  $U_r$  a log  $\Lambda$ -qubit operator.

The circuit implementation of the PREPARE oracle reduces to preparing a uniform superposition state in binary, as per (58), and then converting the encoding to a unary one. The overall circuit with the general pattern is depicted in Figure 5 with  $k = \log(8(N-1))$  ancilla control

qubits. Note that since in the unary encoding an integer k is expressed as a state with a 1 in the k-th spot and 0's elsewhere, the X gate on  $|0\rangle_1$  and the subsequent swaps have the effect of permuting the 1 to the appropriate position.

![](_page_23_Figure_1.jpeg)

Figure 5: PREPARE circuit for the  $\mathcal{H}_h$  term in Schwinger Model

The control structure on the bits  $b_j$  encoding the binary integers for the controlled-swap gates is given precisely by the binary representation of that index. For example, since the binary integer  $|00...1\rangle$  gets mapped to  $|01...0\rangle$  in our unary encoding, we have to do a swap on the  $|0\rangle_1$  and  $|0\rangle_2$  qubits controlled on the first k-1 b qubits being 0 and  $b_k$  being 1.

#### 5.3 Gate Complexity Analysis

We now analyze the gate complexity per query to CTRL(W) of our simulation protocol and do so by analyzing the circuits given in Figure 4 and Figure 5. It suffices to express the complexity in terms of Toffoli gates since they dominate the computational complexity compared to Clifford operations.

Our analysis proceeds as follows:

1. First consider the PREPARE<sup>†</sup> and PREPARE operations in Figure 1. We make the approximation that they have roughly the same gate complexity and that it therefore suffices to determine the gate complexity of just the PREPARE circuit.

From Figure 5, note that we have N-1 multiply-controlled swap gates since we needed to perform a binary-to-unary conversion to the N-1 qubits we have. Each can be converted to standard  $C^k(SWAP)$  by inserting X gates on either side of the 0 controls. Since we are assuming Pauli operations are approximately cost-free, it suffices to determine the gate complexity of these N-1  $C^k(SWAP)$  gates. Standard circuit arguments show that the following identities hold:

![](_page_23_Picture_9.jpeg)

Thus, each  $C^k(\mathrm{SWAP})$  gate can be decomposed into a  $C^{k+1}(\mathrm{NOT})$  gate and 2 CNOT gates. From Corollary 1 in [44], we get that  $C^{k+1}(\mathrm{NOT})$  gate can be decomposed into 8(k+2)-24=8k-8 Toffoli gates using only a single auxiliary qubit that can be reused. This gives roughly 2(N-1)(8k-8) Toffoli gates that are needed for both the PREPARE and PREPARE<sup>†</sup> parts of Figure 1. Overall we have a gate complexity of

 $O(N \log N)$ 

with 1 ancilla qubit needed.

The methods in [45] can be used to perform PREPARE circuit with  $N \log N$  controlled swap gates, each of which can be decomposed into at most four non-Clifford operations using [46]. This results in a smaller gate cost but ultimately does not affect the asymptotic gate complexity shown above.

2. The multiply-controlled Z gate in Figure 1 is controlled only on the N-1 control qubits that make up the unary encoding portion of Figure 5. Applying the above corollary again, we get a gate complexity of

O(N)

with 1 ancilla qubit needed.

3. To analyze the gate complexity of the controlled-SELECT operation in Figure 1, we first examine the operations that don't involve  $U_r$  and Q. The external control distributes among the operations involving the 2(N-1) controlled-S and controlled- $S^{\dagger}$  gates, 2(N-2)+2 controlled- $X_r$  gates, and the final 3 CNOT operations. Adding these together yields a total of 4N-1 Toffoli gates, giving a gate complexity of

O(N)

with no ancilla qubits needed.

4. For the  $U_r$  gates, note that its action on states is that of an incrementer. This can be implemented by utilizing the quantum ripple-carry adder circuit given by Cuccaro [47]. Since we increment  $\log \Lambda$ -qubit numbers, the gate complexity is given in the paper to be  $2 \log \Lambda - 1$  Toffoli gates,  $5 \log \Lambda - 3$  CNOTs, and  $2 \log \Lambda - 4$  negations.

Since we must perform a controlled- $U_r$  operation for the walk operator, we get  $(5 \log \Lambda - 3)$  Toffoli gates, and  $(2 \log \Lambda - 1)$   $C^3(\text{NOT})$  gates. Again from Corollary 1 in [44], the latter is equivalent to  $8(2 \log \Lambda - 1)$  Toffoli gates with 1 extra qubit needed. Since we must perform N-1 of these  $U_r$  operations, we have altogether  $(N-1)(21 \log \Lambda - 11)$  Toffoli gates, giving a gate complexity of

$$O(N \log \Lambda)$$

with 1 ancilla qubit needed.

5. The Q and  $Q^{\dagger}$  operations can be implemented with  $O(\log(\Lambda))$  Toffoli gates each (see [43]), with the extra controls giving only constant pre-factors to the cost. Since there are 2(N-1) of these operations performed, we have a gate complexity of

$$O(N \log \Lambda)$$

6. Finally, the cost of performing the diagonal Hamiltonian simulation is  $O(N \log^2(\Lambda))$  as the computation of the diagonal elements of the Hamiltonian involves squaring the input value, which can be performed in time  $O(\log^2(\Lambda))$  (see Lemma 2 of [48]).

These considerations give us the following corollaries:

Corollary 5.3 (Gate Complexity for Hybrid qDRIFT and Qubitization I.P. Simulation of Schwinger Model). Let  $H = H_h + H_M + H_E$  be the Schwinger model Hamiltonian as given in (49), (50), and (51). Then the Hamiltonian simulation of H can be performed using the method of Theorem 4.2 with a gate complexity in

$$O\left(\frac{N^3 t^2}{a^2 \epsilon} \frac{\log(Nt/a\epsilon)}{\log\log(Nt/a\epsilon)} \log^2(N\Lambda)\right),\tag{65}$$

with an ancilla qubit overhead of O(1). In  $\tilde{O}$  notation, the gate complexity is

$$\tilde{O}\left(\frac{N^3 t^2}{a^2 \epsilon} \log^2 \Lambda\right). \tag{66}$$

*Proof.* Summing up the scaling results from steps 1-6 as outlined above, we get a *per-query* gate complexity of

$$O(N\log^2(\Lambda) + N\log(N)) \subseteq O(N\log^2(N\Lambda)). \tag{67}$$

Multiplying these by (60) and retaining the dominant terms yields the stated results.

Corollary 5.4 (Gate Complexity for Hybrid Trotter, qDRIFT, Qubitization I.P. Simulation of Schwinger Model). Let  $H = H_h + H_M + H_E$  be the Schwinger model Hamiltonian as given in (49), (50), and (51). Then the Hamiltonian simulation of H can be performed using the method of Theorem 4.3 with a gate complexity in

$$O\left(\frac{N^2 t^2}{a^2 \epsilon} \frac{\log(N t^2 / (a^2 \epsilon^2))}{\log\log(N t^2 / (a^2 \epsilon^2))} \log^2(\Lambda)\right),\tag{68}$$

with an ancilla qubit overhead of O(1). In  $\tilde{O}$  notation, the gate complexity is

$$\tilde{O}\left(\frac{N^2t^2}{a^2\epsilon}\log^2(\Lambda)\right). \tag{69}$$

*Proof.* Multiplying (62) by  $N \log(N\Lambda)$  gives the big-O cost. Dropping all sub-dominant logarithmic factors gives the  $\tilde{O}$  scaling.

#### 5.4 Comparison with Trotterization

The results of (66) and (69) can be directly compared with the result given in Corollary 11 of [48] for using a second-order Trotter-Suzuki formula to perform the quantum simulation of the Schwinger model. We will first consider the regime in which simulations are carried at constant 1/(ga) = O(1) and for fixed m/g = O(1). For this condition, we can use the result in Corollary 9 of [48] which after rescaling the time variable  $T \to ag^2t/2$  to align with our normalization conventions for the Schwinger Model Hamiltonian, gives a total T-gate cost of

$$\tilde{O}\bigg(\frac{N^{3/2}t^{3/2}\Lambda a^{1/2}g^2}{\epsilon^{1/2}}\bigg) = \tilde{O}\bigg(\frac{N^{3/2}t^{3/2}\Lambda g^{3/2}}{\epsilon^{1/2}}\bigg)\;.$$

In the same regime, the result of (69) gives a gate complexity in

$$\tilde{O}\bigg(\frac{N^2t^2}{a^2\epsilon}\log^2(\Lambda)\bigg) = \tilde{O}\bigg(\frac{N^2t^2g^2}{\epsilon}\log^2(\Lambda)\bigg)\;.$$

We then see that the hybrid I.P. scheme provides a quasi-exponential speedup with respect to the electric cutoff  $\Lambda$  over the second-order Trotter-Suzuki approach, at the expense of a slightly worse scaling in all the other parameters  $(N, t, g, \epsilon)$ .

In order to extract physical observables however, it is important to consider that the number of sites N and the the lattice spacing cannot be chosen independently as the product L=Na gives the physical size of the system. In past numerical simulations it was found that choosing Nga=O(10) is appropriate for a large number of configurations (see e.g. [36]). In order to keep our derivation general, we will then introduce the dimensionless parameter l=Nga. In addition to the thermodynamic limit  $Na \to \infty$ , one also has to work with  $ga \to 0$  in order to recover the continuum limit of the theory. The resulting gate complexity of the hybrid I.P. algorithm from Corollary 5.4 is found to be

$$\tilde{O}\left(\frac{l^2t^2}{g^2a^4\epsilon}\log^2(\Lambda)\right)$$
,

while for the second order Trotter-Suzuki scheme we have to consider two distinct regimes

• large cutoff limit  $\Lambda ga > 1$ , in which case the T-gate count is bounded by

$$\tilde{O}\left(\frac{l^{3/2}t^{3/2}\Lambda}{a^{3/2}\epsilon^{1/2}}\right)\,,$$

• small lattice spacing limit  $\Lambda ga < 1$ , in which case the result of Corollary 9 of [48] does not hold anymore. The T-gate count can be found instead by using the more general result from Corollary 11 there, resulting in the  $\Lambda$ -independent scaling

$$\tilde{O}\!\left(\frac{l^{3/2}t^{3/2}}{g^{3/2}a^3\epsilon^{1/2}}\right)$$
 .

These results show that for fixed error  $\epsilon$  and lattice extent l, the hybrid I.P. approach can be especially beneficial in the first regime thanks to the poly-logarithmic dependence on the cutoff  $\Lambda$ . In the small lattice spacing regime relevant for the continuum limit, the second order Trotter-Suzuki scheme developed in [48] has instead a better scaling with respect to all the parameters.

Finally, for the continuum limit it might be possible to improve the the gate complexity in some regimes by choosing to perform the I.P. simulation in the rotating frame given by the the interaction Hamiltonian  $H_h$  instead. Using the hybrid Trotter and qDRIFT scheme from Corollary 3.3, together with the implementation via qubitization of the time evolution operator for  $H_h$  derived in Section 5.2, this scheme has gate cost in

$$\tilde{O}\!\left(\frac{N^2t}{a} + \frac{N^2t^2}{\epsilon}\left(m^2 + g^4a^2\Lambda^4\right)\,\right)\,.$$

For m/g = O(1) and introducing the dimensional lattice size l = Nga, this becomes

$$\tilde{O}\!\left(\frac{l^2t}{g^2a^3} + \frac{l^2t^2}{a^2\epsilon} + \frac{l^2t^2}{\epsilon}g^2\Lambda^4\right).$$

This is clearly worse than either the Hybrid approaches discussed above or the second order Trotter-Suzuki scheme from [48] in the large cutoff limit  $\Lambda ga > 1$ , but can become competitive in the small lattice spacing limit  $\Lambda ga < 1$  for some choices of  $(\epsilon, l, \Lambda)$ .

A detailed comparison of these different schemes to extract continuum quantities of physical interest in the Schwinger model with some target precision  $\delta$  would require a more careful analysis of the scaling of the lattice size l and the electric field cutoff  $\Lambda$ , as well as a more careful consideration of the logarithmic factors hidden by the  $\tilde{O}$  notation. We leave this interesting extension of the present work to future studies.

#### 6 Collective Neutrino Oscillations

In extreme astrophysical environments, such as supernova explosions, neutrinos are present in such large densities that neutrino-neutrino interactions can become important to describe flavor evolution [49, 50]. These interactions are responsible for the appearance of collective modes in flavor oscillations and have traditionally been studied with the help of a mean-field approximation (see e.g. [51, 52] for reviews). Due to the presence of interactions, many-body effects and quantum correlations could be important in understanding these phenomena and a number of studies is underway with a variety of techniques: from exact diagonalization [53] to Bethe-ansatz solutions [54], from tensor networks [55, 56] to digital quantum simulations [57, 58]. Quantum computing might offer a promising route to study these phenomena in situations where the entanglement entropy grows too fast with system size for tensor network simulations to remain feasible.

An important obstacle towards describing collective oscillations in realistic regimes is the fact that besides interactions with other neutrinos, scattering with external leptons (especially the abundant electrons) is an important effect near the proto-neutron star. The matter interaction terms can become the dominant contributions in this regime, requiring very small time-steps for an accurate simulation of the flavor dynamics. On the quantum computing side, this requirement translates into a large number of gates required for the simulation and it is therefore important to design simulation algorithms with a gentle computational scaling with the external matter density.

The Hamiltonian we are interested in can be written as follows (see e.g. [59] for a derivation)

$$H = \sum_{i=1}^{N} \frac{\omega_i}{2} \vec{B} \cdot \vec{\sigma}_i + \frac{\lambda}{2} \sum_{i=1}^{N} Z_i + \frac{\mu}{2N} \sum_{i < j}^{N} J_{ij} \vec{\sigma}_i \cdot \vec{\sigma}_j .$$
 (70)

Here  $\vec{\sigma}_i$  is the vector of Pauli matrices acting on the *i*-th qubit and the single particle energies  $\omega_i$  are positive for neutrinos and negative for anti-neutrinos. The coupling matrix  $J_{ij}$  takes values in [0,2] and the normalized vector  $\vec{B}$  contains the vacuum mixing angle as  $\vec{B} = (\sin(2\theta), 0, -\cos(2\theta))$ . The constants are given by  $\lambda = \sqrt{2}G_F n_e$  and  $\mu = \sqrt{2}G_F n_\nu$ , with  $G_F$  Fermi's constant and  $n_e$  and  $n_\nu$  the electron and neutrino densities respectively. In typical situations the electron contribution  $\lambda$  is the dominant term. A standard approach to deal with this problem is to move to the rotating frame defined by the unitary  $U_e(t) = \exp(-i\frac{t}{2}\lambda\sum_{i=1}^N Z_i)$  and define the Hamiltonian in the interaction picture as

$$H(t) = U_e^{\dagger}(t)HU_e(t) - iU_e^{\dagger}(t)\frac{\partial}{\partial t}U_e(t)$$

$$= \sin(2\theta)\sum_{i=1}^{N} \frac{\omega_i}{2} \left(\cos(\lambda t)X_i - \sin(\lambda t)Y_i\right) - \cos(2\theta)\sum_{i=1}^{N} \frac{\omega_i}{2}Z_i + \frac{\mu}{2N}\sum_{i< j}^{N} J_{ij}\vec{\sigma}_i \cdot \vec{\sigma}_j \qquad (71)$$

$$= e^{i\lambda\sum_i Z_i t} H_{\nu} e^{-i\lambda\sum_i Z_i t},$$

where

$$H_{\nu} = \sum_{i=1}^{N} \frac{\omega_i}{2} \vec{B} \cdot \vec{\sigma}_i + \frac{\mu}{2N} \sum_{i < j}^{N} J_{ij} \vec{\sigma}_i \cdot \vec{\sigma}_j . \tag{72}$$

Typically only the leading order contribution in the Magnus expansion is retained, giving the time-independent Hamiltonian

$$H_0 = -\cos(2\theta) \sum_{i=1}^{N} \frac{\omega_i}{2} Z_i + \frac{\mu}{2N} \sum_{i < j}^{N} J_{ij} \vec{\sigma}_i \cdot \vec{\sigma}_j .$$
 (73)

In this limit, flavor states will not experience oscillations and typically this is solved by defining the flavor axis to be rotated by a small phenomenological amount away from the Z axis. It would be desirable however to be able to exercise more control in this approximation. Expansions to high orders in the Magnus expansion quickly produce higher order interactions which will complicate the implementation of the corresponding time-independent evolution. Here we use the time-dependent algorithm described above to work directly in the interaction picture without introducing uncontrollable errors.

#### 6.1 Trotter Suzuki Approximations in Interaction Frame

As a first step, let us consider simulating the Hamiltonian in the interaction frame using a  $k^{\text{th}}$ order Trotter-Suzuki formula such as those in [8]. To do this, we need to introduce a notion of the
typical energy scale of the time-dependent Hamiltonian with respect to the Trotter decomposition
of the interaction frame Hamiltonian. If we use a conventional Trotter decomposition, as opposed
to (18), we find that the error incurred from using a first-order Trotter formula for an ordered
operator exponential  $U_1(t)$  formed by evaluating the Hamiltonian at t=0 and then Trotterizing
the resultant ordinary operator exponential is

$$\left\| \exp_{\tau} \left( -i \int H(t) dt \right) - U_1(t) \right\|_{\infty} \in O((\max_{t} \|H'(t)\|_{\infty} + \sum_{p,q} \max_{t} \|[H_p(t), H_q(t)]\|_{\infty}) t^2), \quad (74)$$

where the specific constants can be found using the techniques in [33]. The derivative of the Hamiltonian in the interaction frame is in

$$||H'(t)||_{\infty} \in O(\theta N\lambda). \tag{75}$$

The commutator sum similarly obeys

$$\|\sum_{p,q} \max_{t,t'} \|[H_p(t'), H_q(t)]\|_{\infty} \in O\left(N\omega\theta + \mu N\theta + \omega N\mu + N\mu^2\right)$$

$$= O\left(N(\theta(\omega + \mu) + \mu(\omega + \mu))\right)$$

$$\subset O\left(N\mu^2\right), \tag{76}$$

where  $\omega = \max_i |\omega_i|$  and in the last term we take  $\mu \gg \omega$ .

The overall error in the simulation is therefore

$$O\left((N\mu^2 + \theta N\lambda)t^2\right). \tag{77}$$

If we break the overall evolution into r time slices, then it follows that the error in the simulation can be made at most  $\epsilon$  by choosing

$$r \in O\left(\frac{N(\mu^2 + \theta\lambda)t^2}{\epsilon}\right). \tag{78}$$

As there are  $O(N^2)$  operator exponentials per time step, the total number of operator exponentials needed to perform the simulation is

$$N_{\text{exp}} \in O\left(\frac{N^3(\mu^2 + \theta\lambda)t^2}{\epsilon}\right).$$
 (79)

Since each operator exponential requires O(1) gates from the  $H, R_z$ , CNOT gate library, the gate complexity is also proportional to this [7]. Interestingly, using the swap-network protocol from Ref. [57] (and inspired from their fermionic variant [60]), this cost is not affected by limited connectivity in the device despite the interaction being all-to-all. This cost also coincides with the optimal scaling with  $\lambda$  permitted by the no-fast forwarding theorem [27], despite being a low-order formula that has inferior scaling with respect to the other parameters relative to alternative simulation methods.

Higher-order time-dependent Trotter formulas for the simulation can be used, but the advantage gleaned by using them with respect to the  $\lambda$  scaling is less clear. Such algorithms scale with the parameter [8]

$$\Lambda_k^{k+1}/r^k = \max_{j < k} (\|\partial_t^j H(t)\|_{\infty}^{1/j+1})^{k+1}/r^k \in O(\lambda^k/r^k), \tag{80}$$

where k represents the order of the Trotter formula. It then follows that these formulas ultimately lead to the same linear scaling in the gate complexity with  $\lambda$  (assuming that  $\theta \in \Theta(1)$ ). By contrast, if we did not use the interaction picture algorithm, the cost of simulation using the  $k^{\text{th}}$ -order Trotter time-independent formula would scale as  $O(\lambda^{1+1/2k})$  [7, 8]. This illustrates that for problems with an imbalance in the scales of the operators, switching to an interaction frame can be beneficial at virtually no cost overhead.

#### 6.2 Simulating Neutrino Oscillations using Hybrid Trotter-qDRIFT

Now we will apply Corollary 3.3 to compare this cost to that required by the hybrid Trotter and continuous qDRIFT algorithm. Specifically, the error in an r-segment simulation is of the form (under the assumption that  $\mu \gg \omega$ )

$$\frac{t^2}{r} \left( c_I + 4 \sum_{k \neq l}^{L} \|H_k\|_{\infty}^2 \right) \in O\left(\frac{N\mu^2 t^2}{r}\right). \tag{81}$$

As each segment of qubitization requires application of a first order Trotter formula, the cost per segment in terms of operator exponentials scales as  $O(N^2)$ . Thus if we demand that the error is at most  $\epsilon$ , the cost is

$$N_{\text{exp}} \in O(N^2 r) \subseteq O\left(\frac{N^3 \mu^2 t^2}{\epsilon}\right),$$
 (82)

wherein each operator exponential requires O(1) applications of  $H, R_z$  and CNOT. This shows that the above asymptotic scaling applies in the gate complexity as well as the number of exponentials.

Interestingly, in the limit where  $\lambda \gg 1$ , this result provides better scaling than even the gate complexity of the truncated Dyson series [20, 21] which scales in the interaction frame as  $\log(\lambda)$ . In our case, the quantum computational complexity is completely independent of  $\lambda$ . Of course, polylogarithmic costs with these algorithms need to be incurred at the classical side to compute the

rotation angles that go into the single qubit rotations but such costs are assumed to be negligible in our cost model. This implies that for such cases where the cost of the simulation is gated by the cost of preparing and controlling from the time-register, switching to a method that only requires classical controls can allow us to outperform such methods and make the gate count (rather than just the query complexity [21]) independent of the magnitude of the norm of the interaction Hamiltonian.

As a final note, similar scaling can also be attained by using the approach of [9] to time-order the operator exponentials that we use in the interaction frame. The performance of this method is summarized in (18) and gives an alternative to the hybrid approach considered here and yields comparable scaling with  $\lambda$ .

# 7 Constrained Hamiltonian Dynamics

As a final application of these techniques, let us consider the application of quantum simulation to dynamics subject to dynamical constraints. Specifically, we will consider a Hamiltonian of the form

$$H = H_f + \lambda P_c, \tag{83}$$

where  $H_f \in \mathbb{C}^{2^n \times 2^n}$  is the free Hamiltonian and  $P_c \in \mathbb{C}^{2^n \times 2^n}$  is a projector onto an infeasible region. The idea behind our approach to simulating constrained quantum dynamics is that if we choose  $\lambda \gg \|H_f\|_{\infty}$  and an initial state  $|\psi\rangle = (\mathbb{I} - P_c)|\psi\rangle$ , then the dynamics of the quantum system will, up to small errors, be confined to within the dynamically feasible region specified by the null-space of  $P_c$ . Note that this result is reminiscent of others in the literature such as [61, 62]; however, this result is specialized to time evolution and is simpler to employ in this context.

**Lemma 7.1.** Let  $H_f \in \mathbb{C}^{2^n \times 2^n}$  be a free Hamiltonian for a system and let  $\lambda$  be a variable describing the strength of the constraint such that  $||H_f||_{\infty} \ll \lambda$ . We then have that for any  $|\psi\rangle$  in the null-space of  $P_c$ ,

$$||e^{-i(H_f - \lambda P_c)t}|\psi\rangle - \lim_{\lambda \to \infty} e^{-i(H_f - \lambda P_c)t}|\psi\rangle||_2 \in O\left(\frac{||H_f||_{\infty}^2 t}{\lambda}\right)$$

where  $\|\cdot\|_2$  refers to the vector 2-norm.

*Proof.* In order to show the deviation in each eigenvector of the Hamiltonian that arises from adding the small Hamiltonian  $H_f$  to the constraint term, we will introduce

$$H_f(x) := H_f x + \lambda P_c, \tag{84}$$

where  $x \in [0, 1]$ . For x = 0,  $H_f(0) = \lambda P_c$  has a degenerate null-space denoted  $\mathcal{P}^0$ . Let  $|v_j(x)\rangle$  denote the eigenvectors of  $H_f(x)$  with corresponding eigenvalues  $E_j(x)$ . We then have from perturbation theory that the derivative of  $|v_j(x)\rangle$  is

$$\frac{\partial |v_j(x)\rangle}{\partial x} = \sum_{k \neq j} |v_k(x)\rangle \frac{\langle v_k(x)|H_f|v_j(x)\rangle}{E_j(x) - E_k(x)}$$
(85)

Assuming that the eigenvalue gaps are non-zero, we further have that the second derivative is finite. From the definition of a Riemann integral, we get

$$|v_{j}(1)\rangle = \int_{0}^{1} \frac{\partial |v_{j}(x)\rangle}{\partial x} dx = |v_{j}(0)\rangle + \lim_{r \to \infty} \sum_{p=2}^{r} \sum_{k \neq j} |v_{k}((p-1)/r)\rangle \frac{\langle v_{k}((p-1)/r)|H_{f}|v_{j}((p-1)/r)\rangle}{E_{j}((p-1)/r) - E_{k}((p-1)/r)} \frac{1}{r}.$$
(86)

This expression allows us to relate the shift in the eigenvectors recursively. First let us consider the initial time step. As  $H_f(x)$  is degenerate at x=0, we can choose the eigenvectors such that the matrix with components  $\langle v_j(0)|H_f|v_k(0)\rangle$  is a diagonal matrix for all  $|v_j(0)\rangle, |v_k(0)\rangle \in \mathcal{P}^0$  or  $|v_j(0)\rangle, |v_k(0)\rangle \in \mathcal{P}^{0\perp}$ . In the former case we have that  $(\mathbbm{1}-P_c)|v_j(0)\rangle = |v_j(0)\rangle$ , so  $\langle v_j(0)|H_f|v_k(0)\rangle = \langle v_j(0)|(\mathbbm{1}-P_c)H_f(\mathbbm{1}-P_c)|v_k(0)\rangle$ . Thus we can achieve the diagonal criteria by choosing each  $|v_j(0)\rangle$  to be an eigenvector of  $(\mathbbm{1}-P_c)H_f(\mathbbm{1}-P_c)$ . Similarly, we can achieve

the diagonal criteria for each vector in  $\mathcal{P}^{0\perp}$  by choosing each  $|v_j\rangle$  to be an eigenvector of  $P_cH_fP_c$ . We then have that for any  $|v_j(0)\rangle$  in  $\mathcal{P}^0$ ,

$$|v_{j}(1/r)\rangle = |v_{j}(0)\rangle + \frac{1}{r} \sum_{k \neq j} |v_{k}(0)\rangle \frac{\langle v_{k}(0)|H_{f}|v_{j}(0)\rangle}{E_{j}(0) - E_{k}(0)}$$

$$= |v_{j}(0)\rangle - \sum_{k:|v_{k}(0)\rangle \neq \mathcal{P}^{0}} |v_{k}(0)\rangle \frac{\langle v_{k}(0)|H_{f}|v_{j}(0)\rangle}{\lambda r} . \tag{87}$$

In turn

$$||v_j(0)\rangle - |v_j(1/r)\rangle||_2 \in O(||H_f||_{\infty}/\lambda r).$$
 (88)

Furthermore from [63], we have that for all k,  $|E_k(x) - E_k(0)| \le x ||H_f||_{\infty}$ . Now let us assume that for some integer  $q \ge 0$ 

$$||v_j(0)\rangle - |v_j(q/r)\rangle||_2 \in O(q||H_f||_{\infty}/\lambda r)$$
 (89)

We then have

$$|v_j((q+1)/r)\rangle = |v_j(q/r)\rangle + \frac{1}{r} \sum_{k \neq j} |v_k(q/r)\rangle \frac{\langle v_k(q/r)|H_f|v_j(q/r)\rangle}{E_j(q/r) - E_k(q/r)}$$
(90)

and therefore

$$|||v_j((q+1)/r)\rangle - |v_j(q/r)\rangle||_2 \in O\left(\frac{||H_f||_{\infty}}{(\lambda - 2||H_f||_{\infty})r}\right) = O\left(\frac{||H_f||_{\infty}}{\lambda r}\right).$$
 (91)

Thus we have

$$|||v_{j}((q+1)/r)\rangle - |v_{j}(0)\rangle||_{2} \leq |||v_{j}((q+1)/r)\rangle - |v_{j}(q/r)\rangle||_{2} + |||v_{j}(0)\rangle - |v_{j}(q/r)\rangle||_{2}$$

$$\in O\left(\frac{(q+1)||H_{f}||_{\infty}}{\lambda r}\right). \tag{92}$$

This in turn shows us that

$$|||v_j(1)\rangle - |v_j(0)\rangle||_2 \in O\left(\frac{||H_f||_{\infty}}{\lambda}\right). \tag{93}$$

Next by examining the differential equation for the eigenvalues, we have that the corresponding eigenvalue  $E_j(1)$  obeys

$$E_{j}(1) = E_{j}(0) + \int_{0}^{1} \frac{\partial E_{j}(x)}{\partial x} dx = \int_{0}^{1} \frac{\partial E_{j}(x)}{\partial x} dx$$
$$= \int_{0}^{1} \langle v_{j}(x) | H_{f} | v_{j}(x) \rangle dx = \langle v_{j}(0) | H_{f} | v_{j}(0) \rangle + O\left(\frac{\|H_{f}\|_{\infty}^{2}}{\lambda}\right) . \tag{94}$$

Similarly for any  $|v_j(0)\rangle \in \mathcal{P}^{0^{\perp}}$ ,  $E_j(1) = \lambda + \langle v_j(0)|H_f|v_j(0)\rangle + O\left(\frac{\|H_f\|_{\infty}^2}{\lambda}\right)$ . We therefore have from the triangle inequality that

$$||H(1) - \sum_{k} (\lambda \delta_{|v_{k}\rangle \in \mathcal{P}^{0\perp}} + \langle v_{k}(0)|H_{f}|v_{k}(0)\rangle |v_{k}(0)\rangle \langle v_{k}(0)|)||_{\infty}$$

$$\in O\left(\frac{||H_{f}||_{\infty}^{2}}{\lambda}\right). \tag{95}$$

We therefore have from the fact that  $||e^{-iHt} - e^{-iH't}||_{\infty} \le ||H - H'||_{\infty}t$  for all Hermitian matrices H and H' of equal dimension that

$$\|e^{-iH(1)t} - e^{-i\sum_{k} \left(\lambda \delta_{|v_{k}\rangle \in \mathcal{P}^{0\perp}} + \langle v_{k}(0)|H_{f}|v_{k}(0)\rangle|v_{k}(0)\rangle\langle v_{k}(0)|\right)}^{t}\|_{\infty} \in O\left(\frac{\|H_{f}\|_{\infty}^{2}t}{\lambda}\right). \tag{96}$$

Therefore for any  $|\psi\rangle \in \mathcal{P}^0$  we have that

$$\|e^{-iH(1)t}|\psi\rangle - \lim_{\lambda \to \infty} e^{-iH(1)t}|\psi\rangle\|_2 \in O\left(\frac{\|H_f\|_{\infty}^2 t}{\lambda}\right). \tag{97}$$

This shows that we can simulate constrained dynamics for time t within error  $\epsilon$  by choosing  $\lambda \geq \|H_f\|_{\infty}^2 t/\epsilon$ . This in turn leads to a substantial degradation of the scaling of most simulation algorithms if  $[H_f, P_c] \neq 0$ , because the Hamiltonian's norm scales with both the evolution time and the uncertainty desired in the simulation. This makes such constrained dynamics impractical for many applications.

This drawback can, however, be mitigated through the use of an interaction frame transformation. By transforming to the interaction frame of the constraint, we can perform the simulation at cost that is (in some cases) independent of the choice of  $\lambda$ . The cost of such simulations using a hybrid qubitization and qDRIFT algorithm is given below. We cite the complexity of this algorithm rather than truncated Dyson methods because such methods explicitly have a cost that scales logarithmically with  $\lambda$ ; whereas in some cases the quantum gate complexity will be independent of  $\lambda$ .

**Theorem 7.2.** Let the assumptions of Theorem 4.2 hold. Then there exists a quantum algorithm that implements, for any t > 0 and  $\epsilon > 0$ , a quantum channel that is a  $(1, O(\log(L)), \epsilon)$  block encoding of  $e^{-i(H_f + \lambda P_c)t}$ . Further this implementation requires a total number of queries to PREPARE, SELECT and  $W_{P_c}$  in

$$O\left(\beta t + \left(\frac{\|H_f\|_{\infty}^2 t^2}{\epsilon}\right) \frac{\log(\|H_f\|_{\infty} t/\epsilon)}{\log\log(\|H_f\|_{\infty} t/\epsilon)}\right).$$

Proof. The proof follows directly from previous results. Specifically we have that

$$||V|\psi\rangle - \lim_{\lambda \to \infty} e^{-i(H_f + \lambda P_c)t}||_2$$

$$\leq ||V|\psi\rangle - e^{-i(H_f + \lambda P_c)t}|\psi\rangle||_2 + ||e^{-i(H_f + \lambda P_c)t}|\psi\rangle - \lim_{\lambda \to \infty} e^{-i(H_f + \lambda P_c)t}|\psi\rangle||_2.$$
(98)

From Theorem 4.2, we have that the number of queries to PREPARE, SELECT and  $W_{P_c}$  needed to implement a  $(1, O(\log(L)), \epsilon/2)$  block encoding is in

$$O\bigg(\beta t + \bigg(\frac{\|H_f\|_{\infty}^2 t^2}{\epsilon}\bigg) \, \frac{\log(\|H_f\|_{\infty} t/\epsilon)}{\log\log(\|H_f\|_{\infty} t/\epsilon)}\bigg).$$

Next, from Theorem 7.1 we have that there exists a value of  $\lambda \in O(\|H_f\|_{\infty}^2 t/\epsilon)$  such that  $\|e^{-i(H_f + \lambda P_c)t}|\psi\rangle - \lim_{\lambda \to \infty} e^{-i(H_f + \lambda P_c)t}|\psi\rangle\|_2 \le \epsilon/2$ . The result then follows from the triangle inequality.

These results show that query efficient methods exist for simulating Hamiltonian dynamics; however, the existence of a query efficient algorithm for simulating dynamics subject to a particular constraint does not imply the existence of a gate efficient algorithm. For example, let us consider the case where  $P_c|x\rangle = |x\rangle$  if and only if  $E(x) \leq \delta$  for some  $\delta > 0$  and E(x) is the energy function for an arbitrary Ising model. Since this problem is NP-hard [64], a gate efficient version of this constraint is only possible if NP  $\subseteq$  BQP, which is strongly believed to be false. For this reason, we provide below a sufficient, but not a necessary, condition for the  $W_{P_c}$  to be simulatable in  $O(\operatorname{polylog}(2^n\lambda t/\epsilon))$  gate operations.

**Proposition 7.3.** Let  $P_c \in \mathbb{C}^{2^n \times 2^n}$  be a projector matrix. Suppose there exist functions such that for any  $x, y \in \mathbb{Z}_{2^n}$ ,  $g(x, y) = \langle x | P_c | y \rangle$  and f(x, i) yields the column index of the  $i^{\text{th}}$  non-zero matrix element of  $P_c$  as represented in the computational basis. If

1. P<sub>c</sub> has at most 1 non-zero matrix elements in each row when expressed in the computational basis

2. f is computable using a number of quantum gates that are in O(poly(n)) and g within error  $2^{-m}$  using O(poly(nm)) quantum operations

then for any  $\lambda \geq 0$  and  $t \geq 0$ , a unitary  $\tilde{U}$  can be constructed such that  $\|\tilde{U} - U_I(\lambda;t)\|_{\infty} \leq \epsilon$  using  $O(\operatorname{polylog}(2^n\lambda t/\epsilon))$  quantum operations.

*Proof.* The proof follows straight forwardly. If we assume that g(x,y) can be implemented within zero error with m bits of precision, we have from [65] that  $e^{-i\lambda P_c t}$  can be implemented with zero error using O(1) applications of f and g as well as O(poly(nm)) auxillary quantum operations.

Now let us assume that g(x,y) cannot be computed within zero error using  $m < \infty$  bits of precision. If we denote  $\tilde{g}(x,y)$  to be the approximate version of g, we have from the fact that  $P_c$  is one-sparse that

$$\|e^{-i\lambda t} \sum_{x} g(x, f(x, 1))|x\rangle\langle f(x, 1)| - e^{-i\lambda t} \sum_{x} \tilde{g}(x, f(x, 1))|x\rangle\langle f(x, 1)| \|_{\infty}$$

$$= \max \left( \max_{x: x \neq f(x, 1)} \|e^{-i\lambda t g(x, f(x, 1))(|x\rangle\langle f(x, 1)| + |f(x, 1)\rangle\langle x|)} - e^{-i\lambda t \tilde{g}(x, f(x, 1))(|x\rangle\langle f(x, 1)| + |f(x, 1)\rangle\langle x|)} \|_{\infty} \right)$$

$$+ \max_{x: x = f(x, 1)} \|e^{-i\lambda t g(x, f(x, 1))|x\rangle\langle x|} - e^{-i\lambda t \tilde{g}(x, f(x, 1))|x\rangle\langle x|} \|_{\infty}$$

$$\leq \lambda t \max_{x} |g(x, f(x, 1)) - \tilde{g}(x, f(x, 1))| \leq \lambda t 2^{-m} .$$

$$(99)$$

Thus to achieve an error of  $\epsilon$ , we need to take  $m \in O(\log(\lambda t/\epsilon))$ . The result immediately follows from the assumptions on the cost of f and g.

There are a number of applications of this approach to solve constrained versions of quantum dynamics. One such application involves the simulation of quantum field theories within a particular gauge, which describes a choice of a dynamically unobservable feature of the system that is needed to unambiguously determine the dynamics. For example, the Lorenz gauge involves choosing the vector potential such that  $\partial_{\mu}A^{\mu}=0$ . Rather than fixing the gauge by a clever choice of an equation of motion, this approach allows us to impose such gauges by penalizing all configurations that violate this.

Another application involves Gauss' law in quantum electrodynamics [38, 66]. For D-dimensional quantum electrodynamics, Gauss' law reads  $\nabla \cdot \hat{E}(s) - \hat{\rho}(s) = 0$ , where  $\hat{E}(s)$  is the electric field operator at position s and  $\hat{\rho}(s)$  is the charge density there. On a lattice, this can be further simplified to  $G(s) := \sum_{i=1}^{D} (\hat{E}(s) - \hat{E}(s-e_i)) - \sum_{s,\sigma} e_{\sigma} n_{\sigma}(s)$ , where  $n_{\sigma}(s)$  is the number of electrons (or positrons) at a site and  $e_{\sigma}$  is  $\pm 1$  depending on the site. From this, the constraint projector  $P_c$  can be expressed using the properties of discrete Fourier transforms as  $P_c = 1 - \frac{1}{N} \sum_{i=1}^{N} e^{-i2\pi G(s)/N}$  [66]. This is relevant because Gauss' law is only approximately held for methods such as Trotter-Suzuki simulations and so the application of this constraint oracle can be used to filter out the unphysical components of simulation error. Specifically, consider a constraint on  $|\psi\rangle \in \mathcal{P}^0$  given by the projector  $P_c$  that commutes with the Hamiltonian. In other words,  $[P_c, \sum_j H_j] = 0$ ; however there may exist k' such that  $[H_{k'}, P_c] \neq 0$ . This creates problems for the Trotter-Suzuki expansion, but we can address this by transforming into the interaction frame as discussed below

$$e^{-i\sum_{j=1}^{M}H_{j}t}|\psi\rangle = e^{-i(\sum_{j=1}^{M}H_{j}+\lambda P_{c})t}|\psi\rangle = e^{-i\lambda P_{c}t}\exp_{\tau}\left(\int_{0}^{t}e^{i\lambda P_{c}s}\sum_{j}H_{j}e^{-i\lambda P_{c}s}\mathrm{d}s\right)|\psi\rangle. \quad (100)$$

We can then implement the time-ordered operator exponential in (100) using one of our previous methods, such as a hybridized Trotter-qDRIFT method or that used in the previous section. This allows us to impose a constraint, such as Gauss' law, on the integration formula at low cost. By contrast, if we were to try to do so using a high-order Trotter formula, we would have remainder terms in the Trotter-Suzuki expansion that are in  $O(\operatorname{poly}(\lambda t))$ . From Theorem 7.1, this is in  $O(\operatorname{poly}(\|H_f\|_{\infty}^2 t^2/\epsilon))$  and thus cannot be implemented at low cost in the limit where  $\epsilon \ll 1$ , unlike in the interaction picture approach.

A similar simple example of this is solving the Schrodinger equation for a particle constrained to a given surface. As an example, consider solving the Schrodinger equation for a particle constrained to be on the surface of a Figure-8 immersion of a Klein bottle, which is a non-orientable surface with no boundary. Such a surface is given, for some fixed value of r > 2, by the following parameterized surface over the angles  $\theta, v \in [0, 2\pi)$ 

$$x = (r + \cos(\theta/2)\sin(v) - \sin(\theta/2)\sin(2v))\cos(\theta)$$

$$y = (r + \cos(\theta/2)\sin(v) - \sin(\theta/2)\sin(2v))\sin(\theta)$$

$$z = \sin(\theta/2)\sin(v) + \cos(\theta/2)\sin(2v),$$
(101)

where in Cartesian coordinates  $\theta = \arctan(y/x)$  and v is found implicitly through the above expressions. As all these coordinate functions are Lipshitz continuous, a least square solution can be found using gradient descent after dividing up the surface in  $(\theta, v)$  coordinates into a finite number of regions and then performing gradient descent of  $\|\vec{x} - \vec{x}(r, \theta, v)\|$ . Thus by following this procedure, we can decide within  $\epsilon$  error whether a given (x, y, z) lies on the surface of Klein bottle. In turn,  $P_c$  can be constructed by using reversible logic to evaluate this in time  $O(\text{poly}(\log(1/\epsilon)))$ . Thus, complicated quantum dynamics on unusual manifolds can be simulated through the use of our approach to constraints, even in cases like the figure-8 immersion of the Klein bottle where no simple coordinate system is available that makes the computation of the Laplacian operator in  $(r, v, \theta)$  coordinates trivial. This is because the gradient fails to be defined there, as the normal vector cannot be defined at the intersection in the figure-8. Instead, we can rely on the constraint operator to force the dynamics to lie on the surface of the bottle and use the standard Laplacian in Cartesian coordinates.

As a final point of discussion, let us consider applying these ideas to simulate a universal Hamiltonian with a quantum circuit. A universal Hamiltonian is a Hamiltonian such that the groundstate of the Hamiltonian encodes a quantum superposition of the history of a quantum computer via a clockstate of the form  $\frac{1}{\sqrt{T}}\sum_t |t\rangle|\psi(t)\rangle$  where  $|\psi(t)\rangle$  is the state of the quantum computer after t gates have been applied to it [67, 68, 69, 70]. In order to minimize the locality needed by these constructions, techniques such as "perturbative gadgets" are employed which allow restricted interactions such as 2-local ones to simulate the action of a Hamiltonian of greater k-locality. It is tempting therefore to ask whether our techniques could be used to accelerate the simulation of these constrained Hamiltonians.

As an example, the work of [70] shows that a translationally invariant 1D Hamiltonian of the following form for parameters T,  $\Delta$  is universal

$$H = \sum_{\langle i,j \rangle} \Delta h_{ij}^{(3)} + T \sum_{i} h_{i}^{(2)}, \tag{102}$$

where each  $h_{ij}^{(3)}$  is a two-body translationally invariant Hamiltonian and each  $h_i$  is a translationally invariant one-body Hamiltonian. At first glance, the latter term appears to be fast forwardable. This is significant, because the value T corresponds to the number of gates employed in the circuit. Thus we would be able to fast forward an arbitrary calculation if this were, by itself, true.

However, the value of  $\Delta$  needed to provide a close approximation to the dynamics generically dominates the remaining term in [70]. In particular if we demand a simulation error on the order of  $\epsilon$ , then it suffices to take  $\Delta \in O(T^4/\epsilon)$  (for all other simulation parameters fixed). Thus the translationally invariant 2-body term dominates asymptotically and even if were possible to fast-forward the simulation of this Hamiltonian, the best case scenario would lead to a method that has scaling  $O(T \log(1/\epsilon))$  from the one-body term. However, this construction is not self-evidently fast-forwardable and so a polynomial improvement is expected at best from transitioning to the interaction frame of the two-body operator.

## 8 Conclusions

We have developed novel simulation protocols that combine the standard simulation protocols of Trotterization, continuous qDRIFT, and qubitization in the interaction picture to simulate time-

independent Hamiltonians. By exploiting the interaction picture, we can enter into the interaction frame of a fast-forwardable term with large or unbounded norm. Continuous qDRIFT is used to split the resulting time-ordered exponential into a product of time-independent exponentials with bounds proven for the number of time steps needed to achieve a desired error  $\epsilon$ . In the case of Hamiltonians with underlying commutator structure, Trotterizing first can reduce the query complexity further. Qubitization is then used for implementing the final time-independent exponentials, though other simulation techniques can be used.

The hybrid protocol using Trotterization before continuous qDRIFT in the interaction frame of a fast-forwardable term in the Hamiltonian has a query complexity of  $O(t^2(c_I + \sum_{k \neq l}^L ||H_k||_{\infty}^2)/\epsilon)$ , where  $c_I$  depends on the sum of norms of commutators. For Hamiltonian simulation simulation with commutator structure, this is a drastic improvement over the complexity  $O(||H_k||_{\infty,1,1}^2/\epsilon)$  obtained from directly employing conventional qDRIFT methods to a linear combination query model. The qubitization and continuous qDRIFT hybrid I.P. protocol has a query complexity bounded by  $\tilde{O}(\lambda_{\alpha}t + ||H_{\alpha}||_{\infty}^2t^2/\epsilon)$ , where the quantities  $\lambda_{\alpha}$  and  $H_{\alpha}$  only involve the terms in the interaction Hamiltonian. If the term selected for the interaction frame is unbounded or of large operator norm, this again yields an improvement in the scaling with the  $\ell^1$ -norm of H compared to qubitization. Our approach does not require a complicated clock construction either, which makes it more practical than truncated Dyson series methods [21].

Direct application of these techniques to the Schwinger Model yield a logarithmic scaling in the electric field cutoff  $\Lambda$  for the query complexity. For the Hamiltonian model of collective neutrino oscillations, the query complexity is independent of the typically large constant  $\lambda = \sqrt{2}G_f n_e$  representing the electron density, with the same scaling with respect to other parameters compared to conventional Trotter-Suzuki methods. The scaling with these parameters outperforms those achieved by current simulation methods.

Further applications of these methods appear in simulating constrained dynamics. We show that the magnitude of the constraint term in the Hamiltonian needs to be prohibitively large to apply such a constraint using traditional simulation methods, such as qubitization. However, using our approaches we can simulate the dynamics using a number of gate operations that (for certain constraints) is independent of the magnitude of the constraint. This allows approximation methods similar to Trotter-Suzuki simulations to be employed while guaranteeing that the simulation does not break important symmetries present in the underlying dynamics (such as Gauss' law).

Another interesting fact to note is that even when Trotter formulas are used for the entire simulation, transforming to the interaction picture can have an advantage over performing the simulation in the laboratory frame. This is because Trotter formulas have costs that scale with fractional powers of the derivatives and lead to costs that are linear in the strength of the interaction term, rather than a super-linear function as would be expected from a simulation in the laboratory frame [8, 10]. Although hybrid methods that provide  $L^1$ -norm scaling are shown to be advantageous in this regard, this advantage can be useful and may lead to improved methods to reduce the cost of simulation purely within the Trotter-Suzuki formalism wherein the structure of commutators can be more easily exploited.

These hybrid techniques are primarily useful in contexts where there are not only terms of large operator norm in a Hamiltonian but when those terms are diagonalizable, one-sparse, or more generally fast-forwardable. However, situations often arise in quantum simulation where it might be desirable to enter the interaction frame of terms that are not fast-forwardable, such as the hopping term  $H_h$  of the Schwinger model in the continuum limit. As a naïve application of the present methods would involve doubling the number of times the non fast-forwardable term would be need to be simulated (see equation (42)), additional work is needed to develop interaction picture algorithms, hybrid or otherwise, that are more optimized with respect to parameters that define certain physical regimes of interest.

# Acknowledgements

We thank Martin Savage for useful discussions. This work was supported in part by the U.S. Department of Energy, Office of Science, Office of Nuclear Physics, Inqubator for Quantum Simulation

(IQuS) under Award Number DOE (NP) Award DE-SC0020970. It was further supported by a grant from Google research award, and NW's theoretical work on this project was supported by the U.S. Department of Energy, Office of Science, National Quantum Information Science Research Centers, Co-Design Center for Quantum Advantage under contract number DE-SC0012704.

## References

- [1] Richard P. Feynman. Simulating physics with computers. *International Journal of Theoretical Physics*, 21(6):467–488, 1982. ISSN 1572-9575. doi:10.1007/BF02650179.
- [2] Seth Lloyd. Universal quantum simulators. Science, 273(5278):1073–1078, 1996. doi:10.1126/science.273.5278.1073.
- [3] Alán Aspuru-Guzik, Anthony D Dutoi, Peter J Love, and Martin Head-Gordon. Simulated quantum computation of molecular energies. *Science*, 309(5741):1704–1707, 2005. doi:10.1126/science.1113479.
- [4] Markus Reiher, Nathan Wiebe, Krysta M Svore, Dave Wecker, and Matthias Troyer. Elucidating reaction mechanisms on quantum computers. *Proceedings of the National Academy of Sciences*, 114(29):7555–7560, 2017. doi:10.1073/pnas.1619152114.
- [5] Stephen P Jordan, Keith SM Lee, and John Preskill. Quantum algorithms for quantum field theories. *Science*, 336(6085):1130–1133, 2012. doi:10.1126/science.1217069.
- [6] Alessandro Roggero, Andy C. Y. Li, Joseph Carlson, Rajan Gupta, and Gabriel N. Perdue. Quantum computing for neutrino-nucleus scattering. *Phys. Rev. D*, 101:074038, Apr 2020. doi:10.1103/PhysRevD.101.074038.
- [7] Dominic W Berry, Graeme Ahokas, Richard Cleve, and Barry C Sanders. Efficient quantum algorithms for simulating sparse hamiltonians. *Communications in Mathematical Physics*, 270 (2):359–371, 2007. doi:https://doi.org/10.1007/s00220-006-0150-x.
- [8] Nathan Wiebe, Dominic Berry, Peter Høyer, and Barry C Sanders. Higher order decompositions of ordered operator exponentials. *Journal of Physics A: Mathematical and Theoretical*, 43(6):065203, 2010. doi:10.1088/1751-8113/43/6/065203.
- [9] David Poulin, Angie Qarry, Rolando Somma, and Frank Verstraete. Quantum simulation of time-dependent hamiltonians and the convenient illusion of hilbert space. *Physical Review Letters*, 106(17), Apr 2011. ISSN 1079-7114. doi:10.1103/physrevlett.106.170501.
- [10] Andrew M Childs, Yuan Su, Minh C Tran, Nathan Wiebe, and Shuchen Zhu. Theory of trotter error with commutator scaling. *Physical Review X*, 11(1):011020, 2021. doi:10.1103/PhysRevX.11.011020.
- [11] Guang Hao Low and Isaac L. Chuang. Optimal hamiltonian simulation by quantum signal processing. *Phys. Rev. Lett.*, 118:010501, Jan 2017. doi:10.1103/PhysRevLett.118.010501.
- [12] Guang Hao Low and Isaac L. Chuang. Hamiltonian simulation by qubitization. Quantum, 3: 163, Jul 2019. ISSN 2521-327X. doi:10.22331/q-2019-07-12-163.
- [13] András Gilyén, Yuan Su, Guang Hao Low, and Nathan Wiebe. Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics. In Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pages 193–204, 2019. doi:10.1145/3313276.3316366.
- [14] Dominic W Berry, Mária Kieferová, Artur Scherer, Yuval R Sanders, Guang Hao Low, Nathan Wiebe, Craig Gidney, and Ryan Babbush. Improved techniques for preparing eigenstates of fermionic hamiltonians. npj Quantum Information, 4(1):1–7, 2018. doi:10.1038/s41534-018-0071-5.
- [15] David Poulin, Alexei Kitaev, Damian S Steiger, Matthew B Hastings, and Matthias Troyer. Quantum algorithm for spectral measurement with a lower gate count. *Physical review letters*, 121(1):010501, 2018. doi:10.1103/PhysRevLett.121.010501.
- [16] John M. Martyn, Zane M. Rossi, Andrew K. Tan, and Isaac L. Chuang. Grand unification of quantum algorithms. *PRX Quantum*, 2(4), dec 2021. doi:10.1103/prxquantum.2.040203.
- [17] Yulong Dong, Xiang Meng, K Birgitta Whaley, and Lin Lin. Efficient phase-factor evaluation in quantum signal processing. *Physical Review A*, 103(4):042419, 2021. doi:10.1103/PhysRevA.103.042419.

- [18] Andrew M Childs and Nathan Wiebe. Hamiltonian simulation using linear combinations of unitary operations. Quantum Information & Computation, 12(11-12):901-924, 2012. doi:10.26421/qic12.11-12.
- [19] Dominic W Berry, Andrew M Childs, Richard Cleve, Robin Kothari, and Rolando D Somma. Exponential improvement in precision for simulating sparse hamiltonians. In *Proceedings* of the forty-sixth annual ACM symposium on Theory of computing, pages 283–292, 2014. doi:10.1145/2591796.2591854.
- [20] Mária Kieferová, Artur Scherer, and Dominic W Berry. Simulating the dynamics of time-dependent hamiltonians with a truncated dyson series. *Physical Review A*, 99(4):042314, 2019. doi:10.1103/PhysRevA.99.042314.
- [21] Guang Hao Low and Nathan Wiebe. Hamiltonian simulation in the interaction picture. arXiv preprint arXiv:1805.00675, 2018. doi:10.48550/ARXIV.1805.00675.
- [22] Yuan Su, Dominic W Berry, Nathan Wiebe, Nicholas Rubin, and Ryan Babbush. Fault-tolerant quantum simulations of chemistry in first quantization. arXiv preprint arXiv:2105.12767, 2021. URL https://doi.org/10.48550/arXiv.2105.12767.
- [23] Earl Campbell. Random compiler for fast hamiltonian simulation. Physical Review Letters, 123(7), Aug 2019. ISSN 1079-7114. doi:10.1103/physrevlett.123.070503. URL http://dx.doi.org/10.1103/PhysRevLett.123.070503.
- [24] Dominic W Berry, Andrew M Childs, Yuan Su, Xin Wang, and Nathan Wiebe. Time-dependent hamiltonian simulation with l1-norm scaling. Quantum, 4:254, 2020. doi:10.22331/q-2020-04-20-254.
- [25] Ryan Babbush, Craig Gidney, Dominic W. Berry, Nathan Wiebe, Jarrod McClean, Alexandru Paler, Austin Fowler, and Hartmut Neven. Encoding electronic spectra in quantum circuits with linear t complexity. *Physical Review X*, 8(4), Oct 2018. ISSN 2160-3308. doi:10.1103/physrevx.8.041015. URL http://dx.doi.org/10.1103/PhysRevX.8.041015.
- [26] Camille Jordan. Essai sur la géométrie à n dimensions. Bulletin de la Société Mathématique de France, 3:103-174, 1875. URL http://eudml.org/doc/85325.
- [27] Guang Hao Low, Theodore J. Yoder, and Isaac L. Chuang. Methodology of resonant equiangular composite quantum gates. *Physical Review X*, 6(4), Dec 2016. ISSN 2160-3308. doi:10.1103/physrevx.6.041067. URL http://dx.doi.org/10.1103/PhysRevX.6.041067.
- [28] Rui Chao, Dawei Ding, Andras Gilyen, Cupjin Huang, and Mario Szegedy. Finding angles for quantum signal processing with machine precision. arXiv preprint arXiv:2003.02831, 2020. URL https://doi.org/10.48550/arXiv.2003.02831.
- [29] Jeongwan Haah. Product decomposition of periodic functions in quantum signal processing. *Quantum*, 3:190, 2019. doi:10.22331/q-2019-10-07-190.
- [30] J. J. Sakurai and Jim Napolitano. Modern Quantum Mechanics. Cambridge University Press, 2 edition, 2017. doi:10.1017/9781108499996.
- [31] Steven Weinberg. The Quantum Theory of Fields, volume 1. Cambridge University Press, 1995. doi:10.1017/CBO9781139644167.
- [32] Michael A. Nielsen and Isaac L. Chuang. Quantum Computation and Quantum Information: 10th Anniversary Edition. Cambridge University Press, USA, 10th edition, 2011. ISBN 1107002176.
- [33] Dave Wecker, Matthew B Hastings, Nathan Wiebe, Bryan K Clark, Chetan Nayak, and Matthias Troyer. Solving strongly correlated electron models on a quantum computer. *Physical Review A*, 92(6):062318, 2015. doi:10.1103/PhysRevA.92.062318.
- [34] Julian Schwinger. Gauge invariance and mass. ii. *Phys. Rev.*, 128:2425–2429, Dec 1962. doi:10.1103/PhysRev.128.2425.
- [35] Sidney Coleman, R Jackiw, and Leonard Susskind. Charge shielding and quark confinement in the massive schwinger model. *Annals of Physics*, 93(1):267–275, 1975. ISSN 0003-4916. doi:https://doi.org/10.1016/0003-4916(75)90212-2.
- [36] M.C. Bañuls, K. Cichy, J.I. Cirac, and K. Jansen. The mass spectrum of the schwinger model with matrix product states. *Journal of High Energy Physics*, 2013(11), Nov 2013. ISSN 1029-8479. doi:10.1007/jhep11(2013)158. URL http://dx.doi.org/10.1007/JHEP11(2013)158.
- [37] T. Pichler, M. Dalmonte, E. Rico, P. Zoller, and S. Montangero. Real-time dynamics in u(1) lattice gauge theories with tensor networks. *Phys. Rev. X*, 6:011023, Mar 2016. doi:10.1103/PhysRevX.6.011023.

- [38] P. Hauke, D. Marcos, M. Dalmonte, and P. Zoller. Quantum simulation of a lattice schwinger model in a chain of trapped ions. *Phys. Rev. X*, 3:041018, Nov 2013. doi:10.1103/PhysRevX.3.041018.
- [39] Esteban A. Martinez, Christine A. Muschik, Philipp Schindler, Daniel Nigg, Alexander Erhard, Markus Heyl, Philipp Hauke, Marcello Dalmonte, Thomas Monz, Peter Zoller, and et al. Real-time dynamics of lattice gauge theories with a few-qubit quantum computer. Nature, 534(7608):516-519, Jun 2016. ISSN 1476-4687. doi:10.1038/nature18318. URL http://dx.doi.org/10.1038/nature18318.
- [40] N. Klco, E. F. Dumitrescu, A. J. McCaskey, T. D. Morris, R. C. Pooser, M. Sanz, E. Solano, P. Lougovski, and M. J. Savage. Quantum-classical computation of schwinger model dynamics using quantum computers. *Phys. Rev. A*, 98:032331, Sep 2018. doi:10.1103/PhysRevA.98.032331.
- [41] John Kogut and Leonard Susskind. Hamiltonian formulation of wilson's lattice gauge theories. *Phys. Rev. D*, 11:395–408, Jan 1975. doi:10.1103/PhysRevD.11.395.
- [42] T. Banks, Leonard Susskind, and John Kogut. Strong-coupling calculations of lattice gauge theories: (1 + 1)-dimensional exercises. *Phys. Rev. D*, 13:1043–1053, Feb 1976. doi:10.1103/PhysRevD.13.1043.
- [43] Yuval R. Sanders, Dominic W. Berry, Pedro C.S. Costa, Louis W. Tessler, Nathan Wiebe, Craig Gidney, Hartmut Neven, and Ryan Babbush. Compilation of fault-tolerant quantum heuristics for combinatorial optimization. *PRX Quantum*, 1(2), Nov 2020. ISSN 2691-3399. doi:10.1103/prxquantum.1.020312. URL http://dx.doi.org/10.1103/PRXQuantum.1.020312.
- [44] Yong He, Mingxing Luo, E. Zhang, Hong-Ke Wang, and Xiao-Feng Wang. Decompositions of n-qubit toffoli gates with linear circuit complexity. *International Journal of Theoretical Physics*, 56, 07 2017. doi:10.1007/s10773-017-3389-4.
- [45] Johannes Bausch. Fast black-box quantum state preparation, 2020. URL https://arxiv. org/abs/2009.10709.
- [46] Cody Jones. Low-overhead constructions for the fault-tolerant toffoli gate. *Physical Review* A, 87(2):022328, 2013. doi:10.1103/PhysRevA.87.022328.
- [47] Steven A Cuccaro, Thomas G Draper, Samuel A Kutin, and David Petrie Moulton. A new quantum ripple-carry addition circuit. arXiv preprint quant-ph/0410184, 2004. URL https://doi.org/10.48550/arXiv.quant-ph/0410184.
- [48] Alexander F. Shaw, Pavel Lougovski, Jesse R. Stryker, and Nathan Wiebe. Quantum algorithms for simulating the lattice schwinger model. Quantum, 4:306, Aug 2020. ISSN 2521-327X. doi:10.22331/q-2020-08-10-306. URL http://dx.doi.org/10.22331/q-2020-08-10-306.
- [49] James Pantaleone. Neutrino oscillations at high densities. *Physics Letters B*, 287(1):128-132, 1992. ISSN 0370-2693. doi:https://doi.org/10.1016/0370-2693(92)91887-F.
- [50] Huaiyu Duan, George M. Fuller, J. Carlson, and Yong-Zhong Qian. Coherent development of neutrino flavor in the supernova environment. *Phys. Rev. Lett.*, 97:241101, Dec 2006. doi:10.1103/PhysRevLett.97.241101.
- [51] Huaiyu Duan, George M. Fuller, and Yong-Zhong Qian. Collective neutrino oscillations. Annual Review of Nuclear and Particle Science, 60(1):569-594, 2010. doi:10.1146/annurev.nucl.012809.104524. URL https://doi.org/10.1146/annurev.nucl.012809.104524.
- [52] Sovan Chakraborty, Rasmus Hansen, Ignacio Izaguirre, and Georg Raffelt. Collective neutrino flavor conversion: Recent developments. *Nuclear Physics B*, 908:366 381, 2016. ISSN 0550-3213. doi:https://doi.org/10.1016/j.nuclphysb.2016.02.012. Neutrino Oscillations: Celebrating the Nobel Prize in Physics 2015.
- [53] Ermal Rrapaj. Exact solution of multiangle quantum many-body collective neutrino-flavor oscillations. Phys. Rev. C, 101:065805, Jun 2020. doi:10.1103/PhysRevC.101.065805.
- [54] Michael J. Cervia, Amol V. Patwardhan, A. B. Balantekin, S. N. Coppersmith, and Calvin W. Johnson. Entanglement and collective flavor oscillations in a dense neutrino gas. *Phys. Rev. D*, 100:083001, Oct 2019. doi:10.1103/PhysRevD.100.083001.
- [55] Alessandro Roggero. Entanglement and many-body effects in collective neutrino oscillations. *Phys. Rev. D*, 104:103016, Nov 2021. doi:10.1103/PhysRevD.104.103016.

- [56] Alessandro Roggero. Dynamical phase transitions in models of collective neutrino oscillations. Phys. Rev. D, 104:123023, Dec 2021. doi:10.1103/PhysRevD.104.123023.
- [57] Benjamin Hall, Alessandro Roggero, Alessandro Baroni, and Joseph Carlson. Simulation of collective neutrino oscillations on a quantum computer. *Phys. Rev. D*, 104:063009, Sep 2021. doi:10.1103/PhysRevD.104.063009.
- [58] Kübra Yeter-Aydeniz, Shikha Bangar, George Siopsis, and Raphael C. Pooser. Collective neutrino oscillations on a quantum computer. *Quantum Information Processing*, 2021. URL https://doi.org/10.1007/s11128-021-03348-x.
- [59] Y. Pehlivan, A. B. Balantekin, Toshitaka Kajino, and Takashi Yoshida. Invariants of collective neutrino oscillations. *Phys. Rev. D*, 84:065008, Sep 2011. doi:10.1103/PhysRevD.84.065008.
- [60] Ian D. Kivlichan, Jarrod McClean, Nathan Wiebe, Craig Gidney, Alán Aspuru-Guzik, Garnet Kin-Lic Chan, and Ryan Babbush. Quantum simulation of electronic structure with linear depth and connectivity. Phys. Rev. Lett., 120:110501, Mar 2018. doi:10.1103/PhysRevLett.120.110501.
- [61] Roberto Oliveira and Barbara M. Terhal. The complexity of quantum spin systems on a two-dimensional square lattice, 2005. URL https://doi.org/10.48550/ARXIV.QUANT-PH/ 0504050.
- [62] Yudong Cao and Sabre Kais. Efficient optimization of perturbative gadgets, 2017. URL https://doi.org/10.48550/arXiv.1709.02705.
- [63] Roger A Horn and Charles R Johnson. Matrix analysis. Cambridge university press, 2012.
- [64] Francisco Barahona. On the computational complexity of ising spin glass models. Journal of Physics A: Mathematical and General, 15(10):3241, 1982. doi:10.1088/0305-4470/15/10/028.
- [65] Andrew M Childs, Richard Cleve, Enrico Deotto, Edward Farhi, Sam Gutmann, and Daniel A Spielman. Exponential algorithmic speedup by a quantum walk. In Proceedings of the thirty-fifth annual ACM symposium on Theory of computing, pages 59–68, 2003. doi:10.1145/780542.780552.
- [66] Jesse R Stryker. Oracles for gauss's law on digital quantum computers. Physical Review A, 99(4):042301, 2019. doi:10.1103/PhysRevA.99.042301.
- [67] Julia Kempe and Oded Regev. 3-local hamiltonian is qma-complete. arXiv preprint quant-ph/0302079, 2003. URL https://doi.org/10.48550/arXiv.quant-ph/0302079.
- [68] Dorit Aharonov, Wim Van Dam, Julia Kempe, Zeph Landau, Seth Lloyd, and Oded Regev. Adiabatic quantum computation is equivalent to standard quantum computation. SIAM review, 50(4):755–787, 2008. doi:10.1137/080734479.
- [69] Tobias J Osborne. Hamiltonian complexity. Reports on progress in physics, 75(2):022001, 2012. doi:10.1088/0034-4885/75/2/022001.
- [70] Tamara Kohler, Stephen Piddock, Johannes Bausch, and Toby Cubitt. Translationally invariant universal quantum hamiltonians in 1d. In *Annales Henri Poincaré*, volume 23, pages 223–254. Springer, 2022. doi:10.1007/s00023-021-01111-7.

#### A Diamond Norm

The diamond distance is often used as a measure of error between two quantum channels. It is defined as follows:

$$d_{\diamond}(\mathcal{E}, \mathcal{N}) = \frac{1}{2} ||\mathcal{E} - \mathcal{N}||_{\diamond}, \tag{103}$$

where  $|| \dots ||_{\diamond}$  is the diamond norm

$$||\mathcal{P}||_{\diamond} := \sup_{\rho:||\rho||_1=1} ||(\mathcal{P} \otimes I)(\rho)||_1 \tag{104}$$

and  $\mathcal{E}$  and  $\mathcal{N}$  are two quantum channels or superoperators. Note that I acts on the same size Hilbert space as  $\mathcal{P}$  and  $\rho$  is a density matrix. All operators here are expressed as square matrices and  $\rho$  can represent states entangled with qubits that are not operated on. We then need an identity matrix to "pad out" the missing dimensions so that  $\mathcal{P} \otimes I$  can act sensibly upon  $\rho$ .

The diamond norm is simply the trace distance but maximized over all possible input states and satisfies two key properties:

- (1) Triangle inequality:  $||A + B||_{\diamond} \le ||A||_{\diamond} + ||B||_{\diamond}$
- (2) Sub-multiplicativity:  $||\mathcal{AB}||_{\diamond} \leq ||\mathcal{A}||_{\diamond}||\mathcal{B}||_{\diamond}$

It follows from the definition of the diamond norm that if we apply the channel  $\mathcal{E}$  and  $\mathcal{N}$  to the quantum state  $\sigma$ , we have

$$d_{tr}(\mathcal{E}(\sigma), \mathcal{N}(\sigma)) = \frac{1}{2} ||\mathcal{E}(\sigma) - \mathcal{N}(\sigma)||_1 \le d_{\diamond}(\mathcal{E}, \mathcal{N}).$$
 (105)

The trace norm distance is important since it bounds the error in expectation values. To see this, consider the expression  $|\text{Tr}(M\mathcal{E}(\sigma)) - \text{Tr}(M\mathcal{N}(\sigma))|$ . The expectation value of an operator M with respect to a state  $\rho$  can be found by taking the trace of their product, i.e  $\text{Tr}(M\rho)$ . Thus, in the above expression, we first send a state  $\sigma$  through our two channels. Then we find the expectation value of M with respect to their outputs and take the absolute value of the difference to find the error in expectation values.

We can bound this error in expectation values by the following inequalities

$$|\operatorname{Tr}(M\mathcal{E}(\sigma)) - \operatorname{Tr}(M\mathcal{N}(\sigma))| = |\operatorname{Tr}[M(\mathcal{E}(\sigma) - \mathcal{N}(\sigma))]| \le 2||M||d_{tr}(\mathcal{E}(\sigma), \mathcal{N}(\sigma))$$

$$\le 2||M||d_{\diamond}(\mathcal{E}, \mathcal{N}). \tag{106}$$

In the first inequality, the von-Neumann trace inequality

$$|\text{Tr}(AB)| \le \sum_{i=1}^{n} \alpha_i \beta_i$$

was used where  $\alpha_i, \beta_i$  are the singular values of the operators A and B respectively. This inequality can be further bounded by recognizing that  $\alpha_i \leq \alpha_{\max}$  for all i, where  $\alpha_{\max}$  is the largest singular value of A. The largest singular value of A is precisely  $||A||_{\infty}$  so

$$|\text{Tr}(AB)| \le \sum_{i=1}^{n} \alpha_i \beta_i \le \sum_{i=1}^{n} \alpha_{\max} \beta_i = ||A||_{\infty} ||B||_1.$$

The second inequality in the above expression follows directly from the definition of the diamond norm.

Now note that if we have a projection operator P,  $P^{\dagger}P=P$  since projection operators are Hermitian and square to themselves. Their eigenvalues are 1 and 0 so it immediately follows that  $||P||_{\infty}=1$ . So if M is a projection operator and we have  $\varepsilon$  error in the diamond distance, then

$$|\operatorname{Tr}(M\mathcal{E}(\sigma)) - \operatorname{Tr}(M\mathcal{N}(\sigma))| < 2\varepsilon$$

This justifies the statement that measurement statistics are correct up to a factor of  $2\varepsilon$  with an  $\varepsilon$  error in diamond distance.

# B Notation for qDRIFT

We establish the following notational conventions from [24] for describing the time-dependent qDRIFT scaling. Let  $\alpha \in \mathbb{C}^L$  be a vector. The notation  $||\alpha||_p$  represents the  $l_p$  norm of  $\alpha$  and we define a few cases as follows:

$$||\alpha||_1 \coloneqq \sum_{j=1}^L |\alpha_j|, \quad ||\alpha||_2 \coloneqq \sqrt{\sum_{j=1}^L |\alpha_j|^2}, \quad ||\alpha||_\infty \coloneqq \max_{j \in \{1, 2, \dots, L\}} |\alpha_j|.$$

If A is a matrix,  $||A||_p$  denotes the Schatten-p norm of A. A few important examples are:

$$||A||_1 \coloneqq \mathrm{Tr}(\sqrt{A^\dagger A}), \quad \ ||A||_2 \coloneqq \sqrt{\mathrm{Tr}(A^\dagger A)}, \quad \ ||A||_\infty \coloneqq \max_{|\psi\rangle} ||A|\psi\rangle||_2 \;.$$

If  $f:[0,t]\to\mathbb{C}$  is a continuous function,  $||f||_p$  denotes the  $L^p$  norm of the function. Thus,

$$||f||_1 \coloneqq \int_0^t d\tau |f(\tau)|, \quad ||f||_2 \coloneqq \sqrt{\int_0^t d\tau |f(\tau)|^2}, \quad ||f||_\infty \coloneqq \max_{\tau \in [0,t]} |f(\tau)|.$$

These norms can be combined to obtain vector and operator-valued functions. Suppose  $\alpha$ :  $[0,t] \to \mathbb{C}^L$  is a continuous vector-valued function with components at time  $\tau$  denoted by  $\alpha_j(\tau)$ .  $||\alpha||_{p,q}$  denotes taking the  $l_p$  norm  $||\alpha(\tau)||_p$  for all  $\tau$  and computing the  $L^q$  norm of the resulting scalar function, e.g.

$$||\alpha||_{1,1} = \int_0^t d\tau \sum_{j=1}^L |\alpha_j| .$$

Similar reasoning applies when dealing with the Schatten p-norm of a time-dependent operator and then applying an  $L^q$  norm to the resulting scalar function, i.e.  $||A||_{p,q}$ . For example,

$$||A||_{1,2} = \sqrt{\int_0^t d\tau \, (\text{Tr}(\sqrt{A^{\dagger}A}))^2}$$
.

Note that this notation, while compact, is not well suited for describing evolution within a subinterval of the entire evolution. In the event that a shorter evolution needs to be described, we explicitly use the integral expression over the domain in question.

For time-dependent linear combinations  $A(\tau) = \sum_{l=1}^{L} A_l(\tau)$ , the notation  $||A||_{p,q,r}$  means taking the Schatten p-norm  $||A_t(\tau)||_p$  of each term in the sum and applying the  $l_q$  and  $L^r$  norms to the resulting vector-valued functions, e.g.

$$||A||_{1,1,\infty} := \max_{\tau \in [0,t]} \sum_{l=1}^{L} ||A_l(\tau)||_1.$$