"""Contoh Praktikum Python Learning Hub: List, Tuple & Pengolahan Data Sensor."""

PENGUKURAN = [
    {'id': 'S01', 'lokasi': 'Gedung A', 'rsrp': -82},
    {'id': 'S02', 'lokasi': 'Gedung B', 'rsrp': -107},
    {'id': 'S03', 'lokasi': 'Gedung A', 'rsrp': -95},
    {'id': 'S04', 'lokasi': 'Gedung C', 'rsrp': -89},
    {'id': 'S05', 'lokasi': 'Gedung B', 'rsrp': -110},
    {'id': 'S06', 'lokasi': 'Gedung A', 'rsrp': -102},
    {'id': 'S07', 'lokasi': 'Gedung C', 'rsrp': -76},
    {'id': 'S08', 'lokasi': 'Gedung B', 'rsrp': -91},
]


def cari_sensor(data, id_sensor):
    """Cari sensor berdasarkan ID; kembalikan dict atau None."""
    for sensor in data:
        if sensor['id'] == id_sensor:
            return sensor
    return None


def filter_lemah(data, batas=-100):
    """Pilih sensor dengan RSRP di bawah nilai batas (dBm)."""
    return [sensor for sensor in data if sensor['rsrp'] < batas]


def urutkan_rsrp(data):
    """Urutkan sensor berdasarkan RSRP tertinggi ke terendah."""
    return sorted(data, key=lambda sensor: sensor['rsrp'], reverse=True)


def ringkasan(data):
    """Buat statistik sederhana RSRP; None untuk data kosong."""
    if not data:
        return None
    rsrp = [sensor['rsrp'] for sensor in data]
    return {'jumlah': len(rsrp), 'minimum': min(rsrp),
            'maksimum': max(rsrp), 'rata_rata': sum(rsrp) / len(rsrp)}


def selection_sort(angka):
    """Urutkan angka menaik dengan selection sort untuk demonstrasi."""
    hasil = angka.copy()
    for i in range(len(hasil)):
        indeks_min = i
        for j in range(i + 1, len(hasil)):
            if hasil[j] < hasil[indeks_min]:
                indeks_min = j
        hasil[i], hasil[indeks_min] = hasil[indeks_min], hasil[i]
    return hasil


if __name__ == '__main__':
    print('Data awal:', PENGUKURAN)
    print('Cari S03:', cari_sensor(PENGUKURAN, 'S03'))
    print('Cari S99:', cari_sensor(PENGUKURAN, 'S99'))
    print('Sinyal lemah:', filter_lemah(PENGUKURAN))
    print('Urutkan:', urutkan_rsrp(PENGUKURAN))
    print('Ringkasan:', ringkasan(PENGUKURAN))
    print('Selection sort:', selection_sort([5, 2, 9, 1]))
    print('Lokasi unik:', sorted({sensor['lokasi'] for sensor in PENGUKURAN}))
    assert cari_sensor(PENGUKURAN, 'S99') is None
    assert ringkasan([]) is None
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    print('Tes berhasil')
