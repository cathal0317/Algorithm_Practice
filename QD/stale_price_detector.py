updates = [
    ("AAPL", 100, 1),
    ("MSFT", 200, 2),
    ("AAPL", 101, 5),
    ("GOOG", 300, 10),
]

data = (str, float, int)
def find_stale(updates: list[data], current_time: int, T: int) -> list[str]:
    res = []
    for update in updates:
        symbol, _, time = update
        if (current_time>time) and (current_time - time) >= T:

            if symbol in res:
                continue
            res.append(symbol)

        else:
            continue

    return res

print(find_stale(updates, 12,5))