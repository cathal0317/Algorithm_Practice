# For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

# val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

# (Assume that the sum of zero elements equals zero.)

# For a given array A, we are looking for such a sequence S that minimizes val(A,S).

# Write a function:

# def solution(A)

# that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

# For example, given array:

#   A[0] =  1
#   A[1] =  5
#   A[2] =  2
#   A[3] = -2
# your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..20,000];
# each element of array A is an integer within the range [−100..100].

def solution(A):
    # Implement your solution here
    A = [abs(a) for a in A]
    total = sum(A)

    cnt = [0] * 101
    for a in A:
        cnt[a] += 1

    dp = [-1] * (total +1)
    dp[0] = 0

    for v in range(1,101):
        if cnt[v] == 0:
            continue
        for s in range(1,total+1):
            if dp[s] >= 0:
                dp[s] = cnt[v]
            elif s>=v and dp[s-v]>0:
                dp[s] = dp[s-v] - 1

    result = total
    for s in range(1,total//2 +1):
        result = min(result,total-2*s)

    return result