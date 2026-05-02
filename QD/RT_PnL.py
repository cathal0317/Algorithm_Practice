positions = {
    "AAPL": 10,
    "MSFT": 5,
    "GOOG": -2
}

initial_prices = {
    "AAPL": 100,
    "MSFT": 200,
    "GOOG": 300
}

price_updates = [
    ("AAPL", 105),
    ("MSFT", 190),
    ("GOOG", 280),
    ("AAPL", 110),
]

def RT_PnL(positions: dict[str, float], initial_prices: dict[str, float], price_updates: list[tuple[str,float]]) -> list[float]:
    pnl = 0
    prices = {}
    res = []

    for symbol, price in price_updates:
        qty = positions.get(symbol, 0)

        if symbol in prices:
            old_price = prices[symbol]
            pnl -= qty * old_price

        prices[symbol] = (price - initial_prices[symbol])
        pnl += qty * prices[symbol]

        res.append(pnl)

    return res

print(RT_PnL(positions, initial_prices, price_updates))


