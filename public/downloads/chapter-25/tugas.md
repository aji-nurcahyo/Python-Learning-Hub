# Tugas Praktik: Pustaka Utilitas Tipe Aman (Chapter 25)

## Deskripsi Tugas
Dalam tugas tingkat profesional ini, Anda diminta merancang dan mengimplementasikan **Type-Safe Network Observability Toolkit** yang memenuhi standar penulisan kode modern, sepenuhnya teranotasi tipe (*100% type annotated*), kompatibel dengan *static type checker* (mypy), dan diformat rapi sesuai PEP 8 / Ruff.

---

## Ketentuan & Persyaratan Arsitektur
1. **Skema Kamus Terstruktur (`MetricPayload` TypedDict):**
   - Mendefinisikan kunci wajib: `metric_name: str`, `value: float`, `unit: str`, `timestamp: str`.
   - Mendefinisikan kunci opsional (`NotRequired`): `tags: dict[str, str]`.
2. **Kontrak Antarmuka Struktural (`MetricEncoder` Protocol):**
   - Menerapkan `Protocol` dengan decorator `@runtime_checkable` yang mewajibkan method `encode_metric(metric: MetricPayload) -> str`.
3. **Repositori Generic (`MetricStore[T]`):**
   - Menggunakan `Generic[T]` dan `TypeVar` untuk menyimpan koleksi elemen metrik secara type-safe.
4. **Layanan Pemrosesan Data Beranotasi Lengkap (`MetricService`):**
   - Menerima encoder melalui dependency injection.
   - Menyediakan method `filter_metrics(predicate: Callable[[MetricPayload], bool]) -> list[MetricPayload]`.
   - Mengombinasikan static type hinting dengan validasi runtime defensif (`isinstance`).

---

## Rubrik Penilaian (Total: 100 Poin)

| Komponen Penilaian | Bobot | Kriteria Evaluasi |
|:---|:---:|:---|
| **1. Kualitas Type Annotations** | 25 Poin | Type hints lengkap pada seluruh parameter fungsi, return type, dan atribut class menggunakan sintaksis modern Python 3.10+. |
| **2. Penerapan TypedDict & Protocol** | 25 Poin | TypedDict menggunakan `NotRequired` secara tepat, Protocol menggunakan `@runtime_checkable` dan structural subtyping. |
| **3. Implementasi Generic Class** | 20 Poin | Pemanfaatan `TypeVar` dan `Generic[T]` secara benar pada kelas penyimpanan tanpa kebocoran tipe `Any`. |
| **4. Validasi Runtime & Defensif** | 15 Poin | Memadukan pemeriksaan statis dengan validasi runtime `isinstance()` yang melempar exception saat data cacat. |
| **5. Kepatuhan Standar PEP 8 & Ruff** | 15 Poin | Format kode konsisten, penamaan PascalCase/snake_case rapi, tidak ada mutable default arguments. |
