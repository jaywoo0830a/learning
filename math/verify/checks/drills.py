"""Drill-answer verification.

Runs a session's declared numeric assertions (see `verify/answers/<id>.py`)
against sympy. The runner is session-agnostic: a session module supplies
`SECTIONS` and a `run(ctx)` hook, and everything else lives here.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import sympy as sp

ANSWERS_DIR = pathlib.Path(__file__).resolve().parent.parent / 'answers'


class Context:
    """Collects pass/fail results and prints them in a readable tree."""

    def __init__(self, verbose: bool = True) -> None:
        self.verbose = verbose
        self.passed = 0
        self.failed: list[str] = []

    def begin_section(self, title: str) -> None:
        if self.verbose:
            print(f'\n[{title}]')

    def check(self, label: str, got, want) -> None:
        if isinstance(want, (list, tuple)):
            ok = (len(got) == len(want)
                  and all(sp.simplify(a - b) == 0 for a, b in zip(got, want)))
        else:
            try:
                ok = sp.simplify(got - want) == 0
            except TypeError:
                ok = got == want
        if ok:
            self.passed += 1
            if self.verbose:
                print(f'  PASS {label}')
        else:
            self.failed.append(label)
            print(f'  FAIL {label}: got {got}, want {want}')

    @property
    def total(self) -> int:
        return self.passed + len(self.failed)


def available_sessions() -> list[str]:
    """Session ids that have a declared answer module, e.g. ['14D']."""
    return sorted(p.stem for p in ANSWERS_DIR.glob('*.py') if not p.name.startswith('_'))


def _load(session: str):
    path = ANSWERS_DIR / f'{session}.py'
    if not path.exists():
        raise FileNotFoundError(
            f'no answer module for session {session!r}; expected {path}')
    spec = importlib.util.spec_from_file_location(f'verify_answers_{session}', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_session(session: str, verbose: bool = True) -> Context:
    """Evaluate one session's checks. Returns the context for inspection."""
    module = _load(session)
    ctx = Context(verbose=verbose)
    if not hasattr(module, 'run'):
        raise AttributeError(f'{session}: answer module must define run(ctx)')
    module.run(ctx)
    return ctx


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith('-')]
    quiet = '-q' in argv or '--quiet' in argv
    sessions = args or available_sessions()
    if not sessions:
        print('no answer modules found in', ANSWERS_DIR)
        return 1

    failures = 0
    for session in sessions:
        ctx = run_session(session, verbose=not quiet)
        status = 'OK' if not ctx.failed else f'{len(ctx.failed)} failed'
        print(f'\n{session}: {ctx.passed}/{ctx.total} checks passed ({status})')
        if ctx.failed:
            failures += len(ctx.failed)

    print('\n' + '=' * 60)
    if failures:
        print(f'RESULT: FAIL — {failures} assertion(s) did not hold')
        return 1
    print('RESULT: PASS — every declared number is confirmed')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
