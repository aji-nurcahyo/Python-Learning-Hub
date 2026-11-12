import { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import type { SlideData } from './decks/registry';
import { getSlideDeckForChapter } from './decks/registry';
import { ThemeSelect, usePreferences } from './deck-shell/preferences';
import { DeckShell } from './deck-shell/DeckShell';
import { SlideContent } from './layouts/SlideContent';
import { Icon } from './ui/Icon';

const taskGuides = import.meta.glob('../content/**/assignments/tugas.md', {
  query: '?raw',
  import: 'default',
  eager: true,
}) as Record<string, string>;

import { HomePage } from './pages/HomePage';
import { LevelPage } from './pages/LevelPage';
import { TrackPage } from './pages/TrackPage';
import { ChapterPage } from './pages/ChapterPage';
import { AboutPage } from './pages/AboutPage';
import { GettingStartedPage } from './pages/GettingStartedPage';
import { SpecializationModulePage } from './pages/SpecializationModulePage';
import {
  getSpecializationModuleById,
  getSlideDeckForSpecialization,
} from './curriculum/specializations';

import '@fontsource-variable/google-sans-flex';
import '@fontsource-variable/google-sans-code';
import '@fontsource-variable/material-symbols-rounded';
import 'katex/dist/katex.min.css';
import './theme/styles.css';

const path = location.pathname;
const rawBase = import.meta.env.BASE_URL || './';
const base = rawBase.endsWith('/') ? rawBase : `${rawBase}/`;

// Common Hub Header
function Header({
  activeNav,
  onNavigateHome,
  onNavigateGettingStarted,
  onNavigateLevel,
  onNavigateAbout,
}: {
  activeNav?: string;
  onNavigateHome?: () => void;
  onNavigateGettingStarted?: (tutorialId?: string) => void;
  onNavigateLevel?: (id: number) => void;
  onNavigateAbout?: () => void;
}) {
  const { theme, setTheme } = usePreferences();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleBrandClick = (e: React.MouseEvent) => {
    setMobileMenuOpen(false);
    if (onNavigateHome) {
      e.preventDefault();
      onNavigateHome();
    }
  };

  const closeMenuAnd = (fn?: () => void, fallbackUrl?: string) => {
    setMobileMenuOpen(false);
    if (fn) {
      fn();
    } else if (fallbackUrl) {
      location.href = fallbackUrl;
    }
  };

  return (
    <header className="site-header">
      <a className="skip-link" href="#main-content">
        Langsung ke konten utama
      </a>
      <a className="brand-hub" href={`${base}index.html`} onClick={handleBrandClick} aria-label="Python Learning Hub Beranda">
        <span className="brand-hub-logo" aria-hidden="true">py_</span>
        <div className="brand-hub-text">
          <span className="brand-hub-name">Python Learning Hub</span>
          <span className="brand-hub-tagline">Interactive Python Learning Modules</span>
        </div>
      </a>

      <nav
        id="hub-primary-nav"
        className={`hub-nav-links ${mobileMenuOpen ? 'is-open' : ''}`}
        aria-label="Navigasi kurikulum"
      >
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'home' ? 'active' : ''}`}
          aria-current={activeNav === 'home' ? 'page' : undefined}
          onClick={() => closeMenuAnd(onNavigateHome, `${base}index.html`)}
        >
          Beranda
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'getting-started' ? 'active' : ''}`}
          aria-current={activeNav === 'getting-started' ? 'page' : undefined}
          onClick={() =>
            closeMenuAnd(
              onNavigateGettingStarted ? () => onNavigateGettingStarted() : undefined,
              `${base}index.html#getting-started`
            )
          }
        >
          Getting Started
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'level-1' ? 'active' : ''}`}
          aria-current={activeNav === 'level-1' ? 'page' : undefined}
          onClick={() => closeMenuAnd(onNavigateLevel ? () => onNavigateLevel(1) : undefined, `${base}index.html#level/1`)}
        >
          Level 1
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'level-2' ? 'active' : ''}`}
          aria-current={activeNav === 'level-2' ? 'page' : undefined}
          onClick={() => closeMenuAnd(onNavigateLevel ? () => onNavigateLevel(2) : undefined, `${base}index.html#level/2`)}
        >
          Level 2
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'level-3' ? 'active' : ''}`}
          aria-current={activeNav === 'level-3' ? 'page' : undefined}
          onClick={() => closeMenuAnd(onNavigateLevel ? () => onNavigateLevel(3) : undefined, `${base}index.html#level/3`)}
        >
          Level 3
        </button>
        <a
          className="hub-nav-link"
          href={`${base}index.html#tracks`}
          onClick={() => setMobileMenuOpen(false)}
        >
          Spesialisasi
        </a>
        <a
          className="hub-nav-link"
          href={`${base}index.html#curriculum-browser`}
          onClick={() => setMobileMenuOpen(false)}
        >
          30 Chapter
        </a>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'about' ? 'active' : ''}`}
          aria-current={activeNav === 'about' ? 'page' : undefined}
          onClick={() => closeMenuAnd(onNavigateAbout, `${base}index.html#about`)}
        >
          Tentang
        </button>
      </nav>

      <div className="hub-header-actions">
        <ThemeSelect theme={theme} onChange={setTheme} />
        <button
          type="button"
          className="hub-mobile-menu-btn"
          aria-expanded={mobileMenuOpen}
          aria-controls="hub-primary-nav"
          aria-label={mobileMenuOpen ? 'Tutup menu navigasi' : 'Buka menu navigasi'}
          onClick={() => setMobileMenuOpen((prev) => !prev)}
        >
          <Icon name={mobileMenuOpen ? 'close' : 'menu'} size={22} />
        </button>
      </div>
    </header>
  );
}

// Common Hub Footer
function Footer() {
  return (
    <footer className="site-footer">
      <div>
        <strong>Python Learning Hub</strong> · Interactive Python Learning Modules · <em>Learn Python, One Chapter at a Time</em>
      </div>
      <div>
        Dikembangkan oleh <strong>Aji Pamungkas Tri Nurcahyo</strong> · Institut Teknologi Sumatera
      </div>
      <div>
        <a
          href={`${base}index.html#about/licenses`}
          onClick={(e) => {
            if (!isDirect404) {
              e.preventDefault();
              location.hash = 'about/licenses';
            }
          }}
        >
          Lisensi &amp; Atribusi
        </a>
      </div>
    </footer>
  );
}

// Single-Page Application View Router
type HubRoute =
  | { type: 'home' }
  | { type: 'getting-started'; tutorialId?: string }
  | { type: 'level'; id: number }
  | { type: 'track'; id: string }
  | { type: 'spec-module'; moduleId: string }
  | { type: 'spec-slides'; moduleId: string }
  | { type: 'spec-reading'; moduleId: string }
  | { type: 'spec-task'; moduleId: string }
  | { type: 'chapter'; id: number }
  | { type: 'slides'; chapterId: number }
  | { type: 'reading'; chapterId: number }
  | { type: 'task'; chapterId: number }
  | { type: 'about' };

function extractRouteFromPathname(pathname: string): string {
  const cleaned = pathname.replace(/\/index\.html$/, '').replace(/^\/+/, '');
  const lower = cleaned.toLowerCase();
  if (lower === 'python-learning-hub') return '';
  if (lower.startsWith('python-learning-hub/')) {
    return cleaned.slice('python-learning-hub/'.length);
  }
  return cleaned;
}

function parseHashRoute(): HubRoute {
  const hash = location.hash.replace(/^#\/?/, '');
  const pathRoute = extractRouteFromPathname(location.pathname);
  const routePath = hash || pathRoute;
  const searchParams = new URLSearchParams(location.search);

  // Check search params first
  if (searchParams.get('page') === 'about' || routePath === 'about' || routePath.startsWith('about/')) {
    return { type: 'about' };
  }

  // Check Getting Started route
  const gettingStartedMatch = /^getting-started(?:\/([a-z0-9-]+))?/.exec(routePath);
  if (gettingStartedMatch || searchParams.get('page') === 'getting-started') {
    const tutId = gettingStartedMatch ? gettingStartedMatch[1] : searchParams.get('tutorial') || undefined;
    return { type: 'getting-started', tutorialId: tutId };
  }

  // Specialization sub-routes (#spec/A01, #spec/A01/slides, #spec/A01/read, #spec/A01/task, #track/<id>/A01)
  const specSlidesMatch = /^(?:spec|track\/[a-z0-9-]+)\/([a-eA-E]\d{2})\/slides/.exec(routePath);
  if (specSlidesMatch || (searchParams.get('spec') && searchParams.get('view') === 'slides')) {
    const mId = (specSlidesMatch ? specSlidesMatch[1] : searchParams.get('spec')!).toUpperCase();
    return { type: 'spec-slides', moduleId: mId };
  }

  const specReadMatch = /^(?:spec|track\/[a-z0-9-]+)\/([a-eA-E]\d{2})\/read/.exec(routePath);
  if (specReadMatch || (searchParams.get('spec') && searchParams.get('view') === 'read')) {
    const mId = (specReadMatch ? specReadMatch[1] : searchParams.get('spec')!).toUpperCase();
    return { type: 'spec-reading', moduleId: mId };
  }

  const specTaskMatch = /^(?:spec|track\/[a-z0-9-]+)\/([a-eA-E]\d{2})\/task/.exec(routePath);
  if (specTaskMatch || (searchParams.get('spec') && searchParams.get('view') === 'task')) {
    const mId = (specTaskMatch ? specTaskMatch[1] : searchParams.get('spec')!).toUpperCase();
    return { type: 'spec-task', moduleId: mId };
  }

  const specModuleMatch = /^(?:spec|track\/[a-z0-9-]+)\/([a-eA-E]\d{2})(?:\/|$)/.exec(routePath);
  if (specModuleMatch || searchParams.get('spec')) {
    const mId = (specModuleMatch ? specModuleMatch[1] : searchParams.get('spec')!).toUpperCase();
    return { type: 'spec-module', moduleId: mId };
  }

  // Chapter sub-routes (slides, read, task)
  const slidesMatch = /^chapter\/(\d+)\/slides/.exec(routePath) || /^slides\/(\d+)/.exec(routePath);
  if (slidesMatch || (searchParams.get('chapter') && searchParams.get('view') === 'slides')) {
    const cId = Number(slidesMatch ? slidesMatch[1] : searchParams.get('chapter'));
    if (cId >= 1 && cId <= 30) return { type: 'slides', chapterId: cId };
  }

  const readMatch = /^chapter\/(\d+)\/read/.exec(routePath) || /^read\/(\d+)/.exec(routePath);
  if (readMatch || (searchParams.get('chapter') && searchParams.get('view') === 'read')) {
    const cId = Number(readMatch ? readMatch[1] : searchParams.get('chapter'));
    if (cId >= 1 && cId <= 30) return { type: 'reading', chapterId: cId };
  }

  const taskMatch = /^chapter\/(\d+)\/task/.exec(routePath) || /^task\/(\d+)/.exec(routePath);
  if (taskMatch || (searchParams.get('chapter') && searchParams.get('view') === 'task')) {
    const cId = Number(taskMatch ? taskMatch[1] : searchParams.get('chapter'));
    if (cId >= 1 && cId <= 30) return { type: 'task', chapterId: cId };
  }

  if (searchParams.get('level')) {
    const lId = Number(searchParams.get('level'));
    if (lId >= 1 && lId <= 3) return { type: 'level', id: lId };
  }
  if (searchParams.get('track')) {
    return { type: 'track', id: searchParams.get('track')! };
  }
  if (searchParams.get('chapter')) {
    const cId = Number(searchParams.get('chapter'));
    if (cId >= 1 && cId <= 30) return { type: 'chapter', id: cId };
  }

  // Check route paths
  const levelMatch = /^level\/(\d+)/.exec(routePath);
  if (levelMatch) {
    const lId = Number(levelMatch[1]);
    if (lId >= 1 && lId <= 3) return { type: 'level', id: lId };
  }

  const trackMatch = /^track\/([a-z0-9-]+)/.exec(routePath);
  if (trackMatch) {
    return { type: 'track', id: trackMatch[1] };
  }

  const chapterMatch = /^chapter\/(\d+)/.exec(routePath);
  if (chapterMatch) {
    const cId = Number(chapterMatch[1]);
    if (cId >= 1 && cId <= 30) return { type: 'chapter', id: cId };
  }

  return { type: 'home' };
}

function HubApp() {
  const [route, setRoute] = useState<HubRoute>(parseHashRoute);

  useEffect(() => {
    const handleHashChange = () => {
      setRoute(parseHashRoute());
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    window.addEventListener('hashchange', handleHashChange);
    window.addEventListener('popstate', handleHashChange);
    return () => {
      window.removeEventListener('hashchange', handleHashChange);
      window.removeEventListener('popstate', handleHashChange);
    };
  }, []);

  const navigateHome = () => {
    location.hash = '';
    setRoute({ type: 'home' });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateAbout = () => {
    location.hash = 'about';
    setRoute({ type: 'about' });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateGettingStarted = (tutorialId?: string) => {
    location.hash = tutorialId ? `getting-started/${tutorialId}` : 'getting-started';
    setRoute({ type: 'getting-started', tutorialId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateLevel = (levelId: number) => {
    location.hash = `level/${levelId}`;
    setRoute({ type: 'level', id: levelId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateTrack = (trackId: string) => {
    location.hash = `track/${trackId}`;
    setRoute({ type: 'track', id: trackId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateChapter = (chapterId: number) => {
    location.hash = `chapter/${chapterId}`;
    setRoute({ type: 'chapter', id: chapterId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateSlides = (chapterId: number) => {
    location.hash = `chapter/${chapterId}/slides`;
    setRoute({ type: 'slides', chapterId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateReading = (chapterId: number) => {
    location.hash = `chapter/${chapterId}/read`;
    setRoute({ type: 'reading', chapterId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateTask = (chapterId: number) => {
    location.hash = `chapter/${chapterId}/task`;
    setRoute({ type: 'task', chapterId });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateSpecModule = (moduleId: string) => {
    location.hash = `spec/${moduleId.toUpperCase()}`;
    setRoute({ type: 'spec-module', moduleId: moduleId.toUpperCase() });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateSpecSlides = (moduleId: string) => {
    location.hash = `spec/${moduleId.toUpperCase()}/slides`;
    setRoute({ type: 'spec-slides', moduleId: moduleId.toUpperCase() });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateSpecReading = (moduleId: string) => {
    location.hash = `spec/${moduleId.toUpperCase()}/read`;
    setRoute({ type: 'spec-reading', moduleId: moduleId.toUpperCase() });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navigateSpecTask = (moduleId: string) => {
    location.hash = `spec/${moduleId.toUpperCase()}/task`;
    setRoute({ type: 'spec-task', moduleId: moduleId.toUpperCase() });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Specialization slide deck view
  if (route.type === 'spec-slides') {
    const slides = getSlideDeckForSpecialization(route.moduleId);
    if (!slides) {
      return (
        <div className="hub-page-wrapper">
          <Header activeNav={undefined} onNavigateHome={navigateHome} onNavigateGettingStarted={navigateGettingStarted} onNavigateLevel={navigateLevel} onNavigateAbout={navigateAbout} />
          <main className="document placeholder">
            <div className="eyebrow">SPECIALIZATION · {route.moduleId}</div>
            <h1>Slide Belum Tersedia</h1>
            <p>Slide untuk modul spesialisasi ini sedang disiapkan.</p>
            <button type="button" className="button primary" onClick={() => navigateSpecModule(route.moduleId)}>
              <Icon name="arrow_back" size={16} /> <span>Kembali ke Modul {route.moduleId}</span>
            </button>
          </main>
          <Footer />
        </div>
      );
    }
    return (
      <DeckShell
        slides={slides}
        meeting={Number(route.moduleId.slice(1))}
        specId={route.moduleId}
        base={base}
        onNavigateChapter={() => navigateSpecModule(route.moduleId)}
        onNavigateReading={() => navigateSpecReading(route.moduleId)}
        onNavigateTask={() => navigateSpecTask(route.moduleId)}
      />
    );
  }

  // Specialization linear reading document view
  if (route.type === 'spec-reading') {
    const mod = getSpecializationModuleById(route.moduleId);
    const slides = mod?.slides || [];
    return (
      <div className="hub-page-wrapper">
        <Header activeNav={undefined} onNavigateHome={navigateHome} onNavigateGettingStarted={navigateGettingStarted} onNavigateLevel={navigateLevel} onNavigateAbout={navigateAbout} />
        <Reading
          meeting={Number(route.moduleId.slice(1))}
          specId={route.moduleId}
          markdownGuide={mod?.readingMarkdown}
          slides={slides}
          onNavigateChapter={() => navigateSpecModule(route.moduleId)}
          onNavigateSlides={() => navigateSpecSlides(route.moduleId)}
          onNavigateTask={() => navigateSpecTask(route.moduleId)}
        />
        <Footer />
      </div>
    );
  }

  // Specialization dedicated task view
  if (route.type === 'spec-task') {
    const mod = getSpecializationModuleById(route.moduleId);
    return (
      <div className="hub-page-wrapper">
        <Header activeNav={undefined} onNavigateHome={navigateHome} onNavigateGettingStarted={navigateGettingStarted} onNavigateLevel={navigateLevel} onNavigateAbout={navigateAbout} />
        <Task
          meeting={Number(route.moduleId.slice(1))}
          specId={route.moduleId}
          customMarkdown={mod?.assignmentMarkdown}
          customDownloadUrl={mod?.resources.codeDownload || undefined}
          onNavigateChapter={() => navigateSpecModule(route.moduleId)}
          onNavigateSlides={() => navigateSpecSlides(route.moduleId)}
        />
        <Footer />
      </div>
    );
  }

  // If in interactive slide presentation mode, render DeckShell directly
  if (route.type === 'slides') {
    const slides = getSlideDeckForChapter(route.chapterId);
    if (!slides) {
      return (
        <div className="hub-page-wrapper">
          <Header activeNav={undefined} onNavigateHome={navigateHome} onNavigateGettingStarted={navigateGettingStarted} onNavigateLevel={navigateLevel} onNavigateAbout={navigateAbout} />
          <main className="document placeholder">
            <div className="eyebrow">CHAPTER {String(route.chapterId).padStart(2, '0')}</div>
            <h1>Slide Belum Tersedia</h1>
            <p>Slide presentasi interaktif untuk chapter ini sedang disiapkan.</p>
            <button type="button" className="button primary" onClick={() => navigateChapter(route.chapterId)}>
              <Icon name="arrow_back" size={16} /> <span>Kembali ke Chapter {route.chapterId}</span>
            </button>
          </main>
          <Footer />
        </div>
      );
    }
    return (
      <DeckShell
        slides={slides}
        meeting={route.chapterId}
        base={base}
        onNavigateChapter={() => navigateChapter(route.chapterId)}
        onNavigateReading={() => navigateReading(route.chapterId)}
        onNavigateTask={() => navigateTask(route.chapterId)}
      />
    );
  }

  // If in linear reading document view
  if (route.type === 'reading') {
    const slides = getSlideDeckForChapter(route.chapterId) || [];
    return (
      <div className="hub-page-wrapper">
        <Header activeNav={undefined} onNavigateHome={navigateHome} onNavigateGettingStarted={navigateGettingStarted} onNavigateLevel={navigateLevel} onNavigateAbout={navigateAbout} />
        <Reading
          meeting={route.chapterId}
          slides={slides}
          onNavigateChapter={() => navigateChapter(route.chapterId)}
          onNavigateSlides={() => navigateSlides(route.chapterId)}
          onNavigateTask={() => navigateTask(route.chapterId)}
        />
        <Footer />
      </div>
    );
  }

  // If in dedicated task view
  if (route.type === 'task') {
    return (
      <div className="hub-page-wrapper">
        <Header activeNav={undefined} onNavigateHome={navigateHome} onNavigateGettingStarted={navigateGettingStarted} onNavigateLevel={navigateLevel} onNavigateAbout={navigateAbout} />
        <Task
          meeting={route.chapterId}
          onNavigateChapter={() => navigateChapter(route.chapterId)}
          onNavigateSlides={() => navigateSlides(route.chapterId)}
        />
        <Footer />
      </div>
    );
  }

  const activeNav =
    route.type === 'home'
      ? 'home'
      : route.type === 'getting-started'
      ? 'getting-started'
      : route.type === 'level'
      ? `level-${route.id}`
      : route.type === 'about'
      ? 'about'
      : undefined;

  return (
    <div className="hub-page-wrapper">
      <a className="skip-link" href="#main-content">
        Lewati ke konten utama
      </a>
      <Header
        activeNav={activeNav}
        onNavigateHome={navigateHome}
        onNavigateGettingStarted={navigateGettingStarted}
        onNavigateLevel={navigateLevel}
        onNavigateAbout={navigateAbout}
      />
      <main id="main-content" className="hub-main-content">
        {route.type === 'home' && (
          <HomePage
            onNavigateLevel={navigateLevel}
            onNavigateTrack={navigateTrack}
            onNavigateChapter={navigateChapter}
            onNavigateGettingStarted={navigateGettingStarted}
          />
        )}
        {route.type === 'getting-started' && (
          <GettingStartedPage
            initialTutorialId={route.tutorialId}
            onNavigateHome={navigateHome}
            onNavigateLevel={navigateLevel}
            onNavigateChapter={navigateChapter}
          />
        )}
        {route.type === 'about' && (
          <AboutPage
            onNavigateHome={navigateHome}
            onNavigateLevel={navigateLevel}
          />
        )}
        {route.type === 'level' && (
          <LevelPage
            levelId={route.id}
            onNavigateHome={navigateHome}
            onNavigateChapter={navigateChapter}
            onNavigateLevel={navigateLevel}
          />
        )}
        {route.type === 'track' && (
          <TrackPage
            trackId={route.id}
            onNavigateHome={navigateHome}
            onNavigateChapter={navigateChapter}
            onNavigateTrack={navigateTrack}
            onNavigateSpecModule={navigateSpecModule}
          />
        )}
        {route.type === 'spec-module' && (
          <SpecializationModulePage
            moduleId={route.moduleId}
            onNavigateHome={navigateHome}
            onNavigateTrack={navigateTrack}
            onNavigateSpecModule={navigateSpecModule}
            onNavigateSpecSlides={navigateSpecSlides}
            onNavigateSpecReading={navigateSpecReading}
            onNavigateSpecTask={navigateSpecTask}
          />
        )}
        {route.type === 'chapter' && (
          <ChapterPage
            chapterId={route.id}
            onNavigateHome={navigateHome}
            onNavigateLevel={navigateLevel}
            onNavigateChapter={navigateChapter}
            onNavigateSlides={navigateSlides}
            onNavigateReading={navigateReading}
            onNavigateTask={navigateTask}
          />
        )}
      </main>
      <Footer />
    </div>
  );
}

// Helper to render structured textbook markdown into semantic React elements
function renderMarkdownDocument(markdown: string) {
  const lines = markdown.replace(/\r\n/g, '\n').split('\n');
  const elements: React.ReactNode[] = [];
  let inCode = false;
  let codeLines: string[] = [];
  let listItems: string[] = [];

  const flushList = (keyPrefix: number) => {
    if (listItems.length > 0) {
      elements.push(
        <ul key={`ul-${keyPrefix}`} className="reading-md-list">
          {listItems.map((item, idx) => (
            <li key={idx}>{item.replace(/\*\*/g, '')}</li>
          ))}
        </ul>,
      );
      listItems = [];
    }
  };

  lines.forEach((line, i) => {
    if (line.trim().startsWith('```')) {
      flushList(i);
      if (!inCode) {
        inCode = true;
        codeLines = [];
      } else {
        elements.push(
          <pre key={`code-${i}`} className="reading-md-code">
            <code>{codeLines.join('\n')}</code>
          </pre>,
        );
        inCode = false;
        codeLines = [];
      }
      return;
    }

    if (inCode) {
      codeLines.push(line);
      return;
    }

    if (line.startsWith('# ')) {
      flushList(i);
      elements.push(<h1 key={`h1-${i}`}>{line.slice(2)}</h1>);
    } else if (line.startsWith('## ')) {
      flushList(i);
      elements.push(<h2 key={`h2-${i}`}>{line.slice(3)}</h2>);
    } else if (line.startsWith('### ')) {
      flushList(i);
      elements.push(<h3 key={`h3-${i}`}>{line.slice(4)}</h3>);
    } else if (/^(\*|-|\d+\.)\s+/.test(line.trim())) {
      listItems.push(line.trim().replace(/^(\*|-|\d+\.)\s+/, ''));
    } else if (line.trim() === '') {
      flushList(i);
    } else {
      flushList(i);
      elements.push(
        <p key={`p-${i}`}>{line.replace(/\*\*/g, '')}</p>,
      );
    }
  });

  flushList(lines.length);
  return elements;
}

// Modular Document Reading View
function Reading({
  meeting,
  specId,
  markdownGuide,
  slides,
  onNavigateChapter,
  onNavigateSlides,
  onNavigateTask,
}: {
  meeting: number;
  specId?: string;
  markdownGuide?: string;
  slides: SlideData[];
  onNavigateChapter?: () => void;
  onNavigateSlides?: () => void;
  onNavigateTask?: () => void;
}) {
  const unitLabel = specId ? `Module ${specId}` : `Chapter ${meeting}`;
  const eyebrowLabel = specId
    ? `MODE BACA DOKUMEN · SPECIALIZATION MODULE ${specId}`
    : `MODE BACA DOKUMEN · CHAPTER ${String(meeting).padStart(2, '0')}`;
  const defaultBackHash = specId ? `spec/${specId}` : `chapter/${meeting}`;
  const defaultSlidesHash = specId ? `spec/${specId}/slides` : `chapter/${meeting}/slides`;
  const defaultTaskHash = specId ? `spec/${specId}/task` : `chapter/${meeting}/task`;

  return (
    <main className="reading">
      <div className="reading-heading">
        <div>
          <button
            type="button"
            className="breadcrumb-back-btn"
            style={{ marginBottom: '12px' }}
            onClick={() => (onNavigateChapter ? onNavigateChapter() : (location.hash = defaultBackHash))}
          >
            <Icon name="arrow_back" size={16} /> <span>Kembali ke {unitLabel}</span>
          </button>
          <div className="eyebrow">{eyebrowLabel}</div>
          <h1>Pelajari dengan ritme mandiri.</h1>
          <p>
            Tampilan linear yang responsif untuk membaca seluruh materi secara berurutan di layar desktop maupun perangkat seluler.
          </p>
        </div>
        <div className="hero-actions">
          <button
            type="button"
            className="button primary"
            onClick={() => (onNavigateSlides ? onNavigateSlides() : (location.hash = defaultSlidesHash))}
          >
            <Icon name="slideshow" size={16} /> <span>Buka Slide</span>
          </button>
          <button
            type="button"
            className="button subtle"
            onClick={() => (onNavigateTask ? onNavigateTask() : (location.hash = defaultTaskHash))}
          >
            <Icon name="assignment" size={16} /> <span>Lihat Tugas</span>
          </button>
        </div>
      </div>
      {markdownGuide && (
        <section className="reading-markdown-guide">
          {renderMarkdownDocument(markdownGuide)}
        </section>
      )}
      {slides.map((slide, i) => (
        <article className={`reading-slide ${slide.kind}`} key={i}>
          <SlideContent slide={slide} meeting={meeting} specId={specId} base={base} />
        </article>
      ))}
    </main>
  );
}

// Modular Task View
function Task({
  meeting,
  specId,
  customMarkdown,
  customDownloadUrl,
  onNavigateChapter,
  onNavigateSlides,
}: {
  meeting: number;
  specId?: string;
  customMarkdown?: string;
  customDownloadUrl?: string;
  onNavigateChapter?: () => void;
  onNavigateSlides?: () => void;
}) {
  const pad = String(meeting).padStart(2, '0');
  const taskEntry = Object.entries(taskGuides).find(([k]) =>
    k.endsWith(`/chapter-${pad}/assignments/tugas.md`),
  );
  const markdown = customMarkdown
    ? customMarkdown
    : taskEntry
      ? taskEntry[1]
      : '# Petunjuk Tugas\n\nPanduan tugas untuk modul ini sedang disiapkan.';
  const unitLabel = specId ? `Module ${specId}` : `Chapter ${meeting}`;
  const eyebrowLabel = specId
    ? `PRAKTIK MANDIRI · MODULE ${specId}`
    : `PRAKTIK MANDIRI · CHAPTER ${String(meeting).padStart(2, '0')}`;
  const defaultBackHash = specId ? `spec/${specId}` : `chapter/${meeting}`;
  const defaultSlidesHash = specId ? `spec/${specId}/slides` : `chapter/${meeting}/slides`;
  const downloadHref = customDownloadUrl
    ? customDownloadUrl.startsWith('/')
      ? `${base}${customDownloadUrl.slice(1)}`
      : `${base}${customDownloadUrl}`
    : `${base}downloads/chapter-${String(meeting).padStart(2, '0')}/contoh.py`;

  return (
    <main className="document">
      <button
        type="button"
        className="breadcrumb-back-btn"
        style={{ marginBottom: '16px' }}
        onClick={() => (onNavigateChapter ? onNavigateChapter() : (location.hash = defaultBackHash))}
      >
        <Icon name="arrow_back" size={16} /> <span>Kembali ke {unitLabel}</span>
      </button>
      <div className="eyebrow">{eyebrowLabel}</div>
      {renderMarkdownDocument(markdown)}
      <div className="hero-actions">
        <button
          type="button"
          className="button primary"
          onClick={() => (onNavigateSlides ? onNavigateSlides() : (location.hash = defaultSlidesHash))}
        >
          <Icon name="slideshow" size={16} /> <span>Buka Slide</span>
        </button>
        <a
          className="button subtle"
          href={downloadHref}
          download
        >
          <Icon name="download" size={16} /> <span>Download Python Code</span>
        </a>
      </div>
    </main>
  );
}

function FallbackNotFound() {
  return (
    <div className="hub-page-wrapper">
      <Header />
      <main className="document placeholder">
        <div className="eyebrow">HALAMAN TIDAK DITEMUKAN</div>
        <h1>Halaman Tidak Tersedia</h1>
        <p>Alamat yang Anda buka tidak sesuai dengan daftar halaman kurikulum.</p>
        <a className="button primary" href={`${base}index.html`}>
          <Icon name="arrow_back" size={16} /> <span>Kembali ke Hub Utama</span>
        </a>
      </main>
      <Footer />
    </div>
  );
}

const isDirect404 = path.endsWith('/404.html') || path.endsWith('/404');

createRoot(document.getElementById('root')!).render(
  isDirect404 ? <FallbackNotFound /> : <HubApp />
);
