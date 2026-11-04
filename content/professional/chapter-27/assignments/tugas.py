"""Tugas Mini Project Chapter 27: Concurrent Task Processing System
Platform: Python Learning Hub
Institusi: Institut Teknologi Sumatera (ITERA)

Petunjuk:
Lengkapi implementasi SafeMetricsTracker dan ConcurrentTaskProcessor di bawah ini.
Pastikan kode memenuhi prinsip thread-safety dengan threading.Lock dan async non-blocking.
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
from typing import Any, Optional


class SafeMetricsTracker:
    """Komponen pelacak metrik eksekusi yang thread-safe menggunakan threading.Lock."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._success_count: int = 0
        self._failure_count: int = 0
        self._timeout_count: int = 0

    def record_success(self) -> None:
        with self._lock:
            self._success_count += 1

    def record_failure(self) -> None:
        with self._lock:
            self._failure_count += 1

    def record_timeout(self) -> None:
        with self._lock:
            self._timeout_count += 1

    @property
    def metrics(self) -> dict[str, int]:
        with self._lock:
            return {
                "success": self._success_count,
                "failure": self._failure_count,
                "timeout": self._timeout_count,
                "total": self._success_count + self._failure_count + self._timeout_count,
            }


class ConcurrentTaskProcessor:
    """Prosesor terpadu untuk mengeksekusi beban kerja I/O-bound dan coroutine asinkron."""

    def __init__(self, metrics_tracker: Optional[SafeMetricsTracker] = None) -> None:
        self.tracker = metrics_tracker or SafeMetricsTracker()

    def process_io_batch(
        self,
        task_names: list[str],
        simulated_delay: float = 0.02,
        max_workers: int = 3,
    ) -> list[dict[str, Any]]:
        """Mengeksekusi sekumpulan tugas I/O secara paralel menggunakan ThreadPoolExecutor."""
        def io_worker(name: str) -> dict[str, Any]:
            time.sleep(simulated_delay)
            return {"task": name, "status": "COMPLETED"}

        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_task = {executor.submit(io_worker, name): name for name in task_names}
            for future in as_completed(future_to_task):
                try:
                    res = future.result()
                    self.tracker.record_success()
                    results.append(res)
                except Exception as exc:
                    self.tracker.record_failure()
                    results.append({"task": future_to_task[future], "error": str(exc)})

        results.sort(key=lambda x: str(x.get("task", "")))
        return results

    async def process_async_batch(
        self,
        endpoints: list[str],
        timeout_sec: float = 0.1,
    ) -> list[dict[str, Any]]:
        """Mengeksekusi pengambilan data non-blocking dengan batas timeout."""
        async def fetch_endpoint(ep: str) -> dict[str, Any]:
            # Simulasi delay: jika endpoint berisi 'slow', berikan waktu melebihi timeout
            if "slow" in ep:
                await asyncio.sleep(timeout_sec * 3)
            else:
                await asyncio.sleep(0.01)
            return {"endpoint": ep, "status": "OK"}

        results = []
        for ep in endpoints:
            try:
                res = await asyncio.wait_for(fetch_endpoint(ep), timeout=timeout_sec)
                self.tracker.record_success()
                results.append(res)
            except asyncio.TimeoutError:
                self.tracker.record_timeout()
                results.append({"endpoint": ep, "status": "TIMEOUT"})

        return results


def main() -> None:
    print("=== PENGUJIAN MANDIRI: CONCURRENT TASK PROCESSING SYSTEM ===")
    tracker = SafeMetricsTracker()
    processor = ConcurrentTaskProcessor(metrics_tracker=tracker)

    # 1. ThreadPool Execution
    tasks = [f"SENSOR_READ_{i:02d}" for i in range(1, 7)]
    print(f"\n[1] Menjalankan {len(tasks)} I/O task secara paralel...")
    io_res = processor.process_io_batch(tasks, max_workers=3)
    print(f" -> Berhasil memproses {len(io_res)} task I/O.")

    # 2. Asyncio Execution dengan Timeout
    endpoints = ["/api/v1/network", "/api/v1/slow_satellite", "/api/v1/traffic"]
    print(f"\n[2] Menjalankan {len(endpoints)} endpoint asinkron dengan proteksi timeout...")
    async_res = asyncio.run(processor.process_async_batch(endpoints, timeout_sec=0.05))
    for item in async_res:
        print(f" -> Endpoint {item['endpoint']}: Status={item['status']}")

    # 3. Validasi Ringkasan Metrik
    summary = tracker.metrics
    print("\n[3] Ringkasan Metrik Operasional:")
    print(f" -> Sukses  : {summary['success']}")
    print(f" -> Timeout : {summary['timeout']}")
    print(f" -> Gagal   : {summary['failure']}")
    print(f" -> Total   : {summary['total']}")

    assert summary["success"] == 8, f"Ekspektasi 8 sukses, diperoleh {summary['success']}"
    assert summary["timeout"] == 1, f"Ekspektasi 1 timeout, diperoleh {summary['timeout']}"
    print("\n[OK] SEMUA ASINKRON & THREAD-SAFE ASSERTIONS LULUS DENGAN SEMPURNA!")


if __name__ == "__main__":
    main()
