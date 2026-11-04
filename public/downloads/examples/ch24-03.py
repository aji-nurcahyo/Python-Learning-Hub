"""Chapter 24 Example 03: Parameterized Validation Decorator
Python Learning Hub - Professional Python Engineering
"""

import functools
from typing import Any, Callable


def validate_range(min_val: float, max_val: float) -> Callable[..., Any]:
    """Decorator factory yang menerima batas minimum dan maksimum untuk parameter numerik."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(val: float, *args: Any, **kwargs: Any) -> Any:
            if not (min_val <= val <= max_val):
                raise ValueError(f"Nilai {val} di luar batas toleransi [{min_val}, {max_val}]")
            return func(val, *args, **kwargs)

        return wrapper

    return decorator


@validate_range(min_val=-120.0, max_val=-30.0)
def record_rssi(rssi_dbm: float) -> str:
    return f"Sinyal RSSI diterima: {rssi_dbm} dBm"


def main() -> None:
    print(record_rssi(-75.5))
    try:
        record_rssi(-15.0)
    except ValueError as err:
        print(f"Validasi ditolak: {err}")


if __name__ == "__main__":
    main()
