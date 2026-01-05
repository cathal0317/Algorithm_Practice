# An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 12
# There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

# For example, given array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 12
# the function should return 4, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..1,000];
# each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
    # Implement your solution here
    N = len(A)
    A = sorted(A)
    if N < 3:
        return 0

    count = 0

    for k in range(2,N):
        i =0 
        j =k - 1
        while i<j:
            if A[k] < A[i] + A[j]:
                count+=(j-i)
                j -=1 
            else:
                i+=1
    return count






