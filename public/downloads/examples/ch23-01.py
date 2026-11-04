"""Chapter 23 Example 01: Abstract Base Class (ABC) & @abstractmethod
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    """Interface dasar abstrak untuk semua perangkat jaringan."""

    def __init__(self, device_id: str, name: str) -> None:
        self.device_id = device_id
        self.name = name

    @abstractmethod
    def ping(self) -> bool:
        """Memeriksa apakah perangkat dapat dihubungi."""
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Mengembalikan status operasional perangkat."""
        pass


class Router(AbstractDevice):
    """Implementasi konkret untuk perangkat Router."""

    def ping(self) -> bool:
        return True

    def get_status(self) -> str:
        return f"Router [{self.device_id}] {self.name} aktif (routing table: OK)"


def main() -> None:
    router = Router("RTR-01", "Gateway Utama")
    print(f"Device ID : {router.device_id}")
    print(f"Ping OK   : {router.ping()}")
    print(f"Status    : {router.get_status()}")


if __name__ == "__main__":
    main()
