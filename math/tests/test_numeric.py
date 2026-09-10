# Tests for the numeric verification helpers.
# TDD: expectations defined first, then verify/numeric.py implements them.
import numpy as np
import pytest

from verify.numeric import is_close, check_sequence, passive_validate


class TestIsClose:
    def test_within_tol(self):
        assert is_close(0.1 + 0.2, 0.3)

    def test_outside_tol(self):
        assert not is_close(1.0, 2.0)

    def test_custom_tol_atol(self):
        assert is_close(1.0, 1.05, rel=0.1)
        assert not is_close(1.0, 1.2, rel=0.1)

    def test_exact_equal(self):
        assert is_close(3.0, 3.0)


class TestCheckSequence:
    def test_increasing(self):
        x = np.linspace(0, 1, 10)
        assert check_sequence(x, monotonic="increasing")

    def test_decreasing(self):
        x = np.linspace(1, 0, 10)
        assert check_sequence(x, monotonic="decreasing")

    def test_not_monotonic(self):
        x = np.array([0, 1, 0])
        assert not check_sequence(x, monotonic="increasing")

    def test_numeric_tolerance(self):
        # 0, 1e-14, 2 - effectively increasing under tolerance
        x = np.array([0.0, 1e-14, 2.0])
        assert check_sequence(x, monotonic="increasing", tol=1e-9)


class TestPassiveValidate:
    def test_ok_case(self):
        # A check closure that holds.
        ok, failures = passive_validate({"c": lambda: 1 + 1 == 2})
        assert ok
        assert failures == {}

    def test_failed_case(self):
        ok, failures = passive_validate({"c": lambda: 1 + 1 == 3})
        assert not ok
        assert "c" in failures

    def test_runs_all(self):
        # Even if the first fails, the second still runs.
        ok, failures = passive_validate(
            {"a": lambda: False, "b": lambda: True}
        )
        assert not ok
        assert set(failures) == {"a"}