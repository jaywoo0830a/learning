"""
Generate visual graphs for Session 11A: Trigonometry Foundations.
PRINCIPLE: graphs are visual, text belongs in markdown.
Only essential geometric labels. No titles, no formula boxes.
Black-and-white optimized: distinct line styles, marker shapes.
Overwrites existing 11A graph files with clean, text-minimal versions.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True
rcParams['font.size'] = 13

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'
DPI = 180

# ================================================================
# 11a: Unit Circle — Special Angles (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(9, 9))

circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(circle)

# Special angles in radians with their (cos, sin) coordinates
specials = [
    (0,           r'$0$',         (1, 0),      'SE'),
    (np.pi/6,     r'$\pi/6$',     (np.sqrt(3)/2, 0.5),    'NE'),
    (np.pi/4,     r'$\pi/4$',     (np.sqrt(2)/2, np.sqrt(2)/2), 'NE'),
    (np.pi/3,     r'$\pi/3$',     (0.5, np.sqrt(3)/2),    'NE'),
    (np.pi/2,     r'$\pi/2$',     (0, 1),      'NW'),
    (2*np.pi/3,   r'$2\pi/3$',    (-0.5, np.sqrt(3)/2),   'NW'),
    (3*np.pi/4,   r'$3\pi/4$',    (-np.sqrt(2)/2, np.sqrt(2)/2), 'NW'),
    (5*np.pi/6,   r'$5\pi/6$',    (-np.sqrt(3)/2, 0.5),   'NW'),
    (np.pi,       r'$\pi$',       (-1, 0),     'SW'),
    (7*np.pi/6,   r'$7\pi/6$',    (-np.sqrt(3)/2, -0.5),  'SW'),
    (5*np.pi/4,   r'$5\pi/4$',    (-np.sqrt(2)/2, -np.sqrt(2)/2), 'SW'),
    (4*np.pi/3,   r'$4\pi/3$',    (-0.5, -np.sqrt(3)/2),  'SW'),
    (3*np.pi/2,   r'$3\pi/2$',    (0, -1),     'SE'),
    (5*np.pi/3,   r'$5\pi/3$',    (0.5, -np.sqrt(3)/2),   'SE'),
    (7*np.pi/4,   r'$7\pi/4$',    (np.sqrt(2)/2, -np.sqrt(2)/2), 'SE'),
    (11*np.pi/6,  r'$11\pi/6$',   (np.sqrt(3)/2, -0.5),   'SE'),
]

for ang, lab, (cx, cy), pos in specials:
    px, py = np.cos(ang), np.sin(ang)
    ax.plot([0, px], [0, py], 'k-', linewidth=0.6, alpha=0.3)
    ax.scatter([px], [py], s=50, facecolors='white', edgecolors='black', linewidths=1.5, zorder=5)
    # coordinate label
    if pos == 'NE':
        ax.text(px+0.08, py+0.08, f'({cx:.2f}, {cy:.2f})', fontsize=7, ha='left', va='bottom', alpha=0.7)
    elif pos == 'NW':
        ax.text(px-0.08, py+0.08, f'({cx:.2f}, {cy:.2f})', fontsize=7, ha='right', va='bottom', alpha=0.7)
    elif pos == 'SW':
        ax.text(px-0.08, py-0.08, f'({cx:.2f}, {cy:.2f})', fontsize=7, ha='right', va='top', alpha=0.7)
    elif pos == 'SE':
        ax.text(px+0.08, py-0.08, f'({cx:.2f}, {cy:.2f})', fontsize=7, ha='left', va='top', alpha=0.7)

# Key angle labels
key_angles = [np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6,
              np.pi, 7*np.pi/6, 5*np.pi/4, 4*np.pi/3, 3*np.pi/2, 5*np.pi/3, 7*np.pi/4, 11*np.pi/6]
key_labels = [r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$',
              r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{4}$', r'$\frac{5\pi}{6}$',
              r'$\pi$', r'$\frac{7\pi}{6}$', r'$\frac{5\pi}{4}$', r'$\frac{4\pi}{3}$',
              r'$\frac{3\pi}{2}$', r'$\frac{5\pi}{3}$', r'$\frac{7\pi}{4}$', r'$\frac{11\pi}{6}$']
for ang, lab in zip(key_angles, key_labels):
    r_label = 1.18
    ax.text(r_label*np.cos(ang), r_label*np.sin(ang), lab, fontsize=8, ha='center', va='center', alpha=0.6)

# Axes
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.text(1.05, -0.08, '1', fontsize=10)
ax.text(-0.12, 1.05, '1', fontsize=10)
ax.text(-0.12, -0.12, '0', fontsize=10)

# Quadrant labels
ax.text(0.55, 0.55, 'I', fontsize=16, fontweight='bold', alpha=0.2, ha='center', va='center')
ax.text(-0.55, 0.55, 'II', fontsize=16, fontweight='bold', alpha=0.2, ha='center', va='center')
ax.text(-0.55, -0.55, 'III', fontsize=16, fontweight='bold', alpha=0.2, ha='center', va='center')
ax.text(0.55, -0.55, 'IV', fontsize=16, fontweight='bold', alpha=0.2, ha='center', va='center')

ax.set_aspect('equal')
ax.set_xlim(-1.35, 1.35)
ax.set_ylim(-1.35, 1.35)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.3)
plt.savefig(OUT + '11a-unit-circle.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11a-unit-circle done")

# ================================================================
# 11f: Unwrapping Circle → Sine Wave (text-minimal)
# ================================================================
fig = plt.figure(figsize=(14, 6))

# Left: Unit circle
ax1 = fig.add_subplot(1, 2, 1)
circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax1.add_patch(circle)

theta_demo = np.radians(55)
px, py = np.cos(theta_demo), np.sin(theta_demo)

ax1.plot([0, px], [0, py], 'k-', linewidth=2.5)
ax1.scatter([px], [py], s=100, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)
# Height indicator
ax1.plot([px, px], [0, py], 'k--', linewidth=1.5)
ax1.plot([-1.1, 1.1], [py, py], 'k:', linewidth=0.8, alpha=0.4)

arc = np.linspace(0, theta_demo, 40)
ax1.plot(0.35*np.cos(arc), 0.35*np.sin(arc), 'k-', linewidth=1.5)
ax1.text(0.42, 0.22, r'$\theta$', fontsize=14)

ax1.text(px/2-0.1, py/2+0.1, '1', fontsize=11)
ax1.text(px+0.12, py/2, r'$\sin\theta$', fontsize=12, va='center')

ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_aspect('equal')
ax1.set_xlim(-1.3, 1.3)
ax1.set_ylim(-1.3, 1.3)
for spine in ['top', 'right', 'bottom', 'left']:
    ax1.spines[spine].set_visible(False)
ax1.set_xticks([])
ax1.set_yticks([])

# Arrow from circle to wave
ax1.annotate('', xy=(1.4, 0), xytext=(1.1, 0),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))

# Right: Sine wave
ax2 = fig.add_subplot(1, 2, 2)
x = np.linspace(0, 2*np.pi, 500)
ax2.plot(x, np.sin(x), 'k-', linewidth=2.5)
ax2.axhline(py, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax2.axvline(theta_demo, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax2.scatter([theta_demo], [py], s=100, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)

ax2.axhline(0, color='black', linewidth=0.5)
ax2.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax2.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=11)
ax2.set_ylim(-1.3, 1.3)
ax2.set_yticks([-1, 0, 1])
ax2.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax2.spines[spine].set_visible(False)

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11f-unwrapping-circle.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11f-unwrapping-circle done")

# ================================================================
# 11g1, 11g2, 11g3: Reference Angles Q2, Q3, Q4 (text-minimal)
# ================================================================
def draw_reference_angle(ax, theta_deg, quad_label):
    """Draw a unit circle with angle theta and its reference angle."""
    theta = np.radians(theta_deg)
    px, py = np.cos(theta), np.sin(theta)

    circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)

    # Terminal side
    ax.plot([0, px], [0, py], 'k-', linewidth=2.5)
    ax.scatter([px], [py], s=80, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)

    # Reference angle — acute angle to x-axis
    if quad_label == 'II':
        ref_ang = np.pi - theta
        arc_full = np.linspace(0, theta, 50)
        arc_ref = np.linspace(theta, np.pi, 40)
        ax.plot(0.25*np.cos(arc_full), 0.25*np.sin(arc_full), 'k-', linewidth=1)
        ax.plot(0.45*np.cos(arc_ref), 0.45*np.sin(arc_ref), 'k--', linewidth=2)
        ax.text(0.35, 0.15, r'$\theta$', fontsize=12)
        ax.text(-0.35, 0.55, r'$\theta_R$', fontsize=13, fontweight='bold')
        # Dashed line to x-axis
        ax.plot([px, -1], [py, 0], 'k:', linewidth=1, alpha=0.5)
    elif quad_label == 'III':
        ref_ang = theta - np.pi
        arc_full = np.linspace(0, theta, 60)
        arc_ref = np.linspace(np.pi, theta, 40)
        ax.plot(0.25*np.cos(arc_full), 0.25*np.sin(arc_full), 'k-', linewidth=1)
        ax.plot(0.45*np.cos(arc_ref), 0.45*np.sin(arc_ref), 'k--', linewidth=2)
        ax.text(0.2, -0.22, r'$\theta$', fontsize=12)
        ax.text(-0.4, -0.32, r'$\theta_R$', fontsize=13, fontweight='bold')
        ax.plot([px, -1], [py, 0], 'k:', linewidth=1, alpha=0.5)
    else:  # IV
        ref_ang = 2*np.pi - theta
        arc_full = np.linspace(0, theta, 70)
        arc_ref = np.linspace(theta, 2*np.pi, 40)
        ax.plot(0.25*np.cos(arc_full), 0.25*np.sin(arc_full), 'k-', linewidth=1)
        ax.plot(0.45*np.cos(arc_ref), 0.45*np.sin(arc_ref), 'k--', linewidth=2)
        ax.text(0.22, -0.18, r'$\theta$', fontsize=12)
        ax.text(0.55, -0.32, r'$\theta_R$', fontsize=13, fontweight='bold')
        ax.plot([px, 1], [py, 0], 'k:', linewidth=1, alpha=0.5)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect('equal')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

# Q2: 150°
fig, ax = plt.subplots(figsize=(6, 6))
draw_reference_angle(ax, 150, 'II')
plt.tight_layout(pad=0.3)
plt.savefig(OUT + '11g1-reference-angle-q2.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11g1 done")

# Q3: 210°
fig, ax = plt.subplots(figsize=(6, 6))
draw_reference_angle(ax, 210, 'III')
plt.tight_layout(pad=0.3)
plt.savefig(OUT + '11g2-reference-angle-q3.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11g2 done")

# Q4: 300° (or 330°)
fig, ax = plt.subplots(figsize=(6, 6))
draw_reference_angle(ax, 300, 'IV')
plt.tight_layout(pad=0.3)
plt.savefig(OUT + '11g3-reference-angle-q4.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11g3 done")

# ================================================================
# 11b: sin, cos, tan graphs (text-minimal)
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(17, 5))

x_sin = np.linspace(0, 2*np.pi, 400)
x_tan = np.linspace(0, 2*np.pi, 600)

# sin
ax = axes[0]
ax.plot(x_sin, np.sin(x_sin), 'k-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=10)
ax.set_ylim(-1.4, 1.4)
ax.set_yticks([-1, 0, 1])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.text(0.02, 0.95, r'$\sin x$', transform=ax.transAxes, fontsize=14, fontweight='bold', va='top')

# cos
ax = axes[1]
ax.plot(x_sin, np.cos(x_sin), 'k-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=10)
ax.set_ylim(-1.4, 1.4)
ax.set_yticks([-1, 0, 1])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.text(0.02, 0.95, r'$\cos x$', transform=ax.transAxes, fontsize=14, fontweight='bold', va='top')

# tan
ax = axes[2]
# Exclude asymptotes
mask = np.abs(np.cos(x_tan)) > 0.03
ax.plot(x_tan[mask], np.tan(x_tan[mask]), 'k-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=10)
ax.set_ylim(-3.5, 3.5)
ax.set_yticks([-3, 0, 3])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
# Asymptote markers
for va in [np.pi/2, 3*np.pi/2]:
    ax.axvline(va, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)
ax.text(0.02, 0.95, r'$\tan x$', transform=ax.transAxes, fontsize=14, fontweight='bold', va='top')

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11b-sin-cos-tan.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b-sin-cos-tan done")

# ================================================================
# 11h: Tangent as Slope of the Radius (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 8))

circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(circle)

theta_d = np.radians(40)
px, py = np.cos(theta_d), np.sin(theta_d)

# Radius line extended
t_val = np.tan(theta_d)
ax.plot([-0.5, 2.0], [-0.5*t_val, 2.0*t_val], 'k-', linewidth=2.5, alpha=0.3)

# Radius segment
ax.plot([0, px], [0, py], 'k-', linewidth=2.5)
ax.scatter([px], [py], s=100, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)

# Vertical tangent line at x=1
ax.axvline(1, color='gray', linestyle='--', linewidth=1.2)
ax.scatter([1], [t_val], s=80, facecolors='black', edgecolors='black', linewidths=2, zorder=10)
ax.text(1.12, t_val, r'$\tan\theta$', fontsize=13, va='center')

# Slope triangle
ax.plot([0, 1], [0, 0], 'k:', linewidth=0.8, alpha=0.4)
ax.text(0.5, -0.12, '1', fontsize=11, ha='center')

# Height
ax.plot([1, 1], [0, t_val], 'k-', linewidth=2)
ax.text(1.15, t_val/2, r'$\frac{\sin\theta}{\cos\theta}$', fontsize=11, va='center')

# Angle
arc = np.linspace(0, theta_d, 40)
ax.plot(0.3*np.cos(arc), 0.3*np.sin(arc), 'k-', linewidth=1.5)
ax.text(0.38, 0.15, r'$\theta$', fontsize=14)

ax.text(px-0.15, py+0.12, r'$(\cos\theta,\sin\theta)$', fontsize=10)
ax.text(1.15, -0.12, '(1,0)', fontsize=9)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal')
ax.set_xlim(-0.5, 2.2)
ax.set_ylim(-0.5, 2.0)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.3)
plt.savefig(OUT + '11h-tangent-as-slope.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11h-tangent-as-slope done")

# ================================================================
# 11c: csc, sec, cot graphs (text-minimal)
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(17, 5.5))

x = np.linspace(0.05, 2*np.pi-0.05, 800)

# csc
ax = axes[0]
y_csc = 1/np.sin(x)
# clip extreme values
y_csc_clipped = np.clip(y_csc, -4, 4)
ax.plot(x, y_csc_clipped, 'k-', linewidth=2)
ax.axhline(0, color='black', linewidth=0.5)
for va in [0, np.pi, 2*np.pi]:
    ax.axvline(va, color='gray', linestyle=':', linewidth=0.7, alpha=0.4)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=9)
ax.set_ylim(-4, 4)
ax.set_yticks([-3, -1, 0, 1, 3])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.axhline(1, color='gray', linestyle=':', linewidth=0.6, alpha=0.3)
ax.axhline(-1, color='gray', linestyle=':', linewidth=0.6, alpha=0.3)
ax.text(0.02, 0.95, r'$\csc x$', transform=ax.transAxes, fontsize=14, fontweight='bold', va='top')

# sec
ax = axes[1]
y_sec = 1/np.cos(x)
y_sec_clipped = np.clip(y_sec, -4, 4)
ax.plot(x, y_sec_clipped, 'k-', linewidth=2)
ax.axhline(0, color='black', linewidth=0.5)
for va in [np.pi/2, 3*np.pi/2]:
    ax.axvline(va, color='gray', linestyle=':', linewidth=0.7, alpha=0.4)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=9)
ax.set_ylim(-4, 4)
ax.set_yticks([-3, -1, 0, 1, 3])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.axhline(1, color='gray', linestyle=':', linewidth=0.6, alpha=0.3)
ax.axhline(-1, color='gray', linestyle=':', linewidth=0.6, alpha=0.3)
ax.text(0.02, 0.95, r'$\sec x$', transform=ax.transAxes, fontsize=14, fontweight='bold', va='top')

# cot
ax = axes[2]
y_cot = 1/np.tan(x)
y_cot_clipped = np.clip(y_cot, -4, 4)
ax.plot(x, y_cot_clipped, 'k-', linewidth=2)
ax.axhline(0, color='black', linewidth=0.5)
for va in [0, np.pi, 2*np.pi]:
    ax.axvline(va, color='gray', linestyle=':', linewidth=0.7, alpha=0.4)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'], fontsize=9)
ax.set_ylim(-4, 4)
ax.set_yticks([-3, -1, 0, 1, 3])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.text(0.02, 0.95, r'$\cot x$', transform=ax.transAxes, fontsize=14, fontweight='bold', va='top')

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11c-csc-sec-cot.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11c-csc-sec-cot done")

# ================================================================
# 11d: y = a sin(bx + c) + d — Wave Transform (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(13, 5))

x = np.linspace(-np.pi/2, 3*np.pi/2, 600)

# Basic sin x
ax.plot(x, np.sin(x), '--', linewidth=1.5, dashes=(6, 4), color='gray', alpha=0.7)

# y = 3 sin(2x - pi/3) + 1
y_trans = 3*np.sin(2*x - np.pi/3) + 1
ax.plot(x, y_trans, 'k-', linewidth=2.8)

# Center line
ax.axhline(1, color='gray', linestyle=':', linewidth=1, alpha=0.5)

# Amplitude markers
x_mid = np.pi/6 + np.pi/4
ax.annotate('', xy=(x_mid, 4), xytext=(x_mid, 1),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text(x_mid+0.08, 2.5, 'A=3', fontsize=12)

# Period marker
ax.annotate('', xy=(np.pi/6, -2.5), xytext=(np.pi/6+np.pi, -2.5),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text(np.pi/6+np.pi/2, -2.9, r'$T=\pi$', fontsize=12, ha='center')

ax.axhline(0, color='black', linewidth=0.5)
ax.set_xticks([-np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2])
ax.set_xticklabels([r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$'], fontsize=11)
ax.set_ylim(-3.5, 5)
ax.set_yticks([-3, -2, 0, 1, 2, 4])
ax.grid(True, alpha=0.15)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout(pad=1)
plt.savefig(OUT + '11d-sin-transform.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11d-sin-transform done")

# ================================================================
# 11i: Pythagorean Identity — Geometric Proof (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 8))

circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(circle)

theta_d = np.radians(45)
px, py = np.cos(theta_d), np.sin(theta_d)

# Filled right triangle
triangle_x = [0, px, px, 0]
triangle_y = [0, 0, py, 0]
ax.fill(triangle_x, triangle_y, facecolor='lightgray', edgecolor='black', linewidth=1.5, alpha=0.4)

# Radius
ax.plot([0, px], [0, py], 'k-', linewidth=2.5)

# Point
ax.scatter([px], [py], s=100, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)
ax.text(px+0.1, py+0.1, r'$(\cos\theta,\sin\theta)$', fontsize=12)

# Side labels
ax.text(px/2, -0.15, r'$\cos\theta$', fontsize=13, ha='center')
ax.text(px+0.15, py/2, r'$\sin\theta$', fontsize=13, va='center')
ax.text(px/2-0.15, py/2+0.15, '1', fontsize=14, fontweight='bold')

# Right angle
ax.plot([px-0.12, px-0.12], [0, 0.12], 'k-', linewidth=1)
ax.plot([px-0.12, px], [0.12, 0.12], 'k-', linewidth=1)

# Angle
arc = np.linspace(0, theta_d, 40)
ax.plot(0.3*np.cos(arc), 0.3*np.sin(arc), 'k-', linewidth=1.5)
ax.text(0.38, 0.15, r'$\theta$', fontsize=14)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal')
ax.set_xlim(-0.3, 1.3)
ax.set_ylim(-0.3, 1.3)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.3)
plt.savefig(OUT + '11i-pythagorean-proof.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11i-pythagorean-proof done")

# ================================================================
# 11g: Combined reference angle overview (bonus, not referenced in md)
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

angles = [(150, 'II'), (210, 'III'), (300, 'IV')]
for ax, (ang, q) in zip(axes, angles):
    draw_reference_angle(ax, ang, q)

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11g-reference-angle.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11g-reference-angle done")

print("\n=== All 11A graphs regenerated (text-minimal) ===")
