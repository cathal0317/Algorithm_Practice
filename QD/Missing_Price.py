prices = [
    ("AAPL", 100),
    ("AAPL", None),
    ("AAPL", 103),
    ("AAPL", None),
]


def Impute_Missing_Price(prices)-> list[tuple[str, int]]:
    res = []
    last_seen = {}

    for symbol, price in prices:
        if price is not None:
            last_seen[symbol] = price
            res.append((symbol, price))
        
        else:
            if symbol in last_seen:
                res.append((symbol, last_seen[symbol]))
            else:
                res.append((symbol, None))

            
    return res
    
print(Impute_Missing_Price(prices))