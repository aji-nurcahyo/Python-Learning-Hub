"""Chapter 28 Example 10: Responsible Retry Logic with Exponential Backoff
Python Learning Hub - Professional Python Engineering
"""

import time
from typing import Any


class SimulatedTransientServer:
    """Simulasi server yang mengalami kegagalan sementara sebelum kembali pulih."""

    def __init__(self, failure_count: int = 2) -> None:
        self.attempts = 0
        self.failure_count = failure_count

    def request(self) -> dict[str, Any]:
        self.attempts += 1
        if self.attempts <= self.failure_count:
            # 503 Service Unavailable atau 429 Too Many Requests
            return {"status": 503, "error": "Service Temporarily Unavailable"}
        return {"status": 200, "data": "Koneksi gateway gateway telemetri berhasil"}


def request_with_exponential_backoff(
    server: SimulatedTransientServer,
    max_retries: int = 3,
    initial_backoff: float = 0.05,
    backoff_factor: float = 2.0,
) -> dict[str, Any]:
    """Mengirim request dengan pola retry eksponensial untuk menghadapi transient error."""
    delay = initial_backoff

    for attempt in range(1, max_retries + 1):
        print(f"Percobaan #{attempt}: Mengirim HTTP request...")
        response = server.request()

        if response["status"] == 200:
            print(" -> Berhasil memperoleh status 200 OK.")
            return response

        print(f" -> Gagal (Status {response['status']}): {response.get('error')}")
        if attempt < max_retries:
            print(f" -> Menunggu backoff {delay:.2f} detik sebelum mencoba ulang...")
            time.sleep(delay)
            delay *= backoff_factor

    raise RuntimeError(f"Request gagal setelah {max_retries} kali percobaan.")


def main() -> None:
    print("Simulasi Penanganan Gangguan Sementara (Transient Fault) dengan Exponential Backoff:\n")
    server = SimulatedTransientServer(failure_count=2)

    try:
        final_res = request_with_exponential_backoff(server, max_retries=4)
        print(f"\nHasil Akhir: {final_res}")
    except RuntimeError as err:
        print(f"\nOperasi Dihentikan: {err}")


if __name__ == "__main__":
    main()

