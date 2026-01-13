# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

def solution(A, B, K):
    # Implement your solution here
    res = []
    if K%2 ==0 and A%2 == 0:
        for num in range(A,B+1,2):
            if num % K == 0:
                res.append(num)

    elif K%2 ==0 and A%2 == 1:
        for num in range(A+1,B+1,2):
            if num % K == 0:
                res.append(num)
    elif K%2 == 1:
        for num in range(A,B+1):
            if num % K == 0:
                res.append(num)
    elif K>B:
        return 0
    return len(res)