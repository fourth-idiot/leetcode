class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        numRows, numCols = len(grid), len(grid[0])
        k %= (numRows * numCols)
        for _ in range(k):
            for i in range(numRows - 1, -1, -1):
                for j in range(numCols - 1, -1, -1):
                    if((i == (numRows - 1)) and (j == (numCols - 1))):
                        lastVal = grid[i][j]
                    if((j == 0) and (i == 0)):
                        grid[i][j] = lastVal
                    elif(j == 0):
                        grid[i][j] = grid[i - 1][numCols - 1]
                    else:
                        grid[i][j] = grid[i][j - 1]
        return grid