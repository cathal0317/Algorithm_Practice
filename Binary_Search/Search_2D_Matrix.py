# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m ,n = len(matrix), len(matrix[0])
        r, c = 0, n -1 

        while r < m and c >= 0:
            if target < matrix[r][c]:
                c-=1
            elif target > matrix[r][c]:
                r+=1
            else:
                return True
        return False