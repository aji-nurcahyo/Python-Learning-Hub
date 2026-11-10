# Tugas Praktik: Sistem Pengujian & Observabilitas Produksi (Chapter 26)

## Deskripsi Tugas
Dalam tugas tingkat profesional ini, Anda diminta mengembangkan **Automated Test Suite & Production Telemetry System** untuk memvalidasi keandalan layanan manajemen infrastruktur telekomunikasi (`TelecomInfrastructureManager`) secara menyeluruh.

Pengujian harus mencakup Unit Testing murni, isolasi panggilan soket/API eksternal dengan *mocking*, penanganan kegagalan (*error scenarios*), pengukuran Test Coverage cabang (*branch coverage*), dan verifikasi keluaran log audit terstruktur.

---

## Ketentuan & Persyaratan Arsitektur
1. **Layanan Bisnis Teruji (`TelecomInfrastructureManager`):**
   - Berinteraksi dengan klien perangkat keras remote (`RemoteSwitchGateway`).
   - Melakukan reboot port switch secara terprogram dengan pemeriksaan status daya.
   - Mencatat log audit terstruktur pada setiap tahapan (INFO, WARNING, ERROR).
2. **Suite Pengujian Komprehensif (`TestTelecomInfrastructure`):**
   - **Test Fixtures (`setUp`/`tearDown`):** Menginisialisasi mock client dan instance manager baru sebelum setiap pengujian.
   - **Mocking Isolasi (`MagicMock` / `patch`):** Mensimulasikan respons gateway remote tanpa melakukan transmisi data fisik ke jaringan.
   - **Pengujian Kasus Ekstrem & Exception (`assertRaises`):** Menguji skenario kegagalan timeout jaringan dan penolakan port tidak sah.
   - **Parameterized Subtests (`subTest`):** Menguji variasi kode status daya port switch.
   - **Verifikasi Log Audit (`assertLogs`):** Memastikan pesan log peringatan dicatat saat port dalam status abnormal.
3. **Isolasi Berkas Sementara (`tempfile.TemporaryDirectory`):**
   - Menguji persistensi dump file konfigurasi lokal secara terisolasi tanpa meninggalkan residu berkas pada direktori sistem.

---

## Rubrik Penilaian (Total: 100 Poin)

| Komponen Penilaian | Bobot | Kriteria Evaluasi |
|:---|:---:|:---|
| **1. Kualitas Isolasi & Mocking** | 25 Poin | Menerapkan `MagicMock` secara efektif, method invocation diverifikasi dengan `assert_called_once_with`, pengujian berjalan cepat tanpa I/O fisik. |
| **2. Pengujian Kegagalan & Exception** | 20 Poin | Menggunakan `assertRaises` untuk memastikan error jaringan dan validasi input ditangani secara anggun. |
| **3. Parameterized Subtesting** | 20 Poin | Evaluasi multi-skenario status port dilakukan rapi via `self.subTest()` dengan pesan assertion yang informatif. |
| **4. Observabilitas & Verifikasi Log** | 20 Poin | Menguji keluaran log audit sistem menggunakan `self.assertLogs` pada level keparahan yang tepat (INFO/WARNING/ERROR). |
| **5. Isolasi Lingkungan & Kebersihan Kode** | 15 Poin | Menggunakan `tempfile` untuk I/O file sementara, type hints lengkap, dan mengikuti panduan bahasa teknis. |

