#!/usr/bin/env python3
"""Generate visual graphs for 15B Optimization and Related Rates."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, Circle, Polygon, Wedge, Rectangle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
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

# ════════════════════════════════════════════════════
# 01 — Box Volume Maximization
# ════════════════════════════════════════════════════
def fig_01_box_volume():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: Diagram of the 12x12 sheet with cut corners
    # Sheet outline
    sheet = Rectangle((-6, -6), 12, 12, fill=False, ec='black', lw=2)
    ax1.add_patch(sheet)
    # Cut squares
    for sx, sy in [(-6, -6), (6, -6), (-6, 6), (6, 6)]:
        cut = Rectangle((sx, sy), 2, 2, fill=True, fc='#E74C3C', alpha=0.3, ec='#E74C3C', lw=1.5)
        ax1.add_patch(cut)
    # Dotted fold lines
    for x in [-4, 4]:
        ax1.plot([x, x], [-6, 6], 'b--', lw=1.5, alpha=0.6)
    for y in [-4, 4]:
        ax1.plot([-6, 6], [y, y], 'b--', lw=1.5, alpha=0.6)
    ax1.annotate('x=2', (-6, -6.8), fontsize=10, color='#E74C3C', fontweight='bold')
    ax1.annotate('12-2x=8', (3, 6.5), fontsize=10, color='blue', fontweight='bold')
    ax1.set_aspect('equal'); ax1.set_xlim(-7, 7); ax1.set_ylim(-7, 7)
    ax1.set_title('Sheet: 12×12, Cut x=2', fontweight='bold')
    ax1.axis('off')

    # Right: Volume function
    x = np.linspace(0.1, 5.9, 300)
    V = x * (12 - 2*x)**2
    ax2.plot(x, V, 'b-', lw=2.5)
    ax2.plot(2, 128, 'o', color='#E74C3C', ms=12, zorder=5)
    ax2.axvline(2, color='#E74C3C', lw=1.5, linestyle='--', alpha=0.5)
    ax2.axhline(128, color='#E74C3C', lw=1.5, linestyle='--', alpha=0.5)
    ax2.annotate('Max: (2, 128)', (2, 128), textcoords="offset points", xytext=(20, 15),
                 fontsize=11, color='#E74C3C', fontweight='bold')
    ax2.set_xlim(0, 6); ax2.set_ylim(0, 140)
    ax2.grid(True, alpha=0.25)
    ax2.set_title('V(x)=x(12-2x)²', fontweight='bold')
    ax2.set_xlabel('x'); ax2.set_ylabel('Volume')
    fig.suptitle('Box Volume Maximization', fontweight='bold', fontsize=14)
    plt.tight_layout()
    save_fig(fig, '01-box-volume.png')

# ════════════════════════════════════════════════════
# 02 — Distance Minimization: Point (2,0) to y=√x
# ════════════════════════════════════════════════════
def fig_02_distance_minimization():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, 4, 400)
    y = np.sqrt(x)
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    # Target point
    ax.plot(2, 0, 'ko', ms=12, zorder=5)
    ax.annotate('(2,0)', (2, 0), textcoords="offset points", xytext=(5, -20), fontsize=11, fontweight='bold')

    # Closest point
    cx, cy = 1.5, np.sqrt(1.5)
    ax.plot(cx, cy, 'o', color='#E74C3C', ms=10, zorder=5)
    ax.annotate(f'(1.5, {cy:.3f})', (cx, cy), textcoords="offset points", xytext=(10, 12),
                fontsize=10, color='#E74C3C', fontweight='bold')

    # Shortest path (normal line)
    ax.plot([2, cx], [0, cy], '#E74C3C', lw=2.5, zorder=4)
    # Tangent at closest point
    m = 1/(2*np.sqrt(cx))
    tx = np.linspace(cx-1, cx+1, 50)
    ax.plot(tx, cy + m*(tx - cx), '#2ECC71', lw=2, linestyle='--', label='tangent', zorder=4)

    # Right angle indicator
    ax.plot([1.75, 1.75, 1.68], [cy-0.08, cy-0.15, cy-0.15], 'k-', lw=1.2)

    ax.set_xlim(-0.2, 4.5); ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.25)
    ax.set_title('Shortest Distance: Point (2,0) to y=√x', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '02-distance-minimization.png')

# ════════════════════════════════════════════════════
# 03 — Rectangle Inscribed in a Semicircle
# ════════════════════════════════════════════════════
def fig_03_rectangle_semicircle():
    fig, ax = plt.subplots(figsize=(9, 7))
    R = 3
    # Semicircle
    theta = np.linspace(0, np.pi, 200)
    ax.plot(R*np.cos(theta), R*np.sin(theta), 'b-', lw=3, zorder=3)
    # Diameter
    ax.plot([-R, R], [0, 0], 'b-', lw=3, zorder=3)

    # Optimal rectangle
    x_opt = R/np.sqrt(2)
    y_opt = np.sqrt(R**2 - x_opt**2)
    rect = Rectangle((-x_opt, 0), 2*x_opt, y_opt, fill=True, fc='#E74C3C', alpha=0.25, ec='#E74C3C', lw=2.5)
    ax.add_patch(rect)

    ax.plot(x_opt, y_opt, 'o', color='#E74C3C', ms=10, zorder=5)
    ax.annotate(f'({x_opt:.2f}, {y_opt:.2f})', (x_opt, y_opt), textcoords="offset points",
                xytext=(10, 10), fontsize=10, color='#E74C3C', fontweight='bold')
    ax.annotate(f'width={2*x_opt:.2f}', (0, -0.4), fontsize=10, ha='center')
    ax.annotate(f'height={y_opt:.2f}', (-x_opt-0.6, y_opt/2), fontsize=10, va='center')

    ax.set_aspect('equal'); ax.set_xlim(-4, 4); ax.set_ylim(-1, 4)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.25)
    ax.set_title('Rectangle Inscribed in Semicircle — Max Area = R²', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '03-rectangle-semicircle.png')

# ════════════════════════════════════════════════════
# 04E — Closest point on ellipse x^2/4 + y^2/9 = 1 to (1,0)
# ════════════════════════════════════════════════════
def fig_04_ellipse_closest():
    """Example 4 — closest point on x^2/4 + y^2/9 = 1 to (1, 0)."""
    Dfun = lambda u: -5*u**2 - 4*u + 10
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Left: ellipse with target, closest, and farthest points
    ax1.set_aspect('equal')
    t = np.linspace(0, 2*np.pi, 400)
    ax1.plot(2*np.cos(t), 3*np.sin(t), 'b-', lw=2.5, zorder=3)
    # target point (1, 0)
    ax1.plot(1, 0, 'o', color='#2C3E50', ms=9, zorder=5)
    ax1.annotate('(1, 0)', (1, 0), textcoords="offset points", xytext=(8, 6),
                 fontsize=11, color='#2C3E50', fontweight='bold')
    # closest point (2, 0)
    ax1.plot(2, 0, 'o', color='#E74C3C', ms=11, zorder=5)
    ax1.plot([1, 2], [0, 0], color='#E74C3C', lw=2, zorder=4)
    ax1.annotate('closest (2, 0)', (2, 0), textcoords="offset points", xytext=(10, 10),
                 fontsize=11, color='#E74C3C', fontweight='bold')
    ax1.annotate('distance = 1', (1.5, 0.18), fontsize=11, color='#E74C3C', ha='center')
    # farthest point (for context, dashed)
    xf, yf = -0.8, 3*np.sqrt(1-0.4**2)
    ax1.plot(xf, yf, 'o', mfc='white', mec='#27AE60', ms=9, zorder=5)
    ax1.plot([1, xf], [0, yf], '--', color='#27AE60', lw=1.5, alpha=0.6)
    ax1.annotate('farthest (−0.8, 2.75)', (xf, yf), textcoords="offset points",
                 xytext=(10, -18), fontsize=10, color='#27AE60')
    ax1.set_xlim(-3, 3); ax1.set_ylim(-3.5, 3.5)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.grid(True, alpha=0.25)
    ax1.set_title('Closest Point on the Ellipse', fontweight='bold')
    ax1.set_xlabel('x'); ax1.set_ylabel('y')

    # Right: D(u) = -5u^2 - 4u + 10 on [-1, 1]
    u = np.linspace(-1, 1, 300)
    ax2.plot(u, Dfun(u), 'b-', lw=2.5, zorder=3)
    ax2.plot(-0.4, Dfun(-0.4), 'o', mfc='white', mec='#F39C12', ms=10, zorder=5)
    ax2.annotate('local MAX\n(u = −0.4)', (-0.4, Dfun(-0.4)), textcoords="offset points",
                 xytext=(-170, 6), fontsize=11, color='#F39C12', fontweight='bold')
    ax2.plot(1, Dfun(1), 'o', color='#E74C3C', ms=11, zorder=5)
    ax2.annotate('min at u = 1', (1, Dfun(1)), textcoords="offset points",
                 xytext=(12, -18), fontsize=11, color='#E74C3C', fontweight='bold')
    ax2.plot(-1, Dfun(-1), 'o', color='gray', ms=8, zorder=5)
    ax2.set_xlim(-1.2, 1.2); ax2.set_ylim(0, 12)
    ax2.axvline(0, color='gray', lw=0.5)
    ax2.grid(True, alpha=0.25)
    ax2.set_title('D(u) = −5u² − 4u + 10 on [−1, 1]', fontweight='bold')
    ax2.set_xlabel('u = cos t'); ax2.set_ylabel('D(u)')

    save_fig(fig, '04-ellipse-closest.png')

# ════════════════════════════════════════════════════
# 04 — Ladder Related Rates
# ════════════════════════════════════════════════════
def fig_04_ladder_rates():
    fig, ax = plt.subplots(figsize=(8, 7))

    # Wall and ground
    ax.plot([0, 0], [0, 6], 'k-', lw=4)
    ax.plot([0, 7], [0, 0], 'k-', lw=4)

    # Ladder at current position (x=3, y=4)
    ax.plot([3, 0], [0, 4], '#E74C3C', lw=4, zorder=3, label='ladder (5m)')

    # Ladder at slightly later position (dashed)
    ax.plot([3.3, 0], [0, 3.75], '#E74C3C', lw=2, linestyle='--', alpha=0.4, zorder=2)

    # Velocity arrows
    ax.arrow(3, 0, 0.8, 0, head_width=0.15, head_length=0.15, fc='#3498DB', ec='#3498DB', lw=2.5, zorder=5)
    ax.annotate('dx/dt = +1 m/s', (3.4, -0.4), fontsize=10, color='#3498DB', fontweight='bold')

    ax.arrow(0, 4, 0, -0.6, head_width=0.12, head_length=0.15, fc='#2ECC71', ec='#2ECC71', lw=2.5, zorder=5)
    ax.annotate('dy/dt = -0.75 m/s', (-0.3, 3.6), fontsize=10, color='#2ECC71', fontweight='bold', ha='right')

    # Labels
    ax.annotate('x=3', (1.5, -0.3), fontsize=12, fontweight='bold')
    ax.annotate('y=4', (-0.6, 2), fontsize=12, fontweight='bold')
    ax.annotate('5 m', (1.8, 2.3), fontsize=12, color='#E74C3C', fontweight='bold')

    # Right angle
    ax.plot([0.3, 0.3, 0], [0, 0.3, 0.3], 'k-', lw=1)

    ax.set_xlim(-1, 7); ax.set_ylim(-1, 6)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_title('Ladder Problem: x²+y²=25', fontweight='bold')
    ax.set_xlabel('x (m)'); ax.set_ylabel('y (m)')
    ax.legend(fontsize=10, loc='upper right')
    save_fig(fig, '04-ladder-rates.png')

# ════════════════════════════════════════════════════
# 05 — Conical Tank Related Rates
# ════════════════════════════════════════════════════
def fig_05_conical_tank():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Tank outline
    tank_x = [0, 2, 0, -2, 0]
    tank_y = [5, 0, 0, 0, 5]
    ax.fill(tank_x, tank_y, alpha=0.12, color='#3498DB', ec='#3498DB', lw=2.5)

    # Water level at h=1
    r_at_h = 0.4 * 1  # r = 0.4h
    water_x = [0, r_at_h, 0, -r_at_h, 0]
    water_y = [1, 0, 0, 0, 1]
    ax.fill(water_x, water_y, alpha=0.35, color='#3498DB', ec='#3498DB', lw=2)

    # Similar triangles
    ax.plot([0, 2], [1, 1], 'k--', lw=1, alpha=0.5)
    ax.plot([0, 2], [0, 0], 'k-', lw=1)
    ax.annotate('r', (1, -0.3), fontsize=11, ha='center')
    ax.annotate('h', (-0.4, 0.5), fontsize=11, va='center')
    ax.annotate('R=2', (2.2, -0.3), fontsize=11, ha='center')
    ax.annotate('H=5', (-0.6, 2.5), fontsize=11, va='center')

    # Inflow arrow
    ax.arrow(0, 2.5, 0, 1.2, head_width=0.25, head_length=0.2, fc='#E74C3C', ec='#E74C3C', lw=2)
    ax.annotate('dV/dt=3 m³/min', (0.5, 3.2), fontsize=11, color='#E74C3C', fontweight='bold')

    # dh/dt annotation
    ax.annotate('dh/dt≈5.97 m/min\n(at h=1)', (1.5, 1.2), fontsize=11, color='#2ECC71', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    ax.set_xlim(-3, 4); ax.set_ylim(-1, 6)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_title('Conical Tank: Similar Triangles r/h=R/H', fontweight='bold')
    ax.set_xlabel('radius (m)'); ax.set_ylabel('height (m)')
    save_fig(fig, '05-conical-tank.png')

# ════════════════════════════════════════════════════
# 06 — Rotating Spotlight Related Rates
# ════════════════════════════════════════════════════
def fig_06_spotlight():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Wall
    ax.axvline(0, color='k', lw=4, ymin=0.05, ymax=0.95)

    # Spotlight
    ax.plot(100, 0, 'o', color='#E67E22', ms=15, zorder=5)
    ax.annotate('light\nsource', (100, 0), textcoords="offset points", xytext=(8, -15),
                fontsize=10, color='#E67E22', fontweight='bold')

    # Beam at 45 degrees
    theta = np.radians(45)
    # Two edge rays
    for offset in [-5, 5]:
        t_offset = np.radians(offset)
        x_beam = [100, 0]
        y_beam = [0, 100*np.tan(theta + t_offset)]
        ax.plot(x_beam, y_beam, '#E67E22', lw=1.5, alpha=0.4)

    # Center ray
    ax.plot([100, 0], [0, 100], '#E67E22', lw=3, zorder=4)
    ax.annotate('θ=45°', (80, 15), fontsize=12, color='#E67E22', fontweight='bold')

    # Light spot
    ax.plot(0, 100, 'o', color='#E74C3C', ms=12, zorder=5)

    # Distance along wall
    ax.plot([0, 0], [0, 100], '#E74C3C', lw=3, linestyle='--')
    darrow = FancyArrowPatch((0, 50), (0, 95), arrowstyle='<->', color='#E74C3C', lw=2)
    ax.add_patch(darrow)
    ax.annotate('x = 100 tan θ\n= 100', (2, 50), fontsize=12, color='#E74C3C', fontweight='bold')

    # Movement arrow on wall
    ax.arrow(0, 100, 0, 30, head_width=3, head_length=4, fc='#2ECC71', ec='#2ECC71', lw=2)
    ax.annotate('dx/dt = 400 m/min', (2, 120), fontsize=11, color='#2ECC71', fontweight='bold')

    # Distance label
    ax.plot([0, 100], [-3, -3], 'k-', lw=1)
    ax.annotate('d = 100 m', (50, -8), fontsize=11, ha='center')

    ax.set_xlim(-5, 110); ax.set_ylim(-15, 150)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Rotating Spotlight: x = d·tanθ', fontweight='bold', fontsize=14)
    save_fig(fig, '06-spotlight.png')

# ════════════════════════════════════════════════════
# 07 — Two Cars Separation (Vector Related Rates)
# ════════════════════════════════════════════════════
def fig_07_two_cars():
    fig, ax = plt.subplots(figsize=(9, 8))

    # Origin (intersection)
    ax.plot(0, 0, 'ko', ms=10, zorder=5)
    ax.annotate('intersection', (0, 0), textcoords="offset points", xytext=(8, -15), fontsize=9)

    # Car A: north at 60 km/h, after 2h
    ax.arrow(0, 0, 0, 120, head_width=5, head_length=8, fc='#E74C3C', ec='#E74C3C', lw=3, zorder=4)
    ax.plot(0, 120, 'o', color='#E74C3C', ms=10, zorder=5)
    ax.annotate('Car A\n(0, 120)\nv=60 km/h N', (0, 120), textcoords="offset points",
                xytext=(15, 5), fontsize=10, color='#E74C3C', fontweight='bold')

    # Car B: east at 80 km/h, after 2h
    ax.arrow(0, 0, 160, 0, head_width=5, head_length=8, fc='#3498DB', ec='#3498DB', lw=3, zorder=4)
    ax.plot(160, 0, 'o', color='#3498DB', ms=10, zorder=5)
    ax.annotate('Car B\n(160, 0)\nv=80 km/h E', (160, 0), textcoords="offset points",
                xytext=(5, 15), fontsize=10, color='#3498DB', fontweight='bold')

    # Distance between them
    ax.plot([0, 160], [120, 0], '#2ECC71', lw=3, linestyle='--', zorder=3)
    ax.annotate('s = 200 km\nds/dt = 100 km/h', (80, 60), fontsize=12, color='#2ECC71',
                fontweight='bold', ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # Velocity vectors (relative velocity)
    ax.arrow(80, 60, 13, -9, head_width=4, head_length=6, fc='#8E44AD', ec='#8E44AD', lw=2, zorder=5)
    ax.annotate('v_rel = (80, -60)\n|v_rel| = 100 km/h', (95, 55), fontsize=10, color='#8E44AD', fontweight='bold')

    ax.set_xlim(-20, 190); ax.set_ylim(-10, 145)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
    ax.set_title('Two Cars: Relative Velocity |v| = 100 km/h', fontweight='bold')
    ax.set_xlabel('x (km)'); ax.set_ylabel('y (km)')
    save_fig(fig, '07-two-cars.png')

# ════════════════════════════════════════════════════
# 08 — Point to Plane Distance (3D Optimization)
# ════════════════════════════════════════════════════
def fig_08_plane_distance_3d():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plane: 2x + y - z = 4  -> z = 2x + y - 4
    xx, yy = np.meshgrid(np.linspace(-1, 3, 15), np.linspace(-1, 3, 15))
    zz = 2*xx + yy - 4
    ax.plot_surface(xx, yy, zz, alpha=0.2, color='#3498DB')

    # Origin
    ax.scatter(0, 0, 0, c='black', s=80, zorder=5)
    ax.text(0, 0, 0.5, 'O', fontsize=12, fontweight='bold')

    # Closest point
    cp = np.array([4/3, 2/3, -2/3])
    ax.scatter(*cp, c='#E74C3C', s=80, zorder=5)
    ax.text(cp[0]+0.1, cp[1]+0.1, cp[2]+0.1, f'P({4/3:.2f},{2/3:.2f},{-2/3:.2f})',
            fontsize=9, color='#E74C3C')

    # Normal line from origin
    t_vals = np.linspace(0, 2/3, 50)
    ax.plot(2*t_vals, 1*t_vals, -1*t_vals, '#E74C3C', lw=3, zorder=4)

    # Normal vector
    ax.quiver(0, 0, 0, 2, 1, -1, color='#E74C3C', arrow_length_ratio=0.15, lw=2)
    ax.text(2.2, 1.2, -1.2, 'n=(2,1,-1)', fontsize=10, color='#E74C3C', fontweight='bold')

    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title('Shortest Distance to Plane: Along Normal Vector', fontweight='bold')
    ax.set_xlim(-1, 3); ax.set_ylim(-1, 3); ax.set_zlim(-3, 2)
    save_fig(fig, '08-plane-distance-3d.png')

# ════════════════════════════════════════════════════
# 09 — Cylinder Inscribed in Sphere
# ════════════════════════════════════════════════════
def fig_09_cylinder_in_sphere():
    fig, ax = plt.subplots(figsize=(8, 8))
    R = 3

    # Sphere cross-section (circle)
    theta = np.linspace(0, 2*np.pi, 300)
    ax.plot(R*np.cos(theta), R*np.sin(theta), 'b-', lw=3, zorder=3)

    # Optimal cylinder
    h_opt = R/np.sqrt(3)
    r_opt = R*np.sqrt(2/3)
    rect = Rectangle((-r_opt, -h_opt), 2*r_opt, 2*h_opt, fill=True,
                     fc='#E74C3C', alpha=0.25, ec='#E74C3C', lw=2.5)
    ax.add_patch(rect)
    ax.plot(r_opt, h_opt, 'o', color='#E74C3C', ms=10, zorder=5)
    ax.annotate(f'(r,h)=({r_opt:.2f},{h_opt:.2f})', (r_opt, h_opt),
                textcoords="offset points", xytext=(10, 10), fontsize=10,
                color='#E74C3C', fontweight='bold')

    # Labels
    ax.annotate('R', (1.2, 0.8), fontsize=13, fontweight='bold')
    ax.annotate('r', (r_opt/2, -0.25), fontsize=11, ha='center')
    ax.annotate('h', (-r_opt-0.3, h_opt/2), fontsize=11, va='center')
    ax.annotate('r²+h²=R²', (1.5, 2.5), fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    ax.annotate(f'V_max = {4*np.pi*R**3/(3*np.sqrt(3)):.1f}\n=0.577 V_sphere',
                (-2.8, 2.7), fontsize=10, ha='left',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    ax.set_aspect('equal'); ax.set_xlim(-3.8, 3.8); ax.set_ylim(-3.8, 3.8)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.2)
    ax.set_title('Cylinder Inscribed in Sphere — Max Volume', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '09-cylinder-in-sphere.png')

# ════════════════════════════════════════════════════
# 10 — Exponential Optimization: f(x)=xe^{-x}
# ════════════════════════════════════════════════════
def fig_10_exponential_optimization():
    fig, ax = plt.subplots(figsize=(9, 6))
    x = np.linspace(0, 5, 400)
    y = x * np.exp(-x)
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    ax.plot(1, 1/np.e, 'o', color='#E74C3C', ms=12, zorder=5)
    ax.axvline(1, color='#E74C3C', lw=1.5, linestyle='--', alpha=0.4)
    ax.axhline(1/np.e, color='#E74C3C', lw=1.5, linestyle='--', alpha=0.4)
    ax.annotate(f'Max: (1, 1/e≈{1/np.e:.3f})', (1, 1/np.e), textcoords="offset points",
                xytext=(30, -25), fontsize=12, color='#E74C3C', fontweight='bold')

    ax.set_xlim(0, 5); ax.set_ylim(0, 0.4)
    ax.grid(True, alpha=0.25)
    ax.set_title('f(x)=x·e^{-x} — Global Max at x=1', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('f(x)')
    save_fig(fig, '10-exponential-optimization.png')

if __name__ == '__main__':
    print("Generating 15B graphs...")
    fig_01_box_volume()
    fig_02_distance_minimization()
    fig_03_rectangle_semicircle()
    fig_04_ellipse_closest()
    fig_04_ladder_rates()
    fig_05_conical_tank()
    fig_06_spotlight()
    fig_07_two_cars()
    fig_08_plane_distance_3d()
    fig_09_cylinder_in_sphere()
    fig_10_exponential_optimization()
    print("Done! 10 graphs generated.")
