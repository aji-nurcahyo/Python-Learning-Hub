# Latihan Praktik Chapter 30: Professional Capstone Project

Latihan integratif berikut mempersiapkan Anda untuk membangun arsitektur sistem monitoring dan otomasi telemetri tingkat profesional.

---

## Latihan 1: Ekstraksi dan Validasi CSV Telemetri

### Deskripsi Masalah
Tulis fungsi `parse_csv_telemetry(raw_csv: str) -> list[dict]` yang mengabaikan baris dengan nilai `rssi_dbm` yang cacat (bukan float) dan mencatat jumlah baris yang diabaikan.

### Kode Solusi Acuan
```python
import csv
import io

def parse_csv_telemetry(raw_csv: str) -> list[dict]:
    valid_records = []
    reader = csv.DictReader(io.StringIO(raw_csv.strip()))
    for row in reader:
        try:
            row["rssi_dbm"] = float(row["rssi_dbm"])
            valid_records.append(row)
        except ValueError:
            continue
    return valid_records

raw = "device_id,rssi_dbm\nNODE-1,-70.5\nNODE-2,CORRUPT\nNODE-3,-85.0\n"
print("Data Valid:", parse_csv_telemetry(raw))
```

---

## Latihan 2: Thread-Safe Metric Storage Counter

### Deskripsi Masalah
Buat class `SafeMetricsAccumulator` dengan method `add_packet_loss(amount: float)` dan `get_average() -> float` yang dilindungi oleh `threading.Lock`.

### Kode Solusi Acuan
```python
import threading

class SafeMetricsAccumulator:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._total_loss = 0.0
        self._count = 0

    def add_packet_loss(self, amount: float) -> None:
        with self._lock:
            self._total_loss += amount
            self._count += 1

    def get_average(self) -> float:
        with self._lock:
            return round(self._total_loss / self._count, 2) if self._count > 0 else 0.0

acc = SafeMetricsAccumulator()
acc.add_packet_loss(1.2)
acc.add_packet_loss(2.4)
print("Rata-rata Packet Loss:", acc.get_average())  # 1.8
```

---

## Latihan 3: Penggabungan Multi-Sumber Data (Local + API)

### Deskripsi Masalah
Tulis fungsi `merge_telemetry_sources(local_records: list, remote_records: list) -> list` yang menggabungkan kedua list dan menghapus duplikasi berdasarkan `device_id` (mengutamakan data remote jika terdapat ID yang sama).

### Kode Solusi Acuan
```python
def merge_telemetry_sources(local: list[dict], remote: list[dict]) -> list[dict]:
    merged = {item["device_id"]: item for item in local}
    for item in remote:
        merged[item["device_id"]] = item  # Overwrite jika duplikat
    return list(merged.values())

loc = [{"device_id": "D-01", "val": 10}, {"device_id": "D-02", "val": 20}]
rem = [{"device_id": "D-02", "val": 99}, {"device_id": "D-03", "val": 30}]
print("Hasil Gabungan:", merge_telemetry_sources(loc, rem))
```

---

## Latihan 4: Format Laporan SLA Markdown

### Deskripsi Masalah
Buat fungsi `format_sla_badge(health_rate: float) -> str` yang mengembalikan string badge Markdown: `[STATUS: COMPLIANT]` jika `health_rate >= 90.0`, `[STATUS: DEGRADED]` jika antara 75.0 dan 89.9, dan `[STATUS: BREACH]` jika di bawah 75.0.

### Kode Solusi Acuan
```python
def format_sla_badge(health_rate: float) -> str:
    if health_rate >= 90.0:
        return "[STATUS: COMPLIANT]"
    elif health_rate >= 75.0:
        return "[STATUS: DEGRADED]"
    return "[STATUS: BREACH]"

print(format_sla_badge(95.5))  # [STATUS: COMPLIANT]
print(format_sla_badge(82.0))  # [STATUS: DEGRADED]
print(format_sla_badge(64.0))  # [STATUS: BREACH]
```

