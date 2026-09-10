"""Grid & origin-axes primitives.

Reusable helpers for drawing cartesian grids and axis lines consistently
across coordinate-geometry graphs (sessions 9B/9C).
"""
from __future__ import annotations

import matplotlib.pyplot as plt

from ..theme import PALETTE


def xaxis(ax, *, color: str = "gray", lw=0.6, zorder=0):
    """Draw the horizontal (x) axis through origin as a light line."""
    c = PALETTE.get(color, color)
    return ax.axhline(0, color=c, lw=lw, zorder=zorder)


def yaxis(ax, *, color: str = "gray", lw=0.6, zorder=0):
    """Draw the vertical (y) axis through origin as a light line."""
    c = PALETTE.get(color, color)
    return ax.axvline(0, color=c, lw=lw, zorder=zorder)


def origin_axes(ax, *, color: str = "gray", lw=0.6, grid_alpha=0.3):
    """Draw both origin axes and a light grid."""
    xaxis(ax, color=color, lw=lw)
    yaxis(ax, color=color, lw=lw)
    light_grid(ax, alpha=grid_alpha)
    return ax


def light_grid(ax, *, alpha=0.3, lw=0.4):
    """Enable a faint grid (commonly used in coordinate graphs)."""
    ax.grid(True, alpha=alpha, lw=lw)
    return ax


def set_limits(ax, xlo, xhi, ylo, yhi):
    """Set x and y limits in one call."""
    ax.set_xlim(xlo, xhi)
    ax.set_ylim(ylo, yhi)
    return ax


def equal_aspect(ax):
    """Force equal aspect (true shape) — important for circle/geometry."""
    ax.set_aspect("equal")
    return ax