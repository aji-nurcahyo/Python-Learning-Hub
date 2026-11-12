import { Icon } from '../ui/Icon';
import type { Chapter } from '../curriculum';

export function ChapterNavigation({
  prevChapter,
  nextChapter,
  onNavigate,
}: {
  prevChapter?: Chapter;
  nextChapter?: Chapter;
  onNavigate: (chapterId: number) => void;
}) {
  return (
    <nav className="chapter-nav-bar" aria-label="Navigasi antar chapter">
      {prevChapter ? (
        <button
          type="button"
          className="chapter-nav-btn prev"
          onClick={() => onNavigate(prevChapter.id)}
        >
          <Icon name="arrow_back" size={18} />
          <div className="nav-meta">
            <span className="nav-dir">Chapter Sebelumnya</span>
            <span className="nav-title">{prevChapter.number}. {prevChapter.title}</span>
          </div>
        </button>
      ) : (
        <div className="chapter-nav-spacer" />
      )}

      {nextChapter ? (
        <button
          type="button"
          className="chapter-nav-btn next"
          onClick={() => onNavigate(nextChapter.id)}
        >
          <div className="nav-meta">
            <span className="nav-dir">Chapter Berikutnya</span>
            <span className="nav-title">{nextChapter.number}. {nextChapter.title}</span>
          </div>
          <Icon name="arrow_forward" size={18} />
        </button>
      ) : (
        <div className="chapter-nav-spacer" />
      )}
    </nav>
  );
}

