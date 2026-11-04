"""Chapter 27 Example 09: Concurrency Model Decision Matrix
Python Learning Hub - Professional Python Engineering
"""


def evaluate_workload(workload_type: str, has_blocking_io: bool) -> dict[str, str]:
    """Mengevaluasi dan merekomendasikan paradigma konkurensi yang tepat."""
    if workload_type == "CPU_BOUND":
        return {
            "model": "Multiprocessing (ProcessPoolExecutor)",
            "alasan": "Bypass GIL dengan memanfaatkan multi-core CPU fisik secara paralel murni",
        }
    elif has_blocking_io:
        return {
            "model": "Multi-threading (ThreadPoolExecutor)",
            "alasan": "Ideal untuk library I/O pemblokir lama (blocking C-extensions, file I/O)",
        }
    else:
        return {
            "model": "Asynchronous (asyncio coroutines)",
            "alasan": "Single-thread cooperative multitasking dengan ribuan soket jaringan non-blocking",
        }


def main() -> None:
    cases = [
        ("Kompresi Video / Kriptografi CRC", "CPU_BOUND", False),
        ("Query Database Relasional Legacy", "IO_BOUND", True),
        ("WebSockets Telemetri 10.000 Koneksi", "IO_BOUND", False),
    ]

    print("=== MATRIKS PENGAMBILAN KEPUTUSAN KONKURENSI ===")
    for desc, wtype, blocking in cases:
        rec = evaluate_workload(wtype, blocking)
        print(f"\nKasus: {desc} [{wtype}]")
        print(f" -> Rekomendasi : {rec['model']}")
        print(f" -> Pertimbangan: {rec['alasan']}")


if __name__ == "__main__":
    main()
