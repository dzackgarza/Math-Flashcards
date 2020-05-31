Retract
%
Retract: A subspace $A \subset X$ is a *retract* of $X$ iff there exists a continuous map $f: X\to A$ such that $f\mid_{A} = \id_A$. 
Equivalently it is a *left* inverse to the inclusion.
%
definition
---

Deformation Retract
%
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a morphism $F:X\cross I$ to $X$ such that $F(x, 0) = x, F(x, 1)\in A, F(a, 1) = a$.
Equivalently it is a homotopy between a retraction and the identity.
%
definition
---

Locally Compact
%
A space $X$ is *locally compact* iff for every $x\in X$ there exists an open $U$ and compact $K$ such that $x\in U \subseteq K$.

Compact implies locally compact but not conversely: $\RR^n$.

Non locally-compact spaces: $\QQ, \theset{\vector 0} \union \theset{(x, y) \suchthat x>0} \subset\RR^2$ (since the origin admits no compact neighborhood).
%
definition, counterexample
---


Are singletons open or closed?
%
- In Hausdorff spaces: closed
%
theorem
---

Normal Space
%
A space $X$ is **normal** iff every two disjoint closed sets have disjoint open neighborhoods.
%
definition
---

Urysohn's Lemma
%
A space $X$ is normal iff for every closed $U, V \subset X$ there exists a continuous function $f: X\to [0, 1]$ with $f(U) = 0, f(V) = 1$.
%
theorem
---

Hausdorff Space
%
A space $X$ is **Hausdorff** iff for every $x,y \in X$ there exist neighborhoods of $x$ and $y$ that are disjoint from each other.

(Implies uniqueness of limits.)
%
definition
---

Semilocally Simply Connected
%
Every point admits a neighborhood $U$ such that $\pi_1(U) = 0$.
%
definition
---

Local homeomorphism
%
A map $f:X\to Y$ is a local homeomorphism iff for every $x\in X$ there exists a neighborhood $U_x$ such that $f(U_x)$ is open in $Y$ and $f\mid_{U_x}: U_x \to f(U_x)$ is a homeomorphism.

Examples: etale spaces, covering spaces.
%
definition
---

Locally homeomorphic
%
$X$ is *locally homeomorphic* to $Y$ iff every $x\in X$ admits a neighborhood $U_x$ that is homeomorphic to an open subset of $Y$.

Note that $X$ being locally homeomorphic to $Y$ does *not* imply that there exists a local homeomorphism.
%

---

