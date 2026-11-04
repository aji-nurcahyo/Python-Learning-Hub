# Latihan Terarah Chapter 19: Object-Oriented Programming I

Latihan ini dirancang untuk melatih kemampuan merancang *class*, menggunakan *constructor* `__init__`, parameter `self`, atribut *instance* vs *class*, serta enkapsulasi menggunakan `@property`.

---

### Latihan 1: Membuat Class Mahasiswa & Predikat Kelulusan
1. Buat class `Mahasiswa` dengan atribut instance `nim` (string), `nama` (string), dan `ipk` (float).
2. Terapkan validasi pada constructor: jika IPK < 0.0 atau > 4.0, lempar exception `ValueError`.
3. Buat instance method `hitung_predikat()` yang mengembalikan:
   - `"Dengan Pujian (Cumlaude)"` jika IPK $\ge 3.50$.
   - `"Sangat Memuaskan"` jika $3.00 \le \text{IPK} < 3.50$.
   - `"Memuaskan"` jika $\text{IPK} < 3.00$.

---

### Latihan 2: Perbedaan Instance Attributes dan Class Attributes
1. Rancang class `ServerNode` yang memiliki:
   - Atribut class `total_server_aktif: int = 0`.
   - Atribut instance `node_id: str` dan `status: str = "OFFLINE"`.
2. Buat method `start_node()` yang mengubah status menjadi `"ONLINE"` dan menambah `total_server_aktif` sebanyak 1.
3. Buat method `stop_node()` yang mengubah status menjadi `"OFFLINE"` dan mengurangi `total_server_aktif` sebanyak 1.
4. Uji dengan membuat 3 instance node dan periksa nilai `ServerNode.total_server_aktif`.

---

### Latihan 3: Enkapsulasi & Proteksi Properti (@property)
1. Buat class `AntennaTransmitter` yang memiliki atribut privat `_frekuensi_mhz`.
2. Gunakan decorator `@property` untuk membuat getter `frekuensi_mhz`.
3. Buat setter `@frekuensi_mhz.setter` yang membatasi input hanya pada rentang spektrum telekomunikasi valid ($700.0 \le \text{frekuensi} \le 3500.0$ MHz).
4. Jika input di luar rentang, lempar exception `ValueError`.

---

### Latihan 4: Manajemen Koleksi Perangkat dalam Inventaris
1. Rancang class `RackCabinet` yang merepresentasikan rak server dengan kapasitas slot terbatas (misal 10 slot).
2. Sediakan method `tambah_device(device)` yang memeriksa apakah rak sudah penuh sebelum menambahkan perangkat.
3. Buat method `daftar_perangkat()` dan `hitung_total_daya()` yang menjumlahkan konsumsi daya seluruh perangkat yang terpasang di rak.
