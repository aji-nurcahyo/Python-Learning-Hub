"""Template Tugas Mahasiswa: Chapter 24 - Decorators, Generators & Context Managers
Topik: Streaming Telemetry Ingestion Engine
Platform: Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo
Institusi: Institut Teknologi Sumatera (ITERA)
"""

import functools
import time
from collections.abc import Generator, Iterable
from types import TracebackType
from typing import Any, Callable


# 1. Parameterized Decorator: Validasi Nilai Numerik
def enforce_range(min_val: float, max_val: float) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(val: float, *args: Any, **kwargs: Any) -> Any:
            if not (min_val <= val <= max_val):
                raise ValueError(f"Nilai {val} di luar batas toleransi [{min_val}, {max_val}]")
            return func(val, *args, **kwargs)

        return wrapper

    return decorator


# 2. Timing & Audit Decorator
def telemetry_audit(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return {"result": result, "func_name": func.__name__, "elapsed_sec": round(elapsed, 6)}

    return wrapper


# 3. Class-based Context Manager: Channel Lease
class ChannelLeaseContext:
    def __init__(self, channel_id: int) -> None:
        self.channel_id = channel_id
        self.is_leased = False

    def __enter__(self) -> "ChannelLeaseContext":
        self.is_leased = True
        print(f"[SPECTRUM] Kanal #{self.channel_id} berhasil dipinjam (Leased).")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        self.is_leased = False
        print(f"[SPECTRUM] Kanal #{self.channel_id} dikembalikan ke pool (Released).")
        return False  # Jangan menelan exception


# 4. Generator Pipeline: Stream -> Filter -> Aggregate
def stream_records(data_list: list[dict[str, Any]]) -> Generator[dict[str, Any], None, None]:
    for item in data_list:
        yield item.copy()


def filter_outliers(
    stream: Iterable[dict[str, Any]],
    min_snr: float,
    max_snr: float,
) -> Generator[dict[str, Any], None, None]:
    for rec in stream:
        snr = float(rec.get("snr", 0.0))
        if min_snr <= snr <= max_snr:
            yield rec


def transform_records(stream: Iterable[dict[str, Any]]) -> Generator[dict[str, Any], None, None]:
    for rec in stream:
        rec["snr_ratio"] = round(10 ** (rec["snr"] / 10), 2)
        yield rec


# 5. Fungsi Bisnis Berdekorator
@enforce_range(min_val=-130.0, max_val=-30.0)
def process_validated_signal(rsrp_dbm: float) -> str:
    return f"Sinyal RSRP {rsrp_dbm} dBm terverifikasi"


def main() -> None:
    print("=== PENGUJIAN STREAMING TELEMETRY INGESTION ENGINE ===")

    dataset = [
        {"id": "PKT-1", "snr": 15.0, "rsrp": -78.0},
        {"id": "PKT-2", "snr": 3.0, "rsrp": -115.0},   # Filtered out (snr < 10)
        {"id": "PKT-3", "snr": 45.0, "rsrp": -50.0},   # Filtered out (snr > 35)
        {"id": "PKT-4", "snr": 22.5, "rsrp": -82.0},
    ]

    with ChannelLeaseContext(channel_id=88) as lease:
        print(f"Status kanal aktif: {lease.is_leased}")

        # Jalankan generator pipeline secara lazy
        pipeline = transform_records(filter_outliers(stream_records(dataset), min_snr=10.0, max_snr=35.0))

        for item in pipeline:
            sig_status = process_validated_signal(item["rsrp"])
            print(f" -> {item['id']}: SNR={item['snr']} dB (Ratio: {item['snr_ratio']}) | {sig_status}")

    print("Pipeline pemrosesan selesai dengan aman.")


if __name__ == "__main__":
    main()
