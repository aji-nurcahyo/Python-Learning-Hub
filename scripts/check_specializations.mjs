import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');

const TRACK_EXPECTATIONS = [
  { dir: 'track-data-science', trackId: 'data-science', prefix: 'A', expectNotebooks: true },
  { dir: 'track-ai-ml', trackId: 'ai-ml', prefix: 'B', expectNotebooks: true },
  { dir: 'track-web-api', trackId: 'web-api', prefix: 'C', expectNotebooks: false },
  { dir: 'track-automation', trackId: 'automation', prefix: 'D', expectNotebooks: false },
  { dir: 'track-iot-telecom', trackId: 'iot-telecom', prefix: 'E', expectNotebooks: false },
];

const specOutputsPath = resolve(root, 'src/code/spec-outputs.json');
if (!existsSync(specOutputsPath)) {
  console.error('✗ Missing src/code/spec-outputs.json');
  process.exit(1);
}
const specOutputs = JSON.parse(readFileSync(specOutputsPath, 'utf-8'));

let errors = 0;
let checkedModules = 0;
let checkedSlides = 0;
let checkedExamples = 0;

function fail(msg) {
  console.error(`✗ ${msg}`);
  errors++;
}

for (const track of TRACK_EXPECTATIONS) {
  for (let order = 1; order <= 5; order++) {
    const modId = `${track.prefix}0${order}`;
    const modDir = resolve(root, `content/specializations/${track.dir}/modules/${modId}`);
    checkedModules++;

    if (!existsSync(modDir)) {
      fail(`Missing module directory: ${track.dir}/modules/${modId}`);
      continue;
    }

    const metaPath = resolve(modDir, 'metadata.json');
    const indexPath = resolve(modDir, 'index.md');
    const deckPath = resolve(modDir, 'slides/deck.json');
    const exercisePath = resolve(modDir, 'exercises/exercise.md');
    const tugasMdPath = resolve(modDir, 'assignments/tugas.md');
    const tugasPyPath = resolve(modDir, 'assignments/tugas.py');
    const codeDir = resolve(modDir, 'code');

    for (const reqFile of [metaPath, indexPath, deckPath, exercisePath, tugasMdPath, tugasPyPath]) {
      if (!existsSync(reqFile) || statSync(reqFile).size === 0) {
        fail(`Missing or empty file: ${reqFile}`);
      }
    }

    if (!existsSync(codeDir)) {
      fail(`Missing code directory for ${modId}`);
      continue;
    }

    const pyFiles = readdirSync(codeDir).filter((f) => f.endsWith('.py'));
    const testFiles = pyFiles.filter((f) => f.startsWith('test_'));
    const exampleFiles = pyFiles.filter((f) => !f.startsWith('test_') && !f.startsWith('_'));

    if (exampleFiles.length < 4) {
      fail(`${modId}: expected at least 4 example scripts in code/, found ${exampleFiles.length}`);
    }
    if (testFiles.length < 1) {
      fail(`${modId}: expected at least 1 pytest file in code/, found 0`);
    }

    // Check metadata.json contract
    if (existsSync(metaPath)) {
      const meta = JSON.parse(readFileSync(metaPath, 'utf-8'));
      if (meta.id !== modId || meta.trackId !== track.trackId) {
        fail(`${modId}: metadata id/trackId mismatch (${meta.id}/${meta.trackId})`);
      }
      const rubricTotal = (meta.assignment?.rubric || []).reduce((acc, r) => acc + (r.weight || 0), 0);
      if (rubricTotal !== 100) {
        fail(`${modId}: assignment rubric weights sum to ${rubricTotal}, expected 100`);
      }
      const outKey = meta.codeExample?.outputKey;
      if (!outKey || typeof specOutputs[outKey] !== 'string' || specOutputs[outKey].trim() === '') {
        fail(`${modId}: missing output in spec-outputs.json for ${outKey}`);
      }

      // Check public/downloads/specializations/<modId> mirrors all non-null resources
      for (const [resKey, resVal] of Object.entries(meta.resources || {})) {
        if (typeof resVal === 'string' && resVal.startsWith('/downloads/')) {
          const pubFile = resolve(root, 'public', resVal.slice(1));
          if (!existsSync(pubFile)) {
            fail(`${modId}: resource '${resKey}' target missing at ${pubFile}`);
          }
        }
      }
    }

    // Check notebook presence when expected
    if (track.expectNotebooks) {
      const nbDir = resolve(modDir, 'notebooks');
      const hasNb = existsSync(nbDir) && readdirSync(nbDir).some((f) => f.endsWith('.ipynb'));
      if (!hasNb) {
        fail(`${modId}: expected .ipynb notebook in notebooks/`);
      }
    }

    // Check slides/deck.json contract
    if (existsSync(deckPath)) {
      const deckRaw = readFileSync(deckPath, 'utf-8');
      if (/reveal\.js/i.test(deckRaw)) {
        fail(`${modId}: deck.json contains forbidden reference to Reveal.js`);
      }
      const slides = JSON.parse(deckRaw);
      if (!Array.isArray(slides) || slides.length < 15 || slides.length > 25) {
        fail(`${modId}: deck length ${slides?.length} outside 15..25 bounds`);
      }
      if (slides[0]?.kind !== 'cover') {
        fail(`${modId}: slide 0 must have kind='cover'`);
      }
      checkedSlides += slides.length;

      for (const slide of slides) {
        if (slide.example) {
          checkedExamples++;
          const expectedPrefix = `spec/${modId}/`;
          if (!slide.example.startsWith(expectedPrefix)) {
            fail(`${modId}: slide example '${slide.example}' must start with '${expectedPrefix}'`);
            continue;
          }
          const stem = slide.example.slice(expectedPrefix.length);
          const pySource = resolve(codeDir, `${stem}.py`);
          const dlTarget = resolve(root, `public/downloads/specializations/${modId}/${stem}.py`);
          if (!existsSync(pySource)) {
            fail(`${modId}: missing code file ${pySource} referenced by slide`);
          }
          if (!existsSync(dlTarget)) {
            fail(`${modId}: missing downloadable copy ${dlTarget}`);
          }
          if (typeof specOutputs[slide.example] !== 'string' || specOutputs[slide.example].trim() === '') {
            fail(`${modId}: missing captured stdout in src/code/spec-outputs.json for ${slide.example}`);
          }
        }
      }
    }
  }
}

if (errors > 0) {
  console.error(`\nSpecialization validation failed with ${errors} error(s).`);
  process.exit(1);
}

console.log(
  `✓ Specialization check passed: ${checkedModules}/25 modules, ${checkedSlides} slides, ${checkedExamples} slide code outputs & downloads verified.`,
);

