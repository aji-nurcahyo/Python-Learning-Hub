# Tugas Terstruktur E01: Resilient Serial Telemetry Frame Decoder

## Instruksi Implementasi (`tugas.py`)
1. `compute_xor_checksum(payload: str) -> str`: hitung XOR semua karakter payload lalu kembalikan string hex kapital 2 digit.
2. `parse_telem_frame(raw_line: str) -> dict | None`: verifikasi prefiks `$`, pemisah `*`, checksum 2-digit, dan panjang field `TELEM,id,temp,hum,volt`. Kembalikan `None` jika tidak sah.
3. `encode_binary_packet(node_id: int, temp_c: float, humidity: float) -> bytes` dan `decode_binary_packet(raw_bytes: bytes)` memakai `struct.Struct("<Hff")`.
4. Uji modul Anda lewat unit test di `pytest`.

## Rubrik Penilaian (Total 100 Poin)
- Kebenaran Framing & XOR Checksum (30%)
- Efisiensi Binary Packing (`struct`) (25%)
- Kalibrasi & Smoothing Sinyal Sensor (25%)
- Unit Testing Stream Offline (Pytest) (20%)

