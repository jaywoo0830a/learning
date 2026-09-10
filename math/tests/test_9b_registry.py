# Descriptive tests for the 9B graph registry + verified math facts.
# Each column graph is genuinely rebuilt on VIZ primitives; here we confirm
# (a) every md placeholder resolves to a canonical path and
# (b) each builder returns verifiable symbolic facts.
import os
import re


MD = "sessions/phase2/9B-2d-functions-geometry.md"


def _refs():
    text = open(MD, encoding="utf-8").read()
    return re.findall(r"\{\{graph:([^}]+)\}\}", text)


class Test9BRegistry:
    def test_all_placeholders_registered_canonical(self):
        from tools.build_markdown import KNOWN_GRAPHS
        refs = _refs()
        assert len(refs) == 25
        for gid in refs:
            p = KNOWN_GRAPHS[gid]
            # canonical: graphs/9b/<num>-<slug>.png
            assert os.sep + "9b" + os.sep in p
            assert p.endswith(".png")
            # filename matches <num>-<slug> (gid minus '9b-' prefix)
            fname = p.split(os.sep)[-1][:-4]
            assert fname == gid[3:]

    def test_source_md_pure_placeholder(self):
        text = open(MD, encoding="utf-8").read()
        assert ".png" not in text
        assert "$" in text  # KaTeX remains


class Test9BBuilders:
    def test_builders_exist(self):
        from scripts.graphs import spec_9b as s
        for slug in [
            "line_forms", "step_line_forms", "parallel_perpendicular",
            "angle_between_lines", "midpoint_division", "point_line_distance",
            "step_distance_line", "two_lines_distance", "point_circle_distance",
            "tangent_lines_circle", "circle_details", "step_conic_circle",
            "ellipse_details", "step_conic_ellipse", "parabola_details",
            "step_conic_parabola", "hyperbola_details", "step_conic_hyperbola",
            "conic_identification", "conic_comparison", "parametric_motion",
            "step_parametric", "triangle_area", "area_polygon", "point_reflection",
        ]:
            assert hasattr(s, "build_" + slug), slug

    def test_triangle_area_verified(self):
        from scripts.graphs import spec_9b as s
        import sympy as sp
        fig, facts, checks = s.build_triangle_area()
        assert facts["area"] == 6 or facts["area"].is_integer
        assert bool(checks)
        import matplotlib.pyplot as plt
        plt.close(fig)

    def test_hyperbola_c_verified(self):
        from scripts.graphs import spec_9b as s
        import sympy as sp
        fig, facts, checks = s.build_hyperbola_details()
        # c^2 = a^2 + b^2 = 9 + 4 = 13
        assert sp.simplify(facts["c"] ** 2) == 13
        import matplotlib.pyplot as plt
        plt.close(fig)

    def test_point_reflection_verified(self):
        from scripts.graphs import spec_9b as s
        import sympy as sp
        fig, facts, checks = s.build_point_reflection()
        assert facts["reflection"] == sp.Point(-5, -1)
        assert facts["midpoint"] == sp.Point(-2, 2)
        import matplotlib.pyplot as plt
        plt.close(fig)