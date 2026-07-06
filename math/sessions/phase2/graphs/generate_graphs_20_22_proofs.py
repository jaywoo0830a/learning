"""
Graphs for Sessions 20, 21, 22 — Proof Bridge.
20: ε-δ strip diagram
21: IVT bisection + secant-to-tangent
22: MVT geometry + FTC accumulation
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 20: ε-δ Strip Diagram — lim_{x→2} (3x+1) = 7
# ================================================================
fig, ax = plt.subplots(figsize=(10, 7))

x = np.linspace(0.8, 3.2, 400)
f = 3*x + 1
ax.plot(x, f, 'b-', linewidth=2.5, label=r'$f(x)=3x+1$')
ax.plot(2, 7, 'ko', markersize=8, zorder=5)

# ε-band (horizontal)
eps = 0.9
ax.axhspan(7-eps, 7+eps, alpha=0.12, color='blue')
ax.axhline(7+eps, color='blue', linestyle='--', linewidth=1, alpha=0.6)
ax.axhline(7-eps, color='blue', linestyle='--', linewidth=1, alpha=0.6)
ax.text(3.05, 7+eps+0.1, r'$L+\varepsilon$', fontsize=11, color='blue', va='bottom')
ax.text(3.05, 7-eps-0.1, r'$L-\varepsilon$', fontsize=11, color='blue', va='top')

# δ-window (vertical)
delta = eps/3
ax.axvspan(2-delta, 2+delta, alpha=0.12, color='red')
ax.axvline(2-delta, color='red', linestyle='--', linewidth=1, alpha=0.6)
ax.axvline(2+delta, color='red', linestyle='--', linewidth=1, alpha=0.6)
ax.text(2-delta-0.02, 2.5, r'$a-\delta$', fontsize=10, color='red', ha='right', rotation=90)
ax.text(2+delta+0.02, 2.5, r'$a+\delta$', fontsize=10, color='red', ha='left', rotation=90)

# Intersection rectangle highlighted
rect = Rectangle((2-delta, 7-eps), 2*delta, 2*eps, linewidth=2, edgecolor='purple',
                  facecolor='purple', alpha=0.08, linestyle='-')
ax.add_patch(rect)

# Annotations
ax.annotate(r'$\varepsilon$-band', xy=(2.8, 7.3), fontsize=13, color='blue', fontweight='bold')
ax.annotate(r'$\delta$-window', xy=(2.45, 4.8), fontsize=13, color='red', fontweight='bold')
ax.annotate('guarantees f(x)\nstays in ε-band', xy=(2.1, 7.5), fontsize=10, color='purple',
           ha='center')

ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title(r'Graph 20: The $\varepsilon$-$\delta$ Definition — $\lim_{x\to 2}(3x+1)=7$',
             fontsize=14, fontweight='bold')
ax.set_xlim(0.8, 3.3)
ax.set_ylim(2, 11)
ax.legend(fontsize=11, loc='upper left')
ax.grid(alpha=0.08)

plt.tight_layout()
plt.savefig(OUT + '20-epsilon-delta-strip.png', dpi=180, bbox_inches='tight')
plt.close()
print("20 done")


# ================================================================
# 21a: IVT Bisection
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

x = np.linspace(-0.2, 3.2, 300)

# Left: IVT statement
ax = axes[0]
f = x**3 - 3*x + 1
ax.plot(x, f, 'b-', linewidth=2.5)
ax.axhline(0, color='gray', linewidth=0.8)
ax.plot(0, 1, 'ro', markersize=8, label='f(0)=1')
ax.plot(1, -1, 'go', markersize=8, label='f(1)=−1')
# Show crossing
ax.annotate('f(c)=0\nfor some c', xy=(0.35, 0), xytext=(1.8, 1.5),
           arrowprops=dict(arrowstyle='->', color='darkred', lw=2),
           fontsize=12, color='darkred', fontweight='bold')
ax.axhline(0.5, color='orange', linestyle=':', alpha=0.5)
ax.set_title('IVT: Continuous on [0,1]\nf(0)=1, f(1)=−1 ⇒ ∃c: f(c)=0', fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.08)

# Right: Bisection steps
ax = axes[1]
# Show intervals shrinking
intervals = [(0, 1), (0, 0.5), (0.25, 0.5), (0.25, 0.375), (0.3125, 0.375)]
colors = ['blue', 'green', 'orange', 'red', 'purple']
y_positions = [4, 3, 2, 1, 0]
for i, ((a_i, b_i), c, y) in enumerate(zip(intervals, colors, y_positions)):
    ax.plot([a_i, b_i], [y, y], '-', color=c, linewidth=4, alpha=0.7)
    mid = (a_i + b_i)/2
    ax.plot(mid, y, 'o', color=c, markersize=8, zorder=5)
    ax.text(b_i+0.03, y, f'[{a_i}, {b_i}]', fontsize=9, va='center', color=c)

ax.set_title('Bisection Method:\nInterval halves each step', fontsize=12, fontweight='bold')
ax.set_xlim(-0.1, 1.5)
ax.set_ylim(-1, 5.5)
ax.set_xlabel('x')
ax.set_yticks([])
ax.grid(alpha=0.08, axis='x')

fig.suptitle('Graph 21a: Intermediate Value Theorem & Bisection Method',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '21-ivt-bisection.png', dpi=180, bbox_inches='tight')
plt.close()
print("21a done")


# ================================================================
# 21b: Secant to Tangent
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

def make_secant_tangent(ax, a, h, title):
    x = np.linspace(a-2, a+2, 300)
    f = lambda x: (x-2)**3 + 2*(x-2) + 3  # shifted cubic
    y = f(x)
    ax.plot(x, y, 'b-', linewidth=2)
    
    # Secant
    ax.plot([a, a+h], [f(a), f(a+h)], 'orange', linewidth=2.5, alpha=0.8, label='secant')
    ax.plot(a, f(a), 'ro', markersize=8, zorder=5)
    ax.plot(a+h, f(a+h), 'ro', markersize=8, zorder=5)
    
    # Tangent (true derivative)
    df_a = 3*(a-2)**2 + 2  # f'(a)
    x_tan = np.linspace(a-1.2, a+1.2, 100)
    ax.plot(x_tan, f(a) + df_a*(x_tan-a), 'r--', linewidth=2, alpha=0.7, label='tangent')
    
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.08)

make_secant_tangent(axes[0], 2, 1.5, 'Step 1: h=1.5\nSecant ≠ Tangent')
make_secant_tangent(axes[1], 2, 0.6, 'Step 2: h=0.6\nSecant gets closer')
make_secant_tangent(axes[2], 2, 0.15, 'Step 3: h→0\nSecant → Tangent (red)')

fig.suptitle(r'Graph 21b: Derivative as Limit of Secant Slopes — $f\'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '21-secant-to-tangent.png', dpi=180, bbox_inches='tight')
plt.close()
print("21b done")


# ================================================================
# 22a: MVT Geometry
# ================================================================
fig, ax = plt.subplots(figsize=(10, 7))

x = np.linspace(-0.5, 4.5, 400)
f = lambda x: 0.3*(x-2)**3 + 0.5*(x-2)**2 + 0.3*x + 1.5
y = f(x)
ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x)$')

a, b = 0.5, 4.0
fa, fb = f(a), f(b)
secant_slope = (fb - fa)/(b - a)

# Secant line
x_sec = np.linspace(a-0.2, b+0.2, 50)
ax.plot(x_sec, fa + secant_slope*(x_sec-a), 'orange', linewidth=2.5, alpha=0.8, 
        label=f'secant (slope={secant_slope:.2f})')
ax.plot([a, b], [fa, fb], 'o', color='orange', markersize=10, zorder=5)

# Tangent at c (approximately where f'=secant_slope)
c = 2.35  # approximate
fc = f(c)
df_c = 0.9*(c-2)**2 + (c-2) + 0.3  # f'(c)
x_tan = np.linspace(c-1.2, c+1.2, 80)
ax.plot(x_tan, fc + secant_slope*(x_tan-c), 'r--', linewidth=2.5, alpha=0.8,
        label=fr'tangent at $c\approx{c:.2f}$')
ax.plot(c, fc, 'ro', markersize=12, zorder=5)

# Dashed vertical projection
ax.plot([c, c], [0, fc], 'gray', linestyle=':', alpha=0.4)
ax.plot([a, a], [0, fa], 'gray', linestyle=':', alpha=0.3)
ax.plot([b, b], [0, fb], 'gray', linestyle=':', alpha=0.3)

ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title(r'Graph 22a: Mean Value Theorem — $f\'(c)=\frac{f(b)-f(a)}{b-a}$',
             fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper left')
ax.grid(alpha=0.08)

plt.tight_layout()
plt.savefig(OUT + '22-mvt-geometry.png', dpi=180, bbox_inches='tight')
plt.close()
print("22a done")


# ================================================================
# 22b: FTC Accumulation
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# Left: f(t) and area under it
ax = axes[0]
t = np.linspace(0, 5, 300)
f_vals = 1 + 0.3*t + 0.2*np.sin(2*t)
ax.plot(t, f_vals, 'r-', linewidth=2.5, label=r'$f(t)$')
# Shade area from 0 to 3
t_shade = np.linspace(0, 3, 100)
ax.fill_between(t_shade, 0, 1 + 0.3*t_shade + 0.2*np.sin(2*t_shade), 
                 alpha=0.3, color='blue', label=r'$A(3)=\int_0^3 f(t)dt$')
ax.axvline(3, color='blue', linestyle='--', alpha=0.5)
ax.set_title(r'$f(t)$ — the curve being integrated', fontsize=12, fontweight='bold')
ax.set_xlabel('t')
ax.legend(fontsize=10)
ax.grid(alpha=0.08)

# Right: A(x) = ∫_0^x f(t)dt and its derivative
ax = axes[1]
# Approximate A(x) numerically using cumulative Riemann sum
dt = 5/300
A_exact = np.cumsum(f_vals) * dt
ax.plot(t, A_exact, 'b-', linewidth=2.5, label=r'$A(x)=\int_0^x f(t)dt$')
# Tangent at x=3
idx3 = int(3/dt)
slope3 = f_vals[idx3]
x_tan = np.linspace(2, 4, 60)
ax.plot(x_tan, A_exact[idx3] + slope3*(x_tan-3), 'r--', linewidth=2, alpha=0.8,
        label=fr'$A\'(3)=f(3)\approx{slope3:.2f}$')
ax.plot(3, A_exact[idx3], 'ro', markersize=8, zorder=5)
ax.set_title(r'$A(x)$ — the accumulation function', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.legend(fontsize=10)
ax.grid(alpha=0.08)

fig.suptitle(r'Graph 22b: FTC Part 1 — $\frac{d}{dx}\int_a^x f(t)dt = f(x)$',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '22-ftc-accumulation.png', dpi=180, bbox_inches='tight')
plt.close()
print("22b done")

print("\n=== SESSIONS 20-22 GRAPHS DONE ===")
