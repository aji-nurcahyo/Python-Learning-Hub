import json
import paho.mqtt.client as mqtt


class OfflineMqttBroker:
    def __init__(self) -> None:
        self.subscribers: list[tuple[str, callable]] = []
        self.retained: dict[str, dict] = {}
        self.seen_qos1_ids: set[int] = set()

    def subscribe(self, pattern: str, callback) -> None:
        self.subscribers.append((pattern, callback))
        for topic, payload in self.retained.items():
            if mqtt.topic_matches_sub(pattern, topic):
                callback(topic, payload, from_retained=True)

    def publish(self, topic: str, payload: dict, qos: int = 0, retain: bool = False, packet_id: int | None = None) -> int:
        if qos == 1 and packet_id is not None:
            if packet_id in self.seen_qos1_ids:
                return 0  # Deduplikasi pesan ulang QoS 1
            self.seen_qos1_ids.add(packet_id)
        if retain:
            self.retained[topic] = payload
        delivered = 0
        for pattern, cb in self.subscribers:
            if mqtt.topic_matches_sub(pattern, topic):
                cb(topic, payload, from_retained=False)
                delivered += 1
        return delivered


if __name__ == "__main__":
    alerts: list[str] = []
    broker = OfflineMqttBroker()

    def temp_monitor(topic: str, data: dict, from_retained: bool) -> None:
        if data.get("temp_c", 0) >= 35.0:
            alerts.append(f"HIGH_TEMP@{topic}:{data['temp_c']}C (retained={from_retained})")

    broker.subscribe("itera/+/env", temp_monitor)
    c1 = broker.publish("itera/lab-telco/env", {"temp_c": 36.8}, qos=1, retain=True, packet_id=501)
    c_dup = broker.publish("itera/lab-telco/env", {"temp_c": 36.8}, qos=1, retain=True, packet_id=501)

    late_events: list[str] = []
    broker.subscribe("itera/lab-telco/#", lambda t, d, from_retained: late_events.append(f"{t}:{d['temp_c']}(ret={from_retained})"))

    print("Pengiriman pesan awal (pid=501) :", c1)
    print("Pengiriman duplikat   (pid=501) :", c_dup)
    print("Alert terpicu                   :", alerts)
    print("Subscriber telat terima retained:", late_events)

