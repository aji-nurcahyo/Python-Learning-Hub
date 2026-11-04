# Latihan Mandiri: Advanced OOP & Design Patterns (Chapter 23)

Selamat datang di latihan mandiri Chapter 23. Melalui serangkaian latihan ini, Anda akan mempraktikkan perancangan berorientasi objek tingkat lanjut, pembuatan antarmuka abstrak dengan `ABC`, penerapan pola kreasi (*Factory Pattern*), dan pola perilaku (*Strategy Pattern*).

---

## Latihan 1: Validasi Kontrak Abstract Base Class (ABC)
Buatlah abstract class `AbstractAntenna` yang mewajibkan subclass mengimplementasikan:
1. Property `frequency_band` (string, contoh: `"2.4GHz"` atau `"5GHz"`).
2. Method `calculate_gain_dbi(elevation_angle: float) -> float`.

Ujilah dengan membuat subclass konkret `DishAntenna` dan buktikan bahwa jika salah satu method tidak diimplementasikan, Python akan menolak instansiasi dengan `TypeError`.

---

## Latihan 2: Dataclass Immutability & Validation
Gunakan `@dataclass(frozen=True)` untuk membuat struktur data konfigurasi transmisi radio `RadioChannelConfig`:
- `channel_number`: `int`
- `center_freq_mhz`: `float`
- `channel_width_mhz`: `int = 20`

Pastikan bahwa setiap upaya untuk memodifikasi nilai atribut setelah instansiasi (misalnya `cfg.channel_number = 5`) akan memicu `FrozenInstanceError`.

---

## Latihan 3: Factory Pattern dengan Registrasi Dinamis
Kembangkan `AntennaFactory` yang mampu membuat objek antena berdasarkan nama tipe:
- Tipe `"dish"` menghasilkan instansiasi `DishAntenna`.
- Tipe `"omni"` menghasilkan instansiasi `OmniAntenna`.

Sediakan class method `register_antenna(name: str, antenna_cls)` agar pengguna dapat mendaftarkan tipe antena kustom baru tanpa memodifikasi kode inti factory (*Open/Closed Principle*).

---

## Latihan 4: Strategy Pattern untuk Payload Compression
Rancang sistem transmisi yang mendukung pergantian algoritma kompresi data secara dinamis (*Strategy Pattern*):
- Antarmuka `CompressionStrategy` dengan method abstrak `compress(data: str) -> str`.
- Implementasi `NoCompression`: Mengembalikan data apa adanya dengan prefiks `"RAW:"`.
- Implementasi `RleCompression`: Melakukan kompresi Run-Length Encoding sederhana.
- Class `TelemetrySender` yang menerima `CompressionStrategy` dan mengeksekusi pengiriman payload yang telah dikompresi.

