import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'node:path';

// Entrypoints for static hosting (includes 404.html SPA fallback for GitHub Pages)
const pages = ['index.html', '404.html'];

function normalizeBasePath(value?: string): string {
  const trimmed = value?.trim();
  if (!trimmed) return './';
  if (trimmed === '.' || trimmed === './') return './';
  return trimmed.endsWith('/') ? trimmed : `${trimmed}/`;
}

const base = normalizeBasePath(process.env.VITE_BASE_PATH);

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
