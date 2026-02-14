# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [7]

# Output: [[7]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)== 0:
            return [[]]
        
        res = []
        perms = self.permute(nums[1:])
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        
        return res