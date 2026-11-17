# Reproducible verification environment for the math sessions.
#
# The image only carries the checker's dependencies; the session Markdown and
# the answer modules are bind-mounted at run time, so editing a session or an
# answer file needs no rebuild.
#
#   docker build -t math-verify verify
#   docker run --rm -v "$PWD:/work" math-verify answers 14D
#
# or, from math/:   make verify / make verify-katex / make verify-all
FROM python:3.12-slim

# sympy is the only dependency: every numeric assertion is symbolic, so a
# wrong answer is caught exactly rather than within a floating-point tolerance.
RUN pip install --no-cache-dir "sympy==1.13.3"

WORKDIR /work

# Fail fast on an import error instead of half-running a session.
RUN python -c "import sympy; print('sympy', sympy.__version__)"

ENTRYPOINT ["python", "/work/verify/verify.py"]
CMD ["all"]
