"""Manajer Sumber Daya & Konteks Eksekusi (Chapter 24)
Python Learning Hub - Professional Python Engineering
"""

import time
from contextlib import contextmanager
from collections.abc import Generator
from types import TracebackType
from typing import Any


class SafeFileSession:
    """Class-based context manager untuk membuka dan menutup berkas secara aman."""

    def __init__(self, filename: str, mode: str = "r") -> None:
        self.filename = filename
        self.mode = mode
        self.file_obj: Any = None

    def __enter__(self) -> Any:
        self.file_obj = open(self.filename, self.mode, encoding="utf-8")
        return self.file_obj

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        if self.file_obj and not self.file_obj.closed:
            self.file_obj.close()
        return False  # Propagate exception jika terjadi


@contextmanager
def execution_timer(label: str) -> Generator[dict[str, Any], None, None]:
    """Generator-based context manager menggunakan contextlib untuk pengukuran waktu."""
    metrics: dict[str, Any] = {"label": label, "elapsed_sec": 0.0, "success": False}
    start = time.perf_counter()
    try:
        yield metrics
        metrics["success"] = True
    finally:
        metrics["elapsed_sec"] = round(time.perf_counter() - start, 6)

