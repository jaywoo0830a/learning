#!/usr/bin/env python3
"""Generate graphs for Session 15A: Curve Analysis."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/15A"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_tangent_normal():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-1, 4, 200)
    f = lambda x: x**2
    ax1.plot(x, f(x), 'b-', lw=2.5, label='$f(x)=x^2$')
    ax1.plot(x, 6*x-9, 'r-', lw=2, label='tangent at $x=3$')
    ax1.plot(x, -x/6+9.5, 'g-', lw=2, label='normal at $x=3$')
    ax1.plot(3, 9, 'ro', markersize=8, zorder=5)
    ax1.set_title('Tangent & Normal Lines\n$y=6x-9$ (tangent), $y=-x/6+9.5$ (normal)', fontweight='bold')
    ax1.axhline(0,color='gray',lw=0.5); ax1.axvline(0,color='gray',lw=0.5)
    ax1.set_xlim(-1,4); ax1.set_ylim(-2,12); ax1.grid(True,alpha=0.3); ax1.legend(fontsize=8)
    # External tangent
    x2 = np.linspace(-3, 3, 200)
    f2 = lambda x: x**2
    ax2.plot(x2, f2(x2), 'b-', lw=2.5, label='$y=x^2$')
    ax2.plot(x2, 2*x2-1, 'r-', lw=2, label='tangent at $x=1$')
    ax2.plot(x2, -2*x2-1, 'g-', lw=2, label='tangent at $x=-1$')
    ax2.plot(0, -1, 'ko', markersize=8, zorder=5, label='external point $(0,-1)$')
    ax2.plot(1,1,'ro',markersize=6); ax2.plot(-1,1,'go',markersize=6)
    ax2.set_title('Tangent from External Point\nThrough $(0,-1)$: $y=\\pm 2x-1$', fontweight='bold')
    ax2.axhline(0,color='gray',lw=0.5); ax2.axvline(0,color='gray',lw=0.5)
    ax2.set_xlim(-3,3); ax2.set_ylim(-2,9); ax2.grid(True,alpha=0.3); ax2.legend(fontsize=8)
    fig.suptitle('Tangent and Normal Lines', fontsize=14, fontweight='bold')
    save('15a-tangent-normal.png')

def fig_mvt_geometry():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, 5, 200)
    f = lambda x: x**2
    ax.plot(x, f(x), 'b-', lw=2.5, label='$f(x)=x^2$')
    # Secant
    ax.plot([1,4], [1,16], 'r--', lw=2.5, label='secant: slope $=(16-1)/(4-1)=5$')
    # Tangent at c=2.5
    c = 2.5
    ax.plot(x, 5*(x-c)+f(c), 'g-', lw=2.5, label=f'tangent at $c={c}$: slope $=5$')
    ax.plot(c, f(c), 'go', markersize=12, zorder=5)
    ax.plot(1,1,'ro',markersize=8,zorder=5); ax.plot(4,16,'ro',markersize=8,zorder=5)
    ax.annotate(f'$c={c}$', (c,f(c)), textcoords="offset points", xytext=(10,-15), fontsize=12, color='green', fontweight='bold')
    ax.annotate('$f\'(c)=5$', (c+0.2,f(c)+0.5), fontsize=11, color='green')
    ax.set_title('Mean Value Theorem\n$f\'(c) = \\frac{f(b)-f(a)}{b-a}$ guarantees such a $c$ exists', fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel('f(x)')
    ax.set_xlim(0,5); ax.set_ylim(-2,20); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    save('15a-mvt-geometry.png')

def fig_first_derivative_test():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-2.5, 2.5, 200)
    f = lambda x: x**3 - 3*x
    # Left: f with extrema
    ax = axes[0]
    ax.plot(x, f(x), 'b-', lw=2.5, label='$f(x)=x^3-3x$')
    ax.plot(-1, 2, 'ro', markersize=12, zorder=5)
    ax.plot(1, -2, 'go', markersize=12, zorder=5)
    ax.annotate('Local max\n$(-1,2)$', (-1,2), textcoords="offset points", xytext=(-30,-30), fontsize=10, color='red', fontweight='bold',
               arrowprops=dict(arrowstyle='->',color='red'))
    ax.annotate('Local min\n$(1,-2)$', (1,-2), textcoords="offset points", xytext=(10,20), fontsize=10, color='green', fontweight='bold',
               arrowprops=dict(arrowstyle='->',color='green'))
    ax.axhline(0,color='gray',lw=0.5); ax.axvline(0,color='gray',lw=0.5)
    ax.set_xlim(-2.5,2.5); ax.set_ylim(-4,4); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    ax.set_title('Critical Points: $f\'(x)=0$ at $x=\\pm1$', fontweight='bold')
    # Right: f' sign chart
    ax = axes[1]
    x_plot = np.linspace(-2.5, 2.5, 100)
    fp = 3*x_plot**2 - 3
    ax.plot(x_plot, fp, 'purple', lw=2.5, label="$f'(x)=3x^2-3$")
    ax.axhline(0, color='gray', lw=1)
    ax.fill_between(x_plot, 0, fp, where=(fp>0), alpha=0.2, color='green', label='$f\'>0$ (increasing)')
    ax.fill_between(x_plot, 0, fp, where=(fp<0), alpha=0.2, color='red', label='$f\'<0$ (decreasing)')
    for crit in [-1, 1]:
        ax.axvline(crit, color='orange', linestyle='--', lw=1.5)
        ax.plot(crit, 0, 'o', color='orange', markersize=8)
    ax.set_title("$f'$ Sign Test: + → − → max, − → + → min", fontweight='bold')
    ax.set_xlabel('x'); ax.set_ylabel("$f'(x)$")
    ax.set_xlim(-2.5,2.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle("First Derivative Test — Increasing/Decreasing", fontsize=14, fontweight='bold')
    save('15a-first-derivative-test.png')

def fig_cubic_analysis():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    x = np.linspace(-2, 4, 200)
    f = lambda x: x**3 - 3*x**2
    fp = lambda x: 3*x**2 - 6*x
    fpp = lambda x: 6*x - 6
    axes[0].plot(x, f(x), 'b-', lw=2.5, label='$f(x)=x^3-3x^2$')
    axes[0].plot(0,0,'ro',markersize=10); axes[0].plot(2,-4,'go',markersize=10); axes[0].plot(1,-2,'mo',markersize=10)
    axes[0].set_title('$f(x)$ — max at 0, min at 2\ninflection at 1', fontweight='bold'); axes[0].grid(True,alpha=0.3); axes[0].legend(fontsize=8)
    axes[1].plot(x, fp(x), 'r-', lw=2.5, label="$f'(x)=3x^2-6x$")
    axes[1].axhline(0,color='gray',lw=0.5); axes[1].plot([0,2],[0,0],'ko',markersize=8)
    axes[1].set_title("$f'(x)$ — zeros at $x=0,2$", fontweight='bold'); axes[1].grid(True,alpha=0.3); axes[1].legend(fontsize=8)
    axes[2].plot(x, fpp(x), 'g-', lw=2.5, label="$f''(x)=6x-6$")
    axes[2].axhline(0,color='gray',lw=0.5); axes[2].plot(1,0,'ko',markersize=8)
    axes[2].set_title("$f''(x)$ — zero at $x=1$\nconcavity change", fontweight='bold'); axes[2].grid(True,alpha=0.3); axes[2].legend(fontsize=8)
    fig.suptitle('Cubic Analysis — $f$, $f\'$, $f\'\'$ Together', fontsize=14, fontweight='bold')
    save('15a-cubic-analysis.png')

def fig_concavity_inflection():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-3, 3, 200)
    # Left: concave up vs down
    ax = axes[0]
    ax.plot(x, x**2, 'b-', lw=2.5, label='$f(x)=x^2$ (concave up)')
    ax.plot(x, -x**2, 'r-', lw=2.5, label='$g(x)=-x^2$ (concave down)')
    ax.plot(0,0,'ko',markersize=8)
    ax.set_title('Concavity: $f\'\'>0$ (cup) vs $f\'\'<0$ (cap)', fontweight='bold')
    ax.axhline(0,color='gray',lw=0.5); ax.axvline(0,color='gray',lw=0.5)
    ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    # Right: inflection point
    ax = axes[1]
    ax.plot(x, x**3, 'purple', lw=2.5, label='$f(x)=x^3$')
    ax.plot(0,0,'ro',markersize=12,zorder=5)
    ax.annotate('Inflection point\n$(0,0)$: $f\'\'=0$\ncurvature changes', (0,0), textcoords="offset points",
               xytext=(20,30), fontsize=10, color='red', fontweight='bold',
               arrowprops=dict(arrowstyle='->',color='red'))
    ax.axhline(0,color='gray',lw=0.5); ax.axvline(0,color='gray',lw=0.5)
    ax.set_xlim(-2,2); ax.set_ylim(-4,4); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    ax.set_title("$f'(0)=0$ but no extremum — inflection!", fontweight='bold')
    fig.suptitle('Concavity and Inflection Points', fontsize=14, fontweight='bold')
    save('15a-concavity-inflection.png')

def fig_complete_sketch():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    x_left = np.linspace(-2, 0.99, 200)
    x_right = np.linspace(1.01, 5, 200)
    f = lambda x: x**2/(x-1)
    # Left branches
    ax = axes[0]
    ax.plot(x_left, f(x_left), 'b-', lw=2.5, label='left branch')
    ax.plot(x_right, f(x_right), 'r-', lw=2.5, label='right branch')
    ax.axvline(1, color='red', linestyle='--', lw=2, label='VA: $x=1$')
    ax.plot(x_left, x_left+1, 'g--', lw=2, alpha=0.7, label='SA: $y=x+1$')
    ax.plot(x_right, x_right+1, 'g--', lw=2, alpha=0.7)
    ax.plot(0,0,'ro',markersize=10,zorder=5); ax.plot(2,4,'go',markersize=10,zorder=5)
    ax.annotate('Local max\n$(0,0)$', (0,0), textcoords="offset points", xytext=(-20,-30), fontsize=9, color='red', fontweight='bold')
    ax.annotate('Local min\n$(2,4)$', (2,4), textcoords="offset points", xytext=(10,15), fontsize=9, color='green', fontweight='bold')
    ax.set_title('$f(x)=\\frac{x^2}{x-1}$ — Complete Sketch', fontweight='bold')
    ax.set_xlim(-2,5); ax.set_ylim(-10,10); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: f' and f''
    ax = axes[1]
    x_plot = np.linspace(-2, 5, 500)
    mask = np.abs(x_plot - 1) > 0.05
    xp = x_plot[mask]
    fp = xp*(xp-2)/((xp-1)**2)
    fpp = 2/((xp-1)**3)
    ax.plot(xp, fp, 'b-', lw=2, label="$f'(x)$")
    ax.plot(xp, fpp, 'r-', lw=2, label="$f''(x)$")
    ax.axhline(0,color='gray',lw=0.5); ax.axvline(1,color='red',linestyle='--',lw=1.5)
    ax.plot([0,2],[0,0],'ko',markersize=6)
    ax.set_title("$f'$ and $f''$ — sign analysis", fontweight='bold')
    ax.set_xlim(-2,5); ax.set_ylim(-10,10); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Complete Curve Sketch — The 7-Step Method', fontsize=14, fontweight='bold')
    save('15a-complete-sketch.png')

if __name__ == "__main__":
    print("Generating 15A graphs...")
    fig_tangent_normal(); fig_mvt_geometry(); fig_first_derivative_test()
    fig_cubic_analysis(); fig_concavity_inflection(); fig_complete_sketch()
    print("Done! ✓")
