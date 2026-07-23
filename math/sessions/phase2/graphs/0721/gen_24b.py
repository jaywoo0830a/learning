#!/usr/bin/env python3
"""Generate individual graphs for Session 24B."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '24B'

def crit_min():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    ax.plot_surface(X, Y, X**2+Y**2, cmap='viridis', alpha=0.9, shade=True, antialiased=True, edgecolor='none')
    ax.scatter([0], [0], [0], color='red', s=120, zorder=10)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'MIN: $z=x^2+y^2$, $D>0$, $f_{xx}>0$', fontsize=12)
    ax.view_init(25, -60)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/crit-min.png', dpi=DPI); plt.close()
    print('  ✓ crit-min.png')

def crit_saddle():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    ax.plot_surface(X, Y, X**2-Y**2, cmap='coolwarm', alpha=0.9, shade=True, antialiased=True, edgecolor='none')
    ax.scatter([0], [0], [0], color='red', s=120, zorder=10)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'SADDLE: $z=x^2-y^2$, $D<0$', fontsize=12)
    ax.view_init(25, -60)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/crit-saddle.png', dpi=DPI); plt.close()
    print('  ✓ crit-saddle.png')

def crit_max():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    ax.plot_surface(X, Y, -(X**2+Y**2), cmap='plasma', alpha=0.9, shade=True, antialiased=True, edgecolor='none')
    ax.scatter([0], [0], [0], color='red', s=120, zorder=10)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'MAX: $z=-x^2-y^2$, $D>0$, $f_{xx}<0$', fontsize=12)
    ax.view_init(25, -60)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/crit-max.png', dpi=DPI); plt.close()
    print('  ✓ crit-max.png')

def lagrange_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(0, 10, 40), np.linspace(0, 10, 40))
    ax.plot_surface(X, Y, X*Y, cmap='viridis', alpha=0.7, shade=True, antialiased=True, edgecolor='none')
    xc = np.linspace(0, 8, 50)
    ax.plot(xc, 8-xc, xc*(8-xc), 'r-', lw=3, label='x+y=8')
    ax.scatter([4], [4], [16], color='orange', s=200, zorder=10, marker='*')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z=xy', fontsize=12)
    ax.set_title('Lagrange: Maximize xy Subject to x+y=8', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/lagrange-3d.png', dpi=DPI); plt.close()
    print('  ✓ lagrange-3d.png')

def lagrange_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    X, Y = np.meshgrid(np.linspace(0, 10, 40), np.linspace(0, 10, 40))
    cf = ax.contour(X, Y, X*Y, levels=20, cmap='viridis', alpha=0.7, linewidths=1.2)
    ax.clabel(cf, inline=True, fontsize=9)
    ax.plot([0, 8], [8, 0], 'r-', lw=2.5, label='x+y=8')
    ax.scatter(4, 4, color='orange', s=200, zorder=10, marker='*')
    ax.quiver(4, 4, 4, 4, color='green', scale=15, width=0.02, label=r'$\nabla f$')
    ax.quiver(4, 4, 1, 1, color='red', scale=15, width=0.02, label=r'$\nabla g$')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'$\nabla f \parallel \nabla g$ at Optimum $(4,4)$', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/lagrange-2d.png', dpi=DPI); plt.close()
    print('  ✓ lagrange-2d.png')

def lagrange_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    x = np.linspace(0, 8, 200)
    ax.plot(x, x*(8-x), 'b-', lw=2.5)
    ax.scatter([4], [16], color='red', s=120, zorder=5)
    ax.set_xlabel('x (with y=8-x)', fontsize=12); ax.set_ylabel('f = x(8-x)', fontsize=12)
    ax.set_title('Objective Along Constraint — Maximum at x=4', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/lagrange-1d.png', dpi=DPI); plt.close()
    print('  ✓ lagrange-1d.png')

def lagrange_lambda():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    P = np.linspace(10, 22, 100)
    ax.plot(P, P/4, 'b-', lw=2.5)
    ax.scatter([16], [4], color='red', s=120, zorder=5)
    ax.set_xlabel('Constraint value (perimeter P)', fontsize=12)
    ax.set_ylabel(r'Max area / $\lambda$', fontsize=12)
    ax.set_title(r'$\lambda$ = Shadow Price = $d(\max f)/dc$', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/lagrange-lambda.png', dpi=DPI); plt.close()
    print('  ✓ lagrange-lambda.png')

if __name__ == '__main__':
    crit_min(); crit_saddle(); crit_max()
    lagrange_3d(); lagrange_2d(); lagrange_1d(); lagrange_lambda()
