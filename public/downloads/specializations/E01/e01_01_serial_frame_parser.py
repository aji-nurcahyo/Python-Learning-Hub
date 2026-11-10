from pathlib import Path


def compute_xor_checksum(payload: str) -> str:
    acc = 0
    for ch in payload:
        acc ^= ord(ch)
    return f"{acc:02X}"


def parse_telem_frame(line: str) -> dict | None:
    stripped = line.strip()
    if not stripped.startswith("$") or "*" not in stripped:
        return None
    body, _, received_crc = stripped[1:].partition("*")
    if len(received_crc) != 2:
        return None
    if compute_xor_checksum(body) != received_crc.upper():
        return None
    parts = body.split(",")
    if len(parts) != 5 or parts[0] != "TELEM":
        return None
    return {
        "node_id": int(parts[1]),
        "temp_c": float(parts[2]),
        "humidity_pct": float(parts[3]),
        "voltage_v": float(parts[4]),
    }


if __name__ == "__main__":
    log_path = Path(__file__).resolve().parent.parent / "datasets" / "serial_sensor_frames.log"
    valid_records = []
    rejected = 0
    for raw_line in log_path.read_text(encoding="utf-8").splitlines():
        parsed = parse_telem_frame(raw_line)
        if parsed is None:
            rejected += 1
        else:
            valid_records.append(parsed)

    print("Frame valid lolos checksum :", len(valid_records))
    print("Frame rusak/terpotong ditolak:", rejected)
    for rec in valid_records:
        print(" -", rec)

