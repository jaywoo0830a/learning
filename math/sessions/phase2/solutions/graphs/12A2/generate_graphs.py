#!/usr/bin/env python3
"""Generate visual graphs for 12A2 Matrices and Vectors Solutions."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Polygon, Arc, Circle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams.update({
    'figure.dpi': 150, 'savefig.dpi': 150,
    'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 11,
    'savefig.facecolor': 'white', 'savefig.edgecolor': 'none',
    'figure.facecolor': 'white',
})

def save_fig(fig, name):
    fig.savefig(f'{OUTPUT_DIR}/{name}', bbox_inches='tight', facecolor='white',
                edgecolor='none', pad_inches=0.15)
    plt.close(fig)

# ═══════════════════════════════════════════════════════════
# 01 — Practice 1: Determinant Zero = Collapse onto Line
# ═══════════════════════════════════════════════════════════
def fig_p1_det_zero_collapse():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    A = np.array([[2, 4], [1, 2]])

    # Left: unit square
    ax1.fill(sq[:,0], sq[:,1], color='#4ECDC4', alpha=0.4, edgecolor='#2C8C84', linewidth=2)
    ax1.plot(sq[:,0], sq[:,1], 'o-', color='#2C8C84', markersize=5)
    ax1.arrow(0, 0, 1, 0, head_width=0.05, head_length=0.05, fc='#E74C3C', ec='#E74C3C', linewidth=2)
    ax1.arrow(0, 0, 0, 1, head_width=0.05, head_length=0.05, fc='#3498DB', ec='#3498DB', linewidth=2)
    ax1.text(0.5, -0.12, 'e₁', fontsize=10, color='#E74C3C', ha='center')
    ax1.text(-0.15, 0.5, 'e₂', fontsize=10, color='#3498DB', va='center')
    ax1.set_title('Unit Square (Area=1)', fontweight='bold', fontsize=12)
    ax1.set_xlim(-0.5, 2); ax1.set_ylim(-0.5, 2)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='black', lw=0.5); ax1.axvline(0, color='black', lw=0.5)

    # Right: collapsed onto line
    corners = np.array([A @ v for v in sq])
    ax2.fill(corners[:,0], corners[:,1], color='#E74C3C', alpha=0.4, edgecolor='#C0392B', linewidth=2)
    # Show it's a line segment
    ax2.plot([0, 6], [0, 3], '--', color='#E74C3C', alpha=0.3, linewidth=1)
    ax2.arrow(0, 0, A[0,0], A[1,0], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=2.5)
    ax2.arrow(0, 0, A[0,1], A[1,1], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=2.5)
    ax2.text(A[0,0]/2-0.2, A[1,0]/2-0.2, 'c₁=(2,1)', fontsize=9, color='#E74C3C')
    ax2.text(A[0,1]/2-0.2, A[1,1]/2-0.2, 'c₂=(4,2)=2c₁', fontsize=9, color='#3498DB')

    ax2.annotate('det(A)=0\nColumns parallel\n→ collapses to line y=x/2',
                xy=(3.5, 0.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))
    ax2.set_title('After A: Collapse onto Line (Area=0)', fontweight='bold', fontsize=12)
    ax2.set_xlim(-0.5, 7); ax2.set_ylim(-0.5, 4)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)

    fig.suptitle('Practice 1: det(A)=0 — Plane Collapses onto a Line', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'p1-det-zero-collapse.png')

# ═══════════════════════════════════════════════════════════
# 02 — Practice 2: Solve Linear System by Matrix Inversion
# ═══════════════════════════════════════════════════════════
def fig_p2_linear_system():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    x = np.linspace(-1, 5, 100)
    y1 = (3*x - 7) / 2    # 3x - 2y = 7 → y = (3x-7)/2
    y2 = (5 - x) / 4      # x + 4y = 5 → y = (5-x)/4

    ax.plot(x, y1, '#E74C3C', linewidth=2.5, label='3x−2y=7')
    ax.plot(x, y2, '#3498DB', linewidth=2.5, label='x+4y=5')

    # Intersection point
    sol_x, sol_y = 19/7, 4/7
    ax.plot(sol_x, sol_y, 'o', color='#27AE60', markersize=14, zorder=5)
    ax.annotate(f'Solution\n({sol_x:.2f}, {sol_y:.2f})', (sol_x, sol_y),
               textcoords="offset points", xytext=(15, 15), fontsize=11, color='#27AE60', fontweight='bold')

    # Column vectors
    A_col1 = np.array([3, 1])
    A_col2 = np.array([-2, 4])
    ax.arrow(0, 0, A_col1[0], A_col1[1], head_width=0.12, head_length=0.12, fc='#E74C3C', ec='#E74C3C', linewidth=2, alpha=0.4, linestyle='--')
    ax.arrow(0, 0, A_col2[0], A_col2[1], head_width=0.12, head_length=0.12, fc='#3498DB', ec='#3498DB', linewidth=2, alpha=0.4, linestyle='--')

    ax.annotate('A⁻¹ = (1/14)[[4,2],[-1,3]]\nx⃗ = A⁻¹b⃗',
               xy=(2.5, 3), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax.legend(fontsize=11, loc='upper right')
    ax.set_xlim(-0.5, 5); ax.set_ylim(-1.5, 4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    ax.set_title('Practice 2: Linear System — Intersection Point', fontweight='bold', fontsize=14)
    save_fig(fig, 'p2-linear-system.png')

# ═══════════════════════════════════════════════════════════
# 03 — Practice 3: Cross Product in 3D
# ═══════════════════════════════════════════════════════════
def fig_p3_cross_product_3d():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    a = np.array([2, -1, 3])
    b = np.array([1, 4, -2])
    c = np.cross(a, b)  # (-10, 7, 9)

    ax.quiver(0, 0, 0, a[0], a[1], a[2], color='#E74C3C', linewidth=3, arrow_length_ratio=0.12, label=r'$\vec{a}=(2,-1,3)$')
    ax.quiver(0, 0, 0, b[0], b[1], b[2], color='#3498DB', linewidth=3, arrow_length_ratio=0.12, label=r'$\vec{b}=(1,4,-2)$')
    ax.quiver(0, 0, 0, c[0], c[1], c[2], color='#27AE60', linewidth=3.5, arrow_length_ratio=0.15, label=r'$\vec{a}\times\vec{b}=(-10,7,9)$')

    # Parallelogram
    verts = [[0,0,0], a.tolist(), (a+b).tolist(), b.tolist()]
    poly = Poly3DCollection([verts], alpha=0.2, facecolor='#BDC3C7', edgecolor='gray')
    ax.add_collection3d(poly)

    ax.annotate('a⃗·b⃗ = −8\n|c⃗| = √206 ≈ 14.35\nc⃗ ⊥ a⃗, c⃗ ⊥ b⃗ ✓',
                xy=(0.5, 0.9), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8),
                xycoords='axes fraction')

    ax.set_xlim([-12, 4]); ax.set_ylim([-3, 8]); ax.set_zlim([-3, 10])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.legend(fontsize=9, loc='upper left')
    ax.set_title('Practice 3: Cross Product — Perpendicular to Both Vectors', fontweight='bold', fontsize=13, pad=20)
    ax.view_init(elev=20, azim=-50)
    save_fig(fig, 'p3-cross-product-3d.png')

# ═══════════════════════════════════════════════════════════
# 04 — Practice 4: Triangle Area in 3D (½|cross|)
# ═══════════════════════════════════════════════════════════
def fig_p4_triangle_area_3d():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([0, 0, 0])
    B = np.array([3, 1, 0])
    C = np.array([1, 4, 0])
    AB = B - A
    AC = C - A
    cross = np.cross(AB, AC)  # (0, 0, 11)

    # Triangle
    verts_tri = [[0,0,0], B.tolist(), C.tolist()]
    poly = Poly3DCollection([verts_tri], alpha=0.35, facecolor='#3498DB', edgecolor='#2471A3', linewidth=2)
    ax.add_collection3d(poly)

    ax.quiver(0, 0, 0, AB[0], AB[1], AB[2], color='#E74C3C', linewidth=2.5, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, AC[0], AC[1], AC[2], color='#3498DB', linewidth=2.5, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, cross[0], cross[1], cross[2], color='#27AE60', linewidth=3, arrow_length_ratio=0.08, label='AB×AC=(0,0,11)')

    ax.annotate('Area = ½|AB×AC| = ½·11 = 5.5',
                xy=(0.5, 0.9), fontsize=11, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8),
                xycoords='axes fraction')

    ax.set_xlim([-1, 4]); ax.set_ylim([-1, 5]); ax.set_zlim([-1, 12])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title('Practice 4: Triangle Area = ½|AB×AC| = 11/2', fontweight='bold', fontsize=13, pad=20)
    ax.view_init(elev=25, azim=-60)
    save_fig(fig, 'p4-triangle-area-3d.png')

# ═══════════════════════════════════════════════════════════
# 05 — Practice 5: Composition — Reflect×Rotate Both Orders
# ═══════════════════════════════════════════════════════════
def fig_p5_composition():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

    Rx = np.array([[1, 0], [0, -1]])
    R90 = np.array([[0, -1], [1, 0]])
    R90_Rx = R90 @ Rx   # [[0,1],[1,0]]  reflect y=x
    Rx_R90 = Rx @ R90   # [[0,-1],[-1,0]] reflect y=-x

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

    results = [
        (R90_Rx, 'R₉₀∘Rx = Reflect y=x\nReflect then Rotate', '#E74C3C', 'y=x'),
        (Rx_R90, 'Rx∘R₉₀ = Reflect y=−x\nRotate then Reflect', '#3498DB', 'y=−x'),
    ]

    # Left: original
    ax = axes[0]
    ax.fill(sq[:,0], sq[:,1], color='#4ECDC4', alpha=0.4, edgecolor='#2C8C84', linewidth=2)
    ax.arrow(0, 0, 1, 0, head_width=0.06, head_length=0.06, fc='#E74C3C', ec='#E74C3C', linewidth=2)
    ax.arrow(0, 0, 0, 1, head_width=0.06, head_length=0.06, fc='#3498DB', ec='#3498DB', linewidth=2)
    ax.set_title('Original Unit Square', fontweight='bold', fontsize=11)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)

    for ax, (M, title, color, mirror_line) in zip(axes[1:], results):
        corners = np.array([M @ v for v in sq])
        ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
        ax.fill(corners[:,0], corners[:,1], color=color, alpha=0.4, edgecolor=color, linewidth=2)
        ax.plot(corners[:,0], corners[:,1], 'o-', color=color, markersize=4)

        # Mirror line
        if mirror_line == 'y=x':
            ax.plot([-2, 2], [-2, 2], ':', color='#27AE60', linewidth=1.5, alpha=0.7)
        else:
            ax.plot([-2, 2], [2, -2], ':', color='#27AE60', linewidth=1.5, alpha=0.7)

        ax.arrow(0, 0, M[0,0], M[1,0], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=2)
        ax.arrow(0, 0, M[0,1], M[1,1], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=2)
        ax.set_title(title, fontweight='bold', fontsize=10)
        ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
        ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
        ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)

    fig.suptitle('Practice 5: Composition Order Matters — R₉₀Rx ≠ RxR₉₀', fontweight='bold', fontsize=13)
    plt.tight_layout()
    save_fig(fig, 'p5-composition.png')

# ═══════════════════════════════════════════════════════════
# 06 — Practice 6: Vector Projection
# ═══════════════════════════════════════════════════════════
def fig_p6_projection():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    a = np.array([5, 12])
    b = np.array([3, 4])
    proj = (np.dot(a, b) / np.dot(b, b)) * b  # (189/25, 252/25) = (7.56, 10.08)
    perp = a - proj

    ax.arrow(0, 0, a[0], a[1], head_width=0.4, head_length=0.4, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    ax.arrow(0, 0, b[0], b[1], head_width=0.3, head_length=0.3, fc='#3498DB', ec='#3498DB', linewidth=2.5, zorder=4)
    ax.arrow(0, 0, proj[0], proj[1], head_width=0.3, head_length=0.3, fc='#27AE60', ec='#27AE60', linewidth=3, zorder=4)

    # Dashed perpendicular
    ax.plot([proj[0], a[0]], [proj[1], a[1]], '--', color='#E67E22', linewidth=2)
    ax.arrow(proj[0], proj[1], perp[0], perp[1], head_width=0.2, head_length=0.2, fc='#E67E22', ec='#E67E22', linewidth=2)

    # Right angle
    d = b / np.linalg.norm(b) * 0.6
    ax.plot([proj[0]-d[1], proj[0]-d[1]+d[0]], [proj[1]+d[0], proj[1]+d[0]+d[1]], 'k-', linewidth=1.5)

    ax.text(a[0]/2-0.5, a[1]/2-0.5, r'$\vec{a}$=(5,12)', fontsize=12, color='#E74C3C', fontweight='bold')
    ax.text(b[0]/2-0.5, b[1]/2-0.5, r'$\vec{b}$=(3,4)', fontsize=12, color='#3498DB', fontweight='bold')
    ax.text(proj[0]/2-1, proj[1]/2-1, 'proj=(7.56,10.08)', fontsize=10, color='#27AE60', fontweight='bold')

    ax.annotate(f'scalar proj = a⃗·b⃗/|b⃗| = 63/5 = 12.6\nvector proj = (a⃗·b⃗/|b⃗|²)·b⃗ = (63/25)(3,4)\n|proj| = 12.6 ✓',
               xy=(6, 8), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax.set_xlim(-0.5, 9); ax.set_ylim(-0.5, 13)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_title('Practice 6: Vector Projection of (5,12) onto (3,4)', fontweight='bold', fontsize=14)
    save_fig(fig, 'p6-projection.png')

# ═══════════════════════════════════════════════════════════
# 07 — Practice 7: Inverse Matrix Geometry
# ═══════════════════════════════════════════════════════════
def fig_p7_inverse_matrix():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5))

    A = np.array([[2, 1], [5, 3]])
    Ainv = np.array([[3, -1], [-5, 2]])

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    steps = [
        (np.eye(2), 'Start\nUnit Square', '#3498DB'),
        (A, 'Apply A\nStretch+Shear', '#E74C3C'),
        (Ainv, 'Apply A⁻¹\nReverse', '#27AE60'),
        (Ainv @ A, 'A⁻¹A = I\nBack to Square', '#8E44AD'),
    ]

    for ax, (M, title, color) in zip(axes, steps):
        corners = np.array([M @ v for v in sq])
        ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.12, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
        ax.fill(corners[:,0], corners[:,1], color=color, alpha=0.4, edgecolor=color, linewidth=2)
        ax.plot(corners[:,0], corners[:,1], 'o-', color=color, markersize=4)
        ax.arrow(0, 0, M[0,0], M[1,0], head_width=0.1, head_length=0.1, fc='#E74C3C', ec='#E74C3C', linewidth=2)
        ax.arrow(0, 0, M[0,1], M[1,1], head_width=0.1, head_length=0.1, fc='#3498DB', ec='#3498DB', linewidth=2)
        ax.set_title(title, fontsize=9.5, fontweight='bold')
        ax.set_aspect('equal'); ax.grid(True, alpha=0.25)
        ax.axhline(0, color='black', lw=0.3); ax.axvline(0, color='black', lw=0.3)
        ax.set_xlim(-2, 5); ax.set_ylim(-2, 5)

    fig.suptitle('Practice 7: A⁻¹ Undoes A — A⁻¹(A(□)) = □', fontweight='bold', fontsize=13)
    plt.tight_layout()
    save_fig(fig, 'p7-inverse-matrix.png')

# ═══════════════════════════════════════════════════════════
# 08 — Practice 8: Parallelepiped Volume from Diagonal Matrix
# ═══════════════════════════════════════════════════════════
def fig_p8_parallelepiped_3d():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    v1 = np.array([2, 0, 0])
    v2 = np.array([0, 3, 0])
    v3 = np.array([0, 0, 5])

    # Parallelepiped vertices
    origin = np.array([0, 0, 0])
    verts = [
        [origin, v1, v1+v2, v2],
        [v3, v1+v3, v1+v2+v3, v2+v3],
        [origin, v1, v1+v3, v3],
        [origin, v2, v2+v3, v3],
        [v1, v1+v2, v1+v2+v3, v1+v3],
        [v2, v1+v2, v1+v2+v3, v2+v3],
    ]

    colors_face = ['#3498DB', '#3498DB', '#E74C3C', '#E74C3C', '#27AE60', '#27AE60']
    for face_verts, fc in zip(verts, colors_face):
        poly = Poly3DCollection([face_verts], alpha=0.2, facecolor=fc, edgecolor='gray', linewidth=0.5)
        ax.add_collection3d(poly)

    ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='#E74C3C', linewidth=3, arrow_length_ratio=0.1, label='v₁=(2,0,0)')
    ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='#3498DB', linewidth=3, arrow_length_ratio=0.1, label='v₂=(0,3,0)')
    ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='#27AE60', linewidth=3, arrow_length_ratio=0.1, label='v₃=(0,0,5)')

    ax.annotate('det(M) = 2·3·5 = 30\nVolume = 30\nRectangular box 2×3×5',
               xy=(0.5, 0.85), fontsize=11, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8),
               xycoords='axes fraction')

    ax.set_xlim([-0.5, 3]); ax.set_ylim([-0.5, 4]); ax.set_zlim([-0.5, 6])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.legend(fontsize=9, loc='upper left')
    ax.set_title('Practice 8: Parallelepiped — Volume = det(M) = 30', fontweight='bold', fontsize=13, pad=20)
    ax.view_init(elev=20, azim=-45)
    save_fig(fig, 'p8-parallelepiped-3d.png')

# ═══════════════════════════════════════════════════════════
# 09 — Basic D11: Stretch Matrix
# ═══════════════════════════════════════════════════════════
def fig_d11_stretch_matrix():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    A = np.array([[2, 0], [0, 0.5]])

    # Left: unit square
    ax1.fill(sq[:,0], sq[:,1], color='#4ECDC4', alpha=0.4, edgecolor='#2C8C84', linewidth=2)
    ax1.plot(sq[:,0], sq[:,1], 'o-', color='#2C8C84', markersize=4)
    ax1.text(0.5, 0.5, '1×1\nArea=1', fontsize=10, ha='center', fontweight='bold')
    ax1.set_title('Before: Unit Square', fontweight='bold')
    ax1.set_xlim(-0.5, 3); ax1.set_ylim(-0.5, 1.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='black', lw=0.5); ax1.axvline(0, color='black', lw=0.5)

    # Right: 2×0.5 rectangle
    corners = np.array([A @ v for v in sq])
    ax2.fill(corners[:,0], corners[:,1], color='#E74C3C', alpha=0.4, edgecolor='#C0392B', linewidth=2)
    ax2.plot(corners[:,0], corners[:,1], 'o-', color='#C0392B', markersize=4)
    ax2.text(1, 0.25, '2×0.5\nArea=1', fontsize=10, ha='center', fontweight='bold')
    ax2.arrow(0, 0, 2, 0, head_width=0.05, head_length=0.05, fc='#E74C3C', ec='#E74C3C', linewidth=2)
    ax2.arrow(0, 0, 0, 0.5, head_width=0.05, head_length=0.05, fc='#3498DB', ec='#3498DB', linewidth=2)

    ax2.annotate('det(A)=2·0.5=1\nx stretches, y shrinks\nArea preserved!',
                xy=(1.8, 0.6), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    ax2.set_title('After: Rectangle 2×0.5', fontweight='bold')
    ax2.set_xlim(-0.5, 3); ax2.set_ylim(-0.5, 1.5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)

    fig.suptitle('Basic D11: Stretch Matrix — Area Preserved (det=1)', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'd11-stretch-matrix.png')

# ═══════════════════════════════════════════════════════════
# 10 — Basic D12: Parallelogram from Columns
# ═══════════════════════════════════════════════════════════
def fig_d12_column_parallelogram():
    fig, ax = plt.subplots(figsize=(7, 7))

    A = np.array([[4, 1], [0, 3]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    corners = np.array([A @ v for v in sq])

    ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.15, edgecolor='#95A5A6', linewidth=1, linestyle='--')
    ax.fill(corners[:,0], corners[:,1], color='#3498DB', alpha=0.3, edgecolor='#2471A3', linewidth=2)
    ax.plot(corners[:,0], corners[:,1], 'o-', color='#2471A3', markersize=4)

    ax.arrow(0, 0, 4, 0, head_width=0.12, head_length=0.12, fc='#E74C3C', ec='#E74C3C', linewidth=2.5)
    ax.arrow(0, 0, 1, 3, head_width=0.12, head_length=0.12, fc='#3498DB', ec='#3498DB', linewidth=2.5)
    ax.text(2, -0.3, 'c₁=(4,0)', fontsize=11, color='#E74C3C', fontweight='bold')
    ax.text(0.3, 2, 'c₂=(1,3)', fontsize=11, color='#3498DB', fontweight='bold')

    # Height
    ax.plot([1, 1], [0, 3], '--', color='#8E44AD', linewidth=2)
    ax.text(1.15, 1.5, 'h=3', fontsize=10, color='#8E44AD', fontweight='bold')
    ax.annotate('Area = base × height\n     = 4 × 3 = 12\n     = det(A) = 4·3−1·0 = 12',
               xy=(3, 2.5), fontsize=11, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))

    ax.set_xlim(-0.5, 5.5); ax.set_ylim(-0.5, 4.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_title('Basic D12: Parallelogram Area = det(A) = 12', fontweight='bold', fontsize=14)
    save_fig(fig, 'd12-column-parallelogram.png')

# ═══════════════════════════════════════════════════════════
# 11 — Basic D13: 90° Rotation on Vector
# ═══════════════════════════════════════════════════════════
def fig_d13_rotation_90():
    fig, ax = plt.subplots(figsize=(7, 7))

    v = np.array([2, 5])
    R90 = np.array([[0, -1], [1, 0]])
    vR = R90 @ v  # (-5, 2)

    ax.arrow(0, 0, v[0], v[1], head_width=0.15, head_length=0.15, fc='#3498DB', ec='#3498DB', linewidth=3, zorder=5)
    ax.arrow(0, 0, vR[0], vR[1], head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)

    # Right angle indicator
    mid = (v + vR) / 4
    ax.plot([0, mid[0]], [0, mid[1]], '--', color='gray', alpha=0.5)
    ax.plot([mid[0]-0.3, mid[0]-0.3+0.3], [mid[1]-0.15, mid[1]-0.15+0.15], 'k-', linewidth=1.5)

    # Rotation arc
    arc = Arc((0, 0), 2, 2, angle=0, theta1=np.degrees(np.arctan2(vR[1], vR[0])),
              theta2=np.degrees(np.arctan2(v[1], v[0])), color='#8E44AD', linewidth=2.5)
    ax.add_patch(arc)

    ax.text(v[0]/2-0.3, v[1]/2-0.3, 'v⃗=(2,5)', fontsize=12, color='#3498DB', fontweight='bold')
    ax.text(vR[0]/2-0.3, vR[1]/2+0.2, 'Av⃗=(−5,2)', fontsize=12, color='#E74C3C', fontweight='bold')
    ax.text(-0.6, 1.5, '90°', fontsize=12, color='#8E44AD', fontweight='bold')

    ax.annotate('v⃗·Av⃗ = (2)(−5)+(5)(2) = 0 → ⊥\n|v⃗| = √29 = |Av⃗|\nPure rotation, no scaling',
               xy=(2.5, 4), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax.set_xlim(-6, 4); ax.set_ylim(-1, 6)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_title('Basic D13: 90° CCW Rotation — Preserves Length', fontweight='bold', fontsize=14)
    save_fig(fig, 'd13-rotation-90.png')

# ═══════════════════════════════════════════════════════════
# 12 — Basic D14: Singular Matrix — Collapse to Line y=2x
# ═══════════════════════════════════════════════════════════
def fig_d14_singular_collapse():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    B = np.array([[1, 2], [2, 4]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

    # Left: unit square with columns
    ax1.fill(sq[:,0], sq[:,1], color='#4ECDC4', alpha=0.4, edgecolor='#2C8C84', linewidth=2)
    ax1.plot(sq[:,0], sq[:,1], 'o-', color='#2C8C84', markersize=4)
    ax1.arrow(0, 0, 1, 2, head_width=0.06, head_length=0.06, fc='#E74C3C', ec='#E74C3C', linewidth=2)
    ax1.arrow(0, 0, 2, 4, head_width=0.06, head_length=0.06, fc='#3498DB', ec='#3498DB', linewidth=2)
    ax1.text(0.3, 1.5, 'c₁=(1,2)', fontsize=10, color='#E74C3C', fontweight='bold')
    ax1.text(1.2, 3, 'c₂=2c₁', fontsize=10, color='#3498DB', fontweight='bold')
    ax1.set_title('Columns: c₂ = 2·c₁ (Parallel!)', fontweight='bold', fontsize=12)
    ax1.set_xlim(-0.5, 3); ax1.set_ylim(-0.5, 5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='black', lw=0.5); ax1.axvline(0, color='black', lw=0.5)

    # Right: grid collapse onto line y=2x
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)
    # Show line y=2x
    x_line = np.linspace(-1, 8, 100)
    ax2.plot(x_line, 2*x_line, '--', color='#E74C3C', linewidth=2, alpha=0.5)

    corners = np.array([B @ v for v in sq])
    ax2.fill(corners[:,0], corners[:,1], color='#E74C3C', alpha=0.4, edgecolor='#C0392B', linewidth=2)
    ax2.plot(corners[:,0], corners[:,1], 'o-', color='#C0392B', markersize=4)

    # Show several grid points collapsing
    for x in [0, 0.5, 1]:
        for y in [0, 0.5, 1]:
            pt = B @ np.array([x, y])
            ax2.plot(pt[0], pt[1], '.', color='#E74C3C', markersize=5, alpha=0.5)

    ax2.annotate('det(B)=0\nEntire plane → line y=2x\n1D subspace (range)',
                xy=(5, 2), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))
    ax2.set_title('After B: All Points Collapse to y=2x', fontweight='bold', fontsize=12)
    ax2.set_xlim(-1, 8); ax2.set_ylim(-1, 7)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)

    fig.suptitle('Basic D14: Singular Matrix — Plane Collapses to Line', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'd14-singular-collapse.png')

# ═══════════════════════════════════════════════════════════
# 13 — Basic D15: Shear Transformation
# ═══════════════════════════════════════════════════════════
def fig_d15_shear():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    S = np.array([[1, 1.5], [0, 1]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

    # Left: before
    ax1.fill(sq[:,0], sq[:,1], color='#4ECDC4', alpha=0.4, edgecolor='#2C8C84', linewidth=2)
    v = np.array([2, 1])
    ax1.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, fc='#E74C3C', ec='#E74C3C', linewidth=2.5)
    ax1.text(1, 0.3, 'v⃗=(2,1)', fontsize=11, color='#E74C3C', fontweight='bold')
    ax1.set_title('Before Shear', fontweight='bold')
    ax1.set_xlim(-0.5, 4.5); ax1.set_ylim(-0.5, 2.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='black', lw=0.5); ax1.axvline(0, color='black', lw=0.5)

    # Right: after
    corners = np.array([S @ p for p in sq])
    ax2.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.12, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
    ax2.fill(corners[:,0], corners[:,1], color='#F39C12', alpha=0.4, edgecolor='#D68910', linewidth=2)
    vS = S @ v  # (3.5, 1)
    ax2.arrow(0, 0, vS[0], vS[1], head_width=0.1, head_length=0.1, fc='#E74C3C', ec='#E74C3C', linewidth=2.5)
    ax2.text(1.8, 0.3, 'Sv⃗=(3.5,1)', fontsize=11, color='#E74C3C', fontweight='bold')

    # Show y unchanged
    ax2.plot([v[1], vS[0]], [v[1], vS[1]], '--', color='green', alpha=0.5)
    ax2.text(2.5, 1.15, 'y unchanged', fontsize=9, color='green')

    ax2.annotate('det(S) = 1·1 − 1.5·0 = 1\nShear preserves area\n"Like pushing a deck of cards"',
                xy=(2.5, 1.7), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FFF9C4', alpha=0.8))
    ax2.set_title('After Shear (det=1)', fontweight='bold')
    ax2.set_xlim(-0.5, 4.5); ax2.set_ylim(-0.5, 2.5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)

    fig.suptitle('Basic D15: Shear — Slides Horizontal Lines, Area Preserved', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'd15-shear.png')

# ═══════════════════════════════════════════════════════════
# 14 — Advanced A3: 60° Rotation Matrix
# ═══════════════════════════════════════════════════════════
def fig_a3_rotation_60():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    R60 = np.array([[0.5, -np.sqrt(3)/2], [np.sqrt(3)/2, 0.5]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    v = np.array([1, 0])

    ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.15, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
    corners = np.array([R60 @ p for p in sq])
    ax.fill(corners[:,0], corners[:,1], color='#3498DB', alpha=0.3, edgecolor='#2471A3', linewidth=2)

    ax.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1, fc='gray', ec='gray', linewidth=2, alpha=0.6)
    vR = R60 @ v
    ax.arrow(0, 0, vR[0], vR[1], head_width=0.1, head_length=0.1, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)

    arc = Arc((0, 0), 1.2, 1.2, angle=0, theta1=0, theta2=60, color='#8E44AD', linewidth=2.5)
    ax.add_patch(arc)

    ax.text(0.6, 0.2, '60°', fontsize=12, color='#8E44AD', fontweight='bold')
    ax.annotate(f'(1,0) → (0.5, √3/2 ≈ 0.866)\nFirst column of R₆₀',
               xy=(0.3, 0.7), fontsize=9, color='#E74C3C')
    ax.annotate('det(R₆₀)=1\nRotation matrices\nhave orthonormal columns',
               xy=(0.6, 1.2), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax.set_xlim(-1.5, 2); ax.set_ylim(-1, 2)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_title('Advanced A3: 60° CCW Rotation — Unit Square Rotated', fontweight='bold', fontsize=14)
    save_fig(fig, 'a3-rotation-60.png')

# ═══════════════════════════════════════════════════════════
# 15 — Advanced A11: Shear then Rotate 90°
# ═══════════════════════════════════════════════════════════
def fig_a11_shear_rotate():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5))

    S = np.array([[1, 1], [0, 1]])
    R = np.array([[0, -1], [1, 0]])
    RS = R @ S  # [[0,-1],[1,1]]

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    steps = [
        (np.eye(2), 'Start\nUnit Square', '#3498DB'),
        (S, 'Step 1: Shear\n[[1,1],[0,1]]', '#F39C12'),
        (R, 'Step 2: Rotate\n[[0,-1],[1,0]]', '#E74C3C'),
        (RS, 'Result: RS\n[[0,-1],[1,1]]', '#8E44AD'),
    ]

    for ax, (M, title, color) in zip(axes, steps):
        corners = np.array([M @ v for v in sq])
        ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
        ax.fill(corners[:,0], corners[:,1], color=color, alpha=0.4, edgecolor=color, linewidth=2)
        ax.plot(corners[:,0], corners[:,1], 'o-', color=color, markersize=4)
        ax.arrow(0, 0, M[0,0], M[1,0], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=2)
        ax.arrow(0, 0, M[0,1], M[1,1], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=2)
        ax.set_title(title, fontsize=9, fontweight='bold')
        ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
        ax.axhline(0, color='black', lw=0.3); ax.axvline(0, color='black', lw=0.3)
        ax.set_xlim(-2, 2.5); ax.set_ylim(-1, 2.5)

    ax.annotate('det(RS) = det(R)·det(S) = 1·1 = 1\nArea preserved through composition',
               xy=(-1, 1.8), fontsize=10, bbox=dict(boxstyle='round', facecolor='#E8DAEF', alpha=0.8))
    fig.suptitle('Advanced A11: Shear then Rotate — Composition Preserves Area', fontweight='bold', fontsize=13)
    plt.tight_layout()
    save_fig(fig, 'a11-shear-rotate.png')

# ═══════════════════════════════════════════════════════════
# 16 — Advanced A12: Reflection Matrix P
# ═══════════════════════════════════════════════════════════
def fig_a12_reflection_p():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    P = np.array([[3/5, 4/5], [4/5, -3/5]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

    ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
    corners = np.array([P @ v for v in sq])
    ax.fill(corners[:,0], corners[:,1], color='#9B59B6', alpha=0.3, edgecolor='#7D3C98', linewidth=2)

    # Reflection line (through (2,1))
    t = np.linspace(-6, 6, 100)
    ax.plot(t, t/2, ':', color='#27AE60', linewidth=2, alpha=0.7)
    ax.text(3.5, 2, 'Reflection line\nthrough (2,1) → y=x/2', fontsize=10, color='#27AE60', fontweight='bold')

    v = np.array([5, 0])
    vP = P @ v  # (3, 4)
    ax.arrow(0, 0, v[0], v[1], head_width=0.15, head_length=0.15, fc='gray', ec='gray', linewidth=2, alpha=0.5)
    ax.arrow(0, 0, vP[0], vP[1], head_width=0.2, head_length=0.2, fc='#E74C3C', ec='#E74C3C', linewidth=2.5, zorder=5)
    ax.text(v[0]/2, -0.4, 'v⃗=(5,0)', fontsize=10, color='gray')
    ax.text(vP[0]/2-0.3, vP[1]/2-0.3, 'Pv⃗=(3,4)', fontsize=10, color='#E74C3C', fontweight='bold')

    # Angle annotation
    ax.annotate('det(P) = −1 (reflection)\nP² = I, P = Pᵀ\nReflection across line y=x/2',
               xy=(3, 3.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#E8DAEF', alpha=0.8))

    ax.set_xlim(-2, 6); ax.set_ylim(-2, 5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_title('Advanced A12: Reflection Matrix — det = −1', fontweight='bold', fontsize=14)
    save_fig(fig, 'a12-reflection-p.png')

# ═══════════════════════════════════════════════════════════
# 17 — Advanced A13: Projection onto Line y=2x
# ═══════════════════════════════════════════════════════════
def fig_a13_projection_line():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    A = np.array([[1/5, 2/5], [2/5, 4/5]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

    ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
    corners = np.array([A @ v for v in sq])
    ax.fill(corners[:,0], corners[:,1], color='#3498DB', alpha=0.35, edgecolor='#2471A3', linewidth=2)

    # Line y = 2x
    t = np.linspace(-1, 5, 100)
    ax.plot(t, 2*t, '--', color='#3498DB', linewidth=1.5, alpha=0.6)

    v = np.array([3, 1])
    v_proj = A @ v  # (1, 2)
    ax.arrow(0, 0, v[0], v[1], head_width=0.12, head_length=0.12, fc='#E74C3C', ec='#E74C3C', linewidth=2.5, zorder=5)
    ax.arrow(0, 0, v_proj[0], v_proj[1], head_width=0.12, head_length=0.12, fc='#27AE60', ec='#27AE60', linewidth=2.5, zorder=4)

    # Dashed perpendicular
    ax.plot([v[0], v_proj[0]], [v[1], v_proj[1]], '--', color='#E67E22', linewidth=1.5)

    ax.text(v[0]/2-0.3, v[1]/2-0.3, '(3,1)', fontsize=11, color='#E74C3C', fontweight='bold')
    ax.text(v_proj[0]/2-0.5, v_proj[1]/2-0.5, '(1,2)', fontsize=11, color='#27AE60', fontweight='bold')

    ax.annotate('det(A) = 4/25−4/25 = 0\nProjection collapses 2D → 1D\nAll points map to line y=2x',
               xy=(2.5, 2.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))

    ax.set_xlim(-0.5, 5); ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)
    ax.set_title('Advanced A13: Projection onto y=2x — det=0', fontweight='bold', fontsize=14)
    save_fig(fig, 'a13-projection-line.png')

# ═══════════════════════════════════════════════════════════
# 18 — Advanced A14: Parallelogram Area in 3D
# ═══════════════════════════════════════════════════════════
def fig_a14_parallelogram_3d():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    a = np.array([4, 1, 2])
    b = np.array([1, 3, -1])
    c = np.cross(a, b)  # (-7, 6, 11)

    # Parallelogram
    verts = [[0,0,0], a.tolist(), (a+b).tolist(), b.tolist()]
    poly = Poly3DCollection([verts], alpha=0.3, facecolor='#3498DB', edgecolor='#2471A3', linewidth=1.5)
    ax.add_collection3d(poly)

    ax.quiver(0, 0, 0, a[0], a[1], a[2], color='#E74C3C', linewidth=2.5, arrow_length_ratio=0.1, label=r'$\vec{a}=(4,1,2)$')
    ax.quiver(0, 0, 0, b[0], b[1], b[2], color='#3498DB', linewidth=2.5, arrow_length_ratio=0.1, label=r'$\vec{b}=(1,3,-1)$')
    ax.quiver(0, 0, 0, c[0], c[1], c[2], color='#27AE60', linewidth=3, arrow_length_ratio=0.08, label=r'$\vec{a}\times\vec{b}=(-7,6,11)$')

    ax.annotate('Area = |a⃗×b⃗| = √206 ≈ 14.35\nUnit normal = (−7,6,11)/√206\ndet(M) = 206',
               xy=(0.5, 0.9), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8),
               xycoords='axes fraction')

    ax.set_xlim([-8, 5]); ax.set_ylim([-2, 7]); ax.set_zlim([-2, 12])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.legend(fontsize=9, loc='upper left')
    ax.set_title('Advanced A14: 3D Parallelogram — Area = |a⃗×b⃗| = √206', fontweight='bold', fontsize=13, pad=20)
    ax.view_init(elev=20, azim=-55)
    save_fig(fig, 'a14-parallelogram-3d.png')

# ═══════════════════════════════════════════════════════════
# 19 — Advanced A15: Rotation on Triangle
# ═══════════════════════════════════════════════════════════
def fig_a15_rotation_triangle():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    tri = np.array([[0,0],[2,0],[0,1],[0,0]])
    A = np.array([[0.8, -0.6], [0.6, 0.8]])

    # Left: original triangle
    ax1.fill(tri[:,0], tri[:,1], color='#4ECDC4', alpha=0.4, edgecolor='#2C8C84', linewidth=2)
    ax1.plot(tri[:,0], tri[:,1], 'o-', color='#2C8C84', markersize=5)
    ax1.text(1, 0.2, 'Area=1', fontsize=12, ha='center', fontweight='bold')
    ax1.set_title('Original Triangle\nArea = ½·2·1 = 1', fontweight='bold')
    ax1.set_xlim(-1.5, 3); ax1.set_ylim(-1, 2.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='black', lw=0.5); ax1.axvline(0, color='black', lw=0.5)

    # Right: rotated triangle
    tri_rot = np.array([A @ v for v in tri])
    ax2.fill(tri[:,0], tri[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
    ax2.fill(tri_rot[:,0], tri_rot[:,1], color='#E74C3C', alpha=0.35, edgecolor='#C0392B', linewidth=2)
    ax2.plot(tri_rot[:,0], tri_rot[:,1], 'o-', color='#C0392B', markersize=5)

    # Angle arc
    v = np.array([2, 0])
    vR = A @ v
    arc = Arc((0, 0), 1.2, 1.2, angle=0, theta1=0,
              theta2=np.degrees(np.arctan2(0.6, 0.8)), color='#8E44AD', linewidth=2)
    ax2.add_patch(arc)

    ax2.text(0.5, 0.2, '≈37°', fontsize=10, color='#8E44AD', fontweight='bold')
    ax2.annotate('Area after = 1 (same)\n|det(A)| = |0.64+0.36| = 1\nPure rotation ≈ 36.87°',
                xy=(0.8, 1.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    ax2.set_title('After Rotation\nArea preserved', fontweight='bold')
    ax2.set_xlim(-1.5, 3); ax2.set_ylim(-1, 2.5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)

    fig.suptitle('Advanced A15: Pure Rotation Preserves Area (|det|=1)', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'a15-rotation-triangle.png')

# ═══════════════════════════════════════════════════════════
# Generate all
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    fig_p1_det_zero_collapse()
    fig_p2_linear_system()
    fig_p3_cross_product_3d()
    fig_p4_triangle_area_3d()
    fig_p5_composition()
    fig_p6_projection()
    fig_p7_inverse_matrix()
    fig_p8_parallelepiped_3d()
    fig_d11_stretch_matrix()
    fig_d12_column_parallelogram()
    fig_d13_rotation_90()
    fig_d14_singular_collapse()
    fig_d15_shear()
    fig_a3_rotation_60()
    fig_a11_shear_rotate()
    fig_a12_reflection_p()
    fig_a13_projection_line()
    fig_a14_parallelogram_3d()
    fig_a15_rotation_triangle()
    print("All 19 graphs generated successfully!")
