limits = {
    "AAPL": 100,
    "MSFT": 50,
} 

trades = [
    ("BUY", "AAPL", 30),
    ("BUY", "AAPL", 80),
    ("SELL", "MSFT", 60),
]

def Risk_Limit_Check(limits: dict[str,int], trades: list[tuple[str,str,int]])->list[tuple[str, int, bool]]:
    res = []
    trade_record = {}
    

    for bs, symbol, qty in trades:
        tf = True
        if bs == "BUY":
            trade_record[symbol] = trade_record.get(symbol, 0) + qty

            if limits[symbol] < trade_record[symbol]:
                tf = False
            res.append((symbol, trade_record[symbol], tf))
        else:
            trade_record[symbol] = trade_record.get(symbol, 0) - qty

            if limits[symbol] < trade_record[symbol]:
                tf = False
            res.append((symbol, trade_record[symbol], tf))
    return res

print(Risk_Limit_Check(limits,trades ))