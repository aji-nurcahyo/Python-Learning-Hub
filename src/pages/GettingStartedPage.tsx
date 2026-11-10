import { useState, useEffect } from 'react';
import {
  GETTING_STARTED_TUTORIALS,
  type GettingStartedTutorial,
  type PlatformCommands,
} from '../curriculum/getting-started';
import { Icon } from '../ui/Icon';
import { CodeBlock } from '../components/CodeBlock';
import { CodeOutput } from '../components/CodeOutput';

interface GettingStartedPageProps {
  onNavigateHome: () => void;
  onNavigateLevel: (levelId: number) => void;
  onNavigateChapter: (chapterId: number) => void;
  initialTutorialId?: string;
}

export function GettingStartedPage({
  onNavigateHome,
  onNavigateLevel,
  onNavigateChapter,
  initialTutorialId,
}: GettingStartedPageProps) {
  const [activeTutorialId, setActiveTutorialId] = useState<string>(() => {
    if (initialTutorialId && GETTING_STARTED_TUTORIALS.some((t) => t.id === initialTutorialId)) {
      return initialTutorialId;
    }
    return GETTING_STARTED_TUTORIALS[0].id;
  });

  const [activePlatform, setActivePlatform] = useState<'windows' | 'linux' | 'macos'>('windows');
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  // Sync state if initialTutorialId changes from outside
  useEffect(() => {
    if (initialTutorialId && GETTING_STARTED_TUTORIALS.some((t) => t.id === initialTutorialId)) {
      setActiveTutorialId(initialTutorialId);
    }
  }, [initialTutorialId]);

  const activeTutorial: GettingStartedTutorial =
    GETTING_STARTED_TUTORIALS.find((t) => t.id === activeTutorialId) || GETTING_STARTED_TUTORIALS[0];

  const currentIndex = GETTING_STARTED_TUTORIALS.findIndex((t) => t.id === activeTutorial.id);
  const prevTutorial = currentIndex > 0 ? GETTING_STARTED_TUTORIALS[currentIndex - 1] : null;
  const nextTutorial = currentIndex < GETTING_STARTED_TUTORIALS.length - 1 ? GETTING_STARTED_TUTORIALS[currentIndex + 1] : null;

  const handleCopyCommand = async (text: string, index: number) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedIndex(index);
      setTimeout(() => setCopiedIndex(null), 2000);
    } catch {
      setCopiedIndex(null);
    }
  };

  const getPlatformCommand = (commands: PlatformCommands): string => {
    return commands[activePlatform] || commands.windows;
  };

  const selectTutorial = (id: string) => {
    setActiveTutorialId(id);
    location.hash = `getting-started/${id}`;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="hub-getting-started-page">
      {/* Breadcrumb Navigation */}
      <div className="page-breadcrumb">
        <button type="button" className="breadcrumb-back-btn" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={16} />
          <span>Kembali ke Beranda</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">Getting Started with Python</span>
      </div>

      {/* Main Hero Header */}
      <header className="getting-started-header-banner">
        <div className="header-eyebrow">
          <Icon name="handyman" size={16} />
          <span>PANDUAN SETUP & DEVELOPMENT ENVIRONMENT</span>
        </div>
        <h1 className="header-title">Getting Started with Python</h1>
        <p className="header-subtitle">Python Development Environment Setup</p>
        <p className="header-description">
          Panduan komprehensif penyiapan lingkungan kerja pemrograman Python untuk pemula dan profesional.
          Pelajari instalasi Python Interpreter resmi, konfigurasi VS Code, penggunaan JupyterLab, isolasi dependensi
          Virtual Environment, eksekusi proyek berbasis terminal, hingga verifikasi diagnostik bebas kendala.
        </p>

        <div className="quick-stats-row">
          <div className="quick-stat-badge">
            <Icon name="menu_book" size={16} />
            <span>8 Modul Tutorial Praktis</span>
          </div>
          <div className="quick-stat-badge">
            <Icon name="devices" size={16} />
            <span>Multi-Platform: Windows, Linux, macOS</span>
          </div>
          <div className="quick-stat-badge">
            <Icon name="verified_user" size={16} />
            <span>Standar Industri & Praktik Aman</span>
          </div>
        </div>
      </header>

      {/* Two-Column Layout: Sidebar Navigation + Tutorial Content */}
      <div className="getting-started-content-grid">
        {/* Sidebar Tutorial Navigator */}
        <aside className="tutorial-sidebar" aria-label="Daftar Tutorial Getting Started">
          <div className="sidebar-sticky-wrapper">
            <h3 className="sidebar-title">
              <Icon name="checklist" size={18} />
              <span>Daftar Tutorial</span>
            </h3>
            <nav className="tutorial-nav-list">
              {GETTING_STARTED_TUTORIALS.map((tut) => {
                const isActive = tut.id === activeTutorial.id;
                return (
                  <button
                    key={tut.id}
                    type="button"
                    className={`tutorial-nav-item ${isActive ? 'active' : ''}`}
                    onClick={() => selectTutorial(tut.id)}
                  >
                    <span className="nav-item-number">{tut.number}</span>
                    <div className="nav-item-text">
                      <span className="nav-item-title">{tut.title}</span>
                      <span className="nav-item-time">{tut.estimatedMinutes} menit baca</span>
                    </div>
                    {isActive && <Icon name="chevron_right" size={18} className="nav-active-arrow" />}
                  </button>
                );
              })}
            </nav>

            <div className="sidebar-callout">
              <Icon name="school" size={20} />
              <p>
                Selesai setup? Lanjutkan ke <strong>Chapter 01: Introduction to Python</strong>.
              </p>
              <button
                type="button"
                className="button primary button-sm"
                onClick={() => onNavigateChapter(1)}
              >
                <span>Buka Chapter 01</span>
                <Icon name="arrow_forward" size={14} />
              </button>
            </div>
          </div>
        </aside>

        {/* Main Tutorial View */}
        <main className="tutorial-main-body">
          <article className="tutorial-card">
            {/* Tutorial Header */}
            <div className="tutorial-header-row">
              <div className="tutorial-number-pill">TUTORIAL {activeTutorial.number}</div>
              <div className="tutorial-time-pill">
                <Icon name="schedule" size={14} />
                <span>{activeTutorial.estimatedMinutes} Menit Estimasi</span>
              </div>
            </div>

            <h2 className="tutorial-title">{activeTutorial.title}</h2>
            <p className="tutorial-subtitle">{activeTutorial.subtitle}</p>

            {/* Platform Selector Tabs */}
            <div className="platform-selector-bar">
              <span className="platform-label">Pilih Sistem Operasi Anda:</span>
              <div className="platform-tabs">
                <button
                  type="button"
                  className={`platform-tab ${activePlatform === 'windows' ? 'active' : ''}`}
                  onClick={() => setActivePlatform('windows')}
                >
                  <Icon name="laptop_windows" size={16} />
                  <span>Windows 10 / 11</span>
                </button>
                <button
                  type="button"
                  className={`platform-tab ${activePlatform === 'linux' ? 'active' : ''}`}
                  onClick={() => setActivePlatform('linux')}
                >
                  <Icon name="terminal" size={16} />
                  <span>Linux (Ubuntu / Debian)</span>
                </button>
                <button
                  type="button"
                  className={`platform-tab ${activePlatform === 'macos' ? 'active' : ''}`}
                  onClick={() => setActivePlatform('macos')}
                >
                  <Icon name="laptop_mac" size={16} />
                  <span>macOS</span>
                </button>
              </div>
            </div>

            {/* Learning Objectives Box */}
            <section className="tutorial-objectives-box">
              <div className="objectives-title">
                <Icon name="target" size={18} />
                <h3>Tujuan Pembelajaran</h3>
              </div>
              <ul className="objectives-list">
                {activeTutorial.objectives.map((obj, i) => (
                  <li key={i}>
                    <Icon name="check_circle" size={16} className="objective-icon" />
                    <span>{obj}</span>
                  </li>
                ))}
              </ul>
            </section>

            {/* Prerequisites */}
            {activeTutorial.prerequisites.length > 0 && (
              <section className="tutorial-prerequisites">
                <strong>Prasyarat: </strong>
                <span>{activeTutorial.prerequisites.join(' • ')}</span>
              </section>
            )}

            {/* Step-by-Step Sections */}
            <div className="tutorial-sections-wrapper">
              {activeTutorial.sections.map((sec, secIdx) => {
                return (
                  <section key={secIdx} className="tutorial-step-section">
                    <h3 className="section-heading">
                      <span className="section-number-circle">{secIdx + 1}</span>
                      <span>{sec.heading}</span>
                    </h3>

                    <div className="section-text-content">
                      {sec.explanation.split('\n\n').map((paragraph, pIdx) => (
                        <p key={pIdx}>
                          {paragraph.split('**').map((chunk, cIdx) =>
                            cIdx % 2 === 1 ? <strong key={cIdx}>{chunk}</strong> : chunk
                          )}
                        </p>
                      ))}
                    </div>

                    {/* Platform Command Block if present */}
                    {sec.commands && (
                      <div className="platform-command-box">
                        <div className="command-box-header">
                          <span className="terminal-chip">
                            <Icon name="terminal" size={14} />
                            <span>
                              {activePlatform === 'windows'
                                ? 'PowerShell / Windows Terminal'
                                : activePlatform === 'linux'
                                ? 'Linux Bash / Shell'
                                : 'macOS Terminal (Zsh)'}
                            </span>
                          </span>
                          <button
                            type="button"
                            className="copy-command-btn"
                            onClick={() => handleCopyCommand(getPlatformCommand(sec.commands!), secIdx)}
                          >
                            <Icon name={copiedIndex === secIdx ? 'check' : 'content_copy'} size={14} />
                            <span>{copiedIndex === secIdx ? 'Tersalin!' : 'Salin Perintah'}</span>
                          </button>
                        </div>
                        <pre className="command-pre">
                          <code>{getPlatformCommand(sec.commands)}</code>
                        </pre>
                      </div>
                    )}

                    {/* Python Code Snippet if present */}
                    {sec.codeSnippet && (
                      <div className="tutorial-code-block-wrapper">
                        <CodeBlock
                          code={sec.codeSnippet.code}
                          filename={sec.codeSnippet.filename || 'example.py'}
                        />
                      </div>
                    )}

                    {/* Expected Output */}
                    {sec.expectedOutput && (
                      <div className="tutorial-output-wrapper">
                        <CodeOutput output={sec.expectedOutput} />
                      </div>
                    )}

                    {/* Alert / Callout Box */}
                    {sec.callout && (
                      <div className={`tutorial-callout-card callout-${sec.callout.type}`}>
                        <div className="callout-icon-col">
                          <Icon
                            name={
                              sec.callout.type === 'warning'
                                ? 'warning'
                                : sec.callout.type === 'tip'
                                ? 'lightbulb'
                                : 'info'
                            }
                            size={20}
                          />
                        </div>
                        <div className="callout-body">
                          <h4 className="callout-title">{sec.callout.title}</h4>
                          <p className="callout-text">{sec.callout.text}</p>
                        </div>
                      </div>
                    )}
                  </section>
                );
              })}
            </div>

            {/* Verification Checklist */}
            <section className="tutorial-checklist-card">
              <div className="checklist-header">
                <Icon name="verified" size={20} />
                <h3>Daftar Periksa Keberhasilan (Verification Checklist)</h3>
              </div>
              <ul className="checklist-items">
                {activeTutorial.verificationChecklist.map((item, i) => (
                  <li key={i}>
                    <input type="checkbox" id={`chk-${activeTutorial.id}-${i}`} defaultChecked />
                    <label htmlFor={`chk-${activeTutorial.id}-${i}`}>{item}</label>
                  </li>
                ))}
              </ul>
            </section>

            {/* Common Mistakes & Troubleshooting Table */}
            {activeTutorial.commonMistakes.length > 0 && (
              <section className="tutorial-troubleshooting-card">
                <div className="troubleshooting-header">
                  <Icon name="troubleshoot" size={20} />
                  <h3>Kesalahan Umum & Solusi Cepat</h3>
                </div>
                <div className="troubleshooting-grid">
                  {activeTutorial.commonMistakes.map((cm, i) => (
                    <div key={i} className="troubleshoot-item">
                      <div className="troubleshoot-issue">
                        <Icon name="error_outline" size={16} />
                        <strong>{cm.issue}</strong>
                      </div>
                      <p className="troubleshoot-cause">
                        <span className="label">Penyebab:</span> {cm.cause}
                      </p>
                      <p className="troubleshoot-solution">
                        <span className="label">Solusi:</span> {cm.solution}
                      </p>
                    </div>
                  ))}
                </div>
              </section>
            )}

            {/* Official References */}
            {activeTutorial.officialReferences.length > 0 && (
              <section className="tutorial-references-card">
                <div className="references-header">
                  <Icon name="link" size={18} />
                  <h4>Dokumentasi & Referensi Resmi</h4>
                </div>
                <ul className="references-links">
                  {activeTutorial.officialReferences.map((ref, i) => (
                    <li key={i}>
                      <a href={ref.url} target="_blank" rel="noopener noreferrer">
                        <span>{ref.title}</span>
                        <Icon name="open_in_new" size={14} />
                      </a>
                    </li>
                  ))}
                </ul>
              </section>
            )}

            {/* Next / Previous Pagination Footer */}
            <nav className="tutorial-pagination-nav" aria-label="Navigasi tutorial">
              {prevTutorial ? (
                <button
                  type="button"
                  className="button subtle pagination-prev"
                  onClick={() => selectTutorial(prevTutorial.id)}
                >
                  <Icon name="arrow_back" size={16} />
                  <div className="btn-text-col">
                    <span className="btn-sub">Tutorial Sebelumnya</span>
                    <span className="btn-main">{prevTutorial.number}. {prevTutorial.title}</span>
                  </div>
                </button>
              ) : (
                <div />
              )}

              {nextTutorial ? (
                <button
                  type="button"
                  className="button primary pagination-next"
                  onClick={() => selectTutorial(nextTutorial.id)}
                >
                  <div className="btn-text-col">
                    <span className="btn-sub">Tutorial Selanjutnya</span>
                    <span className="btn-main">{nextTutorial.number}. {nextTutorial.title}</span>
                  </div>
                  <Icon name="arrow_forward" size={16} />
                </button>
              ) : (
                <button
                  type="button"
                  className="button primary pagination-next finish-btn"
                  onClick={() => onNavigateLevel(1)}
                >
                  <div className="btn-text-col">
                    <span className="btn-sub">Setup Selesai!</span>
                    <span className="btn-main">Mulai Belajar: Level 1 (Foundations)</span>
                  </div>
                  <Icon name="rocket_launch" size={18} />
                </button>
              )}
            </nav>
          </article>
        </main>
      </div>
    </div>
  );
}
