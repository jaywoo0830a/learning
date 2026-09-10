# Descriptive tests for the 9b/9c graph registry mapping.
# Verifies graph ids in the source markdown resolve to canonical, real paths
# in the build registry — no assertions on PNG bytes.
import os
import re


SRC = {
    "9B": "sessions/phase2/9B-2d-functions-geometry.md",
    "9C": "sessions/phase2/9C-3d-surfaces-geometry.md",
}


def _ids_in(md_rel):
    src = open(md_rel, encoding="utf-8").read()
    return re.findall(r"\{\{graph:([^}]+)\}\}", src)


class TestNineRegistry:
    def test_every_placeholder_registered(self):
        from tools.build_markdown import KNOWN_GRAPHS
        for md in SRC.values():
            for gid in _ids_in(md):
                assert gid in KNOWN_GRAPHS, f"{gid} not registered"

    def test_source_md_pure_placeholder(self):
        for md in SRC.values():
            text = open(md, encoding="utf-8").read()
            assert ".png" not in text
            assert re.search(r"\$.*\$", text)  # KaTeX still expected somewhere

    def test_ids_per_session(self):
        assert len(_ids_in(SRC["9B"])) == 25
        assert len(_ids_in(SRC["9C"])) == 35

    def test_registered_paths_point_under_graphs(self):
        from tools.build_markdown import KNOWN_GRAPHS
        for gid in _ids_in(SRC["9B"]) + _ids_in(SRC["9C"]):
            p = KNOWN_GRAPHS[gid]
            assert "graphs" in p.split(os.sep)
            assert p.endswith(".png")

    def test_markdown_files_registered_in_build(self):
        from tools.build import MARKDOWN_FILES
        for rel in SRC.values():
            assert rel in MARKDOWN_FILES