#!/usr/bin/env python3
"""Generate visual graphs for 15A Curve Analysis — Geometry Meets Calculus."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, Circle, Polygon
import numpy as np
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams.update({
    'figure.dpi': 150, 'savefig.dpi': 150,
    'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 11,
    'savefig.facecolor': 'white', 'savefig.edgecolor': 'none',
    'figure.facecolor': 'white',
})

def save_fig(fig, name):
    fig.savefig(f'{OUTPUT_DIR}/{name}', bbox_inches='tight', facecolor='white',
                edgecolor='none', pad_inches=0.15)
    plt.close(fig)

# ════════════════════════════════════════════════════
# 01 — Tangent & Normal Line to f(x)=x² at x=3
# ════════════════════════════════════════════════════
def fig_01_tangent_normal():
    fig, ax = plt.subplots(figsize=(8, 7))
    x = np.linspace(-1, 6, 300)
    y = x**2
    ax.plot(x, y, 'b-', lw=2.5, label='f(x)=x²', zorder=3)

    x0, y0 = 3, 9
    m_tan = 6
    m_nor = -1/6

    x_tan = np.linspace(1, 5, 100)
    ax.plot(x_tan, y0 + m_tan*(x_tan - x0), '#E74C3C', lw=2, label='tangent: y=6x-9', zorder=4)
    ax.plot(x_tan, y0 + m_nor*(x_tan - x0), '#2ECC71', lw=2, label='normal: slope=-1/6', zorder=4)
    ax.plot(x0, y0, 'ko', ms=10, zorder=5)
    ax.annotate('(3,9)', (x0, y0), textcoords="offset points", xytext=(12, 12), fontsize=12, fontweight='bold')

    # Perpendicular indicator (small right angle)
    ax.plot([3.3, 3.3, 3.15], [9, 9.15, 9.15], 'k-', lw=1.2)

    ax.set_xlim(-0.5, 5.5); ax.set_ylim(-2, 18)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.25)
    ax.set_title('Tangent & Normal Lines to f(x)=x² at x=3', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '01-tangent-normal.png')

# ════════════════════════════════════════════════════
# 02 — Tangent from External Point (0,-1) to y=x²
# ════════════════════════════════════════════════════
def fig_02_external_tangent():
    fig, ax = plt.subplots(figsize=(8, 7))
    x = np.linspace(-3, 3, 400)
    y = x**2
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    # Tangency points
    for a, sign in [(-1, -1), (1, 1)]:
        ya = a**2
        m = 2*a
        xline = np.linspace(-3, 3, 100)
        ax.plot(xline, ya + m*(xline - a), '#E74C3C', lw=2, linestyle='--', zorder=4)
        ax.plot(a, ya, 'o', color='#E74C3C', ms=10, zorder=5)
        ax.annotate(f'({a},{ya})', (a, ya), textcoords="offset points",
                    xytext=(15*sign, 12), fontsize=11, color='#E74C3C', fontweight='bold')

    ax.plot(0, -1, 'ko', ms=12, zorder=5)
    ax.annotate('(0,-1)', (0, -1), textcoords="offset points", xytext=(-25, -18),
                fontsize=12, fontweight='bold')

    ax.set_xlim(-3, 3); ax.set_ylim(-2, 10)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.25)
    ax.set_title('Tangents to y=x² from External Point (0,-1)', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '02-external-tangent.png')

# ════════════════════════════════════════════════════
# 03 — Mean Value Theorem: f(x)=x³ on [0,2]
# ════════════════════════════════════════════════════
def fig_03_mvt():
    fig, ax = plt.subplots(figsize=(8, 7))
    x = np.linspace(-0.5, 2.5, 300)
    y = x**3
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    a, b = 0, 2
    fa, fb = a**3, b**3
    avg_slope = (fb - fa) / (b - a)  # 4

    # Secant
    x_sec = np.linspace(-0.3, 2.3, 100)
    ax.plot(x_sec, fa + avg_slope*(x_sec - a), '#8E44AD', lw=2, linestyle='--', 
            label=f'secant: avg slope={avg_slope}', zorder=4)

    # Tangent at c
    c = 2/np.sqrt(3)
    fc = c**3
    ax.plot(x_sec, fc + avg_slope*(x_sec - c), '#E74C3C', lw=2.5, 
            label=f'tangent at c={c:.3f}', zorder=4)

    # Points
    ax.plot(a, fa, 'o', color='#8E44AD', ms=10, zorder=5)
    ax.plot(b, fb, 'o', color='#8E44AD', ms=10, zorder=5)
    ax.plot(c, fc, 'o', color='#E74C3C', ms=10, zorder=5)
    ax.annotate(f'(0,0)', (a, fa), textcoords="offset points", xytext=(-15, -20), fontsize=10)
    ax.annotate(f'(2,8)', (b, fb), textcoords="offset points", xytext=(8, 12), fontsize=10)
    ax.annotate(f'c={c:.3f}', (c, fc), textcoords="offset points", xytext=(10, -20),
                fontsize=11, color='#E74C3C', fontweight='bold')

    ax.set_xlim(-0.3, 2.3); ax.set_ylim(-1, 10)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.25)
    ax.set_title("Mean Value Theorem: f'(c) = Average Slope", fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '03-mvt.png')

# ════════════════════════════════════════════════════
# 04 — First Derivative Sign Test & Extrema: f(x)=x³-3x
# ════════════════════════════════════════════════════
def fig_04_first_derivative_test():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 9), gridspec_kw={'height_ratios': [1.6, 1]})

    # Top: f(x)
    x = np.linspace(-2.5, 2.5, 400)
    fx = x**3 - 3*x
    ax1.plot(x, fx, 'b-', lw=2.5, zorder=3)
    ax1.plot(-1, 2, 'o', color='#E74C3C', ms=12, zorder=5)
    ax1.plot(1, -2, 'o', color='#2ECC71', ms=12, zorder=5)
    ax1.annotate('local max\n(-1,2)', (-1, 2), textcoords="offset points", xytext=(-30, 15),
                 fontsize=10, color='#E74C3C', fontweight='bold')
    ax1.annotate('local min\n(1,-2)', (1, -2), textcoords="offset points", xytext=(10, -25),
                 fontsize=10, color='#2ECC71', fontweight='bold')

    # Shade increasing/decreasing regions
    ax1.axvspan(-2.5, -1, alpha=0.08, color='green')
    ax1.axvspan(-1, 1, alpha=0.08, color='red')
    ax1.axvspan(1, 2.5, alpha=0.08, color='green')
    ax1.text(-1.75, 7, 'f increasing\nf\'>0', fontsize=9, color='green', ha='center')
    ax1.text(0, 7, 'f decreasing\nf\'<0', fontsize=9, color='red', ha='center')
    ax1.text(1.75, 7, 'f increasing\nf\'>0', fontsize=9, color='green', ha='center')

    ax1.axhline(0, color='gray', lw=0.5)
    ax1.set_xlim(-2.5, 2.5); ax1.set_ylim(-4, 8)
    ax1.grid(True, alpha=0.25)
    ax1.set_title("f(x)=x³-3x — Local Max at (-1,2), Local Min at (1,-2)", fontweight='bold')
    ax1.set_ylabel('f(x)')

    # Bottom: f'(x)
    fp = 3*x**2 - 3
    ax2.plot(x, fp, '#E74C3C', lw=2.5, zorder=3)
    ax2.fill_between(x, fp, 0, where=(fp>0), alpha=0.15, color='green')
    ax2.fill_between(x, fp, 0, where=(fp<0), alpha=0.15, color='red')
    ax2.axhline(0, color='gray', lw=0.8, linestyle='--')
    ax2.plot([-1, 1], [0, 0], 'ko', ms=8, zorder=5)
    ax2.annotate("f'(-1)=0\nsign + → -", (-1, 0), textcoords="offset points", xytext=(-40, 30),
                 fontsize=9, color='#E74C3C')
    ax2.annotate("f'(1)=0\nsign - → +", (1, 0), textcoords="offset points", xytext=(10, 30),
                 fontsize=9, color='#2ECC71')
    ax2.set_xlim(-2.5, 2.5); ax2.set_ylim(-5, 15)
    ax2.grid(True, alpha=0.25)
    ax2.set_title("f'(x)=3x²-3 — Sign Changes Classify Extrema", fontweight='bold')
    ax2.set_xlabel('x'); ax2.set_ylabel("f'(x)")
    plt.tight_layout()
    save_fig(fig, '04-first-derivative-test.png')

# ════════════════════════════════════════════════════
# 05 — Concavity & Inflection: f(x)=x³-3x
# ════════════════════════════════════════════════════
def fig_05_concavity_inflection():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 9), gridspec_kw={'height_ratios': [1.6, 1]})

    x = np.linspace(-2.5, 2.5, 400)
    fx = x**3 - 3*x

    # Top: f(x) with concavity regions
    ax1.plot(x, fx, 'b-', lw=2.5, zorder=3)
    ax1.axvspan(-2.5, 0, alpha=0.06, color='orange')
    ax1.axvspan(0, 2.5, alpha=0.06, color='cyan')
    ax1.text(-1.25, 6.5, 'CONCAVE DOWN\nf\'\'<0', fontsize=10, color='#E67E22', ha='center', fontweight='bold')
    ax1.text(1.25, 6.5, 'CONCAVE UP\nf\'\'>0', fontsize=10, color='#2980B9', ha='center', fontweight='bold')
    ax1.plot(0, 0, 'o', color='#8E44AD', ms=12, zorder=5)
    ax1.annotate('inflection\npoint (0,0)', (0, 0), textcoords="offset points", xytext=(40, -20),
                 fontsize=10, color='#8E44AD', fontweight='bold')
    ax1.axhline(0, color='gray', lw=0.5)
    ax1.set_xlim(-2.5, 2.5); ax1.set_ylim(-4, 8)
    ax1.grid(True, alpha=0.25)
    ax1.set_title("f(x)=x³-3x — Concave Down (x<0), Concave Up (x>0)", fontweight='bold')
    ax1.set_ylabel('f(x)')

    # Bottom: f''(x)=6x
    fpp = 6*x
    ax2.plot(x, fpp, '#8E44AD', lw=2.5, zorder=3)
    ax2.fill_between(x, fpp, 0, where=(fpp>0), alpha=0.12, color='cyan')
    ax2.fill_between(x, fpp, 0, where=(fpp<0), alpha=0.12, color='orange')
    ax2.axhline(0, color='gray', lw=0.8, linestyle='--')
    ax2.plot(0, 0, 'o', color='#8E44AD', ms=10, zorder=5)
    ax2.annotate("f''(0)=0\nsign change → inflection", (0, 0), textcoords="offset points",
                 xytext=(30, 35), fontsize=9, color='#8E44AD')
    ax2.set_xlim(-2.5, 2.5); ax2.set_ylim(-20, 20)
    ax2.grid(True, alpha=0.25)
    ax2.set_title("f''(x)=6x — Sign Change at x=0 = Inflection Point", fontweight='bold')
    ax2.set_xlabel('x'); ax2.set_ylabel("f''(x)")
    plt.tight_layout()
    save_fig(fig, '05-concavity-inflection.png')

# ════════════════════════════════════════════════════
# 06 — Curvature: Circle (κ=1/R) vs Line (κ=0)
# ════════════════════════════════════════════════════
def fig_06_curvature():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Circle: constant curvature
    R = 2
    theta = np.linspace(0, 2*np.pi, 300)
    ax1.plot(R*np.cos(theta), R*np.sin(theta), 'b-', lw=3)
    # Tangent at a point
    t0 = np.pi/4
    pt = np.array([R*np.cos(t0), R*np.sin(t0)])
    tangent_dir = np.array([-np.sin(t0), np.cos(t0)])
    ax1.arrow(pt[0], pt[1], 1.2*tangent_dir[0], 1.2*tangent_dir[1],
              head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', lw=2, zorder=5)
    # Radius
    ax1.plot([0, pt[0]], [0, pt[1]], 'gray', lw=1.5, linestyle='--')
    ax1.plot(0, 0, 'ko', ms=6)
    ax1.plot(pt[0], pt[1], 'ko', ms=8)
    ax1.text(0.3, 0.3, f'R={R}', fontsize=12, fontweight='bold')
    ax1.text(2.2, 1.7, r'$\kappa = \frac{1}{R}$', fontsize=13, color='#E74C3C', fontweight='bold')

    ax1.set_aspect('equal'); ax1.set_xlim(-3, 4); ax1.set_ylim(-3, 3.5)
    ax1.axhline(0, color='gray', lw=0.5); ax1.axvline(0, color='gray', lw=0.5)
    ax1.grid(True, alpha=0.2)
    ax1.set_title('Circle: Constant Curvature', fontweight='bold')

    # Line: zero curvature
    ax2.plot([-3, 3], [0, 0], 'b-', lw=3)
    ax2.arrow(0, 0, 1.5, 0, head_width=0.15, head_length=0.15, fc='#E74C3C', ec='#E74C3C', lw=2)
    ax2.text(0.7, -0.6, r'$\kappa = 0$', fontsize=13, color='#E74C3C', fontweight='bold')
    ax2.set_aspect('equal'); ax2.set_xlim(-3, 3); ax2.set_ylim(-2, 2)
    ax2.axhline(0, color='gray', lw=0.5); ax2.axvline(0, color='gray', lw=0.5)
    ax2.grid(True, alpha=0.2)
    ax2.set_title('Line: Zero Curvature (No Turning)', fontweight='bold')

    fig.suptitle('Curvature κ — Rate of Tangent Turning', fontweight='bold', fontsize=14, y=1.01)
    plt.tight_layout()
    save_fig(fig, '06-curvature.png')

# ════════════════════════════════════════════════════
# 07 — Complete Curve Sketch: f(x)=x²/(x-1)
# ════════════════════════════════════════════════════
def fig_07_curve_sketch():
    fig, ax = plt.subplots(figsize=(10, 8))

    # Left branch
    xL = np.linspace(-3, 0.88, 300)
    yL = xL**2 / (xL - 1)
    ax.plot(xL, yL, 'b-', lw=2.5, zorder=3)

    # Right branch
    xR = np.linspace(1.12, 5, 300)
    yR = xR**2 / (xR - 1)
    ax.plot(xR, yR, 'b-', lw=2.5, zorder=3)

    # Asymptotes
    ax.axvline(1, color='#E74C3C', lw=2, linestyle='--', zorder=2)
    x_asymp = np.linspace(-3, 5, 200)
    ax.plot(x_asymp, x_asymp + 1, '#2ECC71', lw=2, linestyle='--', zorder=2)

    # Critical points
    ax.plot(0, 0, 'o', color='#E74C3C', ms=12, zorder=5)
    ax.plot(2, 4, 'o', color='#2ECC71', ms=12, zorder=5)
    ax.annotate('local max\n(0,0)', (0, 0), textcoords="offset points", xytext=(15, -30),
                fontsize=10, color='#E74C3C', fontweight='bold')
    ax.annotate('local min\n(2,4)', (2, 4), textcoords="offset points", xytext=(20, 10),
                fontsize=10, color='#2ECC71', fontweight='bold')

    ax.annotate('x=1\n(vertical\nasymptote)', (1.05, -6), fontsize=10, color='#E74C3C', fontweight='bold')
    ax.annotate('y=x+1\n(slant\nasymptote)', (3.3, 5.5), fontsize=10, color='#2ECC71', fontweight='bold')

    ax.set_xlim(-3, 5); ax.set_ylim(-8, 10)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.2)
    ax.set_title("Complete Curve Sketch: f(x)=x²/(x-1)", fontweight='bold', fontsize=14)
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '07-curve-sketch.png')

# ════════════════════════════════════════════════════
# 08 — Parametric Curve: r(t)=(t³-3t, t²-1) with Vectors
# ════════════════════════════════════════════════════
def fig_08_parametric_vectors():
    fig, ax = plt.subplots(figsize=(9, 7))

    t = np.linspace(-2.2, 2.2, 500)
    x = t**3 - 3*t
    y = t**2 - 1
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    # Mark key points
    key_ts = [-2, -1, 0, 1, 2]
    colors = ['#E74C3C', '#E67E22', '#2ECC71', '#3498DB', '#8E44AD']
    for i, t0 in enumerate(key_ts):
        px, py = t0**3 - 3*t0, t0**2 - 1
        ax.plot(px, py, 'o', color=colors[i], ms=10, zorder=5)
        ax.annotate(f't={t0}', (px, py), textcoords="offset points", xytext=(8, 8),
                    fontsize=10, color=colors[i], fontweight='bold')

        # Velocity vector
        vx, vy = 3*t0**2 - 3, 2*t0
        scale = 0.25
        if abs(vx) + abs(vy) > 0.01:
            ax.arrow(px, py, scale*vx, scale*vy, head_width=0.2, head_length=0.2,
                     fc=colors[i], ec=colors[i], alpha=0.7, lw=1.8, zorder=4)

    # Horizontal tangent label
    ax.annotate('horizontal\ntangent', (0, -1), textcoords="offset points", xytext=(25, -5),
                fontsize=10, color='#2ECC71', fontweight='bold')
    # Vertical tangent labels
    ax.annotate('vertical\ntangent', (-2, 0), textcoords="offset points", xytext=(-25, -20),
                fontsize=10, color='#E67E22', fontweight='bold')
    ax.annotate('vertical\ntangent', (2, 0), textcoords="offset points", xytext=(8, -20),
                fontsize=10, color='#3498DB', fontweight='bold')

    ax.set_xlim(-6, 6); ax.set_ylim(-3, 4)
    ax.set_aspect('equal')
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.2)
    ax.set_title('Parametric Curve r(t)=(t³-3t, t²-1) with Velocity Vectors', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '08-parametric-vectors.png')

# ════════════════════════════════════════════════════
# 09 — Tangent to Parametric Ellipse at t=π/4
# ════════════════════════════════════════════════════
def fig_09_parametric_ellipse_tangent():
    fig, ax = plt.subplots(figsize=(8, 7))
    a, b = 4, 2.5
    t = np.linspace(0, 2*np.pi, 400)
    ax.plot(a*np.cos(t), b*np.sin(t), 'b-', lw=2.5, zorder=3)

    t0 = np.pi/4
    x0, y0 = a*np.cos(t0), b*np.sin(t0)
    vx, vy = -a*np.sin(t0), b*np.cos(t0)

    # Tangent line
    ts = np.linspace(-2, 2, 50)
    ax.plot(x0 + ts*vx, y0 + ts*vy, '#E74C3C', lw=2.5, label='tangent', zorder=4)
    ax.plot(x0, y0, 'ko', ms=10, zorder=5)
    ax.arrow(x0, y0, 0.6*vx, 0.6*vy, head_width=0.15, head_length=0.15,
             fc='#E74C3C', ec='#E74C3C', lw=2, zorder=5)
    ax.annotate(f't=π/4\n({x0:.1f},{y0:.1f})', (x0, y0), textcoords="offset points",
                xytext=(10, 15), fontsize=10, fontweight='bold')

    ax.set_aspect('equal'); ax.set_xlim(-5, 5); ax.set_ylim(-3.5, 3.5)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.2)
    ax.set_title('Tangent to Parametric Ellipse at t=π/4', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '09-ellipse-tangent.png')

# ════════════════════════════════════════════════════
# 10 — Graph of f(x)=x³ showing f'(0)=0 but no extremum
# ════════════════════════════════════════════════════
def fig_10_cubic_no_extremum():
    fig, ax = plt.subplots(figsize=(8, 7))
    x = np.linspace(-2, 2, 400)
    y = x**3
    ax.plot(x, y, 'b-', lw=2.5, zorder=3)

    # Tangent at x=0
    ax.plot([-1.5, 1.5], [0, 0], '#E74C3C', lw=2, linestyle='--', zorder=4)
    ax.plot(0, 0, 'o', color='#8E44AD', ms=12, zorder=5)

    # Concavity shading
    ax.axvspan(-2, 0, alpha=0.06, color='orange')
    ax.axvspan(0, 2, alpha=0.06, color='cyan')
    ax.text(-1, 7, "concave\ndown", fontsize=11, color='#E67E22', ha='center', fontweight='bold')
    ax.text(1, -7, "concave\nup", fontsize=11, color='#2980B9', ha='center', fontweight='bold')

    ax.annotate("f'(0)=0\nBUT no extremum\n— inflection!", (0, 0), textcoords="offset points",
                xytext=(35, -35), fontsize=11, color='#8E44AD', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.set_xlim(-2, 2); ax.set_ylim(-8, 8)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.grid(True, alpha=0.2)
    ax.set_title("f(x)=x³: f'(0)=0 But No Extremum — Inflection Point", fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('y')
    save_fig(fig, '10-cubic-no-extremum.png')

if __name__ == '__main__':
    print("Generating 15A graphs...")
    fig_01_tangent_normal()
    fig_02_external_tangent()
    fig_03_mvt()
    fig_04_first_derivative_test()
    fig_05_concavity_inflection()
    fig_06_curvature()
    fig_07_curve_sketch()
    fig_08_parametric_vectors()
    fig_09_parametric_ellipse_tangent()
    fig_10_cubic_no_extremum()
    print("Done! 10 graphs generated.")
