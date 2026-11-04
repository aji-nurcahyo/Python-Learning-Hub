# Latihan Praktik Chapter 27: Concurrent & Asynchronous Programming

Latihan mandiri berikut dirancang untuk mengasah pemahaman Anda terkait pemilihan model konkurensi (Threading vs Multiprocessing vs Asyncio) serta manajemen sinkronisasi data (*shared state*).

---

## Latihan 1: Eksekusi I/O Konkuren dengan `ThreadPoolExecutor`

### Deskripsi Masalah
Anda memiliki daftar 5 alamat IP antena telekomunikasi yang perlu di-ping untuk memeriksa ketersediaan status. Jika dilakukan secara sekuensial dengan jeda 0.5 detik per IP, total waktu mencapai 2.5 detik. Implementasikan eksekusi konkuren dengan `ThreadPoolExecutor` (3 worker) agar seluruh simpul dapat diperiksa dalam waktu kurang dari 1 detik.

### Kode Solusi Acuan
```python
import time
from concurrent.futures import ThreadPoolExecutor

IPS = ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13", "192.168.1.14"]

def ping_ip(ip: str) -> dict[str, str]:
    time.sleep(0.05)  # Simulasi network latency
    return {"ip": ip, "status": "REACHABLE"}

def main() -> None:
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(ping_ip, IPS))
    elapsed = time.perf_counter() - start
    print(f"Selesai memeriksa {len(results)} IP dalam {elapsed:.2f} detik.")

if __name__ == "__main__":
    main()
```

---

## Latihan 2: Mencegah Race Condition dengan `threading.Lock`

### Deskripsi Masalah
Sepuluh thread mengakses variabel saldo kuota jaringan yang sama secara bersamaan. Setiap thread melakukan pengurangan kuota sebesar 5 MB sebanyak 20 kali. Terapkan context manager `threading.Lock` agar nilai akhir kuota berkurang tepat 1.000 MB tanpa ada *lost update*.

### Kode Solusi Acuan
```python
import threading

class NetworkQuota:
    def __init__(self, initial_mb: int = 2000) -> None:
        self.quota = initial_mb
        self.lock = threading.Lock()

    def consume(self, amount: int) -> None:
        with self.lock:
            self.quota -= amount

quota_manager = NetworkQuota()
threads = [threading.Thread(target=lambda: [quota_manager.consume(5) for _ in range(20)]) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Sisa Kuota: {quota_manager.quota} MB (Ekspektasi: 1000 MB)")
```

---

## Latihan 3: Pengumpulan Data Multi-Endpoint dengan `asyncio.gather()`

### Deskripsi Masalah
Buat coroutine `async def fetch_telemetry(sensor_id: str)` yang menunggu secara asinkron selama 0.05 detik menggunakan `asyncio.sleep()`. Panggil 4 sensor secara non-blocking menggunakan `asyncio.gather()` dan cetak semua hasilnya.

### Kode Solusi Acuan
```python
import asyncio

async def fetch_telemetry(sensor_id: str) -> dict[str, str]:
    await asyncio.sleep(0.05)
    return {"sensor": sensor_id, "reading": "24.5 C"}

async def main() -> None:
    sensors = ["TEMP-01", "TEMP-02", "TEMP-03", "TEMP-04"]
    tasks = [fetch_telemetry(s) for s in sensors]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(f"Sensor {r['sensor']}: {r['reading']}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Latihan 4: Penanganan Timeout dengan `asyncio.wait_for()`

### Deskripsi Masalah
Sebuah panggilan telemetri satelit kadang mengalami *network hanging*. Terapkan `asyncio.wait_for()` dengan timeout 0.1 detik untuk menangkap `asyncio.TimeoutError` secara elegan ketika server satelit membutuhkan waktu 0.3 detik untuk merespons.

### Kode Solusi Acuan
```python
import asyncio

async def call_satellite() -> str:
    await asyncio.sleep(0.3)
    return "Satelit OK"

async def main() -> None:
    try:
        res = await asyncio.wait_for(call_satellite(), timeout=0.1)
        print(res)
    except asyncio.TimeoutError:
        print("Peringatan: Koneksi satelit mengalami timeout (kegagalan ditangani secara aman).")

if __name__ == "__main__":
    asyncio.run(main())
```

