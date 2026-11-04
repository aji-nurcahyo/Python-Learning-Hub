"""Chapter 27 Example 08: Synchronization with threading.Lock
Python Learning Hub - Professional Python Engineering
"""

import threading


class ThreadSafeTelemetryCounter:
    """Penghitung paket aman-thread (thread-safe) menggunakan locking."""

    def __init__(self) -> None:
        self._count = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        # Menggunakan context manager lock menjamin acquire() dan release() otomatis
        with self._lock:
            current = self._count
            # Simulasi context switch kecil
            self._count = current + 1

    @property
    def value(self) -> int:
        with self._lock:
            return self._count


def worker(counter: ThreadSafeTelemetryCounter, iterations: int) -> None:
    for _ in range(iterations):
        counter.increment()


def main() -> None:
    counter = ThreadSafeTelemetryCounter()
    threads: list[threading.Thread] = []
    num_threads = 4
    iterations_per_thread = 500

    print(f"Menjalankan {num_threads} thread serentak dengan threading.Lock...")
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(counter, iterations_per_thread))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    expected = num_threads * iterations_per_thread
    print(f"Nilai Akhir Counter : {counter.value}")
    print(f"Nilai yang Diharapkan: {expected}")
    print(f"Status Sinkronisasi : {'BEBAS RACE CONDITION' if counter.value == expected else 'TERJADI RACE CONDITION'}")


if __name__ == "__main__":
    main()

