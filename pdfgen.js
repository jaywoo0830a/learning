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
    breaks: true,
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

/* ── 기본 ── */
body {
    font-family: "Noto Sans CJK KR", "Noto Sans SC", sans-serif;
    font-size: 11.5pt;
    line-height: 1.9;
    color: #1e1e1e;
    max-width: 780px;
    margin: 0 auto;
    padding: 30px 35px;
    word-break: keep-all;
}

/* ── 제목 ── */
h1 {
    font-size: 1.7em;
    text-align: center;
    border-bottom: 2.5px solid #222;
    padding-bottom: 10px;
    margin: 0 0 1.0em 0;
    letter-spacing: -0.02em;
}
h2 {
    font-size: 1.25em;
    color: #222;
    border-left: 4px solid #4a90d9;
    padding: 6px 0 6px 12px;
    margin: 1.4em 0 0.6em 0;
    background: #f7f9fc;
    border-radius: 0 4px 4px 0;
}
h3 {
    font-size: 1.08em;
    color: #333;
    margin: 1.1em 0 0.4em 0;
}

/* ── 본문 ── */
p {
    margin: 0.4em 0;
    text-indent: 0;
}
p + p {
    margin-top: 0.25em;
}

/* 강조 */
strong {
    color: #c0392b;
    font-weight: 700;
}

/* ── 구분선 ── */
hr {
    border: none;
    height: 0;
    margin: 1.6em 0;
    text-align: center;
}
hr::after {
    content: "· · ·";
    color: #bbb;
    font-size: 1.2em;
    letter-spacing: 0.4em;
}

/* ── 인라인 코드 ── */
code {
    background: #f0f0f0;
    padding: 1px 6px;
    border-radius: 3px;
    font-size: 0.94em;
    font-family: "JetBrains Mono", "Consolas", monospace;
    color: #333;
}

/* ── 코드 블록 ── */
pre {
    background: #f5f5f5;
    padding: 12px 16px;
    border-radius: 6px;
    overflow-x: auto;
    border: 1px solid #e0e0e0;
    margin: 0.7em 0;
}

/* ── 인용 ── */
blockquote {
    border-left: 4px solid #4a90d9;
    background: #f0f4f8;
    padding: 8px 14px;
    margin: 0.8em 0;
    color: #444;
    border-radius: 0 4px 4px 0;
}

/* ── 표 ── */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.9em 0;
    font-size: 0.95em;
}
th, td {
    border: 1px solid #ddd;
    padding: 7px 12px;
    text-align: left;
}
th {
    background: #eef2f7;
    font-weight: 700;
}
tr:nth-child(even) td {
    background: #fafbfc;
}

/* ── KaTeX ── */
.katex {
    font-size: 1.08em;
}
.katex-display {
    margin: 0.9em 0;
    padding: 4px 0;
}
.katex-display > .katex {
    font-size: 1.1em;
}

/* ── 리스트 ── */
ul, ol {
    padding-left: 1.5em;
    margin: 0.4em 0;
}
li {
    margin: 0.2em 0;
}

/* ── 인쇄 최적화 ── */
@page {
    size: A4;
    margin: 20mm 15mm;
}
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
