"""
Generate visual graphs for Session 11B.
PRINCIPLE: graphs are visual, text belongs in markdown.
Only essential geometric labels (A, B, C, a, b, c, R, θ, φ, etc.) appear in images.
No titles, no formula boxes, no explanatory text — just the geometry.
Black-and-white optimized: distinct line styles, marker shapes, hatch patterns.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True
rcParams['font.size'] = 14

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'
DPI = 180

# ================================================================
# 11b1: Harmonic Addition — Phasor + Wave (text-minimal)
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5.5))

a, b = 3, 4
R_val = np.sqrt(a**2 + b**2)
phi = np.arctan2(b, a)

# Left: Phasor triangle
ax1.fill([0, a, a], [0, 0, b], facecolor='lightgray', edgecolor='black', linewidth=2, alpha=0.4)
ax1.plot([0, a], [0, 0], 'k-', linewidth=2.5)
ax1.plot([a, a], [0, b], 'k--', linewidth=2.5)
ax1.plot([0, a], [0, b], 'k-', linewidth=3)
arc_phi = np.linspace(0, phi, 50)
ax1.plot(0.7 * np.cos(arc_phi), 0.7 * np.sin(arc_phi), 'k-', linewidth=1.5)
ax1.text(a/2, -0.35, 'a', ha='center', fontsize=15)
ax1.text(a + 0.25, b/2, 'b', fontsize=15)
ax1.text(a/2 - 0.15, b/2 + 0.25, 'R', fontsize=15)
ax1.text(0.95, 0.35, r'$\phi$', fontsize=16)
ax1.set_xlim(-0.6, 5.2)
ax1.set_ylim(-0.6, 4.8)
ax1.set_aspect('equal')
ax1.axhline(0, color='black', linewidth=0.4)
ax1.axvline(0, color='black', linewidth=0.4)
ax1.set_xticks([])
ax1.set_yticks([])
for spine in ax1.spines.values():
    spine.set_visible(False)

# Right: Wave superposition
x = np.linspace(0, 2*np.pi, 500)
ax2.plot(x, a*np.sin(x), '--', linewidth=1.3, dashes=(7, 4), color='gray')
ax2.plot(x, b*np.cos(x), '-.', linewidth=1.3, color='gray')
ax2.plot(x, a*np.sin(x)+b*np.cos(x), 'k-', linewidth=2.8)
ax2.axhline(0, color='black', linewidth=0.4)
xt = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
xl = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
ax2.set_xticks(xt)
ax2.set_xticklabels(xl, fontsize=11)
ax2.set_ylim(-6.5, 6.5)
ax2.set_yticks([-5, 0, 5])
ax2.grid(True, alpha=0.2)
for spine in ['top', 'right']:
    ax2.spines[spine].set_visible(False)

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11b1-harmonic-addition.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b1 done")

# ================================================================
# 11b2: Sum-to-Product — Beat Pattern (text-minimal)
# ================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6.5))

x = np.linspace(0, 4*np.pi, 1000)
A_f, B_f = 10, 8
y_sum = np.sin(A_f*x) + np.sin(B_f*x)
env = 2 * np.cos((A_f - B_f)/2 * x)

ax1.plot(x, y_sum, 'k-', linewidth=1.8)
ax1.plot(x, env, ':', linewidth=1.8, color='gray')
ax1.plot(x, -env, ':', linewidth=1.8, color='gray')
ax1.axhline(0, color='black', linewidth=0.4)
ax1.set_ylim(-3, 3)
ax1.set_yticks([-2, 0, 2])
ax1.set_xticks([])
ax1.grid(True, alpha=0.2)
for spine in ['top', 'right', 'bottom']:
    ax1.spines[spine].set_visible(False)

y_prod = np.sin(10*x) * np.cos(2*x)
ax2.plot(x, y_prod, 'k-', linewidth=2)
ax2.plot(x, 0.5*np.sin(12*x), '--', linewidth=1, dashes=(6, 4), color='gray', alpha=0.6)
ax2.plot(x, 0.5*np.sin(8*x), '-.', linewidth=1, color='gray', alpha=0.6)
ax2.axhline(0, color='black', linewidth=0.4)
ax2.set_ylim(-1.3, 1.3)
ax2.set_yticks([-1, 0, 1])
ax2.set_xticks([])
ax2.grid(True, alpha=0.2)
for spine in ['top', 'right', 'bottom']:
    ax2.spines[spine].set_visible(False)

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11b2-sum-product-waves.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b2 done")

# ================================================================
# 11b3: Trig Equation Solutions — sin x = 1/2
# ================================================================
fig, ax = plt.subplots(figsize=(12, 4.5))

x = np.linspace(-np.pi, 3*np.pi, 800)
ax.plot(x, np.sin(x), 'k-', linewidth=2.5)
ax.axhline(0.5, color='gray', linestyle='--', linewidth=1.5)

sols = [np.pi/6, 5*np.pi/6, 13*np.pi/6, 17*np.pi/6]
labs = [r'$\frac{\pi}{6}$', r'$\frac{5\pi}{6}$', r'$\frac{13\pi}{6}$', r'$\frac{17\pi}{6}$']
for s, l in zip(sols, labs):
    ax.scatter([s], [0.5], s=100, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)
    ax.annotate(l, (s, 0.5), textcoords="offset points", xytext=(0, 15),
                ha='center', fontsize=12)

ax.axhline(0, color='black', linewidth=0.5)
ax.set_xticks([-np.pi, 0, np.pi, 2*np.pi, 3*np.pi])
ax.set_xticklabels([r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$'], fontsize=12)
ax.set_ylim(-1.5, 1.8)
ax.set_yticks([-1, 0, 1])
ax.grid(True, alpha=0.2)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout(pad=1)
plt.savefig(OUT + '11b3-trig-equation-solutions.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b3 done")

# ================================================================
# 11b4: Law of Sines — Circumcircle (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 8))

R_val = 3
angs = [30, 80, 70]
A_ang = np.radians(0)
B_ang = np.radians(angs[0])
C_ang = np.radians(angs[0] + angs[1])

A = np.array([R_val*np.cos(A_ang), R_val*np.sin(A_ang)])
B = np.array([R_val*np.cos(B_ang), R_val*np.sin(B_ang)])
C = np.array([R_val*np.cos(C_ang), R_val*np.sin(C_ang)])

circle = plt.Circle((0, 0), R_val, fill=False, edgecolor='black', linewidth=2, linestyle='--')
ax.add_patch(circle)

ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', linewidth=2.5)
ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', linewidth=2.5)
ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', linewidth=2.5)

mAB = (A+B)/2; mBC = (B+C)/2; mCA = (C+A)/2
ax.text(mAB[0]+0.3, mAB[1]-0.1, 'c', fontsize=15, fontweight='bold')
ax.text(mBC[0]-0.5, mBC[1]+0.15, 'a', fontsize=15, fontweight='bold')
ax.text(mCA[0]+0.25, mCA[1]+0.15, 'b', fontsize=15, fontweight='bold')

ax.text(A[0]+0.2, A[1]-0.25, 'A', fontsize=15, fontweight='bold')
ax.text(B[0]-0.3, B[1]+0.25, 'B', fontsize=15, fontweight='bold')
ax.text(C[0]-0.3, C[1]-0.25, 'C', fontsize=15, fontweight='bold')

ax.scatter([0], [0], s=40, c='black', zorder=5)
ax.text(0.2, -0.3, 'O', fontsize=13)
ax.plot([0, A[0]], [0, A[1]], 'k:', linewidth=1, alpha=0.5)
ax.text(1.3, 0.3, 'R', fontsize=13)

ax.set_aspect('equal')
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-4.2, 4.2)
ax.axis('off')

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b4-law-of-sines.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b4 done")

# ================================================================
# 11b5: Law of Cosines — Altitude Derivation (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 6.5))

C_pt = np.array([0, 0])
B_pt = np.array([7, 0])
A_pt = np.array([2.5, 4])
D_pt = np.array([A_pt[0], 0])

ax.plot([C_pt[0], B_pt[0]], [C_pt[1], B_pt[1]], 'k-', linewidth=2.5)
ax.plot([B_pt[0], A_pt[0]], [B_pt[1], A_pt[1]], 'k-', linewidth=2.5)
ax.plot([A_pt[0], C_pt[0]], [A_pt[1], C_pt[1]], 'k-', linewidth=2.5)
ax.plot([A_pt[0], D_pt[0]], [A_pt[1], D_pt[1]], 'k--', linewidth=1.5)

# Labels
ax.text((C_pt[0]+B_pt[0])/2, -0.45, 'a', fontsize=15, fontweight='bold', ha='center')
ax.text((B_pt[0]+A_pt[0])/2+0.35, (B_pt[1]+A_pt[1])/2, 'c', fontsize=15, fontweight='bold')
ax.text((C_pt[0]+A_pt[0])/2-0.45, (C_pt[1]+A_pt[1])/2, 'b', fontsize=15, fontweight='bold')
ax.text(A_pt[0]+0.2, A_pt[1]/2, 'h', fontsize=14)
ax.text(D_pt[0]/2-0.1, -0.45, r'$b\cos C$', fontsize=12, ha='center')
ax.text((D_pt[0]+B_pt[0])/2, -0.45, r'$a-b\cos C$', fontsize=12, ha='center')

# Right angle
ax.plot([D_pt[0]+0.3, D_pt[0]+0.3], [0, 0.3], 'k-', linewidth=1)
ax.plot([D_pt[0], D_pt[0]+0.3], [0.3, 0.3], 'k-', linewidth=1)

ax.text(C_pt[0]-0.35, C_pt[1]-0.35, 'C', fontsize=15, fontweight='bold')
ax.text(B_pt[0]+0.15, B_pt[1]-0.35, 'B', fontsize=15, fontweight='bold')
ax.text(A_pt[0]-0.35, A_pt[1]+0.2, 'A', fontsize=15, fontweight='bold')
ax.text(D_pt[0]+0.15, D_pt[1]-0.35, 'D', fontsize=12)

arc = np.linspace(0, np.arctan2(A_pt[1], A_pt[0]), 40)
ax.plot(1.0*np.cos(arc), 1.0*np.sin(arc), 'k-', linewidth=1.5)
ax.text(1.3, 0.45, 'C', fontsize=14)

ax.set_aspect('equal')
ax.set_xlim(-1, 8)
ax.set_ylim(-1.5, 5.5)
ax.axis('off')

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b5-law-of-cosines.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b5 done")

# ================================================================
# 11b6: Triangle Area — Three Methods (text-minimal, 3 panels)
# ================================================================
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

# Method 1: half base * height
ax1.plot([0, 6, 2, 0], [0, 0, 4, 0], 'k-', linewidth=2.5)
ax1.plot([2, 2], [0, 4], 'k--', linewidth=1.5)
ax1.text(3, -0.5, 'b', ha='center', fontsize=14)
ax1.text(2.3, 2, 'h', fontsize=14)
ax1.plot([1.7, 2], [0.3, 0.3], 'k-', linewidth=1)
ax1.plot([2, 2], [0, 0.3], 'k-', linewidth=1)
ax1.set_aspect('equal')
ax1.set_xlim(-0.5, 6.5)
ax1.set_ylim(-1, 5)
ax1.axis('off')

# Method 2: half ab sin C
ax2.plot([0, 6, 1.2, 0], [0, 0, 3.8, 0], 'k-', linewidth=2.5)
ax2.plot([1.2, 1.2], [0, 3.8], 'k--', linewidth=1.5)
arc2 = np.linspace(0, np.arctan2(3.8, 1.2), 40)
ax2.plot(1.0*np.cos(arc2), 1.0*np.sin(arc2), 'k-', linewidth=1.5)
ax2.text(1.4, 0.5, 'C', fontsize=14)
ax2.text(3, -0.5, 'a', ha='center', fontsize=14)
ax2.text(0.2, 2, 'b', fontsize=14)
ax2.set_aspect('equal')
ax2.set_xlim(-0.5, 6.5)
ax2.set_ylim(-1, 5)
ax2.axis('off')

# Method 3: Heron — just sides
a3, b3, c3 = 13, 14, 15
xA = (a3**2 + b3**2 - c3**2)/(2*a3)
yA = np.sqrt(b3**2 - xA**2)
ax3.plot([0, a3, xA, 0], [0, 0, yA, 0], 'k-', linewidth=2.5)
ax3.text(a3/2, -0.8, 'a', ha='center', fontsize=14)
ax3.text((a3+xA)/2+0.5, yA/2, 'c', fontsize=14)
ax3.text(xA/2-0.6, yA/2, 'b', fontsize=14)
ax3.set_aspect('equal')
ax3.set_xlim(-2, 16)
ax3.set_ylim(-2, 13)
ax3.axis('off')

plt.tight_layout(pad=1)
plt.savefig(OUT + '11b6-triangle-area-methods.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b6 done")

# ================================================================
# 11b7: Inverse Trig Functions — Reflection (text-minimal)
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(17, 5.5))

for idx, ax in enumerate(axes):
    if idx == 0:
        xo = np.linspace(-np.pi/2, np.pi/2, 300)
        ax.plot(xo, np.sin(xo), 'k-', linewidth=2)
        ax.plot(np.sin(xo), xo, 'k--', linewidth=2.5)
        ax.set_xlim(-1.8, 1.8)
        ax.set_ylim(-1.8, 1.8)
    elif idx == 1:
        xo = np.linspace(0, np.pi, 300)
        ax.plot(xo, np.cos(xo), 'k-', linewidth=2)
        ax.plot(np.cos(xo), xo, 'k--', linewidth=2.5)
        ax.set_xlim(-1.8, 2.5)
        ax.set_ylim(-0.5, 3.5)
    else:
        xo = np.linspace(-1.3, 1.3, 300)
        ax.plot(xo, np.tan(xo), 'k-', linewidth=2)
        ax.plot(np.tan(xo), xo, 'k--', linewidth=2.5)
        ax.set_xlim(-4, 4)
        ax.set_ylim(-1.6, 1.6)
        ax.axhline(np.pi/2, color='gray', linestyle=':', linewidth=0.6)
        ax.axhline(-np.pi/2, color='gray', linestyle=':', linewidth=0.6)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    lo = max(xlim[0], ylim[0])
    hi = min(xlim[1], ylim[1])
    ax.plot([lo, hi], [lo, hi], ':', linewidth=1, color='gray', alpha=0.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11b7-inverse-trig-functions.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b7 done")

# ================================================================
# 11b8: Euler's Formula — Complex Unit Circle (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 8))

theta_c = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', linewidth=2)

theta_d = np.radians(50)
pt = np.array([np.cos(theta_d), np.sin(theta_d)])

ax.plot([0, pt[0]], [0, pt[1]], 'k-', linewidth=2.5)
ax.scatter([pt[0]], [pt[1]], s=120, facecolors='white', edgecolors='black', linewidths=3, zorder=10)
ax.text(pt[0]+0.1, pt[1]+0.1, r'$e^{i\theta}$', fontsize=15, fontweight='bold')

# Projections
ax.plot([pt[0], pt[0]], [0, pt[1]], 'k--', linewidth=1.2)
ax.plot([0, pt[0]], [pt[1], pt[1]], 'k:', linewidth=1.2)
ax.text(pt[0]/2, -0.18, r'$\cos\theta$', fontsize=13, ha='center')
ax.text(-0.4, pt[1]/2, r'$\sin\theta$', fontsize=13, va='center')

arc = np.linspace(0, theta_d, 40)
ax.plot(0.4*np.cos(arc), 0.4*np.sin(arc), 'k-', linewidth=1.5)
ax.text(0.52, 0.22, r'$\theta$', fontsize=15)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.text(1.12, -0.12, 'Re', fontsize=14)
ax.text(-0.12, 1.12, 'Im', fontsize=14)

for ang, lab in [(0, '1'), (90, 'i'), (180, '-1'), (270, '-i')]:
    ar = np.radians(ang)
    ax.scatter([np.cos(ar)], [np.sin(ar)], s=40, c='black', zorder=5)
    ax.text(np.cos(ar)*1.18-0.06, np.sin(ar)*1.18, lab, fontsize=13, fontweight='bold')

ax.set_aspect('equal')
ax.set_xlim(-1.45, 1.45)
ax.set_ylim(-1.45, 1.45)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b8-euler-formula-complex.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b8 done")

# ================================================================
# 11b9: Chebyshev Polynomials (text-minimal)
# ================================================================
fig, axes = plt.subplots(2, 2, figsize=(11, 9))
x = np.linspace(-1.05, 1.05, 400)

data = [
    (r'$T_1$', x),
    (r'$T_2$', 2*x**2 - 1),
    (r'$T_3$', 4*x**3 - 3*x),
    (r'$T_4$', 8*x**4 - 8*x**2 + 1),
]

for ax, (lab, yv) in zip(axes.flat, data):
    ax.plot(x, yv, 'k-', linewidth=2.5)
    ax.axhline(0, color='black', linewidth=0.4)
    ax.axvline(0, color='black', linewidth=0.4)
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.3, 1.3)
    ax.text(0.95, 1.1, lab, fontsize=16, fontweight='bold', ha='right', va='top',
            transform=ax.transAxes)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.grid(True, alpha=0.2)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

plt.tight_layout(pad=1.5)
plt.savefig(OUT + '11b9-chebyshev-polynomials.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b9 done")

# ================================================================
# 11b10: Cubic via Trig — Casus Irreducibilis (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(10, 5.5))

x = np.linspace(-2.5, 2.5, 500)
y = x**3 - 3*x - 1
ax.plot(x, y, 'k-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=0.8)

roots = [2*np.cos(np.pi/9), 2*np.cos(7*np.pi/9), 2*np.cos(13*np.pi/9)]
for r in roots:
    ax.scatter([r], [0], s=100, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-4, 4)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.grid(True, alpha=0.2)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout(pad=1)
plt.savefig(OUT + '11b10-cubic-trigonometric.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b10 done")

# ================================================================
# 11b11: Weierstrass Substitution — Stereographic Projection (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 8))

theta_c = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', linewidth=2.5)

# Pole at (-1,0)
ax.scatter([-1], [0], s=80, c='black', zorder=10)

# A point on the circle
t_val = 1.5
px = (1 - t_val**2)/(1 + t_val**2)
py = 2*t_val/(1 + t_val**2)
ax.scatter([px], [py], s=100, facecolors='white', edgecolors='black', linewidths=3, zorder=10)

# t on y-axis
ax.scatter([0], [t_val], s=80, facecolors='black', edgecolors='black', linewidths=2, zorder=10)
ax.text(0.15, t_val, 't', fontsize=14)

# Projection line
ax.plot([-1, 0], [0, t_val], 'k:', linewidth=1.2, alpha=0.5)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='gray', linestyle=':', linewidth=0.6)

ax.set_aspect('equal')
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.3, 3.2)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b11-weierstrass-substitution.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b11 done")

# ================================================================
# 11b12: Golden Ratio Pentagon (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(9, 9))

n = 5
angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, n+1)
R_p = 3.5
vx = R_p * np.cos(angles)
vy = R_p * np.sin(angles)

ax.plot(vx, vy, 'k-', linewidth=2.5)

# All diagonals
for i in range(n):
    for j in range(i+2, n):
        if not (i == 0 and j == n-1):
            ax.plot([vx[i], vx[j]], [vy[i], vy[j]], 'k--', linewidth=1, alpha=0.4)

# Vertex labels
for i in range(n):
    ax.text(vx[i]*1.15, vy[i]*1.15, chr(65+i), fontsize=14, fontweight='bold', ha='center', va='center')

# Diagonal ratio
ax.annotate('', xy=(vx[0], vy[0]), xytext=(vx[2], vy[2]),
            arrowprops=dict(arrowstyle='<->', color='black', lw=2.5))
mid = ((vx[0]+vx[2])/2, (vy[0]+vy[2])/2)
ax.text(mid[0]+0.5, mid[1]+0.3, r'$\phi$', fontsize=18, fontweight='bold')

# Side marker
ms = ((vx[0]+vx[1])/2, (vy[0]+vy[1])/2)
ax.text(ms[0]-0.7, ms[1]-0.1, '1', fontsize=14, ha='center')

ax.set_aspect('equal')
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-4.5, 4.5)
ax.axis('off')

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b12-golden-ratio-pentagon.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b12 done")

# ================================================================
# 11b13: Sum Formula — Euler Rotation (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 8))

circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(circle)

A_d = np.radians(30)
B_d = np.radians(25)

PA = np.array([np.cos(A_d), np.sin(A_d)])
PAB = np.array([np.cos(A_d+B_d), np.sin(A_d+B_d)])
PB = np.array([np.cos(B_d), np.sin(B_d)])

ax.plot([0, PA[0]], [0, PA[1]], 'k-', linewidth=2)
ax.plot([0, PAB[0]], [0, PAB[1]], 'k-', linewidth=2.5)
ax.plot([0, PB[0]], [0, PB[1]], 'k--', linewidth=1.5, alpha=0.5)

arcA = np.linspace(0, A_d, 40)
arcAB = np.linspace(0, A_d+B_d, 60)
arcB = np.linspace(A_d, A_d+B_d, 40)

ax.plot(0.3*np.cos(arcA), 0.3*np.sin(arcA), 'k-', linewidth=1.5)
ax.plot(0.5*np.cos(arcAB), 0.5*np.sin(arcAB), 'k-', linewidth=2)
ax.plot(0.65*np.cos(arcB), 0.65*np.sin(arcB), 'k--', linewidth=1.5)

ax.text(0.38, 0.12, 'A', fontsize=14)
ax.text(0.6, 0.38, 'B', fontsize=14)
ax.text(0.72, 0.68, 'A+B', fontsize=14)

ax.text(PA[0]+0.1, PA[1]+0.1, r'$e^{iA}$', fontsize=13)
ax.text(PAB[0]+0.1, PAB[1]+0.1, r'$e^{i(A+B)}$', fontsize=14, fontweight='bold')

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

ax.set_aspect('equal')
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b13-sum-formula-geometric.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b13 done")

# ================================================================
# 11b14: Morrie's Law — cos 20°·cos 40°·cos 80° (text-minimal)
# ================================================================
fig, ax = plt.subplots(figsize=(8, 7))

circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2)
ax.add_patch(circle)

angs = [20, 40, 80]
styles = ['-', '--', '-.']

for ang, sty in zip(angs, styles):
    ar = np.radians(ang)
    px, py = np.cos(ar), np.sin(ar)
    ax.plot([0, px], [0, py], f'k{sty}', linewidth=2)
    ax.plot([0, px], [0, -py], f'k{sty}', linewidth=1, alpha=0.3)
    ax.plot([px, px], [0, py], 'k:', linewidth=0.7, alpha=0.4)
    ax.scatter([px], [0], s=50, facecolors='white', edgecolors='black', linewidths=2, zorder=8)
    ax.text(px, -0.15, f'{ang}°', fontsize=10, ha='center')

ax.set_aspect('equal')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.1, 1.1)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
for spine in ['top', 'right', 'bottom', 'left']:
    ax.spines[spine].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout(pad=0.5)
plt.savefig(OUT + '11b14-morries-law.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b14 done")

# ================================================================
# 11b15: Spherical Coordinates — Trig in 3D (NEW)
# ================================================================
fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(111, projection='3d')

# Wireframe sphere
u = np.linspace(0, 2*np.pi, 40)
v = np.linspace(0, np.pi, 25)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_wireframe(x, y, z, color='gray', linewidth=0.3, alpha=0.4)

# Equator
eq = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(eq), np.sin(eq), 0, 'k-', linewidth=1.5)

# A meridian
mer = np.linspace(0, np.pi, 60)
mer_phi = np.radians(45)
ax.plot(np.sin(mer)*np.cos(mer_phi), np.sin(mer)*np.sin(mer_phi), np.cos(mer), 'k--', linewidth=1.2)

# A point P
phi_p = np.radians(50)
theta_p = np.radians(45)
P = np.array([np.sin(phi_p)*np.cos(theta_p), np.sin(phi_p)*np.sin(theta_p), np.cos(phi_p)])
ax.scatter([P[0]], [P[1]], [P[2]], s=80, facecolors='white', edgecolors='black', linewidths=2.5, zorder=10)
ax.text(P[0]+0.1, P[1]+0.1, P[2], 'P', fontsize=13, fontweight='bold')

# Lines
ax.plot([0, P[0]], [0, P[1]], [0, P[2]], 'k-', linewidth=1.5)
Pxy = np.array([P[0], P[1], 0])
ax.plot([0, Pxy[0]], [0, Pxy[1]], [0, 0], 'k:', linewidth=1)
ax.plot([P[0], Pxy[0]], [P[1], Pxy[1]], [P[2], 0], 'k:', linewidth=0.8, alpha=0.5)

# Angle arcs
arc_th = np.linspace(0, theta_p, 30)
ax.plot(0.3*np.cos(arc_th), 0.3*np.sin(arc_th), 0, 'k-', linewidth=1.5)
ax.text(0.28, 0.15, 0, r'$\theta$', fontsize=13)

# Phi arc (small dots along arc)
for a in np.linspace(0, phi_p, 20):
    r_arc = 0.4
    ax.plot([r_arc*np.sin(a)*np.cos(theta_p)], [r_arc*np.sin(a)*np.sin(theta_p)], [r_arc*np.cos(a)],
            'k.', markersize=1.5)
ax.text(0.22, 0.22, 0.45, r'$\phi$', fontsize=13)

# Axes
ax.plot([-1.2, 1.2], [0, 0], [0, 0], 'k-', linewidth=0.6)
ax.plot([0, 0], [-1.2, 1.2], [0, 0], 'k-', linewidth=0.6)
ax.plot([0, 0], [0, 0], [-1.2, 1.2], 'k-', linewidth=0.6)
ax.text(1.3, 0, 0, 'x', fontsize=13)
ax.text(0, 1.3, 0, 'y', fontsize=13)
ax.text(0, 0, 1.3, 'z', fontsize=13)

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')
ax.view_init(elev=20, azim=-60)

plt.tight_layout(pad=0)
plt.savefig(OUT + '11b15-spherical-coordinates.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b15 done")

# ================================================================
# 11b16: Hypersphere Volumes — n-dimensional ball (NEW)
# ================================================================
import math

fig, ax = plt.subplots(figsize=(10, 5.5))

n_vals = np.arange(1, 21)
V = np.array([np.pi**(n/2) / math.gamma(n/2 + 1) for n in n_vals])

ax.plot(n_vals, V, 'ko-', linewidth=2, markersize=8, markerfacecolor='white')

# Mark peak at n=5
max_idx = np.argmax(V)
ax.scatter([n_vals[max_idx]], [V[max_idx]], s=140, facecolors='black', edgecolors='black', linewidths=2, zorder=10)

ax.set_xlabel('dimension n', fontsize=14)
ax.set_ylabel('volume', fontsize=14)
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.2, linestyle=':')
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout(pad=1)
plt.savefig(OUT + '11b16-hypersphere-volumes.png', dpi=DPI, bbox_inches='tight')
plt.close()
print("11b16 done")

print("\n=== All 11B graphs regenerated (text-minimal) + 2 new Visual Interlude graphs ===")
