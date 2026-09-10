# Development helpers for the math viz/verify core.
# All commands run inside the Docker container so the host Python stays clean.

.PHONY: build up run test shell clean run-sample

# Build (or rebuild) the dev image.
build:
	docker compose build

# Run the full test suite in the container.
test:
	docker compose run --rm math pytest -q

# Run an arbitrary pytest selection, e.g. `make test-select tests/test_symbolic.py`
test-collect:
	docker compose run --rm math pytest $(ARGS) -q

# Generate the verified demo graph (circle + tangent) into math/graphs/
run-sample:
	docker compose run --rm math python scripts/demo_circle_tangent.py

# Open a bash shell inside the container (for debugging).
shell:
	docker compose run --rm math bash

# Remove stopped containers for this project.
clean:
	docker compose down