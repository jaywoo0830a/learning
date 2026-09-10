"""Migrated 14D / 14D1 session graphs, rebuilt on the shared viz/verify core.

Builds the seven graphs referenced by:
  - sessions/phase2/14D-relation-lens.md         (d1, d2)
  - sessions/phase2/14D1-derivative-interpretation.md  (d3..d7)

Each builder:
  1. verifies the relevant math with verify.symbolic and attaches it as
     ``checks`` (name -> () -> bool) so tests can run all claims uniformly,
  2. renders only through viz.primitives / the chainable ``G`` builder,
  3. is registered via ``@graph`` — the single source of truth for its id and
     canonical ``graphs/<session>/<nn>-<slug>.png`` location.
"""
from __future__ import annotations

import matplotlib.pyplot as plt  # module-level only (3D axis special case)
import numpy as np
import sympy as sp

from viz.canvas import simple_axes, subplots_canvas
from viz.primitives import (
    plot_curve, plot_tangent, plot_point,
    plot_region, plot_circle, plot_ring, plot_shell_3d,
)
from viz.graph import G
from viz.theme import PALETTE
from viz.registry import graph
from verify.symbolic import simplify_true


# ─────────────────────────── d1: derivative units ───────────────────────────
@graph("14d-01-derivative-units", session="14d", number="01", slug="derivative-units")
def build_d1():
    """Return (fig, facts, checks): s=1/2 t^2 and C=q^2+4q+144, each with a tangent."""
    t, q = sp.symbols("t q")
    m_t = simplify_true(sp.diff(sp.Rational(1, 2) * t**2, t).subs(t, 2))   # 2 m/s
    C = q**2 + 4 * q + 144
    m_q = simplify_true(sp.diff(C, q).subs(q, 12))                          # 28 $/unit
    c12 = int(C.subs(q, 12))
    facts = {"slope_mps_at_2": m_t, "mc_at_12": m_q, "C12": c12}

    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(11, 4.6))
    for ax in (ax1, ax2):
        simple_axes(ax)
    # panel 1: position
    tt = np.linspace(0, 6, 400)
    plot_curve(ax1, tt, 0.5 * tt**2, label=r"$s(t)=\frac{1}{2} t^2$ [m]")
    plot_tangent(ax1, 2.0, 2.0, float(m_t), half=2.0, label="tangent at $t=2$")
    plot_point(ax1, 2.0, 2.0)
    ax1.set_xlabel("time $t$ [s]"); ax1.set_ylabel("position $s$ [m]")
    ax1.set_ylim(0, 20)
    ax1.set_title(r"Position: $s'$ has units m/s", fontweight="bold")
    # panel 2: cost
    qq = np.linspace(0, 24, 400)
    plot_curve(ax2, qq, qq**2 + 4 * qq + 144, label=r"$C(q)=q^2+4q+144$ [$]", color="green")
    plot_tangent(ax2, 12.0, float(c12), float(m_q), half=4.0, color="purple",
                 label="tangent at $q=12$")
    plot_point(ax2, 12.0, float(c12), color="purple")
    ax2.set_xlabel("quantity $q$ [units]"); ax2.set_ylabel(r"cost $C$ [$]")
    ax2.set_ylim(0, 900)
    ax2.set_title(r"Cost: $C'$ has units $/unit", fontweight="bold")

    checks = {
        "slope of s at t=2 is 2 m/s": lambda: bool(m_t == 2),
        "slope of C at q=12 is 28 $/unit": lambda: bool(m_q == 28),
        "C(12)=336": lambda: bool(c12 == 336),
    }
    return fig, facts, checks


# ─────────────────────────── d2: motion story ───────────────────────────
@graph("14d-02-motion-story", session="14d", number="02", slug="motion-story")
def build_d2():
    """Return (fig, facts, checks): v=t^2-4t+3, a=2t-4 with sign regions + timeline."""
    t = sp.symbols("t")
    roots = sorted(int(r) for r in sp.solve(t**2 - 4 * t + 3, t))
    facts = {"turn_points": roots}

    fig, (ax1, ax2) = subplots_canvas(2, 1, size=(10, 6.2))
    simple_axes(ax1)
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

    simple_axes(ax2)
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

    checks = {
        "v turns around at t=1 and t=3": lambda: bool(roots == [1, 3]),
        "a(1) < 0 and a(3) > 0": lambda: bool(
            simplify_true(sp.diff(t**2 - 4 * t + 3, t).subs(t, 1)) < 0
            and simplify_true(sp.diff(t**2 - 4 * t + 3, t).subs(t, 3)) > 0),
        "v vanishes at the turn points": lambda: bool(
            all(simplify_true((t**2 - 4 * t + 3).subs(t, r)) == 0 for r in roots)),
    }
    return fig, facts, checks


# ─────────────────────────── d3: linearization ───────────────────────────
@graph("14d1-03-linearization", session="14d1", number="03", slug="linearization")
def build_d3():
    """Return (fig, facts, checks): sqrt(x), tangent at x=4, zoom at x=4.1."""
    x = sp.symbols("x", positive=True)
    f = sp.sqrt(x)
    m4 = simplify_true(sp.diff(f, x).subs(x, 4))          # 1/4
    L41 = simplify_true(f.subs(x, 4) + m4 * (sp.Rational(41, 10) - 4))  # 81/40
    facts = {"fprime_4": m4, "L_4_1": L41}

    # single-axis graph via the chainable builder (curve + tangent + 2 points)
    g = G(size=(9, 5), title="Linearization: the tangent is the best local model")
    xx = np.linspace(0, 9, 900)
    g.curve(xx, np.sqrt(xx), label=r"$f(x)=\sqrt{x}$")
    g.tangent((4.0, 2.0), 0.25, half=4.0, label=r"$L(x)=2+\frac{x-4}{4}$")
    g.point((4.0, 2.0)).point((4.1, 2.0248), color="blue", ms=6)
    g.ax.set_xlim(0, 9); g.ax.set_ylim(0, 3.2)
    g.ax.set_xlabel("$x$"); g.ax.set_ylabel("$y$")
    ins = g.ax.inset_axes([0.18, 0.15, 0.42, 0.38])
    xz = np.linspace(3.9, 4.3, 600)
    ins.plot(xz, np.sqrt(xz), color=PALETTE["blue"], lw=2.5)
    ins.plot(xz, 2 + (xz - 4) / 4, color=PALETTE["red"], lw=2, ls="--")
    ins.plot([4.1], [2.0248], "o", color=PALETTE["blue"], ms=6)
    ins.plot([4.1], [2.025], "o", color=PALETTE["red"], ms=6)
    ins.set_xticks([]); ins.set_yticks([])
    ins.set_title("zoom", fontsize=8)
    fig, _garbage_facts, checks = g.build()
    checks.update({
        "f'(4) = 1/4": lambda: bool(m4 == sp.Rational(1, 4)),
        "L(4.1) = 81/40 = 2.025": lambda: bool(L41 == sp.Rational(81, 40)),
        "L(4) = f(4)": lambda: bool(simplify_true(f.subs(x, 4) + m4 * 0) == 2),
    })
    return fig, facts, checks


# ─────────────────────────── d4: circle ring ───────────────────────────
@graph("14d1-04-circle-ring", session="14d1", number="04", slug="circle-ring")
def build_d4():
    """Return (fig, facts, checks): A=pi r^2, ring of width dr ~ 2 pi r dr."""
    r = sp.symbols("r")
    dA = sp.diff(sp.pi * r**2, r)
    facts = {"dA_dr": dA}

    g = G(size=(7, 6.2), equal_aspect=True,
          title=r"$dA/dr$ = circumference: growth happens on the boundary")
    plot_circle(g.ax, 0, 0, 3, color="blue")
    plot_ring(g.ax, 0, 0, 3.0, 0.45, color="amber")
    g.ax.plot([0, 3], [0, 0], color=PALETTE["blue"], lw=2)
    g.ax.plot([0, 3.45], [0, 0], color=PALETTE["amber"], lw=2, ls="--")
    g.ax.annotate(r"$r$", (1.5, 0.08), fontsize=12, color=PALETTE["blue"], fontweight="bold")
    g.ax.annotate(r"$dr$", (3.2, 0.12), fontsize=12, color=PALETTE["amber"], fontweight="bold")
    g.ax.set_xlim(-3.9, 3.9); g.ax.set_ylim(-3.6, 3.9)
    g.ax.set_xticks([]); g.ax.set_yticks([])
    fig, _garbage_facts, checks = g.build()
    checks["dA/dr = 2 pi r (circumference)"] = lambda: bool(simplify_true(dA) == 2 * sp.pi * r)
    checks["ring width-dr area is 2 pi r dr to leading order"] = lambda: bool(
        sp.simplify(sp.expand(sp.pi * (r + 1) ** 2 - sp.pi * r**2) - 2 * sp.pi * r) == sp.pi)
    return fig, facts, checks


# ─────────────────────────── d5: sphere shell ───────────────────────────
@graph("14d1-05-sphere-shell", session="14d1", number="05", slug="sphere-shell")
def build_d5():
    """Return (fig, facts, checks): V=4/3 pi r^3, shell gives dV/dr = 4 pi r^2."""
    r = sp.symbols("r")
    dV = sp.diff(sp.Rational(4, 3) * sp.pi * r**3, r)
    facts = {"dV_dr": dV}

    fig = plt.figure(figsize=(8, 6.8))
    ax = fig.add_subplot(111, projection="3d")
    plot_shell_3d(ax, R=3.0, dr=0.5, inner_color="blue", outer_color="amber")
    ax.quiver(0, 0, 0, 3.0, 0, 0, color=PALETTE["blue"], lw=2.5, arrow_length_ratio=0.08)
    ax.text(0, 0, 4.1, r"$V=\frac{4}{3}\pi r^3 \Rightarrow \frac{dV}{dr}=4\pi r^2$",
            fontsize=11, color=PALETTE["blue"], fontweight="bold", ha="center")
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.set_title(r"$dV/dr$ = surface area: a thin shell wraps the sphere", fontweight="bold")

    checks = {"dV/dr = 4 pi r^2 (surface area)": lambda: bool(simplify_true(dV) == 4 * sp.pi * r**2)}
    return fig, facts, checks


# ─────────────────────────── d6: marginal cost ───────────────────────────
@graph("14d1-06-marginal-cost", session="14d1", number="06", slug="marginal-cost")
def build_d6():
    """Return (fig, facts, checks): MC crosses AC at the min of AC (q=12)."""
    q = sp.symbols("q", positive=True)
    MC = 2 * q + 4
    AC = q + 4 + 144 / q
    cross = [int(s) for s in sp.solve(sp.Eq(MC, AC), q) if s.is_real]
    facts = {"MC_AC_cross": cross}

    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(11, 4.6))
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

    checks = {
        "MC == AC at q=12": lambda: bool(cross == [12]),
        "AC has a minimum at q=12": lambda: bool(
            [int(s) for s in sp.solve(sp.Eq(sp.diff(AC, q), 0), q) if s.is_real] == [12]
            and sp.simplify(sp.diff(AC, q, 2)) > 0),
    }
    return fig, facts, checks


# ─────────────────────────── d7: elasticity ───────────────────────────
@graph("14d1-07-elasticity", session="14d1", number="07", slug="elasticity")
def build_d7():
    """Return (fig, facts, checks): q=500-10p; E=-1 & revenue max at p=25."""
    p = sp.symbols("p")
    qq_expr = 500 - 10 * p
    E = p / qq_expr * sp.diff(qq_expr, p)
    R = p * qq_expr
    pcrit = [int(s) for s in sp.solve(sp.Eq(sp.diff(R, p), 0), p) if s.is_real]
    e25 = simplify_true(E.subs(p, 25))
    facts = {"elasticity_at_25": e25, "rev_max_p": pcrit}

    fig, (ax1, ax2) = subplots_canvas(1, 2, size=(11, 4.6))
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

    checks = {
        "elasticity at p=25 is -1": lambda: bool(e25 == -1),
        "revenue is maximized at p=25": lambda: bool(
            pcrit == [25] and sp.simplify(sp.diff(R, p, 2)) < 0),
    }
    return fig, facts, checks