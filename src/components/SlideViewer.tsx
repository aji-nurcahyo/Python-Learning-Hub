import { DeckShell } from '../deck-shell/DeckShell';
import type { SlideData } from '../decks/registry';

interface SlideViewerProps {
  slides: SlideData[];
  chapterNumber: number;
  base?: string;
  onNavigateChapter?: () => void;
  onNavigateReading?: () => void;
  onNavigateTask?: () => void;
}

export function SlideViewer({
  slides,
  chapterNumber,
  base = './',
  onNavigateChapter,
  onNavigateReading,
  onNavigateTask,
}: SlideViewerProps) {
  return (
    <div className="slide-viewer-container">
      <DeckShell
        slides={slides}
        meeting={chapterNumber}
        base={base}
        onNavigateChapter={onNavigateChapter}
        onNavigateReading={onNavigateReading}
        onNavigateTask={onNavigateTask}
      />
    </div>
  );
}
