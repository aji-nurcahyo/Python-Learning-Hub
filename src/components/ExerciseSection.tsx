import { ExerciseCard } from './ExerciseCard';
import { QuizCard } from './QuizCard';

export interface ExerciseData {
  title: string;
  instructions: string[];
  tips: string;
  time: string;
}

export interface QuizData {
  question: string;
  options: string[];
  correctIndex: number;
  explanation: string;
  hint?: string;
}

interface ExerciseSectionProps {
  exercise: ExerciseData;
  quiz: QuizData;
}

export function ExerciseSection({ exercise, quiz }: ExerciseSectionProps) {
  const answerFormatted = `Kunci Jawaban: ${quiz.options[quiz.correctIndex]}\n\nPembahasan: ${quiz.explanation}`;

  return (
    <div className="practice-grid">
      <ExerciseCard
        title={exercise.title}
        instructions={exercise.instructions}
        tips={exercise.tips}
        timeEstimate={exercise.time}
      />
      <QuizCard
        question={quiz.question}
        answer={answerFormatted}
        hint={quiz.hint}
      />
    </div>
  );
}
