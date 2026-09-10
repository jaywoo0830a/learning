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
]

# graph id -> absolute png path (canonical filenames via graph_path).
KNOWN_GRAPHS = {
    gid: _graph_path(session, gnum, slug)
    for gid, session, gnum, slug in _KNOWN
}

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