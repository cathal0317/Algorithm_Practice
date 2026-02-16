# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ndicts = defaultdict(int)
        ndictt = defaultdict(int)

        for i in s:
            ndicts[i] += 1
        for j in t:
            ndictt[j] += 1
        
        return ndictt == ndicts