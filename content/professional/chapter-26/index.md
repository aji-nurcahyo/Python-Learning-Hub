# Chapter 26: Advanced Testing & Logging
## Test Fixtures, Parameterized Tests, Mocking & Structured Logging

Selamat datang di **Chapter 26: Advanced Testing & Logging** pada tingkat **Level 3: Professional Python Engineering** di **Python Learning Hub**.

Pada modul-modul sebelumnya, Anda telah mempelajari bagaimana merancang arsitektur sistem dengan pola desain (Chapter 23), mengoptimalkan eksekusi dengan metaprogramming dan generator (Chapter 24), serta menjamin integritas tipe dengan type hints dan static analysis (Chapter 25). Bab ini melengkapi pilar keandalan perangkat lunak tingkat profesional dengan dua instrumen esensial: **pengujian otomatis mendalam (*advanced automated testing*)** dan **pencatatan log terstruktur (*structured logging*)**.

Sebagus apa pun kode yang ditulis, tanpa suite pengujian yang komprehensif, setiap perubahan kode atau refactoring berisiko menimbulkan *regresi* (fitur lama yang rusak tanpa terdeteksi). Di sisi lain, ketika aplikasi berjalan di lingkungan produksi, log yang terstruktur adalah satu-satunya jendela observabilitas teknisi untuk mendiagnosis insiden.

---

## 1. Strategi Pengujian & Piramida Uji (Testing Pyramid)

Dalam rekayasa perangkat lunak modern, pengujian dibagi ke dalam tiga tingkatan utama:

1. **Unit Tests (Dasar Piramida):**
   - Menguji unit terkecil (fungsi murni atau class tunggal) dalam isolasi penuh dari ketergantungan luar.
   - Waktu eksekusi sangat cepat (hitungan milidetik per test).
   - Memiliki jumlah terbanyak (70-80% dari total pengujian).
2. **Integration Tests (Tengah Piramida):**
   - Menguji interaksi gabungan antar modul internal (misalnya interaksi antara repositori, service, dan serializer).
   - Menjamin bahwa modul-modul yang lolos uji unit dapat bekerja sama dengan benar.
3. **End-to-End Tests (Puncak Piramida):**
   - Menguji alur sistem lengkap dari sudut pandang pengguna atau klien eksternal.
   - Jumlah lebih sedikit karena biaya pemeliharaan dan waktu eksekusi yang lebih lambat.

---

## 2. Test Fixtures: Siklus Hidup `setUp()` dan `tearDown()`

**Prinsip Isolasi Pengujian (*Test Isolation*):** Setiap test case harus berjalan dalam lingkungan yang bersih (*clean room*). Status yang dimodifikasi oleh satu test case tidak boleh memengaruhi test case lainnya.

Modul bawaan `unittest` menyediakan method fixture:
- **`setUp()`**: Dijalankan secara otomatis **sebelum** setiap method pengujian (`test_*`). Digunakan untuk mengalokasikan objek, inisialisasi koneksi mock, atau membuat data awal.
- **`tearDown()`**: Dijalankan secara otomatis **setelah** setiap method pengujian selesai (baik lulus maupun gagal). Digunakan untuk membersihkan status memori, menutup socket, atau menghapus data sementara.

```python
import unittest

class TestDeviceDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.db = InMemoryDatabase()
        self.db.insert("DEV-01", "Online")

    def tearDown(self) -> None:
        self.db.clear()

    def test_retrieve(self) -> None:
        self.assertEqual(self.db.get("DEV-01"), "Online")
```

---

## 3. Parameterized Testing dengan `self.subTest()`

Sering kali kita perlu menguji satu fungsi dengan puluhan variasi input dan ekspektasi keluaran yang berbeda. Menulis satu method `test_*` terpisah untuk setiap variasi akan menimbulkan pengulangan kode yang membosankan (*code duplication*).

Menggunakan perulangan biasa dengan `assert` memiliki kelemahan: jika iterasi pertama gagal, seluruh loop berhenti dan kita tidak mengetahui apakah iterasi berikutnya lulus atau gagal.

Solusi elegan di Python adalah menggunakan context manager **`self.subTest()`**:

```python
class TestSignalClassification(unittest.TestCase):
    def test_parameterized_quality(self) -> None:
        test_cases = [
            (-70.0, "EXCELLENT"),
            (-85.0, "GOOD"),
            (-100.0, "FAIR"),
            (-115.0, "POOR"),
        ]
        for rsrp, expected in test_cases:
            with self.subTest(rsrp=rsrp, expected=expected):
                actual = classify_signal_quality(rsrp)
                self.assertEqual(actual, expected)
```

Jika salah satu skenario gagal, CPython tetap melanjutkan evaluasi untuk skenario-skenario lainnya dan melaporkan kegagalan secara terinci.

---

## 4. Pengujian Kegagalan dengan `self.assertRaises()`

Aplikasi yang tangguh tidak hanya diuji pada jalur normal (*happy path*), melainkan juga harus diuji pada jalur kegagalan (*error path*): memastikan bahwa input cacat secara konsisten memicu tipe exception yang benar.

Context manager `assertRaises` menangkap exception yang dilempar dan memungkinkan inspeksi pesan error di dalamnya:

```python
def test_invalid_ip_raises(self) -> None:
    with self.assertRaises(ValueError) as ctx:
        parse_ip_address("192.168.1.300")
    self.assertIn("di luar rentang", str(ctx.exception))
```

---

## 5. Mocking Dependensi Eksternal dengan `unittest.mock`

Unit test harus dapat dijalankan secara instan di laptop pengembang maupun mesin CI/CD tanpa koneksi fisik ke server database, gateway telekomunikasi, atau API pembayaran pihak ketiga.

Modul bawaan **`unittest.mock`** menyediakan:
- **`MagicMock`**: Objek serbaguna yang merekam seluruh pemanggilan method dan argumen yang diberikan kepadanya, serta dapat dikonfigurasi untuk mengembalikan nilai palsu (*fake return value*) atau melempar exception (*side effect*).
- **`patch`**: Decorator atau context manager yang menggantikan objek atau fungsi nyata pada target modul dengan mock object selama durasi pengujian.

```python
from unittest.mock import MagicMock

def test_service_with_mock():
    mock_client = MagicMock(spec=ExternalApiClient)
    mock_client.fetch_status.return_value = {"status": "UP"}

    service = MonitoringService(mock_client)
    self.assertTrue(service.is_healthy("GW-01"))
    # Verifikasi bahwa method dipanggil dengan parameter yang tepat
    mock_client.fetch_status.assert_called_once_with("GW-01")
```

---

## 6. Isolasi File Sementara dengan `tempfile.TemporaryDirectory`

Ketika menguji fungsi yang membaca atau menulis file fisik, jangan menulis file langsung di direktori proyek pengembang. Gunakan **`tempfile.TemporaryDirectory`**:

```python
import tempfile
import os

with tempfile.TemporaryDirectory() as temp_dir:
    filepath = os.path.join(temp_dir, "test.cfg")
    # Tulis dan uji operasi berkas di sini
# Setelah keluar dari blok with, temp_dir dan isinya otomatis dihapus bersih
```

---

## 7. Fondasi Logging dan Observabilitas Sistem

Fungsi `print()` hanya cocok untuk skrip sederhana. Di sistem produksi, gunakan modul **`logging`** bawaan Python yang mendukung:
1. **Tingkat Keparahan (*Severity Levels*):** `DEBUG` (10), `INFO` (20), `WARNING` (30), `ERROR` (40), `CRITICAL` (50).
2. **Handlers & Formatters:** Mengarahkan aliran log ke konsol terminal, file berkas terotasi (*RotatingFileHandler*), atau layanan pemantauan cloud (ELK, CloudWatch).
3. **Structured Logging:** Memformat pesan log dengan metadata stempel waktu (*timestamp*), nama logger, tingkat keparahan, dan payload terstruktur (JSON).

### Pengujian Log dengan `self.assertLogs()`
Kita dapat menguji apakah suatu alur bisnis benar-benar mencatat log peringatan saat terjadi anomali:

```python
with self.assertLogs("telecom.service", level="WARNING") as cm:
    service.check_health("OFFLINE_NODE")

self.assertTrue(any("Sinyal lemah" in msg for msg in cm.output))
```

---

## 8. Rangkuman & Langkah Selanjutnya

- **Test Fixtures (`setUp`/`tearDown`)** memastikan kebersihan status dan independensi antar test case.
- **`subTest()`** menyederhanakan pengujian berparameter tanpa pengulangan kode.
- **`unittest.mock` (`MagicMock` dan `patch`)** mengisolasi kode bisnis dari dependensi I/O eksternal yang lambat atau tidak stabil.
- **`logging` dan `assertLogs`** memberikan visibilitas operasional penuh dan jaminan bahwa telemetri sistem berjalan semestinya.

Dengan selesainya Chapter 23–26, Anda telah menguasai fondasi arsitektur, metaprogramming, static typing, dan testing engineering di tingkat profesional!
