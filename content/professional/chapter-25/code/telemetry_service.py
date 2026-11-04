"""Layanan Telemetri & Validasi Tipe Statis (Chapter 25)
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Callable
from domain_types import TelemetryRecord
from protocols import Transmittable
from containers import EntityRepository


class TelemetryService:
    """Layanan bisnis yang memproses telemetri dengan jaminan keamanan tipe statis."""

    def __init__(self, repository: EntityRepository[TelemetryRecord]) -> None:
        self.repository = repository

    def ingest_record(self, record: TelemetryRecord) -> bool:
        # Runtime validation melengkapi static typing
        if not isinstance(record.get("node_id"), str):
            raise TypeError("node_id harus berupa string")
        if not isinstance(record.get("rsrp_dbm"), (int, float)):
            raise TypeError("rsrp_dbm harus berupa numerik")

        self.repository.save(record)
        return True

    def filter_records(
        self,
        predicate: Callable[[TelemetryRecord], bool],
    ) -> list[TelemetryRecord]:
        return [r for r in self.repository.get_all() if predicate(r)]

    @staticmethod
    def transmit(payload: Transmittable) -> str:
        """Mengirimkan payload apa pun yang memenuhi protokol Transmittable."""
        return f"TX_OUT -> {payload.serialize()}"
