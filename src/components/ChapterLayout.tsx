import { useState, type ReactNode } from 'react';
import { Icon } from '../ui/Icon';
import type { Chapter } from '../curriculum';
import { ChapterHeader } from './ChapterHeader';
import { LearningObjectives } from './LearningObjectives';
import { PrerequisiteList } from './PrerequisiteList';
import { ChapterNavigation } from './ChapterNavigation';
import { ResourceDownloads } from './ResourceDownloads';
import { getChapterResources } from '../curriculum/resources';

interface ChapterLayoutProps {
  chapter: Chapter;
  prevChapter?: Chapter;
  nextChapter?: Chapter;
  onNavigateLevel: (levelId: number) => void;
  onNavigateHome: () => void;
  onNavigateChapter: (chapterId: number) => void;
  onNavigateSlides?: (chapterId: number) => void;
  onNavigateReading?: (chapterId: number) => void;
  onNavigateTask?: (chapterId: number) => void;
  codeSection?: ReactNode;
  practiceSection?: ReactNode;
  assignmentSection?: ReactNode;
  overviewChildren?: ReactNode;
}

export function ChapterLayout({
  chapter,
  prevChapter,
  nextChapter,
  onNavigateLevel,
  onNavigateHome,
  onNavigateChapter,
  onNavigateSlides,
  onNavigateReading,
  onNavigateTask,
  codeSection,
  practiceSection,
  assignmentSection,
  overviewChildren,
}: ChapterLayoutProps) {
  const [activeTab, setActiveTab] = useState<'overview' | 'code' | 'practice' | 'assignment'>('overview');

  // If Chapter is Upcoming / Coming Soon
  if (!chapter.available) {
    return (
      <div className="hub-chapter-page upcoming-view">
        <ChapterHeader
          chapter={chapter}
          onNavigateLevel={onNavigateLevel}
          onNavigateSlides={onNavigateSlides}
          onNavigateReading={onNavigateReading}
          onNavigateTask={onNavigateTask}
        />

        {/* Coming Soon Notice Card */}
        <div className="coming-soon-notice-card">
          <div className="notice-icon-box">
            <Icon name="construction" size={32} />
          </div>
          <div className="notice-content">
            <h3>Materi Sedang Dalam Tahap Penyusunan</h3>
            <p>
              Silabus, tujuan pembelajaran, dan prasyarat chapter ini telah dirancang sesuai kurikulum.
              Materi slide interaktif, contoh eksekusi kode, dan tugas mandiri akan dirilis secara bertahap.
              Selesaikan chapter-chapter dasar yang telah tersedia terlebih dahulu untuk membangun pemahaman yang solid.
            </p>
            <div className="notice-actions">
              <button
                type="button"
                className="button primary"
                onClick={() => onNavigateLevel(chapter.levelId)}
              >
                <Icon name="arrow_back" size={18} />
                <span>Lihat Silabus Level {chapter.levelId}</span>
              </button>
              <button
                type="button"
                className="button subtle"
                onClick={onNavigateHome}
              >
                <span>Katalog Chapter</span>
              </button>
            </div>
          </div>
        </div>

        {/* Prereqs & Objectives Preview */}
        <div className="chapter-preview-grid">
          <PrerequisiteList prerequisites={chapter.prerequisites} />
          <LearningObjectives objectives={chapter.learningObjectives} />
        </div>

        {/* Navigation to Prev / Next */}
        <ChapterNavigation
          prevChapter={prevChapter}
          nextChapter={nextChapter}
          onNavigate={(targetId) => onNavigateChapter(targetId)}
        />
      </div>
    );
  }

  // Active Chapter View
  return (
    <div className="hub-chapter-page active-view">
      <ChapterHeader
        chapter={chapter}
        onNavigateLevel={onNavigateLevel}
        onNavigateSlides={onNavigateSlides}
        onNavigateReading={onNavigateReading}
        onNavigateTask={onNavigateTask}
      />

      {/* Tabs Navigation for Chapter Content */}
      <div className="chapter-tabs-nav" role="tablist">
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'overview'}
          className={activeTab === 'overview' ? 'active' : ''}
          onClick={() => setActiveTab('overview')}
        >
          <Icon name="info" size={18} />
          <span>Ikhtisar & Kompetensi</span>
        </button>
        {codeSection && (
          <button
            type="button"
            role="tab"
            aria-selected={activeTab === 'code'}
            className={activeTab === 'code' ? 'active' : ''}
            onClick={() => setActiveTab('code')}
          >
            <Icon name="terminal" size={18} />
            <span>Contoh Kode & Output</span>
          </button>
        )}
        {practiceSection && (
          <button
            type="button"
            role="tab"
            aria-selected={activeTab === 'practice'}
            className={activeTab === 'practice' ? 'active' : ''}
            onClick={() => setActiveTab('practice')}
          >
            <Icon name="fitness_center" size={18} />
            <span>Latihan & Kuis Konsep</span>
          </button>
        )}
        {assignmentSection && (
          <button
            type="button"
            role="tab"
            aria-selected={activeTab === 'assignment'}
            className={activeTab === 'assignment' ? 'active' : ''}
            onClick={() => setActiveTab('assignment')}
          >
            <Icon name="assignment" size={18} />
            <span>Tugas & Rubrik Penilaian</span>
          </button>
        )}
      </div>

      {/* Tab Panels */}
      <div className="chapter-tab-content">
        {/* Tab: Overview */}
        {activeTab === 'overview' && (
          <div className="tab-pane-overview">
            <div className="chapter-preview-grid">
              <PrerequisiteList prerequisites={chapter.prerequisites} />
              <LearningObjectives objectives={chapter.learningObjectives} />
            </div>

            {overviewChildren}

            {(() => {
              const res = getChapterResources(chapter.id);
              return (
                <ResourceDownloads
                  pptxUrl={res.powerpoint}
                  starterCodeUrl={res.pythonFiles[0] || (chapter.resources?.starterCode ? `downloads/chapter-${chapter.number}/contoh.py` : undefined)}
                  guideUrl={res.assignmentGuide || (chapter.resources?.assignmentGuide ? `downloads/chapter-${chapter.number}/tugas.md` : undefined)}
                />
              );
            })()}
          </div>
        )}

        {/* Tab: Code & Output */}
        {activeTab === 'code' && codeSection && (
          <div className="tab-pane-code">{codeSection}</div>
        )}

        {/* Tab: Practice & Quiz */}
        {activeTab === 'practice' && practiceSection && (
          <div className="tab-pane-practice">{practiceSection}</div>
        )}

        {/* Tab: Assignment */}
        {activeTab === 'assignment' && assignmentSection && (
          <div className="tab-pane-assignment">{assignmentSection}</div>
        )}
      </div>

      {/* Navigation to Prev / Next */}
      <ChapterNavigation
        prevChapter={prevChapter}
        nextChapter={nextChapter}
        onNavigate={(targetId) => onNavigateChapter(targetId)}
      />
    </div>
  );
}
