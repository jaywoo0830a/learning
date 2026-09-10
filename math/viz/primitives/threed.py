"""3D primitives (sphere shells) needed by geometry interpretations (d5 sphere)."""
from __future__ import annotations

import numpy as np

from ..theme import PALETTE


def _sphere_grid(n=60):
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)
    return u, v


def plot_shell_3d(ax, R: float, dr: float, *, inner_color: str = "blue",
                  outer_color: str = "amber", inner_alpha: float = 0.12,
                  outer_alpha: float = 0.25):
    """Draw a sphere of radius ``R`` plus a translucent outer shell to ``R+dr``.

    Returns None; draws directly on the 3D axis ``ax``. This visualizes
    ``dV/dr = 4 pi r^2`` (the thin shell wraps the sphere).
    """
    u, v = _sphere_grid()

    def shell(rad, col, alpha):
        col_c = PALETTE.get(col, col)
        xs = rad * np.outer(np.cos(u), np.sin(v))
        ys = rad * np.outer(np.sin(u), np.sin(v))
        zs = rad * np.outer(np.ones_like(u), np.cos(v))
        ax.plot_surface(xs, ys, zs, color=col_c, alpha=alpha, linewidth=0)
        ax.plot_wireframe(xs[::6, ::6], ys[::6, ::6], zs[::6, ::6],
                          color=col_c, lw=0.4, alpha=0.8)

    shell(R, inner_color, inner_alpha)
    shell(R + dr, outer_color, outer_alpha)