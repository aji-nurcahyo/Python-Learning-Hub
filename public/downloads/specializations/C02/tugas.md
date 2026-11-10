# Tugas Terstruktur C02: REST API Inventaris Perangkat Jaringan

## Instruksi Implementasi (`tugas.py`)
1. Definisikan `DeviceCreate(BaseModel)` (`serial_number`, `model_name`, `power_watt > 0`, `status: str = "active"`) serta `DeviceOut(DeviceCreate)` dengan tambahan `id: int`.
2. Implementasikan factory function `create_devices_app() -> FastAPI` yang menyediakan:
   - `POST /devices` -> `201 Created`
   - `GET /devices` -> `200 OK` (dukung filter opsional `?status=active`)
   - `GET /devices/{device_id}` -> `200 OK` atau `404 Not Found`
   - `PUT /devices/{device_id}` -> `200 OK` atau `404`
   - `DELETE /devices/{device_id}` -> `204 No Content` atau `404`
3. Verifikasi dengan unit test memakai `TestClient`.

## Rubrik Penilaian (Total 100 Poin)
- Desain Route & HTTP Status Codes (30%)
- Validasi Skema Pydantic v2 (30%)
- Response Model & OpenAPI Docs (20%)
- Test Suite TestClient (Pytest) (20%)
