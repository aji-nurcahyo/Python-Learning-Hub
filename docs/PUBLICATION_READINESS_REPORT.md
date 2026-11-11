# Laporan Kesiapan Publikasi Perdana — Python Learning Hub

> **Repositori Target:** `https://github.com/aji-nurcahyo/Python-Learning-Hub`  
> **Direktori Proyek Lokal:** `D:\Workstation\Repo My Corses\Alpro-python`  
> **Pengembang & Institusi:** Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera  
> **URL GitHub Pages Produksi:** `https://aji-nurcahyo.github.io/Python-Learning-Hub/`  
> **Status Konfigurasi:** **Terkonfigurasi Permanen (`/Python-Learning-Hub/`) — Siap Push & Verifikasi Workflow**

---

## 1. Status Repositori Git & Audit `.gitignore`

- **Branch Aktif:** `main` (tidak ada remote GitHub yang terpasang — `git remote -v` kosong sesuai aturan aman sebelum persetujuan push perdana).
- **Kebersihan Berkas Terlacak (`git ls-files`):**
  - `node_modules/`, `.venv/`, `dist/`, `.env`, `.env.*`, `*.pem`, `*.key`, `*.db`, `*.sqlite`, `*.sqlite3`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.ipynb_checkpoints/`, dan `*.log` diabaikan pada [`.gitignore`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/.gitignore).
  - Verifikasi `git ls-files` mengonfirmasi nol berkas dependensi, virtual environment, hasil build `dist/`, maupun database lokal masuk ke indeks Git.

---

## 2. Audit Keamanan, Lisensi & Atribusi

- **Pemindaian Kredensial & Data Sensitif (`git grep`):**
  - Nol kunci API produksi (`AKIA...`, `ghp_...`, `AIza...`, `sk-...`), nol private key PEM, dan nol file `.env` tersimpan di repositori.
  - Dua kemunculan kata `Bearer` pada Chapter 28 ([exercise.md](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/content/professional/chapter-28/exercises/exercise.md#L94) dan [test_networking.py](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/content/professional/chapter-28/tests/test_networking.py#L69)) merupakan string dummy edukatif untuk latihan penyensoran header log.
  - Seluruh modul autentikasi di Track C (`C04`, `C05`) menerima secret uji melalui parameter fungsi / env mapping lokal, tanpa secret produksi hardcoded.
  - Seluruh dataset CSV, log serial, drive test RF, serta snapshot HTML di `content/specializations/*/modules/*/datasets/` adalah data sintetis edukatif buatan mandiri (bebas PII dan bebas data privat institusi/operator).
- **Lisensi & Atribusi Upstream:**
  - [`LICENSE`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/LICENSE): MIT License untuk **Aji Pamungkas Tri Nurcahyo (Institut Teknologi Sumatera)**.
  - [`LICENSE.upstream`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/LICENSE.upstream) & [`public/downloads/LICENSE.upstream`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/public/downloads/LICENSE.upstream): Salinan lisensi MIT upstream dipertahankan utuh.
  - [`THIRD_PARTY_NOTICES.md`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/THIRD_PARTY_NOTICES.md) & [`docs/LICENSE_REGISTER.md`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/docs/LICENSE_REGISTER.md): Mencatat atribusi penuh untuk React, Reveal.js, Vite, TypeScript, Shiki, KaTeX, Fontsource, Material Symbols, serta seluruh pustaka Python Track A–E.

---

## 3. Verifikasi Kurikulum 55 Modul, Konfigurasi Subpath & Build

- **Representasi 55 Modul:** **30 Core Chapters** (`Chapter 01`–`30` di 3 Level) + **25 Specialization Modules** (`A01`–`E05` di 5 Tracks), terdokumentasi akurat di [`README.md`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/README.md), [`docs/SPECIALIZATION_CURRICULUM.md`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/docs/SPECIALIZATION_CURRICULUM.md), [`docs/CONTENT_AUDIT.md`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/docs/CONTENT_AUDIT.md), serta terindeks di [`index.html`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/index.html).
- **Konfigurasi Base Path (`vite.config.ts`):** Fungsi [`normalizeBasePath`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/vite.config.ts#L8-L13) memakai `'./'` secara default untuk dev/preview lokal dan menerima `VITE_BASE_PATH='/Python-Learning-Hub/'` untuk produksi GitHub Pages (`npm run build:pages`).
- **GitHub Actions Workflow ([`.github/workflows/deploy.yml`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/.github/workflows/deploy.yml)):**
  - Trigger otomatis pada push ke branch `main` + `workflow_dispatch`.
  - Menggunakan aksi resmi GitHub (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/setup-node@v4`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`) dengan token permission minimal (`contents: read`, `pages: write`, `id-token: write`).
  - Menjalankan `npm ci`, `npm run lint`, dan `npm run build:pages` (`check:outputs`, `check:content`, `check:presentations`, `check:specializations`, `typecheck`, `vite build`, `test:routes`) dengan `VITE_BASE_PATH: /Python-Learning-Hub/`.
- **Aset Statis Build (`dist/`) & Perilaku Browser Refresh:**
  - `npm run build:pages` memverifikasi 209 contoh kode inti, 30 paket download chapter, 25 paket download modul spesialisasi (`A01`–`E05`), `Materi_Pengkom_Pertemuan_9_10_Python.pptx`, `getting-started/main.py`, `.nojekyll`, `LICENSE.upstream`, serta injeksi subpath `/Python-Learning-Hub/assets/` pada `index.html` dan `404.html`.
  - Pengujian Playwright terhadap `dist/` di bawah `/Python-Learning-Hub/` memverifikasi 14 hash routes + reload (`F5`), 6 direct non-hash URL via `404.html` redirect (termasuk `#chapter/10/slides`, `#spec/A01/read`, `#track/iot-telecom`, `#getting-started/vscode-setup`, `#about`, dan `/pertemuan-09/` -> `#chapter/10/slides`), serta 9 static downloads (`HTTP 200`).

---

## 4. Perintah Sinkronisasi & Deployment GitHub Pages

1. **Verifikasi repositori remote:**
   - Remote `origin`: **`https://github.com/aji-nurcahyo/Python-Learning-Hub.git`**

2. **Tinjau status lokal dan push ke GitHub (hanya setelah verifikasi lokal selesai):**
   ```powershell
   cd "D:\Workstation\Repo My Corses\Alpro-python"

   # 1. Pastikan working tree bersih dan berada di branch main
   git status
   git remote -v

   # 2. Push branch main ke GitHub
   git push -u origin main
   ```

3. **Aktifkan GitHub Pages:**
   - Buka `https://github.com/aji-nurcahyo/Python-Learning-Hub/settings/pages`
   - Pada **Build and deployment > Source**, pilih **GitHub Actions**.
   - Tunggu workflow **Deploy to GitHub Pages** di tab **Actions** selesai berstatus hijau (*Succeeded*).

---

## 5. Cara Memperbarui Website Setelah Publikasi

Setiap kali Anda memperbarui materi atau kode aplikasi di `D:\Workstation\Repo My Corses\Alpro-python`:
1. Jika mengubah skrip Python inti, jalankan `npm run gen:outputs`; jika mengubah modul spesialisasi (`A01`–`E05`), jalankan `.\.venv\Scripts\python.exe scripts/run_specialization_examples.py`.
2. Jalankan pemeriksaan lokal sebelum commit:
   ```powershell
   npm run lint
   npm run build:pages
   ```
   *(Atau secara eksplisit: `$env:VITE_BASE_PATH="/Python-Learning-Hub/"; npm run build; Remove-Item Env:VITE_BASE_PATH`)*
3. Commit dan push ke `main`:
   ```powershell
   git add -A
   git commit -m "chore: ringkasan pembaruan materi"
   git push origin main
   ```
   GitHub Actions akan otomatis membangun ulang dan mempublikasikan perubahan ke GitHub Pages.

---

## 6. Checklist Verifikasi Pasca-Deployment (Wajib Dijalankan di URL Publik)

Setelah workflow GitHub Actions selesai, uji langsung di browser pada `https://aji-nurcahyo.github.io/Python-Learning-Hub/`:
- [ ] **Beranda (`/`):** Hero tampil bersih tanpa error konsol/404; statistik menampilkan 30 Core Chapters & 5 Specialization Tracks; Light Mode dan Dark Mode terbaca jelas.
- [ ] **Navigasi Core & Getting Started:** `#/getting-started/vscode-setup`, `#/level/1`, `#/chapter/10`, `#/chapter/10/slides`, `#/chapter/10/read`, dan `#/chapter/10/task` terbuka lengkap dengan contoh kode & output.
- [ ] **Navigasi 5 Specialization Tracks & 25 Modul:** `#/track/data-science` (`A01`–`A05`), `#/track/ai-ml` (`B01`–`B05`), `#/track/web-api` (`C01`–`C05`), `#/track/automation` (`D01`–`D05`), dan `#/track/iot-telecom` (`E01`–`E05`), termasuk `#/spec/A01/slides` dan `#/spec/E05`.
- [ ] **Browser Refresh & Fallback 404:** Tekan `F5` pada rute `#/chapter/10/slides` dan akses langsung `/Python-Learning-Hub/spec/A01/read` serta `/Python-Learning-Hub/about` — halaman tetap termuat tanpa layar 404 kosong.
- [ ] **Unduhan Berkas:** Uji unduh minimal 1 skrip `.py`, 1 notebook `.ipynb`, 1 dataset `.csv`, 1 panduan `tugas.md`, dan `Materi_Pengkom_Pertemuan_9_10_Python.pptx`.

