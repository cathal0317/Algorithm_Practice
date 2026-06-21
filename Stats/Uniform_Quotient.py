import random

quotients = []
num_iters = 10_000
for i in range(num_iters):

    a = random.uniform(0, 1)
    b = random.uniform(0, 1)

    quotients.append(a/b)

in_bounds = len([q for q in quotients if q >= 1 and q <= 3])
#expecting answer close to 1/3
print(in_bounds/num_iters)