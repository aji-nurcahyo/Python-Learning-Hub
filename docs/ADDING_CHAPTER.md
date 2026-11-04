# Panduan Penambahan & Pemeliharaan Modul Chapter (Python Learning Hub)

Dokumen ini menjelaskan arsitektur konten modular di **Python Learning Hub** dan tata cara menambahkan materi pembelajaran baru atau memperbarui materi yang sudah ada tanpa perlu mengubah kode logika React inti.

---

## 1. Arsitektur Konten Modular (`content/`)

Seluruh materi pembelajaran diatur secara hierarkis dan mandiri di dalam folder `content/`:

```text
content/
├── foundations/                     # Level 1: Chapter 01 – 12
│   ├── chapter-01/
│   │   ├── metadata.json           # Sumber data tunggal informasi chapter
│   │   ├── index.md                # Teks modul lengkap / ringkasan bacaan
│   │   ├── slides/
│   │   │   └── deck.json           # Slide presentasi interaktif Reveal.js
│   │   ├── code/
│   │   │   └── contoh.py           # Program Python terverifikasi
│   │   ├── exercises/              # Panduan latihan terarah & kuis konsep
│   │   ├── assignments/            # Spesifikasi tugas praktik mandiri
│   │   │   └── tugas.md
│   │   └── assets/                 # Gambar atau diagram khusus chapter
│   ├── ...
│   └── chapter-12/
├── intermediate/                    # Level 2: Chapter 13 – 22
│   ├── chapter-13/
│   └── ...
├── professional/                    # Level 3: Chapter 23 – 30
│   ├── chapter-23/
│   └── ...
└── specializations/                 # 5 Jalur Spesialisasi Industri
    ├── track-data-science/
    ├── track-ai-ml/
    ├── track-web-api/
    ├── track-automation/
    └── track-iot-telecom/
```

Setiap chapter berdiri sendiri (*self-contained*), sehingga pemeliharaan, penambahan contoh kode, kuis, atau slide dapat dilakukan secara independen.

---

## 2. Struktur `metadata.json` (Single Source of Truth)

Setiap chapter memiliki `metadata.json` yang mendefinisikan informasi modul:

```json
{
  "id": "11",
  "slug": "chapter-11",
  "level": 1,
  "levelName": "Python Foundations",
  "title": "Modules, Packages, and Docstrings",
  "subtitle": "Modularitas Kode & Dokumentasi Standar PEP 257",
  "difficulty": "Beginner",
  "estimatedHours": 4,
  "competencyFocus": "Struktur modular program Python",
  "available": true,
  "summary": "Memahami import modul, standard library, serta penulisan docstring.",
  "learningObjectives": [
    "Memahami konsep modularitas dan pemisahan tanggung jawab kode",
    "Mengimpor modul dari Python Standard Library (math, random, sys)",
    "Menulis modul kustom dan memahami eksekusi kondisional __name__ == '__main__'"
  ],
  "prerequisites": [
    "Fungsi dan Parameter (Chapter 10)",
    "Struktur Data Python (Chapter 08 & 09)"
  ],
  "resources": [
    {
      "name": "Script Contoh Python",
      "format": "PY",
      "url": "downloads/chapter-11/contoh.py",
      "description": "Contoh pembuatan modul statistik dan program pemanggil"
    },
    {
      "name": "Panduan Tugas Mandiri",
      "format": "MD",
      "url": "downloads/chapter-11/tugas.md",
      "description": "Spesifikasi tugas perancangan modul konversi unit"
    }
  ],
  "exercises": [
    {
      "id": "ex-11-01",
      "title": "Latihan 1: Ekstraksi Modul Geometri",
      "description": "Pisahkan fungsi keliling dan luas lingkaran ke dalam modul geometri terpisah.",
      "steps": [
        "Buat file geometri.py dengan konstanta PI dan fungsi luas_lingkaran",
        "Buat file main.py yang mengimpor modul geometri",
        "Jalankan main.py dan verifikasi output"
      ],
      "tips": "Gunakan blok if __name__ == '__main__': di geometri.py untuk pengujian lokal."
    }
  ],
  "quizzes": [
    {
      "id": "q-11-01",
      "question": "Kapan variabel khusus __name__ bernilai '__main__'?",
      "options": [
        "Selalu bernilai '__main__' di semua file Python",
        "Hanya ketika file tersebut dieksekusi secara langsung oleh interpreter",
        "Ketika file tersebut diimpor oleh file lain",
        "Hanya ketika file berada di folder root"
      ],
      "answerIndex": 1,
      "explanation": "Interpreter Python menyetel __name__ = '__main__' hanya untuk skrip entrypoint yang dieksekusi langsung."
    }
  ],
  "assignments": [
    {
      "id": "asg-11-01",
      "title": "Tugas Mandiri: Perancangan Modul Metrologi & Konversi",
      "description": "Rancang modul kustom untuk konversi satuan telekomunikasi (dBm ke Watt, frekuensi ke panjang gelombang).",
      "starterCode": "# Modul telemetri.py\nimport math\n\ndef dbm_to_watt(dbm: float) -> float:\n    \"\"\"Konversi daya dari satuan dBm ke Watt.\"\"\"\n    return (10 ** (dbm / 10)) / 1000\n",
      "rubric": [
        {"criteria": "Modularitas & pemisahan file", "weight": "30%", "target": "Modul mandiri dan import bersih"},
        {"criteria": "Docstrings & PEP 257", "weight": "30%", "target": "Setiap fungsi memiliki docstring lengkap"},
        {"criteria": "Pengujian & __name__ block", "weight": "40%", "target": "Dilengkapi uji coba mandiri"}
      ]
    }
  ]
}
```

---

## 3. Menambahkan Komponen Materi

### A. Slide Presentasi (`slides/deck.json`)
Buat file `slides/deck.json` dengan format Reveal.js JSON:
```json
{
  "title": "Modules, Packages, and Docstrings",
  "chapterId": "11",
  "slides": [
    {
      "kind": "cover",
      "title": "Modules, Packages, and Docstrings",
      "body": "<p class=\"subtitle\">Chapter 11 — Python Foundations</p>",
      "notes": "Selamat datang di Chapter 11. Fokus sesi ini adalah modularitas kode."
    },
    {
      "kind": "content",
      "title": "Mengapa Membutuhkan Modul?",
      "body": "<ul><li>Mencegah kode duplikat (DRY principle).</li><li>Memisahkan tanggung jawab (Separation of Concerns).</li></ul>",
      "notes": "Jelaskan analogi perkakas kerja dalam bengkel."
    }
  ]
}
```
*Catatan:* Nilai `kind` yang didukung: `"cover"`, `"content"`, `"exercise"`, `"quiz"`.

### B. Kode Contoh Python (`code/contoh.py`)
Simpan file contoh program Python yang dapat dijalankan secara nyata:
```python
"""
Chapter 11 - Contoh Modul dan Docstring
Pengembang: Aji Pamungkas Tri Nurcahyo
"""

def hitung_snr(daya_sinyal: float, daya_noise: float) -> float:
    """Menghitung Signal-to-Noise Ratio (SNR) dalam desibel (dB)."""
    if daya_noise <= 0:
        raise ValueError("Daya noise harus lebih besar dari 0.")
    import math
    return 10 * math.log10(daya_sinyal / daya_noise)

if __name__ == "__main__":
    snr = hitung_snr(100.0, 1.0)
    print(f"SNR: {snr:.2f} dB")
```

### C. Dokumen Tugas Mandiri (`assignments/tugas.md`)
Buat file Markdown yang berisi panduan teknis, langkah pengerjaan, dan ketentuan pengumpulan tugas mandiri.

---

## 4. Mengaktifkan Chapter (`"available": true`)

Ketika materi chapter telah siap dipublikasikan:
1. Buka `content/<level>/chapter-XX/metadata.json`.
2. Ubah nilai `"available": false` menjadi `"available": true`.
3. Simpan perubahan.
4. Buka `src/curriculum/index.ts`, ubah properti `available: true` pada chapter yang sesuai.

Sistem secara otomatis akan:
- Menghilangkan badge status *"Segera Hadir"* pada daftar chapter di Beranda.
- Menampilkan tab navigasi lengkap: **Materi & Kode**, **Presentasi Slide**, **Latihan Terarah**, dan **Tugas Mandiri**.
- Menghubungkan chapter ke rute `#/chapter/:id`, `#/chapter/:id/slides`, `#/chapter/:id/read`, dan `#/chapter/:id/task`.

---

## 5. Menyiapkan Berkas Unduhan (`public/downloads/`)

Agar pembaca dapat mengunduh berkas materi secara langsung:
1. Buat folder `public/downloads/chapter-XX/`.
2. Salin file `contoh.py`, `tugas.md`, atau slide PPTX pendukung ke dalam folder tersebut.
3. Pastikan URL di `metadata.json` mengarah ke path relatif `downloads/chapter-XX/<nama-berkas>`.

---

## 6. Prosedur Verifikasi & Uji Kualitas (QA)

Sebelum melakukan commit atau push ke GitHub, jalankan rangkaian pengujian otomatis berikut:

```powershell
# 1. Validasi struktur seluruh 30 paket chapter dan 5 jalur spesialisasi
npm run check:content

# 2. Validasi eksekusi dan konsistensi output CPython
npm run check:outputs

# 3. Validasi tipe statis TypeScript (0 error)
npm run typecheck

# 4. Validasi standar kode ESLint
npm run lint

# 5. Build produksi lengkap Vite dan verifikasi rute statis
npm run build
```

Jika seluruh perintah di atas mengembalikan status `PASSED` (kode keluar 0), materi baru telah terintegrasi sempurna dan siap dipublikasikan.
