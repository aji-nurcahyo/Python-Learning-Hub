from pathlib import Path
import numpy as np


def zscore_normalize(matrix: np.ndarray) -> np.ndarray:
    mean = np.mean(matrix, axis=0, keepdims=True)
    std = np.std(matrix, axis=0, keepdims=True)
    safe_std = np.where(std == 0, 1.0, std)
    return (matrix - mean) / safe_std


def test_dataset_load_and_shape() -> None:
    csv_path = Path(__file__).resolve().parent.parent / "datasets" / "sensor_matrix.csv"
    data = np.genfromtxt(csv_path, delimiter=",", skip_header=1, dtype=np.float64)
    assert data.shape == (12, 5)
    assert data.dtype == np.float64


def test_zscore_zero_mean_unit_variance() -> None:
    sample = np.array([[10.0, 5.0], [20.0, 5.0], [30.0, 5.0]], dtype=np.float64)
    norm = zscore_normalize(sample)
    assert np.allclose(np.mean(norm, axis=0), [0.0, 0.0])
    assert np.isclose(np.std(norm[:, 0]), 1.0)
    assert np.allclose(norm[:, 1], [0.0, 0.0, 0.0])


def test_broadcasting_subtraction() -> None:
    mat = np.ones((4, 3), dtype=np.float64)
    vec = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    res = mat * vec
    assert res.shape == (4, 3)
    assert np.allclose(res[0], [1.0, 2.0, 3.0])

