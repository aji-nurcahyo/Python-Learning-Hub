"""Chapter 25 Example 06: Callable Type Annotations & Pipelines
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Callable


def apply_calibration(
    raw_readings: list[float],
    calibrator: Callable[[float], float],
) -> list[float]:
    """Menerapkan fungsi kalibrator pada setiap data telemetri mentah."""
    return [round(calibrator(val), 2) for val in raw_readings]


def dbm_offset(val: float) -> float:
    return val + 1.25


def main() -> None:
    readings = [-75.0, -82.4, -90.2]
    calibrated = apply_calibration(readings, dbm_offset)
    print(f"Data Mentah      : {readings}")
    print(f"Hasil Kalibrasi  : {calibrated}")


if __name__ == "__main__":
    main()
