Does $A^n=B^n$ imply $A=B$?
%
No, counterexample: 
\[  
M^2 = \begin{bmatrix}
0 & 1 \
1 & 0
\end{bmatrix}^2 = I
.\]
%
counterexample
---

Characterizations of Diagonalizability of a Square Matrix $M$
%

- $\min_M(x)/\FF$ splits into distinct linear factors over $\FF$ (i.e. is separable)
- $\FF$ contains all of the roots of $\min_M(x)/\FF$
- There exists a basis of $\FF^n$ consisting of eigenvectors of $M$
- All elementary divisors are linear
- (Sufficient) $M$ has $n$ distinct eigenvalues
- (Sufficient) $\min_M(x)/\FF$ has $n$ distinct roots.

%
theorem
---

Definition: Free module
%

![](https://i.imgur.com/h5r2lty.png)

%
definition
---

Definition: Projective module
%

![](https://i.imgur.com/z4sW2hh.png)

Equivalently, for $R\dash$modules, $M$ is projective $\iff$ $M$ is a direct summand of a free module.

%
definition
---

Submodule test
%
If \( r\in R,\, m,n \in M \implies rm + n \in M  \) then $M$ is a submodule.
%
fact
---

$\gens{p}\dash$primary
%
For every $m\in M$ and $t\in R$ with $t\not\in \gens{p}$, there exists a $a\in R$ such that $atm = m$.
%
definition  
---

Noetherian Module
%
Any strictly increasing chain of submodules \(M_1 \subsetneq M_2 \cdots \) is finite.
%
definition
---

Definition: Torsion element
%
$m\in M$ is torsion iff \( \tor(m)\neq 0 \).
%
---


Definition: Torsion submodule.
%
\[  
\tor(M) = \{m \in M \suchthat \exists r \in R, ~r \neq 0, ~rm = 0\}
.\]
%
definition
---

Rank of a Free module
%
Maximal number of $R\dash$linearly independent elements of \( M\).
%
definition
---

Definition: torsionfree
%
\( \tor(M) = \theset{0} \)
%
definition
---


Annihilator of a module
%
For $M$ an $R\dash$module,
\[  
\mathrm{ann}_R(M) = \theset{r\in R\suchthat \forall m\in M,\, rm=0} \normal R
.\]
%
definition
---


Irreducible Module
%
Simple module, i.e. no nontrivial proper submodules.
%
definition
---

Indecomposable Module
%
Can not be written as a direct sum of two nonzero submodules.
%
definition
---

Definition: Rational Canonical Form
%
For $\phi:V\to V$, corresponds to invariant factor decomposition of $V$ as a $k[x]\dash$module, 
\[  
V \cong \bigoplus k[x]/ (r_i) \qquad r_1 \divides r_2 \divides \cdots
.\]

The $r_i$ are the minimal polynomials of $\phi$ restricted to $V_i$.
The matrix of $\phi$ consists of blocks of companion matrices for the $\phi_i$.
%
definition
---


Definition: Characteristic polynomial
%
\[  
p_A(x) = \mathrm{det}(xI - A)
.\]

%
definition
---

Definition: Diagonalizable.
%
For a matrix $A$, similar to a diagonal matrix.
I.e. there exists a diagonal $D$ and some $P\in \mathrm{GL}(n, R)$ such that $A = PDP^{-1}$
%
definition
---


Cyclic Module
%
For $M$ an $R\dash$module, $M$ is cyclic iff $M = \gens{m}$ iff $M \cong R/I$ for some ideal $I\normal R$.
%
definition
---

Classification of Finitely Generated Modules over a PID
%

![](https://i.imgur.com/z4sW2hh.png)

%
theorem
---

Proposition: Every free module is projective.
%

![](https://i.imgur.com/qZiRxvR.png)

%
proposition
---

