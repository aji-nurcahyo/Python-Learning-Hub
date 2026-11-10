import numpy as np

# Bobot komposit kesehatan jaringan untuk [suhu_norm, loss_norm, latensi_norm]
readings_norm = np.array(
    [
        [0.10, 0.05, 0.12],
        [0.45, 0.30, 0.40],
        [0.95, 0.88, 0.92],
        [0.08, 0.04, 0.10],
    ],
    dtype=np.float64,
)

weights = np.array([0.20, 0.45, 0.35], dtype=np.float64)

# Dot product tervektorisasi untuk menghitung skor risiko tiap node
risk_scores = readings_norm @ weights

# Jarak Euclidean terhadap titik operasi ideal [0.0, 0.0, 0.0]
ideal_point = np.zeros(3, dtype=np.float64)
euclidean_dist = np.linalg.norm(readings_norm - ideal_point, axis=1)

print("Skor risiko node :", np.round(risk_scores, 4))
print("Jarak Euclidean  :", np.round(euclidean_dist, 4))
print("Persentil ke-75  :", round(float(np.percentile(risk_scores, 75)), 4))
