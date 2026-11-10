# Tugas Terstruktur E02: MQTT Telemetry Router & Offline Broker Simulator

## Instruksi Implementasi (`tugas.py`)
1. `filter_matching_topics(subscription: str, candidate_topics: list[str]) -> list[str]`: gunakan `mqtt.topic_matches_sub`.
2. Implementasikan kelas `SimulatedMqttBroker` yang mendukung `register_lwt(client_id, topic, payload)`, `subscribe(pattern, callback)`, `publish(topic, payload, qos, retain, packet_id)`, serta `trigger_ungraceful_disconnect(client_id)`.
3. Pastikan duplikat `packet_id` pada `qos == 1` tidak dikirim dua kali dan subscriber baru menerima pesan `retain=True` yang cocok dengan polanya.
4. Uji memakai `pytest` secara offline penuh.

## Rubrik Penilaian (Total 100 Poin)
- Desain Hierarki Topik & Wildcard Matching (25%)
- Implementasi Retained Message & Trigger LWT (30%)
- Penanganan Payload JSON & Paho v2 Callback (25%)
- Unit Testing Broker Simulasi (Pytest) (20%)

