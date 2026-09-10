"""Canvas creation with consistent layout defaults.

The idea: a session requests a figure via these helpers instead of calling
``plt.subplots`` directly, so that sizing, tight layout, and (later) z-order /
equal-aspect policies live in one place and every graph inherits them.
"""
from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt

from .theme import apply_matplotlib_defaults


def new_canvas(size: Optional[Tuple[float, float]] = None):
    """Return ``(fig, ax)`` for a single-axis figure with canonical defaults.

    ``size`` is a ``(width_inches, height_inches)`` tuple; defaults to a
    reasonable 8x5 portrait when omitted. Ensures matplotlib defaults are
    applied exactly once before creation.
    """
    apply_matplotlib_defaults()
    w, h = size if size is not None else (8.0, 5.0)
    fig, ax = plt.subplots(figsize=(w, h))
    return fig, ax


def subplots_canvas(rows: int, cols: int, *, size: Optional[Tuple[float, float]] = None,
                    projection: Optional[str] = None):
    """Return ``(fig, axes)`` for an ``rows x cols`` grid of subplots.

    ``size`` is figure size inches. ``projection`` (e.g. '3d') may be passed
    to apply to every subplot. Returns the ndarray of axes like ``plt.subplots``.
    """
    apply_matplotlib_defaults()
    w, h = size if size is not None else (8.0, 5.0)
    fig, axes = plt.subplots(rows, cols, figsize=(w, h), subplot_kw={"projection": projection} if projection else None)
    return fig, np.atleast_2d(axes)


def new_axes3d(fig):
    """Add a single 3D axis to ``fig`` (headless-safe)."""
    return fig.add_subplot(111, projection="3d")


def simple_axes(ax, *, grid: bool = False, equal_aspect: bool = False) -> None:
    """Apply the canonical axis styling used by most session graphs."""
    if grid:
        ax.grid(True, alpha=0.15, lw=0.4)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    if equal_aspect:
        ax.set_aspect("equal")