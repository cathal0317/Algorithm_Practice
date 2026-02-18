# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rset = set()
        total = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in rset:
                rset.remove(s[l])
                l+=1
            rset.add(s[r])
            total = max(total, r-l+1)
        return total