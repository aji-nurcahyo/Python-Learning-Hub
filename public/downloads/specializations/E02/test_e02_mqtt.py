import sys
from pathlib import Path
import paho.mqtt.client as mqtt

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e02_03_mqtt_payload_router import create_telemetry_mqtt_client
from e02_04_offline_broker_pipeline import OfflineMqttBroker


def test_topic_wildcards_and_callback_parsing() -> None:
    assert mqtt.topic_matches_sub("itera/+/env/temp", "itera/lab/env/temp") is True
    assert mqtt.topic_matches_sub("itera/+/env/temp", "itera/lab/room2/env/temp") is False
    assert mqtt.topic_matches_sub("itera/#", "itera/lab/room2/env/temp") is True

    store = []
    client = create_telemetry_mqtt_client(store)
    msg = mqtt.MQTTMessage(topic=b"itera/lab/temp")
    msg.payload = b'{"temp_c": 29.5}'
    client.on_message(client, None, msg)
    assert len(store) == 1 and store[0]["data"]["temp_c"] == 29.5


def test_offline_broker_qos1_dedup_and_retained() -> None:
    broker = OfflineMqttBroker()
    seen = []
    broker.subscribe("itera/#", lambda t, d, from_retained: seen.append((t, d["v"], from_retained)))
    assert broker.publish("itera/n1", {"v": 1}, qos=1, retain=True, packet_id=77) == 1
    assert broker.publish("itera/n1", {"v": 1}, qos=1, retain=True, packet_id=77) == 0

    late = []
    broker.subscribe("itera/n1", lambda t, d, from_retained: late.append(from_retained))
    assert late == [True]

