"""Chapter 28 Example 03: Processing JSON Payloads Defensively
Python Learning Hub - Professional Python Engineering
"""

import json


def parse_and_validate_telemetry_json(raw_json_str: str) -> dict[str, str | float]:
    """Mengurai string JSON dan memvalidasi tipe serta keberadaan field wajib."""
    try:
        data = json.loads(raw_json_str)
    except json.JSONDecodeError as err:
        raise ValueError(f"Sintaks JSON tidak valid: {err}")

    if not isinstance(data, dict):
        raise TypeError(f"Payload JSON harus berupa object/dict, bukan {type(data).__name__}")

    required_fields = ["tower_id", "frequency_mhz", "signal_dbm"]
    for field in required_fields:
        if field not in data:
            raise KeyError(f"Field wajib '{field}' tidak ditemukan dalam response JSON")

    return {
        "tower_id": str(data["tower_id"]),
        "frequency_mhz": float(data["frequency_mhz"]),
        "signal_dbm": float(data["signal_dbm"]),
    }


def main() -> None:
    valid_payload = '{"tower_id": "TWR-JKT-09", "frequency_mhz": 2100.5, "signal_dbm": -78.2}'
    parsed = parse_and_validate_telemetry_json(valid_payload)
    print("Hasil Validasi JSON:")
    print(f" -> Tower ID  : {parsed['tower_id']}")
    print(f" -> Frekuensi : {parsed['frequency_mhz']} MHz")
    print(f" -> Signal    : {parsed['signal_dbm']} dBm")

    # Uji coba payload cacat
    try:
        parse_and_validate_telemetry_json('{"tower_id": "TWR-ERR"}')
    except KeyError as err:
        print(f"Validasi berhasil menolak: {err}")


if __name__ == "__main__":
    main()

