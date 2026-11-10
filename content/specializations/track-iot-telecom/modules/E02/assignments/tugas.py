"""Starter code Tugas E02: MQTT Telemetry Router & Offline Broker Simulator."""

from __future__ import annotations

import paho.mqtt.client as mqtt


def filter_matching_topics(subscription: str, candidate_topics: list[str]) -> list[str]:
    """Mengembalikan topik yang cocok terhadap filter wildcard MQTT (+ / #)."""
    # TODO: Gunakan mqtt.topic_matches_sub(subscription, topic)
    raise NotImplementedError("Implementasikan filter_matching_topics")


class SimulatedMqttBroker:
    """Simulator broker MQTT deterministik di memori untuk pengujian offline."""

    def __init__(self) -> None:
        self.subscribers: list[tuple[str, object]] = []
        self.retained: dict[str, dict] = {}
        self.lwt_map: dict[str, tuple[str, dict]] = {}
        self.seen_qos1_packets: set[int] = set()

    def subscribe(self, pattern: str, callback) -> None:
        # TODO: Simpan subscriber dan kirim retained message yang cocok
        raise NotImplementedError("Implementasikan subscribe")

    def publish(self, topic: str, payload: dict, qos: int = 0, retain: bool = False, packet_id: int | None = None) -> int:
        # TODO: Terapkan deduplikasi QoS 1 dan simpan retained bila retain=True
        raise NotImplementedError("Implementasikan publish")


if __name__ == "__main__":
    print("Starter E02 siap diuji dengan paho-mqtt v2 & pytest offline.")

