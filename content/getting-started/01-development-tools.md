# Tutorial 01 — Understanding Python Development Tools
## Memahami Perangkat Kerja dan Ekosistem Pemrograman Python

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pemula, mahasiswa, dan pengembang yang baru memulai Python  
> **Fokus Utama:** Membedakan peran runtime, editor, IDE, terminal, dan notebook dalam workflow pengembangan

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Membedakan fungsi **Python Interpreter** sebagai *runtime engine* dan **Code Editor / IDE** sebagai antarmuka penulisan kode.
2. Menjelaskan mengapa IDE tidak sama dengan Python Interpreter.
3. Memilih tooling yang tepat antara workflow berbasis skrip (`.py`) dan berbasis dokumen interaktif (*notebook* `.ipynb`).
4. Mengenal peran ekstensi editor (seperti Python Extension pada VS Code) dalam menyediakan fitur linting, autocomplete, dan debugging.
5. Menentukan perangkat kerja yang paling sesuai dengan kebutuhan proyek (rekayasa perangkat lunak vs. eksplorasi sains data).

---

## 2. Prasyarat (Prerequisites)

- Tidak memerlukan pengetahuan pemrograman sebelumnya.
- Komputer atau laptop dengan sistem operasi Windows 10/11, Linux (Ubuntu/Debian/Fedora), atau macOS.
- Koneksi internet untuk mengunduh perangkat lunak pada tutorial berikutnya.

---

## 3. Penjelasan Konsep & Peta Ekosistem Tooling

Saat belajar pemrograman, pemula sering kali bingung membedakan antara aplikasi untuk mengetik kode (seperti VS Code atau Notepad) dan program yang benar-benar menjalankan kode tersebut (Python Interpreter). Memahami pemisahan tanggung jawab ini adalah langkah pertama menuju penguasaan Development Environment.

```text
+-----------------------------------------------------------------------+
|                       DEVELOPER WORKSTATION                           |
|                                                                       |
|  [ Text Editor / IDE ]       [ Terminal / Shell ]     [ Browser ]     |
|   - VS Code                   - PowerShell             - JupyterLab   |
|   - PyCharm                   - Bash / Zsh             - Google Colab |
|   - Sublime / Nano            - Command Prompt                        |
|          |                            |                     |         |
|          +------------+---------------+                     |         |
|                       |                                     |         |
|                       v                                     v         |
|          [ PYTHON INTERPRETER / RUNTIME ENGINE ]   [ JUPYTER KERNEL ] |
|            - CPython (python.exe / python3)         - ipykernel       |
|            - Bytecode Compiler (.pyc)                                 |
|            - Virtual Machine (PVM)                                    |
|                       |                                               |
|                       v                                               |
|          [ OPERATING SYSTEM / HARDWARE CPU / RAM ]                    |
+-----------------------------------------------------------------------+
```

### A. Python Interpreter (Mesin Eksekusi Kode)
Python Interpreter adalah program inti yang membaca kode sumber Python (`.py`), mengompilasinya menjadi *bytecode*, dan mengeksekusinya di atas mesin virtual Python (*Python Virtual Machine* / PVM).
- **Implementasi Standar:** CPython (ditulis dalam bahasa C, merupakan versi resmi dari [python.org](https://www.python.org)).
- **Tanggung Jawab:** Memeriksa sintaksis, mengalokasikan memori, mengeksekusi instruksi, dan mencetak keluaran atau error ke terminal.
- **Karakteristik:** Python Interpreter adalah program berbasis CLI (Command Line Interface) tanpa antarmuka grafis (GUI) jendela modern.

### B. Code Editor vs. Integrated Development Environment (IDE)
Banyak pemula mengira bahwa menginstal VS Code otomatis berarti Python sudah terpasang. Ini adalah **miskonsepsi umum**:
- **Code Editor (Penyunting Teks Kode):** Program editor teks ringan yang dirancang untuk menulis dan mengedit file kode dengan fitur penyorotan sintaksis (*syntax highlighting*). Contoh: **Visual Studio Code (VS Code)**, Sublime Text, Notepad++. Editor membutuhkan Python Interpreter eksternal untuk mengeksekusi kode.
- **IDE (Integrated Development Environment):** Lingkungan terpadu berskala penuh yang menggabungkan editor, debugger, build automation, profiler, dan interpreter management dalam satu paket besar. Contoh: **PyCharm Professional**, Microsoft Visual Studio.
- **Mengapa IDE Bukan Python Interpreter?** IDE hanyalah "papan ketik canggih" dan antarmuka manajemen proyek. Tanpa Python Interpreter yang terpasang di sistem operasi, IDE tidak dapat mengeksekusi atau menguji kode program Python Anda sama sekali.

### C. Terminal / Command Line Interface (CLI)
Terminal (PowerShell di Windows, Terminal di macOS, Bash di Linux) adalah jembatan komunikasi teks langsung dengan sistem operasi. Terminal digunakan untuk memanggil Python Interpreter, mengelola paket melalui `pip`, dan menjalankan skrip otomasi.

### D. Ekstensi Bahasa (Python Extension)
Pada editor modern seperti VS Code, fungsionalitas cerdas (seperti IntelliSense, penandaan tipe, refactoring, dan pendeteksi interpreter) disediakan oleh ekstensi modular (misalnya ekstensi resmi *Python by Microsoft*).

### E. Jupyter Notebook, JupyterLab, dan Google Colab
Untuk analisis data, komputasi ilmiah, dan eksplorasi bertahap, ekosistem Python menyediakan format komputasi interaktif:
- **Jupyter Notebook (`.ipynb`):** Dokumen web interaktif yang menggabungkan blok kode eksekusi (*code cells*), teks narasi kaya (*Markdown cells*), visualisasi grafik, dan rumus matematika KaTeX.
- **JupyterLab:** Antarmuka kerja modern berbasis tab untuk mengelola beberapa notebook, terminal, file browser, dan output interaktif sekaligus di peramban lokal.
- **Google Colab:** Layanan cloud gratis dari Google berbasis Jupyter Notebook yang berjalan di atas server Google dengan dukungan GPU/TPU sementara tanpa perlu instalasi lokal.

---

## 4. Perbandingan Paradigma: Skrip (`.py`) vs. Notebook (`.ipynb`)

| Karakteristik | Script-Based (`.py`) | Notebook-Based (`.ipynb`) |
| :--- | :--- | :--- |
| **Format Berkas** | Teks polos (*plain text* UTF-8) | Struktur dokumen JSON terstruktur |
| **Alur Eksekusi** | Linear dari baris pertama hingga selesai | Interaktif sel per sel (*cell-by-cell*) |
| **State Memory** | Bersih setiap kali program selesai berjalan | State variabel tersimpan di memori Kernel selama sesi aktif |
| **Output Grafis** | Ditampilkan lewat jendela pop-up GUI atau disimpan ke disk | Tersemat langsung (*inline*) tepat di bawah sel kode |
| **Version Control (Git)** | Sangat ramah diff, merge, dan review baris | Memerlukan tool pembersih metadata JSON |
| **Penggunaan Utama** | Aplikasi produksi, CLI, API web backend, otomasi, testing | Eksplorasi data, machine learning, visualisasi, riset edukasi |

---

## 5. Panduan Memilih Development Tools

1. **Gunakan VS Code + Python Interpreter Lokal jika:**
   - Anda sedang mempelajari dasar pemrograman terstruktur (Chapter 01–12).
   - Anda membangun aplikasi multi-file, package, REST API, atau proyek capstone produksi.
   - Anda membutuhkan integrasi Git yang rapi dan Unit Testing otomatis.
2. **Gunakan Jupyter Notebook / JupyterLab jika:**
   - Anda melakukan eksperimen analisis data cepat, statistik, atau plotting grafik.
   - Anda membuat catatan teknis interaktif atau laporan praktikum laboratorium komputasi.
3. **Gunakan Google Colab jika:**
   - Anda menggunakan komputer dengan spesifikasi terbatas atau perangkat tablet/Chromebook.
   - Anda membutuhkan akselerasi GPU gratis untuk melatih model Machine Learning kecil.
   - Anda ingin berbagi kode analisis instan ke rekan tim tanpa kendala instalasi lokal.

---

## 6. Langkah Verifikasi Pemahaman

Tanyakan pada diri Anda sebelum melangkah ke Tutorial 02:
- [ ] Apakah saya sudah memahami bahwa menginstal VS Code saja **belum** menginstal Python?
- [ ] Apakah saya mengetahui bahwa Python Interpreter adalah mesin eksekusi utama?
- [ ] Apakah saya tahu kapan harus menggunakan file `.py` dan kapan menggunakan `.ipynb`?

---

## 7. Kesalahan Umum Pemula (Common Mistakes)

1. **Membuka file `.py` menggunakan Microsoft Word:** File Python adalah teks polos; membukanya di Word akan menyisipkan format biner tersembunyi yang merusak kode.
2. **Mengira VS Code adalah compiler:** VS Code adalah editor teks yang memanggil Python Interpreter eksternal di latar belakang.
3. **Mengabaikan Terminal:** Mengandalkan tombol GUI "Run" tanpa memahami perintah terminal yang dijalankan di baliknya membuat pengembang bingung saat terjadi error path atau environment.

---

## 8. Referensi Resmi

- Python Software Foundation: [What is Python? Executive Summary](https://www.python.org/doc/essays/blurb/)
- Visual Studio Code Documentation: [Python in VS Code Overview](https://code.visualstudio.com/docs/languages/python)
- Project Jupyter: [Jupyter Architecture and Project Overview](https://docs.jupyter.org/en/latest/)
