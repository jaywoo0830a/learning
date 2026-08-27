---
name: KaTeX validation
description: Validate KaTeX math in markdown answers by real rendering and fix any errors.
alwaysApply: true
---

After writing KaTeX math ($...$, $$...$$, \(...\), \[...\]) in markdown, you MUST call the `validate_katex` tool (MCP) to validate it with real rendering.

- Fix invalid expressions using the reported errors (including character positions).
- Repeat the validation call until there are zero errors.
- The final answer must contain only expressions that passed validation.
- Use only KaTeX-supported syntax. Display environments (align, cases, matrix, etc.) must be written inside $$...$$ only.