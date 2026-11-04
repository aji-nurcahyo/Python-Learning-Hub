"""Chapter 27: Concurrent & Asynchronous Programming
Model Data & Definisi Task untuk Sistem Pemrosesan Konkuren
"""

from dataclasses import dataclass, field
from enum import Enum
import time
from typing import Any, Optional


class TaskStatus(str, Enum):
    """Status siklus hidup task konkuren."""
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


@dataclass
class ConcurrentTask:
    """Representasi unit kerja yang dieksekusi secara konkuren."""
    task_id: str
    task_type: str  # 'io_bound' | 'cpu_bound'
    payload: Any
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[Any] = None
    error_message: Optional[str] = None
    duration_sec: float = 0.0


def simulate_io_task(task_id: str, delay_sec: float = 0.05) -> dict[str, Any]:
    """Simulasi operasi I/O-bound (seperti network socket atau pembacaan file disk)."""
    start = time.perf_counter()
    time.sleep(delay_sec)
    duration = time.perf_counter() - start
    return {
        "task_id": task_id,
        "type": "I/O",
        "duration_sec": round(duration, 4),
        "status": "SUCCESS",
    }


def simulate_cpu_bound_task(task_id: str, n: int = 150_000) -> dict[str, Any]:
    """Simulasi kalkulasi intensif CPU (seperti hashing atau komputasi matematika)."""
    start = time.perf_counter()
    total = sum(i * i for i in range(n))
    duration = time.perf_counter() - start
    return {
        "task_id": task_id,
        "type": "CPU",
        "result_checksum": total % 1_000_007,
        "duration_sec": round(duration, 4),
    }

