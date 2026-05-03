import heapq

class DataFlow:
    def __init__(self):
        self.small, self.large = [], []

    def add_data(self, num: int) -> None:
        heapq.heappush(self.small, -1 *num)

        # check all elems in small is greater or equal to large
        if self.small and self.large and (-1* self.small[0] > self.large[0]):  
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        
        # check the length of small and large differs by at most 1
        if len(self.small) > len(self.large) + 1:
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        
        if len(self.large) > len(self.small) + 1:
            tmp =  heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * tmp)

    def find_median(self)-> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        
        if len(self.large) < len(self.small):
            return -self.small[0]

        if len(self.large) == len(self.small):
            return (self.large[0] + self.small[0]) /2
            

df = DataFlow()

df.add_data(3)
df.add_data(7)
df.add_data(1)
df.add_data(2)
df.add_data(12)
df.add_data(41)
df.add_data(56)

print(df.find_median())


