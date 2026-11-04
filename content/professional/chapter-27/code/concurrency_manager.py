"""Chapter 27: Concurrent & Asynchronous Programming
Manajer Eksekusi Konkuren (ThreadPool, ProcessPool, Asyncio & Lock)
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import threading
import time
from typing import Any, Callable

try:
    from tasks import ConcurrentTask, TaskStatus, simulate_cpu_bound_task, simulate_io_task
except ImportError:
    from .tasks import ConcurrentTask, TaskStatus, simulate_cpu_bound_task, simulate_io_task


class SynchronizedCounter:
    """Penghitung thread-safe yang dilindungi oleh threading.Lock."""

    def __init__(self, initial_value: int = 0) -> None:
        self._value = initial_value
        self._lock = threading.Lock()

    def increment(self, amount: int = 1) -> int:
        with self._lock:
            self._value += amount
            return self._value

    def decrement(self, amount: int = 1) -> int:
        with self._lock:
            self._value -= amount
            return self._value

    @property
    def value(self) -> int:
        with self._lock:
            return self._value


class ConcurrencyManager:
    """Manajer orkestrasi task konkuren dengan ThreadPool, ProcessPool, dan asyncio."""

    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers
        self.counter = SynchronizedCounter()

    def execute_threaded(
        self,
        task_ids: list[str],
        worker_fn: Callable[[str], dict[str, Any]] = simulate_io_task,
    ) -> list[dict[str, Any]]:
        """Mengeksekusi task I/O-bound menggunakan ThreadPoolExecutor."""
        results: list[dict[str, Any]] = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_id = {executor.submit(worker_fn, tid): tid for tid in task_ids}
            for future in as_completed(future_to_id):
                try:
                    res = future.result()
                    self.counter.increment()
                    results.append(res)
                except Exception as exc:
                    results.append({"task_id": future_to_id[future], "error": str(exc)})
        # Urutkan berdasarkan task_id demi determinisme
        results.sort(key=lambda x: str(x.get("task_id", "")))
        return results

    def execute_multiprocess(
        self,
        task_ids: list[str],
        worker_fn: Callable[[str], dict[str, Any]] = simulate_cpu_bound_task,
    ) -> list[dict[str, Any]]:
        """Mengeksekusi task CPU-bound menggunakan ProcessPoolExecutor melintasi multi-core CPU."""
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            # executor.map mempertahankan urutan input secara deterministik
            results = list(executor.map(worker_fn, task_ids))
        return results

    async def execute_async_gather(
        self,
        endpoints: list[str],
        simulated_delay: float = 0.02,
    ) -> list[dict[str, Any]]:
        """Mengeksekusi request asinkron non-blocking menggunakan asyncio.gather()."""
        async def fetch_item(endpoint: str) -> dict[str, Any]:
            await asyncio.sleep(simulated_delay)
            return {
                "endpoint": endpoint,
                "status": "COMPLETED",
                "timestamp": round(time.time(), 2),
            }

        tasks = [fetch_item(ep) for ep in endpoints]
        results = await asyncio.gather(*tasks)
        return list(results)

    async def execute_with_timeout(
        self,
        coro_fn: Callable[[], Any],
        timeout_seconds: float = 0.1,
    ) -> Any:
        """Mengeksekusi coroutine dengan batas waktu timeout dan pembatalan otomatis."""
        try:
            return await asyncio.wait_for(coro_fn(), timeout=timeout_seconds)
        except asyncio.TimeoutError:
            return {"status": "TIMEOUT", "message": f"Task melebihi batas waktu {timeout_seconds}s"}
