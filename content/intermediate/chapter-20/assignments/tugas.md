# Tugas Mandiri: Hierarchical Telecom Infrastructure Management
## Chapter 20 — Object-Oriented Programming II

### Deskripsi Tugas
Anda ditugaskan oleh operator telekomunikasi untuk merancang arsitektur manajemen infrastruktur jaringan bertingkat menggunakan konsep Pewarisan (*Inheritance*), *Method Overriding*, pemanggilan `super()`, Polimorfisme, dan *Special Methods* (`__str__`, `__repr__`, `__eq__`, `__hash__`).

Sistem harus mampu mengelola tiga jenis perangkat spesifik di stasiun pemancar:
1. `CellularAntenna` (Antena Seluler 4G/5G)
2. `MicrowaveLink` (Link Transmisi Gelombang Mikro Antar-Tower)
3. `FiberOpticNode` (Node Terminasi Kabel Serat Optik)

---

### Kriteria Kebutuhan Teknis

1. **Class Induk `TransceiverNode`**:
   - Atribut instance: `node_id: str`, `site_name: str`, `power_consumption_w: float`.
   - Method `run_diagnostics() -> dict`: Mengembalikan dictionary diagnosa dasar.
   - Special Methods:
     - `__str__`: Mengembalikan string ringkas ramah pengguna.
     - `__repr__`: Mengembalikan string representasi formal yang reproducible.
     - `__eq__`: Membandingkan kesetaraan berdasarkan `node_id`.
     - `__hash__`: Menghasilkan hash berdasarkan `node_id` agar dapat dimasukkan ke dalam `set`.

2. **Class Turunan `CellularAntenna`**:
   - Menambahkan atribut: `mimo_config: str` (misal `"4x4 MIMO"`) dan `azimuth_deg: float`.
   - Override `run_diagnostics()` dengan memanggil `super().run_diagnostics()` dan menyematkan parameter MIMO dan sudut azimuth.

3. **Class Turunan `MicrowaveLink`**:
   - Menambahkan atribut: `frequency_ghz: float` dan `capacity_mbps: float`.
   - Override `run_diagnostics()` dengan memanggil `super().run_diagnostics()` dan menyematkan frekuensi dan kapasitas tautan.

4. **Class Turunan `FiberOpticNode`**:
   - Menambahkan atribut: `core_count: int` dan `rx_optical_power_dbm: float`.
   - Override `run_diagnostics()` dan menyematkan evaluasi redaman optik.

5. **Class `TelecomInfrastructureManager`**:
   - Menyimpan koleksi objek `TransceiverNode` dalam dictionary privat.
   - Method `register_node(node: TransceiverNode)`: Mencegah duplikasi ID (`KeyError`).
   - Method `execute_system_diagnostics()`: Menjalankan eksekusi polimorfik diagnostik pada seluruh perangkat yang terdaftar.
   - Method `total_power_load()`: Menghitung total konsumsi daya stasiun.

---

### Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Indikator |
| :--- | :---: | :--- |
| **Pewarisan & Pemanggilan super()** | 25 Poin | Hirarki inheritance bersih, pemanggilan `super().__init__()` benar, tidak ada duplikasi atribut induk di class turunan. |
| **Method Overriding & Polimorfisme** | 25 Poin | Method `run_diagnostics()` di-override dengan rapi pada setiap subclass dan dieksekusi secara polimorfik dalam satu loop koleksi heterogen. |
| **Implementasi Special Methods** | 20 Poin | `__str__`, `__repr__`, `__eq__`, dan `__hash__` diimplementasikan dengan benar serta teruji fungsinya (termasuk deduplikasi dalam `set`). |
| **Arsitektur Manajer & Eksekusi** | 15 Poin | Class `TelecomInfrastructureManager` mengelola pendaftaran, diagnostik, dan kalkulasi agregasi daya dengan benar. |
| **Kualitas Kode, Type Hint & PEP 8** | 15 Poin | Kode rapi, type hint lengkap, docstring jelas, dan penanganan boundary condition diterapkan secara konsisten. |
