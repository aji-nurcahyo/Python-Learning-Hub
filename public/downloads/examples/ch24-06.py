"""Chapter 24 Example 06: Generator Pipeline Chaining
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Generator, Iterable


def data_source() -> Generator[int, None, None]:
    """Tahap 1: Penghasil data mentah (raw integer signal levels)."""
    for val in [12, 45, 88, 102, 33, 95, 120, 15]:
        yield val


def threshold_filter(stream: Iterable[int], min_val: int) -> Generator[int, None, None]:
    """Tahap 2: Filter sinyal di atas ambang batas (lazy filter)."""
    for item in stream:
        if item >= min_val:
            yield item


def amplify_transform(stream: Iterable[int], factor: float) -> Generator[float, None, None]:
    """Tahap 3: Transformasi penguatan nilai sinyal."""
    for item in stream:
        yield round(item * factor, 1)


def main() -> None:
    # Membangun rantai pipeline (composable generator pipeline)
    pipeline = amplify_transform(threshold_filter(data_source(), min_val=50), factor=1.5)

    print("Hasil pemrosesan generator pipeline (sinyal >= 50, dikalikan 1.5):")
    for output in pipeline:
        print(f" Output teramplifikasi: {output}")


if __name__ == "__main__":
    main()

