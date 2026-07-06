"""
Generate visualization graphs for Sessions 12C1, 12C2, 12C3 —
Geometric Transformations, Parametric Curves & Surfaces, Coordinate Systems & Optimization.

12c1a — 2D: Four fundamental transformations on a unit square
12c1b — 2D: Eigenvector directions — invariant lines under a matrix
12c1c — 2D: SVD decomposition — rotate→scale→rotate on unit circle
12c2a — 3D: Helix — parametric space curve
12c2b — 2D: Cubic Bezier curve with control points
12c2c — 3D: Parametric surfaces — sphere, cylinder, torus (multi-panel)
12c3a — 2D: Polar coordinates — cardioid and rose curves
12c3b — 3D: Spherical coordinates — point on a sphere
12c3c — 2D: Convex hull of a point set
12c3d — 2D: Point–line distance in 3D (projected to 2D schematic)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 12C1a — Four Fundamental 2D Transformations on Unit Square
# ================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 13))
(ax1, ax2), (ax3, ax4) = axes

square = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
theta_rot = np.radians(45)

transformations = [
    (ax1, 'Rotation 45° CCW',
     np.array([[np.cos(theta_rot), -np.sin(theta_rot)],
               [np.sin(theta_rot),  np.cos(theta_rot)]])),
    (ax2, 'Scaling (sx=2.5, sy=1.5)',
     np.array([[2.5, 0.0], [0.0, 1.5]])),
    (ax3, 'Reflection across y=x (45°)',
     np.array([[0.0, 1.0], [1.0, 0.0]])),
    (ax4, 'Shear (k=1.2 parallel to x)',
     np.array([[1.0, 1.2], [0.0, 1.0]])),
]

for ax, title, A in transformations:
    transformed = (A @ square.T).T
    # Original square
    ax.plot(square[:,0], square[:,1], 'k--', linewidth=2, alpha=0.45, label='Original')
    ax.fill(square[:,0], square[:,1], alpha=0.06, color='gray')
    # Transformed
    ax.plot(transformed[:,0], transformed[:,1], 'b-', linewidth=2.8, label='Transformed')
    ax.fill(transformed[:,0], transformed[:,1], alpha=0.22, color='steelblue')
    # Basis vectors
    col1, col2 = A[:,0], A[:,1]
    ax.arrow(0, 0, col1[0], col1[1], head_width=0.07, head_length=0.1,
             fc='red', ec='red', linewidth=2.2)
    ax.arrow(0, 0, col2[0], col2[1], head_width=0.07, head_length=0.1,
             fc='darkgreen', ec='darkgreen', linewidth=2.2)
    ax.set_aspect('equal')
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.grid(alpha=0.18)
    ax.axhline(0, color='gray', linewidth=0.35)
    ax.axvline(0, color='gray', linewidth=0.35)
    ax.set_xlim(-1.8, 3.5)
    ax.set_ylim(-2.2, 2.2)

fig.suptitle('Graph 12C1a: Four Fundamental 2D Transformations on the Unit Square',
             fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '12c1a-four-transformations.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C1a done — Four transformations")


# ================================================================
# 12C1b — Eigenvector Directions (Invariant Lines)
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
ax1, ax2 = axes

# Matrix A = [[4,1],[2,3]] — has eigenvectors (1,1) with λ=5 and (1,-2) with λ=2
A = np.array([[4.0, 1.0], [2.0, 3.0]])

# Draw a circle of test vectors to show deformation
theta = np.linspace(0, 2*np.pi, 200)
circle_pts = np.vstack([np.cos(theta), np.sin(theta)])  # 2x200
ellipse_pts = A @ circle_pts  # 2x200

ax1.plot(circle_pts[0,:], circle_pts[1,:], 'k-', linewidth=1.2, alpha=0.5, label='Unit circle')
ax1.plot(ellipse_pts[0,:], ellipse_pts[1,:], 'b-', linewidth=2.8, label='A × (unit circle)')
ax1.fill(ellipse_pts[0,:], ellipse_pts[1,:], alpha=0.18, color='steelblue')

# Draw eigenvector directions
# Eigenvector v1 = (1,1)/√2, stretch to λ=5: goes to (5,5)/√2 ≈ (3.536, 3.536)
v1 = np.array([1,1]) / np.sqrt(2)
ax1.arrow(0, 0, v1[0], v1[1], head_width=0.1, head_length=0.15,
          fc='red', ec='red', linewidth=2.5, label=r'$\vec{v}_1$ (λ=5)')
ax1.arrow(0, 0, 5*v1[0], 5*v1[1], head_width=0.1, head_length=0.15,
          fc='darkred', ec='darkred', linewidth=2.5, linestyle='--',
          label=r'$A\vec{v}_1 = 5\vec{v}_1$')

v2 = np.array([1,-2]) / np.sqrt(5)
ax1.arrow(0, 0, v2[0], v2[1], head_width=0.1, head_length=0.15,
          fc='darkgreen', ec='darkgreen', linewidth=2.5, label=r'$\vec{v}_2$ (λ=2)')
ax1.arrow(0, 0, 2*v2[0], 2*v2[1], head_width=0.1, head_length=0.15,
          fc='limegreen', ec='limegreen', linewidth=2.5, linestyle='--',
          label=r'$A\vec{v}_2 = 2\vec{v}_2$')

ax1.set_aspect('equal')
ax1.set_xlim(-6, 6)
ax1.set_ylim(-6, 6)
ax1.set_title('Eigenvectors: Invariant Directions', fontsize=13, fontweight='bold')
ax1.legend(fontsize=9, loc='upper left')
ax1.grid(alpha=0.15)
ax1.axhline(0, color='gray', linewidth=0.3)
ax1.axvline(0, color='gray', linewidth=0.3)

# Right: rotation matrix — no real eigenvectors
R = np.array([[0.0, -1.0], [1.0, 0.0]])  # 90° rotation
rotated_pts = R @ circle_pts
ax2.plot(circle_pts[0,:], circle_pts[1,:], 'k-', linewidth=1.2, alpha=0.5, label='Unit circle')
ax2.plot(rotated_pts[0,:], rotated_pts[1,:], 'purple', linewidth=2.8, label='R₉₀ × (unit circle)')

# Show a few vectors rotated
for angle_deg in [0, 45, 90, 135]:
    ang = np.radians(angle_deg)
    v = np.array([np.cos(ang), np.sin(ang)])
    rv = R @ v
    ax2.arrow(0, 0, v[0], v[1], head_width=0.08, head_length=0.12,
              fc='gray', ec='gray', linewidth=1.5, alpha=0.7)
    ax2.arrow(0, 0, rv[0], rv[1], head_width=0.08, head_length=0.12,
              fc='purple', ec='purple', linewidth=1.5, alpha=0.8)

ax2.set_aspect('equal')
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_title('Pure Rotation: No Real Eigenvector\n(every vector changes direction)',
              fontsize=13, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(alpha=0.15)
ax2.axhline(0, color='gray', linewidth=0.3)
ax2.axvline(0, color='gray', linewidth=0.3)

fig.suptitle('Graph 12C1b: Eigenvectors — When a Matrix Preserves Direction',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '12c1b-eigenvectors.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C1b done — Eigenvectors")


# ================================================================
# 12C1c — SVD Decomposition: Rotate → Scale → Rotate
# ================================================================
fig, axes = plt.subplots(1, 4, figsize=(18, 5.5))

A = np.array([[2.0, 1.0], [0.5, 1.5]])
U, S, Vt = np.linalg.svd(A)
Sigma = np.diag(S)
V = Vt.T

theta = np.linspace(0, 2*np.pi, 200)
circle = np.vstack([np.cos(theta), np.sin(theta)])

# (1) Original unit circle
ax = axes[0]
ax.plot(circle[0,:], circle[1,:], 'k-', linewidth=2, label='Unit circle')
ax.set_title('(1) Unit Circle\n(Input Space)', fontsize=11, fontweight='bold')
ax.set_aspect('equal'); ax.grid(alpha=0.15); ax.set_xlim(-3,3); ax.set_ylim(-3,3)
ax.axhline(0,color='gray',lw=0.3); ax.axvline(0,color='gray',lw=0.3)

# (2) After V^T rotation
ax = axes[1]
rot1 = Vt @ circle
ax.plot(rot1[0,:], rot1[1,:], 'orange', linewidth=2, label='After Vᵀ (rotate)')
ax.set_title('(2) Vᵀ rotates\nto align axes', fontsize=11, fontweight='bold')
ax.set_aspect('equal'); ax.grid(alpha=0.15); ax.set_xlim(-3,3); ax.set_ylim(-3,3)
ax.axhline(0,color='gray',lw=0.3); ax.axvline(0,color='gray',lw=0.3)

# (3) After Sigma scaling
ax = axes[2]
scaled = Sigma @ rot1
ax.plot(scaled[0,:], scaled[1,:], 'green', linewidth=2, label='After Σ (scale)')
ax.set_title(f'(3) Σ scales (σ₁={S[0]:.2f}, σ₂={S[1]:.2f})',
             fontsize=11, fontweight='bold')
ax.set_aspect('equal'); ax.grid(alpha=0.15); ax.set_xlim(-3,3); ax.set_ylim(-3,3)
ax.axhline(0,color='gray',lw=0.3); ax.axvline(0,color='gray',lw=0.3)

# (4) After U rotation = final ellipse
ax = axes[3]
final = U @ scaled
ax.plot(final[0,:], final[1,:], 'blue', linewidth=2.5, label='After U (rotate) = A×circle')
ax.fill(final[0,:], final[1,:], alpha=0.15, color='steelblue')
ax.set_title('(4) U rotates\n= Final Ellipse', fontsize=11, fontweight='bold')
ax.set_aspect('equal'); ax.grid(alpha=0.15); ax.set_xlim(-3,3); ax.set_ylim(-3,3)
ax.axhline(0,color='gray',lw=0.3); ax.axvline(0,color='gray',lw=0.3)

fig.suptitle('Graph 12C1c: SVD — Every Matrix = Rotate → Scale → Rotate',
             fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig(OUT + '12c1c-svd-decomposition.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C1c done — SVD decomposition")


# ================================================================
# 12C2a — 3D Helix (Parametric Space Curve)
# ================================================================
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, 6*np.pi, 600)
x = np.cos(t)
y = np.sin(t)
z = t

# Main helix
ax.plot(x, y, z, 'b-', linewidth=2.2, label='Helix: (cos t, sin t, t)')

# Start and end markers
ax.scatter([1], [0], [0], c='green', s=80, zorder=5, label='Start (t=0)')
ax.scatter([1], [0], [6*np.pi], c='red', s=80, zorder=5, label='End (t=6π)')

# Highlight one turn
t_one = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(t_one), np.sin(t_one), t_one, 'orange', linewidth=3.5,
        label='One full turn (pitch = 2π)')

# Projection on xy-plane
ax.plot(x, y, np.zeros_like(z), 'gray', linewidth=0.7, alpha=0.4)

ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_zlabel('z (height)', fontsize=13)
ax.set_title('Graph 12C2a: Circular Helix — A 3D Parametric Curve\n'
             'r(t) = (cos t, sin t, t),  t ∈ [0, 6π]',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper left')
ax.view_init(elev=22, azim=-55)
plt.tight_layout()
plt.savefig(OUT + '12c2a-helix.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C2a done — 3D Helix")


# ================================================================
# 12C2b — Cubic Bézier Curve with Control Points
# ================================================================
fig, ax = plt.subplots(figsize=(11, 8))

P = np.array([[0, 0], [1, 3], [4, 3], [5, 0]])  # control points

t_vals = np.linspace(0, 1, 200)
curve = np.zeros((len(t_vals), 2))
for i, t in enumerate(t_vals):
    b0 = (1-t)**3
    b1 = 3*(1-t)**2*t
    b2 = 3*(1-t)*t**2
    b3 = t**3
    curve[i] = b0*P[0] + b1*P[1] + b2*P[2] + b3*P[3]

# Draw control polygon
ax.plot(P[:,0], P[:,1], 'o-', color='gray', linewidth=1.5, markersize=9,
        markerfacecolor='darkgray', label='Control polygon')

# Draw curve
ax.plot(curve[:,0], curve[:,1], 'b-', linewidth=3.5, label='Cubic Bézier curve')

# Label control points
labels = [r'$\vec{P}_0$', r'$\vec{P}_1$', r'$\vec{P}_2$', r'$\vec{P}_3$']
offsets = [(-0.25, -0.3), (-0.3, 0.2), (0.15, 0.2), (0.1, -0.3)]
for pt, lbl, off in zip(P, labels, offsets):
    ax.annotate(lbl, pt, textcoords='offset points', xytext=off,
                fontsize=14, fontweight='bold', color='darkred')

# Mark t=0.5
t05 = curve[100]
ax.plot(t05[0], t05[1], 'o', color='red', markersize=10, zorder=5)
ax.annotate('t=0.5', t05, textcoords='offset points', xytext=(8, 8),
            fontsize=12, color='red', fontweight='bold')

ax.set_aspect('equal')
ax.set_xlim(-0.8, 6)
ax.set_ylim(-1, 4.5)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 12C2b: Cubic Bézier Curve — 4 Control Points, Smooth Interpolation',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '12c2b-bezier-cubic.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C2b done — Cubic Bezier")


# ================================================================
# 12C2c — Parametric Surfaces: Sphere, Cylinder, Torus
# ================================================================
fig = plt.figure(figsize=(20, 6.5))

# --- Sphere ---
ax1 = fig.add_subplot(131, projection='3d')
phi = np.linspace(0, np.pi, 40)
theta = np.linspace(0, 2*np.pi, 60)
phi_g, theta_g = np.meshgrid(phi, theta)
R = 1.0
x_s = R * np.sin(phi_g) * np.cos(theta_g)
y_s = R * np.sin(phi_g) * np.sin(theta_g)
z_s = R * np.cos(phi_g)
ax1.plot_surface(x_s, y_s, z_s, cmap='Blues', alpha=0.75, edgecolor='none')
ax1.set_title('Sphere\nr(θ,φ) = (R sinφ cosθ, R sinφ sinθ, R cosφ)',
              fontsize=10, fontweight='bold')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.view_init(elev=22, azim=-60)

# --- Cylinder ---
ax2 = fig.add_subplot(132, projection='3d')
z_c = np.linspace(0, 2, 30)
theta_c = np.linspace(0, 2*np.pi, 60)
z_g, theta_g = np.meshgrid(z_c, theta_c)
x_c = np.cos(theta_g)
y_c = np.sin(theta_g)
ax2.plot_surface(x_c, y_c, z_g, cmap='Greens', alpha=0.75, edgecolor='none')
ax2.set_title('Cylinder\nr(θ,z) = (cos θ, sin θ, z),  z∈[0,2]',
              fontsize=10, fontweight='bold')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')
ax2.view_init(elev=22, azim=-60)

# --- Torus ---
ax3 = fig.add_subplot(133, projection='3d')
phi_t = np.linspace(0, 2*np.pi, 40)
theta_t = np.linspace(0, 2*np.pi, 60)
phi_g, theta_g = np.meshgrid(phi_t, theta_t)
R_t, r_t = 3.0, 1.0
x_t = (R_t + r_t*np.cos(phi_g)) * np.cos(theta_g)
y_t = (R_t + r_t*np.cos(phi_g)) * np.sin(theta_g)
z_t = r_t * np.sin(phi_g)
ax3.plot_surface(x_t, y_t, z_t, cmap='Oranges', alpha=0.75, edgecolor='none')
ax3.set_title('Torus\nr(θ,φ) = ((R+r cosφ)cosθ, (R+r cosφ)sinθ, r sinφ)',
              fontsize=10, fontweight='bold')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.view_init(elev=22, azim=-60)

fig.suptitle('Graph 12C2c: Three Classic Parametric Surfaces',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '12c2c-parametric-surfaces.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C2c done — Parametric surfaces")


# ================================================================
# 12C3a — Polar Coordinates: Cardioid and Rose Curve
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
ax1, ax2 = axes

# Cardioid: r = 1 + cos θ
theta = np.linspace(0, 2*np.pi, 400)
r_cardioid = 1 + np.cos(theta)
x_c = r_cardioid * np.cos(theta)
y_c = r_cardioid * np.sin(theta)

ax1.fill(x_c, y_c, alpha=0.25, color='coral')
ax1.plot(x_c, y_c, 'darkred', linewidth=2.8, label=r'$r = 1 + \cos\theta$')
ax1.set_aspect('equal')
ax1.set_title('Cardioid (heart curve)', fontsize=13, fontweight='bold')
ax1.legend(fontsize=12)
ax1.grid(alpha=0.18)
ax1.axhline(0, color='gray', lw=0.35)
ax1.axvline(0, color='gray', lw=0.35)
ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2)

# Rose curve: r = sin(3θ)
theta = np.linspace(0, 2*np.pi, 600)
r_rose = np.sin(3*theta)
# Remove negative r values (trace only for r >= 0)
mask = r_rose >= 0
x_r = r_rose[mask] * np.cos(theta[mask])
y_r = r_rose[mask] * np.sin(theta[mask])

ax2.fill(x_r, y_r, alpha=0.25, color='purple')
ax2.plot(x_r, y_r, 'darkviolet', linewidth=2.5, label=r'$r = \sin(3\theta)$')
ax2.set_aspect('equal')
ax2.set_title('3-petal Rose', fontsize=13, fontweight='bold')
ax2.legend(fontsize=12)
ax2.grid(alpha=0.18)
ax2.axhline(0, color='gray', lw=0.35)
ax2.axvline(0, color='gray', lw=0.35)
ax2.set_xlim(-1.3, 1.3)
ax2.set_ylim(-1.3, 1.3)

fig.suptitle('Graph 12C3a: Polar Coordinates — Curves Made Simple by Symmetry',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '12c3a-polar-curves.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C3a done — Polar curves")


# ================================================================
# 12C3b — Spherical Coordinates: Point on a Sphere
# ================================================================
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

# Draw a semi-transparent sphere
phi = np.linspace(0, np.pi, 30)
theta = np.linspace(0, 2*np.pi, 50)
phi_g, theta_g = np.meshgrid(phi, theta)
R = 1.0
x_s = R * np.sin(phi_g) * np.cos(theta_g)
y_s = R * np.sin(phi_g) * np.sin(theta_g)
z_s = R * np.cos(phi_g)
ax.plot_surface(x_s, y_s, z_s, cmap='Blues', alpha=0.2, edgecolor='none')

# A specific point: φ=π/3 (60° from z), θ=π/4 (45° in xy)
phi_pt = np.pi/3
theta_pt = np.pi/4
x_pt = np.sin(phi_pt) * np.cos(theta_pt)
y_pt = np.sin(phi_pt) * np.sin(theta_pt)
z_pt = np.cos(phi_pt)

# Draw the radius line
ax.plot([0, x_pt], [0, y_pt], [0, z_pt], 'r-', linewidth=2.5, label='ρ (radius)')
ax.scatter([x_pt], [y_pt], [z_pt], c='red', s=100, zorder=5, label=f'Point (ρ=1, φ=π/3, θ=π/4)')

# Draw the projection onto xy-plane
ax.plot([0, x_pt], [0, y_pt], [0, 0], 'gray', linewidth=1, linestyle='--', alpha=0.7)
ax.plot([x_pt, x_pt], [y_pt, y_pt], [0, z_pt], 'gray', linewidth=1, linestyle='--', alpha=0.7)

# Draw the angle arcs (approximate with lines)
# θ arc in xy-plane
theta_arc = np.linspace(0, theta_pt, 30)
r_arc = 0.3
ax.plot(r_arc*np.cos(theta_arc), r_arc*np.sin(theta_arc), 0, 'darkgreen', linewidth=2,
        label='θ (azimuthal)')

# φ arc in plane containing point and z-axis
phi_arc = np.linspace(0, phi_pt, 30)
# Points in the plane along the φ direction
for i in range(len(phi_arc)):
    pass  # Simplified — draw small arc on sphere surface

# Annotations
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
ax.set_title('Graph 12C3b: Spherical Coordinates (ρ, φ, θ) on the Unit Sphere',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.view_init(elev=25, azim=-50)
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
plt.tight_layout()
plt.savefig(OUT + '12c3b-spherical-coords.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C3b done — Spherical coordinates")


# ================================================================
# 12C3c — Convex Hull of a 2D Point Set
# ================================================================
fig, ax = plt.subplots(figsize=(10, 8))

# Random-looking but predetermined points
points = np.array([
    [0.5, 0.5],
    [1.0, 2.5],
    [2.0, 1.0],
    [3.5, 2.0],
    [4.0, 3.5],
    [5.0, 1.5],
    [4.5, 0.2],
    [2.5, 3.8],
    [0.8, 3.2],
    [3.0, 2.8],
    [2.2, 2.0],   # interior point
    [1.5, 1.8],   # interior point
])


# Convex hull vertices (computed manually for these points)
# Graham scan order: lowest y then CCW
hull_indices = [0, 6, 5, 4, 7, 8, 1]  # approximate hull order
hull_pts = points[hull_indices]
hull_pts = np.vstack([hull_pts, hull_pts[0]])  # close the polygon

# Draw all points
ax.scatter(points[:,0], points[:,1], c='steelblue', s=70, zorder=3,
           label='Points')

# Highlight interior points
interior_idx = [10, 11]
ax.scatter(points[interior_idx,0], points[interior_idx,1],
           c='gray', s=70, zorder=3, marker='s', label='Interior points')

# Draw convex hull
ax.plot(hull_pts[:,0], hull_pts[:,1], 'r-', linewidth=3, label='Convex hull')
ax.fill(hull_pts[:,0], hull_pts[:,1], alpha=0.12, color='red')

# Label hull vertices
for i in hull_indices:
    ax.annotate(f'({points[i,0]}, {points[i,1]})', points[i],
                textcoords='offset points', xytext=(5, 7),
                fontsize=9, color='darkred')

ax.set_aspect('equal')
ax.set_xlim(-0.3, 6)
ax.set_ylim(-0.3, 4.5)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 12C3c: Convex Hull — The Smallest Convex Polygon\nContaining All Points',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '12c3c-convex-hull.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C3c done — Convex hull")


# ================================================================
# 12C3d — Point–Line Distance in 3D (Schematic)
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
ax1, ax2 = axes

# Left: 2D point-to-line distance
# Line: 3x + 4y = 10, point: (3, 4)
ax1.set_xlim(-1, 6)
ax1.set_ylim(-1, 6)
ax1.set_aspect('equal')

# Draw the line 3x+4y=10 → y = (10-3x)/4
x_line = np.linspace(-1, 5, 100)
y_line = (10 - 3*x_line) / 4
ax1.plot(x_line, y_line, 'b-', linewidth=2.5, label='Line: 3x + 4y = 10')

# Point
ax1.scatter([3], [4], c='red', s=100, zorder=5, label='Point P(3, 4)')

# Perpendicular from point to line
# Distance formula: d = |3*3+4*4-10|/5 = 15/5 = 3
# Foot of perpendicular: solve (x-3, y-4) ∝ (3,4), and 3x+4y=10
# (x-3)/3 = (y-4)/4 = t → x=3+3t, y=4+4t
# 3(3+3t)+4(4+4t)=10 → 9+9t+16+16t=10 → 25t=-15 → t=-0.6
# Foot: (3-1.8, 4-2.4) = (1.2, 1.6)
ax1.plot([3, 1.2], [4, 1.6], 'r--', linewidth=2, label='d = 3 (perpendicular)')
ax1.scatter([1.2], [1.6], c='darkgreen', s=80, zorder=5, label='Foot of perpendicular')

ax1.set_title('2D: Distance Point to Line\nFormula: d = |ax₀+by₀+c|/√(a²+b²)',
              fontsize=11, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(alpha=0.15)

# Right: 3D point-to-line (schematic projection)
# Line through O with direction d=(1,1,1); point p=(1,2,3)
ax2.set_xlim(-0.5, 4)
ax2.set_ylim(-0.5, 4)
ax2.set_aspect('equal')

# Draw line direction
ax2.arrow(0, 0, 3.8, 3.8, head_width=0.12, head_length=0.18,
          fc='blue', ec='blue', linewidth=2.5, label='Line direction d⃗', alpha=0.6)

# Vector to point (projected onto 2D plane for visualization)
# p = (1,2,3), project to show concept
p_proj = np.array([1.5, 3.0])  # stylized projection
ax2.arrow(0, 0, p_proj[0], p_proj[1], head_width=0.12, head_length=0.18,
          fc='red', ec='red', linewidth=2.5, label='Vector to point v⃗')

# Projection of p onto d
d_dir = np.array([1, 1]) / np.sqrt(2)
proj_scalar = np.dot(p_proj, d_dir)
proj_vec = proj_scalar * d_dir
ax2.arrow(0, 0, proj_vec[0], proj_vec[1], head_width=0.10, head_length=0.15,
          fc='green', ec='green', linewidth=2.5, linestyle='--',
          label='Projection onto line')

# Perpendicular component
perp_vec = p_proj - proj_vec
ax2.arrow(proj_vec[0], proj_vec[1], perp_vec[0], perp_vec[1],
          head_width=0.10, head_length=0.15,
          fc='purple', ec='purple', linewidth=2.5, label='⊥ component = distance')

ax2.set_title('3D: Distance = |v⃗ × d⃗| / |d⃗|\n(Cross product yields perpendicular component)',
              fontsize=11, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(alpha=0.15)

fig.suptitle('Graph 12C3d: Distance from a Point to a Line — 2D and 3D',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '12c3d-point-line-distance.png', dpi=180, bbox_inches='tight')
plt.close()
print("12C3d done — Point-line distance")

print("\n=== ALL 12C GRAPHS GENERATED ===")
