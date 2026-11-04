"""Contoh 13.3: Jebakan Mutable Default Argument & Solusi Idiomatis None
Python Learning Hub - Level 2: Intermediate
"""

# PERILAKU KELIRU: Menggunakan objek mutable (list) sebagai nilai default
def tambah_log_keliru(pesan: str, riwayat: list[str] = []) -> list[str]:
    riwayat.append(pesan)
    return riwayat

# Setiap pemanggilan berbagi objek list yang SAMA di memori fungsi!
print("--- Perilaku Bermasalah (Mutable Default) ---")
print("Panggilan 1:", tambah_log_keliru("Error koneksi 404"))
print("Panggilan 2:", tambah_log_keliru("Timeout gateway 504"))  # Riwayat lama terbawa!

# PERILAKU BENAR: Gunakan None sebagai sentinel default
def tambah_log_benar(pesan: str, riwayat: list[str] | None = None) -> list[str]:
    if riwayat is None:
        riwayat = []  # List baru dibuat setiap pemanggilan mandiri
    riwayat.append(pesan)
    return riwayat

print("\n--- Perilaku Benar (Sentinel None) ---")
print("Panggilan 1:", tambah_log_benar("Error koneksi 404"))
print("Panggilan 2:", tambah_log_benar("Timeout gateway 504"))  # Bersih dan independen!
log_kustom = ["Sistem mulai"]
print("Panggilan dengan list eksternal:", tambah_log_benar("Shutdown terencana", log_kustom))

