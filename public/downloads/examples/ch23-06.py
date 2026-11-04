"""Chapter 23 Example 06: Strategy Pattern
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod


class EncodingStrategy(ABC):
    """Antarmuka strategi encoding payload data."""

    @abstractmethod
    def encode(self, data: str) -> str:
        pass


class PlainStrategy(EncodingStrategy):
    def encode(self, data: str) -> str:
        return f"PLAIN:{data}"


class HexStrategy(EncodingStrategy):
    def encode(self, data: str) -> str:
        return f"HEX:{data.encode('utf-8').hex()}"


class PayloadTransmitter:
    """Konteks yang menggunakan EncodingStrategy yang dapat diganti secara dinamis."""

    def __init__(self, strategy: EncodingStrategy) -> None:
        self.strategy = strategy

    def send(self, message: str) -> str:
        encoded = self.strategy.encode(message)
        return f"Mengirim -> {encoded}"


def main() -> None:
    transmitter = PayloadTransmitter(PlainStrategy())
    print(transmitter.send("STATUS_OK"))

    transmitter.strategy = HexStrategy()
    print(transmitter.send("STATUS_OK"))


if __name__ == "__main__":
    main()

