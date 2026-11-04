"""Unit Test Suite untuk Chapter 27: Concurrent & Asynchronous Programming
Memvalidasi ThreadPool, ProcessPool/CPU, Asyncio, Timeout, dan Lock Synchronization.
"""

import asyncio
import os
import sys
import unittest

# Menambahkan direktori code ke sys.path agar modul dapat diimpor
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from concurrency_manager import ConcurrencyManager, SynchronizedCounter
from tasks import simulate_cpu_bound_task, simulate_io_task


class TestConcurrencyMechanisms(unittest.TestCase):
    """Test case untuk memvalidasi eksekusi dan integritas pola konkurensi."""

    def setUp(self) -> None:
        self.manager = ConcurrencyManager(max_workers=3)

    def test_synchronized_counter_thread_safety(self) -> None:
        """Memvalidasi bahwa SynchronizedCounter bebas dari race condition saat diakses multi-thread."""
        import threading
        counter = SynchronizedCounter(initial_value=0)

        def worker() -> None:
            for _ in range(50):
                counter.increment()

        threads = [threading.Thread(target=worker) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(counter.value, 500)
        counter.decrement(100)
        self.assertEqual(counter.value, 400)

    def test_thread_pool_execution(self) -> None:
        """Memvalidasi eksekusi I/O task konkuren pada ThreadPoolExecutor."""
        task_ids = ["T-101", "T-102", "T-103"]
        results = self.manager.execute_threaded(task_ids, worker_fn=simulate_io_task)

        self.assertEqual(len(results), 3)
        self.assertEqual(self.manager.counter.value, 3)
        for res in results:
            self.assertEqual(res["status"], "SUCCESS")
            self.assertIn(res["task_id"], task_ids)

    def test_cpu_bound_task_computation(self) -> None:
        """Memvalidasi fungsi simulasi tugas CPU-bound menghasilkan checksum deterministik."""
        res = simulate_cpu_bound_task("CPU-01", n=5000)
        self.assertEqual(res["task_id"], "CPU-01")
        self.assertEqual(res["type"], "CPU")
        self.assertIsInstance(res["result_checksum"], int)

    def test_asyncio_gather_nonblocking(self) -> None:
        """Memvalidasi pengumpulan hasil coroutine secara konkuren dengan asyncio.gather()."""
        endpoints = ["/api/v1/sensors", "/api/v1/gateways"]
        loop_results = asyncio.run(self.manager.execute_async_gather(endpoints, simulated_delay=0.01))

        self.assertEqual(len(loop_results), 2)
        endpoint_names = [item["endpoint"] for item in loop_results]
        self.assertIn("/api/v1/sensors", endpoint_names)
        self.assertIn("/api/v1/gateways", endpoint_names)

    def test_asyncio_timeout_handling(self) -> None:
        """Memvalidasi bahwa eksekusi coroutine yang melewati timeout dibatalkan secara elegan."""
        async def slow_operation() -> str:
            await asyncio.sleep(0.5)
            return "COMPLETED"

        result = asyncio.run(
            self.manager.execute_with_timeout(slow_operation, timeout_seconds=0.05)
        )
        self.assertEqual(result.get("status"), "TIMEOUT")
        self.assertIn("melebihi batas waktu", result.get("message", ""))


if __name__ == "__main__":
    unittest.main()

