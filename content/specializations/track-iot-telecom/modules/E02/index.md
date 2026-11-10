# Modul E02: IoT Protocols & MQTT Publish-Subscribe

## 1. Mengapa MQTT Lebih Cocok daripada HTTP Polling untuk IoT?
HTTP meminta klien membuka permintaan berulang (*request-response*) dengan header ratusan byte. **MQTT** menggunakan pola **Publish-Subscribe** melalui perantara **Broker** berheader biner minimum 2 byte:
- Sensor cukup melakukan `publish` ke topik saat ada data tanpa perlu tahu alamat IP dashboard penerima.
- Banyak layanan analitik dan alert dapat `subscribe` topik yang sama secara paralel (*decoupled architecture*).

---

## 2. Hierarki Topik & Wildcards (`+` dan `#`)
Topik MQTT berbentuk path hierarkis dipisah garis miring: `kampus/itera/gedung-c/node-01/temp`.
- **Single-Level Wildcard (`+`):** mencocokkan tepat **satu** tingkat folder topik, misalnya `kampus/+/gedung-c/+/temp`.
- **Multi-Level Wildcard (`#`):** hanya boleh berada di akhir filter dan mencocokkan nol atau banyak sub-level (`kampus/itera/#`).

Fungsi `paho.mqtt.client.topic_matches_sub(sub, topic)` memungkinkan pengujian pencocokan pola topik secara tepat.

---

## 3. QoS 0/1/2, Retained Message & LWT
- **QoS 0 (*At most once*):** fire-and-forget, paling cepat dan hemat daya; cocok untuk telemetri berkala berfrekuensi tinggi.
- **QoS 1 (*At least once*):** menjamin pesan sampai minimal sekali (penerima harus idempoten terhadap kemungkinan pesan duplikat saat retry jaringan).
- **QoS 2 (*Exactly once*):** jaminan pengiriman tepat satu kali lewat 4-way handshake; overhead paling tinggi.
- **Retained Message (`retain=True`):** broker menyimpan pesan terakhir topik tersebut sehingga subscriber baru yang baru bergabung langsung mendapat status terkini.
- **Last Will and Testament (LWT):** pesan darurat yang dititipkan ke broker saat koneksi awal; jika sensor putus koneksi mendadak, broker otomatis menyiarkannya ke subscriber status.

