"""Contoh praktikum Pengantar Komputasi, pertemuan 9."""

def celsius_ke_fahrenheit(celsius):
    """Ubah suhu Celsius menjadi Fahrenheit."""
    return celsius * 9 / 5 + 32


def rata_rata(data):
    """Hitung rata-rata angka; kembalikan None bila data kosong."""
    if not data:
        return None
    return sum(data) / len(data)


def nilai_tertinggi(data):
    """Ambil nilai maksimum; kembalikan None bila data kosong."""
    if not data:
        return None
    return max(data)


def kategori_rsrp(rsrp):
    """Klasifikasikan RSRP menggunakan batas ilustrasi pembelajaran."""
    if rsrp >= -90:
        return 'Baik'
    if rsrp >= -105:
        return 'Sedang'
    return 'Buruk'


if __name__ == '__main__':
    rsrp = [-78, -96, -108, -85]
    print('Konversi 25 C:', celsius_ke_fahrenheit(25), 'F')
    print('Rata-rata:', rata_rata(rsrp))
    print('RSRP tertinggi:', nilai_tertinggi(rsrp))
    print('Kategori:', [kategori_rsrp(x) for x in rsrp])
    assert celsius_ke_fahrenheit(0) == 32
    assert rata_rata([]) is None
    assert nilai_tertinggi([-80, -100]) == -80
    assert kategori_rsrp(-110) == 'Buruk'
    print('Tes berhasil')
