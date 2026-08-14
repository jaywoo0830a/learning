#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 17B (same pattern as 13X/14X/17A).

Outputs into graphs/0808/17B.
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
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0808')
os.makedirs(os.path.join(BASE, '17B'), exist_ok=True)

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

# ─────────────────────── 5-scene walkthroughs ───────────────────────
# Each scene is its OWN image (17b-<topic>-sceneN.png), shown separately in
# the markdown — one figure per scene keeps every step large and readable.

def _scene_new(title, xlim, ylim, aspect=True, fs=(5.0, 4.0)):
    """A fresh, self-contained scene figure with a title bar."""
    fig, ax = plt.subplots(figsize=fs)
    ax.axis('off')
    ax.set_facecolor('#fafbfc')
    for s in ax.spines.values():
        s.set_visible(True); s.set_color('#cccccc')
    ax.text(0.02, 0.97, title, transform=ax.transAxes, fontsize=11, color='#222',
            fontweight='bold', va='top')
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if aspect:
        ax.set_aspect('equal')
    return fig, ax

def _scene_caption(ax, text):
    ax.text(0.5, -0.06, text, transform=ax.transAxes, fontsize=9, color='#333',
            ha='center', va='top')

def _scene_save(fig, name):
    fig.tight_layout()
    save(fig, '17B', name)

# ───────────────────────── 17B ─────────────────────────

def arc_length_scenes():
    """Arc length — 5 separate scene images (y=x^{3/2} on [0,4], L≈9.07)."""

    def curve(ax):
        x = np.linspace(0, 4, 400)
        ax.plot(x, x**1.5, BLUE, lw=2.6)
        ax.plot([0, 4], [0, 8], 'o', color=RED, ms=6)
        ax.text(0.15, 0.4, 'start', fontsize=9, color=RED, fontweight='bold')
        ax.text(4.05, 8.15, 'end', fontsize=9, color=RED, fontweight='bold')

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: what do we want?', (-0.5, 4.6), (-1.1, 9.4))
    curve(ax)
    ax.plot([0, 4], [0, 8], color='#999', lw=1.6, ls='--')
    ax.text(2.1, 4.05, 'chord (shorter)', fontsize=9.5, color='#777', fontweight='bold',
            rotation=63)
    ax.text(2.4, 6.7, 'the path itself', fontsize=10, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHEN: we measure distance ALONG the curve, not straight-line distance')
    _scene_save(fig, '17b-arclen-scene1.png')

    # Scene 2 — How: chop
    fig, ax = _scene_new('Scene 2 — How: chop into small pieces', (-0.5, 4.6), (-1.1, 9.4))
    curve(ax)
    ts = np.linspace(0, 4, 9)
    pts = np.array([ts, ts**1.5]).T
    ax.plot(pts[:, 0], pts[:, 1], color='#888', lw=1.3, ls='--')
    for p in pts:
        ax.plot([p[0]], [p[1]], 'o', color='#666', ms=3.5)
    ax.add_patch(Rectangle((3.5, 6.1), 0.5, 1.9, facecolor=RED, alpha=0.22,
                           edgecolor=RED, lw=1.2))
    ax.text(3.75, 8.15, 'zoom here', fontsize=8.5, color=RED, fontweight='bold',
            ha='center')
    _scene_caption(ax, 'HOW: replace the curve by many short straight segments')
    _scene_save(fig, '17b-arclen-scene2.png')

    # Scene 3 — How: one triangle
    fig, ax = _scene_new('Scene 3 — How: one segment is a hypotenuse', (-0.3, 4.3), (-0.6, 3.6))
    ax.plot([0.5, 2.9], [0.5, 0.5], GREEN, lw=2.0)
    ax.plot([2.9, 2.9], [0.5, 2.5], GREEN, lw=2.0)
    ax.plot([0.5, 2.9], [0.5, 2.5], RED, lw=2.8)
    ax.text(1.7, 0.25, '$\\Delta x$', ha='center', fontsize=12, color=GREEN,
            fontweight='bold')
    ax.text(3.05, 1.5, '$\\Delta y$', va='center', fontsize=12, color=GREEN,
            fontweight='bold')
    ax.text(1.5, 1.8, '$\\Delta L$', fontsize=12, color=RED, fontweight='bold', rotation=33)
    ax.text(2.1, 3.05, 'Pythagoras: $\\Delta L=\\sqrt{\\Delta x^2+\\Delta y^2}$',
            ha='center', fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'HOW: each segment is the hypotenuse of a tiny right triangle')
    _scene_save(fig, '17b-arclen-scene3.png')

    # Scene 4 — Where: the element
    fig, ax = _scene_new('Scene 4 — Where: the arc length element', (-0.3, 4.3), (-0.8, 4.0))
    ax.plot([0.5, 2.9], [0.5, 0.5], GREEN, lw=2.0)
    ax.plot([2.9, 2.9], [0.5, 2.5], GREEN, lw=2.0)
    ax.plot([0.5, 2.9], [0.5, 2.5], RED, lw=2.8)
    ax.text(1.7, 0.25, '$dx$', ha='center', fontsize=12, color=GREEN, fontweight='bold')
    ax.text(3.05, 1.5, "$dy=f'(x)\\,dx$", va='center', fontsize=10.5, color=GREEN,
            fontweight='bold')
    ax.text(0.55, 2.4, '$dL=\\sqrt{dx^2+dy^2}$', fontsize=11, color=RED, fontweight='bold')
    ax.text(2.1, -0.55, "$dL=\\sqrt{1+(f'(x))^2}\\,dx$", ha='center', fontsize=12,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: factor out $dx$ → $dL=\\sqrt{1+(f\')^2}\\,dx$')
    _scene_save(fig, '17b-arclen-scene4.png')

    # Scene 5 — Where: integrate
    fig, ax = _scene_new('Scene 5 — Where: sum them all', (-0.5, 4.6), (-1.1, 9.4))
    curve(ax)
    ax.text(2.2, -0.9, '$L=\\int_0^4 \\sqrt{1+(\\frac{3}{2}\\sqrt{x})^2}\\,dx$\n'
            '$=\\int_0^4\\sqrt{1+\\frac{9}{4}x}\\,dx \\approx 9.07$',
            ha='center', fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: integrate the element over $x\\in[0,4]$ → $L=\\int dL$')
    _scene_save(fig, '17b-arclen-scene5.png')

def helix_3d():
    """3D helix r(t)=(cos t, sin t, t), t in [0,6π], constant speed √2."""
    fig = plt.figure(figsize=(8, 6.5))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(0, 6*np.pi, 1500)
    ax.plot(np.cos(t), np.sin(t), t, color=BLUE, lw=2.2)
    ax.plot([0], [0], [0], 'o', color=RED, ms=7)
    ax.text(0, 0, 0.3, 'start', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
    ax.set_title(r'Helix $\vec{r}(t)=(\cos t,\sin t,t)$ — speed $|\vec{r}\,^{\prime}|=\sqrt{2}$ constant',
                 fontweight='bold')
    ax.view_init(elev=18, azim=-55)
    fig.tight_layout()
    save(fig, '17B', '17b-helix-3d.png')

def spiral_arc_length():
    """Archimedean spiral r=θ on [0,2π] with arc length annotation."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 1200)
    r = th
    ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=2.4)
    ax.plot([0], [0], 'o', color=RED, ms=6)
    ax.annotate('$L=\\int_0^{2\\pi}\\sqrt{1+\\theta^2}\\,d\\theta$\n$=\\frac{1}{2}[2\\pi\\sqrt{1+4\\pi^2}+\\ln(2\\pi+\\sqrt{1+4\\pi^2})]$\n$\\approx 21.26$',
                (0.5, 0.5), xytext=(-5.6, 2.4), fontsize=10.5, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.4))
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-6.6, 6.6); ax.set_ylim(-6.6, 6.6)
    ax.set_aspect('equal')
    ax.set_title(r'Archimedean spiral $r=\theta$ — arc length $\approx 21.26$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '17B', '17b-spiral-arc-length.png')

def cycloid():
    """One arch of the cycloid x=t-sin t, y=1-cos t, L=8 (a=1)."""
    fig, ax = plt.subplots(figsize=(9, 4.4)); g(ax)
    t = np.linspace(0, 2*np.pi, 1000)
    x = t - np.sin(t)
    y = 1 - np.cos(t)
    ax.plot(x, y, BLUE, lw=2.6, label=r'$x=t-\sin t,\ y=1-\cos t$')
    ax.plot([0, 2*np.pi], [0, 0], 'o', color=RED, ms=7)
    ax.annotate('one arch: $L=\\int_0^{2\\pi}2|\\sin(t/2)|\\,dt=8a$', (np.pi, 2),
                xytext=(np.pi-3.4, 1.9), fontsize=11, color='#222', fontweight='bold')
    ax.annotate('', (0, -0.45), xytext=(2*np.pi, -0.45),
                arrowprops=dict(arrowstyle='<->', color='#888', lw=1.4))
    ax.text(np.pi, -0.8, '$2\\pi a$ (one revolution of the wheel)', ha='center',
            fontsize=10, color='#888')
    ax.set_xlim(-0.4, 2*np.pi+0.4); ax.set_ylim(-1.2, 2.6)
    ax.set_xticks([0, np.pi, 2*np.pi])
    ax.set_xticklabels(['$0$', '$\\pi a$', '$2\\pi a$'])
    ax.set_title('Cycloid — one arch has length $8a$ (four diameters)', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '17B', '17b-cycloid.png')

def conical_spiral():
    """3D conical spiral (t cos t, t sin t, t), speed grows like √(t²+2)."""
    fig = plt.figure(figsize=(8, 6.5))
    ax = fig.add_subplot(111, projection='3d')
    t = np.linspace(0, 4*np.pi, 1500)
    ax.plot(t*np.cos(t), t*np.sin(t), t, color=PURPLE, lw=2.2)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
    ax.set_title(r'Conical spiral $\vec{r}(t)=(t\cos t,t\sin t,t)$ — speed $\sqrt{t^2+2}$ grows',
                 fontweight='bold')
    ax.view_init(elev=18, azim=-55)
    fig.tight_layout()
    save(fig, '17B', '17b-conical-spiral.png')

def surface_area_scenes():
    """Surface area — 5 separate scene images (y=√x about x-axis, S≈36.18)."""

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: the skin of the solid', (-0.6, 4.7), (-2.8, 3.0))
    x = np.linspace(0, 4, 300)
    ax.fill_between(x, -np.sqrt(x), np.sqrt(x), color=GREEN, alpha=0.18)
    ax.plot(x, np.sqrt(x), BLUE, lw=2.4)
    ax.plot(x, -np.sqrt(x), BLUE, lw=1.2, alpha=0.6)
    ax.plot([-0.3, 4.5], [0, 0], '#333', lw=2.0)
    ax.text(4.55, 0.15, 'axis', fontsize=9, color='#333')
    ax.text(2.0, -2.1, 'we want the area of this SKIN', ha='center', fontsize=10.5,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHEN: rotate the curve about the axis → measure the surface skin')
    _scene_save(fig, '17b-surface-scene1.png')

    # Scene 2 — How: slanted piece
    fig, ax = _scene_new('Scene 2 — How: a slanted slice', (-0.4, 4.6), (-1.3, 3.1))
    x = np.linspace(0, 4, 300)
    ax.plot(x, np.sqrt(x), BLUE, lw=2.0)
    xa, xb = 2.35, 2.95
    ax.plot([xa, xb], [np.sqrt(xa), np.sqrt(xb)], RED, lw=3.2)
    ax.annotate('slanted piece (length $ds$)', (xb, np.sqrt(xb)), xytext=(2.7, 2.5),
                fontsize=9.5, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.plot([xa, xa], [0, np.sqrt(xa)], color='#999', lw=1.4, ls=':')
    ax.text(xa - 0.22, np.sqrt(xa)/2, '$dx$', fontsize=9, color='#888', fontweight='bold')
    _scene_caption(ax, 'HOW: a slanted slice sweeps a CONICAL band (frustum), not a cylinder')
    _scene_save(fig, '17b-surface-scene2.png')

    # Scene 3 — How: one band
    fig, ax = _scene_new('Scene 3 — How: one band', (-1.9, 1.9), (-0.7, 2.7))
    r1, r2 = 1.5, 1.05
    ax.fill([-r1, -r2, r2, r1], [0.3, 1.6, 1.6, 0.3], color=RED, alpha=0.25,
            edgecolor=RED, lw=2.0)
    ax.plot([-r1, r1], [0.3, 0.3], '#333', lw=1.4)
    ax.annotate('radius $f(x)$', (-r1, 0.3), xytext=(-1.85, -0.4), fontsize=9.5,
                color='#222', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#222', lw=1.1))
    ax.annotate('slant $ds$', (-r2, 1.6), xytext=(-1.7, 2.1), fontsize=9.5,
                color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.text(0, 2.35, 'not $dx$ — the surface is slanted', ha='center', fontsize=9.5,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'HOW: band = radius $f(x)$, slant length $ds$ (the arc length element)')
    _scene_save(fig, '17b-surface-scene3.png')

    # Scene 4 — Where: the slant factor
    fig, ax = _scene_new('Scene 4 — Where: the slant factor', (-2.0, 4.9), (-1.0, 3.0))
    ax.add_patch(Rectangle((-1.9, 0.3), 1.4, 1.3, facecolor='#eee', edgecolor='#999',
                           lw=1.6))
    ax.text(-1.2, 2.1, 'cylinder: $2\\pi f\\,dx$', ha='center', fontsize=9.5, color='#999',
            fontweight='bold')
    ax.text(-1.2, -0.55, 'WRONG (too small)', ha='center', fontsize=9, color=RED,
            fontweight='bold')
    ax.fill([1.4, 1.85, 2.7, 2.25], [0.3, 1.6, 1.6, 0.3], color=GREEN, alpha=0.3,
            edgecolor=GREEN, lw=2.0)
    ax.text(2.1, 2.1, 'frustum: $2\\pi f\\,ds$', ha='center', fontsize=9.5, color=GREEN,
            fontweight='bold')
    ax.text(2.1, -0.55, 'RIGHT', ha='center', fontsize=9, color=GREEN, fontweight='bold')
    ax.text(1.45, -0.9, "$dS = 2\\pi f\\sqrt{1+(f')^2}\\,dx$", ha='center', fontsize=11,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: $ds=\\sqrt{1+(f\')^2}\\,dx$ corrects the slant — the #1 mistake')
    _scene_save(fig, '17b-surface-scene4.png')

    # Scene 5 — Where: integrate
    fig, ax = _scene_new('Scene 5 — Where: sum all bands', (-0.6, 4.7), (-2.8, 3.0))
    x = np.linspace(0, 4, 300)
    ax.fill_between(x, -np.sqrt(x), np.sqrt(x), color=GREEN, alpha=0.18)
    ax.plot(x, np.sqrt(x), BLUE, lw=2.4)
    ax.plot(x, -np.sqrt(x), BLUE, lw=1.2, alpha=0.6)
    ax.plot([-0.3, 4.5], [0, 0], '#333', lw=2.0)
    for xd in (0.6, 1.4, 2.2, 3.0, 3.8):
        r = np.sqrt(xd)
        ax.plot([xd, xd], [-r, r], RED, lw=1.1, alpha=0.75)
    ax.text(2.2, -2.1, '$S = 2\\pi\\int_0^4 \\sqrt{x}\\,\\sqrt{1+\\frac{1}{4x}}\\,dx$\n'
            '$= \\frac{\\pi}{6}(17^{3/2}-1) \\approx 36.18$',
            ha='center', fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: integrate every band over $x\\in[0,4]$ → $S=\\int dS$')
    _scene_save(fig, '17b-surface-scene5.png')

def sphere_surface_area():
    """Semicircle with a slant band element: S=2π∫(radius)(slant)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    R = 3
    th = np.linspace(0, np.pi, 800)
    x = R*np.cos(th); y = R*np.sin(th)
    ax.plot(x, y, BLUE, lw=2.6, label=r'$y=\sqrt{R^2-x^2}$')
    ax.plot(x, -y, BLUE, lw=1.4, alpha=0.4)
    # highlight a band at angle th0 with slant ds
    th0 = np.deg2rad(55)
    x0 = R*np.cos(th0); y0 = R*np.sin(th0)
    dth = np.deg2rad(9)
    ax.plot([R*np.cos(th0-dth), R*np.cos(th0+dth)], [R*np.sin(th0-dth), R*np.sin(th0+dth)],
            RED, lw=3.0)
    ax.annotate('band: radius $y$, slant $ds$\n$dS=2\\pi y\\,ds$', (x0, y0), xytext=(-2.6, 2.6),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.4))
    ax.text(0, -2.2, '$S=2\\pi\\int_{-R}^R y\\sqrt{1+(y\')^2}\\,dx = 4\\pi R^2$',
            ha='center', fontsize=12, color='#222', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-3.7, 3.7); ax.set_ylim(-3.4, 3.7)
    ax.set_aspect('equal')
    ax.set_title('Sphere surface: the slant factor cancels the shrinking radius',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '17B', '17b-sphere-surface-area.png')

def improper_scenes():
    """Improper integrals — 5 separate scene images (∫₁^∞ 1/x² dx → p-test)."""

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: the tail is infinite', (0.8, 5.2), (-0.15, 1.15))
    x = np.linspace(1, 5, 400)
    ax.plot(x, 1/x**2, BLUE, lw=2.5)
    ax.fill_between(x, 1/x**2, 0, color=BLUE, alpha=0.2)
    ax.annotate('the region runs forever →', (4.85, 0.55), xytext=(4.35, 0.95),
                fontsize=9.5, color='#222', fontweight='bold', ha='right')
    ax.text(3.0, 0.22, r'$\int_1^\infty \frac{1}{x^2}\,dx$', ha='center', fontsize=12,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHEN: the upper limit is ∞ — the "area" extends to infinity')
    _scene_save(fig, '17b-improper-scene1.png')

    # Scene 2 — How: cut at b
    fig, ax = _scene_new('Scene 2 — How: cut at a finite b', (0.8, 5.2), (-0.15, 1.15))
    x = np.linspace(1, 5, 400)
    ax.plot(x, 1/x**2, BLUE, lw=2.5)
    b = 3
    ax.fill_between(x[x <= b], 1/x[x <= b]**2, 0, color=BLUE, alpha=0.3)
    ax.plot([b, b], [0, 1/b**2], RED, lw=2.4)
    ax.text(b, 1/b**2 + 0.09, 'cut at $x=b$', fontsize=9.5, color=RED, fontweight='bold',
            ha='center')
    ax.text(3.9, 0.22, 'tail chopped off', fontsize=9.5, color='#888', fontweight='bold')
    _scene_caption(ax, 'HOW: replace ∞ by a finite b — compute the finite area first')
    _scene_save(fig, '17b-improper-scene2.png')

    # Scene 3 — How: evaluate
    fig, ax = _scene_new('Scene 3 — How: evaluate the finite integral', (-0.4, 4.6), (-0.5, 2.6))
    ax.text(2.1, 2.15, r'$\int_1^b \frac{1}{x^2}\,dx = \left[-\frac{1}{x}\right]_1^b = 1 - \frac{1}{b}$',
            ha='center', fontsize=12, color='#222', fontweight='bold')
    ax.text(2.1, 1.2, 'a finite number for every $b$', ha='center', fontsize=10.5,
            color='#555', fontweight='bold')
    _scene_caption(ax, 'HOW: evaluate normally — the answer is $1-1/b$')
    _scene_save(fig, '17b-improper-scene3.png')

    # Scene 4 — Where: take the limit
    fig, ax = _scene_new('Scene 4 — Where: let b→∞', (-0.4, 3.7), (-0.6, 2.9))
    bs = [2, 3, 5, 10]
    xs = np.arange(len(bs))
    vals = [1 - 1/b for b in bs]
    ax.plot(xs, vals, 'o-', color=BLUE, lw=2.2, ms=8)
    for i, (b, v) in enumerate(zip(bs, vals)):
        ax.annotate(f'$b={b}$: ${v:.3f}$', (i, v), xytext=(i - 0.15, v + 0.4),
                    fontsize=9.5, color='#222', fontweight='bold')
    ax.axhline(1, color=GREEN, lw=1.8, ls='--')
    ax.text(2.2, 1.15, r'$\lim_{b\to\infty}\left(1-\frac{1}{b}\right) = 1$', fontsize=11.5,
            color=GREEN, fontweight='bold')
    ax.set_xticks([])
    _scene_caption(ax, 'WHERE: as b→∞ the area approaches 1 — it CONVERGES')
    _scene_save(fig, '17b-improper-scene4.png')

    # Scene 5 — Where: the p-test
    fig, ax = _scene_new('Scene 5 — Where: the p-test', (0.8, 5.4), (-0.15, 1.15))
    x = np.linspace(1, 5, 400)
    ax.plot(x, 1/x**2, BLUE, lw=2.4, label=r'$p=2$: converges')
    ax.plot(x, 1/x, RED, lw=2.4, ls='--', label=r'$p=1$: diverges')
    ax.fill_between(x, 1/x**2, 0, color=BLUE, alpha=0.15)
    ax.legend(fontsize=9, loc='upper right')
    ax.text(3.1, 0.95, r'$\int_1^\infty \frac{1}{x^p}\,dx$' '\n' r'converges iff $p>1$',
            ha='center', fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: $p=2$ (decays fast) converges; $p=1$ (harmonic) diverges')
    _scene_save(fig, '17b-improper-scene5.png')

def gabriels_horn():
    """3D Gabriel's Horn: y=1/x rotated about x-axis on [1,6]."""
    fig = plt.figure(figsize=(8.5, 6))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(1, 6, 90)
    th = np.linspace(0, 2*np.pi, 60)
    X, TH = np.meshgrid(x, th)
    R = 1/X
    ax.plot_surface(X, R*np.cos(TH), R*np.sin(TH), color=AMBER, alpha=0.55, rstride=1, cstride=2)
    ax.plot([-0.4, 6.6], [0, 0], [0, 0], color='#333', lw=2.0)
    ax.text(6.6, 0, 0, '$x$', fontsize=12)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
    ax.set_title(r'Gabriel\'s Horn: $V=\pi$ finite, $S=\infty$', fontweight='bold')
    ax.view_init(elev=12, azim=-60)
    fig.tight_layout()
    save(fig, '17B', '17b-gabriels-horn.png')

def gaussian_scenes():
    """Gaussian integral — 5 separate scene images (the polar trick proof)."""

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: no elementary antiderivative', (-3.4, 3.4), (-0.2, 1.2))
    x = np.linspace(-3.2, 3.2, 600)
    ax.plot(x, np.exp(-x**2), BLUE, lw=2.5)
    ax.fill_between(x, np.exp(-x**2), 0, color=BLUE, alpha=0.2)
    ax.text(0, 0.62, r'$I=\int_{-\infty}^{\infty} e^{-x^2}\,dx$\n(no elementary antiderivative)',
            ha='center', fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, r'WHEN: we cannot find $\int e^{-x^2}dx$ — so SQUARE the integral')
    _scene_save(fig, '17b-gaussian-scene1.png')

    # Scene 2 — How: square it
    fig, ax = _scene_new('Scene 2 — How: square the integral', (-3.6, 3.6), (-3.6, 3.6))
    th = np.linspace(0, 2*np.pi, 400)
    for r in (0.5, 1.0, 1.5, 2.0, 2.5):
        ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=1.8, alpha=0.9 - 0.12*r)
    ax.text(0, 3.2, r'$I^2 = \iint_{\mathbb{R}^2} e^{-(x^2+y^2)}\,dx\,dy$',
            ha='center', fontsize=11, color='#222', fontweight='bold')
    ax.text(1.5, 1.15, r'$e^{-(x^2+y^2)}=e^{-r^2}$', fontsize=10, color='#222',
            fontweight='bold')
    _scene_caption(ax, 'HOW: I² = a double integral over the whole plane (a 2D bell)')
    _scene_save(fig, '17b-gaussian-scene2.png')

    # Scene 3 — How: polar
    fig, ax = _scene_new('Scene 3 — How: circular symmetry → polar', (-3.6, 3.6), (-3.6, 3.6))
    th = np.linspace(0, 2*np.pi, 400)
    for r in (0.5, 1.0, 1.5, 2.0, 2.5):
        ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=1.8, alpha=0.9 - 0.12*r)
    ax.annotate('', (0, 0), xytext=(1.6*np.cos(0.6), 1.6*np.sin(0.6)),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2.0))
    ax.text(1.8, 1.0, '$r$', fontsize=13, color=RED, fontweight='bold')
    ax.text(-3.4, 3.0, r'$I^2 = \int_0^{2\pi}\int_0^{\infty} e^{-r^2} r\,dr\,d\theta$',
            fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'HOW: the integrand depends only on r — switch to polar')
    _scene_save(fig, '17b-gaussian-scene3.png')

    # Scene 4 — Where: the area element
    fig, ax = _scene_new('Scene 4 — Where: why the extra r', (-0.4, 5.0), (-0.4, 3.4))
    th0 = np.deg2rad(25); dth = np.deg2rad(22); r1, r2 = 1.6, 2.7
    ths = np.linspace(th0, th0 + dth, 40)
    ax.fill(np.concatenate([r1*np.cos(ths), r2*np.cos(ths[::-1])]),
            np.concatenate([r1*np.sin(ths), r2*np.sin(ths[::-1])]),
            color=GREEN, alpha=0.35, edgecolor=GREEN, lw=2.0)
    ax.annotate('', (r1*np.cos(th0), r1*np.sin(th0)), xytext=(r2*np.cos(th0), r2*np.sin(th0)),
                arrowprops=dict(arrowstyle='->', color='#222', lw=1.6))
    ax.annotate('', (r1*np.cos(th0 + dth), r1*np.sin(th0 + dth)),
                xytext=(r1*np.cos(th0), r1*np.sin(th0)),
                arrowprops=dict(arrowstyle='->', color='#222', lw=1.6))
    ax.text(2.55, 0.55, '$dr$', fontsize=11, color='#222', fontweight='bold')
    ax.text(1.05, 1.1, r'$r\,d\theta$', fontsize=11, color='#222', fontweight='bold')
    ax.text(2.6, 2.75, r'area $\approx r\,dr\,d\theta$', fontsize=11, color='#222',
            fontweight='bold')
    ax.text(2.6, 1.9, 'outer cells are WIDER\nby the factor $r$', fontsize=9.5,
            color='#555', fontweight='bold')
    _scene_caption(ax, r'WHERE: $dx\,dy = r\,dr\,d\theta$ — wider far from the origin')
    _scene_save(fig, '17b-gaussian-scene4.png')

    # Scene 5 — Where: evaluate
    fig, ax = _scene_new('Scene 5 — Where: evaluate', (-3.4, 3.4), (-0.3, 1.5))
    x = np.linspace(-3.2, 3.2, 600)
    ax.plot(x, np.exp(-x**2), BLUE, lw=2.5)
    ax.fill_between(x, np.exp(-x**2), 0, color=BLUE, alpha=0.2)
    ax.text(0, 0.85, r'$I^2 = 2\pi\int_0^{\infty} r e^{-r^2}\,dr = 2\pi\cdot\frac{1}{2} = \pi$\n$I = \sqrt{\pi}$',
            ha='center', fontsize=10.5, color='#222', fontweight='bold')
    _scene_caption(ax, r'WHERE: $\int_0^{\infty} r e^{-r^2}dr = \frac{1}{2}$ → $I=\sqrt{\pi}$')
    _scene_save(fig, '17b-gaussian-scene5.png')

def cardioid_arc_length():
    """Cardioid r=1+cosθ with arc length L=8 (Practice 3)."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 1000)
    r = 1 + np.cos(th)
    ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=2.6)
    ax.text(0.0, 0.0, '$L=\\int_0^{2\\pi}\\sqrt{(r\')^2+r^2}\\,d\\theta$\n$=\\int_0^{2\\pi}2|\\cos(\\theta/2)|\\,d\\theta=8$',
            ha='center', va='center', fontsize=12, color='#222', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-2.3, 2.3); ax.set_ylim(-2.3, 2.3)
    ax.set_aspect('equal')
    ax.set_title(r'Cardioid $r=1+\cos\theta$ — arc length $=8$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '17B', '17b-cardioid-arc-length.png')

if __name__ == '__main__':
    for fn in (arc_length_scenes, helix_3d, spiral_arc_length, cycloid, conical_spiral,
               surface_area_scenes, sphere_surface_area, improper_scenes, gabriels_horn,
               gaussian_scenes, cardioid_arc_length):
        fn()
        print('done:', fn.__name__)
    print('All 17B session graphs written under', BASE)
