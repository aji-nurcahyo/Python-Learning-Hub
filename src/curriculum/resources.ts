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
