class Transactions:
    def k_transactions(self, records: list[float], k) -> float:
        if not records:
            return 0.0

        buy = [float('-inf')] *  (k+1)
        sell = [0] * (k+1)

        for price in records:
            for t in range(1, k+1):
                buy[t] = max(buy[t], sell[t-1] -1 * price)
                sell[t] = max(sell[t], buy[t] + price)
                print(buy)
                print(sell)

        return sell[k]
    
tr = Transactions()
print(tr.k_transactions([1, 3, 5, 1, 6 , 9],2))

        







