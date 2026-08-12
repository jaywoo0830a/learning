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

# ───────────────────────── 17B ─────────────────────────

def arc_length_pythagoras():
    """Curve with inscribed segments; one highlighted Pythagorean right triangle."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0, 2*np.pi, 800)
    y = 1.2*np.sin(x) + 0.4*x
    ax.plot(x, y, BLUE, lw=2.5, label='curve')
    # polyline segments
    ts = np.linspace(0, 2*np.pi, 9)
    pts = np.array([ts, 1.2*np.sin(ts) + 0.4*ts]).T
    ax.plot(pts[:, 0], pts[:, 1], color='#888', lw=1.4, ls='--', label='segments')
    # highlight one segment with right triangle (between points 3 and 4)
    P = pts[3]; Q = pts[4]
    ax.plot([P[0], Q[0]], [P[1], Q[1]], RED, lw=2.6)
    # right triangle: horizontal from P, vertical to Q
    ax.plot([P[0], Q[0]], [P[1], P[1]], color=GREEN, lw=1.6, ls=':')
    ax.plot([Q[0], Q[0]], [P[1], Q[1]], color=GREEN, lw=1.6, ls=':')
    ax.annotate('$\\Delta x$', ((P[0]+Q[0])/2, P[1]-0.28), ha='center', fontsize=10,
                color=GREEN, fontweight='bold')
    ax.annotate('$\\Delta y$', (Q[0]+0.12, (P[1]+Q[1])/2), va='center', fontsize=10,
                color=GREEN, fontweight='bold')
    ax.annotate('$\\Delta L=\\sqrt{\\Delta x^2+\\Delta y^2}$', ((P[0]+Q[0])/2, (P[1]+Q[1])/2 + 0.25),
                ha='center', fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-0.6, 4.4)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['$0$', '$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    ax.set_title('Arc length: sum of $\\sqrt{\\Delta x^2+\\Delta y^2}$ as segments shrink to zero',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '17B', '17b-arc-length-pythagoras.png')

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

def surface_revolution():
    """3D surface: y=√x rotated about x-axis (Example 6), S≈36.18."""
    fig = plt.figure(figsize=(8.5, 6.5))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, 4, 80)
    th = np.linspace(0, 2*np.pi, 80)
    X, TH = np.meshgrid(x, th)
    R = np.sqrt(X)
    ax.plot_surface(X, R*np.cos(TH), R*np.sin(TH), color=GREEN, alpha=0.5, rstride=2, cstride=2)
    ax.plot([-0.5, 4.5], [0, 0], [0, 0], color='#333', lw=2.0)
    ax.text(4.5, 0, 0, '$x$', fontsize=12)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
    ax.set_title(r'$y=\sqrt{x}$ rotated about the $x$-axis — $S=\frac{\pi}{6}(17^{3/2}-1)\approx36.18$',
                 fontweight='bold')
    ax.view_init(elev=18, azim=-60)
    fig.tight_layout()
    save(fig, '17B', '17b-surface-revolution.png')

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

def p_test():
    """p-test: two panels — ∫₁∞ (p>1 vs p≤1) and ∫₀¹ (p<1 vs p≥1)."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    # left: at infinity
    ax = axes[0]; g(ax)
    x = np.linspace(1, 5, 600)
    ax.plot(x, 1/x**2, BLUE, lw=2.4, label=r'$1/x^2$ ($p=2$, converges)')
    ax.plot(x, 1/x, RED, lw=2.4, ls='--', label=r'$1/x$ ($p=1$, diverges)')
    xs = np.linspace(1, 5, 300)
    ax.fill_between(xs, 1/xs**2, 0, color=BLUE, alpha=0.2)
    ax.annotate(r'$\int_1^\infty x^{-2}dx = 1$', (3.1, 0.16), fontsize=10,
                color=BLUE, fontweight='bold')
    ax.annotate(r'$\int_1^\infty x^{-1}dx = \infty$', (1.4, 0.75), fontsize=10,
                color=RED, fontweight='bold')
    ax.set_xlim(1, 5); ax.set_ylim(0, 1.1)
    ax.set_title(r'$\int_1^\infty 1/x^p\,dx$: converges iff $p>1$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=8, loc='upper right')
    # right: at 0
    ax = axes[1]; g(ax)
    x = np.linspace(0.01, 1, 600)
    ax.plot(x, 1/np.sqrt(x), BLUE, lw=2.4, label=r'$1/\sqrt{x}$ ($p=1/2$, converges)')
    ax.plot(x, 1/x**2, RED, lw=2.4, ls='--', label=r'$1/x^2$ ($p=2$, diverges)')
    xs = np.linspace(0.01, 1, 300)
    ax.fill_between(xs, 1/np.sqrt(xs), 0, color=BLUE, alpha=0.2)
    ax.annotate(r'$\int_0^1 x^{-1/2}dx = 2$', (0.35, 2.6), fontsize=10,
                color=BLUE, fontweight='bold')
    ax.annotate(r'$\int_0^1 x^{-2}dx = \infty$', (0.62, 3.4), fontsize=10,
                color=RED, fontweight='bold')
    ax.set_xlim(0, 1); ax.set_ylim(0, 4.6)
    ax.set_title(r'$\int_0^1 1/x^p\,dx$: converges iff $p<1$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=8, loc='upper right')
    fig.suptitle('The $p$-test: at infinity $p>1$ converges; at a singularity $p<1$ converges',
                 fontweight='bold', fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    save(fig, '17B', '17b-p-test.png')

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

def gaussian_integral():
    """Gaussian bell e^{-x^2} with shaded area = √π."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    x = np.linspace(-3.2, 3.2, 800)
    y = np.exp(-x**2)
    ax.plot(x, y, BLUE, lw=2.6, label=r'$y=e^{-x^2}$')
    ax.fill_between(x, y, 0, color=BLUE, alpha=0.2)
    ax.annotate(r'$\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi} \approx 1.772$',
                (0, 0.55), xytext=(-2.9, 0.9), fontsize=12, color='#222',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#222', lw=1.4))
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-3.2, 3.2); ax.set_ylim(-0.08, 1.25)
    ax.set_title('The Gaussian integral — proved by squaring and going polar',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper right')
    fig.tight_layout()
    save(fig, '17B', '17b-gaussian-integral.png')

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
    for fn in (arc_length_pythagoras, helix_3d, spiral_arc_length, cycloid, conical_spiral,
               surface_revolution, sphere_surface_area, p_test, gabriels_horn,
               gaussian_integral, cardioid_arc_length):
        fn()
        print('done:', fn.__name__)
    print('All 17B session graphs written under', BASE)
