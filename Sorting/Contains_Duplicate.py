# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
from typing import List
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ndict = defaultdict(int)
        for num in nums:
            if num not in ndict:
                ndict[num] = 1
            else:
                ndict[num] += 1

            if ndict[num] > 1:
                return True
            
        return False

print(Solution().hasDuplicate([1, 2, 3, 3]))