# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in 
# O
# (
# l
# o
# g
# n
# )
# O(logn) time.

# Example 1:

# Input: nums = [-1,0,2,4,6,8], target = 4

# Output: 3

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0, len(nums) -1 

        while l < r:
            m = l + (r-l) // 2
            if nums[m] >= target:
                r = m 
            elif nums[m] < target:
                l = m +1
        return l if (l <len(nums) and nums[l] == target) else -1