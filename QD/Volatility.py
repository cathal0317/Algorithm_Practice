prices = [100, 102, 101, 105, 107, 106]
window = 3

import math

def Rolling_Volatility(prices: list[int], window: int)->list[float]:
    returns = []

    for i in range(1, len(prices)):
        r = (prices[i] - prices[i -1])/ prices[i-1] 
        returns.append(r)
    
    res = []

    # for start in range(len(returns)-window +1):
    #     chunk = returns[start:start+window]

    #     mean = sum(chunk) / window
    #     var = sum((x-mean)**2 for x in chunk) / window
    #     std = math.sqrt(var)

    #     res.append(std)

    sum_x = sum(returns[:window])
    sum_x2 = sum(x * x for x in returns[:window])

    for start in range(len(returns)-window+1):
        mean = sum_x/window
        var = (sum_x2/window) - mean ** 2
        
        res.append(math.sqrt(var))

        if start + window < len(returns):
            old = returns[start]
            new = returns[start+window]

            sum_x -= old
            sum_x += new

            sum_x2 -= old * old
            sum_x2 += new *new
    return res

print(Rolling_Volatility(prices, 3))