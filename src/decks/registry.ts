import ch10Slides from '../../content/foundations/chapter-10/slides/deck.json';
import ch08Slides from '../../content/foundations/chapter-08/slides/deck.json';
import ch09Slides from '../../content/foundations/chapter-09/slides/deck.json';
import ch11Slides from '../../content/foundations/chapter-11/slides/deck.json';

export interface SlideData {
  title: string;
  body: string;
  kind: string;
  notes: string;
  example?: string;
  dependency?: string;
  files?: { name: string; code: string }[];
  question?: string;
  answer?: string;
}

export function getSlideDeckForChapter(chapterId: number): SlideData[] | null {
  if (chapterId === 10) return ch10Slides as SlideData[];
  if (chapterId === 8) return ch08Slides as SlideData[];
  if (chapterId === 9) return ch09Slides as SlideData[];
  if (chapterId === 11) return ch11Slides as SlideData[];
  return null;
}

// Backward-compatibility meeting helper
export const meetings = Array.from({ length: 16 }, (_, i) => {
  const number = i + 1;
  return {
    number,
    available: number === 8 || number === 9 || number === 10 || number === 11,
    title: number === 10 ? 'Functions & Scope' : number === 8 ? 'Lists & Tuples' : 'Materi Pembelajaran',
    description: 'Modul pembelajaran Python Learning Hub.',
    tags: ['Python', 'Learning Hub'],
    path: `index.html#chapter/${number}`,
  };
});
