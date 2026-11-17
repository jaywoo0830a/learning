"""KaTeX command / environment reference used by the syntax checker.

Vendored from https://katex.org/docs/supported so the checker works without a
Node runtime. When a newer KaTeX adds commands, extend these sets — the checker
names the file, line and command, so drift shows up as a precise failure rather
than a silent pass.
"""

# KaTeX-supported control sequences, grouped by purpose.
KATEX_COMMANDS = set("""
frac dfrac tfrac sqrt left right middle big Big bigg Bigg bigl bigr Bigl Bigr
lbrace rbrace lbrack rbrack langle rangle lfloor rfloor lceil rceil lvert rvert
lVert rVert vert Vert lgroup rgroup lmoustache rmoustache backslash lparen rparen
cdot cdots ldots dots times div pm mp ast star circ bullet oplus otimes
le leq ge geq ne neq lt gt approx equiv sim simeq cong propto
to rightarrow leftarrow Rightarrow Leftarrow leftrightarrow Leftrightarrow
longrightarrow longleftarrow Longrightarrow Longleftarrow iff implies impliedby
uparrow downarrow Uparrow Downarrow updownarrow Updownarrow mapsto
in notin ni subset subseteq supset supseteq cup cap setminus emptyset varnothing
forall exists nexists neg land lor lnot therefore because perp parallel
mid nmid prime backprime
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi varphi
chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
infty partial nabla hbar ell wp Re Im aleph
text textbf textit textrm textsf texttt textnormal mathrm mathbf mathit mathsf
mathtt mathbb mathcal mathfrak mathscr operatorname boldsymbol bm
quad qquad hspace hfill kern phantom hphantom vphantom smash
overline underline overbrace underbrace overrightarrow overleftarrow widehat
widetilde hat bar vec dot ddot dddot acute grave breve check tilde
overset underset stackrel substack atop choose
displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits
begin end
array matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix smallmatrix
aligned align alignat gathered split cases dcases rcases equation
ln log lg exp sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh
coth sech csch max min sup inf lim liminf limsup det dim ker hom deg gcd arg
sum prod coprod int iint iiint oint bigcup bigcap bigoplus bigotimes
space enspace thinspace negthinspace hline cline
boxed cancel bcancel xcancel color textcolor colorbox fbox
raisebox rule strut mathstrut tag notag
bmod pmod pod operatornamewithlimits
binom dbinom tbinom
lesssim gtrsim lessgtr gtrless ll gg lll ggg vdots ddots dotsi
longleftrightarrow Longleftrightarrow longmapsto mapstochar
square triangle triangledown blacksquare lozenge blacklozenge
ulcorner urcorner llcorner lrcorner smile frown asymp bowtie models vdash dashv
bot top not
""".split())

KATEX_ENVIRONMENTS = {
    'array', 'matrix', 'pmatrix', 'bmatrix', 'Bmatrix', 'vmatrix', 'Vmatrix',
    'smallmatrix', 'aligned', 'align', 'alignat', 'gathered', 'split',
    'cases', 'dcases', 'rcases', 'equation', 'equation*', 'align*',
}
