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


We want to find P(D | P)

P(D) = 0.01

P(P | D) = 0.99
=> P(N | D) = 0.01
by law of total probability


P(N | not D) = 0.95
 => P(P | not D) = 0.05

P(D | P) = P(P | D) * P(D) / P(P)

P(P) = P(P | D)* P(D) + P(P | not D) * P(not D)
     = 0.99 * 0.01 + 0.05 * 0.99 = 0.0594

= 0.99 * 0.01 / 0.0594 = 0.167