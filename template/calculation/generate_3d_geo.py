#!/usr/bin/env python3
"""Generate 3d-geo-pad.html — 50-page pad for 3D analytic geometry problem-solving.
   Isometric (triangular) dot grid as primary, faint square grid secondary.
   Darker colours tuned for print visibility."""

import html as html_mod

from quotes import QUOTES

# 5 anchors — wider spacing for 3D problems which need more room per problem
PAGE_BODY = """  <!-- ================================================================== -->
  <section class="hai-page calc-pad">

    <div class="calc-quote">&ldquo;{quote}&rdquo; &mdash; {author}</div>

    <div class="calc-header">
      <div class="field"><span class="label">Date</span><span class="value"></span></div>
      <div class="field"><span class="label">Subject</span><span class="value" style="min-width:22mm;"></span></div>
      <div class="field"><span class="label">Topic</span><span class="value" style="min-width:28mm;"></span></div>
      <div class="field spacer"></div>
      <div class="field"><span class="label">p.</span><span class="value" style="min-width:8mm;text-align:right;"></span></div>
    </div>

    <div class="anchors-area" style="position:relative;">

      <div class="anchor-row"><div class="anchor-num">1</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>
      <div class="anchor-row"><div class="anchor-num">2</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>

      <div class="fold-guide"></div>

      <div class="anchor-row"><div class="anchor-num">3</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>
      <div class="anchor-row"><div class="anchor-num">4</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>
      <div class="anchor-row" style="margin-bottom:0;"><div class="anchor-num">5</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>

    </div>


  </section>
"""

HTML_HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3D Analytic Geometry Pad</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/htmlasitis@0.1.0/htmlasitis.css">

  <style>
    :root {
      --hai-font-body: "PT Serif", serif;
      --hai-font-mono: "PT Serif", monospace;
      --hai-font-size-body: 9pt;
      --hai-line-height-body: 1.4;
    }

    /* ── Page layout ─────────────────────────────────────────────── */
    .hai-page.calc-pad {
      display: flex;
      flex-direction: column;
      background-color: #fff;
      /*
         Isometric dot grid — triangular lattice for 3D axis guides.
         Two offset dot layers at 5 mm spacing.  Visible but not dominant.
      */
      background-image:
        radial-gradient(circle, #888 0.65pt, transparent 0.65pt),
        radial-gradient(circle, #888 0.65pt, transparent 0.65pt);
      background-size:
        5mm 8.66mm,
        5mm 8.66mm;
      background-position:
        0 0,
        2.5mm 4.33mm;
    }

    /* ── Quote ──────────────────────────────────────────────────── */
    .calc-quote {
      position: absolute;
      top: 9mm;
      left: 50%;
      transform: translateX(-50%);
      width: fit-content;
      max-width: 85%;
      font-family: "PT Serif", serif;
      font-size: 8pt;
      font-style: italic;
      color: #666;
      line-height: 1.35;
      text-align: center;
      pointer-events: none;
      z-index: 0;
    }

    /* ── Header ─────────────────────────────────────────────────── */
    .calc-header {
      display: flex;
      align-items: baseline;
      gap: 3mm;
      margin-bottom: 6mm;
      padding-bottom: 2.5mm;
      border-bottom: 0.4pt solid #777;
      font-family: "PT Serif", serif;
      font-size: 7pt;
      color: #555;
      letter-spacing: 0.3pt;
      flex-shrink: 0;
    }
    .calc-header .field { display: flex; align-items: baseline; gap: 1.5mm; }
    .calc-header .field .label { font-style: italic; color: #666; }
    .calc-header .field .value {
      min-width: 18mm;
      border-bottom: 0.3pt solid #777;
      color: #555;
    }
    .calc-header .field.spacer { flex: 1; }

    /* ── Anchors area ───────────────────────────────────────────── */
    .anchors-area {
      position: relative;
      flex: 1;
      min-height: 0;
    }
    .anchor-row {
      display: flex;
      align-items: center;
      height: 0;
      margin-bottom: 45mm;   /* wider spacing — 3D problems need more room */
      position: relative;
    }
    .anchor-row:last-of-type { margin-bottom: 0; }

    .anchor-num {
      flex-shrink: 0;
      width: 6.5mm;
      height: 6.5mm;
      border-radius: 50%;
      border: 0.5pt solid #666;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: "PT Serif", serif;
      font-size: 7pt;
      font-weight: 700;
      color: #666;
      margin-right: 3mm;
    }

    .anchor-guide {
      flex: 1;
      border-top: 0.3pt dotted #888;
      margin: 0 2mm;
    }

    .anchor-answer {
      flex-shrink: 0;
      font-family: "PT Serif", serif;
      font-size: 6.5pt;
      color: #777;
      letter-spacing: 1pt;
      border: 0.35pt solid #777;
      border-radius: 2pt;
      padding: 1pt 2.5mm;
    }

    /* ── Fold guide ─────────────────────────────────────────────── */
    .fold-guide {
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      border-top: 0.35pt dashed #888;
      pointer-events: none;
    }
    .fold-guide::after {
      content: "half-page guide";
      position: absolute;
      right: 2mm;
      top: -3.5mm;
      font-family: "PT Serif", serif;
      font-size: 5.5pt;
      font-style: italic;
      color: #888;
      letter-spacing: 0.3pt;
      background: #fff;
      padding: 0 1mm;
    }

    /* ── Global reset ───────────────────────────────────────────── */
    .calc-pad, .calc-pad * { font-family: "PT Serif", serif; }

    /* ── Print ──────────────────────────────────────────────────── */
    @media print {
      .calc-pad {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
        color-adjust: exact;
      }
      .calc-pad * {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
    }
  </style>
</head>
<body>
"""

HTML_FOOT = """
</body>
</html>
"""

def generate():
    pages = []
    for i in range(1, 51):
        author, quote = QUOTES[(i - 1) % len(QUOTES)]
        pages.append(PAGE_BODY.format(
            author=html_mod.escape(author),
            quote=html_mod.escape(quote),
        ))

    with open("3d-geo-pad.html", "w") as f:
        f.write(HTML_HEAD)
        f.write("\n".join(pages))
        f.write(HTML_FOOT)

    print(f"Generated 3d-geo-pad.html — 50 pages, {len(QUOTES)} quotes.")

if __name__ == "__main__":
    generate()
