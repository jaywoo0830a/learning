#!/usr/bin/env python3
"""Generate all graph images for Session 12C3: Coordinate Systems and Optimization.

New graphs for 0721 refresh — leveraging 9B/9C prerequisite knowledge.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/12C3"
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    'figure.dpi': 150,
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
})

def save(name):
    plt.tight_layout(pad=1.5)
    plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"  ✓ {name}")

# ============================================================
# 12c3a-polar-curves.png
# ============================================================
def fig_polar_curves():
    """Polar curves: cardioid r = 1 + cos θ and rose r = sin(3θ).
    Shows both polar and Cartesian views.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 11))

    theta = np.linspace(0, 2*np.pi, 500)

    # (1) Cardioid in polar
    ax = axes[0, 0]
    r = 1 + np.cos(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.fill(x, y, alpha=0.15, color='red')
    ax.plot(x, y, 'r-', lw=2.5)
    ax.set_title('Cardioid: $r = 1 + \\cos\\theta$', fontweight='bold')
    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)

    # (2) Cardioid in Cartesian for comparison
    ax = axes[0, 1]
    # Plot r vs θ to show simplicity
    ax.plot(theta, 1+np.cos(theta), 'r-', lw=2.5)
    ax.axhline(0, color='gray', lw=0.5)
    ax.set_title('$r = 1 + \\cos\\theta$ in $(\\theta, r)$', fontweight='bold')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-0.5, 2.5)
    ax.set_xlabel('$\\theta$'); ax.set_ylabel('$r$')
    ax.grid(True, alpha=0.3)

    # (3) Rose in polar
    ax = axes[1, 0]
    r = np.sin(3*theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.fill(x, y, alpha=0.15, color='blue')
    ax.plot(x, y, 'b-', lw=2.5)
    ax.set_title('Rose: $r = \\sin(3\\theta)$', fontweight='bold')
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)

    # (4) Rose in Cartesian
    ax = axes[1, 1]
    ax.plot(theta, np.sin(3*theta), 'b-', lw=2.5)
    ax.axhline(0, color='gray', lw=0.5)
    ax.set_title('$r = \\sin(3\\theta)$ in $(\\theta, r)$', fontweight='bold')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('$\\theta$'); ax.set_ylabel('$r$')
    ax.grid(True, alpha=0.3)

    fig.suptitle('Polar Curves: Simple in $(r,\\theta)$, Complex in $(x,y)$',
                 fontsize=14, fontweight='bold', y=1.01)
    save('12c3a-polar-curves.png')


# ============================================================
# 12c3b-spherical-coords.png
# ============================================================
def fig_spherical_coords():
    """Spherical coordinates on the unit sphere with labeled components.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    phi = np.pi/3   # polar angle (from z-axis)
    theta = np.pi/4  # azimuthal angle

    # Point on sphere
    rho = 1
    px = rho * np.sin(phi) * np.cos(theta)
    py = rho * np.sin(phi) * np.sin(theta)
    pz = rho * np.cos(phi)

    # Sphere wireframe
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi, 25)
    X = np.outer(np.cos(u), np.sin(v))
    Y = np.outer(np.sin(u), np.sin(v))
    Z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(X, Y, Z, alpha=0.1, color='blue', lw=0.3)

    # Point
    ax.plot([px], [py], [pz], 'ro', markersize=12, zorder=10)

    # Radial line from origin
    ax.plot([0, px], [0, py], [0, pz], 'r-', lw=2, alpha=0.7)

    # Projection onto xy-plane
    ax.plot([px, px], [py, py], [0, pz], color='gray', linestyle='--', lw=1.5, alpha=0.5)
    ax.plot([0, px], [0, py], [0, 0], 'g-', lw=2, alpha=0.7)

    # Azimuth angle arc (in xy-plane)
    arc_t = np.linspace(0, theta, 40)
    r_arc = 0.4
    ax.plot(r_arc*np.cos(arc_t), r_arc*np.sin(arc_t), np.zeros(40),
            'green', lw=2)
    ax.text(0.5, 0.25, 0, '$\\theta$', fontsize=14, color='green',
            fontweight='bold')

    # Polar angle arc
    arc_pts = np.linspace(0, phi, 40)
    r_arc2 = 0.4
    ax.plot(r_arc2*np.sin(arc_pts)*np.cos(theta),
            r_arc2*np.sin(arc_pts)*np.sin(theta),
            r_arc2*np.cos(arc_pts), 'purple', lw=2)
    ax.text(0.15, 0.15, 0.5, '$\\phi$', fontsize=14, color='purple',
            fontweight='bold')

    # Labels
    ax.text(px+0.1, py+0.1, pz+0.1, f'P($\\rho$={rho}, $\\phi$={phi:.2f}, $\\theta$={theta:.2f})',
            fontsize=10, fontweight='bold')
    ax.text(0.6, 0, 0, '$\\rho$', fontsize=12, color='red', fontweight='bold')

    # Axes
    ax.quiver(0, 0, 0, 1.6, 0, 0, color='gray', lw=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1.6, 0, color='gray', lw=1, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1.6, color='gray', lw=1, arrow_length_ratio=0.1)
    ax.text(1.7, 0, 0, 'x', fontsize=12)
    ax.text(0, 1.7, 0, 'y', fontsize=12)
    ax.text(0, 0, 1.7, 'z', fontsize=12)

    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_zlim(-1.5, 1.5)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Spherical Coordinates $(\\rho, \\phi, \\theta)$\non the Unit Sphere',
                 fontweight='bold', fontsize=13)
    ax.view_init(elev=20, azim=-50)
    save('12c3b-spherical-coords.png')


# ============================================================
# 12c3c-convex-hull.png
# ============================================================
def fig_convex_hull():
    """Convex hull of a set of points — the smallest convex polygon.
    """
    np.random.seed(42)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Generate random points
    points = np.random.rand(20, 2) * 8 + 1

    # Compute convex hull (simple method using angle sorting)
    def convex_hull(points):
        pts = points.copy()
        # Find lowest point
        start = pts[np.argmin(pts[:, 1])]
        # Sort by angle
        angles = np.arctan2(pts[:, 1] - start[1], pts[:, 0] - start[0])
        pts = pts[np.argsort(angles)]
        return pts

    hull = convex_hull(points)

    # Left: Points only
    ax1.scatter(points[:, 0], points[:, 1], c='blue', s=50, zorder=5)
    ax1.scatter(hull[0, 0], hull[0, 1], c='green', s=80, zorder=6, marker='s')
    ax1.set_title('Set of Points', fontweight='bold')
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)

    # Right: Convex hull
    ax2.scatter(points[:, 0], points[:, 1], c='blue', s=50, zorder=5, label='points')
    ax2.scatter(hull[0, 0], hull[0, 1], c='green', s=80, zorder=6, marker='s',
                label='lowest point')

    # Draw hull
    hull_closed = np.vstack([hull, hull[0]])
    ax2.fill(hull_closed[:, 0], hull_closed[:, 1], alpha=0.15, color='red')
    ax2.plot(hull_closed[:, 0], hull_closed[:, 1], 'r-', lw=2.5, label='convex hull')

    # Mark interior vs hull points
    # (Simplified: just show all points)
    for i, pt in enumerate(points):
        # Check if point is a hull vertex (approximate)
        dists = np.min(np.sqrt(np.sum((hull - pt)**2, axis=1)))
        if dists < 0.01:
            ax2.plot(pt[0], pt[1], 'ro', markersize=8)
        else:
            ax2.plot(pt[0], pt[1], 'bs', markersize=6, alpha=0.5)

    ax2.set_title('Convex Hull: Smallest Enclosing Polygon', fontweight='bold')
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9, loc='upper left')

    fig.suptitle('Convex Hull — The Outer Boundary of Points',
                 fontsize=14, fontweight='bold')
    save('12c3c-convex-hull.png')


# ============================================================
# 12c3d-point-line-distance.png
# ============================================================
def fig_point_line_distance():
    """Distance from point to line — 2D and 3D comparison.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(14, 6))

    # Left: 2D
    ax1 = fig.add_subplot(1, 2, 1)
    x = np.linspace(-2, 6, 100)
    # Line: 3x + 4y = 10
    ax1.plot(x, (10-3*x)/4, 'b-', lw=2.5, label='line: $3x+4y=10$')
    # Point P(3, 4)
    ax1.plot(3, 4, 'ro', markersize=10, zorder=5)
    ax1.text(3.2, 4.3, 'P(3,4)', fontsize=11, fontweight='bold', color='red')
    # Perpendicular distance
    foot_x, foot_y = 1.2, 1.6
    ax1.plot([3, foot_x], [4, foot_y], 'r--', lw=2.5)
    ax1.plot(foot_x, foot_y, 'go', markersize=8)
    ax1.text(2, 3, 'd = 3', fontsize=13, color='red', fontweight='bold')
    # Normal vector
    ax1.quiver(foot_x, foot_y, 3, 4, angles='xy', scale_units='xy', scale=1,
               color='purple', width=0.012, alpha=0.6, label='n=(3,4)')
    ax1.set_title('2D: $d = \\frac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}$',
                  fontweight='bold', fontsize=12)
    ax1.set_xlim(-1, 6); ax1.set_ylim(-1, 6)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.legend(fontsize=9)

    # Right: 3D
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    # Line through (0,0,0) with direction (1,1,1)
    t = np.linspace(-1, 3, 100)
    ax2.plot(t, t, t, 'b-', lw=2.5, label='line: $\\vec{r}(t) = t(1,1,1)$')
    # Point P(2, 1, 0)
    ax2.plot([2], [1], [0], 'ro', markersize=10, zorder=5)
    ax2.text(2.2, 1.2, 0.2, 'P(2,1,0)', fontsize=11, color='red', fontweight='bold')
    # Perpendicular distance and foot
    # d = |v × d| / |d|
    v = np.array([2, 1, 0])
    d_dir = np.array([1, 1, 1])
    v_perp = v - np.dot(v, d_dir) / np.dot(d_dir, d_dir) * d_dir
    foot = v - v_perp
    d = np.linalg.norm(v_perp)
    ax2.plot([2, foot[0]], [1, foot[1]], [0, foot[2]], 'r--', lw=2.5)
    ax2.plot(foot[0], foot[1], foot[2], 'go', markersize=8)
    ax2.text(foot[0], foot[1], foot[2]+0.2,
             f'd = {d:.2f}', fontsize=12, color='red', fontweight='bold')
    # Perpendicular component
    ax2.quiver(foot[0], foot[1], foot[2],
               v_perp[0], v_perp[1], v_perp[2],
               color='purple', lw=2, arrow_length_ratio=0.2, label='v⊥')

    ax2.set_title('3D: $d = \\frac{|\\vec{v} \\times \\vec{d}|}{|\\vec{d}|}$',
                  fontweight='bold', fontsize=12)
    ax2.set_xlim(-1, 3); ax2.set_ylim(-1, 3); ax2.set_zlim(-1, 3)
    ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('Z')
    ax2.legend(fontsize=9)
    ax2.view_init(elev=20, azim=-60)

    fig.suptitle('Distance from Point to Line — 2D vs 3D',
                 fontsize=14, fontweight='bold')
    save('12c3d-point-line-distance.png')


# ============================================================
# 12c3e-coordinate-systems-comparison.png  [NEW]
# ============================================================
def fig_coordinate_systems_comparison():
    """Comparison of Cartesian, polar, cylindrical, and spherical coordinates.
    Shows how the same point looks in each system.
    """
    fig = plt.figure(figsize=(15, 10))

    # Same point in different systems
    # Cartesian: (3, 4, 5)
    x0, y0, z0 = 3, 4, 5
    # Polar: r = 5, θ = arctan(4/3)
    r0 = np.sqrt(x0**2 + y0**2)
    theta0 = np.arctan2(y0, x0)
    # Spherical: ρ = √(x²+y²+z²) = √50 ≈ 7.07
    rho0 = np.sqrt(x0**2 + y0**2 + z0**2)
    phi0 = np.arccos(z0/rho0)

    # 1) Cartesian 2D
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.plot(3, 4, 'ro', markersize=10)
    ax1.plot([0, 3], [0, 0], color='gray', linestyle='--', lw=1)
    ax1.plot([3, 3], [0, 4], color='gray', linestyle='--', lw=1)
    ax1.text(3.5, 4.2, 'P(3, 4)', fontsize=12, fontweight='bold', color='red')
    ax1.set_title('Cartesian $(x, y)$\n$x$=3, $y$=4', fontweight='bold')
    ax1.set_xlim(-1, 6); ax1.set_ylim(-1, 6)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)

    # 2) Polar 2D
    ax2 = fig.add_subplot(2, 3, 2, projection='polar')
    ax2.plot(theta0, r0, 'ro', markersize=10)
    ax2.plot([0, theta0], [0, r0], 'r-', lw=2, alpha=0.5)
    ax2.set_title(f'Polar $(r, \\theta)$\n$r$={r0:.1f}, $\\theta$={theta0:.2f}',
                  fontweight='bold', va='bottom')
    ax2.set_rlim(0, 6)

    # 3) Comparison
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.axis('off')
    info = (
        "Same Point, Different Coordinates:\n\n"
        f"Cartesian:  ({x0}, {y0}, {z0})\n\n"
        f"Polar (2D): r = {r0:.1f}, θ = {np.degrees(theta0):.1f}°\n\n"
        f"Cylindrical: r = {r0:.1f}, θ = {np.degrees(theta0):.1f}°, z = {z0}\n\n"
        f"Spherical: ρ = {rho0:.2f}, φ = {np.degrees(phi0):.1f}°, θ = {np.degrees(theta0):.1f}°"
    )
    ax3.text(0.1, 0.5, info, transform=ax3.transAxes, fontsize=12, fontfamily='monospace',
             verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))
    ax3.set_title('Coordinate Conversion', fontweight='bold', fontsize=12)

    # 4) Cartesian 3D
    from mpl_toolkits.mplot3d import Axes3D
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')
    ax4.plot([x0], [y0], [z0], 'ro', markersize=10)
    # Projection lines
    ax4.plot([x0, x0], [y0, y0], [0, z0], color='gray', linestyle='--', lw=1, alpha=0.5)
    ax4.plot([0, x0], [0, y0], [0, 0], color='gray', linestyle='--', lw=1, alpha=0.5)
    ax4.text(x0+0.3, y0+0.3, z0+0.3, f'({x0},{y0},{z0})', fontsize=10, color='red')
    ax4.quiver(0, 0, 0, 7, 0, 0, color='gray', lw=0.8, arrow_length_ratio=0.05)
    ax4.quiver(0, 0, 0, 0, 6, 0, color='gray', lw=0.8, arrow_length_ratio=0.05)
    ax4.quiver(0, 0, 0, 0, 0, 6, color='gray', lw=0.8, arrow_length_ratio=0.05)
    ax4.set_title('Cartesian $(x, y, z)$', fontweight='bold')
    ax4.set_xlabel('X'); ax4.set_ylabel('Y'); ax4.set_zlabel('Z')
    ax4.view_init(elev=20, azim=-60)

    # 5) Spherical 3D
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')
    u = np.linspace(0, 2*np.pi, 25)
    v = np.linspace(0, np.pi, 20)
    ax5.plot_wireframe(np.outer(np.cos(u), np.sin(v))*rho0,
                       np.outer(np.sin(u), np.sin(v))*rho0,
                       np.outer(np.ones(np.size(u)), np.cos(v))*rho0,
                       alpha=0.08, color='blue', lw=0.3)
    ax5.plot([x0], [y0], [z0], 'ro', markersize=10)
    ax5.plot([0, x0], [0, y0], [0, z0], 'r-', lw=2, alpha=0.5)
    ax5.text(x0+0.3, y0+0.3, z0+0.3,
             f'ρ={rho0:.1f}', fontsize=10, color='red', fontweight='bold')
    ax5.set_title(f'Spherical $(\\rho, \\phi, \\theta)$\nρ={rho0:.2f}',
                  fontweight='bold')
    ax5.set_xlim(-rho0, rho0); ax5.set_ylim(-rho0, rho0); ax5.set_zlim(-rho0, rho0)
    ax5.view_init(elev=20, azim=-60)

    # 6) Legend/Summary
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.axis('off')
    formulas = (
        "Conversion Formulas:\n\n"
        "Polar $\\to$ Cartesian:\n"
        "$x = r\\cos\\theta$, $y = r\\sin\\theta$\n\n"
        "Cylindrical $\\to$ Cartesian:\n"
        "$x = r\\cos\\theta$, $y = r\\sin\\theta$, $z = z$\n\n"
        "Spherical $\\to$ Cartesian:\n"
        "$x = \\rho\\sin\\phi\\cos\\theta$\n"
        "$y = \\rho\\sin\\phi\\sin\\theta$\n"
        "$z = \\rho\\cos\\phi$"
    )
    ax6.text(0.1, 0.5, formulas, transform=ax6.transAxes, fontsize=11,
             fontfamily='monospace', verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='#e8f0e8', alpha=0.8))

    fig.suptitle('Coordinate Systems Compared',
                 fontsize=14, fontweight='bold', y=1.01)
    save('12c3e-coordinate-systems-comparison.png')


# ============================================================
# 12c3f-lagrange-optimization.png  [NEW]
# ============================================================
def fig_lagrange_optimization():
    """Lagrange multipliers: closest point on a plane to the origin.
    Shows the plane, the constraint, level sets of distance, and the optimum.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Plane: 2x + 3y + z = 6
    xx, yy = np.meshgrid(np.linspace(-1, 4, 20), np.linspace(-1, 4, 20))
    zz = (6 - 2*xx - 3*yy)
    zz = np.clip(zz, -2, 6)
    ax.plot_surface(xx, yy, zz, alpha=0.3, color='lightblue')

    # Level sets of distance (spheres) — use curves on the plane
    # The closest point is along the normal
    n = np.array([2, 3, 1])
    d = 6
    closest = d / np.dot(n, n) * n  # = (6/14)*(2,3,1) = (6/7, 9/7, 3/7)

    # Mark closest point
    ax.plot([closest[0]], [closest[1]], [closest[2]], 'ro', markersize=12, zorder=10)
    ax.text(closest[0]+0.2, closest[1]+0.2, closest[2],
            f'Closest: ({closest[0]:.2f}, {closest[1]:.2f}, {closest[2]:.2f})',
            fontsize=10, color='red', fontweight='bold')

    # Normal from origin
    ax.plot([0, closest[0]], [0, closest[1]], [0, closest[2]], 'r--', lw=2.5)

    # Sphere at the tangent point
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi, 25)
    R = np.linalg.norm(closest)
    Xs = R * np.outer(np.cos(u), np.sin(v))
    Ys = R * np.outer(np.sin(u), np.sin(v))
    Zs = R * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(Xs, Ys, Zs, alpha=0.08, color='green', lw=0.4)

    # Gradient vectors
    ax.quiver(closest[0], closest[1], closest[2],
              2, 3, 1, color='purple', lw=2.5, arrow_length_ratio=0.15,
              label='$\\nabla g = \\vec{n}$')
    ax.quiver(closest[0], closest[1], closest[2],
              closest[0], closest[1], closest[2],
              color='darkgreen', lw=2.5, arrow_length_ratio=0.15,
              label='$\\nabla f = 2\\vec{p}$')

    # Origin
    ax.plot([0], [0], [0], 'ko', markersize=8)

    ax.set_xlim(-0.5, 4); ax.set_ylim(-0.5, 4); ax.set_zlim(-1, 5)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Geometric Optimization: Closest Point on Plane\n'
                 '$\\nabla f \\parallel \\nabla g$ at optimum',
                 fontweight='bold', fontsize=11)
    ax.legend(fontsize=9)
    ax.view_init(elev=20, azim=-55)
    save('12c3f-lagrange-optimization.png')


# ============================================================
# 12c3g-barycentric-coords.png  [NEW]
# ============================================================
def fig_barycentric_coords():
    """Barycentric coordinates inside a triangle — area-based visualization.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Triangle vertices
    A, B, C = np.array([0, 0]), np.array([6, 0]), np.array([2, 5])
    tri = np.array([A, B, C, A])

    # Left: Barycentric coordinates shown as areas
    ax1.plot(tri[:, 0], tri[:, 1], 'k-', lw=2.5)
    ax1.text(A[0]-0.3, A[1]-0.3, 'A', fontsize=14, fontweight='bold')
    ax1.text(B[0]+0.1, B[1]-0.3, 'B', fontsize=14, fontweight='bold')
    ax1.text(C[0]-0.1, C[1]+0.2, 'C', fontsize=14, fontweight='bold')

    # Point inside with barycentric (0.5, 0.3, 0.2)
    alpha, beta, gamma = 0.5, 0.3, 0.2
    P = alpha*A + beta*B + gamma*C
    ax1.plot(P[0], P[1], 'ro', markersize=10, zorder=5)
    ax1.text(P[0]+0.2, P[1]+0.2, f'P({alpha},{beta},{gamma})',
             fontsize=11, color='red', fontweight='bold')

    # Sub-triangles colored
    sub_tris = [
        (P, B, C, 'red', 'α = Area(PBC)/Area(ABC)'),
        (A, P, C, 'blue', 'β = Area(APC)/Area(ABC)'),
        (A, B, P, 'green', 'γ = Area(ABP)/Area(ABC)'),
    ]
    for pts_list in sub_tris:
        poly = np.array([pts_list[0], pts_list[1], pts_list[2], pts_list[0]])
        ax1.fill(poly[:, 0], poly[:, 1], alpha=0.15, color=pts_list[3])

    ax1.set_title('Barycentric Coordinates as Area Ratios\n'
                  '$\\vec{P} = \\alpha\\vec{A} + \\beta\\vec{B} + \\gamma\\vec{C}$',
                  fontweight='bold', fontsize=11)
    ax1.set_xlim(-1, 7); ax1.set_ylim(-1, 6)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)

    # Right: Color interpolation
    ax2.plot(tri[:, 0], tri[:, 1], 'k-', lw=2.5)
    # Fill with interpolated colors
    xs = np.linspace(0, 6, 40)
    ys = np.linspace(0, 5, 35)
    for x in xs:
        for y in ys:
            # Check if inside triangle
            # Compute barycentric coords
            denom = (B[1]-C[1])*(A[0]-C[0]) + (C[0]-B[0])*(A[1]-C[1])
            a = ((B[1]-C[1])*(x-C[0]) + (C[0]-B[0])*(y-C[1])) / denom
            b = ((C[1]-A[1])*(x-C[0]) + (A[0]-C[0])*(y-C[1])) / denom
            c = 1 - a - b
            if a >= -0.01 and b >= -0.01 and c >= -0.01:
                # Interpolate RGB: A=red, B=green, C=blue
                rgb = [min(1, max(0, a*0.8+0.2)),
                       min(1, max(0, b*0.8+0.2)),
                       min(1, max(0, c*0.8+0.2))]
                ax2.plot(x, y, 's', markersize=3, color=rgb)

    ax2.text(A[0]-0.3, A[1]-0.3, 'A', fontsize=14, fontweight='bold')
    ax2.text(B[0]+0.1, B[1]-0.3, 'B', fontsize=14, fontweight='bold')
    ax2.text(C[0]-0.1, C[1]+0.2, 'C', fontsize=14, fontweight='bold')
    ax2.set_title('Application: Color Interpolation\n(Gouraud Shading)',
                  fontweight='bold', fontsize=11)
    ax2.set_xlim(-1, 7); ax2.set_ylim(-1, 6)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)

    fig.suptitle('Barycentric Coordinates — Inside a Triangle',
                 fontsize=14, fontweight='bold')
    save('12c3g-barycentric-coords.png')


# ============================================================
# 12c3h-skew-lines-distance.png  [NEW]
# ============================================================
def fig_skew_lines_distance():
    """Distance between two skew lines in 3D — the common perpendicular.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    # Line 1: through (0,0,0) with direction (1,0,0) — x-axis
    t = np.linspace(-1, 3, 100)
    ax.plot(t, np.zeros(100), np.zeros(100), 'b-', lw=2.5, label='L₁: x-axis')

    # Line 2: through (0,1,1) with direction (0,0,1) — parallel to z-axis
    s = np.linspace(-0.5, 2.5, 100)
    ax.plot(np.zeros(100), np.ones(100), s, 'r-', lw=2.5, label='L₂: through (0,1,1)')

    # The common perpendicular
    # L1 dir = (1,0,0), L2 dir = (0,0,1)
    # vector between lines at closest: (0,1,1) - (0,0,0) = (0,1,1)
    # perpendicular direction = d1 × d2 = (0,-1,0)
    # Project (0,1,1) onto (0,-1,0): (0,1,0)
    # So shortest segment connects (0,0,0) on L1 and (0,1,1) on L2
    ax.plot([0, 0], [0, 1], [0, 1], 'r--', lw=3, label='shortest distance = 1')
    ax.plot([0], [0], [0], 'go', markersize=8)
    ax.plot([0], [1], [1], 'go', markersize=8)

    ax.text(0, 0.5, 0.5, 'd = 1', fontsize=14, color='red', fontweight='bold')

    ax.set_xlim(-1, 3); ax.set_ylim(-0.5, 2); ax.set_zlim(-0.5, 2)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Distance Between Skew Lines\nCommon Perpendicular Segment',
                 fontweight='bold', fontsize=12)
    ax.legend(fontsize=9)
    ax.view_init(elev=20, azim=-60)
    save('12c3h-skew-lines-distance.png')


# ============================================================
if __name__ == "__main__":
    print("Generating 12C3 graphs...")
    fig_polar_curves()
    fig_spherical_coords()
    fig_convex_hull()
    fig_point_line_distance()
    fig_coordinate_systems_comparison()
    fig_lagrange_optimization()
    fig_barycentric_coords()
    fig_skew_lines_distance()
    print("Done! ✓")
