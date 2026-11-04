"""Chapter 25 Example 02: Optional Values & Type Narrowing
Python Learning Hub - Professional Python Engineering
"""


def parse_packet_data(raw_payload: str | None) -> str:
    """Menerima str atau None, melakukan type narrowing untuk keamanan runtime."""
    # Type narrowing: Sebelum pemeriksaan, raw_payload adalah str | None
    if raw_payload is None:
        return "[EMPTY] Tidak ada payload data yang diterima"

    # Setelah pemeriksaan, type checker mengetahui raw_payload pasti bertipe str
    cleaned = raw_payload.strip().upper()
    return f"[PAYLOAD-{len(cleaned)}B] {cleaned}"


def process_reading(value: int | float | str) -> float:
    """Memproses beragam format input dan melakukan konversi tipe secara aman."""
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        return float(value.replace("dBm", "").strip())
    raise TypeError(f"Tipe tidak didukung: {type(value)}")


def main() -> None:
    print(parse_packet_data(None))
    print(parse_packet_data("  ack_frame_sync  "))
    print(f"Hasil konversi: {process_reading('-45.8 dBm')} dBm")


if __name__ == "__main__":
    main()

