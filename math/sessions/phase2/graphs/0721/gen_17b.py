#!/usr/bin/env python3
"""Generate graphs for Session 17B: Arc Length, Surface Area, Improper Integrals."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/17B"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_arc_length_formula():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(0, 4, 200)
    f = lambda x: x**1.5
    # Left: curve with poly approx
    ax = axes[0]; ax.plot(x, f(x), 'b-', lw=2.5, label='$y=x^{3/2}$')
    n = 6; xs = np.linspace(0, 4, n)
    ax.plot(xs, f(xs), 'r.-', lw=1, markersize=8, label=f'{n} segments')
    for i in range(n-1):
        ax.plot([xs[i],xs[i+1]],[f(xs[i]),f(xs[i+1])],'r-',lw=2)
    ax.set_title('Arc Length: $L = \\int \\sqrt{1+(f\')^2} dx$\nPolygonal approximation', fontweight='bold')
    ax.set_xlim(0,4.5); ax.set_ylim(-0.5,9); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    # Right: integrand
    ax = axes[1]
    integrand = np.sqrt(1 + (1.5*np.sqrt(x))**2)
    ax.plot(x, integrand, 'r-', lw=2.5, label='$\\sqrt{1+(f\')^2}$')
    ax.fill_between(x, 0, integrand, alpha=0.15, color='red')
    L = 8/27*(10**1.5 - 1)
    ax.annotate(f'$L \\approx {L:.2f}$', (2, integrand[100]+0.5), fontsize=12, fontweight='bold',
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('Integrand $\\sqrt{1+(f\')^2}$ — area = arc length', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_xlim(0,4.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    fig.suptitle('Arc Length — Formula and Approximation', fontsize=14, fontweight='bold')
    save('17b-arc-length-formula.png')

def fig_surface_revolution():
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2*np.pi, 40)
    x = np.linspace(0, 4, 50)
    T, X = np.meshgrid(theta, x)
    R = np.sqrt(X)
    Y = R * np.cos(T); Z = R * np.sin(T)
    ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis', edgecolor='none')
    # Highlight rings
    for xi in [1, 2, 3]:
        ri = np.sqrt(xi)
        ax.plot([xi]*len(theta), ri*np.cos(theta), ri*np.sin(theta), 'r-', lw=1.5, alpha=0.8)
    ax.set_title('Surface of Revolution: $y=\\sqrt{x}$ about $x$-axis\n$S=2\\pi\\int f(x)\\sqrt{1+(f\')^2}dx$',
                 fontweight='bold', fontsize=11)
    ax.set_xlim(0,4.5); ax.set_ylim(-2.5,2.5); ax.set_zlim(-2.5,2.5)
    ax.view_init(elev=20, azim=-60)
    save('17b-surface-revolution.png')

def fig_improper_infinite():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(1, 10, 200)
    # Left: 1/x² converges
    ax = axes[0]
    ax.plot(x, 1/x**2, 'b-', lw=2.5, label='$1/x^2$ (converges)')
    ax.fill_between(x, 0, 1/x**2, alpha=0.15, color='blue')
    ax.annotate('$\\int_1^\\infty \\frac{1}{x^2}dx = 1$', (3, 0.5), fontsize=12,
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('$\\int_1^\\infty \\frac{1}{x^2}dx$ — Finite area!\n$p=2>1$ → converges', fontweight='bold')
    ax.set_xlim(1,10); ax.set_ylim(0,1); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    # Right: 1/x diverges
    ax = axes[1]
    ax.plot(x, 1/x, 'r-', lw=2.5, label='$1/x$ (diverges)')
    ax.fill_between(x, 0, 1/x, alpha=0.1, color='red')
    # Fill to show infinite area
    x2 = np.linspace(10, 30, 50)
    ax.plot(x2, 1/x2, 'r-', lw=2, alpha=0.5)
    ax.fill_between(x2, 0, 1/x2, alpha=0.05, color='red')
    ax.annotate('$\\int_1^\\infty \\frac{1}{x}dx = \\infty$\n$p=1$ → diverges', (5, 0.3), fontsize=12,
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('$\\int_1^\\infty \\frac{1}{x}dx$ — Infinite area!\n$p=1$ → diverges', fontweight='bold')
    ax.set_xlim(1,15); ax.set_ylim(0,1); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    fig.suptitle('Improper Integrals — Infinite Intervals', fontsize=14, fontweight='bold')
    save('17b-improper-infinite.png')

def fig_improper_unbounded():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(0.001, 1, 200)
    # Left: 1/√x converges
    ax = axes[0]
    ax.plot(x, 1/np.sqrt(x), 'b-', lw=2.5, label='$1/\\sqrt{x}$ (converges)')
    ax.fill_between(x, 0, 1/np.sqrt(x), alpha=0.15, color='blue')
    ax.annotate('$\\int_0^1 \\frac{1}{\\sqrt{x}}dx = 2$\n$p=1/2<1$ → converges', (0.5, 3), fontsize=11,
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('$\\int_0^1 \\frac{1}{\\sqrt{x}}dx$ — Finite!\nInfinite height, finite area', fontweight='bold')
    ax.set_xlim(0,1); ax.set_ylim(0,8); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    # Right: 1/x² diverges near 0
    ax = axes[1]
    ax.plot(x, 1/x**2, 'r-', lw=2.5, label='$1/x^2$ (diverges)')
    ax.fill_between(x, 0, 1/x**2, alpha=0.1, color='red')
    ax.annotate('$\\int_0^1 \\frac{1}{x^2}dx = \\infty$\n$p=2>1$ → diverges', (0.5, 10), fontsize=11,
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('$\\int_0^1 \\frac{1}{x^2}dx$ — Infinite!\n$p \\geq 1$ at singularity → diverges', fontweight='bold')
    ax.set_xlim(0,1); ax.set_ylim(0,20); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    fig.suptitle('Improper Integrals — Unbounded Integrands', fontsize=14, fontweight='bold')
    save('17b-improper-unbounded.png')

def fig_p_test():
    fig, ax = plt.subplots(figsize=(9, 7))
    p_vals = np.linspace(0.1, 3, 100)
    # ∫₁^∞ 1/x^p dx converges to 1/(p-1) for p>1
    conv = 1/(p_vals-1)
    conv[p_vals <= 1] = np.nan
    ax.plot(p_vals, conv, 'b-', lw=2.5, label='$\\int_1^\\infty 1/x^p dx = 1/(p-1)$ for $p>1$')
    ax.axvline(1, color='red', linestyle='--', lw=2.5, label='$p=1$ boundary')
    ax.fill_between(p_vals[p_vals>1], 0, conv[p_vals>1], alpha=0.12, color='blue', label='CONVERGES ($p>1$)')
    ax.fill_betweenx([0, 8], 0.1, 1, alpha=0.08, color='red', label='DIVERGES ($p\\leq 1$)')
    ax.set_title('$p$-Test for Improper Integrals\n$\\int_1^\\infty \\frac{1}{x^p}dx$ converges iff $p>1$', fontweight='bold')
    ax.set_xlabel('$p$'); ax.set_ylabel('$\\int_1^\\infty 1/x^p dx$')
    ax.set_xlim(0.1, 3); ax.set_ylim(0, 5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    save('17b-p-test.png')

def fig_gabriels_horn():
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2*np.pi, 50)
    x = np.linspace(1, 5, 80)
    T, X = np.meshgrid(theta, x)
    R = 1/X
    Y = R * np.cos(T); Z = R * np.sin(T)
    ax.plot_surface(X, Y, Z, alpha=0.5, color='coral', edgecolor='none')
    # Add axis
    ax.plot([0,6],[0,0],[0,0],'gray',lw=1)
    ax.set_title("Gabriel's Horn\n$y=1/x$ rotated about $x$-axis\nFinite volume $\\pi$, infinite surface area",
                 fontweight='bold', fontsize=11)
    ax.set_xlim(1,5.5); ax.set_ylim(-1,1); ax.set_zlim(-1,1)
    ax.view_init(elev=20, azim=-60)
    save('17b-gabriels-horn.png')

if __name__ == "__main__":
    print("Generating 17B graphs...")
    fig_arc_length_formula(); fig_surface_revolution(); fig_improper_infinite()
    fig_improper_unbounded(); fig_p_test(); fig_gabriels_horn()
    print("Done! ✓")
