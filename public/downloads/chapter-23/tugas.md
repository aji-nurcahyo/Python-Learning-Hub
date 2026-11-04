# Tugas Praktik: Sistem Manajemen Jaringan Berbasis Pola Desain (Chapter 23)

## Deskripsi Tugas
Dalam tugas tingkat profesional ini, Anda diminta merancang dan mengimplementasikan **Extensible Network Controller System** menggunakan paradigma Object-Oriented Programming (OOP) modern, Abstract Base Classes (ABC), Dataclasses, Factory Pattern, dan Strategy Pattern.

---

## Ketentuan & Persyaratan Arsitektur
1. **Domain Abstraction (`AbstractNode`):**
   - Mendefinisikan kontrak interface wajib: `get_operational_state() -> dict` dan `process_traffic(packets: int) -> int`.
   - Menggunakan `@property` dan `@setter` terenkapsulasi untuk validasi alamat IP manajemen.
2. **Dataclass Configuration (`NodeConfig`):**
   - Konfigurasi simpul jaringan menggunakan `@dataclass(frozen=True)` untuk menjamin integritas konfigurasi saat runtime.
3. **Pola Desain Kreasi (Factory Pattern):**
   - Class `NodeFactory` terpusat yang mampu membuat instansiasi `EdgeRouter` dan `AggregationSwitch` secara dinamis.
4. **Pola Desain Perilaku (Strategy Pattern):**
   - Antarmuka `TrafficRoutingStrategy` dengan dua implementasi konkret: `PriorityRoutingStrategy` dan `RoundRobinRoutingStrategy`.
5. **Komposisi & Injeksi Dependensi (`NetworkController`):**
   - Controller mengelola koleksi simpul jaringan menggunakan komposisi (bukan inheritance berjenjang) dan menerima `TrafficRoutingStrategy` via dependency injection.

---

## Rubrik Penilaian (Total: 100 Poin)

| Komponen Penilaian | Bobot | Kriteria Evaluasi |
|:---|:---:|:---|
| **1. Abstraksi & Kontrak ABC** | 25 Poin | Abstract base class dirancang bersih, `@abstractmethod` diterapkan tepat sasaran, validasi property setter menolak input yang cacat. |
| **2. Penerapan Factory Pattern** | 20 Poin | Factory terpusat mampu membuat objek simpul secara dinamis dan melempar ValueError pada tipe yang tidak terdaftar. |
| **3. Penerapan Strategy Pattern** | 20 Poin | Algoritma perutean lalu lintas dienkapsulasi ke dalam class strategi yang dapat dipertukarkan saat runtime. |
| **4. Komposisi & Loose Coupling** | 20 Poin | Controller mengelola simpul melalui komposisi, modular, tanpa ketergantungan erat (*tight coupling*). |
| **5. Standar Kode & Type Hints** | 15 Poin | Type hints lengkap, dokumentasi docstring profesional, dan kode teruji bebas crash. |
