"""Chapter 24 Example 07: Class-based Context Manager Protocol
Python Learning Hub - Professional Python Engineering
"""

from types import TracebackType


class NetworkSession:
    """Mengelola siklus hidup sesi koneksi soket telekomunikasi."""

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        self.is_connected = False

    def __enter__(self) -> "NetworkSession":
        self.is_connected = True
        print(f"[SESSION OPEN] Membuka kanal koneksi ke {self.endpoint}")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        self.is_connected = False
        print(f"[SESSION CLOSE] Menutup kanal koneksi dari {self.endpoint}")
        if exc_type is not None:
            print(f"[SESSION ERROR] Tertangkap exception: {exc_val}")
            return False  # Jangan menelan exception, biarkan propagate
        return True


def main() -> None:
    with NetworkSession("192.168.10.1:5000") as session:
        print(f"Status saat ini: Terhubung={session.is_connected}")
        print("Mengirim payload paket data...")

    print(f"Status setelah with block: Terhubung={session.is_connected}")


if __name__ == "__main__":
    main()

