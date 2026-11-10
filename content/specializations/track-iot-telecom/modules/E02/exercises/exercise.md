# Latihan Mandiri E02 — IoT Protocols & MQTT

## Latihan 1: Topic Wildcards & Offline Broker Simulation
1. Evaluasi daftar topik `itera/+/env/temp` dan `itera/gedung-c/#` memakai `paho.mqtt.client.topic_matches_sub`.
2. Konfigurasikan `mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)` dengan `on_message` yang mem-parse JSON serta menolak payload korup secara aman.
3. Simulasikan LWT disconnect dan deduplikasi pesan QoS 1 menggunakan kelas `OfflineMqttBroker` serta jalankan `pytest code/test_e02_mqtt.py`.

