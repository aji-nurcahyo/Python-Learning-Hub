"""Contoh 18.8: Penerapan Modul logging untuk Audit Operasional Sistem
Python Learning Hub - Level 2: Intermediate
"""

import logging

# Konfigurasi logger standar dengan format pesan deterministik
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def pantau_koneksi_gateway(ip_gateway: str, status_ping: bool) -> None:
    """Mencatat aktivitas koneksi dengan berbagai tingkat keparahan log."""
    logging.debug(f"Mengirim paket uji ICMP ke {ip_gateway}")

    if status_ping:
        logging.info(f"Gateway {ip_gateway} terhubung dengan latensi 5 ms.")
    else:
        logging.warning(f"Gateway {ip_gateway} tidak merespons ping pertama.")
        logging.error(f"Koneksi fisik ke {ip_gateway} terputus!")

print("Audit Log Sistem Gateway:")
pantau_koneksi_gateway("192.168.1.1", status_ping=True)
pantau_koneksi_gateway("192.168.1.254", status_ping=False)

