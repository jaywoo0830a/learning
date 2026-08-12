#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 10A and 10B (same pattern as 13X/14X).

Outputs into graphs/0808/10A and graphs/0808/10B.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0808')
for _sub in ('10A', '10B'):
    os.makedirs(os.path.join(BASE, _sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'
PURPLE = '#7b1fa2'

def save(fig, sub, name):
    fig.savefig(os.path.join(BASE, sub, name), bbox_inches='tight')
    plt.close(fig)

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# ───────────────────────── 10A ─────────────────────────

def a_doubling_numberline():
    """Multiplicative number line: 1,2,4,8,16 at equal steps, each arrow ×2."""
    fig, ax = plt.subplots(figsize=(9.5, 3.6)); g(ax)
    ax.set_xlim(-0.4, 5.0); ax.set_ylim(0, 2.6)
    # the axis
    ax.annotate('', (4.7, 1.3), xytext=(-0.2, 1.3),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.6))
    vals = [1, 2, 4, 8, 16]
    for p, v in enumerate(vals):
        ax.plot([p], [1.3], 'o', color=BLUE, ms=8, zorder=6)
        ax.text(p, 1.3 - 0.28, '$%d$' % v, ha='center', va='top', fontsize=13,
                color=BLUE, fontweight='bold')
    # ×2 arrows between consecutive positions
    for p in range(4):
        ax.annotate('', (p + 1, 1.55), xytext=(p, 1.55),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.8))
        ax.text(p + 0.5, 1.75, '$\\times 2$', ha='center', fontsize=11,
                color=RED, fontweight='bold')
    # ÷2 note going left
    ax.text(0.6, 0.55, '$\\div 2$ going left', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(2.5, 0.15, 'equal steps in $x$ = equal multiplicative jumps (×2)',
            ha='center', fontsize=11, color='#222', fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('The number line is multiplicative — each step multiplies by 2',
                 fontweight='bold')
    fig.tight_layout()
    save(fig, '10A', '10a-doubling-numberline.png')

def a_dimension_scaling():
    """Squares and cubes: doubling the side quadruples area, octuples volume."""
    fig, ax = plt.subplots(figsize=(9.5, 4.6)); g(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')

    def cube(ax, x0, y0, s, color):
        # front square
        ax.add_patch(Rectangle((x0, y0), s, s, fill=False, edgecolor=color, lw=2.2))
        # back square (offset)
        d = 0.28 * s
        ax.add_patch(Rectangle((x0 + d, y0 + d), s, s, fill=False, edgecolor=color, lw=1.8, alpha=0.6))
        # connecting lines
        for px, py in [(x0, y0), (x0 + s, y0), (x0, y0 + s), (x0 + s, y0 + s)]:
            ax.plot([px, px + d], [py, py + d], color=color, lw=1.8, alpha=0.6)

    # squares (left)
    ax.add_patch(Rectangle((0.7, 3.0), 1.0, 1.0, facecolor=BLUE, alpha=0.25, edgecolor=BLUE, lw=2.2))
    ax.text(1.2, 2.7, 'side $s$: area $s^2$', ha='center', fontsize=11, color=BLUE, fontweight='bold')
    ax.add_patch(Rectangle((2.2, 2.4), 2.0, 2.0, facecolor=BLUE, alpha=0.18, edgecolor=BLUE, lw=2.2))
    ax.text(3.2, 2.2, 'side $2s$: area $4s^2$', ha='center', fontsize=11, color=BLUE, fontweight='bold')
    ax.annotate('area ×4', (1.2, 3.5), xytext=(1.2, 4.9), fontsize=11, color=RED,
                fontweight='bold', arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))
    ax.annotate('', (3.2, 4.7), xytext=(3.2, 4.4),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))

    # cubes (right)
    cube(ax, 5.2, 3.0, 1.0, GREEN)
    ax.text(5.7, 2.7, 'side $s$: volume $s^3$', ha='center', fontsize=11, color=GREEN, fontweight='bold')
    cube(ax, 7.0, 2.2, 2.0, GREEN)
    ax.text(8.0, 2.0, 'side $2s$: volume $8s^3$', ha='center', fontsize=11, color=GREEN, fontweight='bold')
    ax.annotate('volume ×8', (5.7, 4.0), xytext=(5.7, 5.3), fontsize=11, color=RED,
                fontweight='bold', arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))
    ax.annotate('', (8.0, 4.4), xytext=(8.0, 4.1),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))

    ax.set_title('The exponent is the dimension: 2D scales as side$^2$, 3D as side$^3$',
                 fontweight='bold')
    fig.tight_layout()
    save(fig, '10A', '10a-dimension-scaling.png')

def a_exp_slope_equals_height():
    """y=e^x with tangents: slope at each point equals the height."""
    fig, ax = plt.subplots(figsize=(9, 5)); g(ax)
    x = np.linspace(-2.2, 2.4, 800)
    ax.plot(x, np.exp(x), BLUE, lw=2.6, label=r'$y=e^x$')
    for a in (-1, 0, 1, 2):
        ea = np.exp(a)
        # tangent: y = e^a*(x-a) + e^a = e^a*x + e^a(1-a)
        xs = np.linspace(a - 0.7, a + 0.7, 2)
        ax.plot(xs, ea * xs + ea * (1 - a), RED, lw=1.6, ls='--')
        ax.plot([a], [ea], 'o', color=RED, ms=5, zorder=6)
    ax.annotate('at $x=1$: slope $= e^1$\n$=$ height $e^1$', (1, np.e),
                xytext=(0.7, 4.2), fontsize=10, color=RED, fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-2.2, 2.4); ax.set_ylim(-0.3, 9)
    ax.set_title('The slope at every point equals the height — $e^x$ is its own derivative',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '10A', '10a-exp-slope-equals-height.png')

def a_log_as_area():
    """ln a = area under y=1/x from 1 to a (a=3)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0.3, 4, 800)
    ax.plot(x, 1/x, BLUE, lw=2.6, label=r'$y=\frac{1}{x}$')
    xs = np.linspace(1, 3, 300)
    ax.fill_between(xs, 1/xs, 0, color=GREEN, alpha=0.35)
    ax.axvline(1, color='#888', lw=1.0, ls='--'); ax.axvline(3, color='#888', lw=1.0, ls='--')
    ax.text(2, 0.55, 'area $= \\ln 3 \\approx 1.099$', ha='center', fontsize=12,
            color=GREEN, fontweight='bold')
    ax.annotate('$x=1$', (1, 0), xytext=(1.0, -0.38), fontsize=10, ha='center', color='#555')
    ax.annotate('$x=3$', (3, 0), xytext=(3.0, -0.38), fontsize=10, ha='center', color='#555')
    ax.set_xlim(0.3, 4); ax.set_ylim(-0.5, 2.6)
    ax.set_title(r'$\ln a$ = the area under $y=1/x$ from $x=1$ to $x=a$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper right')
    fig.tight_layout()
    save(fig, '10A', '10a-log-as-area.png')

def a_exp_ln_inverse():
    """e^x and ln x are mirror images across y=x."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    x1 = np.linspace(-2.4, 2.4, 800)
    ax.plot(x1, np.exp(x1), BLUE, lw=2.6, label=r'$y=e^x$')
    x2 = np.linspace(0.08, 2.4, 800)
    ax.plot(x2, np.log(x2), RED, lw=2.6, label=r'$y=\ln x$')
    xd = np.linspace(-2.4, 2.4, 100)
    ax.plot(xd, xd, color='#888', lw=1.4, ls='--', label='$y=x$')
    # mirror pairs
    for (px, py) in [(0, 1), (1, np.e)]:
        ax.plot([px], [py], 'o', color=BLUE, ms=7, zorder=6)
        ax.plot([py], [px], 'o', color=RED, ms=7, zorder=6)
        ax.plot([px, py], [py, px], color='#aaa', lw=1.0, ls=':')
    ax.annotate('$(0,1)\\leftrightarrow(1,0)$', (-1.9, 0.45), fontsize=10, color='#222', fontweight='bold')
    ax.annotate('$(1,e)\\leftrightarrow(e,1)$', (1.05, -1.15), fontsize=10, color='#222', fontweight='bold')
    ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.4, 2.4)
    ax.set_aspect('equal')
    ax.set_title('Exponential and natural log are mirror images across $y=x$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '10A', '10a-exp-ln-inverse.png')

def a_growth_race():
    """Growth race: x, x^2, 2^x, ln x — the exponential overtakes the quadratic."""
    fig, ax = plt.subplots(figsize=(9, 5.2)); g(ax)
    x = np.linspace(0.5, 4.6, 800)
    ax.plot(x, x, '#888', lw=2.0, label=r'$x$')
    ax.plot(x, x**2, GREEN, lw=2.4, label=r'$x^2$')
    ax.plot(x, 2**x, RED, lw=2.6, label=r'$2^x$')
    ax.plot(x, np.log(x), PURPLE, lw=2.2, ls='-.', label=r'$\ln x$')
    # crossing of x^2 and 2^x at x=4
    ax.plot([4], [16], 'o', color='#333', ms=8, zorder=7)
    ax.annotate('$2^x$ passes $x^2$ at $x=4$\n($16=16$) and never looks back',
                (4, 16), xytext=(2.4, 13.5), fontsize=10, color='#333', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(0.5, 4.6); ax.set_ylim(-0.5, 24)
    ax.set_title('Growth race — the exponential overtakes every polynomial; the log crawls',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '10A', '10a-growth-race.png')

# ───────────────────────── 10B ─────────────────────────

def b_log_bases():
    """Compare logarithms with different bases."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    x = np.linspace(0.5, 8, 800)
    ax.plot(x, np.log2(x), BLUE, lw=2.5, label=r'$\log_2 x$')
    ax.plot(x, np.log(x)/np.log(3), GREEN, lw=2.4, label=r'$\log_3 x$')
    ax.plot(x, np.log(x), RED, lw=2.4, label=r'$\ln x = \log_e x$')
    ax.plot(x, np.log10(x), PURPLE, lw=2.2, ls='--', label=r'$\log_{10} x$')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(1, color='#888', lw=0.8, ls=':', alpha=0.6)
    ax.annotate('larger base → smaller values\nfor $x>1$', (6.2, 0.9), fontsize=10,
                color='#222', fontweight='bold')
    ax.set_xlim(0.5, 8); ax.set_ylim(-2, 3.4)
    ax.set_title('Log bases: the larger the base, the slower the growth (for $x>1$)',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '10B', '10b-log-bases.png')

def b_linear_scale():
    """Linear scale: equal steps = equal differences."""
    fig, ax = plt.subplots(figsize=(9.5, 3.2)); g(ax)
    ax.set_xlim(0, 5); ax.set_ylim(0, 2.2)
    ax.annotate('', (4.7, 1.2), xytext=(-0.1, 1.2),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.6))
    for v in range(5):
        ax.plot([v], [1.2], 'o', color=BLUE, ms=8, zorder=6)
        ax.text(v, 1.2 - 0.28, '$%d$' % v, ha='center', va='top', fontsize=13,
                color=BLUE, fontweight='bold')
        if v < 4:
            ax.annotate('', (v + 1, 1.5), xytext=(v, 1.5),
                        arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))
            ax.text(v + 0.5, 1.72, '$+1$', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(2.5, 0.1, 'equal steps = equal differences (add 1 each time)',
            ha='center', fontsize=11, color='#222', fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Linear scale — 1 and 2 are as far apart as 1001 and 1002',
                 fontweight='bold')
    fig.tight_layout()
    save(fig, '10B', '10b-linear-scale.png')

def b_log_scale():
    """Log scale: equal steps = equal multiplicative factors (×10)."""
    fig, ax = plt.subplots(figsize=(9.5, 3.2)); g(ax)
    ax.set_xlim(-0.4, 5.0); ax.set_ylim(0, 2.2)
    ax.annotate('', (4.7, 1.2), xytext=(-0.1, 1.2),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.6))
    vals = [1, 10, 100, 1000, 10000]
    for p, v in enumerate(vals):
        ax.plot([p], [1.2], 'o', color=GREEN, ms=8, zorder=6)
        ax.text(p, 1.2 - 0.3, '$%d$' % v, ha='center', va='top', fontsize=11.5,
                color=GREEN, fontweight='bold')
        if p < 4:
            ax.annotate('', (p + 1, 1.5), xytext=(p, 1.5),
                        arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))
            ax.text(p + 0.5, 1.72, '$\\times 10$', ha='center', fontsize=10.5,
                    color=RED, fontweight='bold')
    ax.text(2.5, 0.1, 'equal steps = equal multiplicative factors (×10)',
            ha='center', fontsize=11, color='#222', fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Log scale — 1 and 10 are as far apart as 1000 and 10000',
                 fontweight='bold')
    fig.tight_layout()
    save(fig, '10B', '10b-log-scale.png')

if __name__ == '__main__':
    for fn in (a_doubling_numberline, a_dimension_scaling, a_exp_slope_equals_height,
               a_log_as_area, a_exp_ln_inverse, a_growth_race,
               b_log_bases, b_linear_scale, b_log_scale):
        fn()
        print('done:', fn.__name__)
    print('All 10A/10B session graphs written under', BASE)
