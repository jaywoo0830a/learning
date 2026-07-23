#!/usr/bin/env python3
"""Generate all graphs for Session 19C — Advanced First-Order."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '19C'

def exact_ode_potential():
    """19C-1: Exact ODE potential surface φ(x,y) = x² + xy + y² — 3D+2D+1D"""
    fig = plt.figure(figsize=(14, 10))
    
    x = np.linspace(-3, 3, 60)
    y = np.linspace(-3, 3, 60)
    X, Y = np.meshgrid(x, y)
    phi = X**2 + X*Y + Y**2
    
    # 3D — potential surface
    ax = fig.add_subplot(221, projection='3d')
    surf = ax.plot_surface(X, Y, phi, cmap='viridis', alpha=0.9,
                           shade=True, antialiased=True, edgecolor='none')
    # Add level curves on surface
    levels = np.linspace(1, 12, 6)
    for lvl in levels:
        ax.contour(X, Y, phi, levels=[lvl], colors='red', alpha=0.5, linewidths=1)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('φ(x,y)')
    ax.set_title('3D: Potential Surface φ = x²+xy+y²', fontsize=10)
    ax.view_init(30, -60)
    
    # 2D — vector field + level curves
    ax2 = fig.add_subplot(222)
    contour = ax2.contour(X, Y, phi, levels=15, colors='green', alpha=0.6, linewidths=1)
    ax2.clabel(contour, inline=True, fontsize=8)
    
    # Gradient vector field
    skip = 3
    Xs, Ys = X[::skip, ::skip], Y[::skip, ::skip]
    M = 2*Xs + Ys
    N = Xs + 2*Ys
    mag = np.sqrt(M**2 + N**2)
    ax2.quiver(Xs, Ys, M/mag, N/mag, mag, cmap='plasma', alpha=0.7, width=0.005)
    
    ax2.set_xlim(-3, 3); ax2.set_ylim(-3, 3)
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.set_title('2D: ∇φ (arrows) ⊥ Level Curves')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    
    # 1D — slice along y=x
    ax3 = fig.add_subplot(223)
    x_slice = np.linspace(-3, 3, 100)
    phi_slice = x_slice**2 + x_slice*x_slice + x_slice**2  # y=x → 3x²
    ax3.plot(x_slice, phi_slice, 'b-', lw=2)
    ax3.axvline(0, color='gray', ls='--', lw=0.5)
    ax3.set_xlim(-3, 3)
    ax3.set_xlabel('x (along y=x)'); ax3.set_ylabel('φ(x,x)')
    ax3.set_title('1D: Slice along y=x — Minimum at Origin')
    ax3.grid(True, alpha=0.3)
    
    # 1D — level curves as ellipses
    ax4 = fig.add_subplot(224)
    for lvl in [1, 3, 6, 10]:
        theta = np.linspace(0, 2*np.pi, 200)
        # Parametric form of ellipse: x² + xy + y² = C
        a = np.sqrt(lvl * 2/3)
        b = np.sqrt(lvl * 2)
        x_el = a * np.cos(theta)
        y_el = -0.5*x_el + b * np.sin(theta)
        ax4.plot(x_el, y_el, lw=1.5, label=f'φ={lvl}')
    ax4.set_xlim(-4, 4); ax4.set_ylim(-4, 4)
    ax4.set_xlabel('x'); ax4.set_ylabel('y')
    ax4.set_title('Level Curves φ(x,y)=C (Ellipses)')
    ax4.set_aspect('equal')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/exact-ode-potential.png', dpi=DPI)
    plt.close()
    print('  ✓ exact-ode-potential.png')

if __name__ == '__main__':
    exact_ode_potential()
