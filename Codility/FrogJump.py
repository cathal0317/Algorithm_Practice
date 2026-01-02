# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.

# Write a function:

# def solution(X, Y, D)

# that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

# For example, given:

#   X = 10
#   Y = 85
#   D = 30

import math

def solution(X, Y, D):
    # Implement your solution here
    dist = Y - X
    return math.ceil(dist/D)