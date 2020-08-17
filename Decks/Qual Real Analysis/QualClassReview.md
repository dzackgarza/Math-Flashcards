Equivalent Characterizations of Completeness
%

- Every Cauchy sequence converges
- Every absolutely convergent series converges
%
definition
---

Arzela-Ascoli Theorem
%
A sequence of functions \(\theset{f_n}\) has a uniformly convergent subsequence \(\iff \theset{f_n}\) is uniformly bounded and uniformly equicontinuous.
%
theorem
---

Minkowski's Inequality
%
For $1 \leq p < \infty$,
\[
\norm{f + g}_p \leq \norm{f}_p + \norm{g}_p
.\]
%
theorem
---


Young's Inequality
%
For \(1\leq p, q\leq r \leq \infty  \) with \({1\over p} + {1\over q} - {1\over r} = 1  \), then  \(\norm{f\ast g}_r \leq \norm{f}_p \norm{g}_q \) 

Useful cases:
\[\begin{align*}
\norm{f\ast g}_1 & \leq \norm{f}_1 \norm{g}_1 \\
\norm{f\ast g}_p & \leq \norm{f}_1 \norm{g}_p \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2 
\end{align*}\]


%
formula
---

Baire Space
%
$X$ is a Baire space iff whenever \( \theset{U_n}\) is a *countable* collection of open dense subsets of $X$, then their intersection $\intersect U_n$ is again dense.
%
definition
---


First and Second Category
%

- A subset is *first category* iff it is countable union of nowhere dense sets.
- A subset is *second category* otherwise.
%
definition
---

Nowhere Dense
%
A set is $A$ **nowhere dense** if its closure has empty interior $\qty{\bar A}^\circ$, equivalently it is not dense in *any* nonempty open set.
For $\RR$, every interval $I$ contains a subinterval $S\subset I$ with $S\intersect A = \emptyset$, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.

Counterexample: $\theset{1 \over n}, \ZZ$ are nowhere dense, $\QQ, \ZZ\union \qty{(a, b)\intersect \QQ}$ is *not* nowhere dense
%
definition, example, counterexample
---

Equicontinuous
%
For $X, Y$ metric spaces and $\mathcal{F}$ a family of functions, $F$ is *equicontinuous at \(x_0\)* iff for every $\varepsilon > 0$ there exists a \(\delta(\varepsilon, x_0)>0\) such that \[x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))\] for all \(f_i \in \mathcal{F}\).
The family $F$ is *uniformly equicontinuous* iff $\delta(\varepsilon)$ only depends on $\varepsilon$ and holds for any pair \(x_1, x_2\) with \(x_1 \in B_\delta(x_2)\).
%
definition
---

Reverse Triangle Inequality
%
$\abs{\norm x - \norm y} \leq \norm{x-y}$
%
formula
---

