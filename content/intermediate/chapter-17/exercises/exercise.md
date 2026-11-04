# Latihan Terarah: Chapter 17 — File Handling & Data Serialization

Selamat datang di lembar latihan terarah **Chapter 17**. Kerjakan 4 latihan terstruktur berikut untuk memperdalam penguasaan pembacaan berkas, parsing format CSV, serta serialisasi data JSON.

---

### Latihan 1: Ekstraksi Log Frekuensi & Level Peringatan (Text I/O)
**Tujuan:** Menggunakan context manager `with` untuk memfilter baris log secara selektif.

1. Buat berkas teks `jaringan.log` yang memuat baris-baris log dengan format:
   ```text
   [INFO] Inisialisasi kanal frekuensi 2412 MHz sukses
   [WARN] Deteksi interferensi tinggi pada kanal 5180 MHz
   [INFO] Status node sinkron
   [ERROR] Gagal menyambung ke gateway utama
   ```
2. Tulis fungsi `ekstrak_peringatan(nama_file: str) -> list[str]` yang hanya mengambil baris yang memiliki level `[WARN]` atau `[ERROR]`.
3. Simpan baris-baris peringatan tersebut ke dalam berkas baru `peringatan_jaringan.txt`.

---

### Latihan 2: Tabulasi Metrik BTS dengan CSV DictWriter
**Tujuan:** Menulis kumpulan data dictionary ke dalam format CSV ber-header secara terstruktur.

1. Diberikan list data pemancar seluler:
   ```python
   pemancar = [
       {"id": "TX-01", "lokasi": "Kampus ITERA", "daya_w": 25.0},
       {"id": "TX-02", "lokasi": "Way Huwi", "daya_w": 30.0},
       {"id": "TX-03", "lokasi": "Sukarame", "daya_w": 20.5},
   ]
   ```
2. Gunakan `csv.DictWriter` dengan parameter `newline=""` dan `encoding="utf-8"` untuk menyimpan data ke file `pemancar.csv`.
3. Pastikan header `id,lokasi,daya_w` tertulis di baris pertama.

---

### Latihan 3: Konversi Payload Sensor CSV ke Dokumen JSON
**Tujuan:** Menghubungkan pembacaan CSV dengan serialisasi JSON terindentasi rapi.

1. Buat file `sensor_suhu.csv` dengan kolom `sensor_id,suhu_celsius,status`.
2. Baca berkas tersebut menggunakan `csv.DictReader`, lakukan konversi `suhu_celsius` ke tipe data float.
3. Simpan data yang telah tervalidasi ke dalam berkas `sensor_suhu.json` menggunakan `json.dump(..., indent=4)`.

---

### Latihan 4: Manajemen Direktori Proyek dengan `pathlib.Path`
**Tujuan:** Memanfaatkan library modern `pathlib` untuk membuat pohon direktori dan mengelola ekstensi berkas.

1. Gunakan `Path("arsip_telemetri") / "2026" / "november"` untuk membuat struktur folder bertingkat (`mkdir(parents=True, exist_ok=True)`).
2. Buat tiga file dummy berformat teks (`log_01.txt`, `log_02.txt`, `data.csv`) di dalam folder tersebut.
3. Gunakan metode `Path.glob("*.txt")` untuk mencari dan mencetak seluruh nama berkas teks yang ada di dalam direktori tersebut beserta ukuran byte masing-masing.

---

> [!TIP]
> Selalu pastikan menggunakan `encoding="utf-8"` pada saat membuka file teks di sistem operasi Windows guna menghindari galat translasi karakter lokal (`cp1252`).
