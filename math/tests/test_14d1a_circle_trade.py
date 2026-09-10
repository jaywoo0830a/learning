# Tests for migrating the real session graph "14D1A-1 circle trade".
#
# The goal: reproduce the graph from the shared viz primitives, and promote the
# facts it encodes (tangent slope, quadrant sign stories, vertical tangent)
# into verifiable checks through the verify layer.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from verify.symbolic import slope_of_implicit, simplify_true, tangent_line


class TestCircleTradeFacts:
    """The mathematical claims the graph visualizes, verified symbolically."""

    @staticmethod
    def _circle_expr():
        x, y = sp.symbols("x y")
        return x**2 + y**2 - 25

    def test_tangent_slope_at_3_4(self):
        x, y = sp.symbols("x y")
        m = slope_of_implicit(self._circle_expr(), x, y)          # -x/y
        m_at = simplify_true(m.subs({x: 3, y: 4}))
        assert m_at == sp.Rational(-3, 4)

    def test_tangent_line_at_3_4(self):
        x, y = sp.symbols("x y")
        line = tangent_line(self._circle_expr(), x, y, sp.Rational(3), 4)
        # y = 4 - (3/4)(x-3) = -3/4 x + 25/4
        expect = sp.Rational(-3, 4) * x + sp.Rational(25, 4)
        assert sp.simplify(line - expect) == 0

    def test_vertical_tangent_only_at_y0(self):
        # dy/dx blows up where F_y = 0, i.e. y = 0 => (x,y) = (+-5, 0)
        x, y = sp.symbols("x y")
        Fy = sp.diff(self._circle_expr(), y)                     # 2y
        pts = sp.solve([self._circle_expr(), Fy], [x, y])
        assert set(pts) == set([(sp.Integer(-5), 0), (sp.Integer(5), 0)])

    def test_quadrant_sign_stories(self):
        # In the first quadrant, dy/dx = -x/y < 0 (fight). Pick (3,4).
        x, y = sp.symbols("x y")
        m = slope_of_implicit(self._circle_expr(), x, y)
        # (3,4): first quadrant -> negative slope
        m_q1 = simplify_true(m.subs({x: 3, y: 4}))
        assert m_q1 < 0
        # (4,3): still first quadrant, smaller |slope| (-4/3)
        m_q1b = simplify_true(m.subs({x: 4, y: 3}))
        assert m_q1b < 0

    def test_contact_point_on_circle(self):
        assert 3**2 + 4**2 == 25


class TestCircleTradeRender:
    """The migrated graph builds only from shared primitives and exports."""

    def test_builder_returns_figure_and_facts(self):
        from scripts.graphs.spec_14d1a import build_circle_trade

        fig, facts = build_circle_trade()
        assert facts["m_at_3_4"] == sp.Rational(-3, 4)
        assert len(fig.axes) == 1
        plt.close(fig)

    def test_render_has_expected_artists(self):
        from scripts.graphs.spec_14d1a import build_circle_trade

        fig, facts = build_circle_trade()
        ax = fig.axes[0]
        # circle + tangent line + (single-point) => curve and tangent are lines
        # plus quadrant annotations are text
        assert len(ax.lines) == 2          # circle + tangent
        assert len(ax.texts) >= 2          # callout + quadrant labels
        assert len(ax.collections) >= 1    # highlight point
        plt.close(fig)

    def test_no_label_swallows_contact_point(self):
        """Guard against the original pain: a text bbox overlapping the point.

        After a draw, no annotation's display bbox may contain the contact point
        (3,4). (The callout ARROWS to it; its text body must sit off the point.)
        """
        from scripts.graphs.spec_14d1a import build_circle_trade

        fig, facts = build_circle_trade()
        ax = fig.axes[0]
        fig.canvas.draw()
        dx, dy = ax.transData.transform((3.0, 4.0))
        for t in ax.texts:
            bbox = t.get_window_extent()
            if bbox.contains(dx, dy):
                raise AssertionError(
                    f"text bbox overlaps contact point (3,4): {t.get_text()!r}"
                )
        plt.close(fig)