events = [
    ("NEW", "order1", 100),
    ("FILL", "order1", 30),
    ("FILL", "order1", 50),
    ("CANCEL", "order1"),
    ("NEW", "order2", 200),
    ("FILL", "order2", 200),
]

from collections import defaultdict

class LifeCycle:
    def __init__(self):
        self.order_book = defaultdict(int)
        self.res = defaultdict(dict)

    def new_order(self, order_id: str, init_qty: int) :
        self.order_book[order_id] = init_qty
        self.res[order_id] = {"initial_qty" : self.order_book[order_id],
                              "filled": 0,
                              "remaining": self.order_book[order_id],
                              "status": "NEW"}

    def fill_order(self, order_id: str, qty: int):
        if self.res[order_id]["remaining"] > qty:
            self.res[order_id]["filled"] += qty
            self.res[order_id]["remaining"] -= qty
            self.res[order_id]["status"] = "FILL"

        elif self.res[order_id]["remaining"]  == qty:
            self.res[order_id]["remaining"] -= qty
            self.res[order_id]["filled"] += qty
            self.res[order_id]["status"] = "PARTIALLY_FILLED"

        else:
            return
        
    def cancel_order(self, order_id: str):
        self.res[order_id]["status"] = "CANCELLED"

    def process_order(self, events)->dict[dict]:
        for item in events:
            if len(item) == 3:
                status, id, qty = item
                if status == "NEW":
                    self.new_order(id, qty)

                elif status == "FILL":
                    self.fill_order(id, qty)

            else: 
                _, id = item
                self.cancel_order(id)

        return self.res

ot = LifeCycle()
print(ot.process_order(events))