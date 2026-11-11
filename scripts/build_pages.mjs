/**
 * Cross-platform GitHub Pages production build script.
 * Ensures VITE_BASE_PATH=/Python-Learning-Hub/ on Windows, macOS, and Linux,
 * then executes the full `npm run build` validation and bundling pipeline.
 */
import { spawnSync } from 'node:child_process';

const base = process.env.VITE_BASE_PATH?.trim() || '/Python-Learning-Hub/';
const isWin = process.platform === 'win32';
const npmCmd = isWin ? 'npm.cmd' : 'npm';

console.log(`Building Python Learning Hub for GitHub Pages (VITE_BASE_PATH=${base})...`);

const result = spawnSync(npmCmd, ['run', 'build'], {
  stdio: 'inherit',
  shell: isWin,
  env: {
    ...process.env,
    VITE_BASE_PATH: base,
  },
});

if (result.error) {
  console.error('Failed to launch npm build:', result.error);
  process.exit(1);
}

process.exit(result.status ?? 1);

