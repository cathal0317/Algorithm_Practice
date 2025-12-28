# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res, maxf = 0,0

        for r in range (len(s)):
            count[s[r]] = 1+ count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l +1) - maxf >k:
                count[s[l]] -= 1 
                l+=1
            res = max(res, r-l +1)
        return res