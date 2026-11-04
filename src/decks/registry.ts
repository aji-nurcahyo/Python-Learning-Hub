import ch01Slides from '../../content/foundations/chapter-01/slides/deck.json';
import ch02Slides from '../../content/foundations/chapter-02/slides/deck.json';
import ch03Slides from '../../content/foundations/chapter-03/slides/deck.json';
import ch04Slides from '../../content/foundations/chapter-04/slides/deck.json';
import ch05Slides from '../../content/foundations/chapter-05/slides/deck.json';
import ch06Slides from '../../content/foundations/chapter-06/slides/deck.json';
import ch07Slides from '../../content/foundations/chapter-07/slides/deck.json';
import ch08Slides from '../../content/foundations/chapter-08/slides/deck.json';
import ch09Slides from '../../content/foundations/chapter-09/slides/deck.json';
import ch10Slides from '../../content/foundations/chapter-10/slides/deck.json';
import ch11Slides from '../../content/foundations/chapter-11/slides/deck.json';
import ch12Slides from '../../content/foundations/chapter-12/slides/deck.json';
import ch13Slides from '../../content/intermediate/chapter-13/slides/deck.json';
import ch14Slides from '../../content/intermediate/chapter-14/slides/deck.json';
import ch15Slides from '../../content/intermediate/chapter-15/slides/deck.json';
import ch16Slides from '../../content/intermediate/chapter-16/slides/deck.json';
import ch17Slides from '../../content/intermediate/chapter-17/slides/deck.json';
import ch18Slides from '../../content/intermediate/chapter-18/slides/deck.json';
import ch19Slides from '../../content/intermediate/chapter-19/slides/deck.json';
import ch20Slides from '../../content/intermediate/chapter-20/slides/deck.json';
import ch21Slides from '../../content/intermediate/chapter-21/slides/deck.json';
import ch22Slides from '../../content/intermediate/chapter-22/slides/deck.json';
import ch23Slides from '../../content/professional/chapter-23/slides/deck.json';
import ch24Slides from '../../content/professional/chapter-24/slides/deck.json';
import ch25Slides from '../../content/professional/chapter-25/slides/deck.json';
import ch26Slides from '../../content/professional/chapter-26/slides/deck.json';
import ch27Slides from '../../content/professional/chapter-27/slides/deck.json';
import ch28Slides from '../../content/professional/chapter-28/slides/deck.json';

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
  if (chapterId === 5) return ch05Slides as SlideData[];
  if (chapterId === 6) return ch06Slides as SlideData[];
  if (chapterId === 7) return ch07Slides as SlideData[];
  if (chapterId === 8) return ch08Slides as SlideData[];
  if (chapterId === 9) return ch09Slides as SlideData[];
  if (chapterId === 10) return ch10Slides as SlideData[];
  if (chapterId === 11) return ch11Slides as SlideData[];
  if (chapterId === 12) return ch12Slides as SlideData[];
  if (chapterId === 13) return ch13Slides as SlideData[];
  if (chapterId === 14) return ch14Slides as SlideData[];
  if (chapterId === 15) return ch15Slides as SlideData[];
  if (chapterId === 16) return ch16Slides as SlideData[];
  if (chapterId === 17) return ch17Slides as SlideData[];
  if (chapterId === 18) return ch18Slides as SlideData[];
  if (chapterId === 19) return ch19Slides as SlideData[];
  if (chapterId === 20) return ch20Slides as SlideData[];
  if (chapterId === 21) return ch21Slides as SlideData[];
  if (chapterId === 22) return ch22Slides as SlideData[];
  if (chapterId === 23) return ch23Slides as SlideData[];
  if (chapterId === 24) return ch24Slides as SlideData[];
  if (chapterId === 25) return ch25Slides as SlideData[];
  if (chapterId === 26) return ch26Slides as SlideData[];
  if (chapterId === 27) return ch27Slides as SlideData[];
  if (chapterId === 28) return ch28Slides as SlideData[];
  return null;
}

// Backward-compatibility meeting helper
export const meetings = Array.from({ length: 28 }, (_, i) => {
  const number = i + 1;
  const isAvail = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
  ].includes(number);
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
        : number === 5
        ? 'Conditional Statements'
        : number === 6
        ? 'Loops & Iteration'
        : number === 7
        ? 'Strings & Text Processing'
        : number === 8
        ? 'Lists & Tuples'
        : number === 9
        ? 'Dictionaries & Sets'
        : number === 10
        ? 'Functions & Scope'
        : number === 11
        ? 'Modules & Basic Exceptions'
        : number === 12
        ? 'Foundations Capstone Project'
        : number === 13
        ? 'Advanced Functions'
        : number === 14
        ? 'Comprehensions & Iterators'
        : number === 15
        ? 'Searching & Sorting Algorithms'
        : number === 16
        ? 'Algorithm Analysis & Problem Solving'
        : number === 17
        ? 'File Handling & Data Serialization'
        : number === 18
        ? 'Exception Handling & Debugging'
        : number === 19
        ? 'Object-Oriented Programming I'
        : number === 20
        ? 'Object-Oriented Programming II'
        : number === 21
        ? 'Packages, Environments & Testing'
        : number === 22
        ? 'Intermediate Capstone Project'
        : number === 23
        ? 'Advanced OOP & Design Patterns'
        : number === 24
        ? 'Decorators, Generators & Context Managers'
        : number === 25
        ? 'Type Hints & Code Quality'
        : number === 26
        ? 'Advanced Testing & Logging'
        : number === 27
        ? 'Concurrent & Asynchronous Programming'
        : number === 28
        ? 'Networking & API Integration'
        : 'Materi Pembelajaran',
    description: 'Modul pembelajaran Python Learning Hub.',
    tags: ['Python', 'Learning Hub'],
    path: `index.html#chapter/${number}`,
  };
});
