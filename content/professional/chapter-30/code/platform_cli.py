"""Chapter 30: Professional Capstone Project
Presentation / CLI Layer: Antarmuka Komando Platform
"""

import argparse
from typing import Any

try:
    from platform_engine import TelemetryProcessingEngine
    from platform_reporter import TelemetryReportGenerator
    from platform_sources import LocalCsvTelemetrySource, MockApiTelemetrySource
    from platform_storage import LocalTelemetryStorage
except ImportError:
    from .platform_engine import TelemetryProcessingEngine
    from .platform_reporter import TelemetryReportGenerator
    from .platform_sources import LocalCsvTelemetrySource, MockApiTelemetrySource
    from .platform_storage import LocalTelemetryStorage


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="monitor-platform",
        description="Python Data Monitoring & Automation Platform (Capstone CLI)",
    )
    parser.add_argument("--run", action="store_true", help="Menjalankan siklus penyerapan dan analisis data")
    parser.add_argument("--report", action="store_true", help="Mencetak laporan ringkasan performa Markdown")
    parser.add_argument("--cluster", default="Lampung-Core", help="Nama klaster target")
    return parser


def run_platform_cli(
    engine: TelemetryProcessingEngine,
    args_list: list[str],
    default_csv_data: str,
) -> dict[str, Any]:
    parser = build_parser()
    args = parser.parse_args(args_list)

    result: dict[str, Any] = {}

    if args.run:
        csv_src = LocalCsvTelemetrySource(default_csv_data)
        api_src = MockApiTelemetrySource()
        ingested = engine.ingest_from_sources([csv_src, api_src])
        result["ingested_count"] = ingested

    summary = engine.analyze_cluster(args.cluster)
    anomalies = engine.detect_anomalies()
    result["total_nodes"] = summary.total_records
    result["health_rate"] = summary.health_rate
    result["anomalies_count"] = len(anomalies)

    if args.report:
        md_text = TelemetryReportGenerator.generate_markdown(summary, len(anomalies))
        result["report_markdown"] = md_text

    return result

