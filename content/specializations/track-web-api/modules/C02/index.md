# Modul C02: Modern REST API with FastAPI & Pydantic

## 1. Mengapa FastAPI Menjadi Standar Modern Python?
**FastAPI** menggabungkan kinerja tinggi ASGI dengan **type hints** Python standar dan **Pydantic**:
- **Validasi Otomatis:** Parameter path, query string, maupun request body JSON divalidasi dan dikonversi otomatis berdasarkan anotasi tipe.
- **Dokumentasi OpenAPI Gratis:** Setiap endpoint, skema model, dan status code otomatis membentuk spesifikasi OpenAPI (`/openapi.json`) serta UI interaktif (`/docs`).
- **Mudah Diuji:** **`TestClient(app)`** menjalankan rute FastAPI langsung di memori dalam satuan milidetik.

---

## 2. Path Parameters vs Query Parameters
- **Path Parameters (`/items/{item_id}`):** Mengidentifikasi resource tunggal secara spesifik (`item_id: int`).
- **Query Parameters (`/items?category=router&limit=10`):** Menyaring, mengurutkan, atau membatasi daftar resource. Berikan nilai default (misal `category: str | None = None`) agar bersifat opsional.

---

## 3. Konvensi Status Code & CRUD RESTful
- `POST /items` -> **`201 Created`** (berhasil membuat resource baru).
- `GET /items/{id}` -> **`200 OK`** atau **`404 Not Found`** via `HTTPException(status_code=404)`.
- `PUT /items/{id}` -> **`200 OK`** (memperbarui resource).
- `DELETE /items/{id}` -> **`204 No Content`** (berhasil menghapus tanpa body balikan).
- Input tidak valid -> **`422 Unprocessable Entity`** otomatis dari Pydantic + FastAPI.

