# Chapter 17: File Handling & Data Serialization

Selamat datang di **Chapter 17: File Handling & Data Serialization**. Pada modul ini, kita melangkah dari program yang hanya menyimpan data sementara di memori RAM (*volatile memory*) menuju sistem yang mampu membaca, memvalidasi, dan menyimpan data secara persisten ke media penyimpanan lokal. Kita akan mempelajari penanganan berkas teks, pemrosesan berkas tabular CSV, serialisasi data hierarkis JSON, serta manipulasi path modern menggunakan pustaka standar `pathlib`.

---

## 1. Pendahuluan: Mengapa File Handling Penting?

Dalam rekayasa perangkat lunak dan sistem telekomunikasi nyata, data tidak diketik manual ke dalam kode program. Konfigurasi server dimuat dari berkas JSON, riwayat sinyal telemetri diekspor ke berkas CSV, dan rekaman aktivitas sistem ditulis ke dalam berkas log teks.

`file handling` yang baik harus menjamin tiga pilar utama:
1. **Keamanan Sumber Daya (*Resource Safety*):** Setiap *file descriptor* yang dibuka oleh sistem operasi harus ditutup kembali secara andal guna mencegah *resource leak*.
2. **Integritas Karakter (*Encoding Consistency*):** Menggunakan standar UTF-8 agar teks dapat dibaca lintas platform tanpa galat translasi biner.
3. **Ketahanan Terhadap Kesalahan (*Defensive I/O*):** Mampu mengantisipasi berkas yang hilang (*missing files*), izin akses ditolak (*permission error*), atau data yang korup.

---

## 2. Siklus Hidup File & Mode Akses Berkas

Siklus hidup interaksi berkas pada Python melibatkan tiga tahapan:
1. **Membuka Berkas (`open`):** Sistem operasi memeriksa keberadaan berkas, alokasi buffer memori, dan memberikan penunjuk berkas (*file pointer*).
2. **Operasi I/O (`read` / `write`):** Membaca byte/teks atau menulis byte/teks ke buffer media penyimpanan.
3. **Menutup Berkas (`close`):** Mengosongkan buffer (*flush*) ke disk dan membebaskan *file descriptor*.

### Tabel Mode Akses Berkas pada Fungsi `open()`

| Mode | Nama Operasi | Perilaku terhadap Berkas yang Sudah Ada | Perilaku jika Berkas Belum Ada |
| :---: | :--- | :--- | :--- |
| **`'r'`** | Read Only (Default) | Membaca dari awal berkas; tidak dapat menulis. | Memicu runtime exception `FileNotFoundError`. |
| **`'w'`** | Write Only | **Menimpa bersih (*truncate*)** seluruh konten yang ada. | Membuat berkas baru secara otomatis. |
| **`'a'`** | Append Only | Menulis data tambahan di posisi paling akhir berkas. | Membuat berkas baru secara otomatis. |
| **`'x'`** | Exclusive Creation | Memicu runtime exception `FileExistsError`. | Membuat berkas baru secara eksklusif. |
| **`'r+'`**| Read & Write | Mengizinkan baca dan tulis tanpa menghapus berkas di awal. | Memicu runtime exception `FileNotFoundError`. |

Tambahkan karakter `'t'` (mode teks, default) atau `'b'` (mode biner untuk audio/gambar/arsip).

---

## 3. Context Manager dengan Statement `with`

Di masa lalu, developer menutup berkas menggunakan blok `try-finally`:

```python
# Pola lama yang rawan kesalahan
f = open("data.txt", "r", encoding="utf-8")
try:
    konten = f.read()
finally:
    f.close()
```

Python modern menyediakan **context manager** menggunakan statement `with`. Pola ini mengimplementasikan protokol manajemen konteks (`__enter__` dan `__exit__`), menjamin berkas otomatis ditutup seketika saat alur keluar dari blok `with`, bahkan jika terjadi exception:

```python
# Pola modern yang direkomendasikan
with open("data.txt", "r", encoding="utf-8") as f:
    konten = f.read()
# Di sini f sudah tertutup sempurna secara otomatis
```

---

## 4. Membaca dan Menulis Berkas Teks

### A. Strategi Membaca File Teks
- `f.read()`: Membaca seluruh isi berkas ke dalam satu variabel `string`. Efektif untuk berkas berukuran kecil.
- `f.readline()`: Membaca satu baris tunggal hingga menemukan karakter newline (`\n`).
- `for baris in f:`: **Pola paling efisien memori.** Objek berkas bertindak sebagai `iterator` yang melakukan streaming baris demi baris secara *lazy*, sangat hemat memori bahkan untuk berkas berukuran gigabyte.

### B. Menulis dan Menambahkan Baris Teks
Gunakan `f.write(teks)` untuk menulis string tunggal, atau `f.writelines(daftar_string)` untuk menulis kumpulan string:

```python
catatan_log = [
    "2026-11-04 08:00:00 Inisialisasi node berhasil\n",
    "2026-11-04 08:00:05 Transmisi paket daya 20 dBm\n"
]
with open("gateway.log", "a", encoding="utf-8") as f:
    f.writelines(catatan_log)
```

---

## 5. Pemrosesan Data Tabular dengan Format CSV

Format **Comma-Separated Values (CSV)** adalah standar paling populer untuk mengekspor data tabel antar basis data dan aplikasi analisis.

### Aturan Emas Pembacaan & Penulisan CSV di Python
1. Selalu sertakan `newline=""` saat memanggil `open()` untuk berkas CSV. Jika diabaikan, sistem operasi Windows dapat menyisipkan baris kosong tambahan di antara tiap baris rekaman.
2. Selalu tentukan `encoding="utf-8"`.

### Memanfaatkan `csv.DictReader` dan `csv.DictWriter`
Daripada mengandalkan indeks angka kolom (`row[0]`, `row[1]`) yang rapuh jika urutan kolom berubah, gunakan `csv.DictReader` yang otomatis memetakan setiap baris menjadi objek `dictionary` Python:

```python
import csv

with open("stasiun_bts.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Mengakses data menggunakan nama key kolom
        print(f"BTS ID: {row['id']} | Lokasi: {row['lokasi']}")
```

---

## 6. Serialisasi Data dengan Format JSON

**JavaScript Object Notation (JSON)** adalah format berbasis teks yang ringan dan menjadi standar utama untuk pertukaran data pada REST API, konfigurasi aplikasi, dan penyimpanan dokumen NoSQL.

### Pemetaan Tipe Data Python dan JSON

| Tipe Data Python | Format JSON |
| :--- | :--- |
| `dict` | Object (`{ "key": "value" }`) |
| `list`, `tuple` | Array (`[ 1, 2, 3 ]`) |
| `str` | String (`"teks"`) |
| `int`, `float` | Number (`42`, `3.14`) |
| `True` / `False` | Boolean (`true` / `false`) |
| `None` | Null (`null`) |

### Empat Fungsi Inti Modul `json`:
- **Serialisasi (Python Object ke JSON):**
  - `json.dumps(obj, indent=2)`: Menghasilkan representasi `string` JSON di memori RAM.
  - `json.dump(obj, file_stream, indent=2)`: Menuliskan data JSON langsung ke berkas fisik.
- **Deserialisasi (JSON ke Python Object):**
  - `json.loads(string_json)`: Mengonversi `string` JSON mentah menjadi `dictionary` atau `list` Python.
  - `json.load(file_stream)`: Membaca berkas JSON dari disk dan mem-parsing isinya menjadi objek Python.

---

## 7. Manajemen Path Modern dengan `pathlib.Path`

Modul `os.path` lama yang berbasis manipulasi string telah digantikan oleh `pathlib` yang berorientasi objek (PEP 428). 

Keunggulan utama `pathlib.Path`:
- Sintaksis operator slash (`/`) intuitif untuk menggabungkan sub-direktori: `folder / "laporan.json"`.
- Metode bawaan lengkap: `.exists()`, `.is_file()`, `.mkdir(parents=True, exist_ok=True)`, `.unlink()`.
- Metode baca-tulis ringkas: `path.read_text(encoding="utf-8")` dan `path.write_text(teks, encoding="utf-8")`.

---

## 8. Proyek Terapan: Telemetry CSV & JSON Data Manager

Sebagai penerapan integratif dari seluruh konsep di atas, modul ini menyediakan mini proyek `TelemetryDataManager` di folder `content/intermediate/chapter-17/code/data_manager.py`:
- Memuat dataset rekaman BTS dari file CSV lokal.
- Memvalidasi kelengkapan field wajib dan tipe data numerik.
- Mendukung pembaruan rekaman secara dinamis.
- Menghitung agregasi statistik metrik telemetri.
- Mengekspor dataset yang tervalidasi ke dalam berkas JSON berstruktur bersih.

---

## 9. Referensi Pembelajaran

1. **Python Software Foundation.** *Reading and Writing Files*. https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
2. **Python Software Foundation.** *csv — CSV File Reading and Writing*. https://docs.python.org/3/library/csv.html
3. **Python Software Foundation.** *json — JSON encoder and decoder*. https://docs.python.org/3/library/json.html
4. **Python Software Foundation.** *pathlib — Object-oriented filesystem paths*. https://docs.python.org/3/library/pathlib.html
5. **Harvard CS50P.** *File I/O — Week 6*. https://cs50.harvard.edu/python/
