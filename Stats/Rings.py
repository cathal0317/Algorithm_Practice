import random
import numpy as np

# PART 1

def simulate_trial():
    lst = []
    for i in range(3):
        # randomly choose A, B, or C according to respective probabilities
        val = np.random.choice(["A", "B", "C"], p=[1/9, 3/9, 5/9])
        lst.append(val)
    return lst

# counter number of successes
num_successes = 0

# simulate trial 100,000 times
for i in range(100000):
    trial = simulate_trial()
    # see if there are three unique values -> A, B, C
    if len(np.unique(trial)) == 3:
        # if so, increase the number of successes by 1
        num_successes += 1

# expected proportion around 90/729 or 0.1234
print(num_successes/100000)