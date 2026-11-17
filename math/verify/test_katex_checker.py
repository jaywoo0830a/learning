#!/usr/bin/env python3
"""Regression tests for the KaTeX syntax checker.

Each case is a tiny Markdown document with a known verdict. They pin the two
properties that matter: the checker must *catch* real defects, and it must not
*invent* problems for legitimate constructs (escaped dollars, matrix row
separators, `\\leftrightarrow`, image alt text, fenced code).

    python3 verify/test_katex_checker.py
"""
from __future__ import annotations

import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from checks.katex import check_file  # noqa: E402

# name -> (markdown, expected_to_report_a_problem)
CASES = {
    # must be caught
    'unknown command':      ('Text $\\foo{x}$ here.\n', True),
    'unclosed brace':       ('Value $\\frac{1}{2$ here.\n', True),
    'left/right mismatch':  ('See $\\left( x$ alone.\n', True),
    'unclosed inline span': ('Broken $x + 1 text.\n', True),
    'bad environment':      ('$$\\begin{aligned} a \\end{cases}$$\n', True),
    'dangling superscript': ('Power $x^}$ here.\n', True),
    # must be silent
    'escaped dollar':       ('Cost $\\text{\\$/item}$ is fine.\n', False),
    'matrix row separator': ('$$\\begin{pmatrix}x\\\\y\\end{pmatrix}$$\n', False),
    'leftrightarrow':       ('Relation $f \\leftrightarrow x$.\n', False),
    'alt text dollar':      ('![a $/unit b](img.png) text\n', False),
    'fenced code':          ('```\n$x broken\n```\n', False),
    'display math':         ('$$\\frac{a}{b} = \\sqrt{c}$$\n', False),
}


def main() -> int:
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        path = pathlib.Path(tmp) / 'case.md'
        for name, (body, should_report) in CASES.items():
            path.write_text(body, encoding='utf-8')
            _, problems = check_file(path)
            got = bool(problems)
            ok = got == should_report
            if not ok:
                failures.append(name)
            verdict = 'PASS' if ok else 'FAIL'
            detail = problems[0].split(': ', 1)[-1] if problems else '(clean)'
            print(f'  {verdict}  {name:22s} -> {detail}')

    print()
    if failures:
        print(f'RESULT: FAIL — {len(failures)} case(s) wrong: {failures}')
        return 1
    print(f'RESULT: PASS — {len(CASES)} cases behave as expected')
    return 0


if __name__ == '__main__':
    sys.exit(main())
