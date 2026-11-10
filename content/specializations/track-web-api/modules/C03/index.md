# Modul C03: Database Persistence with SQLite & SQLAlchemy 2.0 ORM

## 1. Dari Penyimpanan Memori ke Database Relasional
Variabel dictionary di RAM akan hilang begitu proses server restart. Dengan **SQLAlchemy 2.0 ORM**, kelas Python dipetakan langsung ke tabel SQL (*Object-Relational Mapping*) secara type-safe sehingga kita bisa berpindah antara SQLite lokal dan PostgreSQL produksi dengan usaha minimal.

---

## 2. Declarative Models Modern SQLAlchemy 2.0
SQLAlchemy 2.0 memperkenalkan gaya deklarasi berbasis tipe `Mapped[...]` dan `mapped_column(...)`:

```python
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class NodeRecord(Base):
    __tablename__ = "nodes"
    id: Mapped[int] = mapped_column(primary_key=True)
    hostname: Mapped[str] = mapped_column(String(50), unique=True)
```

---

## 3. Session CRUD dengan `select()` dan `scalars()`
Gunakan `with Session(engine) as session:` dan kueri eksplisit `select(...)`:
- **Insert:** `session.add(obj)` lalu `session.commit()` serta `session.refresh(obj)` untuk memperoleh ID auto-increment.
- **Query:** `session.scalars(select(NodeRecord).where(NodeRecord.hostname == "BTS-01")).first()`.
- **Update & Delete:** ubah atribut objek lalu `session.commit()`, atau panggil `session.delete(obj)` diikuti `session.commit()`.

---

## 4. Dependency Injection `Depends(get_db)` di FastAPI
Gunakan generator dependency dengan blok `try / yield / finally` agar setiap request HTTP memperoleh sesi database bersih dan menutupnya otomatis selesai request:
- Tambahkan `model_config = ConfigDict(from_attributes=True)` pada Pydantic Output Schema agar FastAPI dapat mengonversi objek ORM SQLAlchemy menjadi JSON secara langsung.
- Untuk SQLite di `TestClient`, sertakan `connect_args={"check_same_thread": False}` dan panggil `engine.dispose()` setelah uji selesai.

