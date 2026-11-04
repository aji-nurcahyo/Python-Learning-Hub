/**
 * Automated Presentation Quality, Branding & Layout Validator
 * Python Learning Hub
 */

import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';
import http from 'http';

const ROOT = process.cwd();
const CANONICAL_TITLES = {
  1: 'Introduction to Python',
  2: 'Variables & Data Types',
  3: 'Operators & Expressions',
  4: 'Input & Output',
  5: 'Conditional Statements',
  6: 'Loops & Iteration',
  7: 'Strings & Text Processing',
  8: 'Lists, Tuples & Sequences',
  9: 'Dictionaries, Sets & Hash Structures',
  10: 'Functions & Scope',
  11: 'Modules & Basic Exceptions',
  12: 'Foundations Capstone Project',
  13: 'Advanced Functions',
  14: 'Comprehensions & Iterators',
  15: 'Searching & Sorting Algorithms',
  16: 'Algorithm Analysis & Problem Solving',
  17: 'File Handling & Data Serialization',
  18: 'Exception Handling & Debugging',
  19: 'Object-Oriented Programming I',
  20: 'Object-Oriented Programming II',
  21: 'Packages, Environments & Testing',
  22: 'Intermediate Capstone Project',
  23: 'Advanced OOP & Design Patterns',
  24: 'Decorators, Generators & Context Managers',
  25: 'Type Hints & Code Quality',
  26: 'Advanced Testing & Logging',
  27: 'Concurrent & Asynchronous Programming',
  28: 'Networking & API Integration',
  29: 'Software Architecture & Deployment',
  30: 'Professional Capstone Project'
};

const FORBIDDEN_BRANDING_TERMS = [
  /\bpertemuan\s*\d+/i,
  /\bpengantar komputasi\b/i,
  /\bpengenalan komputasi\b/i,
  /\balgoritma dan pemrograman\b/i,
  /\balpro\b/i,
  /\bprogram studi teknik telekomunikasi\b/i,
  /\bfakultas teknologi industri\b/i
];

console.log('====================================================');
console.log('PYTHON LEARNING HUB — PRESENTATION AUDIT & VALIDATION');
console.log('====================================================\n');

let staticErrors = 0;
let totalDecks = 0;
let totalSlides = 0;

// 1. Static Audit of All Slide Decks
console.log('▶ [1/2] Auditing Slide Decks & Branding Metadata...');

const outputsPath = path.join(ROOT, 'src/code/outputs.json');
const outputs = fs.existsSync(outputsPath) ? JSON.parse(fs.readFileSync(outputsPath, 'utf8')) : {};

for (let ch = 1; ch <= 30; ch++) {
  const chStr = String(ch).padStart(2, '0');
  const levelFolder = ch <= 12 ? 'foundations' : ch <= 22 ? 'intermediate' : 'professional';
  const deckPath = path.join(ROOT, `content/${levelFolder}/chapter-${chStr}/slides/deck.json`);

  if (!fs.existsSync(deckPath)) {
    console.error(`❌ Chapter ${chStr}: deck.json missing at ${deckPath}`);
    staticErrors++;
    continue;
  }

  totalDecks++;
  let slides = [];
  try {
    slides = JSON.parse(fs.readFileSync(deckPath, 'utf8'));
  } catch (err) {
    console.error(`❌ Chapter ${chStr}: Invalid JSON in deck.json (${err.message})`);
    staticErrors++;
    continue;
  }

  totalSlides += slides.length;

  // Cover slide verification
  if (slides.length === 0 || slides[0].kind !== 'cover') {
    console.error(`❌ Chapter ${chStr}: Slide 1 must have kind: "cover"`);
    staticErrors++;
  } else {
    const cover = slides[0];
    const expectedTitle = CANONICAL_TITLES[ch];
    if (expectedTitle && cover.title.toLowerCase() !== expectedTitle.toLowerCase()) {
      console.warn(`⚠️ Chapter ${chStr}: Cover title "${cover.title}" differs from canonical "${expectedTitle}"`);
    }
  }

  // Scan every slide for forbidden terms & code assets
  slides.forEach((s, idx) => {
    const slideNum = idx + 1;
    const fullText = `${s.title || ''} ${s.body || ''} ${s.notes || ''} ${s.question || ''} ${s.answer || ''}`;

    for (const pattern of FORBIDDEN_BRANDING_TERMS) {
      if (pattern.test(fullText)) {
        console.error(`❌ Chapter ${chStr} Slide ${slideNum} ("${s.title}") contains forbidden branding: ${pattern}`);
        staticErrors++;
      }
    }

    if (s.example) {
      const codePath = path.join(ROOT, `src/code/${s.example}.py`);
      if (!fs.existsSync(codePath) && !s.files) {
        console.error(`❌ Chapter ${chStr} Slide ${slideNum}: Example script missing: ${codePath}`);
        staticErrors++;
      }
      if (!outputs[s.example] && outputs[s.example] !== '') {
        console.warn(`⚠️ Chapter ${chStr} Slide ${slideNum}: Missing output cache for ${s.example}`);
      }
    }

    if (s.dependency) {
      const depPath = path.join(ROOT, `public/downloads/examples/${s.dependency}`);
      if (!fs.existsSync(depPath)) {
        console.error(`❌ Chapter ${chStr} Slide ${slideNum}: Dependency file missing: ${depPath}`);
        staticErrors++;
      }
    }
  });

  console.log(`   ✓ Chapter ${chStr}: ${slides.length} slides validated.`);
}

console.log(`\nStatic Audit Summary: ${totalDecks} decks, ${totalSlides} slides inspected. Errors: ${staticErrors}\n`);

// 2. DOM Rendering & Geometry Validation
async function fetchJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); } catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const browserExe = fs.existsSync(CHROME_PATH) ? CHROME_PATH : (fs.existsSync(EDGE_PATH) ? EDGE_PATH : null);

if (!browserExe) {
  console.log('ℹ️ Headless Chrome/Edge not found. Skipping live DOM geometry checks.');
  if (staticErrors > 0) process.exit(1);
  process.exit(0);
}

// Check if dev server is running on port 8932
async function checkServer() {
  return new Promise(resolve => {
    http.get('http://127.0.0.1:8932/', (res) => resolve(res.statusCode === 200)).on('error', () => resolve(false));
  });
}

const isServerUp = await checkServer();
if (!isServerUp) {
  console.log('ℹ️ Local server on port 8932 not reachable. Skipping live DOM geometry checks.');
  if (staticErrors > 0) process.exit(1);
  process.exit(0);
}

console.log('▶ [2/2] Running Live Browser Geometry & Layout Validation...');
const PORT = 9224;
const browserProc = spawn(browserExe, [
  '--headless=new',
  `--remote-debugging-port=${PORT}`,
  '--disable-gpu',
  '--no-sandbox',
  '--window-size=1920,1080',
  'about:blank'
], { stdio: 'ignore' });

let targetWs = null;
for (let i = 0; i < 20; i++) {
  await new Promise(r => setTimeout(r, 250));
  try {
    const list = await fetchJson(`http://127.0.0.1:${PORT}/json/list`);
    const page = list.find(t => t.type === 'page');
    if (page) {
      targetWs = page.webSocketDebuggerUrl;
      break;
    }
  } catch {
    // retry
  }
}

if (!targetWs) {
  console.error('❌ Could not connect to headless browser CDP. Skipping layout test.');
  browserProc.kill();
  if (staticErrors > 0) process.exit(1);
  process.exit(0);
}

const ws = new WebSocket(targetWs);
await new Promise(resolve => ws.onopen = resolve);

let msgId = 1;
function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = msgId++;
    const handler = (evt) => {
      const res = JSON.parse(evt.data);
      if (res.id === id) {
        ws.removeEventListener('message', handler);
        if (res.error) reject(res.error);
        else resolve(res.result);
      }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

async function safeEval(params, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await send('Runtime.evaluate', params);
    } catch (err) {
      if (err?.code === -32000 && attempt < maxRetries) {
        await new Promise((r) => setTimeout(r, 250));
        continue;
      }
      throw err;
    }
  }
}

await send('Page.enable');

const testResolutions = [
  { w: 1920, h: 1080, name: '1920x1080 (Full HD)' },
  { w: 1366, h: 768,  name: '1366x768 (Laptop)' },
  { w: 1280, h: 720,  name: '1280x720 (Native 720p)' }
];

let totalLayoutIssues = 0;

for (const res of testResolutions) {
  console.log(`\nTesting Resolution: ${res.name}...`);
  await send('Emulation.setDeviceMetricsOverride', {
    width: res.w,
    height: res.h,
    deviceScaleFactor: 1,
    mobile: false
  });

  for (let ch = 1; ch <= 30; ch++) {
    await send('Page.navigate', { url: `http://127.0.0.1:8932/index.html#chapter/${ch}/slides` });
    await new Promise(r => setTimeout(r, 450));

    const countRes = await safeEval({
      expression: `document.querySelectorAll('.reveal .slides > section').length`,
      returnByValue: true
    });
    const sCount = countRes.result?.value || 0;

    let chIssues = 0;
    for (let i = 0; i < sCount; i++) {
      const slideRes = await safeEval({
        expression: `(async () => {
          if (window.Reveal) window.Reveal.slide(${i}, 0);
          await new Promise(r => setTimeout(r, 40));
          const sec = document.querySelectorAll('.reveal .slides > section')[${i}];
          if (!sec) return null;
          const rect = sec.getBoundingClientRect();
          const footer = sec.querySelector('.slide-footer');
          const footerRect = footer ? footer.getBoundingClientRect() : null;
          
          const elements = Array.from(sec.querySelectorAll('h1, .slide-kicker, .explanation, .code-layout, .content-layout, .output-card, .math-card, .exercise-tip, .question-card, ul, p.lead, p.note, .cover-author-block, .code-card'));
          const bottomMax = elements.length > 0 ? Math.max(...elements.map(c => c.getBoundingClientRect().bottom)) : 0;
          const rightMax = elements.length > 0 ? Math.max(...elements.map(c => c.getBoundingClientRect().right)) : 0;
          
          const overflowsVertical = sec.scrollHeight > sec.clientHeight + 4;
          const collidesFooter = footerRect ? (bottomMax > footerRect.top + 2) : false;
          const overflowsBottom = bottomMax > rect.bottom + 4;
          const overflowsRight = rightMax > rect.right + 4;

          return {
            index: ${i + 1},
            title: sec.querySelector('h1')?.innerText?.trim() || '',
            hasIssue: (overflowsVertical || collidesFooter || overflowsBottom || overflowsRight),
            collidesFooter,
            overflowsVertical,
            overflowsBottom,
            overflowsRight
          };
        })()`,
        awaitPromise: true,
        returnByValue: true
      });

      const sData = slideRes?.result?.value;
      if (sData?.hasIssue) {
        console.error(`   ❌ Ch ${ch} Slide ${sData.index} ("${sData.title}"): Layout Issue (collidesFooter: ${sData.collidesFooter}, vert: ${sData.overflowsVertical}, btm: ${sData.overflowsBottom}, right: ${sData.overflowsRight})`);
        chIssues++;
        totalLayoutIssues++;
      }
    }

    if (chIssues === 0) {
      process.stdout.write(`   ✓ Ch ${String(ch).padStart(2, '0')}: PASS | `);
      if (ch % 4 === 0) process.stdout.write('\n');
    }
  }
  process.stdout.write('\n');
}

ws.close();
browserProc.kill();

console.log('\n====================================================');
console.log(`FINAL RESULT: Static Errors: ${staticErrors} | Layout Issues: ${totalLayoutIssues}`);
console.log('====================================================');

if (staticErrors > 0 || totalLayoutIssues > 0) {
  process.exit(1);
} else {
  console.log('🎉 ALL PRESENTATION AUDIT & LAYOUT CHECKS PASSED PERFECTLY!\n');
  process.exit(0);
}

