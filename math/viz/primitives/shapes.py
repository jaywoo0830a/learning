"""Shape primitives: shaded regions, filled circles, and ring (annulus) patches.

Adds the 2D "area" vocabulary needed by economics/geometry session graphs
(d2 motion regions, d4 circle rings) while staying consistent with the shared
palette and style.
"""
from __future__ import annotations

from typing import Optional

import numpy as np
from matplotlib.patches import Circle, Wedge

from ..theme import PALETTE


def plot_region(ax, x, y, *, baseline=0.0, where=None, color: str = "blue", alpha: float = 0.15):
    """Shade the region between ``y`` and ``baseline`` over ``x``, optionally only
    where ``where`` is True. Returns the PolyCollection (or None)."""
    c = PALETTE.get(color, color)
    if where is None:
        where = np.ones_like(x, dtype=bool)
    return ax.fill_between(x, baseline, y, where=where, color=c, alpha=alpha)


def plot_circle(ax, cx, cy, r, *, color: str = "blue", alpha: float = 0.18, ec: bool = True, lw: float = 2.5):
    """Draw a filled circle of radius ``r`` centered at ``(cx, cy)``. Returns the Circle."""
    c = PALETTE.get(color, color)
    return ax.add_patch(
        Circle((cx, cy), r, fill=True, fc=c, alpha=alpha, ec=c if ec else "none", lw=lw)
    )


def plot_ring(ax, cx, cy, r, width, *, color: str = "amber", alpha: float = 0.45, lw: float = 1.5):
    """Draw a ring (annulus) of inner radius ``r`` and thickness ``width``. Returns the Wedge.

    Represents e.g. the area element ``2 pi r dr`` around a circle.
    """
    c = PALETTE.get(color, color)
    return ax.add_patch(
        Wedge((cx, cy), r + width, 0, 360, width=width, fc=c, alpha=alpha, ec=c, lw=lw)
    )