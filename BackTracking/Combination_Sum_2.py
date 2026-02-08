# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: candidates = [9,2,2,4,6,1,5], target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i==len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res