prices = [100, 102, 101, 105, 107, 106]
window = 3

import math

def Rolling_Volatility(prices: list[int], window: int)->list[float]:
    returns = []

    for i in range(1, len(prices)):
        r = (prices[i] - prices[i -1])/ prices[i-1] 
        returns.append(r)
    
    res = []
    for start in range(len(returns)-window +1):
        chunk = returns[start:start+window]

        mean = sum(chunk) / window
        var = sum((x-mean)**2 for x in chunk) / window
        std = math.sqrt(var)

        res.append(std)

    return res

print(Rolling_Volatility(prices, 3))