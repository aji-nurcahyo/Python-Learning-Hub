# Chapter 09 — Dictionaries & Sets
> **Struktur Data Berbasis Hash: Key-Value & Himpunan Unik**
*Level 1 · FOUNDATIONS · Beginner · 4 Jam Pembelajaran*

## Deskripsi Modul
Menyimpan data asosiatif dengan key-value pairs pada dictionary, pencarian O(1), penghapusan duplikasi dan operasi himpunan matematika pada set.

## Fokus Kompetensi
PCEP 4.2: Mapping types dan Set operations

## Prasyarat
- Chapter 08

## Capaian Pembelajaran (Learning Objectives)
- [ ] Membuat dan memanipulasi dictionary dengan method get(), items(), keys(), dan values()
- [ ] Menggunakan set untuk deduplikasi data seketika dan operasi union, intersection, difference
- [ ] Memilih struktur data yang tepat untuk kebutuhan query data tabular dan sensor

---

## Ringkasan Materi & Kode Utama
```python
# Struktur Data Dictionary & Hash Key-Value
sensor = {"id": "S01", "lokasi": "Gedung A", "rsrp": -80}
print(sensor["id"])
print(sensor.get("status", "tidak tersedia"))
print(sensor.items())
```
**Penjelasan:**
Dictionary menyimpan data berpasangan key-value dengan kompleksitas pencarian O(1). Metode get() mencegah timbulnya KeyError saat kunci tidak ditemukan.

