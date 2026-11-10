# Tutorial 06 — Google Colab
## Bekerja dengan Cloud Jupyter Notebook di Google Colab

> **Bagian:** Getting Started with Python  
> **Target Audiens:** Pengembang yang ingin menjalankan komputasi Python di cloud tanpa setup lokal  
> **Fokus Utama:** Alur kerja Google Colab, eksekusi sel, instalasi paket, integrasi Google Drive, dan pemahaman batasan runtime

---

## 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan tutorial ini, Anda diharapkan mampu:
1. Memahami apa itu **Google Colaboratory (Google Colab)** dan bagaimana cara kerjanya.
2. Membuat, mengedit, dan mengeksekusi dokumen notebook berbasis cloud.
3. Menulis dan merender sel kode Python serta sel teks naratif berformat Markdown.
4. Menginstal pustaka pihak ketiga secara dinamis menggunakan sintaksis perintah `!pip install`.
5. Mengunggah berkas dataset lokal ke dalam *virtual machine* Colab.
6. Menghubungkan dan mengotorisasi penyimpanan **Google Drive** ke dalam workspace runtime Colab.
7. Memahami realitas batasan teknis lingkungan komputasi gratis (*runtime timeout*, *idle disconnect*, dan *ephemeral disk*).
8. Mengonfigurasi akselerator perangkat keras (GPU T4) secara bijak sesuai kuota ketersediaan.

---

## 2. Mengenal Google Colaboratory

**Google Colab** adalah layanan hosting notebook Jupyter berbasis peramban web gratis yang disediakan oleh Google. Colab berjalan di atas mesin virtual (*virtual machine*) Linux Ubuntu yang dikelola penuh oleh infrastruktur Google Cloud Platform.

### Keuntungan Utama Google Colab:
- **Nol Konfigurasi Lokal:** Tidak memerlukan instalasi Python Interpreter atau editor di komputer Anda. Sangat cocok untuk perangkat tablet, Chromebook, atau laptop berspesifikasi rendah.
- **Pustaka Populer Sudah Terpasang:** Modul data science seperti `numpy`, `pandas`, `matplotlib`, `scipy`, `scikit-learn`, `torch`, dan `tensorflow` sudah terinstal secara bawaan.
- **Kolaborasi Real-Time:** Memungkinkan beberapa pengguna membuka, mengomentari, dan mengedit notebook yang sama secara simultan layaknya Google Docs.
- **Akses Akselerator Perangkat Keras:** Menyediakan opsi alokasi GPU gratis (seperti NVIDIA T4) untuk eksperimen komputasi paralel dan pelatihan model machine learning kecil.

---

## 3. Membuat Notebook Baru & Eksekusi Kode

1. Buka situs resmi: [https://colab.research.google.com/](https://colab.research.google.com/).
2. Masuk menggunakan akun Google Anda.
3. Pada jendela dialog awal, klik tombol **New Notebook** (atau klik menu **File > New notebook in Drive**).
4. Sebuah dokumen notebook baru akan terbuka dan disimpan otomatis di folder `Colab Notebooks` pada Google Drive Anda.
5. **Mengganti Nama File:** Klik teks nama file di kiri atas (misalnya `Untitled0.ipynb`) lalu ubah menjadi `latihan_colab.ipynb`.

### Menjalankan Sel Kode:
Ketik kode Python berikut pada sel pertama:
```python
import platform

print("Halo dari Google Colab!")
print(f"Sistem Operasi Cloud: {platform.system()} {platform.release()}")
print(f"Versi Python Runtime : {platform.python_version()}")
```
Tekan tombol panah melingkar di samping kiri sel (atau tekan `Shift + Enter`). Colab akan mengalokasikan mesin virtual (status di kanan atas berubah menjadi: *Connecting -> Initializing -> Connected*) dan menampilkan hasil eksekusi tepat di bawah sel.

---

## 4. Menginstal Paket Tambahan dengan `!pip`

Meskipun ratusan pustaka sudah terpasang, jika proyek Anda membutuhkan paket khusus yang belum ada, gunakan tanda seru (`!`) di awal perintah untuk mengeksekusi perintah shell bash di Linux host Colab:

```python
# Menginstal paket visualisasi tambahan
!pip install plotly -q

# Menginstal paket manipulasi telemetri
!pip install rich
```

Tanda `-q` (*quiet*) berguna untuk menyembunyikan log download yang panjang agar dokumen notebook tetap bersih.

---

## 5. Mengunggah Dataset & Menghubungkan Google Drive

### A. Mengunggah File dari Komputer Lokal:
Gunakan modul utilitas bawaan Colab:
```python
from google.colab import files

# Membuka jendela dialog pilih file lokal
uploaded = files.upload()

for filename in uploaded.keys():
    print(f"File {filename} berhasil diunggah ke runtime Colab.")
```

### B. Menghubungkan (Mount) Google Drive:
Karena file yang diunggah lewat cara di atas akan terhapus saat sesi berakhir, menghubungkan Google Drive adalah metode terbaik untuk menyimpan dataset atau model secara permanen:

```python
from google.colab import drive

# Menghubungkan Google Drive Anda ke direktori /content/drive
drive.mount('/content/drive')
```
Colab akan menampilkan pop-up persetujuan otorisasi OAuth:
1. Klik **Connect to Google Drive**.
2. Pilih akun Google Anda dan izinkan akses baca/tulis.
3. Setelah selesai, file Google Drive Anda dapat diakses layaknya folder disk biasa pada path `/content/drive/MyDrive/`.

---

## 6. Realitas Batasan Runtime & Persistensi Data (PENTING)

Banyak pemula salah mengira bahwa disk Google Colab bersifat permanen layaknya hard drive komputer lokal. Pahami batasan berikut:

1. **Penyimpanan Bersifat Ephemeral (Sementara):**
   - Direktori kerja lokal `/content/` akan **dihapus bersih** setiap kali sesi runtime di-reset atau diputuskan.
   - Jangan pernah menyimpan satu-satunya salinan tugas atau dataset penting di folder root `/content/`. Selalu salin ke `/content/drive/MyDrive/` atau download ke laptop Anda.
2. **Idle Timeout (Batas Waktu Diam):**
   - Jika Anda meninggalkan tab Colab tanpa aktivitas eksekusi selama ~60 hingga 90 menit, Google akan memutuskan koneksi (*disconnect*) dan mematikan virtual machine Anda.
3. **Maksimum Session Lifetime (Maksimal Durasi Sesi):**
   - Akun gratis dibatasi maksimal durasi eksekusi terus-menerus selama **12 jam**. Setelah batas ini tercapai, mesin virtual akan di-recycle secara otomatis.
4. **Ketersediaan GPU Bersifat Dinamis (Bukan Kuota Tak Terbatas):**
   - Akses GPU gratis (NVIDIA T4) disediakan berdasarkan ketersediaan dinamis (*best-effort basis*). Google tidak menjamin GPU selalu tersedia setiap saat.
   - Untuk mengubah runtime: Buka menu **Runtime > Change runtime type** -> pilih **T4 GPU** di bawah *Hardware accelerator*.
   - **Etika Penggunaan:** Jika Anda hanya menulis kode dasar logika (Chapter 01–12), gunakan runtime **CPU**. Mengaktifkan GPU saat tidak diperlukan akan menghabiskan kuota harian Anda dengan sia-sia.

---

## 7. Menyimpan dan Membagikan Notebook

1. **Simpan ke GitHub:** Klik menu **File > Save a copy in GitHub...**. Colab memungkinkan Anda langsung melakukan git commit ke repositori pribadi atau organisasi Anda.
2. **Unduh ke Laptop:** Klik menu **File > Download > Download .ipynb** (format notebook) atau **Download .py** (format skrip Python biasa).
3. **Berbagi Tautan (Share Link):** Klik tombol **Share** di pojok kanan atas, atur izin akses (*Anyone with the link can view/comment*), dan bagikan tautan kepada rekan belajar atau instruktur Anda.

---

## 8. Referensi Resmi

- Google Colaboratory: [Frequently Asked Questions (FAQ)](https://research.google.com/colaboratory/faq.html)
- Google Colaboratory: [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
- Google Colaboratory Resource Limits Guide: [Colab Free vs Paid Tiers](https://colab.research.google.com/signup)

