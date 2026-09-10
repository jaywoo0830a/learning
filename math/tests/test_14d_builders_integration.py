# Integration: the 7 migrated 14D/14D1 builders return verified facts.
import matplotlib
matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
import sympy as sp

from scripts.graphs.spec_14d_relations import ALL_BUILDERS, build_all


class TestAllBuildersRun:
    def test_all_factories_exist(self):
        assert len(ALL_BUILDERS) == 7

    def test_build_all_runs_without_error(self):
        res = build_all()
        assert set(res.keys()) == set(ALL_BUILDERS.keys())


class TestVerifiedFacts:
    """The facts each builder hard-checks at build time."""

    def _build(self, name):
        fig, facts, path = ALL_BUILDERS[name]()
        plt.close(fig)
        return facts

    def test_d1_units(self):
        f = self._build("14d-01-derivative-units")
        assert f["slope_mps_at_2"] == 2
        assert f["mc_at_12"] == 28
        assert f["C12"] == 336

    def test_d2_motion(self):
        f = self._build("14d-02-motion-story")
        assert f["turn_points"] == [1, 3]

    def test_d3_linearization(self):
        f = self._build("14d1-03-linearization")
        assert f["fprime_4"] == sp.Rational(1, 4)
        assert f["L_4_1"] == sp.Rational(81, 40)

    def test_d4_ring(self):
        f = self._build("14d1-04-circle-ring")
        assert sp.simplify(f["dA_dr"]) == 2 * sp.pi * sp.symbols("r")

    def test_d5_shell(self):
        f = self._build("14d1-05-sphere-shell")
        assert sp.simplify(f["dV_dr"]) == 4 * sp.pi * sp.symbols("r") ** 2

    def test_d6_marginal_cost(self):
        f = self._build("14d1-06-marginal-cost")
        assert f["MC_AC_cross"] == [12]

    def test_d7_elasticity(self):
        f = self._build("14d1-07-elasticity")
        assert f["elasticity_at_25"] == -1
        assert f["rev_max_p"] == [25]


class TestCanonicalPaths:
    def test_paths_match_session_folders(self):
        res = build_all()
        for name, (_, path) in res.items():
            # e.g. "14d-01-..." lives under .../graphs/14d/
            sid = name.split("-")[0]
            assert path.split("/")[-2] == sid
            assert path.endswith(".png")