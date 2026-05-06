orders = [
    ("BUY", 100, 5),
    ("BUY", 101, 3),
    ("SELL", 105, 2),
    ("SELL", 104, 4),
]

class OrderBook:
    data = (str, float, int)

    def __init__(self):
        self.bid = {}
        self.ask = {}
    def Best_Bid(self, orders: list[data])-> tuple[float, float]:
    

        for bs, price, qty in orders:
            if bs == "BUY":
                self.bid[price] = qty
            
            else:
                self.ask[price] = qty
        return (max(self.bid), min(self.ask))

    def Cancel_Order(self, cancel_order: list[data]):
        bs, price, qty = cancel_order

        if bs == "BUY" and price in self.bid:
            self.bid.remove()


ob = OrderBook()
print(ob.Best_Bid(orders))