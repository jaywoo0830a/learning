"""Static KaTeX validation for the 14D drill content.

1. Extracts every math span ($...$, $$...$$) from the session and solutions files.
2. Enumerates every control sequence and environment used.
3. Checks each against the KaTeX supported-functions list (katex.org/docs/supported).
4. Checks brace balance and \\left/\\right pairing.
"""
import io, re, sys

# KaTeX-supported control sequences we rely on (verified against katex.org/docs/supported)
SUPPORTED = set("""
frac dfrac tfrac sqrt partial left right big Big Bigg bigl bigr Bigl Bigr middle
cdot cdots ldots times div pm mp
le ge ne approx equiv sim to rightarrow leftarrow Rightarrow Longrightarrow longrightarrow
leftrightarrow Leftarrow uparrow downarrow mapsto
infty pi alpha beta gamma delta theta lambda mu sigma phi omega varepsilon epsilon
Delta Sigma Omega Gamma Lambda Pi Theta
quad qquad text textbf textit textrm mathrm mathbf mathbb mathcal mathsf mathtt operatorname
begin end aligned align gathered split cases matrix pmatrix bmatrix vmatrix Vmatrix array
hat bar vec overline underline overbrace underbrace widehat widetilde
ln log exp sin cos tan cot sec csc arcsin arccos arctan max min sup inf lim det gcd
in notin subset subseteq supset cup cap emptyset forall exists neg land lor therefore
lfloor rfloor lceil rceil langle rangle vert Vert mid
boxed cancel overset underset substack displaystyle textstyle scriptstyle
prime circ ast star bullet angle triangle square hline
int iint iiint oint sum prod
""".split())

latex_cmds = set()
envs = set()
math_spans = []

def extract(path):
    s = io.open(path, encoding='utf-8').read()
    s = re.sub(r'```[\s\S]*?```', '', s)          # drop code fences
    spans = []
    spans += re.findall(r'\$\$([\s\S]+?)\$\$', s)
    s2 = re.sub(r'\$\$[\s\S]+?\$\$', ' ', s)
    spans += re.findall(r'(?<!\\)\$([^$\n]+?)\$', s2)
    return spans

base = '/Users/jeongwookim/Desktop/projects/learning/math/sessions/phase2/'
files = [base + '14D-relation-lens.md', base + 'solutions/14D-solutions.md']

for f in files:
    for sp in extract(f):
        math_spans.append(sp)
        for c in re.findall(r'\\([a-zA-Z]+)', sp):
            latex_cmds.add(c)
        for e in re.findall(r'\\begin\{([a-zA-Z*]+)\}', sp):
            envs.add(e)

print(f'math spans: {len(math_spans)}')
print(f'commands: {len(latex_cmds)}')
print('  ', sorted(latex_cmds))
print(f'environments: {sorted(envs)}')

bad_cmds = sorted(c for c in latex_cmds if c not in SUPPORTED and c not in ('begin', 'end'))
bad_envs = sorted(e for e in envs if e not in
                  ('aligned', 'cases', 'matrix', 'pmatrix', 'bmatrix', 'vmatrix', 'array'))

print('\nunsupported commands:', bad_cmds if bad_cmds else 'none')
print('unsupported environments:', bad_envs if bad_envs else 'none')

# brace balance and \left/\right pairing
unbalanced, mismatched = [], []
for sp in math_spans:
    depth = 0
    ok = True
    for ch in sp:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                ok = False
                break
    if depth != 0 or not ok:
        unbalanced.append(sp[:80])
    if sp.count('\\left') != sp.count('\\right'):
        mismatched.append(sp[:80])

print('\nunbalanced braces:', unbalanced if unbalanced else 'none')
print('mismatched \\left/\\right:', mismatched if mismatched else 'none')

fail = bool(bad_cmds or bad_envs or unbalanced or mismatched)
print('\nRESULT:', 'FAIL' if fail else 'PASS — every expression uses only supported constructs, braces balanced')
sys.exit(1 if fail else 0)
