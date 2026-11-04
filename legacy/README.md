# Pengenalan Komputasi — Python (Materi Perkuliahan)

Situs materi berbasis **GitHub Pages + Reveal.js**, disusun sebagai proyek terpisah dengan konsep navigasi serupa dari [informatika-itera/pengkom](https://github.com/informatika-itera/pengkom). Tidak mengubah atau mengklaim kepemilikan repository sumber.

## Status materi
- Pertemuan 1–8: placeholder (belum ada materi).
- Pertemuan 9: Review Python; function design; module dan docstring (slide HTML, kode Python, tugas).
- Pertemuan 10: List, tuple, dictionary, set, comprehension, searching, sorting (slide HTML, kode Python, tugas).
- Pertemuan 11–16: placeholder (belum ada materi).

## Menjalankan situs secara lokal

Jalankan dari direktori repository:

```bash
python -m http.server 8000
```

Buka `http://localhost:8000` di browser. Slide menggunakan **Reveal.js 5.2.1 dari CDN**; akses internet dibutuhkan untuk memuat pustaka slide. Halaman tugas menggunakan marked.js dari CDN.

## Menjalankan contoh kode

```bash
python pertemuan-09/contoh.py
python pertemuan-10/contoh.py
```

Kode menggunakan pustaka standar Python, tanpa dependencies tambahan.

## Publikasi GitHub Pages
1. Buat repository **public** baru di akun GitHub milik Anda.
2. Unggah seluruh isi folder ini ke branch `main`.
3. Buka `Settings → Pages → Build and deployment`.
4. Pada `Source`, pilih `Deploy from a branch`, `main`, folder `/ (root)` lalu Save.
5. Situs akan tersedia di `https://USERNAME.github.io/NAMA-REPO/` setelah deployment selesai.

Tidak ada perintah push otomatis; publikasi dilakukan setelah pemilik repository memutuskan nama dan lokasinya.

## Menambahkan pertemuan berikutnya
Ganti konten `pertemuan-XX/index.html` dan ubah kartu pada `index.html` menjadi aktif serta tambahkan link tugas/kode. Sebaiknya gunakan format folder seperti Pertemuan 9–10 untuk konsistensi.

## Atribusi
Desain dan slide pada repository ini merupakan implementasi baru yang **terinspirasi** dari portal [Pengkom Informatika ITERA](https://informatika-itera.github.io/pengkom/), yang menggunakan Reveal.js. Materi, kode, serta tugas Pertemuan 9–10 adalah konten baru. Untuk menyalin aset asli atau logo dari upstream, ikuti lisensi dan atribusi repository sumber.
