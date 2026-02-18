# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ndict = defaultdict(int)
        l = 0

        res = 0
        maxf = 0
        for r in range(len(s)):
            ndict[s[r]] += 1
            maxf = max(maxf, ndict[s[r]])
            while (r-l+1) - maxf > k:
                ndict[s[l]] -= 1
                l+=1 
            res = max(res, r-l+1)
        return res
