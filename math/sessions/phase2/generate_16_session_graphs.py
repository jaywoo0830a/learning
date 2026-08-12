#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 16A and 16B (same pattern as 13X/14X).

Outputs into graphs/0812/16A and graphs/0812/16B.
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
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0812')
for _sub in ('16A', '16B'):
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

# ───────────────────────── 16A ─────────────────────────

def a_sin_area():
    """FTC net signed area: sin x on [0,2π]; ∫0^π=2, ∫0^{2π}=0."""
    fig, ax = plt.subplots(figsize=(9, 4.8)); g(ax)
    x = np.linspace(0, 2*np.pi, 800)
    ax.plot(x, np.sin(x), BLUE, lw=2.4, label=r'$y=\sin x$')
    x1 = np.linspace(0, np.pi, 300)
    ax.fill_between(x1, np.sin(x1), 0, color=GREEN, alpha=0.35)
    x2 = np.linspace(np.pi, 2*np.pi, 300)
    ax.fill_between(x2, np.sin(x2), 0, color=RED, alpha=0.35)
    ax.axhline(0, color='#888', lw=1.0)
    ax.text(np.pi/2, 0.82, 'area $2$', ha='center', fontsize=12, color=GREEN, fontweight='bold')
    ax.text(3*np.pi/2, -0.82, 'area $-2$', ha='center', fontsize=12, color=RED, fontweight='bold')
    ax.annotate('$\\int_0^\\pi\\sin x\\,dx=2$\n$\\int_0^{2\\pi}\\sin x\\,dx=0$ (cancel)',
                (5.4, 0.6), xytext=(4.4, 1.15), fontsize=11, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.3))
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.35, 1.35)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['$0$', '$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_title('Definite integral = net signed area: above counts $+$, below counts $-$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '16A', '16a-sin-area.png')

def a_ftc_area():
    """FTC geometry: area under f from a to b = F(b)−F(a)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0, 4.2, 800)
    f = 0.5*x**2 + 0.6
    ax.plot(x, f, BLUE, lw=2.6, label=r'$y=f(x)$')
    xs = np.linspace(1, 3, 300)
    ax.fill_between(xs, 0.5*xs**2 + 0.6, 0, color=GREEN, alpha=0.35)
    ax.axvline(1, color='#888', lw=1.2, ls='--')
    ax.axvline(3, color='#888', lw=1.2, ls='--')
    ax.text(1, -0.42, '$a$', ha='center', fontsize=12, color='#555')
    ax.text(3, -0.42, '$b$', ha='center', fontsize=12, color='#555')
    ax.text(2, 2.2, 'area $= \\int_a^b f(x)\\,dx$\n$= F(b)-F(a)$', ha='center',
            fontsize=12, color='#222', fontweight='bold')
    ax.annotate('$F$ is any antiderivative:\n$F\'(x)=f(x)$', (3.5, 6.4), xytext=(0.3, 6.0),
                fontsize=10, color='#222', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#222', lw=1.3))
    ax.set_xlim(0, 4.2); ax.set_ylim(-0.7, 7.6)
    ax.set_title('FTC: the area under $f$ from $a$ to $b$ equals $F(b)-F(a)$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '16A', '16a-ftc-area.png')

def a_average_value():
    """Average value: equal-area rectangle. f=x² on [0,3], avg = 3."""
    fig, ax = plt.subplots(figsize=(8.5, 5.4)); g(ax)
    x = np.linspace(0, 3, 600)
    ax.plot(x, x**2, BLUE, lw=2.6, label=r'$f(x)=x^2$')
    xs = np.linspace(0, 3, 300)
    ax.fill_between(xs, xs**2, 0, color=BLUE, alpha=0.18)
    # equal-area rectangle at height 3
    ax.add_patch(Rectangle((0, 0), 3, 3, facecolor=GREEN, alpha=0.30, edgecolor=GREEN, lw=2.2))
    ax.axhline(3, color=GREEN, lw=2.0, ls='--')
    ax.text(1.5, 3.35, 'average value $\\bar f = 3$', ha='center', fontsize=12,
            color=GREEN, fontweight='bold')
    ax.annotate('rectangle $3\\times 3$ has the same area\n$\\int_0^3 x^2\\,dx = 9$',
                (0.5, 0.4), xytext=(0.15, 4.9), fontsize=10.5, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.3))
    ax.set_xlim(0, 3.2); ax.set_ylim(0, 9.6)
    ax.set_title('Average value $\\bar f=\\frac{1}{b-a}\\int_a^b f$ — the equal-area rectangle',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '16A', '16a-average-value.png')

# ───────────────────────── 16B ─────────────────────────

def b_trig_sub_triangles():
    """The three reference triangles for trig substitution (Example 14), one small figure each.

    Correct orientation: the two legs meet at the bottom-RIGHT corner = right angle;
    θ is the bottom-LEFT acute corner; vertical leg on the right, horizontal leg on the bottom.
    """
    def tri_fig(name, opp, adj, hyp, caption, title):
        fig, ax = plt.subplots(figsize=(4.8, 4.2))
        ax.axis('off')
        x0, y0, base, height = 1.7, 1.9, 3.0, 2.2
        # triangle: bottom-left = θ corner, bottom-right = right angle, top-right = hyp end
        ax.add_patch(Polygon([(x0, y0), (x0 + base, y0), (x0 + base, y0 + height)],
                             closed=True, fill=False, edgecolor=BLUE, lw=2.4))
        # right-angle square at the bottom-RIGHT corner (where the legs meet)
        s = 0.16
        ax.add_patch(Rectangle((x0 + base - s, y0), s, s, facecolor=BLUE, edgecolor='none'))
        # θ arc at the bottom-LEFT acute corner
        th = np.linspace(0, np.arctan2(height, base), 40)
        ax.plot(x0 + 0.36*np.cos(th), y0 + 0.36*np.sin(th), color=RED, lw=1.8)
        ax.text(x0 + 0.52, y0 + 0.24, '$\\theta$', fontsize=12, color=RED, fontweight='bold')
        # side labels placed OUTSIDE the edges (no overlap)
        ax.text(x0 + base/2, y0 + height/2 + 0.24, hyp, ha='center', fontsize=11.5,
                color=BLUE, fontweight='bold')           # hypotenuse above
        ax.text(x0 + base + 0.42, y0 + height/2, opp, ha='left', va='center', fontsize=11.5,
                color=RED, fontweight='bold')            # opposite, right of vertical leg
        ax.text(x0 + base/2, y0 - 0.34, adj, ha='center', fontsize=11.5, color=GREEN,
                fontweight='bold')                       # adjacent below the base
        # captions
        ax.text(x0 + base/2, y0 - 0.86, caption, ha='center', fontsize=10, color='#222',
                fontweight='bold')
        ax.text(x0 + base/2, y0 - 1.26, title, ha='center', fontsize=12, color=GREEN,
                fontweight='bold')
        ax.set_xlim(0.6, 6.5); ax.set_ylim(0, 4.5)
        fig.tight_layout()
        save(fig, '16B', name)

    # 1) sin case: x = a sin θ → opp = x, adj = √(a²−x²), hyp = a
    tri_fig('16b-trig-sub-sin.png',
            '$x$', '$\\sqrt{a^2-x^2}$', '$a$',
            'hyp $= a$, opp $= x$, adj $= \\sqrt{a^2-x^2}$',
            '$x = a\\sin\\theta$')
    # 2) tan case: x = a tan θ → opp = x, adj = a, hyp = √(x²+a²)
    tri_fig('16b-trig-sub-tan.png',
            '$x$', '$a$', '$\\sqrt{x^2+a^2}$',
            'opp $= x$, adj $= a$, hyp $= \\sqrt{x^2+a^2}$',
            '$x = a\\tan\\theta$')
    # 3) sec case: x = a sec θ → opp = √(x²−a²), adj = a, hyp = x
    tri_fig('16b-trig-sub-sec.png',
            '$\\sqrt{x^2-a^2}$', '$a$', '$x$',
            'hyp $= x$, adj $= a$, opp $= \\sqrt{x^2-a^2}$',
            '$x = a\\sec\\theta$')

def b_decision_tree():
    """The integration decision tree as a flowchart."""
    fig, ax = plt.subplots(figsize=(9, 7.2)); g(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, 9)
    ax.axis('off')

    def box(x, y, w, h, text, fc, ec, fs=10.5, tc='black'):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=2.0, zorder=3))
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fs,
                color=tc, zorder=4, fontweight='bold')

    # top
    box(3.2, 8.15, 3.6, 0.75, 'Look at the integral —\nfirst match wins',
        '#e8f0fe', BLUE, fs=11, tc='#222')
    rows = [
        ('Basic dictionary form?', 'Antiderivative dictionary (16A)', '#e8f5e9'),
        ('$f(g(x))\\cdot g\'(x)$?', 'u-substitution (16A)', '#e8f5e9'),
        ('Product of different types?', 'Integration by parts (16B-A)', '#f3e5f5'),
        ('$\\sin^m x\\cos^n x$ or $\\tan^m x\\sec^n x$?', 'Trigonometric integrals (16B-B)', '#f3e5f5'),
        ('$\\sqrt{a^2\\pm x^2}$ or $\\sqrt{x^2-a^2}$?', 'Trigonometric substitution (16B-C)', '#fff3e0'),
        ('Rational $P(x)/Q(x)$?', 'Partial fractions (16B-D)', '#fff3e0'),
    ]
    y0 = 6.95
    dy = 1.12
    for i, (q, method, fc) in enumerate(rows):
        y = y0 - i*dy
        # question box (left), method box (right)
        box(0.4, y, 5.6, 0.85, q, '#fafafa', '#bbb', fs=10, tc='#222')
        box(6.6, y, 3.1, 0.85, method, fc, GREEN, fs=8.8, tc='#222')
        ax.annotate('', (6.55, y + 0.42), xytext=(6.05, y + 0.42),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.8))
        if i > 0:
            ax.annotate('', (3.2, y + dy - 0.05), xytext=(3.2, y + dy + 0.05),
                        arrowprops=dict(arrowstyle='->', color='#888', lw=1.4))
    ax.set_title('Integration decision tree — run top to bottom, first match wins',
                 fontweight='bold')
    fig.tight_layout()
    save(fig, '16B', '16b-decision-tree.png')

def b_parts_cycle():
    """The cycling pattern for ∫eˣ sin x dx: apply parts twice, solve for I."""
    fig, ax = plt.subplots(figsize=(10, 3.6)); g(ax)
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6)
    ax.axis('off')

    def box(x, y, w, h, text, fc, ec, fs=9.5, tc='#222'):
        ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=2.0, zorder=3))
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fs,
                color=tc, zorder=4, fontweight='bold')

    box(0.3, 1.3, 2.3, 1.1, '$I=\\int e^x\\sin x\\,dx$', '#e8f0fe', BLUE, fs=10)
    box(3.1, 1.3, 2.6, 1.1, '$=e^x\\sin x$\n$-\\int e^x\\cos x\\,dx$', '#f3e5f5', PURPLE, fs=9.5)
    box(6.2, 1.3, 2.6, 1.1, '$=e^x(\\sin x-\\cos x)$\n$-I$  (round 2)', '#f3e5f5', PURPLE, fs=9.5)
    box(9.1, 1.3, 0.7, 1.1, '$I$', '#fce4ec', RED, fs=10)
    # arrows
    ax.annotate('', (2.7, 1.85), xytext=(3.05, 1.85),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.annotate('', (5.8, 1.85), xytext=(6.15, 1.85),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.annotate('', (8.9, 1.85), xytext=(9.05, 1.85),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2.0))
    # cycle back arrow on top
    ax.annotate('', (7.5, 3.15), xytext=(1.7, 3.15),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.8,
                                connectionstyle='arc3,rad=-0.3'))
    ax.text(4.6, 3.3, 'the integral $I$ reappears → solve algebraically: $2I=e^x(\\sin x-\\cos x)$',
            ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.text(4.6, 0.45, '$I=\\frac{e^x}{2}(\\sin x-\\cos x)+C$', ha='center', fontsize=12,
            color='#222', fontweight='bold')
    ax.set_title('Cycling integrals: parts twice, then solve for $I$', fontweight='bold')
    fig.tight_layout()
    save(fig, '16B', '16b-parts-cycle.png')

if __name__ == '__main__':
    for fn in (a_sin_area, a_ftc_area, a_average_value,
               b_trig_sub_triangles, b_decision_tree, b_parts_cycle):
        fn()
        print('done:', fn.__name__)
    print('All 16A/16B session graphs written under', BASE)
