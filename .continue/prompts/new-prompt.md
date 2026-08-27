---
name: Validate and fix KaTeX
description: Validate all KaTeX math in the selected text/file by real rendering and fix any errors.
invokable: true
---

Validate and fix all KaTeX math in the text provided below (or the current selection).

1. Find every KaTeX expression in the text ($...$, $$...$$, \(...\), \[...\]).
2. Call the `validate_katex` tool (MCP) to validate it with real rendering.
3. Fix any invalid expressions using the reported errors (including character positions).
4. Repeat steps 2–3 until there are zero errors.
5. Output the full corrected text, containing only expressions that passed validation.