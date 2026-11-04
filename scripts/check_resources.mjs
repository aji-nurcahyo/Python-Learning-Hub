import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');
const contentDir = path.join(rootDir, 'content');
const publicDir = path.join(rootDir, 'public');

console.log('========================================================================');
console.log(' PYTHON LEARNING HUB — CHAPTER PRESENTATIONS & RESOURCES AUDIT');
console.log('========================================================================\n');

const levels = ['foundations', 'intermediate', 'professional'];
const seenIds = new Set();
let errorCount = 0;
const auditTable = [];

for (const level of levels) {
  const levelDir = path.join(contentDir, level);
  if (!fs.existsSync(levelDir)) {
    console.error(`ERROR: Level directory missing: ${levelDir}`);
    errorCount++;
    continue;
  }

  const entries = fs.readdirSync(levelDir, { withFileTypes: true })
    .filter((e) => e.isDirectory() && e.name.startsWith('chapter-'))
    .sort((a, b) => a.name.localeCompare(b.name));

  for (const entry of entries) {
    const chDir = path.join(levelDir, entry.name);
    const metaPath = path.join(chDir, 'metadata.json');

    if (!fs.existsSync(metaPath)) {
      console.error(`ERROR: Missing metadata.json in ${chDir}`);
      errorCount++;
      continue;
    }

    let meta;
    try {
      meta = JSON.parse(fs.readFileSync(metaPath, 'utf-8'));
    } catch (err) {
      console.error(`ERROR: Corrupt JSON in ${metaPath}:`, err.message);
      errorCount++;
      continue;
    }

    const id = meta.id;
    if (seenIds.has(id)) {
      console.error(`ERROR: Duplicate chapter ID detected: ${id} in ${chDir}`);
      errorCount++;
    }
    seenIds.add(id);

    const res = meta.resources || {};
    let slideStatus = 'None';
    let pptxStatus = 'None';
    let codeStatus = 'None';
    let guideStatus = 'None';

    // 1. Audit Reveal.js Slides
    if (res.hasSlides) {
      if (!res.slidesDeck) {
        console.error(`ERROR: Chapter ${id} claims hasSlides=true but slidesDeck is null/empty.`);
        errorCount++;
        slideStatus = 'MISSING_PATH';
      } else {
        const slideFilePath = path.join(chDir, res.slidesDeck);
        if (!fs.existsSync(slideFilePath)) {
          console.error(`ERROR: Chapter ${id} slide file missing: ${slideFilePath}`);
          errorCount++;
          slideStatus = 'FILE_NOT_FOUND';
        } else {
          try {
            const slideData = JSON.parse(fs.readFileSync(slideFilePath, 'utf-8'));
            const count = Array.isArray(slideData) ? slideData.length : (slideData.slides?.length || 0);
            slideStatus = `OK (${count} slides)`;
          } catch (e) {
            console.error(`ERROR: Chapter ${id} corrupt slide deck: ${e.message}`);
            errorCount++;
            slideStatus = 'CORRUPT_DECK';
          }
        }
      }
    } else {
      if (res.slidesDeck) {
        console.warn(`WARNING: Chapter ${id} hasSlides=false but declares slidesDeck: ${res.slidesDeck}`);
      }
      slideStatus = '-';
    }

    // 2. Audit PowerPoint Download (.pptx)
    if (res.pptxDownload) {
      const pptxFilePath = path.join(publicDir, res.pptxDownload);
      if (!fs.existsSync(pptxFilePath)) {
        console.error(`ERROR: Chapter ${id} claims PPTX at ${res.pptxDownload} but file is missing: ${pptxFilePath}`);
        errorCount++;
        pptxStatus = 'FILE_NOT_FOUND';
      } else {
        const stat = fs.statSync(pptxFilePath);
        if (stat.size < 50000) {
          console.error(`ERROR: Chapter ${id} PPTX file is unexpectedly small (<50KB): ${stat.size} bytes`);
          errorCount++;
          pptxStatus = 'SUSPICIOUS_SIZE';
        } else {
          const buf = Buffer.alloc(4);
          const fd = fs.openSync(pptxFilePath, 'r');
          fs.readSync(fd, buf, 0, 4, 0);
          fs.closeSync(fd);
          const isZip = buf[0] === 0x50 && buf[1] === 0x4b; // 'PK' magic number
          if (!isZip) {
            console.error(`ERROR: Chapter ${id} PPTX file is not a valid zip archive.`);
            errorCount++;
            pptxStatus = 'CORRUPT_ZIP';
          } else {
            pptxStatus = `OK (${Math.round(stat.size / 1024)} KB)`;
          }
        }
      }
    } else {
      pptxStatus = '- (Belum tersedia)';
    }

    // 3. Audit Python Starter Code
    if (res.starterCode) {
      const codeLocal = path.join(chDir, res.starterCode);
      const codePub = path.join(publicDir, 'downloads', `chapter-${String(id).padStart(2, '0')}`, 'contoh.py');
      if (fs.existsSync(codeLocal) || fs.existsSync(codePub)) {
        codeStatus = 'OK (.py)';
      } else {
        console.error(`ERROR: Chapter ${id} starter code declared but missing: ${res.starterCode}`);
        errorCount++;
        codeStatus = 'MISSING';
      }
    } else {
      codeStatus = '-';
    }

    // 4. Audit Assignment Guide
    if (res.assignmentGuide) {
      const guideLocal = path.join(chDir, res.assignmentGuide);
      const guidePub = path.join(publicDir, 'downloads', `chapter-${String(id).padStart(2, '0')}`, 'tugas.md');
      if (fs.existsSync(guideLocal) || fs.existsSync(guidePub)) {
        guideStatus = 'OK (.md)';
      } else {
        console.error(`ERROR: Chapter ${id} guide declared but missing: ${res.assignmentGuide}`);
        errorCount++;
        guideStatus = 'MISSING';
      }
    } else {
      guideStatus = '-';
    }

    auditTable.push({
      id,
      number: meta.number || String(id).padStart(2, '0'),
      title: meta.title || 'Untitled',
      level,
      available: meta.available ? 'AVAILABLE' : 'UPCOMING',
      slideStatus,
      pptxStatus,
      codeStatus,
      guideStatus,
    });
  }
}

// Print formatted audit table
console.log('| Ch | Status     | Title                            | Reveal.js Slides | PowerPoint (.pptx)     | Code     | Guide   |');
console.log('|:---|:-----------|:---------------------------------|:-----------------|:-----------------------|:---------|:--------|');
for (const r of auditTable) {
  const ch = `Ch ${r.number}`.padEnd(4);
  const st = r.available.padEnd(10);
  const tit = (r.title.length > 32 ? r.title.slice(0, 31) + '…' : r.title).padEnd(32);
  const sl = r.slideStatus.padEnd(16);
  const ppt = r.pptxStatus.padEnd(22);
  const cd = r.codeStatus.padEnd(8);
  const gd = r.guideStatus.padEnd(7);
  console.log(`| ${ch} | ${st} | ${tit} | ${sl} | ${ppt} | ${cd} | ${gd} |`);
}

console.log('\n========================================================================');
console.log(`Total Chapters Audited : ${auditTable.length} / 30`);
console.log(`Active Interactive Decks: ${auditTable.filter((r) => r.slideStatus.startsWith('OK')).length}`);
console.log(`Verified PPTX Downloads: ${auditTable.filter((r) => r.pptxStatus.startsWith('OK')).length}`);
console.log(`Intentionally Pending   : ${auditTable.filter((r) => !r.slideStatus.startsWith('OK')).length}`);

if (errorCount > 0) {
  console.error(`\nFAILED: Found ${errorCount} resource reference errors!`);
  process.exit(1);
} else {
  console.log('\nSUCCESS: All chapter presentations, slide decks, PPTX files, and resources are 100% verified!');
  process.exit(0);
}

