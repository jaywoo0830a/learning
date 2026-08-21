# Mechanics — Special: Visual Diagrams

Python-drawn setup diagrams for the accounting-model worked examples
([`work/examples.md`](../special/work/examples.md) and
[`energy/examples.md`](../special/energy/examples.md)).

## Contents

- `generate_examples.py` — draws all 14 diagrams (matplotlib, Agg backend, mathtext only, no LaTeX)
- `graphs/` — output PNGs:
  - `work-1-lift.png` … `work-7-spring.png` — the seven examples in `work/examples.md`
  - `energy-1-toss.png` … `energy-7-crate.png` — the seven examples in `energy/examples.md`

## Usage

```bash
python3 generate_examples.py
```

Re-runnable; overwrites the PNGs in `graphs/`. The markdown files reference the images
with relative paths like `../../visual/graphs/work-1-lift.png`.

## Conventions

- Color code: blue-gray = objects, red = forces, green = velocity/motion, brown = ground/Earth, gray = wall/ceiling.
- `$g=10$ m/s²`, schematic only (not to scale); every figure carries a title naming its example.
- Force arrows are drawn from the point of application; dimension lines are dashed double-arrows.
