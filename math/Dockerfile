# Math viz/verify core development image.
# Runs pytest + matplotlib + sympy + z3 fully inside the container,
# so the host Python is never polluted.
FROM python:3.12-slim

# matplotlib needs these at build time to avoid runtime font/config hiccups.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace/math

# Install Python deps (pinned for reproducibility).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Make the math package importable when running pytest from /workspace/math.
ENV PYTHONPATH=/workspace/math

# Non-root user for safety.
RUN useradd -m -u 1000 dev && chown -R dev:dev /workspace
USER dev

CMD ["pytest", "-q"]