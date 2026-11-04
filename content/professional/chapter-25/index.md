# Chapter 25: Type Hints & Code Quality
## Static Typing, Generic Types, Protocols & Code Formatting

Selamat datang di **Chapter 25: Type Hints & Code Quality** pada tingkat **Level 3: Professional Python Engineering** di **Python Learning Hub**.

Python terkenal dengan karakteristik pengetikan dinamisnya (*dynamic typing*), di mana tipe variabel ditentukan saat runtime. Meskipun fleksibilitas ini mempercepat proses pengembangan awal, pada sistem berskala besar yang dikerjakan oleh puluhan perekayasa, pengetikan dinamis murni dapat menimbulkan bug tersembunyi yang baru terungkap saat aplikasi telah berjalan di server produksi.

Modul ini membahas ekosistem **Type Hints modern (Python 3.10+)**, bagaimana menggabungkan static typing dengan idiom alami Python melalui `TypedDict` dan `Protocol`, serta pemanfaatan linter modern (seperti **Ruff**) dan static type checker (**mypy**) untuk menjamin keandalan perangkat lunak.

---

## 1. Dynamic Typing vs Static Type Checking

Di Python, tipe data terikat pada nilai objek di memori, bukan pada nama variabel:
```python
x = 42        # x mengikat objek int
x = "halo"    # x sekarang mengikat objek str (valid secara runtime)
```

Mulai Python 3.5 (PEP 484) hingga perkembangan mutakhir di Python 3.10–3.12, Python mendukung **sistem anotasi tipe (*type annotations*)**:
```python
def calculate_snr(signal_power: float, noise_power: float) -> float:
    return round(signal_power / noise_power, 3)
```

### Karakteristik Penting Anotasi Tipe di Python
1. **Tidak Memengaruhi Performa Runtime:** CPython interpreter mengabaikan anotasi tipe saat menjalankan bytecode. Anotasi tipe murni beroperasi sebagai metadata instruksi bagi editor (IDE) dan alat analisis statis.
2. **Tidak Otomatis Menolak Tipe Salah saat Runtime:** Memanggil `calculate_snr("100", 2)` tidak akan dicegah oleh Python secara langsung kecuali ada validasi kode eksplisit.
3. **Dokumentasi yang Dapat Diuji:** Mengubah komentar docstring menjadi kontrak formal yang dapat diverifikasi oleh mesin secara otomatis (*machine-verifiable contracts*).

---

## 2. Sintaksis Type Hints Modern (Python 3.10+)

### A. Union Types Modern (`|`)
Sebelum Python 3.10, pengembang harus mengimpor `Union` dari modul `typing`. Sekarang, operator pipa (`|`) dapat digunakan secara langsung (PEP 604):
```python
# Modern Python 3.10+
def format_freq(freq: int | float) -> str:
    return f"{freq:.2f} MHz"
```

### B. Nilai Opsional dan Type Narrowing
Alih-alih `Optional[str]`, gunakan `str | None`. Ketika berhadapan dengan tipe gabungan, gunakan `isinstance()` untuk melakukan **penyempitan tipe (*type narrowing*)**:

```python
def parse_payload(raw: str | None) -> str:
    # Sebelum if: tipe adalah str | None
    if raw is None:
        return "[KOSONG]"
    # Di dalam blok ini: type checker mengetahui raw pasti str
    return raw.strip().upper()
```

### C. Generik Bawaan Koleksi (PEP 585)
Gunakan koleksi standar bawaan tanpa mengimpor `List`, `Dict`, `Tuple` dari modul typing:
```python
active_ips: list[str] = ["10.0.0.1", "10.0.0.2"]
metrics_map: dict[str, float] = {"snr": 18.5, "rsrp": -82.0}
point: tuple[int, int] = (100, 200)
```

---

## 3. Kamus Terstruktur dengan `TypedDict`

Python sering menggunakan dictionary untuk pertukaran data JSON. Namun, dictionary generik `dict[str, Any]` tidak memberikan informasi tipe spesifik pada masing-masing kunci.

**`TypedDict`** (PEP 589) menetapkan skema tipe eksplisit pada setiap kunci dictionary tanpa mengubahnya menjadi objek class yang berat:

```python
from typing import TypedDict, NotRequired

class CellTelemetryRecord(TypedDict):
    cell_id: str
    rsrp_dbm: float
    is_active: bool
    azimuth: NotRequired[int]  # Kunci opsional
```

Saat menggunakan `rec: CellTelemetryRecord`, IDE akan memberikan autocompletion nama kunci dan type checker akan menandai error jika kunci wajib terlewatkan.

---

## 4. Antarmuka Struktural dengan `Protocol`

Dalam paradigma OOP nominal (seperti Java atau C++), suatu class hanya dianggap memiliki tipe antarmuka jika class tersebut secara eksplisit menyatakan pewarisan (`class MySensor(AbstractSensor):`).

Python mendukung paradigma **duck typing**: *"Jika ia berjalan seperti bebek dan bersuara seperti bebek, maka ia adalah bebek."*

Melalui **`typing.Protocol`** (PEP 544), kita dapat mendefinisikan antarmuka struktural (*structural subtyping*). Class mana pun yang memiliki method sesuai kontrak otomatis dianggap kompatibel, tanpa perlu mewarisi class induk:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Transmittable(Protocol):
    def serialize_payload(self) -> str:
        ...

class SensorPayload:
    # Memenuhi kontrak Transmittable tanpa menyatakan inheritance
    def serialize_payload(self) -> str:
        return "SENSOR_DATA:OK"
```

Dengan menambahkan `@runtime_checkable`, kita juga dapat menggunakan `isinstance(obj, Transmittable)` saat runtime!

---

## 5. Generic Classes dengan `TypeVar` dan `Generic[T]`

Ketika membuat wadah penyimpanan (*container*) atau algoritma pemrosesan yang dapat bekerja dengan beragam jenis data, kita menggunakan **Generic Types** untuk mencegah hilangnya informasi tipe:

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class TelemetryRepository(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_latest(self) -> T | None:
        return self._items[-1] if self._items else None
```

Saat dideklarasikan `repo: TelemetryRepository[float]`, metode `get_latest()` dijamin mengembalikan `float | None`, bukan `Any`.

---

## 6. Standar PEP 8, Ruff, dan Analisis Statis Mypy

### A. Konvensi PEP 8
- **Nama Class:** `PascalCase` (contoh: `NetworkController`, `DeviceFactory`).
- **Nama Fungsi & Variabel:** `snake_case` (contoh: `calculate_path_loss`, `power_dbm`).
- **Nama Konstanta:** `UPPER_SNAKE_CASE` (contoh: `MAX_RETRIES`, `DEFAULT_TIMEOUT`).
- **Indentasi:** Tepat 4 spasi (bukan tab).

### B. Perkakas Analisis Statis
1. **Mypy:** Menjalankan pengecekan tipe statis di seluruh file Python tanpa menjalankan program:
   ```bash
   mypy src/
   ```
2. **Ruff:** Linter dan code formatter modern berkecepatan tinggi yang menggantikan gabungan flake8, isort, dan black:
   ```bash
   ruff check .
   ruff format .
   ```

---

## 7. Rangkuman & Langkah Selanjutnya

- **Type Hints** mengubah kode Python menjadi basis data yang aman, terdokumentasi, dan terverifikasi secara statis.
- **TypedDict** memberikan type safety pada struktur JSON tanpa overhead serialisasi class.
- **Protocol** menyatukan fleksibilitas duck-typing dengan kekuatan static checking.
- **Generic (`Generic[T]`)** membangun abstraksi komponen data tanpa kebocoran tipe `Any`.
- **Ruff dan Mypy** adalah perkakas wajib untuk menjamin kualitas kode di lingkungan industri modern.

Pada modul berikutnya di **Chapter 26**, kita akan melengkapi keandalan perangkat lunak dengan teknik **Advanced Testing, Mocking, Coverage, dan Logging**.
