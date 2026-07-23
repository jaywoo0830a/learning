#!/usr/bin/env python3
"""Generate individual graphs for Session 23B."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

DPI = 150
OUT_DIR = '23B'

def gradient_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-3, 3, 40), np.linspace(-3, 3, 40))
    Z = X**2 + Y**2
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, shade=True, antialiased=True, edgecolor='none')
    skip = 5
    Xs, Ys = X[::skip,::skip], Y[::skip,::skip]
    ax.quiver(Xs, Ys, Z[::skip,::skip], 2*Xs, 2*Ys, np.zeros_like(Xs),
              length=0.5, color='red', alpha=0.6, normalize=True)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'Surface $z=x^2+y^2$ with Gradient Vectors', fontsize=12)
    ax.view_init(25, -60)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/gradient-3d.png', dpi=DPI); plt.close()
    print('  ✓ gradient-3d.png')

def gradient_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    X, Y = np.meshgrid(np.linspace(-3, 3, 40), np.linspace(-3, 3, 40))
    Z = X**2 + Y**2
    cf = ax.contour(X, Y, Z, levels=12, colors='blue', alpha=0.6, linewidths=1.5)
    ax.clabel(cf, inline=True, fontsize=9)
    Xq, Yq = np.meshgrid(np.linspace(-2.5, 2.5, 7), np.linspace(-2.5, 2.5, 7))
    ax.quiver(Xq, Yq, 2*Xq, 2*Yq, color='red', alpha=0.8, width=0.005, scale=8, label=r'$\nabla f$')
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title(r'$\nabla f$ Perpendicular to Level Curves', fontsize=12)
    ax.set_aspect('equal'); ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/gradient-2d.png', dpi=DPI); plt.close()
    print('  ✓ gradient-2d.png')

def gradient_1d():
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    th = np.linspace(0, 2*np.pi, 100)
    ax.plot(th, 2*np.sqrt(5)*np.cos(th), 'b-', lw=2.5, label=r'$D_{\vec{u}}f = |\nabla f|\cos\theta$')
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', ls=':', lw=1, alpha=0.5)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    ax.set_xlabel(r'Angle $\theta$ from $\nabla f$', fontsize=12)
    ax.set_ylabel(r'$D_{\vec{u}}f$', fontsize=12)
    ax.set_title(r'Directional Derivative = Dot Product $\nabla f\cdot\vec{u}$', fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/gradient-1d.png', dpi=DPI); plt.close()
    print('  ✓ gradient-1d.png')

def tangent_plane_3d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.linspace(-1, 3, 40), np.linspace(0, 3, 40))
    Z = X**2 + Y**2
    Zt = 2*X + 4*Y - 5
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, shade=True, antialiased=True, edgecolor='none')
    ax.plot_surface(X, Y, Zt, color='orange', alpha=0.5, shade=False, edgecolor='none')
    ax.scatter([1], [2], [5], color='red', s=120, zorder=10)
    ax.quiver(1, 2, 5, 2, 4, 0, color='green', length=0.5, normalize=True, lw=2, label=r'$\nabla f$')
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12); ax.set_zlabel('z', fontsize=12)
    ax.set_title(r'Tangent Plane at $(1,2,5)$ to $z=x^2+y^2$', fontsize=12)
    ax.view_init(25, -60); ax.legend(fontsize=10)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/tangent-plane-3d.png', dpi=DPI); plt.close()
    print('  ✓ tangent-plane-3d.png')

def tangent_plane_2d():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    X, Y = np.meshgrid(np.linspace(0.5, 1.5, 10), np.linspace(1.5, 2.5, 10))
    cf = ax.contour(X, Y, X**2 + Y**2, levels=8, colors='blue', alpha=0.6, linewidths=1.5)
    ax.clabel(cf, inline=True, fontsize=9)
    ax.scatter(1, 2, color='red', s=100, zorder=5)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)
    ax.set_title('Zoom Near Tangent Point — Linear Approximation', fontsize=12)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{OUT_DIR}/tangent-plane-2d.png', dpi=DPI); plt.close()
    print('  ✓ tangent-plane-2d.png')

if __name__ == '__main__':
    gradient_3d(); gradient_2d(); gradient_1d()
    tangent_plane_3d(); tangent_plane_2d()
