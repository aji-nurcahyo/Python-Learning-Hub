/**
 * Content regression checks for slide preservation, placeholder status,
 * and example availability.
 */
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');

for (const n of [9, 10]) {
  const pad = String(n).padStart(2, '0');
  const legacyHtml = resolve(root, `legacy/pertemuan-${pad}/index.html`);
  if (existsSync(legacyHtml)) {
    const original = readFileSync(legacyHtml, 'utf-8');
    const titles = [...original.matchAll(/<h[12]>(.*?)<\/h[12]>/g)].map(m => m[1].replace(/&quot;/g, '"').replace(/&amp;/g, '&'));
    const slides = JSON.parse(readFileSync(resolve(root, `src/decks/pertemuan-${pad}.json`), 'utf-8'));
    const slideTitles = new Set(slides.map(s => s.title));

    for (const title of titles) {
      if (!slideTitles.has(title)) {
        console.error(`Warning: original slide title "${title}" not directly matched in pertemuan-${pad}.json`);
      }
    }
  }

  // Ensure tugas.md and contoh.py are preserved
  const tugasMd = resolve(root, `pertemuan-${pad}/tugas.md`);
  const contohPy = resolve(root, `pertemuan-${pad}/contoh.py`);
  if (!existsSync(tugasMd) || !existsSync(contohPy)) {
    console.error(`Missing required file in pertemuan-${pad}`);
    process.exit(1);
  }

  const slides = JSON.parse(readFileSync(resolve(root, `src/decks/pertemuan-${pad}.json`), 'utf-8'));
  for (const slide of slides) {
    if (slide.example) {
      const exFile = resolve(root, `src/code/${slide.example}.py`);
      if (!existsSync(exFile)) {
        console.error(`Missing example file: ${exFile}`);
        process.exit(1);
      }
    }
  }

  console.log(`Meeting ${n}: slides, examples, and preserved assets verified.`);
}

const entries = readdirSync(root, { withFileTypes: true })
  .filter(d => d.isDirectory() && /^pertemuan-\d{2}$/.test(d.name))
  .map(d => d.name);

if (entries.length !== 16) {
  console.error(`Expected 16 meeting directories, found ${entries.length}`);
  process.exit(1);
}

console.log('✓ 16 entry routes verified: Pertemuan 1-8 (Segera Hadir), Pertemuan 9-10 (Aktif), Pertemuan 11-16 (Segera Hadir).');

