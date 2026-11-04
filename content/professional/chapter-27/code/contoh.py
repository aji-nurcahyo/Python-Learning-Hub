"""Chapter 27: Concurrent & Asynchronous Programming
Contoh Kode Terpadu: ThreadPoolExecutor, ProcessPoolExecutor, Asyncio & Lock
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import threading
import time


# 1. Thread-safe Shared Counter dengan Lock
class SafeCounter:
    def __init__(self) -> None:
        self.count = 0
        self.lock = threading.Lock()

    def increment(self) -> None:
        with self.lock:
            self.count += 1


# 2. Operasi I/O-bound (Cocok untuk Threading)
def worker_io(task_id: int) -> str:
    time.sleep(0.02)
    return f"I/O Task #{task_id} selesai"


# 3. Operasi CPU-bound (Cocok untuk Multiprocessing)
def worker_cpu(num: int) -> int:
    return sum(i * i for i in range(num))


# 4. Operasi Asinkron (Cocok untuk I/O skala tinggi)
async def async_fetch_node(node_name: str) -> dict[str, str]:
    await asyncio.sleep(0.02)
    return {"node": node_name, "status": "ONLINE"}


async def run_async_demo() -> list[dict[str, str]]:
    nodes = ["BTS-JKT", "BTS-BDG", "BTS-SMG"]
    tasks = [async_fetch_node(node) for node in nodes]
    results = await asyncio.gather(*tasks)
    return list(results)


def main() -> None:
    print("=== DEMO CHAPTER 27: CONCURRENT & ASYNCHRONOUS PROGRAMMING ===\n")

    # 1. ThreadPoolExecutor untuk I/O
    print("[1] Menjalankan I/O Task dengan ThreadPoolExecutor:")
    start_t = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        io_results = list(executor.map(worker_io, [1, 2, 3, 4]))
    t_elapsed = time.perf_counter() - start_t
    for res in io_results:
        print(f" -> {res}")
    print(f"Waktu eksekusi thread pool: {t_elapsed:.3f} detik\n")

    # 2. Thread-safe Synchronization
    print("[2] Sinkronisasi Shared State dengan threading.Lock:")
    counter = SafeCounter()
    threads = [threading.Thread(target=counter.increment) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Nilai akhir SafeCounter setelah 10 thread: {counter.count}\n")

    # 3. Asyncio Event Loop
    print("[3] Eksekusi Asinkron non-blocking dengan asyncio.gather():")
    async_results = asyncio.run(run_async_demo())
    for item in sorted(async_results, key=lambda x: x["node"]):
        print(f" -> Node: {item['node']} | Status: {item['status']}")
    print("\nDemonstrasi pola konkurensi selesai dieksekusi.")


if __name__ == "__main__":
    main()

