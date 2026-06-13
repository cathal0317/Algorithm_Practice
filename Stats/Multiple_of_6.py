import random
from typing import Callable

roll_dice: Callable [[None], int] = lambda: random.randrange(1,7)

total_rolls = 0
num_iters = 10_000
#simulates rolling until we get a multiple of 6 num_iters times
for i in range(num_iters):

   run_sum = roll_dice()
   rolls = 1

   #reroll until the sum is a multiple of 6
   while run_sum % 6 != 0:
      run_sum += roll_dice()
      rolls += 1

   total_rolls += rolls

#expecting value close to 6.00
print(total_rolls/num_iters)