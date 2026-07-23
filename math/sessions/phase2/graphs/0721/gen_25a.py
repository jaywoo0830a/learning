#!/usr/bin/env python3
"""Generate individual graphs for Session 25A."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '25A'

def fubini_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(0, 1, 30), np.linspace(0, 1, 30))
    Z = np.exp(X**2)
    mask = Y <= X
    Z[~mask] = np.nan
    ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.9, shade=True, antialiased=True, edgecolor='none')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'Volume under $e^{x^2}$ over Triangle Region', fontsize=12)
    ax.view_init(25, -60)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/fubini-3d.png', dpi=DPI); plt.close()
    print('  ✓ fubini-3d.png')

def fubini_type1():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    x = np.linspace(0, 1, 200)
    ax.fill_between(x, 0, x, alpha=0.3, color='blue', label=r'$0\leq y\leq x$')
    for xi in [0.2, 0.5, 0.8]:
        ax.plot([xi, xi], [0, xi], 'r-', lw=2)
    ax.set_xlim(0, 1.2); ax.set_ylim(0, 1.2)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'Type I: $\int_0^1\int_0^x f\,dy\,dx$ (Vertical Strips)', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/fubini-type1.png', dpi=DPI); plt.close()
    print('  ✓ fubini-type1.png')

def fubini_type2():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    y = np.linspace(0, 1, 200)
    ax.fill_betweenx(y, y, 1, alpha=0.3, color='green', label=r'$y\leq x\leq 1$')
    for yi in [0.2, 0.5, 0.8]:
        ax.plot([yi, 1], [yi, yi], 'r-', lw=2)
    ax.set_xlim(0, 1.2); ax.set_ylim(0, 1.2)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'Type II: $\int_0^1\int_y^1 f\,dx\,dy$ (Horizontal Strips)', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/fubini-type2.png', dpi=DPI); plt.close()
    print('  ✓ fubini-type2.png')

def fubini_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    x = np.linspace(0, 1, 100)
    ax.plot(x, x*np.exp(x**2), 'b-', lw=2.5, label=r'$x e^{x^2}$ (after $\int_0^x dy$)')
    ax.fill_between(x, 0, x*np.exp(x**2), alpha=0.3)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('Integrand', fontsize=12)
    ax.set_title(r'After Inner Integral: $\int_0^x e^{x^2}dy = x e^{x^2}$', fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/fubini-1d.png', dpi=DPI); plt.close()
    print('  ✓ fubini-1d.png')

if __name__ == '__main__':
    fubini_3d(); fubini_type1(); fubini_type2(); fubini_1d()
