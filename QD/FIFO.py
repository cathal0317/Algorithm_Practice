trades = [
    ("BUY", 10, 100),
    ("BUY", 5, 110),
    ("SELL", 12, 120),
]

data = (str, float, float)

from collections import deque

def Matching_FIFO(trades: list[data])-> float:
    queue = deque()
    pnl = 0

    for bs, qty, price in trades:

        if bs == "BUY":
            queue.append([qty, price])

        if bs == "SELL":
            while qty >0:
                if queue:
                    buy_qty, buy_price = queue[0]

                    if buy_qty <= qty:
                        pnl += buy_qty * (price - buy_price)
                        qty -= buy_qty
                        queue.popleft()
                    else:
                        pnl += qty * (price - buy_price)
                        queue[0][0] -= qty
                        qty = 0
                else:
                    print("You cant sell more than what you own.")
                
    return pnl, list(queue)
print(Matching_FIFO(trades))