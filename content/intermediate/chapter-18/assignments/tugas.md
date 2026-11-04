# Tugas Praktik 18: Telecom Anomaly Detection & Robust Validator Suite
## Python Learning Hub — Level 2: Intermediate

---

### Deskripsi Tugas

Dalam pemrosesan data telekomunikasi berkecepatan tinggi, kegagalan satu baris sensor tidak boleh meruntuhkan (*crash*) seluruh pipeline pemantauan jaringan. Sebagai Software Engineer, Anda ditugaskan untuk merancang modul **Robust Telemetry Record Validator** yang mampu menerima kumpulan data mentah, memvalidasi aturan fisis jaringan, mencatat aktivitas anomali dengan modul `logging`, serta memberikan laporan diagnostik komprehensif.

---

### Persyaratan Fungsional & Teknis

1. **Struktur Exception Khusus (Custom Hierarchy):**
   - Bangun kelas dasar `TelemetryValidationError(Exception)`.
   - Turunkan kelas khusus `MissingPropertyError` (jika field wajib hilang).
   - Turunkan kelas khusus `ValueRangeError` (jika nilai di luar rentang wajar: frekuensi $100-6000\text{ MHz}$, daya $-140 \text{ s.d. } 50\text{ dBm}$, latensi $> 0\text{ ms}$).
2. **Penanganan Multi-Exception yang Bersih:**
   - Dilarang keras menggunakan bare `except:` atau `except Exception:` yang menelan seluruh error secara diam-diam (*silent swallowing*).
   - Tangkap exception secara spesifik (`ValueError`, `KeyError`, `TypeError`, dan custom exceptions).
3. **Pencatatan Audit dengan Modul `logging`:**
   - Gunakan `logging.info()` untuk mencatat rekaman yang sukses divalidasi.
   - Gunakan `logging.warning()` saat rekaman ditolak karena melanggar aturan rentang nilai.
   - Gunakan `logging.error()` saat terjadi kegagalan format kritis atau payload rusak.
4. **Metrik & Pelaporan Evaluasi:**
   - Kembalikan dictionary statistik yang memuat total rekaman, jumlah valid, jumlah ditolak, dan daftar rincian alasan penolakan.

---

### Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Kualitas |
| :--- | :---: | :--- |
| **1. Desain Hierarki Custom Exception** | 25 Poin | Merancang class exception turunan yang informatif dan merepresentasikan aturan domain jaringan. |
| **2. Presisi Penanganan try-except-else-finally** | 25 Poin | Menerapkan blok proteksi spesifik tanpa bare `except:` dan memanfaatkan `else`/`finally` secara tepat. |
| **3. Ketahanan Validasi Rekaman & Edge Cases** | 25 Poin | Mampu menangani tipe string non-numerik, nilai negatif tak valid, list kosong, dan data duplikat. |
| **4. Integrasi Logging & Pelaporan Diagnostik** | 25 Poin | Menerapkan modul `logging` dengan level yang sesuai serta menghasilkan ringkasan statistik yang akurat. |

---

### Berkas Pengumpulan

- `tugas_18.py`: Skrip mandiri implementasi solusi yang mematuhi standar PEP 8, memiliki type hints, dan docstring lengkap.
