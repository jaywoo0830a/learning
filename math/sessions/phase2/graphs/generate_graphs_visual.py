"""
Generate visualization graphs for Sessions 10 (Exponents & Logs) and 11 (Trigonometry).
All graphs are FULL-SIZE standalone figures — no subplots crammed together.
Suitable for print: large fonts, thick lines, high DPI.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'
BIG = (12, 7)
SQ  = (9, 9)

# ================================================================
# SESSION 10 — EXPONENTS & LOGARITHMS
# ================================================================

# --- 10e1: Number Line — Repeated Doubling (FULL SIZE) ---
fig, ax = plt.subplots(figsize=(12, 4))
for i in range(-4, 5):
    if i < 0:
        val = r'$\frac{1}{%d}$' % (2**(-i))
    elif i == 0:
        val = '1'
    else:
        val = str(2**i)
    ax.plot(i, 0, 'ko', markersize=14)
    ax.text(i, 0.55, val, ha='center', fontsize=16, fontweight='bold')
ax.axhline(0, color='gray', linewidth=1)
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-0.8, 1.8)
ax.set_xticks(range(-4, 5))
ax.set_xticklabels([str(i) for i in range(-4, 5)], fontsize=14)
ax.set_yticks([])
ax.set_xlabel('x (input)', fontsize=16)
fig.suptitle('View 1: $2^x$ as Repeated Doubling on a Number Line', fontsize=18, fontweight='bold')
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.annotate('', xy=(4.3, 0), xytext=(-4.3, 0),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
ax.text(0, -0.55, 'divide by 2 (halving)          multiply by 2 (doubling)',
        ha='center', fontsize=13, color='blue')
plt.tight_layout()
plt.savefig(OUT + '10e1-doubling-numberline.png', dpi=180, bbox_inches='tight')
plt.close()
print("10e1 done")

# --- 10e2: Dimension Scaling — Area vs Volume (FULL SIZE) ---
fig, ax = plt.subplots(figsize=(10, 7))
sides = np.array([1, 2, 3, 4, 5])
area = sides**2
volume = sides**3
x_plot = np.arange(len(sides))
w = 0.35
bars1 = ax.bar(x_plot - w/2, area, w, color='steelblue', alpha=0.8, label='Area = side^2')
bars2 = ax.bar(x_plot + w/2, volume, w, color='darkorange', alpha=0.8, label='Volume = side^3')
for bar, val in zip(bars1, area):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, str(val),
            ha='center', fontsize=13, fontweight='bold', color='steelblue')
for bar, val in zip(bars2, volume):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, str(val),
            ha='center', fontsize=13, fontweight='bold', color='darkorange')
ax.set_xticks(x_plot)
ax.set_xticklabels([str(s) for s in sides], fontsize=15)
ax.set_xlabel('Side Length', fontsize=16)
ax.set_ylabel('Measure', fontsize=16)
fig.suptitle('View 2: Exponent = Dimension — Scaling Area and Volume', fontsize=18, fontweight='bold')
ax.legend(fontsize=14, loc='upper left')
ax.grid(axis='y', alpha=0.3)
ax.tick_params(axis='y', labelsize=13)
plt.tight_layout()
plt.savefig(OUT + '10e2-dimension-scaling.png', dpi=180, bbox_inches='tight')
plt.close()
print("10e2 done")

# --- 10e3: e^x — Slope Equals Height (FULL SIZE) ---
fig, ax = plt.subplots(figsize=BIG)
x = np.linspace(-0.5, 3.5, 400)
y = np.exp(x)
ax.plot(x, y, 'b-', linewidth=4, label=r'$y = e^x$', zorder=3)
x_t0 = np.linspace(-0.6, 1.2, 80)
ax.plot(x_t0, x_t0 + 1, 'r--', linewidth=3, label='tangent at (0,1): slope = 1')
x_t1 = np.linspace(0.2, 1.8, 80)
ax.plot(x_t1, np.e*(x_t1 - 1) + np.e, 'g--', linewidth=3,
        label='tangent at (1,e): slope = e = 2.718')
ax.scatter([0, 1], [1, np.e], s=150, c='red', zorder=5)
ax.text(0.08, 1.5, '(0, 1)\nslope = 1', fontsize=14, color='red', fontweight='bold')
ax.text(1.08, np.e + 0.6, '(1, e)\nslope = e', fontsize=14, color='green', fontweight='bold')
ax.set_xlim(-0.4, 3.5)
ax.set_ylim(-0.5, 18)
ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('y', fontsize=16)
fig.suptitle('View 3: $e^x$ — The Curve Whose Slope Equals Its Height', fontsize=18, fontweight='bold')
ax.legend(fontsize=13, loc='upper left')
ax.grid(alpha=0.3)
ax.tick_params(labelsize=13)
plt.tight_layout()
plt.savefig(OUT + '10e3-exp-slope-equals-height.png', dpi=180, bbox_inches='tight')
plt.close()
print("10e3 done")

# --- 10f: Logarithm as Area Under 1/x (BIGGER) ---
fig, ax = plt.subplots(figsize=(12, 7))
x = np.linspace(0.12, 6.5, 900)
y = 1 / x
ax.plot(x, y, 'b-', linewidth=3.5, label=r'$y = 1/x$')
a = 4
x_fill = np.linspace(1, a, 350)
ax.fill_between(x_fill, 0, 1/x_fill, alpha=0.35, color='steelblue',
                label=rf'Area = $\ln(4) \approx {np.log(4):.3f}$')
b = 2.5
x_fill_b = np.linspace(1, b, 250)
ax.fill_between(x_fill_b, 0, 1/x_fill_b, alpha=0.25, color='darkorange',
                label=rf'Area = $\ln(2.5) \approx {np.log(2.5):.3f}$')
ax.axhline(0, color='gray', linewidth=0.6)
ax.axvline(1, color='gray', linestyle=':', linewidth=1.2)
ax.axvline(a, color='steelblue', linestyle='--', linewidth=1, alpha=0.6)
ax.axvline(b, color='darkorange', linestyle='--', linewidth=1, alpha=0.6)
ax.scatter([1, b, a], [1, 1/b, 1/a], s=80, c='red', zorder=5)
ax.set_xlim(0, 6.5)
ax.set_ylim(0, 4.5)
ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('y', fontsize=16)
fig.suptitle(r'$\ln a$ = Area Under $y = 1/x$ from $x=1$ to $x=a$', fontsize=18, fontweight='bold')
ax.legend(fontsize=13, loc='upper right')
ax.grid(alpha=0.2)
ax.tick_params(labelsize=13)
ax.text(3.8, 3.6, r'$\ln(ab) = \ln a + \ln b$', fontsize=14, color='darkgreen',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.4))
ax.text(3.8, 3.0, r'$\ln(a^k) = k\ln a$', fontsize=14, color='darkgreen',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.4))
ax.text(3.8, 2.4, r'$\ln(1/a) = -\ln a$', fontsize=14, color='darkgreen',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.4))
plt.tight_layout()
plt.savefig(OUT + '10f-log-as-area.png', dpi=180, bbox_inches='tight')
plt.close()
print("10f done — Log as Area")

# --- 10g1: Linear Scale (STANDALONE) ---
fig, ax = plt.subplots(figsize=(14, 4))
values = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
ax.plot(values, [0]*len(values), 'ko', markersize=10)
for v in values:
    ax.text(v, 0.18, str(v), ha='center', fontsize=13, fontweight='bold')
ax.set_xlim(-30, 1050)
ax.set_ylim(-0.3, 0.8)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
fig.suptitle('Linear Scale — Equal Spacing for Equal Additive Steps', fontsize=18, fontweight='bold')
ax.set_xlabel('Value', fontsize=15)
ax.tick_params(labelsize=12)
ax.text(500, 0.55, '1 to 2 looks same distance as 500 to 501 — additive thinking',
        ha='center', fontsize=13, color='gray',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
plt.tight_layout()
plt.savefig(OUT + '10g1-linear-scale.png', dpi=180, bbox_inches='tight')
plt.close()
print("10g1 done")

# --- 10g2: Log Scale (STANDALONE) ---
fig, ax = plt.subplots(figsize=(14, 4))
values = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
log_vals = np.log10(values)
ax.plot(log_vals, [0]*len(log_vals), 'ko', markersize=10)
for lv, v in zip(log_vals, values):
    ax.text(lv, 0.18, str(v), ha='center', fontsize=13, fontweight='bold')
ax.set_xlim(-0.3, 3.3)
ax.set_ylim(-0.3, 0.8)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
fig.suptitle(r'Log Scale ($\log_{10}$) — Equal Spacing for Equal Multiplicative Jumps',
             fontsize=18, fontweight='bold')
ax.set_xlabel(r'$\log_{10}$(Value)', fontsize=15)
ax.tick_params(labelsize=12)
ax.text(1.5, 0.55, '1 to 10 is same distance as 100 to 1000 — both are x10\n'
         r'$10^{-35}$ m (Planck) to $10^{26}$ m (universe) all on one page',
         ha='center', fontsize=13, color='darkblue',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
plt.tight_layout()
plt.savefig(OUT + '10g2-log-scale.png', dpi=180, bbox_inches='tight')
plt.close()
print("10g2 done")

# --- 10h: Growth Race — NO inset, BIGGER ---
fig, ax = plt.subplots(figsize=BIG)
x = np.linspace(0.1, 10, 500)
ax.plot(x, x, 'k--', linewidth=2.5, label=r'$y = x$', alpha=0.8)
ax.plot(x, x**2, 'orange', linewidth=2.5, label=r'$y = x^2$', alpha=0.8)
ax.plot(x, 2**x, 'red', linewidth=4, label=r'$y = 2^x$')
ax.plot(x, np.log(x), 'blue', linewidth=3.5, label=r'$y = \ln x$')
ax.annotate(r'$2^x$ overtakes $x^2$ at $x=4$', xy=(4, 16), xytext=(5.8, 8),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5), fontsize=14,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax.annotate(r'$\ln x$ crawls — only 2.30 at $x=10$', xy=(7.5, np.log(7.5)),
            xytext=(3.5, 0.5), arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
            fontsize=14, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 55)
ax.set_xlabel('x', fontsize=16)
ax.set_ylabel('y', fontsize=16)
fig.suptitle('A Race Between Growth Types: $x$, $x^2$, $2^x$, $\ln x$', fontsize=18, fontweight='bold')
ax.legend(fontsize=14, loc='upper left')
ax.grid(alpha=0.3)
ax.tick_params(labelsize=13)
plt.tight_layout()
plt.savefig(OUT + '10h-growth-race.png', dpi=180, bbox_inches='tight')
plt.close()
print("10h done")


# ================================================================
# SESSION 11 — TRIGONOMETRY
# ================================================================

# --- 11f: Unwrapping Circle into Sine Wave (TALL, BIG) ---
fig = plt.figure(figsize=(15, 11))
ax_circle = fig.add_axes([0.08, 0.50, 0.40, 0.45])
theta_c = np.linspace(0, 2*np.pi, 400)
ax_circle.plot(np.cos(theta_c), np.sin(theta_c), 'k-', linewidth=2.5)
ax_circle.axhline(0, color='gray', linewidth=0.6)
ax_circle.axvline(0, color='gray', linewidth=0.6)
tp = np.pi/4
xp, yp = np.cos(tp), np.sin(tp)
ax_circle.plot([0, xp], [0, yp], 'r-', linewidth=3, alpha=0.8)
ax_circle.scatter([xp], [yp], s=180, c='red', zorder=5)
ax_circle.plot([xp, xp], [0, yp], 'r--', linewidth=1.2, alpha=0.6)
ax_circle.plot([0, xp], [0, 0], 'r--', linewidth=1.2, alpha=0.6)
ax_circle.text(xp + 0.1, yp/2, r'$\sin\theta$', fontsize=16, color='red')
ax_circle.text(xp/2 - 0.05, -0.15, r'$\cos\theta$', fontsize=16, color='red')
ax_circle.set_aspect('equal')
ax_circle.set_xlim(-1.4, 1.4)
ax_circle.set_ylim(-1.4, 1.4)
ax_circle.set_title(r'Unit Circle — Point at $\theta = \pi/4$', fontsize=16, fontweight='bold')
ax_circle.grid(alpha=0.2)
ax_circle.tick_params(labelsize=12)

ax_sine = fig.add_axes([0.08, 0.06, 0.88, 0.38])
theta = np.linspace(0, 4*np.pi, 1000)
ax_sine.plot(theta, np.sin(theta), 'b-', linewidth=3.5, label=r'$y = \sin\theta$')
ax_sine.scatter([tp], [np.sin(tp)], s=180, c='red', zorder=5)
ax_sine.axvline(tp, color='red', linestyle='--', linewidth=1, alpha=0.5)
for t_val, label in [(0, '0'), (np.pi/2, r'$\pi/2$'), (np.pi, r'$\pi$'),
                       (3*np.pi/2, r'$3\pi/2$'), (2*np.pi, r'$2\pi$'),
                       (5*np.pi/2, r'$5\pi/2$'), (3*np.pi, r'$3\pi$')]:
    ax_sine.axvline(t_val, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax_sine.text(t_val, -1.55, label, ha='center', fontsize=13)
ax_sine.axhline(0, color='gray', linewidth=0.6)
ax_sine.set_xlim(0, 4*np.pi)
ax_sine.set_ylim(-1.6, 1.6)
ax_sine.set_xlabel(r'$\theta$ (angle / time)', fontsize=16)
ax_sine.set_ylabel(r'$\sin\theta$ (height)', fontsize=16)
ax_sine.set_title('Sine Wave — The Circle Unwrapped', fontsize=16, fontweight='bold')
ax_sine.grid(alpha=0.2)
ax_sine.tick_params(labelsize=12)
fig.suptitle('Unwrapping the Unit Circle into the Sine Wave', fontsize=20, fontweight='bold')
plt.savefig(OUT + '11f-unwrapping-circle.png', dpi=180, bbox_inches='tight')
plt.close()
print("11f done")

# --- 11g1, 11g2, 11g3: Reference Angle — ONE PER QUADRANT ---
def draw_ref_angle(ax, angle_deg, quad, title):
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=2.5)
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    rad = np.deg2rad(angle_deg)
    ax.plot([0, 1.2*np.cos(rad)], [0, 1.2*np.sin(rad)], 'b-', linewidth=4)
    ax.scatter([np.cos(rad)], [np.sin(rad)], s=200, c='blue', zorder=5)
    if quad == 2:
        ra = np.deg2rad(180 - angle_deg)
        arc = np.linspace(np.pi - ra, np.pi, 60)
    elif quad == 3:
        ra = np.deg2rad(angle_deg - 180)
        arc = np.linspace(np.pi, np.pi + ra, 60)
    else:
        ra = np.deg2rad(360 - angle_deg)
        arc = np.linspace(2*np.pi - ra, 2*np.pi, 60)
    ax.plot(0.35*np.cos(arc), 0.35*np.sin(arc), 'r-', linewidth=4)
    mid = (arc[0] + arc[-1]) / 2
    ax.text(0.5*np.cos(mid), 0.5*np.sin(mid), r'$\theta_R = 30^\circ$',
            fontsize=18, color='red', fontweight='bold', ha='center')
    ax.set_aspect('equal')
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    signs = {2: r'$\sin$: +    $\cos$: $-$',
             3: r'$\sin$: $-$    $\cos$: $-$',
             4: r'$\sin$: $-$    $\cos$: +'}
    ax.text(0.05, -0.15, signs[quad], transform=ax.transAxes, fontsize=16,
            ha='center', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.grid(alpha=0.15)
    ax.tick_params(labelsize=12)

for angle, quad, title, fname in [
    (150, 2, r'Quadrant II: $\theta = 150^\circ$', '11g1-reference-angle-q2.png'),
    (210, 3, r'Quadrant III: $\theta = 210^\circ$', '11g2-reference-angle-q3.png'),
    (330, 4, r'Quadrant IV: $\theta = 330^\circ$', '11g3-reference-angle-q4.png'),
]:
    fig, ax = plt.subplots(figsize=SQ)
    draw_ref_angle(ax, angle, quad, title)
    plt.tight_layout()
    plt.savefig(OUT + fname, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"{fname} done")

# --- 11h: Tangent as Slope (BIGGER) ---
fig, ax = plt.subplots(figsize=SQ)
theta_c = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', linewidth=2.5)
angles = [np.pi/6, np.pi/4, np.pi/3, 2*np.pi/3, 5*np.pi/4, 11*np.pi/6]
colors = ['blue', 'green', 'purple', 'orange', 'brown', 'teal']
for ang, col in zip(angles, colors):
    ax.plot([0, 1.25*np.cos(ang)], [0, 1.25*np.sin(ang)], '-',
            color=col, linewidth=3.5, alpha=0.85)
    slope = np.tan(ang)
    deg = int(round(ang * 180 / np.pi))
    ax.text(1.35*np.cos(ang), 1.35*np.sin(ang),
            f'{deg}°\ntan = {slope:.2f}',
            fontsize=12, color=col, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.85))
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.8)
ax.set_ylim(-1.5, 2.5)
ax.set_title(r'$\tan\theta$ = Slope of the Radius', fontsize=18, fontweight='bold')
ax.grid(alpha=0.2)
ax.tick_params(labelsize=12)
ax.text(-1.3, 2.2,
        r'Slope = rise / run = $\sin\theta / \cos\theta = \tan\theta$',
        fontsize=14, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
plt.tight_layout()
plt.savefig(OUT + '11h-tangent-as-slope.png', dpi=180, bbox_inches='tight')
plt.close()
print("11h done")

# --- 11i: Pythagorean Proof (BIGGER) ---
fig, ax = plt.subplots(figsize=SQ)
theta_c = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', linewidth=2.5)
td = np.deg2rad(50)
xp, yp = np.cos(td), np.sin(td)
ax.plot([0, xp], [0, 0], 'b-', linewidth=5, label=f'adjacent = cos = {xp:.2f}')
ax.plot([xp, xp], [0, yp], 'r-', linewidth=5, label=f'opposite = sin = {yp:.2f}')
ax.plot([0, xp], [0, yp], 'darkgreen', linewidth=5, label='hypotenuse = radius = 1')
s = 0.1
ax.plot([xp-s, xp-s], [0, s], 'k-', linewidth=1.5)
ax.plot([xp-s, xp], [s, s], 'k-', linewidth=1.5)
ax.set_aspect('equal')
ax.set_xlim(-1.4, 1.6)
ax.set_ylim(-0.3, 1.5)
ax.set_title(r'$\sin^2\theta + \cos^2\theta = 1$ — Pythagorean Theorem', fontsize=18, fontweight='bold')
ax.legend(fontsize=14, loc='lower left')
ax.grid(alpha=0.2)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.tick_params(labelsize=12)
ax.text(0.05, 0.92, r'$(y/1)^2 + (x/1)^2 = 1^2$',
        transform=ax.transAxes, fontsize=16, color='darkred', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
plt.tight_layout()
plt.savefig(OUT + '11i-pythagorean-proof.png', dpi=180, bbox_inches='tight')
plt.close()
print("11i done")

# --- 11j: Complex Plane Rotation (BIGGER) ---
fig, ax = plt.subplots(figsize=SQ)
theta_c = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', linewidth=1.2, alpha=0.35)
za = np.deg2rad(30)
zx, zy = 2.0*np.cos(za), 2.0*np.sin(za)
ax.arrow(0, 0, zx, zy, head_width=0.10, head_length=0.14, fc='blue', ec='blue',
         linewidth=4, label=r'$z = r e^{i\alpha}$', length_includes_head=True)
ra = np.deg2rad(60)
zra = za + ra
zrx, zry = 2.0*np.cos(zra), 2.0*np.sin(zra)
ax.arrow(0, 0, zrx, zry, head_width=0.10, head_length=0.14, fc='red', ec='red',
         linewidth=4, label=r'$z \cdot e^{i\theta}$ (rotated by $\theta$)',
         length_includes_head=True)
arc = mpatches.Arc((0, 0), 1.4, 1.4, angle=0,
                    theta1=np.rad2deg(za), theta2=np.rad2deg(zra),
                    color='darkgreen', linewidth=4)
ax.add_patch(arc)
ma = za + ra/2
ax.text(1.15*np.cos(ma), 1.15*np.sin(ma), r'$\theta = 60^\circ$', fontsize=18,
        color='darkgreen', fontweight='bold', ha='center')
ax.set_aspect('equal')
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.4, 2.4)
ax.set_xlabel('Real', fontsize=16)
ax.set_ylabel('Imaginary', fontsize=16)
ax.set_title(r'$e^{i\theta}$ is a Rotation Operator', fontsize=18, fontweight='bold')
ax.legend(fontsize=13, loc='upper left')
ax.grid(alpha=0.2)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.tick_params(labelsize=12)
ax.text(0.05, 0.96, r'$e^{i\theta} = \cos\theta + i\sin\theta$' + '\n' +
        'Multiplying by $e^{i\theta}$ rotates any complex number by $\\theta$',
        transform=ax.transAxes, fontsize=15, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
plt.tight_layout()
plt.savefig(OUT + '11j-complex-rotation.png', dpi=180, bbox_inches='tight')
plt.close()
print("11j done")

print("\n=== All FULL-SIZE standalone graphs generated! ===")
