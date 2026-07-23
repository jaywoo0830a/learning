#!/usr/bin/env python3
"""Generate individual graphs for Session 24A."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '24A'

def chain_path_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    ax.plot_surface(X, Y, X**2+Y**2, cmap='viridis', alpha=0.6, shade=True, antialiased=True, edgecolor='none')
    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(t), np.sin(t), np.ones_like(t), 'r-', lw=3, label=r'$\vec{r}(t)=(\cos t,\sin t)$')
    idx = 15
    ax.quiver(np.cos(t[idx]), np.sin(t[idx]), 1,
              -np.sin(t[idx]), np.cos(t[idx]), 0,
              color='orange', length=0.5, normalize=True, lw=2)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'Parametric Path on $z=x^2+y^2$ (z=1 constant)', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/chain-path-3d.png', dpi=DPI); plt.close()
    print('  ✓ chain-path-3d.png')

def chain_path_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(t), np.sin(t), 'b-', lw=2.5, label=r'$\vec{r}(t)=(\cos t,\sin t)$')
    skip = 10
    for i in range(0, len(t), skip):
        ax.arrow(np.cos(t[i]), np.sin(t[i]), -np.sin(t[i])*0.15, np.cos(t[i])*0.15,
                 head_width=0.05, head_length=0.05, fc='red', ec='red', alpha=0.5)
    ax.scatter([1], [0], color='green', s=80, zorder=5, label='Start t=0')
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title('Path in xy-plane with Tangent Vectors', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/chain-path-2d.png', dpi=DPI); plt.close()
    print('  ✓ chain-path-2d.png')

def chain_tree():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5); ax.axis('off')
    ax.text(2, 4.5, 'z = f(x,y)', fontsize=14, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightblue'))
    ax.text(0.5, 2.5, 'x = g(u,v)', fontsize=12, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen'))
    ax.text(3.5, 2.5, 'y = h(u,v)', fontsize=12, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightgreen'))
    for xu, xv, yu, yv in [(0, 1, 3, 4)]:
        for x, lbl in [(0, 'u'), (1, 'v')]:
            ax.text(x, 0.5, lbl, fontsize=12, ha='center',
                    bbox=dict(boxstyle='circle', facecolor='wheat'))
        for x, lbl in [(3, 'u'), (4, 'v')]:
            ax.text(x, 0.5, lbl, fontsize=12, ha='center',
                    bbox=dict(boxstyle='circle', facecolor='wheat'))
    ax.plot([2, 0.5], [4.2, 2.8], 'k-', lw=1.5)
    ax.plot([2, 3.5], [4.2, 2.8], 'k-', lw=1.5)
    ax.plot([0.5, 0], [2.2, 0.8], 'k-', lw=1.5)
    ax.plot([0.5, 1], [2.2, 0.8], 'k-', lw=1.5)
    ax.plot([3.5, 3], [2.2, 0.8], 'k-', lw=1.5)
    ax.plot([3.5, 4], [2.2, 0.8], 'k-', lw=1.5)
    ax.text(1.2, 3.6, 'f_x', fontsize=10, color='red')
    ax.text(2.8, 3.6, 'f_y', fontsize=10, color='blue')
    ax.text(0.3, 1.6, 'x_u', fontsize=10, color='red')
    ax.text(0.8, 1.6, 'x_v', fontsize=10, color='red')
    ax.text(3.4, 1.6, 'y_u', fontsize=10, color='blue')
    ax.text(3.9, 1.6, 'y_v', fontsize=10, color='blue')
    ax.set_title('Chain Rule Tree Diagram — Sum Over All Paths', fontsize=12)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/chain-tree.png', dpi=DPI); plt.close()
    print('  ✓ chain-tree.png')

def chain_dzdt():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(t, np.zeros_like(t), 'b-', lw=2.5)
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(-1, 1)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    ax.set_xlabel('t', fontsize=12); ax.set_ylabel('dz/dt', fontsize=12)
    ax.set_title(r'$dz/dt = \nabla f \cdot \vec{r}\,''(t) = 0$ (constant on circle)', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/chain-dzdt.png', dpi=DPI); plt.close()
    print('  ✓ chain-dzdt.png')

def implicit_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2*np.pi, 40); v = np.linspace(0, np.pi, 40)
    U, V = np.meshgrid(u, v); R = np.sqrt(14)
    ax.plot_surface(R*np.cos(U)*np.sin(V), R*np.sin(U)*np.sin(V), R*np.cos(V),
                    cmap='viridis', alpha=0.7, shade=True, antialiased=True, edgecolor='none')
    xr = np.linspace(-1, 3, 10); yr = np.linspace(0, 4, 10)
    Xp, Yp = np.meshgrid(xr, yr)
    ax.plot_surface(Xp, Yp, (14-Xp-2*Yp)/3, color='orange', alpha=0.5, shade=False, edgecolor='none')
    ax.scatter([1], [2], [3], color='red', s=120, zorder=10)
    ax.quiver(1, 2, 3, 2, 4, 6, color='green', length=1.5, normalize=True, lw=2, label=r'$\nabla F$')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'Sphere $x^2+y^2+z^2=14$ + Tangent Plane at $(1,2,3)$', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/implicit-3d.png', dpi=DPI); plt.close()
    print('  ✓ implicit-3d.png')

def implicit_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    x = np.linspace(-4, 4, 200); y = np.linspace(-4, 4, 200); X, Y = np.meshgrid(x, y)
    cf = ax.contour(X, Y, X**2+Y**2+9, levels=[14], colors='blue', linewidths=2)
    ax.clabel(cf, inline=True, fontsize=10, fmt='%d')
    ax.scatter(1, 2, color='red', s=100, zorder=5)
    ax.quiver(1, 2, 2, 4, color='green', scale=8, width=0.01, label=r'$\nabla F$')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'Level Curve $F(x,y,3)=14$ — Implicit Function', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/implicit-2d.png', dpi=DPI); plt.close()
    print('  ✓ implicit-2d.png')

def implicit_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    x = np.linspace(-3, 3, 200)
    z = np.sqrt(10 - x**2)
    ax.plot(x, z, 'b-', lw=2.5, label=r'$z(x)$ on sphere at $y=2$')
    zt = 3 - (x-1)/3
    ax.plot(x, zt, 'r--', lw=2, label=r'$z_x = -F_x/F_z$ tangent')
    ax.scatter([1], [3], color='red', s=100, zorder=5)
    ax.set_xlim(-3, 3); ax.set_ylim(0, 4)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('z', fontsize=12)
    ax.set_title(r'Implicit Differentiation: $\partial z/\partial x = -F_x/F_z$', fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/implicit-1d.png', dpi=DPI); plt.close()
    print('  ✓ implicit-1d.png')

if __name__ == '__main__':
    chain_path_3d(); chain_path_2d(); chain_tree(); chain_dzdt()
    implicit_3d(); implicit_2d(); implicit_1d()
