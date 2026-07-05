import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

output_dir = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

# ============================================================
# Graph 1: y = x^3 - 4x (odd function, polynomial)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-3, 3, 600)
y = x**3 - 4*x
ax.plot(x, y, 'b-', linewidth=2, label=r'$y = x^3 - 4x$')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.scatter([-2, 0, 2], [0, 0, 0], s=60, c='red', zorder=5, label='x intercepts')
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-5, 5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graph 1: $y = x^3 - 4x$ (Odd function, origin symmetric)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '01-cubic-poly.png', dpi=150)
plt.close()
print("Graph 1 done")

# ============================================================
# Graph 2: y = (x^2 - x - 2)/(x^2 - 4)  — rational with hole
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Wide view
x_wide = np.linspace(-8, 8, 1000)
# Exclude x=-2 for vertical asymptote
mask = np.abs(x_wide - (-2)) > 0.05
x_far1 = x_wide[x_wide < -2.5]
x_far2 = x_wide[(x_wide > -1.5) & (x_wide < 1.8)]
x_far3 = x_wide[x_wide > 2.2]

for ax, x_range in [(ax1, [x_far1, x_far2, x_far3])]:
    for xs in x_range:
        y = (xs**2 - xs - 2) / (xs**2 - 4)
        ax.plot(xs, y, 'b-', linewidth=1.5)

for ax in [ax1, ax2]:
    ax.axhline(1, color='gray', linestyle='--', linewidth=0.8, label='y=1 (horizontal)')
    ax.axvline(-2, color='red', linestyle='--', linewidth=0.8, label='x=-2 (vertical)')
    ax.axhline(0, color='black', linewidth=0.4)
    ax.axvline(0, color='black', linewidth=0.4)
    # hole at (2, 0.75)
    ax.scatter([2], [0.75], s=100, facecolors='none', edgecolors='red', linewidths=2, zorder=10, label='hole at x=2')
    # x-intercept at -1
    ax.scatter([-1], [0], s=50, c='green', zorder=5, label='x-intercept: -1')
    # y-intercept
    ax.scatter([0], [0.5], s=50, c='orange', zorder=5, label='y-intercept: 0.5')

ax1.set_xlim(-8, 8)
ax1.set_ylim(-3, 4)
ax1.set_title('Wide view')
ax1.legend(fontsize=7)
ax1.grid(True, alpha=0.2)

# Zoomed view
x_zoom_left = np.linspace(-3.5, -2.1, 300)
x_zoom_mid = np.linspace(-1.9, 1.9, 400)
x_zoom_right = np.linspace(2.1, 4, 200)
for xs in [x_zoom_left, x_zoom_mid, x_zoom_right]:
    y = (xs**2 - xs - 2) / (xs**2 - 4)
    ax2.plot(xs, y, 'b-', linewidth=1.5)

ax2.set_xlim(-3.5, 4)
ax2.set_ylim(-2, 3)
ax2.set_title('Zoomed view')
ax2.legend(fontsize=7)
ax2.grid(True, alpha=0.2)

plt.suptitle(r'Graph 2: $y = \frac{x^2 - x - 2}{x^2 - 4}$ (hole at x=2)', fontsize=13)
plt.tight_layout()
plt.savefig(output_dir + '02-rational-hole.png', dpi=150)
plt.close()
print("Graph 2 done")

# ============================================================
# Graph 3: y = (x^2+2x)/(x-1)  — slant asymptote
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
x_left = np.linspace(-6, 0.85, 500)
x_right = np.linspace(1.15, 6, 500)
y_left = (x_left**2 + 2*x_left) / (x_left - 1)
y_right = (x_right**2 + 2*x_right) / (x_right - 1)
ax.plot(x_left, y_left, 'b-', linewidth=1.8)
ax.plot(x_right, y_right, 'b-', linewidth=1.8, label=r'$y = \frac{x^2+2x}{x-1}$')

# slant asymptote y = x + 3
x_slant = np.linspace(-6, 6, 100)
ax.plot(x_slant, x_slant + 3, 'g--', linewidth=1.2, label=r'slant: $y = x+3$')
ax.axvline(1, color='red', linestyle='--', linewidth=0.8, label='vertical: x=1')
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.scatter([-2, 0], [0, 0], s=60, c='red', zorder=5, label='x-intercepts: -2, 0')
ax.set_xlim(-6, 6)
ax.set_ylim(-10, 15)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 3: $y = \frac{x^2+2x}{x-1}$ (slant asymptote)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '03-slant-asymptote.png', dpi=150)
plt.close()
print("Graph 3 done")

# ============================================================
# Graph 4: y = sqrt(x-1) + 2  — square root, shifted
# ============================================================
fig, ax = plt.subplots(figsize=(7, 5))
x = np.linspace(1, 10, 400)
y = np.sqrt(x - 1) + 2
ax.plot(x, y, 'b-', linewidth=2, label=r'$y = \sqrt{x-1} + 2$')
ax.scatter([1], [2], s=80, c='red', zorder=5, label='start: (1, 2)')
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.set_xlim(-0.5, 10)
ax.set_ylim(0, 6)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 4: $y = \sqrt{x-1} + 2$ (shifted square root)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '04-sqrt-shifted.png', dpi=150)
plt.close()
print("Graph 4 done")

# ============================================================
# Graph 5: Floor function [x] — staircase
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-3, 4, 1000)
y_floor = np.floor(x)
# Plot as segments
for i in range(-3, 4):
    xs = np.linspace(i, i+0.999, 100)
    ax.plot(xs, np.full_like(xs, i), 'b-', linewidth=2)
    ax.scatter([i], [i], s=50, c='blue', zorder=5)  # filled left
    ax.scatter([i+1], [i], s=50, facecolors='none', edgecolors='blue', linewidths=1.5, zorder=5)  # empty right

ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.set_xlim(-3.5, 4.5)
ax.set_ylim(-3.5, 4.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 5: $y = [x]$ (floor function — staircase)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '05-floor-function.png', dpi=150)
plt.close()
print("Graph 5 done")

# ============================================================
# Graph 6: Fractional part {x} — sawtooth
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-2, 4, 2000)
y_frac = x - np.floor(x)
ax.plot(x, y_frac, 'b-', linewidth=1.5, label=r'$\{x\} = x - [x]$')
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.axhline(1, color='gray', linestyle=':', linewidth=0.6, alpha=0.5)
ax.set_xlim(-2.5, 4.5)
ax.set_ylim(-0.2, 1.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 6: $y = \{x\}$ (fractional part — sawtooth)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '06-frac-part.png', dpi=150)
plt.close()
print("Graph 6 done")

# ============================================================
# Graph 7: ceiling and sign functions
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Ceiling
x = np.linspace(-3, 4, 1000)
y_ceil = np.ceil(x)
for i in range(-3, 5):
    xs = np.linspace(i-0.999, i, 100)
    ax1.plot(xs, np.full_like(xs, i), 'b-', linewidth=2)
    if i > -3:
        ax1.scatter([i-1], [i], s=50, facecolors='none', edgecolors='blue', linewidths=1.5, zorder=5)  # empty left
    ax1.scatter([i], [i], s=50, c='blue', zorder=5)  # filled right

ax1.axhline(0, color='black', linewidth=0.4)
ax1.axvline(0, color='black', linewidth=0.4)
ax1.set_xlim(-3.5, 4.5)
ax1.set_ylim(-3.5, 4.5)
ax1.set_xlabel('x')
ax1.set_title(r'$\lceil x \rceil$ (ceiling)')
ax1.grid(True, alpha=0.3)

# Sign function
x_neg = np.linspace(-3, -0.02, 200)
x_zero = [0]
x_pos = np.linspace(0.02, 3, 200)
ax2.plot(x_neg, np.full_like(x_neg, -1), 'b-', linewidth=2)
ax2.scatter([0], [0], s=70, c='blue', zorder=5)
ax2.plot(x_pos, np.full_like(x_pos, 1), 'b-', linewidth=2)
ax2.scatter([0], [-1], s=50, facecolors='none', edgecolors='blue', linewidths=1.5, zorder=5)
ax2.scatter([0], [1], s=50, facecolors='none', edgecolors='blue', linewidths=1.5, zorder=5)

ax2.axhline(0, color='black', linewidth=0.4)
ax2.axvline(0, color='black', linewidth=0.4)
ax2.set_xlim(-3.5, 3.5)
ax2.set_ylim(-1.8, 1.8)
ax2.set_xlabel('x')
ax2.set_title(r'$\mathrm{sgn}(x)$ (sign)')
ax2.grid(True, alpha=0.3)

plt.suptitle('Graph 7: Ceiling & Sign Functions', fontsize=13)
plt.tight_layout()
plt.savefig(output_dir + '07-ceiling-sign.png', dpi=150)
plt.close()
print("Graph 7 done")

# ============================================================
# Graph 8: Absolute value transformations
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Original: y = x^2 - 1
x = np.linspace(-2.5, 2.5, 500)
ax = axes[0, 0]
ax.plot(x, x**2 - 1, 'b-', linewidth=2)
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.fill_between(x, x**2 - 1, 0, where=(x**2 - 1 < 0), color='red', alpha=0.15)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 5)
ax.set_title(r'Original: $y = x^2 - 1$')
ax.grid(True, alpha=0.3)

# |f(x)|: y = |x^2 - 1|
ax = axes[0, 1]
ax.plot(x, np.abs(x**2 - 1), 'b-', linewidth=2)
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.5, 5)
ax.set_title(r'$y = |x^2 - 1|$ (fold up)')
ax.grid(True, alpha=0.3)

# f(|x|): y = |x|^2 - 1 = x^2 - 1 (same for x^2)
# Better: use f(x) = x^2 - 2x
x_pos = np.linspace(0, 3, 300)
ax = axes[1, 0]
y_orig = x_pos**2 - 2*x_pos
ax.plot(x_pos, y_orig, 'b-', linewidth=2, label='x >= 0')
ax.plot(-x_pos, y_orig, 'r--', linewidth=1.5, alpha=0.7, label='x < 0 (mirror)')
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-1.5, 4)
ax.set_title(r'$y = f(|x|) = |x|^2 - 2|x|$ (mirror)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Scaling: sin(x), 2sin(x), sin(2x)
ax = axes[1, 1]
x = np.linspace(0, 4*np.pi, 500)
ax.plot(x, np.sin(x), 'b-', linewidth=1.5, label=r'$\sin x$')
ax.plot(x, 2*np.sin(x), 'g--', linewidth=1.2, label=r'$2\sin x$ (height x2)')
ax.plot(x, np.sin(2*x), 'r-.', linewidth=1.2, label=r'$\sin 2x$ (period /2)')
ax.axhline(0, color='black', linewidth=0.4)
ax.set_xlim(0, 4*np.pi)
ax.set_ylim(-2.5, 2.5)
ax.set_title('Scaling: $a \\cdot \\sin(bx)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xticks([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
ax.set_xticklabels(['0', 'π', '2π', '3π', '4π'])

plt.suptitle('Graph 8: Absolute Value & Scaling Transformations', fontsize=13)
plt.tight_layout()
plt.savefig(output_dir + '08-transformations.png', dpi=150)
plt.close()
print("Graph 8 done")

# ============================================================
# Graph 9: Piecewise function
# ============================================================
fig, ax = plt.subplots(figsize=(8, 5))

# Piece 1: x+2 for x <= 0
x1 = np.linspace(-4, 0, 200)
ax.plot(x1, x1+2, 'b-', linewidth=2, label='x+2 (x ≤ 0)')
ax.scatter([0], [2], s=60, c='blue', zorder=5)  # filled at boundary

# Piece 2: 4 - x^2 for 0 < x <= 2
x2 = np.linspace(0.02, 2, 200)
ax.plot(x2, 4 - x2**2, 'g-', linewidth=2, label='4−x² (0 < x ≤ 2)')
ax.scatter([0], [4], s=60, facecolors='none', edgecolors='green', linewidths=2, zorder=5)  # empty at start
ax.scatter([2], [0], s=60, c='green', zorder=5)  # filled at end

# Piece 3: 1/(x-2) for x > 2
x3a = np.linspace(2.15, 5, 300)
ax.plot(x3a, 1/(x3a-2), 'r-', linewidth=2, label='1/(x−2) (x > 2)')
ax.axvline(2, color='gray', linestyle=':', linewidth=0.8, alpha=0.5)

ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.set_xlim(-4.5, 5.5)
ax.set_ylim(-3, 6)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graph 9: Piecewise Function (3 pieces, discontinuity at x=0)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '09-piecewise.png', dpi=150)
plt.close()
print("Graph 9 done")

# ============================================================
# Graph 10: Mixed — y = x + [x] and y = x{x}
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# y = x + [x]
x = np.linspace(-2.5, 3.5, 2000)
y1 = x + np.floor(x)
ax1.plot(x, y1, 'b-', linewidth=1.2, label=r'$y = x + [x]$')
ax1.axhline(0, color='black', linewidth=0.4)
ax1.axvline(0, color='black', linewidth=0.4)
ax1.set_xlim(-2.5, 3.5)
ax1.set_ylim(-5, 7)
ax1.set_xlabel('x')
ax1.set_title(r'$y = x + [x]$ (linear in each [n,n+1))')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# y = x * {x}
y2 = x * (x - np.floor(x))
ax2.plot(x, y2, 'b-', linewidth=1.2, label=r'$y = x\{x\}$')
ax2.axhline(0, color='black', linewidth=0.4)
ax2.axvline(0, color='black', linewidth=0.4)
ax2.set_xlim(-2.5, 3.5)
ax2.set_ylim(-0.5, 3.5)
ax2.set_xlabel('x')
ax2.set_title(r'$y = x\{x\}$ (parabolic in each [n,n+1))')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

plt.suptitle('Graph 10: Mixed Floor/Fractional Part Functions', fontsize=13)
plt.tight_layout()
plt.savefig(output_dir + '10-mixed-floor.png', dpi=150)
plt.close()
print("Graph 10 done")

# ============================================================
# Graph 11: Rational with absolute value — f(x) = |x-1|/(x^2-1)
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))

# x < -1
x1 = np.linspace(-4, -1.15, 300)
y1 = np.abs(x1-1) / (x1**2 - 1)
ax.plot(x1, y1, 'b-', linewidth=1.8, label=r'$y = \frac{|x-1|}{x^2-1}$')

# -1 < x < 1
x2 = np.linspace(-0.85, 0.85, 300)
y2 = np.abs(x2-1) / (x2**2 - 1)
ax.plot(x2, y2, 'b-', linewidth=1.8)

# x > 1
x3 = np.linspace(1.15, 5, 300)
y3 = np.abs(x3-1) / (x3**2 - 1)
ax.plot(x3, y3, 'b-', linewidth=1.8)

# hole at (1, 0.5)
ax.scatter([1], [0.5], s=100, facecolors='none', edgecolors='red', linewidths=2, zorder=10, label='hole at (1, 1/2)')
# y-intercept
ax.scatter([0], [-1], s=50, c='orange', zorder=5, label='y-intercept: -1')
# asymptotes
ax.axvline(-1, color='red', linestyle='--', linewidth=0.8, label='vertical: x=-1')
ax.axhline(0, color='gray', linestyle='--', linewidth=0.8, label='horizontal: y=0')
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)

ax.set_xlim(-4.5, 5.5)
ax.set_ylim(-3, 3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 11: $y = \frac{|x-1|}{x^2-1}$ (absolute value + rational)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '11-abs-rational.png', dpi=150)
plt.close()
print("Graph 11 done")

# ============================================================
# Graph 12: Simple rational — y = (2x+1)/(x-1) hyperbola
# ============================================================
fig, ax = plt.subplots(figsize=(8, 6))
x_left = np.linspace(-4, 0.85, 400)
x_right = np.linspace(1.15, 6, 400)
y_left = (2*x_left + 1) / (x_left - 1)
y_right = (2*x_right + 1) / (x_right - 1)
ax.plot(x_left, y_left, 'b-', linewidth=1.8)
ax.plot(x_right, y_right, 'b-', linewidth=1.8, label=r'$y = \frac{2x+1}{x-1}$')
ax.axvline(1, color='red', linestyle='--', linewidth=0.8, label='x=1 (vertical)')
ax.axhline(2, color='green', linestyle='--', linewidth=0.8, label='y=2 (horizontal)')
ax.axhline(0, color='black', linewidth=0.4)
ax.axvline(0, color='black', linewidth=0.4)
ax.scatter([0], [-1], s=60, c='orange', zorder=5, label='y-intercept: -1')
ax.scatter([-0.5], [0], s=60, c='red', zorder=5, label='x-intercept: -1/2')
ax.scatter([1], [2], s=30, c='purple', zorder=5, alpha=0.5, label='center (1,2)')
ax.set_xlim(-4, 6)
ax.set_ylim(-4, 8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 12: $y = \frac{2x+1}{x-1}$ (hyperbola, center at (1,2))')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir + '12-hyperbola.png', dpi=150)
plt.close()
print("Graph 12 done")

print("\n=== All 12 graphs saved to", output_dir, "===")
