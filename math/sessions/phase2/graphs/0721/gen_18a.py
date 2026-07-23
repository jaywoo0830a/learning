#!/usr/bin/env python3
"""Generate graphs for Session 18A: Series Convergence."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os, math

OUT = os.path.dirname(os.path.abspath(__file__)) + "/18A"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_geometric_series():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    n = np.arange(0, 11)
    # Left: convergent geometric (r=1/2)
    ax = axes[0]
    terms = (0.5)**n
    S = np.cumsum(terms)
    ax.bar(n, terms, alpha=0.3, color='blue', label='terms $a_n$')
    ax.plot(n, S, 'ro-', lw=2.5, markersize=7, label='partial sums $S_n$')
    ax.axhline(y=2, color='orange', linestyle='--', lw=2.5, label=r'$S_\infty = \frac{1}{1-0.5}=2$')
    ax.set_title(r'Convergent: $\sum (0.5)^n$' + '\n' + r'Terms shrink, sums approach $2$', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('value'); ax.set_xlim(-0.5,10.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: divergent geometric (r=1.2)
    ax = axes[1]
    terms2 = (1.2)**n
    S2 = np.cumsum(terms2)
    ax.bar(n[:6], terms2[:6], alpha=0.3, color='red', label='terms $a_n$')
    ax.plot(n[:8], S2[:8], 'ro-', lw=2.5, markersize=7, label='partial sums $S_n$')
    ax.set_title(r'Divergent: $\sum (1.2)^n$' + '\n' + r'Terms grow, sums $\infty$', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('value'); ax.set_xlim(-0.5,7.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Geometric Series — Convergence vs Divergence', fontsize=14, fontweight='bold')
    save('18a-geometric-series.png')

def fig_p_series():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    n = np.arange(1, 51)
    # Left: p=2 converges, p=1 diverges
    ax = axes[0]
    for p, c, lbl in [(2, 'blue', '$p=2$ (converges)'), (1, 'red', '$p=1$ (diverges)'), (0.5, 'green', '$p=1/2$ (diverges)')]:
        S = np.cumsum(1/n**p)
        ax.plot(n, S, '-', color=c, lw=2, label=lbl)
    ax.set_title(r'Partial Sums of $\sum 1/n^p$' + '\n' + r'$p>1$ converges, $p\leq 1$ diverges', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$S_n$'); ax.set_xlim(1,50); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: integral test visualization
    ax = axes[1]
    x = np.linspace(1, 10, 200)
    ax.plot(x, 1/x**2, 'b-', lw=2.5, label='$f(x)=1/x^2$')
    ax.fill_between(x, 0, 1/x**2, alpha=0.12, color='blue', label='area $= \\int_1^\\infty 1/x^2 dx = 1$')
    # Bars showing sum
    n_bars = np.arange(1, 11)
    ax.bar(n_bars, 1/n_bars**2, alpha=0.25, color='red', width=0.8, label=r'$\sum 1/n^2$ (bars)')
    ax.set_title(r'Integral Test: $\sum 1/n^2$ and $\int 1/x^2 dx$' + '\n' + r'Both converge together', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_xlim(0.5,10.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('$p$-Series and the Integral Test', fontsize=14, fontweight='bold')
    save('18a-p-series.png')

def fig_ratio_test():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    n = np.arange(1, 16)
    # Left: ratio test convergence — n!/n^n
    ax = axes[0]
    terms = np.array([math.factorial(i)/i**i for i in n])
    ratios = terms[1:] / terms[:-1]
    ax.plot(n[1:], ratios, 'bo-', lw=2.5, markersize=7, label=r'$a_{n+1}/a_n$')
    ax.axhline(y=1/np.e, color='orange', linestyle='--', lw=2, label=r'$\lim = 1/e < 1$ → converges')
    ax.axhline(y=1, color='red', linestyle=':', lw=1.5, alpha=0.7)
    ax.set_title(r'Ratio Test: $\sum n!/n^n$' + '\n' + r'$\lim a_{n+1}/a_n = 1/e < 1$', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$a_{n+1}/a_n$'); ax.set_xlim(0.5,15.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: ratio test divergence — n!/2^n
    ax = axes[1]
    terms2 = np.array([math.factorial(i)/2**i for i in n[:10]])
    ratios2 = terms2[1:] / terms2[:-1]
    ax.plot(n[1:10], ratios2, 'ro-', lw=2.5, markersize=7, label=r'$a_{n+1}/a_n$')
    ax.axhline(y=1, color='red', linestyle='--', lw=2.5, label=r'$\lim = \infty > 1$ → diverges')
    ax.set_title(r'Ratio Test: $\sum n!/2^n$' + '\n' + r'Ratio grows without bound', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$a_{n+1}/a_n$'); ax.set_xlim(0.5,10.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Ratio Test — How It Works', fontsize=14, fontweight='bold')
    save('18a-ratio-test.png')

def fig_alternating_series():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    n = np.arange(1, 21)
    # Left: alternating harmonic
    ax = axes[0]
    terms = (-1)**(n+1) / n
    S = np.cumsum(terms)
    ax.plot(n, terms, 'bo-', lw=1.5, markersize=5, alpha=0.5, label='terms $a_n$')
    ax.plot(n, S, 'r.-', lw=2.5, markersize=8, label='partial sums $S_n$')
    ax.axhline(y=np.log(2), color='orange', linestyle='--', lw=2.5, label=r'$S_\infty = \ln 2$')
    ax.fill_between(n, S, np.log(2), alpha=0.08, color='green')
    ax.set_title(r'Alternating Harmonic: $\sum (-1)^{n+1}/n$' + '\n' + r'Converges to $\ln 2$', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('value'); ax.set_xlim(0.5,20.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: absolute vs conditional
    ax = axes[1]
    n2 = np.arange(1, 31)
    abs_terms = np.cumsum(1/n2)
    ax.plot(n2, abs_terms, 'b-', lw=2.5, label=r'$\sum 1/n$ (diverges — harmonic)')
    alt_terms = np.cumsum((-1)**(n2+1)/n2)
    ax.plot(n2, alt_terms, 'r-', lw=2.5, label=r'$\sum (-1)^{n+1}/n$ (converges — conditional)')
    # Mark ln 2
    ax.axhline(y=np.log(2), color='orange', linestyle='--', lw=1.5, alpha=0.7, label=r'$\ln 2$')
    ax.set_title('Absolute vs Conditional Convergence\nSeries converges but absolute diverges', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$S_n$'); ax.set_xlim(0.5,30.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Alternating Series — Conditional Convergence', fontsize=14, fontweight='bold')
    save('18a-alternating-series.png')

def fig_convergence_tests():
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.axis('off')
    info = (
        "Convergence Tests — Decision Flow:\n\n"
        "1. Divergence Test: $\\lim a_n \\neq 0$? → Diverge\n"
        "   (If $\\lim a_n = 0$, test is inconclusive)\n\n"
        "2. Recognizable type?\n"
        "   • Geometric $\\sum ar^n$: converges iff $|r| < 1$\n"
        "   • $p$-series $\\sum 1/n^p$: converges iff $p > 1$\n"
        "   • Telescoping: write $b_n - b_{n+1}$, cancel\n\n"
        "3. Integral Test: $a_n = f(n)$, $f$ positive/dec.\n"
                "   $\\int f(x)\\,dx$ converges  $\\Longleftrightarrow$  $\\sum a_n$ converges\n\n"
        "4. Comparison: bound by known series\n"
                "    • Direct: $0 \\leq a_n \\leq b_n$, $\\sum b_n$ conv. $\\rightarrow$ $\\sum a_n$ conv.\n"
        "    • Limit: $\\lim a_n/b_n = c > 0$ → same fate\n\n"
        "5. Ratio Test: $\\lim |a_{n+1}/a_n| = \\rho$\n"
        "    $\\rho < 1$ → conv., $\\rho > 1$ → div., $\\rho = 1$ → inconclusive\n\n"
        "6. Alternating Series: $a_n \\searrow 0$ → converges\n"
        "    • Absolutely convergent if $\\sum |a_n|$ converges\n"
        "    • Conditionally convergent otherwise"
    )
    ax.text(0.05, 0.5, info, transform=ax.transAxes, fontsize=10,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))
    ax.set_title('Convergence Tests — Complete Reference', fontweight='bold', fontsize=13)
    save('18a-convergence-tests.png')

if __name__ == "__main__":
    print("Generating 18A graphs...")
    fig_geometric_series(); fig_p_series(); fig_ratio_test()
    fig_alternating_series(); fig_convergence_tests()
    print("Done! ✓")
