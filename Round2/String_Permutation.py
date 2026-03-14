# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1dict, s2dict = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1dict[ord(s1[i]) - ord('a')] += 1
            s2dict[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1dict[i] == s2dict[i] else 0)
        
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2dict[idx] += 1

            if s1dict[idx] == s2dict[idx]:
                matches += 1
            elif s1dict[idx] + 1 == s2dict[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2dict[idx] -= 1
            if s1dict[idx] == s2dict[idx]:
                matches += 1
            elif s1dict[idx] - 1 == s2dict[idx]:
                matches -= 1
            l += 1
        return matches == 26

            
