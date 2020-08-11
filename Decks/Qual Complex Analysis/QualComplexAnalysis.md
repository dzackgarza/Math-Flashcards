An analytic function with convergence radius 1 which fails to converge at any point on $S^1$
%
$\sum_{n=1}^\infty nz^n$
%
example
---

An analytic function with convergence radius 1 which converges at every point on $S^1$
%
\[
\sum_{n=1}^\infty {z^n\over n^2}
\]
%
example
---

An analytic function with convergence radius 1 that converges at every point on $S^1$ except $z=1$
%
\[
\sum_{n=1}^\infty {z^n\over n}
\]
%
example
---

Dirichlet's Test
%
If \(\theset{a_n}, \theset{b_n}\) satisfy

- \(  a_{n+1} \leq a_n\) 
- \(  a_n \to 0\) 
- For every $N$, there exists an $M$ such that \(  \abs{\sum^N b_n} \leq M\)

Then \( \sum a_n b_n < \infty \).
%
theorem
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
The smallest $m$ such that 
\[
\lim_{x\to a}^{m+1}f(z) = 0
.\]
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
- If $f$ is holomorphic on \(\Omega\setminus\theset{z_0} \subseteq \CC\) where \(z_0\) is an essential singularity and \(V\subseteq \Omega\) then \(f(V\setminus\theset{z_0}) \injects \CC\) is dense.
- If $f$ is non-constant and entire then \(f(\CC)\injects \CP^1\) is dense.
%
Theorem
---

Cauchy Inequalities
%
\[
\left|f^{(n)}\left(z_{0}\right)\right| \leq \frac{n ! | f \|_{C}}{R^{n}}
.\]
%
formula, theorem
---

Cauchy Integral Formula (First Derivative)
%
For $f$ holomorphic in $U\supseteq \bar D$, then for any $z\in D$,
\[
f(z) = {1 \over 2\pi i} \int _{\bd D} {f(\xi) \over \xi - z} \,d\xi
.\]
%
formula, theorem
---

Cauchy Integral Formula (Higher Derivatives)
%
For $f$ holomorphic in $U\supseteq \bar D$ and $C$ is a circle such that $C^\circ \subset U$ then for any $z\in C^\circ$,
\[
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
.\]
%
formula, theorem
---

Maximum Length Lemma
%
\[
\abs{\int _\gamma f} \leq \sup_{z\in \gamma} \abs{f(z)} \cdot \ell(\gamma)
.\]
%

---

Maximum Modulus Principle
%
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $\abs{f}$ is unbounded in $\Omega^\circ$.
%
complex, theorem
---

Open Mapping Theorem
%
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $f$ is an open map.
%
complex, theorem
---

Exponential expansions of $\sin(z)$
%
$$
\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i},~~d\theta = \frac{dz}{iz}
$$
%
complex, identity
---

Rouche's Theorem
%
If $f, g$ are holomorphic on $\bar{D}(z_0)$ and $\abs{f - g} < \abs{f} + \abs{g}$ on $\bd D$, then $f,g$ are nonvanishing on $\bd D$ and have the same number of zeros.
%
complex, theorem
---

Cauchy-Goursat Theorem
%
If $f$ is analytic on a simply connected region $\Omega$ containing a contour $\gamma$, then \[\int_\gamma f = 0.\]
Moreover, this holds for any contour $\gamma \subset \Omega$.
%
complex, theorem
---

Types of singularities
%

- Removable: $\abs{f(z)}$ is bounded in a punctured disc.
- Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
- Essential: neither removable nor a pole.
%

complex, fact
---

Conformal Map
%
A holomorphic map with nowhere vanishing derivative (locally injective).
%
definition
---

Example of a conformal map that is not injective.
%
$$z\mapsto e^z$$
%
examples
---

General form of maps in $\aut(\DD)$.
%
$$f_\alpha(z) \definedas {\alpha - z \over 1 - \bar\alpha z}$$
%
fact
---

Cauchy's Integral Formula for Derivatives
%
\[
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
.\]
%
formula
---
