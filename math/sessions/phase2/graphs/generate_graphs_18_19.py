"""
Graphs for Sessions 18 and 19 — Series, Taylor, and ODEs.

18a1 — Geometric series: partial sums converging
18a2 — p-series integral test visualization
18b1 — Radius of convergence on number line
18c1 — Taylor approximations of sin x (T1,T3,T5,T7)
18c2 — Taylor approximations of e^x
19a1 — Slope field for dy/dx = x+y
19a2 — Logistic curve with carrying capacity
19d1 — Euler method vs exact solution
19d2 — Lotka-Volterra phase plane preview
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 18A1 — Geometric Series Partial Sums
# ================================================================
fig, ax = plt.subplots(figsize=(11, 7))

terms_a = 2 * (0.6)**np.arange(0, 20)
partial_a = np.cumsum(terms_a)
ax.plot(range(1, 21), partial_a, 'b-o', markersize=5, linewidth=2,
        label=r'$\sum 2(0.6)^n \to \frac{2}{1-0.6}=5$')

terms_b = 2 * (-0.6)**np.arange(0, 20)
partial_b = np.cumsum(terms_b)
ax.plot(range(1, 21), partial_b, 'r-s', markersize=5, linewidth=2,
        label=r'$\sum 2(-0.6)^n \to \frac{2}{1+0.6}=1.25$')

ax.axhline(5, color='blue', linestyle='--', alpha=0.4, linewidth=1)
ax.axhline(1.25, color='red', linestyle='--', alpha=0.4, linewidth=1)

ax.set_xlabel('Number of terms N', fontsize=13)
ax.set_ylabel('Partial sum S_N', fontsize=13)
ax.set_title('Graph 18A1: Geometric Series — Partial Sums Converge\nto a/(1−r) when |r|<1',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(OUT + '18a1-geometric-series.png', dpi=180, bbox_inches='tight')
plt.close()
print("18A1 done")


# ================================================================
# 18A2 — p-Series Integral Test
# ================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
ax1, ax2 = axes

x = np.linspace(1, 10, 300)
# p=2 (converges)
y2 = 1/x**2
ax1.fill_between(x, 0, y2, alpha=0.3, color='steelblue')
ax1.plot(x, y2, 'b-', linewidth=2)
n_pts = np.arange(1, 11)
ax1.bar(n_pts, 1/n_pts**2, width=0.6, alpha=0.6, color='blue', label=r'$\sum 1/n^2$ terms')
ax1.set_title(r'$p=2$: $\int_1^\infty 1/x^2\,dx$ converges → series converges',
              fontsize=11, fontweight='bold')
ax1.legend(fontsize=9); ax1.grid(alpha=0.15)

# p=1 (diverges)
y1 = 1/x
ax2.fill_between(x, 0, y1, alpha=0.3, color='coral')
ax2.plot(x, y1, 'r-', linewidth=2)
ax2.bar(n_pts, 1/n_pts, width=0.6, alpha=0.6, color='red', label=r'$\sum 1/n$ terms')
ax2.set_title(r'$p=1$: $\int_1^\infty 1/x\,dx$ diverges → harmonic diverges',
              fontsize=11, fontweight='bold')
ax2.legend(fontsize=9); ax2.grid(alpha=0.15)

fig.suptitle('Graph 18A2: Integral Test — Series and Improper Integral Share Fate',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '18a2-p-series.png', dpi=180, bbox_inches='tight')
plt.close()
print("18A2 done")


# ================================================================
# 18B1 — Radius of Convergence
# ================================================================
fig, ax = plt.subplots(figsize=(12, 3.5))

# Three series with different radii
series_data = [
    (r'$\sum x^n$', -1, 1, 'blue', 'R=1'),
    (r'$\sum \frac{x^n}{n}$', -1, 1, 'green', 'R=1, x=1 diverges'),
    (r'$\sum \frac{x^n}{n^2}$', -1, 1, 'darkred', 'R=1, endpoints converge'),
]

for i, (label, lo, hi, color, note) in enumerate(series_data):
    y_pos = 3 - i
    ax.plot([lo, hi], [y_pos, y_pos], '-', color=color, linewidth=6, alpha=0.5)
    ax.plot(lo, y_pos, 'o', color=color, markersize=10, fillstyle='none' if 'x=1 diverges' in note else 'full')
    ax.plot(hi, y_pos, 'o', color=color, markersize=10, fillstyle='none' if 'x=1 diverges' in note and i==1 else 'full')
    ax.text(-1.5, y_pos, label, fontsize=11, ha='right', va='center')
    ax.text(1.3, y_pos, note, fontsize=9, ha='left', va='center', style='italic')

ax.axvline(0, color='gray', linewidth=1, alpha=0.5)
ax.set_xlim(-2.5, 3.5)
ax.set_ylim(0, 4)
ax.set_xlabel('x', fontsize=14)
ax.set_yticks([])
ax.set_title('Graph 18B1: Radius & Interval of Convergence — Check Endpoints!',
             fontsize=13, fontweight='bold')
ax.grid(alpha=0.1, axis='x')
plt.tight_layout()
plt.savefig(OUT + '18b1-radius-convergence.png', dpi=180, bbox_inches='tight')
plt.close()
print("18B1 done")


# ================================================================
# 18C1 — Taylor Approximations of sin x
# ================================================================
fig, ax = plt.subplots(figsize=(12, 8))

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y_true = np.sin(x)

ax.plot(x, y_true, 'k-', linewidth=2.5, label=r'$\sin x$ (exact)')

# Taylor polynomials
T1 = x
T3 = x - x**3/6
T5 = x - x**3/6 + x**5/120
T7 = x - x**3/6 + x**5/120 - x**7/5040

colors = ['red', 'orange', 'green', 'blue']
for T, color, label in [(T1, 'red', 'T₁(x)=x'), (T3, 'orange', 'T₃'),
                          (T5, 'green', 'T₅'), (T7, 'blue', 'T₇')]:
    ax.plot(x, T, '--', color=color, linewidth=1.8, alpha=0.8, label=label)

ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-2.5, 2.5)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 18C1: Taylor Approximations of sin x\nHigher degree = better approximation over wider interval',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10, loc='lower left')
ax.grid(alpha=0.15)
ax.axhline(0, color='gray', lw=0.4)
plt.tight_layout()
plt.savefig(OUT + '18c1-taylor-sin.png', dpi=180, bbox_inches='tight')
plt.close()
print("18C1 done")


# ================================================================
# 18C2 — Taylor of e^x
# ================================================================
fig, ax = plt.subplots(figsize=(12, 8))

x = np.linspace(-3, 3, 500)
y_true = np.exp(x)

ax.plot(x, y_true, 'k-', linewidth=2.5, label=r'$e^x$ (exact)')
ax.fill_between(x, 0, y_true, alpha=0.05, color='black')

# Taylor
T1 = 1 + x
T2 = 1 + x + x**2/2
T3 = 1 + x + x**2/2 + x**3/6
T4 = 1 + x + x**2/2 + x**3/6 + x**4/24

for T, color, label in [(T1,'red','T₁'), (T2,'orange','T₂'),
                          (T3,'green','T₃'), (T4,'blue','T₄')]:
    ax.plot(x, T, '--', color=color, linewidth=1.8, alpha=0.8, label=label)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 15)
ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 18C2: Taylor Approximations of e^x\nAt x=1: 1+1+1/2+1/6+1/24≈2.708 vs e≈2.718',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '18c2-taylor-exp.png', dpi=180, bbox_inches='tight')
plt.close()
print("18C2 done")


# ================================================================
# 19A1 — Slope Field dy/dx = x+y
# ================================================================
fig, ax = plt.subplots(figsize=(11, 9))

x_vals = np.linspace(-3, 3, 18)
y_vals = np.linspace(-3, 3, 18)
X, Y = np.meshgrid(x_vals, y_vals)
U = np.ones_like(X)
V = X + Y
# Normalize
mag = np.sqrt(1 + V**2)
ax.quiver(X, Y, U/mag, V/mag, angles='xy', scale_units='xy', scale=20,
          color='gray', alpha=0.6, width=0.002)

# Solution curves: y = Ce^x - x - 1
for C in [-2, -1, 0, 1, 2, 3]:
    x_c = np.linspace(-3, 3, 300)
    y_c = C * np.exp(x_c) - x_c - 1
    mask = (y_c > -3.5) & (y_c < 3.5)
    ax.plot(x_c[mask], y_c[mask], 'b-', linewidth=1.8 if abs(C)<=1 else 1.2,
            alpha=0.9 if abs(C)<=1 else 0.5)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('Graph 19A1: Slope Field for dy/dx = x+y\nSolution curves: y = Ceˣ − x − 1',
             fontsize=13, fontweight='bold')
ax.grid(alpha=0.1)
plt.tight_layout()
plt.savefig(OUT + '19a1-slope-field.png', dpi=180, bbox_inches='tight')
plt.close()
print("19A1 done")


# ================================================================
# 19A2 — Logistic Curve
# ================================================================
fig, ax = plt.subplots(figsize=(12, 7))

t = np.linspace(0, 20, 400)
L, k = 1000, 0.5

for P0, color, label in [(50, 'blue', 'P₀=50'), (200, 'green', 'P₀=200'),
                           (500, 'orange', 'P₀=500'), (1200, 'red', 'P₀=1200')]:
    A = (L - P0) / P0
    P = L / (1 + A * np.exp(-k * t))
    ax.plot(t, P, color=color, linewidth=2.2, label=label)

ax.axhline(L, color='gray', linestyle='--', linewidth=1.5, alpha=0.7, label=f'Carrying capacity L={L}')
ax.axhline(L/2, color='gray', linestyle=':', linewidth=1, alpha=0.5, label=f'Inflection P={L/2}')

ax.set_xlabel('Time t', fontsize=13)
ax.set_ylabel('Population P', fontsize=13)
ax.set_title('Graph 19A2: Logistic Growth — S-Curve with Carrying Capacity',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '19a2-logistic.png', dpi=180, bbox_inches='tight')
plt.close()
print("19A2 done")


# ================================================================
# 19D1 — Euler Method vs Exact
# ================================================================
fig, ax = plt.subplots(figsize=(11, 8))

# y' = y, y(0)=1 → exact: y=e^x
x_exact = np.linspace(0, 1, 200)
y_exact = np.exp(x_exact)
ax.plot(x_exact, y_exact, 'b-', linewidth=2.5, label='Exact: y=eˣ')

# Euler with h=0.25
h = 0.25
x_euler = np.arange(0, 1.01, h)
y_euler = np.zeros_like(x_euler)
y_euler[0] = 1
for i in range(len(x_euler)-1):
    y_euler[i+1] = y_euler[i] + h * y_euler[i]

ax.plot(x_euler, y_euler, 'r-o', markersize=8, linewidth=2,
        label=f'Euler h=0.25 (4 steps)')

# Connect with vertical error bars
for i in range(len(x_euler)):
    ax.plot([x_euler[i], x_euler[i]], [y_euler[i], np.exp(x_euler[i])],
            'gray', linewidth=0.8, linestyle=':', alpha=0.6)

ax.set_xlabel('x', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Graph 19D1: Euler Method — Approximating y\'=y, y(0)=1\n'
             f'Final error: |{np.exp(1):.3f} − {y_euler[-1]:.3f}| = {abs(np.exp(1)-y_euler[-1]):.3f}',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig(OUT + '19d1-euler-method.png', dpi=180, bbox_inches='tight')
plt.close()
print("19D1 done")


# ================================================================
# 19D2 — Lotka-Volterra Phase Plane Preview
# ================================================================
fig, ax = plt.subplots(figsize=(10, 9))

# Simple Euler simulation of Lotka-Volterra
# dx/dt = x - xy, dy/dt = -y + xy
def lotka_volterra(x0, y0, T=30, dt=0.01):
    t = np.arange(0, T, dt)
    x, y = np.zeros(len(t)), np.zeros(len(t))
    x[0], y[0] = x0, y0
    for i in range(len(t)-1):
        x[i+1] = x[i] + dt * (x[i] - x[i]*y[i])
        y[i+1] = y[i] + dt * (-y[i] + x[i]*y[i])
    return x, y

# Multiple orbits
for x0, y0 in [(0.5, 0.5), (0.8, 0.8), (1.2, 0.8), (0.5, 1.2), (1.5, 1.5)]:
    x, y = lotka_volterra(x0, y0)
    ax.plot(x, y, linewidth=1.5, alpha=0.7)

# Equilibrium
ax.plot(1, 1, 'ro', markersize=12, label='Equilibrium (1,1)')

ax.set_xlabel('Prey population x', fontsize=13)
ax.set_ylabel('Predator population y', fontsize=13)
ax.set_title('Graph 19D2: Lotka-Volterra Phase Plane\nPredator-Prey Orbits (Phase 4 Preview)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.15)
ax.set_xlim(0, 3.5)
ax.set_ylim(0, 3.5)
plt.tight_layout()
plt.savefig(OUT + '19d2-phase-plane.png', dpi=180, bbox_inches='tight')
plt.close()
print("19D2 done")

print("\n=== ALL 18+19 GRAPHS GENERATED ===")
