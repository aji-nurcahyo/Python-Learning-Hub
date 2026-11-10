# Tutorial 05 — Virtual Environment & Package Management
## Isolasi Dependensi Proyek dengan Virtual Environment dan Pip

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang ingin mengelola dependensi pihak ketiga secara profesional dan rapi  
> **Fokus Utama:** Konsep isolasi dependensi, modul bawaan `venv`, aktivasi lintas OS, `pip`, dan berkas `requirements.txt`

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Menjelaskan mengapa **Virtual Environment** mutlak diperlukan dalam pengembangan perangkat lunak Python.
2. Memahami risiko bahaya jika menginstal paket pihak ketiga langsung ke Python global sistem operasi.
3. Membuat direktori Virtual Environment lokal (`.venv`) menggunakan modul bawaan `venv`.
4. Mengaktifkan dan menonaktifkan Virtual Environment di Windows (PowerShell & CMD), Linux, dan macOS.
5. Memahami dan mengatasi kebijakan eksekusi skrip Windows PowerShell (*Execution Policy*) secara aman tanpa merusak keamanan sistem.
6. Memasang, memperbarui, dan memeriksa daftar pustaka (*library*) menggunakan `pip`.
7. Menghasilkan dan menggunakan berkas daftar dependensi `requirements.txt`.
8. Mengonfigurasi VS Code dan Jupyter agar mengenali dan menggunakan Virtual Environment proyek secara tepat.

---

## 2. Mengapa Virtual Environment Mutlak Diperlukan?

Bayangkan skenario nyata berikut:
- **Proyek A (Sistem Analisis Sinyal 2024):** Membutuhkan pustaka `pandas` versi `1.5.3` karena menggunakan method API lama.
- **Proyek B (Platform Dashboard IoT 2026):** Membutuhkan `pandas` versi `2.2.0` yang memiliki breaking changes dan dependensi baru.

Jika Anda menginstal paket langsung ke lingkungan Python global sistem operasi:
1. Kedua proyek tersebut akan saling menimpa versi dependensi (*dependency conflict / dependency hell*).
2. Proyek A atau Proyek B akan mengalami crash runtime karena ketidakcocokan versi fungsi.
3. Menghapus pustaka secara global berisiko merusak utilitas internal sistem operasi (terutama di distribusi Linux seperti Ubuntu yang mengandalkan Python untuk paket sistem).

> 🛡️ **Solusi Standar Industri:** **Virtual Environment** membuat salinan terisolasi dari Python Interpreter, pustaka standar, direktori `site-packages`, dan executable `pip` di dalam folder proyek Anda (lazim dinamai `.venv`). Setiap proyek memiliki ekosistem paketnya sendiri yang mandiri tanpa mencemari sistem global.

---

## 3. Membuat Virtual Environment (`.venv`)

Modul `venv` adalah pustaka standar bawaan Python (PEP 405) sehingga tidak memerlukan instalasi tambahan.

Buka terminal di dalam direktori proyek kerja Anda, lalu jalankan:

### Pada Windows (PowerShell / Command Prompt):
```powershell
# Membuat virtual environment bernama .venv
py -m venv .venv
```

### Pada Linux dan macOS:
```bash
# Membuat virtual environment bernama .venv
python3 -m venv .venv
```

Setelah perintah selesai, folder baru bernama `.venv/` akan terbentuk di direktori kerja Anda. Folder ini berisi:
- `Scripts/` (di Windows) atau `bin/` (di Linux/macOS): Berisi executable python lokal dan skrip aktivasi.
- `Lib/site-packages/`: Tempat seluruh paket yang Anda instal nanti akan disimpan.
- `pyvenv.cfg`: Berkas konfigurasi path versi Python asal.

> 💡 **Best Practice:** Tambahkan nama folder `.venv/` ke dalam berkas `.gitignore` agar file biner lingkungan virtual tidak ikut terunggah ke repositori Git!

---

## 4. Mengaktifkan dan Menonaktifkan Virtual Environment

Sebelum menginstal paket apa pun, Anda **wajib mengaktifkan** environment tersebut pada sesi terminal Anda:

### A. Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

#### Mengatasi Kendala Execution Policy di PowerShell:
Jika saat menjalankan perintah di atas muncul pesan error berwarna merah:
> *"File ... Activate.ps1 cannot be loaded because running scripts is disabled on this system."*

**Penyebab:** Kebijakan keamanan bawaan Windows membatasi eksekusi skrip PowerShell lokal (`Restricted`).

**Solusi Aman yang Benar:** Berikan izin eksekusi hanya untuk jendela terminal (proses) saat ini tanpa melonggarkan keamanan sistem secara permanen:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

---

### B. Windows Command Prompt (CMD):
```cmd
.\.venv\Scripts\activate.bat
```

---

### C. Linux dan macOS (Bash / Zsh):
```bash
source .venv/bin/activate
```

---

### Tanda Berhasil Aktif:
Perhatikan awalan prompt terminal Anda. Jika di sisi paling kiri muncul teks `(.venv)` di dalam tanda kurung, berarti Virtual Environment telah **aktif**:
```text
(.venv) PS D:\ProyekPython>
# atau
(.venv) user@machine:~/proyek-python$
```

### Menonaktifkan (Deactivate):
Kapan pun Anda selesai bekerja, cukup ketik satu kata perintah:
```bash
deactivate
```
Prompt terminal akan kembali normal ke status sistem biasa.

---

## 5. Manajemen Paket dengan `pip`

Saat Virtual Environment aktif, setiap pemanggilan perintah `pip` akan secara otomatis memasang paket ke dalam direktori `.venv/Lib/site-packages/` lokal proyek Anda, **bukan ke sistem global**.

### A. Memperbarui pip:
```bash
python -m pip install --upgrade pip
```

### B. Memasang Paket Baru:
```bash
# Menginstal paket tunggal
pip install requests

# Menginstal paket dengan versi spesifik
pip install numpy==1.26.4

# Menginstal beberapa paket sekaligus
pip install requests rich matplotlib
```

### C. Memeriksa Daftar Paket yang Terpasang:
```bash
pip list
```

---

## 6. Mengelola Berkas Dependensi `requirements.txt`

Untuk mempermudah kolaborasi tim dan deployment ke server, daftar seluruh pustaka yang dibutuhkan proyek dicatat dalam berkas standar `requirements.txt`.

### A. Menghasilkan Berkas `requirements.txt` (Freeze):
```bash
pip freeze > requirements.txt
```
Berkas `requirements.txt` akan berisi daftar nama paket dan versinya secara presisi:
```text
matplotlib==3.8.4
numpy==1.26.4
requests==2.31.0
rich==13.7.1
```

### B. Memasang Seluruh Dependensi di Komputer Lain:
Saat rekan tim atau Anda sendiri meng-clone repositori di komputer baru:
1. Buat virtual environment baru: `python -m venv .venv`
2. Aktifkan virtual environment: `source .venv/bin/activate` (atau skrip Windows)
3. Instal seluruh paket sekaligus:
   ```bash
   pip install -r requirements.txt
   ```

---

## 7. Memilih Virtual Environment di VS Code & Jupyter

### A. Pada VS Code:
1. Buka folder proyek yang memuat `.venv`.
2. Tekan `Ctrl + Shift + P` -> ketik `Python: Select Interpreter`.
3. VS Code biasanya akan memberi tanda bintang `Recommended` pada opsi:  
   `Python 3.12.x ('.venv': venv) .\.venv\Scripts\python.exe`.
4. Pilih opsi tersebut. Setiap kali Anda membuka Integrated Terminal baru (`Ctrl + \``), VS Code akan otomatis mengaktifkan `(.venv)` untuk Anda.

### B. Menghubungkan Virtual Environment ke Jupyter Kernel:
Jika Anda ingin menggunakan paket yang diinstal di dalam `.venv` pada notebook Jupyter:
1. Pastikan `.venv` aktif.
2. Instal paket `ipykernel`:
   ```bash
   pip install ipykernel
   ```
3. Daftarkan environment ke daftar kernel Jupyter:
   ```bash
   python -m ipykernel install --user --name=.venv --display-name "Python (.venv Proyek)"
   ```
4. Di notebook Jupyter, pilih kernel **"Python (.venv Proyek)"**.

---

## 8. Kesalahan Umum (Common Mistakes)

1. **Lupa mengaktifkan `.venv` sebelum menjalankan `pip install`:** Akibatnya paket terpasang ke Python global, dan saat dijalankan di proyek lain modul tersebut tidak ditemukan.
2. **Menyimpan Virtual Environment ke repositori Git:** Folder `.venv` berisi ribuan berkas biner spesifik platform OS Anda. Jangan pernah meng-commit folder `.venv`; cukup commit berkas `requirements.txt` atau `pyproject.toml`.
3. **Memindahkan atau mengganti nama folder proyek:** Virtual Environment menyimpan path absolut. Jika folder proyek dipindahkan atau diubah namanya, path internal `.venv` bisa rusak. Solusi terbaik adalah menghapus folder `.venv` lama dan membuatnya kembali (`python -m venv .venv`).

---

## 9. Referensi Resmi

- Python Software Foundation: [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- Python Packaging Authority (PyPA): [Installing Packages Tutorial](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- Python Packaging Authority (PyPA): [Requirements Files](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

