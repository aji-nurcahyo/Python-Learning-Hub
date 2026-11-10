# Tutorial 04 — Jupyter Notebook & JupyterLab
## Bekerja dengan Dokumen Komputasi Interaktif Jupyter

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang ingin melakukan eksplorasi data, komputasi visual, dan analisis interaktif  
> **Fokus Utama:** Struktur notebook `.ipynb`, instalasi JupyterLab, manajemen sel kode & Markdown, serta pemilihan kernel

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Menjelaskan konsep dokumen komputasi interaktif **Jupyter Notebook**.
2. Memahami struktur internal berkas `.ipynb` berbasis format data JSON.
3. Membedakan karakteristik penggunaan antara skrip Python linear (`.py`) dan notebook interaktif (`.ipynb`).
4. Menginstal **JupyterLab** dan **Jupyter Notebook** menggunakan manajer paket `pip`.
5. Menjalankan server lokal JupyterLab dan mengakses dashboard kerjanya melalui peramban web (*browser*).
6. Membuat sel kode (*code cells*) dan sel teks narasi (*Markdown cells*).
7. Memilih dan mengganti **Jupyter Kernel** yang bertanggung jawab mengeksekusi kode.
8. Mengatasi kendala umum seperti *Kernel Died*, *Kernel Busy*, atau paket yang tidak terdeteksi di notebook.

---

## 2. Prasyarat (Prerequisites)

- Python Interpreter versi 3.10+ telah terpasang di komputer Anda.
- Manajer paket `pip` dapat dipanggil dari terminal.
- Disarankan telah memahami konsep Virtual Environment (Tutorial 05) jika ingin menjaga keteraturan dependensi sistem.

---

## 3. Apa Itu Jupyter Notebook & Bagaimana Strukturnya?

**Jupyter Notebook** adalah aplikasi web sumber terbuka (*open source*) yang memungkinkan Anda membuat dan berbagi dokumen yang memuat kode program hidup (*live code*), visualisasi interaktif, teks penjelasan naratif, dan persamaan matematika terformat KaTeX/LaTeX.

### Struktur Berkas `.ipynb` di Balik Layar:
Meskipun tampil sebagai dokumen visual di browser, berkas berekstensi `.ipynb` sebenarnya adalah file teks berformat **JSON** (*JavaScript Object Notation*). Di dalamnya tersimpan array sel yang mencakup:
- `cell_type`: Menentukan apakah sel berupa `"code"` atau `"markdown"`.
- `source`: Teks kode atau narasi yang ditulis oleh pengguna.
- `outputs`: Keluaran komputasi, teks error, grafik citra (Base64 encoded PNG), atau tabel HTML hasil eksekusi.
- `execution_count`: Angka urutan eksekusi sel (misalnya `[1]`, `[2]`).
- `metadata`: Informasi kernel bahasa pemrograman yang digunakan (Python 3, R, Julia).

```json
{
 "cells": [
  {
   "cell_type": "markdown",
   "source": ["# Analisis Sinyal Telekomunikasi\n", "Eksplorasi SNR."]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "source": ["daya_mw = 100\n", "print(daya_mw)"],
   "outputs": [{"output_type": "stream", "text": ["100\n"]}]
  }
 ],
 "metadata": { "kernelspec": { "name": "python3", "display_name": "Python 3" } }
}
```

---

## 4. Instalasi JupyterLab & Jupyter Notebook

JupyterLab adalah antarmuka generasi terbaru dari Project Jupyter yang lebih modular dan fleksibel dibandingkan Jupyter Notebook klasik.

### Perintah Instalasi via Terminal:

#### Pada Windows (PowerShell):
```powershell
py -m pip install --upgrade pip
py -m pip install jupyterlab notebook
```

#### Pada Linux / macOS:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install jupyterlab notebook
```

---

## 5. Menjalankan JupyterLab di Peramban Web

Setelah proses instalasi selesai, buka terminal Anda di direktori kerja proyek yang diinginkan, lalu jalankan:

```bash
jupyter lab
```

Perintah di atas akan memulai server lokal Jupyter (biasanya pada port `http://localhost:8888/lab`) dan secara otomatis membuka antarmuka kerja JupyterLab di peramban web bawaan Anda.

> 💡 **Tips Penggunaan:** Jangan menutup jendela terminal tempat Anda menjalankan perintah `jupyter lab`! Terminal tersebut bertindak sebagai backend server yang melayani proses komputasi notebook. Untuk menghentikan server, tekan `Ctrl + C` dua kali di jendela terminal tersebut.

---

## 6. Membuat Notebook Baru & Mengelola Sel

1. Pada halaman **Launcher** JupyterLab, di bagian bawah kategori **Notebook**, klik ikon **Python 3 (ipykernel)**.
2. Sebuah file notebook baru tanpa judul (`Untitled.ipynb`) akan terbuka.
3. **Mengganti Nama Berkas:** Klik kanan tab file di atas atau di file browser kiri -> klik **Rename Notebook...** -> beri nama `analisis_dasar.ipynb`.

### A. Sel Kode (Code Cells)
Sel kode adalah tempat Anda menulis instruksi Python yang dapat dieksekusi:
1. Ketik baris kode berikut pada sel pertama:
   ```python
   nilai_a = 50
   nilai_b = 25
   total = nilai_a + nilai_b
   print(f"Hasil penjumlahan: {total}")
   ```
2. **Cara Menjalankan Sel:**
   - Tekan `Shift + Enter`: Mengeksekusi sel saat ini dan langsung berpindah ke sel di bawahnya (atau membuat sel baru jika berada di akhir).
   - Tekan `Ctrl + Enter`: Mengeksekusi sel saat ini tanpa memindahkan kursor.
3. Perhatikan label di sebelah kiri: `[1]`. Angka ini menunjukkan urutan eksekusi sel tersebut.

### B. Sel Markdown (Markdown Cells)
Sel Markdown digunakan untuk menulis dokumentasi, rumus, catatan penjelasan, dan judul bab:
1. Buat sel baru di bawahnya.
2. Ubah tipe sel dari **Code** menjadi **Markdown** melalui menu dropdown di toolbar atas (atau tekan tombol pintas `Esc` lalu tekan `M`).
3. Ketik format teks Markdown:
   ```markdown
   ### Kesimpulan Eksperimen
   - Data terproses secara akurat.
   - Variabel `total` bernilai **75**.
   ```
4. Tekan `Shift + Enter` untuk merender tampilan teks berformat.

---

## 7. Memilih dan Mengelola Jupyter Kernel

**Kernel** adalah proses terpisah di latar belakang yang menjalankan kode Python Anda dan mempertahankan state variabel di dalam memori RAM komputer.

- **Status Indikator Kernel:** Perhatikan lingkaran kecil di pojok kanan atas notebook:
  - Lingkaran kosong (`⚪`): Kernel dalam kondisi siap (*Idle*).
  - Lingkaran penuh (`⚫`): Kernel sedang sibuk menghitung (*Busy*).
- **Restart Kernel:** Jika program Anda terjebak dalam perulangan tanpa henti (*infinite loop*) atau variabel menjadi berantakan, klik menu **Kernel > Restart Kernel...** untuk membersihkan memori dan memulai sesi komputasi dari awal.
- **Restart & Run All Cells:** Klik menu **Kernel > Restart Kernel and Run All Cells...** untuk menguji apakah seluruh notebook dapat dieksekusi secara linear dan konsisten dari sel teratas hingga terbawah.

---

## 8. Menggunakan Jupyter Notebook Langsung di VS Code

Jika Anda lebih menyukai lingkungan kerja VS Code:
1. Buka VS Code.
2. Pasang ekstensi resmi: **Jupyter** buatan Microsoft (ID: `ms-toolsai.jupyter`).
3. Buat file dengan ekstensi `.ipynb` (misalnya `catatan.ipynb`).
4. VS Code akan langsung membuka antarmuka editor notebook lengkap dengan tombol sel, pemilih kernel di pojok kanan atas, dan output grafis yang terintegrasi rapi dengan tema VS Code Anda.

---

## 9. Kesalahan Umum & Solusi Kendala (Common Mistakes & Troubleshooting)

| Masalah | Penyebab | Solusi Penanganan |
| :--- | :--- | :--- |
| **`No module named 'pandas'` di notebook padahal sudah diinstal** | Paket diinstal pada Python global, sedangkan notebook menggunakan kernel dari Virtual Environment lain (atau sebaliknya). | Jalankan instalasi langsung ke kernel yang aktif dari dalam sel notebook:<br>`%pip install pandas`<br>(Simbol `%` memastikan pip yang dipanggil adalah pip milik kernel aktif). |
| **Eksekusi sel berurutan acak menghasilkan error `NameError`** | Sel di bagian bawah dijalankan sebelum sel di atas yang mendefinisikan variabel dieksekusi. | Biasakan menjalankan notebook dari atas ke bawah. Gunakan menu **Kernel > Restart & Run All Cells**. |
| **Port 8888 sudah digunakan (*Port already in use*)** | Ada sesi Jupyter server lama yang masih berjalan di latar belakang. | Jupyter akan otomatis mencoba port berikutnya (`8889`), atau Anda dapat menentukan port secara manual:<br>`jupyter lab --port 8890` |

---

## 10. Referensi Resmi

- Project Jupyter Installation Guide: [https://jupyter.org/install](https://jupyter.org/install)
- JupyterLab Official Documentation: [https://jupyterlab.readthedocs.io/](https://jupyterlab.readthedocs.io/)
- VS Code Jupyter Extension Guide: [https://code.visualstudio.com/docs/datascience/jupyter-notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

