import random

roll_dice = lambda: random.randint(1, 6)

results = []
num_iters = 10_000
for i in range(num_iters):

    highest = 0
    while(True):

        roll = roll_dice()
        highest = max(highest, roll)

        if roll == 4:
            break

    results.append(highest)

print(sum(results) / num_iters)