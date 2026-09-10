"""Callout / annotation primitives.

Consistent annotation for pointing at a location on a graph. Centralizes the
arrow style and text appearance so every session annotates the same way —
reducing the "label overlaps the curve / drifts off the axes" class of bugs.
"""
from __future__ import annotations

from typing import Tuple

from ..theme import PALETTE


def add_callout(
    ax,
    target: Tuple[float, float],
    text: str,
    offset: Tuple[float, float],
    *,
    color: str = "red",
    fontsize: float = 11,
    fontweight: str = "bold",
):
    """Add an annotated arrow pointing at ``target``, text placed at ``offset``.

    ``offset`` is data-space displacement from ``target`` for the label. Returns
    the matplotlib ``Annotation`` so callers / tests can inspect or move it.
    """
    c = PALETTE.get(color, color)
    return ax.annotate(
        text,
        xy=target,
        xytext=(target[0] + offset[0], target[1] + offset[1]),
        fontsize=fontsize,
        color=c,
        fontweight=fontweight,
        arrowprops=dict(arrowstyle="->", color=c, lw=1.2),
    )