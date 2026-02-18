# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:



# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0 
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]

        while l< r:
            if maxl<maxr:
                l+=1
                maxl = max(maxl, height[l])
                total += maxl - height[l]
            else:
                r-=1
                maxr = max(maxr, height[r])
                total += maxr - height[r]

        return total

