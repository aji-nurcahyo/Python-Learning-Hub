# Tugas Terstruktur C04: Keamanan Token, Konfigurasi & Logging API

## Instruksi Implementasi (`tugas.py`)
1. Implementasikan dataclass `AppSettings.from_mapping(env)` yang mewajibkan `API_SECRET` minimal 16 karakter tanpa nilai rahasia produksi hardcoded.
2. Implementasikan `hash_secret_value(raw)` & `verify_secret_value(raw, stored)` dengan `pbkdf2_hmac` dan `hmac.compare_digest`.
3. Implementasikan `issue_token(subject, secret, ttl_seconds)` dan `decode_verified_token(token, secret, now_epoch)`.
4. Bangun factory `build_protected_app(settings)` dengan middleware logging serta rute `/admin/status` terproteksi token (401 vs 200).

## Rubrik Penilaian (Total 100 Poin)
- Manajemen Konfigurasi Env Bebas Hardcoded Secret (20%)
- Hashing Kriptografis & Token HMAC-SHA256 (30%)
- FastAPI Security Guard & Logging Middleware (30%)
- Cakupan Security Unit Tests (Pytest) (20%)
