# Python Learning Hub

> **Tagline:** Learn Python, One Chapter at a Time  
> **Subtitle:** Interactive Python Learning Modules  
> **Status:** Open Access Educational Resource (OER)  
> **Repository:** `https://github.com/aji-nurcahyo/Python-Learning-Hub`  
> **Live Site URL (GitHub Pages):** `https://aji-nurcahyo.github.io/Python-Learning-Hub/`

Python Learning Hub is a free, open-access collection of structured Python learning modules, interactive browser presentations, verified programming examples, guided exercises, conceptual quizzes, and practical projects.

Developed and maintained by **Aji Pamungkas Tri Nurcahyo** from **Institut Teknologi Sumatera (ITERA)**.

---

## 1. Identitas & Pengembang Platform

- **Nama Proyek:** Python Learning Hub
- **Tagline:** *Learn Python, One Chapter at a Time*
- **Subjudul:** *Interactive Python Learning Modules*
- **Inisiator & Pengembang:** **Aji Pamungkas Tri Nurcahyo**
- **Institusi Resmi:** **Institut Teknologi Sumatera (ITERA)**
- **Tujuan Platform:** Menyediakan materi edukasi pemrograman Python 3 yang independen, gratis, terstruktur secara bertahap, dan dapat diakses siapa pun tanpa batasan registrasi maupun sekat jadwal perkuliahan.

---

## 2. Filosofi Pembelajaran

Platform ini dibangun berlandaskan 6 pilar edukasi komputasi modern:

1. **Pemahaman Konseptual Mendalam:** Menjelaskan logika di balik sintaks, alokasi memori, prinsip interpreter CPython, dan alasan teknis di balik rancangan suatu struktur data atau fungsi.
2. **Eksekusi Nyata & Terverifikasi:** Seluruh 209 contoh kode inti dan 100 skrip spesialisasi (total 309 program Python, 25 suite `pytest`, dan 10 Jupyter notebook) dieksekusi oleh CPython 3. Keluaran terminal yang ditampilkan di antarmuka web adalah hasil aktual sistem tanpa manipulasi simulasi.
3. **Eksplorasi Mandiri Tanpa Sekat:** Pengguna memiliki kebebasan penuh memilih modul mana pun di antara 30 Core Chapter dan 25 Modul Spesialisasi (total 55 modul pembelajaran) tanpa kewajiban menyelesaikan modul sebelumnya secara linier.
4. **Pemecahan Masalah Algoritmik:** Latihan terarah bertahap yang mengasah daya nalar algoritmik dari kasus dasar hingga optimasi kompleksitas Big-O.
5. **Keterampilan Standar Industri:** Menanamkan konvensi kode Python (PEP 8), penanganan error terstruktur, modularitas fungsi, hingga pengujian otomatis.
6. **Sumber Terbuka & Terbuka untuk Umum:** Seluruh materi dapat diakses secara bebas sebagai kontribusi nyata bagi literasi pemrograman dan rekayasa telekomunikasi.

---

## 3. Arsitektur Kurikulum

Kurikulum Python Learning Hub disusun berjenjang dan mencakup:

### Modul Pengantar: Getting Started with Python (Setup Environment)
Panduan onboarding praktis penyiapan *Python Development Environment* lokal dan cloud secara mandiri:
- **Tutorial 01:** Understanding Python Development Tools (Interpreter vs IDE vs Terminal vs Notebook)
- **Tutorial 02:** Installing Python (Instalasi CPython resmi, PATH, Python Launcher di Windows/Linux/macOS)
- **Tutorial 03:** Installing & Configuring VS Code (Ekstensi Python, Open Folder, Interpreter Selection, Debugging F5)
- **Tutorial 04:** Jupyter Notebook & JupyterLab (Struktur `.ipynb`, pip install, server lokal, eksekusi sel & kernel)
- **Tutorial 05:** Virtual Environment & Package Management (`venv`, aktivasi lintas OS, `pip`, `requirements.txt`)
- **Tutorial 06:** Google Colab (Cloud notebook gratis, `!pip`, Google Drive mount, batasan runtime & kuota GPU)
- **Tutorial 07:** Running Python Projects (Navigasi direktori, eksekusi `main.py`, relative imports, traceback error)
- **Tutorial 08:** Troubleshooting & Environment Verification (Solusi aman kendala umum & verifikasi 8 langkah)

### 3 Level Kompetensi Utama (30 Chapter)
1. **Level 1 — Python Foundations (Chapter 01 – 12)**  
   *Selaras secara luas dengan area kompetensi sertifikasi Python Institute PCEP.*  
   Mencakup: Pengenalan Python & Python Interpreter, variabel & tipe data skalar, operator aritmatika & logika, masukan/keluaran interaktif, percabangan if/elif/else, perulangan for & while, pemrosesan sequence string, struktur data list & tuple, dictionary & set, rancangan fungsi modular & scope LEGB, modul & exception handling dasar, serta Foundations Capstone Project.
2. **Level 2 — Intermediate Python Development (Chapter 13 – 22)**  
   *Selaras secara luas dengan area kompetensi sertifikasi Python Institute PCAP.*  
   Mencakup: Advanced functions (*args, **kwargs, lambda), list/dict/set comprehension, generator expressions, algoritma pencarian (linear & binary search), algoritma pengurutan (selection, bubble, insertion sort), analisis kompleksitas Big-O, file handling (I/O, CSV, JSON), Exception Handling & debugging terstruktur, OOP I (class, object, attribute, method), OOP II (Inheritance, Polymorphism, Encapsulation, dunder methods), Virtual Environment & packaging (`pyproject.toml`, pytest), serta Intermediate Capstone Project.
3. **Level 3 — Professional Python Engineering (Chapter 23 – 30)**  
   *Standar rekayasa sistem perangkat lunak industri.*  
   Mencakup: Advanced OOP & Gang of Four Design Patterns, decorators, custom generators & context managers (`with`), static typing & type hints (`typing`, `mypy`), automated testing & structured logging (`logging`, `unittest`, mock), concurrent & asynchronous programming (`threading`, `multiprocessing`, `asyncio`), networking & REST API integration, Clean Architecture & containerized deployment (Docker, CI/CD Actions), serta Professional Capstone Project.

### 5 Jalur Spesialisasi Industri (25 Modul: `A01`–`E05`)
- **Track A (`A01`–`A05`): Data Science & Visualization** (NumPy `ndarray`, Pandas wrangling, EDA, Matplotlib/Seaborn multi-panel visualizations, Capstone End-to-End Analytics Report).
- **Track B (`B01`–`B05`): Artificial Intelligence & Machine Learning** (Scikit-Learn Pipelines anti-*data leakage*, Regression & Classification, Clustering & PCA, Cross-Validation & `GridSearchCV`, Capstone Predictive Maintenance).
- **Track C (`C01`–`C05`): Web Development & APIs** (`httpx` client & Pydantic contracts, FastAPI REST CRUD, SQLAlchemy 2.0 ORM, API Security PBKDF2/HMAC & logging middleware, Capstone Modular REST API).
- **Track D (`D01`–`D05`): Automation & Scripting** (`pathlib`/`shutil` dry-run & ZIP rotation, OpenPyXL & `fpdf2` reporting, ethical `BeautifulSoup`/`robots.txt` parsing, exponential backoff & idempotency ledger, Capstone Autonomous Reporting Bot).
- **Track E (`E01`–`E05`): IoT, Signal Processing & Telecommunications** (Serial framing & XOR/`struct`, MQTT v2 publish-subscribe, SciPy FFT & Butterworth filtering, Wireless RF Analytics RSSI/RSRP/RSRQ/SINR vs SNR, Capstone IoT Monitoring Dashboard).

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
  - Tampilan tab modern terintegrasi: **Materi & Kode**, **Presentasi Slide**, **Latihan Terarah**, dan **Tugas Mandiri**.
  - Metadata modul (level, kesulitan, estimasi jam, fokus kompetensi).
  - Tautan langsung ke presentasi interaktif Reveal.js 6 dan mode baca dokumen linier.
  - Penampil kode sumber dengan syntax highlighting Shiki dan tombol salin satu-klik.
  - Output terminal hasil eksekusi CPython 3 nyata.
  - Latihan terarah (*Guided Exercise*) dengan langkah instruksi dan tips pengujian.
  - Kuis konsep (*Conceptual Quiz*) dengan pilihan ganda dan pengungkapan pembahasan.
  - Tugas praktik mandiri (*Assignment Card*) dengan spesifikasi, starter code, tautan unduh panduan, dan rubrik penilaian berbobot 100%.
  - Navigasi antar-chapter (Sebelumnya / Selanjutnya).
  - Tampilan *Coming Soon* ramah pengguna untuk chapter yang masih dalam penyusunan silabus.
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

## 5. Manajemen Konten Modular (`content/`)

Seluruh materi pembelajaran diorganisasikan dalam folder modular `content/`:

```text
content/
├── foundations/                     # Level 1 (Chapter 01 – 12)
│   ├── chapter-08/                 # List & Tuple
│   ├── chapter-09/                 # Dictionaries & Sets
│   ├── chapter-10/                 # Functions & Scope
│   ├── chapter-11/                 # Modules & Packages
│   └── ... (chapter-01 s.d. 12)
├── intermediate/                    # Level 2 (Chapter 13 – 22)
│   └── ... (chapter-13 s.d. 22)
├── professional/                    # Level 3 (Chapter 23 – 30)
│   └── ... (chapter-23 s.d. 30)
└── specializations/                 # 5 Jalur Spesialisasi Industri
    ├── track-data-science/
    ├── track-ai-ml/
    ├── track-web-api/
    ├── track-automation/
    └── track-iot-telecom/
```

Setiap chapter memiliki struktur mandiri:
- `metadata.json`: Sumber data tunggal untuk ID, judul, tujuan pembelajaran, prasyarat, latihan, kuis, dan tugas.
- `index.md`: Ringkasan modul atau bacaan linier.
- `slides/deck.json`: Slide presentasi Reveal.js 6.
- `code/contoh.py`: Skrip program Python terverifikasi.
- `exercises/`: Soal latihan dan kunci pembahasan kuis.
- `assignments/tugas.md`: Panduan tugas mandiri dan kriteria penilaian.
- `assets/`: Diagram atau ilustrasi pendukung.

> 📖 **Panduan Penambahan Modul:** Untuk tata cara menambahkan chapter baru atau memperbarui modul yang sudah ada, baca [docs/ADDING_CHAPTER.md](docs/ADDING_CHAPTER.md).

---

## 6. Berkas Unduhan Publik (`public/downloads/`)

Berkas yang dapat diunduh langsung oleh pembaca disimpan di `public/downloads/`:

```text
public/downloads/
├── chapter-08/             # Paket starter Python & tugas Chapter 08
│   ├── contoh.py
│   └── tugas.md
├── chapter-09/             # Paket starter Python & tugas Chapter 09
│   ├── contoh.py
│   └── tugas.md
├── chapter-10/             # Paket starter Python & tugas Chapter 10
│   ├── contoh.py
│   └── tugas.md
├── chapter-11/             # Paket starter Python & tugas Chapter 11
│   ├── contoh.py
│   └── tugas.md
├── examples/               # Skrip Python mandiri terpisah (p09-01.py s.d. p10-09.py)
├── datasets/               # Dataset latihan (CSV, JSON) untuk data science & IoT
├── docs/                   # Dokumen PDF / cheatsheet pendukung
├── .nojekyll               # Penanda non-Jekyll untuk GitHub Pages
├── LICENSE.upstream        # Salinan lisensi MIT dari repositori upstream
└── Materi_Pengkom_Pertemuan_9_10_Python.pptx  # Slide sumber PPTX
```

---

## 7. Menjalankan di Lingkungan Lokal

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
# 1. Memeriksa konsistensi 209 contoh kode inti terhadap keluaran CPython
npm run check:outputs

# 2. Memeriksa ketersediaan konten 30 chapter, aset, dan presentasi
npm run check:content
npm run check:presentations

# 3. Memeriksa 25 modul spesialisasi, 376 slide, dan output spec-outputs.json
npm run check:specializations

# 4. Typecheck TypeScript (tsc --noEmit) dan Linting ESLint
npm run typecheck
npm run lint

# 5. Build produksi lokal (base path default './') dan verifikasi rute statis di dist/
npm run build

# 6. Build produksi GitHub Pages (base path '/Python-Learning-Hub/')
npm run build:pages

# Alternatif manual PowerShell (Windows):
# $env:VITE_BASE_PATH="/Python-Learning-Hub/"
# npm run build

# Alternatif manual Linux / macOS:
# VITE_BASE_PATH="/Python-Learning-Hub/" npm run build

# 7. (Opsional, menggunakan .venv) Menjalankan seluruh 100 skrip spesialisasi, 25 pytest, & 10 notebooks
.\.venv\Scripts\python.exe scripts/run_specialization_examples.py --check

# 8. Menjalankan server preview hasil build produksi
npm run preview
```

---

## 8. Publikasi & Hosting Statis Gratis (GitHub Pages)

Proyek ini telah dikonfigurasi secara lengkap untuk dapat dipublikasikan secara gratis di **GitHub Pages** menggunakan bundler Vite SPA dan GitHub Actions.

### Format URL Publik yang Diharapkan
```text
https://aji-nurcahyo.github.io/Python-Learning-Hub/
```

### Kompatibilitas Subpath & SPA Routing
- **Base Path Adaptif & Permanen:** Konfigurasi `vite.config.ts` membaca `process.env.VITE_BASE_PATH` (default `'./'` untuk pengembangan lokal), sedangkan skrip `npm run build:pages` dan workflow GitHub Actions secara permanen menetapkan `VITE_BASE_PATH="/Python-Learning-Hub/"` untuk produksi GitHub Pages.
- **Dukungan Refresh Peramban (`404.html` SPA Handler):** File `404.html` dilengkapi skrip pengalih otomatis yang menormalkan base subpath `/Python-Learning-Hub/` serta mempertahankan path dan parameter URL yang diminta, lalu memuatnya kembali melalui hash route sehingga refresh pada URL nested (`/chapter/10`, `/spec/A01`, `/level/2`, `/about`) tidak menghasilkan halaman kosong atau 404. Selain itu, tautan lama seperti `/pertemuan-09/` dialihkan ke chapter baru `#/chapter/10`.
- **Bebas Jekyll (`.nojekyll`):** File `public/.nojekyll` otomatis disertakan ke folder `dist/` untuk mencegah pemrosesan Jekyll pada GitHub Pages.

### Alur Kerja GitHub Actions (`.github/workflows/deploy.yml`)
Workflow otomatis telah disiapkan di `.github/workflows/deploy.yml`:
1. Berjalan otomatis saat ada `push` ke branch `main`, atau dijalankan manual melalui menu `Actions > Deploy to GitHub Pages > Run workflow` (`workflow_dispatch`).
2. Menyiapkan Python 3.12 dan Node.js 22 dengan cache dependensi npm.
3. Menjalankan `npm ci`, `npm run lint`, lalu `npm run build:pages` dengan `env: VITE_BASE_PATH: /Python-Learning-Hub/` (yang juga menjalankan validasi `check:outputs`, `check:content`, `check:presentations`, `check:specializations`, `typecheck`, `vite build`, dan `test:routes`).
4. Mengunggah folder `dist/` dan mempublikasikannya ke GitHub Pages dengan izin token minimum (`contents: read`, `pages: write`, `id-token: write`).

### Langkah-Langkah Publikasi oleh Pemilik Repositori
1. **Repositori Target di GitHub:**
   - Repositori: `https://github.com/aji-nurcahyo/Python-Learning-Hub` (visibilitas **Public**).

2. **Sinkronisasi Repositori Lokal & Push ke GitHub (Branch `main`):**
   ```powershell
   cd "D:\Workstation\Repo My Corses\Alpro-python"

   # Pastikan working tree bersih dan berada di branch main
   git status
   git remote -v

   # Push ke GitHub (hanya setelah verifikasi lokal selesai)
   git push -u origin main
   ```

3. **Aktifkan GitHub Pages melalui GitHub Actions:**
   - Masuk ke halaman repositori di GitHub: `https://github.com/aji-nurcahyo/Python-Learning-Hub/settings/pages`.
   - Pada bagian **Build and deployment > Source**, pilih opsi: **GitHub Actions**.
   - Setelah branch `main` di-push, workflow `Deploy to GitHub Pages` akan berjalan secara otomatis di tab **Actions**.
   - Setelah workflow selesai (status hijau), uji seluruh rute pada URL live:  
     `https://aji-nurcahyo.github.io/Python-Learning-Hub/`

---

## 9. Struktur Rute Aplikasi

| Rute URL | Tampilan / Fungsi |
|---|---|
| `#/` atau `index.html` | Beranda Python Learning Hub (Hero, Level, Spesialisasi, Roadmap, Browser 30 Chapter) |
| `#/about` | Halaman Tentang Platform, Profil Pengembang & Filosofi Belajar |
| `#/getting-started` | Panduan onboarding setup Python Development Environment lokal & Colab |
| `#/level/1`, `#/level/2`, `#/level/3` | Halaman detail Level 1, 2, atau 3 (Silabus, target kompetensi, capstone) |
| `#/track/:id` | Halaman silabus jalur spesialisasi (misal `#/track/data-science`, `#/track/iot-telecom`) |
| `#/spec/:id` | Halaman modul spesialisasi `A01`–`E05` (Ikhtisar, Kode & Output, Latihan & Kuis, Tugas) |
| `#/spec/:id/slides` | Tampilan slide presentasi modul spesialisasi layar penuh |
| `#/spec/:id/read` | Mode baca dokumen linier modul spesialisasi |
| `#/spec/:id/task` | Tampilan fokus tugas praktik mandiri modul spesialisasi |
| `#/chapter/:id` | Halaman modul pembelajaran 30 Core Chapter (Tab Materi, Slide, Latihan, Tugas) |
| `#/chapter/:id/slides` | Slide presentasi interaktif layar penuh |
| `#/chapter/:id/read` | Mode baca dokumen linier untuk perangkat ponsel / tablet |
| `#/chapter/:id/task` | Tampilan fokus tugas praktik mandiri dan rubrik penilaian |
| `/404.html` | SPA redirect fallback (mengarahkan URL langsung & bookmark lama ke hash route) |

---

## 10. Struktur Direktori Proyek

```text
Alpro-python/
├── .github/
│   └── workflows/
│       └── deploy.yml         # GitHub Actions CI/CD deployment ke GitHub Pages
├── content/                   # Modular Chapter Curriculum (Single Source of Truth)
│   ├── foundations/           # Chapter 01 – 12
│   │   ├── chapter-08/        # Lists & Tuples (metadata, code, slides, exercises, tugas)
│   │   ├── chapter-09/        # Dictionaries & Sets
│   │   ├── chapter-10/        # Functions & Scope
│   │   ├── chapter-11/        # Modules & Docstrings
│   │   └── ... (chapter-01 s.d. 12)
│   ├── intermediate/          # Chapter 13 – 22
│   ├── professional/          # Chapter 23 – 30
│   └── specializations/       # 5 Specialization Tracks
├── src/
│   ├── code/                  # Skrip Python sumber, outputs.json, verifikator eksekusi CPython
│   ├── components/            # Komponen modular edukasi:
│   │   ├── AssignmentCard.tsx    # Kartu tugas dengan spesifikasi & starter code
│   │   ├── AssignmentSection.tsx # Section tugas mandiri dan tabel rubrik penilaian berbobot
│   │   ├── ChapterHeader.tsx     # Header chapter dengan breadcrumb, badge, & tombol aksi
│   │   ├── ChapterLayout.tsx     # Shell tata letak tab materi, slide, latihan, dan tugas
│   │   ├── ChapterNavigation.tsx # Navigasi chapter sebelumnya / berikutnya
│   │   ├── CodeBlock.tsx         # Tokenizer Shiki dengan penomoran baris & tombol salin
│   │   ├── CodeOutput.tsx        # Terminal card keluaran nyata CPython
│   │   ├── DifficultyBadge.tsx   # Badge Beginner / Intermediate / Advanced
│   │   ├── ExerciseCard.tsx      # Latihan terarah dengan langkah & tips pengujian
│   │   ├── ExerciseSection.tsx   # Section latihan terarah dan kuis konsep
│   │   ├── LearningObjectives.tsx# Kartu capaian tujuan pembelajaran
│   │   ├── PrerequisiteList.tsx  # Daftar prasyarat materi
│   │   ├── QuizCard.tsx          # Kuis konsep interaktif dengan pembukaan pembahasan
│   │   ├── ResourceDownloads.tsx # Tombol unduh materi (.py, .md, .pptx)
│   │   └── SlideViewer.tsx       # Embed presentasi Reveal.js di dalam tab chapter
│   ├── curriculum/
│   │   └── index.ts           # Definisi kurikulum 3 Level, 30 Chapter, 5 Tracks, dan Disclaimer
│   ├── deck-shell/            # Toolbar presentasi Reveal.js, preferensi tema, rasio layar
│   ├── decks/                 # Data slide JSON, registri slide, markdown tugas
│   ├── layouts/
│   │   └── SlideContent.tsx   # Komponen tata letak konten slide Reveal.js
│   ├── pages/
│   │   ├── HomePage.tsx       # Beranda utama Python Learning Hub
│   │   ├── AboutPage.tsx      # Halaman Tentang Platform, Profil Pengembang & Filosofi Belajar
│   │   ├── LevelPage.tsx      # Halaman rincian level kompetensi
│   │   ├── TrackPage.tsx      # Halaman silabus jalur spesialisasi
│   │   └── ChapterPage.tsx    # Halaman modul pembelajaran terintegrasi
│   ├── theme/
│   │   └── styles.css         # Desain sistem Material 3, Dark/Light mode overrides, responsive
│   ├── ui/                    # Komponen utilitas (Icon, Code, Highlight, Math)
│   └── main.tsx               # Entry point aplikasi React & router SPA
├── docs/
│   ├── ADDING_CHAPTER.md          # Panduan lengkap penambahan & pemeliharaan modul chapter
│   ├── TECHNICAL_LANGUAGE_GUIDE.md# Kebijakan standar bahasa & terminologi teknis
│   ├── GETTING_STARTED_GUIDE.md   # Panduan modul onboarding setup environment
│   ├── GITHUB_PAGES_DEPLOYMENT.md # Panduan publikasi & hosting GitHub Pages
│   └── FINAL_CURRICULUM_AUDIT.md  # Laporan audit final 30 chapter kurikulum
├── scripts/
│   ├── check_outputs.mjs      # Verifikator output CPython 3
│   ├── check_content.mjs      # Verifikator integritas 30 paket chapter dan 5 tracks
│   ├── check_content.py       # Validasi Python independen untuk metadata chapter
│   ├── run_examples.py        # Runner eksekusi CPython 3
│   └── test_routes.mjs        # Verifikator integritas bundle dist/
├── public/                    # Aset statis yang disalin langsung ke dist/
│   ├── .nojekyll              # Penonaktif pemroses Jekyll GitHub Pages
│   └── downloads/             # Berkas materi sumber (.pptx, .md, .py) untuk diunduh pengguna
├── legacy/                    # Arsip baca-saja materi awal perkuliahan
├── dist/                      # Direktori keluaran build produksi Vite
├── index.html                 # Entry point HTML utama
├── 404.html                   # Halaman fallback 404 & SPA redirect handler
├── package.json               # Konfigurasi dependensi dan skrip npm
├── tsconfig.json              # Konfigurasi TypeScript
├── vite.config.ts             # Konfigurasi bundler Vite
├── .gitignore                 # Konfigurasi pengabaian Git (node_modules, build, secrets, temp)
└── README.md                  # Dokumentasi resmi proyek
```

---

## 11. Atribusi & Lisensi Sumber Terbuka

- **Pengembang & Penulis Kurikulum Python Learning Hub:**  
  Aji Pamungkas Tri Nurcahyo (Institut Teknologi Sumatera).
- **Fondasi Perangkat Lunak:**  
  Arsitektur peramban slide dan fondasi teknis situs diadaptasi dari repositori open-source [Pengkom ITERA](https://github.com/informatika-itera/pengkom) di bawah ketentuan [MIT License](LICENSE.upstream).
- **Pustaka Pihak Ketiga:**  
  - [React](https://react.dev/) — MIT License
  - [Reveal.js](https://revealjs.com/) — MIT License (Hak Cipta Hakim El Hattab)
  - [Shiki](https://shiki.style/) — MIT License (Anthony Fu & Pine Wu)
  - [KaTeX](https://katex.org/) — MIT License (Khan Academy)
  - [Google Sans Flex & Code](https://fonts.google.com/) — Open Font License
  - [Material Symbols](https://fonts.google.com/icons) — Apache License 2.0
