# katex-mcp — packages the Continue (MCP) server plus real KaTeX validation into a single container
# Build (from the workspace root): docker build -t katex-mcp:latest -f tools/katex-mcp/Dockerfile .
# Run: docker run --rm -i katex-mcp:latest   (speaks the MCP stdio protocol over stdin/stdout)
FROM node:20-alpine

WORKDIR /app
COPY tools/katex-mcp/package.json ./
RUN npm install --omit=dev

# Reuse katex-validate/validate.js as the single source of truth for the validation logic
# (this package is type:module, so the CJS module is copied with a .cjs extension)
COPY katex-validate/validate.js ./validate.cjs
COPY tools/katex-mcp/index.js ./index.js

ENTRYPOINT ["node", "index.js"]
