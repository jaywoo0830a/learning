# Tests for the Z3 logic verification layer.
# TDD: define expected behavior, implement verify/z3logics.py to satisfy it.
import pytest

z3 = pytest.importorskip("z3")


class TestFormulaEquivalence:
    def test_de_morgan(self):
        from verify.z3logics import z3_equivalent

        A, B = z3.Bools("A B")
        lhs = z3.Not(z3.And(A, B))
        rhs = z3.Or(z3.Not(A), z3.Not(B))
        assert z3_equivalent(lhs, rhs)

    def test_distributive_false(self):
        from verify.z3logics import z3_equivalent

        A, B, C = z3.Bools("A B C")
        assert not z3_equivalent(
            z3.And(A, z3.Or(B, C)),
            z3.Or(A, z3.And(B, C)),  # not the distributive identity
        )

    def test_distributive_true(self):
        from verify.z3logics import z3_equivalent

        A, B, C = z3.Bools("A B C")
        assert z3_equivalent(
            z3.And(A, z3.Or(B, C)),
            z3.Or(z3.And(A, B), z3.And(A, C)),
        )


class TestFormulaTautology:
    def test_tautology(self):
        from verify.z3logics import z3_tautology

        A, B = z3.Bools("A B")
        # (A -> B) <-> (~A | B)
        assert z3_tautology(z3.Implies(A, B) == z3.Or(z3.Not(A), B))

    def test_not_tautology(self):
        from verify.z3logics import z3_tautology

        A = z3.Bool("A")
        assert not z3_tautology(A)  # A is not always true


class TestModelCandidates:
    def test_sat_example(self):
        from verify.z3logics import z3_satisfiable

        A, B = z3.Bools("A B")
        assert z3_satisfiable(z3.And(A, z3.Not(B)))  # model (A=T, B=F)

    def test_unsat(self):
        from verify.z3logics import z3_satisfiable

        A = z3.Bool("A")
        assert not z3_satisfiable(z3.And(A, z3.Not(A)))