"""Migrated 14D / 14D1 session graphs, rebuilt on the shared viz/verify core.

Builds the seven graphs referenced by:
  - sessions/phase2/14D-relation-lens.md         (d1, d2)
  - sessions/phase2/14D1-derivative-interpretation.md  (d3..d7)

Each builder:
  1. verifies the relevant math with verify.symbolic,
  2. renders only through viz.primitives,
  3. returns (fig, facts, path) so tests can check claims and the exporter
     writes to the canonical graphs/<session>/<nn>-<slug>.png location.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

from viz.canvas import new_canvas, simple_axes
from viz.primitives import (
    plot_curve, plot_tangent, plot_point, add_callout,
    plot_region, plot_circle, plot_ring, plot_shell_3d,
)
from viz.theme import PALETTE
from viz.export import graph_path
from verify.symbolic import simplify_true, slope_of_implicit


# ─────────────────────────── d1: derivative units ───────────────────────────
def build_d1():
    """s=1/2 t^2 (m/s) and C=q^2+4q+144 ($/unit), each with a tangent."""
    import matplotlib.pyplot as plt

    t, q = sp.symbols("t q")
    m_t = simplify_true(sp.diff(sp.Rational(1, 2) * t**2, t).subs(t, 2))      # 2 m/s
    C = q**2 + 4 * q + 144
    m_q = simplify_true(sp.diff(C, q).subs(q, 12))                            # 28 $/unit
    facts = {"slope_mps_at_2": m_t, "mc_at_12": m_q, "C12": int(C.subs(q, 12))}

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in (ax1, ax2):
        simple_axes(ax)
    # panel 1: position
    tt = np.linspace(0, 6, 400)
    plot_curve(ax1, tt, 0.5 * tt**2, label=r"$s(t)=\frac{1}{2} t^2$ [m]")
    plot_tangent(ax1, 2.0, 2.0, 2.0, half=2.0, label="tangent at $t=2$")
    plot_point(ax1, 2.0, 2.0)
    ax1.set_xlabel("time $t$ [s]"); ax1.set_ylabel("position $s$ [m]")
    ax1.set_ylim(0, 20)
    ax1.set_title(r"Position: $s'$ has units m/s", fontweight="bold")
    # panel 2: cost
    qq = np.linspace(0, 24, 400)
    plot_curve(ax2, qq, qq**2 + 4 * qq + 144, label=r"$C(q)=q^2+4q+144$ [$]", color="green")
    # tangent at q=12: slope 28, C(12)=336 -> y = 28q + (336-336) = 28q
    plot_tangent(ax2, 12.0, 336.0, 28.0, half=4.0, color="purple", label="tangent at $q=12$")
    plot_point(ax2, 12.0, 336.0, color="purple")
    ax2.set_xlabel("quantity $q$ [units]"); ax2.set_ylabel(r"cost $C$ [$]")
    ax2.set_ylim(0, 900)
    ax2.set_title(r"Cost: $C'$ has units $/unit", fontweight="bold")
    path = graph_path("14d", "01", "derivative-units")
    return fig, facts, path


# ─────────────────────────── d2: motion story ───────────────────────────
def build_d2():
    """v=t^2-4t+3, a=2t-4 with sign regions and a motion timeline."""
    import matplotlib.pyplot as plt

    t = sp.symbols("t")
    roots = sorted(int(r) for r in sp.solve(t**2 - 4 * t + 3, t))
    facts = {"turn_points": roots}
    assert roots == [1, 3]

    fig = plt.figure(figsize=(10, 6.2))
    ax1 = fig.add_subplot(211); simple_axes(ax1)
    tt = np.linspace(0, 4.6, 600)
    v = tt**2 - 4 * tt + 3
    a = 2 * tt - 4
    plot_curve(ax1, tt, v, label=r"$v(t)=t^2-4t+3$")
    plot_curve(ax1, tt, a, label=r"$a(t)=2t-4$", color="red", ls="--")
    plot_region(ax1, tt, v, baseline=0, where=v > 0, color="blue")
    ax1.axhline(0, color="#888", lw=1)
    for xr in (1, 3):
        ax1.axvline(xr, color=PALETTE["gray"], lw=0.8, alpha=0.5)
    ax1.set_xlim(0, 4.6); ax1.set_ylim(-3.6, 4.2)
    ax1.set_title("The motion story: signs of $v$ and $a$ together", fontweight="bold")

    ax2 = fig.add_subplot(212); simple_axes(ax2)
    ax2.set_xlim(0, 4.6); ax2.set_ylim(0, 1); ax2.set_yticks([])
    zones = [
        (0, 1, "v>0, a<0\nforward, slowing", "blue"),
        (1, 2, "v<0, a<0\nbackward, speeding", "red"),
        (2, 3, "v<0, a>0\nbackward, slowing", "amber"),
        (3, 4.6, "v>0, a>0\nforward, speeding", "green"),
    ]
    for x0, x1, label, col in zones:
        ax2.axvspan(x0, x1, color=PALETTE[col], alpha=0.25)
        ax2.text((x0 + x1) / 2, 0.55, label, ha="center", va="center", fontsize=9,
                 color=PALETTE[col], fontweight="bold")
    for xr in (1, 2, 3):
        ax2.plot([xr, xr], [0, 1], color=PALETTE["gray"], lw=1)
    ax2.set_xlabel("time $t$ [s]")
    ax2.set_title("Motion timeline", fontweight="bold", fontsize=11)
    fig.tight_layout()
    path = graph_path("14d", "02", "motion-story")
    return fig, facts, path


# ─────────────────────────── d3: linearization ───────────────────────────
def build_d3():
    """sqrt(x), tangent at x=4, zoom inset at x=4.1."""
    import matplotlib.pyplot as plt

    x = sp.symbols("x", positive=True)
    f = sp.sqrt(x)
    m4 = simplify_true(sp.diff(f, x).subs(x, 4))          # 1/4
    L41 = f.subs(x, 4) + m4 * (sp.Rational(41, 10) - 4)   # 2.025
    facts = {"fprime_4": m4, "L_4_1": L41}
    assert m4 == sp.Rational(1, 4)

    fig, ax = plt.subplots(figsize=(9, 5)); simple_axes(ax)
    xx = np.linspace(0, 9, 900)
    plot_curve(ax, xx, np.sqrt(xx), label=r"$f(x)=\sqrt{x}$")
    plot_tangent(ax, 4.0, 2.0, 0.25, half=4.0, label=r"$L(x)=2+\frac{x-4}{4}$")
    plot_point(ax, 4.0, 2.0)
    plot_point(ax, 4.1, 2.0248, color="blue", ms=6)
    ax.set_xlim(0, 9); ax.set_ylim(0, 3.2)
    ax.set_title("Linearization: the tangent is the best local model", fontweight="bold")
    ax.set_xlabel("$x$"); ax.set_ylabel("$y$")
    ins = ax.inset_axes([0.18, 0.15, 0.42, 0.38])
    xz = np.linspace(3.9, 4.3, 600)
    ins.plot(xz, np.sqrt(xz), color=PALETTE["blue"], lw=2.5)
    ins.plot(xz, 2 + (xz - 4) / 4, color=PALETTE["red"], lw=2, ls="--")
    ins.plot([4.1], [2.0248], "o", color=PALETTE["blue"], ms=6)
    ins.plot([4.1], [2.025], "o", color=PALETTE["red"], ms=6)
    ins.set_xticks([]); ins.set_yticks([])
    ins.set_title("zoom", fontsize=8)
    fig.tight_layout()
    path = graph_path("14d1", "03", "linearization")
    return fig, facts, path


# ─────────────────────────── d4: circle ring ───────────────────────────
def build_d4():
    """A=pir^2; ring of width dr: area ~ 2 pi r dr."""
    r = sp.symbols("r")
    dA = sp.diff(sp.pi * r**2, r)
    facts = {"dA_dr": dA}
    assert simplify_true(dA) == 2 * sp.pi * r

    fig, ax = new_canvas(size=(7, 6.2)); simple_axes(ax, equal_aspect=True)
    plot_circle(ax, 0, 0, 3, color="blue")
    plot_ring(ax, 0, 0, 3.0, 0.45, color="amber")
    ax.plot([0, 3], [0, 0], color=PALETTE["blue"], lw=2)
    ax.plot([0, 3.45], [0, 0], color=PALETTE["amber"], lw=2, ls="--")
    ax.annotate(r"$r$", (1.5, 0.08), fontsize=12, color=PALETTE["blue"], fontweight="bold")
    ax.annotate(r"$dr$", (3.2, 0.12), fontsize=12, color=PALETTE["amber"], fontweight="bold")
    ax.set_xlim(-3.9, 3.9); ax.set_ylim(-3.6, 3.9)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(r"$dA/dr$ = circumference: growth happens on the boundary",
                 fontweight="bold")
    path = graph_path("14d1", "04", "circle-ring")
    return fig, facts, path


# ─────────────────────────── d5: sphere shell ───────────────────────────
def build_d5():
    """3D sphere + shell of thickness dr: dV/dr = 4 pi r^2."""
    r = sp.symbols("r")
    dV = sp.diff(sp.Rational(4, 3) * sp.pi * r**3, r)
    facts = {"dV_dr": dV}
    assert simplify_true(dV) == 4 * sp.pi * r**2

    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(8, 6.8))
    ax = fig.add_subplot(111, projection="3d")
    plot_shell_3d(ax, R=3.0, dr=0.5, inner_color="blue", outer_color="amber")
    ax.quiver(0, 0, 0, 3.0, 0, 0, color=PALETTE["blue"], lw=2.5, arrow_length_ratio=0.08)
    ax.text(0, 0, 4.1, r"$V=\frac{4}{3}\pi r^3 \Rightarrow \frac{dV}{dr}=4\pi r^2$",
            fontsize=11, color=PALETTE["blue"], fontweight="bold", ha="center")
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.set_title(r"$dV/dr$ = surface area: a thin shell wraps the sphere",
                 fontweight="bold")
    path = graph_path("14d1", "05", "sphere-shell")
    return fig, facts, path


# ─────────────────────────── d6: marginal cost ───────────────────────────
def build_d6():
    """MC=2q+4 crosses AC=q+4+144/q at the min of AC (q=12)."""
    import matplotlib.pyplot as plt

    q = sp.symbols("q", positive=True)
    MC = 2 * q + 4
    AC = q + 4 + 144 / q
    cross = [int(s) for s in sp.solve(sp.Eq(MC, AC), q) if s.is_real]
    facts = {"MC_AC_cross": cross}
    assert cross == [12]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in (ax1, ax2):
        simple_axes(ax)
    qq = np.linspace(0.1, 24, 500)
    C = qq**2 + 4 * qq + 144
    plot_curve(ax1, qq, C, label=r"$C(q)=q^2+4q+144$", color="green")
    plot_tangent(ax1, 12.0, 336.0, 28.0, half=4.0, color="purple")
    plot_point(ax1, 12.0, 336.0, color="purple")
    ax1.set_xlabel("$q$ [units]"); ax1.set_ylabel(r"cost [$]")
    ax1.set_ylim(0, 750)
    ax1.set_title("Tangent slope = cost of the next unit", fontweight="bold")
    ax2.plot(qq, 2 * qq + 4, color=PALETTE["red"], lw=2.5, label=r"$MC=C'(q)=2q+4$")
    ax2.plot(qq, qq + 4 + 144 / qq, color=PALETTE["blue"], lw=2.2, label=r"$AC=C(q)/q$")
    plot_point(ax2, 12.0, 28.0, color="gray")
    ax2.set_xlabel("$q$ [units]"); ax2.set_ylabel(r"cost per unit [$/unit]")
    ax2.set_ylim(0, 80)
    ax2.set_title(r"Marginal meets average at the average's minimum", fontweight="bold")
    fig.tight_layout()
    path = graph_path("14d1", "06", "marginal-cost")
    return fig, facts, path


# ─────────────────────────── d7: elasticity ───────────────────────────
def build_d7():
    """q=500-10p; E=-1 & revenue max at p=25."""
    import matplotlib.pyplot as plt

    p = sp.symbols("p")
    qq = 500 - 10 * p
    E = p / qq * sp.diff(qq, p)
    R = p * qq
    pcrit = [int(s) for s in sp.solve(sp.Eq(sp.diff(R, p), 0), p) if s.is_real]
    facts = {"elasticity_at_25": simplify_true(E.subs(p, 25)), "rev_max_p": pcrit}
    assert simplify_true(E.subs(p, 25)) == -1

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in (ax1, ax2):
        simple_axes(ax)
    pp = np.linspace(0, 50, 600)
    qval = 500 - 10 * pp
    plot_curve(ax1, pp, qval, label=r"demand $q=500-10p$")
    plot_region(ax1, pp, qval, baseline=0, where=pp < 25, color="amber")
    plot_region(ax1, pp, qval, baseline=0, where=pp > 25, color="red")
    plot_point(ax1, 25.0, 250.0, color="gray")
    ax1.text(10, 110, "elastic $|E|>1$", color=PALETTE["red"], fontsize=9, fontweight="bold")
    ax1.text(32, 300, "inelastic $|E|<1$", color=PALETTE["amber"], fontsize=9, fontweight="bold")
    ax1.set_xlabel(r"price $p$ [$]"); ax1.set_ylabel("quantity $q$")
    ax1.set_ylim(0, 520)
    ax1.set_title("Demand: elasticity changes along the curve", fontweight="bold")
    Rval = pp * qval
    plot_curve(ax2, pp, Rval, label=r"revenue $R=p\,q(p)$", color="green")
    plot_point(ax2, 25.0, 6250.0, color="red")
    ax2.set_xlabel(r"price $p$ [$]"); ax2.set_ylabel(r"revenue [$]")
    ax2.set_ylim(0, 7000)
    ax2.set_title("Revenue is maximized where $E=-1$", fontweight="bold")
    fig.tight_layout()
    path = graph_path("14d1", "07", "elasticity")
    return fig, facts, path


ALL_BUILDERS = {
    "14d-01-derivative-units": build_d1,
    "14d-02-motion-story": build_d2,
    "14d1-03-linearization": build_d3,
    "14d1-04-circle-ring": build_d4,
    "14d1-05-sphere-shell": build_d5,
    "14d1-06-marginal-cost": build_d6,
    "14d1-07-elasticity": build_d7,
}


def build_all():
    """Run every builder and return {name: (facts, path)} without saving."""
    out = {}
    for name, fn in ALL_BUILDERS.items():
        fig, facts, path = fn()
        out[name] = (facts, path)
    return out