# Chapter 22: Intermediate Capstone Project
## Inventory Management System — Aplikasi Terminal Terintegrasi

Selamat datang di **Chapter 22: Intermediate Capstone Project** pada **Python Learning Hub**. Bab ini merupakan puncak kulminasi pembelajaran kurikulum **Level 2: Intermediate Python**.

Setelah mengarungi konsep-konsep tingkat menengah mulai dari manipulasi fungsi tingkat tinggi, *comprehensions*, algoritma pencarian dan pengurutan, penanganan berkas dan serialisasi data, *exception handling* defensif, pemrograman berorientasi objek hierarkis, hingga tata kelola paket dan *automated testing*, kini saatnya Anda menyatukan seluruh kompetensi tersebut ke dalam satu proyek rekayasa perangkat lunak nyata: **Inventory Management System**.

---

## 1. Ikhtisar & Tujuan Proyek

Tujuan utama dari proyek ini adalah membangun sebuah sistem aplikasi inventaris perangkat keras dan aset infrastruktur telekomunikasi berbasis baris perintah (*Command-Line Interface* atau CLI) yang tangguh, modular, teruji secara otomatis, dan memiliki persistensi data permanen di media disk.

### Spesifikasi Fungsional Inti
1. **Model Domain OOP Bertingkat**: Memodelkan berbagai jenis perangkat keras (Network Device, Server Node, Sensor Telemetri) menggunakan inheritance, encapsulation, dan method overriding.
2. **Operasi CRUD Lengkap**:
   - **Create**: Mendaftarkan entitas perangkat baru dengan validasi data ketat dan proteksi duplikasi ID.
   - **Read**: Menginspeksi detail spesifikasi perangkat tertentu atau mendaftar seluruh aset.
   - **Update**: Memperbarui harga pasar dan status operasional perangkat (aktif / non-aktif).
   - **Delete**: Menghapus perangkat yang sudah dipensiunkan dari sistem.
3. **Pencarian & Pengurutan Cerdas**:
   - Pencarian substring tidak peka huruf besar/kecil (*case-insensitive*) pada nama dan nomor seri perangkat.
   - Pengurutan multi-kriteria berdasarkan harga (termurah ke termahal atau sebaliknya), nama, maupun konsumsi daya.
4. **Penyimpanan Berkas JSON Teruji**:
   - Menyimpan seluruh data perangkat ke berkas JSON dengan encoding UTF-8.
   - Menerapkan pola *Atomic File Write* (menulis ke file `.tmp` terlebih dahulu sebelum me-replace file utama) untuk menjamin integritas data terhadap kegagalan daya mendadak.
5. **Hierarki Custom Exception**: Penanganan error terstruktur yang membedakan antara kesalahan validasi input, perangkat tidak ditemukan, ID duplikat, dan kesalahan I/O berkas.
6. **Analitik Portofolio**: Menghasilkan ringkasan manajerial yang mengagregasikan total unit aset, total valuasi finansial (Rupiah), total beban konsumsi daya operasional (Watt), dan distribusi kategori.
7. **Suite Pengujian Otomatis**: Dilengkapi dengan unit test menyeluruh berbasis `unittest` / `pytest` yang memverifikasi seluruh komponen tanpa error.

---

## 2. Arsitektur Perangkat Lunak Modular

Sistem dirancang dengan mematuhi prinsip *Separation of Concerns* (pemisahan tanggung jawab), terbagi ke dalam lapisan (*layers*) modular berikut:

```text
content/intermediate/chapter-22/
├── code/
│   ├── exceptions.py          # Hierarki custom exception domain
│   ├── validators.py          # Logika validasi input & integritas data
│   ├── domain_models.py       # Blueprint class Device & spesialisasi subclass
│   ├── storage.py             # Mesin persistensi berkas JSON (atomic write)
│   ├── inventory_manager.py   # Service layer logika bisnis & operasi CRUD
│   ├── main.py                # Antarmuka CLI menu interaktif bagi pengguna
│   └── contoh.py              # Skrip demonstrasi alur program mandiri
└── tests/
    └── test_capstone.py       # Suite pengujian otomatis komprehensif
```

### Diagram Alur Data & Komponen

```text
[ Pengguna / Terminal CLI (main.py) ]
                 │
                 ▼
[ InventoryManager (inventory_manager.py) ]
  ├── [ Validators (validators.py) ] ──── melempar ──► [ Exceptions (exceptions.py) ]
  ├── [ Domain Models (domain_models.py) ]
  └── [ Storage Handler (storage.py) ] ── I/O Disk ──► [ inventory_db.json ]
```

---

## 3. Desain Model Domain Berorientasi Objek

### A. Class Dasar: `Device`
Mendefinisikan atribut umum seluruh perangkat keras:
- `serial_id` (str): Nomor seri unik perangkat (divalidasi dengan format standar seperti `RTR-01`).
- `name` (str): Nama deskriptif perangkat.
- `category` (str): Kategori operasional (`Network`, `Server`, `Sensor`, `Storage`, `Power`).
- `price` (float): Harga perolehan aset dalam Rupiah (wajib bernilai positif).
- `power_watts` (float): Konsumsi daya listrik operasional dalam satuan Watt.
- `is_active` (bool): Status operasional perangkat.

Menerapkan special methods:
- `__str__`: Representasi teks ramah pengguna.
- `__repr__`: Representasi formal untuk keperluan debugging.
- `__eq__`: Kesetaraan nilai data berdasarkan kesamaan `serial_id`.
- `__hash__`: Hash stabil berdasarkan `serial_id` agar dapat dimasukkan ke dalam `set` atau `dict key`.

### B. Subclass Spesialisasi
1. **`NetworkDevice(Device)`**: Menambahkan spesifikasi `ports` (jumlah port fisik) dan `routing_protocol` (BGP, OSPF, Static).
2. **`ServerDevice(Device)`**: Menambahkan kapasitas `cpu_cores` dan `ram_gb`.
3. **`SensorDevice(Device)`**: Menambahkan tipe pemantauan `metric_type` (suhu, kelembaban, arus) dan `reading_unit`.

Masing-masing subclass mengoverride method `to_dict()` dan class method `from_dict()` untuk memungkinkan rekonstruksi objek polimorfik yang presisi dari berkas JSON.

---

## 4. Persistensi JSON & Teknik Atomic File Write

Salah satu risiko terbesar pada aplikasi berbasis berkas adalah korupsi data ketika proses penulisan terputus (misalnya program dihentikan paksa atau listrik padam saat file baru tertulis separuh).

Untuk mengatasi hal tersebut, modul `storage.py` menerapkan teknik **Atomic File Write**:
1. Seluruh daftar objek diserialisasi ke format JSON dan ditulis terlebih dahulu ke berkas temporer: `file_path.with_suffix(".tmp")`.
2. Setelah penulisan berkas temporer selesai 100% dan berkas tertutup rapat, berkas temporer tersebut menggantikan berkas utama secara instan (*atomic rename*) menggunakan `temp_file.replace(target_file)`.
3. Pada level sistem operasi modern, operasi *rename/replace* ini bersifat atomik, sehingga berkas basis data utama dijamin selalu dalam kondisi utuh dan valid.

---

## 5. Panduan Pengujian Otomatis

Proyek Capstone ini dilengkapi dengan suite pengujian otomatis komprehensif pada `tests/test_capstone.py`. Anda dapat menjalankan seluruh rangkaian pengujian menggunakan perintah:

```powershell
python -m unittest content/intermediate/chapter-22/tests/test_capstone.py
```

Suite pengujian memverifikasi 7 dimensi kritis:
1. `test_model_creation_and_inheritance`: Memvalidasi instansiasi model dan pewarisan atribut subclass.
2. `test_model_validation_errors`: Memverifikasi penolakan harga negatif, format serial salah, dan kategori ilegal.
3. `test_crud_lifecycle`: Menguji siklus Create, Read, Update harga/status, dan Delete.
4. `test_duplicate_and_not_found_errors`: Memastikan `DuplicateDeviceError` dan `DeviceNotFoundError` terlempar pada kondisi yang tepat.
5. `test_search_and_sorting`: Menguji pencarian substring keyword dan pengurutan harga ascending/descending.
6. `test_json_persistence`: Menguji penyimpanan dan pemulihan objek dari disk menggunakan direktori temporer terisolasi.
7. `test_portfolio_summary`: Memverifikasi kalkulasi agregasi aset finansial dan total konsumsi daya stasiun.

---

## 6. Rubrik Penilaian Capstone (Total: 100 Poin)

| Komponen Penilaian | Bobot | Kriteria Evaluasi Eksplisit |
| :--- | :---: | :--- |
| **Fungsionalitas Inti & CRUD** | 25 Poin | Operasi Create, Read, Update, Delete, Search, dan Sort berfungsi 100% tanpa crash atau silent failure. |
| **Desain OOP & Arsitektur Class** | 20 Poin | Pewarisan class bersih, pemanggilan `super()` tepat, enkapsulasi data terpenuhi, dan special methods dunder terimplementasi. |
| **Persistensi & Validasi Data** | 20 Poin | Penyimpanan JSON handal dengan atomic write, validasi input menolak data ilegal, dan custom exception tertangani rapi. |
| **Automated Testing & Reliability** | 20 Poin | Suite pengujian otomatis komprehensif menguji skenario sukses, skenario boundary, penanganan error, serta kelangsungan data. |
| **Dokumentasi & Standar Kode PEP 8** | 15 Poin | Struktur proyek modular, type hints lengkap, docstring informatif, antarmuka CLI ramah pengguna, dan panduan penggunaan jelas. |

---

## 7. Refleksi & Penutupan Level 2

Selamat atas keberhasilan Anda menuntaskan seluruh kurikulum **Level 2: Intermediate Python**! 

Dengan menyelesaikan Chapter 22, Anda telah membuktikan penguasaan komprehensif atas:
- Pemrograman fungsional dan manipulasi koleksi data mutakhir.
- Analisis algoritma pencarian dan pengurutan efisien.
- Persistensi file dan Exception Handling defensif.
- Pemrograman berorientasi objek hierarkis dan *special dunder methods*.
- Pengemasan paket terstandar dan *automated unit testing*.

Fondasi kokoh ini menjadi batu loncatan sempurna untuk melangkah ke **Level 3: Professional Python (Chapter 23–30)**, di mana kita akan mendalami *Design Patterns*, pemrograman asinkron tingkat tinggi (`asyncio`), arsitektur REST API, dan *deployment* aplikasi tingkat industri.
