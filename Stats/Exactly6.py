import random
from typing import Callable
from collections import Counter

roll_dice: Callable[[None], int] = lambda: random.randrange(1, 7, 1)

def simulation() -> bool:
    # Roll the dice 36 times
    rolls = [roll_dice() for _ in range(36)]
    # Count how many times each number appeared
    counts = Counter(rolls)
    # Check that each number appeared 6 times
    return len(counts.keys()) == 6 and all([count == 6 for count in counts.values()])

iterations = 100_000
probability = sum([simulation() for _ in range(iterations)]) / iterations
print(f"The probability that each number appears exactly six times is: {probability}")