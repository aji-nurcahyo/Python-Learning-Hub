from pathlib import Path
import paho.mqtt.client as mqtt
import pandas as pd


def dispatch_csv_stream_to_topics(csv_path: Path, subscription_filter: str = "iot/Sumatera/#") -> list[dict]:
    df = pd.read_csv(csv_path)
    matched_events: list[dict] = []
    for row in df.to_dict(orient="records"):
        topic = f"iot/{row['region']}/{row['node_id']}/telemetry"
        if mqtt.topic_matches_sub(subscription_filter, topic):
            matched_events.append({"topic": topic, "node_id": row["node_id"], "rsrp_dbm": row["rsrp_dbm"]})
    return matched_events


if __name__ == "__main__":
    csv_file = Path(__file__).resolve().parent.parent / "datasets" / "iot_node_telemetry_stream.csv"
    sumatera_msgs = dispatch_csv_stream_to_topics(csv_file, "iot/Sumatera/#")
    all_msgs = dispatch_csv_stream_to_topics(csv_file, "iot/#")
    print("Total pesan masuk (iot/#)         :", len(all_msgs))
    print("Pesan terfilter (iot/Sumatera/#)  :", len(sumatera_msgs))
    for ev in sumatera_msgs:
        print(" -", ev)

