"""Chapter 25 Example 04: Protocol & Structural Subtyping
Python Learning Hub - Professional Python Engineering
"""

from typing import Protocol


class Transmittable(Protocol):
    """Protokol struktural: Objek apa pun yang memiliki method serialize_payload()."""

    def serialize_payload(self) -> str:
        ...


class SensorPayload:
    """Kelas tanpa pewarisan eksplisit yang memenuhi kontrak Transmittable."""

    def __init__(self, sensor_type: str, value: float) -> None:
        self.sensor_type = sensor_type
        self.value = value

    def serialize_payload(self) -> str:
        return f"{self.sensor_type}:{self.value}"


class TextPayload:
    """Kelas lain yang juga memenuhi kontrak Transmittable secara struktural."""

    def __init__(self, text: str) -> None:
        self.text = text

    def serialize_payload(self) -> str:
        return f"TEXT:{self.text}"


def transmit_packet(payload: Transmittable) -> str:
    """Fungsi yang menerima objek apa pun selama memenuhi protokol Transmittable."""
    return f"TX -> [{payload.serialize_payload()}]"


def main() -> None:
    sensor = SensorPayload("TEMP", 32.8)
    msg = TextPayload("BEACON_ALIVE")

    print(transmit_packet(sensor))
    print(transmit_packet(msg))


if __name__ == "__main__":
    main()
