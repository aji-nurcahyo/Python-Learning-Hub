import { useState } from 'react';
import {
  LEVELS,
  CHAPTERS,
  SPECIALIZATION_TRACKS,
  CURRICULUM_DISCLAIMER,
  type Level,
  type Chapter,
} from '../curriculum';
import { DifficultyBadge } from '../components/DifficultyBadge';
import { Icon } from '../ui/Icon';
import { getAssetUrl } from '../curriculum/resources';

interface HomePageProps {
  onNavigateLevel: (levelId: number) => void;
  onNavigateTrack: (trackId: string) => void;
  onNavigateChapter: (chapterId: number) => void;
}

export function HomePage({
  onNavigateLevel,
  onNavigateTrack,
  onNavigateChapter,
}: HomePageProps) {
  const [levelFilter, setLevelFilter] = useState<'all' | '1' | '2' | '3'>('all');
  const [availabilityFilter, setAvailabilityFilter] = useState<'all' | 'available'>('all');
  const [searchTerm, setSearchTerm] = useState('');

  const filteredChapters = CHAPTERS.filter((ch) => {
    if (levelFilter !== 'all' && ch.levelId !== Number(levelFilter)) {
      return false;
    }
    if (availabilityFilter === 'available' && !ch.available) {
      return false;
    }
    if (searchTerm.trim()) {
      const q = searchTerm.toLowerCase();
      const matchNumber = ch.number.includes(q);
      const matchTitle = ch.title.toLowerCase().includes(q);
      const matchSubtitle = ch.subtitle.toLowerCase().includes(q);
      const matchDesc = ch.description.toLowerCase().includes(q);
      const matchTags = ch.tags.some((t) => t.toLowerCase().includes(q));
      const matchCompetency = ch.competencyFocus.toLowerCase().includes(q);
      if (!matchNumber && !matchTitle && !matchSubtitle && !matchDesc && !matchTags && !matchCompetency) {
        return false;
      }
    }
    return true;
  });

  const availableCount = CHAPTERS.filter((c) => c.available).length;

  return (
    <div className="hub-home-page">
      {/* Hero Section */}
      <section className="hub-hero">
        <div className="hub-hero-inner">
          <div className="hero-eyebrow">
            <span className="status-dot pulsing" />
            <span>Learn Python, One Chapter at a Time</span>
          </div>
          <h1 className="hero-main-title">
            Python Learning Hub
          </h1>
          <p className="hero-subheading">
            Interactive Python Learning Modules
          </p>
          <p className="hero-subtext">
            Explore Python programming through structured learning modules, interactive presentations, practical coding examples, and hands-on exercises. Platform mencakup 3 Level Kompetensi, 30 Chapter Terstruktur, dan 5 Jalur Spesialisasi Industri.
          </p>
          <div className="hero-cta-group">
            <button
              type="button"
              className="button primary button-lg"
              onClick={() => onNavigateLevel(1)}
            >
              <span>Mulai Level 1 (Foundations)</span>
              <Icon name="arrow_forward" size={20} />
            </button>
            <a href="#curriculum-browser" className="button subtle button-lg">
              <span>Jelajahi 30 Chapter</span>
              <Icon name="explore" size={20} />
            </a>
          </div>

          <div className="hub-stats-bar">
            <div className="stat-item">
              <span className="stat-number">3</span>
              <span className="stat-label">Level Kompetensi</span>
            </div>
            <div className="stat-separator" />
            <div className="stat-item">
              <span className="stat-number">30</span>
              <span className="stat-label">Chapter Terstruktur</span>
            </div>
            <div className="stat-separator" />
            <div className="stat-item">
              <span className="stat-number">5</span>
              <span className="stat-label">Jalur Spesialisasi</span>
            </div>
            <div className="stat-separator" />
            <div className="stat-item">
              <span className="stat-number">{availableCount}</span>
              <span className="stat-label">Chapter Siap Belajar</span>
            </div>
          </div>
        </div>
      </section>

      {/* 3 Main Competency Levels */}
      <section className="hub-levels-section" id="levels">
        <div className="section-header-centered">
          <div className="eyebrow">STRUKTUR KOMPETENSI BERTAHAP</div>
          <h2>Tiga Tingkat Kemahiran Python</h2>
          <p>
            Kurikulum dirancang berjenjang dari logika dasar hingga rekayasa sistem produksi tingkat lanjut.
          </p>
        </div>

        <div className="levels-card-grid">
          {LEVELS.map((level: Level) => (
            <div key={level.id} className={`level-card level-${level.id}`}>
              <div className="level-card-top">
                <span className="level-badge">{level.badge}</span>
                <span className="level-range">{level.chapterRange}</span>
              </div>
              <h3 className="level-card-title">{level.title}</h3>
              <p className="level-card-sub">{level.subtitle}</p>
              <div className="level-alignment-pill">
                <Icon name="verified" size={16} />
                <span>{level.alignment}</span>
              </div>
              <p className="level-card-desc">{level.overview}</p>

              <div className="level-competencies-preview">
                <strong>Fokus Kompetensi:</strong>
                <ul>
                  {level.competencyTargets.slice(0, 3).map((target, idx) => (
                    <li key={idx}>{target}</li>
                  ))}
                </ul>
              </div>

              <div className="level-capstone-snippet">
                <Icon name="workspace_premium" size={18} />
                <div>
                  <span className="capstone-label">Capstone Project:</span>
                  <span className="capstone-name">{level.capstoneTitle}</span>
                </div>
              </div>

              <div className="level-card-footer">
                <button
                  type="button"
                  className="button primary button-block"
                  onClick={() => onNavigateLevel(level.id)}
                >
                  <span>Masuk ke Level {level.id}</span>
                  <Icon name="arrow_forward" size={18} />
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 5 Specialization Tracks */}
      <section className="hub-tracks-section" id="tracks">
        <div className="section-header-centered">
          <div className="eyebrow">JALUR KARIER & PENERAPAN INDUSTRI</div>
          <h2>5 Spesialisasi Python Terapan</h2>
          <p>
            Setelah membangun fondasi yang kuat, pilih arah spesialisasi sesuai minat karier dan domain komputasi Anda.
          </p>
        </div>

        <div className="tracks-card-grid">
          {SPECIALIZATION_TRACKS.map((track) => (
            <div key={track.id} className="track-card">
              <div className="track-icon-wrapper">
                <Icon name={track.icon} size={32} />
              </div>
              <span className="track-tagline">{track.tagline}</span>
              <h3 className="track-title">{track.title}</h3>
              <p className="track-sub">{track.subtitle}</p>
              <p className="track-desc">{track.description}</p>
              <div className="track-meta">
                <span className="target-pill">
                  <Icon name="person" size={14} /> {track.targetAudience}
                </span>
                <span className="modules-count">
                  <Icon name="layers" size={14} /> {track.modules.length} Modul Terstruktur
                </span>
              </div>
              <button
                type="button"
                className="button subtle track-explore-btn"
                onClick={() => onNavigateTrack(track.id)}
              >
                <span>Pelajari Silabus Track</span>
                <Icon name="arrow_forward" size={16} />
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* Learning Roadmap Visualization */}
      <section className="hub-roadmap-section">
        <div className="section-header-centered">
          <div className="eyebrow">PETA JALAN BELAJAR</div>
          <h2>Roadmap Penguasaan Komprehensif</h2>
          <p>Alur langkah terstruktur dari pemula absolut hingga insinyur perangkat lunak profesional.</p>
        </div>

        <div className="roadmap-flow-container">
          <div className="roadmap-step">
            <div className="step-number">01</div>
            <div className="step-content">
              <h4>Foundations (Ch 01–12)</h4>
              <p>Sintaks Python 3, variabel, logika if/else, perulangan, list, dict, set, dan fungsi modular.</p>
              <span className="roadmap-tag">Sertifikasi: Aligned PCEP</span>
            </div>
          </div>
          <div className="roadmap-arrow">→</div>
          <div className="roadmap-step">
            <div className="step-number">02</div>
            <div className="step-content">
              <h4>Intermediate (Ch 13–22)</h4>
              <p>Algoritma pencarian/pengurutan, penanganan file, exception handling, dan OOP (Class & Inheritence).</p>
              <span className="roadmap-tag">Sertifikasi: Aligned PCAP</span>
            </div>
          </div>
          <div className="roadmap-arrow">→</div>
          <div className="roadmap-step">
            <div className="step-number">03</div>
            <div className="step-content">
              <h4>Professional (Ch 23–30)</h4>
              <p>Decorators, generators, asynchronous programming, REST API integration, type safety & CI/CD.</p>
              <span className="roadmap-tag">Standar Rekayasa Industri</span>
            </div>
          </div>
          <div className="roadmap-arrow">→</div>
          <div className="roadmap-step highlight">
            <div className="step-number">04</div>
            <div className="step-content">
              <h4>Specialization & Capstones</h4>
              <p>Pilih salah satu dari 5 jalur spesialisasi untuk membangun portofolio proyek dunia nyata.</p>
              <span className="roadmap-tag">Portofolio & Capstone</span>
            </div>
          </div>
        </div>
      </section>

      {/* Chapter Browser Section */}
      <section className="hub-browser-section" id="curriculum-browser">
        <div className="browser-header">
          <div>
            <div className="eyebrow">KATALOG CHAPTER PEMBELAJARAN</div>
            <h2>Eksplorasi Seluruh 30 Chapter</h2>
            <p>Telusuri materi, tujuan pembelajaran, dan buka chapter yang telah tersedia.</p>
          </div>
        </div>

        {/* Filter and Search Bar */}
        <div className="hub-filter-bar">
          <div className="filter-level-buttons" role="group" aria-label="Filter berdasarkan level">
            <button
              type="button"
              className={levelFilter === 'all' ? 'active' : ''}
              onClick={() => setLevelFilter('all')}
            >
              Semua Level (30)
            </button>
            <button
              type="button"
              className={levelFilter === '1' ? 'active' : ''}
              onClick={() => setLevelFilter('1')}
            >
              Level 1 (12)
            </button>
            <button
              type="button"
              className={levelFilter === '2' ? 'active' : ''}
              onClick={() => setLevelFilter('2')}
            >
              Level 2 (10)
            </button>
            <button
              type="button"
              className={levelFilter === '3' ? 'active' : ''}
              onClick={() => setLevelFilter('3')}
            >
              Level 3 (8)
            </button>
          </div>

          <div className="filter-availability-buttons" role="group" aria-label="Filter ketersediaan">
            <button
              type="button"
              className={availabilityFilter === 'all' ? 'active' : ''}
              onClick={() => setAvailabilityFilter('all')}
            >
              Semua Status
            </button>
            <button
              type="button"
              className={availabilityFilter === 'available' ? 'active' : ''}
              onClick={() => setAvailabilityFilter('available')}
            >
              Tersedia ({availableCount})
            </button>
          </div>

          <div className="search-box-wrapper">
            <Icon name="search" size={20} />
            <input
              type="search"
              aria-label="Cari chapter, topik, atau kata kunci"
              placeholder="Cari chapter, konsep, tag (mis: list, OOP, async)..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            {searchTerm && (
              <button
                type="button"
                className="clear-search-btn"
                onClick={() => setSearchTerm('')}
                aria-label="Hapus pencarian"
              >
                <Icon name="close" size={16} />
              </button>
            )}
          </div>
        </div>

        <p className="filter-count-status" role="status">
          Menampilkan {filteredChapters.length} dari 30 chapter
        </p>

        {/* Chapter Grid */}
        <div className="hub-chapters-grid">
          {filteredChapters.map((ch: Chapter) => (
            <article
              key={ch.id}
              className={`hub-chapter-card ${ch.available ? 'available' : 'upcoming'}`}
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
              <div className="ch-card-header">
                <span className="ch-number-badge">Ch {ch.number}</span>
                <div className="ch-status-tags">
                  {ch.available ? (
                    <span className="status-badge ready">● Tersedia</span>
                  ) : (
                    <span className="status-badge upcoming">Segera Hadir</span>
                  )}
                </div>
              </div>

                <div className="ch-card-meta">
                  <span className="ch-level-indicator">Level {ch.levelId}</span>
                  <DifficultyBadge difficulty={ch.difficulty} />
                  <span className="ch-hours">
                    <Icon name="schedule" size={14} /> {ch.estimatedHours} jam
                  </span>
                </div>

                <h3 className="ch-card-title">{ch.title}</h3>
                <p className="ch-card-sub">{ch.subtitle}</p>
                <p className="ch-card-desc">{ch.description}</p>

                <div className="ch-card-competency">
                  <Icon name="radar" size={14} />
                  <span>{ch.competencyFocus}</span>
                </div>

                <div className="ch-tags-row">
                  {ch.tags.map((tag) => (
                    <span key={tag} className="tag-chip">
                      {tag}
                    </span>
                  ))}
                </div>

                <div className="ch-card-footer">
                  {ch.available ? (
                    <button
                      type="button"
                      className="button primary button-sm"
                      onClick={(e) => {
                        e.stopPropagation();
                        onNavigateChapter(ch.id);
                      }}
                    >
                      <span>Buka Pembelajaran</span>
                      <Icon name="arrow_forward" size={16} />
                    </button>
                  ) : (
                    <span className="upcoming-notice">
                      Rencana Silabus <Icon name="chevron_right" size={16} />
                    </span>
                  )}
                </div>
              </article>
            ))}
        </div>

        {filteredChapters.length === 0 && (
          <div className="hub-empty-state">
            <Icon name="search_off" size={36} />
            <h3>Tidak Ada Chapter yang Cocok</h3>
            <p>Coba gunakan kata kunci lain atau ubah filter level dan ketersediaan di atas.</p>
            <button
              type="button"
              className="button subtle"
              onClick={() => {
                setLevelFilter('all');
                setAvailabilityFilter('all');
                setSearchTerm('');
              }}
            >
              Reset Filter Pencarian
            </button>
          </div>
        )}
      </section>

      {/* Quality & Pedagogy Note */}
      <section className="hub-pedagogy-section">
        <div className="pedagogy-card">
          <div className="pedagogy-symbol">&lt;/&gt;</div>
          <div className="pedagogy-body">
            <h3>Rekayasa Kode Python Terverifikasi</h3>
            <p>
              Seluruh contoh kode dalam platform ini dijalankan menggunakan interpreter CPython standar.
              Hasil eksekusi terminal yang ditampilkan adalah keluaran sistem sebenarnya tanpa simulasi buatan.
              Pelajari kode, uji di mesin lokal Anda, dan bangun intuisi pemrograman yang presisi.
            </p>
          </div>
          <div className="pedagogy-actions">
            <a
              href={getAssetUrl('downloads/Materi_Pengkom_Pertemuan_9_10_Python.pptx')}
              className="button subtle"
              download
            >
              <Icon name="download" size={18} />
              <span>Unduh Slide Sumber (.pptx)</span>
            </a>
          </div>
        </div>
      </section>

      {/* Curriculum Disclaimer Notice */}
      <section className="hub-disclaimer-section">
        <div className="disclaimer-inner">
          <Icon name="gavel" size={20} />
          <p>{CURRICULUM_DISCLAIMER}</p>
        </div>
      </section>
    </div>
  );
}
