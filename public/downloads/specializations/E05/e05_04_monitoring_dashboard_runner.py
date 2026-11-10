import json
import sys
import tempfile
from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e05_01_telemetry_decoder_mqtt import dispatch_csv_stream_to_topics
from e05_02_signal_conditioning import analyze_and_denoise_vibration
from e05_03_rf_sla_diagnostics import evaluate_all_nodes


def run_iot_monitoring_capstone(csv_path: Path, out_dir: Path) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    routed = dispatch_csv_stream_to_topics(csv_path, "iot/#")
    dsp_res = analyze_and_denoise_vibration()
    rf_audit = evaluate_all_nodes(csv_path)

    df = pd.read_csv(csv_path)
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.4), dpi=150)
    colors = ["#dc2626" if s <= 3.0 else "#16a34a" for s in df["sinr_db"]]
    axes[0].bar(df["node_id"], df["sinr_db"], color=colors)
    axes[0].axhline(3.0, color="#0f172a", linestyle="--", linewidth=1.2, label="Ambang SINR 3 dB")
    axes[0].set_title("Kualitas Radio SINR per Node IoT")
    axes[0].set_ylabel("SINR (dB)")
    axes[0].tick_params(axis="x", rotation=25)
    axes[0].legend()

    axes[1].plot(dsp_res["t"][:120], dsp_res["raw"][:120], alpha=0.45, label="Getaran Mentah")
    axes[1].plot(dsp_res["t"][:120], dsp_res["denoised"][:120], linewidth=2.0, label="Butterworth Filtered")
    axes[1].set_title(f"DSP Denoising Sinyal Menara (+{dsp_res['snr_gain_db']} dB)")
    axes[1].set_xlabel("Waktu (detik)")
    axes[1].legend()

    chart_path = out_dir / "rf_monitoring_dashboard.png"
    fig.tight_layout()
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)

    report_payload = {
        "mqtt_events_routed": len(routed),
        "dsp_snr_gain_db": dsp_res["snr_gain_db"],
        "dsp_dominant_hz": dsp_res["dominant_hz_after"],
        "node_diagnostics": rf_audit,
    }
    json_path = out_dir / "node_health_report.json"
    json_path.write_text(json.dumps(report_payload, indent=2), encoding="utf-8")

    md_lines = [
        "# Laporan Monitoring IoT & Kesehatan Sinyal RF",
        "",
        f"- Pesan telemetri ter-routing via MQTT: {len(routed)}",
        f"- Perbaikan SNR sinyal sensor (Butterworth SOS): +{dsp_res['snr_gain_db']} dB",
        "",
        "## Status Kesehatan Node",
    ]
    for item in rf_audit:
        md_lines.append(f"- {item['node_id']} ({item['region']}): {item['status']} | flags={item['flags']}")
    md_path = out_dir / "ops_summary.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    return {"chart": chart_path, "json": json_path, "markdown": md_path}


if __name__ == "__main__":
    csv_file = CODE_DIR.parent / "datasets" / "iot_node_telemetry_stream.csv"
    with tempfile.TemporaryDirectory() as td:
        artifacts = run_iot_monitoring_capstone(csv_file, Path(td))
        payload = json.loads(artifacts["json"].read_text(encoding="utf-8"))
        print("Artefak monitoring dibuat :", [p.name for p in artifacts.values()])
        print("Event MQTT ter-routing    :", payload["mqtt_events_routed"])
        print("Kenaikan SNR DSP          : +", payload["dsp_snr_gain_db"], "dB")
        print("Node berstatus CRITICAL   :", [n["node_id"] for n in payload["node_diagnostics"] if n["status"] == "CRITICAL"])

