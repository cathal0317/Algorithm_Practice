# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.



# Example 1:

# Input: digits = "34"

# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# Example 2:

# Input: digits = ""

# Output: []

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def dfs(i, curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return
            
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curstr + c)
        if digits:
            dfs(0, "")
        return res
