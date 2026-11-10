import numpy as np

# Matriks fitur (4 observasi x 3 fitur)
X = np.array(
    [
        [28.4, 62.0, 18.2],
        [29.1, 60.5, 19.5],
        [36.5, 48.0, 45.2],
        [27.9, 64.1, 16.8],
    ],
    dtype=np.float64,
)

# Kalibrasi offset per kolom dengan broadcasting (4, 3) + (3,)
offset_kalibrasi = np.array([-0.5, 1.0, -2.0], dtype=np.float64)
X_calibrated = X + offset_kalibrasi

# Z-score normalization per kolom dengan keepdims=True -> shape (1, 3)
mean_col = np.mean(X_calibrated, axis=0, keepdims=True)
std_col = np.std(X_calibrated, axis=0, keepdims=True)
safe_std = np.where(std_col == 0, 1.0, std_col)
z_scores = (X_calibrated - mean_col) / safe_std

print("Mean per kolom :", np.round(mean_col.ravel(), 2))
print("Std per kolom  :", np.round(std_col.ravel(), 2))
print("Matriks Z-score:\n", np.round(z_scores, 3))
