# Tugas Praktik: Pipeline Pemrosesan Data Telemetri Skala Besar (Chapter 24)

## Deskripsi Tugas
Dalam tugas ini, Anda diminta mengembangkan **Streaming Telemetry Ingestion Engine** yang mampu membaca, memvalidasi, memfilter, dan mentransformasikan aliran data pengukuran jaringan secara streaming (hemat memori) dengan menerapkan:
1. **Decorator**: Validasi parameter dan pengukuran kinerja runtime.
2. **Generators**: Pipeline pengolahan data multi-tahap tanpa memuat seluruh rekaman ke memori RAM sekaligus.
3. **Context Managers**: Manajemen resource kanal dan pencatatan metrik eksekusi yang aman terhadap crash.

---

## Ketentuan & Persyaratan Arsitektur
1. **Decorator Lapisan Pemantauan (`@telemetry_audit` & `@enforce_range`):**
   - `@telemetry_audit`: Menggunakan `functools.wraps` untuk mengukur durasi pemrosesan dan mencatat nama fungsi.
   - `@enforce_range(param_name, min_val, max_val)`: Memastikan nilai numerik tidak melebihi batas legal toleransi.
2. **Streaming Generator Pipeline:**
   - Tahap 1: `stream_records(raw_source)` — Mengalirkan data satu per satu (`yield`).
   - Tahap 2: `filter_outliers(stream, min_snr, max_snr)` — Menyaring data derau di luar rentang valid.
   - Tahap 3: `aggregate_signal_metrics(stream, window_size)` — Mengelompokkan data per jendela waktu tanpa merusak aliran lazy evaluation.
3. **Context Manager Resource Management (`ChannelLeaseContext`):**
   - Mengelola alokasi spektrum frekuensi sementara dengan implementasi protokol `__enter__` dan `__exit__`.
   - Menjamin bahwa kanal frekuensi selalu dilepaskan (*deallocated*) kembali ke pool terlepas dari keberhasilan atau kegagalan transaksi di dalam blok `with`.

---

## Rubrik Penilaian (Total: 100 Poin)

| Komponen Penilaian | Bobot | Kriteria Evaluasi |
|:---|:---:|:---|
| **1. Kualitas & Preservasi Decorator** | 25 Poin | Menerapkan `functools.wraps`, menangani `*args` dan `**kwargs` dengan benar, validasi parameter melempar exception tepat sasaran. |
| **2. Efisiensi Generator Pipeline** | 25 Poin | Menggunakan `yield` murni tanpa konversi ke list/array intermediate, chaining antar generator berjalan mulus. |
| **3. Manajemen Sumber Daya Context Manager** | 25 Poin | Protokol `__enter__` dan `__exit__` menangani pembebasan resource secara deterministik dan aman terhadap exception. |
| **4. Integrasi Pipeline Terpadu** | 15 Poin | Aliran data dari generator melewati fungsi berdekorator di dalam context manager berjalan tanpa error. |
| **5. Dokumentasi & Type Annotations** | 10 Poin | Kode terstruktur rapi, type annotations lengkap, dan mengikuti panduan bahasa teknis. |

