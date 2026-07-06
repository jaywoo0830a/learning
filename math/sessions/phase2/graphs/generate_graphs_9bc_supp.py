"""
Supplementary graphs for 9B and 9C — additional key visualizations.

9b4 — Inverse function: reflection across y=x
9c5 — Elliptic paraboloid z = x² + y²
9c6 — Domain of z = √(4-x²-y²): disk in xy-plane
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 9B4 — Inverse Function: Reflection Across y = x
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

# f(x) = 2x+1 (linear)
x_f = np.linspace(-3, 4, 200)
y_f = 2*x_f + 1
ax.plot(x_f, y_f, 'b-', linewidth=3, label=r'$f(x)=2x+1$')

# f⁻¹(x) = (x-1)/2
x_inv = np.linspace(-5, 9, 200)
y_inv = (x_inv - 1) / 2
ax.plot(x_inv, y_inv, 'r-', linewidth=3, label=r'$f^{-1}(x)=\frac{x-1}{2}$')

# y = x mirror line
x_mirror = np.linspace(-5, 10, 200)
ax.plot(x_mirror, x_mirror, 'k--', linewidth=1.5, alpha=0.6, label=r'$y=x$ (mirror)')

# Show reflection of specific points
points = [(0, 1), (1, 3), (2, 5)]
for px, py in points:
    ax.plot(px, py, 'bo', markersize=10, zorder=5)
    ax.plot(py, px, 'ro', markersize=10, zorder=5)
    # Dashed connection line perpendicular to y=x
    mid = ((px+py)/2, (py+px)/2)
    ax.plot([px, py], [py, px], 'gray', linewidth=0.8, linestyle=':', alpha=0.6)

# Annotate one pair
ax.annotate('(1,3)', (1, 3), textcoords='offset points', xytext=(-30, -15),
            fontsize=11, color='blue', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='blue'))
ax.annotate('(3,1)', (3, 1), textcoords='offset points', xytext=(8, -20),
            fontsize=11, color='red', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red'))

ax.set_aspect('equal')
ax.set_xlim(-4, 10)
ax.set_ylim(-4, 10)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 9B4: Inverse Function = Reflection Across y = x\n'
             r'Every point (a,b) on $f$ becomes (b,a) on $f^{-1}$',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '9b4-inverse-reflection.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B4 done — Inverse function reflection")


# ================================================================
# 9C5 — Elliptic Paraboloid z = x² + y²
# ================================================================
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

# Surface
x = np.linspace(-2.5, 2.5, 60)
y = np.linspace(-2.5, 2.5, 60)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.75, edgecolor='none')

# Draw a few level curves on the surface
for c in [1, 2, 3, 4, 5]:
    theta = np.linspace(0, 2*np.pi, 150)
    r = np.sqrt(c)
    x_c = r * np.cos(theta)
    y_c = r * np.sin(theta)
    z_c = np.full_like(theta, c)
    ax.plot(x_c, y_c, z_c, 'white', linewidth=1.2, alpha=0.7)

# Mark vertex
ax.scatter([0], [0], [0], c='black', s=80, zorder=10)

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z (height)', fontsize=12)
ax.set_title('Graph 9C5: Elliptic Paraboloid z = x² + y²\n'
             'Level curves are circles x²+y²=c (white rings)',
             fontsize=13, fontweight='bold')
ax.view_init(elev=25, azim=-55)
plt.tight_layout()
plt.savefig(OUT + '9c5-paraboloid.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C5 done — Elliptic paraboloid")


# ================================================================
# 9C6 — Domain: Disk (for z = √(4-x²-y²))
# ================================================================
fig, ax = plt.subplots(figsize=(9, 9))

# Draw the disk x² + y² ≤ 4
theta = np.linspace(0, 2*np.pi, 300)
r_disk = 2
ax.fill(r_disk*np.cos(theta), r_disk*np.sin(theta), alpha=0.3, color='steelblue')
ax.plot(r_disk*np.cos(theta), r_disk*np.sin(theta), 'b-', linewidth=2.5, label='Boundary: x²+y²=4')

# Shade the interior
for r_shade in np.linspace(0.3, 1.7, 6):
    ax.plot(r_shade*np.cos(theta), r_shade*np.sin(theta), 'steelblue', linewidth=0.6, alpha=0.35)

# Mark center
ax.plot(0, 0, 'ko', markersize=8, label='Center (0,0)')

# Annotate
ax.annotate('Domain:\nDisk of\nradius 2', xy=(1.2, 1.2), fontsize=13, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax.annotate('√(4−x²−y²)\nrequires\nx²+y² ≤ 4', xy=(-1.2, -1.2), fontsize=12,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 9C6: Domain of z = √(4 − x² − y²)\n'
             'All points (x,y) satisfying x² + y² ≤ 4',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
ax.axhline(0, color='gray', lw=0.35)
ax.axvline(0, color='gray', lw=0.35)
plt.tight_layout()
plt.savefig(OUT + '9c6-domain-disk.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C6 done — Domain visualization")

print("\n=== SUPPLEMENTARY GRAPHS DONE ===")
