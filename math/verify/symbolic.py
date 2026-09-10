"""Symbolic verification helpers built on sympy.

Each function returns an exact sympy/sympy bool (or the simplified expression)
so callers and tests can assert equality *exactly* as rationals, never as
floating point.
"""
from __future__ import annotations

import sympy as sp
from sympy.logic.boolalg import Boolean  # covers And/Or/Not/Equivalent/...


def simplify_true(expr) -> sp.Expr:
    """Simplify an expression and return it as an exact sympy object.

    ``sp.simplify(x+x) -> 2*x``, ``sp.simplify(2/4) -> 1/2``.
    """
    return sp.simplify(expr)


def slope_of_implicit(expr, x, y) -> sp.Expr:
    """Return dy/dx for the implicit equation ``expr == 0``.

    Uses implicit differentiation: F_x + F_y * dy/dx = 0  =>  dy/dx = -F_x / F_y.

    Raises ValueError if the expression does not depend on ``y`` (the slope is
    undefined, e.g. for ``x**2 = 1``).
    """
    Fx = sp.diff(expr, x)
    Fy = sp.diff(expr, y)
    if Fy == 0:
        raise ValueError("dy/dx is undefined: expression has no y-dependence")
    return sp.simplify(-Fx / Fy)


def is_equivalent(lhs, rhs) -> bool:
    """Return True if ``lhs`` and ``rhs`` are logically/symbolically identical.

    Works for both algebraic expressions (numeric identity) and sympy Boolean
    expressions (logical equivalence via truth tables / Boolean simplification).
    """
    # Boolean case: compare after truth-table minimization.
    # simplify_logic normalizes both sides into canonical NNF/SOP form;
    # identical normalized forms <=> logically equivalent.
    if isinstance(lhs, Boolean) or isinstance(rhs, Boolean):
        from sympy.logic.boolalg import simplify_logic

        return bool(simplify_logic(lhs) == simplify_logic(rhs))
    return bool(sp.simplify(lhs - rhs) == 0)


def tangent_line(expr, x, y, x0, y0) -> sp.Expr:
    """Return the tangent line as ``y = m*(x - x0) + y0`` (an explicit function of x).

    For F(x, y) == 0 with slope m = dy/dx(x0, y0), evaluates and expands the
    right-hand side ``m*(x - x0) + y0``. The caller can treat it as ``y = ...``.
    """
    m = slope_of_implicit(expr, x, y).subs({x: x0, y: y0})
    m = sp.simplify(m)
    return sp.expand(m * (x - x0) + y0)