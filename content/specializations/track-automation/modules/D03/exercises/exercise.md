# Latihan Mandiri D03 — Ethical Web Data Collection

## Latihan 1: Selector CSS & Normalisasi Harga
1. Muat `datasets/catalog_snapshot.html` lalu parse memakai `BeautifulSoup(html, "html.parser")`.
2. Ekstrak seluruh `<tr class="device-row">` termasuk elemen opsional `<span class="badge-note">` dengan pengecekan `is not None`.
3. Bersihkan string harga seperti `"Rp 4.250.000"` menjadi integer `4250000`.
4. Periksa izin jalur dengan `RobotFileParser` sebelum mengambil endpoint HTML dari `MockTransport`.

