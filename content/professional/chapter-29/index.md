# Chapter 29: Software Architecture & Deployment
## Clean Architecture, Twelve-Factor App, Packaging & CI/CD

Selamat datang di **Chapter 29: Software Architecture & Deployment** pada tingkat **Level 3: Professional Python Engineering** di **Python Learning Hub**.

Pada bab-bab sebelumnya, Anda telah menguasai penulisan kode tingkat lanjut, mulai dari pola desain berorientasi objek (Chapter 23), metaprogramming dan generator (Chapter 24), pengetikan statis tipe (Chapter 25), pengujian otomatis mendalam (Chapter 26), pemrograman konkuren (Chapter 27), hingga integrasi REST API (Chapter 28). Namun, dalam dunia industri perangkat lunak profesional, keterampilan menulis kode hanyalah separuh dari perjalanan rekayasa. Separuh lainnya adalah kemampuan merancang **arsitektur perangkat lunak (*software architecture*)** yang mudah dipelihara dan membangun **alur rilis (*deployment pipeline*)** yang andal.

Bab ini membahas prinsip-prinsip arsitektur perangkat lunak modern, pemisahan tanggung jawab (*Separation of Concerns*), *Dependency Injection*, konfigurasi berbasis prinsip *Twelve-Factor App*, standardisasi packaging Python modern dengan `pyproject.toml`, serta otomatisasi penjaminan mutu melalui pipeline *Continuous Integration* (CI) menggunakan GitHub Actions.

---

## 1. Pengantar Arsitektur Perangkat Lunak: Monolit vs Modular

Dalam fase eksplorasi awal, pengembang sering kali menulis seluruh logika program ke dalam satu file skrip tunggal (*monolithic script*). Pendekatan ini dapat diterima untuk prototipe kecil, tetapi menjadi bencana ketika aplikasi berkembang:

- **Monolitik Tak Terstruktur:**
  Logika pengambilan input dari pengguna, koneksi soket jaringan, kueri basis data, dan aturan validasi bisnis bercampur baur di satu tempat. Mengubah format keluaran CLI berisiko merusak logika kalkulasi data, dan menulis unit test otomatis menjadi hampir mustahil.
- **Arsitektur Modular (Modular Architecture):**
  Sistem dibagi menjadi modul-modul independen dengan batas tanggung jawab yang tegas (*clear boundaries*). Setiap modul dapat dikembangkan, diuji, dan diperbarui secara terisolasi tanpa merusak komponen lain.

---

## 2. Pemisahan Tanggung Jawab (*Separation of Concerns*) & Arsitektur Berlapis

Prinsip **Separation of Concerns (SoC)** menyatakan bahwa sebuah sistem perangkat lunak harus dipecah menjadi beberapa bagian yang menangani aspek permasalahan yang berbeda secara terpisah.

Dalam pola **Layered / Clean Architecture**, sistem dibagi menjadi lapisan-lapisan konsentris:

```
  ┌───────────────────────────────────────────────────────────────┐
  │                   Presentation / CLI Layer                    │
  │                  (argparse, Click, Web Router)                │
  └───────────────────────────────┬───────────────────────────────┘
                                  │ memanggil
  ┌───────────────────────────────▼───────────────────────────────┐
  │                   Application / Service Layer                 │
  │              (Orkestrasi Alur Kasus Penggunaan)               │
  └──────────────────┬─────────────────────────────▲──────────────┘
                     │ menggunakan                 │ membaca
  ┌──────────────────▼────────────┐    ┌───────────┴──────────┐
  │       Ports & Adapters        │    │ Configuration Layer  │
  │     (Repository Protocols)    │    │ (Twelve-Factor Env)  │
  └──────────────────┬────────────┘    └──────────────────────┘
                     │ mengelola
  ┌──────────────────▼────────────┐
  │          Domain Layer         │
  │    (Entitas Bisnis Murni)     │
  └───────────────────────────────┘
```

1. **Domain Layer (Lapisan Inti):**
   Berisi entitas data bisnis murni (seperti `NetworkNode`, `DeploymentRelease`). Lapisan ini sama sekali **tidak boleh** bergantung pada framework luar, database, atau terminal I/O.
2. **Ports & Repository Layer:**
   Mendefinisikan antarmuka abstraksi data access (misalnya class `Protocol` yang menentukan method `get_by_id`, `save`).
3. **Application / Service Layer:**
   Mengorkestrasikan aturan bisnis spesifik aplikasi menggunakan antarmuka port repository.
4. **Presentation Layer:**
   Berfungsi sebagai penerjemah antara dunia luar (argumen baris perintah atau payload HTTP) dengan domain internal aplikasi.

---

## 3. Dependency Injection & Inversion of Control

Keterikatan kuat (*tight coupling*) terjadi ketika sebuah class membuat sendiri dependensinya secara langsung di dalam constructor:

```python
# CONTOH BURUK (Tight Coupling - Sulit diuji):
class IncidentService:
    def __init__(self) -> None:
        self.notifier = SmtpEmailClient()  # Membuat dependensi konkret langsung!
```

Jika server SMTP tidak tersedia saat menjalankan unit test, seluruh pengujian akan gagal. Solusinya adalah **Dependency Injection (DI)**, di mana dependensi disuntikkan dari luar:

```python
# CONTOH BAIK (Dependency Injection via Protocol):
from typing import Protocol

class Notifier(Protocol):
    def send(self, message: str) -> bool: ...

class IncidentService:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier  # Disuntikkan dari luar
```

Dengan pola ini, Anda dapat menyuntikkan `MockNotifier` selama pengujian dan menyuntikkan `SmtpEmailClient` di lingkungan produksi tanpa mengubah satu baris pun kode pada `IncidentService`.

---

## 4. Konfigurasi Aplikasi: Metodologi Twelve-Factor App

Metodologi **The Twelve-Factor App** merumuskan praktik terbaik untuk membangun aplikasi yang portabel dan siap dirilis di lingkungan cloud:

- **Faktor III: Simpan Konfigurasi di Lingkungan (Store config in the environment):**
  Jangan pernah menyimpan parameter konfigurasi (seperti nomor port, URL database, dan API key) secara *hardcoded* di source code.
- **Environment Variables:**
  Gunakan variabel lingkungan sistem operasi (`os.environ.get`) untuk menyuntikkan konfigurasi saat runtime.
- **Pemisahan Lingkungan:**
  Nilai konfigurasi yang berbeda (misal `development`, `staging`, `production`) dapat diterapkan pada *codebase* yang sama persis tanpa perlu melakukan kompilasi ulang.

---

## 5. Observabilitas & Structured Logging di Produksi

Menggunakan fungsi `print()` di aplikasi produksi memiliki kelemahan fatal:
- Tidak memiliki stempel waktu (*timestamp*).
- Tidak memiliki penanda tingkat keparahan (*severity levels* seperti INFO, WARNING, ERROR).
- Sulit diuraikan oleh mesin pengumpul log terpusat (*log aggregators*).

Praktik standar industri adalah menerapkan **Structured Logging** berformat JSON. Setiap peristiwa sistem dicatat sebagai satu objek JSON yang memuat konteks operasi, mempermudah pelacakan anomali pada lingkungan cloud seperti AWS CloudWatch, Google Cloud Logging, atau ElasticSearch.

---

## 6. Standar Packaging Modern Python: `pyproject.toml` (PEP 621)

Dalam ekosistem Python modern, file lama `setup.py` dan `setup.cfg` telah digantikan oleh standar deklaratif tunggal: **`pyproject.toml`**.

```toml
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "telecom-monitoring"
version = "1.0.0"
description = "Sistem Pemantauan Infrastruktur Jaringan Produksi"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "pydantic>=2.0.0",
    "httpx>=0.24.0",
]

[project.scripts]
telecom-cli = "telecom_monitoring.cli:main"
```

### Format Distribusi: Wheel (`.whl`) vs SDist (`.tar.gz`)
- **Wheel (`.whl`):** Format distribusi biner siap pasang (*built distribution*). Tidak memerlukan tahap kompilasi di mesin target sehingga proses instalasi sangat cepat.
- **SDist (`.tar.gz`):** Distribusi kode sumber mentah (*source distribution*). Berguna sebagai cadangan universal ketika format wheel untuk arsitektur CPU tertentu belum tersedia.

---

## 7. Otomatisasi Penjaminan Mutu dengan Continuous Integration (CI)

**Continuous Integration (CI)** adalah praktik rekayasa di mana setiap perubahan kode yang didorong (*push*) ke repositori Git secara otomatis diuji dan divalidasi oleh server otomatisasi (*runner*).

Contoh workflow GitHub Actions (`.github/workflows/ci.yml`):
```yaml
name: Production CI Pipeline
on: [push, pull_request]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Static Typecheck
        run: mypy src

      - name: Run Test Suite
        run: pytest --cov=src
```

Jika salah satu tahap (misalnya uji unit atau static type checking) gagal, rilis otomatis dibatalkan, mencegah kode yang cacat mencapai lingkungan produksi.

---

## 8. Ringkasan & Referensi Lanjutan

- Pisahkan domain model bisnis dari implementasi infrastruktur I/O dengan Clean Architecture.
- Terapkan *Dependency Injection* agar modul dapat diuji secara terisolasi tanpa server nyata.
- Kelola konfigurasi dan rahasia aplikasi melalui *Environment Variables* sesuai prinsip *Twelve-Factor App*.
- Gunakan `pyproject.toml` untuk standardisasi packaging dan distribusi paket Python.
- Amankan rilis perangkat lunak melalui otomatisasi pengetesan pada pipeline Continuous Integration.
- **Referensi Resmi:**
  - [The Twelve-Factor App](https://12factor.net/)
  - [Python Packaging User Guide (packaging.python.org)](https://packaging.python.org/)
  - [PEP 621 — Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
  - [GitHub Actions Documentation](https://docs.github.com/en/actions)
