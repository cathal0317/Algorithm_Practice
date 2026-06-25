class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s:
            return ""
        best = ""
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                   left-= 1
                   right +=1
            return s[left+1:right]
        
        for i in range(n):
            odd = expand(i,i)
            even = expand(i, i+1)
            
            if len(odd) > len(best):
                best = odd

            if len(even) > len(best):
                best = even

        return best