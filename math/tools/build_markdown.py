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

# Graph id -> canonical output path, derived from the single registry.
# Importing the spec modules runs their ``@graph`` decorators, populating
# ``viz.registry``.  Keeping that import here means this module works both on
# its own (tests) and from the build pipeline.
from viz.registry import specs as _registry_specs
from scripts.graphs import spec_14d_relations  # noqa: F401  (register)
from scripts.graphs import spec_14d1a           # noqa: F401  (register)
from scripts.graphs import spec_9b              # noqa: F401  (register)

# Every registered graph maps to a canonical <GRAPH_ROOT>/<session>/<nn>-<slug>.png
KNOWN_GRAPHS = {gid: s.path for gid, s in _registry_specs().items()}

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