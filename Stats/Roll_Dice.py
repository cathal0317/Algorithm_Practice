import random

roll_dice = lambda: random.randint(1, 6)

valid_cases = 0
num_iters = 100_000
for i in range(num_iters):

    seen_faces = set()
    while(True):

        roll = roll_dice()
        seen_faces.add(roll)

        if roll % 2 == 1 and len(seen_faces) < 4:
            break

        if len(seen_faces) == 6:
            valid_cases += 1
            break

print(valid_cases / num_iters)