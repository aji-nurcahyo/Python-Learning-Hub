# Modul C01: HTTP Client Utility & JSON Contract Consumption

## 1. Mengonsumsi API Eksternal Secara Tangguh dengan `httpx`
Aplikasi backend modern tidak hanya menyediakan API, tetapi juga sering berkomunikasi dengan layanan lain melalui HTTP. Menggunakan **`httpx.Client`** memberi empat keunggulan dibanding skrip ad-hoc:
- **Connection Pooling:** menggunakan context manager `with httpx.Client(...) as client:` menjaga koneksi TCP tetap hemat.
- **Timeout Wajib:** selalu pasang `timeout=5.0` agar permintaan macet tidak menggantung proses utama selamanya.
- **URL Params Aman:** serahkan pembentukan query string ke argumen `params={"page": 2, "q": "bandar lampung"}` agar karakter khusus otomatis di-encode benar.
- **Pengujian Deterministik Offline:** **`httpx.MockTransport`** memungkinkan kita mensimulasikan berbagai respons server (200, 404, 503, pagination) di memori tanpa menyentuh jaringan internet publik.

---

## 2. Retry Selektif vs Kesalahan Klien (`4xx` vs `5xx`)
Tidak semua kegagalan HTTP boleh diulang otomatis:
- **Status `4xx` (Client Error):** `400 Bad Request`, `401 Unauthorized`, `404 Not Found` menandakan permintaan atau otorisasi memang keliru. Mencoba ulang tidak akan memperbaikinya.
- **Status `5xx` (Server/Gateway Transient Error):** `502`, `503`, `504`, atau `httpx.TimeoutException` menandakan server sibuk sesaat dan layak dicoba ulang beberapa kali dengan jeda singkat.

---

## 3. Validasi Kontrak JSON dengan Pydantic v2
Mengakses `response.json()["data"][0]["nilai"]` secara mentah berisiko memicu `KeyError` atau `TypeError` jika format API eksternal berubah. Dengan **Pydantic `BaseModel`**, payload tervalidasi seketika saat diterima:

```python
from pydantic import BaseModel, Field

class SensorPayload(BaseModel):
    device_id: str
    temp_c: float = Field(ge=-40.0, le=120.0)
```

