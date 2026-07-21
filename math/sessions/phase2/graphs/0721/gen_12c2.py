#!/usr/bin/env python3
"""Generate all graph images for Session 12C2: Parametric Curves and Surfaces.

New graphs for 0721 refresh — leveraging 9B/9C prerequisite knowledge.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/12C2"
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
# 12c2a-helix.png
# ============================================================
def fig_helix():
    """Circular helix with projection onto xy-plane.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(0, 6*np.pi, 500)
    x = np.cos(t)
    y = np.sin(t)
    z = t

    # Main helix
    ax.plot(x, y, z, 'b-', lw=2.5, label='helix')
    # Projection onto xy-plane
    ax.plot(x, y, np.zeros_like(z), color='gray', linestyle='--', lw=1.2, alpha=0.5, label='xy-projection (circle)')

    # Highlight one full turn (pitch)
    idx = np.where((t >= 2*np.pi) & (t <= 4*np.pi))
    ax.plot(x[idx], y[idx], z[idx], 'orange', lw=3.5, label='one turn (pitch=2π)')

    # Vertical lines at start/end of highlighted turn
    ax.plot([1, 1], [0, 0], [2*np.pi, 4*np.pi], 'orange', lw=1.5, linestyle=':', alpha=0.7)
    ax.text(1.2, 0, 3*np.pi, 'pitch = 2π', fontsize=11, color='orange', fontweight='bold')

    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_zlim(0, 6*np.pi)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Circular Helix\n$\\vec{r}(t) = (\\cos t,\\; \\sin t,\\; t)$',
                 fontweight='bold', fontsize=13)
    ax.legend(fontsize=9)
    ax.view_init(elev=20, azim=-60)
    save('12c2a-helix.png')


# ============================================================
# 12c2b-bezier-cubic.png
# ============================================================
def fig_bezier_cubic():
    """Cubic Bézier curve with control polygon.
    Shows linear, quadratic, and cubic Béziers side by side.
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    def bezier_linear(P0, P1, t):
        return (1-t)*P0 + t*P1

    def bezier_quad(P0, P1, P2, t):
        return (1-t)**2*P0 + 2*(1-t)*t*P1 + t**2*P2

    def bezier_cubic(P0, P1, P2, P3, t):
        return (1-t)**3*P0 + 3*(1-t)**2*t*P1 + 3*(1-t)*t**2*P2 + t**3*P3

    # Linear
    ax = axes[0]
    P0, P1 = np.array([0.5, 0.5]), np.array([5.5, 4.5])
    t_vals = np.linspace(0, 1, 100)
    curve = np.array([bezier_linear(P0, P1, t) for t in t_vals])
    ax.plot(curve[:, 0], curve[:, 1], 'b-', lw=2.5)
    ax.plot([P0[0], P1[0]], [P0[1], P1[1]], 'r--', lw=1, alpha=0.5)
    ax.plot(P0[0], P0[1], 'ro', markersize=10, zorder=5)
    ax.plot(P1[0], P1[1], 'ro', markersize=10, zorder=5)
    ax.text(P0[0]-0.3, P0[1]-0.4, 'P₀', fontsize=11, fontweight='bold')
    ax.text(P1[0]+0.1, P1[1]+0.1, 'P₁', fontsize=11, fontweight='bold')
    ax.set_title('Linear Bézier\n(straight line)', fontweight='bold')
    ax.set_xlim(0, 6); ax.set_ylim(0, 5); ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)

    # Quadratic
    ax = axes[1]
    P0, P1, P2 = np.array([0.5, 0.5]), np.array([3, 5]), np.array([5.5, 0.5])
    curve = np.array([bezier_quad(P0, P1, P2, t) for t in t_vals])
    ax.plot(curve[:, 0], curve[:, 1], 'b-', lw=2.5)
    ax.plot([P0[0], P1[0], P2[0]], [P0[1], P1[1], P2[1]], 'r--', lw=1, alpha=0.5)
    for pt, label in [(P0, 'P₀'), (P1, 'P₁'), (P2, 'P₂')]:
        ax.plot(pt[0], pt[1], 'ro', markersize=10, zorder=5)
        ax.text(pt[0]+0.1, pt[1]+0.1, label, fontsize=11, fontweight='bold')
    # Mark t=0.5
    mid = bezier_quad(P0, P1, P2, 0.5)
    ax.plot(mid[0], mid[1], 'go', markersize=8, zorder=5)
    ax.text(mid[0]+0.1, mid[1]-0.4, 't=0.5', fontsize=9, color='green')
    ax.set_title('Quadratic Bézier\n(3 control points)', fontweight='bold')
    ax.set_xlim(0, 6); ax.set_ylim(0, 5.5); ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)

    # Cubic
    ax = axes[2]
    P0 = np.array([0.5, 0.5]); P1 = np.array([1.5, 5])
    P2 = np.array([4.5, 5]); P3 = np.array([5.5, 0.5])
    curve = np.array([bezier_cubic(P0, P1, P2, P3, t) for t in t_vals])
    ax.plot(curve[:, 0], curve[:, 1], 'b-', lw=2.5)
    ax.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]],
            'r--', lw=1, alpha=0.5)
    for pt, label in [(P0, 'P₀'), (P1, 'P₁'), (P2, 'P₂'), (P3, 'P₃')]:
        ax.plot(pt[0], pt[1], 'ro', markersize=10, zorder=5)
        ax.text(pt[0]+0.1, pt[1]+0.1, label, fontsize=11, fontweight='bold')
    mid = bezier_cubic(P0, P1, P2, P3, 0.5)
    ax.plot(mid[0], mid[1], 'go', markersize=8, zorder=5)
    ax.text(mid[0]+0.1, mid[1]-0.4, 't=0.5', fontsize=9, color='green')
    ax.set_title('Cubic Bézier\n(4 control points)', fontweight='bold')
    ax.set_xlim(0, 6); ax.set_ylim(0, 5.5); ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)

    fig.suptitle('Bézier Curves — Linear, Quadratic, Cubic',
                 fontsize=14, fontweight='bold', y=1.02)
    save('12c2b-bezier-cubic.png')


# ============================================================
# 12c2c-parametric-surfaces.png
# ============================================================
def fig_parametric_surfaces():
    """Three classic parametric surfaces: sphere, cylinder, torus.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(15, 5))

    u = np.linspace(0, 2*np.pi, 40)
    v = np.linspace(0, np.pi, 30)
    U, V = np.meshgrid(u, v)

    # Sphere
    ax1 = fig.add_subplot(1, 3, 1, projection='3d')
    R = 1
    X = R * np.sin(V) * np.cos(U)
    Y = R * np.sin(V) * np.sin(U)
    Z = R * np.cos(V)
    ax1.plot_wireframe(X, Y, Z, color='blue', alpha=0.4, lw=0.4)
    ax1.set_title('Sphere\n$\\rho = R$', fontweight='bold')
    ax1.set_xlim(-1.3, 1.3); ax1.set_ylim(-1.3, 1.3); ax1.set_zlim(-1.3, 1.3)
    ax1.set_xlabel('X'); ax1.set_ylabel('Y'); ax1.set_zlabel('Z')
    ax1.view_init(elev=25, azim=-60)

    # Cylinder
    ax2 = fig.add_subplot(1, 3, 2, projection='3d')
    v = np.linspace(0, 2*np.pi, 40)
    z = np.linspace(0, 2, 20)
    V, Z = np.meshgrid(v, z)
    R = 1
    X = R * np.cos(V)
    Y = R * np.sin(V)
    ax2.plot_wireframe(X, Y, Z, color='red', alpha=0.4, lw=0.4)
    ax2.set_title('Cylinder\n$r = R$', fontweight='bold')
    ax2.set_xlim(-1.3, 1.3); ax2.set_ylim(-1.3, 1.3); ax2.set_zlim(-0.3, 2.3)
    ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('Z')
    ax2.view_init(elev=25, azim=-60)

    # Torus
    ax3 = fig.add_subplot(1, 3, 3, projection='3d')
    u_torus = np.linspace(0, 2*np.pi, 40)
    v_torus = np.linspace(0, 2*np.pi, 30)
    U_t, V_t = np.meshgrid(u_torus, v_torus)
    R_major, r_minor = 1.2, 0.5
    X = (R_major + r_minor * np.cos(V_t)) * np.cos(U_t)
    Y = (R_major + r_minor * np.cos(V_t)) * np.sin(U_t)
    Z = r_minor * np.sin(V_t)
    ax3.plot_wireframe(X, Y, Z, color='purple', alpha=0.4, lw=0.4)
    ax3.set_title('Torus\n$(R + r\\cos\\phi)\\cos\\theta$', fontweight='bold')
    ax3.set_xlim(-2, 2); ax3.set_ylim(-2, 2); ax3.set_zlim(-1, 1)
    ax3.set_xlabel('X'); ax3.set_ylabel('Y'); ax3.set_zlabel('Z')
    ax3.view_init(elev=25, azim=-60)

    fig.suptitle('Three Classic Parametric Surfaces',
                 fontsize=14, fontweight='bold', y=1.02)
    save('12c2c-parametric-surfaces.png')


# ============================================================
# 12c2d-cycloid.png  [NEW]
# ============================================================
def fig_cycloid():
    """Cycloid — the curve traced by a point on a rolling wheel.
    Also shows the rolling circle at multiple positions.
    """
    fig, ax = plt.subplots(figsize=(13, 5))

    R = 1
    t = np.linspace(0, 4*np.pi, 500)
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))

    ax.plot(x, y, 'b-', lw=2.5, label='cycloid')

    # Show rolling circle at several positions
    for t_val in [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi, 7*np.pi/2, 4*np.pi]:
        cx = R * t_val
        cy = R
        # Circle
        theta = np.linspace(0, 2*np.pi, 50)
        ax.plot(cx + R*np.cos(theta), cy + R*np.sin(theta), 'gray', lw=0.8, alpha=0.5)
        # Point on rim
        px = R * (t_val - np.sin(t_val))
        py = R * (1 - np.cos(t_val))
        ax.plot(px, py, 'ro', markersize=4)
        # Spoke
        ax.plot([cx, px], [cy, py], 'gray', lw=0.8, alpha=0.5)

    # Mark one arch
    ax.axvline(2*np.pi*R, color='orange', linestyle=':', lw=1.5, alpha=0.7)
    ax.annotate('one arch\n$(0 \\to 2\\pi R)$', xy=(np.pi*R, 2*R),
                fontsize=11, color='orange', fontweight='bold', ha='center')

    ax.set_title('Cycloid: A Point on a Rolling Wheel\n$\\vec{r}(t) = (R(t-\\sin t),\\; R(1-\\cos t))$',
                 fontweight='bold', fontsize=12)
    ax.set_xlim(-0.5, 4*np.pi*R+0.5); ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=9)
    save('12c2d-cycloid.png')


# ============================================================
# 12c2e-conical-spiral.png  [NEW]
# ============================================================
def fig_conical_spiral():
    """Conical spiral — a spiral that climbs and expands outward.
    This builds on the helix (12C2a) connecting to cone concept from 9C.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(0, 6*np.pi, 500)
    r = t / (6*np.pi)  # radius grows from 0 to 1
    x = r * np.cos(t)
    y = r * np.sin(t)
    z = t / (2*np.pi)  # height grows

    ax.plot(x, y, z, 'blue', lw=2.5, label='conical spiral')

    # Cone surface (wireframe)
    theta = np.linspace(0, 2*np.pi, 30)
    h = np.linspace(0, 3, 20)
    Theta, H = np.meshgrid(theta, h)
    R_grid = H / 3
    X_grid = R_grid * np.cos(Theta)
    Y_grid = R_grid * np.sin(Theta)
    ax.plot_wireframe(X_grid, Y_grid, H, alpha=0.08, color='gray', lw=0.3)

    # Projection onto xy-plane
    ax.plot(x, y, np.zeros_like(z), color='gray', linestyle='--', lw=1, alpha=0.5,
            label='xy-projection')

    ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2); ax.set_zlim(0, 3.2)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Conical Spiral\n$\\vec{r}(t) = (t\\cos t,\\; t\\sin t,\\; t/2\\pi)$',
                 fontweight='bold', fontsize=12)
    ax.legend(fontsize=9)
    ax.view_init(elev=20, azim=-60)
    save('12c2e-conical-spiral.png')


# ============================================================
# 12c2f-arc-length-visual.png  [NEW]
# ============================================================
def fig_arc_length_visual():
    """Visualizing arc length — approximating a curve with line segments.
    Shows the curve, velocity vectors, and the integral.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Left: Curve with velocity vectors
    t = np.linspace(0, 2*np.pi, 200)
    x = 3*np.cos(t)
    y = 2*np.sin(t)
    ax1.plot(x, y, 'b-', lw=2.5, label='ellipse')

    # Velocity vectors at several points
    t_samples = np.linspace(0, 2*np.pi, 12)
    for ts in t_samples:
        vx = -3*np.sin(ts)
        vy = 2*np.cos(ts)
        speed = np.sqrt(vx**2 + vy**2)
        # Normalize for display
        ax1.quiver(3*np.cos(ts), 2*np.sin(ts),
                   vx/speed, vy/speed,
                   angles='xy', scale_units='xy', scale=1,
                   color='red', alpha=0.5, width=0.01)

    ax1.set_title('Velocity vectors along an ellipse\n$|\\vec{r}\'(t)|$ = speed',
                  fontweight='bold')
    ax1.set_xlim(-4, 4); ax1.set_ylim(-3, 3)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.legend(fontsize=9)

    # Right: Approximating with line segments
    t_few = np.linspace(0, 2*np.pi, 8)
    x_few = 3*np.cos(t_few)
    y_few = 2*np.sin(t_few)
    ax2.plot(x, y, 'b-', lw=2.5, alpha=0.3, label='exact curve')
    ax2.plot(x_few, y_few, 'r.-', lw=2, markersize=10, label='8 segments')

    # Compute total length of segments
    seg_lengths = np.sqrt(np.diff(x_few)**2 + np.diff(y_few)**2)
    total = np.sum(seg_lengths)
    ax2.text(0, -2.5, f'Approx. length: {total:.2f}\n(as n → ∞, length → exact)',
             fontsize=11, ha='center', fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax2.set_title('Arc Length: $\\int |\\vec{r}\'(t)|\\,dt$\nSum of segment lengths',
                  fontweight='bold')
    ax2.set_xlim(-4, 4); ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='gray', lw=0.5); ax2.axvline(0, color='gray', lw=0.5)
    ax2.legend(fontsize=9)

    fig.suptitle('Arc Length: Integrating Speed Along the Curve',
                 fontsize=14, fontweight='bold')
    save('12c2f-arc-length-visual.png')


# ============================================================
# 12c2g-parametric-surface-normals.png  [NEW]
# ============================================================
def fig_surface_normals():
    """Surface normals on a parametric surface — tangent vectors and normal.
    Shows a patch with ru, rv, and n at several points.
    """
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi/2, 20)
    U, V = np.meshgrid(u, v)

    # Hemisphere
    R = 1
    X = R * np.sin(V) * np.cos(U)
    Y = R * np.sin(V) * np.sin(U)
    Z = R * np.cos(V)
    ax.plot_wireframe(X, Y, Z, color='blue', alpha=0.2, lw=0.3)

    # Show tangent vectors and normals at several points
    sample_us = np.linspace(0, 2*np.pi, 6)
    sample_vs = np.linspace(np.pi/6, np.pi/2.5, 3)
    for u0 in sample_us:
        for v0 in sample_vs:
            # Point
            p = np.array([R*np.sin(v0)*np.cos(u0),
                          R*np.sin(v0)*np.sin(u0),
                          R*np.cos(v0)])
            # Tangent vectors
            ru = np.array([-R*np.sin(v0)*np.sin(u0),
                           R*np.sin(v0)*np.cos(u0),
                           0])
            rv = np.array([R*np.cos(v0)*np.cos(u0),
                           R*np.cos(v0)*np.sin(u0),
                           -R*np.sin(v0)])
            # Normal (cross product)
            n = np.cross(ru, rv)
            n = n / np.linalg.norm(n) * 0.3

            ax.quiver(*p, *ru/np.linalg.norm(ru)*0.2, color='green', alpha=0.5, lw=0.8)
            ax.quiver(*p, *rv/np.linalg.norm(rv)*0.2, color='orange', alpha=0.5, lw=0.8)
            ax.quiver(*p, *n, color='red', alpha=0.7, lw=1.5, arrow_length_ratio=0.2)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='green', lw=1.5, label='$\\vec{r}_u$ (tangent)'),
        Line2D([0], [0], color='orange', lw=1.5, label='$\\vec{r}_v$ (tangent)'),
        Line2D([0], [0], color='red', lw=2, label='$\\vec{n} = \\vec{r}_u \\times \\vec{r}_v$'),
    ]
    ax.legend(handles=legend_elements, fontsize=8, loc='upper left')

    ax.set_title('Surface Normals on a Sphere\n$\\vec{r}_u \\times \\vec{r}_v$ gives normal',
                 fontweight='bold', fontsize=12)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_zlim(-0.3, 1.3)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.view_init(elev=25, azim=-60)
    save('12c2g-surface-normals.png')


# ============================================================
if __name__ == "__main__":
    print("Generating 12C2 graphs...")
    fig_helix()
    fig_bezier_cubic()
    fig_parametric_surfaces()
    fig_cycloid()
    fig_conical_spiral()
    fig_arc_length_visual()
    fig_surface_normals()
    print("Done! ✓")
