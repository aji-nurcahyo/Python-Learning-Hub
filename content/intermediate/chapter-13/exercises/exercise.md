# Latihan Terarah — Chapter 13: Advanced Functions

Selesaikan latihan berikut untuk menguji pemahaman Anda mengenai *args, **kwargs, fungsi tingkat tinggi, ekspresi lambda, closures, dan rekursi.

---

### Latihan 1: Akumulator Multi-Metrik Berbasis `*args`
**Tujuan:** Menerapkan fungsi dengan jumlah argumen posisi variabel (*variable-length arguments*).

1. Buat fungsi `hitung_metrik_sinyal(nama_stasiun: str, *daya_dbm: float) -> dict`.
2. Fungsi harus menerima nama stasiun sebagai parameter wajib, dan sembarang banyaknya data daya sinyal dalam `*daya_dbm`.
3. Jika tidak ada data yang diberikan, kembalikan kamus dengan status `"KOSONG"`.
4. Jika ada data, kembalikan kamus berisi:
   - `"stasiun"`: Nama stasiun.
   - `"jumlah_sampel"`: Total sampel yang diterima.
   - `"daya_maksimum"`: Nilai dBm tertinggi.
   - `"daya_rata_rata"`: Nilai rata-rata dBm (dibulatkan 2 desimal).

---

### Latihan 2: Pengurutan Paket Jaringan Menggunakan Lambda
**Tujuan:** Menggunakan ekspresi `lambda` sebagai *custom key* pada fungsi `sorted()`.

1. Diberikan struktur data daftar paket jaringan telekomunikasi:
   ```python
   paket = [
       {"id": "PKT-1", "prioritas": 2, "ukuran_byte": 1500, "latensi_ms": 12.4},
       {"id": "PKT-2", "prioritas": 1, "ukuran_byte": 64,   "latensi_ms": 4.2},
       {"id": "PKT-3", "prioritas": 1, "ukuran_byte": 512,  "latensi_ms": 8.1},
       {"id": "PKT-4", "prioritas": 3, "ukuran_byte": 1024, "latensi_ms": 25.0},
   ]
   ```
2. Urutkan paket dengan kriteria:
   - Terurut utama: Berdasarkan prioritas terkecil (nilai `1` adalah prioritas tertinggi).
   - Terurut sekunder: Jika prioritas sama, dahulukan latensi terkecil (`latensi_ms`).
3. Gunakan satu fungsi `sorted()` dengan *tuple key* pada ekspresi `lambda`.

---

### Latihan 3: Pembangkit Validator Ambang Batas (Closure Generator)
**Tujuan:** Membuat fungsi bertingkat (*nested function*) yang mempertahankan status lingkup penutup (*lexical scope*).

1. Rancang fungsi pabrik (*factory function*) `buat_penguji_tegangan(tegangan_nominal: float, toleransi_persen: float = 5.0)`.
2. Fungsi harus mengembalikan sebuah fungsi closure `cek_tegangan(tegangan_terbaca: float) -> tuple[bool, str]`.
3. Hitung rentang toleransi bawah dan atas:
   $$\text{Batas Bawah} = \text{nominal} \times (1 - \text{toleransi}/100)$$
   $$\text{Batas Atas} = \text{nominal} \times (1 + \text{toleransi}/100)$$
4. Uji closure dengan tegangan nominal $48.0\text{ V}$ dan toleransi $10.0\%$.

---

### Latihan 4: Rekursi Penelusuran Topologi Cabang Jaringan
**Tujuan:** Mengimplementasikan fungsi rekursif sederhana dengan *base case* yang kokoh.

1. Buat fungsi rekursif `hitung_kedalaman_node(pohon_jaringan: dict) -> int`.
2. Sebuah node jaringan direpresentasikan sebagai:
   ```python
   jaringan = {
       "nama": "Router Pusat",
       "sub_node": {
           "nama": "Switch Gedung A",
           "sub_node": {
               "nama": "Access Point Lab",
               "sub_node": None
           }
       }
   }
   ```
3. Jika `sub_node` adalah `None`, kembalikan `1` (*base case*).
4. Jika terdapat anak node, panggil `1 + hitung_kedalaman_node(pohon_jaringan["sub_node"])`.

