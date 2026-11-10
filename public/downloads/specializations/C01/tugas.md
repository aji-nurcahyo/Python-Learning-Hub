# Tugas Terstruktur C01: Reusable Telemetry HTTP Client

## Instruksi Implementasi (`tugas.py`)
1. Definisikan kelas Pydantic `TelemetryRecord` (`device_id: str`, `temp_c: float` dalam `[-40.0, 120.0]`, `battery_pct: int` dalam `[0, 100]`).
2. `safe_get_json(client: httpx.Client, path: str, max_attempts: int = 3) -> dict`: ulangi hanya jika status berada pada `{502, 503, 504}`; panggil `resp.raise_for_status()` untuk kesalahan 4xx atau percobaan akhir.
3. `fetch_all_pages(client: httpx.Client, endpoint: str) -> list[TelemetryRecord]`: tarik semua halaman sampai array `items` kosong dan validasi setiap elemen dengan `TelemetryRecord`.

## Rubrik Penilaian (Total 100 Poin)
- Konfigurasi httpx.Client & Timeout Eksplisit (25%)
- Logika Pagination & Retry Selektif (30%)
- Validasi Skema JSON via Pydantic (25%)
- Unit Testing Offline dengan MockTransport (20%)
