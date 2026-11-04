# Chapter 18: Exception Handling & Debugging

Selamat datang di **Chapter 18: Exception Handling & Debugging**. Menulis kode yang berjalan sukses pada skenario normal (*happy path*) hanyalah separuh dari tugas seorang insinyur perangkat lunak. Separuh lainnya—yang sering kali paling krusial—adalah memastikan program tetap tangguh, aman, dan informatif ketika berhadapan dengan situasi abnormal: berkas yang tiba-tiba terhapus, koneksi jaringan terputus, atau masukan data yang cacat.

---

## 1. Taksonomi Kesalahan: Syntax, Runtime, dan Logical Errors

Sebelum dapat menangani kesalahan secara efektif, kita harus membedakan tiga kategori utama masalah dalam program Python:

### A. Kesalahan Sintaksis (*Syntax Errors*)
Terjadi ketika kode melanggar aturan tata bahasa Python (misalnya tanda kurung tidak berpasangan atau titik dua `:` yang terlupa).
- **Waktu Terdeteksi:** Pada fase penguraian (*parsing/compile-time*) sebelum interpreter menjalankan satu baris kode pun.
- **Solusi:** Memperbaiki teks kode sumber sesuai aturan bahasa.

### B. Kesalahan Waktu Eksekusi (*Runtime Exceptions*)
Terjadi saat sintaksis program sudah benar, namun komputer diperintahkan untuk melakukan operasi yang secara matematis atau operasional tidak sah (misalnya membagi angka dengan nol, mengakses indeks `list` yang melampaui batas, atau membaca file yang tidak ada).
- **Waktu Terdeteksi:** Saat program sedang berjalan (*runtime*). Jika tidak ditangani, Python akan menghentikan eksekusi secara paksa dan mencetak *traceback*.
- **Solusi:** Ditangani secara elegan menggunakan mekanisme `try-except`.

### C. Kesalahan Logika (*Logical Errors / Bugs*)
Program berjalan lancar dari awal hingga akhir tanpa memicu exception apa pun, tetapi menghasilkan keluaran yang keliru (misalnya menghitung luas segitiga dengan rumus persegi).
- **Solusi:** Diidentifikasi melalui pengujian unit (*unit testing*), penelusuran *traceback*, dan *debugging* sistematis.

---

## 2. Hirarki Built-in Exception Python

Seluruh exception di Python adalah kelas (*class*) yang tersusun dalam pohon hierarki warisan (*inheritance tree*):

```text
BaseException
 ├── SystemExit                  # Pemanggilan sys.exit()
 ├── KeyboardInterrupt           # Pengguna menekan Ctrl+C di terminal
 └── Exception                   # INDUK SELURUH EXCEPTION APLIKASI
      ├── ArithmeticError
      │    ├── ZeroDivisionError # Pembagian dengan nol
      │    └── OverflowError     # Angka float melebihi batas representasi
      ├── LookupError
      │    ├── IndexError        # Indeks urutan melampaui rentang (list/tuple)
      │    └── KeyError          # Key tidak ditemukan pada dictionary
      ├── ValueError             # Tipe benar tapi isi nilai tidak valid
      ├── TypeError              # Tipe data tidak sesuai operasi
      └── OSError
           ├── FileNotFoundError # Berkas fisik tidak ada di disk
           └── PermissionError   # Hak akses file ditolak
```

> [!IMPORTANT]
> **Hindari Bare `except:`**: Jangan pernah menulis `except:` tanpa nama kelas exception, karena blok tersebut juga akan menangkap `KeyboardInterrupt` dan `SystemExit`, membuat program Anda tidak dapat dihentikan oleh pengguna dari terminal. Selalu tangkap kelas spesifik, atau minimal tangkap `except Exception:` jika benar-benar membutuhkan penanganan umum.

---

## 3. Alur Lengkap: `try`, `except`, `else`, dan `finally`

Python menyediakan empat blok terpadu untuk mengendalikan alur penanganan galat:

```python
try:
    # 1. Jalankan blok kode yang berpotensi memicu exception
    file = open("data.txt", "r", encoding="utf-8")
    konten = file.read()
    nilai = int(konten.strip())
except FileNotFoundError as err:
    # 2. Eksekusi jika terjadi FileNotFoundError
    print(f"Penanganan: Berkas tidak ditemukan ({err})")
except ValueError as err:
    # 3. Eksekusi jika konversi int() gagal
    print(f"Penanganan: Isi berkas bukan integer valid ({err})")
else:
    # 4. Eksekusi HANYA JIKA TIDAK ADA exception sama sekali di blok try
    print(f"Sukses membaca nilai konfigurasi: {nilai}")
finally:
    # 5. SELALU DIEKSEKUSI, baik terjadi exception maupun tidak
    print("Membersihkan alokasi memori dan merilis operasi I/O.")
```

- **`try`**: Menguji operasi berbahaya.
- **`except`**: Menangkap dan mengisolasi kegagalan spesifik.
- **`else`**: Menampung kode yang hanya boleh berjalan jika blok `try` sukses 100% tanpa error (memisahkan kode pengetesan dari kode kelanjutan).
- **`finally`**: Blok pembersihan mutlak (misalnya menutup koneksi soket jaringan atau merilis kunci basis data).

---

## 4. Memicu Exception dengan `raise`

Kita tidak hanya pasif menangani error; program yang baik menerapkan prinsip *fail-fast*—memicu exception secara sengaja menggunakan statement `raise` saat aturan bisnis atau invarian dilanggar:

```python
def atur_daya_pemancar(daya_watt: float) -> None:
    if daya_watt < 0:
        raise ValueError(f"Daya pemancar tidak boleh bernilai negatif: {daya_watt} W")
    print(f"Daya berhasil disetel ke {daya_watt} W")
```

---

## 5. Merancang Custom Exception Domain

Untuk membedakan galat logika bisnis jaringan telekomunikasi dari kesalahan internal Python, kita dapat mendefinisikan kelas exception khusus:

```python
class TelecomError(Exception):
    """Base exception untuk domain telekomunikasi."""
    pass

class SignalLossError(TelecomError):
    """Dipicu ketika redaman transmisi melebihi ambang batas aman."""
    def __init__(self, redaman_db: float, ambang_db: float = 30.0) -> None:
        self.redaman_db = redaman_db
        self.ambang_db = ambang_db
        super().__init__(f"Redaman sinyal ({redaman_db} dB) melampaui batas aman ({ambang_db} dB)!")
```

### Exception Chaining (`raise ... from ...`)
Saat menangani exception tingkat rendah (misalnya `KeyError`) di dalam modul gateway, kita dapat membungkusnya ke dalam exception tingkat tinggi domain kita sambil mempertahankan jejak penyebab aslinya:

```python
try:
    port = config["port"]
except KeyError as err:
    raise GatewayConfigError("Konfigurasi port jaringan hilang") from err
```

---

## 6. Anatomi dan Cara Membaca Python Traceback

Ketika runtime exception yang tidak tertangkap terjadi, Python mencetak *traceback* (jejak tumpukan pemanggilan fungsi / *call stack*).

### Strategi Membaca Traceback:
1. **Mulai dari Baris Paling Bawah:** Baris terbawah menunjukkan jenis kelas exception (`ZeroDivisionError`, `KeyError`) beserta pesan penjelasnya.
2. **Lihat Satu Baris ke Atas:** Temukan nama berkas (`File "main.py"`) dan nomor baris kode sumber milik Anda tempat error tersebut meledak.
3. **Telusuri Rantai Pemanggilan ke Atas:** Baris-baris di atasnya menggambarkan urutan fungsi yang memanggil fungsi tersebut dari awal eksekusi program.

---

## 7. Teknik Debugging Sistematis

### A. Defensive Invariants dengan `assert`
Statement `assert kondisi, "Pesan"` digunakan oleh programmer untuk memastikan asumsi logika internal selalu terpenuhi:

```python
def hitung_snr(daya_sinyal: float, daya_noise: float) -> float:
    assert daya_noise > 0, "Daya noise harus lebih besar dari 0 untuk mencegah pembagian tak terhingga"
    return daya_sinyal / daya_noise
```

### B. Interactive Debugger (`breakpoint()` dan `pdb`)
Sejak Python 3.7, Anda cukup menyisipkan `breakpoint()` pada baris kode yang mencurigakan. Saat dijalankan di terminal, program akan membeku dan memberi Anda prompt interaktif `(Pdb)`:
- `n` (*next*): Jalankan satu baris berikutnya.
- `s` (*step into*): Masuk ke dalam fungsi yang sedang dipanggil.
- `c` (*continue*): Lanjutkan eksekusi hingga breakpoint berikutnya atau selesai.
- `p nama_var` (*print*): Cetak nilai variabel saat ini di memori.
- `q` (*quit*): Hentikan eksekusi program.

---

## 8. Pencatatan Terstruktur dengan Modul `logging`

Statement `print()` sementara sering digunakan untuk *quick debugging*, namun meninggalkan `print()` di kode produksi adalah praktik yang buruk. Modul standar `logging` menyediakan kendali level keparahan:

- `logging.DEBUG`: Informasi diagnostik terperinci untuk developer saat melacak bug.
- `logging.INFO`: Konfirmasi bahwa alur operasional sistem berjalan sesuai harapan.
- `logging.WARNING`: Peringatan bahwa terjadi sesuatu yang tak terduga namun sistem masih bisa berlanjut.
- `logging.ERROR`: Kegagalan fungsionalitas tertentu (misal satu transaksi/rekaman gagal diproses).
- `logging.CRITICAL`: Galat parah yang berpotensi melumpuhkan seluruh aplikasi.

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.info("Node telekomunikasi aktif")
logging.warning("Suhu pemancar mencapai 48 C")
```

---

## 9. Proyek Terapan: Robust Data Validator

Sebagai implementasi menyeluruh, modul ini menyediakan mini proyek `TelecomRecordValidator` di folder `content/intermediate/chapter-18/code/validator.py`:
- Menangani berbagai skenario kesalahan data secara defensif tanpa membiarkan pipeline crash.
- Memisahkan data valid dari data anomali dan mencatat diagnostik ke modul `logging`.
- Menerapkan hierarki custom exception (`MissingFieldError`, `InvalidRangeError`).
- Diuji secara otomatis menggunakan framework `unittest`.

---

## 10. Referensi Pembelajaran

1. **Python Software Foundation.** *Errors and Exceptions Tutorial*. https://docs.python.org/3/tutorial/errors.html
2. **Python Software Foundation.** *Built-in Exceptions Reference*. https://docs.python.org/3/library/exceptions.html
3. **Python Software Foundation.** *Logging HOWTO*. https://docs.python.org/3/howto/logging.html
4. **Python Software Foundation.** *The Python Debugger (pdb)*. https://docs.python.org/3/library/pdb.html
5. **Harvard CS50P.** *Exceptions — Week 3*. https://cs50.harvard.edu/python/
