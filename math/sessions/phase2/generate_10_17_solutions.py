#!/usr/bin/env python3
"""Generate solution graphs for 10A/10B/17A solution files (same pattern as 14X solutions).

Outputs into solutions/graphs/10A, 10B, 17A.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'solutions', 'graphs')
for sub in ('10A', '10B', '17A'):
    os.makedirs(os.path.join(BASE, sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'
PURPLE = '#7b1fa2'

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

def save(fig, sub, name):
    fig.savefig(os.path.join(BASE, sub, name), bbox_inches='tight')
    plt.close(fig)

# ═══════════════════════════ 10A ═══════════════════════════

def a_p6():
    """P6: 3^{x+2}-3^x=72 → 8·3^x=72 → x=2."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    x = np.linspace(0, 2.6, 800)
    ax.plot(x, 8*3**x, RED, lw=2.6, label=r'$y=8\cdot 3^x$')
    ax.axhline(72, color=BLUE, lw=2.0, ls='--', label=r'$y=72$')
    ax.plot([2], [72], 'o', color='#333', ms=8, zorder=7)
    ax.annotate('$(2,72)$: $3^{x+2}-3^x=3^x(9-1)=8\\cdot 3^x$', (2, 72),
                xytext=(0.35, 76), fontsize=10, color='#333', fontweight='bold')
    ax.set_xlim(0, 2.6); ax.set_ylim(0, 90)
    ax.set_title('Practice 6: factor out $3^x$ — $8\\cdot 3^x=72 \\to x=2$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '10A', 'p6-exp-factoring.png')

def a_p9():
    """P9: log_{1/2}(3x+1) ≥ -2 → -1/3 < x ≤ 1."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    x = np.linspace(-1/3 + 0.01, 1.6, 800)
    y = np.log(3*x + 1)/np.log(0.5)
    ax.plot(x, y, BLUE, lw=2.6, label=r'$y=\log_{1/2}(3x+1)$')
    ax.axhline(-2, color=RED, lw=2.0, ls='--', label='$y=-2$')
    xs = np.linspace(-1/3 + 0.01, 1, 200)
    ax.fill_between(xs, -6, np.log(3*xs + 1)/np.log(0.5), color=GREEN, alpha=0.25)
    ax.plot([1], [-2], 'o', color=RED, ms=8, zorder=7, mfc='white', mew=2)
    ax.plot([-1/3], [-6], 'o', color=BLUE, ms=8, zorder=7, mfc='white', mew=2)
    ax.annotate('solution: $-\\frac{1}{3} < x \\leq 1$\n(base $<1$ flips the sign)', (0.4, -3.4),
                fontsize=11, color=GREEN, fontweight='bold')
    ax.set_xlim(-1/3 + 0.01, 1.6); ax.set_ylim(-7, 1.5)
    ax.axvline(1, color='#888', lw=1.0, ls=':'); ax.axvline(-1/3, color='#888', lw=1.0, ls=':')
    ax.set_title('Practice 9: $\\log_{1/2}(3x+1) \\geq -2$ — argument $>0$ and base $<1$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '10A', 'p9-log-inequality.png')

def a_p10():
    """P10: 25^x+5^{x+1}-6=0 → t=5^x, t²+5t-6=0 → t=1 → x=0."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    t = np.linspace(-7, 2, 800)
    ax.plot(t, t**2 + 5*t - 6, BLUE, lw=2.6, label=r'$y=t^2+5t-6$')
    ax.axhline(0, color='#888', lw=1.2, ls='--')
    ax.plot([-6, 1], [0, 0], 'o', color=RED, ms=8, zorder=7)
    ax.annotate('$t=-6$ discarded\n($t=5^x>0$)', (-6, 0), xytext=(-6.9, 14),
                fontsize=10, color=RED, fontweight='bold')
    ax.annotate('$t=1 \\to 5^x=1 \\to x=0$', (1, 0), xytext=(0.5, 14),
                fontsize=10, color=GREEN, fontweight='bold')
    ax.fill_betweenx(np.linspace(0, 1e-3, 2), 0, 1, color='none')
    ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-7, 2); ax.set_ylim(-14, 20)
    ax.set_title('Practice 10: $t=5^x \\to t^2+5t-6=0 \\to t=1 \\to x=0$',
                 fontweight='bold')
    ax.set_xlabel('$t$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='lower right')
    fig.tight_layout()
    save(fig, '10A', 'p10-quadratic-sub.png')

# ═══════════════════════════ 10B ═══════════════════════════

def b_p1():
    """P1: 500(0.92)^t < 100 → t > 19.3 years."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    t = np.linspace(0, 30, 800)
    ax.plot(t, 500*0.92**t, BLUE, lw=2.6, label=r'$N(t)=500(0.92)^t$')
    ax.axhline(100, color=RED, lw=2.0, ls='--', label='$N=100$')
    ax.plot([19.3], [100], 'o', color='#333', ms=8, zorder=7)
    ax.annotate('$t \\approx 19.3$ years\n$500(0.92)^t<100 \\to t>\\frac{\\ln 0.2}{\\ln 0.92}$',
                (19.3, 100), xytext=(8, 190), fontsize=10, color='#333', fontweight='bold')
    ax.set_xlim(0, 30); ax.set_ylim(0, 520)
    ax.set_title('Practice 1: exponential decay — falls below 100 g after ~19.3 years',
                 fontweight='bold')
    ax.set_xlabel('$t$ (years)'); ax.set_ylabel('$N$ (g)')
    ax.legend(fontsize=10, loc='upper right')
    fig.tight_layout()
    save(fig, '10B', 'p1-decay.png')

def b_p2():
    """P2: x·3^x = 9 → x = W(9 ln3)/ln3 ≈ 1.58."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    x = np.linspace(0.2, 2.4, 800)
    ax.plot(x, x*3**x, BLUE, lw=2.6, label=r'$y=x\cdot 3^x$')
    ax.axhline(9, color=RED, lw=2.0, ls='--', label='$y=9$')
    ax.plot([1.579], [9], 'o', color='#333', ms=8, zorder=7)
    ax.annotate('$x \\approx 1.58$\n$x=\\frac{W(9\\ln 3)}{\\ln 3}$', (1.579, 9),
                xytext=(0.6, 12.5), fontsize=10, color='#333', fontweight='bold')
    ax.set_xlim(0.2, 2.4); ax.set_ylim(0, 16)
    ax.set_title('Practice 2: $x\\cdot 3^x=9$ — rearrange to $u e^u = 9\\ln 3$, apply $W$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '10B', 'p2-lambert.png')

# ═══════════════════════════ 17A ═══════════════════════════

def c_p1():
    """P1: cardioid r=1+cosθ, area = 3π/2."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 1000)
    r = 1 + np.cos(th)
    ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=2.6)
    ax.fill(r*np.cos(th), r*np.sin(th), color=GREEN, alpha=0.3)
    ax.text(0.0, 0.0, '$A=\\frac{1}{2}\\int_0^{2\\pi}(1+\\cos\\theta)^2\\,d\\theta$\n$=\\frac{3\\pi}{2}$',
            ha='center', va='center', fontsize=12, color='#222', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.3, 2.3)
    ax.set_aspect('equal')
    ax.set_title(r'Practice 1: cardioid $r=1+\cos\theta$ — area $=3\pi/2$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '17A', 'p1-cardioid.png')

def c_p4():
    """P4: region between y=x^2 and y=√x about y=-1, V = 29π/30."""
    fig, ax = plt.subplots(figsize=(8, 6)); g(ax)
    x = np.linspace(0, 1.1, 400)
    ax.plot(x, np.sqrt(x), BLUE, lw=2.5, label=r'$y=\sqrt{x}$')
    ax.plot(x, x**2, RED, lw=2.5, label=r'$y=x^2$')
    xs = np.linspace(0, 1, 200)
    ax.fill_between(xs, xs**2, np.sqrt(xs), color=GREEN, alpha=0.3)
    ax.axhline(-1, color='#333', lw=2.0, ls='--', label='axis $y=-1$')
    xr = 0.55
    ax.plot([xr, xr], [-1, np.sqrt(xr)], color=BLUE, lw=1.8)
    ax.plot([xr, xr], [-1, xr**2], color=RED, lw=1.8)
    ax.annotate('$R_{\\text{outer}}=\\sqrt{x}+1$', (xr, np.sqrt(xr)), xytext=(0.62, 0.75),
                fontsize=10, color=BLUE, fontweight='bold')
    ax.annotate('$R_{\\text{inner}}=x^2+1$', (xr, xr**2), xytext=(0.62, -0.35),
                fontsize=10, color=RED, fontweight='bold')
    ax.text(0.5, 0.45, 'region', fontsize=11, color=GREEN, fontweight='bold')
    ax.set_xlim(-0.05, 1.2); ax.set_ylim(-1.35, 1.25)
    ax.set_title('Practice 4: washer about $y=-1$ — $V=\\frac{29\\pi}{30}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '17A', 'p4-washer-shifted.png')

def c_p5():
    """P5: Archimedean spiral r=θ, 0→2π, with x-axis: A = 4π³/3."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 1200)
    r = th
    ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=2.4)
    # shade the region between spiral and x-axis (upper and lower)
    ths = np.linspace(0, 2*np.pi, 300)
    ax.fill(np.append(ths*np.cos(ths), 0), np.append(ths*np.sin(ths), 0),
            color=GREEN, alpha=0.28)
    ax.annotate('$A=\\frac{1}{2}\\int_0^{2\\pi}\\theta^2\\,d\\theta$\n$=\\frac{4\\pi^3}{3}$',
                (2.0, 2.0), xytext=(0.6, 3.6), fontsize=11, color=GREEN,
                fontweight='bold', arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.4))
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-6.6, 6.6); ax.set_ylim(-6.6, 6.6)
    ax.set_aspect('equal')
    ax.set_title(r'Practice 5: Archimedean spiral $r=\theta$ — area $=4\pi^3/3$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '17A', 'p5-spiral.png')

def c_p6():
    """P6: unit square under M=[[3,1],[1,2]] → parallelogram, det=5."""
    fig, ax = plt.subplots(figsize=(8.5, 6)); g(ax)
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    M = np.array([[3, 1], [1, 2]])
    para = (M @ sq.T).T
    ax.plot(sq[:, 0], sq[:, 1], BLUE, lw=2.4, label='unit square (area 1)')
    ax.fill(sq[:, 0], sq[:, 1], color=BLUE, alpha=0.15)
    ax.plot(para[:, 0], para[:, 1], RED, lw=2.4, label='image parallelogram (area 5)')
    ax.fill(para[:, 0], para[:, 1], color=RED, alpha=0.15)
    for (x1, y1), (x2, y2) in [((0.5, 0.5), (2, 1.5)), ((1, 0), (3, 1))]:
        ax.annotate('', (x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=1.6))
    ax.text(2.0, 1.4, '$\\det M = 3\\cdot2-1\\cdot1=5$', fontsize=11,
            color='#333', fontweight='bold')
    ax.text(2.2, 5.6, 'area $= |\\det M| \\times 1 = 5$', fontsize=12, color=RED,
            fontweight='bold')
    ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.5, 4.2)
    ax.set_aspect('equal')
    ax.set_title('Practice 6: $M = [[3,1],[1,2]]$, det $= 5$ — area of the image $= 5$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '17A', 'p6-determinant.png')

if __name__ == '__main__':
    for fn in (a_p6, a_p9, a_p10, b_p1, b_p2, c_p1, c_p4, c_p5, c_p6):
        fn()
        print('done:', fn.__name__)
    print('All 10A/10B/17A solution graphs written under', BASE)
