# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()          
        count = 1
        longest = 1

        for prev, curr in zip(nums, nums[1:]):
            if curr == prev:
                continue
            elif curr == prev +1 :
                count+=1
            else:
                count = 1
            longest = max(longest, count)
        return longest