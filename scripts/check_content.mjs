/**
 * Content regression checks for modular chapter structure, slide preservation,
 * and example availability.
 */
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');
const contentRoot = resolve(root, 'content');

// 1. Verify 30 chapter directories in content/
const levels = [
  { folder: 'foundations', count: 12 },
  { folder: 'intermediate', count: 10 },
  { folder: 'professional', count: 8 },
];

let totalChapters = 0;
for (const lvl of levels) {
  const lvlDir = resolve(contentRoot, lvl.folder);
  if (!existsSync(lvlDir)) {
    console.error(`Missing level directory: ${lvlDir}`);
    process.exit(1);
  }
  const chapters = readdirSync(lvlDir, { withFileTypes: true })
    .filter((d) => d.isDirectory() && /^chapter-\d{2}$/.test(d.name))
    .map((d) => d.name);

  if (chapters.length !== lvl.count) {
    console.error(`Expected ${lvl.count} chapters in ${lvl.folder}, found ${chapters.length}`);
    process.exit(1);
  }

  for (const ch of chapters) {
    const chPath = resolve(lvlDir, ch);
    const metaPath = resolve(chPath, 'metadata.json');
    const indexPath = resolve(chPath, 'index.md');
    if (!existsSync(metaPath) || !existsSync(indexPath)) {
      console.error(`Chapter ${ch} in ${lvl.folder} is missing metadata.json or index.md`);
      process.exit(1);
    }
    totalChapters++;
  }
}
console.log(`✓ ${totalChapters}/30 modular chapter packages verified in content/`);

// 2. Verify 5 Specialization Tracks
const specDir = resolve(contentRoot, 'specializations');
const tracks = readdirSync(specDir, { withFileTypes: true })
  .filter((d) => d.isDirectory() && d.name.startsWith('track-'))
  .map((d) => d.name);

if (tracks.length !== 5) {
  console.error(`Expected 5 tracks in content/specializations, found ${tracks.length}`);
  process.exit(1);
}
console.log(`✓ 5 specialization tracks verified in content/specializations/`);

// 3. Verify Active Chapter Slides & Python Examples
const activeChecks = [
  'foundations/chapter-01',
  'foundations/chapter-02',
  'foundations/chapter-03',
  'foundations/chapter-04',
  'foundations/chapter-05',
  'foundations/chapter-06',
  'foundations/chapter-07',
  'foundations/chapter-08',
  'foundations/chapter-09',
  'foundations/chapter-10',
  'foundations/chapter-11',
  'foundations/chapter-12',
  'intermediate/chapter-13',
  'intermediate/chapter-14',
  'intermediate/chapter-15',
  'intermediate/chapter-16',
];

for (const ch of activeChecks) {
  const deckFile = resolve(contentRoot, ch, 'slides/deck.json');
  const tugasFile = resolve(contentRoot, ch, 'assignments/tugas.md');
  const contohFile = existsSync(resolve(contentRoot, ch, 'code/contoh.py'))
    ? resolve(contentRoot, ch, 'code/contoh.py')
    : resolve(contentRoot, ch, 'assignments/contoh.py');

  if (!existsSync(deckFile) || !existsSync(tugasFile) || !existsSync(contohFile)) {
    console.error(`Missing required active educational asset in ${ch}`);
    process.exit(1);
  }

  const slides = JSON.parse(readFileSync(deckFile, 'utf-8'));
  for (const slide of slides) {
    if (slide.example) {
      const exFile = resolve(root, `src/code/${slide.example}.py`);
      if (!existsSync(exFile)) {
        console.error(`Missing slide code example: ${exFile}`);
        process.exit(1);
      }
    }
  }

  console.log(`✓ Chapter ${ch}: slides, examples, assignments, and Python code verified.`);
}

console.log('✓ All content, slide registries, and modular chapter assets verified successfully.');
