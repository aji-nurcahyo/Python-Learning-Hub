# Latihan Terarah Chapter 20: Object-Oriented Programming II

Latihan ini dirancang untuk memperdalam pemahaman mengenai Pewarisan (*Inheritance*), pemanggilan `super()`, *Method Overriding*, Polimorfisme, Komposisi (*Composition*), serta implementasi *Special Methods* (`__str__`, `__repr__`, `__eq__`, `__hash__`).

---

### Latihan 1: Single Inheritance & Pemanggilan `super()`
1. Buat class induk `NetworkInterface` dengan atribut `name: str` dan `mac_address: str`.
2. Buat class turunan `WirelessInterface` yang mewarisi `NetworkInterface` dan menambahkan atribut `ssid: str` serta `frequency_ghz: float`.
3. Gunakan `super().__init__(name, mac_address)` untuk menginisialisasi atribut induk.
4. Buat method `get_info()` pada class induk dan override pada class turunan dengan menyertakan SSID dan frekuensi.

---

### Latihan 2: Polimorfisme & Dynamic Dispatch
1. Buat class dasar `SignalProcessor` yang mendefinisikan method `proses_sinyal(self, raw_samples: list[float]) -> list[float]`.
2. Buat dua class turunan:
   - `AmplifierProcessor`: Mengalikan setiap sampel sinyal dengan faktor penguatan $G = 2.0$.
   - `NoiseFilterProcessor`: Memotong nilai sampel yang berada di bawah ambang batas $0.1$ menjadi $0.0$.
3. Tulis fungsi `pipeline_pemrosesan(processors: list[SignalProcessor], data: list[float])` yang mengeksekusi setiap processor secara polimorfik berturut-turut.

---

### Latihan 3: Komposisi ("has-a") vs Pewarisan ("is-a")
1. Rancang class `Transceiver` yang memiliki modul pemancar (`Transmitter`) dan modul penerima (`Receiver`) sebagai atribut internal (bukan pewarisan).
2. Buat method `kirim_dan_terima(payload: str)` pada `Transceiver` yang mendelegasikan tugas pengiriman ke objek `Transmitter` dan verifikasi penerimaan ke objek `Receiver`.

---

### Latihan 4: Special Methods `__eq__`, `__repr__`, dan Hashability
1. Buat class `VlanConfig` dengan atribut `vlan_id: int` dan `vlan_name: str`.
2. Implementasikan method `__str__` dan `__repr__`.
3. Implementasikan method `__eq__` sehingga dua objek `VlanConfig` bernilai sama jika `vlan_id`-nya identik.
4. Implementasikan method `__hash__` agar instance `VlanConfig` dapat dimasukkan ke dalam `set` untuk deduplikasi ID otomatis.
