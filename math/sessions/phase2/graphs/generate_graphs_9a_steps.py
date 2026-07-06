"""
9A — 7-Step Graph Drawing Sequence visualized step-by-step.

Function: f(x) = (x²-4)/(x²-1) — a rational function with holes? No holes here.
Wait, let's use a richer one: f(x) = (x-2)(x+1)/(x+1)(x-3) = (x-2)/(x-3) for x≠-1
with a hole at x=-1, vertical at x=3, horizontal at y=1.

Actually, let me use the function from the session: f(x) = (x²-4)/(x²-1)
- Domain: x≠±1
- Symmetry: even
- Intercepts: x=±2, y-int (0,4)
- Asymptotes: vertical x=±1, horizontal y=1
- Sign: pos outside [-2,-1)∪(1,2], neg inside

6-panel build-up: Domain → Symmetry → Intercepts → Asymptotes → Sign → Connect
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

x_full = np.linspace(-5, 5, 600)
x_left = x_full[x_full < -1.001]
x_mid = x_full[(x_full > -0.999) & (x_full < 0.999)]
x_right = x_full[x_full > 1.001]

f = lambda x: (x**2 - 4) / (x**2 - 1)


# ================================================================
# 6-panel step-by-step graph drawing
# ================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 13))
(ax1, ax2, ax3), (ax4, ax5, ax6) = axes

step_color = '#1a5276'
asym_color = '#c0392b'
intercept_color = '#27ae60'
fill_pos = '#d5f5e3'
fill_neg = '#fadbd8'

for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 8)
    ax.axhline(0, color='gray', lw=0.4, alpha=0.5)
    ax.axvline(0, color='gray', lw=0.4, alpha=0.5)
    ax.set_aspect('auto')
    ax.grid(alpha=0.1)

# ---- Panel 1: DOMAIN ----
ax1.set_title('Step 1: DOMAIN — Exclude x = ±1', fontsize=13, fontweight='bold', color=step_color)
# Shade the excluded regions
ax1.axvspan(-5, -1.05, alpha=0.08, color='green')
ax1.axvspan(-0.95, 0.95, alpha=0.08, color='green')
ax1.axvspan(1.05, 5, alpha=0.08, color='green')
ax1.axvline(-1, color='red', linestyle='--', linewidth=2, alpha=0.8, label='x=−1 (excluded)')
ax1.axvline(1, color='red', linestyle='--', linewidth=2, alpha=0.8, label='x=1 (excluded)')
# Show the whole graph faintly
for seg in [x_left, x_mid, x_right]:
    ax1.plot(seg, f(seg), 'gray', linewidth=1, alpha=0.5)
ax1.legend(fontsize=9, loc='upper right')
ax1.set_ylabel('', fontsize=10)

# ---- Panel 2: SYMMETRY ----
ax2.set_title('Step 2: SYMMETRY — Even: f(−x)=f(x)', fontsize=13, fontweight='bold', color=step_color)
# Draw right half solid, left half dashed to show mirror
x_right_half = x_full[(x_full >= 0) & (np.abs(x_full - 1) > 0.01) & (np.abs(x_full - (-1)) > 0.01)]
# Actually just draw the right side
x_right_part = x_full[(x_full > 1.001)]
x_mid_right = x_full[(x_full >= 0) & (x_full < 0.999)]
ax2.plot(x_right_part, f(x_right_part), 'b-', linewidth=2.5)
ax2.plot(x_mid_right, f(x_mid_right), 'b-', linewidth=2.5)
# Mirror: left side
x_left_part = x_full[(x_full < -1.001)]
x_mid_left = x_full[(x_full > -0.999) & (x_full < 0)]
ax2.plot(x_left_part, f(x_left_part), 'b--', linewidth=2, alpha=0.7)
ax2.plot(x_mid_left, f(x_mid_left), 'b--', linewidth=2, alpha=0.7)
ax2.text(0, 7, 'Draw right → mirror left', fontsize=11, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax2.axvline(0, color='purple', linestyle=':', linewidth=1.5, alpha=0.6, label='y-axis (mirror)')
ax2.legend(fontsize=9)

# ---- Panel 3: INTERCEPTS ----
ax3.set_title('Step 3: INTERCEPTS — x=±2, y=4', fontsize=13, fontweight='bold', color=step_color)
for seg in [x_left, x_mid, x_right]:
    ax3.plot(seg, f(seg), 'b-', linewidth=2)
ax3.plot([-2, 2], [0, 0], 'o', color=intercept_color, markersize=12, zorder=5, label='x-int: (−2,0), (2,0)')
ax3.plot(0, 4, 'o', color='darkorange', markersize=12, zorder=5, label='y-int: (0,4)')
ax3.legend(fontsize=9)

# ---- Panel 4: ASYMPTOTES ----
ax4.set_title('Step 4: ASYMPTOTES — x=±1 (V), y=1 (H)', fontsize=13, fontweight='bold', color=step_color)
for seg in [x_left, x_mid, x_right]:
    ax4.plot(seg, f(seg), 'b-', linewidth=2)
ax4.axvline(-1, color=asym_color, linestyle='--', linewidth=2, label='Vertical: x=−1')
ax4.axvline(1, color=asym_color, linestyle='--', linewidth=2, label='Vertical: x=1')
ax4.axhline(1, color='darkorange', linestyle='--', linewidth=2, label='Horizontal: y=1')
ax4.legend(fontsize=9)

# ---- Panel 5: SIGN ----
ax5.set_title('Step 5: SIGN — Positive/Negative regions', fontsize=13, fontweight='bold', color=step_color)
# Draw the graph
for seg in [x_left, x_mid, x_right]:
    ax5.plot(seg, f(seg), 'b-', linewidth=2)

# Shade positive and negative regions
# Positive: (−∞,−2), (−1,1), (2,∞)
# Negative: (−2,−1), (1,2)
x_pos1 = np.linspace(-5, -2, 100)
x_pos2 = np.linspace(-0.99, 0.99, 100)
x_pos3 = np.linspace(2, 5, 100)
for xp in [x_pos1, x_pos2, x_pos3]:
    ax5.fill_between(xp, 0, f(xp), alpha=0.25, color='steelblue')

x_neg1 = np.linspace(-2, -1.01, 100)
x_neg2 = np.linspace(1.01, 2, 100)
for xn in [x_neg1, x_neg2]:
    ax5.fill_between(xn, f(xn), 0, alpha=0.25, color='coral')

ax5.text(-3.5, 5, 'POSITIVE', fontsize=10, color='steelblue', fontweight='bold')
ax5.text(-1.5, -2, 'NEG', fontsize=10, color='coral', fontweight='bold')
ax5.text(0, 5, 'POS', fontsize=10, color='steelblue', fontweight='bold')
ax5.text(1.5, -2, 'NEG', fontsize=10, color='coral', fontweight='bold')
ax5.text(3.5, 3, 'POS', fontsize=10, color='steelblue', fontweight='bold')

# ---- Panel 6: CONNECT (FINAL) ----
ax6.set_title('Step 6–7: CONNECT + Final Graph', fontsize=13, fontweight='bold', color=step_color)
for seg in [x_left, x_mid, x_right]:
    ax6.plot(seg, f(seg), 'b-', linewidth=3, zorder=3)
ax6.axvline(-1, color=asym_color, linestyle='--', linewidth=1.5, alpha=0.7)
ax6.axvline(1, color=asym_color, linestyle='--', linewidth=1.5, alpha=0.7)
ax6.axhline(1, color='darkorange', linestyle='--', linewidth=1.5, alpha=0.7)
ax6.plot([-2, 2], [0, 0], 'o', color=intercept_color, markersize=10, zorder=5)
ax6.plot(0, 4, 'o', color='darkorange', markersize=10, zorder=5)
ax6.text(0, -4, r'$f(x)=\frac{x^2-4}{x^2-1}$', fontsize=14, ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.95))

fig.suptitle('Graph 9A: The 7-Step Graph Drawing Sequence — Build Up One Layer at a Time',
             fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(OUT + '9a-seven-step-sequence.png', dpi=180, bbox_inches='tight')
plt.close()
print("9A 7-step sequence done")
