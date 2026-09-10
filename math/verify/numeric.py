"""Numeric verification helpers built on numpy.

Provide tolerance-aware checks and a small "validate" runner so a graph spec
can attach assertions that are collected and reported without throwing on the
first failure.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, Tuple

import numpy as np


def is_close(a: float, b: float, rel: float = 1e-7, atol: float = 1e-9) -> bool:
    """Return True if ``a`` and ``b`` are within float tolerance.

    Uses the same rule as numpy's allclose: |a-b| <= atol + rel * |b|.
    """
    return bool(np.isclose(a, b, rtol=rel, atol=atol))


def check_sequence(
    seq,
    monotonic: str = "increasing",
    tol: float = 0.0,
) -> bool:
    """Return True if ``seq`` is monotonic in the requested direction.

    ``monotonic`` is "increasing" or "decreasing". A small ``tol`` allows a
    tiny backward/forward step (useful for sampled curved data).
    """
    seq = np.asarray(seq, dtype=float)
    if seq.ndim != 1 or seq.size < 2:
        return True
    diff = np.diff(seq)
    if monotonic == "increasing":
        return bool(np.all(diff >= -tol))
    if monotonic == "decreasing":
        return bool(np.all(diff <= tol))
    raise ValueError("monotonic must be 'increasing' or 'decreasing'")


def passive_validate(
    checks: Dict[str, Callable[[], bool]],
) -> Tuple[bool, Dict[str, Any]]:
    """Run each check closure, collecting failures without early-exit.

    Returns ``(all_ok, failures)`` where ``failures`` maps check-name to the
    raised exception (or a False mark). Useful so one bad graph does not hide
    the rest.
    """
    failures: Dict[str, Any] = {}
    for name, fn in checks.items():
        try:
            result = fn()
            if not result:
                failures[name] = False
        except Exception as exc:  # noqa: BLE001 - report everything
            failures[name] = exc
    return (len(failures) == 0), failures