"""Verification layer for the math viz pipeline.

Provides symbolic (sympy) and numeric (numpy) helpers so that every graph's
claim can be checked as an executable test, in addition to rendering.

Submodules:
- symbolic: sympy-based exact checks (slopes, equivalence, tangent lines).
- numeric:   floating-point / sampling checks.
- z3logics:  Z3-based logic / constraint checks (added as needed).
"""
from .symbolic import (
    simplify_true,
    slope_of_implicit,
    is_equivalent,
    tangent_line,
)
from .numeric import (
    is_close,
    check_sequence,
    passive_validate,
)
from .z3logics import (
    z3_equivalent,
    z3_tautology,
    z3_satisfiable,
)

__all__ = [
    "simplify_true",
    "slope_of_implicit",
    "is_equivalent",
    "tangent_line",
    "is_close",
    "check_sequence",
    "passive_validate",
    "z3_equivalent",
    "z3_tautology",
    "z3_satisfiable",
]