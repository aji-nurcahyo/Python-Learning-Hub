"""Chapter 24 Example 08: Context Manager with @contextlib.contextmanager
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Generator
from contextlib import contextmanager


@contextmanager
def temporary_channel(channel_id: int) -> Generator[str, None, None]:
    """Mengalokasikan frekuensi kanal sementara dan menjamin pembebasan sumber daya."""
    print(f"[ALLOCATE] Frekuensi kanal #{channel_id} dialokasikan")
    try:
        yield f"CH-{channel_id}"
    finally:
        print(f"[RELEASE] Frekuensi kanal #{channel_id} dikembalikan ke pool")


def main() -> None:
    print("Sebelum blok context:")
    with temporary_channel(104) as ch:
        print(f"Sedang mentransmisikan sinyal melalui kanal: {ch}")
    print("Setelah blok context selesai.")


if __name__ == "__main__":
    main()

