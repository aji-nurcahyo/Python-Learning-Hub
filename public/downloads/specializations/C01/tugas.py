"""Starter code Tugas C01: Reusable Telemetry HTTP Client."""

from __future__ import annotations

import httpx
from pydantic import BaseModel, Field


class TelemetryRecord(BaseModel):
    device_id: str = Field(min_length=3)
    temp_c: float = Field(ge=-40.0, le=120.0)
    battery_pct: int = Field(ge=0, le=100)


def safe_get_json(client: httpx.Client, path: str, max_attempts: int = 3) -> dict:
    """Mengambil respons JSON dengan retry selektif pada status 502/503/504."""
    # TODO: Implementasikan loop retry selektif dan resp.raise_for_status()
    raise NotImplementedError("Implementasikan safe_get_json")


def fetch_all_pages(client: httpx.Client, endpoint: str) -> list[TelemetryRecord]:
    """Menarik data berhalaman dan memvalidasi tiap item memakai TelemetryRecord."""
    # TODO: Iterasi parameter page=1, 2, ... hingga 'items' kosong lalu validasi via model_validate
    raise NotImplementedError("Implementasikan fetch_all_pages")


if __name__ == "__main__":
    print("Starter C01 siap diuji dengan httpx.MockTransport dan pytest.")
