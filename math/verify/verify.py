#!/usr/bin/env python3
"""Verification entry point for the math sessions.

Two independent checks, both usable on any session:

    python3 verify/verify.py katex 14D        # Markdown + KaTeX syntax
    python3 verify/verify.py answers 14D      # numbers asserted against sympy
    python3 verify/verify.py all              # katex on every session, all answers
    python3 verify/verify.py answers          # every session that has an answer module

Exit code is 0 only when every selected check passes, so it can gate CI:

    python3 verify/verify.py all && make strict
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
MATH = ROOT.parent
SESSIONS = MATH / 'sessions'

sys.path.insert(0, str(ROOT))

from checks import drills, katex  # noqa: E402

USAGE = __doc__


def session_files(selector: str | None) -> list[pathlib.Path]:
    """Markdown files for a session id (e.g. '14D'), a phase, or the whole tree."""
    if selector is None:
        return sorted(SESSIONS.rglob('*.md'))
    hits = sorted(SESSIONS.rglob(f'{selector}*.md'))
    if not hits:
        raise SystemExit(f'no session files match {selector!r} under {SESSIONS}')
    return hits


def cmd_katex(args: list[str]) -> int:
    paths: list[pathlib.Path] = []
    if not args:
        paths = session_files(None)
    for a in args:
        paths.extend(session_files(a))
    # de-duplicate while keeping order
    seen, unique = set(), []
    for p in paths:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    print(f'KaTeX syntax check — {len(unique)} file(s)')
    return katex.main(unique, quiet=len(unique) > 8)


def cmd_answers(args: list[str]) -> int:
    sessions = args or drills.available_sessions()
    if not sessions:
        print('no answer modules in', drills.ANSWERS_DIR)
        print('add verify/answers/<SESSION>.py to start checking a session')
        return 1
    return drills.main(sessions)


def main(argv: list[str]) -> int:
    if not argv or argv[0] in {'-h', '--help', 'help'}:
        print(USAGE)
        return 0

    cmd, rest = argv[0], argv[1:]
    if cmd == 'katex':
        return cmd_katex(rest)
    if cmd == 'answers':
        return cmd_answers(rest)
    if cmd == 'all':
        rc_answers = cmd_answers([])
        print()
        rc_katex = cmd_katex([])
        return 0 if (rc_answers == 0 and rc_katex == 0) else 1

    print(f'unknown command {cmd!r}\n')
    print(USAGE)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
