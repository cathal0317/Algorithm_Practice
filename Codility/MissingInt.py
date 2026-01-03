# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    # Implement your solution here
    N = len(A)
    count = [False] * (N+1)

    for num in A:
        if 1<= num <= N+1:
            count[num-1] = True
        
    for i in range(len(count)):
        if count[i] == False:
            return i + 1