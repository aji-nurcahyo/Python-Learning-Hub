# Pemetaan Sumber Referensi Terbuka (30 Chapter)
## Python Learning Hub — Reference Source Mapping

Dokumen ini memetakan 8 sumber edukasi terkemuka dan berstandar internasional ke dalam 30 chapter kurikulum **Python Learning Hub**.

---

## 1. Daftar Sumber Referensi Kanonikal

1. **[DOCS] Python 3 Official Tutorial** — [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/)  
   *Lisensi: Python Software Foundation License (PSF 2.0)*. Otoritatif, baku, rujukan utama sintaks & standard library.
2. **[THINK] Think Python (3rd Edition)** oleh Allen B. Downey — [allendowney.github.io/ThinkPython](https://allendowney.github.io/ThinkPython/)  
   *Lisensi: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)*. Model mental komputasional, analogi, diagram alokasi memori, latihan berpikir kritis.
3. **[30DAY] 30 Days of Python** oleh Asabeneh S. Yetayeh — [github.com/Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python)  
   *Lisensi: MIT License*. Progresi harian berurutan, latihan berjenjang (Level 1, 2, 3), ringkasan tabel dan fungsi bawaan.
4. **[CS50P] CS50’s Introduction to Programming with Python** (Harvard University / David J. Malan) — [cs50.harvard.edu/python](https://cs50.harvard.edu/python/)  
   *Lisensi: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)*. Desain instruksional modern, studi kasus dunia nyata, pengujian otomatis menggunakan `pytest`.
5. **[SWCARP] Software Carpentry: Programming with Python** — [swcarpentry.github.io/python-novice-inflammation](https://swcarpentry.github.io/python-novice-inflammation/)  
   *Lisensi: Creative Commons Attribution 4.0 International (CC BY 4.0)*. Komputasi ilmiah, pemrosesan array numerik, analisis data bertahap, praktik *defensive programming*.
6. **[LEARN] Learn Python** oleh Oleksii Trekhleb — [github.com/trekhleb/learn-python](https://github.com/trekhleb/learn-python)  
   *Lisensi: MIT License*. Ratusan contoh kode modular yang seluruhnya dilengkapi pengujian otomatis *unit testing* `pytest`.
7. **[PYTEST] pytest Documentation** — [docs.pytest.org/en/stable](https://docs.pytest.org/en/stable/)  
   *Lisensi: MIT License*. Standar industri pengujian otomatis Python, fixtures, mock, parameterisasi kasus uji.
8. **[PYPA] Python Packaging User Guide** — [packaging.python.org](https://packaging.python.org/en/latest/)  
   *Lisensi: Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)*. Panduan resmi pengelolaan virtual environment, `pyproject.toml`, dan distribusi paket software.

---

## 2. Pemetaan Referensi Per Chapter

### LEVEL 1: PYTHON FOUNDATIONS (CHAPTER 01 – 12)

#### Chapter 01 — Introduction to Python
- **Topik:** Sejarah Python, filosofi Zen of Python, interpreted vs compiled language, instalasi CPython & VS Code/Colab, eksekusi skrip pertama.
- **Rujukan Utama:** [DOCS] Section 1 & 2 ("Whetting Your Appetite", "Using the Python Interpreter").
- **Rujukan Pendukung:** [THINK] Chapter 1 ("The Way of the Program"); [30DAY] Day 01 ("Introduction").
- **Materi Dapat Diadaptasi:** Diagram alur interpreter CPython, panduan instalasi multi-platform, pengenalan REPL interaktif.
- **Kebutuhan Konten Asli:** Panduan penyiapan lingkungan VS Code berbahasa Indonesia, studi kasus peran Python di bidang rekayasa telekomunikasi & otomasi jaringan.

#### Chapter 02 — Variables & Scalar Data Types
- **Topik:** Variabel sebagai referensi memori (labeling), tipe data primitif (`int`, `float`, `str`, `bool`), konversi tipe (*type casting*), fungsi `type()`, `id()`.
- **Rujukan Utama:** [THINK] Chapter 2 ("Variables, Expressions and Statements"); [DOCS] Section 3.1 ("Using Python as a Calculator").
- **Rujukan Pendukung:** [30DAY] Day 02 ("Variables, Builtin Functions"); [CS50P] Week 0 ("Functions, Variables").
- **Materi Dapat Diadaptasi:** Latihan tipe data, mental model diagram alokasi referensi objek di memori, konversi suhu/waktu.
- **Kebutuhan Konten Asli:** Contoh variabel telekomunikasi (frekuensi MHz, level daya dBm, status transceiver boolean).

#### Chapter 03 — Operators & Expressions
- **Topik:** Operator aritmatika (`+`, `-`, `*`, `/`, `//`, `%`, `**`), operator pembanding, operator logika (`and`, `or`, `not`), presedensi operator (PEMDAS), bitwise dasar.
- **Rujukan Utama:** [DOCS] Section 3.1.1 ("Numbers"); [THINK] Chapter 2.4 ("Expressions and Statements").
- **Rujukan Pendukung:** [30DAY] Day 03 ("Operators"); [LEARN] `src/operators/`.
- **Materi Dapat Diadaptasi:** Tabel presedensi operator, latihan ekspresi aritmatika bertingkat, operasi modulus untuk siklus waktu.
- **Kebutuhan Konten Asli:** Perhitungan formula fisika gelombang elektromagnetik ($\lambda = c / f$) dan kalkulasi budget daya transmisi.

#### Chapter 04 — Interactive Input & Formatted Output
- **Topik:** Fungsi `input()`, konversi string input ke numerik, format output f-strings (PEP 498), specifiers (`:.2f`, padding, alignment), pemisah `sep` dan akhiran `end`.
- **Rujukan Utama:** [DOCS] Section 7.1 ("Fancier Output Formatting"); [CS50P] Week 0 ("Functions, Variables").
- **Rujukan Pendukung:** [30DAY] Day 04 ("Strings - formatting"); [THINK] Chapter 7.3 ("Formatted String Literals").
- **Materi Dapat Diadaptasi:** Pola formatting nilai desimal persentase dan mata uang, prompt interaktif CLI.
- **Kebutuhan Konten Asli:** Format pelaporan data telemetri sensor telekomunikasi dengan f-string terstruktur.

#### Chapter 05 — Conditional Statements & Branching Logic
- **Topik:** Percabangan logika `if`, `elif`, `else`, nested conditionals, operator keanggotaan `in`, operator identitas `is`, evaluasi short-circuit.
- **Rujukan Utama:** [DOCS] Section 4.1 ("if Statements"); [THINK] Chapter 5 ("Conditionals and Recursion").
- **Rujukan Pendukung:** [CS50P] Week 1 ("Conditionals"); [30DAY] Day 09 ("Conditionals").
- **Materi Dapat Diadaptasi:** Latihan klasifikasi grade nilai, pemeriksaan tahun kabisat, alur validasi formulir.
- **Kebutuhan Konten Asli:** Algoritma klasifikasi kualitas sinyal seluler LTE (kategori RSRP: Sangat Baik, Baik, Cukup, Buruk).

#### Chapter 06 — Loops & Iteration
- **Topik:** Perulangan `while` (kondisional), perulangan `for` (iterasi sequence), fungsi `range(start, stop, step)`, kontrol `break`, `continue`, klausa `else` pada loop.
- **Rujukan Utama:** [DOCS] Section 4.2 & 4.3 ("for Statements", "The range() Function", "break and continue").
- **Rujukan Pendukung:** [THINK] Chapter 6 ("Iteration"); [SWCARP] Episode 02 ("Repeating Actions with Loops").
- **Materi Dapat Diadaptasi:** Pola akumulasi hitung total/rata-rata, simulasi countdown timer, deteksi batas toleransi loop.
- **Kebutuhan Konten Asli:** Simulasi pembacaan paket buffer telekomunikasi dan algoritma retransmisi percobaan berulang (retry mechanism).

#### Chapter 07 — Strings & Text Processing
- **Topik:** String sebagai sequence immutable, indexing, slicing `[start:stop:step]`, escape characters, method string (`split`, `join`, `strip`, `replace`, `find`, `upper`, `lower`), dasar regex (`re`).
- **Rujukan Utama:** [DOCS] Section 3.1.2 ("Text") & Standard Library `str` methods.
- **Rujukan Pendukung:** [THINK] Chapter 7 ("Strings"); [30DAY] Day 04 ("Strings"); [CS50P] Week 7 ("Regular Expressions").
- **Materi Dapat Diadaptasi:** Algoritma palindrome check, pembersihan spasi data input, ekstraksi domain email.
- **Kebutuhan Konten Asli:** Parsing string log perangkat jaringan (ekstraksi alamat IP, MAC address, kode status respon BTS).

#### Chapter 08 — Lists & Tuples *(Sudah Aktif — Perlu Pengayaan Narasi)*
- **Topik:** Sequence terurut, mutable vs immutable, list methods (`append`, `extend`, `insert`, `pop`, `sort`, `reverse`), tuple packing & unpacking, passing tuple koordinat.
- **Rujukan Utama:** [DOCS] Section 5.1 & 5.3 ("More on Lists", "Tuples and Sequences").
- **Rujukan Pendukung:** [THINK] Chapter 8 & 10 ("Lists", "Tuples"); [SWCARP] Episode 03 ("Storing Multiple Values in Lists").
- **Materi Dipertahankan:** Slide interaktif Ch 08 (21 slide), `contoh.py`, tugas pengolahan statistik sinyal telekomunikasi.
- **Pengayaan:** Menambahkan teks dokumen konsep lengkap di `index.md` dan menyematkan sitasi [DOCS] & [THINK].

#### Chapter 09 — Dictionaries & Sets *(Sudah Aktif — Perlu Pengayaan Narasi)*
- **Topik:** Hash tables, associative arrays key-value, dictionary methods (`get`, `keys`, `values`, `items`, `pop`), himpunan set unik, operasi matematis set (`union`, `intersection`, `difference`).
- **Rujukan Utama:** [DOCS] Section 5.4 & 5.5 ("Sets", "Dictionaries").
- **Rujukan Pendukung:** [THINK] Chapter 9 ("Dictionaries"); [30DAY] Day 07 & 08 ("Sets", "Dictionaries").
- **Materi Dipertahankan:** Slide interaktif Ch 09 (21 slide), `contoh.py`, latihan ekstraksi lokasi unik pemancar.
- **Pengayaan:** Menambahkan narasi pendalaman konsep hashability, tabel ringkasan kompleksitas lookup O(1) di `index.md`.

#### Chapter 10 — Functions & Scope *(Sudah Aktif — Perlu Pengayaan Narasi)*
- **Topik:** Deklarasi `def`, parameter wajib vs nilai default, pembedaan tegas `print` vs `return`, aturan ruang lingkup variabel LEGB (Local, Enclosing, Global, Built-in).
- **Rujukan Utama:** [DOCS] Section 4.7 ("Defining Functions"); [THINK] Chapter 3 & 4 ("Functions").
- **Rujukan Pendukung:** [CS50P] Week 0 & Week 2; [SWCARP] Episode 05 ("Creating Functions").
- **Materi Dipertahankan:** Slide interaktif Ch 10 (20 slide), `contoh.py`, latihan fungsi klasifikasi sinyal, tugas modularitas.
- **Pengayaan:** Menambahkan diagram visual alur pemanggilan call stack dan LEGB scope diagram pada `index.md`.

#### Chapter 11 — Modules & Basic Exceptions *(Sudah Aktif — Perlu Pengayaan Narasi)*
- **Topik:** Pembuatan modul `.py` mandiri, `import` statement, namespace isolation, docstrings (PEP 257), proteksi runnable `if __name__ == '__main__':`, penanganan error `try-except` dasar.
- **Rujukan Utama:** [DOCS] Section 6 ("Modules") & Section 8.1–8.3 ("Errors and Exceptions").
- **Rujukan Pendukung:** [THINK] Chapter 11 ("Files and Databases"); [CS50P] Week 3 & 4 ("Exceptions", "Libraries").
- **Materi Dipertahankan:** Slide interaktif Ch 11 (20 slide), modul `statistik.py` + `main.py`, tugas perancangan pustaka fungsi.
- **Pengayaan:** Menambahkan referensi resmi PEP 257 dan dokumentasi panduan exception handling di `index.md`.

#### Chapter 12 — Foundations Capstone Project
- **Topik:** Proyek integrasi Level 1 Foundations: aplikasi CLI komprehensif yang memadukan menu kendali, pengolahan sequence list/dict/set, fungsi modular, dan penanganan exception dasar.
- **Rujukan Utama:** [CS50P] Project Guidelines; [30DAY] Project Challenges Day 10 & 20.
- **Materi Dapat Diadaptasi:** Standar arsitektur proyek mandiri mahasiswa, rubrik penilaian capstone terstruktur.
- **Kebutuhan Konten Asli:** Capstone Project spesifik: *"Sistem Pemantauan dan Analisis Kualitas Sinyal Jaringan Seluler"* (Telecom Tower Telemetry Logger).

---

### LEVEL 2: INTERMEDIATE PYTHON DEVELOPMENT (CHAPTER 13 – 22)

#### Chapter 13 — Advanced Function Design
- **Topik:** Variable-length arguments (`*args`, `**kwargs`), fungsi kelas satu (*first-class functions*), fungsi anonim (`lambda`), fungsi tingkat tinggi (`map`, `filter`, `reduce`), closures.
- **Rujukan Utama:** [DOCS] Section 4.8 ("More on Defining Functions"); [THINK] Chapter 18.
- **Rujukan Pendukung:** [30DAY] Day 14 ("Higher Order Functions"); [LEARN] `src/functions/`.
- **Materi Dapat Diadaptasi:** Contoh closure dan lambda expressions, latihan pipeline transformasi data.

#### Chapter 14 — Comprehensions & Generator Expressions
- **Topik:** List comprehensions dengan filter kondisi if/else, nested comprehensions, dictionary comprehensions, set comprehensions, memory-efficient generator expressions `(x for x in data)`.
- **Rujukan Utama:** [DOCS] Section 5.1.3 & 5.1.4 ("List Comprehensions", "Nested List Comprehensions").
- **Rujukan Pendukung:** [30DAY] Day 13 ("List Comprehension"); [LEARN] `src/data_types/`.
- **Materi Dapat Diadaptasi:** Perbandingan alokasi memori menggunakan `sys.getsizeof()`.

#### Chapter 15 — Searching & Sorting Algorithms
- **Topik:** Algoritma pencarian (Linear Search, Binary Search), algoritma pengurutan manual (Selection Sort, Insertion Sort, Bubble Sort), pemanfaatan bawaan `sorted()` dengan parameter `key=lambda` dan `reverse`.
- **Rujukan Utama:** Python HowTo — Sorting ([docs.python.org/3/howto/sorting.html](https://docs.python.org/3/howto/sorting.html)).
- **Rujukan Pendukung:** [THINK] Chapter 10 & 13; [LEARN] `src/algorithms/`.
- **Materi Dapat Diadaptasi:** Implementasi algoritma pencarian biner pada data terurut, demonstrasi sorting objek kompleks multi-atribut.

#### Chapter 16 — Algorithm Analysis & Computational Complexity
- **Topik:** Notasi Big-O, analisis kompleksitas waktu ($O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$), kompleksitas ruang memori, komparasi efisiensi list lookup vs set/dict hash lookup.
- **Rujukan Utama:** [THINK] Appendix B ("Analysis of Algorithms"); Python TimeComplexity Wiki.
- **Rujukan Pendukung:** [LEARN] `src/algorithms/`; [CS50P] Lecture insights.
- **Materi Dapat Diadaptasi:** Benchmark waktu nyata menggunakan modul bawaan `timeit`.

#### Chapter 17 — File Handling & Data Serialization
- **Topik:** Context manager `with open()`, mode berkas (`'r'`, `'w'`, `'a'`, `'b'`), modul `csv` (`csv.reader`, `csv.DictWriter`), modul `json` (`loads`, `dumps`), penanganan path modern dengan `pathlib.Path`.
- **Rujukan Utama:** [DOCS] Section 7.2 ("Reading and Writing Files"); [CS50P] Week 6 ("File I/O").
- **Rujukan Pendukung:** [THINK] Chapter 14 ("Files"); [30DAY] Day 19 ("File Handling").
- **Materi Dapat Diadaptasi:** Membaca dan menulis file dataset CSV/JSON, penanganan encoding `utf-8`.

#### Chapter 18 — Structured Exception Handling & Debugging
- **Topik:** Hierarki class exception Python, blok `try-except-else-finally`, membangkitkan exception dengan `raise`, pembuatan custom exception class, teknik debugging menggunakan `breakpoint()` dan modul `pdb`.
- **Rujukan Utama:** [DOCS] Section 8 ("Errors and Exceptions"); [CS50P] Week 3 ("Exceptions").
- **Rujukan Pendukung:** [THINK] Chapter 11.5 ("Catching Exceptions"); [30DAY] Day 17 ("Exception Handling").
- **Materi Dapat Diadaptasi:** Pola penanganan error bertingkat dan sanitasi input pengguna.

#### Chapter 19 — Object-Oriented Programming I: Fundamentals
- **Topik:** Paradigma OOP, class vs instance, constructor method `__init__`, parameter `self`, atribut instance vs atribut class, encapsulation dasar (konvensi `_private`).
- **Rujukan Utama:** [DOCS] Section 9.1–9.4 ("A Word About Names and Objects", "Class Definition Syntax").
- **Rujukan Pendukung:** [THINK] Chapter 15 & 16 ("Classes and Objects", "Classes and Functions"); [CS50P] Week 8 ("Object-Oriented Programming").
- **Materi Dapat Diadaptasi:** Pemodelan entitas fisik perangkat pemancar BTS atau sensor telemetri.

#### Chapter 20 — Object-Oriented Programming II: Inheritance & Advanced OOP
- **Topik:** Pewarisan (*inheritance*), fungsi `super()`, polimorfisme (*method overriding*), multiple inheritance & Method Resolution Order (MRO), dunder/magic methods (`__str__`, `__repr__`, `__eq__`, `__len__`, `__add__`), decorators `@property`.
- **Rujukan Utama:** [DOCS] Section 9.5 & 9.8 ("Inheritance", "Iterators").
- **Rujukan Pendukung:** [THINK] Chapter 17 ("Classes and Methods"); [CS50P] Week 8.
- **Materi Dapat Diadaptasi:** Pola inheritance kelas perangkat jaringan (Device -> Router -> Switch), dunder methods untuk kalkulasi vektor sinyal.

#### Chapter 21 — Virtual Environments, Packaging & Testing
- **Topik:** Isolasi environment dengan `venv`, manajemen dependensi dengan `pip` dan `requirements.txt`, konfigurasi standar `pyproject.toml`, dasar automated testing dengan `pytest`.
- **Rujukan Utama:** [PYPA] ("Tutorial on Managing Application Dependencies"); [PYTEST] ("Getting Started with pytest").
- **Rujukan Pendukung:** [DOCS] Section 12 ("Virtual Environments and Packages"); [CS50P] Week 5 ("Unit Tests").
- **Materi Dapat Diadaptasi:** Struktur direktori proyek standar industri Python, penulisan fungsi pengujian `test_*()` dengan assertions.

#### Chapter 22 — Intermediate Capstone Project
- **Topik:** Proyek integrasi Level 2 Intermediate: pengembangan pustaka perangkat lunak berorientasi objek yang dilengkapi penyimpanan file I/O (CSV/JSON), penanganan error kustom, isolasi virtual environment, dan pengujian otomatis `pytest`.
- **Rujukan Utama:** [CS50P] Final Project Standards; [SWCARP] Capstone guidelines.
- **Kebutuhan Konten Asli:** Capstone Project: *"Telecom Network Element Simulator & Log Analyzer Engine"* lengkap dengan unit testing `pytest`.

---

### LEVEL 3: PROFESSIONAL PYTHON ENGINEERING (CHAPTER 23 – 30)

#### Chapter 23 — Advanced OOP & Design Patterns
- **Topik:** Abstract Base Classes (`abc.ABC`, `@abstractmethod`), Gang of Four Design Patterns terapan dalam Python (Singleton, Factory, Observer, Strategy), komposisi vs pewarisan (*composition over inheritance*).
- **Rujukan Utama:** Python Docs `abc` module documentation; [THINK] Chapter 19 ("The Goodies").
- **Rujukan Pendukung:** [LEARN] `src/design_patterns/`.
- **Materi Dapat Diadaptasi:** Implementasi pattern Factory dan Observer untuk dispatch event telemetri jaringan.

#### Chapter 24 — Decorators, Custom Generators & Context Managers
- **Topik:** Function decorators (@syntax, decorators dengan argumen), chaining decorators, generator functions dengan `yield`, generator pipelines, context managers manual (`__enter__`, `__exit__`), modul `contextlib.contextmanager`.
- **Rujukan Utama:** [DOCS] Section 9.9 & 9.10 ("Generators", "Generator Expressions"); Python Decorator Wiki.
- **Rujukan Pendukung:** [CS50P] Week 9 ("Et Cetera"); [30DAY] Day 15 ("Type Errors & Decorators").
- **Materi Dapat Diadaptasi:** Decorator pengukur waktu eksekusi (`@timing_decorator`) dan decorator logging.

#### Chapter 25 — Type Hints & Static Code Quality
- **Topik:** Type annotations (PEP 484), modul `typing` (`Union`, `Optional`, `Callable`, `Generic`), static type checker (`mypy`), validasi data runtime modern (`Pydantic`), konvensi gaya kode PEP 8, linting dengan `flake8` / `ruff`.
- **Rujukan Utama:** Python Docs `typing` library; PEP 484, PEP 8.
- **Rujukan Pendukung:** [CS50P] Week 9; Real Python Type Checking Guide.
- **Materi Dapat Diadaptasi:** Contoh migrasi kode Python dinamis ke kode dengan type hints ketat.

#### Chapter 26 — Automated Testing & Production Logging
- **Topik:** Pengujian otomatis mendalam dengan `pytest` (fixtures, `@pytest.mark.parametrize`, mocking dengan `unittest.mock`), pengukuran code coverage, penulisan log produksi dengan modul bawaan `logging` (levels, formatters, handlers, file rotation).
- **Rujukan Utama:** [PYTEST] Full Documentation; Python Docs `logging` Tutorial.
- **Rujukan Pendukung:** [CS50P] Week 5 ("Unit Tests").
- **Materi Dapat Diadaptasi:** Setup logging multi-handler (konsol warna + berkas berotasi harian).

#### Chapter 27 — Concurrent & Asynchronous Programming
- **Topik:** Perbedaan I/O-bound vs CPU-bound, Global Interpreter Lock (GIL), multi-threading (`threading`), multi-processing (`multiprocessing`), asynchronous programming (`asyncio`, `async`/`await`, event loop, `asyncio.gather`).
- **Rujukan Utama:** Python Docs `asyncio` & `multiprocessing` documentation.
- **Rujukan Pendukung:** Real Python AsyncIO in Python Tutorial.
- **Materi Dapat Diadaptasi:** Simulasi scraping I/O konkuren dan pemrosesan paralel data batch sinyal telekomunikasi.

#### Chapter 28 — Networking & REST API Integration
- **Topik:** Dasar socket programming (`socket`), protokol HTTP/HTTPS, HTTP client interaktif (`httpx` / `urllib`), perancangan backend REST API modern menggunakan `FastAPI`, request handling, serialisasi schema Pydantic, dokumentasi Swagger otomatis.
- **Rujukan Utama:** FastAPI Official Tutorial ([fastapi.tiangolo.com](https://fastapi.tiangolo.com)); Python Docs `socket`.
- **Rujukan Pendukung:** [30DAY] Day 18 ("Regular Expressions & APIs"); [CS50P] Week 4 ("Libraries").
- **Materi Dapat Diadaptasi:** Endpoint API data sensor dan pengiriman query parameter filter.

#### Chapter 29 — Software Architecture & Containerized Deployment
- **Topik:** Prinsip arsitektur perangkat lunak (Clean Architecture dasar, Service Layer), Twelve-Factor App methodology, kontainerisasi aplikasi dengan Docker (`Dockerfile`, `.dockerignore`, `docker-compose`), otomatisasi CI/CD dengan GitHub Actions.
- **Rujukan Utama:** [PYPA] Packaging Guidelines; Docker Documentation.
- **Rujukan Pendukung:** Twelve-Factor App specification ([12factor.net](https://12factor.net)).
- **Materi Dapat Diadaptasi:** Konfigurasi multi-stage Docker build untuk aplikasi Python ringan.

#### Chapter 30 — Professional Capstone Project
- **Topik:** Proyek integrasi menyeluruh tingkat profesional: perancangan sistem backend microservice lengkap dengan FastAPI, asynchronous background task, database persistent, unit & integration test `pytest` (>80% coverage), kontainerisasi Docker, dan pipeline CI/CD GitHub Actions.
- **Rujukan Utama:** Industri Best Practices & Production Python Standards.
- **Kebutuhan Konten Asli:** Capstone Project: *"Cloud-Native IoT Telecommunications Monitoring & Alerting Microservice"*.

---

## Pemetaan Referensi 25 Modul Spesialisasi (Tracks A–E)

- **Track A (`A01`–`A05`, Data Science & Visualization):** NumPy Official User Guide (BSD-3-Clause), Pandas User Guide (BSD-3-Clause), NIST Engineering Statistics Handbook (Public Domain), Matplotlib & Seaborn Official Tutorials (PSF/BSD-3-Clause), Python Data Science Handbook (Jake VanderPlas), dan Pytest `tmp_path` Docs (MIT).
- **Track B (`B01`–`B05`, AI & Machine Learning):** Scikit-Learn User Guide (Pipelines, Common Pitfalls Data Leakage, Linear/Ensemble Models, Clustering/PCA, Cross-Validation/GridSearchCV, Model Persistence `joblib` — BSD-3-Clause) dan Google Developers *Rules of Machine Learning* (CC BY 4.0).
- **Track C (`C01`–`C05`, Web Development & APIs):** HTTPX Official Documentation (BSD-3-Clause), Pydantic v2 Documentation (MIT), FastAPI Official Tutorial & Testing/Security Guides (MIT), SQLAlchemy 2.0 ORM Unified Tutorial (MIT), Python `secrets`/`hmac`/`hashlib` Docs (PSF-2.0), dan *Architecture Patterns with Python* (CC BY-NC-ND 4.0).
- **Track D (`D01`–`D05`, Automation & Scripting):** Python Official Docs (`pathlib`, `shutil`, `urllib.robotparser`, `argparse`, `logging` — PSF-2.0), OpenPyXL Documentation (MIT), fpdf2 Documentation (LGPL-3.0), Beautiful Soup 4 Documentation (MIT), dan Twelve-Factor App Guidelines (MIT).
- **Track E (`E01`–`E05`, IoT, Signal Processing & Telecommunications):** Python `struct` Docs (PSF-2.0), pySerial URL Handlers Docs (BSD-3-Clause), Eclipse Paho MQTT Python v2 Docs (EPL-2.0/EDL-1.0), OASIS MQTT Spec, SciPy FFT & Signal Processing Reference (BSD-3-Clause), serta 3GPP TS 36.214 E-UTRA Physical Layer Measurements.


