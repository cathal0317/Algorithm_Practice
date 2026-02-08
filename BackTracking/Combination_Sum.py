# Combination Sum
# Solved 
# Medium
# Topics
# Company Tags
# Hints
# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input:
# nums = [2,5,6,9]
# target = 9

# Output: [[2,2,5],[9]]

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total >target or len(nums)<= i:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total+ nums[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0, [], 0)
        return res