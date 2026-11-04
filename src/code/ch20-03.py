"""Contoh 20.3: Polimorfisme (Pemrosesan Koleksi Objek Heterogen)
Python Learning Hub - Level 2: Intermediate Python
"""

class DeviceNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def jalankan_diagnostik(self) -> dict:
        raise NotImplementedError("Subclass wajib mengimplementasikan method jalankan_diagnostik!")

class BTSNode(DeviceNode):
    def jalankan_diagnostik(self) -> dict:
        return {"id": self.node_id, "tipe": "BTS Seluler", "parameter": "VSWR=1.15, Pwr=43dBm", "status": "HEALTHY"}

class MicrowaveLinkNode(DeviceNode):
    def jalankan_diagnostik(self) -> dict:
        return {"id": self.node_id, "tipe": "Microwave Link", "parameter": "FadeMargin=24dB, BER=1e-9", "status": "OPTIMAL"}

class FiberSwitchNode(DeviceNode):
    def jalankan_diagnostik(self) -> dict:
        return {"id": self.node_id, "tipe": "Switch Fiber", "parameter": "PortUp=24/24, SFP_Tx=Good", "status": "STABLE"}

# Koleksi heterogen berisi berbagai jenis subclass DeviceNode
jaringan: list[DeviceNode] = [
    BTSNode("BTS-BANDAR-LAMPUNG-01"),
    MicrowaveLinkNode("MW-BAKAUHENI-02"),
    FiberSwitchNode("SW-ITERA-CORE-03"),
    BTSNode("BTS-KALIANDA-04"),
]

print("=== Eksekusi Polimorfik Diagnostik Jaringan ===")
for node in jaringan:
    # Memanggil method yang sama secara seragam pada objek yang berbeda kelas
    hasil = node.jalankan_diagnostik()
    print(f"[{hasil['tipe']:<14}] Node {hasil['id']:<23} | {hasil['parameter']} => {hasil['status']}")
