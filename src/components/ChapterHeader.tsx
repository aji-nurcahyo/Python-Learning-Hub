import { Icon } from '../ui/Icon';
import { DifficultyBadge } from './DifficultyBadge';
import type { Chapter } from '../curriculum';
import { hasInteractivePresentation } from '../curriculum/resources';

interface ChapterHeaderProps {
  chapter: Chapter;
  onNavigateLevel: (levelId: number) => void;
  onNavigateSlides?: (chapterId: number) => void;
  onNavigateReading?: (chapterId: number) => void;
  onNavigateTask?: (chapterId: number) => void;
}

export function ChapterHeader({
  chapter,
  onNavigateLevel,
  onNavigateSlides,
  onNavigateReading,
  onNavigateTask,
}: ChapterHeaderProps) {
  return (
    <>
      {/* Breadcrumb */}
      <div className="page-breadcrumb">
        <button
          type="button"
          className="breadcrumb-back-btn"
          onClick={() => onNavigateLevel(chapter.levelId)}
        >
          <Icon name="arrow_back" size={16} />
          <span>Level {chapter.levelId}</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">
          Chapter {chapter.number}: {chapter.title}
        </span>
      </div>

      {/* Header Banner */}
      <header className={`chapter-header-banner ${!chapter.available ? 'upcoming-banner' : ''}`}>
        <div className="chapter-meta-badges">
          {chapter.available ? (
            <span className="status-badge ready">● Tersedia</span>
          ) : (
            <span className="status-badge upcoming">Segera Hadir</span>
          )}
          <span className="ch-level-chip">Level {chapter.levelId}</span>
          <DifficultyBadge difficulty={chapter.difficulty} />
          <span className="ch-hours-chip">
            <Icon name="schedule" size={14} /> {chapter.estimatedHours} jam pembelajaran
          </span>
        </div>

        <h1 className="chapter-title">
          <span className="ch-num-prefix">Chapter {chapter.number} ·</span> {chapter.title}
        </h1>
        <p className="chapter-subtitle">{chapter.subtitle}</p>
        <p className="chapter-desc">{chapter.description}</p>

        <div className="chapter-competency-alert">
          <Icon name={chapter.available ? 'verified' : 'radar'} size={20} />
          <div>
            <strong>Target Fokus Kompetensi:</strong>
            <p>{chapter.competencyFocus}</p>
          </div>
        </div>

        {/* Action Launch Buttons for Active Chapters */}
        {chapter.available && (
          <div className="chapter-launch-bar">
            <div className="launch-group">
              {(chapter.resources?.hasSlides ?? hasInteractivePresentation(chapter.id)) ? (
                <button
                  type="button"
                  className="button primary button-lg"
                  onClick={() => (onNavigateSlides ? onNavigateSlides(chapter.id) : (location.hash = `chapter/${chapter.id}/slides`))}
                >
                  <Icon name="slideshow" size={20} />
                  <span>Buka Presentasi Interaktif Reveal.js</span>
                </button>
              ) : (
                <button
                  type="button"
                  className="button subtle button-lg"
                  disabled
                  title="Slide presentasi interaktif sedang disiapkan untuk modul ini"
                  style={{ opacity: 0.65, cursor: 'not-allowed' }}
                >
                  <Icon name="slideshow" size={20} />
                  <span>Slide Sedang Disiapkan</span>
                </button>
              )}
              <button
                type="button"
                className="button subtle button-lg"
                onClick={() => (onNavigateReading ? onNavigateReading(chapter.id) : (location.hash = `chapter/${chapter.id}/read`))}
              >
                <Icon name="menu_book" size={20} />
                <span>Mode Baca Dokumen</span>
              </button>
              <button
                type="button"
                className="button subtle button-lg"
                onClick={() => (onNavigateTask ? onNavigateTask(chapter.id) : (location.hash = `chapter/${chapter.id}/task`))}
              >
                <Icon name="assignment" size={20} />
                <span>Tugas Mandiri</span>
              </button>
            </div>
          </div>
        )}
      </header>
    </>
  );
}
