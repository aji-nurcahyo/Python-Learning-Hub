"""Contoh 20.6: Special Methods __str__ dan __repr__
Python Learning Hub - Level 2: Intermediate Python
"""

class DeviceSpec:
    def __init__(self, model: str, ram_gb: int, storage_gb: int):
        self.model = model
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

    def __repr__(self) -> str:
        """Representasi formal untuk developer dan debugging (reproducible)."""
        return f"DeviceSpec(model='{self.model}', ram_gb={self.ram_gb}, storage_gb={self.storage_gb})"

    def __str__(self) -> str:
        """Representasi ramah pengguna (user-friendly)."""
        return f"{self.model} [{self.ram_gb}GB RAM / {self.storage_gb}GB Storage]"

spec = DeviceSpec("Cisco-Catalyst-9300", 16, 256)

# __str__ dipanggil oleh print() dan str()
print("Hasil str()  :", str(spec))
print("Hasil print():", spec)

# __repr__ dipanggil oleh repr() dan ketika objek berada di dalam list
print("Hasil repr() :", repr(spec))

daftar = [spec, DeviceSpec("MikroTik-CCR2004", 4, 128)]
print("List repr    :", daftar)
