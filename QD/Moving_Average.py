prices = [10, 20, 30, 40, 50]
window = 3

# [20, 30, 40]

def Moving_Average(prices: list[float], window: int)-> list[int]:
    if window <= 0 or len(prices) < window:
        return []
    
    res = []
    cur_sum = sum(prices[:window])
    res.append(cur_sum / window)


    for i in range(window, len(prices)):
        cur_sum += prices[i] - prices[i - window]
        res.append(cur_sum / window)
    
    return res


print(Moving_Average(prices, window))