import { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import type { SlideData } from './decks/registry';
import { ThemeSelect, usePreferences } from './deck-shell/preferences';
import { DeckShell } from './deck-shell/DeckShell';
import { SlideContent } from './layouts/SlideContent';
import { Icon } from './ui/Icon';
import p09 from './decks/pertemuan-09.json';
import p10 from './decks/pertemuan-10.json';
import task09 from './decks/tugas-09.md?raw';
import task10 from './decks/tugas-10.md?raw';

import { HomePage } from './pages/HomePage';
import { LevelPage } from './pages/LevelPage';
import { TrackPage } from './pages/TrackPage';
import { ChapterPage } from './pages/ChapterPage';
import { AboutPage } from './pages/AboutPage';

import '@fontsource-variable/google-sans-flex';
import '@fontsource-variable/google-sans-code';
import '@fontsource-variable/material-symbols-rounded';
import 'katex/dist/katex.min.css';
import './theme/styles.css';

const path = location.pathname;
const match = /\/pertemuan-(\d+)\/(?:index\.html|tugas\.html)?$/.exec(path);
const number = match ? Number(match[1]) : 0;
const base = match ? '../' : './';

// Common Hub Header
function Header({
  activeNav,
  onNavigateHome,
  onNavigateLevel,
  onNavigateAbout,
}: {
  activeNav?: string;
  onNavigateHome?: () => void;
  onNavigateLevel?: (id: number) => void;
  onNavigateAbout?: () => void;
}) {
  const { theme, setTheme } = usePreferences();

  const handleBrandClick = (e: React.MouseEvent) => {
    if (onNavigateHome) {
      e.preventDefault();
      onNavigateHome();
    }
  };

  return (
    <header className="site-header">
      <a className="brand-hub" href={`${base}index.html`} onClick={handleBrandClick} aria-label="Python Learning Hub Beranda">
        <span className="brand-hub-logo">py_</span>
        <div className="brand-hub-text">
          <span className="brand-hub-name">Python Learning Hub</span>
          <span className="brand-hub-tagline">Interactive Python Learning Modules</span>
        </div>
      </a>

      <nav className="hub-nav-links" aria-label="Navigasi kurikulum">
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'home' ? 'active' : ''}`}
          onClick={() => (onNavigateHome ? onNavigateHome() : (location.href = `${base}index.html`))}
        >
          Beranda
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'level-1' ? 'active' : ''}`}
          onClick={() => (onNavigateLevel ? onNavigateLevel(1) : (location.href = `${base}index.html#level/1`))}
        >
          Level 1
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'level-2' ? 'active' : ''}`}
          onClick={() => (onNavigateLevel ? onNavigateLevel(2) : (location.href = `${base}index.html#level/2`))}
        >
          Level 2
        </button>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'level-3' ? 'active' : ''}`}
          onClick={() => (onNavigateLevel ? onNavigateLevel(3) : (location.href = `${base}index.html#level/3`))}
        >
          Level 3
        </button>
        <a className="hub-nav-link" href={`${base}index.html#tracks`}>
          Spesialisasi
        </a>
        <a className="hub-nav-link" href={`${base}index.html#curriculum-browser`}>
          30 Chapter
        </a>
        <button
          type="button"
          className={`hub-nav-link ${activeNav === 'about' ? 'active' : ''}`}
          onClick={() => (onNavigateAbout ? onNavigateAbout() : (location.href = `${base}index.html#about`))}
        >
          Tentang
        </button>
      </nav>

      <div className="hub-header-actions">
        <ThemeSelect theme={theme} onChange={setTheme} />
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
        Dikembangkan oleh <strong>Aji Pamungkas Tri Nurcahyo</strong> · Teknik Telekomunikasi | Institut Teknologi Sumatera
      </div>
      <div>
        Fondasi:{' '}
        <a href="https://github.com/informatika-itera/pengkom" target="_blank" rel="noreferrer">
          Pengkom ITERA
        </a>{' '}
        · React 19 + Reveal.js 6 ·{' '}
        <a href={`${base}downloads/LICENSE.upstream`}>Lisensi MIT</a>
      </div>
    </footer>
  );
}

// Single-Page Application View Router
type HubRoute =
  | { type: 'home' }
  | { type: 'level'; id: number }
  | { type: 'track'; id: string }
  | { type: 'chapter'; id: number }
  | { type: 'about' };

function parseHashRoute(): HubRoute {
  const hash = location.hash.replace(/^#\/?/, '');
  const searchParams = new URLSearchParams(location.search);

  // Check search params first
  if (searchParams.get('page') === 'about' || hash === 'about' || hash.startsWith('about')) {
    return { type: 'about' };
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

  // Check hash routes
  const levelMatch = /^level\/(\d+)/.exec(hash);
  if (levelMatch) {
    const lId = Number(levelMatch[1]);
    if (lId >= 1 && lId <= 3) return { type: 'level', id: lId };
  }

  const trackMatch = /^track\/([a-z0-9-]+)/.exec(hash);
  if (trackMatch) {
    return { type: 'track', id: trackMatch[1] };
  }

  const chapterMatch = /^chapter\/(\d+)/.exec(hash);
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

  const activeNav =
    route.type === 'home'
      ? 'home'
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
        onNavigateLevel={navigateLevel}
        onNavigateAbout={navigateAbout}
      />
      <main id="main-content" className="hub-main-content">
        {route.type === 'home' && (
          <HomePage
            onNavigateLevel={navigateLevel}
            onNavigateTrack={navigateTrack}
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
          />
        )}
        {route.type === 'chapter' && (
          <ChapterPage
            chapterId={route.id}
            onNavigateHome={navigateHome}
            onNavigateLevel={navigateLevel}
            onNavigateChapter={navigateChapter}
          />
        )}
      </main>
      <Footer />
    </div>
  );
}

// Legacy Presentation & Task Views (Preserved for compatibility and slides access)
function Task({ meeting }: { meeting: number }) {
  const markdown = meeting === 9 ? task09 : task10;
  return (
    <>
      <Header />
      <main className="document">
        <a className="text-link" href="index.html">
          <Icon name="arrow_back" size={16} /> Kembali ke presentasi slide
        </a>
        <div className="eyebrow">PRAKTIK MANDIRI · CHAPTER {String(meeting).padStart(2, '0')}</div>
        {markdown.split('\n').map((line, i) =>
          line.startsWith('# ') ? (
            <h1 key={i}>{line.slice(2)}</h1>
          ) : line.startsWith('## ') ? (
            <h2 key={i}>{line.slice(3)}</h2>
          ) : line ? (
            <p className={/^\d|^-/.test(line) ? 'task-item' : ''} key={i}>
              {line.replace(/`|\*\*/g, '')}
            </p>
          ) : null,
        )}
        <div className="hero-actions">
          <a
            className="button primary"
            href={`../downloads/pertemuan-${String(meeting).padStart(2, '0')}/tugas.md`}
            download
          >
            <Icon name="download" size={16} /> <span>Unduh Panduan Tugas (.md)</span>
          </a>
          <a
            className="button subtle"
            href={`../downloads/pertemuan-${String(meeting).padStart(2, '0')}/contoh.py`}
            download
          >
            <Icon name="download" size={16} /> <span>Unduh Contoh Python (.py)</span>
          </a>
        </div>
      </main>
      <Footer />
    </>
  );
}

function Placeholder() {
  return (
    <>
      <Header />
      <main className="document placeholder">
        <div className="eyebrow">
          {number >= 1 && number <= 16 ? `CHAPTER ${String(number).padStart(2, '0')}` : 'HALAMAN TIDAK DITEMUKAN'}
        </div>
        <h1>{number >= 1 && number <= 16 ? 'Segera Hadir' : 'Halaman Tidak Tersedia'}</h1>
        <p>
          {number >= 1 && number <= 16
            ? 'Materi chapter ini sedang disiapkan. Silakan kembali ke Hub untuk mengakses silabus 30 Chapter yang telah tersedia.'
            : 'Alamat yang Anda buka tidak sesuai dengan daftar halaman kurikulum.'}
        </p>
        <a className="button primary" href={`${base}index.html`}>
          <Icon name="arrow_back" size={16} /> <span>Kembali ke Hub Utama</span>
        </a>
      </main>
      <Footer />
    </>
  );
}

function Reading({ meeting, slides }: { meeting: number; slides: SlideData[] }) {
  return (
    <>
      <Header />
      <main className="reading">
        <div className="reading-heading">
          <div>
            <div className="eyebrow">MODE BACA DOKUMEN · CHAPTER {String(meeting).padStart(2, '0')}</div>
            <h1>Pelajari dengan ritme mandiri.</h1>
            <p>
              Tampilan linear yang responsif untuk membaca seluruh materi secara berurutan di layar desktop maupun perangkat seluler.
            </p>
          </div>
          <div className="hero-actions">
            <a className="button primary" href="index.html">
              <Icon name="slideshow" size={16} /> <span>Buka Mode Presentasi</span>
            </a>
            <a className="button subtle" href="tugas.html">
              <Icon name="assignment" size={16} /> <span>Lihat Tugas Mandiri</span>
            </a>
          </div>
        </div>
        {slides.map((slide, i) => (
          <article className={`reading-slide ${slide.kind}`} key={i}>
            <SlideContent slide={slide} meeting={meeting} base="../" />
          </article>
        ))}
      </main>
      <Footer />
    </>
  );
}

const isDashboard = !match && !path.endsWith('/404.html') && !path.endsWith('/404');

createRoot(document.getElementById('root')!).render(
  number === 9 || number === 10 ? (
    path.endsWith('tugas.html') ? (
      <Task meeting={number} />
    ) : new URLSearchParams(location.search).get('view') === 'read' ? (
      <Reading meeting={number} slides={(number === 9 ? p09 : p10) as SlideData[]} />
    ) : (
      <DeckShell slides={(number === 9 ? p09 : p10) as SlideData[]} meeting={number} base={base} />
    )
  ) : isDashboard ? (
    <HubApp />
  ) : (
    <Placeholder />
  ),
);
