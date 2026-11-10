import { SPECIALIZATION_TRACKS, CHAPTERS, type SpecializationTrack, type Chapter } from '../curriculum';
import { getModulesForTrack } from '../curriculum/specializations';
import { DifficultyBadge } from '../components/DifficultyBadge';
import { Icon } from '../ui/Icon';

interface TrackPageProps {
  trackId: string;
  onNavigateHome: () => void;
  onNavigateChapter: (chapterId: number) => void;
  onNavigateTrack: (trackId: string) => void;
  onNavigateSpecModule?: (moduleId: string) => void;
}

export function TrackPage({
  trackId,
  onNavigateHome,
  onNavigateChapter,
  onNavigateTrack,
  onNavigateSpecModule,
}: TrackPageProps) {
  const track: SpecializationTrack | undefined = SPECIALIZATION_TRACKS.find((t) => t.id === trackId);

  if (!track) {
    return (
      <div className="hub-page-container document placeholder">
        <div className="eyebrow">TRACK TIDAK DITEMUKAN</div>
        <h1>Spesialisasi Tidak Tersedia</h1>
        <p>Jalur spesialisasi yang Anda cari tidak ditemukan dalam kurikulum.</p>
        <button type="button" className="button primary" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={18} /> <span>Kembali ke Beranda</span>
        </button>
      </div>
    );
  }

  const recommendedChaptersList: Chapter[] = track.recommendedChapters
    .map((num) => CHAPTERS.find((c) => c.id === num))
    .filter((c): c is Chapter => c !== undefined);

  const implementedModules = getModulesForTrack(track.id);

  return (
    <div className="hub-track-page">
      {/* Breadcrumb */}
      <div className="page-breadcrumb">
        <button type="button" className="breadcrumb-back-btn" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={16} />
          <span>Kembali ke Hub Utama</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">{track.title}</span>
      </div>

      {/* Track Banner */}
      <header className="track-header-banner">
        <div className="track-header-top">
          <div className="track-icon-large">
            <Icon name={track.icon} size={40} />
          </div>
          <div>
            <span className="track-eyebrow">JALUR SPESIALISASI INDUSTRI</span>
            <h1 className="track-header-title">{track.title}</h1>
            <p className="track-header-sub">{track.subtitle}</p>
          </div>
        </div>

        <div className="track-quote-box">
          <Icon name="format_quote" size={24} />
          <span>{track.tagline}</span>
        </div>

        <p className="track-header-desc">{track.description}</p>

        <div className="track-header-pills">
          <div className="pill-target">
            <Icon name="work" size={16} />
            <span>Target Profesi: <strong>{track.targetAudience}</strong></span>
          </div>
          <div className="pill-modules">
            <Icon name="view_module" size={16} />
            <span>{track.modules.length} Modul Terstruktur</span>
          </div>
        </div>
      </header>

      {/* Recommended Core Chapters */}
      <section className="track-prereqs-section">
        <div className="section-heading-clean">
          <div>
            <div className="eyebrow">FONDASI KURIKULUM YANG DIREKOMENDASIKAN</div>
            <h2>Chapter Fondasi Wajib untuk Jalur Ini</h2>
          </div>
          <p>
            Sebelum mendalami modul spesialisasi teknis, pastikan Anda telah menyelesaikan atau memahami konsep pada chapter-chapter berikut:
          </p>
        </div>

        <div className="track-recommended-grid">
          {recommendedChaptersList.map((ch) => (
            <div
              key={ch.id}
              className={`track-rec-card ${ch.available ? 'available' : 'upcoming'}`}
              onClick={() => onNavigateChapter(ch.id)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault();
                  onNavigateChapter(ch.id);
                }
              }}
            >
              <div className="rec-card-top">
                <span className="rec-num">Ch {ch.number}</span>
                <span className={`status-badge ${ch.available ? 'ready' : 'upcoming'}`}>
                  {ch.available ? 'Tersedia' : 'Segera Hadir'}
                </span>
              </div>
              <h4 className="rec-title">{ch.title}</h4>
              <p className="rec-sub">{ch.subtitle}</p>
              <div className="rec-meta">
                <DifficultyBadge difficulty={ch.difficulty} />
                <span>Level {ch.levelId}</span>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Track Modules Syllabus */}
      <section className="track-modules-section">
        <div className="section-heading-clean">
          <div>
            <div className="eyebrow">SILABUS MODUL SPESIALISASI</div>
            <h2>Daftar Modul Pembelajaran Teknis</h2>
          </div>
          <p>
            Modul-modul ini mengajarkan library, pola desain, dan algoritma terapan spesifik industri.
          </p>
        </div>

        <div className="track-modules-list">
          {implementedModules.length > 0
            ? implementedModules.map((mod) => (
                <article
                  key={mod.id}
                  className="track-module-row clickable-module-row"
                  role="button"
                  tabIndex={0}
                  onClick={() =>
                    onNavigateSpecModule
                      ? onNavigateSpecModule(mod.id)
                      : (location.hash = `spec/${mod.id}`)
                  }
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      if (onNavigateSpecModule) onNavigateSpecModule(mod.id);
                      else location.hash = `spec/${mod.id}`;
                    }
                  }}
                >
                  <div className="module-number-badge">{mod.id}</div>
                  <div className="module-info">
                    <div className="module-status-line" style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
                      <span className={`module-status-chip ${mod.isCapstone ? 'project' : 'spec'}`}>
                        {mod.isCapstone ? 'Capstone Project' : 'Specialization Module'}
                      </span>
                      <DifficultyBadge difficulty={mod.difficulty} />
                      <span className="ch-hours">
                        <Icon name="schedule" size={14} /> {mod.estimatedHours} jam
                      </span>
                    </div>
                    <h3 className="module-title">{mod.title}</h3>
                    <p className="module-desc">{mod.description}</p>
                  </div>
                  <div className="row-right">
                    <button
                      type="button"
                      className="button primary button-sm"
                      onClick={(e) => {
                        e.stopPropagation();
                        if (onNavigateSpecModule) onNavigateSpecModule(mod.id);
                        else location.hash = `spec/${mod.id}`;
                      }}
                    >
                      <span>Buka Modul {mod.id}</span>
                      <Icon name="arrow_forward" size={16} />
                    </button>
                  </div>
                </article>
              ))
            : track.modules.map((mod, idx) => (
                <div key={idx} className="track-module-row">
                  <div className="module-number-badge">{String(idx + 1).padStart(2, '0')}</div>
                  <div className="module-info">
                    <div className="module-status-line">
                      <span
                        className={`module-status-chip ${
                          mod.status === 'Advanced Project'
                            ? 'project'
                            : mod.status === 'Core Prerequisite'
                            ? 'core'
                            : 'spec'
                        }`}
                      >
                        {mod.status}
                      </span>
                    </div>
                    <h3 className="module-title">{mod.title}</h3>
                    <p className="module-desc">{mod.description}</p>
                  </div>
                </div>
              ))}
        </div>
      </section>

      {/* Other Tracks Browser */}
      <section className="track-other-section">
        <h3>Jelajahi Jalur Spesialisasi Lainnya</h3>
        <div className="other-tracks-pills">
          {SPECIALIZATION_TRACKS.filter((t) => t.id !== track.id).map((other) => (
            <button
              key={other.id}
              type="button"
              className="other-track-btn"
              onClick={() => onNavigateTrack(other.id)}
            >
              <Icon name={other.icon} size={18} />
              <span>{other.title}</span>
            </button>
          ))}
        </div>
      </section>

      {/* Navigation Footer */}
      <footer className="track-nav-footer">
        <button type="button" className="button subtle" onClick={onNavigateHome}>
          <Icon name="home" size={18} />
          <span>Kembali ke Beranda Hub</span>
        </button>
      </footer>
    </div>
  );
}

