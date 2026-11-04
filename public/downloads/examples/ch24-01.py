"""Chapter 24 Example 01: Logging Decorator with functools.wraps
Python Learning Hub - Professional Python Engineering
"""

import functools
from typing import Any, Callable


def audit_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator untuk mencatat pemanggilan fungsi beserta argumen dan outputnya."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[LOG CALL] {func.__name__} dengan args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG RESULT] {func.__name__} menghasilkan {result}")
        return result

    return wrapper


@audit_logger
def calculate_path_loss(distance_km: float, freq_mhz: float) -> float:
    """Menghitung estimasi path loss dalam dB (model sederhana)."""
    return round(32.4 + 20 * (distance_km ** 0.5) + 0.1 * freq_mhz, 2)


def main() -> None:
    loss = calculate_path_loss(2.5, freq_mhz=1800.0)
    print(f"Hasil path loss : {loss} dB")
    print(f"Nama fungsi asli: {calculate_path_loss.__name__}")
    print(f"Docstring asli  : {calculate_path_loss.__doc__}")


if __name__ == "__main__":
    main()

