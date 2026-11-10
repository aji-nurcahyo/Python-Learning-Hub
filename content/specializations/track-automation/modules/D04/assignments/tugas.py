"""Starter code Tugas D04: Resilient Scheduled Automation & Alert Dispatcher."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Callable, TypeVar
import httpx

T = TypeVar("T")


def run_with_backoff(
    op: Callable[[], T],
    max_attempts: int = 3,
    base_delay: float = 0.5,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> T:
    """Menjalankan operasi dengan retry exponential backoff yang deterministik diuji."""
    # TODO: Implementasikan loop percobaan & pemanggilan sleep_fn(base_delay * 2**attempt)
    raise NotImplementedError("Implementasikan run_with_backoff")


class JobLedger:
    def __init__(self, state_path: Path) -> None:
        self.state_path = state_path

    def has_completed(self, job_key: str) -> bool:
        # TODO: Baca state JSON dan periksa keberadaan job_key
        raise NotImplementedError("Implementasikan has_completed")

    def mark_completed(self, job_key: str) -> None:
        # TODO: Simpan status selesai ke file JSON secara persisten
        raise NotImplementedError("Implementasikan mark_completed")


def dispatch_webhook_alert(client: httpx.Client, url: str, job_name: str, detail: str) -> int:
    """Mengirim JSON alert webhook dan mengembalikan HTTP status code."""
    # TODO: Post JSON {'job': job_name, 'detail': detail} dan panggil resp.raise_for_status()
    raise NotImplementedError("Implementasikan dispatch_webhook_alert")


if __name__ == "__main__":
    print("Starter D04 siap diuji memakai pytest dan httpx.MockTransport.")

