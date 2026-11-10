import { CHAPTERS, type Chapter } from '../curriculum';
import { ChapterLayout } from '../components/ChapterLayout';
import { CodeBlock } from '../components/CodeBlock';
import { CodeOutput } from '../components/CodeOutput';
import { ExerciseSection } from '../components/ExerciseSection';
import { AssignmentSection } from '../components/AssignmentSection';
import { Icon } from '../ui/Icon';
import outputs from '../code/outputs.json';

interface ChapterPageProps {
  chapterId: number;
  onNavigateHome: () => void;
  onNavigateLevel: (levelId: number) => void;
  onNavigateChapter: (chapterId: number) => void;
  onNavigateSlides?: (chapterId: number) => void;
  onNavigateReading?: (chapterId: number) => void;
  onNavigateTask?: (chapterId: number) => void;
}

export function ChapterPage({
  chapterId,
  onNavigateHome,
  onNavigateLevel,
  onNavigateChapter,
  onNavigateSlides,
  onNavigateReading,
  onNavigateTask,
}: ChapterPageProps) {
  const chapter: Chapter | undefined = CHAPTERS.find((c) => c.id === chapterId);

  if (!chapter) {
    return (
      <div className="hub-page-container document placeholder">
        <div className="eyebrow">CHAPTER TIDAK DITEMUKAN</div>
        <h1>Chapter {chapterId} Belum Terdaftar</h1>
        <p>Silakan kembali ke kurikulum untuk memilih chapter 1 hingga 30.</p>
        <button type="button" className="button primary" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={18} /> <span>Kembali ke Beranda Hub</span>
        </button>
      </div>
    );
  }

  const prevChapter = CHAPTERS.find((c) => c.id === chapter.id - 1);
  const nextChapter = CHAPTERS.find((c) => c.id === chapter.id + 1);

  const codeOutputText = chapter.codeExample
    ? (outputs as Record<string, string>)[chapter.codeExample.outputKey] || ''
    : '';

  return (
    <ChapterLayout
      chapter={chapter}
      prevChapter={prevChapter}
      nextChapter={nextChapter}
      onNavigateLevel={onNavigateLevel}
      onNavigateHome={onNavigateHome}
      onNavigateChapter={onNavigateChapter}
      onNavigateSlides={onNavigateSlides}
      onNavigateReading={onNavigateReading}
      onNavigateTask={onNavigateTask}
      overviewChildren={
        <div className="pedagogy-callout">
          <Icon name="psychology" size={24} />
          <div>
            <h4>Pendekatan Belajar Terarah</h4>
            <p>
              Mulailah dengan menyimak materi presentasi interaktif Reveal.js untuk memahami konsep visual dan rumus komputasional.
              Lanjutkan dengan membaca contoh kode nyata, mencoba latihan mandiri, menjawab kuis penguatan konsep, dan menyelesaikan tugas terstruktur.
            </p>
          </div>
        </div>
      }
      codeSection={
        chapter.codeExample ? (
          <div>
            <div className="section-heading-clean">
              <div>
                <div className="eyebrow">EKSEKUSI PYTHON 3 ASLI</div>
                <h3>Kode Sumber & Hasil Keluaran Terminal</h3>
              </div>
              <p>Kode berikut dijalankan langsung di mesin Python Interpreter tanpa simulasi.</p>
            </div>

            <div className="code-output-side-by-side">
              <div className="code-side">
                <CodeBlock
                  code={chapter.codeExample.code}
                  filename={`contoh_ch${chapter.number}.py`}
                />
              </div>
              <div className="output-side">
                <CodeOutput output={codeOutputText} />
              </div>
            </div>

            <div className="code-explanation-card">
              <Icon name="lightbulb" size={20} />
              <div>
                <strong>Penjelasan Mekanisme:</strong>
                <p>{chapter.codeExample.explanation}</p>
              </div>
            </div>
          </div>
        ) : undefined
      }
      practiceSection={
        chapter.exercise && chapter.quiz ? (
          <ExerciseSection exercise={chapter.exercise} quiz={chapter.quiz} />
        ) : undefined
      }
      assignmentSection={
        chapter.assignment ? (
          <AssignmentSection assignment={chapter.assignment} />
        ) : undefined
      }
    />
  );
}
