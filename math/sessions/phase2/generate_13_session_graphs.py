#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 13A, 13B, 13C (same pattern as phase1 graphs)."""
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
for _sub in ('13A', '13B', '13C'):
    os.makedirs(os.path.join(BASE, _sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'

def save(fig, sub, name):
    fig.savefig(os.path.join(BASE, sub, name), bbox_inches='tight')
    plt.close(fig)

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

def hole(ax, x, y, color=RED, label=None):
    ax.plot([x], [y], 'o', mfc='white', mec=color, ms=9, mew=2, zorder=6, label=label)

# ───────────────────────── 13A ─────────────────────────

def a_limit_hole():
    """(x^2-4)/(x-2) = x+2 with a hole at (2,4)."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(0, 4, 800)
    x = x[np.abs(x - 2) > 1e-3]
    ax.plot(x, x + 2, BLUE, lw=2.5, label=r'$y=x+2$')
    hole(ax, 2, 4)
    ax.annotate('hole at $(2,4)$\n$\\lim\\to 4$', (2, 4), xytext=(2.15, 2.1),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 4); ax.set_ylim(1, 6.5)
    ax.set_title(r'$f(x)=\frac{x^2-4}{x-2}=x+2$' '\n' 'the hole is the limit', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '13A', '13a-factored-hole.png')

def a_conjugate_hole():
    """(sqrt(x+4)-2)/x = 1/(sqrt(x+4)+2) with a hole at (0, 1/4)."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(-3.5, 3.5, 800)
    y = 1.0/(np.sqrt(x+4)+2)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y=\frac{1}{\sqrt{x+4}+2}$')
    hole(ax, 0, 0.25)
    ax.annotate('hole at $(0,\\frac{1}{4})$', (0, 0.25), xytext=(0.3, 0.30),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-3.5, 3.5); ax.set_ylim(0.08, 0.5)
    ax.set_title(r'$\frac{\sqrt{x+4}-2}{x}$' '\n' 'conjugate clears the root — hole at $(0,\\frac{1}{4})$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '13A', '13a-conjugate-hole.png')

def a_t_substitution():
    """sin(x-1)/(x-1) with a hole at (1,1) — the t = x-1 substitution."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(-1, 3, 2000)
    x = x[np.abs(x - 1) > 1e-3]
    y = np.sin(x-1)/(x-1)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y=\frac{\sin(x-1)}{x-1}$')
    hole(ax, 1, 1)
    ax.annotate('hole at $(1,1)$: put $t=x-1$\n$\\to\\frac{\\sin t}{t}\\to 1$', (1, 1),
                xytext=(1.15, -0.7), fontsize=10, color=RED, fontweight='bold')
    ax.axhline(1, color=GREEN, lw=1.1, ls='--', alpha=0.6)
    ax.set_xlim(-1, 3); ax.set_ylim(-1.2, 1.4)
    ax.set_title(r'$\frac{\sin(x-1)}{x-1}$' '\n' 'substitute $t=x-1$ to reach the standard limit',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '13A', '13a-t-substitution.png')

def a_onesided():
    """Piecewise f: x+2 for x<1, x^2 for x>=1 — jump at x=1 (left limit 3, right 1)."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    xl = np.linspace(0, 1 - 1e-4, 800)
    xr = np.linspace(1, 3, 800)
    ax.plot(xl, xl + 2, BLUE, lw=2.5, label=r'$x+2$ for $x<1$')
    ax.plot(xr, xr**2, RED, lw=2.5, label=r'$x^2$ for $x\geq1$')
    ax.plot([1], [1], 'o', color=RED, ms=7, zorder=6)
    hole(ax, 1, 3, color=BLUE)
    ax.annotate('left limit $=3$', (1, 3), xytext=(0.35, 3.4), fontsize=10, color=BLUE, fontweight='bold')
    ax.annotate('right limit $=1$', (1, 1), xytext=(1.35, 0.55), fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 3); ax.set_ylim(0, 8)
    ax.set_title('One-sided limits — left $\\neq$ right, so no limit at $x=1$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '13A', '13a-onesided.png')

def a_sinx_over_x():
    """sin(x)/x with a hole at (0,1)."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    x = np.linspace(-8, 8, 4000)
    x = x[np.abs(x) > 1e-3]
    y = np.sin(x)/x
    ax.plot(x, y, BLUE, lw=2.2)
    hole(ax, 0, 1)
    ax.annotate('hole at $(0,1)$ — the limit', (0, 1), xytext=(1.0, 0.9),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-8, 8); ax.set_ylim(-0.6, 1.3)
    ax.set_title(r'$\frac{\sin x}{x} \to 1$' ' as $x\\to 0$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '13A', '13a-sinx-over-x.png')

# ───────────────────────── 13B ─────────────────────────

def b_horizontal():
    """(3x^2+2x-1)/(x^2+5) approaches the horizontal asymptote y=3."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(0.5, 22, 2000)
    y = (3*x**2 + 2*x - 1)/(x**2 + 5)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y=\frac{3x^2+2x-1}{x^2+5}$')
    ax.axhline(3, color=GREEN, lw=1.5, ls='--', label=r'$y=3$')
    ax.annotate('horizontal asymptote $y=3$', (8, 3.06), fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(0.5, 22); ax.set_ylim(0, 4.5)
    ax.set_title(r'$\lim_{x\to\infty}\frac{3x^2+2x-1}{x^2+5}=3$' '\n' 'ratio of leading coefficients',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9)
    fig.tight_layout()
    save(fig, '13B', '13b-horizontal-asymptote.png')

def b_slant():
    """(x^2+1)/(x-1) approaches the slant asymptote y=x+1."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    xr = np.linspace(1.25, 9, 2000)
    y = (xr**2 + 1)/(xr - 1)
    ax.plot(xr, y, BLUE, lw=2.5, label=r'$y=\frac{x^2+1}{x-1}$')
    xl = np.linspace(-8, -1.25, 2000)
    ax.plot(xl, (xl**2 + 1)/(xl - 1), BLUE, lw=2.5)
    line_x = np.linspace(-8, 9, 300)
    ax.plot(line_x, line_x + 1, GREEN, lw=1.5, ls='--', label=r'$y=x+1$')
    ax.axvline(1, color='#999', lw=1.0, ls=':', alpha=0.6)
    ax.annotate('slant asymptote $y=x+1$', (3.0, -5.4), fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(-8, 9); ax.set_ylim(-9, 14)
    ax.set_title(r'$f(x)=\frac{x^2+1}{x-1}=x+1+\frac{2}{x-1}$' '\n' 'graph follows the slant line',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '13B', '13b-slant-asymptote.png')

# ───────────────────────── 13C ─────────────────────────

def c_discontinuities():
    """Three types of discontinuity: removable, jump, infinite."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.4))
    for ax in axes:
        ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.axis('off')
    # removable
    ax = axes[0]
    ax.add_patch(Rectangle((-3, -3), 6, 6, fc='#f8f9fa', ec='none'))
    x = np.linspace(-3, 3, 400)
    x = x[np.abs(x - 1) > 1e-3]
    ax.plot(x, x + 1, BLUE, lw=2.4)
    hole(ax, 1, 2)
    ax.set_title('removable (hole)\nlimit exists = 2, f(1) missing', fontsize=10.5, fontweight='bold')
    # jump
    ax = axes[1]
    ax.add_patch(Rectangle((-3, -3), 6, 6, fc='#f8f9fa', ec='none'))
    ax.plot([-3, 1 - 1e-3], [0, 0], BLUE, lw=2.4)
    ax.plot([1, 3], [1, 1], RED, lw=2.4)
    ax.plot([1], [1], 'o', color=RED, ms=6, zorder=6)
    hole(ax, 1, 0, color=BLUE)
    ax.set_title('jump\nleft limit 0, right limit 1', fontsize=10.5, fontweight='bold')
    # infinite
    ax = axes[2]
    ax.add_patch(Rectangle((-3, -3), 6, 6, fc='#f8f9fa', ec='none'))
    xr = np.linspace(0.05, 3, 600)
    xl = np.linspace(-3, -0.05, 600)
    ax.plot(xr, 1/xr, BLUE, lw=2.4)
    ax.plot(xl, 1/xl, BLUE, lw=2.4)
    ax.axvline(0, color='#999', lw=1.0, ls=':', alpha=0.6)
    ax.set_title('infinite\n$\\pm\\infty$ — vertical asymptote', fontsize=10.5, fontweight='bold')
    fig.suptitle('Three types of discontinuity', fontweight='bold', fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    save(fig, '13C', '13c-discontinuities.png')

def c_squeeze():
    """x^2 sin(1/x) squeezed between -x^2 and x^2."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(-1.2, 1.2, 4000)
    x = x[np.abs(x) > 1e-4]
    y = x**2*np.sin(1.0/x)
    ax.plot(x, y, BLUE, lw=1.6, label=r'$f(x)=x^2\sin\frac{1}{x}$')
    ax.plot(x, x**2, GREEN, lw=1.5, ls='--', label=r'$\pm x^2$')
    ax.plot(x, -x**2, GREEN, lw=1.5, ls='--')
    ax.annotate('squeezed to 0', (0, 0.72), ha='center', fontsize=11, color=GREEN, fontweight='bold')
    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1, 1)
    ax.set_title('Sandwich: $x^2\\sin\\frac{1}{x}$ trapped between $-x^2$ and $x^2$ → $0$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '13C', '13c-squeeze.png')

def c_ivt():
    """x^3 - 3x + 1 on [0,1]: f(0)=1, f(1)=-1 — IVT gives a root."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(0, 1.4, 1000)
    f = x**3 - 3*x + 1
    ax.plot(x, f, BLUE, lw=2.5, label=r'$f(x)=x^3-3x+1$')
    ax.axhline(0, color='#999', lw=1.0, ls=':')
    ax.plot([0], [1], 'o', color=RED, ms=7, zorder=6)
    ax.plot([1], [-1], 'o', color=RED, ms=7, zorder=6)
    ax.annotate('$f(0)=1$', (0, 1), xytext=(0.05, 1.25), fontsize=10, color=RED, fontweight='bold')
    ax.annotate('$f(1)=-1$', (1, -1), xytext=(1.05, -1.6), fontsize=10, color=RED, fontweight='bold')
    ax.annotate('sign change ⇒ root in $(0,1)$ by IVT', (0.7, 0.35), ha='center',
                fontsize=10.5, color=GREEN, fontweight='bold')
    ax.set_xlim(0, 1.4); ax.set_ylim(-1.8, 1.4)
    ax.set_title('IVT: a root must exist without solving the cubic', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$f(x)$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '13C', '13c-ivt.png')

def c_monotone():
    """a_{n+1} = sqrt(2 + a_n), a_1 = 1 — increasing, bounded, converges to 2."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    a = 1.0
    terms = [a]
    for _ in range(9):
        a = np.sqrt(2 + a)
        terms.append(a)
    n = np.arange(1, len(terms)+1)
    ax.plot(n, terms, 'o-', color=BLUE, ms=6, lw=2.0, label=r'$a_{n+1}=\sqrt{2+a_n}$')
    ax.axhline(2, color=GREEN, lw=1.5, ls='--', label=r'$L=2$ (fixed point)')
    ax.annotate('increasing, bounded above → converges', (4.0, 1.62), fontsize=10,
                color='#333', fontweight='bold')
    ax.set_xlim(0, 10); ax.set_ylim(0.9, 2.15)
    ax.set_title('Monotone + bounded ⇒ convergent (limit $L=\\sqrt{2+L}$)', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$a_n$')
    ax.legend(fontsize=9)
    fig.tight_layout()
    save(fig, '13C', '13c-monotone-sequence.png')

def a_complex_fraction_hole():
    """(1/x - 1/3)/(x-3) = -1/(3x) with a hole at (3, -1/9)."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(-6, 6, 1200)
    x = x[np.abs(x) > 1e-3]
    y = -1.0/(3*x)
    ax.plot(x, y, BLUE, lw=2.5, label=r'$y = -\frac{1}{3x}$')
    ax.axhline(0, color='#888', lw=1.0)
    ax.axvline(0, color='#888', lw=1.0, ls=':')
    hole(ax, 3, -1/9)
    ax.annotate('hole at $(3,-\\frac{1}{9})$\n$\\lim \\to -\\frac{1}{9}$', (3, -1/9),
                xytext=(3.6, -0.42), fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-6, 6); ax.set_ylim(-1.2, 1.2)
    ax.set_title(r'$\frac{\frac{1}{x}-\frac{1}{3}}{x-3} = -\frac{1}{3x}$' '\n'
                 'combine & cancel — the hole is the limit', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '13A', '13a-complex-fraction-hole.png')

def b_complex_fraction():
    """Nested fraction at infinity: x(x+1)/((x-1)(2x+3)) with HA y=1/2."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(-8, 8, 3000)
    x = x[(np.abs(x - 1) > 1e-3) & (np.abs(x + 1.5) > 1e-3)]
    y = x*(x+1)/((x-1)*(2*x+3))
    ax.plot(x, y, BLUE, lw=2.2, label=r'$y = \frac{x(x+1)}{(x-1)(2x+3)}$')
    ax.axhline(0.5, color=GREEN, lw=1.6, ls='--', label=r'HA $y = \frac{1}{2}$')
    ax.axvline(1, color='#999', lw=1.2, ls=':')
    ax.axvline(-1.5, color='#999', lw=1.2, ls=':')
    ax.annotate(r'$\to \frac{1}{2}$', (5.5, 0.66), fontsize=12, color=GREEN, fontweight='bold')
    ax.set_xlim(-8, 8); ax.set_ylim(-6, 6)
    ax.set_title(r'$\frac{\ \frac{x+1}{x-1}\ }{\ \frac{2x+3}{x}\ } = \frac{x(x+1)}{(x-1)(2x+3)}$' '\n'
                 'flip & multiply, then the degree rule → $y=\\frac{1}{2}$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '13B', '13b-complex-fraction.png')

if __name__ == '__main__':
    a_limit_hole(); a_conjugate_hole(); a_t_substitution(); a_onesided(); a_sinx_over_x()
    a_complex_fraction_hole()
    b_horizontal(); b_slant(); b_complex_fraction()
    c_discontinuities(); c_squeeze(); c_ivt(); c_monotone()
    print('All 14 graphs written to', BASE)
