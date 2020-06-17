An analytic function with convergence radius 1 which fails to converge at any point on $S^1$
%
$\sum nz^n$
%
example
---

An analytic function with convergence radius 1 which converges at every point on $S^1$
%
$\sum z^n/n^2$
%
example
---

An analytic function with convergence radius 1 that converges at every point on $S^1$ except $z=1$
%
$\sum z^n/n$
%
example
---

Dirichlet's Test
%
If $\theset{a_n}, \theset{b_n}$ satisfy

- $a_{n+1} \leq a_n$
- $a_n \to 0$
- For every $N$, there exists an $M$ such that $\abs{\sum^N b_n} \leq M$

Then $\sum a_n b_n < \infty$.
%
theorem
---

Cauchy Integral Formula
%
For $f: U\to \CC$ holomorphic with $\gamma \subset U^\circ$ and every $a\in \gamma^\circ$, 
\begin{align*}
f(a) = {1\over 2\pi i} \int_\gamma {f(z) \over z-a}\,dz
.\end{align*}
%
formula
---

Morera's Theorem
%
If $f$ is continuous in an open disc $D$ and for every triangle $T\subset D, \int_T f = 0$, then $f$ is holomorphic.
%
theorem
---

Riemann's Removable Singularity Theorem
%
Let $U\subset \CC$ be open, $a\in U$, and $f$ holomorphic on $U\setminus\theset{a}$. 
Then TFAE
- $f$ extends holomorphically to all of $U$
- $f$ extends continuously to all of $U$
- There exists a neighborhood of $a$ on which $f$ is bounded.
- $\lim_{z\to a} (z-a)f(z) = 0$.
%
theorem
---

Definition: A pole $a$ of order $m$
%
The smallest $m$ such that $\lim_{x\to a}^{m+1}f(z) = 0$.
%
definition
---

Definition: A removable singularity
%
A pole of order zero.
%
definition
---

Definition: An essential singularity
%
An isolated singularity that is not a pole (or removable).
%
definition
---

Casorati-Weierstrass Theorem
%
If $f$ is non-constant and entire then $f(\CC)\injects \CC$ is dense.
%
Theorem
---

Cauchy Inequalities
%
\begin{align*}
\left|f^{(n)}\left(z_{0}\right)\right| \leq \frac{n ! | f \|_{C}}{R^{n}}
.\end{align*}
%
formula, theorem
---

