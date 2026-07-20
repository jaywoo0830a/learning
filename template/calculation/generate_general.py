#!/usr/bin/env python3
"""Generate general-pad.html — 50-page calculation pad for general STEM problem-solving.
   Darker colours tuned for print visibility."""

import html as html_mod

QUOTES = [
    ("Isaac Newton", "If I have seen further, it is by standing on the shoulders of giants."),
    ("Albert Einstein", "Imagination is more important than knowledge."),
    ("Richard Feynman", "The first principle is that you must not fool yourself — and you are the easiest person to fool."),
    ("Carl Friedrich Gauss", "Mathematics is the queen of the sciences, and number theory is the queen of mathematics."),
    ("Henri Poincaré", "The scientist does not study nature because it is useful; he studies it because he delights in it."),
    ("Marie Curie", "Nothing in life is to be feared, it is only to be understood."),
    ("Galileo Galilei", "The book of nature is written in the language of mathematics."),
    ("Johannes Kepler", "I much prefer the sharpest criticism of a single intelligent man to the thoughtless approval of the masses."),
    ("Niels Bohr", "Prediction is very difficult, especially about the future."),
    ("Werner Heisenberg", "What we observe is not nature itself, but nature exposed to our method of questioning."),
    ("Paul Dirac", "A physical law must possess mathematical beauty."),
    ("John von Neumann", "If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is."),
    ("Alan Turing", "We can only see a short distance ahead, but we can see plenty there that needs to be done."),
    ("Emmy Noether", "My methods are really methods of working and thinking; this is why they have crept in everywhere anonymously."),
    ("Leonardo da Vinci", "Simplicity is the ultimate sophistication."),
    ("Archimedes", "Give me a place to stand, and I shall move the earth."),
    ("Euclid", "There is no royal road to geometry."),
    ("Gottfried Wilhelm Leibniz", "The present is big with the future."),
    ("Leonhard Euler", "Logic is the foundation of the certainty of all the knowledge we acquire."),
    ("Joseph-Louis Lagrange", "As long as algebra and geometry have been separated, their progress has been slow and their uses limited."),
    ("Pierre-Simon Laplace", "What we know is not much. What we do not know is immense."),
    ("James Clerk Maxwell", "Thoroughly conscious ignorance is the prelude to every real advance in science."),
    ("Michael Faraday", "Nothing is too wonderful to be true, if it be consistent with the laws of nature."),
    ("Ludwig Boltzmann", "If you are out to describe the truth, leave elegance to the tailor."),
    ("Erwin Schrödinger", "The task is not to see what has never been seen, but to think what has never been thought."),
    ("Max Planck", "Science cannot solve the ultimate mystery of nature. And that is because, in the last analysis, we ourselves are part of the mystery we are trying to solve."),
    ("Enrico Fermi", "There are two possible outcomes: if the result confirms the hypothesis, then you have made a measurement. If the result is contrary to the hypothesis, then you have made a discovery."),
    ("David Hilbert", "We must know. We will know."),
    ("Bernhard Riemann", "The value of mathematical science is measured by the progress it brings about in our understanding of the physical world."),
    ("Évariste Galois", "Unfortunately what is little recognized is that the most worthwhile scientific works are those in which the author points out what he does not know."),
    ("Blaise Pascal", "We are generally the better persuaded by the reasons we discover ourselves than by those given to us by others."),
    ("René Descartes", "Each problem that I solved became a rule which served afterwards to solve other problems."),
    ("Kurt Gödel", "The more I think about language, the more it amazes me that people ever understand each other at all."),
    ("Ada Lovelace", "That brain of mine is something more than merely mortal; as time will show."),
    ("Srinivasa Ramanujan", "An equation for me has no meaning unless it expresses a thought of God."),
    ("George Pólya", "If you cannot solve the proposed problem, try to solve first some related problem."),
    ("G. H. Hardy", "A mathematician, like a painter or a poet, is a maker of patterns."),
    ("John Archibald Wheeler", "If you are not completely confused by quantum mechanics, you do not understand it."),
    ("Steven Weinberg", "The effort to understand the universe is one of the very few things that lifts human life a little above the level of farce."),
    ("Roger Penrose", "Sometimes it is the people no one can imagine anything of who do the things no one can imagine."),
    ("Terence Tao", "Mathematics is a game of ideas. The more ideas you have, the richer the game becomes."),
    ("Maryam Mirzakhani", "I find it fascinating that you can look at the same problem from different perspectives and approach it using different methods."),
    ("Subrahmanyan Chandrasekhar", "Science is a perception of the world around us. Science is a place where what you find in nature pleases you."),
    ("Freeman Dyson", "The essential fact which emerges is that the three smallest and most active reservoirs of carbon are the atmosphere, the biosphere, and the human population."),
    ("Claude Shannon", "I visualize a time when we will be to robots what dogs are to humans, and I am rooting for the machines."),
    ("Norbert Wiener", "The world of the future will be an ever more demanding struggle against the limitations of our intelligence."),
    ("Grace Hopper", "The most dangerous phrase in the language is: we have always done it this way."),
    ("Dennis Ritchie", "UNIX is simple. It just takes a genius to understand its simplicity."),
    ("Donald Knuth", "The most important thing in the programming language is the name. A language will not succeed without a good name."),
    ("Edsger W. Dijkstra", "Simplicity is a great virtue but it requires hard work to achieve it and education to appreciate it."),
    ("Alan Kay", "The best way to predict the future is to invent it."),
    ("Barbara Liskov", "The power of abstraction is that it allows you to ignore the details you do not need to know."),
    ("Stephen Hawking", "Look up at the stars and not down at your feet. Try to make sense of what you see."),
    ("Carl Sagan", "Somewhere, something incredible is waiting to be known."),
    ("Neil deGrasse Tyson", "The good thing about science is that it is true whether or not you believe in it."),
]

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
      <div class="anchor-row"><div class="anchor-num">3</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>

      <div class="fold-guide"></div>

      <div class="anchor-row"><div class="anchor-num">4</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>
      <div class="anchor-row"><div class="anchor-num">5</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>
      <div class="anchor-row" style="margin-bottom:0;"><div class="anchor-num">6</div><div class="anchor-guide"></div><div class="anchor-answer">Ans</div></div>

    </div>

    <div class="hai-page-number">&mdash; {page_num} &mdash;</div>

  </section>
"""

HTML_HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>General Problem-Solving Pad</title>

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
      /* 5 mm square dot grid — visible on textured paper without dominating */
      background-image:
        radial-gradient(circle, #888 0.65pt, transparent 0.65pt);
      background-size: 5mm 5mm;
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
      margin-bottom: 38mm;
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
      font-size: 8pt;
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

    /* ── Page number ────────────────────────────────────────────── */
    .calc-pad .hai-page-number {
      font-family: "PT Serif", serif;
      font-size: 7pt;
      color: #888;
      font-style: italic;
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
            page_num=i,
            author=html_mod.escape(author),
            quote=html_mod.escape(quote),
        ))

    with open("general-pad.html", "w") as f:
        f.write(HTML_HEAD)
        f.write("\n".join(pages))
        f.write(HTML_FOOT)

    print(f"Generated general-pad.html — 50 pages, {len(QUOTES)} quotes.")

if __name__ == "__main__":
    generate()
