# Python Learning Hub

> **Tagline:** Learn Python, One Chapter at a Time  
> **Subtitle:** Interactive Python Learning Modules  
> **Status:** Open Access Educational Resource (OER)  
> **Live Site URL (GitHub Pages):** `https://USERNAME.github.io/python-learning-hub/`

Python Learning Hub is a free, open-access collection of structured Python learning modules, interactive browser presentations, verified programming examples, guided exercises, conceptual quizzes, and practical projects.

Developed and maintained by **Aji Pamungkas Tri Nurcahyo** from **Program Studi Teknik Telekomunikasi, Fakultas Teknologi Industri, Institut Teknologi Sumatera (ITERA)**.

---

## 1. Identitas & Pengembang Platform

- **Nama Proyek:** Python Learning Hub
- **Tagline:** *Learn Python, One Chapter at a Time*
- **Subjudul:** *Interactive Python Learning Modules*
- **Inisiator & Pengembang:** **Aji Pamungkas Tri Nurcahyo**
- **Afiliasi Akademik:**
  - Program Studi Teknik Telekomunikasi
  - Fakultas Teknologi Industri
  - Institut Teknologi Sumatera (ITERA)
- **Tujuan Platform:** Menyediakan materi edukasi pemrograman Python 3 yang independen, gratis, terstruktur secara bertahap, dan dapat diakses siapa pun tanpa batasan registrasi maupun sekat jadwal perkuliahan.

---

## 2. Filosofi Pembelajaran

Platform ini dibangun berlandaskan 6 pilar edukasi komputasi modern:

1. **Pemahaman Konseptual Mendalam:** Menjelaskan logika di balik sintaks, alokasi memori, prinsip interpreter CPython, dan alasan teknis di balik rancangan suatu struktur data atau fungsi.
2. **Eksekusi Nyata & Terverifikasi:** Seluruh 24 contoh program dieksekusi secara nyata oleh interpreter CPython 3. Keluaran terminal yang ditampilkan di antarmuka web adalah hasil aktual sistem tanpa manipulasi simulasi.
3. **Eksplorasi Mandiri Tanpa Sekat:** Pengguna memiliki kebebasan penuh memilih chapter mana pun di antara 30 chapter dan 5 jalur spesialisasi tanpa kewajiban menyelesaikan chapter sebelumnya secara linier.
4. **Pemecahan Masalah Algoritmik:** Latihan terarah bertahap yang mengasah daya nalar algoritmik dari kasus dasar hingga optimasi kompleksitas Big-O.
5. **Keterampilan Standar Industri:** Menanamkan konvensi kode Python (PEP 8), penanganan error terstruktur, modularitas fungsi, hingga pengujian otomatis.
6. **Sumber Terbuka & Terbuka untuk Umum:** Seluruh materi dapat diakses secara bebas sebagai kontribusi nyata bagi literasi pemrograman dan rekayasa telekomunikasi.

---

## 3. Arsitektur Kurikulum

Kurikulum Python Learning Hub disusun berjenjang dan mencakup:

### 3 Level Kompetensi Utama
1. **Level 1 — Python Foundations (Chapter 01 – 12)**  
   *Selaras secara luas dengan area kompetensi sertifikasi Python Institute PCEP.*  
   Mencakup: Pengenalan Python & instalasi interpreter, variabel & tipe data skalar, operator aritmatika & logika, masukan/keluaran interaktif, percabangan if/elif/else, perulangan for & while, pemrosesan sequence string, struktur data list & tuple, kamus dictionary & set, rancangan fungsi modular & scope LEGB, modul & exception handling dasar, serta Foundations Capstone Project.
2. **Level 2 — Intermediate Python Development (Chapter 13 – 22)**  
   *Selaras secara luas dengan area kompetensi sertifikasi Python Institute PCAP.*  
   Mencakup: Advanced functions (*args, **kwargs, lambda), list/dict/set comprehension, generator expressions, algoritma pencarian (linear & binary search), algoritma pengurutan (selection, bubble, insertion sort), analisis kompleksitas Big-O, file handling (I/O, CSV, JSON), exception handling & debugging terstruktur, OOP I (class, object, attribute, method), OOP II (inheritance, polymorphism, encapsulation, dunder methods), virtual environment & packaging (pip, venv, pytest), serta Intermediate Capstone Project.
3. **Level 3 — Professional Python Engineering (Chapter 23 – 30)**  
   *Standar rekayasa sistem perangkat lunak industri.*  
   Mencakup: Advanced OOP & Gang of Four Design Patterns, decorators, custom generators & context managers (`with`), static typing & type hints (`typing`, `mypy`, Pydantic), automated testing & logging (`logging`, `pytest`, mock), concurrent & asynchronous programming (`threading`, `multiprocessing`, `asyncio`), networking & REST API integration (`FastAPI`, `httpx`), software architecture & containerized deployment (Docker, CI/CD), serta Professional Capstone Project.

### 5 Jalur Spesialisasi Industri
- **Track A: Data Science & Visualization** (NumPy, Pandas, Matplotlib, Seaborn, exploratory data analysis).
- **Track B: Artificial Intelligence & Machine Learning** (Scikit-Learn, feature engineering, regresi, klasifikasi, clustering).
- **Track C: Web Development & APIs** (FastAPI, SQLAlchemy, JWT auth, background workers Celery/Redis).
- **Track D: Automation & Scripting** (pathlib, BeautifulSoup, Playwright, openpyxl, alert webhooks).
- **Track E: IoT, Signal Processing & Telecommunications** (SciPy signal, analisis propagasi sinyal RSRP/RSRQ, protokol MQTT, telemetri sensor).

*Pernyataan Independensi: Kurikulum ini dikembangkan secara independen oleh Aji Pamungkas Tri Nurcahyo sebagai sarana belajar mandiri terbuka. Kurikulum diselaraskan secara luas dengan area kompetensi sertifikasi industri, namun platform ini bersifat independen dan tidak terafiliasi resmi maupun disponsori komersial oleh Python Institute.*

---

## 4. Fitur Utama Platform

- **Perpustakaan Terbuka & Bebas Akses**: Tidak memerlukan login, pendaftaran akun, maupun tracking progress wajib. Pengguna dapat melompat ke chapter mana saja.
- **Beranda Interaktif (Home Page)**:
  - Hero banner responsif dengan tagline *Learn Python, One Chapter at a Time*.
  - Ringkasan metrik kurikulum (3 Level, 30 Chapter, 5 Spesialisasi, Chapter Siap Belajar).
  - Kartu pengenalan 3 Level Kompetensi lengkap dengan capaian dan capstone.
  - Kartu 5 Jalur Spesialisasi terapan industri.
  - Roadmap visual 4 tahapan penguasaan komprehensif.
  - Browser 30 chapter interaktif dengan filter level, status ketersediaan, dan pencarian instan.
- **Halaman Tentang Platform (`#/about`)**:
  - Ikhtisar platform edukasi Python.
  - Profil inisiator dan pengembang (Aji Pamungkas Tri Nurcahyo).
  - Penjabaran 6 filosofi pembelajaran.
  - Atribusi dan transparansi lisensi sumber terbuka.
- **Halaman Detail Level (`#/level/:id`)**:
  - Target kompetensi, capaian pembelajaran (*learning outcomes*), prasyarat, deskripsi capstone project, dan daftar chapter terkait.
- **Halaman Silabus Spesialisasi (`#/track/:id`)**:
  - Target profesi, 5 modul materi berurutan, dan prasyarat chapter dasar.
- **Halaman Modul Pembelajaran (`#/chapter/:id`)**:
  - Metadata modul (level, kesulitan, estimasi jam, fokus kompetensi).
  - Tautan langsung ke presentasi interaktif Reveal.js 6 dan mode baca dokumen linier.
  - Penampil kode sumber dengan syntax highlighting Shiki dan tombol salin satu-klik.
  - Output terminal hasil eksekusi CPython 3 nyata.
  - Latihan terarah (*Guided Exercise*) dengan langkah instruksi dan tips pengujian.
  - Kuis konsep (*Conceptual Quiz*) dengan pengungkapan pembahasan.
  - Tugas praktik mandiri (*Assignment Card*) dengan spesifikasi, starter code, tautan unduh panduan, dan rubrik penilaian berbobot 100%.
  - Navigasi antar-chapter (Sebelumnya / Selanjutnya).
  - Tampilan *Coming Soon* ramah pengguna untuk chapter yang masih dalam penulisan silabus.
- **Sistem Presentasi Reveal.js 6**:
  - Navigasi keyboard penuh (`Panah`, `Space`, `ESC`).
  - Slide Overview (`ESC` / `O`).
  - Speaker View (`S`) lengkap dengan catatan pemateri, jam, dan cuplikan slide berikutnya.
  - Rasio layar adaptif: Auto, 16:9, dan 4:3.
  - Ekspor/Cetak PDF melalui menu browser (`?print-pdf`).
  - Rendering rumus matematika presisi menggunakan KaTeX.
- **Dukungan Tampilan & Aksesibilitas**:
  - Light mode, Dark mode, dan Auto (mengikuti sistem operasi).
  - Tipografi Google Sans Flex & Code yang tersimpan lokal (tanpa dependensi eksternal Google Fonts).
  - Kontras tinggi ramah proyektor kelas dan layar redup.
  - Dukungan navigasi keyboard ramah screen reader (`skip-link`).

---

## 5. Manajemen Sumber Daya Materi Pembelajaran

Untuk mendukung skalabilitas materi pembelajaran pada chapter-chapter berikutnya, struktur penyimpanan berkas diatur sebagai berikut:

```text
public/downloads/
├── examples/               # Skrip Python (.py) mandiri untuk diunduh pembaca
│   ├── p09-01.py
│   ├── ...
│   └── p09-module/
│       └── statistik.py
├── pertemuan-09/           # Paket unduhan materi per chapter
│   ├── contoh.py           # Starter code contoh Python
│   └── tugas.md            # Panduan tugas mandiri dalam format Markdown
├── pertemuan-10/
│   ├── contoh.py
│   └── tugas.md
├── datasets/               # Dataset latihan (CSV, JSON) untuk data science & IoT
├── docs/                   # Dokumen PDF / cheatsheet pendukung
├── .nojekyll               # Penanda non-Jekyll untuk GitHub Pages
├── LICENSE.upstream        # Salinan lisensi MIT dari repositori upstream
└── Materi_Pengkom_Pertemuan_9_10_Python.pptx  # Slide sumber PPTX
```

Setiap chapter baru dapat menambahkan berkas pendukung pada direktori `public/downloads/chapter-XX/` atau `pertemuan-XX/`, dan berkas tersebut akan langsung dapat diunduh tanpa konfigurasi server tambahan.

---

## 6. Menjalankan di Lingkungan Lokal

### Prasyarat Perangkat Lunak
- **Node.js**: Versi 20+ (direkomendasikan v22 LTS / v24+)
- **npm**: Versi 10+
- **Python**: Versi 3.10+ (untuk menjalankan verifikasi eksekusi kode CPython)

### Langkah Instalasi & Menjalankan Server Dev
```powershell
# 1. Masuk ke direktori proyek
cd "D:\Workstation\Repo My Corses\Alpro-python"

# 2. Pasang dependensi
npm ci

# 3. Jalankan server lokal Vite
npm run dev
```
Buka peramban pada URL yang ditampilkan di terminal (default: `http://localhost:8932` atau `http://localhost:5173`).

### Skrip Pengujian & QA Lengkap
```powershell
# 1. Memeriksa konsistensi seluruh 24 contoh kode Python terhadap keluaran CPython
npm run check:outputs

# 2. Memeriksa ketersediaan konten dan slide materi
npm run check:content

# 3. Typecheck TypeScript (tsc --noEmit)
npm run typecheck

# 4. Linting ESLint (standar kode bebas error)
npm run lint

# 5. Build produksi dan verifikasi seluruh 20 rute statis
npm run build

# 6. Menjalankan server preview hasil build produksi
npm run preview
```

---

## 7. Publikasi & Hosting Statis Gratis (GitHub Pages)

Proyek ini telah dikonfigurasi secara lengkap untuk dapat dipublikasikan secara gratis di **GitHub Pages** menggunakan arsitektur multi-page static site builder Vite dan GitHub Actions.

### Format URL Publik yang Diharapkan
```text
https://USERNAME.github.io/python-learning-hub/
```
*(Ganti `USERNAME` dengan username akun GitHub Anda)*

### Kompatibilitas Subpath & SPA Routing
- **Base Path Adaptif:** Konfigurasi `vite.config.ts` menggunakan `base: process.env.VITE_BASE_PATH || './'`, menghasilkan jalur aset relatif (`./assets/...` dan `../assets/...`) yang dapat berjalan lancar di subpath repositori GitHub Pages, root domain kustom, maupun Cloudflare Pages.
- **Dukungan Refresh Peramban (`404.html` SPA Handler):** File `404.html` dilengkapi skrip pengalih otomatis yang mempertahankan path dan parameter URL yang diminta, lalu memuatnya kembali melalui hash route sehingga refresh pada URL nested (`/chapter/10`, `/level/2`, `/about`) tidak menghasilkan halaman kosong atau 404.
- **Bebas Jekyll (`.nojekyll`):** File `public/.nojekyll` otomatis disertakan ke folder `dist/` untuk mencegah pemrosesan Jekyll pada GitHub Pages.

### Alur Kerja GitHub Actions (`.github/workflows/deploy.yml`)
Workflow otomatis telah disiapkan di `.github/workflows/deploy.yml`:
1. Berjalan otomatis saat ada `push` ke branch `main`, atau dijalankan manual melalui menu `Actions > Deploy to GitHub Pages > Run workflow` (`workflow_dispatch`).
2. Menyiapkan Python 3.12 dan Node.js 22 dengan cache dependensi npm.
3. Menjalankan seluruh pengujian: `check:outputs`, `check:content`, `typecheck`, `lint`, dan `build`.
4. Mengunggah folder `dist/` dan mempublikasikannya ke GitHub Pages dengan izin token minimum (`contents: read`, `pages: write`, `id-token: write`).

### Langkah-Langkah Publikasi oleh Pemilik Repositori
Berikut adalah langkah yang perlu dilakukan pada akun GitHub Anda:

1. **Buat Repositori Baru di GitHub:**
   - Masuk ke akun GitHub Anda dan buat repositori baru bernama: `python-learning-hub`.
   - Pilih visibilitas **Public**.
   - Jangan centang "Add a README file" atau .gitignore (karena proyek lokal sudah memilikinya).

2. **Inisialisasi & Push Kode Lokal ke GitHub:**
   ```powershell
   cd "D:\Workstation\Repo My Corses\Alpro-python"

   # Inisialisasi git jika belum ada
   git init

   # Tambahkan semua berkas yang telah siap
   git add .

   # Buat commit pertama
   git commit -m "feat: initial release of Python Learning Hub"

   # Pastikan branch utama bernama main
   git branch -M main

   # Hubungkan ke repositori GitHub Anda (ganti USERNAME)
   git remote add origin https://github.com/USERNAME/python-learning-hub.git

   # Push ke GitHub
   git push -u origin main
   ```

3. **Aktifkan GitHub Pages melalui GitHub Actions:**
   - Masuk ke halaman repositori di GitHub: `https://github.com/USERNAME/python-learning-hub/settings/pages`.
   - Pada bagian **Build and deployment > Source**, pilih opsi: **GitHub Actions**.
   - Setelah branch `main` di-push, workflow `Deploy to GitHub Pages` akan berjalan secara otomatis di tab **Actions**.
   - Setelah workflow selesai (status hijau), situs web Anda akan aktif di:  
     `https://USERNAME.github.io/python-learning-hub/`

### Kompatibilitas Cloudflare Pages (Alternatif Masa Depan)
Aplikasi ini juga 100% kompatibel dengan Cloudflare Pages untuk domain kustom atau root-domain hosting gratis:
- **Framework preset:** `Vite`
- **Build command:** `npm run build`
- **Build output directory:** `dist`
- **Root directory:** `/`

---

## 8. Struktur Rute Aplikasi

| Rute URL | Tampilan / Fungsi |
|---|---|
| `#/` atau `index.html` | Beranda Python Learning Hub (Hero, Level, Spesialisasi, Roadmap, Browser 30 Chapter) |
| `#/about` | Halaman Tentang Platform, Profil Pengembang & Filosofi Belajar |
| `#/level/1`, `#/level/2`, `#/level/3` | Halaman detail Level 1, 2, atau 3 (Silabus, target kompetensi, capstone) |
| `#/track/:id` | Halaman silabus jalur spesialisasi (misal `#/track/data-science`, `#/track/iot-telecom`) |
| `#/chapter/:id` | Halaman modul pembelajaran chapter 1 s.d. 30 (Slide, kode, output, latihan, kuis, tugas) |
| `/pertemuan-09/index.html` | Slide presentasi interaktif Reveal.js untuk Materi Chapter 09 (Fungsi, Scope, Modul) |
| `/pertemuan-10/index.html` | Slide presentasi interaktif Reveal.js untuk Materi Chapter 10 (Struktur Data Python) |
| `/pertemuan-09/tugas.html` & `10` | Dokumen panduan tugas praktik mandiri dan tabel rubrik penilaian |
| `/pertemuan-09/index.html?view=read` | Mode baca dokumen linier untuk perangkat ponsel / tablet |
| `/pertemuan-01/`–`08/`, `/pertemuan-11/`–`16/` | Rute placeholder (Segera Hadir) yang mengarahkan kembali ke kurikulum Hub |
| `/404.html` | Halaman penanganan URL tidak ditemukan & router fallback |

---

## 9. Struktur Direktori Proyek

```text
Alpro-python/
├── .github/
│   └── workflows/
│       └── deploy.yml         # GitHub Actions CI/CD deployment ke GitHub Pages
├── src/
│   ├── code/                  # Skrip Python sumber, outputs.json, verifikator eksekusi CPython
│   ├── components/            # Komponen modular edukasi:
│   │   ├── AssignmentCard.tsx # Kartu tugas dengan spesifikasi, unduh, dan tabel rubrik penilaian
│   │   ├── ChapterNavigation.tsx # Tombol navigasi chapter sebelumnya / berikutnya
│   │   ├── CodeBlock.tsx         # Tokenizer Shiki dengan penomoran baris & tombol salin
│   │   ├── CodeOutput.tsx        # Terminal card keluaran nyata CPython
│   │   ├── DifficultyBadge.tsx   # Badge Beginner / Intermediate / Advanced
│   │   ├── ExerciseCard.tsx      # Latihan terarah dengan langkah dan tips pengujian
│   │   ├── LearningObjectives.tsx# Kartu daftar capaian tujuan pembelajaran
│   │   ├── PrerequisiteList.tsx  # Daftar prasyarat materi
│   │   └── QuizCard.tsx          # Kuis konsep interaktif dengan pembukaan pembahasan
│   ├── curriculum/
│   │   └── index.ts           # Definisi terpusat 3 Level, 30 Chapter, 5 Tracks, dan Disclaimer
│   ├── deck-shell/            # Toolbar presentasi Reveal.js, preferensi tema, rasio layar
│   ├── decks/                 # Data slide JSON pertemuan 9 & 10, registri slide, markdown tugas
│   ├── layouts/
│   │   └── SlideContent.tsx   # Komponen tata letak konten slide Reveal.js
│   ├── pages/
│   │   ├── HomePage.tsx       # Beranda utama Python Learning Hub
│   │   ├── AboutPage.tsx      # Halaman Tentang Platform, Profil Pengembang & Filosofi Belajar
│   │   ├── LevelPage.tsx      # Halaman rincian level kompetensi
│   │   ├── TrackPage.tsx      # Halaman silabus jalur spesialisasi
│   │   └── ChapterPage.tsx    # Halaman modul pembelajaran chapter aktif & upcoming
│   ├── theme/
│   │   └── styles.css         # Desain sistem Material 3, Dark/Light mode overrides, responsive
│   ├── ui/                    # Komponen utilitas (Icon, Code, Highlight, Math)
│   └── main.tsx               # Entry point aplikasi React & router SPA
├── scripts/
│   ├── check_outputs.mjs      # Verifikator output CPython 3
│   ├── check_content.mjs      # Verifikator slide materi & kelengkapan slide
│   └── test_routes.mjs        # Verifikator integritas 20 rute produksi di dist/
├── public/                    # Aset statis yang disalin langsung ke dist/
│   ├── .nojekyll              # Penonaktif pemroses Jekyll GitHub Pages
│   └── downloads/             # Berkas materi sumber (.pptx, .md, .py) untuk diunduh pengguna
├── dist/                      # Direktori keluaran build produksi Vite
├── index.html                 # Entry point HTML utama
├── 404.html                   # Halaman fallback 404 & SPA redirect handler
├── package.json               # Konfigurasi dependensi dan skrip npm
├── tsconfig.json              # Konfigurasi TypeScript
├── vite.config.ts             # Konfigurasi bundler Vite multi-page
├── .gitignore                 # Konfigurasi pengabaian Git (node_modules, build, secrets, temp)
└── README.md                  # Dokumentasi resmi proyek
```

---

## 10. Atribusi & Lisensi Sumber Terbuka

- **Pengembang & Penulis Kurikulum Python Learning Hub:**  
  Aji Pamungkas Tri Nurcahyo (Program Studi Teknik Telekomunikasi, FTI, Institut Teknologi Sumatera).
- **Fondasi Perangkat Lunak:**  
  Arsitektur peramban slide dan fondasi teknis situs diadaptasi dari repositori open-source [Pengkom ITERA](https://github.com/informatika-itera/pengkom) di bawah ketentuan [MIT License](downloads/LICENSE.upstream).
- **Pustaka Pihak Ketiga:**  
  - [React](https://react.dev/) — MIT License
  - [Reveal.js](https://revealjs.com/) — MIT License (Hak Cipta Hakim El Hattab)
  - [Shiki](https://shiki.style/) — MIT License (Anthony Fu & Pine Wu)
  - [KaTeX](https://katex.org/) — MIT License (Khan Academy)
  - [Google Sans Flex & Code](https://fonts.google.com/) — Open Font License
  - [Material Symbols](https://fonts.google.com/icons) — Apache License 2.0
