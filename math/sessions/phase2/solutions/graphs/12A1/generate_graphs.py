#!/usr/bin/env python3
"""Generate visual graphs for 12A1 Complex Numbers Solutions."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Polygon, Arc, Circle
import numpy as np
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
# 01 — Practice 1: Division (3-i)/(2+i) = 1-i, Matrix
# ═══════════════════════════════════════════════════════════
def fig_p1_division_matrix():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Left: Complex plane showing (3-i)/(2+i) = 1-i
    z_num = np.array([3, -1])
    z_den = np.array([2, 1])
    z_result = np.array([1, -1])

    ax1.axhline(0, color='black', lw=0.8)
    ax1.axvline(0, color='black', lw=0.8)

    # Show divisor and result
    ax1.arrow(0, 0, 3, -1, head_width=0.12, head_length=0.12, fc='#3498DB', ec='#3498DB', linewidth=2.5, zorder=4)
    ax1.annotate('3−i', (3, -1), textcoords="offset points", xytext=(8, 8), fontsize=11, color='#3498DB', fontweight='bold')
    ax1.arrow(0, 0, 2, 1, head_width=0.1, head_length=0.1, fc='#95A5A6', ec='#95A5A6', linewidth=2, alpha=0.6)
    ax1.annotate('2+i', (2, 1), textcoords="offset points", xytext=(8, 5), fontsize=9, color='#95A5A6')
    ax1.arrow(0, 0, 1, -1, head_width=0.12, head_length=0.12, fc='#E74C3C', ec='#E74C3C', linewidth=3.5, zorder=5)
    ax1.annotate('= 1−i', (1, -1), textcoords="offset points", xytext=(10, -15), fontsize=12, color='#E74C3C', fontweight='bold')

    ax1.set_xlim(-1, 5); ax1.set_ylim(-3, 3)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.25)
    ax1.set_xlabel('Real'); ax1.set_ylabel('Imaginary')
    ax1.set_title('Complex Division: (3−i)/(2+i) = 1−i', fontweight='bold', fontsize=12)

    # Right: Matrix M and determinant
    # Show unit square transformed by M = [[1,1],[-1,1]]
    M = np.array([[1, 1], [-1, 1]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    t_sq = np.array([M @ v for v in sq])

    ax2.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.2, edgecolor='#95A5A6', linewidth=1, linestyle='--')
    ax2.fill(t_sq[:,0], t_sq[:,1], color='#E74C3C', alpha=0.35, edgecolor='#C0392B', linewidth=2)
    ax2.plot(t_sq[:,0], t_sq[:,1], 'o-', color='#C0392B', markersize=4)
    ax2.arrow(0, 0, M[0,0], M[1,0], head_width=0.1, head_length=0.1, fc='#E74C3C', ec='#E74C3C', linewidth=2.5)
    ax2.arrow(0, 0, M[0,1], M[1,1], head_width=0.1, head_length=0.1, fc='#3498DB', ec='#3498DB', linewidth=2.5)
    ax2.text(1.5, -0.3, r'$M\vec{e}_1$=(1,−1)', fontsize=9, color='#E74C3C')
    ax2.text(1.5, 1.3, r'$M\vec{e}_2$=(1,1)', fontsize=9, color='#3498DB')

    ax2.annotate('det(M)=1²+(−1)²=2\n|z|²=1²+(−1)²=2\n|z|² = det(M) ✓',
                xy=(1.5, 1.8), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax2.set_xlim(-1.5, 3); ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.25)
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)
    ax2.set_title('Matrix M for z=1−i: det(M)=|z|²', fontweight='bold', fontsize=12)

    fig.suptitle('Practice 1: Complex Division & Matrix-Determinant Verification', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'p1-division-matrix.png')

# ═══════════════════════════════════════════════════════════
# 02 — Practice 2: z = 1-i, z⁸ = 16 (rotation cycle)
# ═══════════════════════════════════════════════════════════
def fig_p2_polar_power():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: z=1-i in polar form
    z = np.array([1, -1])
    r = np.sqrt(2)
    theta = -np.pi/4

    ax1.axhline(0, color='black', lw=0.8); ax1.axvline(0, color='black', lw=0.8)
    circle_r = Circle((0,0), r, fill=False, color='#3498DB', linestyle=':', alpha=0.5, linewidth=1.5)
    ax1.add_patch(circle_r)
    ax1.arrow(0, 0, z[0], z[1], head_width=0.12, head_length=0.12, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    arc = Arc((0,0), 1, 1, angle=0, theta1=-45, theta2=0, color='#8E44AD', linewidth=2.5)
    ax1.add_patch(arc)
    ax1.annotate('z = 1−i', (1, -1), textcoords="offset points", xytext=(10, -15), fontsize=12, color='#E74C3C', fontweight='bold')
    ax1.text(0.7, -0.1, 'θ=−45°', fontsize=10, color='#8E44AD', fontweight='bold')
    ax1.text(1.1, -0.6, f'r=√2≈{r:.2f}', fontsize=10, color='#3498DB')

    ax1.set_xlim(-1.5, 2.5); ax1.set_ylim(-2.5, 1.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.25)
    ax1.set_xlabel('Real'); ax1.set_ylabel('Imaginary')
    ax1.set_title('Polar Form: z = √2·e^{−iπ/4}', fontweight='bold', fontsize=12)

    # Right: z⁸ = 16 — rotation cycle
    angles = [-45, -90, -135, -180, -225, -270, -315, -360]
    radii = [r**k for k in range(1, 9)]
    colors = plt.cm.plasma(np.linspace(0, 0.85, 8))

    ax2.axhline(0, color='black', lw=0.8); ax2.axvline(0, color='black', lw=0.8)
    for i, (ang, rad, c) in enumerate(zip(angles, radii, colors)):
        th = np.radians(ang)
        x, y = rad * np.cos(th), rad * np.sin(th)
        ax2.plot([0, x], [0, y], '-', color=c, linewidth=2, alpha=0.7)
        ax2.plot(x, y, 'o', color=c, markersize=8, zorder=5)
        if i == 7:
            ax2.annotate(f'z⁸=16', (x, y), textcoords="offset points", xytext=(10, 5),
                        fontsize=11, color=c, fontweight='bold')

    # Arc showing full rotation
    circle_16 = Circle((0,0), 16, fill=False, color='#E74C3C', linestyle='--', alpha=0.3, linewidth=1)
    ax2.add_patch(circle_16)
    ax2.annotate('8 × (−45°) = −360°\n→ Returns to 0°\n→ Pure real: 16',
                xy=(10, 8), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    ax2.set_xlim(-18, 18); ax2.set_ylim(-18, 18)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.2)
    ax2.set_xlabel('Real'); ax2.set_ylabel('Imaginary')
    ax2.set_title('z⁸ = (√2)⁸·e^{−i·8π/4} = 16', fontweight='bold', fontsize=12)

    fig.suptitle('Practice 2: Polar Form & De Moivre — Powers Spiral', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'p2-polar-power.png')

# ═══════════════════════════════════════════════════════════
# 03 — Practice 3: Cube Roots of −8
# ═══════════════════════════════════════════════════════════
def fig_p3_cube_roots_minus8():
    fig, ax = plt.subplots(figsize=(8, 7.5))

    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    circle_2 = Circle((0,0), 2, fill=False, color='gray', linestyle='--', alpha=0.4, linewidth=1.2)
    ax.add_patch(circle_2)

    # Roots
    roots = [
        (1, np.sqrt(3), r'$2e^{i\pi/3}=1+i\sqrt{3}$', '#E74C3C'),
        (-2, 0, r'$2e^{i\pi}=-2$', '#27AE60'),
        (1, -np.sqrt(3), r'$2e^{i5\pi/3}=1-i\sqrt{3}$', '#3498DB'),
    ]

    poly_x, poly_y = [], []
    for x, y, label, color in roots:
        ax.plot(x, y, 'o', color=color, markersize=14, zorder=5)
        off_x, off_y = (10, 15) if y >= 0 else (10, -18)
        if y == 0 and x < 0:
            off_x, off_y = (-25, -18)
        ax.annotate(label, (x, y), textcoords="offset points", xytext=(off_x, off_y),
                   fontsize=9, color=color, fontweight='bold')
        poly_x.append(x); poly_y.append(y)

    # Triangle
    poly_x.append(poly_x[0]); poly_y.append(poly_y[0])
    ax.fill(poly_x, poly_y, color='#8E44AD', alpha=0.15, edgecolor='#7D3C98', linewidth=2)
    ax.plot(poly_x, poly_y, '-', color='#7D3C98', linewidth=2)

    # 120° arcs
    for i, ang in enumerate([60, 180, 300]):
        arc = Arc((0,0), 1.2, 1.2, angle=0, theta1=ang-60, theta2=ang+60, color='#8E44AD', linewidth=1.5, linestyle=':', alpha=0.5)
        ax.add_patch(arc)

    ax.text(0, 0, '120°', fontsize=10, color='#8E44AD', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    ax.annotate('Equilateral triangle\non circle of radius 2\nM³ = −8I for each root',
               xy=(2.2, 1.2), fontsize=10, bbox=dict(boxstyle='round', facecolor='#E8DAEF', alpha=0.8))

    ax.set_xlim(-3, 3.5); ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Practice 3: Three Cube Roots of −8 — Equilateral Triangle', fontweight='bold', fontsize=14)
    save_fig(fig, 'p3-cube-roots-minus8.png')

# ═══════════════════════════════════════════════════════════
# 04 — Practice 4: i³ Rotation (90° CW)
# ═══════════════════════════════════════════════════════════
def fig_p4_i3_rotation():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    z = np.array([3, 4])
    z_result = np.array([4, -3])  # (3+4i)*i³ = 4-3i

    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)

    # Original z
    ax.arrow(0, 0, z[0], z[1], head_width=0.15, head_length=0.15, fc='#3498DB', ec='#3498DB', linewidth=3, zorder=5)
    ax.annotate('3+4i', (3, 4), textcoords="offset points", xytext=(8, 8), fontsize=13, color='#3498DB', fontweight='bold')

    # After i³ rotation
    ax.arrow(0, 0, z_result[0], z_result[1], head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    ax.annotate('(3+4i)·i³ = 4−3i', (4, -3), textcoords="offset points", xytext=(8, -15), fontsize=13, color='#E74C3C', fontweight='bold')

    # Rotation arc (270° CW = -90°)
    th1 = np.degrees(np.arctan2(4, 3))  # ~53°
    th2 = np.degrees(np.arctan2(-3, 4))  # ~-37° = 323°
    arc = Arc((0,0), 2.5, 2.5, angle=0, theta1=th2, theta2=th1, color='#8E44AD', linewidth=3)
    ax.add_patch(arc)
    ax.text(1.2, 0.6, '−90°\n(i³ = −i)', fontsize=10, color='#8E44AD', fontweight='bold')

    # J³ matrix
    ax.annotate('J³ = [[0,1],[-1,0]] = R₂₇₀° (90° CW)',
                xy=(-2, 3.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax.set_xlim(-4, 6); ax.set_ylim(-5, 5.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.25)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Practice 4: Multiplying by i³ Rotates 90° Clockwise', fontweight='bold', fontsize=14)
    save_fig(fig, 'p4-i3-rotation.png')

# ═══════════════════════════════════════════════════════════
# 05 — Practice 5: z⁶ from z=−1+i√3
# ═══════════════════════════════════════════════════════════
def fig_p5_z6_computation():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Polar form
    z = np.array([-1, np.sqrt(3)])
    r = 2; theta = 2*np.pi/3
    ax1.axhline(0, color='black', lw=0.8); ax1.axvline(0, color='black', lw=0.8)
    circle_2 = Circle((0,0), 2, fill=False, color='#3498DB', linestyle=':', alpha=0.4)
    ax1.add_patch(circle_2)
    ax1.arrow(0, 0, z[0], z[1], head_width=0.12, head_length=0.12, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    arc = Arc((0,0), 1.3, 1.3, angle=0, theta1=0, theta2=120, color='#8E44AD', linewidth=2.5)
    ax1.add_patch(arc)
    ax1.annotate('z=−1+i√3', (-1, np.sqrt(3)), textcoords="offset points", xytext=(-30, 10),
                fontsize=11, color='#E74C3C', fontweight='bold')
    ax1.text(0.5, 0.7, 'θ=120°', fontsize=10, color='#8E44AD', fontweight='bold')
    ax1.text(0.2, 1.9, 'r=2', fontsize=10, color='#3498DB')

    ax1.set_xlim(-2.5, 2.5); ax1.set_ylim(-0.5, 3)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.2)
    ax1.set_xlabel('Real'); ax1.set_ylabel('Imaginary')
    ax1.set_title('z = 2e^{i·2π/3}', fontweight='bold', fontsize=12)

    # Right: z⁶ = 64 on real axis
    ax2.axhline(0, color='black', lw=0.8); ax2.axvline(0, color='black', lw=0.8)
    # Show the rotation in 120° increments
    for k in range(1, 7):
        radius = 2**k
        angle = k * 120  # degrees
        x, y = radius * np.cos(np.radians(angle)), radius * np.sin(np.radians(angle))
        ax2.plot([0, x], [0, y], '-', color=plt.cm.plasma(k/7), linewidth=2, alpha=0.6)
        ax2.plot(x, y, 'o', color=plt.cm.plasma(k/7), markersize=7)

    # Final point z⁶ = 64
    ax2.plot(64, 0, 'o', color='#E74C3C', markersize=14, zorder=5)
    ax2.annotate('z⁶ = 64', (64, 0), textcoords="offset points", xytext=(5, 12),
                fontsize=12, color='#E74C3C', fontweight='bold')

    ax2.annotate('6 × 120° = 720° = 2 × 360°\nReturns to real axis\n64 = 2⁶',
                xy=(30, 40), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    ax2.set_xlim(-10, 75); ax2.set_ylim(-50, 50)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.2)
    ax2.set_xlabel('Real'); ax2.set_ylabel('Imaginary')
    ax2.set_title('z⁶ = (2e^{i·2π/3})⁶ = 64', fontweight='bold', fontsize=12)

    fig.suptitle('Practice 5: z⁶ = 64 — Rotation Returns to Positive Real', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'p5-z6-computation.png')

# ═══════════════════════════════════════════════════════════
# 06 — Practice 6: Cube Roots Triangle Area & 120° Rotation
# ═══════════════════════════════════════════════════════════
def fig_p6_triangle_area():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    # Left: Triangle with area calculation
    roots = [(1, np.sqrt(3)), (-2, 0), (1, -np.sqrt(3))]
    ax1.axhline(0, color='black', lw=0.8); ax1.axvline(0, color='black', lw=0.8)
    circle_2 = Circle((0,0), 2, fill=False, color='gray', linestyle='--', alpha=0.3)
    ax1.add_patch(circle_2)

    px = [p[0] for p in roots] + [roots[0][0]]
    py = [p[1] for p in roots] + [roots[0][1]]
    ax1.fill(px, py, color='#3498DB', alpha=0.2, edgecolor='#2471A3', linewidth=2)
    for x, y in roots:
        ax1.plot(x, y, 'o', color='#E74C3C', markersize=12, zorder=5)

    # Height visualization
    ax1.plot([-2, -2], [0, np.sqrt(3)], '--', color='#8E44AD', linewidth=2)
    ax1.text(-2.3, np.sqrt(3)/2, 'h=√3', fontsize=10, color='#8E44AD')
    ax1.text(0, 0.5, 'base=2√3', fontsize=9, color='#27AE60')

    ax1.annotate('Area = ½(base)(height)\n      = ½(2√3)(3)\n      = 3√3',
                xy=(1.5, 1.5), fontsize=11, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))
    ax1.set_xlim(-3.5, 3); ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.2)
    ax1.set_xlabel('Real'); ax1.set_ylabel('Imaginary')
    ax1.set_title('Triangle Area = 3√3', fontweight='bold', fontsize=12)

    # Right: 120° rotation matrix connection
    ax2.axhline(0, color='black', lw=0.8); ax2.axvline(0, color='black', lw=0.8)
    circle_1 = Circle((0,0), 1, fill=False, color='gray', linestyle='--', alpha=0.3)
    ax2.add_patch(circle_1)

    omega = np.array([-0.5, np.sqrt(3)/2])  # e^{i·2π/3}
    ax2.arrow(0, 0, omega[0], omega[1], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    ax2.annotate('ω=e^{i·2π/3}', (omega[0], omega[1]), textcoords="offset points", xytext=(-35, 12),
                fontsize=10, color='#E74C3C', fontweight='bold')

    arc = Arc((0,0), 1, 1, angle=0, theta1=0, theta2=120, color='#8E44AD', linewidth=2.5)
    ax2.add_patch(arc)
    ax2.text(0.3, 0.5, '120°', fontsize=11, color='#8E44AD', fontweight='bold')

    ax2.annotate('R₁₂₀° = [[-1/2,-√3/2],[√3/2,-1/2]]\n↔ ω = e^{i·2π/3}\nR³ = I ✓',
                xy=(0.7, 0.9), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    ax2.set_xlim(-1.5, 1.8); ax2.set_ylim(-1, 1.8)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.2)
    ax2.set_xlabel('Real'); ax2.set_ylabel('Imaginary')
    ax2.set_title('120° Rotation ↔ Primitive Cube Root', fontweight='bold', fontsize=12)

    fig.suptitle('Practice 6: Triangle Area & 120° Rotation Matrix Connection', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'p6-triangle-area.png')

# ═══════════════════════════════════════════════════════════
# 07 — Practice 7: M⁻¹ = 1/z Correspondence
# ═══════════════════════════════════════════════════════════
def fig_p7_inverse_correspondence():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

    z = np.array([3, 4])
    z_inv = np.array([3/25, -4/25])

    # Left: Complex plane
    ax1.axhline(0, color='black', lw=0.8); ax1.axvline(0, color='black', lw=0.8)
    circle_1 = Circle((0,0), 1, fill=False, color='#27AE60', linewidth=1.5, linestyle='--', alpha=0.5)
    ax1.add_patch(circle_1)

    ax1.arrow(0, 0, z[0], z[1], head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    ax1.annotate('z = 3+4i\n|z| = 5', (3, 4), textcoords="offset points", xytext=(8, 8), fontsize=11, color='#E74C3C', fontweight='bold')

    ax1.arrow(0, 0, z_inv[0], z_inv[1], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=3, zorder=5)
    ax1.annotate('1/z = 3/25 − 4i/25\n|1/z| = 1/5', (z_inv[0], z_inv[1]), textcoords="offset points",
                xytext=(15, -15), fontsize=10, color='#3498DB', fontweight='bold')

    ax1.text(1.5, -1, 'Outside → Inside\n|z|·|1/z| = 1', fontsize=9, color='#27AE60',
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.7))

    ax1.set_xlim(-1, 5); ax1.set_ylim(-2, 5)
    ax1.set_aspect('equal'); ax1.grid(True, alpha=0.2)
    ax1.set_xlabel('Real'); ax1.set_ylabel('Imaginary')
    ax1.set_title('Complex Reciprocal: 1/z = z̄/|z|²', fontweight='bold', fontsize=12)

    # Right: Matrix inverse geometry
    M = np.array([[3, -4], [4, 3]])
    Minv = np.array([[3/25, 4/25], [-4/25, 3/25]])
    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])

    t_M = np.array([M @ v for v in sq])
    t_Minv = np.array([Minv @ v for v in sq])

    ax2.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.15, edgecolor='#95A5A6', linewidth=1, linestyle='--')
    ax2.fill(t_M[:,0], t_M[:,1], color='#E74C3C', alpha=0.25, edgecolor='#C0392B', linewidth=2)
    ax2.fill(t_Minv[:,0], t_Minv[:,1], color='#3498DB', alpha=0.3, edgecolor='#2471A3', linewidth=2)

    ax2.arrow(0, 0, M[0,0], M[1,0], head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', linewidth=2, alpha=0.6)
    ax2.arrow(0, 0, Minv[0,0], Minv[1,0], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=2)

    ax2.annotate('M⁻¹ = 1/det(M) [[3,4],[-4,3]]\n     = (1/25)[[3,4],[-4,3]]\nMatches 1/z matrix!',
                xy=(2.5, 3), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))

    ax2.set_xlim(-1, 5); ax2.set_ylim(-1, 5)
    ax2.set_aspect('equal'); ax2.grid(True, alpha=0.2)
    ax2.axhline(0, color='black', lw=0.5); ax2.axvline(0, color='black', lw=0.5)
    ax2.set_title('M⁻¹ = Matrix for 1/z', fontweight='bold', fontsize=12)

    fig.suptitle('Practice 7: Matrix Inverse ≡ Complex Reciprocal', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, 'p7-inverse-correspondence.png')

# ═══════════════════════════════════════════════════════════
# 08 — Practice 8: Roots of Unity — Product & n-gon Area
# ═══════════════════════════════════════════════════════════
def fig_p8_roots_unity():
    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

    for ax, n, title in zip(axes, [3, 4, 6], ['n=3: Triangle\nArea=3√3/4', 'n=4: Square\nArea=2', 'n=6: Hexagon\nArea=3√3/2']):
        circle = Circle((0,0), 1.2, fill=False, color='gray', linestyle='--', alpha=0.35)
        ax.add_patch(circle)
        ax.axhline(0, color='black', lw=0.5); ax.axvline(0, color='black', lw=0.5)

        roots_pts = [1.2 * np.exp(1j * 2 * np.pi * k / n) for k in range(n)]
        poly_x = [r.real for r in roots_pts] + [roots_pts[0].real]
        poly_y = [r.imag for r in roots_pts] + [roots_pts[0].imag]
        ax.fill(poly_x, poly_y, color='#3498DB', alpha=0.2, edgecolor='#2471A3', linewidth=2)

        colors = plt.cm.viridis(np.linspace(0, 0.9, n))
        for k, r in enumerate(roots_pts):
            ax.plot(r.real, r.imag, 'o', color=colors[k], markersize=10, zorder=5)

        area = n/2 * np.sin(2*np.pi/n) * 1.2**2
        prod = (-1)**(n-1)
        ax.text(0, 0, f'Π={prod}\nSum=0', fontsize=9, ha='center', va='center',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.85))
        ax.set_title(f'{title}\nArea≈{area:.2f}', fontweight='bold', fontsize=10)
        ax.set_aspect('equal'); ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.8, 1.8)
        ax.set_xlabel('Re'); ax.set_ylabel('Im')

    fig.suptitle('Practice 8: Roots of Unity = Regular n-gon, Product = (−1)^{n−1}, Sum = 0', fontweight='bold', fontsize=13)
    plt.tight_layout()
    save_fig(fig, 'p8-roots-unity.png')

# ═══════════════════════════════════════════════════════════
# 09 — Advanced A3: 4th Roots of −16 (Square)
# ═══════════════════════════════════════════════════════════
def fig_a3_fourth_roots():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    circle_2 = Circle((0,0), 2, fill=False, color='gray', linestyle='--', alpha=0.35, linewidth=1.2)
    ax.add_patch(circle_2)

    rts = [(np.sqrt(2), np.sqrt(2)), (-np.sqrt(2), np.sqrt(2)),
           (-np.sqrt(2), -np.sqrt(2)), (np.sqrt(2), -np.sqrt(2))]
    labels = ['√2+i√2', '−√2+i√2', '−√2−i√2', '√2−i√2']
    colors = ['#E74C3C', '#3498DB', '#27AE60', '#F39C12']

    poly_x = [r[0] for r in rts] + [rts[0][0]]
    poly_y = [r[1] for r in rts] + [rts[0][1]]
    ax.fill(poly_x, poly_y, color='#8E44AD', alpha=0.15, edgecolor='#7D3C98', linewidth=2)

    for (x, y), lbl, c in zip(rts, labels, colors):
        ax.plot(x, y, 'o', color=c, markersize=12, zorder=5)
        off_x = 10 if x > 0 else -28
        off_y = 12 if y > 0 else -18
        ax.annotate(lbl, (x, y), textcoords="offset points", xytext=(off_x, off_y),
                   fontsize=9, color=c, fontweight='bold')

    ax.annotate('Square inscribed in circle r=2\n−16 = 16e^{iπ}\n$z_k = 2e^{i(π+2πk)/4}$',
               xy=(1.2, 1.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#E8DAEF', alpha=0.8))

    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Advanced A3: Four 4th Roots of −16 = Square', fontweight='bold', fontsize=14)
    save_fig(fig, 'a3-fourth-roots.png')

# ═══════════════════════════════════════════════════════════
# 10 — Advanced A4: Square from 4th Roots of 1 (Area=2)
# ═══════════════════════════════════════════════════════════
def fig_a4_square_4th_roots():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    circle_1 = Circle((0,0), 1, fill=False, color='gray', linestyle='--', alpha=0.35)
    ax.add_patch(circle_1)

    rts = [(1,0), (0,1), (-1,0), (0,-1)]
    labels = ['1', 'i', '−1', '−i']
    colors = ['#27AE60', '#3498DB', '#E74C3C', '#F39C12']

    poly_x = [r[0] for r in rts] + [rts[0][0]]
    poly_y = [r[1] for r in rts] + [rts[0][1]]
    ax.fill(poly_x, poly_y, color='#27AE60', alpha=0.15, edgecolor='#1E8449', linewidth=2)

    for (x, y), lbl, c in zip(rts, labels, colors):
        ax.plot(x, y, 'o', color=c, markersize=14, zorder=5)
        off_x, off_y = (12, 10) if x >= 0 and y >= 0 else \
                        (-25, 10) if x < 0 and y >= 0 else \
                        (-25, -18) if x < 0 else (12, -18)
        ax.annotate(lbl, (x, y), textcoords="offset points", xytext=(off_x, off_y),
                   fontsize=11, color=c, fontweight='bold')

    # Show diagonal and side length
    ax.plot([1, -1], [0, 0], '--', color='#8E44AD', alpha=0.5, linewidth=1.5)
    ax.text(0, 0.2, 'diag=2', fontsize=9, color='#8E44AD', ha='center')
    ax.annotate('s = √(1²+1²) = √2\nArea = s² = 2\n= 2r² = 2(1)² = 2',
               xy=(0.7, 0.8), fontsize=11, bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))

    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Advanced A4: 4th Roots of 1 = Square, Area = 2', fontweight='bold', fontsize=14)
    save_fig(fig, 'a4-square-4th-roots.png')

# ═══════════════════════════════════════════════════════════
# 11 — Advanced A7: Cube Roots of 8i (Triangle)
# ═══════════════════════════════════════════════════════════
def fig_a7_cube_roots_8i():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    circle_2 = Circle((0,0), 2, fill=False, color='gray', linestyle='--', alpha=0.35, linewidth=1.2)
    ax.add_patch(circle_2)

    rts = [(np.sqrt(3), 1), (-np.sqrt(3), 1), (0, -2)]
    labels = ['√3+i', '−√3+i', '−2i']
    colors = ['#E74C3C', '#3498DB', '#27AE60']

    poly_x = [r[0] for r in rts] + [rts[0][0]]
    poly_y = [r[1] for r in rts] + [rts[0][1]]
    ax.fill(poly_x, poly_y, color='#3498DB', alpha=0.15, edgecolor='#2471A3', linewidth=2)

    for (x, y), lbl, c in zip(rts, labels, colors):
        ax.plot(x, y, 'o', color=c, markersize=12, zorder=5)
        off_x = 10 if x >= 0 else -25
        off_y = 12 if y > 0 else -18
        ax.annotate(lbl, (x, y), textcoords="offset points", xytext=(off_x, off_y),
                   fontsize=10, color=c, fontweight='bold')

    ax.annotate('$8i = 8e^{iπ/2}$\n$z_k = 2e^{i(π/2+2πk)/3}$\nEquilateral triangle\nArea = 3√3',
               xy=(1.2, 1.5), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))

    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Advanced A7: Three Cube Roots of 8i', fontweight='bold', fontsize=14)
    save_fig(fig, 'a7-cube-roots-8i.png')

# ═══════════════════════════════════════════════════════════
# 12 — Advanced A11: z³=−1, 60° Rotation Matrix
# ═══════════════════════════════════════════════════════════
def fig_a11_z3_minus1():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    circle_1 = Circle((0,0), 1, fill=False, color='gray', linestyle='--', alpha=0.35)
    ax.add_patch(circle_1)

    z = np.array([0.5, np.sqrt(3)/2])  # e^{iπ/3}
    ax.arrow(0, 0, z[0], z[1], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    ax.annotate('z=½+i√3/2\n=e^{iπ/3}', (0.5, np.sqrt(3)/2), textcoords="offset points",
               xytext=(10, 10), fontsize=10, color='#E74C3C', fontweight='bold')

    arc = Arc((0,0), 0.9, 0.9, angle=0, theta1=0, theta2=60, color='#8E44AD', linewidth=2.5)
    ax.add_patch(arc)
    ax.text(0.5, 0.25, '60°', fontsize=11, color='#8E44AD', fontweight='bold')

    # Show z³ = -1 path
    ax.plot(-1, 0, 'o', color='#27AE60', markersize=14, zorder=5)
    ax.annotate('z³=−1', (-1, 0), textcoords="offset points", xytext=(-25, -18),
               fontsize=11, color='#27AE60', fontweight='bold')

    ax.annotate('R = [[1/2,-√3/2],[√3/2,1/2]]\nR³ = -I ✓\ndet(R) = 1',
               xy=(0.5, 0.85), fontsize=10, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.5, 1.8)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Advanced A11: z = e^{iπ/3}, z³ = −1, 60° Rotation', fontweight='bold', fontsize=13)
    save_fig(fig, 'a11-z3-minus1.png')

# ═══════════════════════════════════════════════════════════
# 13 — Advanced A12: Triangle from z₁, z₁z₂
# ═══════════════════════════════════════════════════════════
def fig_a12_triangle_product():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)

    z1 = np.array([3*np.cos(np.pi/6), 3*np.sin(np.pi/6)])  # 3e^{iπ/6}
    z2_th = np.pi/3  # 60°
    z1z2 = np.array([6*np.cos(np.pi/6+np.pi/3), 6*np.sin(np.pi/6+np.pi/3)])  # 6e^{iπ/2} = 6i

    # Triangle: 0, z1, z1z2
    tri_x = [0, z1[0], z1z2[0], 0]
    tri_y = [0, z1[1], z1z2[1], 0]
    ax.fill(tri_x, tri_y, color='#3498DB', alpha=0.2, edgecolor='#2471A3', linewidth=2)

    ax.arrow(0, 0, z1[0], z1[1], head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', linewidth=3, zorder=5)
    ax.annotate('z₁=3e^{iπ/6}', (z1[0], z1[1]), textcoords="offset points", xytext=(10, 10),
               fontsize=10, color='#E74C3C', fontweight='bold')

    ax.arrow(0, 0, z1z2[0], z1z2[1], head_width=0.2, head_length=0.2, fc='#8E44AD', ec='#8E44AD', linewidth=3.5, zorder=4)
    ax.annotate('z₁z₂=6i', (0, 6), textcoords="offset points", xytext=(15, 5),
               fontsize=11, color='#8E44AD', fontweight='bold')

    # Angle arc
    arc = Arc((0,0), 2, 2, angle=0, theta1=30, theta2=90, color='#27AE60', linewidth=2.5)
    ax.add_patch(arc)
    ax.text(1.5, 1.8, 'θ₂=60°', fontsize=10, color='#27AE60', fontweight='bold')

    ax.annotate('Area = ½|z₁||z₁z₂|sin(60°)\n     = ½·3·6·√3/2\n     = 9√3/2',
               xy=(2, 4), fontsize=11, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))

    ax.set_xlim(-0.5, 4); ax.set_ylim(-0.5, 7)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Advanced A12: Triangle (0, z₁, z₁z₂), Area = 9√3/2', fontweight='bold', fontsize=13)
    save_fig(fig, 'a12-triangle-product.png')

# ═══════════════════════════════════════════════════════════
# 14 — Advanced A14: Roots of Unity Sum = 0 (Center of Mass)
# ═══════════════════════════════════════════════════════════
def fig_a14_roots_sum_zero():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    circle = Circle((0,0), 1.5, fill=False, color='gray', linestyle='--', alpha=0.3)
    ax.add_patch(circle)

    n = 5
    roots = [1.5 * np.exp(1j * 2 * np.pi * k / n) for k in range(n)]
    poly_x = [r.real for r in roots] + [roots[0].real]
    poly_y = [r.imag for r in roots] + [roots[0].imag]
    ax.fill(poly_x, poly_y, color='#3498DB', alpha=0.15, edgecolor='#2471A3', linewidth=2)

    colors = plt.cm.viridis(np.linspace(0, 0.9, n))
    for k, r in enumerate(roots):
        ax.plot(r.real, r.imag, 'o', color=colors[k], markersize=10, zorder=5)

    # Center of mass arrow
    ax.plot(0, 0, '*', color='#E74C3C', markersize=20, zorder=6)
    ax.annotate('Sum = 0\nCenter of mass\nat origin', (0, 0), textcoords="offset points",
               xytext=(15, -20), fontsize=11, color='#E74C3C', fontweight='bold')

    ax.annotate('$1+ω+ω²+⋯+ω^{n-1} = \\frac{1-ω^n}{1-ω} = 0$\nAverage position = 0 → origin',
               xy=(1, 1.3), fontsize=10, bbox=dict(boxstyle='round', facecolor='#D6EAF8', alpha=0.8))

    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.2)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_xlabel('Real'); ax.set_ylabel('Imaginary')
    ax.set_title('Advanced A14: Sum of n-th Roots of Unity = 0', fontweight='bold', fontsize=14)
    save_fig(fig, 'a14-roots-sum-zero.png')

# ═══════════════════════════════════════════════════════════
# 15 — Advanced A15: T∘S vs S∘T (Rotation & Reflection)
# ═══════════════════════════════════════════════════════════
def fig_a15_composition():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5))

    T = np.array([[0, -1], [1, 0]])    # Rotate 90°
    S = np.array([[1, 0], [0, -1]])    # Reflect x-axis
    TS = T @ S   # [[0,1],[1,0]]  — reflect y=x
    ST = S @ T   # [[0,-1],[-1,0]] — reflect y=-x

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    steps = [
        (np.eye(2), 'Start\nUnit Square', '#3498DB'),
        (S, '1. Reflect\n(x-axis)', '#E74C3C'),
        (T, '2. Rotate\n(90° CCW)', '#F39C12'),
        (TS, 'T∘S = [[0,1],[1,0]]\nReflect y=x', '#8E44AD'),
    ]

    for ax, (M, title, color) in zip(axes, steps):
        corners = np.array([M @ v for v in sq])
        ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
        ax.fill(corners[:,0], corners[:,1], color=color, alpha=0.35, edgecolor=color, linewidth=2)
        ax.plot(corners[:,0], corners[:,1], 'o-', color=color, markersize=3)
        ax.arrow(0, 0, M[0,0], M[1,0], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=1.8)
        ax.arrow(0, 0, M[0,1], M[1,1], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=1.8)
        ax.set_title(title, fontsize=9, fontweight='bold')
        ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
        ax.axhline(0, color='black', lw=0.3); ax.axvline(0, color='black', lw=0.3)
        ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)

    ax.annotate('Reflect then Rotate ≠ Rotate then Reflect\nMatrix multiplication is NOT commutative!',
                xy=(-1.5, 1.5), fontsize=11, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    fig.suptitle('Advanced A15: T∘S (Reflect x then Rotate) = Reflect y=x', fontweight='bold', fontsize=13)
    plt.tight_layout()
    save_fig(fig, 'a15-composition-ts.png')

# ═══════════════════════════════════════════════════════════
# 16 — Advanced A15b: S∘T vs T∘S comparison
# ═══════════════════════════════════════════════════════════
def fig_a15b_composition_st():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.5))

    T = np.array([[0, -1], [1, 0]])
    S = np.array([[1, 0], [0, -1]])
    ST = S @ T

    sq = np.array([[0,0],[1,0],[1,1],[0,1],[0,0]])
    steps = [
        (np.eye(2), 'Start\nUnit Square', '#3498DB'),
        (T, '1. Rotate\n(90° CCW)', '#F39C12'),
        (S, '2. Reflect\n(x-axis)', '#E74C3C'),
        (ST, 'S∘T = [[0,-1],[-1,0]]\nReflect y=−x', '#8E44AD'),
    ]

    for ax, (M, title, color) in zip(axes, steps):
        corners = np.array([M @ v for v in sq])
        ax.fill(sq[:,0], sq[:,1], color='#BDC3C7', alpha=0.1, edgecolor='#95A5A6', linewidth=0.8, linestyle='--')
        ax.fill(corners[:,0], corners[:,1], color=color, alpha=0.35, edgecolor=color, linewidth=2)
        ax.plot(corners[:,0], corners[:,1], 'o-', color=color, markersize=3)
        ax.arrow(0, 0, M[0,0], M[1,0], head_width=0.08, head_length=0.08, fc='#E74C3C', ec='#E74C3C', linewidth=1.8)
        ax.arrow(0, 0, M[0,1], M[1,1], head_width=0.08, head_length=0.08, fc='#3498DB', ec='#3498DB', linewidth=1.8)
        ax.set_title(title, fontsize=9, fontweight='bold')
        ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
        ax.axhline(0, color='black', lw=0.3); ax.axvline(0, color='black', lw=0.3)
        ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)

    ax.annotate('T∘S (y=x) ≠ S∘T (y=−x)\nDifferent results — order matters!',
                xy=(-1.5, 1.5), fontsize=11, bbox=dict(boxstyle='round', facecolor='#FADBD8', alpha=0.8))

    fig.suptitle('Advanced A15: S∘T (Rotate then Reflect) = Reflect y=−x', fontweight='bold', fontsize=13)
    plt.tight_layout()
    save_fig(fig, 'a15b-composition-st.png')

# ═══════════════════════════════════════════════════════════
# Generate all
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    fig_p1_division_matrix()
    fig_p2_polar_power()
    fig_p3_cube_roots_minus8()
    fig_p4_i3_rotation()
    fig_p5_z6_computation()
    fig_p6_triangle_area()
    fig_p7_inverse_correspondence()
    fig_p8_roots_unity()
    fig_a3_fourth_roots()
    fig_a4_square_4th_roots()
    fig_a7_cube_roots_8i()
    fig_a11_z3_minus1()
    fig_a12_triangle_product()
    fig_a14_roots_sum_zero()
    fig_a15_composition()
    fig_a15b_composition_st()
    print("All 16 graphs generated successfully!")
