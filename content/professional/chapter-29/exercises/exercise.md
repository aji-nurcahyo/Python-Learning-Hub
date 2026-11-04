# Latihan Praktik Chapter 29: Software Architecture & Deployment

Latihan mandiri berikut dirancang untuk melatih kemampuan Anda dalam menerapkan pemisahan layer (Separation of Concerns), Dependency Injection, manajemen konfigurasi Twelve-Factor, dan integrasi entry point CLI.

---

## Latihan 1: Pemisahan Domain Model dari Infrastruktur I/O

### Deskripsi Masalah
Buat dataclass `BandwidthLimit` dengan atribut `link_id: str`, `max_mbps: float`, dan method `is_exceeded(used_mbps: float) -> bool`. Pastikan class ini adalah domain murni tanpa fungsi `print()` maupun ketergantungan pada library eksternal.

### Kode Solusi Acuan
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class BandwidthLimit:
    link_id: str
    max_mbps: float

    def is_exceeded(self, used_mbps: float) -> bool:
        return used_mbps > self.max_mbps

limit = BandwidthLimit(link_id="LINK-JKT-BDG", max_mbps=1000.0)
print("Link Terlampaui?", limit.is_exceeded(1250.0))  # True
print("Link Terlampaui?", limit.is_exceeded(800.0))   # False
```

---

## Latihan 2: Penerapan Dependency Injection (DI)

### Deskripsi Masalah
Buat Protocol `AuditLogger` dengan method `log_action(action: str) -> None`. Buat class `DeploymentManager` yang menerima `AuditLogger` pada constructor `__init__`. Buat mock logger untuk memverifikasi tindakan rilis tanpa mencatat ke disk fisik.

### Kode Solusi Acuan
```python
from typing import Protocol

class AuditLogger(Protocol):
    def log_action(self, action: str) -> None:
        ...

class ConsoleAuditLogger:
    def log_action(self, action: str) -> None:
        print(f"[AUDIT LOG] {action}")

class DeploymentManager:
    def __init__(self, logger: AuditLogger) -> None:
        self.logger = logger

    def release_version(self, version: str) -> None:
        # Melakukan proses deployment...
        self.logger.log_action(f"Rilis versi {version} berhasil diterapkan.")

manager = DeploymentManager(logger=ConsoleAuditLogger())
manager.release_version("1.4.0")
```

---

## Latihan 3: Konfigurasi Berbasis Variabel Lingkungan (Twelve-Factor)

### Deskripsi Masalah
Tulis fungsi `load_server_settings()` yang membaca environment variable `SERVER_TIMEOUT` dan `DEBUG_MODE`. Jika tidak diset, gunakan default `30` detik dan `False`. Pastikan fungsi mengembalikan dictionary dengan tipe data yang tepat (`int` dan `bool`).

### Kode Solusi Acuan
```python
import os

def load_server_settings() -> dict[str, int | bool]:
    timeout_raw = os.environ.get("SERVER_TIMEOUT", "30")
    try:
        timeout = int(timeout_raw)
    except ValueError:
        timeout = 30

    debug = os.environ.get("DEBUG_MODE", "false").lower() in ("true", "1", "yes")
    return {"timeout": timeout, "debug": debug}

print("Pengaturan Server:", load_server_settings())
```

---

## Latihan 4: Pembuatan CLI Subcommand dengan `argparse`

### Deskripsi Masalah
Gunakan modul standar `argparse` untuk membangun CLI yang memiliki subcommand `ping` yang menerima argumen posisional `host` dan flag opsional `--count` (default 4).

### Kode Solusi Acuan
```python
import argparse

def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="net-tool")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    ping_cmd = subparsers.add_parser("ping", help="Ping host jaringan")
    ping_cmd.add_argument("host", help="Alamat IP atau domain target")
    ping_cmd.add_argument("--count", type=int, default=4, help="Jumlah paket")
    return parser

parser = build_cli()
args = parser.parse_args(["ping", "10.0.0.1", "--count", "8"])
print(f"Perintah: {args.cmd} | Target: {args.host} | Jumlah: {args.count}")
```

