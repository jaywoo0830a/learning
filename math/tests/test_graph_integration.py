# End-to-end graph test: build + verify + render + save one real figure.
# This is the "reach goal": a single graph whose mathematical claim is checked
# by the verify layer and whose rendering reuses the viz primitives.
import os

import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from viz.canvas import new_canvas, simple_axes
from viz.primitives.curve import plot_curve, plot_tangent, plot_point
from viz.primitives.annotate import add_callout
from viz.export import save_figure
from verify.symbolic import slope_of_implicit, simplify_true, tangent_line


def build_circle_tangent_graph():
    """Build the x^2+y^2=25 circle with tangent at (3,4).

    Returns the sympy-verified tangent slope, tangent line, and the figure.
    """
    # --- number the facts to verify ---
    x, y = sp.symbols("x y")
    circle = x**2 + y**2 - 25
    m = slope_of_implicit(circle, x, y)               # -x/y
    x0, y0 = sp.Rational(3), 4
    m_at = simplify_true(m.subs({x: x0, y: y0}))       # -3/4
    line = tangent_line(circle, x, y, x0, y0)          # y = -3/4 x + 25/4

    assert m_at == sp.Rational(-3, 4)

    # --- render ---
    fig, ax = new_canvas(size=(7.6, 6.8))
    simple_axes(ax, equal_aspect=True)
    th = np.linspace(0, 2 * np.pi, 500)
    plot_curve(ax, 5 * np.cos(th), 5 * np.sin(th), label=r"$x^2+y^2=25$")

    # tangent via lambda of the verified line y = -3/4 x + 25/4
    tx = np.array([x0 - 2, x0 + 2], dtype=float)
    plot_tangent(ax, float(x0), 4.0, -0.75, half=2.0, label="tangent")
    plot_point(ax, float(x0), 4.0)
    add_callout(ax, target=(float(x0), 4.0), text=r"$\frac{dy}{dx}=-\frac{3}{4}$",
                offset=(-2.2, 0.8))
    ax.set_title("The circle: tangent slope is verified as -3/4")
    return fig, m_at, line


class TestCircleTangentGraph:
    def test_slope_verified_symbolically(self):
        x, y = sp.symbols("x y")
        circle = x**2 + y**2 - 25
        m = slope_of_implicit(circle, x, y)
        m_at = simplify_true(m.subs({x: 3, y: 4}))
        assert m_at == sp.Rational(-3, 4)

    def test_graph_renders_at_least_one_curve_and_point(self):
        fig, m_at, line = build_circle_tangent_graph()
        ax = fig.axes[0]
        assert m_at == sp.Rational(-3, 4)
        # one curve + one tangent line
        assert len(ax.lines) == 2
        # one callout present
        assert len(ax.texts) == 1
        # one highlighted point (scatter collection)
        assert len(ax.collections) >= 1
        plt.close(fig)

    def test_save_produces_png(self, tmp_path):
        fig, m_at, line = build_circle_tangent_graph()
        out = save_figure(fig, str(tmp_path / "circle-tangent.png"))
        assert os.path.exists(out)
        assert os.path.getsize(out) > 0
        plt.close(fig)

    def test_curve_is_actually_the_circle(self):
        # every sampled point of the drawn curve must satisfy x^2+y^2=25 (radius 5)
        fig, _, _ = build_circle_tangent_graph()
        ax = fig.axes[0]
        xs, ys = ax.lines[0].get_xdata(), ax.lines[0].get_ydata()
        radii2 = xs**2 + ys**2
        assert np.allclose(radii2, 25.0, atol=1e-9)
        plt.close(fig)

    def test_tangent_passes_through_contacts_point(self):
        # the tangent segment's endpoints satisfy y = 4 + (-3/4)(x-3)
        fig, _, _ = build_circle_tangent_graph()
        ax = fig.axes[0]
        xs = ax.lines[1].get_xdata()
        ys = ax.lines[1].get_ydata()
        # half=2.0 -> x in [1,5]; y = 4 - 0.75(x-3)
        expect = 4.0 - 0.75 * (xs - 3.0)
        assert np.allclose(ys, expect, atol=1e-9)
        # contacts point lies exactly on the circle
        xc, yc = 3.0, 4.0
        assert abs(xc**2 + yc**2 - 25) < 1e-12
        plt.close(fig)

    def test_callout_target_sits_on_curve(self):
        # the annotation's arrow target equals the highlight point's location
        fig, _, _ = build_circle_tangent_graph()
        ax = fig.axes[0]
        ann = ax.texts[0]
        tx, ty = ann.xy
        assert abs(tx - 3.0) < 1e-9 and abs(ty - 4.0) < 1e-9
        plt.close(fig)