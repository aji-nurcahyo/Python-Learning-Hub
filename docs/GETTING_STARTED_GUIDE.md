# Panduan Modul Getting Started (Getting Started Guide)
## Python Learning Hub — Python Development Environment Setup Documentation

> **Versi Dokumen:** 1.0.0  
> **Tanggal Efektif:** 4 November 2026  
> **Bagian Kurikulum:** Onboarding & Development Environment Setup (Independen di luar 30 Chapter)  
> **Target Pengguna:** Mahasiswa, pemula, instruktur lab, dan kurikulum developer

---

## 1. Ikhtisar Bagian Getting Started

Bagian **"Getting Started with Python"** dirancang sebagai modul fondasi onboarding yang berdiri sendiri sebelum peserta didik memulai **Level 1: Python Foundations (Chapter 01–12)**. 

Modul ini memandu penyiapan *Python Development Environment* lokal dan cloud secara menyeluruh, mandiri, dan bebas kendala pada sistem operasi Windows 10/11, Ubuntu/Linux, dan macOS.

### Karakteristik Desain:
- **Independen dari 30 Chapter:** Tidak menggunakan penomoran "Chapter 00" atau mengubah nomor bab yang sudah ada.
- **Rute Web Khusus:** Diakses melalui `#getting-started` atau `#getting-started/[id_tutorial]` dan tombol navigasi utama di header website.
- **Dukungan Multi-Platform Terpadu:** Setiap perintah terminal dan instalasi dipisahkan secara interaktif untuk Windows (PowerShell/CMD), Linux (Ubuntu/Debian), dan macOS.
- **Verifikasi Mandiri:** Dilengkapi dengan daftar periksa (*checklist*) dan skrip uji coba yang dapat dieksekusi secara nyata (`content/getting-started/code/main.py`).

---

## 2. Struktur 8 Modul Tutorial

Bagian Getting Started terdiri atas 8 modul tutorial terstruktur:

| No | ID Tutorial | Judul Resmi | Estimasi Baca | Fokus Utama |
| :---: | :--- | :--- | :---: | :--- |
| **01** | `development-tools` | **Understanding Python Development Tools** | 12 menit | Peta ekosistem, Python Interpreter vs. Code Editor/IDE, perbandingan skrip `.py` vs. `.ipynb`. |
| **02** | `installing-python` | **Installing Python** | 15 menit | Unduhan resmi python.org, aktivasi PATH Windows, instalasi apt Linux & pkg/brew macOS, Python Launcher (`py`). |
| **03** | `vscode-setup` | **Installing & Configuring VS Code** | 15 menit | Ekstensi Python Microsoft, konsep Open Folder workspace, pemilih interpreter, Integrated Terminal, debugging F5. |
| **04** | `jupyter-setup` | **Jupyter Notebook & JupyterLab** | 15 menit | Struktur JSON `.ipynb`, instalasi pip, peluncuran server lokal, eksekusi sel kode & Markdown, manajemen kernel. |
| **05** | `virtual-environment` | **Virtual Environment & Package Management** | 18 menit | Isolasi paket via `venv`, aktivasi lintas OS, solusi aman bypass execution policy PowerShell, `pip`, `requirements.txt`. |
| **06** | `google-colab` | **Google Colab** | 12 menit | Komputasi cloud tanpa setup lokal, eksekusi `!pip`, integrasi `drive.mount`, pemahaman batas idle & kuota GPU T4. |
| **07** | `running-projects` | **Running Python Projects** | 15 menit | Navigasi direktori (`cd`, `ls`, `pwd`), eksekusi skrip `main.py`, idiom `if __name__ == "__main__":`, cara membaca traceback error. |
| **08** | `troubleshooting` | **Troubleshooting & Environment Verification** | 20 menit | Solusi aman perintah unrecognized, konflik port Jupyter, ModuleNotFoundError, SSL certs macOS, alur verifikasi 8 langkah. |

---

## 3. Struktur Berkas & Arsitektur Modul

Materi Getting Started dikelola secara modular pada direktori:

```text
Alpro-python/
├── content/
│   └── getting-started/
│       ├── 01-development-tools.md
│       ├── 02-installing-python.md
│       ├── 03-vscode-setup.md
│       ├── 04-jupyter-setup.md
│       ├── 05-virtual-environment.md
│       ├── 06-google-colab.md
│       ├── 07-running-projects.md
│       ├── 08-troubleshooting.md
│       └── code/
│           └── main.py                     <-- Skrip verifikasi CPython
├── public/
│   └── downloads/
│       └── getting-started/
│           └── main.py                     <-- Berkas unduhan publik
└── src/
    ├── curriculum/
    │   └── getting-started.ts              <-- Definisi data TypeScript terstruktur
    └── pages/
        └── GettingStartedPage.tsx          <-- Komponen antarmuka peramban interaktif
```

---

## 4. Cara Menambah atau Memperbarui Tutorial Getting Started

Untuk memperbarui panduan instalasi di masa mendatang (misalnya saat rilis versi baru Python LTS):

1. **Perbarui Berkas Markdown:**  
   Buka berkas terkait di `content/getting-started/0X-nama-tutorial.md`. Gunakan Bahasa Indonesia formal untuk penjelasan dan pertahankan istilah teknis baku dalam Bahasa Inggris sesuai `docs/TECHNICAL_LANGUAGE_GUIDE.md`.
2. **Sinkronkan Data TypeScript:**  
   Buka `src/curriculum/getting-started.ts` dan perbarui array `GETTING_STARTED_TUTORIALS`. Pastikan perintah terminal untuk Windows, Linux, dan macOS tetap terdefinisi secara presisi.
3. **Validasi Sintaksis & Linting:**  
   Jalankan pemeriksaan otomatis:
   ```bash
   npm run typecheck
   npm run lint
   ```
4. **Verifikasi Jalur Tautan & Build:**  
   Jalankan `npm run build` dan pastikan routing serta aset terkompilasi bersih tanpa peringatan.

---

## 5. Standar Kebijakan Bahasa Teknis

Seluruh modul dalam Getting Started wajib mematuhi panduan resmi:
- **Prinsip:** *"Indonesian for explanations, English for established technical terminology."*
- **Istilah Wajib:** Gunakan `Development Environment`, `Python Interpreter`, `Code Editor`, `Virtual Environment`, `Dependency Management`, dll. (Hindari terjemahan harfiah kaku seperti *lingkungan pengembangan* atau *penerjemah Python*).

