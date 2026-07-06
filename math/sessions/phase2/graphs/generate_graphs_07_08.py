"""
Graphs for Sessions 07 and 08.

07a — Cubic polynomial with 3 real roots
07b — System of equations: line + circle intersection
08a — Quadratic inequality sign chart
08b — Rational inequality sign chart
08c — Absolute value inequality regions
08d — Floor and ceiling inequalities
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle as MplCircle, Arc, FancyBboxPatch
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 07A — Cubic Polynomial with 3 Real Roots
# ================================================================
fig, ax = plt.subplots(figsize=(11, 8))

x = np.linspace(-1.5, 4.5, 400)
y = x**3 - 6*x**2 + 11*x - 6  # roots at 1, 2, 3

ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x)=x^3-6x^2+11x-6$')
ax.axhline(0, color='gray', linewidth=0.8, alpha=0.6)

# Mark roots
for root, color in [(1, 'red'), (2, 'green'), (3, 'darkorange')]:
    ax.plot(root, 0, 'o', color=color, markersize=12, zorder=5)
    ax.annotate(f'x={root}', (root, 0), textcoords='offset points',
                xytext=(0, -20), fontsize=12, color=color, fontweight='bold',
                ha='center')

# Factor annotation
ax.text(2.5, 5, r'$f(x)=(x-1)(x-2)(x-3)$', fontsize=14,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax.text(2.5, 3, r'Sum of roots = $1+2+3=6$ (Vieta)', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('f(x)', fontsize=13)
ax.set_title('Graph 07A: Cubic Polynomial — Three Real Roots\nFactoring Reveals Everything',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
ax.set_xlim(-1.5, 4.5)
ax.set_ylim(-3, 8)
plt.tight_layout()
plt.savefig(OUT + '07a-cubic-roots.png', dpi=180, bbox_inches='tight')
plt.close()
print("07A done")


# ================================================================
# 07B — System of Equations: Line + Circle Intersection
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

# Circle x^2 + y^2 = 25
theta = np.linspace(0, 2*np.pi, 300)
ax.plot(5*np.cos(theta), 5*np.sin(theta), 'b-', linewidth=2.5, label=r'$x^2+y^2=25$')

# Line y = 7-2x (from 2x+y=7)
x_line = np.linspace(-6, 7, 200)
y_line = 7 - 2*x_line
ax.plot(x_line, y_line, 'r-', linewidth=2.5, label=r'$2x+y=7$')

# Intersection points
# (6/5, 23/5) = (1.2, 4.6) and (4, -1)
for pt, label in [((1.2, 4.6), r'$(\frac{6}{5},\frac{23}{5})$'), ((4, -1), r'$(4,-1)$')]:
    ax.plot(pt[0], pt[1], 'o', color='darkred', markersize=12, zorder=5)
    ax.annotate(label, pt, textcoords='offset points', xytext=(10, 10),
                fontsize=12, color='darkred', fontweight='bold')

ax.set_aspect('equal')
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 07B: System of Equations — Line Meets Circle\nSubstitution Solves the Intersection',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(alpha=0.15)
ax.axhline(0, color='gray', lw=0.4)
ax.axvline(0, color='gray', lw=0.4)
plt.tight_layout()
plt.savefig(OUT + '07b-system-intersection.png', dpi=180, bbox_inches='tight')
plt.close()
print("07B done")


# ================================================================
# 08A — Quadratic Inequality Sign Chart
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))
ax1, ax2 = axes

# Left: graph
x = np.linspace(-1, 5, 400)
y = x**2 - 5*x + 6
ax1.plot(x, y, 'b-', linewidth=2.5)
ax1.axhline(0, color='gray', linewidth=0.8)
ax1.fill_between(x, 0, y, where=(y > 0), alpha=0.25, color='steelblue',
                  label='y>0 (solution)')
ax1.fill_between(x, 0, y, where=(y < 0), alpha=0.25, color='coral',
                  label='y<0 (excluded)')
ax1.plot([2, 2], [-2, 0], 'r--', linewidth=1, alpha=0.7)
ax1.plot([3, 3], [-2, 0], 'r--', linewidth=1, alpha=0.7)
ax1.plot([2, 3], [0, 0], 'ro', markersize=8)
ax1.set_title(r'$x^2-5x+6>0$: Above x-axis', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(alpha=0.12)

# Right: sign chart
ax2.set_xlim(-1, 5)
ax2.set_ylim(-0.5, 2)
ax2.axhline(1, color='black', linewidth=2)
ax2.plot([2, 2], [0.6, 1.4], 'k-', linewidth=1.5)
ax2.plot([3, 3], [0.6, 1.4], 'k-', linewidth=1.5)

# Signs
for x_pos, sign, color in [(0.5, '+', 'steelblue'), (2.5, '−', 'coral'), (4, '+', 'steelblue')]:
    ax2.text(x_pos, 1, sign, fontsize=20, ha='center', va='center',
             color=color, fontweight='bold')

ax2.annotate('', xy=(2, 0.5), xytext=(-1, 0.5),
            arrowprops=dict(arrowstyle='<-', color='steelblue', lw=2))
ax2.annotate('', xy=(5, 0.5), xytext=(3, 0.5),
            arrowprops=dict(arrowstyle='<-', color='steelblue', lw=2))
ax2.text(0.5, 0.3, 'x<2', fontsize=12, ha='center')
ax2.text(4, 0.3, 'x>3', fontsize=12, ha='center')

ax2.set_title('Sign chart: + on (−∞,2) and (3,∞)', fontsize=12, fontweight='bold')
ax2.set_yticks([])
ax2.grid(alpha=0.1)

fig.suptitle('Graph 08A: Quadratic Inequality — Sign Chart Method',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '08a-sign-chart.png', dpi=180, bbox_inches='tight')
plt.close()
print("08A done")


# ================================================================
# 08B — Rational Inequality Sign Chart
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))
ax1, ax2 = axes

# Left: graph of (x-1)/(x+2)
x = np.linspace(-5, -2.05, 200)
x2 = np.linspace(-1.95, 5, 300)
y1 = (x-1)/(x+2)
y2 = (x2-1)/(x2+2)
ax1.plot(x, y1, 'b-', linewidth=2.2)
ax1.plot(x2, y2, 'b-', linewidth=2.2)
ax1.axhline(0, color='gray', linewidth=0.8)
ax1.axvline(-2, color='red', linestyle='--', linewidth=1.5, alpha=0.8,
            label='x=−2 (excluded)')
ax1.fill_between(x, 0, y1, where=(y1>0), alpha=0.15, color='steelblue')
ax1.fill_between(x2, 0, y2, where=(y2>0), alpha=0.15, color='steelblue')
ax1.plot(1, 0, 'go', markersize=10, label='x=1 (numerator=0)')
ax1.set_ylim(-5, 5)
ax1.set_title(r'$y=\frac{x-1}{x+2}$', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(alpha=0.12)

# Right: sign chart
ax2.set_xlim(-5, 3)
ax2.set_ylim(-0.5, 2.5)
ax2.axhline(1, color='black', linewidth=2)
ax2.plot([-2, -2], [0.6, 1.4], 'r-', linewidth=2)
ax2.plot([1, 1], [0.6, 1.4], 'g-', linewidth=2)
ax2.text(-2, 0.5, 'den=0', fontsize=10, ha='center', color='red')
ax2.text(1, 0.5, 'num=0', fontsize=10, ha='center', color='green')

for x_pos, sign in [(-3.5, '+'), (0, '−'), (2, '+')]:
    color = 'steelblue' if sign == '+' else 'coral'
    ax2.text(x_pos, 1, sign, fontsize=20, ha='center', va='center',
             color=color, fontweight='bold')

ax2.set_title('Sign chart: (+) (−) (+) → x<−2 or x>1', fontsize=12, fontweight='bold')
ax2.set_yticks([])
ax2.grid(alpha=0.1)

fig.suptitle('Graph 08B: Rational Inequality — Sign Chart with Denominator Exclusion',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '08b-rational-inequality.png', dpi=180, bbox_inches='tight')
plt.close()
print("08B done")


# ================================================================
# 08C — Absolute Value Inequality: Regions
# ================================================================
fig, ax = plt.subplots(figsize=(12, 7))

x = np.linspace(-2, 6, 500)
y = np.abs(x-1) + np.abs(x-3)

ax.plot(x, y, 'b-', linewidth=2.8, label=r'$f(x)=|x-1|+|x-3|$')
ax.axhline(4, color='gray', linestyle='--', linewidth=1.5, alpha=0.7,
           label='y=4 (threshold)')

# Shade solution region
ax.fill_between(x, 0, y, where=(y < 4), alpha=0.25, color='steelblue',
                 label='f(x)<4 → 0<x<4')

# Critical points
for pt in [1, 3]:
    ax.axvline(pt, color='red', linestyle=':', linewidth=1.2, alpha=0.6)
    ax.plot(pt, 2, 'ro', markersize=8)
    ax.text(pt, -0.3, f'x={pt}', fontsize=11, ha='center', color='red')

ax.text(2, 3, 'Solution:\n0 < x < 4', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax.set_xlim(-2, 6)
ax.set_ylim(-0.5, 8)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('f(x)', fontsize=13)
ax.set_title('Graph 08C: Two Absolute Values — $|x-1|+|x-3|<4$\nSplit into 3 regions at x=1 and x=3',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.12)
plt.tight_layout()
plt.savefig(OUT + '08c-absolute-value-regions.png', dpi=180, bbox_inches='tight')
plt.close()
print("08C done")


# ================================================================
# 08D — Floor and Ceiling Inequalities
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))
ax1, ax2 = axes

# Floor function
x = np.linspace(-2, 5, 800)
y_floor = np.floor(x)
ax1.step(x, y_floor, 'b-', linewidth=2.2, where='post', label=r'$\lfloor x\rfloor$')
ax1.scatter(np.arange(-2, 6), np.arange(-2, 6), c='blue', s=50, zorder=5)
ax1.scatter(np.arange(-1, 6), np.arange(-2, 5), c='white', s=50, zorder=5,
            edgecolors='blue', linewidths=1.5)

# Shade region where floor(x) >= 2
x_fill = np.linspace(2, 5, 100)
ax1.fill_between(x_fill, 0, 6, alpha=0.2, color='steelblue')
ax1.text(3.5, 3.5, r'$\lfloor x\rfloor \geq 2$', fontsize=13, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax1.set_title(r'Floor: $\lfloor x\rfloor \geq 2 \Longleftrightarrow x \geq 2$', fontsize=12, fontweight='bold')
ax1.set_xlim(-2, 5); ax1.set_ylim(-2.5, 5.5)
ax1.legend(fontsize=10); ax1.grid(alpha=0.12)

# Ceiling + fractional part
x2 = np.linspace(-2, 4, 700)
y_ceil = np.ceil(x2)
y_frac = x2 - np.floor(x2)
ax2.plot(x2, y_frac, 'purple', linewidth=2, label=r'$\{x\}=x-\lfloor x\rfloor$')
ax2.fill_between(x2, 0, y_frac, alpha=0.12, color='purple')

# Shade {x} > 0.5
for n in range(-2, 5):
    x_fill = np.linspace(n+0.5, n+1, 50)
    ax2.fill_between(x_fill, 0, 1, alpha=0.25, color='orange')

ax2.text(1, 0.75, r'$\{x\}>0.5$', fontsize=12, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax2.set_title(r'Fractional part: $\{x\}>0.5$ — shaded bands', fontsize=12,
             fontweight='bold')
ax2.set_xlim(-2, 4); ax2.set_ylim(-0.1, 1.2)
ax2.legend(fontsize=10); ax2.grid(alpha=0.12)

fig.suptitle('Graph 08D: Floor, Ceiling, and Fractional Part Inequalities',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '08d-floor-ceiling.png', dpi=180, bbox_inches='tight')
plt.close()
print("08D done")

print("\n=== ALL 07+08 GRAPHS GENERATED ===")
