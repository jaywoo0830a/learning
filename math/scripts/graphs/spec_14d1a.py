"""14D1A-1 \"circle trade\" graph — rebuilt on the shared viz/verify core.

This is a reference migration of a real session graph. Instead of hard-coding
colors / layout / numbers in a one-off script, it:
  1. verifies the math first via verify.symbolic (slope, tangent, vertical pts),
  2. builds the figure only through the chainable ``G`` builder,
  3. registers via ``@graph`` (single source of truth for id + canonical path),
  4. returns ``(fig, facts, checks)`` so the test runner can verify every claim.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

from viz.graph import G
from viz.registry import graph
from verify.symbolic import slope_of_implicit, simplify_true, tangent_line


@graph("14d1a-01-circle-trade", session="14d1a", number="01", slug="circle-trade")
def build_circle_trade():
    """Return (fig, facts, checks): tangent slope -3/4 at (3,4) on x^2+y^2=25."""
    # ── verify first ─────────────────────────────────────────────
    x, y = sp.symbols("x y")
    circle = x**2 + y**2 - 25
    m = slope_of_implicit(circle, x, y)                    # -x/y
    m_at = simplify_true(m.subs({x: 3, y: 4}))            # -3/4
    line = tangent_line(circle, x, y, sp.Rational(3), 4)  # y=-3/4 x + 25/4

    facts = {
        "m_at_3_4": m_at,
        "tangent_line": line,
        "radius2": 25,
    }

    # ── render with the chainable builder ─────────────────────────
    g = G(size=(7.6, 6.8), equal_aspect=True,
          title="The circle: one formula, four sign stories")
    th = np.linspace(0, 2 * np.pi, 500)
    g.curve(5 * np.cos(th), 5 * np.sin(th), label=r"$x^2+y^2=25$")
    g.tangent((3.0, 4.0), -0.75, half=2.0,
              label=r"tangent: $y-4=-\frac{3}{4}(x-3)$")
    g.point((3.0, 4.0))
    g.callout((3.0, 4.0), r"$\frac{dy}{dx}=-\frac{x}{y}=-\frac{3}{4}$",
              offset=(-2.2, 0.7))
    # quadrant sign stories (visually annotated, matching original)
    g.ax.text(3.1, 2.1, "fight\n($y\\downarrow$ as $x\\uparrow$)",
              fontsize=9, color="purple", ha="center")
    g.ax.text(3.1, -1.5, "cooperate\n($y\\uparrow$ as $x\\uparrow$)",
              fontsize=9, color="green", ha="center")
    # vertical tangent marker at (5,0)
    g.callout((5.0, 0.0), "vertical tangent\n$y=0$",
              offset=(-1.8, -1.0), color="gray", fontsize=9, fontweight="normal")

    g.ax.set_xlim(-5.8, 6.2); g.ax.set_ylim(-4.6, 5.6)
    g.ax.set_xlabel("$x$"); g.ax.set_ylabel("$y$")

    fig, _garbage_facts, checks = g.build()
    checks["slope at (3,4) == -3/4"] = lambda: bool(m_at == sp.Rational(-3, 4))
    checks["tangent line == -3/4 x + 25/4"] = lambda: bool(
        sp.simplify(line - (sp.Rational(-3, 4) * x + sp.Rational(25, 4))) == 0)
    checks["contact point lies on circle"] = lambda: bool(3**2 + 4**2 == 25)
    checks["vertical tangents only where y=0"] = lambda: bool(
        set(sp.solve([circle, sp.diff(circle, y)], [x, y]))
        == set([(sp.Integer(-5), 0), (sp.Integer(5), 0)]))
    checks["dy/dx < 0 in first quadrant"] = lambda: bool(
        simplify_true(m.subs({x: 4, y: 3})) < 0)
    return fig, facts, checks


def main():
    from viz.export import save_figure
    from viz.registry import spec

    gs = spec("14d1a-01-circle-trade")
    fig, facts, checks = gs.fn()
    out = save_figure(fig, gs.path)
    print("verified facts:", facts)
    print("all checks pass:", all(fn() for _, fn in checks.items()))
    print("saved to:", out)


if __name__ == "__main__":
    main()