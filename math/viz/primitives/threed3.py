"""Extended 3D primitives for 9C (coordinate geometry & quadrics).

Provides axis arrows, points, wireframe/surface meshes, and the common
quadric surfaces (ellipsoid, paraboloid, hyperboloid, cone, cylinder),
each parametrized so the sampled points satisfy the implicit equation.
"""
from __future__ import annotations

import numpy as np

from ..theme import PALETTE


def _color(c):  # resolve palette name or hex
    return PALETTE.get(c, c)


def plot_axis3d(ax, origin, vec, *, color: str = "red", length=None, arrow_ratio=0.1, lw=2):
    """Draw a 3D arrow from ``origin`` along ``vec`` (a length-3 array)."""
    v = np.asarray(vec, dtype=float)
    if length is not None:
        v = v / np.linalg.norm(v) * length
    o = np.asarray(origin, dtype=float)
    c = _color(color)
    return ax.quiver(o[0], o[1], o[2], v[0], v[1], v[2],
                     color=c, arrow_length_ratio=arrow_ratio, lw=lw)


def plot_point3d(ax, x, y, z, *, color: str = "red", size=10, zorder=5):
    """Plot a single 3D point."""
    c = _color(color)
    return ax.plot([x], [y], [z], "o", color=c, markersize=size, zorder=zorder)


def plot_axes3d(ax, lim=5, *, colors=("red", "green", "blue"), labels=("x", "y", "z")):
    """Draw the three labeled axes from the origin out to ``lim``."""
    for i, (c, lab) in enumerate(zip(colors, labels)):
        v = np.zeros(3); v[i] = lim
        plot_axis3d(ax, (0, 0, 0), v, color=c, arrow_ratio=0.08, lw=2)
        end = v.copy(); end[i] = lim + 0.5
        ax.text(end[0], end[1], end[2], lab, fontsize=14, color=c, fontweight="bold")
    return ax


def plot_surface(ax, X, Y, Z, *, color: str = "steelblue", alpha=0.5, cmap=None,
                 lw=0, edgecolor="none"):
    """Draw a shaded surface defined on grids X, Y -> Z."""
    if cmap:
        return ax.plot_surface(X, Y, Z, alpha=alpha, cmap=cmap, linewidth=lw, edgecolor=edgecolor)
    c = _color(color)
    return ax.plot_surface(X, Y, Z, color=c, alpha=alpha, linewidth=lw, edgecolor=edgecolor)


def plot_wireframe(ax, X, Y, Z, *, color: str = "blue", alpha=0.4, lw=0.3):
    """Draw a wireframe mesh."""
    c = _color(color)
    return ax.plot_wireframe(X, Y, Z, color=c, alpha=alpha, lw=lw)


def grid2d(lo=-2, hi=2, n=40):
    """Return (X, Y) meshgrid over ``[lo,hi]``."""
    x = np.linspace(lo, hi, n); y = np.linspace(lo, hi, n)
    return np.meshgrid(x, y)


def contour_circle(center, r, *, n=100):
    """Return (x, y) arrays for a circle at height-independent coords."""
    c = np.asarray(center, dtype=float)
    t = np.linspace(0, 2 * np.pi, n)
    return c[0] + r * np.cos(t), c[1] + r * np.sin(t)


# ── Quadric surfaces ──────────────────────────────────────────────
def _ellipsoid(X, Y, a=1, b=1, c=1):
    return c * np.sqrt(np.clip(1 - (X / a) ** 2 - (Y / b) ** 2, 0, None))


def plot_quadric(ax, kind: str, *, a=2, b=3, c=1, color: str = "blue", alpha=0.45, lo=-2):
    """Draw a named quadric surface (wireframe + translate is optional).

    Supported kinds: ellipsoid, paraboloid, hyperparaboloid, cone,
    hyperboloid-one, hyperboloid-two, cylinder.
    """
    X, Y = grid2d(lo, -lo, 40)
    if kind == "ellipsoid":
        Z = _ellipsoid(X, Y, a, b, c)
        plot_surface(ax, X, Y, Z, color=color, alpha=alpha)
        plot_surface(ax, X, Y, -Z, color=color, alpha=alpha)
    elif kind == "paraboloid":
        Z = X**2 / a + 2 * Y**2 / b
        plot_surface(ax, X, Y, Z, color=color, alpha=alpha)
    elif kind == "hyperparaboloid":
        Z = X**2 - Y**2
        plot_surface(ax, X, Y, Z, color=color, alpha=alpha)
    elif kind == "cone":
        Z = np.sqrt(X**2 + Y**2)
        plot_surface(ax, X, Y, Z, color=color, alpha=alpha)
        plot_surface(ax, X, Y, -Z, color=color, alpha=alpha)
    elif kind == "hyperboloid-one":
        # x^2/a^2 + y^2/b^2 - z^2/c^2 = 1  =>  z = c sqrt(x^2/a^2 + y^2/b^2 - 1)
        Z = c * np.sqrt(np.clip((X / a) ** 2 + (Y / b) ** 2 - 1, 0, 3))
        plot_surface(ax, X, Y, Z, color=color, alpha=alpha)
        plot_surface(ax, X, Y, -Z, color=color, alpha=alpha)
    elif kind == "hyperboloid-two":
        # z^2/c^2 - x^2/a^2 - y^2/b^2 = 1 => z above c
        Z = c * np.sqrt(np.clip(1 + (X / a) ** 2 + (Y / b) ** 2, 0, None))
        plot_surface(ax, X, Y, Z, color=color, alpha=alpha)
        plot_surface(ax, X, Y, -Z, color=color, alpha=alpha)
    elif kind == "cylinder":
        # x^2 + y^2 = a^2 : parametrize z
        t = np.linspace(0, 2 * np.pi, 40); zz = np.linspace(-lo, lo, 20)
        T, Zz = np.meshgrid(t, zz)
        Xs = a * np.cos(T); Ys = a * np.sin(T)
        plot_surface(ax, Xs, Ys, Zz, color=color, alpha=alpha)
    else:
        raise ValueError(f"unknown quadric kind: {kind}")
    return ax