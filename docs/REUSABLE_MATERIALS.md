# Katalog Materi yang Dapat Digunakan Kembali (*Reusable Materials*)
## Python Learning Hub — Reusable Educational Assets Catalog

Dokumen ini menginventarisasi komponen edukasi konkret dari 8 sumber referensi terbuka yang dapat langsung diadaptasi, diterjemahkan, dan diintegrasikan ke dalam 30 chapter **Python Learning Hub**.

---

## 1. Kode Program & Pola Algoritmik (*Code Snippets & Algorithmic Patterns*)

### A. Pola Algoritma Pencarian & Pengurutan (dari *Learn Python* & *Think Python*)
- **Pencarian Linear (*Linear Search*):** Implementasi iteratif dengan penanganan kasus elemen tidak ditemukan (`return None` / `return -1`). Target: **Chapter 15**.
- **Pencarian Biner (*Binary Search*):** Implementasi divide-and-conquer pada list terurut, demonstrasi reduksi kompleksitas dari $O(n)$ ke $O(\log n)$. Target: **Chapter 15**.
- **Selection Sort & Insertion Sort:** Implementasi sorting klasik manual dengan visualisasi pergeseran indeks swap data. Target: **Chapter 15**.
- **Custom Key Sorting:** Pemanfaatan fungsi bawaan Python `sorted(data, key=lambda x: ...)` untuk pengurutan record data kamus dictionary multi-atribut. Target: **Chapter 15**.

### B. Pola Pemrosesan Sequence & Comprehensions (dari *30 Days of Python* & *Python Docs*)
- **List Comprehensions:** Transformasi data tabular dengan filter kondisi `[expr for item in iterable if condition]`. Target: **Chapter 14**.
- **Dictionary Comprehensions:** Pembuatan indeks asosiatif cepat `{item['id']: item for item in records}`. Target: **Chapter 14**.
- **Generator Expressions:** Penghematan memori RAM saat memproses sequence data masif `(x ** 2 for x in huge_dataset)`. Target: **Chapter 14**.
- **Tuple Unpacking Idiom:** Pola pertukaran nilai dua variabel tanpa variabel pembantu sementara (`a, b = b, a`) dan ekstraksi koordinat posisi. Target: **Chapter 08**.

### C. Pola Rekayasa OOP & Design Patterns (dari *Think Python* & *Learn Python*)
- **Dunder Methods Boilerplate:** Implementasi `__repr__`, `__str__`, `__eq__`, `__len__`, dan operator overloading (`__add__`). Target: **Chapter 20**.
- **Decorator Pola Standar:** Decorator pengukuran latensi waktu eksekusi fungsi (`@timer_decorator`) dan decorator logging panggilan fungsi. Target: **Chapter 24**.
- **Context Manager Kustom:** Implementasi class dengan method `__enter__` dan `__exit__` untuk pengelolaan resource koneksi jaringan atau soket telemetri. Target: **Chapter 24**.

### D. Pola Arsitektur Capstone Proyek Terpadu (Chapter 12)
- **Tiga Lapisan Modular:** Pemisahan `validators.py` (validasi murni), `student_manager.py` (logika bisnis murni), dan `main.py` (antarmuka CLI interaktif).
- **In-Memory List of Dictionaries:** Pola manipulasi basis data lokal tanpa dependensi eksternal.
- **Pola Tuple Return:** `tuple[bool, str, ...]` untuk transfer status dan pesan edukatif.
- **Automated Unit Testing (`unittest`):** Pengujian menyeluruh fungsi bisnis dan validasi tanpa interaksi terminal.

---

## 2. Bank Soal Latihan & Kasus Uji (*Exercise Problem Sets*)

### A. Latihan Berjenjang Level 1, 2, 3 (dari *30 Days of Python*)
- **Level 1 (Pemula):** Operasi dasar sintaks, manipulasi variabel, pemotongan string, pembuatan koleksi list sederhana. (Cocok untuk Chapter 02, 03, 04, 07).
- **Level 2 (Menengah):** Pemfilteran data multi-kriteria, perulangan bersarang (*nested loops*), manipulasi kamus dictionary bersarang (*nested dictionaries*). (Cocok untuk Chapter 05, 06, 08, 09).
- **Level 3 (Penalaran):** Pembuatan fungsi modular, penanganan kasus ekstrim (*edge cases*), deduplikasi himpunan data sensor. (Cocok untuk Chapter 10, 11, 13, 14).

### B. Pola Soal Validasi Logika (dari *CS50P Problem Sets*)
- **"Playback Speed" / "Making Faces" pattern:** Manipulasi string interaktif dan sanitasi input teks pengguna. (Cocok untuk Chapter 04 & 07).
- **"Deep Thought" / "Bank" pattern:** Logika pengujian percabangan bertingkat dengan pembersihan spasi dan *case-insensitivity*. (Cocok untuk Chapter 05).
- **"CamelCase to Snake_case" pattern:** Iterasi karakter string dan penggabungan sequence dinamis. (Cocok untuk Chapter 06 & 07).
- **"Fuel Gauge" / "Grocery List" pattern:** Pengolahan loop berulang hingga masukan valid dan pengurutan frekuensi elemen dengan kamus. (Cocok untuk Chapter 09 & 18).
- **"Unit Testing with pytest" pattern:** Penulisan berkas pengujian `test_*.py` untuk memastikan fungsi mengembalikan hasil yang tepat dan memunculkan exception pada masukan cacat. (Cocok untuk Chapter 21 & 26).

---

## 3. Model Mental, Analogi & Diagram Konseptual (*Mental Models from Think Python*)

1. **Variabel sebagai Label Memori (*Variables as Tags/References*):**
   - Menghindari kesalahpahaman umum bahwa variabel adalah "kotak penyimpanan fisik".
   - Variabel dijelaskan sebagai label/tag yang merujuk pada objek di heap memory CPython.
   - Sangat krusial untuk menjelaskan perilaku mutable list di **Chapter 02 & Chapter 08**.
2. **Diagram Alokasi Frame Fungsi (*Stack Diagrams*):**
   - Visualisasi alur pembuatan frame fungsi baru saat fungsi dipanggil, pemisahan variabel lokal di dalam frame, dan penghapusan frame saat `return` dieksekusi.
   - Sangat membantu memahami aturan ruang lingkup variabel LEGB di **Chapter 10**.
3. **Analogi Buku Kamus (*Dictionary Hash Lookup*):**
   - Menjelaskan perbedaan pencarian sekuensial pada daftar panjang ($O(n)$) dibandingkan pembukaan kata pada buku kamus berindeks hash ($O(1)$).
   - Diintegrasikan ke narasi **Chapter 09**.

---

## 4. Panduan & Arsitektur Pengujian Standar (*Testing & Packaging Standards*)

### A. pytest Test Suites (dari *pytest Documentation* & *Learn Python*)
- Struktur pengujian fungsi murni (*pure functions*):
  ```python
  def test_hitung_snr_valid():
      assert hitung_snr(100.0, 1.0) == 20.0

  def test_hitung_snr_invalid():
      with pytest.raises(ValueError):
          hitung_snr(100.0, 0.0)
  ```
- Parameterisasi kasus uji menggunakan decorator `@pytest.mark.parametrize` untuk menguji puluhan kombinasi input dalam satu fungsi tes ringkas. Target: **Chapter 21 & 26**.

### B. Konfigurasi Proyek Modern (dari *Python Packaging Authority / PyPA*)
- Template berkas `pyproject.toml` standar PEP 621:
  ```toml
  [build-system]
  requires = ["setuptools>=61.0"]
  build-backend = "setuptools.build_meta"

  [project]
  name = "telecom-analytics"
  version = "1.0.0"
  authors = [{ name="Aji Pamungkas Tri Nurcahyo" }]
  description = "Pustaka analisis kualitas sinyal telekomunikasi"
  dependencies = ["numpy", "pytest"]
  ```
- Panduan pembuatan dan aktivasi virtual environment multi-platform:
  - Windows: `python -m venv .venv` lalu `.venv\Scripts\Activate.ps1`
  - Linux/macOS: `python3 -m venv .venv` lalu `source .venv/bin/activate`

---

## 5. Matriks Adaptasi Kasus Rekayasa Telekomunikasi (*Telecom Engineering Contextualization*)

Untuk memberikan identitas keilmuan yang khas bagi mahasiswa Teknik Telekomunikasi dan rekayasa komputasi, contoh umum dari sumber referensi diadaptasi menjadi kasus teknis nyata:

| Contoh Umum di Referensi Terbuka | Adaptasi Kontekstual di Python Learning Hub | Modul Target |
|:---|:---|:---|
| Menghitung luas persegi / lingkaran | Menghitung Signal-to-Noise Ratio (SNR) dan konversi daya dBm ke Watt | **Chapter 03 & 10** |
| Daftar nilai ujian mahasiswa | Array pengukuran daya terima sinyal seluler (RSRP dalam dBm) | **Chapter 08** |
| `Dictionary` kontak telepon nama-nomor | Basis data parameter pemancar BTS (Cell ID, Azimuth, Frekuensi, Status) | **Chapter 09** |
| Kalkulasi diskon & filter belanja | Higher-order pipeline telemetri jaringan, closure filter rentang frekuensi | **Chapter 13** |
| List comprehension angka kuadrat | Transformasi skala sinyal dBm ke mW & inverted map IP ke host BTS | **Chapter 14** |
| Sorting angka acak integer | Pemeringkatan metrik BTS & transmisi multi-kriteria (latensi, RSRP) | **Chapter 15** |
| Benchmarking umum loop timer | Profiling empiris deduplikasi sinyal dan perbandingan Big-O time.perf_counter() | **Chapter 16** |
| Membaca file daftar belanjaan / data teks umum | Pipeline pembacaan, penulisan, dan serialisasi data CSV/JSON metrik stasiun transmisi telekomunikasi | **Chapter 17** |
| Pembagian nol sederhana / crash runtime tanpa penanganan | Penanganan exception bertingkat, custom exception hierarchy (`TelecomException`, `SignalRangeError`), dan logging audit telemetri | **Chapter 18** |
| Class Hewan (Dog, Cat) & BankAccount | Modeling perangkat keras (`Device`), validasi state enkapsulasi (`@property`, `@setter`), daya transmisi, dan Device Inventory Manager | **Chapter 19** |
| Hierarki Hewan (Animal -> Mammal/Bird) & Polimorfisme | Hierarki perangkat telekomunikasi (`TransceiverNode`, `CellularAntenna`, `MicrowaveLink`, `FiberOpticNode`), duck typing audit diagnostik, dunder method (`__str__`, `__repr__`, `__eq__`, `__hash__`), dan deduplikasi set BTS | **Chapter 20** |
| Setup kalkulator dasar tanpa struktur modul | Paket modular rekayasa telekomunikasi (`telecom_toolkit`), modern `pyproject.toml`, link budget calculator, parameterized testing SNR/Shannon, exception testing | **Chapter 21** |
| Aplikasi inventaris toko retail generik | **Inventory Management System (Telecom Infrastructure)**: OOP terpadu, persistence atomic write JSON, schema validation, domain exceptions, audit logging, CLI, dan 7 unit tests | **Chapter 22** |
| Pola Desain Toko Online / GUI Widget | **Extensible Device Management System**: Abstract Base Class (`AbstractDevice`), Factory Pattern (`DeviceFactory`), Strategy Pattern (`DiagnosticStrategy`), komposisi klaster, unit tests | **Chapter 23** |
| Decorator otentikasi web generik | **Streaming Telemetry Ingestion Engine**: Decorator validasi rentang nilai, pipeline generator lazy multi-tahap (`yield`), context manager alokasi kanal frekuensi | **Chapter 24** |
| Type hints umum kalkulator | **Type-Safe Network Observability Toolkit**: Skema `TypedDict` (`MetricPayload`), structural subtyping `Protocol` (`MetricEncoder`), generic store `Generic[T]`, static checking mypy & Ruff | **Chapter 25** |
| Pengujian dasar penambahan angka | **Automated Test Suite & Production Telemetry System**: Test fixtures, mocking external gateway client dengan `MagicMock` & `patch`, `assertRaises`, parameterized `subTest`, dan `assertLogs` | **Chapter 26** |
| Multithreading dasar & sleep sleep loop | **Concurrent Task Processing System**: ThreadPoolExecutor untuk I/O paralel, ProcessPoolExecutor untuk komputasi CPU, asyncio event loop, cancellation & timeout, mitigasi race condition dengan `threading.Lock` | **Chapter 27** |
| Mengambil data situs cuaca generik | **REST API Data Client**: Integrasi HTTP klien, Bearer token authentication dari environment variables, penanganan pagination otomatis, proteksi timeout, retry eksponensial untuk transient faults (503), dan sanitasi kredensial pada log | **Chapter 28** |

