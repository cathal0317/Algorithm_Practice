# Trapping Rain Water
# Solved 
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        area = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                area += maxl - height[l]

            else:
                r-=1
                maxr = max(maxr, height[r])
                area += maxr - height[r]
        return area
