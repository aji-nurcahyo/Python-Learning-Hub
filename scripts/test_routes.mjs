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

// Check Chapter starter downloads in dist/ (all 30 chapters)
let missingDownloads = 0;
for (let ch = 1; ch <= 30; ch++) {
  const pad = String(ch).padStart(2, '0');
  const codePath = resolve(dist, `downloads/chapter-${pad}/contoh.py`);
  const guidePath = resolve(dist, `downloads/chapter-${pad}/tugas.md`);
  if (!existsSync(codePath) || !existsSync(guidePath)) {
    console.error(`✗ Missing download assets for chapter-${pad} in dist/downloads/`);
    missingDownloads++;
  }
}
if (missingDownloads === 0) {
  console.log('✓ All 30 chapter starter code and guide packages present in dist/downloads/');
} else {
  passed = -999;
}

// Check Getting Started & Upstream License in dist/downloads/
const gsCode = resolve(dist, 'downloads/getting-started/main.py');
const licenseUpstream = resolve(dist, 'downloads/LICENSE.upstream');
if (existsSync(gsCode) && existsSync(licenseUpstream)) {
  console.log('✓ Getting Started script and LICENSE.upstream present in dist/downloads/');
} else {
  console.error('✗ Getting Started script or LICENSE.upstream missing in dist/downloads/');
  passed = -999;
}

// Check base path injection if VITE_BASE_PATH is configured
const configuredBase = process.env.VITE_BASE_PATH?.trim();
if (configuredBase && configuredBase !== './' && configuredBase !== '.') {
  const normalizedBase = configuredBase.endsWith('/') ? configuredBase : `${configuredBase}/`;
  for (const r of routes) {
    const html = readFileSync(resolve(dist, r), 'utf-8');
    if (!html.includes(`${normalizedBase}assets/`)) {
      console.error(`✗ Route /${r} does not reference configured base path ${normalizedBase}assets/`);
      passed = -999;
    } else {
      console.log(`✓ Route /${r} correctly references ${normalizedBase}assets/`);
    }
  }
}

if (passed === routes.length) {
  console.log('\nAll production routes, presentations, PPTX files, and static markers verified successfully.');
  process.exit(0);
} else {
  console.error('\nProduction artifact verification failed.');
  process.exit(1);
}
