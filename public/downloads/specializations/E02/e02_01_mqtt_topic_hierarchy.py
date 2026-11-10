import paho.mqtt.client as mqtt

TOPICS = [
    "itera/gedung-c/node-01/env/temp",
    "itera/gedung-c/node-02/env/humidity",
    "itera/gedung-e/node-01/env/temp",
    "itera/gedung-c/node-01/status",
]

SUBSCRIPTIONS = [
    "itera/+/+/env/temp",
    "itera/gedung-c/#",
    "itera/+/node-01/+",
]

for sub in SUBSCRIPTIONS:
    matched = [t for t in TOPICS if mqtt.topic_matches_sub(sub, t)]
    print(f"Filter '{sub}'")
    for m in matched:
        print(f"  -> cocok: {m}")

