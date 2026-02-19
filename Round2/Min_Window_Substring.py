# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        sdict, tdict = defaultdict(int),defaultdict(int)  

        for c in t:
            tdict[c] += 1

        have, need = 0, len(tdict)

        l = 0
        res, lenres = [-1, -1], float('inf')

        for r in range(len(s)):
            c = s[r]
            sdict[c] += 1

            if c in tdict and sdict[c] == tdict[c]:
                have+=1 
            
            while have == need:
                if (r-l+1) < lenres:
                    res = [l , r] 
                    lenres = (r-l+1)
                sdict[s[l]] -= 1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l: r+1] if lenres != float('inf') else ""