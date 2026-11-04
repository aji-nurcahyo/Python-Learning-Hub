"""Contoh 13.1: Parameter Posisi, Kata Kunci, Default, dan Pembatas Sintaksis
Python Learning Hub - Level 2: Intermediate
"""

# 1. Parameter posisi, default, dan kata kunci
def kirim_notifikasi(pesan: str, tujuan: str = "Semua", prioritas: str = "NORMAL") -> str:
    return f"[{prioritas}] Kepada: {tujuan} -> Pesan: {pesan}"

# Pemanggilan positional vs keyword
print(kirim_notifikasi("Sistem menyala"))
print(kirim_notifikasi("Server overload", "Admin", "TINGGI"))
print(kirim_notifikasi("Pembaruan kuota", prioritas="RENDAH", tujuan="User_101"))

# 2. Positional-only (/) dan Keyword-only (*)
def konfigurasi_node(node_id: int, /, frekuensi_mhz: float, *, mode: str = "AUTO") -> str:
    """node_id wajib posisi, frekuensi_mhz bebas, mode wajib kata kunci."""
    return f"Node #{node_id} @ {frekuensi_mhz:.1f} MHz [Mode: {mode}]"

print("\nUji Positional-Only & Keyword-Only:")
print(konfigurasi_node(101, 2412.0, mode="MANUAL"))
print(konfigurasi_node(102, frekuensi_mhz=5180.0))
