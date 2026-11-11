# Panduan Persiapan & Publikasi GitHub Pages
## Python Learning Hub — GitHub Repository & GitHub Pages Deployment Guide

> **Target Repositori GitHub:** `https://github.com/aji-nurcahyo/Python-Learning-Hub`  
> **Target URL Produksi:** `https://aji-nurcahyo.github.io/Python-Learning-Hub/`  
> **Workflow Otomatis:** `.github/workflows/deploy.yml` (GitHub Actions Official Pages Actions)  
> **Status Kesiapan Lokal:** Terverifikasi (Siap dipublikasikan dengan konfigurasi `/Python-Learning-Hub/` permanen)

---

## 1. Ikhtisar Konfigurasi Deployment

**Python Learning Hub** adalah aplikasi web statis (*Single-Page Application* / SPA) berbasis React, TypeScript, Vite, dan Reveal.js tanpa kebutuhan backend server. Platform ini dirancang untuk di-hosting secara gratis melalui **GitHub Pages** di bawah subpath proyek `/Python-Learning-Hub/`.

### Komponen Kunci Kesiapan Hosting Statis:
1. **Vite Base Path (`vite.config.ts`):**
   - Secara default untuk pengembangan lokal, `VITE_BASE_PATH` bernilai `'./'`.
   - Untuk produksi GitHub Pages di bawah subpath `https://aji-nurcahyo.github.io/Python-Learning-Hub/`, script `npm run build:pages` dan workflow CI menetapkan environment variable:
     ```text
     VITE_BASE_PATH=/Python-Learning-Hub/
     ```
   - Fungsi `normalizeBasePath()` di [`vite.config.ts`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/vite.config.ts) memastikan akhiran garis miring `/` selalu konsisten baik untuk build lokal (`./`) maupun subpath produksi (`/Python-Learning-Hub/`).
2. **Resolusi Aset & Resource (`getAssetUrl`):**
   - Seluruh berkas unduhan (`.py`, `.md`, `.pptx`, dan `LICENSE.upstream`) disimpan di `public/downloads/` sehingga disalin utuh ke `dist/downloads/`.
   - Seluruh tautan di komponen UI menggunakan helper [`getAssetUrl()`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/src/curriculum/resources.ts) dan `import.meta.env.BASE_URL` agar jalur aset menyesuaikan otomatis dengan root maupun subpath `/Python-Learning-Hub/`.
3. **Penanda `.nojekyll` (`public/.nojekyll`):**
   - Disertakan otomatis di folder akar hasil build `dist/` untuk menonaktifkan pemrosesan Jekyll di GitHub Pages agar tidak ada folder atau berkas aset yang diabaikan.

---

## 2. Dukungan Nested Routes & Browser Refresh (`404.html`)

Karena GitHub Pages merupakan server berkas statis murni, permintaan URL langsung pada rute dalam (*nested route*) atau penyegaran halaman (*browser refresh*) ditangani dengan kombinasi dua mekanisme:

1. **Hash-Based SPA Routing (`src/main.tsx`):**
   - Navigasi utama aplikasi menggunakan hash URL seperti `#getting-started`, `#level/1`, `#chapter/15`, `#chapter/15/slides`, `#chapter/15/read`, `#chapter/15/task`, `#spec/A01`, dan `#about`.
   - Saat pengguna menekan tombol *Refresh* (`F5`) di browser, server GitHub Pages hanya meminta `/Python-Learning-Hub/` dan langsung menyajikan `index.html`, lalu React merender ulang halaman sesuai hash aktif.
2. **Fallback `404.html` SPA Redirect (`404.html`):**
   - Jika pengguna mengetik URL path langsung tanpa `#` (misalnya `/Python-Learning-Hub/chapter/05/slides` atau `/Python-Learning-Hub/spec/A01/read`), GitHub Pages menyajikan `dist/404.html`.
   - Skrip pada [`404.html`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/404.html) mendeteksi prefiks repositori `Python-Learning-Hub` (beserta varian huruf kecilnya), memetakan path legacy (`pertemuan-XX`), mempertahankan query parameter (seperti `?print-pdf`), lalu mengarahkan secara instan ke `/Python-Learning-Hub/#<rute>` sebelum aplikasi React dimuat.
   - `extractRouteFromPathname()` pada [`src/main.tsx`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/src/main.tsx) juga menyediakan fallback pembacaan `location.pathname` (dengan menghapus prefiks `/Python-Learning-Hub/` secara case-insensitive) sehingga pengujian rute langsung pada `vite dev` dan `vite preview` tetap berfungsi mulus.

---

## 3. Konfigurasi GitHub Actions (`.github/workflows/deploy.yml`)

Otomasi deployment menggunakan aksi resmi GitHub (*official maintained GitHub Actions*):

| Tahap Pipeline | Action Resmi | Fungsi Utama |
| :--- | :--- | :--- |
| **Checkout** | `actions/checkout@v4` | Mengambil kode sumber branch `main`. |
| **Runtime Python** | `actions/setup-python@v5` | Menyiapkan CPython 3.12 untuk menjalankan verifikasi `check:outputs`. |
| **Runtime Node.js** | `actions/setup-node@v4` | Menyiapkan Node.js 22 dengan cache `npm`. |
| **Pages Config** | `actions/configure-pages@v5` | Menyiapkan metadata lingkungan GitHub Pages. |
| **Artifact Upload** | `actions/upload-pages-artifact@v3` | Mengemas direktori `./dist` hasil build produksi. |
| **Pages Deploy** | `actions/deploy-pages@v4` | Menerbitkan artifact `./dist` ke layanan hosting GitHub Pages. |

Sebelum artifact diunggah, job `build` menjalankan pemeriksaan wajib:
- `npm ci`
- `npm run lint`
- `npm run build:pages` (mencakup `check:outputs`, `check:content`, `check:presentations`, `check:specializations`, `typecheck`, `vite build`, dan `test:routes`) dengan `VITE_BASE_PATH: /Python-Learning-Hub/`.

---

## 4. Konfigurasi Remote & Aktivasi GitHub Pages

### Langkah 1: Verifikasi Remote GitHub
Repositori terhubung ke:
```text
https://github.com/aji-nurcahyo/Python-Learning-Hub.git
```

Untuk memeriksa status dan remote lokal di `D:\Workstation\Repo My Corses\Alpro-python`:
```powershell
git status
git remote -v
```

### Langkah 2: Aktivasi GitHub Pages di Pengaturan Repositori
1. Buka halaman repositori `https://github.com/aji-nurcahyo/Python-Learning-Hub`.
2. Masuk ke tab **Settings** -> di sidebar kiri bagian *Code and automation*, klik **Pages**.
3. Pada bagian **Build and deployment**, ubah opsi **Source** dari *Deploy from a branch* menjadi:
   - **GitHub Actions**
4. Buka tab **Actions** di repositori Anda untuk memantau proses workflow **Deploy to GitHub Pages**.
5. Setelah job `build` dan `deploy` berstatus hijau (*Succeeded*), situs Anda akan aktif pada alamat:
   ```text
   https://aji-nurcahyo.github.io/Python-Learning-Hub/
   ```

---

## 5. Pengujian Build Produksi Secara Lokal (*Local Testing*)

Sebelum melakukan push ke GitHub, Anda dapat membangun dan mensimulasikan hasil build GitHub Pages `/Python-Learning-Hub/` secara konsisten:

### Menggunakan Cross-Platform Script (Windows, Linux, macOS):
```bash
npm run build:pages
npx vite preview --host 127.0.0.1 --port 8932
```

### Menggunakan PowerShell (Windows):
```powershell
$env:VITE_BASE_PATH="/Python-Learning-Hub/"
npm run build
npx vite preview --host 127.0.0.1 --port 8932
```

### Menggunakan Linux / GitHub Actions Shell:
```bash
VITE_BASE_PATH="/Python-Learning-Hub/" npm run build
npx vite preview --host 127.0.0.1 --port 8932
```

Kemudian uji di browser:
- `http://127.0.0.1:8932/Python-Learning-Hub/`
- `http://127.0.0.1:8932/Python-Learning-Hub/#getting-started`
- `http://127.0.0.1:8932/Python-Learning-Hub/#chapter/05/slides`
- `http://127.0.0.1:8932/Python-Learning-Hub/#spec/A01`
- `http://127.0.0.1:8932/Python-Learning-Hub/#chapter/30/task`

Untuk mengembalikan build ke mode relatif default (`'./'`):
```powershell
Remove-Item Env:VITE_BASE_PATH -ErrorAction SilentlyContinue
npm run build
```

---

## 6. Alur Pembaruan di Masa Depan (*Future Updates*)

Setiap kali Anda menambahkan materi atau memperbaiki bug di repositori lokal:

1. Lakukan perubahan pada kode atau konten markdown/JSON.
2. Jalankan rangkaian verifikasi lokal:
   ```bash
   npm run lint
   npm run build:pages
   ```
3. Commit dan push perubahan ke branch `main`:
   ```bash
   git add .
   git commit -m "docs: deskripsi singkat pembaruan"
   git push origin main
   ```
4. GitHub Actions akan otomatis mendeteksi push ke `main`, menjalankan ulang seluruh validasi CPython/konten/TypeScript/build, dan memperbarui halaman live secara otomatis dalam ~1–2 menit.

---

## 7. Daftar Periksa Audit Keamanan & Lisensi

- **`.gitignore`:** Mengabaikan `node_modules/`, `dist/`, `.env`, `.env.*`, `.venv/`, `__pycache__/`, `*.db`, `*.sqlite`, `*.pem`, `*.key`, dan berkas log/sementara.
- **Keamanan Konten Publik:** Seluruh materi di `public/` dan `content/` adalah sumber terbuka (*Open Educational Resource*). Tidak terdapat kunci jawaban tertutup instruktur, dataset rahasia, maupun token API produksi.
- **Atribusi & Hak Cipta Upstream:** [`LICENSE.upstream`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/LICENSE.upstream), [`public/downloads/LICENSE.upstream`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/public/downloads/LICENSE.upstream), dan [`THIRD_PARTY_NOTICES.md`](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/THIRD_PARTY_NOTICES.md) tetap dipertahankan utuh sesuai lisensi MIT upstream.

