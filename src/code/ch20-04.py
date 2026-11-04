"""Contoh 20.4: Duck Typing dalam Python ("If it walks like a duck...")
Python Learning Hub - Level 2: Intermediate Python
"""

# Duck typing: Python tidak mewajibkan pewarisan dari class induk yang sama,
# asalkan objek menyediakan method atau antarmuka yang diharapkan.

class AudioStreamer:
    def stream_payload(self, data: str) -> str:
        return f"[Audio Codec Opus] Mengirim paket audio: '{data}' (Bitrate: 64kbps)"

class TelemetryStreamer:
    def stream_payload(self, data: str) -> str:
        return f"[IoT MQTT Stream] Memublikasikan telemetri: '{data}' (QoS: 1)"

class VideoStreamer:
    def stream_payload(self, data: str) -> str:
        return f"[H.265 Stream] Streaming frame video: '{data}' (1080p60)"

def broadcast_transceiver(streamer_obj, payload: str) -> None:
    """Fungsi ini hanya peduli bahwa objek memiliki method stream_payload()."""
    print(streamer_obj.stream_payload(payload))

streamers = [AudioStreamer(), TelemetryStreamer(), VideoStreamer()]

print("=== Duck Typing: Menjalankan Streamer Transceiver ===")
for s in streamers:
    broadcast_transceiver(s, "SAMPLE_PAYLOAD_DATA_2026")
