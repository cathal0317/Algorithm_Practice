from typing import List
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations, product
from math import gcd, lcm, ceil, floor, sqrt

# X is the list of non-empty list of integres
X = [1,2,3,4]

def and_list(X:list):
    res = X[0]
    for i in range(1,len(X)):
        res &= X[i]
    return res


def xor_list(X:list):
    res = X[0]
    for i in range(1,len(X)):
        res ^= X[i]
    return res

def f(X:list):
    if not X:
        return 0
    n = len(X)
    # First find all contiguous sublists of X
    res = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            res.append(X[start:end])
    print(res)
    # Then use xor_list of all its elements
    res_XOR = []
    for item in res:
        res_XOR.append(xor_list(item))
    print(res_XOR)


    # Finally and_list to each elements 
    return and_list(res_XOR)


print(f(X))



# def f_eff(X: list):
#     if len(X) % 2 ==0:
#         return 0
#     else:
#         odd_indexed = []
#         for i in range(0,len(X), 2):
#             odd_indexed.append(X[i])

#         # return and_list(t)


