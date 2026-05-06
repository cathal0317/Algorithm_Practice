positions = {
    "AAPL": 10,
    "MSFT": 5,
    "GOOG": -2
}

price_updates = [
    ("AAPL", 100),
    ("MSFT", 200),
    ("GOOG", 300),
    ("AAPL", 105),
    ("GOOG", 280),
]

from collections import defaultdict

def RT_Portfolio(positions: dict[str, float], price_updates:list[tuple[str,float]]) -> list[float]:
    RT_dict = defaultdict(int)
    res = []

    for symbol, price in price_updates:
        if symbol in positions:
            RT_dict[symbol] = positions[symbol] * price
        
        total = sum(RT_dict.values())
        res.append(total)


    return res

print(RT_Portfolio(positions, price_updates))

def RT_Portfolio2(positions: dict[str, float], price_updates:list[tuple[str,float]]) ->list[float]:
    prices = {}
    total = 0
    res = []

    for symbol, new_price in price_updates:
        qty = positions.get(symbol, 0)

        if symbol in prices:
            old_price = prices[symbol]
            total -= qty * old_price
        
        prices[symbol] = new_price
        total += qty * new_price

        res.append(total)
    return res

print(RT_Portfolio2(positions, price_updates))
