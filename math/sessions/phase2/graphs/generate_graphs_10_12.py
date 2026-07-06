import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

out = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

# ========== SESSION 10 GRAPHS ==========

# Graph 10a: y = e^x and y = ln x side by side with y=x
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

x = np.linspace(-2, 3, 500)
ax1.plot(x, np.exp(x), 'b-', linewidth=2, label=r'$y = e^x$')
ax1.axhline(0, color='gray', linestyle=':', linewidth=0.5)
ax1.axvline(0, color='gray', linestyle=':', linewidth=0.5)
ax1.axhline(1, color='red', linestyle='--', linewidth=0.6, alpha=0.5)
ax1.scatter([0], [1], s=50, c='red', zorder=5)
ax1.set_xlim(-2, 3)
ax1.set_ylim(-1, 10)
ax1.set_title(r'$y = e^x$')
ax1.legend()
ax1.grid(True, alpha=0.3)

x_pos = np.linspace(0.02, 10, 500)
ax2.plot(x_pos, np.log(x_pos), 'b-', linewidth=2, label=r'$y = \ln x$')
ax2.axhline(0, color='gray', linestyle=':', linewidth=0.5)
ax2.axvline(0, color='gray', linestyle=':', linewidth=0.5)
ax2.axvline(1, color='red', linestyle='--', linewidth=0.6, alpha=0.5)
ax2.scatter([1], [0], s=50, c='red', zorder=5)
ax2.scatter([np.e], [1], s=50, c='green', zorder=5)
ax2.set_xlim(-0.5, 10)
ax2.set_ylim(-3, 3)
ax2.set_title(r'$y = \ln x$')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle('Graph 10a: Exponential & Natural Log', fontsize=13)
plt.tight_layout()
plt.savefig(out + '10a-exp-ln.png', dpi=150)
plt.close()
print("10a done")

# Graph 10b: e^x and ln x together showing symmetry about y=x
fig, ax = plt.subplots(figsize=(7, 7))
x_exp = np.linspace(-2, 2, 400)
ax.plot(x_exp, np.exp(x_exp), 'b-', linewidth=2, label=r'$y = e^x$')
x_ln = np.linspace(0.05, 7, 400)
ax.plot(x_ln, np.log(x_ln), 'r-', linewidth=2, label=r'$y = \ln x$')
x_diag = np.linspace(-2, 7, 100)
ax.plot(x_diag, x_diag, 'k--', linewidth=0.8, alpha=0.4, label=r'$y=x$')
ax.scatter([0], [1], c='blue', s=50, zorder=5)
ax.scatter([1], [0], c='red', s=50, zorder=5)
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
ax.set_xlim(-2, 7)
ax.set_ylim(-2, 7)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 10b: $y=e^x$ and $y=\ln x$ (inverse, mirror about $y=x$)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '10b-exp-ln-inverse.png', dpi=150)
plt.close()
print("10b done")

# Graph 10c: Exponential growth vs decay
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 5, 300)
ax.plot(x, np.exp(0.5*x), 'b-', linewidth=2, label=r'growth: $e^{0.5t}$ (doubling)')
ax.plot(x, np.exp(-0.5*x), 'r-', linewidth=2, label=r'decay: $e^{-0.5t}$ (half-life)')
ax.axhline(0, color='gray', linewidth=0.4)
ax.axhline(1, color='gray', linestyle=':', linewidth=0.5)
ax.set_xlim(0, 5)
ax.set_ylim(-0.2, 10)
ax.set_xlabel('t')
ax.set_ylabel('y')
ax.set_title('Graph 10c: Exponential Growth vs Decay')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '10c-growth-decay.png', dpi=150)
plt.close()
print("10c done")

# Graph 10d: Log plots (log10, ln, log2)
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0.01, 10, 500)
ax.plot(x, np.log10(x), 'b-', linewidth=1.5, label=r'$\log_{10} x$')
ax.plot(x, np.log(x), 'r-', linewidth=1.5, label=r'$\ln x$')
ax.plot(x, np.log2(x), 'g--', linewidth=1.5, label=r'$\log_2 x$')
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(1, color='gray', linestyle=':', linewidth=0.5)
ax.scatter([1], [0], s=40, c='black', zorder=5)
ax.scatter([10], [1], s=40, c='blue', zorder=4)
ax.scatter([np.e], [1], s=40, c='red', zorder=4)
ax.scatter([2], [1], s=40, c='green', zorder=4)
ax.set_xlim(-0.3, 10)
ax.set_ylim(-2, 3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graph 10d: Comparing Logarithm Bases')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '10d-log-bases.png', dpi=150)
plt.close()
print("10d done")

# ========== SESSION 11 GRAPHS ==========

# Graph 11a: Unit circle with special angles
fig, ax = plt.subplots(figsize=(7, 7))
theta = np.linspace(0, 2*np.pi, 300)
ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=1.5)
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 3*np.pi/4, 5*np.pi/6,
          np.pi, 7*np.pi/6, 5*np.pi/4, 4*np.pi/3, 3*np.pi/2, 5*np.pi/3, 7*np.pi/4, 11*np.pi/6]
labels = ['0', 'π/6', 'π/4', 'π/3', 'π/2', '2π/3', '3π/4', '5π/6',
          'π', '7π/6', '5π/4', '4π/3', '3π/2', '5π/3', '7π/4', '11π/6']
colors = ['red', 'blue', 'green', 'orange', 'purple', 'blue', 'green', 'orange',
          'red', 'blue', 'green', 'orange', 'purple', 'orange', 'green', 'blue']
for a, l, c in zip(angles, labels, colors):
    ax.scatter([np.cos(a)], [np.sin(a)], s=50, c=c, zorder=5)
    ax.annotate(l, (np.cos(a)*1.12, np.sin(a)*1.12), fontsize=7, ha='center')
ax.set_aspect('equal')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_xlabel('cos θ')
ax.set_ylabel('sin θ')
ax.set_title('Graph 11a: Unit Circle — Special Angles')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '11a-unit-circle.png', dpi=150)
plt.close()
print("11a done")

# Graph 11b: sin, cos, tan — all 3 on same plot
fig, axes = plt.subplots(3, 1, figsize=(10, 9))
x = np.linspace(-2*np.pi, 2*np.pi, 800)
axes[0].plot(x, np.sin(x), 'b-', linewidth=1.5)
axes[0].axhline(0, color='gray', linewidth=0.4)
axes[0].set_ylim(-1.3, 1.3)
axes[0].set_title(r'$y = \sin x$')
axes[0].grid(True, alpha=0.3)
axes[0].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
axes[0].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

axes[1].plot(x, np.cos(x), 'r-', linewidth=1.5)
axes[1].axhline(0, color='gray', linewidth=0.4)
axes[1].set_ylim(-1.3, 1.3)
axes[1].set_title(r'$y = \cos x$')
axes[1].grid(True, alpha=0.3)
axes[1].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
axes[1].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

# tan with asymptotes
x_tan = np.linspace(-2*np.pi, 2*np.pi, 2000)
y_tan = np.tan(x_tan)
y_tan[np.abs(y_tan) > 5] = np.nan
axes[2].plot(x_tan, y_tan, 'g-', linewidth=1.2)
axes[2].axhline(0, color='gray', linewidth=0.4)
for v in [-3*np.pi/2, -np.pi/2, np.pi/2, 3*np.pi/2]:
    axes[2].axvline(v, color='red', linestyle='--', linewidth=0.6, alpha=0.5)
axes[2].set_ylim(-5, 5)
axes[2].set_title(r'$y = \tan x$')
axes[2].grid(True, alpha=0.3)
axes[2].set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
axes[2].set_xticklabels(['-2π', '-π', '0', 'π', '2π'])

plt.suptitle('Graph 11b: sine, cosine, tangent', fontsize=13)
plt.tight_layout()
plt.savefig(out + '11b-sin-cos-tan.png', dpi=150)
plt.close()
print("11b done")

# Graph 11c: csc, sec, cot graphs
fig, axes = plt.subplots(3, 1, figsize=(10, 9))
x = np.linspace(-2*np.pi, 2*np.pi, 2000)
# csc
y_csc = 1/np.sin(x)
y_csc[np.abs(y_csc) > 4] = np.nan
axes[0].plot(x, y_csc, 'b-', linewidth=1.2, label=r'$\csc x$')
axes[0].plot(x, np.sin(x), 'gray', linewidth=0.5, alpha=0.4, label=r'$\sin x$')
for v in [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]:
    axes[0].axvline(v, color='red', linestyle='--', linewidth=0.5, alpha=0.5)
axes[0].set_ylim(-4, 4)
axes[0].set_title(r'$y = \csc x$ (with $\sin x$ dashed)')
axes[0].legend(fontsize=8)
axes[0].grid(True, alpha=0.3)
# sec
y_sec = 1/np.cos(x)
y_sec[np.abs(y_sec) > 4] = np.nan
axes[1].plot(x, y_sec, 'r-', linewidth=1.2, label=r'$\sec x$')
axes[1].plot(x, np.cos(x), 'gray', linewidth=0.5, alpha=0.4, label=r'$\cos x$')
for v in [-3*np.pi/2, -np.pi/2, np.pi/2, 3*np.pi/2]:
    axes[1].axvline(v, color='red', linestyle='--', linewidth=0.5, alpha=0.5)
axes[1].set_ylim(-4, 4)
axes[1].set_title(r'$y = \sec x$ (with $\cos x$ dashed)')
axes[1].legend(fontsize=8)
axes[1].grid(True, alpha=0.3)
# cot
y_cot = 1/np.tan(x)
y_cot[np.abs(y_cot) > 4] = np.nan
axes[2].plot(x, y_cot, 'g-', linewidth=1.2, label=r'$\cot x$')
for v in [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]:
    axes[2].axvline(v, color='red', linestyle='--', linewidth=0.5, alpha=0.5)
axes[2].set_ylim(-4, 4)
axes[2].set_title(r'$y = \cot x$')
axes[2].legend(fontsize=8)
axes[2].grid(True, alpha=0.3)

plt.suptitle('Graph 11c: cosecant, secant, cotangent', fontsize=13)
plt.tight_layout()
plt.savefig(out + '11c-csc-sec-cot.png', dpi=150)
plt.close()
print("11c done")

# Graph 11d: a sin(bx+c)+d — example y=3sin(2x-pi/3)+1
fig, ax = plt.subplots(figsize=(9, 5))
x = np.linspace(0, 2*np.pi, 500)
y = 3*np.sin(2*x - np.pi/3) + 1
ax.plot(x, y, 'b-', linewidth=2, label=r'$3\sin(2x-\pi/3)+1$')
ax.axhline(1, color='gray', linestyle=':', linewidth=0.8, label='vertical shift: +1')
ax.axhline(4, color='green', linestyle='--', linewidth=0.6, alpha=0.5)
ax.axhline(-2, color='green', linestyle='--', linewidth=0.6, alpha=0.5)
ax.axvline(np.pi/6, color='red', linestyle='--', linewidth=0.6, alpha=0.5, label='phase shift: π/6')
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-3, 5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Graph 11d: $y = 3\sin(2x-\pi/3)+1$ — Amplitude, Period, Shift')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xticks([0, np.pi/6, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', 'π/6', 'π/2', 'π', '3π/2', '2π'])
plt.tight_layout()
plt.savefig(out + '11d-sin-transform.png', dpi=150)
plt.close()
print("11d done")

# Graph 11e: Law of sines & cosines illustration
fig, ax = plt.subplots(figsize=(7, 6))
# Triangle: A=(0,0), B=(5,0), C=(2,4)
A, B, C = np.array([0,0]), np.array([5,0]), np.array([2,4])
ax.plot([A[0],B[0]], [A[1],B[1]], 'k-', linewidth=2)
ax.plot([B[0],C[0]], [B[1],C[1]], 'k-', linewidth=2)
ax.plot([C[0],A[0]], [C[1],A[1]], 'k-', linewidth=2)
ax.text(A[0]-0.2, A[1]-0.3, 'A', fontsize=12)
ax.text(B[0]+0.1, B[1]-0.3, 'B', fontsize=12)
ax.text(C[0]-0.1, C[1]+0.3, 'C', fontsize=12)
# Label sides
ax.text(2.5, -0.3, 'c', fontsize=11, ha='center')
ax.text(3.7, 2.2, 'a', fontsize=11, ha='center')
ax.text(0.8, 2.2, 'b', fontsize=11, ha='center')
# Angle arcs
from matplotlib.patches import Arc
ax.add_patch(Arc((0,0), 0.8, 0.8, angle=0, theta1=0, theta2=63, color='blue', linewidth=1.5))
ax.add_patch(Arc((5,0), 0.8, 0.8, angle=0, theta1=126.87, theta2=180, color='red', linewidth=1.5))
ax.add_patch(Arc((2,4), 0.8, 0.8, angle=243, theta1=0, theta2=64, color='green', linewidth=1.5))
ax.set_aspect('equal')
ax.set_xlim(-1, 6.5)
ax.set_ylim(-1, 5.5)
ax.set_title('Graph 11e: Triangle for Law of Sines & Cosines')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '11e-triangle-laws.png', dpi=150)
plt.close()
print("11e done")

# ========== SESSION 12 GRAPHS ==========

# Graph 12a: Complex plane — z=1+√3i in polar form
fig, ax = plt.subplots(figsize=(7, 7))
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
# Circle radius 2
theta = np.linspace(0, 2*np.pi, 200)
ax.plot(2*np.cos(theta), 2*np.sin(theta), 'gray', linewidth=0.5, linestyle=':', alpha=0.5)
# Point z=1+√3i
ax.plot([0, 1], [0, np.sqrt(3)], 'b-', linewidth=2, label=r'$r=2$')
ax.scatter([1], [np.sqrt(3)], s=80, c='blue', zorder=5)
ax.annotate(r'$z=1+i\sqrt{3}$', (1.1, 1.8), fontsize=11)
# Angle arc
from matplotlib.patches import Arc
ax.add_patch(Arc((0,0), 1, 1, angle=0, theta1=0, theta2=60, color='red', linewidth=1.5))
ax.annotate(r'$\theta=\pi/3$', (0.7, 0.35), fontsize=10, color='red')
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title(r'Graph 12a: Complex Plane — $z=1+i\sqrt{3}=2(\cos\pi/3+i\sin\pi/3)$')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '12a-complex-plane.png', dpi=150)
plt.close()
print("12a done")

# Graph 12b: Roots of unity — z^4=1
fig, ax = plt.subplots(figsize=(7, 7))
theta = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=1.5)
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
roots = [(1,0), (0,1), (-1,0), (0,-1)]
colors = ['red', 'blue', 'green', 'orange']
labels = ['1', 'i', '-1', '-i']
for (x,y), c, l in zip(roots, colors, labels):
    ax.scatter([x], [y], s=100, c=c, zorder=5, edgecolors='black')
    ax.annotate(l, (x*1.15, y*1.15), fontsize=11, ha='center')
# Connect to form square
pts = np.array(roots + [roots[0]])
ax.plot(pts[:,0], pts[:,1], 'b--', linewidth=1, alpha=0.5)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title(r'Graph 12b: 4th Roots of Unity ($z^4=1$) — Square')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '12b-roots-unity.png', dpi=150)
plt.close()
print("12b done")

# Graph 12c: Vector operations
fig, ax = plt.subplots(figsize=(7, 7))
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
# a = (3,1)
ax.arrow(0, 0, 3, 1, head_width=0.15, head_length=0.2, fc='blue', ec='blue', linewidth=2, label=r'$\vec{a}=(3,1)$')
# b = (1,2)
ax.arrow(0, 0, 1, 2, head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=2, label=r'$\vec{b}=(1,2)$')
# a+b = (4,3)
ax.arrow(0, 0, 4, 3, head_width=0.15, head_length=0.2, fc='green', ec='green', linewidth=2, alpha=0.7, label=r'$\vec{a}+\vec{b}=(4,3)$')
# Dashed parallelogram
ax.plot([3, 4], [1, 3], 'gray', linestyle='--', linewidth=0.8)
ax.plot([1, 4], [2, 3], 'gray', linestyle='--', linewidth=0.8)
# Angle
ax.annotate(r'$\theta$', (0.5, 0.15), fontsize=11)
ax.set_aspect('equal')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graph 12c: Vector Addition & Parallelogram')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '12c-vectors.png', dpi=150)
plt.close()
print("12c done")

# Graph 12d: Arithmetic vs Geometric sequences
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
n = np.arange(1, 8)
# Arithmetic: a1=2, d=3
arith = 2 + (n-1)*3
ax1.stem(n, arith, linefmt='b-', markerfmt='bo', basefmt='k-')
for i, v in zip(n, arith):
    ax1.annotate(str(v), (i, v+0.3), fontsize=9, ha='center')
ax1.set_title('Arithmetic: $a_1=2, d=3$')
ax1.set_xlabel('n')
ax1.set_ylabel('$a_n$')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 22)

# Geometric: a1=2, r=1.8
geom = 2 * (1.8)**(n-1)
ax2.stem(n, geom, linefmt='r-', markerfmt='ro', basefmt='k-')
for i, v in zip(n, geom):
    ax2.annotate(f'{v:.1f}', (i, v+0.5), fontsize=8, ha='center')
ax2.set_title(r'Geometric: $a_1=2, r=1.8$')
ax2.set_xlabel('n')
ax2.set_ylabel('$a_n$')
ax2.grid(True, alpha=0.3)

plt.suptitle('Graph 12d: Arithmetic vs Geometric Sequences', fontsize=13)
plt.tight_layout()
plt.savefig(out + '12d-sequences.png', dpi=150)
plt.close()
print("12d done")

# Graph 12e: De Moivre — z^6 for z=1+i
fig, ax = plt.subplots(figsize=(7, 7))
n_powers = 6
r0 = np.sqrt(2)
theta0 = np.pi/4
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(0, color='gray', linewidth=0.4)
colors = plt.cm.viridis(np.linspace(0, 1, n_powers+1))
for k in range(1, n_powers+1):
    rk = r0**k
    thetak = k * theta0
    xk, yk = rk*np.cos(thetak), rk*np.sin(thetak)
    ax.scatter([xk], [yk], s=80, c=[colors[k]], zorder=5, edgecolors='black')
    ax.annotate(f'z^{k}', (xk*1.1, yk*1.1), fontsize=8, ha='center')
max_r = r0**n_powers
ax.set_aspect('equal')
ax.set_xlim(-max_r*1.3, max_r*1.3)
ax.set_ylim(-max_r*1.3, max_r*1.3)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title(r'Graph 12e: De Moivre — Powers of $z=1+i$')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(out + '12e-demoivre.png', dpi=150)
plt.close()
print("12e done")

print("\n=== All session 10-12 graphs saved ===")
