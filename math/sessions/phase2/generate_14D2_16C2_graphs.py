#!/usr/bin/env python3
"""Generate the session graphs for 14D2 (advanced derivative interpretation) and 16C2 (advanced integral interpretation).

Outputs into graphs/0821/14D2 and graphs/0821/16C2 (png).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as MplCircle, FancyArrowPatch
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
BASE = os.path.join(os.path.dirname(__file__), 'graphs', '0821')
for _sub in ('14D2', '16C2'):
    os.makedirs(os.path.join(BASE, _sub), exist_ok=True)

BLUE = '#1a73e8'
RED = '#d93025'
GREEN = '#188038'
AMBER = '#f9ab00'
PURPLE = '#7b1fa2'
GRAY = '#666666'

def save(fig, sub, name):
    fig.savefig(os.path.join(BASE, sub, name), bbox_inches='tight')
    plt.close(fig)

def g(ax):
    ax.grid(True, alpha=0.15, lw=0.4)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# ═══════════════════════════ 14D2 ═══════════════════════════

def a1_dimension_space():
    """3D axis frame {L, M, T} with unit vectors of speed, force, energy."""
    fig = plt.figure(figsize=(8.5, 6.2))
    ax = fig.add_subplot(111, projection='3d')
    for axis, label, col in (((0, 3), 'L (length)', BLUE), ((3, 0), 'M (mass)', GREEN), ((0, -3), 'T (time)', RED)):
        pass
    # axes
    for span, lbl, col in (([0, 2.8], 'L', BLUE), ([0, 2.8], 'M', GREEN), ([0, -2.8], 'T', RED)):
        if lbl == 'L':
            ax.plot([0, span[1]], [0, 0], [0, 0], color=col, lw=2)
            ax.text(span[1], 0, 0.1, '  L', color=col, fontsize=13, fontweight='bold')
        elif lbl == 'M':
            ax.plot([0, 0], [0, span[1]], [0, 0], color=col, lw=2)
            ax.text(0, span[1], 0.1, '  M', color=col, fontsize=13, fontweight='bold')
        else:
            ax.plot([0, 0], [0, 0], [span[1], 0], color=col, lw=2)
            ax.text(0, 0.1, span[1], '  T', color=col, fontsize=13, fontweight='bold')
    vecs = [
        ((1, 0, -1), 'speed', BLUE),
        ((1, 1, -2), 'force', PURPLE),
        ((2, 1, -2), 'energy', AMBER),
    ]
    for v, name, col in vecs:
        ax.quiver(0, 0, 0, v[0], v[1], v[2], color=col, lw=3, arrow_length_ratio=0.12)
        ax.text(v[0]*1.08, v[1]*1.08, v[2]*1.08, f'  {name}', color=col, fontsize=10, fontweight='bold')
    ax.quiver(0.9, 0, -1.2, 0, 0, 1, color=RED, lw=2, arrow_length_ratio=0.2)
    ax.text(1.0, 0, -0.75, 'd/dt', color=RED, fontsize=10, fontweight='bold')
    ax.quiver(1.0, 0, -0.8, 0, 0, -1, color=RED, lw=2, arrow_length_ratio=0.2, ls='--')
    ax.text(1.0, 0, -1.7, '∫dt', color=RED, fontsize=10, fontweight='bold')
    ax.set_xlim(-0.5, 3.2); ax.set_ylim(-0.5, 3.2); ax.set_zlim(-3.2, 1.2)
    ax.set_axis_off()
    ax.view_init(elev=16, azim=-64)
    ax.set_title('The dimension space: units are vectors', fontweight='bold')
    fig.tight_layout()
    save(fig, '14D2', '14d2-1-dimension-space.png')

def a2_temperature_gradient():
    """T=60-x^2-2y^2: elliptical contours + gradient arrows (quiver)."""
    fig, ax = plt.subplots(figsize=(8, 6.8)); g(ax)
    x = np.linspace(-8.2, 8.2, 500)
    y = np.linspace(-6.2, 6.2, 500)
    X, Y = np.meshgrid(x, y)
    Z = 60 - X**2 - 2*Y**2
    levels = [8, 16, 24, 32, 40, 48, 56]
    cs = ax.contour(X, Y, Z, levels=levels, colors=GRAY, linewidths=0.9, alpha=0.75)
    ax.clabel(cs, fmt='%d°C', fontsize=7, inline_spacing=2)
    gx, gy = np.meshgrid(np.linspace(-7, 7, 9), np.linspace(-5, 5, 7))
    U = -2*gx; V = -4*gy
    ax.quiver(gx, gy, U, V, color=RED, angles='xy', scale_units='xy', scale=14, width=0.005)
    ax.plot([0], [0], 'o', color=AMBER, ms=9, zorder=6)
    ax.annotate('warm peak\n(∇T = 0)', (0, 0), xytext=(0.7, 0.9), fontsize=9,
                color=AMBER, fontweight='bold')
    ax.annotate('$\\nabla T=(-2x,-4y)$\nperpendicular to every contour', (-7.4, 4.6),
                fontsize=10, color=RED, fontweight='bold')
    ax.set_xlim(-8.2, 8.2); ax.set_ylim(-6.2, 6.2)
    ax.set_aspect('equal')
    ax.set_title('Temperature field $T=60-x^2-2y^2$ and its gradient', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
    fig.tight_layout()
    save(fig, '14D2', '14d2-2-temperature-gradient.png')

def a3_radial_gradient_3d():
    """T=x^2+y^2+z^2: radial gradient arrows + one level sphere."""
    fig = plt.figure(figsize=(8, 6.8))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2*np.pi, 48); v = np.linspace(0, np.pi, 48)
    R = 2.0
    xs = R*np.outer(np.cos(u), np.sin(v))
    ys = R*np.outer(np.sin(u), np.sin(v))
    zs = R*np.outer(np.ones_like(u), np.cos(v))
    ax.plot_wireframe(xs, ys, zs, color=GRAY, lw=0.35, alpha=0.6)
    pts = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2], [-2, 0, 0], [0, -2, 0], [0, 0, -2],
                    [3, 0, 0], [0, 3, 0], [0, 0, 3]], dtype=float)
    for p in pts:
        n = np.linalg.norm(p)
        if n > 0:
            ax.quiver(p[0], p[1], p[2], 2*p[0]*0.4, 2*p[1]*0.4, 2*p[2]*0.4,
                      color=RED, lw=2.2, arrow_length_ratio=0.22)
    ax.text(0, 0, 0.3, 'cold\ncenter', fontsize=9, color=AMBER, fontweight='bold', ha='center')
    ax.text(3.4, 1.2, 1.2, '$\\nabla T=2(x,y,z)$', fontsize=11, color=RED, fontweight='bold')
    lim = 3.6
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.view_init(elev=18, azim=-55)
    ax.set_title('Radial gradient of $T=x^2+y^2+z^2$ (level surface: sphere)', fontweight='bold')
    fig.tight_layout()
    save(fig, '14D2', '14d2-3-radial-gradient-3d.png')

def a4_complex_rotation_field():
    """Velocity field iωz on the unit circle: arrows rotated 90° ahead."""
    fig, ax = plt.subplots(figsize=(7, 6.6)); g(ax)
    ax.add_patch(MplCircle((0, 0), 1, fill=False, ec=BLUE, lw=2))
    for th in np.linspace(0, 2*np.pi, 13)[:-1]:
        p = np.array([np.cos(th), np.sin(th)])
        v = np.array([-np.sin(th), np.cos(th)])  # i z
        ax.quiver(p[0], p[1], 0.42*v[0], 0.42*v[1], color=RED, angles='xy',
                  scale_units='xy', scale=1, width=0.007)
        ax.plot([p[0]], [p[1]], 'o', color=BLUE, ms=5, zorder=6)
    p0 = np.array([1.0, 0.0])
    ax.annotate('$z$', (p0[0], p0[1]), xytext=(0.7, -0.32), fontsize=12, color=BLUE,
                fontweight='bold')
    ax.annotate('$v=i\\omega z$\n(rotated 90° ahead)', (0.55, 0.62), xytext=(0.9, 1.05),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.set_xlim(-1.6, 1.7); ax.set_ylim(-1.55, 1.5)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Differentiating circular motion: multiply by $i\\omega$', fontweight='bold')
    fig.tight_layout()
    save(fig, '14D2', '14d2-4-complex-rotation-field.png')

def a5_conformal_z2():
    """A tiny square near 1+i and its image under z^2: stretched 2.83x, rotated 45°."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    for ax in (ax1, ax2): g(ax)
    z0 = 1 + 1j
    corner = np.array([0.25 + 0.25j, 0.75 + 0.25j, 0.75 + 0.75j, 0.25 + 0.75j])
    sq = z0 + corner
    # left: z-plane
    ax1.add_patch(MplCircle((0, 0), np.sqrt(2), fill=False, ec=GRAY, lw=0.8, ls='--', alpha=0.5))
    ax1.plot([0, 1], [0, 1], color=GRAY, lw=0.8, alpha=0.6)
    ax1.fill(sq.real, sq.imag, color=BLUE, alpha=0.30, ec=BLUE, lw=2)
    ax1.plot([z0.real], [z0.imag], 'o', color=BLUE, ms=7, zorder=6)
    ax1.annotate('$z_0=1+i$', (z0.real, z0.imag), xytext=(0.35, 0.45), fontsize=10, color=BLUE, fontweight='bold')
    ax1.set_xlim(0, 2.2); ax1.set_ylim(0, 2.2)
    ax1.set_aspect('equal')
    ax1.set_title('$z$-plane: a tiny square near $1+i$', fontweight='bold')
    ax1.set_xlabel('Re'); ax1.set_ylabel('Im')
    # right: image under z^2
    im = sq**2
    ax2.fill(im.real, im.imag, color=RED, alpha=0.30, ec=RED, lw=2)
    ax2.plot([0], [2], 'o', color=GRAY, ms=6, zorder=6)
    ax2.annotate('$f(1+i)=2i$', (0, 2), xytext=(0.08, 1.45), fontsize=10, color=GRAY, fontweight='bold')
    ax2.annotate("stretch $2\\sqrt{2}$, rotate $45°$\n$f'(z_0)=2z_0=2+2i$", (1.6, 2.1),
                 fontsize=10, color=RED, fontweight='bold', ha='center')
    ax2.set_xlim(-1.2, 2.6); ax2.set_ylim(-0.8, 2.6)
    ax2.set_aspect('equal')
    ax2.set_title('image under $f(z)=z^2$: pure rotation + scale', fontweight='bold')
    ax2.set_xlabel('Re'); ax2.set_ylabel('Im')
    fig.tight_layout()
    save(fig, '14D2', '14d2-5-conformal-z2.png')

def a6_rotation_matrix_field():
    """Velocity field of a spinning plate v=(-2y,2x) with the matrix annotation."""
    fig, ax = plt.subplots(figsize=(7.6, 6.6)); g(ax)
    x = np.linspace(-3.6, 3.6, 8)
    X, Y = np.meshgrid(x, x)
    U = -2*Y; V = 2*X
    ax.quiver(X, Y, U, V, color=PURPLE, angles='xy', scale_units='xy', scale=22, width=0.006)
    for r in (1, 2, 3):
        ax.add_patch(MplCircle((0, 0), r, fill=False, ec=GRAY, lw=0.7, alpha=0.45))
    ax.annotate('$v = (-2y,\\ 2x) = i\\omega z$   (a 2x2 matrix acting on every point)',
                (0, 0), xytext=(0.25, 3.15), fontsize=10.5, color=PURPLE, fontweight='bold', ha='center')
    ax.set_xlim(-3.8, 3.8); ax.set_ylim(-3.5, 3.5)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('The spinning plate: a matrix IS a field', fontweight='bold')
    fig.tight_layout()
    save(fig, '14D2', '14d2-6-rotation-matrix-field.png')

# ═══════════════════════════ 16C2 ═══════════════════════════

def b1_wire_density():
    """Wire along [0,10] with density lambda=2x+1: shading + ds element."""
    fig, ax = plt.subplots(figsize=(9.5, 4.2)); g(ax)
    x = np.linspace(0, 10, 600)
    ax.plot(x, np.zeros_like(x), color='#333', lw=6, alpha=0.25)
    for xi in np.linspace(0.15, 9.85, 60):
        lam = 2*xi + 1
        ax.plot([xi, xi], [-0.22, -0.22 + 0.05*lam/21], color=BLUE, lw=1.6,
                alpha=min(1.0, 0.25 + lam/24))
    ax.plot([0, 10], [0, 0], color='#333', lw=3)
    ax.annotate('$\\lambda(x)=2x+1$ g/cm', (4.2, 0.32), fontsize=11, color=BLUE, fontweight='bold')
    ax.annotate('$ds$', (5.0, -0.42), fontsize=11, color=RED, fontweight='bold')
    ax.plot([5.0, 5.0], [-0.18, 0.0], color=RED, lw=1.2, ls='--')
    ax.annotate('$M=\\int_0^{10}(2x+1)\\,dx = 110$ g', (2.2, 0.85), fontsize=11,
                color=RED, fontweight='bold')
    ax.set_xlim(-0.4, 10.4); ax.set_ylim(-1.1, 1.1)
    ax.set_yticks([])
    ax.set_title('A wire with varying density: mass = density × arc element, summed', fontweight='bold')
    ax.set_xlabel('$x$ [cm]')
    fig.tight_layout()
    save(fig, '16C2', '16c2-1-wire-density.png')

def b2_circulation():
    """Vortex field F=(-y,x) around the unit circle: tangent arrows + circulation 2π."""
    fig, ax = plt.subplots(figsize=(7, 6.6)); g(ax)
    ax.add_patch(MplCircle((0, 0), 1, fill=False, ec=GRAY, lw=2))
    for th in np.linspace(0, 2*np.pi, 9)[:-1]:
        p = np.array([np.cos(th), np.sin(th)])
        v = np.array([-np.sin(th), np.cos(th)])
        ax.quiver(p[0], p[1], 0.4*v[0], 0.4*v[1], color=RED, angles='xy',
                  scale_units='xy', scale=1, width=0.008)
    ax.annotate('$F=(-y,x)$ pushes along\nthe path everywhere', (0.42, 0.5), xytext=(0.85, 1.05),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.1))
    ax.annotate('$\\oint F\\cdot dr = 2\\pi$', (0, -0.15), xytext=(-1.5, -1.35),
                fontsize=12, color=PURPLE, fontweight='bold', ha='center')
    ax.set_xlim(-1.55, 1.6); ax.set_ylim(-1.5, 1.55)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Circulation: the vortex field never rests', fontweight='bold')
    fig.tight_layout()
    save(fig, '16C2', '16c2-2-circulation.png')

def b3_flux():
    """Source field F=(x,y) through the unit circle (outward); inset vortex (tangent)."""
    fig, ax = plt.subplots(figsize=(7, 6.6)); g(ax)
    ax.add_patch(MplCircle((0, 0), 1, fill=False, ec=GRAY, lw=2))
    for th in np.linspace(0, 2*np.pi, 9)[:-1]:
        p = np.array([np.cos(th), np.sin(th)])
        ax.quiver(p[0], p[1], 0.45*p[0], 0.45*p[1], color=GREEN, angles='xy',
                  scale_units='xy', scale=1, width=0.008)
    ax.annotate('$F=(x,y)$ crosses the boundary\noutward everywhere', (0.4, 0.5), xytext=(0.8, 1.02),
                fontsize=10, color=GREEN, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.1))
    ax.annotate('flux $= \\oint F\\cdot n\\,ds = 2\\pi$', (0, 0), xytext=(0, -1.38),
                fontsize=12, color=AMBER, fontweight='bold', ha='center')
    ax.set_xlim(-1.55, 1.6); ax.set_ylim(-1.5, 1.55)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('Flux: the source field flows out (vortex would give 0)', fontweight='bold')
    fig.tight_layout()
    save(fig, '16C2', '16c2-3-flux.png')

def b4_divergence():
    """Two panels: source field div=2 vs spin field div=0."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 5))
    for ax in (ax1, ax2): g(ax)
    x = np.linspace(-2.6, 2.6, 6)
    X, Y = np.meshgrid(x, x)
    ax1.quiver(X, Y, X, Y, color=GREEN, angles='xy', scale_units='xy', scale=18, width=0.009)
    ax1.set_title('$F=(x,y)$: div $= 1+1 = 2$\nevery point is a source', fontweight='bold')
    ax1.set_aspect('equal'); ax1.set_xticks([]); ax1.set_yticks([])
    ax1.set_xlim(-3, 3); ax1.set_ylim(-3, 3)
    U = -Y; V = X
    ax2.quiver(X, Y, U, V, color=RED, angles='xy', scale_units='xy', scale=18, width=0.009)
    ax2.set_title('$F=(-y,x)$: div $= 0+0 = 0$\npure spin, nothing is created', fontweight='bold')
    ax2.set_aspect('equal'); ax2.set_xticks([]); ax2.set_yticks([])
    ax2.set_xlim(-3, 3); ax2.set_ylim(-3, 3)
    fig.tight_layout()
    save(fig, '16C2', '16c2-4-divergence.png')

def b5_gauss_law():
    """Point charge with radial E field through two spheres: equal flux."""
    fig, ax = plt.subplots(figsize=(7.6, 6.6)); g(ax)
    ax.plot([0], [0], 'o', color=AMBER, ms=12, zorder=6)
    ax.annotate('$Q$', (0, 0), xytext=(0.12, 0.15), fontsize=13, color='#7a4a00', fontweight='bold')
    for r, col in ((1.4, GRAY), (2.6, GRAY)):
        ax.add_patch(MplCircle((0, 0), r, fill=False, ec=col, lw=1.6, ls='--', alpha=0.8))
    for th in np.linspace(0, 2*np.pi, 13)[:-1]:
        d = np.array([np.cos(th), np.sin(th)])
        for rr in (1.4, 2.6):
            p = rr*d
            ax.quiver(p[0], p[1], 0.5*d[0], 0.5*d[1], color=RED, angles='xy',
                      scale_units='xy', scale=1, width=0.007)
    ax.annotate('$R$', (1.4, 0.05), xytext=(1.32, -0.45), fontsize=11, color=GRAY, fontweight='bold')
    ax.annotate('$2R$', (2.6, 0.05), xytext=(2.52, -0.45), fontsize=11, color=GRAY, fontweight='bold')
    ax.annotate('strength $\\times$ area:\n$\\frac{kQ}{R^2}\\cdot 4\\pi R^2 = 4\\pi kQ$\nat every radius', (1.7, 1.9),
                fontsize=10.5, color=RED, fontweight='bold', ha='center')
    ax.set_xlim(-3.1, 3.1); ax.set_ylim(-3.0, 3.0)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Gauss's law: the charge is the field's only source", fontweight='bold')
    fig.tight_layout()
    save(fig, '16C2', '16c2-5-gauss-law.png')

def b6_complex_integral():
    """Unit circle with the quarter-turn path element dz and the angle swept 2π."""
    fig, ax = plt.subplots(figsize=(7.4, 6.6)); g(ax)
    th = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), BLUE, lw=2.2)
    for t in np.linspace(0, 2*np.pi, 9)[:-1]:
        p = np.array([np.cos(t), np.sin(t)])
        dz = np.array([-np.sin(t), np.cos(t)])  # i z dt
        ax.quiver(p[0], p[1], 0.34*dz[0], 0.34*dz[1], color=RED, angles='xy',
                  scale_units='xy', scale=1, width=0.008)
    ax.plot([0], [0], 'o', color=GRAY, ms=7, zorder=6)
    ax.annotate('pole $z=0$', (0, 0), xytext=(0.15, 0.2), fontsize=10, color=GRAY, fontweight='bold')
    ax.annotate('$dz = iz\\,dt$\n(quarter-turn element)', (0.75, 0.75), xytext=(0.95, 0.85),
                fontsize=10, color=RED, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.0))
    ax.annotate('$\\oint \\frac{dz}{z} = 2\\pi i$\none winding, times the\nquarter-turn marker $i$', (-1.05, -0.6),
                xytext=(-1.48, -1.35), fontsize=11, color=PURPLE, fontweight='bold')
    ax.set_xlim(-1.55, 1.6); ax.set_ylim(-1.5, 1.55)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title('$dz/z$ counts the winding: $2\\pi i$ per lap', fontweight='bold')
    fig.tight_layout()
    save(fig, '16C2', '16c2-6-complex-integral.png')

if __name__ == '__main__':
    a1_dimension_space(); a2_temperature_gradient(); a3_radial_gradient_3d()
    a4_complex_rotation_field(); a5_conformal_z2(); a6_rotation_matrix_field()
    b1_wire_density(); b2_circulation(); b3_flux()
    b4_divergence(); b5_gauss_law(); b6_complex_integral()
    print('Done: 14D2 + 16C2 graphs written to graphs/0821/')
