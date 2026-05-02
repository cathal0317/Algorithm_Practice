values = [100, 110, 105, 120, 90, 95, 80, 130]


# Peak = 120
# Trough = 80
# Drawdown = (120 - 80) / 120 = 33.3%

def MaxDown(values: list[float]):
    if not values:
        return None

    peak = values[0]
    maxdd = 0.0

    best_peak = values[0]
    best_trough = values[0]

    for val in values:
        if val > peak:
            peak = val

        if peak != 0:
            drawdown = (peak - val) / peak

            if drawdown > maxdd:
                maxdd = drawdown
                best_peak = peak
                best_trough = val

    return best_peak, best_trough, maxdd

print(MaxDown(values))