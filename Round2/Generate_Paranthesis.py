# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(s, openn, closen):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if openn < n:
                dfs(s + '(', openn + 1, closen)
            if closen < openn:
                dfs(s + ')', openn, closen + 1)
        dfs("", 0 ,0)
        
        return res
            
            
            
            