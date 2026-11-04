"""Chapter 25 Example 01: Function Type Hints with Modern Union Syntax
Python Learning Hub - Professional Python Engineering
"""


def calculate_snr(signal_power: float, noise_power: float) -> float:
    """Menghitung SNR (Signal to Noise Ratio) dalam rasio linear."""
    if noise_power <= 0:
        raise ValueError("Noise power harus lebih besar dari nol")
    return round(signal_power / noise_power, 3)


def format_frequency(mhz: int | float, precision: int = 2) -> str:
    """Format frekuensi RF dengan union type (int | float) modern Python 3.10+."""
    return f"{mhz:.{precision}f} MHz"


def main() -> None:
    snr = calculate_snr(100.5, 2.1)
    print(f"SNR Linear : {snr}")
    print(f"Freq (int) : {format_frequency(1800)}")
    print(f"Freq (flt) : {format_frequency(2145.75, precision=1)}")


if __name__ == "__main__":
    main()

