"""
Generate new visualization graphs for Session 9B and 9C —
2D Geometry (conics, parametric, distance) and 3D Surfaces (quadrics).

9b1 — 2D: Four conic sections on one canvas
9b2 — 2D: Parametric cycloid
9b3 — 2D: Point-to-line distance schematic
9c1 — 3D: Level curves of a saddle (z = x² - y²)
9c2 — 3D: Ellipsoid surface
9c3 — 3D: Hyperboloid of one sheet + cone
9c4 — 3D: Sphere + intersecting plane (circle of intersection)
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 9B1 — Four Conic Sections
# ================================================================
fig, axes = plt.subplots(2, 2, figsize=(13, 13))
(ax1, ax2), (ax3, ax4) = axes

# Circle
theta = np.linspace(0, 2*np.pi, 300)
ax1.plot(3*np.cos(theta), 3*np.sin(theta), 'b-', linewidth=2.5)
ax1.plot(0, 0, 'ro', markersize=8)
ax1.set_title('Circle: $x^2+y^2=9$\nCenter (0,0), R=3', fontsize=12, fontweight='bold')
ax1.set_aspect('equal'); ax1.grid(alpha=0.2); ax1.set_xlim(-5,5); ax1.set_ylim(-5,5)
ax1.axhline(0,color='gray',lw=0.4); ax1.axvline(0,color='gray',lw=0.4)

# Ellipse
a, b = 4, 2
ax2.plot(a*np.cos(theta), b*np.sin(theta), 'darkgreen', linewidth=2.5)
ax2.plot([-np.sqrt(a**2-b**2), np.sqrt(a**2-b**2)], [0, 0], 'ro', markersize=6, label='Foci')
ax2.set_title('Ellipse: $x^2/16 + y^2/4 = 1$\nFoci at (±2√3, 0)', fontsize=12, fontweight='bold')
ax2.set_aspect('equal'); ax2.grid(alpha=0.2); ax2.set_xlim(-5,5); ax2.set_ylim(-3,3)
ax2.axhline(0,color='gray',lw=0.4); ax2.axvline(0,color='gray',lw=0.4); ax2.legend(fontsize=8)

# Parabola
x = np.linspace(-5, 5, 300)
y = x**2 / 4
ax3.plot(x, y, 'darkred', linewidth=2.5)
ax3.plot(0, 1, 'ro', markersize=6, label='Focus (0,1)')
ax3.axhline(-1, color='gray', linestyle='--', linewidth=1.5, label='Directrix y=-1')
ax3.set_title('Parabola: $y = x^2/4$\nFocus (0,1), Directrix y=-1', fontsize=12, fontweight='bold')
ax3.set_aspect('equal'); ax3.grid(alpha=0.2); ax3.set_xlim(-5,5); ax3.set_ylim(-2,6)
ax3.axhline(0,color='gray',lw=0.4); ax3.axvline(0,color='gray',lw=0.4); ax3.legend(fontsize=8)

# Hyperbola
x_h = np.linspace(-5, -2.001, 150)
x_h2 = np.linspace(2.001, 5, 150)
y_h_pos = 1.5 * np.sqrt(x_h2**2/4 - 1)
y_h_neg = -1.5 * np.sqrt(x_h2**2/4 - 1)
y_h_pos2 = 1.5 * np.sqrt(x_h**2/4 - 1)
y_h_neg2 = -1.5 * np.sqrt(x_h**2/4 - 1)

ax4.plot(x_h2, y_h_pos, 'purple', linewidth=2.5)
ax4.plot(x_h2, y_h_neg, 'purple', linewidth=2.5)
ax4.plot(x_h, y_h_pos2, 'purple', linewidth=2.5)
ax4.plot(x_h, y_h_neg2, 'purple', linewidth=2.5)
# Asymptotes
x_asym = np.linspace(-5, 5, 100)
ax4.plot(x_asym, 1.5*x_asym/2, 'orange', linestyle='--', linewidth=1.5, label='y=±(3/2)x')
ax4.plot(x_asym, -1.5*x_asym/2, 'orange', linestyle='--', linewidth=1.5)
ax4.set_title('Hyperbola: $x^2/4 - y^2/2.25 = 1$\nAsymptotes: y = ±(3/2)x', fontsize=12, fontweight='bold')
ax4.set_aspect('equal'); ax4.grid(alpha=0.2); ax4.set_xlim(-5,5); ax4.set_ylim(-5,5)
ax4.axhline(0,color='gray',lw=0.4); ax4.axvline(0,color='gray',lw=0.4); ax4.legend(fontsize=8)

fig.suptitle('Graph 9B1: Four Conic Sections — Circle, Ellipse, Parabola, Hyperbola',
             fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '9b1-four-conics.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B1 done — Four conic sections")


# ================================================================
# 9B2 — Parametric Cycloid
# ================================================================
fig, ax = plt.subplots(figsize=(12, 6))

R = 1.0
t = np.linspace(0, 4*np.pi, 800)
x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

# Two arches
ax.plot(x, y, 'b-', linewidth=2.5, label='Cycloid: (t−sin t, 1−cos t)')

# Mark the base line
ax.axhline(0, color='gray', linewidth=1, linestyle='--', alpha=0.6)

# Highlight one arch
t_one = np.linspace(0, 2*np.pi, 300)
x_one = R * (t_one - np.sin(t_one))
y_one = R * (1 - np.cos(t_one))
ax.fill_between(x_one, 0, y_one, alpha=0.2, color='steelblue')
ax.plot(x_one, y_one, 'darkblue', linewidth=3.5, label='One arch (t∈[0,2π])')

# Mark key points
ax.plot(0, 0, 'go', markersize=10, label='Start (t=0)')
ax.plot(np.pi*R, 2*R, 'ro', markersize=10, label='Peak (t=π, height=2R)')
ax.plot(2*np.pi*R, 0, 'o', color='purple', markersize=10, label='End of arch (t=2π)')

ax.set_aspect('equal')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-0.3, 2.5)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 9B2: The Cycloid — Path of a Point on a Rolling Wheel',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper right')
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '9b2-cycloid.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B2 done — Cycloid")


# ================================================================
# 9B3 — Point-to-Line Distance (2D schematic)
# ================================================================
fig, ax = plt.subplots(figsize=(10, 8))

# Line: 3x + 4y = 10  →  y = (10-3x)/4
x_line = np.linspace(-2, 6, 200)
y_line = (10 - 3*x_line) / 4
ax.plot(x_line, y_line, 'b-', linewidth=2.8, label='Line: 3x + 4y = 10')

# Point (3, 4)
ax.scatter([3], [4], c='red', s=120, zorder=5, label='P(3, 4)')

# Perpendicular foot
# Distance formula: |3*3+4*4-10|/5 = 15/5 = 3
# Foot: (3,4) - 3*(3/5, 4/5) = (3-9/5, 4-12/5) = (6/5, 8/5) = (1.2, 1.6)
foot = np.array([1.2, 1.6])
ax.plot([3, foot[0]], [4, foot[1]], 'r--', linewidth=2.2, label='d = 3')
ax.scatter([foot[0]], [foot[1]], c='darkgreen', s=80, zorder=5, label='Foot (1.2, 1.6)')

# Annotation with formula
ax.text(3.2, 2.2,
        r'$d = \frac{|3\cdot3 + 4\cdot4 - 10|}{\sqrt{3^2+4^2}} = \frac{15}{5} = 3$',
        fontsize=13, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax.set_aspect('equal')
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 5.5)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 9B3: Point-to-Line Distance in 2D',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '9b3-point-line-distance.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B3 done — Point-line distance")


# ================================================================
# 9C1 — Level Curves of z = x² - y² (Saddle)
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

x = np.linspace(-4, 4, 300)
y_vals = np.linspace(-4, 4, 300)
X, Y = np.meshgrid(x, y_vals)
Z = X**2 - Y**2

# Contour plot
levels = [-6, -4, -2, -1, 0, 1, 2, 4, 6]
contours = ax.contour(X, Y, Z, levels=levels, cmap='RdBu_r', linewidths=1.8)
ax.clabel(contours, inline=True, fontsize=10, fmt='%d')

# Highlight the crossing lines at z=0
ax.axhline(0, color='black', linewidth=1.5, linestyle='--', alpha=0.7)
ax.axvline(0, color='black', linewidth=1.5, linestyle='--', alpha=0.7)

# Mark saddle point
ax.plot(0, 0, 'ko', markersize=10, label='Saddle point (0,0,0)')

ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 9C1: Level Curves of z = x² − y²\nHyperbolas meeting at the saddle point',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.12)
plt.tight_layout()
plt.savefig(OUT + '9c1-level-curves-saddle.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C1 done — Level curves of saddle")


# ================================================================
# 9C2 — Ellipsoid Surface
# ================================================================
fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(111, projection='3d')

# Ellipsoid: x²/4 + y²/9 + z²/1 = 1
# Parametric: x=2 sinφ cosθ, y=3 sinφ sinθ, z=1 cosφ
phi = np.linspace(0, np.pi, 40)
theta = np.linspace(0, 2*np.pi, 60)
phi_g, theta_g = np.meshgrid(phi, theta)

a, b, c = 2, 3, 1
x_e = a * np.sin(phi_g) * np.cos(theta_g)
y_e = b * np.sin(phi_g) * np.sin(theta_g)
z_e = c * np.cos(phi_g)

ax.plot_surface(x_e, y_e, z_e, cmap='Blues', alpha=0.7, edgecolor='none')
ax.set_xlabel('x (semi-axis=2)', fontsize=12)
ax.set_ylabel('y (semi-axis=3)', fontsize=12)
ax.set_zlabel('z (semi-axis=1)', fontsize=12)
ax.set_title('Graph 9C2: Ellipsoid — x²/4 + y²/9 + z²/1 = 1',
             fontsize=13, fontweight='bold')
ax.view_init(elev=20, azim=-55)
plt.tight_layout()
plt.savefig(OUT + '9c2-ellipsoid.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C2 done — Ellipsoid")


# ================================================================
# 9C3 — Hyperboloid of One Sheet + Cone
# ================================================================
fig = plt.figure(figsize=(18, 8))

# Hyperboloid of one sheet: x² + y² - z²/4 = 1
ax1 = fig.add_subplot(121, projection='3d')
z_hyp = np.linspace(-3, 3, 40)
theta_hyp = np.linspace(0, 2*np.pi, 60)
z_g, t_g = np.meshgrid(z_hyp, theta_hyp)
r_hyp = np.sqrt(1 + z_g**2 / 4)
x_hyp = r_hyp * np.cos(t_g)
y_hyp = r_hyp * np.sin(t_g)
ax1.plot_surface(x_hyp, y_hyp, z_g, cmap='Oranges', alpha=0.7, edgecolor='none')
ax1.set_title('Hyperboloid of One Sheet\n$x^2+y^2-z^2/4=1$', fontsize=12, fontweight='bold')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.view_init(elev=20, azim=-50)

# Cone: x² + y² - z² = 0  →  z² = x² + y²
ax2 = fig.add_subplot(122, projection='3d')
z_cone = np.linspace(-3, 3, 40)
theta_cone = np.linspace(0, 2*np.pi, 60)
z_g2, t_g2 = np.meshgrid(z_cone, theta_cone)
r_cone = np.abs(z_g2)
x_cone = r_cone * np.cos(t_g2)
y_cone = r_cone * np.sin(t_g2)
ax2.plot_surface(x_cone, y_cone, z_g2, cmap='Purples', alpha=0.7, edgecolor='none')
ax2.set_title('Double Cone\n$x^2+y^2=z^2$', fontsize=12, fontweight='bold')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')
ax2.view_init(elev=20, azim=-50)

fig.suptitle('Graph 9C3: Hyperboloid of One Sheet vs. Double Cone',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9c3-hyperboloid-cone.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C3 done — Hyperboloid + Cone")


# ================================================================
# 9C4 — Sphere Intersected by a Plane (Circle of intersection)
# ================================================================
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Sphere x²+y²+z²=20 (R ≈ 4.472)
R = np.sqrt(20)
phi = np.linspace(0, np.pi, 40)
theta = np.linspace(0, 2*np.pi, 60)
phi_g, theta_g = np.meshgrid(phi, theta)
x_s = R * np.sin(phi_g) * np.cos(theta_g)
y_s = R * np.sin(phi_g) * np.sin(theta_g)
z_s = R * np.cos(phi_g)
ax.plot_surface(x_s, y_s, z_s, cmap='Blues', alpha=0.2, edgecolor='none')

# Plane x+y+z=6 → z = 6-x-y
xx, yy = np.meshgrid(np.linspace(-1, 5, 30), np.linspace(-1, 5, 30))
zz = 6 - xx - yy
ax.plot_surface(xx, yy, zz, alpha=0.35, color='orange', edgecolor='none')

# Intersection circle center and normal
center = np.array([2, 2, 2])
r_circle = np.sqrt(8)  # 2√2

# Draw intersection circle
u = np.array([1, -1, 0]) / np.sqrt(2)  # orthogonal to normal (1,1,1)
v = np.cross(np.array([1, 1, 1]), u)
v = v / np.linalg.norm(v)
circle_t = np.linspace(0, 2*np.pi, 100)
circle_pts = center[:, None] + r_circle * (u[:, None] * np.cos(circle_t) + v[:, None] * np.sin(circle_t))
ax.plot(circle_pts[0], circle_pts[1], circle_pts[2], 'r-', linewidth=3, label='Intersection circle')

ax.scatter([2], [2], [2], c='red', s=80, label='Center (2,2,2)')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
ax.set_title('Graph 9C4: Sphere x²+y²+z²=20 ∩ Plane x+y+z=6\n'
             'Intersection: circle, center (2,2,2), radius 2√2',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.view_init(elev=22, azim=-60)
plt.tight_layout()
plt.savefig(OUT + '9c4-sphere-plane-intersection.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C4 done — Sphere-plane intersection")

print("\n=== ALL 9B/9C GRAPHS GENERATED ===")
