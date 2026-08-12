#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 07A and 07B (same pattern as 13X/14X).

Outputs into graphs/0812/07A and graphs/0812/07B.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0812')
for _sub in ('07A', '07B'):
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

# ───────────────────────── 07A ─────────────────────────

def a_cubic_roots():
    """x^3-6x^2+11x-6 = (x-1)(x-2)(x-3) with roots 1,2,3 on the x-axis."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(-0.6, 4.4, 800)
    f = x**3 - 6*x**2 + 11*x - 6
    ax.plot(x, f, BLUE, lw=2.6, label=r'$f(x)=x^3-6x^2+11x-6$')
    ax.axhline(0, color='#888', lw=1.0)
    for r in (1, 2, 3):
        ax.plot([r], [0], 'o', color=RED, ms=9, zorder=6)
        ax.annotate('root $%d$' % r, (r, 0), xytext=(r - 0.35, 0.5), fontsize=10,
                    color=RED, fontweight='bold')
    ax.annotate('$f(x)=(x-1)(x-2)(x-3)$\nVieta: sum $=1+2+3=6$, product $=6$',
                (0.4, 1.6), xytext=(-0.55, 4.0), fontsize=11, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.3))
    ax.set_xlim(-0.6, 4.4); ax.set_ylim(-2.5, 4.6)
    ax.set_title('Roots of the cubic are the $x$-intercepts — Vieta links them to coefficients',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower left')
    fig.tight_layout()
    save(fig, '07A', '07a-cubic-roots.png')

def a_diff_squares():
    """Area model of a^2 - b^2 = (a-b)(a+b): clean two-panel layout."""
    fig, ax = plt.subplots(figsize=(10, 5.4)); g(ax)
    ax.set_xlim(-1.4, 11.2); ax.set_ylim(-1.8, 9.4)
    ax.axis('off')
    a, b = 5, 3
    # ── Left: a×a square with the b×b corner cut out (L-shape) ──
    ax.add_patch(Rectangle((0, 0), a, a, facecolor='#e8f0fe', edgecolor=BLUE, lw=2.6))
    ax.add_patch(Rectangle((a-b, a-b), b, b, facecolor='white', edgecolor=RED, lw=2.2,
                           hatch='//'))
    ax.add_patch(Rectangle((0, 0), a, a-b, facecolor=BLUE, alpha=0.28, edgecolor='none'))
    ax.add_patch(Rectangle((0, a-b), a-b, b, facecolor=GREEN, alpha=0.30, edgecolor='none'))
    ax.text(2.5, -0.55, '$a$', ha='center', fontsize=13, color=BLUE, fontweight='bold')
    ax.text(-0.55, 2.5, '$a$', va='center', fontsize=13, color=BLUE, fontweight='bold')
    ax.text(a-b + b/2, a + 0.45, '$b$', ha='center', fontsize=13, color=RED, fontweight='bold')
    ax.text(a + 0.45, a-b + b/2, '$b$', va='center', fontsize=13, color=RED, fontweight='bold')
    ax.text(1.05, 1.05, '$a^2-b^2$', fontsize=14, color='#222', fontweight='bold')
    # "=" between panels
    ax.text(6.0, 2.5, '$=$', fontsize=22, ha='center', va='center', fontweight='bold',
            color='#333')
    # ── Right: the rearranged (a-b)×(a+b) rectangle ──
    x0 = 7.4
    ax.add_patch(Rectangle((x0, 0), a-b, a, facecolor=BLUE, alpha=0.28, edgecolor=BLUE, lw=2.4))
    ax.add_patch(Rectangle((x0, a), a-b, b, facecolor=GREEN, alpha=0.30, edgecolor=GREEN, lw=2.4))
    ax.text(x0 + (a-b)/2, -0.55, '$a-b$', ha='center', fontsize=13, color='#222', fontweight='bold')
    ax.text(x0 - 0.5, a/2, '$a$', va='center', fontsize=13, color=BLUE, fontweight='bold')
    ax.text(x0 - 0.5, a + b/2, '$b$', va='center', fontsize=13, color=GREEN, fontweight='bold')
    ax.text(x0 + (a-b)/2, 8.9, '$(a-b)(a+b)$', ha='center', fontsize=14, color='#222',
            fontweight='bold')
    # bottom caption
    ax.text(5.1, -1.3, 'Cut a $b\\times b$ corner from an $a\\times a$ square, then rearrange the L-shape:',
            ha='center', fontsize=11, color='#222')
    ax.text(5.1, -1.72, '$a^2-b^2=(a-b)(a+b)$', ha='center', fontsize=12, color='#222',
            fontweight='bold')
    ax.set_title('Difference of squares as area', fontweight='bold', fontsize=12.5)
    fig.tight_layout()
    save(fig, '07A', '07a-diff-squares.png')

def a_factor_graph():
    """2x^3-3x^2-3x+2 = (x-2)(2x-1)(x+1): roots 2, 1/2, -1 ↔ x-intercepts."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(-1.8, 2.8, 800)
    f = 2*x**3 - 3*x**2 - 3*x + 2
    ax.plot(x, f, BLUE, lw=2.6, label=r'$f(x)=2x^3-3x^2-3x+2$')
    ax.axhline(0, color='#888', lw=1.0)
    for r in (-1, 0.5, 2):
        ax.plot([r], [0], 'o', color=RED, ms=9, zorder=6)
        ax.annotate('root $%s$' % ('-1' if r == -1 else ('1/2' if r == 0.5 else '2')),
                    (r, 0), xytext=(r - 0.3, 1.1), fontsize=10, color=RED, fontweight='bold')
    ax.annotate('$=(x-2)(2x-1)(x+1)$\nrational root candidates: $\\pm1,\\pm2,\\pm\\frac{1}{2}$',
                (1.6, 1.6), xytext=(0.5, 2.3), fontsize=10.5, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.3))
    ax.set_xlim(-1.8, 2.8); ax.set_ylim(-5, 4.2)
    ax.set_title('Rational Root Theorem + synthetic division: roots $\\to$ $x$-intercepts',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '07A', '07a-factor-graph.png')

# ───────────────────────── 07B ─────────────────────────

def b_system_intersection():
    """x+y=5 (line) and xy=6 (hyperbola), intersection (2,3),(3,2) — Ex 7 symmetric."""
    fig, ax = plt.subplots(figsize=(7.6, 6)); g(ax)
    x = np.linspace(-1, 7, 800)
    ax.plot(x, 5 - x, BLUE, lw=2.6, label=r'$x+y=5$')
    xh = np.linspace(0.35, 7, 800)
    ax.plot(xh, 6/xh, GREEN, lw=2.6, label=r'$xy=6$')
    for (px, py) in [(2, 3), (3, 2)]:
        ax.plot([px], [py], 'o', color=RED, ms=9, zorder=7)
    ax.annotate('$(2,3)$ and $(3,2)$\n$\\to$ roots of $t^2-5t+6=0$', (2, 3),
                xytext=(2.5, 3.6), fontsize=11, color=RED, fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-1, 7); ax.set_ylim(-1.5, 8)
    ax.set_title('Symmetric system: sum $5$, product $6$ — the solutions swap $x,y$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '07B', '07b-system-intersection.png')

def b_line_circle():
    """2x+y=7 and x^2+y^2=25 intersect at (4,-1) and (6/5,23/5) — Ex 4 substitution."""
    fig, ax = plt.subplots(figsize=(7.6, 6.6)); g(ax)
    th = np.linspace(0, 2*np.pi, 800)
    ax.plot(5*np.cos(th), 5*np.sin(th), BLUE, lw=2.4, label=r'$x^2+y^2=25$')
    x = np.linspace(-4.5, 8, 400)
    ax.plot(x, 7 - 2*x, GREEN, lw=2.6, label=r'$2x+y=7$')
    for (px, py) in [(4, -1), (6/5, 23/5)]:
        ax.plot([px], [py], 'o', color=RED, ms=9, zorder=7)
    ax.annotate('$(4,-1)$', (4, -1), xytext=(4.2, -1.6), fontsize=11, color=RED, fontweight='bold')
    ax.annotate('$(\\frac{6}{5},\\frac{23}{5})$', (6/5, 23/5), xytext=(0.2, 5.4),
                fontsize=11, color=RED, fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-6.2, 7.5); ax.set_ylim(-6.2, 7.2)
    ax.set_aspect('equal')
    ax.set_title('Substitution: $y=7-2x$ into the circle — a line meets a circle in two points',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '07B', '07b-line-circle.png')

def b_elimination():
    """3x+2y=8 and 2x-y=3 intersect at (2,1) — Ex 5 elimination."""
    fig, ax = plt.subplots(figsize=(7.6, 6)); g(ax)
    x = np.linspace(-1, 4, 400)
    ax.plot(x, (8 - 3*x)/2, BLUE, lw=2.6, label=r'$3x+2y=8$')
    ax.plot(x, 2*x - 3, GREEN, lw=2.6, label=r'$2x-y=3$')
    ax.plot([2], [1], 'o', color=RED, ms=10, zorder=7)
    ax.annotate('$(2,1)$\n(add $4x-2y=6$ to cancel $y$)', (2, 1), xytext=(2.2, 2.6),
                fontsize=11, color=RED, fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-1, 4); ax.set_ylim(-4, 5.5)
    ax.set_title('Elimination: align coefficients, add to cancel a variable', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='lower right')
    fig.tight_layout()
    save(fig, '07B', '07b-elimination.png')

def a_synthetic_division():
    """Clean synthetic division tableau for x^3-6x^2+11x-6 divided by (x-1)."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.4)
    ax.axis('off')

    cols = [3.2, 4.8, 6.4, 8.0]   # column centers (tight, even spacing 1.6)

    # title
    ax.set_title('Synthetic division: $x^3-6x^2+11x-6$ divided by $(x-1)$',
                 fontweight='bold', fontsize=12.5)

    # dividend coefficients
    for v, x in zip(['1', '-6', '11', '-6'], cols):
        ax.text(x, 4.25, v, ha='center', va='center', fontsize=15, color=BLUE, fontweight='bold')
    ax.text(3.2, 4.85, 'dividend coefficients', ha='center', fontsize=9, color='#777')

    # divisor box (root of x-1)
    ax.add_patch(Rectangle((1.55-0.45, 4.25-0.38), 0.9, 0.76, facecolor='#f3e5f5',
                           edgecolor=PURPLE, lw=2.2))
    ax.text(1.55, 4.25, '1', ha='center', va='center', fontsize=15, color=PURPLE,
            fontweight='bold')
    ax.text(1.55, 3.5, 'root $r=1$', ha='center', fontsize=9.5, color=PURPLE, fontweight='bold')

    # vertical bar: divisor | columns
    ax.plot([2.5, 2.5], [2.85, 4.72], color='#333', lw=1.8)

    # multiply row (1×1, 1×(−5), 1×6) — under columns 2-4
    for v, x in zip(['1', '-5', '6'], cols[1:]):
        ax.text(x, 3.35, v, ha='center', va='center', fontsize=12.5, color=GREEN,
                fontweight='bold')

    # horizontal rule
    ax.plot([2.5, cols[-1]+0.65], [2.85, 2.85], color='#333', lw=1.8)

    # quotient + remainder row
    for v, x in zip(['1', '-5', '6', '0'], cols):
        ax.text(x, 2.15, v, ha='center', va='center', fontsize=15,
                color=RED if v == '0' else BLUE, fontweight='bold')

    # remainder divider bar
    ax.plot([cols[-1]-0.6, cols[-1]-0.6], [1.72, 2.58], color=RED, lw=2.2)

    # row captions
    ax.text(4.8, 1.25, 'quotient  $x^2-5x+6$', ha='center', fontsize=12, color=BLUE,
            fontweight='bold')
    ax.text(8.0, 1.25, 'remainder  $0$', ha='center', fontsize=12, color=RED, fontweight='bold')

    # algorithm caption
    ax.text(5.0, 0.35, 'bring down $1$  $\\to$  $\\times 1$, add $\\to$ $-5$  $\\to$  $\\times 1$, add $\\to$  $6$  $\\to$  $\\times 1$, add $\\to$  $0$',
            ha='center', fontsize=11, color='#222', fontweight='bold')

    fig.tight_layout()
    save(fig, '07A', '07a-synthetic-division.png')

def a_discriminant():
    """Discriminant: D>0 two real roots, D=0 one, D<0 none over the reals."""
    fig, ax = plt.subplots(figsize=(9, 5.2)); g(ax)
    x = np.linspace(-2.6, 2.6, 800)
    ax.plot(x, x**2 - 1, BLUE, lw=2.4, label=r'$x^2-1$: $D=4>0$ (2 roots)')
    ax.plot(x, x**2, GREEN, lw=2.4, label=r'$x^2$: $D=0$ (1 root)')
    ax.plot(x, x**2 + 1, RED, lw=2.4, ls='--', label=r'$x^2+1$: $D=-4<0$ (no real roots)')
    for r in (-1, 1):
        ax.plot([r], [0], 'o', color=BLUE, ms=8, zorder=6)
    ax.plot([0], [0], 'o', color=GREEN, ms=8, zorder=6)
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.text(1.65, 2.75, 'no $x$-intercepts', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.2, 6.5)
    ax.set_title('The discriminant $b^2-4ac$ decides: 2, 1, or 0 real roots', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '07A', '07a-discriminant.png')

def b_consistent_inconsistent():
    """Two panels: parallel lines (no solution) vs coincident lines (infinite solutions)."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    # left: parallel lines
    ax = axes[0]; g(ax)
    x = np.linspace(-1, 5, 300)
    ax.plot(x, 3 - x, BLUE, lw=2.4, label=r'$x+y=3$')
    ax.plot(x, 3.5 - x, RED, lw=2.4, ls='--', label=r'$2x+2y=7$')
    ax.text(2.5, 3.6, 'no solution\n(parallel, inconsistent)', ha='center', fontsize=11,
            color='#222', fontweight='bold')
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.set_title('Parallel lines — no intersection', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=8, loc='lower left')
    # right: coincident lines
    ax = axes[1]; g(ax)
    ax.plot(x, 3 - x, BLUE, lw=2.8, label=r'$x+y=3$')
    ax.plot(x, 3 - x, RED, lw=1.6, ls='--', label=r'$2x+2y=6$')
    ax.fill_between(x, 3 - x, 3 - x, color=GREEN, alpha=0.0)
    ax.plot([1], [2], 'o', color=GREEN, ms=7, zorder=6)
    ax.text(2.5, 3.6, 'same line\n(infinitely many solutions)', ha='center', fontsize=11,
            color='#222', fontweight='bold')
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.set_title('Coincident lines — every point works', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=8, loc='lower left')
    fig.suptitle(r'Inconsistent vs. dependent systems: $D=0$ means 0 or $\infty$ solutions',
                 fontweight='bold', fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    save(fig, '07B', '07b-consistent-inconsistent.png')

if __name__ == '__main__':
    for fn in (a_cubic_roots, a_diff_squares, a_factor_graph,
               b_system_intersection, b_line_circle, b_elimination,
               a_synthetic_division, a_discriminant, b_consistent_inconsistent):
        fn()
        print('done:', fn.__name__)
    print('All 07A/07B session graphs written under', BASE)
