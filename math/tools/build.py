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
    "9b-01-line-forms": "scripts.graphs.spec_9b.build_line_forms",
    "9b-02-step-line-forms": "scripts.graphs.spec_9b.build_step_line_forms",
    "9b-03-parallel-perpendicular": "scripts.graphs.spec_9b.build_parallel_perpendicular",
    "9b-04-angle-between-lines": "scripts.graphs.spec_9b.build_angle_between_lines",
    "9b-05-midpoint-division": "scripts.graphs.spec_9b.build_midpoint_division",
    "9b-06-point-line-distance": "scripts.graphs.spec_9b.build_point_line_distance",
    "9b-07-step-distance-line": "scripts.graphs.spec_9b.build_step_distance_line",
    "9b-08-two-lines-distance": "scripts.graphs.spec_9b.build_two_lines_distance",
    "9b-09-point-circle-distance": "scripts.graphs.spec_9b.build_point_circle_distance",
    "9b-10-tangent-lines-circle": "scripts.graphs.spec_9b.build_tangent_lines_circle",
    "9b-11-circle-details": "scripts.graphs.spec_9b.build_circle_details",
    "9b-12-step-conic-circle": "scripts.graphs.spec_9b.build_step_conic_circle",
    "9b-13-ellipse-details": "scripts.graphs.spec_9b.build_ellipse_details",
    "9b-14-step-conic-ellipse": "scripts.graphs.spec_9b.build_step_conic_ellipse",
    "9b-15-parabola-details": "scripts.graphs.spec_9b.build_parabola_details",
    "9b-16-step-conic-parabola": "scripts.graphs.spec_9b.build_step_conic_parabola",
    "9b-17-hyperbola-details": "scripts.graphs.spec_9b.build_hyperbola_details",
    "9b-18-step-conic-hyperbola": "scripts.graphs.spec_9b.build_step_conic_hyperbola",
    "9b-19-conic-identification": "scripts.graphs.spec_9b.build_conic_identification",
    "9b-20-conic-comparison": "scripts.graphs.spec_9b.build_conic_comparison",
    "9b-21-parametric-motion": "scripts.graphs.spec_9b.build_parametric_motion",
    "9b-22-step-parametric": "scripts.graphs.spec_9b.build_step_parametric",
    "9b-23-triangle-area": "scripts.graphs.spec_9b.build_triangle_area",
    "9b-24-area-polygon": "scripts.graphs.spec_9b.build_area_polygon",
    "9b-25-point-reflection": "scripts.graphs.spec_9b.build_point_reflection",
}

# Session markdown sources (relative to repo) we render.
MARKDOWN_FILES = [
    "sessions/phase2/14D-relation-lens.md",
    "sessions/phase2/14D1-derivative-interpretation.md",
    "sessions/phase2/9B-2d-functions-geometry.md",
]

RENDER_DIR = os.path.join(REPO, "build", "rendered")


def _import(name):
    parts = name.split(".")
    mod = __import__(".".join(parts[:-1]), fromlist=[parts[-1]])
    return getattr(mod, parts[-1])


def generate_graphs() -> dict:
    """Rebuild every graph; return {id: abs_png_path}.

    Individual ``(fig, facts, path)`` builders are saved to their canonical
    path; bulk "spec" modules (9b, 9c) write their own graphs in place via a
    ``build_all()`` that routes through the VIZ exporter.
    """
    import matplotlib
    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt

    from tools.build_markdown import image_path_for
    from viz.export import save_figure

    out = {}
    # individual builders (14d + 9b); each returns (fig, facts, path) and draws
    # purely through the shared VIZ primitives.
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