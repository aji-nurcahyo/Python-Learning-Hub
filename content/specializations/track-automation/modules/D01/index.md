# Modul D01: File System Automation with `pathlib` & `shutil`

## 1. Mengapa `pathlib.Path` Menggantikan `os.path`?
Menggabungkan jalur folder dengan string (`folder + "\\" + nama`) sering patah antara Windows dan Linux. **`pathlib.Path`** menyediakan operator `/` yang portabel lintas sistem operasi serta API berorientasi objek yang sangat ekspresif:
- `p.suffix.lower()`: membaca ekstensi file (`.csv`, `.pdf`).
- `p.stat().st_size`: membaca ukuran byte berkas.
- `p.rglob("*")`: menelusuri seluruh subdirektori secara rekursif.

---

## 2. Pola Keselamatan Wajib: `--dry-run`
Skrip pengelola berkas yang keliru menarget folder bisa menghapus ratusan dokumen kerja dalam sedetik. Oleh karena itu:
1. Pisahkan fase **perencanaan** (`plan = [(src, dst), ...]`) dari fase **eksekusi** (`shutil.move`).
2. Berikan parameter default **`dry_run: bool = True`** agar pengguna melihat daftar perubahan secara aman sebelum mengeksekusinya.

---

## 3. Deteksi Duplikat Berbasis SHA-256 Chunk Reader
Dua file dengan nama berbeda (`laporan_final.csv` dan `salinan.csv`) bisa memiliki isi byte persis sama. Menggunakan **SHA-256** per blok 64 KB (`chunk = f.read(65536)`) memungkinkan pemeriksaan file berukuran ratusan megabyte tanpa memakan RAM berlebih.

---

## 4. Arsip Backup & Kebijakan Rotasi (`keep=N`)
Membuat cadangan berkas tiap hari tanpa batas lama-kelamaan memenuhi kapasitas disk. Gabungkan `zipfile.ZipFile(..., compression=zipfile.ZIP_DEFLATED)` dengan penyortiran berdasarkan nama/waktu untuk otomatis menghapus arsip terlama di luar jumlah retensi `keep=3`.

