# Latihan Mandiri C05 (Capstone) — Modular REST API

## Latihan 1: Audit Arsitektur & Integration Testing
1. Bandingkan tanggung jawab `c05_01_domain_schemas.py` hingga `c05_04_app_factory_testclient.py`.
2. Pastikan `NodeRepository` hanya berurusan dengan kueri SQLAlchemy, sedangkan `APIRouter` hanya berurusan dengan status HTTP dan otorisasi.
3. Jalankan `pytest code/test_c05_capstone.py` untuk menguji status `200`, `201`, `204`, `401`, `404`, `409`, `422`, serta pemeriksaan OpenAPI schema.

