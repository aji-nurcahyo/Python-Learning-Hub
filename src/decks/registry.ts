import ch01Slides from '../../content/foundations/chapter-01/slides/deck.json';
import ch02Slides from '../../content/foundations/chapter-02/slides/deck.json';
import ch03Slides from '../../content/foundations/chapter-03/slides/deck.json';
import ch04Slides from '../../content/foundations/chapter-04/slides/deck.json';
import ch08Slides from '../../content/foundations/chapter-08/slides/deck.json';
import ch09Slides from '../../content/foundations/chapter-09/slides/deck.json';
import ch10Slides from '../../content/foundations/chapter-10/slides/deck.json';
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
  if (chapterId === 1) return ch01Slides as SlideData[];
  if (chapterId === 2) return ch02Slides as SlideData[];
  if (chapterId === 3) return ch03Slides as SlideData[];
  if (chapterId === 4) return ch04Slides as SlideData[];
  if (chapterId === 8) return ch08Slides as SlideData[];
  if (chapterId === 9) return ch09Slides as SlideData[];
  if (chapterId === 10) return ch10Slides as SlideData[];
  if (chapterId === 11) return ch11Slides as SlideData[];
  return null;
}

// Backward-compatibility meeting helper
export const meetings = Array.from({ length: 16 }, (_, i) => {
  const number = i + 1;
  const isAvail = [1, 2, 3, 4, 8, 9, 10, 11].includes(number);
  return {
    number,
    available: isAvail,
    title:
      number === 1
        ? 'Introduction to Python'
        : number === 2
        ? 'Variables & Data Types'
        : number === 3
        ? 'Operators & Expressions'
        : number === 4
        ? 'Input & Output'
        : number === 10
        ? 'Functions & Scope'
        : number === 8
        ? 'Lists & Tuples'
        : 'Materi Pembelajaran',
    description: 'Modul pembelajaran Python Learning Hub.',
    tags: ['Python', 'Learning Hub'],
    path: `index.html#chapter/${number}`,
  };
});
