# Tutorial 07 — Running Python Projects
## Menjalankan Proyek Python Modular & Navigasi Workspace

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang ingin menjalankan proyek Python multi-file secara terstruktur dari terminal  
> **Fokus Utama:** Navigasi direktori, eksekusi skrip `.py`, pembacaan traceback error, modul import, dan path relatif

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Membuat dan mengorganisasi direktori kerja proyek (*project directory*) dengan tata kelola standar.
2. Membuka terminal dan melakukan navigasi folder menggunakan perintah `cd`, `ls` / `dir`, dan `pwd`.
3. Menjalankan skrip Python mandiri (`.py`) secara presisi dari terminal menggunakan interpreter yang benar.
4. Memahami idiom standar Python `if __name__ == "__main__":`.
5. Mengimpor fungsi dari modul lokal lain menggunakan *relative import*.
6. Membaca pesan kesalahan (*traceback error*) Python secara sistematis untuk menemukan akar permasalahan.
7. Menjalankan skrip pengujian kesiapan lingkungan kerja (*verification script*).

---

## 2. Prasyarat (Prerequisites)

- Python Interpreter telah terpasang (Tutorial 02).
- Terminal (PowerShell / Command Prompt di Windows, atau Bash/Zsh di Linux/macOS) siap digunakan.
- Virtual Environment aktif jika proyek menggunakan pustaka eksternal (Tutorial 05).

---

## 3. Membuat Direktori Kerja & Navigasi Terminal

Setiap aplikasi Python profesional harus memiliki folder proyeknya sendiri.

### Perintah Pembuatan Direktori & Navigasi:

#### Pada Windows (PowerShell):
```powershell
# 1. Buat folder proyek baru bernama ProyekPertama
mkdir ProyekPertama

# 2. Masuk ke dalam direktori tersebut
cd ProyekPertama

# 3. Periksa direktori saat ini
Get-Location  # atau pwd

# 4. Lihat daftar file dalam direktori
dir  # atau ls
```

#### Pada Linux / macOS (Bash / Zsh):
```bash
# 1. Buat folder proyek baru
mkdir -p ~/ProyekPertama

# 2. Masuk ke dalam direktori
cd ~/ProyekPertama

# 3. Cetak direktori kerja saat ini
pwd

# 4. Lihat daftar file
ls -la
```

---

## 4. Menulis Skrip Utama & Idiom `__name__ == "__main__"`

Di dalam direktori `ProyekPertama`, buat berkas bernama `main.py` menggunakan editor kode favorit Anda (misal VS Code):

```python
"""Python Learning Hub — Getting Started Verification Script.

Skrip standar untuk memverifikasi kesiapan Python Development Environment.
"""


def main() -> None:
    print("Python Learning Hub")
    print("Development Environment Ready!")


if __name__ == "__main__":
    main()
```

### Mengapa Menggunakan `if __name__ == "__main__":`?
Saat Python mengeksekusi file langsung dari terminal, variabel internal `__name__` secara otomatis bernilai `"__main__"`. Pengecekan kondisi ini memastikan:
1. Fungsi `main()` hanya akan dijalankan jika file dieksekusi secara langsung.
2. Jika suatu saat file ini diimpor oleh modul lain (`import main`), kode eksekusi di dalam `main()` tidak akan berjalan secara tidak sengaja. Ini adalah praktik terbaik (*best practice*) rekayasa perangkat lunak Python.

---

## 5. Mengeksekusi Berkas Python dari Terminal

Pastikan terminal Anda berada di dalam folder tempat berkas `main.py` berada (gunakan perintah `dir` atau `ls` untuk memastikan file terlihat).

### Perintah Eksekusi:

#### Pada Windows:
```powershell
# Menggunakan Python Launcher resmi
py main.py

# Atau menggunakan python langsung jika aktif di PATH / venv
python main.py
```

#### Pada Linux dan macOS:
```bash
python3 main.py
```

---

## 6. Hasil Keluaran Terminal yang Terverifikasi

Program akan mencetak keluaran berikut ke terminal:

```text
Python Learning Hub
Development Environment Ready!
```

Jika keluaran di atas tercetak dengan bersih tanpa pesan kesalahan, berarti workstation dan Python Development Environment Anda telah siap 100% untuk digunakan mempelajari seluruh kurikulum pemrograman!

---

## 7. Proyek Modular: Mengimpor Modul Lokal Lain

Dalam proyek nyata, kode dipecah ke dalam beberapa file terpisah agar mudah dirawat.

### Contoh Struktur Folder Modular:
```text
ProyekPertama/
├── kalkulator.py      <-- Modul pembantu (helper module)
└── main.py            <-- Skrip pengendali utama (entry point)
```

#### Berkas `kalkulator.py`:
```python
def hitung_snr(daya_sinyal_mw: float, daya_noise_mw: float) -> float:
    """Menghitung rasio sinyal terhadap derau (SNR)."""
    if daya_noise_mw <= 0:
        raise ValueError("Daya noise harus lebih besar dari nol.")
    return daya_sinyal_mw / daya_noise_mw
```

#### Berkas `main.py` (Mengimpor modul `kalkulator`):
```python
from kalkulator import hitung_snr


def main() -> None:
    daya_sinyal = 100.0
    daya_noise = 2.5
    snr = hitung_snr(daya_sinyal, daya_noise)

    print("=== HASIL ANALISIS TELEMETRI ===")
    print(f"Daya Sinyal : {daya_sinyal} mW")
    print(f"Daya Noise  : {daya_noise} mW")
    print(f"Nilai SNR   : {snr:.2f}")


if __name__ == "__main__":
    main()
```

Jalankan kembali `py main.py` (atau `python3 main.py`). Python akan otomatis mencari berkas `kalkulator.py` di direktori yang sama, mengimpor fungsi `hitung_snr`, dan mencetak hasil kalkulasi.

---

## 8. Membaca dan Memahami Traceback Error Python

Saat terjadi kesalahan logika atau salah ketik, Python Interpreter akan menghentikan eksekusi dan mencetak laporan beruntun bernama **Traceback**.

### Contoh Traceback Error:
```text
Traceback (most recent call last):
  File "D:\ProyekPertama\main.py", line 7, in main
    snr = hitung_snr(daya_sinyal, daya_noise)
  File "D:\ProyekPertama\kalkulator.py", line 4, in hitung_snr
    if daya_noise_mw <= 0:
ValueError: Daya noise harus lebih besar dari nol.
```

### Cara Membaca Traceback Secara Efektif:
1. **Lihat Baris Paling Bawah Terlebih Dahulu:** Baris terakhir memberi tahu jenis exception (`ValueError`) dan pesan deskriptif kesalahannya (*"Daya noise harus lebih besar dari nol"*).
2. **Lihat Rantai Panggilan dari Bawah ke Atas:**
   - Baris di atasnya memberi tahu file dan nomor baris persis tempat error dipicu (`kalkulator.py`, line 4).
   - Baris di atasnya lagi menunjukkan pemanggil fungsi tersebut di `main.py` baris 7.
3. Dengan membaca traceback dari bawah ke atas, Anda dapat langsung melompat ke baris kode yang perlu diperbaiki tanpa menebak-nebak.

---

## 9. Kesalahan Umum Saat Menjalankan Proyek

1. **`python: can't open file 'main.py': [Errno 2] No such file or directory`:**
   - **Penyebab:** Terminal Anda tidak berada di dalam folder yang sama dengan berkas `main.py`.
   - **Solusi:** Jalankan perintah `pwd` (atau `Get-Location` di PowerShell) untuk melihat folder Anda saat ini, lalu gunakan perintah `cd nama_folder` untuk berpindah ke folder tempat file `main.py` disimpan.
2. **`ModuleNotFoundError: No module named 'kalkulator'`:**
   - **Penyebab:** Berkas `kalkulator.py` berada di luar folder kerja atau salah ejaan nama file.

---

## 10. Referensi Resmi

- Python Software Foundation: [Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html)
- Python Software Foundation: [The Python Standard Library — pathlib](https://docs.python.org/3/library/pathlib.html)
- Python Software Foundation: [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

