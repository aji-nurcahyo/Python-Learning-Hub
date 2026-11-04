import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'node:path';

// Multi-page entrypoints for static hosting
const pages = [
  'index.html',
  ...Array.from({ length: 16 }, (_, i) => `pertemuan-${String(i + 1).padStart(2, '0')}/index.html`),
  'pertemuan-09/tugas.html',
  'pertemuan-10/tugas.html',
  '404.html',
];

// Base path configuration:
// Defaults to './' for seamless relative resolution on GitHub Pages subpaths,
// Cloudflare Pages, and local previews. Can be overridden via VITE_BASE_PATH.
const base = process.env.VITE_BASE_PATH || './';

export default defineConfig({
  plugins: [react()],
  base,
  build: {
    target: 'es2022',
    rollupOptions: {
      input: pages.map((p) => resolve(import.meta.dirname, p)),
    },
  },
});
