# Chapter 10 — Functions & Scope
> **Modularitas Kode, Parameter, Return & Ruang Lingkup**
*Level 1 · FOUNDATIONS · Beginner · 5 Jam Pembelajaran*

## Deskripsi Modul
Merancang fungsi reusable dengan def, argumen posisi & default, perbedaan fundamental print vs return, serta isolasi variabel lokal vs global (LEGB rule).

## Fokus Kompetensi
PCEP 4.3: Deklarasi fungsi, parameter, return, scope

## Prasyarat
- Chapter 08
- Chapter 09

## Capaian Pembelajaran (Learning Objectives)
- [ ] Mendeklarasikan fungsi dengan parameter wajib dan argumen nilai default
- [ ] Membedakan secara tegas mekanisme cetak layar (print) dan nilai balik pemrosesan (return)
- [ ] Menganalisis siklus hidup variabel lokal dan menghindari efek samping manipulasi variabel global

---

## Ringkasan Materi & Kode Utama
```python
# Perbedaan Nilai Balik (Return) dan Cetak Layar (Print)
def hitung_persegi(sisi):
    return sisi * sisi

hasil = hitung_persegi(4)
print(hasil + 8)  # Nilai return dapat diproses lebih lanjut!
```
**Penjelasan:**
Return mengembalikan data ke pemanggil fungsi agar dapat disimpan dalam variabel atau digunakan dalam ekspresi matematika lain. Print hanya mencetak teks ke layar dan mengembalikan None.

