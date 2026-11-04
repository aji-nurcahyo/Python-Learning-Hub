"""Chapter 25 Example 03: TypedDict for Structured Dictionaries
Python Learning Hub - Professional Python Engineering
"""

from typing import NotRequired, TypedDict


class CellTelemetryRecord(TypedDict):
    """Skema kamus terstruktur untuk data telemetri seluler."""

    cell_id: str
    rsrp_dbm: float
    is_active: bool
    azimuth: NotRequired[int]


def summarize_cell(telemetry: CellTelemetryRecord) -> str:
    """Mengkonsumsi TypedDict dengan type safety pada kunci dictionary."""
    azimuth_info = f", Azimuth: {telemetry['azimuth']} deg" if "azimuth" in telemetry else ""
    return (
        f"Cell: {telemetry['cell_id']} | "
        f"RSRP: {telemetry['rsrp_dbm']} dBm | "
        f"Aktif: {telemetry['is_active']}"
        f"{azimuth_info}"
    )


def main() -> None:
    rec1: CellTelemetryRecord = {
        "cell_id": "BTS-BDO-01",
        "rsrp_dbm": -82.4,
        "is_active": True,
        "azimuth": 120,
    }
    rec2: CellTelemetryRecord = {
        "cell_id": "BTS-BDO-02",
        "rsrp_dbm": -104.1,
        "is_active": False,
    }
    print(summarize_cell(rec1))
    print(summarize_cell(rec2))


if __name__ == "__main__":
    main()
