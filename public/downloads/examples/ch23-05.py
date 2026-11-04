"""Chapter 23 Example 05: Factory Pattern
Python Learning Hub - Professional Python Engineering
"""

from abc import ABC, abstractmethod


class AbstractDevice(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass


class RadioDevice(AbstractDevice):
    def describe(self) -> str:
        return "Perangkat Radio BTS (Frekuensi RF)"


class OpticalDevice(AbstractDevice):
    def describe(self) -> str:
        return "Perangkat Optik DWDM (Laser Fiber)"


class DeviceFactory:
    """Factory terpusat untuk instansiasi tipe perangkat berdasarkan string identifier."""

    _registry: dict[str, type[AbstractDevice]] = {
        "radio": RadioDevice,
        "optical": OpticalDevice,
    }

    @classmethod
    def create(cls, device_type: str) -> AbstractDevice:
        target_cls = cls._registry.get(device_type.lower())
        if not target_cls:
            valid = list(cls._registry.keys())
            raise ValueError(f"Tipe '{device_type}' tidak valid. Pilihan: {valid}")
        return target_cls()


def main() -> None:
    d1 = DeviceFactory.create("radio")
    d2 = DeviceFactory.create("optical")
    print(f"Device 1: {d1.describe()}")
    print(f"Device 2: {d2.describe()}")


if __name__ == "__main__":
    main()
