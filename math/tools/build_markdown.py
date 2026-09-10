"""Markdown build tool: keep session markdown pure text + KaTeX.

Session files (the committed source) reference graphs only through
``{{graph:<id>}}`` placeholders. At build time this tool rewrites each
placeholder to a path relative to a target markdown — writing the resolved
text to a *rendered* output (never mutating the source .md), so the committed
document stays pure text + KaTeX and PNGs stay git-ignored build artifacts.
"""
from __future__ import annotations

import os
import re

# Registry: graph id -> (session dir, absolute png path).
# Built from viz.export.graph_path so filenames are canonical.
from viz.export import graph_path as _graph_path

_KNOWN = [
    ("14d-01-derivative-units", "14d", "01", "derivative-units"),
    ("14d-02-motion-story", "14d", "02", "motion-story"),
    ("14d1-03-linearization", "14d1", "03", "linearization"),
    ("14d1-04-circle-ring", "14d1", "04", "circle-ring"),
    ("14d1-05-sphere-shell", "14d1", "05", "sphere-shell"),
    ("14d1-06-marginal-cost", "14d1", "06", "marginal-cost"),
    ("14d1-07-elasticity", "14d1", "07", "elasticity"),
    ("9b-angle-between-lines", "9b", "angle-between-lines"),
    ("9b-area-polygon", "9b", "area-polygon"),
    ("9b-circle-details", "9b", "circle-details"),
    ("9b-conic-comparison", "9b", "conic-comparison"),
    ("9b-conic-identification", "9b", "conic-identification"),
    ("9b-ellipse-details", "9b", "ellipse-details"),
    ("9b-hyperbola-details", "9b", "hyperbola-details"),
    ("9b-line-forms", "9b", "line-forms"),
    ("9b-midpoint-division", "9b", "midpoint-division"),
    ("9b-parabola-details", "9b", "parabola-details"),
    ("9b-parallel-perpendicular", "9b", "parallel-perpendicular"),
    ("9b-parametric-motion", "9b", "parametric-motion"),
    ("9b-point-circle-distance", "9b", "point-circle-distance"),
    ("9b-point-line-distance-derivation", "9b", "point-line-distance-derivation"),
    ("9b-point-reflection", "9b", "point-reflection"),
    ("9b-step-conic-circle", "9b", "step-conic-circle"),
    ("9b-step-conic-ellipse", "9b", "step-conic-ellipse"),
    ("9b-step-conic-hyperbola", "9b", "step-conic-hyperbola"),
    ("9b-step-conic-parabola", "9b", "step-conic-parabola"),
    ("9b-step-distance-line", "9b", "step-distance-line"),
    ("9b-step-line-forms", "9b", "step-line-forms"),
    ("9b-step-parametric", "9b", "step-parametric"),
    ("9b-tangent-lines-circle", "9b", "tangent-lines-circle"),
    ("9b-triangle-area-coordinates", "9b", "triangle-area-coordinates"),
    ("9b-two-lines-distance", "9b", "two-lines-distance"),
    ("9c-angle-planes", "9c", "angle-planes"),
    ("9c-cone-details", "9c", "cone-details"),
    ("9c-contour-steepness", "9c", "contour-steepness"),
    ("9c-coordinate-system-3d", "9c", "coordinate-system-3d"),
    ("9c-cylinder-types", "9c", "cylinder-types"),
    ("9c-cylinders-intersection", "9c", "cylinders-intersection"),
    ("9c-degenerate-cases", "9c", "degenerate-cases"),
    ("9c-distance-parallel-planes", "9c", "distance-parallel-planes"),
    ("9c-domain-regions", "9c", "domain-regions"),
    ("9c-ellipsoid-details", "9c", "ellipsoid-details"),
    ("9c-hyperbolic-paraboloid-details", "9c", "hyperbolic-paraboloid-details"),
    ("9c-hyperboloid-one-sheet", "9c", "hyperboloid-one-sheet"),
    ("9c-hyperboloid-two-sheets", "9c", "hyperboloid-two-sheets"),
    ("9c-level-curves-method", "9c", "level-curves-method"),
    ("9c-level-curves-to-surface", "9c", "level-curves-to-surface"),
    ("9c-line-surface-intersection", "9c", "line-surface-intersection"),
    ("9c-paraboloid-details", "9c", "paraboloid-details"),
    ("9c-plane-intercept", "9c", "plane-intercept"),
    ("9c-plane-normal", "9c", "plane-normal"),
    ("9c-point-plane-distance", "9c", "point-plane-distance"),
    ("9c-point-sphere-distance", "9c", "point-sphere-distance"),
    ("9c-quadric-comparison", "9c", "quadric-comparison"),
    ("9c-quadric-identification", "9c", "quadric-identification"),
    ("9c-sphere-details", "9c", "sphere-details"),
    ("9c-sphere-plane-intersection", "9c", "sphere-plane-intersection"),
    ("9c-step-3d-coords", "9c", "step-3d-coords"),
    ("9c-step-intersection", "9c", "step-intersection"),
    ("9c-step-level-curves", "9c", "step-level-curves"),
    ("9c-step-plane", "9c", "step-plane"),
    ("9c-step-quadrics", "9c", "step-quadrics"),
    ("9c-step-surface-build", "9c", "step-surface-build"),
    ("9c-step-vectors", "9c", "step-vectors"),
    ("9c-surface-height-map", "9c", "surface-height-map"),
    ("9c-symmetry-3d", "9c", "symmetry-3d"),
    ("9c-vector-dot-cross", "9c", "vector-dot-cross"),
]

# graph id -> absolute png path.
# - 14d entries are 4-tuples (gid, session, num, slug) -> graphs/<s>/<num>-<slug>.png
# - 9x entries are 3-tuples (gid, session, slug)      -> graphs/<s>/<gid>.png
_GRAPH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "graphs"))

def _resolve(gid, session, rest):
    if len(rest) == 2:  # (gnum, slug)
        gnum, slug = rest
        return _graph_path(session, gnum, slug)
    slug = rest[0]      # (slug,) -> flat file named <gid>.png
    return os.path.join(_GRAPH_ROOT, session, gid + ".png")

KNOWN_GRAPHS = {gid: _resolve(gid, session, rest)
                for gid, session, *rest in _KNOWN}

# Matches {{graph:any-chars-here}}
_REF = re.compile(r"\{\{graph:([^}]+)\}\}")


def find_graph_refs(markdown: str) -> list:
    """Return the list of graph ids referenced via {{graph:id}} in ``markdown``."""
    return _REF.findall(markdown)


def image_path_for(gid: str) -> str:
    """Return the absolute path for a known graph id (raises KeyError if unknown)."""
    try:
        return KNOWN_GRAPHS[gid]
    except KeyError:
        raise KeyError(f"unknown graph id: {gid!r}; add it to KNOWN_GRAPHS")


def resolve_image_path(md_path: str, img_abs: str) -> str:
    """Return the path to ``img_abs`` relative to the markdown file's directory."""
    return os.path.relpath(img_abs, os.path.dirname(md_path))


def render_text(markdown: str, md_path: str) -> str:
    """Replace every {{graph:id}} placeholder in ``markdown`` with a relative path."""
    def _sub(m):
        gid = m.group(1)
        return resolve_image_path(md_path, image_path_for(gid))
    return _REF.sub(_sub, markdown)


def render_to_text(md_path: str) -> str:
    """Read source md at ``md_path`` and return the resolved (unwritten) text."""
    with open(md_path, encoding="utf-8") as fh:
        return render_text(fh.read(), md_path)