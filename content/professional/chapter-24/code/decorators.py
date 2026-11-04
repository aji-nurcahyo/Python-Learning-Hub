"""Koleksi Decorator untuk Monitoring & Validasi (Chapter 24)
Python Learning Hub - Professional Python Engineering
"""

import functools
import time
from typing import Any, Callable


def audit_log(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator pencatat audit pemanggilan fungsi."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        return result

    return wrapper


def time_tracker(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator pengukur durasi eksekusi dengan time.perf_counter()."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        # Menyimpan metrik durasi jika hasil berupa dictionary
        if isinstance(result, dict):
            result["_elapsed_sec"] = round(elapsed, 6)
        return result

    return wrapper


def validate_record_schema(required_keys: list[str]) -> Callable[..., Any]:
    """Decorator factory untuk memvalidasi kelengkapan kunci dictionary."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(record: dict[str, Any], *args: Any, **kwargs: Any) -> Any:
            for k in required_keys:
                if k not in record:
                    raise KeyError(f"Record kehilangan kunci wajib: '{k}'")
            return func(record, *args, **kwargs)

        return wrapper

    return decorator

