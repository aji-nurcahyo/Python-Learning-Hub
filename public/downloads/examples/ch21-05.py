"""Contoh 21.5: Pola Test Fixture (Setup, Execution & Teardown)
Python Learning Hub - Level 2: Intermediate Python
"""

# Fixture adalah mekanisme untuk menyiapkan data awal (state) yang konsisten
# sebelum pengujian dijalankan, dan membersihkannya setelah selesai.

class DeviceRegistry:
    def __init__(self):
        self.devices = []

    def register(self, dev_id: str, ip: str) -> None:
        self.devices.append({"id": dev_id, "ip": ip})

    def count(self) -> int:
        return len(self.devices)

def fixture_clean_registry():
    """Generator fixture yang meniru perilaku @pytest.fixture."""
    print("  [Setup Fixture] Menginisialisasi registry baru yang bersih...")
    reg = DeviceRegistry()
    reg.register("RTR-01", "10.0.0.1")
    reg.register("SW-01", "10.0.0.2")
    yield reg
    print("  [Teardown Fixture] Membersihkan alokasi memori registry...")

print("=== Mensimulasikan Siklus Hidup Test Fixture ===")
fixture_gen = fixture_clean_registry()
test_reg = next(fixture_gen)

print(f"  [Eksekusi Test] Menjalankan assertion pada registry ({test_reg.count()} perangkat)...")
assert test_reg.count() == 2, "Jumlah perangkat awal harus 2"
test_reg.register("AP-01", "10.0.0.3")
assert test_reg.count() == 3, "Setelah registrasi, jumlah harus 3"
print("  [Eksekusi Test] Assertion berhasil diverifikasi!")

# Menyelesaikan tahap teardown
try:
    next(fixture_gen)
except StopIteration:
    pass

print("Siklus hidup fixture pengujian selesai.")
