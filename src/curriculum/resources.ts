/**
 * Centralized Chapter Resource Management for Python Learning Hub.
 *
 * Resolves physical availability, download paths, base-path-aware URLs,
 * and presentation links for all 30 chapters.
 */

export interface ChapterResourceConfig {
  chapterId: number;
  hasSlides: boolean;
  slidesDeck: string | null;
  powerpoint: string | null;
  pythonFiles: string[];
  assignmentGuide: string | null;
}

/**
 * Resolves a public/static asset path into a Vite base-path-aware URL.
 * Supports root domain, relative base (`./`), and GitHub Pages subpaths (`/python-learning-hub/`).
 */
export function getAssetUrl(relativePath: string | null | undefined): string {
  if (!relativePath) return '';
  if (/^(https?:)?\/\//.test(relativePath) || relativePath.startsWith('data:')) {
    return relativePath;
  }
  const cleanPath = relativePath.replace(/^\/+/, '');
  const base = import.meta.env.BASE_URL || './';
  return base.endsWith('/') ? `${base}${cleanPath}` : `${base}/${cleanPath}`;
}

/**
 * Catalog of actual, verified physical resources across the platform.
 * Single source of truth for runtime component resolution.
 */
const PPTX_VERIFIED_FILE = 'downloads/Materi_Pengkom_Pertemuan_9_10_Python.pptx';

export const CHAPTER_RESOURCES_MAP: Record<number, ChapterResourceConfig> = {
  1: {
    chapterId: 1,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-01/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-01/contoh.py', 'downloads/examples/ch01-01.py'],
    assignmentGuide: 'downloads/chapter-01/tugas.md',
  },
  2: {
    chapterId: 2,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-02/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-02/contoh.py', 'downloads/examples/ch02-01.py'],
    assignmentGuide: 'downloads/chapter-02/tugas.md',
  },
  3: {
    chapterId: 3,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-03/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-03/contoh.py', 'downloads/examples/ch03-01.py'],
    assignmentGuide: 'downloads/chapter-03/tugas.md',
  },
  4: {
    chapterId: 4,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-04/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-04/contoh.py', 'downloads/examples/ch04-01.py'],
    assignmentGuide: 'downloads/chapter-04/tugas.md',
  },
  5: {
    chapterId: 5,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-05/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-05/contoh.py', 'downloads/examples/ch05-01.py'],
    assignmentGuide: 'downloads/chapter-05/tugas.md',
  },
  6: {
    chapterId: 6,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-06/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-06/contoh.py', 'downloads/examples/ch06-01.py'],
    assignmentGuide: 'downloads/chapter-06/tugas.md',
  },
  7: {
    chapterId: 7,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-07/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-07/contoh.py', 'downloads/examples/ch07-01.py'],
    assignmentGuide: 'downloads/chapter-07/tugas.md',
  },
  8: {
    chapterId: 8,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-08/slides/deck.json',
    powerpoint: PPTX_VERIFIED_FILE,
    pythonFiles: ['downloads/chapter-08/contoh.py', 'downloads/examples/p10-02.py'],
    assignmentGuide: 'downloads/chapter-08/tugas.md',
  },
  9: {
    chapterId: 9,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-09/slides/deck.json',
    powerpoint: PPTX_VERIFIED_FILE,
    pythonFiles: ['downloads/chapter-09/contoh.py', 'downloads/examples/p10-05.py'],
    assignmentGuide: 'downloads/chapter-09/tugas.md',
  },
  10: {
    chapterId: 10,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-10/slides/deck.json',
    powerpoint: PPTX_VERIFIED_FILE,
    pythonFiles: ['downloads/chapter-10/contoh.py', 'downloads/examples/p09-14.py'],
    assignmentGuide: 'downloads/chapter-10/tugas.md',
  },
  11: {
    chapterId: 11,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-11/slides/deck.json',
    powerpoint: PPTX_VERIFIED_FILE,
    pythonFiles: ['downloads/chapter-11/contoh.py', 'downloads/examples/p09-13.py'],
    assignmentGuide: 'downloads/chapter-11/tugas.md',
  },
  12: {
    chapterId: 12,
    hasSlides: true,
    slidesDeck: 'content/foundations/chapter-12/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-12/contoh.py', 'downloads/examples/ch12-01.py'],
    assignmentGuide: 'downloads/chapter-12/tugas.md',
  },
  13: {
    chapterId: 13,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-13/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-13/contoh.py', 'downloads/examples/ch13-01.py'],
    assignmentGuide: 'downloads/chapter-13/tugas.md',
  },
  14: {
    chapterId: 14,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-14/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-14/contoh.py', 'downloads/examples/ch14-01.py'],
    assignmentGuide: 'downloads/chapter-14/tugas.md',
  },
  15: {
    chapterId: 15,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-15/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-15/contoh.py', 'downloads/examples/ch15-01.py'],
    assignmentGuide: 'downloads/chapter-15/tugas.md',
  },
  16: {
    chapterId: 16,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-16/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-16/contoh.py', 'downloads/examples/ch16-01.py'],
    assignmentGuide: 'downloads/chapter-16/tugas.md',
  },
  17: {
    chapterId: 17,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-17/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-17/contoh.py', 'downloads/examples/ch17-01.py'],
    assignmentGuide: 'downloads/chapter-17/tugas.md',
  },
  18: {
    chapterId: 18,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-18/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-18/contoh.py', 'downloads/examples/ch18-01.py'],
    assignmentGuide: 'downloads/chapter-18/tugas.md',
  },
  19: {
    chapterId: 19,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-19/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-19/contoh.py', 'downloads/examples/ch19-01.py'],
    assignmentGuide: 'downloads/chapter-19/tugas.md',
  },
  20: {
    chapterId: 20,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-20/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-20/contoh.py', 'downloads/examples/ch20-01.py'],
    assignmentGuide: 'downloads/chapter-20/tugas.md',
  },
  21: {
    chapterId: 21,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-21/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-21/contoh.py', 'downloads/examples/ch21-01.py'],
    assignmentGuide: 'downloads/chapter-21/tugas.md',
  },
  22: {
    chapterId: 22,
    hasSlides: true,
    slidesDeck: 'content/intermediate/chapter-22/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-22/contoh.py', 'downloads/examples/ch22-01.py'],
    assignmentGuide: 'downloads/chapter-22/tugas.md',
  },
  23: {
    chapterId: 23,
    hasSlides: true,
    slidesDeck: 'content/professional/chapter-23/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-23/contoh.py', 'downloads/examples/ch23-01.py'],
    assignmentGuide: 'downloads/chapter-23/tugas.md',
  },
  24: {
    chapterId: 24,
    hasSlides: true,
    slidesDeck: 'content/professional/chapter-24/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-24/contoh.py', 'downloads/examples/ch24-01.py'],
    assignmentGuide: 'downloads/chapter-24/tugas.md',
  },
  25: {
    chapterId: 25,
    hasSlides: true,
    slidesDeck: 'content/professional/chapter-25/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-25/contoh.py', 'downloads/examples/ch25-01.py'],
    assignmentGuide: 'downloads/chapter-25/tugas.md',
  },
  26: {
    chapterId: 26,
    hasSlides: true,
    slidesDeck: 'content/professional/chapter-26/slides/deck.json',
    powerpoint: null,
    pythonFiles: ['downloads/chapter-26/contoh.py', 'downloads/examples/ch26-01.py'],
    assignmentGuide: 'downloads/chapter-26/tugas.md',
  },
};

/**
 * Returns the resource configuration for a given chapter ID (1 to 30).
 * Gracefully returns null resources for chapters that are still in roadmap/planning.
 */
export function getChapterResources(chapterId: number): ChapterResourceConfig {
  if (CHAPTER_RESOURCES_MAP[chapterId]) {
    return CHAPTER_RESOURCES_MAP[chapterId];
  }
  return {
    chapterId,
    hasSlides: false,
    slidesDeck: null,
    powerpoint: null,
    pythonFiles: [],
    assignmentGuide: null,
  };
}

export function hasInteractivePresentation(chapterId: number): boolean {
  return getChapterResources(chapterId).hasSlides;
}

export function hasPowerPointDownload(chapterId: number): boolean {
  return getChapterResources(chapterId).powerpoint !== null;
}

export function getPowerPointDownloadUrl(chapterId: number): string | null {
  const pptx = getChapterResources(chapterId).powerpoint;
  return pptx ? getAssetUrl(pptx) : null;
}

