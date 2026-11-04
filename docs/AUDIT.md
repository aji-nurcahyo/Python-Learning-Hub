# Audit dan keputusan arsitektur

Audit 3 November 2026. Lokasi dikonfirmasi pengguna: `D:\Workstation\Repo My Corses\Alpro-python`.
Alamat awal yang disebutkan tidak tersedia; tidak dibuat folder pengganti tanpa persetujuan.

## Sumber dan cadangan

- Proyek lokal: HTML statis, 16 direktori pertemuan; materi aktif 9 dan 10, dua berkas tugas Markdown, dua program Python, satu PPTX.
- Cadangan penuh sebelum perubahan: `../Alpro-python-backup-20261103-215142`.
- Salinan materi asli: `legacy/`; file contoh dan tugas pada direktori pertemuan juga tetap ada.
- Referensi baca-saja: `../ref-pengkom`, commit `30ce99f8a4a4bed7e9dc7d801a0030da949df3ab`.
- Upstream: https://github.com/informatika-itera/pengkom; https://informatika-itera.github.io/pengkom/.
- Tidak mengubah repository referensi, tidak push, tidak deploy.

## Perbandingan

| Area | Proyek awal | Referensi | Implementasi baru |
|---|---|---|---|
| Runtime | HTML + Reveal 5.2.1 CDN | React 19, TypeScript, Vite, Reveal 6 | React 19, TypeScript, Vite, Reveal 6 lokal |
| Tema | CSS statis dan tema putih | Token MD3, font lokal, preferensi | Permukaan tonal biru/cyan, light/dark/auto, reduced motion |
| Dashboard | Kartu statis | Registry + filter + pencarian | 16 kartu, status jelas, filter tersedia, pencarian |
| Slide | HTML berulang | `src/layouts` dan `DeckShell` | Data materi terpisah + layout cover/konten/kode/latihan/pertanyaan |
| Kode | `<pre>`, output dalam komentar | Shiki, runner Python dan output terverifikasi | Shiki, copy, unduhan, runner CPython dengan check saat build |
| Presentasi | Navigasi dasar | Notes, overview, ratio, theme, print | Kontrol eksplisit, notes plugin, keyboard, rasio, tema, PDF |
| Tugas | marked.js CDN | Layout assignment | Halaman tugas lokal tanpa CDN; rubrik dan instruksi lengkap |

## Pemetaan source referensi yang dipelajari

- `src/theme`: warna, tipografi, bentuk, gerakan, Reveal. Diganti token biru/cyan untuk memenuhi brief; animasi reduced-motion dipertahankan.
- `src/ui`: Shiki tokenizer, KaTeX, CodeBlock/CodeRun/Output, snippet. `highlight.ts` dan `Math.tsx` digunakan kembali dengan atribusi; komponen kode dibuat lebih ringkas dengan tombol salin.
- `src/layouts`: Page, TitleSlide, ContentSlide, CodeSlide, practice dan assignment. Pola komposisi diturunkan ke `SlideContent`, mempertahankan materi lokal, bukan menggantinya dengan kurikulum upstream.
- `src/deck-shell`: pilihan kanvas, preferensi, kontrol, notes dan print. Siklus hidup Reveal dikelola langsung lewat React effect; tidak memakai `@revealjs/react` agar kontrol API eksplisit dan mudah diuji.
- `src/decks`: registry dan pemuatan deck. Proyek ini hanya memuat materi 9–10; 14 pertemuan lain tidak mempunyai konten.
- `src/code`: berkas Python dan output; prinsip output berasal dari eksekusi sungguhan dipertahankan.
- `slides`: entry multi-page Vite. Rute direktori lama dipertahankan sebagai entry HTML di root proyek; `slides/README.md` menjelaskan keputusan tersebut.

## Koreksi contoh tanpa menghilangkan materi

- Contoh modul dua file dipisah menjadi `statistik.py` dan `main.py`; keduanya dapat diunduh.
- Contoh pencarian mengimpor definisi dan data dari `contoh.py`; dependensi disediakan di kartu.
- Fungsi linear search dan selection sort diberi pemanggilan contoh agar output nyata tersedia.
- Output set menggunakan `PYTHONHASHSEED=0` untuk pemeriksaan yang stabil; UI menjelaskan urutan set tidak dijamin.
- Semua 39 judul slide asli tetap disajikan; dua slide cek pemahaman ditambahkan.
- TypeScript 6 dipilih karena parser ESLint yang tersedia belum mendukung TypeScript 7 milik referensi.

## Lisensi

MIT upstream disimpan utuh dalam `LICENSE.upstream`, juga tersedia melalui footer.
`THIRD_PARTY_NOTICES.md` mencatat kode adaptasi dan pustaka. Tidak mengklaim materi asli milik upstream atau memakai logo institusi sebagai identitas baru.
