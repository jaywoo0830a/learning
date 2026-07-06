"""
9A — 7-Step Graph Drawing Sequence for ALL 6 core examples.

Generates 6-panel step-by-step builds for:
  Ex2: f(x)=x³-4x (polynomial)
  Ex3: f(x)=(x²-x-2)/(x²-4) (rational with hole)
  Ex4: f(x)=(x²+2x)/(x-1) (slant asymptote)
  Ex5: f(x)=(2x+1)/(x-1) (hyperbola)
  Ex6: f(x)=√(x-1)+2 (radical half-graph)
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.unicode_minus'] = True

OUT = '/home/rlawjddn/learning/math/sessions/phase2/graphs/'

STEP_COLOR = '#1a5276'
ASYM_COLOR = '#c0392b'
INT_COLOR = '#27ae60'


def make_step_figure(func, x_segments, title, filename,
                     domain_excluded=None, symmetry_type='odd',
                     intercepts_x=None, intercept_y=None,
                     asym_vertical=None, asym_horizontal=None, asym_slant=None,
                     sign_intervals=None,
                     special_hole=None, special_jump=None):
    """
    Create a 6-panel step-by-step graph building figure.
    
    x_segments: list of (x_array, label) for domain-split plotting
    domain_excluded: list of x values to mark as excluded (vertical dashed red)
    symmetry_type: 'odd', 'even', or 'none'
    intercepts_x: list of x-intercept x-values
    intercept_y: y-intercept value (f(0))
    asym_vertical: list of x-values for vertical asymptotes
    asym_horizontal: y-value for horizontal asymptote (or None)
    asym_slant: (m, b) for slant asymptote y=mx+b (or None)
    sign_intervals: list of (x_start, x_end, 'pos'|'neg') for sign shading
    special_hole: (x, y) for a removable discontinuity
    special_jump: (x, y_left, y_right) for a jump discontinuity
    """
    fig, axes = plt.subplots(2, 3, figsize=(18, 13))
    (ax1, ax2, ax3), (ax4, ax5, ax6) = axes

    for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
        ax.set_xlim(-5, 5)
        ax.set_ylim(-6, 8)
        ax.axhline(0, color='gray', lw=0.4, alpha=0.5)
        ax.axvline(0, color='gray', lw=0.4, alpha=0.5)
        ax.grid(alpha=0.1)
    
    # Helper: draw the function on all segments
    def draw_func(ax, alpha=1.0, lw=2, color='b', style='-'):
        for x_arr in x_segments:
            y_arr = func(x_arr)
            # Clip extreme values for display
            y_arr = np.clip(y_arr, -20, 20)
            ax.plot(x_arr, y_arr, color=color, linewidth=lw, alpha=alpha, linestyle=style)
    
    # ---- Panel 1: DOMAIN ----
    ax1.set_title('Step 1: DOMAIN', fontsize=13, fontweight='bold', color=STEP_COLOR)
    if domain_excluded:
        for x_ex in domain_excluded:
            ax1.axvline(x_ex, color='red', linestyle='--', linewidth=2, alpha=0.8)
        # Shade valid regions
        all_ex = sorted(domain_excluded)
        bounds = [-5] + all_ex + [5]
        for i in range(len(bounds)-1):
            a, b = bounds[i], bounds[i+1]
            mid = (a+b)/2
            # Check if this region is valid (not beyond excluded)
            is_valid = True
            if a in all_ex: a += 0.05
            if b in all_ex: b -= 0.05
            if a < b:
                ax1.axvspan(a, b, alpha=0.06, color='green')
    else:
        ax1.axvspan(-5, 5, alpha=0.06, color='green')
        ax1.text(0, 7, 'All real numbers', fontsize=11, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    draw_func(ax1, alpha=0.4, lw=1, color='gray')
    if domain_excluded:
        label_text = ', '.join([f'x={x}' for x in domain_excluded])
        ax1.text(0, -5, f'Excluded: {label_text}', fontsize=10, ha='center', color='red')

    # ---- Panel 2: SYMMETRY ----
    ax2.set_title('Step 2: SYMMETRY', fontsize=13, fontweight='bold', color=STEP_COLOR)
    if symmetry_type == 'even':
        # Draw right solid, left mirrored dashed
        x_right = np.linspace(0, 5, 300)
        if domain_excluded:
            x_right = x_right[~np.isclose(x_right, np.array(domain_excluded)[:,None], atol=0.05).any(axis=0)]
        for x_arr in [x_right]:
            y_arr = np.clip(func(x_arr), -20, 20)
            ax2.plot(x_arr, y_arr, 'b-', linewidth=2.5)
        # Mirror left
        x_left = -x_right[::-1]
        y_left = np.clip(func(x_left), -20, 20)
        ax2.plot(x_left, y_left, 'b--', linewidth=2, alpha=0.7)
        ax2.axvline(0, color='purple', linestyle=':', linewidth=1.5, alpha=0.6)
        ax2.text(0, 7, 'Even: mirror across y-axis', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    elif symmetry_type == 'odd':
        x_right = np.linspace(0, 5, 300)
        if domain_excluded:
            x_right = x_right[~np.isclose(x_right, np.array(domain_excluded)[:,None], atol=0.05).any(axis=0)]
        for x_arr in [x_right]:
            y_arr = np.clip(func(x_arr), -20, 20)
            ax2.plot(x_arr, y_arr, 'b-', linewidth=2.5)
        x_left = -x_right[::-1]
        y_left = np.clip(func(x_left), -20, 20)
        ax2.plot(x_left, y_left, 'b--', linewidth=2, alpha=0.7)
        ax2.text(0, 7, 'Odd: rotate 180° around origin', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    else:
        draw_func(ax2)
        ax2.text(0, 7, 'No symmetry (draw full graph)', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # ---- Panel 3: INTERCEPTS ----
    ax3.set_title('Step 3: INTERCEPTS', fontsize=13, fontweight='bold', color=STEP_COLOR)
    draw_func(ax3)
    if intercepts_x:
        for xi in intercepts_x:
            # Check if xi is valid (not excluded)
            if domain_excluded and any(abs(xi - ex) < 0.01 for ex in domain_excluded):
                continue
            ax3.plot(xi, 0, 'o', color=INT_COLOR, markersize=10, zorder=5)
    if intercept_y is not None:
        if not (domain_excluded and any(abs(0 - ex) < 0.01 for ex in domain_excluded)):
            ax3.plot(0, intercept_y, 'o', color='darkorange', markersize=10, zorder=5)
            ax3.annotate(f'(0,{intercept_y:.1f})', (0, intercept_y),
                        textcoords='offset points', xytext=(5, 5), fontsize=9, color='darkorange')

    # ---- Panel 4: ASYMPTOTES ----
    ax4.set_title('Step 4: ASYMPTOTES', fontsize=13, fontweight='bold', color=STEP_COLOR)
    draw_func(ax4)
    if asym_vertical:
        for xv in asym_vertical:
            ax4.axvline(xv, color=ASYM_COLOR, linestyle='--', linewidth=2, alpha=0.8)
    if asym_horizontal is not None:
        ax4.axhline(asym_horizontal, color='darkorange', linestyle='--', linewidth=2, alpha=0.8)
    if asym_slant is not None:
        m, b = asym_slant
        x_slant = np.linspace(-5, 5, 200)
        ax4.plot(x_slant, m*x_slant + b, 'darkorange', linestyle='--', linewidth=2, alpha=0.8)

    # ---- Panel 5: SIGN ----
    ax5.set_title('Step 5: SIGN (+/−)', fontsize=13, fontweight='bold', color=STEP_COLOR)
    draw_func(ax5)
    if sign_intervals:
        for x_start, x_end, sign_type in sign_intervals:
            xs = np.linspace(x_start, x_end, 100)
            ys = np.clip(func(xs), -20, 20)
            if sign_type == 'pos':
                ax5.fill_between(xs, 0, ys, alpha=0.2, color='steelblue')
                mid = (x_start + x_end) / 2
                ax5.text(mid, 6.5, '+', fontsize=16, ha='center', color='steelblue', fontweight='bold')
            else:
                ax5.fill_between(xs, ys, 0, alpha=0.2, color='coral')
                mid = (x_start + x_end) / 2
                ax5.text(mid, -4, '−', fontsize=16, ha='center', color='coral', fontweight='bold')

    # ---- Panel 6: CONNECT (FINAL) ----
    ax6.set_title('Step 6–7: CONNECT + FINAL', fontsize=13, fontweight='bold', color=STEP_COLOR)
    draw_func(ax6, lw=3)
    # Re-draw asymptotes faintly
    if asym_vertical:
        for xv in asym_vertical:
            ax6.axvline(xv, color=ASYM_COLOR, linestyle='--', linewidth=1, alpha=0.5)
    if asym_horizontal is not None:
        ax6.axhline(asym_horizontal, color='darkorange', linestyle='--', linewidth=1, alpha=0.5)
    if intercepts_x:
        for xi in intercepts_x:
            if domain_excluded and any(abs(xi - ex) < 0.01 for ex in domain_excluded):
                continue
            ax6.plot(xi, 0, 'o', color=INT_COLOR, markersize=8, zorder=5)
    if intercept_y is not None:
        if not (domain_excluded and any(abs(0 - ex) < 0.01 for ex in domain_excluded)):
            ax6.plot(0, intercept_y, 'o', color='darkorange', markersize=8, zorder=5)
    if special_hole:
        hx, hy = special_hole
        ax6.plot(hx, hy, 'o', color='white', markersize=10, markeredgecolor='red', 
                markeredgewidth=2, zorder=6)

    fig.suptitle(title, fontsize=15, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig(OUT + filename, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"  {filename} done")


# ================================================================
# Example 2: f(x) = x³ − 4x (Polynomial)
# ================================================================
def ex2(x): return x**3 - 4*x

make_step_figure(
    func=ex2,
    x_segments=[np.linspace(-5, 5, 500)],
    title='Graph 9A Ex2: 7-Step Build — Polynomial $f(x)=x^3-4x$',
    filename='9a-step-ex2-polynomial.png',
    domain_excluded=[],
    symmetry_type='odd',
    intercepts_x=[-2, 0, 2],
    intercept_y=0,
    asym_vertical=[],
    asym_horizontal=None,
    sign_intervals=[
        (-5, -2, 'neg'), (-2, 0, 'pos'), (0, 2, 'neg'), (2, 5, 'pos')
    ]
)


# ================================================================
# Example 3: f(x) = (x²−x−2)/(x²−4) (Rational with hole at x=2)
# ================================================================
def ex3(x):
    # (x-2)(x+1)/(x-2)(x+2) = (x+1)/(x+2) for x≠2
    result = np.zeros_like(x)
    mask_valid = (np.abs(x - 2) > 0.01)
    result[mask_valid] = (x[mask_valid] + 1) / (x[mask_valid] + 2)
    result[~mask_valid] = np.nan
    return result

# Domain segments excluding x=-2, x=2
x_left = np.linspace(-5, -2.05, 150)
x_mid = np.linspace(-1.95, 1.95, 300)
x_right = np.linspace(2.05, 5, 150)

make_step_figure(
    func=ex3,
    x_segments=[x_left, x_mid, x_right],
    title='Graph 9A Ex3: 7-Step Build — Rational with Hole $f(x)=\\frac{x^2-x-2}{x^2-4}$',
    filename='9a-step-ex3-rational-hole.png',
    domain_excluded=[-2, 2],
    symmetry_type='none',
    intercepts_x=[-1],
    intercept_y=0.5,
    asym_vertical=[-2],
    asym_horizontal=1,
    sign_intervals=[
        (-5, -2, 'pos'), (-2, -1, 'neg'), (-1, 2, 'pos'), (2, 5, 'pos')
    ],
    special_hole=(2, 0.75)
)


# ================================================================
# Example 4: f(x) = (x²+2x)/(x-1) = x+3 + 3/(x-1) (Slant)
# ================================================================
def ex4(x):
    result = np.zeros_like(x)
    mask = np.abs(x - 1) > 0.01
    result[mask] = (x[mask]**2 + 2*x[mask]) / (x[mask] - 1)
    result[~mask] = np.nan
    return result

x4_left = np.linspace(-5, 0.95, 300)
x4_right = np.linspace(1.05, 5, 300)

make_step_figure(
    func=ex4,
    x_segments=[x4_left, x4_right],
    title='Graph 9A Ex4: 7-Step Build — Slant Asymptote $f(x)=\\frac{x^2+2x}{x-1}$',
    filename='9a-step-ex4-slant.png',
    domain_excluded=[1],
    symmetry_type='none',
    intercepts_x=[-2, 0],
    intercept_y=0,
    asym_vertical=[1],
    asym_slant=(1, 3),
    sign_intervals=[
        (-5, -2, 'neg'), (-2, 0, 'pos'), (0, 1, 'neg'), (1, 5, 'pos')
    ]
)


# ================================================================
# Example 5: f(x) = (2x+1)/(x-1) (Hyperbola)
# ================================================================
def ex5(x):
    result = np.zeros_like(x)
    mask = np.abs(x - 1) > 0.01
    result[mask] = (2*x[mask] + 1) / (x[mask] - 1)
    result[~mask] = np.nan
    return result

x5_left = np.linspace(-5, 0.95, 300)
x5_right = np.linspace(1.05, 5, 300)

make_step_figure(
    func=ex5,
    x_segments=[x5_left, x5_right],
    title='Graph 9A Ex5: 7-Step Build — Hyperbola $f(x)=\\frac{2x+1}{x-1}$',
    filename='9a-step-ex5-hyperbola.png',
    domain_excluded=[1],
    symmetry_type='none',
    intercepts_x=[-0.5],
    intercept_y=-1,
    asym_vertical=[1],
    asym_horizontal=2,
    sign_intervals=[
        (-5, -0.5, 'pos'), (-0.5, 1, 'neg'), (1, 5, 'pos')
    ]
)


# ================================================================
# Example 6: f(x) = √(x-1) + 2 (Radical half-graph)
# ================================================================
def ex6(x):
    result = np.full_like(x, np.nan)
    mask = x >= 1
    result[mask] = np.sqrt(x[mask] - 1) + 2
    return result

x6_valid = np.linspace(1, 5, 300)

make_step_figure(
    func=ex6,
    x_segments=[x6_valid],
    title='Graph 9A Ex6: 7-Step Build — Radical Half-Graph $f(x)=\\sqrt{x-1}+2$',
    filename='9a-step-ex6-radical.png',
    domain_excluded=[],
    symmetry_type='none',
    intercepts_x=[],
    intercept_y=None,
    asym_vertical=[],
    asym_horizontal=None,
    sign_intervals=[
        (1, 5, 'pos')
    ]
)

print("\n=== ALL 9A STEP-BY-STEP GRAPHS GENERATED ===")
