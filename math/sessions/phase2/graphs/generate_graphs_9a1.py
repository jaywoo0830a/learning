"""
Graphs for 9A1 — Function Fundamentals.
Two graphs: increasing/decreasing intervals, fold vs copy.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'


# ================================================================
# 9A0-1: Increasing vs Decreasing
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

x = np.linspace(-3, 3, 300)

# Left: f(x) = x² — decreases then increases
ax = axes[0]
ax.plot(x, x**2, 'b-', linewidth=2.5)
ax.fill_between(x[x<=0], x[x<=0]**2, alpha=0.15, color='red')
ax.fill_between(x[x>=0], x[x>=0]**2, alpha=0.15, color='green')
# Arrow: decreasing
ax.annotate('decreasing\n(y falls)', xy=(-2, 4), xytext=(-1.5, 7),
           arrowprops=dict(arrowstyle='->', color='red', lw=2),
           fontsize=11, color='red', fontweight='bold', ha='center')
# Arrow: increasing
ax.annotate('increasing\n(y rises)', xy=(2, 4), xytext=(1.5, 7),
           arrowprops=dict(arrowstyle='->', color='green', lw=2),
           fontsize=11, color='green', fontweight='bold', ha='center')
ax.axvline(0, color='gray', linestyle=':', alpha=0.5)
ax.set_title(r'$f(x)=x^2$: ↓ then ↑', fontsize=13, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(alpha=0.1)

# Middle: f(x) = x³ — always increasing
ax = axes[1]
ax.plot(x, x**3, 'g-', linewidth=2.5)
ax.fill_between(x, x**3, alpha=0.1, color='green')
ax.annotate('always\nincreasing', xy=(0, 0), xytext=(0.5, -15),
           arrowprops=dict(arrowstyle='->', color='darkgreen', lw=2),
           fontsize=11, color='darkgreen', fontweight='bold', ha='center')
ax.set_title(r'$f(x)=x^3$: always ↑', fontsize=13, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(alpha=0.1)

# Right: f(x) = -x+3 — always decreasing
ax = axes[2]
ax.plot(x, -x+3, 'r-', linewidth=2.5)
ax.fill_between(x, -x+3, alpha=0.1, color='red')
ax.annotate('always\ndecreasing', xy=(0, 3), xytext=(-1.5, 0),
           arrowprops=dict(arrowstyle='->', color='darkred', lw=2),
           fontsize=11, color='darkred', fontweight='bold', ha='center')
ax.set_title(r'$f(x)=-x+3$: always ↓', fontsize=13, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(alpha=0.1)

fig.suptitle('Graph 9A0-1: Increasing vs Decreasing Intervals',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9a1-inc-dec.png', dpi=180, bbox_inches='tight')
plt.close()
print("9A0 inc-dec done")


# ================================================================
# 9A0-2: |f(x)| vs f(|x|)
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

x = np.linspace(-3.5, 3.5, 400)

# Left: f(x) = x²-4
ax = axes[0]
ax.plot(x, x**2-4, 'b-', linewidth=2.5)
ax.fill_between(x[x**2-4<0], x[x**2-4<0]**2-4, color='blue', alpha=0.15)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title(r'Original: $f(x)=x^2-4$', fontsize=12, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(alpha=0.1)
ax.set_ylim(-5, 6)

# Middle: |f(x)| = |x²-4|
ax = axes[1]
y_fold = np.abs(x**2 - 4)
ax.plot(x[x**2-4>=0], x[x**2-4>=0]**2-4, 'b-', linewidth=2.5)
ax.plot(x[x**2-4<0], -x[x**2-4<0]**2+4, linewidth=2.5, color='#1a5276')
ax.fill_between(x[np.abs(x)<2], -x[np.abs(x)<2]**2+4, color='#1a5276', alpha=0.2)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title(r'Folded: $|f(x)|=|x^2-4|$', fontsize=12, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(alpha=0.1)
ax.set_ylim(-1, 6)
# Annotation
ax.annotate('flipped\nupward', xy=(0, 4), xytext=(1.5, 1.5),
           arrowprops=dict(arrowstyle='->', color='darkblue', lw=1.5, connectionstyle='arc3,rad=0.3'),
           fontsize=10, color='darkblue', fontweight='bold')

# Right: f(|x|) = |x|²-4 = x²-4 → wait this is same! Let use a non-even f.
# Actually f(x)=x²-4 is even so f(|x|)=f(x). Let me use f(x)=x-2 instead.
ax = axes[2]
f_orig_right = x[x>=0] - 2
ax.plot(x[x>=0], f_orig_right, 'b-', linewidth=2.5, label='right half of $x-2$')
ax.plot(x[x<=0], -x[x<=0] - 2, 'r--', linewidth=2.5, label='copied left half')
ax.fill_between(x[x<=0], -x[x<=0] - 2, alpha=0.1, color='red')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title(r'Copied: $f(|x|)=|x|-2$', fontsize=12, fontweight='bold')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.legend(fontsize=9)
ax.grid(alpha=0.1)
# Annotation
ax.annotate('right side\ncopied left', xy=(-2, 0), xytext=(-1.8, 3),
           arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
           fontsize=10, color='red', fontweight='bold')

fig.suptitle('Graph 9A0-2: |f(x)| Folds Upward vs f(|x|) Copies Right-to-Left',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(OUT + '9a1-fold-copy.png', dpi=180, bbox_inches='tight')
plt.close()
print("9A0 fold-copy done")

print("\n=== 9A0 GRAPHS DONE ===")
