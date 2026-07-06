"""
Step-by-step progressive build-up graphs for 9B and 9C.

9B:
  b-step-composition   — f∘g pipeline: x→g→g(x)→f→f(g(x)) visual chain
  b-step-inverse       — y=x reflection: point-by-point mapping
  b-step-conics        — 4-panel conic build: circle→ellipse→parabola→hyperbola
  b-step-cycloid       — cycloid: wheel at 4 positions, point trace

9C:
  c-step-surface       — z=x²+y²: wireframe→surface→level curves overlay
  c-step-quadrics      — gallery: ellipsoid, paraboloid, hyperboloid, cone (cross-sections)
  c-step-intersection  — sphere+plane: sphere→plane added→intersection circle
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle as MplCircle, Arc, FancyBboxPatch, FancyArrowPatch
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 9B: COMPOSITION PIPELINE — f(x)=2x+1, g(x)=x² → (f∘g)(x)=2x²+1
# ================================================================
fig, axes = plt.subplots(1, 4, figsize=(18, 5))

x_input = 3
g_out = x_input**2  # 9
f_out = 2*g_out + 1  # 19

# Panel 1: Input
ax = axes[0]
ax.set_xlim(-2, 5); ax.set_ylim(-2, 22)
ax.text(1.5, 10, f'x = {x_input}', fontsize=28, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
ax.set_title('Step 1: Start with x', fontsize=13, fontweight='bold')
ax.axis('off')

# Panel 2: Apply g(x)=x²
ax = axes[1]
ax.set_xlim(-2, 5); ax.set_ylim(-2, 22)
ax.text(1.5, 10, f'g({x_input}) = {g_out}', fontsize=28, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
ax.annotate('', xy=(0.8, 10), xytext=(2.2, 10),
           arrowprops=dict(arrowstyle='->', color='gray', lw=2))
ax.set_title('Step 2: Push into g → square it', fontsize=13, fontweight='bold')
ax.axis('off')

# Panel 3: Apply f to result
ax = axes[2]
ax.set_xlim(-2, 5); ax.set_ylim(-2, 22)
ax.text(1.5, 10, f'f({g_out}) = {f_out}', fontsize=28, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
ax.set_title('Step 3: Push result into f → 2×()+1', fontsize=13, fontweight='bold')
ax.axis('off')

# Panel 4: Final formula
ax = axes[3]
ax.set_xlim(-3, 3); ax.set_ylim(-1, 20)
x = np.linspace(-3, 3, 200)
ax.plot(x, 2*x**2+1, 'b-', linewidth=3)
ax.plot(3, 19, 'ro', markersize=12, zorder=5)
ax.text(0, 16, r'$(f\circ g)(x)=2x^2+1$', fontsize=16, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax.set_title('Result: (f∘g)(x)=2x²+1', fontsize=13, fontweight='bold')
ax.grid(alpha=0.15)
ax.set_xlabel('x'); ax.set_ylabel('y')

fig.suptitle('Graph 9B: Composition as a Pipeline — Push Through g, Then f',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9b-step-composition.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B composition done")


# ================================================================
# 9B: INVERSE AS REFLECTION — f(x)=2x+1
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

x = np.linspace(-4, 8, 300)
y_f = 2*x + 1
y_inv = (x - 1) / 2

# Panel 1: Original function
ax = axes[0]
ax.plot(x, y_f, 'b-', linewidth=3, label=r'$f(x)=2x+1$')
pts = [(0,1), (1,3), (2,5)]
for px, py in pts:
    ax.plot(px, py, 'bo', markersize=10, zorder=5)
ax.set_aspect('equal')
ax.set_xlim(-4, 8); ax.set_ylim(-4, 8)
ax.set_title('Step 1: Original points on f', fontsize=13, fontweight='bold')
ax.legend(fontsize=10); ax.grid(alpha=0.15)
ax.plot([-4,8], [-4,8], 'gray', lw=0.5, alpha=0.3)

# Panel 2: Swap (x,y) → (y,x)
ax = axes[1]
ax.plot(x, y_inv, 'r-', linewidth=3, label=r'$f^{-1}(x)=\frac{x-1}{2}$')
for px, py in pts:
    ax.plot(py, px, 'ro', markersize=10, zorder=5)
    ax.plot([px, py], [py, px], 'gray', lw=0.8, linestyle=':', alpha=0.5)
ax.set_aspect('equal')
ax.set_xlim(-4, 8); ax.set_ylim(-4, 8)
ax.set_title('Step 2: Swap coordinates', fontsize=13, fontweight='bold')
ax.legend(fontsize=10); ax.grid(alpha=0.15)
ax.plot([-4,8], [-4,8], 'gray', lw=0.5, alpha=0.3)

# Panel 3: Reflection across y=x
ax = axes[2]
ax.plot(x, y_f, 'b-', linewidth=3, label=r'$f$')
ax.plot(x, y_inv, 'r-', linewidth=3, label=r'$f^{-1}$')
ax.plot([-4,8], [-4,8], 'k--', linewidth=2, alpha=0.6, label=r'$y=x$')
for px, py in pts:
    ax.plot(px, py, 'bo', markersize=8)
    ax.plot(py, px, 'ro', markersize=8)
ax.set_aspect('equal')
ax.set_xlim(-4, 8); ax.set_ylim(-4, 8)
ax.set_title('Step 3: Mirror across y=x', fontsize=13, fontweight='bold')
ax.legend(fontsize=10); ax.grid(alpha=0.15)

fig.suptitle('Graph 9B: Inverse Function — Three Steps to Reflection',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9b-step-inverse.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B inverse done")


# ================================================================
# 9B: CONIC BUILD-UPS — Circle, Ellipse, Parabola, Hyperbola
# ================================================================
fig, axes = plt.subplots(2, 4, figsize=(18, 10))
# Row 1: Circle, Ellipse. Row 2: Parabola, Hyperbola
# Each has 2 sub-panels: geometry definition → final curve

theta = np.linspace(0, 2*np.pi, 300)

# ---- Circle ----
ax = axes[0, 0]
ax.plot(0, 0, 'ro', markersize=8, zorder=5, label='Center (0,0)')
ax.plot([0, 3], [0, 0], 'b-', linewidth=2)
ax.text(1.5, -0.5, 'R=3', fontsize=10, ha='center')
ax.set_aspect('equal'); ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
ax.set_title('Circle: center + radius', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1); ax.legend(fontsize=8)

ax = axes[0, 1]
ax.plot(3*np.cos(theta), 3*np.sin(theta), 'b-', linewidth=2.5)
ax.plot(0, 0, 'ro', markersize=5)
ax.set_aspect('equal'); ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
ax.set_title(r'$x^2+y^2=9$', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1)

# ---- Ellipse ----
ax = axes[0, 2]
c = np.sqrt(4**2 - 2**2)
ax.plot([-c, c], [0, 0], 'ro', markersize=6, label=f'Foci (±{c:.1f},0)')
ax.plot([-4, 4], [0, 0], 'gray', lw=0.5)
ax.plot([0, 0], [-2, 2], 'gray', lw=0.5)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-3, 3)
ax.set_title('Ellipse: foci + axes', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1); ax.legend(fontsize=8)

ax = axes[0, 3]
ax.plot(4*np.cos(theta), 2*np.sin(theta), 'darkgreen', linewidth=2.5)
ax.plot([-c, c], [0, 0], 'ro', markersize=5)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-3, 3)
ax.set_title(r'$\frac{x^2}{16}+\frac{y^2}{4}=1$', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1)

# ---- Parabola ----
ax = axes[1, 0]
ax.plot(0, 1, 'ro', markersize=8, label='Focus (0,1)')
ax.axhline(-1, color='gray', linestyle='--', linewidth=2, label='Directrix y=−1')
ax.plot(0, 0, 'go', markersize=8, label='Vertex (0,0)')
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-3, 4)
ax.set_title('Parabola: focus + directrix', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1); ax.legend(fontsize=8)

ax = axes[1, 1]
x_p = np.linspace(-5, 5, 300)
ax.plot(x_p, x_p**2/4, 'darkred', linewidth=2.5)
ax.plot(0, 1, 'ro', markersize=5)
ax.axhline(-1, color='gray', linestyle='--', linewidth=1)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-3, 4)
ax.set_title(r'$y=\frac{1}{4}x^2$', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1)

# ---- Hyperbola ----
ax = axes[1, 2]
a, b = 2, 1.5
c_hyp = np.sqrt(a**2 + b**2)
ax.plot([-a, a], [0, 0], 'go', markersize=8, label=f'Vertices (±{a},0)')
x_asym = np.linspace(-5, 5, 100)
ax.plot(x_asym, b/a*x_asym, 'orange', linestyle='--', linewidth=1.5, alpha=0.7)
ax.plot(x_asym, -b/a*x_asym, 'orange', linestyle='--', linewidth=1.5, alpha=0.7)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-4, 4)
ax.set_title('Hyperbola: vertices + asymptotes', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1); ax.legend(fontsize=8)

ax = axes[1, 3]
x_h = np.linspace(2.05, 5, 200)
y_h = b*np.sqrt(x_h**2/a**2 - 1)
ax.plot(x_h, y_h, 'purple', linewidth=2.5)
ax.plot(x_h, -y_h, 'purple', linewidth=2.5)
ax.plot(-x_h, y_h, 'purple', linewidth=2.5)
ax.plot(-x_h, -y_h, 'purple', linewidth=2.5)
ax.plot(x_asym, b/a*x_asym, 'orange', linestyle='--', linewidth=1, alpha=0.5)
ax.plot(x_asym, -b/a*x_asym, 'orange', linestyle='--', linewidth=1, alpha=0.5)
ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-4, 4)
ax.set_title(r'$\frac{x^2}{4}-\frac{y^2}{2.25}=1$', fontsize=11, fontweight='bold')
ax.grid(alpha=0.1)

fig.suptitle('Graph 9B: Conic Sections — Geometry Definition → Final Curve',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9b-step-conics.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B conics done")


# ================================================================
# 9B: CYCLOID GENERATION — Wheel at 4 positions
# ================================================================
fig, axes = plt.subplots(1, 4, figsize=(18, 5.5))
R = 1

for i, (t_val, ax) in enumerate(zip([0, np.pi/2, np.pi, 3*np.pi/2], axes)):
    # Draw the ground
    ax.axhline(0, color='brown', linewidth=2, alpha=0.5)
    
    # Center of wheel: (R*t, R)
    cx, cy = R * t_val, R
    
    # Draw wheel
    wheel = MplCircle((cx, cy), R, fill=False, edgecolor='gray', linewidth=2)
    ax.add_patch(wheel)
    
    # Draw spoke to the point
    px = R*(t_val - np.sin(t_val))
    py = R*(1 - np.cos(t_val))
    ax.plot([cx, px], [cy, py], 'r-', linewidth=2)
    ax.plot(px, py, 'ro', markersize=10, zorder=5)
    
    # Trace the cycloid so far
    t_trace = np.linspace(0, t_val, 100)
    x_trace = R*(t_trace - np.sin(t_trace))
    y_trace = R*(1 - np.cos(t_trace))
    ax.plot(x_trace, y_trace, 'b-', linewidth=2.5, alpha=0.8)
    
    ax.set_aspect('equal')
    ax.set_xlim(-0.3, 7)
    ax.set_ylim(-0.3, 3)
    phases = ['Start (t=0)', 'Quarter (t=π/2)', 'Half (t=π)', '3/4 (t=3π/2)']
    ax.set_title(phases[i], fontsize=12, fontweight='bold')
    ax.grid(alpha=0.1)
    ax.axis('off')

fig.suptitle('Graph 9B: Cycloid — Rolling Wheel Generates the Curve Step by Step',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9b-step-cycloid.png', dpi=180, bbox_inches='tight')
plt.close()
print("9B cycloid done")


# ================================================================
# 9C: SURFACE BUILD-UP — z = x² + y² (paraboloid)
# ================================================================
fig = plt.figure(figsize=(18, 6))

x = np.linspace(-2.5, 2.5, 40)
y = np.linspace(-2.5, 2.5, 40)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Panel 1: Wireframe only
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_wireframe(X, Y, Z, color='gray', linewidth=0.4, alpha=0.6)
ax1.scatter([0], [0], [0], c='red', s=60, zorder=5)
ax1.set_title('Step 1: Wireframe\n(see the skeleton)', fontsize=12, fontweight='bold')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.view_init(elev=25, azim=-55)

# Panel 2: Solid surface
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8, edgecolor='none')
ax2.scatter([0], [0], [0], c='black', s=60, zorder=5)
ax2.set_title('Step 2: Surface\n(fill the faces)', fontsize=12, fontweight='bold')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')
ax2.view_init(elev=25, azim=-55)

# Panel 3: Surface + level curves
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, Z, cmap='plasma', alpha=0.6, edgecolor='none')
# Level curves
for c in [1, 2, 3, 4]:
    t_c = np.linspace(0, 2*np.pi, 120)
    r_c = np.sqrt(c)
    ax3.plot(r_c*np.cos(t_c), r_c*np.sin(t_c), c, 'white', linewidth=1.5, alpha=0.9)
ax3.set_title('Step 3: Level Curves\n(horizontal slices)', fontsize=12, fontweight='bold')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.view_init(elev=25, azim=-55)

fig.suptitle('Graph 9C: Building a 3D Surface — $z=x^2+y^2$',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9c-step-surface.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C surface done")


# ================================================================
# 9C: QUADRIC SURFACE GALLERY with cross-sections
# ================================================================
fig = plt.figure(figsize=(18, 12))

titles = ['Ellipsoid', 'Elliptic Paraboloid\n(Bowl)', 'Hyperboloid\n(One Sheet)', 'Cone\n(Double)']
surfaces_data = []

# Ellipsoid: x²/4 + y²/9 + z²/1 = 1
phi, theta = np.linspace(0, np.pi, 30), np.linspace(0, 2*np.pi, 50)
phi_g, theta_g = np.meshgrid(phi, theta)
X_e = 2*np.sin(phi_g)*np.cos(theta_g)
Y_e = 3*np.sin(phi_g)*np.sin(theta_g)
Z_e = 1*np.cos(phi_g)
surfaces_data.append((X_e, Y_e, Z_e, 'Blues', []))

# Paraboloid: z = x² + y²
x_p = np.linspace(-2.5, 2.5, 40)
y_p = np.linspace(-2.5, 2.5, 40)
X_p, Y_p = np.meshgrid(x_p, y_p)
Z_p = X_p**2 + Y_p**2
surfaces_data.append((X_p, Y_p, Z_p, 'plasma', []))

# Hyperboloid of one sheet: x²+y²-z²/4=1
z_h = np.linspace(-3, 3, 40)
theta_h = np.linspace(0, 2*np.pi, 50)
Z_h, T_h = np.meshgrid(z_h, theta_h)
R_h = np.sqrt(1 + Z_h**2/4)
X_h = R_h*np.cos(T_h)
Y_h = R_h*np.sin(T_h)
surfaces_data.append((X_h, Y_h, Z_h, 'Oranges', []))

# Cone: x²+y²=z²
z_c = np.linspace(-3, 3, 40)
theta_c = np.linspace(0, 2*np.pi, 50)
Z_c, T_c = np.meshgrid(z_c, theta_c)
R_c = np.abs(Z_c)
X_c = R_c*np.cos(T_c)
Y_c = R_c*np.sin(T_c)
surfaces_data.append((X_c, Y_c, Z_c, 'Purples', []))

for i, ((X, Y, Z, cmap, _), title) in enumerate(zip(surfaces_data, titles)):
    ax = fig.add_subplot(2, 4, 2*i+1, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cmap, alpha=0.7, edgecolor='none')
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.view_init(elev=22, azim=-55)

# Cross-section panels (right column)
# Ellipsoid cross-section
ax = fig.add_subplot(2, 4, 2)
for z_val in [0, 0.5]:
    r = np.sqrt(1 - z_val**2)
    ax.add_patch(MplCircle((0,0), 1, fill=False, ec='blue', alpha=0.4))
ax.set_aspect('equal'); ax.set_xlim(-2.5,2.5); ax.set_ylim(-2.5,2.5)
ax.set_title('Cross-sections:\nellipses shrinking\nto a point', fontsize=10)
ax.grid(alpha=0.1)

ax = fig.add_subplot(2, 4, 4)
for z_val in [1, 2, 3]:
    r = np.sqrt(z_val)
    ax.add_patch(MplCircle((0,0), 1, fill=False, ec='red', alpha=0.4))
ax.set_aspect('equal'); ax.set_xlim(-2.5,2.5); ax.set_ylim(-2.5,2.5)
ax.set_title('Cross-sections:\ncirlces growing\nwith height', fontsize=10)
ax.grid(alpha=0.1)

ax = fig.add_subplot(2, 4, 6)
for z_val in [0, 1, 2]:
    r = np.sqrt(1 + z_val**2/4)
    ax.add_patch(MplCircle((0,0), 0.5, fill=False, ec='orange', alpha=0.4))
ax.set_aspect('equal'); ax.set_xlim(-3,3); ax.set_ylim(-3,3)
ax.set_title('Cross-sections:\ncircles, narrowest\nat z=0', fontsize=10)
ax.grid(alpha=0.1)

ax = fig.add_subplot(2, 4, 8)
for z_val in [1, 2, 3]:
    ax.add_patch(MplCircle((0,0), 0.5, fill=False, ec='purple', alpha=0.4))
ax.set_aspect('equal'); ax.set_xlim(-3,3); ax.set_ylim(-3,3)
ax.set_title('Cross-sections:\ncircles growing\nlinearly', fontsize=10)
ax.grid(alpha=0.1)

fig.suptitle('Graph 9C: Quadric Surface Gallery — 3D Shapes + Cross-Sections',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '9c-step-quadrics.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C quadrics done")


# ================================================================
# 9C: SPHERE-PLANE INTERSECTION — Step by step
# ================================================================
fig = plt.figure(figsize=(18, 6.5))

R = np.sqrt(20)
phi, theta = np.linspace(0, np.pi, 35), np.linspace(0, 2*np.pi, 55)
phi_g, theta_g = np.meshgrid(phi, theta)
X_s = R*np.sin(phi_g)*np.cos(theta_g)
Y_s = R*np.sin(phi_g)*np.sin(theta_g)
Z_s = R*np.cos(phi_g)

# Plane: x+y+z=6
xx, yy = np.meshgrid(np.linspace(-1, 5, 25), np.linspace(-1, 5, 25))
zz = 6 - xx - yy

# Intersection circle
center = np.array([2., 2., 2.])
r_circle = np.sqrt(8)
u = np.array([1., -1., 0.]) / np.sqrt(2)
v = np.cross(np.array([1., 1., 1.]), u)
v = v / np.linalg.norm(v)
t_c = np.linspace(0, 2*np.pi, 150)
circle_pts = center[:,None] + r_circle*(u[:,None]*np.cos(t_c) + v[:,None]*np.sin(t_c))

# Panel 1: Sphere only
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X_s, Y_s, Z_s, cmap='Blues', alpha=0.4, edgecolor='none')
ax1.set_title('Step 1: Sphere\n$x^2+y^2+z^2=20$', fontsize=12, fontweight='bold')
ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('z')
ax1.view_init(elev=22, azim=-60)

# Panel 2: Add plane
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X_s, Y_s, Z_s, cmap='Blues', alpha=0.25, edgecolor='none')
ax2.plot_surface(xx, yy, zz, alpha=0.4, color='orange', edgecolor='none')
ax2.set_title('Step 2: Add Plane\n$x+y+z=6$', fontsize=12, fontweight='bold')
ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')
ax2.view_init(elev=22, azim=-60)

# Panel 3: Intersection circle
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X_s, Y_s, Z_s, cmap='Blues', alpha=0.2, edgecolor='none')
ax3.plot_surface(xx, yy, zz, alpha=0.3, color='orange', edgecolor='none')
ax3.plot(circle_pts[0], circle_pts[1], circle_pts[2], 'r-', linewidth=3.5)
ax3.scatter([2], [2], [2], c='red', s=50, zorder=5)
ax3.set_title('Step 3: Intersection Circle\nCenter (2,2,2), r=$2\\sqrt{2}$', fontsize=12, fontweight='bold')
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.view_init(elev=22, azim=-60)

fig.suptitle('Graph 9C: Sphere–Plane Intersection — Three Steps to the Circle',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9c-step-intersection.png', dpi=180, bbox_inches='tight')
plt.close()
print("9C intersection done")

print("\n=== ALL 9B+9C STEP-BY-STEP GRAPHS DONE ===")
