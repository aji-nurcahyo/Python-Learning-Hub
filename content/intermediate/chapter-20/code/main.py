"""Main Runner: Eksekusi Multi-Device Management System.
Python Learning Hub - Chapter 20: Object-Oriented Programming II
"""

from models import RouterDevice, SwitchDevice, SensorDevice
from manager import MultiDeviceManager

def main():
    manager = MultiDeviceManager("NOC Gedung Lab Telekomunikasi ITERA")

    # Instansiasi berbagai macam class turunan Device
    r1 = RouterDevice("RT-01", "Core-Router-BGP", "10.0.0.1", 180.0, 40.0, "BGP/MPLS")
    s1 = SwitchDevice("SW-01", "Distribution-Switch-1", "10.0.1.1", 75.0, 48, poe_enabled=True)
    s2 = SwitchDevice("SW-02", "Access-Switch-Lt2", "10.0.2.1", 45.0, 24, poe_enabled=False)
    t1 = SensorDevice("SN-01", "Rack-Thermal-Sensor", "10.0.99.1", 12.0, "Temperature", 38.4, "°C")

    for dev in [r1, s1, s2, t1]:
        manager.register_device(dev)

    # Eksekusi polimorfik
    manager.generate_report()

    # Uji special methods
    print("\n--- Pengujian Special Methods (__str__, __repr__, __eq__) ---")
    print("str(r1)  :", str(r1))
    print("repr(r1) :", repr(r1))

    # Objek duplikat identitas tapi lokasi memori beda
    r_clone = RouterDevice("RT-01", "Different-Name", "10.0.0.99", 200.0, 10.0, "Static")
    print("r1 == r_clone (Equality data) :", r1 == r_clone)
    print("r1 is r_clone (Object identity):", r1 is r_clone)

if __name__ == "__main__":
    main()
