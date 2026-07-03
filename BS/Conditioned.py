import random

roll_dice = lambda: random.randint(1,6)

sequence_lengths = []
num_iters = 10_000
for i in range(num_iters):

    sequence = []
    while(True):

        sequence.append(roll_dice())

        if sequence[-1] == 5:
            break
        elif sequence[-1] == 6:
            sequence_lengths.append(len(sequence))
            break

print(sum(sequence_lengths)/len(sequence_lengths))