# Tugas Mini Project: Production-Ready Python Application

**Chapter 29: Software Architecture & Deployment**  
**Tingkat:** Level 3 — Professional Python Engineering  
**Platform:** Python Learning Hub  
**Institusi:** Institut Teknologi Sumatera (ITERA)  

---

## 1. Deskripsi Tugas

Dalam standar rekayasa perangkat lunak modern, skrip tunggal monolitik yang mencampuradukkan input pengguna, koneksi database, dan logika bisnis sangat sulit dirawat (*unmaintainable*) dan rentan terhadap regresi (*bug-prone*).

Tugas Anda adalah merancang dan menyempurnakan modul **`ProductionReadyApp`** di dalam berkas `tugas.py`. Aplikasi ini memodelkan sistem manajemen deployment perangkat telekomunikasi dengan standar arsitektur berlapis (*Clean / Layered Architecture*):
1. **Domain Layer:** Entitas data murni (`NetworkNode`, `DeploymentRelease`) tanpa ketergantungan pada pustaka luar.
2. **Ports & Repository Layer:** Abstraksi penyimpanan menggunakan Python `Protocol` dan implementasi konkret `InMemoryNodeRepository`.
3. **Application / Service Layer:** Logika orkestrasi bisnis (`NodeDeploymentService`) yang menerapkan *Dependency Injection* (DI).
4. **Configuration Layer:** Manajemen konfigurasi Twelve-Factor berbasis `os.environ`.
5. **Presentation / CLI Layer:** Antarmuka baris perintah (`argparse`) dengan *subcommands* (`status` dan `deploy`).

---

## 2. Diagram Arsitektur Aplikasi Berlapis

```
  ┌───────────────────────────────────────────────────────────────┐
  │                   Presentation Layer                          │
  │              (CLI Dispatcher / argparse)                      │
  └───────────────────────────────┬───────────────────────────────┘
                                  │ memanggil
  ┌───────────────────────────────▼───────────────────────────────┐
  │                   Application / Service Layer                 │
  │        (NodeDeploymentService with Dependency Injection)      │
  └──────────────────┬─────────────────────────────▲──────────────┘
                     │ menggunakan                 │ membaca
  ┌──────────────────▼────────────┐    ┌───────────┴──────────┐
  │       Ports & Adapters        │    │ Configuration Layer  │
  │      (NodeRepository Protocol)│    │ (Twelve-Factor Env)  │
  └──────────────────┬────────────┘    └──────────────────────┘
                     │ mengelola
  ┌──────────────────▼────────────┐
  │          Domain Layer         │
  │   (NetworkNode / Pure Models) │
  └───────────────────────────────┘
```

---

## 3. Persyaratan Fungsional Modul

Modul wajib diimplementasikan di dalam file `tugas.py` dengan komponen berikut:

1. **`AppConfig`:**
   - Membaca `DEPLOY_ENV` (default: "production"), `SERVICE_PORT` (default: 8000), dan `LOG_LEVEL` (default: "INFO").
2. **`NodeRepository` & `InMemoryNodeRepository`:**
   - Menyediakan method `get_by_id(node_id)`, `list_by_cluster(cluster_zone)`, dan `save(node)`.
3. **`NodeDeploymentService`:**
   - Menerima `NodeRepository` via constructor injection (`__init__`).
   - Method `deploy_release(cluster_zone, version, operator)`: hanya mengupdate simpul yang operasional (status bukan MAINTENANCE).
   - Method `get_cluster_status(cluster_zone)`: menghitung persentase skor kesehatan klaster.
4. **`run_cli_command(service, args_list)`:**
   - Menerjemahkan argumen string ke pemanggilan service dan mengembalikan hasil dictionary.

---

## 4. Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi |
| :--- | :---: | :--- |
| **Separation of Concerns & Layering** | 25 Poin | Pemisahan yang tegas antara domain model, port repository, service layer, dan CLI presenter. |
| **Penerapan Dependency Injection** | 25 Poin | Service bergantung pada abstraksi repository, memungkinkan mock testing tanpa dependensi fisik. |
| **Twelve-Factor Configuration** | 20 Poin | Pembacaan konfigurasi dari environment variables dengan fallback default yang aman dan tipe terkonversi. |
| **CLI Dispatcher & Error Handling** | 15 Poin | Penanganan subcommands (`status`, `deploy`) dengan argparse dan penanganan kesalahan klaster tidak valid. |
| **Kerapian Kode & Type Hints** | 15 Poin | Mengikuti standar PEP 8, type hints lengkap pada seluruh method, dan docstrings Bahasa Indonesia yang jelas. |

---

## 5. Cara Pengujian

Jalankan skrip pengujian mandiri:
```bash
python tugas.py
```
Pastikan seluruh validasi status kode dan asersi arsitektur lulus 100%.
