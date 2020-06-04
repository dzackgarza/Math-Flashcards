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
A cycle is odd iff it has an odd number of even cycles (i.e. odd number of elements in cycle).
%
definition
---



