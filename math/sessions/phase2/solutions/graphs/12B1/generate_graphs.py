#!/usr/bin/env python3
"""12B1 Sequences Foundations — visual graphs (recursive/geometric focus)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'savefig.dpi': 150, 'font.size': 10})

def save(fig, name):
    fig.savefig(f'{OUT}/{name}', bbox_inches='tight', facecolor='white', pad_inches=0.15)
    plt.close(fig)

# ── P1: Arithmetic 5,9,13,…  a20=81 S20=860 ────────────────────
def p1():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5))
    n = np.arange(1, 21)
    an = 5 + (n-1)*4

    # Left: stem + line
    a1.stem(n, an, linefmt='#3498DB', markerfmt='o', basefmt='gray', bottom=0)
    a1.plot(n, an, '#E74C3C', lw=2, alpha=0.5)
    a1.plot(20, 81, 'o', color='#E74C3C', markersize=14, zorder=10)
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_title('Arithmetic: a_n = 4n+1', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: sum via pairing (recursive visual)
    colors = plt.cm.Blues(np.linspace(0.3, 0.9, 10))
    a2.bar(n[:10], an[:10], color=colors, ec='white', lw=1, width=0.7)
    colors2 = plt.cm.Reds(np.linspace(0.3, 0.9, 10))
    a2.bar(n[10:], an[10:], color=colors2, ec='white', lw=1, width=0.7, alpha=0.6)
    # Pairing lines
    for i in range(5):
        a2.plot([1+i, 20-i], [an[i], an[19-i]], '-', color='#8E44AD', lw=1, alpha=0.5)
    a2.axhline(an[0]+an[-1], color='#27AE60', lw=2, ls='--', alpha=0.7)
    a2.set_xlabel('n'); a2.set_ylabel('a_n')
    a2.set_title('S_20 = 10 x (5+81) = 860', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p1-arithmetic.png')

# ── P2: Geometric 3,6,12,… S8=765 ──────────────────────────────
def p2():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5))
    n = np.arange(1, 9)
    an = 3 * 2**(n-1)
    sn = np.cumsum(an)

    # Left: exponential bars
    colors = plt.cm.Oranges(np.linspace(0.3, 0.95, 8))
    a1.bar(n, an, color=colors, ec='#D35400', lw=1, width=0.6)
    a1.plot(n, an, 'o-', color='#C0392B', lw=2, ms=6)
    for i, v in enumerate(an):
        a1.text(n[i], v+8, str(v), ha='center', fontsize=8)
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_title('Geometric: a_n = 3*2^{n-1}', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: cumulative sum growing
    a2.bar(n, an, color=plt.cm.PuBu(np.linspace(0.3, 0.9, 8)), ec='#2980B9', lw=1, width=0.6, alpha=0.5, label='terms')
    a2.plot(n, sn, 'o-', color='#E74C3C', lw=2.5, ms=8, label='S_n')
    a2.axhline(765, color='#27AE60', lw=2, ls='--')
    for i, s in enumerate(sn):
        a2.text(n[i], s+12, str(s), ha='center', fontsize=7, color='#E74C3C', fontweight='bold')
    a2.set_xlabel('n'); a2.set_ylabel('Sum')
    a2.set_title('S_8 = 765', fontweight='bold')
    a2.legend(fontsize=9); a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p2-geometric.png')

# ── P3: Infinite 5 + 5/3 + 5/9 + … = 15/2 ─────────────────────
def p3():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5))
    n = np.arange(1, 13)
    an = 5*(1/3)**(n-1)
    sn = np.cumsum(an)

    # Left: terms decaying
    a1.bar(n, an, color=plt.cm.Greens(np.linspace(0.3, 0.9, 12)), ec='#27AE60', lw=0.5, width=0.6)
    a1.axhline(0, color='gray', lw=0.5)
    for i, v in enumerate(an):
        if v > 0.03:
            a1.text(n[i], v+0.1, f'{v:.3f}', ha='center', fontsize=6)
    a1.set_xlabel('k'); a1.set_ylabel('a_k')
    a1.set_title('Terms shrink: r=1/3', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: partial sums converging
    a2.plot(n, sn, 'o-', color='#E74C3C', lw=2.5, ms=8)
    a2.axhline(7.5, color='#27AE60', lw=2.5, ls='--')
    a2.fill_between(n, sn, 7.5, alpha=0.1, color='#27AE60')
    for i, s in enumerate(sn):
        a2.text(n[i], s+0.15, f'{s:.3f}', ha='center', fontsize=6, color='#E74C3C')
    a2.set_xlabel('n'); a2.set_ylabel('S_n')
    a2.set_title('S_inf = 5/(1-1/3) = 7.5', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p3-infinite-sum.png')

# ── P4: Constant sequence (both arithmetic & geometric) ────────
def p4():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.5))
    n = np.arange(1, 11); c = 5

    # Left: constant line
    a1.stem(n, [c]*10, linefmt='#3498DB', markerfmt='o', basefmt='gray')
    a1.axhline(c, color='#E74C3C', lw=2, ls='--', alpha=0.6)
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_ylim(0, 8)
    a1.set_title('Constant: d=0 (arith), r=1 (geom)', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: bar chart
    a2.bar(n, [c]*10, color='#27AE60', alpha=0.6, ec='#1E8449', lw=1, width=0.6)
    a2.set_xlabel('n'); a2.set_ylabel('a_n')
    a2.set_ylim(0, 8)
    a2.set_title('All terms equal: a_n = 5', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p4-constant.png')

# ── P5: Sum of odds = n² (L-shaped gnomons) ────────────────────
def p5():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # Left: recursive L-shaped gnomons building squares
    for n in range(1, 7):
        odd = 2*n - 1
        col = plt.cm.viridis(n/6)
        # horizontal bar
        a1.add_patch(Rectangle((n-1, 0), 1, n, color=col, alpha=0.7, ec='white', lw=1))
        # vertical bar (minus corner)
        a1.add_patch(Rectangle((0, n-1), n-1, 1, color=col, alpha=0.7, ec='white', lw=1))
        a1.text(n-0.5, n-0.5, str(odd), ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    a1.set_xlim(-0.5, 6.5); a1.set_ylim(-0.5, 6.5)
    a1.set_aspect('equal'); a1.axis('off')
    a1.set_title('L-gnomons: 1+3+5+... = n^2', fontweight='bold')

    # Right: cumulative sum = n^2
    n = np.arange(1, 11)
    cs = np.cumsum(2*n-1)
    a2.plot(n, cs, 'o-', color='#E74C3C', lw=2.5, ms=8, label='sum odds')
    a2.plot(n, n**2, '--', color='#3498DB', lw=2, alpha=0.6, label='n^2')
    for i, v in enumerate(cs):
        a2.text(n[i], v+2, str(v), ha='center', fontsize=8, color='#E74C3C')
    a2.set_xlabel('n'); a2.set_ylabel('Sum')
    a2.set_title('Sum_{k=1}^n (2k-1) = n^2', fontweight='bold')
    a2.legend(fontsize=9); a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p5-sum-odds.png')

# ── P6: Bouncing ball (recursive heights) ──────────────────────
def p6():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Left: recursive bounce heights
    H = 20; r = 0.75; nb = 8
    for i in range(nb):
        h = H * r**i
        t = np.linspace(0, 1, 50)
        a1.plot(i+t, h - h*t**2, color='#3498DB', lw=2.5)
        if i < nb-1:
            h2 = H * r**(i+1)
            a1.plot(i+1+t, h2*(1-t)**2, color='#E74C3C', lw=2, alpha=0.5)
    a1.axhline(0, color='#333', lw=1.5)
    a1.set_xlabel('Bounce'); a1.set_ylabel('Height (m)')
    a1.set_title('Recursive bounce heights', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: distance per segment
    segs = [20] + [2*20*r**i for i in range(1, 10)]
    colors = ['#E74C3C'] + ['#3498DB']*9
    a2.bar(range(len(segs)), segs, color=colors, alpha=0.7, ec='white')
    a2.axhline(140, color='#27AE60', lw=2.5, ls='--')
    for i, d in enumerate(segs):
        if d > 1:
            a2.text(i, d+2, f'{d:.1f}', ha='center', fontsize=7)
    a2.set_xlabel('Segment'); a2.set_ylabel('Distance (m)')
    a2.set_title('Total = 20 + 40*0.75/(1-0.75) = 140m', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p6-bouncing-ball.png')

# ── P7: Compound interest ──────────────────────────────────────
def p7():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5))
    yr = np.arange(0, 31)
    amt = 2000 * 1.045**yr

    # Left: exponential curve
    a1.plot(yr, amt, color='#27AE60', lw=2.5)
    a1.fill_between(yr, 2000, amt, alpha=0.12, color='#27AE60')
    a1.axhline(2000, color='gray', lw=1, ls='--', alpha=0.4)
    a1.plot(20, amt[20], 'o', color='#E74C3C', ms=12, zorder=10)
    a1.axhline(4000, color='#E74C3C', lw=1, ls=':', alpha=0.5)
    a1.set_xlabel('Year'); a1.set_ylabel('Amount ($)')
    a1.set_title('$2000 at 4.5% APR', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: log scale (geometric -> linear)
    a2.semilogy(yr, amt, color='#2980B9', lw=2.5)
    a2.semilogy(yr, amt, 'o', color='#2980B9', ms=3, alpha=0.4)
    a2.set_xlabel('Year'); a2.set_ylabel('Amount (log)')
    a2.set_title('Log scale: straight line = geometric', fontweight='bold')
    a2.grid(True, alpha=0.15, which='both')

    plt.tight_layout(); save(fig, 'p7-compound.png')

# ── P8: Recover a_n from S_n = 3n^2+2n ────────────────────────
def p8():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5))
    n = np.arange(1, 11)
    Sn = 3*n**2 + 2*n
    an = 6*n - 1

    # Left: Sn curve
    a1.plot(n, Sn, 'o-', color='#3498DB', lw=2.5, ms=8)
    for i, s in enumerate(Sn):
        a1.text(n[i], s+5, str(s), ha='center', fontsize=8, color='#3498DB')
    a1.set_xlabel('n'); a1.set_ylabel('S_n')
    a1.set_title('S_n = 3n^2 + 2n', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: recovered an (difference)
    a2.stem(n, an, linefmt='#E74C3C', markerfmt='o', basefmt='gray')
    a2.plot(n, an, '#C0392B', lw=2, alpha=0.4)
    # Show recursive relation: a_n = S_n - S_{n-1}
    for i, v in enumerate(an):
        a2.text(n[i], v+2, str(v), ha='center', fontsize=8, color='#C0392B')
    a2.set_xlabel('n'); a2.set_ylabel('a_n')
    a2.set_title('a_n = S_n - S_{n-1} = 6n-1', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p8-recover.png')

# ── P9: a1=4, S_inf=10, find r ────────────────────────────────
def p9():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5))
    n = np.arange(1, 11)
    an = 4*(0.6)**(n-1)
    sn = 4*(1-0.6**n)/(1-0.6)

    # Left: terms + partial sums
    a1.bar(n-0.2, an, width=0.35, color='#3498DB', alpha=0.6, label='a_k')
    a1.plot(n, sn, 'o-', color='#E74C3C', lw=2.5, ms=8, label='S_n')
    a1.axhline(10, color='#27AE60', lw=2, ls='--', label='S_inf=10')
    a1.set_xlabel('n'); a1.set_ylabel('Value')
    a1.set_title('a1=4, r=3/5, S_inf=10', fontweight='bold')
    a1.legend(fontsize=9); a1.grid(True, alpha=0.15)

    # Right: gap shrinks exponentially
    gap = 10 - sn
    a2.semilogy(n, gap, 'o-', color='#E74C3C', lw=2.5, ms=8, label='gap')
    a2.axhline(0.01, color='#27AE60', lw=2, ls='--', label='0.01')
    a2.set_xlabel('n'); a2.set_ylabel('Gap (log)')
    a2.set_title('Exponential decay of gap', fontweight='bold')
    a2.legend(fontsize=9); a2.grid(True, alpha=0.15, which='both')

    plt.tight_layout(); save(fig, 'p9-geometric-series.png')

# ── P10: Recursive subdivision 1/3+1/9+…=1/2 ──────────────────
def p10():
    fig, axes = plt.subplots(2, 3, figsize=(10, 7))
    for step, ax in enumerate(axes.flat, 1):
        ax.set_xlim(0, 3); ax.set_ylim(0, 1)
        ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(Rectangle((0,0), 3, 1, fill=False, ec='#333', lw=2))

        # Recursive subdivision: shade 1/3 of remaining each time
        remain_x, remain_y = 0, 0
        remain_w, remain_h = 3, 1
        colors = ['#E74C3C', '#3498DB', '#27AE60', '#F39C12', '#9B59B6', '#1ABC9C']

        for i in range(step):
            if i == 0:
                # Shade left 1/3 of full
                ax.add_patch(Rectangle((0, 0), 1, 1, color=colors[0], alpha=0.7))
                remain_x, remain_y = 1, 0
                remain_w, remain_h = 2, 1
            elif i == 1:
                # Shade bottom 1/3 of remaining
                ax.add_patch(Rectangle((remain_x, 0), remain_w, remain_h/3, color=colors[1], alpha=0.7))
                remain_x, remain_y = remain_x, remain_h/3
                remain_w, remain_h = remain_w, remain_h*2/3
            elif i == 2:
                # Shade left 1/3 of remaining
                ax.add_patch(Rectangle((remain_x, remain_y), remain_w/3, remain_h, color=colors[2], alpha=0.7))
                remain_x, remain_y = remain_x + remain_w/3, remain_y
                remain_w, remain_h = remain_w*2/3, remain_h
            elif i % 2 == 1:
                # Bottom 1/3 of remaining
                ax.add_patch(Rectangle((remain_x, remain_y), remain_w, remain_h/3, color=colors[i], alpha=0.7))
                remain_y = remain_y + remain_h/3
                remain_h = remain_h*2/3
            else:
                # Left 1/3 of remaining
                ax.add_patch(Rectangle((remain_x, remain_y), remain_w/3, remain_h, color=colors[i], alpha=0.7))
                remain_x = remain_x + remain_w/3
                remain_w = remain_w*2/3

        total = sum([(1/3)*(1/3)**i for i in range(step)])
        ax.set_title(f'Step {step}: area={total:.4f}', fontsize=9)

    fig.suptitle('Recursive subdivision: 1/3 + 1/9 + 1/27 + ... = 1/2', fontweight='bold')
    plt.tight_layout(); save(fig, 'p10-visual-proof.png')

if __name__ == '__main__':
    for name, fn in [('P1',p1),('P2',p2),('P3',p3),('P4',p4),('P5',p5),
                     ('P6',p6),('P7',p7),('P8',p8),('P9',p9),('P10',p10)]:
        fn(); print(f'  12B1 {name}')
