"""
Graphs for Sessions 23, 24, 25 — Multivariable Calculus.
23: tangent plane, critical points (min/max/saddle)
24: (uses existing level curve and 3D graphs)
25: coordinate systems, vector theorems diagram
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, Arc
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 23: Tangent Plane to z = x² + y² at (1, 2, 5)
# ================================================================
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-0.5, 3, 60)
y = np.linspace(-0.5, 3, 60)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

ax.plot_surface(X, Y, Z, cmap='Blues', alpha=0.5, edgecolor='none', label='_nolegend_')

# Tangent plane: z = 5 + 2(x-1) + 4(y-2) = 2x + 4y - 5
xx, yy = np.meshgrid(np.linspace(0.3, 1.8, 12), np.linspace(1.2, 2.8, 12))
zz = 2*xx + 4*yy - 5
ax.plot_surface(xx, yy, zz, color='orange', alpha=0.7, edgecolor='none', label='_nolegend_')

# Point of tangency
ax.scatter([1], [2], [5], c='red', s=80, zorder=10, label='(1, 2, 5)')

# Gradient arrow
ax.quiver(1, 2, 5, 2, 4, 0, color='darkgreen', linewidth=3, arrow_length_ratio=0.15, label=r'$\nabla f(1,2)$')

ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title(r'Graph 23: Tangent Plane to $z=x^2+y^2$ at (1,2,5)', fontsize=13, fontweight='bold')
ax.legend(fontsize=10, loc='upper left')
ax.view_init(elev=22, azim=-55)

plt.tight_layout()
plt.savefig(OUT + '23-tangent-plane.png', dpi=180, bbox_inches='tight')
plt.close()
print("23 done")


# ================================================================
# 24: Critical Points — Min, Saddle, Max
# ================================================================
fig = plt.figure(figsize=(18, 6))

# Min: z = x² + y²
ax1 = fig.add_subplot(131, projection='3d')
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
ax1.plot_surface(X, Y, Z, cmap='Blues', alpha=0.7, edgecolor='none')
ax1.scatter([0], [0], [0], c='red', s=60, zorder=10)
ax1.set_title(r'Local Minimum (bowl)', fontsize=12, fontweight='bold')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.view_init(elev=25, azim=-50)

# Saddle: z = x² - y²
ax2 = fig.add_subplot(132, projection='3d')
Z2 = X**2 - Y**2
ax2.plot_surface(X, Y, Z2, cmap='RdBu', alpha=0.7, edgecolor='none')
ax2.scatter([0], [0], [0], c='red', s=60, zorder=10)
ax2.set_title(r'Saddle Point (D<0)', fontsize=12, fontweight='bold')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')
ax2.view_init(elev=25, azim=-50)

# Max: z = -x² - y²
ax3 = fig.add_subplot(133, projection='3d')
Z3 = -X**2 - Y**2
ax3.plot_surface(X, Y, Z3, cmap='Oranges', alpha=0.7, edgecolor='none')
ax3.scatter([0], [0], [0], c='red', s=60, zorder=10)
ax3.set_title(r'Local Maximum (hill)', fontsize=12, fontweight='bold')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.view_init(elev=25, azim=-50)

fig.suptitle('Graph 24: Critical Points — Min (D>0, f_xx>0), Saddle (D<0), Max (D>0, f_xx<0)',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '24-critical-points.png', dpi=180, bbox_inches='tight')
plt.close()
print("24 done")


# ================================================================
# 25a: Coordinate Systems Diagram
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Polar
ax = axes[0]
theta = np.linspace(0, 2*np.pi, 100)
for r_val in [0.5, 1.0, 1.5]:
    ax.plot(r_val*np.cos(theta), r_val*np.sin(theta), 'gray', alpha=0.3, linewidth=0.5)
for th in np.linspace(0, 2*np.pi, 9)[:-1]:
    ax.plot([0, 2*np.cos(th)], [0, 2*np.sin(th)], 'gray', alpha=0.2, linewidth=0.5)
# Highlight a point
r_pt, th_pt = 1.5, np.pi/4
ax.plot(r_pt*np.cos(th_pt), r_pt*np.sin(th_pt), 'ro', markersize=8, zorder=5)
ax.annotate(r'$(r,\theta)$', xy=(r_pt*np.cos(th_pt), r_pt*np.sin(th_pt)),
           xytext=(r_pt*np.cos(th_pt)+0.4, r_pt*np.sin(th_pt)+0.3),
           fontsize=12, fontweight='bold', color='red',
           arrowprops=dict(arrowstyle='->', color='red'))
# Small area element
r_small, dr_small = 1.0, 0.3
dth_small = 0.3
rect_theta = np.linspace(th_pt-dth_small/2, th_pt+dth_small/2, 10)
ax.fill_between([r_small*np.cos(t) for t in rect_theta], 
                [r_small*np.sin(t) for t in rect_theta],
                [(r_small+dr_small)*np.sin(t) for t in rect_theta],
                alpha=0.3, color='blue')
ax.set_aspect('equal')
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
ax.set_title(r'Polar: $dA = r\,dr\,d\theta$', fontsize=12, fontweight='bold')
ax.text(1.8, -0.5, r'$r$', fontsize=13, color='blue', fontweight='bold')
ax.axis('off')

# Cylindrical
ax = axes[1]
ax.set_xlim(-2, 2); ax.set_ylim(-1, 3.5)
# Draw a cylinder outline
z_vals = [0, 3]
for z_i in z_vals:
    ax.plot(np.cos(theta), np.sin(theta), 'gray', alpha=0.3, linewidth=0.8)
# Side lines
ax.plot([1, 1], [0, 3], 'gray', alpha=0.4, linewidth=0.8)
ax.plot([-1, -1], [0, 3], 'gray', alpha=0.4, linewidth=0.8)
# Point
ax.plot(0.7, 2.2, 'ro', markersize=8, zorder=5)
ax.annotate(r'$(r,\theta,z)$', xy=(0.7, 2.2), xytext=(0.7+0.8, 2.2+0.3),
           fontsize=12, fontweight='bold', color='red',
           arrowprops=dict(arrowstyle='->', color='red'))
ax.set_title(r'Cylindrical: $dV = r\,dr\,d\theta\,dz$', fontsize=12, fontweight='bold')
ax.text(1.4, 2.5, r'$r$', fontsize=13, color='blue', fontweight='bold')
ax.axis('off')

# Spherical
ax = axes[2]
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
# Sphere outline
phi_circle = np.linspace(0, np.pi, 80)
ax.plot(2*np.sin(phi_circle), 2*np.cos(phi_circle), 'gray', alpha=0.3, linewidth=0.8)
ax.plot(2*np.cos(theta[:50]), 2*np.sin(theta[:50]), 'gray', alpha=0.3, linewidth=0.8)
# Origin
ax.plot(0, 0, 'ko', markersize=4)
# Point
rho_pt, phi_pt = 1.8, np.pi/5
ax.plot(rho_pt*np.sin(phi_pt), rho_pt*np.cos(phi_pt), 'ro', markersize=8, zorder=5)
ax.annotate(r'$(\rho,\phi,\theta)$', xy=(rho_pt*np.sin(phi_pt), rho_pt*np.cos(phi_pt)),
           xytext=(rho_pt*np.sin(phi_pt)+0.5, rho_pt*np.cos(phi_pt)+0.3),
           fontsize=12, fontweight='bold', color='red',
           arrowprops=dict(arrowstyle='->', color='red'))
ax.set_title(r'Spherical: $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$', fontsize=12, fontweight='bold')
ax.text(0.5, -0.5, r'$\rho^2\sin\phi$', fontsize=13, color='blue', fontweight='bold')
ax.set_aspect('equal')
ax.axis('off')

fig.suptitle('Graph 25a: Coordinate Systems and Their Volume Elements',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25-coordinate-systems.png', dpi=180, bbox_inches='tight')
plt.close()
print("25a done")


# ================================================================
# 25b: The Three Theorems — FTC Unification
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6.5))

# Green's Theorem (2D)
ax = axes[0]
theta = np.linspace(0, 2*np.pi, 100)
# Region D (ellipse-like)
t_d = np.linspace(0, 2*np.pi, 100)
x_d = 1.5*np.cos(t_d)
y_d = 1.0*np.sin(t_d)
ax.fill(x_d, y_d, alpha=0.15, color='blue')
ax.plot(x_d, y_d, 'b-', linewidth=2.5, label='C (boundary)')
# Vector field arrows on the boundary
for t_i in np.linspace(0, 2*np.pi, 12):
    x_i, y_i = 1.5*np.cos(t_i), 1.0*np.sin(t_i)
    # tangent-like arrow
    dx_i, dy_i = -1.5*np.sin(t_i)*0.3, 1.0*np.cos(t_i)*0.3
    ax.arrow(x_i, y_i, dx_i, dy_i, head_width=0.12, head_length=0.15, fc='darkblue', alpha=0.6)
# Curl symbol inside
ax.text(0, 0, r'curl = $Q_x-P_y$', fontsize=12, ha='center', fontweight='bold', color='darkred',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax.set_aspect('equal')
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-1.6, 1.6)
ax.set_title(r'Green (2D)', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper right')

# Stokes' Theorem (3D surface)
ax = axes[1]
# Draw a hemisphere-like surface with a boundary
# Simplified: an elliptical surface
phi_s = np.linspace(0, np.pi/2, 20)
theta_s = np.linspace(0, 2*np.pi, 40)
Phi, Theta = np.meshgrid(phi_s, theta_s)
# Projected surface (paraboloid-like)
r_surf = 1 - Phi/(np.pi/2) * 0.2
X_s = r_surf * np.cos(Theta) * 1.5
Y_s = r_surf * np.sin(Theta) * 1.0
Z_s = (1 - r_surf) * 1.0
# Plot as a 2D projection
ax.fill(X_s[:,0], Y_s[:,0], alpha=0.1, color='blue')
for i in range(0, len(phi_s), 3):
    ax.plot(X_s[:,i], Y_s[:,i], 'gray', alpha=0.2, linewidth=0.5)
# Boundary
boundary_x = 1.5*np.cos(theta)
boundary_y = 1.0*np.sin(theta)
ax.plot(boundary_x, boundary_y, 'b-', linewidth=2.5, label='C (boundary)')
ax.text(0, 0, r'$\nabla\times\vec{F}$', fontsize=12, ha='center', fontweight='bold', color='darkred',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax.set_aspect('equal')
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-1.6, 1.6)
ax.set_title(r'Stokes (3D surface)', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper right')

# Divergence Theorem (3D volume)
ax = axes[2]
# Project a sphere as circle, show outward flux
ax.add_patch(plt.Circle((0,0), 1.5, fill=True, alpha=0.1, color='blue', ec='blue', linewidth=2.5, label='S (closed surface)'))
# Outward arrows
for t_i in np.linspace(0, 2*np.pi, 12):
    x_i, y_i = 1.5*np.cos(t_i), 1.5*np.sin(t_i)
    ax.arrow(x_i, y_i, x_i*0.2, y_i*0.2, head_width=0.12, head_length=0.15, fc='darkblue', alpha=0.6)
ax.text(0, 0, r'$\nabla\cdot\vec{F}$', fontsize=12, ha='center', fontweight='bold', color='darkred',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax.set_aspect('equal')
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
ax.set_title(r'Divergence (3D volume)', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper right')

fig.suptitle('Graph 25b: The Three Great Theorems — Boundary = Interior Derivative',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25-vector-theorems.png', dpi=180, bbox_inches='tight')
plt.close()
print("25b done")

print("\n=== SESSIONS 23-25 GRAPHS DONE ===")
