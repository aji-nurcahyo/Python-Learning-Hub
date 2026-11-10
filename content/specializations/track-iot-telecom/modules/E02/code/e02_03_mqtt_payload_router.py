import json
import paho.mqtt.client as mqtt


def create_telemetry_mqtt_client(received_store: list[dict]) -> mqtt.Client:
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id="hub-analytics-worker")

    def on_message(_client, _userdata, msg: mqtt.MQTTMessage) -> None:
        try:
            data = json.loads(msg.payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return
        received_store.append({"topic": msg.topic, "qos": msg.qos, "data": data})

    client.on_message = on_message
    return client


if __name__ == "__main__":
    store: list[dict] = []
    client = create_telemetry_mqtt_client(store)

    # Simulasi kedatangan paket MQTTMessage secara offline langsung ke callback on_message
    msg_ok = mqtt.MQTTMessage(topic=b"itera/gedung-c/node-01/telemetry")
    msg_ok.payload = json.dumps({"temp_c": 31.4, "rssi_dbm": -74}).encode("utf-8")
    msg_ok.qos = 1

    msg_bad = mqtt.MQTTMessage(topic=b"itera/gedung-c/node-01/telemetry")
    msg_bad.payload = b"{invalid-json"

    client.on_message(client, None, msg_ok)
    client.on_message(client, None, msg_bad)

    print("Pesan valid tersimpan :", len(store))
    print("Detail pesan pertama  :", store[0])

