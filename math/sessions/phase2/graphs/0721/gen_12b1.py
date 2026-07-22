#!/usr/bin/env python3
"""Generate all graph images for Session 12B1: Sequences and Series — Foundations."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/12B1"
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    'figure.dpi': 150,
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
})

def save(name):
    plt.tight_layout(pad=1.5)
    plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"  ✓ {name}")

# ============================================================
# 12b1a-arithmetic-line.png
# ============================================================
def fig_arithmetic_line():
    """Arithmetic sequence as points on a line — constant slope = common difference."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    n_vals = np.arange(1, 11)
    a1, d = 3, 2
    a_n = a1 + (n_vals - 1) * d

    # Left: Points on the line
    ax1.plot(n_vals, a_n, 'bo-', lw=2, markersize=8)
    for i, (n, val) in enumerate(zip(n_vals, a_n)):
        ax1.plot(n, val, 'bo', markersize=8)
        ax1.text(n, val+1.5, f'{val}', ha='center', fontsize=8, color='blue')
    # Show the slope = d
    ax1.annotate('', xy=(2, 5), xytext=(1, 3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax1.text(1.5, 4.5, 'd=2', fontsize=12, color='red', fontweight='bold')
    ax1.plot([1, 10], [a1, a1 + 9*d], 'r--', lw=1.5, alpha=0.5, label=f'y = {a1} + {d}(n-1)')
    ax1.set_title(f'Arithmetic: $a_1={a1}$, $d={d}$\n$a_n = a_1 + (n-1)d$', fontweight='bold')
    ax1.set_xlabel('n (term number)'); ax1.set_ylabel('a_n (term value)')
    ax1.set_xticks(n_vals); ax1.set_xlim(0.5, 10.5); ax1.set_ylim(0, 25)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=9)

    # Right: Sum visualization (bar chart)
    ax2.bar(n_vals, a_n, alpha=0.5, color='blue', label='terms')
    # Pairing first+last visualization
    ax2.fill_between([0.5, 10.5], [a1, a_n[-1]], [a_n[-1], a1],
                     alpha=0.12, color='red', label='first+last pairs')
    ax2.set_title(f'Sum $S_n = \\frac{{n(a_1+a_n)}}{{2}}$\n$S_{{10}} = \\frac{{10({a1}+{a_n[-1]})}}{{2}} = {10*(a1+a_n[-1])//2}$',
                  fontweight='bold')
    ax2.set_xlabel('n'); ax2.set_ylabel('a_n')
    ax2.set_xticks(n_vals); ax2.set_xlim(0.5, 10.5)
    ax2.grid(True, alpha=0.3); ax2.legend(fontsize=9)

    fig.suptitle('Arithmetic Sequences — Linear Growth', fontsize=14, fontweight='bold')
    save('12b1a-arithmetic-line.png')


# ============================================================
# 12b1b-geometric-curve.png
# ============================================================
def fig_geometric_curve():
    """Geometric sequence as exponential growth/decay."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    n_vals = np.arange(1, 11)

    # Left: Growth (r > 1)
    a1, r = 2, 1.5
    a_n = a1 * r ** (n_vals - 1)
    ax1.plot(n_vals, a_n, 'ro-', lw=2, markersize=8)
    ax1.fill_between(n_vals, 0, a_n, alpha=0.1, color='red')
    ax1.set_title(f'Geometric Growth: $a_1={a1}$, $r={r}$\n$a_n = a_1 \\cdot r^{{{{n-1}}}}$',
                  fontweight='bold')
    ax1.set_xlabel('n'); ax1.set_ylabel('a_n')
    ax1.set_xticks(n_vals); ax1.set_xlim(0.5, 10.5)
    ax1.grid(True, alpha=0.3)
    # Annotate first few terms
    for i in range(4):
        ax1.annotate(f'{a_n[i]:.1f}', (n_vals[i], a_n[i]),
                    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    # Right: Decay (0 < r < 1)
    a1, r = 8, 0.6
    a_n = a1 * r ** (n_vals - 1)
    ax2.plot(n_vals, a_n, 'go-', lw=2, markersize=8)
    ax2.fill_between(n_vals, 0, a_n, alpha=0.1, color='green')
    # Show infinite sum convergence
    S_inf = a1 / (1 - r)
    ax2.axhline(y=S_inf, color='orange', linestyle='--', lw=2, label=f'$S_\\infty$ = {S_inf:.1f}')
    ax2.set_title(f'Geometric Decay: $a_1={a1}$, $r={r}$\n$S_\\infty = \\frac{{{a1}}}{{1-{r}}} = {S_inf:.1f}$',
                  fontweight='bold')
    ax2.set_xlabel('n'); ax2.set_ylabel('a_n')
    ax2.set_xticks(n_vals); ax2.set_xlim(0.5, 10.5)
    ax2.grid(True, alpha=0.3); ax2.legend(fontsize=9)
    for i in range(3):
        ax2.annotate(f'{a_n[i]:.2f}', (n_vals[i], a_n[i]),
                    textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    fig.suptitle('Geometric Sequences — Exponential Growth and Decay',
                 fontsize=14, fontweight='bold')
    save('12b1b-geometric-curve.png')


# ============================================================
# 12b1c-infinite-series-visual.png
# ============================================================
def fig_infinite_series_visual():
    """Visual proof that 1/2 + 1/4 + 1/8 + ... = 1 using a unit square."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    steps = [1, 3, 6]

    for idx, n_steps in enumerate(steps):
        ax = axes[idx]
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.set_aspect('equal')

        x, y = 0, 0
        size = 1
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

        ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=False, color='black', lw=1.5))

        total = 0
        for i in range(n_steps):
            val = size / 2
            if i % 2 == 0:  # Right half
                ax.add_patch(plt.Rectangle((x, y), val, size, alpha=0.6,
                                          color=colors[i % len(colors)]))
                ax.text(x + val/2, y + size/2, f'{val:.0f}/{size*2:.0f}',
                       ha='center', va='center', fontsize=8, fontweight='bold')
                x += val
            else:  # Top half
                ax.add_patch(plt.Rectangle((x - val, y + size - val), val, val, alpha=0.6,
                                          color=colors[i % len(colors)]))
                ax.text(x - val/2, y + size - val/2, f'{val:.0f}/{size*2:.0f}',
                       ha='center', va='center', fontsize=8, fontweight='bold')
                size = val
            total += val

        remaining = 1 - total
        # Show remaining area
        if remaining > 0.01 and n_steps > 1:
            ax.add_patch(plt.Rectangle((x - size, y), size, remaining, alpha=0.2,
                                      color='gray', hatch='//'))
            ax.text(x - size/2, y + remaining/2, f'remain\n{remaining:.4f}',
                   ha='center', va='center', fontsize=7, color='gray')

        ax.set_title(f'{n_steps} terms: sum = {total:.4f}\n$\\frac{{1}}{{2}} + \\frac{{1}}{{4}} + \\cdots$',
                    fontweight='bold', fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    fig.suptitle('Visual Proof: $\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\cdots = 1$',
                 fontsize=14, fontweight='bold')
    save('12b1c-infinite-series-visual.png')


# ============================================================
# 12b1d-arith-vs-geo.png
# ============================================================
def fig_arith_vs_geo():
    """Side-by-side comparison of arithmetic vs geometric growth."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    n = np.arange(1, 11)
    arith = 2 * n  # a_n = 2n
    geo = 2 ** (n - 1)  # a_n = 2^{n-1}

    # Linear scale
    ax1.plot(n, arith, 'b-o', lw=2.5, markersize=8, label='arithmetic: $a_n=2n$')
    ax1.plot(n, geo, 'r-s', lw=2.5, markersize=8, label='geometric: $a_n=2^{n-1}$')
    ax1.set_title('Linear Scale', fontweight='bold')
    ax1.set_xlabel('n'); ax1.set_ylabel('a_n')
    ax1.set_xticks(n); ax1.set_xlim(0.5, 10.5)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=9)

    # Log scale (shows geometric as straight line)
    ax2.plot(n, arith, 'b-o', lw=2.5, markersize=8, label='arithmetic: $a_n=2n$')
    ax2.plot(n, geo, 'r-s', lw=2.5, markersize=8, label='geometric: $a_n=2^{n-1}$')
    ax2.set_yscale('log')
    ax2.set_title('Log Scale (geometric → straight line)', fontweight='bold')
    ax2.set_xlabel('n'); ax2.set_ylabel('a_n (log scale)')
    ax2.set_xticks(n); ax2.set_xlim(0.5, 10.5)
    ax2.grid(True, alpha=0.3); ax2.legend(fontsize=9)

    fig.suptitle('Arithmetic vs Geometric Growth — The Explosive Difference',
                 fontsize=14, fontweight='bold')
    save('12b1d-arith-vs-geo.png')


# ============================================================
# 12b1e-sigma-visual.png
# ============================================================
def fig_sigma_visual():
    """Visualizing sigma notation as stacked rectangles."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    n = 8

    # (1) Sum of integers
    ax = axes[0]
    k = np.arange(1, n+1)
    ax.bar(k, k, alpha=0.5, color='steelblue')
    ax.fill_between([0.5, n+0.5], [n, 1], [1, n], alpha=0.12, color='red')
    total = n*(n+1)//2
    ax.set_title(f'$\\sum_{{k=1}}^{{{n}}} k = \\frac{{{n}\\cdot{n+1}}}{{2}} = {total}$',
                 fontweight='bold')
    ax.set_xlabel('k'); ax.set_ylabel('k')
    ax.set_xticks(k); ax.set_xlim(0.5, n+0.5)
    ax.grid(True, alpha=0.3)

    # (2) Sum of squares
    ax = axes[1]
    ax.bar(k, k**2, alpha=0.5, color='coral')
    total_sq = n*(n+1)*(2*n+1)//6
    ax.set_title(f'$\\sum_{{k=1}}^{{{n}}} k^2 = \\frac{{{n}\\cdot{n+1}\\cdot{2*n+1}}}{{6}} = {total_sq}$',
                 fontweight='bold')
    ax.set_xlabel('k'); ax.set_ylabel('k²')
    ax.set_xticks(k); ax.set_xlim(0.5, n+0.5)
    ax.grid(True, alpha=0.3)

    # (3) Sum of cubes = (sum of integers)^2
    ax = axes[2]
    ax.bar(k, k**3, alpha=0.5, color='green')
    total_cu = (n*(n+1)//2)**2
    ax.set_title(f'$\\sum_{{k=1}}^{{{n}}} k^3 = (\\sum k)^2 = {total_cu}$',
                 fontweight='bold')
    ax.set_xlabel('k'); ax.set_ylabel('k³')
    ax.set_xticks(k); ax.set_xlim(0.5, n+0.5)
    ax.grid(True, alpha=0.3)

    fig.suptitle('Sigma Notation — Sums as Areas', fontsize=14, fontweight='bold')
    save('12b1e-sigma-visual.png')


# ============================================================
# 12b1f-partial-sums.png
# ============================================================
def fig_partial_sums():
    """Partial sums approaching the infinite sum — convergence visualization."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    n_vals = np.arange(1, 13)
    a1, r = 8, 0.5

    # Terms
    terms = a1 * r ** (n_vals - 1)
    # Partial sums
    S_n = np.cumsum(terms)
    S_inf = a1 / (1 - r)

    # Left: Individual terms (bars) and partial sums (line)
    ax1.bar(n_vals, terms, alpha=0.4, color='blue', label=f'terms $a_n = {a1}\\cdot{r}^{{{{n-1}}}}$')
    ax1.plot(n_vals, S_n, 'ro-', lw=2.5, markersize=8, label=f'partial sums $S_n$')
    ax1.axhline(y=S_inf, color='orange', linestyle='--', lw=2.5,
                label=f'$S_\\infty = {S_inf}$')
    # Annotate convergence
    for i in [0, 1, 2, 5, 11]:
        ax1.annotate(f'{S_n[i]:.2f}', (n_vals[i], S_n[i]),
                    textcoords="offset points", xytext=(0, -15),
                    ha='center', fontsize=7, color='red')
    ax1.set_title(f'Terms (bars) and Partial Sums (red line)\nConverging to $S_\\infty = {S_inf}$',
                  fontweight='bold')
    ax1.set_xlabel('n'); ax1.set_ylabel('value')
    ax1.set_xticks(n_vals); ax1.set_xlim(0.5, 12.5); ax1.set_ylim(0, S_inf + 1)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=8)

    # Right: Gap between S_n and S_inf (decay of error)
    gap = S_inf - S_n
    ax2.plot(n_vals, gap, 'g-o', lw=2.5, markersize=8)
    ax2.fill_between(n_vals, 0, gap, alpha=0.15, color='green')
    ax2.set_yscale('log')
    ax2.set_title(f'Gap $S_\\infty - S_n$ (log scale)\nExponential decay → linear on log plot',
                  fontweight='bold')
    ax2.set_xlabel('n'); ax2.set_ylabel('$S_\\infty - S_n$ (log)')
    ax2.set_xticks(n_vals); ax2.set_xlim(0.5, 12.5)
    ax2.grid(True, alpha=0.3)

    fig.suptitle('Convergence of Partial Sums — How $S_n$ Approaches $S_\\infty$',
                 fontsize=14, fontweight='bold')
    save('12b1f-partial-sums.png')


# ============================================================
# 12b1g-compound-interest.png
# ============================================================
def fig_compound_interest():
    """Real-world application: compound interest as geometric sequence."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # $1000 at 5% annual interest, compounded annually for 30 years
    P, r_rate = 1000, 0.05
    years = np.arange(0, 31)
    amount = P * (1 + r_rate) ** years

    # Left: Growth curve
    ax1.plot(years, amount, 'g-', lw=2.5)
    ax1.fill_between(years, P, amount, alpha=0.1, color='green')
    ax1.axhline(y=P, color='gray', linestyle='--', lw=1, alpha=0.5)
    # Mark key years
    for y in [0, 5, 10, 20, 30]:
        ax1.plot(y, P * (1+r_rate)**y, 'ro', markersize=6)
        ax1.text(y, P*(1+r_rate)**y + 200, f'${P*(1+r_rate)**y:.0f}',
                ha='center', fontsize=8)
    ax1.set_title(f'Compound Interest: ${P} at {r_rate*100:.0f}% APR\n'
                  f'$A_n = P(1+r)^{{n}}$ → Geometric!',
                  fontweight='bold')
    ax1.set_xlabel('Years (n)'); ax1.set_ylabel('Amount ($)')
    ax1.set_xlim(-0.5, 31); ax1.grid(True, alpha=0.3)

    # Right: Log scale shows it's geometric (straight line)
    ax2.plot(years, amount, 'g-', lw=2.5)
    ax2.set_yscale('log')
    ax2.set_title('Log Scale: Straight Line → Geometric Growth\n'
                  'Confirming $A_n = P \\cdot (1+r)^{{n-1}}$',
                  fontweight='bold')
    ax2.set_xlabel('Years (n)'); ax2.set_ylabel('Amount ($, log scale)')
    ax2.set_xlim(-0.5, 31); ax2.grid(True, alpha=0.3)

    fig.suptitle('Real-World Geometric Sequence: Compound Interest',
                 fontsize=14, fontweight='bold')
    save('12b1g-compound-interest.png')


# ============================================================
if __name__ == "__main__":
    print("Generating 12B1 graphs...")
    fig_arithmetic_line()
    fig_geometric_curve()
    fig_infinite_series_visual()
    fig_arith_vs_geo()
    fig_sigma_visual()
    fig_partial_sums()
    fig_compound_interest()
    print("Done! ✓")
