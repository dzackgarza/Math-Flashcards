Fatou's Lemma
%
If $\theset{f_n} \subset L^+$, then $$\int \liminf f_n \leq \liminf \int f_n$$
%
theorem
---

Egorov's Theorem
%
?
%
theorem
---

Riesz Representation Theorem
%
?
%
theorem
---

Borel set
%
?
%
definition
---

Dominated Convergence Theorem
%
If $\theset{f_n} \subset L^1$ and $f_n\to f$ a.e. with $\abs{f_n} \leq g \in L^1$ for every $n$, then
$$\lim \int f_n = \int \lim f_n$$
%
theorem
---

Monotone Convergence Theorem
If $f_n \in L^+$ and $f_n\nearrow f$ a.e. then
$$
\lim \ing f_n = \int \lim f_n
$$
%
theorem
---

(Lebesgue) Measurable Function
%
?
%
definition
---

Equivalent Characterizations of Completeness
%
?
%
definition
---

Bernoulli's Inequality
%
?
%
formula
---

Uniform Continuity
%
?
%
definition
---

Proof of Borel-Cantelli Lemma
%
*Proof of Borel Cantelli:*
 
- If $E = \limsup_j E_j$ with $\sum m(E_j) < \infty$ then $m(E) = 0$.
- If $E_j$ are measurable, then $\limsup_j E_j$ is measurable.
- If $\sum_j m(E_j) < \infty$, then $\sum_{j=N}^\infty m(E_j) \converges{N\to\infty}\to 0$ as the tail of a convergent sequence.
- $E = \limsup_j E_j = \intersect_{k=1}^\infty \union_{j=k}^\infty E_j \implies E \subseteq \union_{j=k}^\infty$ for all $k$
- $E \subset \union_{j=k}^\infty \implies m(E) \leq \sum_{j=k}^\infty m(E_j) \converges{k\to\infty}\to 0$.
%
proof
---

Baire Space
%
Countable intersections of open dense sets are still dense
%
definition
---

Limsup/Liminf of Sets
%
\begin{align*}
\limsup_n A_n \definedas \intersect_n \union_{j\geq n} A_j&= \theset{x \suchthat x\in A_n \text{ for inf. many $n$}}  \\
\liminf_n A_n \definedas \union_n \intersect_{j\geq n} A_j &= \theset{x \suchthat x\in A_n \text{ for all except fin. many $n$}}  \\
.\end{align*}
%
definition
---

Arzela-Ascoli Theorem
%
A sequence of functions $\theset{f_n}$ has a uniformly convergent subsequence $\iff$ it is uniformly bounded and uniformly equicontinuous.
%
theorem
---

Holder's Inequality
%
?
%
formula
---

Young's Inequality
%
?
%
formula
---

Baire Space
%
If $\theset{U_n}$ is dense in $X$ then the intersection $\intersect U_n$ is again dense.
%
definition
---

First and Second Category
%

- A subset is *first category* iff it is an (arbitrary) union of nowhere dense sets
- A subset is *second category* otherwise.
%
definition
---

Nowhere Dense
%
A set is **nowhere dense** if its closure has empty interior, equivalently it is not dense in *any* nonempty open set.

Intuition: elements are not tightly clustered.

Counterexample: $\theset{1 \over n}, \ZZ$ are nowhere dense, $\QQ, \ZZ\union \qty{(a, b)\intersect \QQ}$ is *not* nowhere dense
%
definition, example, counterexample
---

