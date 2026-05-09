positions = {
    "AAPL": 50,
    "MSFT": -20,
    "TSLA": 10,
}

prices = {
    "AAPL": 100,
    "MSFT": 300,
    "TSLA": 800,
}

import heapq
def top_k_exposure(positions: dict[str, float], prices: dict[str, float], k: int)-> list[str]:
    heap = []
    res = []
    for symbol in positions:
        qty = positions[symbol]
        if symbol in prices:
            # portfolio[symbol] = abs(qty * prices[symbol])
            heapq.heappush(heap, (abs(qty * prices[symbol]), symbol))
        
        if len(heap) > k:
            heapq.heappop(heap)
    # for _ in range(k):
    #     val, symbol = heapq.heappop(heap)
    #     res.append(symbol)
    return [symbol for _, symbol in heap]

print(top_k_exposure(positions, prices, 2))
