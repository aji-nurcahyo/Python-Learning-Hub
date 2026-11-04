# Tugas Praktik Chapter 13: Flexible Telemetry Pipeline Engine

## Deskripsi Tugas
Dalam stasiun pemancar dan infrastruktur jaringan cerdas, aliran data telemetri (suhu perangkat keras, konsumsi arus listrik, daya RF, dan rasio paket hilang) harus diolah melalui rantai pemrosesan data (*data processing pipeline*) yang fleksibel.

Anda diminta merancang arsitektur mesin pemroses data fungsional modular pada berkas `tugas_13.py` yang menerapkan teknik-teknik fungsi tingkat lanjut Python:
1. **Higher-Order Pipeline Execution:** Fungsi yang menerima serangkaian fungsi transformasi (`*transforms`) dan mengeksekusinya secara berurutan (*function chaining*).
2. **Predicate Filter Closure:** Fungsi pabrik (*closure*) yang mengunci ambang batas toleransi dan mengembalikan fungsi penyaring (*predicate function*).
3. **Dynamic Aggregator:** Fungsi ringkasan statistik yang dapat menerima argumen kata kunci bervariasi (`**kwargs`) untuk mengevaluasi metrik kustom di masa depan.
4. **Keyword-Only & Positional-Only Constraints:** Penataan parameter fungsi secara ketat menggunakan pembatas `/` dan `*` untuk mencegah kerancuan pemanggilan antarmuka program.

---

## Petunjuk Pengerjaan

1. Buka berkas starter code `tugas_13.py`.
2. Lengkapi fungsi pabrik `buat_filter_rentang(min_val, max_val)` sebagai *closure*.
3. Lengkapi fungsi higher-order `jalankan_pipeline(data, *transforms, filter_kustom=None)`.
4. Lengkapi fungsi agregator `analisis_telemetri(data, /, unit="mW", **kalkulator_tambahan)`.
5. Uji program Anda dengan dataset sampel telemetri sensor:
   `[15.2, 48.0, 102.5, 7.8, 64.0, 95.2, 33.1]`
6. Pastikan tidak ada galat *mutable default arguments* dan semua fungsi memiliki tipe petunjuk (*type hints*) serta *docstrings*.

---

## Format Laporan Konsol Terminal

```text
======================================================================
               MESIN PIPELINE TELEMETRI CERDAS (ENGINE 13)
======================================================================
Dataset Awal : [15.2, 48.0, 102.5, 7.8, 64.0, 95.2, 33.1]

--- Tahap 1: Pemfilteran Ambang Normal [10.0 - 100.0] ---
Data Tersaring : [15.2, 48.0, 7.8 (Ditolak), 102.5 (Ditolak)] -> 5 Sampel Valid

--- Tahap 2: Transformasi Berantai (Kompensasi Gain & Kalibrasi) ---
Hasil Pipeline : [18.24, 57.6, 76.8, 114.24, 39.72]

--- Tahap 3: Ringkasan Analitik (*args & **kwargs) ---
Total Sampel   : 5
Unit Daya      : mW
Rata-Rata      : 61.32 mW
Nilai Minimum  : 18.24 mW
Nilai Maksimum : 114.24 mW
Rentang Dinamis: 96.00 mW (Metrik Kustom **kwargs)
Status Sistem  : NORMAL
======================================================================
```

---

## Rubrik Penilaian (Total Bobot: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Capaian Kualitas |
|:---|:---:|:---|
| **1. Desain Higher-Order & Pipeline Chaining** | 30 Poin | Fungsi pipeline mampu menerima `*transforms` fleksibel dan mengeksekusi transformasi data berantai secara presisi. |
| **2. Implementasi Closure & Lexical Scope** | 25 Poin | Fungsi pembuat filter bekerja sebagai closure murni tanpa variabel global, mempertahankan state ambang batas secara independen. |
| **3. Pemanfaatan *args, **kwargs & Parameter Constraints** | 25 Poin | Menerapkan `*args`, `**kwargs`, serta pembatas `/` dan `*` secara tepat sesuai kaidah PEP 570 dan PEP 3102. |
| **4. Kebersihan Kode, Type Hints & Zero-Bug Mutable Default** | 20 Poin | Menggunakan sentinel `None` untuk parameter list opsional, menyertakan type hints lengkap, docstring standar, dan formatting PEP 8. |

