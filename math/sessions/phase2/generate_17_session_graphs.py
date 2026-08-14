#!/usr/bin/env python3
"""Generate/regenerate the session graphs for 17A (same pattern as 13X/14X).

Outputs into graphs/0808/17A.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, FancyArrowPatch
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0808')
os.makedirs(os.path.join(BASE, '17A'), exist_ok=True)

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

# ───────────────────────── 17A ─────────────────────────

def area_between_curves():
    """Area between y=x and y=x^2 on [0,1]: A = 1/6."""
    fig, ax = plt.subplots(figsize=(8, 5.2)); g(ax)
    x = np.linspace(-0.1, 1.15, 400)
    ax.plot(x, x, BLUE, lw=2.5, label=r'$y=x$')
    ax.plot(x, x**2, RED, lw=2.5, label=r'$y=x^2$')
    xs = np.linspace(0, 1, 300)
    ax.fill_between(xs, xs, xs**2, color=GREEN, alpha=0.35)
    ax.plot([0, 1], [0, 0], 'o', color='#333', ms=6, zorder=6)
    ax.text(0.5, 0.30, 'area $= \\int_0^1 (x-x^2)\\,dx = \\frac{1}{6}$',
            ha='center', fontsize=12, color=GREEN, fontweight='bold')
    ax.set_xlim(-0.1, 1.15); ax.set_ylim(-0.1, 1.15)
    ax.set_aspect('equal')
    ax.set_title('Area between curves: $\\int$ (top $-$ bottom), intersections are the bounds',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=10, loc='upper left')
    fig.tight_layout()
    save(fig, '17A', '17a-area-between-curves.png')

def polar_rose():
    """r = sin(2θ): 4-petal rose, one petal [0, π/2] shaded, A = π/8."""
    fig, ax = plt.subplots(figsize=(7.4, 7.4)); g(ax)
    th = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(2*th)
    ax.plot(r*np.cos(th), r*np.sin(th), BLUE, lw=2.6)
    # shade one petal
    thp = np.linspace(0, np.pi/2, 300)
    rp = np.sin(2*thp)
    ax.fill(rp*np.cos(thp), rp*np.sin(thp), color=GREEN, alpha=0.4)
    ax.annotate('one petal: $\\theta\\in[0,\\pi/2]$\n$A=\\frac{1}{2}\\int_0^{\\pi/2}\\sin^2 2\\theta\\,d\\theta=\\frac{\\pi}{8}$',
                (0.35, 0.5), xytext=(0.42, 0.72), fontsize=10.5, color=GREEN,
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.4))
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25)
    ax.set_aspect('equal')
    ax.set_title(r'$r=\sin(2\theta)$ — four petals, one petal has area $\pi/8$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '17A', '17a-polar-rose.png')

def parametric_ellipse():
    """Ellipse x=3cos t, y=2sin t; upper half shaded; A = πab = 6π."""
    fig, ax = plt.subplots(figsize=(8, 5.4)); g(ax)
    t = np.linspace(0, 2*np.pi, 800)
    ax.plot(3*np.cos(t), 2*np.sin(t), BLUE, lw=2.6, label=r'$x=3\cos t,\ y=2\sin t$')
    tu = np.linspace(0, np.pi, 300)
    ax.fill_between(3*np.cos(tu), 0, 2*np.sin(tu), color=GREEN, alpha=0.35)
    ax.annotate('upper half: $t\\in[0,\\pi]$\n$A=\\int_0^\\pi y(t)\\,x\'(t)\\,dt$\n$=\\pi ab=6\\pi$',
                (0.4, 0.6), xytext=(-2.9, 0.9), fontsize=10.5, color=GREEN,
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.4))
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-3.6, 3.6); ax.set_ylim(-2.4, 2.9)
    ax.set_aspect('equal')
    ax.set_title('Parametric area: $\\int y(t)\\,x\'(t)\\,dt$ — ellipse area $=\\pi ab$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower left')
    fig.tight_layout()
    save(fig, '17A', '17a-parametric-ellipse.png')

def triangle_cross_product():
    """3D triangle A(1,0,2), B(4,1,6), C(2,5,0) with AB×AC = (-22,10,14)."""
    fig = plt.figure(figsize=(8.5, 6.5))
    ax = fig.add_subplot(111, projection='3d')
    A = np.array([1, 0, 2]); B = np.array([4, 1, 6]); C = np.array([2, 5, 0])
    AB = B - A; AC = C - A
    n = np.cross(AB, AC)  # (-22, 10, 14)
    for P, name, col in [(A, 'A', BLUE), (B, 'B', RED), (C, 'C', GREEN)]:
        ax.plot([P[0]], [P[1]], [P[2]], 'o', color=col, ms=8, zorder=6)
        ax.text(P[0], P[1], P[2], '  ' + name, fontsize=13, color=col, fontweight='bold')
    # triangle edges
    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], tri[:, 2], color='#333', lw=2.0)
    # cross product vector from A
    ax.quiver(A[0], A[1], A[2], n[0], n[1], n[2], color=AMBER, lw=2.5, arrow_length_ratio=0.12)
    mid = (A + B + C)/3
    ax.text(mid[0] + n[0]*0.25, mid[1] + n[1]*0.25, mid[2] + n[2]*0.25,
            r'$\vec{AB}\times\vec{AC}=(-22,10,14)$', fontsize=10, color=AMBER, fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('Triangle area $= \\frac{1}{2}|\\vec{AB}\\times\\vec{AC}| = \\sqrt{195}$',
                 fontweight='bold')
    ax.view_init(elev=20, azim=-60)
    fig.tight_layout()
    save(fig, '17A', '17a-triangle-cross-product.png')

def _method_card_ax():
    """A clean axes for one method comparison card."""
    fig, ax = plt.subplots(figsize=(5.8, 4.4))
    g(ax); ax.set_xticks([]); ax.set_yticks([])
    for s in ('top', 'right'):
        ax.spines[s].set_visible(True); ax.spines[s].set_color('#ccc')
    return fig, ax

def volume_method_disk():
    """Disk method comparison card: V = π∫R² dx (region touches the axis)."""
    fig, ax = _method_card_ax()
    ax.add_patch(Rectangle((0.2, 0.15), 2.6, 0.05, color='#333'))
    xs = np.linspace(0.25, 2.75, 100)
    ax.fill_between(xs, 0.2, 0.2 + 1.5*np.sin((xs-0.25)/2.5*np.pi), color=BLUE, alpha=0.25)
    ax.plot(xs, 0.2 + 1.5*np.sin((xs-0.25)/2.5*np.pi), BLUE, lw=2.2)
    ax.add_patch(Circle((1.5, 0.2), 1.2, fill=True, facecolor=RED, alpha=0.3,
                        edgecolor=RED, lw=2.0))
    ax.annotate('', (2.7, 0.2), xytext=(2.7, 1.4),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.4))
    ax.text(1.5, -0.28, '$V=\\pi\\int R^2\\,dx$', ha='center', fontsize=11,
            color='#222', fontweight='bold')
    ax.text(1.5, 1.78, '$R=f(x)$', ha='center', fontsize=11, color=RED, fontweight='bold')
    ax.text(1.5, -0.55, 'when: region touches the axis (no hole)',
            ha='center', fontsize=9, color='#555', fontweight='bold')
    ax.set_title('Disk', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 3); ax.set_ylim(-0.7, 2.1)
    fig.tight_layout()
    save(fig, '17A', '17a-volume-method-disk.png')

def volume_method_washer():
    """Washer method comparison card: V = π∫(R²−r²) dx (hole appears)."""
    fig, ax = _method_card_ax()
    ax.add_patch(Rectangle((0.2, 0.15), 2.6, 0.05, color='#333'))
    ax.add_patch(Circle((1.5, 0.2), 1.3, fill=True, facecolor=RED, alpha=0.3,
                        edgecolor=RED, lw=2.0))
    ax.add_patch(Circle((1.5, 0.2), 0.6, fill=True, facecolor='white', edgecolor=GREEN,
                        lw=2.0))
    ax.annotate('', (1.5, 1.5), xytext=(1.5, 0.85),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.4))
    ax.text(1.5, -0.28, '$V=\\pi\\int(R^2-r^2)\\,dx$', ha='center', fontsize=11,
            color='#222', fontweight='bold')
    ax.text(2.25, 1.15, '$R$', fontsize=11, color=RED, fontweight='bold')
    ax.text(1.05, 0.62, '$r$', fontsize=11, color=GREEN, fontweight='bold')
    ax.text(1.5, -0.55, 'when: axis outside the region (hole appears)',
            ha='center', fontsize=9, color='#555', fontweight='bold')
    ax.set_title('Washer', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 3); ax.set_ylim(-0.7, 2.1)
    fig.tight_layout()
    save(fig, '17A', '17a-volume-method-washer.png')

def volume_method_shell():
    """Shell method comparison card: V = 2π∫ x·h(x) dx (slice parallel to axis)."""
    fig, ax = _method_card_ax()
    ax.add_patch(Rectangle((0.15, 0.2), 0.05, 2.6, color='#333'))
    xs = np.linspace(0.3, 2.9, 100)
    ax.fill_between(xs, 0.25, 0.25 + 1.3*np.sin((xs-0.3)/2.6*np.pi), color=BLUE, alpha=0.25)
    ax.plot(xs, 0.25 + 1.3*np.sin((xs-0.3)/2.6*np.pi), BLUE, lw=2.2)
    ax.add_patch(Rectangle((1.5, 0.25), 0.08, 1.2, facecolor=RED, alpha=0.55,
                           edgecolor=RED, lw=1.6))
    ax.add_patch(Circle((0, 1.6), 1.5, fill=False, edgecolor=AMBER, lw=1.6, ls='--'))
    ax.annotate('', (0.3, 1.15), xytext=(0.15, 1.15),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.4))
    ax.text(1.5, -0.28, '$V=2\\pi\\int x\\,h(x)\\,dx$', ha='center', fontsize=11,
            color='#222', fontweight='bold')
    ax.text(1.7, 1.0, '$h(x)$', fontsize=11, color=RED, fontweight='bold')
    ax.text(1.5, -0.55, 'when: slice runs parallel to the axis',
            ha='center', fontsize=9, color='#555', fontweight='bold')
    ax.set_title('Shell', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 3); ax.set_ylim(-0.7, 2.1)
    fig.tight_layout()
    save(fig, '17A', '17a-volume-method-shell.png')

def washer_shifted_axis():
    """Region between y=√x and y=x² on [0,1] rotated about y=2."""
    fig, ax = plt.subplots(figsize=(8, 6)); g(ax)
    x = np.linspace(0, 1.05, 400)
    ax.plot(x, np.sqrt(x), BLUE, lw=2.5, label=r'$y=\sqrt{x}$')
    ax.plot(x, x**2, RED, lw=2.5, label=r'$y=x^2$')
    xs = np.linspace(0, 1, 200)
    ax.fill_between(xs, xs**2, np.sqrt(xs), color=GREEN, alpha=0.3)
    ax.axhline(2, color='#333', lw=2.0, ls='--', label='axis $y=2$')
    # radii at x=0.6
    xr = 0.6
    ax.plot([xr, xr], [xr**2, 2], color=RED, lw=1.8)
    ax.plot([xr, xr], [np.sqrt(xr), 2], color=BLUE, lw=1.8)
    ax.annotate('$R_{\\text{outer}}=2-x^2$', (xr, 2), xytext=(0.62, 2.45), fontsize=10,
                color=RED, fontweight='bold')
    ax.annotate('$R_{\\text{inner}}=2-\\sqrt{x}$', (xr, np.sqrt(xr)), xytext=(0.62, 1.05),
                fontsize=10, color=BLUE, fontweight='bold')
    ax.text(0.5, 0.42, 'region', fontsize=11, color=GREEN, fontweight='bold')
    ax.set_xlim(-0.05, 1.15); ax.set_ylim(-0.15, 2.7)
    ax.set_title('Washer about a shifted axis: radii are distances $|c-f(x)|$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '17A', '17a-washer-shifted-axis.png')

def sphere_volume():
    """Semicircle y=√(R²-x²) rotated about x-axis → sphere, V=4/3πR³."""
    fig, ax = plt.subplots(figsize=(8.5, 5)); g(ax)
    R = 3
    x = np.linspace(-R, R, 800)
    y = np.sqrt(R**2 - x**2)
    ax.plot(x, y, BLUE, lw=2.6, label=r'$y=\sqrt{R^2-x^2}$')
    ax.fill_between(x, 0, y, color=BLUE, alpha=0.18)
    ax.plot(x, -y, BLUE, lw=1.4, alpha=0.4)
    # representative disk at x=1
    xd = 1.0
    rd = np.sqrt(R**2 - xd**2)
    ax.add_patch(Ellipse((xd, 0), 0.18, 2*rd, facecolor=RED, alpha=0.35, edgecolor=RED, lw=1.6))
    ax.plot([xd, xd], [-rd, rd], color=RED, lw=1.2, ls=':')
    ax.annotate('disk at $x$: radius $R=\\sqrt{R^2-x^2}$', (xd, 0), xytext=(-2.95, 1.6),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.4))
    ax.annotate('', (0, -3.2), xytext=(0, -2.1),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))
    ax.text(0.35, -3.35, 'rotate about x-axis', fontsize=9.5, color='#333', fontweight='bold')
    ax.axhline(0, color='#888', lw=0.8, alpha=0.5); ax.axvline(0, color='#888', lw=0.8, alpha=0.5)
    ax.set_xlim(-3.7, 3.7); ax.set_ylim(-3.7, 3.4)
    ax.set_aspect('equal')
    ax.set_title('$V=\\pi\\int_{-R}^{R}(R^2-x^2)\\,dx=\\frac{4}{3}\\pi R^3$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '17A', '17a-sphere-volume.png')

def torus():
    """Circle (x-R)²+y²=r² rotated about the y-axis → torus V=2π²Rr²."""
    fig, ax = plt.subplots(figsize=(8, 6)); g(ax)
    R, r = 3.0, 1.0
    th = np.linspace(0, 2*np.pi, 800)
    ax.plot(R + r*np.cos(th), r*np.sin(th), BLUE, lw=2.6, label=r'$(x-R)^2+y^2=r^2$')
    # rotation axis = y-axis
    ax.axvline(0, color='#333', lw=1.8, ls='--', label='rotation axis (y-axis)')
    # centroid path
    ax.add_patch(Circle((0, 0), R, fill=False, edgecolor=AMBER, lw=1.6, ls=':'))
    # radius labels
    ax.annotate('', (3.0, 0.0), xytext=(0.0, 0.0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.8))
    ax.text(1.5, -0.28, '$R$', fontsize=11, color=GREEN, fontweight='bold')
    ax.annotate('', (2.6, 0.0), xytext=(3.0, 0.0),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.6))
    ax.text(2.55, -0.5, '$r$', fontsize=11, color=RED, fontweight='bold')
    # rotation arrow
    ax.annotate('', (0.2, 3.3), xytext=(1.3, 3.3),
                arrowprops=dict(arrowstyle='->', color='#333', lw=1.8))
    ax.text(0.75, 3.5, 'rotate', fontsize=10, color='#333', fontweight='bold')
    ax.set_xlim(-4.4, 4.6); ax.set_ylim(-4.4, 4.2)
    ax.set_aspect('equal')
    ax.set_title('Torus: $V=(\\pi r^2)(2\\pi R)=2\\pi^2 R r^2$ (Pappus)', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '17A', '17a-torus.png')

def determinant_area():
    """Unit square → 3×2 rectangle under M=[[3,0],[0,2]]; det = area factor = 6."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    # original unit square
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    ax.plot(sq[:, 0], sq[:, 1], BLUE, lw=2.4, label='unit square (area 1)')
    ax.fill(sq[:, 0], sq[:, 1], color=BLUE, alpha=0.15)
    # image rectangle 3×2
    rect = np.array([[0, 0], [3, 0], [3, 2], [0, 2], [0, 0]])
    ax.plot(rect[:, 0], rect[:, 1], RED, lw=2.4, label='image (area 6)')
    ax.fill(rect[:, 0], rect[:, 1], color=RED, alpha=0.15)
    for (x1, y1), (x2, y2) in [((0.5, 0.5), (1.5, 1.0)), ((1, 0), (3, 0))]:
        ax.annotate('', (x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#333', lw=1.6))
    ax.text(1.5, 1.0, '$M = [[3,0],[0,2]]$  (det $= 6$)', fontsize=11,
            color='#333', fontweight='bold', ha='center', va='center')
    ax.text(1.5, 3.6, 'area $\\times |\\det M| = 1 \\times 6 = 6$', ha='center', fontsize=12,
            color=RED, fontweight='bold')
    ax.set_xlim(-0.4, 3.6); ax.set_ylim(-0.4, 3.0)
    ax.set_aspect('equal')
    ax.set_title('The determinant is the area scaling factor of a linear map',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='lower right')
    fig.tight_layout()
    save(fig, '17A', '17a-determinant-area.png')

def cross_section_volume():
    """Base between y=x^2 and y=1; equilateral-triangle cross-sections ⟂ y-axis."""
    fig, ax = plt.subplots(figsize=(8.5, 5.4)); g(ax)
    y = np.linspace(0, 1, 400)
    ax.plot(np.sqrt(y), y, BLUE, lw=2.4, label=r'$y=x^2$')
    ax.plot(-np.sqrt(y), y, BLUE, lw=2.4)
    ax.axhline(1, color='#888', lw=1.0, ls='--')
    ax.fill_betweenx(y, -np.sqrt(y), np.sqrt(y), color=BLUE, alpha=0.12)
    # equilateral triangle cross-section at y=0.6
    yc = 0.6
    s = 2*np.sqrt(yc)
    tri_y = np.array([yc, yc, yc + np.sqrt(3)*np.sqrt(yc), yc])
    tri_x = np.array([-np.sqrt(yc), np.sqrt(yc), 0, -np.sqrt(yc)])
    ax.fill(tri_x, tri_y, color=RED, alpha=0.4)
    ax.plot(tri_x, tri_y, RED, lw=2.2)
    ax.annotate('at height $y$: side $s=2\\sqrt{y}$\n$A_{\\triangle}=\\frac{\\sqrt{3}}{4}s^2=\\sqrt{3}\\,y$',
                (0, yc), xytext=(0.6, 0.75), fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.4))
    ax.text(0, 0.12, '$V=\\int_0^1 \\sqrt{3}\\,y\\,dy=\\frac{\\sqrt{3}}{2}$',
            ha='center', fontsize=12, color='#222', fontweight='bold')
    ax.set_xlim(-1.3, 1.6); ax.set_ylim(-0.15, 1.65)
    ax.set_title('Volume by cross-sections: $V=\\int A(y)\\,dy$ for any shape',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper right')
    fig.tight_layout()
    save(fig, '17A', '17a-cross-section-volume.png')

def inverse_curves():
    """Area between y=e^x and y=ln x on [0,1]: A = e (improper at x=0)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.2)); g(ax)
    x = np.linspace(0.02, 1, 600)
    ax.plot(x, np.exp(x), BLUE, lw=2.5, label=r'$y=e^x$')
    ax.plot(x, np.log(x), RED, lw=2.5, label=r'$y=\ln x$')
    xd = np.linspace(-0.2, 1.1, 100)
    ax.plot(xd, xd, color='#888', lw=1.2, ls='--', label='$y=x$')
    ax.fill_between(x, np.log(x), np.exp(x), color=GREEN, alpha=0.3)
    ax.annotate('area $= \\int_0^1 (e^x-\\ln x)\\,dx = e$\n(improper at $x=0$: $x\\ln x\\to 0$)',
                (0.5, 0.5), xytext=(0.12, 0.35), fontsize=10, color=GREEN, fontweight='bold')
    ax.set_xlim(-0.2, 1.15); ax.set_ylim(-3.0, 3.2)
    ax.set_title('Inverse curves: the lens between $e^x$ and $\\ln x$ on $[0,1]$ has area $e$',
                 fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=9, loc='upper left')
    fig.tight_layout()
    save(fig, '17A', '17a-inverse-curves.png')

def solid_revolution():
    """3D: y=sqrt(x) rotated about the x-axis (Example 6), one disk highlighted."""
    fig = plt.figure(figsize=(8.5, 6.5))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, 4, 80)
    th = np.linspace(0, 2*np.pi, 80)
    X, TH = np.meshgrid(x, th)
    R = np.sqrt(X)
    Y = R*np.cos(TH)
    Z = R*np.sin(TH)
    ax.plot_surface(X, Y, Z, color=BLUE, alpha=0.55, rstride=2, cstride=2)
    t = np.linspace(0, 2*np.pi, 100)
    r2 = np.sqrt(2)
    ax.plot([2]*100, r2*np.cos(t), r2*np.sin(t), color=RED, lw=2.0)
    ax.plot([-0.5, 4.5], [0, 0], [0, 0], color='#333', lw=2.0)
    ax.text(4.5, 0, 0, '$x$', fontsize=12)
    ax.text(1.1, 1.6, 1.6, 'disk at $x=2$: radius $\\sqrt{2}$', fontsize=10,
            color=RED, fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
    ax.set_title(r'$y=\sqrt{x}$ rotated about the $x$-axis — slices are disks $\pi(\sqrt{x})^2\,dx$',
                 fontweight='bold')
    ax.view_init(elev=20, azim=-60)
    fig.tight_layout()
    save(fig, '17A', '17a-solid-revolution.png')

def solid_revolution_dy():
    """3D: y=x^2 rotated about the y-axis (Example 6A), one disk with dy highlighted."""
    fig = plt.figure(figsize=(8.5, 6.5))
    ax = fig.add_subplot(111, projection='3d')
    y = np.linspace(0, 4, 80)
    th = np.linspace(0, 2*np.pi, 80)
    Y, TH = np.meshgrid(y, th)
    R = np.sqrt(Y)
    X = R*np.cos(TH)
    Z = R*np.sin(TH)
    ax.plot_surface(X, Y, Z, color=GREEN, alpha=0.55, rstride=2, cstride=2)
    t = np.linspace(0, 2*np.pi, 100)
    r2 = np.sqrt(2)
    ax.plot(r2*np.cos(t), [2]*100, r2*np.sin(t), color=RED, lw=2.0)
    ax.plot([0, 0], [-0.5, 4.5], [0, 0], color='#333', lw=2.0)
    ax.text(0, 4.5, 0, '$y$', fontsize=12)
    ax.text(2.2, 3.4, 0.8, 'disk at $y=2$: radius $\\sqrt{2}$', fontsize=10,
            color=RED, fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); ax.set_zlabel('$z$')
    ax.set_title(r'$y=x^2$ rotated about the $y$-axis — disk method with $dy$',
                 fontweight='bold')
    ax.view_init(elev=20, azim=-60)
    fig.tight_layout()
    save(fig, '17A', '17a-solid-revolution-dy.png')

# ─────────────────────── 5-scene walkthroughs ───────────────────────
# Each scene is its OWN image (17a-<method>-sceneN.png), shown separately in
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
    save(fig, '17A', name)

def _disk3d(ax, cx, cy, R, dx, color, lw=2.0, alpha=0.35, foreshort=0.42):
    """A short cylinder (disk) seen in perspective: front+back ellipses + edges."""
    h = R * foreshort
    back = Ellipse((cx - dx, cy), 2*R, 2*h, facecolor=color, alpha=alpha*0.45,
                   edgecolor=color, lw=lw*0.7)
    front = Ellipse((cx, cy), 2*R, 2*h, facecolor=color, alpha=alpha, edgecolor=color, lw=lw)
    ax.add_patch(back); ax.add_patch(front)
    ax.plot([cx - dx, cx], [cy + h, cy + h], color, lw=lw*0.8)
    ax.plot([cx - dx, cx], [cy - h, cy - h], color, lw=lw*0.8)

def disk_scenes():
    """Disk method — 5 separate scene images. Rotate y=√x about the x-axis, x∈[0,4]."""

    def curve(ax):
        x = np.linspace(0, 4, 300)
        ax.plot(x, np.sqrt(x), BLUE, lw=2.4)
        ax.fill_between(x, 0, np.sqrt(x), color=BLUE, alpha=0.16)
        ax.plot([-0.2, 4.35], [0, 0], '#333', lw=2.0)
        ax.text(4.45, 0.15, 'axis', fontsize=9, color='#333')

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: setup', (-0.5, 4.7), (-0.7, 2.7))
    curve(ax)
    ax.text(2.2, 2.3, 'Region sits ON the axis →\nno hole → solid disk',
            ha='center', fontsize=10, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHEN: the region touches the rotation axis (no hole)')
    _scene_save(fig, '17a-disk-scene1.png')

    # Scene 2 — How: slice
    fig, ax = _scene_new('Scene 2 — How: cut a slice', (-0.5, 4.7), (-0.7, 3.1))
    curve(ax)
    ax.add_patch(Rectangle((2.0, 0), 0.3, np.sqrt(2), facecolor=RED, alpha=0.6,
                           edgecolor=RED, lw=1.6))
    ax.annotate('width $dx$', (2.15, 0.08), xytext=(2.6, 0.7), fontsize=9.5, color=RED,
                fontweight='bold', arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.annotate('height $\\sqrt{x}$', (2.15, np.sqrt(2)), xytext=(2.85, 2.15), fontsize=9.5,
                color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    _scene_caption(ax, 'HOW: slice ⟂ to the axis — thickness $dx$, height $\\sqrt{x}$')
    _scene_save(fig, '17a-disk-scene2.png')

    # Scene 3 — How: rotate
    fig, ax = _scene_new('Scene 3 — How: rotate the slice', (0.3, 4.9), (-1.5, 2.3))
    _disk3d(ax, 2.55, 0.3, np.sqrt(2), 0.4, RED)
    ax.plot([2.55, 2.55 + np.sqrt(2)], [0.3, 0.3], '#333', lw=1.4)
    ax.text(2.55 + np.sqrt(2)/2, 0.04, '$R=\\sqrt{x}$', fontsize=11, color='#222',
            fontweight='bold', ha='center')
    _scene_caption(ax, 'HOW: the strip sweeps a disk — radius $R=\\sqrt{x}$, thickness $dx$')
    _scene_save(fig, '17a-disk-scene3.png')

    # Scene 4 — Where: one disk
    fig, ax = _scene_new('Scene 4 — Where: volume of ONE disk', (0.3, 4.9), (-1.9, 2.3))
    _disk3d(ax, 2.55, 0.5, np.sqrt(2), 0.4, GREEN)
    ax.plot([2.55, 2.55 + np.sqrt(2)], [0.5, 0.5], '#333', lw=1.4)
    ax.text(2.55 + np.sqrt(2)/2, 0.22, '$R$', fontsize=11, color='#222', fontweight='bold',
            ha='center')
    ax.text(2.55, -0.75, '$dV = \\pi R^2\\,dx = \\pi(\\sqrt{x})^2\\,dx = \\pi x\\,dx$',
            ha='center', fontsize=10, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: one disk = (face area $\\pi R^2$) × thickness $dx$')
    _scene_save(fig, '17a-disk-scene4.png')

    # Scene 5 — Where: stack + integrate
    fig, ax = _scene_new('Scene 5 — Where: stack them all', (-0.5, 4.7), (-2.5, 2.6))
    x = np.linspace(0.2, 4, 200)
    ax.fill_between(x, -np.sqrt(x), np.sqrt(x), color=BLUE, alpha=0.3)
    ax.plot(x, np.sqrt(x), BLUE, lw=1.8)
    ax.plot(x, -np.sqrt(x), BLUE, lw=1.8)
    for xd in (0.7, 1.5, 2.3, 3.1, 3.9):
        r = np.sqrt(xd)
        ax.plot([xd, xd], [-r, r], RED, lw=1.1, alpha=0.75)
    ax.plot([-0.2, 4.35], [0, 0], '#333', lw=1.8)
    ax.text(2.4, -1.35, '$V = \\pi\\int_0^4 x\\,dx = 8\\pi$', ha='center', fontsize=11,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: add every disk $x\\in[0,4]$ → $V=\\int dV$')
    _scene_save(fig, '17a-disk-scene5.png')

def washer_scenes():
    """Washer method — 5 separate scene images. Region between √x and x² about y=2."""

    def region(ax):
        x = np.linspace(0, 1, 250)
        ax.plot(x, np.sqrt(x), BLUE, lw=2.4)
        ax.plot(x, x**2, RED, lw=2.4)
        ax.fill_between(x, x**2, np.sqrt(x), color=GREEN, alpha=0.22)
        ax.axhline(2, color='#333', lw=1.8, ls='--')
        ax.text(1.5, 2.08, 'axis $y=2$', fontsize=9, color='#333')

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: setup', (-0.35, 1.7), (-0.55, 2.55))
    region(ax)
    ax.text(0.67, 1.35, 'Axis is OUTSIDE the region →\nspinning leaves a HOLE → washer',
            ha='center', fontsize=9.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHEN: the axis does NOT touch the region (a hole appears)')
    _scene_save(fig, '17a-washer-scene1.png')

    # Scene 2 — How: slice
    fig, ax = _scene_new('Scene 2 — How: cut a slice', (-0.35, 1.7), (-0.55, 2.55))
    region(ax)
    xs = 0.5
    ax.add_patch(Rectangle((xs, xs**2), 0.12, np.sqrt(xs) - xs**2, facecolor=RED,
                           alpha=0.6, edgecolor=RED, lw=1.6))
    ax.plot([xs, xs], [xs**2, 2], color='#555', lw=1.1, ls=':')
    ax.plot([xs, xs], [np.sqrt(xs), 2], color='#555', lw=1.1, ls=':')
    ax.text(xs + 0.16, 1.78, '$R=2-x^2$', fontsize=9.5, color='#222', fontweight='bold')
    ax.text(xs + 0.16, 1.22, '$r=2-\\sqrt{x}$', fontsize=9.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'HOW: slice ⟂ axis; radii = distance from axis to each curve')
    _scene_save(fig, '17a-washer-scene2.png')

    # Scene 3 — How: rotate
    fig, ax = _scene_new('Scene 3 — How: rotate the slice', (0.5, 4.9), (-1.5, 2.6))
    cx, cy, R, r = 2.7, 0.4, 1.5, 0.62
    ax.add_patch(Circle((cx, cy), R, facecolor=RED, alpha=0.35, edgecolor=RED, lw=2.2))
    ax.add_patch(Circle((cx, cy), r, facecolor='white', edgecolor=GREEN, lw=2.2))
    ax.plot([cx, cx + R], [cy, cy], RED, lw=1.4)
    ax.plot([cx, cx + r], [cy, cy], GREEN, lw=1.4)
    ax.text(cx + R/2, cy - 0.28, '$R$', fontsize=11, color='#222', fontweight='bold',
            ha='center')
    ax.text(cx + r/2, cy - 0.28, '$r$', fontsize=11, color='#222', fontweight='bold',
            ha='center')
    ax.text(cx, cy + R + 0.32, 'the hole!', fontsize=10, color=GREEN, fontweight='bold',
            ha='center')
    _scene_caption(ax, 'HOW: the strip sweeps a washer — outer $R$, inner $r$ (hole)')
    _scene_save(fig, '17a-washer-scene3.png')

    # Scene 4 — Where: one washer
    fig, ax = _scene_new('Scene 4 — Where: volume of ONE washer', (0.5, 4.9), (-1.8, 2.6))
    cx, cy = 2.7, 0.6
    ax.add_patch(Circle((cx, cy), R, facecolor=GREEN, alpha=0.3, edgecolor=GREEN, lw=2.2))
    ax.add_patch(Circle((cx, cy), r, facecolor='white', edgecolor=GREEN, lw=2.2))
    ax.text(cx, cy - R - 0.25, '$dV = \\pi(R^2-r^2)\\,dx$\n$= \\pi[(2-x^2)^2-(2-\\sqrt{x})^2]\\,dx$',
            ha='center', fontsize=9.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: washer = big disk $\\pi R^2$ − hole $\\pi r^2$; × $dx$')
    _scene_save(fig, '17a-washer-scene4.png')

    # Scene 5 — Where: stack + integrate
    fig, ax = _scene_new('Scene 5 — Where: stack them all', (-0.35, 1.7), (-1.1, 4.7))
    x = np.linspace(0, 1, 250)
    ax.fill_between(x, x**2, np.sqrt(x), color=GREEN, alpha=0.3)
    ax.fill_between(x, 4 - np.sqrt(x), 4 - x**2, color=GREEN, alpha=0.3)
    ax.plot(x, x**2, BLUE, lw=1.6)
    ax.plot(x, 4 - x**2, BLUE, lw=1.6)
    ax.plot(x, np.sqrt(x), RED, lw=1.4, ls='--')
    ax.plot(x, 4 - np.sqrt(x), RED, lw=1.4, ls='--')
    ax.axhline(2, color='#333', lw=1.6, ls=':')
    ax.text(1.5, 2.05, 'axis', fontsize=9, color='#333')
    ax.text(0.5, -0.75, '$V = \\pi\\int_0^1[(2-x^2)^2-(2-\\sqrt{x})^2]\\,dx = \\frac{31\\pi}{30}$',
            ha='center', fontsize=9.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: every washer $x\\in[0,1]$ → $V=\\int dV$ (solid is hollow)')
    _scene_save(fig, '17a-washer-scene5.png')

def shell_scenes():
    """Shell method — 5 separate scene images. Rotate y=x² about the y-axis, x∈[0,2]."""

    def region(ax):
        x = np.linspace(0, 2, 200)
        ax.plot(x, x**2, BLUE, lw=2.4)
        ax.fill_between(x, 0, x**2, color=BLUE, alpha=0.16)
        ax.plot([0, 0], [-0.2, 4.4], '#333', lw=2.0)
        ax.text(0.14, 4.15, 'axis', fontsize=9, color='#333')

    # Scene 1 — When
    fig, ax = _scene_new('Scene 1 — When: setup', (-0.6, 2.7), (-0.5, 4.7))
    region(ax)
    ax.text(1.3, 3.3, 'Natural slice runs PARALLEL\nto the axis → cylindrical shell',
            ha='center', fontsize=9.5, color='#222', fontweight='bold')
    _scene_caption(ax, 'WHEN: the slice runs ∥ to the rotation axis (no hole, no washer)')
    _scene_save(fig, '17a-shell-scene1.png')

    # Scene 2 — How: slice
    fig, ax = _scene_new('Scene 2 — How: cut a slice', (-0.6, 2.7), (-0.5, 4.7))
    region(ax)
    xs = 1.2
    ax.add_patch(Rectangle((xs, 0), 0.24, xs**2, facecolor=RED, alpha=0.6, edgecolor=RED,
                           lw=1.6))
    ax.annotate('width $dx$', (xs + 0.12, 0.1), xytext=(xs + 0.55, 0.55), fontsize=9.5,
                color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.annotate('height $x^2$', (xs + 0.24, xs**2), xytext=(1.95, 2.35), fontsize=9.5,
                color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.annotate('distance $x$', (xs, 0), xytext=(0.2, 1.15), fontsize=9.5, color='#333',
                fontweight='bold', arrowprops=dict(arrowstyle='->', color='#333', lw=1.1))
    _scene_caption(ax, 'HOW: vertical strip — height $x^2$, thickness $dx$, distance $x$')
    _scene_save(fig, '17a-shell-scene2.png')

    # Scene 3 — How: rotate
    fig, ax = _scene_new('Scene 3 — How: rotate the slice', (0.7, 5.5), (-1.3, 3.0))
    r, h, cx, cy = 1.2, 1.44, 2.7, 0.4
    fs = 0.45
    ax.add_patch(Ellipse((cx, cy), 2*r, 2*r*fs, facecolor=RED, alpha=0.35, edgecolor=RED,
                         lw=2.0))
    ax.add_patch(Ellipse((cx, cy + h), 2*r, 2*r*fs, facecolor='white', edgecolor=RED,
                         lw=2.0))
    ax.plot([cx - r, cx - r], [cy, cy + h], RED, lw=1.6)
    ax.plot([cx + r, cx + r], [cy, cy + h], RED, lw=1.6)
    ax.plot([cx, cx + r], [cy, cy], '#333', lw=1.4)
    ax.text(cx + r/2, cy - 0.24, 'radius $r=x$', fontsize=10, color='#222', fontweight='bold',
            ha='center')
    ax.text(cx + r + 0.22, cy + h/2, 'height $h=x^2$', fontsize=10, color='#222',
            fontweight='bold')
    _scene_caption(ax, 'HOW: the strip sweeps a hollow cylinder — radius $x$, height $x^2$')
    _scene_save(fig, '17a-shell-scene3.png')

    # Scene 4 — Where: unroll
    fig, ax = _scene_new('Scene 4 — Where: unroll the shell', (-0.6, 8.8), (-1.5, 2.4),
                         aspect=False, fs=(5.8, 4.0))
    w, h = 2*np.pi*1.2, 1.44
    ax.add_patch(Rectangle((0.3, 0.5), w, h, facecolor=GREEN, alpha=0.3, edgecolor=GREEN,
                           lw=2.2))
    ax.add_patch(Rectangle((0.3 + w, 0.5), 0.12, h, facecolor=GREEN, alpha=0.5,
                           edgecolor=GREEN, lw=1.4))
    ax.annotate('length $2\\pi r = 2\\pi x$', (0.3, 0.55), xytext=(0.7, -0.3), fontsize=9.5,
                color='#222', fontweight='bold')
    ax.annotate('height $h = x^2$', (0.3, 0.5 + h), xytext=(-0.4, 1.4), fontsize=9.5,
                color='#222', fontweight='bold')
    ax.text(0.3 + w + 0.06, 0.5 + h/2, '$dx$', fontsize=9.5, color='#222', fontweight='bold')
    ax.text((0.3 + 0.3 + w)/2, -1.1, '$dV = (2\\pi x)(x^2)(dx)$', ha='center', fontsize=10,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: cut open & flatten — length $2\\pi x$, height $x^2$, thickness $dx$')
    _scene_save(fig, '17a-shell-scene4.png')

    # Scene 5 — Where: stack + integrate
    fig, ax = _scene_new('Scene 5 — Where: stack them all', (-2.6, 2.6), (-1.4, 4.6))
    y = np.linspace(0, 4, 200)
    ax.fill_betweenx(y, -np.sqrt(y), np.sqrt(y), color=BLUE, alpha=0.3)
    ax.plot(np.sqrt(y), y, BLUE, lw=1.8)
    ax.plot(-np.sqrt(y), y, BLUE, lw=1.8)
    for yd in (0.6, 1.4, 2.2, 3.0, 3.8):
        r = np.sqrt(yd)
        ax.plot([-r, r], [yd, yd], RED, lw=1.1, alpha=0.75)
    ax.plot([0, 0], [-0.2, 4.4], '#333', lw=1.8)
    ax.text(0, -1.2, '$V = 2\\pi\\int_0^2 x\\cdot x^2\\,dx = 8\\pi$', ha='center', fontsize=10,
            color='#222', fontweight='bold')
    _scene_caption(ax, 'WHERE: every shell $x\\in[0,2]$ → $V=\\int dV$')
    _scene_save(fig, '17a-shell-scene5.png')

if __name__ == '__main__':
    for fn in (area_between_curves, polar_rose, parametric_ellipse, triangle_cross_product,
               volume_method_disk, volume_method_washer, volume_method_shell,
               washer_shifted_axis, sphere_volume, torus,
               determinant_area, cross_section_volume, inverse_curves,
               solid_revolution, solid_revolution_dy,
               disk_scenes, washer_scenes, shell_scenes):
        fn()
        print('done:', fn.__name__)
    print('All 17A session graphs written under', BASE)
