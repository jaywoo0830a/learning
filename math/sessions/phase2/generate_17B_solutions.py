#!/usr/bin/env python3
"""Generate solution graphs for 17B-solutions.md (same pattern as other solution graphs).

Outputs into solutions/graphs/17B.
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
os.makedirs(os.path.join(BASE, '17B'), exist_ok=True)

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

# ───────────────────────── 17B ─────────────────────────

def p1_arc_length():
    """P1: y=(2/3)x^{3/2} on [0,3], arc length = 14/3."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0, 3, 600)
    y = (2.0/3)*x**1.5
    ax.plot(x, y, BLUE, lw=2.6, label=r'$y=\frac{2}{3}x^{3/2}$')
    ax.plot([0, 3], [0, (2/3)*3**1.5], 'o', color=RED, ms=7)
    ax.annotate('$L=\\int_0^3\\sqrt{1+x}\\,dx$\n$=\\frac{2}{3}(4^{3/2}-1)=\\frac{14}{3}$',
                (1.8, 2.9), xytext=(0.6, 3.4), fontsize=11, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.4))
    ax.set_xlim(0, 3.2); ax.set_ylim(0, 4.4)
    ax.set_title('Practice 1: $y=\\frac{2}{3}x^{3/2}$ — arc length $=\\frac{14}{3}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '17B', 'p1-arc-length.png')

def p4_improper():
    """P4: ∫₀^∞ dx/(1+x²) = π/2 via arctan."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0, 12, 800)
    y = 1/(1+x**2)
    ax.plot(x, y, BLUE, lw=2.6, label=r'$y=\frac{1}{1+x^2}$')
    xs = np.linspace(0, 8, 300)
    ax.fill_between(xs, 1/(1+xs**2), 0, color=GREEN, alpha=0.3)
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5)
    ax.annotate(r'$\int_0^\infty \frac{dx}{1+x^2}=\lim_{b\to\infty}\arctan b=\frac{\pi}{2}$',
                (2.4, 0.35), xytext=(3.6, 0.72), fontsize=11, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.4))
    ax.set_xlim(0, 12); ax.set_ylim(0, 1.15)
    ax.set_title('Practice 4: improper integral $\\int_0^\\infty \\frac{dx}{1+x^2}=\\frac{\\pi}{2}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper right')
    fig.tight_layout()
    save(fig, '17B', 'p4-improper.png')

if __name__ == '__main__':
    for fn in (p1_arc_length, p4_improper):
        fn()
        print('done:', fn.__name__)
    print('All 17B solution graphs written under', BASE)
