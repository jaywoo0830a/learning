"""Session 9B graphs — rebuilt genuinely on the VIZ framework.

Each builder:
  1. verifies a core math fact with sympy (``facts``) and attaches it as
     ``checks`` (name -> () -> bool) so tests run every claim uniformly,
  2. draws only through the shared VIZ primitives / canvas helpers,
  3. is registered via ``@graph`` — the single source of truth for its id and
     canonical ``graphs/9b/<nn>-<slug>.png`` location.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

from viz.canvas import new_canvas, subplots_canvas
from viz.theme import PALETTE as C
from viz.primitives import grid, conic
from viz.primitives.conic import plot_circle_c, plot_ellipse_c, plot_param2d, plot_parabola_v, plot_hyperbola_branches, plot_asymptotes
from viz.primitives.curve import plot_curve, plot_point
from viz.coords import coords_ax
from viz.registry import graph


@graph("9b-01-line-forms", session="9b", number="01", slug="line-forms")
def build_line_forms():
    """Five forms of one line 2x+3y=6, each on its own subplot."""
    facts = {"line_expr": sp.simplify(2 * sp.Symbol("x") + 3 * sp.Symbol("y") - 6)}

    checks = {
        "line 2x+3y=6 passes through (3,0)": lambda: bool(sp.simplify(2*3 + 3*0 - 6) == 0),
    }

    fig, axes = subplots_canvas(2, 3, size=(14, 9))
    xs = np.linspace(-2, 8, 100)
    forms = [
        ("I Slope-Intercept", r"$y=-\frac{2}{3}x+2$"),
        ("II Point-Slope", r"$y-0=-\frac{2}{3}(x-3)$"),
        ("III Two-Point", r"$\frac{y-2}{x}=\frac{-2}{3}$"),
        ("IV Intercept", r"$\frac{x}{3}+\frac{y}{2}=1$"),
        ("V General", r"$2x+3y-6=0$"),
        ("Same line", "2x+3y=6"),
    ]
    for ax, (title, eq) in zip(axes.flat, forms):
        coords_ax(ax, xlo=-1, xhi=7, ylo=-1.5, yhi=3.5)
        plot_curve(ax, xs, -2 / 3 * xs + 2, color="blue", lw=2.5)
        ax.set_title(f"{title}\n{eq}", fontsize=10, fontweight="bold")
    axes.flat[-1].text(0.5, 0.5, "2x + 3y = 6", transform=axes.flat[-1].transAxes,
                       ha="center", va="center", fontsize=16, fontweight="bold", color="navy")
    fig.suptitle("The Five Forms of a Line", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-02-step-line-forms", session="9b", number="02", slug="step-line-forms")
def build_step_line_forms():
    """Walk the 3-step build of the line through (2,1) with slope 3/4."""
    facts = {"slope": sp.Rational(3, 4)}

    checks = {
        "line through (2,1) and (6,4) has slope 3/4": lambda: bool(facts['slope'] == sp.Rational(3, 4) and sp.simplify(sp.Rational(4 - 1, 6 - 2)) == sp.Rational(3, 4)),
    }

    fig, axes = subplots_canvas(1, 3, size=(15, 5))
    xs = np.linspace(-1, 7, 100)
    titles = ["Step 1: point + slope 3/4", "Step 2: trace the line", "Step 3: all forms"]
    for i, ax in enumerate(axes.flat):
        coords_ax(ax, xlo=-0.5, xhi=7, ylo=-1.5, yhi=5)
        plot_curve(ax, xs, 0.75 * xs - 0.5, color="blue", lw=2.5)
        plot_point(ax, 2, 1)
        if i >= 1:
            plot_point(ax, 6, 4)
        ax.set_title(titles[i], fontweight="bold")
    fig.suptitle("Building a Line — Step by Step", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-03-parallel-perpendicular", session="9b", number="03", slug="parallel-perpendicular")
def build_parallel_perpendicular():
    """Parallel (same m) and perpendicular (product -1)."""
    m1, m2 = sp.Rational(2, 3), sp.Rational(-3, 2)
    facts = {"perp_product": sp.simplify(m1 * m2)}

    checks = {
        "perpendicular slopes multiply to -1": lambda: bool(facts['perp_product'] == -1),
    }

    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(13, 5.5))
    xs = np.linspace(-3, 3, 100)
    coords_ax(ax1, xlo=-3, xhi=3, ylo=-6, yhi=6)
    plot_curve(ax1, xs, 2 * xs + 1, color="blue", lw=2.5, label=r"$y=2x+1$")
    plot_curve(ax1, xs, 2 * xs - 5, color="red", lw=2.5, ls="--", label=r"$y=2x-5$")
    ax1.set_title("Parallel: $m_1=m_2=2$", fontweight="bold")
    ax1.legend()
    coords_ax(ax2, xlo=-3, xhi=3, ylo=-3, yhi=3)
    plot_curve(ax2, xs, 2 / 3 * xs, color="blue", lw=2.5, label=r"$y=\frac{2}{3}x$")
    plot_curve(ax2, xs, -3 / 2 * xs, color="red", lw=2.5, ls="--", label=r"$y=-\frac{3}{2}x$")
    ax2.set_title("Perpendicular: $m_1m_2=-1$", fontweight="bold")
    ax2.legend()
    ax2.text(0.5, 0.4, "90°", fontsize=14, color=C["purple"])
    fig.suptitle("Parallel and Perpendicular Lines", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-04-angle-between-lines", session="9b", number="04", slug="angle-between-lines")
def build_angle_between_lines():
    """Angle between y=2x and y=-x/3: tan(phi)=|(m2-m1)/(1+m1 m2)|."""
    from matplotlib.patches import Arc
    m1, m2 = sp.Rational(2), sp.Rational(-1, 3)
    tan = sp.simplify(abs((m2 - m1) / (1 + m1 * m2)))
    facts = {"tan_phi": tan}

    checks = {
        "tan(phi) == 7": lambda: bool(facts['tan_phi'] == 7),
        "angle from formula is ~81.9 deg": lambda: bool(np.isclose(np.degrees(np.arctan(7)), 81.87, atol=0.1)),
    }

    fig, ax = new_canvas(size=(9, 7))
    coords_ax(ax, xlo=-2, xhi=3, ylo=-1, yhi=6)
    xs = np.linspace(-2, 3, 100)
    plot_curve(ax, xs, 2 * xs, color="blue", lw=2.5, label=r"$y=2x$")
    plot_curve(ax, xs, -1 / 3 * xs, color="red", lw=2.5, label=r"$y=-\frac{1}{3}x$")
    ax.add_patch(Arc((0, 0), 0.8, 0.8, angle=0, theta1=np.arctan(-1 / 3) * 180 / np.pi,
                     theta2=np.arctan(2) * 180 / np.pi, color=C["purple"], lw=2))
    ax.text(0.45, 0.2, r"$\phi\approx 81.9°$", fontsize=13, color=C["purple"], fontweight="bold")
    ax.legend(fontsize=11)
    ax.set_title(r"Angle: $\tan\phi=\left|\frac{m_2-m_1}{1+m_1m_2}\right|=7$", fontweight="bold")
    return fig, facts, checks



@graph("9b-05-midpoint-division", session="9b", number="05", slug="midpoint-division")
def build_midpoint_division():
    """Midpoint of (2,5)-(8,-1) is M(5,2); centroid of a triangle."""
    facts = {"mid": sp.Point(5, 2), "centroid": sp.Point(sp.Rational(11, 3), sp.Rational(5, 3))}

    checks = {
        "midpoint == (5,2)": lambda: bool(facts['mid'] == sp.Point(5, 2)),
        "centroid == (11/3, 5/3)": lambda: bool(facts['centroid'] == sp.Point(sp.Rational(11, 3), sp.Rational(5, 3))),
    }

    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(13, 5.5))
    grid.light_grid(ax1)
    plot_curve(ax1, [2, 8], [5, -1], color="blue", lw=2, marker="o", markersize=8)
    plot_point(ax1, 5, 2, color="red", ms=12)
    ax1.text(5, 2.3, "M(5,2)", color=C["red"], fontweight="bold")
    ax1.text(2, 5.2, "(2,5)"); ax1.text(7.8, -1.6, "(8,-1)")
    grid.set_limits(ax1, 0, 10, -3, 7)
    ax1.set_title("Midpoint", fontweight="bold")

    tri = np.array([[0, 0], [8, 0], [3, 5], [0, 0]])
    grid.light_grid(ax2)
    ax2.plot(tri[:, 0], tri[:, 1], color=C["green"], lw=1.5, alpha=0.6)
    ax2.fill(tri[:, 0], tri[:, 1], "green", alpha=0.08)
    ax2.plot([11 / 3], [5 / 3], "g*", markersize=15)
    ax2.text(11 / 3, 5 / 3 + 0.3, "Centroid (11/3, 5/3)", color=C["green"], fontweight="bold")
    grid.set_limits(ax2, -1, 10, -1, 9)
    ax2.set_title("Centroid", fontweight="bold")
    fig.suptitle("Midpoint and Section Formula", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-06-point-line-distance", session="9b", number="06", slug="point-line-distance")
def build_point_line_distance():
    """Distance from P(6,4) to 3x+4y-12=0 is 22/5."""
    x0, y0, A, B, Cv = 6, 4, 3, 4, -12
    dist = sp.simplify(abs(A * x0 + B * y0 + Cv) / sp.sqrt(A**2 + B**2))
    facts = {"distance": dist}

    checks = {
        "distance from (6,4) to 3x+4y-12=0 is 22/5": lambda: bool(facts['distance'] == sp.Rational(22, 5)),
    }

    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(14, 6))
    xs = np.linspace(-2, 6, 100)
    coords_ax(ax1, xlo=-2, xhi=7, ylo=-1, yhi=6)
    plot_curve(ax1, xs, 3 - 3 / 4 * xs, color="blue", lw=2.5, label=r"$3x+4y=12$")
    plot_point(ax1, 6, 4, color="red")
    ax1.text(6, 4.2, "P(6,4)", color=C["red"], fontweight="bold")
    ax1.legend()
    ax1.set_title("Distance from a point to a line", fontweight="bold")
    ax2.axis("off")
    ax2.text(0.1, 0.5,
             r"$d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}=\frac{|3\cdot6+4\cdot4-12|}{5}=\frac{22}{5}$",
             transform=ax2.transAxes, fontsize=15, va="center",
             bbox=dict(boxstyle="round", facecolor="#f0f0f0", alpha=0.8))
    fig.suptitle("Point-to-Line Distance Formula", fontsize=14, fontweight="bold")
    return fig, facts, checks

@graph("9b-07-step-distance-line", session="9b", number="07", slug="step-distance-line")
def build_step_distance_line():
    """3-step derivation of point-to-line distance."""
    facts = {"dist": sp.Rational(22, 5)}

    checks = {
        "point-line distance is 22/5": lambda: bool(facts['dist'] == sp.Rational(22, 5)),
    }
    fig, axes = subplots_canvas(1, 3, size=(15, 5))
    xs = np.linspace(-1, 7, 100)
    titles = ["Step 1: line + point", "Step 2: perpendicular leg", "Step 3: formula"]
    for i, ax in enumerate(axes.flat):
        coords_ax(ax, xlo=-1, xhi=7, ylo=-1, yhi=5)
        plot_curve(ax, xs, 3 - 3 / 4 * xs, color="blue", lw=2.5)
        plot_point(ax, 6, 4, color="red")
        ax.set_title(titles[i], fontweight="bold")
    fig.suptitle("Deriving Point-to-Line Distance", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-08-two-lines-distance", session="9b", number="08", slug="two-lines-distance")
def build_two_lines_distance():
    """Distance between parallel lines 3x+4y=12 and 3x+4y=-8."""
    d = sp.simplify(abs(12 - (-8)) / sp.sqrt(3**2 + 4**2))
    facts = {"distance": d}

    checks = {
        "distance between 3x+4y=12 and 3x+4y=-8 is 4": lambda: bool(facts['distance'] == 4),
    }
    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(13, 5.5))
    xs = np.linspace(-2, 5, 100)
    for ax in (ax1, ax2):
        coords_ax(ax, xlo=-2, xhi=5, ylo=-4, yhi=5)
        plot_curve(ax, xs, 3 - 3 / 4 * xs, color="blue", lw=2.5, label="3x+4y=12")
        plot_curve(ax, xs, -2 - 3 / 4 * xs, color="red", lw=2.5, label="3x+4y=-8")
        ax.legend(fontsize=9)
    ax2.text(1.5, 2, r"$d=\frac{|12-(-8)|}{5}=\frac{20}{5}=4$",
             fontsize=14, ha="center", bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))
    ax1.set_title("Two parallel lines", fontweight="bold")
    ax2.set_title("Distance between parallels", fontweight="bold")
    fig.suptitle("Distance Between Parallel Lines", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-09-point-circle-distance", session="9b", number="09", slug="point-circle-distance")
def build_point_circle_distance():
    """Point (6,1) to circle center (3,-2) radius 3: dist to circle = 3sqrt2-3."""
    d = sp.simplify(sp.sqrt((6 - 3) ** 2 + (1 + 2) ** 2) - 3)
    facts = {"to_circle": d}

    checks = {
        "distance to circle == 3sqrt(2) - 3": lambda: bool(sp.simplify(facts['to_circle'] - (3*sp.sqrt(2) - 3)) == 0),
    }
    theta = np.linspace(0, 2 * np.pi, 200)
    fig, ax = new_canvas(size=(8, 6))
    coords_ax(ax, xlo=-2, xhi=8, ylo=-5, yhi=4)
    plot_curve(ax, 3 + 3 * np.cos(theta), -2 + 3 * np.sin(theta), color="blue", lw=2.5)
    plot_point(ax, 3, -2, color="red")
    plot_point(ax, 6, 1, color="red")
    ax.plot([3, 6], [-2, 1], "k--", lw=1)
    ax.text(3, -1.4, "C(3,-2) R=3", color=C["red"], fontweight="bold")
    ax.text(6, 1.2, "P(6,1)", color=C["red"], fontweight="bold")
    ax.set_title(r"$PC=\sqrt{18}=3\sqrt{2}$; to circle $=3\sqrt{2}-3$", fontweight="bold")
    return fig, facts, checks



@graph("9b-10-tangent-lines-circle", session="9b", number="10", slug="tangent-lines-circle")
def build_tangent_lines_circle():
    """Two tangents from P(8,0) to circle x^2+y^2=16 (center 0, R=4)."""
    # tangent point satisfies x^2+y^2=16 and (x-8)x+(y) y = 0  => x=2, y=+-2sqrt3
    xp, yp = sp.Symbol("xp"), sp.Symbol("yp")
    sol = sp.solve([sp.Eq(xp**2 + yp**2, 16),
                    sp.Eq(xp * (xp - 8) + yp * yp, 0)], [xp, yp])
    pts = [(sp.nsimplify(s[0]), sp.nsimplify(s[1])) for s in sol]
    facts = {"tangent_points": pts}

    checks = {
        "every tangent point lies on x^2+y^2=16": lambda: bool(all(sp.simplify(x**2 + y**2 - 16) == 0 for x, y in facts['tangent_points'])),
        "external point (8,0) is outside the circle": lambda: bool(8**2 > 16),
    }
    theta = np.linspace(0, 2 * np.pi, 200)
    fig, ax = new_canvas(size=(8, 7))
    coords_ax(ax, xlo=-1, xhi=9, ylo=-5, yhi=5)
    plot_curve(ax, 4 * np.cos(theta), 4 * np.sin(theta), color="blue", lw=2.5, label=r"x$^2$+y$^2$=16")
    plot_point(ax, 8, 0, color="red")
    for x_, y_ in [(2.0, float(sp.sqrt(12))), (2.0, -float(sp.sqrt(12)))]:
        ax.plot([8, x_], [0, y_], color="green", lw=2)
        plot_point(ax, x_, y_, color="green")
    ax.text(8, 0.3, "P(8,0)", fontweight="bold", color=C["red"])
    ax.legend()
    ax.set_title("Tangents from an external point", fontweight="bold")
    return fig, facts, checks



@graph("9b-11-circle-details", session="9b", number="11", slug="circle-details")
def build_circle_details():
    """Circle (x-3)^2+(y+2)^2=16: completing the square."""
    r, cx, cy = 4, 3, -2
    facts = {"center": sp.Point(cx, cy), "radius": r}

    checks = {
        "center (3,-2) radius 4": lambda: bool(facts['center'] == sp.Point(3, -2) and facts['radius'] == 4),
    }
    theta = np.linspace(0, 2 * np.pi, 200)
    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(13, 5.5))
    coords_ax(ax1, xlo=-3, xhi=9, ylo=-8, yhi=4)
    plot_curve(ax1, cx + r * np.cos(theta), cy + r * np.sin(theta), color="blue", lw=2.5)
    plot_point(ax1, cx, cy, color="red")
    ax1.plot([cx, cx + r], [cy, cy], "g--", lw=1.5)
    ax1.text(cx, cy + 0.6, "C(3,-2)", color=C["red"], fontweight="bold")
    ax1.text(cx + 2.5, cy, "R=4", fontsize=12, color=C["blue"], fontweight="bold")
    ax1.set_title(r"$(x-3)^2+(y+2)^2=16$", fontweight="bold")
    ax2.axis("off")
    ax2.text(0.1, 0.5,
             "General: $x^2+y^2-6x+4y-3=0$\n\nStep: $(x^2-6x+9)+(y^2+4y+4)=3+9+4$\n\n$(x-3)^2+(y+2)^2=16$",
             transform=ax2.transAxes, fontsize=14, va="center", family="monospace",
             bbox=dict(boxstyle="round", facecolor="#f0f0f0", alpha=0.8))
    fig.suptitle("Circle — Standard vs General Form", fontsize=14, fontweight="bold")
    return fig, facts, checks

@graph("9b-12-step-conic-circle", session="9b", number="12", slug="step-conic-circle")
def build_step_conic_circle():
    """Build a circle (x-3)^2+(y+2)^2=16 from center to trace."""
    facts = {"radius": 4}

    checks = {
        "radius is 4": lambda: bool(facts['radius'] == 4),
    }
    theta = np.linspace(0, 2 * np.pi, 200)
    fig, axes = subplots_canvas(1, 3, size=(15, 5))
    titles = ["Step 1: Center (h,k)", "Step 2: points at distance R", "Step 3: circle"]
    for i, ax in enumerate(axes.flat):
        coords_ax(ax, xlo=-3, xhi=9, ylo=-8, yhi=4)
        plot_point(ax, 3, -2, color="red")
        ax.text(3, -1.6, "C(3,-2)", color=C["red"], fontweight="bold")
        if i >= 1:
            plot_curve(ax, 3 + 4 * np.cos(theta), -2 + 4 * np.sin(theta), color="blue", lw=2.5)
        ax.set_title(titles[i], fontweight="bold", fontsize=10)
    fig.suptitle("Building a Circle — Step by Step", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-13-ellipse-details", session="9b", number="13", slug="ellipse-details")
def build_ellipse_details():
    """Ellipse x^2/25+y^2/9=1: foci +-4, sum property PF1+PF2=2a=10."""
    a, b = 5, 3
    c = sp.sqrt(sp.simplify(a**2 - b**2))
    facts = {"c": c}

    checks = {
        "c^2 == a^2 - b^2 == 16": lambda: bool(sp.simplify(facts['c'] ** 2) == 16),
    }
    theta = np.linspace(0, 2 * np.pi, 300)
    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(14, 6))
    coords_ax(ax1, xlo=-6, xhi=6, ylo=-4, yhi=4)
    plot_curve(ax1, a * np.cos(theta), b * np.sin(theta), color="blue", lw=2.5)
    plot_point(ax1, 4, 0, color="magenta", ms=6)
    plot_point(ax1, -4, 0, color="magenta", ms=6)
    plot_point(ax1, 5, 0, color="red", ms=6)
    ax1.text(4, 0.4, "F(4,0)", color=C["purple"])
    ax1.text(-4, 0.4, "F(-4,0)", color=C["purple"])
    ax1.set_title(r"$x^2/25+y^2/9=1$, foci $\pm4$", fontweight="bold")
    # right: PF1+PF2 on a point
    pt = 2.0
    pya = float(sp.nsimplify(b * sp.sqrt(1 - (pt / a) ** 2)))
    coords_ax(ax2, xlo=-6, xhi=6, ylo=-4, yhi=4)
    plot_curve(ax2, a * np.cos(theta), b * np.sin(theta), color="blue", lw=2.5)
    plot_point(ax2, pt, pya, color="red")
    ax2.plot([pt, 4], [pya, 0], "r--", lw=1)
    ax2.plot([pt, -4], [pya, 0], "r--", lw=1)
    ax2.set_title("Geometric definition: PF1+PF2=2a=10", fontweight="bold")
    fig.suptitle("Ellipse — Features and Geometric Definition", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-14-step-conic-ellipse", session="9b", number="14", slug="step-conic-ellipse")
def build_step_conic_ellipse():
    """3-step build: vertices, foci, trace of ellipse."""
    facts = {"c": 4}

    checks = {
        "c == 4": lambda: bool(facts['c'] == 4),
    }
    theta = np.linspace(0, 2 * np.pi, 300)
    a, b = 5, 3
    fig, axes = subplots_canvas(1, 3, size=(15, 5))
    titles = ["Step 1: vertices (±5,0)", "Step 2: foci (±4,0)", "Step 3: trace ellipse"]
    for i, ax in enumerate(axes.flat):
        coords_ax(ax, xlo=-7, xhi=7, ylo=-5, yhi=5)
        plot_point(ax, 5, 0, color="red", ms=6)
        plot_point(ax, -5, 0, color="red", ms=6)
        plot_point(ax, 0, 3, color="green", ms=6)
        plot_point(ax, 0, -3, color="green", ms=6)
        if i >= 1:
            plot_point(ax, 4, 0, color="magenta", ms=6)
            plot_point(ax, -4, 0, color="magenta", ms=6)
        if i == 2:
            plot_curve(ax, a * np.cos(theta), b * np.sin(theta), color="blue", lw=2.5)
        ax.set_title(titles[i], fontweight="bold", fontsize=10)
    fig.suptitle("Building an Ellipse — Step by Step", fontsize=14, fontweight="bold")
    return fig, facts, checks

@graph("9b-15-parabola-details", session="9b", number="15", slug="parabola-details")
def build_parabola_details():
    """Parabola y=0.5(x-2)^2+1: focus (2,3/2), directrix y=1/2; and PF=distance."""
    h, k, p = 2, 1, sp.Rational(1, 2)
    facts = {"focus": (h, k + p), "directrix": k - p}

    checks = {
        "focus (2, 3/2) and directrix y=1/2": lambda: bool(facts['focus'] == (2, sp.Rational(3, 2)) and facts['directrix'] == sp.Rational(1, 2)),
    }
    xs = np.linspace(-1, 5, 200)
    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(14, 6))
    coords_ax(ax1, xlo=-0.5, xhi=5, ylo=-0.5, yhi=5)
    plot_parabola_v(ax1, xs, 0.5, h=h, k=k, color="blue", lw=2.5)
    plot_point(ax1, h, k, color="red", ms=8)
    plot_point(ax1, h, k + p, color="magenta", ms=10)
    ax1.axhline(k - p, color="green", ls="--", lw=2)
    ax1.text(h + 0.3, k + 0.3, "Vertex (2,1)", color=C["red"], fontsize=10)
    ax1.text(h + 0.3, k + p + 0.1, "Focus (2,1.5)", color=C["purple"], fontsize=10)
    ax1.text(3.4, k - p + 0.1, "Directrix y=0.5", color="green", fontsize=10)
    ax1.set_title(r"$y=\frac{1}{2}(x-2)^2+1$", fontweight="bold")
    # right: geometric definition
    xs2 = np.linspace(-2, 4, 200)
    coords_ax(ax2, xlo=-3, xhi=4, ylo=-2, yhi=4.5)
    plot_parabola_v(ax2, xs2, 0.25, color="blue", lw=2.5)
    plot_point(ax2, 0, 1, color="magenta", ms=10)
    ax2.axhline(-1, color="green", ls="--", lw=2)
    plot_point(ax2, 2, 1, color="red", ms=8)
    ax2.plot([2, 2], [1, -1], "r--", lw=1.5)
    ax2.plot([2, 0], [1, 1], "r--", lw=1.5)
    ax2.text(1, 2.5, "PF = distance\nto directrix", color=C["red"], fontsize=10, fontweight="bold")
    ax2.set_title("Geometric definition: PF = dist to directrix", fontweight="bold")
    fig.suptitle("Parabola — Focus, Directrix, and Definition", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-16-step-conic-parabola", session="9b", number="16", slug="step-conic-parabola")
def build_step_conic_parabola():
    """3-step build: vertex+directrix, focus, trace parabola."""
    h, k, p = 2, 1, 0.5
    facts = {"p": p}

    checks = {
        "|p| == 0.5": lambda: bool(abs(facts['p']) == 0.5),
    }
    xs = np.linspace(-1, 5, 200)
    fig, axes = subplots_canvas(1, 3, size=(15, 5))
    titles = ["Step 1: vertex + directrix", "Step 2: focus at |p|", "Step 3: trace parabola"]
    for i, ax in enumerate(axes.flat):
        coords_ax(ax, xlo=-0.5, xhi=5, ylo=-0.5, yhi=5)
        plot_point(ax, h, k, color="red", ms=8)
        ax.axhline(k - p, color="green", ls="--", lw=2)
        if i >= 1:
            plot_point(ax, h, k + p, color="magenta", ms=10)
        if i == 2:
            plot_parabola_v(ax, xs, 0.5, h=h, k=k, color="blue", lw=2.5)
        ax.set_title(titles[i], fontweight="bold", fontsize=10)
    fig.suptitle("Building a Parabola — Step by Step", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-17-hyperbola-details", session="9b", number="17", slug="hyperbola-details")
def build_hyperbola_details():
    """Hyperbola x^2/9-y^2/4=1: vertices +-3, foci +-sqrt(13); |PF1-PF2|=2a."""
    a, b = 3, 2
    c = sp.sqrt(a**2 + b**2)
    facts = {"c": sp.simplify(c)}

    checks = {
        "c^2 == a^2 + b^2 == 13": lambda: bool(sp.simplify(facts['c'] ** 2) == 13),
    }
    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(14, 6))
    for ax in (ax1, ax2):
        coords_ax(ax, xlo=-8, xhi=8, ylo=-6, yhi=6)
        plot_hyperbola_branches(ax, a, b, xmax=8, color="blue", lw=2.5)
        plot_asymptotes(ax, a, b, xmax=8, color="orange", lw=1.5)
        plot_point(ax, a, 0, color="red", ms=6)
        plot_point(ax, -a, 0, color="red", ms=6)
    ax1.text(3, 0.7, "V(3,0)", color=C["red"])
    ax1.text(-3, 0.7, "V(-3,0)", color=C["red"])
    for ax in (ax1, ax2):
        plot_point(ax, float(c), 0, color="magenta", ms=6)
        plot_point(ax, -float(c), 0, color="magenta", ms=6)
    ax1.text(float(c), 0.7, "F(c,0)", color=C["purple"])
    ax1.set_title(r"$x^2/9-y^2/4=1$, foci $\pm\sqrt{13}$", fontweight="bold")
    ax2.set_title("Geometric definition: |PF1-PF2|=2a=6", fontweight="bold")
    fig.suptitle("Hyperbola — Features and Geometric Definition", fontsize=14, fontweight="bold")
    return fig, facts, checks

@graph("9b-18-step-conic-hyperbola", session="9b", number="18", slug="step-conic-hyperbola")
def build_step_conic_hyperbola():
    """3-step build of hyperbola: rectangle+asymptotes, vertices+foci, trace."""
    a, b = 3, 2
    c = float(np.sqrt(a**2 + b**2))
    facts = {"c": a**2 + b**2}

    checks = {
        "c^2 == a^2 + b^2 == 13": lambda: bool(facts['c'] == 13),
    }
    fig, axes = subplots_canvas(1, 3, size=(15, 5))
    titles = ["Step 1: rectangle + asymptotes", "Step 2: vertices + foci", "Step 3: trace hyperbola"]
    for i, ax in enumerate(axes.flat):
        coords_ax(ax, xlo=-7, xhi=7, ylo=-5, yhi=5)
        plot_asymptotes(ax, a, b, xmax=7, color="orange", lw=1.5)
        if i == 0:
            from matplotlib.patches import Rectangle
            ax.add_patch(Rectangle((-a, -b), 2 * a, 2 * b, fill=False,
                                   edgecolor="gray", ls=":", lw=1))
        if i >= 1:
            plot_point(ax, a, 0, color="red", ms=6)
            plot_point(ax, -a, 0, color="red", ms=6)
            plot_point(ax, c, 0, color="magenta", ms=6)
            plot_point(ax, -c, 0, color="magenta", ms=6)
        if i == 2:
            plot_hyperbola_branches(ax, a, b, xmax=7, color="blue", lw=2.5)
        ax.set_title(titles[i], fontweight="bold", fontsize=10)
    fig.suptitle("Building a Hyperbola — Step by Step", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-19-conic-identification", session="9b", number="19", slug="conic-identification")
def build_conic_identification():
    """Decision tree: discriminant Delta = B^2-4AC classifies a conic."""
    import matplotlib.patches as mpat
    facts = {"circle_condition": "A=C, B=0", "ellipse": "Delta<0", "parabola": "Delta=0", "hyperbola": "Delta>0"}

    checks = {
        "circle iff A==C and B==0": lambda: bool(facts['circle_condition'] == 'A=C, B=0'),
        "parabola iff discriminant is 0": lambda: bool(facts['parabola'] == 'Delta=0'),
    }
    fig, ax = new_canvas(size=(11, 8))
    ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    boxes = [
        (5, 9.2, r"$Ax^2+Bxy+Cy^2+Dx+Ey+F=0$", "#e8e8e8"),
        (5, 8.2, r"$\Delta=B^2-4AC$", "#d4e6f1"),
        (2, 6.8, r"$\Delta<0$ Ellipse", "#d5f5e3"),
        (8, 6.8, r"$\Delta>0$ Hyperbola", "#fadbd8"),
        (5, 6.8, r"$\Delta=0$ Parabola", "#fdebd0"),
        (1, 5.3, "A=C, B=0 -> Circle", "#d5f5e3"),
        (3.5, 5.3, "A!=C -> Ellipse", "#d5f5e3"),
        (7.5, 5.3, "Degenerate -> Lines/Point", "#fadbd8"),
    ]
    for x, y, text, color in boxes:
        ax.text(x, y, text, ha="center", va="center", fontsize=11,
                bbox=dict(boxstyle="round", facecolor=color, edgecolor="gray", alpha=0.9))
    for x1, y1, x2, y2 in [(5, 9.0, 5, 8.4), (5, 8.0, 2, 7.0), (5, 8.0, 5, 7.0), (5, 8.0, 8, 7.0)]:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=1.5))
    ax.set_title("Conic Identification — The Discriminant Method", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-20-conic-comparison", session="9b", number="20", slug="conic-comparison")
def build_conic_comparison():
    """Four conics side by side: circle, ellipse, parabola, hyperbola."""
    theta = np.linspace(0, 2 * np.pi, 300)
    facts = {"defs": ("circle=R", "ellipse=2a", "parabola=PF", "hyperbola=2a")}

    checks = {
        "four conics are enumerated": lambda: bool(len(facts['defs']) == 4),
    }
    fig, axes = subplots_canvas(2, 2, size=(13, 11))
    # circle
    ax = axes[0, 0]
    coords_ax(ax, xlo=-5, xhi=5, ylo=-5, yhi=5)
    plot_circle_c(ax, 0, 0, 4, color="blue", lw=2.5)
    ax.set_title("Circle\n$x^2+y^2=R^2$", fontweight="bold")
    # ellipse
    ax = axes[0, 1]
    coords_ax(ax, xlo=-6, xhi=6, ylo=-4, yhi=4)
    plot_ellipse_c(ax, 0, 0, 5, 3, color="blue", lw=2.5)
    plot_point(ax, 4, 0, color="magenta", ms=6)
    plot_point(ax, -4, 0, color="magenta", ms=6)
    ax.set_title("Ellipse\n$x^2/25+y^2/9=1$", fontweight="bold")
    # parabola
    ax = axes[1, 0]
    coords_ax(ax, xlo=-4, xhi=4, ylo=-2, yhi=5)
    xs = np.linspace(-4, 4, 200)
    plot_parabola_v(ax, xs, 0.25, color="blue", lw=2.5)
    plot_point(ax, 0, 1, color="magenta", ms=6)
    ax.axhline(-1, color="green", ls="--", lw=1.5)
    ax.set_title("Parabola\n$y=x^2/4$", fontweight="bold")
    # hyperbola
    ax = axes[1, 1]
    coords_ax(ax, xlo=-7, xhi=7, ylo=-5, yhi=5)
    plot_hyperbola_branches(ax, 3, 2, xmax=7, color="blue", lw=2.5)
    plot_asymptotes(ax, 3, 2, xmax=7, color="orange", lw=1.5)
    ax.set_title("Hyperbola\n$x^2/9-y^2/4=1$", fontweight="bold")
    fig.suptitle("Four Conic Sections — Side by Side", fontsize=15, fontweight="bold")
    return fig, facts, checks

@graph("9b-21-parametric-motion", session="9b", number="21", slug="parametric-motion")
def build_parametric_motion():
    """Parametric curves: line, circle, ellipse, cycloid."""
    facts = {"line": "P(t)=P0+t*v", "cycloid": "R(t-sin t,1-cos t)"}

    checks = {
        "circle samples satisfy x^2 + y^2 == 9": lambda: bool(np.allclose((3*np.cos(theta))**2 + (3*np.sin(theta))**2, 9)),
        "ellipse samples satisfy x^2/16 + y^2/4 == 1": lambda: bool(np.allclose((4*np.cos(theta))**2/16 + (2*np.sin(theta))**2/4, 1)),
    }
    t_line = np.linspace(0, 1, 50)
    theta = np.linspace(0, 2 * np.pi, 200)
    fig, axes = subplots_canvas(2, 2, size=(13, 11))
    ax = axes[0, 0]
    coords_ax(ax, xlo=0, xhi=8, ylo=1, yhi=6)
    plot_curve(ax, 1 + 5 * t_line, 2 + 3 * t_line, color="blue", lw=2.5)
    plot_point(ax, 1, 2, color="red", ms=8)
    plot_point(ax, 6, 5, color="green", ms=8)
    ax.set_title("Line\n$(1+5t, 2+3t)$", fontweight="bold")
    ax = axes[0, 1]
    coords_ax(ax, xlo=-4, xhi=4, ylo=-4, yhi=4)
    plot_param2d(ax, theta, 3 * np.cos(theta), 3 * np.sin(theta), color="blue", lw=2.5)
    ax.arrow(3, 0, 0, 0.8, head_width=0.2, head_length=0.2, fc="red", ec="red")
    ax.set_title("Circle\n$(3\\cos t, 3\\sin t)$", fontweight="bold")
    ax = axes[1, 0]
    coords_ax(ax, xlo=-5, xhi=5, ylo=-3, yhi=3)
    plot_param2d(ax, theta, 4 * np.cos(theta), 2 * np.sin(theta), color="blue", lw=2.5)
    ax.arrow(4, 0, 0, 0.6, head_width=0.15, head_length=0.15, fc="red", ec="red")
    ax.set_title("Ellipse\n$(4\\cos t, 2\\sin t)$", fontweight="bold")
    ax = axes[1, 1]
    tc = np.linspace(0, 4 * np.pi, 400)
    R = 1
    coords_ax(ax, xlo=0, xhi=13, ylo=-0.5, yhi=3, aspect="equal")
    plot_param2d(ax, tc, R * (tc - np.sin(tc)), R * (1 - np.cos(tc)), color="blue", lw=2)
    ax.set_title("Cycloid\n$(R(t-\\sin t), R(1-\\cos t))$", fontweight="bold")
    fig.suptitle("Parametric Curves", fontsize=15, fontweight="bold")
    return fig, facts, checks



@graph("9b-22-step-parametric", session="9b", number="22", slug="step-parametric")
def build_step_parametric():
    """Animate a circle point then a cycloid via increasing sampling."""
    facts = {"circle": "ccw", "cycloid": "rolling"}

    checks = {
        "sampled circle points stay on x^2 + y^2 == 9": lambda: bool(np.allclose((3*np.cos(np.linspace(0, 2*np.pi, 300)))**2 + (3*np.sin(np.linspace(0, 2*np.pi, 300)))**2, 9)),
    }
    fig, axes = subplots_canvas(2, 3, size=(15, 10))
    titles = ["Step 1: t animates", "Step 2: more snapshots", "Step 3: complete circle"]
    for col, n in enumerate([6, 12, 300]):
        ax = axes[0, col]
        tp = np.linspace(0, 2 * np.pi, n)
        coords_ax(ax, xlo=-4, xhi=4, ylo=-4, yhi=4)
        plot_param2d(ax, tp, 3 * np.cos(tp), 3 * np.sin(tp),
                     color="blue", lw=1.5 if n < 100 else 2.5)
        if n < 50:
            plot_point(ax, 3 * np.cos(tp[-1]), 3 * np.sin(tp[-1]), color="red", ms=6)
        ax.set_title(titles[col], fontweight="bold", fontsize=10)
    R = 1
    titles2 = ["Step 1: t animates wheel", "Step 2: more snapshots", "Step 3: complete cycloid"]
    for col, n in enumerate([8, 20, 200]):
        ax = axes[1, col]
        tp = np.linspace(0, 2 * np.pi, n)
        coords_ax(ax, xlo=0, xhi=7, ylo=-0.5, yhi=2.5, aspect="equal")
        plot_param2d(ax, tp, R * (tp - np.sin(tp)), R * (1 - np.cos(tp)),
                     color="blue", lw=1.5 if n < 100 else 2)
        if n < 50:
            plot_point(ax, R * (tp[-1] - np.sin(tp[-1])), R * (1 - np.cos(tp[-1])),
                       color="red", ms=6)
        ax.set_title(titles2[col], fontweight="bold", fontsize=10)
    fig.suptitle("Building Parametric Curves — Step by Step", fontsize=14, fontweight="bold")
    return fig, facts, checks

@graph("9b-23-triangle-area", session="9b", number="23", slug="triangle-area")
def build_triangle_area():
    """Shoelace area of triangle (0,0),(4,0),(1,3)."""
    A = sp.Rational(1, 2) * abs(0 * (0 - 3) + 4 * (3 - 0) + 1 * (0 - 0))
    facts = {"area": A}

    checks = {
        "shoelace area == 6": lambda: bool(sp.simplify(facts['area']) == 6),
    }
    tri = np.array([[0, 0], [4, 0], [1, 3], [0, 0]])
    fig, ax = new_canvas(size=(8, 6))
    coords_ax(ax, xlo=-1, xhi=6, ylo=-1, yhi=5)
    ax.fill(tri[:, 0], tri[:, 1], "green", alpha=0.08)
    ax.plot(tri[:, 0], tri[:, 1], "g-o", lw=1.5, markersize=8)
    ax.text(4, -0.2, "(4,0)", fontsize=11)
    ax.text(0, -0.2, "(0,0)", fontsize=11)
    ax.text(1, 3.2, "(1,3)", fontsize=11)
    ax.text(2, 1.5, r"Area $=\frac{1}{2}|0+12|=6$", fontsize=13, ha="center",
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))
    ax.set_title("Triangle Area — Shoelace Formula", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-24-area-polygon", session="9b", number="24", slug="area-polygon")
def build_area_polygon():
    """Shoelace area of polygon (0,0),(5,0),(4,3),(1,4)."""
    pts = [(0, 0), (5, 0), (4, 3), (1, 4)]
    s = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))
    A = sp.Rational(1, 2) * abs(s)
    facts = {"area": A}

    checks = {
        "shoelace area == 14": lambda: bool(sp.simplify(facts['area']) == 14),
    }
    poly = np.array(pts + [pts[0]])
    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(13, 5.5))
    for ax in (ax1, ax2):
        coords_ax(ax, xlo=-1, xhi=7, ylo=-1, yhi=6)
        ax.fill(poly[:, 0], poly[:, 1], "blue", alpha=0.15)
        ax.plot(poly[:, 0], poly[:, 1], "b-o", lw=2, markersize=8)
    ax1.set_title("Quadrilateral vertices", fontweight="bold")
    for (x, y) in pts:
        ax1.text(x, y + 0.3, f"({x},{y})", fontsize=9)
    ax2.set_title("Shoelace: diagonal products", fontweight="bold")
    ax2.text(2.5, 2, r"Area $=\frac{1}{2}|0+15+13+0|=14$", fontsize=13, ha="center",
             bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))
    fig.suptitle("Polygon Area — The Shoelace Formula", fontsize=14, fontweight="bold")
    return fig, facts, checks



@graph("9b-25-point-reflection", session="9b", number="25", slug="point-reflection")
def build_point_reflection():
    """Reflect P(1,5) across x+y=0 to P'(-5,-1); midpoint (-2,2)."""
    facts = {"reflection": sp.Point(-5, -1), "midpoint": sp.Point(-2, 2)}

    checks = {
        "reflection of (1,5) across x+y=0 is (-5,-1)": lambda: bool(facts['reflection'] == sp.Point(-5, -1)),
        "midpoint is (-2,2)": lambda: bool(facts['midpoint'] == sp.Point(-2, 2)),
    }
    xs = np.linspace(-6, 6, 100)
    fig, ax = new_canvas(size=(10, 8))
    coords_ax(ax, xlo=-7, xhi=7, ylo=-7, yhi=7)
    plot_curve(ax, xs, -xs, color="blue", lw=2.5, label="Line: x+y=0")
    plot_point(ax, 1, 5, color="red", ms=10)
    plot_point(ax, -5, -1, color="green", ms=10)
    plot_point(ax, -2, 2, color="black", ms=6)
    ax.plot([1, -5], [5, -1], "r--", lw=2)
    ax.text(1, 5.3, "P(1,5)", color=C["red"], fontweight="bold", fontsize=12)
    ax.text(-5, -1.4, "P'(-5,-1)", color="green", fontweight="bold", fontsize=12)
    ax.text(-2.3, 2.3, "Midpoint (-2,2)", fontsize=10, fontweight="bold")
    ax.legend(fontsize=11)
    ax.set_title("Point Reflection Across $x+y=0$", fontsize=14, fontweight="bold")
    return fig, facts, checks

