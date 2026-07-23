#!/usr/bin/env python3
"""Generate individual graphs for Session 23A — each image is standalone A4-friendly."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '23A'

def path_limit_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    Z = X*Y / (X**2 + Y**2); Z[np.isnan(Z)] = 0
    ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.85, shade=True, antialiased=True, edgecolor='none')
    xl = np.linspace(-2, 2, 80)
    ax.plot(xl, np.zeros_like(xl), np.zeros_like(xl), 'b-', lw=2.5, label='y=0 (limit=0)')
    ax.plot(xl, xl, np.full_like(xl, 0.5), 'r-', lw=2.5, label='y=x (limit=1/2)')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'$f(x,y)=\frac{xy}{x^2+y^2}$ — Two Paths Disagree', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/path-limit-3d.png', dpi=DPI); plt.close()
    print('  ✓ path-limit-3d.png')

def path_limit_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    X, Y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    Z = X*Y / (X**2 + Y**2); Z[np.isnan(Z)] = 0
    cf = ax.contour(X, Y, Z, levels=15, cmap='coolwarm', linewidths=1.2, alpha=0.8)
    ax.clabel(cf, inline=True, fontsize=9)
    xl = np.linspace(-2, 2, 100)
    ax.plot(xl, np.zeros_like(xl), 'b-', lw=2.5, label='y=0 → 0')
    ax.plot(xl, xl, 'r-', lw=2.5, label='y=x → 1/2')
    ax.scatter(0, 0, color='black', s=100, zorder=5)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title('Two Paths, Two Limits — Limit Does Not Exist', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/path-limit-2d.png', dpi=DPI); plt.close()
    print('  ✓ path-limit-2d.png')

def path_limit_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    t = np.linspace(-2, 2, 200)
    ax.plot(t, np.zeros_like(t), 'b-', lw=2.5, label='Along y=0: f=0')
    ax.plot(t, np.full_like(t, 0.5), 'r-', lw=2.5, label='Along y=x: f=1/2')
    ax.axvline(0, color='gray', ls='--', lw=1)
    ax.set_ylim(-0.2, 0.8); ax.set_xlabel('t', fontsize=12); ax.set_ylabel('f(t)', fontsize=12)
    ax.set_title('Values Along Each Path Never Meet', fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/path-limit-1d.png', dpi=DPI); plt.close()
    print('  ✓ path-limit-1d.png')

def polar_squeeze_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-2, 2, 60))
    Z = X**3 / (X**2 + Y**2); Z[np.isnan(Z)] = 0
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9, shade=True, antialiased=True, edgecolor='none')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'$f(x,y)=\frac{x^3}{x^2+y^2}$ — Continuous at (0,0)', fontsize=12)
    ax.view_init(25, -60)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/polar-squeeze-3d.png', dpi=DPI); plt.close()
    print('  ✓ polar-squeeze-3d.png')

def polar_squeeze_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-2, 2, 60))
    Z = X**3 / (X**2 + Y**2); Z[np.isnan(Z)] = 0
    cf = ax.contour(X, Y, Z, levels=15, cmap='viridis', linewidths=1.2, alpha=0.8)
    ax.clabel(cf, inline=True, fontsize=9)
    for r in [0.5, 1, 1.5]:
        th = np.linspace(0, 2*np.pi, 100)
        ax.plot(r*np.cos(th), r*np.sin(th), 'gray', ls='--', lw=1.5, alpha=0.6)
    ax.scatter(0, 0, color='black', s=100, zorder=5)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title('Polar Circles Show r → 0 from All Directions', fontsize=12)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/polar-squeeze-2d.png', dpi=DPI); plt.close()
    print('  ✓ polar-squeeze-2d.png')

def polar_squeeze_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    r = np.linspace(0, 2, 100)
    for th in [0, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3]:
        ax.plot(r, r*np.abs(np.cos(th)**3), lw=1.8, label=f'θ={th:.2f}')
    ax.plot(r, r, 'k--', lw=2.5, label='Bound: |f| ≤ r → 0')
    ax.set_xlabel('r', fontsize=12); ax.set_ylabel('|f(r,θ)|', fontsize=12)
    ax.set_title(r'Polar Squeeze: $|f|=r|\cos^3\theta|\leq r\to 0$', fontsize=12)
    ax.legend(fontsize=9, ncol=2); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/polar-squeeze-1d.png', dpi=DPI); plt.close()
    print('  ✓ polar-squeeze-1d.png')

def level_curves_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    x = np.linspace(-3, 3, 200); X, Y = np.meshgrid(x, x)
    cf = ax.contour(X, Y, X**2 - Y**2, levels=20, cmap='coolwarm', linewidths=1.2)
    ax.clabel(cf, inline=True, fontsize=9)
    ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'Level Curves of $z=x^2-y^2$ (Saddle)', fontsize=12)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/level-curves-2d.png', dpi=DPI); plt.close()
    print('  ✓ level-curves-2d.png')

def level_curves_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-3, 3, 60); X, Y = np.meshgrid(x, x)
    ax.plot_surface(X, Y, X**2 - Y**2, cmap='coolwarm', alpha=0.9, shade=True, antialiased=True, edgecolor='none')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'3D: $z=x^2-y^2$ — Hyperbolic Paraboloid', fontsize=12)
    ax.view_init(25, -50)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/level-curves-3d.png', dpi=DPI); plt.close()
    print('  ✓ level-curves-3d.png')

if __name__ == '__main__':
    path_limit_3d(); path_limit_2d(); path_limit_1d()
    polar_squeeze_3d(); polar_squeeze_2d(); polar_squeeze_1d()
    level_curves_2d(); level_curves_3d()
