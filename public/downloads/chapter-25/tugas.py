"""Template Tugas Mahasiswa: Chapter 25 - Type Hints & Code Quality
Topik: Type-Safe Network Observability Toolkit
Platform: Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo
Institusi: Institut Teknologi Sumatera (ITERA)
"""

from collections.abc import Callable
from typing import Generic, NotRequired, Protocol, TypeVar, TypedDict, runtime_checkable


# 1. TypedDict Schema: MetricPayload
class MetricPayload(TypedDict):
    metric_name: str
    value: float
    unit: str
    timestamp: str
    tags: NotRequired[dict[str, str]]


# 2. Structural Subtyping Protocol: MetricEncoder
@runtime_checkable
class MetricEncoder(Protocol):
    def encode_metric(self, metric: MetricPayload) -> str:
        ...


# Implementasi encoder konkret yang memenuhi MetricEncoder secara struktural
class JsonMetricEncoder:
    def encode_metric(self, metric: MetricPayload) -> str:
        tag_str = f" | tags={metric.get('tags', {})}"
        return f'{{"name": "{metric["metric_name"]}", "val": {metric["value"]}, "unit": "{metric["unit"]}"}}{tag_str}'


class LineProtocolEncoder:
    def encode_metric(self, metric: MetricPayload) -> str:
        return f"{metric['metric_name']},unit={metric['unit']} value={metric['value']} {metric['timestamp']}"


# 3. Generic Repository: MetricStore[T]
T = TypeVar("T")


class MetricStore(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def append(self, item: T) -> None:
        self._items.append(item)

    def all(self) -> list[T]:
        return list(self._items)

    def size(self) -> int:
        return len(self._items)


# 4. Service Pemrosesan Beranotasi Lengkap
class MetricService:
    def __init__(self, store: MetricStore[MetricPayload], encoder: MetricEncoder) -> None:
        self.store = store
        self.encoder = encoder

    def record_metric(self, payload: MetricPayload) -> str:
        # Runtime validation defensif
        if not isinstance(payload.get("value"), (int, float)):
            raise TypeError("Nilai metrik harus berupa numerik (int atau float)")

        self.store.append(payload)
        return self.encoder.encode_metric(payload)

    def filter_metrics(
        self,
        predicate: Callable[[MetricPayload], bool],
    ) -> list[MetricPayload]:
        return [m for m in self.store.all() if predicate(m)]


def main() -> None:
    print("=== PENGUJIAN TYPE-SAFE OBSERVABILITY TOOLKIT ===")

    store: MetricStore[MetricPayload] = MetricStore()
    encoder = JsonMetricEncoder()
    service = MetricService(store, encoder)

    # Ingest metrik 1
    m1: MetricPayload = {
        "metric_name": "cpu_load",
        "value": 42.5,
        "unit": "percent",
        "timestamp": "2026-11-04T12:00:00Z",
        "tags": {"host": "gw-01", "region": "jkt"},
    }
    # Ingest metrik 2
    m2: MetricPayload = {
        "metric_name": "bandwidth_utilization",
        "value": 850.0,
        "unit": "mbps",
        "timestamp": "2026-11-04T12:00:05Z",
    }

    out1 = service.record_metric(m1)
    out2 = service.record_metric(m2)

    print("\n--- Metrik Terformat (JSON Encoder) ---")
    print(f" * {out1}")
    print(f" * {out2}")

    # Ganti encoder ke LineProtocolEncoder (Protocol interchangeability)
    service.encoder = LineProtocolEncoder()
    print("\n--- Format Line Protocol ---")
    for item in store.all():
        print(f" * {service.encoder.encode_metric(item)}")

    # Filter metrik
    high_metrics = service.filter_metrics(lambda m: m["value"] > 50.0)
    print(f"\nTotal metrik bernilai tinggi (> 50.0): {len(high_metrics)}")


if __name__ == "__main__":
    main()
