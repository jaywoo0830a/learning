#!/usr/bin/env python3
"""Generate graphs for Session 18C: Taylor Series."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os, math

OUT = os.path.dirname(os.path.abspath(__file__)) + "/18C"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_taylor_polynomials():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-2*np.pi, 2*np.pi, 300)
    # Left: sin x with Taylor polynomials
    ax = axes[0]
    ax.plot(x, np.sin(x), 'k-', lw=2.5, label='$\\sin x$ (exact)')
    for N, c in [(1, 'blue'), (3, 'green'), (5, 'orange'), (7, 'red')]:
        S = np.zeros_like(x)
        for n in range(0, (N+1)//2):
            k = 2*n + 1
            S += (-1)**n * x**k / np.array([math.factorial(k) for _ in x])
        ax.plot(x, S, '-', color=c, lw=1.5, label=f'$T_{{{N}}}(x)$')
    ax.set_title('Taylor Polynomials of $\\sin x$ at $a=0$\nHigher degree = better approximation', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylim(-3,3); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: error behavior
    ax = axes[1]
    ax.plot(x, np.abs(np.sin(x) - x), 'b-', lw=2, label='$|\\sin x - T_1|$')
    ax.plot(x, np.abs(np.sin(x) - (x - x**3/6)), 'g-', lw=2, label='$|\\sin x - T_3|$')
    ax.plot(x, np.abs(np.sin(x) - (x - x**3/6 + x**5/120)), 'orange', lw=2, label='$|\\sin x - T_5|$')
    ax.set_yscale('log')
    ax.set_title('Error $|\\sin x - T_N(x)|$ (log scale)\nError decreases as degree increases', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylim(1e-17, 10); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Taylor Polynomials — Approximating $\\sin x$', fontsize=14, fontweight='bold')
    save('18c-taylor-polynomials.png')

def fig_taylor_exp():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-2, 3, 200)
    # Left: e^x with Taylor polynomials
    ax = axes[0]
    ax.plot(x, np.exp(x), 'k-', lw=2.5, label='$e^x$ (exact)')
    for N, c in [(1, 'blue'), (2, 'green'), (3, 'orange'), (5, 'red')]:
        S = np.zeros_like(x)
        for n in range(N+1):
            S += x**n / np.array([math.factorial(n) for _ in x])
        ax.plot(x, S, '-', color=c, lw=1.5, label=f'$T_{{{N}}}(x)$')
    ax.set_title('Taylor Polynomials of $e^x$ at $a=0$\n$T_N(x) = \\sum_{n=0}^N x^n/n!$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylim(-2,10); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: error
    ax = axes[1]
    for N, c in [(1,'blue'),(3,'green'),(5,'red')]:
        S = np.zeros_like(x)
        for n in range(N+1):
            S += x**n / np.array([math.factorial(n) for _ in x])
        err = np.abs(np.exp(x) - S)
        err[err < 1e-17] = 1e-17
        ax.plot(x, err, '-', color=c, lw=2, label=f'$|e^x - T_{{{N}}}|$')
    ax.set_yscale('log')
    ax.set_title('Error $|e^x - T_N(x)|$ (log scale)\nExponential convergence near $x=0$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylim(1e-17, 10); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Taylor Polynomials — Approximating $e^x$', fontsize=14, fontweight='bold')
    save('18c-taylor-exp.png')

def fig_error_bound():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    # Left: Lagrange remainder concept
    ax = axes[0]
    x = np.linspace(0, 1, 100)
    ax.plot(x, np.exp(x), 'k-', lw=2.5, label='$f(x)=e^x$')
    T3 = 1 + x + x**2/2 + x**3/6
    ax.plot(x, T3, 'b-', lw=2, label='$T_3(x)$')
    ax.fill_between(x, T3, np.exp(x), alpha=0.15, color='red', label='error $R_3(x)$')
    ax.set_title('Lagrange Remainder: $f = T_n + R_n$\n$R_n(x) = \\frac{f^{(n+1)}(c)}{(n+1)!}x^{n+1}$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylim(0,3); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # Right: error bound vs actual error
    ax = axes[1]
    x_vals = np.array([0.1, 0.2, 0.5, 1.0])
    for xi in x_vals:
        actual_err = abs(np.exp(xi) - sum(xi**n/math.factorial(n) for n in range(4)))
        bound = np.exp(xi) * xi**4 / 24
        ax.bar(xi, actual_err, width=0.04, alpha=0.6, color='blue', label='actual error' if xi==0.1 else '')
        ax.bar(xi+0.04, bound, width=0.04, alpha=0.6, color='red', label='error bound' if xi==0.1 else '')
    ax.set_yscale('log')
    ax.set_title(r'Error Bound: $|R_n| \leq \frac{M}{(n+1)!}|x|^{n+1}$' + '\n' + r'Bound always $\geq$ actual error', fontweight='bold')
    ax.set_xlabel('$x$'); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    fig.suptitle('Taylor Error Bounds — Lagrange Remainder', fontsize=14, fontweight='bold')
    save('18c-error-bound.png')

def fig_series_operations():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    x = np.linspace(-1.5, 1.5, 200)
    # (1) sin(x²) by substitution
    ax = axes[0]
    ax.plot(x, np.sin(x**2), 'k-', lw=2.5, label='$\\sin(x^2)$')
    for N, c in [(1,'blue'),(3,'green'),(5,'red')]:
        S = np.zeros_like(x)
        for n in range(N+1):
            k = 2*n + 1
            S += (-1)**n * x**(4*n+2) / np.array([math.factorial(k) for _ in x])
        ax.plot(x, S, '--', color=c, lw=1.5, label=f'{2*N+1} terms')
    ax.set_title('$\\sin(x^2) = \\sum (-1)^n x^{4n+2}/(2n+1)!$\nSubstitution: $x \\to x^2$ in $\\sin x$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # (2) (1+x)^(1/2) binomial
    ax = axes[1]
    ax.plot(x, np.sqrt(1+x), 'k-', lw=2.5, label='$\\sqrt{1+x}$')
    for N, c in [(1,'blue'),(2,'green'),(3,'red')]:
        S = np.zeros_like(x)
        coeff = 1.0
        for n in range(N+1):
            if n == 0:
                S += 1
            else:
                coeff = coeff * (0.5 - n + 1) / n
                S += coeff * x**n
        ax.plot(x[x>-1], S[x>-1], '--', color=c, lw=1.5, label=f'{N} terms')
    ax.set_title('$\\sqrt{1+x}$ via Binomial Series\n$(1+x)^{1/2} = \\sum \\binom{1/2}{n} x^n$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_xlim(-1.1,1.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=8)
    # (3) e^x * e^(-x) → 1
    ax = axes[2]
    ax.axis('off')
    info = (
        "Building Series — Key Operations:\n\n"
        "1. Substitution:\n"
        "   $\\sin(x^2) = \\sum (-1)^n x^{4n+2}/(2n+1)!$\n\n"
        "2. Multiply by $x$:\n"
        "   $x e^x = \\sum x^{n+1}/n!$\n\n"
        "3. Divide by $x$:\n"
        "   $\\frac{e^x-1}{x} = \\sum x^n/(n+1)!$\n\n"
        "4. Binomial series:\n"
        "   $(1+x)^k = \\sum \\binom{k}{n} x^n$\n\n"
        "5. Integrate:\n"
        "   $\\int_0^x e^{-t^2} dt = \\sum \\frac{(-1)^n x^{2n+1}}{n!(2n+1)}$\n\n"
        "6. Differentiate:\n"
        "   $\\frac{d}{dx} e^x = e^x$ matches series!"
    )
    ax.text(0.1, 0.5, info, transform=ax.transAxes, fontsize=10,
            fontfamily='monospace', verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='#f0f0f0', alpha=0.8))
    ax.set_title('Series Operations Reference', fontweight='bold')
    fig.suptitle('Building Taylor Series — Substitution, Binomial, Operations', fontsize=14, fontweight='bold')
    save('18c-series-operations.png')

if __name__ == "__main__":
    print("Generating 18C graphs...")
    fig_taylor_polynomials(); fig_taylor_exp(); fig_error_bound(); fig_series_operations()
    print("Done! ✓")
