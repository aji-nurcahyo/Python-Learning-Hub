import time
from typing import Callable, TypeVar

T = TypeVar("T")


def run_with_backoff(
    operation: Callable[[], T],
    max_attempts: int = 4,
    base_delay: float = 0.5,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> T:
    last_exc: Exception | None = None
    for attempt in range(max_attempts):
        try:
            return operation()
        except Exception as exc:
            last_exc = exc
            if attempt < max_attempts - 1:
                delay = base_delay * (2 ** attempt)
                sleep_fn(delay)
    assert last_exc is not None
    raise last_exc


if __name__ == "__main__":
    delays_recorded: list[float] = []
    state = {"calls": 0}

    def unstable_task() -> str:
        state["calls"] += 1
        if state["calls"] < 3:
            raise ConnectionError("Timeout sementara ke gateway")
        return "DATA_TERUNDUH"

    result = run_with_backoff(
        unstable_task,
        max_attempts=4,
        base_delay=0.5,
        sleep_fn=delays_recorded.append,
    )
    print("Hasil operasi   :", result)
    print("Total panggilan :", state["calls"])
    print("Jeda backoff (s):", delays_recorded)
