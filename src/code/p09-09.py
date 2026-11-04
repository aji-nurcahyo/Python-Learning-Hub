def kategori_rsrp(rsrp):
    """Kategori ilustratif RSRP untuk latihan."""
    if rsrp >= -90:
        return "Baik"
    elif rsrp >= -105:
        return "Sedang"
    return "Buruk"

print(kategori_rsrp(-110))  # Buruk
