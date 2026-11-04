# Tugas Mandiri: Telecommunications Station Inventory Manager
## Chapter 19 — Object-Oriented Programming I

### Deskripsi Tugas
Anda diminta untuk membangun sistem inventaris perangkat keras stasiun pemancar telekomunikasi menggunakan paradigma Object-Oriented Programming (OOP) berbasis Python. 

Pada tugas ini, **jangan gunakan inheritance (pewarisan)** karena materi inheritance akan dipelajari pada Chapter 20. Fokuskan implementasi pada pembuatan class tunggal, constructor `__init__`, parameter `self`, atribut instance vs class, serta enkapsulasi menggunakan decorator `@property`.

---

### Kriteria Kebutuhan Teknis

1. **Class `StationDevice`**:
   - Atribut instance: `serial_id` (str), `device_name` (str), `vendor` (str), `operating_freq_mhz` (float), `power_watts` (float).
   - Enkapsulasi `@property`:
     - `operating_freq_mhz`: batas valid $700.0 \text{ MHz} \le \text{frekuensi} \le 6000.0 \text{ MHz}$.
     - `power_watts`: batas valid $0.0 \text{ W} \le \text{daya} \le 2000.0 \text{ W}$.
   - Method `info()` -> mengembalikan format deskripsi ringkas string.
   - Method `to_dict()` -> mengembalikan dictionary representasi atribut.

2. **Class `StationInventory`**:
   - Atribut instance: `station_id` (str), `location_name` (str), dan koleksi privat `_devices` (dictionary mapping `serial_id` -> instance `StationDevice`).
   - Method `add_device(dev: StationDevice)` -> melempar `KeyError` jika ID duplikat.
   - Method `remove_device(serial_id: str)` -> melempar `KeyError` jika ID tidak ada.
   - Method `search_by_vendor(vendor: str)` -> mencari perangkat berdasarkan nama vendor (case-insensitive).
   - Method `calculate_total_power()` -> menghitung total konsumsi daya stasiun.
   - Method `summary_report()` -> mencetak laporan ringkas status stasiun.

---

### Rubrik Penilaian (Total: 100 Poin)

| Kriteria Penilaian | Bobot | Deskripsi Indikator |
| :--- | :---: | :--- |
| **Desain Class & Constructor** | 25 Poin | Class `StationDevice` terdefinisi rapi, parameter `self` digunakan dengan benar, atribut instance dan class terpisah jelas. |
| **Enkapsulasi & Validasi @property** | 25 Poin | Getter dan setter `@property` untuk frekuensi dan daya terimplementasi dengan validasi batas rentang dan penanganan `ValueError`. |
| **Operasi Manajemen Inventaris** | 25 Poin | Class `StationInventory` berhasil melakukan penambahan (dengan proteksi duplikasi), penghapusan, pencarian vendor, dan kalkulasi total daya. |
| **Dokumentasi & Standar Kode PEP 8** | 15 Poin | Type hint lengkap, docstring jelas, penamaan atribut privat dengan konvensi garis bawah `_`, dan struktur kode modular. |
| **Uji Eksekusi & Test Cases** | 10 Poin | Skrip demonstrasi pada blok `if __name__ == '__main__':` berjalan tanpa error dan menguji kasus normal serta kasus boundary/exception. |
