#!/usr/bin/env python3
"""Generate solution graphs for 13A-solutions.md, 13B-solutions.md, 13C-solutions.md"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import lgamma, log
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'solutions', 'graphs')
for sub in ('13A', '13B', '13C'):
    os.makedirs(os.path.join(BASE, sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

def hole(ax, x, y, color=RED, label=None):
    """Draw an open-circle 'hole' at (x,y)."""
    ax.plot([x], [y], 'o', mfc='white', mec=color, ms=9, mew=2, zorder=6, label=label)

# ═══════════════════════════ 13A ═══════════════════════════

def a1():
    """P1: (x^3-8)/(x-2) = x^2+2x+4 with hole at (2,12)."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(0, 4, 800)
    y = x**2 + 2*x + 4
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = x^2 + 2x + 4$')
    hole(ax, 2, 12)
    ax.annotate('hole at $(2,12)$', (2, 12), textcoords="offset points",
                xytext=(18, 14), fontsize=10, color=RED, fontweight='bold')
    ax.annotate(r'$\lim_{x\to2}\frac{x^3-8}{x-2} = 12$', (0.1, 25),
                fontsize=12, color=GREEN, fontweight='bold')
    ax.set_xlim(0, 4); ax.set_ylim(0, 30)
    ax.set_title('Practice 1: Difference of Cubes — $(x^3-8)/(x-2) = x^2+2x+4$, hole at $(2,12)$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13A', 'p1-cube-hole.png'), bbox_inches='tight')
    plt.close(fig)

def a2():
    """P2: (sqrt(x+9)-3)/x with hole at (0, 1/6)."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(-4, 4, 800)
    y = 1.0/(np.sqrt(x+9)+3)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \frac{1}{\sqrt{x+9}+3}$')
    hole(ax, 0, 1/6)
    ax.annotate('hole at $(0, \\frac{1}{6})$', (0, 1/6), textcoords="offset points",
                xytext=(16, 10), fontsize=10, color=RED, fontweight='bold')
    ax.annotate(r'$\lim_{x\to0}\frac{\sqrt{x+9}-3}{x} = \frac{1}{6}$', (-3.8, 0.30),
                fontsize=12, color=GREEN, fontweight='bold')
    ax.set_xlim(-4, 4); ax.set_ylim(0.05, 0.45)
    ax.set_title('Practice 2: Conjugate — $\\frac{\\sqrt{x+9}-3}{x} \\to \\frac{1}{6}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper right')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13A', 'p2-conjugate.png'), bbox_inches='tight')
    plt.close(fig)

def a3():
    """P3: sin(7x)/tan(3x) near 0 -> 7/3."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(-0.3, 0.3, 2000)
    y = np.sin(7*x)/np.tan(3*x)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \frac{\sin 7x}{\tan 3x}$')
    ax.axhline(7/3, color=GREEN, lw=1.2, ls='--', alpha=0.7, label=r'$y = \frac{7}{3}$')
    hole(ax, 0, 7/3)
    ax.annotate(r'$\to \frac{7}{3}$', (0.03, 7/3), textcoords="offset points",
                xytext=(8, 10), fontsize=11, color=GREEN, fontweight='bold')
    ax.set_title('Practice 3: Trig limit — $\\frac{\\sin 7x}{\\tan 3x} \\to \\frac{7}{3}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13A', 'p3-trig-ratio.png'), bbox_inches='tight')
    plt.close(fig)

def a4():
    """P4: three holes at x=2, x=3, x=-1, all -> 5."""
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    specs = [
        (r'$f_1(x)=\frac{x^2+x-6}{x-2}$', 2, 5, 0.5, 3.5, 'x+3'),
        (r'$f_2(x)=\frac{2x^2-7x+3}{x-3}$', 3, 5, 1.0, 5.0, '2x-1'),
        (r'$f_3(x)=\frac{x^2+7x+6}{x+1}$', -1, 5, -3.0, 1.0, 'x+6'),
    ]
    for ax, (title, a, L, lo, hi, fn) in zip(axes, specs):
        g(ax)
        x = np.linspace(lo, hi, 800)
        x = x[np.abs(x - a) > 1e-3]
        if fn == 'x+3':
            y = x + 3
        elif fn == '2x-1':
            y = 2*x - 1
        else:
            y = x + 6
        ax.plot(x, y, BLUE, lw=2.5)
        hole(ax, a, L)
        ax.axhline(L, color=GREEN, lw=1.0, ls='--', alpha=0.6)
        ax.annotate(f'hole at $x={a}$\n$\\to {L}$', (a, L), textcoords="offset points",
                    xytext=(12, 10), fontsize=9, color=RED, fontweight='bold')
        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
        ax.set_ylim(L - 2.5, L + 2.5)
    fig.suptitle('Practice 4: Three different $\\frac{0}{0}$ functions, all with limit $5$',
                 fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(os.path.join(BASE, '13A', 'p4-three-holes.png'), bbox_inches='tight')
    plt.close(fig)

def a5():
    """P5: (e^{3x}-1)/ln(1+2x) near 0 -> 3/2."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(-0.15, 0.15, 3000)
    y = (np.exp(3*x) - 1)/np.log(1 + 2*x)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \frac{e^{3x}-1}{\ln(1+2x)}$')
    ax.axhline(1.5, color=GREEN, lw=1.2, ls='--', alpha=0.7, label=r'$y = \frac{3}{2}$')
    hole(ax, 0, 1.5)
    ax.annotate(r'$\to \frac{3}{2}$', (0.012, 1.5), textcoords="offset points",
                xytext=(10, 8), fontsize=11, color=GREEN, fontweight='bold')
    ax.set_title('Practice 5: Two standard limits — $\\frac{e^{3x}-1}{\\ln(1+2x)} \\to \\frac{3}{2}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13A', 'p5-exp-log.png'), bbox_inches='tight')
    plt.close(fig)

def a6():
    """P6: piecewise sin(x)/x for x<0, e^x for x>=0; continuous at 0."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    xl = np.linspace(-4, -1e-6, 2000)
    xr = np.linspace(0, 1.2, 800)
    ax.plot(xl, np.sin(xl)/xl, BLUE, lw=2.5, label=r'$\frac{\sin x}{x}$ for $x<0$')
    ax.plot(xr, np.exp(xr), RED, lw=2.5, label=r'$e^x$ for $x\geq 0$')
    ax.plot([0], [1], 'o', color=GREEN, ms=7, zorder=6)
    ax.annotate('both branches meet at $(0,1)$', (0, 1), textcoords="offset points",
                xytext=(12, -18), fontsize=10, color=GREEN, fontweight='bold')
    ax.axhline(1, color='#999', lw=0.8, ls=':', alpha=0.5)
    ax.set_title('Practice 6: Piecewise — continuous at $x=0$ (left = right = 1)',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.set_ylim(-0.4, 3.3)
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13A', 'p6-piecewise.png'), bbox_inches='tight')
    plt.close(fig)

# ═══════════════════════════ 13B ═══════════════════════════

def b1():
    """P1: sqrt(4x^2+3x)/(2x-1) -> 1."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(1, 30, 2000)
    y = np.sqrt(4*x**2 + 3*x)/(2*x - 1)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \frac{\sqrt{4x^2+3x}}{2x-1}$')
    ax.axhline(1, color=GREEN, lw=1.4, ls='--', label=r'$y=1$')
    ax.annotate('horizontal asymptote $y=1$', (12, 1.045), fontsize=10,
                color=GREEN, fontweight='bold')
    ax.set_xlim(1, 30); ax.set_ylim(0.9, 2.2)
    ax.set_title('Practice 1: Radical at infinity — $\\frac{\\sqrt{4x^2+3x}}{2x-1} \\to 1$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'p1-radical-infinity.png'), bbox_inches='tight')
    plt.close(fig)

def b2():
    """P2: (2x^3-5x+1)/(3x^3+4x^2) -> 2/3."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(1, 30, 2000)
    y = (2*x**3 - 5*x + 1)/(3*x**3 + 4*x**2)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \frac{2x^3-5x+1}{3x^3+4x^2}$')
    ax.axhline(2/3, color=GREEN, lw=1.4, ls='--', label=r'$y = \frac{2}{3}$')
    ax.annotate('ratio of leading coefficients $= \\frac{2}{3}$', (12, 0.718),
                fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(1, 30); ax.set_ylim(0.4, 0.85)
    ax.set_title('Practice 2: $\\frac{\\infty}{\\infty}$ — $\\frac{2x^3-5x+1}{3x^3+4x^2} \\to \\frac{2}{3}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'p2-rational-asymptote.png'), bbox_inches='tight')
    plt.close(fig)

def b3():
    """P3: sqrt(x^2+5x)-sqrt(x^2-3x) -> 4."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(3, 30, 2000)
    y = np.sqrt(x**2 + 5*x) - np.sqrt(x**2 - 3*x)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \sqrt{x^2+5x}-\sqrt{x^2-3x}$')
    ax.axhline(4, color=GREEN, lw=1.4, ls='--', label=r'$y=4$')
    ax.annotate(r'$\infty-\infty \to 4$ via conjugate', (12, 4.45),
                fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(1, 30); ax.set_ylim(3.2, 6.5)
    ax.set_title('Practice 3: $\\infty-\\infty$ — $\\sqrt{x^2+5x}-\\sqrt{x^2-3x} \\to 4$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'p3-diff-of-roots.png'), bbox_inches='tight')
    plt.close(fig)

def b4():
    """P4: 1/x^2 -> +infinity from both sides."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    xl = np.linspace(-2, -0.05, 800)
    xr = np.linspace(0.05, 2, 800)
    ax.plot(xl, 1/xl**2, BLUE, lw=2.5, label=r'$y = 1/x^2$')
    ax.plot(xr, 1/xr**2, BLUE, lw=2.5)
    ax.annotate(r'$x\to 0^-$: $+\infty$', (-1.8, 30), fontsize=10, color=RED, fontweight='bold')
    ax.annotate(r'$x\to 0^+$: $+\infty$', (0.6, 30), fontsize=10, color=RED, fontweight='bold')
    ax.annotate('squared denominator → both sides $0^+$', (0, 95), ha='center',
                fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(-2, 2); ax.set_ylim(0, 120)
    ax.set_title('Practice 4: $\\frac{1}{x^2} \\to +\\infty$ (two-sided)', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper center')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'p4-one-over-x2.png'), bbox_inches='tight')
    plt.close(fig)

def b5():
    """P5: (1+5/n)^{2n} -> e^10 ~ 22026."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    n = np.arange(1, 60)
    a = (1 + 5.0/n)**(2*n)
    ax.plot(n, a, 'o', color=BLUE, ms=4, label=r'$a_n = \left(1+\frac{5}{n}\right)^{2n}$')
    ax.axhline(np.e**10, color=GREEN, lw=1.4, ls='--', label=r'$e^{10} \approx 22026$')
    ax.annotate(r'$\to e^{10}$', (38, np.e**10 + 900), fontsize=11, color=GREEN, fontweight='bold')
    ax.set_xlim(0, 60); ax.set_ylim(0, 26000)
    ax.set_title('Practice 5: The $e$ limit — $\\left(1+\\frac{5}{n}\\right)^{2n} \\to e^{10}$',
                 fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$a_n$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'p5-e-limit.png'), bbox_inches='tight')
    plt.close(fig)

def b6():
    """P6: growth hierarchy — ratio (e^n+n^100)/(2^n+n!) -> 0."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    # Panel 1: the four sequences on a log scale
    g(ax1)
    n = np.arange(1, 130)
    ln10 = np.log(10.0)
    log_e = n/ln10
    log_pow = 100*np.log10(n)
    log_2 = n*np.log10(2)
    log_fact = np.array([lgamma(k+1)/ln10 for k in n])
    ax1.plot(n, log_e, BLUE, lw=2.2, label=r'$e^n$')
    ax1.plot(n, log_pow, RED, lw=2.2, label=r'$n^{100}$')
    ax1.plot(n, log_2, '#f9ab00', lw=2.2, label=r'$2^n$')
    ax1.plot(n, log_fact, GREEN, lw=2.2, label=r'$n!$')
    ax1.set_ylim(0, 220)
    ax1.set_xlabel('$n$'); ax1.set_ylabel(r'$\log_{10}$ value')
    ax1.set_title('Growth race (log scale): $n!$ overtakes everything', fontweight='bold')
    ax1.legend(fontsize=9, loc='upper left')

    # Panel 2: the ratio itself, computed in log space
    g(ax2)
    n2 = np.arange(1, 200)
    log_num = np.logaddexp(n2/ln10, 100*np.log10(n2))
    log_den = np.logaddexp(n2*np.log10(2), np.array([lgamma(k+1)/ln10 for k in n2]))
    log_ratio = log_num - log_den
    ax2.plot(n2, log_ratio, BLUE, lw=2.0, label=r'$\log_{10}\left(\frac{e^n+n^{100}}{2^n+n!}\right)$')
    ax2.axhline(0, color=GREEN, lw=1.2, ls='--')
    ax2.annotate(r'$\to 0$  (ratio $= e^n/n! \to 0$)', (120, -22),
                 fontsize=10, color=GREEN, fontweight='bold')
    ax2.set_xlabel('$n$'); ax2.set_ylabel(r'$\log_{10}$ ratio')
    ax2.set_title(r'Practice 6: $\frac{e^n+n^{100}}{2^n+n!} \to 0$', fontweight='bold')
    ax2.legend(fontsize=8, loc='upper right')

    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'p6-growth-hierarchy.png'), bbox_inches='tight')
    plt.close(fig)

# ═══════════════════════════ 13C ═══════════════════════════

def c1():
    """P1: removable — line y=x+2 with hole at (2,4)."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(0, 4, 800)
    x = x[np.abs(x - 2) > 1e-3]
    ax.plot(x, x + 2, BLUE, lw=2.5, label=r'$y = x+2$')
    hole(ax, 2, 4)
    ax.annotate('hole at $(2,4)$ — $f(2)$ undefined', (2, 4), textcoords="offset points",
                xytext=(16, 12), fontsize=10, color=RED, fontweight='bold')
    ax.annotate(r'$\lim_{x\to2}f(x) = 4$ exists', (0.2, 3.1), fontsize=11,
                color=GREEN, fontweight='bold')
    ax.set_xlim(0, 4); ax.set_ylim(1, 6.5)
    ax.set_title('Practice 1: Removable discontinuity — $(x^2-4)/(x-2)$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p1-removable.png'), bbox_inches='tight')
    plt.close(fig)

def c2():
    """P2: piecewise made continuous with k=-1."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    xl = np.linspace(0, 1 - 1e-6, 800)
    xr = np.linspace(1, 3, 800)
    ax.plot(xl, 2*xl - 1, BLUE, lw=2.5, label=r'$2x-1$ for $x<1$')
    ax.plot(xr, xr**2, RED, lw=2.5, label=r'$x^2$ for $x\geq 1$')
    ax.plot([1], [1], 'o', color=GREEN, ms=7, zorder=6)
    ax.annotate('meet at $(1,1)$ when $k=-1$', (1, 1), textcoords="offset points",
                xytext=(12, -18), fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(0, 3); ax.set_ylim(-1, 8)
    ax.set_title('Practice 2: Piecewise continuous at $x=1$ with $k=-1$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p2-piecewise-continuous.png'), bbox_inches='tight')
    plt.close(fig)

def c3():
    """P3: squeeze — x^3 cos(1/x^2) between +-|x^3|."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(-1.2, 1.2, 4000)
    x = x[np.abs(x) > 1e-4]
    y = x**3*np.cos(1.0/x**2)
    ax.plot(x, y, BLUE, lw=1.6, label=r'$f(x) = x^3\cos\frac{1}{x^2}$')
    ax.plot(x, x**3, GREEN, lw=1.6, ls='--', label=r'$+|x^3|$')
    ax.plot(x, -x**3, GREEN, lw=1.6, ls='--', label=r'$-|x^3|$')
    ax.annotate('squeezed to 0', (0, 0.55), ha='center', fontsize=11,
                color=GREEN, fontweight='bold')
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1, 1)
    ax.set_title('Practice 3: Sandwich — $x^3\\cos(1/x^2) \\to 0$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p3-squeeze.png'), bbox_inches='tight')
    plt.close(fig)

def c4():
    """P4: IVT — x^5-2x^3+x-1 on [0,2] crosses zero."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(0, 2, 2000)
    f = x**5 - 2*x**3 + x - 1
    ax.plot(x, f, BLUE, lw=2.5, label=r'$f(x) = x^5 - 2x^3 + x - 1$')
    ax.axhline(0, color='#999', lw=1.0, ls=':')
    ax.plot([0], [-1], 'o', color=RED, ms=7, zorder=6)
    ax.plot([2], [17], 'o', color=RED, ms=7, zorder=6)
    ax.annotate('$f(0) = -1$', (0, -1), textcoords="offset points", xytext=(10, -4),
                fontsize=10, color=RED, fontweight='bold')
    ax.annotate('$f(2) = 17$', (2, 17), textcoords="offset points", xytext=(-44, 6),
                fontsize=10, color=RED, fontweight='bold')
    ax.annotate('sign change ⇒ root in $(0,2)$ by IVT', (1.0, 3.2), ha='center',
                fontsize=11, color=GREEN, fontweight='bold')
    ax.set_xlim(0, 2); ax.set_ylim(-4, 18)
    ax.set_title('Practice 4: IVT — a root of $x^5-2x^3+x-1$ must exist in $(0,2)$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p4-ivt-root.png'), bbox_inches='tight')
    plt.close(fig)

def c5():
    """P5: recursive sequence a_n = 4 - 1/2^{n-1} -> 4."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    n = np.arange(1, 11)
    a = 4 - 1.0/2.0**(n - 1)
    ax.plot(n, a, 'o-', color=BLUE, ms=6, lw=2.0,
            label=r'$a_n = 4 - \frac{1}{2^{n-1}}$')
    ax.axhline(4, color=GREEN, lw=1.4, ls='--', label=r'$L = 4$ (fixed point)')
    ax.annotate(r'$a_1=3$', (1, 3.05), textcoords="offset points", xytext=(2, 8),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 10); ax.set_ylim(2.8, 4.15)
    ax.set_title('Practice 5: $a_{n+1}=\\frac{a_n+4}{2}$ converges to the fixed point $L=4$',
                 fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$a_n$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p5-recursive-limit.png'), bbox_inches='tight')
    plt.close(fig)

def c6():
    """P6: three-piece function continuous at 0."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    xl = np.linspace(-4, -1e-6, 2000)
    xr = np.linspace(1e-6, 1.5, 2000)
    ax.plot(xl, np.sin(xl)/xl, BLUE, lw=2.5, label=r'$\frac{\sin x}{x}$ for $x<0$')
    ax.plot(xr, (np.exp(xr) - 1)/xr, RED, lw=2.5, label=r'$\frac{e^x-1}{x}$ for $x>0$')
    ax.plot([0], [1], 'o', color=GREEN, ms=9, zorder=6, label=r'$f(0)=1$')
    ax.axhline(1, color='#999', lw=0.8, ls=':', alpha=0.5)
    ax.annotate('all three meet at height 1', (0, 1), textcoords="offset points",
                xytext=(14, -20), fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(-4, 1.5); ax.set_ylim(-0.3, 2.2)
    ax.set_title('Practice 6: Three branches meeting at $(0,1)$ — continuous at $0$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p6-three-piece.png'), bbox_inches='tight')
    plt.close(fig)

def a_d11():
    """D11: (1/x-1/4)/(x-4) = -1/(4x) with a hole at (4, -1/16)."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(-8, 8, 1200)
    x = x[np.abs(x) > 1e-3]
    y = -1.0/(4*x)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = -\frac{1}{4x}$')
    ax.axhline(0, color='#999', lw=1.0, ls=':')
    hole(ax, 4, -1/16)
    ax.annotate('hole at $(4,-\\frac{1}{16})$', (4, -1/16), textcoords="offset points",
                xytext=(14, 10), fontsize=10, color=RED, fontweight='bold')
    ax.annotate(r'$\lim_{x\to4}\frac{\ \frac{1}{x}-\frac{1}{4}\ }{x-4} = -\frac{1}{16}$',
                (-7.8, 0.30), fontsize=12, color=GREEN, fontweight='bold')
    ax.set_xlim(-8, 8); ax.set_ylim(-0.6, 0.6)
    ax.set_title('D11: Complex fraction — $\\frac{\\ \\frac{1}{x}-\\frac{1}{4}\\ }{x-4} \\to -\\frac{1}{16}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13A', 'd11-complex-fraction.png'), bbox_inches='tight')
    plt.close(fig)

def b_d11():
    """D11: (2x+1)(x+1)/x^2 with horizontal asymptote y=2."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(0.5, 30, 1200)
    y = (2*x+1)*(x+1)/x**2
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = \frac{(2x+1)(x+1)}{x^2}$')
    ax.axhline(2, color=GREEN, lw=1.4, ls='--', label=r'$y=2$')
    ax.annotate('horizontal asymptote $y=2$', (14, 2.14), fontsize=10,
                color=GREEN, fontweight='bold')
    ax.set_xlim(0.5, 30); ax.set_ylim(1.6, 3.6)
    ax.set_title('D11: Complex fraction at infinity — $\\frac{\\ \\frac{2x+1}{x}\\ }{\\ \\frac{x}{x+1}\\ } \\to 2$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13B', 'd11-complex-fraction.png'), bbox_inches='tight')
    plt.close(fig)

def c7():
    """P7: (1/x-1/3)/(x-3) = -1/(3x), continuity restored by filling (3,-1/9)."""
    fig, ax = plt.subplots(figsize=(9, 5.5)); g(ax)
    x = np.linspace(-6, 6, 1200)
    x = x[np.abs(x) > 1e-3]
    y = -1.0/(3*x)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = -\frac{1}{3x}$')
    ax.axhline(0, color='#999', lw=1.0, ls=':')
    ax.plot([3], [-1/9], 'o', color=GREEN, ms=8, zorder=6,
            label=r'$f(3) = -\frac{1}{9}$ (filled)')
    ax.annotate(r'$k=-\frac{1}{9}$ fills the hole → continuous', (3, -1/9),
                textcoords="offset points", xytext=(16, -20), fontsize=10,
                color=GREEN, fontweight='bold')
    ax.set_xlim(-6, 6); ax.set_ylim(-0.8, 0.8)
    ax.set_title('Practice 7: $\\frac{\\ \\frac{1}{x}-\\frac{1}{3}\\ }{x-3}$ — continuity restored at $k=-\\frac{1}{9}$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    fig.savefig(os.path.join(BASE, '13C', 'p7-complex-continuity.png'), bbox_inches='tight')
    plt.close(fig)

if __name__ == '__main__':
    a1(); a2(); a3(); a4(); a5(); a6(); a_d11()
    b1(); b2(); b3(); b4(); b5(); b6(); b_d11()
    c1(); c2(); c3(); c4(); c5(); c6(); c7()
    print('All 21 solution graphs written to', BASE)
