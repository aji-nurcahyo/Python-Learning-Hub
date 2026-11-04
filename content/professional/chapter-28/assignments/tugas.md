# Tugas Mini Project: REST API Data Client

**Chapter 28: Networking & API Integration**  
**Tingkat:** Level 3 — Professional Python Engineering  
**Platform:** Python Learning Hub  
**Institusi:** Institut Teknologi Sumatera (ITERA)  

---

## 1. Deskripsi Tugas

Dalam arsitektur *microservices* dan sistem telekomunikasi terdistribusi, aplikasi Python sering bertindak sebagai *API consumer* yang bertugas mengonsumsi data telemetri, status simpul jaringan, dan metrik performa dari server REST API eksternal.

Tugas Anda adalah merancang dan mengimplementasikan modul **`ProductionApiClient`** yang andal di dalam file `tugas.py`. Klien ini harus memenuhi standar perangkat lunak tingkat produksi (*production-grade*):
1. **Autentikasi Aman:** Mengambil *token* dari *environment variables* tanpa *hardcoded credentials*, serta menyamarkan token pada log sistem.
2. **Kepatuhan Protokol HTTP:** Mengirim request `GET` dan `POST` dengan *headers* standar (`Content-Type`, `Accept`, `User-Agent`).
3. **Paginasi Otomatis:** Menjelajahi (*traversing*) seluruh halaman data secara sistematis hingga tuntas.
4. **Ketahanan Jaringan (Fault Tolerance):** Menerapkan strategi *exponential backoff retry* untuk menghadapi kegagalan sementara (*transient faults* seperti HTTP 503 / 429).
5. **Validasi Skema Respon:** Memeriksa struktur JSON secara defensif untuk mencegah `KeyError` atau crash pada aplikasi.

---

## 2. Diagram Arsitektur REST API Data Client

```
  ┌───────────────────────────────────────────────────────────────┐
  │                   ProductionApiClient                         │
  │                                                               │
  │  ┌────────────────────┐    ┌───────────────────────────────┐  │
  │  │  os.environ.get()  │    │   Header Sanitizer (Masking)  │  │
  │  │  (Token Injection) │    │   (Safe Log Auditing)         │  │
  │  └─────────┬──────────┘    └───────────────▲───────────────┘  │
  │            │                               │                  │
  │  ┌─────────▼───────────────────────────────┴───────────────┐  │
  │  │   Request Engine: GET / POST with Timeout & Backoff     │  │
  │  └────────────────────────┬────────────────────────────────┘  │
  └───────────────────────────┼───────────────────────────────────┘
                              │ HTTP Requests (JSON)
                              ▼
  ┌───────────────────────────────────────────────────────────────┐
  │                 Mock Telecom REST API Server                  │
  │                                                               │
  │  - GET  /api/v1/nodes?page=N&limit=M   (Status 200 OK)        │
  │  - POST /api/v1/metrics                (Status 201 Created)   │
  │  - Transient Errors                    (Status 503 Backoff)   │
  └───────────────────────────────────────────────────────────────┘
```

---

## 3. Persyaratan Fungsional Modul

Modul wajib diimplementasikan di dalam file `tugas.py` dengan method-method berikut:

1. **Inisialisasi & Konfigurasi:**
   - Membaca token dari environment variable atau parameter fallback yang aman.
   - Mengonfigurasi `timeout` bawaan (misalnya 3.0 detik).
2. **`mask_token(headers: dict) -> dict`:**
   - Menyamarkan nilai Bearer token agar hanya menyisakan beberapa karakter awal dan akhir.
3. **`get_paginated_nodes(endpoint: str, limit: int = 2) -> list[dict]`:**
   - Mengambil seluruh record dari endpoint secara iteratif hingga flag `has_next` bernilai `False`.
4. **`post_metric_record(endpoint: str, payload: dict) -> dict`:**
   - Memvalidasi isi payload dan mengirimkannya via HTTP POST.
5. **`fetch_with_backoff(endpoint: str, max_retries: int = 3) -> dict`:**
   - Mengirim request dengan retry dan jeda eksponensial saat menerima status kode 503 atau 429.

---

## 4. Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi |
| :--- | :---: | :--- |
| **Autentikasi & Log Sanitization** | 20 Poin | Manajemen Bearer token melalui variabel lingkungan dan penyamaran token yang aman saat audit log. |
| **Penanganan Paginasi API** | 25 Poin | Kemampuan mengonsumsi seluruh halaman dataset terpaginasi secara komprehensif tanpa data terpotong. |
| **Exponential Backoff Retry** | 25 Poin | Algoritma pengulangan cerdas dengan pertambahan jeda (delay multiplier) untuk mengatasi *transient errors*. |
| **Kepatuhan Payload & HTTP Method** | 15 Poin | Format payload POST JSON yang tepat, pemeriksaan status kode (200, 201, 401, 503), dan validasi defensif. |
| **Kerapian Kode & Type Hints** | 15 Poin | Menerapkan type hints lengkap, modularitas class yang bersih, dan standar dokumentasi PEP 8. |

---

## 5. Cara Pengujian

Jalankan skrip pengujian mandiri:
```bash
python tugas.py
```
Pastikan seluruh validasi status kode dan asersi paginasi lulus 100% tanpa error jaringan yang tidak tertangani.
