# Modul C05 (Capstone): Production-Ready Modular REST API

## 1. Arsitektur Microservice 4 Lapis
Untuk menghindari file `main.py` raksasa yang mencampur database, validasi, keamanan, dan rute HTTP, proyek Capstone Track C memakai arsitektur berlapis yang bersih:
1. **Domain Schemas (`c05_01_domain_schemas.py`):** Kontrak JSON Pydantic (`NodeCreate`, `NodeUpdate`, `NodeOut`) dan dataclass konfigurasi.
2. **Repository & DB (`c05_02_repository_db.py`):** Model ORM SQLAlchemy 2.0 beserta kelas `NodeRepository` yang mengemas operasi `create`, `get`, `list`, `update`, dan `delete`.
3. **Auth & Modular Router (`c05_03_service_auth_router.py`):** Token guard HMAC-SHA256 via `Depends()`, `APIRouter(prefix="/api/v1/nodes")`, dan pemetaan HTTP `201/200/204/401/404/409`.
4. **Application Factory (`c05_04_app_factory_testclient.py`):** Fungsi `create_app(db_url, api_secret)` yang merakit middleware logging timing, router publik `/health`, dan router `/api/v1/nodes`.

---

## 2. Mengapa Application Factory Mengungguli App Global?
Dengan mendefinisikan `create_app(db_url, api_secret)`:
- Setiap environment (`dev`, `staging`, `prod`) dan setiap suite pengujian `pytest` mendapat instance aplikasi serta engine database terisolasi (`tmp_path`).
- Tidak ada kebocoran state antar pengujian dan penghancuran koneksi `engine.dispose()` terkendali sepenuhnya.

