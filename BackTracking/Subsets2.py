# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,1]

# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
# Example 2:

# Input: nums = [7,7]

# Output: [[],[7], [7,7]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            backtrack(i+1, sub)
            sub.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            backtrack(i+1, sub)
        
        backtrack(0, [])
        return res


