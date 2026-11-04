"""Contoh 22.4: Operasi CRUD, Pencarian & Pengurutan Inventaris Capstone
Python Learning Hub - Level 2: Intermediate Capstone Project
"""

class DeviceItem:
    def __init__(self, dev_id: str, name: str, category: str, price: float):
        self.dev_id = dev_id
        self.name = name
        self.category = category
        self.price = price

class InventoryRepo:
    def __init__(self):
        self._items: dict[str, DeviceItem] = {}

    def create(self, item: DeviceItem) -> None:
        if item.dev_id in self._items:
            raise KeyError(f"ID '{item.dev_id}' sudah terdaftar!")
        self._items[item.dev_id] = item

    def read(self, dev_id: str) -> DeviceItem:
        if dev_id not in self._items:
            raise KeyError(f"Perangkat '{dev_id}' tidak ditemukan!")
        return self._items[dev_id]

    def update_price(self, dev_id: str, new_price: float) -> None:
        item = self.read(dev_id)
        item.price = new_price

    def delete(self, dev_id: str) -> None:
        self.read(dev_id)
        del self._items[dev_id]

    def search_by_name(self, keyword: str) -> list[DeviceItem]:
        kw = keyword.lower()
        return [item for item in self._items.values() if kw in item.name.lower()]

    def sort_by_price(self, descending: bool = False) -> list[DeviceItem]:
        return sorted(self._items.values(), key=lambda x: x.price, reverse=descending)

repo = InventoryRepo()
repo.create(DeviceItem("D1", "Cisco Switch 24P", "Network", 7500000.0))
repo.create(DeviceItem("D2", "HP ProLiant Server", "Server", 55000000.0))
repo.create(DeviceItem("D3", "Ubiquiti AP WiFi-6", "Wireless", 2800000.0))

print("=== Pengurutan Berdasarkan Harga (Termurah ke Termahal) ===")
for d in repo.sort_by_price():
    print(f"- {d.dev_id}: {d.name:<22} (Rp {d.price:,.0f})")

# Update harga
repo.update_price("D3", 3100000.0)
print(f"\nHarga D3 setelah pembaruan: Rp {repo.read('D3').price:,.0f}")

# Pencarian
pencarian = repo.search_by_name("Switch")
print(f"Hasil pencarian 'Switch': Ditemukan {len(pencarian)} perangkat ({pencarian[0].name})")
