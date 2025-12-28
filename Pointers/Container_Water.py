# Container With Most Water
# Solved 
# You are given an integer array heights where heights[i] represents the height of the ith bar


# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxar = 0
        while l < r:
            length = abs(r-l)
            area = (length * min(heights[l],heights[r])) 
            maxar = max(maxar, area)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
                
        return maxar