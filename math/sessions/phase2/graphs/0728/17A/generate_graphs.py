#!/usr/bin/env python3
"""Generate visual graphs for 17A Area and Volume — Geometry Meets Integration."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, Circle, Polygon, Rectangle, Wedge
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
# 01 — Area Between y=x² and y=x
# ════════════════════════════════════════════════════
def fig_01_area_between_curves():
    fig, ax = plt.subplots(figsize=(8, 7))
    x = np.linspace(-0.2, 1.4, 300)
    ax.plot(x, x, '#E74C3C', lw=2.5, label='y=x (top)', zorder=3)
    ax.plot(x, x**2, '#3498DB', lw=2.5, label='y=x² (bottom)', zorder=3)

    # Fill region
    x_fill = np.linspace(0, 1, 200)
    ax.fill_between(x_fill, x_fill, x_fill**2, alpha=0.25, color='#8E44AD')
    ax.text(0.5, 0.35, 'A = 1/6', fontsize=14, color='#8E44AD', fontweight='bold', ha='center')

    # Intersection points
    ax.plot(0, 0, 'ko', ms=8, zorder=5)
    ax.plot(1, 1, 'ko', ms=8, zorder=5)
    ax.annotate('(0,0)', (0, 0), textcoords="offset points", xytext=(-15, -15), fontsize=10)
    ax.annotate('(1,1)', (1, 1), textcoords="offset points", xytext=(8, 8), fontsize=10)

    ax.set_xlim(-0.2, 1.3); ax.set_ylim(-0.1, 1.4)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=11); ax.grid(True, alpha=0.25)
    ax.set_title('Area Between Curves: ∫(top−bottom)dx = 1/6', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '01-area-between-curves.png')

# ════════════════════════════════════════════════════
# 02 — Polar Area: One Petal of r=sin(2θ)
# ════════════════════════════════════════════════════
def fig_02_polar_rose():
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(2*theta)
    # Only plot where r >= 0
    mask = r >= 0
    ax.fill_between(theta[mask], 0, r[mask], alpha=0.3, color='#E74C3C')
    ax.plot(theta, np.abs(np.sin(2*theta)), 'b-', lw=1.5, alpha=0.3)

    # Highlight one petal
    theta_petal = np.linspace(0, np.pi/2, 200)
    r_petal = np.sin(2*theta_petal)
    ax.fill_between(theta_petal, 0, r_petal, alpha=0.45, color='#E74C3C')
    ax.text(np.pi/4, 0.7, 'A = π/8', fontsize=13, color='#E74C3C', fontweight='bold', ha='center')

    ax.set_title('Polar Rose r=sin(2θ) — One Petal Area = π/8', fontweight='bold', fontsize=13, pad=20)
    save_fig(fig, '02-polar-rose.png')

# ════════════════════════════════════════════════════
# 03 — Triangle Area via Cross Product (3D)
# ════════════════════════════════════════════════════
def fig_03_triangle_cross_product():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([1, 0, 2])
    B = np.array([4, 1, 6])
    C = np.array([2, 5, 0])

    # Triangle edges
    for pair, color in [([A, B], '#E74C3C'), ([B, C], '#3498DB'), ([C, A], '#2ECC71')]:
        ax.plot(*zip(*pair), color=color, lw=3, zorder=3)

    # Cross product vector AB × AC
    AB = B - A
    AC = C - A
    cross = np.cross(AB, AC)
    mid = A + (AB + AC) / 2
    ax.quiver(mid[0], mid[1], mid[2], cross[0]/15, cross[1]/15, cross[2]/15,
              color='#8E44AD', arrow_length_ratio=0.2, lw=2.5)

    # Vertices
    for pt, label in [(A, 'A(1,0,2)'), (B, 'B(4,1,6)'), (C, 'C(2,5,0)')]:
        ax.scatter(*pt, c='black', s=60, zorder=5)
        ax.text(pt[0], pt[1], pt[2]+0.5, label, fontsize=9, fontweight='bold')

    ax.text(mid[0], mid[1], mid[2]+2, 'AB×AC\nArea = ½|AB×AC|', fontsize=10,
            color='#8E44AD', fontweight='bold', ha='center')

    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('Triangle Area = ½|AB × AC| in 3D', fontweight='bold')
    save_fig(fig, '03-triangle-cross-product.png')

# ════════════════════════════════════════════════════
# 04 — Disk, Washer, Shell Methods Compared
# ════════════════════════════════════════════════════
def fig_04_volume_methods():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Disk method
    ax = axes[0]
    x_disk = np.linspace(0, 4, 300)
    y_disk = np.sqrt(x_disk)
    ax.fill_between(x_disk, 0, y_disk, alpha=0.2, color='#3498DB')
    ax.plot(x_disk, y_disk, 'b-', lw=2)
    # Sample disk
    x0 = 2
    r = np.sqrt(x0)
    disk = Rectangle((x0-0.1, -r), 0.2, 2*r, fill=True, fc='#E74C3C', alpha=0.5, ec='#E74C3C', lw=1.5)
    ax.add_patch(disk)
    ax.annotate(f'R=√x', (x0+0.1, r), fontsize=9, color='#E74C3C')
    ax.set_title('DISK: V=π∫R²dx', fontweight='bold')
    ax.set_xlim(0, 4.5); ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)

    # Washer method
    ax = axes[1]
    x_w = np.linspace(0, 1, 200)
    ax.fill_between(x_w, x_w, x_w**2, alpha=0.2, color='#3498DB')
    ax.plot(x_w, x_w, 'b-', lw=2, label='y=x (outer)')
    ax.plot(x_w, x_w**2, 'g-', lw=2, label='y=x² (inner)')
    # Sample washer
    x1 = 0.6
    ax.plot([x1, x1], [x1**2, x1], '#E74C3C', lw=4)
    ax.annotate('R_outer', (x1+0.05, x1), fontsize=8, color='#E74C3C')
    ax.annotate('R_inner', (x1+0.05, x1**2+0.05), fontsize=8, color='#E74C3C')
    ax.set_title('WASHER: V=π∫(R²-r²)dx', fontweight='bold')
    ax.set_xlim(0, 1.1); ax.set_ylim(0, 1.1)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)

    # Shell method
    ax = axes[2]
    x_s = np.linspace(0, 2, 200)
    ax.fill_between(x_s, 0, x_s**2, alpha=0.2, color='#3498DB')
    ax.plot(x_s, x_s**2, 'b-', lw=2)
    # Sample shell
    x2 = 1.2
    shell = Rectangle((x2-0.05, 0), 0.1, x2**2, fill=True, fc='#E74C3C', alpha=0.5, ec='#E74C3C', lw=1.5)
    ax.add_patch(shell)
    ax.annotate('h=x²', (x2+0.05, x2**2/2), fontsize=9, color='#E74C3C')
    ax.annotate(f'x={x2:.1f}\ncirc=2πx', (x2-0.3, x2**2+0.1), fontsize=8, color='#E74C3C')
    ax.set_title('SHELL: V=2π∫x·h(x)dx', fontweight='bold')
    ax.set_xlim(0, 2.3); ax.set_ylim(0, 4.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)

    fig.suptitle('Three Volume-of-Revolution Methods', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '04-volume-methods.png')

# ════════════════════════════════════════════════════
# 05 — Washer with Shifted Axis: y=2
# ════════════════════════════════════════════════════
def fig_05_washer_shifted_axis():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, 1.1, 300)
    ax.plot(x, np.sqrt(x), 'b-', lw=2.5, label='y=√x')
    ax.plot(x, x**2, '#2ECC71', lw=2.5, label='y=x²')
    ax.fill_between(x, x**2, np.sqrt(x), alpha=0.15, color='#3498DB')

    # Axis of rotation
    ax.axhline(2, color='#E74C3C', lw=2.5, linestyle='--', zorder=2)
    ax.annotate('axis: y=2', (1.05, 2.05), fontsize=12, color='#E74C3C', fontweight='bold')

    # Show radii at x=0.5
    x0 = 0.5
    y_outer = x0**2  # farther from axis
    y_inner = np.sqrt(x0)  # closer to axis
    ax.plot([x0, x0], [y_outer, 2], '#E74C3C', lw=3, zorder=4)
    ax.plot([x0, x0], [y_inner, 2], '#E67E22', lw=3, zorder=4)
    ax.annotate(f'R_outer=2-x²\n={2-y_outer:.2f}', (x0+0.03, (y_outer+2)/2),
                fontsize=9, color='#E74C3C')
    ax.annotate(f'R_inner=2-√x\n={2-y_inner:.2f}', (x0+0.03, (y_inner+2)/2),
                fontsize=9, color='#E67E22')

    ax.set_xlim(-0.05, 1.3); ax.set_ylim(-0.1, 2.5)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.25)
    ax.set_title('Washer Method — Shifted Axis (y=2)', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '05-washer-shifted-axis.png')

# ════════════════════════════════════════════════════
# 06 — Sphere Volume Derivation
# ════════════════════════════════════════════════════
def fig_06_sphere_volume():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    R = 3
    # Left: generating curve
    x = np.linspace(-R, R, 400)
    y = np.sqrt(R**2 - x**2)
    ax1.plot(x, y, 'b-', lw=3)
    ax1.plot(x, -y, 'b-', lw=3)
    ax1.fill_between(x, -y, y, alpha=0.1, color='#3498DB')

    # Sample disk
    x0 = 1.2
    r0 = np.sqrt(R**2 - x0**2)
    ax1.plot([x0, x0], [-r0, r0], '#E74C3C', lw=3)
    ax1.annotate(f'R(x)=√(R²-x²)', (x0+0.1, r0/2), fontsize=9, color='#E74C3C')

    ax1.set_aspect('equal'); ax1.set_xlim(-4, 4); ax1.set_ylim(-4, 4)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.grid(True, alpha=0.2)
    ax1.set_title('Rotate semicircle about x-axis', fontweight='bold')
    ax1.set_xlabel('x'); ax1.set_ylabel('y')

    # Right: volume accumulation
    xV = np.linspace(-R-0.5, R+0.5, 500)
    # V(x) for partial volume from -R to x: π(R²x - x³/3 + 2R³/3)
    V_x = np.pi * (R**2 * xV - xV**3/3 + 2*R**3/3)
    V_x = np.clip(V_x, 0, 4/3*np.pi*R**3)
    ax2.plot(xV, V_x, 'b-', lw=2.5)
    ax2.axhline(4/3*np.pi*R**3, color='#E74C3C', lw=1.5, linestyle='--')
    ax2.annotate(f'V={4/3}πR³={4/3*np.pi*R**3:.1f}', (R, 4/3*np.pi*R**3-5),
                 fontsize=11, color='#E74C3C', fontweight='bold', ha='right')
    ax2.set_xlim(-R-0.5, R+0.5); ax2.set_ylim(0, 130)
    ax2.grid(True, alpha=0.25)
    ax2.set_title('V = π∫(R²-x²)dx = (4/3)πR³', fontweight='bold')
    ax2.set_xlabel('x'); ax2.set_ylabel('V(x)')

    fig.suptitle('Sphere Volume via Disk Method', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '06-sphere-volume.png')

# ════════════════════════════════════════════════════
# 07 — Torus Volume
# ════════════════════════════════════════════════════
def fig_07_torus():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    R, r = 4, 1.5
    # Left: generating circle
    theta = np.linspace(0, 2*np.pi, 300)
    cx, cy = R, 0
    ax1.plot(cx + r*np.cos(theta), cy + r*np.sin(theta), 'b-', lw=3)
    ax1.plot(0, 0, 'ko', ms=8)
    ax1.annotate('y-axis\n(rotation axis)', (0, 0), textcoords="offset points", xytext=(-25, -25), fontsize=9)
    ax1.fill_between([R-r, R+r], -r, r, alpha=0.08, color='#3498DB')

    # Shell at position x
    x0 = R + r/2
    y_shell = np.sqrt(r**2 - (x0-R)**2)
    ax1.plot([x0, x0], [-y_shell, y_shell], '#E74C3C', lw=3)
    ax1.annotate(f'x={x0:.1f}', (x0, -y_shell-0.4), fontsize=9, ha='center', color='#E74C3C')
    ax1.annotate('R', (R/2, -0.2), fontsize=11, fontweight='bold')
    ax1.annotate('r', (R, r/2), fontsize=11, fontweight='bold')

    ax1.set_aspect('equal'); ax1.set_xlim(-1, 7); ax1.set_ylim(-3, 3)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.grid(True, alpha=0.2)
    ax1.set_title('Cross-section: Shell method', fontweight='bold')
    ax1.set_xlabel('x'); ax1.set_ylabel('y')

    # Right: Pappus Theorem visualization
    ax2.add_patch(Circle((0, 0), R, fill=False, ec='gray', lw=1.5, linestyle='--', alpha=0.5))
    # The generating circle centroid travels along the dashed circle
    ax2.add_patch(Circle((R, 0), r, fill=True, fc='#E74C3C', alpha=0.3, ec='#E74C3C', lw=2))
    # Centroid path
    theta_p = np.linspace(0, 2*np.pi, 200)
    ax2.plot(R*np.cos(theta_p), R*np.sin(theta_p), '--', color='#8E44AD', lw=2)
    ax2.arrow(np.pi/4, 0.5, 0, 0, color='#8E44AD', lw=1)  # dummy for annotation
    ax2.annotate('centroid\npath: 2πR', (R+0.3, 0), fontsize=10, color='#8E44AD', fontweight='bold')

    ax2.text(0, -R-1.2, f'V = (πr²)·(2πR)\n  = 2π²Rr²\n  = {2*np.pi**2*R*r**2:.1f}',
             fontsize=13, fontweight='bold', ha='center',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    ax2.set_aspect('equal'); ax2.set_xlim(-6, 6); ax2.set_ylim(-6, 4)
    ax2.axhline(0, color='gray', lw=0.5); ax2.axvline(0, color='gray', lw=0.5)
    ax2.grid(True, alpha=0.2)
    ax2.set_title("Pappus: V = Area × centroid's path", fontweight='bold')

    fig.suptitle('Torus Volume: Shell Method & Pappus Theorem', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '07-torus.png')

# ════════════════════════════════════════════════════
# 08 — Determinant = Area Scaling Factor
# ════════════════════════════════════════════════════
def fig_08_determinant_area():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5))

    # Left: unit square
    square_pts = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    ax1.plot(square_pts[:, 0], square_pts[:, 1], 'b-', lw=2.5)
    ax1.fill(square_pts[:, 0], square_pts[:, 1], alpha=0.15, color='#3498DB')
    ax1.annotate('Area = 1', (0.5, 0.5), fontsize=12, ha='center', fontweight='bold')
    ax1.annotate('e₁=(1,0)', (1.05, 0.05), fontsize=9)
    ax1.annotate('e₂=(0,1)', (0.05, 1.05), fontsize=9)
    ax1.set_aspect('equal'); ax1.set_xlim(-0.5, 4); ax1.set_ylim(-0.5, 4)
    ax1.grid(True, alpha=0.2)
    ax1.set_title('Unit Square: Area = 1', fontweight='bold')

    # Right: transformed parallelogram
    M = np.array([[3, 1], [1, 2]])
    c1, c2 = M[:, 0], M[:, 1]
    para_pts = np.array([[0, 0], c1, c1+c2, c2, [0, 0]])
    ax2.plot(para_pts[:, 0], para_pts[:, 1], '#E74C3C', lw=2.5)
    ax2.fill(para_pts[:, 0], para_pts[:, 1], alpha=0.2, color='#E74C3C')
    det = np.linalg.det(M)
    ax2.annotate(f'Area = |det(M)| = {det:.0f}', (c1[0]/2, c2[1]/2),
                 fontsize=12, ha='center', fontweight='bold', color='#E74C3C')
    ax2.annotate(f'col₁=({c1[0]},{c1[1]})', (c1[0], c1[1]), textcoords="offset points",
                 xytext=(5, 5), fontsize=9, color='#E74C3C')
    ax2.annotate(f'col₂=({c2[0]},{c2[1]})', (c2[0], c2[1]), textcoords="offset points",
                 xytext=(5, 5), fontsize=9, color='#E74C3C')
    ax2.set_aspect('equal'); ax2.set_xlim(-0.5, 5); ax2.set_ylim(-0.5, 4)
    ax2.grid(True, alpha=0.2)
    ax2.set_title(f'M=[[3,1],[1,2]], det(M)={det:.0f}', fontweight='bold')

    fig.suptitle('Determinant = Area Scaling Factor', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '08-determinant-area.png')

# ════════════════════════════════════════════════════
# 09 — Cross-Section Volume (Equilateral Triangles)
# ════════════════════════════════════════════════════
def fig_09_cross_section_volume():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Base region: y=x² and y=1
    x = np.linspace(-1, 1, 300)
    ax.fill_between(x, x**2, 1, alpha=0.15, color='#3498DB')
    ax.plot(x, x**2, 'b-', lw=2.5, label='y=x²')
    ax.plot(x, np.ones_like(x), '#2ECC71', lw=2, label='y=1')

    # Sample cross-section (equilateral triangle at height y)
    for y0 in [0.3, 0.6, 0.85]:
        half_w = np.sqrt(y0)
        # Draw triangle above the base
        side = 2*half_w
        h_tri = side * np.sqrt(3)/2
        # Show triangle as polygon pointing up from the base
        tri_pts = np.array([[-half_w, y0], [half_w, y0], [0, y0+h_tri], [-half_w, y0]])
        ax.plot(tri_pts[:, 0], tri_pts[:, 1], '#E74C3C', lw=1.5, alpha=0.7)
        ax.fill(tri_pts[:, 0], tri_pts[:, 1], alpha=0.1, color='#E74C3C')
        ax.plot([-half_w, half_w], [y0, y0], '#E74C3C', lw=2.5, alpha=0.7)

    ax.annotate('equilateral\ntriangle\ncross-sections', (0.35, 0.7), fontsize=10,
                color='#E74C3C', fontweight='bold')
    ax.annotate('V = ∫A(y)dy\nA(y) = √3·y', (-0.9, 1.1), fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-0.1, 1.8)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.2)
    ax.set_title('Volume by Cross-Sections: Equilateral Triangles', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '09-cross-section-volume.png')

# ════════════════════════════════════════════════════
# 10 — Area via Parametric: Ellipse
# ════════════════════════════════════════════════════
def fig_10_parametric_ellipse_area():
    fig, ax = plt.subplots(figsize=(8, 8))
    a, b = 3, 2
    t = np.linspace(0, 2*np.pi, 400)
    ax.plot(a*np.cos(t), b*np.sin(t), 'b-', lw=3)

    # Fill
    ax.fill(a*np.cos(t), b*np.sin(t), alpha=0.15, color='#3498DB')

    # Upper half shading (darker)
    t_upper = np.linspace(0, np.pi, 200)
    ax.fill_between(a*np.cos(t_upper), 0, b*np.sin(t_upper), alpha=0.15, color='#E74C3C')

    ax.annotate(f'Area = πab\n= π·{a}·{b}\n= {np.pi*a*b:.1f}', (0, 0), fontsize=14,
                fontweight='bold', ha='center', color='#E74C3C')
    ax.annotate(f'a={a}', (a/2, 0.15), fontsize=11, fontweight='bold')
    ax.annotate(f'b={b}', (0.15, b/2), fontsize=11, fontweight='bold')

    ax.set_aspect('equal'); ax.set_xlim(-4, 4); ax.set_ylim(-3, 3)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.2)
    ax.set_title('Ellipse Area via Parametric: A=πab', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '10-parametric-ellipse-area.png')

if __name__ == '__main__':
    print("Generating 17A graphs...")
    fig_01_area_between_curves()
    fig_02_polar_rose()
    fig_03_triangle_cross_product()
    fig_04_volume_methods()
    fig_05_washer_shifted_axis()
    fig_06_sphere_volume()
    fig_07_torus()
    fig_08_determinant_area()
    fig_09_cross_section_volume()
    fig_10_parametric_ellipse_area()
    print("Done! 10 graphs generated.")
