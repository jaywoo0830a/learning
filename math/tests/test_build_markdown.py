# Tests for the markdown build tool: graph registry + image injection.
# The committed source .md uses {{graph:<id>}}; build renders it to a resolved
# (unwritten) string — source is never mutated.
import os

import pytest


SAMPLE = """# Session

Some prose with math: $x^2 + y^2 = 25$.

![A circle diagram]({{graph:14d1-04-circle-ring}})

More KaTeX: $$\\frac{dy}{dx} = -\\frac{x}{y}$$
"""

MD_PATH = "/repo/math/sessions/phase2/14D1-derivative-interpretation.md"


class TestFindGraphRefs:
    def test_extracts_ids(self):
        from tools.build_markdown import find_graph_refs

        assert find_graph_refs(SAMPLE) == ["14d1-04-circle-ring"]

    def test_no_refs_returns_empty(self):
        from tools.build_markdown import find_graph_refs

        assert find_graph_refs("No images here.") == []


class TestRegistry:
    def test_known_id_has_canonical_path(self):
        from tools.build_markdown import image_path_for

        p = image_path_for("14d1-04-circle-ring")
        assert p.endswith(os.path.join("graphs", "14d1", "04-circle-ring.png"))
        assert not p.endswith("14d1-04-circle-ring.png")  # no double-session encoding

    def test_unknown_id_raises(self):
        from tools.build_markdown import image_path_for

        with pytest.raises(KeyError):
            image_path_for("does-not-exist")


class TestResolveRelativePath:
    def test_relpath_from_md(self):
        from tools.build_markdown import resolve_image_path

        img_abs = "/repo/math/graphs/14d1/04-circle-ring.png"
        rel = resolve_image_path(MD_PATH, img_abs)
        assert rel == os.path.join("..", "..", "graphs", "14d1", "04-circle-ring.png")


class TestRender:
    def test_renders_in_memory_and_preserves_text(self):
        from tools.build_markdown import render_text

        text = render_text(SAMPLE, MD_PATH)
        assert "{{graph:14d1-04-circle-ring}}" not in text
        assert ".png" in text
        # pure KaTeX + prose preserved
        assert "$x^2 + y^2 = 25$" in text
        assert "\\frac{dy}{dx}" in text

    def test_source_unchanged(self, tmp_path):
        # render_to_text reads source but does not write it back
        from tools.build_markdown import render_to_text

        md = tmp_path / "s.md"
        md.write_text(SAMPLE)
        before = md.read_text()
        render_to_text(str(md))
        assert md.read_text() == before  # untouched