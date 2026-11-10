# Tutorial 02 — Installing Python
## Panduan Instalasi Python Interpreter di Windows, Linux, dan macOS

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang ingin memasang CPython resmi pada workstation lokal  
> **Fokus Utama:** Instalasi bersih, konfigurasi PATH sistem, penggunaan Python Launcher, dan verifikasi interpreter

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Mengunduh dan menginstal rilis stabil resmi CPython dari situs web resmi [python.org](https://www.python.org).
2. Memahami pentingnya opsi **Add python.exe to PATH** pada sistem operasi Windows.
3. Memasang Python Interpreter beserta modul `pip` dan `venv` pada distribusi Linux (Ubuntu/Debian).
4. Menginstal Python resmi pada macOS menggunakan installer paket `.pkg` atau Homebrew.
5. Memverifikasi keberhasilan instalasi melalui terminal menggunakan perintah `py` atau `python3`.
6. Mengelola beberapa versi Python yang terpasang di komputer yang sama tanpa konflik.

---

## 2. Prasyarat (Prerequisites)

- Akses akun dengan hak administrator / root pada komputer Anda.
- Koneksi internet aktif untuk mengunduh berkas installer resmi (~30–40 MB).
- Mengetahui arsitektur prosesor sistem Anda (kebanyakan PC modern menggunakan 64-bit / x86_64 atau ARM64 pada Mac Apple Silicon).

---

## 3. Sumber Unduhan Resmi & Rilis Stabil

Selalu unduh Python dari situs web resmi Python Software Foundation:
- **Halaman Unduhan Utama:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Dokumentasi Panduan Setup OS:** [https://docs.python.org/3/using/](https://docs.python.org/3/using/)

> ⚠️ **Prinsip Versi Stabil:** Gunakan rilis stabil resmi (misalnya cabang Python 3.11 atau Python 3.12 LTS). Hindari menginstal versi *pre-release*, *alpha*, atau *beta* untuk keperluan belajar kurikulum umum karena paket pihak ketiga seperti NumPy sering kali belum menyediakan *pre-compiled binary wheels* untuk versi eksperimental.

---

## 4. Langkah Instalasi Berdasarkan Sistem Operasi

### A. Windows 10 / 11

1. **Unduh Installer:** Kunjungi [python.org/downloads/windows](https://www.python.org/downloads/windows/) dan unduh file installer:  
   `Windows installer (64-bit)`.
2. **Jalankan Installer:** Klik dua kali berkas `.exe` yang diunduh.
3. **LANGKAH PALING KRUSIAL:** Pada layar pertama wizard instalasi, pastikan Anda **mencentang kotak pilihan di bagian bawah**:
   - ☑️ **Add python.exe to PATH**
   - ☑️ **Use admin privileges when installing py.exe**
4. **Pilih Metode Instalasi:**
   - Klik **Install Now** untuk instalasi standar (direkomendasikan untuk pemula), atau
   - Klik **Customize installation** jika Anda ingin menginstal ke direktori sistem tanpa spasi (misalnya `C:\Python312`).
5. **Disable Path Length Limit (Opsional tapi Disarankan):** Di akhir instalasi, jika muncul tombol **Disable path length limit**, klik tombol tersebut untuk mencegah kendala batas panjang karakter path Windows (>260 karakter).
6. **Selesai:** Klik **Close**.

---

### B. Linux (Ubuntu / Debian / Linux Mint)

Distribusi modern Linux umumnya sudah menyertakan Python 3 secara bawaan, namun paket manajer `pip` dan modul `venv` sering kali dipisahkan oleh pengelola distro.

Buka terminal Linux Anda (`Ctrl+Alt+T`) dan jalankan:

```bash
# 1. Perbarui indeks repositori paket
sudo apt update

# 2. Instal Python 3, pip, dan virtual environment module
sudo apt install -y python3 python3-pip python3-venv python3-dev

# 3. Verifikasi instalasi paket
python3 --version
python3 -m pip --version
```

Untuk distribusi berbasis Fedora / RHEL:
```bash
sudo dnf install -y python3 python3-pip
```

---

### C. macOS (Apple Silicon M1/M2/M3 & Intel)

macOS modern tidak lagi menyertakan Python 3 bawaan secara lengkap. Ada dua cara standar:

#### Cara 1: Installer Resmi (.pkg) — Direkomendasikan untuk Pemula
1. Kunjungi [python.org/downloads/macos](https://www.python.org/downloads/macos/).
2. Unduh berkas **macOS 64-bit universal2 installer**.
3. Buka paket `.pkg`, ikuti petunjuk wizard, dan selesaikan instalasi.
4. **PENTING:** Buka folder aplikasi Python di `/Applications/Python 3.x/` dan klik dua kali berkas skrip `Install Certificates.command` untuk memperbarui sertifikat SSL Root (mencegah error saat `pip` mengunduh paket via HTTPS).

#### Cara 2: Menggunakan Homebrew (Untuk Pengembang)
Jika Anda sudah memasang Homebrew:
```bash
brew install python
```

---

## 5. Verifikasi Keberhasilan Instalasi di Terminal

Tutup semua jendela terminal yang terbuka sebelumnya, lalu buka jendela terminal baru agar variabel lingkungan sistem `PATH` dimuat ulang.

### Perintah Verifikasi di Windows (PowerShell / Command Prompt):
```powershell
# Menggunakan Python Launcher resmi Windows (Direkomendasikan)
py --version

# Atau memanggil executable python langsung
python --version

# Memeriksa modul pip bawaan
py -m pip --version
```

**Keluaran Terminal yang Diharapkan:**
```text
Python 3.12.x
pip 24.x from ... (python 3.12)
```

---

### Perintah Verifikasi di Linux dan macOS:
```bash
# Memanggil python3 interpreter
python3 --version

# Memeriksa modul pip bawaan
python3 -m pip --version
```

**Keluaran Terminal yang Diharapkan:**
```text
Python 3.12.x
pip 24.x from ... (python 3.12)
```

---

## 6. Mengelola Beberapa Versi Python (Multiple Python Versions)

Di dunia nyata, Anda mungkin memiliki proyek lama yang memerlukan Python 3.10 dan proyek baru yang menggunakan Python 3.12.

### Pada Windows:
Windows menyediakan utilitas resmi bawaan bernama **Python Launcher (`py.exe`)**:
```powershell
# Melihat seluruh versi Python yang terdeteksi di komputer Anda
py --list

# Menjalankan versi spesifik Python 3.11
py -3.11 --version

# Menjalankan versi spesifik Python 3.12
py -3.12 --version

# Menjalankan skrip script.py dengan Python 3.12
py -3.12 script.py
```

### Pada Linux & macOS:
Sistem UNIX menggunakan symlink eksplisit per versi:
```bash
python3.10 --version
python3.12 --version
```

---

## 7. Kesalahan Umum & Solusi Kendala (Common Mistakes & Troubleshooting)

| Gejala Masalah | Penyebab Utama | Solusi Penanganan Aman |
| :--- | :--- | :--- |
| **`python: command not found`** atau *"is not recognized as an internal or external command"* | Kotak **Add python.exe to PATH** lupa dicentang saat instalasi di Windows. | 1. Buka kembali file installer Python `.exe`.<br>2. Pilih opsi **Modify**.<br>3. Centang opsi **Add Python to environment variables** lalu selesaikan wizard.<br>4. Restart jendela terminal. |
| **Membuka Microsoft Store saat mengetik `python` di Windows** | Windows App Execution Aliases mencegat perintah sebelum interpreter asli terpanggil. | Buka Windows Settings -> ketik *"Manage app execution aliases"* -> matikan tombol toggle untuk *"App Installer (python.exe)"* dan *"App Installer (python3.exe)"*. |
| **`SSL: CERTIFICATE_VERIFY_FAILED` saat menjalankan pip di macOS** | Sertifikat root CA bawaan macOS belum terhubung ke bundle Python. | Jalankan skrip sertifikat bawaan:<br>`/Applications/Python\ 3.x/Install\ Certificates.command` |
| **`No module named pip` di Ubuntu** | Paket pip dipisahkan oleh repositori Debian. | Jalankan: `sudo apt install python3-pip` |

---

## 8. Referensi Resmi

- Python Software Foundation: [Using Python on Windows](https://docs.python.org/3/using/windows.html)
- Python Software Foundation: [Using Python on Unix platforms](https://docs.python.org/3/using/unix.html)
- Python Software Foundation: [Using Python on a Mac](https://docs.python.org/3/using/mac.html)

