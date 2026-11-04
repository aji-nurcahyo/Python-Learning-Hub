"""Chapter 24 Example 02: Execution Time Measurement Decorator
Python Learning Hub - Professional Python Engineering
"""

import functools
import time
from typing import Any, Callable


def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator untuk mengukur durasi eksekusi fungsi menggunakan time.perf_counter()."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_sec = time.perf_counter() - start_time
        # Memastikan durasi terukur valid secara non-negatif
        is_valid = elapsed_sec >= 0.0
        print(f"[BENCHMARK] {func.__name__} selesai diproses (Valid: {is_valid})")
        return result

    return wrapper


@measure_execution_time
def process_signal_block(samples: int) -> int:
    total = 0
    for i in range(samples):
        total += i % 7
    return total


def main() -> None:
    res = process_signal_block(5000)
    print(f"Total kalkulasi: {res}")


if __name__ == "__main__":
    main()
