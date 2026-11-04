# Chapter 11 — Modules & Basic Exceptions
> **Organisasi Berkas, Standard Library, Docstring & try/except**
*Level 1 · FOUNDATIONS · Beginner · 4 Jam Pembelajaran*

## Deskripsi Modul
Membuat modul mandiri (.py), impor fungsi, proteksi __name__ == "__main__", dokumentasi standar PEP 257 (docstrings), dan penanganan error dasar.

## Fokus Kompetensi
PCEP 4.4: Modul, namespaces, docstring, exception dasar

## Prasyarat
- Chapter 10

## Capaian Pembelajaran (Learning Objectives)
- [ ] Membuat modul buatan sendiri dan mengimpor fungsi spesifik tanpa polusi namespace
- [ ] Menulis docstring yang rapi dan informatif yang terbaca melalui fungsi help()
- [ ] Menggunakan pola if __name__ == "__main__": untuk pemisahan runnable demo dan modul impor
- [ ] Menangani ValueError dan ZeroDivisionError menggunakan blok try-except dasar

---

## Ringkasan Materi & Kode Utama
```python
# Ekstraksi Docstring Standar PEP 257
def konversi_c_ke_f(celsius):
    """Konversi suhu dari Celsius ke Fahrenheit.

    Args:
        celsius (float): Suhu dalam Celsius.
    Returns:
        float: Suhu dalam Fahrenheit.
    """
    return celsius * 9 / 5 + 32

print(konversi_c_ke_f.__doc__)
```
**Penjelasan:**
Docstring ditulis tepat di bawah header fungsi menggunakan triple quotes ("""). Atribut __doc__ atau fungsi help() dapat membacanya secara otomatis untuk dokumentasi interaktif.

