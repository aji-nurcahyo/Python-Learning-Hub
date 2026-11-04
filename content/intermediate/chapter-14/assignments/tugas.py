"""Starter Template: Dataset Transformation Toolkit
Tugas Praktik Chapter 14: Comprehensions & Iterators — Python Learning Hub
Pengembang: Aji Pamungkas Tri Nurcahyo — Institut Teknologi Sumatera

Instruksi:
Gantikan blok berlabel TODO dengan ekspresi comprehension atau generator yang sesuai.
Hindari penggunaan loop for manual imperatif jika dapat diselesaikan dengan satu baris ekspresif.
"""

from typing import Any, Generator


# ==============================================================================
# BAGIAN 1: LIST COMPREHENSION & TRANSFORMASI
# ==============================================================================

def saring_dan_skala(
    data_log: list[dict[str, Any]],
    ambang_min: float = 30.0,
    faktor_gain: float = 1.2
) -> list[dict[str, Any]]:
    """Memfilter perangkat dengan daya >= ambang_min dan mengalikan daya dengan faktor_gain."""
    # TODO: Gunakan list comprehension dengan klausa if untuk filtering
    return [
        {**d, "daya": round(float(d["daya"]) * faktor_gain, 2)}
        for d in data_log
        if float(d.get("daya", 0.0)) >= ambang_min
    ]


# ==============================================================================
# BAGIAN 2: DICT & SET COMPREHENSIONS
# ==============================================================================

def buat_indeks_perangkat(daftar_perangkat: list[dict[str, Any]]) -> dict[str, str]:
    """Membangun kamus lookup: IP -> Nama Perangkat."""
    # TODO: Gunakan dict comprehension
    return {p["ip"]: p["nama"] for p in daftar_perangkat if "ip" in p and "nama" in p}


def isolasi_zona_aktif(daftar_perangkat: list[dict[str, Any]]) -> set[str]:
    """Mengekstrak kumpulan nama zona unik yang telah dinormalisasi huruf besar-kecilnya."""
    # TODO: Gunakan set comprehension
    return {p["zona"].strip().title() for p in daftar_perangkat if "zona" in p}


# ==============================================================================
# BAGIAN 3: NESTED COMPREHENSION & GENERATOR EXPRESSION
# ==============================================================================

def ratakan_topologi_matriks(grid_matriks: list[list[Any]]) -> list[Any]:
    """Meratakan matriks 2D menjadi list 1D menggunakan nested comprehension."""
    # TODO: Gunakan nested list comprehension [item for baris in ... for item in ...]
    return [item for baris in grid_matriks for item in baris]


def aliran_daya_generator(
    aliran_data: list[float],
    ambang: float = 20.0
) -> Generator[float, None, None]:
    """Generator expression: Evaluasi lazy untuk penghematan memori."""
    # TODO: Gunakan generator expression dengan tanda kurung (expr for ... in ...)
    return (round(x * 1.5, 2) for x in aliran_data if x >= ambang)


def main() -> None:
    sampel_log = [
        {"id": "N1", "nama": "Router-Pusat", "ip": "10.0.0.1", "zona": "  inti ", "daya": 48.0},
        {"id": "N2", "nama": "Switch-Utara", "ip": "10.0.0.2", "zona": "akses", "daya": 88.0},
        {"id": "N3", "nama": "AP-Labtek",   "ip": "10.0.0.3", "zona": "Akses", "daya": 15.0},
        {"id": "N4", "nama": "Gateway-IoT", "ip": "10.0.0.4", "zona": "DISTRIBUSI", "daya": 62.5},
    ]

    print("1. Hasil Filter & Gain (List Comprehension):")
    hasil_filter = saring_dan_skala(sampel_log, ambang_min=30.0)
    for h in hasil_filter:
        print(f"   - {h['id']} ({h['nama']}): {h['daya']} mW")

    print("\n2. Peta Indeks Asosiatif (Dict Comprehension):")
    peta_ip = buat_indeks_perangkat(sampel_log)
    for ip, host in peta_ip.items():
        print(f"   {ip} -> {host}")

    print("\n3. Zona Unik (Set Comprehension):")
    zona = isolasi_zona_aktif(sampel_log)
    print(f"   Zona Terdeteksi: {zona}")

    print("\n4. Perataan Matriks 2D (Nested Comprehension):")
    matriks = [[10, 20], [30, 40], [50, 60]]
    print(f"   Rata: {ratakan_topologi_matriks(matriks)}")

    print("\n5. Aliran Generator Lazy:")
    gen = aliran_daya_generator([10.0, 25.0, 50.0, 15.0, 80.0], ambang=20.0)
    print(f"   Tiga item pertama: {[next(gen), next(gen), next(gen)]}")


if __name__ == "__main__":
    main()
