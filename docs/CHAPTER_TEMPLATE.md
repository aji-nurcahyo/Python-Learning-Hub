# Standar & Templat Konten Modul Chapter
## Python Learning Hub — Standard Chapter Content Template

Dokumen ini adalah cetak biru (*blueprint*) dan templat standar pengembangan konten untuk seluruh 30 chapter di **Python Learning Hub**.

> [!IMPORTANT]
> **Kebijakan Bahasa & Terminologi Teknis Permanen:**  
> Seluruh narasi materi, instruksi latihan, dan panduan tugas wajib mematuhi pedoman baku [TECHNICAL_LANGUAGE_GUIDE.md](file:///d:/Workstation/Repo%20My%20Corses/Alpro-python/docs/TECHNICAL_LANGUAGE_GUIDE.md) dan aturan workspace `.agent/rules/technical-terminology.md`.  
> **Prinsip Dasar:** *"Indonesian for explanations, English for established technical terminology."*  
> Tulis penjelasan dalam Bahasa Indonesia yang natural dan baku, namun pertahankan istilah teknis mapan dalam Bahasa Inggris (misalnya `Development Environment`, `Python Interpreter`, `Code Editor`, `Virtual Environment`, `Python List`, `Python Dictionary`, `Inheritance`, `Encapsulation`, `Polymorphism`, `Exception Handling`, `Error Handling`, `Unit Testing`, `Dependency Management`, dll.) tanpa terjemahan harfiah kaku. Istilah umum seperti *algoritma*, *variabel*, *parameter*, *perulangan*, *percabangan*, dan *pengujian* tetap digunakan secara wajar.

---

## 1. Tata Letak Direktori Standar (*Directory Structure*)

Setiap chapter baru disimpan di `content/<levelCategory>/chapter-<number>/` dengan susunan berkas berikut:

```text
content/<levelCategory>/chapter-<number>/
├── metadata.json           # Sumber data tunggal konfigurasi modul
├── index.md                # Teks modul konsep komprehensif (bahasa Indonesia)
├── slides/
│   └── deck.json           # 15–25 Slide presentasi interaktif Reveal.js
├── code/
│   └── contoh.py           # 5–8 Contoh kode program Python terverifikasi CPython
├── exercises/
│   └── exercise.md         # 3–5 Latihan terarah dengan langkah & petunjuk
└── assignments/
    ├── tugas.md            # Panduan tugas mandiri & tabel rubrik penilaian 100%
    └── tugas.py            # Template starter code yang dapat diunduh mahasiswa
```

---

## 2. Templat Berkas Konfigurasi: `metadata.json`

```json
{
  "id": 1,
  "number": "01",
  "slug": "01-introduction",
  "levelId": 1,
  "levelCategory": "foundations",
  "title": "Introduction to Python",
  "subtitle": "Filosofi, Ekosistem & Eksekusi Program Pertama",
  "description": "Mengenal sejarah Python, Zen of Python, instalasi CPython, Colab/IDE, serta cara kerja interpreter.",
  "competencyFocus": "PCEP 1.1: Dasar eksekusi & lingkungan Python",
  "estimatedHours": 3,
  "difficulty": "Beginner",
  "available": true,
  "prerequisites": [],
  "learningObjectives": [
    "Memahami perbedaan interpreted language dan compiled language",
    "Menjalankan program Python pertama melalui CLI dan script file",
    "Mengenal kaidah penulisan komentar dan indentation standar PEP 8"
  ],
  "tags": [
    "Interpreter",
    "CPython",
    "PEP 8",
    "Syntax"
  ],
  "resources": {
    "hasSlides": true,
    "slidesDeck": "slides/deck.json",
    "starterCode": "code/contoh.py",
    "assignmentGuide": "assignments/tugas.md",
    "pptxDownload": null
  },
  "codeExample": {
    "title": "Program Pertama: Eksekusi Terminal & Greeting",
    "code": "# Program Pertama Python Learning Hub\ndef sapa_pengguna(nama: str) -> str:\n    return f\"Halo {nama}, selamat datang di Python Learning Hub!\"\n\nif __name__ == \"__main__\":\n    pesan = sapa_pengguna(\"Rekayasa Telekomunikasi\")\n    print(pesan)",
    "outputKey": "ch01-01",
    "explanation": "Fungsi sapa_pengguna menerima parameter string dan mengembalikan formatted f-string. Blok __name__ memastikan kode uji hanya berjalan saat dieksekusi langsung."
  },
  "exercise": {
    "title": "Latihan Terarah: Format Identitas Sistem",
    "instructions": [
      "Deklarasikan variabel nama_perangkat bertipe string dan id_node bertipe integer.",
      "Gunakan formatted string literal (f-string) untuk mencetak string gabungan.",
      "Cetak keluaran ke layar terminal dan periksa kesesuaian tipe data."
    ],
    "tips": "Gunakan kurung kurawal {variabel} di dalam f\"...\" untuk menyisipkan nilai.",
    "time": "15 menit"
  },
  "quiz": {
    "question": "Manakah pernyataan yang BENAR mengenai cara kerja interpreter CPython?",
    "options": [
      "CPython menerjemahkan kode sumber langsung ke file binary .exe",
      "CPython mengompilasi kode sumber ke bytecode (.pyc) lalu menjalankannya di Python Virtual Machine (PVM)",
      "CPython tidak melakukan kompilasi apa pun dan membaca teks baris per baris secara mentah saat runtime",
      "CPython membutuhkan compiler eksternal seperti GCC sebelum kode dapat dijalankan"
    ],
    "correctIndex": 1,
    "explanation": "CPython mengompilasi kode sumber (.py) menjadi bytecode internal (disimpan di folder __pycache__ sebagai .pyc) yang kemudian dieksekusi oleh Python Virtual Machine (PVM).",
    "hint": "Ingat keberadaan direktori __pycache__ saat Anda menjalankan modul Python."
  },
  "assignment": {
    "title": "Tugas Praktik 01: Verifikasi Environment & Logger Terminal",
    "description": "Rancang skrip Python mandiri yang mengidentifikasi versi sistem operasi, versi interpreter Python, dan mencetak laporan inisialisasi node telekomunikasi.",
    "instructions": [
      "Gunakan modul bawaan sys dan platform untuk membaca metadata interpreter.",
      "Cetak status kesiapan node telekomunikasi dalam format tabel bersih.",
      "Terapkan konvensi docstring PEP 257 dan blok proteksi __name__ == '__main__':."
    ],
    "rubric": [
      { "criteria": "Kebenaran Logika & Modul sys/platform", "weight": 40, "description": "Mengimpor modul bawaan secara benar dan membaca versi sistem tanpa error." },
      { "criteria": "Format Keluaran & Kerapian Tampilan", "weight": 30, "description": "Teks tersusun rapi menggunakan f-string dan pemisah visual yang proporsional." },
      { "criteria": "Kepatuhan Standar PEP 8 & Docstring", "weight": 30, "description": "Memiliki docstring lengkap dan penamaan variabel sesuai kaidah snake_case." }
    ],
    "starterCode": "# Template Starter Code - Chapter 01\nimport sys\nimport platform\n\ndef cetak_info_sistem():\n    \"\"\"Mencetak informasi interpreter Python dan sistem operasi.\"\"\"\n    print(f\"Versi Python: {sys.version}\")\n    print(f\"Platform: {platform.system()} {platform.release()}\")\n\nif __name__ == '__main__':\n    cetak_info_sistem()\n",
    "starterFilename": "tugas_01.py",
    "downloadMdUrl": "downloads/chapter-01/tugas.md",
    "downloadPyUrl": "downloads/chapter-01/contoh.py"
  }
}
```

---

## 3. Templat Teks Modul Konsep: `index.md`

```markdown
# Chapter 01 — Introduction to Python
> **Filosofi, Ekosistem & Eksekusi Program Pertama**  
*Level 1 · FOUNDATIONS · Beginner · 3 Jam Pembelajaran*

---

## 1. Pendahuluan & Filosofi Bahasa

Python adalah bahasa pemrograman aras tinggi (*high-level*), berorientasi objek, dinamis, dan terinterpretasi yang diciptakan oleh **Guido van Rossum** pada tahun 1991. Python dirancang dengan filosofi yang menekankan **keterbacaan kode** (*code readability*) melalui sintaks yang bersih dan penggunaan indentasi blok yang konsisten.

Filosofi inti Python tertuang dalam **Zen of Python (PEP 20)**:
- *Beautiful is better than ugly.*
- *Explicit is better than implicit.*
- *Simple is better than complex.*
- *Readability counts.*

---

## 2. Cara Kerja Interpreter CPython

Berbeda dengan bahasa terkompilasi murni seperti C/C++ yang langsung menghasilkan instruksi biner mesin (*machine code*), interpreter standar Python (**CPython**) bekerja melalui proses hibrida dua tahap:

```text
[Kode Sumber: main.py] ──► [Compiler CPython] ──► [Bytecode: __pycache__/*.pyc] ──► [Python Virtual Machine (PVM)] ──► [Sistem Operasi]
```

1. **Tahap Kompilasi Bytecode:** CPython mengompilasi kode sumber tingkat tinggi menjadi representasi perantara bernama *bytecode*.
2. **Tahap Eksekusi Virtual Machine:** PVM mengeksekusi urutan bytecode tersebut menjadi panggilan sistem operasi.

---

## 3. Kode Contoh Terverifikasi

```python
# File: contoh.py
"""
Contoh Program Pertama - Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo
"""

def hitung_delay_transmisi(ukuran_bit: float, bandwidth_bps: float) -> float:
    """Menghitung delay transmisi data paket telekomunikasi."""
    if bandwidth_bps <= 0:
        raise ValueError("Bandwidth harus lebih besar dari 0 bps.")
    return ukuran_bit / bandwidth_bps

if __name__ == "__main__":
    paket_bit = 8_000_000.0   # 1 Megabyte = 8 Megabit
    link_speed = 100_000_000.0 # 100 Mbps
    delay_detik = hitung_delay_transmisi(paket_bit, link_speed)
    print(f"Delay Transmisi: {delay_detik * 1000:.2f} ms")
```

**Hasil Keluaran Terminal (CPython 3.12):**
```text
Delay Transmisi: 80.00 ms
```

---

## 4. Latihan Pemahaman Mandiri

1. **Latihan 1:** Modifikasi fungsi `hitung_delay_transmisi` agar menerima parameter tambahan `efisiensi_link` bertipe float dengan nilai default `0.90` (90%).
2. **Latihan 2:** Buat fungsi konversi ukuran data dari Megabyte (MB) ke bit.

---

## 5. Referensi & Sumber Rujukan Terbuka

1. **Python Software Foundation.** *The Python Tutorial: Whetting Your Appetite & Using the Interpreter*. https://docs.python.org/3/tutorial/ — PSF License.
2. **Downey, Allen B.** *Think Python: The Way of the Program (Chapter 1)*. Green Tea Press. https://allendowney.github.io/ThinkPython/ — CC BY-NC 4.0.
3. **Yetayeh, Asabeneh S.** *30 Days of Python: Day 1 - Introduction*. https://github.com/Asabeneh/30-Days-Of-Python — MIT License.
```

---

## 4. Templat Slide Presentasi Reveal.js: `slides/deck.json`

### Standar Identitas Resmi Slide (*Official Presentation Identity*)
Setiap slide presentasi wajib mengikuti kaidah identitas resmi platform:
- **Nama Platform:** Python Learning Hub
- **Tagline:** Learn Python, One Chapter at a Time
- **Pengembang / Creator:** Aji Pamungkas Tri Nurcahyo
- **Institusi Resmi:** Institut Teknologi Sumatera
- **Aturan Afiliasi Ketat:** **JANGAN** menampilkan nama Program Studi (Teknik Telekomunikasi) atau Fakultas (Teknologi Industri) sebagai afiliasi creator pada slide cover, footer, metadata, maupun speaker notes. Gunakan HANYA **Aji Pamungkas Tri Nurcahyo** dan **Institut Teknologi Sumatera**.
- **Standar Rasio Slide:** 16:9 (lebar 1280px × tinggi 720px) dengan layout fleksibel dan penskalaan responsif bebas *overflow* atau *footer collision*.

### Struktur Cover Slide Standar:
Komponen cover slide dirender secara terpusat oleh `SlideContent.tsx`:
```text
PYTHON LEARNING HUB / CHAPTER XX
[Judul Chapter Resmi]
[Deskripsi / Lead Singkat]
Aji Pamungkas Tri Nurcahyo
Institut Teknologi Sumatera
```

### Format Berkas JSON:
Setiap slide deck memuat antara 15 s.d. 25 objek slide dengan format terstruktur:

```json
[
  {
    "title": "Introduction to Python",
    "body": "<p class=\"lead\">Filosofi, Ekosistem & Eksekusi Program Pertama</p>",
    "kind": "cover",
    "notes": "Selamat datang di Chapter 01. Fokus sesi ini adalah memahami filosofi Python dan alur kerja interpreter."
  },
  {
    "title": "Capaian Pembelajaran Modul",
    "body": "<ul><li>Memahami perbedaan interpreted language dan compiled language.</li><li>Mampu menjalankan program Python melalui REPL interaktif dan berkas skrip.</li><li>Menerapkan aturan indentasi dan komentar standar PEP 8.</li></ul>",
    "kind": "content",
    "notes": "Jelaskan target kompetensi yang selaras dengan sertifikasi PCEP."
  },
  {
    "title": "Arsitektur Interpreter CPython",
    "body": "<p>CPython menerjemahkan kode sumber menjadi bytecode perantara (.pyc) sebelum dieksekusi oleh Python Virtual Machine (PVM).</p><div class=\"callout-box\">Bytecode bersifat portabel lintas platform yang memiliki PVM yang kompatibel.</div>",
    "kind": "content",
    "notes": "Bahas analogi penerjemah naskah drama sebelum dipentaskan oleh aktor PVM."
  },
  {
    "title": "Contoh Kode: Eksekusi Fungsi Sapaan",
    "example": "ch01-01",
    "body": "<p>Fungsi modular dengan type hints dan blok proteksi eksekusi langsung.</p>",
    "kind": "code",
    "notes": "Ajak peserta memperhatikan blok if __name__ == '__main__'."
  },
  {
    "title": "Cek Pemahaman: Cara Kerja Interpreter",
    "question": "Mengapa folder __pycache__ muncul saat kita menjalankan modul Python?",
    "answer": "Folder tersebut menyimpan bytecode terkompilasi (.pyc) agar eksekusi berikutnya dapat berjalan lebih cepat tanpa kompilasi ulang dari awal.",
    "kind": "quiz",
    "notes": "Beri jeda 30 detik agar peserta menjawab sebelum membuka jawaban."
  },
  {
    "title": "Refleksi & Persiapan Chapter Berikutnya",
    "body": "<p>Pada Chapter 02 kita akan membedah variabel sebagai label referensi memori dan tipe-tipe data skalar dasar Python.</p>",
    "kind": "content",
    "notes": "Tutup sesi dengan mengingatkan pengerjaan tugas mandiri."
  }
]
```

---

## 5. Prosedur Uji Mutu Sebelum Publikasi (*Pre-Release Checklist*)

Jalankan perintah pengujian bertingkat sebelum chapter diubah ke `"available": true`:

```powershell
# 1. Jalankan skrip contoh dan rekam output CPython
python scripts/run_examples.py

# 2. Verifikasi kesesuaian output dengan runner
npm run check:outputs

# 3. Validasi keberadaan fisik seluruh slide deck, file python, dan tugas
npm run check:resources

# 4. Validasi integritas struktur 30 modul dan metadata
npm run check:content

# 5. Audit otomatis kualitas presentasi, branding, dan layout geometri DOM (Chrome/Edge headless)
npm run check:presentations

# 6. Typecheck TypeScript (0 error)
npm run typecheck

# 7. Linting ESLint (0 warning/error)
npm run lint

# 8. Build bundle produksi dan uji rute statis
npm run build
```

