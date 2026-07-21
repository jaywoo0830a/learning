#!/usr/bin/env python3
"""Generate all graph images for Session 12C1: Geometric Transformations.

New graphs for 0721 refresh — leveraging 9B/9C prerequisite knowledge.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/12C1"
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
# 12c1a-four-transformations.png
# ============================================================
def fig_four_transformations():
    """Four fundamental 2D transformations on a unit square.
    Each subplot shows the original square (gray dashed) and transformed shape (solid).
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Original unit square vertices
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T

    configs = [
        # (ax, title, matrix, color, label)
        (axes[0, 0], "Rotation by 60°\n$R_{60}$",
         np.array([[np.cos(np.pi/3), -np.sin(np.pi/3)],
                   [np.sin(np.pi/3), np.cos(np.pi/3)]]), 'blue', 'rotated'),
        (axes[0, 1], "Scaling (3, 1.5)\n$S(3, 1.5)$",
         np.array([[3, 0], [0, 1.5]]), 'red', 'scaled'),
        (axes[1, 0], "Reflection across y=x\n$F_{45°}$",
         np.array([[0, 1], [1, 0]]), 'green', 'reflected'),
        (axes[1, 1], "Shear (k=1.2)\n$H_x(1.2)$",
         np.array([[1, 1.2], [0, 1]]), 'purple', 'sheared'),
    ]

    for ax, title, M, color, label in configs:
        transformed = M @ sq
        # Original square
        ax.plot(sq[0], sq[1], 'k--', lw=1.2, alpha=0.4, label='unit square')
        # Transformed shape
        ax.fill(transformed[0], transformed[1], alpha=0.15, color=color)
        ax.plot(transformed[0], transformed[1], color=color, lw=2.5, label=label)
        # Mark vertices
        ax.plot(transformed[0, :-1], transformed[1, :-1], 'o', color=color, markersize=5)
        # Basis vectors
        ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1,
                  color='gray', alpha=0.5, width=0.008)
        ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1,
                  color='gray', alpha=0.5, width=0.008)
        # Columns = images of basis
        c1, c2 = M[:, 0], M[:, 1]
        ax.quiver(0, 0, c1[0], c1[1], angles='xy', scale_units='xy', scale=1,
                  color=color, alpha=0.7, width=0.015, label='A·e₁')
        ax.quiver(0, 0, c2[0], c2[1], angles='xy', scale_units='xy', scale=1,
                  color=color, alpha=0.7, width=0.015, label='A·e₂')
        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.set_xlim(-0.5, 3.5); ax.set_ylim(-0.5, 3)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color='gray', lw=0.5)
        ax.axvline(0, color='gray', lw=0.5)
        # Legend
        ax.legend(fontsize=7, loc='upper right')

    fig.suptitle('Four Fundamental 2D Transformations',
                 fontsize=14, fontweight='bold', y=1.01)
    save('12c1a-four-transformations.png')


# ============================================================
# 12c1b-eigenvectors.png
# ============================================================
def fig_eigenvectors():
    """Eigenvectors visualization — directions preserved by a matrix.
    Left: scaling matrix with real eigenvectors along axes.
    Right: rotation matrix (no real eigenvectors).
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Scaling matrix — eigenvectors are axes
    theta = np.linspace(0, 2*np.pi, 300)
    circle = np.array([np.cos(theta), np.sin(theta)])
    A = np.array([[3, 0], [0, 1.5]])
    ellipse = A @ circle

    ax1.fill(circle[0], circle[1], alpha=0.08, color='blue', label='unit circle')
    ax1.plot(circle[0], circle[1], 'b--', lw=1.5, alpha=0.5)
    ax1.fill(ellipse[0], ellipse[1], alpha=0.12, color='red', label='A·circle')
    ax1.plot(ellipse[0], ellipse[1], 'r-', lw=2.5)

    # Eigenvector directions
    ax1.quiver(0, 0, 3, 0, angles='xy', scale_units='xy', scale=1,
               color='darkred', width=0.02, label='λ₁=3, v=(1,0)')
    ax1.quiver(0, 0, 0, 1.5, angles='xy', scale_units='xy', scale=1,
               color='darkgreen', width=0.02, label='λ₂=1.5, v=(0,1)')

    ax1.set_title('Scaling: Real Eigenvectors\n$A = \\mathrm{diag}(3,\\;1.5)$',
                  fontweight='bold')
    ax1.set_xlim(-3.5, 3.5); ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', lw=0.5)
    ax1.axvline(0, color='gray', lw=0.5)
    ax1.legend(fontsize=8, loc='upper right')

    # Right: Rotation matrix — no real eigenvectors
    R = np.array([[0, -1], [1, 0]])  # 90° rotation
    rot_circle = R @ circle

    ax2.fill(circle[0], circle[1], alpha=0.08, color='blue', label='unit circle')
    ax2.plot(circle[0], circle[1], 'b--', lw=1.5, alpha=0.5)
    ax2.fill(rot_circle[0], rot_circle[1], alpha=0.12, color='purple')
    ax2.plot(rot_circle[0], rot_circle[1], 'purple', lw=2.5, label='R·circle')

    # Show a few vectors and their rotated versions
    test_vecs = [(1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7)]
    for vx, vy in test_vecs:
        vec = np.array([vx, vy])
        rvec = R @ vec
        ax2.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1,
                   color='blue', alpha=0.5, width=0.01)
        ax2.quiver(0, 0, rvec[0], rvec[1], angles='xy', scale_units='xy', scale=1,
                   color='purple', alpha=0.5, width=0.01)

    ax2.set_title('Rotation: No Real Eigenvectors\n$R_{90^\\circ}$ = 90 deg rotation',
                  fontweight='bold')
    ax2.set_xlim(-1.5, 1.5); ax2.set_ylim(-1.5, 1.5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='gray', lw=0.5)
    ax2.axvline(0, color='gray', lw=0.5)
    ax2.legend(fontsize=8, loc='upper right')

    fig.suptitle('Eigenvectors: Invariant Directions Under a Matrix',
                 fontsize=14, fontweight='bold')
    save('12c1b-eigenvectors.png')


# ============================================================
# 12c1c-svd-decomposition.png
# ============================================================
def fig_svd_decomposition():
    """SVD: Any matrix = rotate → scale → rotate.
    Shows the unit circle transforming through each step.
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    theta = np.linspace(0, 2*np.pi, 300)
    circle = np.array([np.cos(theta), np.sin(theta)])

    # A = [[2, 1], [1, 2]]
    A = np.array([[2, 1], [1, 2]])
    U, S, Vt = np.linalg.svd(A)
    # Vt rotates input, Sigma scales, U rotates output

    stages = [
        (0, "Step 1: $V^T$ (rotate)", Vt, 'blue'),
        (1, "Step 2: $\\Sigma$ (scale)", np.diag(S), 'red'),
        (2, "Step 3: $U$ (rotate)", U, 'green'),
    ]

    current = circle.copy()
    for idx, title, M, color in stages:
        ax = axes[idx]
        ax.fill(current[0], current[1], alpha=0.08, color='gray')
        ax.plot(current[0], current[1], color='gray', linestyle='--', lw=1.2, alpha=0.5,
                label='before')
        transformed = M @ current
        ax.fill(transformed[0], transformed[1], alpha=0.15, color=color)
        ax.plot(transformed[0], transformed[1], color=color, lw=2.5,
                label='after')

        # Basis vectors
        e1 = M @ np.array([1, 0])
        e2 = M @ np.array([0, 1])
        ax.quiver(0, 0, e1[0], e1[1], angles='xy', scale_units='xy', scale=1,
                  color=color, width=0.02, alpha=0.8)
        ax.quiver(0, 0, e2[0], e2[1], angles='xy', scale_units='xy', scale=1,
                  color=color, width=0.02, alpha=0.8)

        ax.set_title(title, fontweight='bold', fontsize=11)
        ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
        ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
        ax.axhline(0, color='gray', lw=0.5)
        ax.axvline(0, color='gray', lw=0.5)
        ax.legend(fontsize=8, loc='upper right')
        current = transformed.copy()

    # Show singular values
    axes[1].annotate(f'$\\sigma_1={S[0]:.2f}$\n$\\sigma_2={S[1]:.2f}$',
                     xy=(0.05, 0.7), fontsize=11, color='darkred',
                     fontweight='bold',
                     bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    fig.suptitle('SVD: $A = U \\Sigma V^T$ — Rotate, Scale, Rotate',
                 fontsize=14, fontweight='bold', y=1.02)
    save('12c1c-svd-decomposition.png')


# ============================================================
# 12c1d-composition.png  [NEW]
# ============================================================
def fig_composition():
    """Composition of transformations — order matters.
    Shows: rotate then reflect vs reflect then rotate on same triangle.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Triangle vertices
    tri = np.array([[1, 0], [2, 1], [1, 2], [1, 0]]).T

    R = np.array([[0, -1], [1, 0]])  # 90° CCW
    F = np.array([[1, 0], [0, -1]])  # reflect across x-axis

    # Left: R then F
    FR = F @ R
    tri1 = FR @ tri
    ax1.fill(tri[0], tri[1], alpha=0.1, color='gray', label='original')
    ax1.plot(tri[0], tri[1], color='gray', linestyle='--', lw=1.2)
    ax1.fill(tri1[0], tri1[1], alpha=0.2, color='blue')
    ax1.plot(tri1[0], tri1[1], 'b-', lw=2.5, label='R→F')
    ax1.plot(tri[0, 0], tri[1, 0], 'ko', markersize=8)
    ax1.plot(tri1[0, 0], tri1[1, 0], 'bo', markersize=8)

    # Annotate
    ax1.text(1.5, 1.8, '$F \\cdot R$', fontsize=14, fontweight='bold', color='blue',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    ax1.text(0.4, 0.2, 'P(1,0)', fontsize=9)

    ax1.set_title('Rotate 90° THEN Reflect\nacross x-axis', fontweight='bold')
    ax1.set_xlim(-2, 3); ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.legend(fontsize=9)

    # Right: F then R
    RF = R @ F
    tri2 = RF @ tri
    ax2.fill(tri[0], tri[1], alpha=0.1, color='gray', label='original')
    ax2.plot(tri[0], tri[1], color='gray', linestyle='--', lw=1.2)
    ax2.fill(tri2[0], tri2[1], alpha=0.2, color='red')
    ax2.plot(tri2[0], tri2[1], 'r-', lw=2.5, label='F→R')
    ax2.plot(tri[0, 0], tri[1, 0], 'ko', markersize=8)
    ax2.plot(tri2[0, 0], tri2[1, 0], 'ro', markersize=8)

    ax2.text(1.5, 0.5, '$R \\cdot F$', fontsize=14, fontweight='bold', color='red',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    ax2.set_title('Reflect THEN Rotate 90°\nDifferent result!', fontweight='bold')
    ax2.set_xlim(-2, 3); ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='gray', lw=0.5); ax2.axvline(0, color='gray', lw=0.5)
    ax2.legend(fontsize=9)

    fig.suptitle('Composition Order Matters: $AB \\neq BA$',
                 fontsize=14, fontweight='bold')
    save('12c1d-composition.png')


# ============================================================
# 12c1e-3d-rotations.png  [NEW]
# ============================================================
def fig_3d_rotations():
    """3D rotations around each axis — visualized as rotating a box.
    """
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    fig = plt.figure(figsize=(15, 5))

    # A simple L-shaped block vertices
    def make_block():
        verts = np.array([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0.5, 1, 0], [0.5, 0.5, 0], [0, 0.5, 0],
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0.5, 1, 1], [0.5, 0.5, 1], [0, 0.5, 1],
        ])
        return verts.T

    def plot_block(ax, verts, color, alpha=0.3):
        # Plot edges
        edges = [
            [0,1],[1,2],[2,3],[3,4],[4,5],[5,0],
            [6,7],[7,8],[8,9],[9,10],[10,11],[11,6],
            [0,6],[1,7],[2,8],[3,9],[4,10],[5,11]
        ]
        for i, j in edges:
            ax.plot([verts[0,i], verts[0,j]], [verts[1,i], verts[1,j]],
                    [verts[2,i], verts[2,j]], color=color, lw=1.5)

    def Rx(theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])

    def Ry(theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])

    def Rz(theta):
        c, s = np.cos(theta), np.sin(theta)
        return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

    titles = ['Rotation around X-axis\n$R_x(60°)$',
              'Rotation around Y-axis\n$R_y(60°)$',
              'Rotation around Z-axis\n$R_z(60°)$']
    matrices = [Rx(np.pi/3), Ry(np.pi/3), Rz(np.pi/3)]
    colors = ['red', 'green', 'blue']

    for i in range(3):
        ax = fig.add_subplot(1, 3, i+1, projection='3d')
        verts = make_block()
        # Original (ghost)
        plot_block(ax, verts, 'gray', 0.1)
        # Transformed
        verts_t = matrices[i] @ verts
        plot_block(ax, verts_t, colors[i])

        # Axis indicator
        axis_vec = np.zeros(3)
        axis_vec[i] = 1.5
        ax.quiver(0, 0, 0, *(axis_vec if i == 0 else [0, 0, 0]),
                  color=colors[i], lw=3, arrow_length_ratio=0.2)
        if i == 1:
            ax.quiver(0, 0, 0, 0, 1.5, 0, color=colors[i], lw=3, arrow_length_ratio=0.2)
        if i == 2:
            ax.quiver(0, 0, 0, 0, 0, 1.5, color=colors[i], lw=3, arrow_length_ratio=0.2)

        ax.set_title(titles[i], fontweight='bold', fontsize=11)
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_zlim(-1.5, 1.5)
        ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
        ax.view_init(elev=25, azim=-60)

    fig.suptitle('3D Rotations Around Each Axis',
                 fontsize=14, fontweight='bold', y=1.02)
    save('12c1e-3d-rotations.png')


# ============================================================
# 12c1f-reflection-geometry.png  [NEW]
# ============================================================
def fig_reflection_geometry():
    """Reflection across arbitrary line — geometric meaning of Householder matrix.
    Shows original vector, its reflection, and the mirror line.
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Mirror line at angle α = 30°
    alpha = np.pi/6
    line_dir = np.array([np.cos(alpha), np.sin(alpha)])

    # Original vector
    v = np.array([3, 1])

    # Reflection matrix
    F = np.array([[np.cos(2*alpha), np.sin(2*alpha)],
                  [np.sin(2*alpha), -np.cos(2*alpha)]])
    v_ref = F @ v

    # Mirror line (extended)
    x = np.linspace(-3, 5, 100)
    ax.plot(x, np.tan(alpha)*x, 'orange', lw=2.5, label=f'mirror line (α={30}°)')

    # Original vector
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
              color='blue', width=0.02, label='original v')

    # Reflected vector
    ax.quiver(0, 0, v_ref[0], v_ref[1], angles='xy', scale_units='xy', scale=1,
              color='red', width=0.02, label='reflected v\' = F·v')

    # Projection onto mirror line
    proj = np.dot(v, line_dir) * line_dir
    ax.plot([0, proj[0]], [0, proj[1]], 'g--', lw=1.5, alpha=0.7, label='projection onto mirror')
    # Perpendicular component (dashed to show reflection)
    perp = v - proj
    ax.plot([proj[0], v[0]], [proj[1], v[1]], 'g:', lw=1, alpha=0.5)
    ax.plot([proj[0], v_ref[0]], [proj[1], v_ref[1]], 'g:', lw=1, alpha=0.5)

    # Angle arc
    arc_theta = np.linspace(0, alpha, 50)
    ax.plot(0.5*np.cos(arc_theta), 0.5*np.sin(arc_theta), 'purple', lw=1.5)
    ax.text(0.55, 0.15, 'α', fontsize=13, color='purple', fontweight='bold')

    ax.set_title('Reflection Across a Line\n$F_\\alpha$ = reflection matrix',
                 fontweight='bold', fontsize=11)
    ax.set_xlim(-1, 5); ax.set_ylim(-2, 4)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=9, loc='upper left')
    save('12c1f-reflection-geometry.png')


# ============================================================
# 12c1g-homogeneous-translation.png  [NEW]
# ============================================================
def fig_homogeneous_translation():
    """Translation visualized: homogeneous coordinates allow translation as matrix.
    Shows original shape, translated shapes.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Shape: a house shape
    house = np.array([
        [0, 0], [2, 0], [2, 1.5], [1, 2.5], [0, 1.5], [0, 0]
    ]).T

    # Left: Can't do translation with 2x2
    ax1.fill(house[0], house[1], alpha=0.15, color='gray')
    ax1.plot(house[0], house[1], color='gray', lw=2, label='original')

    # Add some rotated versions
    R = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                  [np.sin(np.pi/4), np.cos(np.pi/4)]])
    rot_house = R @ house
    ax1.fill(rot_house[0], rot_house[1], alpha=0.15, color='blue')
    ax1.plot(rot_house[0], rot_house[1], 'b-', lw=2, label='rotated (2×2 OK)')

    ax1.text(1.5, 1.8, 'Rotation ✔\nTranslation ✗',
             fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    ax1.set_title('2×2 Matrices:\nRotation yes, Translation no',
                  fontweight='bold')
    ax1.set_xlim(-2, 4); ax1.set_ylim(-1, 4)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.legend(fontsize=9)

    # Right: Homogeneous coordinates
    house_h = np.vstack([house, np.ones((1, house.shape[1]))])

    # T = translate by (3, 1)
    T = np.array([[1, 0, 3], [0, 1, 1], [0, 0, 1]])
    house_t = T @ house_h

    # R_h = rotate in homogeneous
    Rh = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4), 0],
                   [np.sin(np.pi/4), np.cos(np.pi/4), 0],
                   [0, 0, 1]])

    # Rotate about (1, 1): T(1,1) · R · T(-1,-1)
    T1 = np.array([[1, 0, 1], [0, 1, 1], [0, 0, 1]])
    T_neg1 = np.array([[1, 0, -1], [0, 1, -1], [0, 0, 1]])
    M = T1 @ Rh @ T_neg1
    house_rt = M @ house_h

    ax2.fill(house[0], house[1], alpha=0.08, color='gray')
    ax2.plot(house[0], house[1], color='gray', linestyle='--', lw=1.2, label='original')
    ax2.fill(house_t[0], house_t[1], alpha=0.15, color='green')
    ax2.plot(house_t[0], house_t[1], 'g-', lw=2, label='translated (3×3)')
    ax2.fill(house_rt[0], house_rt[1], alpha=0.15, color='purple')
    ax2.plot(house_rt[0], house_rt[1], 'purple', lw=2,
             label='rotated about (1,1)')

    ax2.set_title('3×3 Homogeneous:\nTranslation + Rotation in one matrix',
                  fontweight='bold')
    ax2.set_xlim(-2, 6); ax2.set_ylim(-1, 5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='gray', lw=0.5); ax2.axvline(0, color='gray', lw=0.5)
    ax2.legend(fontsize=9, loc='upper left')

    fig.suptitle('Homogeneous Coordinates: Translation as Matrix Multiplication',
                 fontsize=14, fontweight='bold')
    save('12c1g-homogeneous-translation.png')


# ============================================================
if __name__ == "__main__":
    print("Generating 12C1 graphs...")
    fig_four_transformations()
    fig_eigenvectors()
    fig_svd_decomposition()
    fig_composition()
    fig_3d_rotations()
    fig_reflection_geometry()
    fig_homogeneous_translation()
    print("Done! ✓")
