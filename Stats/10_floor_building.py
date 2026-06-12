import random

def simulate_trial() -> int:
    # each of the 12 people pick a random floor between 1 and 10
    floors = [random.randint(1, 10) for _ in range(12)]

    # count the number of unique floors the elevator must stop at
    return len(set(floors))

# list of the number of floors the elevator stopped at for each trial
res = [simulate_trial() for _ in range(10_000)]

# compute the average, or expected number of floors the elevator needed to stop at over all 10,000 trials
print(sum(res) / len(res))