"""Chapter 24 Example 05: Lazy Data Processing with Generators
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Generator


def simulate_telemetry_stream(total_records: int) -> Generator[dict[str, float | str], None, None]:
    """Menghasilkan record telemetri satu per satu tanpa menampung seluruh list di memori."""
    for i in range(1, total_records + 1):
        yield {
            "id": f"PKT-{i:03d}",
            "snr_db": round(15.0 + (i % 5) * 2.5, 1),
            "status": "PASS" if i % 4 != 0 else "DEGRADED",
        }


def main() -> None:
    stream = simulate_telemetry_stream(5)
    print("Membaca streaming data telemetri:")
    for record in stream:
        print(f" -> Paket {record['id']}: SNR={record['snr_db']} dB [{record['status']}]")


if __name__ == "__main__":
    main()
