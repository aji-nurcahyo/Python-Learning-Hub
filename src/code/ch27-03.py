"""Chapter 27 Example 03: ThreadPoolExecutor from concurrent.futures
Python Learning Hub - Professional Python Engineering
"""

from concurrent.futures import ThreadPoolExecutor
import time


def fetch_rf_metrics(channel_id: int) -> dict[str, int | float]:
    """Mensimulasikan pengambilan metrik RF dari kanal frekuensi."""
    time.sleep(0.01)
    return {
        "channel_id": channel_id,
        "frequency_mhz": 1800.0 + (channel_id * 5),
        "power_dbm": -75.0 + (channel_id % 3),
    }


def main() -> None:
    channels = [1, 2, 3, 4]
    print(f"Mengeksekusi pengambilan data {len(channels)} kanal via ThreadPoolExecutor...")

    # Menggunakan context manager ThreadPoolExecutor untuk alokasi thread pool
    with ThreadPoolExecutor(max_workers=3) as executor:
        # executor.map mempertahankan urutan hasil sesuai urutan input iterable
        results = list(executor.map(fetch_rf_metrics, channels))

    for item in results:
        print(f" -> Kanal {item['channel_id']}: {item['frequency_mhz']} MHz | Power: {item['power_dbm']} dBm")


if __name__ == "__main__":
    main()

