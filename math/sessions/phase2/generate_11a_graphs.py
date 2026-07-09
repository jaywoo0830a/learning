#!/usr/bin/env python3
"""
Generate all 14 graphs for 11A-trig-foundations.md — v3.
Large fonts, high DPI, clean rendering, no text-background boxes.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyBboxPatch
import os

plt.rcParams.update({
    'figure.dpi': 200,
    'font.size': 12,
    'font.family': 'sans-serif',
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'legend.fontsize': 9,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'axes.grid': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'text.usetex': False,
})

OUT = os.path.join(os.path.dirname(__file__), 'graphs')
os.makedirs(OUT, exist_ok=True)

def grid(ax):
    ax.grid(True, alpha=0.1, lw=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ══════════════════════════════════════════════════════════════════
# 1 — Radian definition
# ══════════════════════════════════════════════════════════════════
def fig1():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect('equal'); ax.set_xlim(-1.6, 2.1); ax.set_ylim(-1.4, 1.6)
    ax.axhline(0, color='#ccc', lw=0.6); ax.axvline(0, color='#ccc', lw=0.6)
    grid(ax); ax.set_xticks([]); ax.set_yticks([])

    t = np.linspace(0, 2*np.pi, 500)
    ax.plot(np.cos(t), np.sin(t), '#222', lw=2)
    ax.plot([0, 1], [0, 0], '#1a73e8', lw=4, label='radius $r$')
    ax.scatter([1], [0], color='#1a73e8', s=80, zorder=6)

    at = np.linspace(0, 1.0, 150)
    ax.plot(np.cos(at), np.sin(at), '#d93025', lw=4.5, label='arc $=r$')

    arc = Arc((0, 0), 0.7, 0.7, theta1=0, theta2=57.3, color='#d93025', lw=2, fill=False)
    ax.add_patch(arc)
    ax.text(0.42, 0.24, '1 rad\n≈ 57.3°', color='#d93025', fontsize=13, fontweight='bold')

    ax.text(0.5, -0.2, '$r$', color='#1a73e8', fontsize=16, fontweight='bold', ha='center')
    ax.text(0.45, 0.55, '$r$', color='#d93025', fontsize=16, fontweight='bold', ha='center')
    ax.scatter([0], [0], color='#222', s=45, zorder=6)

    ax.legend(loc='lower left', fontsize=10)
    ax.set_title('1 Radian — Arc Length = Radius', fontweight='bold', fontsize=15, pad=12)
    fig.tight_layout(pad=0.5)
    fig.savefig(os.path.join(OUT, '11a1-radian-definition.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 2 — Degrees ↔ Radians circle (BIGGER, CLEANER)
# ══════════════════════════════════════════════════════════════════
def fig2():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal'); ax.set_xlim(-1.75, 1.75); ax.set_ylim(-1.75, 1.75)
    ax.axhline(0, color='#ccc', lw=0.6); ax.axvline(0, color='#ccc', lw=0.6)
    grid(ax); ax.set_xticks([]); ax.set_yticks([])

    t = np.linspace(0, 2*np.pi, 600)
    ax.plot(np.cos(t), np.sin(t), '#222', lw=1.8)

    # Simpler labels — just the angle
    labels = {
        0:   '0°/0',
        30:  '30°  π/6',
        45:  '45°  π/4',
        60:  '60°  π/3',
        90:  '90°  π/2',
        120: '120°  2π/3',
        135: '135°  3π/4',
        150: '150°  5π/6',
        180: '180°  π',
        210: '210°  7π/6',
        225: '225°  5π/4',
        240: '240°  4π/3',
        270: '270°  3π/2',
        300: '300°  5π/3',
        315: '315°  7π/4',
        330: '330°  11π/6',
    }

    for deg, lbl in labels.items():
        r = np.deg2rad(deg)
        x, y = np.cos(r), np.sin(r)
        ax.scatter(x, y, color='#1a73e8', s=30, zorder=6)
        # Place text outside circle
        rx, ry = 1.35*x, 1.35*y
        ha = 'center' if abs(x) < 0.08 else ('left' if x > 0 else 'right')
        va = 'center' if abs(y) < 0.08 else ('bottom' if y > 0 else 'top')
        ax.text(rx, ry, lbl, color='#1a73e8', fontsize=8.5, ha=ha, va=va, fontweight='bold')

    ax.set_title('Degrees ↔ Radians on the Unit Circle', fontweight='bold', fontsize=15, pad=12)
    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT, '11a2-degree-radian-circle.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 3 — Unit circle (cos θ, sin θ)
# ══════════════════════════════════════════════════════════════════
def fig3():
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.set_aspect('equal'); ax.set_xlim(-1.6, 1.8); ax.set_ylim(-1.5, 1.5)
    ax.axhline(0, color='#ccc', lw=0.6); ax.axvline(0, color='#ccc', lw=0.6)
    grid(ax); ax.set_xticks([]); ax.set_yticks([])

    t = np.linspace(0, 2*np.pi, 600)
    ax.plot(np.cos(t), np.sin(t), '#222', lw=1.8)

    ang = np.deg2rad(55)
    x, y = np.cos(ang), np.sin(ang)
    ax.plot([0, x], [0, y], '#1a73e8', lw=2.8)
    ax.plot([x, x], [0, y], '#d93025', lw=2.2, ls='--')
    ax.plot([0, x], [y, y], '#188038', lw=2.2, ls='--')
    ax.scatter(x, y, color='#222', s=70, zorder=6)

    ax.text(x+0.1, y+0.1, f'$(\\cos\\theta,\\,\\sin\\theta)$\n$= ({x:.2f},\\,{y:.2f})$',
            fontsize=11, fontweight='bold')

    arc = Arc((0, 0), 0.6, 0.6, theta1=0, theta2=55, color='#1a73e8', lw=1.8, fill=False)
    ax.add_patch(arc)
    ax.text(0.28, 0.08, '$\\theta$', color='#1a73e8', fontsize=13)

    ax.text(x/2, -0.22, '$\\cos\\theta$', color='#188038', fontsize=11, ha='center')
    ax.text(x+0.2, y/2, '$\\sin\\theta$', color='#d93025', fontsize=11)

    for px, py, tt in [(1,0,'(1,0)'), (0,1,'(0,1)'), (-1,0,'(-1,0)'), (0,-1,'(0,-1)')]:
        ax.text(px*1.1, py*1.1, tt, fontsize=9, color='#555')

    ax.set_title('Unit Circle — $\\cos\\theta = x,\\; \\sin\\theta = y$', fontweight='bold', fontsize=14, pad=12)
    fig.tight_layout(pad=0.5)
    fig.savefig(os.path.join(OUT, '11a3-unit-circle-cos-sin.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 4 — Special angles
# ══════════════════════════════════════════════════════════════════
def fig4():
    fig, ax = plt.subplots(figsize=(8.5, 8.5))
    ax.set_aspect('equal'); ax.set_xlim(-1.6, 1.85); ax.set_ylim(-1.5, 1.65)
    ax.axhline(0, color='#ccc', lw=0.6); ax.axvline(0, color='#ccc', lw=0.6)
    grid(ax); ax.set_xticks([]); ax.set_yticks([])

    t = np.linspace(0, 2*np.pi, 600)
    ax.plot(np.cos(t), np.sin(t), '#222', lw=1.8)

    special = [
        (0,   '$0$',       '$(1,0)$'),
        (30,  '$\\frac{\\pi}{6}$', '$(\\frac{\\sqrt{3}}{2},\\frac{1}{2})$'),
        (45,  '$\\frac{\\pi}{4}$', '$(\\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2})$'),
        (60,  '$\\frac{\\pi}{3}$', '$(\\frac{1}{2},\\frac{\\sqrt{3}}{2})$'),
        (90,  '$\\frac{\\pi}{2}$', '$(0,1)$'),
    ]
    colors = ['#888', '#1a73e8', '#188038', '#e37400', '#c5221f']

    for (deg, rl, cl), c in zip(special, colors):
        rad = np.deg2rad(deg)
        x, y = np.cos(rad), np.sin(rad)
        ax.plot([0, x], [0, y], c, lw=2, alpha=0.5)
        ax.scatter(x, y, color=c, s=55, zorder=6)
        rx, ry = 1.28*x, 1.28*y
        ha = 'left' if x >= 0.01 else 'right'
        ax.text(rx, ry, f'{rl}  {cl}', color=c, fontsize=8.5, fontweight='bold',
                ha=ha, va='center')

    ax.set_title('Special Angles — Exact Coordinates', fontweight='bold', fontsize=14, pad=12)
    fig.tight_layout(pad=0.5)
    fig.savefig(os.path.join(OUT, '11a4-special-angles-unit-circle.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 5 — Reference angles + ASTC
# ══════════════════════════════════════════════════════════════════
def fig5():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 6))

    axL.set_aspect('equal'); axL.set_xlim(-1.5, 1.65); axL.set_ylim(-1.45, 1.55)
    axL.axhline(0, color='#ccc', lw=0.6); axL.axvline(0, color='#ccc', lw=0.6)
    grid(axL); axL.set_xticks([]); axL.set_yticks([])

    t = np.linspace(0, 2*np.pi, 600)
    axL.plot(np.cos(t), np.sin(t), '#222', lw=1.8)

    ang = np.deg2rad(150); ref = np.deg2rad(30)
    x, y = np.cos(ang), np.sin(ang)
    axL.plot([0, x], [0, y], '#d93025', lw=2.5)
    axL.scatter(x, y, color='#d93025', s=60, zorder=6)
    axL.plot([x, np.cos(ref)], [y, 0], '#d93025', lw=1.5, ls='--')
    axL.plot([0, np.cos(ref)], [0, 0], '#188038', lw=1.5, ls=':')

    arc_b = Arc((0, 0), 0.7, 0.7, theta1=0, theta2=150, color='#d93025', lw=1.5, fill=False)
    axL.add_patch(arc_b)
    axL.text(0.06, 0.45, '$\\frac{5\\pi}{6}$', color='#d93025', fontsize=13)
    arc_s = Arc((0, 0), 0.35, 0.35, theta1=0, theta2=30, color='#188038', lw=1.5, fill=False)
    axL.add_patch(arc_s)
    axL.text(0.30, 0.04, '$\\frac{\\pi}{6}$', color='#188038', fontsize=11)

    axL.text(-1.1, -0.55,
             '$\\sin\\frac{5\\pi}{6}=+\\frac{1}{2}$\n$\\cos\\frac{5\\pi}{6}=-\\frac{\\sqrt{3}}{2}$',
             color='#d93025', fontsize=11)
    axL.set_title('Reference Angle — Acute Angle to $x$-axis', fontweight='bold', fontsize=12)

    # ASTC
    axR.set_aspect('equal'); axR.set_xlim(-1.2, 1.2); axR.set_ylim(-1.2, 1.2)
    axR.axhline(0, color='#333', lw=1.2); axR.axvline(0, color='#333', lw=1.2)
    axR.set_xticks([]); axR.set_yticks([]); axR.set_frame_on(False)

    quads = [
        (0.55, 0.55,  'I\nsin+\ncos+\ntan+',        '#e8f5e9'),
        (-0.55, 0.55, 'II\nsin+\ncos−\ntan−',       '#e3f2fd'),
        (-0.55, -0.55,'III\nsin−\ncos−\ntan+',       '#fff3e0'),
        (0.55, -0.55, 'IV\nsin−\ncos+\ntan−',        '#fce4ec'),
    ]
    for cx, cy, txt, col in quads:
        rect = FancyBboxPatch((cx-0.55, cy-0.55), 1.1, 1.1,
                              boxstyle='round,pad=0.03', facecolor=col,
                              edgecolor='#aaa', alpha=0.75, lw=0.8)
        axR.add_patch(rect)
        axR.text(cx, cy, txt, ha='center', va='center', fontsize=11, fontweight='bold', color='#222')

    axR.set_title('ASTC — "All Students Take Calculus"', fontweight='bold', fontsize=12)
    fig.tight_layout(pad=1.5)
    fig.savefig(os.path.join(OUT, '11a5-reference-angles-astc.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 6 — sin & cos waves
# ══════════════════════════════════════════════════════════════════
def fig6():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
    for ax in (ax1, ax2): grid(ax)
    x = np.linspace(-np.pi/2, 3*np.pi, 800)

    ax1.plot(x, np.sin(x), '#d93025', lw=2.5)
    ax1.set_ylim(-1.4, 1.4)
    for xi in [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]:
        ax1.scatter(xi, np.sin(xi), color='#d93025', s=40, zorder=5)
    ax1.set_ylabel('$\\sin\\theta$', fontsize=14)
    ax1.set_title('$\\sin\\theta$  and  $\\cos\\theta$  —  Period $2\\pi$, $\\frac{\\pi}{2}$ Apart',
                  fontweight='bold', fontsize=15)

    ax2.plot(x, np.cos(x), '#1a73e8', lw=2.5)
    ax2.set_ylim(-1.4, 1.4)
    for xi in [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]:
        ax2.scatter(xi, np.cos(xi), color='#1a73e8', s=40, zorder=5)
    ax2.set_ylabel('$\\cos\\theta$', fontsize=14)

    xt = [-np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi]
    xl = ['$-\\frac{\\pi}{2}$','0','$\\frac{\\pi}{2}$','$\\pi$',
          '$\\frac{3\\pi}{2}$','$2\\pi$','$\\frac{5\\pi}{2}$','$3\\pi$']
    ax2.set_xticks(xt); ax2.set_xticklabels(xl, fontsize=10)
    ax2.set_xlabel('$\\theta$ (radians)', fontsize=14)
    ax2.set_xlim(-np.pi/2, 3*np.pi)

    for ax in (ax1, ax2):
        ax.plot([0, 2*np.pi], [-1.24, -1.24], color='#999', lw=1.2)
        ax.plot([0, 0], [-1.18, -1.30], color='#999', lw=0.8)
        ax.plot([2*np.pi, 2*np.pi], [-1.18, -1.30], color='#999', lw=0.8)
        ax.text(np.pi, -1.37, 'period $=2\\pi$', ha='center', fontsize=10, color='#555')

    fig.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT, '11a6-sin-cos-graphs.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 7 — tan graph
# ══════════════════════════════════════════════════════════════════
def fig7():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(14, 6))

    axL.set_aspect('equal'); axL.set_xlim(-1.5, 1.65); axL.set_ylim(-1.4, 2.2)
    axL.axhline(0, color='#ccc', lw=0.6); axL.axvline(0, color='#ccc', lw=0.6)
    grid(axL); axL.set_xticks([]); axL.set_yticks([])

    t = np.linspace(0, 2*np.pi, 600)
    axL.plot(np.cos(t), np.sin(t), '#222', lw=1.8)
    axL.plot([1, 1], [-1.4, 2.0], '#188038', lw=1.5, ls='--', alpha=0.5)
    axL.text(1.08, 1.85, '$x=1$\n(tangent line)', color='#188038', fontsize=10)

    ang = np.deg2rad(42); x, y = np.cos(ang), np.sin(ang)
    axL.plot([0, 1.6*x], [0, 1.6*y], '#1a73e8', lw=2.5)
    axL.scatter(x, y, color='#1a73e8', s=55, zorder=6)

    tv = np.tan(ang)
    if tv < 2.0:
        axL.scatter(1, tv, color='#d93025', s=60, zorder=6)
        axL.text(1.08, tv, f'$\\tan\\theta={tv:.2f}$', color='#d93025', fontsize=11, fontweight='bold')

    axL.set_title('Geometric: Slope of the Ray', fontweight='bold', fontsize=13)

    # Right: tan graph
    grid(axR)
    xt = np.linspace(-np.pi, 2*np.pi, 2500)
    yt = np.tan(xt)
    yt_m = np.ma.masked_where(np.abs(np.cos(xt)) < 0.012, yt)
    axR.plot(xt, yt_m, '#d93025', lw=2.2)
    axR.set_ylim(-5, 5)
    for n in range(-1, 3):
        a = np.pi/2 + n*np.pi
        if -np.pi <= a <= 2*np.pi:
            axR.axvline(a, color='#999', lw=1, ls='--', alpha=0.5)

    xtk = [-np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2]
    xlk = ['$-\\frac{\\pi}{2}$','0','$\\frac{\\pi}{2}$','$\\pi$','$\\frac{3\\pi}{2}$']
    axR.set_xticks(xtk); axR.set_xticklabels(xlk, fontsize=10)
    axR.set_title('$\\tan\\theta$ — Period $\\pi$, Asymptotes at $\\frac{\\pi}{2}+n\\pi$',
                  fontweight='bold', fontsize=13)
    axR.set_xlabel('$\\theta$'); axR.set_ylabel('$\\tan\\theta$')

    fig.tight_layout(pad=1)
    fig.savefig(os.path.join(OUT, '11a7-tan-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 8 — csc, sec, cot
# ══════════════════════════════════════════════════════════════════
def fig8():
    fig, axes = plt.subplots(3, 1, figsize=(11, 10.5))
    for ax in axes: grid(ax)

    x = np.linspace(-np.pi/2, 5*np.pi/2, 2500)
    xt = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2]
    xl = ['0','$\\frac{\\pi}{2}$','$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$','$\\frac{5\\pi}{2}$']

    yc = 1/np.sin(x); yc_m = np.ma.masked_where(np.abs(np.sin(x)) < 0.02, yc)
    axes[0].plot(x, yc_m, '#d93025', lw=2.2)
    axes[0].plot(x, np.sin(x), '#d93025', lw=0.6, alpha=0.2, ls='--')
    axes[0].set_ylim(-4.5, 4.5)
    axes[0].axhline(1, color='#ccc', lw=0.4, ls=':')
    axes[0].axhline(-1, color='#ccc', lw=0.4, ls=':')
    for n in range(0,4): axes[0].axvline(n*np.pi, color='#bbb', lw=0.6, ls='--', alpha=0.4)
    axes[0].set_title('$\\csc\\theta = 1/\\sin\\theta$    Range: $(-\\infty,-1]\\cup[1,\\infty)$',
                      fontweight='bold', fontsize=12)
    axes[0].set_ylabel('$\\csc\\theta$', fontsize=12)
    axes[0].set_xticks(xt); axes[0].set_xticklabels(xl)

    ys = 1/np.cos(x); ys_m = np.ma.masked_where(np.abs(np.cos(x)) < 0.02, ys)
    axes[1].plot(x, ys_m, '#1a73e8', lw=2.2)
    axes[1].plot(x, np.cos(x), '#1a73e8', lw=0.6, alpha=0.2, ls='--')
    axes[1].set_ylim(-4.5, 4.5)
    axes[1].axhline(1, color='#ccc', lw=0.4, ls=':')
    axes[1].axhline(-1, color='#ccc', lw=0.4, ls=':')
    for n in range(0,4): axes[1].axvline(np.pi/2+n*np.pi, color='#bbb', lw=0.6, ls='--', alpha=0.4)
    axes[1].set_title('$\\sec\\theta = 1/\\cos\\theta$', fontweight='bold', fontsize=12)
    axes[1].set_ylabel('$\\sec\\theta$', fontsize=12)
    axes[1].set_xticks(xt); axes[1].set_xticklabels(xl)

    xc = np.linspace(0.02, 2*np.pi-0.02, 2500)
    yco = 1/np.tan(xc); yco_m = np.ma.masked_where(np.abs(np.sin(xc)) < 0.02, yco)
    axes[2].plot(xc, yco_m, '#188038', lw=2.2)
    axes[2].set_ylim(-4.5, 4.5)
    for n in range(0,3): axes[2].axvline(n*np.pi, color='#bbb', lw=0.6, ls='--', alpha=0.4)
    axes[2].set_title('$\\cot\\theta = 1/\\tan\\theta = \\cos\\theta/\\sin\\theta$',
                      fontweight='bold', fontsize=12)
    axes[2].set_ylabel('$\\cot\\theta$', fontsize=12)
    axes[2].set_xticks(xt); axes[2].set_xticklabels(xl)
    axes[2].set_xlabel('$\\theta$ (radians)', fontsize=13)

    fig.tight_layout(pad=1)
    fig.savefig(os.path.join(OUT, '11a8-csc-sec-cot-graphs.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 9 — All six functions on unit circle
# ══════════════════════════════════════════════════════════════════
def fig9():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal'); ax.set_xlim(-2.6, 3.2); ax.set_ylim(-2.3, 2.6)
    ax.axhline(0, color='#ccc', lw=0.6); ax.axvline(0, color='#ccc', lw=0.6)
    grid(ax); ax.set_xticks([]); ax.set_yticks([])

    t = np.linspace(0, 2*np.pi, 600)
    ax.plot(np.cos(t), np.sin(t), '#222', lw=2.2)

    ang = np.deg2rad(52); x, y = np.cos(ang), np.sin(ang)
    ax.plot([0, 2.3*x], [0, 2.3*y], '#777', lw=1, alpha=0.3)
    ax.scatter(x, y, color='#222', s=60, zorder=6)
    ax.text(x+0.12, y+0.12, '$(\\cos,\\sin)$', fontsize=10, fontweight='bold')

    ax.plot([1, 1], [-3.5, 3.5], '#188038', lw=0.8, ls='--', alpha=0.25)
    ax.plot([-3.5, 3.5], [1, 1], '#188038', lw=0.8, ls='--', alpha=0.25)

    # sin
    ax.plot([x, x], [0, y], '#d93025', lw=3)
    ax.text(x-0.3, y/2, '$\\sin$', color='#d93025', fontsize=10, ha='right', fontweight='bold')
    # cos
    ax.plot([0, x], [0, 0], '#1a73e8', lw=3)
    ax.text(x/2, -0.28, '$\\cos$', color='#1a73e8', fontsize=10, ha='center', fontweight='bold')

    tv = np.tan(ang)
    if abs(tv) < 2.4:
        ax.scatter(1, tv, color='#e37400', s=50, zorder=6)
        ax.text(1.15, tv, '$\\tan$', color='#e37400', fontsize=10, fontweight='bold')
    cv = 1/tv
    if abs(cv) < 2.6:
        ax.scatter(cv, 1, color='#9334e6', s=50, zorder=6)
        ax.text(cv-0.1, 1.16, '$\\cot$', color='#9334e6', fontsize=10, fontweight='bold', ha='center')
    sx = 1/np.cos(ang)
    if sx < 3.0:
        ax.scatter(sx, 0, color='#00838f', s=50, zorder=6)
        ax.text(sx+0.1, -0.28, '$\\sec$', color='#00838f', fontsize=10, fontweight='bold')
    cs = 1/np.sin(ang)
    if cs < 2.4:
        ax.scatter(0, cs, color='#c5221f', s=50, zorder=6)
        ax.text(-0.28, cs+0.1, '$\\csc$', color='#c5221f', fontsize=10, fontweight='bold', ha='right')

    # Legend top-left
    legends = [
        ('$\\sin\\theta$','#d93025'),('$\\cos\\theta$','#1a73e8'),
        ('$\\tan\\theta$','#e37400'),('$\\cot\\theta$','#9334e6'),
        ('$\\sec\\theta$','#00838f'),('$\\csc\\theta$','#c5221f'),
    ]
    for i, (lb, cl) in enumerate(legends):
        ax.text(-2.4, 2.3 - i*0.34, lb, color=cl, fontsize=11, fontweight='bold')

    ax.set_title('All Six Trig Functions from One Diagram', fontweight='bold', fontsize=14, pad=12)
    fig.tight_layout(pad=0.5)
    fig.savefig(os.path.join(OUT, '11a9-six-functions-unit-circle.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 10 — Transformations (4 panels)
# ══════════════════════════════════════════════════════════════════
def fig10():
    fig, axes = plt.subplots(2, 2, figsize=(14, 10.5))
    for ax in axes.flat: grid(ax)
    x = np.linspace(0, 2*np.pi, 600)
    xt = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xl = ['0','$\\frac{\\pi}{2}$','$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$']

    ax = axes[0,0]
    ax.plot(x, np.sin(x), '#bbb', lw=1.5, alpha=0.6, label='$\\sin\\theta$')
    ax.plot(x, 2*np.sin(x), '#d93025', lw=3, label='$2\\sin\\theta$')
    ax.set_ylim(-3.2, 3.2); ax.set_title('Amplitude: $A=2$', fontweight='bold', fontsize=12)
    ax.legend(fontsize=10); ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=9)

    ax = axes[0,1]
    ax.plot(x, np.sin(x), '#bbb', lw=1.5, alpha=0.6, label='$\\sin\\theta$')
    ax.plot(x, np.sin(3*x), '#1a73e8', lw=3, label='$\\sin 3\\theta$')
    ax.set_ylim(-1.6, 1.6); ax.set_title('Period: $B=3$, $T=\\frac{2\\pi}{3}$', fontweight='bold', fontsize=12)
    ax.legend(fontsize=10); ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=9)

    ax = axes[1,0]
    ax.plot(x, np.sin(x), '#bbb', lw=1.5, alpha=0.6, label='$\\sin\\theta$')
    y3 = 2*np.sin(3*x - np.pi/2) + 1
    ax.plot(x, y3, '#188038', lw=3, label='$2\\sin(3\\theta-\\frac{\\pi}{2})+1$')
    ax.set_ylim(-2.8, 4.2); ax.set_title('Full transform: $A=2,\\,B=3,\\,C/B=\\frac{\\pi}{6},\\,D=1$',
                                         fontweight='bold', fontsize=12)
    ax.legend(fontsize=9); ax.set_xticks(xt); ax.set_xticklabels(xl, fontsize=9)

    ax = axes[1,1]
    xt2 = np.linspace(0, np.pi, 600)
    yt0 = np.tan(xt2); yt0_m = np.ma.masked_where(np.abs(np.cos(xt2)) < 0.015, yt0)
    yt1 = np.tan(2*xt2+np.pi/4); yt1_m = np.ma.masked_where(np.abs(np.cos(2*xt2+np.pi/4)) < 0.015, yt1)
    ax.plot(xt2, yt0_m, '#bbb', lw=1.5, alpha=0.6, label='$\\tan\\theta$')
    ax.plot(xt2, yt1_m, '#e37400', lw=3, label='$\\tan(2\\theta+\\frac{\\pi}{4})$')
    ax.set_ylim(-6, 6); ax.set_title('$\\tan$: $T=\\frac{\\pi}{2}$, shift $=-\\frac{\\pi}{8}$',
                                     fontweight='bold', fontsize=12)
    ax.legend(fontsize=10)
    xtt = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    xlt = ['0','$\\frac{\\pi}{4}$','$\\frac{\\pi}{2}$','$\\frac{3\\pi}{4}$','$\\pi$']
    ax.set_xticks(xtt); ax.set_xticklabels(xlt, fontsize=9)

    fig.suptitle('Transformations: $A\\cdot\\operatorname{trig}(B\\theta-C)+D$, Step by Step',
                 fontweight='bold', fontsize=15, y=0.99)
    fig.tight_layout(pad=1, rect=[0, 0, 1, 0.96])
    fig.savefig(os.path.join(OUT, '11a10-trig-transformations.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 11 — arcsin
# ══════════════════════════════════════════════════════════════════
def fig11():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    for ax in (ax1, ax2): grid(ax)

    xs = np.linspace(-np.pi/2, np.pi/2, 400)
    ax1.plot(xs, np.sin(xs), '#d93025', lw=3)
    ax1.set_xlim(-1.9, 1.9); ax1.set_ylim(-1.6, 1.6)
    ax1.plot([-1.9, 1.9], [-1.9, 1.9], '#bbb', lw=0.8, ls='--', alpha=0.5)
    ax1.axvspan(-np.pi/2, np.pi/2, alpha=0.06, color='#d93025')
    ax1.set_title('$y=\\sin\\theta$  on  $[-\\frac{\\pi}{2},\\frac{\\pi}{2}]$', fontweight='bold', fontsize=13)
    ax1.set_xlabel('$\\theta$', fontsize=13); ax1.set_ylabel('$\\sin\\theta$', fontsize=13)

    xa = np.linspace(-1, 1, 400)
    ax2.plot(xa, np.arcsin(xa), '#d93025', lw=3)
    ax2.set_xlim(-1.5, 1.5); ax2.set_ylim(-1.9, 1.9)
    ax2.plot([-1.5, 1.5], [-1.5, 1.5], '#bbb', lw=0.8, ls='--', alpha=0.5)
    ax2.axhline(np.pi/2, color='#bbb', lw=0.6, ls=':')
    ax2.axhline(-np.pi/2, color='#bbb', lw=0.6, ls=':')
    ax2.set_title('$y=\\arcsin x$  —  Mirror Across $y=x$', fontweight='bold', fontsize=13)
    ax2.set_xlabel('$x$', fontsize=13); ax2.set_ylabel('$\\arcsin x$', fontsize=13)
    ax2.text(0.3, np.pi/2+0.08, '$y=\\frac{\\pi}{2}$', fontsize=10, color='#888')
    ax2.text(0.3, -np.pi/2-0.15, '$y=-\\frac{\\pi}{2}$', fontsize=10, color='#888')

    fig.tight_layout(pad=1.5)
    fig.savefig(os.path.join(OUT, '11a11-arcsin-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 12 — arccos
# ══════════════════════════════════════════════════════════════════
def fig12():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    for ax in (ax1, ax2): grid(ax)

    xs = np.linspace(0, np.pi, 400)
    ax1.plot(xs, np.cos(xs), '#1a73e8', lw=3)
    ax1.set_xlim(-0.5, 3.6); ax1.set_ylim(-1.6, 3.6)
    ax1.plot([-0.5, 3.6], [-0.5, 3.6], '#bbb', lw=0.8, ls='--', alpha=0.5)
    ax1.axvspan(0, np.pi, alpha=0.06, color='#1a73e8')
    ax1.set_title('$y=\\cos\\theta$  on  $[0,\\pi]$', fontweight='bold', fontsize=13)
    ax1.set_xlabel('$\\theta$', fontsize=13); ax1.set_ylabel('$\\cos\\theta$', fontsize=13)

    xa = np.linspace(-1, 1, 400)
    ax2.plot(xa, np.arccos(xa), '#1a73e8', lw=3)
    ax2.set_xlim(-1.5, 1.5); ax2.set_ylim(-0.5, 3.6)
    ax2.plot([-1.5, 1.5], [-1.5, 1.5], '#bbb', lw=0.8, ls='--', alpha=0.5)
    ax2.axhline(np.pi, color='#bbb', lw=0.6, ls=':')
    ax2.set_title('$y=\\arccos x$  —  Mirror Across $y=x$', fontweight='bold', fontsize=13)
    ax2.set_xlabel('$x$', fontsize=13); ax2.set_ylabel('$\\arccos x$', fontsize=13)
    ax2.text(0.3, np.pi+0.1, '$y=\\pi$', fontsize=10, color='#888')

    fig.tight_layout(pad=1.5)
    fig.savefig(os.path.join(OUT, '11a12-arccos-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 13 — arctan
# ══════════════════════════════════════════════════════════════════
def fig13():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    for ax in (ax1, ax2): grid(ax)

    xs = np.linspace(-np.pi/2+0.03, np.pi/2-0.03, 500)
    ax1.plot(xs, np.tan(xs), '#e37400', lw=3)
    ax1.set_xlim(-2.3, 2.3); ax1.set_ylim(-6, 6)
    ax1.plot([-2.3, 2.3], [-2.3, 2.3], '#bbb', lw=0.8, ls='--', alpha=0.5)
    ax1.axvline(-np.pi/2, color='#bbb', lw=0.8, ls='--')
    ax1.axvline(np.pi/2, color='#bbb', lw=0.8, ls='--')
    ax1.axvspan(-np.pi/2, np.pi/2, alpha=0.06, color='#e37400')
    ax1.set_title('$y=\\tan\\theta$  on  $(-\\frac{\\pi}{2},\\frac{\\pi}{2})$', fontweight='bold', fontsize=13)
    ax1.set_xlabel('$\\theta$', fontsize=13); ax1.set_ylabel('$\\tan\\theta$', fontsize=13)

    xa = np.linspace(-6, 6, 600)
    ax2.plot(xa, np.arctan(xa), '#e37400', lw=3)
    ax2.set_xlim(-6.5, 6.5); ax2.set_ylim(-2.3, 2.3)
    ax2.plot([-6.5, 6.5], [-2.3, 2.3], '#bbb', lw=0.8, ls='--', alpha=0.5)
    ax2.axhline(np.pi/2, color='#bbb', lw=0.6, ls=':')
    ax2.axhline(-np.pi/2, color='#bbb', lw=0.6, ls=':')
    ax2.set_title('$y=\\arctan x$  —  S-Curve, $(-\\frac{\\pi}{2},\\frac{\\pi}{2})$', fontweight='bold', fontsize=13)
    ax2.set_xlabel('$x$', fontsize=13); ax2.set_ylabel('$\\arctan x$', fontsize=13)
    ax2.text(-5.5, np.pi/2+0.08, '$y=\\frac{\\pi}{2}$', fontsize=10, color='#888')
    ax2.text(-5.5, -np.pi/2-0.15, '$y=-\\frac{\\pi}{2}$', fontsize=10, color='#888')

    fig.tight_layout(pad=1.5)
    fig.savefig(os.path.join(OUT, '11a13-arctan-graph.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
# 14 — arcsin(sin x) sawtooth
# ══════════════════════════════════════════════════════════════════
def fig14():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9))
    for ax in (ax1, ax2): grid(ax)

    xf = np.linspace(-2*np.pi, 2*np.pi, 2500)
    y_sin = np.sin(xf); y_as = np.arcsin(y_sin)
    ax1.plot(xf, y_sin, '#1a73e8', lw=1.5, alpha=0.45, label='$\\sin x$')
    ax1.plot(xf, y_as, '#d93025', lw=2.8, label='$\\arcsin(\\sin x)$')
    ax1.axhline(np.pi/2, color='#bbb', lw=0.6, ls=':')
    ax1.axhline(-np.pi/2, color='#bbb', lw=0.6, ls=':')
    ax1.axvspan(-np.pi/2, np.pi/2, alpha=0.04, color='#d93025')
    ax1.set_ylim(-2, 2)
    ax1.set_title('$\\arcsin(\\sin x)$  —  Sawtooth Wave', fontweight='bold', fontsize=15)
    ax1.legend(fontsize=11, loc='upper right')
    ax1.set_ylabel('$y$', fontsize=13)

    ax1.text(2*np.pi+0.4, 0, 'Range of\n$\\arcsin$:\n$[-\\frac{\\pi}{2},\\frac{\\pi}{2}]$',
             color='#d93025', fontsize=10, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', fc='#fff5f5', alpha=0.85, ec='#d93025', lw=0.8))

    xt = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xl = ['$-2\\pi$','$-\\frac{3\\pi}{2}$','$-\\pi$','$-\\frac{\\pi}{2}$','0',
          '$\\frac{\\pi}{2}$','$\\pi$','$\\frac{3\\pi}{2}$','$2\\pi$']
    ax1.set_xticks(xt); ax1.set_xticklabels(xl, fontsize=9)

    xa = np.linspace(-1, 1, 400)
    ax2.plot(xa, np.sin(np.arcsin(xa)), '#d93025', lw=3, label='$\\sin(\\arcsin x)=x$')
    ax2.plot([-1.3, 1.3], [-1.3, 1.3], '#bbb', lw=0.8, ls='--', alpha=0.5, label='$y=x$')
    ax2.set_xlim(-1.3, 1.3); ax2.set_ylim(-1.3, 1.3)
    ax2.set_title('$\\sin(\\arcsin x) = x$  for all  $x \\in [-1,1]$', fontweight='bold', fontsize=15)
    ax2.legend(fontsize=11, loc='upper left')
    ax2.set_xlabel('$x$', fontsize=13); ax2.set_ylabel('$y$', fontsize=13)

    fig.tight_layout(pad=1.5)
    fig.savefig(os.path.join(OUT, '11a14-arcsin-composition.png'), bbox_inches='tight')
    plt.close(fig)

# ══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    funcs = [fig1, fig2, fig3, fig4, fig5, fig6, fig7,
             fig8, fig9, fig10, fig11, fig12, fig13, fig14]
    for i, f in enumerate(funcs, 1):
        print(f'[{i:2d}/14] {f.__name__}...')
        f()
    print(f'\nDone → {OUT}/')
