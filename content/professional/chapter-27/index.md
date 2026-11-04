# Chapter 27: Concurrent & Asynchronous Programming
## Threading, Multiprocessing, Asyncio & Task Concurrency

Selamat datang di **Chapter 27: Concurrent & Asynchronous Programming** pada tingkat **Level 3: Professional Python Engineering** di **Python Learning Hub**.

Pada modul-modul sebelumnya, Anda telah mempelajari bagaimana membangun basis kode yang bersih dan teruji (Chapters 23–26). Namun, dalam aplikasi produksi dunia nyata—terutama sistem backend berskala tinggi, pipeline pemrosesan telemetri, dan integrasi jaringan—menjalankan instruksi secara sekuensial satu per satu sering kali menjadi kendala utama performa (*bottleneck*).

Bab ini mengupas secara komprehensif paradigma pemrograman konkuren dan asinkron di Python. Anda akan mempelajari komparasi antara *threading*, *multiprocessing*, dan *asyncio*, memahami realitas *Global Interpreter Lock* (GIL), mengamankan *shared mutable state* dari *race condition* menggunakan *locks*, serta merancang arsitektur tugas konkuren yang tangguh terhadap *timeout* dan kegagalan.

---

## 1. Konkurensi vs Paralelisme & Klasifikasi Beban Kerja

Dalam rekayasa sistem komputer, penting untuk membedakan dua konsep yang sering disamakan:

1. **Concurrency (Konkurensi):**
   - Kemampuan suatu sistem untuk menangani beberapa tugas dalam rentang waktu yang sama (*dealing with a lot of things at once*).
   - Pada CPU dengan satu *core*, konkurensi diwujudkan melalui *interleaving* atau *context switching*, di mana sistem operasi atau runtime berganti-ganti mengeksekusi potongan tugas secara cepat sehingga tampak berjalan bersamaan.
2. **Parallelism (Paralelisme):**
   - Kemampuan perangkat keras untuk mengeksekusi beberapa instruksi secara fisik simultan pada waktu yang persis sama (*doing a lot of things at once*).
   - Paralelisme sejati membutuhkan perangkat keras fisik dengan *multi-core* atau *multi-CPU*.

### Klasifikasi Beban Kerja (*Workload Classification*)

Strategi optimasi yang dipilih bergantung sepenuhnya pada karakteristik beban kerja:

- **I/O-Bound Workload:**
  Tugas yang menghabiskan sebagian besar waktunya untuk menunggu respons perangkat eksternal, seperti pembacaan soket jaringan (*network socket*), kueri basis data (*database queries*), atau pembacaan file dari disk. Selama menunggu I/O, prosesor berada dalam kondisi menganggur (*idle*). Model yang cocok: **`threading`** atau **`asyncio`**.
- **CPU-Bound Workload:**
  Tugas yang memerlukan komputasi intensif dan pemanfaatan siklus prosesor secara terus-menerus, seperti enkripsi data kriptografis, kompresi file, kalkulasi matriks, atau algoritma pencarian berat. Model yang cocok: **`multiprocessing`**.

---

## 2. Threading & Thread Lifecycle

Thread adalah unit eksekusi terkecil di dalam sebuah proses sistem operasi. Semua thread di dalam proses yang sama berbagi ruang alamat memori (*shared address space*) yang identik.

### Siklus Hidup Thread (*Thread Lifecycle*)
1. **Inisialisasi:** Membuat instance `threading.Thread(target=fn, args=(...))`.
2. **Starting:** Memanggil `thread.start()` untuk meminta sistem operasi menjadwalkan eksekusi thread.
3. **Execution:** Fungsi target dieksekusi secara konkuren dengan thread utama.
4. **Joining:** Memanggil `thread.join()` pada thread utama untuk menahan proses hingga thread pekerja selesai melakukan tugasnya.

```python
import threading
import time

def worker(sensor_id: str) -> None:
    time.sleep(0.1)
    print(f"Sensor {sensor_id} selesai dibaca.")

thread = threading.Thread(target=worker, args=("BTS-01",))
thread.start()
thread.join()  # Menunggu worker selesai
```

---

## 3. High-Level Thread Pools dengan `ThreadPoolExecutor`

Membuat dan menghancurkan objek thread OS secara manual untuk setiap tugas menimbulkan *overhead* performa yang mahal. Modul standar `concurrent.futures` menyediakan **`ThreadPoolExecutor`**, sebuah pola *worker pool* yang mengelola siklus hidup sekumpulan thread yang siap digunakan kembali (*reusable threads*).

Keuntungan `ThreadPoolExecutor`:
- Mengatur batas maksimum konkurensi (`max_workers`) agar sistem tidak kehabisan sumber daya OS.
- Mengembalikan objek **`Future`** yang merepresentasikan hasil operasi masa depan.
- Mempermudah pengambilan hasil secara berurutan dengan `executor.map()` atau berdasarkan waktu selesai dengan `as_completed()`.

---

## 4. Global Interpreter Lock (GIL) & Multiprocessing

Salah satu topik terpenting dalam ekosistem Python adalah **Global Interpreter Lock (GIL)**.

### Apa itu GIL?
GIL adalah mekanisme muteks internal yang digunakan oleh implementasi CPython (interpreter Python standar) untuk menjamin keamanan manajemen memori (*reference counting*). GIL memastikan bahwa hanya **satu thread** yang mengeksekusi *bytecode* CPython pada satu saat, meskipun aplikasi dijalankan pada mesin dengan puluhan *core* prosesor.

### Realitas Teknis GIL:
- **Detail Implementasi CPython:** GIL bukan bagian dari spesifikasi bahasa Python murni. Runtimes lain seperti Jython (Java) atau IronPython (.NET) tidak memiliki GIL. Pada Python versi terbaru (PEP 703), opsi *free-threaded CPython* mulai diperkenalkan secara eksperimental.
- **Dampak pada I/O-Bound:** Ketika sebuah thread Python melakukan panggilan I/O (seperti `socket.recv()` atau `time.sleep()`), CPython melepaskan GIL. Oleh karena itu, *threading* tetap sangat efektif untuk mempercepat tugas I/O-bound.
- **Dampak pada CPU-Bound:** Untuk tugas komputasi murni, multi-threading tidak akan memberikan percepatan paralelisme sejati karena thread akan saling berebut GIL.

### Solusi CPU-Bound: `ProcessPoolExecutor`
Untuk memanfaatkan seluruh *core* CPU pada tugas komputasi intensif, gunakan modul **`multiprocessing`** atau **`ProcessPoolExecutor`**. Setiap proses memiliki interpreter CPython dan ruang memori independen, sehingga masing-masing proses berjalan di core yang berbeda tanpa terhambat oleh GIL.

> [!IMPORTANT]
> **Windows Multiprocessing Guard:** Pada sistem operasi Windows, proses baru dibuat dengan cara men-spawn interpreter baru dan mengimpor ulang modul utama. Anda **wajib** melindungi pemanggilan `ProcessPoolExecutor` dengan blok `if __name__ == '__main__':` untuk mencegah perulangan *infinite process spawning*.

---

## 5. Pemrograman Asinkron dengan `asyncio`

Sementara *threading* menggunakan model *preemptive multitasking* yang diatur oleh kernel sistem operasi, modul **`asyncio`** mengadopsi model **single-threaded cooperative multitasking**.

### Konsep Inti Asyncio:
1. **Event Loop:** Orkestrator pusat yang memantau penanda waktu (*timer*), soket jaringan, dan antrean *task*. Ketika suatu operasi menunggu respon jaringan, event loop mengalihkan eksekusi ke coroutine lain yang sudah siap.
2. **Coroutine (`async def`):** Fungsi khusus yang dapat ditangguhkan (*suspended*) dan dilanjutkan kembali (*resumed*) eksekusinya.
3. **Await (`await`):** Menyerahkan kendali kembali ke event loop secara kooperatif hingga operasi yang ditunggu selesai.
4. **`asyncio.gather(*tasks)`:** Menjalankan banyak coroutine secara konkuren dan mengumpulkan semua hasilnya dalam bentuk daftar terurut.
5. **Timeouts (`asyncio.wait_for`):** Membatasi waktu maksimum eksekusi suatu coroutine untuk mencegah *hanging* pada koneksi yang tidak responsif.

---

## 6. Bahaya Konkurensi: Race Condition, Lock & Deadlock

### Race Condition
Kondisi di mana keluaran aplikasi menjadi tidak konsisten atau salah karena beberapa thread membaca dan menulis ke variabel bersama (*shared mutable state*) pada saat yang sama tanpa koordinasi.

### Solusi: `threading.Lock`
Untuk melindungi *critical section* (bagian kode yang mengakses data bersama), gunakan primitif **`threading.Lock`**. Terapkan selalu menggunakan idiom *context manager*:

```python
import threading

lock = threading.Lock()
counter = 0

def safe_increment() -> None:
    global counter
    with lock:  # acquire lock otomatis
        counter += 1
    # release lock otomatis bahkan jika terjadi exception
```

### Pencegahan Deadlock
Deadlock terjadi ketika Thread A memegang Lock 1 dan menunggu Lock 2, sementara Thread B memegang Lock 2 dan menunggu Lock 1. Keduanya saling menunggu selamanya.
- **Aturan Lock Ordering:** Selalu peroleh lock dengan urutan yang sama di seluruh alur kode.
- **Lock Timeouts:** Gunakan `lock.acquire(timeout=2.0)` untuk menghindari penantian tanpa akhir.

---

## 7. Matriks Pengambilan Keputusan

| Karakteristik Beban Kerja | Model yang Direkomendasikan | Alasan Rekayasa |
| :--- | :--- | :--- |
| **I/O Sederhana / Integrasi Legacy** | `ThreadPoolExecutor` | Mudah diintegrasikan dengan pustaka synchronous; efisien untuk puluhan koneksi. |
| **I/O Skala Masif (Web/API/WebSocket)** | `asyncio` | Mampu menangani puluhan ribu koneksi konkuren dengan jejak memori sangat rendah. |
| **CPU-Bound / Komputasi Matematika** | `ProcessPoolExecutor` | Melewati batas GIL dengan mendistribusikan beban kerja ke seluruh core CPU fisik. |
| **Alur Logika Sederhana & Cepat** | Sequential Execution | Menghindari kompleksitas dan overhead manajemen konkurensi. |

---

## 8. Ringkasan & Referensi Lanjutan

- Modul `threading` dan `concurrent.futures` memberikan abstraksi tingkat tinggi untuk tugas berbasis thread.
- `asyncio` menjadi standar de-facto untuk membangun arsitektur layanan web asinkron modern.
- Selalu proteksi *shared state* menggunakan `threading.Lock` untuk mencegah *race condition*.
- Simak referensi resmi Python:
  - [Python Docs: `concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html)
  - [Python Docs: `asyncio`](https://docs.python.org/3/library/asyncio.html)
  - [Python Docs: `threading`](https://docs.python.org/3/library/threading.html)
  - [Python Docs: `multiprocessing`](https://docs.python.org/3/library/multiprocessing.html)
