# Tugas Capstone Track C: Production-Ready Telemetry Nodes Microservice

## Instruksi Implementasi (`tugas.py`)
1. Definisikan model Pydantic `NodeCreate`, `NodeUpdate`, dan `NodeOut(ConfigDict(from_attributes=True))`.
2. Implementasikan `NodeRepository` di atas SQLAlchemy 2.0 `Session` (`create`, `get_by_id`, `get_by_code`, `list_all`, `update`, `delete`).
3. Rakit `APIRouter(prefix="/api/v1/nodes")` yang mensyaratkan Bearer HMAC token pada operasi `POST`, `PUT`, dan `DELETE`.
4. Implementasikan Application Factory `create_microservice_app(db_url: str, api_secret: str)` lengkap dengan middleware timing, `/health`, serta unit test `pytest` penuh.

## Rubrik Penilaian (Total 100 Poin)
- Arsitektur Berlapis & Modular APIRouter (25%)
- SQLAlchemy 2.0 CRUD & Integritas Data (25%)
- Keamanan Token, Validasi 422 & Middleware (25%)
- Integration Test Pytest & OpenAPI Check (25%)

