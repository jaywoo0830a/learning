#!/usr/bin/env python3
"""Generate graphs for Session 17A: Area and Volume."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os

OUT = os.path.dirname(os.path.abspath(__file__)) + "/17A"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'figure.dpi': 150, 'font.size': 10, 'axes.titlesize': 12, 'axes.labelsize': 10})

def save(name):
    plt.tight_layout(pad=1.5); plt.savefig(f"{OUT}/{name}", bbox_inches='tight', facecolor='white', edgecolor='none'); plt.close()
    print(f"  ✓ {name}")

def fig_area_between_curves():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(-0.5, 1.5, 200)
    # Left: area between x² and x
    ax = axes[0]
    ax.plot(x, x**2, 'b-', lw=2.5, label='$y=x^2$')
    ax.plot(x, x, 'r-', lw=2.5, label='$y=x$')
    ax.fill_between(x, x**2, x, where=(x>=0)&(x<=1), alpha=0.2, color='purple')
    ax.annotate('$A = \\int_0^1 (x-x^2)dx = \\frac{1}{6}$', (0.5,0.3), fontsize=11, ha='center',
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('Area: $y=x$ (top) minus $y=x^2$ (bottom)', fontweight='bold')
    ax.axhline(0,color='gray',lw=0.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    ax.set_xlim(-0.5,1.5); ax.set_ylim(-0.2,1.8)
    # Right: area with respect to y
    ax = axes[1]
    y_vals = np.linspace(-1, 2, 200)
    ax.plot(y_vals**2, y_vals, 'b-', lw=2.5, label='$x=y^2$')
    ax.plot(y_vals+2, y_vals, 'r-', lw=2.5, label='$x=y+2$')
    ax.fill_betweenx(y_vals, y_vals**2, y_vals+2, where=(y_vals>=-1)&(y_vals<=2), alpha=0.2, color='purple')
    ax.set_title('$A = \\int_{-1}^2 [(y+2)-y^2] dy = \\frac{9}{2}$', fontweight='bold')
    ax.axhline(0,color='gray',lw=0.5); ax.axvline(0,color='gray',lw=0.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    ax.set_xlim(-1,5); ax.set_ylim(-1.5,3)
    fig.suptitle('Area Between Curves — $x$ and $y$ integration', fontsize=14, fontweight='bold')
    save('17a-area-between-curves.png')

def fig_trig_area():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, np.pi/2, 200)
    ax.plot(x, np.sin(x), 'b-', lw=2.5, label='$\\sin x$')
    ax.plot(x, np.cos(x), 'r-', lw=2.5, label='$\\cos x$')
    ax.fill_between(x, np.sin(x), np.cos(x), where=(x>=np.pi/4), alpha=0.15, color='blue')
    ax.fill_between(x, np.cos(x), np.sin(x), where=(x<=np.pi/4), alpha=0.15, color='red')
    ax.axvline(np.pi/4, color='green', linestyle='--', lw=2, label='$x=\\pi/4$ (cross)')
    ax.annotate('$A = 2\\sqrt{2}-2$', (np.pi/4,0.5), fontsize=12, ha='center',
               bbox=dict(boxstyle='round',facecolor='wheat',alpha=0.7))
    ax.set_title('Trigonometric Area\n$\\sin x$ and $\\cos x$ on $[0,\\pi/2]$', fontweight='bold')
    ax.set_xlim(0,np.pi/2); ax.set_ylim(-0.2,1.2); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    save('17a-trig-area.png')

def fig_disk_method():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(0, 4, 200)
    # Left: region with disk
    ax = axes[0]
    ax.plot(x, np.sqrt(x), 'b-', lw=2.5, label='$y=\\sqrt{x}$')
    ax.plot(x, -np.sqrt(x), 'gray', linestyle='--', lw=1, alpha=0.5)
    ax.fill_between(x, 0, np.sqrt(x), alpha=0.15, color='blue')
    # Sample disk at x=2
    r2 = np.sqrt(2)
    ax.plot([2,2],[-r2,r2],'r-',lw=3,alpha=0.7)
    ax.annotate('$R(x)=\\sqrt{x}$\nArea $=\\pi x$', (2.5, np.sqrt(2.5)), fontsize=9, color='red')
    ax.set_title('Disk Method: $V = \\pi\\int_0^4 (\\sqrt{x})^2 dx = 8\\pi$', fontweight='bold')
    ax.set_xlim(0,4.5); ax.set_ylim(-2.5,2.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9); ax.set_aspect('equal')
    # Right: accumulated volume
    ax = axes[1]
    V = np.pi * x**2 / 2
    ax.plot(x, V, 'r-', lw=2.5, label='$V(x) = \\pi x^2/2$')
    ax.fill_between(x, 0, V, alpha=0.1, color='red')
    ax.plot(4, 8*np.pi, 'ro', markersize=10, zorder=5)
    ax.annotate('$V(4) = 8\\pi$', (4, 8*np.pi), textcoords="offset points", xytext=(10,-15), fontsize=10, color='red', fontweight='bold')
    ax.set_title('Accumulated Volume', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$V(x)$'); ax.set_xlim(0,4.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    fig.suptitle('Disk Method — Solid of Revolution', fontsize=14, fontweight='bold')
    save('17a-disk-method.png')

def fig_washer_method():
    fig, ax = plt.subplots(figsize=(9, 7))
    x = np.linspace(0, 1, 200)
    ax.plot(x, x, 'b-', lw=2.5, label='$y=x$ (outer)')
    ax.plot(x, x**2, 'r-', lw=2.5, label='$y=x^2$ (inner)')
    ax.fill_between(x, x**2, x, alpha=0.2, color='purple')
    # Sample washer at x=0.6
    xs = 0.6
    ax.plot([xs,xs],[xs**2,xs],'g-',lw=3)
    ax.annotate('Washer at $x=0.6$\n$R_{out}=0.6$, $R_{in}=0.36$', (xs+0.02, (xs+xs**2)/2), fontsize=9, color='green', fontweight='bold')
    ax.set_title('Washer Method: $V = \\pi\\int_0^1 (x^2 - x^4) dx = \\frac{2\\pi}{15}$', fontweight='bold')
    ax.set_xlim(0,1.2); ax.set_ylim(-0.1,1.2); ax.grid(True,alpha=0.3); ax.legend(fontsize=9); ax.set_aspect('equal')
    save('17a-washer-method.png')

def fig_shell_method():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    x = np.linspace(0, 2, 200)
    # Left: region with sample shell
    ax = axes[0]
    ax.plot(x, x**2, 'b-', lw=2.5, label='$y=x^2$')
    ax.fill_between(x, 0, x**2, alpha=0.1, color='blue')
    # Sample shell at x=1.5
    xs = 1.5
    ax.plot([xs,xs],[0,xs**2],'r-',lw=3)
    ax.annotate(f'Shell at $x={xs}$\nheight $=x^2={xs**2:.2f}$', (xs+0.05, xs**2/2), fontsize=9, color='red', fontweight='bold')
    ax.set_title('Shell Method: $V = 2\\pi\\int_0^2 x\\cdot x^2 dx = 8\\pi$', fontweight='bold')
    ax.set_xlim(0,2.5); ax.set_ylim(-0.2,4.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    # Right: the shell integrand
    ax = axes[1]
    ax.plot(x, x*x**2, 'g-', lw=2.5, label='$x \\cdot h(x) = x^3$')
    ax.fill_between(x, 0, x**3, alpha=0.15, color='green')
    ax.set_title('Integrand $x \\cdot h(x)$ — $V = 2\\pi\\int x^3 dx$', fontweight='bold')
    ax.set_xlabel('$x$'); ax.set_ylabel('$x \\cdot h(x)$'); ax.set_xlim(0,2.5); ax.grid(True,alpha=0.3); ax.legend(fontsize=9)
    fig.suptitle('Shell Method — Rotation About $y$-Axis', fontsize=14, fontweight='bold')
    save('17a-shell-method.png')

def fig_revolution_summary():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    x = np.linspace(0, 1, 200)
    # Disk
    ax = axes[0]; ax.plot(x, x, 'b-', lw=2)
    ax.fill_between(x, 0, x, alpha=0.15, color='blue')
    ax.set_title('Disk: $V=\\pi\\int R^2 dx$\nRotate region, no hole', fontweight='bold'); ax.grid(True,alpha=0.3)
    # Washer
    ax = axes[1]; ax.plot(x, x, 'b-', lw=2, label='outer'); ax.plot(x, x**2, 'r-', lw=2, label='inner')
    ax.fill_between(x, x**2, x, alpha=0.15, color='purple')
    ax.set_title('Washer: $V=\\pi\\int (R^2-r^2) dx$\nRotate region with hole', fontweight='bold'); ax.grid(True,alpha=0.3); ax.legend(fontsize=7)
    # Shell
    ax = axes[2]; ax.plot(x, x**2, 'b-', lw=2)
    ax.fill_between(x, 0, x**2, alpha=0.15, color='green')
    ax.set_title('Shell: $V=2\\pi\\int x\\cdot h(x) dx$\nShells about $y$-axis', fontweight='bold'); ax.grid(True,alpha=0.3)
    for ax in axes: ax.set_xlim(0,1.2); ax.set_ylim(-0.1,1.2)
    fig.suptitle('Volume Methods — Disk, Washer, Shell', fontsize=14, fontweight='bold')
    save('17a-revolution-summary.png')

if __name__ == "__main__":
    print("Generating 17A graphs...")
    fig_area_between_curves(); fig_trig_area(); fig_disk_method()
    fig_washer_method(); fig_shell_method(); fig_revolution_summary()
    print("Done! ✓")
