# Solutions — 05: Counting Infinite Sets — Sizes of Infinity
## Basic Drills

**D1.** Perfect squares $\{1,4,9,\dots\}$ — **same size** as $\mathbb{N}$ ($n \mapsto n^2$).
**D2.** Powers of 2 — **same size** ($n \mapsto 2^{n-1}$).
**D3.** Integers $\geq 100$ — **same size** ($n \mapsto n+99$).
**D4.** Finite $\{0,1\}$-strings — **countable** (each is a binary number).
**D5.** All finite strings over $\{0,1\}$ — **countable** (finite union over lengths, each length countable).
**D6.** $\mathbb{Z}$ countable — pairing $0,1,-1,2,-2,\dots$.
**D7.** Finite subsets of $\mathbb{N}$ — **countable** (map each subset to its binary-encoded number).
**D8.** $\mathbb{R}$ — **uncountable** (diagonal argument).
**D9.** $[0,1]$ and $[0,2]$ — **same size** ($x \leftrightarrow 2x$).
**D10.** $\mathcal{P}(\emptyset)$ has $2^0 = 1$ element ($\emptyset$ itself) — bigger than $\emptyset$ (which has 0).

> **Answers**: D1–D3 same as ℕ; D4–D5 countable; D6 yes; D7 countable; D8 uncountable; D9 same size; D10 one element.

---

## Advanced Drills

### A1. $|\mathbb{N} \times \mathbb{N}| = \aleph_0$ with a formula
Diagonal ordering by $s = a+b$: the diagonals before $s$ hold $\frac{(s-2)(s-1)}{2}$ pairs, then within diagonal $s$ pair $(a,b)$ sits at position $a$. So
$$f(a,b) = \frac{(a+b-2)(a+b-1)}{2} + a.$$
Check: $(1,1)\to1$, $(1,2)\to2$, $(2,1)\to3$, $(1,3)\to4$, $(2,2)\to5$, $(3,1)\to6$. This is a bijection.

### A2. Finite subsets of $\mathbb{N}$ are countable
Map subset $\{n_1 < n_2 < \dots < n_k\}$ to the binary number with 1s exactly in positions $n_1,\dots,n_k$. Distinct subsets give distinct numbers (unique binary representation) → injective into $\mathbb{N}$ → countable.

### A3. Infinite binary strings are uncountable
Assume a list $s_1, s_2, \dots$ of all infinite binary strings. Build $d$ whose $n$th bit is the *opposite* of the $n$th bit of $s_n$. Then $d$ differs from every listed string — not in the list. Contradiction.

### A4. $|(0,1)| = |\mathbb{R}|$
The map $x \mapsto \tan(\pi x - \pi/2)$ sends $(0,1)$ bijectively onto $\mathbb{R}$ (tangent rises from $-\infty$ to $\infty$ on $(-\pi/2,\pi/2)$). So the open interval has the same size as the whole real line.

### A5. $|\mathbb{R}| = |\mathbb{R}^2|$ (idea)
Interleave decimal digits: $0.a_1a_2a_3\dots$ and $0.b_1b_2b_3\dots$ map to $0.a_1b_1a_2b_2\dots$ (and reverse). Digit-interleaving builds a bijection between $(0,1)$ and $(0,1)^2$ — so $\mathbb{R}$ and $\mathbb{R}^2$ have the same cardinality. (The two-representation issue for reals like $0.4999\dots = 0.5$ is handled by a canonical choice; it's the same size regardless.)

### A6. Sequences of natural numbers are uncountable
Assume a list of all sequences $(a^{(1)}, a^{(2)}, \dots)$. Build $d$ with $d_n = a^{(n)}_n + 1$ (change each diagonal entry). $d$ differs from every listed sequence → not in the list. Contradiction.

### A7. No bijection between $S$ and $\mathcal{P}(S)$
Generalize the diagonal argument: suppose $f: S \to \mathcal{P}(S)$ is onto. Let $D = \{x \in S : x \notin f(x)\}$. Then $D = f(d)$ for some $d$; check both memberships — each contradicts the other. No onto map exists.

### A8. Integer polynomials are countable
For each degree $n$, polynomials of degree $n$ with integer coefficients form $\mathbb{Z}^{n+1}$, which is countable. Countable union of countable sets is countable → all integer polynomials countable. (Their roots — the algebraic numbers — are consequently countable too.)

### A9. Real polynomials are uncountable
Real polynomials contain the constant polynomials $\{c : c \in \mathbb{R}\}$, which are already uncountable. So the set of real polynomials is uncountable. (A8's countability dies because the *coefficients* are now real.)

### A10. $|\mathbb{R}| = |\mathcal{P}(\mathbb{N})|$ (idea)
Each real in $(0,1)$ has a binary expansion — an infinite string of 0s and 1s. Reading that string as the indicator function of a subset of $\mathbb{N}$ (positions of 1s) gives a subset of $\mathbb{N}$. This pairs $(0,1)$ with $\mathcal{P}(\mathbb{N})$ up to the harmless ambiguity of reals with two expansions (e.g., $0.1000\dots = 0.0111\dots$), which affects only countably many points. Hence $|\mathbb{R}| = 2^{\aleph_0} = |\mathcal{P}(\mathbb{N})|$.
