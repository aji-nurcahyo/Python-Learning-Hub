# Tugas Pertemuan 9 — Function Design, Module & Docstring

## Tujuan
Mengembangkan program yang modular dan dapat diuji untuk mengolah data sinyal sederhana.

## Instruksi
1. Buat dua berkas: `olah_sinyal.py` (modul) dan `main.py` (program pemanggil).
2. Buat fungsi `rata_rata(data)`, `nilai_tertinggi(data)`, `nilai_terendah(data)`, dan `kategori_rsrp(rsrp)`; gunakan `return`, bukan hanya `print`.
3. Data pengukuran minimal 8 nilai RSRP. Untuk list kosong, fungsi statistik mengembalikan `None`.
4. Tambahkan docstring pada setiap fungsi dan sekurangnya lima pengujian `assert`.
5. Klasifikasi ilustratif: baik >= -90 dBm, sedang -105 sampai kurang dari -90 dBm, buruk < -105 dBm.

## Pengumpulan
Unggah `olah_sinyal.py`, `main.py`, tangkapan layar output, dan README singkat berisi cara menjalankan serta penjelasan masing-masing fungsi.

## Rubrik
- Kebenaran output dan penanganan data kosong: 40%
- Fungsi modular, parameter, dan `return`: 25%
- Docstring dan keterbacaan: 15%
- Minimal 5 `assert`: 15%
- Kelengkapan berkas: 5%
