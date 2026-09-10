"""Generate a verified sample graph: circle with tangent at (3,4).

The tangent slope is verified symbolically (sympy) BEFORE rendering; the
figure is built only from shared viz primitives and saved via viz/export.
Run inside the container:  make run-sample  (or pytest test_graph_integration).
"""
import os
import sys

import matplotlib
matplotlib.use("Agg", force=True)
import numpy as np
import sympy as sp

from viz.canvas import new_canvas, simple_axes
from viz.primitives.curve import plot_curve, plot_tangent, plot_point
from viz.primitives.annotate import add_callout
from viz.export import save_figure
from verify.symbolic import slope_of_implicit, simplify_true, tangent_line


def main():
    # 1) verify the math first
    x, y = sp.symbols("x y")
    circle = x**2 + y**2 - 25
    m = slope_of_implicit(circle, x, y)                      # -x/y
    m_at = simplify_true(m.subs({x: 3, y: 4}))               # -3/4
    line = tangent_line(circle, x, y, sp.Rational(3), 4)     # y = -3/4 x + 25/4
    print("verified tangent slope:", m_at, "| line:", line, "=", sp.simplify(line - (sp.Rational(-3, 4) * x + sp.Rational(25, 4))))

    # 2) render with shared primitives
    fig, ax = new_canvas(size=(7.6, 6.8))
    simple_axes(ax, equal_aspect=True)
    t = np.linspace(0, 2 * np.pi, 500)
    plot_curve(ax, 5 * np.cos(t), 5 * np.sin(t), label=r"$x^2+y^2=25$")
    plot_tangent(ax, 3.0, 4.0, -0.75, half=2.0, label="tangent")
    plot_point(ax, 3.0, 4.0)
    add_callout(ax, target=(3.0, 4.0), text=r"$\frac{dy}{dx}=-\frac{3}{4}$",
                offset=(-2.4, 0.9))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-2, 7)
    ax.set_title("Verified circle tangent: dy/dx = -3/4 (sympy-checked)")

    # 3) save
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "graphs", "verified-circle-tangent.png")
    save_figure(fig, out)
    print("saved:", out)


if __name__ == "__main__":
    main()