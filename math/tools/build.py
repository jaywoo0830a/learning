"""One-command build: regenerate graphs, then render markdown with them.

Usage (inside the container):
    python tools/build.py [--all]

Steps:
  1. (re)generate every registered graph into the git-ignored graphs/ tree,
  2. render each session markdown: read the committed source (which uses pure
     {{graph:<id>}} placeholders), substitute the built graph paths, and write
     the resolved result under build/rendered/ — leaving the source untouched.

The committed markdown stays pure text + KaTeX; PNGs and build/ are artifacts.
"""
from __future__ import annotations

import os
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Registry of graph builders: id -> importable callable string.
BUILDERS = {
    "14d-01-derivative-units": "scripts.graphs.spec_14d_relations.build_d1",
    "14d-02-motion-story": "scripts.graphs.spec_14d_relations.build_d2",
    "14d1-03-linearization": "scripts.graphs.spec_14d_relations.build_d3",
    "14d1-04-circle-ring": "scripts.graphs.spec_14d_relations.build_d4",
    "14d1-05-sphere-shell": "scripts.graphs.spec_14d_relations.build_d5",
    "14d1-06-marginal-cost": "scripts.graphs.spec_14d_relations.build_d6",
    "14d1-07-elasticity": "scripts.graphs.spec_14d_relations.build_d7",
}

# Session markdown sources (relative to repo) we render.
MARKDOWN_FILES = [
    "sessions/phase2/14D-relation-lens.md",
    "sessions/phase2/14D1-derivative-interpretation.md",
]

RENDER_DIR = os.path.join(REPO, "build", "rendered")


def _import(name):
    parts = name.split(".")
    mod = __import__(".".join(parts[:-1]), fromlist=[parts[-1]])
    return getattr(mod, parts[-1])


def generate_graphs() -> dict:
    """Rebuild every graph; return {id: abs_png_path}."""
    import matplotlib
    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt

    from tools.build_markdown import image_path_for
    from viz.export import save_figure

    out = {}
    for gid, builder_ref in BUILDERS.items():
        builder = _import(builder_ref)
        fig, facts, _ = builder()
        save_figure(fig, image_path_for(gid))
        plt.close(fig)
        out[gid] = image_path_for(gid)
        print(f"[build] {gid} -> {out[gid]}  verified={facts}")
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
        resolved = render_text(text, src)
        out = os.path.join(RENDER_DIR, os.path.basename(rel))
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