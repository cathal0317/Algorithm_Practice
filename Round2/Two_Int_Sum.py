# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2] 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l ,r = 0, len(numbers) -1 
        while l < r:
            ans = numbers[l] + numbers[r]
            if target > ans:
                l+=1
            if target < ans:
                r-=1 
            if target == ans:
                return [l+1,r+1]