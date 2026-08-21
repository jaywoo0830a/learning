#!/usr/bin/env python3
"""Generate the session graphs for 14D (derivative interpretation) and 16C (integral interpretation).

Outputs into graphs/0821/14D and graphs/0821/16C (png).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0821')
for _sub in ('14D1', '16C1'):
    os.makedirs(os.path.join(BASE, _sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'
PURPLE = '#7b1fa2'
GRAY = '#666666'

def save(fig, sub, name):
    fig.savefig(os.path.join(BASE, sub, name), bbox_inches='tight')
    plt.close(fig)

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# ═══════════════════════════ 14D ═══════════════════════════

def d1_units():
    """Two panels: position vs time (m/s slope) and cost vs quantity ($/unit slope)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in (ax1, ax2): g(ax)

    t = np.linspace(0, 6, 400)
    s = 0.5 * t**2
    ax1.plot(t, s, BLUE, lw=2.5, label=r'$s(t)=\frac{1}{2} t^2$ [m]')
    ax1.plot(t, 2*t - 2, RED, lw=2, ls='--', label='tangent at $t=2$')
    ax1.plot([2], [2], 'o', color=RED, ms=7, zorder=6)
    ax1.annotate("slope $= 4\\,\\mathrm{m/s}$", (2, 2), xytext=(0.4, 12),
                 fontsize=10, color=RED, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))
    ax1.set_xlabel('time $t$ [s]'); ax1.set_ylabel('position $s$ [m]')
    ax1.set_title("Position: $s'$ has units m/s", fontweight='bold')
    ax1.set_ylim(0, 20); ax1.legend(fontsize=9, loc='upper left')

    q = np.linspace(0, 24, 400)
    C = q**2 + 4*q + 144
    ax2.plot(q, C, GREEN, lw=2.5, label=r'$C(q)=q^2+4q+144$ [\$]')
    ax2.plot(q, 28*q - 0*1, PURPLE, lw=2, ls='--', label='tangent at $q=12$')
    ax2.plot([12], [336], 'o', color=PURPLE, ms=7, zorder=6)
    ax2.annotate(r"slope $= 28\,\mathrm{\$/unit}$", (12, 336), xytext=(2, 560),
                 fontsize=10, color=PURPLE, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.2))
    ax2.set_xlabel('quantity $q$ [units]'); ax2.set_ylabel(r'cost $C$ [\$]')
    ax2.set_title(r"Cost: $C'$ has units \$/unit", fontweight='bold')
    ax2.set_ylim(0, 900); ax2.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14D1', '14d1-derivative-units.png')

def d2_motion_story():
    """v(t)=t^2-4t+3 and a(t)=2t-4 with speeding/slowing regions and a motion timeline."""
    fig = plt.figure(figsize=(10, 6.2))
    ax1 = fig.add_subplot(211); g(ax1)
    t = np.linspace(0, 4.6, 600)
    v = t**2 - 4*t + 3
    a = 2*t - 4
    ax1.plot(t, v, BLUE, lw=2.5, label=r'$v(t)=t^2-4t+3$')
    ax1.plot(t, a, RED, lw=2.2, ls='--', label=r'$a(t)=2t-4$')
    ax1.axhline(0, color='#888', lw=1)
    ax1.fill_between(t, v, 0, where=(v > 0), color=BLUE, alpha=0.10)
    for xt in (1, 3):
        ax1.axvline(xt, color=GRAY, lw=0.8, alpha=0.5)
    ax1.annotate('turn\naround', (1, 0), xytext=(0.4, 2.0), fontsize=9, color=GRAY)
    ax1.annotate('turn\naround', (3, 0), xytext=(3.05, -3.4), fontsize=9, color=GRAY)
    ax1.set_xlim(0, 4.6); ax1.set_ylim(-3.6, 4.2)
    ax1.set_title('The motion story: signs of $v$ and $a$ together', fontweight='bold')
    ax1.legend(fontsize=9, loc='upper right')

    ax2 = fig.add_subplot(212); g(ax2)
    ax2.set_xlim(0, 4.6); ax2.set_ylim(0, 1)
    ax2.set_yticks([])
    zones = [
        (0, 1, 'v>0, a<0\nforward, slowing', BLUE),
        (1, 2, 'v<0, a<0\nbackward, speeding', RED),
        (2, 3, 'v<0, a>0\nbackward, slowing', AMBER),
        (3, 4.6, 'v>0, a>0\nforward, speeding', GREEN),
    ]
    for x0, x1, label, col in zones:
        ax2.axvspan(x0, x1, color=col, alpha=0.25)
        ax2.text((x0 + x1)/2, 0.55, label, ha='center', va='center', fontsize=9,
                 color=col, fontweight='bold')
    ax2.plot([1, 1], [0, 1], color=GRAY, lw=1); ax2.plot([2, 2], [0, 1], color=GRAY, lw=1)
    ax2.plot([3, 3], [0, 1], color=GRAY, lw=1)
    ax2.set_xlabel('time $t$ [s]')
    ax2.set_title('Motion timeline', fontweight='bold', fontsize=11)
    fig.tight_layout()
    save(fig, '14D1', '14d2-motion-story.png')

def d3_linearization():
    """sqrt(x), tangent at x=4, zoom inset showing the tiny gap at x=4.1."""
    fig, ax = plt.subplots(figsize=(9, 5)); g(ax)
    x = np.linspace(0, 9, 900)
    ax.plot(x, np.sqrt(x), BLUE, lw=2.5, label=r'$f(x)=\sqrt{x}$')
    ax.plot(x, 2 + (x - 4)/4, RED, lw=2, ls='--', label=r'$L(x)=2+\frac{x-4}{4}$')
    ax.plot([4], [2], 'o', color=RED, ms=7, zorder=6)
    ax.plot([4.1], [np.sqrt(4.1)], 'o', color=BLUE, ms=7, zorder=6)
    ax.plot([4.1], [2.025], 'o', color=RED, ms=7, zorder=6)
    ax.annotate(r'$\sqrt{4.1}=2.024845\ldots$', (4.1, np.sqrt(4.1)), xytext=(4.6, 1.72),
                fontsize=10, color=BLUE, fontweight='bold')
    ax.annotate(r'$L(4.1)=2.025$', (4.1, 2.025), xytext=(4.6, 2.12),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 9); ax.set_ylim(0, 3.2)
    ax.set_title('Linearization: the tangent is the best local model', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')

    # zoom inset
    ins = ax.inset_axes([0.18, 0.15, 0.42, 0.38])
    xz = np.linspace(3.9, 4.3, 600)
    ins.plot(xz, np.sqrt(xz), BLUE, lw=2.5)
    ins.plot(xz, 2 + (xz - 4)/4, RED, lw=2, ls='--')
    ins.plot([4.1], [np.sqrt(4.1)], 'o', color=BLUE, ms=6)
    ins.plot([4.1], [2.025], 'o', color=RED, ms=6)
    ins.annotate('error $\\approx 0.00015$', (4.1, 2.025), xytext=(4.11, 2.035),
                 fontsize=8, color=RED)
    ins.set_xticks([]); ins.set_yticks([])
    ins.set_title('zoom', fontsize=8)
    for s in ins.spines.values():
        s.set_color('#aaa')
    fig.tight_layout()
    save(fig, '14D1', '14d3-linearization.png')

def d4_circle_ring():
    """Circle of radius r with a thin ring of width dr: ring area ~ 2 pi r dr."""
    fig, ax = plt.subplots(figsize=(7, 6.2)); g(ax)
    ax.add_patch(Circle((0, 0), 3, fill=True, fc=BLUE, alpha=0.18, ec=BLUE, lw=2.5))
    ax.add_patch(Wedge((0, 0), 3.45, 0, 360, width=0.45, fc=AMBER, alpha=0.45, ec=AMBER, lw=1.5))
    ax.plot([0, 3], [0, 0], color=BLUE, lw=2)
    ax.plot([0, 3.45], [0, 0], color=AMBER, lw=2, ls='--')
    ax.annotate('$r$', (1.5, 0.08), fontsize=12, color=BLUE, fontweight='bold')
    ax.annotate('$dr$', (3.2, 0.12), fontsize=12, color=AMBER, fontweight='bold')
    ax.annotate('ring area $\\approx 2\\pi r\\,dr$', (0.4, 2.5), fontsize=11, color=AMBER,
                fontweight='bold')
    ax.annotate(r'$A=\pi r^2 \Rightarrow \frac{dA}{dr}=2\pi r$', (0.35, 1.95), fontsize=11,
                color=BLUE, fontweight='bold')
    ax.set_xlim(-3.9, 3.9); ax.set_ylim(-3.6, 3.9)
    ax.set_aspect('equal')
    ax.set_title('$dA/dr$ = circumference: growth happens on the boundary', fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    save(fig, '14D1', '14d4-circle-ring.png')

def d5_sphere_shell():
    """3D sphere with a translucent shell of thickness dr — dV/dr = 4 pi r^2."""
    fig = plt.figure(figsize=(8, 6.8))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2*np.pi, 60); v = np.linspace(0, np.pi, 60)
    R = 3.0; dr = 0.5
    for rad, col, alpha in ((R, BLUE, 0.12), (R + dr, AMBER, 0.25)):
        xs = rad*np.outer(np.cos(u), np.sin(v))
        ys = rad*np.outer(np.sin(u), np.sin(v))
        zs = rad*np.outer(np.ones_like(u), np.cos(v))
        ax.plot_surface(xs, ys, zs, color=col, alpha=alpha, linewidth=0)
        ax.plot_wireframe(xs[::6, ::6], ys[::6, ::6], zs[::6, ::6], color=col, lw=0.4, alpha=0.8)
    ax.quiver(0, 0, 0, R, 0, 0, color=BLUE, lw=2.5, arrow_length_ratio=0.08)
    ax.text(1.2, 0.15, 0.6, '$r$', fontsize=13, color=BLUE, fontweight='bold')
    ax.text(3.1, 1.2, 0.8, '$dr$', fontsize=13, color=AMBER, fontweight='bold')
    ax.text(0, 0, R + dr + 0.6, 'shell volume $\\approx 4\\pi r^2\\,dr$', fontsize=11,
            color=AMBER, fontweight='bold', ha='center')
    ax.text(0, 0, -R - dr - 0.5, r'$V=\frac{4}{3}\pi r^3 \Rightarrow \frac{dV}{dr}=4\pi r^2$',
            fontsize=11, color=BLUE, fontweight='bold', ha='center')
    lim = R + dr + 1
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.set_title('$dV/dr$ = surface area: a thin shell wraps the sphere', fontweight='bold')
    fig.tight_layout()
    save(fig, '14D1', '14d5-sphere-shell.png')

def d6_marginal_cost():
    """Cost curve with tangent (= marginal cost) and MC vs AC crossing at the min of AC."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in (ax1, ax2): g(ax)

    q = np.linspace(0, 24, 500)
    C = q**2 + 4*q + 144
    ax1.plot(q, C, GREEN, lw=2.5, label=r'$C(q)=q^2+4q+144$')
    ax1.plot(q, 28*q - 144 + 144, PURPLE, lw=2, ls='--')  # tangent at q=12: C=336, slope 28
    ax1.plot([12], [336], 'o', color=PURPLE, ms=7, zorder=6)
    ax1.plot([12, 13], [336, 336], color=GRAY, lw=1, alpha=0.6)
    ax1.plot([13, 13], [336, 365], color=GRAY, lw=1, alpha=0.6)
    ax1.annotate('$C\\,(12)=336$\nnext unit: 365', (12, 336), xytext=(6, 470),
                 fontsize=9, color=PURPLE,
                 arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.0))
    ax1.set_xlabel('$q$ [units]'); ax1.set_ylabel(r'cost [\$]')
    ax1.set_title('Tangent slope = cost of the next unit', fontweight='bold')
    ax1.set_ylim(0, 750); ax1.legend(fontsize=9, loc='upper left')

    MC = 2*q + 4
    AC = q + 4 + 144/q
    ax2.plot(q, MC, RED, lw=2.5, label=r'$MC=C\'(q)=2q+4$')
    ax2.plot(q[1:], AC[1:], BLUE, lw=2.2, label=r'$AC=C(q)/q$')
    ax2.plot([12], [28], 'o', color=GRAY, ms=8, zorder=6)
    ax2.annotate('$MC=AC$ at the\nminimum of $AC$', (12, 28), xytext=(2.5, 55),
                 fontsize=9, color=GRAY, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.0))
    ax2.set_xlabel('$q$ [units]'); ax2.set_ylabel(r'cost per unit [\$/unit$]')
    ax2.set_title('Marginal meets average at the average\'s minimum', fontweight='bold')
    ax2.set_ylim(0, 80); ax2.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14D1', '14d6-marginal-cost.png')

def d7_elasticity():
    """Demand q=500-10p and revenue R=pq with elastic/inelastic regions; max revenue at E=-1."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    for ax in (ax1, ax2): g(ax)

    p = np.linspace(0, 50, 600)
    q = 500 - 10*p
    ax1.plot(p, q, BLUE, lw=2.5, label=r'demand $q=500-10p$')
    ax1.fill_between(p, q, 0, where=(p < 25), color=AMBER, alpha=0.18)
    ax1.fill_between(p, q, 0, where=(p > 25), color=RED, alpha=0.18)
    ax1.plot([25], [250], 'o', color=GRAY, ms=8, zorder=6)
    ax1.annotate('$|E|=1$\n(unit elastic)', (25, 250), xytext=(10, 380),
                 fontsize=9, color=GRAY, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.0))
    ax1.text(10, 100, 'elastic $|E|>1$', color=RED, fontsize=9, fontweight='bold')
    ax1.text(35, 300, 'inelastic $|E|<1$', color=AMBER, fontsize=9, fontweight='bold')
    ax1.set_xlabel(r'price $p$ [\$]'); ax1.set_ylabel('quantity $q$')
    ax1.set_title('Demand: elasticity changes along the curve', fontweight='bold')
    ax1.set_ylim(0, 520); ax1.legend(fontsize=9, loc='upper right')

    R = p * q
    ax2.plot(p, R, GREEN, lw=2.5, label=r'revenue $R=p\,q(p)$')
    ax2.plot([25], [6250], 'o', color=RED, ms=8, zorder=6)
    ax2.annotate('max revenue\nat $E=-1$', (25, 6250), xytext=(27, 5200),
                 fontsize=9, color=RED, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=RED, lw=1.0))
    ax2.set_xlabel(r'price $p$ [\$]'); ax2.set_ylabel(r'revenue [\$]')
    ax2.set_title('Revenue is maximized where $E=-1$', fontweight='bold')
    ax2.set_ylim(0, 7000); ax2.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14D1', '14d7-elasticity.png')

# ═══════════════════════════ 16C ═══════════════════════════

def c1_accumulation():
    """Water flow r(t)=30-2t: shaded area = 225 L total, with trapezoid slices."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    t = np.linspace(0, 15, 600)
    r = 30 - 2*t
    ax.plot(t, r, BLUE, lw=2.5, label=r'flow rate $r(t)=30-2t$ [L/min]')
    ax.fill_between(t, r, 0, color=BLUE, alpha=0.20)
    for i in range(3):
        ax.fill_between([5*i, 5*i + 5], [30 - 2*5*i, 30 - 2*(5*i + 5)], 0,
                        facecolor='none', edgecolor=RED, lw=1.4, alpha=0.8)
    ax.annotate('area = total volume\n$\\int_0^{15}(30-2t)\\,dt = 225$ L', (4, 25), xytext=(5.6, 22),
                fontsize=11, color=RED, fontweight='bold')
    ax.set_xlim(0, 15); ax.set_ylim(0, 34)
    ax.set_title('Accumulation: the area under a rate IS the total', fontweight='bold')
    ax.set_xlabel('time $t$ [min]'); ax.set_ylabel('rate [L/min]')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '16C1', '16c1-accumulation.png')

def c2_average_value():
    """T(t)=20+10sin(pi t/12) over 24 h with equal-area rectangle at height 20."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    t = np.linspace(0, 24, 900)
    T = 20 + 10*np.sin(np.pi*t/12)
    ax.plot(t, T, BLUE, lw=2.5, label=r'$T(t)=20+10\sin(\pi t/12)$ [$^\circ$C]')
    ax.axhline(20, color=RED, lw=2, ls='--', label=r'mean $=20^\circ$C')
    ax.fill_between(t, T, 20, where=(T >= 20), color=AMBER, alpha=0.25)
    ax.fill_between(t, T, 20, where=(T < 20), color=BLUE, alpha=0.25)
    ax.annotate('above the mean\n(balances the below)', (10, 28), xytext=(12.5, 28.5),
                fontsize=9, color=AMBER, fontweight='bold')
    ax.annotate('below the mean', (3, 13), xytext=(0.4, 6),
                fontsize=9, color=BLUE, fontweight='bold')
    ax.set_xlim(0, 24); ax.set_ylim(0, 34)
    ax.set_title('Average value: the rectangle with the same area', fontweight='bold')
    ax.set_xlabel('time of day [h]'); ax.set_ylabel('temperature [$^\\circ$C]')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '16C1', '16c2-average-value.png')

def c3_work_spring():
    """F=kx with shaded triangle: work = 1/2 k x^2."""
    fig, ax = plt.subplots(figsize=(8, 5)); g(ax)
    x = np.linspace(0, 0.5, 300)
    ax.plot(x, 20*x, BLUE, lw=2.5, label=r'$F(x)=20x$ [N]')
    ax.fill_between(x, 20*x, 0, color=BLUE, alpha=0.22)
    ax.plot([0.3], [6], 'o', color=RED, ms=7, zorder=6)
    ax.plot([0.3, 0.3], [0, 6], RED, lw=1.4, ls='--', alpha=0.7)
    ax.plot([0, 0.3], [6, 6], RED, lw=1.4, ls='--', alpha=0.7)
    ax.annotate('$W=\\int_0^{0.3}20x\\,dx = \\frac{1}{2}\\cdot 6\\cdot 0.3 = 0.9$ J', (0.31, 6.5),
                fontsize=10, color=RED, fontweight='bold')
    ax.annotate('force grows as you stretch —\nthe last cm costs the most', (0.06, 8.5),
                fontsize=9, color=GRAY)
    ax.set_xlim(0, 0.55); ax.set_ylim(0, 12)
    ax.set_title(r'Work = area under the force curve (triangle: $\frac{1}{2}kx^2$)', fontweight='bold')
    ax.set_xlabel('stretch $x$ [m]'); ax.set_ylabel('force [N]')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '16C1', '16c3-work-spring.png')

def c4_surplus():
    """Supply and demand with consumer and producer surplus shaded."""
    fig, ax = plt.subplots(figsize=(8.5, 5.4)); g(ax)
    q = np.linspace(0, 55, 500)
    D = 100 - 2*q
    S = 10 + q
    ax.plot(q, D, BLUE, lw=2.5, label=r'demand $D(q)=100-2q$')
    ax.plot(q, S, GREEN, lw=2.5, label=r'supply $S(q)=10+q$')
    ax.axhline(40, color=GRAY, lw=1.4, ls='--')
    ax.fill_between(q[q <= 30], D[q <= 30], 40, color=AMBER, alpha=0.30)
    ax.fill_between(q[q <= 30], 40, S[q <= 30], color=PURPLE, alpha=0.30)
    ax.plot([30], [40], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('equilibrium (30, 40)', (30, 40), xytext=(33, 30),
                fontsize=9, color=RED, fontweight='bold')
    ax.text(8, 72, 'consumer surplus\n$\\int_0^{30}(D-40)\\,dq=900$', fontsize=10,
            color=AMBER, fontweight='bold')
    ax.text(8, 20, 'producer surplus\n$\\int_0^{30}(40-S)\\,dq=450$', fontsize=10,
            color=PURPLE, fontweight='bold')
    ax.set_xlim(0, 55); ax.set_ylim(0, 105)
    ax.set_title('Surplus: willingness-to-pay above the price, measured as area', fontweight='bold')
    ax.set_xlabel('quantity $q$'); ax.set_ylabel(r'price [\$]')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '16C1', '16c4-surplus.png')

def c5_present_value():
    """Income stream R(t)=10000/yr discounted at 5%: PV = area under R e^{-rt}."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    t = np.linspace(0, 10, 700)
    R = 10000*np.ones_like(t)
    disc = 10000*np.exp(-0.05*t)
    ax.plot(t, R, BLUE, lw=2.2, label=r'$R(t)=10{,}000$ \$/yr')
    ax.plot(t, disc, RED, lw=2.5, label=r'$R(t)e^{-rt}$, $r=0.05$')
    ax.fill_between(t, disc, 0, color=RED, alpha=0.22)
    ax.annotate('PV = area\n$\\int_0^{10}10000e^{-0.05t}dt\\approx 78{,}694$ \\$', (3, 4000),
                xytext=(3.2, 5500), fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 10); ax.set_ylim(0, 11000)
    ax.set_title('Present value: discount each dollar by when it arrives, then integrate', fontweight='bold')
    ax.set_xlabel('time $t$ [yr]'); ax.set_ylabel(r'value rate [\$/yr]')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '16C1', '16c5-present-value.png')

def c6_density_3d():
    """3D probability density surface (2D gaussian): total volume 1, slice = probability."""
    fig = plt.figure(figsize=(9, 6.6))
    ax = fig.add_subplot(111, projection='3d')
    xg = np.linspace(-3, 3, 100)
    yg = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(xg, yg)
    Z = np.exp(-(X**2 + Y**2)/2) / (2*np.pi)
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9, linewidth=0, antialiased=True)
    mask = (X >= 0.5) & (X <= 1.5)
    Zm = np.where(mask, Z, np.nan)
    ax.plot_surface(X, Y, Zm, color=AMBER, alpha=0.85, linewidth=0)
    ax.plot([0.5, 0.5], [-3, -3], [0, 0], color=RED, lw=1.5)
    ax.plot([1.5, 1.5], [-3, -3], [0, 0], color=RED, lw=1.5)
    ax.text(0.85, 2.6, 0.16, '$P(0.5\\leq X\\leq 1.5)$\n= slice volume', color='#7a4a00',
            fontsize=10, fontweight='bold', ha='center')
    ax.text(0, 0, 0.24, 'total volume $= \\iint p = 1$', fontsize=10, color=BLUE,
            fontweight='bold', ha='center')
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(0, 0.25)
    ax.set_axis_off()
    ax.view_init(elev=32, azim=-58)
    ax.set_title('Probability = volume under the density surface', fontweight='bold')
    fig.colorbar(surf, ax=ax, shrink=0.55, pad=0.02, label='density $p(x,y)$')
    fig.tight_layout()
    save(fig, '16C1', '16c6-density-3d.png')

def c7_expectation():
    """Triangle density p(x)=x/50 on [0,10]; expectation = balance point at 20/3."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    x = np.linspace(0, 10, 600)
    p = x/50
    ax.plot(x, p, BLUE, lw=2.5, label=r'$p(x)=\frac{x}{50}$ on $[0,10]$')
    ax.fill_between(x, p, 0, color=BLUE, alpha=0.18)
    ax.axvline(20/3, color=RED, lw=2, ls='--', label=r'$E[X]=\frac{20}{3}\approx 6.67$')
    ax.plot([20/3], [0], '^', color=RED, ms=10, zorder=6)
    ax.annotate('balance point:\nthe density balances here', (20/3, 0), xytext=(7.2, 0.14),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))
    ax.text(3.3, 0.17, 'half the area is left of the median ($\\sqrt{50}\\approx7.07$)',
            fontsize=9, color=GRAY)
    ax.set_xlim(0, 10); ax.set_ylim(0, 0.24)
    ax.set_title('Expectation = center of mass of the density', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('probability density')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '16C1', '16c7-expectation.png')

if __name__ == '__main__':
    d1_units(); d2_motion_story(); d3_linearization(); d4_circle_ring()
    d5_sphere_shell(); d6_marginal_cost(); d7_elasticity()
    c1_accumulation(); c2_average_value(); c3_work_spring(); c4_surplus()
    c5_present_value(); c6_density_3d(); c7_expectation()
    print('Done: 14D1 + 16C1 graphs written to graphs/0821/')
