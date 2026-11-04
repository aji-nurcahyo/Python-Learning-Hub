# Latihan Praktik Chapter 28: Networking & API Integration

Latihan mandiri berikut dirancang untuk melatih kemampuan Anda dalam mengintegrasikan REST API, menangani autentikasi Bearer, memproses pagination, dan menerapkan strategi retry backoff.

---

## Latihan 1: Penyusunan Query Parameter URL secara Dinamis

### Deskripsi Masalah
Buat fungsi `build_telecom_query(base_url: str, params: dict) -> str` menggunakan modul standar `urllib.parse` untuk mengonversi dictionary filter pencarian (seperti status, band, dan limit) menjadi URL query string yang valid dan ter-encode dengan aman.

### Kode Solusi Acuan
```python
from urllib.parse import urlencode

def build_telecom_query(base_url: str, params: dict[str, str | int]) -> str:
    encoded_params = urlencode(params)
    return f"{base_url}?{encoded_params}"

url = build_telecom_query(
    "https://api.telekom.id/v1/sites",
    {"status": "ONLINE", "band": "1800MHz", "city": "Bandar Lampung"}
)
print("URL Terbentuk:", url)
```

---

## Latihan 2: Pengolahan JSON Response Defensif

### Deskripsi Masalah
Terkadang payload JSON dari API eksternal memiliki struktur kunci yang tidak lengkap (*missing keys*). Buat fungsi `extract_sensor_metrics(payload: dict) -> dict` yang menggunakan method `.get()` dengan nilai bawaan (*default values*) agar tidak memicu `KeyError`.

### Kode Solusi Acuan
```python
def extract_sensor_metrics(payload: dict) -> dict:
    device = payload.get("device", {})
    return {
        "device_id": device.get("id", "UNKNOWN"),
        "voltage": payload.get("telemetry", {}).get("voltage", 0.0),
        "status": payload.get("status", "OFFLINE"),
    }

sample_json = {"device": {"id": "BTS-001"}, "status": "ONLINE"}
result = extract_sensor_metrics(sample_json)
print("Hasil Ekstraksi Defensif:", result)
```

---

## Latihan 3: Traversal Paginasi REST API Berbasis Halaman

### Deskripsi Masalah
Sebuah endpoint mengembalikan respon JSON berformat `{ "page": 1, "has_next": true, "items": [...] }`. Tulis perulangan `while` yang secara terus menerus memanggil fungsi pengambil halaman hingga `has_next` bernilai `False` dan gabungkan semua `items` ke dalam satu list tunggal.

### Kode Solusi Acuan
```python
def mock_fetch_page(page: int) -> dict:
    data = {
        1: {"items": ["Node-1", "Node-2"], "has_next": True},
        2: {"items": ["Node-3", "Node-4"], "has_next": False},
    }
    return data.get(page, {"items": [], "has_next": False})

all_nodes = []
current_page = 1
while True:
    res = mock_fetch_page(current_page)
    all_nodes.extend(res["items"])
    if not res.get("has_next"):
        break
    current_page += 1

print(f"Total data terkumpul ({len(all_nodes)}):", all_nodes)
```

---

## Latihan 4: Mekanisme Sanitasi Kredensial untuk Logging

### Deskripsi Masalah
Sebelum sebuah header dictionary dicatat ke dalam log file, buat fungsi `sanitize_auth_headers(headers: dict) -> dict` yang menduplikasi dictionary dan mengganti isi nilai header `Authorization` dengan format sensor `Bearer ****[4 karakter terakhir]` agar tidak membocorkan token rahasia ke berkas log.

### Kode Solusi Acuan
```python
def sanitize_auth_headers(headers: dict[str, str]) -> dict[str, str]:
    clean = headers.copy()
    if "Authorization" in clean:
        token = clean["Authorization"]
        if len(token) > 10:
            clean["Authorization"] = f"{token[:7]}****{token[-4:]}"
    return clean

raw = {"Authorization": "Bearer my_super_secret_production_token_1234", "Content-Type": "application/json"}
print("Header Tersanitasi:", sanitize_auth_headers(raw))
```
