#!/usr/bin/env node
// math/tools/build.mjs — 그래프 렌더 + 마크다운 태그 치환
//
// ── 하는 일 ────────────────────────────────────────────────────
//   ① math/graph/ 의 logos 스케치(*.mjs)를 렌더 → math/graphs/  (SVG/PNG/manifest)
//   ② math/sessions/**/*.md 의 `{{graph:<id>}}` 태그를, 렌더 산출물을 가리키는
//      **상대경로**로 치환해 math/build/rendered/ 에 기록한다(원본 md 는 불변).
//
// ── 사용 ───────────────────────────────────────────────────────
//   node math/tools/build.mjs                 # 렌더 + 치환 (기본)
//   node math/tools/build.mjs --no-render      # 이미 렌더된 그래프로 치환만
//   node math/tools/build.mjs --no-png         # 렌더 시 PNG 생략
//   node math/tools/build.mjs --scale 2        # 렌더 PNG 배율
//
// ── 태그 규약 ─────────────────────────────────────────────────
//   ![alt]({{graph:<id>}})      <id> = 스케치의 figures 키 = 출력 파일명(확장자 제외)
//   렌더 결과가 없거나 종료코드가 0 이 아니면, 미해결 태그를 보고하고 종료코드 1.
import { readdirSync, readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, join, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const HERE = dirname(fileURLToPath(import.meta.url));
const MATH = resolve(HERE, '..');                    // math/
const GRAPH_DIR = join(MATH, 'graph');               // 스케치 소스
const GRAPHS_DIR = join(MATH, 'graphs');             // 렌더 산출물 (gitignore)
const SESSIONS_DIR = join(MATH, 'sessions');         // 세션 마크다운
const OUT_DIR = join(MATH, 'build', 'rendered');     // 치환된 md (gitignore)
const LOGOS_BIN = join(GRAPH_DIR, 'node_modules', '@jaywoo0830a', 'logos', 'bin', 'logos.mjs');

// ── CLI 파서 ───────────────────────────────────────────────────
const argv = process.argv.slice(2);
const opt = { render: true, png: true, scale: null, strict: false, help: false };
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--no-render') opt.render = false;
  else if (a === '--no-png') opt.png = false;
  else if (a === '--strict') opt.strict = true;
  else if (a === '--scale') opt.scale = Number(argv[++i]);
  else if (a === '-h' || a === '--help') opt.help = true;
  else { console.error(`알 수 없는 옵션: ${a}`); process.exit(2); }
}
if (opt.help) {
  console.log(readFileSync(new URL(import.meta.url)).toString().split('\n').slice(1, 20).join('\n'));
  process.exit(0);
}

const log = (...a) => console.log(...a);

// ── ① 렌더 ─────────────────────────────────────────────────────
if (opt.render) {
  if (!existsSync(LOGOS_BIN)) {
    console.error(`✗ logos 가 설치되지 않았습니다: ${LOGOS_BIN}`);
    console.error('  먼저 설치하세요 →  cd math/graph && npm install');
    process.exit(1);
  }
  const args = [LOGOS_BIN, 'render', GRAPH_DIR, '--recursive', '--out', GRAPHS_DIR];
  if (!opt.png) args.push('--no-png');
  if (opt.scale) args.push('--scale', String(opt.scale));
  log(`▶ 렌더: logos render ${relative(MATH, GRAPH_DIR)} --recursive --out ${relative(MATH, GRAPHS_DIR)}`);
  const r = spawnSync(process.execPath, args, { stdio: 'inherit' });
  if (r.status !== 0) { console.error(`✗ 렌더 실패 (exit ${r.status})`); process.exit(r.status || 1); }
}

// ── ② manifest 로 유효 id 확보 ─────────────────────────────────
const manifestPath = join(GRAPHS_DIR, 'manifest.json');
if (!existsSync(manifestPath)) {
  console.error(`✗ manifest 가 없습니다: ${manifestPath} (렌더를 먼저 실행하세요)`);
  process.exit(1);
}
const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
const known = new Set((manifest.figures || []).map((f) => f.name));
log(`▶ 렌더된 figure ${known.size}개 (실패 ${manifest.fail ?? '?'})`);

// ── ③ md 수집 (재귀) ───────────────────────────────────────────
/**
 * alt 텍스트에 ']' 가 있어 이미지 문법이 깨진 줄을 찾는다.
 *
 *   정상: ![alt](url)      ← 첫 ']' 다음 글자가 '('
 *   깨짐: ![range (0, 1]](url)  ← alt 안의 ']' 가 먼저 닫혀 다음 글자가 ']'/'b' …
 *
 * (정규식 `[^\]]*` 는 개행까지 삼켜 오탐하므로, 줄 단위로 직접 스캔한다.)
 * @returns {{ln:number, alt:string}[]}
 */
function findBrokenAlts(text) {
  const out = [];
  text.split('\n').forEach((line, i) => {
    let from = 0;
    while ((from = line.indexOf('![', from)) !== -1) {
      const close = line.indexOf(']', from + 2);
      if (close === -1) break;
      if (line[close + 1] !== '(') out.push({ ln: i + 1, alt: line.slice(from, close + 1) });
      from = close + 1;
    }
  });
  return out;
}

function walk(dir, acc = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) walk(p, acc);
    else if (e.isFile() && e.name.endsWith('.md')) acc.push(p);
  }
  return acc;
}

const TAG = /\{\{graph:\s*([^}\s]+)\s*\}\}/g;
let files = 0, replaced = 0;
const missing = new Set();
const legacy = new Map();
const badAlt = new Map();   // alt 텍스트에 ']' 가 있어 이미지 문법이 깨지는 줄

for (const src of walk(SESSIONS_DIR)) {
  const rel = relative(MATH, src);                        // 예: sessions/phase2/11C-....md
  const outFile = join(OUT_DIR, rel);
  let text = readFileSync(src, 'utf8');

  text = text.replace(TAG, (m, id) => {
    if (!known.has(id)) { missing.add(id); return m; }
    // 렌더본 위치 기준 상대경로 → ../../../../graphs/<id>.svg
    const target = join(GRAPHS_DIR, `${id}.svg`);
    const relPath = relative(dirname(outFile), target).split('\\').join('/');
    replaced++;
    return relPath;
  });

  // (참고) 아직 태그로 바뀌지 않은 옛 이미지 참조 수집 — 빌드 로그용
  const legacyCount = (text.match(/\]\((?:\.\.\/)*graphs\/[^)]*\.png\)/g) || []).length;
  if (legacyCount) legacy.set(rel, legacyCount);

  // alt 텍스트에 ']' 가 있으면 마크다운 이미지 문법이 조기에 닫혀 렌더되지 않는다.
  //   예) ![sech x — even, range (0, 1]](url)   ← '(0, 1]' 의 ']' 가 문제
  const broken = findBrokenAlts(text);
  if (broken.length) badAlt.set(rel, broken);

  mkdirSync(dirname(outFile), { recursive: true });
  writeFileSync(outFile, text);
  files++;
}

// ── ④ 보고 ─────────────────────────────────────────────────────
log(`▶ md ${files}개 → ${relative(MATH, OUT_DIR)}  (태그 ${replaced}개 치환)`);
if (legacy.size) {
  const total = [...legacy.values()].reduce((a, b) => a + b, 0);
  log(`  · 아직 태그가 아닌 옛 이미지 참조 ${total}개 (${legacy.size}개 세션) — 순차 이관 대상`);
}
if (badAlt.size) {
  const total = [...badAlt.values()].reduce((a, b) => a + b.length, 0);
  const stream = opt.strict ? console.error : console.warn;
  stream(`${opt.strict ? '✗' : '!'} 깨진 이미지 alt ${total}개 (${badAlt.size}개 세션) — alt 안의 ']' 때문에 그 이미지가 렌더되지 않습니다:`);
  let shown = 0;
  for (const [f, arr] of badAlt) {
    for (const { ln, alt } of arr) {
      if (shown++ >= 12) break;
      stream(`    ${f}:${ln}  ${alt}…`);
    }
    if (shown >= 12) break;
  }
  if (opt.strict) process.exit(1);
}
if (missing.size) {
  // 점진 이관: 아직 이관하지 않은 세션의 태그는 남아 있을 수 있다.
  // 기본은 경고, `--strict`(CI) 에서만 실패로 만든다.
  const head = [...missing].slice(0, 12).join(', ');
  const more = missing.size > 12 ? ` … (+${missing.size - 12})` : '';
  const stream = opt.strict ? console.error : console.warn;
  stream(`${opt.strict ? '✗' : '!'} 미해결 태그 ${missing.size}개: ${head}${more}`);
  stream('  → math/graph 에 해당 id 를 export 하는 스케치가 있는지 확인하세요.');
  if (opt.strict) process.exit(1);
}
log('✓ 완료');
