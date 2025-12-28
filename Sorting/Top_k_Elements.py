# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ndict = defaultdict(int)
        for num in nums:
            ndict[num] += 1 
        
        heap = []

        for num in ndict.keys():
            heapq.heappush(heap, (ndcit[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return out