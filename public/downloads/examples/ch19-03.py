"""Contoh 19.3: Sensor Telemetri Telekomunikasi Menggunakan Class & Instance Methods
Python Learning Hub - Level 2: Intermediate Python
"""

class Sensor:
    """Representasi sensor telemetri perangkat telekomunikasi."""

    def __init__(self, sensor_id: str, tipe: str, satuan: str, ambang_batas: float):
        self.sensor_id = sensor_id
        self.tipe = tipe
        self.satuan = satuan
        self.ambang_batas = ambang_batas
        self.nilai_terakhir: float = 0.0
        self.status: str = "OFFLINE"

    def update_pembacaan(self, nilai: float) -> str:
        """Memperbarui nilai pembacaan dan mengevaluasi status peringatan."""
        self.nilai_terakhir = float(nilai)
        if self.nilai_terakhir > self.ambang_batas:
            self.status = "ALERT"
        else:
            self.status = "NORMAL"
        return self.status

    def get_telemetri(self) -> str:
        return f"[{self.sensor_id}] {self.tipe}: {self.nilai_terakhir:.1f} {self.satuan} | Status: {self.status}"

# Membuat instance sensor suhu dan sensor daya
temp_sensor = Sensor("SENS-TH-01", "Suhu Rak Server", "°C", ambang_batas=45.0)
power_sensor = Sensor("SENS-PWR-02", "Daya Pemancar BTS", "Watt", ambang_batas=120.0)

temp_sensor.update_pembacaan(38.5)
power_sensor.update_pembacaan(135.2)

print(temp_sensor.get_telemetri())
print(power_sensor.get_telemetri())
