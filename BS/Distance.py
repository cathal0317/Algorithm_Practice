import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return None
        heap = []
        
        for point in points:
            x,y = point[0],point[1]
            distance = x**2 + y**2 
            heapq.heappush(heap, [distance, point])
            
        res = []
        
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            res.append(point)
        return res
            
            
            
             