import struct
import sys
from pathlib import Path
import serial

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e01_01_serial_frame_parser import compute_xor_checksum, parse_telem_frame
from e01_03_sensor_smoothing_calib import exponential_moving_average


def test_checksum_and_frame_parser_filters_corrupted_lines() -> None:
    valid_body = "TELEM,101,28.4,62.0,3.85"
    assert compute_xor_checksum(valid_body) == "7F"

    log_path = CODE_DIR.parent / "datasets" / "serial_sensor_frames.log"
    parsed = [parse_telem_frame(ln) for ln in log_path.read_text(encoding="utf-8").splitlines()]
    ok = [item for item in parsed if item is not None]
    assert len(ok) == 4
    assert all(item["node_id"] in {101, 102} for item in ok)


def test_struct_roundtrip_and_loopback_serial() -> None:
    pkt = struct.Struct("<Hff")
    raw = pkt.pack(105, 31.25, 55.5)
    assert len(raw) == 10
    nid, temp, hum = pkt.unpack(raw)
    assert nid == 105 and abs(temp - 31.25) < 1e-4 and abs(hum - 55.5) < 1e-4

    ser = serial.serial_for_url("loop://", timeout=0.5)
    try:
        ser.write(b"$TELEM,101,28.4,62.0,3.85*7F\n")
        rec = parse_telem_frame(ser.readline().decode("ascii"))
        assert rec is not None and rec["node_id"] == 101
    finally:
        ser.close()

    ema = exponential_moving_average([20.0, 30.0], alpha=0.5)
    assert ema == [20.0, 25.0]

