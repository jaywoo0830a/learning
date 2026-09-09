# Mathematics Curriculum v5: The Tool Inventor's Path

> **Grand goal:** Become someone who someday builds new tools that advance mathematics and science.
> **Means:** Decompose the great tools already invented, by method, and embody them.
> **Principle:** Method first, vocabulary last. Every session follows the ① ② ③ step pattern.
> **Scale:** 111 sessions, ~156 hours. From Precalculus technique to 21st-century tools.
> **Time:** 30 minutes to 2 hours, depending on method complexity.
> **v5 changes:** Linear algebra moved before differential equations (fixes dependency inversion); Fourier series added as an explicit session; session counts and hour totals reconciled; every phase now ends in a timed synthesis/milestone; Phase 1 gained a formative milestone.

---

## Overall Structure

| Phase | Tool family | Sessions | Hours |
|:---:|------|:---:|:---:|
| 1 | The grammar of tools — logic·proof·sets | 7 | 7.5h |
| **2** | **Classical technique — Precalculus→AP Calculus, compressed** | **14** | **15h** |
| 3 | Change & accumulation — real analysis (proof) | 17 | 23h |
| 4 | Many at once — linear algebra | 11 | 11.75h |
| 5 | The laws of change — differential equations | 10 | 13.75h |
| 6 | The eye for structure — abstract algebra | 8 | 11.5h |
| 7 | Space & shape — topology·geometry | 10 | 18h |
| 8 | Uncertainty — measure-theoretic probability | 11 | 18.5h |
| 9 | Computation & optimization — numerical·ML math | 11 | 16.75h |
| 10 | The frontier — 20th–21st century topics | 12 | 20.5h |
| **Total** | | **111** | **~156.25h** |

> Counting: **101 tool sessions** + **9 phase syntheses** + **1 capstone** = 111 sessions.

---

## Phase 1: The Grammar of Tools — Logic·Proof·Sets (7 sessions, 7.5h)

> **Core question:** "How can you be certain a claim is true?"

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 01 | Truth tables & logical equivalence | ① memorize the rules for $\neg, \land, \lor, \to$ ② fill columns of a compound statement ③ transform via De Morgan, test tautology | 30m |
| 02 | $\forall$, $\exists$, negation | ① fix the domain ② $\forall$: substitute all, $\exists$: one only ③ $\neg\forall \equiv \exists\neg$, $\neg\exists \equiv \forall\neg$ | 45m |
| 03 | Direct, contrapositive, contradiction | ① direct: derive $P$→$Q$ ② contrapositive: $\neg Q$→$\neg P$ ③ contradiction: $P\land\neg Q$→contradiction ④ counterexample strategy | 60m |
| 04 | Mathematical induction | ① check $P(1)$ ② assume $P(k)$ → derive $P(k+1)$ ③ strong induction | 45m |
| 05 | Sets·functions·cardinality | ① compare size by bijection ② $\lvert\mathbb{N}\rvert=\lvert\mathbb{Z}\rvert=\lvert\mathbb{Q}\rvert=\aleph_0$ ③ diagonal argument: $\lvert\mathbb{R}\rvert>\aleph_0$ | 90m |
| 06 | Gödel's incompleteness theorem | ① Gödel number $\ulcorner\phi\urcorner$ ② construct $\text{Provable}(x)$ ③ $G \leftrightarrow \neg\text{Provable}(\ulcorner G\urcorner)$ ④ if consistent, neither $G$ nor $\neg G$ is provable — yet $G$ is true | 120m |
| 07 | **Phase 1 synthesis** | mixed proofs across sessions 01–06 — the "how do we know" milestone | 60m |

---

## Phase 2: Classical Technique — Precalculus→AP Calculus, Compressed (14 sessions, 15h)

> **Core question:** "Before modern mathematics, master every computation the hand must remember."
> **Principle:** Proof is deferred to Phase 3. Here only the "plug in, get an answer" procedures.

### Part A: Precalculus technique (6 sessions)

| # | Technique bundle | Method procedure | Time |
|:--:|------|-----------|:---:|
| 08 | Polynomials·rationals·equations | ① synthetic division: test divisors of the constant → remainder 0 → lower the degree, repeat ② factoring strategy: common factor→substitution→formula→synthetic order ③ partial fractions: $\frac{P(x)}{Q(x)}=\frac{A}{x-a}+\frac{B}{x-b}+\cdots$ compare coefficients ④ systems: eliminate one variable → back-substitute ⑤ higher-degree: lower the degree by factoring | 60m |
| 09 | Inequalities·sign charts·absolute value | ① factor → mark critical points on a line → decide sign on each interval ② rational inequalities: exclude denominator $\neq 0$ ③ absolute value: $\lvert x\rvert<a \Leftrightarrow -a<x<a$, $\lvert x\rvert>a \Leftrightarrow x<-a \lor x>a$ ④ quadratic: where the parabola is above/below the $x$-axis | 45m |
| 10 | Functions all-in-one | ① four domain rules: denominator$\neq$0, under-root$\geq$0, inside-log$>$0, $\tan$ asymptotes ② composition $f(g(x))$: inside→outside order ③ inverse: reflect over $y=x$, solve for $y$ ④ translation: $f(x-h)$ shifts right $h$, $f(x)+k$ shifts up $k$ ⑤ read 5 features: domain·range·increase/decrease·extrema·asymptotes | 60m |
| 11 | Exponentials·logarithms all-in-one | ① laws: $a^m a^n=a^{m+n}$, $(a^m)^n=a^{mn}$, $a^{-n}=1/a^n$, $a^{m/n}=\sqrt[n]{a^m}$ ② log: $\log_a b=c \leftrightarrow a^c=b$, $\log(MN)=\log M+\log N$, $\log(M/N)=\log M-\log N$, $\log(M^k)=k\log M$ ③ equations: unify bases or combine logs, check argument$>$0 ④ computational definition of $e$: $\lim(1+1/n)^n$, continuous compounding | 45m |
| 12 | Trigonometry all-in-one | ① radians: $\pi=180^\circ$, convert by proportion ② unit circle: $(\cos\theta,\sin\theta)$, $\tan\theta=\sin/\cos$, quadrant signs ③ graphs: $\sin$/$\cos$ period$=2\pi/\lvert b\rvert$, amplitude$=\lvert a\rvert$, $\tan$ period$=\pi/\lvert b\rvert$ ④ identities: $\sin^2+\cos^2=1$, $\sin2\theta=2\sin\theta\cos\theta$, $\cos2\theta=\cos^2-\sin^2$ ⑤ equations: base solution $+n\cdot$period, law of sines·cosines | 75m |
| 13 | Complex numbers·vectors·sequences | ① complex arithmetic·conjugate $\bar{z}$·modulus $\lvert z\rvert$ ② polar form $z=r(\cos\theta+i\sin\theta)=re^{i\theta}$, de Moivre $z^n=r^n e^{in\theta}$ ③ vectors: components·dot product $\mathbf{a}\cdot\mathbf{b}=a_1b_1+a_2b_2$·angle formula ④ arithmetic: $a_n=a_1+(n-1)d$, $S_n=\frac{n(a_1+a_n)}{2}$ ⑤ geometric: $a_n=a_1 r^{n-1}$, $S_n=a_1\frac{1-r^n}{1-r}$ ⑥ $\sum k=\frac{n(n+1)}{2}$, $\sum k^2=\frac{n(n+1)(2n+1)}{6}$ | 60m |

### Part B: AP Calculus technique (8 sessions)

| # | Technique bundle | Method procedure | Time |
|:--:|------|-----------|:---:|
| 14 | The limit machine | ① direct substitution: continuous → just plug in ② $\frac{0}{0}$: factor→cancel, conjugate→cancel, use $\frac{\sin x}{x}\to1$ ③ $\frac{\infty}{\infty}$: divide by highest power ④ limits at infinity: sign of highest power → $\pm\infty$ ⑤ standard limits: $(1+\frac{1}{n})^n\to e$, $\frac{\ln n}{n}\to0$ | 60m |
| 15 | Differentiation: the full arsenal | ① basics: $\frac{d}{dx}x^n=nx^{n-1}$, $e^x$, $\ln x$, $\sin x\to\cos x$, $\cos x\to-\sin x$, $\tan x\to\sec^2 x$ ② product: $(fg)'=f'g+fg'$ ③ quotient: $(\frac{f}{g})'=\frac{f'g-fg'}{g^2}$ ④ chain: $\frac{d}{dx}f(g(x))=f'(g(x))g'(x)$ ⑤ implicit: differentiate both sides → collect $\frac{dy}{dx}$ terms → solve ⑥ logarithmic: take $\ln$ then differentiate → handle complex powers ⑦ inverse-function·parametric: $\frac{dy}{dx}=\frac{dy/dt}{dx/dt}$ | 75m |
| 16 | Applications of the derivative | ① tangent at $(a,f(a))$: $y-f(a)=f'(a)(x-a)$, normal: slope$=-1/f'(a)$ ② MVT: find $c$ with $f'(c)=\frac{f(b)-f(a)}{b-a}$ ③ inc/dec table: sign of $f'$ ④ extrema: sign change at $f'=0$ ⑤ concavity·inflection: sign of $f''$ ⑥ 7-step sketch: domain→intercepts→asymptotes→inc/dec→extrema→concavity→draw ⑦ optimization: objective→eliminate constraint→$f'=0$→verify ⑧ related rates: relation→differentiate by $t$→substitute | 75m |
| 17 | Integration: the full arsenal | ① FTC: $\int_a^b f(x)dx=F(b)-F(a)$ ② substitution: $u=g(x)$, $du=g'(x)dx$, convert $u$-bounds ③ parts: $\int u dv=uv-\int v du$, choose $u$ by LIATE ④ partial fractions: factor → $\frac{A}{x-a}+\frac{B}{(x-a)^2}+\frac{Cx+D}{x^2+bx+c}$ ⑤ trig substitution: $\sqrt{a^2-x^2}\to x=a\sin\theta$, $\sqrt{a^2+x^2}\to x=a\tan\theta$, $\sqrt{x^2-a^2}\to x=a\sec\theta$ ⑥ trig integrals: $\sin^2 x=\frac{1-\cos2x}{2}$, $\cos^2 x=\frac{1+\cos2x}{2}$, split $\tan^n\sec^m$ | 90m |
| 18 | Applications of the integral | ① area between curves: $\int_a^b[f(x)-g(x)]dx$ ② disk: $\pi\int R^2 dx$, washer: $\pi\int(R^2-r^2)dx$, shell: $2\pi\int r h dx$ ③ arc length: $L=\int_a^b\sqrt{1+(y')^2}dx$ ④ improper: $\int_a^\infty=\lim_{b\to\infty}\int_a^b$, one-sided limit at discontinuity ⑤ convergence: compare against $\int_1^\infty 1/x^p$ | 75m |
| 19 | Series & Taylor | ① geometric: $\sum ar^n=\frac{a}{1-r}$ ($\lvert r\rvert<1$) ② $p$-series: $\sum 1/n^p$ converges↔$p>1$ ③ comparison·limit-comparison·ratio·root tests ④ alternating: $a_n\searrow0$→converges, error$\leq a_{n+1}$ ⑤ Taylor: $f(x)=\sum\frac{f^{(n)}(a)}{n!}(x-a)^n$ ⑥ Maclaurin table: $e^x,\sin x,\cos x,\ln(1+x),\frac{1}{1-x}$ | 75m |
| 20 | Differential equations: basics | ① separable: $\frac{dy}{dx}=g(x)h(y)$ → $\int\frac{dy}{h(y)}=\int g(x)dx$ ② exponential model: $y'=ky$ → $y=Ce^{kt}$, doubling time $t_2=\ln2/k$ ③ logistic: $y'=ky(1-y/L)$ → $y=\frac{L}{1+Ae^{-kt}}$ ④ first-order linear: $y'+P(x)y=Q(x)$, integrating factor $\mu=e^{\int Pdx}$ | 45m |
| 21 | **Phase 2 synthesis** | mixed problems over all 14 sessions — decide which technique, first | 60m |

---

## Phase 3: Change & Accumulation — Real Analysis (17 sessions, 23h)

> **Core question:** "Why do the Phase 2 computations work? — answer with proof."
> **Premise:** Limit·derivative·integral computation is already embodied in Phase 2. Here focus on $\varepsilon$-$\delta$ and proof.

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 22 | Completeness of $\mathbb{R}$ | ① find $\sup$, $\inf$ ② sequence convergence via $\varepsilon$-$N$ ③ Cauchy sequences ↔ convergence (in $\mathbb{R}$ only) | 90m |
| 23 | Limits — $\varepsilon$-$\delta$ | ① given $\varepsilon$, find $\delta$ ② justify $\frac{0}{0}$ limits ③ prove $\lim\frac{\sin x}{x}=1$, $\lim(1+\frac{1}{n})^n=e$ | 90m |
| 24 | Continuity·intermediate value·extreme value | ① continuity via $\varepsilon$-$\delta$ ② prove IVT ③ EVT: continuous on closed interval → max/min exists | 60m |
| 25 | Derivative — definition & proofs | ① $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ ② prove differentiable→continuous ③ prove product·quotient·chain rules | 75m |
| 26 | Mean value theorem·Taylor's theorem | ① prove Rolle→MVT ② justify inc/dec test via MVT ③ Taylor's theorem + remainder (Lagrange·Cauchy) | 60m |
| 27 | Integration — Riemann sums & FTC | ① Riemann sums·upper/lower sums ② prove FTC ③ test integrability | 75m |
| 28 | Justifying integration techniques | ① prove substitution ② prove integration by parts ③ theoretical basis of partial fractions·trig substitution | 90m |
| 29 | Improper integrals | ① infinite intervals·discontinuities: $\lim$ handling ② prove comparison test | 60m |
| 30 | Convergence of sequences & series | ① prove comparison·limit-comparison·ratio·root tests ② alternating series estimate | 75m |
| 31 | Power series & Taylor series | ① radius of convergence: ratio test ② convergence of Taylor series·analytic functions | 75m |
| 32 | Sequences of functions·uniform convergence | ① pointwise vs uniform: $\sup\lvert f_n-f\rvert\to0$ ② uniform → $\lim\int=\int\lim$ ③ condition for $\lim f_n' = (\lim f_n)'$ | 90m |
| 33 | Fourier series | ① orthogonality: $\int_{-\pi}^{\pi}\sin nx\cos mx\,dx=0$ ② compute coefficients $a_n,b_n$ ③ pointwise/uniform convergence, Gibbs phenomenon | 90m |
| 34 | Topology of $\mathbb{R}^n$ | ① open balls·open/closed sets ② compact: Heine–Borel | 60m |
| 35 | Multivariable differentiation | ① partial derivatives·gradient $\nabla f$ ② directional derivative·Jacobian·chain rule | 90m |
| 36 | Multivariable integration | ① Fubini·change of variables·polar·cylindrical·spherical | 90m |
| 37 | Stokes' theorem (classical) | ① Green·Gauss·Stokes ② unified: $\int_{\partial M}\omega = \int_M d\omega$ | 120m |
| 38 | **Phase 3 synthesis** | $\varepsilon$-$\delta$ → FTC → multivariable → Stokes — one chain | 90m |

---

## Phase 4: Many at Once — Linear Algebra (11 sessions, 11.75h)

> **Core question:** "How do you solve a problem with dozens of variables in one move?"
> **Order note (v5):** Linear algebra now precedes differential equations, because eigenvalues, linear independence, and matrices are prerequisites for systems of ODEs and Sturm–Liouville theory (Phase 5).

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 39 | Matrices & Gaussian elimination | ① multiply: $(AB)_{ij}=\sum_k a_{ik}b_{kj}$ ② zero below the pivot → back-substitute ③ RREF | 45m |
| 40 | Vector spaces·subspaces·dimension | ① test subspace ② linear independence·basis·$\dim$ | 75m |
| 41 | Linear maps & rank-nullity | ① $T(\mathbf{x})=A\mathbf{x}$, $\ker T$, $\operatorname{range}T$ ② $\dim\ker + \dim\operatorname{range} = n$ | 60m |
| 42 | Determinants & eigenvalues | ① cofactor expansion ② $\det(A-\lambda I)=0$ → $\lambda_i$ → eigenvectors | 75m |
| 43 | Diagonalization & spectral theorem | ① $P^{-1}AP=\Lambda$ ② symmetric: $A=Q\Lambda Q^{\mathsf{T}}$ | 75m |
| 44 | Inner products·Gram–Schmidt·QR | ① GS: normalize→subtract projection→repeat ② $A=QR$ | 60m |
| 45 | Singular value decomposition (SVD) | ① $A=U\Sigma V^{\mathsf{T}}$, rank-$k$ approximation | 90m |
| 46 | Least squares & pseudoinverse | ① $A^{\mathsf{T}}A\hat{\mathbf{x}}=A^{\mathsf{T}}\mathbf{b}$ ② $A^\dagger$ (via SVD) | 60m |
| 47 | PCA & dimensionality reduction | ① covariance matrix→eigendecomposition→principal components ② $X_k = X V_k$ | 60m |
| 48 | Norms·condition numbers·stability | ① vector·matrix norms ② $\kappa(A)=\lVert A\rVert\lVert A^{-1}\rVert$ | 45m |
| 49 | **Phase 4 synthesis** | elimination → eigenvalues → SVD — the linear toolbox | 60m |

---

## Phase 5: The Laws of Change — Differential Equations (10 sessions, 13.75h)

> **Core question:** "Nature speaks as 'rate of change = something.' How do we solve that equation?"
> **Order note (v5):** Eigenvalues, eigenvectors, and linear independence are already available from Phase 4.

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 50 | First-order ODE: separable·linear | ① separable: $\frac{dy}{dx}=g(x)h(y)$ → $\int\frac{dy}{h(y)}=\int g(x)dx$ ② linear: $y'+P(x)y=Q(x)$, integrating factor $\mu=e^{\int Pdx}$ → $y=\frac{1}{\mu}\int\mu Q dx$ | 75m |
| 51 | First-order ODE: exact·homogeneous·Bernoulli | ① exact: $Mdx+Ndy=0$, $M_y=N_x$ → $\phi(x,y)=C$ ② homogeneous: substitute $v=y/x$ → separable ③ Bernoulli: substitute $v=y^{1-n}$ → linear | 90m |
| 52 | Second-order linear ODE: homogeneous | ① characteristic equation $ar^2+br+c=0$ → distinct·repeated·complex roots ② Wronskian linear-independence test | 75m |
| 53 | Second-order linear ODE: nonhomogeneous | ① undetermined coefficients: guess from $g(x)$ ② variation of parameters: $y_p=-y_1\!\int\!\frac{y_2 g}{W}dx + y_2\!\int\!\frac{y_1 g}{W}dx$ | 90m |
| 54 | Laplace transform | ① $\mathcal{L}\{f\}=\int_0^\infty e^{-st}f(t)dt$, basic table ② $\mathcal{L}\{f'\}=s\mathcal{L}\{f\}-f(0)$ ③ ODE→algebra→partial fractions→inverse transform | 90m |
| 55 | Systems of ODEs & phase plane | ① $\mathbf{x}'=A\mathbf{x}$ → eigenvalues·eigenvectors ② classify phase-plane stability ③ nonlinear: Jacobian linearization | 90m |
| 56 | Series solutions & Frobenius | ① $y=\sum a_n x^n$ → recurrence ② Frobenius: $y=x^r\sum a_n x^n$, indicial equation | 75m |
| 57 | Boundary value problems & Sturm–Liouville | ① $-(py')'+qy=\lambda wy$, eigenvalues·eigenfunctions ② orthogonality·generalized Fourier expansion | 90m |
| 58 | Intro to PDE: separation of variables | ① heat·wave·Laplace → separate $X(x)T(t)$ → Fourier series solution | 90m |
| 59 | **Phase 5 synthesis** | first-order→second-order→systems→Laplace→series→S-L→PDE — the solution chain | 60m |

---

## Phase 6: The Eye for Structure — Abstract Algebra (8 sessions, 11.5h)

> **Core question:** "How do we grasp that different objects share the same structure?"

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 60 | Groups: definition + many examples | ① check the 4 axioms ② $\mathbb{Z}_n, S_n, D_n, \mathrm{GL}_n, \mathbb{Z}, \mathbb{R}^\times$ | 60m |
| 61 | Subgroups·Lagrange·homomorphisms | ① test $H\leq G$ ② $\lvert H\rvert \mid \lvert G\rvert$ ③ $G/\ker\varphi\cong\operatorname{im}\varphi$ | 75m |
| 62 | Group actions·seeing through symmetry | ① orbit·stabilizer·$\lvert G\rvert=\lvert G\cdot x\rvert\cdot\lvert G_x\rvert$ ② Burnside → counting colorings | 90m |
| 63 | Rings·ideals·quotient rings | ① ring axioms ② $I\trianglelefteq R$, construct $R/I$ | 75m |
| 64 | Fields·polynomials·algebraic extensions | ① field: every nonzero element has an inverse ② $\mathbb{Q}(\sqrt{2})$, $\mathbb{F}_p$, $\mathbb{F}_{p^n}$ | 90m |
| 65 | Category theory: intro | ① objects·morphisms·functors·natural transformations ② $\mathbf{Set}, \mathbf{Grp}, \mathbf{Vect}, \mathbf{Top}$ | 120m |
| 66 | Universal properties·limits·duality | ① universal property ② limits·colimits ③ duality principle | 120m |
| 67 | **Phase 6 synthesis** | group → ring → field → category — the structural ladder | 60m |

---

## Phase 7: Space & Shape — Topology & Geometry (10 sessions, 18h)

> **Core question:** "Using only the notion 'near,' how do we describe every property of space?"

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 68 | Metric spaces → topological spaces | ① metric axioms→open balls→open sets ② topological axioms ③ subspace·product·quotient | 90m |
| 69 | Connectedness·compactness | ① connected ② compact·Heine–Borel ③ properties of continuous functions on compacta | 90m |
| 70 | Homotopy·fundamental group | ① $\pi_1(X,x_0)$: loop homotopy classes ② prove $\pi_1(S^1)=\mathbb{Z}$ | 120m |
| 71 | Covering spaces·Seifert–van Kampen | ① covering spaces·lifting ② SvK → fundamental groups of surfaces | 120m |
| 72 | Homology: intro | ① chain complexes·$\partial^2=0$ ② $H_n=\ker\partial_n/\operatorname{im}\partial_{n+1}$ ③ sphere·torus·$\mathbb{RP}^2$ | 120m |
| 73 | Smooth manifolds | ① charts·atlases·tangent spaces ② immersions·submersions·regular value theorem | 90m |
| 74 | Differential forms·de Rham cohomology | ① $k$-forms·$d$·$d^2=0$ ② $H^k_{dR}$, generalized Stokes | 120m |
| 75 | Riemannian metric·curvature | ① $g_{ij}$·geodesics ② curvature tensor·Gauss–Bonnet | 120m |
| 76 | Fiber bundles·connections | ① $F\to E\to B$·principal bundles·vector bundles ② connections·curvature·gauge theory | 120m |
| 77 | **Phase 7 synthesis** | point-set → algebraic → smooth → Riemannian — the geometry chain | 90m |

---

## Phase 8: Modern Tools of Uncertainty — Measure-Theoretic Probability (11 sessions, 18.5h)

> **Core question:** "How do we extend the notions of length and area to every set?"

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 78 | Measures·$\sigma$-algebras | ① $\sigma$-algebra·Lebesgue outer measure ② Carathéodory measurability ③ Lebesgue measure | 120m |
| 79 | Lebesgue integral | ① simple functions→integral ② monotone·dominated convergence·Fatou | 120m |
| 80 | $L^p$ spaces | ① $\lVert f\rVert_p$, Hölder·Minkowski ② $L^p$ completeness, $L^2$ Hilbert | 90m |
| 81 | Probability spaces·random variables·expectation | ① $(\Omega,\mathcal{F},P)$ ② $E(X)=\int X dP$ ③ independence·distributions | 75m |
| 82 | Laws of large numbers·CLT (proof) | ① Markov·Chebyshev ② weak·strong law ③ CLT: characteristic functions+Lévy | 120m |
| 83 | Conditional expectation·martingales | ① $\mathbb{E}[X\mid\mathcal{G}]$ ② martingales·stopping times·convergence theorems | 120m |
| 84 | Markov chains·ergodicity | ① transition probabilities·Chapman–Kolmogorov ② $\pi P=\pi$·stationary distribution | 90m |
| 85 | Brownian motion·Itô integral | ① Wiener process ② Itô integral·Itô's formula | 120m |
| 86 | SDEs·financial mathematics | ① geometric Brownian motion ② Black–Scholes PDE | 90m |
| 87 | Information theory | ① entropy·KL divergence·mutual information ② Shannon's theorem | 75m |
| 88 | **Phase 8 synthesis** | measure → integral → probability → stochastic — the uncertainty chain | 90m |

---

## Phase 9: Modern Tools of Computation & Optimization (11 sessions, 16.75h)

> **Core question:** "When an exact answer is impossible, how do we get a close-enough one?"

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 89 | Numerical linear algebra | ① LU·QR·SVD algorithms ② Jacobi·Gauss–Seidel·CG iteration | 75m |
| 90 | Convex optimization: basics | ① convex sets·convex functions ② $\nabla f=0$ = optimum ③ KKT conditions | 90m |
| 91 | Gradient descent·Newton's method | ① GD·SGD·momentum·Adam ② Newton: quadratic convergence | 60m |
| 92 | Numerical ODE methods | ① Euler·RK4·Butcher tableaux ② stiffness·A-stability·adaptive steps | 75m |
| 93 | Numerical PDE: overview | ① finite differences·finite elements ② CFL·von Neumann stability | 120m |
| 94 | Fourier analysis (discrete·fast) | ① DFT→$O(N^2)$ ② FFT→$O(N\log N)$ ③ Shannon sampling | 75m |
| 95 | Wavelets·compressed sensing | ① Haar·multiresolution ② $\ell^1$-minimization recovery | 90m |
| 96 | Randomized algorithms·MCMC | ① Monte Carlo ② Metropolis–Hastings·Gibbs ③ convergence diagnostics | 120m |
| 97 | Mathematics of machine learning | ① ERM ② PAC-learning·VC dimension·Rademacher | 120m |
| 98 | Mathematics of neural networks | ① universal approximation ② backpropagation ③ NTK | 90m |
| 99 | **Phase 9 synthesis** | optimization → discretization → learning — the computation chain | 90m |

---

## Phase 10: The Frontier — 20th–21st Century Topics (12 sessions, 20.5h)

> **Core question:** "What lies beyond these tools?"

| # | Tool | Method procedure | Time |
|:--:|------|-----------|:---:|
| 100 | Functional analysis | ① Banach·Hilbert ② Hahn–Banach·open mapping ③ spectral theorem | 120m |
| 101 | Operator algebras·$C^*$-algebras | ① $B(H)$·Gelfand transform ② GNS construction ③ mathematical foundations of quantum mechanics | 120m |
| 102 | Algebraic geometry: intro | ① $V(I)$, Nullstellensatz ② coordinate ring·Zariski topology | 120m |
| 103 | Schemes·sheaves | ① define sheaves ② $\operatorname{Spec}R$ ③ the language of Grothendieck | 120m |
| 104 | Representation theory | ① $\rho:G\to\mathrm{GL}(V)$ ② irreducible representations·Schur·characters·character tables | 90m |
| 105 | Lie groups·Lie algebras | ① $\exp:\mathfrak{g}\to G$ ② Killing·Cartan·root systems ③ Dynkin diagrams | 120m |
| 106 | Advanced algebraic topology | ① spectral sequences ② characteristic classes ③ homotopy groups via Serre | 120m |
| 107 | Symplectic geometry·mirror symmetry | ① $\omega$·Darboux ② Hamiltonian mechanics ③ Gromov–Witten·mirror symmetry | 120m |
| 108 | Computational complexity·P vs NP | ① Turing machines·P·NP ② Cook–Levin·NP-completeness ③ barriers | 90m |
| 109 | Mathematics of quantum computing | ① qubits·quantum gates ② Shor·Grover ③ error correction | 120m |
| 110 | Random matrices·free probability | ① Wigner semicircle·Tracy–Widom ② Voiculescu free independence ③ connection to neural networks | 120m |
| 111 | **The Map of the Tool Inventor** | full tool dependency graph + open problems + what you will build | 90m |

---

## The Philosophy of This Curriculum

```
Mathematics is the history of tools that pierce problems.

Computation the hand remembers → justification by proof → inventing new tools → solving still more problems.

Phase 1: Forge the blade of logic.
Phase 2: Carve classical technique into the hand. (Proof comes later.)
Phase 3: Prove why those techniques work.
Phases 4–10: Build every modern tool on that foundation.

101 great tools, disassembled into manuals, over 111 sessions.
Which tool to build next is yours to decide.
```
