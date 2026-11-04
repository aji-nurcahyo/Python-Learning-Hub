# Tugas Mandiri: Intermediate Capstone Project — Inventory Management System
## Chapter 22 — Intermediate Capstone Project

### Deskripsi Proyek
Sebagai proyek pamungkas Level 2 (Intermediate Python), Anda ditugaskan untuk membangun sebuah aplikasi terminal profesional: **Inventory Management System**.

Sistem ini dirancang untuk mengelola inventaris aset perangkat teknologi informasi dan infrastruktur telekomunikasi secara komprehensif. Anda harus memadukan seluruh kompetensi yang telah dipelajari sepanjang Chapter 13 hingga 21:
- Paradigma Object-Oriented Programming bertingkat (*Inheritance*, *Polymorphism*, `@property`).
- Special methods dunder (`__str__`, `__repr__`, `__eq__`, `__hash__`).
- Pemrosesan koleksi data (*Searching*, *Sorting*, *Comprehensions*).
- Persistensi data disk permanen (*JSON storage* dengan *atomic file write*).
- Validasi data defensif dan hierarki *custom exceptions*.
- Arsitektur modular terpisah (*domain models*, *storage*, *service*, *CLI interface*).
- Suite pengujian otomatis (*automated unit tests*).

---

### Kebutuhan Fungsional & Non-Fungsional

1. **Model Domain & Hierarki OOP**:
   - Class dasar `Device` dengan atribut: `serial_id`, `name`, `category`, `price`, `power_watts`, `is_active`.
   - Subclass `NetworkDevice`: Menambahkan `ports` dan `routing_protocol`.
   - Subclass `ServerDevice`: Menambahkan `cpu_cores` dan `ram_gb`.
   - Subclass `SensorDevice`: Menambahkan `metric_type` dan `reading_unit`.
   - Setiap class mengimplementasikan `to_dict()`, `from_dict()`, `__str__`, `__repr__`, dan `__eq__`.

2. **Operasi CRUD & Pencarian**:
   - **Create**: Mendaftarkan perangkat baru dengan pencegahan ID duplikat (`DuplicateDeviceError`).
   - **Read**: Mengambil perangkat berdasarkan serial ID atau menampilkan semua perangkat.
   - **Update**: Memperbarui harga dan mengubah status operasional (`toggle_status`).
   - **Delete**: Menghapus perangkat dari sistem dengan aman (`DeviceNotFoundError`).
   - **Search**: Mencari perangkat berdasarkan kata kunci pada nama atau serial ID.
   - **Sort**: Mengurutkan perangkat berdasarkan harga (termurah/termahal), nama, atau konsumsi daya.

3. **Persistensi File Teruji**:
   - Menyimpan seluruh data perangkat ke berkas JSON dengan encoding UTF-8.
   - Memulihkan objek kembali ke instance class spesifiknya saat aplikasi dijalankan kembali.
   - Menerapkan teknik *atomic write* (`.tmp` lalu `replace`) untuk integritas data.

4. **Pengujian Terotomasi**:
   - Minimal 6 kasus pengujian pada suite `unittest`/`pytest` yang mencakup: validasi model, operasi CRUD, pendeteksian duplikasi, pengurutan, dan pemulihan dari berkas JSON.

---

### Rubrik Penilaian Capstone (Total: 100 Poin)

| Komponen Penilaian | Bobot | Kriteria Evaluasi Eksplisit |
| :--- | :---: | :--- |
| **Fungsionalitas Inti & CRUD** | 25 Poin | Operasi Create, Read, Update, Delete, Search, dan Sort berfungsi 100% tanpa celah crash atau silent error. |
| **Desain OOP & Arsitektur Class** | 20 Poin | Pewarisan class bersih, pemanggilan `super()` tepat, enkapsulasi data terpenuhi, dan special methods (`__str__`, `__repr__`, `__eq__`, `__hash__`) terimplementasi. |
| **Persistensi & Validasi Data** | 20 Poin | Penyimpanan JSON handal, teknik *atomic write* aktif, validasi input menolak data ilegal, dan custom exception tertangani rapi. |
| **Automated Testing & Reliability** | 20 Poin | Suite pengujian otomatis komprehensif menguji skenario sukses, skenario boundary, penanganan error, serta kelangsungan data. |
| **Dokumentasi & Standar Kode PEP 8** | 15 Poin | Struktur proyek modular, type hints lengkap, docstring informatif, antarmuka CLI ramah pengguna, dan panduan penggunaan jelas. |

