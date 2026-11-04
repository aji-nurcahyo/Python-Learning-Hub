# Tugas Praktik Chapter 14: Dataset Transformation Toolkit

## Deskripsi Tugas
Dalam analisis jaringan telekomunikasi dan pemrosesan data IoT (*Internet of Things*), insinyur perangkat lunak sering kali harus membersihkan, menata ulang format, memfilter anomali, dan mengonversi ribuan log perangkat keras secara efisien tanpa membebani memori kerja (RAM).

Anda diminta melengkapi pustaka utilitas pemrosesan data fungsional pada berkas `tugas_14.py` dengan memanfaatkan seluruh kemampuan koleksi ekspresif Python:
1. **List Comprehensions:** Transformasi dan penyaringan data sinyal biner/skalar.
2. **Dictionary Comprehensions:** Pembentukan tabel indeks asosiatif dan agregasi terkelompok.
3. **Set Comprehensions:** Deduplikasi otomatis dan isolasi kategori unik.
4. **Nested Comprehensions:** Perataan matriks spasial multi-dimensi.
5. **Generator Expressions:** Pemrosesan aliran data *streaming* berukuran masif dengan evaluasi *lazy*.

---

## Petunjuk Pengerjaan

1. Buka berkas starter code `tugas_14.py`.
2. Lengkapi fungsi `saring_dan_skala(data_log, ambang_min)` menggunakan *list comprehension*.
3. Lengkapi fungsi `buat_indeks_perangkat(daftar_perangkat)` menggunakan *dict comprehension*.
4. Lengkapi fungsi `isolasi_zona_aktif(daftar_perangkat)` menggunakan *set comprehension*.
5. Lengkapi fungsi `ratakan_topologi_matriks(grid_matriks)` menggunakan *nested list comprehension*.
6. Lengkapi fungsi `aliran_daya_generator(aliran_data)` menggunakan *generator expression*.
7. Jalankan berkas untuk memverifikasi seluruh keluaran terminal.

---

## Format Laporan Konsol Terminal

```text
======================================================================
           DATASET TRANSFORMATION TOOLKIT (ENGINE 14)
======================================================================
1. Pemfilteran Daya & Skala Gain:
   Total data awal: 6 -> 4 perangkat memenuhi syarat (> 30.0 mW)
   Data tersaring : [{'id': 'N1', 'daya': 52.8}, {'id': 'N2', 'daya': 105.6}, ...]

2. Peta Indeks Asosiatif (Dict Comprehension):
   Peta IP -> Hostname:
   - 10.0.0.1  : Router-Pusat
   - 10.0.0.2  : Switch-Utara

3. Deduplikasi Zona Unik (Set Comprehension):
   Zona Terdeteksi : {'Inti', 'Akses', 'Distribusi'}

4. Perataan Matriks Grid 3x3 (Nested Comprehension):
   Hasil Flattening: [10, 20, 30, 40, 50, 60, 70, 80, 90]

5. Evaluasi Lazy Generator (Memory-Safe Streaming):
   Konsumsi 3 data pertama dari stream: [15.0, 30.0, 45.0]
   Semua transformasi data sukses dijalankan secara ekspresif.
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Capaian Kualitas |
|:---|:---:|:---|
| **1. Penguasaan List & Nested Comprehensions** | 25 Poin | Menerapkan list comprehension dan nested flattening secara presisi tanpa loop manual imperatif. |
| **2. Penguasaan Dict & Set Comprehensions** | 25 Poin | Mampu menginversi dan membangun mapping kamus serta deduplikasi himpunan unik secara bersih. |
| **3. Protokol Iterator & Generator Expression** | 25 Poin | Menerapkan generator expression bertipe lazy, memahami interaksi `iter()`, `next()`, dan efisiensi memori RAM. |
| **4. Pemanfaatan Enumerate, Zip & Standar PEP 8** | 25 Poin | Menggunakan `enumerate()` dan `zip()` secara idiomatis, kode memiliki type hints lengkap, dan format rapi. |
