#!/usr/bin/env python3
"""Generate all graph images for Session 12B2: Sequences and Series — Advanced Techniques."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/12B2"
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
# 12b2a-telescoping.png
# ============================================================
def fig_telescoping():
    """Visualization of telescoping cancellation — terms cancel in the middle."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    n = 8

    # Left: Partial fraction decomposition bars
    k_vals = np.arange(1, n+1)
    fracs = 1/(k_vals*(k_vals+1))
    decomposed = 1/k_vals - 1/(k_vals+1)

    ax1.bar(k_vals, 1/k_vals, alpha=0.3, color='blue', label='$1/k$ (positive)')
    ax1.bar(k_vals+0.3, 1/(k_vals+1), alpha=0.3, color='red', label='$1/(k+1)$ (negative)')
    ax1.set_title(f'Telescoping: $\\frac{{1}}{{k(k+1)}} = \\frac{{1}}{{k}} - \\frac{{1}}{{k+1}}$\n'
                  f'Positive (blue) and negative (red) parts',
                  fontweight='bold')
    ax1.set_xlabel('k'); ax1.set_ylabel('value')
    ax1.set_xticks(k_vals); ax1.set_xlim(0.5, n+0.5)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=8)

    # Right: Show cancellation — partial sums
    S_n = np.cumsum(fracs)
    # Theoretical: 1 - 1/(n+1)
    S_theory = 1 - 1/(k_vals+1)

    ax2.plot(k_vals, S_n, 'bo-', lw=2.5, markersize=8, label='$S_n$ (actual sum)')
    ax2.plot(k_vals, S_theory, 'r--', lw=2, label='$1 - \\frac{1}{n+1}$ (theory)')
    # Show the gap shrinking
    ax2.fill_between(k_vals, S_n, S_theory, alpha=0.1, color='green')

    for i in [0, 1, 2, 5, 7]:
        ax2.annotate(f'{S_n[i]:.4f}', (k_vals[i], S_n[i]),
                    textcoords="offset points", xytext=(0, -12),
                    ha='center', fontsize=7, color='blue')

    ax2.set_title(f'Telescoping Sum: $\\sum_{{k=1}}^{{n}} \\frac{{1}}{{k(k+1)}} = 1 - \\frac{{1}}{{n+1}}$\n'
                  f'Only first and last terms survive',
                  fontweight='bold')
    ax2.set_xlabel('n'); ax2.set_ylabel('$S_n$')
    ax2.set_xticks(k_vals); ax2.set_xlim(0.5, n+0.5)
    ax2.grid(True, alpha=0.3); ax2.legend(fontsize=9)
    ax2.set_ylim(0, 1)

    fig.suptitle('Telescoping Series — Middle Terms Cancel Out',
                 fontsize=14, fontweight='bold')
    save('12b2a-telescoping.png')


# ============================================================
# 12b2b-fibonacci-spiral.png
# ============================================================
def fig_fibonacci_spiral():
    """Connected Fibonacci spiral — each arc joins the next seamlessly."""
    from matplotlib.patches import Arc, Rectangle
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(14, 6.5))

    colors = ['#FF6B6B', '#FFE66D', '#4ECDC4', '#45B7D1', '#96CEB4',
              '#DDA0DD', '#F0B27A', '#82E0AA', '#85C1E9']

    # Build connected spiral arcs recursively
    fib = [1, 1, 2, 3, 5, 8, 13, 21]
    # Each arc: (cx, cy, r, start_deg, end_deg)
    # Arc 1: start at (1,0), center (0,0), r=1, 0°→90°
    arcs = [(0, 0, fib[0], 0, 90)]

    for i in range(1, len(fib)):
        prev_cx, prev_cy, prev_r, prev_a1, prev_a2 = arcs[-1]
        r = fib[i]
        # The spiral continues CCW: each arc starts where previous ended.
        # The center of the new arc is offset from the previous center
        # by (prev_r) in the direction the spiral has grown.
        # Pattern: centers cycle through quadrant shifts
        if i % 4 == 1:  # same center as prev (shifts to next quadrant)
            cx, cy = prev_cx, prev_cy
            a1, a2 = 90, 180
        elif i % 4 == 2:
            cx, cy = prev_cx + prev_r, prev_cy
            a1, a2 = 180, 270
        elif i % 4 == 3:
            cx, cy = prev_cx + prev_r, prev_cy + prev_r
            a1, a2 = 270, 360
        else:  # i % 4 == 0
            cx, cy = prev_cx - r, prev_cy + prev_r
            a1, a2 = 0, 90
        arcs.append((cx, cy, r, a1, a2))

    # Alternative: use pre-verified connected arc data
    arcs = [
        (0, 0, 1, 0, 90),       # F1: (1,0)→(0,1), sq(0,0,1)
        (0, 0, 1, 90, 180),     # F2: (0,1)→(-1,0), sq(-1,0,1)
        (1, 0, 2, 180, 270),    # F3: (-1,0)→(1,-2), sq(-1,-2,2)
        (1, 1, 3, 270, 360),    # F4: (1,-2)→(4,1), sq(1,-2,3)
        (-1, 1, 5, 0, 90),      # F5: (4,1)→(-1,6), sq(-1,1,5)
        (-1, -2, 8, 90, 180),   # F6: (-1,6)→(-9,-2), sq(-9,-2,8)
        (4, -2, 13, 180, 270),  # F7: (-9,-2)→(4,-15), sq(-9,-15,13)
        (4, 6, 21, 270, 360),   # F8: (4,-15)→(25,6), sq(4,-15,21)
    ]

    # Compute squares from arcs
    def arc_to_square(cx, cy, r, a1, a2):
        if a1 == 0:      bx, by = cx, cy
        elif a1 == 90:   bx, by = cx - r, cy
        elif a1 == 180:  bx, by = cx - r, cy - r
        else:            bx, by = cx, cy - r
        return (bx, by, r)

    squares = [arc_to_square(*a) for a in arcs]

    axL.set_aspect('equal')
    # Draw squares
    for idx, (bx, by, s) in enumerate(squares):
        rect = Rectangle((bx, by), s, s, alpha=0.35,
                        facecolor=colors[idx % len(colors)], edgecolor='#555', lw=0.8)
        axL.add_patch(rect)
        fs = max(6, min(9, 11 - idx))
        axL.text(bx + s/2, by + s/2, str(s), ha='center', va='center',
                fontsize=fs, fontweight='bold')

    # Draw connected spiral arcs
    for cx, cy, r, a1, a2 in arcs:
        arc = Arc((cx, cy), 2*r, 2*r, angle=0, theta1=a1, theta2=a2,
                  color='purple', lw=2.5, zorder=5)
        axL.add_patch(arc)

    # Tight crop
    xs = [b[0] for b in squares] + [b[0]+b[2] for b in squares]
    ys = [b[1] for b in squares] + [b[1]+b[2] for b in squares]
    margin = 3
    axL.set_xlim(min(xs) - margin, max(xs) + margin)
    axL.set_ylim(min(ys) - margin, max(ys) + margin)
    axL.set_title('Fibonacci Spiral — connected arcs', fontweight='bold', fontsize=13)
    axL.set_xticks([]); axL.set_yticks([])
    axL.spines['top'].set_visible(False)
    axL.spines['right'].set_visible(False)

    # Right: Ratio convergence
    fib_full = [1, 1]
    for _ in range(16):
        fib_full.append(fib_full[-1] + fib_full[-2])
    nv = np.arange(1, len(fib_full))
    ratios = np.array([fib_full[i+1]/fib_full[i] for i in range(len(fib_full)-1)])
    phi = (1 + np.sqrt(5)) / 2

    axR.plot(nv[1:11], ratios[1:11], 'bo-', lw=2, markersize=6, label='$F_{n+1}/F_n$')
    axR.axhline(y=phi, color='orange', linestyle='--', lw=2,
                label=f'$\\phi \\approx {phi:.6f}$')
    for i in [2, 5, 8]:
        axR.annotate(f'{ratios[i]:.4f}', (nv[i], ratios[i]),
                    textcoords="offset points", xytext=(0, 12),
                    ha='center', fontsize=8, color='blue')
    axR.set_title('Ratio $F_{n+1}/F_n \\to \\phi$', fontweight='bold', fontsize=13)
    axR.set_xlabel('n'); axR.set_ylabel('$F_{n+1} / F_n$')
    axR.set_xlim(0.5, 11.5); axR.grid(True, alpha=0.3); axR.legend(fontsize=9)

    fig.suptitle('Fibonacci Numbers and the Golden Ratio',
                 fontsize=15, fontweight='bold', y=0.98)
    save('12b2b-fibonacci-spiral.png')


# ============================================================
# 12b2c-recurrence-fixed-point.png
# ============================================================
def fig_recurrence_fixed_point():
    """Cobweb diagram / fixed point visualization for recurrence a_{n+1}=pa_n+q."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # (1) Cobweb diagram for a_{n+1} = 0.5*a_n + 2, a_1 = 1
    ax = axes[0]
    x = np.linspace(0, 5, 100)
    p, q = 0.5, 2
    f = lambda x: p*x + q
    fixed = q / (1 - p)  # = 4

    ax.plot(x, f(x), 'b-', lw=2.5, label=f'$a_{{n+1}} = {p}a_n + {q}$')
    ax.plot(x, x, color='gray', linestyle='--', lw=1.5, label='$a_{n+1} = a_n$ (identity)')
    ax.plot(fixed, fixed, 'ro', markersize=12, zorder=5)
    ax.annotate(f'Fixed point = {fixed}', (fixed+0.1, fixed+0.1),
               fontsize=11, color='red', fontweight='bold')

    # Cobweb steps
    a = 1
    steps_x, steps_y = [], []
    for _ in range(8):
        steps_x.append(a); steps_y.append(a)
        a_new = f(a)
        steps_x.append(a); steps_y.append(a_new)
        a = a_new
    ax.plot(steps_x, steps_y, 'g-', lw=1.5, alpha=0.7, label='cobweb path')

    ax.set_title('Cobweb Diagram: $a_{n+1} = 0.5a_n + 2$\nFixed point attraction',
                 fontweight='bold')
    ax.set_xlabel('$a_n$'); ax.set_ylabel('$a_{n+1}$')
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    # (2) Second-order: Fibonacci — characteristic equation
    ax = axes[1]
    ax.axis('off')
    info = (
        "Second-Order Recurrence: $a_{n+2} = pa_{n+1} + qa_n$\n\n"
        "Step 1: Characteristic Equation\n"
        "$r^2 = pr + q$\n\n"
        "Step 2: Solve for roots $r_1, r_2$\n\n"
        "Step 3: General solution\n"
        "$a_n = A\\cdot r_1^{n-1} + B\\cdot r_2^{n-1}$\n\n"
        "Step 4: Use $a_1, a_2$ to find $A, B$\n\n"
        "---\n\n"
        "Example — Fibonacci:\n"
        "$F_{n+2} = F_{n+1} + F_n$\n"
        "$r^2 = r + 1$\n"
        "$r = \\frac{1 \\pm \\sqrt{5}}{2}$\n\n"
        "Binet's Formula:\n"
        "$F_n = \\frac{\\phi^n - \\psi^n}{\\sqrt{5}}$\n"
        "$\\phi = \\frac{1+\\sqrt{5}}{2}$ (golden ratio)\n"
        "$\\psi = \\frac{1-\\sqrt{5}}{2}$"
    )
    ax.text(0.1, 0.5, info, transform=ax.transAxes, fontsize=10,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    fig.suptitle('Recurrence Relations — Fixed Points and Characteristic Equations',
                 fontsize=14, fontweight='bold')
    save('12b2c-recurrence-fixed-point.png')


# ============================================================
# 12b2d-induction-domino.png
# ============================================================
def fig_induction_domino():
    """Domino / mathematical induction visualization."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # (1) Domino chain — base case
    ax = axes[0, 0]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-0.5, 3.5)
    
    from matplotlib.transforms import Affine2D
    for i in range(8):
        x = i * 1.0
        if i == 0:
            # Fallen domino (rotated)
            rect = plt.Rectangle((x, 0), 0.6, 1.0, alpha=0.8, color='#4ECDC4')
            t = Affine2D().rotate_deg_around(x, 0, -60) + ax.transData
            rect.set_transform(t)
            ax.add_patch(rect)
        else:
            rect = plt.Rectangle((x, 0), 0.6, 1.0, alpha=0.7, color='gray', lw=1)
            ax.add_patch(rect)
            ax.text(x+0.3, 0.5, str(i+1), ha='center', va='center', fontsize=8)
    # Push arrow
    ax.annotate('Push!', xy=(0.3, 1.2), xytext=(-1.0, 2.5),
               arrowprops=dict(arrowstyle='->', color='red', lw=2.5),
               fontsize=14, color='red', fontweight='bold')
    ax.set_title('Base Case: $P(1)$ is true\n(The first domino falls)', fontweight='bold')
    ax.axis('off')

    # (2) Inductive step: if k falls, k+1 falls
    ax = axes[0, 1]
    ax.set_xlim(-1, 10)
    ax.set_ylim(-0.5, 3.5)
    
    for i in range(8):
        x = i * 1.0
        if i <= 3:
            # Fallen dominoes
            rect = plt.Rectangle((x, 0), 0.6, 1.0, alpha=0.8, color='#FF6B6B')
            t = Affine2D().rotate_deg_around(x, 0, -50 + i*5) + ax.transData
            rect.set_transform(t)
            ax.add_patch(rect)
        elif i == 4:
            # Falling (just starting to tip)
            rect = plt.Rectangle((x, 0), 0.6, 1.0, alpha=0.8, color='#FFE66D')
            t = Affine2D().rotate_deg_around(x, 0, -15) + ax.transData
            rect.set_transform(t)
            ax.add_patch(rect)
        else:
            # Still standing
            rect = plt.Rectangle((x, 0), 0.6, 1.0, alpha=0.7, color='gray', lw=1)
            ax.add_patch(rect)
            ax.text(x+0.3, 0.5, str(i+1), ha='center', va='center', fontsize=8)
    # Annotations
    ax.annotate('If $k$ falls...', xy=(3*1.0+0.3, 1.5), xytext=(2.0, 2.5),
               arrowprops=dict(arrowstyle='->', color='red', lw=2),
               fontsize=13, color='red', fontweight='bold')
    ax.annotate('...$k+1$ falls', xy=(4*1.0+0.3, 1.5), xytext=(5.5, 2.5),
               arrowprops=dict(arrowstyle='->', color='green', lw=2),
               fontsize=13, color='green', fontweight='bold')
    ax.set_title('Inductive Step: $P(k) \\Rightarrow P(k+1)$\n(If $k$ falls, $k+1$ falls)',
                 fontweight='bold')
    ax.axis('off')

    # (3) The logic flow
    ax = axes[1, 0]
    ax.axis('off')
    logic = (
        "Mathematical Induction — Two Steps:\n\n"
        "1. Base Case: Verify $P(1)$ is true.\n"
        "   (The first domino falls.)\n\n"
        "2. Inductive Step: Assume $P(k)$ true.\n"
        "   Prove $P(k+1)$ is true.\n"
        "   (If domino $k$ falls, $k+1$ falls.)\n\n"
        "$\\therefore$ $P(n)$ is true for ALL $n \\in \\mathbb{N}$.\n"
        "(All dominoes fall.)"
    )
    ax.text(0.1, 0.5, logic, transform=ax.transAxes, fontsize=12,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))
    ax.set_title('The Induction Principle', fontweight='bold', fontsize=12)

    # (4) Example: Sum of first n integers
    ax = axes[1, 1]
    ax.axis('off')
    example = (
        "Prove: $1+2+\\cdots+n = \\frac{n(n+1)}{2}$\n\n"
        "Base ($n=1$): $1 = \\frac{1\\cdot2}{2} = 1$  $\\checkmark$\n\n"
        "Assume for $k$: $1+\\cdots+k = \\frac{k(k+1)}{2}$\n\n"
        "For $k+1$:\n"
        "$1+\\cdots+k+(k+1)$\n"
        "$= \\frac{k(k+1)}{2} + (k+1)$\n"
        "$= \\frac{(k+1)(k+2)}{2}$\n\n"
        "Matches formula with $n=k+1$. $\\checkmark$\n\n"
        "$\\therefore$ True for ALL $n \\in \\mathbb{N}$."
    )
    ax.text(0.1, 0.5, example, transform=ax.transAxes, fontsize=11,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#e8f5e8', alpha=0.8))
    ax.set_title('Worked Example', fontweight='bold', fontsize=12)

    fig.suptitle('Mathematical Induction — The Domino Principle',
                 fontsize=14, fontweight='bold', y=1.01)
    save('12b2d-induction-domino.png')


# ============================================================
# 12b2e-sequence-convergence.png
# ============================================================
def fig_sequence_convergence():
    """Sequence convergence visualization — limit behavior."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    n = np.arange(1, 31)

    # (1) Convergent: a_n = n/(n+1) → 1
    ax = axes[0, 0]
    a_n = n / (n+1)
    ax.plot(n, a_n, 'b-o', lw=2, markersize=4)
    ax.axhline(y=1, color='orange', linestyle='--', lw=2, label='limit = 1')
    ax.fill_between(n, a_n, 1, alpha=0.1, color='green')
    # Epsilon band
    ax.fill_between([0, 31], 0.95, 1.05, alpha=0.08, color='red')
    ax.text(20, 0.97, '$\\varepsilon$ band', fontsize=9, color='red')
    N_eps = 19  # where a_n > 0.95
    ax.plot(N_eps, a_n[N_eps-1], 'ro', markersize=10)
    ax.annotate(f'N({N_eps})', (N_eps, a_n[N_eps-1]), textcoords="offset points",
               xytext=(10, -15), fontsize=9, color='red', fontweight='bold')
    ax.set_title('$a_n = \\frac{n}{n+1} \\to 1$\nFinds $N$ for $\\varepsilon$',
                 fontweight='bold')
    ax.set_xlabel('n'); ax.set_ylabel('$a_n$')
    ax.set_xlim(0, 31); ax.set_ylim(0.4, 1.05)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=9)

    # (2) Divergent: a_n = n^2
    ax = axes[0, 1]
    a_n = n**2
    ax.plot(n, a_n, 'r-o', lw=2, markersize=4)
    ax.set_title('$a_n = n^2 \\to \\infty$ (Divergent)\nGrows without bound',
                 fontweight='bold')
    ax.set_xlabel('n'); ax.set_ylabel('$a_n$')
    ax.set_xlim(0, 31)
    ax.grid(True, alpha=0.3)

    # (3) Oscillating convergent: a_n = (-1)^n / n → 0
    ax = axes[1, 0]
    a_n = (-1)**n / n
    ax.plot(n, a_n, 'g-o', lw=2, markersize=4)
    ax.axhline(y=0, color='orange', linestyle='--', lw=2, label='limit = 0')
    ax.fill_between(n, -1/n, 1/n, alpha=0.08, color='gray', label='$\\pm 1/n$ envelope')
    ax.set_title('$a_n = \\frac{(-1)^n}{n} \\to 0$\nOscillating convergence',
                 fontweight='bold')
    ax.set_xlabel('n'); ax.set_ylabel('$a_n$')
    ax.set_xlim(0, 31); ax.set_ylim(-0.5, 0.5)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=9)

    # (4) Key limit facts chart
    ax = axes[1, 1]
    ax.axis('off')
    facts = (
        "Key Limit Facts:\n\n"
        "$\\lim_{n\\to\\infty} \\frac{1}{n^p} = 0$ for $p > 0$\n\n"
        "$\\lim_{n\\to\\infty} r^n = 0$ for $|r| < 1$\n\n"
        "$\\lim_{n\\to\\infty} \\left(1+\\frac{1}{n}\\right)^n = e$\n\n"
        "$\\lim_{n\\to\\infty} \\frac{\\ln n}{n} = 0$\n\n"
        "$\\lim_{n\\to\\infty} \\sqrt[n]{n} = 1$\n\n"
        "Squeeze Theorem:\nIf $b_n \\leq a_n \\leq c_n$ and\n$b_n, c_n \\to L$, then $a_n \\to L$"
    )
    ax.text(0.1, 0.5, facts, transform=ax.transAxes, fontsize=12,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    fig.suptitle('Sequence Convergence and Divergence',
                 fontsize=14, fontweight='bold')
    save('12b2e-sequence-convergence.png')


# ============================================================
# 12b2f-grouped-sequences.png
# ============================================================
def fig_grouped_sequences():
    """Visualization of grouped sequences — blocks of numbers."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Visual representation of groups
    ax1.axis('off')
    groups = [
        [1, 2],
        [3, 4, 5],
        [6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20],
    ]
    y_pos = 4
    for g_idx, group in enumerate(groups):
        x_start = 0
        group_label = f'Group {g_idx+1}'
        ax1.text(-5, y_pos, group_label, fontsize=10, fontweight='bold', va='center', ha='right')
        for num in group:
            ax1.add_patch(plt.Rectangle((x_start, y_pos-0.35), 0.9, 0.7,
                                       alpha=0.4, color='#4ECDC4', lw=1))
            ax1.text(x_start+0.45, y_pos, str(num), ha='center', va='center', fontsize=9)
            x_start += 1
        y_pos -= 1

    ax1.set_title('Grouped Sequences Structure\nGroup $n$ contains $n$ consecutive integers',
                  fontweight='bold')
    ax1.set_xlim(-6, 10); ax1.set_ylim(-0.5, 5.5)

    # Right: Formula derivation
    ax2.axis('off')
    formulas = (
        "Finding Group Elements:\n\n"
        "Numbers before group $n$:\n"
        "$1+2+\\cdots+(n-1) = \\frac{(n-1)n}{2}$\n\n"
        "First number in group $n$:\n"
        "$1 + \\frac{(n-1)n}{2}$\n\n"
        "Last number in group $n$:\n"
        "$\\frac{n(n+1)}{2}$\n\n"
        "---\n\n"
        "Example — Group 10:\n"
        "First = $1 + \\frac{9\\cdot10}{2} = 46$\n"
        "Last = $\\frac{10\\cdot11}{2} = 55$\n"
        "Group 10: 46, 47, ..., 55\n\n"
        "Reverse lookup — Number 100 is in:\n"
        "$\\frac{n(n+1)}{2} \\geq 100$\n"
        "$n=14$: Group 14 (92 to 105)"
    )
    ax2.text(0.1, 0.5, formulas, transform=ax2.transAxes, fontsize=11,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    fig.suptitle('Grouped Sequences — Counting by Blocks',
                 fontsize=14, fontweight='bold')
    save('12b2f-grouped-sequences.png')


# ============================================================
# 12b2g-harmonic-series.png
# ============================================================
def fig_harmonic_series():
    """Harmonic series divergence intuition — stacking blocks."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Harmonic series blocks showing 1/n heights
    n_vals = np.arange(1, 21)
    heights = 1/n_vals
    ax1.bar(n_vals, heights, alpha=0.5, color='steelblue')
    # Partial sums of harmonic
    S_n = np.cumsum(heights)
    ax1.plot(n_vals, S_n, 'ro-', lw=2, markersize=6, label='partial sum $H_n$')
    # Show it grows slowly
    ax1.text(15, S_n[14]+0.2, f'$H_{{20}} \\approx {S_n[19]:.2f}$', fontsize=10,
            fontweight='bold', color='red')
    # Comparison: integral of 1/x
    x = np.linspace(1, 20, 100)
    ax1.plot(x, np.log(x) + 1, 'g--', lw=2, alpha=0.7, label='$\\ln n + 1$ (approx)')
    ax1.set_title('Harmonic Series $H_n = \\sum_{{k=1}}^{{n}} \\frac{{1}}{{k}}$\n'
                  'Grows like $\\ln n$ — diverges VERY slowly',
                  fontweight='bold')
    ax1.set_xlabel('n'); ax1.set_ylabel('value')
    ax1.set_xticks(np.arange(0, 21, 5))
    ax1.set_xlim(0.5, 20.5)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=9)

    # Right: Comparison with geometric for convergence
    ax2.axis('off')
    comparison = (
        "Harmonic vs Geometric Comparison:\n\n"
        "Harmonic Series:\n"
        "$\\sum_{n=1}^{\\infty} \\frac{1}{n}$\n"
        "Terms: $1, \\frac{1}{2}, \\frac{1}{3}, \\frac{1}{4}, \\dots$\n"
        "→ DIVERGES (grows like $\\ln n$)\n\n"
        "Geometric Series ($|r|<1$):\n"
        "$\\sum_{n=0}^{\\infty} ar^n$\n"
        "Terms shrink exponentially\n"
        "→ CONVERGES to $\\frac{a}{1-r}$\n\n"
        "Key Difference:\n"
        "Harmonic: terms ~ $1/n$ (too slow to sum)\n"
        "Geometric: terms ~ $r^n$ (fast enough to sum)\n\n"
        "Intuition: $\\frac{1}{n}$ doesn't shrink fast enough.\n"
        "$\\sum \\frac{1}{n^p}$ converges only if $p > 1$."
    )
    ax2.text(0.1, 0.5, comparison, transform=ax2.transAxes, fontsize=11,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))

    fig.suptitle('Harmonic Series and Convergence Intuition',
                 fontsize=14, fontweight='bold')
    save('12b2g-harmonic-series.png')


# ============================================================
if __name__ == "__main__":
    print("Generating 12B2 graphs...")
    fig_telescoping()
    fig_fibonacci_spiral()
    fig_recurrence_fixed_point()
    fig_induction_domino()
    fig_sequence_convergence()
    fig_grouped_sequences()
    fig_harmonic_series()
    print("Done! ✓")
