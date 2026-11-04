# Chapter 23: Advanced OOP & Design Patterns
## Abstract Base Classes, Dataclasses, Composition & Design Patterns

Selamat datang di **Chapter 23: Advanced OOP & Design Patterns** pada tingkat **Level 3: Professional Python Engineering** di **Python Learning Hub**.

Pada modul-modul sebelumnya, Anda telah menguasai dasar-dasar pemrograman berorientasi objek (OOP), termasuk pembuatan class, enkapsulasi, pewarisan (*single inheritance*), dan pemanfaatan metode khusus (*dunder methods*). Pada bab ini, kita melangkah ke standar rekayasa perangkat lunak tingkat profesional: merancang sistem berskala besar yang bersih, modular, mudah diuji (*testable*), dan siap dievolusikan tanpa merusak fungsionalitas yang telah ada.

---

## 1. Abstraksi dan Interface-Based Design

Dalam sistem perangkat lunak yang kompleks, seperti sistem kendali jaringan telekomunikasi atau infrastruktur komputasi awan, salah satu tantangan terbesar adalah menghindari ketergantungan erat (*tight coupling*) antara modul pemanggil dan modul pelaksana.

Abstraksi memungkinkan kita mendefinisikan **kontrak antarmuka (*interface contract*)** eksplisit: apa yang harus dilakukan oleh suatu komponen, tanpa mengikat implementasi konkret mengenai bagaimana tugas tersebut dikerjakan.

### Keuntungan Interface-Based Design
1. **Penegakan Kontrak Formal:** CPython runtime menjamin bahwa setiap modul anak wajib mengimplementasikan method yang dijanjikan.
2. **Polimorfisme Tanpa Ambiguitas:** Komponen konsumen dapat berinteraksi dengan berbagai jenis perangkat keras melalui satu antarmuka yang seragam.
3. **Kemudahan Pengujian (Mockability):** Mempermudah pembuatan tiruan (*mock objects*) saat menjalankan unit testing tanpa menyentuh perangkat keras fisik.

---

## 2. Abstract Base Classes (ABC) dan `@abstractmethod`

Python menyediakan modul bawaan **`abc`** (*Abstract Base Classes*) untuk mendefinisikan class abstrak dan method abstrak melalui decorator `@abstractmethod`.

Jika suatu class mewarisi `ABC` dan memiliki setidaknya satu `@abstractmethod`, class tersebut **tidak dapat diinstansiasi secara langsung**. Upaya membuat objek langsung akan memicu `TypeError`.

```python
from abc import ABC, abstractmethod

class AbstractDevice(ABC):
    def __init__(self, device_id: str, name: str) -> None:
        self.device_id = device_id
        self.name = name

    @abstractmethod
    def ping(self) -> bool:
        """Memeriksa konektivitas simpul."""
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Mengembalikan status operasional perangkat."""
        pass
```

Setiap subclass konkret wajib mengimplementasikan `ping()` dan `get_status()`. Jika ada method abstrak yang terlewat, subclass tersebut tetap dianggap abstrak dan ditolak saat instansiasi.

---

## 3. Konfigurasi Sistem dengan Dataclass

Diperkenalkan secara resmi melalui PEP 557 pada Python 3.7, modul bawaan **`dataclasses`** menyediakan decorator `@dataclass` yang mengotomatisasi pembuatan method boiler-plate seperti `__init__()`, `__repr__()`, dan perbandingan kesetaraan `__eq__()`.

Untuk data konfigurasi yang tidak boleh diubah setelah proses inisialisasi (*immutable*), gunakan parameter `frozen=True`:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class NetworkConfig:
    host: str
    port: int = 8080
    timeout_sec: float = 5.0
    allowed_ips: list[str] = field(default_factory=lambda: ["127.0.0.1", "192.168.1.1"])

    def endpoint(self) -> str:
        return f"{self.host}:{self.port}"
```

Penggunaan dataclass meningkatkan keterbacaan kode, menjamin kejelasan struktur data antar tim pengembang, dan meminimalisir bug akibat mutasi state yang tidak disengaja.

---

## 4. Enkapsulasi Nilai dengan Validated Properties

Validasi integritas data merupakan pilar keandalan sistem. Dengan memanfaatkan decorator `@property` dan `@setter`, kita dapat mengekspos atribut layaknya field publik biasa bagi pemanggil kode, namun tetap menjalankan validasi defensif di belakang layar.

```python
class SignalTransmitter:
    def __init__(self, transmitter_id: str, power_dbm: float = 20.0) -> None:
        self.transmitter_id = transmitter_id
        self._power_dbm = 0.0
        self.power_dbm = power_dbm  # Memanggil property setter

    @property
    def power_dbm(self) -> float:
        return self._power_dbm

    @power_dbm.setter
    def power_dbm(self, value: float) -> None:
        if not (-30.0 <= value <= 50.0):
            raise ValueError(f"Daya {value} dBm di luar batas legal (-30 hingga 50 dBm)")
        self._power_dbm = float(value)
```

---

## 5. Composition Over Inheritance

Salah satu prinsip terpenting dalam arsitektur perangkat lunak berorientasi objek adalah:
> **"Favor object composition over class inheritance."** (Gang of Four)

Pewarisan (*inheritance* / hubungan *is-a*) menciptakan keterikatan yang sangat kuat antara class induk dan class anak. Perubahan kecil pada class induk dapat merusak perilaku subclass (*Fragile Base Class Problem*).

Sebaliknya, **komposisi (*composition* / hubungan *has-a*)** merakit fungsionalitas kompleks dengan menggabungkan objek-objek mandiri yang berukuran lebih kecil.

| Karakteristik | Pewarisan (*Inheritance*) | Komposisi (*Composition*) |
|:---|:---|:---|
| **Hubungan Relasional** | *Is-A* (misal: `RadioNode is an AbstractDevice`) | *Has-A* (misal: `Node has a PowerSupply`) |
| **Keterikatan (*Coupling*)** | Erat (*Tight coupling*) | Longgar (*Loose coupling*) |
| **Fleksibilitas Runtime** | Kaku (ditentukan saat penulisan kode/compile time) | Dinamis (komponen dapat ditukar saat program berjalan) |
| **Kemudahan Pengujian** | Sulit diisolasi tanpa instansiasi hirarki induk | Sangat mudah diuji menggunakan mock object |

---

## 6. Prinsip Desain SOLID (Tingkat Pengantar)

Prinsip SOLID merupakan lima pedoman fundamental rekayasa perangkat lunak:
1. **Single Responsibility Principle (SRP):** Satu class hanya boleh memiliki satu alasan untuk berubah. Pisahkan logika pemrosesan data, penyimpanan berkas, dan penyajian antarmuka.
2. **Open/Closed Principle (OCP):** Entitas perangkat lunak harus terbuka untuk penambahan fitur baru (*open for extension*), tetapi tertutup untuk modifikasi kode inti yang telah teruji (*closed for modification*).
3. **Liskov Substitution Principle (LSP):** Objek dari subclass harus dapat menggantikan objek dari class induk tanpa mengubah kebenaran jalannya program.
4. **Interface Segregation Principle (ISP):** Lebih baik memiliki banyak antarmuka kecil yang spesifik daripada satu antarmuka raksasa dengan method yang tidak dibutuhkan oleh implementor.
5. **Dependency Inversion Principle (DIP):** Modul tingkat tinggi tidak boleh bergantung langsung pada modul tingkat rendah; keduanya harus bergantung pada abstraksi (antarmuka/ABC).

---

## 7. Pola Desain (Design Patterns)

### A. Factory Pattern (Pola Kreasi)
Factory Pattern mengisolasi logika penentuan tipe dan pembuatan objek ke dalam satu entitas pembuat (*factory*). Konsumen sistem cukup meminta objek berdasarkan string atau parameter konfigurasi tanpa perlu mengimpor class konkret secara langsung.

```python
class DeviceFactory:
    _registry = {"radio": RadioDevice, "optical": OpticalDevice}

    @classmethod
    def create(cls, device_type: str) -> AbstractDevice:
        target_cls = cls._registry.get(device_type.lower())
        if not target_cls:
            raise ValueError(f"Tipe '{device_type}' tidak terdaftar.")
        return target_cls()
```

### B. Strategy Pattern (Pola Perilaku)
Strategy Pattern mendefinisikan sekumpulan algoritma yang memiliki antarmuka serupa, mengemas masing-masing algoritma ke dalam class terpisah, dan membuatnya dapat saling dipertukarkan secara dinamis saat runtime (*interchangeable algorithms*).

Contoh: Menukar strategi encoding payload dari `PlainStrategy` ke `HexStrategy` atau strategi pengalokasian antrean dari `PriorityRouting` ke `RoundRobinRouting`.

### C. Dependency Injection Basics
Alih-alih membuat dependensi secara internal di dalam constructor (`self.logger = ConcreteLogger()`), dependensi dilewatkan dari luar melalui parameter constructor (`def __init__(self, logger: AbstractLogger): self.logger = logger`). Hal ini membuat class bisnis sepenuhnya terisolasi dan mudah diuji.

---

## 8. Menghindari Perangkap Desain (Overengineering)

Pola desain adalah solusi teruji untuk masalah umum, namun penerapannya secara membabi-buta dapat memicu arsitektur yang berlebihan (*overengineering*):
- **Premature Abstraction:** Menulis puluhan layer abstraksi untuk sistem sederhana yang tidak pernah berubah.
- **God Class:** Membuat satu class raksasa yang mencoba mengendalikan seluruh sistem secara monolitik.
- **YAGNI (You Aren't Gonna Need It):** Hanya bangun fleksibilitas jika persyaratan fungsional atau kebutuhan bisnis nyata membutuhkannya.

---

## 9. Rangkuman & Langkah Selanjutnya

- **Abstract Base Classes (`abc.ABC`)** menjamin kepatuhan implementasi method abstrak pada sistem berorientasi objek.
- **`@dataclass`** menyajikan sintaks bersih dan deklaratif untuk struktur data dan konfigurasi immutable.
- **Composition over Inheritance** menghasilkan basis kode yang fleksibel, modular, dan terisolasi dengan baik.
- **Factory dan Strategy Pattern** memisahkan pembuatan objek dari penggunaan bisnisnya dan memungkinkan penggantian algoritma secara dinamis.

Pada modul berikutnya di **Chapter 24**, kita akan menjelajahi kekuatan metaprogramming Python: **Decorators, Generators, dan Context Managers**.
