"""Chapter 28 Example 06: Request Timeout Configuration
Python Learning Hub - Professional Python Engineering
"""

import time


class RequestTimeoutException(Exception):
    pass


def request_with_timeout(endpoint: str, timeout_sec: float, simulated_latency: float) -> str:
    """Mensimulasikan mekanisme guard timeout pada pemanggilan HTTP."""
    print(f"Mengirim permintaan ke {endpoint} (Batas timeout: {timeout_sec}s)...")
    start = time.perf_counter()

    # Simulasi latensi jaringan
    time.sleep(simulated_latency)
    elapsed = time.perf_counter() - start

    if elapsed > timeout_sec:
        raise RequestTimeoutException(
            f"Koneksi ke {endpoint} timeout setelah {elapsed:.2f}s (Maksimal {timeout_sec}s)"
        )

    return f"Respons diterima dari {endpoint} dalam {elapsed:.3f}s"


def main() -> None:
    # 1. Permintaan cepat (di bawah batas timeout)
    res = request_with_timeout("https://api.telecom.internal/fast", timeout_sec=0.1, simulated_latency=0.01)
    print("Hasil Permintaan 1: SUKSES")

    # 2. Permintaan lambat (melebihi batas timeout)
    try:
        request_with_timeout("https://api.telecom.internal/slow", timeout_sec=0.02, simulated_latency=0.05)
    except RequestTimeoutException as err:
        print(f"Hasil Permintaan 2: TERTANGKAP TIMEOUT -> {err}")


if __name__ == "__main__":
    main()

