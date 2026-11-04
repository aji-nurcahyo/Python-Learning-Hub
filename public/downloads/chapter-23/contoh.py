"""Chapter 23: Mini Project Demonstrator
Extensible Device Management System
Python Learning Hub - Professional Python Engineering
"""

import sys
from pathlib import Path

# Memastikan direktori saat ini ada di sys.path
sys.path.insert(0, str(Path(__file__).parent))

from pattern_models import DeviceMetadata, RadioNode, SwitchNode
from strategies import StandardDiagnostic, DeepDiagnostic
from factory import DeviceFactory
from cluster_manager import DeviceClusterManager


def run_demonstration() -> None:
    print("=" * 65)
    print("DEMO: EXTENSIBLE DEVICE MANAGEMENT SYSTEM (CHAPTER 23)")
    print("=" * 65)

    # 1. Membuat perangkat via DeviceFactory
    radio = DeviceFactory.create(
        device_type="radio",
        device_id="BTS-SMG-01",
        model="Ericsson 6601",
        firmware="v4.2.1",
        bandwidth_mbps=1000.0,
    )
    switch = DeviceFactory.create(
        device_type="switch",
        device_id="SW-CORE-01",
        model="Cisco Catalyst 9300",
        firmware="17.9.4",
        bandwidth_mbps=10000.0,
    )

    radio.is_online = True
    switch.is_online = True

    # 2. Mengelola perangkat dalam klaster (Komposisi & Injeksi Dependensi)
    manager = DeviceClusterManager(
        cluster_name="Klaster Wilayah Jawa Tengah",
        diagnostic_strategy=StandardDiagnostic(),
    )
    manager.add_device(radio)
    manager.add_device(switch)

    print("\n--- [Laporan 1: Strategi Standar] ---")
    for rep in manager.run_cluster_diagnostics():
        print(f" -> {rep}")

    # Mengubah strategi secara dinamis (Strategy Pattern)
    manager.diagnostic_strategy = DeepDiagnostic()

    print("\n--- [Laporan 2: Strategi Audit Mendalam] ---")
    for rep in manager.run_cluster_diagnostics():
        print(f" -> {rep}")

    # Uji coba transmisi paket
    print("\n--- [Uji Transmisi Paket] ---")
    print(f"Radio transmit 1400B : {radio.transmit_packet(1400)}")
    print(f"Radio transmit 2000B : {radio.transmit_packet(2000)} (melebihi MTU 1500)")
    print(f"Switch transmit 8000B: {switch.transmit_packet(8000)} (Jumbo Frame)")


if __name__ == "__main__":
    run_demonstration()
