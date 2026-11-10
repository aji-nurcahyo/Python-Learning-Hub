import { Icon } from '../ui/Icon';
import { getAssetUrl } from '../curriculum/resources';
import { CURRICULUM_DISCLAIMER } from '../curriculum';

interface AboutPageProps {
  onNavigateHome: () => void;
  onNavigateLevel: (levelId: number) => void;
}

export function AboutPage({ onNavigateHome, onNavigateLevel }: AboutPageProps) {
  return (
    <div className="hub-about-page">
      {/* Breadcrumb */}
      <div className="page-breadcrumb">
        <button type="button" className="breadcrumb-back-btn" onClick={onNavigateHome}>
          <Icon name="arrow_back" size={16} />
          <span>Kembali ke Beranda</span>
        </button>
        <span className="breadcrumb-separator">/</span>
        <span className="breadcrumb-current">Tentang Platform</span>
      </div>

      {/* Main Header */}
      <header className="about-header-banner">
        <div className="about-eyebrow">
          <Icon name="school" size={16} />
          <span>TENTANG PYTHON LEARNING HUB</span>
        </div>
        <h1 className="about-title">Python Learning Hub</h1>
        <p className="about-subtitle">Interactive Python Learning Modules</p>
        <p className="about-tagline">Learn Python, One Chapter at a Time</p>
      </header>

      {/* Content Section: About Platform */}
      <section className="about-section-card">
        <div className="about-card-header">
          <div className="about-icon-pill">
            <Icon name="terminal" size={24} />
          </div>
          <div>
            <h2>Tentang Platform</h2>
            <p className="about-card-desc">Sumber belajar pemrograman Python mandiri dan terbuka</p>
          </div>
        </div>
        <div className="about-card-body">
          <p>
            <strong>Python Learning Hub</strong> adalah platform edukasi mandiri dan terbuka yang dirancang
            untuk menyediakan materi pembelajaran pemrograman Python 3 yang terstruktur, mudah diakses,
            dan aplikatif. Platform ini memadukan sistem presentasi interaktif berbasis peramban, contoh kode
            program terverifikasi, latihan terarah, kuis penguatan konsep, dan proyek praktis.
          </p>
          <p>
            Seluruh kurikulum disusun secara modular dalam tiga jenjang kompetensi—mulai dari fondasi logika dasar
            hingga rekayasa sistem produksi tingkat lanjut—memungkinkan pembaca mengeksplorasi setiap konsep
            sesuai dengan ritme belajar masing-masing tanpa hambatan pendaftaran akun atau batasan jadwal.
          </p>
        </div>
      </section>

      {/* Content Section: Creator Identity */}
      <section className="about-section-card creator-card">
        <div className="about-card-header">
          <div className="about-icon-pill creator-icon">
            <Icon name="person" size={24} />
          </div>
          <div>
            <h2>Profil Pengembang & Inisiator</h2>
            <p className="about-card-desc">Creator and Developer</p>
          </div>
        </div>
        <div className="about-card-body">
          <div className="creator-profile-box">
            <div className="creator-avatar">
              <span>AP</span>
            </div>
            <div className="creator-details">
              <h3 className="creator-name">Aji Pamungkas Tri Nurcahyo</h3>
              <p className="creator-role">Creator & Developer · Python Learning Hub</p>
              <div className="creator-affiliation">
                <div className="affiliation-item">
                  <Icon name="account_balance" size={16} />
                  <span>Institut Teknologi Sumatera (ITERA)</span>
                </div>
              </div>
            </div>
          </div>
          <p className="creator-bio-text">
            Python Learning Hub dikembangkan sebagai wujud dedikasi untuk mendukung pembelajaran mandiri,
            pendidikan pemrograman yang mudah diakses, dan pengembangan keterampilan rekayasa komputasi
            terapan di bidang telekomunikasi serta rekayasa perangkat lunak modern.
          </p>
        </div>
      </section>

      {/* Content Section: Learning Philosophy */}
      <section className="about-section-card">
        <div className="about-card-header">
          <div className="about-icon-pill">
            <Icon name="psychology" size={24} />
          </div>
          <div>
            <h2>Filosofi Pembelajaran</h2>
            <p className="about-card-desc">Prinsip dasar perancangan modul edukasi</p>
          </div>
        </div>
        <div className="about-card-body">
          <div className="philosophy-grid">
            <div className="philosophy-item">
              <div className="philosophy-num">01</div>
              <h4>Pemahaman Konseptual</h4>
              <p>Menjelaskan logika di balik kode, prinsip kerja interpreter, dan alasan arsitektural suatu fungsi dirancang.</p>
            </div>
            <div className="philosophy-item">
              <div className="philosophy-num">02</div>
              <h4>Eksekusi Nyata &amp; Teruji</h4>
              <p>Seluruh keluaran program pada contoh kode divalidasi langsung menggunakan Python Interpreter (CPython 3).</p>
            </div>
            <div className="philosophy-item">
              <div className="philosophy-num">03</div>
              <h4>Eksplorasi Mandiri</h4>
              <p>Akses bebas ke 30 chapter dan 5 jalur spesialisasi tanpa kewajiban urutan belajar yang membatasi.</p>
            </div>
            <div className="philosophy-item">
              <div className="philosophy-num">04</div>
              <h4>Pemecahan Masalah Algoritmik</h4>
              <p>Latihan bertahap yang mengasah kemampuan berpikir komputasional dari kasus nyata.</p>
            </div>
            <div className="philosophy-item">
              <div className="philosophy-num">05</div>
              <h4>Keterampilan Teruji &amp; Reusable</h4>
              <p>Mengajarkan konvensi PEP 8, modularitas kode, Error Handling, Unit Testing, dan struktur data standar industri.</p>
            </div>
            <div className="philosophy-item">
              <div className="philosophy-num">06</div>
              <h4>Sumber Terbuka (OER)</h4>
              <p>Materi pembelajaran dapat diakses secara gratis dan terbuka untuk kemajuan pendidikan pemrograman.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Content Section: Quality & Academic Standards */}
      <section className="about-section-card" id="standards">
        <div className="about-card-header">
          <div className="about-icon-pill">
            <Icon name="verified" size={24} />
          </div>
          <div>
            <h2>Standar Kualitas, Pengujian &amp; Disclaimer Akademik</h2>
            <p className="about-card-desc">Quality Assurance Methodology &amp; Curriculum Alignment Disclaimer</p>
          </div>
        </div>
        <div className="about-card-body">
          <p>
            <strong>Metodologi Pengujian Konten &amp; Kode:</strong> Setiap pembaruan kurikulum divalidasi melalui
            rangkaian skrip pemeriksaan otomatis: verifikasi luaran 209 contoh kode Python terhadap runtime CPython 3
            (<code>check:outputs</code>), eksekusi 19 suite <em>Unit Testing</em> modular untuk modul Intermediate dan
            Professional, validasi konsistensi aset statis (<code>check:resources</code> &amp; <code>check:content</code>),
            serta pengecekan struktur slide presentasi.
          </p>
          <p>
            <strong>Pernyataan Standar Akademik &amp; Sertifikasi:</strong> {CURRICULUM_DISCLAIMER}
          </p>
        </div>
      </section>

      {/* Content Section: Open Source Acknowledgments */}
      <section className="about-section-card acknowledgments-card">
        <div className="about-card-header">
          <div className="about-icon-pill">
            <Icon name="handshake" size={24} />
          </div>
          <div>
            <h2>Pengakuan & Atribusi Sumber Terbuka</h2>
            <p className="about-card-desc">Open-source software foundation & license transparency</p>
          </div>
        </div>
        <div className="about-card-body">
          <p>
            Platform ini menghormati dan mematuhi etika ekosistem open-source dengan membedakan secara tegas
            antara identitas pengembang kurikulum Python Learning Hub dan pencipta perangkat lunak fondasi:
          </p>
          <ul className="ack-list">
            <li>
              <strong>Arsitektur Presentasi:</strong> Diadaptasi dari fondasi antarmuka peramban slide{' '}
              <a href="https://github.com/informatika-itera/pengkom" target="_blank" rel="noreferrer">
                Pengkom ITERA
              </a>{' '}
              yang berlisensi <a href={getAssetUrl('downloads/LICENSE.upstream')}>MIT License</a>.
            </li>
            <li>
              <strong>Library & Ekosistem:</strong> Dibangun dengan React 19, Reveal.js 6 (Hak Cipta Hakim El Hattab),
              Shiki syntax highlighter (Anthony Fu & Pine Wu), KaTeX typesetting math (Khan Academy),
              font Google Sans Flex & Code, serta Material Symbols Rounded.
            </li>
          </ul>
        </div>
      </section>

      {/* Navigation CTA */}
      <div className="about-cta-footer">
        <button type="button" className="button primary button-lg" onClick={() => onNavigateLevel(1)}>
          <span>Mulai Belajar di Level 1</span>
          <Icon name="arrow_forward" size={18} />
        </button>
        <button type="button" className="button subtle button-lg" onClick={onNavigateHome}>
          <Icon name="explore" size={18} />
          <span>Jelajahi 30 Chapter</span>
        </button>
      </div>
    </div>
  );
}

