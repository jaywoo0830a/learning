#!/usr/bin/env python3
"""Generate 3D/2D/1D graphs for 15A, 15B, 17A, 17B."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

plt.rcParams.update({'font.size': 10, 'figure.dpi': 150})
OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs'

# ═══════════════════════════════════════════════════════════
# 15A-1: MVT Geometry — secant and tangent
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D: function surface with secant plane and tangent
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
x3 = np.linspace(0, 5, 100)
f3 = lambda x: x**2
ax3.plot(x3, np.zeros_like(x3), f3(x3), 'b', linewidth=2, label='f(x)=x²')
ax3.plot([1, 4], [0, 0], [1, 16], 'r-', linewidth=2.5, label='secant: avg slope=5')
ax3.plot([2.5, 2.5], [0, 0], [0, 6.25], 'g--', linewidth=1)
ax3.scatter([2.5], [0], [6.25], c='g', s=60, zorder=5)
# tangent segment at x=2.5
tx = np.linspace(2, 3, 20)
ax3.plot(tx, np.zeros_like(tx), 6.25 + 5*(tx - 2.5), 'g-', linewidth=2.5)
ax3.set_xlabel('x'); ax3.set_ylabel(''); ax3.set_zlabel('f(x)')
ax3.set_title('3D: Secant (red) & tangent (green)', fontweight='bold')
ax3.view_init(25, -50)

# 2D: classic MVT plot
ax2 = fig.add_subplot(1, 3, 2)
x2 = np.linspace(0, 5, 200)
ax2.plot(x2, f3(x2), 'b', linewidth=2.5, label='f(x)=x²')
ax2.plot([1, 4], [1, 16], 'r-', linewidth=2, label=f'secant slope = (16-1)/(4-1) = 5')
ax2.plot([2.5], [6.25], 'go', markersize=10, zorder=5)
tx2 = np.linspace(1.5, 3.5, 50)
ax2.plot(tx2, 6.25 + 5*(tx2 - 2.5), 'g--', linewidth=2, label=f'tangent at c=2.5, f\'(c)=5')
ax2.set_xlabel('x'); ax2.set_ylabel('f(x)')
ax2.set_title('2D: MVT — f\'(c) = (f(b)-f(a))/(b-a)', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D: derivative with average
ax1 = fig.add_subplot(1, 3, 3)
x1 = np.linspace(0.5, 4.5, 200)
ax1.plot(x1, 2*x1, 'b', linewidth=2, label="f'(x)=2x")
ax1.axhline(y=5, color='r', linestyle='--', linewidth=2, label='average slope = 5')
ax1.axvline(x=2.5, color='g', linestyle=':', linewidth=1.5)
ax1.plot([2.5], [5], 'go', markersize=10, zorder=5)
ax1.fill_between([1, 4], 0, 5, alpha=0.1, color='r')
ax1.set_xlabel('x'); ax1.set_ylabel("f'(x)")
ax1.set_title('1D: f\'(c) equals average slope at c=2.5', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/15a-mvt-geometry.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 15a-mvt-geometry.png')

# ═══════════════════════════════════════════════════════════
# 15A-2: Complete curve sketch — f(x)=x²/(x-1)
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 8))

x_vals = np.linspace(-2, 4, 300)
x_left = x_vals[x_vals < 0.95]
x_right = x_vals[x_vals > 1.05]

f_sk = lambda x: x**2/(x-1)

# 3D: three surfaces (f, f', f'')
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
y_pos = np.array([0, 1, 2])
for xi in x_left[::3]:
    ax3.plot([xi, xi], [0.1, 0.1], [f_sk(xi), f_sk(xi)], 'b.', alpha=0.3, markersize=1)
for xi in x_right[::3]:
    ax3.plot([xi, xi], [0.1, 0.1], [f_sk(xi), f_sk(xi)], 'b.', alpha=0.3, markersize=1)
# Simplified: just show the main branches
xl = np.linspace(-2, 0.9, 80)
xr = np.linspace(1.1, 4, 80)
ax3.plot(xl, np.ones_like(xl)*0, f_sk(xl), 'b', linewidth=2.5)
ax3.plot(xr, np.ones_like(xr)*0, f_sk(xr), 'b', linewidth=2.5)
ax3.axvline(x=1, color='r', linestyle='--', linewidth=2, alpha=0.7)
ax3.set_xlabel('x'); ax3.set_ylabel(''); ax3.set_zlabel('f(x)')
ax3.set_title('3D: f(x)=x²/(x-1) — two branches', fontweight='bold')

# 2D: full sketch with asymptotes
ax2 = fig.add_subplot(2, 3, 3)
ax2.plot(xl, f_sk(xl), 'b', linewidth=2)
ax2.plot(xr, f_sk(xr), 'b', linewidth=2)
ax2.axvline(x=1, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label='VA: x=1')
xa = np.linspace(-2, 4, 100)
ax2.plot(xa, xa + 1, 'g--', linewidth=1.5, alpha=0.7, label='slant: y=x+1')
ax2.plot([0], [0], 'ko', markersize=6, label='(0,0) max')
ax2.plot([2], [4], 'ko', markersize=6, label='(2,4) min')
ax2.set_xlim(-2, 4); ax2.set_ylim(-10, 10)
ax2.set_xlabel('x'); ax2.set_ylabel('f(x)')
ax2.set_title('2D: Full sketch with asymptotes & extrema', fontweight='bold')
ax2.legend(fontsize=7); ax2.grid(True, alpha=0.3)

# 1D: sign charts for f' and f''
ax1 = fig.add_subplot(2, 3, (4, 6))
xx = np.linspace(-2, 4, 300)
fp = lambda x: x*(x-2)/(x-1)**2
fpp = lambda x: 2/(x-1)**3

ax1b = ax1.twinx()
ax1.plot(xl, fp(xl), 'b-', linewidth=2, label="f'(x)")
ax1.plot(xr, fp(xr), 'b-', linewidth=2)
ax1b.plot(xl, fpp(xl), 'r--', linewidth=1.5, label="f''(x)")
ax1b.plot(xr, fpp(xr), 'r--', linewidth=1.5)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.set_xlim(-2, 4); ax1.set_ylim(-5, 8)
ax1b.set_ylim(-10, 10)
ax1.set_xlabel('x'); ax1.set_ylabel("f'(x) [blue]", color='b')
ax1b.set_ylabel("f''(x) [red]", color='r')
ax1.set_title('1D: f\' and f\'\' — sign changes at critical/inflection points', fontweight='bold')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, fontsize=8, loc='upper left')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/15a-complete-sketch.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 15a-complete-sketch.png')

# ═══════════════════════════════════════════════════════════
# 15A-3: Cubic analysis — f(x)=x³-3x
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 8))

xc = np.linspace(-2.5, 2.5, 300)
fc = lambda x: x**3 - 3*x
fpc = lambda x: 3*x**2 - 3
fppc = lambda x: 6*x

# 3D: f, f', f'' as stacked curves in 3D
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
ax3.plot(xc, np.ones_like(xc)*0, fc(xc), 'b', linewidth=2, label='f(x)')
ax3.plot(xc, np.ones_like(xc)*1, fpc(xc), 'g', linewidth=2, label="f'(x)")
ax3.plot(xc, np.ones_like(xc)*2, fppc(xc), 'r', linewidth=2, label="f''(x)")
ax3.scatter([-1, 1], [0, 0], [fc(-1), fc(1)], c='#e74c3c', s=80, zorder=5)
ax3.scatter([-1, 1], [1, 1], [0, 0], c='#e74c3c', s=80, zorder=5)
ax3.scatter([0], [0], [0], c='#f39c12', s=100, marker='D', zorder=5)
ax3.set_xlabel('x'); ax3.set_ylabel('layer'); ax3.set_zlabel('value')
ax3.set_title('3D: f (blue), f\' (green), f\'\' (red)', fontweight='bold')
ax3.view_init(20, -55)

# 2D: annotated graph
ax2 = fig.add_subplot(2, 3, 3)
ax2.plot(xc, fc(xc), 'b', linewidth=2.5)
ax2.plot([-1], [fc(-1)], 'ro', markersize=10, zorder=5)
ax2.plot([1], [fc(1)], 'go', markersize=10, zorder=5)
ax2.plot([0], [0], 'o', color='#f39c12', markersize=12, markeredgewidth=2, markerfacecolor='none', zorder=5)
ax2.annotate('local max\n(-1, 2)', xy=(-1, fc(-1)), xytext=(-2.2, 3.5), fontsize=9,
            arrowprops=dict(arrowstyle='->', color='#e74c3c'), color='#e74c3c', fontweight='bold')
ax2.annotate('local min\n(1, -2)', xy=(1, fc(1)), xytext=(1.3, -3.5), fontsize=9,
            arrowprops=dict(arrowstyle='->', color='#2ecc71'), color='#2ecc71', fontweight='bold')
ax2.annotate('inflection\n(0, 0)', xy=(0, 0), xytext=(0.5, 1.5), fontsize=9,
            arrowprops=dict(arrowstyle='->', color='#f39c12'), color='#f39c12', fontweight='bold')
ax2.axhline(y=0, color='gray', linewidth=0.5)
ax2.set_xlabel('x'); ax2.set_ylabel('f(x)')
ax2.set_title('2D: f(x)=x³−3x — max, min, inflection', fontweight='bold')
ax2.grid(True, alpha=0.3)

# 1D: derivative sign chart
ax1 = fig.add_subplot(2, 3, (4, 6))
ax1.plot(xc, fc(xc), 'b', linewidth=2, label='f(x)')
ax1.fill_between(xc, -5, fc(xc), where=(xc < -1), alpha=0.1, color='#2ecc71', label="f'>0 (inc)")
ax1.fill_between(xc, -5, fc(xc), where=((xc > -1) & (xc < 1)), alpha=0.1, color='#e74c3c', label="f'<0 (dec)")
ax1.fill_between(xc, -5, fc(xc), where=(xc > 1), alpha=0.1, color='#2ecc71')
ax1.fill_between(xc, -5, fc(xc), where=(xc < 0), alpha=0.05, color='gray')
# Concavity marks
ax1.annotate('concave down\nf\'\'<0', xy=(-1.3, -1), fontsize=9, style='italic')
ax1.annotate('concave up\nf\'\'>0', xy=(1.3, -1), fontsize=9, style='italic')
ax1.set_xlabel('x'); ax1.set_ylabel('f(x)')
ax1.set_title('1D: Increasing/decreasing intervals + concavity', fontweight='bold')
ax1.legend(fontsize=8, loc='lower right'); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/15a-cubic-analysis.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 15a-cubic-analysis.png')

# ═══════════════════════════════════════════════════════════
# 15B-1: Box volume optimization
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 8))

# 3D: V(x) surface + box visualization
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
# Draw a wireframe box at x=2
def draw_box(ax, x, offset_x=0, alpha=0.8):
    s = 12 - 2*x
    verts = np.array([[0,0,0],[s,0,0],[s,s,0],[0,s,0],[0,0,s],[s,0,s],[s,s,s],[0,s,s]]) + np.array([offset_x, 0, 0])
    edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
    for e in edges:
        ax.plot3D(*zip(verts[e[0]], verts[e[1]]), 'k-', linewidth=1, alpha=alpha)
draw_box(ax3, 2.0, offset_x=-2)

x_box = np.linspace(0.2, 5.8, 100)
V = lambda x: x*(12-2*x)**2
ax3.plot(x_box, np.ones_like(x_box)*(-3), V(x_box), 'b', linewidth=2.5)
ax3.scatter([2], [-3], [128], c='r', s=100, zorder=5)
ax3.set_xlabel('x'); ax3.set_ylabel(''); ax3.set_zlabel('V(x)')
ax3.set_title('3D: Box (at x=2) + V(x) curve', fontweight='bold')
ax3.view_init(25, -60)

# 2D: V(x) curve with max
ax2 = fig.add_subplot(2, 3, 3)
ax2.plot(x_box, V(x_box), 'b', linewidth=2.5)
ax2.plot([2], [128], 'ro', markersize=10, zorder=5)
ax2.axvline(x=2, color='r', linestyle=':', alpha=0.5)
ax2.axhline(y=128, color='r', linestyle=':', alpha=0.5)
ax2.annotate('MAX: x=2\nV=128', xy=(2, 128), xytext=(3.5, 140), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='r'), fontweight='bold', color='r')
ax2.set_xlabel('x (cut size)'); ax2.set_ylabel('V(x)')
ax2.set_title('2D: V(x)=x(12-2x)² — max at x=2', fontweight='bold')
ax2.grid(True, alpha=0.3)

# 1D: V'(x) sign
ax1 = fig.add_subplot(2, 3, (4, 6))
Vp = lambda x: 12*(6-x)*(2-x)  # simplified derivative
ax1.plot(x_box, Vp(x_box), 'g', linewidth=2)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.fill_between(x_box, Vp(x_box), 0, where=(x_box<2), alpha=0.15, color='#2ecc71', label="V'>0 (increasing)")
ax1.fill_between(x_box, Vp(x_box), 0, where=(x_box>2), alpha=0.15, color='#e74c3c', label="V'<0 (decreasing)")
ax1.plot([2], [0], 'ro', markersize=10, zorder=5)
ax1.set_xlabel('x'); ax1.set_ylabel("V'(x)")
ax1.set_title("1D: V'(x) — positive before x=2, negative after → MAX", fontweight='bold')
ax1.legend(fontsize=9); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/15b-box-optimization.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 15b-box-optimization.png')

# ═══════════════════════════════════════════════════════════
# 15B-2: Ladder related rates
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D: ladder sliding with time axis
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
t_vals = np.linspace(0, 3, 4)
for i, t in enumerate(t_vals):
    x_pos = 1 + t  # bottom slides at 1 m/s from x=1
    y_pos = np.sqrt(25 - x_pos**2) if x_pos <= 5 else 0
    ax3.plot([x_pos, 0], [0, y_pos], [t, t], 'b-', linewidth=2+0.5*i, alpha=0.4+0.15*i)
    ax3.scatter([x_pos], [0], [t], c='r', s=30)
    ax3.scatter([0], [y_pos], [t], c='g', s=30)
ax3.set_xlabel('x (m)'); ax3.set_ylabel('y (m)'); ax3.set_zlabel('t (s)')
ax3.set_title('3D: Ladder sliding over time', fontweight='bold')

# 2D: geometry with rates
ax2 = fig.add_subplot(1, 3, 2)
# Draw ladder at x=3
ax2.plot([3, 0], [0, 4], 'b-', linewidth=4)
ax2.plot([3], [0], 'ro', markersize=8, label='bottom: dx/dt=1 m/s →')
ax2.plot([0], [4], 'go', markersize=8, label='top: dy/dt=−3/4 m/s ↓')
ax2.plot([0, 3], [0, 0], 'k-', linewidth=1)
ax2.plot([0, 0], [0, 4], 'k-', linewidth=1)
ax2.annotate('x=3', xy=(1.5, -0.3), fontsize=10, ha='center')
ax2.annotate('y=4', xy=(-0.5, 2), fontsize=10, ha='center')
ax2.annotate('5 m', xy=(1.2, 2.2), fontsize=10, rotation=-53, color='b')
# rate arrows
ax2.arrow(3, -0.5, 0.6, 0, head_width=0.2, head_length=0.15, fc='r', ec='r')
ax2.arrow(-0.5, 4, 0, -0.6, head_width=0.15, head_length=0.2, fc='g', ec='g')
ax2.set_xlim(-0.5, 5.5); ax2.set_ylim(-0.5, 5)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: x²+y²=25 → 2x·dx/dt+2y·dy/dt=0', fontweight='bold')
ax2.set_aspect('equal'); ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D: dy/dt as function of x
ax1 = fig.add_subplot(1, 3, 3)
xx_lad = np.linspace(0.5, 4.9, 200)
dy_dt = -xx_lad / np.sqrt(25 - xx_lad**2)
ax1.plot(xx_lad, dy_dt, 'g', linewidth=2.5)
ax1.plot([3], [-0.75], 'ro', markersize=10, zorder=5)
ax1.axhline(y=0, color='gray', linewidth=0.5)
ax1.fill_between(xx_lad, dy_dt, 0, alpha=0.1, color='g')
ax1.annotate('at x=3: dy/dt=−0.75 m/s', xy=(3, -0.75), xytext=(3.5, -3),
            arrowprops=dict(arrowstyle='->'), fontsize=9, fontweight='bold')
ax1.set_xlabel('x (m)'); ax1.set_ylabel('dy/dt (m/s)')
ax1.set_title('1D: Top speed vs bottom position', fontweight='bold')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/15b-ladder-rates.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 15b-ladder-rates.png')

# ═══════════════════════════════════════════════════════════
# 15B-3: Conical tank related rates
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D: cone with water level
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
theta = np.linspace(0, 2*np.pi, 40)
h_level = 1.0
r_level = 0.4 * h_level
# Full cone wireframe
for hh in [5.0]:
    rr = 0.4 * hh
    z_cone = np.linspace(0, hh, 10)
    for zz in z_cone:
        rzz = rr * (1 - zz/hh)
        ax3.plot(rzz*np.cos(theta), rzz*np.sin(theta), np.full_like(theta, zz), 'b-', linewidth=0.5, alpha=0.3)
# Water cone
z_water = np.linspace(0, h_level, 6)
for zz in z_water:
    rzz = r_level * (1 - zz/h_level)
    ax3.plot(rzz*np.cos(theta), rzz*np.sin(theta), np.full_like(theta, zz), '#3498db', linewidth=1.5)
# Fill water volume
r_fill = np.linspace(0, r_level, 20)
for rr in r_fill[::2]:
    z_top = h_level * (1 - rr/r_level)
    ax3.plot(rr*np.cos(theta), rr*np.sin(theta), np.full_like(theta, z_top), '#3498db', linewidth=0.3, alpha=0.5)
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z (height)')
ax3.set_title(f'3D: Conical tank — water at h={h_level}m', fontweight='bold')

# 2D: cross-section with similar triangles
ax2 = fig.add_subplot(1, 3, 2)
# Triangle
ax2.plot([-2, 0, 2, -2], [0, 5, 0, 0], 'b-', linewidth=2)
ax2.plot([-0.4, 0, 0.4, -0.4], [0, 1, 0, 0], '#3498db', linewidth=2)
ax2.fill_between([-0.4, 0.4], [0, 0], [1, 1], alpha=0.3, color='#3498db')
ax2.annotate('r=0.4h', xy=(0.3, 2.5), fontsize=10, color='b')
ax2.annotate('R=2, H=5', xy=(0.8, 4.2), fontsize=9, color='b')
ax2.annotate('r/h = R/H = 2/5', xy=(0.2, 1.5), fontsize=10, fontweight='bold', color='#2980b9')
ax2.arrow(0.5, 1.0, 0, 0.8, head_width=0.08, head_length=0.15, fc='#3498db', ec='#3498db')
ax2.set_xlim(-2.5, 2.5); ax2.set_ylim(-0.5, 5.5)
ax2.set_xlabel('radius'); ax2.set_ylabel('height')
ax2.set_title('2D: Similar triangles → r=0.4h', fontweight='bold')
ax2.set_aspect('equal'); ax2.grid(True, alpha=0.3)

# 1D: dh/dt vs h
ax1 = fig.add_subplot(1, 3, 3)
h_vals = np.linspace(0.2, 5, 200)
dh_dt = 3 / (0.16 * np.pi * h_vals**2)  # from dV/dt = 0.16π h² dh/dt = 3
ax1.plot(h_vals, dh_dt, '#e74c3c', linewidth=2.5)
ax1.plot([1], [3/(0.16*np.pi)], 'ko', markersize=10, zorder=5)
ax1.annotate(f'at h=1: dh/dt≈5.97 m/min', xy=(1, 3/(0.16*np.pi)),
            xytext=(2.5, 20), arrowprops=dict(arrowstyle='->'),
            fontsize=9, fontweight='bold')
ax1.fill_between(h_vals, dh_dt, 0, alpha=0.1, color='#e74c3c')
ax1.set_xlabel('h (m)'); ax1.set_ylabel('dh/dt (m/min)')
ax1.set_title('1D: Water rise rate — slows as tank fills', fontweight='bold')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/15b-conical-tank.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 15b-conical-tank.png')

# ═══════════════════════════════════════════════════════════
# 17A-1: Disk method — y=√x rotated about x-axis
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D: solid of revolution wireframe
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
theta_d = np.linspace(0, 2*np.pi, 50)
x_disk_pts = np.linspace(0.2, 3.8, 8)
for xd in x_disk_pts:
    r = np.sqrt(xd)
    ax3.plot(np.full_like(theta_d, xd), r*np.cos(theta_d), r*np.sin(theta_d), 'b-', linewidth=0.6, alpha=0.6)
# Meridian lines
for th in [0, np.pi/2, np.pi, 3*np.pi/2]:
    ax3.plot(x_disk_pts, np.sqrt(x_disk_pts)*np.cos(th), np.sqrt(x_disk_pts)*np.sin(th), 'b-', linewidth=1.5)
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.set_title('3D: Solid — y=√x rotated about x-axis', fontweight='bold')

# 2D: cross-section with disk
ax2 = fig.add_subplot(1, 3, 2)
x2d = np.linspace(0, 4, 200)
ax2.fill_between(x2d, np.sqrt(x2d), -np.sqrt(x2d), alpha=0.3, color='b')
ax2.plot(x2d, np.sqrt(x2d), 'b', linewidth=2)
ax2.plot(x2d, -np.sqrt(x2d), 'b', linewidth=2)
# Highlight one disk at x=2
ax2.plot([2, 2], [-np.sqrt(2), np.sqrt(2)], 'r-', linewidth=3, label=f'disk at x=2: R=√2')
ax2.annotate(f'A=π(√2)²=2π', xy=(2, 0), fontsize=9, ha='center')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: Cross-section — each disk has area π[R(x)]²', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D: R(x)² and cumulative volume
ax1 = fig.add_subplot(1, 3, 3)
ax1.fill_between(x2d, 0, x2d, alpha=0.3, color='b', label='[R(x)]² = x')
ax1.plot(x2d, x2d, 'b', linewidth=2)
V_cum = np.pi * x2d**2 / 2
ax1b = ax1.twinx()
ax1b.plot(x2d, V_cum, 'r--', linewidth=2, label='V(x) = πx²/2')
ax1.set_xlabel('x'); ax1.set_ylabel('[R(x)]²', color='b')
ax1b.set_ylabel('V(x)', color='r')
ax1.set_title('1D: [R(x)]² and accumulating volume V(x)', fontweight='bold')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, fontsize=8, loc='upper left')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/17a-disk-method-3d.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 17a-disk-method-3d.png')

# ═══════════════════════════════════════════════════════════
# 17A-2: Washer method — region between y=x, y=x² rotated
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
theta_w = np.linspace(0, 2*np.pi, 50)
x_washer = np.linspace(0.1, 0.9, 8)
for xw in x_washer:
    r_outer = xw
    r_inner = xw**2
    ax3.plot(np.full_like(theta_w, xw), r_outer*np.cos(theta_w), r_outer*np.sin(theta_w), 'b-', linewidth=0.6, alpha=0.6)
    ax3.plot(np.full_like(theta_w, xw), r_inner*np.cos(theta_w), r_inner*np.sin(theta_w), 'r-', linewidth=0.6, alpha=0.6)
for th in [0, np.pi]:
    ax3.plot(x_washer, x_washer*np.cos(th), x_washer*np.sin(th), 'b-', linewidth=1.5)
    ax3.plot(x_washer, x_washer**2*np.cos(th), x_washer**2*np.sin(th), 'r-', linewidth=1.5)
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.set_title('3D: Hollow solid — outer R=x, inner r=x²', fontweight='bold')

# 2D
ax2 = fig.add_subplot(1, 3, 2)
x2w = np.linspace(0, 1, 200)
ax2.fill_between(x2w, x2w, x2w**2, alpha=0.3, color='b')
ax2.plot(x2w, x2w, 'b', linewidth=2, label='y=x (outer)')
ax2.plot(x2w, x2w**2, 'r', linewidth=2, label='y=x² (inner)')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: Region between curves → hollow when rotated', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D
ax1 = fig.add_subplot(1, 3, 3)
ax1.fill_between(x2w, 0, x2w**2 - x2w**4, alpha=0.3, color='b')
ax1.plot(x2w, x2w**2, 'b', linewidth=2, label='R² = x²')
ax1.plot(x2w, x2w**4, 'r', linewidth=2, label='r² = x⁴')
ax1.fill_between(x2w, x2w**4, x2w**2, alpha=0.2, color='#9b59b6', label='R²−r² = x²−x⁴')
ax1.set_xlabel('x'); ax1.set_ylabel('R², r²')
ax1.set_title('1D: Washer area π(R²−r²) = π(x²−x⁴)', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/17a-washer-method-3d.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 17a-washer-method-3d.png')

# ═══════════════════════════════════════════════════════════
# 17A-3: Shell method — y=x² rotated about y-axis
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D: nested cylindrical shells
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
theta_s = np.linspace(0, 2*np.pi, 60)
x_shells = np.linspace(0.3, 2.0, 6)
z_top = np.linspace(0, 4, 20)
for xs in x_shells:
    h = xs**2
    for zz in [0, h]:
        ax3.plot(xs*np.cos(theta_s), xs*np.sin(theta_s), np.full_like(theta_s, zz), 'g-', linewidth=0.8, alpha=0.7)
    for th in np.linspace(0, 2*np.pi, 12):
        ax3.plot([xs*np.cos(th), xs*np.cos(th)], [xs*np.sin(th), xs*np.sin(th)], [0, h], 'g-', linewidth=0.4, alpha=0.5)
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.set_title('3D: Nested cylindrical shells', fontweight='bold')

# 2D: unwrapped shell
ax2 = fig.add_subplot(1, 3, 2)
xs_demo = 1.5
h_demo = xs_demo**2
circum = 2*np.pi*xs_demo
# Show the region and one shell
x2s = np.linspace(0, 2, 200)
ax2.fill_between(x2s, 0, x2s**2, alpha=0.3, color='g')
ax2.plot(x2s, x2s**2, 'g', linewidth=2)
ax2.axvline(x=xs_demo, color='r', linestyle='--', linewidth=1.5, alpha=0.7)
ax2.annotate(f'shell at x={xs_demo}\nheight={h_demo:.2f}\ncircumference={circum:.2f}',
            xy=(xs_demo, h_demo/2), xytext=(0.5, 3.5), fontsize=8,
            arrowprops=dict(arrowstyle='->'), fontweight='bold')
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: Region + one shell highlighted', fontweight='bold')
ax2.grid(True, alpha=0.3)

# 1D: x*h(x)
ax1 = fig.add_subplot(1, 3, 3)
ax1.fill_between(x2s, 0, x2s * x2s**2, alpha=0.3, color='g')
ax1.plot(x2s, x2s**3, 'g', linewidth=2, label='x·h(x) = x³')
V_shell = 2*np.pi * x2s**4 / 4
ax1b = ax1.twinx()
ax1b.plot(x2s, V_shell, 'r--', linewidth=2, label='V(x) = 2πx⁴/4')
ax1.set_xlabel('x'); ax1.set_ylabel('x·h(x)', color='g')
ax1b.set_ylabel('V(x)', color='r')
ax1.set_title('1D: Shell volume = 2π∫x·h(x)dx', fontweight='bold')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1b.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, fontsize=8, loc='upper left')
ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/17a-shell-method-3d.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 17a-shell-method-3d.png')

# ═══════════════════════════════════════════════════════════
# 17B-1: Arc length — polygonal approximation
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

x_al = np.linspace(0, 4, 300)
f_al = lambda x: x**(1.5)
fp_al = lambda x: 1.5 * np.sqrt(x)

# 3D: curve with piecewise segments lifting to arc length
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
n_segs = np.array([2, 4, 8, 16])
for i, n in enumerate(n_segs):
    x_seg = np.linspace(0, 4, n+1)
    y_seg = f_al(x_seg)
    z_offset = i * 3
    for j in range(n):
        ax3.plot([x_seg[j], x_seg[j+1]], [z_offset, z_offset], [y_seg[j], y_seg[j+1]],
                '-', linewidth=2-0.1*i, alpha=0.8, color=plt.cm.viridis(i/len(n_segs)))
    ax3.text(4.2, z_offset, f_al(4), f'n={n}', fontsize=8)
ax3.plot(x_al, np.ones_like(x_al)*(-1.5), f_al(x_al), 'k-', linewidth=2.5, label='true curve')
ax3.set_xlabel('x'); ax3.set_ylabel('approximation level'); ax3.set_zlabel('y')
ax3.set_title('3D: Polygonal approximations → arc length', fontweight='bold')

# 2D: curve + segments
ax2 = fig.add_subplot(1, 3, 2)
n_show = 6
x_s = np.linspace(0, 4, n_show+1)
y_s = f_al(x_s)
ax2.plot(x_al, f_al(x_al), 'k-', linewidth=2.5, label=f'y=x^(3/2)')
for j in range(n_show):
    ax2.plot([x_s[j], x_s[j+1]], [y_s[j], y_s[j+1]], 'r-', linewidth=1.5, alpha=0.8)
    ax2.plot([x_s[j], x_s[j+1]], [y_s[j], y_s[j]], 'r:', linewidth=0.5, alpha=0.4)
    ax2.plot([x_s[j+1], x_s[j+1]], [y_s[j], y_s[j+1]], 'r:', linewidth=0.5, alpha=0.4)
ax2.plot(x_s, y_s, 'ro', markersize=5)
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: ΔL ≈ √(Δx²+Δy²) = √(1+(Δy/Δx)²)Δx', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D: integrand √(1+(f')²)
ax1 = fig.add_subplot(1, 3, 3)
integrand = np.sqrt(1 + fp_al(x_al)**2)
ax1.fill_between(x_al, 0, integrand, alpha=0.3, color='b')
ax1.plot(x_al, integrand, 'b', linewidth=2.5, label='√(1+(f\')²)')
L_approx = np.trapz(integrand, x_al)
ax1.text(2.5, 5, f'L = ∫₀⁴ √(1+(1.5√x)²)dx ≈ {L_approx:.2f}', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
ax1.set_xlabel('x'); ax1.set_ylabel('√(1+(dy/dx)²)')
ax1.set_title('1D: Arc length = area under √(1+(f\')²)', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/17b-arc-length-approx.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 17b-arc-length-approx.png')

# ═══════════════════════════════════════════════════════════
# 17B-2: Surface of revolution
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 6))

# 3D: surface
ax3 = fig.add_subplot(1, 3, 1, projection='3d')
theta_sr = np.linspace(0, 2*np.pi, 60)
x_sr = np.linspace(0.2, 3.8, 30)
Xsr, Tsr = np.meshgrid(x_sr, theta_sr)
R_sr = np.sqrt(Xsr)
Ysr = R_sr * np.cos(Tsr)
Zsr = R_sr * np.sin(Tsr)
ax3.plot_surface(Xsr, Ysr, Zsr, cmap='Blues', alpha=0.6, edgecolor='none')
# Highlight one band
for th in np.linspace(0, 2*np.pi, 8):
    ax3.plot([2, 2], [np.sqrt(2)*np.cos(th), np.sqrt(2)*np.cos(th)],
             [np.sqrt(2)*np.sin(th), np.sqrt(2)*np.sin(th)], 'r-', linewidth=0.5)
ax3.set_xlabel('x'); ax3.set_ylabel('y'); ax3.set_zlabel('z')
ax3.set_title('3D: Surface — y=√x rotated about x-axis', fontweight='bold')

# 2D: band element
ax2 = fig.add_subplot(1, 3, 2)
x_sb = np.linspace(0.2, 3.8, 200)
ax2.plot(x_sb, np.sqrt(x_sb), 'b', linewidth=2.5)
# Show a band at x=2
ax2.fill_between([1.7, 2.3], [np.sqrt(1.7), np.sqrt(2.3)], alpha=0.3, color='r')
ax2.annotate('band: radius y, slant width ds', xy=(2, np.sqrt(2)),
            xytext=(2.5, 2.5), fontsize=10, arrowprops=dict(arrowstyle='->'), fontweight='bold')
ax2.annotate('dS = 2πy·ds\n   = 2πy·√(1+(y\')²)dx', xy=(1, 1.5), fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
ax2.set_xlabel('x'); ax2.set_ylabel('y')
ax2.set_title('2D: Surface area band = circumference × slant width', fontweight='bold')
ax2.grid(True, alpha=0.3)

# 1D: integrand
ax1 = fig.add_subplot(1, 3, 3)
integrand_s = 2*np.pi * np.sqrt(x_sb) * np.sqrt(1 + (1/(2*np.sqrt(x_sb)))**2)
ax1.fill_between(x_sb, 0, integrand_s, alpha=0.3, color='r')
ax1.plot(x_sb, integrand_s, 'r', linewidth=2.5, label='2πy√(1+(y\')²)')
S_approx = np.trapz(integrand_s, x_sb)
ax1.text(2, 8, f'S = 2π∫₀⁴ y√(1+(y\')²)dx ≈ {S_approx:.1f}', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
ax1.set_xlabel('x'); ax1.set_ylabel('2πy√(1+(y\')²)')
ax1.set_title('1D: Surface area = area under integrand', fontweight='bold')
ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/17b-surface-revolution.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 17b-surface-revolution.png')

# ═══════════════════════════════════════════════════════════
# 17B-3: Improper integrals — p-test comparison
# ═══════════════════════════════════════════════════════════
fig = plt.figure(figsize=(18, 8))

# 3D: area extending to infinity
ax3 = fig.add_subplot(2, 3, (1, 2), projection='3d')
x_inf = np.linspace(1, 8, 200)
f_inf = 1/x_inf**2
ax3.plot(x_inf, np.zeros_like(x_inf), f_inf, 'b', linewidth=2.5)
# Fill area
for i in range(0, len(x_inf)-1, 3):
    ax3.plot([x_inf[i], x_inf[i]], [0, 0], [0, f_inf[i]], 'b-', linewidth=0.3, alpha=0.5)
ax3.set_xlabel('x'); ax3.set_ylabel(''); ax3.set_zlabel('1/x²')
ax3.set_title('3D: ∫₁^∞ 1/x² dx — area extends to infinity but total is FINITE (=1)', fontweight='bold')
ax3.view_init(30, -60)

# 2D: 1/x² vs 1/x
ax2 = fig.add_subplot(2, 3, 3)
x_comp = np.linspace(1, 10, 300)
ax2.fill_between(x_comp, 0, 1/x_comp**2, alpha=0.4, color='#2ecc71', label='1/x²: converges (p=2>1)')
ax2.plot(x_comp, 1/x_comp**2, '#2ecc71', linewidth=2)
ax2.fill_between(x_comp, 0, 1/x_comp, alpha=0.2, color='#e74c3c', label='1/x: diverges (p=1)')
ax2.plot(x_comp, 1/x_comp, '#e74c3c', linewidth=2)
ax2.set_xlim(1, 10); ax2.set_ylim(0, 1.2)
ax2.set_xlabel('x'); ax2.set_ylabel('f(x)')
ax2.set_title('2D: 1/x² (converges) vs 1/x (diverges)', fontweight='bold')
ax2.legend(fontsize=8); ax2.grid(True, alpha=0.3)

# 1D: p-test boundary + cumulative area
ax1 = fig.add_subplot(2, 3, (4, 6))
p_vals = np.linspace(0.5, 3, 200)
# Numerical approximations for ∫₁^∞ 1/x^p dx
cum_areas = []
for p in p_vals:
    if p > 1:
        cum_areas.append(1/(p-1))
    else:
        cum_areas.append(np.nan)
ax1.plot(p_vals, cum_areas, 'b', linewidth=2.5)
ax1.axvline(x=1, color='r', linestyle='--', linewidth=2, alpha=0.7, label='p=1: boundary')
ax1.fill_between(p_vals, 0, np.array(cum_areas), alpha=0.2, color='b')
ax1.annotate('CONVERGES\n(p>1)', xy=(2, 1), fontsize=12, ha='center', fontweight='bold', color='#2ecc71')
ax1.annotate('DIVERGES\n(p≤1)', xy=(0.75, 2), fontsize=12, ha='center', fontweight='bold', color='#e74c3c')
ax1.set_xlabel('p'); ax1.set_ylabel('∫₁^∞ 1/x^p dx')
ax1.set_title('1D: p-test — ∫₁^∞ 1/x^p dx = 1/(p-1) for p>1, diverges for p≤1', fontweight='bold')
ax1.legend(fontsize=9); ax1.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/17b-improper-integrals.png', bbox_inches='tight', dpi=150)
plt.close()
print('✓ 17b-improper-integrals.png')

print('\n=== All 12 graphs generated! ===')
