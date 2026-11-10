# Latihan Mandiri E01 — Serial Telemetry & Binary Framing

## Latihan 1: Parsing Frame Serial & XOR Checksum
1. Baca berkas `datasets/serial_sensor_frames.log`.
2. Implementasikan fungsi `compute_xor_checksum(body)` dan tolak baris yang terpotong atau memiliki checksum salah.
3. Kemaskan `(node_id, temp_c, humidity_pct)` ke payload biner 10-byte memakai `struct.Struct("<Hff")`.
4. Uji pembacaan serial virtual dengan `serial.serial_for_url("loop://")` serta jalankan `pytest code/test_e01_telemetry.py`.

