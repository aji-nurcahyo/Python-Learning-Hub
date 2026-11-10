"""Starter code Tugas E01: Resilient Serial Telemetry Frame Decoder."""

from __future__ import annotations

import struct
from pathlib import Path

PACKET_STRUCT = struct.Struct("<Hff")


def compute_xor_checksum(payload: str) -> str:
    """Menghitung checksum XOR 8-bit dalam format heksadesimal 2 digit huruf kapital."""
    # TODO: Lakukan bitwise XOR untuk setiap karakter di payload
    raise NotImplementedError("Implementasikan compute_xor_checksum")


def parse_telem_frame(raw_line: str) -> dict | None:
    """Mem-parsing frame '$TELEM,id,temp,hum,volt*XX' sambil menolak baris korup."""
    # TODO: Cek awalan '$', tanda '*', kecocokan checksum, dan tipe float/int
    raise NotImplementedError("Implementasikan parse_telem_frame")


def encode_binary_packet(node_id: int, temp_c: float, humidity: float) -> bytes:
    """Mengemas pembacaan sensor menjadi 10-byte biner little-endian."""
    return PACKET_STRUCT.pack(node_id, temp_c, humidity)


def decode_binary_packet(raw_bytes: bytes) -> tuple[int, float, float]:
    """Membongkar 10-byte paket biner menjadi tuple (node_id, temp_c, humidity)."""
    return PACKET_STRUCT.unpack(raw_bytes)


if __name__ == "__main__":
    log_file = Path(__file__).resolve().parent.parent / "datasets" / "serial_sensor_frames.log"
    print(f"Log serial E01 siap diuji dari: {log_file}")

