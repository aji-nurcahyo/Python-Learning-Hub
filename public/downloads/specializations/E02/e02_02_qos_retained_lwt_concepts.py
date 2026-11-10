from dataclasses import dataclass, field


@dataclass
class SimBrokerState:
    retained: dict[str, str] = field(default_factory=dict)
    will_registry: dict[str, tuple[str, str]] = field(default_factory=dict)
    delivered_log: list[tuple[str, str]] = field(default_factory=list)

    def connect_with_lwt(self, client_id: str, will_topic: str, will_payload: str) -> None:
        self.will_registry[client_id] = (will_topic, will_payload)

    def publish(self, topic: str, payload: str, retain: bool = False) -> None:
        if retain:
            self.retained[topic] = payload
        self.delivered_log.append((topic, payload))

    def simulate_ungraceful_disconnect(self, client_id: str) -> None:
        if client_id in self.will_registry:
            w_topic, w_payload = self.will_registry.pop(client_id)
            self.publish(w_topic, w_payload, retain=True)


broker = SimBrokerState()
broker.connect_with_lwt("sensor-gku-01", "itera/gku/sensor-01/status", "OFFLINE_LWT")
broker.publish("itera/gku/sensor-01/status", "ONLINE", retain=True)
print("Status awal (retained) :", broker.retained["itera/gku/sensor-01/status"])

broker.simulate_ungraceful_disconnect("sensor-gku-01")
print("Status sesudah putus   :", broker.retained["itera/gku/sensor-01/status"])
print("Urutan log broker      :", broker.delivered_log)

