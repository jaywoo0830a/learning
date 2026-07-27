#!/usr/bin/env python3
"""Generate visual graphs for 17B Arc Length, Surface Area, Improper Integrals."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, Circle, Polygon, Rectangle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams.update({
    'figure.dpi': 150, 'savefig.dpi': 150,
    'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 11,
    'savefig.facecolor': 'white', 'savefig.edgecolor': 'none',
    'figure.facecolor': 'white',
})

def save_fig(fig, name):
    fig.savefig(f'{OUTPUT_DIR}/{name}', bbox_inches='tight', facecolor='white',
                edgecolor='none', pad_inches=0.15)
    plt.close(fig)

# ════════════════════════════════════════════════════
# 01 — Arc Length: Pythagorean Approximation
# ════════════════════════════════════════════════════
def fig_01_arc_length_pythagoras():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, 4, 400)
    y = x**(1.5)
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    # Polygonal approximation with 5 segments
    n_seg = 5
    x_seg = np.linspace(0, 4, n_seg+1)
    y_seg = x_seg**(1.5)
    for i in range(n_seg):
        ax.plot([x_seg[i], x_seg[i+1]], [y_seg[i], y_seg[i+1]], '#E74C3C', lw=2, alpha=0.7, zorder=4)
    ax.plot(x_seg, y_seg, 'o', color='#E74C3C', ms=5, zorder=5)

    # Show Δx, Δy for one segment
    i = 1
    dx = x_seg[i+1] - x_seg[i]
    dy = y_seg[i+1] - y_seg[i]
    ax.plot([x_seg[i], x_seg[i+1]], [y_seg[i], y_seg[i]], 'g--', lw=1, alpha=0.6)
    ax.plot([x_seg[i+1], x_seg[i+1]], [y_seg[i], y_seg[i+1]], 'g--', lw=1, alpha=0.6)
    ax.annotate('Δx', (x_seg[i]+dx/2, y_seg[i]-0.3), fontsize=9, ha='center', color='green')
    ax.annotate('Δy', (x_seg[i+1]+0.15, y_seg[i]+dy/2), fontsize=9, color='green')
    ax.annotate(r'ΔL≈√(Δx²+Δy²)', (x_seg[i]+dx/2, y_seg[i]+dy/2+0.3),
                fontsize=10, color='#E74C3C', ha='center', fontweight='bold')

    ax.set_xlim(-0.2, 4.3); ax.set_ylim(-0.5, 9)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.25)
    ax.set_title('Arc Length: ΔL ≈ √(Δx²+Δy²) — Pythagorean Sum at Infinitesimal Scale', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '01-arc-length-pythagoras.png')

# ════════════════════════════════════════════════════
# 02 — Helix Arc Length (3D)
# ════════════════════════════════════════════════════
def fig_02_helix_3d():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(0, 6*np.pi, 500)
    x, y, z = np.cos(t), np.sin(t), t
    ax.plot(x, y, z, 'b-', lw=2, zorder=3)

    # Projection on xy-plane
    ax.plot(x, y, np.zeros_like(t), 'gray', lw=1, alpha=0.3, linestyle='--')
    theta_c = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(theta_c), np.sin(theta_c), np.zeros(200), 'gray', lw=1, alpha=0.4)

    # Mark one full turn
    t_one = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(t_one), np.sin(t_one), t_one, '#E74C3C', lw=3.5, zorder=4)

    # Velocity vector at a point
    t0 = np.pi
    pt = np.array([np.cos(t0), np.sin(t0), t0])
    v = np.array([-np.sin(t0), np.cos(t0), 1])
    ax.quiver(pt[0], pt[1], pt[2], v[0], v[1], v[2],
              color='#2ECC71', arrow_length_ratio=0.25, lw=2)

    ax.text(0, 0, 0, 'xy-projection\n(circle)', fontsize=9, ha='center')
    ax.text(1.2, 0, 4*np.pi, f'One turn: L=2π√2\nSpeed=|v|=√2',
            fontsize=11, color='#E74C3C', fontweight='bold')

    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('Helix: r(t)=(cos t, sin t, t) — Constant Speed √2', fontweight='bold')
    save_fig(fig, '02-helix-3d.png')

# ════════════════════════════════════════════════════
# 03 — Cycloid Arc Length
# ════════════════════════════════════════════════════
def fig_03_cycloid():
    fig, ax = plt.subplots(figsize=(10, 6))
    a = 1
    t = np.linspace(0, 2*np.pi, 500)
    x = a*(t - np.sin(t))
    y = a*(1 - np.cos(t))
    ax.plot(x, y, 'b-', lw=3, zorder=3)

    # Rolling circle at several positions
    for t0 in [np.pi/2, np.pi, 3*np.pi/2]:
        cx = a*t0
        cy = a
        circle = Circle((cx, cy), a, fill=False, ec='gray', lw=1, alpha=0.5, linestyle='--')
        ax.add_patch(circle)
        # Point on rim
        ax.plot(a*(t0 - np.sin(t0)), a*(1 - np.cos(t0)), 'o', color='#E74C3C', ms=6)

    # Ground
    ax.axhline(0, color='k', lw=2)
    ax.annotate('L = 8a\n(= 4 × diameter)', (np.pi*a, 1.6), fontsize=14, color='#E74C3C',
                fontweight='bold', ha='center', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    ax.annotate('One arch: 0 → 2π', (np.pi*a, 2.1), fontsize=11, ha='center')

    ax.set_xlim(-0.5, 2*np.pi*a+0.5); ax.set_ylim(-0.3, 2.5*a)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_title('Cycloid: One Arch Arc Length = 8a', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '03-cycloid.png')

# ════════════════════════════════════════════════════
# 04 — Surface Area of Revolution: y=√x about x-axis
# ════════════════════════════════════════════════════
def fig_04_surface_revolution():
    fig, ax = plt.subplots(figsize=(9, 7))

    # Generating curve
    x = np.linspace(0, 4.2, 400)
    y = np.sqrt(x)
    ax.plot(x, y, 'b-', lw=3, zorder=3)
    ax.fill_between(x, -y, y, alpha=0.06, color='#3498DB')

    # Axis
    ax.axhline(0, color='k', lw=1.5)

    # Surface bands at several positions
    for x0 in [0.5, 1.5, 2.5, 3.5]:
        y0 = np.sqrt(x0)
        # Show band as ellipse (perspective view of circular band)
        band = mpatches.Ellipse((x0, 0), 0.15, 2*y0, fill=True, fc='#E74C3C', alpha=0.25, ec='#E74C3C', lw=1.5)
        ax.add_patch(band)

    # Show one band detail
    xd = 2.5
    yd = np.sqrt(xd)
    ax.annotate(f'radius=y\nslant=ds', (xd, yd), textcoords="offset points", xytext=(15, 20),
                fontsize=10, color='#E74C3C', fontweight='bold')
    ax.annotate('dS = 2πy·ds', (xd, -yd-0.3), fontsize=10, color='#E74C3C', ha='center')

    ax.set_xlim(-0.2, 4.5); ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_title('Surface of Revolution: S=2π∫y√(1+(y\')²)dx', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '04-surface-revolution.png')

# ════════════════════════════════════════════════════
# 05 — Sphere Surface Area Derivation
# ════════════════════════════════════════════════════
def fig_05_sphere_surface_area():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    R = 3

    # Left: generating semicircle with slant element
    theta = np.linspace(0, np.pi, 400)
    x, y = R*np.cos(theta), R*np.sin(theta)
    ax1.plot(x, y, 'b-', lw=3)
    ax1.fill_between(x, -0.2, y, alpha=0.08, color='#3498DB')
    ax1.axhline(0, color='k', lw=1.5)

    # Show slant element
    t0 = np.pi/3
    x0, y0 = R*np.cos(t0), R*np.sin(t0)
    ax1.plot(x0, y0, 'ko', ms=8)
    # Tangent segment showing ds
    ds_scale = 1.2
    dx = -np.sin(t0)*ds_scale
    dy = np.cos(t0)*ds_scale
    ax1.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0),
                 arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2.5))
    ax1.annotate(f'ds', (x0+dx/2, y0+dy/2+0.3), fontsize=11, color='#E74C3C', fontweight='bold')
    ax1.annotate(f'radius\n= y = R sin θ', (x0-0.3, y0/2), fontsize=9, ha='right')

    ax1.set_aspect('equal'); ax1.set_xlim(-4, 4); ax1.set_ylim(-0.5, 4)
    ax1.grid(True, alpha=0.2)
    ax1.set_title('Rotate semicircle about x-axis', fontweight='bold')
    ax1.set_xlabel('x'); ax1.set_ylabel('y')

    # Right: sphere with bands
    ax2.set_aspect('equal')
    for y_band in np.linspace(-R+0.5, R-0.5, 5):
        r_band = np.sqrt(R**2 - y_band**2)
        band = mpatches.Ellipse((0, y_band), 2*(r_band+0.15), 0.4, fill=True,
                                 fc='#E74C3C', alpha=0.2, ec='#E74C3C', lw=1)
        ax2.add_patch(band)
    # Outline
    circle = Circle((0, 0), R, fill=False, ec='#3498DB', lw=3)
    ax2.add_patch(circle)

    ax2.annotate(f'S = 4πR²\n  = 4π·{R}²\n  = {4*np.pi*R**2:.1f}', (0, 0),
                 fontsize=14, fontweight='bold', ha='center', color='#E74C3C',
                 bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    ax2.set_xlim(-4, 4); ax2.set_ylim(-4, 4)
    ax2.grid(True, alpha=0.15)
    ax2.set_title('Sphere: S = 4πR²', fontweight='bold')

    fig.suptitle('Sphere Surface Area — The Classic Derivation', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '05-sphere-surface-area.png')

# ════════════════════════════════════════════════════
# 06 — Gabriel's Horn
# ════════════════════════════════════════════════════
def fig_06_gabriels_horn():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Left: generating curve y=1/x
    x = np.linspace(1, 8, 500)
    y = 1/x
    ax1.plot(x, y, 'b-', lw=3, zorder=3)
    ax1.fill_between(x, -y, y, alpha=0.08, color='#3498DB')
    ax1.axhline(0, color='k', lw=1.5)

    # Show thickening: area under 1/x² vs 1/x
    x2 = np.linspace(1, 6, 300)
    ax1.fill_between(x2, 1/x2**2, alpha=0.2, color='#2ECC71', label='Volume: integrand 1/x²')
    ax1.fill_between(x2, 1/x2, alpha=0.15, color='#E74C3C', label='Surface: integrand ~1/x')

    ax1.set_xlim(0.8, 7); ax1.set_ylim(-0.3, 1.5)
    ax1.legend(fontsize=9); ax1.grid(True, alpha=0.2)
    ax1.set_title('y=1/x: Volume ~ 1/x², Surface ~ 1/x', fontweight='bold')
    ax1.set_xlabel('x'); ax1.set_ylabel('y')

    # Right: horn shape (profile view)
    # Upper and lower surfaces
    x_horn = np.linspace(1, 6, 200)
    y_horn = 1/x_horn
    ax2.fill_between(x_horn, y_horn, -y_horn, alpha=0.25, color='#3498DB')
    ax2.plot(x_horn, y_horn, 'b-', lw=2)
    ax2.plot(x_horn, -y_horn, 'b-', lw=2)

    # Annotations
    ax2.annotate('V = π (finite!)', (4.5, 0.5), fontsize=12, color='#2ECC71', fontweight='bold')
    ax2.annotate('S → ∞ (infinite!)', (4.5, -0.55), fontsize=12, color='#E74C3C', fontweight='bold')
    ax2.annotate('You can FILL it\nbut cannot PAINT it', (2.5, 0.1), fontsize=11,
                 fontweight='bold', ha='center',
                 bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    ax2.arrow(6.2, 0, 2, 0, head_width=0.08, head_length=0.3, fc='gray', ec='gray')
    ax2.annotate('→ ∞', (7.5, 0.05), fontsize=11, ha='center')

    ax2.set_xlim(0.8, 9); ax2.set_ylim(-1, 1)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.2)
    ax2.set_title("Gabriel's Horn: Finite Volume, Infinite Surface", fontweight='bold')
    ax2.set_xlabel('x')

    fig.suptitle("Gabriel's Horn Paradox", fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '06-gabriels-horn.png')

# ════════════════════════════════════════════════════
# 07 — p-Test: Convergence vs Divergence
# ════════════════════════════════════════════════════
def fig_07_p_test():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Left: p>1 (converges) - 1/x²
    ax = axes[0]
    x = np.linspace(1, 6, 400)
    ax.fill_between(x, 1/x**2, alpha=0.3, color='#2ECC71')
    ax.plot(x, 1/x**2, 'b-', lw=2.5)
    ax.axhline(0, color='k', lw=1)
    ax.annotate(r'$\int_1^\infty 1/x^2\,dx = 1$', (2, 0.5), fontsize=12,
                fontweight='bold', color='#2ECC71',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax.set_title('p=2 > 1: CONVERGES', fontweight='bold', color='#27AE60')
    ax.set_xlim(0.8, 6); ax.set_ylim(-0.05, 1.2)
    ax.grid(True, alpha=0.2)
    ax.set_xlabel('x'); ax.set_ylabel('1/x²')

    # Middle: p=1 (diverges) - 1/x (harmonic)
    ax = axes[1]
    ax.fill_between(x, 1/x, alpha=0.3, color='#E74C3C')
    ax.plot(x, 1/x, 'b-', lw=2.5)
    ax.axhline(0, color='k', lw=1)
    ax.annotate(r'$\int_1^\infty 1/x\,dx = \infty$', (2, 0.5), fontsize=12,
                fontweight='bold', color='#E74C3C',
                bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax.set_title('p=1: DIVERGES (harmonic)', fontweight='bold', color='#C0392B')
    ax.set_xlim(0.8, 6); ax.set_ylim(-0.05, 1.2)
    ax.grid(True, alpha=0.2)
    ax.set_xlabel('x'); ax.set_ylabel('1/x')

    # Right: p-test summary
    ax = axes[2]
    ax.axis('off')
    summary = (
        "p-TEST SUMMARY\n\n"
        "∫₁^∞ 1/x^p dx:\n"
        "  p > 1 → CONVERGES\n"
        "  p ≤ 1 → DIVERGES\n\n"
        "∫₀¹ 1/x^p dx:\n"
        "  p < 1 → CONVERGES\n"
        "  p ≥ 1 → DIVERGES\n\n"
        "The boundary p=1\n"
        "is the harmonic threshold."
    )
    ax.text(0.1, 0.9, summary, transform=ax.transAxes, fontsize=13,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.suptitle('Improper Integral p-Test', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '07-p-test.png')

# ════════════════════════════════════════════════════
# 08 — Gaussian Integral: Polar Coordinate Trick
# ════════════════════════════════════════════════════
def fig_08_gaussian_integral():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

    # Left: 1D Gaussian
    ax = axes[0]
    x = np.linspace(-4, 4, 500)
    ax.fill_between(x, np.exp(-x**2), alpha=0.3, color='#3498DB')
    ax.plot(x, np.exp(-x**2), 'b-', lw=2.5)
    ax.annotate(r'$I = \int_{-\infty}^\infty e^{-x^2}dx$', (0, 0.5), fontsize=12,
                ha='center', fontweight='bold')
    ax.annotate(r'$I = \sqrt{\pi}$', (0, 0.25), fontsize=13, ha='center',
                color='#E74C3C', fontweight='bold')
    ax.set_xlim(-4, 4); ax.set_ylim(0, 1.1)
    ax.grid(True, alpha=0.2)
    ax.set_title('1D Gaussian', fontweight='bold')
    ax.set_xlabel('x')

    # Middle: 2D Gaussian (I² as volume under bell surface)
    ax = axes[1]
    # Show concentric circles
    for r in [0.5, 1, 1.5, 2, 2.5]:
        circle = Circle((0, 0), r, fill=False, ec='#E74C3C', lw=1.5, alpha=0.5)
        ax.add_patch(circle)
    # Color shading
    xx, yy = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
    zz = np.exp(-(xx**2 + yy**2))
    ax.contourf(xx, yy, zz, levels=15, cmap='Blues', alpha=0.6)
    ax.annotate(r'$I^2 = \iint e^{-(x^2+y^2)}dx\,dy$', (0, -3.3), fontsize=11,
                ha='center', fontweight='bold')
    ax.set_aspect('equal'); ax.set_xlim(-3.2, 3.2); ax.set_ylim(-3.5, 3.5)
    ax.set_title('2D: Square & Convert to Polar', fontweight='bold')

    # Right: Polar integration
    ax = axes[2]
    ax.axis('off')
    derivation = (
        "POLAR TRICK\n\n"
        "I² = ∫∫ e^{-(x²+y²)} dx dy\n\n"
        "Switch to polar:\n"
        "x²+y² = r²\n"
        "dx dy = r dr dθ\n"
        "  ↑ Jacobian det = r\n\n"
        "I² = ∫₀^{2π}∫₀^∞ e^{-r²} r dr dθ\n"
        "   = 2π · [−½e^{-r²}]₀^∞\n"
        "   = 2π · ½ = π\n\n"
        "∴ I = √π"
    )
    ax.text(0.1, 0.95, derivation, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.suptitle('Gaussian Integral: The Polar Coordinate Proof', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '08-gaussian-integral.png')

# ════════════════════════════════════════════════════
# 09 — Arc Length: Polar Curve (Cardioid)
# ════════════════════════════════════════════════════
def fig_09_polar_arc_length():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, 2*np.pi, 800)
    r = 1 + np.cos(theta)
    ax.plot(theta, r, 'b-', lw=3)

    # Show ds element
    t0 = np.pi/4
    r0 = 1 + np.cos(t0)
    # Tangent at that point
    ax.plot(t0, r0, 'o', color='#E74C3C', ms=10, zorder=5)

    ax.annotate('L = 8', (np.pi, 1.8), fontsize=14, color='#E74C3C', fontweight='bold', ha='center')
    ax.annotate('ds = √((dr/dθ)²+r²) dθ', (np.pi, 1.4), fontsize=10, ha='center')
    ax.set_title('Cardioid r=1+cosθ: Arc Length L=8', fontweight='bold', fontsize=13, pad=20)
    save_fig(fig, '09-polar-arc-length.png')

# ════════════════════════════════════════════════════
# 10 — Conical Spiral: Speed grows with t
# ════════════════════════════════════════════════════
def fig_10_conical_spiral():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(0, 4*np.pi, 500)
    x, y, z = t*np.cos(t), t*np.sin(t), t
    ax.plot(x, y, z, 'b-', lw=1.5, zorder=3)

    # Highlight first and last turn
    for t_start, color, alpha in [(0, '#E74C3C', 0.7), (3*np.pi, '#2ECC71', 0.7)]:
        t_highlight = np.linspace(t_start, t_start+2*np.pi, 100)
        ax.plot(t_highlight*np.cos(t_highlight), t_highlight*np.sin(t_highlight),
                t_highlight, color=color, lw=3.5, alpha=alpha)

    # Cone surface (wireframe)
    t_cone = np.linspace(0, 4*np.pi, 30)
    theta_cone = np.linspace(0, 2*np.pi, 30)
    T, Th = np.meshgrid(t_cone, theta_cone)
    X = T*np.cos(Th); Y = T*np.sin(Th); Z = T
    ax.plot_wireframe(X, Y, Z, alpha=0.08, color='gray', rstride=3, cstride=3)

    ax.text(0, 0, 0, 'speed = √(t²+2)\ngrows with t', fontsize=10,
            color='#E74C3C', fontweight='bold')

    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('Conical Spiral: r(t)=(t cos t, t sin t, t) — Accelerating', fontweight='bold')
    save_fig(fig, '10-conical-spiral.png')

if __name__ == '__main__':
    print("Generating 17B graphs...")
    fig_01_arc_length_pythagoras()
    fig_02_helix_3d()
    fig_03_cycloid()
    fig_04_surface_revolution()
    fig_05_sphere_surface_area()
    fig_06_gabriels_horn()
    fig_07_p_test()
    fig_08_gaussian_integral()
    fig_09_polar_arc_length()
    fig_10_conical_spiral()
    print("Done! 10 graphs generated.")
