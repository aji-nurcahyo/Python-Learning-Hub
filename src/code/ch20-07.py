"""Contoh 20.7: Special Method __eq__, Kesetaraan (==) vs Identitas (is) & Hashability
Python Learning Hub - Level 2: Intermediate Python
"""

class NetworkHost:
    def __init__(self, mac_address: str, ip_address: str):
        self.mac_address = mac_address.upper()
        self.ip_address = ip_address

    def __repr__(self) -> str:
        return f"NetworkHost('{self.mac_address}', '{self.ip_address}')"

    def __eq__(self, other: object) -> bool:
        """Dua host dianggap sama nilainya jika memiliki MAC address yang identik."""
        if not isinstance(other, NetworkHost):
            return NotImplemented
        return self.mac_address == other.mac_address

    def __hash__(self) -> int:
        """Mengimplementasikan hash agar objek dapat dijadikan elemen set / key dictionary."""
        return hash(self.mac_address)

# Dua instance objek berbeda dengan data MAC yang sama
h1 = NetworkHost("AA:BB:CC:11:22:33", "192.168.1.10")
h2 = NetworkHost("aa:bb:cc:11:22:33", "192.168.1.99")
h3 = h1  # Referensi ke instance objek yang sama

print(f"h1: {h1}")
print(f"h2: {h2}")

# Perbandingan Kesetaraan Nilai (__eq__)
print("h1 == h2 (Kesetaraan data):", h1 == h2)  # True karena MAC sama
print("h1 is h2 (Identitas objek):", h1 is h2)  # False karena lokasi memori berbeda
print("h1 is h3 (Identitas objek):", h1 is h3)  # True karena merujuk instance yang sama

# Menguji keanggotaan dalam set karena __hash__ telah diimplementasikan
host_set = {h1, h2}
print(f"Jumlah elemen unik dalam set: {len(host_set)} (Deduplikasi otomatis berhasil)")
