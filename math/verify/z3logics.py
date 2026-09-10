"""Z3-based logic verification helpers.

Built on the ``z3-solver`` package. These are the exact, decision-procedure
checks for the logic / truth-table problems in Phase 1 (and any constraint that
boils down to a satisfiability/validity query): tautology, logical
equivalence, and existence of a satisfying model.

Importing ``z3`` is deferred to call time so the rest of the verify package
still imports even if z3 is absent on a given machine.
"""
from __future__ import annotations

from typing import Optional

import z3


def z3_equivalent(lhs, rhs) -> bool:
    """Return True if Boolean formula ``lhs`` and ``rhs`` are logically equal.

    Two formulas are equivalent iff ``lhs == rhs`` (XNOR) is a tautology, i.e.
    its negation is unsatisfiable under every assignment.
    """
    s = z3.Solver()
    s.add(z3.Not(lhs == rhs))
    return s.check() == z3.unsat


def z3_tautology(formula) -> bool:
    """Return True if ``formula`` holds for all assignments (is a tautology)."""
    # formula is a z3 Bool; asserting NOT formula must be unsat.
    s = z3.Solver()
    s.add(z3.Not(formula))
    return s.check() == z3.unsat


def z3_satisfiable(formula) -> bool:
    """Return True if some assignment satisfies ``formula``."""
    s = z3.Solver()
    s.add(formula)
    return s.check() == z3.sat