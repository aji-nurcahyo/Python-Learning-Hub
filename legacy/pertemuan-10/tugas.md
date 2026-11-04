# Tugas Pertemuan 10 — Mini Proyek Pengolahan Data Sinyal

## Tujuan
Memanfaatkan struktur data Python, comprehension, searching, sorting dan modul fungsi.

## Instruksi
1. Siapkan **minimal 10 record sensor** berupa dictionary dengan `id`, `lokasi`, dan `rsrp` yang disimpan dalam list.
2. Gunakan **tuple** untuk menyimpan salah satu data koordinat `(latitude, longitude)`.
3. Gunakan **set** untuk memperoleh daftar lokasi unik.
4. Buat **minimal dua comprehension**; salah satunya memfilter RSRP di bawah -100 dBm.
5. Buat fungsi **linear search** berdasarkan ID sensor; kembalikan `None` bila tidak ditemukan.
6. Urutkan sensor dari RSRP terbesar ke terkecil dengan `sorted(..., key=..., reverse=True)`.
7. Hitung jumlah, rata-rata, RSRP minimum, dan maksimum.
8. Impor dan gunakan minimal satu fungsi dari modul yang dibuat pada Pertemuan 9.

## Pengumpulan
Unggah seluruh file `.py` yang diperlukan, `README.md` dengan cara menjalankan, dan tangkapan layar hasil.

## Rubrik
- Ketepatan pengolahan dan hasil: 35%
- Struktur data dan comprehension: 25%
- Searching dan sorting: 20%
- Modularitas, dokumentasi: 15%
- Kelengkapan berkas: 5%
