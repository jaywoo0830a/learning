import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch
rcParams = plt.rcParams
rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True
out = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

# ===== SESSION 13: LIMITS =====

# 13a: 0/0 limit — f(x)=(x^2-4)/(x-2) approaching x=2
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 3.95, 400)
y = (x**2 - 4)/(x - 2)
ax.plot(x, y, 'b-', linewidth=2, label=r'$f(x)=\frac{x^2-4}{x-2}=x+2\ (x\neq2)$')
ax.scatter([2], [4], s=120, facecolors='none', edgecolors='red', linewidths=2.5, zorder=10, label='hole at (2,4), limit=4')
ax.axvline(2, color='gray', linestyle=':', linewidth=0.6, alpha=0.5)
ax.axhline(4, color='gray', linestyle=':', linewidth=0.6, alpha=0.5)
ax.set_xlim(0, 4)
ax.set_ylim(1.5, 6.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Graph 13a: $\\lim_{x\\to2}\\frac{x^2-4}{x-2}=4$ (hole)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'13a-limit-hole.png', dpi=150); plt.close()
print("13a done")

# 13b: One-sided limits — 1/(x-2)
fig, ax = plt.subplots(figsize=(8, 5))
xL = np.linspace(0, 1.92, 200); xR = np.linspace(2.08, 4, 200)
ax.plot(xL, 1/(xL-2), 'b-', linewidth=2, label=r'$y=\frac{1}{x-2}$')
ax.plot(xR, 1/(xR-2), 'b-', linewidth=2)
ax.axvline(2, color='red', linestyle='--', linewidth=1, label='x=2 (vertical asymptote)')
ax.axhline(0, color='gray', linewidth=0.4)
ax.annotate(r'$x\to2^-:\ -\infty$', (1.7, -8), fontsize=10, color='blue')
ax.annotate(r'$x\to2^+:\ +\infty$', (2.2, 8), fontsize=10, color='blue')
ax.set_xlim(0, 4); ax.set_ylim(-10, 10)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('Graph 13b: One-sided limits — $\\lim_{x\\to2}\\frac{1}{x-2}$ does not exist')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'13b-onesided.png', dpi=150); plt.close()
print("13b done")

# 13c: sin x / x → 1
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-4*np.pi, 4*np.pi, 1000)
y = np.where(x != 0, np.sin(x)/x, 1.0)
ax.plot(x, y, 'b-', linewidth=1.5, label=r'$y=\frac{\sin x}{x}$')
ax.axhline(1, color='red', linestyle='--', linewidth=0.8, label='y=1 (limit)')
ax.scatter([0], [1], s=80, c='red', zorder=10)
ax.set_xlim(-4*np.pi, 4*np.pi); ax.set_ylim(-0.4, 1.2)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 13c: $\lim_{x\to0}\frac{\sin x}{x}=1$')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'13c-sinx-over-x.png', dpi=150); plt.close()
print("13c done")

# 13d: Horizontal asymptote — (3x^2+2x-1)/(x^2+5)
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-15, 15, 1000)
y = (3*x**2 + 2*x - 1)/(x**2 + 5)
ax.plot(x, y, 'b-', linewidth=1.8, label=r'$y=\frac{3x^2+2x-1}{x^2+5}$')
ax.axhline(3, color='red', linestyle='--', linewidth=1, label='y=3 (horizontal asymptote)')
ax.set_xlim(-15, 15); ax.set_ylim(0, 5)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 13d: $\lim_{x\to\infty}\frac{3x^2+2x-1}{x^2+5}=3$')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'13d-horizontal-asymptote.png', dpi=150); plt.close()
print("13d done")

# ===== SESSION 14: DERIVATIVES =====

# 14a: Tangent line to x^2 at x=3
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-1, 5, 300); y = x**2
ax.plot(x, y, 'b-', linewidth=2, label=r'$y=x^2$')
x_tan = np.linspace(1.5, 4.5, 100)
ax.plot(x_tan, 6*x_tan - 9, 'r-', linewidth=1.5, label=r'$y=6x-9$ (tangent at x=3)')
ax.scatter([3], [9], s=80, c='red', zorder=10)
ax.set_xlim(-1, 5); ax.set_ylim(-2, 18)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 14a: Tangent to $y=x^2$ at $x=3$ (slope=6)')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'14a-tangent.png', dpi=150); plt.close()
print("14a done")

# 14b: Derivative of sin x is cos x
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 2*np.pi, 500)
ax.plot(x, np.sin(x), 'b-', linewidth=2, label=r'$y=\sin x$')
ax.plot(x, np.cos(x), 'r--', linewidth=1.5, label=r"$y'=\cos x$")
ax.axhline(0, color='gray', linewidth=0.4)
ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r"Graph 14b: $\frac{d}{dx}\sin x=\cos x$")
ax.legend(); ax.grid(True, alpha=0.3)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0','π/2','π','3π/2','2π'])
plt.tight_layout(); plt.savefig(out+'14b-sin-derivative.png', dpi=150); plt.close()
print("14b done")

# ===== SESSION 15: DERIVATIVE APPLICATIONS =====

# 15a: f(x)=x^3-3x^2-9x+5 — critical points
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(-3, 6, 500)
y = x**3 - 3*x**2 - 9*x + 5
ax.plot(x, y, 'b-', linewidth=2, label=r'$f(x)=x^3-3x^2-9x+5$')
ax.scatter([-1], [10], s=100, c='red', zorder=10, label='local max: (-1,10)')
ax.scatter([3], [-22], s=100, c='green', zorder=10, label='local min: (3,-22)')
ax.axhline(0, color='gray', linewidth=0.4)
ax.set_xlim(-3, 6); ax.set_ylim(-30, 20)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 15a: $f(x)=x^3-3x^2-9x+5$, critical at $x=-1,3$')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'15a-critical-points.png', dpi=150); plt.close()
print("15a done")

# 15b: Optimization — fence problem (square is optimal)
fig, ax = plt.subplots(figsize=(7, 6))
x_vals = np.linspace(1, 49, 200)
A = x_vals * (50 - x_vals)
ax.plot(x_vals, A, 'b-', linewidth=2, label=r'$A=x(50-x)$')
ax.scatter([25], [625], s=100, c='red', zorder=10, label='max: (25, 625)')
ax.axvline(25, color='red', linestyle='--', linewidth=0.6, alpha=0.5)
ax.set_xlim(0, 50); ax.set_ylim(0, 700)
ax.set_xlabel('x (width)'); ax.set_ylabel('Area A')
ax.set_title('Graph 15b: Fence Optimization — Max area at x=25')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'15b-optimization.png', dpi=150); plt.close()
print("15b done")

# ===== SESSION 16: INTEGRATION =====

# 16a: FTC visualization — area under x^2 from 0 to 2
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 2.5, 300); y = x**2
ax.plot(x, y, 'b-', linewidth=2, label=r'$y=x^2$')
x_fill = np.linspace(0, 2, 100)
ax.fill_between(x_fill, x_fill**2, alpha=0.3, color='blue', label=r'Area = $\int_0^2 x^2 dx = \frac{8}{3}$')
ax.set_xlim(0, 2.5); ax.set_ylim(0, 5)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 16a: $\int_0^2 x^2 dx = \frac{8}{3}$ (FTC)')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'16a-ftc-area.png', dpi=150); plt.close()
print("16a done")

# 16b: Integration of sin x from 0 to pi
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, np.pi, 300)
ax.plot(x, np.sin(x), 'b-', linewidth=2, label=r'$y=\sin x$')
ax.fill_between(x, np.sin(x), alpha=0.3, color='blue', label=r'Area = $\int_0^\pi\sin x\,dx=2$')
ax.set_xlim(0, np.pi); ax.set_ylim(0, 1.2)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 16b: $\int_0^\pi\sin x\,dx=2$')
ax.legend(); ax.grid(True, alpha=0.3)
ax.set_xticks([0, np.pi/2, np.pi])
ax.set_xticklabels(['0','π/2','π'])
plt.tight_layout(); plt.savefig(out+'16b-sin-area.png', dpi=150); plt.close()
print("16b done")

# ===== SESSION 17: INTEGRATION APPLICATIONS =====

# 17a: Area between curves — y=x and y=x^2
fig, ax = plt.subplots(figsize=(7, 6))
x = np.linspace(0, 1, 200)
ax.plot(x, x, 'b-', linewidth=2, label=r'$y=x$')
ax.plot(x, x**2, 'r-', linewidth=2, label=r'$y=x^2$')
x_fill = np.linspace(0, 1, 100)
ax.fill_between(x_fill, x_fill, x_fill**2, alpha=0.3, color='purple', label=r'Area = $\frac{1}{6}$')
ax.set_xlim(0, 1.2); ax.set_ylim(0, 1.2)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 17a: Area between $y=x$ and $y=x^2$')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'17a-between-curves.png', dpi=150); plt.close()
print("17a done")

# 17b: Volume of revolution — y=x^2 rotated about x-axis
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 2, 300)
ax.plot(x, x**2, 'b-', linewidth=2, label=r'$y=x^2$')
ax.fill_between(x, x**2, alpha=0.2, color='blue')
ax.annotate('rotate about x-axis', (0.5, 2.5), fontsize=10, color='red')
ax.annotate(r'$V=\pi\int_0^2 x^4 dx = \frac{32\pi}{5}$', (0.5, 2.0), fontsize=11, color='red')
ax.set_xlim(0, 2.2); ax.set_ylim(0, 4.5)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Graph 17b: Solid of revolution — $y=x^2$ about $x$-axis')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'17b-solid-revolution.png', dpi=150); plt.close()
print("17b done")

# 17c: Gabriel's Horn — y=1/x, x>=1
fig, ax = plt.subplots(figsize=(9, 5))
x = np.linspace(1, 8, 500)
ax.plot(x, 1/x, 'b-', linewidth=2, label=r'$y=\frac{1}{x}$')
ax.fill_between(x, 1/x, alpha=0.2, color='blue')
ax.axhline(0, color='gray', linewidth=0.4)
ax.axvline(1, color='red', linestyle='--', linewidth=0.8, alpha=0.6)
ax.annotate(r'Volume = $\pi\int_1^\infty\frac{1}{x^2}dx=\pi$ (finite!)', (2.5, 0.6), fontsize=11, color='red')
ax.annotate(r'Surface area = $\infty$ (infinite!)', (2.5, 0.4), fontsize=11, color='red')
ax.set_xlim(0.5, 8.5); ax.set_ylim(-0.1, 1.2)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title("Graph 17c: Gabriel's Horn — finite volume, infinite surface")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(out+'17c-gabriels-horn.png', dpi=150); plt.close()
print("17c done")

print("\n=== All 13 graphs for sessions 13-17 saved ===")
