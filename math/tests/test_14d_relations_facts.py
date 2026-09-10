# Symbolic verification of the math facts behind session graphs 14D / 14D1.
# These are the claims the 7 migrated graphs visualize — checked via verify.
import matplotlib
matplotlib.use("Agg", force=True)
import sympy as sp

from verify.symbolic import simplify_true, slope_of_implicit, is_equivalent


class TestD1DerivativeUnits:
    """d1: position s=1/2 t^2 (m/s); cost C=q^2+4q+144 ($/unit)."""

    @staticmethod
    def _s():
        t = sp.symbols("t")
        return sp.Rational(1, 2) * t**2

    def test_tangent_slope_at_2(self):
        t = sp.symbols("t")
        s = self._s()
        assert simplify_true(sp.diff(s, t).subs(t, 2)) == 2  # m/s

    @staticmethod
    def _C():
        q = sp.symbols("q")
        return q**2 + 4 * q + 144

    def test_marginal_cost_at_12(self):
        q = sp.symbols("q")
        C = self._C()
        assert simplify_true(sp.diff(C, q).subs(q, 12)) == 28  # $/unit

    def test_C_of_12(self):
        q = sp.symbols("q")
        assert sp.simplify(self._C().subs(q, 12)) == 336


class TestD2MotionStory:
    """d2: v=t^2-4t+3, a=2t-4; turns at t=1,3; a sign change."""

    @staticmethod
    def _v():
        t = sp.symbols("t")
        return t**2 - 4 * t + 3

    def test_velocity_roots_exact(self):
        t = sp.symbols("t")
        roots = sp.solve(self._v(), t)
        assert sorted(int(r) for r in roots) == [1, 3]

    def test_acceleration_sign(self):
        t = sp.symbols("t")
        a = sp.diff(self._v(), t)  # 2t-4
        # a<0 for t<2, a>0 for t>2
        assert simplify_true(a.subs(t, 1)) == -2
        assert simplify_true(a.subs(t, 3)) == 2

    def test_tangent_slope_at_points(self):
        t = sp.symbols("t")
        assert simplify_true(sp.diff(self._v(), t)) == 2 * t - 4


class TestD3Linearization:
    """d3: f=sqrt(x), f'(4)=1/4, L(4.1)~2.025, sqrt(4.1)~2.0248."""

    @staticmethod
    def _f():
        x = sp.symbols("x", positive=True)
        return sp.sqrt(x)

    def test_derivative_at_4(self):
        x = sp.symbols("x", positive=True)
        assert simplify_true(sp.diff(self._f(), x).subs(x, 4)) == sp.Rational(1, 4)

    def test_linearization_value(self):
        x = sp.symbols("x", positive=True)
        f = self._f()
        L = f.subs(x, 4) + sp.diff(f, x).subs(x, 4) * (x - 4)  # 2 + (x-4)/4
        assert simplify_true(L.subs(x, 4)) == 2
        assert simplify_true(L.subs(x, sp.Rational(41, 10))) == sp.Rational(81, 40)  # 2.025

    def test_error_is_small(self):
        import math
        # sqrt(4.1) ~ 2.024845... vs L(4.1)=2.025, error ~ 0.00015
        exact = sp.N(sp.sqrt(sp.Rational(41, 10)), 8)
        approx = sp.Rational(81, 40)
        assert abs(float(exact) - float(approx)) < 0.0002


class TestD4CircleRing:
    """d4: A=pi r^2 => dA/dr = 2 pi r = circumference; ring area ~ 2 pi r dr."""

    def test_area_derivative_is_circumference(self):
        r = sp.symbols("r")
        A = sp.pi * r**2
        assert simplify_true(sp.diff(A, r)) == 2 * sp.pi * r

    def test_ring_area_formula(self):
        r, dr = sp.symbols("r dr")
        # A(r+dr) - A(r) ~ = 2 pi r dr + pi dr^2
        dA = sp.pi * (r + dr) ** 2 - sp.pi * r**2
        # leading order is 2 pi r dr
        assert sp.simplify(sp.expand(dA) - (2 * sp.pi * r * dr)) == sp.pi * dr**2


class TestD5SphereShell:
    """d5: V=4/3 pi r^3 => dV/dr = 4 pi r^2 = surface area."""

    def test_volume_derivative_is_surface_area(self):
        r = sp.symbols("r")
        V = sp.Rational(4, 3) * sp.pi * r**3
        assert simplify_true(sp.diff(V, r)) == 4 * sp.pi * r**2


class TestD6MarginalCost:
    """d6: MC=2q+4, AC=q+4+144/q; minimum AC at q=12 where MC=AC."""

    @staticmethod
    def _MC():
        q = sp.symbols("q", positive=True)
        return 2 * q + 4

    @staticmethod
    def _AC():
        q = sp.symbols("q", positive=True)
        return q + 4 + 144 / q

    def test_MC_AC_equal_at_12(self):
        q = sp.symbols("q", positive=True)
        sol = sp.solve(sp.Eq(self._MC(), self._AC()), q)
        assert [int(s) for s in sol if s.is_real] == [12]

    def test_AC_min_at_12(self):
        q = sp.symbols("q", positive=True)
        AC = self._AC()
        crit = sp.solve(sp.Eq(sp.diff(AC, q), 0), q)
        assert [int(s) for s in crit if s.is_real] == [12]
        # second derivative positive (minimum)
        assert sp.simplify(sp.diff(AC, q, 2)) > 0


class TestD7Elasticity:
    """d7: q=500-10p; E=-1 & revenue max at p=25."""

    @staticmethod
    def _q():
        p = sp.symbols("p")
        return 500 - 10 * p

    def test_elasticity_at_25(self):
        p = sp.symbols("p")
        q = self._q()
        E = p / q * sp.diff(q, p)  # p/q * dq/dp
        assert simplify_true(E.subs(p, 25)) == -1

    def test_revenue_quadratic_max(self):
        p = sp.symbols("p")
        R = p * self._q()  # 500p - 10 p^2
        assert sp.simplify(sp.diff(R, p)) == 500 - 20 * p
        crit = sp.solve(sp.Eq(sp.diff(R, p), 0), p)
        assert [int(s) for s in crit if s.is_real] == [25]
        # max: second derivative < 0
        assert sp.simplify(sp.diff(R, p, 2)) < 0