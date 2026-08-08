#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 14A, 14B, 14C (same pattern as phase1/13X graphs).

Outputs into graphs/0808/14A, graphs/0808/14B, graphs/0808/14C.
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
for _sub in ('14A', '14B', '14C'):
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

def hole(ax, x, y, color=RED, label=None):
    ax.plot([x], [y], 'o', mfc='white', mec=color, ms=9, mew=2, zorder=6, label=label)

# ───────────────────────── 14A ─────────────────────────

def a_tangent():
    """y = x^2 with the tangent line y = 2x - 1 at (1,1)."""
    fig, ax = plt.subplots(figsize=(8, 4.8)); g(ax)
    x = np.linspace(-1.4, 2.6, 800)
    ax.plot(x, x**2, BLUE, lw=2.5, label=r'$y=x^2$')
    ax.plot(x, 2*x - 1, RED, lw=2.2, ls='--', label=r'$y=2x-1$ (tangent at $x=1$)')
    ax.plot([1], [1], 'o', color=RED, ms=7, zorder=6)
    ax.annotate('$(1,1)$\nslope $f\'(1)=2$', (1, 1), xytext=(1.35, 0.35),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-1.4, 2.6); ax.set_ylim(-0.6, 5.5)
    ax.set_title('The tangent line: $f\'(a)$ is the slope at $x=a$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14A', '14a-tangent.png')

def a_sin_derivative():
    """sin x and cos x on [0, 2pi] — derivative of sin is cos."""
    fig, ax = plt.subplots(figsize=(9, 4.6)); g(ax)
    x = np.linspace(0, 2*np.pi, 800)
    ax.plot(x, np.sin(x), BLUE, lw=2.5, label=r'$f(x)=\sin x$')
    ax.plot(x, np.cos(x), RED, lw=2.2, ls='--', label=r"$f'(x)=\cos x$")
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5)
    # mark where the slope of sin x matches cos x: at pi/4, derivative 0.707
    ax.annotate('at $x=\\frac{\\pi}{4}$: slope of $\\sin x$\n= $\\cos\\frac{\\pi}{4}=\\frac{\\sqrt{2}}{2}$',
                (np.pi/4, np.sin(np.pi/4)), xytext=(1.4, 0.85),
                fontsize=9, color=RED, fontweight='bold')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.25, 1.35)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['$0$', '$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_title(r"$\frac{d}{dx}\sin x=\cos x$" ' — the slope of $\\sin x$ at each point is $\\cos x$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper right')
    fig.tight_layout()
    save(fig, '14A', '14a-sin-derivative.png')

def a_secant_to_tangent():
    """y = x^2 at a=1: secants through (1,1) and (1+h, (1+h)^2) approach the tangent."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    x = np.linspace(0, 2.6, 800)
    ax.plot(x, x**2, BLUE, lw=2.6, label=r'$y=x^2$')
    hs = [1.4, 0.7, 0.3]
    colors = [AMBER, GREEN, PURPLE]
    for h, c in zip(hs, colors):
        xa, ya = 1, 1
        xb, yb = 1 + h, (1 + h)**2
        m = (yb - ya) / (xb - xa)  # 2 + h
        xs = np.array([0.0, 2.6])
        ax.plot(xs, ya + m*(xs - xa), color=c, lw=1.8, ls='-',
                label=r'secant, slope $%s$' % ('%.1f' % (2 + h)))
    # tangent
    xt = np.linspace(0, 2.6, 100)
    ax.plot(xt, 2*xt - 1, RED, lw=2.2, ls='--', label=r'tangent, slope $2$')
    ax.plot([1], [1], 'o', color=RED, ms=7, zorder=6)
    ax.annotate('$a=1$', (1, 1), xytext=(1.05, -0.15), fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 2.6); ax.set_ylim(-0.4, 5.6)
    ax.set_title(r"$f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$" '\n'
                 'secant slopes $2+h$ squeeze down to the tangent slope $2$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14A', '14a-secant-to-tangent.png')

# ───────────────────────── 14B ─────────────────────────

def b_chain_layers():
    """Peel-the-onion diagram for sin(e^{x^2}): three stacked layers, each with its derivative."""
    fig, ax = plt.subplots(figsize=(9.5, 4.6)); g(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')

    # header: the composition
    ax.text(5.0, 5.55, r'$f(x)=\sin(e^{x^2})$' ' — peel from the outside in, layer by layer',
            ha='center', va='center', fontsize=12.5, fontweight='bold', color='#222')

    # peel-direction arrow on the left
    ax.annotate('', (0.42, 1.7), xytext=(0.42, 4.5),
                arrowprops=dict(arrowstyle='->', color='#666', lw=2.0))
    ax.text(0.42, 5.0, 'peel\norder', ha='center', va='bottom', fontsize=8.5,
            color='#666', fontweight='bold')

    # layer rows: (cy, color, fill, name, box math, derivative math, order)
    layers = [
        (4.5, BLUE,   '#e8f0fe', 'OUTER',  r'$\sin(□)$', r'$\cos(□)$', '1st'),
        (3.1, GREEN,  '#e8f5e9', 'MIDDLE', r'$e^{□}$',   r'$e^{□}$',   '2nd'),
        (1.7, PURPLE, '#f3e5f5', 'INNER',  r'$x^2$',     r'$2x$',      '3rd'),
    ]
    for cy, color, face, name, boxmath, dermath, order in layers:
        # layer box
        r = Rectangle((0.9, cy - 0.45), 4.7, 0.9, facecolor=face, edgecolor=color,
                      lw=2.2, zorder=3)
        ax.add_patch(r)
        # order badge (circle) on the left inside the box
        ax.text(1.05, cy, order, ha='center', va='center', fontsize=10,
                color='white', fontweight='bold', zorder=5,
                bbox=dict(boxstyle='circle,pad=0.28', facecolor=color, edgecolor='none'))
        # layer name + inner function inside the box
        ax.text(3.15, cy + 0.15, name, ha='center', va='center', fontsize=9,
                color=color, fontweight='bold')
        ax.text(3.15, cy - 0.22, boxmath, ha='center', va='center', fontsize=12.5,
                color='black', fontweight='bold')
        # arrow box -> derivative
        ax.annotate('', (5.75, cy), xytext=(5.6, cy),
                    arrowprops=dict(arrowstyle='->', color='#777', lw=1.8))
        # derivative
        ax.text(6.9, cy, dermath, ha='center', va='center', fontsize=12.5,
                color=color, fontweight='bold')

    # multiply chain at the bottom
    ax.text(5.0, 0.55, r'$\cos(e^{x^2})\cdot e^{x^2}\cdot 2x \;=\; 2x\,e^{x^2}\cos(e^{x^2})$',
            ha='center', va='center', fontsize=12, color=RED, fontweight='bold')

    fig.tight_layout()
    save(fig, '14B', '14b-chain-layers.png')

def b_implicit_tangent():
    """Circle x^2 + y^2 = 25 with tangent at (3,4): slope -3/4, radius slope 4/3."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 800)
    ax.plot(5*np.cos(th), 5*np.sin(th), BLUE, lw=2.5, label=r'$x^2+y^2=25$')
    # radius
    ax.plot([0, 3], [0, 4], GREEN, lw=2.0, ls='-', label='radius: slope $4/3$')
    # tangent: through (3,4) slope -3/4
    xs = np.linspace(-4.5, 8.5, 100)
    ax.plot(xs, 4 - 0.75*(xs - 3), RED, lw=2.2, ls='--', label='tangent: slope $-3/4$')
    ax.plot([3], [4], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$(3,4)$\n$\\frac{dy}{dx}=-\\frac{3}{4}$', (3, 4), xytext=(3.4, 4.6),
                fontsize=10, color=RED, fontweight='bold')
    ax.text(0.35, 2.2, '$r$', fontsize=12, color=GREEN, fontweight='bold')
    ax.text(2.6, 3.1, '$\\perp$', fontsize=12, color='#333', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-6.5, 8.5); ax.set_ylim(-6, 8)
    ax.set_aspect('equal')
    ax.set_title('Implicit: tangent $\\perp$ radius, slopes multiply to $-1$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '14B', '14b-implicit-tangent.png')

def b_parametric():
    """Parametric curve x=t^2, y=t^3 with tangent at t=2 (slope 3t/2 = 3)."""
    fig, ax = plt.subplots(figsize=(8, 5.6)); g(ax)
    t = np.linspace(-2.4, 2.4, 800)
    ax.plot(t**2, t**3, BLUE, lw=2.5, label=r'$x=t^2, \ y=t^3$')
    # tangent at t=2: point (4,8), slope 3
    xs = np.linspace(0.5, 7.5, 100)
    ax.plot(xs, 8 + 3*(xs - 4), RED, lw=2.2, ls='--', label='tangent at $t=2$: slope $3$')
    ax.plot([4], [8], 'o', color=RED, ms=8, zorder=6)
    ax.annotate('$t=2$: $(4,8)$\n$\\frac{dy}{dx}=\\frac{3t}{2}=3$', (4, 8), xytext=(4.3, 4.8),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-1, 7.5); ax.set_ylim(-13, 13)
    ax.set_title(r"$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}=\frac{3t^2}{2t}=\frac{3t}{2}$" ' — one rule, no $y$ needed',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '14B', '14b-parametric.png')

# ───────────────────────── 14C ─────────────────────────

def c_motion():
    """Car example: s(t)=t^3-6t^2+9t, v(t)=3t^2-12t+9, a(t)=6t-12 on [0,4]."""
    fig, ax = plt.subplots(figsize=(9, 5)); g(ax)
    t = np.linspace(0, 4, 800)
    s = t**3 - 6*t**2 + 9*t
    v = 3*t**2 - 12*t + 9
    a = 6*t - 12
    ax.plot(t, s, BLUE, lw=2.5, label=r'$s(t)=t^3-6t^2+9t$ (position)')
    ax.plot(t, v, RED, lw=2.2, label=r"$v(t)=s'(t)$ (velocity)")
    ax.plot(t, a, GREEN, lw=2.2, ls='--', label=r"$a(t)=s''(t)$ (acceleration)")
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5)
    for tc in (1, 3):
        ax.plot([tc], [0], 'o', color=RED, ms=6, zorder=6)
        ax.annotate('$v=0$ at $t=%d$' % tc, (tc, 0), xytext=(tc - 0.25, 2.6),
                    fontsize=9, color=RED, fontweight='bold')
    ax.set_xlim(0, 4); ax.set_ylim(-13, 13)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_title('Differentiate twice: position $\\to$ velocity $\\to$ acceleration', fontweight='bold')
    ax.set_xlabel('$t$ (seconds)'); ax.set_ylabel('$s$, $v$, $a$')
    ax.legend(fontsize=9, loc='upper left', ncol=1)
    fig.tight_layout()
    save(fig, '14C', '14c-motion.png')

def c_trig_cycle():
    """sin, cos, -sin, -cos on [0, 2pi] — the derivative cycle of 4."""
    fig, ax = plt.subplots(figsize=(9, 5.2)); g(ax)
    x = np.linspace(0, 2*np.pi, 800)
    ax.plot(x, np.sin(x), BLUE, lw=2.6, label=r'$f=\sin x$')
    ax.plot(x, np.cos(x), RED, lw=2.2, ls='--', label=r"$f'=\cos x$")
    ax.plot(x, -np.sin(x), GREEN, lw=2.2, ls='-.', label=r"$f''=-\sin x$")
    ax.plot(x, -np.cos(x), PURPLE, lw=2.2, ls=':', label=r"$f'''=-\cos x$")
    ax.plot(x, np.sin(x), BLUE, lw=1.0, alpha=0.0)
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5)
    # cycle arrows at bottom
    ax.annotate('', (1.6, -1.75), xytext=(0.6, -1.75),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.annotate('', (2.6, -1.75), xytext=(1.6, -1.75),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.annotate('', (3.6, -1.75), xytext=(2.6, -1.75),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.annotate('', (4.6, -1.75), xytext=(3.6, -1.75),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.text(1.1, -1.98, '$\\sin$', ha='center', fontsize=10, color=BLUE, fontweight='bold')
    ax.text(2.1, -1.98, '$\\cos$', ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(3.1, -1.98, '$-\\sin$', ha='center', fontsize=10, color=GREEN, fontweight='bold')
    ax.text(4.1, -1.98, '$-\\cos$', ha='center', fontsize=10, color=PURPLE, fontweight='bold')
    ax.text(5.1, -1.98, '$\\sin$ (cycle of 4)', ha='center', fontsize=10, color=BLUE, fontweight='bold')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-2.3, 1.45)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['$0$', '$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_title('Derivatives cycle through four shapes — divide $n$ by 4, read the remainder',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '14C', '14c-trig-cycle.png')

def c_concavity():
    """f(x)=x^3-3x: concave down for x<0, concave up for x>0, inflection at (0,0)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(-2.2, 2.2, 800)
    f = x**3 - 3*x
    ax.plot(x, f, BLUE, lw=2.6, label=r'$f(x)=x^3-3x$')
    # inflection point
    ax.plot([0], [0], 'o', color=RED, ms=9, zorder=7)
    ax.annotate('inflection at $(0,0)$\n$f\'\'(x)=6x$ changes sign', (0, 0),
                xytext=(0.15, -1.7), fontsize=10, color=RED, fontweight='bold')
    # shade concave-down region (x<0) and concave-up (x>0)
    xl = np.linspace(-2.2, 0, 100)
    ax.fill_between(xl, xl**3 - 3*xl, -4, color=RED, alpha=0.12)
    xr = np.linspace(0, 2.2, 100)
    ax.fill_between(xr, xr**3 - 3*xr, -4, color=GREEN, alpha=0.12)
    ax.text(-1.1, -3.4, '$f\'\'<0$\nconcave down', ha='center', fontsize=10,
            color=RED, fontweight='bold')
    ax.text(1.1, -3.4, '$f\'\'>0$\nconcave up', ha='center', fontsize=10,
            color=GREEN, fontweight='bold')
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-4, 4)
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_title('Concavity from $f\'\'$: sign of $f\'\'$ tells which way the graph bends',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '14C', '14c-concavity.png')

if __name__ == '__main__':
    for fn in (a_tangent, a_sin_derivative, a_secant_to_tangent,
               b_chain_layers, b_implicit_tangent, b_parametric,
               c_motion, c_trig_cycle, c_concavity):
        fn()
        print('done:', fn.__name__)
    print('All 14X session graphs written under', BASE)
