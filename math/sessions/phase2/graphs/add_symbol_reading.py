#!/usr/bin/env python3
"""Add English-only 'How to Read These Symbols' sections to all phase2 math files.
- Files that already have the section: convert Korean+English → English-only
- Files missing the section: add English-only section before Terminology/Today's Procedure"""

import re, os

BASE = '/home/rlawjddn/learning/math/sessions/phase2'

# ── Symbol definitions for each file ──────────────────────────
# Format: (symbol, reads_as, meaning)
SYMBOLS = {
    '07A-factoring-equations': [
        ('$x^n$', '"x to the n" / "x raised to the n-th power"', 'power / exponent form'),
        ('$a x^2 + b x + c = 0$', '"a x squared plus b x plus c equals zero"', 'quadratic equation (standard form)'),
        ('$x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$', '"x equals negative b plus or minus the square root of b squared minus 4 a c, all over 2 a"', 'quadratic formula'),
        ('$b^2-4ac$', '"b squared minus 4 a c" / "discriminant"', 'determines nature of roots (>0: two real, =0: one real, <0: complex)'),
        ('$(x-r)(x-s)=0$', '"x minus r times x minus s equals zero"', 'factored form — roots are r and s'),
        ('$a^2-b^2$', '"a squared minus b squared"', 'difference of squares — factors as (a-b)(a+b)'),
        ('$a^3 \\pm b^3$', '"a cubed plus or minus b cubed"', 'sum/difference of cubes'),
        ('$(x+a)^n$', '"x plus a, all to the n"', 'binomial expansion — use Pascal\'s triangle'),
        ('$\\pm$', '"plus or minus"', 'two possibilities: plus AND minus'),
        ('synthetic division', '"synthetic division"', 'fast polynomial division by (x-r)'),
        ('$\\sum r_i$', '"sum of r sub i" / "sum of roots"', 'Vieta: sum = -b/a'),
        ('$\\prod r_i$', '"product of r sub i" / "product of roots"', 'Vieta: product = (-1)^n a_0/a_n'),
    ],
    '07B-partial-fractions-systems': [
        ('$\\frac{P(x)}{Q(x)}$', '"P of x over Q of x"', 'rational function — polynomial divided by polynomial'),
        ('$\\frac{A}{x-a}$', '"A over x minus a"', 'partial fraction — linear factor term'),
        ('$\\frac{Ax+B}{x^2+bx+c}$', '"A x plus B over x squared plus b x plus c"', 'partial fraction — irreducible quadratic term'),
        ('$\\begin{cases} ax+by=e \\\\ cx+dy=f \\end{cases}$', '"system: a x plus b y equals e, c x plus d y equals f"', '2×2 linear system'),
        ('elimination', '"elimination" / "Gaussian elimination"', 'add/subtract equations to remove a variable'),
        ('substitution', '"substitution"', 'solve one equation for a variable, plug into the other'),
        ('$\\det = ad-bc$', '"determinant equals a d minus b c"', 'determines if system has unique solution (≠0)'),
        ('consistent / inconsistent', '"consistent" / "inconsistent"', 'has solution(s) / has no solution'),
        ('$n \\times n$', '"n by n"', 'square system with n equations and n unknowns'),
    ],
    '08A-inequalities-sign-charts': [
        ('$<$', '"less than"', 'strict inequality — endpoint NOT included'),
        ('$\\leq$', '"less than or equal to"', 'non-strict inequality — endpoint IS included'),
        ('$>$', '"greater than"', 'strict inequality'),
        ('$\\geq$', '"greater than or equal to"', 'non-strict inequality'),
        ('$(x-a)(x-b) < 0$', '"x minus a times x minus b less than zero"', 'quadratic inequality'),
        ('sign chart', '"sign chart" / "sign diagram"', 'number line divided at critical points; test each interval'),
        ('critical point / zero', '"critical point" / "zero"', 'where expression equals zero or is undefined'),
        ('interval notation', '"interval notation"', '$(a,b)$ = open, $[a,b]$ = closed, $(a,b]$ = half-open'),
        ('$\\cup$', '"union"', 'combine disjoint intervals'),
        ('$\\cap$', '"intersection"', 'common elements of intervals'),
        ('$|x| < a$', '"absolute value of x less than a"', 'equivalent to $-a < x < a$'),
        ('$|x| > a$', '"absolute value of x greater than a"', 'equivalent to $x < -a$ or $x > a$'),
    ],
    '08B-advanced-inequalities': [
        ('$\\frac{P(x)}{Q(x)} \\geq 0$', '"P of x over Q of x greater than or equal to zero"', 'rational inequality — watch denominator zeros'),
        ('$x \\neq a$', '"x not equal to a" / "x cannot be a"', 'excluded value — denominator cannot be zero'),
        ('quadratic in form', '"quadratic in form"', 'substitution $t = f(x)$ reduces to quadratic'),
        ('$\\sqrt{A} < B$', '"square root of A less than B"', 'requires $A \\geq 0$ AND squaring both sides'),
        ('AM-GM', '"A M G M" / "arithmetic mean - geometric mean inequality"', '$(a+b)/2 \\geq \\sqrt{ab}$ for $a,b \\geq 0$'),
        ('Cauchy-Schwarz', '"Cauchy-Schwarz inequality"', '$(a_1b_1+\\cdots)^2 \\leq (a_1^2+\\cdots)(b_1^2+\\cdots)$'),
        ('$\\pm\\infty$', '"plus or minus infinity"', 'unbounded direction on number line'),
    ],
    '9A1-function-fundamentals': [
        ('$f(x)$', '"f of x" / "the value of f at x"', 'function notation — input x, output f(x)'),
        ('domain', '"domain"', 'set of all valid inputs x'),
        ('range', '"range" / "image"', 'set of all possible outputs f(x)'),
        ('$f: A \\to B$', '"f maps A to B" / "f from A to B"', 'function with domain A, codomain B'),
        ('$f \\circ g$', '"f composed with g" / "f circle g"', 'composition: $(f \\circ g)(x) = f(g(x))$ — apply g first, then f'),
        ('$f^{-1}$', '"f inverse" / "the inverse of f"', 'undoes f: $f^{-1}(f(x)) = x$'),
        ('one-to-one / injective', '"one-to-one" / "injective"', 'each output comes from exactly one input — passes horizontal line test'),
        ('onto / surjective', '"onto" / "surjective"', 'every element of codomain is hit'),
        ('$f(x-h)$', '"f of x minus h"', 'shift RIGHT by h (counterintuitive!)'),
        ('$f(x)+k$', '"f of x plus k"', 'shift UP by k'),
        ('$-f(x)$', '"negative f of x"', 'reflect across x-axis'),
        ('$f(-x)$', '"f of negative x"', 'reflect across y-axis'),
        ('$a \\cdot f(x)$', '"a times f of x"', 'vertical stretch ($|a|>1$) or compression ($|a|<1$)'),
    ],
    '9A2-graph-drawing-toolkit': [
        ('intercepts', '"intercepts"', 'where graph crosses axes: x-intercept (y=0), y-intercept (x=0)'),
        ('asymptote', '"asymptote" / "AS-imp-tote"', 'line the graph approaches but never touches'),
        ('vertical asymptote', '"vertical asymptote" / "VA"', 'denominator = 0, function → ±∞'),
        ('horizontal asymptote', '"horizontal asymptote" / "HA"', 'end behavior as x → ±∞'),
        ('slant asymptote', '"slant asymptote" / "oblique"', 'degree of numerator = degree of denominator + 1'),
        ('increasing / decreasing', '"increasing" / "decreasing"', 'f\'(x)>0 / f\'(x)<0 — slope sign'),
        ('local maximum / minimum', '"local max" / "local min" / "turning point"', 'f\' changes sign (+→- for max, -→+ for min)'),
        ('concave up / down', '"concave up" / "concave down"', 'f\'\'(x)>0 = cup shape ∪, f\'\'(x)<0 = cap shape ∩'),
        ('inflection point', '"inflection point"', 'concavity changes — f\'\' changes sign'),
        ('symmetry', '"symmetry"', 'even: f(-x)=f(x) (y-axis mirror), odd: f(-x)=-f(x) (origin rotation)'),
    ],
    '9B-2d-functions-geometry': [
        ('$d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$', '"distance equals square root of x2 minus x1 squared plus y2 minus y1 squared"', 'distance formula'),
        ('$m = \\frac{y_2-y_1}{x_2-x_1}$', '"m equals y2 minus y1 over x2 minus x1" / "slope"', 'slope = rise over run'),
        ('$y = mx + b$', '"y equals m x plus b" / "slope-intercept form"', 'line: m=slope, b=y-intercept'),
        ('$y-y_1 = m(x-x_1)$', '"y minus y1 equals m times x minus x1"', 'point-slope form'),
        ('$Ax+By+C=0$', '"A x plus B y plus C equals zero"', 'general form of a line'),
        ('$(x-h)^2 + (y-k)^2 = r^2$', '"x minus h squared plus y minus k squared equals r squared"', 'circle: center (h,k), radius r'),
        ('$(x-h)^2/a^2 + (y-k)^2/b^2 = 1$', '"ellipse equation"', 'ellipse: a=semi-major, b=semi-minor'),
        ('$(x-h)^2/a^2 - (y-k)^2/b^2 = 1$', '"hyperbola equation"', 'hyperbola: opens left-right'),
        ('$y = ax^2+bx+c$', '"y equals a x squared plus b x plus c"', 'parabola: vertex at x=-b/(2a)'),
        ('$m_1 m_2 = -1$', '"m1 times m2 equals negative one"', 'perpendicular lines condition'),
        ('$\\theta = \\tan^{-1}(m)$', '"theta equals inverse tan of m"', 'angle of inclination'),
    ],
    '9C-3d-surfaces-geometry': [
        ('$z = f(x,y)$', '"z equals f of x y"', 'surface over the xy-plane — height at each point'),
        ('level curve / contour', '"level curve" / "contour line"', '$f(x,y)=c$ — horizontal slice through surface'),
        ('$x^2+y^2+z^2 = R^2$', '"x squared plus y squared plus z squared equals R squared"', 'sphere of radius R centered at origin'),
        ('$z = x^2 + y^2$', '"z equals x squared plus y squared"', 'paraboloid — bowl shape opening upward'),
        ('$z^2 = x^2 + y^2$', '"z squared equals x squared plus y squared"', 'double cone'),
        ('$x^2/a^2 + y^2/b^2 - z^2/c^2 = 1$', '"hyperboloid of one sheet"', 'cooling tower shape'),
        ('trace', '"trace" / "cross-section"', 'intersection of surface with a coordinate plane'),
        ('$xy$-plane, $xz$-plane, $yz$-plane', '"x y plane" / "x z plane" / "y z plane"', 'the three coordinate planes'),
        ('octant', '"octant"', 'one of 8 regions divided by the coordinate planes'),
        ('quadric surface', '"quadric surface"', 'surface defined by a second-degree equation in x, y, z'),
    ],
    '10A-exponents-logarithms-core': [
        ('$a^m$', '"a to the m" / "a raised to the m-th power"', 'exponentiation: base a, exponent m'),
        ('$a^m \\cdot a^n = a^{m+n}$', '"a to the m times a to the n equals a to the m plus n"', 'product rule — add exponents'),
        ('$(a^m)^n = a^{mn}$', '"a to the m, all to the n, equals a to the m n"', 'power of a power — multiply exponents'),
        ('$a^{-n} = 1/a^n$', '"a to the negative n equals one over a to the n"', 'negative exponent = reciprocal'),
        ('$a^{m/n} = \\sqrt[n]{a^m}$', '"a to the m over n equals the n-th root of a to the m"', 'fractional exponent = root'),
        ('$e$', '"e" / "Euler\'s number"', 'natural base ≈ 2.71828...'),
        ('$\\ln x$', '"natural log of x" / "ell-en of x"', 'logarithm base e — inverse of e^x'),
        ('$\\log_a x$', '"log base a of x"', 'logarithm: a^{\\log_a x} = x'),
        ('$\\log(MN) = \\log M + \\log N$', '"log of M N equals log M plus log N"', 'product property'),
        ('$\\log(M/N) = \\log M - \\log N$', '"log of M over N equals log M minus log N"', 'quotient property'),
        ('$\\log(M^k) = k\\log M$', '"log of M to the k equals k log M"', 'power property'),
        ('$e^{\\ln x} = x$', '"e to the natural log of x equals x"', 'exponential and natural log are inverses'),
    ],
    '10B-exponents-logarithms-advanced': [
        ('$b^x = e^{x \\ln b}$', '"b to the x equals e to the x natural log b"', 'change of base for exponentials'),
        ('$\\log_b a = \\frac{\\ln a}{\\ln b}$', '"log base b of a equals ln a over ln b"', 'change of base formula'),
        ('$a^x = b$', '"a to the x equals b"', 'exponential equation — take log of both sides'),
        ('$\\log_a(x+1) + \\log_a(x-1) = c$', '"log base a of x plus 1 plus log base a of x minus 1 equals c"', 'logarithmic equation — combine then exponentiate'),
        ('compound interest', '"compound interest"', '$A = P(1+r/n)^{nt}$ — interest added n times per year'),
        ('continuous compounding', '"continuous compounding"', '$A = Pe^{rt}$ — interest added continuously'),
        ('$t_2 = \\ln 2 / k$', '"t-two equals ln 2 over k" / "doubling time"', 'time for quantity to double under exponential growth'),
        ('$t_{1/2} = \\ln 2 / |k|$', '"t-half equals ln 2 over absolute k" / "half-life"', 'time for quantity to halve under exponential decay'),
        ('log-log plot', '"log-log plot"', 'both axes logarithmic — power laws appear as straight lines'),
        ('semi-log plot', '"semi-log plot"', 'y-axis logarithmic, x-axis linear — exponentials appear as straight lines'),
    ],
    '11A-trig-foundations': [
        ('$\\sin\\theta$', '"sine theta"', 'opposite / hypotenuse in right triangle; y-coordinate on unit circle'),
        ('$\\cos\\theta$', '"cosine theta"', 'adjacent / hypotenuse; x-coordinate on unit circle'),
        ('$\\tan\\theta$', '"tangent theta"', 'sin/cos = opposite/adjacent; slope of terminal ray'),
        ('$\\csc\\theta$', '"cosecant theta"', '1/sin — reciprocal of sine'),
        ('$\\sec\\theta$', '"secant theta"', '1/cos — reciprocal of cosine'),
        ('$\\cot\\theta$', '"cotangent theta"', '1/tan = cos/sin — reciprocal of tangent'),
        ('$\\pi$ rad = 180°', '"pi radians equals 180 degrees"', 'radian-degree conversion'),
        ('$\\sin^2\\theta + \\cos^2\\theta = 1$', '"sine squared theta plus cosine squared theta equals one"', 'Pythagorean identity'),
        ('$\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta$', '"sine two theta equals two sine theta cosine theta"', 'double-angle formula for sine'),
        ('$\\cos(2\\theta) = \\cos^2\\theta - \\sin^2\\theta$', '"cosine two theta equals cos squared theta minus sin squared theta"', 'double-angle formula for cosine'),
        ('$2\\pi$', '"two pi" / "tau"', 'period of sine and cosine (one full circle)'),
        ('$\\pi$', '"pi"', 'period of tangent'),
        ('$f(x) = A\\sin(Bx + C) + D$', '"A sine B x plus C plus D"', 'sinusoid: A=amplitude, 2π/B=period, -C/B=phase shift, D=vertical shift'),
    ],
    '11B-trig-advanced': [
        ('$\\sin(A\\pm B)$', '"sine of A plus or minus B"', 'sine addition formula: sinAcosB ± cosAsinB'),
        ('$\\cos(A\\pm B)$', '"cosine of A plus or minus B"', 'cosine addition formula: cosAcosB ∓ sinAsinB'),
        ('$\\tan(A\\pm B)$', '"tangent of A plus or minus B"', '(tanA ± tanB)/(1 ∓ tanA tanB)'),
        ('$\\sin^2\\theta = \\frac{1-\\cos2\\theta}{2}$', '"sine squared theta equals one minus cosine two theta over two"', 'power-reduction — used in integration'),
        ('$\\cos^2\\theta = \\frac{1+\\cos2\\theta}{2}$', '"cosine squared theta equals one plus cosine two theta over two"', 'power-reduction — used in integration'),
        ('$\\sin^{-1}x$, $\\cos^{-1}x$, $\\tan^{-1}x$', '"inverse sine of x" / "arcsine of x"', 'inverse trig — returns an angle'),
        ('$\\arcsin x$', '"arcsine of x"', 'alternative notation for sin^{-1}x (avoids confusion with 1/sin)'),
        ('Law of Sines', '"Law of Sines"', '$\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C}$'),
        ('Law of Cosines', '"Law of Cosines"', '$c^2 = a^2 + b^2 - 2ab\\cos C$ — generalizes Pythagorean theorem'),
        ('harmonic identity', '"harmonic identity" / "auxiliary angle method"', '$a\\sin x + b\\cos x = R\\sin(x+\\phi)$ where $R=\\sqrt{a^2+b^2}$'),
    ],
    '12A1-complex-numbers': [
        ('$i$', '"i" / "the imaginary unit"', '$i^2 = -1$ — fundamental imaginary number'),
        ('$z = a + bi$', '"z equals a plus b i"', 'complex number: a=real part, b=imaginary part'),
        ('$\\bar{z}$', '"z bar" / "z conjugate" / "complex conjugate"', '$\\overline{a+bi} = a - bi$ — flip sign of imaginary part'),
        ('$|z|$', '"modulus of z" / "absolute value of z" / "magnitude"', '$|a+bi| = \\sqrt{a^2+b^2}$ — distance from origin'),
        ('$\\operatorname{Re}(z)$', '"real part of z"', 'the a in a+bi'),
        ('$\\operatorname{Im}(z)$', '"imaginary part of z"', 'the b in a+bi (a real number — NOT bi!)'),
        ('$re^{i\\theta}$', '"r e to the i theta" / "polar form"', '$r=|z|$, $\\theta=\\arg(z)$ — polar/exponential form'),
        ('$\\arg(z)$', '"argument of z"', 'angle $\\theta$ from positive real axis'),
        ('Euler\'s formula', '"Euler\'s formula"', '$e^{i\\theta} = \\cos\\theta + i\\sin\\theta$'),
        ('De Moivre', '"De Moivre\'s theorem"', '$z^n = r^n e^{in\\theta} = r^n(\\cos n\\theta + i\\sin n\\theta)$'),
        ('$n$-th roots of unity', '"n-th roots of unity"', '$e^{2\\pi i k/n}$ for k=0,1,…,n-1 — equally spaced on unit circle'),
        ('complex plane / Argand diagram', '"complex plane" / "Argand diagram"', 'x-axis=real, y-axis=imaginary'),
    ],
    '12A2-matrices-vectors': [
        ('$\\vec{v} = \\langle v_1, v_2 \\rangle$', '"vector v equals angle-bracket v1 comma v2"', 'vector in component form'),
        ('$\\|\\vec{v}\\|$', '"magnitude of v" / "norm of v" / "length"', '$\\sqrt{v_1^2+v_2^2}$ — length of the arrow'),
        ('$\\vec{v} \\cdot \\vec{w}$', '"v dot w" / "dot product"', '$v_1w_1+v_2w_2$ — scalar result, related to cosine of angle'),
        ('$\\vec{v} \\cdot \\vec{w} = \\|\\vec{v}\\|\\|\\vec{w}\\|\\cos\\theta$', '"v dot w equals norm v times norm w times cosine theta"', 'geometric dot product formula'),
        ('$A = [a_{ij}]$', '"A equals matrix with entries a i j"', 'matrix: i=row index, j=column index'),
        ('$AB$', '"A times B" / "matrix product"', '$(AB)_{ij} = \\sum_k a_{ik}b_{kj}$ — row of A dot column of B'),
        ('$A^{-1}$', '"A inverse"', 'matrix inverse: $AA^{-1}=A^{-1}A=I$'),
        ('$I$', '"I" / "the identity matrix"', 'ones on diagonal, zeros elsewhere — like multiplying by 1'),
        ('$\\det(A)$', '"determinant of A"', '$\\det = ad-bc$ for 2×2 — zero means singular (no inverse)'),
        ('$A^\\mathsf{T}$', '"A transpose"', 'rows become columns, columns become rows'),
        ('orthogonal', '"orthogonal"', '$\\vec{v}\\cdot\\vec{w}=0$ — perpendicular vectors'),
        ('$\\vec{0}$', '"zero vector"', 'vector with all components zero'),
    ],
    '12B-sequences-series': [
        ('$a_n$', '"a sub n" / "a n"', 'n-th term of a sequence'),
        ('$\\{a_n\\}_{n=1}^{\\infty}$', '"the sequence a n from n equals 1 to infinity"', 'infinite sequence notation'),
        ('$\\sum_{n=1}^{\\infty} a_n$', '"sum from n equals 1 to infinity of a n"', 'infinite series — sum of all terms'),
        ('$S_n = \\sum_{k=1}^{n} a_k$', '"S sub n equals sum from k equals 1 to n of a k"', 'n-th partial sum'),
        ('$\\lim_{n\\to\\infty} a_n = L$', '"limit as n goes to infinity of a n equals L"', 'sequence converges to L'),
        ('$a_n = a_1 + (n-1)d$', '"a n equals a1 plus n minus 1 d"', 'arithmetic sequence — constant difference d'),
        ('$a_n = a_1 r^{n-1}$', '"a n equals a1 times r to the n minus 1"', 'geometric sequence — constant ratio r'),
        ('$S_n = \\frac{n(a_1+a_n)}{2}$', '"S n equals n times a1 plus a n over 2"', 'arithmetic series sum'),
        ('$S_n = a_1\\frac{1-r^n}{1-r}$', '"S n equals a1 times one minus r to the n over one minus r"', 'geometric series sum (finite)'),
        ('$\\sum_{n=0}^{\\infty} ar^n = \\frac{a}{1-r}$', '"sum of a r to the n equals a over one minus r"', 'infinite geometric series — converges if |r|<1'),
        ('$\\sum_{k=1}^{n} k = \\frac{n(n+1)}{2}$', '"sum of first n integers equals n times n plus 1 over 2"', 'Gauss\'s formula'),
        ('$\\sum_{k=1}^{n} k^2 = \\frac{n(n+1)(2n+1)}{6}$', '"sum of first n squares"', 'sum of squares formula'),
        ('telescoping', '"telescoping"', 'series where intermediate terms cancel — only first and last survive'),
    ],
    '12C1-geometric-transformations': [
        ('translation', '"translation" / "shift"', 'move every point by the same vector — shape unchanged'),
        ('rotation', '"rotation"', 'spin around a point by angle θ — shape and size preserved'),
        ('reflection', '"reflection" / "mirror"', 'flip across a line — mirror image'),
        ('dilation / scaling', '"dilation" / "scaling"', 'stretch or shrink — size changes, shape preserved'),
        ('$T(\\vec{x}) = A\\vec{x} + \\vec{b}$', '"T of x equals A x plus b"', 'affine transformation: linear part + translation'),
        ('$R_\\theta$', '"R sub theta" / "rotation by theta"', '$\\begin{bmatrix}\\cos\\theta&-\\sin\\theta\\\\\\sin\\theta&\\cos\\theta\\end{bmatrix}$ — rotation matrix'),
        ('isometry', '"isometry" / "rigid motion"', 'distance-preserving transformation — rotation, reflection, translation'),
        ('congruent', '"congruent"', 'same size and shape — can be mapped by isometries'),
        ('similar', '"similar"', 'same shape, possibly different size — isometry + dilation'),
        ('$\\det A$', '"determinant of A"', 'area scaling factor of linear transformation'),
        ('eigenvalue / eigenvector', '"eigenvalue" / "eigenvector"', '$A\\vec{v}=\\lambda\\vec{v}$ — direction unchanged by transformation'),
    ],
    '12C2-parametric-curves-surfaces': [
        ('$\\vec{r}(t) = \\langle x(t), y(t) \\rangle$', '"r of t equals angle-bracket x of t comma y of t"', 'parametric curve — position at time t'),
        ('$\\vec{r}\\,\'(t)$', '"r prime of t" / "velocity vector"', 'derivative of position — tangent direction'),
        ('$\\|\\vec{r}\\,\'(t)\\|$', '"speed" / "magnitude of velocity"', 'how fast the point moves — scalar'),
        ('$\\vec{T}(t) = \\vec{r}\\,\'/\\|\\vec{r}\\,\'\\|$', '"T of t equals r prime over its magnitude"', 'unit tangent vector'),
        ('$\\vec{N}(t)$', '"N of t" / "unit normal"', 'perpendicular to tangent — points toward center of curvature'),
        ('$\\kappa(t)$', '"kappa of t" / "curvature"', 'how sharply the curve bends — 1/radius of curvature'),
        ('$L = \\int_a^b \\|\\vec{r}\\,\'(t)\\|\\,dt$', '"arc length equals integral of speed"', 'length of curve from t=a to t=b'),
        ('$\\vec{r}(u,v) = \\langle x(u,v), y(u,v), z(u,v) \\rangle$', '"r of u v"', 'parametric surface — two parameters sweep a surface'),
        ('tangent plane', '"tangent plane"', 'spanned by $\\vec{r}_u$ and $\\vec{r}_v$ — best flat approximation to surface'),
    ],
    '12C3-coordinate-systems-optimization': [
        ('$x = r\\cos\\theta$, $y = r\\sin\\theta$', '"x equals r cosine theta, y equals r sine theta"', 'polar → rectangular conversion'),
        ('$r = \\sqrt{x^2+y^2}$', '"r equals square root of x squared plus y squared"', 'distance from origin in polar'),
        ('$\\theta = \\tan^{-1}(y/x)$', '"theta equals inverse tangent of y over x"', 'angle from positive x-axis'),
        ('$x = \\rho\\sin\\phi\\cos\\theta$', '"x equals rho sine phi cosine theta"', 'spherical → rectangular (x)'),
        ('$y = \\rho\\sin\\phi\\sin\\theta$', '"y equals rho sine phi sine theta"', 'spherical → rectangular (y)'),
        ('$z = \\rho\\cos\\phi$', '"z equals rho cosine phi"', 'spherical → rectangular (z)'),
        ('$\\rho$', '"rho"', 'distance from origin (spherical) — NOT same as polar r'),
        ('$\\phi$', '"phi"', 'angle from positive z-axis: 0 at north pole, π at south pole'),
        ('$x = r\\cos\\theta$, $y = r\\sin\\theta$, $z = z$', '"x equals r cosine theta, y equals r sine theta, z equals z"', 'cylindrical coordinates — polar in xy + z'),
        ('$dA = r\\,dr\\,d\\theta$', '"d A equals r d r d theta"', 'polar area element — Jacobian = r'),
        ('$dV = \\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$', '"d V equals rho squared sine phi d rho d phi d theta"', 'spherical volume element'),
    ],
    '13A-algebraic-limits': [
        ('$\\lim_{x \\to a} f(x)$', '"limit as x approaches a of f of x"', 'value f(x) gets arbitrarily close to as x nears a'),
        ('$\\frac{0}{0}$', '"zero over zero" / "indeterminate form"', 'cannot evaluate directly — factor, rationalize, or use known limits'),
        ('$\\frac{\\infty}{\\infty}$', '"infinity over infinity"', 'indeterminate — divide numerator and denominator by highest power'),
        ('$\\frac{\\sin x}{x} \\to 1$', '"sine x over x goes to 1 as x goes to 0"', 'fundamental trigonometric limit'),
        ('$\\frac{e^x-1}{x} \\to 1$', '"e to the x minus 1 over x goes to 1"', 'fundamental exponential limit'),
        ('conjugate', '"conjugate"', '$\\sqrt{A}+\\sqrt{B}$ is conjugate of $\\sqrt{A}-\\sqrt{B}$ — multiply to remove radicals'),
        ('$\\lim_{x \\to a^-}$', '"limit as x approaches a from the left" / "left-hand limit"', 'approach a from smaller values'),
        ('$\\lim_{x \\to a^+}$', '"limit as x approaches a from the right" / "right-hand limit"', 'approach a from larger values'),
        ('DNE', '"does not exist"', 'limit does not exist — left ≠ right, or infinite oscillation'),
        ('$\\infty$', '"infinity"', 'unbounded growth — NOT a number, notation meaning "grows without bound"'),
        ('hole / removable discontinuity', '"hole" / "removable discontinuity"', 'limit exists but function value is different or undefined'),
    ],
    '13B-limits-at-infinity': [
        ('$\\lim_{x \\to \\infty} f(x) = L$', '"limit as x goes to infinity of f of x equals L"', 'horizontal asymptote at y = L'),
        ('$\\lim_{x \\to -\\infty} f(x) = L$', '"limit as x goes to negative infinity"', 'end behavior as x → -∞'),
        ('$\\deg(P) < \\deg(Q)$', '"degree of P less than degree of Q"', 'rational function → 0 as x → ±∞'),
        ('$\\deg(P) = \\deg(Q)$', '"degrees equal"', 'limit = ratio of leading coefficients'),
        ('$\\deg(P) > \\deg(Q)$', '"degree of P greater than degree of Q"', 'limit = ±∞ — check leading coefficient signs'),
        ('leading coefficient', '"leading coefficient"', 'coefficient of highest-degree term — dominates at infinity'),
        ('$\\frac{\\ln x}{x} \\to 0$', '"ln x over x goes to zero as x goes to infinity"', 'logarithm grows slower than any positive power'),
        ('$\\frac{x}{e^x} \\to 0$', '"x over e to the x goes to zero"', 'exponential dominates any polynomial'),
        ('slant asymptote', '"slant asymptote" / "oblique asymptote"', 'deg(num) = deg(den)+1 — polynomial long division gives line'),
        ('end behavior model', '"end behavior model"', 'leading term dominates — ignore lower-order terms at infinity'),
    ],
    '13C-continuity-theorems': [
        ('continuous at $x=a$', '"continuous at x equals a"', 'limit = f(a) — no break, jump, or hole'),
        ('$\\lim_{x\\to a} f(x) = f(a)$', '"limit as x goes to a of f of x equals f of a"', 'continuity definition — three conditions in one'),
        ('IVT', '"I V T" / "Intermediate Value Theorem"', 'continuous function on [a,b] hits every value between f(a) and f(b)'),
        ('EVT', '"E V T" / "Extreme Value Theorem"', 'continuous function on closed [a,b] attains absolute max and min'),
        ('$[a,b]$', '"closed interval a b"', 'includes endpoints — required for EVT'),
        ('$(a,b)$', '"open interval a b"', 'excludes endpoints — EVT does NOT apply here'),
        ('jump discontinuity', '"jump discontinuity"', 'left and right limits exist but are different'),
        ('removable discontinuity', '"removable discontinuity"', 'limit exists — could be "fixed" by redefining f(a)'),
        ('infinite discontinuity', '"infinite discontinuity" / "vertical asymptote"', 'function → ±∞ at the point'),
        ('oscillating discontinuity', '"oscillating discontinuity"', 'sin(1/x) near 0 — no limit, infinite oscillation'),
        ('$C^0$, $C^1$, $C^2$', '"C zero, C one, C two"', 'C^0=continuous, C^1=continuously differentiable, C^2=second derivative continuous'),
    ],
    '14A-derivative-fundamentals': [
        ('$f\'(x)$', '"f prime of x"', 'derivative of f — instantaneous rate of change, slope of tangent'),
        ('$\\frac{dy}{dx}$', '"d y d x" / "derivative of y with respect to x"', 'Leibniz notation for derivative'),
        ('$\\frac{d}{dx}$', '"d d x" / "derivative operator"', 'take the derivative with respect to x'),
        ('$f\'(a) = \\lim_{h\\to0}\\frac{f(a+h)-f(a)}{h}$', '"f prime of a equals limit as h goes to zero of f of a plus h minus f of a over h"', 'limit definition of the derivative'),
        ('$\\frac{d}{dx}x^n = nx^{n-1}$', '"derivative of x to the n equals n x to the n minus 1"', 'power rule'),
        ('$\\frac{d}{dx}e^x = e^x$', '"derivative of e to the x equals e to the x"', 'e^x is its own derivative'),
        ('$\\frac{d}{dx}\\sin x = \\cos x$', '"derivative of sine x equals cosine x"', 'sine derivative'),
        ('$\\frac{d}{dx}\\cos x = -\\sin x$', '"derivative of cosine x equals negative sine x"', 'cosine derivative — note the minus sign'),
        ('$(f+g)\' = f\' + g\'$', '"f plus g prime equals f prime plus g prime"', 'sum rule — derivative of sum = sum of derivatives'),
        ('$(fg)\' = f\'g + fg\'$', '"f g prime equals f prime g plus f g prime"', 'product rule — NOT f\'g\'!'),
        ('$(f/g)\' = \\frac{f\'g - fg\'}{g^2}$', '"f over g prime equals f prime g minus f g prime over g squared"', 'quotient rule'),
        ('tangent line: $y - f(a) = f\'(a)(x-a)$', '"tangent line at a"', 'line that just touches the curve at exactly one point'),
    ],
    '14B-advanced-differentiation': [
        ('$\\frac{d}{dx}f(g(x)) = f\'(g(x)) \\cdot g\'(x)$', '"derivative of f of g of x equals f prime of g of x times g prime of x"', 'chain rule — differentiate outside, then multiply by inside derivative'),
        ('implicit differentiation', '"implicit differentiation"', 'differentiate both sides w.r.t. x, treat y as y(x), solve for dy/dx'),
        ('$\\frac{d}{dx}[\\ln f(x)] = \\frac{f\'(x)}{f(x)}$', '"derivative of ln f of x equals f prime of x over f of x"', 'logarithmic derivative'),
        ('logarithmic differentiation', '"logarithmic differentiation"', 'take ln of both sides first — useful for products/quotients/powers'),
        ('$\\frac{d}{dx}[f^{-1}(x)] = \\frac{1}{f\'(f^{-1}(x))}$', '"derivative of inverse function"', 'slope of inverse = reciprocal of slope at corresponding point'),
        ('$\\frac{dy}{dx} = \\frac{dy/dt}{dx/dt}$', '"d y d x equals d y d t over d x d t"', 'parametric derivative — chain rule with parameter t'),
        ('$\\frac{d}{dx}[a^x] = a^x \\ln a$', '"derivative of a to the x equals a to the x ln a"', 'exponential derivative for arbitrary base'),
        ('$\\frac{d}{dx}[\\log_a x] = \\frac{1}{x\\ln a}$', '"derivative of log base a of x"', 'logarithmic derivative for arbitrary base'),
        ('related rates', '"related rates"', 'two quantities change with time — relate their rates via implicit differentiation w.r.t. t'),
        ('$\\frac{dx}{dt}$', '"d x d t" / "rate of change of x with respect to time"', 'time derivative in related rates problems'),
    ],
    '14C-higher-derivatives': [
        ('$f\'\'(x)$', '"f double prime of x" / "second derivative"', 'derivative of derivative — rate of change of slope'),
        ('$f\'\'\'(x)$', '"f triple prime" / "third derivative"', 'derivative of second derivative — jerk in physics'),
        ('$f^{(n)}(x)$', '"f superscript n of x" / "n-th derivative"', 'higher-order derivative notation (for n > 3)'),
        ('$\\frac{d^2y}{dx^2}$', '"d two y d x squared" / "second derivative"', 'Leibniz notation for f\'\'(x)'),
        ('$\\frac{d^ny}{dx^n}$', '"d n y d x to the n" / "n-th derivative"', 'Leibniz notation for n-th derivative'),
        ('concavity', '"concavity"', 'f\'\'>0 = concave up (∪), f\'\'<0 = concave down (∩)'),
        ('inflection point', '"inflection point"', 'f\'\' changes sign — concavity flips'),
        ('Taylor polynomial', '"Taylor polynomial"', '$P_n(x) = \\sum_{k=0}^n \\frac{f^{(k)}(a)}{k!}(x-a)^k$ — polynomial that matches f and its first n derivatives at a'),
        ('jerk', '"jerk"', 'third derivative of position — rate of change of acceleration'),
        ('$C^n$', '"C n" / "n-times continuously differentiable"', 'first n derivatives exist and are continuous'),
    ],
    '15A-curve-analysis': [
        ('critical point', '"critical point"', 'f\'(x)=0 or f\'(x) undefined — candidate for extremum'),
        ('local maximum', '"local max" / "relative maximum"', 'highest point in its neighborhood — f\' changes + → −'),
        ('local minimum', '"local min" / "relative minimum"', 'lowest point in its neighborhood — f\' changes − → +'),
        ('absolute/global extremum', '"absolute max/min" / "global extremum"', 'highest/lowest point on the entire domain — check critical points AND endpoints'),
        ('$f\'(x) > 0$', '"f prime of x greater than zero"', 'function is increasing'),
        ('$f\'(x) < 0$', '"f prime of x less than zero"', 'function is decreasing'),
        ('$f\'\'(x) > 0$', '"f double prime greater than zero"', 'concave up ∪ — slope is increasing'),
        ('$f\'\'(x) < 0$', '"f double prime less than zero"', 'concave down ∩ — slope is decreasing'),
        ('first derivative test', '"first derivative test"', 'check sign of f\' on either side of critical point'),
        ('second derivative test', '"second derivative test"', 'f\'(a)=0, f\'\'(a)>0 → local min; f\'\'(a)<0 → local max; f\'\'(a)=0 → inconclusive'),
        ('MVT', '"M V T" / "Mean Value Theorem"', '$f\'(c) = [f(b)-f(a)]/(b-a)$ for some c in (a,b)'),
    ],
    '15B-optimization-related-rates': [
        ('optimization', '"optimization"', 'find maximum or minimum of a quantity'),
        ('objective function', '"objective function"', 'the quantity to maximize or minimize'),
        ('constraint', '"constraint"', 'relationship between variables — used to eliminate one variable'),
        ('feasible region', '"feasible region" / "domain"', 'all valid values satisfying constraints'),
        ('endpoint check', '"endpoint check"', 'evaluate objective at domain boundaries — extremum could occur there'),
        ('related rates', '"related rates"', 'find rate of change of one quantity from known rate of another'),
        ('$\\frac{d}{dt}$', '"d d t" / "time derivative"', 'differentiate with respect to time — key operator in related rates'),
        ('$\\frac{dV}{dt}$', '"d V d t" / "rate of change of volume"', 'example: filling/draining rate of a tank'),
        ('Pythagorean relation', '"Pythagorean relation"', '$x^2+y^2=z^2$ — common in distance-related problems'),
        ('similar triangles', '"similar triangles"', 'ratio-preserving — used to relate variables geometrically'),
    ],
    '16A-integration-fundamentals': [
        ('$\\int f(x)\\,dx$', '"integral of f of x d x" / "antiderivative"', 'indefinite integral — family of functions whose derivative is f'),
        ('$\\int_a^b f(x)\\,dx$', '"integral from a to b of f of x d x"', 'definite integral — net signed area under curve'),
        ('FTC', '"F T C" / "Fundamental Theorem of Calculus"', '$\\int_a^b f = F(b)-F(a)$ where $F\'=f$'),
        ('$\\int x^n\\,dx = \\frac{x^{n+1}}{n+1} + C$', '"integral of x to the n equals x to the n+1 over n+1 plus C"', 'power rule for integration — reverse of derivative power rule'),
        ('$+C$', '"plus C" / "constant of integration"', 'antiderivative is a family — all differ by a constant'),
        ('$u$-substitution', '"u substitution"', 'reverse chain rule: $u=g(x)$, $du=g\'(x)dx$'),
        ('$\\int e^x\\,dx = e^x + C$', '"integral of e to the x equals e to the x plus C"', 'exponential antiderivative'),
        ('$\\int \\frac{1}{x}\\,dx = \\ln|x| + C$', '"integral of one over x equals natural log of absolute x plus C"', 'produces natural log — absolute value essential'),
        ('$\\int \\sin x\\,dx = -\\cos x + C$', '"integral of sine x equals negative cosine x plus C"', 'note the minus sign — derivative of cos is -sin'),
        ('$\\int \\cos x\\,dx = \\sin x + C$', '"integral of cosine x equals sine x plus C"', 'cosine antiderivative'),
        ('Riemann sum', '"Riemann sum"', '$\\sum f(x_i^*)\\Delta x$ — approximates area with rectangles'),
    ],
    '16B-advanced-integration': [
        ('integration by parts', '"integration by parts"', '$\\int u\\,dv = uv - \\int v\\,du$ — reverse product rule'),
        ('LIATE', '"L I A T E" / "lee-ah-tay"', 'order for choosing u: Logarithmic, Inverse trig, Algebraic, Trig, Exponential'),
        ('$\\int \\sin^2 x\\,dx$', '"integral of sine squared x"', 'use power-reduction: $\\sin^2 x = (1-\\cos2x)/2$'),
        ('$\\int \\tan x\\,dx = \\ln|\\sec x| + C$', '"integral of tangent x equals ln absolute secant x plus C"', 'write as sin/cos, substitute u=cos x'),
        ('$\\int \\sec x\\,dx = \\ln|\\sec x + \\tan x| + C$', '"integral of secant x"', 'multiply top and bottom by sec x + tan x'),
        ('$\\sqrt{a^2-x^2}$', '"square root of a squared minus x squared"', 'trig substitution: $x = a\\sin\\theta$'),
        ('$\\sqrt{a^2+x^2}$', '"square root of a squared plus x squared"', 'trig substitution: $x = a\\tan\\theta$'),
        ('$\\sqrt{x^2-a^2}$', '"square root of x squared minus a squared"', 'trig substitution: $x = a\\sec\\theta$'),
        ('partial fractions', '"partial fractions"', 'decompose rational function into sum of simpler fractions'),
        ('completing the square', '"completing the square"', 'rewrite $ax^2+bx+c$ as $a(x-h)^2+k$ — used for arctan/arcsin integrals'),
    ],
    '17A-area-volume': [
        ('$\\int_a^b [f(x)-g(x)]\\,dx$', '"integral from a to b of f of x minus g of x d x"', 'area between curves — top minus bottom'),
        ('disk method', '"disk method"', '$V = \\pi\\int R(x)^2\\,dx$ — rotate region about axis, solid disk cross-sections'),
        ('washer method', '"washer method"', '$V = \\pi\\int (R^2 - r^2)\\,dx$ — hollow solid, outer radius R, inner radius r'),
        ('shell method', '"shell method"', '$V = 2\\pi\\int x\\,h(x)\\,dx$ — cylindrical shells, integrate parallel to axis'),
        ('$\\pi$', '"pi"', 'appears in volume formulas — area of circle = πr²'),
        ('cross-section', '"cross-section"', 'slice perpendicular to axis — basis for volume integration'),
        ('solid of revolution', '"solid of revolution"', '3D shape formed by rotating a 2D region around an axis'),
        ('$x$-axis / $y$-axis rotation', '"rotation about the x-axis" / "y-axis"', 'axis of revolution determines disk/washer/shell choice'),
        ('$\\Delta x$, $\\Delta y$', '"delta x" / "delta y"', 'thickness of slice — becomes dx or dy in the limit'),
    ],
    '17B-arc-length-improper': [
        ('$L = \\int_a^b \\sqrt{1+(y\')^2}\\,dx$', '"arc length equals integral from a to b of square root of one plus y prime squared d x"', 'length of curve y=f(x) from x=a to x=b'),
        ('$L = \\int_a^b \\sqrt{(dx/dt)^2+(dy/dt)^2}\\,dt$', '"arc length in parametric form"', 'length of parametric curve'),
        ('$\\int_a^\\infty f(x)\\,dx$', '"improper integral from a to infinity"', 'limit: $\\lim_{b\\to\\infty}\\int_a^b f(x)dx$ — infinite interval'),
        ('$\\int_a^b f(x)\\,dx$ with discontinuity', '"improper integral with a discontinuity"', 'limit at the point where integrand blows up'),
        ('convergent / divergent', '"convergent" / "divergent"', 'improper integral has finite value / does not'),
        ('$\\int_1^\\infty \\frac{1}{x^p}\\,dx$', '"integral from 1 to infinity of 1 over x to the p"', 'p-test: converges if p>1, diverges if p≤1'),
        ('comparison test', '"comparison test"', 'if 0 ≤ f(x) ≤ g(x) and ∫g converges, then ∫f converges'),
        ('surface of revolution', '"surface area of revolution"', '$S = 2\\pi\\int y\\sqrt{1+(y\')^2}\\,dx$ — rotate curve, find surface area'),
    ],
    '18A-series-convergence': [
        ('$\\sum_{n=1}^{\\infty} a_n$ converges', '"the series converges"', 'partial sums approach a finite limit'),
        ('$\\sum a_n$ diverges', '"the series diverges"', 'partial sums → ∞, −∞, or oscillate'),
        ('$\\lim_{n\\to\\infty} a_n \\neq 0$', '"limit of a n does not equal zero"', 'Divergence Test: if limit ≠ 0, series MUST diverge (but limit=0 does NOT guarantee convergence!)'),
        ('geometric series', '"geometric series"', '$\\sum ar^n$ — converges to $a/(1-r)$ if |r|<1'),
        ('$p$-series', '"p series"', '$\\sum 1/n^p$ — converges if p>1, diverges if p≤1'),
        ('Integral Test', '"integral test"', 'compare series to $\\int f(x)dx$ where $f(n)=a_n$ — same convergence behavior'),
        ('Comparison Test', '"comparison test" / "direct comparison"', 'term-by-term ≤ known series — if bigger converges, smaller also converges'),
        ('Limit Comparison Test', '"limit comparison test"', 'if $\\lim a_n/b_n = c > 0$ (finite), series share convergence fate'),
        ('Ratio Test', '"ratio test"', '$\\lim |a_{n+1}/a_n| = L$: L<1→converges, L>1→diverges, L=1→inconclusive'),
        ('Root Test', '"root test"', '$\\lim \\sqrt[n]{|a_n|} = L$ — same criteria as Ratio Test'),
        ('Alternating Series Test', '"alternating series test"', 'terms decrease to 0 in absolute value → converges'),
        ('absolutely / conditionally convergent', '"absolutely convergent" / "conditionally convergent"', '∑|a_n| converges / ∑|a_n| diverges but ∑a_n converges'),
    ],
    '18B-power-series': [
        ('$\\sum_{n=0}^{\\infty} c_n (x-a)^n$', '"power series centered at a"', 'infinite polynomial — function represented as series around a'),
        ('center', '"center" / "a"', 'point around which the power series is expanded'),
        ('radius of convergence $R$', '"radius of convergence"', 'series converges for |x-a|<R, diverges for |x-a|>R'),
        ('interval of convergence', '"interval of convergence"', '(a-R, a+R) — endpoints must be checked separately'),
        ('Ratio Test for $R$', '"ratio test for radius"', '$R = \\lim |c_n/c_{n+1}|$ if the limit exists'),
        ('term-by-term differentiation', '"term-by-term differentiation"', 'derivative of power series = sum of derivatives — valid inside radius'),
        ('term-by-term integration', '"term-by-term integration"', 'integral of power series = sum of integrals — valid inside radius'),
        ('$e^x = \\sum_{n=0}^{\\infty} \\frac{x^n}{n!}$', '"e to the x equals sum of x to the n over n factorial"', 'Maclaurin series for exponential — converges for all x'),
        ('analytic function', '"analytic function"', 'function that equals its power series in some interval'),
        ('singular point', '"singular point"', 'where function is not analytic — determines radius of convergence'),
    ],
    '18C-taylor-series': [
        ('Taylor series', '"Taylor series"', '$f(x) = \\sum_{n=0}^{\\infty} \\frac{f^{(n)}(a)}{n!}(x-a)^n$ — infinite polynomial matching all derivatives at a'),
        ('Maclaurin series', '"Maclaurin series"', 'Taylor series centered at a=0 — special case'),
        ('$n!$', '"n factorial"', 'product 1×2×3×...×n — grows extremely fast'),
        ('$\\sin x = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\cdots$', '"sine x equals x minus x cubed over 3 factorial plus x to the fifth over 5 factorial minus ..."', 'Maclaurin series for sine — odd powers, alternating signs'),
        ('$\\cos x = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\cdots$', '"cosine x equals one minus x squared over 2 factorial plus ..."', 'Maclaurin series for cosine — even powers, alternating signs'),
        ('$e^x = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\cdots$', '"e to the x equals one plus x plus x squared over 2 factorial ..."', 'Maclaurin series for exponential — all positive'),
        ('$\\frac{1}{1-x} = 1 + x + x^2 + x^3 + \\cdots$', '"one over one minus x equals one plus x plus x squared ..."', 'geometric series — converges for |x|<1'),
        ('$\\ln(1+x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\cdots$', '"ln of one plus x equals x minus x squared over 2 plus x cubed over 3 ..."', 'Maclaurin series for natural log — alternating, converges for -1<x≤1'),
        ('Lagrange remainder', '"Lagrange remainder"', '$R_n = \\frac{f^{(n+1)}(\\xi)}{(n+1)!}(x-a)^{n+1}$ — bounds error of Taylor polynomial'),
        ('$|R_n| \\leq \\frac{M}{(n+1)!}|x-a|^{n+1}$', '"absolute remainder less than or equal to M over n+1 factorial times x minus a to the n+1"', 'error bound — M = max of |f^{(n+1)}| on the interval'),
    ],
    '19A-ode-modeling': [
        ('$\\frac{dy}{dx}$', '"d y d x" / "the derivative of y with respect to x"', 'instantaneous rate of change, slope'),
        ('$y\'$', '"y prime"', 'shorthand for dy/dx'),
        ('$\\frac{dP}{dt}$', '"d P d t" / "the rate of change of P"', 'time derivative — how P changes per unit time'),
        ('$\\int$', '"integral"', 'integration symbol — finds area, accumulation'),
        ('$e^{kt}$', '"e to the k t"', 'exponential function — e ≈ 2.718, base of natural growth/decay'),
        ('$\\ln$', '"natural log" / "ell-en"', 'logarithm base e — inverse of e^x'),
        ('$\\lim$', '"limit"', 'limit — value approached, not necessarily reached'),
        ('$t_{1/2}$', '"t-half" / "half-life"', 'time for quantity to decrease by half'),
        ('$t_2$', '"t-two" / "doubling time"', 'time for quantity to double'),
        ('$k$', '"k" / "rate constant"', 'growth (k>0) or decay (k<0) rate'),
        ('$L$', '"L" / "carrying capacity"', 'upper bound in logistic growth — saturation level'),
        ('$C$', '"C" / "constant of integration"', 'arbitrary constant — determined by initial condition'),
        ('$T_{\\text{env}}$', '"T env" / "environment temperature"', 'ambient temperature in Newton cooling'),
    ],
    '19B-first-order-solution': [
        ('$\\frac{dy}{dx} = g(x)h(y)$', '"d y d x equals g of x times h of y"', 'separable ODE — split y and x to opposite sides'),
        ('$\\int \\frac{dy}{h(y)}$', '"integral of d y over h of y"', 'integration with respect to y after separation'),
        ('$y\' + P(x)y = Q(x)$', '"y prime plus P of x y equals Q of x"', 'standard form of a first-order linear ODE'),
        ('$\\mu(x)$', '"mu of x" / "integrating factor"', 'μ = e^{∫P dx} — multiplies ODE to make left side an exact derivative'),
        ('$\\frac{d}{dx}(\\mu y)$', '"d d x of mu y"', 'derivative of product — left side becomes this after multiplying by μ'),
        ('$\\ln|y|$', '"natural log of absolute y"', 'absolute value is essential — domain of ln is positive numbers only'),
        ('$y \\equiv 0$', '"y is identically zero"', 'zero everywhere — the trivial equilibrium solution'),
        ('$\\lim_{t\\to\\infty}$', '"limit as t goes to infinity"', 'long-term behavior of the solution'),
        ('equilibrium', '"equilibrium" / "steady state"', 'constant solution where y\'=0 — no change over time'),
        ('separable / linear', '"separable" / "linear"', 'ODE classification — determines solution method'),
    ],
    '19C-advanced-first-order': [
        ('$v = \\frac{y}{x}$', '"v equals y over x"', 'substitution for homogeneous equations — y = xv'),
        ('$\\frac{dy}{dx} = F(\\frac{y}{x})$', '"d y d x equals F of y over x"', 'homogeneous ODE — depends only on ratio y/x'),
        ('$y\' + P(x)y = Q(x)y^n$', '"y prime plus P y equals Q y to the n"', 'Bernoulli equation — nonlinear, reduces to linear via v = y^{1-n}'),
        ('$v = y^{1-n}$', '"v equals y to the one minus n"', 'Bernoulli substitution — transforms to linear ODE in v'),
        ('$M(x,y)dx + N(x,y)dy = 0$', '"M d x plus N d y equals zero"', 'standard form for exact ODE'),
        ('$\\frac{\\partial M}{\\partial y}$', '"partial M partial y" / "M sub y"', 'partial derivative of M with respect to y'),
        ('$M_y = N_x$', '"M sub y equals N sub x"', 'exactness condition — partial derivatives match'),
        ('$\\phi(x,y)$', '"phi of x y" / "potential function"', 'scalar function whose gradient gives the vector field ⟨M,N⟩'),
        ('$\\mu(x)$, $\\mu(y)$', '"mu of x" / "integrating factor"', 'factor making a non-exact ODE exact'),
        ('orthogonal trajectories', '"orthogonal trajectories"', 'curves intersecting a given family at right angles'),
        ('Riccati', '"Riccati" / "ree-CAH-tee"', 'y\' = P y² + Q y + R — nonlinear, needs one known solution'),
    ],
    '19D-higher-order-numerical': [
        ('$y\'\'$', '"y double prime" / "second derivative"', 'acceleration — rate of change of slope'),
        ('$ay\'\'+by\'+cy=0$', '"a y double prime plus b y prime plus c y equals zero"', 'second-order linear homogeneous ODE'),
        ('$r$', '"r" / "characteristic root"', 'root of ar²+br+c=0 — determines solution form'),
        ('$i$', '"i" / "the imaginary unit"', 'i² = −1 — appears in complex roots for oscillatory solutions'),
        ('$e^{\\alpha x}(c_1\\cos\\beta x + c_2\\sin\\beta x)$', '"e to the alpha x times c1 cosine beta x plus c2 sine beta x"', 'solution for complex roots α±iβ — damped/growing oscillation'),
        ('$c_1, c_2$', '"c one, c two" / "arbitrary constants"', 'determined by initial conditions'),
        ('$\\omega$', '"omega" / "angular frequency"', 'ω = 2πf = 2π/T — radians per unit time'),
        ('$T = 2\\pi/\\omega$', '"T equals two pi over omega"', 'period — time for one complete cycle'),
        ('$h$', '"h" / "step size"', 'Euler method step — smaller h = better accuracy'),
        ('$y_{n+1} = y_n + h f(x_n, y_n)$', '"y n+1 equals y n plus h times f of x n, y n"', 'Euler method — one step of slope-following'),
        ('$O(h^2)$', '"big-O of h squared"', 'local truncation error proportional to h²'),
        ('RK2', '"R K two" / "Runge-Kutta second order"', 'improved Euler — averages slopes for better accuracy'),
        ('overdamped / critically damped / underdamped', '"overdamped" / "critically damped" / "underdamped"', 'three damping regimes: no oscillation / fastest return / decaying oscillation'),
    ],
    '19E-linear-systems-phase-portraits': [
        ('$\\dot{\\vec{x}}$', '"x dot"', 'time derivative of state vector — dx/dt'),
        ('$\\dot{\\vec{x}} = A\\vec{x}$', '"x dot equals A x"', 'linear dynamical system in state-space form'),
        ('$A$', '"A" / "system matrix"', 'coefficient matrix — n×n for n-dimensional system'),
        ('$\\lambda$', '"lambda" / "eigenvalue"', 'growth/decay rate + oscillation frequency — λ = α ± iβ'),
        ('$\\vec{v}$', '"v" / "eigenvector"', 'direction of pure exponential motion — A v = λ v'),
        ('$\\det(A-\\lambda I)$', '"determinant of A minus lambda I"', 'characteristic polynomial — roots are eigenvalues'),
        ('$\\tau = \\operatorname{tr}(A)$', '"tau equals trace of A"', 'sum of diagonal = sum of eigenvalues: τ = λ₁ + λ₂'),
        ('$\\Delta = \\det(A)$', '"Delta equals determinant of A"', 'product of eigenvalues: Δ = λ₁·λ₂'),
        ('$J$', '"J" / "Jacobian matrix"', 'J_{ij} = ∂F_i/∂x_j — linearization of nonlinear system at equilibrium'),
        ('$\\vec{F}(\\vec{x})$', '"F of x" / "vector field"', 'right-hand side of nonlinear system ẋ = F(x)'),
        ('$\\vec{x}^*$', '"x star" / "equilibrium point"', 'F(x*) = 0 — system at rest'),
        ('saddle / node / spiral / center', '"saddle" / "node" / "spiral" / "center"', 'six canonical 2D phase portraits determined by eigenvalues'),
        ('Hartman-Grobman', '"Hartman-Grobman theorem"', 'near equilibrium, nonlinear phase portrait ≈ linearized portrait'),
    ],
    '20-epsilon-delta-rigorous-limits': [
        ('$\\forall$', '"for all" / "for every"', 'universal quantifier — applies to every element'),
        ('$\\exists$', '"there exists" / "for some"', 'existential quantifier — at least one element'),
        ('$\\Rightarrow$', '"implies" / "then"', 'logical implication — if left holds, right must hold'),
        ('$\\varepsilon$', '"epsilon"', 'output tolerance — an arbitrarily small positive number'),
        ('$\\delta$', '"delta"', 'input window radius — chosen based on ε'),
        ('$\\lim_{x \\to a} f(x) = L$', '"limit as x approaches a of f of x equals L"', 'ε-δ definition: for every ε>0, there exists δ>0 such that...'),
        ('$0 < |x-a| < \\delta$', '"zero less than absolute x minus a less than delta"', 'x is within δ of a, but x ≠ a — the point itself is excluded'),
        ('$|f(x)-L| < \\varepsilon$', '"absolute f of x minus L less than epsilon"', 'f(x) is within ε of the limit L'),
        ('$\\lceil x \\rceil$', '"ceiling of x"', 'smallest integer ≥ x — used in ε-N to pick integer N'),
        ('$\\neg$', '"not" / "negation"', 'logical negation — flips truth value'),
        ('$N \\in \\mathbb{N}$', '"N in the natural numbers"', 'N is a natural number (1, 2, 3, ...)'),
        ('Cauchy criterion', '"Cauchy criterion"', '∀ε ∃N ∀m,n≥N: |a_m−a_n|<ε — sequence converges iff Cauchy'),
    ],
    '21-continuity-derivatives-rigorous': [
        ('$f\'(a)$', '"f prime of a"', 'derivative at a — slope of tangent line'),
        ('$\\frac{d}{dx}$', '"d d x" / "derivative operator"', 'take the derivative with respect to x'),
        ('$(f+g)\' = f\' + g\'$', '"f plus g prime equals f prime plus g prime"', 'sum rule — derivative distributes over addition'),
        ('$(fg)\' = f\'g + fg\'$', '"f g prime equals f prime g plus f g prime"', 'product rule — NOT simply f\'g\'!'),
        ('$(1/g)\' = -g\'/g^2$', '"one over g prime equals negative g prime over g squared"', 'reciprocal rule — special case of quotient rule'),
        ('$(f \\circ g)\' = f\'(g) \\cdot g\'$', '"f composed with g prime equals f prime of g times g prime"', 'chain rule — differentiate outer, multiply by inner derivative'),
        ('IVT', '"I V T" / "Intermediate Value Theorem"', 'continuous f on [a,b] hits every value between f(a) and f(b)'),
        ('EVT', '"E V T" / "Extreme Value Theorem"', 'continuous f on closed [a,b] attains max and min'),
        ('$C^0, C^1, C^2$', '"C zero, C one, C two"', 'C⁰=continuous, C¹=continuously differentiable, C²=second derivative continuous'),
        ('removable / jump / essential', '"removable" / "jump" / "essential"', 'three discontinuity types: hole, step, infinite oscillation'),
    ],
    '22-mvt-ftc-taylor-proofs': [
        ('$\\exists c$', '"there exists c"', 'theorem guarantees existence of a point c — not necessarily unique'),
        ('$f\'(c) = \\frac{f(b)-f(a)}{b-a}$', '"f prime of c equals f of b minus f of a over b minus a"', 'MVT: instantaneous slope equals average slope at some c'),
        ('$\\int_a^b f(x)\\,dx$', '"integral from a to b of f of x d x"', 'definite integral — net signed area on [a,b]'),
        ('$F\'(x) = f(x)$', '"F prime of x equals f of x"', 'FTC Part 1: derivative of accumulation function is the integrand'),
        ('$P_n(x)$', '"P n of x" / "Taylor polynomial"', 'degree-n polynomial matching f and its first n derivatives at a'),
        ('$R_n(x)$', '"R n of x" / "remainder"', 'error term — the difference f(x) − P_n(x)'),
        ('$f^{(n)}$', '"f superscript n" / "n-th derivative"', 'f^{(4)} = fourth derivative — parentheses distinguish from power'),
        ('$O((x-a)^{n+1})$', '"big-O of x minus a to the n+1"', 'remainder decays at least as fast as (x-a)^{n+1}'),
        ('$\\equiv$', '"identically equals"', 'equality holding for all x — stronger than ='),
        ('Rolle\'s Theorem', '"Rolle\'s theorem"', 'f(a)=f(b) ⇒ ∃c with f\'(c)=0 — special case of MVT'),
        ('Cauchy MVT', '"Cauchy Mean Value Theorem"', 'generalizes MVT to two functions — foundation of L\'Hôpital and Taylor proofs'),
    ],
    '23A-multivariable-limits-continuity': [
        ('$\\lim_{(x,y)\\to(a,b)}$', '"limit as x y approaches a b"', 'multivariable limit — must be same along ALL paths to exist'),
        ('$\\mathbb{R}^2$', '"R two" / "the plane"', 'two-dimensional real space — all ordered pairs (x,y)'),
        ('$r$', '"r" / "radial distance"', 'distance from origin: r = √(x²+y²)'),
        ('$\\theta$', '"theta"', 'angle from positive x-axis in polar coordinates'),
        ('$x = r\\cos\\theta$, $y = r\\sin\\theta$', '"x equals r cosine theta, y equals r sine theta"', 'polar-to-rectangular conversion'),
        ('two-path test', '"two-path test"', 'find two paths giving different limits → limit DNE'),
        ('polar squeeze', '"polar squeeze"', 'convert to (r,θ), show expression → 0 as r→0 regardless of θ'),
        ('$f(x,y)$', '"f of x y"', 'function of two variables — height z over each point (x,y)'),
        ('level curve', '"level curve" / "contour"', 'f(x,y)=c — horizontal slice through the surface'),
    ],
    '23B-multivariable-partials-gradient': [
        ('$\\frac{\\partial f}{\\partial x}$', '"partial f partial x" / "del f del x"', 'derivative with respect to x, treating y as constant'),
        ('$f_x$', '"f sub x"', 'shorthand for ∂f/∂x'),
        ('$\\nabla f$', '"grad f" / "del f" / "gradient"', 'vector of all partial derivatives: ∇f = ⟨f_x, f_y⟩'),
        ('$D_{\\vec{u}}f$', '"d sub u f" / "directional derivative"', 'rate of change in direction of unit vector u — D_u f = ∇f·u'),
        ('$f_{xy}$', '"f sub x y" / "mixed partial"', 'differentiate first with respect to x, then y'),
        ('$f_{xx}$', '"f sub x x"', 'second partial with respect to x — differentiate twice'),
        ('$\\nabla^2 f$', '"del squared f" / "Laplacian"', 'f_{xx} + f_{yy} — sum of all second partials'),
        ('$|\\nabla f|$', '"magnitude of grad f"', 'maximum rate of change — steepness of the steepest path'),
        ('Clairaut\'s Theorem', '"Clairaut\'s theorem" / "Clair-OH"', 'f_{xy} = f_{yx} when mixed partials are continuous — order doesn\'t matter'),
        ('tangent plane', '"tangent plane"', 'z = f(a,b) + ∇f(a,b)·⟨x−a, y−b⟩ — best flat approximation to surface'),
    ],
    '24A-multivariable-chain-implicit': [
        ('$\\frac{dz}{dt}$', '"d z d t" / "total derivative"', 'z ultimately depends only on t — use d, not ∂'),
        ('$\\frac{\\partial z}{\\partial u}$', '"partial z partial u"', 'partial derivative when z depends on multiple variables'),
        ('$\\nabla F$', '"grad F" / "del F"', 'gradient of F(x,y,z) — normal vector to level surface'),
        ('$\\frac{dy}{dx} = -\\frac{F_x}{F_y}$', '"d y d x equals negative F sub x over F sub y"', 'implicit differentiation formula for F(x,y)=0'),
        ('$\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z}$', '"partial z partial x equals negative F_x over F_z"', 'implicit partial for surface F(x,y,z)=0'),
        ('$J$', '"J" / "Jacobian"', 'matrix of all first-order partial derivatives — chain rule = matrix multiplication'),
        ('tree diagram', '"tree diagram"', 'visual dependency graph — sum over all paths from output to input'),
        ('$\\nabla F \\cdot \\langle x-x_0, y-y_0, z-z_0 \\rangle = 0$', '"grad F dot displacement vector equals zero"', 'tangent plane to implicit surface — gradient is normal vector'),
    ],
    '24B-multivariable-optimization-lagrange': [
        ('$\\nabla f = \\vec{0}$', '"grad f equals the zero vector"', 'critical point condition — both partial derivatives vanish'),
        ('$D = f_{xx}f_{yy} - f_{xy}^2$', '"D equals f x x times f y y minus f x y squared"', 'second derivative discriminant — D>0 extremum, D<0 saddle'),
        ('$D>0, f_{xx}>0$', '"D greater than zero, f x x greater than zero"', 'local minimum — bowl shape opening upward'),
        ('$D>0, f_{xx}<0$', '"D greater than zero, f x x less than zero"', 'local maximum — hill shape'),
        ('$D<0$', '"D less than zero"', 'saddle point — curves up in one direction, down in another'),
        ('$\\nabla f = \\lambda \\nabla g$', '"grad f equals lambda grad g"', 'Lagrange multiplier condition — gradients are parallel'),
        ('$\\lambda$', '"lambda" / "Lagrange multiplier"', 'shadow price — rate of change of optimum per unit relaxation of constraint'),
        ('$g(x,y) = c$', '"g of x y equals c"', 'constraint equation — the curve the optimum must lie on'),
        ('Hessian', '"Hessian"', 'matrix of second partials — eigenvalues determine min/max/saddle'),
        ('saddle point', '"saddle point"', 'critical point that is neither min nor max — Hessian has both positive and negative eigenvalues'),
    ],
    '25A-double-integrals-fubini': [
        ('$\\iint_D f\\,dA$', '"double integral over D of f d A"', 'integral over 2D region — volume under surface'),
        ('$dA$', '"d A" / "area element"', 'dA = dx dy = dy dx — infinitesimal area piece'),
        ('$\\int_a^b\\int_{g_1(x)}^{g_2(x)} f\\,dy\\,dx$', '"integral a to b, integral g1 to g2, f dy dx"', 'iterated integral — inner first (y), then outer (x)'),
        ('$dy\\,dx$', '"dy dx" / "integrate y first, then x"', 'Type I: vertical strips — outer limits are constants'),
        ('$dx\\,dy$', '"dx dy" / "integrate x first, then y"', 'Type II: horizontal strips — outer limits are constants'),
        ('Fubini', '"Fubini" / "foo-BEE-nee"', 'theorem: order of integration can be swapped for continuous functions'),
        ('Type I region', '"type one region"', 'vertical strips: a≤x≤b, g₁(x)≤y≤g₂(x)'),
        ('Type II region', '"type two region"', 'horizontal strips: c≤y≤d, h₁(y)≤x≤h₂(y)'),
    ],
    '25B-triple-integrals-coordinates': [
        ('$\\iiint_E f\\,dV$', '"triple integral over E of f d V"', 'integral over 3D region — hypervolume under a 3D graph, or mass with density f'),
        ('$dV$', '"d V" / "volume element"', 'depends on coordinate system — must include Jacobian'),
        ('$r\\,dr\\,d\\theta$', '"r d r d theta"', 'polar area element — Jacobian = r'),
        ('$r\\,dr\\,d\\theta\\,dz$', '"r d r d theta d z"', 'cylindrical volume element — Jacobian = r'),
        ('$\\rho^2\\sin\\phi\\,d\\rho\\,d\\phi\\,d\\theta$', '"rho squared sine phi d rho d phi d theta"', 'spherical volume element — Jacobian = ρ² sin φ'),
        ('$\\rho$', '"rho"', 'distance from origin (spherical) — not the same as polar/cylindrical r'),
        ('$\\phi$', '"phi"', 'angle from positive z-axis: 0=north pole, π/2=equator, π=south pole'),
        ('$\\theta$', '"theta"', 'azimuthal angle in xy-plane: 0 to 2π'),
        ('$\\left|\\frac{\\partial(x,y)}{\\partial(u,v)}\\right|$', '"absolute Jacobian" / "absolute value of partial x y over partial u v"', 'area scaling factor for coordinate transformation — determinant of Jacobian matrix'),
        ('$\\det J$', '"determinant of J"', 'determinant of Jacobian matrix — gives local volume/area stretch factor'),
    ],
    '25C-vector-calculus-theorems': [
        ('$\\int_C \\vec{F}\\cdot d\\vec{r}$', '"line integral over C of F dot d r"', 'work done by vector field F along curve C'),
        ('$\\oint_C$', '"closed line integral" / "circulation"', 'line integral around a closed loop'),
        ('$\\nabla\\times\\vec{F}$', '"curl of F" / "del cross F"', 'vector field rotation — local vorticity, measures circulation density'),
        ('$\\nabla\\cdot\\vec{F}$', '"divergence of F" / "del dot F"', 'scalar spreading rate — measures flux density, source/sink strength'),
        ('$\\iint_S \\vec{F}\\cdot d\\vec{S}$', '"surface integral of F dot d S"', 'flux through surface S — amount of field passing through'),
        ('$d\\vec{S}$', '"d S vector" / "surface element vector"', 'magnitude = area, direction = outward normal'),
        ('$\\iiint_E (\\nabla\\cdot\\vec{F})\\,dV$', '"triple integral of divergence F d V"', 'total divergence inside volume — equals flux through boundary'),
        ('Green', '"Green\'s theorem"', '∮_C = ∬_D (Q_x−P_y) dA — 2D: circulation = curl over area'),
        ('Stokes', '"Stokes\' theorem"', '∮_C = ∬_S (∇×F)·dS — 3D surface: circulation = curl flux'),
        ('Divergence / Gauss', '"Divergence theorem" / "Gauss\'s theorem"', '∬_S = ∭_E (∇·F) dV — flux = total divergence'),
        ('$\\partial M$', '"boundary of M"', '∂M = boundary of region M — unified FTC: ∫_{∂M} = ∫_M (derivative)'),
    ],
    '25D-conservative-fields-potentials': [
        ('$\\oint\\vec{F}\\cdot d\\vec{r} = 0$', '"closed line integral of F dot d r equals zero"', 'definition of conservative field — zero work around any closed loop'),
        ('$\\vec{F} = \\nabla\\phi$', '"F equals grad phi"', 'field is gradient of a scalar potential — conservative (on simply connected region)'),
        ('$\\nabla\\times\\vec{F} = \\vec{0}$', '"curl of F equals zero vector"', 'curl test — zero curl ⇔ conservative (on simply connected domain)'),
        ('$\\phi$', '"phi" / "scalar potential"', 'potential function — gravity: U, electrostatics: V'),
        ('$\\vec{A}$', '"A" / "vector potential"', 'B = ∇×A — used in electromagnetism since ∇·B=0 always'),
        ('$\\nabla\\cdot\\vec{F}$', '"divergence of F"', 'div E = ρ/ε₀ — Gauss\'s law in differential form'),
        ('$\\nabla^2$', '"del squared" / "Laplacian"', '∇² = ∇·∇ — ∇²V = −ρ/ε₀ is Poisson\'s equation'),
        ('$\\vec{F} = -\\nabla U$', '"F equals negative grad U"', 'physics convention: force points downhill in potential — minus sign essential'),
        ('gauge freedom', '"gauge freedom"', 'U→U+C, A→A+∇χ — physics unchanged, choose convenient form'),
        ('simply connected', '"simply connected"', 'no holes — any loop can shrink to a point. Required for curl=0 ⇒ conservative'),
        ('$\\delta(\\vec{r})$', '"delta of r" / "Dirac delta"', 'point source distribution — represents point charge or point mass'),
    ],
    '25E-fourier-series-transform': [
        ('$a_n, b_n$', '"a n, b n" / "Fourier coefficients"', 'amplitudes of cosine (a_n) and sine (b_n) harmonics'),
        ('$\\sum_{n=1}^{\\infty}$', '"sum from n equals 1 to infinity"', 'infinite series — add contributions from all harmonics'),
        ('$\\omega$', '"omega" / "angular frequency"', 'ω = 2πf — radians per second'),
        ('$\\omega_0$', '"omega zero" / "fundamental frequency"', 'ω₀ = 2π/T — fundamental angular frequency'),
        ('$\\hat{f}(\\omega)$', '"f hat of omega"', 'Fourier transform — frequency-domain representation'),
        ('$\\mathcal{F}\\{f(t)\\}$', '"script F of f of t" / "Fourier transform of f"', 'Fourier transform operator'),
        ('$c_n$', '"c n" / "complex Fourier coefficient"', 'c_n = (1/T)∫ f e^{-i n ω₀ t} dt — complex form'),
        ('$\\operatorname{sinc}(x)$', '"sinc of x" / "sink of x"', 'sin(πx)/(πx) — Fourier transform of a rectangular pulse'),
        ('$\\delta(t)$', '"delta of t" / "Dirac delta"', 'unit impulse — zero everywhere except t=0, integral = 1'),
        ('$f * g$', '"f convolved with g" / "convolution"', '(f∗g)(t) = ∫ f(τ)g(t−τ)dτ — FT converts convolution to multiplication'),
        ('Parseval', '"Parseval\'s theorem"', 'total energy in time domain = total energy in frequency domain'),
        ('FWHM', '"F W H M" / "full width at half maximum"', 'peak width measured at half its maximum height'),
        ('$\\Delta t \\cdot \\Delta\\omega \\geq \\frac{1}{2}$', '"delta t times delta omega greater than or equal to one-half"', 'time-frequency uncertainty principle — Gaussian saturates this bound'),
    ],
    '25F-pde-separation-of-variables': [
        ('$\\frac{\\partial u}{\\partial t}$', '"partial u partial t"', 'time derivative — x is held constant'),
        ('$\\nabla^2 u$', '"del squared u" / "Laplacian of u"', 'u_{xx}+u_{yy} (2D) or u_{xx}+u_{yy}+u_{zz} (3D) — diffusion/equilibrium operator'),
        ('$u(x,t) = X(x)T(t)$', '"u equals X of x times T of t"', 'separation of variables ansatz — product form assumption'),
        ('$\\lambda$', '"lambda" / "separation constant" / "eigenvalue"', 'connects spatial and temporal ODEs — determined by boundary conditions'),
        ('$X\'\' + \\lambda X = 0$', '"X double prime plus lambda X equals zero"', 'spatial eigenvalue problem — solutions are sines, cosines, or exponentials'),
        ('$X_n(x) = \\sin(n\\pi x/L)$', '"X n of x equals sine of n pi x over L"', 'eigenfunction — standing wave shape for mode n'),
        ('$\\sinh$', '"hyperbolic sine" / "sinch"', 'sinh x = (e^x−e^{−x})/2 — appears in Laplace equation solutions'),
        ('$\\cosh$', '"hyperbolic cosine" / "cosh"', 'cosh x = (e^x+e^{−x})/2 — appears in Laplace equation solutions'),
        ('$J_m$', '"J sub m" / "Bessel function of order m"', 'radial solution in cylindrical/spherical coordinates — vibration of drum head'),
        ('Sturm-Liouville', '"Sturm-Liouville" / "S L problem"', 'general theory of eigenvalue problems — guarantees orthogonal eigenfunctions'),
        ('$\\delta(x)$', '"delta of x" / "Dirac delta"', 'point source — represents concentrated initial heat or charge'),
        ('Dirichlet / Neumann', '"Dirichlet" / "Neumann"', 'boundary condition types: specify function value / specify derivative value'),
    ],
}

# ── Update existing bilingual sections to English-only ─────
def update_existing(filepath, symbols):
    """Replace the 'How to Read' table in a file that already has one."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the existing table
    start_marker = '## How to Read These Symbols\n\n| Symbol | Reads as | Meaning |'
    end_marker = '\n---\n\n## Terminology'

    if start_marker not in content:
        print(f'  WARNING: {filepath} has no How to Read section (unexpected)')
        return False

    # Build new table
    table_lines = ['## How to Read These Symbols\n', '\n', '| Symbol | Reads as | Meaning |\n', '|:---:|:---:|------|\n']
    for sym, reads, meaning in symbols:
        table_lines.append(f'| {sym} | {reads} | {meaning} |\n')

    new_table = ''.join(table_lines)

    # Replace from start marker to end marker
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        # fallback: find the next '## Terminology'
        end_idx = content.find('\n## Terminology', start_idx)
        if end_idx == -1:
            print(f'  ERROR: cannot find end of How to Read section in {filepath}')
            return False

    new_content = content[:start_idx] + new_table + '\n' + content[end_idx:]

    with open(filepath, 'w') as f:
        f.write(new_content)
    return True


def add_new(filepath, symbols):
    """Add a new 'How to Read' section before ## Terminology or ## Today's Procedure."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Find insertion point: prefer before ## Terminology, else before last ## Today's Procedure
    marker = '## Terminology'
    idx = content.rfind(marker)
    if idx == -1:
        marker = '## Today\'s Procedure'
        idx = content.rfind(marker)
    if idx == -1:
        print(f'  ERROR: no Terminology or Today\'s Procedure in {filepath}')
        return False

    # Build new table
    table_lines = ['## How to Read These Symbols\n', '\n', '| Symbol | Reads as | Meaning |\n', '|:---:|:---:|------|\n']
    for sym, reads, meaning in symbols:
        table_lines.append(f'| {sym} | {reads} | {meaning} |\n')

    new_section = ''.join(table_lines) + '\n---\n\n'

    new_content = content[:idx] + new_section + content[idx:]

    with open(filepath, 'w') as f:
        f.write(new_content)
    return True


# ── Main ─────────────────────────────────────────────────────
def main():
    # Files that already have the section (need English-only update)
    existing_files = [
        '19A-ode-modeling', '19B-first-order-solution', '19C-advanced-first-order',
        '19D-higher-order-numerical', '19E-linear-systems-phase-portraits',
        '20-epsilon-delta-rigorous-limits', '21-continuity-derivatives-rigorous',
        '22-mvt-ftc-taylor-proofs', '23A-multivariable-limits-continuity',
        '23B-multivariable-partials-gradient', '24A-multivariable-chain-implicit',
        '24B-multivariable-optimization-lagrange', '25A-double-integrals-fubini',
        '25B-triple-integrals-coordinates', '25C-vector-calculus-theorems',
        '25D-conservative-fields-potentials', '25E-fourier-series-transform',
        '25F-pde-separation-of-variables',
    ]

    # Files that need the section added
    new_files = [k for k in SYMBOLS if k not in existing_files]

    count_updated = 0
    count_added = 0

    for fname in existing_files:
        filepath = os.path.join(BASE, fname + '.md')
        if not os.path.exists(filepath):
            print(f'  MISSING: {filepath}')
            continue
        syms = SYMBOLS.get(fname, [])
        if not syms:
            print(f'  NO SYMBOLS defined for {fname}')
            continue
        if update_existing(filepath, syms):
            count_updated += 1
            print(f'  UPDATED: {fname} ({len(syms)} symbols → English-only)')

    for fname in new_files:
        filepath = os.path.join(BASE, fname + '.md')
        if not os.path.exists(filepath):
            print(f'  MISSING: {filepath}')
            continue
        syms = SYMBOLS.get(fname, [])
        if not syms:
            print(f'  NO SYMBOLS defined for {fname}')
            continue
        if add_new(filepath, syms):
            count_added += 1
            print(f'  ADDED: {fname} ({len(syms)} symbols)')

    print(f'\n=== Done: {count_updated} updated, {count_added} added ===')

if __name__ == '__main__':
    main()
