"""Kontrak Subtyping Struktural Berbasis Protocol (Chapter 25)
Python Learning Hub - Professional Python Engineering
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Transmittable(Protocol):
    """Protokol struktural untuk objek apa pun yang dapat diubah menjadi string transmisi."""

    def serialize(self) -> str:
        ...


@runtime_checkable
class HealthCheckable(Protocol):
    """Protokol struktural untuk entitas yang dapat diperiksa status kesehatannya."""

    def check_health(self) -> bool:
        ...


class RadioSensor:
    """Implementasi sensor tanpa pewarisan eksplisit yang memenuhi kedua protokol."""

    def __init__(self, sensor_id: str, temperature_c: float) -> None:
        self.sensor_id = sensor_id
        self.temperature_c = temperature_c

    def serialize(self) -> str:
        return f"TEMP_SENSOR:{self.sensor_id}:{self.temperature_c}C"

    def check_health(self) -> bool:
        return self.temperature_c < 70.0
