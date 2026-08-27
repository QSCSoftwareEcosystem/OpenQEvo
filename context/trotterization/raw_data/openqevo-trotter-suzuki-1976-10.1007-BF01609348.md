![](_page_0_Picture_1.jpeg)

# Generalized Trotter's Formula and Systematic Approximants of Exponential Operators and Inner Derivations with Applications to Many-Body Problems

Masuo Suzuki

Department of Physics, University of Tokyo, Hongo, Bunkyo-ku, Tokyo, Japan

**Abstract.** New systematic approximants are proposed for exponential functions, operators and inner derivation  $\delta_H$ . Remainders of systematic approximants are evaluated explicitly, which give degrees of convergence of approximants. The first approximant corresponds to Trotter's formula [1]:  $\exp(A+B) = \lim_{n\to\infty} [\exp(A/n) \exp(B/n)]^n$ . Some applications to physics are also discussed.

### 1. Introduction

In this paper, we investigate systematic approximants and errors of exponential operators such as  $e^A$ ,  $e^{A+B}$  etc. and exponential inner derivations such as  $\exp \delta_H$ ,  $\exp(\delta_{H_1} + \delta_{H_2})$  etc. These exponential operators and inner derivations are used very frequently in many-body problems. As it is mostly difficult to diagonalize such exponential operators, it is convenient to find appropriate systematic approximants of them which can be easily evaluated. In Section 2, systematic approximants of  $e^x$  are discussed for illustrating our idea. In Section 3, systematic approximants of exponential operators are introduced and studied in detail. Some applications are listed in Section 4.

### 2. Systematic Approximants of an Exponential Function

In this section we present our idea in a simple exponential function  $e^x$ . As is well-known, this is expressed by

$$e^x = \lim_{n \to \infty} (1 + x/n)^n,$$
 (2.1a)

or

$$e^{x} = 1 + x + x^{2}/2! + x^{3}/3! + \dots + x^{m}/m! + \dots$$
 (2.1b)

The above two formulae give methods to calculate  $e^x$  numerically. The second expression (2.1b) is more convenient for such a purpose, because the convergence of (2.1b) is better than that of (2.1a).

Is there a much more rapidly convergent expression for  $e^x$ ? To answer this question, we try to unify or combine the above two formulae as follows:

$$e^{x} = \lim_{n \to \infty} e_{n,m}(x) = \lim_{m \to \infty} e_{n,m}(x),$$
 (2.2)

where

$$e_{n,m}(x) = \left[ \sum_{k=0}^{m} \frac{1}{k!} \left( \frac{x}{n} \right)^{k} \right]^{n}. \tag{2.3}$$

The case m=1 corresponds to (2.1a) and n=1 to (2.1b). It is easy to evaluate (the upper bound of) the remainder  $S_{n,m}(x)$  defined by

$$e^x = e_{n,m}(x) + S_{n,m}(x)$$
. (2.4)

In fact, using the generalized mean value theorem or Taylor's theorem, we obtain the following result:

**Theorem 1.** With (2.3), we have

$$|e^{x} - e_{n,m}(x)| \le \frac{|x|^{m+1}}{n^{m}(m+1)!} e^{|x|}. \tag{2.5}$$

*Proof.* The proof is the same as Theorem 2 for general case.

It is easily seen from this theorem that the error  $S_{n,m}(x)$  becomes extremely small for large n and m. The convergence of  $e_{n,m}(x)$  with respect to the series m (or n) for a large fixed n (or m) is much better even than (2.1b). Consequently the above formula (2.3) will be very useful in calculating  $e^x$  (and other elementary functions derived from it) by a high speed computer, in which the operation of product is much reduced if  $n=2^p$  (where p is an integer). Thus, we may call  $e_{n,m}(x)$  the n-m approximant of  $e^x$ .

# 3. Systematic Approximants of Exponential Operators and the Generalized Trotter's Formula

(i) We first discuss a simple exponential operator  $e^A$ . Similarly to (2.3), we define the n-m approximant of  $e^A$  by

$$f_{n,m}(A) = \left[ \sum_{k=0}^{m} \frac{1}{k!} \left( \frac{A}{n} \right)^{k} \right]^{n}. \tag{3.1}$$

We obtain easily the following theorem concerning the convergence and error estimation:

**Theorem 2.** For any operator A in a Banach algebra,

$$||e^{A} - f_{n,m}(A)|| \le \frac{1}{n^{m}(m+1)!} ||A||^{m+1} e^{||A||},$$
(3.2)

and  $f_{n,m}(A)$  converges to  $e^A$ :

$$\lim_{n \to \infty} f_{n,m}(A) = \lim_{m \to \infty} f_{n,m}(A) = e^A$$
 (3.3)

for a bounded operator A.

Using the properties of a norm in a Banach algebra, we can easily prove Theorem 2 as follows:

$$||e^{A} - f_{n,m}(A)|| \le ||e^{A/n} - h|| \cdot ||(e^{A/n})^{n-1} + (e^{A/n})^{n-2}h + \dots + h^{n-1}||$$

$$\le n ||\exp(A/n) - h|| \exp\left[\frac{n-1}{n} ||A||\right], \tag{3.4}$$

with

$$h = \sum_{k=0}^{m} \frac{1}{k!} (A/n)^k.$$
 (3.5)

Next, the Taylor's theorem yields

$$\|\exp(A/n) - h\| = \left\| \sum_{k=m+1}^{\infty} \frac{1}{k!} (A/n)^{k} \right\|$$

$$\leq \sum_{k=m+1}^{\infty} \frac{1}{k!} (\|A\|/n)^{k} = \exp(\|A\|/n) - \sum_{k=0}^{m} \frac{1}{k!} (\|A\|/n)^{k}$$

$$= \frac{1}{(m+1)!} (\|A\|/n)^{m+1} \exp(\theta \|A\|/n); \quad 0 < \theta < 1.$$
(3.6)

Substituting (3.6) into (3.4), we get Theorem 2.

(ii) Next we study here systematic approximants of a non-commutative exponential operator such as  $e^{A+B}$ . It is convenient to introduce the following approximant

$$f_{n,1}(\{A_j\}) = \{e^{A_1/n} e^{A_2/n} \dots e^{A_p/n}\}^n.$$
(3.7)

We have the following theorem.

**Theorem 3.** For any operators  $\{A_j\}$  in a Banach algebra,

$$\left\| \exp\left(\sum_{j=1}^{p} A_{j}\right) - f_{n,1}(\{A_{j}\}) \right\| \leq \frac{2}{n} \left(\sum_{j=1}^{p} \|A_{j}\|\right)^{2} \exp\left(\frac{n+2}{n} \sum_{j=1}^{p} \|A_{j}\|\right)$$
(3.8)

with an arbitrary positive integer p. For bounded operators  $\{A_j\}$ ,

$$\lim_{n \to \infty} f_{n,1}(\{A_j\}) = \exp\left(\sum_{j=1}^p A_j\right). \tag{3.9}$$

**Corollary 1.** For p=2, Eq. (3.9) is reduced to the following Trotter's formula:

$$e^{A+B} = \lim_{n \to \infty} \left( e^{A/n} e^{B/n} \right)^n \tag{3.10}$$

for bounded operators A and B.

The above formula (3.9) and (3.10) have been used in statistical mechanics  $[2 \sim 5]$ .

Proof of Theorem 3. If we put

$$g = \exp\left(\frac{1}{n} \sum_{j=1}^{p} A_j\right) \text{ and } h = e^{A_1/n} \dots e^{A_p/n},$$
 (3.11)

then we obtain

$$P = \left\| \exp\left(\sum_{j=1}^{p} A_{j}\right) - f_{n,1}(\{A_{j}\}) \right\| = \|g^{n} - h^{n}\|$$

$$\leq \|g - h\| \left(\|g\|^{n-1} + \|g\|^{n-2} \|h\| + \dots + \|h\|^{n-1}\right)$$

$$\leq n\|g - h\| \exp\left(\frac{n-1}{n} \sum_{j=1}^{p} \|A_{j}\|\right), \tag{3.12}$$

where we have used the following lemma:

**Lemma 1.** For any operators a and b in a Banach algebra,

$$||a^{n}-b^{n}|| = ||a^{n-1}(a-b)+a^{n-2}(a-b)b+...+(a-b)b^{n-1}||$$

$$\leq ||a-b|| (||a||^{n-1}+||a||^{n-2}||b||+...+||b||^{n-1})$$

$$\leq n||a-b|| \{\max(||a||,||b||)\}^{n-1}.$$
(3.13)

Then we get

$$||g-h|| \le ||h|| \cdot ||gh^{-1} - 1||$$

$$\le ||h|| \left\{ \exp\left(\frac{2}{n} \sum_{j=1}^{p} ||A_{j}||\right) - \left(1 + \frac{2}{n} \sum_{j=1}^{p} ||A_{j}||\right) \right\}$$

$$\le ||h|| \cdot \frac{2}{n^{2}} \left( \sum_{j=1}^{p} ||A_{j}||\right)^{2} \exp\left(\frac{2}{n} \sum_{j=1}^{p} ||A_{j}||\right), \tag{3.14}$$

where we have used Theorem 1. From (3.12) and (3.14), we arrive finally at Theorem 3.

Next we introduce the following systematic n-m approximant  $f_{n,m}(A, B)$ :

$$f_{n,m}(A,B) = (e^{A/n}e^{B/n}e^{C_2/n^2}...e^{n^{-m}C_m})^n,$$
(3.15)

where  $\{C_n\}$  are defined recursively as

$$C_2 = \frac{1}{2} \left[ \frac{\partial^2}{\partial \lambda^2} \left( e^{-\lambda B} e^{-\lambda A} e^{\lambda (A+B)} \right) \right]_{\lambda=0} = \frac{1}{2} [B, A], \tag{3.16}$$

$$C_3 = \frac{1}{3!} \left[ \frac{\partial^3}{\partial \lambda^3} (e^{-\lambda^2 C_2} e^{-\lambda B} e^{-\lambda A} e^{\lambda (A+B)}) \right]_{\lambda=0} = \frac{1}{6} [C_2, A+2B], \tag{3.17}$$

and in general

$$C_n = \frac{1}{n!} \left[ \frac{\partial^n}{\partial \lambda^n} \left( e^{-\lambda^{n-1} C_{n-1}} \dots e^{-\lambda^2 C_2} e^{-\lambda B} e^{-\lambda A} e^{\lambda (A+B)} \right) \right]_{\lambda=0}. \tag{3.18}$$

The coefficient  $C_n$  is a polynomial of order n (of operators A and B), which appears in the Zassenhaus formula [6]:

$$e^{\lambda(A+B)} = e^{\lambda A} e^{\lambda B} e^{\lambda^2 C_2} e^{\lambda^3 C_3} \dots$$
 (3.19)

For this series of approximants,  $f_{n,m}(A, B)$ , the following theorem holds.

**Theorem 4.** For any operators A and B in a Banach algebra,

$$\left\| e^{A+B} - f_{n,m}(A,B) \right\| \le \frac{c_{n,m}}{n^m(m+1)!} e^{\|A\| + \|B\|}, \tag{3.20}$$

where  $c_{n,m}$  is defined by (3.31) and satisfies the following property

$$0 \le \lim_{n \to \infty} c_{n,m} < \infty . \tag{3.21}$$

For bounded operators A and B,

$$\lim_{n \to \infty} f_{n,m}(A, B) = \exp(A + B). \tag{3.22}$$

*Proof.* For the proof, it is convenient to introduce the following *projection operator*  $\mathscr{P}_m$ :

$$\mathcal{P}_{m}(f(\lambda)) = \mathcal{P}_{m}\left(\sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!} f^{(k)}(0)\right)$$

$$= \sum_{k=m+1}^{\infty} \frac{\lambda^{k}}{k!} f^{(k)}(0) = f(\lambda) - \sum_{k=0}^{m} \frac{\lambda^{k}}{k!} f^{(k)}(0), \qquad (3.23)$$

for any operator or scalar function  $f(\lambda)$ . Namely,  $\mathcal{P}_m$  means to eliminate all the terms of order lower than  $\lambda^{m+1}$ . Now we have

$$P = \|e^{A+B} - f_{n,m}(A, B)\| = \|g^n - h^n\|$$

$$\leq \|g - h\| \times n\{\max(\|g\|, \|h\|)\}^{n-1},$$
(3.24)

where

$$g = \exp\left[\frac{1}{n}(A+B)\right]$$
 and  $h = [f_{n,m}(A,B)]^{\frac{1}{n}}$ . (3.25)

Then, using the projection operator  $\mathcal{P}_m$ , and the definitions (3.16)  $\sim$  (3.18) of  $\{C_n\}$ , we obtain

$$||g-h|| \le ||g|| \cdot ||g^{-1}h - 1|| \le ||g|| \cdot ||\mathscr{P}_{m}(g^{-1}h)||$$

$$\le ||g|| \mathscr{P}_{m}\left(\exp\left[\frac{2}{n}(||A|| + ||B||) + \frac{||C_{2}||}{n^{2}} + \dots + \frac{||C_{m}||}{n^{m}}\right]\right)$$
(3.26)

Thus, we arrive at the following inequality

$$P \leq n \|g\| \left[ \max(\|g\|, \|h\|) \right]^{n-1} f_m\left(\frac{1}{n}\right), \tag{3.27}$$

where

$$f_m(\lambda) \equiv \mathcal{P}_m(\exp[2\lambda(\|A\| + \|B\|) + \lambda^2 \|C_2\| + \dots + \lambda^m \|C_m\|]). \tag{3.28}$$

From the generalized mean value theorem and from the property that  $f_m(0) = f_m^{(1)}(0) = \dots = f_m^{(m)}(0) = 0$ , we obtain

$$f_m(\lambda) = \frac{\lambda^{m+1}}{(m+1)!} f_m^{(m+1)}(\theta \lambda) \le \frac{\lambda^{m+1}}{(m+1)!} f_m^{(m+1)}(\lambda)$$
(3.29)

with  $0 < \theta < 1$  and  $\lambda \ge 0$ . Consequently, P is bounded as

$$P \leq \frac{\|g\|}{n^{m}(m+1)!} \left[ \max(\|g\|, \|h\|) \right]^{n-1} f_{m}^{(m+1)} \left( \frac{1}{n} \right)$$

$$\leq \frac{c_{n,m}}{n^{m}(m+1)!} \exp(\|A\| + \|B\|), \tag{3.30}$$

where the coefficients  $\{c_{n,m}\}$  are given by

$$c_{n,m} = f_m^{(m+1)} \left(\frac{1}{n}\right) \exp\left(\sum_{k=2}^m \frac{1}{n^{k-1}} \|C_k\|\right), \tag{3.31}$$

and they satisfy the property (3.21), because all  $\{C_k\}$  are bounded and

$$\lim_{n \to \infty} c_{n,m} = f_m^{(m+1)}(0) = \text{finite}$$
(3.32)

for bounded operators A and B.

The above result can be easily extended to a more general exponential operator  $\exp(A_1 + A_2 + A_3... + A_p)$ . We first define a sequence  $\{C_k\}$  by

$$C_{2} = \frac{1}{2} \left[ \frac{\partial^{2}}{\partial \lambda^{2}} (e^{-\lambda A_{p}} \dots e^{-\lambda A_{1}} e^{\lambda (A_{1} + \dots + A_{p})}) \right]_{\lambda = 0}$$

$$= -\frac{1}{2} \{ [A_{1}, A_{2} + \dots + A_{p}] + [A_{2}, A_{3} + \dots + A_{p}] + \dots + [A_{p-1}, A_{p}] \}, \quad (3.33)$$

and in general  $C_n$  is determined recursively by

$$C_{n} = \frac{1}{n!} \left[ \frac{\partial^{n}}{\partial \lambda^{n}} (e^{-\lambda^{n-1}C_{n-1}} ... e^{-\lambda^{2}C_{2}} e^{-\lambda A_{p}} ... e^{-\lambda A_{1}} e^{\lambda(A_{1} + ... + A_{p})}) \right]_{\lambda = 0}$$
(3.34)

It should be noted that these coefficients are also determined *formally* by the following generalized Zassenhaus formula:

$$\exp\left(\lambda \sum_{j=1}^{p} A_{j}\right) = e^{\lambda A_{1}} e^{\lambda A_{2}} \dots e^{\lambda A_{p}} e^{\lambda^{2} C_{2}} e^{\lambda^{3} C_{3}} \dots$$

$$(3.35)$$

With these preparations, we obtain the following theorem.

**Theorem 5.** For any operator  $\{A_i\}$  in a Banach algebra

$$\left\| \exp\left(\sum_{j=1}^{p} A_{j}\right) - f_{n,m}(\{A_{j}\}) \right\| \le \frac{c_{n,m}}{n^{m}(m+1)!} \exp\left(\sum_{j=1}^{p} \|A_{j}\|\right), \tag{3.36}$$

where  $f_{n,m}$  denotes the n-m approximant defined by

$$f_{n,m}(\{A_j\}) = (e^{A_1/n}e^{A_2/n}\dots e^{A_p/n}e^{C_2/n^2}\dots e^{n^{-m}C_m})^n,$$
(3.37)

and  $c_{n,m}$  is given by (3.31) with  $f_m(\lambda)$  defined by

$$f_m(\lambda) = \mathcal{P}_m \left( \exp \left[ 2\lambda \sum_{j=1}^p \|A_j\| + \lambda^2 \|C_2\| + \dots + \lambda^m \|C_m\| \right] \right)$$
 (3.38)

instead of (3.28). For bounded operators  $\{A_i\}$ ,

$$\lim_{n \to \infty} f_{n,m}(\{A_j\}) = \exp\left(\sum_{j=1}^{p} A_j\right). \tag{3.39}$$

As a simple example, we consider the case that [A, B] commutes with A and B. Then, we have  $C_3 = C_4 \dots \equiv 0$ , and consequently

$$e^{A+B} = e^A e^B e^{\frac{1}{2}[B,A]} \tag{3.40}$$

as is well-known. Therefore, we get

$$e^{A+B} = f_{n,1}(A, B) \exp\left(\frac{1}{2n}[B, A]\right),$$
 (3.41)

or

$$||e^{A+B} - f_{n,1}(A, B)|| \le (e^{||[A,B]||/(2n)} - 1) \exp(||A|| + ||B||). \tag{3.42}$$

All the above results are easily extended to the inner derivation  $\delta_H$  (i.e.,  $\delta_H(A) = [H, A]$ ). In particular it should be noted here that the inner derivations  $\{\delta_{H_j}\}$  satisfy the following formula

$$(\exp \delta_{H_1} \exp \delta_{H_2} ... \exp \delta_{H_m})^n (A) = (e^{H_1} ... e^{H_m})^n A (e^{-H_m} ... e^{-H_1})^n, \tag{3.43}$$

as is easily proven from the well-known formula [7]

$$(\exp \delta_H)(A) = e^H A e^{-H}. \tag{3.44}$$

All the formulae derived in this section are applicable to strongly interacting systems, for example, models for phase transition, in which two competing interactions play equally important roles and consequently neither of them can be treated as a perturbation.

## 4. Applications and Concluding Remarks

The theorems derived in the preceding sections, particularly (3.9), (3.10) and the corresponding formula on  $\delta_H$  are very useful for studying the following problems:

1. It is possible to prove that the ground state of the *d*-dimensional quantal spin system described by

$$\mathcal{H} = -\sum_{ij} J_{ij} \sigma_i^z \sigma_j^z - \Gamma \sum_j \sigma_j^x \tag{4.1}$$

is equivalent to the (d+1)-dimensional Ising model [5, 8].

- 2. The partition function of a quantal spin system in d dimensions is expressed by that of the Ising model with many-spin interaction in (d+1) dimensions.
- 3. The above fact makes it possible to perform the Monte Carlo calculation of quantal spin systems such as the Heisenberg model [9].
- 4. One can prove the existence of the thermodynamic limit of non-equilibrium quantum mechanical systems [10].

5. It is possible to calculate approximately thermodynamic properties of some quantal spin systems with the use of the n-m approximants introduced in in the present paper. Detailed analyses will be published elsewhere.

Acknowledgement. The author would like to thank Professor R. Kubo for useful suggestions and also thank Professor H. Araki for critical comments.

### References

- 1. Trotter, H.F.: Proc. Amer. Math. Soc. 10, 545 (1959)
- 2. Ginibre, J.: In lectures given at the Cargese Summer School in Statistical Mechanics, July 1969
- 3. Asano, T.: J. Phys. Soc. Japan 29, 350 (1970)
- 4. Suzuki, M., Fisher, M.E.: J. math. Phys. 12, 235 (1971)
- 5. Suzuki, M.: Prog. Theor. Phys. 56, No. 5 (1976)
- Magnus, W.: Commun. Pure Appl. Math. 7, 649 (1954)
   Wilcox, R. M.: J. math. Phys. 8, 962 (1967)
- 7. Kubo, R.: J. Phys. Soc. Japan 12, 570 (1957)
- 8. Suzuki, M.: Prog. Theor. Phys. 46, 1337 (1971)
- 9. Suzuki, M., Miyashita, S., Kuroda, A.: In preparation
- Suzuki, M.: Prog. Theor. Phys. 53, 1657 (1975); J. Stat. Phys. 14, 129 (1976); Prog. Theor. Phys. (submitted)

Communicated by H. Araki

Received May 24, 1976; in revised form August 2, 1976