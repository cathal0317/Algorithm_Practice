trades = [
    {"symbol": "AAPL", "pnl": 100},
    {"symbol": "MSFT", "pnl": -50},
    {"symbol": "AAPL", "pnl": 200},
    {"symbol": "GOOG", "pnl": 300},
    {"symbol": "MSFT", "pnl": 150},
]

## input is dictionary so nee to think about how i am going to use its key,val
from collections import defaultdict
import heapq

def TopPnL(trades: list[dict], k: int) -> list[tuple[str, float]]:
    #if k >= len(trades):
    pnl_map = defaultdict(float)

    res = []
    for t in trades:
        symbol = t["symbol"]
        pnl = t["pnl"]
        pnl_map[symbol] = pnl_map[symbol] + pnl

    sorted_pnl = sorted(pnl_map.items(), key=lambda x:x[1], reverse = True)
    return sorted_pnl[:k]

print(TopPnL(trades, 1))

def Heap_pnl(trades, k):
    pnl_map = defaultdict(float)

    for t in trades:
        symbol = t["symbol"]
        pnl = t["pnl"]
        pnl_map[symbol] = pnl_map[symbol] + pnl

    return heapq.nlargest(k, pnl_map.items(), key=lambda x: x[1])

print(Heap_pnl(trades, 2))