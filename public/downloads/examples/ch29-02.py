"""Chapter 29 Example 02: Separating Business Logic from CLI Logic
Python Learning Hub - Professional Python Engineering
"""

import sys


# === DOMAIN & BUSINESS LOGIC (Nir-dependensi CLI / UI) ===
class BandwidthCalculator:
    """Logika murni kalkulasi kapasitas jaringan yang mudah diuji tanpa sys.argv."""

    @staticmethod
    def calculate_utilization(used_mbps: float, capacity_mbps: float) -> float:
        if capacity_mbps <= 0:
            raise ValueError("Kapasitas total harus bernilai lebih besar dari 0 Mbps.")
        if used_mbps < 0:
            raise ValueError("Penggunaan bandwidth tidak boleh bernilai negatif.")
        return round((used_mbps / capacity_mbps) * 100.0, 2)


# === CLI CONTROLLER LAYER (Menangani parsing argumen dan format output) ===
class BandwidthCliController:
    def __init__(self, calculator: BandwidthCalculator) -> None:
        self.calculator = calculator

    def execute(self, raw_args: list[str]) -> int:
        if len(raw_args) < 2:
            print("Penggunaan: bandwidth-cli <used_mbps> <capacity_mbps>", file=sys.stderr)
            return 1

        try:
            used = float(raw_args[0])
            capacity = float(raw_args[1])
            percentage = self.calculator.calculate_utilization(used, capacity)
            print(f"[HASIL CLI] Utilisasi Link: {percentage}% ({used}/{capacity} Mbps)")
            return 0
        except ValueError as err:
            print(f"[ERROR CLI] Input tidak valid: {err}", file=sys.stderr)
            return 2


def main() -> None:
    calc = BandwidthCalculator()
    cli = BandwidthCliController(calculator=calc)

    print("Simulasi Pemanggilan CLI dengan Argumen Valid:")
    exit_code_1 = cli.execute(["450", "1000"])
    print(f" -> Exit code: {exit_code_1}")

    print("\nSimulasi Pemanggilan CLI dengan Input Kapasitas 0:")
    exit_code_2 = cli.execute(["100", "0"])
    print(f" -> Exit code: {exit_code_2}")


if __name__ == "__main__":
    main()
