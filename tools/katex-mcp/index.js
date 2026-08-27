// katex-mcp — validate_katex tool called by Continue (MCP)
// Runs inside the Docker image (katex-mcp:latest). KaTeX validation is done
// in-process using the real katex 0.18.4 installed in the same container.
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import validate from "./validate.cjs";

const { validateMarkdown } = validate;

const server = new Server(
  { name: "katex-validate", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "validate_katex",
      description:
        "Validate all KaTeX math ($...$, $$...$$, \\(...\\), \\[...\\]) in a markdown string by actually rendering it with KaTeX 0.18.4. Returns per-expression pass/fail with the error message and character position for each failure. Fix the invalid expressions and call this tool again until there are zero errors.",
      inputSchema: {
        type: "object",
        properties: {
          markdown: {
            type: "string",
            description: "The markdown text (including KaTeX math) to validate.",
          },
        },
        required: ["markdown"],
      },
    },
  ],
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name !== "validate_katex") {
    return {
      content: [{ type: "text", text: `Unknown tool: ${request.params.name}` }],
      isError: true,
    };
  }

  const markdown = request.params.arguments?.markdown ?? "";
  const results = validateMarkdown(markdown);

  const errors = results.filter((r) => !r.ok);
  const okCount = results.length - errors.length;
  const lines = [
    `KaTeX validation (katex 0.18.4): ${results.length} expression(s), ${okCount} passed, ${errors.length} error(s).`,
  ];

  if (errors.length === 0) {
    lines.push("All KaTeX expressions are valid.");
  } else {
    errors.forEach((e) => {
      const pos =
        e.position != null ? ` (position ${e.position}, length ${e.length})` : "";
      lines.push(`- [${e.kind}] offset ${e.at}${pos}: ${e.error}`);
      lines.push(`  expression: ${e.tex}`);
    });
    lines.push("Fix the errors above, then call the validation again.");
  }

  // Validation itself succeeded, so isError is false (the error list is returned as normal content)
  return {
    content: [{ type: "text", text: lines.join("\n") }],
    isError: false,
  };
});

await server.connect(new StdioServerTransport());
