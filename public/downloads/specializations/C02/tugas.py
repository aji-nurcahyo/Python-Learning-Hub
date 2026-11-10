"""Starter code Tugas C02: REST API Inventaris Perangkat Jaringan."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field


class DeviceCreate(BaseModel):
    serial_number: str = Field(min_length=4, max_length=40)
    model_name: str = Field(min_length=2)
    power_watt: float = Field(gt=0.0)
    status: str = Field(default="active")


class DeviceOut(DeviceCreate):
    id: int


def create_devices_app() -> FastAPI:
    """Membangun aplikasi FastAPI inventaris perangkat jaringan."""
    app = FastAPI(title="Network Inventory API")
    # TODO: Implementasikan endpoint POST/GET/PUT/DELETE beserta HTTPException 404
    raise NotImplementedError("Implementasikan route CRUD pada create_devices_app")


if __name__ == "__main__":
    print("Starter C02 siap diuji memakai fastapi.testclient.TestClient.")
