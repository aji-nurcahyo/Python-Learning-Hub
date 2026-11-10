# Latihan Mandiri C02 — FastAPI & Pydantic

## Latihan 1: Endpoint Katalog & Validasi
1. Buat model `DeviceCreate(BaseModel)` dengan `serial_number: str = Field(min_length=4)` dan `power_watt: float = Field(gt=0)`.
2. Implementasikan endpoint `POST /devices` (`status_code=201`) dan `GET /devices/{device_id}`.
3. Gunakan `fastapi.testclient.TestClient` untuk menguji kasus sukses `201`, input invalid `422`, dan ID tidak ditemukan `404`.

