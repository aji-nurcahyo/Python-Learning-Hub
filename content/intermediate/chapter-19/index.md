# Chapter 19: Object-Oriented Programming I
## Class, Object, Constructor `__init__`, Parameter `self` & Enkapsulasi

Selamat datang di **Chapter 19: Object-Oriented Programming I** pada kurikulum **Python Learning Hub**. Modul ini merupakan gerbang utama menuju paradigma pemrograman berorientasi objek (*Object-Oriented Programming* atau OOP) di lingkungan Python.

Pada modul-modul sebelumnya di Level 1 dan awal Level 2, Anda telah mempelajari paradigma imperatif dan fungsional di mana data (variabel, list, dictionary) dan fungsi pengolahnya dipisahkan secara eksplisit. Pada bab ini, Anda akan mempelajari bagaimana menyatukan data (*state*) dan perilaku (*behavior*) ke dalam satu kesatuan modular yang disebut **`class`** dan **`object`**.

---

## 1. Pengenalan Paradigma Object-Oriented Programming (OOP)

Dalam rekayasa perangkat lunak modern, paradigma berorientasi objek digunakan untuk memodelkan sistem dunia nyata secara alami. Perangkat telekomunikasi seperti *router*, *switch*, stasiun pemancar (*Base Transceiver Station* / BTS), maupun sensor telemetri tidak hanya memiliki data fisik (nomor seri, frekuensi, alamat IP), tetapi juga memiliki fungsi operasional (mengirim paket data, menyalakan alarm, mereset port).

### Prosedural vs Object-Oriented

| Aspek | Pendekatan Prosedural | Pendekatan Object-Oriented (OOP) |
| :--- | :--- | :--- |
| **Pusat Perhatian** | Rangkaian langkah instruksi dan fungsi | Entitas objek yang memiliki tanggung jawab |
| **Struktur Data** | Terpisah dari fungsi pengolahnya (misal dictionary + fungsi) | Terikat erat di dalam instance objek (*encapsulation*) |
| **Skalabilitas** | Rentan salah manipulasi data saat basis kode membesar | Sangat modular dan mudah diperluas tanpa merusak kode lain |
| **Abstraksi** | Mengandalkan parameter passing antar fungsi | Memodelkan konsep domain sistem nyata secara intuitif |

---

## 2. Anatomi Class, Constructor `__init__`, dan Parameter `self`

### A. Class vs Object
- **`class`**: Cetak biru (*blueprint*) konseptual yang mendefinisikan struktur data dan kapabilitas fungsional.
- **`object` (instance)**: Wujud konkret dari class yang dialokasikan di dalam memori komputer pada saat *runtime*.

### B. Constructor `__init__` dan Parameter `self`
Ketika kita membuat objek baru (proses *instantiation*), Python secara otomatis memanggil metode konstruktor khusus bernama `__init__`.

```python
class Rectangle:
    """Blueprint representasi bentuk persegi panjang."""
    
    def __init__(self, panjang: float, lebar: float):
        # self merujuk secara eksplisit ke objek yang sedang dibuat di memori
        self.panjang = float(panjang)
        self.lebar = float(lebar)

    def luas(self) -> float:
        """Instance method untuk menghitung luas persegi panjang."""
        return self.panjang * self.lebar
```

Mengapa harus ada parameter `self`?  
Dalam Python, filosofi desain *Zen of Python* menyatakan bahwa *"Explicit is better than implicit"*. Tidak seperti bahasa lain seperti Java atau C++ di mana pointer objek disembunyikan dalam kata kunci `this`, Python secara eksplisit mewajibkan instance objek diteruskan sebagai parameter pertama (`self`) pada setiap *instance method*.

---

## 3. Instance Attributes vs Class Attributes

Dalam perancangan class, sangat krusial membedakan antara atribut milik instance dan atribut milik class:

1. **Instance Attributes**: Didefinisikan di dalam method (biasanya di dalam `__init__`) menggunakan prefiks `self.nama_atribut`. Nilainya bersifat unik dan independen untuk setiap instance objek.
2. **Class Attributes**: Didefinisikan langsung di tubuh class di luar method apa pun. Nilainya dibagi bersama (*shared*) oleh seluruh objek turunan dari class tersebut. Cocok digunakan untuk mendefinisikan konstanta atau penghitung global (*object counter*).

```python
class NetworkDevice:
    # Class attribute: dibagi oleh seluruh instance
    vendor_default = "ITERA-Telecom"
    total_devices = 0

    def __init__(self, hostname: str):
        # Instance attribute: unik untuk objek ini saja
        self.hostname = hostname
        NetworkDevice.total_devices += 1
```

> [!WARNING]
> Jangan pernah memutasi atribut class bersama melalui `self.vendor_default = "Baru"`, karena hal tersebut justru akan menciptakan atribut *instance* baru yang menutupi atribut class (*shadowing*) khusus pada objek tersebut. Selalu mutasi class attribute menggunakan nama class secara eksplisit: `NetworkDevice.total_devices += 1`.

---

## 4. Filosofi Enkapsulasi & Proteksi Properti dengan `@property`

### Konvensi Enkapsulasi di Python
Berbeda dengan bahasa seperti C++ atau Java yang menyediakan pembatasan hak akses yang kaku (`public`, `private`, `protected`), komunitas Python berpegang pada prinsip:
> *"We are all consenting adults here."*

Python tidak mengunci atribut secara mutlak di level compiler. Sebagai gantinya, digunakan konvensi penamaan:
- **`nama` (Public)**: Dapat diakses dan diubah secara bebas oleh kode luar.
- **`_nama` (Protected)**: Penanda bagi pengembang lain bahwa atribut ini adalah internal implementasi dan tidak disarankan dimodifikasi sembarangan.
- **`__nama` (Private / Name Mangling)**: Nama variabel diubah otomatis oleh interpreter menjadi `_ClassName__nama` untuk menghindari tabrakan nama (*name collision*).

### Validasi Menggunakan Decorator `@property`
Untuk memproteksi integritas data tanpa mengorbankan sintaks akses atribut dot (`obj.atribut`), Python menyediakan *decorator* bawaan `@property` (getter) dan `@<property>.setter` (setter).

```python
class SignalTransmitter:
    def __init__(self, power_dbm: float):
        self.power_dbm = power_dbm  # Memanggil setter tervalidasi

    @property
    def power_dbm(self) -> float:
        """Getter properti."""
        return self._power_dbm

    @power_dbm.setter
    def power_dbm(self, value: float) -> None:
        """Setter dengan validasi rentang daya operasional."""
        val = float(value)
        if not (-30.0 <= val <= 50.0):
            raise ValueError(f"Daya {val} dBm di luar batas operasional [-30 s/d 50 dBm]!")
        self._power_dbm = val
```

---

## 5. Mini Proyek: Device Inventory Manager

Pada modul ini, kita merancang sistem mini proyek **Device Inventory Manager** untuk mengelola perangkat keras telekomunikasi di stasiun pemancar.
Arsitektur terdiri dari:
1. `Device`: Entitas mandiri dengan enkapsulasi properti konsumsi daya (`power_watts`) dan status aktif/nonaktif.
2. `DeviceInventory`: Pengelola koleksi perangkat dengan operasi pendaftaran (proteksi ID duplikat), penghapusan, filter kategori, dan kalkulasi agregasi daya total stasiun.

Kode modular dapat dipelajari pada direktori `content/intermediate/chapter-19/code/` dan diuji melalui unit test pada `tests/test_inventory.py`.

---

## 6. Ringkasan Bab
- Paradigma OOP menyatukan status (*attributes*) dan fungsi (*methods*) ke dalam objek mandiri.
- `class` adalah cetak biru, sedangkan `object` adalah instansiasi nyata di memori komputer.
- Method konstruktor `__init__` bertugas menginisialisasi atribut awal saat objek dibuat.
- Parameter `self` merepresentasikan objek aktif yang sedang mengeksekusi method tersebut.
- Pisahkan antara atribut *instance* (unik per objek) dan atribut *class* (bersama untuk semua objek).
- Terapkan enkapsulasi cerdas menggunakan `@property` dan `@setter` untuk menjaga validitas data sistem.
- Pada chapter berikutnya (**Chapter 20: Object-Oriented Programming II**), kita akan memperluas paradigma ini dengan konsep Pewarisan (*Inheritance*), Polimorfisme, dan *Special Methods*.
