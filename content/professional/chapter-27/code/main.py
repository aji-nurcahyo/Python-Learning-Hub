"""Chapter 27: Concurrent & Asynchronous Programming
Main Application Entry Point: Concurrent Task Processing System
"""

import asyncio
from concurrency_manager import ConcurrencyManager
from tasks import simulate_cpu_bound_task, simulate_io_task


def run_system() -> None:
    print("Memulai Concurrent Task Processing System...")
    manager = ConcurrencyManager(max_workers=3)

    # 1. Eksekusi ThreadPool
    io_tasks = ["TASK-IO-1", "TASK-IO-2", "TASK-IO-3"]
    print(f"\n[1] Menjadwalkan {len(io_tasks)} task I/O ke ThreadPoolExecutor:")
    io_results = manager.execute_threaded(io_tasks, worker_fn=simulate_io_task)
    for res in io_results:
        print(f" -> {res['task_id']}: status={res.get('status')} (durasi: {res.get('duration_sec')}s)")
    print(f"Total task sukses tercatat di SafeCounter: {manager.counter.value}")

    # 2. Eksekusi Asyncio Gather
    endpoints = ["/metrics/cpu", "/metrics/memory", "/metrics/bandwidth"]
    print(f"\n[2] Menjalankan {len(endpoints)} endpoint asinkron via asyncio.gather():")
    async_results = asyncio.run(manager.execute_async_gather(endpoints))
    for res in async_results:
        print(f" -> Endpoint {res['endpoint']}: status={res['status']}")

    print("\nConcurrent Task Processing System berhasil menyelesaikan seluruh beban kerja.")


if __name__ == "__main__":
    run_system()

