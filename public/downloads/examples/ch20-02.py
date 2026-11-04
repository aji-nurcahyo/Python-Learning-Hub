"""Contoh 20.2: Method Overriding dan Pemanggilan super()
Python Learning Hub - Level 2: Intermediate Python
"""

class TelemetrySensor:
    def __init__(self, sensor_id: str, lokasi: str):
        self.sensor_id = sensor_id
        self.lokasi = lokasi

    def baca_telemetri(self, raw_value: float) -> str:
        """Method dasar yang akan di-override oleh class turunan."""
        return f"Sensor {self.sensor_id} ({self.lokasi}): raw={raw_value}"

class TemperatureSensor(TelemetrySensor):
    def __init__(self, sensor_id: str, lokasi: str, satuan: str = "°C"):
        super().__init__(sensor_id, lokasi)
        self.satuan = satuan

    def baca_telemetri(self, raw_value: float) -> str:
        # Override perilaku dasar dan menyematkan evaluasi termal spesifik
        status = "BAHAYA" if raw_value > 50.0 else "NORMAL"
        return f"[Thermal {self.sensor_id}] {self.lokasi} -> {raw_value:.1f}{self.satuan} ({status})"

class OpticalPowerSensor(TelemetrySensor):
    def __init__(self, sensor_id: str, lokasi: str, lambda_nm: int = 1550):
        super().__init__(sensor_id, lokasi)
        self.lambda_nm = lambda_nm

    def baca_telemetri(self, raw_value: float) -> str:
        # Override dengan evaluasi redaman optik fiber
        kualitas = "EXCELLENT" if raw_value >= -20.0 else "DEGRADED"
        return f"[Optik {self.sensor_id}] λ={self.lambda_nm}nm -> {raw_value:.2f} dBm ({kualitas})"

s_temp = TemperatureSensor("TH-01", "Rack A", "°C")
s_opt = OpticalPowerSensor("FIBER-02", "ODC Box 3", lambda_nm=1310)

print(s_temp.baca_telemetri(54.2))
print(s_opt.baca_telemetri(-18.45))
