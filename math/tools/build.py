"""One-command build: regenerate graphs, then render markdown with them.

Usage (inside the container):
    python tools/build.py [--all]

Steps:
  1. (re)generate every registered graph into the git-ignored graphs/ tree,
  2. render each session markdown: read the committed source (which uses pure
     {{graph:<id>}} placeholders), substitute the built graph paths, and write
     the resolved result under build/rendered/ — leaving the source untouched.

The committed markdown stays pure text + KaTeX; PNGs and build/ are artifacts.
The set of graphs we build is not listed here — it comes straight from
``viz.registry`` (the single source of truth), so adding a graph = one
``@graph(...)`` decorator and nothing else.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Session markdown sources (relative to repo) we render.
MARKDOWN_FILES = [
    "sessions/phase2/14D-relation-lens.md",
    "sessions/phase2/14D1-derivative-interpretation.md",
    "sessions/phase2/9B-2d-functions-geometry.md",
]

RENDER_DIR = os.path.join(REPO, "build", "rendered")


def generate_graphs() -> dict:
    """Rebuild every registered graph; return {id: abs_png_path}.

    Each registered builder returns ``(fig, facts, checks)``; the exporter
    writes it to the canonical path owned by the registry.  ``facts`` (exact
    values) and ``checks`` (verifiable claims) are printed for the log.
    """
    import matplotlib
    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt

    from tools.build_markdown import image_path_for
    from viz.export import save_figure
    from viz.registry import specs

    # Import the spec modules (registers every @graph builder into the registry).
    import scripts.graphs.spec_14d_relations  # noqa: F401
    import scripts.graphs.spec_14d1a           # noqa: F401
    import scripts.graphs.spec_9b              # noqa: F401

    out = {}
    for gid, gspec in sorted(specs().items()):
        fig, facts, _checks, _ = gspec.run()
        out[gid] = image_path_for(gid)
        save_figure(fig, out[gid])
        plt.close(fig)
        print(f"[build] {gid} -> {out[gid]}  facts={facts}")
    return out


def render_markdown() -> list:
    """Render each source md into build/rendered/. Returns list of written paths."""
    from tools.build_markdown import render_text

    os.makedirs(RENDER_DIR, exist_ok=True)
    written = []
    for rel in MARKDOWN_FILES:
        src = os.path.join(REPO, rel)
        if not os.path.exists(src):
            continue
        with open(src, encoding="utf-8") as fh:
            text = fh.read()
        out = os.path.join(RENDER_DIR, os.path.basename(rel))
        resolved = render_text(text, out)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(resolved)
        written.append(out)
        print(f"[md] rendered {rel} -> {out}")
    return written


def main(argv=None):
    argv = argv or sys.argv[1:]
    generate_graphs()
    render_markdown()
    print("build complete")


if __name__ == "__main__":
    main()