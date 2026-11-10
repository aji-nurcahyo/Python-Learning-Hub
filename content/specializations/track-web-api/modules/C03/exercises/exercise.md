# Latihan Mandiri C03 — SQLite & SQLAlchemy ORM

## Latihan 1: Skema Relasional & FastAPI Session
1. Definisikan kelas `Location` dan `Asset` menggunakan `DeclarativeBase` SQLAlchemy 2.0 dan `ForeignKey("locations.id")`.
2. Buat generator dependency `get_db()` dengan `try / yield / finally: db.close()`.
3. Tambahkan `model_config = ConfigDict(from_attributes=True)` di model Pydantic output.
4. Uji pembuatan dan pengambilan record menggunakan `tmp_path` di `pytest`, lalu panggil `engine.dispose()`.

