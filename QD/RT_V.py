positions = {"AAPL": 10, "MSFT": 5, "GOOG": -2}

price_updates = [
    ("AAPL", 100),
    ("MSFT", 200),
    ("GOOG", 300),
    ("AAPL", 105),
    ("GOOG", 280),
]

# AAPL 100 → 1000
# MSFT 200 → 2000
# GOOG 300 → 1400
# AAPL 105 → 1450
# GOOG 280 → 1490

## So the naive approach will be to have separate memeory storage for each symbols and sum up the dictionary value stored in each symbol. However this is 
## slightly inefficient as the runtime can be optimised using deducting the previous contribution of past value.

def PTF_Val(positions: dict[str, int], price_updates) -> list[float]:
    total = 0
    prices = {}
    res = []

    for symbol, price in price_updates:
        qty = positions.get(symbol, 0)
        if symbol in prices:
            old_contribution = prices[symbol]
            total -= qty * old_contribution
            
        prices[symbol] = price
        total += price * qty

        res.append(total)
    
    return res

print(PTF_Val(positions,price_updates))