# Tugas Terstruktur D03: Polite Catalog & Maintenance Notice Extractor

## Instruksi Implementasi (`tugas.py`)
1. `is_path_allowed(robots_txt: str, user_agent: str, path: str) -> bool`: periksa aturan `robots.txt` menggunakan `urllib.robotparser.RobotFileParser`.
2. `parse_idr_price(raw_text: str) -> int`: bersihkan simbol mata uang dan pemisah ribuan sehingga mengembalikan integer bersih.
3. `extract_catalog_rows(html: str) -> list[dict]`: ekstrak baris katalog dari HTML dengan fallback aman bila badge/field opsional absen.
4. Uji ekstraksi dan kepatuhan `robots.txt` menggunakan fixture snapshot HTML dan `httpx.MockTransport` di `pytest`.

## Rubrik Penilaian (Total 100 Poin)
- Kepatuhan Etika robots.txt & Headers (25%)
- Selector BeautifulSoup Tahan Elemen Hilang (30%)
- Normalisasi Teks & Parsing Harga Bersih (25%)
- Unit Testing Offline & Dokumentasi (20%)
