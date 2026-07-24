# Solution — Problem 6: Abstraction Ladder

**(a)** Level 0 peak WM: ~7 slots (holds: matrix entries, $\lambda$, determinant expression, expanded terms, quadratic coefficients, discriminant, two roots). Steps: ~15.

**(b)** Level 2 peak WM: ~3 slots (holds: matrix structure $3I+J$, eigenvalue property of $J$, final computation). Steps: ~4.

**(c)** Compression factor: $7/3 \approx 2.3\times$ in WM, $15/4 \approx 3.75\times$ in steps.

**(d)** The matrix is $3I + 2\begin{pmatrix}1&1\\1&1\end{pmatrix} = 3I + 2J$. Eigenvalues: $3+2\cdot2=7$, $3+2\cdot0=3$.

**(e)** The matrix has the form $(a-b)I + bJ$ where $J$ is the $4\times4$ all-ones matrix (a **rank-1 perturbation of identity**). The eigenvalues are: $(a-b) + 4b = a + 3b$ (once) and $a - b$ (multiplicity 3).
