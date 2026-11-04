"""Chapter 30 Example 08: Capstone Health Monitoring & Automated Alert Dispatcher
Python Learning Hub - Professional Capstone Project
"""


class AutomatedHealthMonitor:
    """Komponen pemantau ambang batas dan pemicu peringatan insiden otomatis."""

    @staticmethod
    def evaluate_node_health(node_id: str, temperature_c: float, cpu_load_pct: float) -> dict[str, str]:
        if temperature_c > 75.0 or cpu_load_pct > 90.0:
            severity = "CRITICAL"
            action = "Kirim notifikasi pager ke tim Network Operations Center"
        elif temperature_c > 60.0 or cpu_load_pct > 75.0:
            severity = "WARNING"
            action = "Jadwalkan inspeksi rutin pada sistem pendingin"
        else:
            severity = "NORMAL"
            action = "Operasional optimal"

        return {
            "node_id": node_id,
            "severity": severity,
            "action": action,
        }


def main() -> None:
    print("Mengevaluasi Kesehatan Perangkat & Peringatan Otomatis (Capstone Layer 8):\n")
    devices = [
        ("CORE-ROUTER-01", 52.0, 45.0),
        ("DIST-SWITCH-02", 68.0, 78.0),
        ("EDGE-ANTENNA-03", 82.5, 94.0),
    ]

    for dev_id, temp, cpu in devices:
        res = AutomatedHealthMonitor.evaluate_node_health(dev_id, temp, cpu)
        print(f" -> [{res['node_id']}] Tingkat Bahaya: {res['severity']} | Tindakan: {res['action']}")


if __name__ == "__main__":
    main()
