Simple group
%
No nontrivial normal subgroups
%
definition
---

Sylow Theorems
%
Write $\abs{G} = p^n m$ with $(p, m) = 1$.

# Sylow 1

Writing $\abs{G} = \prod p_i^{n_i}$, there exist Sylow $p_i\dash$subgroups $P_i$ of order $p_i^{n_i}$ for every $i$.

## Sylow 2

All Sylows are conjugate.

# Sylow 3

1. $n_p$ divides $m$
1. $n_p \equiv 1 \mod p$
2. $n_p = [G: N_G(P)]$
%
theorem
---

Recognizing Direct Products
%
When there exist two subgroups $H, K \leq G$ such that

1. $H\intersect K = \emptyset$
2. $G = HK$
3. $H$ and $K$ are both normal.
%
theorem
---

Solvable Group
%
A group is **solvable** iff it has a composition series with *abelian* composition factors.
%
definition
---

Composition Series
%
A **composition series** of $G$ is a sequence of subgroups
\begin{align*}
1=N_{0} \leq N_{1} \leq N_{2} \leq \cdots \leq N_{k-1} \leq N_{k}=G
\end{align*}
such that $N_i \normal N_{i+1}$ and the *composition factors* $N_{i+1}/N_i$ are simple.
%
definition
---

Alternating Group
%
The kernel of the sign homomorphism, i.e. the set of even permutations (sign = 1).
%
definition
---

Even vs Odd Permutations
%
- Even: $\eps(\sigma) = 1$, product of even number of transpositions.
- Odd: $\eps(\sigma) = -1$, product of *odd* number of transpositions.
%
definition
---

How to determine sign of a permutation
%
A cycle is odd iff it has an odd number of odd cycles (i.e. *even* number of elements in cycle).i
%
definition
---

What is the sign of the cycle $\sigma=(123456)(789)(10~11)(12~13~14~15)(16~17~18)$?
%
$\eps(\sigma) = -1$, since it has 3 (an odd number) cycles of odd cycles (even length).
%
problem
---

Burnside's Formula
%
$\abs{G} \abs{X/G} = \sum \abs{X^g}$ where $X/G$ is the set of orbits and $X^g = \theset{x\in X \suchthat g.x = x}$ are the fixed points of $g$.
%
formula
---

Stabilizer
%
A subgroup: $G_x = \theset{g\in G \suchthat g.x = x}$.
%
definition, notation
---

$G_x$
%
The Stabilizer subgroup: $G_x = \theset{g\in G \suchthat g.x = x} \leq G$.
%
definition, notation
---

$X^n$
%
$X^g = \theset{x\in X \suchthat g.x = x} \subseteq X$
%
definition, notation
---

Class Equation
%
$\abs{G} = \abs{Z(G)} + \sum_{i} [G: C_G(x_i)]$
%
definition, notation
---

$p\dash$group
%
A group of order $p^n$ for some $n\geq 1$.
%
definition
---

Lagrange's Theorem
%
Any $H\leq G$ has size dividing $\abs{G}$.
%
theorem
---

Fermat's Little Theorem
%
$a^p \cong a \mod p$, and if $p$ does not divide $a$, $a^{p-1} \cong 1 \mod p$.
%
theorem
---

Euler's Theorem
%
$a^{\phi(n)} \cong 1 \mod n$.
%
theorem
---

$\phi(p^k) = ?$
%
$\phi(p^k) = p^{k-1}(p-1) = p^k \qty{1 - {1\over p}}$
%
formula
---

Definition: Transitive Group Action
%
A group action $G\actson X$ is *transitive* iff for every pair $x, y\in X$ there exists a $g\in G$ such that $g.x = y$.
%
definition
---

