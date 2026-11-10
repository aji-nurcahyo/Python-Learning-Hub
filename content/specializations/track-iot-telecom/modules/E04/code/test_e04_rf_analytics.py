import sys
from pathlib import Path
import pandas as pd

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from e04_01_rf_metrics_classification import classify_rsrp
from e04_02_drive_test_blindspots import diagnose_rf_issue
from e04_03_pathloss_link_budget import compute_fspl_db


def test_rf_classification_and_interference_diagnosis() -> None:
    assert classify_rsrp(-75.0) == "Excellent"
    assert classify_rsrp(-85.0) == "Good"
    assert classify_rsrp(-98.0) == "Mid-Cell"
    assert classify_rsrp(-110.0) == "Cell-Edge"

    assert diagnose_rf_issue(-83.5, 1.4) == "HIGH_INTERFERENCE"
    assert diagnose_rf_issue(-112.4, -1.2) == "CRITICAL_EDGE"
    assert diagnose_rf_issue(-76.5, 19.5) == "HEALTHY"


def test_drive_test_sinr_lower_than_snr_and_fspl_doubling() -> None:
    csv_path = CODE_DIR.parent / "datasets" / "drive_test_lte_measurements.csv"
    df = pd.read_csv(csv_path)
    assert (df["sinr_db"] <= df["snr_db"]).all()

    loss_1km = compute_fspl_db(1.0, 1800.0)
    loss_2km = compute_fspl_db(2.0, 1800.0)
    assert abs((loss_2km - loss_1km) - 6.02) < 0.05

