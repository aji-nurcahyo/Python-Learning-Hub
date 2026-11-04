# Latihan Mandiri: Type Hints & Code Quality (Chapter 25)

Selamat datang di latihan mandiri Chapter 25. Pada modul ini, Anda akan mempraktikkan penulisan type hints modern (Python 3.10+), pembuatan skema data dengan `TypedDict`, penerapan antarmuka struktural (*duck typing*) menggunakan `Protocol`, serta pemanfaatan generic class dengan `TypeVar`.

---

## Latihan 1: Union Types & Modern Type Narrowing
Buatlah fungsi `format_bandwidth(mbps: int | float | str) -> str`:
- Jika parameter bertipe `int` atau `float`: Kembalikan string dengan format `"{val:.1f} Mbps"`.
- Jika parameter bertipe `str` (misal `"1 Gbps"` atau `"500 kbps"`): Lakukan normalisasi string dan kembalikan dengan huruf kapital.
- Jika tipe lain dilewatkan: Lemparkan `TypeError`.
- Gunakan `isinstance()` untuk melakukan *type narrowing* yang dikenali oleh static type checker (seperti mypy).

---

## Latihan 2: Skema TypedDict dengan NotRequired
Definisikan skema dictionary terstruktur `GatewayProfile`:
- `gateway_id`: `str`
- `ip_address`: `str`
- `port`: `int`
- `is_encrypted`: `bool`
- `backup_ip`: `NotRequired[str]` (atribut opsional dari modul `typing`)

Buatlah fungsi `inspect_gateway(profile: GatewayProfile) -> str` yang mengembalikan ringkasan status gateway tersebut secara type-safe.

---

## Latihan 3: Structural Subtyping dengan Protocol
Gunakan `typing.Protocol` dan decorator `@runtime_checkable` untuk mendefinisikan interface `Loggable`:
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Loggable(Protocol):
    def to_log_entry(self) -> str:
        ...
```
Buatlah dua class berbeda tanpa hubungan pewarisan:
1. `DeviceAlarm`: Memiliki method `to_log_entry()`.
2. `UserAction`: Memiliki method `to_log_entry()`.

Buktikan bahwa kedua objek dari class tersebut lolos pemeriksaan `isinstance(obj, Loggable)` dan dapat diterima oleh fungsi `write_audit_log(item: Loggable)`.

---

## Latihan 4: Generic Stack / Buffer Container
Rancang class generik `BoundedBuffer[T]` menggunakan `Generic[T]` dan `TypeVar`:
- Batasi kapasitas maksimal buffer (misalnya `max_size: int = 5`).
- Sediakan method `push(item: T) -> None` yang menolak penambahan jika buffer penuh (`BufferError`).
- Sediakan method `pop() -> T` yang mengambil elemen terakhir (LIFO).
- Buktikan bahwa buffer dapat diinstansiasi secara khusus untuk `BoundedBuffer[int]` maupun `BoundedBuffer[str]` dengan tipe kembalian yang konsisten.

