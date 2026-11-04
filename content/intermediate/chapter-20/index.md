# Chapter 20: Object-Oriented Programming II
## Pewarisan (Inheritance), Polimorfisme, `super()`, dan Special Dunder Methods

Selamat datang di **Chapter 20: Object-Oriented Programming II** pada kurikulum **Python Learning Hub**. Melanjutkan pemahaman fondasi class dan enkapsulasi dari Chapter 19, bab ini membedah pilar-pilar tingkat lanjut dari pemrograman berorientasi objek: bagaimana membangun hierarki taksonomi melalui **Pewarisan (*Inheritance*)**, memanfaatkan pemanggilan **`super()`**, menerapkan **Polimorfisme** untuk memproses berbagai tipe data secara seragam, memahami prinsip **Komposisi vs Pewarisan**, serta menguasai **Special Methods (*Dunder Methods*)** seperti `__str__`, `__repr__`, `__eq__`, dan `__hash__`.

---

## 1. Konsep Pewarisan (Inheritance) & Relasi "is-a"

Pewarisan adalah mekanisme yang memungkinkan sebuah class baru (*child class* / *subclass*) mewarisi atribut dan method dari class yang sudah ada (*parent class* / *base class* / *superclass*).

Pewarisan digunakan ketika terdapat relasi taksonomi alami berupa *"is-a"* (adalah sebuah):
- Sebuah *Router* **adalah sebuah** *Network Device*.
- Sebuah *Cellular Antenna* **adalah sebuah** *Transceiver Node*.

### Sintaks Single Inheritance
Dalam Python, class induk ditulis di dalam tanda kurung saat mendeklarasikan class turunan:

```python
class BaseDevice:
    def __init__(self, serial_number: str, hostname: str):
        self.serial_number = serial_number
        self.hostname = hostname

class NetworkRouter(BaseDevice):
    def __init__(self, serial_number: str, hostname: str, throughput_gbps: float):
        # Memanggil constructor class induk
        super().__init__(serial_number, hostname)
        self.throughput_gbps = throughput_gbps
```

Dengan inheritance, fungsi bawaan Python seperti `isinstance()` dan `issubclass()` dapat digunakan untuk memverifikasi relasi tipe:
```python
router = NetworkRouter("RT-01", "Core-GW", 40.0)
print(isinstance(router, BaseDevice))      # True
print(issubclass(NetworkRouter, BaseDevice)) # True
```

---

## 2. Method Overriding dan Pemanggilan `super()`

### A. Method Overriding
Method overriding terjadi ketika class turunan mendefinisikan kembali suatu method yang sudah ada di class induknya dengan nama dan tanda tangan yang sama, untuk memberikan perilaku yang lebih spesifik bagi subclass tersebut.

### B. Pemanggilan `super()`
Fungsi bawaan `super()` mengembalikan objek proksi yang mendelegasikan pemanggilan method ke class induk dalam rantai Method Resolution Order (MRO). Penggunaan `super()` sangat disarankan daripada memanggil nama induk secara langsung (`BaseDevice.__init__(self, ...)`), karena:
1. Menghindari penulisan nama class induk secara hardcode.
2. Mendukung pewarisan jamak (*multiple inheritance*) secara aman dan konsisten.

```python
class TelemetrySensor:
    def baca_telemetri(self, raw_value: float) -> str:
        return f"Raw: {raw_value}"

class TemperatureSensor(TelemetrySensor):
    def baca_telemetri(self, raw_value: float) -> str:
        # Menyesuaikan perilaku dengan evaluasi termal spesifik
        status = "ALERT" if raw_value > 50.0 else "NORMAL"
        return f"[Thermal] {raw_value:.1f}°C ({status})"
```

---

## 3. Polimorfisme & Duck Typing dalam Python

### A. Polimorfisme (Dynamic Dispatch)
Polimorfisme memungkinkan method dengan antarmuka yang sama dipanggil secara seragam pada berbagai objek yang berbeda kelas. Hal ini memungkinkan pemrosesan koleksi heterogen secara elegan tanpa memerlukan rantai percabangan `if-elif isinstance(...)` yang panjang dan kaku:

```python
perangkat_jaringan = [
    BTSNode("BTS-01"),
    MicrowaveLinkNode("MW-02"),
    FiberSwitchNode("SW-03")
]

for node in perangkat_jaringan:
    # Pemanggilan method seragam secara polimorfik
    hasil = node.jalankan_diagnostik()
    print(hasil)
```

### B. Filosofi Duck Typing
Python mengusung filosofi dinamis yang dikenal sebagai *Duck Typing*:
> *"If it walks like a duck and quacks like a duck, it's a duck."*

Dalam Python, kesesuaian sebuah objek ditentukan oleh apakah objek tersebut memiliki method atau atribut yang dibutuhkan, bukan dari mana hierarki class-nya berasal. Dua objek tidak harus mewarisi class induk yang sama untuk dapat diproses secara polimorfik.

---

## 4. Komposisi vs Pewarisan ("has-a" vs "is-a")

Salah satu kesalahan paling umum bagi pengembang perangkat lunak adalah memaksakan pewarisan (*inheritance*) untuk relasi yang sebenarnya lebih tepat dimodelkan menggunakan **Komposisi (*Composition*)**.

Prinsip desain rekayasa perangkat lunak modern menyatakan:
> *"Favor object composition over class inheritance."*

| Pendekatan | Relasi Logis | Kapan Digunakan | Contoh Kasus |
| :--- | :--- | :--- | :--- |
| **Pewarisan** | *"is-a"* (adalah sebuah) | Spesialisasi murni dengan substitusi penuh | `RouterDevice` mewarisi `Device` |
| **Komposisi** | *"has-a"* (memiliki sebuah) | Entitas yang tersusun dari komponen independen | `ModularRouter` memiliki `PowerSupply` dan `list[NetworkPort]` |

Dengan komposisi, perubahan pada modul internal (misal mengganti model catu daya) tidak akan merusak kontrak atau hierarki router.

---

## 5. Special Methods (*Dunder Methods*)

Special methods (juga dikenal sebagai *magic methods* atau *dunder methods* karena diawali dan diakhiri dengan dua garis bawah ganda) memungkinkan objek buatan kita berinteraksi secara mulus dengan operasi dan fungsi bawaan Python.

### A. `__str__` vs `__repr__`
- **`__str__(self)`**: Ditujukan untuk pengguna umum (*user-friendly*). Dipanggil oleh fungsi `str(obj)` dan `print(obj)`.
- **`__repr__(self)`**: Ditujukan untuk developer dan debugging. Menghasilkan string formal yang sebisa mungkin merepresentasikan ekspresi pembuatan objek kembali. Dipanggil oleh `repr(obj)` dan saat objek berada di dalam list/koleksi.

### B. `__eq__` dan Kesetaraan vs Identitas (`is`)
- Operator `is`: Memeriksa apakah dua variabel menunjuk ke **alamat memori yang sama** (identitas fisik objek).
- Operator `==`: Memeriksa **kesetaraan nilai data**, yang perilakunya diatur oleh method `__eq__(self, other)`.

### C. Implikasi Hashability
> [!IMPORTANT]
> **Aturan Hashability Python:**  
> Ketika Anda mengoverride method `__eq__`, CPython secara otomatis menetapkan `__hash__ = None` pada class tersebut. Akibatnya, instance class menjadi *unhashable* dan **tidak dapat** dimasukkan ke dalam `set` atau dijadikan *key* pada `dict`. Jika objek Anda immutable atau memiliki identitas stabil (misalnya `serial_id` unik), Anda wajib mengimplementasikan method `__hash__(self)` yang mengembalikan nilai hash berdasarkan identitas tersebut:
> ```python
> def __hash__(self) -> int:
>     return hash(self.serial_id)
> ```

---

## 6. Mini Proyek: Multi-Device Management System

Proyek **Multi-Device Management System** pada direktori `content/intermediate/chapter-20/code/` memperluas sistem inventaris Chapter 19 dengan:
1. Class induk `Device` yang dilengkapi dengan `__str__`, `__repr__`, `__eq__`, dan `__hash__`.
2. Tiga class turunan spesifik: `RouterDevice`, `SwitchDevice`, dan `SensorDevice` yang mengoverride method `diagnostics()`.
3. Manajer sistem `MultiDeviceManager` yang mengeksekusi inspeksi perangkat secara polimorfik dan menghitung agregasi daya seluruh site.

Seluruh perilaku sistem ini divalidasi secara otomatis melalui unit test di `tests/test_multi_device.py`.

---

## 7. Ringkasan Bab
- Pewarisan (*Inheritance*) memungkinkan reuse kode melalui relasi taksonomi *"is-a"*.
- Gunakan `super()` untuk memanggil constructor dan method class induk secara dinamis dan aman.
- Method overriding memungkinkan subclass menyesuaikan perilaku spesifik tanpa merusak antarmuka publik.
- Polimorfisme memungkinkan pemrosesan koleksi objek heterogen dengan memanggil method antarmuka yang seragam.
- Utamakan komposisi (*has-a*) dibanding pewarisan (*is-a*) untuk komponen sistem yang fleksibel.
- Implementasikan `__str__` dan `__repr__` untuk representasi teks objek yang bersih.
- Implementasikan `__eq__` dan `__hash__` secara bersamaan agar objek dapat dibandingkan kesetaraan nilainya dan dapat disimpan dalam struktur `set` atau `dict`.
- Pada bab berikutnya (**Chapter 21: Packages, Environments & Testing**), kita akan belajar bagaimana mengemas modul-modul ini ke dalam paket distribusi resmi, mengelola virtual environment, dan merancang automated test suite menggunakan pytest.
