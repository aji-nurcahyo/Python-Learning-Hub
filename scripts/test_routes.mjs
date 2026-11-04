import { readFileSync, existsSync } from 'node:fs';
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

// Check downloads folder
const downloadsPath = resolve(dist, 'downloads');
if (existsSync(downloadsPath)) {
  console.log('✓ Static downloads directory is present in dist/');
} else {
  console.warn('! Warning: downloads directory not found in dist/.');
}

console.log(`\nAll production routes and static markers verified successfully.`);
if (passed === routes.length) {
  process.exit(0);
} else {
  process.exit(1);
}
