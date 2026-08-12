#!/usr/bin/env python3
"""Generate solution graphs for 07A-solutions.md and 07B-solutions.md.

Outputs into solutions/graphs/07A and 07B.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'solutions', 'graphs')
for sub in ('07A', '07B'):
    os.makedirs(os.path.join(BASE, sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

def save(fig, sub, name):
    fig.savefig(os.path.join(BASE, sub, name), bbox_inches='tight')
    plt.close(fig)

# ───────────────────────── 07A ─────────────────────────

def a_p1():
    """P1: x^3-4x^2+x+6 = (x+1)(x-2)(x-3), roots -1,2,3."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(-2.2, 4.2, 800)
    f = x**3 - 4*x**2 + x + 6
    ax.plot(x, f, BLUE, lw=2.6, label=r'$f(x)=x^3-4x^2+x+6$')
    ax.axhline(0, color='#888', lw=1.0)
    for r in (-1, 2, 3):
        ax.plot([r], [0], 'o', color=RED, ms=9, zorder=6)
        ax.annotate('$%d$' % r, (r, 0), xytext=(r - 0.18, 0.8), fontsize=11,
                    color=RED, fontweight='bold')
    ax.annotate('$=(x+1)(x-2)(x-3)$\n$f(-1)=0$ → synthetic → $(x+1)(x^2-5x+6)$',
                (0.6, 2.6), xytext=(-2.1, 5.4), fontsize=10.5, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.3))
    ax.set_xlim(-2.2, 4.2); ax.set_ylim(-6, 7)
    ax.set_title('Practice 1: $x^3-4x^2+x+6 = (x+1)(x-2)(x-3)$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '07A', 'p1-cubic-factor.png')

# ───────────────────────── 07B ─────────────────────────

def b_p3():
    """P3: x^2+y^2=13 and xy=6 → (±2,±3),(±3,±2) — 4 solutions."""
    fig, ax = plt.subplots(figsize=(7.6, 6.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 800)
    ax.plot(np.sqrt(13)*np.cos(th), np.sqrt(13)*np.sin(th), BLUE, lw=2.4,
            label=r'$x^2+y^2=13$')
    x = np.linspace(0.5, 6, 600)
    ax.plot(x, 6/x, GREEN, lw=2.4, label=r'$xy=6$')
    ax.plot(-x, -6/x, GREEN, lw=2.4)
    for (px, py) in [(2, 3), (3, 2), (-2, -3), (-3, -2)]:
        ax.plot([px], [py], 'o', color=RED, ms=8, zorder=7)
    ax.annotate('$(x+y)^2=x^2+y^2+2xy=25$\n$x+y=\\pm5$, $xy=6$ → 4 points', (2.2, 3.6),
                xytext=(-6.3, 2.6), fontsize=10.5, color='#222', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-6.3, 6.3); ax.set_ylim(-6.3, 6.3)
    ax.set_aspect('equal')
    ax.set_title('Practice 3: $x^2+y^2=13$, $xy=6$ — four intersection points',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '07B', 'p3-circle-hyperbola.png')

if __name__ == '__main__':
    for fn in (a_p1, b_p3):
        fn()
        print('done:', fn.__name__)
    print('All 07A/07B solution graphs written under', BASE)
