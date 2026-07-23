#!/usr/bin/env python3
"""Generate all graphs for Session 19B — First-Order Solution Methods."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '19B'

def integrating_factor():
    """19B-1: Integrating factor — 3D+2D+1D for y' + 2xy = x"""
    fig = plt.figure(figsize=(14, 10))
    
    mu = lambda x: np.exp(x**2)
    Q = lambda x: x
    y_exact = lambda x, C: 0.5 + C * np.exp(-x**2)
    
    x = np.linspace(-2, 2, 200)
    X = np.linspace(-2, 2, 30)
    Y = np.linspace(-1, 2, 30)
    Xg, Yg = np.meshgrid(X, Y)
    
    # 3D — surface μy
    ax = fig.add_subplot(221, projection='3d')
    XX, YY = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-1, 2, 60))
    muY = mu(XX) * YY
    surf = ax.plot_surface(XX, YY, muY, cmap='viridis', alpha=0.85,
                           shade=True, antialiased=True, edgecolor='none')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('μ(x)·y')
    ax.set_title('3D: Surface μ(x)·y', fontsize=10)
    ax.view_init(25, -50)
    
    # 2D — slope field + solution curves
    ax2 = fig.add_subplot(222)
    U = np.ones_like(Xg)
    V = -2*Xg*Yg + Xg
    M = np.sqrt(U**2 + V**2)
    ax2.quiver(Xg, Yg, U/M, V/M, M, alpha=0.5, cmap='viridis', width=0.005)
    
    for C in [-0.5, 0, 0.5, 1, 2]:
        y = y_exact(x, C)
        ax2.plot(x, y, lw=2, label=f'C={C}')
    
    ax2.set_xlim(-2, 2); ax2.set_ylim(-1, 2)
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.set_title('2D: Slope Field + Solutions')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    # 1D — product rule verification
    ax3 = fig.add_subplot(223)
    mu_y = mu(x) * y_exact(x, 1)
    mu_Q = mu(x) * Q(x)
    d_mu_y = np.gradient(mu_y, x[1]-x[0])
    ax3.plot(x, mu_y, 'b-', lw=2, label='μy')
    ax3.plot(x, mu_Q, 'r--', lw=1.5, alpha=0.7, label='μQ')
    ax3.plot(x, d_mu_y, 'g:', lw=1.5, alpha=0.7, label='d(μy)/dx')
    ax3.set_xlim(-2, 2)
    ax3.set_xlabel('x'); ax3.set_ylabel('Value')
    ax3.set_title('1D: Product Rule — (μy)\' = μQ')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    # 1D — equilibrium behavior
    ax4 = fig.add_subplot(224)
    for C in [-1, -0.5, 0, 0.5, 1, 2]:
        y = y_exact(x, C)
        ax4.plot(x, y, lw=1.5, label=f'C={C}')
    ax4.axhline(0.5, color='red', ls='--', lw=2, alpha=0.8, label='y=0.5 (equilibrium)')
    ax4.set_xlim(-2, 2); ax4.set_ylim(-1, 3)
    ax4.set_xlabel('x'); ax4.set_ylabel('y')
    ax4.set_title('Solutions Approach y=0.5')
    ax4.legend(fontsize=7)
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/integrating-factor.png', dpi=DPI)
    plt.close()
    print('  ✓ integrating-factor.png')

if __name__ == '__main__':
    integrating_factor()
