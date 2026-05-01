prices = [100, 120, 90, 110, 80]

def Drawdown(prices):
    if not prices:
        return 0
    
    curmax = prices[0]
    res = 0

    for p in prices:
        if p > curmax:
            curmax = p
        if curmax != 0:
            drawdown = (p - curmax) / curmax
            res = min(res, drawdown)

    return res

print(Drawdown(prices))
