// validate.js — Extract KaTeX math from markdown and validate it by actually rendering it.
// - CLI: reads markdown from stdin, prints JSON to stdout (exit 1 if any error).
// - Module: validateMarkdown(md) returns an array of results (used by the MCP server).
const fs = require("fs");
const katex = require("katex");

function validateMarkdown(md) {
  const blocks = [];

  // display $$...$$
  for (const m of md.matchAll(/\$\$([\s\S]+?)\$\$/g))
    blocks.push({ kind: "display", tex: m[1], at: m.index });
  // display \[...\]
  for (const m of md.matchAll(/\\\[([\s\S]+?)\\\]/g))
    blocks.push({ kind: "display", tex: m[1], at: m.index });
  // inline $...$ (no whitespace adjacent to $, and not overlapping $$ — avoids false positives like currency)
  for (const m of md.matchAll(/(?<!\$)\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\$)/g))
    blocks.push({ kind: "inline", tex: m[1], at: m.index });
  // inline \(...\)
  for (const m of md.matchAll(/\\\(([\s\S]+?)\\\)/g))
    blocks.push({ kind: "inline", tex: m[1], at: m.index });

  blocks.sort((a, b) => a.at - b.at);

  return blocks.map((b) => {
    try {
      katex.renderToString(b.tex, { throwOnError: true });
      return { ok: true, kind: b.kind, at: b.at, tex: b.tex };
    } catch (e) {
      return {
        ok: false,
        kind: b.kind,
        at: b.at,
        tex: b.tex,
        error: e.message,
        position: e.position ?? null,
        length: e.length ?? null,
      };
    }
  });
}

module.exports = { validateMarkdown };

if (require.main === module) {
  const md = fs.readFileSync(0, "utf8");
  const results = validateMarkdown(md);
  console.log(JSON.stringify(results, null, 2));
  process.exit(results.some((r) => !r.ok) ? 1 : 0);
}
