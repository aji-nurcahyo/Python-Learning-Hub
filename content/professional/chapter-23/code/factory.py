"""Pabrik Pembuatan Perangkat (Chapter 23)
Python Learning Hub - Professional Python Engineering
"""

from typing import Type
from pattern_models import AbstractDevice, DeviceMetadata, RadioNode, SwitchNode


class DeviceFactory:
    """Factory terpusat untuk instansiasi tipe perangkat jaringan."""

    _registry: dict[str, Type[AbstractDevice]] = {
        "radio": RadioNode,
        "switch": SwitchNode,
    }

    @classmethod
    def register_type(cls, name: str, device_cls: Type[AbstractDevice]) -> None:
        cls._registry[name.lower()] = device_cls

    @classmethod
    def create(
        cls,
        device_type: str,
        device_id: str,
        model: str,
        firmware: str,
        bandwidth_mbps: float,
    ) -> AbstractDevice:
        target_cls = cls._registry.get(device_type.lower())
        if not target_cls:
            valid = list(cls._registry.keys())
            raise ValueError(f"Tipe perangkat '{device_type}' tidak terdaftar. Pilihan: {valid}")

        metadata = DeviceMetadata(
            device_id=device_id,
            model=model,
            firmware_version=firmware,
            max_bandwidth_mbps=bandwidth_mbps,
        )
        return target_cls(metadata)
