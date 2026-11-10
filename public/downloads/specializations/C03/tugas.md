# Tugas Terstruktur C03: REST API Inventaris Persisten Berbasis SQLAlchemy

## Instruksi Implementasi (`tugas.py`)
1. Definisikan model ORM `LocationModel` (`id`, `name` unik) dan `AssetModel` (`id`, `hostname` unik, `status`, `location_id` ForeignKey ke `locations.id`).
2. Buat factory `build_db_app(db_url: str)` yang mengembalikan `(app, engine)` dengan SQLite `check_same_thread=False`.
3. Sediakan endpoint:
   - `POST /locations` (`201 Created`)
   - `POST /assets` (`201 Created`, tolak hostname duplikat dengan `409 Conflict`, tolak location_id hilang dengan `404`)
   - `GET /assets` (dukung filter opsional `?location_id=`)
4. Uji menyeluruh di `pytest` menggunakan `tmp_path` dan panggil `engine.dispose()`.

## Rubrik Penilaian (Total 100 Poin)
- Skema Declarative SQLAlchemy 2.0 & ForeignKey (30%)
- Manajemen Session & Lifecycle Cleanup (25%)
- Integrasi FastAPI CRUD & Pydantic ConfigDict (25%)
- Unit Testing Terisolasi dengan tmp_path (20%)
