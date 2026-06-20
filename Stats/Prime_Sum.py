import random

def simulate_trial():
    primes = [2, 3, 4, 5, 11, 13, 17, 19]
    elts = random.sample(primes, 2)
    if 2 in elts:
        return 0
    return 1

res = []

for i in range(100000):
    res.append(simulate_trial())

print(float(sum(res) / 100000)) 