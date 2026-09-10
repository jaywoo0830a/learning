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
    ("9b-01-line-forms", "9b", "01", "line-forms"),
    ("9b-02-step-line-forms", "9b", "02", "step-line-forms"),
    ("9b-03-parallel-perpendicular", "9b", "03", "parallel-perpendicular"),
    ("9b-04-angle-between-lines", "9b", "04", "angle-between-lines"),
    ("9b-05-midpoint-division", "9b", "05", "midpoint-division"),
    ("9b-06-point-line-distance", "9b", "06", "point-line-distance"),
    ("9b-07-step-distance-line", "9b", "07", "step-distance-line"),
    ("9b-08-two-lines-distance", "9b", "08", "two-lines-distance"),
    ("9b-09-point-circle-distance", "9b", "09", "point-circle-distance"),
    ("9b-10-tangent-lines-circle", "9b", "10", "tangent-lines-circle"),
    ("9b-11-circle-details", "9b", "11", "circle-details"),
    ("9b-12-step-conic-circle", "9b", "12", "step-conic-circle"),
    ("9b-13-ellipse-details", "9b", "13", "ellipse-details"),
    ("9b-14-step-conic-ellipse", "9b", "14", "step-conic-ellipse"),
    ("9b-15-parabola-details", "9b", "15", "parabola-details"),
    ("9b-16-step-conic-parabola", "9b", "16", "step-conic-parabola"),
    ("9b-17-hyperbola-details", "9b", "17", "hyperbola-details"),
    ("9b-18-step-conic-hyperbola", "9b", "18", "step-conic-hyperbola"),
    ("9b-19-conic-identification", "9b", "19", "conic-identification"),
    ("9b-20-conic-comparison", "9b", "20", "conic-comparison"),
    ("9b-21-parametric-motion", "9b", "21", "parametric-motion"),
    ("9b-22-step-parametric", "9b", "22", "step-parametric"),
    ("9b-23-triangle-area", "9b", "23", "triangle-area"),
    ("9b-24-area-polygon", "9b", "24", "area-polygon"),
    ("9b-25-point-reflection", "9b", "25", "point-reflection"),
]

# All `_KNOWN` entries are 4-tuples (gid, session, num, slug) -> canonical path.
_GRAPH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "graphs"))


def _resolve(gid, session, num, slug):
    del gid
    return _graph_path(session, num, slug)


KNOWN_GRAPHS = {gid: _resolve(gid, session, num, slug)
                for gid, session, num, slug in _KNOWN}

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