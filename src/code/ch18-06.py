"""Contoh 18.6: Exception Chaining dengan Sintaksis raise ... from ...
Python Learning Hub - Level 2: Intermediate
"""

class GatewayConfigurationError(Exception):
    """Exception tingkat tinggi saat inisialisasi konfigurasi gateway gagal."""
    pass


def muat_port_gateway(konfigurasi: dict) -> int:
    """Membaca nomor port gateway dengan membungkus KeyError ke GatewayConfigurationError."""
    try:
        return int(konfigurasi["port_jaringan"])
    except KeyError as err_asli:
        # Menautkan exception asli ke exception domain tingkat tinggi (chaining)
        raise GatewayConfigurationError("Kunci konfigurasi 'port_jaringan' tidak ditemukan.") from err_asli


config_rusak = {"nama_node": "GW-UTAMA"}

print("Mendemonstrasikan Exception Chaining:")
try:
    port = muat_port_gateway(config_rusak)
except GatewayConfigurationError as err:
    print(f"Exception Utama Tertangkap : {err}")
    print(f"Penyebab Asli (Chained)    : {type(err.__cause__).__name__} -> {err.__cause__}")

