# You are given two binary strings s and t​​​​​​​, each of length n.

# You may rearrange the characters of t in any order, but s must remain unchanged.

# Return a binary string of length n representing the maximum integer value obtainable by taking the bitwise XOR of s and rearranged t.

 

# Example 1:

# Input: s = "101", t = "011"

# Output: "110"

# Explanation:

# One optimal rearrangement of t is "011".
# The bitwise XOR of s and rearranged t is "101" XOR "011" = "110", which is the maximum possible.
# Example 2:

# Input: s = "0110", t = "1110"

# Output: "1101"

# Explanation:

# One optimal rearrangement of t is "1011".
# The bitwise XOR of s and rearranged t is "0110" XOR "1011" = "1101", which is the maximum possible.
# Example 3:

# Input: s = "0101", t = "1001"

# Output: "1111"

# Explanation:

# One optimal rearrangement of t is "1010".
# The bitwise XOR of s and rearranged t is "0101" XOR "1010" = "1111", which is the maximum possible.

from collections import Counter

class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        count = Counter(t)
        res = []

        for char in s:
            opposite = "1" if char == "0" else "0"

            if count[opposite] > 0:
                res.append("1")
                count[opposite] -= 1
            else:
                res.append("0")
                count[char] -= 1

        return "".join(res)