from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def build_region_boxplot(df: pd.DataFrame, out_path: Path) -> Path:
    fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
    sns.boxplot(data=df, x="region", y="latency_ms", ax=ax)
    ax.set_title("Distribusi Latensi per Wilayah")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path


def test_boxplot_renders_nonempty_png(tmp_path: Path) -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "telecom_qos_kpi.csv"
    df = pd.read_csv(csv_path)
    out = build_region_boxplot(df, tmp_path / "boxplot.png")
    assert out.exists()
    assert out.stat().st_size > 3000

