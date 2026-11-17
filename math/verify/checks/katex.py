"""KaTeX / Markdown math-syntax checking for any session file.

`$...$` and `$$...$$` spans are parsed the way a Markdown-with-KaTeX renderer
does, then each span is checked for constructs KaTeX rejects:

  1. every control sequence is a KaTeX-supported command
  2. every `\\begin{env}` uses a supported environment and is closed
  3. braces balance
  4. `\\left` / `\\right` pair up
  5. `_` and `^` carry an operand
  6. no stray `$` inside a span; `$` count is even outside code fences
"""
from __future__ import annotations

import pathlib
import re

from .katex_commands import KATEX_COMMANDS, KATEX_ENVIRONMENTS


def strip_code(md: str) -> list[tuple[str, int]]:
    """Blank out fenced code and image alt text, keeping line numbers aligned.

    Alt text is not rendered as math, so a literal `$` inside `![...]` must not
    be mistaken for an unterminated span. Fenced code is skipped for the same
    reason.
    """
    out: list[tuple[str, int]] = []
    in_fence = False
    fence_re = re.compile(r'^\s*(```|~~~)')
    alt_re = re.compile(r'!\[[^\]]*\]')
    for i, line in enumerate(md.split('\n'), start=1):
        if fence_re.match(line):
            in_fence = not in_fence
            out.append(('', i))
            continue
        out.append(('' if in_fence else alt_re.sub('![]', line), i))
    return out


def find_spans(lines: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Return (body, source_line) for each math span.

    Display math (`$$...$$`) may span lines; inline math may not. The scanning
    is done character by character rather than by regex so that an escaped
    dollar (`\\$`, a literal currency sign) never terminates a span — a plain
    regex cannot distinguish `$...\\$...$` from `$...$` followed by `\\$`.
    """
    text = '\n'.join(t for t, _ in lines)

    # map every character position back to its source line
    line_of: list[int] = []
    for t, n in lines:
        line_of.extend([n] * (len(t) + 1))

    spans: list[tuple[str, int]] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == '\\':                 # skip the escaped character
            i += 2
            continue
        if ch != '$':
            i += 1
            continue

        display = text.startswith('$$', i)
        open_len = 2 if display else 1
        start = i
        j = i + open_len
        closed = -1
        while j < n:
            if text[j] == '\\':
                j += 2
                continue
            if text[j] == '$':
                if display:
                    if text.startswith('$$', j):
                        closed = j
                        break
                else:
                    if j > 0 and text[j - 1] == '\n':
                        pass
                    closed = j
                    break
            elif not display and text[j] == '\n':
                break                  # inline math cannot span a line
            j += 1

        if closed < 0:
            i = start + open_len       # unterminated: leave it to the parity check
            continue

        body = text[start + open_len:closed]
        spans.append((body, line_of[start]))
        i = closed + open_len
    return spans


def _brace_depth_problems(body: str) -> list[str]:
    problems, depth = [], 0
    i = 0
    while i < len(body):
        ch = body[i]
        if ch == '\\':          # skip the escaped char (\{ \} \$ \\ ...)
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                problems.append('unmatched closing brace')
                return problems
        i += 1
    if depth > 0:
        problems.append(f'{depth} unclosed brace(s)')
    return problems


def _control_sequences(body: str) -> list[str]:
    r"""Return control-sequence names, treating `\\` as a single line break.

    A naive `\\([a-zA-Z]+)` would read the row separator `\\y` inside a matrix
    as the command `\y`. Walking the string makes `\\` consume both characters.
    """
    names, i, n = [], 0, len(body)
    while i < n:
        if body[i] != '\\':
            i += 1
            continue
        j = i + 1
        while j < n and body[j].isalpha():
            j += 1
        if j == i + 1:          # '\\', '\{', '\$' … — no name
            i = j + 1
            continue
        names.append(body[i + 1:j])
        i = j
    return names


def _delimiter_problems(body: str) -> list[str]:
    r"""Count \left / \right as whole commands — \leftrightarrow is not a \left."""
    left = len(re.findall(r'\\left(?![a-zA-Z])', body))
    right = len(re.findall(r'\\right(?![a-zA-Z])', body))
    if left != right:
        return [f'\\left/\\right mismatch ({left} vs {right})']
    return []


def _has_bare_dollar(body: str) -> bool:
    r"""True when a '$' appears that is not escaped as '\$'.

    '\$' is a legitimate literal currency sign inside math, e.g.
    `\text{\$/item}`, so it must not be reported.
    """
    i, n = 0, len(body)
    while i < n:
        if body[i] == '\\':
            i += 2
            continue
        if body[i] == '$':
            return True
        i += 1
    return False


def check_span(body: str) -> list[str]:
    """Return a list of problems for one math span (empty = clean)."""
    problems: list[str] = []

    for cmd in _control_sequences(body):
        if cmd not in KATEX_COMMANDS:
            problems.append(f'unknown KaTeX command \\{cmd}')

    begins = re.findall(r'\\begin\{([a-zA-Z*]+)\}', body)
    ends = re.findall(r'\\end\{([a-zA-Z*]+)\}', body)
    for env in begins:
        if env not in KATEX_ENVIRONMENTS:
            problems.append(f'unsupported environment {{{env}}}')
    if sorted(begins) != sorted(ends):
        problems.append(f'unbalanced \\begin/\\end ({begins} vs {ends})')

    problems.extend(_brace_depth_problems(body))
    problems.extend(_delimiter_problems(body))

    if re.search(r'[_^]\s*(?=[_^}\s]|$)', body):
        problems.append('subscript/superscript without an operand')

    # a bare '$' inside a span means the span was mis-detected; '\$' is a
    # legitimate literal dollar sign (e.g. \text{\$/item})
    if _has_bare_dollar(body):
        problems.append('stray $ inside math span')

    return problems


def _unescaped_dollar_count(text: str) -> int:
    r"""Count '$' that are not escaped as '\$'."""
    count, i, n = 0, 0, len(text)
    while i < n:
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '$':
            count += 1
        i += 1
    return count


def check_file(path: pathlib.Path) -> tuple[int, list[str]]:
    """Check one Markdown file. Returns (span_count, problems)."""
    lines = strip_code(path.read_text(encoding='utf-8'))
    text = '\n'.join(t for t, _ in lines)

    problems: list[str] = []
    unescaped = _unescaped_dollar_count(text)
    if unescaped % 2:
        problems.append(f'odd number of unescaped $ ({unescaped}) '
                        f'— an inline math span is unclosed')

    spans = find_spans(lines)
    for body, line in spans:
        for p in check_span(body):
            problems.append(f'{path}:{line}: {p}')
    return len(spans), problems


def main(paths: list[pathlib.Path], quiet: bool = False) -> int:
    total, problems = 0, []
    for p in paths:
        n, probs = check_file(p)
        total += n
        problems.extend(probs)
        if not quiet:
            state = 'ok' if not probs else f'{len(probs)} problem(s)'
            print(f'  {p.name}: {n} math span(s) — {state}')

    print()
    if problems:
        for p in problems:
            print('✗', p)
        print(f'\nRESULT: FAIL — {len(problems)} problem(s) in {total} spans')
        return 1
    print(f'RESULT: PASS — {total} math span(s), all KaTeX constructs valid')
    return 0
