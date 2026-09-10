"""Reusable visual primitives that compose into session graphs.

Each primitive is a thin, consistent wrapper around matplotlib artists:
- curve: parametric / x-y curves, tangent segments, and points.
- annotate: called-out labels with arrows.
(Schematics, filled regions, and 3D / vector-field primitives come next.)
"""
from .curve import plot_curve, plot_tangent, plot_point
from .annotate import add_callout

__all__ = ["plot_curve", "plot_tangent", "plot_point", "add_callout"]