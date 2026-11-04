# Tugas Proyek Akhir: Integrated Python Application — Professional Capstone

**Chapter 30: Professional Capstone Project**  
**Tingkat:** Level 3 — Professional Python Engineering  
**Platform:** Python Learning Hub  
**Institusi:** Institut Teknologi Sumatera (ITERA)  

---

## 1. Deskripsi Proyek Puncak

Selamat datang di modul proyek akhir **Level 3: Professional Python Engineering**. Tugas Capstone ini merupakan integrasi menyeluruh dari seluruh kompetensi yang telah Anda pelajari pada Chapter 01 s.d. 29.

Sebagai seorang Senior Python Engineer, tugas Anda adalah merancang dan membangun **Python Data Monitoring & Automation Platform** di dalam berkas `tugas.py`. Platform ini memproses data telemetri infrastruktur jaringan secara terdistribusi, memvalidasi integritas data, menghitung metrik SLA, serta menghasilkan laporan performa otomatis.

---

## 2. Arsitektur Sistem Berlapis (System Architecture)

```
       ┌────────────────────────────────────────────────────────┐
       │                   Presentation Layer                   │
       │           (CLI Dispatcher / Command Routing)           │
       └───────────────────────────┬────────────────────────────┘
                                   │ memanggil
       ┌───────────────────────────▼────────────────────────────┐
       │               TelemetryProcessingEngine                │
       │    (Data Ingestion, Analysis & Anomaly Detection)      │
       └─────┬───────────────────────────┬────────────────▲─────┘
             │                           │                │ membaca
  ┌──────────▼──────────┐     ┌──────────▼──────────┐ ┌───┴─────────────┐
  │ LocalCsvSource      │     │ MockApiSource       │ │ PlatformConfig  │
  │ (Aliran Berkas CSV) │     │ (REST Endpoint Mock)│ │ (Twelve-Factor) │
  └──────────┬──────────┘     └──────────┬──────────┘ └─────────────────┘
             │                           │
             └─────────────┬─────────────┘
                           │ menyimpan & mengindeks
              ┌────────────▼────────────┐
              │  LocalTelemetryStorage  │
              │  (threading.Lock safe)  │
              └────────────┬────────────┘
                           │ menyintesis
              ┌────────────▼────────────┐
              │ TelemetryReportGenerator│
              │ (Laporan SLA Markdown)  │
              └─────────────────────────┘
```

---

## 3. Persyaratan Fungsional Modul

Modul wajib diimplementasikan di dalam file `tugas.py` dengan ketentuan sebagai berikut:

1. **Domain Entities (`TelemetryRecord`):**
   - Menyimpan atribut: `device_id`, `timestamp`, `rssi_dbm`, `packet_loss_pct`, `cpu_load_pct`, `temperature_c`, dan `status`.
   - Property `is_healthy -> bool`: Bernilai `True` jika `rssi_dbm >= -85.0`, `packet_loss_pct < 2.0`, `cpu_load_pct < 80.0`, dan `temperature_c < 75.0`.
2. **Configuration Layer (`PlatformConfig`):**
   - Membaca konfigurasi dari *environment variables* dengan nilai bawaan yang aman.
3. **Multi-Source Data Ingestion:**
   - Mampu mengekstrak data dari `LocalCsvTelemetrySource` dan `MockApiTelemetrySource`.
4. **Thread-Safe Storage (`LocalTelemetryStorage`):**
   - Operasi penyimpanan batch dan perorangan dilindungi oleh `threading.Lock`.
5. **Analytics & Anomaly Detection (`TelemetryProcessingEngine`):**
   - Menghitung rata-rata `packet_loss_pct`, rata-rata `cpu_load_pct`, dan persentase rasio kesehatan klaster.
   - Mendeteksi anomali perangkat yang melanggar batas ambang toleransi.
6. **Automated Reporting (`TelemetryReportGenerator`):**
   - Menghasilkan ringkasan laporan operasional berformat Markdown lengkap dengan status kepatuhan SLA.
7. **Presentation Layer (`run_cli`):**
   - Menyediakan antarmuka komando dengan flag `--run`, `--report`, dan `--cluster`.

---

## 4. Rubrik Penilaian Capstone (Total: 100 Poin)

| Kategori Penilaian | Bobot | Indikator Evaluasi |
| :--- | :---: | :--- |
| **Core Application Functionality** | 25 Poin | Alur penyerapan data multi-sumber, penyimpanan, kalkulasi analitik, dan pelaporan berjalan mulus tanpa error. |
| **Software Architecture & OOP** | 20 Poin | Penerapan Clean Architecture yang bersih, pemisahan layer Domain/Ports/Services/CLI, dan penggunaan Protocol yang tepat. |
| **Data Processing & Integration** | 15 Poin | Kemampuan memproses stream CSV lokal dan integrasi endpoint REST API dengan parsing tipe data yang akurat. |
| **Error Handling & Reliability** | 15 Poin | Proteksi thread-safety menggunakan Lock, penanganan kegagalan parsing defensif, dan zero unhandled exceptions. |
| **Testing & Code Quality** | 15 Poin | Mematuhi standar PEP 8, memiliki type hints lengkap, modularitas tinggi, dan lolos uji asersi mandiri 100%. |
| **Documentation & Deployment Readiness** | 10 Poin | Konfigurasi Twelve-Factor berbasis environment variables dan struktur kode yang siap dikemas (packageable). |

---

## 5. Cara Pengujian

Jalankan skrip pengujian mandiri:
```bash
python tugas.py
```
Pastikan seluruh asersi dan verifikasi arsitektur lulus 100%.
