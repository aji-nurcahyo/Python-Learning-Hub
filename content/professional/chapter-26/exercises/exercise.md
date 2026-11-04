# Latihan Mandiri: Advanced Testing & Logging (Chapter 26)

Selamat datang di latihan mandiri Chapter 26. Melalui serangkaian latihan ini, Anda akan mempraktikkan pengujian perangkat lunak tingkat profesional: memanfaatkan test fixtures, pengujian berparameter (*parameterized testing*), isolasi dependensi eksternal dengan *mocking*, verifikasi log terstruktur, dan isolasi berkas sementara.

---

## Latihan 1: Fixtures & State Isolation
Rancang kelas pengujian `TestNodeCache` yang menguji komponen cache in-memory:
- Gunakan `setUp()` untuk menginisialisasi cache baru dan memasukkan 3 data dummy.
- Gunakan `tearDown()` untuk mengosongkan cache (*clear*) guna memastikan isolasi penuh antar test case.
- Ujilah fungsionalitas penambahan, penghapusan, dan kedaluwarsa data cache.

---

## Latihan 2: Parameterized Subtests dengan batas Frekuensi
Buat fungsi `validate_lte_band(band_number: int) -> bool` yang memvalidasi apakah nomor band berada pada rentang band LTE yang diizinkan (misalnya Band 1, 3, 5, 8, 40):
- Tulis satu unit test yang memuat tabel skenario: sekumpulan input integer dan nilai boolean yang diharapkan.
- Gunakan `with self.subTest(band=band):` untuk menguji setiap skenario secara terpisah sehingga jika satu nilai gagal, pengujian nilai lainnya tetap berjalan.

---

## Latihan 3: Mocking API Eksternal dengan `unittest.mock.patch`
Diberikan fungsi bisnis yang memanggil API cuaca eksternal:
```python
def check_tower_wind_safety(tower_id: str, weather_api_client) -> bool:
    data = weather_api_client.get_wind_speed(tower_id)
    return data["speed_kmh"] < 60.0
```
- Buat unit test yang menggunakan `unittest.mock.MagicMock`.
- Konfigurasikan mock agar mengembalikan `{"speed_kmh": 45.0}` pada skenario aman dan `{"speed_kmh": 85.0}` pada skenario angin kencang berbahaya.
- Verifikasi bahwa method `get_wind_speed` dipanggil tepat satu kali dengan ID tower yang benar.

---

## Latihan 4: Verifikasi Log Terstruktur dengan `assertLogs`
Diberikan fungsi transaksional yang mencatat log audit:
```python
import logging
logger = logging.getLogger("audit.security")

def revoke_user_token(user_id: str, reason: str) -> None:
    logger.warning(f"SECURITY: Token untuk user '{user_id}' dicabut. Alasan: {reason}")
```
- Tulis unit test yang menggunakan `with self.assertLogs("audit.security", level="WARNING") as cm:`.
- Panggil `revoke_user_token("admin_01", "Suspicious IP")`.
- Lakukan assertion bahwa pesan log yang tertangkap di `cm.output` memuat teks `"SECURITY"` dan ID pengguna yang bersangkutan.

