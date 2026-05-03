trades = [
    ("BUY", "AAPL", 10, 100),
    ("BUY", "AAPL", 5, 110),
    ("SELL", "AAPL", 8, 120),
]

# Buy 10 at 100 → cost = 1000
# Buy 5 at 110 → total qty = 15, total cost = 1550
# Average cost = 103.33

# Sell 8 at 120
# Realised PnL = 8 * (120 - 103.33) = 133.33

# Remaining qty = 7
# Remaining cost = 7 * 103.33 = 723.33

from collections import defaultdict

class Trades:
    Trade = tuple[str, str, int, int]

    def __init__(self):
        self.qty_dict = defaultdict(int)
        self.cost_dict = defaultdict(float)
        self.realised_pnl = defaultdict(float)

    def Buy_Sell(self, trades: Trade):
        bs, symbol, qty, price = trades 

        if bs == "BUY":
            self.qty_dict[symbol] += qty
            self.cost_dict[symbol] += qty * price

        if bs == "SELL":
            if qty > self.qty_dict[symbol]:
                raise ValueError("Cannot sell more than current position")

            avg_cost = self.cost_dict[symbol] / self.qty_dict[symbol]

            self.realised_pnl[symbol] = qty * (price - avg_cost)

            self.qty_dict[symbol] -= qty
            self.cost_dict[symbol] -= qty * avg_cost


    def summary(self, symbol: str):
        avg_cost = self.cost_dict[symbol] / self.qty_dict[symbol] if self.qty_dict[symbol] != 0 else 0
        
        return {
            "position": self.qty_dict[symbol],
            "average_cost": avg_cost,
            "remaining_cost": self.cost_dict[symbol],
            "realised_pnl": self.realised_pnl[symbol],
        }

book = Trades()

for trade in trades:
    book.Buy_Sell(trade)

print(book.summary("AAPL"))