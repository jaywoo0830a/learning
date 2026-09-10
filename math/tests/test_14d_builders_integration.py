# Integration: the registered 14D / 14D1 builders run and expose verifiable
# facts.  Builders now return (fig, facts, checks) and are registered under
# viz.registry (the single source of truth); the canonical path comes from the
# spec, not from the builder.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import sympy as sp

from viz.registry import specs, spec, build_all


class _Build:
    @staticmethod
    def facts(gid):
        fig, facts, checks, _ = spec(gid).run()
        plt.close(fig)
        return facts


class TestAllBuildersRun:
    def test_registry_has_the_seven_14d_14d1_graphs(self):
        ids = {gid for gid in specs() if gid.split("-")[0] in {"14d", "14d1"}}
        assert ids == {
            "14d-01-derivative-units", "14d-02-motion-story",
            "14d1-03-linearization", "14d1-04-circle-ring", "14d1-05-sphere-shell",
            "14d1-06-marginal-cost", "14d1-07-elasticity",
        }

    def test_build_all_runs_and_paths_exist(self):
        res = build_all()
        assert set(res) == set(specs())
        for gid, (fig, _facts, checks, path) in res.items():
            assert callable(fig.savefig)
            assert isinstance(checks, dict)
            assert path.endswith(".png")
            plt.close(fig)


class TestVerifiedFacts:
    """The facts each builder hard-checks and returns at build time."""

    def test_d1_units(self):
        f = _Build.facts("14d-01-derivative-units")
        assert f["slope_mps_at_2"] == 2
        assert f["mc_at_12"] == 28
        assert f["C12"] == 336

    def test_d2_motion(self):
        f = _Build.facts("14d-02-motion-story")
        assert f["turn_points"] == [1, 3]

    def test_d3_linearization(self):
        f = _Build.facts("14d1-03-linearization")
        assert f["fprime_4"] == sp.Rational(1, 4)
        assert f["L_4_1"] == sp.Rational(81, 40)

    def test_d4_ring(self):
        f = _Build.facts("14d1-04-circle-ring")
        assert sp.simplify(f["dA_dr"]) == 2 * sp.pi * sp.symbols("r")

    def test_d5_shell(self):
        f = _Build.facts("14d1-05-sphere-shell")
        assert sp.simplify(f["dV_dr"]) == 4 * sp.pi * sp.symbols("r") ** 2

    def test_d6_marginal_cost(self):
        f = _Build.facts("14d1-06-marginal-cost")
        assert f["MC_AC_cross"] == [12]

    def test_d7_elasticity(self):
        f = _Build.facts("14d1-07-elasticity")
        assert f["elasticity_at_25"] == -1
        assert f["rev_max_p"] == [25]


class TestCanonicalPaths:
    def test_paths_match_session_folders(self):
        res = build_all()
        for gid, (_, _, _, path) in res.items():
            # e.g. "14d-01-..." lives under .../graphs/14d/
            sid = gid.split("-")[0]
            assert path.split("/")[-2] == sid
            assert path.endswith(".png")