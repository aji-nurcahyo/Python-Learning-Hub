"""Chapter 24 Example 04: Fibonacci & Infinite Sequence Generator
Python Learning Hub - Professional Python Engineering
"""

from collections.abc import Generator


def fibonacci_sequence() -> Generator[int, None, None]:
    """Generator tak berhingga yang menghasilkan deret Fibonacci secara lazy."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main() -> None:
    fib = fibonacci_sequence()
    first_10 = [next(fib) for _ in range(10)]
    print(f"10 Angka Pertama Fibonacci: {first_10}")

    # Mengambil nilai berikutnya dari generator yang sama
    print(f"Angka ke-11: {next(fib)}")
    print(f"Angka ke-12: {next(fib)}")


if __name__ == "__main__":
    main()

