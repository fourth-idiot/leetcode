import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])
        low, high = 0, (numRows * numCols) - 1
        while(low <= high):
            mid = (low + high) // 2
            row, col = divmod(mid, numCols)
            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] > target):
                high = mid - 1
            else:
                low = mid + 1
        return False
                