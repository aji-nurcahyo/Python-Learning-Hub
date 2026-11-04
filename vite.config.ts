import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'node:path';

// Entrypoints for static hosting
const pages = ['index.html', '404.html'];

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
