"""
Generate 2D, 3D, and 4D+ visualization graphs for Session 12A —
Matrices, Complex Numbers, Vectors.

12f — 2D: Matrix transformation of the unit square (parallelogram)
12g — 2D: Complex multiplication as rotation + scaling
12h — 3D: Cross product — perpendicular vector + parallelogram area
12i — 3D: Determinant as volume — parallelepiped from 3 vectors
12j — 4D+: Projection concept — higher dimensions collapsing to 2D
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 12f — 2D: Matrix Transformation of the Unit Square
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

# Unit square vertices
square = np.array([[0,0], [1,0], [1,1], [0,1], [0,0]])

# Original unit square (dashed)
ax.plot(square[:,0], square[:,1], 'k--', linewidth=2, alpha=0.5, label='Unit square (original)')
ax.fill(square[:,0], square[:,1], alpha=0.08, color='gray')

# Transformation matrix A = [[2, 1], [0.5, 1.5]]
A = np.array([[2.0, 1.0], [0.5, 1.5]])
transformed = (A @ square.T).T

ax.plot(transformed[:,0], transformed[:,1], 'b-', linewidth=3, label='A × (unit square)')
ax.fill(transformed[:,0], transformed[:,1], alpha=0.25, color='steelblue')

# Annotate basis vectors
ax.arrow(0, 0, 2.0, 0.5, head_width=0.08, head_length=0.12, fc='red', ec='red',
         linewidth=2.5, label=r'$A\vec{e}_1$ = column 1')
ax.arrow(0, 0, 1.0, 1.5, head_width=0.08, head_length=0.12, fc='darkgreen', ec='darkgreen',
         linewidth=2.5, label=r'$A\vec{e}_2$ = column 2')

# Determinant annotation
det = np.linalg.det(A)
ax.text(1.5, 2.8,
        f'Area of parallelogram = |det(A)| = |{det:.1f}| = {abs(det):.1f}\n'
        f'Original square area = 1 → scaled by {abs(det):.1f}×',
        fontsize=14, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax.set_aspect('equal')
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 3.5)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 12f: How a 2x2 Matrix Transforms the Unit Square into a Parallelogram',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11, loc='upper left')
ax.grid(alpha=0.2)
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
ax.tick_params(labelsize=12)
plt.tight_layout()
plt.savefig(OUT + '12f-matrix-transformation.png', dpi=180, bbox_inches='tight')
plt.close()
print("12f done — Matrix Transformation (2D)")


# ================================================================
# 12g — 2D: Complex Multiplication as Rotation + Scaling
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

# Draw unit circle (faint)
theta = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=0.8, alpha=0.25)

# z1 = 2 + i  (modulus ~2.236, angle ~26.6°)
z1 = np.array([2.0, 1.0])
# z2 = 1 + 1.5i  (modulus ~1.803, angle ~56.3°)
z2 = np.array([1.0, 1.5])
# z1 * z2 = (2+i)(1+1.5i) = 2+3i+i+1.5i² = 2+4i−1.5 = 0.5+4i
z_prod = np.array([0.5, 4.0])

# Draw vectors
ax.arrow(0, 0, z1[0], z1[1], head_width=0.1, head_length=0.15, fc='blue', ec='blue',
         linewidth=3, label=r'$z_1 = 2 + i$', length_includes_head=True, zorder=3)
ax.arrow(0, 0, z2[0], z2[1], head_width=0.1, head_length=0.15, fc='green', ec='green',
         linewidth=3, label=r'$z_2 = 1 + 1.5i$', length_includes_head=True, zorder=3)
ax.arrow(0, 0, z_prod[0], z_prod[1], head_width=0.1, head_length=0.15, fc='red', ec='red',
         linewidth=4, label=r'$z_1 z_2 = 0.5 + 4i$', length_includes_head=True, zorder=4)

# Annotate moduli and angles
def annotate_vector(ax, vec, color, label_offset):
    r = np.sqrt(vec[0]**2 + vec[1]**2)
    theta = np.arctan2(vec[1], vec[0])
    mid = vec * 0.55
    ax.text(mid[0] + label_offset[0], mid[1] + label_offset[1],
            f'|z| = {r:.2f}\nθ = {np.degrees(theta):.0f}°',
            fontsize=10, color=color, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

annotate_vector(ax, z1, 'blue', (0.1, -0.3))
annotate_vector(ax, z2, 'green', (-0.8, 0.1))
annotate_vector(ax, z_prod, 'red', (0.1, 0.1))

# Product rule text
ax.text(0.05, 0.95,
        r'$z_1 \cdot z_2 = (r_1 r_2) e^{i(\theta_1 + \theta_2)}$' + '\n'
        r'Multiply moduli: $|z_1z_2| = |z_1| \cdot |z_2|$' + '\n'
        r'Add angles: $\arg(z_1z_2) = \arg(z_1) + \arg(z_2)$',
        transform=ax.transAxes, fontsize=13, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

ax.set_aspect('equal')
ax.set_xlim(-1.5, 4)
ax.set_ylim(-1, 5)
ax.set_xlabel('Real', fontsize=14)
ax.set_ylabel('Imaginary', fontsize=14)
ax.set_title('Graph 12g: Complex Multiplication = Stretch + Rotate', fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper left')
ax.grid(alpha=0.2)
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
ax.tick_params(labelsize=12)
plt.tight_layout()
plt.savefig(OUT + '12g-complex-multiplication.png', dpi=180, bbox_inches='tight')
plt.close()
print("12g done — Complex Multiplication (2D)")


# ================================================================
# 12h — 3D: Cross Product — Perpendicular Vector + Parallelogram
# ================================================================
fig = plt.figure(figsize=(12, 11))
ax = fig.add_subplot(111, projection='3d')

# Vectors a and b — use clean, well-separated vectors
a = np.array([2.5, 0.3, 0.3])
b = np.array([0.3, 2.5, 0.3])
cross = np.cross(a, b)  # a×b ≈ (-0.66, -0.66, 6.16) — points mostly up

origin = np.array([0, 0, 0])

# Draw vectors with thicker arrows
ax.quiver(*origin, *a, color='blue', linewidth=4, arrow_length_ratio=0.10,
          label=r'$\vec{a} = (2.5,\;0.3,\;0.3)$')
ax.quiver(*origin, *b, color='green', linewidth=4, arrow_length_ratio=0.10,
          label=r'$\vec{b} = (0.3,\;2.5,\;0.3)$')
ax.quiver(*origin, *cross, color='red', linewidth=5, arrow_length_ratio=0.08,
          label=r'$\vec{a} \times \vec{b}$')

# Parallelogram edges — dashed gray
p_verts = np.array([origin, a, a+b, b])
for i in range(4):
    ax.plot([p_verts[i][0], p_verts[(i+1)%4][0]],
            [p_verts[i][1], p_verts[(i+1)%4][1]],
            [p_verts[i][2], p_verts[(i+1)%4][2]],
            'gray', linewidth=2, alpha=0.6, linestyle='--')
poly = Poly3DCollection([p_verts], alpha=0.12, color='cyan')
ax.add_collection3d(poly)

# Annotate cross product result
cn = np.linalg.norm(cross)
ax.text2D(0.05, 0.95,
          f'$|\\vec{{a}}\\times\\vec{{b}}| = {cn:.2f}$  (parallelogram area)\n'
          f'$\\vec{{a}}\\cdot(\\vec{{a}}\\times\\vec{{b}}) = {np.dot(a,cross):.1f}$  (perpendicular check)\n'
          f'$\\vec{{b}}\\cdot(\\vec{{a}}\\times\\vec{{b}}) = {np.dot(b,cross):.1f}$  (perpendicular check)',
          transform=ax.transAxes, fontsize=13, verticalalignment='top',
          bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

# Better viewing angle
ax.view_init(elev=20, azim=-50)
ax.set_xlabel('X', fontsize=14, labelpad=10)
ax.set_ylabel('Y', fontsize=14, labelpad=10)
ax.set_zlabel('Z', fontsize=14, labelpad=10)
ax.set_title('Graph 12h: Cross Product — A Vector Perpendicular to Both a and b', fontsize=15, fontweight='bold')
ax.legend(fontsize=12, loc='upper left')
ax.set_xlim([0, 3.5])
ax.set_ylim([0, 3.5])
ax.set_zlim([-1, 7])
ax.tick_params(labelsize=11)
plt.tight_layout()
plt.savefig(OUT + '12h-3d-cross-product.png', dpi=180, bbox_inches='tight')
plt.close()
print("12h done — Cross Product (3D, fixed)")


# ================================================================
# 12i — 3D: Determinant as Volume — Parallelepiped
# ================================================================
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Three vectors forming a parallelepiped
v1 = np.array([2, 0, 0.3])
v2 = np.array([0.5, 2, 0.2])
v3 = np.array([0.4, 0.5, 2.5])

# Draw vectors
ax.quiver(*origin, *v1, color='blue', linewidth=3, arrow_length_ratio=0.1, label=r'$\vec{v}_1$')
ax.quiver(*origin, *v2, color='green', linewidth=3, arrow_length_ratio=0.1, label=r'$\vec{v}_2$')
ax.quiver(*origin, *v3, color='purple', linewidth=3, arrow_length_ratio=0.1, label=r'$\vec{v}_3$')

# Build the parallelepiped — 8 vertices
O = np.array([0, 0, 0])
verts = np.array([
    O, v1, v1+v2, v2,                    # bottom face
    v3, v1+v3, v1+v2+v3, v2+v3           # top face
])

# Define the 6 faces
faces = [
    [0, 1, 2, 3],  # bottom
    [4, 5, 6, 7],  # top
    [0, 1, 5, 4],  # front
    [2, 3, 7, 6],  # back
    [1, 2, 6, 5],  # right
    [0, 3, 7, 4],  # left
]

# Draw edges
for face in faces:
    for i in range(4):
        j = (i + 1) % 4
        ax.plot([verts[face[i]][0], verts[face[j]][0]],
                [verts[face[i]][1], verts[face[j]][1]],
                [verts[face[i]][2], verts[face[j]][2]],
                'gray', linewidth=1.2, alpha=0.6)

# Fill faces with translucent colors
colors = ['lightblue', 'lightblue', 'lightcoral', 'lightcoral', 'lightgreen', 'lightgreen']
for face, col in zip(faces, colors):
    poly = Poly3DCollection([verts[face]], alpha=0.15, color=col, edgecolor='none')
    ax.add_collection3d(poly)

# Volume = |det([v1, v2, v3])|
M = np.column_stack([v1, v2, v3])
vol = abs(np.linalg.det(M))
ax.text2D(0.05, 0.95,
          f'Volume = |det($A$)| = |det([v₁ v₂ v₃])|\n'
          f'       = {vol:.2f} (cubic units)\n'
          f'Original unit cube volume = 1\n'
          f'→ scaled by {vol:.2f}×',
          transform=ax.transAxes, fontsize=13, verticalalignment='top',
          bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

ax.set_xlabel('X', fontsize=13)
ax.set_ylabel('Y', fontsize=13)
ax.set_zlabel('Z', fontsize=13)
ax.set_title('Graph 12i: Determinant = Volume of the Parallelepiped (3D)', fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper right')
ax.set_xlim([0, 3.5])
ax.set_ylim([0, 3.5])
ax.set_zlim([0, 3.5])
ax.tick_params(labelsize=10)
plt.tight_layout()
plt.savefig(OUT + '12i-determinant-volume-3d.png', dpi=180, bbox_inches='tight')
plt.close()
print("12i done — Determinant as Volume (3D)")


# ================================================================
# 12j1 — 2D→1D Projection (FULL SIZE standalone)
# ================================================================
fig, ax = plt.subplots(figsize=(10, 8))

np.random.seed(1)
points_2d = np.array([[1, 2], [3, 1], [2, 3.5], [4.5, 2.5], [2.5, 0.5], [4, 1.5]])
ax.scatter(points_2d[:,0], points_2d[:,1], s=120, c='steelblue', zorder=3,
           edgecolors='black', linewidth=0.5, label='Original data (2D)')
for i, (x, y) in enumerate(points_2d):
    ax.text(x + 0.12, y + 0.12, str(i+1), fontsize=13, fontweight='bold')

# Project onto x-axis
for x, y in points_2d:
    ax.plot([x, x], [y, 0], 'r-', linewidth=1.5, alpha=0.5)
    ax.scatter([x], [0], s=70, c='red', zorder=3, edgecolors='darkred', linewidth=0.5)
ax.axhline(0, color='red', linewidth=3, alpha=0.6, label='Projection onto 1D (x-axis)')

# Annotate what's lost
ax.annotate('Information lost:\n y-coordinate discarded',
            xy=(4.5, 2.5), xytext=(3, 3.8),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5), fontsize=13,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax.set_xlim(-0.3, 5.5)
ax.set_ylim(-0.8, 4.5)
ax.set_aspect('equal')
ax.set_title('2D → 1D Projection — Dropping One Dimension', fontsize=16, fontweight='bold')
ax.legend(fontsize=13, loc='lower right')
ax.grid(alpha=0.2)
ax.set_xlabel('x₁ (kept)', fontsize=15)
ax.set_ylabel('x₂ (lost)', fontsize=15)
ax.tick_params(labelsize=12)
plt.tight_layout()
plt.savefig(OUT + '12j1-2d-to-1d-projection.png', dpi=180, bbox_inches='tight')
plt.close()
print("12j1 done")

# ================================================================
# 12j2 — 3D→2D Projection (FULL SIZE standalone)
# ================================================================
fig, ax = plt.subplots(figsize=(10, 8))

np.random.seed(42)
n_pts = 20
# Generate 3D points with some cluster structure
pts_3d = np.random.multivariate_normal([0, 0, 1], [[2.5, 1, 0.5], [1, 2.5, 0.5], [0.5, 0.5, 2]], n_pts)

# Project by dropping z — show original 3D positions as "shadows"
# The 2D projection = (x, y) from original 3D (x, y, z)
ax.scatter(pts_3d[:,0], pts_3d[:,1], s=100, c='steelblue', zorder=3, alpha=0.85,
           edgecolors='black', linewidth=0.5, label='3D data → 2D (z-coordinate dropped)')

# Show the "shadow" effect for a few representative points
highlight = [0, 3, 5, 10, 15]
for i in highlight:
    x, y, z = pts_3d[i]
    # The original 3D point would be offset — show the displacement
    offset_x = z * 0.6
    offset_y = z * 0.6
    ax.annotate('', xy=(x, y), xytext=(x + offset_x, y + offset_y),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.6, lw=2))
    ax.scatter([x + offset_x], [y + offset_y], s=50, c='red', alpha=0.6, zorder=2,
               edgecolors='darkred', linewidth=0.3)

# Legend for "original" vs "projected"
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, alpha=0.6, label='Original 3D position (offset)'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='steelblue', markersize=10, alpha=0.85, label='2D projection (z dropped)')]
ax.legend(handles=custom_lines, fontsize=13, loc='upper left')

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_title('3D → 2D Projection — The z-dimension is Flattened', fontsize=16, fontweight='bold')
ax.grid(alpha=0.2)
ax.set_xlabel('x₁ (width — kept)', fontsize=15)
ax.set_ylabel('x₂ (height — kept)', fontsize=15)
ax.tick_params(labelsize=12)
ax.text(0.05, 0.94, 'Red arrows show the displacement\ncaused by dropping the z-coordinate.',
        transform=ax.transAxes, fontsize=13,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
        verticalalignment='top')
plt.tight_layout()
plt.savefig(OUT + '12j2-3d-to-2d-projection.png', dpi=180, bbox_inches='tight')
plt.close()
print("12j2 done")

# ================================================================
# 12j3 — Dimensionality Reduction Cascade (FULL SIZE standalone)
# ================================================================
fig, ax = plt.subplots(figsize=(11, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Nested boxes showing dimensional reduction
boxes = [
    (0.3, 0.3, 9.4, 9.4, r'$\mathbb{R}^n$ — Original high-dimensional data', '#1a5276', 0.08),
    (1.3, 1.3, 7.4, 7.4, r'$\mathbb{R}^m$ — After linear transformation (matrix $A$)', '#c0392b', 0.10),
    (2.3, 2.3, 5.4, 5.4, r'$\mathbb{R}^k$ — After projection / feature selection', '#1e8449', 0.12),
    (3.3, 3.3, 3.4, 3.4, r'$\mathbb{R}^2$ — Final 2D visualization', '#7d3c98', 0.15),
]
for x, y, w, h, label, color, alpha in boxes:
    rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15',
                                     facecolor=color, alpha=alpha, edgecolor=color, linewidth=3)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=14,
            fontweight='bold', color=color)

# Arrows
for i in range(len(boxes)-1):
    x1 = boxes[i][0] + boxes[i][2]/2
    y1 = boxes[i][1]
    x2 = boxes[i+1][0] + boxes[i+1][2]/2
    y2 = boxes[i+1][1] + boxes[i+1][3]
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=3,
                                connectionstyle='arc3,rad=0'))

# Side annotation
ax.text(0.5, 9.6, 'Dimensionality Reduction Pipeline', fontsize=18, fontweight='bold', color='#333333')

# Bottom explanation
ax.text(5, -0.2,
        'A 4D→2D projection matrix is just a 2×4 matrix.\n'
        'It loses information — but the essential structure\n'
        '(clusters, directions, relative distances) often survives.',
        ha='center', fontsize=14, color='#333333',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

ax.text(5, 0.05, '', fontsize=1)  # spacing hack
plt.tight_layout()
plt.savefig(OUT + '12j3-dimensionality-cascade.png', dpi=180, bbox_inches='tight')
plt.close()
print("12j3 done")


print("\n=== All dimension visualization graphs generated! ===")
