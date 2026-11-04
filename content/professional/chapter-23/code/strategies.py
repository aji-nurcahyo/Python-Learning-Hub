"""Strategi Pemrosesan Diagnostik (Chapter 23)
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod
from typing import Any


class DiagnosticStrategy(ABC):
    """Antarmuka strategi diagnostik sistem."""

    @abstractmethod
    def evaluate(self, health_data: dict[str, Any]) -> str:
        pass


class StandardDiagnostic(DiagnosticStrategy):
    """Diagnostik standar untuk pemeriksaan cepat berkala."""

    def evaluate(self, health_data: dict[str, Any]) -> str:
        dev_id = health_data.get("device_id", "UNKNOWN")
        is_online = health_data.get("online", False)
        status_str = "SEHAT" if is_online else "OFFLINE"
        return f"[STANDARD] {dev_id}: {status_str}"


class DeepDiagnostic(DiagnosticStrategy):
    """Diagnostik mendalam untuk audit keandalan perangkat."""

    def evaluate(self, health_data: dict[str, Any]) -> str:
        dev_id = health_data.get("device_id", "UNKNOWN")
        dev_type = health_data.get("type", "Generic")
        is_online = health_data.get("online", False)
        metrics = ", ".join(f"{k}={v}" for k, v in health_data.items() if k not in ("device_id", "type", "online"))
        return f"[DEEP AUDIT] {dev_id} ({dev_type}) Online={is_online} | Param: {metrics}"

