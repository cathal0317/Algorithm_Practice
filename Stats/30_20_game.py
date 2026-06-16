import random
from typing import Callable

earnings = []
roll_dice: Callable[[int], int] = lambda num_sides: random.randrange(1, num_sides+1)

for i in range(100000):
    philip_roll = roll_dice(30)
    brandon_roll = roll_dice(20)

    if philip_roll > brandon_roll:
        earnings.append(philip_roll)
    else:
        earnings.append(-brandon_roll)

#expecting close to 8.15
print(sum(earnings)/len(earnings))