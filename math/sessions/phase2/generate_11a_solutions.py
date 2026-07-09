#!/usr/bin/env python3
"""Generate solution graphs for 11A-solutions.md"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import os

plt.rcParams.update({
    'figure.dpi': 200, 'font.size': 11, 'font.family': 'sans-serif',
    'axes.titlesize': 12, 'axes.labelsize': 11,
    'legend.fontsize': 9, 'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.grid': False, 'figure.facecolor': 'white', 'axes.facecolor': 'white',
})
OUT = os.path.join(os.path.dirname(__file__), 'graphs')
os.makedirs(OUT, exist_ok=True)

def g(ax):
    ax.grid(True, alpha=0.1, lw=0.3)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)

# ── P3: y = -3cos(2θ + π/3) - 1 ──────────────────────────────────
def p3():
    fig, ax = plt.subplots(figsize=(10, 5.5)); g(ax)
    x = np.linspace(-np.pi/2, np.pi, 600)
    y = -3*np.cos(2*x + np.pi/3) - 1
    ax.plot(x, y, '#d93025', lw=2.5)
    ax.axhline(-1, color='#999', lw=0.8, ls='--', alpha=0.5, label='midline $y=-1$')

    # Key points
    kx = [-np.pi/6, np.pi/12, np.pi/3, 7*np.pi/12, 5*np.pi/6]
    ky = [-4, -1, 2, -1, -4]
    ax.scatter(kx, ky, color='#1a73e8', s=50, zorder=5)
    for xi, yi in zip(kx, ky):
        ax.annotate(f'({xi/np.pi:.2f}π, {yi})', (xi, yi), textcoords="offset points",
                    xytext=(0, -18 if yi < 0 else 12), ha='center', fontsize=7.5, color='#1a73e8')

    ax.set_ylim(-5.5, 3.5)
    ax.set_title('Practice 3: $y = -3\\cos(2\\theta + \\pi/3) - 1$  (Amp=3, T=$\\pi$, shift=$-\\pi/6$)', fontweight='bold')
    ax.set_xlabel('$\\theta$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=8)
    xt = [-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    xl = ['$-\\pi/2$','$-\\pi/4$','0','$\\pi/4$','$\\pi/2$','$3\\pi/4$','$\\pi$']
    ax.set_xticks(xt); ax.set_xticklabels(xl)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'sol11a-p3-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ── P5: Right triangles ──────────────────────────────────────────
def p5():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))
    for ax in (ax1, ax2):
        ax.set_aspect('equal'); ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.5, 6)
        ax.axis('off')

    # Triangle 1: arccos(5/13)
    ax1.plot([0,5], [0,0], '#1a73e8', lw=3, label='adj = 5')
    ax1.plot([0,0], [0,12], '#d93025', lw=3, label='opp = 12')
    ax1.plot([0,5], [12,0], '#333', lw=3, label='hyp = 13')
    ax1.text(2.5, -0.4, 'adj = 5', ha='center', color='#1a73e8', fontweight='bold', fontsize=11)
    ax1.text(-0.6, 6, 'opp = 12', ha='center', rotation=90, color='#d93025', fontweight='bold', fontsize=11)
    ax1.text(2.2, 7.2, 'hyp = 13', ha='center', rotation=-67, color='#333', fontweight='bold', fontsize=11)
    ax1.text(0.4, 0.6, '$\\alpha$', fontsize=13, color='#333')
    ax1.set_title('$\\alpha = \\arccos\\frac{5}{13}$', fontweight='bold', fontsize=12)
    ax1.legend(fontsize=8, loc='lower right')

    # Triangle 2: arcsin(4/5)
    ax2.plot([0,3], [0,0], '#1a73e8', lw=3, label='adj = 3')
    ax2.plot([3,3], [0,4], '#d93025', lw=3, label='opp = 4')
    ax2.plot([0,3], [4,0], '#333', lw=3, label='hyp = 5')
    ax2.text(1.5, -0.4, 'adj = 3', ha='center', color='#1a73e8', fontweight='bold', fontsize=11)
    ax2.text(3.6, 2, 'opp = 4', ha='center', color='#d93025', fontweight='bold', fontsize=11)
    ax2.text(1.2, 2.8, 'hyp = 5', ha='center', rotation=-53, color='#333', fontweight='bold', fontsize=11)
    ax2.text(0.4, 0.4, '$\\beta$', fontsize=13, color='#333')
    ax2.set_title('$\\beta = \\arcsin\\frac{4}{5}$', fontweight='bold', fontsize=12)
    ax2.legend(fontsize=8, loc='lower right')

    fig.suptitle('Practice 5: Right Triangles for Inverse Trig', fontweight='bold', fontsize=13)
    fig.tight_layout(pad=0.5)
    fig.savefig(os.path.join(OUT, 'sol11a-p5-triangles.png'), bbox_inches='tight')
    plt.close(fig)

# ── P8: arcsin(sin x) + sin(arcsin x) ────────────────────────────
def p8():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.5))
    for ax in (ax1, ax2): g(ax)

    xf = np.linspace(-2*np.pi, 2*np.pi, 2500)
    y_sin = np.sin(xf); y_as = np.arcsin(y_sin)
    ax1.plot(xf, y_sin, '#1a73e8', lw=1.2, alpha=0.4, label='$\\sin x$')
    ax1.plot(xf, y_as, '#d93025', lw=2.5, label='$\\arcsin(\\sin x)$')
    ax1.axhline(np.pi/2, color='#999', lw=0.5, ls=':')
    ax1.axhline(-np.pi/2, color='#999', lw=0.5, ls=':')
    ax1.axvspan(-np.pi/2, np.pi/2, alpha=0.04, color='#d93025')
    ax1.set_ylim(-2, 2)
    ax1.set_title('$\\arcsin(\\sin x)$ — Sawtooth / Triangle Wave', fontweight='bold', fontsize=12)
    ax1.legend(fontsize=10)
    xt = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xl = ['$-2\\pi$','$-3\\pi/2$','$-\\pi$','$-\\pi/2$','0','$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$']
    ax1.set_xticks(xt); ax1.set_xticklabels(xl, fontsize=8)
    # Annotate the folding
    ax1.annotate('$x$', xy=(0.5, 0.5), fontsize=10, color='#d93025', fontweight='bold')
    ax1.annotate('$\\pi-x$', xy=(2.2, 1.0), fontsize=9, color='#d93025')

    xa = np.linspace(-1, 1, 300)
    ax2.plot(xa, np.sin(np.arcsin(xa)), '#d93025', lw=2.5, label='$\\sin(\\arcsin x)=x$')
    ax2.plot([-1.3, 1.3], [-1.3, 1.3], '#999', lw=0.7, ls='--', alpha=0.5, label='$y=x$')
    ax2.set_xlim(-1.3, 1.3); ax2.set_ylim(-1.3, 1.3)
    ax2.set_title('$\\sin(\\arcsin x) = x$  on  $[-1,1]$', fontweight='bold', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.set_xlabel('$x$')

    fig.tight_layout(pad=1.2)
    fig.savefig(os.path.join(OUT, 'sol11a-p8-composition.png'), bbox_inches='tight')
    plt.close(fig)

# ── P10: All six trig functions ──────────────────────────────────
def p10():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    for ax in (ax1, ax2): g(ax)
    x = np.linspace(0, 2*np.pi, 1500)

    # Top: sin, cos, tan
    ax1.plot(x, np.sin(x), '#d93025', lw=2.2, label='$\\sin\\theta$')
    ax1.plot(x, np.cos(x), '#1a73e8', lw=2.2, label='$\\cos\\theta$')
    yt = np.tan(x); yt_m = np.ma.masked_where(np.abs(np.cos(x)) < 0.015, yt)
    ax1.plot(x, yt_m, '#188038', lw=2.2, label='$\\tan\\theta$')
    ax1.set_ylim(-4, 4)
    ax1.axvline(np.pi/2, color='#188038', lw=0.8, ls='--', alpha=0.4)
    ax1.axvline(3*np.pi/2, color='#188038', lw=0.8, ls='--', alpha=0.4)
    ax1.set_title('$\\sin$, $\\cos$, $\\tan$ on $[0, 2\\pi]$', fontweight='bold', fontsize=13)
    ax1.legend(fontsize=10, loc='lower left')
    xt = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xl = ['0','$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$']
    ax1.set_xticks(xt); ax1.set_xticklabels(xl)

    # Bottom: csc, sec, cot
    yc = 1/np.sin(x); yc_m = np.ma.masked_where(np.abs(np.sin(x)) < 0.02, yc)
    ys = 1/np.cos(x); ys_m = np.ma.masked_where(np.abs(np.cos(x)) < 0.02, ys)
    yco = 1/np.tan(x[1:-1]); yco_m = np.ma.masked_where(np.abs(np.sin(x[1:-1])) < 0.02, yco)
    ax2.plot(x, yc_m, '#d93025', lw=2.2, label='$\\csc\\theta$')
    ax2.plot(x, ys_m, '#1a73e8', lw=2.2, label='$\\sec\\theta$')
    ax2.plot(x[1:-1], yco_m, '#188038', lw=2.2, label='$\\cot\\theta$')
    ax2.set_ylim(-4, 4)
    for a in [0, np.pi, 2*np.pi]: ax2.axvline(a, color='#d93025', lw=0.6, ls='--', alpha=0.3)
    for a in [np.pi/2, 3*np.pi/2]: ax2.axvline(a, color='#1a73e8', lw=0.6, ls='--', alpha=0.3)
    ax2.set_title('$\\csc$, $\\sec$, $\\cot$ on $[0, 2\\pi]$', fontweight='bold', fontsize=13)
    ax2.legend(fontsize=10, loc='lower left')
    ax2.set_xticks(xt); ax2.set_xticklabels(xl)
    ax2.set_xlabel('$\\theta$')

    fig.tight_layout(pad=1.5)
    fig.savefig(os.path.join(OUT, 'sol11a-p10-six-graphs.png'), bbox_inches='tight')
    plt.close(fig)

# ── A1: y = 2csc(θ - π/4) ────────────────────────────────────────
def a1():
    fig, ax = plt.subplots(figsize=(10, 5.5)); g(ax)
    x = np.linspace(0, 2*np.pi, 2500)
    y = 2/np.sin(x - np.pi/4); y_m = np.ma.masked_where(np.abs(np.sin(x - np.pi/4)) < 0.02, y)
    ax.plot(x, y_m, '#d93025', lw=2.5)
    ax.set_ylim(-5, 5)
    for a in [np.pi/4, 5*np.pi/4]: ax.axvline(a, color='#999', lw=0.8, ls='--', alpha=0.5)
    ax.scatter([3*np.pi/4], [2], color='#1a73e8', s=60, zorder=5)
    ax.annotate('$(3\\pi/4, 2)$ min', (3*np.pi/4, 2), textcoords="offset points",
                xytext=(10, 10), fontsize=9, color='#1a73e8', fontweight='bold')
    ax.scatter([7*np.pi/4], [-2], color='#1a73e8', s=60, zorder=5)
    ax.annotate('$(7\\pi/4, -2)$ max', (7*np.pi/4, -2), textcoords="offset points",
                xytext=(10, -18), fontsize=9, color='#1a73e8', fontweight='bold')
    ax.set_title('A1: $y = 2\\csc(\\theta - \\pi/4)$ on $[0, 2\\pi]$', fontweight='bold', fontsize=12)
    ax.set_xlabel('$\\theta$')
    xt = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi]
    xl = ['0','$\\pi/4$','$\\pi/2$','$3\\pi/4$','$\\pi$','$5\\pi/4$','$3\\pi/2$','$7\\pi/4$','$2\\pi$']
    ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'sol11a-a1-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ── A2: y = -2sin(θ/2 + π/3) ────────────────────────────────────
def a2():
    fig, ax = plt.subplots(figsize=(11, 5)); g(ax)
    x = np.linspace(-2*np.pi, 4*np.pi, 1000)
    y = -2*np.sin(x/2 + np.pi/3)
    ax.plot(x, y, '#1a73e8', lw=2.5)
    ax.axhline(0, color='#999', lw=0.6, ls='--', alpha=0.4, label='midline $y=0$')
    ax.set_ylim(-2.5, 2.5)
    # x-intercepts
    zx = [-2*np.pi/3, 4*np.pi/3, 10*np.pi/3]
    for zxi in zx:
        ax.scatter(zxi, 0, color='#d93025', s=50, zorder=5)
    ax.set_title('A2: $y = -2\\sin(\\theta/2 + \\pi/3)$  (Amp=2, T=$4\\pi$, shift=$-2\\pi/3$)', fontweight='bold', fontsize=12)
    ax.set_xlabel('$\\theta$'); ax.set_ylabel('$y$')
    ax.legend(fontsize=8)
    xt = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi]
    xl = ['$-2\\pi$','$-\\pi$','0','$\\pi$','$2\\pi$','$3\\pi$','$4\\pi$']
    ax.set_xticks(xt); ax.set_xticklabels(xl)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'sol11a-a2-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ── A3: y = 3tan(θ/2 - π/6) ─────────────────────────────────────
def a3():
    fig, ax = plt.subplots(figsize=(11, 5)); g(ax)
    x = np.linspace(-np.pi, 3*np.pi, 3000)
    arg = x/2 - np.pi/6
    y = 3*np.tan(arg); y_m = np.ma.masked_where(np.abs(np.cos(arg)) < 0.015, y)
    ax.plot(x, y_m, '#e37400', lw=2.5)
    ax.set_ylim(-6, 6)
    for a in [-2*np.pi/3, 4*np.pi/3]:
        if -np.pi <= a <= 3*np.pi:
            ax.axvline(a, color='#999', lw=0.8, ls='--', alpha=0.5)
    # Zero crossings
    for z in [np.pi/3, 7*np.pi/3]:
        if -np.pi <= z <= 3*np.pi:
            ax.scatter(z, 0, color='#d93025', s=50, zorder=5)
    ax.set_title('A3: $y = 3\\tan(\\theta/2 - \\pi/6)$  (T=$2\\pi$, shift=$\\pi/3$)', fontweight='bold', fontsize=12)
    ax.set_xlabel('$\\theta$')
    xt = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi]
    xl = ['$-\\pi$','$-\\pi/2$','0','$\\pi/2$','$\\pi$','$3\\pi/2$','$2\\pi$','$5\\pi/2$','$3\\pi$']
    ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'sol11a-a3-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ── A9: Ferris wheel ─────────────────────────────────────────────
def a9():
    fig, ax = plt.subplots(figsize=(10, 5.5)); g(ax)
    x = np.linspace(0, 2*np.pi/3, 400)
    y = 4*np.sin(3*x - np.pi/2) + 2
    ax.plot(x, y, '#d93025', lw=2.5)
    ax.axhline(2, color='#999', lw=0.8, ls='--', alpha=0.5, label='midline $y=2$')
    ax.set_ylim(-3, 7.5)

    # Key points
    pts = [(0, -2), (np.pi/6, 2), (np.pi/3, 6), (np.pi/2, 2), (2*np.pi/3, -2)]
    for xi, yi in pts:
        ax.scatter(xi, yi, color='#1a73e8', s=50, zorder=5)
    ax.annotate('max = 6 m', (np.pi/3, 6), textcoords="offset points",
                xytext=(0, 12), ha='center', fontsize=10, color='#1a73e8', fontweight='bold')
    ax.annotate('min = −2 m', (2*np.pi/3, -2), textcoords="offset points",
                xytext=(0, -20), ha='center', fontsize=10, color='#1a73e8', fontweight='bold')

    ax.set_title('A9: Ferris Wheel $f(\\theta)=4\\sin(3\\theta-\\pi/2)+2$  (1 period)', fontweight='bold', fontsize=12)
    ax.set_xlabel('$\\theta$ (minutes)'); ax.set_ylabel('Height (meters)')
    ax.legend(fontsize=8)
    xt = [0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3]
    xl = ['0','$\\pi/6$','$\\pi/3$','$\\pi/2$','$2\\pi/3$']
    ax.set_xticks(xt); ax.set_xticklabels(xl)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, 'sol11a-a9-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    for f in [p3, p5, p8, p10, a1, a2, a3, a9]:
        print(f'  {f.__name__}...')
        f()
    print(f'Done → {OUT}/')
