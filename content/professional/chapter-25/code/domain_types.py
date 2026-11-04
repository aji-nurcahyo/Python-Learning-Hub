"""Definisi Tipe Data & Skema TypedDict (Chapter 25)
Python Learning Hub - Professional Python Engineering
"""

from typing import NotRequired, TypedDict


class TelemetryRecord(TypedDict):
    """Skema kamus data terstruktur untuk metrik telemetri simpul."""

    node_id: str
    frequency_mhz: float
    rsrp_dbm: float
    snr_db: float
    is_active: bool
    description: NotRequired[str]


class IncidentReport(TypedDict):
    """Skema laporan insiden jaringan terstandar."""

    incident_id: str
    severity: str
    timestamp: str
    affected_nodes: list[str]


type NodeId = str
type SignalReading = float | int
