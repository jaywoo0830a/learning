import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

output_dir = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

# ============================================================
# Ex2: f(x) = (x^2-4)/(x^2-1) — rational, even, asymptotes at x=±1, y=1
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))

# Left of x=-1
xl1 = np.linspace(-5, -1.08, 500)
yl1 = (xl1**2 - 4) / (xl1**2 - 1)
ax.plot(xl1, yl1, 'b-', linewidth=2)

# Between -1 and 1
xl2 = np.linspace(-0.92, 0.92, 500)
yl2 = (xl2**2 - 4) / (xl2**2 - 1)
ax.plot(xl2, yl2, 'b-', linewidth=2)

# Right of x=1
xl3 = np.linspace(1.08, 5, 500)
yl3 = (xl3**2 - 4) / (xl3**2 - 1)
ax.plot(xl3, yl3, 'b-', linewidth=2, label=r'$f(x)=\frac{x^2-4}{x^2-1}$')

# Asymptotes
ax.axvline(-1, color='red', linestyle='--', linewidth=1.2)
ax.axvline(1, color='red', linestyle='--', linewidth=1.2, label=r'$x=\pm1$ (vertical)')
ax.axhline(1, color='green', linestyle='--', linewidth=1.2, label=r'$y=1$ (horizontal)')

# Intercepts
ax.scatter([-2, 2], [0, 0], s=80, c='red', zorder=10, label=r'$x$-intercepts: $(\pm2,0)$')
ax.scatter([0], [4], s=80, c='orange', zorder=10, label=r'$y$-intercept: $(0,4)$')

# Axis
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-5, 9)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Exercise 2: $f(x) = \frac{x^2-4}{x^2-1}$ (Even, symmetric about $y$-axis)')
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.25)
plt.tight_layout()
plt.savefig(output_dir + 'sol09-ex2-rational.png', dpi=150)
plt.close()
print("Ex2 done")

# ============================================================
# Ex3: f1(x)=x/(x-2) and f2(x)=(x+2)/(x-2) — two hyperbolas
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# f1: y = x/(x-2)
x_l1 = np.linspace(-4, 1.88, 400)
x_r1 = np.linspace(2.12, 8, 400)
y_l1 = x_l1 / (x_l1 - 2)
y_r1 = x_r1 / (x_r1 - 2)
ax1.plot(x_l1, y_l1, 'b-', linewidth=2)
ax1.plot(x_r1, y_r1, 'b-', linewidth=2, label=r'$f_1(x)=\frac{x}{x-2}$')
ax1.axvline(2, color='red', linestyle='--', linewidth=1.2, label=r'$x=2$')
ax1.axhline(1, color='green', linestyle='--', linewidth=1.2, label=r'$y=1$')
ax1.scatter([0], [0], s=80, c='orange', zorder=10, label=r'$(0,0)$')
ax1.axhline(0, color='black', linewidth=0.4)
ax1.axvline(0, color='black', linewidth=0.4)
ax1.set_xlim(-4, 8)
ax1.set_ylim(-3, 5)
ax1.set_title(r'$f_1(x) = \frac{x}{x-2}$')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.2)

# f2: y = (x+2)/(x-2)
x_l2 = np.linspace(-6, 1.88, 400)
x_r2 = np.linspace(2.12, 8, 400)
y_l2 = (x_l2 + 2) / (x_l2 - 2)
y_r2 = (x_r2 + 2) / (x_r2 - 2)
ax2.plot(x_l2, y_l2, 'purple', linewidth=2)
ax2.plot(x_r2, y_r2, 'purple', linewidth=2, label=r'$f_2(x)=\frac{x+2}{x-2}$')
ax2.axvline(2, color='red', linestyle='--', linewidth=1.2, label=r'$x=2$')
ax2.axhline(1, color='green', linestyle='--', linewidth=1.2, label=r'$y=1$')
ax2.scatter([-2], [0], s=80, c='red', zorder=10, label=r'$(-2,0)$')
ax2.scatter([0], [-1], s=80, c='orange', zorder=10, label=r'$(0,-1)$')
ax2.axhline(0, color='black', linewidth=0.4)
ax2.axvline(0, color='black', linewidth=0.4)
ax2.set_xlim(-6, 8)
ax2.set_ylim(-3, 5)
ax2.set_title(r'$f_2(x) = \frac{x+2}{x-2}$')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.2)

plt.suptitle('Exercise 3: Two Hyperbolas with Same Asymptotes $x=2$, $y=1$', fontsize=13)
plt.tight_layout()
plt.savefig(output_dir + 'sol09-ex3-two-hyperbolas.png', dpi=150)
plt.close()
print("Ex3 done")

# ============================================================
# Ex4: f(x) = [x] + {x}^2 on [-2, 3]
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

intervals = [(-2, -1), (-1, 0), (0, 1), (1, 2), (2, 3)]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for (n_start, n_end), color in zip(intervals, colors):
    n = n_start
    # On [n, n+1): f(x) = n + (x-n)^2
    x_vals = np.linspace(n_start, n_end - 0.001, 300)
    y_vals = n + (x_vals - n)**2
    ax.plot(x_vals, y_vals, color=color, linewidth=2.5,
            label=rf'$[{n},{n+1})$: $f(x)={n}+(x-{n:+d})^2$')

    # Left endpoint (filled)
    if n_start >= -2:
        ax.scatter([n_start], [n + 0], s=60, c=color, zorder=10)

    # Right endpoint (empty)
    ax.scatter([n_end], [n + 1], s=60, facecolors='none', edgecolors=color, linewidths=1.5, zorder=10)

# x=3 (special point from problem: f(3)=3+0^2=3)
ax.scatter([3], [3], s=60, c='#9467bd', zorder=10)

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-2.3, 3.3)
ax.set_ylim(-2.5, 3.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Exercise 4: $f(x) = [x] + \{x\}^2$ on $[-2, 3]$')
ax.legend(fontsize=8, ncol=2)
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig(output_dir + 'sol09-ex4-floor-frac.png', dpi=150)
plt.close()
print("Ex4 done")

# ============================================================
# Ex5: f(x) = (|x|-1)/(x-1)
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

# x >= 0, x != 1: f(x) = 1 (horizontal line with hole at x=1)
x_pos_left = np.linspace(0, 0.98, 200)
x_pos_right = np.linspace(1.02, 5, 200)
ax.plot(x_pos_left, [1]*len(x_pos_left), 'b-', linewidth=2)
ax.plot(x_pos_right, [1]*len(x_pos_right), 'b-', linewidth=2, label=r'$x \geq 0,\ x \neq 1$: $f(x)=1$')

# Hole at (1,1)
ax.scatter([1], [1], s=100, facecolors='none', edgecolors='blue', linewidths=2, zorder=10, label='Hole at $(1,1)$')

# x < 0: f(x) = (-x-1)/(x-1)
x_neg = np.linspace(-8, -0.02, 500)
y_neg = (-x_neg - 1) / (x_neg - 1)
ax.plot(x_neg, y_neg, 'purple', linewidth=2, label=r'$x < 0$: $f(x)=\frac{-x-1}{x-1}$')

# Asymptote: x=1 for the negative branch (but x<0, so not really relevant)
# Horizontal asymptote as x -> -inf: y = -1
ax.axhline(-1, color='red', linestyle='--', linewidth=1, label=r'$y=-1$ (as $x\to-\infty$)')

# Key points
ax.scatter([0], [1], s=80, c='orange', zorder=10, label=r'$(0,1)$')
ax.scatter([-1], [0], s=80, c='green', zorder=10, label=r'$(-1,0)$')

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-8.5, 5.5)
ax.set_ylim(-3, 3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Exercise 5: $f(x) = \frac{|x|-1}{x-1}$')
ax.legend(fontsize=9, loc='lower right')
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig(output_dir + 'sol09-ex5-abs-rational.png', dpi=150)
plt.close()
print("Ex5 done")

# ============================================================
# Ex6: f(x) = [x]/x on [-3,0) ∪ (0,3]
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# x > 0 region
# (0,1): [x]=0 -> f(x)=0
x01 = np.linspace(0.02, 0.98, 200)
ax1.plot(x01, [0]*len(x01), '#1f77b4', linewidth=2, label=r'$(0,1)$: $f(x)=0$')
ax1.scatter([0], [0], s=60, facecolors='none', edgecolors='#1f77b4', linewidths=1.5)

# [1,2): [x]=1 -> f(x)=1/x
x12 = np.linspace(1, 1.98, 200)
ax1.plot(x12, 1/x12, '#ff7f0e', linewidth=2, label=r'$[1,2)$: $f(x)=1/x$')
ax1.scatter([1], [1], s=60, c='#ff7f0e', zorder=5)
ax1.scatter([2], [0.5], s=60, facecolors='none', edgecolors='#ff7f0e', linewidths=1.5, zorder=5)

# [2,3]: [x]=2 -> f(x)=2/x
x23 = np.linspace(2, 3, 200)
ax1.plot(x23, 2/x23, '#2ca02c', linewidth=2, label=r'$[2,3]$: $f(x)=2/x$')
ax1.scatter([2], [1], s=60, c='#2ca02c', zorder=5)
ax1.scatter([3], [2/3], s=60, c='#2ca02c', zorder=5)

ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlim(-0.3, 3.5)
ax1.set_ylim(-0.3, 1.5)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title(r'$x > 0$ region')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.2)

# x < 0 region
# [-1,0): [x]=-1 -> f(x)=-1/x, shoots to +inf as x->0-
x_neg1 = np.linspace(-0.98, -0.02, 300)
ax2.plot(x_neg1, -1/x_neg1, '#d62728', linewidth=2, label=r'$[-1,0)$: $f(x)=-1/x$')
ax2.scatter([-1], [1], s=60, c='#d62728', zorder=5)

# [-2,-1): [x]=-2 -> f(x)=-2/x
x_neg2 = np.linspace(-1.98, -1.02, 200)
ax2.plot(x_neg2, -2/x_neg2, '#9467bd', linewidth=2, label=r'$[-2,-1)$: $f(x)=-2/x$')
ax2.scatter([-2], [1], s=60, c='#9467bd', zorder=5)
ax2.scatter([-1], [2], s=60, facecolors='none', edgecolors='#9467bd', linewidths=1.5, zorder=5)

# [-3,-2): [x]=-3 -> f(x)=-3/x
x_neg3 = np.linspace(-3, -2.02, 200)
ax2.plot(x_neg3, -3/x_neg3, '#8c564b', linewidth=2, label=r'$[-3,-2)$: $f(x)=-3/x$')
ax2.scatter([-3], [1], s=60, c='#8c564b', zorder=5)
ax2.scatter([-2], [1.5], s=60, facecolors='none', edgecolors='#8c564b', linewidths=1.5, zorder=5)

ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_xlim(-3.5, 0.3)
ax2.set_ylim(-0.3, 4.5)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title(r'$x < 0$ region')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.2)

plt.suptitle(r'Exercise 6: $f(x) = \frac{[x]}{x}$ on $[-3,0) \cup (0,3]$', fontsize=13)
plt.tight_layout()
plt.savefig(output_dir + 'sol09-ex6-floor-over-x.png', dpi=150)
plt.close()
print("Ex6 done")

print("\nAll Chapter 9 solution graphs generated!")
