# Tests for the symbolic verification helpers.
# TDD: write expectations first, then implement verify/symbolic.py to pass them.
import sympy as sp
import pytest

from verify.symbolic import (
    simplify_true,
    slope_of_implicit,
    is_equivalent,
    tangent_line,
)


class TestSimplifyTrue:
    def test_simple_identity(self):
        # -x/y evaluated at (3,4) simplifies to -3/4
        x, y = sp.symbols("x y")
        expr = -x / y
        val = simplify_true(expr.subs({x: 3, y: 4}))
        assert val == sp.Rational(-3, 4)

    def test_fraction_reduces(self):
        val = simplify_true(sp.Rational(2, 4))
        assert val == sp.Rational(1, 2)

    def test_keeps_symbol(self):
        x = sp.symbols("x")
        val = simplify_true(x + x)
        assert val == 2 * x


class TestSlopeOfImplicit:
    def test_circle(self):
        # x^2 + y^2 = 25  =>  dydx = -x/y
        x, y = sp.symbols("x y")
        expr = x**2 + y**2 - 25
        dydx = slope_of_implicit(expr, x, y)
        got = simplify_true(dydx.subs({x: 3, y: 4}))
        assert got == sp.Rational(-3, 4)

    def test_linear(self):
        # y = 2x + 1  =>  y - 2x - 1 = 0  =>  dydx = 2
        x, y = sp.symbols("x y")
        expr = y - 2 * x - 1
        dydx = slope_of_implicit(expr, x, y)
        assert simplify_true(dydx) == 2

    def test_no_y_dependence_raises(self):
        # x^2 = 1 has no y; dy/dx is undefined.
        x, y = sp.symbols("x y")
        expr = x**2 - 1
        with pytest.raises(ValueError):
            slope_of_implicit(expr, x, y)


class TestIsEquivalent:
    def test_de_morgan(self):
        # not(A and B) == not A or not B
        A, B = sp.symbols("A B")
        lhs = sp.Not(A & B)
        rhs = sp.Or(sp.Not(A), sp.Not(B))
        assert is_equivalent(lhs, rhs)

    def test_not_equivalent(self):
        A, B = sp.symbols("A B")
        assert not is_equivalent(A & B, A | B)

    def test_same_expression(self):
        A = sp.symbols("A")
        assert is_equivalent(A, A)


class TestTangentLine:
    def test_slope_intercept(self):
        x, y = sp.symbols("x y")
        expr = x**2 + y**2 - 25
        line = tangent_line(expr, x, y, sp.Rational(3), 4)
        # y = 4 + (-3/4)(x - 3) = -3/4 x + 25/4
        expect = sp.Rational(-3, 4) * x + sp.Rational(25, 4)
        assert sp.simplify(line - expect) == 0

    def test_tangent_passes_through_point(self):
        x, y = sp.symbols("x y")
        expr = x**2 + y**2 - 25
        line = tangent_line(expr, x, y, sp.Rational(3), 4)
        assert sp.simplify(line.subs(x, 3) - 4) == 0