# Valid Anagram
# Solved 
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = defaultdict(int)
        tdict = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(s):
            sdict[s[i]] = 1 + sdict.get(s[i], 0)
            tdict[s[i]] = 1 + tdict.get(s[i], 0)
            
        return sdict == tdict 

