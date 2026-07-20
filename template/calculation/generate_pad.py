#!/usr/bin/env python3
"""Generate a 50-page calculation pad HTML file with scholarly quotes."""

import html as html_mod

# ── Quotes (50+ scholars) ──────────────────────────────────────────────
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

# ── Page body template ─────────────────────────────────────────────────
PAGE_TEMPLATE = """  <!-- ====================================================================
       PAGE {page_num}
       ==================================================================== -->
  <section class="hai-page calc-pad">

    <!-- QUOTE -->
    <div class="calc-quote">&ldquo;{quote}&rdquo; &mdash; {author}</div>

    <!-- HEADER -->
    <div class="calc-header">
      <div class="field">
        <span class="label">Date</span>
        <span class="value"></span>
      </div>
      <div class="field">
        <span class="label">Subject</span>
        <span class="value" style="min-width:22mm;"></span>
      </div>
      <div class="field">
        <span class="label">Topic</span>
        <span class="value" style="min-width:28mm;"></span>
      </div>
      <div class="field spacer"></div>
      <div class="field">
        <span class="label">p.</span>
        <span class="value" style="min-width:8mm;text-align:right;"></span>
      </div>
    </div>

    <!-- ANCHOR ROWS -->
    <div class="anchors-area" style="position:relative;">

      <div class="anchor-row">
        <div class="anchor-num">1</div>
        <div class="anchor-guide"></div>
        <div class="anchor-answer">Ans</div>
      </div>
      <div class="anchor-row">
        <div class="anchor-num">2</div>
        <div class="anchor-guide"></div>
        <div class="anchor-answer">Ans</div>
      </div>
      <div class="anchor-row">
        <div class="anchor-num">3</div>
        <div class="anchor-guide"></div>
        <div class="anchor-answer">Ans</div>
      </div>

      <div class="fold-guide"></div>

      <div class="anchor-row">
        <div class="anchor-num">4</div>
        <div class="anchor-guide"></div>
        <div class="anchor-answer">Ans</div>
      </div>
      <div class="anchor-row">
        <div class="anchor-num">5</div>
        <div class="anchor-guide"></div>
        <div class="anchor-answer">Ans</div>
      </div>
      <div class="anchor-row" style="margin-bottom:0;">
        <div class="anchor-num">6</div>
        <div class="anchor-guide"></div>
        <div class="anchor-answer">Ans</div>
      </div>

      <div class="iso-mini">
        <span class="iso-mini-label">3 mm iso grid</span>
      </div>

    </div><!-- /.anchors-area -->

    <!-- PAGE NUMBER -->
    <div class="hai-page-number">&mdash; {page_num} &mdash;</div>

  </section><!-- /.hai-page -->
"""

# ── CSS for the quote line ─────────────────────────────────────────────
QUOTE_CSS = """    /* =====================================================================
       QUOTE — absolutely positioned in the top margin, never affects layout.
       Regardless of quote length (1–3 lines), the header and anchors
       remain fixed in place.  Faint enough not to distract from writing.
       ===================================================================== */
    .calc-quote {
      position: absolute;
      top: 9mm;                         /* sits inside the 20 mm top padding */
      left: 50%;
      transform: translateX(-50%);
      width: fit-content;
      max-width: 85%;                   /* prevent overflow on very long quotes */
      font-family: "PT Serif", serif;
      font-size: 6.5pt;
      font-style: italic;
      color: #d0d0d0;
      line-height: 1.35;
      text-align: center;
      pointer-events: none;             /* does not interfere with selection */
      z-index: 0;
    }
"""

# ── Assemble the full HTML ─────────────────────────────────────────────
def generate():
    # Collect pages
    pages = []
    for i in range(1, 51):
        author, quote = QUOTES[(i - 1) % len(QUOTES)]
        page_html = PAGE_TEMPLATE.format(
            page_num=i,
            author=html_mod.escape(author),
            quote=html_mod.escape(quote),
        )
        pages.append(page_html)

    all_pages = "\n".join(pages)

    # Read the current file to extract the <head> up to (but not including) </style>
    with open("flow-grid-pad.html", "r") as f:
        existing = f.read()

    # Split at </style> — keep everything before it as the head prefix
    style_end = existing.find("  </style>")
    if style_end == -1:
        print("ERROR: Could not find </style> in the HTML file.")
        return
    head_prefix = existing[:style_end]

    # The suffix after </style> is </head>\n<body>\n...
    # We need to find where the body content ends and the closing tags are
    body_start = existing.find("<body>")
    # Everything from </style> to <body> (exclusive) is the head tail
    head_tail = existing[style_end:body_start]

    # Build the final HTML
    output = f"""{head_prefix}
{QUOTE_CSS}
    /* =====================================================================
       GLOBAL RESET within calc-pad — keep PT Serif everywhere
       ===================================================================== */
    .calc-pad,
    .calc-pad * {{
      font-family: "PT Serif", serif;
    }}

    /* =====================================================================
       PRINT — ensure dot grid and all faint elements print correctly
       ===================================================================== */
    @media print {{
      .calc-pad {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
        color-adjust: exact;
      }}
      .calc-pad * {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }}
    }}
  </style>
</head>
<body>

{all_pages}

</body>
</html>
"""

    with open("flow-grid-pad.html", "w") as f:
        f.write(output)

    print(f"Generated flow-grid-pad.html with 50 pages ({len(QUOTES)} unique quotes).")

if __name__ == "__main__":
    generate()
