#!/usr/bin/env node
// pdfgen.js — Markdown → PDF (marked + KaTeX + Puppeteer)
// 사용법: node pdfgen.js <input.md> [output.pdf]

const { readFileSync, writeFileSync } = require('fs');
const { resolve, dirname, basename, extname } = require('path');
const { marked } = require('marked');
const katex = require('katex');
const puppeteer = require('puppeteer');

// ── 인자 처리 ──
const inputPath = resolve(process.argv[2]);
const outputPath = process.argv[3]
    ? resolve(process.argv[3])
    : inputPath.replace(/\.md$/, '.pdf');

if (!inputPath) {
    console.error('사용법: node pdfgen.js <input.md> [output.pdf]');
    process.exit(1);
}

// ── KaTeX → HTML 변환 ($$...$$, $...$) ──
function renderMath(md) {
    let result = md;

    // 블록 수식 $$...$$
    result = result.replace(/\$\$([\s\S]*?)\$\$/g, (_, tex) => {
        try {
            return katex.renderToString(tex.trim(), {
                displayMode: true,
                throwOnError: false,
            });
        } catch {
            return `<pre>${tex}</pre>`;
        }
    });

    // 인라인 수식 $...$ ($$는 제외)
    result = result.replace(/(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)/g, (_, tex) => {
        try {
            return katex.renderToString(tex.trim(), {
                displayMode: false,
                throwOnError: false,
            });
        } catch {
            return `<code>${tex}</code>`;
        }
    });

    return result;
}

// ── Markdown → HTML ──
const mdContent = readFileSync(inputPath, 'utf-8');
const withMath = renderMath(mdContent);

// marked 설정: KaTeX로 변환된 HTML을 그대로 보존
const htmlBody = marked.parse(withMath, {
    breaks: false,
});

// ── 완성 HTML ──
const katexCss = readFileSync(
    require.resolve('katex/dist/katex.min.css'),
    'utf-8'
);

const fullHtml = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
${katexCss}
body {
    font-family: "Noto Sans CJK KR", "Noto Sans SC", sans-serif;
    font-size: 12pt;
    line-height: 1.8;
    color: #1a1a1a;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px 30px;
}
h1 { font-size: 1.8em; border-bottom: 2px solid #333; padding-bottom: 6px; margin-top: 1.2em; }
h2 { font-size: 1.4em; border-bottom: 1px solid #999; padding-bottom: 4px; margin-top: 1em; }
h3 { font-size: 1.15em; margin-top: 0.8em; }
p { margin: 0.5em 0; }
code {
    background: #f4f4f4;
    padding: 2px 5px;
    border-radius: 3px;
    font-size: 0.92em;
}
pre {
    background: #f4f4f4;
    padding: 10px 14px;
    border-radius: 5px;
    overflow-x: auto;
}
blockquote {
    border-left: 3px solid #ccc;
    padding-left: 12px;
    color: #555;
    margin-left: 0;
}
hr { border: none; border-top: 1px solid #ddd; margin: 1.5em 0; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; }
th, td { border: 1px solid #ccc; padding: 6px 10px; text-align: left; }
th { background: #f0f0f0; }
.katex { font-size: 1.05em; }
.katex-display { margin: 0.8em 0; }
</style>
</head>
<body>
${htmlBody}
</body>
</html>`;

// ── Puppeteer PDF 생성 ──
(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
        ],
    });

    const page = await browser.newPage();
    await page.setContent(fullHtml, {
        waitUntil: 'networkidle0',
        timeout: 30000,
    });

    await page.pdf({
        path: outputPath,
        format: 'A4',
        margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' },
        printBackground: true,
    });

    await browser.close();
    console.log(`✅ 완료: ${outputPath}`);
})();
