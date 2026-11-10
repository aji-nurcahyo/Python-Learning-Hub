# Modul A05 (Capstone): End-to-End Analytics Report

## 1. Arsitektur Pipeline Analitik Profesional
Sebuah proyek Data Science tingkat industri tidak berhenti pada eksplorasi sel demi sel di notebook, melainkan dirangkai menjadi **pipeline modular** yang deterministik, dapat diuji ulang, dan menghasilkan artefak laporan otomatis:
1. **Stage 1 — Ingestion & Schema Validation:** memeriksa keberadaan berkas dan kelengkapan kolom wajib sebelum analisis dimulai.
2. **Stage 2 — Cleaning & Enrichment:** membersihkan duplikasi kunci (`log_id`), memperbaiki anomali sensor tidak masuk akal (seperti latensi negatif `-5.0 ms`), mengisi nilai hilang berbasis segmen, lalu memperkaya baris fakta melalui `left join` dengan `tower_metadata.csv`.
3. **Stage 3 — KPI Engine:** menghitung metrik berdaya guna seperti `sla_compliance_pct`, `median_latency_ms`, `p95_latency_ms`, dan daftar menara pelanggar SLA.
4. **Stage 4 — Artifact & Report Generation:** mengekspor figur ringkas beresolusi tinggi serta menyusun ringkasan terstruktur (Markdown + JSON) untuk pengambil keputusan.

---

## 2. Mengapa Harus Memisahkan Kalkulasi dari File I/O?
Dengan menempatkan transformasi Pandas/NumPy ke fungsi murni yang menerima dan mengembalikan `DataFrame`, Anda dapat menjalankan unit test `pytest` tanpa bergantung pada konfigurasi server eksternal. Fungsi ekspor file menerima objek `Path` (atau `tmp_path` dari `pytest`), menjamin zero side-effect selama testing.

