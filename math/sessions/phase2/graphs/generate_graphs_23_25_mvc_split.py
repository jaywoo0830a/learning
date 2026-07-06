"""
New graphs for MVC split sessions 23A-25C.
23A: path-limit (two paths→two limits), polar-squeeze
23B: gradient-contour (∇f ⟂ level curves)
24A: chain-rule-tree, implicit-surface
24B: lagrange-geometry
25A: fubini-swap
25B: spherical-breakdown
25C: conservative-field (conservative vs non-conservative)
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch, Circle, Arc, Polygon
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 23A: Path Limit — Two paths, two limits for f=xy/(x²+y²)
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Left: 3D surface plot
ax = axes[0]
ax = fig.add_subplot(121, projection='3d')
r = np.linspace(0.01, 2, 40)
theta = np.linspace(0, 2*np.pi, 80)
R, T = np.meshgrid(r, theta)
X, Y = R*np.cos(T), R*np.sin(T)
Z = X*Y / (X**2 + Y**2 + 1e-10)
surf = ax.plot_surface(X, Y, Z, cmap='RdBu', alpha=0.7, edgecolor='none', vmin=-0.5, vmax=0.5)

# y=0 path (limit 0)
t_path = np.linspace(0.02, 2, 50)
ax.plot(t_path, 0*t_path, 0*t_path, 'b-', linewidth=3, label='y=0: limit=0', zorder=10)
# y=x path (limit 1/2)
ax.plot(t_path, t_path, 0*t_path+0.5, 'r-', linewidth=3, label='y=x: limit=1/2', zorder=10)
ax.scatter([0], [0], [0], c='k', s=50, zorder=10)
ax.set_title(r'$f(x,y)=xy/(x^2+y^2)$ — Rip at Origin', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.view_init(elev=30, azim=-60)

# Right: Top-down path view
ax2 = fig.add_subplot(122)
theta_c = np.linspace(0, 2*np.pi, 100)
ax2.add_patch(Circle((0,0), 1.5, fill=False, ec='gray', alpha=0.3))
ax2.plot([0, 1.5], [0, 0], 'b-', linewidth=2.5, label='Path 1: y=0 → lim=0')
ax2.plot([0, 1.06], [0, 1.06], 'r-', linewidth=2.5, label='Path 2: y=x → lim=1/2')
# Many radial paths
for ang in np.linspace(0.2, np.pi/2-0.2, 6):
    ax2.plot([0, 1.3*np.cos(ang)], [0, 1.3*np.sin(ang)], 'gray', alpha=0.2, linewidth=0.5)
ax2.set_xlim(-1.8, 1.8); ax2.set_ylim(-0.3, 1.8)
ax2.set_aspect('equal')
ax2.set_title('Different paths → Different limits', fontsize=12, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(alpha=0.1)

fig.suptitle('Graph 23A: Two-Path Test — Limit Does NOT Exist', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '23a-path-limit.png', dpi=180, bbox_inches='tight')
plt.close()
print("23a-path-limit done")


# ================================================================
# 23A: Polar Squeeze — f=x³/(x²+y²) surface, smooth at origin
# ================================================================
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
r = np.linspace(0.01, 2, 40)
theta = np.linspace(0, 2*np.pi, 80)
R, T = np.meshgrid(r, theta)
X, Y = R*np.cos(T), R*np.sin(T)
Z = X**3 / (X**2 + Y**2 + 1e-10)
surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.75, edgecolor='none')

# Show that as r→0, z→0 from all directions
for ang in [0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3]:
    r_line = np.linspace(0, 2, 40)
    x_line = r_line*np.cos(ang)
    y_line = r_line*np.sin(ang)
    z_line = (x_line**3) / (x_line**2 + y_line**2 + 1e-10)
    ax.plot(x_line, y_line, z_line, 'white', linewidth=1.5, alpha=0.7)

ax.scatter([0], [0], [0], c='red', s=60, zorder=10)
ax.set_title(r'$f(x,y)=x^3/(x^2+y^2)$ — Continuous at Origin', fontsize=13, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.view_init(elev=28, azim=-55)

plt.tight_layout()
plt.savefig(OUT + '23a-polar-squeeze.png', dpi=180, bbox_inches='tight')
plt.close()
print("23a-polar-squeeze done")


# ================================================================
# 23B: Gradient + Contour — ∇f ⟂ level curves
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Level curves
levels = [0.5, 1, 2, 3, 5, 7, 9, 12]
contour = ax.contour(X, Y, Z, levels=levels, colors='blue', alpha=0.5, linewidths=1.2)
ax.clabel(contour, fontsize=8)

# Gradient vectors at selected points
pts = [(1,0), (0,1.5), (2,1), (1.5,1.5), (2.5,0.5), (-1,2)]
for px, py in pts:
    gx, gy = 2*px, 2*py
    ax.arrow(px, py, gx*0.18, gy*0.18, head_width=0.15, head_length=0.2, 
             fc='red', ec='red', alpha=0.85, linewidth=1.8)

ax.set_aspect('equal')
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
ax.set_title(r'Graph 23B: $\nabla f$ (red) $\perp$ Level Curves (blue) — $f(x,y)=x^2+y^2$',
             fontsize=13, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(alpha=0.08)

plt.tight_layout()
plt.savefig(OUT + '23b-gradient-contour.png', dpi=180, bbox_inches='tight')
plt.close()
print("23b-gradient-contour done")


# ================================================================
# 24A: Chain Rule Tree Diagram
# ================================================================
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10); ax.set_ylim(0, 8)
ax.axis('off')

# Nodes
ax.text(5, 7, r'$z = f(x,y)$', fontsize=16, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
ax.text(2.5, 4.5, r'$x$', fontsize=14, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
ax.text(7.5, 4.5, r'$y$', fontsize=14, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
ax.text(1, 2, r'$u$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(4, 2, r'$v$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(6.5, 2, r'$u$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(9, 2, r'$v$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Edges z→x,y
ax.annotate('', xy=(2.5, 5), xytext=(4.8, 6.5), arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.annotate('', xy=(7.5, 5), xytext=(5.2, 6.5), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax.text(3.5, 6.2, r'$\frac{\partial z}{\partial x}$', fontsize=11, color='red', fontweight='bold')
ax.text(6.2, 6.2, r'$\frac{\partial z}{\partial y}$', fontsize=11, color='blue', fontweight='bold')

# Edges x→u,v
ax.annotate('', xy=(1, 2.5), xytext=(2.3, 4), arrowprops=dict(arrowstyle='->', color='darkred', lw=1.5))
ax.annotate('', xy=(4, 2.5), xytext=(2.7, 4), arrowprops=dict(arrowstyle='->', color='darkred', lw=1.5))
ax.text(1.2, 3.3, r'$\frac{\partial x}{\partial u}$', fontsize=9, color='darkred')
ax.text(3.8, 3.3, r'$\frac{\partial x}{\partial v}$', fontsize=9, color='darkred')

# Edges y→u,v
ax.annotate('', xy=(6.5, 2.5), xytext=(7.3, 4), arrowprops=dict(arrowstyle='->', color='darkblue', lw=1.5))
ax.annotate('', xy=(9, 2.5), xytext=(7.7, 4), arrowprops=dict(arrowstyle='->', color='darkblue', lw=1.5))
ax.text(6.8, 3.3, r'$\frac{\partial y}{\partial u}$', fontsize=9, color='darkblue')
ax.text(8.5, 3.3, r'$\frac{\partial y}{\partial v}$', fontsize=9, color='darkblue')

# Formulas at bottom
ax.text(5, 0.5, r'$\frac{\partial z}{\partial u} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial u}$',
        fontsize=13, ha='center', fontweight='bold', color='purple',
        bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.6))
ax.text(5, -0.3, r'Sum over all paths from $z$ to $u$', fontsize=10, ha='center', color='gray')

ax.set_title('Graph 24A: Chain Rule Tree Diagram', fontsize=14, fontweight='bold', y=1.01)

plt.tight_layout()
plt.savefig(OUT + '24a-chain-rule-tree.png', dpi=180, bbox_inches='tight')
plt.close()
print("24a-chain-rule-tree done")


# ================================================================
# 24A: Implicit Surface — Tangent plane to F(x,y,z)=0
# ================================================================
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

phi = np.linspace(0, np.pi, 35)
theta = np.linspace(0, 2*np.pi, 55)
Phi, Theta = np.meshgrid(phi, theta)
R = np.sqrt(14)
X = R*np.sin(Phi)*np.cos(Theta)
Y = R*np.sin(Phi)*np.sin(Theta)
Z = R*np.cos(Phi)

ax.plot_surface(X, Y, Z, cmap='Blues', alpha=0.35, edgecolor='none')

# Tangent plane at (1,2,3): x+2y+3z=14
xx, yy = np.meshgrid(np.linspace(-1, 3, 10), np.linspace(0, 4, 10))
zz = (14 - xx - 2*yy) / 3
ax.plot_surface(xx, yy, zz, color='orange', alpha=0.55, edgecolor='none')

# Normal vector
ax.quiver(1, 2, 3, 1, 2, 3, color='darkgreen', linewidth=3, arrow_length_ratio=0.12,
          label=r'$\nabla F = \langle 2,4,6 \rangle$')
ax.scatter([1], [2], [3], c='red', s=60, zorder=10, label='(1,2,3)')

ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title(r'Graph 24A: Implicit Surface $x^2+y^2+z^2=14$ + Tangent Plane',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=9, loc='upper left')
ax.view_init(elev=20, azim=-55)

plt.tight_layout()
plt.savefig(OUT + '24a-implicit-surface.png', dpi=180, bbox_inches='tight')
plt.close()
print("24a-implicit-surface done")


# ================================================================
# 24B: Lagrange Multiplier Geometry
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

x = np.linspace(0, 8, 250)
y = np.linspace(0, 8, 250)
X, Y = np.meshgrid(x, y)
Z = X*Y  # f(x,y)=xy

# Level curves of f
levels_f = [2, 6, 10, 14, 16, 18, 22]
contour_f = ax.contour(X, Y, Z, levels=levels_f, colors='red', alpha=0.5, linewidths=1.5)
ax.clabel(contour_f, fontsize=9)

# Constraint: x+y=8
x_line = np.linspace(0, 8, 100)
ax.plot(x_line, 8-x_line, 'b-', linewidth=3, label=r'$x+y=8$')

# Optimum point
ax.plot(4, 4, 'ro', markersize=12, zorder=10)
ax.annotate('(4,4)', xy=(4, 4), xytext=(5.5, 5), fontsize=13, fontweight='bold', color='darkred',
           arrowprops=dict(arrowstyle='->', color='darkred', lw=2))

# Gradient vectors at optimum
ax.arrow(4, 4, 0.6, 0.6, head_width=0.2, head_length=0.25, fc='red', ec='red', linewidth=2.5,
         label=r'$\nabla f = \langle 4,4 \rangle$')
ax.arrow(4, 4, 0.6, 0.6, head_width=0.2, head_length=0.25, fc='blue', ec='blue', linewidth=2.5,
         linestyle='--', label=r'$\lambda\nabla g$ (parallel)')

ax.set_aspect('equal')
ax.set_xlim(0, 8); ax.set_ylim(0, 8)
ax.set_title(r'Graph 24B: Lagrange Multipliers — $\nabla f \parallel \nabla g$ at Optimum',
             fontsize=13, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.legend(fontsize=10, loc='upper right')
ax.grid(alpha=0.08)

plt.tight_layout()
plt.savefig(OUT + '24b-lagrange-geometry.png', dpi=180, bbox_inches='tight')
plt.close()
print("24b-lagrange-geometry done")


# ================================================================
# 25A: Fubini Swap Diagram
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Left: dy dx order
ax = axes[0]
x_vals = np.linspace(0, 1, 8)
for i, xv in enumerate(x_vals):
    ax.plot([xv, xv], [0, xv], 'b-', alpha=0.4, linewidth=1)
    if i % 2 == 0:
        ax.annotate('', xy=(xv, xv-0.01), xytext=(xv, 0.01),
                   arrowprops=dict(arrowstyle='<->', color='blue', alpha=0.6, lw=1.2))
ax.fill_between(np.linspace(0, 1, 100), 0, np.linspace(0, 1, 100), alpha=0.12, color='blue')
ax.plot([0, 1], [0, 1], 'k-', linewidth=2)
ax.set_title(r'Order: $dy\,dx$' + '\nfor each $x$, $y$: $0\to x$', fontsize=12, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_xlim(-0.05, 1.1); ax.set_ylim(-0.05, 1.1)
ax.set_aspect('equal')
ax.grid(alpha=0.08)
ax.text(0.5, 0.25, r'$\int_0^1\int_0^x f\,dy\,dx$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Right: dx dy order
ax = axes[1]
y_vals = np.linspace(0, 1, 8)
for i, yv in enumerate(y_vals):
    ax.plot([yv, 1], [yv, yv], 'r-', alpha=0.4, linewidth=1)
    if i % 2 == 0:
        ax.annotate('', xy=(0.99, yv), xytext=(yv+0.01, yv),
                   arrowprops=dict(arrowstyle='<->', color='red', alpha=0.6, lw=1.2))
ax.fill_between(np.linspace(0, 1, 100), 0, np.linspace(0, 1, 100), alpha=0.12, color='red')
ax.plot([0, 1], [0, 1], 'k-', linewidth=2)
ax.set_title(r'Order: $dx\,dy$' + '\nfor each $y$, $x$: $y\to 1$', fontsize=12, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_xlim(-0.05, 1.1); ax.set_ylim(-0.05, 1.1)
ax.set_aspect('equal')
ax.grid(alpha=0.08)
ax.text(0.65, 0.5, r'$\int_0^1\int_y^1 f\,dx\,dy$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('Graph 25A: Fubini — Same Region, Two Integration Orders',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25a-fubini-swap.png', dpi=180, bbox_inches='tight')
plt.close()
print("25a-fubini-swap done")


# ================================================================
# 25B: Spherical Coordinates Breakdown
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Earth-like sphere silhouette
phi = np.linspace(0, np.pi, 80)
ax.plot(2*np.sin(phi), 2*np.cos(phi), 'gray', linewidth=1.5, alpha=0.5)
ax.plot(2*np.cos(np.linspace(0, 2*np.pi, 100)), 2*np.sin(np.linspace(0, 2*np.pi, 100)), 
        'gray', linewidth=1, alpha=0.3)

# Origin
ax.plot(0, 0, 'ko', markersize=4)

# Point
rho_pt, phi_pt = 1.8, np.pi/4
x_pt, y_pt = rho_pt*np.sin(phi_pt), rho_pt*np.cos(phi_pt)
ax.plot(x_pt, y_pt, 'ro', markersize=10, zorder=10)

# Radial line
ax.plot([0, x_pt], [0, y_pt], 'r-', linewidth=1.5, alpha=0.6)
ax.text(x_pt/2, y_pt/2-0.3, r'$\rho$', fontsize=14, color='red', fontweight='bold')

# φ arc
phi_arc = np.linspace(0, phi_pt, 30)
ax.plot(0.6*np.sin(phi_arc), 0.6*np.cos(phi_arc), 'blue', linewidth=2)
ax.text(0.35, 0.5, r'$\phi$', fontsize=13, color='blue', fontweight='bold')

# dρ, ρdφ, ρsinφ dθ annotations
# Radial increment
ax.annotate(r'$d\rho$', xy=(x_pt*0.7, y_pt*0.7), xytext=(x_pt*0.7+0.4, y_pt*0.7-0.3),
           fontsize=12, color='red', fontweight='bold',
           arrowprops=dict(arrowstyle='->', color='red'))

# Polar arc
ax.annotate(r'$\rho\,d\phi$', xy=(x_pt*0.85, y_pt*0.85+0.15), xytext=(x_pt+0.3, y_pt+0.6),
           fontsize=12, color='blue', fontweight='bold',
           arrowprops=dict(arrowstyle='->', color='blue'))

# Azimuthal arc (out of plane — draw as curved arrow)
ax.annotate(r'$\rho\sin\phi\,d\theta$', xy=(x_pt, y_pt), xytext=(x_pt+0.8, y_pt-0.7),
           fontsize=12, color='darkgreen', fontweight='bold',
           arrowprops=dict(arrowstyle='->', color='darkgreen', connectionstyle='arc3,rad=0.4'))

# Jacobian formula
ax.text(0, -1.8, r'$dV = \rho^2\sin\phi\;d\rho\,d\phi\,d\theta$', fontsize=16, ha='center',
        fontweight='bold', color='purple',
        bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))
ax.text(0, -2.2, r'= $(d\rho) \cdot (\rho\,d\phi) \cdot (\rho\sin\phi\,d\theta)$', fontsize=12, ha='center', color='gray')

ax.set_title('Graph 25B: Spherical Volume Element Breakdown', fontsize=14, fontweight='bold', y=1.01)

plt.tight_layout()
plt.savefig(OUT + '25b-spherical-breakdown.png', dpi=180, bbox_inches='tight')
plt.close()
print("25b-spherical-breakdown done")


# ================================================================
# 25C: Conservative vs Non-Conservative Field
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Left: Conservative field F = ⟨2x, 2y⟩ = ∇(x²+y²)
ax = axes[0]
x = np.linspace(-2, 2, 14)
y = np.linspace(-2, 2, 14)
X, Y = np.meshgrid(x, y)
U, V = 2*X, 2*Y
ax.quiver(X, Y, U, V, color='darkgreen', alpha=0.7, scale=40, width=0.004)

# Two paths from (-1.5,-1.5) to (1.5,1.5)
# Path 1: straight
ax.plot([-1.5, 1.5], [-1.5, 1.5], 'b-', linewidth=2.5, label='Path 1 (straight)')
# Path 2: curved
t_c = np.linspace(0, 1, 100)
x_c = -1.5 + 3*t_c
y_c = -1.5 + 3*t_c + 1.5*np.sin(np.pi*t_c)
ax.plot(x_c, y_c, 'r--', linewidth=2.5, label='Path 2 (curved)')
ax.plot(-1.5, -1.5, 'ko', markersize=8)
ax.plot(1.5, 1.5, 'ko', markersize=8)
ax.text(-1.5, -1.5, 'A', fontsize=12, fontweight='bold', va='top', ha='right')
ax.text(1.5, 1.5, 'B', fontsize=12, fontweight='bold', va='bottom', ha='left')

# Level curves of potential
theta_l = np.linspace(0, 2*np.pi, 100)
for r in [0.5, 1.0, 1.5, 2.0, 2.5]:
    ax.plot(r*np.cos(theta_l), r*np.sin(theta_l), 'gray', alpha=0.15, linewidth=0.5)

ax.set_title(r'Conservative: $\vec{F}=\nabla(x^2+y^2)$' + '\nWork = same on both paths', fontsize=12, fontweight='bold')
ax.set_aspect('equal')
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
ax.legend(fontsize=9, loc='lower right')
ax.grid(alpha=0.08)

# Right: Non-conservative field F = ⟨−y, x⟩
ax = axes[1]
U2, V2 = -Y, X
ax.quiver(X, Y, U2, V2, color='darkred', alpha=0.7, scale=30, width=0.004)

# Closed loop: circle
t_circ = np.linspace(0, 2*np.pi, 100)
ax.plot(1.5*np.cos(t_circ), 1.5*np.sin(t_circ), 'b-', linewidth=3, label=r'Closed loop $C$')
ax.text(1.1, 1.1, r'$\oint_C \neq 0$', fontsize=14, color='darkred', fontweight='bold')

ax.set_title(r'Non-Conservative: $\vec{F}=\langle -y,x\rangle$' + '\nCirculation around loop ≠ 0', fontsize=12, fontweight='bold')
ax.set_aspect('equal')
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
ax.legend(fontsize=9)
ax.grid(alpha=0.08)

fig.suptitle('Graph 25C: Conservative vs Non-Conservative Vector Fields',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '25c-conservative-field.png', dpi=180, bbox_inches='tight')
plt.close()
print("25c-conservative-field done")

print("\n=== ALL 7 NEW MVC SPLIT GRAPHS DONE ===")
