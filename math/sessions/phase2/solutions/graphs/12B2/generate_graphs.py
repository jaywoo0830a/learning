#!/usr/bin/env python3
"""12B2 Sequences Advanced — visual graphs (recursive/geometric focus)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Arrow

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'savefig.dpi': 150, 'font.size': 10})

def save(fig, name):
    fig.savefig(f'{OUT}/{name}', bbox_inches='tight', facecolor='white', pad_inches=0.15)
    plt.close(fig)

# ── P1: Telescoping 1/k(k+1) = 20/21 ──────────────────────────
def p1():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    k = np.arange(1, 21)
    terms = 1/(k*(k+1)); sn = np.cumsum(terms)

    # Left: terms + partial sums
    a1.bar(k, terms, color='#3498DB', alpha=0.6, ec='white', width=0.6, label='1/k(k+1)')
    a1.plot(k, sn, 'o-', color='#E74C3C', lw=2.5, ms=7, label='S_n')
    a1.axhline(1, color='#27AE60', lw=2, ls='--', alpha=0.7)
    a1.plot(20, sn[-1], 'o', color='#E74C3C', ms=12, zorder=10)
    a1.set_xlabel('k'); a1.set_ylabel('Value')
    a1.set_title('Telescoping: middle cancels', fontweight='bold')
    a1.legend(fontsize=9); a1.grid(True, alpha=0.15)

    # Right: cancellation visualization (recursive pairs)
    y = np.arange(20, 0, -1)
    for i, ki in enumerate(k):
        a2.barh(y[i], 1/ki, height=0.5, color='#3498DB', alpha=0.5, left=0)
        a2.barh(y[i], -1/(ki+1), height=0.5, color='#E74C3C', alpha=0.5, left=1/ki)
    # Cancellation arrows between adjacent rows
    for i in range(19):
        a2.annotate('', xy=(1/(i+2), y[i+1]), xytext=(1/(i+2), y[i]),
                    arrowprops=dict(arrowstyle='<->', color='#27AE60', lw=1.2, alpha=0.5))
    a2.axvline(0, color='gray', lw=0.5)
    a2.set_xlabel('Value'); a2.set_ylabel('k')
    a2.set_yticks(y); a2.set_yticklabels([str(kk) for kk in k])
    a2.set_title('1/k cancels with -1/(k+1)', fontweight='bold')
    a2.grid(True, alpha=0.1, axis='x')

    plt.tight_layout(); save(fig, 'p1-telescoping.png')

# ── P2: Recurrence a_{n+1}=2a_n+3 (cobweb) ────────────────────
def p2():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5.5))
    n = np.arange(1, 11)
    an = 2**(n+1) - 3

    # Left: sequence growing
    a1.stem(n, an, linefmt='#E74C3C', markerfmt='o', basefmt='gray')
    a1.plot(n, an, '#C0392B', lw=2, alpha=0.4)
    for i, v in enumerate(an):
        a1.text(n[i], v+3, str(v), ha='center', fontsize=8, color='#C0392B')
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_title('Sequence: a_{n+1}=2a_n+3, a_1=1', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: cobweb diagram (recursive fixed point)
    x = np.linspace(-4, 30, 300)
    a2.plot(x, 2*x+3, '#3498DB', lw=2, label='f(x)=2x+3')
    a2.plot(x, x, '#333', lw=1.5, ls='--', alpha=0.4, label='y=x')
    a2.plot(-3, -3, 'o', color='#27AE60', ms=12, zorder=10)  # fixed point

    # Cobweb steps
    a = 1
    sx, sy = [a], [a]
    for _ in range(6):
        b = 2*a + 3
        sx += [a, b]; sy += [b, b]
        a = b
    a2.plot(sx, sy, '-', color='#E74C3C', lw=1.5, alpha=0.7)
    a2.plot(sx, sy, 'o', color='#E74C3C', ms=5)

    a2.set_xlim(-4, 30); a2.set_ylim(-4, 30)
    a2.set_aspect('equal')
    a2.set_xlabel('a_n'); a2.set_ylabel('a_{n+1}')
    a2.set_title('Cobweb: fixed point at -3', fontweight='bold')
    a2.legend(fontsize=9); a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p2-recurrence.png')

# ── P3: Repeated root r=2 ──────────────────────────────────────
def p3():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    n = np.arange(1, 11)
    an = 2**n

    # Left: sequence a_n = 2^n
    a1.stem(n, an, linefmt='#8E44AD', markerfmt='o', basefmt='gray')
    a1.plot(n, an, '#7D3C98', lw=2, alpha=0.4)
    for i, v in enumerate(an):
        a1.text(n[i], v+8, str(v), ha='center', fontsize=8, color='#7D3C98')
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_title('a_n = 2^n  (repeated root)', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: characteristic polynomial touching zero
    r = np.linspace(-1, 5, 200)
    a2.plot(r, r**2-4*r+4, '#3498DB', lw=2.5)
    a2.axhline(0, color='gray', lw=1)
    a2.axvline(2, color='#E74C3C', lw=2, ls='--', alpha=0.7)
    a2.plot(2, 0, 'o', color='#E74C3C', ms=12, zorder=10)
    a2.set_xlabel('r'); a2.set_ylabel('r^2 - 4r + 4')
    a2.set_title('Characteristic: (r-2)^2=0 (tangent)', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p3-repeated-root.png')

# ── P4: Method of differences ─────────────────────────────────
def p4():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    n = np.arange(1, 11)
    an = np.array([2,5,10,17,26,37,50,65,82,101])
    diffs = np.diff(an)

    # Left: sequence bars
    a1.bar(n, an, color=plt.cm.Blues(np.linspace(0.3,0.9,10)), ec='#2980B9', lw=0.5, width=0.6)
    a1.plot(n, an, 'o-', color='#2980B9', lw=2, ms=6)
    for i, v in enumerate(an):
        a1.text(n[i], v+3, str(v), ha='center', fontsize=7, color='#2980B9')
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_title('Original sequence a_n', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: differences (recursive structure)
    a2.stem(n[1:], diffs, linefmt='#E74C3C', markerfmt='o', basefmt='gray')
    a2.plot(n[1:], diffs, '#C0392B', lw=2, alpha=0.4)
    for i, d in enumerate(diffs):
        a2.text(n[i+1], d+0.8, str(d), ha='center', fontsize=8, color='#C0392B')
    a2.set_xlabel('n'); a2.set_ylabel('Differences')
    a2.set_title('First differences: arithmetic (d=2)', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p4-differences.png')

# ── P5: Grouped sequence ───────────────────────────────────────
def p5():
    fig, ax = plt.subplots(figsize=(12, 7))
    colors = plt.cm.Set2(np.linspace(0, 1, 10))
    yp = 0
    for g in range(1, 11):
        nums = list(range(1 + g*(g-1)//2, 1 + g*(g-1)//2 + g))
        xp = 0
        for num in nums:
            ax.add_patch(Rectangle((xp, yp), 1, 0.8, color=colors[g-1], alpha=0.6, ec='white', lw=1.5))
            ax.text(xp+0.5, yp+0.4, str(num), ha='center', va='center', fontsize=8)
            xp += 1
        yp += 1.2
    ax.set_xlim(-0.5, 14); ax.set_ylim(-0.5, 13)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('Group n has n numbers (groups 1-10 shown)', fontweight='bold')
    save(fig, 'p5-grouped.png')

# ── P6: Induction (domino recursive) ───────────────────────────
def p6():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    n = np.arange(1, 9)
    sc = np.array([(i*(i+1)//2)**2 for i in n])
    sn = n*(n+1)//2

    # Left: sum of cubes = (sum n)^2
    a1.plot(n, sc, 'o-', color='#E74C3C', lw=2.5, ms=8, label='sum k^3')
    a1.plot(n, sn**2, '--', color='#3498DB', lw=2, alpha=0.6, label='(sum k)^2')
    for i, v in enumerate(sc):
        a1.text(n[i], v+20, str(v), ha='center', fontsize=8, color='#E74C3C')
    a1.set_xlabel('n'); a1.set_ylabel('Value')
    a1.set_title('Sum k^3 = (sum k)^2', fontweight='bold')
    a1.legend(fontsize=9); a1.grid(True, alpha=0.15)

    # Right: domino chain (recursive proof)
    ax_dom = a2  # use the right subplot
    for i in range(1, 8):
        h = i*0.12 + 0.3
        col = plt.cm.Reds(0.3 + 0.6*i/8)
        ax_dom.add_patch(Rectangle((i-0.3, 0), 0.6, h, color=col, alpha=0.7, ec='#333', lw=1, zorder=10))
        ax_dom.text(i, h/2, f'n={i}', ha='center', va='center', fontsize=7, fontweight='bold')
    for i in range(1, 7):
        ax_dom.annotate('', xy=(i+0.6, 0.15), xytext=(i+1-0.6, 0.15),
                    arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2))
    ax_dom.set_xlim(0, 8); ax_dom.set_ylim(-0.2, 2)
    ax_dom.set_aspect('equal'); ax_dom.axis('off')
    ax_dom.set_title('Domino: base + step => all n', fontweight='bold')

    plt.tight_layout(); save(fig, 'p6-induction.png')

# ── P7: Limit convergence ─────────────────────────────────────
def p7():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    n = np.arange(1, 51)
    an = (5*n**3 - 2*n + 1)/(3*n**3 + n**2 + 4)

    # Left: sequence converging
    a1.plot(n, an, '-', color='#3498DB', lw=1.5, alpha=0.4)
    a1.plot(n, an, 'o', color='#3498DB', ms=3)
    a1.axhline(5/3, color='#E74C3C', lw=2.5, ls='--')
    a1.set_xlabel('n'); a1.set_ylabel('a_n')
    a1.set_title('Limit = 5/3', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: gap shrinking
    gap = np.abs(an - 5/3)
    a2.semilogy(n, gap, 'o-', color='#E74C3C', lw=2, ms=4)
    a2.axhline(0.01, color='#27AE60', lw=1.5, ls='--', alpha=0.7)
    a2.set_xlabel('n'); a2.set_ylabel('|a_n - L| (log)')
    a2.set_title('Gap shrinks to zero', fontweight='bold')
    a2.grid(True, alpha=0.15, which='both')

    plt.tight_layout(); save(fig, 'p7-limit.png')

# ── P8: Radical telescoping ───────────────────────────────────
def p8():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    k = np.arange(1, 100)
    sn = np.cumsum(1/(np.sqrt(k)+np.sqrt(k+1)))

    # Left: partial sums
    a1.plot(k, sn, '-', color='#3498DB', lw=1.5, alpha=0.4)
    a1.plot(k, sn, 'o', color='#3498DB', ms=2)
    a1.axhline(9, color='#E74C3C', lw=2.5, ls='--')
    a1.plot(99, sn[-1], 'o', color='#E74C3C', ms=12, zorder=10)
    a1.set_xlabel('k'); a1.set_ylabel('S_n')
    a1.set_title('Telescoping: sqrt(100)-1 = 9', fontweight='bold')
    a1.grid(True, alpha=0.15)

    # Right: rationalization structure
    a2.axis('off')
    info = '1/(sqrt(k)+sqrt(k+1))\n  = sqrt(k+1)-sqrt(k)\n\nSum telescopes to\nsqrt(100)-1 = 9'
    a2.text(0.5, 0.5, info, ha='center', va='center', fontsize=14, transform=a2.transAxes,
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8))
    a2.set_title('Rationalization step', fontweight='bold')

    plt.tight_layout(); save(fig, 'p8-radical-telescoping.png')

# ── P9: Fibonacci & golden ratio ───────────────────────────────
def p9():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(14, 5.5))

    # Generate Fibonacci recursively
    F = np.zeros(18, dtype=int)
    F[1] = F[2] = 1
    for i in range(3, 18):
        F[i] = F[i-1] + F[i-2]

    nv = np.arange(1, 16)
    cumF = np.cumsum(F[1:16])

    # Left: Fibonacci + cumulative
    a1.bar(nv, F[1:16], color='#F39C12', alpha=0.6, ec='#E67E22', width=0.6, label='F_n')
    a1.plot(nv, cumF, 'o-', color='#E74C3C', lw=2.5, ms=7, label='sum F_k')
    a1.plot(nv, F[3:18]-1, '--', color='#3498DB', lw=2, alpha=0.7, label='F_{n+2}-1')
    for i in range(8):
        a1.text(nv[i], F[i+1]+2, str(F[i+1]), ha='center', fontsize=8, color='#E67E22', fontweight='bold')
    a1.set_xlabel('n'); a1.set_ylabel('Value')
    a1.set_title('Sum F_k = F_{n+2} - 1', fontweight='bold')
    a1.legend(fontsize=9); a1.grid(True, alpha=0.15)

    # Right: ratio converging to phi
    ratios = F[2:17] / F[1:16]
    phi = (1+np.sqrt(5))/2
    a2.plot(nv, ratios, 'o-', color='#8E44AD', lw=2.5, ms=8)
    a2.axhline(phi, color='#E74C3C', lw=2.5, ls='--')
    a2.axhline(phi-0.01, color='gray', lw=0.8, ls=':', alpha=0.4)
    a2.axhline(phi+0.01, color='gray', lw=0.8, ls=':', alpha=0.4)
    for i, r in enumerate(ratios):
        a2.text(nv[i], r+0.015, f'{r:.4f}', ha='center', fontsize=6.5, color='#8E44AD')
    a2.set_xlabel('n'); a2.set_ylabel('F_{n+1}/F_n')
    a2.set_title('Ratio -> phi = (1+sqrt(5))/2', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p9-fibonacci.png')

# ── P10: Second differences -> quadratic ───────────────────────
def p10():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 5))
    n = np.arange(1, 9)
    an = n**2 - 1
    d1 = np.diff(an)
    d2 = np.diff(d1)

    # Left: sequence and first differences
    a1.plot(n, an, 'o-', color='#3498DB', lw=2.5, ms=8, label='a_n=n^2-1')
    a1.plot(n[1:], d1, 's--', color='#E74C3C', lw=2, ms=7, label='1st diff')
    for i, v in enumerate(an):
        a1.text(n[i], v+1.5, str(v), ha='center', fontsize=8, color='#3498DB')
    a1.set_xlabel('n'); a1.set_ylabel('Value')
    a1.set_title('Sequence & first differences', fontweight='bold')
    a1.legend(fontsize=9); a1.grid(True, alpha=0.15)

    # Right: constant second differences
    a2.stem(n[2:], d2, linefmt='#27AE60', markerfmt='o', basefmt='gray')
    a2.axhline(2, color='#27AE60', lw=2, ls='--', alpha=0.7)
    a2.set_xlabel('n'); a2.set_ylabel('2nd difference')
    a2.set_title('Constant 2nd diff => quadratic', fontweight='bold')
    a2.grid(True, alpha=0.15)

    plt.tight_layout(); save(fig, 'p10-second-diff.png')

# ── P11: Squeeze theorem ──────────────────────────────────────
def p11():
    fig, ax = plt.subplots(figsize=(10, 6))
    n = np.arange(1, 31)
    an = np.cos(n)/n
    up = 1/n; low = -1/n

    ax.fill_between(n, low, up, alpha=0.1, color='#27AE60')
    ax.plot(n, up, '--', color='#27AE60', lw=2, label='+1/n')
    ax.plot(n, low, '--', color='#27AE60', lw=2, label='-1/n')
    ax.stem(n, an, linefmt='#E74C3C', markerfmt='o', basefmt='gray')
    ax.axhline(0, color='#333', lw=1)
    ax.set_xlabel('n'); ax.set_ylabel('cos(n)/n')
    ax.set_title('Squeeze: -1/n <= cos(n)/n <= 1/n -> 0', fontweight='bold')
    ax.legend(fontsize=9); ax.grid(True, alpha=0.15)
    plt.tight_layout(); save(fig, 'p11-squeeze.png')

# ── P12: Harmonic divergence by grouping ───────────────────────
def p12():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(14, 5.5))
    n = np.arange(1, 101)
    H = np.cumsum(1/n)

    # Left: harmonic grows slowly
    a1.plot(n, H, '-', color='#3498DB', lw=2)
    a1.plot(n, np.log(n)+0.577, '--', color='#E74C3C', lw=2, alpha=0.7, label='ln n + gamma')
    a1.set_xlabel('n'); a1.set_ylabel('H_n')
    a1.set_title('Harmonic series grows like ln n', fontweight='bold')
    a1.legend(fontsize=9); a1.grid(True, alpha=0.15)

    # Right: grouping proof (recursive blocks)
    colors = plt.cm.Reds(np.linspace(0.2, 0.8, 6))
    groups = [(1,1,1),(2,2,0.5),(3,4,0.5),(5,8,0.5),(9,16,0.5),(17,32,0.5)]
    for idx, (s, e, ms) in enumerate(groups):
        for k in range(s, e+1):
            if k <= 40:
                a2.barh(k, 1/k, height=0.6, color=colors[idx], alpha=0.6)
        if e <= 40:
            a2.plot([0.4, 0.4], [s-0.3, e+0.3], color='#E74C3C', lw=2)
            a2.text(0.45, (s+e)/2, f'>{ms}', va='center', fontsize=9, color='#E74C3C', fontweight='bold')
    a2.set_xlabel('Value'); a2.set_ylabel('k')
    a2.set_title('Each group sums to > 1/2 => diverges', fontweight='bold')
    a2.grid(True, alpha=0.1, axis='x')

    plt.tight_layout(); save(fig, 'p12-harmonic.png')

if __name__ == '__main__':
    for name, fn in [('P1',p1),('P2',p2),('P3',p3),('P4',p4),('P5',p5),
                     ('P6',p6),('P7',p7),('P8',p8),('P9',p9),('P10',p10),
                     ('P11',p11),('P12',p12)]:
        fn(); print(f'  12B2 {name}')
