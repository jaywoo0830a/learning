"""Contract test for the graph registry.

Every registered graph must:
  - run without raising,
  - return ``(fig, facts, checks)`` (via ``GraphSpec.run`` -> +path),
  - have every one of its ``checks`` (name -> () -> bool) pass.

This makes "the picture is the test": the same claims the builder attaches are
executed here, uniformly, for every graph in the repo.
"""
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt

import pytest

from verify.numeric import passive_validate
from viz.registry import specs


def _ids():
    return sorted(specs())


@pytest.mark.parametrize("gid", _ids())
def test_graph_runs_and_all_checks_hold(gid):
    gs = specs()[gid]
    fig, facts, checks, path = gs.run()
    try:
        assert isinstance(facts, dict)
        assert isinstance(checks, dict) and checks, f"{gid} has no checks"
        ok, failures = passive_validate(checks)
        assert ok, f"{gid} failed checks: {failures}"
        assert path.endswith(".png")
    finally:
        plt.close(fig)


@pytest.mark.parametrize("gid", _ids())
def test_graph_path_is_canonical(gid):
    gs = specs()[gid]
    path = gs.path
    assert path.endswith(".png")
    assert "/graphs/" in path
    # canonical: graphs/<session>/<nn>-<slug>.png -> folder matches gid prefix
    assert path.split("/")[-2] == gid.split("-")[0]