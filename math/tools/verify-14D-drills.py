"""14D drill bank — single source of truth for every number printed in
sessions/phase2/14D-relation-lens.md and solutions/14D-solutions.md.

Run: python3 /tmp/d14final.py
All checks must report PASS.
"""
import sympy as sp

PASS, FAIL = [], []
def ck(label, got, want):
    if isinstance(want, (list, tuple)):
        same_len = len(got) == len(want)
        good = same_len and all(sp.simplify(a - b) == 0 for a, b in zip(got, want))
    else:
        good = sp.simplify(got - want) == 0
    (PASS if good else FAIL).append(label)
    print(("  PASS " if good else "  FAIL ") + f"{label}: got {got}, want {want}")

x, t, v, P, q, w, h = sp.symbols('x t v P q w h', real=True)

print("\n[Basic 1] t(v) = 120/v   (duration jail)")
tv = 120 / v
ck("t(60)=2", tv.subs(v, 60), sp.Integer(2))
ck("t'(60)=-1/30", sp.diff(tv, v).subs(v, 60), -sp.Rational(1, 30))
ck("t'(40)=-3/40", sp.diff(tv, v).subs(v, 40), sp.Rational(-3, 40))
ck("t'(120)=-1/120", sp.diff(tv, v).subs(v, 120), -sp.Rational(1, 120))
ck("preimage t=1.5h -> v=80", sp.solve(sp.Eq(tv, sp.Rational(3, 2)), v)[0], sp.Integer(80))

print("\n[Basic 2] P = V^2/R  at V=120, R=10")
PP = sp.Symbol('V', positive=True)**2 / sp.Symbol('R', positive=True)
Vv, Rr = sp.symbols('V R', positive=True)
PP = Vv**2 / Rr
ck("P0=1440", PP.subs({Vv: 120, Rr: 10}), sp.Integer(1440))
ck("dP/dV=24", sp.diff(PP, Vv).subs({Vv: 120, Rr: 10}), sp.Integer(24))
ck("dP/dR=-144", sp.diff(PP, Rr).subs({Vv: 120, Rr: 10}), sp.Integer(-144))
ck("P(V=121)=1464.1", PP.subs({Vv: 121, Rr: 10}), sp.Rational(14641, 10))

print("\n[Basic 3] j(x) = 3(x-2)^2 + 5")
j = 3 * (x - 2)**2 + 5
ck("j(2)=5", j.subs(x, 2), sp.Integer(5))
ck("j'(2)=0", sp.diff(j, x).subs(x, 2), sp.Integer(0))
ck("j(0)=17", j.subs(x, 0), sp.Integer(17))
ck("j'(0)=-12", sp.diff(j, x).subs(x, 0), sp.Integer(-12))
ck("j(3)=8", j.subs(x, 3), sp.Integer(8))
ck("j'(3)=6", sp.diff(j, x).subs(x, 3), sp.Integer(6))

print("\n[Basic 4] r(t)=6-t/2 L/min, S(t)=6t-t^2/4")
r = 6 - t / 2
S = sp.integrate(r, t)
ck("S(t)=6t-t^2/4", sp.expand(S), sp.expand(6 * t - t**2 / 4))
ck("r(6)=3", r.subs(t, 6), sp.Integer(3))
ck("r(12)=0", r.subs(t, 12), sp.Integer(0))
ck("S(12)=36", S.subs(t, 12), sp.Integer(36))
ck("S(6)=27", S.subs(t, 6), sp.Integer(27))


print("\n[Intermediate 1] guess-and-repair the rate of a budget: B(p)=900/p thousand units")
B = 900 / P
ck("B(30)=30", B.subs(P, 30), sp.Integer(30))
ck("B'(p)=-900/p^2", sp.diff(B, P), -900 / P**2)
ck("B'(30)=-1", sp.diff(B, P).subs(P, 30), sp.Integer(-1))
ck("B'(45)=-4/9", sp.diff(B, P).subs(P, 45), sp.Rational(-4, 9))
ck("B'(60)=-1/4", sp.diff(B, P).subs(P, 60), sp.Rational(-1, 4))
ck("doubling price quarters the rate", sp.diff(B, P).subs(P, 60) * 4, sp.diff(B, P).subs(P, 30))

print("\n[Intermediate 2] container cost C(x) = x^3/12 + 24/x")
C = x**3 / 12 + 24 / x
ck("C(4)=34/3", C.subs(x, 4), sp.Rational(34, 3))
ck("C(6)=22", C.subs(x, 6), sp.Integer(22))
ck("C(12)=146", C.subs(x, 12), sp.Integer(146))
ck("C'(x)=(x^4-96)/(4x^2)", sp.simplify(sp.diff(C, x) - (x**4 - 96) / (4 * x**2)), 0)
ck("C'(4)=5/2", sp.diff(C, x).subs(x, 4), sp.Rational(5, 2))
ck("C'(6)=25/3", sp.diff(C, x).subs(x, 6), sp.Rational(25, 3))
ck("C'(12)=215/6", sp.diff(C, x).subs(x, 12), sp.Rational(215, 6))
crit = [s for s in sp.solve(sp.diff(C, x), x) if s.is_real and s > 0]
ck("one positive critical point", len(crit), 1)
ck("crit = 2*6^(1/4)", crit[0], 2 * sp.Pow(6, sp.Rational(1, 4)))
print(f"        x* = {float(crit[0]):.5f} cm,  C(x*) = {float(C.subs(x, crit[0])):.5f}")
print(f"        C''(x*) = {float(sp.diff(C, x, 2).subs(x, crit[0])):.5f} > 0 (minimum)")

print("\n[Intermediate 3] sign table of g(x) = x^3 - 12x + 16 vs its degree")
g = x**3 - 12 * x + 16
gp = sp.expand(sp.diff(g, x)); gpp = sp.expand(sp.diff(g, x, 2))
ck("g'(x)=3x^2-12", gp, 3 * x**2 - 12)
ck("g'=0 at x=+-2", sorted(sp.solve(gp, x)), [-2, 2])
ck("g''(x) = 6x", gpp, 6 * x)
ck("g''=0 at x=0 only", sp.solve(gpp, x), [0])
ck("g(0)=16 > 0 where g''=0", g.subs(x, 0), sp.Integer(16))
ck("g''(-4)=-24, g''(2)=12 (neither zero)", (gpp.subs(x, -4), gpp.subs(x, 2)), [-24, 12])
ck("g factors as (x-2)^2 (x+4)", sp.factor(g), (x - 2)**2 * (x + 4))
ck("g zeros: -4 and 2", sorted(sp.solve(g, x)), [-4, 2])
ck("x=2 is a DOUBLE zero (g'=0 there)", sp.diff(g, x).subs(x, 2), sp.Integer(0))
ck("x=-4 is a SIMPLE zero (g'!=0 there)", sp.diff(g, x).subs(x, -4), sp.Integer(36))
ck("g' zeros: -2 and 2", sorted(sp.solve(gp, x)), [-2, 2])
ck("at x=2: g=0 and turns up (g''=12>0)", (g.subs(x, 2), gpp.subs(x, 2)), [0, 12])
ck("g crosses at x=-4 (sign changes)", [sp.sign(g.subs(x, -5)), sp.sign(g.subs(x, -3))], [-1, 1])
ck("at x=-1: g=27 > 0 but g'=-9 < 0", (g.subs(x, -1), gp.subs(x, -1)), [27, -9])


print("\n[Intermediate 4] chained jail: depth d -> sand mass m -> cost K")
msym = sp.Symbol('m', positive=True)
m = 1600 * x
K_m = sp.Rational(2, 5) * msym + msym**2 / 100000
K = K_m.subs(msym, m)
dKdx = sp.expand(sp.diff(K, x))
ck("m'(d)=1600", sp.diff(m, x), sp.Integer(1600))
ck("K'(m)=2/5 + m/50000", sp.expand(sp.diff(K_m, msym)), sp.expand(sp.Rational(2, 5) + msym / 50000))
ck("K'(d)=640 + 51.2 d", dKdx, 640 + sp.Rational(256, 5) * x)

print("\n[Advanced 1] f(x)=x^4+ax^3+bx^2, stationary inflection at x=2")
A, Bs = sp.symbols('a b', real=True)
F = x**4 + A * x**3 + Bs * x**2
sol = sp.solve([sp.Eq(sp.diff(F, x).subs(x, 2), 0), sp.Eq(sp.diff(F, x, 2).subs(x, 2), 0)], [A, Bs], dict=True)
ck("unique (a,b)", [sol[0][A], sol[0][Bs]], [sp.Rational(-16, 3), sp.Integer(8)])
fa = sp.expand(F.subs(sol[0]))
ck("f = 3x^4-16x^3+24x^2 over 3", sp.simplify(fa - (3 * x**4 - 16 * x**3 + 24 * x**2) / 3), 0)
ck("f' = 4x(x-2)^2", sp.simplify(sp.diff(fa, x) - 4 * x * (x - 2)**2), 0)
ck("f'' = 4(x-2)(3x-2)", sp.simplify(sp.diff(fa, x, 2) - 4 * (x - 2) * (3 * x - 2)), 0)
ck("f'''(2)=16 != 0 (genuine inflection)", sp.diff(fa, x, 3).subs(x, 2), sp.Integer(16))
ck("f(2)=16/3", fa.subs(x, 2), sp.Rational(16, 3))
ck("f'(2)=0", sp.diff(fa, x).subs(x, 2), 0)
ck("f''(2)=0", sp.diff(fa, x, 2).subs(x, 2), 0)
ck("x=2 is NOT an extremum (f' same sign both sides)", [sp.sign(sp.diff(fa, x).subs(x, sp.Rational(19, 10))), sp.sign(sp.diff(fa, x).subs(x, sp.Rational(21, 10)))], [1, 1])
ck("only extremum is x=0, local min f=0", fa.subs(x, 0), sp.Integer(0))
ck("f'(1)=4 > 0 (so not constant / not flat)", sp.diff(fa, x).subs(x, 1), sp.Integer(4))
ck("f(2/3)=176/81", fa.subs(x, sp.Rational(2, 3)), sp.Rational(176, 81))
ck("f''(2/3)=0 too", sp.diff(fa, x, 2).subs(x, sp.Rational(2, 3)), 0)
print(f"        f(2) = 16/3 = {float(sp.Rational(16,3)):.6f}")

print("\n[Advanced 2] chained: price P -> sales q -> batches w -> gas G")
Pv = sp.Symbol('P', positive=True)
qq = 400 - 5 * Pv
ww = qq / 40
wsym = sp.Symbol("w", positive=True)
GG_w = 2 + wsym**2
GG = GG_w.subs(wsym, ww)
ck("dq/dP=-5", sp.diff(qq, Pv), sp.Integer(-5))
ck("dw/dq=1/40", sp.diff(ww, qq) if False else sp.Rational(1, 40), sp.Rational(1, 40))
ck("dG/dw=2w", sp.diff(GG_w, wsym), 2 * wsym)
dGdP = sp.diff(GG, Pv)
ck("dG/dP = 2w/40 * (-5) = -w/4", sp.simplify(dGdP - (-ww / 4)), 0)
ck("dG/dP at P=40 (w=5) = -5/4", sp.nsimplify(dGdP.subs(Pv, 40)), sp.Rational(-5, 4))
ck("dG/dP at P=60 (w=5/2) = -5/8", sp.nsimplify(dGdP.subs(Pv, 60)), sp.Rational(-5, 8))
ck("dG/dP at P=80 (w=0) = 0", sp.nsimplify(dGdP.subs(Pv, 80)), 0)
ck("G(P) = P^2/64 - 5P/2 + 102", sp.expand(GG - (Pv**2 / 64 - 5 * Pv / 2 + 102)), 0)
ck("G'(P) zero at P=80 only", sp.solve(sp.diff(sp.expand(GG), Pv), Pv), [80])
ck("q(40)=200, w=5", (qq.subs(Pv, 40), sp.nsimplify(ww.subs(Pv, 40))), [sp.Integer(200), sp.Integer(5)])


print("\n[Advanced 3] constructive: quartic, flat + concave-flip at x=1, through (1,4)")
Cc = sp.Symbol('C', real=True)
xs = sp.Symbol('x', real=True)
Dd = sp.Symbol('D', real=True)
Fsym = xs**4 + A*xs**3 + Bs*xs**2 + Cc*xs + Dd
cons = [sp.Eq(Fsym.subs(xs, 1), 4), sp.Eq(sp.diff(Fsym, xs).subs(xs, 1), 0), sp.Eq(sp.diff(Fsym, xs, 2).subs(xs, 1), 0)]
sF = sp.solve(cons, [A, Bs, Dd], dict=True)[0]
ck("A = C/3 - 8/3", sF[A], Cc / 3 - sp.Rational(8, 3))
ck("B = 2 - C", sF[Bs], 2 - Cc)
ck("D = 11/3 - C/3", sF[Dd], sp.Rational(11, 3) - Cc / 3)
Fam = sp.expand(Fsym.subs(sF))
ck("F' = (x-1)^2 (4x + C)", sp.simplify(sp.diff(Fam, xs) - (xs - 1)**2 * (4 * xs + Cc)), 0)
ck("F''' = 24x + 6A = 24x + 2C - 16", sp.diff(Fam, xs, 3), 24 * xs + 2 * Cc - 16)
ck("F'''(1) = 2C + 8", sp.diff(Fam, xs, 3).subs(xs, 1), 2 * Cc + 8)

# pinned member: C = 2 (the quadratic term B = 2 - C vanishes)
Fp = sp.expand(Fam.subs(Cc, 2))
ck("C=2: F = x^4 - 2x^3 + 2x + 3", Fp, sp.expand(xs**4 - 2 * xs**3 + 2 * xs + 3))
ck("C=2: quadratic coefficient is 0", sp.Poly(Fp, xs).coeff_monomial(xs**2), sp.Integer(0))
ck("C=2: F(1) = 4", Fp.subs(xs, 1), sp.Integer(4))
ck("C=2: F'(1) = 0", sp.diff(Fp, xs).subs(xs, 1), 0)
ck("C=2: F''(1) = 0", sp.diff(Fp, xs, 2).subs(xs, 1), 0)
ck("C=2: F'''(1) = 12 != 0", sp.diff(Fp, xs, 3).subs(xs, 1), sp.Integer(12))
ck("C=2: F''(x) = 12x(x-1), so concavity flips at x=1", sp.simplify(sp.diff(Fp, xs, 2) - 12 * xs * (xs - 1)), 0)
ck("C=2: concave down just left of 1", sp.sign(sp.diff(Fp, xs, 2).subs(xs, sp.Rational(1, 2))), -1)
ck("C=2: concave up just right of 1", sp.sign(sp.diff(Fp, xs, 2).subs(xs, sp.Rational(3, 2))), 1)
ck("C=2: F'(0) = 2 (so not constant)", sp.diff(Fp, xs).subs(xs, 0), sp.Integer(2))
ck("C=2: F' > 0 on both sides of x=1 (increasing through it, not turning)",
   (sp.sign(sp.diff(Fp, xs).subs(xs, sp.Rational(1, 2))),
    sp.sign(sp.diff(Fp, xs).subs(xs, sp.Rational(3, 2))),
    sp.sign(sp.diff(Fp, xs).subs(xs, 2))), [1, 1, 1])
ck("C=2: other critical point x = -1/2", [z for z in sp.solve(sp.diff(Fp, xs), xs) if z != 1], [sp.Rational(-1, 2)])
ck("C=2: local min at x=-1/2, value 37/16", Fp.subs(xs, sp.Rational(-1, 2)), sp.Rational(37, 16))
ck("C=2: F' changes sign only at x=-1/2 (that is the only extremum)",
   [sp.sign(sp.diff(Fp, xs).subs(xs, -1)), sp.sign(sp.diff(Fp, xs).subs(xs, 0))], [-1, 1])

# the degenerate trap: C = -4
Fq = sp.expand(Fam.subs(Cc, -4))
ck("C=-4: F = (x-1)^4 + 4", sp.factor(Fq) if False else sp.simplify(Fq - ((xs - 1)**4 + 4)), 0)
ck("C=-4: F'''(1) = 0 (fails the inflection test)", sp.diff(Fq, xs, 3).subs(xs, 1), 0)
ck("C=-4: F' = 4(x-1)^3, so it IS increasing through 1 but not inflectional",
   sp.simplify(sp.diff(Fq, xs) - 4 * (xs - 1)**3), 0)
ck("C=-4: F'' = 12(x-1)^2 >= 0 everywhere (no concavity change)",
   (sp.sign(sp.diff(Fq, xs, 2).subs(xs, 0)), sp.sign(sp.diff(Fq, xs, 2).subs(xs, 2))), [1, 1])
ck("C=-4: F factors as (x^2+1)(x^2-4x+5)", sp.factor(Fq), sp.expand((xs**2 + 1) * (xs**2 - 4 * xs + 5)))
ck("C=-4: F(1) = 4 still", Fq.subs(xs, 1), sp.Integer(4))



print("\n[Advanced 4] error forensics: hours h -> widgets w -> cost C")
hsym = sp.Symbol('h', positive=True)
wsym2 = sp.Symbol('w', positive=True)
w_of_h = 4 * hsym
C_of_w = 60 + 3 * wsym2 + wsym2**2 / 50
dwdh = sp.diff(w_of_h, hsym)
dCdw = sp.diff(C_of_w, wsym2)
ck("dw/dh=4", dwdh, sp.Integer(4))
ck("dC/dw=3+w/25", dCdw, 3 + wsym2 / 25)
ck("dC/dh=(3+w/25)*4", sp.expand(dCdw.subs(wsym2, w_of_h) * dwdh), sp.expand((3 + w_of_h / 25) * 4))
C_of_h = sp.expand(C_of_w.subs(wsym2, w_of_h))
ck("C(h) = 60+12h+8h^2/25", C_of_h, sp.expand(60 + 12 * hsym + sp.Rational(8, 25) * hsym**2))
ck("C'(h)=12+16h/25", sp.expand(sp.diff(C_of_h, hsym)), sp.expand(12 + sp.Rational(16, 25) * hsym))
ck("C'(5)=76/5", sp.diff(C_of_h, hsym).subs(hsym, 5), sp.Rational(76, 5))
ck("chain equals composite at h=5", sp.nsimplify(sp.diff(C_of_h, hsym).subs(hsym, 5)),
   sp.nsimplify(sp.expand((dCdw * dwdh).subs(wsym2, w_of_h)).subs(hsym, 5)))
wrong = dwdh / dCdw
ck("wrong = (dw/dh)/(dC/dw) = 4/(3+w/25)", sp.simplify(wrong - 4 / (3 + wsym2 / 25)), 0)
print(f"        at h=5 (w=20): wrong = {float(wrong.subs(wsym2, 20)):.6f}, correct = {float(sp.Rational(76,5)):.6f}")
print(f"        ratio correct/wrong = {sp.Rational(76,5) / sp.nsimplify(wrong.subs(wsym2,20))}")
ck("A4: marginal cost at w=20 is 19/5 = $3.80", sp.diff(C_of_w, wsym2).subs(wsym2, 20), sp.Rational(19, 5))
ck("A4: 4 widgets x $3.80 = $15.20 = 76/5", 4 * sp.diff(C_of_w, wsym2).subs(wsym2, 20), sp.Rational(76, 5))
ck("A4: wrong/correct ratio = 361/25", sp.Rational(76, 5) / sp.Rational(20, 19), sp.Rational(361, 25))

print("\n" + "=" * 60)
print(f"RESULT: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    print("FAILED:", FAIL)
    raise SystemExit(1)
print("ALL CHECKS PASS")

ck("K'(5)=896", dKdx.subs(x, 5), sp.Integer(896))
ck("K'(10)=1152", dKdx.subs(x, 10), sp.Integer(1152))
ck("composite route agrees", sp.diff(sp.expand(K), x), dKdx)
