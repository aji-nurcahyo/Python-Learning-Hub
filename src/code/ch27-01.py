"""Chapter 27 Example 01: Sequential Task Execution
Python Learning Hub - Professional Python Engineering
"""

import time


def process_telemetry_packet(packet_id: int) -> dict[str, int | str]:
    """Mensimulasikan pemrosesan satu paket data secara sekuensial."""
    # Simulasi latensi komputasi kecil
    time.sleep(0.01)
    return {"packet_id": packet_id, "status": "PROCESSED"}


def main() -> None:
    total_packets = 5
    results: list[dict[str, int | str]] = []

    print(f"Memulai pemrosesan {total_packets} paket data secara sekuensial...")
    for pid in range(1, total_packets + 1):
        res = process_telemetry_packet(pid)
        results.append(res)
        print(f" -> Paket #{res['packet_id']}: {res['status']}")

    print(f"Selesai! Total paket diproses: {len(results)}")


if __name__ == "__main__":
    main()

