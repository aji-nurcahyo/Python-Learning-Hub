"""Chapter 25 Example 08: PEP 8 Standards & Code Quality Patterns
Python Learning Hub - Professional Python Engineering
"""

from dataclasses import dataclass

MAX_RETRIES: int = 3  # Konstanta global menggunakan UPPER_SNAKE_CASE


@dataclass(frozen=True)
class ServiceEndpoint:
    """Kelas konfigurasi sesuai standar PEP 8 (PascalCase untuk nama class)."""

    name: str
    host: str
    port: int

    def formatted_address(self) -> str:
        """Method menggunakan snake_case dengan tipe kembalian jelas."""
        return f"{self.name} -> {self.host}:{self.port}"


def format_audit_report(endpoints: list[ServiceEndpoint]) -> list[str]:
    """Menghasilkan laporan audit rapi tanpa mutable default arguments."""
    return [ep.formatted_address() for ep in endpoints]


def main() -> None:
    services = [
        ServiceEndpoint("NTP", "192.168.1.5", 123),
        ServiceEndpoint("SNMP", "192.168.1.10", 161),
    ]
    report = format_audit_report(services)
    print("Daftar Layanan Terstandar PEP 8:")
    for line in report:
        print(f" * {line}")


if __name__ == "__main__":
    main()
