import type { SlideData } from '../decks/registry';
import type { RubricItem } from '../components/AssignmentCard';

export interface SpecializationModuleMeta {
  id: string; // e.g. 'A01'
  trackId: string; // e.g. 'data-science'
  trackTitle: string;
  order: number;
  title: string;
  subtitle: string;
  description: string;
  difficulty: 'Intermediate' | 'Advanced';
  estimatedHours: number;
  prerequisites: string[];
  learningObjectives: string[];
  dependencies: string[];
  tags: string[];
  isCapstone?: boolean;
  codeExample: {
    title: string;
    filename: string; // e.g. 'a01_01_ndarray_basics.py'
    outputKey: string; // e.g. 'spec/A01/a01_01_ndarray_basics'
    explanation: string;
  };
  exercise: {
    title: string;
    instructions: string[];
    tips: string;
    time: string;
  };
  quiz: {
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
    hint?: string;
  };
  assignment: {
    title: string;
    description: string;
    instructions: string[];
    rubric: RubricItem[];
    starterFilename: string;
  };
  resources: {
    hasSlides: boolean;
    codeDownload?: string | null;
    notebookDownload?: string | null;
    datasetDownload?: string | null;
    guideDownload?: string | null;
    pptxDownload?: string | null;
  };
  references: {
    title: string;
    source: string;
    url: string;
    license?: string;
  }[];
}

export interface SpecializationModule extends SpecializationModuleMeta {
  slides: SlideData[];
  readingMarkdown: string;
  starterCode: string;
  exampleCode: string;
  assignmentMarkdown: string;
}

const metaGlobs = import.meta.glob('../../content/specializations/*/modules/*/metadata.json', {
  import: 'default',
  eager: true,
}) as Record<string, SpecializationModuleMeta>;

const deckGlobs = import.meta.glob('../../content/specializations/*/modules/*/slides/deck.json', {
  import: 'default',
  eager: true,
}) as Record<string, SlideData[]>;

const readingGlobs = import.meta.glob('../../content/specializations/*/modules/*/index.md', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>;

const codeGlobs = import.meta.glob('../../content/specializations/*/modules/*/code/*.py', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>;

const tugasPyGlobs = import.meta.glob('../../content/specializations/*/modules/*/assignments/tugas.py', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>;

const tugasMdGlobs = import.meta.glob('../../content/specializations/*/modules/*/assignments/tugas.md', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>;

function findBySuffix<T>(map: Record<string, T>, prefix: string, suffix: string): T | undefined {
  const entry = Object.entries(map).find(([k]) => k.startsWith(prefix) && k.endsWith(suffix));
  return entry ? entry[1] : undefined;
}

export const SPECIALIZATION_MODULES: SpecializationModule[] = Object.entries(metaGlobs)
  .map(([path, meta]) => {
    const baseDir = path.replace(/\/metadata\.json$/, '');
    const slides = findBySuffix(deckGlobs, baseDir, '/slides/deck.json') || [];
    const readingMarkdown = findBySuffix(readingGlobs, baseDir, '/index.md') || '';
    const starterCode = findBySuffix(tugasPyGlobs, baseDir, '/assignments/tugas.py') || '';
    const assignmentMarkdown = findBySuffix(tugasMdGlobs, baseDir, '/assignments/tugas.md') || '';
    const exampleCode =
      (meta.codeExample?.filename
        ? findBySuffix(codeGlobs, baseDir, `/code/${meta.codeExample.filename}`)
        : undefined) || '';

    return {
      ...meta,
      slides,
      readingMarkdown,
      starterCode,
      exampleCode,
      assignmentMarkdown,
    };
  })
  .sort((a, b) => a.id.localeCompare(b.id));

export function getSpecializationModuleById(moduleId: string): SpecializationModule | undefined {
  const normalized = moduleId.trim().toUpperCase();
  return SPECIALIZATION_MODULES.find((m) => m.id.toUpperCase() === normalized);
}

export function getModulesForTrack(trackId: string): SpecializationModule[] {
  return SPECIALIZATION_MODULES.filter((m) => m.trackId === trackId).sort((a, b) => a.order - b.order);
}

export function getSlideDeckForSpecialization(moduleId: string): SlideData[] | null {
  const mod = getSpecializationModuleById(moduleId);
  return mod && mod.slides.length > 0 ? mod.slides : null;
}

export function getSpecializationCodeFile(key: string): string | undefined {
  // key format: 'spec/A01/a01_01_ndarray_basics'
  const m = /^spec\/([A-E]\d{2})\/([a-zA-Z0-9_.-]+)$/.exec(key);
  if (!m) return undefined;
  const [, modId, fileBase] = m;
  const targetSuffix = `/modules/${modId}/code/${fileBase}.py`;
  const entry = Object.entries(codeGlobs).find(([k]) => k.endsWith(targetSuffix));
  return entry ? entry[1] : undefined;
}

