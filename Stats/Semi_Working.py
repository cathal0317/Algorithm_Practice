import random

generate = lambda: random.uniform(0, 3)

valid_trial = 0
num_iters = 100_000
for i in range(num_iters):

    a = generate()
    b = generate()
    c = generate()

    smallest = min(a, b, c)
    if smallest > 1 and smallest < 2:
        valid_trial += 1

#expecting ~ 0.259
print(valid_trial/num_iters)