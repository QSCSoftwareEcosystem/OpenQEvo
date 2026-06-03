# qSWIFT: High-order randomized compiler for Hamiltonian simulation

Kouhei Nakaji, 1, 2, 3, \* Mohsen Bagherimehrab, 1, 4, † and Alán Aspuru-Guzik 1, 4, 5, 6, 7, 8

Chemical Physics Theory Group, Department of Chemistry, University of Toronto, Toronto, Ontario, Canada <sup>2</sup>Research Center for Emerging Computing Technologies, National Institute of Advanced Industrial Science and Technology (AIST), 1-1-1 Umezono, Tsukuba, Ibaraki 305-8568, Japan
 Quantum Computing Center, Keio University, 3-14-1 Hiyoshi, Kohoku-ku, Yokohama, Kanagawa, 223-8522, Japan <sup>4</sup>Department of Computer Science, University of Toronto, Toronto, Ontario, Canada <sup>5</sup>Vector Institute for Artificial Intelligence, Toronto, Ontario, Canada <sup>6</sup>Department of Chemical Engineering & Applied Chemistry, University of Toronto, Toronto, Ontario, Canada <sup>7</sup>Department of Materials Science & Engineering, University of Toronto, Toronto, Ontario, Canada <sup>8</sup>Lebovic Fellow, Canadian Institute for Advanced Research, Toronto, Ontario, Canada

Hamiltonian simulation is known to be one of the fundamental building blocks of a variety of quantum algorithms such as its most immediate application, that of simulating many-body systems to extract their physical properties. In this work, we present qSWIFT, a high-order randomized algorithm for Hamiltonian simulation. In qSWIFT, the required number of gates for a given precision is independent of the number of terms in Hamiltonian, while the systematic error is exponentially reduced with regards to the order parameter. In this respect, our aSWIFT is a higher-order counterpart of the previously proposed quantum stochastic drift protocol (qDRIFT), in which the number of gates scales linearly with the inverse of the precision required. We construct the qSWIFT channel and establish a rigorous bound for the systematic error quantified by the diamond norm, qSWIFT provides an algorithm to estimate given physical quantities using a system with one ancilla qubit, which is as simple as other product-formula-based approaches such as regular Trotter-Suzuki decompositions and qDRIFT. Our numerical experiment reveals that the required number of gates in qSWIFT is significantly reduced compared to qDRIFT. Particularly, the advantage is significant for problems where high precision is required; for example, to achieve a systematic relative propagation error of 10<sup>-6</sup>, the required number of gates in third-order qSWIFT is 1000 times smaller than that of qDRIFT.

### CONTENTS

| I.   | Introduction                                           | 1  |
|------|--------------------------------------------------------|----|
| II.  | Background A. Hamiltonian simulation by Trotter-Suzuki | 3  |
|      | formulae                                               | 3  |
|      | B. Hamiltonian simulation by qDRIFT                    | 4  |
| III. | Second order qSWIFT                                    | 4  |
|      | A. Mixture function                                    | 4  |
|      | B. Second-order qSWIFT channel                         | 5  |
|      | C. Implementation of the second-order                  | 5  |
|      | qSWIFT channel                                         | Ð  |
| IV.  | Higher-order qSWIFT                                    | 7  |
|      | A. Higher-order qSWIFT channel                         | 7  |
|      | B. Implementation of the higher-order qSWIFT channel   | 8  |
|      | C. Note on the previous higher-order                   |    |
|      | randomized method                                      | 11 |
| V.   | Numerical experiments                                  | 12 |
|      | A. Asymptotic behaviour                                | 12 |
|      | B. Simulation of the hydrogen molecule                 | 13 |
| VI.  | Conclusion and Discussion                              | 14 |
|      | Acknowledgement                                        | 15 |
|      |                                                        |    |

| A. Bound for the systematic errors in qSWIFT                                                                         |    |
|----------------------------------------------------------------------------------------------------------------------|----|
| channels                                                                                                             | 15 |
| <ol> <li>Error bound for the second-order qSWIFT channel</li> <li>Error bound for the higher-order qSWIFT</li> </ol> | 15 |
| channels                                                                                                             | 17 |
|                                                                                                                      |    |
| B. Statistical error                                                                                                 | 18 |
| C. All-order qSWIFT                                                                                                  | 19 |
| D. Note on the LCU-based randomized approach                                                                         | 20 |
| <ul><li>a. The LCU-based randomized approach</li><li>b. Application to the Hamiltonian</li></ul>                     | 20 |
| simulation problem                                                                                                   | 21 |
| D 4                                                                                                                  |    |
| References                                                                                                           | 22 |

### I. INTRODUCTION

Hamiltonian simulation is a key subroutine of quantum algorithms for simulating quantum systems. Given a Hamiltonian  $H = \sum_{\ell=1}^L h_\ell H_\ell$ , where  $h_\ell \geq 0$  and L is the number of terms, the task in Hamiltonian simulation is to construct a quantum circuit that approximately emulate time evolution  $U(t) := \exp(-iHt)$  of the system for time t. Several approaches have been established for this task. The conventional approach uses the Trotter-Suzuki decompositions that provide a deterministic way for Hamiltonian simulation [1–3]. The gate count of this approach scales at least linearly with the number of terms L in H [3]; we note

<sup>\*</sup> kohei.nakaji@utoronto.ca

<sup>†</sup> mohsen.bagherimehrab@utoronto.ca

$$S_{\ell}^{(0)} = \underbrace{S}_{\ell} \underbrace{K}_{\ell} \underbrace{K}_{\ell} \underbrace{K}_{\ell}$$
(a) Quantum circuit for  $\tilde{S}_{\ell}^{(0)}(\rho)$ .
(b) Quantum circuit for  $\tilde{S}_{\ell}^{(1)}(\rho)$ .

FIG. 1. Quantum circuits for implementing the swift operators  $\tilde{\mathcal{S}}_{\ell}^{(b)} := S_{\ell}^{(b)} \rho S_{\ell}^{(b)\dagger}$  ( $b \in \{0,1\}$ ). The top line corresponds to an ancilla qubit, and the bottom line corresponds to the qubits in the system. The S gate is defined by the operator  $e^{i\pi/2}e^{i\sigma_z}$  with  $\sigma_z$  is the Pauli-Z operator.

![](_page_1_Figure_3.jpeg)

FIG. 2. Examples of quantum circuits used for qDRIFT and qSWIFT.

that the gate count in [2] scales at least quadratically with L. Although this scaling is formally efficient but is impractical for many applications of interest, particularly for the electronic-structure problem in quantum chemistry, where the number of terms in a Hamiltonian is prohibitively large. An alternative approach is randomly permuting the order of terms in the Trotter-Suzuki decompositions [4]. This randomized compilation provides a slightly better scaling for gate count over Ref. [2], but the gate count still depends on the number of Hamiltonian terms quadratically.

The quantum stochastic drift protocol (qDRIFT) [5] is another randomized Hamiltonian simulation approach but is independent of the number of terms. In qDRIFT, gates of the form  $\exp(-iH_{\ell}\tau)$  with small interval  $\tau$  are applied randomly with a probability proportional to the strength  $h_{\ell}$  of the corresponding term in the Hamiltonian. qDRIFT improves upon the Trotter-Suzuki approach in that its gate count is independent of L and  $\Lambda := \max_{\ell} h_{\ell}$  (magnitude of the strongest term in the Hamiltonian), and instead depends on  $\lambda := \sum_{\ell=1}^{L} h_{\ell}$ . However, qDRIFT has poor scaling with respect to the precision  $\varepsilon$  in contrast to that in the Trotter-Suzuki approach. We note that there are other approaches to Hamiltonian simulation with asymptotically better performance as a function of various parameters [6-11]. Still, the approaches based on product formulae, e.g., Trotter-Suzuki decompositions and aDRIFT, are preferred for their superior performance in practice [12] and predominant usage in experimental implementations [13–15] due to their simplicity and the fact that they do not require any ancilla qubits. From this perspective, we focus on an approach based on product formulae while having better gate scaling than the previous methods.

In this paper, we propose the quantum swift protocol  $(qSWIFT)^1$ , a high-order randomized algorithm hav-

We will now describe in more detail how qSWIFT is carried out. First, we build the qSWIFT channel that simulates the ideal time evolution. We then establish a bound for the distance between the qSWIFT channel and the ideal channel, quantified with the diamond norm, which exponentially decreases by increasing the order parameter. The established bound yields the desired scaling for the gate count of qSWIFT. It should be

ing (i) better scaling with respect to the precision  $\varepsilon$ and (ii) the same scaling with respect to  $\lambda$  compared to qDRIFT. Specifically, the gate count of qSWIFT scales as  $\mathcal{O}((\lambda t)^2/\varepsilon^{\frac{1}{K}})$  with K as the order-parameter while that of qDRIFT scales as  $\mathcal{O}((\lambda t)^2/\varepsilon)$ . For example, with respect to the precision  $\varepsilon$ , the gate count of qSWIFT scales as  $\mathcal{O}(1/\sqrt{\varepsilon})$  for the second-order and as  $\mathcal{O}(1/\varepsilon^{\frac{1}{3}})$  for the third-order. Our qSWIFT algorithm shares its simplicity with the other approaches based on product formulae. It works in the system with one ancilla qubit (we refer to the qubits other than the ancilla qubit simply as the system qubits). We can construct all gate operations with  $\exp(\mathrm{i}H_\ell\tau)$  and the *swift operators*  $\tilde{\mathcal{S}}_\ell^b := S_\ell^{(b)} \rho S_\ell^{(b)\dagger}$  where  $S_\ell^{(b)}$  is a unitary transformation; the swift operators can be constructed if we can efficiently implement controlled- $H_{\ell}$  gates, as shown in Fig. 1. In the case of qDRIFT, the entire time evolution is divided into segments, and a sampled time evolution  $\exp(iH_{\ell}\tau)$  is performed in each segment (see Fig. I). In qSWIFT, we utilize the *swift circuit* in addition to the circuit for qDRIFT. The swift circuit also has segments; in most segments, a sampled time evolution  $\exp(iH_{\ell}\tau)$ is performed to the system qubits, but in the other segments, a sequence of the swift operators is performed (see Fig. I). The number of swift operators is upper bounded by about twice the order parameter. Therefore, the qSWIFT algorithm can be performed with almost no additional resources compared to the qDRIFT.

<sup>&</sup>lt;sup>1</sup> The code for the qSWIFT algorithm is available at

noted that the qSWIFT channel itself is not physical in the sense that it is not a completely-positive and trace-preserving (CPTP) map. Nevertheless, we can employ the qSWIFT channel to develop a procedure for measuring a physical quantity of interest, i.e., computing the expectation value of some given observable that is exponentially more precise than the original qDRIFT with respect to the order parameter.

Our numerical analysis also reveals the advantage of our qSWIFT algorithm. We show the asymptotic behavior of qSWIFT by using electronic molecular Hamiltonians with the number of qubits  $\sim 50$  and compare the performance with the other approaches based on the product formulae. Specifically, we compute the required number of gates to approximate the time evolution with the molecule Hamiltonians with a given systematic error  $\varepsilon$ . We show that the number of gates in the thirdorder version of qSWIFT is 10 times smaller than that of qDRIFT when  $\varepsilon = 0.001$  for every time region. A significant reduction of the number of gates is observed when  $\varepsilon = 10^{-6}$ ; the required number of gates in third-order (sixth-order) qSWIFT is 1,000 (10,000) times smaller than that of qDRIFT. We also simulate our qSWIFT algorithm and the other product formulae-based algorithms by using a quantum circuit simulator with the small-size (eight-qubits) molecular Hamiltonian. Its result is consistent with the result of the asymptotic behavior analysis.

The rest of the paper is organized as follows. In Section II, we briefly review approaches for the Hamiltonian simulation based on the product formula. Section III and Section IV are dedicated to proposing and analyzing our qSWIFT algorithm. In Section III, we introduce the way of constructing the second-order qSWIFT algorithm. Then we generalize the algorithm to the higher-order in Section IV. In Section V, we validate our algorithm by numerical experiments. Finally, in Section VI, we conclude with some discussions.

## II. BACKGROUND

This section covers the key background pertinent to the following sections. We begin with a brief description of Hamiltonian simulation and Trotter-Suzuki formulae in Section II A. Then we review the qDRIFT algorithm for Hamiltonian simulation in Section II B.

# A. Hamiltonian simulation by Trotter-Suzuki formulae

We begin with a brief description of the Hamiltonian simulation. For a given time-independent Hamiltonian of the form  $H = \sum_{\ell=1}^L h_\ell H_\ell$ , where  $h_\ell > 0$  and  $H_\ell$  are Hermitian operators with  $\|H_\ell\| = 1$ , the task in Hamiltonian simulation is to find a good approximation of the transformation

$$\mathcal{U}(t): \rho \to U(t)\rho U^{\dagger}(t),$$
 (1)

with  $U(t) := e^{iHt}$  and t as a real parameter. We assume we can efficiently implement each  $e^{iH_{\ell}t'}$  by quantum gates with t' as a real number. For example, if we decompose H to the sum of the tensor products of the Pauli operators, we can efficiently implement each  $e^{iH_{\ell}t'}$ .

The conventional approach for the Hamiltonian simulation is the Trotter-Suzuki decomposition [1, 2]. In the first-order Trotter-Suzuki decomposition for Hamiltonian simulation, the entire simulation for time t is divided into r segments of simulations for time t/r as  $U(t) = (U(t/r))^r$  and U(t/r) is approximated as  $U(t/r) \approx U_{T_s}^{(1)}(t/r)$  with

$$U_{\text{TS}}^{(1)}(t) := \prod_{\ell=1}^{L} e^{ih_{\ell}H_{\ell}t},$$
 (2)

which yields the approximation  $U(t) \approx (U_{\text{TS}}^{(1)}(t/r))^r$  for the entire simulation. The second-order Trotter-Suzuki decomposition is given by  $U(t) \approx (U_{\text{TS}}^{(2)}(t/r))^r$  with

$$U_{\text{TS}}^{(2)}(t) := \prod_{\ell'=L}^{1} e^{ih_{\ell'}H_{\ell'}t/2} \prod_{\ell=1}^{L} e^{ih_{\ell}H_{\ell}t/2}, \quad (3)$$

which serves as the base case for the recursive formula

$$U_{\text{TS}}^{(2k)}(t) := \left[ U_{\text{TS}}^{(2k-2)}(p_k t) \right]^2 U_{\text{TS}}^{(2k-2)}((1-4p_k)t) \left[ U_{\text{TS}}^{(2k-2)}(p_k t) \right]^2$$
(4)

for the  $2k^{\text{th}}$ -order decomposition, where  $p_k := 1/(4 - 4^{1/(2k-1)})$ .

Let us discuss the Trotter-Suzuki decomposition in the channel representation. The  $2k^{\text{th}}$ -order Trotter-Suzuki channel  $\mathcal{U}_{\text{TS}}^{(2k)}(t): \rho \to U_{\text{TS}}^{(2k)}(t)\rho U_{\text{TS}}^{(2k)}(t)$  is used to approximate the channel  $\mathcal{U}(\rho)$  as  $\mathcal{U}(\rho) \approx (\mathcal{U}_{\text{TS}}^{(2k)}(t/r))^r$ . For a given channel  $\mathcal{C}$ , we denote by  $\mathcal{C}^{r'}$  the r'-repetition of  $\mathcal{C}$ . Previous analytic work [2, 16, 17] shows that

$$||\mathcal{U}(t) - (\mathcal{U}_{TS}^{(2k)}(t/r))^r||_{\diamond} \le \varepsilon$$
 (5)

for  $r \in \mathcal{O}(\alpha L\Lambda t(\alpha L\Lambda t/\varepsilon)^{1/2k})$  with  $\alpha := 2 \cdot 5^{k-1}$ , where  $||\cdot||_{\diamond}$  is the diamond norm. We note that  $\alpha$  here is defined so that  $r\alpha L$  is the number of gates used in the  $2k^{\text{th}}$ -order decomposition. Hence the gate count for the  $2k^{\text{th}}$ -order Trotter-Suzuki decomposition, denoted by  $G_{\text{TS}}$ , is

$$G_{\text{TS}} = r\alpha L \in O\left(\frac{\alpha^2 L^2 \Lambda t (\alpha L \Lambda t)^{\frac{1}{2k}}}{\varepsilon^{\frac{1}{2k}}}\right).$$
 (6)

Notice that the gate count approaches to  $\mathcal{O}(L^2\Lambda t)$  by increasing the order parameter 2k, but the prefactor scales exponentially with 2k. Because of this rapidly growing prefactor, Trotter-Suzuki decompositions of finite orders, typically second (k=1) or fourth order (k=2), are used in practice [5].

We note that [3] demonstrates that the gate-count scaling can be more rigorously bounded using the commutator bounds, where the upper bound is represented as the commutation relation. However, we use the gate-count scaling in Eq. (6) to compare qSWIFT against qDRIFT [5], particularly for comparing the numerical experiments in [5].

### B. Hamiltonian simulation by qDRIFT

Developed by Campbell [5], qDRIFT is an algorithm for Hamiltonians simulation using a randomized procedure. While the procedure is randomized, with many repetitions the evolution stochastically drifts towards the target unitary. Specifically, the exact time evolution is approximated by N repetitions of the qDRIFT channel  $\mathcal{E}_N$  as  $\mathcal{U} \approx \mathcal{E}_N^N$ , with the qDRIFT channel defined as

$$\mathcal{E}_N(\rho) := \sum_{\ell=1}^L p_\ell \mathcal{T}_\ell(\rho), \tag{7}$$

where

$$\mathcal{T}_{\ell}(\rho) = e^{iH_{\ell}\tau} \rho e^{-iH_{\ell}\tau}, \tag{8}$$

is the unitary channel that we call the time operator, and

$$p_{\ell} := h_{\ell}/\lambda, \quad \lambda = \sum_{\ell} h_{\ell}, \quad \tau := \lambda t/N,$$
 (9)

are three variables used through the paper. To realize the qDRIFT channel  $\mathcal{E}_N$ , the index  $\ell$  is sampled according to the probability  $p_\ell$  and the quantum state  $\rho$  is evolved through the channel associated with the operator  $\mathrm{e}^{\mathrm{i}H_\ell\tau}$ .

For evaluating the systematic error of the approximation, they define the exact short time evolution  $\mathcal{U}_N$  as

$$\mathcal{U}_N(\rho) := e^{iHt/N} \rho e^{-iHt/N}. \tag{10}$$

Then, they show

$$d_{\diamond}(\mathcal{U}_N, \mathcal{E}_N) \le \frac{2(\lambda t)^2}{N^2} e^{2\lambda t/N},$$
 (11)

where the diamond distance is defined as

$$d_{\diamond}\left(\mathcal{U}',\mathcal{E}'\right) := \frac{1}{2}||\mathcal{U}' - \mathcal{E}'||_{\diamond}.\tag{12}$$

They utilize the diamond distance  $d_{\diamond}\left(\mathcal{U},\mathcal{E}_{N}^{N}\right)$  as the measure of the systematic error. By using the subadditive feature of the diamond distance, they obtain the bound for the diamond distance as:

$$d_{\diamond} \left( \mathcal{U}, \mathcal{E}_{N}^{N} \right) \leq N d_{\diamond} \left( \mathcal{U}_{N}, \mathcal{E}_{N} \right)$$

$$\leq \frac{2(\lambda t)^{2}}{N} e^{2\lambda t/N}$$

$$\in \mathcal{O} \left( \frac{(\lambda t)^{2}}{N} \right). \tag{13}$$

In other words, to reduce the systematic error within  $\varepsilon$ , we need to set  $N \in \mathcal{O}((\lambda t)^2/\varepsilon)$ .

In most of the applications of the Hamiltonian simulation, what we have interests is computing the expectation value of an observable after applying the time evolution operator  $\mathcal{U}$ . Let us write the expectation value as

$$q := \text{Tr}(QU(\rho_{\text{init}})),$$
 (14)

where Q is an observable and  $\rho_{\text{init}}$  is an input quantum state. By using the qDRIFT algorithm, we can approximately compute the value of Q as

$$q^{(1)} := \operatorname{Tr}\left(Q\mathcal{E}_N^N(\rho_{\text{init}})\right),\tag{15}$$

where the systematic error is bounded as

$$|q - q^{(1)}| \le 2||Q||_{\infty} d_{\diamond} \left(\mathcal{U}, \mathcal{E}_{N}^{N}\right) \in \mathcal{O}\left(||Q||_{\infty} \left(\frac{(\lambda t)^{2}}{N}\right)\right). \tag{16}$$

### III. SECOND ORDER QSWIFT

In this section, we describe our second-order qSWIFT as a preparation for introducing the general high-order qSWIFT in Section IV. To elucidate our algorithm, we use a "mixture function" in our second and higher-order qSWIFT. We begin by describing this function in Section III A. Next, we construct the second-order qSWIFT channel and discuss its error bound in Section III B. Finally, in Section III C, we explain how to apply the constructed qSWIFT channel for computing physical quantities.

# A. Mixture function

In constructing our qSWIFT channels, we make use of a mixture function. As a preparation, let us first define the following *sorting function*.

**Definition III.1** (Sorting function). Let  $S_N$  be the permutation group. For positive integers k, N with k < N, let  $\vec{\mathcal{A}} := (\mathcal{A}_1, \dots, \mathcal{A}_k)$  and  $\vec{\mathcal{B}} := (\mathcal{B}_1, \dots, \mathcal{B}_{N-k})$ . We define the sorting function as

$$f_{\sigma,k,N-k}(\vec{\mathcal{A}},\vec{\mathcal{B}}) := \mathcal{X}_{\sigma(1)}\mathcal{X}_{\sigma(2)}\cdots\mathcal{X}_{\sigma(N)},$$
 (17)

where  $\sigma \in S_N$  and

$$\mathcal{X}_{j} = \begin{cases} \mathcal{A}_{j} & j \leq k, \\ \mathcal{B}_{j-k} & j \geq k+1. \end{cases}$$
 (18)

The mixture function is defined by using the sorting function as follows.

**Definition III.2** (Mixture function). For positive integers k, N with k < N, let  $\vec{\mathcal{A}} := (\mathcal{A}_1, \dots, \mathcal{A}_k)$  and  $\vec{\mathcal{B}} := (\mathcal{B}_1, \dots, \mathcal{B}_{N-k})$ . Then we define the mixture function as

$$M_{k,N-k}(\vec{\mathcal{A}}, \vec{\mathcal{B}}) = \sum_{\sigma \in S_{N-k}^{\text{sub}}} f_{\sigma,k,N-k}(\vec{\mathcal{A}}, \vec{\mathcal{B}}), \tag{19}$$

where the set  $S_{N,k}^{\mathrm{sub}}$  is the subgroup of the permutation group  $S_N$  comprised of all elements  $\sigma \in S_N$  that satisfies the following condition: if both  $\mathcal{X}_i, \mathcal{X}_j \in \vec{\mathcal{A}}$  or  $\in \vec{\mathcal{B}}$  then  $\sigma(i) < \sigma(j)$  for any i < j. We remark that the number of elements in  $S_{N,k}^{\mathrm{sub}}$  is  $\binom{N}{k}$ .

For simplicity, if elements of  $\vec{\mathcal{B}}$  are identical, we denote the sorting and mixture functions as  $f_{\sigma,k,N-k}(\vec{\mathcal{A}},\mathcal{B})$  and  $M_{k,N-k}(\vec{\mathcal{A}},\mathcal{B})$ , respectively. In this case  $\mathcal{X}_j = \mathcal{B}$  for  $j \geq k+1$ . Similarly, we use the notation  $f_{\sigma,k,N-k}(\mathcal{A},\mathcal{B})$  and  $M_{k,N-k}(\mathcal{A},\mathcal{B})$  if elements of  $\vec{\mathcal{A}}$ , and also elements of  $\vec{\mathcal{B}}$ , are identical. In this case,  $\mathcal{X}_j = \mathcal{A}$  for  $j \leq k$  and  $\mathcal{X}_j = \mathcal{B}$  for  $j \geq k+1$ .

Note that the sorting function in Eq. (17) and mixture function in Eq. (19) are bilinear functions. For example, if the  $\ell$ th element of  $\vec{\mathcal{A}}$  is a linear combination of elements of another vector  $\vec{\mathcal{F}}$ , i.e., if  $\mathcal{A}_{\ell} = \sum_{n} c_{n} \mathcal{F}_{n}$  for  $c_{n} \in \mathbb{C}$ , then we have

$$M_{k,N-k}\left((\mathcal{A}_1,\ldots,\mathcal{A}_{\ell-1},\sum_n c_n\mathcal{F}_n,\mathcal{A}_{\ell+1},\ldots,\mathcal{A}_k),\vec{\mathcal{B}}\right)$$

$$=\sum_n c_n M_{k,N-k}\left((\mathcal{A}_1,\ldots,\mathcal{A}_{\ell-1},\mathcal{F}_n,\mathcal{A}_{\ell+1},\ldots,\mathcal{A}_k),\vec{\mathcal{B}}\right).$$
(20)

In general, if  $\mathcal{A}_{\ell} = \sum_{n_{\ell}} c_{n_{\ell}} \mathcal{F}_{n_{\ell}}$  for any  $\ell$ , then the identity

$$M_{k,N-k}\left(\vec{\mathcal{A}},\vec{\mathcal{B}}\right) = \sum_{n_1} c_{n_1} \sum_{n_2} c_{n_2} \cdots \sum_{n_k} c_{n_k}$$

$$M_{k,N-k}\left((\mathcal{F}_{n_1},\dots,\mathcal{F}_{n_k}),\vec{\mathcal{B}}\right)$$
(21)

holds.

### B. Second-order qSWIFT channel

To construct the qSWIFT channel, let us define

$$\mathcal{L}_{\ell}(\rho) := i[H_{\ell}, \rho], \tag{22}$$

$$\mathcal{L}(\rho) := \frac{\mathrm{i}}{\lambda}[H, \rho] = \sum_{\ell} p_{\ell} \mathcal{L}_{\ell}(\rho), \tag{23}$$

where the variables  $\lambda, p_{\ell}$  and  $\tau$  are defined in Eq. (9). We then have

$$\mathcal{U}_N = e^{\mathcal{L}\tau} = \mathbb{I} + \tau \mathcal{L} + \Delta^{(2)} \mathcal{U}_N, \tag{24}$$

$$\mathcal{E}_N = \sum_{\ell} p_{\ell} e^{\mathcal{L}_{\ell} \tau} = \mathbb{I} + \tau \mathcal{L} + \Delta^{(2)} \mathcal{E}_N, \qquad (25)$$

for the ideal time-evolution channel in Eq. (10) and the qDRIFT channel in Eq. (7), where

$$\Delta^{(k)}\mathcal{U}_N = \sum_{n=k}^{\infty} \frac{\tau^n}{n!} \mathcal{L}^n, \tag{26}$$

$$\Delta^{(k)}\mathcal{E}_N = \sum_{n=k}^{\infty} \frac{\tau^n}{n!} \sum_{\ell=1}^{L} p_{\ell} \mathcal{L}_{\ell}^n.$$
 (27)

Let  $\Delta_k := \Delta^{(k)} \mathcal{U}_N - \Delta^{(k)} \mathcal{E}_N$ , then

$$\Delta_k = \sum_{n=k}^{\infty} \frac{\tau^n}{n!} \mathcal{L}^{(n)}, \quad \mathcal{L}^{(n)} := \mathcal{L}^n - \sum_{\ell=1}^L p_{\ell} \mathcal{L}_{\ell}^n.$$
 (28)

Using the definition of  $\Delta_k$  and Eqs. (24) and (25), we have  $\mathcal{U}_N = \mathcal{E}_N + \Delta_2$  which we use to expand  $\mathcal{U} = \mathcal{U}_N^N$  as

$$\mathcal{U} = (\mathcal{E}_N + \Delta_2)^N$$

$$= \mathcal{E}_N^N + \sum_{k=1}^N M_{k,N-k} (\Delta_2, \mathcal{E}_N)$$

$$= \mathcal{E}_N^N + \frac{\tau^2}{2} M_{1,N-1} (\mathcal{L}^{(2)}, \mathcal{E}_N) + M_{1,N-1} (\Delta_3, \mathcal{E}_N)$$

$$+ \sum_{k=2}^N M_{k,N-k} (\Delta_2, \mathcal{E}_N),$$
(29)

where we used  $\Delta_2 = (\tau^2/2)\mathcal{L}^{(2)} + \Delta_3$  and linearity of  $M_{1,N-1}$  to obtain the last equality. Let us denote the first two terms as

$$\mathcal{E}^{(2)} := \mathcal{E}_N^N + \frac{\tau^2}{2} M_{1,N-1} \left( \mathcal{L}^{(2)}, \mathcal{E}_N \right). \tag{30}$$

We refer to  $\mathcal{E}^{(2)}$  as the second-order qSWIFT channel. In the following lemma, we provide a bound for the error in approximating the ideal channel  $\mathcal{U}$  in Eq. (1) by the second-order qSWIFT channel  $\mathcal{E}^{(2)}$ , where the error is quantified as the diamond norm of their difference.

**Lemma III.3.** Let  $\mathcal{U}$  be the ideal channel in Eq. (1) and let  $\mathcal{E}^{(2)}$  be the second-order qSWIFT channel in Eq. (30). Then, in the region  $\lambda t \geq 1$ ,

$$d_{\diamond}\left(\mathcal{U}, \mathcal{E}^{(2)}\right) \in \mathcal{O}\left(\left(\frac{(\lambda t)^2}{N}\right)^2\right),$$
 (31)

provided  $N < 2\sqrt{2}e(\lambda t)^2$ .

We provide the proof in Appendix A1. Invoking this lemma for the reasonable parameter region  $\lambda t \geq 1$ , if  $N \in \mathcal{O}((\lambda t)^2/\sqrt{\varepsilon})$  for  $\varepsilon > 0$ , then  $d_{\diamond}(\mathcal{U}, \mathcal{E}^{(2)}) \leq \varepsilon$ . This result provides a quadratic improvement over the original qDRIFT with respect to  $\varepsilon$ .

# C. Implementation of the second-order qSWIFT channel

The second-order qSWIFT channel we constructed is not a physical channel as it is not a CPTP map. Therefore, we cannot directly implement the qSWIFT channel itself. However, in most applications of the Hamiltonian simulation, our interest is in computing physical quantities, i.e., the expectation value of an observable after applying the time evolution operator as described in Section IIB. Thus, in the following, we focus on how

to compute  $q^{(2)} := \text{Tr}(Q\mathcal{E}^{(2)}(\rho_{\text{init}}))$ , for a given observable Q and the input  $\rho_{\text{init}}$ . By using  $q^{(2)}$ , the systematic error is reduced to

$$|q - q^{(2)}| \le 2||Q||_{\infty} d_{\diamond} \left( \mathcal{U}, \mathcal{E}^{(2)} \right) \in \mathcal{O} \left( ||Q||_{\infty} \left( \frac{(\lambda t)^2}{N} \right)^2 \right), \tag{32}$$

where we use (31), which is the quadratic improvement in terms of  $(\lambda t)^2/N$  from the one in qDRIFT (16).

Here we provide a way of computing  $q^{(2)}$  by quantum circuits. We can expand  $q^{(2)}$  as

$$q^{(2)} = q^{(1)} + \delta q, (33)$$

where

$$\delta q = \frac{\tau^2}{2} \operatorname{Tr} \left( Q M_{1,N-1} \left( \mathcal{L}^{(2)}, \mathcal{E}_N \right) (\rho_{\text{init}}) \right). \tag{34}$$

For computing  $q^{(1)}$ , we just need to apply the original qDRIFT channel and compute the expectation value. Thus, we focus on how to compute  $\delta q$  in the following. More specifically, we will show that  $\delta q$  is computable by using the swift circuits, composed of the time evolution  $\exp(iH_{\ell}\tau)$  and the swift operators shown in Fig. 1.

By using

$$M_{1,N-1}\left(\mathcal{L}^{(2)},\mathcal{E}_{N}\right) = \sum_{r=0}^{N-1} \mathcal{E}_{N}^{N-1-r} \mathcal{L}^{(2)} \mathcal{E}_{N}^{r}, \qquad (35)$$

which can be derived from the definition (19), we obtain

$$\delta q = \frac{\tau^2}{2} \sum_{r=0}^{N-1} \delta q_r,$$
 (36)

where  $\delta q_r := \text{Tr} \left( Q \mathcal{E}_N^{N-1-r} \mathcal{L}^{(2)} \mathcal{E}_N^r(\rho_{\text{init}}) \right)$ . Now let us move on to the evaluation of  $\delta q_r$ . We transform  $\delta q_r$  as

$$\delta q_r = \operatorname{Tr}\left(Q\mathcal{E}_N^{N-1-r}\mathcal{L}^{(2)}\mathcal{E}_N^r(\rho_{\text{init}})\right),$$

$$= \sum_{\ell,k=1}^L p_\ell p_k \operatorname{Tr}\left(Q\mathcal{E}_N^{N-1-r}\mathcal{L}_\ell \mathcal{L}_k \mathcal{E}_N^r(\rho_{\text{init}})\right)$$

$$- \sum_{\ell=1}^L p_\ell \operatorname{Tr}\left(Q\mathcal{E}_N^{N-1-r}\mathcal{L}_\ell^2 \mathcal{E}_N^r(\rho_{\text{init}})\right),$$
(37)

where we use (28) in the second equality. Let two probability distributions be

$$P_0^{(2)}(\vec{\ell}) = p_{\ell_2} p_{\ell_1}, \ P_1^{(2)}(\vec{\ell}) = \begin{cases} p_{\ell} & \ell_1 = \ell_2 = \ell \\ 0 & \ell_1 \neq \ell_2 \end{cases}, \quad (38)$$

where the input  $\vec{\ell}$  is a vector with two elements  $(\ell_1, \ell_2)$ . Also, let

$$\mathcal{L}_2(\vec{\ell}) := \mathcal{L}_{\ell_2} \mathcal{L}_{\ell_1}. \tag{39}$$

Then it holds

$$\delta q_r := \sum_{s=0}^{1} (-1)^s \sum_{\vec{\ell}} P_s^{(2)}(\vec{\ell}) \operatorname{Tr} \left( Q \mathcal{K}(r, \vec{\ell})(\rho_{\text{init}}) \right), \quad (40)$$

where we define a channel  $\mathcal{K}(r, \vec{\ell})$  as

$$\mathcal{K}(r,\vec{\ell}) := \mathcal{E}_N^{N-1-r} \mathcal{L}_2(\vec{\ell}) \mathcal{E}_N^r. \tag{41}$$

To evaluate each term of (40), we utilize a system with one ancilla qubit. Let us write the density matrix for a given system with one ancilla qubit as the matrix form:

$$\begin{pmatrix}
\rho_{00} & \rho_{01} \\
\rho_{10} & \rho_{11}
\end{pmatrix}$$

$$:= |0\rangle\langle 0| \otimes \rho_{00} + |0\rangle\langle 1| \otimes \rho_{01} + |1\rangle\langle 0| \otimes \rho_{10} + |1\rangle\langle 1| \otimes \rho_{11}.$$
(42)

We define the operation of a quantum channel  $\tilde{\mathcal{K}}(r, \vec{\ell})$  that transforms the initial state

$$\tilde{\rho}_{\text{init}} := |+\rangle\langle+| \otimes \rho_{\text{init}} = \begin{pmatrix} \rho_{\text{init}}/2 & \rho_{\text{init}}/2 \\ \rho_{\text{init}}/2 & \rho_{\text{init}}/2 \end{pmatrix}$$
(43)

into a final state as

$$\tilde{\rho}_{\text{init}} \xrightarrow{\tilde{\mathcal{K}}(r,\vec{\ell})} \begin{pmatrix} \vdots & \frac{1}{2}\mathcal{K}(r,\vec{\ell})(\rho_{\text{init}}) \\ \frac{1}{2}\mathcal{K}(r,\vec{\ell})(\rho_{\text{init}}) & \vdots \end{pmatrix}, \quad (44)$$

where the dot [.] in the diagonal element denotes a matrix we do not have interest in now. Then it holds

$$\operatorname{Tr}(Q\mathcal{K}(r,\vec{\ell})(\rho_{\mathrm{init}})) = \operatorname{Tr}\left(\tilde{Q}\tilde{\mathcal{K}}(r,\vec{\ell})(\tilde{\rho}_{\mathrm{init}})\right),$$
 (45)

and consequently,

$$\delta q_r := \sum_{s=0}^{1} (-1)^s \sum_{\vec{\ell}} P_s^{(2)}(\vec{\ell}) \operatorname{Tr} \left( \tilde{Q} \tilde{\mathcal{K}}(r, \vec{\ell}) (\tilde{\rho}_{\text{init}}) \right), \quad (46)$$

where

$$\tilde{Q} = X \otimes Q,\tag{47}$$

with X as the Pauli-X observable for the ancilla qubit. Therefore, we can evaluate  $\delta q_r$  if we implement the channel  $\tilde{\mathcal{K}}(r,\vec{\ell})$  by using quantum circuits.

We can specify the channel  $\tilde{\mathcal{K}}(r, \vec{\ell})$  as follows:

$$\tilde{\mathcal{K}}(r,\vec{\ell}) := \tilde{\mathcal{E}}_N^{N-1-r} \tilde{\mathcal{L}}_{\ell_2} \tilde{\mathcal{L}}_{\ell_1} \tilde{\mathcal{E}}_N^r, \tag{48}$$

where we define  $\tilde{\mathcal{E}}_N := \mathbf{1} \otimes \mathcal{E}_N$  and  $\vec{\ell} = (\ell_1, \ell_2)$ , and where the operation of the channel  $\tilde{\mathcal{L}}_\ell$  is specified for the input having the identical non-diagonal elements as follows:

$$\begin{pmatrix} \cdot & \rho \\ \rho & \cdot \end{pmatrix} \xrightarrow{\tilde{\mathcal{L}}_{\ell}} \begin{pmatrix} \cdot & \mathcal{L}_{\ell}(\rho) \\ \mathcal{L}_{\ell}(\rho) & \cdot \end{pmatrix}. \tag{49}$$

The channel  $\tilde{\mathcal{L}}_{\ell}$  can be written as the sum of two swift operators  $\tilde{\mathcal{S}}_{\ell}^{(0)}$  and  $\tilde{\mathcal{S}}_{\ell}^{(1)}$  introduced in Fig. 1 as

$$\tilde{\mathcal{L}}_{\ell} = \tilde{\mathcal{S}}_{\ell}^{(0)} + \tilde{\mathcal{S}}_{\ell}^{(1)},\tag{50}$$

which is easily checked by using

$$\begin{pmatrix} \cdot & \rho \\ \rho & \cdot \end{pmatrix} \xrightarrow{\tilde{\mathcal{S}}_{\ell}^{(0)}} \begin{pmatrix} \cdot & -i\rho H_{\ell} \\ iH_{\ell}\rho & \cdot \end{pmatrix},
\begin{pmatrix} \cdot & \rho \\ \rho & \cdot \end{pmatrix} \xrightarrow{\tilde{\mathcal{S}}_{\ell}^{(1)}} \begin{pmatrix} \cdot & iH_{\ell}\rho \\ -i\rho H_{\ell} & \cdot \end{pmatrix}.$$
(51)

It can be pedagogically shown that the channel (48) reproduces the transformation in (44); with  $\rho'_{\text{init}} = \rho_{\text{init}}/2$ , it holds

$$\begin{pmatrix}
\rho'_{\text{init}} & \rho'_{\text{init}} \\
\rho'_{\text{init}} & \rho'_{\text{init}}
\end{pmatrix} \xrightarrow{\tilde{\mathcal{E}}_{N}^{r}} \begin{pmatrix}
\mathcal{E}_{N}^{r}(\rho'_{\text{init}}) & \mathcal{E}_{N}^{r}(\rho'_{\text{init}}) \\
\mathcal{E}_{N}^{r}(\rho'_{\text{init}}) & \mathcal{E}_{N}^{r}(\rho'_{\text{init}})
\end{pmatrix}$$

$$\xrightarrow{\tilde{\mathcal{L}}_{\ell_{1}}} \begin{pmatrix}
\vdots & \mathcal{L}_{\ell_{1}} \mathcal{E}_{N}^{r}(\rho'_{\text{init}}) \\
\mathcal{L}_{\ell_{1}} \mathcal{E}_{N}^{r}(\rho'_{\text{init}}) & \vdots \\
\mathcal{L}_{\ell_{2}} \mathcal{L}_{\ell_{1}} \mathcal{E}_{N}^{r}(\rho'_{\text{init}}) & \vdots \\
\mathcal{L}_{\ell_{2}} \mathcal{L}_{\ell_{1}} \mathcal{E}_{N}^{r}(\rho'_{\text{init}}) & \vdots \\
\tilde{\mathcal{E}}_{N}^{N-1-r} & \vdots & \tilde{\mathcal{K}}(r, \vec{\ell})(\rho'_{\text{init}}) \\
\tilde{\mathcal{K}}(r, \vec{\ell})(\rho'_{\text{init}}) & \vdots \\
\vdots & \vdots & \vdots \\
\tilde{\mathcal{K}}(r, \vec{\ell})(\rho'_{\text{init}}) & \vdots
\end{pmatrix} .$$
(52)

By substituting (50) to (48), we obtain

$$\tilde{\mathcal{K}}(r,\vec{\ell}) = \sum_{b_1,b_2=0}^{1} \tilde{\mathcal{E}}_N^{N-1-r} \tilde{\mathcal{S}}_{\ell_2}^{(b_2)} \tilde{\mathcal{S}}_{\ell_1}^{(b_1)} \tilde{\mathcal{E}}_N^r.$$
 (53)

Finally, from (36), (46), and (53),

$$\delta q = \frac{\tau^2}{2} \sum_{s=0}^{1} (-1)^s \sum_{b_1, b_2=0}^{1} \sum_{r=0}^{N-1} \sum_{\vec{\ell}} P_s^{(2)}(\vec{\ell}) \text{Tr} \left( \tilde{Q} \tilde{\mathcal{E}}_N^{N-1-r} \tilde{\mathcal{S}}_{\ell_2}^{(b_2)} \tilde{\mathcal{S}}_{\ell_1}^{(b_1)} \tilde{\mathcal{E}}_N^r(\rho_{\text{init}}) \right),$$

$$= \frac{(\lambda t)^2}{2N} \sum_{s=0}^{1} (-1)^s \sum_{b_1, b_2=0}^{1} \delta q(s, b_1, b_2),$$
(54)

where in the second equality, we define

 $\delta q(s,b_1,b_2)$

$$:= \frac{1}{N} \sum_{r=0}^{N-1} \sum_{\vec{\ell}} P_s^{(2)}(\vec{\ell}) \operatorname{Tr} \left( \tilde{Q} \tilde{\mathcal{E}}_N^{N-1-r} \tilde{\mathcal{S}}_{\ell_2}^{(b_2)} \tilde{\mathcal{S}}_{\ell_1}^{(b_1)} \tilde{\mathcal{E}}_N^r (\tilde{\rho}_{\text{init}}) \right). \tag{55}$$

We can evaluate (55) using Monte Carlo sampling. To this end, let

$$P_{\text{MDRIFT}}(\vec{k}, n) = p_{k_1} p_{k_2} \cdots p_{k_n} \tag{56}$$

be the probability distribution for product of multiple qDRIFT probability distributions, where  $n \in \mathbb{Z}^+$  specifies the number of qDRIFT distributions and  $k_j$ , for each j, goes from 1 to L. Then

$$\tilde{\mathcal{E}}_{N}^{n} = \sum_{k_{1}, k_{2}, \dots k_{n}}^{L} P_{\text{MDRIFT}}(\vec{k}, n) \tilde{\mathcal{T}}_{n}(\vec{k}), \tag{57}$$

where  $\tilde{\mathcal{T}}_n(\vec{k})$  is the unitary channel defined as the sequence of the time operators:

$$\tilde{\mathcal{T}}_n(\vec{k}) := (\mathbf{1} \otimes \mathcal{T}_{k_n} \cdots \mathcal{T}_{k_2} \mathcal{T}_{k_1}). \tag{58}$$

We obtain an unbiased estimator of  $\delta q(s, b_1, b_2)$  as follows:

1. Sample  $\ell$  uniformly from  $\{0, 1, \dots N - 1\}$ .

- 2. With probability  $P_s^{(2)}(\vec{\ell})$  sample  $\vec{\ell} = (\ell_1, \ell_2)$ . With probability  $P_{\text{MDRIFT}}(\vec{k}, r)$  and  $P_{\text{MDRIFT}}(\vec{k}', N 1 r)$ , sample  $\vec{k}$  and  $\vec{k}'$ .
- 3. Estimate

$$\operatorname{Tr}\left(\tilde{Q}\tilde{\mathcal{T}}_{N-1-r}(\vec{k}')\tilde{\mathcal{S}}_{\ell_{2}}^{(b_{2})}\tilde{\mathcal{S}}_{\ell_{1}}^{(b_{1})}\tilde{\mathcal{T}}_{r}(\vec{k})(\tilde{\rho}_{\mathrm{init}})\right)$$
(59)

with  $N_{\rm shot}$  measurements and set the resulting value to  $\delta \hat{q}(s,b_1,b_2)$ , which is an unbiased estimator of  $\delta q(s,b_1,b_2)$ . The value (59) can be evaluated by applying a swift circuit composed of the time evolution and the swift operators and estimating the expectation value of  $\tilde{Q}$  by measurements.

We repeat the above process  $N_{\text{sample}}$  times, and the estimate of  $\delta q(s,b_1,b_2)$  is computed as the sample average. By substituting each estimate of  $\delta q(s,b_1,b_2)$  to (55), we obtain the estimate of  $\delta q$  as  $\delta \hat{q}$ . It should be noted that the swift circuit for evaluating each term of (59) has the structure that two swift operators are tucked in between N-1 time operators as in Fig. I. Therefore, the number of gates in the swift circuit is almost the same as the original qDRIFT that requires N time operators.

# IV. HIGHER-ORDER QSWIFT

In this section, we generalize the second-order qSWIFT channel introduced in Section III B to an arbitrary high-order channel. First we construct the higher-order qSWIFT channel and discuss the error bound in Section IV A. Then, in Section IV B, we construct an algorithm to apply the qSWIFT channel for computing physical quantities.

### A. Higher-order qSWIFT channel

To construct a high-order qSWIFT channel, we retain higher orders of  $\tau$  in the right-hand-side of

$$\mathcal{U} = (\mathcal{E}_N + \Delta_2)^N = \mathcal{E}_N^N + \sum_{k=1}^N M_{k,N-k}(\Delta_2, \mathcal{E}_N), \quad (60)$$

where  $M_{k,N-k}$  is the mixture function defined in Eq (19). We note that  $\Delta_2$  is a linear combination of  $\mathcal{L}^{(n)}$

as per Eq. (28). Thus by Eq. (21) we obtain  $M_{k,N-k}(\Delta_2, \mathcal{E}_N)$

$$= \sum_{n_{1}=2}^{\infty} \frac{\tau^{n_{1}}}{n_{1}!} \sum_{n_{2}=2}^{\infty} \frac{\tau^{n_{2}}}{n_{2}!} \cdots \sum_{n_{k}=2}^{\infty} \frac{\tau^{n_{k}}}{n_{k}!}$$

$$M_{k,N-k} \left( \left( \mathcal{L}^{(n_{1})}, \dots, \mathcal{L}^{(n_{k})} \right), \mathcal{E}_{N} \right),$$

$$= \sum_{n_{1},n_{2},\dots,n_{k}=2}^{\infty} \frac{\tau^{\sum_{j=1}^{k} n_{j}}}{n_{1}! n_{2}! \cdots n_{k}!} \sum_{\xi=2}^{\infty} \delta \left[ \xi, \sum_{\ell=1}^{k} n_{\ell} \right]$$

$$M_{k,N-k} \left( \left( \mathcal{L}^{(n_{1})}, \dots, \mathcal{L}^{(n_{k})} \right), \mathcal{E}_{N} \right),$$

$$= \sum_{\xi=2}^{\infty} \tau^{\xi} \sum_{n_{1},n_{2},\dots,n_{k}=2}^{\xi} \frac{1}{n_{1}! n_{2}! \cdots n_{k}!} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right]$$

$$M_{k,N-k} \left( \left( \mathcal{L}^{(n_{1})}, \dots, \mathcal{L}^{(n_{k})} \right), \mathcal{E}_{N} \right),$$

$$(61)$$

where  $\delta[i,j]$  here is the Kronecker  $\delta$ . To show the second equality, we use the identity

$$\sum_{\xi=2}^{\infty} \delta \left[ \xi, \sum_{j=1}^{k} n_j \right] = 1, \tag{62}$$

which holds for a fixed set of integers  $\{n_j\}_{j=1}^k$  with  $n_j \geq 2$ . In the last equality, we use the fact that the Kronecker  $\delta$  is zero if any of  $n_1, n_2 \cdots n_k$  is larger than  $\xi$ . Truncating the upper limit of  $\xi$  yields a high-order qSWIFT channel. Specifically, we define the high-order qDRIFT as follows.

**Definition IV.1** (Higher-order qSWIFT). We define K-th order qSWIFT channel ( $K \leq N$ ) as

 $\mathcal{L}(K$

$$:= \mathcal{E}_{N}^{N} + \sum_{\xi=2}^{2K-2} \tau^{\xi} \sum_{k=1}^{N} \sum_{n_{1},\dots,n_{k}=2}^{\xi} \frac{1}{n_{1}! n_{2}! \cdots n_{k}!} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right]$$

$$M_{k,N-k} \left( \left( \mathcal{L}^{(n_{1})}, \dots, \mathcal{L}^{(n_{k})} \right), \mathcal{E}_{N} \right).$$
(63)

Here we note that the upper limit N in the second summation can be replaced with K for  $K \leq N$  because the terms with k > K become zero by the Kronecker  $\delta$ . We remark that setting K = 2 yields the second-order qSWIFT channel in Eq. (30). Also, by setting K = 1, we reproduce the qDRIFT channel.

We now provide a bound for the error in approximating the ideal channel  $\mathcal{U}$  in Eq. (1) by the high-order qSWIFT channel  $\mathcal{E}^{(K)}$  in the following lemma.

**Lemma IV.2.** Let  $\mathcal{U}$  be the ideal channel in and let  $\mathcal{E}^{(K)}$  be the K-th order qSWIFT channel. Then, in the region  $\lambda t \geq 1$ ,

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(K)}\right) \in \mathcal{O}\left(\left(\frac{(\lambda t)^2}{N}\right)^K\right).$$
 (64)

as far as  $N \leq 2\sqrt{2}e(\lambda t)^2$ .

The proof is given in Appendix A 2. As in the case of the second order, for  $\lambda t \geq 1$  and  $\varepsilon > 0$ , if  $N \in \mathcal{O}((\lambda t)^2/\sqrt{\varepsilon})$ , then  $d_{\diamond}(\mathcal{U}, \mathcal{E}^{(K)}) \leq \varepsilon$ .

# B. Implementation of the higher-order qSWIFT channel

As we discuss in Section III C, the qSWIFT channel is not a physical channel, but we can apply it to computing the physical quantities. Specifically, we discuss how to compute

$$q^{(K)} := \operatorname{Tr}\left(Q\mathcal{E}^{(K)}\right). \tag{65}$$

Then, the systematic error is bounded as

$$|q - q^{(K)}| \le 2||Q||_{\infty} d_{\diamond} \left(\mathcal{U}, \mathcal{E}^{(K)}\right)$$

$$\in \mathcal{O}\left(||Q||_{\infty} \left(\frac{(\lambda t)^{2}}{N}\right)^{K}\right), \tag{66}$$

which can be exponentially small with the order parameter

Here, we provide the way to compute  $q^{(K)}$ . We can expand  $q^{(K)}$  as

$$q^{(K)} = q^{(1)}$$

$$+ \sum_{\xi=2}^{2K-2} \sum_{k=1}^{N} \sum_{n_1, \dots, n_k=2}^{\xi} \delta \left[ \xi, \sum_{j=1}^{k} n_j \right] \delta q^{(k)}(\vec{n}), \quad (68)$$

$$= q^{(1)} + \sum_{\xi=2}^{2K-2} \sum_{k=1}^{K} \sum_{\vec{n} \in \mathcal{C}(k, \xi)} \delta q^{(k)}(\vec{n}), \quad (69)$$

where

$$\delta q^{(k)}(\vec{n}) := \frac{\tau^{\sum_{j=1}^{k} n_j}}{n_1! n_2! \cdots n_k!} \times \operatorname{Tr}\left(QM_{k,N-k}\left(\left(\mathcal{L}^{(n_1)}, \dots, \mathcal{L}^{(n_k)}\right), \mathcal{E}_N\right)(\rho_{\text{init}})\right),$$
(70)

with  $\vec{n} = \{n_1, n_2, \cdots, n_k\}$  and where we replace N in the second summation with K in the second equality (since the terms with k > K become zero by the Kronecker  $\delta$ .). To obtain (69), we define the set  $G_2(k, \xi)$  composed of all vectors with k integer elements  $\{n_j\}_{j=1}^k$  that satisfies  $n_j \geq 2$  and  $\sum_{j=1}^k n_j = \xi$ . As an example, when using the second-order (K = 2) qSWIFT, the summation of the second term in (70) includes only one term as:

$$q^{(2)} = q^{(1)} + \delta q^{(1)} (\{2\}). \tag{71}$$

we see  $\delta q$  in (33) corresponds to  $\delta q^{(1)}$  ({2}), where we write  $\{a_1, \dots, a_k\}$  as the vector having elements  $a_1, \dots, a_k$ . As another example, when using the third-order (K=3) qSWIFT,

$$q^{(3)} = q^{(1)} + \delta q^{(1)} (\{2\}) + \delta q^{(1)} (\{3\}) + \delta q^{(1)} (\{4\}) + \delta q^{(2)} (\{2, 2\}).$$
(72)

Since  $q^{(1)}$  is again evaluable by using the original qDRIFT, we focus on the evaluation of  $\delta q^{(k)}(\vec{n})$  in the following.

Similar to the second-order case, we will transform  $\delta q^{(k)}(\vec{n})$  as a sum of the terms evaluable with quantum circuits. The mixture function  $M_{k,N-k}(\cdot)$  included in (70) is written as the summation of  $\binom{N}{k}$  terms as

$$\delta q^{(k)}(\vec{n}) = \frac{\tau^{\sum_{j=1}^{k} n_j}}{n_1! n_2! \cdots n_k!} \sum_{\sigma \in S_{\tau}^{\text{sub}}} \delta q_{\sigma}^{(k)}(\vec{n}), \tag{73}$$

where

$$\delta q_{\sigma}^{(k)}(\vec{n})
:= \operatorname{Tr} \left( Q f_{\sigma,k,N-k} \left( \left( \mathcal{L}^{(n_1)}, \dots, \mathcal{L}^{(n_k)} \right), \mathcal{E}_N \right) (\rho_{\text{init}}) \right),$$
(74)

with  $f_{\sigma,k,N-k}$  as the sorting function defined in (17).

Now we move on to the calculation of  $\delta q_{\sigma}^{(k)}(\vec{n})$ . To this end, let

$$\mathcal{D}_0^{(n)} := \mathcal{L}^n, \ \mathcal{D}_1^{(n)} := \sum_{\ell} p_{\ell} \mathcal{L}_{\ell}^n. \tag{75}$$

We can write  $\mathcal{L}^{(n)}$  as a linear combination of  $\mathcal{D}_s^{(n)}$ :

$$\mathcal{L}^{(n)} = \sum_{s=0}^{1} (-1)^s \mathcal{D}_s^{(n)} \tag{76}$$

as per (28). Let two probability distributions:

$$P_0^{(n)}(\vec{\ell}) = P_{\text{MDRIFT}}(\vec{\ell}, n), \tag{77}$$

$$P_1^{(n)}(\vec{\ell}) = \begin{cases} p_{\ell} & \ell_1 = \dots = \ell_n = \ell, \\ 0 & \ell_a \neq \ell_b \text{ for } \exists (a, b) \end{cases}, \tag{78}$$

where n specifies the number of vectors in  $\vec{\ell}$  and we write the ath element of  $\vec{\ell}$  as  $\ell_a$ . We see that for n=2, (77) is consistent with (38). Then it holds

$$\mathcal{D}_s^{(n)} = \sum_{\vec{\ell}} P_s^{(n)}(\vec{\ell}) \mathcal{L}_n(\vec{\ell}), \tag{79}$$

with

$$\mathcal{L}_n(\vec{\ell}) := \mathcal{L}_{\ell_n} \cdots \mathcal{L}_{\ell_1}, \tag{80}$$

which is consistent with (39) for n = 2. By using the bilinearity of the sorting function, we obtain

$$f_{\sigma,k,N-k}\left(\left(\mathcal{L}^{(n_1)},\dots,\mathcal{L}^{(n_k)}\right),\mathcal{E}_N\right)$$

$$= \sum_{s_1,\dots,s_k=0}^{1} (-1)^{\sum_c s_c} f_{\sigma,k,N-k}\left(\left(\mathcal{D}_{s_1}^{(n_1)},\dots,\mathcal{D}_{s_k}^{(n_k)}\right),\mathcal{E}_N\right),$$

$$= \sum_{s_1,\dots,s_k=0}^{1} (-1)^{\sum_c s_c} \sum_{\vec{\ell_1},\dots\vec{\ell_k}} P_{s_1}^{(n_1)}(\vec{\ell_1})\dots P_{s_k}^{(n_k)}(\vec{\ell_k})$$

$$f_{\sigma,k,N-k}\left(\left(\mathcal{L}_{n_1}(\vec{\ell_1}),\dots,\mathcal{L}_{n_k}(\vec{\ell_k})\right),\mathcal{E}_N\right),$$
(81)

where we use (76) in the first equality and (79) in the second equality. Substituting above into (74), we obtain

$$\delta q_{\sigma}^{(k)}(\vec{n}) = \sum_{s_1, \dots, s_k = 0}^{1} (-1)^{\sum_c s_c} \sum_{\vec{\ell_1}, \dots \vec{\ell_k}} P_{s_1}^{(n_1)}(\vec{\ell_1}) \dots P_{s_k}^{(n_k)}(\vec{\ell_k}) \delta q_{\sigma}^{(k)} \left( \vec{n}, \left( \vec{\ell_1}, \dots, \vec{\ell_k} \right) \right),$$
(82)

where

$$\delta q_{\sigma}^{(k)} \left( \vec{n}, \left( \vec{\ell}_{1}, \cdots, \vec{\ell}_{k} \right) \right)$$

$$:= \operatorname{Tr} \left( Q f_{\sigma, k, N-k} \left( \left( \mathcal{L}_{n_{1}} (\vec{\ell}_{1}), \cdots, \mathcal{L}_{n_{k}} (\vec{\ell}_{k}) \right), \mathcal{E}_{N} \right) (\rho_{\text{init}}) \right). \tag{83}$$

As in Section III C, we compute the right hand side of (83) by using the system with one ancilla qubit. Let

$$\tilde{\mathcal{L}}_n(\vec{\ell}) := \tilde{\mathcal{L}}_{\ell_n} \cdots \tilde{\mathcal{L}}_{\ell_1}. \tag{84}$$

By repeatedly operating (49) with  $j = \ell_1, \dots, \ell_n$ , we obtain the operation of  $\tilde{\mathcal{L}}_n(\vec{\ell})$  as

$$\begin{pmatrix} \cdot & \rho \\ \rho & \cdot \end{pmatrix} \xrightarrow{\tilde{\mathcal{L}}_n(\vec{\ell})} \begin{pmatrix} \cdot & \mathcal{L}_n(\vec{\ell})(\rho) \\ \mathcal{L}_n(\vec{\ell})(\rho) & \cdot \end{pmatrix}$$
(85)

for a given density operator  $\rho$ . Recall the definition of the sorting function (17):

$$f_{\sigma,k,N-k}\left(\left(\mathcal{L}_{n_1}(\vec{\ell}_1),\cdots,\mathcal{L}_{n_k}(\vec{\ell}_k)\right),\mathcal{E}_N\right)$$

$$=\mathcal{X}_{\sigma(1)}\cdots\mathcal{X}_{\sigma(N)},$$
(86)

with

$$\mathcal{X}_a = \begin{cases} \mathcal{L}_{n_a}(\vec{\ell}_a) & a \le k, \\ \mathcal{E}_N & a \ge k+1 \end{cases}$$
(87)

Then in the system with one ancilla qubit, it holds

$$f_{\sigma,k,N-k}\left(\left(\tilde{\mathcal{L}}_{n_1}(\vec{\ell}_1),\cdots,\tilde{\mathcal{L}}_{n_k}(\vec{\ell}_k)\right),\tilde{\mathcal{E}}_N\right)$$

$$=\tilde{\mathcal{X}}_{\sigma(1)}\cdots\tilde{\mathcal{X}}_{\sigma(N)},$$
(88)

with

$$\tilde{\mathcal{X}}_a = \begin{cases} \tilde{\mathcal{L}}_{n_a}(\vec{\ell}_a) & a \le k, \\ \tilde{\mathcal{E}}_N & a \ge k+1 \end{cases}$$
 (89)

Since it holds that

$$\begin{pmatrix} \cdot & \rho \\ \rho & \cdot \end{pmatrix} \xrightarrow{\tilde{\mathcal{X}}_a} \begin{pmatrix} \cdot & \mathcal{X}_a(\rho) \\ \mathcal{X}_a(\rho) & \cdot \end{pmatrix}, \tag{90}$$

the operation of  $\tilde{\mathcal{X}}_{\sigma(1)}\cdots\tilde{\mathcal{X}}_{\sigma(N)}$  to the input state  $\tilde{\rho}_{\text{init}}=|+\rangle\langle+|\otimes\rho_{\text{init}}|$  reproduces the operation of  $\mathcal{X}_{\sigma(1)}\cdots\mathcal{X}_{\sigma(N)}$  as

$$\tilde{\rho}_{\text{init}} = \begin{pmatrix} \rho_{\text{init}}/2 & \rho_{\text{init}}/2 \\ \rho_{\text{init}}/2 & \rho_{\text{init}}/2 \end{pmatrix} \xrightarrow{\tilde{\mathcal{X}}_{\sigma(1)} \cdots \tilde{\mathcal{X}}_{\sigma(N)}}$$

$$\begin{pmatrix} \vdots & \mathcal{X}_{\sigma(1)} \cdots \mathcal{X}_{\sigma(N)}(\rho_{\text{init}})/2 \\ \mathcal{X}_{\sigma(1)} \cdots \mathcal{X}_{\sigma(N)}(\rho_{\text{init}})/2 & \vdots \end{pmatrix}.$$

$$(91)$$

Therefore, the estimation value of the observable  $\tilde{Q} = X \otimes Q$  with the final state in (91) gives  $\delta q_{\sigma}^{(k)} \left( \vec{n}, \left( \vec{\ell_1}, \cdots, \vec{\ell_k} \right) \right)$ , i.e.,

$$\delta q_{\sigma}^{(k)}\left(\vec{n}, \left(\vec{\ell_{1}}, \cdots, \vec{\ell_{k}}\right)\right) \\
= \operatorname{Tr}\left(\tilde{Q}f_{\sigma,k,N-k}\left(\left(\tilde{\mathcal{L}}_{n_{1}}(\vec{\ell_{1}}), \cdots, \tilde{\mathcal{L}}_{n_{k}}(\vec{\ell_{k}})\right), \tilde{\mathcal{E}}_{N}\right)(\tilde{\rho}_{\text{init}})\right). \tag{92}$$

Next, we discuss the way of evaluating the right hand side of (92). By substituting (50) to (92), we obtain

$$\tilde{\mathcal{L}}_n(\vec{\ell}) = \sum_{\vec{k}} \tilde{\mathcal{S}}_n^{(\vec{b})}(\vec{\ell}), \tag{93}$$

with  $\vec{b} \in \{0,1\}^{\otimes n}$ , where

$$\tilde{\mathcal{S}}_n^{(\vec{b})}(\vec{\ell}) = \tilde{\mathcal{S}}_{\ell_n}^{(b_n)} \cdots \tilde{\mathcal{S}}_{\ell_1}^{(b_1)}. \tag{94}$$

Then with  $\vec{b}_j \in \{0,1\}^{\otimes n_j} (j=1\cdots k)$ , we obtain

$$f_{\sigma,k,N-k}\left(\left(\tilde{\mathcal{L}}_{n_{1}}(\vec{\ell}_{1}),\cdots,\tilde{\mathcal{L}}_{n_{k}}(\vec{\ell}_{k})\right),\tilde{\mathcal{E}}_{N}\right)$$

$$=\sum_{\vec{b_{1}}\cdots\vec{b_{k}}}f_{\sigma,k,N-k}\left(\left(\tilde{\mathcal{S}}_{n_{1}}^{(\vec{b_{1}})}(\vec{\ell}_{1}),\cdots,\tilde{\mathcal{S}}_{n_{k}}^{(\vec{b_{k}})}(\vec{\ell}_{k})\right),\tilde{\mathcal{E}}_{N}\right)$$

$$=\sum_{\vec{b_{1}}\cdots\vec{b_{k}}}\sum_{\vec{r}}P_{\text{MDRIFT}}(\vec{r},N-k)$$

$$\mathcal{C}_{\sigma,k,N-k}^{(\vec{b_{1}},\cdots,\vec{b_{k}})}\left(\vec{n},\left(\vec{\ell}_{1},\cdots\vec{\ell}_{k}\right),\vec{r}\right),$$
(95)

where  $C_{\sigma,k,N-k}^{(\vec{b}_1,\cdots,\vec{b}_k)}\left(\vec{n},\left(\vec{\ell}_1,\cdots\vec{\ell}_k\right),\vec{r}\right)$  is an unitary channel defined by

$$C_{\sigma,k,N-k}^{(\vec{b}_1,\cdots,\vec{b}_k)}\left(\vec{n},\left(\vec{\ell}_1,\cdots\vec{\ell}_k\right),\vec{r}\right) = f_{\sigma,k,N-k}\left(\left(\tilde{\mathcal{S}}_{n_1}^{(\vec{b}_1)}(\vec{\ell}_1),\cdots,\tilde{\mathcal{S}}_{n_k}^{(\vec{b}_k)}(\vec{\ell}_k)\right),\left(\tilde{\mathcal{T}}_{r_1},\cdots,\tilde{\mathcal{T}}_{r_{N-k}}\right)\right). \tag{96}$$

We use (93) in the first equality of (95) and we use

$$\tilde{\mathcal{E}}_N := \sum_{r=1}^L p_r \tilde{\mathcal{T}}_r,\tag{97}$$

and

$$P_{\text{MDRIFT}}(\vec{r}, N - k) = p_{r_1} \cdots p_{r_{N-k}}, \tag{98}$$

with  $\vec{\ell} = \{\ell_1 \cdots \ell_{N-k}\}$  in the second equality. By substituting (95) to (92), we obtain

$$\delta q_{\sigma}^{(k)} \left( \vec{n}, \left( \vec{\ell_1}, \cdots, \vec{\ell_k} \right) \right) \\
= \sum_{\vec{b_1} \cdots \vec{b_k}} \sum_{\vec{r}} P_{\text{MDRIFT}}(\vec{r}, N - k)$$

$$\operatorname{Tr} \left( \tilde{Q} \mathcal{C}_{\sigma, k, N - k}^{(\vec{b_1}, \cdots, \vec{b_k})} \left( \vec{n}, \left( \vec{\ell_1}, \cdots \vec{\ell_k} \right), \vec{r} \right) (\tilde{\rho}_{\text{init}}) \right).$$
(99)

Finally, combining (73), (74), and (82) with (99),

$$\delta q^{(k)}(\vec{n}) = \binom{N}{k} \frac{\tau^{\sum_{j=1}^{k} n_j}}{n_1! n_2! \cdots n_k!} \frac{1}{\binom{N}{k}} \sum_{\sigma \in S_{N,k}^{\text{sub}}} \delta q_{\sigma}^{(k)}(\vec{n}),
= c^{(k)}(\vec{n}) \sum_{\vec{b_1} \cdots \vec{b_k}} \sum_{\vec{s}} (-1)^{\sum_{c=1}^{k} s_c} \delta q^{(k)} \left( \left( \vec{b_1}, \cdots \vec{b_k} \right), \vec{s} \right),
(100)$$

where

$$\delta q^{(k)} \left( \left( \vec{b}_{1}, \cdots \vec{b}_{k} \right), \vec{s} \right)
:= \frac{1}{\binom{N}{k}} \sum_{\sigma \in S_{N,k}^{\text{sub}}} \sum_{\vec{\ell}_{1}, \cdots \vec{\ell}_{k}} P_{s_{1}}^{(n_{1})}(\vec{\ell}_{1}) \cdots P_{s_{k}}^{(n_{k})}(\vec{\ell}_{k})
\sum_{\vec{r}} P_{\text{MDRIFT}}(\vec{r}, N - k)
\text{Tr} \left( \tilde{Q} C_{\sigma,k,N-k}^{(\vec{l}_{1}, \cdots, \vec{b}_{k})} \left( \vec{n}, \left( \vec{\ell}_{1}, \cdots \vec{\ell}_{k} \right), \vec{r} \right) (\tilde{\rho}_{\text{init}}) \right),$$
(101)

and we define the coefficient as

$$c^{(k)}(\vec{n}) := \binom{N}{k} \frac{\tau^{\sum_{j=1}^{k} n_j}}{n_1! n_2! \cdots n_k!}.$$
 (102)

We can get an unbiased estimator of (101) using Monte Carlo sampling. More specifically, we repeat the following procedure and compute the average of the output: the p-th operation works as follows:

- 1. Sample  $\sigma$  uniformly from all elements of  $S_{N,k}^{\text{sub}}$ .
- 2. Sample  $\vec{\ell}_1, \dots \vec{\ell}_k$  according to  $P_{s_1}^{n_1}(\vec{\ell}_1) \dots P_{s_k}^{n_k}(\vec{\ell}_k)$ . Sample  $\vec{r}$  according to  $P_{\text{MDRIFT}}(\vec{r}, N k)$ .
- 3. Evaluate

$$\operatorname{Tr}\left(\tilde{Q}C_{\sigma,k,N-k}^{(\vec{b}_{1},\cdots,\vec{b}_{k})}\left(\vec{n},\left(\vec{\ell}_{1},\cdots\vec{\ell}_{k}\right),\vec{r}\right)(\tilde{\rho}_{\mathrm{init}})\right), \quad (103)$$

with  $N_{\rm shot}$  measurements. We set the result to  $\delta\hat{q}_{\sigma_p}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)$ .

As in the second-order case, we repeat the above process  $N_{\text{sample}}$  times and compute the average of  $\delta\hat{q}_{\sigma_p}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)$  as  $\delta\hat{q}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)$ , which gives the estimate of  $\delta q^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)$ . Substituting the estimate to (100), we obtain the estimate of  $\delta q^{(k)}(\vec{n})$  as

$$\delta \hat{q}^{(k)}(\vec{n}) = c^{(k)}(\vec{n}) \sum_{\vec{b_1} \cdots \vec{b_k}} \sum_{\vec{s}} (-1)^{\sum_{c=1}^k s_c} \delta \hat{q}^{(k)} \left( \left( \vec{b_1}, \cdots \vec{b_k} \right), \vec{s} \right).$$
(104)

We write the above algorithm to estimate  $\delta q^{(k)}(\vec{n})$  as **Evalcorrection** and summarize it in **Algorithm 1**. By using the **Evalcorrection**, we can construct the algorithm to compute  $q^{(K)}$  according to (67). We write

# Algorithm 1 Evalcorrection

```
Input: k, \vec{n}, N, N_{\text{sample}}, and N_{\text{shot}}
1: for \vec{s} in \{0,1\}^{\otimes k} do
               for (\vec{b}_1,...,\vec{b}_k) in (\{0,1\}^{\otimes n_1},...,\{0,1\}^{\otimes n_k}) do
  3:
                    for p = 1 to N_{\text{sample}} do
                          Sample \sigma uniformly from S_{N.k}^{\text{sub}}.
  4:
                          Sample \vec{\ell}_1, \dots, \vec{\ell}_k according to P_{s_1}^{n_1}(\vec{\ell}_1) \dots P_{s_k}^{n_k}(\vec{\ell}_k). Sample \vec{r} according to P_{\text{MDRIFT}}(\vec{r}, N-k).
  5:
                          With N_{\text{shot}} measurements, estimate the following by the quantum circuit and set it to \delta \hat{q}_{\sigma_p}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right):
  6:
                                                                                                \operatorname{Tr}\left(\tilde{Q}\mathcal{C}_{\sigma,k,N-k}^{(\vec{b}_1,\cdots,\vec{b}_k)}\left(\vec{n},\left(\vec{\ell}_1,\cdots\vec{\ell}_k\right),\vec{r}\right)(\tilde{\rho}_{\mathrm{init}})\right),
                    end for Set \delta \hat{q}^{(k)}\left(\left(\vec{b_1}, \cdots \vec{b_k}\right), \vec{s}\right) = \frac{1}{N_{\text{sample}}} \sum_{p=1}^{N_{\text{sample}}} \delta \hat{q}_{\sigma_p}^{(k)}\left(\left(\vec{b_1}, \cdots \vec{b_k}\right), \vec{s}\right).
  7:
  8:
              end for
  9:
10: end for
11: Set
                                                                          \delta \hat{q}^{(k)}(\vec{n}) = c^{(k)}(\vec{n}) \sum_{\vec{b_1} \dots \vec{b_l}} \sum_{\vec{s}} (-1)^{\sum_{c=1}^k s_c} \delta \hat{q}^{(k)} \left( \left( \vec{b_1}, \dots \vec{b_k} \right), \vec{s} \right).
```

Output:  $\delta \hat{q}^{(k)}(\vec{n})$

# Algorithm 2 qSWIFT

```
Input: K, N, N_{\text{sample}}(\vec{n}), N_{\text{shot}}(\vec{n}), N_{\text{sample}}^{0}, and N_{\text{shot}}^{0}
 1: Estimate \text{Tr}(Q\mathcal{E}_N^N(\rho_{\text{init}})) by sampling N_{\text{sample}}^0 circuits and measuring each circuit N_{\text{shot}}^0 times; set the result to \hat{q}^{(1)}.
 2: Set delta = 0.
 3: for \xi = 2, ..., 2K - 2 do
         for k = 1, ..., K do
 4:
             for \vec{n} \in G_2(k,\xi) do
 5:
 6:
                 Add the result of Evalcorrection (k, \vec{n}, N, N_{\text{sample}}(\vec{n}), N_{\text{shot}}(\vec{n})) to delta.
 7:
             end for
 8:
         end for
 9: end for
10: Set \hat{q}^{(K)} = \hat{q}^{(1)} + \text{delta}.

Output: \hat{q}^{(K)}
```

the algorithm as **qSWIFT** and summarize it in **Algorithm 2**. Since we can tune  $N_{\rm sample}$  and  $N_{\rm shot}$  depending on  $\delta \hat{q}^{(k)}(\vec{n})$  we parameterize them as  $N_{\rm sample}(\vec{n})$  and  $N_{\rm shot}(\vec{n})$ . We also write the number of circuits sampled and the number of running each circuit for calculating  $q^{(1)}$  as  $N_{\rm sample}^0$  and  $N_{\rm shot}^0$ .

It should be noted that there is a statistical error in  $\hat{q}^{(K)}$  due to the use of Monte Carlo sampling and the limited number of measurements. To reduce the statistical error, we need to increase  $N_{\text{sample}}(\vec{n})$ ,  $N_{\text{shot}}(\vec{n})$ ,  $N_{\text{shot}}^0$ . We show how the total number of quantum circuits runs scale with the order in Appendix B even though our focus in this paper is discussing the reduction of systematic error and not the statistical error. In the discussion, we show that the dominant source of the quantum circuit runs comes from the estimation of  $\Delta \hat{q}^{(k)}(\vec{n})$  with limited  $\vec{n}$  and the cost for  $\Delta \hat{q}^{(k)}(\vec{n})$  with other  $\vec{n}$  is negligible when N is large; consequently, the total number of quantum circuit runs scale only less than quadratically with K.

In this section, we present the high-order qSWIFT method by expanding the unitary channel  $\mathcal{U}$ , where the systematic error decreases exponentially with the order parameter. We wish to highlight that it is possible to

construct an all-order qSWIFT, which completely eliminates systematic error, as shown in Appendix C. To avoid exponentially large statistical errors, we must set  $N \in \mathcal{O}\left((\lambda t)^2\right)$ . The primary drawback of the all-order qSWIFT is the lack of an upper bound for the number of swift operators. Therefore, the higher-order qSWIFT is more appropriate for use in quantum devices with limited gate operation capacity. The detail of the all-order qSWIFT is described in Appendix C.

# C. Note on the previous higher-order randomized ${\rm method}$

We mention that the work by Wan et al. [18] introduces a higher-order randomized technique for phase estimation, where the task is to compute  $\text{Tr}[\rho e^{iHt}]$  with  $\rho$  as the initial state. They propose a randomized approach to estimate  $\text{Tr}[\rho e^{iHt}]$  that leverages the linear combination of unitaries (LCU) scheme. Methodologically, they express  $e^{iHt}$  as a weighted sum of unitary operations and select a term for sampling based on a specific probability distribution.

While the study [18] is primarily focused on phase

![](_page_11_Figure_1.jpeg)

FIG. 3. The asymptotic behaviors of N for each time for each molecule to achieve the systematic error  $\varepsilon = 0.001$ . Three subfigures correspond to each molecule: propane with STO-3G basis (left), ethane with 6-31G basis (center), and carbon dioxide with the 6-31G basis (right). We show the third-order qSWIFT by the pink line (qSWIFT-3), the sixth-order qSWIFT by the pink dotted line (qSWIFT-6), and the qDRIFT by the black line (qDRIFT). For the Trotter-Suzuki decomposition, the best of the deterministic method among the first, second, and fourth order is shown by the gray dotted line (TS (Best)), and the best of the randomized method is shown by the green dotted line (RTS (Best)).

![](_page_11_Figure_3.jpeg)

FIG. 4. The asymptotic behavior to achieve  $\varepsilon = 10^{-6}$ . Other settings are the same as Fig. 3.

estimation, it could be extended to a higher-order randomization approach to estimate  $q = \text{Tr}(QU(\rho_{\text{init}})) = \text{Tr}(Qe^{iHt}\rho_{\text{init}}e^{-iHt})$  by expanding  $e^{iHt}$  and  $e^{-iHt}$  in a similar fashion to the LCU technique, which we refer to as the LCU-based method. Detailed in Appendix D, this method, as in the all-order qSWIFT presented in Appendix C, is free from systematic error. Nonetheless, the LCU-based method demands that all the  $\mathcal{O}((\lambda t)^2)$  time-evolution operations to be controlled by the ancilla qubit. In contrast, qSWIFT only requires swift operators to interact with the ancilla qubit. Appendix D illustrates how the demand for  $\mathcal{O}((\lambda t)^2)$  time evolutions in the LCU-based method could lead to a substantial increase in the number of control gates in comparison to qSWIFT for certain problems.

### V. NUMERICAL EXPERIMENTS

In this section, we present two numerical simulations of qSWIFT. In Section  $V\,A$ , we show the asymptotic behavior of qSWIFT and compare it with Trotter-Suzuki decomposition and qDRIFT. In Section  $V\,B$ , we perform a numerical experiment with the hydrogen molecule Hamiltonian and compare its performance with those of the previous algorithms.

### A. Asymptotic behaviour

We compute the required number of gates N to achieve a given systematic error for each evolution time and each algorithm: qSWIFT, Trotter-Suzuki decomposition, and qDRIFT. To clarify the difference from the original qDRIFT, we use the three molecules used in the numerical experiment of the original paper [5]:

propane, ethane, and carbon dioxide.

For the qSWIFT algorithm, we utilize the third-order (K=3) qSWIFT. We also use the sixth-order qSWIFT (K=6) as a reference. For the Trotter-Suzuki decomposition, we use both the deterministic and the randomized methods of the first, second, and fourth order. For calculating the systematic error of qSWIFT, we use the bound (A22) derived in Appendix A 2. For the error of qDRIFT and the Trotter-Suzuki decompositions, we utilize the same upper-bound formulae as in the literature [5] (See Appendix B and Appendix C of [5]).

Fig 3 show the asymptotic behaviors of N for each time to achieve the systematic error  $\varepsilon=0.001$ , which includes three subfigures corresponding to each molecule: propane with STO-3G basis (left), ethane with 6-31G basis (center), and carbon dioxide with 6-31G basis (right). To generate each molecule Hamiltonian, we use OpenFermion [19]. For each figure, we show the third-order qSWIFT by the pink line (qSWIFT-3), the sixth-order qSWIFT by the pink dotted line (qSWIFT-6), and the qDRIFT by the black line (qDRIFT). For the Trotter-Suzuki decomposition, the best of the deterministic method among the first, second, and fourth order is shown by the gray dotted line (TS (Best)), and the best of the randomized method is shown by the green dotted line (RTS (Best)).

We see that the qSWIFT algorithms outperform the qDRIFT for all t in the sense that the required number of gates N is more than 10 times smaller in the qSWIFT algorithms than in the qDRIFT. While the original qDRIFT reduces the number of gates in the region  $t \lesssim 10^8$  from the Trotter-Suzuki decompositions, the qSWIFT algorithms realize a further reduction of the gates. Note that the improvement from the third-order qSWIFT to the sixth-order qSWIFT is not as large as that from the qDRIFT to the third-order qSWIFT. Since there is a trade-off between the order and the number of quantum circuits run as we discuss in Appendix B, it may be better to utilize the third-order qSWIFT rather than the sixth-order qSWIFT though it depends on the features of quantum devices.

Fig. 4 is the same figure as Fig. 3; other than that, the required systematic error is  $\varepsilon = 10^{-6}$ . In this case, where more precise time evolution is necessary, the merit of using qSWIFT is much clearer. In qSWIFT-3 (qSWIFT-6), the required number of gates for each time is almost 1,000 (10,000) times smaller than that of gDRIFT. The region where gDRIFT has an advantage over the Trotter-Suzuki is very limited ( $t \lesssim 10^5 \sim 10^6$ ) due to the bad scaling of qDRIFT in terms of  $\varepsilon$ . In contrast, the region where qSWIFT has the advantage over Trotter-Suzuki decompositions does not change much from the case of  $\varepsilon = 0.001$  ( $t \lesssim 10^9 \sim 10^{10}$ ). This result shows the merit of our algorithm; in the case of qDRIFT, we need to increase the number of gates to reduce the systematic error, but in the case of our qSWIFT, it can be reduced just by increasing the order parameter of the algorithm.

We note that as we write at the end of Section II A, we can further improve the bound for the deterministic Trotter-Suzuki decomposition (TS) by using the commutator bounds [3] represented as the commutator

relation. It should also be noted that the derivation of upper bounds for qDRIFT and qSWIFT involves many triangular inequalities that are loosely bounded. Therefore, the upper bounds for the randomized compiling methods could also be improved by considering relations between operators, presenting a promising direction for future research.

### B. Simulation of the hydrogen molecule

We estimate  $\text{Tr}(QU(\rho_{\text{init}}))$  by using qSWIFT algorithm described in Algorithm 2 with an observable Q, time evolution  $\mathcal{U}$ , and an input state  $\rho_{\text{init}}$ . For  $\mathcal{U}$ , we implement the time evolution with the hydrogen molecule Hamiltonian with the 6-31G basis and t=1. Again we use OpenFermion [19] to generate the molecule Hamiltonian. We utilize the Bravyi-Kitaev transformation [20] for transforming the Fermionic operators to Pauli operators. The number of terms in the Hamiltonian L is 184. The generated Hamiltonian has eight qubits, and therefore, we use a system with nine qubits (including one ancilla qubit). As for the observable Q, we choose Q = ZIIIIIIII, and as for the input state, we choose  $\rho_{\text{init}} = |+\rangle^{\otimes 8}$ . For comparison, we also estimate  $Tr(QU(\rho_{init}))$  by using the qDRIFT and the Trotter-Suzuki decomposition. As the input parameters of the qSWIFT, we set  $N_{\text{shot}}^0 = N_{\text{shot}}(\vec{n}) = 100$ ,  $N_{\rm sample}^0 = 400,000$ , and  $N_{\rm sample}(\vec{n}) = C(\vec{n}) \times N_{\rm sample}^0$ . For qDRIFT and the randomized Trotter-Suzuki decomposition, we sample  $N_{\text{sample}}^0$  quantum circuits and perform  $N_{\rm shot}^0$  measurements for each circuit. For the deterministic Trotter-Suzuki decomposition, we perform  $N_{\rm shot}^0 \times N_{\rm sample}^0$  measurements. For the quantum circuit simulation, we use Qulacs [21].

Fig. 5 shows the estimation error of  $Tr(QU(\rho_{init}))$ for each number of gates N for each method. In plotting each point, we perform six trials and show the mean value and the standard deviation of the mean. For qSWIFT, we show the result of the second-order (qSWIFT-2) with the purple line and the third-order (qSWIFT-3) with the pink line. The result of the qDRIFT (qDRIFT) is plotted with the black line. For the Trotter-Suzuki decomposition, we show the first and second-order results. The minimum N for the first and second Trotter-Suzuki decomposition is 184 and 368 (1840 for the fourth order). For the deterministic Trotter-Suzuki decomposition, the first-order result (TS-1st) is plotted with the dotted gray line, and the second-order result (TS-2nd) is plotted with the dotted green line. For the randomized Trotter-Suzuki decomposition, the first-order result (RTS-1st) is plotted with the dotted yellow line, and the second-order result (RTS-2nd) is plotted with the dotted blue line.

We see that qSWIFT algorithms outperform the other methods. Particularly, the required N for the third-order qSWIFT for achieving  $\varepsilon \sim 0.001$  is almost 10 times smaller than that for qDRIFT, which is consistent with the asymptotic behavior shown in Fig. 3. Consequently, even in the region where Trotter-Suzuki decomposition works better than qDRIFT, qSWIFT al-

![](_page_13_Figure_1.jpeg)

FIG. 5. The estimation error of  $\text{Tr}(QU(\rho_{\text{init}}))$  for each number of gates N for each method with Q=ZIIIIIII and  $\rho_{\text{init}}=|+\rangle^{\otimes 8}$ . The time evolution is performed by the hydrogen molecule Hamiltonian with 6-31g basis transformed by the Bravyi-Kitaev transformation. The evolution time is set to be t=1. In plotting each point, we perform six trials and show the mean value and the standard deviation of the mean. For qSWIFT, we show the result of the second-order (qSWIFT-2) with the purple line and the third-order (qSWIFT-3) with the pink line. The result of the qDRIFTalgorithm (qDRIFT) is plotted with the black line. For the deterministic Trotter-Suzuki decomposition, the first-order result (TS-1st) is plotted with the dotted gray line, and the second-order result (RTS-1st) is plotted with the dotted yellow line, and the second-order result (RST-2nd) is plotted with the dotted yellow line, and the second-order result (RST-2nd) is plotted with the dotted blue line.

gorithms outperform Trotter-Suzuki decompositions.

## VI. CONCLUSION AND DISCUSSION

Hamiltonian simulation is a crucial subroutine of various quantum algorithms. Approaches based on the product formulae are practically favored due to their simplicity and ancilla-free nature. There are two representative product formulae-based methods: Trotter-Suzuki decompositions and qDRIFT [5]. Trotter-Suzuki decompositions have the issue that the number of gates depends on the number of the terms in the Hamiltonian, at least linearly. In contrast, qDRIFT avoids the dependency on the number of terms but has the issue that the number of gates is dependent on the systematic error  $\varepsilon$  as  $O(1/\varepsilon)$ .

In this paper, we propose qSWIFT, a high-order randomized algorithm having both the advantage of the Trotter Suzuki decompositions and qDRIFT, in the sense that its gate count is independent of the number of terms and that the gate count is asymptotically optimal with respect to the precision. We construct the qSWIFT channel and bound the systematic error by the diamond norm. We prove that the qSWIFT channel satisfies the required precision that decreases exponentially with the order parameter in terms of the diamond norm. Then we construct the algorithm by applying the qSWIFT channel to estimate given physical quantities. The algorithm requires a system as simple

as qDRIFT; it requires just one ancilla qubit, and only the time evolution operators and the swift operators constructible with the gate in Fig. I are necessary to construct the quantum circuits. Our numerical demonstration shows that qSWIFT outperforms qDRIFT with respect to the number of gates for required precision. Particularly when high precision is required, there is a significant advantage of using qSWIFT; the number of gates in the third-order (sixth-order) qSWIFT is 1000 (10000) times smaller than qDRIFT to achieve the systematic error of  $\varepsilon=10^{-6}$ .

As a future direction, it is beneficial to perform case studies to investigate the performance of qSWIFT in specific problems. Particularly, the literature [22] points out that the qDRIFT does not perform well in the phase estimation problems, unlike originally expected [5] due to the relatively large systematic error for a given number of gates. In contrast, since qSWIFT can successfully reduce systematic error by increasing the order parameter, we expect that the performance in the phase estimation is significantly improved with qSWIFT. Also, as we note in Section I, there are algorithms using many ancilla qubits [6–11] that achieve a better asymptotic gate scaling with respect to  $\lambda$  and t though its constant prefactor is relatively large compared to qDRIFT and qSWIFT. Comparing qSWIFT with those algorithms and discussing the advantages of each algorithm in specific problems is a promising direction for future work.

Whether we can improve the scaling with respect to  $\lambda t$  within the framework of qDRIFT and qSWIFT is

another important open question. Unlike qDRIFT and qSWIFT, where the number of gates required for a given error scales quadratically with  $\lambda t$ , the scaling with t can be improved by increasing the order parameter in the Trotter-Suzuki decomposition. Developing methods to enhance the  $\lambda t$  scaling would further expedite the realization of practical Hamiltonian simulations.

search Fellow 22J01501. A.A.-G. acknowledges support from the Canada 150 Research Chairs program and CI-FAR. A.A.-G. acknowledges the generous support of Anders G. Frøseth.

#### ACKNOWLEDGEMENT

We thank Nathan Wiebe for helpful discussions. K.N. acknowledges the support of Grant-in-Aid for JSPS Re-

# Appendix A: Bound for the systematic errors in qSWIFT channels

#### 1. Error bound for the second-order qSWIFT channel

In this subsection, we prove the error bound given in Lemma III.3 for our second-order qSWIFT channel. To this end, we utilize the triangle and submultiplicative properties of the diamond norm. Namely, we utilize

$$||\mathcal{A} + \mathcal{B}||_{\diamond} \le ||\mathcal{A}||_{\diamond} + ||\mathcal{B}||_{\diamond},\tag{A1}$$

$$||\mathcal{A}\mathcal{B}||_{\diamond} \le ||\mathcal{A}||_{\diamond} ||\mathcal{B}||_{\diamond},\tag{A2}$$

for given channels  $\mathcal{A}$  and  $\mathcal{B}$ .

The diamond distance between the exact time evolution and the qSWIFT channel can be evaluated as

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(2)}\right) = \frac{1}{2}||M_{1,N-1}\left(\Delta_{3},\mathcal{E}_{N}\right) + \sum_{k=2}^{N} M_{k,N-k}\left(\Delta_{2},\mathcal{E}_{N}\right)||_{\diamond}$$

$$\leq \frac{1}{2}||M_{1,N-1}\left(\Delta_{3},\mathcal{E}_{N}\right)||_{\diamond} + \frac{1}{2}\sum_{k=2}^{N}||M_{k,N-k}\left(\Delta_{2},\mathcal{E}_{N}\right)||_{\diamond},$$

$$\leq \frac{1}{2}\sum_{n=3}^{\infty} \frac{\tau^{n}}{n!}||M_{1,N-1}(\mathcal{L}^{(n)},\mathcal{E}_{N})||_{\diamond} + \frac{1}{2}\sum_{k=2}^{N}\sum_{n_{1},\dots,n_{k}=2}^{\infty} \frac{\tau^{\sum_{j}^{k}n_{j}}}{n_{1}!\dots n_{k}!}||M_{k,N-k}\left(\left(\mathcal{L}^{(n_{1})},\dots,\mathcal{L}^{(n_{k})}\right),\mathcal{E}_{N}\right)||_{\diamond},$$
(A3)

where we use (A1) and (A2) to show the inequality. By the definition of the mixture function  $M_{k,N-k}$  in Eq. (19) and using the triangle and submultiplicative properties of the diamond norm, we obtain

$$||M_{k,N-k}\left(\left(\mathcal{L}^{(n_1)},\ldots,\mathcal{L}^{(n_k)}\right),\mathcal{E}_N\right)||_{\diamond} \leq \sum_{\sigma \in S_{N,k}^{\text{sub}}} ||f_{\sigma,k,N-k}\left(\left(\mathcal{L}^{(n_1)},\ldots,\mathcal{L}^{(n_k)}\right),\mathcal{E}_N\right)||_{\diamond}$$

$$\leq \binom{N}{k} \prod_{j=1}^k ||\mathcal{L}^{(n_j)}||_{\diamond} ||\mathcal{E}_N||_{\diamond}^{N-k}$$

$$\leq \binom{N}{k} 2^{k+\sum_{j=1}^k n_j}.$$
(A4)

To show the last inequality we use

$$||\mathcal{L}^{(n)}||_{\diamond} \le ||\mathcal{L}||_{\diamond}^{n} + \sum_{\ell=1}^{L} p_{\ell}||\mathcal{L}_{\ell}||_{\diamond}^{n} \le 2^{n+1},$$
 (A5)

which holds since  $||\mathcal{L}||_{\diamond} \leq 2$  and  $||\mathcal{L}_{\ell}||_{\diamond} \leq 2$ . By using (A4),

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(2)}\right) \leq \frac{1}{2} \sum_{n=3}^{\infty} \frac{\tau^{n}}{n!} \binom{N}{1} 2^{n+1} + \frac{1}{2} \sum_{k=2}^{N} \sum_{n_{1}, \dots n_{k}=2}^{\infty} \frac{\tau^{\sum_{j}^{k} n_{j}}}{n_{1}! \dots n_{k}!} \binom{N}{k} 2^{k+\sum_{j=1}^{k} n_{j}}$$

$$= \frac{1}{2} \sum_{n=3}^{\infty} \frac{N\tau^{n}}{n!} 2^{n+1} + \frac{1}{2} \sum_{k=2}^{N} \sum_{n_{1}, \dots n_{k}=2}^{\xi} \sum_{\xi=4}^{\infty} \delta \left[\xi, \sum_{j=1}^{k} n_{j}\right] \frac{\tau^{\xi}}{n_{1}! \dots n_{k}!} \binom{N}{k} 2^{k+\xi}, \tag{A6}$$

where in the second line, we use

$$\sum_{\xi=4}^{\infty} \delta \left[ \xi, \sum_{j=1}^{k} n_j \right] = 1, \tag{A7}$$

which holds for a fixed set of integers  $\{n_j\}_{j=1}^k$  with  $n_j \ge 2$  and  $k \ge 2$ . By using that  $1/n \le 1/2$  in the summand of the first term and  $1/n_j \le 1/2$  in the summand of the second term, we obtain

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(2)}\right) \leq \frac{1}{2} \sum_{n=3}^{\infty} (2\tau)^{n} N + \frac{1}{2} \sum_{\xi=4}^{\infty} \sum_{k=2}^{N} (2\tau)^{\xi} \binom{N}{k} \sum_{n_{1},\dots n_{k}=2}^{\xi} \delta \left[\xi, \sum_{j=1}^{k} n_{j}\right],$$

$$= \frac{1}{2} \sum_{n=3}^{\infty} (2\tau)^{n} N + \frac{1}{2} \sum_{\xi=4}^{\infty} \sum_{k=2}^{\lfloor \xi/2 \rfloor} (2\tau)^{\xi} \binom{N}{k} \sum_{n_{1},\dots n_{k}=2}^{\xi} \delta \left[\xi, \sum_{j=1}^{k} n_{j}\right],$$
(A8)

with  $\lfloor x \rfloor$  as the largest integer that does not exceed a real value x, where we use the fact that the summand of the second term vanishes if  $k \geq \lfloor \xi/2 \rfloor$ . Using

$$\sum_{n_1,\dots,n_k=2}^{\xi} \delta \left[ \xi, \sum_{j=1}^k n_j \right] \le \xi^k, \tag{A9}$$

we obtain

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(2)}\right) \leq \frac{1}{2} \sum_{n=3}^{\infty} (2\tau)^{n} \binom{N}{1} + \frac{1}{2} \sum_{\xi=4}^{\infty} \sum_{k=2}^{\lfloor \xi/2 \rfloor} (2\tau)^{\xi} \binom{N}{k} \xi^{k},$$

$$\leq \frac{1}{2} \sum_{n=3}^{\infty} (2\tau)^{n} N + \frac{1}{2} \sum_{\xi=4}^{\infty} (2\tau)^{\xi} N^{\lfloor \xi/2 \rfloor} \sum_{k=2}^{\lfloor \xi/2 \rfloor} \frac{\xi^{k}}{k!}$$

$$\leq \frac{1}{2} \sum_{n=3}^{\infty} (2\tau)^{n} N + \frac{1}{2} \sum_{\xi=4}^{\infty} (2e\tau)^{\xi} N^{\lfloor \xi/2 \rfloor}$$

$$\leq \frac{1}{2} \sum_{\xi=3}^{\infty} (2e\tau)^{\xi} N^{\lfloor \xi/2 \rfloor},$$
(A10)

where to show the third inequality, we use

$$\sum_{k=1}^{\lfloor \xi/2 \rfloor} \frac{\xi^k}{k!} \le \sum_{k=0}^{\infty} \frac{\xi^k}{k!} = e^{\xi}. \tag{A11}$$

Now let us evaluate  $\frac{1}{2} \sum_{\xi=2K-1}^{\infty} (2e\tau)^{\xi} N^{\lfloor \xi/2 \rfloor}$  (in the current case, K=2). It can be evaluated depending on if  $\xi$  is odd ( $\xi=2m$  with m as an integer) or even ( $\xi=2m-1$ ) as,

$$\sum_{\xi=2K-1}^{\infty} \frac{1}{2} (2e\tau)^{\xi} N^{\lfloor \xi/2 \rfloor} \leq \frac{1}{2} \sum_{m=K}^{\infty} (2e\tau)^{2m} N^m + \frac{1}{2} \sum_{m=K}^{\infty} (2e\tau)^{2m-1} N^{m-1}$$

$$= \frac{1}{2} \left( 1 + \frac{1}{2eN\tau} \right) \sum_{m=K}^{\infty} (2e\tau)^{2m} N^m$$

$$= \eta(\lambda t, N) \left( \frac{(2e\lambda t)^2}{N} \right)^K,$$
(A12)

as far as

$$\frac{(2e\lambda t)^2}{N} < 1,\tag{A13}$$

where

$$\eta(x,N) := \frac{1}{2} \left( 1 + \frac{1}{2ex} \right) \frac{1}{1 - (2ex)^2/N}.$$
(A14)

By setting K=2, we obtain the bound

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(2)}\right) \leq \eta(\lambda t, N) \left(\frac{(2e\lambda t)^{2}}{N}\right)^{2}.$$
(A15)

In the reasonable parameter range:  $1 \le \lambda t \le \sqrt{N}/2\sqrt{2}e$  (where the latter inequality holds by choosing suitable N), it holds  $\eta(\lambda t, N) \le 3/2$ , and therefore

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(2)}\right) \leq \frac{3}{2}\left(\frac{(2e\lambda t)^{2}}{N}\right) \in \mathcal{O}\left(\left(\frac{(\lambda t)^{2}}{N}\right)^{2}\right). \tag{A16}$$

## 2. Error bound for the higher-order qSWIFT channels

We now prove the error bound given in Lemma IV.2 for the K-th order qSWIFT channel. By the definition of this channel in Eq. (63), we have

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(K)}\right) = \frac{1}{2}||\Phi^{(\infty)} - \mathcal{E}^{(K)}||_{\diamond} \tag{A17}$$

$$= \frac{1}{2} \sum_{\xi=2K-1}^{\infty} \tau^{\xi} \sum_{k=1}^{N} \sum_{n_{1},\dots,n_{k}=2}^{\xi} \frac{1}{n_{1}! n_{2}! \cdots n_{k}!} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right] M_{k,N-k} \left( \left( \mathcal{L}^{(n_{1})}, \dots, \mathcal{L}^{(n_{k})} \right), \mathcal{E}_{N} \right)$$
(A18)

$$\leq \frac{1}{2} \sum_{\xi=2K-1}^{\infty} \tau^{\xi} \sum_{k=1}^{N} \sum_{n_{1},\dots,n_{k}=2}^{\xi} \frac{1}{n_{1}! n_{2}! \cdots n_{k}!} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right] ||M_{k,N-k} \left( \left( \mathcal{L}^{(n_{1})}, \dots, \mathcal{L}^{(n_{k})} \right), \mathcal{E}_{N} \right) ||_{\diamond},$$
 (A19)

where we used the triangular inequality (A1).

By substituting (A4) into (A17), we obtain

$$d_{\diamond} \left( \mathcal{U}, \mathcal{E}^{(K)} \right) \leq \frac{1}{2} \sum_{\xi=2K-1}^{\infty} \tau^{\xi} \sum_{k=1}^{N} \sum_{n_{1}, \dots, n_{k}=2}^{\xi} \frac{1}{n_{1}! n_{2}! \cdots n_{k}!} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right] \binom{N}{k} 2^{\xi+k}$$

$$\leq \frac{1}{2} \sum_{\xi=2K-1}^{\infty} (2\tau)^{\xi} \sum_{k=1}^{N} \binom{N}{k} \sum_{n_{1}, \dots, n_{k}=2}^{\xi} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right], \qquad (A20)$$

$$= \frac{1}{2} \sum_{\xi=2K-1}^{\infty} (2\tau)^{\xi} \sum_{k=1}^{\lfloor \xi/2 \rfloor} \binom{N}{k} \sum_{n_{1}, \dots, n_{k}=2}^{\xi} \delta \left[ \xi, \sum_{j=1}^{k} n_{j} \right].$$

We use  $1/n_j \le 1/2$  for  $(n_j \ge 2)$  in the second inequality and to show the third equality, we use the fact that summands with  $k > |\xi/2|$  vanishes. Using (A9), we obtain

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(K)}\right) \leq \frac{1}{2} \sum_{\xi=2K-1}^{\infty} (2\tau)^{\xi} \sum_{k=1}^{\lfloor \xi/2 \rfloor} \binom{N}{k} \xi^{k},$$

$$\leq \frac{1}{2} \sum_{\xi=2K-1}^{\infty} (2\tau)^{\xi} N^{\lfloor \xi/2 \rfloor} \sum_{k=1}^{\lfloor \xi/2 \rfloor} \frac{\xi^{k}}{k!},$$

$$\leq \frac{1}{2} \sum_{\xi=2K-1}^{\infty} (2e\tau)^{\xi} N^{\lfloor \xi/2 \rfloor},$$
(A21)

where to show the last inequality, we use (A11). By using (A12), we obtain

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(K)}\right) \leq \eta(\lambda t, N) \left(\frac{(2e\lambda t)^{2}}{N}\right)^{K},\tag{A22}$$

In the reasonable parameter range:  $1 \le \lambda t \le \sqrt{N}/2\sqrt{2}e$  again, it holds  $\eta(\lambda t, N) \le 3/2$ , and therefore

$$d_{\diamond}\left(\mathcal{U},\mathcal{E}^{(K)}\right) \leq \frac{3}{2}\left(\frac{(2e\lambda t)^{2}}{N}\right) \in \mathcal{O}\left(\left(\frac{(\lambda t)^{2}}{N}\right)^{K}\right). \tag{A23}$$

Note that when we draw Fig. 3 and Fig. 4, we use the formula (A22).

### Appendix B: Statistical error

Due to the sampling error and the shot noise, there is a statistical error in  $\delta\hat{q}^{(k)}(\vec{n})$ . Let us estimate the statistical error in the following. For simplicity, we set  $N_{\rm shot}(\vec{n})=1$ . Let  $\Delta_q\left((\vec{b_1},\vec{b_2},\cdots,\vec{b_k}),\vec{s}\right)$  as the statistical error of  $\delta\hat{q}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)$ . Then, from the central limit theorem, it behaves as

$$\Delta_q\left((\vec{b_1}, \vec{b_2}, \cdots, \vec{b_k}), \vec{s}\right) \sim \frac{\operatorname{Var}\left(\delta\hat{q}^{(k)}\left(\left(\vec{b_1}, \cdots, \vec{b_k}\right), \vec{s}\right)\right)}{\sqrt{N_{\text{sample}}(\vec{n})}},\tag{B1}$$

where Var(A) denotes the variance of the variable A. In the rest of the section, we use ' $\sim$ ' with the same meaning. Since

$$-1 \le \delta \hat{q}^{(k)} \left( \left( \vec{b_1}, \cdots \vec{b_k} \right), \vec{s} \right) \le 1, \tag{B2}$$

from Popoviciu's inequality on variances, it holds  $\operatorname{Var}\left(\delta\hat{q}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)\right)\leq 1$ , and

$$\Delta_q\left((\vec{b_1}, \vec{b_2}, \cdots, \vec{b_k}), \vec{s}\right) \lesssim \frac{1}{\sqrt{N_{\text{sample}}(\vec{n})}}.$$
 (B3)

Using the fact that each  $\delta \hat{q}^{(k)}\left(\left(\vec{b_1},\cdots\vec{b_k}\right),\vec{s}\right)$  is independent, we can estimate the statistical error of  $\delta \hat{q}^{(k)}(\vec{n})$  as

$$|\delta q^{(k)}(\vec{n}) - \delta \hat{q}^{(k)}(\vec{n})| \leq c^{(k)}(\vec{n}) \sqrt{\sum_{\vec{b_1} \cdots \vec{b_k}} \sum_{\vec{s}} \left[ \Delta_q \left( (\vec{b_1}, \vec{b_2}, \cdots, \vec{b_k}), \vec{s} \right) \right]^2}$$

$$\lesssim c^{(k)}(\vec{n}) \sqrt{\frac{2^{\sum_j n_j + k}}{N_{\text{sample}}(\vec{n})}},$$
(B4)

where to show the second inequality, we use  $\sum_{\vec{b_1} \cdots \vec{b_k}} \sum_{\vec{s}} 1 = 2^{\sum_j n_j + k}$ . In other words, the statistical error is bounded as

$$|\delta q^{(k)}(\vec{n}) - \delta \hat{q}^{(k)}(\vec{n})| \le \varepsilon, \tag{B5}$$

if we set

$$N_{\text{sample}}(\vec{n}) \sim \frac{[c^{(k)}(\vec{n})]^2 \times 2^{\sum_j n_j + k}}{\varepsilon^2}.$$
 (B6)

Let  $N_{\rm total}^{(k)}(\vec{n})$  be the total circuit run for calculating  $\delta \hat{q}^{(k)}(\vec{n})$ . Then it holds

$$N_{\text{total}}(\vec{n}) = 2^{\sum_{j} n_j + k} \times N_{\text{sample}}(\vec{n}) \sim \frac{[c^{(k)}(\vec{n})]^2 \times 2^{2\sum_{j} n_j + 2k}}{\varepsilon^2}.$$
 (B7)

Let us further clarify the implication of (B7). Recall that in the qSWIFT algorithm, we only compute  $\delta \hat{q}^{(k)}(\vec{n})$  only if

$$\sum_{j=1}^{k} n_j = \xi, \quad n_j \ge 2 \ (\forall j). \tag{B8}$$

When the condition (B8) is satisfied, it holds

$$c^{(k)}(\vec{n}) \le N^k \left(\frac{\tau^{\xi}}{2^k}\right),$$
 (B9)

where  $\xi \geq 2k$  (the equality holds when  $n_j = 2$  for all j). Conversely,

$$c^{(k)}(\vec{n}) \le \begin{cases} \left(\frac{(\lambda t)^2}{2N}\right)^{\frac{\xi}{2}} & \text{if } n_j = 2 \text{ for all } j\\ \sqrt{\frac{2}{N}} \left(\frac{(\lambda t)^2}{2N}\right)^{\frac{\xi}{2}} & \text{otherwise} \end{cases}, \tag{B10}$$

meaning that  $c^{(k)}(\vec{n})$  is suppressed by the factor  $\sqrt{2/N}$  unless  $n_j=2$  is satisfied for all j. Therefore, the dominant source of the quantum circuits run comes from the calculation of  $\delta \hat{q}^{(k)}(\vec{n})$  with  $n_j=2$  for all j; and the number of measurements for calculating  $\delta \hat{q}^{(k)}(\vec{n})$  with other  $\vec{n}$  asymptotically becomes negligible as N becomes large. In the asymptotic limit, the total number of quantum circuits run  $N_{\text{total}}$  for computing all terms in  $q^{(K)}$  within the error  $\varepsilon$  in 2K-th order qSWIFT can be estimated as

$$N_{\text{total}} \approx N_{\text{sample}}^{0} + N_{\text{total}}^{(1)}(\{2\}) + N_{\text{total}}^{(2)}(\{2,2\}) + \cdots + N_{\text{total}}^{(K)}(\{2,\cdots2\})$$
 (B11)

$$\sim \frac{1}{\varepsilon^2} \sum_{k=0}^K \left( \frac{(2\lambda t)^2}{N} \right)^{\xi},$$
 (B12)

which includes the number of samples  $N_{\text{sample}}^0$  to compute  $q^{(1)}$ . The approximation in the first line denotes the asymptotic limit. To obtain the last expression, we use (B7) and also use that if  $N_{\text{shot}}^0 = 1$ , required number of samples to reduce the statistical error of  $q^{(1)}$  within  $\varepsilon$  is

$$N_{\text{sample}}^0 \sim \frac{1}{\varepsilon^2}$$
 (B13)

from the central limit theorem. To reduce the statistical error of  $q^{(K)}$  less than  $\varepsilon_{\text{total}}$ , we should set  $\varepsilon = \varepsilon_{\text{total}}/\sqrt{K+1}$ , and therefore,

$$N_{\text{total}} \sim \frac{K+1}{\varepsilon_{\text{total}}^2} \sum_{k=0}^{K} \left(\frac{(2\lambda t)^2}{N}\right)^{\xi}.$$
 (B14)

Thus, if we fix  $\varepsilon_{\text{total}}$ ,  $N_{\text{total}}$  scales less than quadratically with K as far as  $(2\lambda t)^2/N < 1$ .

## Appendix C: All-order qSWIFT

In the main text, we constructed the second-order and higher-order versions of qSWIFT, which include systematic errors dependent on the order parameter. In this section, we demonstrate that we can create an all-order version of qSWIFT that has no systematic error.

The expectation value of an observable can be expanded as

$$\operatorname{Tr}\left(Q\mathcal{U}(\rho_{\mathrm{init}})\right) = \operatorname{Tr}\left(Q(\mathcal{E}_{N} + \Delta_{2})^{N}(\rho_{\mathrm{init}})\right)$$

$$= \operatorname{Tr}\left(Q\left(\mathcal{E}_{N} + \sum_{n=2}^{\infty} \frac{\tau^{n}}{n!} \mathcal{L}^{(n)}\right)^{N}(\rho_{\mathrm{init}})\right)$$

$$= \operatorname{Tr}\left(Q\left(\mathcal{E}_{N} + \sum_{n=2}^{\infty} \frac{\tau^{n}}{n!} \sum_{\vec{\ell}} \sum_{s=0}^{1} (-1)^{s} P_{s}^{(n)}(\vec{\ell}) \mathcal{L}_{n}(\vec{\ell})\right)^{N}(\rho_{\mathrm{init}})\right)$$

$$= \operatorname{Tr}\left(\tilde{Q}\left(\tilde{\mathcal{E}}_{N} + \sum_{n=2}^{\infty} \frac{\tau^{n}}{n!} \sum_{\vec{\ell}} \sum_{s=0}^{1} (-1)^{s} P_{s}^{(n)}(\vec{\ell}) \tilde{\mathcal{L}}_{n}(\vec{\ell})\right)^{N}(\tilde{\rho}_{\mathrm{init}})\right)$$

$$= \operatorname{Tr}\left(\tilde{Q}\tilde{\mathcal{U}}_{N}^{N}(\tilde{\rho}_{\mathrm{init}})\right),$$
(C1)

where we use (28) in the second equality, and we use (76) and (79) in the third equality. We can readily show the fourth equality by using (91). In the last equality, we define

$$\tilde{\mathcal{U}}_N := \tilde{\mathcal{E}}_N + \sum_{n=2}^{\infty} \frac{\tau^n}{n!} \sum_{s=0}^{1} \sum_{\vec{b} \in \{0,1\} \otimes n} \sum_{\vec{\ell}} (-1)^s P_s^{(n)}(\vec{\ell}) \tilde{S}_n^{(b)}(\vec{\ell}). \tag{C2}$$

We can rewrite  $\tilde{\mathcal{U}}_N$  by using the physical channel as follows:

$$\tilde{\mathcal{U}}_{N} = \tilde{\mathcal{E}}_{N} + \sum_{n=2}^{\infty} \frac{2^{n+1}\tau^{n}}{n!} \frac{1}{2} \sum_{s=0}^{1} \frac{1}{2^{n}} \sum_{\vec{b} \in \{0,1\}^{\otimes n}} \sum_{\vec{\ell}} (-1)^{s} P_{s}^{(n)}(\vec{\ell}) \tilde{S}_{n}^{(b)}(\vec{\ell})$$

$$= \tilde{\mathcal{E}}_{N} + \sum_{n=2}^{\infty} \beta(n) \tilde{\mathcal{W}}_{n}$$

$$= B \mathcal{E}_{N}^{(\text{all})}.$$
(C3)

In the second equality of (C3), we define

$$\beta(n) := \frac{2^{n+1}\tau^n}{n!}, \ \tilde{\mathcal{W}}_n := \frac{1}{2} \sum_{s=0}^1 \frac{1}{2^n} \sum_{\vec{b} \in \{0,1\}^{\otimes n}} \sum_{\vec{\ell}} (-1)^s P_s^{(n)}(\vec{\ell}) \tilde{S}_n^{(b)}(\vec{\ell}), \tag{C4}$$

where  $\tilde{\mathcal{W}}_n(n \geq 2)$  is the physical channel; we can implement the process by sampling s and  $\vec{b}$  uniformly, sampling  $\vec{\ell}$  according to  $P_s^{(n)}(\vec{\ell})$ , and applying  $(-1)^s \tilde{S}_n^{(b)}(\vec{\ell})$ . In the last equality, we define

$$B := 1 + \sum_{n=2}^{\infty} \beta(n) = e^{(2\ln 2)\tau} - 4\tau - 1,$$
(C5)

and the channel  $\mathcal{E}_N^{(\mathrm{all})}$ , the physical channel implemented by applying  $\mathcal{E}_N$  with the probability 1/B and  $\mathcal{W}_n (n \geq 2)$  with the probability  $\beta(n)/B$ . Consequently, we obtain

$$\operatorname{Tr}\left(Q\mathcal{U}(\rho_{\mathrm{init}})\right) = B^{N}\operatorname{Tr}\left(\tilde{Q}\left(\mathcal{E}_{N}^{(\mathrm{all})}\right)^{N}\left(\tilde{\rho}_{\mathrm{init}}\right)\right). \tag{C6}$$

We see that there is no systematic error on the right-hand side. For a given number of samples, denoted as  $N_{\text{sample}}$ , the statistical error  $\epsilon_{\text{st}}$  scales as

$$\epsilon_{\rm st} \in \mathcal{O}\left(\frac{B^N}{\sqrt{N_{\rm sample}}}\right).$$
 (C7)

Since  $B^N < e^{(2\ln 2)(\lambda t)^2/N}$ , we get  $N_{\text{sample}} \in \mathcal{O}(1/\epsilon_{\text{st}}^2)$  by setting  $N \in \mathcal{O}\left((\lambda t)^2\right)$ .

We note that even though N is upper-bounded, there is no theoretical upper bound on the number of gates, as the count of swift operators in  $W_n$  is determined by n. Here, n is not bounded and can take on a large value with probability  $\beta(n)/B$ . Conversely, the count of swift operators in the second- or higher-order qSWIFT is upper-bounded by the order parameter, and therefore, the number of gates is also upper-bounded. Thus, in practical situations where the number of operational gates is limited, the second- or higher-order qSWIFT may be more advantageous than the previously introduced all-order qSWIFT.

### Appendix D: Note on the LCU-based randomized approach

The literature [18] provides a higher-order randomized method for phase estimation. The calculation includes the evaluation of  $\text{Tr}\left[\rho e^{iHt}\right]$  with  $H = \sum_{\ell=1}^{L} h_{\ell} H_{\ell}$ , where again we define  $\{H_{\ell}\}_{\ell=1}^{L}$  so that  $h_{\ell} > 0$  and define  $\lambda := \sum_{\ell} h_{\ell}$ . For that, they propose an all-order randomized method for estimating  $\text{Tr}\left[\rho e^{iHt}\right]$  based on the linear combination of the unitary (LCU) approach. In this section, we show that by extending the randomized method, we can construct another all-order randomized method for estimating  $\text{Tr}(Qe^{iHt}\rho e^{-iHt})$ , which is the target of our qSWIFT algorithm.

We begin by reviewing the method given in [18] and discuss how to extend this method to estimate the expectation value of an observable. Then, we discuss the difference between the LCU-based approach and the all-order qSWIFT introduced in Appendix C.

a. The LCU-based randomized approach

To estimate  $\text{Tr}[\rho e^{iHt}]$ , the authors of [18] utilize the expansion

$$e^{iHt/N} = \sum_{m} c_m W_m \,, \tag{D1}$$

where

$$W_m \to (i \text{ sign}(t))^n H_{\ell_1} \dots H_{\ell_n} V_{\ell'}^{(n)}, \quad c_m \to \frac{1}{n!} \left(\frac{\lambda |t|}{N}\right)^n \sqrt{1 + \left(\frac{\lambda t}{N(n+1)}\right)^2} p_{\ell_1} \dots p_{\ell_n} p_{\ell'} > 0,$$
 (D2)

with

$$V_{\ell'}^{(n)} = \exp(\mathrm{i}\theta_n H_{\ell'}), \quad \text{with } \theta_n := \arccos\left(\left[1 + \left(\frac{\lambda t}{N(n+1)}\right)^2\right]^{-1/2}\right).$$
 (D3)

The multi-index m denotes the indices  $(n, \vec{\ell}, \ell')$ . Then

$$e^{iHt} = \sum_{m_1,\dots,m_N} c_{m_1} \dots c_{m_N} W_{m_1} \dots W_{m_N} = C^N \sum_{m_1,\dots,m_N} q_{m_1} \dots q_{m_N} W_{m_1} \dots W_{m_N}, \tag{D4}$$

where  $q_m = c_m/C$  with  $C = \sum_m c_m$ . Since  $q_m > 0$  and  $\sum_m q_m = 1$ ,  $\{q_m\}$  can be interpreted as a probability distribution.

By using the expansion, we obtain

$$\operatorname{Tr}\left[\rho e^{iHt}\right] = C^N \sum_{m_1,\dots,m_N} q_{m_1} \dots q_{m_N} \left(\Re\left[\operatorname{Tr}\left(\rho W_{m_1} \dots W_{m_N}\right)\right] + i\Im\left[\operatorname{Tr}\left(\rho W_{m_1} \dots W_{m_N}\right)\right]\right). \tag{D5}$$

We can estimate the right-hand side, by sampling  $(m_1
ldots m_N)$  according to  $q_{m_1}
ldots q_{m_N}$  and evaluate the real part and the imaginary part of  $\text{Tr}(\rho W_{m_1}
ldots W_{m_N})$  by the Hadamard test repeatedly. There is no systematic error. The statistical error  $\epsilon_{\text{st}}$  scales as

$$\epsilon_{\rm st} \in \mathcal{O}\left(\frac{C^N}{\sqrt{N_{\rm sample}}}\right)$$
(D6)

with  $N_{\text{sample}}$  as the number of sampling the set  $(m_1, \dots m_N)$ . In [18],  $C \in \mathcal{O}\left(\exp\left((\lambda t)^2/N^2\right)\right)$ , i.e.,  $C^N = \mathcal{O}\left(\exp\left((\lambda t)^2/N\right)\right)$  in our notation. Thus, we need  $N = O\left((\lambda t)^2\right)$  so that  $N_{\text{sample}} \in \mathcal{O}\left(1/\epsilon_{\text{st}}^2\right)$ .

# b. Application to the Hamiltonian simulation problem

We can utilize the expansion (D4) to calculate the expectation value after applying the time evolution:

$$\operatorname{Tr}\left(Qe^{iHt}\rho e^{-iHt}\right) = C^{2N} \sum_{m_1' \dots m_N'} \sum_{m_1 \dots m_N} q_{m_1'} \dots q_{m_N'} q_{m_1} \dots q_{m_N} \operatorname{Tr}\left(QW_{m_1'} \dots W_{m_N'} \rho W_{m_1}^{\dagger} \dots W_{m_N}^{\dagger}\right) \tag{D7}$$

$$= C^{2N} \sum_{m'_1 \dots m'_N} \sum_{m_1 \dots m_N} q_{m'_1} \dots q_{m'_N} q_{m_1} \dots q_{m_N} \Re \left[ \text{Tr} \left( Q W_{m'_1} \dots W_{m'_N} \rho W_{m_1}^{\dagger} \dots W_{m_N}^{\dagger} \right) \right], \quad (D8)$$

where we use that the left-hand side is the real value in the second equality. As in the case of (D5), we can estimate the value of (D8), by sampling  $(m_1, \ldots m_N)$  and  $(m'_1, \ldots m'_N)$  and estimating  $\Re[\operatorname{Tr}(QW_{m'_1} \ldots W_{m'_N} \rho W_{m_1}^{\dagger} \ldots W_{m_N}^{\dagger})]$  by the Hadamard test. Again, there is no systematic error, and by setting  $N = O((\lambda t)^2)$ , the number of samples  $N_{\text{sample}}$  scales as  $N_{\text{sample}} \in \mathcal{O}(1/\epsilon_{\text{st}}^2)$ . Therefore, the behavior of both the systematic error and the statistical error with respect to N is the same as that of the all-order qSWIFT introduced in Appendix C.

However, the LCU-based method and our qSWIFT approach have a key distinction: the former expands the unitary operation, while the latter expands the unitary channel. This difference in expansion methodology results in distinct quantum circuits. In the LCU-based approach, the Hadamard test is necessary for calculating the real part of the trace function, requiring the implementation of controlled- $W_m$  operations. For instance, the quantum circuit for evaluating (D8) is depicted in Fig. 6 (we note that the circuit is also used in another higher-order randomization protocol [23]). Given that each  $W_m$  operation involves a rotational operator of the form  $e^{iH_\ell t'}$  (with t' as a real value), a total of 2N controlled- $e^{iH_\ell t'}$  operations are needed for the circuit. Conversely, in the qSWIFT approach, as illustrated in Fig. 2, no controlled- $e^{iH_\ell t'}$  operations are necessary. The only interactions with the ancilla qubit involve swift operators, as all exponential time evolution operators are encapsulated within the qDRIFT channel, which can be implemented without the need for an ancilla qubit.

![](_page_20_Figure_15.jpeg)

FIG. 6. Quantum circuits for evaluating (D8) by the LCU-based approach.

The implementation of the controlled- $e^{iH_\ell t'}$  operation requires additional controlled gates in the LCU-based methods compared to the implementation of  $e^{iH_\ell t'}$  operation. In particular, in the simulation where one body term is dominant, the LCU-based method needs many more controlled gates than in qSWIFT. To demonstrate this, let us consider the following Hamiltonian, written as the summation of the multi-body terms (the first summation) and the one-body terms (the second summation):

$$H = \frac{J}{h'_{\text{sum}} n} \sum_{\ell=1}^{L'} h'_{\ell} P_{\ell} + \frac{h}{c_{\text{sum}}} \sum_{j=1}^{n} \sum_{k=x,y,z} c_j^k \sigma_j^k.$$
 (D9)

The first summation corresponds to L' multi-body terms, where  $P_{\ell}$  is the tensor product of the Pauli operators that act non-trivially on multiple qubits, with  $h'_{\ell}$  as a real coefficient,  $h'_{\text{sum}} := \sum_{\ell} |h'_{\ell}|$ , and J is a positive value. The second summation corresponds to 3n one-body terms, with n as the number of qubits,  $\sigma^k_j$  as one of the Pauli operators acting on the j-th qubit,  $c^k_j$  and  $h'_{\ell}$  as real coefficients,  $c_{\text{sum}} = \sum_{j=1}^b \sum_{k=x,y,z} |c^k_j|$  and h as a positive value. We assume the case where one-body term is dominant in the sense that  $J \ll h$ . The sum of all absolute values of the coefficients is given as  $\lambda = J/n + h$ .

Our objective of the simulation is approximately computing  $\operatorname{Tr}\left(Qe^{\mathrm{i}Ht}\rho e^{-\mathrm{i}Ht}\right)$  using directly implementable time evolutions:  $e^{iP_\ell t'}$  and  $e^{i\sigma_j^k t'}$ . Note that the collective neutrino oscillation problem is an example of the Hamiltonian simulation where the one body term is dominant and has been already discussed in [24]. On the one hand, in the LCU-based approach, the required number of controlled time evolution gates is  $O((\lambda t)^2)$ , and since each controlled time evolution requires at least one controlled gate, the total number of controlled gates is also  $O((\lambda t)^2)$ . On the other hand, the number of time evolution gates is also  $O((\lambda t)^2)$  in the all-order qSWIFT. However, most of the time evolution gates sampled are  $e^{i\sigma_j^k t'}$ , which do not need the controlled gate; the number of  $e^{iP_\ell t'}$  sampled is  $O(J/(\lambda n))$  on average. Since each  $e^{iP_\ell t'}$  requires at most O(n) controlled gates, the total number of controlled gates in qSWIFT is at most

$$\mathcal{O}\left((\lambda t)^2 \times \frac{J}{\lambda n} \times n\right) \sim \mathcal{O}\left((\lambda t)^2 \times \frac{J}{h}\right),$$
 (D10)

where to show the expression on the right-hand side, we use  $\lambda \sim h$  since  $J \ll h$ . Therefore, for the simulation with the Hamiltonian (D9), qSWIFT achieves a significant reduction of the CNOT gates by the factor J/h.

- [1] M. Suzuki, Fractal decomposition of exponential operators with applications to many-body theories and monte carlo simulations, Phys. lett. A **146**, 319 (1990).
- [2] D. W. Berry, G. Ahokas, R. Cleve, and B. C. Sanders, Efficient quantum algorithms for simulating sparse Hamiltonians, Commun. Math. Phys. 270, 359 (2007).
- [3] A. M. Childs, Y. Su, M. C. Tran, N. Wiebe, and S. Zhu, Theory of Trotter error with commutator scaling, Phys. Rev. X 11, 011020 (2021).
- [4] A. M. Childs, A. Ostrander, and Y. Su, Faster quantum simulation by randomization, Quantum 3, 182 (2019).
- [5] E. Campbell, Random compiler for fast Hamiltonian simulation, Phys. Rev. Lett. 123, 070503 (2019).
- [6] D. W. Berry and A. M. Childs, Black-box Hamiltonian simulation and unitary implementation Quantum Inf. Comput. 12, 29 (2012).
- [7] D. W. Berry, A. M. Childs, R. Cleve, R. Kothari, and R. D. Somma, Simulating Hamiltonian dynamics with a truncated taylor series, Phys. Rev. Lett. 114, 090502 (2015).
- [8] D. W. Berry, A. M. Childs, and R. Kothari, Hamiltonian simulation with nearly optimal dependence on all parameters, in 2015 IEEE 56th Annual Symposium on Foundations of Computer Science (IEEE, 2015) pp. 792–809.
- [9] G. H. Low and I. L. Chuang, Optimal Hamiltonian simulation by quantum signal processing Phys. Rev. Lett. 118, 010501 (2017).
- [10] G. H. Low and I. L. Chuang, Hamiltonian Simulation by Qubitization, Quantum 3, 163 (2019).
- [11] A. Gilvén. Υ. Su. H. N. Wiebe. Low. and Quantum singular value transformation Exponential for quantum and beyond: improvements matrix arithmetics. Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, STOC 2019 Computing Machinery, New York, USA, 2019) pp. 193—-204.
- [12] A. M. Childs, D. Maslov, Y. Nam, N. J. Ross, and Y. Su, Toward the first quantum simulation with quantum speedup, Proc. Natl. Acad. Sci 115, 9456 (2018).
- [13] K. R. Brown, R. J. Clark, and I. L. Chuang, Limitations of quantum simulation examined by simulating a pairing Hamiltonian using nuclear magnetic resonance, Phys. Rev. Lett. 97, 050504 (2006).
- [14] B. P. Lanyon, C. Hempel, D. Nigg, M. Müller, R. Gerritsma, F. Zähringer, P. Schindler, J. T. Barreiro, M. Rambach, G. Kirchmair, M. Hennrich, P. Zoller, R. Blatt, and C. F. Roos, Universal digital quantum simulation with trapped ions, Science 334, 57 (2011).
- [15] R. Barends, L. Lamata, J. Kelly, L. García-Álvarez, A. G. Fowler, A. Megrant, E. Jeffrey, T. C. White, D. Sank, J. Y. Mutus, et al., Digital quantum simulation of fermionic models with a superconducting circuit, Nat. commun. 6, 1 (2015).
- [16] A. M. Childs, A. Ostrander, and Y. Su, Faster quantum simulation by randomization, Quantum 3, 182 (2019).
- [17] A. M. Childs, D. Maslov, Y. Nam, N. J. Ross, and Y. Su, Toward the first quantum simulation with quantum speedup, Proceedings of the National Academy of Sciences 115, 9456 (2018).
- [18] K. Wan, M. Berta, and E. T. Campbell, Randomized quantum algorithm for statistical phase estimation, Physical Review Letters 129, 030503 (2022).
- [19] J. R. McClean, N. C. Rubin, K. J. Sung, I. D. Kivlichan, X. Bonet-Monroig, Y. Cao, C. Dai, E. S. Fried, C. Gidney, B. Gimby, et al., Openfermion: the electronic structure package for quantum computers, Quantum Sci. Technol. 5, 034014 (2020).
- [20] S. B. Bravyi and A. Y. Kitaev, Fermionic quantum computation, Ann. Physics 298, 210 (2002).

- [21] Y. Suzuki, Y. Kawase, Y. Masumura, Y. Hiraga, M. Nakadai, J. Chen, K. M. Nakanishi, K. Mitarai, R. Imai, S. Tamiya, et al., Qulacs: a fast and versatile quantum circuit simulator for research purpose, Quantum 5, 559 (2021).
- [22] J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean, N. Wiebe, and R. Babbush, Even more efficient quantum computations of chemistry through tensor hypercontraction, PRX Quantum 2, 030305 (2021).
- [23] P. K. Faehrmann, M. Steudtner, R. Kueng, M. Kieferova, and J. Eisert, Randomizing multi-product formulas for hamiltonian simulation, Quantum 6, 806 (2022).
- [24] A. Rajput, A. Roggero, and N. Wiebe, Hybridized methods for quantum simulation in the interaction picture, Quantum 6, 780 (2022).