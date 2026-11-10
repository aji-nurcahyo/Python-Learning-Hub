import { useState } from 'react';
import {
  getSpecializationModuleById,
  getModulesForTrack,
  type SpecializationModule,
} from '../curriculum/specializations';
import specOutputs from '../code/spec-outputs.json';
import { DifficultyBadge } from '../components/DifficultyBadge';
import { PrerequisiteList } from '../components/PrerequisiteList';
import { LearningObjectives } from '../components/LearningObjectives';
import { ResourceDownloads } from '../components/ResourceDownloads';
import { CodeBlock } from '../components/CodeBlock';
import { CodeOutput } from '../components/CodeOutput';
import { ExerciseSection } from '../components/ExerciseSection';
import { AssignmentSection } from '../components/AssignmentSection';
import { Icon } from '../ui/Icon';

interface SpecializationModulePageProps {
  moduleId: string;
  onNavigateHome: () => void;
  onNavigateTrack: (trackId: string) => void;
  onNavigateSpecModule: (moduleId: string) => void;
  onNavigateSpecSlides: (moduleId: string) => void;
  onNavigateSpecReading: (moduleId: string) => void;
  onNavigateSpecTask: (moduleId: string) => void;
}

export function SpecializationModulePage({
  moduleId,
  onNavigateHome,
  onNavigateTrack,
  onNavigateSpecModule,
  onNavigateSpecSlides,
  onNavigateSpecReading,
  onNavigateSpecTask,
}: SpecializationModulePageProps) {
  const [activeTab, setActiveTab] = useState<'overview' | 'code' | 'practice' | 'assignment'>('overview');

  const mod: SpecializationModule | undefined = getSpecializationModuleById(moduleId);

  if (!mod) {
    return (
      <div className="hub-page-container document placeholder">
        <div className="eyebrow">MODUL SPESIALISASI TIDAK DITEMUKAN</div>
        <h1>Modul {moduleId} Belum Tersedia</h1>
        <p>Silakan kembali ke beranda atau pilih jalur spesialisasi yang tersedia.</p>
        <button type="button" className="button primary" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={18} /> <span>Kembali ke Beranda Hub</span>
        </button>
      </div>
    );
  }

  const trackModules = getModulesForTrack(mod.trackId);
  const idx = trackModules.findIndex((m) => m.id === mod.id);
  const prevMod = idx > 0 ? trackModules[idx - 1] : undefined;
  const nextMod = idx >= 0 && idx < trackModules.length - 1 ? trackModules[idx + 1] : undefined;

  const outputText = mod.codeExample?.outputKey
    ? (specOutputs as Record<string, string>)[mod.codeExample.outputKey] || ''
    : '';

  return (
    <div className="hub-chapter-page active-view">
      {/* Breadcrumb */}
      <div className="page-breadcrumb">
        <button
          type="button"
          className="breadcrumb-back-btn"
          onClick={() => onNavigateTrack(mod.trackId)}
        >
          <Icon name="arrow_back" size={16} />
          <span>{mod.trackTitle}</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">
          {mod.id}: {mod.title}
        </span>
      </div>

      {/* Header Banner */}
      <header className="chapter-header-banner">
        <div className="chapter-meta-badges">
          <span className="status-badge ready">● Tersedia</span>
          <span className="ch-level-chip">Specialization · {mod.id}</span>
          <DifficultyBadge difficulty={mod.difficulty} />
          <span className="ch-hours-chip">
            <Icon name="schedule" size={14} /> {mod.estimatedHours} jam pembelajaran
          </span>
        </div>

        <h1 className="chapter-title">
          <span className="ch-num-prefix">Modul {mod.id} ·</span> {mod.title}
        </h1>
        <p className="chapter-subtitle">{mod.subtitle}</p>
        <p className="chapter-desc">{mod.description}</p>

        {mod.dependencies && mod.dependencies.length > 0 && (
          <div className="chapter-competency-alert">
            <Icon name="inventory_2" size={20} />
            <div>
              <strong>Python Libraries &amp; Dependencies:</strong>
              <p>{mod.dependencies.join(' • ')}</p>
            </div>
          </div>
        )}

        {/* Action Launch Buttons */}
        <div className="chapter-launch-bar">
          <div className="launch-group">
            {mod.resources.hasSlides && mod.slides.length > 0 && (
              <button
                type="button"
                className="button primary button-lg"
                onClick={() => onNavigateSpecSlides(mod.id)}
              >
                <Icon name="slideshow" size={20} />
                <span>Buka Slide</span>
              </button>
            )}
            <button
              type="button"
              className="button subtle button-lg"
              onClick={() => onNavigateSpecReading(mod.id)}
            >
              <Icon name="menu_book" size={20} />
              <span>Baca Materi</span>
            </button>
            <button
              type="button"
              className="button subtle button-lg"
              onClick={() => onNavigateSpecTask(mod.id)}
            >
              <Icon name="assignment" size={20} />
              <span>Lihat Tugas</span>
            </button>
          </div>
        </div>
      </header>

      {/* Tabs Navigation */}
      <div className="chapter-tabs-nav" role="tablist">
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'overview'}
          className={activeTab === 'overview' ? 'active' : ''}
          onClick={() => setActiveTab('overview')}
        >
          <Icon name="info" size={18} />
          <span>Ikhtisar &amp; Kompetensi</span>
        </button>
        {mod.exampleCode && (
          <button
            type="button"
            role="tab"
            aria-selected={activeTab === 'code'}
            className={activeTab === 'code' ? 'active' : ''}
            onClick={() => setActiveTab('code')}
          >
            <Icon name="terminal" size={18} />
            <span>Contoh Kode &amp; Output</span>
          </button>
        )}
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'practice'}
          className={activeTab === 'practice' ? 'active' : ''}
          onClick={() => setActiveTab('practice')}
        >
          <Icon name="fitness_center" size={18} />
          <span>Latihan &amp; Kuis Konsep</span>
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={activeTab === 'assignment'}
          className={activeTab === 'assignment' ? 'active' : ''}
          onClick={() => setActiveTab('assignment')}
        >
          <Icon name="assignment" size={18} />
          <span>Tugas &amp; Rubrik Penilaian</span>
        </button>
      </div>

      {/* Tab Content */}
      <div className="chapter-tab-content">
        {activeTab === 'overview' && (
          <div className="tab-pane-overview">
            <div className="chapter-preview-grid">
              <PrerequisiteList prerequisites={mod.prerequisites} />
              <LearningObjectives objectives={mod.learningObjectives} />
            </div>

            <div className="pedagogy-callout">
              <Icon name="psychology" size={24} />
              <div>
                <h4>Alur Belajar Modul Spesialisasi</h4>
                <p>
                  Mulailah dengan mempelajari slide, kemudian baca penjelasan materi terperinci, coba contoh kode dengan dataset atau skrip lokal Anda, dan selesaikan proyek terapan.
                </p>
              </div>
            </div>

            <ResourceDownloads
              pptxUrl={mod.resources.pptxDownload || null}
              starterCodeUrl={mod.resources.codeDownload || null}
              notebookUrl={mod.resources.notebookDownload || null}
              datasetUrl={mod.resources.datasetDownload || null}
              guideUrl={mod.resources.guideDownload || null}
            />

            {mod.references && mod.references.length > 0 && (
              <div className="tutorial-references-card" style={{ marginTop: '24px', marginBottom: 0 }}>
                <div className="references-header">
                  <Icon name="link" size={18} />
                  <h4>Referensi &amp; Dokumentasi Otoritatif</h4>
                </div>
                <ul className="references-links">
                  {mod.references.map((ref, rIdx) => (
                    <li key={rIdx}>
                      <a href={ref.url} target="_blank" rel="noopener noreferrer">
                        <span>
                          {ref.title} — {ref.source}
                          {ref.license ? ` (${ref.license})` : ''}
                        </span>
                        <Icon name="open_in_new" size={14} />
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}

        {activeTab === 'code' && mod.exampleCode && (
          <div className="tab-pane-code">
            <div className="section-heading-clean">
              <div>
                <div className="eyebrow">CONTOH KODE PYTHON · {mod.id}</div>
                <h3>{mod.codeExample.title}</h3>
              </div>
              <p>Pelajari implementasi kode Python berikut beserta keluaran program di terminal.</p>
            </div>

            <div className="code-output-side-by-side">
              <div className="code-side">
                <CodeBlock code={mod.exampleCode} filename={mod.codeExample.filename} />
              </div>
              <div className="output-side">
                <CodeOutput output={outputText} />
              </div>
            </div>

            <div className="code-explanation-card">
              <Icon name="lightbulb" size={20} />
              <div>
                <strong>Penjelasan Mekanisme:</strong>
                <p>{mod.codeExample.explanation}</p>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'practice' && (
          <div className="tab-pane-practice">
            <ExerciseSection exercise={mod.exercise} quiz={mod.quiz} />
          </div>
        )}

        {activeTab === 'assignment' && (
          <div className="tab-pane-assignment">
            <AssignmentSection
              assignment={{
                ...mod.assignment,
                starterCode: mod.starterCode || undefined,
              }}
            />
          </div>
        )}
      </div>

      {/* Prev / Next Navigation within Track */}
      <nav className="chapter-nav-bar" aria-label="Navigasi antar modul dalam track">
        {prevMod ? (
          <button
            type="button"
            className="chapter-nav-btn prev"
            onClick={() => onNavigateSpecModule(prevMod.id)}
          >
            <Icon name="arrow_back" size={18} />
            <div className="nav-meta">
              <span className="nav-dir">Modul Sebelumnya</span>
              <span className="nav-title">
                {prevMod.id}: {prevMod.title}
              </span>
            </div>
          </button>
        ) : (
          <div className="chapter-nav-spacer" />
        )}

        {nextMod ? (
          <button
            type="button"
            className="chapter-nav-btn next"
            onClick={() => onNavigateSpecModule(nextMod.id)}
          >
            <div className="nav-meta">
              <span className="nav-dir">Modul Berikutnya</span>
              <span className="nav-title">
                {nextMod.id}: {nextMod.title}
              </span>
            </div>
            <Icon name="arrow_forward" size={18} />
          </button>
        ) : (
          <button
            type="button"
            className="chapter-nav-btn next"
            onClick={() => onNavigateTrack(mod.trackId)}
          >
            <div className="nav-meta">
              <span className="nav-dir">Selesai Track</span>
              <span className="nav-title">Kembali ke Ikhtisar {mod.trackTitle}</span>
            </div>
            <Icon name="emoji_events" size={18} />
          </button>
        )}
      </nav>
    </div>
  );
}

