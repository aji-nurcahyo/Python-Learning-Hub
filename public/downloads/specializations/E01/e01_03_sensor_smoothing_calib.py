def apply_linear_calibration(raw_readings: list[float], gain: float = 1.02, offset: float = -0.4) -> list[float]:
    return [round(raw * gain + offset, 3) for raw in raw_readings]


def exponential_moving_average(values: list[float], alpha: float = 0.35) -> list[float]:
    if not values:
        return []
    smoothed = [values[0]]
    for x in values[1:]:
        smoothed.append(round(alpha * x + (1.0 - alpha) * smoothed[-1], 3))
    return smoothed


if __name__ == "__main__":
    raw_temp = [28.1, 29.8, 28.3, 32.5, 28.6, 28.4]
    calibrated = apply_linear_calibration(raw_temp)
    ema = exponential_moving_average(calibrated, alpha=0.35)

    print("Pembacaan mentah :", raw_temp)
    print("Ter-kalibrasi    :", calibrated)
    print("EMA smoothed     :", ema)
