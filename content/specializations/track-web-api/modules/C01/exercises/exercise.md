# Latihan Mandiri C01 — HTTP Client Utility

## Latihan 1: Klien httpx dengan MockTransport
1. Buat fungsi handler mock yang mengembalikan status `503` satu kali sebelum `200 OK`.
2. Konfigurasikan `httpx.Client(timeout=5.0, transport=httpx.MockTransport(...))`.
3. Implementasikan loop retry maksimal 3 percobaan untuk status `502`, `503`, dan `504`.
4. Validasi JSON balikan memakai model Pydantic `BaseModel`.

