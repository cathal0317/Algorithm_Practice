# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001
# content_copy
#  and contains a binary gap of length 2. The number 529 has binary representation 1000010001
# content_copy
#  and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100
# content_copy
#  and contains one binary gap of length 1. The number 15 has binary representation 1111
# content_copy
#  and has no binary gaps. The number 32 has binary representation 100000
# content_copy
#  and has no binary gaps.


def solution(N):
    # Implement your solution here
    converted = bin(N)

    indices = []
    for i, ch in enumerate(converted[2:]):
        if ch == "1":
            indices.append(i)

    if len(indices) < 2:
        return 0

    diff = []
    for curr, nxt in zip(indices, indices[1:]):
        diff.append(nxt-curr-1)

    return max(diff)







