import json
import sys
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from a05_01_pipeline_ingestion import load_and_validate
from a05_02_cleaning_enrichment import clean_and_enrich
from a05_03_kpi_engine import compute_regional_kpis


def run_capstone_pipeline(logs_path: Path, meta_path: Path, out_dir: Path) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    logs_df, meta_df = load_and_validate(logs_path, meta_path)
    enriched = clean_and_enrich(logs_df, meta_df)
    kpi_df = compute_regional_kpis(enriched)

    # Render dashboard chart
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), dpi=150)
    sns.barplot(data=kpi_df, x="region", y="sla_compliance_pct", ax=axes[0], color="#2563eb")
    axes[0].set_ylim(0, 105)
    axes[0].set_title("SLA Compliance Rate (%) per Wilayah")
    axes[0].set_ylabel("Compliance (%)")

    sns.boxplot(data=enriched, x="technology", y="latency_ms", ax=axes[1], color="#0d9488")
    axes[1].set_title("Distribusi Latensi: 4G vs 5G")
    axes[1].set_ylabel("Latensi (ms)")

    chart_path = out_dir / "capstone_dashboard.png"
    fig.tight_layout()
    fig.savefig(chart_path, dpi=150)
    plt.close(fig)

    summary_path = out_dir / "kpi_summary.json"
    summary_records = kpi_df.round(2).to_dict(orient="records")
    summary_path.write_text(json.dumps(summary_records, indent=2), encoding="utf-8")

    md_lines = [
        "# Laporan Analitik Kinerja Jaringan Regional",
        "",
        f"- Total log tervalidasi: {len(enriched)}",
        f"- Pelanggaran SLA terdeteksi: {int(enriched['sla_breach'].sum())}",
        "",
        "## Ringkasan Wilayah",
    ]
    for row in summary_records:
        md_lines.append(
            f"- {row['region']}: compliance {row['sla_compliance_pct']}%, median latency {row['median_latency_ms']} ms"
        )
    report_path = out_dir / "analytics_report.md"
    report_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    return {"chart": chart_path, "summary": summary_path, "report": report_path}


if __name__ == "__main__":
    ds_dir = CODE_DIR.parent / "datasets"
    with tempfile.TemporaryDirectory() as tmp_dir:
        artifacts = run_capstone_pipeline(
            ds_dir / "network_operations_logs.csv",
            ds_dir / "tower_metadata.csv",
            Path(tmp_dir),
        )
        print("Pipeline Capstone selesai. Artefak terverifikasi:")
        for key, path in artifacts.items():
            print(f" - {key:8s}: {path.name} ({path.stat().st_size} bytes)")
        print("\nCuplikan Ringkasan KPI:")
        print(artifacts["summary"].read_text(encoding="utf-8").strip())

