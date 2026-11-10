# Latihan Mandiri C04 — Security, Logging & Testing

## Latihan 1: Hashing Password & Token Guard
1. Buat fungsi `hash_password` dan `verify_password` memakai `hashlib.pbkdf2_hmac("sha256", ..., 100_000)` + `hmac.compare_digest`.
2. Terapkan dependency Bearer auth guard yang membalas `HTTP 401` apabila token hilang, salah, atau kedaluwarsa.
3. Tambahkan middleware HTTP pencatat method, path, status code, dan header `X-Process-Time-Ms`.
4. Jalankan uji keamanan otomatis lewat `pytest`.

