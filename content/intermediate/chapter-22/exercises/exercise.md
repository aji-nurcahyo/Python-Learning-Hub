# Latihan Terarah Chapter 22: Intermediate Capstone Project

Latihan ini dirancang sebagai pemanasan integratif sebelum Anda membangun arsitektur lengkap **Inventory Management System**.

---

### Latihan 1: Serialisasi dan Deserialisasi Subclass Polymorphic
1. Buat class dasar `Equipment` dan dua subclass `ComputingEquipment` dan `NetworkEquipment`.
2. Implementasikan method `to_dict()` pada setiap class yang menyertakan field `"type": "Computing"` atau `"type": "Network"`.
3. Tulis fungsi `pabrik_equipment(data: dict) -> Equipment` yang secara dinamis menginstansiasi subclass yang tepat berdasarkan nilai field `"type"`.
4. Uji konversi objek ke JSON string dan deserialisasi kembali ke instance subclass yang sesuai.

---

### Latihan 2: Validasi Data Transaksi Inventaris
1. Definisikan exception kustom `NegativePriceError(Exception)` dan `InvalidHostnameError(Exception)`.
2. Tulis validator untuk memastikan nama hostname hanya memuat karakter alfanumerik dan tanda hubung `-` (misal: `"ROUTER-JKT-01"`).
3. Jika harga < 0, lempar `NegativePriceError`. Jika format hostname melanggar aturan, lempar `InvalidHostnameError`.

---

### Latihan 3: Pengurutan Multi-Kriteria (Multi-Key Sorting)
1. Diberikan daftar dictionary inventaris yang memiliki atribut `kategori` (str) dan `harga` (float).
2. Gunakan `list.sort()` atau `sorted()` dengan fungsi `lambda` atau `operator.itemgetter` untuk mengurutkan daftar berdasarkan:
   - Kategori secara alfabetis (A-Z).
   - Jika kategori sama, urutkan berdasarkan harga dari yang paling mahal ke paling murah (*descending*).

---

### Latihan 4: Atomic File Persistence dengan Backup File
1. Rancang fungsi `simpan_aman_json(filepath: Path, data: list[dict]) -> None`.
2. Tulis data ke file temporer dengan akhiran `.tmp`.
3. Setelah proses penulisan file temporer berhasil tanpa exception, ganti nama file temporer tersebut menimpa file target menggunakan `os.replace()` atau `Path.replace()`.
4. Jelaskan mengapa teknik *atomic write* ini penting untuk mencegah kerusakan basis data ketika komputer mati mendadak saat proses penulisan file berlangsung.

