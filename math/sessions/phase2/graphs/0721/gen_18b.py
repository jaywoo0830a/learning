#!/usr/bin/env python3
"""Generate graphs for Session 18B: Power Series."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os, math

OUT = os.path.dirname(os.path.abspath(__file__)) + "/18B"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_radius_convergence():
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    x = np.linspace(-3, 3, 200)
    # (1) R=∞: e^x
    ax = axes[0,0]
    S = np.zeros_like(x)
    for n in range(8):
        S += x**n / np.array([math.factorial(n) for _ in x])
        # Simpler: just compute partial sums
    ax.axis('off')
    info1 = (
        "Radius of Convergence $R$:\n\n"
        "$R = \\infty$: $e^x = \\sum x^n/n!$\n"
        "→ Converges for ALL $x$\n\n"
        "$R = 1$: $1/(1-x) = \\sum x^n$\n"
        "→ Converges for $|x| < 1$\n\n"
        "$R = 0$: $\\sum n! x^n$\n"
        "→ Converges only at $x=0$"
    )
    ax.text(0.1, 0.5, info1, transform=ax.transAxes, fontsize=11,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))
    ax.set_title('Radius of Convergence — Three Cases', fontweight='bold')
    # (2) Partial sums converging
    ax = axes[0,1]
    x_vals = np.linspace(-0.95, 0.95, 100)
    for N, color in [(1,'blue'),(3,'green'),(5,'orange'),(10,'red')]:
        S = np.zeros_like(x_vals)
        for n in range(N+1):
            S += x_vals**n
        ax.plot(x_vals, S, '-', color=color, lw=1.5, label=f'$S_{{{N}}}$')
    ax.plot(x_vals, 1/(1-x_vals), 'k--', lw=2.5, label='$1/(1-x)$')
    ax.axvline(-1,color='gray',linestyle=':',lw=1); ax.axvline(1,color='gray',linestyle=':',lw=1)
    ax.set_title('Partial Sums of $\\sum x^n$ converge to $1/(1-x)$\non $(-1,1)$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$S_N(x)$'); ax.set_xlim(-1.2,1.2); ax.set_ylim(-2,5)
    ax.grid(True,alpha=0.3); ax.legend(fontsize=7)
    # (3) Endpoint behavior
    ax = axes[1,0]
    n = np.arange(1, 30)
    for name, c, series in [('$\\sum x^n/n$ at $x=1$', 'red', 1/n),
                             ('$\\sum x^n/n$ at $x=-1$', 'blue', (-1)**n/n)]:
        S = np.cumsum(series)
        ax.plot(n, S, '-', color=c, lw=2, label=name)
    ax.set_title('Endpoint Behavior: $\\sum x^n/n$\n$x=1$ diverges, $x=-1$ converges', fontweight='bold')
    ax.set_xlabel('$n$'); ax.set_ylabel('$S_N$'); ax.set_xlim(0.5,29.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # (4) Number line
    ax = axes[1,1]
    ax.axis('off')
    info2 = (
        "Interval of Convergence:\n\n"
        "$\\sum c_n(x-a)^n$\n\n"
        "Center: $x=a$\n"
        "Radius: $R = \\lim |c_n/c_{n+1}|$\n\n"
        "Converges for $|x-a| < R$\n"
        "Check endpoints $x = a \\pm R$ separately!\n\n"
        "Examples:\n"
        "$\\sum x^n$: $R=1$, interval $(-1,1)$\n"
        "$\\sum x^n/n$: $R=1$, interval $[-1,1)$\n"
        "$\\sum x^n/n^2$: $R=1$, interval $[-1,1]$\n"
        "$\\sum x^n/n!$: $R=\\infty$, interval $(-\\infty,\\infty)$"
    )
    ax.text(0.1, 0.5, info2, transform=ax.transAxes, fontsize=10,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))
    ax.set_title('Interval of Convergence', fontweight='bold')
    fig.suptitle('Power Series — Radius and Interval of Convergence', fontsize=14, fontweight='bold')
    save('18b-radius-convergence.png')

def fig_building_series():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    x = np.linspace(-0.95, 0.95, 100)
    # (1) Geometric → 1/(1+x)
    ax = axes[0]
    true_fn = 1/(1+x)
    for N, c in [(2,'blue'),(5,'green'),(10,'red')]:
        S = np.zeros_like(x)
        for n in range(N+1):
            S += (-x)**n
        ax.plot(x, S, '-', color=c, lw=1.5, label=f'$S_{{{N}}}$')
    ax.plot(x, true_fn, 'k--', lw=2.5, label='$1/(1+x)$')
    ax.set_title('$\\frac{1}{1+x} = \\sum (-x)^n$\nSubstitute $x\\to-x$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # (2) Integrated → ln(1+x)
    ax = axes[1]
    true_fn2 = np.log(1+x)
    for N, c in [(2,'blue'),(5,'green'),(10,'red')]:
        S = np.zeros_like(x)
        for n in range(1, N+2):
            S += (-1)**(n+1) * x**n / n
        ax.plot(x, S, '-', color=c, lw=1.5, label=f'$S_{{{N}}}$')
    ax.plot(x, true_fn2, 'k--', lw=2.5, label='$\\ln(1+x)$')
    ax.set_title('$\\ln(1+x) = \\sum (-1)^{n+1}x^n/n$\nIntegrate $1/(1+x)$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # (3) Integrated → arctan x
    ax = axes[2]
    true_fn3 = np.arctan(x)
    for N, c in [(1,'blue'),(3,'green'),(10,'red')]:
        S = np.zeros_like(x)
        for n in range(N+1):
            S += (-1)**n * x**(2*n+1) / (2*n+1)
        ax.plot(x, S, '-', color=c, lw=1.5, label=f'$T_{{{2*N+1}}}$')
    ax.plot(x, true_fn3, 'k--', lw=2.5, label='$\\arctan x$')
    ax.set_title('$\\arctan x = \\sum (-1)^n x^{2n+1}/(2n+1)$\nIntegrate $1/(1+x^2)$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Building New Power Series from $\\frac{1}{1-x}$', fontsize=14, fontweight='bold')
    save('18b-building-series.png')

if __name__ == "__main__":
    print("Generating 18B graphs...")
    fig_radius_convergence(); fig_building_series()
    print("Done! ✓")
