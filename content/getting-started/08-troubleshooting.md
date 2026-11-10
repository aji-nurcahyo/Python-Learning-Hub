# Tutorial 08 — Troubleshooting & Environment Verification
## Diagnostik Masalah dan Verifikasi Aman Lingkungan Kerja Python

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang mengalami kendala teknis saat setup environment atau eksekusi program  
> **Fokus Utama:** Katalog solusi aman untuk kendala PATH, permission, interpreter, pip, virtual environment, dan kernel

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Melakukan diagnosis sistematis ketika perintah `python`, `python3`, atau `py` tidak dikenali oleh terminal.
2. Memperbaiki variabel lingkungan sistem **PATH** tanpa merusak konfigurasi sistem operasi.
3. Mengatasi pesan error *PowerShell Execution Policy* secara aman tanpa menurunkan tingkat keamanan Windows secara global.
4. Menyelesaikan kendala **`ModuleNotFoundError`** akibat salah pemilihan interpreter atau Virtual Environment yang tidak aktif.
5. Memperbaiki error sertifikat SSL pada `pip` saat mengunduh paket di macOS dan Windows.
6. Memperbaiki masalah deteksi Python Interpreter di Visual Studio Code.
7. Mengatasi masalah *Port Conflict* dan *Kernel Died* pada JupyterLab / Jupyter Notebook.
8. Menjalankan alur verifikasi menyeluruh 8 langkah sebelum memulai pembelajaran kurikulum.

---

## 2. Matriks Diagnostik Kendala Umum & Solusi Aman

Berikut adalah panduan pemecahan masalah terstruktur untuk kendala yang paling sering dihadapi oleh pengembang:

### Kendala 1: Perintah `python` atau `py` Tidak Dikenali di Terminal
- **Pesan Galat:**  
  *Windows:* `'python' is not recognized as an internal or external command, operable program or batch file.*  
  *Linux/macOS:* `bash: python: command not found`
- **Penyebab:** Direktori instalasi Python belum terdaftar pada variabel lingkungan sistem `PATH`.
- **Solusi Penanganan:**
  - **Pada Windows:**  
    1. Buka kembali file installer Python `.exe` yang diunduh dari [python.org](https://www.python.org).
    2. Pilih opsi **Modify**.
    3. Pastikan kotak **Add Python to environment variables** tercentang.
    4. Selesaikan wizard dan **buka jendela terminal baru** (terminal lama tidak membaca perubahan PATH).
    5. Sebagai alternatif cepat di Windows, coba gunakan perintah Python Launcher resmi:
       ```powershell
       py --version
       ```
  - **Pada Linux/macOS:**  
    Sistem UNIX modern tidak menggunakan alias `python`, melainkan `python3`:
    ```bash
    python3 --version
    ```

---

### Kendala 2: PowerShell Membuka Microsoft Store Saat Mengetik `python`
- **Gejala:** Mengetik `python` di PowerShell Windows 10/11 tiba-tiba membuka jendela aplikasi Microsoft Store untuk mengunduh Python.
- **Penyebab:** Windows menyertakan shortcut penunjuk (*App Execution Aliases*) bawaan yang memiliki prioritas lebih tinggi daripada installer CPython resmi.
- **Solusi Penanganan:**
  1. Buka menu **Start** Windows -> ketik dan buka **Settings**.
  2. Buka menu **Apps > Advanced app settings > App execution aliases**.
  3. Cari daftar aplikasi bernama **App Installer (python.exe)** dan **App Installer (python3.exe)**.
  4. Matikan (*toggle OFF*) kedua opsi tersebut.
  5. Buka kembali terminal PowerShell dan jalankan `python --version`.

---

### Kendala 3: PowerShell Script Execution Policy Terblokir
- **Pesan Galat:**  
  `File C:\Proyek\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`
- **Penyebab:** Kebijakan keamanan bawaan Windows PowerShell melarang eksekusi skrip pihak ketiga yang tidak ditandatangani (*Restricted*).
- ⚠️ **Larangan Keamanan:** Jangan pernah menjalankan perintah `Set-ExecutionPolicy Unrestricted` secara sistem global, karena ini melemahkan perlindungan komputer Anda terhadap malware skrip eksternal!
- **Solusi Aman yang Direkomendasikan:**
  Gunakan parameter cakupan `-Scope Process`. Kebijakan ini hanya mengizinkan eksekusi skrip pada jendela terminal yang sedang terbuka saat ini tanpa mengubah konfigurasi sistem operasi secara permanen:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .\.venv\Scripts\Activate.ps1
  ```

---

### Kendala 4: `ModuleNotFoundError: No module named 'nama_paket'`
- **Pesan Galat:**  
  `ModuleNotFoundError: No module named 'requests'` (atau pandas, numpy, dll.).
- **Penyebab:** Anda sudah menginstal paket menggunakan `pip`, tetapi kode Anda dijalankan oleh Python Interpreter atau Virtual Environment yang berbeda.
- **Solusi Penanganan Sistematis:**
  1. Periksa executable Python mana yang sedang aktif saat ini:
     - Windows: `Get-Command python | Format-List Source` (atau `where python`)
     - Linux/macOS: `which python3`
  2. Pastikan Virtual Environment proyek Anda aktif (tanda `(.venv)` muncul di awal prompt terminal).
  3. Instal paket menggunakan pemanggilan interpreter eksplisit:
     - Windows: `py -m pip install requests`
     - Linux/macOS: `python3 -m pip install requests`
  4. Di VS Code, pastikan status bar di kanan bawah menunjuk ke interpreter `.venv`:  
     Tekan `Ctrl + Shift + P` -> ketik `Python: Select Interpreter` -> pilih opsi `.venv`.

---

### Kendala 5: Kendala Sertifikat SSL pada `pip` di macOS
- **Pesan Galat:**  
  `pip install ... [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate`
- **Penyebab:** Python di macOS tidak menggunakan sertifikat root OS bawaan secara langsung.
- **Solusi Penanganan:**
  Buka terminal macOS dan jalankan berkas pembaruan sertifikat resmi:
  ```bash
  /Applications/Python\ 3.12/Install\ Certificates.command
  ```
  *(Sesuaikan angka `3.12` dengan versi Python yang Anda pasang).*

---

### Kendala 6: Error Jalur Berkas (*File Path Errors*) di Windows
- **Pesan Galat:**  
  `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes...` saat menulis path file `"C:\Users\nama\data.csv"`.
- **Penyebab:** Karakter garis miring terbalik (`\`) di Windows diperlakukan oleh Python sebagai karakter escape (misal `\n`, `\t`, `\u`).
- **Solusi Penanganan (3 Pilihan Aman):**
  1. Gunakan garis miring biasa (*forward slash* - direkomendasikan):  
     `path = "C:/Users/nama/data.csv"`
  2. Gunakan *raw string* dengan awalan huruf `r`:  
     `path = r"C:\Users\nama\data.csv"`
  3. Gunakan modul modern standar `pathlib`:
     ```python
     from pathlib import Path
     path = Path("C:/Users/nama/data.csv")
     ```

---

### Kendala 7: Konflik Port Server Jupyter (Port 8888 Already in Use)
- **Pesan Galat:**  
  `[C ... NetworkError] Port 8888 is already in use, trying another port.`
- **Penyebab:** Ada sesi lama `jupyter lab` atau aplikasi web lokal lain yang masih mendengarkan port `8888`.
- **Solusi Penanganan:**
  1. Biarkan JupyterLab secara otomatis memilih port berikutnya (`8889` atau `8890`), atau
  2. Tentukan port eksplisit saat menjalankan perintah:
     ```bash
     jupyter lab --port 8900
     ```

---

## 3. Alur Verifikasi Lingkungan Kerja 8 Langkah (8-Step Verification Workflow)

Sebelum Anda melanjutkan ke materi pemrograman **Level 1: Python Foundations**, lakukan verifikasi akhir menggunakan daftar periksa berikut:

```text
[LANGKAH 1] Verifikasi Instalasi Python
  Windows : py --version
  Linux   : python3 --version
  macOS   : python3 --version
  Status  : [OK] Menampilkan Python 3.10+

[LANGKAH 2] Verifikasi Modul Pip
  Windows : py -m pip --version
  Linux   : python3 -m pip --version
  Status  : [OK] Menampilkan versi pip terpasang

[LANGKAH 3] Uji Coba Pembuatan Virtual Environment
  Perintah: python -m venv .test_env
  Status  : [OK] Folder .test_env terbentuk bersih

[LANGKAH 4] Uji Coba Aktivasi Virtual Environment
  Windows : .\.test_env\Scripts\Activate.ps1
  Linux   : source .test_env/bin/activate
  Status  : [OK] Awalan prompt terminal berubah menjadi (.test_env)

[LANGKAH 5] Uji Instalasi Paket Terisolasi
  Perintah: pip install requests
  Status  : [OK] Paket berhasil terpasang di .test_env tanpa izin administrator

[LANGKAH 6] Uji Coba Deaktivasi
  Perintah: deactivate
  Status  : [OK] Awalan prompt kembali normal

[LANGKAH 7] Pembersihan Folder Uji
  Windows : Remove-Item -Recurse -Force .test_env
  Linux   : rm -rf .test_env
  Status  : [OK] Workspace bersih kembali

[LANGKAH 8] Eksekusi Skrip Uji Pertama (main.py)
  Perintah: python content/getting-started/code/main.py
  Output  : Python Learning Hub
            Development Environment Ready!
  Status  : [OK] LULUS 100%
```

---

## 4. Referensi Resmi

- Python Software Foundation: [Frequently Asked Questions (FAQ) — Python on Windows](https://docs.python.org/3/faq/windows.html)
- Microsoft Learn: [About Execution Policies in PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)
- Python Packaging Authority: [Pip Troubleshooting Guide](https://pip.pypa.io/en/stable/topics/troubleshooting/)

