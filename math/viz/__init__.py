"""Shared rendering core for the math viz pipeline.

A single place that owns visual identity (colors, sizes, backend), canvas
creation with sane layout defaults, export helpers, the graph registry (the one
source of truth for graph ids / canonical paths), and a thin chainable graph
builder — so that graphs produced across sessions look consistent, are placed
at canonical paths, and bring their verifiable facts/checks with them.

Public API:
- theme: PALETTE, DPI, FONTS, apply_matplotlib_defaults()
- canvas: new_canvas(), simple_axes(), subplots_canvas(), new_axes3d()
- export: save_figure(), graph_path(), GRAPH_ROOT
- registry: graph(), specs(), spec(), paths(), build_all()
- graph: G  (chainable single-axes builder collecting facts + checks)
"""
from .theme import PALETTE, DPI, FONTS, apply_matplotlib_defaults
from .canvas import new_canvas, simple_axes, subplots_canvas, new_axes3d
from .export import save_figure, graph_path, GRAPH_ROOT
from .coords import coords_ax, build_and_save
from .registry import graph, specs, spec, paths, build_all, GraphSpec
from .graph import G

__all__ = [
    "PALETTE",
    "DPI",
    "FONTS",
    "apply_matplotlib_defaults",
    "new_canvas",
    "simple_axes",
    "subplots_canvas",
    "new_axes3d",
    "save_figure",
    "graph_path",
    "GRAPH_ROOT",
    "coords_ax",
    "build_and_save",
    "graph",
    "specs",
    "spec",
    "paths",
    "build_all",
    "GraphSpec",
    "G",
]