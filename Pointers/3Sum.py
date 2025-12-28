# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if num >0:
                break
            if i>0 and num == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                tsum = num + nums[left] + nums[right]
                if tsum >0:
                    right -=1 
                elif tsum < 0:
                    left += 1
                else:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
        return res