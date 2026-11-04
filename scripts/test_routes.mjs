import { readFileSync, existsSync, statSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const dist = resolve(__dirname, '../dist');

const routes = ['index.html', '404.html'];

console.log(`Checking production build artifacts in ${dist}...`);
let passed = 0;
for (const r of routes) {
  const filePath = resolve(dist, r);
  if (!existsSync(filePath)) {
    console.error(`✗ Route ${r} - File missing at ${filePath}`);
    continue;
  }
  const content = readFileSync(filePath, 'utf-8');
  const hasRoot = content.includes('id="root"');
  const hasScript = content.includes('<script type="module"');
  if (hasRoot && hasScript) {
    console.log(`✓ Route /${r} - OK (file exists, root element, bundled script)`);
    passed++;
  } else {
    console.error(`✗ Route /${r} - Missing root element or bundled script hook`);
  }
}

// Check GitHub Pages .nojekyll marker
const nojekyllPath = resolve(dist, '.nojekyll');
if (existsSync(nojekyllPath)) {
  console.log('✓ GitHub Pages .nojekyll marker is present');
} else {
  console.warn('! Warning: .nojekyll not found in dist/. Jekyll may ignore underscore-prefixed assets on GitHub Pages.');
}

// Check PPTX physical download in dist/
const pptxPath = resolve(dist, 'downloads/Materi_Pengkom_Pertemuan_9_10_Python.pptx');
if (existsSync(pptxPath)) {
  const stat = statSync(pptxPath);
  if (stat.size > 50000) {
    console.log(`✓ PowerPoint binary present in dist/: Materi_Pengkom_Pertemuan_9_10_Python.pptx (${Math.round(stat.size / 1024)} KB)`);
  } else {
    console.error(`✗ PowerPoint file too small in dist/ (${stat.size} bytes)`);
    passed = -999;
  }
} else {
  console.error('✗ PowerPoint file missing in dist/downloads/');
  passed = -999;
}

// Check Chapter starter downloads in dist/
const ch08Code = resolve(dist, 'downloads/chapter-08/contoh.py');
const ch10Code = resolve(dist, 'downloads/chapter-10/contoh.py');
if (existsSync(ch08Code) && existsSync(ch10Code)) {
  console.log('✓ Chapter starter code packages present in dist/downloads/');
} else {
  console.error('✗ Chapter starter code missing in dist/downloads/');
  passed = -999;
}

if (passed === routes.length) {
  console.log('\nAll production routes, presentations, PPTX files, and static markers verified successfully.');
  process.exit(0);
} else {
  console.error('\nProduction artifact verification failed.');
  process.exit(1);
}
