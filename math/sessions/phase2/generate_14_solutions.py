#!/usr/bin/env python3
"""Generate solution graphs for 14A-solutions.md, 14B-solutions.md, 14C-solutions.md"""
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
BASE = os.path.join(os.path.dirname(__file__), 'solutions', 'graphs')
for sub in ('14A', '14B', '14C'):
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

# ═══════════════════════════ 14A ═══════════════════════════

def a_p1():
    """P1: f(x)=x^2+3x with tangent at (2,10), slope f'(2)=7."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(-4, 2.6, 800)
    ax.plot(x, x**2 + 3*x, BLUE, lw=2.5, label=r'$f(x)=x^2+3x$')
    ax.plot(x, 7*x - 4, RED, lw=2.2, ls='--', label=r'tangent $y=7x-4$ (slope $7$)')
    ax.plot([2], [10], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$(2,10)$\n$f\'(2)=7$', (2, 10), xytext=(0.6, 11.5),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-4, 2.6); ax.set_ylim(-5, 15)
    ax.set_title('Practice 1: $f\'(2)=\\lim_{h\\to0}\\frac{f(2+h)-f(2)}{h}=7$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '14A', 'p1-tangent.png')

def a_p5():
    """P5: f(x)=x^3-3x^2-9x+5 with horizontal tangents at x=-1 (y=10) and x=3 (y=-22)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.4)); g(ax)
    x = np.linspace(-2.5, 4.5, 800)
    f = x**3 - 3*x**2 - 9*x + 5
    ax.plot(x, f, BLUE, lw=2.5, label=r'$f(x)=x^3-3x^2-9x+5$')
    ax.axhline(10, color=RED, lw=1.6, ls='--', alpha=0.8)
    ax.axhline(-22, color=RED, lw=1.6, ls='--', alpha=0.8)
    ax.plot([-1], [10], 'o', color=RED, ms=8, zorder=6)
    ax.plot([3], [-22], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$f\'(-1)=0$\n$(-1,10)$', (-1, 10), xytext=(-2.45, 9.0),
                fontsize=10, color=RED, fontweight='bold')
    ax.annotate('$f\'(3)=0$\n$(3,-22)$', (3, -22), xytext=(1.15, -27),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-2.5, 4.5); ax.set_ylim(-30, 18)
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_title('Practice 5: $f\'(x)=3(x-3)(x+1)$ — horizontal at $x=-1$ and $x=3$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '14A', 'p5-horizontal-tangents.png')

def a_p6():
    """P6: f(x)=x^2+ln x with tangent y=3x-2 at (1,1)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0.25, 2.4, 800)
    ax.plot(x, x**2 + np.log(x), BLUE, lw=2.5, label=r'$f(x)=x^2+\ln x$')
    ax.plot(x, 3*x - 2, RED, lw=2.2, ls='--', label=r'tangent $y=3x-2$ (slope $3$)')
    ax.plot([1], [1], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$(1,1)$\n$f\'(1)=2+1=3$', (1, 1), xytext=(1.05, -1.6),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0.25, 2.4); ax.set_ylim(-3, 6)
    ax.set_title('Practice 6: tangent at $x=1$ — $y=3x-2$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '14A', 'p6-tangent-line.png')

# ═══════════════════════════ 14B ═══════════════════════════

def b_p4():
    """P4: x^2+xy+y^2=7 with tangent at (1,2), slope -4/5."""
    fig, ax = plt.subplots(figsize=(8, 6)); g(ax)
    x = np.linspace(-3.05, 3.05, 1000)
    inner = 28 - 3*x**2
    ytop = (-x + np.sqrt(inner))/2
    ybot = (-x - np.sqrt(inner))/2
    ax.plot(x, ytop, BLUE, lw=2.5, label=r'$x^2+xy+y^2=7$')
    ax.plot(x, ybot, BLUE, lw=2.5)
    xs = np.linspace(-2.6, 4.0, 100)
    ax.plot(xs, 2 - 0.8*(xs - 1), RED, lw=2.2, ls='--', label='tangent: slope $-4/5$')
    ax.plot([1], [2], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$(1,2)$\n$\\frac{dy}{dx}=-\\frac{4}{5}$', (1, 2), xytext=(1.5, 2.35),
                fontsize=10, color=RED, fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-3.6, 4.2); ax.set_ylim(-3.8, 3.8)
    ax.set_aspect('equal')
    ax.set_title('Practice 4: implicit $y\'=\\frac{-(2x+y)}{x+2y}$ — at $(1,2)$ it is $-\\frac{4}{5}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14B', 'p4-implicit-tangent.png')

def b_p6():
    """P6: x=2t-t^2, y=3t^2-t^3 with a vertical tangent x=1 at t=1, point (1,2)."""
    fig, ax = plt.subplots(figsize=(8, 5.6)); g(ax)
    t = np.linspace(-1.6, 3.1, 1200)
    x = 2*t - t**2
    y = 3*t**2 - t**3
    ax.plot(x, y, BLUE, lw=2.5, label=r'$x=2t-t^2,\ y=3t^2-t^3$')
    ax.axvline(1, color=RED, lw=2.0, ls='--', label='vertical tangent $x=1$')
    ax.plot([1], [2], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$t=1$: $(1,2)$\n$\\frac{dy}{dx}$ undefined ($\\frac{3}{0}$)', (1, 2),
                xytext=(1.6, 2.9), fontsize=10, color=RED, fontweight='bold')
    ax.annotate('', (1, 3.0), xytext=(1, 4.0),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-4.5, 1.8); ax.set_ylim(-2, 7.5)
    ax.set_title('Practice 6: $\\frac{dy}{dx}=\\frac{6t-3t^2}{2-2t}$ — at $t=1$ the tangent is vertical',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14B', 'p6-parametric.png')

# ═══════════════════════════ 14C ═══════════════════════════

def c_p6():
    """P6: f(x)=x^3-3x^2-9x+5 — critical points, inflection, concavity regions."""
    fig, ax = plt.subplots(figsize=(9, 5.4)); g(ax)
    x = np.linspace(-2.4, 4.4, 800)
    f = x**3 - 3*x**2 - 9*x + 5
    ax.plot(x, f, BLUE, lw=2.6, label=r'$f(x)=x^3-3x^2-9x+5$')
    # critical points
    ax.plot([-1], [10], 'o', color=RED, ms=9, zorder=7)
    ax.plot([3], [-22], 'o', color=RED, ms=9, zorder=7)
    # inflection
    ax.plot([1], [-6], 'o', color=PURPLE, ms=9, zorder=7, mfc='white', mew=2.2)
    ax.annotate('local max $(-1,10)$\n$f\'=0$', (-1, 10), xytext=(-2.35, 11.5),
                fontsize=9.5, color=RED, fontweight='bold')
    ax.annotate('local min $(3,-22)$\n$f\'=0$', (3, -22), xytext=(3.1, -27),
                fontsize=9.5, color=RED, fontweight='bold')
    ax.annotate('inflection $(1,-6)$\n$f\'\'=0$, sign changes', (1, -6), xytext=(1.35, -2.5),
                fontsize=9.5, color=PURPLE, fontweight='bold')
    # concavity shading
    xl = np.linspace(-2.4, 1, 100)
    ax.fill_between(xl, xl**3 - 3*xl**2 - 9*xl + 5, -34, color=RED, alpha=0.10)
    xr = np.linspace(1, 4.4, 100)
    ax.fill_between(xr, xr**3 - 3*xr**2 - 9*xr + 5, -34, color=GREEN, alpha=0.10)
    ax.text(-1.7, -32, '$f\'\'<0$\nconcave down', ha='center', fontsize=9.5,
            color=RED, fontweight='bold')
    ax.text(3.0, -32, '$f\'\'>0$\nconcave up', ha='center', fontsize=9.5,
            color=GREEN, fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-2.4, 4.4); ax.set_ylim(-34, 20)
    ax.set_title('Practice 6: $f\'=3(x-3)(x+1)$, $f\'\'=6(x-1)$ — max, min, inflection',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '14C', 'p6-concavity.png')

if __name__ == '__main__':
    for fn in (a_p1, a_p5, a_p6, b_p4, b_p6, c_p6):
        fn()
        print('done:', fn.__name__)
    print('All 14X solution graphs written under', BASE)
