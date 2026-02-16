# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

# Example 1:

# Input: s = "aab"

# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"

# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res , part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            
            for j in range(i, len(s)):
                if self.Pali(s,i, j):
                    part.append(s[i : j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
    
    def Pali(self,s, l ,r):
        
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l, r = l+1, r-1
        return True
