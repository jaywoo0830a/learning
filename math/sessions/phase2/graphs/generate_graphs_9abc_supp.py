"""
Supplementary graphs for 9A, 9B, 9C — adding visual richness.

9a-fold — |f(x)| folding (y = |x²-1|)
9a-stretch — sin x vs 2sin x vs sin 2x
9b-even-odd — even symmetry (x²) vs odd symmetry (x³)
9b-point-circle — point-to-circle distance
9c-plane-3d — a plane ax+by+cz=d in 3D
9c-saddle-3d — hyperbolic paraboloid z = x² - y²
9c-cylinder-3d — circular cylinder
9c-intersecting-cylinders — two perpendicular cylinders
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle as MplCircle
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 9A — Fold: y = |x²-1| (absolute value of function)
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
ax1, ax2 = axes

x = np.linspace(-2.5, 2.5, 400)

# Before folding
y_before = x**2 - 1
ax1.plot(x, y_before, 'b-', linewidth=2.5, label=r'$y=x^2-1$')
ax1.fill_between(x, y_before, 0, where=(y_before<0), alpha=0.3, color='coral', label='Below x-axis')
ax1.axhline(0, color='gray', lw=0.5)
ax1.set_title('Before: $y=x^2-1$\n(negative between −1 and 1)', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9); ax1.grid(alpha=0.15)
ax1.set_ylim(-1.5, 4)

# After folding
y_after = np.abs(x**2 - 1)
ax2.plot(x, y_after, 'darkred', linewidth=2.5, label=r'$y=|x^2-1|$')
ax2.fill_between(x, 0, y_after, alpha=0.2, color='steelblue')
# Show the fold arrow
ax2.annotate('', xy=(0, 1), xytext=(0, 0.2),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax2.text(0.3, 0.5, 'FOLD', fontsize=11, color='red', fontweight='bold')
ax2.axhline(0, color='gray', lw=0.5)
ax2.set_title('After: $y=|x^2-1|$\n(negative part folded upward)', fontsize=12, fontweight='bold')
ax2.legend(fontsize=9); ax2.grid(alpha=0.15)
ax2.set_ylim(-0.2, 4)

fig.suptitle('Graph 9A: The Fold — $|f(x)|$ Wraps Everything Upward',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9a-fold-absolute-value.png', dpi=180, bbox_inches='tight')
plt.close()
print("9A fold done")


# ================================================================
# 9A — Stretch: sin x vs 2sin x vs sin(2x)
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
ax1, ax2 = axes

x = np.linspace(0, 2*np.pi, 400)
ax1.plot(x, np.sin(x), 'b-', linewidth=2.5, label=r'$\sin x$ (height=1)')
ax1.plot(x, 2*np.sin(x), 'r--', linewidth=2.2, label=r'$2\sin x$ (height=2)')
ax1.plot(x, 0.5*np.sin(x), 'g--', linewidth=2.2, label=r'$\frac{1}{2}\sin x$ (height=½)')
ax1.axhline(0, color='gray', lw=0.4)
ax1.set_title('Vertical Stretch ($a$ changes amplitude)', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9); ax1.grid(alpha=0.15)
ax1.set_ylim(-2.5, 2.5)

ax2.plot(x, np.sin(x), 'b-', linewidth=2.5, label=r'$\sin x$ (period $2\pi$)')
ax2.plot(x, np.sin(2*x), 'r--', linewidth=2.2, label=r'$\sin(2x)$ (period $\pi$)')
ax2.plot(x, np.sin(0.5*x), 'g--', linewidth=2.2, label=r'$\sin(x/2)$ (period $4\pi$)')
ax2.axhline(0, color='gray', lw=0.4)
ax2.set_title('Horizontal Stretch ($b$ changes period)', fontsize=12, fontweight='bold')
ax2.legend(fontsize=9); ax2.grid(alpha=0.15)
ax2.set_ylim(-1.5, 1.5)

fig.suptitle('Graph 9A: Stretch and Shrink — $a\\cdot f(bx)$',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9a-stretch-comparison.png', dpi=180, bbox_inches='tight')
plt.close()
print("9A stretch done")


# ================================================================
# 9B — Even and Odd Symmetry
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
ax1, ax2 = axes

x = np.linspace(-3, 3, 400)
# Even: f(x)=x²
ax1.plot(x, x**2, 'b-', linewidth=2.8, label=r'$f(x)=x^2$')
ax1.axvline(0, color='gray', lw=0.8, alpha=0.5)
# Show mirror: draw arrows showing (2,4) ↔ (-2,4)
for xp in [1, 2]:
    yp = xp**2
    ax1.annotate('', xy=(-xp, yp), xytext=(xp, yp),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1.5, linestyle='--'))
ax1.text(0, 8, 'MIRROR across y-axis', fontsize=11, ha='center', color='red',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax1.set_title('Even Function: $f(-x)=f(x)$\nSymmetric about y-axis', fontsize=12, fontweight='bold')
ax1.legend(fontsize=10); ax1.grid(alpha=0.15)

# Odd: f(x)=x³
ax2.plot(x, x**3, 'darkgreen', linewidth=2.8, label=r'$f(x)=x^3$')
ax2.axhline(0, color='gray', lw=0.5, alpha=0.5)
ax2.axvline(0, color='gray', lw=0.5, alpha=0.5)
for xp in [1, 2]:
    yp = xp**3
    ax2.plot(xp, yp, 'o', color='darkgreen', markersize=8)
    ax2.plot(-xp, -yp, 'o', color='darkgreen', markersize=8)
    ax2.annotate('', xy=(-xp, -yp), xytext=(xp, yp),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1.5, linestyle='--',
                               connectionstyle='arc3,rad=0.3'))
ax2.text(0, -22, 'ROTATE 180° around origin', fontsize=11, ha='center', color='red',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax2.set_title('Odd Function: $f(-x)=-f(x)$\nSymmetric about origin', fontsize=12, fontweight='bold')
ax2.legend(fontsize=10); ax2.grid(alpha=0.15)
ax2.set_ylim(-30, 30)

fig.suptitle('Graph 9B: Even and Odd Symmetry — Two Types of Mirror',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9b-even-odd-symmetry.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B even/odd done")


# ================================================================
# 9B — Point-to-Circle Distance
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

R = 3
theta = np.linspace(0, 2*np.pi, 300)
ax.plot(R*np.cos(theta), R*np.sin(theta), 'b-', linewidth=2.5, label=f'Circle: $x^2+y^2={R^2}$')
ax.plot(0, 0, 'bo', markersize=8, label='Center (0,0)')

# Point P(5,0)
ax.plot(5, 0, 'ro', markersize=10, zorder=5, label='P(5,0)')
# Closest point on circle: (3,0)
ax.plot(3, 0, 'go', markersize=10, zorder=5, label='Closest (3,0)')
ax.plot([5, 3], [0, 0], 'r-', linewidth=2.5, label='Distance = 5−3 = 2')
ax.plot([0, 5], [0, 0], 'gray', linestyle=':', linewidth=1)

# Annotations
ax.annotate('R=3', (1.5, 0.5), fontsize=12)
ax.annotate('|PC|=5', (2.5, -0.8), fontsize=11, color='gray')
ax.annotate('d = |PC| − R\n   = 5 − 3 = 2', (4, 1.2), fontsize=13, fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax.set_aspect('equal')
ax.set_xlim(-2, 7); ax.set_ylim(-4, 4)
ax.set_xlabel('x', fontsize=13); ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 9B: Point-to-Circle Distance\nShortest = |distance to center − radius|',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10, loc='upper left'); ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '9b-point-circle-distance.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B point-circle done")


# ================================================================
# 9C — Plane in 3D: 2x + 3y - z = 6
# ================================================================
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

# Plane 2x + 3y - z = 6 → z = 2x + 3y - 6
xx, yy = np.meshgrid(np.linspace(-1, 5, 25), np.linspace(-1, 4, 25))
zz = 2*xx + 3*yy - 6
ax.plot_surface(xx, yy, zz, alpha=0.4, color='steelblue', edgecolor='none')

# Intercepts
ax.scatter([3, 0, 0], [0, 2, 0], [0, 0, -6], c='red', s=80, zorder=5)
ax.text(3.3, 0, 0, '(3,0,0)', fontsize=10, color='red')
ax.text(0, 2.3, 0, '(0,2,0)', fontsize=10, color='red')
ax.text(0, 0, -5.5, '(0,0,−6)', fontsize=10, color='red')

# Normal vector (2,3,-1)
ax.quiver(0, 0, 0, 2, 3, -1, color='darkred', linewidth=2.5, arrow_length_ratio=0.15,
          label='Normal n⃗=(2,3,−1)')

ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
ax.set_title('Graph 9C: A Plane in 3D — $2x+3y-z=6$\nIntercepts + Normal Vector',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.view_init(elev=22, azim=-55)
plt.tight_layout()
plt.savefig(OUT + '9c-plane-3d.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C plane done")


# ================================================================
# 9C — Hyperbolic Paraboloid (Saddle): z = x² − y²
# ================================================================
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-2.5, 2.5, 60)
y = np.linspace(-2.5, 2.5, 60)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.75, edgecolor='none')

# Saddle point
ax.scatter([0], [0], [0], c='black', s=100, zorder=10)
ax.text(0, 0, 0.5, 'Saddle point', fontsize=11, ha='center')

ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
ax.set_title('Graph 9C: Hyperbolic Paraboloid (Saddle)\n$z=x^2-y^2$ — curves up in x, down in y',
             fontsize=13, fontweight='bold')
ax.view_init(elev=25, azim=-55)
plt.tight_layout()
plt.savefig(OUT + '9c-saddle-3d.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C saddle done")


# ================================================================
# 9C — Circular Cylinder x² + y² = 1
# ================================================================
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

z = np.linspace(-3, 3, 40)
theta = np.linspace(0, 2*np.pi, 80)
Z, THETA = np.meshgrid(z, theta)
X = np.cos(THETA)
Y = np.sin(THETA)

ax.plot_surface(X, Y, Z, cmap='Greens', alpha=0.6, edgecolor='none')

# Show that z is free — draw a few horizontal circles
for z_val in [-2, 0, 2]:
    ax.plot(np.cos(theta), np.sin(theta), z_val, 'darkgreen', linewidth=1.5, alpha=0.7)

ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z (free)', fontsize=12)
ax.set_title('Graph 9C: Circular Cylinder $x^2+y^2=1$\nA circle extruded infinitely along z',
             fontsize=13, fontweight='bold')
ax.view_init(elev=15, azim=-50)
plt.tight_layout()
plt.savefig(OUT + '9c-cylinder-3d.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C cylinder done")


# ================================================================
# 9C — Two Intersecting Cylinders
# ================================================================
fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2*np.pi, 80)
z = np.linspace(-2, 2, 20)
THETA, Z = np.meshgrid(theta, z)

# Cylinder 1: x²+y²=1 (vertical, along z)
X1 = np.cos(THETA); Y1 = np.sin(THETA)
ax.plot_surface(X1, Y1, Z, cmap='Blues', alpha=0.25, edgecolor='none')

# Cylinder 2: x²+z²=1 (along y)
Y_vals = np.linspace(-2, 2, 20)
THETA2, Y2 = np.meshgrid(theta, Y_vals)
X2 = np.cos(THETA2); Z2 = np.sin(THETA2)
ax.plot_surface(X2, Y2, Z2, cmap='Oranges', alpha=0.25, edgecolor='none')

# Intersection curve (bicylindrical curve)
t_int = np.linspace(0, 2*np.pi, 200)
x_int = np.cos(t_int)
y_int = np.sin(t_int)
z_int = np.sin(t_int)
# But the intersection is where both satisfy each other: x²+y²=1 and x²+z²=1 → y²=z² → z=±y
x_curve = np.cos(t_int)
y_curve = np.sin(t_int)
z_curve_pos = np.abs(np.sin(t_int))
z_curve_neg = -np.abs(np.sin(t_int))

# Actually the true intersection curve is more complex. Draw a simplified version:
# Points satisfying x²+y²=1 and x²+z²=1 simultaneously
# Results in curves z=±y
t_curve = np.linspace(0, np.pi, 100)
for sign in [1, -1]:
    x_c = np.cos(t_curve)
    y_c = np.sin(t_curve)
    z_c = sign * np.sin(t_curve)
    ax.plot(x_c, y_c, z_c, 'red', linewidth=3, label='Intersection curve' if sign==1 else '')

ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
ax.set_title('Graph 9C: Intersecting Cylinders\n$x^2+y^2=1$ and $x^2+z^2=1$',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.view_init(elev=22, azim=-50)
plt.tight_layout()
plt.savefig(OUT + '9c-intersecting-cylinders.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C intersecting cylinders done")

print("\n=== ALL SUPPLEMENTARY 9ABC GRAPHS GENERATED ===")
