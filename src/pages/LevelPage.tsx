import { LEVELS, CHAPTERS, type Level, type Chapter } from '../curriculum';
import { DifficultyBadge } from '../components/DifficultyBadge';
import { Icon } from '../ui/Icon';

interface LevelPageProps {
  levelId: number;
  onNavigateHome: () => void;
  onNavigateChapter: (chapterId: number) => void;
  onNavigateLevel: (levelId: number) => void;
}

export function LevelPage({
  levelId,
  onNavigateHome,
  onNavigateChapter,
  onNavigateLevel,
}: LevelPageProps) {
  const level: Level | undefined = LEVELS.find((l) => l.id === levelId);

  if (!level) {
    return (
      <div className="hub-page-container document placeholder">
        <div className="eyebrow">LEVEL TIDAK DITEMUKAN</div>
        <h1>Level {levelId} Belum Terdaftar</h1>
        <p>Silakan kembali ke beranda untuk memilih level 1, 2, atau 3.</p>
        <button type="button" className="button primary" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={18} /> <span>Kembali ke Beranda</span>
        </button>
      </div>
    );
  }

  const levelChapters = CHAPTERS.filter((ch) => ch.levelId === levelId);

  return (
    <div className="hub-level-page">
      {/* Top Breadcrumb & Nav */}
      <div className="page-breadcrumb">
        <button type="button" className="breadcrumb-back-btn" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={16} />
          <span>Kembali ke Hub Utama</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">Level {level.id}: {level.title}</span>
      </div>

      {/* Level Header Banner */}
      <header className="level-header-banner">
        <div className="level-badge-row">
          <span className="level-badge">{level.badge}</span>
          <span className="level-range-pill">{level.chapterRange}</span>
          <span className="level-alignment-pill">
            <Icon name="verified" size={16} /> {level.alignment}
          </span>
        </div>

        <h1 className="level-title">{level.title}</h1>
        <p className="level-subtitle">{level.subtitle}</p>
        <p className="level-overview-text">{level.overview}</p>
      </header>

      {/* Competencies & Prerequisites Row */}
      <section className="level-spec-grid">
        <div className="spec-card">
          <div className="spec-card-header">
            <Icon name="target" size={20} />
            <h3>Target Kompetensi Utama</h3>
          </div>
          <ul className="spec-list">
            {level.competencyTargets.map((item, idx) => (
              <li key={idx}>
                <Icon name="check_circle" size={16} className="item-icon" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="spec-card">
          <div className="spec-card-header">
            <Icon name="psychology" size={20} />
            <h3>Capaian Pembelajaran (Learning Outcomes)</h3>
          </div>
          <ul className="spec-list">
            {level.learningOutcomes.map((item, idx) => (
              <li key={idx}>
                <Icon name="emoji_events" size={16} className="item-icon" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="spec-card">
          <div className="spec-card-header">
            <Icon name="rule" size={20} />
            <h3>Prasyarat Pengetahuan</h3>
          </div>
          <ul className="spec-list">
            {level.prerequisites.map((item, idx) => (
              <li key={idx}>
                <Icon name="arrow_forward" size={16} className="item-icon" />
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* Capstone Project Card */}
      <section className="level-capstone-section">
        <div className="capstone-card">
          <div className="capstone-icon-wrapper">
            <Icon name="workspace_premium" size={32} />
          </div>
          <div className="capstone-body">
            <div className="capstone-eyebrow">FINAL INTEGRATION PROJECT</div>
            <h3 className="capstone-title">{level.capstoneTitle}</h3>
            <p className="capstone-desc">{level.capstoneDescription}</p>
          </div>
        </div>
      </section>

      {/* Level Chapter List */}
      <section className="level-chapters-section">
        <div className="section-heading-clean">
          <div>
            <div className="eyebrow">DAFTAR CHAPTER LEVEL {level.id}</div>
            <h2>Silabus {levelChapters.length} Chapter Pembelajaran</h2>
          </div>
          <p>
            Materi disusun secara modular. Selesaikan chapter berurutan untuk pemahaman konsep yang maksimal.
          </p>
        </div>

        <div className="level-chapters-list">
          {levelChapters.map((ch: Chapter) => (
            <article
              key={ch.id}
              className={`level-chapter-row ${ch.available ? 'available' : 'upcoming'}`}
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
              <div className="row-left">
                <div className="row-number">Ch {ch.number}</div>
                <div className="row-info">
                  <div className="row-top-badges">
                    <DifficultyBadge difficulty={ch.difficulty} />
                    <span className="row-hours">
                      <Icon name="schedule" size={14} /> {ch.estimatedHours} jam
                    </span>
                    <span className="row-competency">{ch.competencyFocus}</span>
                  </div>
                  <h3 className="row-title">{ch.title}</h3>
                  <p className="row-sub">{ch.subtitle}</p>
                  <p className="row-desc">{ch.description}</p>
                  <div className="row-tags">
                    {ch.tags.map((tag) => (
                      <span key={tag} className="tag-chip">
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              </div>

              <div className="row-right">
                <div className="row-status-box">
                  {ch.available ? (
                    <span className="status-badge ready">● Tersedia</span>
                  ) : (
                    <span className="status-badge upcoming">Segera Hadir</span>
                  )}
                </div>
                <button
                  type="button"
                  className={`button ${ch.available ? 'primary' : 'subtle'} row-btn`}
                  onClick={(e) => {
                    e.stopPropagation();
                    onNavigateChapter(ch.id);
                  }}
                >
                  <span>{ch.available ? 'Buka Chapter' : 'Detail Silabus'}</span>
                  <Icon name="arrow_forward" size={16} />
                </button>
              </div>
            </article>
          ))}
        </div>
      </section>

      {/* Level Navigation Footer */}
      <footer className="level-nav-footer">
        {level.id > 1 ? (
          <button
            type="button"
            className="button subtle"
            onClick={() => onNavigateLevel(level.id - 1)}
          >
            <Icon name="arrow_back" size={18} />
            <span>Kembali ke Level {level.id - 1}</span>
          </button>
        ) : (
          <button type="button" className="button subtle" onClick={onNavigateHome}>
            <Icon name="home" size={18} />
            <span>Beranda Hub</span>
          </button>
        )}

        {level.id < 3 ? (
          <button
            type="button"
            className="button primary"
            onClick={() => onNavigateLevel(level.id + 1)}
          >
            <span>Lanjut ke Level {level.id + 1}</span>
            <Icon name="arrow_forward" size={18} />
          </button>
        ) : (
          <button type="button" className="button primary" onClick={onNavigateHome}>
            <span>Jelajahi Spesialisasi</span>
            <Icon name="explore" size={18} />
          </button>
        )}
      </footer>
    </div>
  );
}
