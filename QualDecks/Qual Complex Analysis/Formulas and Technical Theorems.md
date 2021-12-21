Cauchy's Integral Formula for Derivatives
%
\[
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
.\]
%
formula
---


Rouché's Theorem
%
If $f, g$ are holomorphic on $\bar{D}(z_0)$ and 
\[
\abs{f - g} < \abs{f} + \abs{g} \quad\text{on}\quad \bd D
,\] 
then $f,g\neq 0$ on $\bd D$ and have the same number of zeros.
%
complex, theorem
---

Cauchy Inequalities
%
\[
\left|f^{(n)}\left(z_{0}\right) \over n! \right| \leq \frac{ \sup_{z\in\gamma} \abs{f(z)} {R^{n}}
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


Double angle formulas involving $\tan$
%
The double angle formulas:
\[
\sin(2t) = {2\tan(t) \over 1+\tan^2(t)} && \cos(2t) = {1-\tan^2(2t) \over 1+\tan^2(t)}
.\]

%
formula
---


Standard parameterization of a circle in $\CC$
%
\[
F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2} \quad x = \tan(t), t\in (-\pi/2, \pi/2)
.\]

%
formula
---

Cross-ratio map
%

\[
R(z) \da (z, z_2, z_3, z_4) &\da {z - z_3\over z-z_4}{z_2 - z_4 \over z_2 - z_3} \\
.\]

Sends 

- $z_2 \to 1$
- $z_3\to 0$
- $z_4\to \infty$

%
formula
---


The generalized residue formula
%
\[
\Res_{z=z_0} f = \lim_{z\to z_0} {1 \over (n-1)!} \qty{\dd{}{z}}^{n-1} (z-z_0)^n f(z)
.\]
%
formula
---
